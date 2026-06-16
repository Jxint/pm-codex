---
name: task-decomposer
description: Decompose a PRD, feature spec, roadmap item, or rough product requirement into detailed, ordered, atomic implementation tasks with requirement traceability, acceptance criteria, dependencies, file hints, verification, PR boundaries, and checkpoint reviews.
---

# Task Decomposer Skill

Use this skill after `pm-intake`, `prd-writer`, or `requirements-traceability`, before implementation.

The goal is to create tasks that Codex can execute accurately without reading the entire PRD every time.

## Core rules

1. Every task must map back to a Goal Lock, requirement ID, user story, or acceptance criterion.
2. Split by product outcome first, then by technical layer.
3. Each task must be small enough for one focused Codex session.
4. Each task must have its own acceptance criteria and verification method.
5. Each task must define what Codex must not touch.
6. Do not repeat the full PRD in every task. Use IDs and a compact task packet.

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

## Step 2: Build the product capability map

Do this before writing tasks. It prevents tasks from becoming random file edits.

```md
## Capability Map
| Capability ID | User outcome | Related requirements | Must work before demo? | Notes |
|---|---|---|---|---|
| CAP-001 |  | REQ-001 | Yes / No |  |
```

## Step 3: Split by product outcome first

Use this hierarchy:

```text
Goal Lock
└─ Capability: user-visible or system-visible outcome
   └─ Feature: usable capability slice
      └─ User Story: user goal
         └─ Task: one implementation unit
            └─ Subtask: one technical action if needed
```

Do not split only by technical layer unless the requirement is already clear. Product outcome comes first; technical layer comes second.

## Step 4: Apply the atomicity test

A task is atomic when:

- It has one primary output.
- It can be completed in one focused Codex session.
- It has a clear start and end.
- It has independent verification.
- It does not bundle unrelated UI, backend, data, docs, and tests unless they are inseparable.
- It can be reviewed and reverted without affecting unrelated requirements.

If any answer below is "no", split the task further:

```md
## Atomicity Test
| Question | Answer | Split needed? |
|---|---|---|
| Does it produce one outcome? | Yes / No |  |
| Can it be verified independently? | Yes / No |  |
| Can it fit in one Codex session? | Yes / No |  |
| Does it avoid unrelated files? | Yes / No |  |
| Can it be reverted safely? | Yes / No |  |
```

## Step 5: Use the detailed task card

```md
## TASK-001: <verb + object + measurable outcome>

### 1. Product link
- Goal Lock:
- Capability ID:
- Requirement IDs:
- User story IDs:
- Acceptance criteria IDs:

### 2. Objective
<One concrete outcome.>

### 3. User/system behavior
- Actor:
- Trigger:
- Before behavior:
- After behavior:
- Success state:
- Failure state:

### 4. Scope boundary
| In scope | Out of scope | Do not touch |
|---|---|---|

### 5. Implementation packet
- Relevant files / modules to inspect:
- Likely files to change:
- Data / API impact:
- UI state impact:
- Config / env impact:
- Migration needed? Yes / No

### 6. Dependencies
- Depends on:
- Blocks:
- Can run in parallel with:

### 7. Acceptance criteria for this task
- [ ] AC-...
- [ ] Happy path:
- [ ] Edge case:
- [ ] Error case:
- [ ] Regression check:

### 8. Verification plan
| Check | Command / manual steps | Expected evidence |
|---|---|---|
| Unit / logic |  |  |
| Integration |  |  |
| UI / manual |  |  |
| Build / lint / type |  |  |

### 9. Risk
| Risk | Impact | Mitigation | Stop condition |
|---|---|---|---|

### 10. Complexity
- Size: XS / S / M / L
- Reason:
- If L, split into:

### 11. PR boundary
- Should this be its own PR? Yes / No
- PR title draft:
- Reviewer focus:

### 12. Minimal Codex prompt
```text
Use $execution-plan for TASK-001. Goal Lock GL-001. Implement only TASK-001. Relevant IDs: REQ-..., US-..., AC-.... Read only <files>. Do not repeat the full PRD. Do not touch <out-of-scope>. After each phase, run a goal-alignment check against GL-001.
```
```

## Step 6: Sequence tasks

Use this ordering:

1. Foundation and project setup.
2. Data model and contracts.
3. Core happy path.
4. Edge cases and error states.
5. UI polish necessary for comprehension.
6. Persistence / integration.
7. Tests and QA.
8. PR and release documentation.

## Step 7: Build the execution backlog

```md
# Execution Backlog

## Milestone 1: <name>
| Task ID | Title | Priority | Size | Depends on | Requirement IDs | Exit criteria | PR boundary |
|---|---|---|---|---|---|---|---|

## Milestone 2: <name>
...
```

## Step 8: Definition of Ready audit

For each P0 task:

```md
## Definition of Ready Audit
| Task ID | Clear goal | AC linked | Files known | Dependencies known | Verification known | Scope boundary clear | Ready? |
|---|---|---|---|---|---|---|---|
```

Tasks marked not ready must not be implemented until corrected.

## Step 9: Token-saving execution packets

After the backlog, create one compact packet per immediate task, not for every future task.

```md
## Next Task Packet
- Task ID:
- Goal Lock:
- Relevant IDs:
- Files to inspect:
- Do not touch:
- Acceptance checks:
- Stop if:
```

## Step 10: Goal Alignment Check

```md
## Goal Alignment Check
- Original target deliverable:
- Task backlog produced:
- Do all P0 requirements have tasks? Yes / No
- Are any tasks scope creep? Yes / No
- Are any tasks too large? Yes / No
- Missing or risky items:
- Next correction:
```
