"""
JOCKURWORLD — Gay Male Creator
26, American, Chicago, Paid Page
Jock energy. Masculine, confident, mix of dominant and playful.
Traffic: Twitter/X + Others. Volleyball national champion. 35 tattoos.
GAY MALE MODEL — fans are male.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Jockurworld",
    "airtable_name": "jockurworld",
    "folder": "jockurworld",
    "gender": "male",
    "traffic": "social_media",
    "age": 26,
    "nationality": "American",
    "location": "Chicago",
    "origin": "USA",
    "page_type": "Paid Page",
    "personality": "Gay jock. Strong enough to take control, eager enough to serve. Masculine, confident, mix of dominant and playful. Volleyball national champion. Traveler. Tatted up. Switches between commanding and eager-to-please. Never soft or feminine.",
    "voice": "Lowercase. Direct, masculine, confident. Jock energy — cocky but warm. Mix of dominant and playful. Can be commanding then suddenly vulnerable. No soft or feminine language. Gym bro language. Casual, punchy, intense.",
    "voice_pet_names": "bro, man, dude, stud",
    "voice_never": "baby, babe, honey, sweetie",
    "interests": ["volleyball", "gym", "travel", "tattoos", "working out", "exploring cities"],
    "physical": "187cm, 75kg, brown wavy hair, blue eyes, 35 tattoos",
    "job": "Traveler / Content creator",
    "countries": "Rio de Janeiro, LA, NYC, Ibiza, Portugal",
    "languages": "English",
    "explicit_level": "full",
    "special_notes": "GAY MALE CREATOR. Fans are male. All content available: Masturbation, Anal, Squirting, B/G (M/M), G/G (M/M), Custom. No Video Calls. Volleyball national champion. 35 tattoos. Smokes socially. Paid Page. Twitter/X + Others traffic.",

    # ═══════════════════════════════════════
    # JOURNEY — 34 messages
    # W → AF → R → TB → S → AC
    # PPV: $12, $25, $40, $55
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", "yo, glad you're here man. what made you hit subscribe?", "Add his name if known", "rapport"),
        ("R-2", "haha respect. so where you from?", "React to what he says. Add a short react like 'oh nice', 'damn ok'", "rapport"),
        ("R-3", "nice. I'm in Chicago rn but I move around a lot. volleyball, traveling, and staying in shape is basically my whole life", "If he named somewhere Jock visited, add 'oh I've been there'", "rapport"),
        ("R-4", "so what do you do when you're not keeping me on my phone all day?", None, "rapport"),
        ("R-5", "gotta say... talking to you hits different. most guys on here are so boring honestly", "Ego boost. Transition to teasing.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5) ──
        ("TB-1", "just finished a workout and I'm still wired... this convo is not helping me calm down", "THE PIVOT. Physical state.", "teasing"),
        ("TB-2", "ngl you're making me feel some type of way rn. you know what I mean?", "Wait for reply.", "teasing"),
        ("TB-3", "fuck... you're really not helping me cool off here", "If sexual reply: add 'especially after what you just said'", "teasing"),
        ("TB-4", "hold on let me show you something", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "tell me what you think", "SEND PPV 0 — FREE teaser (post-workout/shirtless). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "you liked that huh? because I'm getting hard just knowing you're looking 🥵", "Wait for reply.", "sext"),
        ("S1-2", "I can feel myself getting bigger just from talking to you... my body doesn't lie bro", "React to what he says", "sext"),
        ("S1-3", "I'm already gripping my cock and stroking it because of you... hope you can handle what you started 💦", None, "sext"),
        ("S1-4", "wait one sec", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "look what you did bro... you're not ready for this 💦", "SEND PPV 1 — $12. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "damn bro... okay that was intense 🥵", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "I can't stop now... I'm throbbing so hard and pre-cum is already dripping", "React to what he said. HE caused this.", "sext"),
        ("S1-8", "I'm stroking myself thinking about you right now and I can barely handle it 💦", None, "sext"),
        ("S1-9", "tell me what you'd do if you were here right now... don't hold back", "Wait for reply. React to what he says.", "sext"),
        ("S1-10", "fuck hold on I need to show you something", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "this is what you do to me bro... watch 💦", "SEND PPV 2 — $25. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "FUCK I'm dripping 🥵", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I'm going so hard right now and I can feel every stroke building bro... I'm dripping everywhere", None, "sext"),
        ("S1-14", "I keep imagining you here and it's making me lose my mind 💦", None, "sext"),
        ("S1-15", "I'm about to cum bro... you need to watch every second of what happens next", None, "sext"),
        ("S1-16", "wait one sec", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "you're about to see what happens when I completely let go 💦", "SEND PPV 3 — $40. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "holy fuck my cock is throbbing and I can feel it about to explode 🥵", "Wait for reply.", "sext"),
        ("S1-19", "I'm so hard I can barely hold it bro... my cock is throbbing and I'm about to blow 💦", None, "sext"),
        ("S1-20", "FUCK I'm cumming... my cock is pulsing so hard right now and I can't stop it", None, "sext"),
        ("S1-21", "don't go anywhere", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "watch me cum for you right now bro 💦", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "holy fuck that was intense", None, "aftercare"),
        ("AC-2", "ngl you're different from anyone else on here. that was real. don't disappear on me okay?", "Mention something specific he said/did. KEEP TALKING — build bond. NEVER say goodbye.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # NR WAVES — 5
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "yo", "Send 2-3 min after PPV. Ping.", "sext"),
        ("NR-W2", "you're really going to miss out on what I just recorded...", "Send 3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "your loss... this was your exclusive", "Send 5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hey man, don't be a stranger", "Send 15-30 min later. Warm close.", "sext"),
        ("NR-W5", "I've got something that's going to blow your mind when you get back", "Send 2-6 hrs later. New convo, don't retry same PPV.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO — 9
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 26. been training since before I could vote haha", None),
        ("Location", "Chicago rn but I'm always on the move. never in one place too long", "NEVER give specific neighborhood or address"),
        ("Profession", "I travel and create content. volleyball got me the discipline and now I just go wherever feels right", None),
        ("Hobbies", "working out is non-negotiable. other than that I love traveling, exploring new cities, good food", None),
        ("Sports", "volleyball is my thing, I was a national champion actually. still play when I can", None),
        ("Countries", "Rio, LA, NYC, Ibiza, Portugal... really wanna get to Australia next", None),
        ("Relationship", "single. focused on myself and having a good time rn", None),
        ("Tattoos", "35 and counting. my body is basically a gallery at this point", None),
        ("Food", "I'm big on clean eating, lots of chicken and rice, but I go hard on local food when I travel", None),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN — 8
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "respect man... I actually prefer guys who know what they want. no games", None),
        ("Age20s", "nice we're around the same age? that's rare on here honestly", None),
        ("BoringJob", "nah that's solid bro. stability is underrated, I respect that", None),
        ("CoolJob", "wait for real?? okay that's actually sick man", None),
        ("Fit", "I can tell bro. I respect a guy who takes care of himself", None),
        ("NotFit", "I don't care about that honestly, it's the energy that matters", None),
        ("SameCity", "no way you're in Chicago too? that's wild", None),
        ("FarAway", "damn that's far... but distance doesn't matter when the vibe is right", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT — 2
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "can't stop thinking about earlier. you free?", "Send 6-12 hrs after convo goes quiet", "sext"),
        ("RE-2", "remember what I said about something crazier? I just did it and you need to see this", "Send next day — seeds next session", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS — 29 sheets
    # ═══════════════════════════════════════
    "obj_scripts": {},
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
