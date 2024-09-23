import PyPDF2
from sentence_transformers import SentenceTransformer
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Load models
embedder = SentenceTransformer('all-mpnet-base-v2')
model_name = "google/flan-t5-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def extract_grading_section(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text = page.extract_text()
            if "GRADING" in text:
                start = text.find("GRADING")
                return text[start:].strip()
    return None

grading_section = extract_grading_section('2024-fall-comp893-jin.pdf')
if not grading_section:
    print("Failed to extract grading section")
    exit(1)

# Split the grading section into sentences
sentences = [sent.strip() for sent in re.split(r'(?<=[.!?])\s+', grading_section) if sent.strip()]
sentence_embeddings = embedder.encode(sentences)

def get_relevant_sentences(query, top_k=3):
    query_embedding = embedder.encode([query])
    similarities = torch.nn.functional.cosine_similarity(torch.tensor(query_embedding), torch.tensor(sentence_embeddings))
    top_indices = similarities.argsort(descending=True)[:top_k]
    return [sentences[i] for i in top_indices]

def generate_answer(query, relevant_sentences):
    context = " ".join(relevant_sentences)
    
    prompt = f"""Based on the following information about a course, answer the question. 
    If the information doesn't directly answer the question, say so and provide the most relevant information available.

    Course Information:
    {context}

    Question: {query}

    Answer:"""

    inputs = tokenizer(prompt, return_tensors="pt", max_length=1024, truncation=True)
    outputs = model.generate(**inputs, max_length=250, num_return_sequences=1, temperature=0.7)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return answer.strip()

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get('user_input')
    if not user_input:
        return jsonify({'error': 'No user input provided'}), 400

    relevant_sentences = get_relevant_sentences(user_input)
    response = generate_answer(user_input, relevant_sentences)
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)