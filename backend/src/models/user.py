from __future__ import annotations
from typing import Optional, List, TYPE_CHECKING
from sqlalchemy import (
    Boolean,
    DateTime,
    Text,
    ForeignKey,
    Index,
    Numeric,
    Enum as SQLEnum,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
import datetime
import uuid

from ..db import Base
from .enums import UserRole, OnboardingStatus, AppTheme

if TYPE_CHECKING:
    from .app_language import AppLanguage
    from .user_device import UserDevice
    from .friendship import Friendship
    from .user_streak import UserStreak
    from .user_interest import UserInterest
    from .speech import Speech
    from .report import Report
    from .rating import Rating
    from .ban import Ban

class User(Base):
    __tablename__ = 'users'
    __table_args__ = (
        Index(
            'idx_users_auth0_user_id',
            'auth0_user_id',
            unique=True,
        ),
        Index(
            'idx_users_email',
            'email',
            unique=True,
        ),
        Index(
            'idx_users_handle',
            'handle',
            unique=True,
        ),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.datetime.now(datetime.timezone.utc),
        nullable=False,
    )

    role: Mapped[UserRole] = mapped_column(
        SQLEnum(UserRole, name='user_role', create_type=True),
        nullable=False,
    )

    auth0_user_id: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        unique=True,
    )
    email_changed_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    handle: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        unique=True,
    )
    handle_changed_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    profile_picture_url: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )
    profile_picture_changed_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    onboarding_status: Mapped[OnboardingStatus] = mapped_column(
        SQLEnum(OnboardingStatus, name='onboarding_status', create_type=True),
        default=OnboardingStatus.PENDING,
        nullable=False,
    )

    preferred_lang: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey('app_languages.id'),
        nullable=False,
    )
    preferred_theme: Mapped[AppTheme] = mapped_column(
        SQLEnum(AppTheme, name='app_theme', create_type=True),
        default=AppTheme.SYSTEM,
        nullable=False,
    )
    preferred_tz_offset: Mapped[float] = mapped_column(
        Numeric(3, 1),
        default=0.0,
        nullable=False,
    )

    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
    anonymized_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    email_notifications_enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )
    push_notifications_enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )
    streak_reminders_enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )
