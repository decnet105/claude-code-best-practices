# Claude Code Best Practices

A production-hardened governance template for AI-assisted software development
with [Claude Code](https://docs.anthropic.com/en/docs/claude-code).

Battle-tested on a live trading system (2000+ commits, 3500+ tests, 5 AI agents)
over 3 months of daily production use.

## What This Is

A ready-to-fork repo structure that gives your Claude Code project:

- **Governance manifest** — rules, roles, and workflows for AI agents
- **CLAUDE.md** — project instructions loaded automatically every session
- **Safety hooks** — PreToolUse hooks that block dangerous edits (e.g., during
  production hours)
- **Skills (slash commands)** — `/tdd`, `/debug`, `/handover`, `/code-review`,
  `/session-health`, `/security-audit`
- **Subagent definitions** — specialized reviewers for parallel code review
- **Memory system** — persistent cross-session context with typed memories
- **Documentation taxonomy** — where every type of document lives
- **Development workflow** — TDD-first, phase-gated, audit-trailed

## Quick Start

1. Fork or copy this repo into your project
2. Edit `CLAUDE.md` — replace `{{YOUR_PROJECT}}` placeholders with your project details
3. Edit `.ai/team_manifest.md` — define your AI team roles
4. Edit `.claude/hooks/production_safety_gate.py` — set your protected files and hours
5. Edit `.claude/settings.json` — configure permissions and hooks
6. Start a Claude Code session — governance loads automatically

```bash
# Clone into your project folder (replace YOUR_PROJECT with your app name)
git clone https://github.com/decnet105/claude-code-best-practices.git YOUR_PROJECT
cd YOUR_PROJECT

# Remove template history and start fresh
rm -rf .git   # On Windows: Remove-Item -Recurse -Force .git
git init

# Edit CLAUDE.md, .ai/team_manifest.md, .claude/settings.json
# Then open Claude Code in this directory
```

> See [GETTING_STARTED.md](GETTING_STARTED.md) for a beginner-friendly
> walkthrough with a concrete example.

## Repo Structure

```
.
├── CLAUDE.md                          # Project instructions (auto-loaded)
├── .ai/
│   └── team_manifest.md               # Governance manifest (roles, rules, logging)
├── .claude/
│   ├── settings.json                  # Permissions + hook config
│   ├── hooks/
│   │   └── production_safety_gate.py  # PreToolUse hook (blocks edits during prod hours)
│   ├── commands/                      # Skills (slash commands)
│   │   ├── tdd.md                     # /tdd — Test-Driven Development
│   │   ├── debug.md                   # /debug — Systematic Debugging
│   │   ├── handover.md                # /handover — Session Handover
│   │   ├── code-review.md             # /code-review — Multi-reviewer code review
│   │   ├── session-health.md          # /session-health — System health check
│   │   └── security-audit.md          # /security-audit — Security review
│   └── agents/                        # Subagent definitions
│       ├── review-logic-correctness.md
│       ├── review-concurrency-performance.md
│       ├── review-test-coverage-style.md
│       └── review-security-risk.md
├── docs/
│   ├── tracker.md                     # Work item index (features, bugs, debt)
│   ├── change_log.md                  # Code change history
│   ├── ai_activity_log.md             # AI audit decisions (PASS/FAIL only)
│   ├── development_workflow.md        # End-to-end dev lifecycle
│   ├── knowledge/                     # Two-tier knowledge base
│   │   ├── README.md
│   │   ├── concepts/                  # Domain concepts
│   │   ├── patterns/                  # Recurring patterns
│   │   ├── incidents/                 # Post-mortems
│   │   ├── modules/                   # Module documentation
│   │   └── qa/                        # QA procedures
│   ├── daily/                         # Append-only daily logs
│   ├── research/                      # Research outputs (RES-XXX)
│   ├── specs/                         # Architecture specs
│   ├── tasks/                         # Agent task briefs
│   ├── reports/                       # Periodic reports
│   ├── handover/                      # Session handover docs
│   └── archive/                       # Historical docs (read-only)
└── .gitignore
```

## Core Principles

These are the principles that survived 3 months of daily production use:

1. **TDD strict** — write failing tests FIRST. No exceptions.
2. **Verify before claim** — read the actual file before stating anything.
3. **No fixes without root cause** — diagnose first, fix second. 3-fix threshold
   forces architecture rethink.
4. **Minimize blast radius** — smallest viable change surface. No "while I'm here"
   improvements.
5. **Log audit decisions** — PASS/FAIL verdicts, not routine steps.
6. **Think before coding** — understand the architecture before touching it.

## Adapting for Your Project

The template is domain-agnostic. Replace:

| Placeholder | Example |
|-------------|---------|
| `{{YOUR_PROJECT}}` | `my-saas-app` |
| `{{PROTECTED_FILES}}` | `src/billing/`, `src/auth/` |
| `{{PROTECTED_HOURS}}` | Business hours, deploy windows, etc. |
| `{{TEST_COMMAND}}` | `npm test`, `cargo test`, `python -m pytest` |
| `{{PROD_DIR}}` | `src/`, `app/`, `lib/` |

## License

MIT — use freely, adapt to your needs.
