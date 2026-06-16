---
name: token-efficient-context
description: Reduce Codex token use by compressing PRDs, long chats, repository state, or task history into Goal Lock, IDs, traceability tables, and minimal context packets. Use when prompts get long or repeated.
---

# Token Efficient Context Skill

Use this skill when context is long, repeated, or slowing Codex down.

The output is not a full summary. It is a working packet for the next Codex step.

## Core rules

1. Preserve decisions, IDs, constraints, and open risks.
2. Remove repeated explanations.
3. Replace long requirement text with stable IDs.
4. Keep only what the next step needs.
5. Do not include full source code unless the next step requires exact code.

## Step 1: Choose packet size

| Packet | Use when | Max target |
|---|---|---|
| Tiny | One task execution | 10 bullets or less |
| Standard | Planning / PR review | 1-2 pages |
| Full | Handoff or new session | 3-5 pages |

Default to Tiny for implementation.

## Step 2: Extract the Goal Lock

```md
## Goal Lock
- GL-ID:
- Target deliverable:
- Core outcome:
- Hard constraints:
- Non-goals:
```

## Step 3: Create an ID index

```md
## ID Index
| ID | Type | One-line meaning | Status |
|---|---|---|---|
| REQ-001 | Requirement |  |  |
| US-001 | User story |  |  |
| AC-001 | Acceptance criterion |  |  |
| TASK-001 | Task |  |  |
```

## Step 4: Create the next-step packet

```md
## Next-Step Context Packet
- Goal Lock:
- Current task:
- Relevant IDs:
- Required files/artifacts:
- Constraints:
- Acceptance checks:
- Do not touch:
- Stop if:
```

## Step 5: Archive but do not repeat

If long details exist but are not needed now, list their location instead of copying them.

```md
## Reference Pointers
| Artifact | Where to find it | When to read it |
|---|---|---|
```

## Step 6: Output ready-to-use prompt

```text
Use $<next-skill>. Goal Lock <GL-ID>. Work on <TASK-ID> only. Relevant IDs: <REQ/US/AC>. Read only <files/artifacts>. Do not repeat the full PRD. After completion, check alignment against <GL-ID>.
```

## Goal Alignment Check
- Original target deliverable:
- Context packet produced:
- Match status: Match / Partial / Off-track
- Missing or risky items:
- Next correction:
