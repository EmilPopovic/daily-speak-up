from __future__ import annotations
from typing import TYPE_CHECKING
from sqlalchemy import DateTime, Text, ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
import datetime
import uuid

from ..db import Base

if TYPE_CHECKING:
    from .user import User

class UserDevice(Base):
    __tablename__ = 'user_devices'
    __table_args__ = (
        Index(
            'idx_user_devices_fcm_token',
            'fcm_token',
            unique=True
        ),
        Index(
            'idx_user_devices_user_id',
            'user_id',
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
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey('users.id'),
        nullable=False,
    )
    fcm_token: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        unique=True,
    )
    last_used_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.datetime.now(datetime.timezone.utc),
        nullable=False,
    )

    # Relationships
    user: Mapped[User] = relationship(
        'User',
        back_populates='devices',
    )
