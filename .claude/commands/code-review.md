# Multi-Reviewer Code Review (Pattern H)

Launch 4 parallel subagent reviewers, each examining the diff from a different
dimension. Synthesize findings into a single verdict.

## When to Use

- After completing a non-trivial implementation (>50 lines changed)
- Before merging changes to production-critical code
- When changes touch multiple modules or cross system boundaries

## The 4 Review Dimensions

| Reviewer | Focus | Agent |
|----------|-------|-------|
| Logic Correctness | Conditions, state machines, arithmetic, comment/code alignment | `review-logic-correctness` |
| Concurrency & Performance | Thread safety, lock contention, hot-path perf, memory leaks | `review-concurrency-performance` |
| Test Coverage & Style | Missing tests, naming conventions, style consistency | `review-test-coverage-style` |
| Security & Risk | Input validation, auth, injection, sensitive data handling | `review-security-risk` |

## Execution

1. Gather the diff: `git diff HEAD~1` (or the relevant range)
2. Spawn all 4 reviewers in parallel, each receiving:
   - The unified diff with 10 lines of context
   - The task ID and one-line intent
   - The list of changed files with line ranges
3. Each reviewer returns findings in this format:

```
## Code review — <TASK-ID> — <reviewer-name>

### Findings
| ID | Severity | File:Line | Finding | Suggested action |
|----|----------|-----------|---------|-----------------|

### Summary
- Findings: N (CRITICAL: n, HIGH: n, MEDIUM: n, LOW: n)
- Verdict: CLEAN | MINOR_ISSUES | CHANGES_REQUESTED | BLOCKING
```

4. Synthesize: if ANY reviewer returns BLOCKING, the overall verdict is BLOCKING.
   Otherwise, take the worst individual verdict.

## Severity Guide

| Level | Meaning | Action |
|-------|---------|--------|
| CRITICAL | Wrong behavior always fires in production | Must fix before merge |
| HIGH | Wrong behavior under normal conditions | Must fix before merge |
| MEDIUM | Wrong behavior under edge cases | Fix or document as known limitation |
| LOW | Redundant code, stale comment, minor style | Optional fix |

## Hard Rules

- Reviewers are **read-only** — no Edit/Write
- Each reviewer stays in their lane — no overlap
- Every finding must quote file:line — no vague observations
- No false positives — if unsure, read more context before flagging
