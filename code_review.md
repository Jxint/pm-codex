# Code Review Guide

Use this guide for Codex `/review`, PR review, and self-review before merge.

## Review priority order

1. Product correctness: does the change satisfy the original goal?
2. Requirement coverage: does it satisfy the linked PRD requirements and acceptance criteria?
3. User flow: can the intended user complete the flow?
4. Regression risk: what existing behavior could be broken?
5. Implementation quality: is the code simple, maintainable, and scoped?
6. Test evidence: are relevant checks present and credible?
7. PR clarity: can a reviewer understand purpose, scope, risks, and verification quickly?

## Review checklist

### 1. Goal and scope
- [ ] PR states the original target deliverable.
- [ ] PR links to PRD / requirement IDs.
- [ ] No unrelated features or refactors are included.
- [ ] Any intentional scope change is explained.

### 2. Product behavior
- [ ] Main happy path works.
- [ ] Empty state is handled.
- [ ] Loading state is handled where relevant.
- [ ] Error state is handled with user-readable feedback.
- [ ] Edge cases are listed and handled or deferred explicitly.

### 3. Technical correctness
- [ ] Data contracts are clear.
- [ ] State transitions are predictable.
- [ ] API calls handle failure.
- [ ] No secret keys or private data are committed.
- [ ] No avoidable global side effects.
- [ ] Naming matches existing conventions.

### 4. Maintainability
- [ ] Change is smaller than necessary, not larger.
- [ ] Reused patterns are preferred over new abstractions.
- [ ] New abstractions are justified.
- [ ] Files are placed in appropriate directories.
- [ ] Comments explain non-obvious decisions, not obvious code.

### 5. Verification
- [ ] Tests added or updated when logic changes.
- [ ] Lint/type/build checks run when available.
- [ ] Manual verification steps are included.
- [ ] Screenshots or recordings are included for UI changes.

## Review output format

```md
# PR Review

## Summary
- Verdict: Approve / Request changes / Comment only
- Main reason:

## Goal Alignment
- Original target:
- What the PR actually changes:
- Match status: Match / Partial / Off-track

## Blocking Issues
| Severity | File / area | Issue | Required fix |
|---|---|---|---|

## Non-blocking Suggestions
| Area | Suggestion | Why it matters |
|---|---|---|

## Acceptance Criteria Coverage
| Requirement / AC | Covered? | Evidence | Gap |
|---|---|---|---|

## Verification Review
- Tests reviewed:
- Manual evidence reviewed:
- Missing checks:

## Final Recommendation
- Merge readiness:
- Required next action:
```
