import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema import Document  # Added this import
import glob
import logging
from tqdm import tqdm
import re

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()

def clean_table_content(text):
    """Clean and structure tabular schedule data"""
    # Remove extra whitespace while preserving table structure
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Standardize week entries
    text = re.sub(r'Week (\d+)[:\s]*(\d+/\d+)', r'Week \1 (\2):', text)
    
    # Ensure scrum meeting information is properly formatted
    text = re.sub(r'Scrum meetings?\s*\((.*?)\)', r'Scrum meetings (\1)', text)
    
    # Add explicit separators between weeks
    text = re.sub(r'(?<=\S)(?=Week \d+)', r'\n\n', text)
    
    return text

def process_pdfs(pdf_directory):
    """Process PDFs with focus on preserving table structure"""
    pdf_files = glob.glob(os.path.join(pdf_directory, "*.pdf"))
    
    if not pdf_files:
        raise Exception(f"No PDF files found in {pdf_directory}")
    
    all_documents = []
    
    for pdf_path in tqdm(pdf_files, desc="Processing PDFs"):
        try:
            loader = PyPDFLoader(pdf_path)
            pages = loader.load()
            
            # Process each page
            for page in pages:
                content = page.page_content
                
                # Check if page contains schedule information
                if re.search(r'Week \d+.*Scrum meeting', content, re.IGNORECASE):
                    # Clean and structure the content
                    cleaned_content = clean_table_content(content)
                    
                    # Split into week blocks
                    week_blocks = re.split(r'\n\n(?=Week \d+)', cleaned_content)
                    
                    for block in week_blocks:
                        if 'Scrum meeting' in block:
                            # Create a new document for each week's schedule
                            metadata = {
                                'source': pdf_path,
                                'type': 'schedule',
                                'week': re.search(r'Week (\d+)', block).group(1) if re.search(r'Week (\d+)', block) else 'unknown'
                            }
                            all_documents.append({
                                'content': block.strip(),
                                'metadata': metadata
                            })
                else:
                    # Keep non-schedule content as is
                    all_documents.append({
                        'content': content,
                        'metadata': {'source': pdf_path, 'type': 'general'}
                    })
            
            logging.info(f"Successfully processed: {pdf_path}")
            
        except Exception as e:
            logging.error(f"Error processing {pdf_path}: {str(e)}")
            continue
    
    if not all_documents:
        raise Exception("No valid documents were processed")
    
    # Convert to LangChain documents
    documents = [
        Document(
            page_content=doc['content'],
            metadata=doc['metadata']
        ) for doc in all_documents
    ]
    
    # Create embeddings
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(documents, embeddings)
    
    return vector_store

def save_embeddings(vector_store, save_path):
    try:
        vector_store.save_local(save_path)
        logging.info(f"Successfully saved embeddings to {save_path}")
    except Exception as e:
        logging.error(f"Error saving embeddings: {str(e)}")
        raise

def main():
    try:
        # Process PDFs
        vector_store = process_pdfs(pdf_directory="pdfs")
        
        # Save embeddings
        save_embeddings(vector_store, "embeddings")
        
        logging.info("Embedding creation completed successfully")
        
    except Exception as e:
        logging.error(f"Application error: {str(e)}")
        raise

if __name__ == "__main__":
    #main()