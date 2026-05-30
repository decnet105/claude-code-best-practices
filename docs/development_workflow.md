# Development Workflow

**Status:** Active — governs all development.

---

## 1. End-to-End Development Lifecycle

Every feature, fix, or improvement follows this pipeline. No steps may be skipped.

```
 PHASE 1: INTAKE
 ================
 Human identifies need (bug, feature, research question)
        |
        v
 PHASE 2: RESEARCH (if needed)
 ==============================
 Produce research findings (RES-XXX brief)
        |
 Review findings, extract actionable items
        |
 Human approves implementation plan
        |
        v
 PHASE 3: DESIGN
 ================
 Design solution:
   - Identify files to modify
   - Define public interfaces
   - List observable behaviors (test cases)
   - For CRITICAL files: post written plan first
        |
        v
 PHASE 4: TDD IMPLEMENTATION
 ============================
 For each behavior (vertical slice):
   RED:   Write one failing test
   GREEN: Write minimal code to pass
   VERIFY: Run full test suite
   REPEAT: Next behavior
        |
 Phase-gate: multi-phase tasks STOP after each phase for review
        |
        v
 PHASE 5: QA VALIDATION *** MANDATORY ***
 =========================================
 Run full test suite + any integration tests
   FAIL → file defect, fix via TDD, re-test
   PASS → mark PASS in ai_activity_log.md
        |
        v
 PHASE 6: FINAL AUDIT
 =====================
 Code review (use /code-review for non-trivial changes)
 Documentation check (change_log, README if user-facing)
        |
        v
 PHASE 7: HUMAN APPROVAL
 ========================
 Human reviews and approves → merge + deploy
```

## 2. TDD Protocol (Mandatory)

See `/tdd` skill for the full protocol. Key rules:

- **Vertical slicing:** one test → one implementation → repeat
- **Never horizontal:** don't write all tests first, then all code
- **RED first:** test MUST fail before writing implementation
- **Minimal GREEN:** write ONLY enough code to pass the current test
- **Regression gate:** full suite must pass after each GREEN

## 3. Debugging Protocol

See `/debug` skill. The iron law: **NO FIXES WITHOUT ROOT CAUSE.**

- 3-fix threshold: if 3 fixes fail, it's architectural, not a code bug
- Always classify: L1 (infrastructure) → L2 (architecture) → L3 (code)
- Trace data flow before proposing changes

## 4. Code Review Protocol

See `/code-review` skill for multi-reviewer Pattern H review.

For non-trivial changes (>50 lines, multiple modules, critical paths):
1. Spawn 4 parallel reviewers (logic, concurrency, tests, security)
2. Each reviewer stays in their lane
3. Synthesize: worst individual verdict = overall verdict
4. BLOCKING findings must be resolved before merge

## 5. Session Management

- Start each session with `/session-health`
- End each session with `/handover`
- Handover captures volatile state that isn't in git or docs
- A cold reader should be able to resume from the handover alone

## 6. Documentation Requirements

| Trigger | Required Doc Updates |
|---------|---------------------|
| Any code change | `docs/change_log.md` |
| Audit decision | `docs/ai_activity_log.md` |
| Schema/interface change | Relevant spec doc |
| User-facing change | `README.md` |
| Bug fix | Inline `# BUG-XXX` comment at fix site |
| Session end | `docs/handover/HANDOVER_<date>_<slug>.md` |

## 7. Git Workflow

- All development on `main` (no feature branches unless explicitly requested)
- Commit early, commit often — each logical unit gets its own commit
- Never force-push to `main`
- Worktree branches (`claude/*`) are ephemeral — merge immediately when done
