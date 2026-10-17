# src/app/application/services.py
"""Application services orchestrating use cases and domain logic."""

from app.application.ports import ItemRepositoryProtocol
from app.domain.exceptions import EntityNotFoundError
from app.domain.models import Item, ItemStatus


class ItemService:
    """Use case orchestrator for Item aggregates."""

    def __init__(self, repository: ItemRepositoryProtocol) -> None:
        self._repository = repository

    def create_item(self, title: str, description: str = "") -> Item:
        """Create and persist a new draft item."""
        item = Item(title=title, description=description)
        return self._repository.save(item)

    def get_item(self, item_id: str) -> Item:
        """Retrieve an item or raise EntityNotFoundError."""
        item = self._repository.get_by_id(item_id)
        if item is None:
            raise EntityNotFoundError("Item", item_id)
        return item

    def list_items(
        self,
        *,
        status: ItemStatus | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> list[Item]:
        """List items with optional status filtering."""
        return self._repository.list_all(status=status, limit=limit, offset=offset)

    def activate_item(self, item_id: str) -> Item:
        """Execute state transition to active."""
        item = self.get_item(item_id)
        activated = item.activate()
        return self._repository.save(activated)

    def complete_item(self, item_id: str) -> Item:
        """Execute state transition to completed."""
        item = self.get_item(item_id)
        completed = item.complete()
        return self._repository.save(completed)

    def archive_item(self, item_id: str) -> Item:
        """Execute state transition to archived."""
        item = self.get_item(item_id)
        archived = item.archive()
        return self._repository.save(archived)

    def delete_item(self, item_id: str) -> None:
        """Delete an item by id or raise EntityNotFoundError."""
        deleted = self._repository.delete(item_id)
        if not deleted:
            raise EntityNotFoundError("Item", item_id)
