---
name: pr-review
description: Review a pull request from both PM and engineering perspectives. Use for PR-style review, uncommitted diff review, or pre-merge checks against original product goals, PRD requirements, acceptance criteria, and implementation risk.
---

# PR Review Skill

Use this skill to review code changes before merge.

## Review principle

A PR is acceptable only if it is technically sound and product-correct.

Do not approve a PR that compiles but misses the original goal.

## Step 1: Reconstruct review context

```md
## Review Context
- PR title:
- Original request / issue:
- Target deliverable:
- Linked PRD / task IDs:
- Claimed scope:
- Files changed:
```

If PRD or task IDs are missing, review the PR more strictly and flag missing traceability.

## Step 2: Product-goal review

```md
## Product Goal Review
| Question | Answer | Evidence | Concern |
|---|---|---|---|
| Does the PR solve the stated user problem? |  |  |  |
| Does it match the target deliverable? |  |  |  |
| Does it preserve non-goals? |  |  |  |
| Does it add scope creep? |  |  |  |
```

## Step 3: Acceptance criteria review

```md
## Acceptance Criteria Coverage
| AC ID | Expected behavior | Evidence in PR | Status | Required fix |
|---|---|---|---|---|
```

Classify status as:

- Covered.
- Partially covered.
- Not covered.
- Cannot verify.

## Step 4: Code and architecture review

Check:

- Correctness.
- Simplicity.
- Compatibility with existing patterns.
- State management.
- Data contracts.
- Error handling.
- Security and privacy.
- Performance where relevant.
- Tests and verification.
- Maintainability.

## Step 5: UX and demo review

For UI/demo features, check:

- First impression.
- Primary flow clarity.
- Empty/loading/error/success states.
- Mobile or screen-size behavior.
- Copy clarity.
- Demo stability.

## Step 6: Write findings by severity

```md
## Findings
### Blocking
| File / area | Issue | Why it blocks | Required fix |
|---|---|---|---|

### Non-blocking
| File / area | Suggestion | Reason |
|---|---|---|

### Questions
| Question | Why it matters |
|---|---|
```

## Step 7: Final verdict

```md
## PR Review Verdict
- Verdict: Approve / Request changes / Comment only
- Main reason:
- Merge readiness:
- Required next action:

## Goal Alignment Check
- Original target deliverable:
- What the PR actually changes:
- Match status: Match / Partial / Off-track
- Missing or risky items:
- Next correction:
```
