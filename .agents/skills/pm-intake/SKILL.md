---
name: pm-intake
description: Product intake and requirement clarification for rough app, web, AI, game, hackathon, course, or startup ideas before PRD or coding. Use when the idea is vague, oral, scattered, or missing user/value/scope/constraints.
---

# PM Intake Skill

Use this skill to turn a rough idea into a product target contract that Codex can later use for PRD writing, task decomposition, implementation, QA, and PR review.

Do not code while using this skill.

## Inputs to look for

- Raw user idea or oral requirement.
- Intended final artifact: app, web demo, game, AI agent, PRD, PPT, Word document, prototype, deployable MVP, or GitHub project.
- Deadline, team size, platform, constraints, and demo expectations.
- Existing materials: screenshots, code, Figma, PPT, class requirements, repository, API docs, or previous decisions.

## Step 1: Extract the Product Target Contract

Write this first.

```md
# Product Target Contract

## One-line product definition
<This product helps [target user] do [core job] by [core mechanism].>

## Target deliverable
<Exactly what must be produced: PRD / MVP / feature / prototype / demo / PR / release.>

## Target users
| User group | Situation | Pain point | Desired outcome |
|---|---|---|---|

## Core value proposition
- Functional value:
- Emotional / presentation value:
- Business / course / hackathon value:

## Success definition
- User success:
- Product success:
- Demo / delivery success:

## Non-goals
- This project will not:
```

## Step 2: Clarify the problem without over-asking

If information is missing but not blocking, make an assumption and label it.

Ask questions only when the answer changes scope, architecture, or acceptance criteria. Ask at most 3 questions.

Question categories:

1. User: Who uses it and in what scene?
2. Job-to-be-done: What do they need to accomplish?
3. Platform: Web, iOS, Android, desktop, WeChat, PPT, Word, 3D model, game engine?
4. Deadline: Hackathon demo, class submission, long-term product?
5. Data: What input does the system need? What output must it produce?
6. Constraints: No network, no external AI, no payment, no dark mode, no backend, etc.
7. Quality bar: Demo only, MVP, production, portfolio, class assignment?

## Step 3: Build the scope table

```md
## Scope Table
| Area | MVP must-have | V1 should-have | Later / not now | Reason |
|---|---|---|---|---|
| User flow |  |  |  |  |
| UI |  |  |  |  |
| Data |  |  |  |  |
| AI / automation |  |  |  |  |
| Backend |  |  |  |  |
| Deployment |  |  |  |  |
| Demo / presentation |  |  |  |  |
```

## Step 4: Define the first complete user flow

Use this format:

```md
## Primary User Flow
1. User enters from:
2. User provides input:
3. System processes:
4. System shows:
5. User confirms / edits:
6. System saves / exports / shares:
7. Success state:
8. Failure state:
```

## Step 5: Identify risks early

```md
## Risk Register
| Risk | Why it matters | Severity | Mitigation | Needs decision? |
|---|---|---|---|---|
```

Common risks:

- The idea is too broad for the deadline.
- The AI behavior is not deterministic enough for demo.
- The UI looks good but core function is fake.
- The backend is overbuilt for MVP.
- Data is unavailable or privacy-sensitive.
- The PRD describes features but not acceptance criteria.
- The task cannot be implemented in one Codex session.

## Step 6: Produce a PRD readiness checklist

```md
## Ready for PRD Checklist
- [ ] Target user is clear.
- [ ] Core user pain point is clear.
- [ ] Target deliverable is clear.
- [ ] MVP scope is bounded.
- [ ] Non-goals are explicit.
- [ ] Primary user flow is written.
- [ ] Main risks are known.
- [ ] Assumptions are marked.
```

## Step 7: Goal Alignment Check

End with:

```md
## Goal Alignment Check
- Original target deliverable:
- Current output produced:
- Match status: Match / Partial / Off-track
- Missing or risky items:
- Next correction:
```
