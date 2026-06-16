---
name: goal-alignment-review
description: Audit whether a PRD, task list, implementation, PR, document, or design still matches the original product goal and target deliverable. Use after each major step or when scope may have drifted.
---

# Goal Alignment Review Skill

Use this skill as a checkpoint after intake, PRD, task decomposition, implementation, QA, PR preparation, or review.

## Step 1: Reconstruct the original target

```md
## Original Target
- User request:
- Target deliverable:
- Target user:
- Product goal:
- Required format / platform:
- Hard constraints:
- Non-goals:
```

If any item is missing, infer cautiously and mark as assumption.

## Step 2: Summarize the current output

```md
## Current Output
- Artifact reviewed:
- Main content / change:
- Claimed completion:
- Evidence provided:
```

## Step 3: Compare against the target

```md
## Alignment Matrix
| Target element | Present in current output? | Evidence | Gap | Correction |
|---|---|---|---|---|
| Target user | Yes / Partial / No |  |  |  |
| Core problem | Yes / Partial / No |  |  |  |
| Core value | Yes / Partial / No |  |  |  |
| MVP scope | Yes / Partial / No |  |  |  |
| Non-goals respected | Yes / Partial / No |  |  |  |
| Acceptance criteria | Yes / Partial / No |  |  |  |
| Verification | Yes / Partial / No |  |  |  |
```

## Step 4: Detect scope drift

Classify each questionable element:

- Required: directly needed for the target deliverable.
- Support: needed to enable the target deliverable.
- Optional: useful but not needed now.
- Scope creep: not requested and increases complexity.
- Contradiction: conflicts with original constraints.

```md
## Scope Drift Check
| Item | Classification | Keep / Remove / Defer | Reason |
|---|---|---|---|
```

## Step 5: Decide correction

```md
## Alignment Verdict
- Status: Match / Partial / Off-track
- Blocking gaps:
- Non-blocking gaps:
- Required correction:
- Next skill to use:
```

## Rules

- Be strict about the target deliverable.
- Do not reward extra features if they reduce clarity or delivery confidence.
- A polished output that misses the original goal is off-track.
- A simple output that satisfies P0 requirements can be marked match.
