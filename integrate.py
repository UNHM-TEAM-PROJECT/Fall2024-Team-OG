from flask import Flask, request, jsonify
from your_tinybert_file import TinyBERTClassifier

app = Flask(__name__)
classifier = TinyBERTClassifier()

@app.route('/classify', methods=['POST'])
def classify_text():
    data = request.json
    text = data.get('text', '')
    result = classifier.classify(text)
    return jsonify({'class': result})

if __name__ == '__main__':
    app.run(debug=True)
