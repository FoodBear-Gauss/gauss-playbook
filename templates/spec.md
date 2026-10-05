# Spec: <Short Name for the Change>

- **Status:** Draft
- **Owner:** <role>
- **Date:** <YYYY-MM-DD>
- **Risk tier:** <R0/R1/R2/R3 with rationale>
- **Intent:** <link to the intent.md this answers>

## What it must do

<Required behavior, in terms a test could be written against. Include the
non-goals: the things a reader might reasonably assume are in scope.>

## Current state and gaps

<For an adoption or migration change: what exists today, and each applicable control
marked met, partial, not met, not applicable, or unknown: with evidence. Omit for
ordinary feature work.>

## Contracts

Fill only the rows this change actually touches; delete the rest rather than writing "n/a". Definitions are in
the project's architecture document.

| Contract | This change |
|---|---|
| User | <what the user is promised, including what happens on failure> |
| Capability | <what the system does, and its stated limits> |
| Data | <sources, classification, allowed purpose, retention> |
| Tool | <tools called, side-effect class, permissions> |
| Evaluation | <how correct behavior is demonstrated> |
| Operations | <how it is run, observed, and rolled back> |

## Design

<Components, data flow, trust boundaries, and where the human authority boundary
sits. A diagram beats a paragraph.>

## Flagged concerns

Raise them here rather than resolving them quietly. A concern that was considered
and accepted is useful evidence; a concern that was never written down is not.

| Concern | Raised by | Severity | Resolution | Accepted by |
|---|---|---|---|---|
| | | Blocking/Material/Minor | Resolved/Accepted/Deferred | |

## Alternatives considered

<What else would work, and why this instead. If the decision is architecturally
significant, it belongs in an ADR: link it.>

## How it will be verified

<The evaluation question, dataset, thresholds, and deterministic tests. Predeclared,
per [`../lifecycle.md`](../lifecycle.md#verification-in-practice).>

## Open questions carried forward

<Anything from the intent still unresolved, and what it now blocks.>
