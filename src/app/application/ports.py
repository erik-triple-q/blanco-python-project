# src/app/application/ports.py
"""Narrow protocol interfaces (ports) for infrastructure adapters."""

from typing import Protocol

from app.domain.models import Item, ItemStatus


class ItemRepositoryProtocol(Protocol):
    """Repository port for persisting and retrieving Item domain entities."""

    def save(self, item: Item) -> Item:
        """Persist or update an item aggregate."""
        ...

    def get_by_id(self, item_id: str) -> Item | None:
        """Retrieve an item by its unique identifier."""
        ...

    def list_all(
        self,
        *,
        status: ItemStatus | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> list[Item]:
        """List items with optional filtering and pagination."""
        ...

    def delete(self, item_id: str) -> bool:
        """Delete an item by its unique identifier."""
        ...
