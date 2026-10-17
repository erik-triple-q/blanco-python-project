# src/app/infrastructure/repositories.py
"""SQLAlchemy repository implementations."""

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.application.ports import ItemRepositoryProtocol
from app.domain.models import Item, ItemStatus
from app.infrastructure.models import ItemModel


class SqlAlchemyItemRepository(ItemRepositoryProtocol):
    """SQLAlchemy adapter implementing the ItemRepositoryProtocol."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, item: Item) -> Item:
        """Persist or update an item aggregate in the database."""
        model = self._session.get(ItemModel, item.id)
        if model is None:
            model = ItemModel.from_domain(item)
            self._session.add(model)
        else:
            model.title = item.title
            model.description = item.description
            model.status = item.status
            model.updated_at = item.updated_at

        self._session.flush()
        return model.to_domain()

    def get_by_id(self, item_id: str) -> Item | None:
        """Retrieve an item by its unique identifier."""
        model = self._session.get(ItemModel, item_id)
        if model is None:
            return None
        return model.to_domain()

    def list_all(
        self,
        *,
        status: ItemStatus | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> list[Item]:
        """List items with optional status filtering and pagination."""
        stmt = select(ItemModel)
        if status is not None:
            stmt = stmt.where(ItemModel.status == status)
        stmt = stmt.order_by(ItemModel.created_at.desc()).offset(offset).limit(limit)

        records = self._session.scalars(stmt).all()
        return [record.to_domain() for record in records]

    def delete(self, item_id: str) -> bool:
        """Delete an item by its unique identifier."""
        model = self._session.get(ItemModel, item_id)
        if model is None:
            return False
        self._session.delete(model)
        self._session.flush()
        return True
