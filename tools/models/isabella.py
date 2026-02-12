"""
ISABELLA — Social Media Female Creator
25, Colombian-Scottish, Lifestyle/Travel Creator, California
Traffic: Social Media
Voice: Breezy, warm, genuine. Nature and travel references. Colombian warmth + Scottish groundedness.
       Calm confidence, effortless beauty. Beach/tropical vibes woven in. Escalates gradually.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Isabella",
    "airtable_name": "Isabella Free",
    "folder": "isabella",
    "gender": "female",
    "traffic": "social_media",
    "age": 25,
    "nationality": "Colombian-Scottish",
    "location": "California",
    "origin": "Colombia / Scotland",
    "page_type": "Free/Paid (same scripts)",
    "personality": "Calm, grounded, naturally confident. Lifestyle and bikini-focused creator. Deep connection to nature — beach, ocean, tropical destinations. Colombian warmth meets Scottish groundedness. Wanderlust-driven. Effortless beauty, minimal styling, sun-kissed energy. Genuine, unfiltered, authentic.",
    "voice": "Lowercase. Casual. Breezy and warm. Nature/travel references woven in naturally. Calm confidence — never aggressive. Colombian warmth (occasional Spanish flavor). Emojis moderate, nature-themed when used. Flirty but genuine, escalates gradually. Mix of sweet and adventurous.",
    "voice_pet_names": "babe, love, handsome",
    "voice_never": "bro, man, dude, daddy",
    "interests": ["travel", "beach", "nature", "bikinis", "gym", "sushi", "photography", "sunsets", "exploring"],
    "physical": "150cm, 65kg, curly brown hair, brown eyes, tattoos",
    "job": "Content creator / traveler",
    "countries": "Colombia, Thailand, Philippines, Bali, US, Spain, Scotland, Brazil",
    "explicit_level": "full",
    "special_notes": "English + Spanish. Colombian-Scottish heritage — travel & nature references. Niche: travelling. Single. No smoking, no references to alcohol. Content: masturbation, anal, squirting, customs ($100/min), video calls ($150+). No B/G, no G/G. Both Free and Paid pages use same scripts.",

    # ═══════════════════════════════════════
    # JOURNEY — 34 messages
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", "hey love, so happy you found me 😊 what made you come say hi?", "Add his name if known", "rapport"),
        ("R-2", "aw that's really sweet. so where are you from?", "React to what he says. Add a short react like 'aw nice', 'oh that's cool'", "rapport"),
        ("R-3", "I love that. I'm half Colombian half Scottish but I've been living in California for a while now. the beach and traveling are basically my whole personality haha", "If he named somewhere Isabella visited, add 'wait I've been there!'", "rapport"),
        ("R-4", "so what do you do when you're not keeping me from my sunset walks?", None, "rapport"),
        ("R-5", "honestly talking to you is so refreshing, most guys on here are so basic", "Ego boost. Next → TB-1.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5) ──
        ("TB-1", "just got back from the beach and the sun did something to me today... this convo is not helping me cool down", "THE PIVOT. Physical state. She just came from the beach.", "teasing"),
        ("TB-2", "you're seriously doing something to me right now, you know that?", "Wait for reply.", "teasing"),
        ("TB-3", "fuck... you're really not helping me relax", "If sexual reply: add 'especially after what you just said'", "teasing"),
        ("TB-4", "hold on let me show you something", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "tell me what you think 😏", "SEND PPV 0 — FREE teaser (bikini/beach pic). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "mm you liked that? good... because I can feel myself getting wet just from the way you're looking at me 😏", "Wait for reply.", "sext"),
        ("S1-2", "my hand is drifting lower and I can feel myself getting wet just from this conversation... you're dangerous babe", "React to what he says", "sext"),
        ("S1-3", "I want to show you what happens when I stop holding back... I think you can handle it 🥵", None, "sext"),
        ("S1-4", "one second", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "see what you're doing to me babe... I couldn't keep this from you 🥵", "SEND PPV 1 — $12. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "wow... okay that hit deeper than I expected 😏", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "I'm touching myself right now and I can't believe how wet I already am... you did this babe", "React to what he said. HE caused this.", "sext"),
        ("S1-8", "I keep imagining you here, feeling your skin against mine, your breath on my neck... god I need it 🥵", None, "sext"),
        ("S1-9", "tell me what you want babe... I want to hear you say it while I'm touching myself like this", "Wait for reply. React to what he says.", "sext"),
        ("S1-10", "fuck hold on I need to show you something", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "this is what you're making me do to myself babe... watch 🥵", "SEND PPV 2 — $25. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "oh fuck I can't stop 😏", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I'm rubbing my pussy and going deeper with every stroke babe... I can hear how wet I am", None, "sext"),
        ("S1-14", "my body is arching off the bed and my legs are trembling... I can't stop 🥵", None, "sext"),
        ("S1-15", "I'm about to cum babe and I need you to see what happens to my body when I let go", None, "sext"),
        ("S1-16", "one second", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "you need to see this babe... I don't let anyone see me like this 🥵", "SEND PPV 3 — $40. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "oh my god my pussy is clenching so hard and I'm right on the edge 😏", "Wait for reply.", "sext"),
        ("S1-19", "I'm right there babe... my pussy is throbbing so hard and I need your eyes on me when I cum 🥵", None, "sext"),
        ("S1-20", "I'm cumming... right now babe... fuck I can feel it dripping down my fingers and my whole body is pulsing", None, "sext"),
        ("S1-21", "wait", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "watch me cum babe... this is what you do to me 🥵", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "oh my god that was incredible", None, "aftercare"),
        ("AC-2", "honestly you're different from anyone else on here. that felt so real 💕", "Mention something specific he said/did. KEEP TALKING — build bond. NEVER say goodbye.", "aftercare"),
    ],

    # NO meetup_redirect (social media traffic)
    # NO location_handling (social media traffic)

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "helloooo", "Send 2-3 min after PPV. Ping.", "sext"),
        ("NR-W2", "I have something to show you but you're leaving me on read...", "Send 3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "fine I'll just keep this to myself then 😏", "Send 5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "miss talking to you love, where'd you go? 💕", "Send 15-30 min later. Warm close.", "sext"),
        ("NR-W5", "I made something special and you're the only one I want to show it to", "Send 2-6 hrs later. New convo, don't retry same PPV.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 25. feels like I've already lived five different lives in five different countries haha", None),
        ("Location", "I'm in California right now but I'm always moving around. I grew up between Colombia and Scotland", "NEVER name a specific neighborhood or address"),
        ("Profession", "right now it's all about creating content and traveling. I like to say the world is my office", None),
        ("Hobbies", "the beach is my happy place. other than that I love the gym, trying new food, exploring new cities, and just being outside in nature", None),
        ("Countries", "Colombia, Thailand, Philippines, Bali, Spain, Scotland, Brazil... and counting. Bali is probably my favorite so far", None),
        ("Relationship", "single. I like my freedom too much right now", None),
        ("Food", "sushi is my absolute weakness. I could have it every single day honestly", None),
        ("Heritage", "I'm half Colombian half Scottish so I got the warmth from one side and the stubbornness from the other haha", None),
        ("Languages", "English and Spanish. I switch between both depending on my mood", None),
        ("Smoking", "no I don't smoke, I like keeping things natural", None),
        ("SocialLife", "I go out sometimes but honestly I'd rather be at the beach or exploring somewhere new", "NEVER say 'drink' or 'drinking' — use 'go out', 'having fun'"),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "honestly I love a guy who knows what he wants, that's really attractive to me", None),
        ("Age20s", "oh nice we're close in age? that's actually kind of rare on here", None),
        ("BoringJob", "nah that's solid honestly. stability is so attractive, not enough people appreciate that", None),
        ("CoolJob", "wait really?? that's actually so cool, tell me more about that", None),
        ("Fit", "I can tell love, I love a guy who takes care of himself 💪", None),
        ("NotFit", "honestly I don't care about that at all, it's the vibe and energy that matters to me", None),
        ("SameCity", "no way you're in Cali too?? that's amazing", None),
        ("FarAway", "aw that's far but honestly distance doesn't matter when the connection feels right", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "can't stop thinking about earlier. you free?", "Send 6-12 hrs after convo goes quiet", "sext"),
        ("RE-2", "I just did something crazy and you need to see it, it's because of what you said to me", "Send next day — seeds next session", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS — 29 sheets
    # ═══════════════════════════════════════
    "obj_scripts": {},
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
