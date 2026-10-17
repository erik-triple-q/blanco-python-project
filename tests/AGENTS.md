<!-- tests/AGENTS.md -->
# Testing Rules & Fixtures

- **Execution**: Run tests via `make test` or `uv run pytest tests/unit/ -v`.
- **Determinism**: Zero external network calls, zero `time.sleep()`. All tests must finish in milliseconds.
- **Style**: Use standalone pytest functions with the AAA pattern and `test_<what>_<when>_<expected>` naming.
- **Fixtures**: Utilize shared fixtures in `conftest.py` (`db_session`, `client`).
