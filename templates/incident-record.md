# Incident: <Short Name>

- **Severity:** <per the operations standard>
- **Status:** Open/Contained/Resolved/Closed
- **Owner:** <incident lead>
- **Detected:** <YYYY-MM-DD HH:MM, and by what>
- **Resolved:** <YYYY-MM-DD HH:MM>
- **System:** <identity and release>

The first steps are in [`../delivery.md`](../delivery.md#incidents): stop, restore, tell the owner.
This is the record it produces, and the last link in the artifact chain: a
recurring failure mode should leave here as a new [`intent.md`](intent.md).

## What happened

<Plain description. What users experienced, not what the code did.>

## Timeline

| Time | Event | Source |
|---|---|---|
| | | Alert/user report/manual observation |

## Impact

<Users affected, data touched, actions taken by the system that cannot be undone,
duration, and cost. State what is unknown rather than estimating it silently.>

## Detection

<What caught it, and how long it took. If a human noticed before monitoring did,
say so: that is the most useful line in this document.>

## Containment and recovery

<What stopped the bleeding, what restored service, and whether rollback worked as
documented.>

## Contributing conditions

<The system conditions that made this possible. Avoid attributing a system failure
only to "the model" or "human error": both are descriptions of where the failure
surfaced, not of why the system allowed it.>

## Evidence gaps

<What could not be reconstructed, and what instrumentation would have answered it.>

## Corrective actions

| Action | Type | Owner | Due | Status |
|---|---|---|---|---|
| | Test/eval case/control/guidance/runbook | | | |

A closed incident whose failure mode can recur without a new control is not
closed. At least one action should make recurrence detectable or impossible.

## Reopen criteria

<What would reopen this, per the incident playbook.>
