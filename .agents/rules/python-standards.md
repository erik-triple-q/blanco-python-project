<!-- .agents/rules/python-standards.md -->
# Python 3.12+ Code & Readability Standards

## 1. File Structure (Top-to-Bottom)
1. Module docstring (concise, focused, in English)
2. Standard library imports
3. Third-party imports
4. First-party imports (`app.*`)
5. Constants (`UPPER_SNAKE_CASE`)
6. Classes and functions

## 2. Syntax, Typing & Style
- **Type Hints**: Mandatory on all public functions and methods (PEP 585 & 604: `list[str]`, `int | None`). Avoid `Any` unless strictly unavoidable with explicit explanation (`# noqa: ANN401`).
- **Paths**: Exclusively `pathlib.Path`; `os.path` is forbidden.
- **Data & Validation**: Pydantic v2 with strict typing (`model_config = ConfigDict(strict=True, frozen=True)`).
- **Error Handling**: Custom domain exceptions; fail fast. Never use bare `except:`.
- **Comments**: Write comments exclusively for **why** (context, caveats, decisions), never for **what** the code already shows.
