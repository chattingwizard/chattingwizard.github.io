"""
TYLER — Dating App Female Creator
22, American (Florida)
Traffic: Dating Apps. Page: Paid Page.
Voice: Takes control gradually. Casual texting, not ultra dominant.
Restrictions: No anal, no squirting, no B/G, no G/G, no video calls.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Tyler",
    "airtable_name": "Tyler",
    "folder": "tyler",
    "gender": "female",
    "traffic": "dating_app",
    "age": 22,
    "nationality": "American",
    "location": "Florida, USA",
    "origin": "Florida",
    "page_type": "Paid Page",
    "personality": "Chill girl who loves the gym and traveling. Not ultra dominant — takes control gradually and naturally. Easygoing, flirty, confident without being aggressive.",
    "voice": "Takes control gradually. Casual texting style. Playful and warm. Not aggressive.",
    "voice_pet_names": "babe, baby",
    "voice_never": "",
    "interests": ["gym", "traveling", "pasta"],
    "physical": "1.78m, athletic, brown hair, brown eyes",
    "job": "travels and lives life",
    "countries": "Europe",
    "explicit_level": "full_solo",
    "special_notes": "No anal. No squirting. No B/G. No G/G. No video calls. | Custom content: Yes",

    # ═══════════════════════════════════════
    # JOURNEY (31 messages)
    # ═══════════════════════════════════════
    "journey": [
        ("R-1", "heyy babe, your profile caught my eye, had to message you", "React to their profile. Add name if known.", "rapport"),
        ("R-2", "okay wait you're actually cute, what do you do?", "React to their response naturally.", "rapport"),
        ("R-3", "that's cool, I'm from Florida, when I'm not here I'm mostly just at the gym or traveling haha", None, "rapport"),
        ("R-4", "so be honest, what are you looking for on here?", None, "rapport"),
        ("R-5", "honestly this is the best convo I've had on here in a while, most guys are so dry", "Ego boost. Next \u2192 TB-1.", "rapport"),
        ("TB-1", "okay confession... I just got back from the gym and I'm lying in bed and this convo is making me feel some type of way", None, "teasing"),
        ("TB-2", "like you're giving me butterflies and that doesn't happen", "Wait for reply.", "teasing"),
        ("TB-3", "you know what, I want to show you something, I have a page where I post exclusive stuff", "TRANSITION to OF. Natural.", "teasing"),
        ("TB-4", "it's free to follow, no pressure, but I think you'd really like what I post there", "Send OF link. Wait for them to subscribe.", "teasing"),
        ("TB-5", "you're here! okay hold on let me send you something special for coming over babe", "SEND PPV 0 \u2014 FREE teaser. Wait for reply. Silent 3 min \u2192 NR Waves.", "ppv"),
        ("S1-1", "mmm you liked that? my body is already reacting to you... I can feel myself getting wet right now", "Wait for reply.", "sext"),
        ("S1-2", "my heart is racing and I can feel my body reacting to you and my fingers are starting to wander... this is your fault babe", "React to what they say.", "sext"),
        ("S1-3", "one sec", "WAIT 2-3 MIN", "wait"),
        ("S1-4", "I want to show you what you're doing to me", "SEND PPV 1 \u2014 $12 (teasing). Bought \u2192 continue. Silent 3 min \u2192 NR Waves. 'I never do this' \u2014 ONE TIME.", "ppv"),
        ("S1-5", "wow... okay I need a second after that", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-6", "I've never been this wet from someone I met on an app before... you're doing something to me", None, "sext"),
        ("S1-7", "I can't stop touching myself and it's all because of you babe", "React to what they said.", "sext"),
        ("S1-8", "hold on", "WAIT 2-3 MIN", "wait"),
        ("S1-9", "you need to see this right now", "SEND PPV 2 \u2014 $25 (more explicit). Bought \u2192 continue. Silent 3 min \u2192 NR Waves.", "ppv"),
        ("S1-10", "oh fuck babe I can't stop", "Wait for reply. NO cooldown.", "sext"),
        ("S1-11", "I'm pushing my fingers deeper and my legs are shaking... I can feel myself getting close", None, "sext"),
        ("S1-12", "I need you to see what you're doing to me right now", None, "sext"),
        ("S1-13", "one second", "WAIT 2-3 MIN", "wait"),
        ("S1-14", "you need to see this... I've never been like this before", "SEND PPV 3 \u2014 $40 (very explicit). Bought \u2192 continue. Silent 3 min \u2192 NR Waves.", "ppv"),
        ("S1-15", "oh my god my pussy is pulsing so hard and I can't stop", "Wait for reply.", "sext"),
        ("S1-16", "I'm right there babe... I need you watching when this happens", None, "sext"),
        ("S1-17", "I'm cumming... fuck I can barely breathe", None, "sext"),
        ("S1-18", "wait", "WAIT 1-2 MIN", "wait"),
        ("S1-19", "watch what happens babe", "SEND PPV 4 \u2014 $55 (full climax). Bought \u2192 Aftercare. Silent \u2192 NR Waves.", "ppv"),
        ("AC-1", "oh my god that was... wow, I can't believe that just happened with someone from a dating app", None, "aftercare"),
        ("AC-2", "you're actually different from everyone else on there babe. I mean it", "Mention something specific. KEEP TALKING. NEVER say goodbye.", "aftercare"),
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
        ("LOC-1", "I'm in Florida but I don't like sharing too many details until I know someone better", "GENERIC area only. Never specific."),
        ("LOC-2", "why do you want to know? planning something?", "Playful deflection."),
        ("LOC-3", "let's focus on getting to know each other first, location doesn't matter when the convo is this good", "Final redirect."),
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
        ("Age", "I'm 22, still figuring life out haha", None),
        ("Location", "I'm in Florida but I don't really like sharing too many details about where exactly", "NEVER give specific neighborhood or address."),
        ("Profession", "I do content creation full time, I just travel and enjoy life honestly", None),
        ("Hobbies", "I'm really into the gym and I love pasta way too much, that's pretty much my life outside of this", None),
        ("Countries", "I've been around Europe, I love traveling whenever I can", None),
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
