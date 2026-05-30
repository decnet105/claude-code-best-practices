# Security Audit

Detect insecure defaults, hardcoded secrets, weak auth, and permissive security
configurations that could allow apps to run insecurely in production.

## When to Use

- Before any new env var, credential handling, or API config change
- When adding authentication or authorization logic
- When modifying file permissions or access controls
- Periodic security sweep

## Checklist

### 1. Hardcoded Secrets

```bash
# Search for potential hardcoded secrets
grep -rn "password\s*=" --include="*.py" --include="*.js" --include="*.ts" .
grep -rn "api_key\s*=" --include="*.py" --include="*.js" --include="*.ts" .
grep -rn "secret\s*=" --include="*.py" --include="*.js" --include="*.ts" .
grep -rn "token\s*=" --include="*.py" --include="*.js" --include="*.ts" .
```

Verify: all secrets come from environment variables, not literals.

### 2. Environment Variable Defaults

Check that env var fallbacks are SAFE defaults (fail-closed):

```python
# BAD — fail-open default
DEBUG = os.getenv("DEBUG", "true")
AUTH_REQUIRED = os.getenv("AUTH_REQUIRED", "false")

# GOOD — fail-closed default
DEBUG = os.getenv("DEBUG", "false")
AUTH_REQUIRED = os.getenv("AUTH_REQUIRED", "true")
```

### 3. File Permissions

```bash
# Check for world-readable sensitive files
find . -name ".env*" -o -name "*.pem" -o -name "*.key" | head -20
```

### 4. Debug Features in Production

Check for debug endpoints, verbose logging of sensitive data, or development-only
features that could leak to production.

### 5. Input Validation

- SQL injection: parameterized queries used everywhere?
- XSS: output encoding applied?
- Command injection: no `os.system()` with user input?
- Path traversal: no unsanitized file paths from user input?

### 6. Dependency Security

```bash
# Check for known vulnerabilities (language-specific)
# Python: pip audit
# Node: npm audit
# Go: govulncheck
```

## Report Format

```
## Security Audit — YYYY-MM-DD

| Category | Status | Findings |
|----------|--------|----------|
| Hardcoded secrets | PASS/FAIL | <count found> |
| Env var defaults | PASS/FAIL | <fail-open count> |
| File permissions | PASS/FAIL | <issues> |
| Debug features | PASS/FAIL | <issues> |
| Input validation | PASS/FAIL | <issues> |
| Dependencies | PASS/FAIL | <vulnerability count> |

**Overall: SECURE / ISSUES_FOUND / CRITICAL**
```
