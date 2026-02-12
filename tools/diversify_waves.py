#!/usr/bin/env python3
"""
diversify_waves.py — Diversify NR Waves & Boosters across all models.

Problem: NR waves (no-response follow-ups) and boosters (h3, h4, h7) were
nearly identical across models. Subscribers following multiple models would
see the same messages, breaking the real-time illusion.

Solution: 5 different wave sets and 5 different booster sets, assigned
to models based on their personality. Pet names and emojis are preserved
per-model to maintain each model's unique voice.

Only changes: NR-W1 to NR-W5 text, and boosters h3, h4, h7 text.
Notes column stays the same. h1, h2, h5, h6, h8 stay the same.
"""
import re
import os
import sys

# Fix Windows console encoding for emoji/unicode output
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(SCRIPT_DIR, "models")


# ═══════════════════════════════════════════════════════════════
# WAVE SETS — NR-W1 through NR-W5
# ═══════════════════════════════════════════════════════════════

WAVE_SETS = {
    "A": {  # Direct/Curious
        "W1": "hey?",
        "W2": "you seriously need to see what I just did...",
        "W3": "okay I guess you're busy... might delete this later, it was only for you",
        "W4": "hey hope you're good, text me when you're back",
        "W5": "can't stop thinking about earlier... you around?",
    },
    "B": {  # Playful/Teasing
        "W1": "helloooo",
        "W2": "I have something to show you but you're leaving me on read...",
        "W3": "fine I'll just keep this to myself then 😏",
        "W4": "miss talking to you, where'd you go?",
        "W5": "I made something special and you're the only one I want to show it to",
    },
    "C": {  # Casual/Chill
        "W1": "hey you",
        "W2": "literally just took something crazy and you're not even here to see it",
        "W3": "I'm starting to think you forgot about me...",
        "W4": "hey, just checking in on you",
        "W5": "still thinking about our conversation... come back when you can",
    },
    "D": {  # Emotional/Vulnerable
        "W1": "hi",
        "W2": "I wish you could see what I'm wearing right now...",
        "W3": "okay you're definitely busy... I'll save this for when you're back",
        "W4": "hope everything's okay with you, I'm here whenever",
        "W5": "been thinking about you all day... text me back?",
    },
    "E": {  # Bold/Confident
        "W1": "yo",
        "W2": "you're really going to miss out on what I just recorded...",
        "W3": "your loss... this was your exclusive",
        "W4": "hey, don't be a stranger",
        "W5": "I've got something that's going to blow your mind when you get back",
    },
}


# ═══════════════════════════════════════════════════════════════
# BOOSTER SETS — Only h3, h4, h7 (others are model-specific)
# ═══════════════════════════════════════════════════════════════

BOOSTER_SETS = {
    "A": {"h3": "don't stop", "h4": "you have no idea what you're doing to me", "h7": "more..."},
    "B": {"h3": "keep going", "h4": "I literally can't handle this right now", "h7": "again..."},
    "C": {"h3": "right there", "h4": "what are you doing to me", "h7": "please..."},
    "D": {"h3": "oh my god", "h4": "I'm losing my mind because of you", "h7": "I need more"},
    "E": {"h3": "yes", "h4": "you're driving me crazy right now", "h7": "don't stop..."},
}


# ═══════════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════════

def build_w4(wave_set, pet="", emoji=""):
    """Build W4 (warm close) with model's pet name and emoji."""
    if pet:
        w4_map = {
            "A": f"hey hope you're good{pet}, text me when you're back{emoji}",
            "B": f"miss talking to you{pet}, where'd you go?{emoji}",
            "C": f"hey{pet}, just checking in on you{emoji}",
            "D": f"hope everything's okay with you{pet}, I'm here whenever{emoji}",
            "E": f"hey{pet}, don't be a stranger{emoji}",
        }
    else:
        w4_map = {
            "A": f"hey hope you're good, text me when you're back{emoji}",
            "B": f"miss talking to you, where'd you go?{emoji}",
            "C": f"hey, just checking in on you{emoji}",
            "D": f"hope everything's okay with you, I'm here whenever{emoji}",
            "E": f"hey, don't be a stranger{emoji}",
        }
    return w4_map[wave_set]


def build_waves(m):
    """Build all 5 NR wave texts adapted to model's voice."""
    ws = m["wave_set"]
    waves = {}

    # W1 — Ping
    if m.get("w1_override"):
        waves["W1"] = m["w1_override"]
    else:
        waves["W1"] = WAVE_SETS[ws]["W1"] + m.get("w1_emoji", "")

    # W2 — Curiosity hook
    waves["W2"] = WAVE_SETS[ws]["W2"] + m.get("w2_emoji", "")

    # W3 — Takeaway
    waves["W3"] = WAVE_SETS[ws]["W3"] + m.get("w3_emoji", "")

    # W4 — Warm close (pet name + emoji)
    waves["W4"] = build_w4(ws, m.get("pet", ""), m.get("w4_emoji", ""))

    # W5 — Re-engagement
    waves["W5"] = WAVE_SETS[ws]["W5"] + m.get("w5_emoji", "")

    return waves


def build_boosters(m):
    """Build h3, h4, h7 booster texts from assigned set."""
    return dict(BOOSTER_SETS[m["booster_set"]])


def replace_tuple_text(content, tuple_id, new_text):
    """Replace the text field (2nd element) in a Python tuple like ("id", "text", ...)."""
    pattern = rf'(\("{re.escape(tuple_id)}",\s*)"[^"]*"'

    def replacer(match):
        return match.group(1) + '"' + new_text + '"'

    return re.subn(pattern, replacer, content, count=1)


def replace_in_file(filepath, m):
    """Find and replace NR wave texts and booster texts in a model .py file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    waves = build_waves(m)
    boosters = build_boosters(m)

    # Replace NR-W1 through NR-W5
    for i in range(1, 6):
        content, count = replace_tuple_text(content, f"NR-W{i}", waves[f"W{i}"])
        if count == 0:
            print(f"    WARNING: NR-W{i} not found")

    # Replace boosters h3, h4, h7
    for hk in ["h3", "h4", "h7"]:
        content, count = replace_tuple_text(content, hk, boosters[hk])
        if count == 0:
            print(f"    WARNING: {hk} not found")

    # Write back if changed
    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False


# ═══════════════════════════════════════════════════════════════
# MODEL ASSIGNMENTS
# Each model specifies:
#   - wave_set / booster_set: A-E
#   - pet: pet name to insert in W4 (with leading space)
#   - w1_override: completely replace W1 (e.g. Maddison's "Daddy?")
#   - w1_emoji..w5_emoji: emoji suffix for each wave position
# ═══════════════════════════════════════════════════════════════

MODELS = [
    # ─── Riri → SET A waves, SET A boosters ───
    {"file": "riri.py", "name": "Riri",
     "wave_set": "A", "booster_set": "A",
     "pet": " babe", "w4_emoji": " 💕"},

    # ─── Eva → SET D waves, SET C boosters ───
    {"file": "eva.py", "name": "Eva",
     "wave_set": "D", "booster_set": "C",
     "pet": " handsome", "w4_emoji": " 💕"},

    # ─── Antonella → SET B waves, SET B boosters ───
    {"file": "antonella.py", "name": "Antonella",
     "wave_set": "B", "booster_set": "B",
     "pet": " cutie", "w1_emoji": " 🥺", "w2_emoji": " 🖤",
     "w4_emoji": " 🖤", "w5_emoji": " 💜"},

    # ─── Jasmine → SET C waves, SET D boosters ───
    {"file": "jasmine.py", "name": "Jasmine",
     "wave_set": "C", "booster_set": "D",
     "pet": " handsome", "w4_emoji": " 💕"},

    # ─── Fernanda → SET D waves, SET C boosters ───
    {"file": "fernanda.py", "name": "Fernanda",
     "wave_set": "D", "booster_set": "C",
     "pet": " handsome", "w4_emoji": " 💕"},

    # ─── Isabella → SET B waves, SET A boosters ───
    {"file": "isabella.py", "name": "Isabella",
     "wave_set": "B", "booster_set": "A",
     "pet": " love", "w4_emoji": " 💕"},

    # ─── Jessica34 → SET C waves, SET D boosters ───
    {"file": "jessica34.py", "name": "Jessica34",
     "wave_set": "C", "booster_set": "D",
     "pet": "", "w1_emoji": " 😊", "w4_emoji": " 😊"},

    # ─── Jessica36 → SET A waves, SET B boosters ───
    {"file": "jessica36.py", "name": "Jessica36",
     "wave_set": "A", "booster_set": "B",
     "pet": "", "w1_emoji": " 😏", "w4_emoji": " 😊"},

    # ─── Maddison → SET E waves, SET E boosters ───
    {"file": "maddison.py", "name": "Maddison",
     "wave_set": "E", "booster_set": "E",
     "pet": " Daddy", "w1_override": "Daddy?"},

    # ─── Vera → SET D waves, SET C boosters ───
    {"file": "vera.py", "name": "Vera",
     "wave_set": "D", "booster_set": "C",
     "pet": "", "w1_emoji": " 😊", "w2_emoji": " 🌸",
     "w4_emoji": " 💕", "w5_emoji": " 🥰"},

    # ─── MiaLuna → SET B waves, SET D boosters ───
    {"file": "mialuna.py", "name": "MiaLuna",
     "wave_set": "B", "booster_set": "D",
     "pet": " handsome", "w1_emoji": " 😏", "w2_emoji": " 🔥",
     "w4_emoji": " ⚽", "w5_emoji": " 🔥"},

    # ─── MiaBrooks → SET C waves, SET B boosters ───
    {"file": "miabrooks.py", "name": "MiaBrooks",
     "wave_set": "C", "booster_set": "B",
     "pet": " handsome", "w1_emoji": " 🥺", "w2_emoji": " 💋",
     "w4_emoji": " 💋", "w5_emoji": " 😏"},

    # ─── Ashley → SET A waves, SET E boosters ───
    {"file": "ashley.py", "name": "Ashley",
     "wave_set": "A", "booster_set": "E",
     "pet": "", "w1_emoji": " 😊", "w2_emoji": " 💕",
     "w4_emoji": " 💕", "w5_emoji": " 😊"},

    # ─── Chayla → SET E waves, SET A boosters ───
    {"file": "chayla.py", "name": "Chayla",
     "wave_set": "E", "booster_set": "A",
     "pet": " babe", "w1_emoji": " 😏", "w2_emoji": " 🔥",
     "w4_emoji": " 💕", "w5_emoji": " 🔥"},

    # ─── EmilyBell → SET C waves, SET D boosters ───
    {"file": "emilybell.py", "name": "EmilyBell",
     "wave_set": "C", "booster_set": "D",
     "pet": " handsome", "w1_emoji": " 😏", "w2_emoji": " 💋",
     "w4_emoji": " 😏", "w5_emoji": " 🔥"},

    # ─── Lana → SET D waves, SET C boosters ───
    {"file": "lana.py", "name": "Lana",
     "wave_set": "D", "booster_set": "C",
     "pet": "", "w1_emoji": " 🌸", "w2_emoji": " 💕",
     "w3_emoji": " 🥺", "w4_emoji": " 🌸", "w5_emoji": " 💕"},

    # ─── Lia → SET B waves, SET B boosters ───
    {"file": "lia.py", "name": "Lia",
     "wave_set": "B", "booster_set": "B",
     "pet": "", "w1_emoji": " 🌸", "w2_emoji": " 💕",
     "w4_emoji": " 💕", "w5_emoji": " 🌸"},

    # ─── Lina → SET A waves, SET E boosters ───
    {"file": "lina.py", "name": "Lina",
     "wave_set": "A", "booster_set": "E",
     "pet": "", "w1_emoji": " 💕", "w2_emoji": " ✨",
     "w3_emoji": " 🎶", "w4_emoji": " 💕", "w5_emoji": " ✨"},

    # ─── Faby → SET E waves, SET A boosters ───
    {"file": "faby.py", "name": "Faby",
     "wave_set": "E", "booster_set": "A",
     "pet": " handsome", "w1_emoji": " 😏", "w4_emoji": " 💕"},

    # ─── Irina → SET D waves, SET C boosters ───
    {"file": "irina.py", "name": "Irina",
     "wave_set": "D", "booster_set": "C",
     "pet": "", "w1_emoji": " 😊", "w2_emoji": " 🥺",
     "w4_emoji": " 😊", "w5_emoji": " 💗"},

    # ─── Zansi → SET E waves, SET E boosters ───
    {"file": "zansi.py", "name": "Zansi",
     "wave_set": "E", "booster_set": "E",
     "pet": "", "w1_emoji": " 😏", "w4_emoji": " 💕", "w5_emoji": " 😏"},

    # ─── Jockurworld → SET E waves (male), SET E boosters ───
    {"file": "jockurworld.py", "name": "Jockurworld",
     "wave_set": "E", "booster_set": "E",
     "pet": " man"},
]


# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("  DIVERSIFYING NR WAVES & BOOSTERS")
    print("=" * 60)

    updated = 0
    skipped = 0
    errors = 0

    for m in MODELS:
        filepath = os.path.join(MODELS_DIR, m["file"])
        if not os.path.exists(filepath):
            print(f"\n  X {m['name']:15s} -- File not found: {m['file']}")
            errors += 1
            continue

        label = f"Waves=SET {m['wave_set']}  Boosters=SET {m['booster_set']}"
        print(f"\n{'-' * 55}")
        print(f"  {m['name']:15s} -- {label}")

        # Show planned changes
        waves = build_waves(m)
        for i in range(1, 6):
            print(f"    W{i}: \"{waves[f'W{i}']}\"")
        boosters = build_boosters(m)
        for hk in ["h3", "h4", "h7"]:
            print(f"    {hk}: \"{boosters[hk]}\"")

        if replace_in_file(filepath, m):
            print(f"  -> {m['file']} UPDATED")
            updated += 1
        else:
            print(f"  -- {m['file']} no changes needed")
            skipped += 1

    print(f"\n{'=' * 60}")
    print(f"  DONE -- {updated} updated, {skipped} unchanged, {errors} errors")
    print(f"{'=' * 60}")
