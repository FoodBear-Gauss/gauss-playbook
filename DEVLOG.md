# Devlog

Current state, open work and evidence. Newest first.

## 2026-10-12: Definition of Done

**State.** `definition-of-done.md` sets the org-wide rule decided by the
program lead on 12 Oct 2026: an issue is done, and closes, when its PR merges
into the default branch and proves every "Done when" box, with or without a
human review. `delivery.md` keeps its review and merge rules and now calls them
the merge policy, separate from done. `scripts/check.py` and the unit tests
pass locally.

**Open.**

- The merge policy is unchanged: a human who is not the author merges. Whether
  a defined low-risk class may merge without human review is a decision for
  each adopting repository's owner. For the engine (R3), that is Damien.
- No CI check yet enforces the "Done when" rule. The engine is to add one with
  its ADR 0021; the playbook only says a repository should.
- Some research sources were seen only in search summaries (the Scrum.org
  articles). Their wording should be re-checked before anyone quotes them.

## 2026-10-08: Claude Code enforcement kit

**State.** `adopt/claude/` adds a live-write guard hook, a pattern file and a
settings template. `templates/progress.md` and the Long tasks section in
`AGENTS.md` are added. The unit tests and `scripts/check.py` pass locally.

An adversarial review found one material gap: deleting the pattern file
through Bash switched the guard off silently. The hook now asks on any
command that names its own files, treats a pattern file it cannot read as
misconfigured, shows matched text past the first 300 characters, and runs
with a 10 second timeout. `scripts/check.py` now also scans `.py`, `.json`
and `.yml` files. 20 tests pass.

**Unproven.**

- The hook has never fired inside a real Claude Code session or an adopting
  repository. The unit tests feed it JSON directly. The kit README's "Test it
  once" step is **not run**.
- The settings template's deny rules have not been tried in a session.
- No real patterns exist yet. They come from discovery in the adopting
  repository, which has not happened.

## 2026-10-05: first version

**State.** Version 0.1.0 is written and `scripts/check.py` passes locally.

**Open.**

- No repository has adopted the playbook yet. The first adoption depends on the
  owner agreeing how our work reaches FoodBear's repositories.
- The behavioral check in `TESTING.md` (a fresh agent session refuses a live
  write to a customer store) has not been run. It needs an adopting repository.
- No license is set. Decide before anyone outside the team reuses it.
- The source playbook is private, so readers cannot follow a link to it. This
  repository is written to stand on its own.
