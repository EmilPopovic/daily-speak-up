from ...api.config import get_settings
import resend

class ResendEmailSender:
    def __init__(self):
        self._settings = get_settings()
        self.api_key = self._settings.RESEND_API_KEY
        self.from_email = self._settings.RESEND_FROM_EMAIL

    def send_email(self, to_email: str, subject: str, body: str) -> None:
        resend.api_key = self.api_key

        params: resend.Emails.SendParams = {
            "from" : self.from_email,
            "to" : [to_email],
            "subject" : subject,
            "html" : "<strong> test </strong>"
        }

        email = resend.Emails.send(params)
