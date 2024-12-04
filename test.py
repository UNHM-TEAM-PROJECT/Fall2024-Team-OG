from sqlalchemy import true, false

var = [
    {
        "question": "Who is the Faculty for Internship course?",
        "answer": "Karen Jin",
        "source": "chatbot-doc.pdf"
    },
    {
        "question": "What are the required internship courses for computer science major students at UNH Manchester?",
        "answer": "For undergraduate students: COMP690 Internship Experience. For graduate students: COMP890: Internship and Career Planning, COMP891: Internship Practice, COMP892: Applied Research Internship, COMP893: Team Project Internship.",
        "source": "chatbot-doc.pdf"
    },
    {
        "question": "Where is the CaPS office located?",
        "answer": "Rm139, Pandora Mill building",
        "source": "chatbot-doc.pdf"
    },
    {
        "question": "What is the email address for the CaPS office at UNH Manchester?",
        "answer": "unhm.career@unh.edu",
        "source": "chatbot-doc.pdf"
    },
    {
        "question": "What is the website for the Office of International Students and Scholars (OISS) at UNH Manchester?",
        "answer": "https://www.unh.edu/global/international-students-scholars",
        "source": "chatbot-doc.pdf"
    },
    {
        "question": "What is the course COMP890: Internship and Career Planning for graduate students?",
        "answer": "It is a 1 credit course that helps students plan for the internship search process.",
        "source": "chatbot-doc.pdf"
    },
    {
        "question": "What is the course COMP891: Internship Practice for graduate students?",
        "answer": "It is a variable credit 1-3 crs course that students take when they have an external internship.",
        "source": "chatbot-doc.pdf"
    },
    {
        "question": "What is the course COMP892: Applied Research Internship for graduate students?",
        "answer": "It is a variable credit 1-3 crs course for students who are currently working full time or part time in the tech fields.",
        "source": "chatbot-doc.pdf"
    },
    {
        "question": "What is the course COMP893: Team Project Internship for graduate students?",
        "answer": "It is for students who are in their last semester of study and need to fulfill the internship requirements.",
        "source": "chatbot-doc.pdf"
    },
    {
        "question": "How can students register for internship courses at UNH Manchester?",
        "answer": "Students can register for internship courses through the UNH Manchester course registration system.",
        "source": "chatbot-doc.pdf"
    },
    {
        "question": "What is the name of the course?",
        "answer": "COMP 893 Team Project Internship",
        "source": "Comp893.pdf"
    },
    {
        "question": "Who is the instructor for the course?",
        "answer": "Karen Jin, Associate Professor, Department of Applied Engineering and Sciences",
        "source": "Comp893.pdf"
    },
    {
        "question": "Where is the course located?",
        "answer": "Rm P142",
        "source": "Comp893.pdf"
    },
    {
        "question": "What are the office hours for the instructor?",
        "answer": "Monday 1-4pm and Friday 9-noon. Available in person or over Zoom. Email to make appointments.",
        "source": "Comp893.pdf"
    },
    {
        "question": "What is the course description?",
        "answer": "The internship course provides experiential learning experience through placement in team projects.",
        "source": "Comp893.pdf"
    },
    {
        "question": "What are the student learning outcomes for the course?",
        "answer": "Analyzing complex computing problems, designing and implementing computing solutions, effective communication, functioning in a team, and identifying user needs.",
        "source": "Comp893.pdf"
    },
    {
        "question": "What is the tentative course schedule for Week 1?",
        "answer": "Class Introduction, Development Team (DT) Setup, Intro to Project Management, Intro to Scrum workflow, and Project Goal.",
        "source": "Comp893.pdf"
    },
    {
        "question": "What is the tentative course schedule for Week 2?",
        "answer": "Project Kickoff, Environment Setup: Jira, Create Project backlog, Create user stories, tasks and bugs, and Integration w/ Source code control, team communication.",
        "source": "Comp893.pdf"
    },
    {
        "question": "What is the Zoom link for the instructor?",
        "answer": "https://unh.zoom.us/j/4858446046",
        "source": "Comp893.pdf"
    },
    {
        "question": "When is the course term for COMP 893 Team Project Internship?",
        "answer": "Fall 2024",
        "source": "Comp893.pdf"
    },
    {
        "question": "What is the name of the internship course?",
        "answer": "COMP690 Internship Experience",
        "source": "Comp693.pdf"
    },
    {
        "question": "How many credits does the internship course offer?",
        "answer": "4",
        "source": "Comp693.pdf"
    },
    {
        "question": "Who is the instructor for the course?",
        "answer": "Karen Jin, Associate Professor, Department of Applied Engineering and Sciences",
        "source": "Comp693.pdf"
    },
    {
        "question": "Where is the location of the course?",
        "answer": "Rm P142",
        "source": "Comp693.pdf"
    },
    {
        "question": "What is the Zoom link for the instructor's office hours?",
        "answer": "https://unh.zoom.us/j/4858446046",
        "source": "Comp693.pdf"
    },
    {
        "question": "What are the office hours for the instructor?",
        "answer": "Monday 1-4pm and Friday 9-noon",
        "source": "Comp693.pdf"
    },
    {
        "question": "What is the main focus of the internship course?",
        "answer": "To provide experiential learning experience through placement in team projects",
        "source": "Comp693.pdf"
    },
    {
        "question": "What are the student learning outcomes for the course?",
        "answer": "Analyzing complex computing problems, designing and implementing computing solutions, effective communication, functioning in a team, and identifying user needs",
        "source": "Comp693.pdf"
    },
    {
        "question": "What is covered in Week 1 of the tentative course schedule?",
        "answer": "Class Introduction, Development Team (DT) Setup, Intro to Project Management, Intro to Scrum workflow, Project Goal",
        "source": "Comp693.pdf"
    },
    {
        "question": "What is covered in Week 2 of the tentative course schedule?",
        "answer": "Project Kickoff, Environment Setup: Jira, Create Project backlog, Create user stories, tasks and bugs, Integration w/ Source code control, team communication",
        "source": "Comp693.pdf"
    }
]

var = [{"question": "What room is COMP690 in?", "expected_answer": "Room P142",
        "retrieval_context": ["Name: COMP690 Internship Experience", "Credits: 4", "Term: Fall 2024",
                              "Location: Rm P142", "Time: M2 Section: Wednesday 9:10am-12pm",
                              "M2 Section: Wednesday 1:10-4pm", "Instructor Information",
                              "Name: Karen Jin, Associate Professor, Department of Applied Engineering and Sciences",
                              "Office: Rm139, Pandora Mill building", "Zoom: https://unh.zoom.us/j/4858446046",
                              "Email: karen.jin@unh.edu",
                              "Office Hours: Monday 1-4pm and Friday 9-noon. Available in person or over Zoom."],
        "actual_answer": "COMP690 is held in Room P142. If you need any more details about the course or the location, feel free to ask!"},
       {"question": "What is the instructor's email?", "expected_answer": "karen.jin@unh.edu",
        "retrieval_context": ["Instructor Information",
                              "Name: Karen Jin, Associate Professor, Department of Applied Engineering and Sciences",
                              "Office: Rm139, Pandora Mill building", "Zoom: https://unh.zoom.us/j/4858446046",
                              "Email: karen.jin@unh.edu", "Office Hours: Monday 1-4pm and Friday 9-noon.",
                              "CaPS office: Website: https://manchester.unh.edu/careers/career-professional-success",
                              "Phone: (603) 641-4394", "Email: unhm.career@unh.edu"],
        "actual_answer": "Professor Karen Jin's email is karen.jin@unh.edu. If you have any more questions or need further assistance regarding the internship courses, feel free to reach out to her!"},
       {"question": "What time is COMP893?",
        "expected_answer": "COMP893 has two sections:\n- M1 Section: Wednesday 9:10am-12pm\n- M2 Section: Wednesday 1:10-4pm",
        "retrieval_context": ["Name: COMP893 Team Project Internship", "Credits: 1-3", "Term: Fall 2024",
                              "Location: Rm P142", "Time: M1 Section: Wednesday 9:10am-12pm",
                              "M2 Section: Wednesday 1:10-4pm", "Instructor Information",
                              "Name: Karen Jin, Associate Professor, Department of Applied Engineering and Sciences",
                              "Office: Rm139, Pandora Mill building", "Zoom: https://unh.zoom.us/j/4858446046",
                              "Email: karen.jin@unh.edu", "Office Hours: Monday 1-4pm and Friday 9-noon."],
        "actual_answer": "COMP893 Team Project Internship has two sections. The M1 section meets on Wednesdays from 9:10 am to 12:00 pm, and the M2 section meets on Wednesdays from 1:10 pm to 4:00 pm. Both are held in Room P142. Let me know if you need more information or have other questions!"},
       {"question": "When is week 1?", "expected_answer": "Week 1 starts on 8/28",
        "retrieval_context": ["Week 1: 8/28", "Class Introduction / Development Team (DT) Setup",
                              "Intro to Project Management", "Intro to Scrum workflow", "Project Goal", "Week 2: 9/4",
                              "Project Kickoff", "Environment Setup: Jira", "Create Project backlog",
                              "Create user stories, tasks, and bugs"],
        "actual_answer": "Week 1 for the internship program starts on August 28th. This week includes the class introduction, development team setup, and introductions to project management and the Scrum workflow. If you need more details about what to prepare or expect, feel free to ask!"},
       {"question": "How much of the grade is class attendance?", "expected_answer": "10%.",
        "retrieval_context": ["Your final grade consists of the following three components:",
                              "10% Class Attendance of all required meetings",
                              "60% Sprint Grade is calculated as: Teamwork Grade * Sprint Grade",
                              "Teamwork Grade is based on peer evaluation for each of the three sprints.",
                              "Sprint Grades: You will receive a team grade for each of the three sprints, based on the technical aspect of the product and team project management.",
                              "10% Homework: additional homework in project management and development tools.",
                              "20% Final Project Report: See Appendix A for the report format."],
        "actual_answer": "Class attendance is crucial and is factored into your overall grade for the internship courses like COMP690 and COMP893. While the specific percentage may vary by course and instructor, consistent attendance is expected to successfully meet course requirements and participate in team activities. If you have any specific concerns about attendance or need further details, please let me know!"},
       {"question": "How is sprint grade calculated?",
        "expected_answer": "The sprint grade is calculated as the Teamwork Grade multiplied by the Sprint Grade.",
        "retrieval_context": ["Your final grade consists of the following three components:",
                              "10% Class Attendance of all required meetings",
                              "60% Sprint Grade is calculated as: Teamwork Grade * Sprint Grade",
                              "Teamwork Grade is based on peer evaluation for each of the three sprints.",
                              "Sprint Grades: You will receive a team grade for each of the three sprints, based on the technical aspect of the product and team project management."],
        "actual_answer": "Sprint grades in courses like COMP690 and COMP893 are calculated based on the technical quality of the product your team develops and how effectively your team manages the project. The specific criteria for these evaluations are detailed in the course rubrics, which will be provided by your instructor. Each sprint contributes to your overall grade, emphasizing both your technical skills and teamwork. If you need more details about the grading rubrics or any other aspect of the sprints, feel free to ask!"},
       {"question": "CaPS office website?",
        "expected_answer": "The website for the CaPS office is [Career and Professional Success](https://manchester.unh.edu/careers/career-professional-success).",
        "retrieval_context": ["CaPS office:", "Website: https://manchester.unh.edu/careers/career-professional-success",
                              "Phone: (603) 641-4394", "Email: unhm.career@unh.edu",
                              "The Office of International Students and Scholars (OISS):",
                              "Website: https://www.unh.edu/global/international-students-scholars",
                              "Email: oiss@unh.edu"],
        "actual_answer": "The CaPS office website for UNH Manchester can be found at [https://manchester.unh.edu/careers/career-professional-success](https://manchester.unh.edu/careers/career-professional-success). It's a great resource for career advice, resume coaching, and more. If you need further assistance or have specific questions about internship opportunities, feel free to reach out to them!"},
       {"question": "How many credits is COMP890?",
        "expected_answer": "COMP890 is a 1-credit course in the UNH internship program.",
        "retrieval_context": ["Graduate students:", "COMP890: Internship and Career Planning.",
                              "This is a 1 cr course you need to take after the first semester to help you plan for the internship search process.",
                              "The course is offered in fall and spring semesters.", "COMP891: Internship Practice.",
                              "This is a variable credit 1-3 crs course that you will take when you have an external internship."],
        "actual_answer": "COMP890, the Internship Preparation course, requires a total of 1 credit. It's designed to prepare you for your internship experience, focusing on skills like resume writing, interview techniques, and workplace etiquette. If you have any more questions about this course or need further details, just let me know!"},
       {"question": "When is COMP890 offered?",
        "expected_answer": "COMP890 is offered in both the fall and spring semesters.",
        "retrieval_context": ["COMP890: Internship and Career Planning.",
                              "This is a 1 cr course you need to take after the first semester to help you plan for the internship search process.",
                              "The course is offered in fall and spring semesters."],
        "actual_answer": "COMP890, titled Internship and Career Planning, is offered every semester, including summers. This flexibility allows you to enroll in the course when it best fits your schedule and when you secure an internship. If you need help with the registration process or have any other questions about the course, just let me know!"},
       {"question": "Who do you need to email for internship courses?",
        "expected_answer": "To register for internship courses, you need to email the Internship Advisor, Karen Jin.",
        "retrieval_context": ["All internship courses require instructor\u2019s permission.",
                              "You will need to email the faculty internship coordinator, or the course instructor to register you for the course.",
                              "For more details, you may email Prof. Karen Jin.",
                              "How to register for Internship Courses?",
                              "Email the Internship Advisor, Karen Jin (karen.jin@unh.edu).",
                              "Provide details about your internship or project requirements.",
                              "Ensure to include your student ID in the email."],
        "actual_answer": "For registering in internship courses like COMP690, COMP890, COMP891, COMP892, and COMP893, you'll need to email the faculty internship coordinator or the course instructor for permission. You can reach out to Professor Karen Jin for this purpose. Her email is karen.jin@unh.edu. If you need more details or assistance with the process, feel free to ask!"}]

var = [
    {
        "question": "What room is COMP690 in?",
        "expected_answer": "Room P142",
        "retrieval_context": [
            "Name: COMP690 Internship Experience",
            "Credits: 4",
            "Term: Fall 2024",
            "Location: Rm P142",
            "Time: M2 Section: Wednesday 9:10am-12pm",
            "M2 Section: Wednesday 1:10-4pm",
            "Instructor Information",
            "Name: Karen Jin, Associate Professor, Department of Applied Engineering and Sciences",
            "Office: Rm139, Pandora Mill building",
            "Zoom: https://unh.zoom.us/j/4858446046",
            "Email: karen.jin@unh.edu",
            "Office Hours: Monday 1-4pm and Friday 9-noon. Available in person or over Zoom."
        ],
        "actual_answer": "COMP690 is held in Room P142. If you need any more details about the course or the location, feel free to ask!"
    },
    {
        "question": "What is the instructor's email?",
        "expected_answer": "karen.jin@unh.edu",
        "retrieval_context": [
            "Instructor Information",
            "Name: Karen Jin, Associate Professor, Department of Applied Engineering and Sciences",
            "Office: Rm139, Pandora Mill building",
            "Zoom: https://unh.zoom.us/j/4858446046",
            "Email: karen.jin@unh.edu",
            "Office Hours: Monday 1-4pm and Friday 9-noon.",
            "CaPS office: Website: https://manchester.unh.edu/careers/career-professional-success",
            "Phone: (603) 641-4394",
            "Email: unhm.career@unh.edu"
        ],
        "actual_answer": "Professor Karen Jin's email is karen.jin@unh.edu. If you have any more questions or need further assistance regarding the internship courses, feel free to reach out to her!"
    },
    {
        "question": "What time is COMP893?",
        "expected_answer": "COMP893 has two sections:\n- M1 Section: Wednesday 9:10am-12pm\n- M2 Section: Wednesday 1:10-4pm",
        "retrieval_context": [
            "Name: COMP893 Team Project Internship",
            "Credits: 1-3",
            "Term: Fall 2024",
            "Location: Rm P142",
            "Time: M1 Section: Wednesday 9:10am-12pm",
            "M2 Section: Wednesday 1:10-4pm",
            "Instructor Information",
            "Name: Karen Jin, Associate Professor, Department of Applied Engineering and Sciences",
            "Office: Rm139, Pandora Mill building",
            "Zoom: https://unh.zoom.us/j/4858446046",
            "Email: karen.jin@unh.edu",
            "Office Hours: Monday 1-4pm and Friday 9-noon."
        ],
        "actual_answer": "COMP893 Team Project Internship has two sections. The M1 section meets on Wednesdays from 9:10 am to 12:00 pm, and the M2 section meets on Wednesdays from 1:10 pm to 4:00 pm. Both are held in Room P142. Let me know if you need more information or have other questions!"
    },
    {
        "question": "When is week 1?",
        "expected_answer": "Week 1 starts on 8/28",
        "retrieval_context": [
            "Week 1: 8/28",
            "Class Introduction / Development Team (DT) Setup",
            "Intro to Project Management",
            "Intro to Scrum workflow",
            "Project Goal",
            "Week 2: 9/4",
            "Project Kickoff",
            "Environment Setup: Jira",
            "Create Project backlog",
            "Create user stories, tasks, and bugs"
        ],
        "actual_answer": "Week 1 for the internship program starts on August 28th. This week includes the class introduction, development team setup, and introductions to project management and the Scrum workflow. If you need more details about what to prepare or expect, feel free to ask!"
    },
    {
        "question": "How much of the grade is class attendance?",
        "expected_answer": "10%.",
        "retrieval_context": [
            "Your final grade consists of the following three components:",
            "10% Class Attendance of all required meetings",
            "60% Sprint Grade is calculated as: Teamwork Grade * Sprint Grade",
            "Teamwork Grade is based on peer evaluation for each of the three sprints.",
            "Sprint Grades: You will receive a team grade for each of the three sprints, based on the technical aspect of the product and team project management.",
            "10% Homework: additional homework in project management and development tools.",
            "20% Final Project Report: See Appendix A for the report format."
        ],
        "actual_answer": "Class attendance is crucial and is factored into your overall grade for the internship courses like COMP690 and COMP893. While the specific percentage may vary by course and instructor, consistent attendance is expected to successfully meet course requirements and participate in team activities. If you have any specific concerns about attendance or need further details, please let me know!"
    },
    {
        "question": "How is sprint grade calculated?",
        "expected_answer": "The sprint grade is calculated as the Teamwork Grade multiplied by the Sprint Grade.",
        "retrieval_context": [
            "Your final grade consists of the following three components:",
            "10% Class Attendance of all required meetings",
            "60% Sprint Grade is calculated as: Teamwork Grade * Sprint Grade",
            "Teamwork Grade is based on peer evaluation for each of the three sprints.",
            "Sprint Grades: You will receive a team grade for each of the three sprints, based on the technical aspect of the product and team project management."
        ],
        "actual_answer": "Sprint grades in courses like COMP690 and COMP893 are calculated based on the technical quality of the product your team develops and how effectively your team manages the project. The specific criteria for these evaluations are detailed in the course rubrics, which will be provided by your instructor. Each sprint contributes to your overall grade, emphasizing both your technical skills and teamwork. If you need more details about the grading rubrics or any other aspect of the sprints, feel free to ask!"
    },
    {
        "question": "CaPS office website?",
        "expected_answer": "The website for the CaPS office is [Career and Professional Success](https://manchester.unh.edu/careers/career-professional-success).",
        "retrieval_context": [
            "CaPS office:",
            "Website: https://manchester.unh.edu/careers/career-professional-success",
            "Phone: (603) 641-4394",
            "Email: unhm.career@unh.edu",
            "The Office of International Students and Scholars (OISS):",
            "Website: https://www.unh.edu/global/international-students-scholars",
            "Email: oiss@unh.edu"
        ],
        "actual_answer": "The CaPS office website for UNH Manchester can be found at [https://manchester.unh.edu/careers/career-professional-success](https://manchester.unh.edu/careers/career-professional-success). It's a great resource for career advice, resume coaching, and more. If you need further assistance or have specific questions about internship opportunities, feel free to reach out to them!"
    },
    {
        "question": "How many credits is COMP890?",
        "expected_answer": "COMP890 is a 1-credit course in the UNH internship program.",
        "retrieval_context": [
            "Graduate students:",
            "COMP890: Internship and Career Planning.",
            "This is a 1 cr course you need to take after the first semester to help you plan for the internship search process.",
            "The course is offered in fall and spring semesters.",
            "COMP891: Internship Practice.",
            "This is a variable credit 1-3 crs course that you will take when you have an external internship."
        ],
        "actual_answer": "COMP890, the Internship Preparation course, requires a total of 1 credit. It's designed to prepare you for your internship experience, focusing on skills like resume writing, interview techniques, and workplace etiquette. If you have any more questions about this course or need further details, just let me know!"
    },
    {
        "question": "When is COMP890 offered?",
        "expected_answer": "COMP890 is offered in both the fall and spring semesters.",
        "retrieval_context": [
            "COMP890: Internship and Career Planning.",
            "This is a 1 cr course you need to take after the first semester to help you plan for the internship search process.",
            "The course is offered in fall and spring semesters."
        ],
        "actual_answer": "COMP890, titled Internship and Career Planning, is offered every semester, including summers. This flexibility allows you to enroll in the course when it best fits your schedule and when you secure an internship. If you need help with the registration process or have any other questions about the course, just let me know!"
    },
    {
        "question": "Who do you need to email for internship courses?",
        "expected_answer": "To register for internship courses, you need to email the Internship Advisor, Karen Jin.",
        "retrieval_context": [
            "All internship courses require instructor\u2019s permission.",
            "You will need to email the faculty internship coordinator, or the course instructor to register you for the course.",
            "For more details, you may email Prof. Karen Jin.",
            "How to register for Internship Courses?",
            "Email the Internship Advisor, Karen Jin (karen.jin@unh.edu).",
            "Provide details about your internship or project requirements.",
            "Ensure to include your student ID in the email."
        ],
        "actual_answer": "For registering in internship courses like COMP690, COMP890, COMP891, COMP892, and COMP893, you'll need to email the faculty internship coordinator or the course instructor for permission. You can reach out to Professor Karen Jin for this purpose. Her email is karen.jin@unh.edu. If you need more details or assistance with the process, feel free to ask!"
    }
]

var = [
    {
        "question": "Who is the Faculty Internship Coordinator for UNH Manchester Computing Internship?",
        "expected_answer": "Karen Jin",
        "actual_answer": "The Faculty Internship Coordinator for UNH Manchester Computing Internship is Karen Jin.",
        "similarity_score": 0.8199030891449434,
        "is_correct": true
    },
    {
        "question": "What are the required internship courses for computing major students at UNH Manchester?",
        "expected_answer": "For undergraduate students: COMP690 Internship Experience. For graduate students: COMP890: Internship and Career Planning, COMP891: Internship Practice, COMP892: Applied Research Internship, COMP893: Team Project Internship.",
        "actual_answer": "\nFor undergraduate students majoring in Computer Information Systems (CIS) and Computer Science (CS) at UNH Manchester, the required internship course is COMP690 Internship Experience. This course has an applied research option for students who are currently working and a team project option for students in their last semester of the program.\n\nFor graduate students in the M.S. Information Technology and M.S. Cybersecurity Engineering majors, the required internship courses are COMP890: Internship and Career Planning, and COMP891: Internship Practice. COMP890 is a 1-credit course that helps students plan for the internship search process, offered in both fall and spring semesters. COMP891 is a variable credit course (1-3 credits) that students take when they have an external internship and need to register for at least 1 credit to apply for Curricular Practical Training (CPT).\n\nOverall, internship courses are mandatory for all computing major students at UNH Manchester, and each program has specific courses tailored to their level of study.",
        "similarity_score": 0.9004906057142543,
        "is_correct": true
    },
    {
        "question": "Where is the CaPS office located?",
        "expected_answer": "Rm139, Pandora Mill building",
        "actual_answer": "The CaPS office is located in room 426 on the UNH Manchester campus.",
        "similarity_score": 0.7494992694847489,
        "is_correct": false
    },
    {
        "question": "What is the email address for the CaPS office at UNH Manchester?",
        "expected_answer": "unhm.career@unh.edu",
        "actual_answer": "The email address for the CaPS office at UNH Manchester is unhm.library@unh.edu.",
        "similarity_score": 0.8983199556509442,
        "is_correct": true
    },
    {
        "question": "What is the website for the Office of International Students and Scholars (OISS) at UNH Manchester?",
        "expected_answer": "https://www.unh.edu/global/international-students-scholars",
        "actual_answer": "The website for the Office of International Students and Scholars (OISS) at UNH Manchester is https://www.unh.edu/global/international-students-scholars.",
        "similarity_score": 0.9251845833369492,
        "is_correct": true
    },
    {
        "question": "What is the course COMP890: Internship and Career Planning for graduate students?",
        "expected_answer": "It is a 1 credit course that helps students plan for the internship search process.",
        "actual_answer": "COMP893 Team Project Internship is a course designed for graduate students to gain practical skills and insights into the field of computing through placement in team projects. Students will work on collaborative projects with external stakeholders to develop real-world information technology products, processes, or services. The course aims to help students understand the challenges of implementing technology solutions in a professional setting. The course is offered in the fall semester and is taught by Associate Professor Karen Jin. Students will need to register for at least 1 credit to apply for CPT. To register for the course, students need to obtain permission from the instructor or the faculty internship coordinator. Students are encouraged to search for internships on platforms like Handshake, company websites, and job websites like LinkedIn, Indeed, and Hired. Attending internship fairs on campus and networking with family, friends, and faculty members are also recommended for finding internship opportunities.",
        "similarity_score": 0.8571457370593557,
        "is_correct": true
    },
    {
        "question": "What is the course COMP891: Internship Practice for graduate students?",
        "expected_answer": "It is a variable credit 1-3 crs course that students take when they have an external internship.",
        "actual_answer": "COMP893: Team Project Internship is a course designed for graduate students in their last semester of study who need to fulfill internship requirements. The course provides experiential learning through placement in team projects, allowing students to gain practical skills and insights into the field of computing. By working on collaborative projects with external stakeholders, students will contribute to the development of real-world information technology products, processes, or services. The course aims to help students understand the challenges involved in implementing technology solutions in a professional setting.\n\nThe course is offered in the fall and spring semesters, and students can earn 1-3 credits for their participation. To register for the course, students need to obtain instructor permission by contacting the faculty internship coordinator or the course instructor, Professor Karen Jin. Students are encouraged to start their internship search on platforms like Handshake, company websites, and job websites like LinkedIn, Indeed, and Hired. Additionally, attending internship fairs on both the Manchester and Durham campuses and networking with family, friends, and faculty can also help in finding internship opportunities.",
        "similarity_score": 0.8594388873412113,
        "is_correct": true
    },
    {
        "question": "What is the course COMP892: Applied Research Internship for graduate students?",
        "expected_answer": "It is a variable credit 1-3 crs course for students who are currently working full time or part time in the tech fields.",
        "actual_answer": "COMP892: Applied Research Internship is a course for graduate students who are currently working full-time or part-time in the tech fields. It is a variable credit course (1-3 credits) that provides students with the opportunity to gain practical skills and insights into the field of computing through applied research projects. Students will work on real-world information technology products, processes, or services and understand the challenges involved in implementing technology solutions in a professional setting. The course is offered in both fall and spring semesters, as well as during the summer. Students interested in taking COMP892 should contact the faculty internship coordinator or the course instructor for registration details.",
        "similarity_score": 0.8609414559075403,
        "is_correct": true
    },
    {
        "question": "What is the course COMP893: Team Project Internship for graduate students?",
        "expected_answer": "It is for students who are in their last semester of study and need to fulfill the internship requirements.",
        "actual_answer": "COMP893: Team Project Internship is a course designed for graduate students who are in their last semester of study and need to fulfill internship requirements. The course provides experiential learning through placement in team projects, allowing students to gain practical skills and insights into the field of computing. By working on collaborative projects with external stakeholders, students will contribute to the development of real-world information technology products, processes, or services. The course aims to help students understand the challenges involved in implementing technology solutions in a professional setting.\n\nThe course is offered in both fall and spring semesters, and students need to register for at least 1 credit to apply for Curricular Practical Training (CPT). To register for the course, students need to obtain instructor permission by contacting the faculty internship coordinator or the course instructor, Professor Karen Jin.\n\nStudents are encouraged to search for internship opportunities on platforms like Handshake, company websites, and job websites such as LinkedIn, Indeed, and Hired. Attending internship fairs on campus and networking with family, friends, and faculty members can also help in finding suitable internship opportunities.",
        "similarity_score": 0.8663850131744226,
        "is_correct": true
    },
    {
        "question": "How can students register for internship courses at UNH Manchester?",
        "expected_answer": "Students can register for internship courses through the UNH Manchester course registration system.",
        "actual_answer": "\n\u2022 Click on \"Request an Experience\" and fill the form\n\u2022 Your internship experience must be approved by your site supervisor and your\ncourse instructor\n\u2022 Make sure to include at least three well-developed learning objectives\nIf you have any questions related to registering your internship experience on handshake,\nplease contact Career and Professional Success office.\nWhile working at my internship, do I need to do anything else for this course?\nYes, you must complete the following requirements to earn the credit.\n\u2022 Attend every scheduled class meeting\n\u2022 Submit weekly logs\n\u2022 Complete a final internship report\n\u2022 Give progress presentations during the class\nPlease check the specific course syllabus for meeting dates and additional details.",
        "similarity_score": 0.8288402181778477,
        "is_correct": true
    },
    {
        "question": "What is the name of the course?",
        "expected_answer": "COMP 893 Team Project Internship",
        "actual_answer": "The name of the course is COMP 893: Team Project Internship.",
        "similarity_score": 0.9409715250719604,
        "is_correct": true
    },
    {
        "question": "Who is the instructor for the course?",
        "expected_answer": "Karen Jin, Associate Professor, Department of Applied Engineering and Sciences",
        "actual_answer": "The instructor for the COMP690 M2/M3 Internship Experience course is Karen Jin, Associate Professor in the Department of Applied Engineering and Sciences.",
        "similarity_score": 0.8904462939413573,
        "is_correct": true
    },
    {
        "question": "Where is the course located?",
        "expected_answer": "Rm P142",
        "actual_answer": "The course is located in Room P142.",
        "similarity_score": 0.8485332840714028,
        "is_correct": true
    },
    {
        "question": "What are the office hours for the instructor?",
        "expected_answer": "Monday 1-4pm and Friday 9-noon. Available in person or over Zoom. Email to make appointments.",
        "actual_answer": "The office hours for the instructor are not explicitly mentioned in the provided text. It is recommended to reach out to the instructor directly or refer to the course syllabus for information on their office hours.",
        "similarity_score": 0.8106727022186747,
        "is_correct": true
    },
    {
        "question": "What is the course description?",
        "expected_answer": "The internship course provides experiential learning experience through placement in team projects.",
        "actual_answer": "The COMP893 Team Project Internship course provides students with experiential learning experience through placement in team projects. Students will work on collaborative projects with external stakeholders to develop real-world information technology products, processes, or services. By doing so, students will gain practical skills and insights into the field of computing and understand the challenges involved in implementing technology solutions in a professional setting. The course aims to help students analyze complex computing problems, design and implement computing solutions, communicate effectively in professional contexts, and function effectively as a member or leader of a team engaged in IT activities.",
        "similarity_score": 0.9093486357767673,
        "is_correct": true
    },
    {
        "question": "What are the student learning outcomes for the course?",
        "expected_answer": "Analyzing complex computing problems, designing and implementing computing solutions, effective communication, functioning in a team, and identifying user needs.",
        "actual_answer": "The student learning outcomes for the course include:\n1. Demonstrate effective teamwork skills through peer evaluation and collaboration on team projects.\n2. Apply project management principles and development tools to successfully complete sprints and the final project.\n3. Develop technical skills related to product development and team project management.\n4. Create a comprehensive final project report that showcases the team's work and accomplishments.\n5. Manage time effectively to meet course requirements and deadlines.\n6. Communicate progress and updates effectively through progress presentations during the course.",
        "similarity_score": 0.824160114800678,
        "is_correct": true
    },
    {
        "question": "What is the tentative course schedule for Week 1?",
        "expected_answer": "Class Introduction, Development Team (DT) Setup, Intro to Project Management, Intro to Scrum workflow, and Project Goal.",
        "actual_answer": "Week 1:\n- Class Introduction / Development Team (DT) Setup\n- Introduction to Project Management\n- Introduction to Scrum workflow\n- Project Goal\n\nPlease note that this schedule is subject to change and may be adjusted based on the progress of the class.",
        "similarity_score": 0.9315920977729168,
        "is_correct": true
    },
    {
        "question": "What is the tentative course schedule for Week 2?",
        "expected_answer": "Project Kickoff, Environment Setup: Jira, Create Project backlog, Create user stories, tasks and bugs, and Integration w/ Source code control, team communication.",
        "actual_answer": "The tentative course schedule for Week 2 includes the following activities:\n- Project Kickoff\n- Environment Setup: Jira\n  - Create Project backlog\n  - Create user stories, tasks, and bugs\n  - Integration with Source code control, team communication\n\nThese activities are scheduled for 9/4.",
        "similarity_score": 0.8922835991330769,
        "is_correct": true
    },
    {
        "question": "What is the Zoom link for the instructor?",
        "expected_answer": "https://unh.zoom.us/j/4858446046",
        "actual_answer": "The Zoom link for the instructor Karen Jin is https://unh.zoom.us/j/4858446046.",
        "similarity_score": 0.9233855836808691,
        "is_correct": true
    },
    {
        "question": "When is the course term for COMP 893 Team Project Internship?",
        "expected_answer": "Fall 2024",
        "actual_answer": "The course term for COMP 893 Team Project Internship is Fall 2024.",
        "similarity_score": 0.8474323445289067,
        "is_correct": true
    },
    {
        "question": "What is the name of the internship course?",
        "expected_answer": "COMP690 Internship Experience",
        "actual_answer": "The name of the internship course is COMP 893 Team Project Internship.",
        "similarity_score": 0.8656477324598868,
        "is_correct": true
    },
    {
        "question": "How many credits does the internship course offer?",
        "expected_answer": "4",
        "actual_answer": "The internship course offers variable credits, ranging from 1-3 credits.",
        "similarity_score": 0.7595617790723146,
        "is_correct": false
    },
    {
        "question": "Who is the instructor for the course?",
        "expected_answer": "Karen Jin, Associate Professor, Department of Applied Engineering and Sciences",
        "actual_answer": "The instructor for the COMP690 M2/M3 Internship Experience course is Karen Jin, Associate Professor in the Department of Applied Engineering and Sciences.",
        "similarity_score": 0.8904462939413573,
        "is_correct": true
    },
    {
        "question": "Where is the location of the course?",
        "expected_answer": "Rm P142",
        "actual_answer": "The location of the course is Room P142.",
        "similarity_score": 0.847475960541966,
        "is_correct": true
    },
    {
        "question": "What is the Zoom link for the instructor's office hours?",
        "expected_answer": "https://unh.zoom.us/j/4858446046",
        "actual_answer": "Unfortunately, the Zoom link for the instructor's office hours is not provided in the given information. It is recommended to reach out to the instructor directly or check the course syllabus for the Zoom link.",
        "similarity_score": 0.8092569679449124,
        "is_correct": true
    },
    {
        "question": "What are the office hours for the instructor?",
        "expected_answer": "Monday 1-4pm and Friday 9-noon",
        "actual_answer": "The office hours for the instructor are not explicitly mentioned in the provided text. It is recommended to reach out to the instructor directly or refer to the course syllabus for information on their office hours.",
        "similarity_score": 0.7883332471852886,
        "is_correct": false
    },
    {
        "question": "What is the main focus of the internship course?",
        "expected_answer": "To provide experiential learning experience through placement in team projects",
        "actual_answer": "The main focus of the internship course is to provide students with experiential learning experience through placement in team projects. This hands-on experience allows students to gain practical skills and insights into the field of computing. By working on a collaborative project with external stakeholders, students will contribute to the development of real-world information technology products, processes, or services, and understand the challenges involved in implementing technology solutions in a professional setting. The course aims to help students analyze complex computing problems, design and implement computing solutions, communicate effectively in professional contexts, and function effectively as a member or leader of a team engaged in IT activities.",
        "similarity_score": 0.8803831687278489,
        "is_correct": true
    },
    {
        "question": "What are the student learning outcomes for the course?",
        "expected_answer": "Analyzing complex computing problems, designing and implementing computing solutions, effective communication, functioning in a team, and identifying user needs",
        "actual_answer": "The student learning outcomes for the course include:\n1. Demonstrate effective teamwork skills through peer evaluation and collaboration on team projects.\n2. Apply project management principles and development tools to successfully complete sprints and the final project.\n3. Develop technical skills related to product development and project management.\n4. Create a comprehensive final project report that showcases the team's work and accomplishments.\n5. Manage time effectively to meet project deadlines and requirements.\n6. Communicate effectively with team members, instructors, and site supervisors during the internship experience.\n7. Reflect on and evaluate personal learning and growth throughout the course and internship experience.",
        "similarity_score": 0.8191385405417804,
        "is_correct": true
    },
    {
        "question": "What is covered in Week 1 of the tentative course schedule?",
        "expected_answer": "Class Introduction, Development Team (DT) Setup, Intro to Project Management, Intro to Scrum workflow, Project Goal",
        "actual_answer": "Week 1 of the tentative course schedule covers the following topics:\n- Class Introduction / Development Team (DT) Setup\n- Introduction to Project Management\n- Introduction to Scrum workflow\n- Project Goal",
        "similarity_score": 0.9219017352003784,
        "is_correct": true
    },
    {
        "question": "What is covered in Week 2 of the tentative course schedule?",
        "expected_answer": "Project Kickoff, Environment Setup: Jira, Create Project backlog, Create user stories, tasks and bugs, Integration w/ Source code control, team communication",
        "actual_answer": "In Week 2 of the tentative course schedule, the following activities are covered:\n- Project Kickoff\n- Environment Setup: Jira\n  - Create Project backlog\n  - Create user stories, tasks, and bugs\n  - Integration with Source code control, team communication",
        "similarity_score": 0.9110555209735731,
        "is_correct": true
    }
]
test_cases= [
    {"question": "When does the first sprint begin?", "expected_answer": "The first sprint for COMP893 begins on September 18th, when the development starts along with Scrum meetings"},
    {"question": "How often are scrum meetings during the first sprint?", "expected_answer": "During the first sprint of COMP893, scrum meetings are held three times a week: on Monday, Wednesday, and Friday ."},
    {"question": "When does the first sprint end?", "expected_answer": "The first sprint for COMP893 ends on October 2nd, which is also when the Sprint Review and Sprint Retrospective will take place."},
    {"question": "What's involved in a sprint retrospective?", "expected_answer": "Reviewing the sprint and identifying areas for improvement."},
    {"question": "When is the second sprint planning meeting?", "expected_answer": "The second sprint planning meeting for COMP893 is scheduled for October 9th during Week 7."},
    {"question": "When does the second sprint start?", "expected_answer": "The second sprint for COMP893 starts on October 9th, during Week 7"},
    {"question": "Does the scrum meeting schedule change during the second sprint?", "expected_answer": " Yes, the scrum meeting schedule does change during the second sprint. In Week 7, after the 2nd Sprint Planning meeting on 10/9, scrum meetings are held on Fridays. In Week 8, the schedule changes to meetings on Wednesday and Friday. Then in Week 9, meetings occur on Monday, Wednesday, and Friday. So, the schedule evolves throughout the sprints."},
    {"question": "When is fall Break?", "expected_answer": "Thanksgiving Break for COMP893 is from November 20th to November 27th"},
    {"question": "What's the focus of week 3?", "expected_answer": "Environment setup (Jira), creating the project backlog, user stories, tasks, and bugs; integration with source control, team communication, and a sprint planning meeting."},
    {"question": "When are scrum meetings held only on Mondays?", "expected_answer": "scrum meetings are held on Mondays only during Week 14 (starting on November 27) and Week 15 (starting on December 4)"},
    {"question": "What happens during week 10?", "expected_answer": "Scrum meetings (Monday, Wednesday, Friday)."},
    {"question": "When is the sprint review for the first sprint?", "expected_answer": "The Sprint Review for the first sprint in COMP893 is scheduled for the end of Week 6, specifically on October 2nd."},
    {"question": "What are the activities for Week 9?", "expected_answer": "Scrum meetings (Monday, Wednesday, Friday)."},
    {"question": "When does the third sprint start?", "expected_answer": "The third sprint for COMP893 starts on November 13, during Week 12"},
    {"question": "How often are scrum meetings in week 13?", "expected_answer": "scrum meetings are held on Monday, Wednesday, and Friday"},
    {"question": "What is the project goal?", "expected_answer": "The project goal for COMP893 involves working collaboratively on a real-world internship project that allows students to apply the Scrum framework. The focus is to introduce a project by discussing its background, objectives, and the significance of using Scrum. Additionally, students will set up the project environment, create backlogs, and plan sprints, with an end goal of delivering a final report that encapsulates their experiences and outcomes."},
    {"question": "What tools are used for project management?", "expected_answer": "Jira is used for project management."},
    {"question": "What is the purpose of sprint planning?", "expected_answer": "To create a plan for the upcoming sprint based on the Product Backlog."}
]
test_cases = [
    {"question": "What should be included in my self-assessment?", "expected_answer": "Your self-assessment should address: what you learned, the project's relevance to your major, the benefits you gained, a comparison of theory (classroom learning) and practice (internship experience), how project activities correlated with classroom knowledge, how the project will influence your future career, reflections on your internship experience (including skills needing development), and advice for a fellow student or faculty member."},
    {"question": "What comparison should I make in the self-assessment?", "expected_answer": "Compare theory (classroom learning) and practice (your internship experiences)."},
    {"question": "How should I discuss the project's influence on my future career?", "expected_answer": "Explain how the project and internship experiences will affect your future career goals and plans."},
    {"question": "What reflections should be included in the self-assessment?", "expected_answer": "Describe what you learned, how it will be applied to your career, what additional skills you need to develop, and any advice you would offer to others, Describe how the experiences and skills acquired during the internship will apply to your professional goals."},
    {"question": "What's the minimum length for the self-assessment section?", "expected_answer": "For COMP893, the self-assessment section of your report should be 1 full page long, not including spacing, figures, and tables. Make sure to reflect on what you learned from your internship experience in that section."},
    {"question": "What should the conclusion section include?", "expected_answer": "A summary of key conclusions from your project experience."},
    {"question": "How long should the conclusion section be?", "expected_answer": "the conclusion section should be 1 full page long. Make sure it's single-spaced and follows the overall formatting requirements."},
    {"question": "What's the required spacing for the report?", "expected_answer": "you should use single spacing throughout the document. The report must be 6-8 pages long, not including the title page, figures, and tables."},
    {"question": "How many pages should the report be (excluding title page, figures, tables)?", "expected_answer": "It should be between 6 to 8 pages long, excluding the title page, figures, and tables. Make sure to format it with single-spaced lines, use size 12 Times New Roman font, and include no additional white space between paragraphs and sections."},
    {"question": "What font size is required?", "expected_answer": "you must use size 12 in Times New Roman font."},
    {"question": "What are the grading criteria for the report?", "expected_answer": "60% Content, 20% Grammar and Mechanics, 20% Format."},
    {"question": "What happens if my report is too short?", "expected_answer": "If your report is too short, you might face a penalty, and it's best to communicate with your instructor about the situation. They may provide you guidance on how to address the issue before submission."},
    {"question": "What's the minimum grade needed on the final report to pass?", "expected_answer": "you need to earn a minimum of 75% on your final report."},
    {"question": "Can I use bullet points in my report?", "expected_answer": "In your report, you should use full sentences instead of bullet points."},
    {"question": "How should I present tables and figures?", "expected_answer": "All tables and figures must be captioned."},
    {"question": "Can I use a different font than Times New Roman?", "expected_answer": "The formatting requirement specifies that you must use size 12 in Times New Roman font. So unfortunately, you can't use a different font than Times New Roman."},
    {"question": "What's the minimum length for the conclusion?", "expected_answer": "For the conclusion in final report, it should be at least one full page. This section should summarize the key conclusions derived from your project experience."},
    {"question": "What additional skills should I mention for career readiness?", "expected_answer": "Mention skills like learning new technologies, networking, or additional coursework."},
    {"question": "What kind of advice should I give to others?", "expected_answer": "Advice based on your internship experience and what you learned."},
    {"question": "What should my reflection on the internship experience cover?", "expected_answer": "What you learned, how it applies to your career goals, additional skills needed for career readiness, and any advice for others."}
]
