from flask import Flask, request, jsonify, render_template
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from Internshipinfo import Internshipinfo

import sqlite3

app = Flask(__name__)

# Create database connection
conn = sqlite3.connect('chatbot.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""CREATE TABLE IF NOT EXISTS questions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    question TEXT,
                    answer TEXT,
                    predicted_class INTEGER
                )""")
conn.commit()

# Load the TinyBERT model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("huawei-noah/TinyBERT_General_4L_312D")
model = AutoModelForSequenceClassification.from_pretrained("huawei-noah/TinyBERT_General_4L_312D", num_labels=2)

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/api/chat', methods=['POST'])
def api_chat():
    data = request.get_json()
    user_input = data['user_input']
    if user_input.lower() in Internshipinfo:
        response = Internshipinfo[user_input.lower()]
    else:
        response = generate_response(user_input)
    return jsonify({'response': response})

def generate_response(user_input):
    inputs = tokenizer(user_input, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    # This is a placeholder. You'll need to implement proper response generation
    return f"Chatbot: I received your message: {user_input}"

if __name__ == '__main__':
    app.run(debug=True)

