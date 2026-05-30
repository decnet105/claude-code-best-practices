# Project Tracker

Single-pane index of all features, bugs, and improvements. Detail lives
elsewhere (change_log, research docs, knowledge articles) — this file is
the **scan list** for "what's open, what's next, what's blocked."

Updated by AI agents after every status change. Human sets priority.

---

## Open Items

| ID | Type | Priority | Summary | Status | Owner | Blocked By | Updated |
|----|------|----------|---------|--------|-------|------------|---------|
| — | — | — | No open items yet | — | — | — | — |

## Recently Closed (last 30 days)

| ID | Type | Summary | Status | Closed | Detail |
|----|------|---------|--------|--------|--------|
| — | — | — | — | — | — |

---

## Field Reference

### ID Format

Use a prefix that matches the work type:

| Prefix | Meaning | Example |
|--------|---------|---------|
| `FEAT-NNN` | New feature | `FEAT-001` |
| `BUG-NNN` | Bug / defect | `BUG-042` |
| `IMP-NNN` | Improvement / refactor | `IMP-007` |
| `RES-NNN` | Research / investigation | `RES-003` |
| `DEBT-NNN` | Tech debt | `DEBT-012` |

### Type

`feature` | `bug` | `improvement` | `research` | `debt`

### Priority

| Priority | Meaning |
|----------|---------|
| `P0` | Drop everything — blocking production or critical path |
| `P1` | Must do this session/sprint |
| `P2` | Should do soon — important but not urgent |
| `P3` | Nice to have — do when capacity allows |
| `P4` | Backlog — captured so it's not lost |

### Status

| Status | Meaning |
|--------|---------|
| `OPEN` | Captured, not yet started |
| `IN_PROGRESS` | Actively being worked on |
| `IN_REVIEW` | Implementation done, awaiting review/QA |
| `BLOCKED` | Cannot proceed — see Blocked By column |
| `DONE` | Complete and verified |
| `WONT_DO` | Decided not to pursue — document reason in Detail |

### Owner

Who is responsible: `Human`, `Claude`, `Codex`, `Antigravity`, or a person's name.

### Blocked By

Reference to the blocking item (e.g., `FEAT-003`, `waiting for API access`,
`needs human decision`). Leave empty if not blocked.

### Detail

Link to the detailed record: `change_log.md#BUG-042`, `docs/research/RES-003_*.md`,
or a knowledge article path.

---

## How to Use

### Adding a new item

Append a row to the **Open Items** table with status `OPEN`. Assign an ID
using the next available number for that prefix. Set priority to `P4` unless
the human specifies otherwise — humans set priority, AI captures items.

### Moving to in-progress

Change status to `IN_PROGRESS`, set Owner, update the date.

### Closing an item

1. Change status to `DONE` (or `WONT_DO`)
2. Move the row from **Open Items** to **Recently Closed**
3. Add the Closed date and a Detail link
4. Update `docs/change_log.md` with the completion entry

### Monthly cleanup

Move items older than 30 days from **Recently Closed** to the archive
(or delete them — the detail is preserved in change_log and git history).

---

## Rules

1. **One row per item.** No sub-tasks here — break those out as separate items
   or track them in the detail doc.
2. **Human sets priority.** AI agents may suggest priority but must not override
   human-set values.
3. **Keep it scannable.** Summaries are one line, max ~80 chars. Detail goes
   in the linked doc.
4. **Update on every status change.** Don't batch updates — change the row
   when the status actually changes.
5. **Don't duplicate change_log.** This is an index, not a record. The row
   points to the record.
