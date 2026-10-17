# Makefile
.PHONY: help install check format lint test commit push ship run migrate migration clean reset-repo health

PYTHON ?= uv run python
PYTEST ?= uv run pytest
RUFF ?= uv run ruff
ALEMBIC ?= uv run alembic

help:
	@echo "Available commands:"
	@echo "  make install         Install dependencies and pre-commit hooks"
	@echo "  make check           Run format check, linter and tests"
	@echo "  make format          Auto-format code and fix lint errors"
	@echo "  make lint            Run ruff linter"
	@echo "  make test            Run pytest test suite"
	@echo "  make run             Run FastAPI application with reload"
	@echo "  make health          Run health check against local service"
	@echo "  make migrate         Apply pending database migrations"
	@echo "  make migration m=... Generate new autodetected migration"
	@echo "  make commit m=...    Format, check, stage all, and commit"
	@echo "  make push            Push commits to active branch"
	@echo "  make ship m=...      Full release pipeline (commit + push)"
	@echo "  make reset-repo      Hard reset to origin branch preserving .env & data/"
	@echo "  make clean           Remove caches and temporary artifacts"

install:
	uv sync --all-extras
	uv run pre-commit install

format:
	$(RUFF) check --fix src tests .agents
	$(RUFF) format src tests .agents

lint:
	$(RUFF) check src tests .agents
	$(RUFF) format --check src tests .agents

test:
	$(PYTEST) $(ARGS)

check: lint test

commit:
	@if [ -z "$(m)" ]; then \
		echo "Error: commit message is required. Example: make commit m=\"feat(core): add item use case\""; \
		exit 1; \
	fi
	make format
	make check
	git add -A
	git commit -m "$(m)"

push:
	git push -u origin $$(git branch --show-current 2>/dev/null || git rev-parse --abbrev-ref HEAD)

ship:
	@if [ -z "$(m)" ]; then \
		echo "Error: commit message is required. Example: make ship m=\"feat(core): add item use case\""; \
		exit 1; \
	fi
	make commit m="$(m)"
	make push

run:
	uv run uvicorn app.presentation.api:app --reload --host 0.0.0.0 --port 8000

migrate:
	$(ALEMBIC) upgrade head

migration:
	@if [ -z "$(m)" ]; then \
		echo "Error: migration message is required. Example: make migration m=\"create_items_table\""; \
		exit 1; \
	fi
	$(ALEMBIC) revision --autogenerate -m "$(m)"

health:
	@curl -sf http://localhost:8000/health || (echo "Health check failed!"; exit 1)
	@echo "Service is healthy."

reset-repo:
	@echo "WARNING: Hard reset to origin/$$(git rev-parse --abbrev-ref HEAD) (preserving .env and data/)."
	@read -p "Are you sure? [y/N] " ans && ( [ "$$ans" = "y" ] || [ "$$ans" = "Y" ] ) || (echo "Aborted."; exit 1)
	git fetch origin
	git reset --hard origin/$$(git rev-parse --abbrev-ref HEAD)
	git clean -fd -e .env -e data/

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	rm -rf .coverage htmlcov dist build *.egg-info
