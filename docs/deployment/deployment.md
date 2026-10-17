<!-- docs/deployment/deployment.md -->
# Deployment & Runtime Guide

This guide details steps for running and deploying the application across development, testing, and production environments.

---

## 1. Local Runtime (uv & Uvicorn)

1. **Set Up Configuration**:
   ```bash
   cp .env.example .env
   # Adjust any environment variables or paths in .env as needed
   ```

2. **Apply Database Migrations**:
   ```bash
   make migrate
   ```

3. **Start Development Server**:
   ```bash
   make run
   # API is served at http://localhost:8000
   # Interactive Swagger docs: http://localhost:8000/docs
   ```

---

## 2. Docker Containerization

A multi-stage `Dockerfile` leverages `uv` for reproducible, lightning-fast builds:

```dockerfile
FROM python:3.12-slim AS builder

WORKDIR /app
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

COPY pyproject.toml README.md ./
RUN uv sync --frozen --no-dev --no-install-project

COPY src/ ./src/
RUN uv sync --frozen --no-dev

FROM python:3.12-slim AS runner

WORKDIR /app
COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app/src /app/src
COPY alembic.ini ./
COPY alembic/ ./alembic/

ENV PATH="/app/.venv/bin:$PATH"
ENV APP_ENV="production"

EXPOSE 8000
CMD ["uvicorn", "app.presentation.api:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 3. Production Health Checks

The application exposes a `/health` endpoint suitable for orchestrators (Kubernetes, Docker healthchecks, or load balancers):

```bash
curl -f http://localhost:8000/health || exit 1
```
