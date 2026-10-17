# Dockerfile
# Multi-stage build leveraging uv for fast, deterministic builds

# --- Stage 1: Build virtual environment ---
FROM python:3.12-slim AS builder

WORKDIR /build

# Install uv from official binary
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy project specification files
COPY pyproject.toml README.md uv.lock* ./

# Compile dependencies without workspace editable project
RUN uv sync --frozen --no-dev --no-install-project

# Copy source code and perform final install
COPY src/ ./src/
RUN uv sync --frozen --no-dev

# --- Stage 2: Final runtime container ---
FROM python:3.12-slim AS runner

WORKDIR /app

# Create non-privileged service user
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# Copy virtual environment and source code
COPY --from=builder /build/.venv /app/.venv
COPY --from=builder /build/src /app/src
COPY alembic.ini ./
COPY alembic/ ./alembic/

# Create runtime data directory with proper ownership
RUN mkdir -p /app/data && chown -R appuser:appgroup /app

USER appuser

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    APP_ENV="production" \
    PORT=8000 \
    HOST="0.0.0.0"

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD python3 -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

CMD ["uvicorn", "app.presentation.api:app", "--host", "0.0.0.0", "--port", "8000"]
