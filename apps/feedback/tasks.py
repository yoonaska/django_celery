from time import sleep
from django.core.mail import send_mail
from celery import shared_task
from threading import Lock


@shared_task(bind=True)
def send_feedback_email_task(self, email_address, message):
    """Sends an email when the feedback form has been submitted."""
    # print('aaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaa')
    send_mail(
        "Your Feedback 2121",
        f"{message} Thank you!",
        "test@yopmail.com.com",
        [email_address],
        fail_silently=False,
    )
    for i in range(0, 10):
        print(i)
    # print('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
    
    return "Completed send_feedback_email_task"
    
    

@shared_task(bind=True)
def send_mail_task(self):
    send_mail(
        "Your Feedback 2121",
        "Test hf hfhfh hfh fgh Thank you!",
        "test@yopmail.com.com",
        ['test@yopmail.com.com'],
        fail_silently=False,
    )
    
    
    return "Completed send_feedback_email_task"
    