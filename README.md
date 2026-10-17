<!-- README.md -->
# Clean Python Project Template

A production-ready Python 3.12+ skeleton built following **Clean Architecture**, **Domain-Driven Design (DDD)**, **SOLID** principles, and the minimalist **Ponytail (KISS/YAGNI)** philosophy.

---

## ⚡ Core Technologies & Tooling

- **Language**: Python 3.12+ with strict type annotations (PEP 585 & PEP 604).
- **Package & Dependency Manager**: [uv](https://docs.astral.sh/uv/) for blazing-fast, deterministic environments.
- **Code Quality & Formatting**: [Ruff](https://docs.astral.sh/ruff/) (linter & code formatter) and [pre-commit](https://pre-commit.com/).
- **Web API Framework**: [FastAPI](https://fastapi.tiangolo.com/) with thin controllers and Pydantic v2 DTO schemas.
- **Database & Migrations**: [SQLAlchemy 2.0](https://www.sqlalchemy.org/) ORM and [Alembic](https://alembic.sqlalchemy.org/) schema evolution.
- **Testing**: [pytest](https://docs.pytest.org/) with 100% deterministic, ultra-fast in-memory unit and integration tests.
- **Agent Governance**: Universal instruction set in [AGENTS.md](AGENTS.md) and [.gemini/GEMINI.md](.gemini/GEMINI.md).

---

## 🏛️ Architecture & Project Structure

```text
├── AGENTS.md                  # Universal agent rules & standards
├── Makefile                   # Make developer & deployment workflow
├── pyproject.toml             # Project configuration & dependencies
├── alembic/                   # Database migration scripts
├── docs/                      # Structured project documentation
│   ├── README.md              # Documentation index & dashboard
│   ├── ACTION_LIST.md         # Lean action list & incident protocol (< 50 lines)
│   ├── CHANGELOG.md           # Keep a Changelog version history
│   ├── design/                # Architecture specifications and design tokens
│   ├── deployment/            # Docker, runtime, and deployment documentation
│   └── roadmap/               # Strategic goals and milestones
├── src/
│   └── app/
│       ├── domain/            # 100% pure domain: entities, value objects, exceptions
│       ├── application/       # Use cases, application services, and ports (Protocols)
│       ├── infrastructure/    # Database adapters, SQLAlchemy models, config
│       └── presentation/      # Thin FastAPI controllers, request/response DTOs
└── tests/
    ├── conftest.py            # Shared in-memory SQLite & client fixtures
    ├── unit/                  # Isolated domain and use case tests
    └── integration/           # Repository and HTTP endpoint tests
```

---

## 🚀 Quickstart

```bash
# 1. Install dependencies and git pre-commit hooks
make install

# 2. Run quality checks and test suite
make check

# 3. Start local development server
make run
```

See [AGENTS.md](AGENTS.md) for full engineering guidelines and tooling workflows.
