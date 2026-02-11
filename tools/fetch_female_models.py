"""Fetch all female LIVE models from Airtable with full details."""
import os, sys, requests, json
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

token = os.environ.get("AIRTABLE_TOKEN", "")
base_id = "appy0qGaMEfyDz9LZ"
table_id = "tbl97sE9V8wbcgjAJ"

FIELDS = [
    "Model Name", "Status", "Age", "Nationality", "Page Type", "Location",
    "Height", "Weight", "Boobs Size", "Hair Color and Type", "Eye Color",
    "Tattoos", "Languages", "Bio", "Notes", "Traffic", "Niche",
    "Countries Visited", "Current Job", "Previous Job before OnlyFans",
    "Sports", "Favorite Food", "Smoking", "Drinking", "Partner", "Children",
    "Masturbation", "Anal", "Squirting", "B/G", "G/G", "Custom", "Video Calls",
    "Price Guide", "Branding Guideline", "Shoe Size", "Surgeries", "Birthday",
    "CHATBOT", "Scripts"
]

all_records = []
offset = None
while True:
    params = {"filterByFormula": "{Status} = 'Live'", "pageSize": 100}
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

# Separate male models (already done: Max, Marco, and pending males)
MALE_MODELS = [
    "Max", "Marco", "Lucas Passione", "3AM feelings Lucas", "Liam",
    "Peter", "Damon", "Stefan", "Zack", "Noah", "Jack Hollywood"
]
SKIP = ["Riri OFTV", "Putri"]  # Already done or skip

print(f"Total LIVE models: {len(all_records)}")
print(f"\n{'='*80}")
print("FEMALE MODELS TO CREATE:")
print(f"{'='*80}")

female_count = 0
output_data = []

for rec in sorted(all_records, key=lambda x: x['fields'].get('Model Name', '')):
    f = rec['fields']
    name = f.get('Model Name', 'Unknown')
    
    # Skip males and already-done
    is_male = any(name.lower().startswith(m.lower()) or m.lower() in name.lower() for m in MALE_MODELS)
    is_skip = any(s.lower() in name.lower() for s in SKIP)
    
    if is_male or is_skip:
        continue
    
    female_count += 1
    
    print(f"\n--- {female_count}. {name} ---")
    print(f"  Age: {f.get('Age', '?')}")
    print(f"  Nationality: {f.get('Nationality', '?')}")
    print(f"  Location: {f.get('Location', '?')}")
    print(f"  Page Type: {f.get('Page Type', '?')}")
    print(f"  Traffic: {f.get('Traffic', '?')}")
    print(f"  Niche: {f.get('Niche', '?')}")
    
    bio = f.get('Bio', '')
    if bio:
        print(f"  Bio: {bio[:200]}...")
    
    notes = f.get('Notes', '')
    if notes:
        print(f"  Notes: {notes[:300]}...")
    
    print(f"  Hair: {f.get('Hair Color and Type', '?')}")
    print(f"  Eyes: {f.get('Eye Color', '?')}")
    print(f"  Tattoos: {f.get('Tattoos', '?')}")
    print(f"  Height: {f.get('Height', '?')}")
    print(f"  Boobs: {f.get('Boobs Size', '?')}")
    print(f"  Current Job: {f.get('Current Job', '?')}")
    print(f"  Sports: {f.get('Sports', '?')}")
    print(f"  Favorite Food: {f.get('Favorite Food', '?')}")
    print(f"  Countries: {f.get('Countries Visited', '?')}")
    print(f"  Partner: {f.get('Partner', '?')}")
    print(f"  Languages: {f.get('Languages', '?')}")
    print(f"  Smoking: {f.get('Smoking', '?')}")
    print(f"  Drinking: {f.get('Drinking', '?')}")
    
    # Content capabilities
    print(f"  Masturbation: {f.get('Masturbation', '?')}")
    print(f"  Anal: {f.get('Anal', '?')}")
    print(f"  Squirting: {f.get('Squirting', '?')}")
    print(f"  B/G: {f.get('B/G', '?')}")
    print(f"  G/G: {f.get('G/G', '?')}")
    print(f"  Custom: {f.get('Custom', '?')}")
    print(f"  Video Calls: {f.get('Video Calls', '?')}")
    print(f"  Price Guide: {f.get('Price Guide', '?')}")
    
    branding = f.get('Branding Guideline', '')
    if branding:
        print(f"  Branding: {branding[:300]}...")
    
    scripts = f.get('Scripts', '')
    if scripts:
        print(f"  Scripts URL: {scripts}")
    
    # Store for output
    model_data = {k: f.get(k, '') for k in FIELDS}
    model_data['_record_id'] = rec['id']
    output_data.append(model_data)

print(f"\n{'='*80}")
print(f"Total female models to create: {female_count}")

# Save clean JSON
with open(r"c:\Users\34683\CW-ScriptManager\cursor_context\female_models_data.json", 'w', encoding='utf-8') as jf:
    json.dump(output_data, jf, ensure_ascii=False, indent=2)
print(f"Saved to cursor_context/female_models_data.json")
