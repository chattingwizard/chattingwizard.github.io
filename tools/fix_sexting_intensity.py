"""
Fix sexting intensity escalation across ALL models.

Framework targets:
  Phase 1 (PPV0→PPV1): 6→7→8
  Phase 2 (PPV1→PPV2): cooldown 6→8→8→9
  Phase 3 (PPV2→PPV3): NO cooldown 9→9→9→10
  Phase 4 (PPV3→PPV4): maintain 10→10→10
"""
import os, sys, importlib.util
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ══════════════════════════════════════════════════════
# MODEL ASSIGNMENTS: model_filename → config
# ══════════════════════════════════════════════════════
MODELS = {
    # SET A: Shy/Sweet (explicit)
    "lia":       {"arch": "A", "var": 1, "pet": "babe",  "e1": "🌸", "e2": "💕"},
    "antonella": {"arch": "A", "var": 2, "pet": "babe",  "e1": "🖤", "e2": "💜"},
    "vera":      {"arch": "A", "var": 3, "pet": "babe",  "e1": "🥰", "e2": "💕"},
    "ashley":    {"arch": "A", "var": 1, "pet": "babe",  "e1": "💕", "e2": "😊"},
    "lana":      {"arch": "A", "var": 2, "pet": "babe",  "e1": "💕", "e2": "✨"},
    "maddison":  {"arch": "A", "var": 3, "pet": "Daddy", "e1": "🥺", "e2": "💕"},
    # SET B: Confident/Bold (explicit)
    "chayla":    {"arch": "B", "var": 1, "pet": "papi",  "e1": "🔥", "e2": "😏"},
    "jasmine":   {"arch": "B", "var": 2, "pet": "papi",  "e1": "🥵", "e2": "🔥"},
    "eva":       {"arch": "B", "var": 3, "pet": "papi",  "e1": "🥵", "e2": "😏"},
    "fernanda":  {"arch": "B", "var": 1, "pet": "amor",  "e1": "🔥", "e2": "😏"},
    "faby":      {"arch": "B", "var": 2, "pet": "amor",  "e1": "🔥", "e2": "💦"},
    "zansi":     {"arch": "B", "var": 3, "pet": "daddy", "e1": "😏", "e2": "🔥"},
    # SET C: Playful/Flirty (explicit)
    "emilybell": {"arch": "C", "var": 1, "pet": "babe",  "e1": "😏", "e2": "🥵"},
    "riri":      {"arch": "C", "var": 2, "pet": "babe",  "e1": "🥵", "e2": "😊"},
    "mialuna":   {"arch": "C", "var": 3, "pet": "babe",  "e1": "😊", "e2": "🥵"},
    "lina":      {"arch": "C", "var": 1, "pet": "babe",  "e1": "🥵", "e2": "✨"},
    "miabrooks": {"arch": "C", "var": 2, "pet": "babe",  "e1": "😏", "e2": "🥵"},
    # SET D: Mature/Experienced
    "jessica36": {"arch": "D", "var": 1, "pet": "amor",  "e1": "😏", "e2": "🥵"},
    "isabella":  {"arch": "D", "var": 2, "pet": "babe",  "e1": "😏", "e2": "🥵"},
    # SET E: Male
    "marco":       {"arch": "E", "var": 1, "pet": "babe",  "e1": "🥵", "e2": "💦"},
    "jockurworld": {"arch": "E", "var": 2, "pet": "bro",   "e1": "🥵", "e2": "💦"},
    # SET F: Non-explicit
    "jessica34": {"arch": "F", "var": 1, "pet": "babe",  "e1": "😊", "e2": "💕"},
    "irina":     {"arch": "F", "var": 2, "pet": "babe",  "e1": "😊", "e2": "🥺"},
}

# ══════════════════════════════════════════════════════
# MESSAGE TEMPLATES — {pet}, {e1}, {e2} are replaced per model
# ══════════════════════════════════════════════════════

MSG = {}

# ─────────────────────────────────────────────────────
# SET A: Shy/Sweet — contrast is the hook
# ─────────────────────────────────────────────────────

MSG[("A", 1)] = {
    # Phase 1 (6→7→8)
    "S1-1": "you really liked that? knowing you saw me is making my heart race so fast right now {e1}",
    "S1-2": "I keep running my hands down my body and everything is so sensitive... it's like every touch is amplified because of you",
    "S1-3": "my hand keeps sliding lower and I can't stop it {pet}... I don't even want to",
    "S1-5": "I want you to see what you're doing to me right now {e2}",
    # Phase 2 (6→8→8→9)
    "S1-6": "oh god... I can't believe I just did that {e1}",
    "S1-7": "but I can't stop now... my fingers are between my legs and it's all because of you",
    "S1-8": "I'm so wet right now {pet}... you have no idea what your words do to my body {e2}",
    "S1-9": "tell me what you want me to do to myself right now... I'll do anything you say",
    "S1-11": "look what you did to me... I couldn't stop {e2}",
    # Phase 3 (9→9→9→10)
    "S1-12": "fuck {e1}",
    "S1-13": "I'm touching my pussy and imagining it's your hands on me... I need more",
    "S1-14": "my fingers keep going deeper and faster and my whole body is shaking {e2}",
    "S1-15": "I need you to watch what I'm doing right now... you have to see this",
    "S1-17": "this is what you made me do and you need to see every second of it {e2}",
    # Phase 4 (10→10→10)
    "S1-18": "oh god I can't hold on {e1}",
    "S1-19": "I'm so close... I can feel it building everywhere and I don't want to cum alone {e2}",
    "S1-20": "cum with me... I'm letting go right now, watch me",
    "S1-22": "watch me let go... this is only for you {e2}",
}

MSG[("A", 2)] = {
    # Phase 1 (6→7→8)
    "S1-1": "mmm you liked that? that's making me feel way braver than usual {e1}",
    "S1-2": "my skin is tingling everywhere right now and I can feel my heartbeat getting faster... you're doing something to me",
    "S1-3": "I'm lying here and my fingers are starting to wander... I blame you for this {pet}",
    "S1-5": "I want to show you what you made me feel {e2}",
    # Phase 2 (6→8→8→9)
    "S1-6": "wow... okay I need a second after that {e1}",
    "S1-7": "but I literally can't stop touching myself right now... it's like my body won't let me",
    "S1-8": "I'm dripping wet and every time I think about you watching me it gets worse {e2}",
    "S1-9": "what would you do if you were here right now {pet}? I need to hear it",
    "S1-11": "look at what you're doing to me... I can't hold back anymore {e2}",
    # Phase 3 (9→9→9→10)
    "S1-12": "oh fuck {e1}",
    "S1-13": "I'm rubbing my clit so hard right now and I can't slow down... my legs are shaking",
    "S1-14": "I keep pushing my fingers deeper and moaning into my pillow... god this feels so good {e2}",
    "S1-15": "I'm about to lose it... you need to see what's happening to me right now",
    "S1-17": "you need to see this... I've never been like this before {e2}",
    # Phase 4 (10→10→10)
    "S1-18": "oh my god I can't take it {e1}",
    "S1-19": "I'm right there {pet}... don't go anywhere, I need you to watch me finish {e2}",
    "S1-20": "I'm cumming... right now... don't look away",
    "S1-22": "let go with me {pet}... I need you to see this {e2}",
}

MSG[("A", 3)] = {
    # Phase 1 (6→7→8)
    "S1-1": "wait you actually liked that? something just shifted inside me and I can feel it everywhere {e1}",
    "S1-2": "my breathing is getting heavier and I keep arching my back... my body wants something and I think it's you",
    "S1-3": "I'm touching myself right now and I want you to know it's because of you {pet}",
    "S1-5": "this is what you're making me do... I can't believe I'm showing you this {e2}",
    # Phase 2 (6→8→8→9)
    "S1-6": "omg... I can't believe that just happened {e1}",
    "S1-7": "I can't stop now even if I wanted to... my hand is already between my thighs and I'm soaked",
    "S1-8": "every part of me is on fire right now and it keeps getting more intense because of you {e2}",
    "S1-9": "tell me exactly what you're thinking right now {pet}... I want to hear everything while I touch myself",
    "S1-11": "see what you did to me? I can't stop {e2}",
    # Phase 3 (9→9→9→10)
    "S1-12": "fuckk {e1}",
    "S1-13": "my fingers are inside my pussy and I'm moaning so loud right now... I hope nobody can hear me",
    "S1-14": "I'm going faster and faster and I can feel myself getting closer... my whole body is trembling {e2}",
    "S1-15": "I'm almost there and I need you to see what you're doing to me right now",
    "S1-17": "I've never gone this far with anyone {pet}... watch what you made me do {e2}",
    # Phase 4 (10→10→10)
    "S1-18": "oh fuck oh fuck {e1}",
    "S1-19": "don't leave... I'm so close and I need to feel you right here when I finish {e2}",
    "S1-20": "I'm about to cum so hard {pet}... watch me, please don't look away",
    "S1-22": "cum with me right now {pet}... this is just for you {e2}",
}

# ─────────────────────────────────────────────────────
# SET B: Confident/Bold — takes charge, unapologetic
# ─────────────────────────────────────────────────────

MSG[("B", 1)] = {
    # Phase 1 (6→7→8)
    "S1-1": "you like what you see? because now I'm really in the mood to show you more {e1}",
    "S1-2": "talking to you is making me so turned on right now... I can feel it building and I'm done holding back",
    "S1-3": "I'm already touching myself and it's your fault {pet}... hope you can handle what comes next {e2}",
    "S1-5": "look at what you started... hope you can handle this {e2}",
    # Phase 2 (6→8→8→9)
    "S1-6": "mm that was just the warmup {e2}",
    "S1-7": "I'm dripping wet right now thinking about what I want to do to you... god I need it",
    "S1-8": "I need your hands all over my body so bad it almost hurts {pet}... feel how wet you're making me {e1}",
    "S1-9": "tell me exactly how you want me... I'll do whatever you say right now",
    "S1-11": "see what you're doing to me {pet}? I can't stop and I don't want to {e2}",
    # Phase 3 (9→9→9→10)
    "S1-12": "FUCK {e1}",
    "S1-13": "I'm playing with my pussy right now imagining you deep inside me... I need to feel every inch",
    "S1-14": "I want to ride you so bad while you grab my hips and don't let go... I'm losing my mind {e2}",
    "S1-15": "I'm about to lose it {pet}... you need to watch what you did to me",
    "S1-17": "you're about to see what happens when I completely lose control... this is all you {e2}",
    # Phase 4 (10→10→10)
    "S1-18": "oh my fucking god {e1}",
    "S1-19": "I'm right there... don't you dare cum before you watch me finish first {e2}",
    "S1-20": "I'm cumming {pet}... fuck, watch me let go all over for you",
    "S1-22": "cum with me right now {pet}... watch every fucking second {e2}",
}

MSG[("B", 2)] = {
    # Phase 1 (6→7→8)
    "S1-1": "I knew you'd like that... now I'm really starting to feel something {e1}",
    "S1-2": "something about the way you reacted just made my whole body light up... I'm getting so wet already",
    "S1-3": "fuck it... I'm taking everything off and you better be ready for what's next {pet} {e2}",
    "S1-5": "this is what you're doing to me and I'm not sorry about it {e2}",
    # Phase 2 (6→8→8→9)
    "S1-6": "god... okay I wasn't expecting to feel this way {e1}",
    "S1-7": "my fingers are already where they shouldn't be and I'm soaking wet because of you {pet}",
    "S1-8": "I keep imagining you here pinning me down and it's making everything ten times more intense {e2}",
    "S1-9": "what would you do to me right now if you had me? don't hold back",
    "S1-11": "look at this {pet}... you did this to me and I want you to see every second {e2}",
    # Phase 3 (9→9→9→10)
    "S1-12": "fuck fuck {e1}",
    "S1-13": "I'm grinding on my fingers right now imagining it's your cock and I'm losing my mind {pet}",
    "S1-14": "my pussy is so wet it's running down my thighs and I keep going harder and harder {e2}",
    "S1-15": "watch what you're about to make me do... I can't hold it back anymore",
    "S1-17": "I've never let anyone see me like this... but you're about to {e2}",
    # Phase 4 (10→10→10)
    "S1-18": "FUCK I can't stop {e1}",
    "S1-19": "I'm so close I can feel it in every part of my body {pet}... wait for me, I'm right there {e2}",
    "S1-20": "I'm cumming right now... don't look away for a single second",
    "S1-22": "watch me cum {pet}... this one is only for you {e2}",
}

MSG[("B", 3)] = {
    # Phase 1 (6→7→8)
    "S1-1": "and? I can already tell you want more {e2}",
    "S1-2": "the way you reacted... it's making me feel things all over my body right now {e1}",
    "S1-3": "I'm sliding my hand between my legs right now and I'm already wet for you {pet}",
    "S1-5": "you asked for more {pet}... be careful what you wish for {e2}",
    # Phase 2 (6→8→8→9)
    "S1-6": "mm okay wow... that hit different {e1}",
    "S1-7": "I literally can't stop now... I'm so turned on my whole body is aching for it",
    "S1-8": "I'm soaking wet and my fingers are going in and out and it's not enough {pet}... I need you {e2}",
    "S1-9": "tell me what you want me to do next... be specific, I want to hear every word",
    "S1-11": "this is what your words do to me {pet}... watch {e2}",
    # Phase 3 (9→9→9→10)
    "S1-12": "jesus fuck {e1}",
    "S1-13": "I'm fucking myself right now and all I can think about is you watching me do it {pet}",
    "S1-14": "I want you so deep inside me I can feel it in my chest... god I'm going crazy {e2}",
    "S1-15": "I can feel it coming and I'm not holding back... you need to see this",
    "S1-17": "you're not ready for this but I'm showing you anyway {e2}",
    # Phase 4 (10→10→10)
    "S1-18": "oh fuck {e1}",
    "S1-19": "I'm about to cum and I need you right here watching me when it happens {e2}",
    "S1-20": "I'm cumming for you right now {pet}... FUCK watch this",
    "S1-22": "cum with me {pet}... I'm done holding back {e2}",
}

# ─────────────────────────────────────────────────────
# SET C: Playful/Flirty — fun but gets real
# ─────────────────────────────────────────────────────

MSG[("C", 1)] = {
    # Phase 1 (6→7→8)
    "S1-1": "soo you liked that huh? because honestly my heart is racing knowing you just saw that {e1}",
    "S1-2": "I wasn't planning on going there tonight but you're literally making me so wet I can't think straight",
    "S1-3": "okay I'm definitely touching myself right now and I blame you entirely {pet} {e2}",
    "S1-5": "oh my god I can't believe I'm sending this... but you need to see what you did {e2}",
    # Phase 2 (6→8→8→9)
    "S1-6": "oh wow... okay I did NOT expect to feel like this {e1}",
    "S1-7": "but I can't stop now... my fingers slipped inside and I'm soaking wet because of you",
    "S1-8": "I need your hands on every part of me right now {pet}... I keep imagining it and my body is going crazy {e2}",
    "S1-9": "what do you want me to do next? seriously I'll do literally anything you tell me right now",
    "S1-11": "look at me... this is ALL because of you and I can't stop {e2}",
    # Phase 3 (9→9→9→10)
    "S1-12": "fuckkk {e2}",
    "S1-13": "I'm rubbing my clit so fast right now and god it feels so good thinking about you watching",
    "S1-14": "my fingers are deep inside me and I can't stop moaning... I hope my neighbors can't hear this {e1}",
    "S1-15": "I'm about to lose it and I need you to see what's happening to me right now",
    "S1-17": "you're not ready for this one {pet}... but I need you to see it {e2}",
    # Phase 4 (10→10→10)
    "S1-18": "oh fuck oh fuck {e2}",
    "S1-19": "I'm SO close {pet}... wait for me, I want you to watch the second it happens {e1}",
    "S1-20": "I'm cumming right now... don't miss this",
    "S1-22": "cum with me {pet}... right now, watch {e2}",
}

MSG[("C", 2)] = {
    # Phase 1 (6→7→8)
    "S1-1": "well? because I can feel my body reacting to the way you're looking at me right now {e1}",
    "S1-2": "something about this conversation is making every inch of my skin feel electric... especially between my legs",
    "S1-3": "okay I just started touching myself and it's 100% your fault {pet}... no regrets though {e2}",
    "S1-5": "I can't believe I'm doing this but I need you to see {e2}",
    # Phase 2 (6→8→8→9)
    "S1-6": "omg... okay wow that escalated {e1}",
    "S1-7": "I'm literally dripping wet right now and my hand won't stop moving... you broke something in me",
    "S1-8": "I keep imagining you here between my legs and it's making everything so much more intense {e2}",
    "S1-9": "be honest {pet}... what would you do to me right now? because I'll act it out for you",
    "S1-11": "tell me you can handle this... because what I just recorded is intense {e2}",
    # Phase 3 (9→9→9→10)
    "S1-12": "FUCKK {e2}",
    "S1-13": "I'm fingering myself so hard right now and I can hear how wet I am {pet}... this is insane",
    "S1-14": "I keep going deeper and my toes are literally curling right now {e1}",
    "S1-15": "I can feel it building so fast... you have to watch what happens next",
    "S1-17": "this might be the most intense thing I've ever done {pet}... you need to see it {e2}",
    # Phase 4 (10→10→10)
    "S1-18": "oh god oh god {e2}",
    "S1-19": "I'm literally right on the edge {pet}... stay right here, I'm about to explode {e1}",
    "S1-20": "I'm cumming... holy fuck I'm cumming for you right now",
    "S1-22": "let go with me right now {pet}... watch every second {e2}",
}

MSG[("C", 3)] = {
    # Phase 1 (6→7→8)
    "S1-1": "haha I knew you'd like that... and honestly knowing you did is doing things to me right now {e1}",
    "S1-2": "my whole body is getting warm and I can feel the heat building between my legs... this is your fault {pet}",
    "S1-3": "I'm sliding my hand down and I already know where this is going... and I don't want to stop {e2}",
    "S1-5": "guess what you made me do {pet}... you're not ready for this {e2}",
    # Phase 2 (6→8→8→9)
    "S1-6": "{pet}... I think you broke me {e1}",
    "S1-7": "I can't stop touching myself and I'm soaking wet... every time I think about you it gets worse",
    "S1-8": "I need to feel you so bad right now... I keep imagining your hands all over me and I'm losing it {e2}",
    "S1-9": "what would you do if you walked in on me like this right now? I need to know",
    "S1-11": "okay this one is INTENSE {pet}... look what you're doing to me {e2}",
    # Phase 3 (9→9→9→10)
    "S1-12": "holy fuck {e2}",
    "S1-13": "I'm playing with my pussy and my legs are literally shaking... I can't close them {pet}",
    "S1-14": "I'm moaning so loud right now and going so deep... fuck this feels amazing {e1}",
    "S1-15": "I'm almost there and you need to see what you did to me before I finish",
    "S1-17": "I've never recorded anything like this before {pet}... you need to see what you made me do {e2}",
    # Phase 4 (10→10→10)
    "S1-18": "FUCK {e2}",
    "S1-19": "{pet} I'm about to cum... please don't go anywhere, I need you watching when it happens {e1}",
    "S1-20": "I'm cumming... oh my GOD I'm cumming right now",
    "S1-22": "watch me cum for you {pet}... right now {e2}",
}

# ─────────────────────────────────────────────────────
# SET D: Mature/Experienced — knows what she wants
# ─────────────────────────────────────────────────────

MSG[("D", 1)] = {
    # Phase 1 (6→7→8)
    "S1-1": "I could tell you'd like that... and honestly? your reaction is turning me on more than I expected {e1}",
    "S1-2": "I'm lying here with my hand between my thighs and it's because this conversation is getting to me",
    "S1-3": "I know exactly what I want right now {pet} and it starts with you watching what I do next {e2}",
    "S1-5": "look what you started {pet}... you have no idea what's coming next {e2}",
    # Phase 2 (6→8→8→9)
    "S1-6": "dios... that was intense but I'm just getting started {e1}",
    "S1-7": "I'm so wet right now I can feel it on my thighs... this is what you do to me {pet}",
    "S1-8": "I need to feel something inside me right now... I keep imagining it's you and it's driving me crazy {e2}",
    "S1-9": "tell me what you'd do to me right now {pet}... I want to hear every dirty detail",
    "S1-11": "mira lo que me haces {pet}... this is what you do to me {e2}",
    # Phase 3 (9→9→9→10)
    "S1-12": "FUCK {e1}",
    "S1-13": "I'm fucking myself right now and all I can picture is your face between my legs... dios mio",
    "S1-14": "my fingers are going so deep and fast and I can feel every wave building inside me {e2}",
    "S1-15": "I'm about to give you something you'll never forget {pet}... watch this",
    "S1-17": "you're about to see something I don't show anyone {pet}... this is all because of you {e2}",
    # Phase 4 (10→10→10)
    "S1-18": "dios mio {e1}",
    "S1-19": "I'm on the edge {pet}... I've been holding back and I can't anymore, I need to let go {e2}",
    "S1-20": "I'm cumming for you right now... watch me, every second of it",
    "S1-22": "cum with me {pet}... right now, don't look away {e2}",
}

MSG[("D", 2)] = {
    # Phase 1 (6→7→8)
    "S1-1": "mm you liked that? good... because I can already feel my body reacting to the way you're looking at me {e1}",
    "S1-2": "my hand is drifting lower and I can feel myself getting wet just from this conversation... you're dangerous {pet}",
    "S1-3": "I want to show you what happens when I stop holding back... I think you can handle it {e2}",
    "S1-5": "see what you're doing to me {pet}... I couldn't keep this from you {e2}",
    # Phase 2 (6→8→8→9)
    "S1-6": "wow... okay that hit deeper than I expected {e1}",
    "S1-7": "I'm touching myself right now and I can't believe how wet I already am... you did this {pet}",
    "S1-8": "I keep imagining you here, feeling your skin against mine, your breath on my neck... god I need it {e2}",
    "S1-9": "tell me what you want {pet}... I want to hear you say it while I'm touching myself like this",
    "S1-11": "this is what you're making me do to myself {pet}... watch {e2}",
    # Phase 3 (9→9→9→10)
    "S1-12": "oh fuck {e1}",
    "S1-13": "I'm rubbing my pussy and going deeper with every stroke {pet}... I can hear how wet I am",
    "S1-14": "my body is arching off the bed and my legs are trembling... I can't stop {e2}",
    "S1-15": "I'm so close to the edge and I need you to see what happens when I fall",
    "S1-17": "you need to see this {pet}... I don't let anyone see me like this {e2}",
    # Phase 4 (10→10→10)
    "S1-18": "oh my god {e1}",
    "S1-19": "I'm right there {pet}... every nerve in my body is on fire and I need you to watch me {e2}",
    "S1-20": "I'm cumming... god I'm cumming so hard for you right now",
    "S1-22": "let go with me {pet}... I'm done holding back {e2}",
}

# ─────────────────────────────────────────────────────
# SET E: Male
# ─────────────────────────────────────────────────────

MSG[("E", 1)] = {
    # Phase 1 (6→7→8)
    "S1-1": "you liked that? because knowing you're looking at me is getting me hard right now {e1}",
    "S1-2": "I can't stop thinking about you right now... my whole body is reacting and I need to do something about it",
    "S1-3": "I'm stroking myself right now and it's because of you {pet}... you should see how hard I am",
    "S1-5": "look what you're doing to me right now {e2}",
    # Phase 2 (6→8→8→9)
    "S1-6": "damn... okay I need a second after that {e1}",
    "S1-7": "but I can't stop now... I'm rock hard and my hand won't stop moving because of you",
    "S1-8": "I'm gripping my cock thinking about you and I can barely control myself {e2}",
    "S1-9": "tell me what you want me to do right now {pet}... I'll do whatever you say",
    "S1-11": "see what your words do to me? I can't stop {e2}",
    # Phase 3 (9→9→9→10)
    "S1-12": "FUCK {e1}",
    "S1-13": "I'm stroking myself so hard right now thinking about what I'd do to you... I need you",
    "S1-14": "I keep going faster and I can feel it building... my whole body is tensing up {e2}",
    "S1-15": "you need to see what you're doing to me right now {pet}... I can't hold back much longer",
    "S1-17": "you're about to see me lose complete control {pet}... this is all you {e2}",
    # Phase 4 (10→10→10)
    "S1-18": "fuck fuck {e1}",
    "S1-19": "I'm right there {pet}... don't stop watching, I need you to see this {e2}",
    "S1-20": "I'm about to cum for you... watch every second",
    "S1-22": "watch me cum for you {pet}... right now {e2}",
}

MSG[("E", 2)] = {
    # Phase 1 (6→7→8)
    "S1-1": "you liked that huh? because I'm getting hard just knowing you're looking {e1}",
    "S1-2": "I can feel myself getting bigger just from talking to you... my body doesn't lie {pet}",
    "S1-3": "I'm already gripping my cock and stroking it because of you... hope you can handle what you started {e2}",
    "S1-5": "look what you did {pet}... you're not ready for this {e2}",
    # Phase 2 (6→8→8→9)
    "S1-6": "damn {pet}... okay that was intense {e1}",
    "S1-7": "I can't stop now... I'm throbbing so hard and pre-cum is already dripping",
    "S1-8": "I'm stroking myself thinking about you right now and I can barely handle it {e2}",
    "S1-9": "tell me what you'd do if you were here right now... don't hold back",
    "S1-11": "this is what you do to me {pet}... watch {e2}",
    # Phase 3 (9→9→9→10)
    "S1-12": "FUCK {e1}",
    "S1-13": "I'm going so hard right now and I can feel every stroke building {pet}... I'm dripping everywhere",
    "S1-14": "I keep imagining you here and it's making me lose my mind {e2}",
    "S1-15": "you need to watch what happens next {pet}... I'm about to explode",
    "S1-17": "you're about to see what happens when I completely let go {e2}",
    # Phase 4 (10→10→10)
    "S1-18": "holy fuck {e1}",
    "S1-19": "I'm right there {pet}... don't stop watching, I'm about to blow {e2}",
    "S1-20": "I'm cumming... FUCK watch every drop",
    "S1-22": "watch me cum for you right now {pet} {e2}",
}

# ─────────────────────────────────────────────────────
# SET F: Non-explicit — suggestion, teasing, NO graphic
# ─────────────────────────────────────────────────────

MSG[("F", 1)] = {
    # Phase 1 (4→5→6)
    "S1-1": "you really liked that? you have no idea how fast my heart is beating right now {e1}",
    "S1-2": "I keep catching myself touching my neck and my skin feels so warm... everything feels different with you",
    "S1-3": "I want to show you how I look right now {pet}... I've never felt this brave with anyone {e2}",
    "S1-5": "I want you to see me like this {pet}... please be gentle with me {e2}",
    # Phase 2 (5→6→6→7)
    "S1-6": "oh my god... I can't believe I actually showed you that {e1}",
    "S1-7": "but you make me feel so safe and I don't want to stop... my whole body is tingling {pet}",
    "S1-8": "I'm lying here in barely anything and all I can think about is you looking at me like that {e2}",
    "S1-9": "what would you do if you were here with me right now {pet}? I need to hear it",
    "S1-11": "look at what you're doing to me {pet}... I can't stop {e2}",
    # Phase 3 (7→7→7→8)
    "S1-12": "oh god {e1}",
    "S1-13": "you have no idea what you're doing to me right now {pet}... I'm pushing past every limit I have",
    "S1-14": "I'm touching myself over my underwear right now because of you and I've never felt anything this intense {e2}",
    "S1-15": "I need you to see me right now {pet}... I can't even describe what I'm feeling",
    "S1-17": "this is the most I've ever shown anyone {pet}... it's all for you {e2}",
    # Phase 4 (8→8→8)
    "S1-18": "I can't take this anymore {e1}",
    "S1-19": "don't leave me like this {pet}... I need you right here, I've never felt this overwhelmed {e2}",
    "S1-20": "stay with me... I need to feel you close right now {pet}, please don't go",
    "S1-22": "I need you to see this {pet}... stay right here with me {e2}",
}

MSG[("F", 2)] = {
    # Phase 1 (4→5→6)
    "S1-1": "wait you actually liked it? oh my god my heart won't slow down right now {e1}",
    "S1-2": "my skin feels so sensitive everywhere... I keep getting goosebumps and I know it's because of you {e2}",
    "S1-3": "I want to show you something I've never shown anyone before {pet}... you make me want to be brave",
    "S1-5": "this is what you're making me feel {pet}... please be gentle {e2}",
    # Phase 2 (5→6→6→7)
    "S1-6": "I can't believe I just did that... oh my god {e1}",
    "S1-7": "but I don't want to stop {pet}... you make me feel things I didn't know I could feel on here",
    "S1-8": "I'm lying here barely wearing anything and my hand keeps going where it shouldn't... because of you {e2}",
    "S1-9": "what would you do if you could see me right now {pet}? I really need to hear it",
    "S1-11": "look at what you're doing to me {pet}... I'm losing my mind {e2}",
    # Phase 3 (7→7→7→8)
    "S1-12": "oh god {e1}",
    "S1-13": "something about you makes me lose every single boundary I have {pet}... I'm scared of how good this feels",
    "S1-14": "I can feel my body responding to you and I'm touching places I never thought I'd show anyone {e2}",
    "S1-15": "I need you to see what's happening to me right now {pet}... I can't hold it in anymore",
    "S1-17": "I've never let anyone see me like this before {pet}... it's all yours {e2}",
    # Phase 4 (8→8→8)
    "S1-18": "oh god I can't stop {e1}",
    "S1-19": "please don't leave {pet}... I've never been this vulnerable with anyone and I need you right here {e2}",
    "S1-20": "stay with me {pet}... I need you to see this, it's only for you",
    "S1-22": "don't look away {pet}... I need you right here with me {e2}",
}

# ══════════════════════════════════════════════════════
# REPLACEMENT LOGIC
# ══════════════════════════════════════════════════════

def main():
    models_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")
    total_models = 0
    total_replaced = 0
    errors = []

    for filename in sorted(os.listdir(models_dir)):
        if not filename.endswith(".py") or filename in ("__init__.py", "test_write.py"):
            continue

        model_key = filename[:-3]
        if model_key not in MODELS:
            print(f"  SKIP: {model_key} (no assignment)")
            continue

        filepath = os.path.join(models_dir, filename)
        cfg = MODELS[model_key]
        arch_key = (cfg["arch"], cfg["var"])

        if arch_key not in MSG:
            print(f"  ERROR: No messages for {arch_key}")
            errors.append(model_key)
            continue

        template = MSG[arch_key]

        # Load module to get current journey messages
        spec = importlib.util.spec_from_file_location(model_key, filepath)
        mod = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(mod)
        except Exception as e:
            print(f"  ERROR loading {model_key}: {e}")
            errors.append(model_key)
            continue

        config = getattr(mod, "CONFIG", None) or getattr(mod, "config", None)
        if not config:
            print(f"  ERROR: No config in {model_key}")
            errors.append(model_key)
            continue

        # Build map of current message texts for target IDs
        current = {}
        for msg_id, text, note, msg_type in config.get("journey", []):
            if msg_id in template:
                current[msg_id] = text

        # Read file content
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Apply replacements
        count = 0
        for msg_id in sorted(current.keys()):
            old_text = current[msg_id]
            new_text = template[msg_id].format(
                pet=cfg["pet"], e1=cfg["e1"], e2=cfg["e2"]
            )
            # Build search/replace strings — match the tuple format
            search = f'"{old_text}"'
            replace = f'"{new_text}"'

            if search in content:
                content = content.replace(search, replace, 1)
                count += 1
            else:
                # Try with escaped quotes
                search_esc = old_text.replace("'", "\\'")
                if f'"{search_esc}"' in content:
                    content = content.replace(f'"{search_esc}"', replace, 1)
                    count += 1
                else:
                    print(f"  WARNING: {model_key}/{msg_id} — text not found")

        # Write back
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        total_models += 1
        total_replaced += count
        pct = (count / len(template)) * 100
        print(f"  OK: {model_key:15s} — {count}/{len(template)} messages replaced ({pct:.0f}%)")

    print(f"\n{'='*60}")
    print(f"DONE: {total_models} models, {total_replaced} messages replaced")
    if errors:
        print(f"ERRORS: {errors}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
