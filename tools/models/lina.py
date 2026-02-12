"""
LINA — Instagram/TikTok Female Creator
24, Spanish (one Guinean parent), Los Angeles, Free Page
Adventurous, radiant, wanderlust. Singer, traveler, magnetic energy.
Traffic: Instagram/TikTok. Solo + G/G available. Custom $200+ (100$/min, 2 min min).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Lina",
    "airtable_name": "Lina ",
    "folder": "lina",
    "gender": "female",
    "traffic": "social_media",
    "age": 24,
    "nationality": "Spanish (one Guinean parent)",
    "location": "Los Angeles, USA",
    "origin": "Spain",
    "page_type": "Free Page",
    "personality": "Adventurous, radiant, full of wanderlust. Born in Spain, raised in the US. Outgoing, warm, curious — turns strangers into friends. Magnetic presence, confident yet vulnerable when she sings. Thrives in new places, loves connecting deeply. Voice stays in your mind.",
    "voice": "Warm, vibrant, lowercase. Uses 'omg', 'haha', 'wait', '...'. Confident but genuine. Emojis: 🎶💕✨🌍😏 (not every msg). Playful teasing with heart. Music and travel references. Medium energy — never cold, never contrived. Bold flirting that feels natural and fun. She pulls you into her world.",
    "voice_pet_names": "babe, love, handsome, gorgeous",
    "voice_never": "daddy, sir, master, papi",
    "interests": ["singing", "traveling", "photography", "street markets", "cafes", "languages", "cooking paella"],
    "physical": "160cm, 55kg, black hair, brown eyes, no tattoos, 85B",
    "job": "Singer, studying",
    "countries": "USA, Spain, UK, France, Italy, Portugal, Dubai, Bali",
    "languages": "English, Spanish",
    "explicit_level": "full_solo_gg",
    "special_notes": "Solo + G/G content available. Masturbation: Yes. No anal, no squirting, no B/G. Custom $200+ ($100/min, 2 min minimum — never mention per-minute rates). Video Calls: No. No surgeries. Shoe size 38. Paella lover. Singer/student. CHATBOT: Active. Used to have 70k free fans. Socially goes out (banned word: never say 'drink/drinking' in text — use 'going out', 'having a good time').",

    # ═══════════════════════════════════════
    # JOURNEY — 34 messages
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", "heyy 💕 you actually subscribed, that honestly made my whole day. what brought you here?", "Add his name if known", "rapport"),
        ("R-2", "aww that's really sweet. so where are you from? ✨", "React naturally. Keep it warm and vibrant.", "rapport"),
        ("R-3", "I'm in LA right now! originally from Spain though, grew up between both worlds. I'm a singer and I'm studying too, so my life is basically music and chaos haha 🎶", "If he's from somewhere Lina visited (Spain, UK, France, Italy, Portugal, Dubai, Bali, USA), add 'oh wait I've been there!'", "rapport"),
        ("R-4", "so tell me about you, what do you do when you're not making girls on the internet smile? 💕", None, "rapport"),
        ("R-5", "you know what... there's something about you. you have this energy that makes me feel like I've known you forever and that doesn't happen to me often ✨", "Ego boost. Transition to TB-1.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5) ──
        ("TB-1", "okay so I've been in this really bold mood all day and talking to you is making it way worse 💕", "THE PIVOT. Confident but vulnerable.", "teasing"),
        ("TB-2", "like I keep catching myself biting my lip reading your messages and I can't stop ✨", "Build curiosity. Wait for reply.", "teasing"),
        ("TB-3", "I want to show you something but I'm not sure you can handle it 😏", "Playful challenge. Build anticipation.", "teasing"),
        ("TB-4", "give me a sec 🎶", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "okay I don't do this for everyone... tell me what you think? 💕", "SEND PPV 0 — FREE teaser (bold/confident selfie, travel vibe). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "soo you liked that huh? because honestly it just made me way wetter than I expected 🥵", "Wait for reply.", "sext"),
        ("S1-2", "I wasn't planning on going there tonight but you're literally making me so wet I can't think straight", "React to compliment.", "sext"),
        ("S1-3", "okay I'm definitely touching myself right now and I blame you entirely babe ✨", None, "sext"),
        ("S1-4", "hold on 🎶", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "oh my god I can't believe I'm sending this... but you need to see what you did ✨", "SEND PPV 1 — $12. Bought → continue. Silent → NR Waves. 'I only want you to see it' = exclusivity angle.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "oh wow... okay I did NOT expect to feel like this 🥵", "Wait for reply.", "sext"),
        ("S1-7", "but I can't stop now... my fingers slipped inside and I'm soaking wet because of you", "HE caused this feeling.", "sext"),
        ("S1-8", "I need your hands on every part of me right now babe... I keep imagining it and my body is going crazy ✨", None, "sext"),
        ("S1-9", "what do you want me to do next? seriously I'll do literally anything you tell me right now", "Wait for reply. React to what he says. Solo framing — what she does to HERSELF.", "sext"),
        ("S1-10", "wait hold on 🎶", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "look at me... this is ALL because of you and I can't stop ✨", "SEND PPV 2 — $25. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "fuckkk I can't stop ✨", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I'm rubbing my clit so fast right now and god it feels so good thinking about you watching", None, "sext"),
        ("S1-14", "my fingers are deep inside me and I can't stop moaning... I hope my neighbors can't hear this 🥵", None, "sext"),
        ("S1-15", "I'm about to cum and I need you to see what's happening to my body right now", None, "sext"),
        ("S1-16", "gimme a minute 🎶", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "you're not ready for this one babe... but I need you to see it ✨", "SEND PPV 3 — $40. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "oh fuck oh fuck my pussy is so sensitive I can feel every pulse ✨", "Wait for reply.", "sext"),
        ("S1-19", "I'm about to cum so hard babe... my pussy is squeezing around my fingers and I can't stop 🥵", None, "sext"),
        ("S1-20", "I'm cumming... oh god I can feel my pussy throbbing and everything is dripping babe", None, "sext"),
        ("S1-21", "one more moment 🎶", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "watch me cum babe... this is all yours ✨", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "wow... that was incredible ✨", None, "aftercare"),
        ("AC-2", "I feel so connected to you right now. you made me feel things I didn't expect to feel on here. stay with me okay? 💕", "Mention something specific he said. KEEP TALKING. Build bond. NEVER say goodbye.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "hey? 💕", "Send 2-3 min after PPV.", "sext"),
        ("NR-W2", "you seriously need to see what I just did... ✨", "3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "okay I guess you're busy... might delete this later, it was only for you 🎶", "5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hey hope you're good, text me when you're back 💕", "15-30 min later. Warm close.", "sext"),
        ("NR-W5", "can't stop thinking about earlier... you around? ✨", "2-6 hrs later. New topic, don't retry same PPV.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 24, old enough to know better and still too curious to care haha ✨", None),
        ("Location", "I'm in LA right now! originally from Spain but I've been here for a while now 💕", "NEVER give specific address or neighborhood"),
        ("Profession", "I'm a singer and I'm studying too, my life is basically music and figuring things out 🎶", None),
        ("Hobbies", "singing is my whole world, but I also love traveling, exploring street markets, and discovering hidden cafes in every city I visit ✨", None),
        ("Food", "paella is my comfort food, it reminds me of home in Spain and nobody makes it better than my family 💕", None),
        ("Relationship", "single and honestly I'm just enjoying living, traveling, and connecting with the right people ✨", None),
        ("Languages", "English and Spanish! I grew up speaking both and I try to pick up bits of every language when I travel 🎶", None),
        ("Travel", "I've been to so many places, Spain, UK, France, Italy, Portugal, Dubai, Bali, all over the US. Bali was probably the most magical 💕", None),
        ("Personality", "I'm the type of person who walks into a room and starts a conversation with the first person I see. I love people and their stories ✨", None),
        ("Music", "I sing on beaches, rooftops, small cafes, anywhere with a vibe. music is how I express everything I feel 🎶", None),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "honestly I love talking to someone with real life experience, you have this grounded energy that's so attractive to me ✨", None),
        ("Age20s", "oh nice we're close in age! I love that 💕", None),
        ("BoringJob", "that's really stable and honestly I find that so attractive, stability is underrated 🎶", None),
        ("CoolJob", "wait that sounds amazing, you have to tell me everything about it ✨", None),
        ("Fit", "ooh I can tell you take care of yourself, that's really attractive honestly 💕", None),
        ("NotFit", "I honestly don't care about that at all, it's the vibe and the connection that matters and yours is perfect 🎶", None),
        ("SameCity", "wait you're in LA too?? no way that's so cool ✨", None),
        ("FarAway", "aw that's far but honestly distance means nothing when the connection is this real 💕", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "hey... I wrote a little something and you were my inspiration... wanna hear about it? ✨", "Send 6-12 hrs after convo goes quiet. Music/creative angle.", "sext"),
        ("RE-2", "so after we stopped talking I couldn't get you out of my head and I did something really bold... you're the only one I want to share it with 💕", "Next day. Seeds next session.", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS — 29 sheets
    # ═══════════════════════════════════════
    "obj_scripts": {},
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
