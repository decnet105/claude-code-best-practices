# Getting Started Guide

**A step-by-step guide to set up Claude Code governance for your project.**

This guide walks through a real example: building an iPhone swim team app
called **swim-app** on the D:\ drive, using a development stack of:

- **GitHub** — stores your code and syncs between devices
- **ngrok** — lets your iPhone reach your local dev server over the internet
- **Sideloadly** — installs your app on a real iPhone without the App Store

By the end, you'll have an AI coding assistant that follows rules, writes
tests before code, keeps a changelog, and won't break your app during
swim meets.

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

## Prerequisites

Before you start, make sure you have these installed:

| Tool | What It Does | Get It From |
|------|-------------|-------------|
| **Git** | Tracks your code changes | [git-scm.com](https://git-scm.com) |
| **GitHub CLI (`gh`)** | Manages GitHub repos from the terminal | [cli.github.com](https://cli.github.com) |
| **Claude Code** | Your AI coding assistant | [claude.ai/claude-code](https://claude.ai/claude-code) |
| **Node.js** | Runs your app's dev server | [nodejs.org](https://nodejs.org) |
| **ngrok** | Tunnels your local server to the internet | [ngrok.com](https://ngrok.com) |
| **Sideloadly** | Installs .ipa files on your iPhone | [sideloadly.io](https://sideloadly.io) |

Sign up for a free GitHub account if you don't have one, then log in:

```powershell
gh auth login
```

Sign up for a free ngrok account and connect your auth token:

```powershell
ngrok config add-authtoken YOUR_TOKEN_HERE
```

---

## Step 1: Get the Template

Open PowerShell and run:

```powershell
# Clone the governance template from GitHub
git clone https://github.com/decnet105/claude-code-best-practices.git D:\swim-app

# Go into your new project
cd D:\swim-app

# Remove the template's git history so you start fresh
Remove-Item -Recurse -Force .git

# Start your own git history
git init
```

> **Note:** If the repo is private, make sure you ran `gh auth login` first.

---

## Step 2: Edit CLAUDE.md (The Rulebook)

Open `D:\swim-app\CLAUDE.md` in any text editor (Notepad, VS Code, whatever
you like). Find the placeholder lines and replace them with your project info:

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
├── src/                    # React Native / Expo source code
│   ├── app/                # Screens, components, navigation
│   ├── api/                # Backend API (runs on your PC)
```

**Find this:**
```bash
{{TEST_COMMAND}}   # e.g., python -m pytest tests/ -x -q
```

**Change to:**
```bash
npm test                    # Runs Jest tests for the React Native app
```

---

## Step 3: Set Up the Safety Hook

The safety hook stops Claude from editing important files at times you choose
— like during a swim meet when your team is relying on the app!

Open `D:\swim-app\.claude\hooks\production_safety_gate.py` and edit the
config section near the top:

```python
# Files that should be protected during meets/events
PROTECTED_PATTERNS = [
    "src/app/timer/",             # The race timer — never break this!
    "src/app/scoreboard/",        # Live scoreboard display
    "src/api/meet-results.js",    # API that saves official results
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
| FEAT-001 | feature | P1 | Swimmer profile page with times and PBs | OPEN | — | — | 2026-05-31 |
| FEAT-002 | feature | P1 | Race timer with lane assignments | OPEN | — | — | 2026-05-31 |
| FEAT-003 | feature | P2 | Meet schedule calendar view | OPEN | — | — | 2026-05-31 |
| FEAT-004 | feature | P2 | Live scoreboard synced across phones | OPEN | — | FEAT-002 | 2026-05-31 |
| FEAT-005 | feature | P3 | Export times to CSV for coach | OPEN | — | — | 2026-05-31 |
| BUG-001 | bug | P1 | App crashes when swimmer has no times yet | OPEN | — | — | 2026-05-31 |
```

**Priority guide:**
- **P0** = Emergency — the app is broken and people need it NOW
- **P1** = Must do next — the most important things to build
- **P2** = Should do soon — important but can wait a bit
- **P3** = Nice to have — do it when you have time
- **P4** = Backlog — just an idea for later

---

## Step 5: First Commit + Push to GitHub

```powershell
cd D:\swim-app

# Commit everything locally
git add -A
git commit -m "Initial setup: swim-app with Claude Code governance"

# Create a NEW repo on YOUR GitHub and push (choose private or public)
gh repo create swim-app --private --source=. --push
```

Now your code is on GitHub. You can see it at `https://github.com/YOUR_USERNAME/swim-app`.

---

## Step 6: The Development Stack

Here's how the three tools work together when you're building and testing
your app on a real iPhone:

```
                YOUR PC (D:\swim-app)                    YOUR iPHONE
               ┌──────────────────────┐
               │                      │
  Claude Code  │   1. You write code  │
  writes code  │      with Claude     │
  here         │                      │
               │   2. Dev server      │        ┌─────────────────┐
               │      runs locally    │        │                 │
               │      (localhost:     │ ◄──────│  4. Open the    │
               │       3000)          │  ngrok │     app on      │
               │         │            │ tunnel │     your phone  │
               │         ▼            │        │     and test!   │
               │   3. ngrok makes     │────────►                 │
               │      localhost       │        └─────────────────┘
               │      reachable from  │
               │      the internet    │        For a real .ipa:
               │                      │        ┌─────────────────┐
               │   5. Build the .ipa  │────────│  6. Sideloadly  │
               │      when ready      │  USB   │     installs it │
               │                      │  cable │     on iPhone   │
               └──────────────────────┘        └─────────────────┘
```

### Running Your Dev Server + ngrok

While developing, you'll have three terminals open:

**Terminal 1 — Claude Code (your AI assistant):**
```powershell
cd D:\swim-app
claude
```

**Terminal 2 — Dev server (runs your app locally):**
```powershell
cd D:\swim-app
npm start
# App is now running at http://localhost:3000
```

**Terminal 3 — ngrok (makes it reachable from your phone):**
```powershell
ngrok http 3000
# ngrok gives you a URL like: https://abc123.ngrok-free.app
# Open this URL on your iPhone's browser to test!
```

### Installing on iPhone with Sideloadly

When you're ready to install the real app (not just test in a browser):

1. **Build the .ipa file** — Claude can help you with this:
   ```
   You: Build the .ipa for my swim-app
   ```

2. **Connect your iPhone** to your PC with a USB cable

3. **Open Sideloadly** and:
   - Drag your `.ipa` file into Sideloadly
   - Enter your Apple ID (a free one works)
   - Click "Start" — it installs the app on your phone!

4. **Trust the app** on your iPhone:
   - Go to Settings → General → VPN & Device Management
   - Tap your Apple ID → Trust

> **Important:** Free Apple IDs need to re-sign every 7 days. Just repeat
> step 3 each week. A $99/year Apple Developer account makes it last a year.

---

## Step 7: Start Using Claude Code

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
    ├── app\                     Screens, components, navigation
    ├── api\                     Backend API server
    └── __tests__\               Test files
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

## Daily Workflow Cheat Sheet

Here's what a typical development day looks like:

```
 ┌─────────────────────────────────────────────────────────────┐
 │  MORNING — Sit down to code                                │
 │                                                             │
 │  1. Open PowerShell → cd D:\swim-app → claude               │
 │  2. /session-health  (check everything is OK)               │
 │  3. Open docs/tracker.md  (pick what to work on)            │
 │  4. Tell Claude: "Let's work on FEAT-002"                   │
 └──────────────────────┬──────────────────────────────────────┘
                        │
 ┌──────────────────────▼──────────────────────────────────────┐
 │  BUILDING — Write features with TDD                        │
 │                                                             │
 │  5. /tdd  (Claude writes test → code → test → code)         │
 │  6. Test on phone:                                          │
 │     • Terminal 2: npm start                                 │
 │     • Terminal 3: ngrok http 3000                            │
 │     • Open the ngrok URL on your iPhone                     │
 │  7. Found a bug? → /debug  (find root cause, then fix)      │
 └──────────────────────┬──────────────────────────────────────┘
                        │
 ┌──────────────────────▼──────────────────────────────────────┐
 │  WRAPPING UP — Save your progress                          │
 │                                                             │
 │  8. Claude commits and pushes to GitHub automatically       │
 │  9. /handover  (saves session state for next time)          │
 │ 10. Close Claude — done for the day!                        │
 └─────────────────────────────────────────────────────────────┘
```

---

## Pushing Updates to GitHub

After Claude makes changes, push them to GitHub so they're backed up:

```powershell
git push
```

If you're working from a **different computer** (like a laptop at the pool),
pull the latest code first:

```powershell
cd D:\swim-app
git pull
claude
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `gh: command not found` | Install GitHub CLI from [cli.github.com](https://cli.github.com) |
| `ngrok: command not found` | Install ngrok from [ngrok.com](https://ngrok.com), add to PATH |
| ngrok URL doesn't load on phone | Make sure `npm start` is running in Terminal 2 first |
| Sideloadly says "Apple ID error" | Use a regular Apple ID (not a managed/school one). Try creating a new free one at [appleid.apple.com](https://appleid.apple.com) |
| App disappears after 7 days | Free Apple IDs expire weekly. Re-sideload, or get a $99/year developer account |
| Claude won't edit a file | Check if the safety hook is blocking it (wrong time/day). Edit the hook config |
| `git push` rejected | Run `git pull --rebase` first, then `git push` again |

---

## Example Session

Here's what a real session might look like:

```
You: /session-health
Claude: Git: main @ a1b2c3d, clean tree
        Tests: 12 passed, 0 failed
        Alerts: none
        Overall: HEALTHY

You: Let's work on FEAT-002, the race timer with lane assignments.

You: /tdd
Claude: Let's plan the behaviors:
        1. Timer shows lane numbers 1-8 with swimmer names
        2. Start button begins countdown (3-2-1-GO)
        3. Each lane has its own split/stop button
        4. Stopping a lane records the time to 2 decimal places
        5. All times are saved to the swimmer's profile
        Does this look right?

You: Yes but only 6 lanes, our pool has 6 lanes not 8.

Claude: Got it — 6 lanes. Starting with behavior 1.
        [writes test_timer_shows_six_lanes_with_names — RED, fails]
        [writes LaneDisplay component — GREEN, passes]
        [writes test_start_button_triggers_countdown — RED, fails]
        [writes CountdownTimer component — GREEN, passes]
        ... (repeats for each behavior)

Claude: All 5 tests passing. Full suite: 17 passed, 0 failed.
        Committed: "feat: add race timer with 6-lane support"
        Updated tracker: FEAT-002 → DONE.

You: Let me test it on my phone. Is ngrok running?

Claude: Start your dev server and ngrok:
        Terminal 2: npm start
        Terminal 3: ngrok http 3000
        Then open the ngrok URL on your iPhone.

You: The timer works but it looks weird on my phone. The lane buttons
     are too small to tap.

You: /debug
Claude: Phase 0 — Classification: L3 (Code) — CSS/layout issue,
        not infrastructure or architecture.
        Phase 1 — Reading src/app/timer/LaneDisplay.jsx...
        Root cause: button height is 32px, Apple recommends minimum
        44px for touch targets on iOS.
        [writes test_lane_buttons_meet_minimum_touch_size — RED]
        [fixes button height to 48px — GREEN]

You: Perfect! /handover
Claude: [writes HANDOVER_2026-05-31_race-timer.md]
        Ship summary: FEAT-002 done (race timer, 6 lanes, iOS touch fix).
        Next up: FEAT-004 (live scoreboard) is unblocked now.
```

---

## What's Next?

Once you're comfortable with the basics:

- **Add more features** to the tracker and work through them with `/tdd`
- **Write knowledge articles** in `docs/knowledge/` when you learn something
  useful (like "how to make buttons tappable on iPhone")
- **Run `/code-review`** before pushing big changes
- **Run `/security-audit`** before adding any login or user data features
- **Share the GitHub repo** with your swim coach so they can see progress

That's it! You now have a professional-grade AI development setup. Have fun
building swim-app!
