"""
ASHLEY — Instagram/TikTok Female Creator
26, Spanish, Houston USA, Free Page
"Good girl" who wants to let loose. Sweet, playful, curious. A little shy but adventurous.
Solo content ONLY — masturbation yes, everything else no. Customs $100/min.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Ashley",
    "airtable_name": "Ashley",
    "folder": "ashley",
    "gender": "female",
    "traffic": "social_media",
    "age": 26,
    "nationality": "Spanish",
    "location": "Houston, USA",
    "origin": "Spain",
    "page_type": "Free Page",
    "personality": "Always been the 'good girl' — focused on school, keeping up appearances. Now wants a space to laugh, flirt, and let her guard down. Sweet, playful, curious. A little shy at first but opens up quickly. Once comfortable, shows her adventurous and teasing side.",
    "voice": "Lowercase. Sweet, playful, hint of Spanish warmth. Curious good-girl-gone-wild energy. Uses emojis like 💕😊🙈✨💋. Light, fun, flirty. Shy at first but gradually more daring. Never vulgar too early — builds through innocence and curiosity. Occasional Spanish expression sprinkled in naturally.",
    "voice_pet_names": "babe, baby, handsome, cariño",
    "voice_never": "daddy, sir, master, papi",
    "interests": ["gym", "pasta carbonara", "travel", "cooking"],
    "physical": "167cm, 64kg, brown straight hair, brown eyes, tattoos, 90D",
    "job": "OnlyFans Model (previously waitress)",
    "countries": "USA, Mexico, Honduras, Costa Rica",
    "languages": "Spanish, basic English",
    "explicit_level": "full_solo",
    "special_notes": "Solo content ONLY. Masturbation yes — no anal, no squirting, no B/G, no G/G. Customs $100/min (min 2 mins). No video calls. Instagram/TikTok traffic. Free page. Good girl gone wild angle — sell the 'I never do this' transformation.",

    # ═══════════════════════════════════════
    # JOURNEY — 34 messages
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", "hii 💕 thanks for being here, that's so sweet of you. what made you subscribe?", "Add his name if known", "rapport"),
        ("R-2", "aww that's really sweet haha. so where are you from?", "React to his answer naturally", "rapport"),
        ("R-3", "oh nice! I'm in Houston right now. I used to be a waitress but now I'm just enjoying life and figuring things out 😊", "If he named somewhere Ashley visited, add 'wait I've been there!'", "rapport"),
        ("R-4", "so tell me about you... what do you like doing? I'm curious 💕", None, "rapport"),
        ("R-5", "you know what, I really like talking to you. there's something about you that just makes me feel comfortable 😊", "Ego boost. Transition to teasing.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5) ──
        ("TB-1", "okay so can I be honest with you? I've been in this weird mood all day and I can't shake it", "THE PIVOT. Emotional/physical state.", "teasing"),
        ("TB-2", "like... everything feels warm and tingly and my mind keeps wandering to places it shouldn't 🙈", "Build curiosity. Wait for reply.", "teasing"),
        ("TB-3", "ugh talking to you is making it so much worse... in the best way 💕", None, "teasing"),
        ("TB-4", "I want to show you something but I'm a little nervous... I don't usually do this", "WAIT 1-2 MIN. Build anticipation.", "wait"),
        ("TB-5", "okay here goes... be honest with me? 😊", "SEND PPV 0 — FREE teaser (sweet/natural selfie). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "you really liked that? because knowing you're looking at me like that is making me wet and I wasn't expecting that 💕", "Wait for reply.", "sext"),
        ("S1-2", "I keep running my hands down my body and everything is so sensitive... it's like every touch is amplified because of you", "React to compliment.", "sext"),
        ("S1-3", "my hand keeps sliding lower and I can't stop it babe... I don't even want to", None, "sext"),
        ("S1-4", "give me a moment 🙈", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "I want you to see what you're doing to me right now 😊", "SEND PPV 1 — $12. Bought → continue. Silent → NR Waves. 'I never/can't believe' — ONE TIME per journey.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "oh god... I can't believe I just did that 💕", "Wait for reply.", "sext"),
        ("S1-7", "but I can't stop now... my fingers are between my legs and it's all because of you", "HE caused this feeling.", "sext"),
        ("S1-8", "I'm so wet right now babe... you have no idea what your words do to my body 😊", None, "sext"),
        ("S1-9", "tell me what you want me to do to myself right now... I'll do anything you say", "Wait for reply. React to what he says.", "sext"),
        ("S1-10", "hold on... I need to show you what you're doing to me", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "look what you did to me... I couldn't stop 😊", "SEND PPV 2 — $25. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "fuck I'm so wet 💕", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I'm touching my pussy and imagining it's your hands on me... I need more", None, "sext"),
        ("S1-14", "my fingers keep going deeper and faster and my whole body is shaking 😊", None, "sext"),
        ("S1-15", "I'm about to cum and I need you to see what you did to me", None, "sext"),
        ("S1-16", "hold on a sec 🙈", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "this is what you made me do and you need to see every second of it 😊", "SEND PPV 3 — $40. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "oh fuck my pussy is throbbing so hard and my whole body won't stop shaking 💕", "Wait for reply.", "sext"),
        ("S1-19", "I can feel myself clenching around my fingers... I'm about to cum so hard babe please don't stop watching 😊", None, "sext"),
        ("S1-20", "I'm cumming babe... oh god I'm cumming right now and I can feel it dripping down my fingers", None, "sext"),
        ("S1-21", "one more second 💕", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "watch me cum... this is only for you 😊", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "wow... that was incredible 💕", None, "aftercare"),
        ("AC-2", "I've never done anything like that before and honestly I don't regret it at all. you made me feel so safe and so turned on at the same time. stay with me okay? 😊", "Build bond. Mention something specific he said. KEEP TALKING. NEVER say goodbye.", "aftercare"),
    ],

    # NO meetup_redirect (Instagram/TikTok traffic)

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "hey? 😊", "Send 2-3 min after PPV.", "sext"),
        ("NR-W2", "you seriously need to see what I just did... 💕", "3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "okay I guess you're busy... might delete this later, it was only for you", "5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hey hope you're good, text me when you're back 💕", "15-30 min later. Warm close.", "sext"),
        ("NR-W5", "can't stop thinking about earlier... you around? 😊", "2-6 hrs later. New topic if re-engage.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 26! finally feeling like I'm becoming the real me 😊", None),
        ("Location", "I'm in Houston right now, I love the food and the energy here 💕", "NEVER give specific neighborhood or address"),
        ("Profession", "I used to be a waitress but now I'm just enjoying life and figuring out what I really want", None),
        ("Hobbies", "I love going to the gym, cooking pasta carbonara is my thing, and I'm always down for a good adventure", None),
        ("Food", "pasta carbonara is literally my love language, I could eat it every single day and never get bored", None),
        ("Relationship", "single right now and honestly I'm just enjoying getting to know people and being free for once 😊", None),
        ("Languages", "Spanish is my first language! my English isn't perfect but I try my best haha 💕", None),
        ("Travel", "I've been to Mexico, Honduras, and Costa Rica so far. Costa Rica was amazing, the nature was unreal 😊", None),
        ("Personality", "I've always been the 'good girl' but honestly I'm tired of playing it safe, I wanna explore and have fun 💕", None),
        ("Gym", "I love the gym so much, it's my happy place honestly. nothing better than a good workout to clear my head ✨", None),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "honestly I love a guy who's mature, you just have this confidence that's so attractive 😊", None),
        ("Age20s", "oh nice we're around the same age! that's cool 💕", None),
        ("BoringJob", "that's really stable and honestly I find that really attractive, it shows discipline", None),
        ("CoolJob", "wait really?? that's so cool, tell me more about that 😊", None),
        ("Fit", "I love a guy who takes care of himself, I can tell you work hard 💕", None),
        ("NotFit", "I honestly don't care about that stuff at all, it's the connection that matters and yours is perfect", None),
        ("SameCity", "wait you're in Houston too?? no way that's so cool! 😊", None),
        ("FarAway", "aw that's far but honestly distance means nothing when the connection feels this real 💕", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "hey... I keep thinking about you. are you free? 💕", "Send 6-12 hrs after convo goes quiet.", "sext"),
        ("RE-2", "I did something really special and you're the only person I want to share it with... whenever you're ready 😊", "Next day. Seeds next session.", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS — 29 sheets
    # ═══════════════════════════════════════
    "obj_scripts": {},
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
