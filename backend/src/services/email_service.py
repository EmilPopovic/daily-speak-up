from .email_impl.celery_tasks import send_email_task

class EmailService:
    """
        Class that provides a high-level abstraction for sending emails using Resend API.
    """
    
    @staticmethod
    def send_email(to_mail: str, subject: str, message: str = 'Welcome to DailySpeakUp!') -> None:
        """
            Send an email using Resend API.

            This method takes the recipient's email address and the subject of the email as parameters.
            It retursns nothing.
            
            :param to_mail: Recipient's email address.
            :param subject: Subject of the email.
        """
        # enqueue email sending task to Celery worker
        send_email_task.delay(to_mail, subject, body_text=message)