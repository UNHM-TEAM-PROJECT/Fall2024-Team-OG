**UNH Manchester Internship Program Chatbot** 

This chatbot is designed to assist students with navigating the internship requirements and coursework for UNH Manchester's internship program.

**Prerequisites**


Before running the chatbot, ensure you have the following installed:

1. Python 3.7 or higher

2. pip (Python package installer)
Installation

3. Clone the repository:
git clone [repository-url]
cd [repository-directory]

**Create a virtual environment:**
text
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`

Install the required packages:
text
pip install -r requirements.txt

**Set up your OpenAI API key:**

**Create a .env file in the project root**
Add your API key: OPENAI_API_KEY=your-api-key-here
Usage

Start the Flask server:text

Run
python chatbot.py

Open a web browser and navigate to http://localhost:8080

Interact with the chatbot through the web interface
Features
Processes and analyzes PDF documents for internship information
Utilizes OpenAI's language models for natural language understanding
Stores chat history in a SQLite database
Provides course-specific information for both undergraduate and graduate levels
Handles various types of queries related to internships and coursework
Project Structure

**chatbot.py:**

Main application file

**templates/index.html:**

Web interface template
embeddings/: Directory for storing document embeddings

chat_history.db: SQLite database for chat history

deqna.json: JSON file containing test cases for the chatbot
Customization

To add or modify the chatbot's knowledge base:
Add new PDF documents to the designated PDF directory

Run the document processing script to update embeddings
Adjust the DocumentProcessor class in chatbot.py if needed
Troubleshooting

If you encounter database errors, check the chat_history.db file permissions
For OpenAI API issues, verify your API key and internet connection
Contributing

**DeepEval Testing**

We use DeepEval for comprehensive testing of our chatbot's performance. DeepEval helps us ensure the quality and reliability of our AI responses.

**Install requirements for Deepeval**

1. pip install deepeval
2. Set up your test cases in the deqna.json file.
3. Run the tests:python -m deepeval run

**Deployment**

Our chatbot application is deployed on Amazon EC2 (Elastic Compute Cloud) instances. Here's an overview of the deployment process:
Create an EC2 Instance:

1. Launch a new instance from the EC2 console

2. Choose an Amazon Machine Image (AMI), typically Amazon Linux
3. Select an appropriate instance type (e.g., t2.micro for free tier)
4. Configure a key pair for secure SSH access
5. Set up security groups to control traffic
6. Connect to the Instance:
7. Use SSH to connect to your EC2 instance
8. For Windows instances, retrieve the initial administrator password
Set Up the Environment:
9. Install necessary software (e.g., Python, Flask, required libraries)
10. Transfer application code to the EC2 instance
11. Configure the application (e.g., set environment variables)
12. 
**Running the Application:**
1. Start the Flask application using Gunicorn or a similar WSGI server
2. Configure the application to run on startup
3. Configure Networking:
4. Set up a domain name (if applicable)
5. Configure SSL/TLS for HTTPS (recommended)
6. Monitor and Maintain:
7. Remember to follow AWS best practices for security and cost management when deploying your application.
