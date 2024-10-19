import openai
import os
import PyPDF2

from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


if openai.api_key is None:
    print("Error: OPENAI_API_KEY environment variable not set. Please set it before running.")
    exit(1)

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page in range(len(pdf_reader.pages)):
                text += pdf_reader.pages[page].extract_text()
            return text.strip()
    except FileNotFoundError:
        return "PDF file not found."
    except Exception as e:
        return f"An error occurred while processing the PDF: {e}"

def get_openai_response(user_input, pdf_text1, pdf_text2, pdf_text3):
    """Gets a response from the OpenAI API, providing all three PDF texts as context."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a helpful assistant. Answer questions based on the following documents:\nDocument 1:\n{pdf_text1}\n\nDocument 2:\n{pdf_text2}\n\nDocument 3:\n{pdf_text3}\n\nIf you don't know the answer, say you don't know."},
                {"role": "user", "content": user_input},
            ],
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.get("content", "").strip()
    except Exception as e:
        return f"An error occurred: {e}"

def test_chatbot(user_input, expected_keywords, pdf_path1, pdf_path2, pdf_path3):
    pdf_text1 = extract_text_from_pdf(pdf_path1)
    pdf_text2 = extract_text_from_pdf(pdf_path2)
    pdf_text3 = extract_text_from_pdf(pdf_path3)
    print(f"\nUser Input: {user_input}")
    actual_output = get_openai_response(user_input, pdf_text1, pdf_text2, pdf_text3) #actual_output defined here
    print(f"Actual Output: {actual_output}")
    actual_output_lower = actual_output.lower()
    passed = all(keyword.lower() in actual_output_lower for keyword in expected_keywords)
    if passed:
        print("Test Result: PASSED")
    else:
        print(f"Test Result: FAILED. Actual: '{actual_output}', Expected Keywords: {expected_keywords}")
test_cases = [
            {"input": "What is the grading structure?",
             "expected_keywords": ["attendance", "sprint grade", "final project report"]},
            {"input": "How much does attendance contribute to the final grade?",
             "expected_keywords": ["10%", "attendance"]},
    {"input": "How is the Sprint Grade calculated?",
     "expected_keywords": ["teamwork grade", "sprint grade", "multiplied", "product", "peer evaluation", "technical",
                           "management"]},
    {"input": "What is the weightage of the final project report?",
     "expected_keywords": ["20%", "final project report", "grade", "weightage", "percentage"]},
    {"input": "Will I receive a certificate after completing the internship?",
     "expected_keywords": ["no mention", "certificate", "award", "completion"]},
    {"input": "How is the teamwork evaluated?",
     "expected_keywords": ["peer evaluation", "three sprints", "teamwork", "collaboration", "rubric"]}
]

pdf_file_path1 = "2024-fall-comp690-M2-M3-jin.pdf"  # Replace with the actual path to your first PDF
pdf_file_path2 = "2024-fall-comp893-jink.pdf"  # Replace with the actual path to your second PDF
pdf_file_path3 = "chatbot-doc.pdf"  #Replace with actual path to your third PDF


for case in test_cases:
    test_chatbot(case['input'], case['expected_keywords'], pdf_file_path1, pdf_file_path2, pdf_file_path3)

print("\nAll test cases completed.")








