"""
Generate Smart Messages HTML pages for models.
Usage: python generate_nudge_pages.py
Generates smart-messages.html for each model defined below.
"""
import os, html as h

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ══════════════════════════════════════════════════════════════
# MODEL NUDGE DATA
# ══════════════════════════════════════════════════════════════

MODELS = [
{
  "name": "Lia", "folder": "lia", "photo": "profile.jpeg",
  "tagline": "22 · Fukuoka, Japan · Student / Artist",
  "vip": {
    "include": "Whale, Shark", "delay": "2 ~ 5", "recent": "6",
    "collections": [
      {"msgs": ["hii 🌸", "I was just thinking about you"], "wait": 15},
      {"msgs": ["hmm guess who just came on 💕", "perfect timing... I just finished drawing and I'm all relaxed in bed"], "wait": 15},
      {"msgs": ["I missed you 🌸"]},
      {"msgs": ["hey ✨", "I'm so bored rn... come talk to me?"], "wait": 20},
      {"msgs": ["there you are 💕 I was waiting for you"]},
      {"msgs": ["{name} 🌸", "I was hoping you'd come on today"], "wait": 15, "tag": True},
      {"msgs": ["omg perfect timing... I need to tell you something 😊"]},
      {"msgs": ["guess what I'm doing rn 💕", "hmm actually... maybe I shouldn't say 🌸"], "wait": 20},
      {"msgs": ["hey love 🌸 you always show up at the right time"]},
      {"msgs": ["you ✨", "I literally just thought \"I wish {name} was on\" and here you are"], "wait": 15, "tag": True},
    ]
  },
  "mid": {
    "include": "Shrimp, Low Spenders", "delay": "2 ~ 5", "recent": "6",
    "collections": [
      {"msgs": ["hey 💕", "I'm in a mood rn and you popped up at the worst time"], "wait": 15},
      {"msgs": ["omg I have something to show you 🌸"]},
      {"msgs": ["hii {name} 💕", "I was just thinking about last time we talked..."], "wait": 15, "tag": True},
      {"msgs": ["well well... look who's here ✨"]},
      {"msgs": ["ugh I'm so bored 😊", "talk to me? I need a distraction from studying"], "wait": 20},
      {"msgs": ["hey you 🌸", "I just did something kinda different... wanna see?"], "wait": 15},
      {"msgs": ["I was literally about to text you 💕"]},
      {"msgs": ["hmm hi 💕", "I'm lying in bed and I can't stop thinking about something"], "wait": 15},
      {"msgs": ["hey babe you caught me at a nice time 😊"]},
      {"msgs": ["wait {name}", "I've been saving something for you and I can't wait anymore 🌸"], "wait": 10, "tag": True},
    ]
  },
  "low": {
    "include": "Rats", "delay": "1 ~ 3", "recent": "6",
    "collections": [
      {"msgs": ["hey ✨", "I have something I think you'll like"], "wait": 15},
      {"msgs": ["omg you're on! I need to show you this 🌸"]},
      {"msgs": ["hi {name} 💕", "you came at the right time... I'm feeling generous today ✨"], "wait": 15, "tag": True},
      {"msgs": ["I can't keep this to myself anymore 🌸"]},
      {"msgs": ["pssst", "I have a surprise for you ✨"], "wait": 10},
      {"msgs": ["hey babe 💕", "I just made something that I think only you would appreciate 🌸"], "wait": 15},
      {"msgs": ["I'm only going to be in this mood for a little bit... come talk to me 💕"]},
      {"msgs": ["you 💕", "I was thinking about you earlier and got a little carried away... 🌸"], "wait": 15},
      {"msgs": ["finally! I've been waiting for someone nice to come on 😊"]},
      {"msgs": ["wait {name}", "there's something I've been wanting to ask you 🌸"], "wait": 10, "tag": True},
    ]
  },
  "zero": {
    "include": "Fans", "exclude_lists": "Whale, Shark, Shrimp, Low Spenders, Rats",
    "delay": "2 ~ 5", "recent": "12",
    "collections": [
      {"msgs": ["I'm feeling generous today 💕", "there's more where that came from... 🌸"], "wait": 15, "attach": "free"},
      {"msgs": ["I just made something really special and I'm sharing it with a few people at a special price ✨"], "attach": "ppv"},
      {"msgs": ["I'm bored and I just did something a little naughty 🌸", "wanna see? I'll make it worth it 💕"], "wait": 15},
      {"msgs": ["{name}... I think you need to see this ✨"], "tag": True, "attach": "free"},
      {"msgs": ["ok I never do this but... 🌸", "I'm sharing my best stuff at a special price rn ✨"], "wait": 10, "attach": "ppv"},
      {"msgs": ["this is what I'm wearing rn... or not wearing 💕"], "attach": "free"},
      {"msgs": ["I wonder if you can handle what I just made ✨", "prove me wrong... it's barely anything 🌸"], "wait": 15, "attach": "ppv"},
      {"msgs": ["hey {name} a little preview just for you 💕 if you want the full thing just say the word 🌸"], "tag": True, "attach": "free"},
      {"msgs": ["I just took this and idk if I should share it 🌸", "you know what... here, it's yours ✨"], "wait": 15, "attach": "free"},
      {"msgs": ["{name} I'm doing something special today... my best stuff at the lowest price ever ✨"], "tag": True, "attach": "ppv"},
    ]
  },
},
{
  "name": "Fernanda", "folder": "fernanda", "photo": "profile.jpeg",
  "tagline": "46 · Brazil · Former Miss Brazil / Psychology",
  "vip": {
    "include": "Whale, Shark", "delay": "2 ~ 5", "recent": "6",
    "collections": [
      {"msgs": ["hey handsome 😊", "I was just thinking about you"], "wait": 15},
      {"msgs": ["mmm look who's here 😏", "perfect timing... I just got back from the gym and I'm all relaxed"], "wait": 15},
      {"msgs": ["finally you're on... I missed talking to you"]},
      {"msgs": ["hey amor 😊", "just got home and I'm bored... save me?"], "wait": 20},
      {"msgs": ["there you are 😏 I was waiting for you"]},
      {"msgs": ["{name} 😊", "I was hoping you'd come on today"], "wait": 15, "tag": True},
      {"msgs": ["perfect timing... I need to tell you something"]},
      {"msgs": ["guess what I'm doing rn 😏", "hmm actually... maybe I shouldn't say"], "wait": 20},
      {"msgs": ["hey babe, you always show up at the right time 😊"]},
      {"msgs": ["you 😏", "I literally just thought \"I wish {name} was here\" and look who shows up"], "wait": 15, "tag": True},
    ]
  },
  "mid": {
    "include": "Shrimp, Low Spenders", "delay": "2 ~ 5", "recent": "6",
    "collections": [
      {"msgs": ["hey 😏", "I'm in a mood rn and you showed up at the worst time"], "wait": 15},
      {"msgs": ["I have something to show you... you're going to like this 😏"]},
      {"msgs": ["hey {name} 😊", "I was just thinking about last time we talked..."], "wait": 15, "tag": True},
      {"msgs": ["well well well... look who showed up 😏"]},
      {"msgs": ["ugh I'm so bored", "talk to me? I need a distraction from my thesis 😊"], "wait": 20},
      {"msgs": ["hey handsome 🔥", "I just did something kinda bold... wanna see?"], "wait": 15},
      {"msgs": ["I was literally about to text you 😊"]},
      {"msgs": ["mmm hi 😏", "I'm lying in bed and I can't stop thinking about something"], "wait": 15},
      {"msgs": ["hey babe you caught me at a good time 😊"]},
      {"msgs": ["wait {name}", "I've been saving something for you and I can't wait anymore 😏"], "wait": 10, "tag": True},
    ]
  },
  "low": {
    "include": "Rats", "delay": "1 ~ 3", "recent": "6",
    "collections": [
      {"msgs": ["hey 😏", "I have something I think you'll like"], "wait": 15},
      {"msgs": ["you're on! I need to show you something"]},
      {"msgs": ["hi {name} 🔥", "you came at the right time... I'm feeling generous today 😏"], "wait": 15, "tag": True},
      {"msgs": ["I can't keep this to myself anymore"]},
      {"msgs": ["pssst", "I have a surprise for you 😏"], "wait": 10},
      {"msgs": ["hey babe 😊", "I just recorded something that I think only you would appreciate"], "wait": 15},
      {"msgs": ["I'm only going to be in this mood for a little bit... come talk to me 😏"]},
      {"msgs": ["you 😏", "I was thinking about you earlier and got a little carried away..."], "wait": 15},
      {"msgs": ["finally! I've been waiting for someone interesting to come on 😊"]},
      {"msgs": ["ok {name}", "there's something I've been wanting to ask you 😏"], "wait": 10, "tag": True},
    ]
  },
  "zero": {
    "include": "Fans", "exclude_lists": "Whale, Shark, Shrimp, Low Spenders, Rats",
    "delay": "2 ~ 5", "recent": "12",
    "collections": [
      {"msgs": ["I'm feeling generous today 😏", "there's more where that came from..."], "wait": 15, "attach": "free"},
      {"msgs": ["I just recorded something really hot and I'm sharing it with a few people at a special price 🔥 interested?"], "attach": "ppv"},
      {"msgs": ["I'm bored and I just did something naughty 😏", "wanna see? I'll make it worth it"], "wait": 15},
      {"msgs": ["{name}... I think you need to see this 😏"], "tag": True, "attach": "free"},
      {"msgs": ["ok I normally don't do this but...", "I'm sharing my best content at a crazy price rn 🔥"], "wait": 10, "attach": "ppv"},
      {"msgs": ["this is what I'm wearing rn... or should I say not wearing 😏"], "attach": "free"},
      {"msgs": ["I wonder if you can handle what I just recorded 😏", "prove me wrong... it's basically nothing"], "wait": 15, "attach": "ppv"},
      {"msgs": ["hey {name} a little preview just for you 🔥 if you want the full thing just say the word"], "tag": True, "attach": "free"},
      {"msgs": ["I just took this and I'm not sure I should share it 😏", "you know what... here, it's yours"], "wait": 15, "attach": "free"},
      {"msgs": ["{name} I'm doing something special today... my best content at the lowest price ever 🔥"], "tag": True, "attach": "ppv"},
    ]
  },
},
{
  "name": "Jasmine", "folder": "jasmine", "photo": "profile.jpeg",
  "tagline": "25 · Dominican Republic · Business Student / F1 Fan",
  "vip": {
    "include": "Whale, Shark", "delay": "2 ~ 5", "recent": "6",
    "collections": [
      {"msgs": ["hey you 😊", "I was literally just thinking about you"], "wait": 15},
      {"msgs": ["mmm look who's here 😏", "perfect timing... I just got home from the gym and I'm all comfy"], "wait": 15},
      {"msgs": ["finally you're on 😊 I missed you papi"]},
      {"msgs": ["hiii 😊", "I'm so bored rn... save me?"], "wait": 20},
      {"msgs": ["there you are 😏 been waiting for you"]},
      {"msgs": ["{name} 😊", "I was hoping you'd come on today"], "wait": 15, "tag": True},
      {"msgs": ["omg perfect timing... I need to tell you something"]},
      {"msgs": ["guess what I'm doing rn 😏", "actually... maybe I shouldn't say"], "wait": 20},
      {"msgs": ["hey papi 😊 you always show up at the right time"]},
      {"msgs": ["you 😏", "I literally just said out loud \"I wish {name} was on\" and here you are"], "wait": 15, "tag": True},
    ]
  },
  "mid": {
    "include": "Shrimp, Low Spenders", "delay": "2 ~ 5", "recent": "6",
    "collections": [
      {"msgs": ["hey 😏", "I'm in a mood rn and you popped up at the worst time"], "wait": 15},
      {"msgs": ["omg I have something to show you"]},
      {"msgs": ["hiii {name} 😊", "I was just thinking about last time we talked..."], "wait": 15, "tag": True},
      {"msgs": ["well well well... look who's here 😏"]},
      {"msgs": ["ugh I'm so bored", "talk to me? I need a distraction from studying 😊"], "wait": 20},
      {"msgs": ["hey handsome 🔥", "I just did something kinda crazy... wanna see?"], "wait": 15},
      {"msgs": ["I was literally about to text you 😊"]},
      {"msgs": ["mmm hi 😏", "I'm lying in bed and I can't stop thinking about something"], "wait": 15},
      {"msgs": ["hey papi you caught me at a fun time 😊"]},
      {"msgs": ["ok wait {name}", "I've been saving something for you and I literally can't wait anymore"], "wait": 10, "tag": True},
    ]
  },
  "low": {
    "include": "Rats", "delay": "1 ~ 3", "recent": "6",
    "collections": [
      {"msgs": ["hey 😏", "I have something I think you'll like"], "wait": 15},
      {"msgs": ["omg you're on! I need to show you this"]},
      {"msgs": ["hi {name} 🔥", "you came at the right time... I'm feeling generous today 😏"], "wait": 15, "tag": True},
      {"msgs": ["ok I can't keep this to myself anymore"]},
      {"msgs": ["pssst", "I have a surprise for you 😏"], "wait": 10},
      {"msgs": ["hey papi 😊", "I just recorded something that I think only you would appreciate"], "wait": 15},
      {"msgs": ["I'm only going to be in this mood for a little bit... come talk to me 😏"]},
      {"msgs": ["you 😏", "I was thinking about you earlier and got a little carried away..."], "wait": 15},
      {"msgs": ["finally! I've been waiting for someone fun to come on 😊"]},
      {"msgs": ["ok {name}", "there's something I've been wanting to ask you"], "wait": 10, "tag": True},
    ]
  },
  "zero": {
    "include": "Fans", "exclude_lists": "Whale, Shark, Shrimp, Low Spenders, Rats",
    "delay": "2 ~ 5", "recent": "12",
    "collections": [
      {"msgs": ["I'm feeling generous today 😏", "there's more where that came from..."], "wait": 15, "attach": "free"},
      {"msgs": ["I just recorded something really hot and I'm sending it to a few people at a special price 🔥 you in?"], "attach": "ppv"},
      {"msgs": ["I'm bored and I just did something naughty", "wanna see? I'll make it worth it 😏"], "wait": 15},
      {"msgs": ["{name}... I think you need to see this 😏"], "tag": True, "attach": "free"},
      {"msgs": ["ok I never do this but...", "I'm giving away my hottest stuff at a crazy price rn 🔥"], "wait": 10, "attach": "ppv"},
      {"msgs": ["this is what I'm wearing rn... or not wearing 😏"], "attach": "free"},
      {"msgs": ["I bet you can't handle what I just recorded 😏", "prove me wrong papi... it's basically nothing"], "wait": 15, "attach": "ppv"},
      {"msgs": ["hey {name} a little preview just for you 🔥 if you want the full thing just say the word"], "tag": True, "attach": "free"},
      {"msgs": ["I just took this and idk if I should share it", "you know what... here, it's yours 😏"], "wait": 15, "attach": "free"},
      {"msgs": ["{name} I'm doing something special today... my best stuff at the lowest price ever 🔥 don't miss it"], "tag": True, "attach": "ppv"},
    ]
  },
},
{
  "name": "Antonella", "folder": "antonella", "photo": "profile.jpeg",
  "tagline": "19 · Miami · Gamer / Cosplayer",
  "vip": {
    "include": "Whale, Shark", "delay": "2 ~ 5", "recent": "6",
    "collections": [
      {"msgs": ["hiiii 🖤", "I was literally just thinking about you"], "wait": 15},
      {"msgs": ["omg look who's here 💜", "perfect timing... I just got off Valorant and I'm all comfy in bed"], "wait": 15},
      {"msgs": ["finally you're on 🖤 I missed you"]},
      {"msgs": ["hiii ✨", "I'm so bored rn... save me?"], "wait": 20},
      {"msgs": ["there you are 💜 been waiting for you"]},
      {"msgs": ["{name} 🖤", "I was hoping you'd come on today"], "wait": 15, "tag": True},
      {"msgs": ["omggg perfect timing... I need to tell you something ✨"]},
      {"msgs": ["guess what I'm doing rn 😏", "hehe actually... maybe I shouldn't say 🖤"], "wait": 20},
      {"msgs": ["hey babe 🖤 you always show up at the right time"]},
      {"msgs": ["you ✨", "I literally just said out loud \"I wish {name} was on\" and here you are 🖤"], "wait": 15, "tag": True},
    ]
  },
  "mid": {
    "include": "Shrimp, Low Spenders", "delay": "2 ~ 5", "recent": "6",
    "collections": [
      {"msgs": ["hey 😏", "I'm in a mood rn and you popped up at the worst time"], "wait": 15},
      {"msgs": ["omg I have something to show you 🖤"]},
      {"msgs": ["hiiii {name} 💜", "I was just thinking about last time we talked..."], "wait": 15, "tag": True},
      {"msgs": ["well well well... look who's here 😏"]},
      {"msgs": ["ugh I'm so bored ✨", "talk to me? I need a distraction from this losing streak in Valo"], "wait": 20},
      {"msgs": ["hey you 🖤", "I just did something kinda crazy... wanna see? 💜"], "wait": 15},
      {"msgs": ["I was literally about to text you hehe"]},
      {"msgs": ["omg hi 😏", "I'm lying in bed and I can't stop thinking about something"], "wait": 15},
      {"msgs": ["hey babe you caught me at a fun time ✨"]},
      {"msgs": ["ok wait {name}", "I've been saving something for you and I literally can't wait anymore 🖤"], "wait": 10, "tag": True},
    ]
  },
  "low": {
    "include": "Rats", "delay": "1 ~ 3", "recent": "6",
    "collections": [
      {"msgs": ["hey 😏", "I have something I think you'll like"], "wait": 15},
      {"msgs": ["omg you're on! I need to show you this 🖤"]},
      {"msgs": ["hiii {name} 💜", "you came at the right time... I'm feeling generous today 😏"], "wait": 15, "tag": True},
      {"msgs": ["ok I can't keep this to myself anymore 🖤"]},
      {"msgs": ["pssst", "I have a surprise for you 😏"], "wait": 10},
      {"msgs": ["hey babe 🖤", "I just made something that I think only you would appreciate 💜"], "wait": 15},
      {"msgs": ["I'm only going to be in this mood for a little bit... come talk to me 😏"]},
      {"msgs": ["you 😏", "I was thinking about you earlier and got a little carried away... 🖤"], "wait": 15},
      {"msgs": ["finally! I've been waiting for someone fun to come on ✨"]},
      {"msgs": ["ok {name}", "there's something I've been wanting to ask you 🖤"], "wait": 10, "tag": True},
    ]
  },
  "zero": {
    "include": "Fans", "exclude_lists": "Whale, Shark, Shrimp, Low Spenders, Rats",
    "delay": "2 ~ 5", "recent": "12",
    "collections": [
      {"msgs": ["I'm feeling generous today 😏", "there's more where that came from... 🖤"], "wait": 15, "attach": "free"},
      {"msgs": ["I just made something really hot and I'm sending it to a few people at a special price 🖤 you in?"], "attach": "ppv"},
      {"msgs": ["I'm bored and I just did something naughty 💜", "wanna see? I'll make it worth it 😏"], "wait": 15},
      {"msgs": ["{name}... I think you need to see this 😏"], "tag": True, "attach": "free"},
      {"msgs": ["ok I never do this but... 🖤", "I'm giving away my hottest stuff at a crazy price rn 💜"], "wait": 10, "attach": "ppv"},
      {"msgs": ["this is what I'm wearing rn... or not wearing 😏"], "attach": "free"},
      {"msgs": ["I bet you can't handle what I just made 😏", "prove me wrong... it's basically nothing 🖤"], "wait": 15, "attach": "ppv"},
      {"msgs": ["hey {name} a little preview just for you 💜 if you want the full thing just say the word 🖤"], "tag": True, "attach": "free"},
      {"msgs": ["I just took this and idk if I should share it 🖤", "you know what... here, it's yours 😏"], "wait": 15, "attach": "free"},
      {"msgs": ["{name} I'm doing something special today... my best stuff at the lowest price ever 🖤 don't miss it"], "tag": True, "attach": "ppv"},
    ]
  },
},
]

# ══════════════════════════════════════════════════════════════
# SM METADATA
# ══════════════════════════════════════════════════════════════
SM_META = {
  "vip": {"id": "sm-vip", "icon": "👑", "label": "SM-NUDGE-VIP", "css": "vip", "color": "#bc8cff",
          "badge": "Whale + Shark", "desc": "GFE warm \u2014 She misses him, she thinks about him, he's special."},
  "mid": {"id": "sm-mid", "icon": "💎", "label": "SM-NUDGE-MID", "css": "mid", "color": "#58a6ff",
          "badge": "Shrimp + Low Spenders", "desc": "Flirty tease + curiosity \u2014 \"Something could happen right now.\""},
  "low": {"id": "sm-low", "icon": "⚡", "label": "SM-NUDGE-LOW", "css": "low", "color": "#d29922",
          "badge": "Rats", "desc": "Direct hooks, no fluff \u2014 Strong curiosity to pull them into conversation."},
  "zero": {"id": "sm-zero", "icon": "🎯", "label": "SM-NUDGE-ZERO", "css": "zero", "color": "#f85149",
           "badge": "$0 Fans", "desc": "Direct sale approach \u2014 Provocative tease + low-price offers. Needs content attached."},
}

# ══════════════════════════════════════════════════════════════
# HTML GENERATOR
# ══════════════════════════════════════════════════════════════
def e(text):
    return h.escape(text).replace('"', '&quot;')

def build_collection_html(idx, coll, sm_key, color):
    attach = coll.get("attach")
    tag = coll.get("tag", False)
    msgs = coll["msgs"]
    wait = coll.get("wait")
    n_msgs = len(msgs)
    collapsed = ' collapsed' if idx > 0 else ''

    type_label = f"{n_msgs} msg{'s' if n_msgs > 1 else ''}"
    if tag: type_label += " · {name}"

    # Determine attach badge
    if attach == "free":
        type_style = "background:#3fb95015;color:#3fb950"
        type_label = "FREE TEASER" + (" · {name}" if tag else "")
    elif attach == "ppv":
        type_style = "background:#f8514915;color:#f85149"
        type_label = "PPV $3-5" + (" · {name}" if tag else "")
    else:
        type_style = f"background:{color}15;color:{color}"

    lines = []
    lines.append(f'<div class="collection{collapsed}" data-coll="{sm_key}-{idx+1}"><div class="coll-header"><span class="coll-num">{idx+1}</span><span class="coll-label">Collection {idx+1}</span><span class="coll-type" style="{type_style}">{type_label}</span><input type="checkbox" class="coll-check" title="Mark as done"><span class="coll-toggle">▼</span></div><div class="coll-body">')

    for mi, msg in enumerate(msgs):
        label = f"Message {mi+1}"
        escaped = e(msg)
        copy_val = e(msg)
        lines.append(f'<div class="msg-row"><span class="msg-label">{label}</span><span class="msg-text">{escaped}</span><button class="cp" data-copy="{copy_val}"><span class="cp-icon">📋</span></button></div>')
        # Attach indicator after message
        if mi == 0 and attach == "free" and n_msgs == 1:
            lines.append('<div class="attach-row attach-free">📎 Attach: <strong>Free teaser photo</strong> (Message price: $0.00)</div>')
        elif mi == 0 and attach == "ppv" and n_msgs == 1:
            lines.append('<div class="attach-row attach-ppv">📎 Attach: <strong>PPV content</strong> (Message price: $3-5)</div>')
        elif mi == 0 and attach == "free" and n_msgs > 1:
            lines.append('<div class="attach-row attach-free">📎 Attach: <strong>Free teaser photo</strong> (Message price: $0.00)</div>')
        elif mi == 0 and attach == "ppv" and n_msgs > 1 and not wait:
            lines.append('<div class="attach-row attach-ppv">📎 Attach: <strong>PPV content</strong> (Message price: $3-5)</div>')

        # Wait indicator between messages
        if mi == 0 and wait and n_msgs > 1:
            lines.append(f'<div class="wait-row"><span class="wait-icon">⏱️</span> Wait: 0 min {wait} sec</div>')

        # Attach on message 2 for PPV
        if mi == 1 and attach == "ppv" and wait:
            lines.append('<div class="attach-row attach-ppv">📎 Attach on Message 2: <strong>PPV content</strong> (Message price: $3-5)</div>')
        elif mi == 1 and attach == "free" and wait:
            lines.append('<div class="attach-row attach-free">📎 Attach on Message 2: <strong>Free teaser photo</strong> (Message price: $0.00)</div>')

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
        config_note = '<div class="config-note">⚠️ <strong>Content required:</strong> Collections marked FREE TEASER need a free photo attached. Collections marked PPV need content priced at $3-5. Do NOT create this Smart Message until content is ready.</div>'

    delay_parts = delay.split(" ~ ")
    return f'''
<div class="sm-section" id="{meta['id']}" style="--sm-color:var(--{meta['css']})">
  <div class="sm-header" data-sm="{sm_key}">
    <span class="toggle">▼</span>
    <h2>{meta['icon']} {meta['label']} <span class="sm-badge" style="background:{meta['color']}20;color:var(--{meta['css']})">{meta['badge']}</span></h2>
    <div class="sm-desc">{meta['desc']} 10 collections.</div>
  </div>
  <div class="sm-body">
    <table class="config-table">
      <tr><td>Trigger</td><td>Fan comes online</td></tr>
      <tr><td>Include</td><td><strong>{e(include)}</strong></td></tr>
      {exclude_lists_row}
      <tr><td>Exclude → Sent messages recently</td><td><span class="check">✓</span> 0 days, {recent} hours</td></tr>
      <tr><td>Exclude → Fans with unread messages</td><td><span class="check">✓</span> On</td></tr>
      <tr><td>Exclude → Creators</td><td><span class="check">✓</span> On</td></tr>
      <tr><td>Action</td><td>After delay, <strong>{delay_parts[0].strip()}</strong> ~ <strong>{delay_parts[1].strip()}</strong> minutes</td></tr>
      <tr><td>Frequency</td><td>Send every time fan matches trigger</td></tr>
      <tr><td>Effective / Expiry</td><td>Immediately / Never</td></tr>
      <tr><td>Auto-unsend → Unsend messages</td><td>OFF</td></tr>
      <tr><td>Auto-unsend → Stop message sequence</td><td><span class="check">✓</span> ON</td></tr>
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

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(name)} — Smart Messages Setup Guide</title>
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
<a href="./" class="back-btn">← {e(name)} Chatter Guide</a>
<div class="hero" id="top">
  <img src="{photo}" alt="{e(name)}" class="hero-photo">
  <div class="hero-info">
    <h1>{e(name).upper()} — Smart Messages</h1>
    <div class="tagline">Nudge Setup Guide · Fan Comes Online</div>
  </div>
</div>
<nav class="toc" id="toc">
  <a href="#sm-vip" class="toc-vip">👑 VIP</a>
  <a href="#sm-mid" class="toc-mid">💎 MID</a>
  <a href="#sm-low" class="toc-low">⚡ LOW</a>
  <a href="#sm-zero" class="toc-zero">🎯 ZERO</a>
</nav>
<div class="intro-box">
  <h2>📋 How to use this guide</h2>
  <ol>
    <li>Open <strong>Infloww</strong> in another tab</li>
    <li>Go to <strong>Smart Messages → New</strong></li>
    <li>Create each Smart Message below (VIP, MID, LOW, ZERO) one by one</li>
    <li>For each one: set the <strong>Configuration</strong> exactly as shown, then create each <strong>Collection</strong> and copy-paste the messages</li>
    <li>Use the <strong>📋 copy button</strong> next to each message to copy it instantly</li>
    <li>Start with VIP, MID, and LOW. <strong>ZERO needs content attached</strong> — skip it until content is ready.</li>
  </ol>
</div>
<div class="progress" id="progress-box">
  <h3>Setup Progress</h3>
  <div class="progress-bar"><div class="progress-fill" id="progress-fill" style="width:0%"></div></div>
  <div class="progress-text" id="progress-text">0 of 40 collections done</div>
</div>
{sections}
<hr style="border:none;border-top:1px solid var(--border);margin:24px 0">
<div style="text-align:center;padding:24px 0 10px;color:var(--muted);font-size:.73rem">Chatting Wizard · Script Manager · 2026</div>
</div>
<button class="top-btn" id="top-btn">↑</button>
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
function updateProgress(){{const done=document.querySelectorAll('.coll-check:checked').length;const total=checks.length;const pct=Math.round(done/total*100);pFill.style.width=pct+'%';pText.textContent=done+' of '+total+' collections done'+(pct===100?' ✅':'')}}
checks.forEach(c=>c.addEventListener('change',updateProgress));
updateProgress();
</script>
</body>
</html>'''


# ══════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    for model in MODELS:
        folder = os.path.join(ROOT, model["folder"])
        os.makedirs(folder, exist_ok=True)
        out = os.path.join(folder, "smart-messages.html")
        html_content = generate_page(model)
        with open(out, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"[OK] Generated {out}")
    print(f"\nDone! {len(MODELS)} pages generated.")
