"""
Production Safety Gate — PreToolUse hook.

Blocks Edit/Write to protected production files during configurable hours.
Adapt PROTECTED_PATTERNS and the time window to your project.

Usage:
  Configure in .claude/settings.json under hooks.PreToolUse.
  The hook reads JSON from stdin (Claude Code hook protocol) and exits 0
  to allow or prints a deny JSON to block.
"""
import json
import sys
from datetime import datetime

try:
    from zoneinfo import ZoneInfo
except ImportError:
    from backports.zoneinfo import ZoneInfo


# ============================================================================
# CONFIGURE THESE FOR YOUR PROJECT
# ============================================================================

# Files/directories that should be protected during production hours.
# Uses substring matching against the normalized (forward-slash, lowercase) path.
PROTECTED_PATTERNS = [
    # Examples — replace with your actual production paths:
    # "src/billing/",
    # "src/auth/",
    # "src/core/database.py",
    # "app/models/",
    # "lib/payment_processor.py",
]

# Timezone for the protection window
TIMEZONE = "America/New_York"

# Protection window: block edits during these hours (24h format)
# Set to your production/business hours, deploy windows, etc.
PROTECT_START_HOUR = 9
PROTECT_START_MINUTE = 30
PROTECT_END_HOUR = 16
PROTECT_END_MINUTE = 0

# Days to protect (0=Monday, 6=Sunday)
PROTECTED_DAYS = {0, 1, 2, 3, 4}  # Monday-Friday

# ============================================================================


def main() -> None:
    hook_input = json.load(sys.stdin)

    tool_name = hook_input.get("tool_name", "")
    if tool_name not in ("Edit", "Write"):
        sys.exit(0)

    tool_input = hook_input.get("tool_input", {})
    file_path = tool_input.get("file_path", "")
    if not file_path:
        sys.exit(0)

    normalized = file_path.replace("\\", "/").lower()

    is_protected = any(p.lower() in normalized for p in PROTECTED_PATTERNS)
    if not is_protected:
        sys.exit(0)

    now = datetime.now(ZoneInfo(TIMEZONE))
    if now.weekday() not in PROTECTED_DAYS:
        sys.exit(0)

    current_minutes = now.hour * 60 + now.minute
    start_minutes = PROTECT_START_HOUR * 60 + PROTECT_START_MINUTE
    end_minutes = PROTECT_END_HOUR * 60 + PROTECT_END_MINUTE

    if current_minutes < start_minutes or current_minutes >= end_minutes:
        sys.exit(0)

    time_str = now.strftime("%H:%M %Z")
    result = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": (
                f"PRODUCTION SAFETY GATE: Cannot modify {file_path} during "
                f"protected hours ({PROTECT_START_HOUR}:{PROTECT_START_MINUTE:02d}"
                f"-{PROTECT_END_HOUR}:{PROTECT_END_MINUTE:02d} {TIMEZONE}). "
                f"Current time: {time_str}. "
                f"Schedule edits for after protected hours."
            ),
        }
    }
    json.dump(result, sys.stdout)
    sys.exit(0)


if __name__ == "__main__":
    main()
