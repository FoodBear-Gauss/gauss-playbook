# Agent Instructions

<!-- Copy this block to the top of the repository's AGENTS.md and fill in every <placeholder>. -->

This repository follows the Gauss playbook:
https://github.com/FoodBear-Gauss/gauss-playbook (version: `<commit or tag>`).
Read its `AGENTS.md` once. **This repository's own rules win** where they are
more specific.

## Project contract

- **What this repository does:** <one sentence>
- **Owner (gives the go for live writes):** <name>
- **Risk tier:** <R0/R1/R2/R3, and why>
- **House rules:** <link; they override the playbook>
- **Test stores:** <names or link; live tests happen only here>
- **Project documents:** `docs/`
- **Review and merge:** <who reviews, who merges>
- **Release and rollback:** <link to runbook>
- **Stop all runs:** <command or procedure>

## Commands

```bash
<install>
<lint>
<test>
<dry-run a push>
```

Never claim a check passed if it did not run.

## Permissions

- **Do freely:** read code, run tests, run dry runs, edit on a branch.
- **Ask first:** any live write, a release, a migration, a new dependency or
  network call, anything touching credentials.
- **Never:** write to a store that is not a test store, arm your own push,
  commit secrets, weaken a test or CI guard, merge your own PR.
