# PM Codex Skills

A repo-scoped Codex skill set for product-manager-style software work: clarify goals, write PRDs, decompose work into atomic tasks, execute with checkpoints, and review pull requests against the original product target.

## Why this exists

Most AI coding failures are not caused by syntax. They happen because the task was vague, too large, missing acceptance criteria, repeated too much context, or disconnected from the original product goal.

This repository gives Codex reusable skills that force a complete loop:

```text
Goal Lock → Product Intake → PRD → Traceability → Task Decomposition → Execution Plan → Implementation → QA → PR Preparation → PR Review → Release → Retrospective
```

Each skill has explicit inputs, outputs, decision gates, and a goal-alignment audit after each major step.

## Core operating idea

Use `$pm-orchestrator` first. It decides the shortest correct workflow and prevents Codex from repeatedly expanding long documents.

The token-saving pattern is:

```text
Create Goal Lock once → assign IDs → pass compact context packets → use specialized skills only when needed
```

## Installed structure

```text
AGENTS.md
PLANS.md
code_review.md
.github/
└─ pull_request_template.md
docs/
├─ SOURCE-NOTES.md
└─ templates/
   ├─ PRD.md
   └─ TASK.md
.agents/
└─ skills/
   ├─ pm-orchestrator/SKILL.md
   ├─ pm-intake/SKILL.md
   ├─ prd-writer/SKILL.md
   ├─ requirements-traceability/SKILL.md
   ├─ task-decomposer/SKILL.md
   ├─ token-efficient-context/SKILL.md
   ├─ change-control/SKILL.md
   ├─ execution-plan/SKILL.md
   ├─ feature-implementation/SKILL.md
   ├─ goal-alignment-review/SKILL.md
   ├─ qa-acceptance/SKILL.md
   ├─ pr-prep/SKILL.md
   ├─ pr-review/SKILL.md
   ├─ context-brief/SKILL.md
   ├─ release-manager/SKILL.md
   └─ retrospective/SKILL.md
```

## How to use in Codex

Use explicit skill calls when you want predictable behavior:

```text
Use $pm-orchestrator for this product request and choose the shortest correct workflow.
Use $pm-intake to clarify this app idea before writing the PRD.
Use $prd-writer to convert the clarified requirements into a complete PRD.
Use $requirements-traceability to map goals → requirements → AC → tasks → tests → PRs.
Use $task-decomposer to split the PRD into atomic Codex-sized tasks.
Use $token-efficient-context to compress context into a small next-step packet.
Use $change-control if I change scope after planning started.
Use $execution-plan before modifying files.
Use $goal-alignment-review after each implementation step.
Use $pr-prep before opening a pull request.
Use $pr-review to review this PR against the PRD and original goal.
```

## Recommended workflow

1. Start with `$pm-orchestrator`.
2. If the idea is rough, route to `$pm-intake`.
3. If the product goal is clear, route to `$prd-writer`.
4. Use `$requirements-traceability` to ensure every goal has requirements, AC, tasks, tests, and PR coverage.
5. Use `$task-decomposer` to convert the PRD into small tasks with acceptance criteria.
6. Use `$token-efficient-context` to create a tiny packet for one task instead of repeating the full PRD.
7. Use `$execution-plan` for any multi-file or ambiguous change.
8. Use `$feature-implementation` for the actual build.
9. Use `$goal-alignment-review` after each phase to check whether the work still matches the original target deliverable.
10. Use `$qa-acceptance` before claiming the feature is complete.
11. Use `$pr-prep` to create the PR summary and checklist.
12. Use `$pr-review` to inspect the PR before merge.
13. Use `$retrospective` to update lessons, risks, and AGENTS.md rules.

## Professional PM principles built in

- Separate problem, user, value, scope, requirements, design, implementation, and release.
- Lock the original target before work begins.
- Use user stories plus testable acceptance criteria.
- Prefer small, reviewable tasks over large vague tasks.
- Every task must map back to a requirement ID.
- Every implementation phase must include a product-goal alignment check.
- Every PR must explain purpose, scope, verification, risks, screenshots when relevant, and relationship to the PRD.
- Every scope change must go through change control instead of silently modifying the plan.

## Token-efficiency principles built in

- Keep `AGENTS.md` concise and put detailed workflows in skills.
- Use skill descriptions as clear triggers so Codex loads only the needed skill.
- Use IDs instead of repeating full requirements.
- Use context packets for one next action.
- Use traceability tables to check coverage without re-reading the whole project.

## Notes

These skills are instruction-only by default. Add scripts only when deterministic checks are needed, such as validating PRD IDs, task IDs, traceability coverage, or checklist completion.
