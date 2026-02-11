"""Generate max/objections.html from data — same structure as Putri but Max's voice."""

protocols = {
    # OBJ
    "price": {
        "name": '"Too expensive"',
        "desc": "He says the PPV price is too high. Use each step only if the previous one didn't convert.",
        "steps": 5, "cat": "obj",
        "seqs": {
            "price-1": [
                ("Reframe Value", "bro that's less than a protein shake and I promise this hits harder", None),
                ("FOMO Temporal", "I'm only feeling like this because of you rn, no idea when that's gonna happen again", None),
                ("Challenge", "maybe you're not ready for what I just did in this one", None),
                ("Downgrade (ONE TIME)", "alright look, [lower price] just for you because this convo has been different", "Reduce 20-30%. NEVER do this twice with the same fan."),
                ("Seed + Return", "it's cool man, let's just keep talking... I'm still thinking about you anyway", None),
            ],
            "price-2": [
                ("Reframe Value", "that's like what you'd spend on a coffee, except this is gonna keep you up way longer", None),
                ("FOMO Temporal", "this mood? it's not gonna last forever and I want you to be the one who sees it", None),
                ("Challenge", "honestly most guys can't handle what I just recorded, thought you were different", None),
                ("Downgrade (ONE TIME)", "you know what... [lower price] because you've been making me feel some type of way, keep that between us", "Reduce 20-30%. NEVER do this twice."),
                ("Seed + Return", "no stress, I like talking to you regardless", None),
            ],
        },
        "after": "After step 5: continue GFE. Retry with different content next session.",
    },
    "discount": {
        "name": '"Give me a discount"',
        "desc": "He wants to pay less but isn't refusing. He's negotiating — GOOD sign.",
        "steps": 4, "cat": "obj",
        "seqs": {
            "discount-1": [
                ("Playful Firmness", "haha you trying to negotiate with me? this isn't a negotiation man, it's worth every cent", None),
                ("Challenge Worthiness", "I don't do discounts... I only share this with guys who actually appreciate what they're getting", None),
                ("Concession (ONE TIME)", "alright... [lower price] just for you but don't tell anyone, this stays between us", "Reduce 20-30%. Only once."),
                ("Takeaway", "if you don't want it that's cool, I'll keep it for myself... or maybe someone else has been asking", None),
            ],
            "discount-2": [
                ("Playful Firmness", "a discount? do I look like I'm on sale?", None),
                ("Challenge Worthiness", "the guys who appreciate what I do don't ask for discounts, just saying", None),
                ("Concession (ONE TIME)", "fine... [lower price] but ONLY because I like you, one time thing", "Only once."),
                ("Takeaway", "alright I'll save it for someone who actually wants it then", None),
            ],
        },
    },
    "free": {
        "name": '"Send it for free"',
        "desc": "Entitlement, not price sensitivity. He already got PPV0 for free.",
        "steps": 4, "cat": "obj",
        "seqs": {
            "free-1": [
                ("Reminder + Tease", "I already sent you one for free remember? and this one is way crazier... you have no idea", None),
                ("Challenge", "free? nah I don't just give this to anyone... you gotta earn the good stuff", None),
                ("Guilt / Investment", "I literally just recorded this because of what YOU said to me, this wasn't just random content man", None),
                ("Seed + Return", "it's cool, I'm not going anywhere... let's just keep talking, I like this", None),
            ],
            "free-2": [
                ("Reminder + Tease", "you already got a free one, this one is on another level trust me", None),
                ("Challenge", "free? you think the best things in life are free? not this one", None),
                ("Guilt / Investment", "I did this because of you... like specifically because of our convo, that took effort and I did it for YOU", None),
                ("Seed + Return", "no pressure at all, I'm just enjoying talking to you honestly", None),
            ],
        },
    },
    "nomoney": {
        "name": '"I don\'t have money"',
        "desc": "Could be real or excuse. Test gently. If genuinely broke, protect relationship.",
        "steps": 4, "cat": "obj",
        "seqs": {
            "nomoney-1": [
                ("Empathy", "hey I totally get it, no pressure at all okay?", None),
                ("Test Sincerity", "not even like [small amount]? I really want you to see this one", "Suggest $3-5."),
                ("Pay What You Want", "just send whatever you can man... even a tiny amount, I just need you to see what you made me do", None),
                ("Protect Relationship", "honestly it's fine, I like talking to you money or not... you do something to me", None),
            ],
            "nomoney-2": [
                ("Empathy", "that's fine, seriously don't worry about it", None),
                ("Test Sincerity", "what about just [small amount]? I really don't want you to miss this", "Suggest $3-5."),
                ("Pay What You Want", "send whatever feels right, even $1... I just can't keep this from you", None),
                ("Protect Relationship", "it's totally cool, you being here is what matters", None),
            ],
        },
    },
    "noppv": {
        "name": '"I don\'t buy PPVs"',
        "desc": "Identity stance. Break the identity, not the price. After Step 1, continue 4-5 sexting msgs before Step 2.",
        "steps": 3, "cat": "obj",
        "seqs": {
            "noppv-1": [
                ("Accept (Disarm)", "that's totally fine I'm not trying to sell you anything, I just like talking to you", "After this: continue sexting 4-5 msgs from main script before Step 2."),
                ("Emotional Reframe", "look this isn't about money... I just need you to see what you're doing to me rn, I don't react like this to people", None),
                ("Pay What You Want", "just send whatever you want, even $1, I can't keep this to myself... you need to see it", None),
            ],
            "noppv-2": [
                ("Accept (Disarm)", "no worries at all, I don't care about that I'm just enjoying this", "After this: continue sexting 4-5 msgs before Step 2."),
                ("Emotional Reframe", "forget about money for a sec... I just want to share this with you, what you're making me feel is real", None),
                ("Pay What You Want", "send me anything, even the smallest amount, I need you to see what you did to me", None),
            ],
        },
    },
    "card": {
        "name": '"Card doesn\'t work"',
        "desc": "Tech issue. Keep it light, solve it, maintain momentum.",
        "steps": 3, "cat": "obj",
        "seqs": {
            "card-1": [
                ("Retry", "ahh that sucks, happens sometimes though try again it usually works the second time", None),
                ("Alternative Card", "try a different card? I really don't want you to miss this", None),
                ("Soft Urgency", "figure it out soon man, I'm in this mood rn and I don't know how long it's gonna last", None),
            ],
            "card-2": [
                ("Retry", "damn that's annoying, it happens a lot just try one more time", None),
                ("Alternative Card", "do you have another card you can try? I really want you to see this", None),
                ("Soft Urgency", "I want you to see this before I change my mind, I don't keep stuff like this around forever", None),
            ],
        },
    },
    # RES
    "nosex": {
        "name": "Doesn't want to go sexual",
        "desc": "NEVER force it. Respect, build tension subtly, try again later.",
        "steps": 4, "cat": "res",
        "seqs": {
            "nosex-1": [
                ("Respect", "haha alright alright I got a little carried away, you're just too easy to talk to", None),
                ("Subtle Tension", "so tell me more about you... what do you do when you're not making dudes on the internet lose their minds?", None),
                ("Natural Re-attempt", "look I can't help it, there's something about you that's messing with my head rn", None),
                ("Accept + GFE", "alright I'll chill... for now, no promises though haha", None),
            ],
            "nosex-2": [
                ("Respect", "my bad I got ahead of myself haha, it's your fault for being so fun to talk to", None),
                ("Subtle Tension", "okay new topic, but first... what's the most wild thing you've ever done?", None),
                ("Natural Re-attempt", "I'm trying to behave but you're making it really hard man, there's something about you", None),
                ("Accept + GFE", "fine I'll stop but don't blame me if it happens again later", None),
            ],
        },
    },
    "offtopic": {
        "name": "Goes off-topic",
        "desc": "Never dismiss. Acknowledge, then redirect back to your flow.",
        "steps": 3, "cat": "res",
        "seqs": {
            "offtopic-1": [
                ("Acknowledge", "haha wait that's actually funny", "Adapt to what he actually said."),
                ("Redirect", "but hold on you totally distracted me, I was about to tell you something and now I lost my train of thought...", None),
                ("Retake Control", "okay wait no I remember now, so like I was saying...", "Continue with next msg from main journey."),
            ],
            "offtopic-2": [
                ("Acknowledge", "lol okay that's random but I like it", "Adapt to his topic."),
                ("Redirect", "wait no stop you're distracting me from what I was gonna say...", None),
                ("Retake Control", "OKAY focus, where was I... oh yeah", "Resume main script."),
            ],
        },
    },
    "real": {
        "name": '"Are you real?"',
        "desc": "Questioning authenticity. Critical moment. Never get defensive.",
        "steps": 3, "cat": "res",
        "seqs": {
            "real-1": [
                ("Humor", "lol do I sound like a bot to you? beep boop... send $5 for human verification haha I'm kidding", None),
                ("Challenge", "ask me anything, literally anything about me my life whatever. I'm an open book", None),
                ("Emotional Grounding", "I get it there's a lot of fake stuff on here, but you felt something in this convo right? because I did... and that's real", None),
            ],
            "real-2": [
                ("Humor", "wait you think I'm fake?? that's actually the funniest thing anyone's said to me today", None),
                ("Challenge", "test me, ask me something only a real person would know. go ahead", None),
                ("Emotional Grounding", "I know there's a lot of bots on here but what we've been talking about... that felt real to me. didn't it feel real to you?", None),
            ],
        },
    },
    "voice": {
        "name": '"Voice note" / "Video call"',
        "desc": "Can't do voice/video. Dodge, redirect to content.",
        "steps": 3, "cat": "res",
        "seqs": {
            "voice-1": [
                ("Playful Dodge", "haha maybe one day if you earn it but not yet... I'm private about that stuff", None),
                ("Redirect", "I have something wayyy better for you though, trust me you'll forget you even asked", None),
                ("Firm Boundary", "I don't do that on here but what I'm about to show you is better than any call... you'll see", None),
            ],
            "voice-2": [
                ("Playful Dodge", "hmmm maybe but you gotta earn that first haha", None),
                ("Redirect", "how about instead of a call I show you something that'll blow your mind?", None),
                ("Firm Boundary", "that's not something I do on here but what I have for you is wayyy better than my voice, trust me", None),
            ],
        },
    },
    "customyes": {
        "name": "Asks for content model HAS",
        "desc": "SALE OPPORTUNITY. Tease, price, close.",
        "steps": 3, "cat": "res",
        "seqs": {
            "customyes-1": [
                ("Tease", "you want that? I might have something... actually I definitely have something", None),
                ("Price", "I have exactly what you're thinking of, you're gonna lose it... [price]", "Set price based on content. Premium for specific requests."),
                ("Close", "trust me you won't regret it, I made this one special", None),
            ],
            "customyes-2": [
                ("Tease", "oh you have good taste... I think I have exactly what you're looking for", None),
                ("Price", "I actually did something just like that, [price] and it's worth every cent", "Set price based on content."),
                ("Close", "you're not gonna be able to stop watching this one", None),
            ],
        },
    },
    "customno": {
        "name": "Asks for content model DOESN'T have",
        "desc": "NEVER say 'I don't have that.' Redirect to something better.",
        "steps": 3, "cat": "res",
        "seqs": {
            "customno-1": [
                ("Redirect", "I don't have exactly that but honestly I have something that'll make you forget you even asked", None),
                ("Alternative + FOMO", "actually what I have might be even crazier and literally no one else has seen it yet", None),
                ("Confidence Close", "trust me... I know what you need better than you do", None),
            ],
            "customno-2": [
                ("Redirect", "I don't have that specific thing but I have something you're gonna like even more", None),
                ("Alternative + FOMO", "what I DO have is something no one has ever seen and I think it's even better than what you asked for", None),
                ("Confidence Close", "just trust me on this one, you'll thank me later", None),
            ],
        },
    },
    "done": {
        "name": '"I already came"',
        "desc": "Finished before final PPV. Validate, rescue, seed next session.",
        "steps": 3, "cat": "res",
        "seqs": {
            "done-1": [
                ("Validate", "fuck that's hot, you came because of me??", None),
                ("Rescue", "but I haven't finished yet, don't you wanna watch me cum too?", None),
                ("Seed Next Session", "okay but next time you have to wait for me, I have something insane planned for round 2", None),
            ],
            "done-2": [
                ("Validate", "already?? damn that's hot", None),
                ("Rescue", "wait but I'm not done yet, you're gonna leave me like this?", None),
                ("Seed Next Session", "next time you HAVE to hold it because what I have planned for us next time is way crazier", None),
            ],
        },
    },
}

sit = {
    "cumcontrol": {
        "name": "He's close to cumming", "meta": "6 scripts", "type": "pick one",
        "desc": "CONTROL the timing. Pick based on where you are in the PPV ladder.",
        "items": [
            ("\\edge1", "don't cum yet... I'm not done with you"),
            ("\\edge2", "hold it, not yet... I need you to last a little longer for me"),
            ("\\sync1", "I'm so close too, cum with me... but you need to see this first"),
            ("\\sync2", "wait for me, I want us to finish together... open this first"),
            ("\\delay1", "hold it... I want you to wait until you see what I'm about to send, trust me it's worth it"),
            ("\\delay2", "don't you dare finish before you see this, trust me you want to wait"),
        ],
    },
    "dickpic": {
        "name": "He sends a dick pic", "meta": "6 scripts", "type": "pick based on moment",
        "desc": "NEVER ignore. ALWAYS react positively. This is a SALES OPPORTUNITY.",
        "items": [
            ("\\dpsext1", "fuck okay that's... damn. you have no idea what that just did to me"),
            ("\\dpsext2", "holy shit that is... fuck. I need to show you something rn"),
            ("\\dprapport1", "damn you don't waste time huh, that's actually really hot though ngl"),
            ("\\dprapport2", "woah I wasn't expecting that but... damn"),
            ("\\dpppv1", "you can't just send me that and expect me not to do something about it, hold on..."),
            ("\\dpppv2", "okay you just made me do something... give me a sec"),
        ],
    },
    "boosters": {
        "name": "Mid-sexting boosters", "meta": "8 scripts", "type": "mix & match",
        "desc": "Filler messages to maintain energy between script messages.",
        "items": [
            ("\\h1", "fuckkk"),
            ("\\h2", "I'm so hard rn because of you"),
            ("\\h3", "don't stop"),
            ("\\h4", "you have no idea what you're doing to me"),
            ("\\h5", "I literally can't think straight rn"),
            ("\\h6", "my hands are shaking"),
            ("\\h7", "more..."),
            ("\\h8", "I should be at the gym but I can't move rn"),
        ],
    },
}

# Read Putri's HTML to extract the CSS and JS (identical structure)
with open(r"c:\Users\34683\CW-ScriptManager\putri\objections.html", "r", encoding="utf-8") as f:
    putri = f.read()

# Extract style block
style_start = putri.index("<style>")
style_end = putri.index("</style>") + len("</style>")
style_block = putri[style_start:style_end]

# Extract script block
script_start = putri.index("<script>")
script_end = putri.index("</script>") + len("</script>")
script_block = putri[script_start:script_end]

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def step_html(i, tech, msg, note):
    h = f'<div class="step"><span class="step-num">{i}</span><div class="step-body"><div class="step-technique">{esc(tech)}</div><div class="step-msg">{esc(msg)}</div>'
    if note:
        h += f'<div class="step-note">{esc(note)}</div>'
    h += f'</div><button class="cp" data-copy="{esc(msg)}"><span class="cp-icon">📋</span></button></div>\n'
    return h

# Build body
body = ""

# OBJ category
obj_protos = {k:v for k,v in protocols.items() if v["cat"]=="obj"}
res_protos = {k:v for k,v in protocols.items() if v["cat"]=="res"}

body += '<div class="cat-header cat-obj"><span class="cat-emoji">💰</span><div class="cat-info"><h2>A. Objection Handling</h2><p>Fan pushes back on buying PPV. 6 protocols, 12 sequences.</p></div></div>\n'

first = True
for pid, p in obj_protos.items():
    collapsed = "" if first else " collapsed"
    first = False
    seq_keys = list(p["seqs"].keys())
    n_steps = p["steps"]
    body += f'<div class="protocol{collapsed}" id="{pid}">\n'
    body += f'  <div class="protocol-header"><span class="p-name">{p["name"]}</span><span class="p-meta">{n_steps} steps &middot; 2 seq</span><span class="toggle">&#9660;</span></div>\n'
    body += f'  <div class="protocol-body">\n'
    body += f'    <div class="p-desc">{esc(p["desc"])}</div>\n'
    body += f'    <div class="seq-tabs">\n'
    for i, sk in enumerate(seq_keys):
        cmd = sk.replace("-", "")
        active = " active" if i == 0 else ""
        body += f'      <div class="seq-tab{active}" data-seq="{sk}"><code>\\{cmd}</code></div>\n'
    body += f'    </div>\n'
    for i, sk in enumerate(seq_keys):
        active = " active" if i == 0 else ""
        body += f'    <div class="seq-panel{active}" id="{sk}">\n'
        for j, (tech, msg, note) in enumerate(p["seqs"][sk], 1):
            body += "      " + step_html(j, tech, msg, note)
        body += f'    </div>\n'
    if "after" in p:
        body += f'    <div class="p-after">{esc(p["after"])}</div>\n'
    body += f'  </div>\n</div>\n'

# RES category
body += '<div class="cat-header cat-res"><span class="cat-emoji">🔀</span><div class="cat-info"><h2>B. Resistance Handling</h2><p>Fan resists the conversation direction. 7 protocols, 14 sequences.</p></div></div>\n'

for pid, p in res_protos.items():
    seq_keys = list(p["seqs"].keys())
    n_steps = p["steps"]
    body += f'<div class="protocol collapsed" id="{pid}">\n'
    body += f'  <div class="protocol-header"><span class="p-name">{p["name"]}</span><span class="p-meta">{n_steps} steps &middot; 2 seq</span><span class="toggle">&#9660;</span></div>\n'
    body += f'  <div class="protocol-body">\n'
    body += f'    <div class="p-desc">{esc(p["desc"])}</div>\n'
    body += f'    <div class="seq-tabs">\n'
    for i, sk in enumerate(seq_keys):
        cmd = sk.replace("-", "")
        active = " active" if i == 0 else ""
        body += f'      <div class="seq-tab{active}" data-seq="{sk}"><code>\\{cmd}</code></div>\n'
    body += f'    </div>\n'
    for i, sk in enumerate(seq_keys):
        active = " active" if i == 0 else ""
        body += f'    <div class="seq-panel{active}" id="{sk}">\n'
        for j, (tech, msg, note) in enumerate(p["seqs"][sk], 1):
            body += "      " + step_html(j, tech, msg, note)
        body += f'    </div>\n'
    body += f'  </div>\n</div>\n'

# SIT category
body += '<div class="cat-header cat-sit"><span class="cat-emoji">⚡</span><div class="cat-info"><h2>C. Situational Scripts</h2><p>Standalone scripts. Not sequences. Pick the right one for the moment.</p></div></div>\n'

for sid, s in sit.items():
    body += f'<div class="protocol collapsed" id="{sid}">\n'
    body += f'  <div class="protocol-header"><span class="p-name">{s["name"]}</span><span class="p-meta">{s["meta"]} &middot; {s["type"]}</span><span class="toggle">&#9660;</span></div>\n'
    body += f'  <div class="protocol-body">\n'
    body += f'    <div class="p-desc">{esc(s["desc"])}</div>\n'
    body += f'    <div class="pool-grid">\n'
    for cmd, msg in s["items"]:
        body += f'      <div class="pool-item"><code>{cmd}</code><span class="pool-text">{esc(msg)}</span><button class="cp" data-copy="{esc(msg)}"><span class="cp-icon">📋</span></button></div>\n'
    body += f'    </div>\n'
    body += f'  </div>\n</div>\n'

# TOC
toc_items = ""
for pid, p in protocols.items():
    cls = "toc-obj" if p["cat"] == "obj" else "toc-res"
    label = pid.capitalize()
    if pid == "customyes": label = "Custom Yes"
    elif pid == "customno": label = "Custom No"
    elif pid == "nomoney": label = "No Money"
    elif pid == "noppv": label = "No PPV"
    elif pid == "nosex": label = "No Sex"
    elif pid == "offtopic": label = "Off-topic"
    elif pid == "real": label = "Are You Real"
    elif pid == "done": label = "Already Came"
    toc_items += f'  <a href="#{pid}" class="{cls}">{label}</a>\n'
for sid in sit:
    label = sid.capitalize()
    if sid == "cumcontrol": label = "Cum"
    elif sid == "dickpic": label = "Dick Pic"
    elif sid == "boosters": label = "Boosters"
    toc_items += f'  <a href="#{sid}" class="toc-sit">{label}</a>\n'

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>MAX — Objection & Resistance Handling</title>
{style_block}
</head>
<body>

<div class="page">

<a href="./" class="back-btn">&larr; Max Guide</a>

<div class="hero">
  <img src="profile.jpeg" alt="Max" class="hero-photo">
  <div>
    <h1>MAX &mdash; Objection & Resistance</h1>
    <div class="tagline">Complete sequences for Infloww &middot; v1 &middot; Feb 2026</div>
  </div>
</div>

<div class="info-bar">
  <span class="info-pill"><b>29</b> sheets</span>
  <span class="info-pill"><b>110</b> scripts</span>
  <span class="info-pill"><b>13</b> protocols &times; 2 sequences each</span>
  <span class="info-pill"><b>3</b> standalone pools</span>
</div>

<div class="howto">
  <strong>How to use:</strong> Each protocol has <strong>2 complete sequences</strong>. Use <code>\\price1</code> the first time. If the same fan objects again, use <code>\\price2</code> (different wording, same escalation). Infloww marks each as used so you always know which one is fresh.
</div>

<nav class="toc" id="toc">
{toc_items}</nav>

{body}

<div style="text-align:center;padding:24px 0 10px;color:var(--muted);font-size:.73rem">
  Chatting Wizard &middot; Script Manager &middot; 2026<br>
  MAX &mdash; OBJ/RES/SIT &middot; v1 (complete sequences)
</div>

</div>

<button class="top-btn" id="top-btn">&uarr;</button>

{script_block}
</body>
</html>"""

with open(r"c:\Users\34683\CW-ScriptManager\max\objections.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"Written: max/objections.html ({len(html)} chars)")
