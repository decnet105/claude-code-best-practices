# Session Handover

Produce a complete, self-contained session handover so a FRESH session (new
Claude window or different agent) can resume exactly where this one left off
**without reading the transcript**.

**When to use:** at the end of a working session, before context gets long, or
any time the operator says "handover" or before a model/context switch.

**Output:** `docs/handover/HANDOVER_<YYYY-MM-DD>_<slug>.md` (slug = 2-4 word
session theme).

**Guiding principle:** the committed `change_log.md` / `ai_activity_log.md`
already hold the durable record — DO NOT duplicate them. The handover's job is
the **session-only state**: in-flight threads, decisions, what's pending, and
the prioritized next move.

---

## Steps

### 1. Gather durable state

```bash
echo "=== git HEAD + branch ==="
git rev-parse --short HEAD && git branch --show-current

echo "=== commits THIS session ==="
git log --since="8 hours ago" --pretty=format:"%h %s" | head -20

echo "=== working tree (uncommitted) ==="
git status --short | head -20
```

### 2. Gather volatile state (session-only knowledge)

From your own session memory (NOT in any file):
- **Config changes pending a restart** — deployed in code, not yet live
- **In-flight threads** — background tasks, awaiting review, running sweeps
- **Decisions/verdicts** made this session and their evidence

### 3. Test / QA status

Cite results you already produced this session. Do not re-run the full suite
just for the handover. If none were run, say so explicitly.

### 4. Write the handover doc

Write `docs/handover/HANDOVER_<date>_<slug>.md` using the template below.

---

## Handover Document Template

```markdown
# Session Handover: <session theme>

**Date:** <YYYY-MM-DD HH:MM>
**Outgoing session focus:** <one line>
**Git HEAD:** `<short-hash>` (main)
**Suite state:** <e.g. "142 passed / 0 failed" or "not run this session">

---

## 0. TL;DR (read this first)
<3-5 lines: what shipped, the single most important pending thing, and any
action required RIGHT NOW.>

## 1. What shipped this session (commits)
| Commit | What |
|--------|------|
| `<hash>` | <one line> |

## 2. Decisions & verdicts
- <AUDIT PASS/FAIL, config promotion, etc.> — evidence: <ref>

## 3. System state (volatile — verify before trusting)
- **Pending a restart:** <config flags deployed but not live yet>

## 4. In-flight threads (do not drop)
- <background task running, awaiting review, etc.>

## 5. Next steps (prioritized)
| Pri | Item | Gate / blocker |
|-----|------|----------------|
| P0  | <...> | <...> |

## 6. Operator action items (needs the human)
- <restart service, approve X, decide Y>

## 7. Risks & honest gaps
- <what was NOT verified; what could bite the next session>

## 8. Canonical record pointers
- change_log.md: <newest IDs>
- ai_activity_log.md: <newest dated entries>
```

---

## Quality Bar (self-check)

- [ ] A cold reader can resume from this doc + its links alone (no transcript)
- [ ] Every pending thread is named
- [ ] Decisions cite evidence
- [ ] No fabricated commit hashes — everything traceable
