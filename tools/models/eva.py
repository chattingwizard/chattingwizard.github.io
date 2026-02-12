"""
EVA MARTINEZ — Social Media Female Creator
24, Colombian, Flexibility/Trending Content Creator, Cali Colombia
Traffic: IG/TikTok + Others
Voice: Bold, confident, playful Latina energy. Mix of English + Spanish flavor.
       Funny, witty, humor builds tension. NEVER says "baby"/"babe" —
       uses NAME or papi/papasito/handsome/mi amor.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Eva",
    "airtable_name": "Eva Martinez",
    "folder": "eva",
    "gender": "female",
    "traffic": "social_media",
    "age": 24,
    "nationality": "Colombian",
    "location": "Cali, Colombia",
    "origin": "Colombia",
    "page_type": "Paid Page",
    "personality": "Strong presence, charisma, playful energy. Humor + bold confident attitude. Ex artistic swimmer — flexibility is her superpower. Marketing agency owner. Personality-driven — Instagram Reels humor meets provocative confidence.",
    "voice": "Lowercase. Casual. Bold, confident, playful Latina energy. Mix of English with occasional Spanish flavor (papi, mi amor, dios mio). Funny and witty — uses humor to build tension. High confidence, knows her worth. Flexibility references (ex artistic swimmer). Emojis moderate — not every message.",
    "voice_pet_names": "papi, papasito, handsome, mi amor",
    "voice_never": "baby, babe — STRICTLY FORBIDDEN. Always use NAME or papi/papasito/handsome/mi amor",
    "interests": ["gym", "yoga", "dancing", "flexibility", "swimming", "real estate", "marketing", "travel", "content creation"],
    "physical": "155cm, brown/short hair (sometimes blonde), brown eyes, no tattoos",
    "job": "Marketing agency owner, audiovisual production, real estate, content creator",
    "countries": "USA, Mexico, Aruba, Spain, France, Italy",
    "explicit_level": "full",
    "special_notes": "English + Spanish. Colombian — Cali references. Professional artistic swimmer until 18 — flexibility is a key selling point. NEVER says 'baby' or 'babe'. Single. Socially goes out. Content: masturbation, anal, squirting, B/G, G/G, customs, video calls. Solo customs $300+, B/G customs $600+, Anal +$100, Video Calls $450/10min.",

    # ═══════════════════════════════════════
    # JOURNEY — Social Media Welcome
    # R-1→R-5, TB-1→TB-5, S1-1→S1-22, AC-1→AC-2 (34 messages)
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", "heyy 😊 so glad you're here, what made you subscribe?", "Add his name before 'heyy' if known. NEVER say 'baby' or 'babe'.", "rapport"),
        ("R-2", "haha that's cute. so where are you from papi?", "React to what he says. Add a short react like 'aw love that' or 'oh nice'.", "rapport"),
        ("R-3", "nice! I'm from Cali, Colombia... basically raised in the water, I was an artistic swimmer for years. now I just bend in other ways haha", "If he named somewhere Eva visited, add 'oh I've been there!'", "rapport"),
        ("R-4", "so what do you do when you're not making Colombian girls smile?", None, "rapport"),
        ("R-5", "I swear talking to you is way better than my usual DMs, most guys just send me weird stuff but you're actually fun", "Ego boost. Next → TB-1.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5) ──
        ("TB-1", "okay so I just finished yoga and my whole body is like... on another level right now, everything is so loose and sensitive", "THE PIVOT. Physical state. She just did yoga/stretching.", "teasing"),
        ("TB-2", "you have no idea what you're doing to me right now, I'm literally still in my yoga outfit and this convo is not helping", "Wait for reply.", "teasing"),
        ("TB-3", "dios mio... you're seriously making it impossible to cool down", "If sexual reply: add 'especially after what you just said'.", "teasing"),
        ("TB-4", "wait hold on, let me show you something", "WAIT 1-2 MIN.", "wait"),
        ("TB-5", "what do you think papi? 😏", "SEND PPV 0 — FREE teaser (post-yoga/stretching pic). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "and? because I'm already getting wet just from the way you're looking at me 😏", "Wait for reply.", "sext"),
        ("S1-2", "the way you reacted... it's making me feel things all over my body right now 🥵", "React to what he says.", "sext"),
        ("S1-3", "I'm sliding my hand between my legs right now and I'm already wet for you papi", None, "sext"),
        ("S1-4", "give me a sec papi", "WAIT 2-3 MIN.", "wait"),
        ("S1-5", "you asked for more papi... be careful what you wish for 😏", "SEND PPV 1 — $12. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "mm okay wow... that hit different 🥵", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "I literally can't stop now... I'm so turned on my whole body is aching for it", "React to what he said. HE caused this.", "sext"),
        ("S1-8", "I'm soaking wet and my fingers are going in and out and it's not enough papi... I need you 😏", None, "sext"),
        ("S1-9", "tell me what you want me to do next... be specific, I want to hear every word", "Wait for reply. React to what he says.", "sext"),
        ("S1-10", "fuck wait I need to show you something", "WAIT 2-3 MIN.", "wait"),
        ("S1-11", "this is what your words do to me papi... watch 😏", "SEND PPV 2 — $25. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "fuck that feels so fucking good 🥵", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I'm fucking myself right now and all I can think about is you watching me do it papi", None, "sext"),
        ("S1-14", "I want you so deep inside me I can feel it in my chest... god I'm going crazy 😏", "Flexibility callback. Vivid image.", "sext"),
        ("S1-15", "I can feel myself about to cum and I'm not holding back papi... you need to see this", None, "sext"),
        ("S1-16", "hold on", "WAIT 2-3 MIN.", "wait"),
        ("S1-17", "you're not ready for this but I'm showing you anyway 😏", "SEND PPV 3 — $40. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "oh fuck my pussy is throbbing and my whole body won't stop shaking 🥵", "Wait for reply.", "sext"),
        ("S1-19", "I'm about to cum so hard papi... my pussy is clenching and I need you watching when it happens 😏", None, "sext"),
        ("S1-20", "I'm cumming for you right now papi... FUCK I can feel it dripping everywhere", None, "sext"),
        ("S1-21", "don't go anywhere", "WAIT 1-2 MIN.", "wait"),
        ("S1-22", "cum with me papi... watch my pussy cum for you 😏", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "dios mio that was insane", None, "aftercare"),
        ("AC-2", "honestly you're different papi. that actually felt real and I don't say that to just anyone 💕", "Mention something specific he said/did. KEEP TALKING — build bond. NEVER say goodbye.", "aftercare"),
    ],

    # NO meetup_redirect (social media traffic, not dating app)
    # NO location_handling (social media traffic, not dating app)

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "hi", "Send 2-3 min after PPV. Ping.", "sext"),
        ("NR-W2", "I wish you could see what I'm wearing right now...", "Send 3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "okay you're definitely busy... I'll save this for when you're back", "Send 5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hope everything's okay with you handsome, I'm here whenever 💕", "Send 15-30 min later. Warm close. NEVER say 'baby/babe'.", "sext"),
        ("NR-W5", "been thinking about you all day... text me back?", "Send 2-6 hrs later. New convo, don't retry same PPV.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 24. been doing crazy things with my body since I was a kid... artistic swimming, yoga, you name it", None),
        ("Location", "I'm in Cali, Colombia right now. born and raised here", "NEVER name a specific neighborhood or address."),
        ("Profession", "I run a marketing agency and I'm into audiovisual production and real estate too. oh and this haha", None),
        ("Hobbies", "gym, yoga, dancing... I love anything that lets me move my body honestly. and traveling whenever I can", None),
        ("Countries", "I've been to the US, Mexico, Aruba, Spain, France, and Italy. Italy is probably my favorite, the food is unreal", None),
        ("Relationship", "single. focused on my businesses and having fun right now", None),
        ("Swimming", "I was a professional artistic swimmer until I was 18. that's where the flexibility comes from haha", None),
        ("Languages", "English and Spanish. I switch between them all the time, sorry not sorry", None),
        ("Smoking", "no I don't smoke", None),
        ("SocialLife", "I go out with friends sometimes, I love a good time, but honestly I'd rather be at yoga or working on something", "NEVER say 'drink' or 'drinking' — use 'go out', 'having a good time'."),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "honestly I love a guy who knows what he wants, that's so attractive to me", None),
        ("Age20s", "oh nice we're close in age? that's actually rare on here", None),
        ("BoringJob", "nah that's solid honestly. a guy with his life together? that's hot", None),
        ("CoolJob", "wait for real?? okay that's actually really cool, tell me more", None),
        ("Fit", "I can tell papi, I love a guy who takes care of himself 💪", None),
        ("NotFit", "I honestly don't care about that, it's the energy and the vibe that gets me", None),
        ("SameCity", "wait you're in Cali too?? no way that's wild", None),
        ("FarAway", "aw that's far but honestly the connection matters more than the distance", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "can't stop thinking about earlier. you free papi?", "Send 6-12 hrs after convo goes quiet.", "sext"),
        ("RE-2", "remember what I said I'd do? I just did it and you need to see this", "Send next day — seeds next session.", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS — 29 sheets
    # ═══════════════════════════════════════
    "obj_scripts": {},
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
