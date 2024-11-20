from flask import Flask, request, jsonify, render_template
import logging
import re
import torch
from sentence_transformers import SentenceTransformer
import PyPDF2
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from info import Internshipinfo

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Initialize models
embedder = SentenceTransformer('all-mpnet-base-v2')
model_name = "google/flan-t5-large"  # Your LLM model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Extract grading section from the PDF
def extract_grading_section(pdf_path):
    """Extract the grading section from a PDF file."""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text = page.extract_text()
            if "GRADING" in text:  # As soon as we find "GRADING", we start extracting relevant text
                return text
    return None

# Extract the grading section only once during startup
grading_section = extract_grading_section('2024-fall-comp690-M2-M3-jin.pdf')
if grading_section:
    sentences = [sent.strip() for sent in grading_section.split('. ') if sent.strip()]
    sentence_embeddings = embedder.encode(sentences)

def get_relevant_sentences(query, top_k=3):
    """Get the most relevant sentences based on the user's query."""
    query_embedding = embedder.encode([query])
    similarities = torch.nn.functional.cosine_similarity(torch.tensor(query_embedding),
                                                         torch.tensor(sentence_embeddings))
    top_indices = similarities.argsort(descending=True)[:top_k]
    return [sentences[i] for i in top_indices if similarities[top_indices].max() > 0.3]  # Increase threshold for relevance

def generate_answer(query, relevant_sentences):
    """Generate an answer based on the provided query and relevant sentences."""
    try:
        context = " ".join(relevant_sentences)
        prompt = f"""Based on the following information, answer the question:
        {context}

        Question: {query}

        Answer: """

        inputs = tokenizer(prompt, return_tensors="pt", max_length=1024, truncation=True)
        outputs = model.generate(**inputs, max_length=250, num_return_sequences=1, temperature=0.7)
        answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return answer.strip()
    except Exception as e:
        return f"Error generating answer: {e}"

@app.route('/')
def home():
    """Render the chat interface."""
    return render_template('chat.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat requests and provide responses."""
    try:
        data = request.get_json()
        if not data or 'user_input' not in data:
            raise ValueError("Invalid input provided.")

        user_input = data['user_input']
        normalized_input = user_input.strip().lower()

        # Handle greetings
        if normalized_input in ["hello", "hi", "hey", "howdy", "greetings", "how are you"]:
            return jsonify({'response': "Hello! How can I help you today?"})

        # Check predefined questions first
        if normalized_input in Internshipinfo:
            response = Internshipinfo[normalized_input]
        else:
            # Get relevant sentences and generate a response
            relevant_sentences = get_relevant_sentences(user_input)
            if relevant_sentences:
                response = generate_answer(user_input, relevant_sentences)
            else:
                response = "I'm sorry, I couldn't find any relevant information for that."

        logging.debug(f"Response generated: {response}")
        return jsonify({'response': response})

    except Exception as e:
        logging.error(f"Error handling chat request: {e}")
        return jsonify({'response': "An error occurred processing your request."}), 500

if __name__ == '__main__':
    print("Starting Flask application...")

