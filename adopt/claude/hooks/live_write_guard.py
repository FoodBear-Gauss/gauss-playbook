#!/usr/bin/env python3
"""Live-write guard: a Claude Code PreToolUse hook for the Bash tool.

Reads the hook input (JSON) on stdin. When a Bash command matches a pattern in
<project>/.claude/live-write-patterns.json, it returns "ask", so a person has to
approve that exact command. It never returns "allow".

  - Not a Bash call: no output (no decision).
  - Hook input unreadable, or no tool_input.command: "ask", with or without a
    pattern file.
  - Command mentions the guard's own files (pattern file, hook, .claude/settings):
    "ask", always, even with no pattern file. This stops a Bash `rm` or `mv` from
    switching the guard off without a person seeing it.
  - No pattern file: no output. The guard is not configured yet.
  - Pattern file broken (including a directory, or an empty pattern): "ask" on
    every Bash command (fails closed, loudly).
  - Command matches a pattern: "ask", with the matched text and the command in
    the reason.

Python 3.9+, standard library only. See adopt/claude/README.md in the Gauss
playbook.
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

CONFIG = Path(".claude") / "live-write-patterns.json"
MAX_SHOWN = 300
CONTEXT = 100
# Always on, whether or not the pattern file exists.
SELF_PROTECT = re.compile(r"live-write-patterns|live_write_guard|\.claude/settings")


def ask(reason: str) -> int:
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": reason,
        }
    }))
    return 0


def load_patterns(path: Path) -> list[re.Pattern[str]]:
    """Return compiled patterns. Raise ValueError with a short detail if broken."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError) as exc:
        raise ValueError(f"cannot read {path.name}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"{path.name} is not valid JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"{path.name} must be a JSON object")
    raw = data.get("patterns")
    if not isinstance(raw, list):
        raise ValueError(f'{path.name}: "patterns" must be a list')
    compiled = []
    for item in raw:
        if not isinstance(item, str):
            raise ValueError(f'{path.name}: pattern {item!r} is not a string')
        if not item:
            raise ValueError(f'{path.name}: empty pattern "" would match every command')
        try:
            compiled.append(re.compile(item))
        except re.error as exc:
            raise ValueError(f"{path.name}: pattern {item!r} does not compile: {exc}") from exc
    return compiled


def shown(command: str, start: int, end: int) -> str:
    """The head of the command, plus the matched text in context if it is past the head."""
    head = command if len(command) <= MAX_SHOWN else command[:MAX_SHOWN] + "..."
    if end <= MAX_SHOWN:
        return f"Command: {head}"
    lo, hi = max(0, start - CONTEXT), min(len(command), end + CONTEXT)
    window = ("..." if lo else "") + command[lo:hi] + ("..." if hi < len(command) else "")
    return f"Matched text: {command[start:end]!r} in: {window} Command start: {head}"


def main() -> int:
    try:
        event = json.loads(sys.stdin.read())
    except (ValueError, UnicodeDecodeError):
        return ask("live-write guard could not read the hook input (not JSON). "
                   "Check this command by hand before approving.")
    if not isinstance(event, dict) or "tool_name" not in event:
        return ask("live-write guard could not read the hook input (no tool_name). "
                   "Check this command by hand before approving.")
    if event.get("tool_name") != "Bash":
        return 0

    tool_input = event.get("tool_input")
    command = tool_input.get("command") if isinstance(tool_input, dict) else None
    if not isinstance(command, str):
        return ask("live-write guard found no tool_input.command in the hook input. "
                   "Check this command by hand before approving.")

    m = SELF_PROTECT.search(command)
    if m:
        return ask(
            "This command touches the live-write guard's own files (pattern file, "
            f"hook or .claude/settings). {shown(command, m.start(), m.end())} "
            "Deleting, moving or rewriting them switches the guard off. Approve only "
            "if a person meant to change the guard."
        )

    project = os.environ.get("CLAUDE_PROJECT_DIR") or event.get("cwd") or os.getcwd()
    config = Path(project) / CONFIG
    if not config.exists():
        return 0  # not configured yet; stay silent rather than ask on every command
    try:
        patterns = load_patterns(config)
    except ValueError as exc:
        return ask(f"live-write guard misconfigured: {exc}")

    for pattern in patterns:
        m = pattern.search(command)
        if m:
            return ask(
                f"Possible live write (matches {pattern.pattern!r}). "
                f"{shown(command, m.start(), m.end())} "
                "A live write needs a go from the owner for this exact action and a "
                "person to arm it (risk-and-approval.md). Approve only if both are true."
            )
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # fail closed: a crash would otherwise not block
        sys.exit(ask(f"live-write guard error: {type(exc).__name__}: {exc}"))
