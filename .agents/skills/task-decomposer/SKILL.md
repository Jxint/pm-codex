---
name: task-decomposer
description: Decompose a PRD, feature spec, roadmap item, or rough product requirement into detailed, ordered, atomic implementation tasks with requirement traceability, acceptance criteria, dependencies, and review checkpoints.
---

# Task Decomposer Skill

Use this skill after `pm-intake` or `prd-writer`, before implementation.

The goal is to create tasks that Codex can execute accurately without reading the entire PRD every time.

## Core rule

Every task must map back to a product goal, requirement ID, user story, or acceptance criterion.

If a task cannot be traced back, classify it as one of:

- Support task: needed for setup, testing, infrastructure, or migration.
- Scope creep: useful but not part of the current target.
- Unknown: needs PM decision.

## Step 1: Build the requirement inventory

```md
## Requirement Inventory
| Req ID | User story | Acceptance criteria | Priority | Notes |
|---|---|---|---|---|
```

## Step 2: Split by product outcome first

Use this hierarchy:

```text
Initiative / Product Goal
└─ Epic: large user outcome
   └─ Feature: usable product capability
      └─ User Story: user goal
         └─ Task: one implementation unit
            └─ Subtask: small technical action if needed
```

Do not split only by technical layer unless the requirement is already clear. Product outcome comes first; technical layer comes second.

## Step 3: Create atomic tasks

A task is atomic when:

- It has one primary output.
- It can be completed in one focused Codex session.
- It has a clear start and end.
- It has independent verification.
- It does not bundle unrelated UI, backend, data, and docs unless they are inseparable.

Use this test:

```text
Can this task be reviewed and reverted without affecting unrelated requirements?
```

If no, split it.

## Step 4: Use the task card template

```md
## TASK-001: <verb + object + outcome>

### Product link
- Product goal:
- Requirement IDs:
- User story IDs:
- Acceptance criteria IDs:

### Objective
<One concrete outcome.>

### Scope
| In scope | Out of scope |
|---|---|

### Expected behavior
- Before:
- After:

### Implementation notes
- Relevant files / modules to inspect:
- Likely files to change:
- Data / API impact:
- UI state impact:

### Dependencies
- Depends on:
- Blocks:

### Acceptance criteria for this task
- [ ] AC-...
- [ ] Manual check:
- [ ] Error case:

### Verification plan
- Automated checks:
- Manual checks:
- Screenshot / demo evidence if UI:

### Risk
- Main risk:
- Mitigation:

### Complexity
- Size: XS / S / M / L
- Reason:

### Codex prompt to execute this task
```text
Use $execution-plan for TASK-001. Implement only the behavior described in TASK-001. Do not expand scope. After each step, run a goal-alignment check against REQ-... and AC-....
```
```

## Step 5: Sequence tasks

Use this ordering:

1. Foundation and project setup.
2. Data model and contracts.
3. Core happy path.
4. Edge cases and error states.
5. UI polish necessary for comprehension.
6. Persistence / integration.
7. Tests and QA.
8. PR and release documentation.

## Step 6: Build the execution backlog

```md
# Execution Backlog

## Milestone 1: <name>
| Task ID | Title | Priority | Size | Depends on | Requirement IDs | Exit criteria |
|---|---|---|---|---|---|---|

## Milestone 2: <name>
...
```

## Step 7: Definition of Ready audit

For each P0 task:

```md
## Definition of Ready Audit
| Task ID | Clear goal | AC linked | Files known | Dependencies known | Verification known | Ready? |
|---|---|---|---|---|---|---|
```

Tasks marked not ready must not be implemented until corrected.

## Step 8: Goal Alignment Check

```md
## Goal Alignment Check
- Original target deliverable:
- Task backlog produced:
- Do all P0 requirements have tasks? Yes / No
- Are any tasks scope creep? Yes / No
- Missing or risky items:
- Next correction:
```
