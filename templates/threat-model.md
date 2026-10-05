# Threat Model: <System or Change>

- **Owner:** <role>
- **Date:** <YYYY-MM-DD>
- **Risk tier:** <R0/R1/R2/R3>
- **Review trigger:** <new platform, new write path, new data, incident>

Keep it to what this system can actually do. A threat model that lists every
possible attack and ranks none of them is not used.

## What the system can touch

| Asset | Where it lives | Who can read | Who can write | Reversible? |
|---|---|---|---|---|
| <menus, prices, promotions, credentials, run records, customer data> | | | | |

## Trust boundaries

<Where data or instructions cross from one trust level to another: operator
machine to backend, backend to delivery platform, shared sheet to push script,
agent session to live write. A diagram is welcome.>

## Threats and failure modes

Include accidents as well as attacks. For a push system, silent success and
writing to the wrong store usually matter more than an outside attacker.

| ID | Threat or failure | How it happens | Impact | Likelihood | Control | Check that proves the control |
|---|---|---|---|---|---|---|
| TM-1 | Wrong store written | | | | | |
| TM-2 | Silent success (reported done, platform unchanged) | | | | | |
| TM-3 | Credential or session leaked | | | | | |
| TM-4 | Untrusted content steers an agent into a live write | | | | | |
| TM-5 | Partial write left after a failure | | | | | |

## Abuse cases

<How a careless or hostile user, script or agent could misuse the write path,
and what stops it.>

## Data handling

<What data is read, stored, logged, retained and deleted, and for how long.
Nothing customer-identifying in logs by default.>

## Accepted risks

| Risk | Why accepted | Owner | Expires |
|---|---|---|---|
| | | | |
