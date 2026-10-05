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

## Out of scope

<What this plan deliberately does not do, so that scope creep is visible when it
happens.>

## Deviations

<Filled in during implementation: what actually differed from this plan, and why.
Plan adherence is only measurable if the deviations are recorded.>
