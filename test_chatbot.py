import requests
import json
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Define the URL of your Flask application
BASE_URL = "http://localhost:5001"

def is_semantically_similar(text1, text2, threshold=0.8):
    # Create the document list
    documents = [text1, text2]
    
    # Create the Document-Term Matrix
    count_vectorizer = CountVectorizer().fit_transform(documents)
    vectors = count_vectorizer.toarray()
    
    # Calculate Cosine Similarity
    similarity = cosine_similarity(vectors)
    
    # We consider them similar if the score is above the threshold
    return similarity[0][1] > threshold

def test_chatbot(user_input, expected_output):
    """
    Test the chatbot with a given input and expected output.
    """
    print(f"\nUser Input: {user_input}")
    
    # Send POST request to the chatbot API
    response = requests.post(f"{BASE_URL}/api/chat", json={"user_input": user_input})
    
    if response.status_code == 200:
        actual_output = response.json()['response']
        print(f"Actual Output: {actual_output}")
        print(f"Expected Output: {expected_output}")
        
        # Check if the actual output matches the expected output semantically
        if is_semantically_similar(actual_output, expected_output):
            print("Test Result: PASSED")
        else:
            print("Test Result: FAILED")
    else:
        print(f"Error: Received status code {response.status_code}")
        print("Test Result: FAILED")

# Test cases
test_cases = [
    {
        "input": "Hello",
        "expected": "Hello! How can I help you today?"
    },
    {
        "input": "What is the grading structure for the internship?",
        "expected": "The grading structure for the internship consists of three components: 10% Class Attendance, 60% Sprint Grade, and 20% Final Project Report. The Sprint Grade is calculated as Teamwork Grade * Sprint Grade."
    },
    {
        "input": "How is the Sprint Grade calculated?",
        "expected": "The Sprint Grade is calculated as: Teamwork Grade * Sprint Grade. The Teamwork Grade is based on peer evaluation for each of the three sprints, and you will receive a team grade for each sprint based on the technical aspect of the product and team project management."
    },
    {
        "input": "What framework does the internship project follow?",
        "expected": "The internship project follows the general structure of the Scrum framework, which includes specific roles, events, artifacts, and rules."
    },
    {
        "input": "What is the credit hour workload estimate?",
        "expected": "The credit hour workload estimate is a minimum of 45 hours of student academic work per credit per term."
    }
]

# Run test cases
for case in test_cases:
    test_chatbot(case['input'], case['expected'])

print("\nAll test cases completed.")
