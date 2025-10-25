from enum import Enum

class AppTheme(str, Enum):
    """Application theme options."""
    SYSTEM = 'system'
    LIGHT = 'light'
    DARK = 'dark'

class UserRole(str, Enum):
    """User role options"""
    USER = 'user'
    MOD = 'mod'
    ADMIN = 'admin'

class OnboardingStatus(str, Enum):
    """Onboarding status options."""
    PENDING = 'pending'
    PROFILE_CUSTOMIZATION = 'profile_customization'
    INTERESTS_SELECTION = 'interests_selection'
    COMPLETED = 'completed'

class RequestStatus(str, Enum):
    """Friendship request status options."""
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    DENIED = 'denied'
    DELETED = 'deleted'

class SpeechVisibility(str, Enum):
    """Speech visibility options."""
    PRIVATE = 'private'
    FRIENDS = 'friends'

class ResolutionAction(str, Enum):
    """Report resolution action options."""
    PENDING = 'pending'
    IGNORED = 'ignored'
    VIDEO_DELETED = 'video_deleted'
    USER_BANNED = 'user_banned'
