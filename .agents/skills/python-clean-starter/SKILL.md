---
name: python-clean-starter
description: >-
  Scaffolds and initializes production-ready Python 3.12+ applications following Clean
  Architecture, Domain-Driven Design (DDD), SOLID, and Ponytail (KISS/YAGNI) principles.
  Sets up uv package management, Ruff formatting and linting, pytest suites, Alembic migrations,
  lean AGENTS.md index, Antigravity lifecycle hooks (.agents/hooks.json), modular rules
  (.agents/rules/), GitHub Actions CI, and multi-stage Dockerfile. Use whenever starting a new
  Python project, scaffolding a repository, or configuring Antigravity rules and hooks for Python.
---

# Python Clean Starter

This skill provides a standardized workflow to bootstrap, structure, or audit Python 3.12+ applications adhering to Clean Architecture, Domain-Driven Design, and modern Google Antigravity agent standards.

---

## Architecture Overview

Every project scaffolded by this skill enforces strict layer separation:

```
[ Presentation (FastAPI, CLI) ]
             │
             ▼
[ Infrastructure (SQLAlchemy, Adapters) ]
             │
             ▼
[ Application (Services, Protocols/Ports) ]
             │
             ▼
[ Domain (Entities, Value Objects, Domain Errors) ]
```

---

## Scaffolding Workflow

When a user asks to start a new Python project or initialize a repository:

### Step 1: Run the Scaffolding Script
If bootstrapping into a new directory:
```bash
python3 .agents/skills/python-clean-starter/scripts/scaffold.py --name <package_name> --dest <target_path>
```

Or manually ensure the following core files exist:
- `pyproject.toml` (with uv, ruff, pytest, alembic, fastapi)
- `Makefile` (`check`, `format`, `lint`, `test`, `commit`, `ship`, `run`, `migrate`)
- `.agents/hooks.json` (with `git_safety.py` and `auto_format.py`)
- `.agents/rules/` (`agent-behavior.md`, `clean-architecture.md`, `python-standards.md`, `testing-standards.md`)
- `AGENTS.md` and `.gemini/GEMINI.md` (lean index with Definition of Done)
- `Dockerfile` and `.dockerignore`
- `.github/workflows/ci.yml`
- `docs/` (`README.md`, `ACTION_LIST.md`, `CHANGELOG.md`, `design/architecture.md`, `deployment/deployment.md`)
- `src/<package_name>/` (`domain/`, `application/`, `infrastructure/`, `presentation/`, `py.typed`)
- `tests/` (`conftest.py`, `unit/`, `integration/`)

### Step 2: Install Dependencies & Pre-Commit
```bash
make install
```

### Step 3: Run the Quality Gate
Verify that the generated template is 100% green before adding business logic:
```bash
make check
```

---

## Agent Operational Rules

1. **Outcome-over-Process**: Do not require upfront `/plan` mode for well-scoped tasks; verify against `make check` and deliver proof.
2. **Lean Index**: Keep root `AGENTS.md` short (< 50 lines). Place domain-specific or testing rules into `.agents/rules/` or sub-directories.
3. **Safety Hooks**: Autonomous git commits and pushes are strictly blocked by `.agents/hooks.json`. Guide the user to run `make commit m="..."` or `make ship m="..."`.
4. **Retry Limit**: If checks fail, attempt at most 3 autonomous fixes before pausing to consult the user with the exact error output.
