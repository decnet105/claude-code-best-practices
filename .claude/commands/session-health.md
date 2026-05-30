# Session Health Check

Quick diagnostic of the current project and development environment state.

## When to Use

- Start of a working session
- After deploying changes
- When something feels off
- On-demand status check

## Checks

Run these diagnostics and report results:

### 1. Git State

```bash
echo "=== branch + HEAD ==="
git branch --show-current && git rev-parse --short HEAD

echo "=== uncommitted changes ==="
git status --short | head -20

echo "=== recent commits ==="
git log --oneline -5
```

### 2. Test Suite

```bash
echo "=== test results ==="
{{TEST_COMMAND}}
```

### 3. Alert Pickup

```bash
echo "=== alerts ==="
if [ -f data/runtime/ALERT_FOR_CLAUDE.json ]; then
  cat data/runtime/ALERT_FOR_CLAUDE.json
else
  echo "No active alerts"
fi
```

### 4. Documentation State

```bash
echo "=== recent change_log entries ==="
head -30 docs/change_log.md

echo "=== recent activity log ==="
tail -20 docs/ai_activity_log.md
```

## Report Format

```
## Session Health — YYYY-MM-DD HH:MM

| Check | Status | Detail |
|-------|--------|--------|
| Git state | OK/WARN | <branch, uncommitted count> |
| Test suite | OK/FAIL | <pass/fail counts> |
| Alerts | CLEAR/ACTIVE | <alert summary if active> |
| Docs | OK/STALE | <last change_log date> |

**Overall: HEALTHY / DEGRADED / CRITICAL**

**Recommended action:** <what to do next>
```
