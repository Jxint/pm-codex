---
name: change-control
description: Manage scope changes after a goal, PRD, task breakdown, or implementation plan already exists. Use when new requirements appear, priorities change, or the user asks to modify the original target.
---

# Change Control Skill

Use this skill when the target changes after work has started.

Do not silently merge new requirements into the existing plan.

## Step 1: Capture the change request

```md
## Change Request
- CR-ID: CR-001
- Requested change:
- Source:
- Date:
- Related Goal Lock:
- Related REQ / TASK / PR:
```

## Step 2: Classify the change

| Type | Definition |
|---|---|
| Clarification | Makes existing requirement more precise |
| Scope addition | Adds new behavior |
| Scope removal | Removes planned behavior |
| Constraint change | Changes platform, deadline, tech, quality, or data constraints |
| Priority change | Changes sequencing or importance |
| Correction | Fixes wrong earlier assumption |

## Step 3: Impact analysis

```md
## Impact Analysis
| Area | Impact | Required update |
|---|---|---|
| Goal Lock |  |  |
| PRD |  |  |
| Acceptance criteria |  |  |
| Task breakdown |  |  |
| Execution plan |  |  |
| Code already changed |  |  |
| QA / PR |  |  |
| Deadline / complexity |  |  |
```

## Step 4: Decision options

```md
## Decision Options
| Option | What changes | Pros | Cons | Recommendation |
|---|---|---|---|---|
| A. Include now |  |  |  |  |
| B. Defer to follow-up |  |  |  |  |
| C. Reject as scope creep |  |  |  |  |
```

## Step 5: Update affected artifacts only

Do not rewrite all docs if only one task changes.

```md
## Minimal Update Plan
| Artifact | Update needed? | Exact change |
|---|---|---|
```

## Step 6: Goal Alignment Check

```md
## Goal Alignment Check
- Original target deliverable:
- Change requested:
- Match status: Match / Partial / Off-track
- Recommended decision:
- Next correction:
```
