# PM Codex Skills

A repo-scoped Codex skill set for product-manager-style software work: clarify goals, write PRDs, decompose work into atomic tasks, execute with checkpoints, and review pull requests against the original product target.

## Why this exists

Most AI coding failures are not caused by syntax. They happen because the task was vague, too large, missing acceptance criteria, or disconnected from the original product goal.

This repository gives Codex reusable skills that force a complete loop:

```text
Idea → Product Intake → PRD → Task Decomposition → Execution Plan → Implementation → QA → PR Preparation → PR Review → Release → Retrospective
```

Each skill has explicit inputs, outputs, decision gates, and a goal-alignment audit after each major step.

## Installed structure

```text
AGENTS.md
PLANS.md
code_review.md
.github/
└─ pull_request_template.md
.agents/
└─ skills/
   ├─ pm-intake/SKILL.md
   ├─ prd-writer/SKILL.md
   ├─ task-decomposer/SKILL.md
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
Use $pm-intake to clarify this app idea before writing the PRD.
Use $prd-writer to convert the clarified requirements into a complete PRD.
Use $task-decomposer to split the PRD into atomic Codex-sized tasks.
Use $execution-plan before modifying files.
Use $goal-alignment-review after each implementation step.
Use $pr-prep before opening a pull request.
Use $pr-review to review this PR against the PRD and original goal.
```

## Recommended workflow

1. Start with `$pm-intake` when the idea is still rough.
2. Use `$prd-writer` once the target user, product value, scope, and constraints are known.
3. Use `$task-decomposer` to convert the PRD into small tasks with acceptance criteria.
4. Use `$execution-plan` for any multi-file or ambiguous change.
5. Use `$feature-implementation` for the actual build.
6. Use `$goal-alignment-review` after each phase to check whether the work still matches the original target deliverable.
7. Use `$qa-acceptance` before claiming the feature is complete.
8. Use `$pr-prep` to create the PR summary and checklist.
9. Use `$pr-review` to inspect the PR before merge.
10. Use `$retrospective` to update lessons, risks, and AGENTS.md rules.

## Product-management principles built in

- Separate problem, user, value, scope, requirements, design, implementation, and release.
- Use user stories plus testable acceptance criteria.
- Prefer small, reviewable tasks over large vague tasks.
- Every task must map back to a requirement ID.
- Every implementation phase must include a product-goal alignment check.
- Every PR must explain purpose, scope, verification, risks, screenshots when relevant, and relationship to the PRD.

## Notes

These skills are instruction-only by default. Add scripts only when deterministic checks are needed, such as validating PRD IDs, task IDs, or checklist completion.
