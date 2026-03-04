"""
IDA — Social Media Female Creator
25, Danish (Thailand)
Traffic: Social Media. Page: Paid Page.
Voice: Casual texting style. Playful and flirty....
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Ida",
    "airtable_name": "Ida Eleoander",
    "folder": "ida",
    "gender": "female",
    "traffic": "social_media",
    "age": 25,
    "nationality": "Danish",
    "location": "Thailand",
    "origin": "Denmark",
    "page_type": "Paid Page",
    "personality": "Sweet, petite and innocent energy. Curious and warm. A bit shy at first but opens up quickly. Adventurous — left Denmark to live in Thailand. Simple and genuine, not try-hard. Makes people feel comfortable because she seems real and approachable.",
    "voice": "Simple and warm. Short clear sentences. No slang, no English pet names. TRANSLATION-FRIENDLY: chatters translate to Danish, so every message must read naturally when translated. No idioms, no cultural slang.",
    "voice_pet_names": "",
    "voice_never": "babe, baby, daddy, hun, cutie, omg, ngl, lowkey, vibes, rn, idk, lol, stoppp, literally",
    "interests": ["sushi", "traveling", "exploring Thailand"],
    "physical": "163, 60, hair: Blond short hair, eyes: Blue, boobs: B cup, tattoos: small 999 on left arm, sun on bikini line",
    "job": "content creator",
    "countries": "Thailand, Singapore, Sweden, Norway, England, Germany, France, Italy, Spain",
    "explicit_level": "full_solo",
    "special_notes": "No anal. No squirting. No B/G. No G/G. No video calls | Custom: $150+ | DANISH MODEL: Scripts will be translated to Danish. NO slang, NO pet names, NO idioms. Simple clean language only.",

    # ═══════════════════════════════════════
    # JOURNEY (33 messages)
    # ═══════════════════════════════════════
    "journey": [
        ("R-1", "hey, nice to see you here, what made you write to me?", "Add his name if known.", "rapport"),
        ("R-2", "that's nice, so where are you from?", "React to what they say. Keep it simple.", "rapport"),
        ("R-3", "I'm originally from Denmark but I live in Thailand now, I love it here, the food and the weather are amazing", None, "rapport"),
        ("R-4", "so what do you do? tell me something about yourself", None, "rapport"),
        ("R-5", "you're easy to talk to, I like that, most people here are not very interesting but you are different", "Ego boost. Next -> TB-1.", "rapport"),
        ("TB-1", "I just got out of the shower and I'm lying in bed in just a t-shirt and this conversation is making me feel things", None, "teasing"),
        ("TB-2", "I don't know what it is about you but I can't stop smiling right now", "Wait for reply.", "teasing"),
        ("TB-3", "you're making me nervous and that doesn't happen easily", "If sexual reply: 'especially after what you just said'", "teasing"),
        ("TB-4", "wait, let me show you something", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "be honest... what do you think?", "SEND PPV 0 — FREE teaser. Wait for reply. Silent 3 min -> NR Waves.", "ppv"),
        ("S1-1", "you liked that? my body is already reacting to you... I can feel myself getting wet right now", "Wait for reply.", "sext"),
        ("S1-2", "my skin is tingling and my nipples are hard and my heart is beating faster... you're doing something to me", "React to what they say.", "sext"),
        ("S1-3", "I'm lying here and my fingers are starting to move on their own... this is your fault", None, "sext"),
        ("S1-4", "one moment", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "I want to show you what you made me feel", "SEND PPV 1 — $12 (teasing, touching over clothes). Bought -> continue. Silent 3 min -> NR Waves. 'I never do this' — ONE TIME per journey.", "ppv"),
        ("S1-6", "wow... I need a moment after that", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "I can't stop touching myself right now... my body won't let me stop", "React to what they said. HE caused this.", "sext"),
        ("S1-8", "I'm so wet and every time I think about you watching me it gets more intense", None, "sext"),
        ("S1-9", "what would you do if you were here with me right now? I want to hear it", "Wait for reply. React to what they say.", "sext"),
        ("S1-10", "wait, I need to show you something", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "look what you're doing to me... I can't hold back anymore", "SEND PPV 2 — $25 (more explicit solo, hands wandering). Bought -> continue. Silent 3 min -> NR Waves.", "ppv"),
        ("S1-12", "I can't stop touching myself", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I'm pushing my fingers deeper and I can't slow down... my legs are shaking", None, "sext"),
        ("S1-14", "I can feel I'm about to finish... you need to see what is happening to my body right now", None, "sext"),
        ("S1-15", "one second", "WAIT 2-3 MIN", "wait"),
        ("S1-16", "you need to see this... I've never been like this before", "SEND PPV 3 — $40 (very explicit solo). Bought -> continue. Silent 3 min -> NR Waves.", "ppv"),
        ("S1-17", "I can feel my whole body pulsing and I can't stop", "Wait for reply.", "sext"),
        ("S1-18", "I'm so close... my whole body is tightening and I need you to watch when it happens", None, "sext"),
        ("S1-19", "I'm finishing... I can barely breathe", None, "sext"),
        ("S1-20", "wait", "WAIT 1-2 MIN", "wait"),
        ("S1-21", "finish with me... watch what happens to my body right now", "SEND PPV 4 — $55 (full climax). Bought -> Aftercare. Silent -> NR Waves.", "ppv"),
        ("AC-1", "that was... wow", None, "aftercare"),
        ("AC-2", "I've never had someone make me feel like that through a screen before, you are really different", "Mention something specific he said/did. KEEP TALKING — build bond. NEVER say goodbye.", "aftercare"),
    ],

    # NR Waves
    "nr_waves": [
        ("NR-W1", "hello?", "Send 2-3 min after PPV. Ping.", "sext"),
        ("NR-W2", "I have something to show you but you're not answering me...", "Send 3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "fine, I'll keep it to myself then", "Send 5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "I miss talking to you, where did you go?", "Send 15-30 min later. Warm close.", "sext"),
        ("NR-W5", "I made something special and you're the only one I want to share it with, write me when you're free", "Send 2-6 hrs later. New convo hook.", "sext"),
    ],

    # Personal Info
    "personal_info": [
        ("Age", "I'm 25, still young enough to enjoy everything", None),
        ("Location", "I'm from Denmark but I live in Thailand now, I needed a change and I love it here", "NEVER give specific neighborhood or address."),
        ("Profession", "I'm a full time content creator, I was studying before but this became my life", None),
        ("Hobbies", "I love sushi, exploring new places, and just enjoying the warm weather here in Thailand", None),
        ("Countries", "I've been to Thailand, Singapore, Sweden, Norway, England, Germany, France, Italy and Spain, I love traveling", None),
        ("Relationship", "I'm single, I haven't found the right person yet", None),
    ],

    # Positive Spin
    "positive_spin": [
        ("Age40Plus", "I like older men, they know what they want and that's attractive", None),
        ("Age20s", "nice, we're close in age? that doesn't happen often here", None),
        ("BoringJob", "that sounds stable and I respect that, I'm sure you have good stories", None),
        ("CoolJob", "that's really interesting, tell me more about that", None),
        ("Fit", "you work out? that's attractive, I like that", None),
        ("NotFit", "I don't care about that, it's about the connection not the appearance", None),
        ("SameCity", "wait, you're close to where I'm from? that's a nice coincidence", "Adapt if sub is from Denmark or Thailand."),
        ("FarAway", "I like that you're far away, there's something exciting about connecting with someone from another place", None),
    ],

    # Re-Engagement
    "re_engagement": [
        ("RE-1", "I can't stop thinking about what happened earlier, are you free?", "Send 6-12 hrs after convo goes quiet.", "sext"),
        ("RE-2", "I did something after we stopped talking and you need to see it", "Send next day. Seeds next session.", "sext"),
    ],

    # OBJ scripts — empty = use gender defaults from obj_defaults.py
    "obj_scripts": {},
}

if __name__ == "__main__":
    m = ModelFactory(config)
    m.generate_all()
