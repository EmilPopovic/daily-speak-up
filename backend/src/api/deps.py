from ..services import (
    AuthService,
    EmailService,
    GeminiService,
    S3Service,
)
from .config import get_settings

_auth_service: AuthService | None = None
_email_service: EmailService | None = None
_gemini_service: GeminiService | None = None
_s3_service: S3Service | None = None

def get_auth_service() -> AuthService:
    """Returns a preconfigured AuthService object"""
    global _auth_service
    if _auth_service is None:
        _auth_service = AuthService()
    return _auth_service

def get_email_service() -> EmailService:
    """Returns a preconfigured EmailService object"""
    global _email_service
    if _email_service is None:
        _email_service = EmailService()
    return _email_service

def get_gemini_service() -> GeminiService:
    """Returns a preconfigured GeminiService object"""
    global _gemini_service
    if _gemini_service is None:
        settings = get_settings()
        _gemini_service = GeminiService(
            api_key=settings.gemini_api_key,
            model_id=settings.gemini_model_id
        )
    return _gemini_service

def get_s3_service() -> S3Service:
    """Returns a preconfigured S3Service object"""
    global _s3_service
    if _s3_service is None:
        _s3_service = S3Service()
    return _s3_service
