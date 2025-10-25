from __future__ import annotations
from typing import Optional, TYPE_CHECKING
from sqlalchemy import DateTime, ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
import datetime
import uuid

from ..db import Base

if TYPE_CHECKING:
    from .user import User
    from .interest import Interest

class UserInterest(Base):
    __tablename__ = 'user_interests'
    __table_args__ = (
        Index(
            'idx_user_interests_user_id',
            'user_id',
        ),
        Index(
            'idx_user_interests_interest_id',
            'interest_id',
        ),
        Index(
            'idx_user_interests_user_interest',
            'user_id',
            'interest_id',
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
        nullable=False
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey('users.id'),
        nullable=False,
    )
    removed_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    # Relationships
    user: Mapped[User] = relationship(
        'User',
        back_populates='user_interests',
    )
    interest: Mapped[Interest] = relationship(
        'Interest',
        back_populates='user_interests',
    )
