# Principles

How the Gauss team thinks about engineering work, for people and agents alike.
These are defaults, not slogans. When a different choice serves the outcome
better, record the trade-off in an ADR.

## 1. Start with the outcome and its consequence

Name the user, the action, what failure costs and how success is measured before
choosing a tool, model or framework.

## 2. Build the smallest honest end-to-end slice

One real workflow, through real boundaries, with evidence, beats a broad scaffold
whose critical path has never run. Prototypes are either thrown away or promoted
on purpose.

## 3. Evidence, not claims

A check passes when its evidence is attached. "It looked fine", a green message,
or an exit code is not evidence that an external platform changed. Read it back.

## 4. Every failure says why

A failed run that stores no reason is a second failure. Errors are specific,
recorded and visible to the person who has to act on them.

## 5. Silent success is the most expensive failure

A run that reports success but did not do the thing is worse than a crash.
Design checks that catch a mismatch between what we meant to write and what the
platform now shows.

## 6. Design for failure and recovery

Networks hang, logins expire, platforms rate-limit and APIs change. Every wait
has a timeout, every retry is bounded, every write has a restore, and every
release has a rollback that someone has tried.

## 7. Authority proportional to confidence

Give a tool or agent only the data, stores, scope and time it needs. A person
approves consequential or hard-to-reverse actions. Prompts guide; code enforces.

## 8. Move enforcement into code

A rule that lives only in a document gets skipped when people are busy. If a rule
matters and is cheap to check, make it a test, a CI guard or a hook.

## 9. Generated work is engineering work

Code, tests and documents written by an agent meet the same review, security and
verification bar as code written by a person. Speed changes the workflow, not
who is accountable.

## 10. Turn evidence into learning

Incidents, near misses, review findings and repeated agent mistakes should change
a test, template or rule. Learning left in a chat transcript is lost.

## Decision posture

We prefer:

- reversible before irreversible;
- observable before opaque;
- explicit before magical;
- simple before distributed;
- least privilege before broad authority;
- the owner's house rules before our general habits.

## What we reject

- A demo as release evidence.
- Tests weakened to accept a preferred implementation.
- Agent instructions as the only safety boundary.
- Live writes to customer stores during testing.
- Documentation that states an aspiration as a fact.
