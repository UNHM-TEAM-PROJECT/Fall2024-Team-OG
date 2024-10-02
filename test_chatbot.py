import requests
from sentence_transformers import SentenceTransformer, util
import re

# Define the URL of your Flask application
BASE_URL = "http://localhost:5000"

# Load the sentence transformer model for semantic similarity
embedder = SentenceTransformer('all-MiniLM-L6-v2')

def extract_keywords(text):
    """
    Extract key information like numeric values or keywords that are central to the sentence.
    """
    # Regular expression to extract simple yes/no, or phrases like percentages, numbers, etc.
    keywords = re.findall(r'\d+%|\d+|yes|no|peer evaluation', text.lower())
    if keywords:
        return keywords
    else:
        # Split the text into words and filter out common words (stopwords)
        return re.findall(r'\b\w+\b', text.lower())

def is_semantically_similar(text1, text2, threshold=0.8):
    # Extract keywords for comparison
    keywords1 = extract_keywords(text1)
    keywords2 = extract_keywords(text2)
    
    # If both texts contain numeric info, percentages, or simple "yes/no", compare keywords
    if keywords1 and keywords2:
        if set(keywords1) == set(keywords2):
            return True

    # Check if responses have core semantic similarity using embeddings
    embedding1 = embedder.encode(text1, convert_to_tensor=True)
    embedding2 = embedder.encode(text2, convert_to_tensor=True)
    
    similarity_score = util.pytorch_cos_sim(embedding1, embedding2).item()
    
    # Return True if the similarity score is above the threshold
    return similarity_score > threshold

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
        
        # Check if the actual output matches the expected output semantically or numerically
        if is_semantically_similar(actual_output, expected_output):
            print("Test Result: PASSED")
        else:
            print("Test Result: FAILED")
    else:
        print(f"Error: Received status code {response.status_code}")
        print("Test Result: FAILED")

# Test cases based on the PDF content
test_cases = [
    {
        "input": "What is the grading structure?",
        "expected": "The grading structure consists of Class Attendance, Sprint Grade, and Final Project Report."
    },
    {
        "input": "How much does attendance contribute to the final grade?",
        "expected": "Class Attendance contributes 10% to the final grade."
    },
    {
        "input": "How is the Sprint Grade calculated?",
        "expected": "The Sprint Grade is calculated as: Teamwork Grade * Sprint Grade."
    },
    {
        "input": "What is the weightage of the final project report?",
        "expected": "The Final Project Report contributes 20% to the final grade."
    },
    {
        "input": "Will I receive a certificate after completing the internship?",
        "expected": "Yes, you will receive a certificate after successfully completing the internship."
    },
    {
        "input": "How is the teamwork evaluated?",
        "expected": "Teamwork is evaluated based on peer evaluation for each of the three sprints."
    },
    {
        "input": "What are the submission deadlines for assignments?",
        "expected": "The submission deadlines will be communicated by the instructor."
    },
    {
        "input": "Is there a makeup policy for missed assignments?",
        "expected": "There is no makeup policy for missed assignments unless you have prior approval."
    },
    {
        "input": "What framework does the internship project follow?",
        "expected": "The internship project follows the Scrum framework."
    },
    {
        "input": "What is the minimum credit hour workload?",
        "expected": "The minimum credit hour workload is 45 hours per credit per term."
    },
    {
        "input": "How are quizzes graded?",
        "expected": "Quizzes contribute to your final grade based on your performance and are averaged."
    },
    {
        "input": "Are there extra credit opportunities?",
        "expected": "Extra credit opportunities will be available at the instructor's discretion."
    },
    {
        "input": "What is the policy for late submissions?",
        "expected": "Late submissions are penalized by a 10% grade reduction per day."
    },
    {
        "input": "What are the penalties for plagiarism?",
        "expected": "Plagiarism results in a failing grade for the assignment and may result in further disciplinary actions."
    }
]

# Run test cases
for case in test_cases:
    test_chatbot(case['input'], case['expected'])

print("\nAll test cases completed.")
