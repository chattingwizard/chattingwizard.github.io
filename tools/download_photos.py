import os, sys, requests
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

token = os.environ.get("AIRTABLE_TOKEN", "")
base_id = "appy0qGaMEfyDz9LZ"
table_id = "tbl97sE9V8wbcgjAJ"

models = {"Putri OFTV": "putri", "Max": "max"}

for airtable_name, folder in models.items():
    r = requests.get(
        f"https://api.airtable.com/v0/{base_id}/{table_id}",
        headers={"Authorization": f"Bearer {token}"},
        params={"filterByFormula": f'{{Model Name}}="{airtable_name}"', "pageSize": 1}
    )
    data = r.json()
    records = data.get("records", [])
    if not records:
        print(f"NOT FOUND: {airtable_name}")
        continue
    
    fields = records[0].get("fields", {})
    pic = fields.get("Profile Picture", [])
    if not pic:
        print(f"NO PHOTO: {airtable_name}")
        continue
    
    url = pic[0].get("url", "")
    fname = pic[0].get("filename", "photo.jpg")
    ext = fname.split(".")[-1] if "." in fname else "jpg"
    
    # Download
    print(f"Downloading {airtable_name}...")
    img = requests.get(url)
    
    # Save to folder
    out_dir = os.path.join(folder)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"profile.{ext}")
    with open(out_path, "wb") as f:
        f.write(img.content)
    print(f"  Saved: {out_path} ({len(img.content)} bytes)")
