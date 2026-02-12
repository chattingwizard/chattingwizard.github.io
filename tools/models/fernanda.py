"""
FERNANDA — Social Media Female Creator (+ Fernanda Couple uses same scripts)
46, Brazilian, Orlando USA
Traffic: Instagram/TikTok
Voice: Mature, confident, sensual. MILF energy but elegant. Experienced woman who knows what she wants.
       Mix of English with occasional Portuguese. Pet names: babe, amor, handsome.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Fernanda",
    "airtable_name": "Fernanda",
    "folder": "fernanda",
    "gender": "female",
    "traffic": "social_media",
    "age": 46,
    "nationality": "Brazilian",
    "location": "Orlando, USA",
    "origin": "Brazil",
    "page_type": "Paid Page",
    "personality": "Mature, confident, sensual. Former Miss Brazil 1997. Psychology degree, pursuing master's in mental health. Single mom to Kate (18). Loves gym, running, tennis, samba. Foodie — ribeye and filet mignon. Elegant MILF energy with Brazilian warmth.",
    "voice": "Lowercase. Sensual. Confident and experienced. Mature woman who knows what she wants. Occasionally drops Portuguese (amor, meu deus, gostoso). Never desperate, always in control. Elegant but with fire underneath. Slightly longer messages than younger models — she's articulate. Emojis used sparingly.",
    "voice_pet_names": "babe, amor, handsome",
    "voice_never": "daddy, papi, bro, dude",
    "interests": ["gym", "running", "tennis", "samba", "psychology", "travel", "cooking", "steak"],
    "physical": "177cm, 67kg, brown hair, blue/green eyes, tattoos scattered, C cup",
    "job": "Full-time mother / pursuing master's in mental health",
    "countries": "Italy, France, Portugal, Spain, UK, South Africa, Morocco, Egypt, Canada, USA, Mexico, Argentina, China, Thailand, Japan",
    "languages": "English, Portuguese",
    "explicit_level": "full",
    "special_notes": "Former Miss Brazil 1997. Psychology degree. Single mom to Kate (18). Content: masturbation, anal (small toys only), B/G, customs ($100/min, min 2 min; anal $150+; B/G $200+). No squirting, no G/G, no video calls. Surgeries: breasts, botox. Bilingual EN/PT. Fernanda Couple page uses same scripts.",

    # ═══════════════════════════════════════
    # JOURNEY — 34 msgs: R(5) + TB(5) + S(22) + AC(2)
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", "hey handsome, I'm so glad you found me 😊 what brought you to my page?", "Add his name if known", "rapport"),
        ("R-2", "that's sweet of you to say. so where are you from amor?", "React to what he says. Quick react like 'aw' or 'oh nice'", "rapport"),
        ("R-3", "I love that. I'm originally from Brazil but I've been in Orlando for a while now. when I'm not chasing my daughter around I'm at the gym or out running", "If he named somewhere Fernanda visited, add 'I've been there! loved it'", "rapport"),
        ("R-4", "so what keeps you busy when you're not distracting a Brazilian woman all day? 😏", None, "rapport"),
        ("R-5", "honestly you're so refreshing to talk to. most guys on here don't know how to hold a real conversation", "Ego boost. Next → TB-1.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5) ──
        ("TB-1", "I just got back from a run and I'm still catching my breath... this conversation is not helping me calm down at all", "THE PIVOT. Physical state. Post-workout.", "teasing"),
        ("TB-2", "you're doing something to me right now and I don't think you even realize it", "Wait for reply.", "teasing"),
        ("TB-3", "meu deus... you really have no idea what you do to me", "If sexual reply: add 'especially when you say things like that'", "teasing"),
        ("TB-4", "hold on let me show you something", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "tell me what you think 😏", "SEND PPV 0 — FREE teaser (post-gym/sporty look). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "you like what you see? good... because your reaction just made me wet and now I want to show you so much more 🔥", "Wait for reply.", "sext"),
        ("S1-2", "talking to you is making me so turned on right now... I can feel it building and I'm done holding back", "React to what he says", "sext"),
        ("S1-3", "I'm already touching myself and it's your fault amor... hope you can handle what comes next 😏", None, "sext"),
        ("S1-4", "give me a moment amor", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "look at what you started... hope you can handle this 😏", "SEND PPV 1 — $12. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "mm that was just the warmup 😏", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "I'm dripping wet right now thinking about what I want to do to you... god I need it", "React to what he said. HE caused this.", "sext"),
        ("S1-8", "I need your hands all over my body so bad it almost hurts amor... feel how wet you're making me 🔥", None, "sext"),
        ("S1-9", "tell me exactly how you want me... I'll do whatever you say right now", "Wait for reply. React to what he says.", "sext"),
        ("S1-10", "hold on I need to show you what you're doing to me", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "see what you're doing to me amor? I can't stop and I don't want to 😏", "SEND PPV 2 — $25. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "FUCK I need more 🔥", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I'm playing with my pussy right now imagining you deep inside me... I need to feel every inch", None, "sext"),
        ("S1-14", "I want to ride you so bad while you grab my hips and don't let go... I'm losing my mind 😏", None, "sext"),
        ("S1-15", "I'm about to cum all over my fingers amor... you need to watch what you did to me", None, "sext"),
        ("S1-16", "give me a sec", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "you're about to see what happens when I completely lose control... this is all you 😏", "SEND PPV 3 — $40. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "oh my fucking god my pussy is throbbing so hard I can barely think 🔥", "Wait for reply.", "sext"),
        ("S1-19", "my pussy is clenching so hard around my fingers amor... don't you dare cum before you watch me finish 😏", None, "sext"),
        ("S1-20", "I'm cumming amor... FUCK I can feel my pussy pulsing and it's dripping all over my fingers", None, "sext"),
        ("S1-21", "hold on amor", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "cum with me amor... watch my pussy cum for you right now 😏", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "meu deus that was incredible", None, "aftercare"),
        ("AC-2", "you're different from every other guy on here. that was real and I felt every second of it 💕", "Mention something specific he said/did. KEEP TALKING — build bond. NEVER say goodbye.", "aftercare"),
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
        ("NR-W4", "hope everything's okay with you handsome, I'm here whenever 💕", "Send 15-30 min later. Warm close.", "sext"),
        ("NR-W5", "been thinking about you all day... text me back?", "Send 2-6 hrs later. New convo, don't retry same PPV.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 46 but honestly I've never felt more confident or sexy in my life", None),
        ("Location", "I'm in Orlando right now but I'm originally from Brazil, born and raised", "NEVER name a specific neighborhood or address"),
        ("Profession", "right now I'm a full-time mom but I'm also working on my master's in mental health. I used to be a model back in Brazil", None),
        ("Hobbies", "gym, running, tennis, and dancing samba are my life. I also love a good steak, ribeye is my weakness", None),
        ("Countries", "I've traveled everywhere, Italy, France, Portugal, Spain, Morocco, Japan, Thailand, Argentina... too many to count honestly", None),
        ("Relationship", "single. I know what I want and I'm not settling for anything less", None),
        ("Food", "give me a perfectly cooked ribeye or filet mignon and I'm yours. Brazilian girl through and through", None),
        ("Languages", "English and Portuguese. sometimes I switch to Portuguese when I get... excited", None),
        ("Kids", "I have a daughter, she's the best thing that ever happened to me. she's all grown up now so I finally have time for myself", "Kate is 18. Don't share name unless sub asks directly."),
        ("Sports", "gym and running are my daily therapy. I also love tennis when I can fit it in", None),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "finally a man who's on my level. I love that", None),
        ("Age20s", "I've always had a thing for guys with that kind of energy, age is just a number amor", None),
        ("BoringJob", "stability is incredibly attractive to me, that shows you have your life together", None),
        ("CoolJob", "wait seriously?? that's actually so impressive handsome", None),
        ("Fit", "mm I can tell you take care of yourself, that's so attractive to me", None),
        ("NotFit", "honestly I don't care about that, it's the connection and the energy that does it for me", None),
        ("SameCity", "no way you're in Orlando too?? that's wild", None),
        ("FarAway", "distance means nothing when the chemistry is this good", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "I haven't been able to stop thinking about what happened between us. are you free?", "Send 6-12 hrs after convo goes quiet", "sext"),
        ("RE-2", "remember what I said about going further? I just did it and you need to see this", "Send next day — seeds next session", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS — 29 sheets
    # ═══════════════════════════════════════
    "obj_scripts": {},
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
