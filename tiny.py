from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

class TinyBERTClassifier:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("huawei-noah/TinyBERT_General_4L_312D")
        self.model = AutoModelForSequenceClassification.from_pretrained("huawei-noah/TinyBERT_General_4L_312D", num_labels=2)  # Adjust num_labels based on your classes
        self.model.eval()

    def classify(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
        with torch.no_grad():
            outputs = self.model(**inputs)
        probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
        predicted_class = torch.argmax(probabilities, dim=-1).item()
        return predicted_class

# Usage
classifier = TinyBERTClassifier()
result = classifier.classify("Short text about UNHM Computing internship")
print(f"Predicted class: {result}")
