from ...api.config import get_settings
from .email_template import basic_html_message, place_holder
import resend

class ResendEmailSender:
    """
        This class is an implementation of a e-mail sender based on Resend API. 
    """
    def __init__(self):
        self._settings = get_settings()
        self.api_key = self._settings.RESEND_API_KEY
        self.from_email = self._settings.RESEND_FROM_EMAIL

    def send_email(self, to_email: str, subject: str, body_text: str) -> None:
        """
            Method for sending an e-mail using Resend API and basic DailySpeakUp mailig template.
            
            :param to_email: reciever's email
            :param subject: subject of the email being sent
            :param body_text: text used as a main message in the body of the DailySpeakUp mailing template
        """
        resend.api_key = self.api_key

        html = basic_html_message().replace(place_holder(), body_text)


        params: resend.Emails.SendParams = {
            "from" : self.from_email,
            "to" : [to_email],
            "subject" : subject,
            "html" : html
        }

        email = resend.Emails.send(params)