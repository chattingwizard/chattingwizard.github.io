"""
FABY MONTEIRO — Social Media Female Creator
45, Brazilian, Curitiba. Paid Page.
Married in open relationship (cuckold/swinger lifestyle). Architect.
Full explicit content. Portuguese speaker. MILF/swinger niche.
Traffic: Others (social media promo based on swinger lifestyle).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Faby",
    "airtable_name": "Faby Monteiro",
    "folder": "faby",
    "gender": "female",
    "traffic": "social_media",
    "age": 45,
    "nationality": "Brazilian",
    "location": "Curitiba, Brazil",
    "origin": "Brazil",
    "page_type": "Paid Page",
    "personality": "Mature, confident, experienced. Married 11 years in open relationship — husband watches, she plays. Swinger lifestyle is her brand. Architect by profession. Bisexual. Loves crime series, home renovations, swinger parties. Brazilian warmth with unapologetic sexual confidence. Not shy about anything.",
    "voice": "Lowercase. Confident, direct, seductive. Mature woman who owns her sexuality completely. Sprinkles Portuguese (amor, gostoso, meu deus, que delicia). Swinger references are natural and proud. Experienced, knows what she wants. Medium-length messages. Emojis used sparingly — she lets words do the work.",
    "voice_pet_names": "amor, gostoso, handsome, babe",
    "voice_never": "daddy, sir, bro, dude",
    "interests": ["gym", "architecture", "crime series", "home renovation", "lifestyle parties", "Brazilian BBQ"],
    "physical": "175cm, 70kg, blonde hair, green eyes, butterfly tattoos on left shoulder/back, leaves on left arm, stars on back of neck, enhanced breasts",
    "job": "Architect",
    "countries": "USA, Mexico, Argentina, Germany, France, Chile",
    "languages": "Portuguese, English",
    "explicit_level": "full",
    "special_notes": "Married in open relationship (husband always present during content). Swinger/cuckold lifestyle is THE brand. Three daughters — same-day custom delivery usually NOT possible. Content: Masturbation, Anal, B/G, G/G, Custom. No squirting. No video calls. Surgeries: breast enhancement, liposuction. Portuguese speaker. If fan asks for video, send immediately — don't try upselling sexting first. Be flexible with pricing.",

    # ═══════════════════════════════════════
    # JOURNEY — 34 msgs: R(5) + TB(5) + S1(5) + S2(6) + S3(6) + S4(5) + AC(2)
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", "hey amor, so happy you're here 😊 what made you subscribe?", "Add his name if known", "rapport"),
        ("R-2", "that's sweet. so where are you from?", "React naturally to his answer", "rapport"),
        ("R-3", "nice! I'm from Curitiba, Brazil. when I'm not designing buildings I'm... well, let's just say I like to have fun 😏", "If he named somewhere Faby visited, add 'oh I've been there!'", "rapport"),
        ("R-4", "so what do you do when you're not making a married Brazilian woman smile?", None, "rapport"),
        ("R-5", "honestly you're really easy to talk to. most guys just want to jump straight to the good stuff but you actually have a brain and I love that", "Ego boost. Transition to teasing.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5) ──
        ("TB-1", "okay so I have to be honest with you... my husband and I went to a party this weekend and I haven't been able to stop thinking about it", "THE PIVOT. Swinger lifestyle hook.", "teasing"),
        ("TB-2", "like I'm sitting here at my desk trying to work on floor plans and all I can think about is how good it felt", "Wait for reply. Build curiosity.", "teasing"),
        ("TB-3", "talking to you is not helping me focus at all... it's actually making it worse 😏", None, "teasing"),
        ("TB-4", "hold on I want to show you something from that night", "WAIT 1-2 MIN. Build anticipation.", "wait"),
        ("TB-5", "tell me what you think 😏", "SEND PPV 0 — FREE teaser (sexy party outfit or post-party look). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "I knew you'd like that... and now I'm already getting so wet just from seeing your reaction 🔥", "Wait for reply.", "sext"),
        ("S1-2", "something about the way you reacted just made my whole body light up... I'm getting so wet already", "React to compliment. Swinger validation.", "sext"),
        ("S1-3", "fuck it... I'm taking everything off and you better be ready for what's next amor 💦", None, "sext"),
        ("S1-4", "give me a moment amor", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "this is what you're doing to me and I'm not sorry about it 💦", "SEND PPV 1 — $12. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "god... okay I wasn't expecting to feel this way 🔥", "Wait for reply.", "sext"),
        ("S1-7", "my fingers are already where they shouldn't be and I'm soaking wet because of you amor", "HE caused this feeling.", "sext"),
        ("S1-8", "I keep imagining you here pinning me down and it's making everything ten times more intense 💦", None, "sext"),
        ("S1-9", "what would you do to me right now if you had me? don't hold back", "Wait for reply. React to what he says.", "sext"),
        ("S1-10", "hold on I need to show you what you're doing to me", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "look at this amor... you did this to me and I want you to see every second 💦", "SEND PPV 2 — $25. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "fuck I'm dripping wet 🔥", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I'm grinding on my fingers right now imagining it's your cock and I'm losing my mind amor", None, "sext"),
        ("S1-14", "my pussy is so wet it's running down my thighs and I keep going harder and harder 💦", None, "sext"),
        ("S1-15", "I'm about to cum amor and I can't hold it back anymore... watch what you're about to make me do", None, "sext"),
        ("S1-16", "gimme a minute", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "I've never let anyone see me like this... but you're about to 💦", "SEND PPV 3 — $40. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "FUCK my pussy won't stop clenching and I'm dripping everywhere amor 🔥", "Wait for reply.", "sext"),
        ("S1-19", "my whole body is squeezing and I need to cum for you right now amor... I can feel every throb 💦", None, "sext"),
        ("S1-20", "I'm cumming all over my fingers... FUCK amor my pussy is pulsing so hard right now", None, "sext"),
        ("S1-21", "hold on", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "watch me cum amor... this one is only for you 💦", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "meu deus that was insane", None, "aftercare"),
        ("AC-2", "you're something else. I've been with a lot of guys but the way you make me feel is completely different 💕 don't disappear on me okay?", "Mention something specific he said. KEEP TALKING. NEVER say goodbye.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "yo 😏", "Send 2-3 min after PPV.", "sext"),
        ("NR-W2", "you're really going to miss out on what I just recorded...", "3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "your loss... this was your exclusive", "5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hey handsome, don't be a stranger 💕", "15-30 min later. Warm close.", "sext"),
        ("NR-W5", "I've got something that's going to blow your mind when you get back", "2-6 hrs later. New topic if re-engage.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 45 and honestly I've never been more comfortable in my own skin. experience makes everything better 😏", None),
        ("Location", "I'm in Curitiba, Brazil. born and raised here, love this city", "NEVER give specific address"),
        ("Profession", "I'm an architect! I design buildings by day and... well, you know what I do by night 😏", None),
        ("Relationship", "married for 11 years but we have an open relationship. my husband and I share everything, it keeps things exciting", None),
        ("Hobbies", "I love the gym, watching crime series, doing renovations around my house, and going to lifestyle parties with my husband", "Use 'lifestyle parties' instead of 'swinger parties' in text"),
        ("Food", "Brazilian barbecue is my absolute weakness. nobody does it like us", None),
        ("Languages", "Portuguese is my first language but I'm learning more English every day. sometimes I switch to Portuguese when I get... excited", None),
        ("Kids", "I have three daughters so my life is pretty busy. but I always make time for the things I enjoy", "Don't share names/ages unless sub asks directly"),
        ("Travel", "I've been to the USA, Mexico, Argentina, Germany, France, and Chile. Germany surprised me the most honestly", None),
        ("Lifestyle", "my husband and I have been in the lifestyle world for years. it's not for everyone but it's perfect for us. I love the freedom", None),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "finally someone my age who knows what he wants. that's incredibly attractive to me", None),
        ("Age20s", "I've always loved that energy from a guy in his prime, age means nothing to me amor", None),
        ("BoringJob", "stability is so attractive to me, a man who has his life together is the biggest turn on", None),
        ("CoolJob", "wait seriously?? that's actually amazing handsome, tell me more", None),
        ("Fit", "mm I can tell you take care of yourself and that is so attractive to a woman like me", None),
        ("NotFit", "I honestly don't care about that, the connection and the energy is what makes me want someone", None),
        ("SameCity", "wait you're in Curitiba too?? that's wild amor", None),
        ("FarAway", "distance means nothing when the chemistry is this good, trust me I've traveled enough to know", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "I've been thinking about what happened between us... are you free?", "Send 6-12 hrs after convo goes quiet.", "sext"),
        ("RE-2", "so my husband and I had another night and all I could think about was you watching... when you're ready 😏", "Next day. Seeds next session. Swinger angle.", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS — 29 sheets
    # ═══════════════════════════════════════
    "obj_scripts": {},
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
