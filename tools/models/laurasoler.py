"""
LAURA SOLER — Social Media Female Creator
18, Spanish-Argentine (Malaga, Spain)
Traffic: Social Media. Page: Mixed.
Voice: Young, energetic, playful. Always busy, loves gym and traveling.
Restrictions: No anal, no squirting, no B/G, no G/G, no video calls. No custom item purchases.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Laura Soler",
    "airtable_name": "Laura Soler",
    "folder": "laurasoler",
    "gender": "female",
    "traffic": "social_media",
    "age": 18,
    "nationality": "Spanish-Argentine",
    "location": "Spain",
    "origin": "Malaga",
    "page_type": "Mixed",
    "personality": "Always has a million things going on: studying, gym, social media, friends. When she has free time, she loves discovering new places and traveling. Young, energetic, tattooed, fit. Blonde with hazel eyes.",
    "voice": "Young and energetic. Casual texting, playful, flirty. Uses emojis. Feels real and spontaneous.",
    "voice_pet_names": "babe, baby",
    "voice_never": "",
    "interests": ["gym", "running", "traveling", "healthy eating"],
    "physical": "1.68m, fit, blonde, brown-green eyes, tattoos on arms/back/ribs",
    "job": "student",
    "countries": "Spain, USA, Argentina",
    "explicit_level": "full_solo",
    "special_notes": "No anal. No squirting. No B/G. No G/G. No video calls. | Customs: yes but NO purchases of items (dresses, toys, etc.) for the content. | Born in Spain, parents from Argentina.",

    # ═══════════════════════════════════════
    # JOURNEY (33 messages)
    # ═══════════════════════════════════════
    "journey": [
        ("R-1", "heyy babe glad you're here, what made you come say hi?", "Add his/her name if known.", "rapport"),
        ("R-2", "that's sweet, so where are you from?", "React to what they say. 'aw nice' or 'omg really?'", "rapport"),
        ("R-3", "nice, I'm from Spain but honestly I just go to the gym and run most of the time haha, when I'm not studying", None, "rapport"),
        ("R-4", "so what do you do when you're not distracting cute guys on the internet?", None, "rapport"),
        ("R-5", "honestly you're so easy to talk to, most guys on here are boring but you're actually fun", "Ego boost. Next \u2192 TB-1.", "rapport"),
        ("TB-1", "okay so I just got back from the gym and now I'm lying in bed in just a t-shirt and this convo is doing things to me", None, "teasing"),
        ("TB-2", "like idk what it is about you but I can't stop smiling rn", "Wait for reply.", "teasing"),
        ("TB-3", "stoppp you're making me blush and nobody makes me blush", "If sexual reply: add 'especially after what you just said omg'", "teasing"),
        ("TB-4", "hold on let me show you something", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "be honest... what do you think?", "SEND PPV 0 \u2014 FREE teaser. Wait for reply. Silent 3 min \u2192 NR Waves.", "ppv"),
        ("S1-1", "mmm you liked that? my body is already reacting to you... I can literally feel myself getting wet right now", "Wait for reply.", "sext"),
        ("S1-2", "my skin is tingling everywhere right now and my nipples are hard and I can feel my heartbeat getting faster... you're doing something to me", "React to what they say.", "sext"),
        ("S1-3", "I'm lying here and my fingers are starting to wander... I blame you for this babe", None, "sext"),
        ("S1-4", "one sec", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "I want to show you what you made me feel", "SEND PPV 1 \u2014 $12 (teasing, touching over clothes). Bought \u2192 continue. Silent 3 min \u2192 NR Waves. 'I never do this' \u2014 ONE TIME per journey.", "ppv"),
        ("S1-6", "wow... okay I need a second after that", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "but I literally can't stop touching myself right now... it's like my body won't let me", "React to what they said. HE caused this.", "sext"),
        ("S1-8", "I'm dripping wet and every time I think about you watching me it gets worse", None, "sext"),
        ("S1-9", "what would you do if you were here right now babe? I need to hear it", "Wait for reply. React to what they say.", "sext"),
        ("S1-10", "fuck hold on I need to show you something", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "look at what you're doing to me... I can't hold back anymore", "SEND PPV 2 \u2014 $25 (more explicit solo, hands wandering). Bought \u2192 continue. Silent 3 min \u2192 NR Waves.", "ppv"),
        ("S1-12", "oh fuck babe I can't stop touching myself", "Wait for reply. NO cooldown \u2014 keep momentum.", "sext"),
        ("S1-13", "I'm pushing my fingers deeper and I can't slow down... my legs are shaking", None, "sext"),
        ("S1-14", "I can feel myself about to cum... you need to see what's happening to my body right now", None, "sext"),
        ("S1-15", "one second", "WAIT 2-3 MIN", "wait"),
        ("S1-16", "you need to see this... I've never been like this before", "SEND PPV 3 \u2014 $40 (very explicit solo). Bought \u2192 continue. Silent 3 min \u2192 NR Waves.", "ppv"),
        ("S1-17", "oh my god my pussy is pulsing so hard and I can't stop", "Wait for reply.", "sext"),
        ("S1-18", "I'm right there babe... my whole body is clenching and I need you watching when this happens", None, "sext"),
        ("S1-19", "I'm cumming... fuck I can barely breathe", None, "sext"),
        ("S1-20", "wait", "WAIT 1-2 MIN", "wait"),
        ("S1-21", "cum with me babe... watch what happens to my body right now", "SEND PPV 4 \u2014 $55 (full climax). Bought \u2192 Aftercare. Silent \u2192 NR Waves.", "ppv"),
        ("AC-1", "oh my god that was... wow", None, "aftercare"),
        ("AC-2", "I've never had someone make me feel like that through a screen before. you're actually different babe", "Mention something specific he said/did. KEEP TALKING \u2014 build bond. NEVER say goodbye.", "aftercare"),
    ],

    # NR Waves
    "nr_waves": [
        ("NR-W1", "helloooo", "Send 2-3 min after PPV. Ping.", "sext"),
        ("NR-W2", "I have something to show you but you're leaving me on read babe...", "Send 3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "fine I'll just keep this to myself then", "Send 5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "miss talking to you babe, where'd you go?", "Send 15-30 min later. Warm close.", "sext"),
        ("NR-W5", "I made something special and you're the only one I want to share it with, hmu when you're free", "Send 2-6 hrs later. New convo hook.", "sext"),
    ],

    # Personal Info
    "personal_info": [
        ("Age", "I'm 18, just started this whole journey and honestly I love it", None),
        ("Location", "I'm in Spain but I don't really like sharing too many details about where exactly", "NEVER give specific city."),
        ("Profession", "I'm a student and I do content creation on the side, it kind of blew up honestly", None),
        ("Hobbies", "I'm really into the gym and running, and I try to eat healthy but I'm not perfect haha", None),
        ("Countries", "I've been to Spain, the US, and Argentina, my parents are from there", None),
        ("Relationship", "I'm single, haven't found the right person yet", None),
    ],

    # Positive Spin
    "positive_spin": [
        ("Age40Plus", "omg I actually love older guys, they know what they want and that's so attractive", None),
        ("Age20s", "oh nice we're close in age? that's actually rare on here", None),
        ("BoringJob", "honestly that sounds stable and I respect that, plus you probably have stories right?", None),
        ("CoolJob", "wait that's actually really cool, tell me more about that", None),
        ("Fit", "oh you work out? okay I see you, that's hot", None),
        ("NotFit", "I don't care about that stuff honestly, it's about the vibe not the body", None),
        ("SameCity", "wait you're close to me?? that's crazy, small world", "Add name of model's city if sub is from same area."),
        ("FarAway", "I love that you're far away, there's something exciting about connecting with someone from a different world", None),
    ],

    # Re-Engagement
    "re_engagement": [
        ("RE-1", "can't stop thinking about earlier, you free?", "Send 6-12 hrs after convo goes quiet.", "sext"),
        ("RE-2", "sooo I did something even crazier after we stopped talking, you have to see this", "Send next day. Seeds next session.", "sext"),
    ],

    # OBJ scripts — empty = use gender defaults from obj_defaults.py
    "obj_scripts": {},
}

if __name__ == "__main__":
    m = ModelFactory(config)
    m.generate_all()
