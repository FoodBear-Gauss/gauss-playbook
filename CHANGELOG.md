# Changelog

Notable changes to the playbook. Newest first.

## Unreleased

- `CLAUDE.md` imports `AGENTS.md` with `@AGENTS.md` and keeps only Claude Code
  notes. `adopt/README.md` step 2 says to do the same.
- `AGENTS.md` and `adopt/AGENTS-block.md`: stop and ask when a permission, hook
  or guard refuses an action; use closing keywords only for issues the owner
  means to close (lessons from the engine's W1). The adopt block's Definition
  of Done line names the check that enforces it.
- `definition-of-done.md`: links the merge policy instead of restating it and
  names the engine's CI guard as an example. `glossary.md`: merge policy.
  `templates/prd.md`: "Done when (project level)".
- `definition-of-done.md`, the org-wide Definition of Done: the shared
  checklist, acceptance-criteria rules (every "Done when" box provable in a PR;
  person-only steps become a gate or a follow-up issue with an owner), closing
  on merge to the default branch through a closing keyword, integration
  branches, reopening with evidence, status words and a short Definition of
  Ready. Cites the Scrum Guide, GitHub Docs, DORA and others.
- `delivery.md`: the review rules are named as the merge policy, separate from
  done; a new "Done and closing" section; PRs list the issues they complete and
  the proof for each "Done when" box.
- `templates/plan.md`: "Done when" and "Gates" sections.
- `glossary.md`: acceptance criteria, Definition of Done, done.
- `AGENTS.md`, `README.md` and `adopt/AGENTS-block.md` point to the new page.
  `scripts/check.py` requires it. (PR #2)
- Claude Code enforcement kit in `adopt/claude/`: a PreToolUse hook that asks
  before a Bash command matching a live-write pattern runs (it never approves),
  an empty pattern file with generic examples, and a settings template that
  denies reading secret files and editing the guard through file tools.
- Unit tests for the hook in `tests/`, run in CI.
- `templates/progress.md`, a resume note for long or multi-session tasks.
- `AGENTS.md`: a Long tasks section (completion condition, progress note,
  reviewer verdicts, re-read after a timed-out write) and a pointer to the kit.
  (PR #1)

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
