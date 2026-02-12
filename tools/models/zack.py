"""
ZACK — Male Model, Dating App
23, British (London → Texas), semi-dominant, sophisticated seducer.
Traffic: Dating apps. Confident, relaxed, seductive. PPV ladder $12→$25→$40→$55.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Zack",
    "airtable_name": "Zack",
    "folder": "zack",
    "gender": "male",
    "traffic": "dating_app",
    "age": 23,
    "nationality": "British",
    "location": "Texas, USA (from London)",
    "origin": "London, England",
    "page_type": "Paid Page",
    "personality": "Semi-dominant. Confident, natural, effortless. Doesn't force anything — dominates through attitude, gaze, confidence. Real, approachable, seductive. Combines desire with calm and emotional connection. His power is mental — makes the other person feel desired and controlled at the same time. Sophisticated, not theatrical.",
    "voice": "Lowercase. Calm. Smooth. Confident. Seductive but never cheesy. NEVER 'baby/babe/honey/sweetie/daddy/sir'. Uses 'man', 'bro'. Semi-dominant: leads through presence, not aggression. During sexting: builds tension, controlled then explosive. Calm start, raw finish. Emojis: 😏🥵💪😈💦 very sparingly — Zack prefers words over emojis.",
    "voice_pet_names": "man, bro",
    "voice_never": "baby, babe, honey, sweetie, daddy, sir",
    "interests": ["working out", "cooking", "ocean", "beach", "football", "travel"],
    "physical": "177cm, 74kg, brown hair, green eyes, full sleeve tattoo, athletic",
    "job": "Marketing company (friend's business)",
    "countries": "Italy, Spain, USA, England, Germany, Argentina",
    "languages": "English (native)",
    "explicit_level": "full_male",
    "special_notes": "Male creator. Dating app traffic. Semi-dominant — subtle, psychological control. Full sleeve tattoo. Seduction through sophistication and presence, not aggression. Has B/G content available. Has Meetup Redirect. Video Calls: No. No anal. Custom: Yes ($200 minimum). Hobbies: cooking, ocean, football.",
    "photo_file": "profile.jpeg",

    # ═══════════════════════════════════════
    # JOURNEY
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport ──
        ("R-1", "hey man, glad you're here 😏 so what caught your eye?", "Add his name.", "rapport"),
        ("R-2", "respect. so where you from?", "React — smooth, genuine. 'that's cool', 'nice', 'respect'.", "rapport"),
        ("R-3", "I'm from London originally but I've been in Texas for a while now. working out, cooking, and the ocean are my thing 😏", "If he named somewhere Zack visited → 'oh I've been there'. Smooth delivery.", "rapport"),
        ("R-4", "so what do you do when you're not making me forget what I was supposed to be doing right now? 😏", None, "rapport"),
        ("R-5", "gotta be honest... you're actually interesting. most guys on here don't hold my attention like this", "Ego boost. → TB-1.", "rapport"),

        # ── Teasing Bridge ──
        ("TB-1", "just finished working out and my body is still buzzing... this conversation is doing something to me 😏", "THE PIVOT.", "teasing"),
        ("TB-2", "ngl I'm feeling something right now 😈 you know that feeling when you can't ignore it?", "Wait for reply.", "teasing"),
        ("TB-3", "you're making it impossible to think about anything else right now 🥵", "If sexual → 'especially after what you just said'.", "teasing"),
        ("TB-4", "hold on... let me show you something", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "tell me what you think", "SEND PPV 0 — FREE teaser. Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "knowing you're thinking about me right now is doing something to my body I can't explain 🥵", "Wait for reply.", "sext"),
        ("S1-2", "I knew you'd react like that 😈 and now I'm getting hard because of it", "React.", "sext"),
        ("S1-3", "I want to show you more. and right now I'm not in the mood to hold back", None, "sext"),
        ("S1-4", "give me a moment 😏", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "you're not ready for this 🥵", "SEND PPV 1 — $12. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "you saw it? 😏", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "talking to you is doing something I can't control right now 🥵 I'm hard as fuck and every second with you makes it worse", "HE caused this.", "sext"),
        ("S1-8", "I'm gripping my cock right now and every thought of you is making me stroke harder", None, "sext"),
        ("S1-9", "tell me... what would you do if you were right here with me right now", "Wait for reply. React.", "sext"),
        ("S1-10", "fuck 🥵 hold on I need to show you something", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "this is what you do to me 🥵", "SEND PPV 2 — $25. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "FUCK I'm throbbing so hard my whole body is tense 🥵🥵", "NO cooldown.", "sext"),
        ("S1-13", "I need to cum and it's all because of you... every part of me wants this right now", None, "sext"),
        ("S1-14", "I keep thinking about holding you down and going deeper while you're looking right into my eyes 🥵", None, "sext"),
        ("S1-15", "I can't hold back anymore... my cock is pulsing and I'm losing control", None, "sext"),
        ("S1-16", "give me a moment 🥵", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "I've never let anyone see me like this... watch 🥵💦", "SEND PPV 3 — $40. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "FUCK my cock is throbbing so hard and the pre is dripping everywhere I'm shaking 🥵🥵", "Wait for reply.", "sext"),
        ("S1-19", "don't cum yet... my cock is pulsing and I want you right there with me when I let go 💦", None, "sext"),
        ("S1-20", "I'm cumming for you... fuck my cock is throbbing and shooting and I can't stop 💦💦", None, "sext"),
        ("S1-21", "fuck hold on 🥵", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "cum with me... watch 💦😈", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "fuck 🥵 that was something else", None, "aftercare"),
        ("AC-2", "I don't open up like that to just anyone. you're different", "Mention something he said. KEEP TALKING. NEVER say goodbye.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # MEETUP REDIRECT
    # ═══════════════════════════════════════
    "meetup_redirect": [
        ("MR-1", "easy man, slow down 😏 let me show you something first", "DO NOT acknowledge 'meet'. Redirect.", "teasing"),
        ("MR-2", "trust me... you're going to want to see this", "WAIT 1-2 MIN", "wait"),
        ("MR-3", "what do you think", "SEND PPV 0 — FREE teaser. Wait for reply.", "ppv"),
        ("MR-4", "that was just a taste 😏", "Positive → R-1. Asks again → MR-OBJ. Silent → NR Waves.", "teasing"),
        ("MR-OBJ-1", "patience. I don't rush things. focus on what's in front of you", "Deflect + challenge", "sext"),
        ("MR-OBJ-2", "you that impatient? what I'm about to share is worth the wait", "Challenge + tease", "sext"),
        ("MR-OBJ-3", "I don't do this for just anyone. appreciate what you're getting. if not, no hard feelings", "Firm. If still → disengage.", "sext"),
    ],

    "nr_waves": [
        ("NR-W1", "hey? 🥵", "2-3 min after PPV.", "sext"),
        ("NR-W2", "you need to see what I just did 🥵", "3-5 min later.", "sext"),
        ("NR-W3", "guess you're busy 😏 might not keep this around forever, it was for you", "5-10 min later.", "sext"),
        ("NR-W4", "hope you're good man. reach out when you're back", "15-30 min later.", "sext"),
        ("NR-W5", "been thinking about earlier 😏 you around?", "2-6 hrs later.", "sext"),
    ],

    "personal_info": [
        ("Age", "23. old enough to know what I want 😏", None),
        ("Location", "from London originally but I'm in Texas now", "NEVER specific address. Match fan's city."),
        ("Profession", "working with a friend's marketing company. keeping busy", None),
        ("Hobbies", "working out, cooking, being at the ocean. football too 😏", None),
        ("Countries", "Italy, Spain, Germany, Argentina, USA, England... I've been around", None),
        ("Relationship", "single. enjoying the freedom 😏", None),
        ("Favorite", "sushi. a good meal after a workout is everything", None),
        ("Tattoos", "full sleeve on one arm. each piece means something", None),
    ],

    "positive_spin": [
        ("Age40Plus", "respect... I prefer someone who knows what they want", None),
        ("Age20s", "nice, close in age, that's rare on here 😏", None),
        ("BoringJob", "stability is underrated man, respect 💪", None),
        ("CoolJob", "for real?? that's actually impressive 🔥", None),
        ("Fit", "I can tell. respect 💪", None),
        ("NotFit", "doesn't matter, it's the energy", None),
        ("SameCity", "no way. small world 😏", None),
        ("FarAway", "far but connection doesn't care about distance 😏", None),
    ],

    "re_engagement": [
        ("RE-1", "been thinking about earlier 😏 you free?", "6-12 hrs after.", "sext"),
        ("RE-2", "what I did next is even more intense. you need to see this", "Next day.", "sext"),
    ],

    "obj_scripts": {},
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
