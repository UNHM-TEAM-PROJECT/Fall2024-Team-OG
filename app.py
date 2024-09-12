from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSequenceClassification

app = Flask(__name__)

# Load the TinyBERT model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("huawei-noah/TinyBERT_General_4L_312D")
model = AutoModelForSequenceClassification.from_pretrained("huawei-noah/TinyBERT_General_4L_312D", num_labels=2)

@app.route('/')
def index():
    return 'Welcome to the chatbot!'

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data['user_input']
    response = generate_response(user_input)
    return jsonify({'response': response})

def generate_response(user_input):
    # Implement the logic to generate a response using the TinyBERT model
    inputs = tokenizer(user_input, return_tensors="pt")
    outputs = model(**inputs)
    # Process the outputs and generate a response
    return "This is a sample response from the chatbot."

if __name__ == '__main__':
    app.run(debug=True)
