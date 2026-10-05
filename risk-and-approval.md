# Risk Tiers and Approval

Scale the controls to the consequence, so low-risk work stays light and
high-risk work is never casual.

## 1. Classify the whole workflow

Classify what the complete workflow can do, not just the piece of code you are
touching. Use the highest tier that applies.

| Tier | Typical scope | Minimum posture |
|---|---|---|
| **R0: Exploration** | Local, disposable, synthetic or public data, no external action | Scope note, no secrets, honest limitations |
| **R1: Assisted internal** | Known users, reversible output, a person decides | Owner, baseline tests, access control, human review |
| **R2: Material workflow** | Customer-facing, sensitive data, a business process, or bounded tools that write | Threat model, representative tests, least privilege, staged release, rollback, monitoring |
| **R3: High consequence** | Money, prices, hard-to-reverse effects, or one failure reaching many stores | All of R2, plus an explicit human authority boundary, independent review, an exercised restore and rollback, and a way to stop everything |

### Escalate at least one tier when the workflow

- writes, publishes, deletes or changes prices on an external platform;
- uses confidential or personal data;
- reads untrusted content that could steer a tool;
- runs without timely human review;
- can affect many stores or users from one failure;
- has no reliable restore or rollback.

A label like "internal" or "just a script" does not lower the tier.

**Pushes that change menus, prices or promotions on delivery platforms are R3.**

### Evidence by tier

| Evidence | R0 | R1 | R2 | R3 |
|---|:---:|:---:|:---:|:---:|
| Outcome, scope, assumptions | MUST | MUST | MUST | MUST |
| Predeclared pass criteria | SHOULD | MUST | MUST | MUST |
| Threat model | Optional | SHOULD | MUST | MUST |
| Data-handling note | If data needs it | If data needs it | MUST | MUST |
| Human authority boundary | If an action exists | MUST | MUST | MUST |
| Staged release and rollback | Optional | SHOULD | MUST | MUST |
| Monitoring after release | No | If persistent | MUST | MUST |
| Independent review | No | Optional | SHOULD | MUST |
| Restore and rollback exercised | No | Optional | SHOULD | MUST |

Record the tier, its reason, its owner and its review date in the project PRD.
Reclassify when users, data, autonomy, integrations or exposure change. A good
pilot does not grandfather weaker controls into production.

## 2. Exceptions

A MUST can be missed only through a recorded exception. Each exception names the
control, the reason, what it affects, the compensating controls, how it is
watched, the remediation, an owner, an approver and an **expiry date**. An
expired exception is closed, renewed or replaced, never left to run on.

## 3. The approval boundary for live writes

Every consequential action moves through four states:

```text
Observe -> Propose (dry run) -> Approve (go + arm) -> Execute -> Re-read
```

| State | What happens |
|---|---|
| **Observe** | Read only the data needed, and keep where it came from. |
| **Propose** | A **dry run** shows exactly what will be written, where, and what it replaces. Nothing is written. Dry run is the default for every push. |
| **Approve** | The accountable owner gives a **go** for that exact action, or for one agreed batch of like actions on the same store in one sitting. A person then **arms** the push. The go and the arming are recorded. |
| **Execute** | Code revalidates the target, the payload, the store and freshness before writing. A changed payload goes back to Propose. |
| **Re-read** | Read the platform back and compare it with the plan. A mismatch is reported as a mismatch, never as success. |

Rules that hold in every case:

- An agent never gives a go, never arms, and never treats another agent's output
  as approval.
- Live tests run only on stores the owner has named as **test stores**, and each
  has a **restore** that puts the store back.
- A go expires. If the session ends or the payload changes, ask again.
- A failed or partial write is never retried automatically unless it is proven
  idempotent.
- There is always a way to **stop all runs**, written in the runbook and tried
  at least once.
