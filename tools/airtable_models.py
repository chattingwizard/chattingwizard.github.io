import os
import sys
import requests

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

token = os.environ.get("AIRTABLE_TOKEN", "")
base_id = "appy0qGaMEfyDz9LZ"
table_id = "tbl97sE9V8wbcgjAJ"  # Models

r = requests.get(
    f"https://api.airtable.com/v0/{base_id}/{table_id}",
    headers={"Authorization": f"Bearer {token}"},
    params={"pageSize": 100}
)
data = r.json()
records = data.get("records", [])

if not records:
    print("No records or error:", data)
else:
    print(f"{'Model Name':<25} {'Status':<15} {'Age':<5} {'Nationality':<20} {'Page Type'}")
    print("-" * 85)
    for rec in records:
        f = rec.get("fields", {})
        name = f.get("Model Name", "?")
        status = f.get("Status", "?")
        age = str(f.get("Age", "?"))
        nat = f.get("Nationality", "?")
        ptype = f.get("Page Type", "?")
        print(f"{name:<25} {status:<15} {age:<5} {nat:<20} {ptype}")
    print(f"\nTotal: {len(records)} models")
