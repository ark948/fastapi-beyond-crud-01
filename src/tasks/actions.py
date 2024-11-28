from src.tasks.celery import client
from typing import List
from src.mail import create_message, mail
from asgiref.sync import async_to_sync




# celery task
@client.task
def send_email(recipient: List[str], subject: str, body: str):
    try:
        message = create_message(recipient=recipient, subject=subject, body=body)
        print("CELERY OK (1) - Message created.")
    except Exception as error:
        print("CELERY Email was not CREATED.")

    try:
        async_to_sync(mail.send_message)(message)
        print("CELERY OK (2) - Message sent.")
    except Exception as error:
        print("CELERY Email was not SENT.")





@client.task
def add(x, y):
    print("Calling add...")
    return x + y