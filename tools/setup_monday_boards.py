"""
🤖 Monday.com Board Setup — Chatting Wizard Task Management System

Creates 5 boards with 🤖 prefix (without touching existing boards):

1. 🤖 CW Master Tasks      — Pau's cockpit: assign ANY task to ANYONE
2. 🤖 CW Chatting Ops      — Ryzel + TLs: coaching, performance, scheduling
3. 🤖 CW Scripts            — Rei + Cath: script pipeline
4. 🤖 CW Content & Clients  — Angeles: content, clients, onboarding
5. 🤖 CW Hiring             — Mileh: recruitment pipeline

Usage:
    python tools/setup_monday_boards.py

Requires: MONDAY_API_TOKEN environment variable
"""

import sys
import os
import json
import time

sys.path.insert(0, os.path.dirname(__file__))
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from monday_cli import query

DELAY = 1.2  # seconds between API calls (rate limit protection)


# ── Helpers ───────────────────────────────────────────────────

def create_board(name):
    """Create a public board and return its ID."""
    escaped = name.replace('"', '\\"')
    data = query(f'''
    mutation {{
        create_board (board_name: "{escaped}", board_kind: public) {{
            id
        }}
    }}
    ''')
    bid = data["create_board"]["id"]
    print(f"\n{'='*60}")
    print(f"  BOARD: {name}")
    print(f"  ID:    {bid}")
    print(f"{'='*60}")
    time.sleep(DELAY)
    return bid


def add_col(bid, title, col_type, defaults=None):
    """Add a column to a board. col_type is Monday ColumnType enum (text, status, people, date, dropdown, etc.)."""
    escaped = title.replace('"', '\\"')
    defaults_part = ""
    if defaults:
        defaults_json = json.dumps(json.dumps(defaults))
        defaults_part = f", defaults: {defaults_json}"

    try:
        data = query(f'''
        mutation {{
            create_column (
                board_id: {bid}
                title: "{escaped}"
                column_type: {col_type}
                {defaults_part}
            ) {{
                id
                title
            }}
        }}
        ''')
        col = data.get("create_column", {})
        print(f"    + Column: {col.get('title', title)} [{col_type}] -> {col.get('id', '?')}")
        time.sleep(DELAY)
        return col.get("id")
    except Exception as e:
        print(f"    ! Column '{title}' failed: {e}")
        time.sleep(DELAY)
        return None


def add_group(bid, name):
    """Create a group in a board."""
    escaped = name.replace('"', '\\"')
    try:
        data = query(f'''
        mutation {{
            create_group (board_id: {bid}, group_name: "{escaped}") {{
                id
            }}
        }}
        ''')
        gid = data["create_group"]["id"]
        print(f"    + Group: {name} -> {gid}")
        time.sleep(DELAY)
        return gid
    except Exception as e:
        print(f"    ! Group '{name}' failed: {e}")
        time.sleep(DELAY)
        return None


def get_groups(bid):
    """Get all groups of a board."""
    data = query(f'{{ boards(ids: [{bid}]) {{ groups {{ id title }} }} }}')
    return data.get("boards", [{}])[0].get("groups", [])


def delete_group(bid, gid):
    """Delete a group."""
    try:
        query(f'mutation {{ delete_group (board_id: {bid}, group_id: "{gid}") {{ id }} }}')
        print(f"    - Removed default group: {gid}")
        time.sleep(DELAY)
    except:
        pass


# ── Shared column definitions ─────────────────────────────────

PRIORITY_DEFAULTS = {
    "labels": {
        "0": "Critical \u26a0\ufe0f",
        "1": "High",
        "2": "Medium",
        "3": "Low"
    }
}

STATUS_DEFAULTS = {
    "labels": {
        "0": "Not Started",
        "1": "Working on it",
        "2": "Stuck",
        "3": "Waiting",
        "4": "Done"
    }
}


def add_common_columns(bid):
    """Add the columns every board shares: Assignee, Status, Priority, Deadline, Description."""
    add_col(bid, "Assignee", "people")
    add_col(bid, "Status", "status", STATUS_DEFAULTS)
    add_col(bid, "Priority", "status", PRIORITY_DEFAULTS)
    add_col(bid, "Deadline", "date")
    add_col(bid, "Description", "text")


def cleanup_default_groups(bid):
    """Remove any auto-created default groups."""
    for g in get_groups(bid):
        if g["title"] in ["Group Title", "New Group", "Título del grupo"]:
            delete_group(bid, g["id"])


# ── Board 1: Master Tasks ────────────────────────────────────

def setup_master_tasks():
    """
    🤖 CW Master Tasks — Pau's command center.
    
    Purpose: Create and track ANY task for ANY person across all departments.
    Owner: Pau (COO)
    
    This is THE board where Pau assigns tasks. Any person in the company
    can be assigned here. Department tag helps filter/sort.
    """
    bid = create_board("🤖 CW Master Tasks")

    # Common columns
    add_common_columns(bid)

    # Board-specific columns
    add_col(bid, "Department", "dropdown", {
        "labels": [
            {"name": "Chatting"},
            {"name": "Scripts"},
            {"name": "Content"},
            {"name": "Hiring"},
            {"name": "Data"},
            {"name": "QA"},
            {"name": "Strategy"},
            {"name": "Other"}
        ]
    })
    add_col(bid, "Notes", "long_text")

    # Groups (created in reverse — Monday puts newest group at top)
    for g in ["❌ Cancelled", "✅ Done", "📋 Backlog", "📌 This Week", "🔴 Urgent"]:
        add_group(bid, g)

    cleanup_default_groups(bid)
    return bid


# ── Board 2: Chatting Ops ────────────────────────────────────

def setup_chatting_ops():
    """
    🤖 CW Chatting Ops — Ryzel + TLs operational board.
    
    Purpose: Manage chatting department operations.
    Owner: Ryzel (CHM)
    Assignees: Ryzel, Danilyn, Huckle, Ezekiel
    
    Covers: coaching sessions, performance investigations, schedule creation,
    probation monitoring, traffic balancing, QA reviews, chatter investigations.
    """
    bid = create_board("🤖 CW Chatting Ops")

    add_common_columns(bid)

    add_col(bid, "Category", "dropdown", {
        "labels": [
            {"name": "Coaching"},
            {"name": "Performance"},
            {"name": "Schedule"},
            {"name": "Probation"},
            {"name": "Traffic"},
            {"name": "Investigation"},
            {"name": "QA"},
            {"name": "Other"}
        ]
    })

    for g in ["✅ Done", "⏸ Waiting", "▶ In Progress", "◉ To Do"]:
        add_group(bid, g)

    cleanup_default_groups(bid)
    return bid


# ── Board 3: Scripts ──────────────────────────────────────────

def setup_scripts():
    """
    🤖 CW Scripts — Script management pipeline.
    
    Purpose: Track all script-related work through its lifecycle.
    Owner: Rei (Script Manager)
    Assignees: Rei, Cath (Script Assistant)
    
    Covers: new model script creation, script updates/optimization,
    sexting diversification, smart messages, QA checks, Infloww imports.
    """
    bid = create_board("🤖 CW Scripts")

    add_common_columns(bid)

    add_col(bid, "Model", "text")
    add_col(bid, "Type", "dropdown", {
        "labels": [
            {"name": "New Model"},
            {"name": "Script Update"},
            {"name": "Diversify"},
            {"name": "Smart Messages"},
            {"name": "QA Check"},
            {"name": "Infloww Import"},
            {"name": "Other"}
        ]
    })

    for g in ["✅ Done", "🔍 Review", "🔨 In Progress", "📋 Backlog"]:
        add_group(bid, g)

    cleanup_default_groups(bid)
    return bid


# ── Board 4: Content & Clients ───────────────────────────────

def setup_content_clients():
    """
    🤖 CW Content & Clients — Content and client management.
    
    Purpose: Track content requests, custom orders, deep dives,
    client reports, and model on/offboarding.
    Owner: Angeles
    
    Covers: content requests from clients, custom orders (video/photo/VC/audio),
    deep dive revenue analysis, client reports & follow-ups,
    model onboarding/offboarding pipeline.
    """
    bid = create_board("🤖 CW Content & Clients")

    add_common_columns(bid)

    add_col(bid, "Client", "text")
    add_col(bid, "Model", "text")
    add_col(bid, "Type", "dropdown", {
        "labels": [
            {"name": "Content Request"},
            {"name": "Custom Order"},
            {"name": "Deep Dive"},
            {"name": "Client Report"},
            {"name": "Model Onboarding"},
            {"name": "Model Offboarding"},
            {"name": "Other"}
        ]
    })

    for g in ["✅ Completed", "⏳ Waiting", "🔨 In Progress", "📋 New Requests"]:
        add_group(bid, g)

    cleanup_default_groups(bid)
    return bid


# ── Board 5: Hiring ──────────────────────────────────────────

def setup_hiring():
    """
    🤖 CW Hiring — Recruitment pipeline.
    
    Purpose: Track the full hiring funnel from application to hire/decline.
    Owner: Mileh (Hiring Manager)
    
    Covers: application screening, interviews, 5-day training program,
    final exam (written + live), probation (14 days), hire/decline decision.
    
    Groups mirror the hiring stages so moving an item between groups
    = advancing the recruit through the pipeline.
    """
    bid = create_board("🤖 CW Hiring")

    add_common_columns(bid)

    add_col(bid, "Test Score", "numbers")
    add_col(bid, "Exam Score", "numbers")
    add_col(bid, "TL Assigned", "people")
    add_col(bid, "Stage", "dropdown", {
        "labels": [
            {"name": "Screening"},
            {"name": "Interview"},
            {"name": "Day 1"},
            {"name": "Day 2"},
            {"name": "Day 3"},
            {"name": "Day 4"},
            {"name": "Day 5"},
            {"name": "Probation W1"},
            {"name": "Probation W2"},
            {"name": "Hired"},
            {"name": "Declined"}
        ]
    })

    for g in ["❌ Declined", "✅ Hired", "⏳ Probation", "📚 Training", "🎤 Interview", "📝 Applicants"]:
        add_group(bid, g)

    cleanup_default_groups(bid)
    return bid


# ── Main ──────────────────────────────────────────────────────

def main():
    print()
    print("🤖 CHATTING WIZARD — Monday.com Board Setup")
    print("=" * 60)
    print("Creating 5 new boards with 🤖 prefix...")
    print("Existing boards will NOT be touched.")
    print()

    boards = {}

    boards["🤖 CW Master Tasks"] = setup_master_tasks()
    boards["🤖 CW Chatting Ops"] = setup_chatting_ops()
    boards["🤖 CW Scripts"] = setup_scripts()
    boards["🤖 CW Content & Clients"] = setup_content_clients()
    boards["🤖 CW Hiring"] = setup_hiring()

    print(f"\n{'='*60}")
    print("🤖 SETUP COMPLETE — All boards created!")
    print(f"{'='*60}")
    for name, bid in boards.items():
        print(f"  {name}: {bid}")
    print(f"\nTotal: {len(boards)} boards created")
    print()
    print("Board IDs (save for reference):")
    print(json.dumps({k: v for k, v in boards.items()}, indent=2, ensure_ascii=False))

    return boards


if __name__ == "__main__":
    main()
