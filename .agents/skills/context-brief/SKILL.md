---
name: context-brief
description: Compress a long project conversation, PRD, repository state, design discussion, or implementation history into a concise Codex-ready context brief for future sessions and token savings.
---

# Context Brief Skill

Use this skill when context is long, scattered, or repeated.

The output should be short enough to paste into a new Codex task, but detailed enough to prevent wrong assumptions.

## Output format

```md
# Project Context Brief

## 1. Product Identity
- Product name:
- One-line definition:
- Target users:
- Core value:
- Target deliverable:

## 2. Current Status
| Area | Status | Evidence / notes |
|---|---|---|
| PRD | Not started / Draft / Approved |  |
| UI |  |  |
| Frontend |  |  |
| Backend |  |  |
| Data |  |  |
| AI logic |  |  |
| Deployment |  |  |
| QA |  |  |

## 3. Key Decisions
| Decision | Reason | Date / source | Impact |
|---|---|---|---|

## 4. Hard Constraints
- 
- 

## 5. Non-goals
- 
- 

## 6. Important Files / Artifacts
| Path / artifact | Purpose | When Codex should read it |
|---|---|---|

## 7. Requirement Map
| Req ID | Summary | Priority | Status |
|---|---|---|---|

## 8. Current Backlog
| Task ID | Summary | Priority | Status | Next action |
|---|---|---|---|---|

## 9. Risks
| Risk | Impact | Mitigation |
|---|---|---|

## 10. Next Best Prompt for Codex
```text
Use $execution-plan to work on TASK-___. Read only <files>. Implement only <behavior>. Check alignment against REQ-___ and AC-___ after each phase.
```

## Goal Alignment Check
- Original target deliverable:
- Brief produced:
- Match status: Match / Partial / Off-track
- Missing or risky items:
- Next correction:
```

## Rules

- Remove repeated conversation history.
- Preserve decisions, constraints, non-goals, and current task status.
- Do not invent completed work.
- Mark assumptions clearly.
- Prefer requirement/task IDs over long explanations.
