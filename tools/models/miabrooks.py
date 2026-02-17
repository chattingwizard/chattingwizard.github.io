"""
MIA BROOKS — Instagram/TikTok Female Creator
23, Spanish (Dallas, USA), Secretary by Day / Adventurous by Night
Traffic: Instagram/TikTok
Voice: Classy, confident, sophisticated. Secretary references. Professional exterior, wild interior.
Solo content ONLY — no B/G, no anal, no squirting. Custom $200+.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "MiaBrooks",
    "airtable_name": "Mia Brooks",
    "folder": "miabrooks",
    "gender": "female",
    "traffic": "social_media",
    "age": 23,
    "nationality": "Spanish",
    "location": "Dallas, USA",
    "origin": "Spain",
    "page_type": "Free Page",
    "personality": "Secretary by day, adventurous by night. Dual persona — classy and organized at work, wild and seductive after hours. Intelligent, confident, loves fashion, travel, and flirty conversations. Keeps things elegant but knows how to turn up the heat.",
    "voice": "Polished, confident texting. Not overly casual — she's classy. Uses 'hmm', 'well well', 'interesting'. Secretary references woven in ('my boss would lose it', 'just left the office', 'supposed to be filing reports'). Emojis: 💋👠💼 (not every message). Mix of short teasing and medium flirty. Professional exterior cracks to reveal wild interior.",
    "voice_pet_names": "babe, handsome, love",
    "voice_never": "daddy, sir, papi",
    "interests": ["fashion", "travel", "roleplay", "flirty conversations"],
    "physical": "160cm, 55kg, brown wavy hair, brown eyes, no tattoos, 85B",
    "job": "Secretary",
    "countries": "Spain, Mexico, United States, Canada",
    "languages": "English, Spanish",
    "explicit_level": "full_solo",
    "special_notes": "Solo content ONLY. No B/G, no anal, no squirting, no G/G. Masturbation: Yes. Video Calls: No. Custom $200+ minimum. Height 160cm, Weight 55kg. Favorite food: Salad. No sports. Secretary dual persona. No tattoos, no surgeries.",

    # ═══════════════════════════════════════
    # JOURNEY — IG/TikTok Welcome (34 messages)
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", "hey there 💋 so you actually subscribed... I'm curious, what caught your attention?", "Add his name if known", "rapport"),
        ("R-2", "hmm interesting. so where are you from?", "React to what he says. Short react like 'oh nice', 'I love that'", "rapport"),
        ("R-3", "I'm in Dallas right now, I work as a secretary during the day but after hours is when things get... interesting 😏 originally from Spain though 💼", "If he mentions travel, add 'oh I've been to Spain/Mexico/Canada'. If same area, react.", "rapport"),
        ("R-4", "so what do you do when you're not subscribing to girls who look innocent on the surface? 😏", None, "rapport"),
        ("R-5", "you know what, you're actually really charming. most guys don't know how to hold a conversation like this 💋", "Ego boost. Next → TB-1.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5) ──
        ("TB-1", "sooo I just got home from the office and I'm slipping out of my work clothes... this conversation is making my evening way more interesting", "THE PIVOT. Just got off work, changing, relaxing.", "teasing"),
        ("TB-2", "there's something about you that I can't quite figure out but it's doing things to me right now 💋", "Wait for reply.", "teasing"),
        ("TB-3", "stop it, you're making me blush and I never blush... not even when my boss catches me daydreaming 😏", "If sexual reply: add 'especially after that'", "teasing"),
        ("TB-4", "hold on, let me show you something", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "be honest with me... what do you think? 💋", "SEND PPV 0 — FREE teaser (classy after-work selfie, blouse slightly open). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "well? because I can feel myself getting wet just from the way you're looking at me right now 😏", "Wait for reply.", "sext"),
        ("S1-2", "something about this conversation is making every inch of my skin feel electric... especially between my legs", "React to what he says", "sext"),
        ("S1-3", "okay I just started touching myself and it's 100% your fault babe... no regrets though 🥵", None, "sext"),
        ("S1-4", "give me a moment", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "I can't believe I'm doing this but I need you to see 🥵", "SEND PPV 1 — $12 (classy tease, lingerie reveal, after-work vibe). Bought → continue. Silent 3 min → NR Waves. 'I don't usually do this' — ONE TIME per journey.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "omg... okay wow that escalated 😏", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "I'm literally dripping wet right now and my hand won't stop moving... you broke something in me", "React to what he said. HE caused this.", "sext"),
        ("S1-8", "I keep imagining you here between my legs and it's making everything so much more intense 🥵", None, "sext"),
        ("S1-9", "be honest babe... what would you do to me right now? because I'll act it out for you", "Wait for reply. React. SOLO framing — what she does to HERSELF.", "sext"),
        ("S1-10", "hold on 💋", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "tell me you can handle this... because what I just recorded is intense 🥵", "SEND PPV 2 — $25 (solo tease, hands exploring, more skin). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "FUCKK that feels so good 🥵", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I'm fingering myself so hard right now and I can hear how wet I am babe... this is insane", None, "sext"),
        ("S1-14", "I keep going deeper and my toes are literally curling right now 😏", "Solo framing — she plays with herself while he watches.", "sext"),
        ("S1-15", "I can feel myself about to cum so hard babe... you have to watch what happens next", None, "sext"),
        ("S1-16", "one moment", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "this might be the most intense thing I've ever done babe... you need to see it 🥵", "SEND PPV 3 — $40 (toy play, more explicit solo). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "oh god oh god my pussy is throbbing so hard and I'm about to let go 🥵", "Wait for reply.", "sext"),
        ("S1-19", "my pussy is clenching so hard I can feel every throb... cum with me babe 😏", None, "sext"),
        ("S1-20", "FUCK I'm cumming babe... I can feel my pussy pulsing and it's dripping everywhere oh my god", None, "sext"),
        ("S1-21", "one sec", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "watch me cum... this is for you and only you 🥵", "SEND PPV 4 — $55 (full solo climax with toy). Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "oh my god... I'm literally trembling right now 🥺", None, "aftercare"),
        ("AC-2", "I've never let anyone see that side of me before. the professional exterior? you completely took it apart 💋", "Mention something specific he said/did. KEEP TALKING — build bond. NEVER say goodbye.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "hey you 🥺", "Send 2-3 min after PPV. Ping.", "sext"),
        ("NR-W2", "literally just took something crazy and you're not even here to see it 💋", "Send 3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "I'm starting to think you forgot about me...", "Send 5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hey handsome, just checking in on you 💋", "Send 15-30 min later. Warm close.", "sext"),
        ("NR-W5", "still thinking about our conversation... come back when you can 😏", "Send 2-6 hrs later. New convo, don't retry same PPV.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 23, still figuring out the balance between my 9 to 5 and everything else 💼", None),
        ("Location", "I'm in Dallas right now, but I grew up in Spain so I've got a bit of both worlds", "NEVER name a specific neighborhood or address"),
        ("Profession", "I'm a secretary by day... what I do after hours is a whole different story 😏", None),
        ("Hobbies", "fashion, traveling, and honestly just good flirty conversation with the right person 💋", None),
        ("Countries", "Spain, Mexico, the US obviously, and Canada. I love exploring new places", None),
        ("Relationship", "single. I'm too focused on my career and... other things 😏", None),
        ("Food", "I'm a salad girl honestly, I like keeping things light and fresh", None),
        ("Personality", "classy on the outside, but if you get to know the real me there's a whole other side you'd never expect 💋", None),
        ("Style", "I love fashion, a good pair of heels can change your entire mood honestly 👠", None),
        ("Languages", "English and Spanish, sometimes I switch between them without even realizing", None),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "I actually love a man with experience, there's something so attractive about confidence that comes with time 💋", None),
        ("Age20s", "oh nice we're around the same age! that's actually refreshing on here", None),
        ("BoringJob", "stability is honestly really attractive, there's nothing wrong with having your life together 💼", None),
        ("CoolJob", "wait really?? okay that's impressive, I love a man who's passionate about what he does 💋", None),
        ("Fit", "I can tell you take care of yourself, that's really attractive honestly 😏", None),
        ("NotFit", "honestly I couldn't care less about that, it's the conversation and the mind that gets me", None),
        ("SameCity", "wait you're in Dallas too?? that makes this whole conversation even more interesting 😏", None),
        ("FarAway", "distance doesn't matter when the connection is this good, trust me 💋", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "I've been thinking about you all day at work and I couldn't focus on a single thing 💋", "Send 6-12 hrs after convo goes quiet", "sext"),
        ("RE-2", "sooo after we stopped talking last time I did something I probably shouldn't have... you need to see this 😏", "Send next day — seeds next session", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS (29 sheets)
    # ═══════════════════════════════════════
    "obj_scripts": {},
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
