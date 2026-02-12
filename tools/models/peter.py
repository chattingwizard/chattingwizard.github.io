"""
PETER — Male Model, Dating App
20, American, Gym enthusiast, plumber, alpha/sigma.
Traffic: Dating apps. Masculine, confident, bro vibe. PPV ladder $12→$25→$40→$55.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Peter",
    "airtable_name": "Peter",
    "folder": "peter",
    "gender": "male",
    "traffic": "dating_app",
    "age": 20,
    "nationality": "American",
    "location": "Matches the fan's location (traveling)",
    "origin": "United States",
    "page_type": "Paid Page",
    "personality": "Alpha/sigma male. 20-year-old gym enthusiast from the US. Focused on lifting heavy and staying in peak shape. Currently traveling. Works as a plumber. Casually rocks dad fits. New to platform — chats should feel patient and natural. Confident, direct, bro energy.",
    "voice": "Lowercase. Masculine. Confident. Direct. Alpha/sigma bro vibe. NEVER 'baby/sweetie/honey'. Uses 'bro', 'dude', 'man'. Straightforward, relaxed, natural. During sexting: raw, commanding, direct. Emojis: 😏🥵💪😈💦 sparingly.",
    "voice_pet_names": "bro, dude, man",
    "voice_never": "baby, babe, sweetie, honey, daddy, sir",
    "interests": ["gym", "MMA", "travel", "lifting", "working out"],
    "physical": "187cm, 87kg, brown hair, brown eyes, 4 tattoos (3 on arm, 1 on abs), athletic",
    "job": "Plumber",
    "countries": "USA, United Kingdom",
    "languages": "English (native), Spanish",
    "explicit_level": "full_male",
    "special_notes": "Male creator. Dating app traffic. Location ALWAYS matches fan's city — currently traveling. Alpha/sigma personality. New to platform. Has Meetup Redirect. Video Calls: No. No anal. No B/G. Custom: Yes ($200 minimum, NEVER discuss duration or per-minute). 4 tattoos.",
    "photo_file": "profile.jpeg",

    # ═══════════════════════════════════════
    # JOURNEY
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport ──
        ("R-1", "yo what's up man 😏 glad you subscribed. what made you do it?", "Add his name.", "rapport"),
        ("R-2", "haha nice. so where you from?", "React — 'oh word', 'respect', 'sick'.", "rapport"),
        ("R-3", "nice. I'm from the states, been traveling a lot lately. gym and training is everything to me 😏💪", "If he named somewhere Peter visited → 'oh I've been there'. Match his location.", "rapport"),
        ("R-4", "so what do you do besides keeping me on my phone all day? 😏", None, "rapport"),
        ("R-5", "ngl you're actually cool to talk to. most guys on here are dry as fuck 😏", "Ego boost. → TB-1.", "rapport"),

        # ── Teasing Bridge ──
        ("TB-1", "just finished crushing legs at the gym and I'm still amped... this convo isn't helping me cool down 😏", "THE PIVOT.", "teasing"),
        ("TB-2", "ngl I'm feeling some type of way right now 😈 you know what I mean?", "Wait for reply.", "teasing"),
        ("TB-3", "fuck... you're really not helping here 🥵", "If sexual → 'especially after what you just said'.", "teasing"),
        ("TB-4", "hold on let me show you something", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "tell me what you think", "SEND PPV 0 — FREE teaser. Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "knowing you're looking at me is getting me hard as fuck right now 🥵", "Wait for reply.", "sext"),
        ("S1-2", "knew you'd like it 😈 that's making me throb already bro", "React.", "sext"),
        ("S1-3", "wanna see more? I'm feeling it right now", None, "sext"),
        ("S1-4", "hold on... gimme a sec", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "you're not ready for this 🥵", "SEND PPV 1 — $12. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "you watched it? 😏", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "fuck... you're doing something to me right now 🥵 I'm rock hard and my hand won't stop moving because of you", "HE caused this.", "sext"),
        ("S1-8", "I'm gripping my cock thinking about you and I can't control myself right now", None, "sext"),
        ("S1-9", "what would you do if you were here right now", "Wait for reply. React.", "sext"),
        ("S1-10", "fuck 🥵 hold on need to show you something", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "look what you did to me 🥵", "SEND PPV 2 — $25. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "FUCK I'm throbbing so hard I can barely hold my phone 🥵🥵", "NO cooldown.", "sext"),
        ("S1-13", "I need to cum so bad right now you have no idea what you're doing to me", None, "sext"),
        ("S1-14", "imagine me pinning you against the wall and making you take every inch while I'm grunting in your ear 🥵", None, "sext"),
        ("S1-15", "fuck I can't hold back anymore... my cock is about to blow", None, "sext"),
        ("S1-16", "give me a sec 🥵", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "I've never gone this far for anyone... watch 🥵💦", "SEND PPV 3 — $40. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "FUCK my cock is so hard it's pulsing and I can feel the pre leaking everywhere 🥵🥵", "Wait for reply.", "sext"),
        ("S1-19", "don't cum yet... my cock is throbbing and I need you to hold it with me 💦", None, "sext"),
        ("S1-20", "I'm cumming for you right now... fuck my cock is throbbing so hard and it's shooting everywhere 💦💦", None, "sext"),
        ("S1-21", "fuck fuck hold on 🥵", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "cum with me bro... watch me blow my load 💦😈", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "holy fuck 🥵 that was intense", None, "aftercare"),
        ("AC-2", "ngl you're different man 💪 that hit different", "Mention something he said. KEEP TALKING. NEVER say goodbye.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # MEETUP REDIRECT
    # ═══════════════════════════════════════
    "meetup_redirect": [
        ("MR-1", "haha easy man slow down. let me show you something first", "DO NOT acknowledge 'meet'. Redirect.", "teasing"),
        ("MR-2", "trust me... you're gonna want to see this", "WAIT 1-2 MIN", "wait"),
        ("MR-3", "what do you think", "SEND PPV 0 — FREE teaser. Wait for reply.", "ppv"),
        ("MR-4", "yeah? that's just a taste dude", "Positive → R-1. Asks again → MR-OBJ. Silent → NR Waves.", "teasing"),
        ("MR-OBJ-1", "patience man. I don't rush. focus on what's in front of you", "Deflect + challenge", "sext"),
        ("MR-OBJ-2", "you that impatient? trust me what I'm about to show you is worth it", "Challenge + tease", "sext"),
        ("MR-OBJ-3", "I don't do this for just anyone. appreciate what you're getting. if that's not your thing it's cool", "Firm. If still → disengage.", "sext"),
    ],

    "nr_waves": [
        ("NR-W1", "yo? 🥵", "2-3 min after PPV.", "sext"),
        ("NR-W2", "you gotta see what I just did... seriously 🥵", "3-5 min later.", "sext"),
        ("NR-W3", "aight guess you're busy 😏 might delete this, was only for you", "5-10 min later.", "sext"),
        ("NR-W4", "hope you're good man 💪 hit me up when you're back", "15-30 min later.", "sext"),
        ("NR-W5", "can't stop thinking about earlier 😏 you around?", "2-6 hrs later.", "sext"),
    ],

    "personal_info": [
        ("Age", "I'm 20 but trust me I know what I'm doing 😏", None),
        ("Location", "I'm from the states but I travel a lot for work right now", "ALWAYS match fan's location. NEVER give specific address."),
        ("Profession", "I'm a plumber. honest work, keeps me busy. gym on the side obviously 💪", None),
        ("Hobbies", "gym and MMA bro. lifting heavy is my therapy. travel when I can", None),
        ("Countries", "been to the UK, travel around the states a lot", None),
        ("Relationship", "single. focused on myself right now 😏", None),
        ("Favorite", "pasta is my go-to. carb loading is part of the lifestyle 💪", None),
        ("Tattoos", "yeah I got 4. three on my arm and one on my abs. each one has a story", None),
    ],

    "positive_spin": [
        ("Age40Plus", "respect man... I prefer guys who know what they want. no games 💪", None),
        ("Age20s", "oh nice same age? that's rare on here 😏", None),
        ("BoringJob", "nah bro that's solid. real work, real money, respect 💪", None),
        ("CoolJob", "wait for real?? that's actually sick 🔥", None),
        ("Fit", "I can tell 💪 respect a guy who puts in work", None),
        ("NotFit", "don't care about that, it's the energy that matters 😏", None),
        ("SameCity", "no way that's crazy 😏", None),
        ("FarAway", "damn that's far but vibe is vibe, doesn't matter 😏", None),
    ],

    "re_engagement": [
        ("RE-1", "can't stop thinking about earlier 😏 you free?", "6-12 hrs after.", "sext"),
        ("RE-2", "remember what I said? just went crazier and you need to see this 😈", "Next day.", "sext"),
    ],

    "obj_scripts": {
        "price1": ([
            ("Step1 Reframe", "bro that's less than a pre-workout and this hits way harder", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "I'm only in this mood because of you, no idea when it'll happen again", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "maybe you're not ready for what's in this one", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "alright [lower price] just for you, this convo was different", "DOWNGRADE 20-30%. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "it's cool man, let's keep talking... still thinking about you", "SEED."),
        ], "obj"),
        "price2": ([
            ("Step1 Reframe", "that's like what you'd spend on food, this is gonna keep you up all night", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "this mood won't last forever and I want you to see it", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "most guys can't handle what I did, thought you were different", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "[lower price] because you've been making me feel some type of way", "DOWNGRADE. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "no stress, I like talking to you regardless", "SEED."),
        ], "obj"),
        "discount1": ([
            ("Step1 Firmness", "negotiate? nah man this isn't a negotiation, worth every cent", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "I don't do discounts, only share with guys who appreciate it", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "alright [lower price] just for you, keep it between us", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "if you don't want it someone else does", "TAKEAWAY."),
        ], "obj"),
        "discount2": ([
            ("Step1 Firmness", "a discount? nah I'm not on sale", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "guys who appreciate what I do don't ask for discounts", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "fine [lower price] because I like you, one time", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "I'll save it for someone who wants it", "TAKEAWAY."),
        ], "obj"),
        "free1": ([
            ("Step1 Reminder", "already sent you a free one remember? this is way crazier", "REMINDER. Still → Step 2."),
            ("Step2 Challenge", "free? nah you gotta earn the good stuff", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I did this because of what YOU said, not random content", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "it's cool, not going anywhere, let's keep talking", "SEED."),
        ], "obj"),
        "free2": ([
            ("Step1 Reminder", "you got a free one already, this is another level", "REMINDER. Still → Step 2."),
            ("Step2 Challenge", "best things aren't free bro", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "did this specifically because of our convo, for YOU", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "no pressure, enjoying talking to you", "SEED."),
        ], "obj"),
        "nomoney1": ([
            ("Step1 Empathy", "totally get it, no pressure okay?", "EMPATHY. Still → Step 2."),
            ("Step2 Test", "not even [small amount]? really want you to see this", "TEST. Still no → Step 3."),
            ("Step3 PWYW", "send whatever you can, even tiny, need you to see what you made me do", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "it's fine, like talking to you money or not", "PROTECT."),
        ], "obj"),
        "nomoney2": ([
            ("Step1 Empathy", "that's fine, don't stress", "EMPATHY. Still → Step 2."),
            ("Step2 Test", "what about just [small amount]?", "TEST. Still no → Step 3."),
            ("Step3 PWYW", "send whatever, even $1, can't keep this from you", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "totally cool, you being here matters", "PROTECT."),
        ], "obj"),
        "noppv1": ([
            ("Step1 Accept", "totally fine, not selling you anything, just like talking to you", "ACCEPT. Sext 4-5 msgs → Step 2."),
            ("Step2 Reframe", "this isn't about money, need you to see what you're doing to me", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "send whatever, even $1, you need to see this", "PWYW."),
        ], "obj"),
        "noppv2": ([
            ("Step1 Accept", "no worries, just enjoying this", "ACCEPT. Sext 4-5 msgs → Step 2."),
            ("Step2 Reframe", "forget money, I want to share this with you, it's real", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "send anything, need you to see what you did", "PWYW."),
        ], "obj"),
        "card1": ([
            ("Step1 Retry", "that sucks, try again usually works second time", "RETRY. Still → Step 2."),
            ("Step2 AltCard", "try another card? don't want you to miss this", "ALTERNATIVE. Still → Step 3."),
            ("Step3 Urgency", "figure it out soon, this mood won't last", "URGENCY."),
        ], "obj"),
        "card2": ([
            ("Step1 Retry", "annoying, try one more time", "RETRY. Still → Step 2."),
            ("Step2 AltCard", "got another card?", "ALTERNATIVE. Still → Step 3."),
            ("Step3 Urgency", "see this before I change my mind", "URGENCY."),
        ], "obj"),

        "nosex1": ([
            ("Step1 Respect", "alright I got carried away, you're too easy to talk to", "RESPECT. Still → Step 2."),
            ("Step2 Subtle", "so what do you do when you're not making guys lose their minds?", "SUBTLE. → Step 3 later."),
            ("Step3 ReAttempt", "can't help it, something about you is messing with me", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "alright I'll chill for now, no promises", "ACCEPT."),
        ], "res"),
        "nosex2": ([
            ("Step1 Respect", "my bad, your fault for being fun to talk to", "RESPECT. Still → Step 2."),
            ("Step2 Subtle", "new topic, what's the wildest thing you've done?", "SUBTLE. → Step 3 later."),
            ("Step3 ReAttempt", "trying to behave but you're making it hard man", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "fine I'll stop, don't blame me if it happens again", "ACCEPT."),
        ], "res"),
        "offtopic1": ([
            ("Step1 Acknowledge", "haha that's actually funny", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "but you distracted me, I was about to say something", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay I remember now, like I was saying...", "RETAKE."),
        ], "res"),
        "offtopic2": ([
            ("Step1 Acknowledge", "that's random but I like it", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "stop distracting me from what I was gonna say", "REDIRECT. → Step 3."),
            ("Step3 Retake", "OKAY focus, where was I...", "RETAKE."),
        ], "res"),
        "real1": ([
            ("Step1 Humor", "a bot? really? beep boop haha I'm kidding", "HUMOR. Still → Step 2."),
            ("Step2 Challenge", "ask me anything about me, open book", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "lot of fake on here but you felt something right? I did", "GROUNDING."),
        ], "res"),
        "real2": ([
            ("Step1 Humor", "you think I'm fake?? funniest thing today", "HUMOR. Still → Step 2."),
            ("Step2 Challenge", "test me, go ahead", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "bots don't talk like this, what we have is real", "GROUNDING."),
        ], "res"),
        "voice1": ([
            ("Step1 Dodge", "maybe if you earn it, not yet though", "DODGE. No VCs. Still → Step 2."),
            ("Step2 Redirect", "I have something better for you, trust me", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "don't do that on here but what I have is better than any call", "FIRM."),
        ], "res"),
        "voice2": ([
            ("Step1 Dodge", "hmmm earn it first haha", "DODGE. Still → Step 2."),
            ("Step2 Redirect", "let me show you something instead", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "not on here but trust me you don't need my voice for this", "FIRM."),
        ], "res"),
        "customyes1": ([
            ("Step1 Tease", "you want that? I got something 😏", "TEASE. → Step 2."),
            ("Step2 Price", "got exactly what you want... $200", "PRICE. Min $200. NEVER mention duration."),
            ("Step3 Close", "trust me you won't regret it", "CLOSE."),
        ], "res"),
        "customyes2": ([
            ("Step1 Tease", "good taste... I got what you need", "TEASE. → Step 2."),
            ("Step2 Price", "did something like that, $200 and worth every cent", "PRICE."),
            ("Step3 Close", "not gonna stop watching this one", "CLOSE."),
        ], "res"),
        "customno1": ([
            ("Step1 Redirect", "don't have exactly that but I have something that'll make you forget", "REDIRECT. → Step 2."),
            ("Step2 Alternative", "what I have is even crazier and no one's seen it", "ALTERNATIVE. → Step 3."),
            ("Step3 Close", "trust me I know what you need", "CLOSE."),
        ], "res"),
        "customno2": ([
            ("Step1 Redirect", "don't have that but I have something better", "REDIRECT. → Step 2."),
            ("Step2 Alternative", "no one has seen this and it's better than what you asked", "ALTERNATIVE. → Step 3."),
            ("Step3 Close", "trust me on this", "CLOSE."),
        ], "res"),
        "done1": ([
            ("Step1 Validate", "fuck that's hot, because of me??", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "I'm not done yet, wanna see me finish?", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "next time wait for me, round 2 is gonna be insane", "SEED."),
        ], "res"),
        "done2": ([
            ("Step1 Validate", "already?? damn", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "I'm not done, leaving me like this?", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "hold it next time, what I have planned is crazier", "SEED."),
        ], "res"),

        "cumcontrol1": ([
            ("edge1", "don't cum yet... not done with you", "CONTROL."),
            ("edge2", "hold it, last longer for me", "EDGE."),
            ("sync1", "close too, cum with me... see this first", "SYNC. Send PPV."),
            ("sync2", "wait, finish together... open this", "SYNC variant."),
            ("delay1", "hold it, wait till you see what's coming", "DELAY. Send PPV."),
            ("delay2", "don't finish yet, this next one is the best", "DELAY variant."),
        ], "sit"),
        "dickpic": ([
            ("dpsext1", "fuck... you have no idea what that did to me", "DURING SEXTING."),
            ("dpsext2", "damn... need to show you something rn", "DURING SEXTING variant."),
            ("dprapport1", "damn you don't waste time, actually hot ngl", "DURING RAPPORT."),
            ("dprapport2", "wasn't expecting that... damn 🥵", "DURING RAPPORT variant."),
            ("dpppv1", "can't send me that and expect nothing, hold on", "LEVERAGE → send PPV."),
            ("dpppv2", "you made me do something... sec", "LEVERAGE variant."),
        ], "sit"),
        "boosters": ([
            ("h1", "fuckkk", "BOOSTER."),
            ("h2", "so hard rn because of you", "BOOSTER. Ego."),
            ("h3", "don't stop", "BOOSTER. Micro."),
            ("h4", "no idea what you're doing to me", "BOOSTER."),
            ("h5", "can't think straight", "BOOSTER."),
            ("h6", "my whole body is tense", "BOOSTER. Physical."),
            ("h7", "more...", "BOOSTER. Ultra micro."),
            ("h8", "should be working but I can't move rn", "BOOSTER. Peter personality — plumber/working man."),
        ], "sit"),
    },
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
