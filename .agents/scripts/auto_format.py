# .agents/scripts/auto_format.py
"""Lifecycle hook script auto-formatting Python files after tool edits."""

import json
import subprocess
import sys
from pathlib import Path


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        print("{}")
        return

    tool_call = payload.get("toolCall", {})
    args = tool_call.get("args", {})
    target_file = args.get("TargetFile", "")

    if target_file and target_file.endswith(".py"):
        file_path = Path(target_file)
        if file_path.is_file():
            subprocess.run(
                ["uv", "run", "ruff", "format", str(file_path)],
                capture_output=True,
                check=False,
            )

    print("{}")


if __name__ == "__main__":
    main()
