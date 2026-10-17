<!-- docs/design/architecture.md -->
# Clean Architecture & DDD Design

This document describes the application architecture and separation of concerns.

---

## 1. The Dependency Rule (Dependencies Point Inward)

The architecture strictly adheres to Clean Architecture and Domain-Driven Design (DDD). Inner layers have no knowledge of outer layers.

```
       [ Presentation (FastAPI Handlers, CLI) ]
                          │
                          ▼
       [ Infrastructure (SQLAlchemy, DB Adapters) ]
                          │
                          ▼
       [ Application (Services, Ports/Protocols) ]
                          │
                          ▼
       [ Domain (Entities, Value Objects, Domain Errors) ]
```

---

## 2. Layer Specification

### 1. Domain (`src/app/domain/`)
- **Purpose**: Encapsulates enterprise business entities, value objects, and domain exceptions.
- **Rule**: Pure Python. Zero imports of frameworks (FastAPI), databases (SQLAlchemy, SQL), network, or disk I/O.
- **Rich Domain Models**: Business validations and state transitions (e.g. `item.activate()`) are encapsulated within entities to prevent anemic models.

### 2. Application (`src/app/application/`)
- **Purpose**: Orchestrates use cases and defines architectural abstractions.
- **Ports (`ports.py`)**: Defines narrow `typing.Protocol` interfaces for repositories and adapters adhering to the Interface Segregation Principle (ISP).
- **Services (`services.py`)**: Framework-agnostic use cases executing domain rules and persisting data through injected repository protocols.

### 3. Infrastructure (`src/app/infrastructure/`)
- **Purpose**: Concrete implementations of external adapters and abstractions.
- **Database & ORM**: SQLAlchemy 2.0 models (`models.py`), database engines, and session management (`database.py`).
- **Repositories (`repositories.py`)**: Implementation of the `ItemRepositoryProtocol` interface.
- **Configuration (`config.py`)**: Pydantic v2 `BaseSettings` for strongly typed environment configuration.

### 4. Presentation (`src/app/presentation/`)
- **Purpose**: External entry point to the system (REST API, CLI, webhooks).
- **Thin Handlers**: Handlers act purely as recipes: request parsing via Pydantic DTOs, service invocation, and response formatting.
- **Exception Handlers**: Maps domain errors (`EntityNotFoundError`, `DomainValidationError`) to standard HTTP status codes (404, 422).

---

## 3. Dependency Injection
Concrete adapters are wired via constructor injection in the presentation layer (Composition Root), keeping application and domain layers fully isolated and deterministically testable.
