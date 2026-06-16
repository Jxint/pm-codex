# Source Notes

This repository's workflow design is based on a combination of Codex documentation, standard product-management practice, agile task decomposition, and pull request review practice.

## Codex-specific design choices

- Skills are stored under `.agents/skills/<skill-name>/SKILL.md`.
- Each skill has focused `name` and `description` metadata so Codex can select it without loading full instructions too early.
- Each skill is instruction-only unless deterministic scripts are needed later.
- `AGENTS.md` is used for durable repository guidance.
- `PLANS.md` is used to make complex work plan-first.

## PM and requirements design choices

- PRDs separate product goal, target user, scope, requirements, acceptance criteria, UX states, data rules, risks, and traceability.
- User stories are written from the user's perspective and expanded with acceptance criteria.
- Acceptance criteria use observable conditions and expected behavior so tasks can be tested.
- Each task links back to requirement IDs and acceptance criteria.

## PR design choices

- PR descriptions must include purpose, requirement coverage, verification, risks, and reviewer focus.
- PR review checks product correctness before implementation polish.
- Every PR should be reviewed against the original target deliverable and acceptance criteria.

## Future improvements

- Add validation scripts to check missing REQ/US/AC/TASK IDs.
- Add a PRD completeness checker.
- Add a task-size checker.
- Add example project walkthroughs.
