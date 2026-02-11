import os, sys, requests
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

model_name = sys.argv[1] if len(sys.argv) > 1 else "Max"
token = os.environ.get("AIRTABLE_TOKEN", "")
base_id = "appy0qGaMEfyDz9LZ"
table_id = "tbl97sE9V8wbcgjAJ"

r = requests.get(
    f"https://api.airtable.com/v0/{base_id}/{table_id}",
    headers={"Authorization": f"Bearer {token}"},
    params={"filterByFormula": f"{{Model Name}}=\"{model_name}\"", "pageSize": 1}
)
data = r.json()
records = data.get("records", [])

if records:
    fields = records[0].get("fields", {})
    for k, v in sorted(fields.items()):
        if isinstance(v, list) and len(v) > 0 and isinstance(v[0], dict):
            print(f"{k}: [attachment/linked]")
        else:
            print(f"{k}: {v}")
else:
    print("No record found:", data)
