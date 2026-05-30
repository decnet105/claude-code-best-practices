# {{YOUR_PROJECT}} — Claude Code Project Instructions

These instructions are loaded automatically by every Claude Code session
(including spawned tasks and worktree sessions).

## Git Workflow

**All development happens on `main`.** No feature branches unless explicitly
requested by a human AND the change spans multiple days.

- Commit directly to `main`. Do NOT run `git checkout -b` or `git switch -c`.
- Worktree branches (`claude/*`) created by spawn_task are ephemeral — merge
  back to `main` immediately when done.
- **Self-rejection trigger:** if you are about to create a branch without an
  explicit human instruction, STOP and commit to `main` instead.

## Session Start — Mandatory Reads

1. `.ai/team_manifest.md` — governance manifest (roles, rules, logging)
2. `docs/development_workflow.md` — TDD, skills, testing workflow
3. `docs/knowledge/README.md` — knowledge base index

## Alert Pickup — Check Before Anything Else

Read `data/runtime/ALERT_FOR_CLAUDE.json`. If it exists, surface the alert
to the user FIRST, before any other work.

## Operating Principles

1. **Think before coding** — understand existing architecture, identify affected
   systems, downstream consumers, invariants, failure modes, and rollback strategy
   before writing any code. For CRITICAL files, post a written plan first.
2. **Simplicity first** — prefer fewer abstractions, explicit code, composable
   functions, predictable data flow. 100 clean lines > 1000 abstract lines.
3. **Existing patterns win** — inspect surrounding code before creating new patterns.
   Reuse established conventions. Preserve architectural consistency.
4. **Minimize blast radius** — limit changes to smallest viable surface area,
   smallest viable dependency set, smallest viable behavioral delta. No
   unrelated refactors in the same commit.

## Key Rules (from governance manifest)

1. **TDD strict** — write failing tests FIRST (RED), then code (GREEN). Never code-first.
2. **Verify before claim** — read the actual file before stating anything. No claims
   from memory or assumption.
3. **No fixes without root cause** — diagnose first, fix second.
4. **Production safety gate** — do NOT edit protected production files during
   protected hours. The PreToolUse hook enforces this.
5. **Log audit decisions** in `docs/ai_activity_log.md` — PASS/FAIL verdicts only.
6. **Record task completion** in `docs/change_log.md`.

## Forbidden Behaviors

Never:
- Pretend tests passed without running them
- Mark incomplete work as done
- Fabricate execution results or file contents
- Invent files, functions, or APIs that don't exist
- Assume behavior without checking (verify before claim)
- Ignore test output or compiler errors
- Silently overwrite user work
- Patch symptoms without diagnosing root cause

If uncertain: say what is uncertain, explain why, propose verification steps.

## Communication Rules

When finishing work:
- Summarize what changed and why
- List tradeoffs made
- List risks and unverified assumptions
- List follow-up work needed
- Do not claim certainty without verification

## Project Structure

```
{{YOUR_PROJECT}}/
├── src/                    # Application source code
│   ├── {{PROD_DIR}}/       # Production code (protected by safety gate)
│   └── ...
├── tests/                  # Test suite
├── docs/                   # Documentation
│   ├── change_log.md       # Code change history
│   ├── ai_activity_log.md  # AI audit decisions
│   └── knowledge/          # Two-tier knowledge base
├── .ai/                    # AI governance
│   └── team_manifest.md    # Roles, rules, workflow
└── .claude/                # Claude Code configuration
    ├── settings.json       # Permissions + hooks
    ├── commands/           # Skills (slash commands)
    ├── hooks/              # Safety hooks
    └── agents/             # Subagent definitions
```

## Testing

```bash
{{TEST_COMMAND}}   # e.g., python -m pytest tests/ -x -q
```

## Full Governance

See `.ai/team_manifest.md` for the complete governance manifest, team roles,
documentation requirements, and workflow patterns.
