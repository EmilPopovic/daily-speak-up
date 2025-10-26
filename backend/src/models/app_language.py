from __future__ import annotations
from typing import TYPE_CHECKING, List
from sqlalchemy import DateTime, Text, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
import datetime
import uuid

from ..db import Base

if TYPE_CHECKING:
    from .user import User

class AppLanguage(Base):
    __tablename__ = 'app_languages'
    __table_args__ = (
        Index(
            'idx_app_languages_slug',
            'slug',
            unique=True,
        ),
        Index(
            'idx_app_languages_display_name',
            'display_name',
            unique=True,
        )
    )

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.datetime.now(datetime.timezone.utc),
        nullable=False
    )
    slug: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        unique=True,
    )
    display_name: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        unique=True,
    )

    # Relationships
    users: Mapped[List[User]] = relationship(
        'User',
        back_populates='preferred_language',
    )
