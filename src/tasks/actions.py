from src.tasks.celery import client
from typing import List
from src.mail import create_message, mail
from asgiref.sync import async_to_sync




# celery task
@client.task
def send_email(recipient: List[str], subject: str, html_message: str):
    message = create_message(recipient=recipient, subject=subject, body=html_message)
    print("CELERY OK (1) - Message created.")

    async_to_sync(mail.send_message)(message)
    print("CELERY OK (2) - Message sent.")





@client.task
def add(x, y):
    return x + y