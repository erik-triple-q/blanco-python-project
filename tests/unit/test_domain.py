# tests/unit/test_domain.py
"""Unit tests for Item domain entity rules and lifecycle transitions."""

import pytest
from pydantic import ValidationError

from app.domain.exceptions import DomainValidationError
from app.domain.models import Item, ItemStatus


def test_item_initialization_with_valid_attributes_creates_draft_item() -> None:
    # Arrange & Act
    item = Item(title="Write documentation", description="Document Clean Architecture")

    # Assert
    assert item.status == ItemStatus.DRAFT


def test_item_activation_from_draft_sets_active_status(sample_item: Item) -> None:
    # Arrange & Act
    activated = sample_item.activate()

    # Assert
    assert activated.status == ItemStatus.ACTIVE


def test_item_activation_when_already_active_raises_domain_validation_error(
    sample_item: Item,
) -> None:
    # Arrange
    active_item = sample_item.activate()

    # Act & Assert
    with pytest.raises(DomainValidationError):
        active_item.activate()


def test_item_completion_from_active_sets_completed_status(sample_item: Item) -> None:
    # Arrange
    active_item = sample_item.activate()

    # Act
    completed = active_item.complete()

    # Assert
    assert completed.status == ItemStatus.COMPLETED


def test_item_completion_when_archived_raises_domain_validation_error(
    sample_item: Item,
) -> None:
    # Arrange
    archived_item = sample_item.archive()

    # Act & Assert
    with pytest.raises(DomainValidationError):
        archived_item.complete()


def test_item_archive_from_any_status_sets_archived_status(sample_item: Item) -> None:
    # Arrange & Act
    archived = sample_item.archive()

    # Assert
    assert archived.status == ItemStatus.ARCHIVED


def test_item_creation_with_empty_title_raises_validation_error() -> None:
    # Arrange & Act & Assert
    with pytest.raises(ValidationError):
        Item(title="")
