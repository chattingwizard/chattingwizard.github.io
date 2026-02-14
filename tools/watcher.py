"""
WATCHER — Automated Monday.com polling daemon.
================================================================
Runs periodically (via Task Scheduler) and handles:

1. NEW ONBOARDINGS: Detects new models in Monday → generates scripts
2. TASK COMPLETION: Watches tracked tasks → executes follow-up actions

State is persisted in watcher_state.json to avoid re-processing.
All actions are logged to watcher.log.

Usage:
    python tools/watcher.py              # Run one check cycle
    python tools/watcher.py --loop 300   # Run continuously every 300s (5 min)
"""

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS_DIR = os.path.join(BASE_DIR, "tools")
sys.path.insert(0, TOOLS_DIR)

# Load .env
ENV_FILE = os.path.join(BASE_DIR, ".env")
if os.path.exists(ENV_FILE):
    with open(ENV_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, val = line.split("=", 1)
                os.environ.setdefault(key.strip(), val.strip())

STATE_FILE = os.path.join(TOOLS_DIR, "watcher_state.json")
LOG_FILE = os.path.join(BASE_DIR, "watcher.log")

# Task IDs to watch (task_id → action config)
WATCHED_TASKS = {
    "2721603979": {
        "name": "List content sets per model",
        "action": "process_sexting_sets",
        "board_id": "5089773142",
    },
}


# ══════════════════════════════════════════
# LOGGING
# ══════════════════════════════════════════

def log(msg, level="INFO"):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] [{level}] {msg}"
    print(line)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception:
        pass


# ══════════════════════════════════════════
# STATE MANAGEMENT
# ══════════════════════════════════════════

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "processed_onboardings": [],
        "processed_tasks": {},
        "last_check": None,
    }


def save_state(state):
    state["last_check"] = datetime.now().isoformat()
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)


# ══════════════════════════════════════════
# MONDAY API HELPERS
# ══════════════════════════════════════════

def monday_query(q, variables=None):
    """Execute Monday.com GraphQL query."""
    import requests
    token = os.environ.get("MONDAY_API_TOKEN")
    if not token:
        log("MONDAY_API_TOKEN not set", "ERROR")
        return {}
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "API-Version": "2024-10",
    }
    payload = {"query": q}
    if variables:
        payload["variables"] = variables
    resp = requests.post("https://api.monday.com/v2", json=payload, headers=headers)
    resp.raise_for_status()
    data = resp.json()
    if "errors" in data:
        for e in data["errors"]:
            log(f"Monday API error: {e.get('message', e)}", "ERROR")
        return {}
    return data.get("data", {})


def get_item_with_updates(item_id):
    """Get a Monday item with its column values and comments."""
    data = monday_query("""
    query ($itemId: [ID!]!) {
        items(ids: $itemId) {
            id
            name
            column_values {
                id
                text
                value
                type
            }
            updates(limit: 20) {
                id
                text_body
                created_at
                creator {
                    name
                    id
                }
            }
        }
    }
    """, {"itemId": [str(item_id)]})
    items = data.get("items", [])
    return items[0] if items else None


# ══════════════════════════════════════════
# SLACK NOTIFICATION
# ══════════════════════════════════════════

def send_slack(channel, message):
    """Send Slack message."""
    try:
        from slack_sdk import WebClient
        token = os.environ.get("SLACK_USER_TOKEN")
        if not token:
            log("SLACK_USER_TOKEN not set, skipping notification", "WARN")
            return
        client = WebClient(token=token)
        # Resolve channel name
        if not channel.startswith("C"):
            name = channel.lstrip("#")
            result = client.conversations_list(types="public_channel", limit=500, exclude_archived=True)
            for ch in result["channels"]:
                if ch["name"] == name:
                    channel = ch["id"]
                    break
        client.chat_postMessage(channel=channel, text=message)
        log(f"Slack notification sent to {channel}")
    except Exception as e:
        log(f"Slack notification failed: {e}", "ERROR")


# ══════════════════════════════════════════
# ACTION: PROCESS NEW ONBOARDINGS
# ══════════════════════════════════════════

def check_new_onboardings(state):
    """Check Monday for new onboardings and run pipeline."""
    from onboard_model import cmd_check_monday, cmd_onboard
    
    class FakeArgs:
        pass
    
    try:
        onboardings = cmd_check_monday(FakeArgs())
    except Exception as e:
        log(f"Error checking Monday onboardings: {e}", "ERROR")
        return
    
    if not onboardings:
        log("No new onboardings")
        return
    
    for ob in onboardings:
        monday_id = ob["monday_id"]
        creator = ob["creator"]
        
        if monday_id in state["processed_onboardings"]:
            log(f"Skipping already processed: {creator} ({monday_id})")
            continue
        
        log(f"NEW ONBOARDING DETECTED: {creator} (client: {ob['client']})")
        
        try:
            # Run onboarding pipeline
            args = FakeArgs()
            args.name = creator
            cmd_onboard(args)
            
            state["processed_onboardings"].append(monday_id)
            save_state(state)
            
            log(f"Onboarding complete for {creator}")
            send_slack("0-management-scripts",
                       f"[AUTO] New model scripts generated for {creator}. "
                       f"@Rei please import into Infloww and assign content.")
        except Exception as e:
            log(f"Error onboarding {creator}: {e}", "ERROR")


# ══════════════════════════════════════════
# ACTION: PROCESS COMPLETED TASKS
# ══════════════════════════════════════════

def parse_sexting_sets(text):
    """Parse content set counts from Rei's comment.
    
    Expected format (flexible):
        Antonella: 4
        Ashley: 6
        Chayla: 3
    Or: Antonella 4, Ashley 6, Chayla 3
    """
    sets = {}
    # Try "Model: N" or "Model - N" or "Model N" patterns
    patterns = [
        r'([A-Za-z][A-Za-z\s]+?)\s*[:=-]\s*(\d+)',  # "Antonella: 4" or "Antonella - 4"
        r'([A-Za-z][A-Za-z\s]+?)\s+(\d+)',            # "Antonella 4"
    ]
    for pattern in patterns:
        matches = re.findall(pattern, text)
        for name, count in matches:
            name = name.strip()
            if len(name) > 2 and int(count) > 0:
                sets[name.lower()] = int(count)
        if sets:
            break
    return sets


def process_sexting_sets(item):
    """Process Rei's response with content set counts."""
    # Get all updates/comments
    updates = item.get("updates", [])
    if not updates:
        log("Task done but no comments found — waiting for Rei to add the data")
        return False
    
    # Look for the most recent update with set data
    all_text = ""
    for u in updates:
        body = u.get("text_body", "")
        if body:
            all_text += body + "\n"
    
    sets = parse_sexting_sets(all_text)
    if not sets:
        log(f"Could not parse content set counts from updates. Raw text: {all_text[:200]}")
        return False
    
    log(f"Parsed {len(sets)} model set counts from Rei's comment")
    
    # Update model configs and regenerate those that need more than 4 sequences
    import glob
    import importlib
    
    models_dir = os.path.join(TOOLS_DIR, "models")
    updated = []
    
    for model_file in sorted(glob.glob(os.path.join(models_dir, "*.py"))):
        basename = os.path.basename(model_file).replace(".py", "")
        if basename.startswith("__") or basename == "test_write":
            continue
        
        # Load config to get model name
        try:
            spec = importlib.util.spec_from_file_location(basename, model_file)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            config = getattr(mod, "config", getattr(mod, "CONFIG", None))
            if not config:
                continue
        except Exception:
            continue
        
        model_name = config.get("name", "").lower()
        airtable_name = config.get("airtable_name", "").lower()
        
        # Match against Rei's data
        matched_count = None
        for rei_name, count in sets.items():
            if (rei_name in model_name or model_name in rei_name or
                rei_name in airtable_name or airtable_name in rei_name):
                matched_count = count
                break
        
        if matched_count and matched_count > 4:
            # Update the config file to set sexting_sets
            try:
                with open(model_file, "r", encoding="utf-8") as f:
                    content = f.read()
                
                if '"sexting_sets"' not in content and "'sexting_sets'" not in content:
                    # Add sexting_sets to the config dict
                    content = content.replace(
                        '"explicit_level"',
                        f'"sexting_sets": {matched_count},\n    "explicit_level"'
                    )
                    with open(model_file, "w", encoding="utf-8") as f:
                        f.write(content)
                    updated.append((config["name"], matched_count))
                    log(f"  {config['name']}: set sexting_sets={matched_count}")
            except Exception as e:
                log(f"  Error updating {config['name']}: {e}", "ERROR")
    
    if updated:
        # Regenerate affected models
        log(f"Regenerating {len(updated)} models with extra sexting sequences...")
        
        from model_factory import ModelFactory
        for model_name, count in updated:
            try:
                # Reload the updated config
                folder = None
                for model_file in glob.glob(os.path.join(models_dir, "*.py")):
                    bn = os.path.basename(model_file).replace(".py", "")
                    spec = importlib.util.spec_from_file_location(bn, model_file)
                    mod = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(mod)
                    c = getattr(mod, "config", getattr(mod, "CONFIG", None))
                    if c and c.get("name") == model_name:
                        folder = c.get("folder")
                        factory = ModelFactory(c)
                        factory.generate_all()
                        break
                log(f"  Regenerated {model_name}")
            except Exception as e:
                log(f"  Error regenerating {model_name}: {e}", "ERROR")
        
        # Update dashboard
        try:
            from onboard_model import update_dashboard
            update_dashboard()
        except Exception as e:
            log(f"Error updating dashboard: {e}", "ERROR")
        
        # Git commit + push
        try:
            import subprocess
            subprocess.run(["git", "add", "-A"], cwd=BASE_DIR, check=True)
            subprocess.run(["git", "commit", "-m",
                           f"auto: update sexting sets for {len(updated)} models"],
                          cwd=BASE_DIR, check=True)
            subprocess.run(["git", "push"], cwd=BASE_DIR, check=True)
            log("Changes committed and pushed")
        except Exception as e:
            log(f"Git error: {e}", "ERROR")
        
        # Notify
        names = ", ".join(f"{n} ({c} sets)" for n, c in updated)
        send_slack("0-management-scripts",
                   f"[AUTO] Extra sexting scripts generated for: {names}. "
                   f"@Rei please import the new sheets into Infloww.")
    else:
        log("No models need more than 4 sexting sequences")
    
    return True


def check_watched_tasks(state):
    """Check if any watched tasks changed to Done."""
    for task_id, task_config in WATCHED_TASKS.items():
        if state["processed_tasks"].get(task_id) == "done":
            continue  # Already processed
        
        log(f"Checking task: {task_config['name']} ({task_id})")
        
        item = get_item_with_updates(task_id)
        if not item:
            log(f"Could not fetch task {task_id}", "WARN")
            continue
        
        # Check status
        status = ""
        for cv in item.get("column_values", []):
            if cv["id"] == "status":
                status = (cv.get("text", "") or "").lower()
                break
        
        if "done" not in status:
            log(f"  Status: '{status}' (not done yet)")
            continue
        
        log(f"  TASK COMPLETED: {task_config['name']}")
        
        # Execute the action
        action = task_config["action"]
        success = False
        
        if action == "process_sexting_sets":
            success = process_sexting_sets(item)
        
        if success:
            state["processed_tasks"][task_id] = "done"
            save_state(state)
            log(f"  Action '{action}' completed successfully")
        else:
            log(f"  Action '{action}' needs more data — will retry next cycle")


# ══════════════════════════════════════════
# MAIN RUN CYCLE
# ══════════════════════════════════════════

def run_cycle():
    """Execute one complete check cycle."""
    log("=" * 50)
    log("WATCHER CYCLE START")
    
    state = load_state()
    
    # 1. Check for new onboardings
    log("--- Checking onboardings ---")
    try:
        check_new_onboardings(state)
    except Exception as e:
        log(f"Onboarding check error: {e}", "ERROR")
    
    # 2. Check watched tasks
    log("--- Checking watched tasks ---")
    try:
        check_watched_tasks(state)
    except Exception as e:
        log(f"Task check error: {e}", "ERROR")
    
    save_state(state)
    log("WATCHER CYCLE END")
    log("")


def main():
    parser = argparse.ArgumentParser(description="Monday.com Watcher Daemon")
    parser.add_argument("--loop", type=int, default=0,
                       help="Run continuously with N seconds between cycles (0=run once)")
    args = parser.parse_args()
    
    log(f"Watcher started (loop={args.loop}s)")
    
    if args.loop > 0:
        log(f"Running every {args.loop} seconds. Press Ctrl+C to stop.")
        while True:
            try:
                run_cycle()
                time.sleep(args.loop)
            except KeyboardInterrupt:
                log("Watcher stopped by user")
                break
            except Exception as e:
                log(f"Cycle error: {e}", "ERROR")
                time.sleep(args.loop)
    else:
        run_cycle()


if __name__ == "__main__":
    main()
