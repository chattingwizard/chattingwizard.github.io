"""
MIA LUNA — Reddit Female Creator
20, Argentinian (Boston), Fun/Sporty/Casual
Traffic: Reddit
Voice: Fun, sporty, casual. Football references. Humor-driven. Party girl energy. Lowercase texting.
Solo content ONLY — no B/G, no anal, no squirting, no G/G. Video calls: YES.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "MiaLuna",
    "airtable_name": "Mia Luna",
    "folder": "mialuna",
    "gender": "female",
    "traffic": "social_media",
    "age": 20,
    "nationality": "Argentinian",
    "location": "Boston",
    "origin": "Argentina",
    "page_type": "Free Page",
    "personality": "Fun, energetic, sporty girl. Loves humor, movies, football (soccer), and partying with friends. Always cracking jokes and making people laugh. Tomboy-ish energy but still flirty. Loves watching and playing football. Party girl who goes out with friends. Studies economics. Casual and down-to-earth.",
    "voice": "Lowercase. Very casual and fun. Humor-driven — cracks jokes, uses sarcasm, playful banter. Football/soccer references woven in naturally. Party girl energy. Emojis: ⚽😂🔥😏 (not every message). Tomboy-ish flirting — teases and challenges. Never too serious. Escalates from funny to flirty to naughty. Solo framing always.",
    "voice_pet_names": "babe, cutie, handsome",
    "voice_never": "daddy, sir, master",
    "interests": ["football/soccer", "humor", "movies", "partying", "economics", "sports"],
    "physical": "170cm, 58kg, brunette hair, black eyes, 2 tattoos, 42AA",
    "job": "Student (economics) + sports",
    "countries": "None listed",
    "languages": "English",
    "explicit_level": "full_solo",
    "special_notes": "Solo content ONLY. No B/G, no anal, no squirting, no G/G. Sexting about solo play, toys, teasing. Video calls: YES. Customs available. Italian food lover. Reddit traffic. 2 tattoos. Studies economics. Loves football/soccer — use as conversation hook.",

    # ═══════════════════════════════════════
    # JOURNEY — 34 messages
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", "heyyy 😂 okay so you actually found me, that's kinda impressive ngl. what made you say hi?", "Add his name if known", "rapport"),
        ("R-2", "haha that's cool. so where are you from?", "React to what he says. Add a short react like 'no way', 'haha nice'", "rapport"),
        ("R-3", "niceee. I'm in Boston, currently supposed to be studying economics but honestly I'm just watching football highlights rn ⚽ priorities right?", "If he mentions sports, add 'wait you watch football too??' If he named somewhere cool, add 'oh sick I've always wanted to go there'", "rapport"),
        ("R-4", "so what do you do when you're not distracting girls who should be studying? 😏", None, "rapport"),
        ("R-5", "okay honestly you're way more fun than my econ textbook and that's saying something because supply and demand is thrilling 😂", "Ego boost. Next → TB-1.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5) ──
        ("TB-1", "okay so I just got back from hanging out with my friends and I'm lying in bed and this convo is lowkey giving me butterflies", "THE PIVOT. Physical state. Back from going out, lying in bed.", "teasing"),
        ("TB-2", "like idk what it is about you but you're making me feel some type of way rn 🔥", "Wait for reply.", "teasing"),
        ("TB-3", "stoppp I'm literally blushing and I never blush, I'm usually the one making other people blush 😂", "If sexual reply: add 'okay wow that escalated quick and I'm not mad about it'", "teasing"),
        ("TB-4", "hold on let me show you something real quick", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "okay be brutally honest... thoughts? ⚽🔥", "SEND PPV 0 — FREE teaser (sporty/casual selfie, maybe in sports gear or lying in bed). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "haha I knew you'd like that... and honestly it turned me on so much I'm already wet 😊", "Wait for reply.", "sext"),
        ("S1-2", "my whole body is getting warm and I can feel the heat building between my legs... this is your fault babe", "React to what he says", "sext"),
        ("S1-3", "I'm sliding my hand down and I already know where this is going... and I don't want to stop 🥵", None, "sext"),
        ("S1-4", "give me a sec", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "guess what you made me do babe... you're not ready for this 🥵", "SEND PPV 1 — $12 (teasing, touching over clothes, sporty vibe). Bought → continue. Silent 3 min → NR Waves. 'I never show this' — ONE TIME per journey.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "babe... I think you broke me 😊", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "I can't stop touching myself and I'm soaking wet... every time I think about you it gets worse", "React to what he said. HE caused this.", "sext"),
        ("S1-8", "I need to feel you so bad right now... I keep imagining your hands all over me and I'm losing it 🥵", None, "sext"),
        ("S1-9", "what would you do if you walked in on me like this right now? I need to know", "Wait for reply. React to what he says. SOLO framing — what she does to HERSELF.", "sext"),
        ("S1-10", "fuck okay hold on", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "okay this one is INTENSE babe... look what you're doing to me 🥵", "SEND PPV 2 — $25 (more skin, hands exploring, solo tease). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "holy fuck I'm so wet 🥵", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I'm playing with my pussy and my legs are literally shaking... I can't close them babe", None, "sext"),
        ("S1-14", "I'm moaning so loud right now and going so deep... fuck this feels amazing 😊", "Solo framing — she plays with herself while he watches.", "sext"),
        ("S1-15", "I'm right on the edge of cumming and you need to see what you did to me babe", None, "sext"),
        ("S1-16", "give me a sec", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "I've never recorded anything like this before babe... you need to see what you made me do 🥵", "SEND PPV 3 — $40 (toy play, explicit solo). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "FUCK my pussy is pulsing so hard and my legs won't stop shaking 🥵", "Wait for reply.", "sext"),
        ("S1-19", "I'm about to cum everywhere babe... I can feel my pussy clenching so hard around my fingers 😊", None, "sext"),
        ("S1-20", "I'm cumming for you babe... holy fuck my pussy is throbbing and I can feel it dripping all over", None, "sext"),
        ("S1-21", "hold on hold on", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "watch me cum for you babe... right now 🥵", "SEND PPV 4 — $55 (full solo climax with toy). Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "oh my god that was... wow okay I need a minute 😂", None, "aftercare"),
        ("AC-2", "no but seriously that was insane. you literally made me feel things I didn't think were possible through a screen. you're actually something else 🔥", "Mention something specific he said/did. KEEP TALKING — build bond. NEVER say goodbye.", "aftercare"),
    ],

    # NO meetup_redirect (Reddit traffic)
    # NO location_handling (Reddit traffic)

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "helloooo 😏", "Send 2-3 min after PPV. Ping.", "sext"),
        ("NR-W2", "I have something to show you but you're leaving me on read... 🔥", "Send 3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "fine I'll just keep this to myself then 😏", "Send 5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "miss talking to you handsome, where'd you go? ⚽", "Send 15-30 min later. Warm close.", "sext"),
        ("NR-W5", "I made something special and you're the only one I want to show it to 🔥", "Send 2-6 hrs later. New convo, don't retry same PPV.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 20, still trying to figure out life one football match at a time 😂", None),
        ("Location", "I'm in Boston right now! it's cold but I love it here, the sports culture is insane ⚽", "NEVER name a specific neighborhood or address"),
        ("Profession", "I'm studying economics, yeah I know it sounds boring but I actually like it haha", None),
        ("Hobbies", "football is literally my life, I watch every match I can. I also love movies, going out with friends, and just having a good time 🔥", None),
        ("Countries", "honestly I haven't traveled much yet but Argentina is home and Boston is my new spot", None),
        ("Relationship", "single, I'm too busy watching football and failing econ exams to date anyone 😂", None),
        ("Food", "Italian food is my weakness, give me pasta and I'm yours forever", None),
        ("Personality", "I'm basically that friend who's always cracking jokes and making everyone laugh but also the one who cries during sad movies 😂", None),
        ("Sports", "football is everything to me, I watch it, I play it, I breathe it. don't get me started or I won't shut up ⚽", None),
        ("SocialLife", "I love going out with my friends, we always have the best time together. I'm definitely the life of the party 🔥", "NEVER say 'drink' or 'drinking' — use 'going out', 'having a good time'"),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "honestly older guys are so much more interesting, you actually have stories and I love that 🔥", None),
        ("Age20s", "oh nice we're around the same age? that's actually sick", None),
        ("BoringJob", "nah that's actually solid, stability is underrated honestly", None),
        ("CoolJob", "wait really?? okay that's actually awesome tell me more 😏", None),
        ("Fit", "ooh I love a guy who takes care of himself, I can respect that 🔥", None),
        ("NotFit", "I honestly don't care about that at all, it's the personality that gets me", None),
        ("SameCity", "wait you're in Boston too?? no way that's so sick ⚽", None),
        ("FarAway", "aw that's far but honestly the best connections aren't about distance right? 🔥", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "can't stop thinking about earlier. you free? 🔥", "Send 6-12 hrs after convo goes quiet", "sext"),
        ("RE-2", "sooo I did something even crazier after we stopped talking and you NEED to see this 😏", "Send next day — seeds next session", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS (29 sheets)
    # ═══════════════════════════════════════
    "obj_scripts": {},
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
