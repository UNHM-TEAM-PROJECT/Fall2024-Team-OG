import json
import pytest
from sentence_transformers import SentenceTransformer, util
import numpy as np
from app import ChatBot #Importing the chatbot class


def load_test_cases():
    with open('questions_answers.json', 'r') as f:
        return json.load(f)


# Initialize the Sentence Transformer model
model = SentenceTransformer('all-mpnet-base-v2')


@pytest.mark.parametrize("test_case", load_test_cases())
def test_chatbot_responses(test_case):
    question = test_case['question']
    expected_sentence = test_case['expected_answer']

    chatbot = ChatBot()  # Instantiate your chatbot class
    actual_response = chatbot.get_response(question)

    # Generate embeddings
    try:
        embedding1 = model.encode(expected_sentence, convert_to_tensor=True)
        embedding2 = model.encode(actual_response, convert_to_tensor=True)
    except Exception as e:
        pytest.fail(f"Error generating embeddings: {e}")

    # Calculate cosine similarity
    cosine_scores = util.cos_sim(embedding1, embedding2)
    similarity_score = cosine_scores.item()

    similarity_threshold = 0.7  # Adjust this threshold as needed

    assert similarity_score >= similarity_threshold, (
        f"Failed for question: '{question}'.\n"
        f"Expected: '{expected_sentence}',\n"
        f"Got: '{actual_response}'.\n"
        f"Similarity score: {similarity_score}"
    )
    print(f"PASSED: '{question}'")
