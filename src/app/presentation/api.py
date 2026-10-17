# src/app/presentation/api.py
"""FastAPI presentation layer providing thin HTTP endpoints and DTO schemas."""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from datetime import datetime
from typing import Annotated

from fastapi import Depends, FastAPI, Query, Request, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy.orm import Session

from app.application.services import ItemService
from app.domain.exceptions import DomainValidationError, EntityNotFoundError
from app.domain.models import Item, ItemStatus
from app.infrastructure.config import get_settings
from app.infrastructure.database import Base, engine, get_db_session
from app.infrastructure.repositories import SqlAlchemyItemRepository

settings = get_settings()


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[None, None]:
    """Auto-initialize database tables on application startup."""
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)


# --- Request and Response DTOs ---


class CreateItemRequest(BaseModel):
    """Payload schema for creating a new item."""

    model_config = ConfigDict(strict=True)

    title: str = Field(min_length=1, max_length=200)
    description: str = Field(default="", max_length=2000)


class ItemResponse(BaseModel):
    """Public JSON representation of an Item."""

    model_config = ConfigDict(strict=True, from_attributes=True)

    id: str
    title: str
    description: str
    status: ItemStatus
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_domain(cls, item: Item) -> "ItemResponse":
        """Map pure domain Item to response DTO."""
        return cls(
            id=item.id,
            title=item.title,
            description=item.description,
            status=item.status,
            created_at=item.created_at,
            updated_at=item.updated_at,
        )


class HealthResponse(BaseModel):
    """Health check response schema."""

    model_config = ConfigDict(strict=True)

    status: str
    app: str
    environment: str


# --- Exception Handlers ---


@app.exception_handler(EntityNotFoundError)
def handle_entity_not_found(_request: Request, exc: EntityNotFoundError) -> JSONResponse:
    """Map domain EntityNotFoundError to HTTP 404."""
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": str(exc)},
    )


@app.exception_handler(DomainValidationError)
def handle_domain_validation(_request: Request, exc: DomainValidationError) -> JSONResponse:
    """Map domain DomainValidationError to HTTP 422."""
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": str(exc)},
    )


# --- Dependency Injection ---


def get_item_service(
    session: Annotated[Session, Depends(get_db_session)],
) -> ItemService:
    """Factory dependency providing ItemService with injected repository."""
    repository = SqlAlchemyItemRepository(session)
    return ItemService(repository)


# --- HTTP Endpoints ---


@app.get("/health", response_model=HealthResponse, tags=["System"])
def health_check() -> HealthResponse:
    """Return application health and environment status."""
    return HealthResponse(
        status="healthy",
        app=settings.app_name,
        environment=settings.app_env,
    )


@app.post(
    "/api/v1/items",
    response_model=ItemResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Items"],
)
def create_item(
    payload: CreateItemRequest,
    service: Annotated[ItemService, Depends(get_item_service)],
) -> ItemResponse:
    """Create a new item in draft status."""
    item = service.create_item(title=payload.title, description=payload.description)
    return ItemResponse.from_domain(item)


@app.get("/api/v1/items", response_model=list[ItemResponse], tags=["Items"])
def list_items(
    service: Annotated[ItemService, Depends(get_item_service)],
    item_status: Annotated[ItemStatus | None, Query(alias="status")] = None,
    limit: Annotated[int, Query(ge=1, le=100)] = 50,
    offset: Annotated[int, Query(ge=0)] = 0,
) -> list[ItemResponse]:
    """Retrieve items with optional status filtering."""
    items = service.list_items(status=item_status, limit=limit, offset=offset)
    return [ItemResponse.from_domain(item) for item in items]


@app.get("/api/v1/items/{item_id}", response_model=ItemResponse, tags=["Items"])
def get_item(
    item_id: str,
    service: Annotated[ItemService, Depends(get_item_service)],
) -> ItemResponse:
    """Retrieve single item by id."""
    item = service.get_item(item_id)
    return ItemResponse.from_domain(item)


@app.post("/api/v1/items/{item_id}/activate", response_model=ItemResponse, tags=["Items"])
def activate_item(
    item_id: str,
    service: Annotated[ItemService, Depends(get_item_service)],
) -> ItemResponse:
    """Transition item to active status."""
    item = service.activate_item(item_id)
    return ItemResponse.from_domain(item)


@app.post("/api/v1/items/{item_id}/complete", response_model=ItemResponse, tags=["Items"])
def complete_item(
    item_id: str,
    service: Annotated[ItemService, Depends(get_item_service)],
) -> ItemResponse:
    """Transition item to completed status."""
    item = service.complete_item(item_id)
    return ItemResponse.from_domain(item)


@app.post("/api/v1/items/{item_id}/archive", response_model=ItemResponse, tags=["Items"])
def archive_item(
    item_id: str,
    service: Annotated[ItemService, Depends(get_item_service)],
) -> ItemResponse:
    """Transition item to archived status."""
    item = service.archive_item(item_id)
    return ItemResponse.from_domain(item)


@app.delete(
    "/api/v1/items/{item_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Items"],
)
def delete_item(
    item_id: str,
    service: Annotated[ItemService, Depends(get_item_service)],
) -> None:
    """Delete an item by id."""
    service.delete_item(item_id)
