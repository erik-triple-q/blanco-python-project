# src/app/domain/models.py
"""Domain entities and value objects."""

from datetime import UTC, datetime
from enum import StrEnum
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field

from app.domain.exceptions import DomainValidationError


class ItemStatus(StrEnum):
    """Lifecycle status of an item."""

    DRAFT = "draft"
    ACTIVE = "active"
    COMPLETED = "completed"
    ARCHIVED = "archived"


class Item(BaseModel):
    """Core domain aggregate representing a trackable work or business item."""

    model_config = ConfigDict(strict=True, frozen=True)

    id: str = Field(default_factory=lambda: str(uuid4()))
    title: str = Field(min_length=1, max_length=200)
    description: str = Field(default="", max_length=2000)
    status: ItemStatus = Field(default=ItemStatus.DRAFT)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    def activate(self) -> "Item":
        """Transition item from draft to active."""
        if self.status != ItemStatus.DRAFT:
            raise DomainValidationError(
                f"Cannot activate item in status '{self.status}'. "
                "Only draft items can be activated."
            )
        return self.model_copy(
            update={"status": ItemStatus.ACTIVE, "updated_at": datetime.now(UTC)}
        )

    def complete(self) -> "Item":
        """Transition item to completed."""
        if self.status not in (ItemStatus.ACTIVE, ItemStatus.DRAFT):
            raise DomainValidationError(
                f"Cannot complete item in status '{self.status}'. Item must be active or draft."
            )
        return self.model_copy(
            update={"status": ItemStatus.COMPLETED, "updated_at": datetime.now(UTC)}
        )

    def archive(self) -> "Item":
        """Archive the item regardless of its current lifecycle state."""
        return self.model_copy(
            update={"status": ItemStatus.ARCHIVED, "updated_at": datetime.now(UTC)}
        )
