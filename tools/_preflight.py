"""Pre-flight check for Justin Daniels."""
import sys, os
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from airtable_cli import get_model_info, get_headers, API_BASE
import requests

info = get_model_info("Justin Daniels")
if not info:
    print("NOT FOUND")
else:
    print(f"  Name: {info['name']}")
    print(f"  Gender: {info['gender']}")
    print(f"  Age: {info['age']}")
    print(f"  Nationality: {info['nationality']}")
    print(f"  Location: {info['location']}")
    print(f"  Traffic: {info['traffic_display']} -> {info['traffic']}")
    print(f"  Explicit: {info['explicit_level']}")
    print(f"  Personality: {info['personality'][:300]}")
    print(f"  Voice: {info['voice'][:150]}")
    print(f"  Pet names: {info['voice_pet_names']}")
    print(f"  Interests: {info['interests']}")
    print(f"  Job: {info['job']}")
    print(f"  Physical: {info['physical']}")
    print(f"  Countries: {info.get('countries', '')}")
    print(f"  Special notes: {info.get('special_notes', '')[:300]}")

# Full raw data
headers = get_headers()
r = requests.get(API_BASE, headers=headers, params={
    'filterByFormula': '{Model Name} = "Justin Daniels"',
})
r.raise_for_status()
records = r.json().get('records', [])
print("\n=== RAW FIELDS ===")
for rec in records:
    f = rec.get('fields', {})
    for key in sorted(f.keys()):
        val = f[key]
        if isinstance(val, list) and len(val) > 0 and isinstance(val[0], dict) and 'url' in val[0]:
            print(f"  {key}: [attachment]")
            for att in val:
                print(f"    filename: {att.get('filename', '?')}")
        else:
            print(f"  {key}: {val}")
