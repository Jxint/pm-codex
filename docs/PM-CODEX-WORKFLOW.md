# PM-Codex Professional Workflow

This document explains how to use the skills as a professional PM workflow while keeping Codex efficient.

## 1. What was missing before this optimization

A basic PM skill set can clarify requirements and write tasks, but a stronger PM-Codex system needs five extra mechanisms:

1. Orchestration: decide which skill to use instead of loading every workflow.
2. Goal Lock: preserve the original target deliverable so later work does not drift.
3. Traceability: connect goal → requirement → story → acceptance criterion → task → test → PR.
4. Token control: compress context into small packets and pass IDs instead of full documents.
5. Change control: handle new requirements without silently breaking the original plan.

## 2. Default command flow

```text
User request
→ $pm-orchestrator
→ Goal Lock
→ choose mode
→ use one specialized skill
→ produce artifact
→ goal alignment check
→ compress next-step context
→ execute / review
```

## 3. Modes

| Mode | Use when | Skill |
|---|---|---|
| Discover | Idea is unclear | `$pm-intake` |
| Define | PRD/spec is needed | `$prd-writer` |
| Trace | Need coverage proof | `$requirements-traceability` |
| Decompose | Need exact tasks | `$task-decomposer` |
| Compress | Context is long | `$token-efficient-context` |
| Change | Scope changed | `$change-control` |
| Plan | Need implementation steps | `$execution-plan` |
| Build | Task is ready | `$feature-implementation` |
| Verify | Need acceptance | `$qa-acceptance` |
| PR Prep | Need PR body/checklist | `$pr-prep` |
| PR Review | Need review | `$pr-review` |

## 4. How to save tokens

Do:

- Create one Goal Lock.
- Assign stable IDs: GL, REQ, US, AC, TASK, PR.
- Pass only the next-step packet to Codex.
- Reference file paths instead of pasting whole files.
- Use `$requirements-traceability` to check coverage instead of re-reading the entire PRD.
- Use `$change-control` only when the target changes.

Do not:

- Paste the full PRD into every prompt.
- Ask Codex to inspect the whole repository by default.
- Combine PRD writing, task breakdown, coding, QA, and PR review in one prompt.
- Recreate long background summaries after the Goal Lock exists.

## 5. Standard next-step packet

```md
## Next-Step Packet
- Goal Lock: GL-001
- Current task: TASK-001
- Relevant IDs: REQ-001, US-001, AC-001
- Required files: <paths only>
- Do not touch: <paths/behaviors>
- Acceptance checks: <short list>
- Stop if: <blockers>
```

## 6. Recommended prompts

### Start a project

```text
Use $pm-orchestrator. Create a Goal Lock and choose the shortest workflow for this product idea. Do not write code yet.
```

### Turn idea into PRD

```text
Use $prd-writer. Use Goal Lock GL-001. Produce a PRD with requirement IDs, user stories, acceptance criteria, risks, and traceability. End with a Goal Alignment Check.
```

### Split into tasks

```text
Use $task-decomposer. Use Goal Lock GL-001 and the PRD IDs. Split by product outcome first, then technical layer. Produce atomic task cards with PR boundaries and next-task packets.
```

### Implement one task efficiently

```text
Use $execution-plan for TASK-001. Goal Lock GL-001. Relevant IDs: REQ-001, US-001, AC-001. Read only the listed files. Implement only the task. Do not repeat the full PRD. After each phase, check goal alignment.
```

### Review a PR

```text
Use $pr-review. Review this PR against GL-001, linked REQ/US/AC/TASK IDs, acceptance criteria, code quality, UX states, risk, and verification evidence.
```

## 7. Professional PM acceptance gate

A project is ready for implementation only when:

- Goal Lock exists.
- MVP scope and non-goals are clear.
- P0 requirements have acceptance criteria.
- P0 acceptance criteria have tasks.
- Each task is atomic and has a verification plan.
- The next task packet is short enough to run without the full PRD.

A PR is ready for review only when:

- It links to the original goal and requirement IDs.
- It explains user-visible behavior changes.
- It lists verification evidence.
- It documents risks and rollback.
- It states what reviewers should focus on.
