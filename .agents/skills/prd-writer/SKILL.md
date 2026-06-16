---
name: prd-writer
description: Write a detailed, implementation-ready PRD from clarified requirements, oral notes, project ideas, screenshots, class assignments, hackathon concepts, or feature requests. Use before task decomposition or coding.
---

# PRD Writer Skill

Use this skill to create a PRD that a PM, designer, engineer, and Codex can all understand and execute.

Do not write code while using this skill.

## PRD principles

- A PRD defines what the product must do and why it matters.
- Separate product requirements from implementation details.
- Implementation notes are allowed only when they clarify constraints or feasibility.
- Every important requirement must have an ID.
- Every user-facing behavior must have acceptance criteria.
- Every acceptance criterion must be testable.

## Required output structure

```md
# PRD: <Product / Feature Name>

## 0. Document Control
| Field | Value |
|---|---|
| Owner |  |
| Date |  |
| Status | Draft / Review / Approved |
| Source materials |  |
| Target deliverable |  |

## 1. Product Summary
### 1.1 One-line definition
### 1.2 Background
### 1.3 Problem statement
### 1.4 Product goal
### 1.5 Success metrics

## 2. Users and Scenarios
### 2.1 Target users
| User | Context | Pain point | Motivation | Success outcome |
|---|---|---|---|---|

### 2.2 Core scenarios
| Scenario ID | Scenario | Trigger | User goal | Priority |
|---|---|---|---|---|

## 3. Scope
### 3.1 MVP scope
### 3.2 V1 scope
### 3.3 Future scope
### 3.4 Explicit non-goals

## 4. User Flow
### 4.1 Primary flow
### 4.2 Alternative flows
### 4.3 Failure flows

## 5. Functional Requirements
| Req ID | Requirement | User value | Priority | Acceptance criteria IDs |
|---|---|---|---|---|
| REQ-001 |  |  | P0/P1/P2 | AC-001 |

## 6. User Stories
| Story ID | User story | Related req | Priority |
|---|---|---|---|
| US-001 | As a <user>, I want <capability>, so that <benefit>. | REQ-001 | P0 |

## 7. Acceptance Criteria
Use either bullet criteria or EARS-style criteria.

| AC ID | Related story / req | Condition | Expected behavior | Test method |
|---|---|---|---|---|
| AC-001 | US-001 | When <condition> | The system shall <behavior> | Manual / Unit / E2E |

## 8. UX Requirements
### 8.1 Screens / pages
| Screen | Purpose | Main elements | Empty state | Loading state | Error state |
|---|---|---|---|---|---|

### 8.2 Interaction rules
### 8.3 Copywriting rules
### 8.4 Accessibility / mobile adaptation

## 9. Data and System Rules
### 9.1 Data entities
| Entity | Fields | Source | Storage | Notes |
|---|---|---|---|---|

### 9.2 State transitions
### 9.3 Permissions / privacy
### 9.4 AI output format if relevant

## 10. Non-functional Requirements
| NFR ID | Requirement | Target | Verification |
|---|---|---|---|
| NFR-001 | Performance |  |  |
| NFR-002 | Reliability |  |  |
| NFR-003 | Security / privacy |  |  |
| NFR-004 | Compatibility |  |  |

## 11. Dependencies and Constraints
| ID | Dependency / constraint | Impact | Mitigation |
|---|---|---|---|

## 12. Risks and Open Questions
| ID | Risk / question | Impact | Owner | Resolution needed before |
|---|---|---|---|---|

## 13. Milestones
| Milestone | Deliverable | Exit criteria |
|---|---|---|

## 14. Requirement Traceability Matrix
| Goal | Req ID | Story ID | AC ID | Task ID later |
|---|---|---|---|---|

## 15. PRD Review Checklist
- [ ] Goal is concrete.
- [ ] MVP and non-goals are explicit.
- [ ] Each P0 requirement has acceptance criteria.
- [ ] Core user flow is complete.
- [ ] Edge cases are captured.
- [ ] Data entities are identified.
- [ ] Risks and assumptions are visible.
- [ ] The PRD can be decomposed into tasks.
```

## Writing rules

### Requirement wording
Prefer:

```text
The system shall <verb> <object> when <condition>, so that <user outcome>.
```

Avoid:

```text
Make the experience better.
Make it smart.
Optimize the page.
Improve interaction.
```

Replace vague terms with observable behavior.

### Priority definitions

- P0: required for the target deliverable to make sense.
- P1: important but can be deferred without breaking the core demo/MVP.
- P2: nice-to-have.

### Acceptance criteria quality bar

A good acceptance criterion is:

- Specific.
- Observable.
- Testable.
- Attached to one requirement or user story.
- Clear about input, condition, expected behavior, and failure state.

## Final Goal Alignment Check

End with:

```md
## Goal Alignment Check
- Original target deliverable:
- Current PRD produced:
- Match status: Match / Partial / Off-track
- Missing or risky items:
- Next correction:
```
