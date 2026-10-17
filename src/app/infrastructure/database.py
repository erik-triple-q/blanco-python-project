# src/app/infrastructure/database.py
"""SQLAlchemy database engine and session configuration."""

from collections.abc import Generator
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.infrastructure.config import get_settings


class Base(DeclarativeBase):
    """Declarative base class for all SQLAlchemy ORM models."""


def _ensure_sqlite_directory(database_url: str) -> None:
    """Ensure parent directory exists for SQLite database paths."""
    if database_url.startswith("sqlite:///") and not database_url.startswith("sqlite:///:memory:"):
        path_str = database_url.removeprefix("sqlite:///")
        db_path = Path(path_str).resolve()
        db_path.parent.mkdir(parents=True, exist_ok=True)


settings = get_settings()
_ensure_sqlite_directory(settings.database_url)

connect_args = {"check_same_thread": False} if settings.database_url.startswith("sqlite") else {}

engine = create_engine(
    settings.database_url,
    connect_args=connect_args,
    echo=(settings.app_env == "development" and settings.log_level == "DEBUG"),
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db_session() -> Generator[Session, None, None]:
    """Dependency generator that yields an isolated database session."""
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
