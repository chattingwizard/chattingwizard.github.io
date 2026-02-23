"""
Generate Smart Messages HTML pages for ALL models using personality profiles.
Includes built-in QA protocol for personality verification.

Usage: python tools/generate_all_nudges.py
"""
import os, sys, random, html as h
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from nudge_profiles import ALL_PROFILES

# ═══════════════════════════════════════════════════════════
# BANNED WORDS CHECK
# ═══════════════════════════════════════════════════════════
BANNED = {
    "abduction","abduct","force","forced","forcing","kidnap","rape","raped",
    "molest","strangle","suffocate","mutilate","torture","choke","choked",
    "chokes","choking","asphyxia","chloroform","unconscious","hypno","trance",
    "intox","paralyze","passed out","drink","drinking","drunk","child","teen",
    "preteen","lolita","underage","young","eleven","twelve","fifteen","animal",
    "dog","farm","blood","pee","piss","poo","poop","scat","vomit","fecal",
    "enema","cervix","lactation","menstrual","slave","fist","fisting","whipped",
    "gangbang","bukkake","bareback","meet","escort","hooker","prostitute",
    "cashapp","paypal","venmo","fansly","consent","cycle","entrance","golden",
    "incest","jail","toilet","showers","nigger","pedo","bait","blackmail",
    "blacked","knock","knocked","knocking",
}

def check_banned(text):
    words = text.lower().split()
    found = []
    for w in words:
        clean = w.strip(".,!?;:'\"")
        if clean in BANNED:
            found.append(clean)
    return found


# ═══════════════════════════════════════════════════════════
# MESSAGE GENERATORS (per gender + style)
# ═══════════════════════════════════════════════════════════

def gen_female_vip(p):
    g = p["greetings"]
    gl = p["greetings_long"]
    ew = p["emojis_warm"]
    ef = p["emojis_flirty"]
    pn = p["pet_names"]
    act = p["activity_chill"]
    miss = p["tone_miss"]

    e1, e2 = ew[0], ew[1 % len(ew)]
    e3 = ef[0]
    pn1 = pn[0] if pn else "babe"
    pn2 = pn[1 % len(pn)] if len(pn) > 1 else pn1

    collections = [
        {"msgs": [f"{g[0]} {e1}", miss], "wait": 15},
        {"msgs": [f"{g[1] if len(g)>1 else g[0]} look who's here {e3}", f"perfect timing... I {act}"], "wait": 15},
        {"msgs": [f"I missed you {e1}"]},
        {"msgs": [f"{gl[0]} {e2}", "I'm so bored rn... come talk to me?"], "wait": 20},
        {"msgs": [f"there you are {e3} I was waiting for you"]},
        {"msgs": [f"{{name}} {e1}", "I was hoping you'd come on today"], "wait": 15, "tag": True},
        {"msgs": [f"perfect timing... I need to tell you something {e2}"]},
        {"msgs": [f"guess what I'm doing rn {e3}", f"hmm actually... maybe I shouldn't say {e1}"], "wait": 20},
        {"msgs": [f"hey {pn1} {e1} you always show up at the right time"]},
        {"msgs": [f"you {e3}", f"I literally just thought \"I wish {{name}} was on\" and here you are"], "wait": 15, "tag": True},
    ]
    return collections


def gen_female_mid(p):
    g = p["greetings"]
    ew = p["emojis_warm"]
    ef = p["emojis_flirty"]
    pn = p["pet_names"]
    act_bored = p["activity_bored"]
    tease = p["tone_tease"]

    e1, e2 = ew[0], ew[1 % len(ew)]
    e3 = ef[0]
    pn1 = pn[0] if pn else "babe"

    collections = [
        {"msgs": [f"{g[0]} {e3}", "I'm in a mood rn and you popped up at the worst time"], "wait": 15},
        {"msgs": [f"omg I have something to show you {e1}"]},
        {"msgs": [f"{g[0]} {{name}} {e2}", "I was just thinking about last time we talked..."], "wait": 15, "tag": True},
        {"msgs": [f"well well... look who's here {e3}"]},
        {"msgs": [f"ugh I'm so bored {e1}", f"talk to me? I need a distraction from {act_bored}"], "wait": 20},
        {"msgs": [f"hey {pn1} {e3}", tease], "wait": 15},
        {"msgs": [f"I was literally about to text you {e2}"]},
        {"msgs": [f"hmm hi {e3}", "I'm lying in bed and I can't stop thinking about something"], "wait": 15},
        {"msgs": [f"hey {pn1} you caught me at a nice time {e1}"]},
        {"msgs": [f"wait {{name}}", f"I've been saving something for you and I can't wait anymore {e2}"], "wait": 10, "tag": True},
    ]
    return collections


def gen_female_low(p):
    g = p["greetings"]
    ew = p["emojis_warm"]
    ef = p["emojis_flirty"]
    pn = p["pet_names"]
    hook = p["tone_hook"]

    e1, e2 = ew[0], ew[1 % len(ew)]
    e3 = ef[0]
    pn1 = pn[0] if pn else "babe"

    collections = [
        {"msgs": [f"{g[0]} {e3}", "I have something I think you'll like"], "wait": 15},
        {"msgs": [f"omg you're on! I need to show you this {e1}"]},
        {"msgs": [f"hi {{name}} {e3}", f"you came at the right time... I'm feeling generous today {e1}"], "wait": 15, "tag": True},
        {"msgs": [f"{hook} {e2}"]},
        {"msgs": ["pssst", f"I have a surprise for you {e3}"], "wait": 10},
        {"msgs": [f"hey {pn1} {e1}", f"I just made something that I think only you would appreciate {e2}"], "wait": 15},
        {"msgs": [f"I'm only going to be in this mood for a little bit... come talk to me {e3}"]},
        {"msgs": [f"you {e3}", f"I was thinking about you earlier and got a little carried away... {e1}"], "wait": 15},
        {"msgs": [f"finally! I've been waiting for someone fun to come on {e1}"]},
        {"msgs": [f"wait {{name}}", f"there's something I've been wanting to ask you {e2}"], "wait": 10, "tag": True},
    ]
    return collections


def gen_female_zero(p):
    g = p["greetings"]
    ew = p["emojis_warm"]
    ef = p["emojis_flirty"]
    pn = p["pet_names"]

    e1, e2 = ew[0], ew[1 % len(ew)]
    e3 = ef[0]
    pn1 = pn[0] if pn else "babe"

    collections = [
        {"msgs": [f"I'm feeling generous today {e3}", f"there's more where that came from... {e1}"], "wait": 15, "attach": "free"},
        {"msgs": [f"I just made something really special and I'm sharing it with a few people at a special price {e3}"], "attach": "ppv"},
        {"msgs": [f"I'm bored and I just did something a little naughty {e1}", f"wanna see? I'll make it worth it {e3}"], "wait": 15},
        {"msgs": [f"{{name}}... I think you need to see this {e3}"], "tag": True, "attach": "free"},
        {"msgs": [f"ok I never do this but... {e1}", f"I'm sharing my best stuff at a special price rn {e3}"], "wait": 10, "attach": "ppv"},
        {"msgs": [f"this is what I'm wearing rn... or not wearing {e3}"], "attach": "free"},
        {"msgs": [f"I wonder if you can handle what I just made {e3}", f"prove me wrong... it's barely anything {e1}"], "wait": 15, "attach": "ppv"},
        {"msgs": [f"hey {{name}} a little preview just for you {e3} if you want the full thing just say the word {e1}"], "tag": True, "attach": "free"},
        {"msgs": [f"I just took this and idk if I should share it {e1}", f"you know what... here, it's yours {e3}"], "wait": 15, "attach": "free"},
        {"msgs": [f"{{name}} I'm doing something special today... my best stuff at the lowest price ever {e3}"], "tag": True, "attach": "ppv"},
    ]
    return collections


# ── MALE GENERATORS ──────────────────────────────────────

def gen_male_vip(p):
    g = p["greetings"]
    ew = p["emojis_warm"]
    ef = p["emojis_flirty"]
    pn = p["pet_names"]
    act = p["activity_chill"]
    miss = p["tone_miss"]

    e1 = ew[0]
    e2 = ef[0]
    pn1 = pn[0] if pn else "man"

    collections = [
        {"msgs": [f"{g[0]} {e1}", miss], "wait": 15},
        {"msgs": [f"look who's on {e1}", f"perfect timing... I {act}"], "wait": 15},
        {"msgs": [f"finally you're on {e1} missed talking to you {pn1}"]},
        {"msgs": [f"{g[1] if len(g)>1 else g[0]} {e1}", "bored rn... come talk"], "wait": 20},
        {"msgs": [f"there you are {e1} been waiting for you"]},
        {"msgs": [f"{{name}} {e1}", "was hoping you'd come on today"], "wait": 15, "tag": True},
        {"msgs": [f"perfect timing {e1} need to tell you something"]},
        {"msgs": [f"guess what I'm doing rn {e2}", f"actually... maybe I shouldn't say {e1}"], "wait": 20},
        {"msgs": [f"{g[0]} {pn1} {e1} you always show up at the right time"]},
        {"msgs": [f"you {e1}", f"ngl I was literally just thinking \"I wish {{name}} was on\""], "wait": 15, "tag": True},
    ]
    return collections


def gen_male_mid(p):
    g = p["greetings"]
    ew = p["emojis_warm"]
    ef = p["emojis_flirty"]
    pn = p["pet_names"]
    act_bored = p["activity_bored"]
    tease = p["tone_tease"]

    e1 = ew[0]
    e2 = ef[0]
    pn1 = pn[0] if pn else "man"

    collections = [
        {"msgs": [f"{g[0]} {e2}", "I'm in a mood rn and you showed up at the worst time"], "wait": 15},
        {"msgs": [f"got something to show you {pn1} {e1}"]},
        {"msgs": [f"{g[0]} {{name}} {e1}", "was just thinking about last time we talked"], "wait": 15, "tag": True},
        {"msgs": [f"well well... look who showed up {e1}"]},
        {"msgs": [f"bored rn {e1}", f"come talk, I need a break from {act_bored}"], "wait": 20},
        {"msgs": [f"{g[0]} {pn1} {e2}", tease], "wait": 15},
        {"msgs": [f"was literally about to message you {e1}"]},
        {"msgs": [f"hey {e2}", "lying in bed rn and I can't stop thinking about something"], "wait": 15},
        {"msgs": [f"{g[0]} {pn1} you caught me at a good time {e1}"]},
        {"msgs": [f"wait {{name}}", f"been saving something for you and I can't wait anymore {e2}"], "wait": 10, "tag": True},
    ]
    return collections


def gen_male_low(p):
    g = p["greetings"]
    ew = p["emojis_warm"]
    ef = p["emojis_flirty"]
    pn = p["pet_names"]
    hook = p["tone_hook"]

    e1 = ew[0]
    e2 = ef[0]
    pn1 = pn[0] if pn else "man"

    collections = [
        {"msgs": [f"{g[0]} {e2}", "got something I think you'll like"], "wait": 15},
        {"msgs": [f"you're on {e1} need to show you something"]},
        {"msgs": [f"{{name}} {e2}", f"you came at the right time... I'm feeling generous {e1}"], "wait": 15, "tag": True},
        {"msgs": [f"{hook}"]},
        {"msgs": ["pssst", f"got a surprise for you {e2}"], "wait": 10},
        {"msgs": [f"{g[0]} {pn1} {e1}", "just made something only you would appreciate"], "wait": 15},
        {"msgs": [f"only gonna be in this mood for a bit... come talk {e2}"]},
        {"msgs": [f"you {e2}", f"was thinking about you earlier and got a little carried away {e1}"], "wait": 15},
        {"msgs": [f"finally someone interesting is on {e1}"]},
        {"msgs": [f"{{name}}", "there's something I've been wanting to show you"], "wait": 10, "tag": True},
    ]
    return collections


def gen_male_zero(p):
    g = p["greetings"]
    ew = p["emojis_warm"]
    ef = p["emojis_flirty"]
    pn = p["pet_names"]

    e1 = ew[0]
    e2 = ef[0]
    pn1 = pn[0] if pn else "man"

    collections = [
        {"msgs": [f"feeling generous today {e1}", f"there's more where that came from {e2}"], "wait": 15, "attach": "free"},
        {"msgs": [f"just shot something and I'm letting a few people see it at a low price {e2}"], "attach": "ppv"},
        {"msgs": [f"bored and I just did something wild {e1}", f"wanna see? it's worth it {e2}"], "wait": 15},
        {"msgs": [f"{{name}}... you need to see this {e2}"], "tag": True, "attach": "free"},
        {"msgs": [f"don't normally do this but {e1}", f"dropping my best stuff at a crazy price rn {e2}"], "wait": 10, "attach": "ppv"},
        {"msgs": [f"this is what I look like rn after the gym {e2}"], "attach": "free"},
        {"msgs": [f"bet you can't handle what I just shot {e2}", f"prove me wrong {pn1}... it's basically nothing"], "wait": 15, "attach": "ppv"},
        {"msgs": [f"{{name}} preview just for you {e2} say the word for the full thing"], "tag": True, "attach": "free"},
        {"msgs": [f"just took this and not sure I should share it {e1}", f"you know what... here, it's yours {e2}"], "wait": 15, "attach": "free"},
        {"msgs": [f"{{name}} doing something special today... best stuff at the lowest price ever {e2}"], "tag": True, "attach": "ppv"},
    ]
    return collections


# ═══════════════════════════════════════════════════════════
# SPECIAL OVERRIDES (models with unique voice that need tweaks)
# ═══════════════════════════════════════════════════════════

def apply_maddison_overrides(model_data):
    """Maddison calls fans 'Daddy' and has bratty shy style."""
    for sm_key in ["vip", "mid", "low", "zero"]:
        for coll in model_data[sm_key]["collections"]:
            for i, msg in enumerate(coll["msgs"]):
                coll["msgs"][i] = msg.replace("babe", "Daddy").replace("love", "Daddy")

def apply_eva_overrides(model_data):
    """Eva never says babe/baby - uses papi/papasito."""
    for sm_key in ["vip", "mid", "low", "zero"]:
        for coll in model_data[sm_key]["collections"]:
            for i, msg in enumerate(coll["msgs"]):
                coll["msgs"][i] = msg.replace("babe", "papi").replace("baby", "papi")

def apply_noah_overrides(model_data):
    """Noah is minimal - strip excess emojis, shorter messages."""
    for sm_key in ["vip", "mid", "low", "zero"]:
        for coll in model_data[sm_key]["collections"]:
            for i, msg in enumerate(coll["msgs"]):
                msg = msg.replace(" 😏 ", " ").replace(" 😏", "").replace("😏 ", "")
                if msg.endswith(" 😏"):
                    msg = msg[:-2].strip()
                if len(msg) > 3 and not any(e in msg for e in ["😏"]):
                    if random.random() < 0.3:
                        msg = msg + " 😏"
                coll["msgs"][i] = msg


# ═══════════════════════════════════════════════════════════
# BUILD MODEL DATA
# ═══════════════════════════════════════════════════════════

def build_model_data(profile):
    is_male = profile["gender"] == "male"

    if is_male:
        vip_colls = gen_male_vip(profile)
        mid_colls = gen_male_mid(profile)
        low_colls = gen_male_low(profile)
        zero_colls = gen_male_zero(profile)
    else:
        vip_colls = gen_female_vip(profile)
        mid_colls = gen_female_mid(profile)
        low_colls = gen_female_low(profile)
        zero_colls = gen_female_zero(profile)

    recent_zero = "12"
    recent_other = "6"
    delay_low = "1 ~ 3"
    delay_other = "2 ~ 5"

    exclude_lists_zero = "Whale, Shark, Shrimp, Low Spenders, Rats"

    data = {
        "name": profile["name"],
        "folder": profile["folder"],
        "photo": profile.get("photo", "profile.jpeg"),
        "tagline": profile["tagline"],
        "vip": {
            "include": "Whale, Shark", "delay": delay_other, "recent": recent_other,
            "collections": vip_colls,
        },
        "mid": {
            "include": "Shrimp, Low Spenders", "delay": delay_other, "recent": recent_other,
            "collections": mid_colls,
        },
        "low": {
            "include": "Rats", "delay": delay_low, "recent": recent_other,
            "collections": low_colls,
        },
        "zero": {
            "include": "Fans", "exclude_lists": exclude_lists_zero,
            "delay": delay_other, "recent": recent_zero,
            "collections": zero_colls,
        },
    }

    # Apply special overrides
    name_lower = profile["name"].lower()
    if "maddison" in name_lower:
        apply_maddison_overrides(data)
    if "eva" in name_lower:
        apply_eva_overrides(data)
    if "noah" in name_lower:
        apply_noah_overrides(data)

    return data


# ═══════════════════════════════════════════════════════════
# QA PROTOCOL
# ═══════════════════════════════════════════════════════════

def qa_check(profile, model_data):
    """Run QA checks against personality profile."""
    issues = []
    name = profile["name"]
    never = set(w.lower() for w in profile.get("never_words", []))

    total_msgs = 0
    for sm_key in ["vip", "mid", "low", "zero"]:
        for ci, coll in enumerate(model_data[sm_key]["collections"]):
            for mi, msg in enumerate(coll["msgs"]):
                total_msgs += 1

                # Check banned words
                banned_found = check_banned(msg)
                if banned_found:
                    issues.append(f"  BANNED WORD in {sm_key} C{ci+1} M{mi+1}: {banned_found} -> \"{msg}\"")

                # Check never_words
                msg_lower = msg.lower()
                for nw in never:
                    if nw in msg_lower.split():
                        issues.append(f"  NEVER WORD '{nw}' in {sm_key} C{ci+1} M{mi+1}: \"{msg}\"")

    # Check pet name usage
    pet_names = profile.get("pet_names", [])
    all_text = " ".join(
        msg for sm_key in ["vip", "mid"]
        for coll in model_data[sm_key]["collections"]
        for msg in coll["msgs"]
    )
    has_pet = any(pn.lower() in all_text.lower() for pn in pet_names)
    if not has_pet and pet_names:
        issues.append(f"  WARNING: No pet names ({pet_names}) found in VIP/MID messages")

    # Check emoji presence
    all_emojis = profile.get("emojis_warm", []) + profile.get("emojis_flirty", [])
    has_emoji = any(e in all_text for e in all_emojis)
    if not has_emoji and all_emojis:
        issues.append(f"  WARNING: No expected emojis found in messages")

    return issues, total_msgs


# ═══════════════════════════════════════════════════════════
# HTML GENERATOR (reused from generate_nudge_pages.py)
# ═══════════════════════════════════════════════════════════

def e(text):
    return h.escape(text).replace('"', '&quot;')

SM_META = {
    "vip": {"id": "sm-vip", "icon": "\U0001F451", "label": "SM-NUDGE-VIP", "css": "vip", "color": "#bc8cff",
            "badge": "Whale + Shark", "desc": "GFE warm \u2014 Misses him, thinks about him, he's special."},
    "mid": {"id": "sm-mid", "icon": "\U0001F48E", "label": "SM-NUDGE-MID", "css": "mid", "color": "#58a6ff",
            "badge": "Shrimp + Low Spenders", "desc": "Flirty tease + curiosity \u2014 \"Something could happen right now.\""},
    "low": {"id": "sm-low", "icon": "\u26A1", "label": "SM-NUDGE-LOW", "css": "low", "color": "#d29922",
            "badge": "Rats", "desc": "Direct hooks, no fluff \u2014 Strong curiosity to pull them into conversation."},
    "zero": {"id": "sm-zero", "icon": "\U0001F3AF", "label": "SM-NUDGE-ZERO", "css": "zero", "color": "#f85149",
             "badge": "$0 Fans", "desc": "Direct sale approach \u2014 Provocative tease + low-price offers. Needs content attached."},
}

def build_collection_html(idx, coll, sm_key, color):
    attach = coll.get("attach")
    tag = coll.get("tag", False)
    msgs = coll["msgs"]
    wait = coll.get("wait")
    n_msgs = len(msgs)
    collapsed = ' collapsed' if idx > 0 else ''
    type_label = f"{n_msgs} msg{'s' if n_msgs > 1 else ''}"
    if tag:
        type_label += " \u00b7 {{name}}"
    if attach == "free":
        type_style = "background:#3fb95015;color:#3fb950"
        type_label = "FREE TEASER" + (" \u00b7 {name}" if tag else "")
    elif attach == "ppv":
        type_style = "background:#f8514915;color:#f85149"
        type_label = "PPV $3-5" + (" \u00b7 {name}" if tag else "")
    else:
        type_style = f"background:{color}15;color:{color}"
    lines = []
    lines.append(f'<div class="collection{collapsed}" data-coll="{sm_key}-{idx+1}"><div class="coll-header"><span class="coll-num">{idx+1}</span><span class="coll-label">Collection {idx+1}</span><span class="coll-type" style="{type_style}">{type_label}</span><input type="checkbox" class="coll-check" title="Mark as done"><span class="coll-toggle">\u25BC</span></div><div class="coll-body">')
    for mi, msg in enumerate(msgs):
        label = f"Message {mi+1}"
        escaped = e(msg)
        copy_val = e(msg)
        lines.append(f'<div class="msg-row"><span class="msg-label">{label}</span><span class="msg-text">{escaped}</span><button class="cp" data-copy="{copy_val}"><span class="cp-icon">\U0001F4CB</span></button></div>')
        if mi == 0 and attach == "free":
            lines.append('<div class="attach-row attach-free">\U0001F4CE Attach: <strong>Free teaser photo</strong> (Message price: $0.00)</div>')
        elif mi == 0 and attach == "ppv" and (n_msgs == 1 or not wait):
            lines.append('<div class="attach-row attach-ppv">\U0001F4CE Attach: <strong>PPV content</strong> (Message price: $3-5)</div>')
        if mi == 0 and wait and n_msgs > 1:
            lines.append(f'<div class="wait-row"><span class="wait-icon">\u23F1\uFE0F</span> Wait: 0 min {wait} sec</div>')
        if mi == 1 and attach == "ppv" and wait:
            lines.append('<div class="attach-row attach-ppv">\U0001F4CE Attach on Message 2: <strong>PPV content</strong> (Message price: $3-5)</div>')
        elif mi == 1 and attach == "free" and wait:
            lines.append('<div class="attach-row attach-free">\U0001F4CE Attach on Message 2: <strong>Free teaser photo</strong> (Message price: $0.00)</div>')
    lines.append('</div></div>')
    return '\n'.join(lines)

def build_sm_section(model, sm_key):
    meta = SM_META[sm_key]
    sm = model[sm_key]
    include = sm["include"]
    delay = sm["delay"]
    recent = sm["recent"]
    exclude_lists = sm.get("exclude_lists", "")
    colls_html = []
    for i, coll in enumerate(sm["collections"]):
        colls_html.append(build_collection_html(i, coll, sm_key, meta["color"]))
    exclude_lists_row = ""
    if exclude_lists:
        exclude_lists_row = f'<tr><td>Exclude lists</td><td><strong>{e(exclude_lists)}</strong></td></tr>'
    config_note = ""
    if sm_key == "zero":
        config_note = '<div class="config-note">\u26A0\uFE0F <strong>Content required:</strong> Collections marked FREE TEASER need a free photo attached. Collections marked PPV need content priced at $3-5. Do NOT create this Smart Message until content is ready.</div>'
    delay_parts = delay.split(" ~ ")
    return f'''
<div class="sm-section" id="{meta['id']}" style="--sm-color:var(--{meta['css']})">
  <div class="sm-header" data-sm="{sm_key}">
    <span class="toggle">\u25BC</span>
    <h2>{meta['icon']} {meta['label']} <span class="sm-badge" style="background:{meta['color']}20;color:var(--{meta['css']})">{meta['badge']}</span></h2>
    <div class="sm-desc">{meta['desc']} 10 collections.</div>
  </div>
  <div class="sm-body">
    <table class="config-table">
      <tr><td>Trigger</td><td>Fan comes online</td></tr>
      <tr><td>Include</td><td><strong>{e(include)}</strong></td></tr>
      {exclude_lists_row}
      <tr><td>Exclude \u2192 Sent messages recently</td><td><span class="check">\u2713</span> 0 days, {recent} hours</td></tr>
      <tr><td>Exclude \u2192 Fans with unread messages</td><td><span class="check">\u2713</span> On</td></tr>
      <tr><td>Exclude \u2192 Creators</td><td><span class="check">\u2713</span> On</td></tr>
      <tr><td>Action</td><td>After delay, <strong>{delay_parts[0].strip()}</strong> ~ <strong>{delay_parts[1].strip()}</strong> minutes</td></tr>
      <tr><td>Frequency</td><td>Send every time fan matches trigger</td></tr>
      <tr><td>Effective / Expiry</td><td>Immediately / Never</td></tr>
      <tr><td>Auto-unsend \u2192 Unsend messages</td><td>OFF</td></tr>
      <tr><td>Auto-unsend \u2192 Stop message sequence</td><td><span class="check">\u2713</span> ON</td></tr>
    </table>
    {config_note}
    {''.join(colls_html)}
  </div>
</div>
'''

def generate_page(model):
    name = model["name"]
    tagline = model["tagline"]
    photo = model["photo"]
    sections = ""
    for key in ["vip", "mid", "low", "zero"]:
        sections += build_sm_section(model, key)
    # Same CSS/JS as Batch 1 pages
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(name)} \u2014 Smart Messages Setup Guide</title>
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{--bg:#0d1117;--card:#161b22;--border:#30363d;--text:#e6edf3;--muted:#8b949e;--accent:#58a6ff;--green:#3fb950;--red:#f85149;--orange:#d29922;--purple:#bc8cff;--yellow:#e3b341;--vip:#bc8cff;--mid:#58a6ff;--low:#d29922;--zero:#f85149}}
html{{scroll-behavior:smooth}}
body{{background:var(--bg);color:var(--text);font-family:"Segoe UI",system-ui,sans-serif;line-height:1.6;padding:0 0 60px}}
.page{{max-width:960px;margin:0 auto;padding:16px 20px}}
.back-btn{{display:inline-flex;align-items:center;gap:6px;color:var(--muted);text-decoration:none;font-size:.85rem;padding:10px 0;transition:.15s}}
.back-btn:hover{{color:var(--accent)}}
.hero{{display:flex;align-items:center;gap:18px;padding:20px 0 16px;border-bottom:1px solid var(--border)}}
.hero-photo{{width:72px;height:72px;border-radius:50%;object-fit:cover;border:3px solid var(--accent);flex-shrink:0}}
.hero-info{{flex:1}}.hero h1{{font-size:1.8rem;font-weight:800;letter-spacing:2px;line-height:1.2}}
.hero .tagline{{color:var(--muted);font-size:.85rem}}
.toc{{position:sticky;top:0;z-index:50;background:var(--bg);border-bottom:1px solid var(--border);padding:8px 0;margin:0 -20px;padding-left:20px;padding-right:20px;display:flex;gap:6px;overflow-x:auto}}
.toc.shadow{{box-shadow:0 4px 16px rgba(0,0,0,.4)}}
.toc a{{font-size:.75rem;color:var(--muted);background:var(--card);border:1px solid var(--border);padding:5px 12px;border-radius:14px;text-decoration:none;white-space:nowrap;transition:.15s;flex-shrink:0}}
.toc a:hover,.toc a.active{{color:var(--accent);border-color:var(--accent)}}
.toc a.toc-vip{{color:var(--vip);border-color:#bc8cff33}}
.toc a.toc-mid{{color:var(--mid);border-color:#58a6ff33}}
.toc a.toc-low{{color:var(--low);border-color:#d2992233}}
.toc a.toc-zero{{color:var(--zero);border-color:#f8514933}}
.intro-box{{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:16px 20px;margin:16px 0;font-size:.88rem;line-height:1.7}}
.intro-box h2{{font-size:1rem;margin-bottom:8px}}
.intro-box ol{{padding-left:20px;margin:8px 0}}
.intro-box li{{margin:4px 0}}
.sm-section{{margin:24px 0 0;border:2px solid var(--sm-color,var(--border));border-radius:14px;overflow:hidden}}
.sm-header{{padding:16px 20px;background:var(--card);border-bottom:1px solid var(--border);cursor:pointer;user-select:none}}
.sm-header:hover{{background:#1c2129}}
.sm-header h2{{font-size:1.1rem;font-weight:700;display:flex;align-items:center;gap:10px}}
.sm-header .sm-badge{{font-size:.7rem;padding:3px 10px;border-radius:10px;font-weight:600}}
.sm-header .sm-desc{{font-size:.82rem;color:var(--muted);margin-top:4px}}
.sm-header .toggle{{color:var(--muted);font-size:.8rem;float:right;margin-top:4px;transition:transform .2s}}
.sm-section.collapsed .toggle{{transform:rotate(-90deg)}}
.sm-section.collapsed .sm-body{{display:none}}
.sm-body{{padding:0}}
.config-table{{width:100%;border-collapse:collapse;font-size:.84rem}}
.config-table td{{padding:8px 20px;border-bottom:1px solid #21262d}}
.config-table td:first-child{{color:var(--muted);width:260px;font-weight:600;font-size:.78rem;text-transform:uppercase;letter-spacing:.5px}}
.config-table .check{{color:var(--green)}}
.config-note{{padding:10px 20px;font-size:.82rem;background:#e3b34108;border-bottom:1px solid #21262d;color:var(--yellow)}}
.collection{{border-top:1px solid var(--border)}}
.coll-header{{display:flex;align-items:center;gap:10px;padding:10px 20px;cursor:pointer;user-select:none;background:var(--card)}}
.coll-header:hover{{background:#1c2129}}
.coll-num{{font-size:.72rem;font-weight:700;padding:3px 10px;border-radius:8px;border:1px solid var(--border);color:var(--muted);min-width:30px;text-align:center}}
.coll-label{{font-size:.88rem;font-weight:600;flex:1}}
.coll-type{{font-size:.68rem;padding:2px 8px;border-radius:8px;font-weight:600}}
.coll-toggle{{color:var(--muted);font-size:.75rem;transition:transform .2s}}
.collection.collapsed .coll-toggle{{transform:rotate(-90deg)}}
.collection.collapsed .coll-body{{display:none}}
.coll-body{{padding:8px 20px 14px}}
.msg-row{{display:flex;align-items:flex-start;gap:10px;margin:6px 0;padding:8px 12px;border-radius:8px;background:var(--bg);border:1px solid #21262d}}
.msg-row:hover{{border-color:var(--border)}}
.msg-label{{font-size:.7rem;font-weight:700;color:var(--muted);padding:4px 8px;background:var(--card);border-radius:6px;white-space:nowrap;min-width:68px;text-align:center;flex-shrink:0}}
.msg-text{{flex:1;font-size:1rem;line-height:1.5;padding:2px 0;word-wrap:break-word}}
.cp{{background:none;border:1px solid transparent;color:var(--border);width:32px;height:32px;border-radius:6px;cursor:pointer;font-size:.8rem;flex-shrink:0;display:flex;align-items:center;justify-content:center;transition:.15s;position:relative;opacity:.3}}
.msg-row:hover .cp{{opacity:1;border-color:var(--border)}}
.cp:hover{{background:var(--card);color:var(--text);opacity:1}}
.cp.ok{{border-color:var(--green);color:var(--green);opacity:1}}
.cp.ok::after{{content:"\\2713";position:absolute;font-size:.75rem;font-weight:700}}
.cp.ok .cp-icon{{visibility:hidden}}
.wait-row{{display:flex;align-items:center;gap:8px;padding:4px 12px;font-size:.78rem;color:var(--orange)}}
.attach-row{{display:flex;align-items:center;gap:8px;padding:6px 12px;margin:4px 0;font-size:.82rem;border-radius:8px}}
.attach-free{{background:#3fb95010;border:1px solid #3fb95028;color:var(--green)}}
.attach-ppv{{background:#f8514910;border:1px solid #f8514928;color:var(--red)}}
.top-btn{{position:fixed;bottom:16px;right:16px;width:36px;height:36px;border-radius:50%;background:var(--card);border:1px solid var(--border);color:var(--muted);font-size:1rem;cursor:pointer;display:none;align-items:center;justify-content:center;z-index:100;transition:.15s}}
.top-btn:hover{{color:var(--text);border-color:var(--muted)}}.top-btn.show{{display:flex}}
.progress{{padding:12px 20px;background:var(--card);border:1px solid var(--border);border-radius:12px;margin:16px 0;font-size:.84rem}}
.progress h3{{font-size:.88rem;margin-bottom:8px}}
.progress-bar{{height:6px;background:var(--border);border-radius:3px;overflow:hidden;margin:6px 0}}
.progress-fill{{height:100%;background:var(--green);border-radius:3px;transition:width .3s}}
.progress-text{{font-size:.75rem;color:var(--muted)}}
@media(max-width:700px){{.page{{padding:12px 10px}}.toc{{margin:0 -10px;padding-left:10px;padding-right:10px}}.config-table td:first-child{{width:140px}}}}
</style>
</head>
<body>
<div class="page">
<a href="./" class="back-btn">\u2190 {e(name)} Chatter Guide</a>
<div class="hero" id="top">
  <img src="{photo}" alt="{e(name)}" class="hero-photo">
  <div class="hero-info">
    <h1>{e(name).upper()} \u2014 Smart Messages</h1>
    <div class="tagline">Nudge Setup Guide \u00b7 Fan Comes Online</div>
  </div>
</div>
<nav class="toc" id="toc">
  <a href="#sm-vip" class="toc-vip">\U0001F451 VIP</a>
  <a href="#sm-mid" class="toc-mid">\U0001F48E MID</a>
  <a href="#sm-low" class="toc-low">\u26A1 LOW</a>
  <a href="#sm-zero" class="toc-zero">\U0001F3AF ZERO</a>
</nav>
<div class="intro-box">
  <h2>\U0001F4CB How to use this guide</h2>
  <ol>
    <li>Open <strong>Infloww</strong> in another tab</li>
    <li>Go to <strong>Smart Messages \u2192 New</strong></li>
    <li>Create each Smart Message below (VIP, MID, LOW, ZERO) one by one</li>
    <li>For each one: set the <strong>Configuration</strong> exactly as shown, then create each <strong>Collection</strong> and copy-paste the messages</li>
    <li>Use the <strong>\U0001F4CB copy button</strong> next to each message to copy it instantly</li>
    <li>Start with VIP, MID, and LOW. <strong>ZERO needs content attached</strong> \u2014 skip it until content is ready.</li>
  </ol>
</div>
<div class="progress" id="progress-box">
  <h3>Setup Progress</h3>
  <div class="progress-bar"><div class="progress-fill" id="progress-fill" style="width:0%"></div></div>
  <div class="progress-text" id="progress-text">0 of 40 collections done</div>
</div>
{sections}
<hr style="border:none;border-top:1px solid var(--border);margin:24px 0">
<div style="text-align:center;padding:24px 0 10px;color:var(--muted);font-size:.73rem">Chatting Wizard \u00b7 Script Manager \u00b7 2026</div>
</div>
<button class="top-btn" id="top-btn">\u2191</button>
<script>
document.addEventListener('click',e=>{{const b=e.target.closest('.cp');if(b){{navigator.clipboard.writeText(b.dataset.copy).then(()=>{{b.classList.add('ok');setTimeout(()=>b.classList.remove('ok'),1200)}});return}}}});
document.querySelectorAll('.coll-header').forEach(h=>{{h.addEventListener('click',e=>{{if(e.target.closest('.cp')||e.target.type==='checkbox')return;h.closest('.collection').classList.toggle('collapsed')}})}});
document.querySelectorAll('.sm-header').forEach(h=>{{h.addEventListener('click',()=>h.closest('.sm-section').classList.toggle('collapsed'))}});
const toc=document.getElementById('toc');
window.addEventListener('scroll',()=>toc.classList.toggle('shadow',window.scrollY>200));
const tocLinks=document.querySelectorAll('.toc a[href^="#"]');
tocLinks.forEach(a=>{{a.addEventListener('click',()=>{{const t=document.getElementById(a.getAttribute('href').slice(1));if(t)t.classList.remove('collapsed')}});}});
const sections=Array.from(tocLinks).map(a=>({{link:a,el:document.getElementById(a.getAttribute('href').slice(1))}})).filter(s=>s.el);
function updateToc(){{let a=sections[0];for(const s of sections)if(s.el.getBoundingClientRect().top<=100)a=s;tocLinks.forEach(l=>l.classList.remove('active'));if(a)a.link.classList.add('active')}}
window.addEventListener('scroll',updateToc);updateToc();
const topBtn=document.getElementById('top-btn');
window.addEventListener('scroll',()=>topBtn.classList.toggle('show',window.scrollY>400));
topBtn.addEventListener('click',()=>window.scrollTo({{top:0,behavior:'smooth'}}));
const checks=document.querySelectorAll('.coll-check');
const pFill=document.getElementById('progress-fill');
const pText=document.getElementById('progress-text');
function updateProgress(){{const done=document.querySelectorAll('.coll-check:checked').length;const total=checks.length;const pct=Math.round(done/total*100);pFill.style.width=pct+'%';pText.textContent=done+' of '+total+' collections done'+(pct===100?' \\u2705':'')}}
checks.forEach(c=>c.addEventListener('change',updateProgress));
updateProgress();
</script>
</body>
</html>'''


# ═══════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("SMART MESSAGES GENERATOR - ALL MODELS")
    print("=" * 60)

    total_issues = 0
    total_messages = 0
    generated = []

    for profile in ALL_PROFILES:
        name = profile["name"]
        print(f"\n--- {name} ({profile['gender']}) ---")

        # Build model data
        model_data = build_model_data(profile)

        # QA check
        issues, msg_count = qa_check(profile, model_data)
        total_messages += msg_count

        if issues:
            total_issues += len(issues)
            print(f"  QA ISSUES ({len(issues)}):")
            for issue in issues:
                print(issue)
        else:
            print(f"  QA: PASS ({msg_count} messages)")

        # Generate HTML
        html_content = generate_page(model_data)
        folder = os.path.join(ROOT, profile["folder"])
        os.makedirs(folder, exist_ok=True)
        out = os.path.join(folder, "smart-messages.html")
        with open(out, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"  HTML: {out}")
        generated.append(name)

    print("\n" + "=" * 60)
    print(f"SUMMARY")
    print(f"  Models generated: {len(generated)}")
    print(f"  Total messages: {total_messages}")
    print(f"  QA issues: {total_issues}")
    print("=" * 60)

    if total_issues > 0:
        print("\n[WARNING] Fix QA issues before deploying!")
    else:
        print("\n[OK] All models passed QA. Ready to deploy.")
