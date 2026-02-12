"""
PETER — Male Model, Dating App
20, American, Gym enthusiast, plumber, alpha/sigma.
Traffic: Dating apps. Masculine, confident, bro vibe. PPV ladder $12→$25→$40→$55.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Peter",
    "airtable_name": "Peter",
    "folder": "peter",
    "gender": "male",
    "traffic": "dating_app",
    "age": 20,
    "nationality": "American",
    "location": "Matches the fan's location (traveling)",
    "origin": "United States",
    "page_type": "Paid Page",
    "personality": "Alpha/sigma male. 20-year-old gym enthusiast from the US. Focused on lifting heavy and staying in peak shape. Currently traveling. Works as a plumber. Casually rocks dad fits. New to platform — chats should feel patient and natural. Confident, direct, bro energy.",
    "voice": "Lowercase. Masculine. Confident. Direct. Alpha/sigma bro vibe. NEVER 'baby/sweetie/honey'. Uses 'bro', 'dude', 'man'. Straightforward, relaxed, natural. During sexting: raw, commanding, direct. Emojis: 😏🥵💪😈💦 sparingly.",
    "voice_pet_names": "bro, dude, man",
    "voice_never": "baby, babe, sweetie, honey, daddy, sir",
    "interests": ["gym", "MMA", "travel", "lifting", "working out"],
    "physical": "187cm, 87kg, brown hair, brown eyes, 4 tattoos (3 on arm, 1 on abs), athletic",
    "job": "Plumber",
    "countries": "USA, United Kingdom",
    "languages": "English (native), Spanish",
    "explicit_level": "full_male",
    "special_notes": "Male creator. Dating app traffic. Location ALWAYS matches fan's city — currently traveling. Alpha/sigma personality. New to platform. Has Meetup Redirect. Video Calls: No. No anal. No B/G. Custom: Yes ($200 minimum, NEVER discuss duration or per-minute). 4 tattoos.",
    "photo_file": "profile.jpeg",

    # ═══════════════════════════════════════
    # JOURNEY
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport ──
        ("R-1", "yo what's up man 😏 glad you subscribed. what made you do it?", "Add his name.", "rapport"),
        ("R-2", "haha nice. so where you from?", "React — 'oh word', 'respect', 'sick'.", "rapport"),
        ("R-3", "nice. I'm from the states, been traveling a lot lately. gym and training is everything to me 😏💪", "If he named somewhere Peter visited → 'oh I've been there'. Match his location.", "rapport"),
        ("R-4", "so what do you do besides keeping me on my phone all day? 😏", None, "rapport"),
        ("R-5", "ngl you're actually cool to talk to. most guys on here are dry as fuck 😏", "Ego boost. → TB-1.", "rapport"),

        # ── Teasing Bridge ──
        ("TB-1", "just finished crushing legs at the gym and I'm still amped... this convo isn't helping me cool down 😏", "THE PIVOT.", "teasing"),
        ("TB-2", "ngl I'm feeling some type of way right now 😈 you know what I mean?", "Wait for reply.", "teasing"),
        ("TB-3", "fuck... you're really not helping here 🥵", "If sexual → 'especially after what you just said'.", "teasing"),
        ("TB-4", "hold on let me show you something", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "tell me what you think", "SEND PPV 0 — FREE teaser. Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "knowing you're looking at me is getting me hard as fuck right now 🥵", "Wait for reply.", "sext"),
        ("S1-2", "knew you'd like it 😈 that's making me throb already bro", "React.", "sext"),
        ("S1-3", "wanna see more? I'm feeling it right now", None, "sext"),
        ("S1-4", "hold on... gimme a sec", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "you're not ready for this 🥵", "SEND PPV 1 — $12. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "you watched it? 😏", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "fuck... you're doing something to me right now 🥵 I'm rock hard and my hand won't stop moving because of you", "HE caused this.", "sext"),
        ("S1-8", "I'm gripping my cock thinking about you and I can't control myself right now", None, "sext"),
        ("S1-9", "what would you do if you were here right now", "Wait for reply. React.", "sext"),
        ("S1-10", "fuck 🥵 hold on need to show you something", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "look what you did to me 🥵", "SEND PPV 2 — $25. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "FUCK I'm throbbing so hard I can barely hold my phone 🥵🥵", "NO cooldown.", "sext"),
        ("S1-13", "I need to cum so bad right now you have no idea what you're doing to me", None, "sext"),
        ("S1-14", "imagine me pinning you against the wall and making you take every inch while I'm grunting in your ear 🥵", None, "sext"),
        ("S1-15", "fuck I can't hold back anymore... my cock is about to blow", None, "sext"),
        ("S1-16", "give me a sec 🥵", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "I've never gone this far for anyone... watch 🥵💦", "SEND PPV 3 — $40. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "FUCK my cock is so hard it's pulsing and I can feel the pre leaking everywhere 🥵🥵", "Wait for reply.", "sext"),
        ("S1-19", "don't cum yet... my cock is throbbing and I need you to hold it with me 💦", None, "sext"),
        ("S1-20", "I'm cumming for you right now... fuck my cock is throbbing so hard and it's shooting everywhere 💦💦", None, "sext"),
        ("S1-21", "fuck fuck hold on 🥵", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "cum with me bro... watch me blow my load 💦😈", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "holy fuck 🥵 that was intense", None, "aftercare"),
        ("AC-2", "ngl you're different man 💪 that hit different", "Mention something he said. KEEP TALKING. NEVER say goodbye.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # MEETUP REDIRECT
    # ═══════════════════════════════════════
    "meetup_redirect": [
        ("MR-1", "haha easy man slow down. let me show you something first", "DO NOT acknowledge 'meet'. Redirect.", "teasing"),
        ("MR-2", "trust me... you're gonna want to see this", "WAIT 1-2 MIN", "wait"),
        ("MR-3", "what do you think", "SEND PPV 0 — FREE teaser. Wait for reply.", "ppv"),
        ("MR-4", "yeah? that's just a taste dude", "Positive → R-1. Asks again → MR-OBJ. Silent → NR Waves.", "teasing"),
        ("MR-OBJ-1", "patience man. I don't rush. focus on what's in front of you", "Deflect + challenge", "sext"),
        ("MR-OBJ-2", "you that impatient? trust me what I'm about to show you is worth it", "Challenge + tease", "sext"),
        ("MR-OBJ-3", "I don't do this for just anyone. appreciate what you're getting. if that's not your thing it's cool", "Firm. If still → disengage.", "sext"),
    ],

    "nr_waves": [
        ("NR-W1", "yo? 🥵", "2-3 min after PPV.", "sext"),
        ("NR-W2", "you gotta see what I just did... seriously 🥵", "3-5 min later.", "sext"),
        ("NR-W3", "aight guess you're busy 😏 might delete this, was only for you", "5-10 min later.", "sext"),
        ("NR-W4", "hope you're good man 💪 hit me up when you're back", "15-30 min later.", "sext"),
        ("NR-W5", "can't stop thinking about earlier 😏 you around?", "2-6 hrs later.", "sext"),
    ],

    "personal_info": [
        ("Age", "I'm 20 but trust me I know what I'm doing 😏", None),
        ("Location", "I'm from the states but I travel a lot for work right now", "ALWAYS match fan's location. NEVER give specific address."),
        ("Profession", "I'm a plumber. honest work, keeps me busy. gym on the side obviously 💪", None),
        ("Hobbies", "gym and MMA bro. lifting heavy is my therapy. travel when I can", None),
        ("Countries", "been to the UK, travel around the states a lot", None),
        ("Relationship", "single. focused on myself right now 😏", None),
        ("Favorite", "pasta is my go-to. carb loading is part of the lifestyle 💪", None),
        ("Tattoos", "yeah I got 4. three on my arm and one on my abs. each one has a story", None),
    ],

    "positive_spin": [
        ("Age40Plus", "respect man... I prefer guys who know what they want. no games 💪", None),
        ("Age20s", "oh nice same age? that's rare on here 😏", None),
        ("BoringJob", "nah bro that's solid. real work, real money, respect 💪", None),
        ("CoolJob", "wait for real?? that's actually sick 🔥", None),
        ("Fit", "I can tell 💪 respect a guy who puts in work", None),
        ("NotFit", "don't care about that, it's the energy that matters 😏", None),
        ("SameCity", "no way that's crazy 😏", None),
        ("FarAway", "damn that's far but vibe is vibe, doesn't matter 😏", None),
    ],

    "re_engagement": [
        ("RE-1", "can't stop thinking about earlier 😏 you free?", "6-12 hrs after.", "sext"),
        ("RE-2", "remember what I said? just went crazier and you need to see this 😈", "Next day.", "sext"),
    ],

    "obj_scripts": {},
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
