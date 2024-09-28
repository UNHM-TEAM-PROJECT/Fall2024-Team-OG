
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load your model here
model_name = "google/flan-t5-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def generate_answer(query, relevant_sentences):
    """Generate an answer based on the provided query and relevant sentences."""
    try:
        context = " ".join(relevant_sentences)
        prompt = f"""Based on the following information, answer the question: 
        {context}

        Question: {query}

        Answer:"""

        inputs = tokenizer(prompt, return_tensors="pt", max_length=1024,truncation=True)

        outputs = model.generate(**inputs, max_length=250, num_return_sequences=1, temperature=0.7)
        answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return answer.strip()

    except Exception as e:
        return f"Error generating answer: {e}"

