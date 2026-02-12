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
        "price1": ([
            ("Step1 Reframe", "bro that's less than a night out and nobody at the bar is showing you this 😏", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "I'm only in this mood because of you and I gotta be careful who I share this with", "FOMO + DL. Still no → Step 3."),
            ("Step3 Challenge", "maybe you're not ready for what's in this", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "[lower price] just for you because this stays between us", "DOWNGRADE 20-30%. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "it's cool dude, let's keep talking... I like this", "SEED."),
        ], "obj"),
        "price2": ([
            ("Step1 Reframe", "cheaper than a pizza and way more satisfying 😏", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "I don't share this with anyone, this is exclusive, between us", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "most guys can't handle this, thought you were different", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "[lower price] because you earned it", "DOWNGRADE. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "no stress bro", "SEED."),
        ], "obj"),
        "discount1": ([
            ("Step1 Firmness", "negotiate? nah dude, this is exclusive and worth it", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "no discounts, this is only for people who appreciate what they're getting", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "[lower price] for you but keep this between us", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "if you don't want it that's fine, someone else does", "TAKEAWAY."),
        ], "obj"),
        "discount2": ([
            ("Step1 Firmness", "a discount? nah this is too exclusive for that", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "the guys who get this don't negotiate", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "fine [lower price], one time, our secret", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "I'll save it for someone else", "TAKEAWAY."),
        ], "obj"),
        "free1": ([
            ("Step1 Reminder", "already sent you one free, this is on another level", "REMINDER. Still → Step 2."),
            ("Step2 Challenge", "free? bro you gotta earn this, nobody gets this for free", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I literally did this because of you, this isn't random content dude", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "it's cool, not going anywhere", "SEED."),
        ], "obj"),
        "free2": ([
            ("Step1 Reminder", "you got a free one already, this goes way further", "REMINDER. Still → Step 2."),
            ("Step2 Challenge", "nothing this exclusive is free", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "did this specifically for you, because of our convo", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "no pressure bro", "SEED."),
        ], "obj"),
        "nomoney1": ([
            ("Step1 Empathy", "I get it bro, no pressure at all", "EMPATHY. Still → Step 2."),
            ("Step2 Test", "not even [small amount]? really want you to see this", "TEST. Still no → Step 3."),
            ("Step3 PWYW", "send whatever you can, need you to see what you made me do", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "it's fine, you being here is enough", "PROTECT."),
        ], "obj"),
        "nomoney2": ([
            ("Step1 Empathy", "don't worry about it dude", "EMPATHY. Still → Step 2."),
            ("Step2 Test", "what about [small amount]?", "TEST. Still no → Step 3."),
            ("Step3 PWYW", "even $1, can't keep this from you", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "you being here matters", "PROTECT."),
        ], "obj"),
        "noppv1": ([
            ("Step1 Accept", "fine, not selling anything, just enjoying this", "ACCEPT. Sext 4-5 msgs → Step 2."),
            ("Step2 Reframe", "not about money dude, I need you to see what you do to me, I don't show anyone this", "REFRAME + DL. Still no → Step 3."),
            ("Step3 PWYW", "send whatever, even $1, you need to see this", "PWYW."),
        ], "obj"),
        "noppv2": ([
            ("Step1 Accept", "no worries, I'm just vibing with you", "ACCEPT. Sext 4-5 msgs → Step 2."),
            ("Step2 Reframe", "forget money, this is between us, it's real", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "send anything", "PWYW."),
        ], "obj"),
        "card1": ([
            ("Step1 Retry", "that sucks, try again usually works", "RETRY. Still → Step 2."),
            ("Step2 AltCard", "another card? really don't want you to miss this", "ALTERNATIVE. Still → Step 3."),
            ("Step3 Urgency", "figure it out bro, I'm in this mood and my door is still locked 😏", "URGENCY + DL."),
        ], "obj"),
        "card2": ([
            ("Step1 Retry", "annoying, try once more", "RETRY. Still → Step 2."),
            ("Step2 AltCard", "got another card?", "ALTERNATIVE. Still → Step 3."),
            ("Step3 Urgency", "see this before I have to go back to my boys", "URGENCY + DL."),
        ], "obj"),

        "nosex1": ([
            ("Step1 Respect", "alright I got ahead of myself haha, you're just easy to talk to", "RESPECT. Still → Step 2."),
            ("Step2 Subtle", "so what do you do for fun besides making me sneak onto my phone? 😏", "SUBTLE. → Step 3 later."),
            ("Step3 ReAttempt", "I can't help it dude, something about you is getting to me", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "alright I'll chill for now, no promises 😏", "ACCEPT."),
        ], "res"),
        "nosex2": ([
            ("Step1 Respect", "my bad, your fault for being fun", "RESPECT. Still → Step 2."),
            ("Step2 Subtle", "okay new topic, wildest party you've been to?", "SUBTLE. Frat angle. → Step 3 later."),
            ("Step3 ReAttempt", "trying to behave but you make it really hard", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "fine, for now", "ACCEPT."),
        ], "res"),
        "offtopic1": ([
            ("Step1 Acknowledge", "haha that's funny", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "but you distracted me from what I was saying", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay where was I...", "RETAKE."),
        ], "res"),
        "offtopic2": ([
            ("Step1 Acknowledge", "that's random but I like it", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "stop distracting me dude 😏", "REDIRECT. → Step 3."),
            ("Step3 Retake", "OKAY focus...", "RETAKE."),
        ], "res"),
        "real1": ([
            ("Step1 Humor", "a bot? bro do bots go to frat parties? 😏 kidding", "HUMOR. Still → Step 2."),
            ("Step2 Challenge", "ask me anything about me. open book, except my face obviously haha", "CHALLENGE. Faceless reference. Still → Step 3."),
            ("Step3 Grounding", "there's fake stuff on here but what we have is real. you know that right?", "GROUNDING."),
        ], "res"),
        "real2": ([
            ("Step1 Humor", "fake?? bro that's funny coming from someone who has my secret content", "HUMOR. Still → Step 2."),
            ("Step2 Challenge", "test me, go ahead", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "this convo was real to me. was it to you?", "GROUNDING."),
        ], "res"),
        "voice1": ([
            ("Step1 Dodge", "haha maybe but you know I gotta be careful... can't let people hear me", "DODGE. VC available but play DL first. Still → Step 2."),
            ("Step2 Redirect", "I have something way better for you though 😏", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "maybe if I'm somewhere private... but for now check this out instead", "FIRM. Note: Jack CAN do VCs — proceed carefully with DL framing."),
        ], "res"),
        "voice2": ([
            ("Step1 Dodge", "risky bro... you know my situation", "DODGE. DL. Still → Step 2."),
            ("Step2 Redirect", "let me show you something that'll make you forget you asked", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "let me find a time when nobody's around and maybe we can make it happen", "FIRM. Leave door open for VC."),
        ], "res"),
        "customyes1": ([
            ("Step1 Tease", "you want that? I can make it happen 😏 faceless obviously", "TEASE. Remind faceless. → Step 2."),
            ("Step2 Price", "I got exactly what you want... [price]", "PRICE. Set based on content."),
            ("Step3 Close", "trust me you won't regret it, nobody else gets this", "CLOSE."),
        ], "res"),
        "customyes2": ([
            ("Step1 Tease", "good taste... I think I can do that, just faceless", "TEASE. → Step 2."),
            ("Step2 Price", "[price] and it's yours, exclusive", "PRICE."),
            ("Step3 Close", "this one is gonna be special", "CLOSE."),
        ], "res"),
        "customno1": ([
            ("Step1 Redirect", "can't do that one but I have something that'll make you forget", "REDIRECT. → Step 2."),
            ("Step2 Alternative", "what I have is even crazier and nobody's seen it", "ALTERNATIVE. → Step 3."),
            ("Step3 Close", "trust me bro", "CLOSE."),
        ], "res"),
        "customno2": ([
            ("Step1 Redirect", "not that but something better", "REDIRECT. → Step 2."),
            ("Step2 Alternative", "exclusive, never shared, better than what you asked", "ALTERNATIVE. → Step 3."),
            ("Step3 Close", "trust me on this", "CLOSE."),
        ], "res"),
        "done1": ([
            ("Step1 Validate", "already?? because of me?? that's hot", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "but I'm not done yet, wanna see me finish? nobody else gets this", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "next time you wait for me, round 2 is gonna be insane 😏", "SEED."),
        ], "res"),
        "done2": ([
            ("Step1 Validate", "damn that was quick... hot though", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "not done yet, leaving me like this?", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "hold it next time, what I have planned is way crazier", "SEED."),
        ], "res"),

        "cumcontrol1": ([
            ("edge1", "don't cum yet dude... I'm not done", "CONTROL."),
            ("edge2", "hold it, last a little longer for me", "EDGE."),
            ("sync1", "I'm close too, cum with me... see this first", "SYNC. Send PPV."),
            ("sync2", "together, right now... open this", "SYNC variant."),
            ("delay1", "hold it... what I'm about to send is worth it", "DELAY. Send PPV."),
            ("delay2", "don't finish before you see this", "DELAY variant."),
        ], "sit"),
        "dickpic": ([
            ("dpsext1", "fuck... that did something to me bro", "DURING SEXTING."),
            ("dpsext2", "damn. need to show you something right now", "DURING SEXTING variant."),
            ("dprapport1", "damn you don't waste time huh, that's actually hot ngl", "DURING RAPPORT."),
            ("dprapport2", "wasn't expecting that... 🥵", "DURING RAPPORT variant."),
            ("dpppv1", "you can't send that and expect me to just sit here, hold on", "LEVERAGE → send PPV."),
            ("dpppv2", "okay you just made me do something... sec", "LEVERAGE variant."),
        ], "sit"),
        "boosters": ([
            ("h1", "fuckkk", "BOOSTER."),
            ("h2", "so hard rn because of you 🥵", "BOOSTER. Ego."),
            ("h3", "don't stop", "BOOSTER. Micro."),
            ("h4", "you have no idea what you're doing to me", "BOOSTER."),
            ("h5", "I can't think straight", "BOOSTER."),
            ("h6", "I'm biting my pillow trying to stay quiet", "BOOSTER. Physical + DL."),
            ("h7", "more...", "BOOSTER. Ultra micro."),
            ("h8", "my boys are right outside and they have no idea what I'm doing rn 😏", "BOOSTER. Jack personality — DL/frat/secret."),
        ], "sit"),
    },
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
