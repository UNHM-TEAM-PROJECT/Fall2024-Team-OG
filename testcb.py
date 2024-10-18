import openai
import os

from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


if openai.api_key is None:
    print("Error: OPENAI_API_KEY environment variable not set. Please set it before running.")
    exit(1)


def get_openai_response(user_input):
    """Gets a response from the OpenAI API."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can experiment with different models here
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Answer questions based on the provided context, and if you do not know the answer, say you don't know."},
                {"role": "user", "content": user_input},
            ],
            temperature=0.7, # Adjusts randomness; lower values are more deterministic
            max_tokens=150      # Limits the length of the response
        )
        return response.choices[0].message.get("content", "").strip()
    except openai.error.OpenAIError as e:
        return f"An error occurred: {e}"

def test_chatbot(user_input, expected_output):
    print(f"\nUser Input: {user_input}")
    actual_output = get_openai_response(user_input)
    print(f"Actual Output: {actual_output}")
    print(f"Expected Output: {expected_output}")
    if actual_output.lower() in expected_output.lower(): #Simplified similarity check
        print("Test Result: PASSED")
    else:
        print("Test Result: FAILED")


test_cases = [
    {"input": "What is the grading structure?", "expected": "The grading structure consists of Class Attendance, Sprint Grade, and Final Project Report."},
    {"input": "How much does attendance contribute to the final grade?", "expected": "Class Attendance contributes 10% to the final grade."},
    {"input": "How is the Sprint Grade calculated?", "expected": "The Sprint Grade is calculated as: Teamwork Grade * Sprint Grade."},
    {"input": "What is the weightage of the final project report?", "expected": "The Final Project Report contributes 20% to the final grade."},
    {"input": "Will I receive a certificate after completing the internship?", "expected": "yes"},
    {"input": "How is the teamwork evaluated?", "expected": "Teamwork is evaluated based on peer evaluation for each of the three sprints."},
    {"input": "What are the submission deadlines for assignments?", "expected": "The submission deadlines will be communicated by the instructor."},
    {"input": "Is there a makeup policy for missed assignments?", "expected": "no"},
    {"input": "What framework does the internship project follow?", "expected": "Scrum"},
    {"input": "What is the minimum credit hour workload?", "expected": "45 hours per credit per term"},
    {"input": "How are quizzes graded?", "expected": "Quizzes contribute to your final grade based on your performance and are averaged."},
    {"input": "Are there extra credit opportunities?", "expected": "Extra credit opportunities will be available at the instructor's discretion."},
    {"input": "What is the policy for late submissions?", "expected": "Late submissions are penalized by a 10% grade reduction per day."},
    {"input": "What are the penalties for plagiarism?", "expected": "Plagiarism results in a failing grade for the assignment and may result in further disciplinary actions."},
    {"input": "What computing majors require internships?", "expected": "Undergraduate Computer Information Systems (CIS), Computer Science (CS). Graduate M.S. Information Technology, M.S. Cybersecurity Engineering."},
    {"input": "Who is the internship coordinator?", "expected": "Karen Jin"},
    {"input": "What undergraduate internship course is there?", "expected": "COMP690"},
    {"input": "What graduate internship courses are available?", "expected": "COMP890, COMP891, COMP892, COMP893"},
    {"input": "What is COMP690?", "expected": "Internship Experience"},
    {"input": "Explain COMP890.", "expected": "Internship and Career Planning"},
    {"input": "What are the credit hours for COMP690 undergraduates?", "expected": "4 credits (150 hours of internship work)."},
    {"input": "How many hours are required for graduate internship courses?", "expected": "Variable; roughly 40 hours per credit."},
    {"input": "Can I use a past internship to meet the requirements?", "expected": "no"},
    {"input": "How do I register for internship courses?", "expected": "Email Prof. Karen Jin or the course instructor for permission."},
    {"input": "How can I find an internship?", "expected": "Handshake, company websites, LinkedIn, Indeed, Hired, internship fairs, family, friends, faculty."},
    {"input": "How do I register my internship on Handshake?", "expected": "Log in, go to 'Experiences,' click 'Request an Experience,' complete the form (3 learning objectives), get approval from your supervisor and instructor."},
    {"input": "Do I need the course if I already work?", "expected": "yes"},
    {"input": "What do I need for F1 CPT authorization?", "expected": "Internship job description/posting, offer letter, proof of course registration."},
    {"input": "What are important dates for internships and CPT?", "expected": "Offer letter must have specific dates; CPT starts on the first day of the semester; a gap exists between semesters where you can't work."},
    {"input": "How do I request CPT authorization?", "expected": "Meet with Karen Jin, log into eOISS, complete the CPT form, upload employer letter and proof of registration; OISS will issue the I-20 after approval."},
    {"input": "How many hours do I need to log weekly?", "expected": "Weekly logs are needed for each week worked until required hours are met (150 for undergraduate COMP690, variable for graduate courses)."},
    {"input": "Can I start my internship before the course begins?", "expected": "yes"},
    {"input": "What if my internship starts after the semester begins?", "expected": "Contact Prof. Karen Jin."},
    {"input": "Is Professor Jin available on Mondays?", "expected": "Contact Professor Jin directly via email to confirm her availability."},
    {"input": "What is the contact information for the CaPS office?", "expected": "(603) 641-4394, unhm.career@unh.edu"},
    {"input": "What is the website for OISS?", "expected": "https://www.unh.edu/global/international-students-scholars"},
    {"input": "What's Karen Jin's email?", "expected": "Karen.Jin@unh.edu"},
    {"input": "What's the phone number for CaPS?", "expected": "(603) 641-4394"},
    {"input": "Where is Karen Jin's office located?", "expected": "Rm139, Pandora Mill building"},
    {"input": "What if I have already completed an internship?", "expected": "You must have an internship while enrolled in the course."},
    {"input": "What should I do if I haven't found an internship by the end of the semester?", "expected": "Contact Professor Jin."},
    {"input": "What's the process for getting CPT authorization?", "expected": "Meet with Karen Jin, log into eOISS, complete the CPT form, upload employer letter and proof of registration; OISS will issue the I-20 after approval."},
    {"input": "How many hours of internship experience are needed for graduate students enrolled in 3 credit hours?", "expected": "120 hours"},
    {"input": "When is COMP890 offered?", "expected": "Fall and Spring semesters"},
    {"input": "What is the purpose of COMP890?", "expected": "To help you plan for the internship search process."},
    {"input": "Can I take COMP891 without completing COMP890?", "expected": "Check the course syllabus."},
    {"input": "What is the difference between COMP892 and COMP893?", "expected": "COMP892 is for students working in tech; COMP893 is for students in their last semester and need to fulfill internship requirements."},
    {"input": "What are some examples of job websites that I can use to find internships?", "expected": "LinkedIn, Indeed, and Hired."},
    {"input": "How long does it take to get an approval from Karen Jin?", "expected": "Contact her directly."},
    {"input": "What are the internship requirements for undergraduates?", "expected": "COMP690 (150 hours)"},
    {"input": "What are the internship requirements for graduates?", "expected": "A graduate-level internship course (roughly 40 hours per credit)."},
    {"input": "What are the weekly log requirements?", "expected": "Weekly logs are required for every week worked."},
    {"input": "What are the requirements for the final internship report?", "expected": "Check the course syllabus."},
    {"input": "What does the applied research option involve?", "expected": "Check the course description for COMP690."},
    {"input": "What is the team project option in COMP690?", "expected": "Check the course description for COMP690."},
    {"input": "When are the progress presentations?", "expected": "Check the course syllabus."},
    {"input": "How are COMP690 applied research credits earned?", "expected": "Check the course syllabus."},
    {"input": "How is the internship experience graded?", "expected": "Check the course syllabus."},
    {"input": "What if I need help with my resume?", "expected": "Contact the Career and Professional Success office."},
    {"input": "What are the consequences of not completing the internship?", "expected": "Check the course syllabus."},
    {"input": "What are the consequences of working without CPT authorization?", "expected": "Check OISS guidelines."},
    {"input": "What is the CPT application deadline?", "expected": "Check with OISS and Professor Jin."},
    {"input": "What is the process for requesting an extension to my CPT?", "expected": "Check with OISS."},
    {"input": "What is the address of the Pandora Mill building?", "expected": "Search online for the address."},
    {"input": "What is the internship course credit hour requirement for graduate students?", "expected": "Check the course description for precise requirements."},
    {"input": "What is the tuition fee?", "expected": "Check the UNH Manchester website."},
    {"input": "How can I apply for financial aid?", "expected": "Check the UNH Manchester website."},
    {"input": "Are there any scholarships available?", "expected": "Check the UNH Manchester website."},
    {"input": "Where is the library located?", "expected": "Check the UNH Manchester campus map."},
    {"input": "What library resources are available?", "expected": "Check the UNH Manchester library website."},
    {"input": "What about campus housing?", "expected": "Check the UNH Manchester housing website."},
    {"input": "What student support services are available?", "expected": "Check the UNH Manchester website."},
    {"input": "Where can I find the campus map?", "expected": "Check the UNH Manchester website."},
    {"input": "How do I register for courses?", "expected": "Check the UNH student portal."},
    {"input": "When is the next semester?", "expected": "Check the UNH Manchester academic calendar."},
    {"input": "How do I get a transcript?", "expected": "Check the UNH Manchester registrar's office website or student portal."},
    {"input": "What is the student code of conduct?", "expected": "Check the UNH student handbook."},
    {"input": "What is the policy on academic integrity?", "expected": "Check the UNH student handbook."},
    {"input": "What are the university's policies on late submissions?", "expected": "Check individual course syllabi."},
    {"input": "How can I get help with my studies?", "expected": "Check the UNH Manchester website."},
    {"input": "Where can I find career services?", "expected": "Check the UNH Manchester website."},
    {"input": "How do I report a problem on campus?", "expected": "Check the UNH Manchester website."},
    {"input": "What if I have questions about my student account?", "expected": "Check the UNH Manchester website."},
    {"input": "How do I change my major?", "expected": "Contact your academic advisor."},
    {"input": "Where can I find the academic calendar?", "expected": "Check the UNH Manchester website."},
    {"input": "What are the office hours for Professor Jin?", "expected": "Check the course syllabus or contact Professor Jin."},
    {"input": "Is there an orientation program for new students?", "expected": "Check the UNH Manchester website."},
    {"input": "What support is available for international students?", "expected": "Check the OISS website."},
    {"input": "What is the process for withdrawing from a course?", "expected": "Check the UNH student handbook or the registrar's office website."},
    {"input": "What resources are available for students with disabilities?", "expected": "Check the UNH disability services website."},
    {"input": "What counseling services are available?", "expected": "Check the UNH Manchester website."},
    {"input": "What is the university's policy on alcohol and drug use?", "expected": "Check the UNH student handbook."},
    {"input": "What are the consequences of violating the code of conduct?", "expected": "Check the UNH student handbook."},
    {"input": "Where can I get help if I'm experiencing a mental health crisis?", "expected": "Contact UNH counseling services or emergency services (911)."},

]

for case in test_cases:
    test_chatbot(case['input'], case['expected'])

print("\nAll test cases completed.")







