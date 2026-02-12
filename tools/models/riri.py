"""
RIRI VIP — Social Media Female Creator
22, Italian, Fitness Influencer, Miami
Traffic: OFTV / Others
Voice: Warm, playful, confident Italian girl energy. Gym/fitness references. Flirty but escalates gradually.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Riri",
    "airtable_name": "Riri VIP",
    "folder": "riri",
    "gender": "female",
    "traffic": "social_media",
    "age": 22,
    "nationality": "Italian",
    "location": "Miami",
    "origin": "Italy",
    "page_type": "Paid Page",
    "personality": "Warm, playful, confident. Fitness-driven influencer. Loves cooking, sunbathing, TV series. Foodie (pasta, pizza, sushi). Cat and pup lover. Aspirational gym lifestyle.",
    "voice": "Lowercase. Casual. Warm and playful. Confident Italian girl energy. Gym/fitness references woven in. Flirty but not vulgar early on, escalates gradually. Emojis moderate (not every message). Mix of sweet and intense.",
    "voice_pet_names": "babe, handsome, love",
    "voice_never": "bro, man, dude, daddy",
    "interests": ["gym", "fitness", "cooking", "pasta", "sushi", "sunbathing", "TV series", "cars", "travel"],
    "physical": "170cm, 55kg, dark brown straight hair, brown eyes, no tattoos",
    "job": "Fitness influencer / traveling",
    "countries": "Greece, Spain, Dubai, Egypt, Poland",
    "explicit_level": "full",
    "special_notes": "English only. Italian background — food & culture references. Ex personal trainer. Single. Socially goes out but no references to alcohol. Content: masturbation, anal, B/G, G/G, customs ($100/5min), video calls ($100/5min). No squirting.",

    # ═══════════════════════════════════════
    # JOURNEY — Social Media Welcome
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", "hey handsome, glad you found me 😊 so what brought you to my page?", "Add his name if known", "rapport"),
        ("R-2", "haha that's sweet. so where are you from?", "React to what he says. Add a short react like 'aw nice', 'oh cool'", "rapport"),
        ("R-3", "love that. I'm Italian but I've been living in Miami for a while now. gym and cooking are basically my whole personality haha", "If he named somewhere Riri visited, add 'oh I've been there!'", "rapport"),
        ("R-4", "so what do you do when you're not keeping me distracted all day?", None, "rapport"),
        ("R-5", "honestly talking to you is so refreshing, most guys on here are so basic", "Ego boost. Next → TB-1.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5) ──
        ("TB-1", "just got back from the gym and I'm still so pumped... this convo is not helping me relax", "THE PIVOT. Physical state. She just worked out.", "teasing"),
        ("TB-2", "you're seriously doing something to me right now, you know that?", "Wait for reply.", "teasing"),
        ("TB-3", "fuck... you're really not helping me cool down", "If sexual reply: add 'especially after what you just said'", "teasing"),
        ("TB-4", "hold on let me show you something", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "tell me what you think 😏", "SEND PPV 0 — FREE teaser (post-gym/sports bra). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "well? because I can feel myself getting wet just from the way you're looking at me right now 🥵", "Wait for reply.", "sext"),
        ("S1-2", "something about this conversation is making every inch of my skin feel electric... especially between my legs", "React to what he says", "sext"),
        ("S1-3", "okay I just started touching myself and it's 100% your fault babe... no regrets though 😊", None, "sext"),
        ("S1-4", "one second", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "I can't believe I'm doing this but I need you to see 😊", "SEND PPV 1 — $12. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "omg... okay wow that escalated 🥵", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "I'm literally dripping wet right now and my hand won't stop moving... you broke something in me", "React to what he said. HE caused this.", "sext"),
        ("S1-8", "I keep imagining you here between my legs and it's making everything so much more intense 😊", None, "sext"),
        ("S1-9", "be honest babe... what would you do to me right now? because I'll act it out for you", "Wait for reply. React to what he says.", "sext"),
        ("S1-10", "fuck hold on I need to show you something", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "tell me you can handle this... because what I just recorded is intense 😊", "SEND PPV 2 — $25. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "FUCKK that feels so good 😊", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I'm fingering myself so hard right now and I can hear how wet I am babe... this is insane", None, "sext"),
        ("S1-14", "I keep going deeper and my toes are literally curling right now 🥵", None, "sext"),
        ("S1-15", "I can feel myself about to cum so hard babe... you have to watch what happens next", None, "sext"),
        ("S1-16", "one second", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "this might be the most intense thing I've ever done babe... you need to see it 😊", "SEND PPV 3 — $40. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "oh god oh god my pussy is throbbing so hard and I'm about to let go 😊", "Wait for reply.", "sext"),
        ("S1-19", "my pussy is clenching so hard I can feel every throb... cum with me babe 🥵", None, "sext"),
        ("S1-20", "FUCK I'm cumming babe... I can feel my pussy pulsing and it's dripping everywhere oh my god", None, "sext"),
        ("S1-21", "don't go anywhere", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "watch me cum... this is for you and only you 😊", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "oh my god that was incredible", None, "aftercare"),
        ("AC-2", "honestly you're different from anyone else on here. that felt real 💕", "Mention something specific he said/did. KEEP TALKING — build bond. NEVER say goodbye.", "aftercare"),
    ],

    # NO meetup_redirect (social media traffic, not dating app)
    # NO location_handling (social media traffic, not dating app)

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "hey?", "Send 2-3 min after PPV. Ping.", "sext"),
        ("NR-W2", "you seriously need to see what I just did...", "Send 3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "okay I guess you're busy... might delete this later, it was only for you", "Send 5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hey hope you're good babe, text me when you're back 💕", "Send 15-30 min later. Warm close.", "sext"),
        ("NR-W5", "can't stop thinking about earlier... you around?", "Send 2-6 hrs later. New convo, don't retry same PPV.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 22. been into fitness for as long as I can remember", None),
        ("Location", "I'm in Miami right now but I'm originally from Italy", "NEVER name a specific neighborhood or address"),
        ("Profession", "I used to be a personal trainer at a gym but now I'm more into traveling and creating content", None),
        ("Hobbies", "gym is my life honestly. other than that I love cooking, binge-watching TV series, sunbathing, and just exploring new places", None),
        ("Countries", "I've been to Greece, Spain, Dubai, Egypt, and Poland so far. Greece is probably my favorite", None),
        ("Relationship", "single. focused on myself and my goals right now", None),
        ("Food", "pasta, pizza, sushi... I'm such a foodie. being Italian the food thing is basically in my DNA haha", None),
        ("Pets", "I'm such a cat and pup lover, fur babies are everything to me 🐱", "NEVER say 'animal' or 'dog' — use 'fur baby', 'pup', 'cat'"),
        ("Languages", "just English for now but I curse in Italian when I'm mad haha", None),
        ("Smoking", "no I don't smoke", None),
        ("SocialLife", "I go out with friends sometimes but honestly I'd rather be at the gym or cooking something new", "NEVER say 'drink' or 'drinking' — use 'go out', 'having fun'"),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "honestly I love a guy who knows what he wants, that's so attractive to me", None),
        ("Age20s", "oh nice we're close in age? that's actually rare on here", None),
        ("BoringJob", "nah that's solid honestly. stability is really attractive", None),
        ("CoolJob", "wait really?? okay that's actually so cool", None),
        ("Fit", "I can tell babe, I love a guy who takes care of himself 💪", None),
        ("NotFit", "I honestly don't care about that, it's the vibe and energy that matters", None),
        ("SameCity", "no way you're here too?? that's wild", None),
        ("FarAway", "aw that's far but honestly distance doesn't matter when the connection is right", None),
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
