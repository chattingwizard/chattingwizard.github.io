import os
import sys
import requests

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

token = os.environ.get("AIRTABLE_TOKEN", "")
base_id = "appy0qGaMEfyDz9LZ"

r = requests.get(
    f"https://api.airtable.com/v0/meta/bases/{base_id}/tables",
    headers={"Authorization": f"Bearer {token}"}
)
data = r.json()
tables = data.get("tables", [])

if not tables:
    print("Error:", data)
else:
    for t in tables:
        fields = [f["name"] for f in t.get("fields", [])]
        print(f"\n=== {t['name']} (ID: {t['id']}) ===")
        print(f"  Fields: {', '.join(fields[:15])}")
        if len(fields) > 15:
            print(f"  ... +{len(fields)-15} more fields")
    print(f"\nTotal: {len(tables)} tables")
