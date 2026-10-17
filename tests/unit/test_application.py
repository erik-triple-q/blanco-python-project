# tests/unit/test_application.py
"""Unit tests for ItemService application use cases using an in-memory repository fake."""

import pytest

from app.application.ports import ItemRepositoryProtocol
from app.application.services import ItemService
from app.domain.exceptions import EntityNotFoundError
from app.domain.models import Item, ItemStatus


class InMemoryItemRepository(ItemRepositoryProtocol):
    """In-memory test double conforming to ItemRepositoryProtocol."""

    def __init__(self) -> None:
        self._store: dict[str, Item] = {}

    def save(self, item: Item) -> Item:
        self._store[item.id] = item
        return item

    def get_by_id(self, item_id: str) -> Item | None:
        return self._store.get(item_id)

    def list_all(
        self,
        *,
        status: ItemStatus | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> list[Item]:
        items = list(self._store.values())
        if status is not None:
            items = [item for item in items if item.status == status]
        return items[offset : offset + limit]

    def delete(self, item_id: str) -> bool:
        if item_id in self._store:
            del self._store[item_id]
            return True
        return False


def test_create_item_persists_and_returns_draft_item() -> None:
    # Arrange
    repo = InMemoryItemRepository()
    service = ItemService(repo)

    # Act
    item = service.create_item(title="Setup CI", description="Configure GitHub Actions")

    # Assert
    assert item.title == "Setup CI"


def test_get_item_with_existing_id_returns_correct_entity() -> None:
    # Arrange
    repo = InMemoryItemRepository()
    service = ItemService(repo)
    created = service.create_item(title="Existing Item")

    # Act
    retrieved = service.get_item(created.id)

    # Assert
    assert retrieved.id == created.id


def test_get_item_with_unknown_id_raises_entity_not_found_error() -> None:
    # Arrange
    repo = InMemoryItemRepository()
    service = ItemService(repo)

    # Act & Assert
    with pytest.raises(EntityNotFoundError):
        service.get_item("non-existent-id")


def test_activate_item_transitions_item_to_active() -> None:
    # Arrange
    repo = InMemoryItemRepository()
    service = ItemService(repo)
    created = service.create_item(title="Draft to Activate")

    # Act
    activated = service.activate_item(created.id)

    # Assert
    assert activated.status == ItemStatus.ACTIVE


def test_delete_item_with_existing_id_removes_from_repository() -> None:
    # Arrange
    repo = InMemoryItemRepository()
    service = ItemService(repo)
    created = service.create_item(title="Item to Delete")

    # Act
    service.delete_item(created.id)

    # Assert
    assert repo.get_by_id(created.id) is None
