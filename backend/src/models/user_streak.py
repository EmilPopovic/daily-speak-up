from __future__ import annotations
from typing import Optional, TYPE_CHECKING
from sqlalchemy import DateTime, Date, ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
import datetime
import uuid

from ..db import Base

if TYPE_CHECKING:
    from .user import User

class UserStreak(Base):
    __tablename__ = 'user_streaks'
    __table_args__ = (
        Index(
            'idx_user_streaks_user_id',
            'user_id',
        ),
        Index(
            'idx_user_streaks_user_id_end_date',
            'user_id',
            'end_date',
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

    start_date: Mapped[datetime.date] = mapped_column(
        Date,
        default=datetime.date.today,
        nullable=False,
    )
    end_date: Mapped[Optional[datetime.date]] = mapped_column(
        Date,
        nullable=True,
    )

    ends_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )
    last_warned_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )
