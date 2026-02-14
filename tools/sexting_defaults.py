"""
Sexting sequence templates — standalone sequences for returning fans.

Each template is a complete sexting session:
  Short teasing bridge (3-4 msgs) → Sexting with 4 PPVs → Aftercare

4 dynamics as defined in the framework:
  - SUB_LEADS: Fan "controls" — "what do you want me to do?"
  - INTIMATE: Emotional + sexual connection — "I feel something real"
  - CHALLENGE: Game/dare-based — "earn the next one"
  - FANTASY: Roleplay/scenario — immersive experience

NOTE: Sex1 (Dominant) is already the S1 embedded in the Welcome Journey.
These templates are Sex2-Sex5 for use in subsequent sessions.

3 gender variants:
  - FEMALE: female creators
  - MALE: male creators (straight, targeting female fans)
  - MALE_GAY: male creators targeting male fans

Placeholder tokens (replaced by model_factory during generation):
  {pet}  → model's preferred pet name (babe, baby, cutie, etc.)
  {pet2} → secondary pet name
  {emoji} → model's preferred emoji (🖤, 💜, etc.)

PPV pricing follows standard ladder:
  PPV 0: FREE | PPV 1: $12 | PPV 2: $25 | PPV 3: $40 | PPV 4: $55
"""

# ═══════════════════════════════════════════════════════════════
# FEMALE — SUB LEADS (fan "controls")
# ═══════════════════════════════════════════════════════════════

SEXT_SUB_LEADS_FEMALE = [
    # -- Short Teasing Bridge --
    ("TB-1", "hey you {emoji} I can't stop thinking about last time", None, "teasing"),
    ("TB-2", "I've been lying in bed all day and my mind keeps going back to you", "React to his reply.", "teasing"),
    ("TB-3", "you wanna know something? I keep wondering what you'd make me do if you were here", None, "teasing"),
    ("TB-4", "hold on let me show you what I mean", "WAIT 1-2 MIN", "wait"),
    ("TB-5", "tell me what you think {emoji}", "SEND PPV 0 — FREE teaser (lounging in bed, suggestive pose). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 1: Fan takes control --
    ("S-1", "mmm okay so what would you do to me right now? I wanna hear it {emoji}", "Wait for reply. Let HIM lead. React to whatever he says.", "sext"),
    ("S-2", "fuck that's hot... okay I'm doing it, I'm touching myself the way you described", "React specifically to what he said. Make him feel in control.", "sext"),
    ("S-3", "wait you want me to go lower? god you're bold and I love it", None, "sext"),
    ("S-4", "one sec {emoji}", "WAIT 2-3 MIN", "wait"),
    ("S-5", "look what you made me do {emoji}", "SEND PPV 1 — $12 (following his 'instructions' — solo tease, touching). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 2: Deeper submission --
    ("S-6", "okay I did that... now what? don't stop telling me {pet}", "Wait for reply. He's in control of the pace.", "sext"),
    ("S-7", "oh my god I can't believe I'm actually doing everything you say right now", "React to his reply. Make it feel like HE is causing every action.", "sext"),
    ("S-8", "my hand is between my legs and I'm following every word you type... this is so hot", None, "sext"),
    ("S-9", "you want me to use my toy too? fuck you're going to destroy me {emoji}", "Wait for reply.", "sext"),
    ("S-10", "hold on let me get it", "WAIT 2-3 MIN", "wait"),
    ("S-11", "you asked for this... look {emoji}", "SEND PPV 2 — $25 (doing what he requested — more explicit solo). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 3: Full surrender --
    ("S-12", "oh fuck {pet} I'm doing exactly what you said and I'm shaking", "Wait for reply. NO cooldown.", "sext"),
    ("S-13", "nobody has ever controlled me like this... I'm literally your puppet right now and I can't stop", None, "sext"),
    ("S-14", "I can feel myself getting close and it's all because of you telling me what to do", "Solo framing — she's following HIS instructions.", "sext"),
    ("S-15", "I need you to see what you're doing to me right now... please", None, "sext"),
    ("S-16", "wait", "WAIT 2-3 MIN", "wait"),
    ("S-17", "you did this to me {emoji}", "SEND PPV 3 — $40 (explicit solo, following his direction, more intense). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 4: Climax --
    ("S-18", "oh my god I'm so close {pet}... tell me to cum, I need to hear you say it", "Wait for reply.", "sext"),
    ("S-19", "I'm right on the edge and I won't let go until you tell me to {emoji}", None, "sext"),
    ("S-20", "fuck yes... I'm cumming so hard right now because you told me to", None, "sext"),
    ("S-21", "wait", "WAIT 1-2 MIN", "wait"),
    ("S-22", "this is what happens when you take control of me {emoji}", "SEND PPV 4 — $55 (climax, full surrender to his commands). Bought → Aftercare. Silent → NR Waves.", "ppv"),

    # -- Aftercare --
    ("AC-1", "holy shit {pet}... that was the most intense thing I've ever done with someone telling me what to do {emoji}", None, "aftercare"),
    ("AC-2", "you have no idea how hard that made me cum... I literally can't move right now", "Mention something specific he said/directed. KEEP TALKING — build bond. NEVER say goodbye.", "aftercare"),
]


# ═══════════════════════════════════════════════════════════════
# FEMALE — INTIMATE (emotional connection + sexual)
# ═══════════════════════════════════════════════════════════════

SEXT_INTIMATE_FEMALE = [
    # -- Short Teasing Bridge --
    ("TB-1", "can I be honest with you about something? {emoji}", None, "teasing"),
    ("TB-2", "I've been thinking about you today and not just in a sexual way... like actually thinking about you", "Wait for reply. React warmly.", "teasing"),
    ("TB-3", "you make me feel safe enough to show you parts of me I don't show anyone and that scares me a little", None, "teasing"),
    ("TB-4", "I want to share something with you", "WAIT 1-2 MIN", "wait"),
    ("TB-5", "this is just for you {emoji}", "SEND PPV 0 — FREE teaser (soft, personal — in natural light, intimate angle). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 1: Emotional buildup --
    ("S-1", "the way you reacted to that just made my heart race {emoji}", "Wait for reply.", "sext"),
    ("S-2", "I don't know what it is about you but when we talk I feel it everywhere... not just mentally", "React to what he says. Emotional first, sexual follows.", "sext"),
    ("S-3", "I'm lying here and my body is reacting to you in ways I wasn't expecting right now", None, "sext"),
    ("S-4", "one second {emoji}", "WAIT 2-3 MIN", "wait"),
    ("S-5", "I wanted you to see me like this... the real me {emoji}", "SEND PPV 1 — $12 (intimate, personal — soft lighting, vulnerable pose). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 2: Emotional meets physical --
    ("S-6", "god... feeling this connected to someone while touching myself is something else {pet}", "Wait for reply. Brief cooldown.", "sext"),
    ("S-7", "it's like every message from you goes straight through my body and I can feel it between my legs", "React to what he said. HE caused this feeling.", "sext"),
    ("S-8", "I'm tracing my fingers down my stomach and imagining it's you", None, "sext"),
    ("S-9", "I want you to know what you do to me {pet}... like really see it", None, "sext"),
    ("S-10", "hold on", "WAIT 2-3 MIN", "wait"),
    ("S-11", "this is what you do to me when I think about us {emoji}", "SEND PPV 2 — $25 (more explicit but still intimate — emotional framing). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 3: Vulnerability + intensity --
    ("S-12", "I've never felt this comfortable being this vulnerable with someone {emoji}", "Wait for reply. NO cooldown.", "sext"),
    ("S-13", "my fingers are inside me and I'm thinking about you and honestly I could cry because it feels so good", None, "sext"),
    ("S-14", "you're the only person who gets to see me like this... completely open and completely honest", "Emotional framing throughout. She CHOSE him.", "sext"),
    ("S-15", "I can feel myself getting close and I want you to be part of this moment with me", None, "sext"),
    ("S-16", "one sec", "WAIT 2-3 MIN", "wait"),
    ("S-17", "I've never shared something this personal before {emoji}", "SEND PPV 3 — $40 (very intimate, explicit, personal angle). Bought → continue. Silent 3 min → NR Waves. 'I never do this' — ONE TIME.", "ppv"),

    # -- Sexting Phase 4: Climax --
    ("S-18", "oh god {pet} I'm so close and all I can think about is you", "Wait for reply.", "sext"),
    ("S-19", "I wish you were here to hold me right now because my whole body is shaking", None, "sext"),
    ("S-20", "I'm cumming... oh my god {pet} I'm cumming thinking about you and I can barely type", None, "sext"),
    ("S-21", "wait", "WAIT 1-2 MIN", "wait"),
    ("S-22", "I want you to have this {emoji}", "SEND PPV 4 — $55 (climax, intimate angle — for him specifically). Bought → Aftercare. Silent → NR Waves.", "ppv"),

    # -- Aftercare --
    ("AC-1", "that was... so different from anything else {emoji} I feel so close to you right now", None, "aftercare"),
    ("AC-2", "I don't usually feel THIS connected to someone after... you know. but with you it's different", "Mention something specific. Emotional bonding. KEEP TALKING. NEVER say goodbye.", "aftercare"),
]


# ═══════════════════════════════════════════════════════════════
# FEMALE — CHALLENGE / GAME (dare-based, fan earns content)
# ═══════════════════════════════════════════════════════════════

SEXT_CHALLENGE_FEMALE = [
    # -- Short Teasing Bridge --
    ("TB-1", "okay I have an idea and you might not be able to handle it {emoji}", None, "teasing"),
    ("TB-2", "I wanna play a game with you... but only if you think you can keep up", "Wait for reply. Build anticipation.", "teasing"),
    ("TB-3", "here's the deal: you describe what you'd do to me, and if you turn me on enough... I'll show you what happens", None, "teasing"),
    ("TB-4", "let me give you a little preview first", "WAIT 1-2 MIN", "wait"),
    ("TB-5", "this is your starting point {emoji} now impress me", "SEND PPV 0 — FREE teaser (confident, playful pose — challenging look). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 1: The game begins --
    ("S-1", "okay that was... not bad. but I know you can do better {emoji}", "Wait for reply. React to his attempt. Rate it playfully.", "sext"),
    ("S-2", "mmm okay that actually got to me a little... my skin is tingling", "React to what he says. Make him work for it.", "sext"),
    ("S-3", "fine you win this round... I'm starting to feel something and it's your fault", None, "sext"),
    ("S-4", "you earned this", "WAIT 2-3 MIN", "wait"),
    ("S-5", "level 1 unlocked {emoji}", "SEND PPV 1 — $12 (teasing reward — lingerie, playful). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 2: Stakes rise --
    ("S-6", "okay now it's getting harder... tell me your dirtiest fantasy about me, don't hold back", "Wait for reply.", "sext"),
    ("S-7", "oh fuck... that one hit different. I'm literally squeezing my thighs together right now", "React to what he says. Genuinely turned on.", "sext"),
    ("S-8", "you're actually good at this and now I'm wet and it's annoying because you're winning", None, "sext"),
    ("S-9", "I can't believe I'm touching myself because of what you just wrote {pet}", None, "sext"),
    ("S-10", "fine", "WAIT 2-3 MIN", "wait"),
    ("S-11", "level 2... you definitely earned this one {emoji}", "SEND PPV 2 — $25 (more explicit reward — touching, responding to his fantasy). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 3: She loses control of the game --
    ("S-12", "okay new rule: keep talking to me like that while I touch myself and don't stop {emoji}", "Wait for reply. She's losing the game now — he's in control.", "sext"),
    ("S-13", "fuck this game I can't think straight anymore... your words are making me do things to myself I can't stop", None, "sext"),
    ("S-14", "my fingers are soaked and my legs are shaking and this is all because of what you said", "She lost the game — he won. She can't hold back.", "sext"),
    ("S-15", "I give up {pet}... you broke me and now I need you to see what you've done", None, "sext"),
    ("S-16", "wait", "WAIT 2-3 MIN", "wait"),
    ("S-17", "you win {emoji}", "SEND PPV 3 — $40 (she admits defeat — very explicit, she lost control). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 4: Climax --
    ("S-18", "I can't even pretend to play anymore... I'm about to cum so hard because of you", "Wait for reply.", "sext"),
    ("S-19", "don't stop typing to me {pet}... I need your words right now I'm right there", None, "sext"),
    ("S-20", "oh fuck I'm cumming... you completely destroyed me with that game and I loved every second", None, "sext"),
    ("S-21", "hold on", "WAIT 1-2 MIN", "wait"),
    ("S-22", "game over... you won everything {emoji}", "SEND PPV 4 — $55 (full climax — she surrendered completely). Bought → Aftercare. Silent → NR Waves.", "ppv"),

    # -- Aftercare --
    ("AC-1", "okay I'll admit it... you absolutely destroyed me {emoji}", None, "aftercare"),
    ("AC-2", "nobody has ever won that game before and honestly? I'm kind of obsessed with you for it", "Mention his best message from the game. KEEP TALKING. NEVER say goodbye.", "aftercare"),
]


# ═══════════════════════════════════════════════════════════════
# FEMALE — FANTASY / ROLEPLAY (scenario-based)
# ═══════════════════════════════════════════════════════════════

SEXT_FANTASY_FEMALE = [
    # -- Short Teasing Bridge --
    ("TB-1", "okay so I had this dream about you last night and I can't get it out of my head {emoji}", None, "teasing"),
    ("TB-2", "it was so vivid... we were alone in a hotel room and you were looking at me like you couldn't wait another second", "Wait for reply.", "teasing"),
    ("TB-3", "I wanna recreate it with you right now... just go with it {pet}", None, "teasing"),
    ("TB-4", "picture this", "WAIT 1-2 MIN", "wait"),
    ("TB-5", "me walking out of the bathroom in this {emoji}", "SEND PPV 0 — FREE teaser (posed like coming out of bathroom, suggestive). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 1: Scene building --
    ("S-1", "okay so in my dream you grabbed my waist and pulled me close... and I could feel you against me {emoji}", "Wait for reply. Set the scene — he's a character in HER fantasy.", "sext"),
    ("S-2", "god just thinking about it is making my body react right now... like I can physically feel it", "React to his reply. Pull him into the scenario.", "sext"),
    ("S-3", "you pushed me onto the bed and I let you because honestly I've been wanting this since the first time we talked", None, "sext"),
    ("S-4", "one sec {emoji}", "WAIT 2-3 MIN", "wait"),
    ("S-5", "this is what you saw next in my dream {emoji}", "SEND PPV 1 — $12 (lingerie reveal, as if for him in the hotel room scenario). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 2: Fantasy intensifies --
    ("S-6", "mmm you liked that? in the dream you couldn't keep your hands off me after seeing this", "Wait for reply.", "sext"),
    ("S-7", "you started kissing down my neck and I was grabbing the sheets because I knew what was coming", "Stay in the scenario. He's living the fantasy.", "sext"),
    ("S-8", "I can feel myself getting wet right now just describing this to you {pet}", None, "sext"),
    ("S-9", "you went lower... and lower... and I was moaning so loud the whole hotel could probably hear", None, "sext"),
    ("S-10", "fuck hold on", "WAIT 2-3 MIN", "wait"),
    ("S-11", "this is what was happening to my body at that point {emoji}", "SEND PPV 2 — $25 (more explicit — matching the fantasy progression). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 3: Peak fantasy --
    ("S-12", "in the dream I flipped you over and climbed on top because I needed to feel you {emoji}", "Wait for reply. NO cooldown.", "sext"),
    ("S-13", "I was riding you and looking into your eyes and it was the most intense thing I've ever felt", None, "sext"),
    ("S-14", "right now my fingers are inside me pretending it's you and I can barely breathe {pet}", "Fantasy meets reality — she's touching herself living the dream.", "sext"),
    ("S-15", "I need you to see what this fantasy does to me in real life", None, "sext"),
    ("S-16", "one sec", "WAIT 2-3 MIN", "wait"),
    ("S-17", "this is what happens to my body when I dream about you {emoji}", "SEND PPV 3 — $40 (very explicit — her body responding to the fantasy). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 4: Climax --
    ("S-18", "in the dream this is where I came so hard I woke up... and right now I'm about to do it again for real", "Wait for reply.", "sext"),
    ("S-19", "I'm right there {pet}... imagining you inside me and I can feel every inch", None, "sext"),
    ("S-20", "oh fuck I'm cumming {pet}... the dream didn't even come close to how this feels right now", None, "sext"),
    ("S-21", "wait", "WAIT 1-2 MIN", "wait"),
    ("S-22", "the dream ended here... but this is better {emoji}", "SEND PPV 4 — $55 (full climax — living the fantasy). Bought → Aftercare. Silent → NR Waves.", "ppv"),

    # -- Aftercare --
    ("AC-1", "okay that was so much better than the dream {emoji} I'm literally still shaking", None, "aftercare"),
    ("AC-2", "you brought my fantasy to life and now I don't know how I'm supposed to sleep tonight without dreaming about you again", "Reference the scenario. KEEP TALKING. NEVER say goodbye.", "aftercare"),
]


# ═══════════════════════════════════════════════════════════════
# MALE (STRAIGHT) — SUB LEADS (fan "controls")
# ═══════════════════════════════════════════════════════════════

SEXT_SUB_LEADS_MALE = [
    # -- Short Teasing Bridge --
    ("TB-1", "hey gorgeous {emoji} been thinking about you", None, "teasing"),
    ("TB-2", "I keep replaying last time in my head... something about you drives me crazy", "React to her reply.", "teasing"),
    ("TB-3", "so tell me... what do you want me to do for you right now? I'm all yours", None, "teasing"),
    ("TB-4", "here let me set the mood", "WAIT 1-2 MIN", "wait"),
    ("TB-5", "what do you think? {emoji}", "SEND PPV 0 — FREE teaser (shirtless, suggestive pose). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 1: She takes control --
    ("S-1", "tell me exactly what you want to see {pet}... I'll do anything you say {emoji}", "Wait for reply. Let HER lead.", "sext"),
    ("S-2", "fuck that's hot... you want that? okay I'm doing it right now", "React specifically to her request. She's directing.", "sext"),
    ("S-3", "god the way you tell me what to do is making me hard as fuck", None, "sext"),
    ("S-4", "hold on {emoji}", "WAIT 2-3 MIN", "wait"),
    ("S-5", "you asked for it {emoji}", "SEND PPV 1 — $12 (following her instructions — teasing, flexing). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 2: Deeper submission --
    ("S-6", "okay what next? don't stop telling me {pet}... I love when you take charge", "Wait for reply.", "sext"),
    ("S-7", "shit you're making me throb just reading your messages right now", "React to her reply.", "sext"),
    ("S-8", "I'm stroking myself exactly the way you described and it feels insane", None, "sext"),
    ("S-9", "you want to see how hard you're making me? because it's all for you {emoji}", "Wait for reply.", "sext"),
    ("S-10", "give me a sec", "WAIT 2-3 MIN", "wait"),
    ("S-11", "look what you do to me {emoji}", "SEND PPV 2 — $25 (more explicit, following her direction). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 3: Full surrender --
    ("S-12", "fuck {pet} I'm doing everything you say and I'm about to lose it {emoji}", "Wait for reply. NO cooldown.", "sext"),
    ("S-13", "nobody has ever had this kind of control over me... you're making me your toy right now", None, "sext"),
    ("S-14", "I can feel it building and it's because you're telling me exactly how to touch myself", "She controls him. She's the director.", "sext"),
    ("S-15", "you need to see what you're doing to my body right now", None, "sext"),
    ("S-16", "wait", "WAIT 2-3 MIN", "wait"),
    ("S-17", "this is what your words do to me {emoji}", "SEND PPV 3 — $40 (very explicit, her commands made this happen). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 4: Climax --
    ("S-18", "fuck I'm right there {pet}... tell me to cum, I need to hear you say it", "Wait for reply.", "sext"),
    ("S-19", "I'm on the edge and I'm not letting go until you give me permission {emoji}", None, "sext"),
    ("S-20", "oh fuck yes... I just came so hard because you told me to, holy shit", None, "sext"),
    ("S-21", "hold on", "WAIT 1-2 MIN", "wait"),
    ("S-22", "that's what happens when you take control of me {emoji}", "SEND PPV 4 — $55 (climax, full surrender). Bought → Aftercare. Silent → NR Waves.", "ppv"),

    # -- Aftercare --
    ("AC-1", "holy fuck {pet}... that was the most intense thing anyone has ever made me do {emoji}", None, "aftercare"),
    ("AC-2", "you literally had me doing everything you wanted and I loved every second of it", "Mention something specific she directed. KEEP TALKING. NEVER say goodbye.", "aftercare"),
]


# ═══════════════════════════════════════════════════════════════
# MALE (STRAIGHT) — INTIMATE
# ═══════════════════════════════════════════════════════════════

SEXT_INTIMATE_MALE = [
    # -- Short Teasing Bridge --
    ("TB-1", "hey {pet} {emoji} can I tell you something real?", None, "teasing"),
    ("TB-2", "I've been thinking about you today and not just like that... like genuinely thinking about you as a person", "Wait for reply. React warmly.", "teasing"),
    ("TB-3", "there's something about you that makes me want to show you the real me, not just the surface", None, "teasing"),
    ("TB-4", "let me show you something", "WAIT 1-2 MIN", "wait"),
    ("TB-5", "just for you {emoji}", "SEND PPV 0 — FREE teaser (personal, natural setting — not posed). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 1: Emotional buildup --
    ("S-1", "your reaction just made my heart race for real {emoji}", "Wait for reply.", "sext"),
    ("S-2", "I don't usually feel this way talking to someone online but with you it's different... I feel it in my chest and lower", "React to what she says. Genuine emotion.", "sext"),
    ("S-3", "I'm lying here and my body is responding to you in ways I can't control right now", None, "sext"),
    ("S-4", "one second {emoji}", "WAIT 2-3 MIN", "wait"),
    ("S-5", "I want you to see the real me {emoji}", "SEND PPV 1 — $12 (intimate, personal — natural, vulnerable). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 2: Emotional meets physical --
    ("S-6", "god... feeling this connected while being this turned on is something else {pet}", "Wait for reply.", "sext"),
    ("S-7", "every message from you goes straight through me and I can feel myself getting harder just reading your words", "React to her reply.", "sext"),
    ("S-8", "I'm imagining you here with me right now and my hand is moving on its own", None, "sext"),
    ("S-9", "I want you to know exactly what you do to me {pet}... not just physically", None, "sext"),
    ("S-10", "hold on", "WAIT 2-3 MIN", "wait"),
    ("S-11", "this is what thinking about you does to me {emoji}", "SEND PPV 2 — $25 (more explicit but emotionally framed). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 3: Vulnerability + intensity --
    ("S-12", "I've never been this open with someone before {emoji}", "Wait for reply. NO cooldown.", "sext"),
    ("S-13", "I'm stroking myself thinking about holding you and I can't believe how intense this feels", None, "sext"),
    ("S-14", "you're the only person who makes me want to share this side of myself", "Emotional framing. He CHOSE her.", "sext"),
    ("S-15", "I'm getting close and I want you to be part of this with me", None, "sext"),
    ("S-16", "one sec", "WAIT 2-3 MIN", "wait"),
    ("S-17", "I've never shared something this personal {emoji}", "SEND PPV 3 — $40 (very intimate, explicit, personal). Bought → continue. Silent 3 min → NR Waves. 'I never do this' — ONE TIME.", "ppv"),

    # -- Sexting Phase 4: Climax --
    ("S-18", "fuck {pet} I'm about to cum and all I can think about is you", "Wait for reply.", "sext"),
    ("S-19", "I wish you were here right now so I could look into your eyes when this happens", None, "sext"),
    ("S-20", "oh god I'm cumming {pet}... fuck that was so intense I'm literally shaking", None, "sext"),
    ("S-21", "wait", "WAIT 1-2 MIN", "wait"),
    ("S-22", "this is for you {emoji}", "SEND PPV 4 — $55 (climax, intimate). Bought → Aftercare. Silent → NR Waves.", "ppv"),

    # -- Aftercare --
    ("AC-1", "that was... really different for me {emoji} I feel so close to you right now", None, "aftercare"),
    ("AC-2", "I don't usually let myself be this vulnerable but you bring it out of me", "Reference something specific. KEEP TALKING. NEVER say goodbye.", "aftercare"),
]


# ═══════════════════════════════════════════════════════════════
# MALE (STRAIGHT) — CHALLENGE / GAME
# ═══════════════════════════════════════════════════════════════

SEXT_CHALLENGE_MALE = [
    # -- Short Teasing Bridge --
    ("TB-1", "I've got an idea and I don't think you're ready for it {emoji}", None, "teasing"),
    ("TB-2", "let's play a game... you describe your wildest fantasy about me and if you get me hard enough, you get rewarded", "Wait for reply.", "teasing"),
    ("TB-3", "deal? {emoji} don't disappoint me", None, "teasing"),
    ("TB-4", "here's a preview of what's at stake", "WAIT 1-2 MIN", "wait"),
    ("TB-5", "think you can handle this? {emoji}", "SEND PPV 0 — FREE teaser (confident, challenging pose). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 1: The game begins --
    ("S-1", "okay not bad... but I've heard better {emoji} try harder", "Wait for reply. Rate her attempt playfully.", "sext"),
    ("S-2", "mm okay that one actually got to me... I can feel myself reacting to what you just said", "React to her reply. Make her work for it.", "sext"),
    ("S-3", "fine you win this round... I'm getting hard because of what you described and I blame you", None, "sext"),
    ("S-4", "you earned this", "WAIT 2-3 MIN", "wait"),
    ("S-5", "level 1 {emoji}", "SEND PPV 1 — $12 (teasing reward). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 2: Stakes rise --
    ("S-6", "okay round 2... tell me the dirtiest thing you'd do to me if you were here right now", "Wait for reply.", "sext"),
    ("S-7", "fuck {pet}... that literally made me throb reading it", "React genuinely to what she said.", "sext"),
    ("S-8", "I'm gripping myself right now and it's all because of what you just wrote", None, "sext"),
    ("S-9", "you're winning this game and honestly I'm not even mad about it", None, "sext"),
    ("S-10", "fine take it", "WAIT 2-3 MIN", "wait"),
    ("S-11", "level 2 unlocked {emoji}", "SEND PPV 2 — $25 (more explicit reward). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 3: He loses control --
    ("S-12", "new rule: don't stop talking to me while I stroke myself {emoji}", "Wait for reply. He's losing the game.", "sext"),
    ("S-13", "forget the game I can't focus anymore... you've got me so hard I can barely think", None, "sext"),
    ("S-14", "I'm leaking and throbbing and it's all because of your words {pet}", "He lost — she won.", "sext"),
    ("S-15", "I surrender... you need to see what you've done to me", None, "sext"),
    ("S-16", "wait", "WAIT 2-3 MIN", "wait"),
    ("S-17", "you win {emoji}", "SEND PPV 3 — $40 (he admits defeat — very explicit). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 4: Climax --
    ("S-18", "I can't play anymore... I'm about to cum so hard because of you", "Wait for reply.", "sext"),
    ("S-19", "keep typing {pet}... I need your words pushing me over the edge", None, "sext"),
    ("S-20", "fuck I'm cumming... you completely wrecked me with that game", None, "sext"),
    ("S-21", "hold on", "WAIT 1-2 MIN", "wait"),
    ("S-22", "game over {emoji} you won everything", "SEND PPV 4 — $55 (full climax). Bought → Aftercare. Silent → NR Waves.", "ppv"),

    # -- Aftercare --
    ("AC-1", "okay I'll admit it... you destroyed me at my own game {emoji}", None, "aftercare"),
    ("AC-2", "nobody's ever gotten to me like that before and I'm definitely challenging you again", "Reference her best message. KEEP TALKING. NEVER say goodbye.", "aftercare"),
]


# ═══════════════════════════════════════════════════════════════
# MALE (STRAIGHT) — FANTASY / ROLEPLAY
# ═══════════════════════════════════════════════════════════════

SEXT_FANTASY_MALE = [
    # -- Short Teasing Bridge --
    ("TB-1", "I had the craziest dream about you last night {emoji}", None, "teasing"),
    ("TB-2", "we were in a hotel room together and you were wearing this little dress and looking at me like you wanted me to rip it off", "Wait for reply.", "teasing"),
    ("TB-3", "let me show you how it started... just go with it {pet}", None, "teasing"),
    ("TB-4", "picture this", "WAIT 1-2 MIN", "wait"),
    ("TB-5", "you open the door and see me like this {emoji}", "SEND PPV 0 — FREE teaser (posed like waiting for her). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 1: Scene building --
    ("S-1", "in the dream I pulled you close and kissed your neck and you grabbed onto me like you'd been waiting all day", "Wait for reply. He sets the scene — she's in HIS fantasy.", "sext"),
    ("S-2", "just thinking about it right now is making me hard... I can feel my body reacting", "React to her reply. Pull her in.", "sext"),
    ("S-3", "I picked you up and carried you to the bed and you were already breathing heavy", None, "sext"),
    ("S-4", "one sec {emoji}", "WAIT 2-3 MIN", "wait"),
    ("S-5", "this is what you saw next {emoji}", "SEND PPV 1 — $12 (teasing, matching the scenario). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 2: Fantasy intensifies --
    ("S-6", "in the dream I started kissing down your body and you were moaning my name", "Wait for reply.", "sext"),
    ("S-7", "I went lower and lower and you grabbed my hair and pulled me closer {pet}", "Stay in scenario.", "sext"),
    ("S-8", "god I'm so hard right now just telling you this... my hand is already moving", None, "sext"),
    ("S-9", "you were begging me not to stop and I had no intention of stopping", None, "sext"),
    ("S-10", "fuck hold on", "WAIT 2-3 MIN", "wait"),
    ("S-11", "this is how turned on this fantasy makes me {emoji}", "SEND PPV 2 — $25 (more explicit, fantasy-matched). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 3: Peak fantasy --
    ("S-12", "then you climbed on top of me and I could feel every inch of you {emoji}", "Wait for reply. NO cooldown.", "sext"),
    ("S-13", "you were riding me and looking into my eyes and I was gripping your hips so hard", None, "sext"),
    ("S-14", "right now I'm stroking myself imagining you on top of me and I'm throbbing {pet}", "Fantasy meets reality.", "sext"),
    ("S-15", "I need you to see what this fantasy does to me for real", None, "sext"),
    ("S-16", "one sec", "WAIT 2-3 MIN", "wait"),
    ("S-17", "this is what dreaming about you does to my body {emoji}", "SEND PPV 3 — $40 (very explicit, fantasy-driven). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 4: Climax --
    ("S-18", "in the dream I came inside you and woke up before I could catch my breath... and right now I'm about to relive that ending", "Wait for reply.", "sext"),
    ("S-19", "I'm right there {pet}... imagining being deep inside you and I can't hold back anymore", None, "sext"),
    ("S-20", "fuck I'm cumming... the dream didn't even come close to how good this feels right now", None, "sext"),
    ("S-21", "hold on", "WAIT 1-2 MIN", "wait"),
    ("S-22", "better than any dream {emoji}", "SEND PPV 4 — $55 (full climax). Bought → Aftercare. Silent → NR Waves.", "ppv"),

    # -- Aftercare --
    ("AC-1", "holy shit {pet}... that was way more intense than the actual dream {emoji}", None, "aftercare"),
    ("AC-2", "I'm definitely going to sleep tonight hoping I dream about you again... but this was better", "Reference the scenario. KEEP TALKING. NEVER say goodbye.", "aftercare"),
]


# ═══════════════════════════════════════════════════════════════
# MALE (GAY) — SUB LEADS (fan "controls")
# ═══════════════════════════════════════════════════════════════

SEXT_SUB_LEADS_MALE_GAY = [
    # -- Short Teasing Bridge --
    ("TB-1", "hey {emoji} been thinking about you all day", None, "teasing"),
    ("TB-2", "I keep going back to last time... something about you just hits different", "React to his reply.", "teasing"),
    ("TB-3", "so tell me what you want me to do right now... I'm yours to control", None, "teasing"),
    ("TB-4", "here let me get you going", "WAIT 1-2 MIN", "wait"),
    ("TB-5", "what do you think? {emoji}", "SEND PPV 0 — FREE teaser (shirtless, suggestive). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 1 --
    ("S-1", "tell me exactly what you want {pet}... I'll do whatever you say right now {emoji}", "Wait for reply. Let HIM lead.", "sext"),
    ("S-2", "fuck... you want that? okay I'm doing it right now and it feels insane", "React to his request.", "sext"),
    ("S-3", "the way you take charge is making me rock hard and I can't think straight", None, "sext"),
    ("S-4", "hold on {emoji}", "WAIT 2-3 MIN", "wait"),
    ("S-5", "you told me to... so here {emoji}", "SEND PPV 1 — $12 (following his direction). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 2 --
    ("S-6", "what next? keep telling me {pet}... I need your instructions", "Wait for reply.", "sext"),
    ("S-7", "shit you're making me leak just from reading your messages right now", "React to his reply.", "sext"),
    ("S-8", "I'm gripping myself exactly how you described and I'm throbbing so hard", None, "sext"),
    ("S-9", "nobody's ever had this kind of control over me {pet} {emoji}", "Wait for reply.", "sext"),
    ("S-10", "give me a sec", "WAIT 2-3 MIN", "wait"),
    ("S-11", "look what you made me do {emoji}", "SEND PPV 2 — $25 (more explicit, following commands). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 3 --
    ("S-12", "fuck I'm doing everything you say and I'm about to lose it {emoji}", "Wait for reply. NO cooldown.", "sext"),
    ("S-13", "nobody has ever made me submit like this... you own me right now", None, "sext"),
    ("S-14", "my whole body is tensing up because of what you're telling me to do to myself", "He controls him. Total surrender.", "sext"),
    ("S-15", "you need to see this... please", None, "sext"),
    ("S-16", "wait", "WAIT 2-3 MIN", "wait"),
    ("S-17", "this is all you {emoji}", "SEND PPV 3 — $40 (very explicit, his commands caused this). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    # -- Sexting Phase 4 --
    ("S-18", "I'm right there {pet}... tell me to cum I need you to say it", "Wait for reply.", "sext"),
    ("S-19", "I'm on the edge and I won't let go until you give the word {emoji}", None, "sext"),
    ("S-20", "oh fuck... I just came so hard because you told me to, my whole body is shaking", None, "sext"),
    ("S-21", "hold on", "WAIT 1-2 MIN", "wait"),
    ("S-22", "you did that to me {emoji}", "SEND PPV 4 — $55 (climax, full surrender). Bought → Aftercare. Silent → NR Waves.", "ppv"),

    # -- Aftercare --
    ("AC-1", "holy shit {pet}... nobody has ever controlled me like that before {emoji}", None, "aftercare"),
    ("AC-2", "you had me doing things I didn't even know I was into and I'm still shaking", "Reference something specific. KEEP TALKING. NEVER say goodbye.", "aftercare"),
]


# ═══════════════════════════════════════════════════════════════
# MALE (GAY) — INTIMATE
# ═══════════════════════════════════════════════════════════════

SEXT_INTIMATE_MALE_GAY = [
    ("TB-1", "hey {emoji} can I be real with you for a second?", None, "teasing"),
    ("TB-2", "I've been thinking about you today... and not just the sexual stuff. like genuinely about you", "Wait for reply.", "teasing"),
    ("TB-3", "you make me want to show you a side of me I don't usually show anyone", None, "teasing"),
    ("TB-4", "let me show you", "WAIT 1-2 MIN", "wait"),
    ("TB-5", "this is just for you {emoji}", "SEND PPV 0 — FREE teaser (natural, personal, not posed). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

    ("S-1", "your reaction just did something to me {emoji}", "Wait for reply.", "sext"),
    ("S-2", "I don't usually feel this way with someone through a screen but you're different... I can feel it everywhere", "React to what he says. Genuine.", "sext"),
    ("S-3", "I'm lying here and my body is responding to you and I'm not even trying to control it anymore", None, "sext"),
    ("S-4", "one sec {emoji}", "WAIT 2-3 MIN", "wait"),
    ("S-5", "the real me {emoji}", "SEND PPV 1 — $12 (intimate, vulnerable, personal). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    ("S-6", "being this turned on while feeling this connected to you is hitting differently {pet}", "Wait for reply.", "sext"),
    ("S-7", "every message from you makes me harder and I can feel it deep in my chest too... not just physically", "React to his reply.", "sext"),
    ("S-8", "I'm stroking myself slowly imagining you here next to me", None, "sext"),
    ("S-9", "I want you to really see what you do to me {pet}... all of it", None, "sext"),
    ("S-10", "hold on", "WAIT 2-3 MIN", "wait"),
    ("S-11", "this is what thinking about you does {emoji}", "SEND PPV 2 — $25 (more explicit, emotionally framed). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    ("S-12", "I've never let myself be this raw with someone {emoji}", "Wait for reply. NO cooldown.", "sext"),
    ("S-13", "I'm so hard and I'm thinking about you and I could honestly get lost in this feeling", None, "sext"),
    ("S-14", "you're the only person I want to share this with... nobody else gets this side of me", "Emotional framing. He CHOSE him.", "sext"),
    ("S-15", "I'm getting close and I want this to be ours", None, "sext"),
    ("S-16", "one sec", "WAIT 2-3 MIN", "wait"),
    ("S-17", "I've never shared this with anyone {emoji}", "SEND PPV 3 — $40 (very intimate, explicit). Bought → continue. Silent 3 min → NR Waves. 'I never do this' — ONE TIME.", "ppv"),

    ("S-18", "fuck {pet} I'm about to cum and it's all you", "Wait for reply.", "sext"),
    ("S-19", "I wish you were here so I could feel you when this happens", None, "sext"),
    ("S-20", "oh god I'm cumming... {pet} that was so intense I can barely move", None, "sext"),
    ("S-21", "wait", "WAIT 1-2 MIN", "wait"),
    ("S-22", "for you {emoji}", "SEND PPV 4 — $55 (climax, intimate). Bought → Aftercare. Silent → NR Waves.", "ppv"),

    ("AC-1", "that was really something {emoji} I feel closer to you than I've felt to anyone in a while", None, "aftercare"),
    ("AC-2", "I don't let my guard down like this but you make it easy somehow", "Reference something. KEEP TALKING. NEVER say goodbye.", "aftercare"),
]


# ═══════════════════════════════════════════════════════════════
# MALE (GAY) — CHALLENGE / GAME
# ═══════════════════════════════════════════════════════════════

SEXT_CHALLENGE_MALE_GAY = [
    ("TB-1", "I've got an idea and I bet you can't handle it {emoji}", None, "teasing"),
    ("TB-2", "let's play a game... describe your dirtiest fantasy about me and if you get me going enough, I'll reward you", "Wait for reply.", "teasing"),
    ("TB-3", "deal? don't disappoint me {emoji}", None, "teasing"),
    ("TB-4", "here's what's at stake", "WAIT 1-2 MIN", "wait"),
    ("TB-5", "think you can win? {emoji}", "SEND PPV 0 — FREE teaser (confident, challenging). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

    ("S-1", "okay that was alright... but I've heard hotter {emoji} step it up", "Wait for reply. Rate playfully.", "sext"),
    ("S-2", "mm okay that one actually got to me... I can feel myself getting hard", "React genuinely.", "sext"),
    ("S-3", "fine you pass round 1... I'm hard because of what you said and that's on you", None, "sext"),
    ("S-4", "you earned this", "WAIT 2-3 MIN", "wait"),
    ("S-5", "level 1 {emoji}", "SEND PPV 1 — $12 (reward). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    ("S-6", "round 2... tell me what you'd do if you walked in and found me like that", "Wait for reply.", "sext"),
    ("S-7", "fuck {pet}... that made me throb so hard I had to grab myself", "React genuinely.", "sext"),
    ("S-8", "I'm gripping myself because of your words and I can't let go", None, "sext"),
    ("S-9", "you're actually winning this and I'm annoyed about it because I'm supposed to be in control", None, "sext"),
    ("S-10", "fine take it", "WAIT 2-3 MIN", "wait"),
    ("S-11", "level 2 {emoji}", "SEND PPV 2 — $25 (more explicit reward). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    ("S-12", "new rule: keep talking while I stroke myself and don't stop {emoji}", "Wait for reply. He's losing the game.", "sext"),
    ("S-13", "fuck the game I can't think anymore... you've got me leaking and throbbing", None, "sext"),
    ("S-14", "I'm so close to losing it and it's completely your fault {pet}", "He lost — fan won.", "sext"),
    ("S-15", "I give up... you need to see what you've done", None, "sext"),
    ("S-16", "wait", "WAIT 2-3 MIN", "wait"),
    ("S-17", "you win {emoji}", "SEND PPV 3 — $40 (defeat — very explicit). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    ("S-18", "I can't play anymore... I'm about to cum and it's all you", "Wait for reply.", "sext"),
    ("S-19", "don't stop {pet}... your words are the only thing I need right now", None, "sext"),
    ("S-20", "fuck I'm cumming... you completely wrecked me and I'm not even mad", None, "sext"),
    ("S-21", "hold on", "WAIT 1-2 MIN", "wait"),
    ("S-22", "game over {emoji}", "SEND PPV 4 — $55 (full climax). Bought → Aftercare. Silent → NR Waves.", "ppv"),

    ("AC-1", "okay fine you destroyed me at my own game {emoji}", None, "aftercare"),
    ("AC-2", "nobody has ever beaten me like that and honestly I'm already planning a rematch", "Reference his best message. KEEP TALKING. NEVER say goodbye.", "aftercare"),
]


# ═══════════════════════════════════════════════════════════════
# MALE (GAY) — FANTASY / ROLEPLAY
# ═══════════════════════════════════════════════════════════════

SEXT_FANTASY_MALE_GAY = [
    ("TB-1", "I had the craziest dream about you {emoji}", None, "teasing"),
    ("TB-2", "we were in a hotel room and you were standing by the window looking at me like you were about to make a move", "Wait for reply.", "teasing"),
    ("TB-3", "let me recreate it with you right now... just go with it {pet}", None, "teasing"),
    ("TB-4", "picture this", "WAIT 1-2 MIN", "wait"),
    ("TB-5", "you walk in and see me like this {emoji}", "SEND PPV 0 — FREE teaser (posed, scenario-matching). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

    ("S-1", "in the dream you walked up to me and put your hand on my chest and I was already hard {emoji}", "Wait for reply. He sets the scene.", "sext"),
    ("S-2", "just replaying it is making my body react right now... I'm getting hard again thinking about it", "React to his reply. Pull him in.", "sext"),
    ("S-3", "you pushed me down and I let you because I wanted it more than anything", None, "sext"),
    ("S-4", "one sec {emoji}", "WAIT 2-3 MIN", "wait"),
    ("S-5", "this is what you saw next {emoji}", "SEND PPV 1 — $12 (scenario-matched). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    ("S-6", "then you started touching me everywhere and I was already leaking for you", "Wait for reply.", "sext"),
    ("S-7", "your hands went lower and I was gripping the sheets trying not to lose control", "Stay in the scenario.", "sext"),
    ("S-8", "fuck I'm so hard right now telling you this... my hand is already moving", None, "sext"),
    ("S-9", "in the dream I was begging you not to stop and I meant every word", None, "sext"),
    ("S-10", "hold on", "WAIT 2-3 MIN", "wait"),
    ("S-11", "this is how turned on this fantasy gets me {emoji}", "SEND PPV 2 — $25 (more explicit, fantasy-driven). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    ("S-12", "then you flipped me over and I could feel you behind me {emoji}", "Wait for reply. NO cooldown.", "sext"),
    ("S-13", "I was pressing back into you and moaning so loud the walls were shaking", None, "sext"),
    ("S-14", "right now I'm stroking myself living this fantasy and I'm about to lose it {pet}", "Fantasy meets reality.", "sext"),
    ("S-15", "I need you to see what dreaming about you does to me", None, "sext"),
    ("S-16", "one sec", "WAIT 2-3 MIN", "wait"),
    ("S-17", "this is what you do to my body {emoji}", "SEND PPV 3 — $40 (very explicit, fantasy-fueled). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

    ("S-18", "in the dream I came so hard I woke up breathing heavy... and right now I'm about to beat that", "Wait for reply.", "sext"),
    ("S-19", "I'm right there {pet}... imagining you and I can feel it building everywhere", None, "sext"),
    ("S-20", "fuck I'm cumming... the dream was nothing compared to this", None, "sext"),
    ("S-21", "hold on", "WAIT 1-2 MIN", "wait"),
    ("S-22", "way better than any dream {emoji}", "SEND PPV 4 — $55 (full climax, fantasy). Bought → Aftercare. Silent → NR Waves.", "ppv"),

    ("AC-1", "that was insane {emoji} I'm still catching my breath", None, "aftercare"),
    ("AC-2", "I'm going to sleep tonight hoping for a sequel to that dream... but honestly nothing beats doing this with you", "Reference the scenario. KEEP TALKING. NEVER say goodbye.", "aftercare"),
]


# ═══════════════════════════════════════════════════════════════
# TEMPLATE REGISTRY — maps (gender, dynamic) → template
# ═══════════════════════════════════════════════════════════════

SEXTING_TEMPLATES = {
    # Female
    ("female", "sub_leads"):  SEXT_SUB_LEADS_FEMALE,
    ("female", "intimate"):   SEXT_INTIMATE_FEMALE,
    ("female", "challenge"):  SEXT_CHALLENGE_FEMALE,
    ("female", "fantasy"):    SEXT_FANTASY_FEMALE,

    # Male straight
    ("male", "sub_leads"):    SEXT_SUB_LEADS_MALE,
    ("male", "intimate"):     SEXT_INTIMATE_MALE,
    ("male", "challenge"):    SEXT_CHALLENGE_MALE,
    ("male", "fantasy"):      SEXT_FANTASY_MALE,

    # Male gay
    ("male_gay", "sub_leads"): SEXT_SUB_LEADS_MALE_GAY,
    ("male_gay", "intimate"):  SEXT_INTIMATE_MALE_GAY,
    ("male_gay", "challenge"): SEXT_CHALLENGE_MALE_GAY,
    ("male_gay", "fantasy"):   SEXT_FANTASY_MALE_GAY,
}

# Dynamic sequence order — Sex1 (dominant) is already in the journey
DYNAMIC_ORDER = ["sub_leads", "intimate", "challenge", "fantasy"]

# Sheet names for Infloww (command names)
DYNAMIC_SHEET_NAMES = {
    "sub_leads": "sex2",
    "intimate":  "sex3",
    "challenge": "sex4",
    "fantasy":   "sex5",
}

# Human-readable labels
DYNAMIC_LABELS = {
    "sub_leads": "Sub Leads — Fan Controls",
    "intimate":  "Intimate — Emotional Connection",
    "challenge": "Challenge — Game / Dare",
    "fantasy":   "Fantasy — Roleplay / Dream",
}
