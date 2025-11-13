from __future__ import annotations
from typing import Optional, TYPE_CHECKING
from sqlalchemy import (
    DateTime,
    ForeignKey,
    Index,
    Numeric,
    CheckConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
import datetime
import uuid

from ..db import Base

if TYPE_CHECKING:
    from .speech import Speech
    from .user import User

class Rating(Base):
    __tablename__ = 'ratings'
    __table_args__ = (
        Index(
            'idx_ratings_rated_by_speech_id_removed_at_unique',
            'rated_by',
            'speech_id',
            'removed_at',
            unique=True,
        ),
        Index(
            'idx_ratings_speech_id',
            'speech_id',
        ),
        CheckConstraint(
            'score >= 0 AND score <= 5',
            name='check_rating_score_range',
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
    speech_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey('speeches.id'),
        nullable=False,
    )
    rated_by: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey('users.id'),
        nullable=False,
    )
    score: Mapped[float] = mapped_column(
        Numeric(5, 2),
        nullable=False,
    )
    removed_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    # Relationship
    speech: Mapped[Speech] = relationship(
        'Speech',
        back_populates='ratings',
    )
    rater: Mapped[User] = relationship(
        'User',
        back_populates='ratings',
    )
