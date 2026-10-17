<!-- src/app/domain/AGENTS.md -->
# Domain Layer Isolation Rules

- **Strict Pure Python**: ZERO imports of frameworks (FastAPI, Starlette), databases (SQLAlchemy, SQL), or network/disk I/O.
- **Rich Models**: Invariants and state transitions belong here (e.g. `item.activate()`). Never write anemic data bags.
- **Exceptions**: All domain errors must inherit from `DomainError` in `exceptions.py`.
