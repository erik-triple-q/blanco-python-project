# src/app/domain/exceptions.py
"""Domain-specific exceptions."""


class DomainError(Exception):
    """Base exception for all domain errors."""


class EntityNotFoundError(DomainError):
    """Raised when a requested domain entity cannot be found."""

    def __init__(self, entity_name: str, identifier: str | int) -> None:
        self.entity_name = entity_name
        self.identifier = identifier
        super().__init__(f"{entity_name} with identifier '{identifier}' was not found.")


class EntityAlreadyExistsError(DomainError):
    """Raised when creating an entity that violates uniqueness constraints."""

    def __init__(self, entity_name: str, identifier: str | int) -> None:
        self.entity_name = entity_name
        self.identifier = identifier
        super().__init__(f"{entity_name} with identifier '{identifier}' already exists.")


class DomainValidationError(DomainError):
    """Raised when an operation violates domain invariants."""
