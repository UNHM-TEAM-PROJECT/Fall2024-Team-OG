import unittest
from chatbot import Chatbot  # Ensure chatbot.py is in the same directory

class TestChatbot(unittest.TestCase):
    def setUp(self):
        self.chatbot = Chatbot()

    def test_greeting(self):
        self.assertEqual(self.chatbot.respond("Hello"), "I'm not sure about that. Can you ask something else?")  

    def test_class_attendance(self):
        self.assertEqual(self.chatbot.respond("What about class attendance?"), "Class attendance accounts for 10% of your final grade.")
    
    def test_final_grade_calculation(self):
        self.assertEqual(self.chatbot.respond("How is the final grade calculated?"), 
                         "The final grade consists of Class Attendance, Sprint Grade, Homework, and Final Project Report.")

    def test_sprint_grade_info(self):
        self.assertEqual(self.chatbot.respond("What is the sprint grade?"), "The Sprint Grade is based on teamwork and technical aspects of the project.")
    
    def test_homework_requirements(self):
        self.assertEqual(self.chatbot.respond("What are the homework requirements?"), "You'll have additional homework focused on project management and development tools.")
    
    def test_final_project_report_format(self):
        self.assertEqual(self.chatbot.respond("What is the final project report format?"), "Please refer to Appendix A for the specific report format requirements.")
    
    def test_class_attendance_percentage(self):
        self.assertEqual(self.chatbot.respond("What percentage is class attendance?"), "Class attendance accounts for 10% of your final grade.")

    def test_unrecognized_input(self):
        self.assertEqual(self.chatbot.respond("Unknown question"), "I'm not sure about that. Can you ask something else?")

    def test_additional_responses(self):
        self.assertEqual(self.chatbot.respond("What is the role of the product owner?"), "The Product Owner prioritizes the backlog for the team.")
        self.assertEqual(self.chatbot.respond("How long is a daily scrum?"), "Daily Scrums are typically 15 minutes long.")

if __name__ == '__main__':
    unittest.main()
