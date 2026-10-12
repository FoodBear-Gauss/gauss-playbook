# Definition of Done

What "done" means for an issue in any FoodBear-Gauss repository, and when the
issue closes. This is the org-wide minimum. An adopting repository adopts it as
a floor and may add to it, never subtract. Its local additions live in its own
docs (usually an ADR) and link here instead of restating this page.

## The rule in one paragraph

An issue is done when the pull request that completes it is merged into the
default branch (`main`), the shared checklist below is met, and every "Done
when" box on the issue is proven in that PR. The PR body carries a closing
keyword, so GitHub closes the issue on merge. This holds whether or not a
person reviewed the PR: who reviews and who merges is the repository's merge
policy, not part of this definition. Anyone may reopen the issue with evidence.

## Two lists, two jobs

| | Definition of Done | Acceptance criteria ("Done when") |
|---|---|---|
| Applies to | Every issue in the repository | One issue |
| Written by | The playbook, plus the adopting repository's additions | Whoever writes the issue, before work starts |
| Answers | "Is this change of releasable quality?" | "Does this change do what this issue asked?" |
| Lives in | This page and the repository's ADR | The issue body, copied into the PR |

Done means both lists are met. This follows the Scrum Guide (the Definition of
Done is the quality bar for all work, and an organisation's standard is the
minimum for every team) and the common practice that acceptance criteria are
specific to one item.

## The shared checklist

An issue is done when all of these are true:

1. **Merged into the default branch** through a PR that names the issue with a
   closing keyword. GitHub closes the issue on merge.
2. **Merged under the repository's merge policy.** The merge policy (review
   passes by risk tier, who may merge) is set in
   [`delivery.md`](delivery.md#review) and the repository's `AGENTS.md`. This
   page does not decide who merges.
3. **Required checks are green** on the PR, including the acceptance-criteria
   check if the repository has one.
4. **Every "Done when" box is ticked, and each tick has proof in the PR body:**
   a test name, a command with its output, or a file and line that was re-read.
5. **Behaviour is tested.** New or changed behaviour has automated tests.
   Existing tests still pass. No test was weakened or skipped to get green.
6. **Docs are current** under the repository's rules: README, changelog,
   devlog, runbook and any affected ADR are added or updated where behaviour,
   configuration or interfaces changed.
7. **Nothing unfinished reaches users.** Incomplete or unreleased behaviour is
   behind a flag or switched off, and the switched-off path is tested.
8. **Nothing left unsaid.** No secrets, no new lint or type errors, and no known
   regression left without its own issue.
9. **Every person-only follow-up exists** as its own issue with a named owner,
   linked from the PR (see [Acceptance criteria](#acceptance-criteria)).

"Merged" is the done point because no repository on the team has an automated
deploy step yet. DORA counts work as complete only once it is deployed. When a
repository gains a deploy step, it adds "deployed" to its local checklist.

## Acceptance criteria

The "Done when" boxes on an issue are its acceptance criteria.

1. Each issue has 1 to 7 boxes, written before work starts.
2. **Each box is provable inside a PR:** a test, a command with its expected
   output, or a file and line someone can re-read. "Looks good" and "reviewed
   by X" are not boxes.
3. **No box needs a specific person or a post-merge event.** A step only a
   person can do (a second engineer's re-run, the owner's sign-off, someone's
   read) is not acceptance criteria. It goes to one of two places:
   - a **gate before merge**, when the merge must wait for it. The gate is part
     of the merge policy (for example a required reviewer), not a "Done when"
     box;
   - a **follow-up issue**, when it can happen after merge. The follow-up has a
     named assignee, the label `needs-human` if the repository uses labels, and
     a `Refs #N` back-link. The original issue still closes on merge.
4. The PR body copies the boxes, ticks them, and puts the proof next to each one.
5. Changing the boxes during the work means editing the issue, with a comment
   that says why, before the PR merges.

A repository should enforce rules 2 and 4 in CI: a check that fails a PR whose
body closes an issue but leaves a "Done when" box unticked, or ticked without
proof. PRs that only reference an issue are exempt. A rule that lives only in
people's memory gets skipped.

Example PR body:

```markdown
Closes #123

## Done when
- [x] Dry run lists the three changed items. Proof: `make dry-run STORE=test-1`, output below.
- [x] A failed login stops the run with a reason. Proof: `test_login_expired_stops_run`.

## Follow-ups
- #124 Second engineer re-runs the dry run on their machine (owner: <name>). Refs #123.
```

## Closing

- **Closing keywords.** Put `Closes #N` in the PR body for each issue the PR
  completes. GitHub also accepts close, closed, fix, fixes, fixed, resolve,
  resolves and resolved, in any case. Use `Refs #N` for partial work; it links
  without closing.
- **Only merges into the default branch close issues.** GitHub processes
  closing keywords only when the PR targets the default branch.
- **Integration branches.** A PR into an integration branch says `Part of #N`
  and does not close anything. The PR that merges the integration branch into
  `main` carries the closing keywords for every issue it completes.
- **Keywords in commit messages** also close issues on merge, but the PR is
  then not shown as linked. Put them in the PR body instead.
- **No hand-closing as completed.** An issue is never closed by hand as
  completed without a merged PR. Closing as **not planned** or as a
  **duplicate** is allowed with a one-line reason.
- To stop a PR closing an issue, edit the keyword out of the PR body before
  merge.

## Reopening

Done is reversible. Anyone, person or agent, may reopen an issue with a comment
that gives the evidence: a failing command and its output, or a "Done when" box
the merged PR did not prove. A reopened issue goes back to the backlog and is
fixed by a new PR that closes it again. Reopening is not a judgement on whoever
merged.

## Status words

Use the same words in every repository and every build plan:

| Status | Means |
|---|---|
| Open | Written, not started |
| In progress | Someone is working on it on a branch |
| In review | A PR that closes it is open |
| Done | Closed by the merge of that PR |
| Reopened | Reopened with evidence; back in the backlog |
| Not planned | Closed without a PR, with a one-line reason |

## Definition of Ready

Optional, and not part of the Scrum Guide. An issue is ready to start when it
has an outcome, a risk tier, its "Done when" boxes, and any person-only steps
already split into gates or follow-ups. Treat this as issue-template hygiene,
not as a gate.

## What closing does not do

- **It does not set the merge policy.** Today's rules stand:
  [`delivery.md`](delivery.md#review) says a human who is not the author
  merges, and AI review is an input, not approval. An adopting repository's
  own merge rule (for example "the owner merges") also stands. Allowing a
  defined low-risk class to merge without human review is a merge-policy
  decision for each repository's owner, recorded in that repository.
- **It does not approve a live write.** A closed issue is not a go. The
  approval boundary in [`risk-and-approval.md`](risk-and-approval.md#3-the-approval-boundary-for-live-writes)
  still applies to every live write on an R3 workflow, before and after merge.

## Sources

- Scrum Guide 2020, "Commitment: Definition of Done":
  https://scrumguides.org/scrum-guide.html
- Agile Alliance glossary, "Definition of Done":
  https://www.agilealliance.org/glossary/definition-of-done/
- Scrum.org, "Definition of Done vs Acceptance Criteria":
  https://www.scrum.org/resources/blog/definition-done-vs-acceptance-criteria-whats-difference
- GitHub Docs, "Linking a pull request to an issue" (closing keywords, default
  branch only):
  https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue
- GitHub Docs, "Closing an issue" (completed or not planned):
  https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/closing-an-issue
- GitHub Docs, "About protected branches" (required reviews and checks are
  merge settings):
  https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- DORA, "Trunk-based development" and "Working in small batches":
  https://dora.dev/capabilities/trunk-based-development/ and
  https://dora.dev/capabilities/working-in-small-batches/
- Google Engineering Practices, "The Standard of Code Review":
  https://google.github.io/eng-practices/review/reviewer/standard.html
- Trunk Based Development, "Feature Flags":
  https://trunkbaseddevelopment.com/feature-flags/

The follow-up-issue-with-an-owner convention is a team convention that follows
from these sources. No source above states it directly.
