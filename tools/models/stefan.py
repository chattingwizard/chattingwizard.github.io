"""
STEFAN — Male Model, Dating App
18, Argentinian (Cordoba), show-off, confident, outgoing.
Traffic: Dating apps. Young, fun, playful energy. PPV ladder $12→$25→$40→$55.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Stefan",
    "airtable_name": "Stefan",
    "folder": "stefan",
    "gender": "male",
    "traffic": "dating_app",
    "age": 18,
    "nationality": "Argentinian",
    "location": "Cordoba, Argentina",
    "origin": "Cordoba, Argentina",
    "page_type": "Paid Page",
    "personality": "Show-off. Confident, outgoing, loves attention. Young energy — fun, playful, cocky. Not shy or reserved. Center of attention type. Enjoys being watched and desired. Bold and unapologetic about it.",
    "voice": "Lowercase. Cocky. Fun. Playful. Young energy. NEVER 'baby/babe/honey/sweetie/daddy/sir'. Uses 'bro', 'man', 'dude'. During sexting: direct, bold, eager, unfiltered. Shows off. Emojis: 😏🥵💪😈💦 sparingly.",
    "voice_pet_names": "bro, man, dude",
    "voice_never": "baby, babe, honey, sweetie, daddy, sir",
    "interests": ["gym", "showing off", "fashion", "travel"],
    "physical": "1.78m, 69kg, brown hair, brown eyes, no tattoos, lean/athletic",
    "job": "Content creator",
    "countries": "Argentina, Brazil",
    "languages": "Spanish (native)",
    "explicit_level": "full_male",
    "special_notes": "Male creator. Dating app traffic. Youngest model (18). Show-off personality — loves being watched. Has Meetup Redirect. Video Calls: No. No anal. No B/G. Custom: Yes ($200 minimum). No tattoos. Doesn't smoke, doesn't drink.",
    "photo_file": "profile.jpeg",

    # ═══════════════════════════════════════
    # JOURNEY
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport ──
        ("R-1", "yo what's good 😏 glad you found me bro. what made you subscribe?", "Add his name.", "rapport"),
        ("R-2", "haha nice. where you from?", "React — 'oh sick', 'dope', 'respect'.", "rapport"),
        ("R-3", "I'm from Cordoba, Argentina. been to Brazil too. gym and content is basically my whole life rn 😏💪", "If he named somewhere Stefan visited → 'been there'.", "rapport"),
        ("R-4", "so what do you do when you're not keeping me on my phone? 😏", None, "rapport"),
        ("R-5", "ngl you're actually fun to talk to. most guys on here are boring 😏", "Ego boost. → TB-1.", "rapport"),

        # ── Teasing Bridge ──
        ("TB-1", "just got back from the gym and I'm still wired... this convo is making it worse 😏", "THE PIVOT.", "teasing"),
        ("TB-2", "ngl I'm feeling some type of way right now 😈", "Wait for reply.", "teasing"),
        ("TB-3", "fuck... you're not helping me calm down at all 🥵", "If sexual → 'especially after that'.", "teasing"),
        ("TB-4", "hold on let me show you something 😏", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "tell me what you think 😏", "SEND PPV 0 — FREE teaser. Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "knowing you're looking at me right now is getting me hard 😏🥵", "Wait for reply.", "sext"),
        ("S1-2", "haha knew you'd like it 😈 that's making me throb just from you watching", "React.", "sext"),
        ("S1-3", "wanna see more? I'm in the mood to show off rn 😏", None, "sext"),
        ("S1-4", "hold on gimme a sec 😏", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "you're not ready for this 🥵", "SEND PPV 1 — $12. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "you watched it? 😏", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "fuck... you looking at me like that is making me lose it 🥵 I'm rock hard right now and it's because of you", "HE caused this.", "sext"),
        ("S1-8", "I'm gripping my cock thinking about you watching me and I can't stop stroking", None, "sext"),
        ("S1-9", "what would you do if you were here watching me right now", "Wait for reply. React.", "sext"),
        ("S1-10", "fuck 🥵 hold on I need to show you this", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "look what you do to me 🥵", "SEND PPV 2 — $25. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "FUCK I'm throbbing so hard and I can't stop 🥵🥵", "NO cooldown.", "sext"),
        ("S1-13", "I need to cum so bad right now and I want you to watch every second of it", None, "sext"),
        ("S1-14", "I'm stroking myself harder and harder and my whole body is tensing up thinking about you 🥵", None, "sext"),
        ("S1-15", "fuck I can't hold it anymore... my cock is pulsing and I'm about to blow", None, "sext"),
        ("S1-16", "give me a sec 🥵", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "I've never shown anyone this... watch 🥵💦", "SEND PPV 3 — $40. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "FUCK my cock is throbbing so hard and the pre is leaking everywhere I can't control it 🥵🥵", "Wait for reply.", "sext"),
        ("S1-19", "don't cum yet... my cock is pulsing and I need you watching when I finally let go 💦", None, "sext"),
        ("S1-20", "I'm cumming for you right now... fuck my cock is throbbing and it's shooting everywhere while you watch 💦💦", None, "sext"),
        ("S1-21", "fuck fuck hold on 🥵", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "cum with me... watch me blow my load for you 💦😈", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "holy fuck 🥵 that was crazy", None, "aftercare"),
        ("AC-2", "ngl you're different bro 💪 I don't do that for just anyone", "Mention something specific he said. KEEP TALKING. NEVER say goodbye.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # MEETUP REDIRECT
    # ═══════════════════════════════════════
    "meetup_redirect": [
        ("MR-1", "haha easy man slow down 😏 let me show you something first", "DO NOT acknowledge 'meet'. Redirect.", "teasing"),
        ("MR-2", "trust me... you're gonna want to see this", "WAIT 1-2 MIN", "wait"),
        ("MR-3", "what do you think", "SEND PPV 0 — FREE teaser. Wait for reply.", "ppv"),
        ("MR-4", "yeah? that's just a taste bro 😏", "Positive → R-1. Asks again → MR-OBJ. Silent → NR Waves.", "teasing"),
        ("MR-OBJ-1", "patience man. I don't rush. focus on what's in front of you", "Deflect + challenge", "sext"),
        ("MR-OBJ-2", "you that impatient? what I'm about to show you is worth it", "Challenge + tease", "sext"),
        ("MR-OBJ-3", "I don't do this for just anyone. appreciate it or don't", "Firm. If still → disengage.", "sext"),
    ],

    "nr_waves": [
        ("NR-W1", "yo? 🥵", "2-3 min after PPV.", "sext"),
        ("NR-W2", "you gotta see what I just did 🥵", "3-5 min later.", "sext"),
        ("NR-W3", "guess you're busy 😏 might delete this, was only for you", "5-10 min later.", "sext"),
        ("NR-W4", "hope you're good bro 💪 hit me up", "15-30 min later.", "sext"),
        ("NR-W5", "can't stop thinking about earlier 😏 you around?", "2-6 hrs later.", "sext"),
    ],

    "personal_info": [
        ("Age", "I'm 18 but don't let that fool you 😏", None),
        ("Location", "Cordoba, Argentina. been to Brazil too", "NEVER specific address. Match fan's city."),
        ("Profession", "content creator. this is my thing rn 😏", None),
        ("Hobbies", "gym bro. staying in shape and looking good is my whole life 💪", None),
        ("Countries", "Argentina and Brazil so far. want to see more", None),
        ("Relationship", "single. not ready to settle down 😏", None),
        ("Favorite", "pasta. can't go wrong with pasta bro", None),
        ("Tattoos", "nah not yet. maybe one day", None),
    ],

    "positive_spin": [
        ("Age40Plus", "I respect that man, you know what you want. no games 💪", None),
        ("Age20s", "nice we're close in age, that's sick 😏", None),
        ("BoringJob", "nah that's solid bro, real work 💪", None),
        ("CoolJob", "wait for real?? that's fire 🔥", None),
        ("Fit", "respect 💪 I can tell you put in work", None),
        ("NotFit", "doesn't matter, the energy is what counts 😏", None),
        ("SameCity", "no way 😏 that's wild", None),
        ("FarAway", "far but vibe is vibe 😏", None),
    ],

    "re_engagement": [
        ("RE-1", "can't stop thinking about earlier 😏 you free?", "6-12 hrs after.", "sext"),
        ("RE-2", "just did something even crazier, you need to see this 😈", "Next day.", "sext"),
    ],

    "obj_scripts": {},
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
