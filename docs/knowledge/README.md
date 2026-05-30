# Knowledge Base

Two-tier knowledge system for accumulating project wisdom.

## Tier 1 — Daily Logs (`docs/daily/`)

Append-only raw observations, hypotheses, and ad-hoc notes.
- One file per date: `YYYY-MM-DD.md`
- Any agent can append
- Never rewrite history — append only

## Tier 2 — Knowledge Articles (`docs/knowledge/`)

Compiled, cross-linked wiki articles distilled from Tier 1 logs.

### Categories

| Directory | Content | Example |
|-----------|---------|---------|
| `concepts/` | Domain concepts and definitions | `cache-invalidation.md` |
| `patterns/` | Recurring solutions and approaches | `retry-with-backoff.md` |
| `incidents/` | Post-mortems (date-prefixed) | `2026-04-06-prod-outage.md` |
| `modules/` | Module documentation | `auth-middleware.md` |
| `qa/` | QA procedures and checklists | `deployment-checklist.md` |

### Article Format

Every knowledge article uses this frontmatter:

```yaml
---
type: concept | pattern | incident | qa | module
status: draft | active | archived
updated: YYYY-MM-DD
---
```

### Naming

- **kebab-case**, no prefix, no underscores, no CamelCase
- **incidents/** — prefix with date: `YYYY-MM-DD-<slug>.md`
- **modules/** — slug matches the source filename without extension

### Promotion Flow

```
Daily log observation → Pattern emerges across multiple days →
Write/update Tier 2 article → Cross-link related articles
```

## Usage

- Session start: scan `README.md` for recently updated articles
- When debugging: check `incidents/` for similar past issues
- When implementing: check `patterns/` for established approaches
- When onboarding: read `concepts/` for domain knowledge
