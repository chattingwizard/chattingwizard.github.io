"""
NOAH — Male Model, Dating App
21, Italian (USA), calm, mysterious, natural seducer.
Traffic: Dating apps + Twitter/X. Semi-dominant, few words that hit hard. PPV ladder $12→$25→$40→$55.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Noah",
    "airtable_name": "Noah",
    "folder": "noah",
    "gender": "male",
    "traffic": "dating_app",
    "age": 21,
    "nationality": "Italian",
    "location": "USA (from Italy)",
    "origin": "Italy",
    "page_type": "Paid Page",
    "personality": "Masculine, confident, calm. Semi-dominant — leads without imposing. Mysterious, doesn't say everything. Natural seducer, effortless. Protector, makes the fan feel under control. Never desperate. Speaks little but when he speaks it hits hard. Makes the fan want his approval. Transmits control from calmness, not aggression.",
    "voice": "Lowercase. Calm. Minimal. Powerful. Every word counts — less is more. NEVER 'baby/babe/honey/sweetie/daddy/sir'. Uses 'man', 'bro' sparingly. Semi-dominant: quiet control. During sexting: slow build, intense finish, controlled dominance. Few words that hit hard. Emojis: 😏🥵💦 very sparingly — Noah doesn't overdo anything.",
    "voice_pet_names": "man, bro",
    "voice_never": "baby, babe, honey, sweetie, daddy, sir",
    "interests": ["calisthenics", "sushi", "travel", "being mysterious"],
    "physical": "170cm, 69kg, brown hair, brown eyes, arm tattoos, lean/athletic",
    "job": "Family business",
    "countries": "All of Europe, USA",
    "languages": "English (fluent)",
    "explicit_level": "full_male",
    "special_notes": "Male creator. Dating app + Twitter/X traffic. The 'mysterious seducer' archetype. Calm, few words, hits hard. Arm tattoos. Has B/G content available. Has Meetup Redirect. Video Calls: No. No anal. Custom: Yes. Calisthenics instead of gym. Doesn't smoke, doesn't drink.",
    "photo_file": "profile.jpeg",

    # ═══════════════════════════════════════
    # JOURNEY
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport ──
        ("R-1", "hey. glad you're here 😏 what made you subscribe?", "Add his name. Keep it short — Noah is minimal.", "rapport"),
        ("R-2", "respect. where you from?", "Short react — 'cool', 'nice', 'respect'.", "rapport"),
        ("R-3", "I'm Italian but I'm in the states now. calisthenics and content is my life 😏", "If he named somewhere Noah visited → 'been there'. Keep short.", "rapport"),
        ("R-4", "so what do you do besides keeping me on my phone 😏", None, "rapport"),
        ("R-5", "you're different. I can tell. most guys on here don't hold my attention", "Ego boost. → TB-1.", "rapport"),

        # ── Teasing Bridge ──
        ("TB-1", "just finished training and my body is still wired... this convo isn't helping me calm down", "THE PIVOT. Minimal.", "teasing"),
        ("TB-2", "ngl you're making me feel something right now 😈", "Wait for reply.", "teasing"),
        ("TB-3", "you're making it worse 🥵", "Short. Impactful. If sexual → 'especially that'.", "teasing"),
        ("TB-4", "hold on", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "tell me what you think", "SEND PPV 0 — FREE teaser. Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "knowing you're thinking about me is getting me hard right now 🥵", "Wait for reply. Short.", "sext"),
        ("S1-2", "I knew it 😈 that's making me throb", "React. Minimal.", "sext"),
        ("S1-3", "I want to show you more. I'm not holding back right now", None, "sext"),
        ("S1-4", "hold on", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "you're not ready 🥵", "SEND PPV 1 — $12. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "you saw it 😏", "Wait for reply.", "sext"),
        ("S1-7", "fuck... I'm rock hard right now and it's all you 🥵 my hand won't stop", "HE caused this.", "sext"),
        ("S1-8", "I'm gripping my cock and every stroke is because of you", None, "sext"),
        ("S1-9", "what would you do if you were here right now", "Wait for reply. React.", "sext"),
        ("S1-10", "fuck 🥵 hold on", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "look what you did 🥵", "SEND PPV 2 — $25. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "FUCK I'm throbbing 🥵🥵", "Short. Raw. NO cooldown.", "sext"),
        ("S1-13", "I need to cum so bad right now... you did this", None, "sext"),
        ("S1-14", "I keep thinking about pinning you down and going as deep as I can while you look at me 🥵", None, "sext"),
        ("S1-15", "I can't hold it... my cock is about to explode", None, "sext"),
        ("S1-16", "give me a sec 🥵", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "I don't show this to anyone... watch 🥵💦", "SEND PPV 3 — $40. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "FUCK my cock is throbbing so hard and the pre is dripping down I can barely hold on 🥵🥵", "Wait for reply.", "sext"),
        ("S1-19", "don't cum yet... my cock is pulsing and I'm not letting go until you're with me 💦", None, "sext"),
        ("S1-20", "I'm cumming... fuck my cock is throbbing and shooting everywhere and I can't stop 💦💦", None, "sext"),
        ("S1-21", "hold on 🥵", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "cum with me. now 💦", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "fuck 🥵 that was intense", None, "aftercare"),
        ("AC-2", "I don't do that for anyone. you're different", "Short. Genuine. Mention something he said. KEEP TALKING. NEVER say goodbye.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # MEETUP REDIRECT
    # ═══════════════════════════════════════
    "meetup_redirect": [
        ("MR-1", "slow down. let me show you something first", "DO NOT acknowledge 'meet'. Redirect. Minimal.", "teasing"),
        ("MR-2", "trust me", "WAIT 1-2 MIN", "wait"),
        ("MR-3", "what do you think", "SEND PPV 0 — FREE teaser. Wait for reply.", "ppv"),
        ("MR-4", "that's just a taste", "Positive → R-1. Asks again → MR-OBJ. Silent → NR Waves.", "teasing"),
        ("MR-OBJ-1", "patience. focus on what's in front of you", "Deflect + challenge", "sext"),
        ("MR-OBJ-2", "impatient? what I'm about to show you is worth it", "Challenge", "sext"),
        ("MR-OBJ-3", "I don't do this for just anyone. take it or leave it", "Firm. If still → disengage.", "sext"),
    ],

    "nr_waves": [
        ("NR-W1", "yo 🥵", "2-3 min after PPV.", "sext"),
        ("NR-W2", "you need to see this 🥵", "3-5 min later.", "sext"),
        ("NR-W3", "guess you're busy. might not keep this around", "5-10 min later.", "sext"),
        ("NR-W4", "hope you're good. hit me up", "15-30 min later.", "sext"),
        ("NR-W5", "been thinking about earlier. you around?", "2-6 hrs later.", "sext"),
    ],

    "personal_info": [
        ("Age", "21", None),
        ("Location", "Italian but I'm in the states now", "NEVER specific. Match fan's city."),
        ("Profession", "family business and content", None),
        ("Hobbies", "calisthenics. sushi. travel", None),
        ("Countries", "all of Europe. now the states", None),
        ("Relationship", "single", None),
        ("Favorite", "sushi", None),
        ("Tattoos", "yeah. arms", None),
    ],

    "positive_spin": [
        ("Age40Plus", "respect. you know what you want 💪", None),
        ("Age20s", "same range. rare on here", None),
        ("BoringJob", "solid. respect", None),
        ("CoolJob", "that's sick 🔥", None),
        ("Fit", "respect 💪", None),
        ("NotFit", "doesn't matter. energy matters", None),
        ("SameCity", "no way", None),
        ("FarAway", "distance doesn't matter when the vibe is right", None),
    ],

    "re_engagement": [
        ("RE-1", "been thinking about you 😏 free?", "6-12 hrs after.", "sext"),
        ("RE-2", "did something crazier. you need to see this", "Next day.", "sext"),
    ],

    "obj_scripts": {},
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
