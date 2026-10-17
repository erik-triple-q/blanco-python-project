<!-- docs/README.md -->
# Documentation Dashboard

Welcome to the central documentation hub. This project maintains a strict Clean Architecture & Domain-Driven Design (DDD) structure in Python 3.12+.

---

## Navigation & Document Structure

| Document | Purpose & Contents |
| :--- | :--- |
| [docs/ACTION_LIST.md](ACTION_LIST.md) | **Active sprint tracker**, current incidents, warnings, and action items (< 50 lines). |
| [docs/CHANGELOG.md](CHANGELOG.md) | Version history adhering to the *Keep a Changelog* standard. |
| [docs/design/architecture.md](design/architecture.md) | Clean Architecture specification, layer separation, protocols, and DDD entities. |
| [docs/design/DESIGN_SYSTEM.example.md](design/DESIGN_SYSTEM.example.md) | Reference design tokens and UI/UX guidelines (for projects with a web/frontend interface). |
| [docs/deployment/deployment.md](deployment/deployment.md) | Deployment guide, Docker containerization, environment variables, and CI/CD. |
| [docs/roadmap/ROADMAP.md](roadmap/ROADMAP.md) | Strategic roadmap and future feature milestones. |
| [AGENTS.md](../AGENTS.md) | Universal agent rules, engineering standards, and constraints. |

---

## Development Quick Reference

```bash
make install     # Install dependencies and git pre-commit hooks
make check       # Run linters, format check, and test suite
make run         # Start local FastAPI server with auto-reload
make migrate     # Apply database migrations via Alembic
```
