from django.shortcuts import render
from time import sleep
from django.core.mail import send_mail
from django.http import HttpResponse
from apps.feedback.tasks import send_feedback_email_task


class FeedbackForm():
    def __init__(self,):
        ...
    
    
    def send_email(self,):
        """Sends an email when the feedback form has been submitted."""
        # sleep(20)  # Simulate expensive operation(s) that freeze Django
        # send_mail(
        #     "Your Feedback",
        #     "test message  Thank you!",
        #     "test@yopmail.com.com",
        #     ['test@yopmail.com.com'],
        #     fail_silently=False,
        # )
        
        
        send_feedback_email_task.delay(
            "test@yopmail.com.com", "fgdfgdfg dgd jhdg kdhgjdghdkdkfj"
        )
    
        return HttpResponse("Done")