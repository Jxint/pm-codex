# AGENTS.md

This repository contains PM-oriented Codex skills. Treat it as a reusable workflow library, not as an application codebase.

## Default working mode

Codex must work like a product-minded implementation partner:

1. Identify the target deliverable before producing outputs.
2. Use `$pm-orchestrator` first for any product, feature, coding, PRD, task-splitting, or PR request.
3. Separate problem, user value, requirements, design, implementation, QA, PR, and release.
4. Keep every step traceable to the original product goal.
5. Prefer precise markdown artifacts over vague prose.
6. When writing tasks, make them small enough for one Codex session.
7. After every major step, audit whether the output still matches the original goal.

## Token-efficiency rules

- Do not repeat the full PRD or full conversation in every output.
- Create a compact `Goal Lock` once, then reference it by ID.
- Use requirement IDs, user story IDs, acceptance criterion IDs, and task IDs instead of restating long text.
- Use `$token-efficient-context` when context exceeds what one task needs.
- Read the smallest relevant file set first. Do not scan the full repository unless the task requires it.
- Prefer Tiny or Standard outputs during execution; use Full only for formal PRD, handoff, or release artifacts.
- Route to a specialized skill instead of embedding all instructions in one response.

## Required language and output rules

- Use clear, execution-oriented language.
- Avoid empty PM phrases such as "optimize experience", "make it smarter", "improve interaction" unless the measurable behavior is defined.
- Mark assumptions explicitly.
- Mark blockers explicitly.
- Do not hide uncertainty.
- Do not ask excessive clarification questions. Ask at most 3 at a time, and only when the answer blocks progress.
- Prefer structured tables for scope, requirements, tasks, risks, and verification.

## Skill routing

| User intent | Start with |
|---|---|
| Rough idea / oral requirement | `$pm-orchestrator` → `$pm-intake` |
| Need formal PRD | `$pm-orchestrator` → `$prd-writer` |
| Need detailed task breakdown | `$pm-orchestrator` → `$task-decomposer` |
| Long context / token pressure | `$token-efficient-context` |
| Need proof all requirements are covered | `$requirements-traceability` |
| Scope changed after planning | `$change-control` |
| Multi-file implementation | `$execution-plan` → `$feature-implementation` |
| Acceptance testing | `$qa-acceptance` |
| PR description / checklist | `$pr-prep` |
| PR review | `$pr-review` using `code_review.md` |

## Project artifact hierarchy

When a project is being planned, use this hierarchy:

```text
Goal Lock: GL-001
└─ PRD
   ├─ Requirement IDs: REQ-001
   ├─ User Stories: US-001
   ├─ Acceptance Criteria: AC-001
   ├─ Non-functional Requirements: NFR-001
   └─ Open Questions: OQ-001
      └─ Task Breakdown
         ├─ Epic: EPIC-001
         ├─ Feature: FEAT-001
         ├─ Task: TASK-001
         └─ Subtask: SUB-001
            └─ PR
               ├─ Linked requirements
               ├─ Changed files
               ├─ Verification evidence
               └─ Remaining risks
```

## Goal-alignment rule

Every skill output must include a short audit block unless the user explicitly requests a very short answer:

```md
## Goal Alignment Check
- Original target deliverable:
- Current output produced:
- Match status: Match / Partial / Off-track
- Missing or risky items:
- Next correction:
```

## Definition of Ready

Before implementation starts, a task should have:

- A user or system goal.
- A clear before/after behavior.
- At least one acceptance criterion.
- Related files or modules to inspect.
- Known constraints and non-goals.
- A verification method.
- A trace link to Goal Lock / REQ / US / AC.

If these are missing, use `$pm-intake`, `$prd-writer`, `$task-decomposer`, or `$requirements-traceability` before coding.

## Definition of Done

A task is not done until:

- The requested behavior is implemented or the limitation is explained.
- The implementation maps to requirement IDs or user stories.
- Acceptance criteria are checked.
- Relevant tests/checks are run, or the reason they were not run is stated.
- The diff is reviewed for regressions, scope creep, and product mismatch.
- PR notes are prepared when changes are meant to be merged.

## Review expectations

Use `code_review.md` when reviewing changes. Review against:

1. Original product goal.
2. PRD requirements.
3. Acceptance criteria.
4. Technical correctness.
5. UX states: empty, loading, error, success.
6. Security, privacy, and data persistence risks.
7. Demo/readiness risks.
8. Traceability: every PR should link back to requirements/tasks.

## When to update this file

Update `AGENTS.md` when:

- Codex repeats the same mistake.
- A recurring review comment appears.
- A project has a new mandatory convention.
- A skill needs a stronger routing rule.
- The workflow needs to prevent scope creep.
- Codex reads too many files or repeats too much context.
