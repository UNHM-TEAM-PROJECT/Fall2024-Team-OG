from transformers import pipeline

# Define the model name
model_name = "distilgpt2"

# Load text generation pipeline
generator = pipeline('text-generation', model=model_name)

# Generate text
results = generator("Once upon a time", max_length=50, num_return_sequences=1)

# Print results
for result in results:
    print(result['generated_text'])
