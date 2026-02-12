#!/usr/bin/env python3
"""
diversify_cumcontrol.py — Diversify cumcontrol scripts for all explicit models.

Current state: cumcontrol messages are IDENTICAL across most models (2/10 QA score).
Solution: 5 different sets based on model archetype, with per-model voice adaptation.

Sets:
  A — Playful/Teasing (younger, playful models)
  B — Dominant/Confident (bold, in-control models)
  C — Emotional/Intimate (sweet, vulnerable models)
  D — Experienced/Mature (MILF/older models)
  E — Masculine/Jock (male models)

Skipped:
  jessica34, irina — already have custom non-explicit cumcontrol
  putri, max — separate configs
"""

import re
import os

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(TOOLS_DIR, "models")

# ═══════════════════════════════════════════════════════════════
# BANNED WORDS CHECK (safety net)
# ═══════════════════════════════════════════════════════════════

BANNED_WORDS = {
    "meet", "drink", "drinking", "drunk", "slave", "slavery", "choke", "choked",
    "choking", "blood", "bleeding", "animal", "dog", "farm", "force", "forced",
    "consent", "entrance", "golden", "cycle", "bait", "jail", "whipped", "toilet",
    "showers", "pee", "piss", "shit", "scat", "vomit", "death", "kill", "young",
    "teen", "child", "underage", "rape", "kidnap", "torture", "strangle",
    "suffocate", "fist", "fisted", "fisting", "gangbang", "escort", "prostitute",
    "cashapp", "paypal", "venmo", "fansly", "twelve", "fifteen", "eleven",
}


def check_banned(text, model_key, msg_name):
    """Check a message for banned words. Return list of found words."""
    found = []
    words = re.findall(r"[a-zA-Z]+", text.lower())
    for w in words:
        if w in BANNED_WORDS:
            found.append(w)
    if found:
        print(f"  !! BANNED WORD(S) {found} in {model_key}/{msg_name}: {text[:60]}...")
    return found


# ═══════════════════════════════════════════════════════════════
# BASE SETS — 5 archetypes, each with cumcontrol1 + cumcontrol2
# ═══════════════════════════════════════════════════════════════

SET_A = {
    "cc1": [
        ("edge1", "not yet... I said not yet", "CONTROL. More PPVs to send. Create urgency to open next."),
        ("edge2", "you better not be close already... I have more to show you", "EDGE variant."),
        ("sync1", "okay NOW we can go together... open this", "SYNC. Send PPV."),
        ("sync2", "I want to feel it at the same time... watch this first", "SYNC variant. Send PPV."),
        ("delay1", "wait wait wait... I have one more thing for you before you finish", "DELAY. Send final PPV."),
        ("delay2", "if you finish before you see what I'm sending next you'll regret it", "DELAY variant."),
    ],
    "cc2": [
        ("edge1", "slow down... I'm not letting you off that easy", "CONTROL."),
        ("edge2", "patience... the best part hasn't even happened yet", "EDGE variant."),
        ("sync1", "okay I'm ready now too... watch this with me", "SYNC. Send PPV."),
        ("sync2", "let's do this together... but you have to open this first", "SYNC variant."),
        ("delay1", "don't you dare... not until you see what I just did", "DELAY. Send PPV."),
        ("delay2", "hold on just a little longer, I promise this next one is worth it", "DELAY variant."),
    ],
}

SET_B = {
    "cc1": [
        ("edge1", "I didn't say you could cum yet", "CONTROL."),
        ("edge2", "not a chance... you're going to wait until I say so", "EDGE variant."),
        ("sync1", "now... right now, with me. open this", "SYNC. Send PPV."),
        ("sync2", "I'm right there too, let's finish this... but you need to see this first", "SYNC variant. Send PPV."),
        ("delay1", "you're not done until I say you are... open this", "DELAY. Send PPV."),
        ("delay2", "trust me you want to edge just a little longer for this one", "DELAY variant."),
    ],
    "cc2": [
        ("edge1", "slow down, I'm in control here", "CONTROL."),
        ("edge2", "if you finish without my permission I'll be annoyed", "EDGE variant."),
        ("sync1", "okay you earned it... let's go together, open this", "SYNC. Send PPV."),
        ("sync2", "I want us to finish at the same time... this one will push you over", "SYNC variant."),
        ("delay1", "hold it... what I'm about to send is the best one and you'll want to last for it", "DELAY. Send PPV."),
        ("delay2", "edge for me... just a little more... this last one is everything", "DELAY variant."),
    ],
}

SET_C = {
    "cc1": [
        ("edge1", "not yet... I want this to last a little longer with you", "CONTROL."),
        ("edge2", "please don't finish yet... I'm not ready for this to be over", "EDGE variant."),
        ("sync1", "I want us to finish together... open this and let go with me", "SYNC. Send PPV."),
        ("sync2", "stay with me, I'm almost there too... watch this", "SYNC variant. Send PPV."),
        ("delay1", "wait for me... I have one more thing and I want you to see it before we finish", "DELAY. Send PPV."),
        ("delay2", "just hold on a little more, I want the last thing you see to be this", "DELAY variant."),
    ],
    "cc2": [
        ("edge1", "slow down... I want to feel every second of this with you", "CONTROL."),
        ("edge2", "don't rush... this is too good to end yet", "EDGE variant."),
        ("sync1", "okay... together, right now... open this", "SYNC. Send PPV."),
        ("sync2", "I need you to see this before we both let go", "SYNC variant."),
        ("delay1", "please wait... what I'm about to send, I want you to really take it in", "DELAY. Send PPV."),
        ("delay2", "just a little longer for me? the next one is special", "DELAY variant."),
    ],
}

SET_D = {
    "cc1": [
        ("edge1", "I can tell you're close... not yet amor, I know what I'm doing", "CONTROL."),
        ("edge2", "a man who can wait gets rewarded... trust me on that", "EDGE variant."),
        ("sync1", "now we go together... I've been holding back too. open this", "SYNC. Send PPV."),
        ("sync2", "I want to feel you let go while I do the same... watch this first", "SYNC variant. Send PPV."),
        ("delay1", "hold it for me... I have years of experience and this next one is my best work", "DELAY. Send PPV."),
        ("delay2", "patience... what's coming is worth every second of waiting", "DELAY variant."),
    ],
    "cc2": [
        ("edge1", "slow down for me... I know exactly when to let you go", "CONTROL."),
        ("edge2", "not yet... a little more anticipation makes it so much better, trust me", "EDGE variant."),
        ("sync1", "okay... let's both let go right now. open this", "SYNC. Send PPV."),
        ("sync2", "I'm ready when you are... but see this first", "SYNC variant."),
        ("delay1", "one more for you before we're done... this is the one I'm most proud of", "DELAY. Send PPV."),
        ("delay2", "save it for this last one, I promise you it's going to be worth it", "DELAY variant."),
    ],
}

SET_E = {
    "cc1": [
        ("edge1", "bro don't you dare finish yet... I'm not even close to done", "CONTROL."),
        ("edge2", "hold it... you're gonna last until I say otherwise", "EDGE variant."),
        ("sync1", "aight let's bust together... open this", "SYNC. Send PPV."),
        ("sync2", "I'm close too man, let's go at the same time... check this", "SYNC variant."),
        ("delay1", "edge for me... what I'm about to send is gonna hit different", "DELAY. Send PPV."),
        ("delay2", "trust me you wanna save it for this next one, it's the best one", "DELAY variant."),
    ],
    "cc2": [
        ("edge1", "yo slow down... we're not done here", "CONTROL."),
        ("edge2", "hold it, I got one more thing to show you first", "EDGE variant."),
        ("sync1", "alright go time, let's finish this together... open it", "SYNC. Send PPV."),
        ("sync2", "I'm about to blow too, watch this and let's go", "SYNC variant."),
        ("delay1", "don't finish yet bro... this last one? insane", "DELAY. Send PPV."),
        ("delay2", "edge just a bit more... the finale is worth it", "DELAY variant."),
    ],
}

SETS = {"A": SET_A, "B": SET_B, "C": SET_C, "D": SET_D, "E": SET_E}


# ═══════════════════════════════════════════════════════════════
# MODEL CONFIGS — set assignment + voice overrides (pet names, emojis)
# Override indices: 0=edge1, 1=edge2, 2=sync1, 3=sync2, 4=delay1, 5=delay2
# ═══════════════════════════════════════════════════════════════

MODELS = {
    # ────────────────────────────────────────────
    # SET A — Playful/Teasing
    # ────────────────────────────────────────────
    "riri": {
        "file": "riri.py",
        "set": "A",
        "cc1_overrides": {
            0: ("edge1", "not yet... I said not yet babe", "CONTROL. More PPVs to send. Create urgency to open next."),
            3: ("sync2", "I want to feel it at the same time babe... watch this first", "SYNC variant. Send PPV."),
        },
        "cc2_overrides": {
            0: ("edge1", "slow down babe... I'm not letting you off that easy", "CONTROL."),
            5: ("delay2", "hold on just a little longer babe, I promise this next one is worth it", "DELAY variant."),
        },
    },
    "antonella": {
        "file": "antonella.py",
        "set": "A",
        "cc1_overrides": {
            0: ("edge1", "not yet... I said not yet 🖤", "CONTROL. More PPVs to send. Create urgency to open next."),
            1: ("edge2", "you better not be close already cutie... I have more to show you 💜", "EDGE variant."),
            2: ("sync1", "okay NOW we can go together... open this 🖤", "SYNC. Send PPV."),
            5: ("delay2", "if you finish before you see what I'm sending next you'll regret it 💜", "DELAY variant."),
        },
        "cc2_overrides": {
            0: ("edge1", "slow down cutie... I'm not letting you off that easy 🖤", "CONTROL."),
            2: ("sync1", "okay I'm ready now too... watch this with me 💜", "SYNC. Send PPV."),
            4: ("delay1", "don't you dare... not until you see what I just did 🖤", "DELAY. Send PPV."),
        },
    },
    "vera": {
        "file": "vera.py",
        "set": "A",
        "cc1_overrides": {
            0: ("edge1", "not yet... I said not yet love", "CONTROL. More PPVs to send. Create urgency to open next."),
            4: ("delay1", "wait wait wait love... I have one more thing for you before you finish", "DELAY. Send final PPV."),
        },
        "cc2_overrides": {
            2: ("sync1", "okay I'm ready now too love... watch this with me", "SYNC. Send PPV."),
            5: ("delay2", "hold on just a little longer love, I promise this next one is worth it", "DELAY variant."),
        },
    },
    "mialuna": {
        "file": "mialuna.py",
        "set": "A",
        "cc1_overrides": {
            0: ("edge1", "not yet... I said not yet 😏", "CONTROL. More PPVs to send. Create urgency to open next."),
            1: ("edge2", "you better not be close already babe... I have more to show you 🔥", "EDGE variant."),
            2: ("sync1", "okay NOW we can go together... open this 🔥", "SYNC. Send PPV."),
        },
        "cc2_overrides": {
            0: ("edge1", "slow down babe... I'm not letting you off that easy 😏", "CONTROL."),
            2: ("sync1", "okay I'm ready now too... watch this with me 🔥", "SYNC. Send PPV."),
            5: ("delay2", "hold on just a little longer, I promise this next one is worth it 😏", "DELAY variant."),
        },
    },
    "emilybell": {
        "file": "emilybell.py",
        "set": "A",
        "cc1_overrides": {
            0: ("edge1", "not yet... I said not yet 😏", "CONTROL. More PPVs to send. Create urgency to open next."),
            1: ("edge2", "you better not be close already babe... I have more to show you 💋", "EDGE variant."),
            2: ("sync1", "okay NOW we can go together... open this 🔥", "SYNC. Send PPV."),
            4: ("delay1", "wait wait wait babe... I have one more thing for you before you finish 💋", "DELAY. Send final PPV."),
        },
        "cc2_overrides": {
            0: ("edge1", "slow down babe... I'm not letting you off that easy 😏", "CONTROL."),
            2: ("sync1", "okay I'm ready now too... watch this with me 🔥", "SYNC. Send PPV."),
            5: ("delay2", "hold on just a little longer babe, I promise this next one is worth it 💋", "DELAY variant."),
        },
    },
    "lia": {
        "file": "lia.py",
        "set": "A",
        "cc1_overrides": {
            0: ("edge1", "not yet... I said not yet love", "CONTROL. More PPVs to send. Create urgency to open next."),
            3: ("sync2", "I want to feel it at the same time love... watch this first", "SYNC variant. Send PPV."),
        },
        "cc2_overrides": {
            0: ("edge1", "slow down love... I'm not letting you off that easy", "CONTROL."),
            3: ("sync2", "let's do this together love... but you have to open this first", "SYNC variant."),
        },
    },

    # ────────────────────────────────────────────
    # SET B — Dominant/Confident
    # ────────────────────────────────────────────
    "jasmine": {
        "file": "jasmine.py",
        "set": "B",
        "cc1_overrides": {
            0: ("edge1", "I didn't say you could cum yet papi", "CONTROL."),
            2: ("sync1", "now... right now, with me papi. open this", "SYNC. Send PPV."),
            4: ("delay1", "you're not done until I say you are papi... open this", "DELAY. Send PPV."),
        },
        "cc2_overrides": {
            1: ("edge2", "if you finish without my permission I'll be annoyed papi", "EDGE variant."),
            2: ("sync1", "okay you earned it papi... let's go together, open this", "SYNC. Send PPV."),
            5: ("delay2", "edge for me papi... just a little more... this last one is everything", "DELAY variant."),
        },
    },
    "maddison": {
        "file": "maddison.py",
        "set": "B",
        "cc1_overrides": {
            0: ("edge1", "I didn't say you could cum yet Daddy", "CONTROL."),
            1: ("edge2", "not a chance... you're going to wait until I say so Daddy", "EDGE variant."),
            3: ("sync2", "I'm right there too Daddy, let's finish this... but you need to see this first", "SYNC variant. Send PPV."),
        },
        "cc2_overrides": {
            0: ("edge1", "slow down Daddy, I'm in control here", "CONTROL."),
            3: ("sync2", "I want us to finish at the same time Daddy... this one will push you over", "SYNC variant."),
            5: ("delay2", "edge for me Daddy... just a little more... this last one is everything", "DELAY variant."),
        },
    },
    "chayla": {
        "file": "chayla.py",
        "set": "B",
        "cc1_overrides": {
            0: ("edge1", "I didn't say you could cum yet babe 🔥", "CONTROL."),
            1: ("edge2", "not a chance... you're going to wait until I say so 😏", "EDGE variant."),
            2: ("sync1", "now... right now, with me babe. open this 🔥", "SYNC. Send PPV."),
        },
        "cc2_overrides": {
            0: ("edge1", "slow down babe, I'm in control here 😏", "CONTROL."),
            2: ("sync1", "okay you earned it babe... let's go together, open this 🔥", "SYNC. Send PPV."),
            5: ("delay2", "edge for me... just a little more... this last one is everything 😏", "DELAY variant."),
        },
    },
    "lina": {
        "file": "lina.py",
        "set": "B",
        "cc1_overrides": {
            0: ("edge1", "I didn't say you could cum yet love ✨", "CONTROL."),
            2: ("sync1", "now... right now, with me love. open this ✨", "SYNC. Send PPV."),
            5: ("delay2", "trust me you want to edge just a little longer for this one 💕", "DELAY variant."),
        },
        "cc2_overrides": {
            0: ("edge1", "slow down love, I'm in control here ✨", "CONTROL."),
            2: ("sync1", "okay you earned it love... let's go together, open this 💕", "SYNC. Send PPV."),
            5: ("delay2", "edge for me... just a little more... this last one is everything ✨", "DELAY variant."),
        },
    },
    "zansi": {
        "file": "zansi.py",
        "set": "B",
        "cc1_overrides": {
            0: ("edge1", "I didn't say you could cum yet babe 😏", "CONTROL."),
            2: ("sync1", "now... right now, with me babe. open this", "SYNC. Send PPV."),
            4: ("delay1", "you're not done until I say you are... open this 😏", "DELAY. Send PPV."),
        },
        "cc2_overrides": {
            0: ("edge1", "slow down babe, I'm in control here 😏", "CONTROL."),
            2: ("sync1", "okay you earned it babe... let's go together, open this", "SYNC. Send PPV."),
            4: ("delay1", "hold it... what I'm about to send is the best one and you'll want to last for it 😏", "DELAY. Send PPV."),
        },
    },

    # ────────────────────────────────────────────
    # SET C — Emotional/Intimate
    # ────────────────────────────────────────────
    "eva": {
        "file": "eva.py",
        "set": "C",
        "cc1_overrides": {
            0: ("edge1", "not yet papi... I want this to last a little longer with you", "CONTROL."),
            2: ("sync1", "I want us to finish together papi... open this and let go with me", "SYNC. Send PPV."),
            4: ("delay1", "wait for me papi... I have one more thing and I want you to see it before we finish", "DELAY. Send PPV."),
        },
        "cc2_overrides": {
            0: ("edge1", "slow down papi... I want to feel every second of this with you", "CONTROL."),
            2: ("sync1", "okay papi... together, right now... open this", "SYNC. Send PPV."),
            5: ("delay2", "just a little longer for me papi? the next one is special", "DELAY variant."),
        },
    },
    "isabella": {
        "file": "isabella.py",
        "set": "C",
        "cc1_overrides": {
            0: ("edge1", "not yet love... I want this to last a little longer with you", "CONTROL."),
            3: ("sync2", "stay with me love, I'm almost there too... watch this", "SYNC variant. Send PPV."),
        },
        "cc2_overrides": {
            0: ("edge1", "slow down love... I want to feel every second of this with you", "CONTROL."),
            5: ("delay2", "just a little longer for me love? the next one is special", "DELAY variant."),
        },
    },
    "miabrooks": {
        "file": "miabrooks.py",
        "set": "C",
        "cc1_overrides": {
            0: ("edge1", "not yet babe... I want this to last a little longer with you 😏", "CONTROL."),
            1: ("edge2", "please don't finish yet... I'm not ready for this to be over 🥺", "EDGE variant."),
            2: ("sync1", "I want us to finish together babe... open this and let go with me 💋", "SYNC. Send PPV."),
        },
        "cc2_overrides": {
            0: ("edge1", "slow down babe... I want to feel every second of this with you 😏", "CONTROL."),
            3: ("sync2", "I need you to see this before we both let go babe 🥺", "SYNC variant."),
            5: ("delay2", "just a little longer for me babe? the next one is special 💋", "DELAY variant."),
        },
    },
    "ashley": {
        "file": "ashley.py",
        "set": "C",
        "cc1_overrides": {
            0: ("edge1", "not yet babe... I want this to last a little longer with you 💕", "CONTROL."),
            1: ("edge2", "please don't finish yet... I'm not ready for this to be over 🙈", "EDGE variant."),
            2: ("sync1", "I want us to finish together... open this and let go with me 💕", "SYNC. Send PPV."),
        },
        "cc2_overrides": {
            0: ("edge1", "slow down babe... I want to feel every second of this with you 😊", "CONTROL."),
            3: ("sync2", "I need you to see this before we both let go 🙈", "SYNC variant."),
            5: ("delay2", "just a little longer for me babe? the next one is special 💕", "DELAY variant."),
        },
    },
    "lana": {
        "file": "lana.py",
        "set": "C",
        "cc1_overrides": {
            0: ("edge1", "not yet babe... I want this to last a little longer with you 🌸", "CONTROL."),
            1: ("edge2", "please don't finish yet... I'm not ready for this to be over 🥺", "EDGE variant."),
            2: ("sync1", "I want us to finish together... open this and let go with me 🌸", "SYNC. Send PPV."),
            5: ("delay2", "just hold on a little more, I want the last thing you see to be this 🥺", "DELAY variant."),
        },
        "cc2_overrides": {
            0: ("edge1", "slow down babe... I want to feel every second of this with you 💕", "CONTROL."),
            2: ("sync1", "okay babe... together, right now... open this 🌸", "SYNC. Send PPV."),
            5: ("delay2", "just a little longer for me babe? the next one is special 🥺", "DELAY variant."),
        },
    },

    # ────────────────────────────────────────────
    # SET D — Experienced/Mature
    # ────────────────────────────────────────────
    "fernanda": {
        "file": "fernanda.py",
        "set": "D",
        "cc1_overrides": {
            # edge1 base already has "amor"
            2: ("sync1", "now we go together amor... I've been holding back too. open this", "SYNC. Send PPV."),
        },
        "cc2_overrides": {
            0: ("edge1", "slow down for me amor... I know exactly when to let you go", "CONTROL."),
            5: ("delay2", "save it for this last one amor, I promise you it's going to be worth it", "DELAY variant."),
        },
    },
    "jessica36": {
        "file": "jessica36.py",
        "set": "D",
        "cc1_overrides": {
            # edge1 base already has "amor"
            3: ("sync2", "I want to feel you let go while I do the same amor... watch this first", "SYNC variant. Send PPV."),
        },
        "cc2_overrides": {
            2: ("sync1", "okay amor... let's both let go right now. open this", "SYNC. Send PPV."),
            5: ("delay2", "save it for this last one amor, I promise you it's going to be worth it", "DELAY variant."),
        },
    },
    "faby": {
        "file": "faby.py",
        "set": "D",
        "cc1_overrides": {
            # edge1 base already has "amor"
            1: ("edge2", "a man who can wait gets rewarded gostoso... trust me on that", "EDGE variant."),
            2: ("sync1", "now we go together amor... I've been holding back too. open this 😏", "SYNC. Send PPV."),
        },
        "cc2_overrides": {
            0: ("edge1", "slow down for me gostoso... I know exactly when to let you go", "CONTROL."),
            2: ("sync1", "okay amor... let's both let go right now. open this 😏", "SYNC. Send PPV."),
            5: ("delay2", "save it for this last one amor, I promise you it's going to be worth it 😏", "DELAY variant."),
        },
    },

    # ────────────────────────────────────────────
    # SET E — Masculine/Jock
    # ────────────────────────────────────────────
    "jockurworld": {
        "file": "jockurworld.py",
        "set": "E",
        "cc1_overrides": {},  # Base text already has bro/man
        "cc2_overrides": {},
    },
    "marco": {
        "file": "marco.py",
        "set": "E",
        "cc1_overrides": {},  # Base text already has bro/man
        "cc2_overrides": {},
    },
}


# ═══════════════════════════════════════════════════════════════
# CORE LOGIC
# ═══════════════════════════════════════════════════════════════

def get_model_cumcontrol(model_key, model_cfg):
    """Build the customized cumcontrol1 and cumcontrol2 for a model."""
    base_set = SETS[model_cfg["set"]]

    # Start with base set copies
    cc1 = list(base_set["cc1"])
    cc2 = list(base_set["cc2"])

    # Apply per-model overrides (pet names, emojis)
    for idx, override in model_cfg.get("cc1_overrides", {}).items():
        cc1[idx] = override
    for idx, override in model_cfg.get("cc2_overrides", {}).items():
        cc2[idx] = override

    return cc1, cc2


def format_cumcontrol_block(indent, key, messages):
    """Format a cumcontrol block as Python source code."""
    lines = [f'{indent}"{key}": ([']
    for name, text, note in messages:
        text_esc = text.replace('"', '\\"')
        note_esc = note.replace('"', '\\"')
        lines.append(f'{indent}    ("{name}", "{text_esc}", "{note_esc}"),')
    lines.append(f'{indent}], "sit"),')
    return "\n".join(lines)


def replace_cumcontrol_in_file(content, cc1_messages, cc2_messages):
    """Replace existing cumcontrol block(s) with cumcontrol1 + cumcontrol2."""

    # === Case 1: Already has cumcontrol1 + cumcontrol2 (re-run) ===
    p1 = re.compile(
        r'^(\s*)"cumcontrol1":\s*\(\[\s*\n(?:.*\n)*?\s*\],\s*"sit"\),',
        re.MULTILINE,
    )
    p2 = re.compile(
        r'^\s*"cumcontrol2":\s*\(\[\s*\n(?:.*\n)*?\s*\],\s*"sit"\),',
        re.MULTILINE,
    )

    m1 = p1.search(content)
    m2 = p2.search(content)

    if m1 and m2:
        indent = m1.group(1)
        start = min(m1.start(), m2.start())
        end = max(m1.end(), m2.end())
        cc1_block = format_cumcontrol_block(indent, "cumcontrol1", cc1_messages)
        cc2_block = format_cumcontrol_block(indent, "cumcontrol2", cc2_messages)
        return content[:start] + cc1_block + "\n" + cc2_block + content[end:]

    # === Case 2: Single "cumcontrol" block (first run) ===
    p_single = re.compile(
        r'^(\s*)"cumcontrol":\s*\(\[\s*\n(?:.*\n)*?\s*\],\s*"sit"\),',
        re.MULTILINE,
    )
    m = p_single.search(content)

    if m:
        indent = m.group(1)
        cc1_block = format_cumcontrol_block(indent, "cumcontrol1", cc1_messages)
        cc2_block = format_cumcontrol_block(indent, "cumcontrol2", cc2_messages)
        return content[:m.start()] + cc1_block + "\n" + cc2_block + content[m.end():]

    return None


def insert_cumcontrol_in_file(content, cc1_messages, cc2_messages):
    """Insert cumcontrol1 + cumcontrol2 before the dickpic section (fallback)."""
    pattern = re.compile(r'^(\s*)"dickpic":', re.MULTILINE)
    match = pattern.search(content)
    if not match:
        return None

    indent = match.group(1)
    cc1_block = format_cumcontrol_block(indent, "cumcontrol1", cc1_messages)
    cc2_block = format_cumcontrol_block(indent, "cumcontrol2", cc2_messages)
    insertion = cc1_block + "\n" + cc2_block + "\n"
    return content[: match.start()] + insertion + content[match.start() :]


# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════

def main():
    print("=" * 60)
    print("DIVERSIFY CUMCONTROL")
    print("Replacing identical scripts with model-specific sets")
    print("=" * 60)
    print()

    success = 0
    fail = 0
    skip = 0
    banned_found = 0

    for model_key, model_cfg in MODELS.items():
        filepath = os.path.join(MODELS_DIR, model_cfg["file"])

        if not os.path.exists(filepath):
            print(f"  SKIP  {model_key:<15} file '{model_cfg['file']}' not found")
            skip += 1
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Build customized messages
        cc1, cc2 = get_model_cumcontrol(model_key, model_cfg)

        # Safety: check for banned words in all messages
        for msgs, label in [(cc1, "cc1"), (cc2, "cc2")]:
            for name, text, note in msgs:
                found = check_banned(text, model_key, f"{label}.{name}")
                if found:
                    banned_found += len(found)

        # Try replacement first, then insertion
        new_content = replace_cumcontrol_in_file(content, cc1, cc2)

        if new_content is None:
            new_content = insert_cumcontrol_in_file(content, cc1, cc2)

        if new_content is None:
            print(f"  FAIL  {model_key:<15} could not find cumcontrol or dickpic section")
            fail += 1
            continue

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

        set_id = model_cfg["set"]
        n_overrides = len(model_cfg.get("cc1_overrides", {})) + len(
            model_cfg.get("cc2_overrides", {})
        )
        print(f"  OK    {model_key:<15} SET {set_id}  ({n_overrides} voice adaptations)")
        success += 1

    # ── Summary ──
    print()
    print("-" * 60)
    print(f"Results: {success} updated, {skip} skipped, {fail} failed")
    if banned_found:
        print(f"!! {banned_found} BANNED WORD(S) DETECTED — review above !!")
    else:
        print("Banned words check: CLEAN")
    print()

    set_names = {
        "A": "Playful/Teasing",
        "B": "Dominant/Confident",
        "C": "Emotional/Intimate",
        "D": "Experienced/Mature",
        "E": "Masculine/Jock",
    }
    print("Set Assignments:")
    for set_id in ["A", "B", "C", "D", "E"]:
        models_in_set = [k for k, v in MODELS.items() if v["set"] == set_id]
        print(f"  SET {set_id} ({set_names[set_id]:<22}): {', '.join(models_in_set)}")

    print()
    print("Skipped models (custom cumcontrol): jessica34, irina")
    print("Skipped models (separate config):   putri, max")


if __name__ == "__main__":
    main()
