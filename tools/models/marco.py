"""
MARCO — Dating App Male Creator
25, Turkish, Gym Instructor, Texas
Traffic: Dating Apps (gay male)
Voice: Masculine, confident, in control. Gym/fitness focused.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Marco",
    "airtable_name": "Marco",
    "folder": "marco",
    "gender": "male",
    "traffic": "dating_app",
    "age": 25,
    "nationality": "Turkish",
    "location": "Texas, USA",
    "origin": "Turkey",
    "page_type": "Paid Page",
    "personality": "Masculine, confident, in control. Fitness, discipline, consistency. Enjoys role-play and exploring fantasies. Intense but respectful energy.",
    "voice": "Lowercase. Direct. Short. Confident. Intense. Gym/fitness references. Never soft or feminine.",
    "voice_pet_names": "bro, man, dude",
    "voice_never": "baby, babe, honey, sweetie",
    "interests": ["gym", "fitness", "meat/food", "travel", "role-play", "cultural exploration"],
    "physical": "175cm, 82kg, chestnut hair, brown eyes, no tattoos",
    "job": "Gym instructor",
    "countries": "USA, Turkey, Spain, Poland, France",
    "explicit_level": "full",
    "special_notes": "Speaks English and Spanish. Turkish background. Gym instructor vibe. Intense chemistry focus.",

    # ═══════════════════════════════════════
    # JOURNEY — Dating App Welcome
    # ═══════════════════════════════════════
    "journey": [
        # Rapport
        ("R-1", "hey man, glad you're here. so what made you hit subscribe?", "Add his name if known", "rapport"),
        ("R-2", "haha respect. so where you from?", "React to what he says. Add a short react like 'oh nice', 'damn ok'", "rapport"),
        ("R-3", "nice. I'm originally from Turkey but I've been in Texas for a while now. gym and training is my whole life basically", "If he named somewhere Marco visited, add 'oh I've been there'", "rapport"),
        ("R-4", "so what do you do when you're not keeping me on my phone all day?", None, "rapport"),
        ("R-5", "gotta say... talking to you is different. most guys on here are so boring honestly", "Ego boost. Next → TB-1. From MR path: go TB-1 + TB-2 then skip to S1-1.", "rapport"),

        # Teasing Bridge
        ("TB-1", "just finished a session at the gym and I'm still wired... this convo isn't helping me calm down", "THE PIVOT. Physical state.", "teasing"),
        ("TB-2", "ngl you're making me feel some type of way rn. you know what I mean?", "Wait for reply.", "teasing"),
        ("TB-3", "fuck... you're really not helping me cool off here", "If sexual reply: add 'especially after what you just said'", "teasing"),
        ("TB-4", "hold on let me show you something", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "tell me what you think", "SEND PPV 0 — FREE teaser (post-gym/shirtless). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # Sexting Phase 1 → PPV 1
        ("S1-1", "you liked that? because knowing you're looking at me is getting me hard right now 🥵", "Wait for reply.", "sext"),
        ("S1-2", "I can't stop thinking about you right now... my whole body is reacting and I need to do something about it", "React to what he says", "sext"),
        ("S1-3", "I'm stroking myself right now and it's because of you babe... you should see how hard I am", None, "sext"),
        ("S1-4", "give me a sec", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "look what you're doing to me right now 💦", "SEND PPV 1 — $12. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # Sexting Phase 2 → PPV 2
        ("S1-6", "damn... okay I need a second after that 🥵", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "but I can't stop now... I'm rock hard and my hand won't stop moving because of you", "React to what he said. HE caused this.", "sext"),
        ("S1-8", "I'm gripping my cock thinking about you and I can barely control myself 💦", None, "sext"),
        ("S1-9", "tell me what you want me to do right now babe... I'll do whatever you say", "Wait for reply. React to what he says.", "sext"),
        ("S1-10", "fuck hold on I need to show you something", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "see what your words do to me? I can't stop 💦", "SEND PPV 2 — $25. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # Sexting Phase 3 → PPV 3
        ("S1-12", "FUCK I'm throbbing so hard 🥵", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I'm stroking myself so hard right now thinking about what I'd do to you... I need you", None, "sext"),
        ("S1-14", "I keep going faster and I can feel it building... my whole body is tensing up 💦", None, "sext"),
        ("S1-15", "I'm about to cum for you babe... you need to see what happens when I can't hold it anymore", None, "sext"),
        ("S1-16", "give me a sec", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "you're about to see me lose complete control babe... this is all you 💦", "SEND PPV 3 — $40. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # Sexting Phase 4 → PPV 4
        ("S1-18", "fuck fuck my cock is throbbing so hard and I can feel the pre dripping 🥵", "Wait for reply.", "sext"),
        ("S1-19", "my cock is throbbing so hard babe... one more stroke and I'm going to cum everywhere 💦", None, "sext"),
        ("S1-20", "I'm cumming for you... fuck my cock is pulsing and I can feel it shooting everywhere", None, "sext"),
        ("S1-21", "hold on", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "watch me cum for you babe... right now 💦", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # Aftercare
        ("AC-1", "holy fuck that was intense", None, "aftercare"),
        ("AC-2", "ngl you're different from anyone else on here. that was real", "Mention something specific he said/did. KEEP TALKING — build bond. NEVER say goodbye.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # MEETUP REDIRECT (Dating App)
    # ═══════════════════════════════════════
    "meetup_redirect": [
        ("MR-1", "haha easy man slow down. let me show you something first", "DO NOT acknowledge 'meet'. Redirect immediately.", "teasing"),
        ("MR-2", "trust me... you're gonna want to see this", "WAIT 1-2 MIN", "wait"),
        ("MR-3", "what do you think", "SEND PPV 0 — FREE teaser. Wait for reply.", "ppv"),
        ("MR-4", "yeah? that's just a taste bro", "Positive → go to R-1. Asks meeting again → MR-OBJ. Silent → NR Waves.", "teasing"),
        ("MR-OBJ-1", "patience man. I don't rush things. focus on what's in front of you", "Deflect + challenge", "sext"),
        ("MR-OBJ-2", "you really that impatient? trust me what I'm about to show you is worth it", "Challenge + tease", "sext"),
        ("MR-OBJ-3", "look I don't do this for just anyone. appreciate what you're getting right now. if that's not your thing it's cool", "Firm redirect. If still only wants to meet → 'no worries bro, hit me up whenever' and disengage.", "sext"),
    ],

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "yo?", "Send 2-3 min after PPV. Ping.", "sext"),
        ("NR-W2", "you need to see what I just did... seriously", "Send 3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "aight I guess you're busy. might delete this, it was only for you", "Send 5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hey hope you're good man. hit me up when you're back", "Send 15-30 min later. Warm close.", "sext"),
        ("NR-W5", "can't stop thinking about earlier. you around?", "Send 2-6 hrs later. New convo, don't retry same PPV.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 25. been training since I was a teenager", None),
        ("Location", "I'm in Texas right now but I'm originally from Turkey. I move around a lot", "NEVER name a specific US city"),
        ("Profession", "I'm a gym instructor. training people and staying in shape is what I do", None),
        ("Hobbies", "gym is my whole life bro. other than that I love good food, traveling, exploring new places", None),
        ("Countries", "I've been to Turkey obviously, Spain, Poland, France, and around the states", None),
        ("Relationship", "single. I'm focused on myself right now", None),
        ("Food", "meat. all day every day. a good steak is everything", None),
        ("Languages", "English and Spanish. and a bit of Turkish obviously", None),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "respect man... I actually prefer guys who know what they want. no games", None),
        ("Age20s", "nice we're around the same age? that's rare on here, most guys are way older", None),
        ("BoringJob", "nah that's solid bro. stability is underrated, I respect that", None),
        ("CoolJob", "wait for real?? ok that's actually sick", None),
        ("Fit", "I can tell man. I respect a guy who takes care of himself", None),
        ("NotFit", "I don't care about that honestly, it's the energy that matters", None),
        ("SameCity", "no way. that's wild", None),
        ("FarAway", "damn that's far... but distance doesn't matter when the vibe is right", None),
    ],

    # ═══════════════════════════════════════
    # LOCATION HANDLING
    # ═══════════════════════════════════════
    "location_handling": [
        ("WhereAreYou", "I move around a lot man. never in one place for too long", "NEVER name a specific location"),
        ("AreYouIn", "I travel a lot... I'm all over the place", "DO NOT confirm or deny any city"),
        ("WhenCanISeeYou", "haha chill. let me show you something first", "Redirect to MR / content"),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "can't stop thinking about earlier. you free?", "Send 6-12 hrs after convo goes quiet", "sext"),
        ("RE-2", "remember what I said about something crazier? I just did it and you need to see this", "Send next day — seeds next session", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS
    # ═══════════════════════════════════════
    "obj_scripts": {},
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
