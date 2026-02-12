"""
ONBOARDING AUTOMATION — New Model Pipeline
=============================================
Detects new onboardings from Monday.com, reads model info from Airtable,
creates scripts, generates XLSX/HTML, updates dashboard, notifies Rei.

Usage:
    # Check Monday.com + Slack for new onboardings
    python tools/onboard_model.py check

    # Full pipeline: Airtable → config → generate → deploy → notify Rei
    python tools/onboard_model.py onboard --name "Claudia"

    # Manual config creation (fallback, no Airtable)
    python tools/onboard_model.py create --name "Luna" --gender female --traffic reddit ...

    # Generate outputs for an existing model config
    python tools/onboard_model.py generate <model_folder>

Flow:
    1. Angeles creates onboarding in Monday → detected by `check`
    2. Script Manager reads Creator name → fetches full info from Airtable
    3. Creates personalized config + scripts based on model data
    4. Generates XLSX (Infloww), HTML guides, objections page
    5. Updates dashboard, notifies Rei on Slack
"""

import argparse
import os
import sys
import re
import json
from datetime import datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, "tools", "models")
SLACK_CHANNEL = "0-management-scripts"
ONBOARDING_KEYWORDS = [
    "onboarding", "new model", "new creator", "new account",
    "nueva creadora", "nuevo modelo", "nuevo onboarding",
    "start preparing", "prepare scripts", "preparing scripts",
    "isn't linked", "isn\u2019t linked", "not linked yet",
    "starting the chat", "new onboarding",
    # Structured trigger (recommended format for Angeles)
    "NEWMODEL:",
]


# ═══════════════════════════════════════════════════════════════
# SLACK INTEGRATION
# ═══════════════════════════════════════════════════════════════

def get_slack_client():
    """Import and return Slack CLI module functions."""
    try:
        from slack_cli import get_client, resolve_channel, resolve_user_name, resolve_user_id
        return get_client(), resolve_channel, resolve_user_name, resolve_user_id
    except ImportError:
        print("[ERROR] slack_cli.py not found or slack_sdk not installed")
        sys.exit(1)


def check_slack_onboarding(days_back=7, verbose=True):
    """Scan Slack #management-scripts for recent onboarding requests."""
    client, resolve_channel, resolve_user_name, _ = get_slack_client()
    channel_id = resolve_channel(client, SLACK_CHANNEL)

    # Get recent messages
    from slack_sdk.errors import SlackApiError
    try:
        result = client.conversations_history(channel=channel_id, limit=50)
    except SlackApiError as e:
        print(f"[ERROR] Slack: {e.response['error']}")
        return []

    cutoff = datetime.now() - timedelta(days=days_back)
    onboarding_msgs = []

    for msg in result.get("messages", []):
        ts = float(msg.get("ts", 0))
        msg_time = datetime.fromtimestamp(ts)
        if msg_time < cutoff:
            continue

        text = (msg.get("text") or "").lower()
        if any(kw in text for kw in ONBOARDING_KEYWORDS):
            user_id = msg.get("user", "unknown")
            user_name = resolve_user_name(client, user_id)
            onboarding_msgs.append({
                "time": msg_time.strftime("%Y-%m-%d %H:%M"),
                "user": user_name,
                "text": msg.get("text", ""),
                "ts": msg.get("ts"),
            })

    if verbose:
        if onboarding_msgs:
            print(f"\n[ONBOARDING] Found {len(onboarding_msgs)} potential onboarding(s) in #{SLACK_CHANNEL}:\n")
            for m in onboarding_msgs:
                print(f"  [{m['time']}] {m['user']}:")
                print(f"  {m['text'][:200]}")
                print()
        else:
            print(f"[OK] No new onboarding requests found in #{SLACK_CHANNEL} (last {days_back} days)")

    return onboarding_msgs


def notify_slack(model_name, channel=SLACK_CHANNEL, notify_rei=True):
    """Notify team on Slack that scripts are ready."""
    client, resolve_channel_fn, _, resolve_user_id = get_slack_client()
    from slack_sdk.errors import SlackApiError

    folder = model_name.lower().replace(" ", "")
    url = f"https://chattingwizard.github.io/{folder}/"

    msg = (
        f"Scripts ready for {model_name}! "
        f"All XLSX and HTML guides have been generated and deployed.\n\n"
        f"Dashboard: https://chattingwizard.github.io/\n"
        f"Model page: {url}\n"
        f"XLSX: {url}{model_name}_Complete_Infloww.xlsx\n\n"
        f"Rei — please import the XLSX into Infloww and assign content to each PPV."
    )

    # Send to channel
    try:
        channel_id = resolve_channel_fn(client, channel)
        client.chat_postMessage(channel=channel_id, text=msg)
        print(f"[SLACK] Notification sent to #{channel}")
    except SlackApiError as e:
        print(f"[WARN] Could not send to #{channel}: {e.response['error']}")

    # Also DM Rei
    if notify_rei:
        try:
            from slack_cli import cmd_send_dm
            rei_id = resolve_user_id(client, "Rei")
            from slack_sdk.errors import SlackApiError as SAE
            try:
                result = client.conversations_open(users=[rei_id])
                dm_channel = result["channel"]["id"]
                client.chat_postMessage(channel=dm_channel, text=msg)
                print("[SLACK] DM sent to Rei")
            except SAE as e:
                print(f"[WARN] Could not DM Rei: {e.response['error']}")
        except Exception:
            print("[WARN] Could not resolve Rei for DM")


# ═══════════════════════════════════════════════════════════════
# MODEL CONFIG CREATION
# ═══════════════════════════════════════════════════════════════

def sanitize_folder(name):
    """Create a clean folder name from model name."""
    return re.sub(r'[^a-z0-9]', '', name.lower())


def create_model_config(info):
    """
    Create a model config .py file from structured info.

    info dict keys:
        name, gender, traffic, age, nationality, location, origin,
        page_type, personality, voice, voice_pet_names, voice_never,
        interests, physical, job, countries, explicit_level, special_notes
    """
    name = info["name"]
    folder = sanitize_folder(name)
    gender = info.get("gender", "female")
    traffic = info.get("traffic", "social_media")
    age = info.get("age", 22)
    nationality = info.get("nationality", "American")
    location = info.get("location", "Unknown")
    origin = info.get("origin", location.split(",")[0] if "," in location else location)
    page_type = info.get("page_type", "Mixed")
    personality = info.get("personality", f"{name} personality TBD")
    voice = info.get("voice", f"Casual texting style. Emojis sometimes. Playful and flirty.")
    voice_pet_names = info.get("voice_pet_names", "babe, baby")
    voice_never = info.get("voice_never", "")
    interests = info.get("interests", [])
    physical = info.get("physical", "TBD")
    job = info.get("job", "OnlyFans model")
    countries = info.get("countries", "")
    explicit = info.get("explicit_level", "full_solo" if gender == "female" else "full_male")
    special_notes = info.get("special_notes", "")

    # Traffic mapping
    traffic_map = {
        "reddit": "social_media",
        "oftv": "social_media",
        "tiktok": "social_media",
        "instagram": "social_media",
        "twitter": "social_media",
        "dating_app": "dating_app",
        "datingapp": "dating_app",
        "social_media": "social_media",
    }
    traffic_type = traffic_map.get(traffic.lower().replace(" ", "_"), "social_media")
    is_dating = traffic_type == "dating_app"

    # Determine pronoun set
    if gender == "female":
        sub_word = "guys"
        pet_default = "babe, cutie"
    else:
        sub_word = "girls" if "gay" not in traffic.lower() else "guys"
        pet_default = "babe, baby"

    if not voice_pet_names:
        voice_pet_names = pet_default

    interests_str = json.dumps(interests) if interests else '["TBD"]'

    # ── Build journey template ──
    if is_dating:
        journey = _build_dating_journey(name, gender, personality)
    else:
        journey = _build_social_journey(name, gender, personality)

    nr_waves = _build_nr_waves(gender)
    personal_info = _build_personal_info(name, age, location, nationality, job, interests, physical, special_notes)
    positive_spin = _build_positive_spin(name, gender, interests)
    re_engagement = _build_re_engagement(gender)

    # ── Write config file ──
    filepath = os.path.join(MODELS_DIR, f"{folder}.py")

    traffic_display = traffic.replace("_", " ").title()
    header = f'"""\n{name.upper()} — {traffic_display} {"Female" if gender == "female" else "Male"} Creator\n'
    header += f'{age}, {nationality} ({location})\n'
    header += f'Traffic: {traffic_display}. Page: {page_type}.\n'
    header += f'Voice: {voice[:80]}...\n"""\n'

    config_str = f'''{header}import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {{
    "name": {json.dumps(name)},
    "airtable_name": {json.dumps(name)},
    "folder": {json.dumps(folder)},
    "gender": {json.dumps(gender)},
    "traffic": {json.dumps(traffic_type)},
    "age": {age},
    "nationality": {json.dumps(nationality)},
    "location": {json.dumps(location)},
    "origin": {json.dumps(origin)},
    "page_type": {json.dumps(page_type)},
    "personality": {json.dumps(personality)},
    "voice": {json.dumps(voice)},
    "voice_pet_names": {json.dumps(voice_pet_names)},
    "voice_never": {json.dumps(voice_never)},
    "interests": {interests_str},
    "physical": {json.dumps(physical)},
    "job": {json.dumps(job)},
    "countries": {json.dumps(countries)},
    "explicit_level": {json.dumps(explicit)},
    "special_notes": {json.dumps(special_notes)},

    # ═══════════════════════════════════════
    # JOURNEY ({len(journey)} messages)
    # ═══════════════════════════════════════
    "journey": {_format_tuples_4(journey)},

{_dating_extras(is_dating, name, gender) if is_dating else ""}    # NR Waves
    "nr_waves": {_format_tuples_4(nr_waves)},

    # Personal Info
    "personal_info": {_format_tuples_3(personal_info)},

    # Positive Spin
    "positive_spin": {_format_tuples_3(positive_spin)},

    # Re-Engagement
    "re_engagement": {_format_tuples_4(re_engagement)},

    # OBJ scripts — empty = use gender defaults from obj_defaults.py
    "obj_scripts": {{}},
}}

if __name__ == "__main__":
    m = ModelFactory(config)
    m.generate_all()
'''

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(config_str)

    print(f"[CONFIG] Created: {filepath}")
    print(f"  Name: {name}")
    print(f"  Gender: {gender}")
    print(f"  Traffic: {traffic_type}")
    print(f"  Journey: {len(journey)} messages")
    print(f"  Explicit: {explicit}")

    return filepath, folder


# ═══════════════════════════════════════════════════════════════
# JOURNEY BUILDERS
# ═══════════════════════════════════════════════════════════════

def _build_social_journey(name, gender, personality):
    """Build a social media journey (Reddit/OFTV/TikTok/etc)."""
    # Pronoun setup
    if gender == "female":
        wet = "wet"
        body_react = "my nipples are hard"
        physical_state = "lying in bed in just a t-shirt"
        cum_word = "cum"
        self_touch = "my fingers are starting to wander"
    else:
        wet = "hard"
        body_react = "I can feel it growing"
        physical_state = "just got out of the shower, lying on my bed"
        cum_word = "cum"
        self_touch = "my hand is starting to wander"

    journey = [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", f"heyy, glad you're here, what made you come say hi?", "Add his/her name if known. React naturally.", "rapport"),
        ("R-2", "that's sweet, so where are you from?", "React to what they say. Short react like 'aw nice' or 'omg really?'", "rapport"),
        ("R-3", f"nice, I'm from [LOCATION] but honestly I [HOBBY/ACTIVITY] most of the time haha", "PERSONALIZE with model's actual location and hobby from personality.", "rapport"),
        ("R-4", f"so what do you do when you're not distracting cute {'girls' if gender == 'male' else 'guys'} on the internet?", None, "rapport"),
        ("R-5", f"honestly you're so easy to talk to, most {'girls' if gender == 'male' else 'guys'} on here are boring but you're actually fun", "Ego boost. Next → TB-1.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5) ──
        ("TB-1", f"okay so I just [ACTIVITY] and now I'm {physical_state} and this convo is doing things to me", "THE PIVOT. PERSONALIZE activity from personality. Physical state.", "teasing"),
        ("TB-2", "like idk what it is about you but I can't stop smiling rn", "Wait for reply.", "teasing"),
        ("TB-3", "stoppp you're making me blush and nobody makes me blush", "If sexual reply: add 'especially after what you just said omg'", "teasing"),
        ("TB-4", "hold on let me show you something", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "be honest... what do you think?", "SEND PPV 0 — FREE teaser. Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ──
        ("S1-1", f"mmm you liked that? I'm already getting {wet} because of you", "Wait for reply.", "sext"),
        ("S1-2", f"my skin is tingling everywhere right now, {body_react}... you're doing something to me", "React to what they say.", "sext"),
        ("S1-3", f"I'm lying here and {self_touch}... I blame you for this", None, "sext"),
        ("S1-4", "one sec", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "I want to show you what you made me feel", "SEND PPV 1 — $12. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ──
        ("S1-6", "wow... okay I need a second after that", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", f"you have no idea what you're doing to me rn, I'm so {wet} it's crazy", None, "sext"),
        ("S1-8", "I just did something I've never done for anyone here before", "ONE TIME 'never done this'.", "sext"),
        ("S1-9", "hold on", "WAIT 2-3 MIN", "wait"),
        ("S1-10", "you need to see this, like right now", "SEND PPV 2 — $25. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ──
        ("S1-11", "fuck that was so intense", "Wait for reply.", "sext"),
        ("S1-12", f"I can't stop, you're making me {cum_word} and I need you to watch", None, "sext"),
        ("S1-13", "give me a second I need to catch my breath", "WAIT 2-3 MIN", "wait"),
        ("S1-14", "okay I did something even crazier and you're the only one seeing this", "SEND PPV 3 — $35. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ──
        ("S1-15", "oh my god I can't believe I just did that", "Wait for reply.", "sext"),
        ("S1-16", "you make me lose all control and I love it", None, "sext"),
        ("S1-17", f"I'm shaking rn, I've never been this {wet} before", None, "sext"),
        ("S1-18", "wait", "WAIT 2-3 MIN", "wait"),
        ("S1-19", "this is the craziest thing I've ever recorded, I need you to see it", "SEND PPV 4 — $50. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 5 → PPV 5 ──
        ("S1-20", "I literally can't move rn, that was everything", "Wait for reply.", "sext"),
        ("S1-21", f"one more, I need you to watch me {cum_word} for you", "Only if sub is still engaged.", "sext"),
        ("S1-22", "hold on this is it", "WAIT 2-3 MIN. SEND PPV 5 — $65 if available. Otherwise skip to AC.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "oh my god that was... wow, I've never felt like that before", "AFTERCARE. Emotional cooldown. No selling.", "aftercare"),
        ("AC-2", "you're something else, I mean it. talk soon?", "SEED next session. End convo naturally.", "aftercare"),
    ]

    return journey


def _build_dating_journey(name, gender, personality):
    """Build a dating app journey (Hinge/Tinder/Bumble)."""
    if gender == "female":
        wet = "wet"
        self_touch = "my fingers are starting to wander"
        cum_word = "cum"
    else:
        wet = "hard"
        self_touch = "my hand is starting to wander"
        cum_word = "cum"

    journey = [
        # ── Rapport ──
        ("R-1", "heyy, your profile caught my eye, had to message you", "React to their profile naturally.", "rapport"),
        ("R-2", "okay wait you're actually cute, what do you do?", "Adapt to their response. Build rapport.", "rapport"),
        ("R-3", "that's actually really cool, I'm into that", "PERSONALIZE from personality.", "rapport"),
        ("R-4", "so be honest, what are you looking for on here?", None, "rapport"),
        ("R-5", "honestly this is the best convo I've had on here in a while", "Ego boost. Next → TB-1.", "rapport"),

        # ── Teasing Bridge ──
        ("TB-1", "okay so confession, I'm lying in bed rn and this convo is making me feel some type of way", "THE PIVOT.", "teasing"),
        ("TB-2", "like you're giving me butterflies and that doesn't happen", "Wait for reply.", "teasing"),
        ("TB-3", "you know what, I want to show you something, I have a page where I post exclusive stuff", "TRANSITION to OF. Natural.", "teasing"),
        ("TB-4", "it's free to follow, no pressure, but I think you'd really like what I post there", "Send OF link. Wait for them to subscribe.", "teasing"),
        ("TB-5", "you're here! okay hold on let me send you something special for coming over", "SEND PPV 0 — FREE teaser. Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ──
        ("S1-1", f"mmm you liked that? I'm already getting {wet} because of you", "Wait for reply.", "sext"),
        ("S1-2", f"my body is reacting to everything you say and {self_touch}... this is your fault", "React to what they say.", "sext"),
        ("S1-3", "one sec", "WAIT 2-3 MIN", "wait"),
        ("S1-4", "I want to show you what you're doing to me", "SEND PPV 1 — $12. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ──
        ("S1-5", "wow... okay I need a second after that", "Wait for reply.", "sext"),
        ("S1-6", f"you have no idea how {wet} I am rn, I've never been like this with someone from a dating app", "ONE TIME 'never done this'.", "sext"),
        ("S1-7", "hold on", "WAIT 2-3 MIN", "wait"),
        ("S1-8", "you need to see this right now", "SEND PPV 2 — $25. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ──
        ("S1-9", "fuck that was intense", "Wait for reply.", "sext"),
        ("S1-10", f"I can't stop, I need you to watch me {cum_word}", None, "sext"),
        ("S1-11", "give me a second", "WAIT 2-3 MIN", "wait"),
        ("S1-12", "okay I did something even crazier, you're the only one seeing this", "SEND PPV 3 — $35. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ──
        ("S1-13", "oh my god I can't believe I just did that for someone I met on an app", "Wait for reply.", "sext"),
        ("S1-14", "you make me lose all control", None, "sext"),
        ("S1-15", "wait", "WAIT 2-3 MIN", "wait"),
        ("S1-16", "this is the craziest thing I've ever recorded, you need to see it", "SEND PPV 4 — $50. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "oh my god that was... I've never felt like that before", "AFTERCARE. No selling.", "aftercare"),
        ("AC-2", "you're something else, I mean it. we should definitely talk again", "SEED. End naturally.", "aftercare"),
    ]

    return journey


def _build_nr_waves(gender):
    """Build NR (No-Response) waves."""
    return [
        ("NR-W1", "helloooo", "Send 2-3 min after PPV. Ping.", "sext"),
        ("NR-W2", "I have something to show you but you're leaving me on read...", "Send 3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "fine I'll just keep this to myself then", "Send 5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "miss talking to you, where'd you go?", "Send 15-30 min later. Warm close.", "sext"),
        ("NR-W5", "I made something special and you're the only one I want to share it with, hmu when you're free", "Send 2-6 hrs later. New convo hook.", "sext"),
    ]


def _build_personal_info(name, age, location, nationality, job, interests, physical, special_notes):
    """Build personal info responses."""
    interest_str = ", ".join(interests[:3]) if interests else "TBD"
    info = [
        ("Age", f"I'm {age}, still figuring life out haha", None),
        ("Location", f"I'm in {location} but I don't really like sharing too many details about where exactly", "NEVER give specific neighborhood or address."),
        ("Profession", f"I do content creation full time, before this I [PREVIOUS JOB]", "PERSONALIZE previous job if known."),
        ("Hobbies", f"I'm really into {interest_str}, that's pretty much my life outside of this", "PERSONALIZE from model interests."),
        ("Countries", f"I've been to [COUNTRIES] but I want to travel more", "PERSONALIZE from model data."),
        ("Relationship", "I'm single, haven't found the right person yet", None),
        ("Food", "honestly I eat everything but [FAVORITE FOOD] is my weakness", "PERSONALIZE."),
        ("Pets", "I don't have any pets right now but I want one", "PERSONALIZE if model has pets."),
        ("Languages", "just English for now, I want to learn Spanish though", "PERSONALIZE from model languages."),
        ("Smoking", "not really my thing", "PERSONALIZE."),
    ]
    return info


def _build_positive_spin(name, gender, interests):
    """Build positive spin responses."""
    spins = [
        ("Age40Plus", "omg I actually love older guys, they know what they want and that's so attractive", None) if gender == "female" else
        ("Age40Plus", "age is just a number honestly, I've always gotten along better with mature people", None),
        
        ("Age20s", "oh nice we're close in age? that's actually rare on here", None),
        
        ("BoringJob", "honestly that sounds stable and I respect that, plus you probably have stories right?", None),
        
        ("CoolJob", "wait that's actually really cool, tell me more about that", None),
        
        ("Fit", "oh you work out? okay I see you, that's hot", None),
        
        ("NotFit", "I don't care about that stuff honestly, it's about the vibe not the body", None),
        
        ("SameCity", f"wait you're in [CITY] too?? that's crazy", "PERSONALIZE with model city."),
        
        ("FarAway", "I love that you're far away, there's something exciting about connecting with someone from a different world", None),
    ]
    return spins


def _build_re_engagement(gender):
    """Build re-engagement messages."""
    return [
        ("RE-1", "can't stop thinking about earlier, you free?", "Send 6-12 hrs after convo goes quiet.", "sext"),
        ("RE-2", "sooo I did something even crazier after we stopped talking, you have to see this", "Send next day. Seeds next session.", "sext"),
    ]


def _dating_extras(is_dating, name, gender):
    """Build meetup redirect and location handling for dating app models."""
    if not is_dating:
        return ""

    meetup = [
        ("MR-1", "haha slow down, let me show you something first", "DO NOT acknowledge 'meet'. Redirect to PPV.", "teasing"),
        ("MR-2", "trust me you're gonna want to see this before anything else", "WAIT 1-2 MIN", "wait"),
        ("MR-3", "what do you think?", "SEND PPV 0 — FREE teaser. Wait for reply.", "ppv"),
        ("MR-OBJ-1", "listen I'm not saying never, but let's get to know each other better first", "If they insist on meeting.", "teasing"),
        ("MR-OBJ-2", "I'm more of a vibe-first kind of person, and right now the vibe is really good", "Second push.", "teasing"),
        ("MR-OBJ-3", "okay how about this, let me show you something special and we'll see where things go", "Final redirect to content.", "teasing"),
    ]

    location = [
        ("LOC-1", "I'm in [AREA] but I don't like sharing too many details until I know someone better", "GENERIC area only. Never specific.", None),
        ("LOC-2", "why do you want to know? planning something?", "Playful deflection.", None),
        ("LOC-3", "let's focus on getting to know each other first, location doesn't matter when the convo is this good", "Final redirect.", None),
    ]

    return f'''    # Meetup Redirect (dating app)
    "meetup_redirect": {_format_tuples_4(meetup)},

    # Location Handling (dating app)
    "location_handling": {_format_tuples_3(location)},

'''


# ═══════════════════════════════════════════════════════════════
# FORMATTING HELPERS
# ═══════════════════════════════════════════════════════════════

def _py_val(v):
    """Format a value as Python literal (None instead of null)."""
    if v is None:
        return "None"
    return json.dumps(v)


def _format_tuples_4(items):
    """Format list of 4-element tuples for Python source."""
    if not items:
        return "[]"
    lines = ["["]
    for item in items:
        a, b, c, d = item
        lines.append(f'        ({_py_val(a)}, {_py_val(b)}, {_py_val(c)}, {_py_val(d)}),')
    lines.append("    ]")
    return "\n".join(lines)


def _format_tuples_3(items):
    """Format list of 3-element tuples for Python source."""
    if not items:
        return "[]"
    lines = ["["]
    for item in items:
        a, b, c = item[0], item[1], item[2] if len(item) > 2 else None
        lines.append(f'        ({_py_val(a)}, {_py_val(b)}, {_py_val(c)}),')
    lines.append("    ]")
    return "\n".join(lines)


# ═══════════════════════════════════════════════════════════════
# GENERATE & DEPLOY
# ═══════════════════════════════════════════════════════════════

def generate_model(folder):
    """Run ModelFactory for a model config."""
    config_path = os.path.join(MODELS_DIR, f"{folder}.py")
    if not os.path.exists(config_path):
        print(f"[ERROR] Config not found: {config_path}")
        return False

    # Import and run
    import importlib.util
    spec = importlib.util.spec_from_file_location(folder, config_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    config = getattr(mod, "CONFIG", None) or getattr(mod, "config", None)
    if not config:
        print(f"[ERROR] No CONFIG/config found in {config_path}")
        return False

    from model_factory import ModelFactory
    factory = ModelFactory(config)
    factory.generate_all()
    return True


def update_dashboard():
    """Regenerate the main dashboard."""
    dashboard_script = os.path.join(BASE_DIR, "tools", "generate_dashboard.py")
    if os.path.exists(dashboard_script):
        os.system(f'python "{dashboard_script}"')
        print("[DASHBOARD] Updated")
    else:
        print("[WARN] generate_dashboard.py not found")


# ═══════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════

def cmd_check_monday(args):
    """Check Monday.com for new onboardings."""
    try:
        from monday_cli import query as monday_query
    except ImportError:
        print("[ERROR] monday_cli.py not found")
        return []

    # Find the onboarding board
    data = monday_query("""{boards(limit: 50) {id name}}""")
    board_id = None
    for b in data.get("boards", []):
        name_lower = b["name"].lower()
        # Skip subitems boards
        if name_lower.startswith("subitems") or name_lower.startswith("subelementos"):
            continue
        if "clientonoffboarding" in name_lower.replace(" ", "").replace("\u200d", ""):
            board_id = b["id"]
            break
    
    if not board_id:
        print("[ERROR] Onboarding board not found in Monday")
        return []

    # Get items from the board
    data = monday_query("""
    query ($boardId: [ID!]!, $limit: Int!) {
        boards(ids: $boardId) {
            name
            items_page(limit: $limit) {
                items {
                    id
                    name
                    group {
                        title
                    }
                    column_values {
                        id
                        text
                        value
                        type
                    }
                }
            }
        }
    }
    """, {"boardId": [board_id], "limit": 100})

    items = data.get("boards", [{}])[0].get("items_page", {}).get("items", [])
    
    new_onboardings = []
    for item in items:
        group = item.get("group", {})
        group_title = group.get("title", "").lower()
        
        cols = {cv["id"]: cv.get("text", "") for cv in item.get("column_values", [])}
        status = cols.get("status", "").lower()
        creator = cols.get("text_mkw8gpsd", "")  # Creator column
        
        # Must have a real Creator name that differs from item name (filters out subtasks)
        if not creator or creator.strip() == item["name"].strip():
            continue
        
        # Only "Onboardings in Progress" group
        if "progress" not in group_title and "onboarding" not in group_title:
            # Also accept items without group if they have "in progress" status
            if "progress" not in status:
                continue
        
        # Not Live and not Cancelled = new onboarding
        if "live" not in status and "cancel" not in status:
            new_onboardings.append({
                "monday_id": item["id"],
                "client": item["name"],
                "creator": creator,
                "status": cols.get("status", ""),
                "start_date": cols.get("date4", ""),
                "go_live": cols.get("date_mkw899c7", ""),
                "infloww_done": cols.get("boolean_mkw8y1px", "") == "v",
            })

    if new_onboardings:
        print(f"\n[MONDAY] {len(new_onboardings)} new onboarding(s) detected:\n")
        for ob in new_onboardings:
            print(f"  Client: {ob['client']}")
            print(f"  Creator: {ob['creator']}")
            print(f"  Status: {ob['status']}")
            print(f"  Start: {ob['start_date']}")
            print(f"  Go-live: {ob['go_live']}")
            print(f"  Infloww: {'Yes' if ob['infloww_done'] else 'No'}")
            print()
    else:
        print("[OK] No new onboardings in Monday")
    
    return new_onboardings


def cmd_check(args):
    """Check Monday + Slack for new onboarding requests."""
    print("=== Checking Monday.com ===")
    monday_results = cmd_check_monday(args)
    
    print("\n=== Checking Slack ===")
    days = getattr(args, "days", 7)
    slack_results = check_slack_onboarding(days_back=days)
    
    return monday_results


def cmd_onboard(args):
    """
    Full onboarding pipeline using Airtable data.
    1. Read model info from Airtable
    2. Create model config
    3. Generate all scripts
    4. Update dashboard
    5. Notify Rei
    """
    model_name = args.name
    
    # Step 1: Fetch from Airtable
    print(f"\n[AIRTABLE] Fetching info for '{model_name}'...")
    try:
        from airtable_cli import get_model_info
    except ImportError:
        print("[ERROR] airtable_cli.py not found")
        return

    info = get_model_info(model_name)
    if not info:
        print(f"[ERROR] Model '{model_name}' not found in Airtable.")
        print("Make sure the model exists in the Model Info table with that exact name.")
        return

    print(f"  Found: {info['name']}, {info['age']}, {info['nationality']}")
    print(f"  Traffic: {info['traffic_display']} → {info['traffic']}")
    print(f"  Gender: {info['gender']}")
    print(f"  Explicit: {info['explicit_level']}")

    # Step 2: Create config
    print(f"\n[CONFIG] Creating model config...")
    filepath, folder = create_model_config(info)

    # Step 3: Generate
    print(f"\n[GENERATING] {model_name}...")
    success = generate_model(folder)

    if success:
        # Step 4: Update dashboard
        update_dashboard()

        # Step 5: Notify Rei
        if not args.no_notify:
            notify_slack(model_name)

        print(f"\n{'='*60}")
        print(f"[DONE] {model_name} fully onboarded!")
        print(f"  Config: tools/models/{folder}.py")
        print(f"  Web: {folder}/")
        print(f"  XLSX: {folder}/{model_name}_Complete_Infloww.xlsx")
        print(f"  Objections: {folder}/objections.html")
        print(f"{'='*60}")
    else:
        print(f"[ERROR] Generation failed for {model_name}")


def cmd_create(args):
    """Create a new model config (manual args, no Airtable)."""
    info = {
        "name": args.name,
        "gender": args.gender,
        "traffic": args.traffic,
        "age": args.age,
        "nationality": args.nationality,
        "location": args.location,
        "origin": args.origin or (args.location.split(",")[0] if args.location and "," in args.location else args.location),
        "page_type": args.page,
        "personality": args.personality or f"{args.name} personality — TBD, needs personalization",
        "voice": args.voice or "Casual texting style. Emojis sometimes. Playful and flirty.",
        "voice_pet_names": args.pet_names or "",
        "voice_never": args.never or "",
        "interests": args.interests.split(",") if args.interests else [],
        "physical": args.physical or "TBD",
        "job": args.job or "Content creator",
        "countries": args.countries or "",
        "explicit_level": "full_solo" if args.explicit and args.gender == "female" else
                         "full_male" if args.explicit else "non_explicit",
        "special_notes": args.notes or "",
    }

    filepath, folder = create_model_config(info)
    return filepath, folder


def cmd_generate(args):
    """Generate all outputs for a model."""
    success = generate_model(args.folder)
    if success:
        update_dashboard()
    return success


def main():
    parser = argparse.ArgumentParser(description="Onboarding Automation — New Model Pipeline")
    sub = parser.add_subparsers(dest="command")

    # Check Monday + Slack
    p = sub.add_parser("check", help="Check Monday + Slack for new onboardings")
    p.add_argument("--days", type=int, default=7, help="Days to look back in Slack")

    # Onboard from Airtable (recommended)
    p = sub.add_parser("onboard", help="Full pipeline: Airtable → config → generate → deploy → notify")
    p.add_argument("--name", required=True, help="Model name (must exist in Airtable)")
    p.add_argument("--no-notify", action="store_true", help="Skip Slack notification")

    # Create manually (fallback)
    p = sub.add_parser("create", help="Create model config manually (no Airtable)")
    _add_model_args(p)

    # Generate
    p = sub.add_parser("generate", help="Generate outputs for existing model config")
    p.add_argument("folder", help="Model folder name")

    args = parser.parse_args()

    cmds = {
        "check": cmd_check,
        "onboard": cmd_onboard,
        "create": cmd_create,
        "generate": cmd_generate,
    }

    if args.command in cmds:
        cmds[args.command](args)
    else:
        parser.print_help()


def _add_model_args(parser):
    """Add common model arguments to a subparser."""
    parser.add_argument("--name", required=True, help="Model name")
    parser.add_argument("--gender", choices=["female", "male"], default="female")
    parser.add_argument("--traffic", default="social_media",
                       help="Traffic source: reddit, oftv, tiktok, dating_app, etc.")
    parser.add_argument("--age", type=int, default=22)
    parser.add_argument("--nationality", default="American")
    parser.add_argument("--location", default="Unknown")
    parser.add_argument("--origin", default=None)
    parser.add_argument("--page", default="Mixed", help="Page type: Mixed, Paid Page, Free Page")
    parser.add_argument("--personality", default=None, help="Personality description")
    parser.add_argument("--voice", default=None, help="Voice/texting style description")
    parser.add_argument("--pet-names", default=None, help="Pet names (comma-separated)")
    parser.add_argument("--never", default=None, help="Words to never use")
    parser.add_argument("--interests", default=None, help="Interests (comma-separated)")
    parser.add_argument("--physical", default=None, help="Physical description")
    parser.add_argument("--job", default=None, help="Job/profession")
    parser.add_argument("--countries", default=None, help="Countries traveled/from")
    parser.add_argument("--explicit", action="store_true", default=True,
                       help="Explicit content (default: yes)")
    parser.add_argument("--non-explicit", dest="explicit", action="store_false",
                       help="Non-explicit content")
    parser.add_argument("--notes", default=None, help="Special notes/restrictions")


if __name__ == "__main__":
    main()
