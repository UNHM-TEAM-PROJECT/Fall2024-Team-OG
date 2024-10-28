import os
import base64
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from PIL import Image
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_community.callbacks import get_openai_callback
import sqlite3
from datetime import datetime
import hashlib

# Load environment variables
load_dotenv()

# Set up OpenAI API key
# Set up OpenAI API key
API_KEY = "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"
os.environ["OPENAI_API_KEY"] = API_KEY


app = Flask(__name__)

# Database setup with modified schema
def init_db():
    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    # Modified to keep existing table and data
    c.execute('''CREATE TABLE IF NOT EXISTS chat_history
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  timestamp TEXT,
                  user_message TEXT,
                  ai_response TEXT,
                  question_hash TEXT)''')
    conn.commit()
    conn.close()

def load_chat_history():
    """Load all chat history from database"""
    try:
        conn = sqlite3.connect('chat_history.db')
        c = conn.cursor()
        c.execute("SELECT timestamp, user_message, ai_response FROM chat_history ORDER BY timestamp ASC")
        history = c.fetchall()
        conn.close()
        
        messages = []
        for _, user_msg, ai_resp in history:
            messages.append({"role": "user", "content": user_msg})
            messages.append({"role": "assistant", "content": ai_resp})
        return messages
    except Exception as e:
        print(f"Error loading chat history: {e}")
        return []

def get_question_hash(question):
    """Create a hash of the question for consistent lookup"""
    normalized_question = " ".join(question.lower().split())
    return hashlib.md5(normalized_question.encode()).hexdigest()

def get_cached_response(question_hash):
    """Retrieve cached response for a given question hash"""
    try:
        conn = sqlite3.connect('chat_history.db')
        c = conn.cursor()
        c.execute("SELECT ai_response FROM chat_history WHERE question_hash = ? ORDER BY timestamp DESC LIMIT 1", 
                (question_hash,))
        result = c.fetchone()
        conn.close()
        return result[0] if result else None
    except Exception as e:
        print(f"Error retrieving cached response: {e}")
        return None

def insert_chat(user_message, ai_response, question_hash):
    """Insert chat history with question hash"""
    try:
        conn = sqlite3.connect('chat_history.db')
        c = conn.cursor()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.execute("INSERT INTO chat_history (timestamp, user_message, ai_response, question_hash) VALUES (?, ?, ?, ?)",
                (timestamp, user_message, ai_response, question_hash))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error inserting chat: {e}")

# PDF processing functions remain the same
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        try:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                text += page.extract_text()
        except Exception as e:
            print(f"Error processing PDF {pdf}: {e}")
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

# Global variables
conversation = None
messages = []  # Will be loaded from database
chat_stats = {
    'total_tokens': 0,
    'prompt_tokens': 0,
    'completion_tokens': 0,
    'total_cost': 0
}

def initialize_knowledge_base():
    global conversation, messages
    try:
        # Initialize conversation
        pdf_docs = ["2024-fall-comp690-M2-M3-jin.pdf", "2024-fall-comp893-jin.pdf", "chatbot-doc.pdf"]
        raw_text = get_pdf_text(pdf_docs)
        text_chunks = get_text_chunks(raw_text)
        vectorstore = get_vectorstore(text_chunks)
        conversation = get_conversation_chain(vectorstore)
        
        # Load existing chat history
        messages = load_chat_history()
        
        # Initialize conversation memory with existing messages
        for i in range(0, len(messages), 2):
            if i + 1 < len(messages):
                conversation.memory.chat_memory.add_user_message(messages[i]["content"])
                conversation.memory.chat_memory.add_ai_message(messages[i + 1]["content"])
                
    except Exception as e:
        print(f"Error initializing knowledge base: {e}")

@app.route('/')
def home():
    global messages
    if not messages:  # Load messages if they haven't been loaded yet
        messages = load_chat_history()
    return render_template('index.html', messages=messages, stats=chat_stats)

@app.route('/chat', methods=['POST'])
def chat():
    global conversation, messages, chat_stats
    
    try:
        if conversation is None:
            initialize_knowledge_base()
        
        user_message = request.json.get('message', '')
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
            
        question_hash = get_question_hash(user_message)
        
        # Try to get cached response first
        cached_response = get_cached_response(question_hash)
        
        if cached_response:
            ai_response = cached_response
            # Update stats with minimal values since we're using cached response
            chat_stats = {
                'total_tokens': chat_stats['total_tokens'],
                'prompt_tokens': chat_stats['prompt_tokens'],
                'completion_tokens': chat_stats['completion_tokens'],
                'total_cost': chat_stats['total_cost']
            }
        else:
            with get_openai_callback() as cb:
                response = conversation.invoke({'question': user_message})
                ai_response = response['answer']
                
                # Store new response in cache
                insert_chat(user_message, ai_response, question_hash)
                
                # Update stats
                chat_stats = {
                    'total_tokens': cb.total_tokens,
                    'prompt_tokens': cb.prompt_tokens,
                    'completion_tokens': cb.completion_tokens,
                    'total_cost': cb.total_cost
                }
        
        # Update messages
        messages.append({"role": "user", "content": user_message})
        messages.append({"role": "assistant", "content": ai_response})
        
        return jsonify({
            'response': ai_response,
            'stats': chat_stats
        })
        
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    init_db()
    initialize_knowledge_base()  # Initialize on startup
    app.run(debug=True)