# Adopt the Playbook in a Repository

Adoption is **additive and reversible**. It adds a few documents and a pointer
to this playbook. It never overrides the repository's own rules, and nothing is
added to a repository without its owner agreeing.

## Steps

1. **Agree with the owner** who reviews, merges and releases, and where project
   documents live. Write the answers into the repository's `AGENTS.md`.
2. **Add the agent block.** Copy [`AGENTS-block.md`](AGENTS-block.md) into the
   top of the repository's `AGENTS.md` (create it if missing) and fill in the
   placeholders. Add a `CLAUDE.md` that says "Read AGENTS.md."
3. **Link the house rules.** If the owner has house rules, link them from
   `AGENTS.md`. Do not restate them; one copy, one source of truth.
4. **Create `docs/`** with only what the first change needs:

   ```text
   docs/
     intent.md or prd.md
     spec.md
     threat-model.md
     adr/0001-<first-decision>.md
     runbook.md
   ```

5. **Make one rule mechanical.** Add the cheapest check that enforces something
   that matters (for example: no write script runs without a dry-run flag on
   staging). See [`../principles.md`](../principles.md#8-move-enforcement-into-code).
   If the team uses Claude Code, also install the enforcement kit in
   [`claude/`](claude/README.md): a hook that asks before a live-write command
   runs, and deny rules for secret files. It covers Claude's Bash tool only, so
   keep the in-script guard as well.
6. **Trial it on a real change.** Take one change from intent to release. Then
   ask a fresh agent session in the repository: "May I push a price change to a
   customer store?" It should say no and cite the rule.

## Adoption passes when

A new engineer and a fresh agent session can each find, without help:

- what the repository does, and its risk tier;
- the house rules, and which stores are test stores;
- the exact build and test commands;
- how a change is reviewed, released and rolled back;
- who gives a go for a live write.

## Rollback

If an adopted rule blocks valid work or causes unsafe behavior, disable that one
rule, keep the evidence, and raise it in this repository. Never delete history or
tests to undo adoption.
