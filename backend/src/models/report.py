from __future__ import annotations
from typing import Optional, List, TYPE_CHECKING
from sqlalchemy import (
    DateTime,
    Text,
    ForeignKey,
    Index,
    Enum as SQLEnum,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
import datetime
import uuid

from ..db import Base
from .enums import ResolutionAction

if TYPE_CHECKING:
    from .speech import Speech
    from .user import User
    from .ban import Ban

class Report(Base):
    __tablename__ = 'reports'
    __table_args__ = (
        Index(
            'idx_reports_speech_id',
            'speech_id',
        ),
        Index(
            'idx_reports_reported_by',
            'reported_by',
        ),
        Index(
            'idx_reports_resolution_action',
            'resolution_action',
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

    reported_by: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey('users.id'),
        nullable=False,
    )
    reason: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )

    resolved_by: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey('users.id'),
        nullable=True,
    )
    resolution_action: Mapped[ResolutionAction] = mapped_column(
        SQLEnum(ResolutionAction, name='resolution_action', create_type=True),
        default=ResolutionAction.PENDING,
        nullable=False,
    )

    # Relationships
    speech: Mapped[Speech] = relationship(
        'Speech',
        back_populates='reports',
    )
    repoter: Mapped[User] = relationship(
        'User',
        foreign_keys=[reported_by],
        back_populates='reports',
    )
    resolver: Mapped[Optional[User]] = relationship(
        'User',
        foreign_keys=[resolved_by],
        back_populates='resolved_reports',
    )
    bans: Mapped[List[Ban]] = relationship(
        'Ban',
        back_populates='report',
    )
