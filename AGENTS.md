# AGENTS.md

This repository contains PM-oriented Codex skills. Treat it as a reusable workflow library, not as an application codebase.

## Default working mode

Codex must work like a product-minded implementation partner:

1. Identify the target deliverable before producing outputs.
2. Separate problem, user value, requirements, design, implementation, QA, PR, and release.
3. Keep every step traceable to the original product goal.
4. Prefer precise markdown artifacts over vague prose.
5. When writing tasks, make them small enough for one Codex session.
6. After every major step, audit whether the output still matches the original goal.

## Required language and output rules

- Use clear, execution-oriented language.
- Avoid empty PM phrases such as "optimize experience", "make it smarter", "improve interaction" unless the measurable behavior is defined.
- Mark assumptions explicitly.
- Mark blockers explicitly.
- Do not hide uncertainty.
- Do not ask excessive clarification questions. Ask at most 3 at a time, and only when the answer blocks progress.
- Prefer structured tables for scope, requirements, tasks, risks, and verification.

## Project artifact hierarchy

When a project is being planned, use this hierarchy:

```text
Vision / Product Goal
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

If these are missing, use `$pm-intake`, `$prd-writer`, or `$task-decomposer` before coding.

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

## When to update this file

Update `AGENTS.md` when:

- Codex repeats the same mistake.
- A recurring review comment appears.
- A project has a new mandatory convention.
- A skill needs a stronger routing rule.
- The workflow needs to prevent scope creep.
