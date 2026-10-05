# PRD: <Product or Capability>

- **Status:** Draft
- **Owner:** <role/team>
- **Date:** <YYYY-MM-DD>
- **Risk tier:** <R0/R1/R2/R3 with rationale>
- **Decision deadline:** <date or trigger>
- **Intent:** <link to the intent.md this grew from, if there was one>

Use this when a change is large enough to need scope, governance, evaluation, and
release sections. For anything smaller, [`intent.md`](intent.md) is the right
artifact: it covers the same first four fields and stops there.

## Problem and outcome

<Who has what problem, why it matters, and the measurable outcome.>

## Users and affected people

<Primary users, indirect stakeholders, access needs, and possible harms.>

## Scope

### In scope

- <capability>

### Out of scope

- <boundary>

## Success and guardrails

| Measure | Baseline | Target/threshold | Window | Owner |
|---|---:|---:|---|---|
| User outcome | | | | |
| Quality | | | | |
| Safety/privacy | | | | |
| Latency/reliability | | | | |
| Resource/cost | | | | |

## Why this approach

<Why this design, and what simpler alternative was considered. If a model or
agent is part of the workflow, say why probabilistic behavior is acceptable here
and what deterministic control backs it up.>

## Workflow and system design

<User journey, components, data flow, trust boundaries, models, retrieval,
tools, external systems, and human decisions.>

## Data and governance

<Sources, provenance, classification, allowed purpose, access, retention,
deletion, providers/regions, and review obligations.>

## Evaluation and acceptance

<Dataset, segments, graders, thresholds, critical cases, software tests,
security/adversarial checks, and owner of the promotion decision.>

## Release and operations

<Environments, staged rollout, monitoring, support, rollback/shutdown, incident
path, and retirement.>

## Risks, assumptions, and open decisions

| Item | Type | Impact | Owner | Resolution/date |
|---|---|---|---|---|
| | Risk/assumption/decision | | | |

## Definition of done

- <observable end-to-end evidence>

