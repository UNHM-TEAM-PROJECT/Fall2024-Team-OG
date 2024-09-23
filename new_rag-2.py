# Install required packages:
# pip install langchain langchain-community langchain-huggingface pypdf transformers torch sentence-transformers faiss-cpu

import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFacePipeline
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Step 1: Load and preprocess the PDF
def load_and_process_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)
    texts = text_splitter.split_documents(documents)
    
    return texts

# Step 2: Create embeddings and vector store
def create_vector_store(texts):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(texts, embeddings)
    
    return vector_store

# Step 3: Load the BART model
def load_bart_model(model_name="facebook/bart-large-cnn"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    
    pipe = pipeline(
        "text2text-generation",
        model=model,
        tokenizer=tokenizer,
        max_length=200,
        do_sample=True,
        temperature=0.2,
    )
    
    llm = HuggingFacePipeline(pipeline=pipe)
    
    return llm

# Step 4: Create the RAG pipeline
def create_rag_pipeline(vector_store, llm):
    template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.

    {context}

    Question: {question}
    Answer: Let me provide you with the most accurate information based on the course syllabus:"""
    
    PROMPT = PromptTemplate(
        template=template, input_variables=["context", "question"]
    )
    
    chain_type_kwargs = {"prompt": PROMPT}
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(search_kwargs={"k": 3}),
        chain_type_kwargs=chain_type_kwargs,
        return_source_documents=True
    )
    
    return qa_chain

# Step 5: Main chatbot function
def chatbot(query, qa_chain):
    result = qa_chain.invoke({"query": query})
    return result["result"]

# Main execution
if __name__ == "__main__":
    pdf_path = '2024-fall-comp690-M2-M3-jin.pdf'  # Replace with your PDF file path
    
    # Process PDF and create vector store
    texts = load_and_process_pdf(pdf_path)
    vector_store = create_vector_store(texts)
    
    # Load BART model
    llm = load_bart_model()
    
    # Create RAG pipeline
    qa_chain = create_rag_pipeline(vector_store, llm)
    
    # Chat loop
    print("Chatbot is ready! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        
        response = chatbot(user_input, qa_chain)
        print(f"Chatbot: {response}")

print("Thank you for using the chatbot!")