#!/usr/bin/env python3
"""Structural checks for the Gauss playbook. Standard library only.

Checks:
  1. Required files exist.
  2. Every relative Markdown link resolves, including #anchors to headings.
  3. Every template in templates/ is listed in templates/README.md.
  4. No secrets, local machine paths or commercial figures are committed
     (Markdown, Python, JSON and YAML files, except this script).

Exit 0 when all pass, 1 otherwise.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED = [
    "README.md", "AGENTS.md", "CLAUDE.md", "TESTING.md", "CHANGELOG.md", "DEVLOG.md",
    "principles.md", "lifecycle.md", "risk-and-approval.md", "delivery.md", "glossary.md",
    "adopt/README.md", "adopt/AGENTS-block.md", "templates/README.md", "templates/progress.md",
    "adopt/claude/README.md", "adopt/claude/settings.json",
    "adopt/claude/live-write-patterns.example.json", "adopt/claude/hooks/live_write_guard.py",
    "tests/test_live_write_guard.py",
]

FORBIDDEN = [
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), "private key"),
    (re.compile(r"\bAKIA[0-9A-Z]{16}\b"), "AWS access key"),
    (re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"), "GitHub token"),
    (re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"), "API key"),
    (re.compile(r"/Users/[A-Za-z0-9._-]+/|C:\\\\Users\\\\"), "local machine path"),
    (re.compile(r"\bTHB\b|฿"), "commercial figure (currency)"),
]

LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")
FENCE = re.compile(r"^(```|~~~)")


def slug(heading: str) -> str:
    """GitHub-style heading anchor."""
    s = heading.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


def anchors(path: Path) -> set[str]:
    out, in_fence = set(), False
    for line in path.read_text(encoding="utf-8").splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence and line.startswith("#"):
            out.add(slug(line.lstrip("#")))
    return out


def markdown_files() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)


def scanned_files() -> list[Path]:
    """Files checked for forbidden content: Markdown, Python, JSON and YAML."""
    out = []
    for ext in ("*.md", "*.py", "*.json", "*.yml", "*.yaml"):
        out += [p for p in ROOT.rglob(ext) if ".git" not in p.parts]
    return sorted(p for p in out if p.resolve() != Path(__file__).resolve())


def main() -> int:
    errors: list[str] = []

    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            errors.append(f"missing required file: {rel}")

    for md in markdown_files():
        rel_md = md.relative_to(ROOT)
        text = md.read_text(encoding="utf-8")
        in_fence = False
        for n, line in enumerate(text.splitlines(), 1):
            if FENCE.match(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            for target in LINK.findall(line):
                if re.match(r"^[a-z]+:", target):
                    continue  # external URL or mailto
                path_part, _, anchor = target.partition("#")
                dest = md if not path_part else (md.parent / path_part).resolve()
                if not dest.exists():
                    errors.append(f"{rel_md}:{n}: broken link {target}")
                elif anchor and dest.suffix == ".md" and anchor not in anchors(dest):
                    errors.append(f"{rel_md}:{n}: missing anchor {target}")

    for path in scanned_files():
        rel = path.relative_to(ROOT)
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for pattern, label in FORBIDDEN:
                if pattern.search(line):
                    errors.append(f"{rel}:{n}: forbidden content ({label})")

    index = (ROOT / "templates/README.md").read_text(encoding="utf-8")
    for tpl in sorted((ROOT / "templates").glob("*.md")):
        if tpl.name != "README.md" and f"({tpl.name})" not in index:
            errors.append(f"templates/README.md does not list {tpl.name}")

    for e in errors:
        print(f"FAIL {e}")
    print(f"{'FAILED' if errors else 'OK'}: {len(markdown_files())} Markdown files, {len(errors)} problem(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
