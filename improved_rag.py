import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFacePipeline
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Step 1: Load and preprocess the PDF
def load_and_process_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_documents(documents)
    
    logging.info(f"Processed PDF: {len(texts)} chunks created")
    return texts

# Step 2: Create embeddings and vector store
def create_vector_store(texts):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(texts, embeddings)
    
    logging.info("Vector store created")
    return vector_store

# Step 3: Load the T5 model
def load_t5_model(model_name="google/flan-t5-base"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    
    pipe = pipeline(
        "text2text-generation",
        model=model,
        tokenizer=tokenizer,
        max_length=512,
        do_sample=True,
        temperature=0.7,
    )
    
    llm = HuggingFacePipeline(pipeline=pipe)
    
    logging.info(f"Loaded language model: {model_name}")
    return llm

# Step 4: Create the RAG pipeline
def create_rag_pipeline(vector_store, llm):
    template = """Use the following pieces of context from the course syllabus to answer the question at the end. If you don't know the answer or if the information is not present in the context, just say that you don't know or that the information is not available in the syllabus. Do not make up an answer.

    {context}

    Question: {question}
    Answer: Based on the course syllabus information provided, """
    
    PROMPT = PromptTemplate(
        template=template, input_variables=["context", "question"]
    )
    
    chain_type_kwargs = {"prompt": PROMPT}
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(search_kwargs={"k": 5}),
        chain_type_kwargs=chain_type_kwargs,
        return_source_documents=True
    )
    
    logging.info("RAG pipeline created")
    return qa_chain

# Step 5: Main chatbot function
def chatbot(query, qa_chain):
    try:
        result = qa_chain.invoke({"query": query})
        return result["result"]
    except Exception as e:
        logging.error(f"Error in processing query: {e}")
        return "I'm sorry, but I encountered an error while processing your query. Could you please try rephrasing your question?"

# Main execution
if __name__ == "__main__":
    pdf_path = '2024-fall-comp690-M2-M3-jin.pdf'  # Replace with your PDF file path
    
    try:
        # Process PDF and create vector store
        texts = load_and_process_pdf(pdf_path)
        vector_store = create_vector_store(texts)
        
        # Load T5 model
        llm = load_t5_model()
        
        # Create RAG pipeline
        qa_chain = create_rag_pipeline(vector_store, llm)
        
        # Chat loop
        print("Chatbot is ready! Type 'exit' to end the conversation.")
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() == 'exit':
                break
            
            if user_input:
                try:
                    response = chatbot(user_input, qa_chain)
                    print(f"Chatbot: {response}")
                except Exception as e:
                    print(f"An error occurred: {e}")
            else:
                print("Please enter a valid question.")
        
    except Exception as e:
        logging.error(f"An error occurred while setting up the chatbot: {e}")
        print(f"An error occurred while setting up the chatbot: {e}")

print("Thank you for using the chatbot!")