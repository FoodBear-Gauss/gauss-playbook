# Templates

Copy a template into the adopting repository (usually under `docs/`), replace
every `<placeholder>` with verified facts, and delete sections the change does
not need rather than writing "n/a".

| Template | Use it for | Lifecycle phase |
|---|---|---|
| [`intent.md`](intent.md) | A one-page problem and outcome, before anything is designed | Frame |
| [`prd.md`](prd.md) | Scope, users, risk tier and requirements for substantial work | Frame |
| [`spec.md`](spec.md) | Contracts, boundaries, failure modes and how it will be verified | Design |
| [`threat-model.md`](threat-model.md) | What the system can touch, and what could go wrong | Design |
| [`adr.md`](adr.md) | One architectural decision, with the options considered | Design |
| [`plan.md`](plan.md) | Files that change, order, risks, proof; written before the code | Build |
| [`progress.md`](progress.md) | Resume note for a long or multi-session task: done with evidence, decisions, next action | Build |
| [`review.md`](review.md) | The three review passes, findings and severities | Verify |
| [`coverage-sheet.md`](coverage-sheet.md) | Every check for one action on one platform, with evidence | Verify |
| [`runbook.md`](runbook.md) | Release, rollback, restore and stop-all steps | Release |
| [`weekly-report.md`](weekly-report.md) | One page for the owner each week | Operate |
| [`incident-record.md`](incident-record.md) | What happened when something went wrong, and what changed | Operate, Learn |

`intent`, `prd`, `spec`, `plan`, `adr`, `review`, `runbook` and `incident-record`
are adapted from the AI Engineering Playbook. `threat-model`, `coverage-sheet`,
`weekly-report` and `progress` are written for Gauss.
