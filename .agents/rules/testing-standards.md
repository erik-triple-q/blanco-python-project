<!-- .agents/rules/testing-standards.md -->
# Testing Standards (pytest)

## 1. Principles
- Standalone pytest functions (avoid `unittest.TestCase`).
- 100% deterministic and fast (< milliseconds/seconds).
- NEVER make live external API calls or network requests in unit tests — always mock via protocols or in-memory doubles.
- No `time.sleep()`.

## 2. Test Structure & Naming
- Test name: `test_<what>_<when>_<expected>` (e.g. `test_activate_item_when_draft_sets_active_status`).
- AAA pattern: Arrange, Act, Assert. Maximum of 1 logical assertion per test.
- Shared database and client fixtures in `tests/conftest.py` (in-memory SQLite `db_session`, `TestClient`).
