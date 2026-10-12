# Plan: <Short Name for the Change>

- **Status:** Proposed
- **Author:** <person or agent session>
- **Date:** <YYYY-MM-DD>
- **Spec:** <link to the spec.md this implements>
- **Approved by:** <who, and when: before implementation starts. On a solo change write
  "self" and the date; the gate is that the plan exists before the code does>

This is written and interrogated *before* code is written. It is not a status
log; that is the repository's `DEVLOG.md`.

## Files that change

| Path | Change | Why |
|---|---|---|
| | Add/Modify/Delete | |

Name them before starting. A file that turns out to need changing and is not on
this list is worth noticing: it usually means the spec missed something.

## Work order

1. <smallest independently verifiable slice, and what proves it works>
2. <next slice>

Each step should be reversible on its own. If step 3 cannot be undone without
undoing step 2, they are one step.

## Risks

| Risk | Likelihood | If it happens | Mitigation |
|---|---|---|---|
| | | | |

## Proof

<The specific commands, tests, and evaluations that will demonstrate this works,
and what their passing output looks like. Naming them now prevents the author grading
their own homework later.>

```bash
<command>
```

## Done when

<1 to 7 boxes, copied from the issue. Each one is provable inside the PR: a test,
a command with its expected output, or a file and line to re-read. See
[`../definition-of-done.md`](../definition-of-done.md#acceptance-criteria).>

- [ ] <observable result>: proved by <test, command, or file:line>

## Gates

<Steps only a person can do, such as a second engineer's re-run or the owner's
sign-off. They are not "Done when" boxes. Say whether each one must happen
before merge (part of the merge policy) or after it (a follow-up issue).>

| Gate | Owner | Before or after merge | Follow-up issue |
|---|---|---|---|
| | <named person> | | <#N, for after-merge gates> |

## Out of scope

<What this plan deliberately does not do, so that scope creep is visible when it
happens.>

## Deviations

<Filled in during implementation: what actually differed from this plan, and why.
Plan adherence is only measurable if the deviations are recorded.>
