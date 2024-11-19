import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_community.callbacks import get_openai_callback
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate
import sqlite3
from datetime import datetime

# Load environment variables
load_dotenv()

app = Flask(__name__)

class ChatDatabase:
    def __init__(self, db_name='chat_history.db'):
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS chat_history
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         timestamp TEXT NOT NULL,
                         user_message TEXT NOT NULL,
                         ai_response TEXT NOT NULL)''')
            conn.commit()

    def store_message(self, user_message, ai_response):
        clean_user_message = user_message.split('[')[0].strip() if '[' in user_message else user_message
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            c.execute('''INSERT INTO chat_history 
                        (timestamp, user_message, ai_response) 
                        VALUES (?, ?, ?)''', 
                        (timestamp, clean_user_message, ai_response))
            conn.commit()

class ChatBot:
    def __init__(self):
        self.chain = None
        self.messages = []
        self.chat_stats = {
            'total_tokens': 0,
            'prompt_tokens': 0,
            'completion_tokens': 0,
            'total_cost': 0
        }
        self.chat_history = []
        self.initialize_chain()

    def initialize_chain(self):
        try:
            embeddings = OpenAIEmbeddings()
            vectorstore = FAISS.load_local(
                "embeddings", 
                embeddings,
                allow_dangerous_deserialization=True
            )
            
            llm = ChatOpenAI(
                model="gpt-4",
                temperature=0.2
            )

            # Enhanced prompt template with better context handling and response guidelines
            prompt = ChatPromptTemplate.from_messages([
                                    ("system", """
                                    You are a precise schedule information assistant focused on answering questions strictly based on the provided UNH course scrum meeting schedule PDF. 
                                    If you cannot find the answer within the PDF, simply respond with, "I'm sorry, but I couldn't find this information in the provided document."

                                    For any question about "final report due" is mentioned, the response should be "The final report is due on 12/9 according to the provided document."
                                    
                                    Instructions for analyzing meeting patterns:

                                    1. PATTERN IDENTIFICATION:
                                    - Track ALL meeting days for each week (e.g., Monday, Wednesday, Friday).
                                    - Identify meeting patterns, such as:
                                        * Single day meetings (e.g., "Monday only")
                                        * Multiple day meetings (e.g., "Monday, Wednesday, Friday")
                                        * Changes in patterns between weeks

                                    2. SPECIFIC DAY ANALYSIS:
                                    When asked about specific days, follow these steps:
                                    - Review each week's full meeting schedule.
                                    - List all weeks where that day appears.
                                    - Distinguish between:
                                        * Weeks where it's the ONLY meeting day.
                                        * Weeks where it's part of multiple meeting days.

                                    3. COMPREHENSIVE RESPONSE:
                                    - Present each relevant week chronologically.
                                    - For each week, include:
                                        * Week number and date
                                        * Complete meeting pattern for that week
                                        * Clearly indicate if it's a single-day or multi-day pattern.

                                    Context from documents:
                                    {context}

                                    Previous conversation:
                                    {chat_history}

                                    VERIFICATION CHECKLIST:
                                    - Have you reviewed the entire semester schedule?
                                    - Are you listing all occurrences of the requested day?
                                    - Are you distinguishing between single-day and multi-day patterns?
                                    - Have you included the full meeting pattern for each week?

                                    Important: Answer only questions related to the UNH course scrum meeting schedule. If an unrelated question is asked (e.g., "What kind of pizza should I get?"), respond with, "I'm here to assist with UNH course scrum meeting schedule information only."
                                    """),
                                    ("user", "{input}")
                                ])

            
            # Create the document chain
            document_chain = create_stuff_documents_chain(
                llm=llm,
                prompt=prompt
            )

            # Create the retrieval chain
            self.chain = create_retrieval_chain(
                vectorstore.as_retriever(
                    search_kwargs={"k": 3}
                ),
                document_chain
            )

        except Exception as e:
            print(f"Error initializing chain: {e}")
            raise

    def format_chat_history(self):
        formatted_history = ""
        for msg in self.chat_history[-5:]:  # Only use last 5 messages for context
            formatted_history += f"Human: {msg['human']}\nAssistant: {msg['ai']}\n\n"
        return formatted_history

    def get_response(self, user_message):
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
                
                self.chat_stats.update({
                    'total_tokens': cb.total_tokens,
                    'prompt_tokens': cb.prompt_tokens,
                    'completion_tokens': cb.completion_tokens,
                    'total_cost': cb.total_cost
                })
                
                self.messages.append({"role": "user", "content": user_message})
                self.messages.append({"role": "assistant", "content": ai_response})
                
                return ai_response

        except Exception as e:
            print(f"Error generating response: {e}")
            raise

    def get_conversation_history(self):
        return self.format_chat_history()

# Initialize global instances
db = ChatDatabase()
chatbot = ChatBot()

@app.route('/')
def home():
    return render_template('index.html', messages=[], stats=chatbot.chat_stats)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'error': 'No message provided'}), 400

        user_message = data['message']
        
        ai_response = chatbot.get_response(user_message)
        db.store_message(user_message, ai_response)
        history = chatbot.get_conversation_history()
        
        return jsonify({
            'response': ai_response,
            'stats': chatbot.chat_stats,
            'history': history
        })
        
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)