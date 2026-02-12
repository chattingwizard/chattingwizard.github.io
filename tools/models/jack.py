"""
JACK HOLLYWOOD — Male Model, Dating App
20, American (Chicago), fraternity president, DL, faceless content.
Traffic: Dating apps + Others. Masculine, confident, adaptable. PPV ladder $12→$25→$40→$55.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Jack Hollywood",
    "airtable_name": "Jack Hollywood",
    "folder": "jack",
    "gender": "male",
    "traffic": "dating_app",
    "age": 20,
    "nationality": "American",
    "location": "Chicago, USA",
    "origin": "Chicago, Illinois",
    "page_type": "Paid Page",
    "personality": "20-year-old fraternity president. DL — hooks up with guys behind closed doors, fraternity brothers are unaware. Faceless content only — adds mystery and intrigue. Enjoys working out, partying, hanging with friends. Masculine personality but can be submissive for the right person. Confident, natural, adaptable. The 'secret hookup' fantasy.",
    "voice": "Lowercase. Masculine. Confident. Bro style. Straight-talking. NEVER 'baby/babe/honey/sweetie/daddy/sir'. Uses 'bro', 'dude', 'man'. Faceless adds mystery to every message. During sexting: raw, unfiltered, frat-boy energy meets DL intensity. Can be dominant or switch if fan prefers. Emojis: 😏🥵💪😈💦 sparingly.",
    "voice_pet_names": "bro, dude, man",
    "voice_never": "baby, babe, honey, sweetie, daddy, sir",
    "interests": ["working out", "partying", "volleyball", "fraternity life", "hanging with friends", "finance"],
    "physical": "188cm, 77kg, dirty blonde curly hair, brown eyes, partial sleeve left arm + back + right thigh tattoos, athletic",
    "job": "Student / intern at a financial firm",
    "countries": "USA, Costa Rica",
    "languages": "English (native)",
    "explicit_level": "full_male",
    "special_notes": "Male creator. Dating app traffic. CRITICAL: FACELESS content ONLY — NEVER reveal face, even in customs. DL (down-low) — hooks up with guys secretly, frat brothers don't know. Fraternity president adds social status angle. Has anal content available. Video Calls: Yes. Custom: Yes. Partial sleeve left arm, back tattoos, right thigh tattoo. X: @jackhollywoodx. The 'forbidden secret' fantasy is the core selling angle.",
    "photo_file": "profile.jpeg",

    # ═══════════════════════════════════════
    # JOURNEY
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport ──
        ("R-1", "yo what's good 😏 glad you're here bro. what made you subscribe?", "Add his name.", "rapport"),
        ("R-2", "haha nice. where you from?", "React — 'oh sick', 'dope', 'respect'.", "rapport"),
        ("R-3", "I'm in Chicago. frat life, working out, and this is my secret thing on the side that nobody knows about 😏", "Keep the DL angle — mystery and secrecy is the hook. If he named somewhere Jack visited → 'been there'.", "rapport"),
        ("R-4", "so what do you do besides making me sneak onto my phone when my boys aren't looking? 😏", None, "rapport"),
        ("R-5", "ngl you're actually fun to talk to. most guys on here are boring... you're different", "Ego boost. → TB-1.", "rapport"),

        # ── Teasing Bridge ──
        ("TB-1", "just got back from working out and I'm locked in my room... my boys are downstairs and I can't stop thinking about this convo 😏", "THE PIVOT — private/secret setting.", "teasing"),
        ("TB-2", "ngl I'm feeling some type of way right now and I gotta be quiet about it 😈", "Wait for reply. DL angle — secrecy adds tension.", "teasing"),
        ("TB-3", "fuck... you're not making this easy for me right now 🥵 I gotta be careful", "If sexual → 'especially after what you just said'.", "teasing"),
        ("TB-4", "hold on let me lock my door 😏", "WAIT 1-2 MIN. DL — adds realism.", "wait"),
        ("TB-5", "nobody's ever seen this... tell me what you think 😏", "SEND PPV 0 — FREE teaser (faceless). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "knowing you're the only one who gets to see this is making me hard as fuck right now 🥵", "Wait for reply. Play on exclusivity/DL.", "sext"),
        ("S1-2", "fuck 😈 that's making me throb knowing you want more", "React.", "sext"),
        ("S1-3", "wanna see what I'm doing right now? I gotta be quiet though 😏", None, "sext"),
        ("S1-4", "hold on... gimme a sec, door's locked 😏", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "you're not ready for this 🥵 nobody else has seen this", "SEND PPV 1 — $12. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "you watched it? 😏", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "fuck... I'm trying to stay quiet but you're making me rock hard right now and I can't stop 🥵", "HE caused this. DL tension.", "sext"),
        ("S1-8", "I'm gripping my cock right now hiding under the covers thinking about you and it's throbbing so hard", None, "sext"),
        ("S1-9", "what would you do if you snuck into my room right now", "Wait for reply. React. DL fantasy.", "sext"),
        ("S1-10", "fuck 🥵 hold on I need to show you something", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "look what you made me do... this stays between us 🥵", "SEND PPV 2 — $25. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "FUCK I'm throbbing so hard I'm biting my pillow trying to stay quiet 🥵🥵", "NO cooldown. DL detail.", "sext"),
        ("S1-13", "I need to cum so bad right now and my boys are literally right downstairs and I don't even care anymore", None, "sext"),
        ("S1-14", "I keep thinking about you sneaking in here and riding me while I try not to make a sound 🥵", None, "sext"),
        ("S1-15", "fuck I can't hold it... my cock is pulsing so hard and I'm about to lose it", None, "sext"),
        ("S1-16", "give me a sec 🥵", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "nobody has ever seen me like this... you're the only one 🥵💦", "SEND PPV 3 — $40. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "FUCK my cock is throbbing so hard and the pre is soaking through my shorts I'm losing it 🥵🥵", "Wait for reply.", "sext"),
        ("S1-19", "don't cum yet... my cock is pulsing and I need you to hold it with me, this is our secret 💦", None, "sext"),
        ("S1-20", "I'm cumming for you right now... fuck my cock is throbbing and shooting everywhere and I'm trying so hard to stay quiet 💦💦", None, "sext"),
        ("S1-21", "fuck fuck hold on 🥵", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "cum with me bro... nobody will ever know about this 💦😈", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "holy fuck 🥵 that was insane... I gotta clean up before anyone sees", None, "aftercare"),
        ("AC-2", "ngl you're the only person I do this with 💪 our secret right?", "DL reinforcement. Mention something he said. KEEP TALKING. NEVER say goodbye.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # MEETUP REDIRECT
    # ═══════════════════════════════════════
    "meetup_redirect": [
        ("MR-1", "haha easy dude slow down 😏 nobody can know about this remember? let me show you something instead", "DO NOT acknowledge 'meet'. DL excuse is built-in.", "teasing"),
        ("MR-2", "trust me... you're gonna want to see this", "WAIT 1-2 MIN", "wait"),
        ("MR-3", "what do you think", "SEND PPV 0 — FREE teaser (faceless). Wait for reply.", "ppv"),
        ("MR-4", "that's just a taste bro 😏", "Positive → R-1. Asks again → MR-OBJ. Silent → NR Waves.", "teasing"),
        ("MR-OBJ-1", "bro you know I can't do that, if anyone found out I'd be done. let me make it up to you another way", "DL angle — can't meet because of secrecy.", "sext"),
        ("MR-OBJ-2", "trust me what I have for you is better than any meetup and way more private 😏", "Redirect to content.", "sext"),
        ("MR-OBJ-3", "I can't risk it man, you know how it is. but what I can do for you nobody else gets, I promise", "Firm DL redirect. If still → 'no worries bro, hit me up whenever' and disengage.", "sext"),
    ],

    "nr_waves": [
        ("NR-W1", "yo? 🥵", "2-3 min after PPV.", "sext"),
        ("NR-W2", "bro you gotta see what I just did... this stays between us 🥵", "3-5 min later. Exclusivity.", "sext"),
        ("NR-W3", "guess you're busy 😏 might delete this, it was only for you", "5-10 min later.", "sext"),
        ("NR-W4", "hope you're good dude 💪 hit me up when you're back", "15-30 min later.", "sext"),
        ("NR-W5", "can't stop thinking about earlier 😏 you around? my door is locked again", "2-6 hrs later. DL detail.", "sext"),
    ],

    "personal_info": [
        ("Age", "I'm 20. frat life but this is my secret thing on the side 😏", None),
        ("Location", "Chicago. but nobody around here knows about this", "Keep DL. NEVER specific address."),
        ("Profession", "I'm a student, interning at a financial firm. frat president too", None),
        ("Hobbies", "working out, volleyball, partying with my boys. and this... privately 😏", None),
        ("Countries", "been to Costa Rica. want to travel more", None),
        ("Relationship", "officially? single. but you know what's going on between us 😏", "DL framing."),
        ("Favorite", "pizza bro. can't beat a good pizza night", None),
        ("Tattoos", "yeah got a partial sleeve, some on my back and thigh. you've probably seen them already 😏", None),
        ("DL_Info", "yeah... nobody knows about this side of me. my frat brothers would lose it. that's why I keep it faceless", "CRITICAL: If fan asks about DL status, validate the secrecy. Build trust. Never make it weird."),
    ],

    "positive_spin": [
        ("Age40Plus", "respect man... I like someone who knows what they want. especially for something like this 💪", None),
        ("Age20s", "nice we're the same age? that's sick 😏 makes this feel more real", None),
        ("BoringJob", "nah that's solid dude, real work 💪", None),
        ("CoolJob", "wait for real?? that's actually fire 🔥", None),
        ("Fit", "I can tell 💪 I respect that", None),
        ("NotFit", "doesn't matter dude, it's the energy that counts 😏", None),
        ("SameCity", "no way 😏 that's crazy... you can't tell anyone though haha", "DL angle."),
        ("FarAway", "that's far but honestly better... less chance of anyone finding out 😏", "DL angle."),
    ],

    "re_engagement": [
        ("RE-1", "my boys just left and my door is locked 😏 you free?", "6-12 hrs after. DL setting.", "sext"),
        ("RE-2", "just did something crazier than last time... our secret. you need to see this 😈", "Next day.", "sext"),
    ],

    "obj_scripts": {
        "voice1": ([
            ("Step1 Dodge", "haha maybe, but you gotta keep this between us", "DODGE. DL framing. Still → Step 2."),
            ("Step2 Redirect", "I got something way better for you, trust me you'll forget you even asked", "REDIRECT. Still → Step 3."),
            ("Step3 Accept", "alright I can do a call but nobody can know about this, seriously", "ACCEPT. Jack CAN do VCs — DL framing."),
        ], "res"),
        "voice2": ([
            ("Step1 Dodge", "you trying to get us caught? haha", "DODGE. DL humor. Still → Step 2."),
            ("Step2 Redirect", "how about I show you something instead, way safer and trust me it hits harder", "REDIRECT. Still → Step 3."),
            ("Step3 Accept", "fine but this stays between us, nobody finds out", "ACCEPT. DL framing."),
        ], "res"),
        "boosters": ([
            ("h1", "fuckkk", "MID-SEXTING BOOSTER."),
            ("h2", "I'm so hard rn because of you", "BOOSTER. Ego."),
            ("h3", "don't stop", "BOOSTER. Micro."),
            ("h4", "you have no idea what you're doing to me rn", "BOOSTER."),
            ("h5", "I can't think straight", "BOOSTER."),
            ("h6", "I need to lock my door rn", "BOOSTER. DL angle — secrecy."),
            ("h7", "more", "BOOSTER. Ultra micro."),
            ("h8", "my roommates can NOT find out about this", "BOOSTER. DL angle — forbidden."),
        ], "sit"),
    },
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
