# .agents/scripts/git_safety.py
"""Lifecycle hook script blocking autonomous git mutations."""

import json
import re
import sys

FORBIDDEN_GIT_PATTERNS = [
    r"\bgit\s+commit\b",
    r"\bgit\s+push\b",
    r"\bgit\s+rebase\b",
    r"\bgit\s+merge\b",
    r"\bmake\s+(commit|ship|push)\b",
    r"\bgit\s+reset\s+--hard\b",
    r"\bgit\s+clean\s+-[a-zA-Z]*f\b",
    r"\bgit\s+restore\s+(\.|\/)\b",
    r"\bgit\s+checkout\s+--\s+(\.|\/)\b",
]


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        # Fallback to allow if input cannot be parsed
        print(json.dumps({"decision": "allow"}))
        return

    tool_call = payload.get("toolCall", {})
    args = tool_call.get("args", {})
    command_line = args.get("CommandLine", "")

    for pattern in FORBIDDEN_GIT_PATTERNS:
        if re.search(pattern, command_line):
            response = {
                "decision": "deny",
                "reason": (
                    f"Blocked by project safety hook: Command '{command_line}' "
                    f"matches forbidden pattern '{pattern}'. "
                    "Git mutations must be executed manually by the user "
                    "via Makefile (e.g. 'make commit' or 'make ship')."
                ),
            }
            print(json.dumps(response))
            return

    print(json.dumps({"decision": "allow"}))


if __name__ == "__main__":
    main()
