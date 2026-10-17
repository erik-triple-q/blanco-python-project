<!-- docs/CHANGELOG.md -->
# Changelog

All notable changes to this project are documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [0.1.0] — 2026-10-17

### [Feature]
- Initial release of the production-ready Python starter skeleton.
- Clean Architecture structure with strict layer separation (`domain/`, `application/`, `infrastructure/`, `presentation/`).
- SQLAlchemy 2.0 ORM integration combined with Alembic database migrations.
- FastAPI REST presentation layer with thin handlers, DTO validation, and custom exception handlers.
- Make workflow (`make install`, `make check`, `make format`, `make commit`, `make ship`).
- Pytest test suite with 100% deterministic unit and integration tests.
- Universal `AGENTS.md` and `.gemini/GEMINI.md` rules for AI coding assistants.
