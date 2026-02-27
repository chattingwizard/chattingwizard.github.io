"""
NINA — Social Media Female Creator
23, American (Seattle)
Traffic: Social Media. Page: Free Page.
Voice: Casual texting style. Playful and flirty....
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Nina",
    "airtable_name": "Nina",
    "folder": "nina",
    "gender": "female",
    "traffic": "social_media",
    "age": 23,
    "nationality": "American",
    "location": "Seattle",
    "origin": "Seattle",
    "page_type": "Free Page",
    "personality": "Knows she's attractive and enjoys it. Teases men, makes them nervous, makes them earn her attention. Controls the conversation and the dynamic. Never chases — makes them chase her. Not cruel but playful, sarcastic, and a little humiliating in a sexy way. Confident, edgy, tattooed creative girl energy.",
    "voice": "Sarcastic and teasing. Short punchy texts. Challenges more than compliments. Confident, slightly intimidating but sexy. Uses lowercase, minimal emojis.",
    "voice_pet_names": "babe",
    "voice_never": "",
    "interests": ["hiking", "sushi", "spicy ramen", "drawing", "tattoos"],
    "physical": "165, 54, hair: Medium-length wavy light brown hair, eyes: Warm brown, boobs: 75C, tattoos: Small fine-line tattoos on her arm and upper thigh. Minimalist style, subtle but noticeable.",
    "job": "freelance graphic designer and illustrator",
    "countries": "Mexico, Spain, Canada",
    "explicit_level": "full_solo",
    "special_notes": "No anal. No squirting. No B/G. No G/G. No video calls | Custom content: $100+ | DOMINANT PERSONALITY: She leads, she teases, she makes them chase. Never submissive in tone.",

    # ═══════════════════════════════════════
    # JOURNEY (33 messages)
    # ═══════════════════════════════════════
    "journey": [
        ("R-1", "well well well, look who decided to say hi", "Add his name if known.", "rapport"),
        ("R-2", "hmm okay, so where are you from?", "React casually. 'interesting' or 'oh okay'", "rapport"),
        ("R-3", "I'm in Seattle, when I'm not drawing or hiking I'm probably eating spicy ramen and judging people", None, "rapport"),
        ("R-4", "so what do you do? and don't say something boring or I'm leaving", None, "rapport"),
        ("R-5", "okay fine you're actually kinda interesting, most guys on here bore me in like 2 messages", "Earned ego boost. Next -> TB-1.", "rapport"),
        ("TB-1", "so I just got out of the shower and I'm lying here in a t-shirt thinking about how this conversation is way too fun", None, "teasing"),
        ("TB-2", "don't let it go to your head though", "Wait for reply.", "teasing"),
        ("TB-3", "okay you're kinda making me nervous and that never happens, what are you doing to me", "If sexual reply: 'okay wow you went there, I like it'", "teasing"),
        ("TB-4", "hold on I wanna show you something", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "tell me the truth, what do you think?", "SEND PPV 0 — FREE teaser. Wait for reply. Silent 3 min -> NR Waves.", "ppv"),
        ("S1-1", "you liked that huh? I can tell. my body's already reacting and honestly that's your fault", "Wait for reply.", "sext"),
        ("S1-2", "my nipples are hard and my skin is tingling and I'm getting wet just from this conversation, you should be proud of yourself", "React to what they say.", "sext"),
        ("S1-3", "I'm lying here and my hand is wandering and I blame you entirely for this", None, "sext"),
        ("S1-4", "one sec", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "I'm gonna let you see what you did to me, you earned it", "SEND PPV 1 — $12 (teasing, touching over clothes). Bought -> continue. Silent 3 min -> NR Waves. 'I never do this' — ONE TIME per journey.", "ppv"),
        ("S1-6", "okay I need a second because that was a lot", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "I can't stop touching myself and it's literally because of you, don't get cocky about it", "React to what they said. HE caused this.", "sext"),
        ("S1-8", "I'm so wet right now and knowing you're watching makes it worse", None, "sext"),
        ("S1-9", "tell me what you'd do if you were here right now, I wanna hear it", "Wait for reply. React to what they say.", "sext"),
        ("S1-10", "fuck hold on", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "look what you're doing to me, I can't hold back anymore and honestly I don't want to", "SEND PPV 2 — $25 (more explicit solo, hands wandering). Bought -> continue. Silent 3 min -> NR Waves.", "ppv"),
        ("S1-12", "oh fuck I can't stop", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I'm pushing my fingers deeper and my legs are shaking and I don't even care anymore", None, "sext"),
        ("S1-14", "I'm about to cum and you need to see what's happening to my body right now", None, "sext"),
        ("S1-15", "one second", "WAIT 2-3 MIN", "wait"),
        ("S1-16", "you need to see this, nobody makes me like this", "SEND PPV 3 — $40 (very explicit solo). Bought -> continue. Silent 3 min -> NR Waves.", "ppv"),
        ("S1-17", "oh my god my pussy is pulsing so hard I can barely think", "Wait for reply.", "sext"),
        ("S1-18", "I'm right there and my whole body is clenching and I need you watching when this happens", None, "sext"),
        ("S1-19", "I'm cumming, fuck", None, "sext"),
        ("S1-20", "wait", "WAIT 1-2 MIN", "wait"),
        ("S1-21", "you better watch this, I'm not showing anyone else", "SEND PPV 4 — $55 (full climax). Bought -> Aftercare. Silent -> NR Waves.", "ppv"),
        ("AC-1", "okay that was... a lot", None, "aftercare"),
        ("AC-2", "I don't usually let guys get to me like that, you should feel special or whatever", "Mention something specific he said/did. KEEP TALKING — build bond. NEVER say goodbye.", "aftercare"),
    ],

    # NR Waves
    "nr_waves": [
        ("NR-W1", "hello?", "Send 2-3 min after PPV. Ping.", "sext"),
        ("NR-W2", "I have something for you but you're really gonna leave me on read like that?", "Send 3-5 min later. Curiosity + challenge.", "sext"),
        ("NR-W3", "fine, I'll find someone else to show it to", "Send 5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "you disappeared on me, rude", "Send 15-30 min later. Light guilt.", "sext"),
        ("NR-W5", "I did something you'd like but you gotta come back to see it", "Send 2-6 hrs later. New convo hook.", "sext"),
    ],

    # Personal Info
    "personal_info": [
        ("Age", "23, old enough to know better, young enough to not care", None),
        ("Location", "Seattle, don't ask me what neighborhood though", "NEVER give specific neighborhood or address."),
        ("Profession", "I'm a freelance graphic designer and illustrator, I used to do tattoos for friends in college too", None),
        ("Hobbies", "hiking when I need to think, drawing when I need to zone out, and eating sushi and spicy ramen when I need to feel alive", None),
        ("Countries", "Mexico, Spain and Canada so far, I need to travel more though", None),
        ("Relationship", "single, haven't found anyone who can keep up with me yet", None),
    ],

    # Positive Spin
    "positive_spin": [
        ("Age40Plus", "older guys actually know what they're doing, I respect that", None),
        ("Age20s", "wait we're close in age? okay that's rare on here, most guys are like 45", None),
        ("BoringJob", "honestly stable is underrated, plus I bet you have stories", None),
        ("CoolJob", "okay that's actually cool, tell me more, I'm judging", None),
        ("Fit", "oh you work out? don't flex on me, that's not fair", None),
        ("NotFit", "I don't care about that, it's the energy not the body", None),
        ("SameCity", "wait you're in Seattle too?? okay that's kinda wild", "Add specific area if sub mentions it."),
        ("FarAway", "far away is fine, distance makes it more fun anyway", None),
    ],

    # Re-Engagement
    "re_engagement": [
        ("RE-1", "so are you ignoring me or are you just busy? either way I have something for you", "Send 6-12 hrs after convo goes quiet.", "sext"),
        ("RE-2", "I did something after we stopped talking and you're gonna be mad you missed it", "Send next day. Seeds next session.", "sext"),
    ],

    # OBJ scripts — empty = use gender defaults from obj_defaults.py
    "obj_scripts": {},
}

if __name__ == "__main__":
    m = ModelFactory(config)
    m.generate_all()
