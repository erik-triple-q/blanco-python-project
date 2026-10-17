# .agents/skills/python-clean-starter/scripts/scaffold.py
"""Scaffolding generator for Python Clean Architecture projects."""

import argparse
import shutil
from pathlib import Path


def scaffold_project(name: str, dest_dir: Path) -> None:
    """Scaffold a full Python Clean Architecture starter template."""
    dest_dir = dest_dir.resolve()
    dest_dir.mkdir(parents=True, exist_ok=True)
    template_root = Path(__file__).resolve().parent.parent.parent.parent

    # Files and folders to copy verbatim
    copy_items = [
        "Makefile",
        ".gitignore",
        ".pre-commit-config.yaml",
        ".env.example",
        "Dockerfile",
        ".dockerignore",
        "alembic.ini",
        "alembic",
        "AGENTS.md",
        ".github",
        ".agents",
        ".gemini",
        "docs",
        "tests",
    ]

    for item in copy_items:
        src_path = template_root / item
        dst_path = dest_dir / item
        if src_path.is_file():
            shutil.copy2(src_path, dst_path)
        elif src_path.is_dir():
            if dst_path.exists():
                shutil.rmtree(dst_path)
            shutil.copytree(src_path, dst_path)

    # Setup src/<name>/ with domain, application, infrastructure, presentation
    src_dir = dest_dir / "src"
    target_package_dir = src_dir / name
    if (src_dir / "app").exists():
        (src_dir / "app").rename(target_package_dir)

    # Customize pyproject.toml
    pyproject_file = dest_dir / "pyproject.toml"
    if (template_root / "pyproject.toml").is_file():
        content = (template_root / "pyproject.toml").read_text(encoding="utf-8")
        content = content.replace('name = "app"', f'name = "{name}"')
        content = content.replace('packages = ["src/app"]', f'packages = ["src/{name}"]')
        content = content.replace('known-first-party = ["app"]', f'known-first-party = ["{name}"]')
        pyproject_file.write_text(content, encoding="utf-8")

    # Customize README.md
    readme_file = dest_dir / "README.md"
    readme_content = f"""# {name}

Production-ready Python 3.12+ app built with Clean Architecture, DDD, and Gemini 3.8 Flash rules.

## Quickstart

```bash
make install     # Install dependencies and pre-commit hooks
make check       # Run linters and test suite
make run         # Run FastAPI server
```
"""
    readme_file.write_text(readme_content, encoding="utf-8")

    print(f"Successfully scaffolded Python Clean Architecture project '{name}' at: {dest_dir}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Scaffold a new Python Clean Architecture project."
    )
    parser.add_argument("--name", required=True, help="Package name (e.g. billing_service)")
    parser.add_argument("--dest", required=True, help="Destination directory path")
    args = parser.parse_args()

    scaffold_project(args.name, Path(args.dest))


if __name__ == "__main__":
    main()
