# Review: <PR or Change Identity>

- **Reviewer:** <person or agent>
- **Date:** <YYYY-MM-DD>
- **Risk tier:** <R0/R1/R2/R3, per ../risk-and-approval.md: this decides which passes are required>
- **Spec / plan:** <links>

AI review is an input, not merge approval or risk acceptance. See
[`../delivery.md`](../delivery.md#review).

State whether this is the author's self-review (a record) or an independent review (the
passes). An independent reviewer re-runs the checks; a self-review says so in its title.

## Passes

Run each pass separately. A single read looking for everything finds the easy
things and misses the rest.

| Pass | Looking for | Skipped? |
|---|---|---|
| Bugs | Logic errors, broken edge cases, regressions, contract violations | |
| Security | Injection, authorization gaps, secret and PII exposure, unsafe side effects | |
| Compliance | Does it match the spec, the plan, and the standards it claims to follow: name any claimed document not read as out of scope | |

## Checks

| Check | State | Evidence |
|---|---|---|
| <command> | Run locally / Run in CI / Skipped / Could not run / Substituted by <what> | <output or link> |

## Severity

| Severity | Meaning | Effect |
|---|---|---|
| Blocking | Wrong behavior, data loss, or an unreviewed security or privacy exposure | Does not merge |
| Material | Real defect or contract gap that will cost more to fix later | Merges only with a filed follow-up and an owner |
| Minor | Clarity, consistency, or a better approach | Merges; author's call |
| Note | Observation with no action requested | Never blocks |

Severity describes the consequence if this ships as-is: not how confident the
reviewer is, and not how much work the fix would be.

## Skip rules

A pass may be skipped when the reason is recorded. Legitimate reasons:

- the change cannot touch that surface (a docs-only change skips Security);
- the pass ran on an earlier revision and the diff since is unrelated;
- the risk tier does not require it.

Not legitimate: time pressure, a trusted author, or a green CI run. Record every
skip in the table above: an unrecorded skip is indistinguishable from a pass.

## Findings

| ID | Pass | Severity | File:line | Finding | Resolution | Owner | Due |
|---|---|---|---|---|---|---|---|
| R-001 | | | | | Fixed/Accepted/Deferred/Disputed | <required for Material> | <condition or date, required for Material> |

For an absence, cite the line that makes the claim the absence breaks. A Material
finding with no owner and due condition is not filed and does not merge.

## Recommendation

<Reviewer: approve / changes requested / blocked, and the one finding that decides it.>

## Decision

<The human who made the call, what they decided, and the date. Blank until they have.>
