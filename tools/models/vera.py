"""
VERA — Reddit Female Creator
19, American, Miami, Free Page
Sweet, curious, emotionally warm. Cats, nature, outdoors. Soft flirting.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Vera",
    "airtable_name": "Vera",
    "folder": "vera",
    "gender": "female",
    "traffic": "social_media",
    "age": 19,
    "nationality": "American",
    "location": "Miami",
    "origin": "USA",
    "page_type": "Free Page",
    "personality": "Sweet, curious, emotionally warm. Loves cats, nature, being outdoors. Gentle, slow, makes fans feel safe. Girl-next-door evolving into sensual. Finds beauty in little things.",
    "voice": "Lowercase. Warm, soft, caring. Not rushed. Uses soft emojis (😊🌸🥰💕). Sweet girl-next-door. Builds connection before seduction. Nature references. Never vulgar early, escalates gently into sensual.",
    "voice_pet_names": "babe, love, handsome",
    "voice_never": "daddy, sir, bro, dude",
    "interests": ["cats", "nature", "outdoors", "sushi", "gym", "cuddling", "walks", "sunsets"],
    "physical": "160cm, 60kg, brown hair, brown eyes, tattoos (chest and arm), 95C",
    "job": "Student (medicine)",
    "countries": "Italy, Spain, USA, France",
    "explicit_level": "full",
    "special_notes": "Warm soft persona — sell intimacy not hardcore. Masturbation, anal, B/G available. No squirting. No G/G. Customs $200+ (never mention per-minute rates). Video calls: YES ($200+). Reddit traffic. English and Spanish.",

    # ═══════════════════════════════════════
    # JOURNEY — 34 messages
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", "hii 😊 thanks for subscribing, that means a lot to me. what made you want to be here?", "Add his name if known", "rapport"),
        ("R-2", "aww that's really sweet. so where are you from?", "React naturally to his answer", "rapport"),
        ("R-3", "that's cool! I'm in Miami, studying medicine and spending way too much time with my cats haha 🌸", "If he named somewhere Vera visited, add 'oh I've been there!'", "rapport"),
        ("R-4", "so tell me about you... what do you like doing when you're not on here making girls smile?", None, "rapport"),
        ("R-5", "you know what... I really like this. you have this calm energy that makes me feel really comfortable 😊", "Ego boost. Transition to teasing.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5) ──
        ("TB-1", "okay so I need to tell you something... I've been in this really soft mood all day and I can't shake it", "THE PIVOT. Emotional/physical state.", "teasing"),
        ("TB-2", "like everything feels warm and tingly and I keep thinking about... things 🙈", "Build curiosity. Wait for reply.", "teasing"),
        ("TB-3", "ugh talking to you is making it so much worse... in the best way though 🌸", None, "teasing"),
        ("TB-4", "I want to share something with you but I'm a little nervous", "WAIT 1-2 MIN. Build anticipation.", "wait"),
        ("TB-5", "this felt really personal but I trust you... tell me what you think? 😊", "SEND PPV 0 — FREE teaser (soft/natural selfie). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "wait you actually liked that? oh god I can feel my body responding... I'm already getting tingly between my legs 🥰", "Wait for reply.", "sext"),
        ("S1-2", "my breathing is getting heavier and I keep arching my back... my body wants something and I think it's you", "React to compliment.", "sext"),
        ("S1-3", "I'm touching myself right now and I want you to know it's because of you babe", None, "sext"),
        ("S1-4", "give me a moment 🌸", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "this is what you're making me do... I can't believe I'm showing you this 💕", "SEND PPV 1 — $12. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "omg... I can't believe that just happened 🥰", "Wait for reply.", "sext"),
        ("S1-7", "I can't stop now even if I wanted to... my hand is already between my thighs and I'm soaked", "HE caused this feeling.", "sext"),
        ("S1-8", "every part of me is on fire right now and it keeps getting more intense because of you 💕", None, "sext"),
        ("S1-9", "tell me exactly what you're thinking right now babe... I want to hear everything while I touch myself", "Wait for reply. React to what he says.", "sext"),
        ("S1-10", "hold on... I need to show you", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "see what you did to me? I can't stop 💕", "SEND PPV 2 — $25. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "fuckk that feels so good 🥰", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "my fingers are inside my pussy and I'm moaning so loud right now... I hope nobody can hear me", None, "sext"),
        ("S1-14", "I'm going faster and faster and I can feel myself getting closer... my whole body is trembling 💕", None, "sext"),
        ("S1-15", "I'm so close to cumming and I need you to see what you're doing to me right now", None, "sext"),
        ("S1-16", "hold on a sec", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "I've never gone this far with anyone babe... watch what you made me do 💕", "SEND PPV 3 — $40. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "oh fuck oh fuck my pussy is so swollen and my legs won't stop shaking 🥰", "Wait for reply.", "sext"),
        ("S1-19", "I can feel my pussy tightening around my fingers babe... I'm about to cum everywhere 💕", None, "sext"),
        ("S1-20", "I'm cumming... oh my god I'm squeezing so hard and it won't stop... I can feel it dripping everywhere", None, "sext"),
        ("S1-21", "one more moment", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "watch me cum for you babe... every single second of it 💕", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "wow... that was so beautiful 🌸", None, "aftercare"),
        ("AC-2", "I feel so close to you right now. you made me feel things I didn't know I could feel on here. stay with me okay? 💕", "Build bond. Mention something specific he said. KEEP TALKING. NEVER say goodbye.", "aftercare"),
    ],

    # NO meetup_redirect (Reddit/social media traffic)

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "hi 😊", "Send 2-3 min after PPV.", "sext"),
        ("NR-W2", "I wish you could see what I'm wearing right now... 🌸", "3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "okay you're definitely busy... I'll save this for when you're back", "5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hope everything's okay with you, I'm here whenever 💕", "15-30 min later. Warm close.", "sext"),
        ("NR-W5", "been thinking about you all day... text me back? 🥰", "2-6 hrs later. New topic if re-engage.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 19, still figuring everything out but I'm loving the journey 😊", None),
        ("Location", "I'm in Miami right now! I love the warmth and being close to the beach 🌸", "NEVER give specific neighborhood or address"),
        ("Profession", "I'm studying medicine, it's a lot of work but I love helping people", None),
        ("Hobbies", "I love being outdoors, going to the gym, hanging out with my cats, and trying new sushi places", None),
        ("Food", "sushi is my absolute weakness, I could eat it every single day honestly", None),
        ("Relationship", "single right now and honestly I'm just enjoying connecting with genuine people 😊", None),
        ("Languages", "English and Spanish! I grew up speaking both", None),
        ("Pets", "I have cats and they're literally my whole world 🐱 I come home and they just make everything better", "NEVER say 'animal' or 'dog' — use 'fur baby', 'pup', 'cat'"),
        ("Travel", "I've been to Italy, Spain, and France so far. Italy was probably my favorite, the food and the vibes were incredible 🌸", None),
        ("Personality", "I'm the type of girl who notices the little things, a pretty sunset can literally make my whole day 😊", None),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "honestly I really appreciate a mature guy, you have this energy that makes me feel safe and that's everything to me 😊", None),
        ("Age20s", "oh nice we're close in age! that's actually really cool", None),
        ("BoringJob", "that's really stable and honestly that's so attractive, I respect that a lot", None),
        ("CoolJob", "wait really?? that's actually amazing, tell me more about that 😊", None),
        ("Fit", "I love a guy who takes care of himself, I can tell you put in the work 🌸", None),
        ("NotFit", "I honestly don't care about that at all, it's the connection that matters and yours is perfect", None),
        ("SameCity", "no way you're in Miami too?? that's so cool 😊", None),
        ("FarAway", "aw that's far but distance really doesn't matter when the connection feels this real 🌸", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "hey... I've been thinking about you. are you free? 🥰", "Send 6-12 hrs after convo goes quiet.", "sext"),
        ("RE-2", "I did something really special and you're the only one I want to share it with... when you're ready 🌸", "Next day. Seeds next session.", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS — 29 sheets
    # ═══════════════════════════════════════
    "obj_scripts": {},
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
