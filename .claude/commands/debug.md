# Systematic Debugging

Use when encountering any bug, test failure, or unexpected behavior BEFORE
proposing fixes.

## The Iron Law

```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

If you have not completed Phase 1, you cannot propose fixes.
If 3+ fixes have failed, STOP and question architecture (Phase 4 Step 5).

## When to Use

Use for ANY technical issue:
- Runtime errors or exceptions
- Test failures
- Unexpected behavior or stale data
- Performance degradation
- Integration failures

Use ESPECIALLY when:
- Under time pressure ("just one quick fix" seems obvious)
- You have already tried multiple fixes
- Previous fix did not work or introduced a new defect

## The Four Phases

### Phase 0: Three-Layer Classification (mandatory)

```
ROOT CAUSE LAYER: [ ] L1-Infrastructure  [ ] L2-Architecture  [ ] L3-Code
L1 CHECK: External services, config, network, disk, permissions?
L2 CHECK: Component interaction design correct?
L3 CHECK: Bug isolated to a specific function/line?
EVIDENCE: <one sentence proving the layer classification>
```

**If a metric is persistently degraded (>5 sessions), CHECK L1 FIRST.**
**If this is the 3rd+ fix for the same symptom, CHECK L1 FIRST.**

### Phase 1: Root Cause Investigation

BEFORE attempting ANY fix:

1. **Read Error Messages Carefully** — full stack traces, exact timestamps, error codes
2. **Reproduce Consistently** — can you trigger it reliably?
3. **Check Recent Changes** — `git log --oneline -10`, what changed?
4. **Trace Data Flow** — where does the bad value originate? Trace backward.
5. **Fix at the source, not at the symptom**

### Phase 2: Pattern Analysis

1. **Find Working Examples** — when did this same logic work? Compare.
2. **Compare Against References** — read specs, docs, expected interfaces.
3. **Identify Differences** — what changed between working and broken?

### Phase 3: Hypothesis and Testing

1. **Form Single Hypothesis** — "Root cause is X because evidence Y shows Z"
2. **Test Minimally** — smallest possible change, ONE variable at a time
3. **Verify** — did it fix it? If not, form NEW hypothesis with new evidence.
   Do NOT add more fixes on top.

### Phase 4: Implementation

1. **Create Failing Test Case** — TDD (RED -> GREEN)
2. **Implement Single Fix** — add inline comment at fix site
3. **Verify Fix** — run full test suite
4. **If Fix Does Not Work:**
   - Count: how many fixes tried?
   - If < 3: return to Phase 1 with new evidence
   - If >= 3: STOP — this is architectural, not a bug. Escalate to human.

## Red Flags — STOP and Return to Phase 1

If you catch yourself thinking:
- "Quick fix for now, investigate later"
- "Just try changing this threshold and see"
- "I don't fully understand but this might work"
- "One more fix attempt" (when already tried 2+)
- Each fix reveals a new problem in a different layer

## Quick Reference

| Phase | Key Activities | Success Criteria |
|-------|---------------|------------------|
| 0. Classify | L1/L2/L3 layer check | Know WHERE to look |
| 1. Root Cause | Read errors, reproduce, trace | Understand WHAT and WHY |
| 2. Pattern | Find working examples, compare | Identify differences |
| 3. Hypothesis | Form theory, test minimally | Confirmed or new hypothesis |
| 4. Implement | Create test, fix, verify | Bug resolved, tests pass |
