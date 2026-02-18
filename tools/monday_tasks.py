"""
🤖 Monday Task Manager — Chatting Wizard

Smart task creation, templates, summaries, and daily digest.

Commands:
    python tools/monday_tasks.py create "Task" --assignee Ryzel --priority high --deadline 2026-02-21
    python tools/monday_tasks.py summary
    python tools/monday_tasks.py overdue
    python tools/monday_tasks.py person Ryzel
    python tools/monday_tasks.py board master
    python tools/monday_tasks.py template model-onboarding --model "Luna"
    python tools/monday_tasks.py template chatter-onboarding --chatter "John" --tl Danilyn
    python tools/monday_tasks.py template weekly
    python tools/monday_tasks.py digest [--send-slack]
    python tools/monday_tasks.py setup-descriptions

Requires: MONDAY_API_TOKEN environment variable
"""

import sys
import os
import json
import argparse
from datetime import datetime, timedelta

sys.path.insert(0, os.path.dirname(__file__))
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from monday_cli import query, get_headers, API_URL

try:
    import requests
except ImportError:
    print("ERROR: requests not installed. Run: pip install requests")
    sys.exit(1)


def query_safe(q, variables=None):
    """Execute a GraphQL query. Returns (data, error) instead of sys.exit on failure."""
    payload = {"query": q}
    if variables:
        payload["variables"] = variables
    resp = requests.post(API_URL, json=payload, headers=get_headers())
    resp.raise_for_status()
    data = resp.json()
    if "errors" in data:
        return None, data["errors"]
    return data.get("data", {}), None


# ══════════════════════════════════════════════════════════════
# CONFIGURATION — Board IDs, Column IDs, User IDs, Routing
# ══════════════════════════════════════════════════════════════

USERS = {
    "pau":      {"id": 89477039, "name": "Pau Lopez Ferrer"},
    "santi":    {"id": 89476988, "name": "Santi Jiang"},
    "ryzel":    {"id": 90023534, "name": "Rycel Monique"},
    "rycel":    {"id": 90023534, "name": "Rycel Monique"},
    "danilyn":  {"id": 90186609, "name": "Danilyn Deo"},
    "huckle":   {"id": 90186611, "name": "Huckle Albisa"},
    "ezekiel":  {"id": 93910277, "name": "Ezekiel Orika"},
    "rei":      {"id": 95309506, "name": "Reishi Glynne Quibido"},
    "cath":     {"id": 97512841, "name": "Roussel Catherine Bonita"},
    "angeles":  {"id": 89875255, "name": "Angeles Diaz"},
    "mileh":    {"id": 96683602, "name": "Mileh"},
    "daniela":  {"id": 89989739, "name": "Ma. Daniela"},
    "daniela_rada": {"id": 92250193, "name": "Daniela Rada"},
}

# Which board each person's tasks go to by default
USER_BOARD_ROUTING = {
    "ryzel": "chatting", "rycel": "chatting",
    "danilyn": "chatting", "huckle": "chatting", "ezekiel": "chatting",
    "rei": "scripts", "cath": "scripts",
    "angeles": "content",
    "mileh": "hiring",
    "daniela": "master", "daniela_rada": "master",
    "pau": "master", "santi": "master",
}

BOARDS = {
    "master": {
        "id": "5091787921",
        "name": "🤖 CW Master Tasks",
        "owner": "Pau",
        "cols": {
            "assignee":    "multiple_person_mm0jvpa8",
            "status":      "color_mm0jxycg",
            "priority":    "color_mm0j4a2",
            "deadline":    "date_mm0jnxmz",
            "description": "text_mm0jzxcj",
            "department":  "color_mm0jj161",
            "notes":       "long_text_mm0jyna5",
        },
        "groups": {
            "urgent":    "group_mm0jhdf9",
            "this_week": "group_mm0j68dj",
            "backlog":   "group_mm0jqkb6",
            "done":      "group_mm0jk5z8",
            "cancelled": "group_mm0jtfwc",
        },
        "priority_to_group": {
            "critical": "group_mm0jhdf9",
            "high":     "group_mm0j68dj",
            "medium":   "group_mm0jqkb6",
            "low":      "group_mm0jqkb6",
        },
        "done_groups": ["group_mm0jk5z8", "group_mm0jtfwc"],
    },
    "chatting": {
        "id": "5091787931",
        "name": "🤖 CW Chatting Ops",
        "owner": "Ryzel",
        "cols": {
            "assignee":    "multiple_person_mm0jmqsd",
            "status":      "color_mm0jje2a",
            "priority":    "color_mm0j1e48",
            "deadline":    "date_mm0j66ty",
            "description": "text_mm0j6zgx",
            "category":    "color_mm0j5xh3",
        },
        "groups": {
            "todo":        "group_mm0jbp2a",
            "in_progress": "group_mm0jmgpq",
            "waiting":     "group_mm0jhz0h",
            "done":        "group_mm0jf2f5",
        },
        "priority_to_group": {
            "critical": "group_mm0jbp2a",
            "high":     "group_mm0jbp2a",
            "medium":   "group_mm0jbp2a",
            "low":      "group_mm0jbp2a",
        },
        "done_groups": ["group_mm0jf2f5"],
    },
    "scripts": {
        "id": "5091787952",
        "name": "🤖 CW Scripts",
        "owner": "Rei",
        "cols": {
            "assignee":    "multiple_person_mm0jshfg",
            "status":      "color_mm0j80k8",
            "priority":    "color_mm0jsf6k",
            "deadline":    "date_mm0jqdt0",
            "description": "text_mm0jq6a4",
            "model":       "text_mm0jtejt",
            "type":        "color_mm0jfqwf",
        },
        "groups": {
            "backlog":     "group_mm0j2b4w",
            "in_progress": "group_mm0j52er",
            "review":      "group_mm0jh8rz",
            "done":        "group_mm0jsbva",
        },
        "priority_to_group": {
            "critical": "group_mm0j2b4w",
            "high":     "group_mm0j2b4w",
            "medium":   "group_mm0j2b4w",
            "low":      "group_mm0j2b4w",
        },
        "done_groups": ["group_mm0jsbva"],
    },
    "content": {
        "id": "5091787968",
        "name": "🤖 CW Content & Clients",
        "owner": "Angeles",
        "cols": {
            "assignee":    "multiple_person_mm0j5bgc",
            "status":      "color_mm0jxrh4",
            "priority":    "color_mm0jkjgx",
            "deadline":    "date_mm0jwxrm",
            "description": "text_mm0jmbbg",
            "client":      "text_mm0je846",
            "model":       "text_mm0jyjp7",
            "type":        "color_mm0j48cv",
        },
        "groups": {
            "new":         "group_mm0j22ag",
            "in_progress": "group_mm0jnvq",
            "waiting":     "group_mm0jf9bk",
            "completed":   "group_mm0jj8qw",
        },
        "priority_to_group": {
            "critical": "group_mm0j22ag",
            "high":     "group_mm0j22ag",
            "medium":   "group_mm0j22ag",
            "low":      "group_mm0j22ag",
        },
        "done_groups": ["group_mm0jj8qw"],
    },
    "hiring": {
        "id": "5091787979",
        "name": "🤖 CW Hiring",
        "owner": "Mileh",
        "cols": {
            "assignee":    "multiple_person_mm0jwha1",
            "status":      "color_mm0j1mpx",
            "priority":    "color_mm0j5eev",
            "deadline":    "date_mm0jqvgt",
            "description": "text_mm0j4q1j",
            "test_score":  "numeric_mm0j9k9q",
            "exam_score":  "numeric_mm0j1zev",
            "tl_assigned": "multiple_person_mm0jftty",
            "stage":       "color_mm0jhyg6",
        },
        "groups": {
            "applicants":  "group_mm0j7p35",
            "interview":   "group_mm0jhpt8",
            "training":    "group_mm0jj064",
            "probation":   "group_mm0jf1sm",
            "hired":       "group_mm0jcejz",
            "declined":    "group_mm0j1ax0",
        },
        "priority_to_group": {
            "critical": "group_mm0j7p35",
            "high":     "group_mm0j7p35",
            "medium":   "group_mm0j7p35",
            "low":      "group_mm0j7p35",
        },
        "done_groups": ["group_mm0jcejz", "group_mm0j1ax0"],
    },
}

ALL_BOARD_IDS = [b["id"] for b in BOARDS.values()]

PRIORITY_MAP = {
    "critical": "Critical \u26a0\ufe0f",
    "high": "High",
    "medium": "Medium",
    "low": "Low",
}


# ══════════════════════════════════════════════════════════════
# HELPERS
# ══════════════════════════════════════════════════════════════

def resolve_user(name_input):
    """Resolve a user name/alias to their config. Case-insensitive, partial match."""
    key = name_input.strip().lower().replace(" ", "_")
    # Direct match
    if key in USERS:
        return USERS[key]
    # Partial match
    for k, v in USERS.items():
        if key in k or key in v["name"].lower():
            return v
    print(f"[ERROR] User '{name_input}' not found. Known users: {', '.join(USERS.keys())}")
    sys.exit(1)


def resolve_board(name_input):
    """Resolve a board name/alias."""
    key = name_input.strip().lower()
    if key in BOARDS:
        return key, BOARDS[key]
    for k, b in BOARDS.items():
        if key in k or key in b["name"].lower():
            return k, b
    print(f"[ERROR] Board '{name_input}' not found. Options: {', '.join(BOARDS.keys())}")
    sys.exit(1)


def get_board_for_user(user_key):
    """Determine which board a user's tasks go to."""
    key = user_key.strip().lower().replace(" ", "_")
    for k in USER_BOARD_ROUTING:
        if key in k or k in key:
            return USER_BOARD_ROUTING[k]
    return "master"  # default fallback


def create_item(board_key, item_name, column_values, group_id=None):
    """Create an item on a board with column values.
    If dropdown labels cause an error, retries without dropdown columns."""
    board = BOARDS[board_key]
    bid = board["id"]
    escaped_name = item_name.replace('"', '\\"').replace('\n', ' ')
    group_part = f', group_id: "{group_id}"' if group_id else ""

    mutation = f'''
    mutation {{
        create_item (
            board_id: {bid}
            item_name: "{escaped_name}"
            column_values: COLVAL_PLACEHOLDER
            {group_part}
        ) {{
            id
            name
        }}
    }}
    '''

    col_json = json.dumps(json.dumps(column_values))
    q = mutation.replace("COLVAL_PLACEHOLDER", col_json)
    data, err = query_safe(q)

    if err:
        # Check if it's a dropdown label error — retry without dropdown columns
        err_msg = str(err)
        if "dropdown" in err_msg.lower() or "label" in err_msg.lower():
            cleaned = {k: v for k, v in column_values.items() if "dropdown" not in k}
            col_json = json.dumps(json.dumps(cleaned))
            q = mutation.replace("COLVAL_PLACEHOLDER", col_json)
            data, err2 = query_safe(q)
            if err2:
                print(f"    [ERROR] Could not create item: {err2}")
                return {}
            print("    [NOTE] Created without dropdown tag (run: monday_tasks.py fix-dropdowns)")
            return data.get("create_item", {})
        else:
            print(f"    [ERROR] Could not create item: {err}")
            return {}

    return data.get("create_item", {})


def build_column_values(board_key, assignee_id=None, priority=None,
                        deadline=None, description=None, **extras):
    """Build a column_values dict for a board."""
    board = BOARDS[board_key]
    cols = board["cols"]
    cv = {}

    if assignee_id and "assignee" in cols:
        cv[cols["assignee"]] = {"personsAndTeams": [{"id": assignee_id, "kind": "person"}]}

    if priority and "priority" in cols:
        label = PRIORITY_MAP.get(priority.lower(), priority)
        cv[cols["priority"]] = {"label": label}

    if deadline and "deadline" in cols:
        cv[cols["deadline"]] = {"date": deadline}

    if description and "description" in cols:
        cv[cols["description"]] = description

    # Board-specific extras
    for key, value in extras.items():
        if key in cols and value:
            col_id = cols[key]
            # Status columns (including category/department/type) use {"label": "..."}
            if "color" in col_id and key != "priority":
                cv[col_id] = {"label": value}
            # People columns
            elif "person" in col_id:
                if isinstance(value, int):
                    cv[col_id] = {"personsAndTeams": [{"id": value, "kind": "person"}]}
                else:
                    cv[col_id] = value
            # Number columns
            elif "numeric" in col_id:
                cv[col_id] = str(value)
            # Long text
            elif "long_text" in col_id:
                cv[col_id] = {"text": value}
            # Text columns
            else:
                cv[col_id] = value

    return cv


def query_board_items(board_id, limit=200):
    """Query all items from a board with their column values and group."""
    data = query(f'''
    {{
        boards(ids: [{board_id}]) {{
            name
            items_page(limit: {limit}) {{
                items {{
                    id
                    name
                    group {{
                        id
                        title
                    }}
                    column_values {{
                        id
                        text
                        type
                    }}
                }}
            }}
        }}
    }}
    ''')
    boards = data.get("boards", [])
    if not boards:
        return [], ""
    board = boards[0]
    items = board.get("items_page", {}).get("items", [])
    return items, board["name"]


def parse_item(item, board_config):
    """Parse an item's column values into a clean dict."""
    cols = board_config["cols"]
    col_id_to_name = {v: k for k, v in cols.items()}

    parsed = {
        "id": item["id"],
        "name": item["name"],
        "group": item.get("group", {}).get("title", "?"),
        "group_id": item.get("group", {}).get("id", ""),
    }

    for cv in item.get("column_values", []):
        field_name = col_id_to_name.get(cv["id"])
        if field_name:
            parsed[field_name] = cv.get("text", "") or ""

    return parsed


def is_done(item_parsed, board_config):
    """Check if an item is in a 'done' group."""
    return item_parsed.get("group_id", "") in board_config.get("done_groups", [])


def is_overdue(item_parsed):
    """Check if an item is past its deadline."""
    dl = item_parsed.get("deadline", "")
    if not dl:
        return False
    try:
        deadline_date = datetime.strptime(dl, "%Y-%m-%d").date()
        return deadline_date < datetime.now().date()
    except ValueError:
        return False


def is_due_today(item_parsed):
    """Check if an item is due today."""
    dl = item_parsed.get("deadline", "")
    if not dl:
        return False
    try:
        return datetime.strptime(dl, "%Y-%m-%d").date() == datetime.now().date()
    except ValueError:
        return False


def next_weekday(weekday):
    """Get the next occurrence of a weekday (0=Monday, 4=Friday)."""
    today = datetime.now().date()
    days_ahead = weekday - today.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return (today + timedelta(days=days_ahead)).strftime("%Y-%m-%d")


def days_from_now(n):
    """Get date n days from now as YYYY-MM-DD."""
    return (datetime.now().date() + timedelta(days=n)).strftime("%Y-%m-%d")


# ══════════════════════════════════════════════════════════════
# PHASE 1: CREATE COMMAND
# ══════════════════════════════════════════════════════════════

def cmd_create(args):
    """Smart task creation with auto-routing."""
    user = resolve_user(args.assignee)
    user_key = args.assignee.strip().lower()

    # Determine board
    if args.board:
        board_key, board = resolve_board(args.board)
    else:
        board_key = get_board_for_user(user_key)
        board = BOARDS[board_key]

    # Determine group based on priority
    priority = (args.priority or "medium").lower()
    group_id = board["priority_to_group"].get(priority, list(board["groups"].values())[0])

    # Build column values
    extras = {}
    if args.department:
        extras["department"] = args.department
    if args.category:
        extras["category"] = args.category
    if args.type:
        extras["type"] = args.type
    if args.model:
        extras["model"] = args.model
    if args.client:
        extras["client"] = args.client
    if args.notes:
        extras["notes"] = args.notes

    cv = build_column_values(
        board_key,
        assignee_id=user["id"],
        priority=priority,
        deadline=args.deadline,
        description=args.description,
        **extras,
    )

    item = create_item(board_key, args.name, cv, group_id)

    print(f"\n[OK] Task created!")
    print(f"  Board:    {board['name']}")
    print(f"  Task:     {item.get('name', args.name)}")
    print(f"  ID:       {item.get('id', '?')}")
    print(f"  Assignee: {user['name']}")
    print(f"  Priority: {PRIORITY_MAP.get(priority, priority)}")
    if args.deadline:
        print(f"  Deadline: {args.deadline}")
    print()

    return item


# ══════════════════════════════════════════════════════════════
# PHASE 1: SUMMARY COMMAND
# ══════════════════════════════════════════════════════════════

def cmd_summary(args):
    """Show summary of all 🤖 boards: active, overdue, by person."""
    print(f"\n{'='*65}")
    print(f"  🤖 MONDAY TASK SUMMARY — {datetime.now().strftime('%B %d, %Y')}")
    print(f"{'='*65}\n")

    total_active = 0
    total_overdue = 0
    person_tasks = {}

    for board_key, board in BOARDS.items():
        items, board_name = query_board_items(board["id"])
        active = []
        overdue = []

        for item in items:
            parsed = parse_item(item, board)
            if is_done(parsed, board):
                continue
            active.append(parsed)
            assignee = parsed.get("assignee", "Unassigned") or "Unassigned"
            person_tasks.setdefault(assignee, {"active": 0, "overdue": 0})
            person_tasks[assignee]["active"] += 1

            if is_overdue(parsed):
                overdue.append(parsed)
                person_tasks[assignee]["overdue"] += 1

        total_active += len(active)
        total_overdue += len(overdue)

        status = "🔴" if overdue else ("🟢" if active else "⚪")
        print(f"  {status} {board_name}")
        print(f"     Active: {len(active):>3}   Overdue: {len(overdue):>3}")

        if overdue:
            for item in overdue[:3]:
                print(f"     ⚠️  {item['name'][:45]} (due {item.get('deadline', '?')})")
        print()

    # Person breakdown
    if person_tasks:
        print(f"  {'─'*60}")
        print(f"  BY PERSON:")
        for person, counts in sorted(person_tasks.items(), key=lambda x: -x[1]["active"]):
            flag = " 🔴" if counts["overdue"] > 0 else ""
            print(f"    {person:<30} {counts['active']:>3} active, {counts['overdue']:>3} overdue{flag}")

    print(f"\n  {'─'*60}")
    print(f"  TOTAL: {total_active} active tasks, {total_overdue} overdue")
    print()


# ══════════════════════════════════════════════════════════════
# PHASE 1: OVERDUE COMMAND
# ══════════════════════════════════════════════════════════════

def cmd_overdue(args):
    """Show all overdue tasks across all boards."""
    print(f"\n🔴 OVERDUE TASKS — {datetime.now().strftime('%B %d, %Y')}\n")

    all_overdue = []
    for board_key, board in BOARDS.items():
        items, board_name = query_board_items(board["id"])
        for item in items:
            parsed = parse_item(item, board)
            if is_done(parsed, board):
                continue
            if is_overdue(parsed):
                parsed["_board"] = board_name
                all_overdue.append(parsed)

    if not all_overdue:
        print("  ✅ No overdue tasks! Everything is on track.\n")
        return

    all_overdue.sort(key=lambda x: x.get("deadline", "9999"))

    for item in all_overdue:
        assignee = item.get("assignee", "?") or "Unassigned"
        print(f"  ⚠️  {item['name'][:50]}")
        print(f"     Assignee: {assignee}  |  Due: {item.get('deadline', '?')}  |  Board: {item['_board']}")
        print()

    print(f"  Total: {len(all_overdue)} overdue tasks\n")


# ══════════════════════════════════════════════════════════════
# PHASE 1: PERSON COMMAND
# ══════════════════════════════════════════════════════════════

def cmd_person(args):
    """Show all active tasks for a specific person."""
    user = resolve_user(args.name)
    search_name = user["name"].lower()
    print(f"\n📋 TASKS FOR: {user['name']}\n")

    found = []
    for board_key, board in BOARDS.items():
        items, board_name = query_board_items(board["id"])
        for item in items:
            parsed = parse_item(item, board)
            if is_done(parsed, board):
                continue
            assignee = (parsed.get("assignee", "") or "").lower()
            if search_name in assignee or assignee in search_name:
                parsed["_board"] = board_name
                parsed["_board_key"] = board_key
                found.append(parsed)

    if not found:
        print(f"  No active tasks for {user['name']}.\n")
        return

    # Sort by deadline (tasks with no deadline last)
    found.sort(key=lambda x: x.get("deadline") or "9999")

    for item in found:
        overdue_flag = " 🔴 OVERDUE" if is_overdue(item) else ""
        today_flag = " 📌 TODAY" if is_due_today(item) else ""
        dl = item.get("deadline", "No deadline")
        priority = item.get("priority", "")
        print(f"  • {item['name'][:55]}{overdue_flag}{today_flag}")
        print(f"    {item['_board']}  |  Due: {dl}  |  Priority: {priority}  |  Group: {item['group']}")
        print()

    print(f"  Total: {len(found)} active tasks\n")


# ══════════════════════════════════════════════════════════════
# PHASE 1: BOARD COMMAND
# ══════════════════════════════════════════════════════════════

def cmd_board(args):
    """Show all active tasks on a specific board."""
    board_key, board = resolve_board(args.name)
    items, board_name = query_board_items(board["id"])

    print(f"\n📋 {board_name}\n")

    active = []
    for item in items:
        parsed = parse_item(item, board)
        if not is_done(parsed, board):
            active.append(parsed)

    if not active:
        print("  No active tasks.\n")
        return

    # Group by group title
    by_group = {}
    for item in active:
        g = item["group"]
        by_group.setdefault(g, []).append(item)

    for group_name, group_items in by_group.items():
        print(f"  {group_name} ({len(group_items)})")
        for item in group_items:
            assignee = item.get("assignee", "?") or "Unassigned"
            dl = item.get("deadline", "")
            dl_str = f" | Due: {dl}" if dl else ""
            overdue = " 🔴" if is_overdue(item) else ""
            print(f"    [{item['id']}] {item['name'][:45]} → {assignee}{dl_str}{overdue}")
        print()

    print(f"  Total: {len(active)} active tasks\n")


# ══════════════════════════════════════════════════════════════
# PHASE 2: TASK TEMPLATES
# ══════════════════════════════════════════════════════════════

def template_model_onboarding(model_name):
    """Create all tasks for a new model onboarding."""
    print(f"\n🤖 TEMPLATE: Model Onboarding — {model_name}")
    print(f"{'─'*55}\n")

    tasks = [
        # (board, name, assignee_key, priority, deadline_days, extras)
        ("content", f"Set up {model_name} profile in systems",
         "angeles", "high", 2, {"type": "Model Onboarding", "model": model_name}),
        ("content", f"Request initial content for {model_name}",
         "angeles", "high", 3, {"type": "Content Request", "model": model_name}),
        ("scripts", f"Create complete scripts for {model_name}",
         "rei", "high", 7, {"type": "New Model", "model": model_name}),
        ("scripts", f"Create Smart Messages for {model_name}",
         "cath", "medium", 10, {"type": "Smart Messages", "model": model_name}),
        ("scripts", f"QA check scripts for {model_name}",
         "rei", "medium", 9, {"type": "QA Check", "model": model_name}),
        ("scripts", f"Import {model_name} scripts to Infloww",
         "rei", "medium", 10, {"type": "Infloww Import", "model": model_name}),
        ("chatting", f"Brief TLs on new model: {model_name}",
         "ryzel", "medium", 10, {"category": "Other"}),
        ("master", f"Review {model_name} onboarding completion",
         "pau", "medium", 12, {"department": "Content"}),
    ]

    created = []
    for board_key, name, assignee_key, priority, days, extras in tasks:
        user = USERS[assignee_key]
        board = BOARDS[board_key]
        deadline = days_from_now(days)
        group_id = board["priority_to_group"].get(priority)

        cv = build_column_values(board_key, user["id"], priority, deadline,
                                 f"Part of {model_name} model onboarding", **extras)
        item = create_item(board_key, name, cv, group_id)
        created.append(item)
        print(f"  ✓ {name}")
        print(f"    → {user['name']}  |  {board['name']}  |  Due: {deadline}")

    print(f"\n  Total: {len(created)} tasks created for {model_name} onboarding\n")
    return created


def template_chatter_onboarding(chatter_name, tl_key):
    """Create all tasks for a new chatter post-hiring onboarding."""
    tl_user = resolve_user(tl_key)
    print(f"\n🤖 TEMPLATE: Chatter Onboarding — {chatter_name} (TL: {tl_user['name']})")
    print(f"{'─'*55}\n")

    tasks = [
        ("chatting", f"Assign {chatter_name} to TL and models",
         "ryzel", "high", 1, {"category": "Schedule"}),
        ("chatting", f"Give {chatter_name} Infloww & tools access",
         "ryzel", "high", 1, {"category": "Other"}),
        ("chatting", f"Probation Week 1 review: {chatter_name}",
         tl_key, "high", 7, {"category": "Probation"}),
        ("chatting", f"Probation Week 2 review: {chatter_name}",
         tl_key, "high", 14, {"category": "Probation"}),
        ("chatting", f"Pass/Fail decision: {chatter_name}",
         "ryzel", "high", 14, {"category": "Probation"}),
    ]

    created = []
    for board_key, name, assignee_key, priority, days, extras in tasks:
        user = resolve_user(assignee_key) if assignee_key not in USERS else USERS[assignee_key]
        board = BOARDS[board_key]
        deadline = days_from_now(days)
        group_id = board["priority_to_group"].get(priority)

        cv = build_column_values(board_key, user["id"], priority, deadline,
                                 f"Onboarding follow-up for new chatter {chatter_name}", **extras)
        item = create_item(board_key, name, cv, group_id)
        created.append(item)
        print(f"  ✓ {name}")
        print(f"    → {user['name']}  |  Due: {deadline}")

    print(f"\n  Total: {len(created)} tasks created for {chatter_name} onboarding\n")
    return created


def template_weekly():
    """Create recurring weekly tasks."""
    friday = next_weekday(4)  # Friday
    next_monday = next_weekday(0)  # Monday
    print(f"\n🤖 TEMPLATE: Weekly Recurring Tasks")
    print(f"{'─'*55}\n")

    tasks = [
        ("chatting", "Create schedule for next week",
         "ryzel", "high", friday, {"category": "Schedule"}),
        ("chatting", "Review weekly KPIs & identify low performers",
         "ryzel", "medium", friday, {"category": "Performance"}),
        ("chatting", "Review coaching log completeness",
         "ryzel", "medium", friday, {"category": "Coaching"}),
        ("master", "Weekly management review",
         "pau", "medium", friday, {"department": "Strategy"}),
        ("master", "Verify Inflow data exported & ingested",
         "daniela", "medium", next_monday, {"department": "Data"}),
    ]

    created = []
    for board_key, name, assignee_key, priority, deadline, extras in tasks:
        user = USERS[assignee_key]
        board = BOARDS[board_key]
        group_id = board["priority_to_group"].get(priority)

        cv = build_column_values(board_key, user["id"], priority, deadline,
                                 "Weekly recurring task", **extras)
        item = create_item(board_key, name, cv, group_id)
        created.append(item)
        print(f"  ✓ {name}")
        print(f"    → {user['name']}  |  Due: {deadline}")

    print(f"\n  Total: {len(created)} weekly tasks created\n")
    return created


def cmd_template(args):
    """Run a task template."""
    if args.template_name == "model-onboarding":
        if not args.model:
            print("[ERROR] --model required for model-onboarding template")
            sys.exit(1)
        template_model_onboarding(args.model)
    elif args.template_name == "chatter-onboarding":
        if not args.chatter or not args.tl:
            print("[ERROR] --chatter and --tl required for chatter-onboarding template")
            sys.exit(1)
        template_chatter_onboarding(args.chatter, args.tl)
    elif args.template_name == "weekly":
        template_weekly()
    else:
        print(f"[ERROR] Unknown template: {args.template_name}")
        print("Available: model-onboarding, chatter-onboarding, weekly")


# ══════════════════════════════════════════════════════════════
# PHASE 3: DAILY DIGEST
# ══════════════════════════════════════════════════════════════

def cmd_digest(args):
    """Generate daily digest. Optionally send to Slack."""
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)

    overdue_items = []
    due_today_items = []
    completed_yesterday = []
    person_stats = {}
    board_stats = {}

    for board_key, board in BOARDS.items():
        items, board_name = query_board_items(board["id"])
        b_active = 0
        b_overdue = 0

        for item in items:
            parsed = parse_item(item, board)
            assignee = parsed.get("assignee", "Unassigned") or "Unassigned"
            person_stats.setdefault(assignee, {"active": 0, "overdue": 0})

            if is_done(parsed, board):
                # Check if completed recently (we can't know exact date,
                # but items in Done group are considered completed)
                continue

            b_active += 1
            person_stats[assignee]["active"] += 1

            if is_overdue(parsed):
                parsed["_board"] = board_name
                overdue_items.append(parsed)
                b_overdue += 1
                person_stats[assignee]["overdue"] += 1

            if is_due_today(parsed):
                parsed["_board"] = board_name
                due_today_items.append(parsed)

        board_stats[board_name] = {"active": b_active, "overdue": b_overdue}

    # Format output
    lines = []
    lines.append(f"🤖 *Monday Daily Digest* — {today.strftime('%B %d, %Y')}")
    lines.append("")

    if overdue_items:
        lines.append(f"🔴 *OVERDUE ({len(overdue_items)})*")
        for item in sorted(overdue_items, key=lambda x: x.get("deadline", "")):
            assignee = item.get("assignee", "?") or "?"
            lines.append(f"• _{item['name'][:50]}_ → {assignee} (due {item.get('deadline', '?')}) — {item['_board']}")
        lines.append("")

    if due_today_items:
        lines.append(f"📌 *DUE TODAY ({len(due_today_items)})*")
        for item in due_today_items:
            assignee = item.get("assignee", "?") or "?"
            lines.append(f"• _{item['name'][:50]}_ → {assignee} — {item['_board']}")
        lines.append("")

    if not overdue_items and not due_today_items:
        lines.append("✅ *No overdue or due-today tasks!*")
        lines.append("")

    # Board summary
    lines.append("📊 *BY BOARD*")
    for bname, stats in board_stats.items():
        flag = " 🔴" if stats["overdue"] > 0 else ""
        lines.append(f"• {bname}: {stats['active']} active, {stats['overdue']} overdue{flag}")
    lines.append("")

    # Person summary
    active_people = {k: v for k, v in person_stats.items() if v["active"] > 0}
    if active_people:
        lines.append("👥 *BY PERSON*")
        for person, counts in sorted(active_people.items(), key=lambda x: -x[1]["active"]):
            flag = " 🔴" if counts["overdue"] > 0 else ""
            lines.append(f"• {person}: {counts['active']} active, {counts['overdue']} overdue{flag}")
        lines.append("")

    total_active = sum(s["active"] for s in board_stats.values())
    total_overdue = sum(s["overdue"] for s in board_stats.values())
    lines.append(f"_Total: {total_active} active tasks, {total_overdue} overdue across {len(BOARDS)} boards_")

    digest_text = "\n".join(lines)

    # Print
    print(digest_text)

    # Send to Slack if requested
    if args.send_slack:
        try:
            from slack_cli import send_message, resolve_user_id
            # Send to Pau's DM
            pau_id = resolve_user_id("Pau")
            if pau_id:
                send_message(pau_id, digest_text)
                print(f"\n[OK] Digest sent to Pau via Slack DM")
            else:
                print(f"\n[WARN] Could not resolve Pau's Slack ID. Digest printed above.")
        except Exception as e:
            print(f"\n[WARN] Could not send to Slack: {e}")
            print("Digest printed above. Send manually if needed.")

    return digest_text


# ══════════════════════════════════════════════════════════════
# PHASE 4: BOARD DESCRIPTIONS
# ══════════════════════════════════════════════════════════════

# Dropdown labels to populate on each board
DROPDOWN_LABELS = {
    "master": {
        "dropdown_mm0jqg03": ["Chatting", "Scripts", "Content", "Hiring", "Data", "QA", "Strategy", "Other"],
    },
    "chatting": {
        "dropdown_mm0jqdw8": ["Coaching", "Performance", "Schedule", "Probation", "Traffic", "Investigation", "QA", "Other"],
    },
    "scripts": {
        "dropdown_mm0j83dp": ["New Model", "Script Update", "Diversify", "Smart Messages", "QA Check", "Infloww Import", "Other"],
    },
    "content": {
        "dropdown_mm0jnsbf": ["Content Request", "Custom Order", "Deep Dive", "Client Report", "Model Onboarding", "Model Offboarding", "Other"],
    },
    "hiring": {
        "dropdown_mm0j956e": ["Screening", "Interview", "Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Probation W1", "Probation W2", "Hired", "Declined"],
    },
}


def cmd_fix_dropdowns(args):
    """Replace empty dropdown columns with status columns (Monday API doesn't support dropdown defaults).
    This deletes old dropdown cols and creates status cols with proper labels.
    Updates the config IDs at the end."""
    import time
    print("\n🔧 Replacing dropdown columns with status columns...\n")

    DROPDOWN_TITLES = {
        "master":   {"dropdown_mm0jqg03": "Department"},
        "chatting": {"dropdown_mm0jqdw8": "Category"},
        "scripts":  {"dropdown_mm0j83dp": "Type"},
        "content":  {"dropdown_mm0jnsbf": "Type"},
        "hiring":   {"dropdown_mm0j956e": "Stage"},
    }

    new_ids = {}

    for board_key, columns in DROPDOWN_LABELS.items():
        board = BOARDS[board_key]
        bid = board["id"]

        for old_col_id, labels in columns.items():
            title = DROPDOWN_TITLES.get(board_key, {}).get(old_col_id, "Tag")

            # Step 1: Delete old empty dropdown column
            try:
                query(f'mutation {{ delete_column(board_id: {bid}, column_id: "{old_col_id}") {{ id }} }}')
                print(f"  ✓ Deleted old dropdown: {title} on {board['name']}")
            except Exception as e:
                print(f"  ! Could not delete {old_col_id}: {e}")
            time.sleep(1)

            # Step 2: Create new status column with labels
            label_map = {str(i): lbl for i, lbl in enumerate(labels)}
            defaults = {"labels": label_map}
            defaults_json = json.dumps(json.dumps(defaults))

            try:
                data = query(f'''
                mutation {{
                    create_column(
                        board_id: {bid}
                        title: "{title}"
                        column_type: status
                        defaults: {defaults_json}
                    ) {{
                        id
                        title
                    }}
                }}
                ''')
                new_id = data["create_column"]["id"]
                new_ids.setdefault(board_key, {})[old_col_id] = new_id
                print(f"  ✓ Created status column: {title} → {new_id} ({len(labels)} labels)")
            except Exception as e:
                print(f"  ✗ Could not create {title}: {e}")
            time.sleep(1)

    # Print new IDs for config update
    print(f"\n{'─'*55}")
    print("NEW COLUMN IDs (update config in monday_tasks.py):")
    print(f"{'─'*55}")
    for board_key, mappings in new_ids.items():
        for old_id, new_id in mappings.items():
            print(f"  {board_key}: {old_id} → {new_id}")

    print(f"\n[OK] Done. Update the BOARDS config and DROPDOWN_LABELS with new IDs.\n")


BOARD_DESCRIPTIONS = {
    "master": (
        "🤖 CW Master Tasks — Pau's Command Center\\n\\n"
        "This is the CENTRAL board for all cross-department tasks. "
        "Pau creates tasks here for anyone in the company.\\n\\n"
        "GROUPS:\\n"
        "• 🔴 Urgent — Critical tasks, due ASAP\\n"
        "• 📌 This Week — Important tasks for this week\\n"
        "• 📋 Backlog — Planned but not urgent\\n"
        "• ✅ Done — Completed (move here when finished)\\n"
        "• ❌ Cancelled — No longer needed\\n\\n"
        "HOW TO USE:\\n"
        "1. Check this board daily for new tasks assigned to you\\n"
        "2. Update Status when you start working\\n"
        "3. Move to ✅ Done when complete\\n"
        "4. If blocked, set Status to Stuck and add a note"
    ),
    "chatting": (
        "🤖 CW Chatting Ops — Chatting Department Tasks\\n\\n"
        "Owner: Ryzel (Chatter Manager)\\n"
        "Team: Danilyn, Huckle, Ezekiel (TLs)\\n\\n"
        "CATEGORIES (use the dropdown):\\n"
        "• Coaching — Coaching sessions, feedback tasks\\n"
        "• Performance — KPI reviews, performance investigations\\n"
        "• Schedule — Shift scheduling, model assignments\\n"
        "• Probation — New chatter monitoring\\n"
        "• Traffic — Workload balancing, fan/hr imbalances\\n"
        "• Investigation — Account reviews, incident investigations\\n"
        "• QA — Quality checks on chats\\n\\n"
        "WORKFLOW: ◉ To Do → ▶ In Progress → ⏸ Waiting (if blocked) → ✅ Done"
    ),
    "scripts": (
        "🤖 CW Scripts — Script Management Pipeline\\n\\n"
        "Owner: Rei (Script Manager)\\n"
        "Team: Cath (Script Assistant)\\n\\n"
        "TYPES (use the dropdown):\\n"
        "• New Model — Full script package for a new model\\n"
        "• Script Update — Modify existing scripts\\n"
        "• Diversify — Add variety to sexting sequences\\n"
        "• Smart Messages — Create/update Infloww smart messages\\n"
        "• QA Check — Quality review of scripts\\n"
        "• Infloww Import — Upload scripts to Infloww CRM\\n\\n"
        "WORKFLOW: 📋 Backlog → 🔨 In Progress → 🔍 Review → ✅ Done\\n"
        "Always set the Model field so we know which model it's for."
    ),
    "content": (
        "🤖 CW Content & Clients — Content and Client Management\\n\\n"
        "Owner: Angeles\\n\\n"
        "TYPES (use the dropdown):\\n"
        "• Content Request — Request content from models/agencies\\n"
        "• Custom Order — Fan custom orders (video, photo, VC, audio)\\n"
        "• Deep Dive — Revenue analysis per model\\n"
        "• Client Report — Client communication and follow-ups\\n"
        "• Model Onboarding — New model setup\\n"
        "• Model Offboarding — Model departure process\\n\\n"
        "WORKFLOW: 📋 New Requests → 🔨 In Progress → ⏳ Waiting → ✅ Completed\\n"
        "Set Client and Model fields for proper tracking."
    ),
    "hiring": (
        "🤖 CW Hiring — Recruitment Pipeline\\n\\n"
        "Owner: Mileh (Hiring Manager)\\n\\n"
        "PIPELINE STAGES (groups):\\n"
        "• 📝 Applicants — New applications received\\n"
        "• 🎤 Interview — Scheduled/completed interviews\\n"
        "• 📚 Training — 5-day training program (Days 1-5)\\n"
        "• ⏳ Probation — 14-day supervised period\\n"
        "• ✅ Hired — Successfully completed probation\\n"
        "• ❌ Declined — Did not pass\\n\\n"
        "Move items between groups as recruits advance through the pipeline.\\n"
        "Record Test Score (screening) and Exam Score (final exam).\\n"
        "Set TL Assigned when recruit enters probation."
    ),
}


def cmd_setup_descriptions(args):
    """Add descriptions to all 🤖 boards."""
    print("\n📝 Setting board descriptions...\n")

    for board_key, desc in BOARD_DESCRIPTIONS.items():
        board = BOARDS[board_key]
        bid = board["id"]
        try:
            # update_board returns JSON scalar, no subfield selection
            escaped = desc.replace('"', '\\"')
            resp = query(f'''
            mutation {{
                update_board (
                    board_id: {bid}
                    board_attribute: description
                    new_value: "{escaped}"
                )
            }}
            ''')
            print(f"  ✓ {board['name']} — description set")
        except Exception as e:
            print(f"  ✗ {board['name']} — failed: {e}")

    print("\n[OK] All board descriptions updated.\n")


# ══════════════════════════════════════════════════════════════
# MAIN — Argument Parser
# ══════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="🤖 Monday Task Manager — Chatting Wizard",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command")

    # ── create ──
    p = sub.add_parser("create", help="Create a task (auto-routes to correct board)")
    p.add_argument("name", help="Task name/title")
    p.add_argument("--assignee", "-a", required=True, help="Person name (e.g. Ryzel, Rei, Angeles)")
    p.add_argument("--priority", "-p", default="medium", choices=["critical", "high", "medium", "low"])
    p.add_argument("--deadline", "-d", default=None, help="Deadline (YYYY-MM-DD)")
    p.add_argument("--description", default=None, help="Task description")
    p.add_argument("--board", "-b", default=None, help="Force specific board (master, chatting, scripts, content, hiring)")
    p.add_argument("--department", default=None, help="Department (for Master Tasks board)")
    p.add_argument("--category", default=None, help="Category (for Chatting Ops board)")
    p.add_argument("--type", default=None, help="Type (for Scripts/Content boards)")
    p.add_argument("--model", default=None, help="Model name (for Scripts/Content boards)")
    p.add_argument("--client", default=None, help="Client name (for Content board)")
    p.add_argument("--notes", default=None, help="Additional notes (for Master Tasks)")

    # ── summary ──
    sub.add_parser("summary", help="Overview of all boards (active, overdue, by person)")

    # ── overdue ──
    sub.add_parser("overdue", help="Show all overdue tasks")

    # ── person ──
    p = sub.add_parser("person", help="Show tasks for a specific person")
    p.add_argument("name", help="Person name (e.g. Ryzel, Rei, Angeles)")

    # ── board ──
    p = sub.add_parser("board", help="Show active tasks on a specific board")
    p.add_argument("name", help="Board name (master, chatting, scripts, content, hiring)")

    # ── template ──
    p = sub.add_parser("template", help="Run a task template")
    p.add_argument("template_name", choices=["model-onboarding", "chatter-onboarding", "weekly"])
    p.add_argument("--model", default=None, help="Model name (for model-onboarding)")
    p.add_argument("--chatter", default=None, help="Chatter name (for chatter-onboarding)")
    p.add_argument("--tl", default=None, help="TL name (for chatter-onboarding)")

    # ── digest ──
    p = sub.add_parser("digest", help="Generate daily digest")
    p.add_argument("--send-slack", action="store_true", help="Send digest to Pau via Slack DM")

    # ── setup-descriptions ──
    sub.add_parser("setup-descriptions", help="Set board descriptions (run once)")

    # ── fix-dropdowns ──
    sub.add_parser("fix-dropdowns", help="Populate dropdown labels on all boards (run once)")

    args = parser.parse_args()

    cmds = {
        "create": cmd_create,
        "summary": cmd_summary,
        "overdue": cmd_overdue,
        "person": cmd_person,
        "board": cmd_board,
        "template": cmd_template,
        "digest": cmd_digest,
        "setup-descriptions": cmd_setup_descriptions,
        "fix-dropdowns": cmd_fix_dropdowns,
    }

    if args.command in cmds:
        cmds[args.command](args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
