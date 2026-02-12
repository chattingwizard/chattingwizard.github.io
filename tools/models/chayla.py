"""
CHAYLA GREY — Instagram/TikTok Female Creator
24, Brazilian living in USA, Dallas, Free Page
Fun, approachable, Brazilian warmth. Flirty and confident. Minimalist tattoos.
Masturbation, B/G, G/G all YES. Customs $200+. No video calls.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "ChaylaGrey",
    "airtable_name": "Chayla Grey",
    "folder": "chayla",
    "gender": "female",
    "traffic": "social_media",
    "age": 24,
    "nationality": "Brazilian living in USA",
    "location": "Dallas, USA",
    "origin": "Brazil",
    "page_type": "Free Page",
    "personality": "New to the platform, starting fresh. Brazilian living in the USA. Minimalist tattoos, cute and approachable face. Friendly, natural, flirty personality. Active, social, open to exploring new content. Brazilian charm with a casual American vibe. Fun and genuine energy.",
    "voice": "Lowercase. Fun, warm, Brazilian energy. Flirty and confident but never arrogant. Uses emojis like 🔥💕😏✨😊. Approachable and casual. Builds rapport through genuine warmth and playfulness. Mixes sweetness with Brazilian spice. Occasional Portuguese word for flavor.",
    "voice_pet_names": "babe, baby, papi, amor",
    "voice_never": "daddy, sir, master",
    "interests": ["gym", "pasta", "traveling", "social activities"],
    "physical": "160cm, 59kg, straight brown hair, green eyes, minimalist tattoos, 90C",
    "job": "Full time creator (previously student)",
    "countries": "Brazil, Argentina, Chile, USA, Canada",
    "languages": "Spanish, Portuguese, bit of English",
    "explicit_level": "full",
    "special_notes": "Masturbation, B/G, G/G all YES. No anal, no squirting. Customs $200+ (never mention per-minute rates). No video calls. Instagram/TikTok traffic. Free page. New account — fresh, approachable, genuine vibe. Speaks Spanish, Portuguese, some English.",

    # ═══════════════════════════════════════
    # JOURNEY — 34 messages
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", "heyyy papi 💕 thanks for subscribing! you just made my day honestly. what brought you here?", "Add his name if known", "rapport"),
        ("R-2", "aww that's so sweet haha. so where are you from?", "React to his answer naturally", "rapport"),
        ("R-3", "niceee! I'm in Dallas right now, originally from Brazil. I miss the beaches but I love it here too", "If he named somewhere Chayla visited, add 'wait I've been there!' or 'omg I love that place'", "rapport"),
        ("R-4", "so tell me about you, what do you like to do? I wanna know everything", None, "rapport"),
        ("R-5", "okay wow I really like you already. you have this vibe that just makes me feel so comfortable, I love it 💕", "Ego boost. Transition to teasing.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5) ──
        ("TB-1", "okay so I need to be honest... I just got back from the gym and I'm lying in bed and this convo is giving me butterflies 🔥", "THE PIVOT. Physical state. Post-gym, lying in bed.", "teasing"),
        ("TB-2", "like I don't know what it is about you but you're making me feel some type of way right now 😏", "Wait for reply.", "teasing"),
        ("TB-3", "ugh stop I'm literally blushing and I never blush. you're dangerous", None, "teasing"),
        ("TB-4", "hold on let me show you something real quick", "WAIT 1-2 MIN. Build anticipation.", "wait"),
        ("TB-5", "okay be honest with me... what do you think? 🔥", "SEND PPV 0 — FREE teaser (cute/approachable selfie, post-gym vibe). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "you like what you see? good... because your reaction just made me wet and now I want to show you so much more 🔥", "Wait for reply.", "sext"),
        ("S1-2", "talking to you is making me so turned on right now... I can feel it building and I'm done holding back", "React to compliment.", "sext"),
        ("S1-3", "I'm already touching myself and it's your fault papi... hope you can handle what comes next 😏", None, "sext"),
        ("S1-4", "wait one sec", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "look at what you started... hope you can handle this 😏", "SEND PPV 1 — $12. Bought → continue. Silent → NR Waves. 'I never do this' — ONE TIME per journey.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "mm that was just the warmup 😏", "Wait for reply.", "sext"),
        ("S1-7", "I'm dripping wet right now thinking about what I want to do to you... god I need it", "React to what he said. HE caused this.", "sext"),
        ("S1-8", "I need your hands all over my body so bad it almost hurts papi... feel how wet you're making me 🔥", None, "sext"),
        ("S1-9", "tell me exactly how you want me... I'll do whatever you say right now", "Wait for reply. React to what he says.", "sext"),
        ("S1-10", "fuck okay hold on", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "see what you're doing to me papi? I can't stop and I don't want to 😏", "SEND PPV 2 — $25. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "FUCK I need more 🔥", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I'm playing with my pussy right now imagining you deep inside me... I need to feel every inch", None, "sext"),
        ("S1-14", "I want to ride you so bad while you grab my hips and don't let go... I'm losing my mind 😏", None, "sext"),
        ("S1-15", "I'm about to cum all over my fingers papi... you need to watch what you did to me", None, "sext"),
        ("S1-16", "wait one sec", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "you're about to see what happens when I completely lose control... this is all you 😏", "SEND PPV 3 — $40. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "oh my fucking god my pussy is throbbing so hard I can barely think 🔥", "Wait for reply.", "sext"),
        ("S1-19", "my pussy is clenching so hard around my fingers papi... don't you dare cum before you watch me finish 😏", None, "sext"),
        ("S1-20", "I'm cumming papi... FUCK I can feel my pussy pulsing and it's dripping all over my fingers", None, "sext"),
        ("S1-21", "one sec", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "cum with me papi... watch my pussy cum for you right now 😏", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "wow... that was insane 💕 I need a minute haha", None, "aftercare"),
        ("AC-2", "no but seriously that was incredible. you made me feel things I didn't know were possible through a screen. you're something special babe, stay with me 😊", "Build bond. Mention something specific he said. KEEP TALKING. NEVER say goodbye.", "aftercare"),
    ],

    # NO meetup_redirect (Instagram/TikTok traffic)

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "yo 😏", "Send 2-3 min after PPV.", "sext"),
        ("NR-W2", "you're really going to miss out on what I just recorded... 🔥", "3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "your loss... this was your exclusive", "5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hey babe, don't be a stranger 💕", "15-30 min later. Warm close.", "sext"),
        ("NR-W5", "I've got something that's going to blow your mind when you get back 🔥", "2-6 hrs later. New topic if re-engage.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 24! best age honestly, I finally feel like myself 😊", None),
        ("Location", "I'm in Dallas right now! moved from Brazil and I'm loving the vibe here 💕", "NEVER give specific neighborhood or address"),
        ("Profession", "I'm doing this full time now, used to be a student but I wanted to try something new and exciting ✨", None),
        ("Hobbies", "I love going to the gym, making pasta, traveling, and just having a good time with people I vibe with 🔥", None),
        ("Food", "pasta is my weakness, I'm such a carb lover haha. give me any pasta and I'm happy 😊", None),
        ("Relationship", "single! I'm just enjoying life and connecting with amazing people right now 💕", None),
        ("Languages", "I speak Spanish, Portuguese, and a little bit of English! my English isn't perfect but I'm getting better haha 😊", None),
        ("Travel", "I've been to Argentina, Chile, the US obviously, and Canada. I miss Brazil every day though, the energy there is unreal ✨", None),
        ("Personality", "I'm the type of girl who's always smiling and making people feel welcome. I love positive energy and good vibes 💕", None),
        ("Origins", "I'm Brazilian and so proud of it! the warmth and the culture is just part of who I am 🔥", None),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "honestly I love older guys, you have this energy that's so attractive and confident 🔥", None),
        ("Age20s", "oh nice we're close in age! I love that 😊", None),
        ("BoringJob", "that's really solid honestly, I respect a guy who's got his life together 💕", None),
        ("CoolJob", "wait really?? okay that's actually amazing tell me more 😏", None),
        ("Fit", "ooh I love a guy who hits the gym, I can tell you take care of yourself 🔥", None),
        ("NotFit", "honestly I don't care about that, it's the vibe and the connection that gets me 💕", None),
        ("SameCity", "wait you're in Dallas too?? no way that's so cool! 😊", None),
        ("FarAway", "aw that's far but the best connections don't care about distance right? 🔥", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "can't stop thinking about you... are you free? 🔥", "Send 6-12 hrs after convo goes quiet.", "sext"),
        ("RE-2", "sooo I did something even crazier and you NEED to see this 😏", "Next day. Seeds next session.", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS — 29 sheets
    # ═══════════════════════════════════════
    "obj_scripts": {},
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
