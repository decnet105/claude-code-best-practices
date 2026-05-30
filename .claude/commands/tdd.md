# Test-Driven Development (TDD)

Enforce vertical-slice TDD for all new code changes. Follow the Red-Green-Refactor
cycle strictly.

## When To Use TDD

TDD is MANDATORY for:
- New features and modules
- Bug fixes to core logic
- New CLI commands or API endpoints
- New hooks or skills

TDD is NOT required for:
- Documentation-only changes
- Configuration changes (thresholds, env vars)
- Exploratory analysis scripts

## Phase 0: Root-Cause Layer Check (mandatory for bug fixes)

Before planning any fix, classify the problem:

```
ROOT CAUSE LAYER: [ ] L1-Infrastructure  [ ] L2-Architecture  [ ] L3-Code
EVIDENCE: <one sentence proving this is the right layer to fix>
```

- **L1 (Infrastructure):** External service limit, config, network — resolve at L1 first.
- **L2 (Architecture):** Components interact incorrectly — fix the design.
- **L3 (Code):** Isolated bug in a specific function — proceed with TDD.

**If this is the 3rd+ fix for the same symptom, STOP and re-evaluate at L1.**

## Phase 1: Planning (Before Writing Any Code)

1. **Confirm the feature with the user.** What observable behaviors should change?
2. **List behaviors to test** — not implementation steps, but user-visible outcomes:
   - "When input is empty, returns a 400 error with message"
   - "When called with valid data, creates a record and returns 201"
3. **Identify the public interface** — what function/command/endpoint will be called?
4. **Get user approval** on the behavior list before writing anything.

## Phase 2: Vertical Slice Loop (RED -> GREEN -> Repeat)

For EACH behavior, one at a time:

### Step A: RED — Write One Failing Test

```python
def test_empty_input_returns_400():
    """BUG-01: Empty input should return 400 with error message."""
    # Arrange
    # Act
    # Assert
```

Run the test to confirm it FAILS. If it passes without code changes, the test
is wrong — it's not testing new behavior.

### Step B: GREEN — Write Minimal Code to Pass

Write ONLY enough code to make this one test pass. Do NOT:
- Add features for future tests
- Refactor existing code
- Optimize or generalize

### Step C: Verify No Regressions

Run the full test suite to ensure nothing else broke.

### Step D: Move to Next Behavior

Go back to Step A with the next behavior.

## Phase 3: Refactor (Only After All Tests GREEN)

1. **Never refactor while RED.** Get to GREEN first.
2. Look for: duplicated code, long functions, constants to externalize.
3. After each refactor, run the full suite to confirm all tests still pass.

## Test Writing Rules

### DO:
- Test observable behavior through public interfaces
- Name tests by behavior: `test_when_X_then_Y()`
- Use real objects when possible (real DB, real objects, real engine)
- Test boundary conditions (exact thresholds, edge cases)

### DON'T:
- Don't test implementation details (private methods, internal state)
- Don't mock internals — use the real code path
- Don't write all tests first then all code (horizontal slicing = BAD)
- Don't anticipate future tests while writing current code

## Checklist Per Cycle

- [ ] Test describes behavior, not implementation
- [ ] Test uses public interface only
- [ ] Test would survive internal refactor
- [ ] Code is minimal for this test
- [ ] No speculative features added
- [ ] Full test suite still passes
