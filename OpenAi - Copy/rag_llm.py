import os
import base64
from dotenv import load_dotenv
import streamlit as st
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

# Load environment variables
load_dotenv()

# Set up OpenAI API key
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Database setup
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

def insert_chat(user_message, ai_response):
    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO chat_history (timestamp, user_message, ai_response) VALUES (?, ?, ?)",
              (timestamp, user_message, ai_response))
    conn.commit()
    conn.close()

# PDF processing functions
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
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

def handle_userinput(user_question):
    with get_openai_callback() as cb:
        response = st.session_state.conversation.invoke({'question': user_question})
        st.session_state.chat_history = response['chat_history']

        # Add messages to session state
        st.session_state.messages.append({"role": "user", "content": user_question})
        st.session_state.messages.append({"role": "assistant", "content": response['answer']})
        
        # Store the chat in the database
        insert_chat(user_question, response['answer'])

        st.session_state.total_tokens = cb.total_tokens
        st.session_state.prompt_tokens = cb.prompt_tokens
        st.session_state.completion_tokens = cb.completion_tokens
        st.session_state.total_cost = cb.total_cost

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def main():
    # Initialize database
    init_db()

    # Set page config
    st.set_page_config(page_title="UNHM Computing Internship Chatbot", layout="wide")

    # Custom CSS
    st.markdown("""
    <style>
    .main-container {
        display: flex;
        flex-direction: column;
        height: 100px;
        padding: 1pppx;
    }
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
    }
    .logo {
        width: 100px;
    }
    .main-title {
        color: #2E8B57;
        text-align: center;
        font-size: 2.5em;
        flex-grow: 1;
    }
    .chat-container {
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        border: 1px solid #ccc;
        border-radius: 10px;
        overflow: hidden;
    }
    .chat-messages {
        flex-grow: 1;
        overflow-y: auto;
        padding: 1rem;
        background-color: #f9f9f9;
        font-size: 18px;
    }
    .chat-input-container {
        display: flex;
        padding: 1rem;
        background-color: #fff;
    }
    .stTextArea textarea {
        font-size: 18px;
        resize: none;
    }
    .stButton > button {
        background-color: #2E8B57;
        color: white;
    }
    .user-message, .bot-message {
        padding: 0.5rem;
        border-radius: 5px;
        margin-bottom: 0.5rem;
    }
    .user-message {
        background-color: #e6f2ff;
        text-align: right;
    }
    .bot-message {
        background-color: #f0f0f0;
    }
    .token-info {
        font-size: 0.8em;
        color: #666;
        margin-bottom: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # Main container
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    # Header with logo and title
    st.markdown("""
    <div class="header">
        <img src="data:image/png;base64,{}" class="logo">
        <h1 class="main-title">UNHM Computing Internship Chatbot</h1>
        <div style="width:100px;"></div>
    </div>
    """.format(get_base64_of_bin_file("CenterStackedWhiteWeb_RGB.png")), unsafe_allow_html=True)

    # Initialize knowledge base
    if "conversation" not in st.session_state:
        with st.spinner("Initializing knowledge base..."):
            pdf_docs = ["2024-fall-comp690-M2-M3-jin.pdf", "2024-fall-comp893-jin.pdf", "chatbot-doc.pdf"]
            raw_text = get_pdf_text(pdf_docs)
            text_chunks = get_text_chunks(raw_text)
            vectorstore = get_vectorstore(text_chunks)
            st.session_state.conversation = get_conversation_chain(vectorstore)
        st.success("Knowledge base initialized. You can now start asking questions!")

    # Token and cost information
    if "total_tokens" in st.session_state:
        st.markdown('<div class="token-info">', unsafe_allow_html=True)
        st.markdown(f"Total Tokens: {st.session_state.total_tokens} | "
                    f"Prompt Tokens: {st.session_state.prompt_tokens} | "
                    f"Completion Tokens: {st.session_state.completion_tokens} | "
                    f"Total Cost (USD): ${st.session_state.total_cost:.4f}", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Chat container
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)

    # Chat messages
    st.markdown('<div class="chat-messages">', unsafe_allow_html=True)
    if "messages" not in st.session_state:
        st.session_state.messages = []
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot-message">{message["content"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Chat input
    st.markdown('<div class="chat-input-container">', unsafe_allow_html=True)
    user_input = st.text_area("Chat Input", placeholder="Type your message here...", key="user_input", height=100, label_visibility="collapsed")
    if st.button("Send"):
        if user_input:
            handle_userinput(user_input)
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)  # Close chat-container
    st.markdown('</div>', unsafe_allow_html=True)  # Close main-container

if __name__ == '__main__':
    main()