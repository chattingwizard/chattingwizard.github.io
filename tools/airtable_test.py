import os
import requests

token = os.environ.get("AIRTABLE_TOKEN", "")
if not token:
    print("ERROR: AIRTABLE_TOKEN not set")
    exit(1)

r = requests.get(
    "https://api.airtable.com/v0/meta/bases",
    headers={"Authorization": f"Bearer {token}"}
)
data = r.json()
bases = data.get("bases", [])

if not bases:
    print("Error:", data)
else:
    for b in bases:
        print(f"{b['id']}  {b['name']}")
    print(f"\nTotal: {len(bases)} bases")
