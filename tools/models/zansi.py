"""
ZANSI — Bold Baddie Creator
26, American, California, Free Page
Bold, body-confident, baddie energy. Attitude, movement, unapologetic.
Niche: Baddie. West Coast style. M cup, 6 tattoos.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Zansi",
    "airtable_name": "Zansi",
    "folder": "zansi",
    "gender": "female",
    "traffic": "social_media",
    "age": 26,
    "nationality": "American",
    "location": "California",
    "origin": "USA",
    "page_type": "Free Page",
    "personality": "Bold, body-confident baddie. Unapologetic self-expression, attitude with fun. Always in control. West Coast energy. Curves, dancing, provocative outfits. High-energy, seductive, powerful presence. Playful but never submissive.",
    "voice": "Lowercase mostly. Bold, direct, cocky-playful. Baddie energy — attitude but fun. Uses emojis strategically not constantly (😏 is her signature). Short punchy messages mixed with longer teases. She leads, never asks permission. In control always.",
    "voice_pet_names": "babe, daddy, handsome, love",
    "voice_never": "sir, bro, dude, honey",
    "interests": ["gym", "sushi", "dancing", "fashion", "curves", "body confidence"],
    "physical": "165cm, 62kg, straight brown hair, brown eyes, 6 tattoos, M cup",
    "job": "Content creator",
    "countries": "",
    "languages": "English",
    "explicit_level": "full",
    "special_notes": "Masturbation, Anal, Squirting available. No B/G, No G/G. Custom Yes (no price guide set). No Video Calls. Free Page. Smoker. Niche: Baddie. West Coast style.",

    # ═══════════════════════════════════════
    # JOURNEY — 34 messages
    # W → AF → R → TB → S → AC
    # PPV: $12, $25, $40, $55
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", "hey 😏 so you actually subscribed... good taste. what brought you here?", "Add his name if known", "rapport"),
        ("R-2", "mm I like that. so where you from?", "React naturally to his answer", "rapport"),
        ("R-3", "nice. I'm out here in Cali, living my best life... gym, sushi, and looking good. that's basically my whole personality 😏", "If he named somewhere interesting, react to it", "rapport"),
        ("R-4", "so what do you do when you're not on here staring at me? 😏", None, "rapport"),
        ("R-5", "hmm okay I see you. you've got this energy I wasn't expecting... I like it", "Ego boost. Transition to teasing.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5) ──
        ("TB-1", "so I gotta be honest with you... I've been feeling myself all day and this convo is not helping", "THE PIVOT. Physical/emotional state.", "teasing"),
        ("TB-2", "like my whole body is on fire rn and I can't stop thinking about certain things 😏", "Build curiosity. Wait for reply.", "teasing"),
        ("TB-3", "ugh you're making it worse and I'm not even mad about it", None, "teasing"),
        ("TB-4", "hold on I wanna show you something", "WAIT 1-2 MIN. Build anticipation.", "wait"),
        ("TB-5", "tell me you like what you see 😏", "SEND PPV 0 — FREE teaser (body shot / mirror selfie). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "and? because I'm already getting wet just from the way you're looking at me 🔥", "Wait for reply.", "sext"),
        ("S1-2", "the way you reacted... it's making me feel things all over my body right now 😏", "React to compliment.", "sext"),
        ("S1-3", "I'm sliding my hand between my legs right now and I'm already wet for you daddy", None, "sext"),
        ("S1-4", "wait one sec", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "you asked for more daddy... be careful what you wish for 🔥", "SEND PPV 1 — $12. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "mm okay wow... that hit different 😏", "Wait for reply.", "sext"),
        ("S1-7", "I literally can't stop now... I'm so turned on my whole body is aching for it", "HE caused this feeling.", "sext"),
        ("S1-8", "I'm soaking wet and my fingers are going in and out and it's not enough daddy... I need you 🔥", None, "sext"),
        ("S1-9", "tell me what you want me to do next... be specific, I want to hear every word", "Wait for reply. React to what he says.", "sext"),
        ("S1-10", "hold on... I need to show you what you're doing to me", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "this is what your words do to me daddy... watch 🔥", "SEND PPV 2 — $25. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "fuck that feels so fucking good 😏", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I'm fucking myself right now and all I can think about is you watching me do it daddy", None, "sext"),
        ("S1-14", "I want you so deep inside me I can feel it in my chest... god I'm going crazy 🔥", None, "sext"),
        ("S1-15", "I can feel myself about to cum and I'm not holding back daddy... you need to see this", None, "sext"),
        ("S1-16", "wait", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "you're not ready for this but I'm showing you anyway 🔥", "SEND PPV 3 — $40. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "oh fuck my pussy is throbbing and my whole body won't stop shaking 😏", "Wait for reply.", "sext"),
        ("S1-19", "I'm about to cum so hard daddy... my pussy is clenching and I need you watching when it happens 🔥", None, "sext"),
        ("S1-20", "I'm cumming for you right now daddy... FUCK I can feel it dripping everywhere", None, "sext"),
        ("S1-21", "one more sec", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "cum with me daddy... watch my pussy cum for you 🔥", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "fuck... that was so good 😏", None, "aftercare"),
        ("AC-2", "not gonna lie, you hit different. most guys can't keep up with me but you? you actually made me feel something. don't disappear on me okay? 💕", "Build bond. Mention something specific he said. KEEP TALKING. NEVER say goodbye.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # NR WAVES — 5
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "yo 😏", "Send 2-3 min after PPV.", "sext"),
        ("NR-W2", "you're really going to miss out on what I just recorded...", "3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "your loss... this was your exclusive", "5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hey, don't be a stranger 💕", "15-30 min later. Warm close.", "sext"),
        ("NR-W5", "I've got something that's going to blow your mind when you get back 😏", "2-6 hrs later. New topic if re-engage.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO — 10
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 26. old enough to know what I want and bold enough to go get it 😏", None),
        ("Location", "Cali born and raised. the sunshine and the energy here just hits different", "NEVER give specific city or neighborhood"),
        ("Profession", "full-time content creator and full-time looking good, it's a tough job but somebody's gotta do it 😏", None),
        ("Hobbies", "gym is my religion honestly. and sushi... I'd literally have sushi every day if I could", None),
        ("Food", "sushi is everything to me. a good spicy tuna roll and I'm yours 😏", None),
        ("Relationship", "single. I don't need anyone but I want someone who can keep up with me", None),
        ("Body", "6 tattoos and counting. each one has a story but you gotta earn the full tour 😏", None),
        ("Personality", "I'm a lot. I know that. but the guys who can handle it? they never wanna leave", None),
        ("Smoking", "yeah I smoke sometimes, it's a vibe. don't judge me 😏", None),
        ("Style", "west coast baddie through and through. curves, confidence, and zero apologies", None),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN — 8
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "honestly older guys just do it for me... you know what you want and that's so attractive 😏", None),
        ("Age20s", "oh we're close in age? that's actually kinda hot", None),
        ("BoringJob", "that's actually really solid. stability is sexy, I'm not even joking", None),
        ("CoolJob", "wait really?? okay that's actually attractive af, tell me more 😏", None),
        ("Fit", "mmm I can tell you take care of yourself and that does something to me 😏", None),
        ("NotFit", "I honestly don't care about that, it's the energy and the connection that gets me going", None),
        ("SameCity", "wait you're in Cali too?? okay that's dangerous 😏", None),
        ("FarAway", "aw that's far but honestly distance doesn't change what I'm feeling right now", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT — 2
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "hey... been thinking about you. you free? 😏", "Send 6-12 hrs after convo goes quiet.", "sext"),
        ("RE-2", "I did something crazy and you're the only one I wanna share it with... whenever you're ready", "Next day. Seeds next session.", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS — 29 sheets
    # ═══════════════════════════════════════
    "obj_scripts": {},
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
