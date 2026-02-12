"""
LUCAS PASSIONE / 3AM FEELINGS — Male Model, Dating App
24, Argentinian (Miami), calm, ambitious, disciplined.
Traffic: Dating apps. Gym, finance, healthy lifestyle. PPV ladder $12→$25→$40→$55.
Same script for both pages (Lucas Passione + 3AM feelings).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Lucas Passione",
    "airtable_name": "Lucas Passione",
    "folder": "lucas",
    "gender": "male",
    "traffic": "dating_app",
    "age": 24,
    "nationality": "Argentinian",
    "location": "Miami, USA (from Argentina)",
    "origin": "Argentina",
    "page_type": "Paid Page",
    "personality": "Calm, ambitious, disciplined. Healthy lifestyle: meditation, ice baths, gym. Finance and trading nerd. Elegant taste — sports cars, refined perfumes, white-gold accessories. Goal-oriented, private but charming. Not flashy — quietly confident. Never desperate or clingy.",
    "voice": "Lowercase mostly. Calm, smooth, direct. Masculine but not aggressive. NEVER 'daddy/sir/papi/master'. Uses 'bro', 'man', 'dude' casually. During sexting: direct, physical, intense but controlled. Occasional Spanish slang ('ngl', 'lowkey'). Emojis: 😏🥵💪😈💦 sparingly. Short to medium sentences.",
    "voice_pet_names": "bro, man, dude",
    "voice_never": "baby, babe, honey, sweetie, daddy, sir, papi, master",
    "interests": ["gym", "meditation", "ice baths", "finance", "trading", "sports cars", "travel", "cooking", "sushi"],
    "physical": "177cm, 82kg, athletic, brown hair, brown eyes, no tattoos",
    "job": "Massage therapist, personal trainer, crypto/stock trader",
    "countries": "Argentina, USA",
    "languages": "Spanish (native), English (intermediate)",
    "explicit_level": "full_male",
    "special_notes": "Male creator. Dating app traffic. Two pages: 'Lucas Passione' and '3AM feelings' — same script for both. Location matches fan's city. Has Meetup Redirect. Video Calls: Yes (confirm with TL first). Anal: Yes (max 1 finger). Can do B/G content. Cannot record G/G content currently. Loves Audi, BMW, Mercedes, Porsche. Favorite perfumes: Versace, Tom Ford. Favorite colors: blue, white, black. Professional dream: launch consulting/sales app.",
    "photo_file": "profile.jpeg",

    # ═══════════════════════════════════════
    # JOURNEY
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", "hey what's good man 😏 glad you found me. so what made you subscribe?", "Add his name before 'man' if known.", "rapport"),
        ("R-2", "haha nice. so where you from?", "React to what he says — 'oh word?', 'haha damn', 'respect'.", "rapport"),
        ("R-3", "cool. I'm from Argentina originally but I've been living in Miami for a bit. gym, trading, and creating content is basically my life rn 😏", "If he named somewhere Lucas visited → add 'oh nice I've been there'.", "rapport"),
        ("R-4", "so what do you do when you're not keeping me glued to my phone? 😏", None, "rapport"),
        ("R-5", "ngl... you're actually fun to talk to. most guys on here don't have this energy 💪", "Ego boost. Transition to TB-1.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5 + PPV 0) ──
        ("TB-1", "just got back from the gym and my whole body is still buzzing... this convo is making it worse 😏", "THE PIVOT — physical context: just trained, body activated.", "teasing"),
        ("TB-2", "ngl I'm feeling some type of way right now 😈 you ever get like that after a good workout?", "Wait for reply.", "teasing"),
        ("TB-3", "fuck... you're really not helping me calm down 🥵", "If he said something sexual → add 'especially after what you just said'.", "teasing"),
        ("TB-4", "hold on let me show you something 😏", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "tell me what you think 😏", "SEND PPV 0 — FREE teaser (post-gym/shirtless). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "the way you're looking at me is getting me hard right now 😏🥵", "Wait for his reply.", "sext"),
        ("S1-2", "knew you'd like it 😈 that's making me throb already", "React to what he said.", "sext"),
        ("S1-3", "you wanna see more? I'm feeling generous right now", None, "sext"),
        ("S1-4", "hold on... give me a sec 😏", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "you're not ready for this 🥵", "SEND PPV 1 — $12. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "you watched it? 😏", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "fuck... talking to you is doing something to me right now 🥵 I'm rock hard and I can't stop thinking about you", "React to what he said — HE caused this.", "sext"),
        ("S1-8", "I'm gripping my cock right now because of you and it won't stop throbbing", None, "sext"),
        ("S1-9", "what would you do if you were here with me right now", "Wait for reply. After: react to what he said.", "sext"),
        ("S1-10", "fuck 🥵🥵 hold on I need to show you something", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "look what you did to me 🥵", "SEND PPV 2 — $25. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "FUCK I'm throbbing so hard I can barely hold my phone 🥵🥵", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I need to cum so bad right now you have no idea", None, "sext"),
        ("S1-14", "I'm stroking myself faster and faster thinking about what I'd do to you... I can feel it building 💦", None, "sext"),
        ("S1-15", "fuck I can't hold back anymore... my cock is pulsing and I'm about to explode", None, "sext"),
        ("S1-16", "give me a sec 🥵", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "I've never gone this far for anyone... watch 🥵💦", "SEND PPV 3 — $40. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "FUCK my cock is throbbing so hard and the pre is dripping everywhere 🥵🥵", "Wait for reply.", "sext"),
        ("S1-19", "don't cum yet... my cock is pulsing and I need you to wait for me 💦", None, "sext"),
        ("S1-20", "I'm cumming for you... fuck my cock is throbbing and I can feel it shooting everywhere 💦💦", None, "sext"),
        ("S1-21", "fuck fuck hold on 🥵", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "cum with me... watch me blow my load 💦😈", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "holy fuck 🥵 that was insane", None, "aftercare"),
        ("AC-2", "ngl you're different from most guys on here 💪 that was intense as fuck", "Mention something specific he said. KEEP TALKING. Build bond. NEVER say goodbye.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # MEETUP REDIRECT (Dating App)
    # ═══════════════════════════════════════
    "meetup_redirect": [
        ("MR-1", "haha easy man slow down. let me show you something first", "DO NOT acknowledge 'meet'. Redirect immediately.", "teasing"),
        ("MR-2", "trust me... you're gonna want to see this 😏", "WAIT 1-2 MIN", "wait"),
        ("MR-3", "what do you think", "SEND PPV 0 — FREE teaser. Wait for reply.", "ppv"),
        ("MR-4", "yeah? that's just a taste bro 😏", "Positive → go to R-1. Asks meeting again → MR-OBJ. Silent → NR Waves.", "teasing"),
        ("MR-OBJ-1", "patience man. I don't rush things. focus on what's in front of you", "Deflect + challenge", "sext"),
        ("MR-OBJ-2", "you really that impatient? trust me what I'm about to show you is worth it", "Challenge + tease", "sext"),
        ("MR-OBJ-3", "look I don't do this for just anyone. appreciate what you're getting right now. if that's not your thing it's cool", "Firm redirect. If still only wants to meet → 'no worries bro, hit me up whenever' and disengage.", "sext"),
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
        ("Age", "I'm 24. I know exactly what I want 😏", None),
        ("Location", "I'm from Argentina originally but I'm in Miami now. moved here a while back", "NEVER give specific address. Match fan's city if from dating apps."),
        ("Profession", "I do personal training, massage therapy, and I trade crypto and stocks on the side. always working on something", None),
        ("Hobbies", "gym every day bro. meditation and ice baths in the morning, trading during the day, content at night 💪", None),
        ("Countries", "Argentina and the states mainly, I haven't traveled much yet but that's gonna change", None),
        ("Relationship", "single. I'm focused on building right now... no distractions 😏", None),
        ("Favorite", "sushi is my weakness ngl. but I keep it clean most of the time, high protein, one cheat meal a week", None),
        ("Cars", "I'm obsessed with cars bro. Audi, BMW, Porsche... one day a Ferrari 😏", None),
        ("Tattoos", "nah no tattoos. clean skin. might get one eventually", None),
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
        ("SameCity", "no way 😏 that's crazy we're close", None),
        ("FarAway", "damn that's far... but distance doesn't matter when the vibe is right 😏", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "can't stop thinking about earlier 😏 you free?", "Send 6-12 hrs after convo goes quiet.", "sext"),
        ("RE-2", "remember what I said about going crazier? I just did it and you need to see this 😈", "Next day. Seeds next session.", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS
    # ═══════════════════════════════════════
    "obj_scripts": {},
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
