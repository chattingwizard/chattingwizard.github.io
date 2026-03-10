"""Check Monday item details for Desconocida onboarding."""
import sys, os, json
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from monday_cli import get_headers, API_URL as MONDAY_API

import requests

BOARD_ID = "5018047892"
headers = get_headers()

query = """
query {
  boards(ids: [%s]) {
    items_page(limit: 50) {
      items {
        id
        name
        group { title }
        column_values {
          id
          text
          value
        }
        updates {
          text_body
          created_at
        }
      }
    }
  }
}
""" % BOARD_ID

r = requests.post(MONDAY_API, headers=headers, json={"query": query})
r.raise_for_status()
data = r.json()

items = data.get("data", {}).get("boards", [{}])[0].get("items_page", {}).get("items", [])

for item in items:
    cols = {cv["id"]: cv["text"] for cv in item.get("column_values", [])}
    status = cols.get("status", "").lower()
    group = item.get("group", {}).get("title", "")
    
    # Show items with "progress" or "confirmed" or recent ones
    if "progress" in status or "confirmed" in status.lower() or "lucas" in item["name"].lower() or "desconocida" in str(cols).lower():
        print(f"=== {item['name']} ===")
        print(f"  ID: {item['id']}")
        print(f"  Group: {group}")
        print(f"  Status: {cols.get('status', '?')}")
        for cv in item.get("column_values", []):
            if cv["text"] and cv["text"].strip():
                print(f"  {cv['id']}: {cv['text']}")
        if item.get("updates"):
            print(f"  Updates:")
            for u in item["updates"][:3]:
                print(f"    [{u['created_at']}] {u['text_body'][:200]}")
        print()
