# Getting Started Guide

**A step-by-step guide to set up Claude Code governance for your project.**

This guide walks through a real example: setting up a swim team tracking app
called **swim-app** on the D:\ drive. By the end, you'll have an AI coding
assistant that follows rules, writes tests before code, keeps a changelog,
and won't break your production files during important hours.

---

## What You're Setting Up

Think of this like giving your AI assistant a **playbook** — a set of rules
and tools so it works the way a professional software team would:

- **CLAUDE.md** — the rulebook that loads every time you start a session
- **A safety hook** — a guard that blocks editing important files at bad times
- **Skills** — special commands like `/tdd` (test first, code second) and
  `/debug` (find the real problem before trying fixes)
- **A tracker** — a simple list of features to build and bugs to fix
- **A changelog** — a record of every change and why it was made

---

## Step 1: Get the Template

Open a terminal (PowerShell or Command Prompt) and run:

```powershell
# Clone the template from GitHub into your project folder
git clone https://github.com/decnet105/claude-code-best-practices.git D:\swim-app

# Go into your new project
cd D:\swim-app

# Remove the template's git history so you start fresh
Remove-Item -Recurse -Force .git

# Start your own git history
git init
```

> **Note:** If the repo is private, make sure you're logged in to GitHub
> on this computer first. Run `gh auth login` if you haven't already.

---

## Step 2: Edit CLAUDE.md (The Rulebook)

Open `D:\swim-app\CLAUDE.md` in any text editor. Find the placeholder lines
and replace them with your project info:

**Find this:**
```
# {{YOUR_PROJECT}} — Claude Code Project Instructions
```

**Change to:**
```
# swim-app — Claude Code Project Instructions
```

**Find this:**
```
├── src/                    # Application source code
│   ├── {{PROD_DIR}}/       # Production code (protected by safety gate)
```

**Change to:**
```
├── src/                    # Application source code
│   ├── app/                # Main swim-app code
```

**Find this:**
```bash
{{TEST_COMMAND}}   # e.g., python -m pytest tests/ -x -q
```

**Change to whatever test command your project uses**, for example:
```bash
python -m pytest tests/ -x -q       # If using Python
npm test                             # If using JavaScript
```

---

## Step 3: Set Up the Safety Hook

The safety hook stops the AI from editing important files at times you choose
(like during a swim meet when you don't want the app to break!).

Open `D:\swim-app\.claude\hooks\production_safety_gate.py` and edit the
config section near the top:

```python
# Files that should be protected during meets/events
PROTECTED_PATTERNS = [
    "src/app/timer.py",          # The race timer — never break this!
    "src/app/scoreboard.py",     # Live scoreboard display
    "src/app/meet_manager.py",   # Meet scheduling logic
]

# Your timezone
TIMEZONE = "America/New_York"

# Block edits during swim meets (Saturday mornings, for example)
PROTECT_START_HOUR = 7
PROTECT_START_MINUTE = 0
PROTECT_END_HOUR = 14
PROTECT_END_MINUTE = 0

# Which days to protect (0=Monday, 5=Saturday, 6=Sunday)
PROTECTED_DAYS = {5, 6}  # Weekends only
```

If you don't need the safety hook yet, that's fine — just leave the
`PROTECTED_PATTERNS` list empty and it won't block anything.

---

## Step 4: Set Up the Tracker

Open `D:\swim-app\docs\tracker.md`. Clear the placeholder row and add your
first items:

```markdown
## Open Items

| ID | Type | Priority | Summary | Status | Owner | Blocked By | Updated |
|----|------|----------|---------|--------|-------|------------|---------|
| FEAT-001 | feature | P1 | Swimmer profile page with times and PBs | OPEN | — | — | 2026-05-30 |
| FEAT-002 | feature | P2 | Race timer with lane assignments | OPEN | — | FEAT-001 | 2026-05-30 |
| FEAT-003 | feature | P2 | Meet schedule calendar view | OPEN | — | — | 2026-05-30 |
| FEAT-004 | feature | P3 | Export times to CSV for coach | OPEN | — | — | 2026-05-30 |
| BUG-001 | bug | P1 | App crashes when swimmer has no times yet | OPEN | — | — | 2026-05-30 |
```

**Priority guide:**
- **P0** = Emergency — the app is broken and people need it NOW
- **P1** = Must do next — the most important things to build
- **P2** = Should do soon — important but can wait a bit
- **P3** = Nice to have — do it when you have time
- **P4** = Backlog — just an idea for later

---

## Step 5: Make Your First Commit

```powershell
cd D:\swim-app
git add -A
git commit -m "Initial setup: swim-app with Claude Code governance"
```

---

## Step 6: Start Using Claude Code

Open Claude Code in your project folder:

```powershell
cd D:\swim-app
claude
```

Claude will automatically read your `CLAUDE.md` and follow the rules you set
up. Here's how to use the skills:

### Building a New Feature

Tell Claude what you want, and it will follow the TDD process:

```
You: Build the swimmer profile page. It should show name, age, and a list
     of their best times by event (50 free, 100 back, etc.)
```

Claude will:
1. Ask you to confirm the behaviors to test
2. Write a failing test first (RED)
3. Write just enough code to pass that test (GREEN)
4. Repeat for each behavior
5. Update the tracker and changelog when done

Or invoke TDD explicitly:

```
You: /tdd
```

### Fixing a Bug

Always use `/debug` before trying to fix anything:

```
You: /debug
     The app crashes when I open a swimmer who hasn't swum any races yet.
```

Claude will:
1. Classify the problem (is it a code bug? a missing feature? a config issue?)
2. Read the error message and trace it to the source
3. Find the root cause BEFORE writing any fix
4. Write a test that reproduces the bug, then fix it

### Ending Your Session

When you're done for the day:

```
You: /handover
```

Claude will write a handover document so you (or Claude in a new session)
can pick up exactly where you left off tomorrow.

### Checking the Code

After building something big, run a code review:

```
You: /code-review
```

This launches 4 reviewers in parallel, each checking a different thing:
- Is the logic correct?
- Is it fast and safe for multiple users?
- Are there enough tests?
- Are there any security issues?

### Quick Health Check

```
You: /session-health
```

Shows you the state of your git repo, test results, and any alerts.

---

## How the Files Work Together

Here's the big picture of what each file does:

```
D:\swim-app\
│
├── CLAUDE.md                    YOU edit this once. Claude reads it every
│                                session to know your project's rules.
│
├── .claude\settings.json        Controls what Claude is allowed to do
│                                (which commands, which tools).
│
├── .claude\hooks\               The "guard" — blocks editing important
│   └── production_safety_gate.py  files at times you set.
│
├── .claude\commands\            Skills — type /tdd, /debug, /handover
│   ├── tdd.md                   etc. in Claude to use them.
│   ├── debug.md
│   ├── handover.md
│   ├── code-review.md
│   ├── session-health.md
│   └── security-audit.md
│
├── .claude\agents\              Helper reviewers that Claude can call
│   ├── review-logic-correctness.md      for parallel code review.
│   ├── review-concurrency-performance.md
│   ├── review-test-coverage-style.md
│   └── review-security-risk.md
│
├── .ai\team_manifest.md         The full governance rulebook
│                                (roles, rules, logging format).
│
├── docs\
│   ├── tracker.md               YOUR feature & bug list (like a to-do
│   │                            list for the whole project).
│   ├── change_log.md            History of every change made.
│   ├── ai_activity_log.md       Record of AI review decisions.
│   ├── development_workflow.md  How the development process works.
│   ├── handover\                Session handover docs go here.
│   └── knowledge\               Your project's "wiki" — things you
│       ├── concepts\            learned along the way.
│       ├── patterns\
│       ├── incidents\
│       ├── modules\
│       └── qa\
│
└── src\                         YOUR actual code goes here.
    ├── app\                     (this is what you're building!)
    └── tests\
```

---

## The 6 Rules to Remember

These are the most important rules. Claude follows them automatically, but
it helps to know them:

1. **Test first, code second** — Claude writes a test that fails, THEN writes
   the code to make it pass. This catches bugs before they happen.

2. **Verify before claiming** — Claude must read the actual file before saying
   what's in it. No guessing.

3. **Find the real problem first** — when something breaks, Claude must figure
   out WHY before trying to fix it. No random guessing.

4. **Small changes only** — each change should be as small as possible. Don't
   rewrite everything at once.

5. **Write it down** — every change goes in the changelog. Every big decision
   goes in the activity log.

6. **Human is the boss** — Claude suggests, you decide. Claude never deploys
   or makes final decisions without your OK.

---

## Tips

- **Start small.** You don't need to use every feature on day one. Start with
  just `CLAUDE.md` and `/tdd`. Add the other skills as you get comfortable.

- **The tracker is your command center.** When you sit down to work, open
  `docs/tracker.md` first to see what's next.

- **Handovers save time.** If you run `/handover` before closing Claude, your
  next session starts 10x faster because Claude knows exactly where you left off.

- **Don't be afraid to edit the rules.** `CLAUDE.md` and the team manifest are
  YOUR rules. If something isn't working, change it.

- **Git is your undo button.** Every commit is a save point. If something goes
  wrong, you can always go back: `git log --oneline` to see your history,
  `git checkout <hash> -- <file>` to restore a specific file.

---

## Example Session

Here's what a real session might look like:

```
You: /session-health
Claude: [shows git state, test results, no alerts — HEALTHY]

You: Let's work on FEAT-001, the swimmer profile page.

You: /tdd
Claude: OK, let's plan the behaviors:
        1. When I view a swimmer, I see their name and age
        2. When a swimmer has times, I see them listed by event
        3. When a swimmer has no times, I see "No times recorded yet"
        4. When I add a new time, it appears in the list
        Does this look right?

You: Yes, let's go.
Claude: [writes test_swimmer_profile_shows_name_and_age — RED, fails]
Claude: [writes minimal code — GREEN, passes]
Claude: [writes test_swimmer_with_times_shows_list — RED, fails]
Claude: [writes code — GREEN, passes]
        ... (repeats for each behavior)
Claude: All 4 tests passing. Full suite: 4 passed, 0 failed.
        Updated tracker: FEAT-001 → DONE.
        Updated change_log with details.

You: /handover
Claude: [writes docs/handover/HANDOVER_2026-05-30_swimmer-profile.md]
        Done. Next session can pick up from FEAT-002 (race timer).
```

---

That's it! You now have a professional-grade AI development setup. Have fun
building swim-app!
