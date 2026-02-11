"""List ALL fields in the Models table."""
import os, sys, requests
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

token = os.environ.get("AIRTABLE_TOKEN", "")
base_id = "appy0qGaMEfyDz9LZ"

r = requests.get(
    f"https://api.airtable.com/v0/meta/bases/{base_id}/tables",
    headers={"Authorization": f"Bearer {token}"}
)
data = r.json()
for t in data.get("tables", []):
    if t["name"] == "Models":
        fields = t.get("fields", [])
        print(f"Models table: {len(fields)} fields\n")
        for i, f in enumerate(fields, 1):
            ftype = f.get("type", "?")
            print(f"  {i:2}. {f['name']:<40} ({ftype})")
        break
