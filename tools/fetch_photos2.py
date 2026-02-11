import os, sys, json, requests
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

token = os.environ.get("AIRTABLE_TOKEN", "")
base_id = "appy0qGaMEfyDz9LZ"
table_id = "tbl97sE9V8wbcgjAJ"

# Fetch all records to find Putri (might be under a different name)
r = requests.get(
    f"https://api.airtable.com/v0/{base_id}/{table_id}",
    headers={"Authorization": f"Bearer {token}"},
    params={"pageSize": 100}
)
data = r.json()
records = data.get("records", [])
print(f"Total records: {len(records)}")
for rec in records:
    fields = rec.get("fields", {})
    name = fields.get("Model Name", "???")
    print(f"  - {name}")
