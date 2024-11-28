from typing import List
from celery import Celery
from src.mail import create_message, mail
from asgiref.sync import async_to_sync





client = Celery(backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')
client.config_from_object("src.config")