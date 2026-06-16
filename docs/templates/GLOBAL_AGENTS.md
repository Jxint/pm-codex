# Global AGENTS.md for PM-Codex

Use this file as `~/.codex/AGENTS.md` if you want every Codex project to follow a PM-first workflow.

## Default behavior

For any product, feature, app, website, game, AI workflow, class project, startup demo, GitHub issue, or PR request:

1. Start from the user's target deliverable.
2. Create or reuse a compact Goal Lock.
3. Route through the shortest correct workflow.
4. Do not code before requirements and acceptance criteria are clear enough.
5. Split work into atomic tasks before implementation.
6. Use compact context packets instead of repeating full documents.
7. After each major step, check alignment with the original goal.
8. Before PR or merge, run product QA and PR review.

## Preferred skill routing

- Rough idea: use `$pm-orchestrator`, then `$pm-intake`.
- Clear product goal but no PRD: use `$prd-writer`.
- Need coverage proof: use `$requirements-traceability`.
- Need implementation tasks: use `$task-decomposer`.
- Long context: use `$token-efficient-context`.
- Scope changed: use `$change-control`.
- Multi-file code change: use `$execution-plan`, then `$feature-implementation`.
- Completed feature: use `$qa-acceptance`.
- Pull request: use `$pr-prep`, then `$pr-review`.

## Token-efficiency rules

- Do not paste or repeat full PRDs unless explicitly needed.
- Use IDs: GL, REQ, US, AC, TASK, PR.
- Read the smallest relevant file set first.
- Ask at most 3 blocking questions.
- Use Full output only for formal PRD, handoff, or release artifacts.

## Review default

When reviewing work, check:

- Original goal.
- Requirement coverage.
- Acceptance criteria.
- UX states.
- Tests/checks.
- Security/privacy risks.
- Scope creep.
- PR clarity.
