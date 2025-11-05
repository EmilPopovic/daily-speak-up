from .celery_app import app
from .sender import ResendEmailSender

@app.task(rate_limit='2/s')
def send_email_task(to_mail: str, subject: str) -> None:
    
    sender = ResendEmailSender()

    sender.send_email(
        to_email=to_mail,
        subject=subject,
        body=""
    )