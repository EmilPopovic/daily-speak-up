from .email_impl.celery_tasks import send_email_task
from celery import Task
from typing import Literal

send_email_task: Task
class EmailService:
    """
        Class that provides a high-level abstraction for sending emails using Resend API.
    """
    
    @staticmethod
    def send_email(to_mail: str, subject: str, 
                   message: str = 'Welcome to DailySpeakUp!',
                   template: Literal['basic_message', 'welcome'] = 'welcome') -> None:
        """
            Send an email using Resend API.

            This method takes the recipient's email address and the subject of the email as parameters.
            It retursns nothing.
            
            :param to_mail: Recipient's email address.
            :param subject: Subject of the email.
            :param message: Message you want to send.
            :param template: Email template to use.
        """
        # enqueue email sending task to Celery worker
        send_email_task.delay(to_mail, subject, body_text=message, template=template)