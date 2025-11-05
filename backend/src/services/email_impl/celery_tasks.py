from .celery_app import app
from .sender import ResendEmailSender

@app.task(rate_limit='2/s')
def send_email_task(to_mail: str, subject: str, body_text: str) -> None:
    """
        This is a celery worker function that reads basic information about an email, assembles it 
        and sends it using ResendEmailSender.

        :param to_email: reciever's email
        :param subject: subject of the email being sent
        :param body_text: text used as a main message in the body of the DailySpeakUp mailing template
    """
    
    sender = ResendEmailSender()

    sender.send_email(
        to_email=to_mail,
        subject=subject,
        body_text=body_text
    )