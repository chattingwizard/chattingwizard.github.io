import os, sys, requests
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

token = os.environ.get("AIRTABLE_TOKEN", "")
base_id = "appy0qGaMEfyDz9LZ"
table_id = "tbl97sE9V8wbcgjAJ"

for name in ["Putri OFTV", "Max"]:
    r = requests.get(
        f"https://api.airtable.com/v0/{base_id}/{table_id}",
        headers={"Authorization": f"Bearer {token}"},
        params={"filterByFormula": f'{{Model Name}}="{name}"', "pageSize": 1}
    )
    data = r.json()
    records = data.get("records", [])
    if records:
        fields = records[0].get("fields", {})
        for k, v in sorted(fields.items()):
            if isinstance(v, list) and len(v) > 0 and isinstance(v[0], dict):
                print(f"=== {name} — {k} ===")
                for att in v[:2]:
                    url = att.get('url', '')
                    fname = att.get('filename', '')
                    thumbs = att.get('thumbnails', {})
                    large = thumbs.get('large', {}).get('url', '')
                    print(f"  file: {fname}")
                    print(f"  url: {url}")
                    print(f"  thumb: {large}")
                    print()
    else:
        print(f"NOT FOUND: {name}")
