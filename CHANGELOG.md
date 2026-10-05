# Changelog

Notable changes to the playbook. Newest first.

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
