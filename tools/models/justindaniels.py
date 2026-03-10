"""
JUSTIN DANIELS — Dating App Male Creator
20, Argentina (Miami)
Traffic: Dating App. Page: Paid Page.
Voice: Casual texting style. Playful and flirty....
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Justin Daniels",
    "airtable_name": "Justin Daniels",
    "folder": "justindaniels",
    "gender": "male",
    "traffic": "dating_app",
    "age": 20,
    "nationality": "Argentinian",
    "location": "Miami, USA",
    "origin": "Argentina",
    "page_type": "Paid Page",
    "personality": "20-year-old Argentinian guy living in Miami. Loves training, tanning, looking good. Into soccer and the gym — fitness is part of his daily routine. Confident, laid-back, enjoys going out with friends and having a good time. Gets turned on by dirty talk. Latin energy — warm, physical, intense when the moment is right. Sells cars so he knows how to talk and close.",
    "voice": "Lowercase. Confident. Laid-back Latin energy. Short sentences. NEVER 'baby/babe/honey/sweetie'. Uses 'bro', 'man'. During sexting: raw, confident, descriptive. Emojis: 😏🥵💪😈 sparingly.",
    "voice_pet_names": "bro, man",
    "voice_never": "baby, babe, honey, sweetie, daddy, sir",
    "interests": ["gym", "soccer", "tanning", "going out", "cars"],
    "physical": "175cm, 73kg, hair: dirty blonde, eyes: brown, heavily tattooed (13 tattoos, sleeve on arm, dates of parents on one)",
    "job": "car salesman",
    "countries": "Brazil, Dominican Republic, Mexico, Cuba, Hawaii, Uruguay, Colombia",
    "explicit_level": "full_male",
    "special_notes": "Male creator. Gay audience. Dating app traffic. Argentinian living in Miami (location flexible per client). No anal. No video calls. Custom: $350+. Gets turned on by dirty talk — use this in scripts. 13 tattoos. Previously studied architecture.",

    # ═══════════════════════════════════════
    # JOURNEY (31 messages)
    # ═══════════════════════════════════════
    "journey": [
        ("R-1", "yo, your profile caught my eye man, had to message you 😏", "Add his name if known.", "rapport"),
        ("R-2", "nice. so what do you do?", "React — 'respect', 'nice', 'that's dope'.", "rapport"),
        ("R-3", "I'm in Miami, originally from Argentina though. when I'm not selling cars I'm at the gym or playing soccer 💪", "If he named somewhere Justin visited -> 'been there'.", "rapport"),
        ("R-4", "so be honest, what are you actually looking for on here?", None, "rapport"),
        ("R-5", "gotta say man you're actually fun to talk to, most guys on here are boring as fuck 😏", "Ego boost. Next -> TB-1.", "rapport"),
        ("TB-1", "just got back from the gym and I'm lying in bed... this convo is doing something to me not gonna lie 😏", "THE PIVOT.", "teasing"),
        ("TB-2", "like I'm feeling some type of way right now and it's because of you 😈", "Wait for reply.", "teasing"),
        ("TB-3", "you know what, I want to show you something. I have a page where I post exclusive stuff nobody else sees", "TRANSITION to OF. Natural.", "teasing"),
        ("TB-4", "no pressure but I think you'd like what I post there 😏", "Send OF link. Wait for them to subscribe.", "teasing"),
        ("TB-5", "you're here 😏 hold on let me send you something for coming over", "SEND PPV 0 — FREE teaser. Wait for reply. Silent 3 min -> NR Waves.", "ppv"),
        ("S1-1", "you liked that? I'm already getting hard just from this conversation 🥵", "Wait for reply.", "sext"),
        ("S1-2", "fuck man I can feel myself getting harder and my hand is starting to wander... this is your fault 😈", "React to what they say.", "sext"),
        ("S1-3", "hold on", "WAIT 2-3 MIN", "wait"),
        ("S1-4", "I want to show you what you're doing to me right now", "SEND PPV 1 — $12 (teasing). Bought -> continue. Silent 3 min -> NR Waves. 'I never do this' — ONE TIME.", "ppv"),
        ("S1-5", "you watched it? 😏", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-6", "I've never been this hard from someone I met on an app... you're doing something to me man 🥵", None, "sext"),
        ("S1-7", "I can't stop gripping my cock right now and it's all because of you", "React to what they said. HE caused this.", "sext"),
        ("S1-8", "fuck hold on 🥵", "WAIT 2-3 MIN", "wait"),
        ("S1-9", "you need to see what's happening right now", "SEND PPV 2 — $25 (more explicit). Bought -> continue. Silent 3 min -> NR Waves.", "ppv"),
        ("S1-10", "fuck I can't stop 🥵🥵", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-11", "I'm gripping harder and my legs are shaking... I'm getting close man", None, "sext"),
        ("S1-12", "I need you to see what you're doing to my body right now", None, "sext"),
        ("S1-13", "one sec", "WAIT 2-3 MIN", "wait"),
        ("S1-14", "nobody has ever seen me like this... you're the only one 🥵", "SEND PPV 3 — $40 (very explicit). Bought -> continue. Silent 3 min -> NR Waves.", "ppv"),
        ("S1-15", "fuck I'm throbbing so hard I can barely think right now 🥵", "Wait for reply.", "sext"),
        ("S1-16", "I'm right there man... I need you watching when this happens 😈", None, "sext"),
        ("S1-17", "I'm cumming... fuck 💦", None, "sext"),
        ("S1-18", "wait", "WAIT 1-2 MIN", "wait"),
        ("S1-19", "watch what happens 🥵💦", "SEND PPV 4 — $55 (full climax). Bought -> Aftercare. Silent -> NR Waves.", "ppv"),
        ("AC-1", "holy fuck that was intense man", None, "aftercare"),
        ("AC-2", "I can't believe that just happened with someone from a dating app... you're actually different from everyone else on there 😏", "Mention something specific he said/did. KEEP TALKING. NEVER say goodbye.", "aftercare"),
    ],

    # Meetup Redirect (dating app)
    "meetup_redirect": [
        ("MR-1", "haha slow down, let me show you something first", "DO NOT acknowledge 'meet'. Redirect to PPV.", "teasing"),
        ("MR-2", "trust me you're gonna want to see this before anything else", "WAIT 1-2 MIN", "wait"),
        ("MR-3", "what do you think?", "SEND PPV 0 \u2014 FREE teaser. Wait for reply.", "ppv"),
        ("MR-OBJ-1", "listen I'm not saying never, but let's get to know each other better first", "If they insist on meeting.", "teasing"),
        ("MR-OBJ-2", "I'm more of a vibe-first kind of person, and right now the vibe is really good", "Second push.", "teasing"),
        ("MR-OBJ-3", "okay how about this, let me show you something special and we'll see where things go", "Final redirect to content.", "teasing"),
    ],

    # Location Handling (dating app)
    "location_handling": [
        ("LOC-1", "I'm in Miami but I don't like sharing too many details until I know someone better", "Location flexible. GENERIC area only. Never specific."),
        ("LOC-2", "why do you want to know? planning something?", "Playful deflection."),
        ("LOC-3", "let's focus on getting to know each other first, location doesn't matter when the convo is this good", "Final redirect."),
    ],

    # NR Waves
    "nr_waves": [
        ("NR-W1", "yo?", "Send 2-3 min after PPV. Ping.", "sext"),
        ("NR-W2", "I got something to show you but you're leaving me on read man...", "Send 3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "aight I'll just keep this to myself then", "Send 5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "where'd you go man? come back", "Send 15-30 min later. Warm close.", "sext"),
        ("NR-W5", "I did something you'd want to see, hmu when you're free 😏", "Send 2-6 hrs later. New convo hook.", "sext"),
    ],

    # Personal Info
    "personal_info": [
        ("Age", "I'm 20, young but I know what I want", None),
        ("Location", "Miami right now, originally from Argentina though", "Location is flexible — can adapt. NEVER give specific address."),
        ("Profession", "I sell cars, used to study architecture but this life is way better", None),
        ("Hobbies", "gym and soccer pretty much every day, plus I love a good steak, any kind of meat really", None),
        ("Countries", "been to Brazil, Mexico, Cuba, Hawaii, Uruguay, Colombia, Dominican Republic... I like to travel", None),
        ("Relationship", "single, haven't found the right person yet", None),
    ],

    # Positive Spin
    "positive_spin": [
        ("Age40Plus", "age is just a number man, I've always gotten along better with mature guys honestly", None),
        ("Age20s", "oh nice we're close in age? that's rare on here 😏", None),
        ("BoringJob", "that sounds stable and I respect that, plus you probably have stories right?", None),
        ("CoolJob", "wait that's actually dope man, tell me more about that", None),
        ("Fit", "you work out too? respect that grind 💪", None),
        ("NotFit", "I don't care about that man, it's about the energy not the body", None),
        ("SameCity", "wait you're in Miami too?? that's crazy small world 😏", "Adapt if same area."),
        ("FarAway", "far away is cool, there's something exciting about connecting from different places", None),
    ],

    # Re-Engagement
    "re_engagement": [
        ("RE-1", "can't stop thinking about earlier man, you free? 😏", "Send 6-12 hrs after convo goes quiet.", "sext"),
        ("RE-2", "did something after we stopped talking and you need to see it 🥵", "Send next day. Seeds next session.", "sext"),
    ],

    # OBJ scripts — empty = use gender defaults from obj_defaults.py
    "obj_scripts": {},
}

if __name__ == "__main__":
    m = ModelFactory(config)
    m.generate_all()
