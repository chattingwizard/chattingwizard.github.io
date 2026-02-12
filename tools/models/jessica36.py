"""
JESSICA FREE/PAID (36) — Explicit Female Creator
36, Argentinian, Tucuman. Reddit + IG/TikTok traffic.
Gym instructor, single mom (Alice 17). Serious about fitness, open-minded underneath.
Loves sailing. Spanish + English.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "JessicaFP",
    "airtable_name": "Jessica Free",
    "folder": "jessica-fp",
    "gender": "female",
    "traffic": "social_media",
    "age": 36,
    "nationality": "Argentinian",
    "location": "Tucuman, Argentina",
    "origin": "Argentina",
    "page_type": "Free/Paid (same scripts)",
    "personality": "Serious and disciplined about fitness. Strict exterior but open-minded, rebellious once comfortable. Passionate gym instructor. Dedicated single mom. Loves sailing. Determined, independent.",
    "voice": "Direct, confident, warm underneath. Slight Spanish flavor but mostly English. Fitness references natural. Disciplined energy that softens into sensual. Pet names used sparingly.",
    "voice_pet_names": "babe, amor, handsome",
    "voice_never": "daddy, papi — too close to her parenting role",
    "interests": ["gym", "fitness coaching", "sailing", "tango", "healthy cooking"],
    "physical": "170cm, 65kg, brown hair, brown eyes, no tattoos, C cup",
    "job": "Gym instructor",
    "countries": "Argentina",
    "explicit_level": "full",
    "special_notes": "Single mom (daughter Alice). NEVER mention or reference her child in sexual context. Customs: Solo, Toys, JOI, B/G (tell fan she needs to find someone). Sailing is her passion.",

    # ═══════════════════════════════════════
    # JOURNEY
    # ═══════════════════════════════════════
    "journey": [
        # Rapport
        ("R-1", "hey, glad you're here 😊 so what caught your eye?", "Add his name if known", "rapport"),
        ("R-2", "haha I like that. so where are you from?", "React naturally.", "rapport"),
        ("R-3", "nice! I'm from Tucuman, Argentina. gym instructor by day but sailing is really my passion... there's nothing like being out on the water", "If he mentions somewhere she knows, react.", "rapport"),
        ("R-4", "so what do you do when you're not making my phone blow up?", None, "rapport"),
        ("R-5", "I barely get free time with everything I have going on but honestly? I'd rather spend it talking to you than anyone else right now", "Ego boost. Hints at responsibilities (single mom) without details. Transition.", "rapport"),

        # Teasing Bridge
        ("TB-1", "I just came back from tango class and I'm still buzzing... everything feels so sensual right now and I keep thinking about you", "THE PIVOT. Tango = physical/sensual bridge.", "teasing"),
        ("TB-2", "something about talking to you right after working out is hitting different right now", "Wait for reply.", "teasing"),
        ("TB-3", "ugh you're not helping me calm down at all honestly", "Playful frustration.", "teasing"),
        ("TB-4", "hold on I want to show you something", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "tell me what you think of this", "SEND PPV 0 — FREE teaser (post-gym selfie, sweaty, fit). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # Sexting Phase 1 → PPV 1
        ("S1-1", "I could tell you'd like that... and your reaction is making me so wet right now, way more than I expected 😏", "Wait for reply.", "sext"),
        ("S1-2", "I'm lying here with my hand between my thighs and it's because this conversation is getting to me", "React to what he says.", "sext"),
        ("S1-3", "I know exactly what I want right now amor and it starts with you watching what I do next 🥵", None, "sext"),
        ("S1-4", "hold on a sec", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "look what you started amor... you have no idea what's coming next 🥵", "SEND PPV 1 — $12. Bought → continue. Silent → NR Waves.", "ppv"),

        # Sexting Phase 2 → PPV 2
        ("S1-6", "dios... that was intense but I'm just getting started 😏", "Wait for reply.", "sext"),
        ("S1-7", "I'm so wet right now I can feel it on my thighs... this is what you do to me amor", "He caused this.", "sext"),
        ("S1-8", "I need to feel something inside me right now... I keep imagining it's you and it's driving me crazy 🥵", None, "sext"),
        ("S1-9", "tell me what you'd do to me right now amor... I want to hear every dirty detail", "Wait for reply. React.", "sext"),
        ("S1-10", "hold on... I need to show you something", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "mira lo que me haces amor... this is what you do to me 🥵", "SEND PPV 2 — $25. Bought → continue. Silent → NR Waves.", "ppv"),

        # Sexting Phase 3 → PPV 3
        ("S1-12", "FUCK I need more 😏", "Wait for reply. Keep momentum.", "sext"),
        ("S1-13", "I'm fucking myself right now and all I can picture is your face between my legs... dios mio", None, "sext"),
        ("S1-14", "my fingers are going so deep and fast and I can feel every wave building inside me 🥵", None, "sext"),
        ("S1-15", "I'm about to cum amor and what you're about to see you'll never forget... watch this", None, "sext"),
        ("S1-16", "hold on a sec", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "you're about to see something I don't show anyone amor... this is all because of you 🥵", "SEND PPV 3 — $40. Bought → continue. Silent → NR Waves.", "ppv"),

        # Sexting Phase 4 → PPV 4
        ("S1-18", "dios mio my pussy is throbbing and I can't stop shaking 😏", "Wait for reply.", "sext"),
        ("S1-19", "my pussy is squeezing so hard amor... I'm about to cum and I need you feeling every second 🥵", None, "sext"),
        ("S1-20", "I'm cumming for you amor... fuck I can feel my pussy pulsing and dripping all over my hand", None, "sext"),
        ("S1-21", "hold on hold on", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "watch me cum amor... every last second of it 🥵", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # Aftercare
        ("AC-1", "dios mio that was incredible", None, "aftercare"),
        ("AC-2", "I seriously needed that mi amor. you're different from everyone else on here, that was real", "Mention something specific. Build bond. KEEP TALKING.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "hey? 😏", "Send 2-3 min after PPV.", "sext"),
        ("NR-W2", "you seriously need to see what I just did...", "3-5 min later.", "sext"),
        ("NR-W3", "okay I guess you're busy... might delete this later, it was only for you", "5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hey hope you're good, text me when you're back 😊", "15-30 min later.", "sext"),
        ("NR-W5", "can't stop thinking about earlier... you around?", "2-6 hrs later.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 36. honestly I feel better now than I did at 25", None),
        ("Location", "I'm in Tucuman, Argentina. it's beautiful here", None),
        ("Profession", "I'm a gym instructor, fitness is my life honestly", None),
        ("Hobbies", "gym obviously, but I also love sailing. there's nothing like being on the water", None),
        ("Food", "pasta is life. I'm Argentinian, what can I say? haha", None),
        ("Relationship", "single and focused on myself right now", "NEVER mention her daughter in sexual context."),
        ("Languages", "Spanish and English. I switch between both all the time", None),
        ("Sailing", "I used to teach sailing actually, it was one of my favorite things. I miss it sometimes", None),
        ("Dream", "if I had more time I'd learn tango or pick up the saxophone", None),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "I actually prefer older guys, maturity is so attractive to me", None),
        ("Age20s", "love that energy, you keep me feeling alive haha", None),
        ("BoringJob", "honestly I respect that, stability is underrated", None),
        ("CoolJob", "wait for real?? okay that's actually impressive", None),
        ("Fit", "I can tell you take care of yourself and I love that about you", None),
        ("NotFit", "I don't care about that, the energy is what matters and yours is perfect", None),
        ("SameCountry", "no way! that's amazing 😊", None),
        ("FarAway", "distance doesn't matter when the connection is this good", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "just got back from the marina and can't stop thinking about you... you free?", "Send 6-12 hrs later.", "sext"),
        ("RE-2", "I just did something I've never done before and you need to see it", "Next day.", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS
    # ═══════════════════════════════════════
    "obj_scripts": {},
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
