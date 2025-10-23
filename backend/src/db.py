import os
from typing import TYPE_CHECKING
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

if TYPE_CHECKING:
    from sqlalchemy.orm import DeclarativeBase as BaseType
else:
    BaseType = object

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL', '')

engine = create_engine(
    DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    pool_timeout=30,
    pool_recycle=3600,
    pool_pre_ping=True,
    echo=False,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base: type[BaseType] = declarative_base()

def get_db():
    """FastAPI dependency for database sessions"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
