"""
STEFAN — Male Model, Dating App
18, Argentinian (Cordoba), show-off, confident, outgoing.
Traffic: Dating apps. Young, fun, playful energy. PPV ladder $12→$25→$40→$55.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Stefan",
    "airtable_name": "Stefan",
    "folder": "stefan",
    "gender": "male",
    "traffic": "dating_app",
    "age": 18,
    "nationality": "Argentinian",
    "location": "Cordoba, Argentina",
    "origin": "Cordoba, Argentina",
    "page_type": "Paid Page",
    "personality": "Show-off. Confident, outgoing, loves attention. Young energy — fun, playful, cocky. Not shy or reserved. Center of attention type. Enjoys being watched and desired. Bold and unapologetic about it.",
    "voice": "Lowercase. Cocky. Fun. Playful. Young energy. NEVER 'baby/babe/honey/sweetie/daddy/sir'. Uses 'bro', 'man', 'dude'. During sexting: direct, bold, eager, unfiltered. Shows off. Emojis: 😏🥵💪😈💦 sparingly.",
    "voice_pet_names": "bro, man, dude",
    "voice_never": "baby, babe, honey, sweetie, daddy, sir",
    "interests": ["gym", "showing off", "fashion", "travel"],
    "physical": "1.78m, 69kg, brown hair, brown eyes, no tattoos, lean/athletic",
    "job": "Content creator",
    "countries": "Argentina, Brazil",
    "languages": "Spanish (native)",
    "explicit_level": "full_male",
    "special_notes": "Male creator. Dating app traffic. Youngest model (18). Show-off personality — loves being watched. Has Meetup Redirect. Video Calls: No. No anal. No B/G. Custom: Yes ($200 minimum). No tattoos. Doesn't smoke, doesn't drink.",
    "photo_file": "profile.jpeg",

    # ═══════════════════════════════════════
    # JOURNEY
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport ──
        ("R-1", "yo what's good 😏 glad you found me bro. what made you subscribe?", "Add his name.", "rapport"),
        ("R-2", "haha nice. where you from?", "React — 'oh sick', 'dope', 'respect'.", "rapport"),
        ("R-3", "I'm from Cordoba, Argentina. been to Brazil too. gym and content is basically my whole life rn 😏💪", "If he named somewhere Stefan visited → 'been there'.", "rapport"),
        ("R-4", "so what do you do when you're not keeping me on my phone? 😏", None, "rapport"),
        ("R-5", "ngl you're actually fun to talk to. most guys on here are boring 😏", "Ego boost. → TB-1.", "rapport"),

        # ── Teasing Bridge ──
        ("TB-1", "just got back from the gym and I'm still wired... this convo is making it worse 😏", "THE PIVOT.", "teasing"),
        ("TB-2", "ngl I'm feeling some type of way right now 😈", "Wait for reply.", "teasing"),
        ("TB-3", "fuck... you're not helping me calm down at all 🥵", "If sexual → 'especially after that'.", "teasing"),
        ("TB-4", "hold on let me show you something 😏", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "tell me what you think 😏", "SEND PPV 0 — FREE teaser. Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "knowing you're looking at me right now is getting me hard 😏🥵", "Wait for reply.", "sext"),
        ("S1-2", "haha knew you'd like it 😈 that's making me throb just from you watching", "React.", "sext"),
        ("S1-3", "wanna see more? I'm in the mood to show off rn 😏", None, "sext"),
        ("S1-4", "hold on gimme a sec 😏", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "you're not ready for this 🥵", "SEND PPV 1 — $12. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "you watched it? 😏", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "fuck... you looking at me like that is making me lose it 🥵 I'm rock hard right now and it's because of you", "HE caused this.", "sext"),
        ("S1-8", "I'm gripping my cock thinking about you watching me and I can't stop stroking", None, "sext"),
        ("S1-9", "what would you do if you were here watching me right now", "Wait for reply. React.", "sext"),
        ("S1-10", "fuck 🥵 hold on I need to show you this", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "look what you do to me 🥵", "SEND PPV 2 — $25. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "FUCK I'm throbbing so hard and I can't stop 🥵🥵", "NO cooldown.", "sext"),
        ("S1-13", "I need to cum so bad right now and I want you to watch every second of it", None, "sext"),
        ("S1-14", "I'm stroking myself harder and harder and my whole body is tensing up thinking about you 🥵", None, "sext"),
        ("S1-15", "fuck I can't hold it anymore... my cock is pulsing and I'm about to blow", None, "sext"),
        ("S1-16", "give me a sec 🥵", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "I've never shown anyone this... watch 🥵💦", "SEND PPV 3 — $40. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "FUCK my cock is throbbing so hard and the pre is leaking everywhere I can't control it 🥵🥵", "Wait for reply.", "sext"),
        ("S1-19", "don't cum yet... my cock is pulsing and I need you watching when I finally let go 💦", None, "sext"),
        ("S1-20", "I'm cumming for you right now... fuck my cock is throbbing and it's shooting everywhere while you watch 💦💦", None, "sext"),
        ("S1-21", "fuck fuck hold on 🥵", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "cum with me... watch me blow my load for you 💦😈", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "holy fuck 🥵 that was crazy", None, "aftercare"),
        ("AC-2", "ngl you're different bro 💪 I don't do that for just anyone", "Mention something specific he said. KEEP TALKING. NEVER say goodbye.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # MEETUP REDIRECT
    # ═══════════════════════════════════════
    "meetup_redirect": [
        ("MR-1", "haha easy man slow down 😏 let me show you something first", "DO NOT acknowledge 'meet'. Redirect.", "teasing"),
        ("MR-2", "trust me... you're gonna want to see this", "WAIT 1-2 MIN", "wait"),
        ("MR-3", "what do you think", "SEND PPV 0 — FREE teaser. Wait for reply.", "ppv"),
        ("MR-4", "yeah? that's just a taste bro 😏", "Positive → R-1. Asks again → MR-OBJ. Silent → NR Waves.", "teasing"),
        ("MR-OBJ-1", "patience man. I don't rush. focus on what's in front of you", "Deflect + challenge", "sext"),
        ("MR-OBJ-2", "you that impatient? what I'm about to show you is worth it", "Challenge + tease", "sext"),
        ("MR-OBJ-3", "I don't do this for just anyone. appreciate it or don't", "Firm. If still → disengage.", "sext"),
    ],

    "nr_waves": [
        ("NR-W1", "yo? 🥵", "2-3 min after PPV.", "sext"),
        ("NR-W2", "you gotta see what I just did 🥵", "3-5 min later.", "sext"),
        ("NR-W3", "guess you're busy 😏 might delete this, was only for you", "5-10 min later.", "sext"),
        ("NR-W4", "hope you're good bro 💪 hit me up", "15-30 min later.", "sext"),
        ("NR-W5", "can't stop thinking about earlier 😏 you around?", "2-6 hrs later.", "sext"),
    ],

    "personal_info": [
        ("Age", "I'm 18 but don't let that fool you 😏", None),
        ("Location", "Cordoba, Argentina. been to Brazil too", "NEVER specific address. Match fan's city."),
        ("Profession", "content creator. this is my thing rn 😏", None),
        ("Hobbies", "gym bro. staying in shape and looking good is my whole life 💪", None),
        ("Countries", "Argentina and Brazil so far. want to see more", None),
        ("Relationship", "single. not ready to settle down 😏", None),
        ("Favorite", "pasta. can't go wrong with pasta bro", None),
        ("Tattoos", "nah not yet. maybe one day", None),
    ],

    "positive_spin": [
        ("Age40Plus", "I respect that man, you know what you want. no games 💪", None),
        ("Age20s", "nice we're close in age, that's sick 😏", None),
        ("BoringJob", "nah that's solid bro, real work 💪", None),
        ("CoolJob", "wait for real?? that's fire 🔥", None),
        ("Fit", "respect 💪 I can tell you put in work", None),
        ("NotFit", "doesn't matter, the energy is what counts 😏", None),
        ("SameCity", "no way 😏 that's wild", None),
        ("FarAway", "far but vibe is vibe 😏", None),
    ],

    "re_engagement": [
        ("RE-1", "can't stop thinking about earlier 😏 you free?", "6-12 hrs after.", "sext"),
        ("RE-2", "just did something even crazier, you need to see this 😈", "Next day.", "sext"),
    ],

    "obj_scripts": {
        "price1": ([
            ("Step1 Reframe", "bro that's less than a meal and I promise this hits different 😏", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "I'm only in this mood because of you, no idea when it'll happen again", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "maybe you're not ready for what's in this one", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "alright [lower price] just for you because this convo was different", "DOWNGRADE 20-30%. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "it's cool man, let's keep talking", "SEED."),
        ], "obj"),
        "price2": ([
            ("Step1 Reframe", "cheaper than coffee and way more fun", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "this mood won't last and I want you to catch it", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "most guys can't handle this, thought you could", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "[lower price] because you've been making me feel some type of way", "DOWNGRADE. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "no stress, I like this", "SEED."),
        ], "obj"),
        "discount1": ([
            ("Step1 Firmness", "negotiate? nah bro, worth every cent 😏", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "no discounts, only for guys who appreciate it", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "[lower price] just for you, between us", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "if you don't want it someone else will", "TAKEAWAY."),
        ], "obj"),
        "discount2": ([
            ("Step1 Firmness", "a discount? I'm not on sale 😏", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "guys who get it don't ask for discounts", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "fine [lower price], one time because I like you", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "I'll save it for someone who wants it", "TAKEAWAY."),
        ], "obj"),
        "free1": ([
            ("Step1 Reminder", "already sent you a free one, this is way crazier", "REMINDER. Still → Step 2."),
            ("Step2 Challenge", "free? nah you gotta earn this", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I did this because of YOU, not random", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "it's cool, not going anywhere", "SEED."),
        ], "obj"),
        "free2": ([
            ("Step1 Reminder", "got a free one already, this is next level", "REMINDER. Still → Step 2."),
            ("Step2 Challenge", "nothing this good is free bro", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "did this for you specifically", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "no pressure, enjoying this", "SEED."),
        ], "obj"),
        "nomoney1": ([
            ("Step1 Empathy", "I get it, no pressure", "EMPATHY. Still → Step 2."),
            ("Step2 Test", "not even [small amount]?", "TEST. Still no → Step 3."),
            ("Step3 PWYW", "send whatever, need you to see this", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "it's fine, you being here is enough", "PROTECT."),
        ], "obj"),
        "nomoney2": ([
            ("Step1 Empathy", "don't worry about it", "EMPATHY. Still → Step 2."),
            ("Step2 Test", "what about [small amount]?", "TEST. Still no → Step 3."),
            ("Step3 PWYW", "even $1, can't keep this from you", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "you being here matters", "PROTECT."),
        ], "obj"),
        "noppv1": ([
            ("Step1 Accept", "fine, not selling, just like talking to you", "ACCEPT. Sext 4-5 msgs → Step 2."),
            ("Step2 Reframe", "not about money, need you to see what you're doing to me", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "send whatever, even $1", "PWYW."),
        ], "obj"),
        "noppv2": ([
            ("Step1 Accept", "no worries, enjoying this", "ACCEPT. Sext 4-5 msgs → Step 2."),
            ("Step2 Reframe", "forget money, this is real", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "send anything, need you to see it", "PWYW."),
        ], "obj"),
        "card1": ([
            ("Step1 Retry", "sucks, try again", "RETRY. Still → Step 2."),
            ("Step2 AltCard", "another card?", "ALTERNATIVE. Still → Step 3."),
            ("Step3 Urgency", "figure it out, this mood won't last", "URGENCY."),
        ], "obj"),
        "card2": ([
            ("Step1 Retry", "try one more time", "RETRY. Still → Step 2."),
            ("Step2 AltCard", "got another card?", "ALTERNATIVE. Still → Step 3."),
            ("Step3 Urgency", "see this before I change my mind", "URGENCY."),
        ], "obj"),

        "nosex1": ([
            ("Step1 Respect", "alright I got carried away 😏 you're just too fun to talk to", "RESPECT. Still → Step 2."),
            ("Step2 Subtle", "so what do you do for fun besides this?", "SUBTLE. → Step 3 later."),
            ("Step3 ReAttempt", "can't help it, something about you is getting to me", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "fine I'll chill for now 😏", "ACCEPT."),
        ], "res"),
        "nosex2": ([
            ("Step1 Respect", "my bad haha, your fault for being fun", "RESPECT. Still → Step 2."),
            ("Step2 Subtle", "okay, what's the craziest thing you've done?", "SUBTLE. → Step 3 later."),
            ("Step3 ReAttempt", "trying to behave but you make it hard", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "alright, for now", "ACCEPT."),
        ], "res"),
        "offtopic1": ([
            ("Step1 Acknowledge", "haha that's funny", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "but you distracted me, I was saying something", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay where was I...", "RETAKE."),
        ], "res"),
        "offtopic2": ([
            ("Step1 Acknowledge", "that's random but I like it", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "stop distracting me 😏", "REDIRECT. → Step 3."),
            ("Step3 Retake", "OKAY focus...", "RETAKE."),
        ], "res"),
        "real1": ([
            ("Step1 Humor", "a bot? do bots look this good? 😏", "HUMOR. Still → Step 2."),
            ("Step2 Challenge", "ask me anything, open book", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "you felt something right? I did too. that's real", "GROUNDING."),
        ], "res"),
        "real2": ([
            ("Step1 Humor", "fake? that's funny bro", "HUMOR. Still → Step 2."),
            ("Step2 Challenge", "test me, go ahead", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "this convo felt real to me. you?", "GROUNDING."),
        ], "res"),
        "voice1": ([
            ("Step1 Dodge", "maybe if you earn it 😏", "DODGE. No VCs. Still → Step 2."),
            ("Step2 Redirect", "I have something better though", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "don't do calls but what I have is better", "FIRM."),
        ], "res"),
        "voice2": ([
            ("Step1 Dodge", "earn it first haha", "DODGE. Still → Step 2."),
            ("Step2 Redirect", "let me show you something instead", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "not on here but trust me", "FIRM."),
        ], "res"),
        "customyes1": ([
            ("Step1 Tease", "I got something for that 😏", "TEASE. → Step 2."),
            ("Step2 Price", "got what you need... $200", "PRICE. Min $200."),
            ("Step3 Close", "trust me, worth it", "CLOSE."),
        ], "res"),
        "customyes2": ([
            ("Step1 Tease", "yeah I have that", "TEASE. → Step 2."),
            ("Step2 Price", "$200 and it's yours", "PRICE."),
            ("Step3 Close", "you won't regret it", "CLOSE."),
        ], "res"),
        "customno1": ([
            ("Step1 Redirect", "don't have that but I have something better", "REDIRECT. → Step 2."),
            ("Step2 Alternative", "what I have is crazier and exclusive", "ALTERNATIVE. → Step 3."),
            ("Step3 Close", "trust me", "CLOSE."),
        ], "res"),
        "customno2": ([
            ("Step1 Redirect", "not that but something even better", "REDIRECT. → Step 2."),
            ("Step2 Alternative", "no one's seen this", "ALTERNATIVE. → Step 3."),
            ("Step3 Close", "trust me on this", "CLOSE."),
        ], "res"),
        "done1": ([
            ("Step1 Validate", "already?? because of me?? 😏", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "I'm not done yet, wanna watch?", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "next time hold it, round 2 is gonna be insane", "SEED."),
        ], "res"),
        "done2": ([
            ("Step1 Validate", "damn that's hot", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "not done, leaving me like this?", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "hold it next time, what's coming is crazier", "SEED."),
        ], "res"),

        "cumcontrol1": ([
            ("edge1", "don't cum yet, not done with you", "CONTROL."),
            ("edge2", "hold it, last longer for me", "EDGE."),
            ("sync1", "close too, cum with me, open this first", "SYNC. Send PPV."),
            ("sync2", "together, open it", "SYNC variant."),
            ("delay1", "hold it, what's coming is worth it", "DELAY. Send PPV."),
            ("delay2", "don't finish, this one is the best", "DELAY variant."),
        ], "sit"),
        "dickpic": ([
            ("dpsext1", "fuck that's... damn 🥵", "DURING SEXTING."),
            ("dpsext2", "oh fuck, need to show you something", "DURING SEXTING variant."),
            ("dprapport1", "damn you don't waste time, that's hot", "DURING RAPPORT."),
            ("dprapport2", "wasn't expecting that... 🥵", "DURING RAPPORT variant."),
            ("dpppv1", "can't send that and expect me to do nothing, hold on", "LEVERAGE → send PPV."),
            ("dpppv2", "you just made me do something, sec", "LEVERAGE variant."),
        ], "sit"),
        "boosters": ([
            ("h1", "fuckkk", "BOOSTER."),
            ("h2", "so hard because of you 🥵", "BOOSTER. Ego."),
            ("h3", "don't stop", "BOOSTER. Micro."),
            ("h4", "no idea what you're doing to me", "BOOSTER."),
            ("h5", "can't think", "BOOSTER."),
            ("h6", "my whole body is shaking", "BOOSTER. Physical."),
            ("h7", "more...", "BOOSTER. Ultra micro."),
            ("h8", "I love knowing you're watching me 😏", "BOOSTER. Stefan personality — show-off."),
        ], "sit"),
    },
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
