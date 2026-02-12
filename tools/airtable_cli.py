"""
Airtable CLI — Read model data from Model Info table.

Usage:
    python tools/airtable_cli.py models                   # List all models
    python tools/airtable_cli.py model <name>             # Get full model info
    python tools/airtable_cli.py fields                   # List all field names

Env var required: AIRTABLE_TOKEN (pat...)
"""

import argparse
import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

try:
    import requests
except ImportError:
    print("ERROR: requests not installed.")
    sys.exit(1)

BASE_ID = "appy0qGaMEfyDz9LZ"
TABLE_ID = "tbl97sE9V8wbcgjAJ"
TOKEN_ENV = "AIRTABLE_TOKEN"
API_BASE = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_ID}"


def get_headers():
    token = os.environ.get(TOKEN_ENV)
    if not token:
        print(f"ERROR: {TOKEN_ENV} not set.")
        sys.exit(1)
    return {"Authorization": f"Bearer {token}"}


def fetch_all_records(fields=None):
    """Fetch all records, handling pagination."""
    headers = get_headers()
    params = {}
    if fields:
        params["fields[]"] = fields
    
    all_records = []
    offset = None
    
    while True:
        if offset:
            params["offset"] = offset
        r = requests.get(API_BASE, headers=headers, params=params)
        r.raise_for_status()
        data = r.json()
        all_records.extend(data.get("records", []))
        offset = data.get("offset")
        if not offset:
            break
    
    return all_records


def fetch_model(name):
    """Fetch a specific model by name."""
    headers = get_headers()
    formula = f"{{Model Name}} = '{name}'"
    r = requests.get(API_BASE, headers=headers, params={"filterByFormula": formula})
    r.raise_for_status()
    data = r.json()
    records = data.get("records", [])
    if not records:
        return None
    return records[0].get("fields", {})


def get_model_info(model_name):
    """
    Fetch and parse all model info into a structured dict ready for script creation.
    Returns a dict with all fields needed by onboard_model.py.
    """
    fields = fetch_model(model_name)
    if not fields:
        return None

    # Parse Bio for personality, voice, hook, boundaries
    bio = fields.get("Bio", "")
    
    # Determine gender from bio/niche or default
    bio_lower = bio.lower()
    niche = (fields.get("Niche") or "").lower()
    
    # Traffic parsing
    traffic_raw = fields.get("Traffic", [])
    if isinstance(traffic_raw, list):
        traffic = traffic_raw[0] if traffic_raw else "social_media"
    else:
        traffic = traffic_raw or "social_media"
    
    # Map traffic to internal type
    traffic_lower = traffic.lower()
    if "dating" in traffic_lower or "hinge" in traffic_lower or "tinder" in traffic_lower or "bumble" in traffic_lower:
        traffic_type = "dating_app"
    else:
        traffic_type = "social_media"

    # Page type
    page_type = fields.get("Page Type", "Mixed")

    # Physical description
    physical_parts = []
    if fields.get("Height"): physical_parts.append(fields["Height"].strip())
    if fields.get("Weight"): physical_parts.append(fields["Weight"].strip())
    if fields.get("Hair Color and Type"): physical_parts.append(f"hair: {fields['Hair Color and Type'].strip()}")
    if fields.get("Eye Color"): physical_parts.append(f"eyes: {fields['Eye Color'].strip()}")
    if fields.get("Boobs Size"): physical_parts.append(f"boobs: {fields['Boobs Size'].strip()}")
    if fields.get("Tattoos") and fields["Tattoos"].strip().lower() not in ["no", "none", ""]:
        physical_parts.append(f"tattoos: {fields['Tattoos'].strip()}")
    physical = ", ".join(physical_parts) if physical_parts else "TBD"

    # Interests from Bio
    interests = []
    if fields.get("Sports") and fields["Sports"].strip().lower() not in ["none", "no", ""]:
        interests.append(fields["Sports"].strip())
    if fields.get("Favorite Food") and fields["Favorite Food"].strip().lower() not in ["none", "no", ""]:
        interests.append(f"food: {fields['Favorite Food'].strip()}")

    # Content restrictions
    restrictions = []
    if fields.get("Anal", "").strip().lower() == "no": restrictions.append("No anal")
    if fields.get("Squirting", "").strip().lower() == "no": restrictions.append("No squirting")
    if fields.get("B/G", "").strip().lower() == "no": restrictions.append("No B/G")
    if fields.get("G/G", "").strip().lower() == "no": restrictions.append("No G/G")
    if fields.get("Video Calls", "").strip().lower() == "no": restrictions.append("No video calls")
    
    # Explicit level
    bg = fields.get("B/G", "").strip().lower()
    masturbation = fields.get("Masturbation", "").strip().lower()
    if masturbation == "no" and bg == "no":
        explicit_level = "non_explicit"
    elif bg == "yes":
        explicit_level = "full_bg"
    else:
        explicit_level = "full_solo"
    
    # Special notes
    notes_parts = []
    if restrictions:
        notes_parts.append(". ".join(restrictions))
    if fields.get("Price Guide"):
        notes_parts.append(f"Price guide: {fields['Price Guide'].strip()}")
    if fields.get("Notes"):
        notes_parts.append(fields["Notes"].strip())
    if fields.get("Custom", "").strip().lower() == "yes":
        notes_parts.append("Custom content: Yes")
    special_notes = " | ".join(notes_parts) if notes_parts else ""

    # Languages
    languages = fields.get("Languages", "")

    # Countries
    countries = fields.get("Countries Visited", "")

    # Job
    current_job = fields.get("Current Job", "Content creator")
    prev_job = fields.get("Previous Job before OnlyFans", "")
    job = current_job
    if prev_job and prev_job.lower() not in ["none", "no", ""]:
        job = f"{current_job} (prev: {prev_job})"

    # Age
    age_str = fields.get("Age", "22")
    try:
        age = int(age_str)
    except (ValueError, TypeError):
        age = 22

    # Build voice description from Bio
    voice = _extract_voice_from_bio(bio)
    personality = _extract_personality_from_bio(bio, fields.get("Model Name", model_name))

    # Pet names and never-use words from Bio
    pet_names, never_words = _extract_voice_rules(bio)

    return {
        "name": fields.get("Model Name", model_name),
        "airtable_name": fields.get("Model Name", model_name),
        "gender": _guess_gender(fields, bio),
        "traffic": traffic_type,
        "traffic_display": traffic,
        "age": age,
        "nationality": fields.get("Nationality", "Unknown"),
        "location": fields.get("Location", "Unknown"),
        "origin": fields.get("Location", "Unknown").split(",")[0] if "," in fields.get("Location", "") else fields.get("Location", "Unknown"),
        "page_type": page_type,
        "personality": personality,
        "voice": voice,
        "voice_pet_names": pet_names,
        "voice_never": never_words,
        "interests": interests,
        "physical": physical,
        "job": job,
        "countries": countries,
        "explicit_level": explicit_level,
        "special_notes": special_notes,
        "languages": languages,
        "bio_raw": bio,
        "smoking": fields.get("Smoking", ""),
        "drinking": fields.get("Drinking", ""),
        "partner": fields.get("Partner", "None"),
        "children": fields.get("Children", "None"),
        "favorite_food": fields.get("Favorite Food", ""),
        "prev_job": prev_job,
        "restrictions": restrictions,
    }


def _guess_gender(fields, bio):
    """Guess gender from available data."""
    bio_lower = bio.lower()
    # Check for clear female indicators
    female_indicators = ["she is", "she's", "her personality", "girl", "girlfriend", "good girl"]
    male_indicators = ["he is", "he's", "his personality", "boy", "boyfriend", "guy"]
    
    f_score = sum(1 for i in female_indicators if i in bio_lower)
    m_score = sum(1 for i in male_indicators if i in bio_lower)
    
    if f_score > m_score:
        return "female"
    elif m_score > f_score:
        return "male"
    return "female"  # default


def _extract_personality_from_bio(bio, name):
    """Extract personality summary from Bio field."""
    if not bio:
        return f"{name} — personality TBD"
    
    # Try to find PERSONALITY section
    lines = bio.split("\n")
    personality_lines = []
    in_personality = False
    
    for line in lines:
        line_stripped = line.strip()
        if "PERSONALITY" in line_stripped.upper() or "personality" in line_stripped.lower():
            in_personality = True
            continue
        if in_personality:
            if line_stripped and not any(line_stripped.upper().startswith(s) for s in ["LIKES", "HOOK", "DISLIKES", "BOUNDARIES", "🔥", "🚫", "⚠️"]):
                personality_lines.append(line_stripped)
            else:
                if personality_lines:
                    break
    
    if personality_lines:
        return " ".join(personality_lines)
    
    # Fallback: use first meaningful paragraph
    for line in lines:
        line_stripped = line.strip()
        if len(line_stripped) > 30 and not line_stripped.startswith(("💖", "🔥", "🚫", "⚠️", "LIKES", "HOOK")):
            return line_stripped[:300]
    
    return bio[:300] if bio else f"{name} — personality TBD"


def _extract_voice_from_bio(bio):
    """Extract voice/texting style from Bio."""
    if not bio:
        return "Casual texting style. Playful and flirty."
    
    bio_lower = bio.lower()
    voice_parts = []
    
    # Check for specific style indicators
    if "emoji" in bio_lower or "emoticon" in bio_lower or "uwu" in bio_lower:
        voice_parts.append("Uses emojis/emoticons")
    if "shy" in bio_lower:
        voice_parts.append("Shy at first, opens up gradually")
    if "playful" in bio_lower:
        voice_parts.append("Playful")
    if "bratty" in bio_lower or "brat" in bio_lower:
        voice_parts.append("Bratty undertone")
    if "sweet" in bio_lower:
        voice_parts.append("Sweet")
    if "flirt" in bio_lower:
        voice_parts.append("Flirty")
    if "curious" in bio_lower:
        voice_parts.append("Curious")
    if "teasing" in bio_lower or "tease" in bio_lower:
        voice_parts.append("Teasing")
    if "dominant" in bio_lower or "takes control" in bio_lower:
        voice_parts.append("Takes control gradually")
    if "submissive" in bio_lower:
        voice_parts.append("Can be submissive")
    if "elongate" in bio_lower or "hiii" in bio_lower:
        voice_parts.append("Elongated words (hiiii, nooo)")
    if "lowercase" in bio_lower or "e-girl" in bio_lower:
        voice_parts.append("Lowercase casual texting")
    
    if voice_parts:
        return ". ".join(voice_parts) + ". Casual texting style."
    
    return "Casual texting style. Playful and flirty."


def _extract_voice_rules(bio):
    """Extract pet names and never-use words from Bio."""
    bio_lower = bio.lower()
    
    pet_names = "babe, baby"
    if "ella" in bio_lower:
        pet_names = "babe, cutie, love"
    if "nickname" in bio_lower:
        pet_names = "babe, cutie"
    
    never_words = ""
    if "do not" in bio_lower or "avoid" in bio_lower or "don't" in bio_lower:
        never_words = ""  # Would need more specific parsing
    
    return pet_names, never_words


# ── CLI Commands ──────────────────────────────────────────────

def cmd_models(args):
    """List all models."""
    records = fetch_all_records(fields=["Model Name", "Status", "Traffic", "Page Type", "Age"])
    models = []
    for r in records:
        f = r.get("fields", {})
        name = f.get("Model Name", "?")
        status = f.get("Status", "?")
        traffic = f.get("Traffic", [])
        traffic_str = ", ".join(traffic) if isinstance(traffic, list) else str(traffic)
        age = f.get("Age", "?")
        page = f.get("Page Type", "?")
        models.append((name, status, traffic_str, page, age))
    
    models.sort(key=lambda x: x[0])
    print(f"{'Model Name':<25} {'Status':<10} {'Traffic':<20} {'Page':<12} {'Age'}")
    print("-" * 80)
    for name, status, traffic, page, age in models:
        print(f"{name:<25} {status:<10} {traffic:<20} {page:<12} {age}")
    print(f"\nTotal: {len(models)} models")


def cmd_model(args):
    """Get full model info."""
    info = get_model_info(args.name)
    if not info:
        print(f"Model '{args.name}' not found in Airtable")
        return
    
    print(f"\n{'='*60}")
    print(f"MODEL: {info['name']}")
    print(f"{'='*60}")
    for key, val in info.items():
        if key == "bio_raw":
            print(f"  {key}: ({len(val)} chars)")
        elif isinstance(val, list):
            print(f"  {key}: {', '.join(str(v) for v in val)}")
        else:
            val_str = str(val)[:80]
            print(f"  {key}: {val_str}")


def cmd_fields(args):
    """List all field names in the table."""
    records = fetch_all_records()
    if not records:
        print("No records found")
        return
    
    all_fields = set()
    for r in records:
        all_fields.update(r.get("fields", {}).keys())
    
    print(f"Fields in Model Info table ({len(all_fields)}):\n")
    for f in sorted(all_fields):
        print(f"  - {f}")


def main():
    parser = argparse.ArgumentParser(description="Airtable CLI — Model Info")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("models", help="List all models")
    sub.add_parser("fields", help="List all field names")

    p = sub.add_parser("model", help="Get full model info")
    p.add_argument("name", help="Model name (exact match)")

    args = parser.parse_args()

    cmds = {
        "models": cmd_models,
        "model": cmd_model,
        "fields": cmd_fields,
    }

    if args.command in cmds:
        cmds[args.command](args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
