<!-- .agents/rules/clean-architecture.md -->
# Clean Architecture & DDD Rules

Dependencies strictly point inward:
`Presentation -> Infrastructure -> Application -> Domain`

## 1. Domain (`src/app/domain/`)
- Pure Python: ZERO imports of frameworks (FastAPI), databases (SQLAlchemy, SQL), network, or disk I/O.
- Rich domain models: Validations and state transitions (e.g. `activate()`) belong in entities/aggregates, never anemic.
- Custom domain exceptions must inherit from `DomainError`.

## 2. Application (`src/app/application/`)
- Orchestrates use cases and business workflows.
- Ports: Define lean contracts via `typing.Protocol` (1–3 methods following ISP).
- Services remain framework- and database-agnostic, receiving abstractions via constructor injection.

## 3. Infrastructure (`src/app/infrastructure/`)
- Concrete adapters for databases, external APIs, and configuration.
- SQLAlchemy ORM models explicitly map to and from pure domain entities via `to_domain()` and `from_domain()`.

## 4. Presentation (`src/app/presentation/`)
- Thin Handlers: Handlers act purely as recipes (input parsing via Pydantic DTOs, service invocation, response formatting).
- Never place business or domain logic in controllers or route functions.
