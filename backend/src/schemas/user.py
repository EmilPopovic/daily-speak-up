from typing import Optional
from pydantic import BaseModel

from ..models.enums import (
    AppLang,
    AppTheme,
    OnboardingStatus,
    UserRole
)

class UserCreate(BaseModel):
    auth0_id: str
    email: str
    name: str | None = None
    email_verified: bool = False

class UserResponse(BaseModel):
    role: UserRole
    email: str
    handle: str
    profile_picture_url: Optional[str]
    onboarding_status: OnboardingStatus
    preferred_lang: AppLang
    preferred_theme: AppTheme
    preferred_tz_offset: float
    email_notifications_enabled: bool
    push_notifications_enabled: bool
    streak_reminders_enabled: bool
