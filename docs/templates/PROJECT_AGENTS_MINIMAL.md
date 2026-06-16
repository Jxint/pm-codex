# AGENTS.md

This project uses PM-Codex workflow.

## Default behavior

For every product, feature, issue, or PR request:

1. Start with the original target deliverable.
2. Use `$pm-orchestrator` when the workflow is not obvious.
3. Create or reuse Goal Lock `GL-001`.
4. Do not start coding until the task has requirements, acceptance criteria, scope boundary, and verification.
5. Split work into atomic tasks with `TASK-` IDs.
6. Use compact context packets instead of repeating the full PRD.
7. After each major step, run a Goal Alignment Check.
8. Before merging, run QA and PR review.

## Required artifact flow

```text
Goal Lock → PRD → Traceability → Atomic Tasks → Execution Plan → Implementation → QA → PR Prep → PR Review
```

## Definition of Ready

A task is ready only when it has:

- Goal Lock link.
- REQ / US / AC IDs.
- In-scope and out-of-scope boundaries.
- Relevant files to inspect.
- Verification method.
- Stop conditions.

## Definition of Done

A task is done only when:

- Acceptance criteria are checked.
- Tests/checks are run or limitations are stated.
- The final behavior matches the original target.
- PR notes are ready.

## Review

Use `code_review.md` and `.github/pull_request_template.md` for PRs.
