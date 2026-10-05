# Runbook: <Operation or Service>

- **Owner:** <role/team>
- **Last exercised:** <YYYY-MM-DD>
- **Applies to:** <service/release/environment>
- **Escalation:** <controlled contact path>

## When to use

<Trigger, symptoms, and when not to use this runbook.>

## Prerequisites and safety

<Access, working directory, identity, backups, data sensitivity, side effects,
and approval needed.>

## Verify current state

```bash
<read-only status and identity commands>
```

Expected: <known healthy or target state>.

## Procedure

1. <one bounded action>
2. <verification immediately after action>
3. <next action>

## Success verification

<User-visible workflow, health, identity, permissions, data, signals, and cleanup.>

## Failure handling

| Symptom | Likely boundary | Safe action | Escalate when |
|---|---|---|---|
| | | | |

## Rollback or containment

<Exact trigger, command/procedure, state/index compatibility, verification, and
what cannot be reversed.>

## Evidence and closeout

<Run ID, time, operator, commands/results, release identity, deviations, incident
link, temporary access removal, and next review.>

