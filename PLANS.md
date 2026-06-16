# PLANS.md

Use this file as the default planning contract for complex Codex work.

## When a plan is required

Create a plan before implementation when the task is:

- Multi-file.
- Ambiguous.
- Related to product scope or user flow.
- Involves data model, API, auth, payment, calendar, AI output, storage, deployment, or PR review.
- Could break existing behavior.

## Standard execution plan format

```md
# Execution Plan: <task name>

## 1. Goal Card
- Original user request:
- Target deliverable:
- Target user / actor:
- Success definition:
- Non-goals:
- Hard constraints:

## 2. Current Context
- Relevant PRD / requirement IDs:
- Existing files likely involved:
- Unknowns:
- Assumptions:

## 3. Scope Boundary
| In scope | Out of scope | Reason |
|---|---|---|

## 4. Step Plan
| Step | Action | Files / artifact | Expected output | Verification |
|---|---|---|---|---|

## 5. Risk Register
| Risk | Impact | Mitigation | Checkpoint |
|---|---|---|---|

## 6. Goal Alignment Check Before Work
- Does this plan directly produce the target deliverable?
- Which step maps to the main user value?
- Which steps are only support work?
- What would count as scope creep?

## 7. Implementation Checkpoints
After each step, write:

### Checkpoint <n>
- Completed:
- Evidence:
- Match to original goal: Match / Partial / Off-track
- Correction needed:
- Continue / Stop:

## 8. Final Verification
- Acceptance criteria checked:
- Tests / commands run:
- Manual verification:
- Known limitations:
- PR notes needed:
```

## Task-size rule

A task is too large if it contains more than one primary user outcome. Split it until each task can be described as:

```text
Change <one behavior> for <one actor> in <one area> so that <one measurable outcome> happens.
```

## No silent expansion

Do not add new features while executing a task. If an extra feature seems useful, record it under "Follow-up" instead of implementing it.
