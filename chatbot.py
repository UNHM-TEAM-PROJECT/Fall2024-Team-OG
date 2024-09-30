class Chatbot:
    def respond(self, user_input):
        # Dictionary of possible responses
        responses = {
            "hello": "Hi there! How can I assist you today?",
            "class attendance": "Class attendance accounts for 10% of your final grade.",
            "how is the final grade calculated": "The final grade consists of Class Attendance, Sprint Grade, Homework, and Final Project Report.",
            "what is the sprint grade": "The Sprint Grade is based on teamwork and technical aspects of the project.",
            "what are the homework requirements": "You'll have additional homework focused on project management and development tools.",
            "what is the final project report format": "Please refer to Appendix A for the specific report format requirements.",
            "credit hour workload": "You should anticipate a minimum of 45 hours of academic work per credit per term.",
            "peer evaluation": "Peer evaluation assesses your teamwork throughout the sprints.",
            "what are sprint events": "Key events include Sprint Planning, Daily Scrum meetings, and Sprint Release.",
            "what are daily scrum meetings": "Daily Scrums are short meetings where team members share updates.",
            "what is sprint planning importance": "Sprint Planning sets the stage for your work in the sprint.",
            "feedback on teamwork": "Feedback will come through peer evaluations and guidance from your Project Manager.",
            "how to manage conflicts": "Address conflicts directly, and consider involving your Project Manager if needed.",
            "how to set sprint goals": "Sprint goals should be SMART: specific, measurable, achievable, relevant, and time-bound.",
            "using development tools": "Specific tools will be outlined in your homework.",
            "how to evaluate technical performance": "Technical performance is evaluated based on the quality of your project deliverables.",
            "how to wrap up after sprints": "Conduct a Sprint Review and a Retrospective after each sprint.",
            "what is the sprint release process": "The Sprint Release involves presenting your completed work to stakeholders.",
            "impact of absences": "Missing a class can impact your attendance grade.",
            "learning objectives": "You'll gain practical experience in project management and teamwork.",
            "role of the product owner": "The Product Owner prioritizes the backlog for the team.",
            "how long is a daily scrum": "Daily Scrums are typically 15 minutes long.",
            "handling deadlines": "Deadlines are set during Sprint Planning and monitored through Daily Scrums.",
            "evaluating homework": "Homework will be graded based on completeness and understanding.",
            "what is retrospective purpose": "The Retrospective allows the team to reflect on the sprint.",
            "time management tips": "Use a planner, set priorities, and stay proactive with communication.",
            "resources for learning scrum": "There are many resources online for learning Scrum.",
            "understanding artifacts": "Scrum artifacts include the Product Backlog, Sprint Backlog, and Increment.",
            "how to deal with team member absence": "Keep everyone updated with notes if a team member misses a meeting.",
            "evaluating project risks": "Identify risks during Sprint Planning and create mitigation strategies.",
            "daily scrum tips": "Stick to the three questions: updates, plans, blockers.",
            "stakeholder feedback": "Gather feedback during the Sprint Review.",
            "building team cohesion": "Foster communication and trust; consider team-building activities.",
            "how to manage scope creep": "Stick to the agreed backlog to manage scope creep.",
            "using agile principles": "Agile principles emphasize flexibility and collaboration.",
            "preparing for sprint reviews": "Ensure deliverables are ready for presentation.",
            "celebrating sprint success": "Consider a team outing or small rewards for success.",
            "learning from failures": "Analyze what went wrong during the Retrospective.",
            "balancing workload": "Assess task assignments regularly to ensure fair distribution.",
            "communicating with the project manager": "Maintain regular updates and transparency.",
            "establishing team norms": "Set clear norms regarding communication and collaboration.",
            "utilizing feedback loops": "Regular assessments of work allow for adjustments based on input.",
            "handling diverse team members": "Embrace diversity by encouraging open discussions.",
            "aligning with project vision": "Revisit the project vision during meetings.",
            "using burndown charts": "Burndown charts track remaining work visually.",
            "collaborative decision-making": "Prioritize consensus and ensure everyone’s voice is heard.",
            "understanding the increment": "An Increment is the sum of all completed work during a sprint.",
            "importance of adaptability": "Adaptability allows your team to respond to changes.",
            "managing expectations": "Keep stakeholders informed about progress and set realistic goals.",
            "post-internship reflections": "Consider what you learned and how to apply it in the future."
        }

        # Convert user input to lowercase for case-insensitive matching
        user_input_lower = user_input.lower()

        # Loop through the responses dictionary and return the matching response
        for key in responses:
            if key in user_input_lower:
                return responses[key]

        # Default response if no match is found
        return "I'm not sure about that. Can you ask something else?"
