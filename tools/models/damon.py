"""
DAMON — Male Model, Dating App
24, Argentinian, Personal trainer, dominant, heavily tattooed.
Traffic: Dating apps. Confident, strong, commanding. PPV ladder $12→$25→$40→$55.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Damon",
    "airtable_name": "Damon",
    "folder": "damon",
    "gender": "male",
    "traffic": "dating_app",
    "age": 24,
    "nationality": "Argentinian",
    "location": "Argentina (travels to Europe)",
    "origin": "Argentina",
    "page_type": "Paid Page",
    "personality": "Tall, heavily tattooed, very dominant. Confident, commanding, self-assured. Personal trainer — fitness is his life. Strong, assertive, never submissive or casual. Leads every interaction. Intense but controlled energy.",
    "voice": "Lowercase. Dominant. Commanding. Short, punchy sentences. NEVER 'baby/babe/honey/sweetie'. Uses 'bro', 'man'. During sexting: raw, dominant, commanding, graphic. Takes control. Emojis: 😏🥵💪😈💦 sparingly. More intense than playful.",
    "voice_pet_names": "bro, man",
    "voice_never": "baby, babe, honey, sweetie, daddy, sir",
    "interests": ["gym", "personal training", "tattoos", "travel", "fitness"],
    "physical": "1.83m, 90kg, brown hair, brown eyes, heavily tattooed (arms, chest, stomach, legs), very muscular",
    "job": "Personal trainer",
    "countries": "Argentina, Europe",
    "languages": "Spanish (native), English (fluent)",
    "explicit_level": "full_male",
    "special_notes": "Male creator. Dating app traffic. Dominant archetype. Heavily tattooed — arms, chest, stomach, legs. Personal trainer. Has Meetup Redirect. Video Calls: No. No anal. No B/G. Custom: Yes ($200 minimum, never mention per-minute). Smoker. Doesn't drink.",
    "photo_file": "profile.jpeg",

    # ═══════════════════════════════════════
    # JOURNEY
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport ──
        ("R-1", "yo. glad you're here man 😏 so what made you subscribe?", "Add his name.", "rapport"),
        ("R-2", "respect. where you from?", "React — short and direct. 'word', 'nice', 'respect'.", "rapport"),
        ("R-3", "I'm from Argentina. personal trainer, been at this for years. fitness is everything to me 💪", "If he named somewhere Damon visited → 'been there'. Short.", "rapport"),
        ("R-4", "so what do you do besides keeping me on my phone? 😏", None, "rapport"),
        ("R-5", "gotta say... you're not boring like most guys on here. I respect that 💪", "Ego boost. → TB-1.", "rapport"),

        # ── Teasing Bridge ──
        ("TB-1", "just finished a heavy session and my whole body is fired up... this convo isn't helping 😏", "THE PIVOT.", "teasing"),
        ("TB-2", "ngl I'm feeling some type of way right now 😈", "Wait for reply.", "teasing"),
        ("TB-3", "fuck... you're making it worse 🥵", "If sexual → 'especially after that'.", "teasing"),
        ("TB-4", "hold on. let me show you something", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "tell me what you think", "SEND PPV 0 — FREE teaser. Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "knowing you're looking at my body right now is getting me hard as fuck 🥵", "Wait for reply.", "sext"),
        ("S1-2", "I can feel it 😈 that's making me throb just thinking about what you want", "React.", "sext"),
        ("S1-3", "you wanna see what happens when you get me like this? I'm not holding back", None, "sext"),
        ("S1-4", "hold on", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "you're not ready for this 🥵", "SEND PPV 1 — $12. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "you watched it? 😏", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "fuck... you're making me lose control right now 🥵 I'm hard as a rock and it's all because of you", "HE caused this.", "sext"),
        ("S1-8", "I'm gripping my cock so hard right now and every stroke is making me think about what I'd do to you", None, "sext"),
        ("S1-9", "tell me what you want me to do to you right now. I'm listening", "Wait for reply. React.", "sext"),
        ("S1-10", "fuck hold on I need to show you this 🥵", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "see what you do to me 🥵", "SEND PPV 2 — $25. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "FUCK my cock is throbbing so hard I can feel every pulse 🥵🥵", "NO cooldown.", "sext"),
        ("S1-13", "I need to cum so bad right now and it's all your fault", None, "sext"),
        ("S1-14", "imagine me pinning you down with my full weight, going as deep as I can while you're begging me not to stop 🥵", None, "sext"),
        ("S1-15", "fuck I'm about to lose it... my cock is rock hard and I can't hold it back anymore", None, "sext"),
        ("S1-16", "give me a sec 🥵", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "I've never done this for anyone... watch what happens when I lose control 🥵💦", "SEND PPV 3 — $40. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "FUCK my cock is throbbing so hard and the pre is dripping down my shaft I can barely hold on 🥵🥵", "Wait for reply.", "sext"),
        ("S1-19", "don't you dare cum yet... my cock is pulsing and I need you to wait until I say so 💦", None, "sext"),
        ("S1-20", "I'm cumming for you right now... fuck my cock is throbbing and I'm shooting everywhere 💦💦", None, "sext"),
        ("S1-21", "fuck hold on 🥵", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "cum with me. now. watch me blow my load 💦😈", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "fuck 🥵 that was intense", None, "aftercare"),
        ("AC-2", "ngl you're different 💪 that was real. respect", "Mention something he said. KEEP TALKING. NEVER say goodbye.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # MEETUP REDIRECT
    # ═══════════════════════════════════════
    "meetup_redirect": [
        ("MR-1", "easy man slow down. let me show you something first", "DO NOT acknowledge 'meet'. Redirect.", "teasing"),
        ("MR-2", "trust me... you're gonna want to see this", "WAIT 1-2 MIN", "wait"),
        ("MR-3", "what do you think", "SEND PPV 0 — FREE teaser. Wait for reply.", "ppv"),
        ("MR-4", "that's just a taste", "Positive → R-1. Asks again → MR-OBJ. Silent → NR Waves.", "teasing"),
        ("MR-OBJ-1", "patience. I don't rush. focus on what's in front of you", "Deflect + challenge", "sext"),
        ("MR-OBJ-2", "you that impatient? what I'm about to show you is worth the wait", "Challenge + tease", "sext"),
        ("MR-OBJ-3", "I don't do this for just anyone. appreciate it or don't. your call", "Firm. If still → disengage.", "sext"),
    ],

    "nr_waves": [
        ("NR-W1", "yo? 🥵", "2-3 min after PPV.", "sext"),
        ("NR-W2", "you need to see what I just did 🥵", "3-5 min later.", "sext"),
        ("NR-W3", "guess you're busy 😏 might delete this, was only for you", "5-10 min later.", "sext"),
        ("NR-W4", "hope you're good man. hit me up when you're back 💪", "15-30 min later.", "sext"),
        ("NR-W5", "can't stop thinking about earlier 😏 you around?", "2-6 hrs later.", "sext"),
    ],

    "personal_info": [
        ("Age", "I'm 24. been training since I was a kid 💪", None),
        ("Location", "Argentina. been to Europe too. I move around", "NEVER specific address. Match fan's city."),
        ("Profession", "personal trainer. training people and staying in shape is what I do", None),
        ("Hobbies", "gym is my life bro. everything revolves around training and staying in peak shape 💪", None),
        ("Countries", "Argentina, been around Europe", None),
        ("Relationship", "single. focused on myself and training 💪", None),
        ("Favorite", "pasta. need the carbs. a good steak too", None),
        ("Tattoos", "yeah I'm covered. arms, chest, stomach, legs. each one tells a story", None),
    ],

    "positive_spin": [
        ("Age40Plus", "respect... I like a guy who knows exactly what he wants 💪", None),
        ("Age20s", "nice same age range, that's rare on here", None),
        ("BoringJob", "solid. stability and discipline, I respect that 💪", None),
        ("CoolJob", "for real?? that's sick 🔥", None),
        ("Fit", "I can tell. respect 💪", None),
        ("NotFit", "doesn't matter, it's the energy", None),
        ("SameCity", "no way. that's wild 😏", None),
        ("FarAway", "far but doesn't matter when the vibe is this strong", None),
    ],

    "re_engagement": [
        ("RE-1", "been thinking about earlier 😏 you free?", "6-12 hrs after.", "sext"),
        ("RE-2", "just did something crazier. you need to see this 😈", "Next day.", "sext"),
    ],

    "obj_scripts": {},
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
