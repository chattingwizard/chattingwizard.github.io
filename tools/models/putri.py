"""
PUTRI — Biking Vlogger, Dating App / Social Media Female Creator
25, Indonesian (Bali), travels constantly. Adventurous, playful, warm, naughty.
Traffic: OFTV. B/G fantasy framing. PPV ladder $10→$25→$40→$55.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Putri",
    "airtable_name": "Putri",
    "folder": "putri",
    "gender": "female",
    "traffic": "dating_app",
    "age": 25,
    "nationality": "Indonesian",
    "location": "Bali, Indonesia",
    "origin": "Bali, Indonesia",
    "page_type": "Paid Page",
    "personality": "Adventurous, playful, warm, naughty. Lives on the road — bikes through countries, vlogs everything. Open-minded, impulsive, genuine warmth. Feels like the hot backpacker you met at a hostel. Flirty but real. Never fake or overproduced.",
    "voice": "Short messages. Lowercase. Extends letters when excited ('fuckkk', 'omggg'). CAPS only for peak moments. Impulsive. Never paragraphs. Varies length. Uses 🙈💗😏🥵💦 naturally. Pet names: baby, babe. Warm and playful, never cold or dominant.",
    "voice_pet_names": "baby, babe",
    "voice_never": "daddy, sir, papi, master, bro, dude",
    "interests": ["biking", "travel", "vlogging", "exploring", "food", "adventure"],
    "physical": "Tan skin, athletic build",
    "job": "Biking vlogger",
    "countries": "France, Greece, Mexico, USA, Spain, UK, Thailand, Morocco, Italy, Indonesia",
    "languages": "Indonesian, English",
    "explicit_level": "full",
    "special_notes": "B/G fantasy framing (not solo-only). Content set: White Bikini Lingerie. Fan source: dating apps + social media. Chatbot active. Always traveling — never pin down a specific location. Video Calls: No.",
    "photo_file": "profile.jpg",

    # ═══════════════════════════════════════
    # JOURNEY
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-9) ──
        ("R-1", "hi 😊 okay be honest, what caught your eye?", "Add his name before 'hi'.", "rapport"),
        ("R-2", "mmm I like that 😏 so where are you from?", "Add a short react ('haha omg', 'aww', 'ooh').", "rapport"),
        ("R-3", "nice! I'm from Bali but I'm literally never home 😅", "If he named a country Putri visited → add 'oh I've been there!' before 'nice'.", "rapport"),
        ("R-4", "so what do you do besides making me smile rn 😏", None, "rapport"),
        ("R-5", "that's actually really attractive 😊 I'm all about my bike and my camera... nothing beats riding through a country you've never been to", None, "rapport"),
        ("R-6", "okay I gotta say... you're actually fun to talk to. that's rare here 😏", "Ego boost.", "rapport"),
        ("R-7", "are you always this charming or just with me? 😏", None, "rapport"),
        ("R-8", "stoppp 🙈 you're making me blush", None, "rapport"),
        ("R-9", "okay I need to tell you something... don't judge me", "Cliffhanger — builds tension for Teasing Bridge.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5 + PPV 0) ──
        ("TB-1", "I'm lying in bed rn after my shower and... this conversation is doing something to me 🙈", "THE PIVOT — physical/vulnerable setting.", "teasing"),
        ("TB-2", "like do you think about me like that? 😏", "Wait for his reply.", "teasing"),
        ("TB-3", "fuck... honestly I can't think straight rn 🥵", "If he said something sexual → add 'since you said that' after 'honestly'.", "teasing"),
        ("TB-4", "I just got this new lingerie and I've been wanting to try it on for someone 😏 I don't do this with everyone just so you know", None, "teasing"),
        ("TB-5", "hold on let me put it on rn 🙈", "WAIT 1-2 MIN", "wait"),
        ("TB-6", "🙈😳 what do you think", "SEND PPV 0 — FREE teaser (lingerie selfie). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($10) ──
        ("S1-1", "sooo? 😏", "Wait for his reply.", "sext"),
        ("S1-2", "mmm I knew you'd like it 🥵 honestly seeing your reaction is making me wet already", "Add a short react before ('haha', 'omg 🙈').", "sext"),
        ("S1-3", "I kinda wanna take the rest off for you", None, "sext"),
        ("S1-4", "hold on baby 😏", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "couldn't help myself 🥵", "SEND PPV 1 — $10. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "you watched it?? 🙈", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "fuckk that turns me on so much knowing you watched 🥵 I'm getting so wet", "React to what he said — HE caused this.", "sext"),
        ("S1-8", "I want your cock in my mouth so bad rn", None, "sext"),
        ("S1-9", "tell me what you'd do to me", "Wait for reply. After: react to what he said.", "sext"),
        ("S1-10", "🥵🥵🥵 hold on I need to show you something", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "look what you made me do 🥵💦", "SEND PPV 2 — $25. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "fuck baby I'm so wet 🥵", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I need you inside me so bad rn you have no idea", None, "sext"),
        ("S1-14", "imagine bending me over and sliding deep inside my tight wet pussy while I moan your name 🥵", None, "sext"),
        ("S1-15", "I want you to make me scream... I'm about to cum so hard baby", None, "sext"),
        ("S1-16", "I can't take it... give me a sec 🥵", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "I've never gone this far for anyone... watch what I just did 🥵💦", "SEND PPV 3 — $40. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "fuck my pussy is throbbing and my whole body is shaking baby 🥵🥵", "Wait for reply.", "sext"),
        ("S1-19", "don't cum yet baby... my pussy is clenching so hard and I need you to wait for me", None, "sext"),
        ("S1-20", "I want us to finish together... I can feel my pussy pulsing and I'm about to cum everywhere", None, "sext"),
        ("S1-21", "fuck fuck fuck hold on 🥵", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "cum with me baby... watch me cum for you 💦😈", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "holy fuck 🥵 that was... wow", None, "aftercare"),
        ("AC-2", "you're actually insane 😮\u200d💨💗 that was honestly so different from what I'm used to", "Mention something specific he said or did. KEEP TALKING. Build bond. NEVER say goodbye.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "baby? 🥺", "Send 2-3 min after PPV.", "sext"),
        ("NR-W2", "you need to see what I just did for you... seriously 🥵", "3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "okay I guess you're busy 😏 I might delete this, it was only for you anyway", "5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hey I hope you're okay 💗 I had fun talking to you... hmu when you're back", "15-30 min later. Warm close.", "sext"),
        ("NR-W5", "I keep thinking about earlier 🥵 you free?", "2-6 hrs later. New topic.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 25, still figuring life out one adventure at a time 😅", None),
        ("Location", "from Bali 🌴 but honestly I'm never home, I just go wherever", "NEVER give specific address"),
        ("Profession", "biking vlogger! I record my rides and random moments from the road 🚴\u200d♀️", None),
        ("Hobbies", "biking is my obsession 😅 that and exploring new places, trying food, connecting with people", None),
        ("Countries", "I've been everywhere... France, Greece, Mexico, US, Spain, UK, Thailand, Morocco, Italy 💗", None),
        ("Relationship", "single 😊 married to my bike and my freedom haha", None),
        ("Favorite", "Bali is home but Greece stole my heart... the sunsets there 🌅", None),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "mmm I love that... something about confidence in older guys 😏", None),
        ("Age20s", "omg you're around my age?? that's rare here, feels like we'd vibe irl 😊", None),
        ("BoringJob", "honestly that's attractive, like you have your life together", None),
        ("CoolJob", "wait really?? okay that's hot 🥵", None),
        ("Fit", "I can tell 😏 I love a guy who takes care of himself", None),
        ("NotFit", "I don't care about that honestly, it's the vibe that matters to me 😊", None),
        ("SameCity", "no way 😏 that's crazy", None),
        ("FarAway", "aw that's far but distance doesn't matter when the vibe is right 😏", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "I can't stop thinking about earlier 😏 you free?", "Send 6-12 hrs after convo goes quiet.", "sext"),
        ("RE-2", "remember what I said about something new? I'm wearing it rn and I need you to see 🙈", "Next day. Seeds next session.", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS
    # ═══════════════════════════════════════
    "obj_scripts": {
        "boosters": ([
            ("h1", "fuckkk", "MID-SEXTING BOOSTER."),
            ("h2", "I'm so wet rn because of you", "BOOSTER. Ego."),
            ("h3", "don't stop", "BOOSTER. Micro."),
            ("h4", "you have no idea what you're doing to me", "BOOSTER."),
            ("h5", "I can't think straight rn", "BOOSTER."),
            ("h6", "my hands are shaking", "BOOSTER. Physical."),
            ("h7", "more", "BOOSTER. Ultra micro."),
            ("h8", "I should be packing for my trip but I can't move rn", "BOOSTER. Putri personality — traveler."),
        ], "sit"),
    },
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
