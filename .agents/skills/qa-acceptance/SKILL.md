---
name: qa-acceptance
description: Product QA and acceptance testing for a completed feature, PRD milestone, demo, or implementation. Use before saying a task is done or before preparing a pull request.
---

# QA Acceptance Skill

Use this skill to verify whether the current work satisfies the product requirement, not merely whether the code compiles.

## Step 1: Identify what is being accepted

```md
## Acceptance Target
- Feature / task ID:
- Original product goal:
- Requirement IDs:
- Acceptance criteria IDs:
- Files / screens / flows involved:
```

## Step 2: Build the QA matrix

```md
## QA Matrix
| Requirement / AC | Test scenario | Steps | Expected result | Actual result | Status |
|---|---|---|---|---|---|
| AC-001 | Happy path |  |  |  | Pass / Fail / Not tested |
```

## Step 3: Cover required states

For user-facing work, verify:

```md
## UX State Coverage
| State | Expected behavior | Covered? | Evidence / gap |
|---|---|---|---|
| Default |  | Yes / No |  |
| Empty |  | Yes / No |  |
| Loading |  | Yes / No |  |
| Success |  | Yes / No |  |
| Error |  | Yes / No |  |
| Invalid input |  | Yes / No |  |
| Mobile / responsive |  | Yes / No / N/A |  |
```

## Step 4: Check edge cases

Common edge cases:

- Missing input.
- Invalid input.
- Slow network or failed request.
- Empty dataset.
- Duplicate data.
- Permission denied.
- User cancels midway.
- Refresh or reload.
- Long text or unusually large data.
- AI returns malformed output if AI is involved.

## Step 5: Verification evidence

```md
## Verification Evidence
| Check type | Command / steps | Result | Notes |
|---|---|---|---|
| Unit test |  |  |  |
| Integration test |  |  |  |
| Manual test |  |  |  |
| Screenshot / recording |  |  |  |
```

## Step 6: Acceptance verdict

```md
## Acceptance Verdict
- Status: Accepted / Conditionally accepted / Rejected
- Blocking issues:
- Non-blocking issues:
- Required fixes before PR:
- Follow-up tasks:

## Goal Alignment Check
- Original target deliverable:
- Current tested behavior:
- Match status: Match / Partial / Off-track
- Missing or risky items:
- Next correction:
```
