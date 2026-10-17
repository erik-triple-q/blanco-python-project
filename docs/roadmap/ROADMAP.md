<!-- docs/roadmap/ROADMAP.md -->
# Product & Architecture Roadmap

This document outlines the strategic roadmap for future application capabilities.

---

## Milestones & Phasing

### Phase 1: Foundation & Baseline Tooling (Completed)
- [x] Clean Architecture package structure (`domain`, `application`, `infrastructure`, `presentation`).
- [x] Make workflow for standardized git commits, linters, and test suites.
- [x] Universal agent governance (`AGENTS.md` and `.gemini/GEMINI.md`).
- [x] SQLAlchemy 2.0 ORM + Alembic database migrations.

### Phase 2: Security & Authentication (Planned)
- [ ] Implement API Key and OAuth2 / JWT bearer authentication in the presentation layer.
- [ ] Add rate limiting middleware for public endpoints.
- [ ] Implement audit logging adapter in the infrastructure layer for critical operations.

### Phase 3: Observability & Production Readiness
- [ ] Structured JSON logging with correlation IDs via middleware.
- [ ] Prometheus metrics endpoint (`/metrics`) for latency and status code monitoring.
- [ ] Docker Compose setup for local multi-container integration testing (PostgreSQL).
