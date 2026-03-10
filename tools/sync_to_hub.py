"""Sync a model's scripts from CW-ScriptManager config to Hub Supabase."""
import sys, os, json, requests
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

SUPABASE_URL = os.environ.get("HUB_SUPABASE_URL", "https://bnmrdlqqzxenyqjknqhy.supabase.co")
SUPABASE_SERVICE_KEY = os.environ.get("HUB_SUPABASE_SERVICE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJubXJkbHFxenhlbnlxamtucWh5Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3MTA4MjE3MywiZXhwIjoyMDg2NjU4MTczfQ.b4-PTuRmk9S0WCrqbsBYACpJgXrTMregG3hNook-1aI")

HEADERS = {
    "apikey": SUPABASE_SERVICE_KEY,
    "Authorization": f"Bearer {SUPABASE_SERVICE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation",
}


def find_model_id(name):
    r = requests.get(
        f"{SUPABASE_URL}/rest/v1/models",
        headers={**HEADERS, "Prefer": ""},
        params={"name": f"ilike.%{name}%", "select": "id,name"},
    )
    r.raise_for_status()
    rows = r.json()
    if rows:
        return rows[0]["id"], rows[0]["name"]
    return None, None


def config_to_hub_json(cfg):
    """Convert CW-ScriptManager config dict to Hub ScriptContent JSON."""
    journey = []
    for step in cfg.get("journey", []):
        journey.append({
            "id": step[0],
            "message": step[1],
            "instruction": step[2],
            "phase": step[3],
        })

    nr_waves = []
    for step in cfg.get("nr_waves", []):
        nr_waves.append({
            "id": step[0],
            "message": step[1],
            "instruction": step[2],
            "phase": step[3] if len(step) > 3 else "sext",
        })

    re_engagement = []
    for step in cfg.get("re_engagement", []):
        re_engagement.append({
            "id": step[0],
            "message": step[1],
            "instruction": step[2],
            "phase": step[3] if len(step) > 3 else "sext",
        })

    personal_info = []
    for item in cfg.get("personal_info", []):
        personal_info.append({
            "topic": item[0],
            "response": item[1],
            "note": item[2],
        })

    positive_spin = []
    for item in cfg.get("positive_spin", []):
        positive_spin.append({
            "topic": item[0],
            "response": item[1],
            "note": item[2] if len(item) > 2 else None,
        })

    content = {
        "age": cfg.get("age"),
        "job": cfg.get("job"),
        "gender": cfg.get("gender"),
        "origin": cfg.get("origin"),
        "location": cfg.get("location"),
        "nationality": cfg.get("nationality"),
        "personality": cfg.get("personality"),
        "voice": cfg.get("voice"),
        "voice_pet_names": cfg.get("voice_pet_names"),
        "voice_never": cfg.get("voice_never"),
        "interests": cfg.get("interests", []),
        "physical": cfg.get("physical"),
        "special_notes": cfg.get("special_notes"),
        "explicit_level": cfg.get("explicit_level"),
        "journey": journey,
        "nr_waves": nr_waves,
        "personal_info": personal_info,
        "positive_spin": positive_spin,
        "re_engagement": re_engagement,
        "obj_scripts": cfg.get("obj_scripts", {}),
    }

    # Include meetup_redirect and location_handling for dating app models
    if cfg.get("meetup_redirect"):
        mr = []
        for step in cfg["meetup_redirect"]:
            mr.append({
                "id": step[0],
                "message": step[1],
                "instruction": step[2],
                "phase": step[3] if len(step) > 3 else "teasing",
            })
        content["meetup_redirect"] = mr

    if cfg.get("location_handling"):
        lh = []
        for item in cfg["location_handling"]:
            lh.append({
                "topic": item[0],
                "response": item[1],
                "note": item[2] if len(item) > 2 else None,
            })
        content["location_handling"] = lh

    return content


def sync_model(module_name):
    """Load a model config by module name and sync to Supabase."""
    mod = __import__(f"models.{module_name}", fromlist=["config"])
    cfg = mod.config

    model_name = cfg["name"]
    slug = cfg["folder"]

    print(f"Syncing {model_name} (slug: {slug})...")

    model_id, db_name = find_model_id(model_name)
    if not model_id:
        print(f"[ERROR] Model '{model_name}' not found in Supabase models table")
        return False

    print(f"  Found in DB: {db_name} (id: {model_id})")

    content = config_to_hub_json(cfg)

    # Check if already exists
    r = requests.get(
        f"{SUPABASE_URL}/rest/v1/model_scripts",
        headers={**HEADERS, "Prefer": ""},
        params={"model_id": f"eq.{model_id}", "select": "id"},
    )
    r.raise_for_status()
    existing = r.json()

    if existing:
        row_id = existing[0]["id"]
        print(f"  Updating existing row {row_id}...")
        r = requests.patch(
            f"{SUPABASE_URL}/rest/v1/model_scripts?id=eq.{row_id}",
            headers=HEADERS,
            json={"content": content, "slug": slug, "updated_at": "now()"},
        )
    else:
        print(f"  Inserting new row...")
        r = requests.post(
            f"{SUPABASE_URL}/rest/v1/model_scripts",
            headers=HEADERS,
            json={"model_id": model_id, "slug": slug, "content": content},
        )

    if r.status_code in (200, 201):
        print(f"  [OK] Synced to Hub!")
        return True
    else:
        print(f"  [ERROR] HTTP {r.status_code}: {r.text}")
        return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python _sync_to_hub.py <module_name>")
        print("Example: python _sync_to_hub.py justindaniels")
        sys.exit(1)
    sync_model(sys.argv[1])
