# src/app/infrastructure/models.py
"""SQLAlchemy database models and entity mapping."""

from datetime import UTC, datetime

from sqlalchemy import DateTime, Enum, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.domain.models import Item, ItemStatus
from app.infrastructure.database import Base


class ItemModel(Base):
    """SQLAlchemy table representation for the Item aggregate."""

    __tablename__ = "items"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False, default="")
    status: Mapped[ItemStatus] = mapped_column(
        Enum(ItemStatus, name="item_status_enum", native_enum=False),
        nullable=False,
        default=ItemStatus.DRAFT,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(UTC),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
    )

    def to_domain(self) -> Item:
        """Map ORM model to pure Domain aggregate."""
        return Item(
            id=self.id,
            title=self.title,
            description=self.description,
            status=self.status,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @classmethod
    def from_domain(cls, item: Item) -> "ItemModel":
        """Create ORM model instance from pure Domain aggregate."""
        return cls(
            id=item.id,
            title=item.title,
            description=item.description,
            status=item.status,
            created_at=item.created_at,
            updated_at=item.updated_at,
        )
