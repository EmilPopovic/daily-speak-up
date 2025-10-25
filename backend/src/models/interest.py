from __future__ import annotations
from typing import List, TYPE_CHECKING
from sqlalchemy import DateTime, Text, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
import datetime
import uuid

from ..db import Base

if TYPE_CHECKING:
    from .user_interest import UserInterest
    from .speech import Speech

class Interest(Base):
    __tablename__ = 'interests'
    __table_args__ = (
        Index(
            'idx_interests_slug',
            'slug',
            unique=True,
        ),
        Index(
            'idx_interests_name',
            'name',
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
        nullable=False,
    )
    slug: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        unique=True,
    )
    name: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        unique=True,
    )

    # Relationships
    user_interests: Mapped[List[UserInterest]] = relationship(
        'UserInterest',
        back_populates='interest',
    )
    speeches: Mapped[List[Speech]] = relationship(
        'Speech',
        back_populates='interest',
    )
