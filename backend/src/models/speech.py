from __future__ import annotations
from typing import Optional, List, TYPE_CHECKING
from sqlalchemy import (
    DateTime,
    Text,
    ForeignKey,
    Index,
    Boolean,
    Enum as SQLEnum,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
import datetime
import uuid

from ..db import Base
from .enums import SpeechVisibility

if TYPE_CHECKING:
    from .user import User
    from .interest import Interest
    from .report import Report
    from .rating import Rating

class Speech(Base):
    __tablename__ = 'speeches'
    __table_args__ = (
        Index(
            'idx_speeches_user_id_created_at_is_cancelled',
            'user_id',
            'created_at',
            'is_cancelled',
        ),
        Index(
            'idx_speeches_user_id',
            'user_id',
        ),
        Index(
            'idx_speeches_interest_id',
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
        nullable=False,
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey('users.id'),
        nullable=False,
    )
    caption: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )
    s3_url: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )
    is_cancelled: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )
    visibility_level: Mapped[SpeechVisibility] = mapped_column(
        SQLEnum(SpeechVisibility, name='speech_visibility', create_type=True),
        default=SpeechVisibility.PRIVATE,
        nullable=False,
    )
    interest_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey('interests.id'),
        nullable=True,
    )
    task: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )
    deleted_by: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey('users.id'),
        nullable=True,
    )

    # Relationships
    user: Mapped[User] = relationship(
        'User',
        foreign_keys=[user_id],
        back_populates='speeches',
    )
    deleter: Mapped[Optional[User]] = relationship(
        'User',
        foreign_keys=[deleted_by],
        back_populates='deleted_speeches',
    )
    interest: Mapped[Optional[Interest]] = relationship(
        'Interest',
        back_populates='speeches',
    )
    reports: Mapped[List[Report]] = relationship(
        'Report',
        back_populates='speech',
    )
    ratings: Mapped[List[Rating]] = relationship(
        'Rating',
        back_populates='speech',
    )
