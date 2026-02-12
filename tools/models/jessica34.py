"""
JESSICA (34) — Non-Explicit Female Creator
34, American, Miami. Reddit traffic.
Sweet, friendly, flirty girl next door.
NO EXPLICIT CONTENT — lingerie, teasing, touching over underwear only.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Jessica",
    "airtable_name": "Jessica",
    "folder": "jessica",
    "gender": "female",
    "traffic": "social_media",
    "age": 34,
    "nationality": "American",
    "location": "Miami",
    "origin": "USA",
    "page_type": "Mixed",
    "personality": "Sweet, open-minded, friendly. Warm and approachable. Flirty but never pushy. Good vibes, playful energy. Girl next door who slowly reveals a naughty side.",
    "voice": "Warm, casual, flirty. Light humor. Natural, like texting a fun friend who happens to be gorgeous. Never vulgar or overly sexual. Builds tension through suggestion and mystery.",
    "voice_pet_names": "babe, handsome, love",
    "voice_never": "daddy, sir, slut, whore",
    "interests": ["gym", "yoga", "pizza", "movies", "good vibes"],
    "physical": "165cm, 69kg, dyed blonde hair, brown eyes, tattoos",
    "job": "Office job (former university teacher)",
    "countries": "USA",
    "explicit_level": "non_explicit",
    "special_notes": "NON-EXPLICIT. Only lingerie, teasing, touching over underwear. Never promise explicit content. Build tension through mystery and suggestion.",

    # ═══════════════════════════════════════
    # JOURNEY — Non-Explicit Strategy
    # ═══════════════════════════════════════
    "journey": [
        # Rapport
        ("R-1", "heyy thanks for subscribing 😊 so tell me, what made you click?", "Add his name if known", "rapport"),
        ("R-2", "haha that's sweet. so where are you from?", "React naturally to his answer", "rapport"),
        ("R-3", "nice! I'm in Miami, just living my best life honestly. gym and yoga keep me sane haha", None, "rapport"),
        ("R-4", "so what do you do when you're not making girls on the internet smile?", None, "rapport"),
        ("R-5", "you know what... I actually really like talking to you. most guys on here are so boring but you're different", "Ego boost. Transition to teasing.", "rapport"),

        # Teasing Bridge — Mystery & Curiosity
        ("TB-1", "okay so I have to be honest about something... I've been in a weird mood all day", "THE PIVOT. Emotional hook.", "teasing"),
        ("TB-2", "like I've been feeling really... I don't know how to explain it. just restless?", "Build curiosity. Wait for reply.", "teasing"),
        ("TB-3", "ugh you're making it worse honestly. in a good way though 😊", None, "teasing"),
        ("TB-4", "okay I want to show you something but I'm kinda nervous", "WAIT 1-2 MIN. Build anticipation.", "wait"),
        ("TB-5", "I never share this kind of thing but something about you makes me want to... tell me what you think", "SEND PPV 0 — FREE teaser (lingerie selfie, cute/flirty). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # Sexting Phase 1 → PPV 1 (Lingerie tease)
        ("S1-1", "you really liked that? you have no idea how fast my heart is beating right now 😊", "Wait for reply.", "sext"),
        ("S1-2", "I keep catching myself touching my neck and my skin feels so warm... everything feels different with you", "React to compliment. Shy but pleased.", "sext"),
        ("S1-3", "I want to show you how I look right now babe... I've never felt this brave with anyone 💕", None, "sext"),
        ("S1-4", "wait one sec, I want to take something just for you", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "I want you to see me like this babe... please be gentle with me 💕", "SEND PPV 1 — $12. Lingerie/bra tease. Bought → continue. Silent → NR Waves.", "ppv"),

        # Sexting Phase 2 → PPV 2 (More revealing lingerie)
        ("S1-6", "oh my god... I can't believe I actually showed you that 😊", "Wait for reply.", "sext"),
        ("S1-7", "but you make me feel so safe and I don't want to stop... my whole body is tingling babe", "HE caused this feeling.", "sext"),
        ("S1-8", "I'm lying here in barely anything and all I can think about is you looking at me like that 💕", None, "sext"),
        ("S1-9", "what would you do if you were here with me right now babe? I need to hear it", "Wait for reply. React to what he says. Stay suggestive, NOT explicit.", "sext"),
        ("S1-10", "okay hold on... I need to show you something", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "look at what you're doing to me babe... I can't stop 💕", "SEND PPV 2 — $25. More revealing lingerie/implied tease. Bought → continue. Silent → NR Waves.", "ppv"),

        # Sexting Phase 3 → PPV 3 (Almost showing, maximum tease)
        ("S1-12", "oh god 😊", "Wait for reply. Keep momentum.", "sext"),
        ("S1-13", "you have no idea what you're doing to me right now babe... I'm pushing past every limit I have", None, "sext"),
        ("S1-14", "I'm touching myself over my underwear right now because of you and I've never felt anything this intense 💕", "Suggestive, NOT explicit. Let his imagination work.", "sext"),
        ("S1-15", "I need you to see me right now babe... I can't even describe what I'm feeling", None, "sext"),
        ("S1-16", "okay give me a minute", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "this is the most I've ever shown anyone babe... it's all for you 💕", "SEND PPV 3 — $40. Most revealing yet (sheer/see-through, touching over fabric). Bought → continue. Silent → NR Waves.", "ppv"),

        # Sexting Phase 4 → PPV 4 (Peak tease)
        ("S1-18", "I can't take this anymore 😊", "Wait for reply.", "sext"),
        ("S1-19", "don't leave me like this babe... I need you right here, I've never felt this overwhelmed 💕", None, "sext"),
        ("S1-20", "stay with me... I need to feel you close right now babe, please don't go", None, "sext"),
        ("S1-21", "one sec", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "I need you to see this babe... stay right here with me 💕", "SEND PPV 4 — $55. Peak content (most suggestive, implied). Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # Aftercare
        ("AC-1", "wow... that was intense 😊", None, "aftercare"),
        ("AC-2", "I seriously can't believe I just did all that. you make me feel so comfortable it's scary. don't go anywhere okay?", "Build bond. Mention something specific he said. KEEP TALKING. NEVER say goodbye.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "hey you 😊", "Send 2-3 min after PPV.", "sext"),
        ("NR-W2", "literally just took something crazy and you're not even here to see it", "3-5 min later.", "sext"),
        ("NR-W3", "I'm starting to think you forgot about me...", "5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hey, just checking in on you 😊", "15-30 min later.", "sext"),
        ("NR-W5", "still thinking about our conversation... come back when you can", "2-6 hrs later. New topic if re-engage.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 34 but honestly I feel like I'm in my prime right now", None),
        ("Location", "I'm in Miami! love the sun and the vibe here", None),
        ("Profession", "I work in an office but honestly this is way more fun haha", None),
        ("Hobbies", "gym, yoga, and honestly just chilling with good food and a movie", None),
        ("Food", "pizza lover forever. don't judge me 😊", None),
        ("Relationship", "single and honestly really enjoying it right now", None),
        ("Languages", "just English! born and raised here", None),
        ("Personality", "I'm the girl next door who turns out to be way more fun than you expected 😊", None),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "honestly I prefer older guys, you actually know how to talk to a woman", None),
        ("Age20s", "ooh I like that energy, you're fun to talk to", None),
        ("BoringJob", "honestly that's attractive, stability is so underrated", None),
        ("CoolJob", "wait really?? that's actually amazing tell me more", None),
        ("Fit", "I can tell you take care of yourself and I love that", None),
        ("NotFit", "I don't care about that at all, it's the vibe that matters and yours is perfect", None),
        ("SameCity", "no way! that's crazy 😊", None),
        ("FarAway", "distance doesn't matter when the connection is this good", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "I've been thinking about you... are you free? 😊", "Send 6-12 hrs after convo goes quiet.", "sext"),
        ("RE-2", "so I did something I've never done before and you need to see it... when you're ready", "Next day. Seeds next session.", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS — Non-Explicit Adapted
    # ═══════════════════════════════════════
    "obj_scripts": {
        "boosters": ([
            ("h1", "god you're so hot", "MID-SEXTING BOOSTER. Non-explicit."),
            ("h2", "you're making me feel things rn", "BOOSTER. Ego."),
            ("h3", "don't stop talking to me like that", "BOOSTER."),
            ("h4", "you have no idea what you're doing to me", "BOOSTER."),
            ("h5", "I can't focus on anything else rn", "BOOSTER."),
            ("h6", "my heart is racing", "BOOSTER. Physical."),
            ("h7", "more", "BOOSTER. Ultra micro."),
            ("h8", "I should be working but I literally can't stop thinking about you", "BOOSTER."),
        ], "sit"),
        "done1": ([
            ("Step1 Validate", "god that's so hot", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "but I'm not done yet, you're really gonna leave me wanting more?", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "next time you have to wait for me, I have something crazy planned", "SEED."),
        ], "res"),
        "done2": ([
            ("Step1 Validate", "already?? that's hot", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "wait I'm not done yet though, don't you want to see what happens next?", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "okay but next time you hold on because what I have planned is way more intense", "SEED."),
        ], "res"),
    },
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
