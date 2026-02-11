import os, sys, json, requests
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

token = os.environ.get("AIRTABLE_TOKEN", "")
base_id = "appy0qGaMEfyDz9LZ"
table_id = "tbl97sE9V8wbcgjAJ"

for name in ["Max", "Putri"]:
    r = requests.get(
        f"https://api.airtable.com/v0/{base_id}/{table_id}",
        headers={"Authorization": f"Bearer {token}"},
        params={"filterByFormula": f'{{Model Name}}="{name}"', "pageSize": 1}
    )
    data = r.json()
    records = data.get("records", [])
    if records:
        fields = records[0].get("fields", {})
        # Look for any field that contains attachments (photo/image)
        for k, v in sorted(fields.items()):
            if isinstance(v, list) and len(v) > 0 and isinstance(v[0], dict):
                # This is likely an attachment field
                print(f"=== {name} — Field: {k} ===")
                for att in v[:3]:  # first 3 attachments
                    print(f"  URL: {att.get('url', 'N/A')}")
                    print(f"  Filename: {att.get('filename', 'N/A')}")
                    print(f"  Type: {att.get('type', 'N/A')}")
                    thumbs = att.get('thumbnails', {})
                    if thumbs:
                        large = thumbs.get('large', {})
                        if large:
                            print(f"  Thumbnail (large): {large.get('url', 'N/A')}")
                    print()
    else:
        print(f"No record found for {name}")
