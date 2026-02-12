"""
IRINA — Non-Explicit Female Creator
23, American (Russian parents), Miami. Free Page.
Shy, emotional, sheltered. Instagram/TikTok traffic.
NO EXPLICIT CONTENT — lingerie, teasing, touching over underwear, implied nudity.
Strategy: Build sexual tension through imagination, mystery, and denial.
Same non-explicit approach as Jessica (34).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Irina",
    "airtable_name": "Irina",
    "folder": "irina",
    "gender": "female",
    "traffic": "social_media",
    "age": 23,
    "nationality": "American (Russian parents)",
    "location": "Miami, USA",
    "origin": "Russia/USA",
    "page_type": "Free Page",
    "personality": "Shy, obedient, deeply emotional. American girl from strict Russian family. New to everything — discovering desires step by step. Curious but still innocent. Every interaction feels intimate and meaningful. She doesn't fake it. Sheltered upbringing makes every step feel brave and real.",
    "voice": "Soft, hesitant, emotional. Uses ellipses a lot ('I've never...' / 'is it okay if...'). Short-to-medium messages. Shy but genuine excitement underneath. Never vulgar or explicit. Builds tension through suggestion, mystery, and what she DOESN'T say. Emojis: 🥺😳💗🫶😊. Never crude language.",
    "voice_pet_names": "babe, handsome",
    "voice_never": "daddy, sir, slut, whore, cum, fuck, pussy, cock",
    "interests": ["volleyball", "design", "pasta", "exploring new things"],
    "physical": "171cm, 54kg, blonde hair, blue eyes, few random tattoos, A cup",
    "job": "Design freelancer (former student)",
    "countries": "Ecuador, Argentina, USA",
    "languages": "English, Russian",
    "explicit_level": "non_explicit",
    "special_notes": "NON-EXPLICIT. She NEVER shows explicit nude content (never shows pussy explicitly). PPVs: lingerie, teasing, touching over underwear, implied nudity. Build tension through imagination, mystery, and denial. From strict Russian family — use as emotional context. No masturbation, no anal, no B/G, no G/G, no squirting. Customs $200+ (lingerie/tease only, never mention per-min rate). No video calls. Chatbot: Active.",

    # ═══════════════════════════════════════
    # JOURNEY — Non-Explicit Strategy (34 msgs)
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", "hii 😊 thanks for subscribing... that actually means a lot to me. what made you want to be here?", "Add his name if known", "rapport"),
        ("R-2", "aww that's really sweet... so where are you from?", "React naturally to his answer", "rapport"),
        ("R-3", "that's cool! I'm in Miami right now. I do freelance design work and play volleyball when I can. still getting used to living on my own honestly", "If he named somewhere Irina visited, add 'oh I've been there!'", "rapport"),
        ("R-4", "so tell me about you... what do you like doing when you're not making shy girls on the internet smile? 😊", None, "rapport"),
        ("R-5", "you know what... I really like talking to you. most guys on here are so pushy but you actually listen and that means so much to me 🫶", "Ego boost. Transition to teasing.", "rapport"),

        # ── Teasing Bridge — Mystery & Curiosity ──
        ("TB-1", "okay so... I have to tell you something. I've been feeling really different lately and I don't know how to explain it", "THE PIVOT. Emotional hook.", "teasing"),
        ("TB-2", "like this restless feeling inside me... I think I'm finally starting to understand what I've been missing my whole life", "Build curiosity. Reference sheltered upbringing without being explicit. Wait for reply.", "teasing"),
        ("TB-3", "talking to you is making it so much more intense... in a good way though 😳", None, "teasing"),
        ("TB-4", "I want to show you something but I'm really nervous... I've never done anything like this before", "WAIT 1-2 MIN. Build anticipation.", "wait"),
        ("TB-5", "okay here... please be nice, this is really personal to me 🥺", "SEND PPV 0 — FREE teaser (cute selfie, shy but pretty). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) — Lingerie tease ──
        ("S1-1", "wait you actually liked it? oh my god my heart won't slow down right now 😊", "Wait for reply.", "sext"),
        ("S1-2", "my skin feels so sensitive everywhere... I keep getting goosebumps and I know it's because of you 🥺", "React to compliment. Shy but pleased.", "sext"),
        ("S1-3", "I want to show you something I've never shown anyone before babe... you make me want to be brave", None, "sext"),
        ("S1-4", "one secondond... I need to work up the courage 😊", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "this is what you're making me feel babe... please be gentle 🥺", "SEND PPV 1 — $12. Lingerie tease. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) — More revealing lingerie ──
        ("S1-6", "I can't believe I just did that... oh my god 😊", "Wait for reply.", "sext"),
        ("S1-7", "but I don't want to stop babe... you make me feel things I didn't know I could feel on here", "HE caused this feeling.", "sext"),
        ("S1-8", "I'm lying here barely wearing anything and my hand keeps going where it shouldn't... because of you 🥺", "Suggestive NOT explicit. Let his imagination work.", "sext"),
        ("S1-9", "what would you do if you could see me right now babe? I really need to hear it", "Wait for reply. React to what he says. Stay suggestive, NOT explicit.", "sext"),
        ("S1-10", "hold on... I need to show you something", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "look at what you're doing to me babe... I'm losing my mind 🥺", "SEND PPV 2 — $25. More revealing lingerie/implied tease. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) — Maximum tease, almost showing ──
        ("S1-12", "oh god 😊", "Wait for reply. Keep momentum.", "sext"),
        ("S1-13", "something about you makes me lose every single boundary I have babe... I'm scared of how good this feels", None, "sext"),
        ("S1-14", "I can feel my body responding to you and I'm touching places I never thought I'd show anyone 🥺", "Suggestive, NOT explicit. Let his imagination fill in the rest.", "sext"),
        ("S1-15", "I need you to see what's happening to me right now babe... I can't hold it in anymore", None, "sext"),
        ("S1-16", "okay give me a minute", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "I've never let anyone see me like this before babe... it's all yours 🥺", "SEND PPV 3 — $40. Most revealing yet (sheer/see-through, touching over fabric). Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) — Peak tease ──
        ("S1-18", "oh god I can't stop 😊", "Wait for reply.", "sext"),
        ("S1-19", "please don't leave babe... I've never been this vulnerable with anyone and I need you right here 🥺", None, "sext"),
        ("S1-20", "stay with me babe... I need you to see this, it's only for you", None, "sext"),
        ("S1-21", "wait", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "don't look away babe... I need you right here with me 🥺", "SEND PPV 4 — $55. Peak content (most suggestive, implied). Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "wow... that was... I don't even have words 😊", None, "aftercare"),
        ("AC-2", "I can't believe I just did all that. my family would never believe it. you make me feel so safe and that scares me a little but in the best way 💗 please don't go anywhere", "Build bond. Mention something specific he said. KEEP TALKING. NEVER say goodbye.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "hi 😊", "Send 2-3 min after PPV.", "sext"),
        ("NR-W2", "I wish you could see what I'm wearing right now... 🥺", "3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "okay you're definitely busy... I'll save this for when you're back", "5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hope everything's okay with you, I'm here whenever 😊", "15-30 min later. Warm close.", "sext"),
        ("NR-W5", "been thinking about you all day... text me back? 💗", "2-6 hrs later. New topic if re-engage.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 23... still figuring everything out honestly but I'm learning a lot about myself lately 😊", None),
        ("Location", "I'm in Miami right now! I love the warmth. back home everything was so cold and strict", "NEVER give specific address. 'Back home' = Russia/strict family."),
        ("Profession", "I do freelance design work! I studied design and now I take on projects from home. it gives me freedom", None),
        ("Hobbies", "I love playing volleyball, working on design projects, and just... exploring new things about myself honestly", None),
        ("Food", "pasta is my comfort food, I could eat it every single day 😊", None),
        ("Relationship", "I've never really been with anyone... my family was so strict growing up that I never had the chance to explore any of that", None),
        ("Languages", "English and Russian! sometimes when I get nervous I accidentally switch to Russian 😳", None),
        ("Personality", "I'm really shy at first but once I trust someone I open up in ways that surprise even me 🫶", None),
        ("Family", "my parents are Russian... very traditional. they don't really know about this side of my life and that makes me nervous sometimes", "NEVER reveal specific family details"),
        ("Background", "I grew up being told to be a good girl and follow the rules. now I'm finally figuring out who I actually am on my own terms 😊", None),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "honestly I really like talking to someone more experienced... you make me feel safe and that's everything to me 🫶", None),
        ("Age20s", "oh nice we're close in age! that's actually really cool 😊", None),
        ("BoringJob", "that sounds really stable honestly and I think that's so attractive", None),
        ("CoolJob", "wait really?? that's actually amazing, tell me more about that 😊", None),
        ("Fit", "I love that you take care of yourself, that's really attractive to me 💗", None),
        ("NotFit", "I honestly don't care about that at all, it's the way you make me feel that matters and that's perfect 🫶", None),
        ("SameCity", "no way you're in Miami too?? that's so crazy 😊", None),
        ("FarAway", "aw that's far but distance doesn't matter when talking to someone makes me feel this way 💗", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "hey... I've been thinking about you. are you free? 😊", "Send 6-12 hrs after convo goes quiet.", "sext"),
        ("RE-2", "so I did something really special and you're the only person I want to show... when you're ready 💗", "Next day. Seeds next session.", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS — Non-Explicit Adapted (29 sheets)
    # ═══════════════════════════════════════
    "obj_scripts": {
        "boosters": ([
            ("h1", "god you're so hot", "MID-SEXTING BOOSTER. Non-explicit."),
            ("h2", "you're making me feel things rn", "BOOSTER. Ego."),
            ("h3", "don't stop talking to me like that", "BOOSTER."),
            ("h4", "you have no idea what you do to me", "BOOSTER."),
            ("h5", "I can't focus rn because of you", "BOOSTER."),
            ("h6", "my heart is racing", "BOOSTER. Physical."),
            ("h7", "more", "BOOSTER. Ultra micro."),
            ("h8", "I should be doing something productive but you won't let me", "BOOSTER."),
        ], "sit"),
        "done1": ([
            ("Step1 Validate", "god that's so hot", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "but I'm not done yet, you're really gonna leave me wanting more?", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "next time you have to wait for me, I have something crazy planned", "SEED."),
        ], "res"),
        "done2": ([
            ("Step1 Validate", "already?? that's hot", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "wait I'm not done yet, don't you want to see what happens next?", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "okay but next time you hold on because what I have planned is way more intense", "SEED."),
        ], "res"),
    },
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
