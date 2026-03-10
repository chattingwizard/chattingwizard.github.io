"""Onboard Justin Daniels with Airtable data — MALE, dating app."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from airtable_cli import get_model_info
from onboard_model import create_model_config

info = get_model_info("Justin Daniels")
if not info:
    print("[ERROR] Justin Daniels not found in Airtable")
    sys.exit(1)

# Fix gender — he's male, detector failed
info["gender"] = "male"
# Force solo for scripts
info["explicit_level"] = "full_male"

print(f"  Gender (fixed): {info['gender']}")
print(f"  Age: {info['age']}")
print(f"  Nationality: {info['nationality']}")
print(f"  Traffic: {info['traffic']}")

filepath, folder = create_model_config(info)
print(f"\nConfig: {filepath}")
print(f"Folder: {folder}")
