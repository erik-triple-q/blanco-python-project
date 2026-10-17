<!-- .gemini/GEMINI.md -->
# Project Index & Quick Reference

Starter skeleton in Python 3.12+ following Clean Architecture and Domain-Driven Design (DDD).
Active runtime profile: **Gemini 3.8 Flash** within Google Antigravity.

---

## ⚡ Definition of Done & Quick Commands

Every task or feature is only complete when `make check` succeeds with zero errors:

```bash
make check       # Mandatory gatekeeper: ruff check + ruff format check + pytest
make format      # Auto-formats code and fixes simple lint errors
make test        # Runs pytest suite (optional: make test ARGS="-k item")
make run         # Starts FastAPI dev server at http://localhost:8000
make health      # Verifies local service health
make migrate     # Applies pending Alembic database migrations
make migration m="description"  # Generates new autodetected migration
make reset-repo  # Emergency recovery: reset to origin branch (preserves .env and data/)
```

---

## 🛡️ Hard Constraints & Hooks (`.agents/hooks.json`)

- **Git Mutations**: Autonomous `git commit` and `git push` are strictly blocked via a `PreToolUse` hook. Commits must be executed manually via `make commit m="..."` or `make ship m="..."`.
- **Auto-Formatting**: A `PostToolUse` hook automatically formats Python files after editing via Ruff.
- **No `make check` on Informational Queries**: Only execute checks when code is actually modified.

---

## 📚 Modular Rules & Documentation Index

Detailed rules are loaded per context via `.agents/rules/` or scoped subdirectories:

| Topic | File / Pointers |
| :--- | :--- |
| **Agent Behavior & Workflow** | [.agents/rules/agent-behavior.md](../.agents/rules/agent-behavior.md) (Gemini 3.8 Flash optimizations, DoD, max 3 retries, proof) |
| **Clean Architecture** | [.agents/rules/clean-architecture.md](../.agents/rules/clean-architecture.md) (Layer separation, Ports & Adapters) |
| **Python 3.12+ Style** | [.agents/rules/python-standards.md](../.agents/rules/python-standards.md) (Typing, Pydantic v2, immutability) |
| **Testing Standards** | [.agents/rules/testing-standards.md](../.agents/rules/testing-standards.md) (AAA, deterministic, fixtures) |
| **Domain Isolation** | [src/app/domain/AGENTS.md](../src/app/domain/AGENTS.md) (100% pure Python, zero framework imports) |
| **Sprint & Bugs** | [docs/ACTION_LIST.md](../docs/ACTION_LIST.md) (Active blockers and warnings protocol) |
| **Changelog** | [docs/CHANGELOG.md](../docs/CHANGELOG.md) (Keep a Changelog standard) |
| **Architecture Doc** | [docs/design/architecture.md](../docs/design/architecture.md) (Layers, data models, and dependency injection) |
