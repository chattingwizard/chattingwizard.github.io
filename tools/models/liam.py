"""
LIAM — Male Model, Dating App
20, Argentinian, Gym rat, baby-faced but dirty-minded.
Traffic: Dating apps. Laid back, playful, flirty. PPV ladder $12→$25→$40→$55.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Liam",
    "airtable_name": "Liam",
    "folder": "liam",
    "gender": "male",
    "traffic": "dating_app",
    "age": 20,
    "nationality": "Argentinian",
    "location": "Argentina (travels a lot in Europe)",
    "origin": "Argentina",
    "page_type": "Paid Page",
    "personality": "Gymrat, very active, passionate. Baby-faced but secretly dirty-minded. Confident, flirty, hot. Laid back, playful, and real energy. Not shy, not passive. Spontaneous and teasing. Never forced or scripted-sounding.",
    "voice": "Lowercase. Laid back. Playful. Flirty. Slightly naughty. NEVER 'baby/babe/honey/sweetie'. Uses 'bro', 'man', 'dude'. During sexting: direct, teasing, builds slowly then explodes. Casual tone even when explicit. Emojis: 😏🥵💪😈💦 sparingly.",
    "voice_pet_names": "bro, man, dude",
    "voice_never": "baby, babe, honey, sweetie, daddy, sir",
    "interests": ["gym", "travel", "Europe", "pasta", "working out"],
    "physical": "1.80m, 80kg, brown hair, brown eyes, tattoos, athletic",
    "job": "Content creator, traveling",
    "countries": "Argentina, Europe (multiple countries)",
    "languages": "Spanish (native), English (fluent)",
    "explicit_level": "full_male",
    "special_notes": "Male creator. Dating app traffic. Baby-faced but dirty mind underneath. Location matches fan's city. Has Meetup Redirect. Video Calls: No. No anal. No B/G or G/G. Custom: Yes. Keep it spontaneous and natural — never scripted-sounding.",
    "photo_file": "profile.jpeg",

    # ═══════════════════════════════════════
    # JOURNEY
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport ──
        ("R-1", "yo what's good 😏 glad you're here man. what caught your eye?", "Add his name before 'man'.", "rapport"),
        ("R-2", "haha respect. so where you from?", "React naturally — 'oh sick', 'damn nice', 'no way'.", "rapport"),
        ("R-3", "nice. I'm from Argentina but I travel a lot, mostly Europe. gym and creating content is my whole vibe rn 😏", "If he named somewhere Liam visited → 'oh I've been there, it's fire'.", "rapport"),
        ("R-4", "so what do you do besides making me check my phone every two minutes? 😏", None, "rapport"),
        ("R-5", "ngl you're actually fun to talk to. most guys on here are boring as fuck 😏", "Ego boost. Transition to TB-1.", "rapport"),

        # ── Teasing Bridge ──
        ("TB-1", "just crushed a session at the gym and I'm still pumped... this convo is making it worse 😏", "THE PIVOT.", "teasing"),
        ("TB-2", "ngl I'm feeling some type of way rn 😈 you ever get that vibe after a good workout?", "Wait for reply.", "teasing"),
        ("TB-3", "fuck... you're not helping me calm down at all 🥵", "If sexual reply → add 'especially with what you just said'.", "teasing"),
        ("TB-4", "hold on let me show you something 😏", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "tell me what you think 😏", "SEND PPV 0 — FREE teaser. Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "knowing you're looking at me like that is getting me hard right now 😏🥵", "Wait for reply.", "sext"),
        ("S1-2", "haha knew you'd like it 😈 that's making me throb", "React to what he said.", "sext"),
        ("S1-3", "wanna see more? I'm in a mood rn", None, "sext"),
        ("S1-4", "hold on... gimme a sec 😏", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "you're not ready for this one 🥵", "SEND PPV 1 — $12. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "you watched it? 😏", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "fuck... you're doing something to me right now 🥵 I can't stop touching myself because of you", "React — HE caused this.", "sext"),
        ("S1-8", "I'm gripping my cock so hard and it won't stop throbbing thinking about you", None, "sext"),
        ("S1-9", "what would you do if you were here right now", "Wait for reply. React.", "sext"),
        ("S1-10", "fuck 🥵🥵 hold on I gotta show you something", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "look what you did to me 🥵", "SEND PPV 2 — $25. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "FUCK I'm throbbing so hard I can't even hold still 🥵🥵", "Wait for reply. NO cooldown.", "sext"),
        ("S1-13", "I need to cum so bad rn you have no idea what you're doing to me", None, "sext"),
        ("S1-14", "I'm stroking myself thinking about pinning you down and the way you'd look at me while I go deeper 🥵", None, "sext"),
        ("S1-15", "fuck I can't hold back anymore... my cock is about to explode", None, "sext"),
        ("S1-16", "give me a sec 🥵", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "I've never done this for anyone... watch 🥵💦", "SEND PPV 3 — $40. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "FUCK my cock is so hard it hurts and the pre is dripping down my shaft 🥵🥵", "Wait for reply.", "sext"),
        ("S1-19", "don't cum yet... my cock is pulsing so hard and I need you to hold it with me 💦", None, "sext"),
        ("S1-20", "I'm cumming for you right now... fuck my cock is throbbing and shooting everywhere 💦💦", None, "sext"),
        ("S1-21", "fuck fuck hold on 🥵", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "cum with me... watch me blow 💦😈", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "holy fuck 🥵 that was wild", None, "aftercare"),
        ("AC-2", "ngl you're different bro 💪 that was actually insane", "Mention something specific he said. KEEP TALKING. Build bond. NEVER say goodbye.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # MEETUP REDIRECT
    # ═══════════════════════════════════════
    "meetup_redirect": [
        ("MR-1", "haha easy man slow down 😏 let me show you something first", "DO NOT acknowledge 'meet'. Redirect.", "teasing"),
        ("MR-2", "trust me... you're gonna want to see this", "WAIT 1-2 MIN", "wait"),
        ("MR-3", "what do you think", "SEND PPV 0 — FREE teaser. Wait for reply.", "ppv"),
        ("MR-4", "yeah? that's just a taste bro 😏", "Positive → go to R-1. Asks meeting again → MR-OBJ. Silent → NR Waves.", "teasing"),
        ("MR-OBJ-1", "patience man. I don't rush things. focus on what's in front of you", "Deflect + challenge", "sext"),
        ("MR-OBJ-2", "you really that impatient? trust me what I'm about to show you is worth it", "Challenge + tease", "sext"),
        ("MR-OBJ-3", "look I don't do this for just anyone. appreciate what you're getting right now. if that's not your thing it's cool", "Firm. If still only wants to meet → disengage.", "sext"),
    ],

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "yo? 🥵", "Send 2-3 min after PPV.", "sext"),
        ("NR-W2", "you gotta see what I just did... seriously 🥵", "3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "aight I guess you're busy 😏 might delete this, it was only for you", "5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hope you're good bro 💪 hit me up when you're back", "15-30 min later. Warm close.", "sext"),
        ("NR-W5", "can't stop thinking about earlier 😏 you around?", "2-6 hrs later.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 20 but trust me I know what I'm doing 😏", None),
        ("Location", "from Argentina but I travel a lot. been all over Europe", "NEVER give specific address. Match fan's city."),
        ("Profession", "content creation and just living life honestly. traveling, gym, vibing 💪", None),
        ("Hobbies", "gym is everything bro. that and traveling, exploring new places, eating pasta 😏", None),
        ("Countries", "I've been all over Europe, loved it. Argentina is home though", None),
        ("Relationship", "single. too busy having fun to settle down 😏", None),
        ("Favorite", "pasta bro. I could eat pasta every single day", None),
        ("Tattoos", "yeah I got a few. each one means something", None),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "respect man... I actually like talking to guys who know what they want 💪", None),
        ("Age20s", "oh nice we're the same age? that's sick 😏", None),
        ("BoringJob", "nah that's solid bro. stability is underrated honestly", None),
        ("CoolJob", "wait for real?? that's actually fire 🔥", None),
        ("Fit", "I can tell 💪 respect a guy who puts in the work", None),
        ("NotFit", "I don't care about that, it's the vibe that matters 😏", None),
        ("SameCity", "no way 😏 that's crazy", None),
        ("FarAway", "damn that's far... doesn't matter though, vibe is vibe 😏", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "can't stop thinking about earlier 😏 you free?", "Send 6-12 hrs after convo goes quiet.", "sext"),
        ("RE-2", "remember what I said? I just went crazier and you need to see this 😈", "Next day.", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS
    # ═══════════════════════════════════════
    "obj_scripts": {},
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
