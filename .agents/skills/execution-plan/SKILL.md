---
name: execution-plan
description: Create a concrete implementation plan before coding, especially for multi-file changes, ambiguous tasks, PRD-linked tasks, refactors, debugging, or anything that needs checkpoints and goal-alignment review.
---

# Execution Plan Skill

Use this skill before editing files for any non-trivial task.

Do not implement until the plan is written.

## Step 1: Restate the task as an execution contract

```md
# Execution Contract
- Task ID:
- Original product goal:
- Linked requirements / stories / acceptance criteria:
- Target behavior:
- Non-goals:
- Hard constraints:
- Done means:
```

## Step 2: Identify what to read

Do not scan the whole repository unless necessary.

```md
## Context Reading Plan
| Priority | File / directory | Why read it | What decision it informs |
|---|---|---|---|
```

## Step 3: Define the change boundary

```md
## Change Boundary
| Area | Will change? | Reason | Risk |
|---|---|---|---|
| UI | Yes / No |  |  |
| State | Yes / No |  |  |
| API | Yes / No |  |  |
| Data model | Yes / No |  |  |
| Tests | Yes / No |  |  |
| Docs | Yes / No |  |  |
```

## Step 4: Make a phased plan

```md
## Phased Plan
| Phase | Action | Expected output | Check after phase |
|---|---|---|---|
| 1 | Inspect files | Current behavior understood | No assumptions hidden |
| 2 | Implement minimal change | Behavior changed | Matches task scope |
| 3 | Add or update checks | Verification exists | AC covered |
| 4 | Self-review | Risk found | PR-ready notes |
```

## Step 5: Add goal-alignment checkpoints

After every phase, write:

```md
### Phase <n> Alignment Check
- Original target:
- What changed in this phase:
- Does it still match? Match / Partial / Off-track
- Evidence:
- Correction before continuing:
```

## Step 6: Verification plan

```md
## Verification Plan
| Requirement / AC | Verification method | Command / steps | Evidence expected |
|---|---|---|---|
```

## Step 7: Stop conditions

Stop and ask or report if:

- The required file does not exist.
- The repository structure contradicts the task.
- Implementation would require adding a new feature not in scope.
- A dependency, API key, environment, or data source is missing.
- The task cannot satisfy the acceptance criteria as written.

## Final output before coding

End the plan with:

```md
## Ready to Implement?
- Status: Ready / Blocked / Needs clarification
- Reason:
- First file to inspect:
- First implementation step:
```
