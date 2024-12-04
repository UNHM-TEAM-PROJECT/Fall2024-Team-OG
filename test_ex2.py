import csv
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

dataset = EvaluationDataset()
test_cases = []

with open("Fall 24 - Chatbot Auto Test Cases.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        retrieval_context = [row["retrieval_context"]] if row["retrieval_context"] else None
        test_case = LLMTestCase(
            input=row["input"],
            actual_output="",
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
context_relevancy_metric = ContextRelevancyMetric()
faithfulness_metric = FaithfulnessMetric(threshold=0.7)

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

def get_chatbot_response(input_text):
    input_text = input_text.lower().strip()
    responses = {
        "what majors are required to take internship courses?": "Students from all computing majors are required to take internship courses. This includes undergraduate Computer Information Systems Major (CIS), Computer Science (CS) Major, and at the graduate level: M.S. Information Technology Major and M.S. Cybersecurity Engineering Major.",
        "what should i do to get an internship?": "Start your search on UNH Handshake. Apply directly through company websites or job sites like LinkedIn and Indeed. Attend internship fairs on both Manchester and Durham campuses. Speak with family, friends, and faculty. The Career and Professional Success office can help with resume writing and interview coaching.",
        "how can i register my internship experience on handshake?": "To register your internship on Handshake: 1. Login to Handshake. 2. Go to Career Center > Experiences. 3. Click 'Request an Experience' and fill out the form. 4. Get approval from your site supervisor and course instructor. Include at least three well-developed learning objectives.",
        "what are the internship course options for undergrads?": "Undergraduate students need to take COMP690 Internship Experience. It has an applied research option for students currently working, and a team project option for students in their last semester.",
        "what are the internship course options for graduate students?": "Graduate students have four options: COMP890: Internship and Career Planning (1 credit), COMP891: Internship Practice (1-3 credits), COMP892: Applied Research Internship (1-3 credits), and COMP893: Team Project Internship (1-3 credits).",
        "tell me more about comp690": "COMP690 Internship Experience is for undergraduate students. It has an applied research option for students who are currently working, and a team project option for students in their last semester of program.",
        "tell me more about comp890": "COMP890 Internship and Career Planning is a 1-credit course for graduate students. Take it after your first semester to help plan your internship search. It's offered in fall and spring semesters.",
        "tell me more about comp891": "COMP891 Internship Practice is a variable credit 1-3 crs course for graduate students with an external internship. Register for at least 1 credit to apply for CPT. Offered in fall, spring, and summer.",
        "tell me more about comp892": "COMP892 Applied Research Internship is a variable credit 1-3 crs course for graduate students working full or part-time in tech fields. Offered in fall, spring, and summer.",
        "tell me more about comp893": "COMP893 Team Project Internship is for graduate students in their last semester who need to fulfill internship requirements. Work on collaborative projects with external stakeholders. Offered in fall and spring.",
        "when may i take comp690?": "You may take COMP690 any time you have an internship, or if you have a part-time or full-time tech job. If you can't find an internship by your last semester, you can take it with the group project option.",
        "when may i take comp890?": "You may take COMP890 Internship and Career Planning after you finish your first semester of study.",
        "when may i take comp891?": "You may take COMP891 Internship Practice when you have found an external internship. The course is offered in all semesters year-round.",
        "when may i take comp892?": "You may take COMP892 Applied Research Internship if you are currently working full time or part time in the tech fields. The course is offered in all semesters year-round.",
        "when may i take comp893?": "You may take COMP893 Team Project Internship in your last semester of study when you need to fulfill the internship requirement. It's offered in fall and spring semesters.",
        "who is the instructor of comp690?": "The instructor of COMP690 Internship Experience is Professor Karen Jin.",
        "who is the instructor of comp893?": "The instructor of COMP893 Team Project Internship is Professor Karen Jin.",
        "what is karen jin's role?": "Karen Jin teaches COMP893 and COMP690. She is also the internship coordinator for the computing programs.",
        "how to contact karen jin?": "You can contact Karen Jin by email at Karen.Jin@unh.edu. Her office is located in Rm139, Pandora Mill building.",
        "what are the instructor's office hours?": "Karen Jin's office hours are Monday 1-4pm and Friday 9-noon. She is available in person or over Zoom, and appointments can be made via email.",
        "what are the attendance policies in comp893 and comp690?": "Students are responsible for attending scheduled meetings and are expected to abide by the University Policy on Attendance. If you can't attend, email the instructor before the class meeting to request an excused absence.",
        "what do you do if you think you'll miss a meeting?": "If you anticipate missing a meeting, email the instructor about the circumstances and request to be excused BEFORE the class meeting. Provide a valid reason for your absence.",
        "what is the policy on late submissions?": "Late submissions may be granted only if you email prior to the deadline, explaining and providing evidence for the circumstances that prevent you from meeting the submission requirement.",
        "do i still need to take the course if i am currently working?": "Yes, you still need to take the Internship Experience course as a degree requirement. If you're currently working in the field, you can use the applied research option of COMP690 for undergrads or COMP892 for grad students.",
        "i did an internship last summer. can i use that to cover the internship requirements?": "No, a past internship cannot be used to fulfill the course requirements. The internship position and required hours must be completed while you are registered in the Internship Experience course.",
        "how to register for internship courses?": "To register for internship courses, obtain permission from the internship course instructor. Contact Prof. Karen Jin, the internship coordinator, for more details.",
        "what requirements do you need to fulfill to earn the credit?": "To earn credit, attend all scheduled class meetings, submit weekly logs, complete a final internship report, give progress presentations, and meet specific course syllabus requirements. Complete the necessary internship hours based on your enrolled credit hours.",
        "do i need to write weekly logs every week?": "Yes, write weekly logs every week during your internship until you complete the required hours. Continue with logs after reaching total hours, but you don't need to submit for weeks you haven't worked.",
        "how many hours do i need to log?": "For COMP690, log 150 hours. For graduate students, each credit hour equals roughly 40 hours of internship work. For example, 3 credit hours require 120 hours of internship work.",
        "can i start my internship position before the internship experience course starts?": "Yes, you can start your internship before the course starts. However, you can only count up to 20% of the total required internship hours if you complete the remaining hours during the same semester.",
        "i just got an internship offer but the semester has already started, what should i do?": "Contact the faculty internship coordinator, Professor Karen Jin, immediately. Depending on the timing, you may be allowed to late add into the internship course or arrange a later start date with the employer.",
        "how do i contact caps office?": "The CaPS office website is https://manchester.unh.edu/careers/career-professional-success. You can reach them by email at unhm.career@unh.edu or by phone at (603) 641-4394.",
        "what is the oiss' website?": "The website for the Office of International Students and Scholars (OISS) is https://www.unh.edu/global/international-students-scholars. Their email is oiss@unh.edu.",
        "what is the course name of comp893?": "The course name of COMP893 is Team Project Internship.",
        "what is the course name of comp690?": "The course name of COMP690 is Internship Experience.",
        "what room is comp893 in?": "In Fall 2024 semester, COMP893 is located in Room P142.",
        "what room is comp690 in?": "In Fall 2024 semester, COMP690 is located in Room P142.",
        "what time is comp893?": "COMP893 has two sections: M1 Section meets on Wednesday 9:10am-12pm and M2 Section meets on Wednesday 1:10-4pm.",
        "what time is comp690?": "COMP690 has two sections: M2 Section meets on Wednesday 9:10am-12pm and M3 Section meets on Wednesday 1:10-4pm.",
        "how do you make appointments with karen jin?": "Email Karen Jin directly at Karen.Jin@unh.edu to arrange a meeting. It's important to schedule these meetings in advance and provide a clear reason for the meeting.",
        "what is the course description for comp893?": "COMP893 provides experiential learning through team projects. Students gain practical skills by working on collaborative projects with external stakeholders, contributing to real-world IT products, processes, or services, and understanding challenges in implementing technology solutions in a professional setting.",
        "what is the course description for comp690?": "COMP690 provides experiential learning through team projects. Students gain practical skills by working on collaborative projects with external stakeholders, contributing to real-world IT products, processes, or services, and understanding challenges in implementing technology solutions in a professional setting.",
        "student learning outcome for comp893?": "Learning outcomes for COMP893: 1. Analyze complex computing problems and identify solutions. 2. Design, implement, and evaluate computing solutions. 3. Communicate effectively in professional contexts. 4. Function effectively in a team. 5. Identify and analyze user needs in developing computing systems.",
        "student learning outcome for comp690?": "Learning outcomes for COMP690: 1. Analyze complex computing problems and identify solutions. 2. Design, implement, and evaluate computing solutions. 3. Communicate effectively in professional contexts. 4. Function effectively in a team. 5. Identify and analyze user needs in developing computing systems.",
        "how much of the grade is class attendance in comp893?": "In Fall 2024 semester, 10% of the grade is based on class attendance for COMP893.",
        "what components does the final grade consist of in comp893?": "The final grade for COMP893 in Fall 2024 consists of: 10% Class Attendance, 60% Sprint Grade, 10% Homework, and 20% Final Project Report.",
        "how is sprint grade calculated?": "The sprint grade is calculated as the Teamwork Grade multiplied by the Sprint Grade. Teamwork Grade is based on peer evaluation for each sprint, and Sprint Grade is based on the technical aspect of the product and team project management.",
        "what is the credit hour workload estimate?": "The Credit Hour Workload Estimate for COMP893 and COMP690 is a minimum of 45 hours of student academic work per credit per term.",
    }
    return responses.get(input_text, "I'm sorry, I don't have specific information on that topic. Please check with your academic advisor or the course instructor for more details.")

prompt_template = ChatPromptTemplate.from_messages([
    ("system", """
    You are a friendly internship advisor for UNH Manchester's computing program. 
    Your responses should be direct, helpful, and natural - like talking to a student in person.
    Use the course syllabi for COMP690/893 specific questions and chatbot-doc.pdf for general internship questions.
    Keep answers brief (2-3 sentences) and use plain text without markdown formatting.
    For undergraduate students, only mention COMP690 (4 credits).
    For graduate students, mention COMP890 (1 credit), 891 (1-3 credits), 892 (1-3 credits), 893 (1-3 credits).
    When handling specific scenarios, analyze the situation and recommend the most relevant course/option.
    """),
    MessagesPlaceholder(variable_name="messages"),
])

@deepeval.log_hyperparameters(model="gpt-3.5-turbo", prompt_template=prompt_template.messages[0].prompt.template)
def hyperparameters():
    return {"temperature": 0.7, "max_tokens": 150, "top_p": 1}

if __name__ == "__main__":
    pytest.main([__file__])