---
name: pr-prep
description: Prepare a pull request before opening or merging it. Use after implementation and QA to create a complete PR description, verify linked requirements, summarize changes, list tests, risks, screenshots, and reviewer focus.
---

# PR Prep Skill

Use this skill before opening a pull request or before asking for review.

## Step 1: Confirm PR purpose

```md
## PR Purpose
- Original request:
- Target deliverable:
- Product goal:
- Linked issue / task:
- Linked PRD requirements:
```

## Step 2: Summarize changes by product impact

Do not only list files. Explain user-visible behavior.

```md
## Change Summary
| Area | Before | After | User / system impact |
|---|---|---|---|
```

## Step 3: Requirement coverage

```md
## Requirement Coverage
| ID | Requirement / AC | Covered? | Evidence |
|---|---|---|---|
| REQ- |  | Yes / Partial / No |  |
| AC- |  | Yes / Partial / No |  |
```

If any P0 item is partial or no, mark the PR as not ready unless the user explicitly accepts a partial PR.

## Step 4: Verification summary

```md
## Verification
### Automated
| Check | Command | Result |
|---|---|---|

### Manual
| Scenario | Steps | Expected | Actual |
|---|---|---|---|
```

## Step 5: Risk and rollback

```md
## Risk and Rollback
| Risk | Impact | Mitigation | Rollback |
|---|---|---|---|
```

## Step 6: Reviewer focus

```md
## Reviewer Focus
- Product behavior to check:
- Technical risk to check:
- UX state to check:
- Data / privacy area to check:
```

## Step 7: Final PR description

Produce a ready-to-paste PR body using `.github/pull_request_template.md`.

## Step 8: PR readiness gate

```md
## PR Readiness Gate
- Product goal clear? Yes / No
- Requirements linked? Yes / No
- Tests/checks documented? Yes / No
- Screenshots/demo included if needed? Yes / No / N/A
- Risks documented? Yes / No
- Scope creep removed? Yes / No
- Ready to open PR? Yes / No

## Goal Alignment Check
- Original target deliverable:
- PR produced:
- Match status: Match / Partial / Off-track
- Missing or risky items:
- Next correction:
```
