"""Pre-flight check: verify Airtable data before onboarding."""
import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
from airtable_cli import get_model_info

for name in ["Skylar", "Laura Soler"]:
    print(f"=== {name} ===")
    info = get_model_info(name)
    if not info:
        print(f"  NOT FOUND in Airtable\n")
        continue
    print(f"  Gender: {info['gender']}")
    print(f"  Age: {info['age']}")
    print(f"  Nationality: {info['nationality']}")
    print(f"  Location: {info['location']}")
    print(f"  Traffic: {info['traffic_display']} -> {info['traffic']}")
    print(f"  Explicit: {info['explicit_level']}")
    print(f"  Personality: {info['personality'][:150]}")
    print(f"  Voice: {info['voice'][:100]}")
    print(f"  Pet names: {info['voice_pet_names']}")
    print(f"  Interests: {info['interests']}")
    print(f"  Job: {info['job']}")
    print(f"  Physical: {info['physical']}")
    print(f"  Special notes: {info.get('special_notes', '')[:150]}")
    print()
