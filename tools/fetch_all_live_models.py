"""Fetch ALL fields for every LIVE model from Airtable."""
import os, sys, requests, json
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

token = os.environ.get("AIRTABLE_TOKEN", "")
base_id = "appy0qGaMEfyDz9LZ"
table_id = "tbl97sE9V8wbcgjAJ"

# Key fields to fetch
FIELDS = [
    "Model Name", "Status", "Age", "Nationality", "Page Type", "Location",
    "Height", "Weight", "Boobs Size", "Hair Color and Type", "Eye Color",
    "Tattoos", "Languages", "Bio", "Notes", "Traffic", "Niche",
    "Countries Visited", "Current Job", "Previous Job before OnlyFans",
    "Sports", "Favorite Food", "Smoking", "Drinking", "Partner", "Children",
    "Masturbation", "Anal", "Squirting", "B/G", "G/G", "Custom", "Video Calls",
    "Price Guide", "Branding Guideline", "Instagram Link", "Shoe Size",
    "Surgeries", "Birthday", "CHATBOT", "Scripts"
]

all_records = []
offset = None

while True:
    params = {
        "filterByFormula": "{Status} = 'Live'",
        "pageSize": 100,
    }
    if offset:
        params["offset"] = offset
    
    r = requests.get(
        f"https://api.airtable.com/v0/{base_id}/{table_id}",
        headers={"Authorization": f"Bearer {token}"},
        params=params
    )
    data = r.json()
    all_records.extend(data.get("records", []))
    offset = data.get("offset")
    if not offset:
        break

print(f"Total LIVE models: {len(all_records)}\n")

for rec in sorted(all_records, key=lambda x: x["fields"].get("Model Name", "")):
    f = rec["fields"]
    name = f.get("Model Name", "?")
    print("=" * 80)
    print(f"MODEL: {name}")
    print("=" * 80)
    for key in FIELDS:
        val = f.get(key)
        if val and val not in [None, "", [], {}]:
            # Clean up display
            if isinstance(val, list):
                if all(isinstance(v, str) for v in val):
                    val = ", ".join(val)
                else:
                    val = json.dumps(val, ensure_ascii=False)[:200]
            elif isinstance(val, dict):
                val = json.dumps(val, ensure_ascii=False)[:200]
            print(f"  {key}: {val}")
    print()
