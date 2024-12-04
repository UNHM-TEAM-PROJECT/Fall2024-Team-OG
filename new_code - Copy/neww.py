# chatbot.py

import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_community.callbacks import get_openai_callback
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate
from langchain.schema import Document  
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

import sqlite3
from datetime import datetime
import logging
import glob
import re
from tqdm import tqdm
from typing import List, Dict, Any, Optional
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('chatbot.log')
    ]
)

# Load environment variables
API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = API_KEY

# Initialize Flask app
app = Flask(__name__)

class DocumentProcessor:
    def __init__(self, pdf_directory: str):
        self.pdf_directory = pdf_directory
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
            separators=["\n\n", "\n", ".", ";", ","]
        )

    def clean_content(self, text: str) -> str:
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        # Clean course codes
        course_patterns = {
            r'COMP\s*690': 'COMP690',
            r'COMP\s*890': 'COMP890',
            r'COMP\s*891': 'COMP891',
            r'COMP\s*892': 'COMP892',
            r'COMP\s*893': 'COMP893'
        }
        
        for pattern, replacement in course_patterns.items():
            text = re.sub(pattern, replacement, text)
        
        # Standardize formatting
        standardizations = [
            (r'Week (\d+)[:\s]*(\d+/\d+)', r'Week \1 (\2):'),
            (r'(?i)office\s*hours?:', 'Office Hours:'),
            (r'(?i)e-?mail:', 'Email:'),
            (r'(?i)prerequisites?:', 'Prerequisites:'),
            (r'(?i)requirements?:', 'Requirements:'),
            (r'(?i)grading criteria:', 'Grading Criteria:')
        ]
        
        for pattern, replacement in standardizations:
            text = re.sub(pattern, replacement, text)
            
        return text

    def process_documents(self) -> List[Document]:
        pdf_files = glob.glob(os.path.join(self.pdf_directory, "*.pdf"))
        if not pdf_files:
            raise Exception(f"No PDF files found in {self.pdf_directory}")
        
        all_documents = []
        for pdf_path in tqdm(pdf_files, desc="Processing PDFs"):
            try:
                loader = PyPDFLoader(pdf_path)
                pages = loader.load()
                
                for page in pages:
                    cleaned_content = self.clean_content(page.page_content)
                    chunks = self.text_splitter.split_text(cleaned_content)
                    
                    for chunk in chunks:
                        metadata = {
                            'source': os.path.basename(pdf_path),
                            'page': page.metadata.get('page', 0),
                            'type': self.determine_content_type(chunk)
                        }
                        all_documents.append(Document(
                            page_content=chunk,
                            metadata=metadata
                        ))
                
                logging.info(f"Successfully processed: {pdf_path}")
                
            except Exception as e:
                logging.error(f"Error processing {pdf_path}: {str(e)}")
                continue
        
        return all_documents

    def determine_content_type(self, text: str) -> str:
        if 'COMP' in text:
            return 'course_info'
        elif 'Week' in text and 'Scrum' in text:
            return 'schedule'
        elif any(term in text for term in ['Email:', 'Phone:', 'Office Hours:']):
            return 'contact_info'
        elif any(term in text for term in ['Prerequisites:', 'Requirements:']):
            return 'requirements'
        return 'general'

class ChatDatabase:
    def __init__(self, db_name='chat_history.db'):
        self.db_name = db_name
        
        self.init_db()

    def init_db(self):
        try:
            with sqlite3.connect(self.db_name) as conn:
                c = conn.cursor()
                c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='chat_history' ''')

                if c.fetchone()[0] == 0:
                        c.execute('''CREATE TABLE chat_history
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            timestamp TEXT NOT NULL,
                            user_message TEXT NOT NULL,
                            ai_response TEXT NOT NULL,
                            tokens_used INTEGER DEFAULT 0,
                            prompt_tokens INTEGER DEFAULT 0,
                            completion_tokens INTEGER DEFAULT 0,
                            total_cost REAL DEFAULT 0.0,
                            response_type TEXT,
                            confidence_score REAL)''')
                        conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Database initialization error: {e}")
            raise
    def store_message(self, user_message: str, ai_response: str, stats: Dict[str, Any]):
        try:
            with sqlite3.connect(self.db_name) as conn:
                c = conn.cursor()
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                c.execute('''INSERT INTO chat_history 
                            (timestamp, user_message, ai_response, tokens_used, 
                             prompt_tokens, completion_tokens, total_cost)
                            VALUES (?, ?, ?, ?, ?, ?, ?)''',
                         (timestamp, user_message, ai_response,
                          stats.get('total_tokens', 0),
                          stats.get('prompt_tokens', 0),
                          stats.get('completion_tokens', 0),
                          stats.get('total_cost', 0.0)))
                conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Database error: {e}")
            raise
    def get_chat_history(self, limit: int = 100) -> List[Dict]:
        try:
            with sqlite3.connect(self.db_name) as conn:
                c = conn.cursor()
                c.execute('''SELECT timestamp, user_message, ai_response 
                           FROM chat_history 
                           ORDER BY timestamp DESC 
                           LIMIT ?''', (limit,))
                rows = c.fetchall()
                return [
                    {
                        'timestamp': row[0],
                        'user_message': row[1],
                        'ai_response': row[2]
                    }
                    for row in rows
                ]
        except sqlite3.Error as e:
            logging.error(f"Database error: {e}")
            return []
class InternshipChatbot:
    def __init__(self, embeddings_path: str):
        self.chain = None
        self.chat_history = []
        self.stats = {
            'total_tokens': 0,
            'prompt_tokens': 0,
            'completion_tokens': 0,
            'total_cost': 0
        }
        self.embeddings_path = embeddings_path
        self.initialize_chain()

    def initialize_chain(self):
        try:
            embeddings = OpenAIEmbeddings()
            vectorstore = FAISS.load_local(
                self.embeddings_path,
                embeddings,
                allow_dangerous_deserialization=True
            )
            
            llm = ChatOpenAI(
                model="gpt-4-turbo",
                temperature=0.1,
                top_p=0.9,
                presence_penalty=0.6,
                frequency_penalty=0.5
            )

            prompt = ChatPromptTemplate.from_messages([
                ("system", """
                You are a specialized AI assistant for UNH Manchester's internship program, 
                designed to help students navigate their internship requirements and coursework.
                Course Level Guidelines:
                1. When asked about undergraduate courses, ONLY mention COMP690(4 credits)
                2. When asked about graduate courses, mention COMP890(1 credit), 891(1-3 credits), 892(1-3 credits), and 893 (1-3 credits)
                
                Context Processing Guidelines:
                1.Do not provide answers to questions that are completely unrelated to the internship program or course content. Politely redirect the student back to the relevant topic.
                2. Always provide complete information from the available context
                3. Read and analyze the provided context carefully
                4. Use chain-of-thought reasoning to break down complex questions
                5. Consider both explicit and implicit student needs
                6. Identify relevant course codes and requirements
                7. Do NOT use any markdown formatting (no #, *, _, etc.)
                8. Present information in plain text with clear formatting
                
                Response Formulation Guidelines:
                1. Start with the most relevant information from the context
                2. Use a warm, supportive tone while maintaining professionalism
                3. Structure responses clearly with appropriate headings when needed
                4. Include specific course codes and deadlines when applicable
                5. Provide step-by-step guidance for complex procedures
                
               
                
                Available Context:
                {context}
                
                Chat History:
                {chat_history}
                
                Answer Guidelines:
                - Be concise but thorough in 2-3 sentences. Please include more information if only required
                - Include all relevant information from the context
                - Use natural, conversational language
                - Break down complex information
                - Cite specific course documents when possible
                """),
                ("user", "{input}")
            ])
            document_chain = create_stuff_documents_chain(
                llm=llm,
                prompt=prompt
            )

            self.chain = create_retrieval_chain(
                vectorstore.as_retriever(
                    search_kwargs={"k": 8}
                ),
                document_chain
            )

        except Exception as e:
            logging.error(f"Chain initialization error: {e}")
            raise

    def get_response(self, user_message: str) -> Dict[str, Any]:
        try:
            with get_openai_callback() as cb:
                response = self.chain.invoke({
                    "input": user_message,
                    "chat_history": self.format_chat_history()
                })
                
                ai_response = response.get('answer', '')
                
                self.chat_history.append({
                    "human": user_message,
                    "ai": ai_response
                })
                
                self.stats.update({
                    'total_tokens': cb.total_tokens,
                    'prompt_tokens': cb.prompt_tokens,
                    'completion_tokens': cb.completion_tokens,
                    'total_cost': cb.total_cost
                })
                
                return {
                    'response': ai_response,
                    'stats': self.stats,
                    'history': self.format_chat_history()
                }

        except Exception as e:
            logging.error(f"Response generation error: {e}")
            raise

    def format_chat_history(self) -> str:
        return "\n".join([
            f"Human: {msg['human']}\nAssistant: {msg['ai']}"
            for msg in self.chat_history[-5:]
        ])

# Initialize components
db = ChatDatabase()
chatbot = InternshipChatbot(embeddings_path="embeddings")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'error': 'No message provided'}), 400

        user_message = data['message'].strip()
        if not user_message:
            return jsonify({'error': 'Empty message'}), 400

        response_data = chatbot.get_response(user_message)
        
        db.store_message(
            user_message=user_message,
            ai_response=response_data['response'],
            stats=response_data['stats']
        )
        
        return jsonify(response_data)
        
    except Exception as e:
        logging.error(f"Chat endpoint error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
