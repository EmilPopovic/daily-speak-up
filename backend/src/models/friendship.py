from __future__ import annotations
from typing import Optional, TYPE_CHECKING
from sqlalchemy import (
    DateTime,
    ForeignKey,
    Index,
    CheckConstraint,
    Enum as SQLEnum
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
import datetime
import uuid

from ..db import Base
from .enums import RequestStatus

if TYPE_CHECKING:
    from .user import User

class Friendship(Base):
    __tablename__ = 'friendships'
    __table_args__ = (
        Index(
            'idx_friendships_user_id1_user_id2_unique',
            'user_id1',
            'user_id2',
            unique=True,
        ),
        Index(
            'idx_friendships_user_id1',
            'user_id1',
        ),
        Index(
            'idx_friendships_user_id2',
            'user_id2',
        ),
        CheckConstraint(
            'user_id1 != user_id2',
            name='check_friendship_different_users',
        ),
        CheckConstraint(
            'user_id1 < user_id2',
            name='check_friencship_ordered_ids',
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

    user_id1: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey('users.id'),
        nullable=False,
    )
    user_id2: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey('users.id'),
        nullable=False,
    )

    requested_by_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey('users.id'),
        nullable=False,
    )

    status: Mapped[RequestStatus] = mapped_column(
        SQLEnum(RequestStatus, name='request_status', create_type=True),
        default=RequestStatus.PENDING,
        nullable=False,
    )
    answered_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
    deleted_by: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey('users.id'),
        nullable=True,
    )
