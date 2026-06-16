---
name: requirements-traceability
description: Build or audit a traceability matrix linking original goal, requirements, user stories, acceptance criteria, tasks, files, tests, and PRs. Use to prove nothing important was missed.
---

# Requirements Traceability Skill

Use this skill whenever accuracy matters more than speed: before task decomposition, before PR, during QA, or when the user asks whether everything has been covered.

## Purpose

Trace every implemented or planned item back to the original goal.

A requirement without a task will not be built. A task without a requirement may be scope creep.

## Step 1: Establish trace levels

```text
Goal Lock → Requirement → User Story → Acceptance Criterion → Task → File / Module → Test / Check → PR
```

## Step 2: Build the matrix

```md
## Traceability Matrix
| Goal | Req ID | User Story | AC ID | Task ID | Files / modules | Test / check | PR | Status |
|---|---|---|---|---|---|---|---|---|
```

Status values:

- Planned.
- Ready.
- In progress.
- Implemented.
- Verified.
- Missing task.
- Missing AC.
- Scope creep.
- Blocked.

## Step 3: Audit coverage

```md
## Coverage Audit
| Check | Result | Evidence | Required action |
|---|---|---|---|
| Every P0 requirement has at least one AC | Pass / Fail |  |  |
| Every P0 AC has at least one task | Pass / Fail |  |  |
| Every implementation task maps to a requirement | Pass / Fail |  |  |
| Every completed task has verification | Pass / Fail |  |  |
| Every PR links to tasks / requirements | Pass / Fail |  |  |
```

## Step 4: Identify orphan items

```md
## Orphan / Drift Items
| Item | Type | Why it is orphaned | Decision |
|---|---|---|---|
```

Decision values:

- Link to existing requirement.
- Create new requirement.
- Defer.
- Remove as scope creep.
- Needs PM decision.

## Step 5: Produce next actions

```md
## Required Corrections
| Priority | Correction | Owner / next skill | Why |
|---|---|---|---|
```

## Goal Alignment Check
- Original target deliverable:
- Traceability output produced:
- Match status: Match / Partial / Off-track
- Missing or risky items:
- Next correction:
