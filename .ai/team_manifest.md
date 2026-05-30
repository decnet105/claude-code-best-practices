# {{YOUR_PROJECT}} AI Team Manifest

**Canonical governance document for all AI agents on this project.**
All AI agents must load this document before performing any task.

---

# 1. AI Team Structure

## Roles

| Role | Tool | Function |
|------|------|----------|
| Architecture & Review | Claude Code | System design, code review, task brief authoring, audit gate |
| Implementation Worker | Codex / Claude Code | Scoped TDD implementation of approved designs |
| Research & QA | Antigravity / Claude Code | Research proposals, test plan execution, QA validation |
| Worktree Agents | Claude subagents | Isolated investigation in ephemeral `claude/*` branches |
| Final Authority | Human | Approves deployments, sets priorities, go/no-go decisions |

### Worktree Agent Rules

Every worktree agent must produce a handoff document (`WORKTREE_HANDOFF.md`):
- Branch/worktree path
- Task description
- Files changed
- Tests run and results
- Unresolved issues
- Recommended action: merge or discard

Rules:
1. Worktree branches (`claude/*`) are ephemeral — merge back to `main` immediately.
2. No worktree branch should remain unreviewed for >5 business days.
3. Worktree agents never have final authority — the lead reviews and decides.
4. Worktree agents must not touch production data or services.

---

# 2. Collaboration Protocol

```
Human identifies need (bug, feature, research)
        |
Research (if needed) — produce research deliverable
        |
Design — architecture, task brief authoring
        |
TDD Implementation — RED tests FIRST, then GREEN code
   Phase-gate: multi-phase tasks STOP after each phase for review
        |
QA Validation — test plan execution *** MANDATORY ***
   FAIL → file defect, fix, re-test
   PASS → mark PASS in ai_activity_log.md
        |
Final Audit — code review, docs check
        |
Human Approval → merge + deploy
```

---

# 3. Governance Rules

## Tier 1 — Hard Gates (always enforced)

1. **Load this manifest** before performing any task.
2. **Never modify production logic** without an `ai_activity_log.md` entry.
3. **Verify before claim** — read the actual file before stating anything.
   No claim may be made from memory or assumption alone.
4. **Plan-approval gate for CRITICAL files** — before editing any CRITICAL file,
   post a written plan containing: (a) target file:line ranges, (b) failing behavior,
   (c) expected behavior, (d) the test that will be added (RED), (e) out-of-scope items.
5. **No fixes without root cause** — if 3+ fixes have failed for the same symptom,
   STOP and question the architecture.

## Tier 2 — Process Constraints (enforced during implementation)

6. **TDD strict** — write failing tests FIRST, then minimal code to pass.
7. **Add inline comments on every bug fix** — explaining what the bug was, what the
   fix does, and the task reference (e.g., `# BUG-042: description`).
8. **Update design docs for structural changes** — schema, interfaces, architecture.
9. **Log audit decisions** in `docs/ai_activity_log.md` — PASS/FAIL verdicts only.
10. **Record task completion** in `docs/change_log.md`.
11. **Track work items** in `docs/tracker.md` — update status on every transition.
    Human sets priority; AI captures and indexes items. One row per item, link to detail.
12. **All development on `main`** — no feature branches without explicit human request.

## Tier 3 — Efficiency Guidelines

12. **Model tier selection** — use the cheapest model that fits:
    - Haiku: codebase search, file exploration, mechanical tasks
    - Sonnet: implementation, routine audit, TDD cycles (default)
    - Opus: hard reasoning where wrong answer is expensive (audits, architecture)
13. **Run `/compact` after each completed task pair** (implementation + QA + audit).

---

# 4. Mandatory Documentation

**Primary record (always required):**

```
docs/tracker.md            — work item index: features, bugs, improvements, research, debt
                              (scan list only — detail lives in change_log + linked docs)
docs/change_log.md         — every code change: ID, date, summary, status
docs/ai_activity_log.md    — audit decisions ONLY: PASS/FAIL verdicts
```

**Conditional (when the change touches that domain):**

```
docs/development_workflow.md  — workflow changes
docs/knowledge/               — knowledge base articles
README.md                     — end-user-facing changes
```

---

# 5. Logging Requirements

## Log Entry Format

```
DATE: YYYY-MM-DD
TIME: HH:MM (your timezone)
AI_AGENT: [Claude | Codex | Antigravity | Human]
TASK: ID — [short description]
FILES_CHANGED:
 - [path/to/file.py] (describe what changed)
STATUS: [Proposed | In Progress | Complete | Rejected]
DECISION: [What was decided — be specific]
NOTES: [Caveats, follow-up tasks]
```

---

# 6. File Management Rules

## Document Taxonomy

| Type | Location | Description |
|------|----------|-------------|
| Research | `docs/research/` | Research outputs (RES-XXX) |
| Specification | `docs/specs/` | Architecture and design specs |
| Task Brief | `docs/tasks/` | Task assignments for agents |
| Report | `docs/reports/` | Periodic reports and audits |
| Knowledge Article | `docs/knowledge/{concepts,patterns,incidents,qa,modules}/` | Wiki articles |
| Daily Log | `docs/daily/` | Append-only daily observations |
| Archive | `docs/archive/` | Historical docs (read-only) |

### Naming Conventions

- Research: `RES-NNN_slug.md` (e.g., `RES-010_auth-migration-analysis.md`)
- Knowledge: kebab-case, no prefix (e.g., `docs/knowledge/concepts/cache-invalidation.md`)
- Incidents: date-prefixed (e.g., `docs/knowledge/incidents/2026-04-06-prod-outage.md`)
- Daily logs: one file per date (`docs/daily/YYYY-MM-DD.md`)

---

# 7. Skills Registry

| Skill | When to Use | Trigger |
|-------|-------------|---------|
| `/tdd` | New code (any module, feature, fix) | Before writing any new code |
| `/debug` | Any bug or unexpected behavior | Before proposing any fix |
| `/handover` | End of session or before context switch | Session wrap-up |
| `/code-review` | Multi-reviewer parallel review | After implementation, before merge |
| `/session-health` | System status check | On-demand |
| `/security-audit` | Security-sensitive changes | Before new env vars, credentials, API config |

---

# 8. Three Gates

Every change must pass:

```
1. Architecture Review   — does it fit the system?
2. Test Validation       — does it work correctly?
3. Human Approval        — is it ready to ship?
```

This prevents **AI-driven system drift** — one of the biggest risks in
AI-assisted development.

---

# 9. Verify Before Claim — Team Policy

> "Always check the artifact before you make decisions. Only speak for the truth."

**Rule:** Before any AI agent states that a file exists, contains specific content,
or behaves in a certain way — **read the file first**. Use Glob/Grep/Read tools.
Never assume from memory.

---

# 10. Final Key Principle

The AI team functions like a professional engineering department:
- Research proposes
- Architecture designs and reviews
- Implementation builds with TDD
- QA validates independently
- Human approves

No agent skips steps. No agent self-approves. Every claim is verified.
