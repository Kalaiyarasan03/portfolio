from django.shortcuts import render

def home(request): return render(request, 'home.html')
def skills(request): return render(request, 'skills.html')
def projects(request): return render(request, 'projects.html')
def education(request): return render(request, 'education.html')
def experience(request): return render(request, 'experience.html')
def certifications(request): return render(request, 'certifications.html')
# your_app/views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages # Import the messages framework

def contact(request):
    return render(request, 'contact.html') # Assumes your template is named contact.html

def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Construct the email content
        email_content = f"""
        New message from: {name} ({email})
        -----------------------------------
        Subject: {subject}
        -----------------------------------
        Message:
        {message}
        """

        try:
            # Send the email
            send_mail(
                f"Portfolio Contact: {subject}",  # Email subject
                email_content,                    # Email body
                'kalaiyarasantech@gmail.com',           # From email (must be same as EMAIL_HOST_USER)
                ['kalaiyarasantech@gmail.com'], # To email (where you want to receive the mail)
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully! Thank you.")
        except Exception as e:
            messages.error(request, f"Sorry, there was an error sending your message. Please try again. Error: {e}")

        return redirect('contact') # Redirect back to the contact page

    # If not a POST request, just redirect to the contact page
    return redirect('contact')
