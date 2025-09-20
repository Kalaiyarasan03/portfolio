from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def chat(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "").lower()
        reply = "Sorry, I didn’t understand that."
        return JsonResponse({"reply": reply})

@csrf_exempt
def chat(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_msg = data.get("message", "").lower().strip()
            
            # Collect all matching responses
            responses = []
            
            # Greetings
            if any(word in user_msg for word in ["hello", "hi", "hey", "good morning", "good evening", "greetings"]):
                responses.append("Hi, I'm Kalaiyarasan! 👋")
            
            # About/Introduction
            if any(word in user_msg for word in ["about", "who are you", "introduce", "yourself"]):
                responses.append("I'm a full-stack developer with expertise in Django, and backend automation. I'm passionate about creating efficient, scalable web applications.")
            
            # Experience & Projects
            if any(word in user_msg for word in ["experience", "worked", "projects", "portfolio", "built", "developed"]):
                responses.append("I've worked on e-commerce platforms, portfolio websites, task automation systems, and data visualization dashboards. Each project showcases different aspects of full-stack development.")
            
            # Skills & Technologies
            if any(word in user_msg for word in ["skills", "technologies", "tech stack", "programming", "languages", "tools"]):
                responses.append("My skills include Python, Django, JavaScript, SQL, REST API development, Git, Docker, and cloud deployment. I'm also experienced with frontend frameworks and database design.")
            
            # Education & Learning
            if any(word in user_msg for word in ["education", "degree", "study", "university", "college", "certification"]):
                responses.append("I hold a degree in Computer Science and have completed various web development certifications. I believe in continuous learning and stay updated with the latest technologies.")
            
            # Contact Information
            if any(word in user_msg for word in ["contact", "email", "phone", "reach", "hire", "collaboration"]):
                responses.append("You can reach me at kalaiyarasanrasantech@gmail.com or +91 9443414323. I'm always open to discussing new opportunities and collaborations!")
            
            # Hobbies & Interests
            if any(word in user_msg for word in ["hobby", "hobbies", "interests", "free time", "passion"]):
                responses.append("I enjoy coding side projects, learning new technologies, contributing to open-source projects, and exploring emerging tech trends like AI and cloud computing.")
            
            # Career & Goals
            if any(word in user_msg for word in ["career", "goals", "future", "ambition", "aspiration"]):
                responses.append("My goal is to become a senior full-stack developer and eventually lead development teams. I'm interested in scalable architecture and mentoring other developers.")
            
            # Specific Technologies - Python/Django
            if any(word in user_msg for word in ["python", "django", "flask"]):
                responses.append("Python is my primary backend language. I'm proficient in Django for web applications and have experience with Flask for lightweight APIs.")
            
            # JavaScript/React
            if any(word in user_msg for word in ["javascript", "react", "frontend", "js"]):
                responses.append("I use JavaScript extensively for frontend development, with React being my preferred framework. I also work with modern ES6+ features and responsive design.")
            
            # Database
            if any(word in user_msg for word in ["database", "sql", "mysql", "postgresql"]):
                responses.append("I work with both SQL and NoSQL databases. My experience includes PostgreSQL, MySQL, and MongoDB, with a focus on efficient query design and database optimization.")
            
            # API Development
            if any(word in user_msg for word in ["api", "rest", "backend"]):
                responses.append("I specialize in building RESTful APIs with proper authentication, error handling, and documentation. I've created APIs for various applications including e-commerce and data management systems.")
            
            # Work Style & Approach
            if any(word in user_msg for word in ["work style", "approach", "methodology", "process"]):
                responses.append("I follow agile development practices, write clean and maintainable code, and believe in thorough testing. I'm comfortable working both independently and in collaborative team environments.")
            
            # Location & Availability
            if any(word in user_msg for word in ["location", "where", "available", "remote", "work"]):
                responses.append("I'm based in Thiruvananthapuram, Kerala, India. I'm open to both remote work and on-site opportunities, depending on the project requirements.")
            
            # Problem Solving
            if any(word in user_msg for word in ["problem", "solve", "debug", "troubleshoot", "challenge"]):
                responses.append("I enjoy tackling complex problems and have experience debugging issues across the full stack. I approach problems methodically and document solutions for future reference.")
            
            # E-commerce
            if any(word in user_msg for word in ["ecommerce", "e-commerce", "shop", "store"]):
                responses.append("I've built e-commerce platforms with features like user authentication, product catalogs, shopping carts, payment integration, and order management systems.")
            
            # Automation
            if any(word in user_msg for word in ["automation", "scripts", "workflow"]):
                responses.append("I've created automation scripts for data processing, report generation, and workflow optimization. I believe in automating repetitive tasks to improve efficiency.")
            
            # Thank you responses
            if any(word in user_msg for word in ["thank", "thanks", "appreciate"]):
                responses.append("You're welcome! Feel free to ask if you have any other questions about my background or experience.")
            
            # Help requests
            if any(word in user_msg for word in ["help", "assist", "support", "question"]):
                responses.append("I'm here to help! You can ask me about my skills, experience, projects, education, or how to get in touch. What would you like to know?")
            
            # Default response
            if not responses:
                responses.append("I didn't quite catch that. You can ask me about:\n• My skills and technologies\n• Work experience and projects\n• Education and certifications\n• How to contact me\n• My hobbies and interests\n• Specific technologies like Python, Django, or React")
            
            # Return the first matching response
            return JsonResponse({"reply": responses[0]})
            
        except json.JSONDecodeError:
            return JsonResponse({"reply": "Sorry, I couldn't process your message."})
        except Exception as e:
            return JsonResponse({"reply": "Sorry, something went wrong. Please try again."})
    
    return JsonResponse({"reply": "Invalid request method."})
   