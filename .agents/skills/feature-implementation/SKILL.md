---
name: feature-implementation
description: Implement a single PRD-linked feature or task after task decomposition and execution planning. Use for scoped coding work with acceptance criteria and required verification.
---

# Feature Implementation Skill

Use this skill only after the task is clear enough to build.

## Mandatory behavior

- Implement only the requested task.
- Do not silently add adjacent features.
- Preserve existing behavior unless the task explicitly changes it.
- Keep changes reviewable.
- After each phase, check alignment against the original product goal.

## Step 1: Confirm task readiness

```md
## Task Readiness
- Task ID:
- Product goal:
- Requirements:
- Acceptance criteria:
- Files to inspect:
- Verification method:
- Ready? Yes / No
```

If not ready, use `$task-decomposer` or `$execution-plan` first.

## Step 2: Inspect before editing

Read the smallest relevant set of files.

Output:

```md
## Current Behavior Summary
- Current user/system behavior:
- Existing relevant patterns:
- Files that matter:
- Risks found before editing:
```

## Step 3: Implement in narrow phases

Use phases like:

1. Data contract / types.
2. Core logic.
3. UI or integration.
4. Error states.
5. Tests / verification.
6. Documentation / PR notes.

After each phase:

```md
## Phase Alignment Check
- Phase completed:
- Requirement IDs affected:
- Evidence:
- Still aligned with original goal? Match / Partial / Off-track
- Next step:
```

## Step 4: Handle UX states

For user-facing features, check:

- Default state.
- Empty state.
- Loading state.
- Error state.
- Success state.
- Disabled / invalid input state.
- Mobile or responsive state if relevant.

## Step 5: Verification

Run the relevant checks available in the repo.

If commands are unknown, inspect package/config files first.

Verification output:

```md
## Verification Evidence
| Check | Command / steps | Result | Notes |
|---|---|---|---|
```

## Step 6: Final implementation summary

```md
## Implementation Summary
- Task ID:
- Requirements covered:
- Files changed:
- Behavior changed:
- Tests/checks run:
- Manual verification:
- Known limitations:
- Follow-up tasks:

## Goal Alignment Check
- Original target deliverable:
- Current implementation:
- Match status: Match / Partial / Off-track
- Missing or risky items:
- PR-ready? Yes / No
```
