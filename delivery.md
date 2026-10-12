# Delivery: Branches, Review, Release

How a change goes from a branch to production in a FoodBear-Gauss repository.
Where the adopting repository's owner has set a different review or release
process, theirs wins. Write it in that repository's `AGENTS.md`.

## Changes and commits

- One change, one coherent outcome, one inspectable diff.
- Commits are focused and named for the behavior they change
  (`fix: record the reason when a push fails to launch`).
- Do not mix formatting churn, generated files or unrelated fixes into a
  behavioral change.
- Never rewrite shared history without the owner agreeing first.

## Pull requests

Every material change goes through a branch and a pull request. The PR states:

- outcome and scope;
- risk tier;
- key decisions, with links to ADRs;
- checks run, with results (passed, failed, skipped, not run);
- the issues it completes (`Closes #N`) or only touches (`Refs #N`);
- each "Done when" box from those issues, ticked, with its proof;
- evidence: re-read output, coverage-sheet rows, screenshots that support
  (not replace) reproducible checks;
- rollback;
- what is still uncertain.

## Review

Run three passes separately. One read looking for everything finds the easy
things and misses the rest.

| Pass | Looking for |
|---|---|
| Bugs | Logic errors, edge cases, regressions, broken contracts |
| Security | Secrets, authorization gaps, customer-data exposure, unsafe live writes |
| Compliance | Does it match the spec, the plan, the house rules and this playbook? |

R0 needs the Bugs pass; R1 and above need all three. A skipped pass is recorded
with its reason. Busy, trusted author and green CI are not reasons.

Every finding has a severity:

| Severity | Effect |
|---|---|
| Blocking | Does not merge |
| Material | Merges only with a filed follow-up and an owner |
| Minor | Author's call |
| Note | Never blocks |

### Merge policy

AI review is an input, not approval. A human who is not the author merges. The
author's self-review is a record of what they checked, not a pass.

The review passes above and this rule are the **merge policy**: they decide who
may merge and on what evidence. They do not define when an issue is done. An
adopting repository may set a stricter merge rule in its `AGENTS.md`. Letting a
defined low-risk class merge without human review is that repository's owner's
decision, recorded there; until then this rule stands.

Use [`templates/review.md`](templates/review.md).

## Done and closing

An issue is done when the PR that completes it merges into the default branch
and proves every "Done when" box on the issue. The PR body says `Closes #N`, so
GitHub closes the issue on merge, whoever merged it under the merge policy.
Anyone may reopen it with evidence. The full rule, the shared checklist and the
acceptance-criteria rules are in [`definition-of-done.md`](definition-of-done.md).

## Release

- Know exactly which version runs on which machine.
- Release in stages: one machine, then a few, then all.
- Exercise the rollback once before the release reaches every machine.
- New push behavior ships switched on for test stores only until the owner
  opens customer stores.
- After each release, check the run records for new failure reasons.

Use [`templates/runbook.md`](templates/runbook.md) for the release and rollback
steps.

## Incidents

If a live write goes wrong: stop all runs, restore the affected store, tell the
owner, then write the [`incident-record.md`](templates/incident-record.md).
Fix forward only after the restore is confirmed by a re-read.
