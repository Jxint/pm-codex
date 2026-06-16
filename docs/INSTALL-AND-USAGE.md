# Install and Usage Guide

You do not need to manually invoke every skill each time.

The long list in README is a reference list, not a required prompt.

## Recommended setup levels

### Level 1: Repo-specific setup

Use this when one project needs PM-Codex behavior.

Copy these into the target project repository:

```text
AGENTS.md
PLANS.md
code_review.md
.github/pull_request_template.md
.agents/skills/
docs/templates/
scripts/validate_pm_artifacts.py
```

Then open Codex in that repository. Codex should read `AGENTS.md` and discover the repo skills.

Normal prompt:

```text
Build this feature: <your request>
```

More controlled prompt:

```text
Use $pm-orchestrator. Create a Goal Lock, choose the right workflow, and do not write code until the task is ready.
```

### Level 2: Global personal setup

Use this if every project you create should follow the same PM workflow.

Put your personal default guidance in:

```text
~/.codex/AGENTS.md
```

Put reusable skills in:

```text
$HOME/.agents/skills/
```

After that, every Codex project can inherit your personal PM workflow. Project-level files can still override or refine it.

### Level 3: Project template setup

Use this if you often start new repos.

Create a GitHub template repository from `Jxint/pm-codex`, or copy this repository's PM files into each new project before development starts.

Recommended new project structure:

```text
<your-project>/
├─ AGENTS.md
├─ PLANS.md
├─ code_review.md
├─ .github/pull_request_template.md
├─ .agents/skills/
├─ docs/product/
│  ├─ PRD.md
│  ├─ TASKS.md
│  └─ TRACEABILITY.md
└─ scripts/validate_pm_artifacts.py
```

## What to say each time

### Default: just describe the goal

```text
I want to build <product/feature>. Follow the project PM-Codex workflow.
```

### If Codex starts coding too early

```text
Use $pm-orchestrator first. Lock the original goal, choose the workflow, and do not code until the task is ready.
```

### If the idea is messy

```text
Use $pm-intake. Ask at most 3 blocking questions, then create a Product Target Contract.
```

### If you already know what to build

```text
Use $prd-writer, then $requirements-traceability, then $task-decomposer. Produce atomic tasks and next-step packets.
```

### If you want implementation

```text
Use $execution-plan for TASK-001. Read only the relevant files. Implement only this task. After each phase, run a Goal Alignment Check.
```

### If you want PR review

```text
Use $pr-review. Review this PR against the Goal Lock, linked requirements, acceptance criteria, verification evidence, and scope creep.
```

## Minimal repeated prompt

For most projects, this is enough:

```text
Use $pm-orchestrator. Follow Goal Lock → PRD → Traceability → Task Decomposition → Execution Plan → QA → PR Review. Keep context compact and do not repeat the full PRD.
```

You only need this line when you want to be extra strict. If `AGENTS.md` and skills are installed correctly, Codex can often route itself from the project guidance.

## Token-saving rules for daily use

- Do not paste the full skill list every time.
- Do not paste the full PRD every time.
- Use IDs: GL-001, REQ-001, US-001, AC-001, TASK-001.
- Ask Codex to produce a `Next-Step Packet` before implementation.
- Give Codex one task at a time.
- Ask for `$token-efficient-context` when the conversation gets long.
- Use `$requirements-traceability` instead of re-reading every document manually.

## Practical project start checklist

Before coding a new project, make sure these exist:

- [ ] `AGENTS.md`
- [ ] `.agents/skills/pm-orchestrator/SKILL.md`
- [ ] `.agents/skills/task-decomposer/SKILL.md`
- [ ] `.agents/skills/execution-plan/SKILL.md`
- [ ] `.agents/skills/pr-review/SKILL.md`
- [ ] `code_review.md`
- [ ] `.github/pull_request_template.md`

If these exist, do not paste the full instruction list. Start with `$pm-orchestrator` or a normal product request.
