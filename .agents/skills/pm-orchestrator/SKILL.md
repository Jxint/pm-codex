---
name: pm-orchestrator
description: PM command center for routing Codex through intake, PRD, decomposition, execution, QA, PR prep, and review with minimal token use. Use at the start of any product or coding request.
---

# PM Orchestrator Skill

Use this skill as the first skill for product-building work.

Its job is not to produce every artifact. Its job is to choose the shortest correct workflow, preserve the original target, and prevent repeated context dumping.

## Core principle

Use the smallest artifact that lets the next step execute correctly.

Do not paste the whole PRD into every step. Use stable IDs and a compact context packet.

## Step 1: Classify request type

Choose exactly one primary mode.

| Mode | Trigger | Next skill |
|---|---|---|
| Discover | Idea is fuzzy, oral, scattered, or user is unsure | `$pm-intake` |
| Define | Goal is clear but PRD/spec is missing | `$prd-writer` |
| Decompose | PRD/spec exists and work must be split | `$task-decomposer` |
| Plan | A specific task exists but files/steps are unclear | `$execution-plan` |
| Build | A ready task exists with AC and files | `$feature-implementation` |
| Verify | Work is implemented and needs acceptance | `$qa-acceptance` |
| Prepare PR | Work is complete and needs PR body/checklist | `$pr-prep` |
| Review PR | PR/diff exists and needs review | `$pr-review` |
| Compress | Context is long or repetitive | `$token-efficient-context` |
| Trace | Need coverage map from goal to tasks/tests/PR | `$requirements-traceability` |
| Change | User changes scope after planning started | `$change-control` |

## Step 2: Create the Goal Lock

Always produce this compact block first. This block is the source of truth for future steps.

```md
## Goal Lock
- GL-ID: GL-001
- Original request:
- Target deliverable:
- Target user / actor:
- Core outcome:
- Deadline / quality bar:
- Non-goals:
- Hard constraints:
- Current mode:
- Next skill:
```

## Step 3: Choose output depth

Use one of these depth levels.

| Depth | Use when | Output size |
|---|---|---|
| Lite | User asks quick planning or next action | 1 screen |
| Standard | Normal PM work | Detailed but not exhaustive |
| Full | PRD, handoff, submission, or complex project | Complete artifact |

Default to Standard. Use Full only when the user asks for a formal artifact or the task will drive implementation.

## Step 4: Context budget rule

Before producing output, declare the context budget:

```md
## Context Budget
- Reuse existing IDs instead of repeating full text: Yes
- Full PRD needed now: Yes / No
- Full repository scan needed now: No by default
- Required context packet size: Tiny / Standard / Full
```

## Step 5: Route instead of duplicating

If another skill should do the work, do not reproduce that skill's full template. Instead output:

```md
## Routed Workflow
1. Use `$<skill>` for <reason>.
2. Input packet:
   - Goal Lock: GL-001
   - Relevant IDs:
   - Required source files/artifacts:
   - Output expected:
3. Stop condition:
4. Alignment check required after completion: Yes
```

## Step 6: Minimal PM command packet

When instructing Codex to execute the next step, use:

```text
Use $<skill>. Goal Lock GL-001: <one-line goal>. Work only on <artifact/task>. Use IDs instead of restating full docs. After the step, run a Goal Alignment Check against GL-001.
```

## Step 7: End with a routing decision

```md
## Orchestrator Decision
- Selected mode:
- Selected next skill:
- Why:
- Artifact to produce next:
- Stop condition:
- Token-saving rule:

## Goal Alignment Check
- Original target deliverable:
- Current orchestration:
- Match status: Match / Partial / Off-track
- Missing or risky items:
- Next correction:
```

## Anti-patterns

Do not:

- Rewrite the entire PRD at every step.
- Ask broad clarification questions after the Goal Lock is enough to proceed.
- Jump from rough idea directly to code.
- Split tasks by file only; split by user outcome first.
- Accept a PR that cannot be traced to requirements.
- Continue implementation after the task becomes off-track.
