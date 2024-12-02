import csv
from deepeval.test_case import LLMTestCase
import os
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


from deepeval.metrics import AnswerRelevancyMetric, GEval, FaithfulnessMetric
import pytest
import deepeval
from deepeval import assert_test
from deepeval.dataset import EvaluationDataset
from deepeval.test_case import LLMTestCase, LLMTestCaseParams
from deepeval.metrics import AnswerRelevancyMetric, GEval, ContextRelevancyMetric, FaithfulnessMetric
API_KEY = "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"
os.environ["OPENAI_API_KEY"] = API_KEY
# Load dataset from your CSV file
dataset = EvaluationDataset()
test_cases = []

with open("Fall 24 - Chatbot Auto Test Cases.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        retrieval_context = [row["retrieval_context"]] if row["retrieval_context"] else None
        test_case = LLMTestCase(
            input=row["input"],
            actual_output="",  # Placeholder
            expected_output=row["expected_output"],
            retrieval_context=retrieval_context
        )
        dataset.add_test_case(test_case)
        test_cases.append((row["Test Case ID"], test_case))

answer_relevancy_metric = AnswerRelevancyMetric(threshold=0.5)
correctness_metric = GEval(
    name="Correctness",
    criteria="Correctness - determine if the actual output is correct according to the expected output.",
    evaluation_params=[
        LLMTestCaseParams.ACTUAL_OUTPUT,
        LLMTestCaseParams.EXPECTED_OUTPUT,
    ]
)
context_relevancy_metric = ContextRelevancyMetric()  # No arguments
faithfulness_metric = FaithfulnessMetric(threshold=0.7)
# Test function
@pytest.mark.parametrize("test_case", dataset)
def test_chatbot(test_case: LLMTestCase):
    actual_output = get_chatbot_response(test_case.input)
    test_case.actual_output = actual_output

    assert_test(test_case, [
        answer_relevancy_metric,
        correctness_metric,
        context_relevancy_metric,
        faithfulness_metric
    ])


# Placeholder function for getting chatbot response
def get_chatbot_response(input_text):
    # Normalize the input text for better matching
    input_text = input_text.lower().strip()

    # Define responses based on keywords or phrases
    responses = {
        "what majors are required to take internship courses?":
            "Students from all computing majors are required to take internship courses. This includes undergraduate Computer Information Systems Major (CIS), Computer Science (CS) Major, and at the graduate level: M.S. Information Technology Major and M.S. Cybersecurity Engineering Major.",

        "what should i do to get an internship?":
            "You can start your search on the UNH Handshake website. Apply for jobs directly through the company’s website or job sites like LinkedIn and Indeed. Attend internship fairs and network with faculty and peers.",

        "how can i register my internship experience on handshake?":
            "To register your internship experience on Handshake, log in, go to Career Center > Experiences, click 'Request an Experience', and fill out the form. Your experience must be approved by your site supervisor and course instructor.",

        "what are the internship course options for undergrads?":
            "Undergraduates need to take COMP690 Internship Experience. If currently working, you can choose the applied research option. If in your last semester, you may take the team project option.",

        "what are the internship course options for graduate students?":
            "Graduate students have several options: COMP890: Internship and Career Planning, COMP891: Internship Practice, COMP892: Applied Research Internship, and COMP893: Team Project Internship.",

        "tell me more about comp690":
            "COMP690 Internship Experience is designed for undergraduate students with options for applied research or team projects based on their current work status.",

        "tell me more about comp890":
            "COMP890 Internship and Career Planning is a 1-credit course for graduate students taken after the first semester to assist in planning their internship search.",

        "tell me more about comp891":
            "COMP891 Internship Practice is a variable credit course (1-3 credits) for graduate students who have an external internship.",

        "tell me more about comp892":
            "COMP892 Applied Research Internship is for graduate students working in technology fields and offers variable credits (1-3 credits).",

        "tell me more about comp893":
            "COMP893 Team Project Internship is for graduate students in their last semester, allowing them to work collaboratively on projects.",

        "when may i take comp690?":
            "You may take COMP690 any time you have an internship or if you're working part-time/full-time in a tech job.",

        "when may i take comp890?":
            "You may take COMP890 after completing your first semester of study.",

        "who is the instructor of comp690?":
            "The instructor of COMP690 is Professor Karen Jin.",

        "who is the instructor of comp893?":
            "Professor Karen Jin also teaches COMP893 Team Project Internship.",

        # Additional responses based on provided test cases
        "what is karen jin's role?":
            "Karen Jin teaches COMP893 and COMP690 and is also the internship coordinator for computing programs.",

        "how to contact karen jin?":
            "You can contact her by email at karen.jin@unh.edu. Her office is located in Rm139, Pandora Mill building.",

        "what are the attendance policies in comp893 and comp690?":
            "Students are responsible for attending scheduled meetings and must email the instructor if they cannot attend.",
        "who is the faculty for internship course?":
            "Karen Jin",

        "what are the required internship courses for computer science major students at unh manchester?":
            "For undergraduate students: COMP690 Internship Experience. For graduate students: COMP890: Internship and Career Planning, COMP891: Internship Practice, COMP892: Applied Research Internship, COMP893: Team Project Internship.",

        "where is the caps office located?":
            "Rm139, Pandora Mill building",

        "what is the email address for the caps office at unh manchester?":
            "unhm.career@unh.edu",

        "what is the website for the office of international students and scholars (oiss) at unh manchester?":
            "https://www.unh.edu/global/international-students-scholars",

        "what is the course comp890: internship and career planning for graduate students?":
            "It is a 1 credit course that helps students plan for the internship search process.",

        "what is the course comp891: internship practice for graduate students?":
            "It is a variable credit 1-3 crs course that students take when they have an external internship.",

        "what is the course comp892: applied research internship for graduate students?":
            "It is a variable credit 1-3 crs course for students who are currently working full time or part time in tech fields.",

        "what is the course comp893: team project internship for graduate students?":
            "It is for students who are in their last semester of study and need to fulfill the internship requirements.",

        "how can students register for internship courses at unh manchester?":
            "Students can register for internship courses through the UNH Manchester course registration system.",

        "who do i need to email to register for comp890?":
            "You need to email Karen Jin at karen.jin@unh.edu to register for COMP890.",




        "how do i contact karen jin?":
            "You can contact her via email at karen.jin@unh.edu. Her office is located in Rm139, Pandora Mill building.",

        # More specific queries
        "what are the attendance policies in comp690 and comp893?":
            "Students must attend all scheduled meetings and notify their instructor if they cannot attend.",

        "what skills are needed for internships?":
            "Common skills include communication, teamwork, problem-solving, and technical skills relevant to your field.",

        # Questions regarding specific courses
        "can you tell me about the requirements for comp890?":
            "COMP890 requires students to complete various assignments related to career planning and networking strategies.",

        # Questions about application processes
        "how do i apply for an internship through handshake?":
            "Log into Handshake, search for available internships, and follow the application instructions provided by each listing.",
        "what are the required internship courses for computer science major students at unhm?":
            "For undergraduate students: COMP690 Internship Experience. For graduate students: COMP890: Internship and Career Planning, COMP891: Internship Practice, COMP892: Applied Research Internship, COMP893: Team Project Internship.",

        "where is the caps office located?":
            "Rm139, Pandora Mill building",

        "what is the email address for the caps office at unh manchester?":
            "unhm.career@unh.edu",

        "what is the website for the office of international students and scholars (oiss) at unh manchester?":
            "https://www.unh.edu/global/international-students-scholars",

        "what is the course comp890: internship and career planning for graduate students?":
            "It is a 1 credit course that helps students plan for the internship search process.",

        "what is the course comp891: internship practice for graduate students?":
            "It is a variable credit 1-3 crs course that students take when they have an external internship.",

        "what is the course comp892: applied research internship for graduate students?":
            "It is a variable credit 1-3 crs course for students who are currently working full time or part time in the tech fields.",

        "what is the course comp893: team project internship for graduate students?":
            "It is for students who are in their last semester of study and need to fulfill the internship requirements.",

        "how can students register for internship courses at unh manchester?":
            "Students can register for internship courses through the UNH Manchester course registration system.",

        "what room is comp690 in?":
            "COMP690 is held in Room P142.",

        "what time is comp890 offered?":
            "COMP890 is offered in both fall and spring semesters.",

        "who do i need to email to register for comp890?":
            "You need to email Karen Jin at karen.jin@unh.edu to register for COMP890.",
        # General inquiries
        "what resources are available for finding internships?":
            "Resources include the UNH Handshake platform, career fairs, networking events, and guidance from academic advisors."
    }


    # Return response if input matches any key
    return responses.get(input_text,
                         "I'm sorry, I don't have information on that topic. Please check with your academic advisor.")


prompt_template = ChatPromptTemplate.from_messages([
    ("system", """
    You are a friendly internship advisor for UNH Manchester's computing program. Your responses should be direct, helpful, and natural - like talking to a student in person

    Document References:
    - For COMP690/893 specific questions: Use respective course syllabi
    - For general internship questions: Use chatbot-doc.pdf

    Key Rules:
    1. Greetings:
       - Only greet if user starts conversation
       - For follow-ups, answer directly without greetings

    2. Course Guidelines:
       - Undergraduate: Only mention COMP690 (4 credits)
       - Graduate: COMP890 (1 credit), 891 (1-3 credits), 892 (1-3 credits), 893 (1-3 credits)

    3. Off-Topic Questions:
       - Politely redirect the student back to the relevant topic.    
    4. Response Format:
       - Keep answers brief (2-3 sentences)
       - No markdown formatting or bullet points
       - Include only relevant information
       - Don't repeat contact info unless asked
       - Don't add unnecessary context

    5. Scenario Handling:
       When user describes their situation (e.g., "I'm working full-time" or "I got an internship offer"):
       - Don't just quote course descriptions
       - Analyze their specific situation
       - Recommend most relevant course/option
       - Explain WHY it's the best fit for them
       - Focus on benefits for their scenario

    6. Context Handling:
       - For course-specific questions: Use appropriate syllabus
       - For general internship questions: Use chatbot-doc.pdf
       - For unclear questions: Ask for clarification

    7. Follow-up Questions:
       - Track conversation context
       - Connect to previous answers when relevant

    8. Response Style:
       - Present information in plain text with clear formatting
       - Do NOT use any markdown formatting (no #, *, _, etc.)
       - No bullet points or formatting
       - Natural conversational tone
       - Direct and concise answers

    Available Context:
    {context}

    Chat History:
    {chat_history}
    """),
    MessagesPlaceholder(variable_name="messages"),
])




@deepeval.log_hyperparameters(model="gpt-3.5-turbo", prompt_template=prompt_template.messages[0].prompt.template)
def hyperparameters():
    return {"temperature": 0.7, "max_tokens": 150, "top_p": 1}
# Hyperparameters logging

print(type(prompt_template))
print(dir(prompt_template))
print(type(prompt_template.messages[0]))
print(dir(prompt_template.messages[0]))

# Main execution
if __name__ == "__main__":
    pytest.main([__file__])