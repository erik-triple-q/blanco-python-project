# tests/integration/test_repository.py
"""Integration tests for SqlAlchemyItemRepository with SQLite database session."""

from sqlalchemy.orm import Session

from app.domain.models import Item, ItemStatus
from app.infrastructure.repositories import SqlAlchemyItemRepository


def test_repository_save_and_get_by_id_persists_item(
    db_session: Session, sample_item: Item
) -> None:
    # Arrange
    repo = SqlAlchemyItemRepository(db_session)

    # Act
    saved = repo.save(sample_item)
    retrieved = repo.get_by_id(saved.id)

    # Assert
    assert retrieved is not None and retrieved.id == sample_item.id


def test_repository_list_all_filters_by_status(db_session: Session) -> None:
    # Arrange
    repo = SqlAlchemyItemRepository(db_session)
    draft_item = Item(title="Draft Task", status=ItemStatus.DRAFT)
    active_item = Item(title="Active Task", status=ItemStatus.ACTIVE)
    repo.save(draft_item)
    repo.save(active_item)

    # Act
    active_list = repo.list_all(status=ItemStatus.ACTIVE)

    # Assert
    assert len(active_list) == 1 and active_list[0].id == active_item.id


def test_repository_delete_removes_item_from_database(
    db_session: Session, sample_item: Item
) -> None:
    # Arrange
    repo = SqlAlchemyItemRepository(db_session)
    repo.save(sample_item)

    # Act
    was_deleted = repo.delete(sample_item.id)

    # Assert
    assert was_deleted and repo.get_by_id(sample_item.id) is None
