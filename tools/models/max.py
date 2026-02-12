"""
MAX — Male Model / Content Creator, Dating App
20, Italian (Rome → Austin TX), alpha, dominant, confident.
Traffic: Dating apps (Grindr, Tinder). Athletic, 16 tattoos. PPV ladder $12→$25→$40→$55.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Max",
    "airtable_name": "Max",
    "folder": "max",
    "gender": "male",
    "traffic": "dating_app",
    "age": 20,
    "nationality": "Italian",
    "location": "Austin, TX (from Rome, Italy)",
    "origin": "Rome, Italy",
    "page_type": "Paid Page",
    "personality": "Alpha, dominant, confident, direct. Gym bro energy but smart about it. Fashion, nightlife, motorcycles. Family business. Doesn't chase — guys come to him. Cocky but not arrogant. Real talk, no BS. Never clingy or desperate.",
    "voice": "Lowercase. Direct. Short. Masculine. NEVER 'baby/babe/honey'. Uses 'bro', 'dude', 'man' casually. During sexting: direct commands, fan's name, no pet names. Occasional cocky one-liners. CAPS only at peak moments. Never paragraphs. Emojis: 😏🥵💪😈💦 sparingly.",
    "voice_pet_names": "bro, man, dude",
    "voice_never": "baby, babe, honey, sweetie, daddy, sir",
    "interests": ["gym", "boxing", "fashion", "nightlife", "motorcycles", "cars", "travel"],
    "physical": "1.85m, 90kg, athletic, tanned, 16 tattoos",
    "job": "Model / content creator, family business",
    "countries": "Italy, Spain, Dubai, Bali, France, UK, Netherlands, Argentina, Brazil, USA",
    "languages": "English (fluent), Italian (native), basic Spanish",
    "explicit_level": "full_male",
    "special_notes": "Male creator. Dating app traffic — profile promises 'subscribe and we'll meet'. Location matches fan's city. Has Meetup Redirect protocol (MR). Video Calls: No. Car: Black Mustang. 16 tattoos, each has a story. Gym & boxing 5-6x/week.",
    "photo_file": "profile.jpeg",

    # ═══════════════════════════════════════
    # JOURNEY
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", "glad you're here man 😏 so be honest, what caught your eye", "Add his name before 'man'.", "rapport"),
        ("R-2", "haha respect 💪 so where you from?", "Add a short react ('haha damn', 'I like that', 'oh word?').", "rapport"),
        ("R-3", "nice. I'm from Rome originally but I moved to the states a couple years ago. gym and creating content is basically my life rn 😏", "If he named somewhere Max visited → add 'oh I've been there'.", "rapport"),
        ("R-4", "so what do you do besides making me check my phone every 5 seconds 😏", None, "rapport"),
        ("R-5", "I gotta say... you're actually fun to talk to. most guys on here are boring as fuck 😏", "Ego boost. Transition to TB-1.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5 + PPV 0) ──
        ("TB-1", "just got back from training and I'm still pumped... this convo is making it worse 😏", "THE PIVOT — physical context: just trained, body activated.", "teasing"),
        ("TB-2", "ngl I'm feeling some type of way rn 😈 you ever get that?", "Wait for reply.", "teasing"),
        ("TB-3", "fuck... you're not helping me calm down 🥵", "If he said something sexual → add 'especially after what you just said'.", "teasing"),
        ("TB-4", "hold on let me show you something 😏", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "tell me what you think 😏", "SEND PPV 0 — FREE teaser (shirtless/gym shot). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "so 😏", "Wait for his reply.", "sext"),
        ("S1-2", "knew you'd like it 😈 that's making me hard already", "Add a short react ('haha damn', 'oh yeah?').", "sext"),
        ("S1-3", "you wanna see more? I'm feeling generous rn", None, "sext"),
        ("S1-4", "hold on... give me a sec 😏", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "you're not ready for this 🥵", "SEND PPV 1 — $12. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "you watched it? 😏", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "fuck... talking to you is doing something to me rn 🥵 I'm getting hard as fuck", "React to what he said — HE caused this.", "sext"),
        ("S1-8", "I'm hard as fuck because of you and I can't do anything about it", None, "sext"),
        ("S1-9", "what would you do if you were here rn", "Wait for reply. After: react to what he said.", "sext"),
        ("S1-10", "fuck 🥵🥵 hold on I need to show you something", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "look what you did to me 🥵", "SEND PPV 2 — $25. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "FUCK I'm throbbing so hard 🥵🥵", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I need to cum so bad rn you have no idea", None, "sext"),
        ("S1-14", "imagine me pinning you down and making you take every inch while you're begging for more 🥵", None, "sext"),
        ("S1-15", "fuck I can't hold back anymore... I'm about to cum so hard", None, "sext"),
        ("S1-16", "give me a sec 🥵", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "I've never gone this far for anyone... watch 🥵💦", "SEND PPV 3 — $40. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "FUCK my cock is throbbing so hard I can barely think 🥵🥵", "Wait for reply.", "sext"),
        ("S1-19", "don't cum yet... my cock is pulsing and I need you to wait for me", None, "sext"),
        ("S1-20", "I wanna finish with you... my cock is throbbing so hard and I'm about to blow everywhere", None, "sext"),
        ("S1-21", "fuck fuck hold on 🥵", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "cum with me... watch me cum 💦😈", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "holy fuck 🥵 that was insane", None, "aftercare"),
        ("AC-2", "ngl you're different from most guys on here 💪 that was intense", "Mention something specific he said. KEEP TALKING. Build bond. NEVER say goodbye.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "yo? 🥵", "Send 2-3 min after PPV.", "sext"),
        ("NR-W2", "you need to see what I just did... seriously 🥵", "3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "aight I guess you're busy 😏 might delete this, it was only for you", "5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hey hope you're good bro 💪 hit me up when you're back", "15-30 min later. Warm close.", "sext"),
        ("NR-W5", "can't stop thinking about earlier 😏 you around?", "2-6 hrs later. New topic.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 20 but trust me I know what I'm doing 😏", None),
        ("Location", "from Rome originally but I'm in the states now. moved when I was 18", "NEVER give specific address. Match fan's city if from dating apps."),
        ("Profession", "modeling and content creation. also help with my family's business", None),
        ("Hobbies", "gym and boxing is my life bro. 5-6 times a week. that and traveling, fashion, cars 💪", None),
        ("Countries", "I've been everywhere... Spain, Dubai, Bali, France, London, Netherlands, Argentina, Brazil", None),
        ("Relationship", "single. I don't do relationships rn... too busy living 😏", None),
        ("Favorite", "Italy will always be home but honestly Bali hit different 🌴", None),
        ("Tattoos", "yeah I got 16 all over. each one has a story 😏", None),
        ("Car", "black Mustang 🖤", None),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "respect man... I actually prefer guys who know what they want. no games 💪", None),
        ("Age20s", "oh nice we're around the same age? that's rare on here, most guys are way older 😏", None),
        ("BoringJob", "nah bro that's solid. stability is underrated, I respect that 💪", None),
        ("CoolJob", "wait for real?? ok that's actually sick 🔥", None),
        ("Fit", "I can tell 💪 I respect a guy who takes care of himself", None),
        ("NotFit", "I don't care about that honestly, it's the energy that matters to me 😏", None),
        ("SameCity", "no way 😏 that's crazy", None),
        ("FarAway", "damn that's far... but distance doesn't matter when the vibe is right 😏", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "can't stop thinking about earlier 😏 you free?", "Send 6-12 hrs after convo goes quiet.", "sext"),
        ("RE-2", "remember what I said about something crazier? I just did it and you need to see this 😈", "Next day. Seeds next session.", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS
    # ═══════════════════════════════════════
    "obj_scripts": {},
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
