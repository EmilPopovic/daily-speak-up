from celery import Task
from .celery_app import app

@app.task
def send_email_task(to_mail: str, subject: str) -> None:
    # Worker function to send email
    # uses ResendEmailSender to send the email
    pass