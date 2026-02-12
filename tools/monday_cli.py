"""
Monday.com CLI — Read boards, items, and detect new onboardings.

Usage:
    python tools/monday_cli.py boards                         # List all boards
    python tools/monday_cli.py items <board_id> [--limit N]   # List items in a board
    python tools/monday_cli.py columns <board_id>             # Show board columns/structure
    python tools/monday_cli.py item <item_id>                 # Get full item details
    python tools/monday_cli.py onboardings                    # Detect new onboardings

Env var required: MONDAY_API_TOKEN
"""

import argparse
import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

try:
    import requests
except ImportError:
    print("ERROR: requests not installed. Run: pip install requests")
    sys.exit(1)

API_URL = "https://api.monday.com/v2"
TOKEN_ENV = "MONDAY_API_TOKEN"


def get_headers():
    token = os.environ.get(TOKEN_ENV)
    if not token:
        print(f"ERROR: {TOKEN_ENV} not set.")
        print(f"Set it: $env:MONDAY_API_TOKEN = 'your-token'")
        sys.exit(1)
    return {
        "Authorization": token,
        "Content-Type": "application/json",
        "API-Version": "2024-10",
    }


def query(q, variables=None):
    """Execute a GraphQL query against Monday.com API."""
    payload = {"query": q}
    if variables:
        payload["variables"] = variables
    resp = requests.post(API_URL, json=payload, headers=get_headers())
    resp.raise_for_status()
    data = resp.json()
    if "errors" in data:
        for e in data["errors"]:
            print(f"[API ERROR] {e.get('message', e)}")
        sys.exit(1)
    return data.get("data", {})


# ── Commands ──────────────────────────────────────────────────

def cmd_boards(args):
    """List all boards."""
    data = query("""
    {
        boards(limit: 50) {
            id
            name
            state
            items_count
        }
    }
    """)
    boards = data.get("boards", [])
    print(f"{'Board Name':<45} {'Items':>6}  {'State':<10} {'ID'}")
    print("-" * 90)
    for b in boards:
        print(f"{b['name']:<45} {b.get('items_count', '?'):>6}  {b['state']:<10} {b['id']}")
    print(f"\nTotal: {len(boards)} boards")


def cmd_columns(args):
    """Show board columns/structure."""
    data = query("""
    query ($boardId: [ID!]!) {
        boards(ids: $boardId) {
            name
            columns {
                id
                title
                type
                settings_str
            }
            groups {
                id
                title
            }
        }
    }
    """, {"boardId": [args.board_id]})

    boards = data.get("boards", [])
    if not boards:
        print(f"Board {args.board_id} not found")
        return

    board = boards[0]
    print(f"\nBoard: {board['name']}")
    print(f"\n{'Column Title':<30} {'Type':<15} {'ID'}")
    print("-" * 60)
    for col in board["columns"]:
        print(f"{col['title']:<30} {col['type']:<15} {col['id']}")

    if board.get("groups"):
        print(f"\n{'Group':<30} {'ID'}")
        print("-" * 45)
        for g in board["groups"]:
            print(f"{g['title']:<30} {g['id']}")


def cmd_items(args):
    """List items in a board."""
    data = query("""
    query ($boardId: [ID!]!, $limit: Int!) {
        boards(ids: $boardId) {
            name
            items_page(limit: $limit) {
                items {
                    id
                    name
                    group {
                        title
                    }
                    column_values {
                        id
                        text
                        value
                        type
                    }
                }
            }
        }
    }
    """, {"boardId": [args.board_id], "limit": args.limit})

    boards = data.get("boards", [])
    if not boards:
        print(f"Board {args.board_id} not found")
        return

    board = boards[0]
    items = board.get("items_page", {}).get("items", [])
    print(f"\nBoard: {board['name']} — {len(items)} items\n")

    for item in items:
        group = item.get("group", {}).get("title", "?")
        print(f"[{item['id']}] {item['name']} (Group: {group})")
        for cv in item.get("column_values", []):
            text = cv.get("text", "")
            if text:
                print(f"  {cv['id']:<20} = {text}")
        print()


def cmd_item(args):
    """Get full details of a single item."""
    data = query("""
    query ($itemId: [ID!]!) {
        items(ids: $itemId) {
            id
            name
            group {
                title
            }
            column_values {
                id
                text
                value
                type
            }
        }
    }
    """, {"itemId": [args.item_id]})

    items = data.get("items", [])
    if not items:
        print(f"Item {args.item_id} not found")
        return

    item = items[0]
    group = item.get("group", {}).get("title", "?")
    print(f"\nItem: {item['name']} (ID: {item['id']}, Group: {group})\n")
    print(f"{'Column':<25} {'Type':<15} {'Value'}")
    print("-" * 70)
    for cv in item.get("column_values", []):
        text = cv.get("text", "") or ""
        title = cv.get("title", cv["id"])
        print(f"{title:<25} {cv['type']:<15} {text[:50]}")


def cmd_onboardings(args):
    """Detect new onboardings (items not in 'Live' status)."""
    # First, find the board
    data = query("""
    {
        boards(limit: 50) {
            id
            name
        }
    }
    """)

    board_id = None
    for b in data.get("boards", []):
        if "clientonoffboarding" in b["name"].lower().replace(" ", ""):
            board_id = b["id"]
            break

    if not board_id:
        print("[ERROR] Board 'clientonoffboarding' not found")
        return

    # Get all items
    data = query("""
    query ($boardId: [ID!]!) {
        boards(ids: $boardId) {
            name
            items_page(limit: 200) {
                items {
                    id
                    name
                    group {
                        title
                    }
                    column_values {
                        id
                        title
                        text
                        value
                        type
                    }
                }
            }
        }
    }
    """, {"boardId": [board_id]})

    boards = data.get("boards", [])
    if not boards:
        return

    items = boards[0].get("items_page", {}).get("items", [])

    # Find items that are NOT "Live" — these are potential new onboardings
    new_onboardings = []
    live_items = []

    for item in items:
        status = ""
        creator = item["name"]
        cols = {}
        for cv in item.get("column_values", []):
            cols[cv["id"]] = cv.get("text", "")
            if cv.get("title", "").lower() == "status" or cv["id"] == "status":
                status = cv.get("text", "").lower()

        if "live" in status:
            live_items.append(creator)
        else:
            new_onboardings.append({
                "id": item["id"],
                "name": creator,
                "status": status,
                "group": item.get("group", {}).get("title", "?"),
                "columns": cols,
            })

    print(f"\n[Monday] Board: {boards[0]['name']}")
    print(f"  Live: {len(live_items)} models")
    print(f"  New/Pending: {len(new_onboardings)} models\n")

    if new_onboardings:
        print("NEW ONBOARDINGS:")
        print("-" * 60)
        for ob in new_onboardings:
            print(f"  [{ob['id']}] {ob['name']} — Status: {ob['status'] or 'empty'} (Group: {ob['group']})")
            for k, v in ob["columns"].items():
                if v and k != "status":
                    print(f"    {k}: {v}")
            print()
    else:
        print("[OK] No new onboardings pending")

    return new_onboardings


# ── Main ──────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Monday.com CLI")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("boards", help="List all boards")

    p = sub.add_parser("columns", help="Show board columns")
    p.add_argument("board_id", help="Board ID")

    p = sub.add_parser("items", help="List items in board")
    p.add_argument("board_id", help="Board ID")
    p.add_argument("--limit", type=int, default=50)

    p = sub.add_parser("item", help="Get item details")
    p.add_argument("item_id", help="Item ID")

    sub.add_parser("onboardings", help="Detect new onboardings")

    args = parser.parse_args()

    cmds = {
        "boards": cmd_boards,
        "columns": cmd_columns,
        "items": cmd_items,
        "item": cmd_item,
        "onboardings": cmd_onboardings,
    }

    if args.command in cmds:
        cmds[args.command](args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
