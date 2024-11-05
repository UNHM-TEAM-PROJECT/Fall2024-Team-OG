import json
import pytest
from app import ChatBot  # Make sure this imports your ChatBot class


# Load test cases from JSON file
def load_test_cases():
    with open('questions_answers.json', 'r') as file:
        return json.load(file)


@pytest.mark.parametrize("test_case", load_test_cases())
def test_chatbot_responses(test_case):
    # Check if the test case is for a direct question or keyword search
    if 'expected_answer' in test_case:
        question = test_case['question']
        expected_answer = test_case['expected_answer']

        # Create an instance of ChatBot to test
        chatbot = ChatBot()

        # Get the actual response from the chatbot
        actual_response = chatbot.get_response(question)

        # Assert the actual response matches the expected answer
        assert actual_response == expected_answer, (
            f"Failed for question: '{question}'. "
            f"Expected: '{expected_answer}', but got: '{actual_response}'."
        )
        print(f"PASSED: {question}")

    elif 'expected_keywords' in test_case:
        question = test_case['input']
        expected_keywords = test_case['expected_keywords']

        # Create an instance of ChatBot to test
        chatbot = ChatBot()

        # Get the actual response from the chatbot
        actual_response = chatbot.get_response(question)

        # Check if all expected keywords are in the actual response
        if not all(keyword in actual_response for keyword in expected_keywords):
            missing_keywords = [kw for kw in expected_keywords if kw not in actual_response]
            print(f"DEBUG: Actual response for '{question}': '{actual_response}'")  # Log the actual response
            assert False, (
                f"Failed for question: '{question}'. "
                f"Missing keywords: {missing_keywords}. Actual response: '{actual_response}'."
            )



