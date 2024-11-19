import os
import base64
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
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

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Initialize the Flask application
app = Flask(__name__)


# Initialize database
def init_db():
    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS chat_history
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  timestamp TEXT,
                  user_message TEXT,
                  ai_response TEXT)''')
    conn.commit()
    conn.close()


# Function to insert chat history into the database
def insert_chat(user_message, ai_response):
    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO chat_history (timestamp, user_message, ai_response) VALUES (?, ?, ?)",
              (timestamp, user_message, ai_response))
    conn.commit()
    conn.close()


# Function to extract text from PDF files
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        try:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + " "
        except Exception as e:
            print(f"Error reading {pdf}: {e}")
    return text.strip()


# Function to split text into chunks
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


# Function to create a vector store from text chunks
def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore


# Function to create a conversational chain
def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain


def handle_userinput(user_question):
    # Append the user's question to the conversation history
    app.config['chat_history'].append({"role": "user", "content": user_question})

    # Construct the full conversation context for the model to understand
    context = "\n".join([f"{msg['role']}: {msg['content']}" for msg in app.config['chat_history']])

    # Generate the response using the language model
    try:
        with get_openai_callback() as cb:
            response = app.config['conversation'].invoke({'question': context})

            # Append the assistant's response to conversation history
            app.config['chat_history'].append({"role": "assistant", "content": response['answer']})

            # Store the chat in the database
            insert_chat(user_question, response['answer'])
            return response['answer']

    except Exception as e:
        print("Error occurred while generating response:", e)
        return "I'm sorry, I can't process that right now."


# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')


# Route for handling chat requests
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = handle_userinput(user_message)
    return jsonify({'response': response})


def initialize_knowledge_base():
    pdf_docs = ["2024-fall-comp690-M2-M3-jin.pdf", "2024-fall-comp893-jin.pdf",
                "chatbot-doc.pdf"]  # Update paths as necessary

    # Extract text and update vectorstore
    text = get_pdf_text(pdf_docs)
    print(f"Extracted Text: {text}")

    text_chunks = get_text_chunks(text)
    print(f"Text Chunks: {text_chunks}")

    vectorstore = get_vectorstore(text_chunks)
    if vectorstore is not None:
        app.config['conversation'] = get_conversation_chain(vectorstore)
        app.config['chat_history'] = []
        print("Knowledge base initialized successfully.")
    else:
        print("Failed to create vectorstore. Exiting the application.")
        exit(1)  # Exit the application if the vectorstore initialization fails


if __name__ == '__main__':
    init_db()
    # Load documents and initialize knowledge base at startup
    initialize_knowledge_base()
    app.run(debug=True, port=8080)  # Run the app on port 8080