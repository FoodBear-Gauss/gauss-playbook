# Changelog

Notable changes to the playbook. Newest first.

## Unreleased

- Claude Code enforcement kit in `adopt/claude/`: a PreToolUse hook that asks
  before a Bash command matching a live-write pattern runs (it never approves),
  an empty pattern file with generic examples, and a settings template that
  denies reading secret files and editing the guard through file tools.
- Unit tests for the hook in `tests/`, run in CI.
- `templates/progress.md`, a resume note for long or multi-session tasks.
- `AGENTS.md`: a Long tasks section (completion condition, progress note,
  reviewer verdicts, re-read after a timed-out write) and a pointer to the kit.

## 0.1.0 (2026-10-05)

First version.

- Agent contract (`AGENTS.md`) with the live-write rules: dry run by default, a
  go for the exact action, a person arms, test stores first, re-read after
  writing.
- Principles, delivery lifecycle, risk tiers R0 to R3 with recorded exceptions,
  and the approval boundary.
- Delivery standard: pull-request contents, three review passes with
  severities, staged release with an exercised rollback.
- Eleven templates, including a threat model, coverage sheet and weekly report
  written for push-lane work.
- Adoption steps and a drop-in `AGENTS.md` block for FoodBear-Gauss repositories.
- `scripts/check.py` and a CI workflow that runs it.
