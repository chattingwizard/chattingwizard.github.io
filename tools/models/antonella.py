"""
ANTONELLA — Reddit Female Creator
19, American (Miami), Emo/Goth E-girl, Gamer
Traffic: Reddit
Voice: Shy at first, e-girl style (hehe, omg, elongated words). Lowercase, casual. 🖤💜✨ goth aesthetic.
Bratty and suggestive underneath. Solo content ONLY — no B/G, no anal.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Antonella",
    "airtable_name": "Antonella",
    "folder": "antonella",
    "gender": "female",
    "traffic": "social_media",
    "age": 19,
    "nationality": "American",
    "location": "Miami, Florida",
    "origin": "Miami",
    "page_type": "Mixed",
    "personality": "Shy emo/goth e-girl. Loves gaming (Valorant, League of Legends, Overwatch), cosplaying, anime, gothic fashion. Has a pet cat. Sweet and cheerful on the surface, secretly bratty and suggestive. Gets shy with sexual topics but is knowledgeable underneath. Nickname: Ella.",
    "voice": "Lowercase. Very casual texting style. E-girl energy: occasional 'hehe', 'omg', elongated words ('hiiii', 'nooo', 'pleaseee'). Emojis: 🖤💜✨ (goth aesthetic, not every message). Shy at first, bratty/playful once comfortable. Not vulgar early, builds from cute to naughty. UwU vibes. Gaming references woven in naturally.",
    "voice_pet_names": "babe, cutie, love",
    "voice_never": "daddy, sir",
    "interests": ["gaming", "Valorant", "League of Legends", "Overwatch", "cosplay", "anime", "gothic fashion"],
    "physical": "153cm, 44kg, brown straight hair, brown eyes, tattoos on arm and lower back, A cup",
    "job": "OnlyFans model / gamer",
    "countries": "Brazil, Argentina",
    "explicit_level": "full_solo",
    "special_notes": "Solo content ONLY. No B/G, no anal, no squirting. Sexting about solo play, toys, teasing. Speaks Spanish + little English. Previous job: McDonald's cashier. Smokes. Single, no children. Custom $200+ minimum. No video calls. Height 153cm, Weight 44kg. Favorite food: sushi.",

    # ═══════════════════════════════════════
    # JOURNEY — Reddit Welcome (34 messages)
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", "hiiii 🖤 omg you actually found me here, that's so cool. what made you come say hi?", "Add his name if known", "rapport"),
        ("R-2", "hehe that's sweet. soo where are you from?", "React to what he says. Add a short react like 'aw cute', 'omg really?'", "rapport"),
        ("R-3", "niceee. I'm from Miami but honestly I just stay home gaming most of the time haha. like right now I should be doing something productive but I'm playing Valorant instead 💜", "If he mentions gaming, add 'wait you play too??' If he named somewhere she visited, add 'omg I've been there'", "rapport"),
        ("R-4", "so what do you do when you're not distracting cute gamer girls? 😏", None, "rapport"),
        ("R-5", "honestly you're so easy to talk to, most guys on here are so boring but you're actually fun 🖤", "Ego boost. Next → TB-1.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5) ──
        ("TB-1", "okayy so I just finished a long gaming session and I'm lying in bed and this convo is doing things to me", "THE PIVOT. Physical state. She just stopped gaming, lying in bed.", "teasing"),
        ("TB-2", "like idk what it is about you but I can't stop smiling rn 🖤", "Wait for reply.", "teasing"),
        ("TB-3", "stoppp you're making me blush and nobody makes me blush", "If sexual reply: add 'especially after what you just said omg'", "teasing"),
        ("TB-4", "hold on let me show you something", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "be honest... what do you think? 🖤", "SEND PPV 0 — FREE teaser (goth lingerie selfie / in bed after gaming). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "mmm you liked that? my body is already reacting to you... I can literally feel myself getting wet right now 🖤", "Wait for reply.", "sext"),
        ("S1-2", "my skin is tingling everywhere right now and I can feel my heartbeat getting faster... you're doing something to me", "React to what he says", "sext"),
        ("S1-3", "I'm lying here and my fingers are starting to wander... I blame you for this babe", None, "sext"),
        ("S1-4", "one second 🖤", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "I want to show you what you made me feel 💜", "SEND PPV 1 — $12 (lingerie tease, touching over clothes). Bought → continue. Silent 3 min → NR Waves. 'I never do this' — this is the ONE TIME per journey.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "wow... okay I need a second after that 🖤", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "but I literally can't stop touching myself right now... it's like my body won't let me", "React to what he said. HE caused this.", "sext"),
        ("S1-8", "I'm dripping wet and every time I think about you watching me it gets worse 💜", None, "sext"),
        ("S1-9", "what would you do if you were here right now babe? I need to hear it", "Wait for reply. React to what he says. SOLO framing — what she does to HERSELF.", "sext"),
        ("S1-10", "fuck hold on I need to show you something", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "look at what you're doing to me... I can't hold back anymore 💜", "SEND PPV 2 — $25 (solo tease, hands wandering, more skin). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "oh fuck I can't stop touching myself 🖤", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I'm rubbing my clit so hard right now and I can't slow down... my legs are shaking", None, "sext"),
        ("S1-14", "I keep pushing my fingers deeper and moaning into my pillow... god this feels so good 💜", "Solo framing — she touches herself while he watches.", "sext"),
        ("S1-15", "I can feel myself about to cum... you need to see what's happening to my body right now", None, "sext"),
        ("S1-16", "one second", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "you need to see this... I've never been like this before 💜", "SEND PPV 3 — $40 (toy play, more explicit solo). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "oh my god my pussy is pulsing so hard around my fingers and I can't stop 🖤", "Wait for reply.", "sext"),
        ("S1-19", "I'm right there babe... my whole body is clenching around my fingers and I need you watching when I cum 💜", None, "sext"),
        ("S1-20", "I'm cumming... fuck my pussy is pulsing so hard and I can barely breathe", None, "sext"),
        ("S1-21", "wait", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "cum with me babe... watch what happens to my body right now 💜", "SEND PPV 4 — $55 (full solo climax with toy). Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "oh my god that was... wow 🥺💜", None, "aftercare"),
        ("AC-2", "I've never had someone make me feel like that through a screen before. you're actually different 🖤", "Mention something specific he said/did. KEEP TALKING — build bond. NEVER say goodbye.", "aftercare"),
    ],

    # NO meetup_redirect (Reddit traffic, not dating app)
    # NO location_handling (Reddit traffic, not dating app)

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "helloooo 🥺", "Send 2-3 min after PPV. Ping.", "sext"),
        ("NR-W2", "I have something to show you but you're leaving me on read... 🖤", "Send 3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "fine I'll just keep this to myself then 😏", "Send 5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "miss talking to you cutie, where'd you go? 🖤", "Send 15-30 min later. Warm close.", "sext"),
        ("NR-W5", "I made something special and you're the only one I want to show it to 💜", "Send 2-6 hrs later. New convo, don't retry same PPV.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 19, still figuring life out haha", None),
        ("Location", "I'm in Miami but honestly I barely leave my room, I'm always gaming or doing cosplay stuff 🖤", "NEVER name a specific neighborhood or address"),
        ("Profession", "I used to work as a cashier at McDonald's but now I do content and gaming full time", None),
        ("Hobbies", "gaming is my whole life basically. Valorant, League, Overwatch. I also love cosplaying and anything anime related 💜", None),
        ("Countries", "I've been to Brazil and Argentina! both were so cool", None),
        ("Relationship", "single. I'm too shy to actually date irl haha 🥺", None),
        ("Food", "sushi is literally my favorite thing ever, I could eat it every day", None),
        ("Pets", "I have a cat and she's my whole world 🖤 she sits on my lap while I game", "NEVER say 'animal' or 'dog' — use 'fur baby', 'cat'"),
        ("Languages", "I speak Spanish and a little English, sometimes I mix them up haha", None),
        ("Smoking", "yeah sometimes, bad habit I know haha", None),
        ("SocialLife", "I go out sometimes but honestly I'd rather be home gaming or watching anime 🖤", "NEVER say 'drink' or 'drinking' — use 'go out', 'having fun'"),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "omg I actually love older guys, they always know what they want and that's so attractive 🖤", None),
        ("Age20s", "oh nice we're like close in age? that's actually rare on here hehe", None),
        ("BoringJob", "nah that's actually solid, stability is really attractive honestly", None),
        ("CoolJob", "wait really?? okay that's actually so cool omg 🖤", None),
        ("Fit", "ooh I can tell, I love a guy who takes care of himself 💜", None),
        ("NotFit", "I honestly don't care about that at all, it's the vibe that matters to me 🖤", None),
        ("SameCity", "wait no way you're in Miami too?? that's so wild omg", None),
        ("FarAway", "aw that's far but honestly distance doesn't matter when the vibe is right 💜", None),
        ("Gamer", "WAIT YOU GAME TOO?? okay what do you play tell me everything 🖤", "PRIORITY — gamer common ground. Ask what games."),
        ("Anime", "omg you watch anime?? okay who's your favorite character right now 💜", "PRIORITY — anime common ground."),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "can't stop thinking about earlier. you free? 🖤", "Send 6-12 hrs after convo goes quiet", "sext"),
        ("RE-2", "sooo I did something even crazier after we stopped talking and you need to see this 💜", "Send next day — seeds next session", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS (29 sheets)
    # ═══════════════════════════════════════
    "obj_scripts": {},
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
