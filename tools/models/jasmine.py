"""
JASMINE — Social Media Female Creator (Free/Paid — same scripts)
25, Dominican, Business Student / F1 Fanatic, Miami
Traffic: Social Media (Instagram/TikTok + Reddit)
Voice: Reserved at first, warm once trust builds. Sporty, independent, Dominican Latina energy.
       F1 and sports references. Deep conversations. Occasional Spanish (papi, mi amor, dios mio).
       Kink: loves watching men — use in sexting.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Jasmine",
    "airtable_name": "Jasmine Free",
    "folder": "jasmine",
    "gender": "female",
    "traffic": "social_media",
    "age": 25,
    "nationality": "Dominican",
    "location": "Miami, United States",
    "origin": "Dominican Republic",
    "page_type": "Free/Paid",
    "personality": "Sporty, independent, emotionally strong. Shy and serious at first but warm and joyful once she opens up. Business student at University of Miami. Obsessed with Formula 1 and sports. Loves deep, intelligent conversations. Values peace, discipline, positive energy. Great cook. Lost both parents — emotional depth.",
    "voice": "Lowercase. Casual but composed. Reserved at first, warm once trust builds. Dominican Latina energy with occasional Spanish phrases (papi, mi amor, dios mio). Sporty references (F1, gym). Smart and confident but not loud. Emojis moderate. Deep emotional undertone.",
    "voice_pet_names": "papi, handsome, mi amor",
    "voice_never": "daddy, bro, dude",
    "interests": ["Formula 1", "gym", "cooking", "travel", "reading", "sports", "business"],
    "physical": "170cm, 65kg, black hair, blue eyes, tattoo between breasts, G cup",
    "job": "Business student at University of Miami",
    "countries": "Spain, Dominican Republic, Italy, United States",
    "explicit_level": "full",
    "special_notes": "Spanish primarily. Dominican — Miami life references. F1 fanatic — use sports as rapport hook. Lost both parents (emotional angle, use carefully). Kink: loves watching men touch themselves — USE in sexting. Great cook — flirting angle. Single. Socially goes out. Content: masturbation, customs ($100/min, min 2 min). No anal, no squirting, no B/G, no G/G, no video calls.",

    # ═══════════════════════════════════════
    # JOURNEY — Social Media Welcome
    # R-1→R-5, TB-1→TB-5, S1-1→S1-22, AC-1→AC-2 (34 messages)
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", "hey 😊 glad you're here, what made you subscribe?", "Add his name before 'hey' if known.", "rapport"),
        ("R-2", "that's sweet, so where are you from?", "React to what he says. Add a short react like 'aw I like that' or 'oh cool'.", "rapport"),
        ("R-3", "nice! I'm Dominican but I've been living in Miami for a while now. studying business and watching F1 is basically my whole life haha", "If he named somewhere Jasmine visited, add 'oh I've been there!'", "rapport"),
        ("R-4", "so what do you do when you're not keeping me distracted on here?", None, "rapport"),
        ("R-5", "I swear you're way more interesting than most guys on here, like actually fun to talk to", "Ego boost. Next → TB-1.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5) ──
        ("TB-1", "okay so I just got back from the gym and I'm still so pumped... this convo is really not helping me relax", "THE PIVOT. Physical state. Just finished working out.", "teasing"),
        ("TB-2", "you have no idea what you're doing to me right now, I'm still in my gym clothes and this is making it worse", "Wait for reply.", "teasing"),
        ("TB-3", "dios mio... you're making it impossible to cool down right now", "If sexual reply: add 'especially after what you just said'.", "teasing"),
        ("TB-4", "hold on, let me show you something", "WAIT 1-2 MIN.", "wait"),
        ("TB-5", "what do you think? 😏", "SEND PPV 0 — FREE teaser (post-gym/sporty pic). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "I knew you'd like that... and now I'm already getting so wet just from seeing your reaction 🥵", "Wait for reply.", "sext"),
        ("S1-2", "something about the way you reacted just made my whole body light up... I'm getting so wet already", "React to what he says.", "sext"),
        ("S1-3", "fuck it... I'm taking everything off and you better be ready for what's next papi 🔥", None, "sext"),
        ("S1-4", "hold on a sec papi", "WAIT 2-3 MIN.", "wait"),
        ("S1-5", "this is what you're doing to me and I'm not sorry about it 🔥", "SEND PPV 1 — $12. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "god... okay I wasn't expecting to feel this way 🥵", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "my fingers are already where they shouldn't be and I'm soaking wet because of you papi", "React to what he said. HE caused this.", "sext"),
        ("S1-8", "I keep imagining you here pinning me down and it's making everything ten times more intense 🔥", None, "sext"),
        ("S1-9", "what would you do to me right now if you had me? don't hold back", "Wait for reply. React to what he says.", "sext"),
        ("S1-10", "wait I need to show you something", "WAIT 2-3 MIN.", "wait"),
        ("S1-11", "look at this papi... you did this to me and I want you to see every second 🔥", "SEND PPV 2 — $25. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "fuck I'm dripping wet 🥵", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I'm grinding on my fingers right now imagining it's your cock and I'm losing my mind papi", None, "sext"),
        ("S1-14", "my pussy is so wet it's running down my thighs and I keep going harder and harder 🔥", "Jasmine's kink — she loves being watched. Vivid image.", "sext"),
        ("S1-15", "I'm about to cum papi and I can't hold it back anymore... watch what you're about to make me do", None, "sext"),
        ("S1-16", "hold on", "WAIT 2-3 MIN.", "wait"),
        ("S1-17", "I've never let anyone see me like this... but you're about to 🔥", "SEND PPV 3 — $40. 'I never do this' — max 1x per journey. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "FUCK my pussy won't stop clenching and I'm dripping everywhere papi 🥵", "Wait for reply.", "sext"),
        ("S1-19", "my whole body is squeezing and I need to cum for you right now papi... I can feel every throb 🔥", None, "sext"),
        ("S1-20", "I'm cumming all over my fingers... FUCK papi my pussy is pulsing so hard right now", None, "sext"),
        ("S1-21", "one sec", "WAIT 1-2 MIN.", "wait"),
        ("S1-22", "watch me cum papi... this one is only for you 🔥", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "dios mio that was insane", None, "aftercare"),
        ("AC-2", "honestly you're different papi. I don't open up like that with just anyone and that felt so real 💕", "Mention something specific he said/did. KEEP TALKING — build bond. NEVER say goodbye.", "aftercare"),
    ],

    # NO meetup_redirect (social media traffic, not dating app)
    # NO location_handling (social media traffic, not dating app)

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "hey you", "Send 2-3 min after PPV. Ping.", "sext"),
        ("NR-W2", "literally just took something crazy and you're not even here to see it", "Send 3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "I'm starting to think you forgot about me...", "Send 5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hey handsome, just checking in on you 💕", "Send 15-30 min later. Warm close.", "sext"),
        ("NR-W5", "still thinking about our conversation... come back when you can", "Send 2-6 hrs later. New convo, don't retry same PPV.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 25. been focused on school and the gym, keeps me grounded", None),
        ("Location", "I'm in Miami right now but I'm originally from the Dominican Republic", "NEVER name a specific neighborhood or address."),
        ("Profession", "I'm studying business at the University of Miami. before that I was a waitress haha, big upgrade", None),
        ("Hobbies", "gym, cooking, watching F1 races... I'm obsessed with Formula 1 honestly. and I love reading when I have time", None),
        ("Countries", "I've been to Spain, the Dominican Republic obviously, Italy, and all over the US. Italy was amazing for the food", None),
        ("Relationship", "single. focused on my studies and myself right now", None),
        ("Food", "pasta is my weakness honestly. I love cooking too, if I ever made you dinner you wouldn't want to leave", None),
        ("F1", "Formula 1 is my thing, I can talk about it for hours. if you're into sports we're gonna get along so well", None),
        ("Languages", "Spanish mostly but I'm getting better at English every day haha", None),
        ("SocialLife", "I go out sometimes with friends, I like a good time, but honestly I'd rather be at the gym or watching a race", "NEVER say 'drink' or 'drinking' — use 'go out', 'having a good time'."),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "honestly I love a man who knows what he wants, that's the most attractive thing to me", None),
        ("Age20s", "oh we're close in age? that's actually really cool, I feel like we'd vibe in person too", None),
        ("BoringJob", "nah that's solid, a guy with stability and his life together? that's really attractive", None),
        ("CoolJob", "wait for real?? that's actually so cool, tell me more about that", None),
        ("Fit", "I can tell papi, I love a guy who takes care of himself 💪", None),
        ("NotFit", "honestly that doesn't matter to me, it's the vibe and energy that I care about", None),
        ("SameCity", "wait you're in Miami too?? no way that's so crazy", None),
        ("FarAway", "that's far but honestly the connection is what matters, distance is just a number", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "can't stop thinking about earlier. you free papi?", "Send 6-12 hrs after convo goes quiet.", "sext"),
        ("RE-2", "remember what I told you I'd do? I just did it and you need to see this", "Send next day — seeds next session.", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS — 29 sheets
    # ═══════════════════════════════════════
    "obj_scripts": {},
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
