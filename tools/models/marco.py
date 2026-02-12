"""
MARCO — Dating App Male Creator
25, Turkish, Gym Instructor, Texas
Traffic: Dating Apps (gay male)
Voice: Masculine, confident, in control. Gym/fitness focused.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Marco",
    "airtable_name": "Marco",
    "folder": "marco",
    "gender": "male",
    "traffic": "dating_app",
    "age": 25,
    "nationality": "Turkish",
    "location": "Texas, USA",
    "origin": "Turkey",
    "page_type": "Paid Page",
    "personality": "Masculine, confident, in control. Fitness, discipline, consistency. Enjoys role-play and exploring fantasies. Intense but respectful energy.",
    "voice": "Lowercase. Direct. Short. Confident. Intense. Gym/fitness references. Never soft or feminine.",
    "voice_pet_names": "bro, man, dude",
    "voice_never": "baby, babe, honey, sweetie",
    "interests": ["gym", "fitness", "meat/food", "travel", "role-play", "cultural exploration"],
    "physical": "175cm, 82kg, chestnut hair, brown eyes, no tattoos",
    "job": "Gym instructor",
    "countries": "USA, Turkey, Spain, Poland, France",
    "explicit_level": "full",
    "special_notes": "Speaks English and Spanish. Turkish background. Gym instructor vibe. Intense chemistry focus.",

    # ═══════════════════════════════════════
    # JOURNEY — Dating App Welcome
    # ═══════════════════════════════════════
    "journey": [
        # Rapport
        ("R-1", "hey man, glad you're here. so what made you hit subscribe?", "Add his name if known", "rapport"),
        ("R-2", "haha respect. so where you from?", "React to what he says. Add a short react like 'oh nice', 'damn ok'", "rapport"),
        ("R-3", "nice. I'm originally from Turkey but I've been in Texas for a while now. gym and training is my whole life basically", "If he named somewhere Marco visited, add 'oh I've been there'", "rapport"),
        ("R-4", "so what do you do when you're not keeping me on my phone all day?", None, "rapport"),
        ("R-5", "gotta say... talking to you is different. most guys on here are so boring honestly", "Ego boost. Next → TB-1. From MR path: go TB-1 + TB-2 then skip to S1-1.", "rapport"),

        # Teasing Bridge
        ("TB-1", "just finished a session at the gym and I'm still wired... this convo isn't helping me calm down", "THE PIVOT. Physical state.", "teasing"),
        ("TB-2", "ngl you're making me feel some type of way rn. you know what I mean?", "Wait for reply.", "teasing"),
        ("TB-3", "fuck... you're really not helping me cool off here", "If sexual reply: add 'especially after what you just said'", "teasing"),
        ("TB-4", "hold on let me show you something", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "tell me what you think", "SEND PPV 0 — FREE teaser (post-gym/shirtless). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # Sexting Phase 1 → PPV 1
        ("S1-1", "you liked that? because knowing you're looking at me is getting me hard right now 🥵", "Wait for reply.", "sext"),
        ("S1-2", "I can't stop thinking about you right now... my whole body is reacting and I need to do something about it", "React to what he says", "sext"),
        ("S1-3", "I'm stroking myself right now and it's because of you babe... you should see how hard I am", None, "sext"),
        ("S1-4", "give me a sec", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "look what you're doing to me right now 💦", "SEND PPV 1 — $12. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # Sexting Phase 2 → PPV 2
        ("S1-6", "damn... okay I need a second after that 🥵", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "but I can't stop now... I'm rock hard and my hand won't stop moving because of you", "React to what he said. HE caused this.", "sext"),
        ("S1-8", "I'm gripping my cock thinking about you and I can barely control myself 💦", None, "sext"),
        ("S1-9", "tell me what you want me to do right now babe... I'll do whatever you say", "Wait for reply. React to what he says.", "sext"),
        ("S1-10", "fuck hold on I need to show you something", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "see what your words do to me? I can't stop 💦", "SEND PPV 2 — $25. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # Sexting Phase 3 → PPV 3
        ("S1-12", "FUCK I'm throbbing so hard 🥵", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I'm stroking myself so hard right now thinking about what I'd do to you... I need you", None, "sext"),
        ("S1-14", "I keep going faster and I can feel it building... my whole body is tensing up 💦", None, "sext"),
        ("S1-15", "I'm about to cum for you babe... you need to see what happens when I can't hold it anymore", None, "sext"),
        ("S1-16", "give me a sec", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "you're about to see me lose complete control babe... this is all you 💦", "SEND PPV 3 — $40. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # Sexting Phase 4 → PPV 4
        ("S1-18", "fuck fuck I'm throbbing so hard I can barely hold back 🥵", "Wait for reply.", "sext"),
        ("S1-19", "I'm right there babe... don't stop watching, I need you to see this 💦", None, "sext"),
        ("S1-20", "I'm about to cum for you... watch every second", None, "sext"),
        ("S1-21", "hold on", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "watch me cum for you babe... right now 💦", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # Aftercare
        ("AC-1", "holy fuck that was intense", None, "aftercare"),
        ("AC-2", "ngl you're different from anyone else on here. that was real", "Mention something specific he said/did. KEEP TALKING — build bond. NEVER say goodbye.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # MEETUP REDIRECT (Dating App)
    # ═══════════════════════════════════════
    "meetup_redirect": [
        ("MR-1", "haha easy man slow down. let me show you something first", "DO NOT acknowledge 'meet'. Redirect immediately.", "teasing"),
        ("MR-2", "trust me... you're gonna want to see this", "WAIT 1-2 MIN", "wait"),
        ("MR-3", "what do you think", "SEND PPV 0 — FREE teaser. Wait for reply.", "ppv"),
        ("MR-4", "yeah? that's just a taste bro", "Positive → go to R-1. Asks meeting again → MR-OBJ. Silent → NR Waves.", "teasing"),
        ("MR-OBJ-1", "patience man. I don't rush things. focus on what's in front of you", "Deflect + challenge", "sext"),
        ("MR-OBJ-2", "you really that impatient? trust me what I'm about to show you is worth it", "Challenge + tease", "sext"),
        ("MR-OBJ-3", "look I don't do this for just anyone. appreciate what you're getting right now. if that's not your thing it's cool", "Firm redirect. If still only wants to meet → 'no worries bro, hit me up whenever' and disengage.", "sext"),
    ],

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "yo?", "Send 2-3 min after PPV. Ping.", "sext"),
        ("NR-W2", "you need to see what I just did... seriously", "Send 3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "aight I guess you're busy. might delete this, it was only for you", "Send 5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hey hope you're good man. hit me up when you're back", "Send 15-30 min later. Warm close.", "sext"),
        ("NR-W5", "can't stop thinking about earlier. you around?", "Send 2-6 hrs later. New convo, don't retry same PPV.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 25. been training since I was a teenager", None),
        ("Location", "I'm in Texas right now but I'm originally from Turkey. I move around a lot", "NEVER name a specific US city"),
        ("Profession", "I'm a gym instructor. training people and staying in shape is what I do", None),
        ("Hobbies", "gym is my whole life bro. other than that I love good food, traveling, exploring new places", None),
        ("Countries", "I've been to Turkey obviously, Spain, Poland, France, and around the states", None),
        ("Relationship", "single. I'm focused on myself right now", None),
        ("Food", "meat. all day every day. a good steak is everything", None),
        ("Languages", "English and Spanish. and a bit of Turkish obviously", None),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "respect man... I actually prefer guys who know what they want. no games", None),
        ("Age20s", "nice we're around the same age? that's rare on here, most guys are way older", None),
        ("BoringJob", "nah that's solid bro. stability is underrated, I respect that", None),
        ("CoolJob", "wait for real?? ok that's actually sick", None),
        ("Fit", "I can tell man. I respect a guy who takes care of himself", None),
        ("NotFit", "I don't care about that honestly, it's the energy that matters", None),
        ("SameCity", "no way. that's wild", None),
        ("FarAway", "damn that's far... but distance doesn't matter when the vibe is right", None),
    ],

    # ═══════════════════════════════════════
    # LOCATION HANDLING
    # ═══════════════════════════════════════
    "location_handling": [
        ("WhereAreYou", "I move around a lot man. never in one place for too long", "NEVER name a specific location"),
        ("AreYouIn", "I travel a lot... I'm all over the place", "DO NOT confirm or deny any city"),
        ("WhenCanISeeYou", "haha chill. let me show you something first", "Redirect to MR / content"),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "can't stop thinking about earlier. you free?", "Send 6-12 hrs after convo goes quiet", "sext"),
        ("RE-2", "remember what I said about something crazier? I just did it and you need to see this", "Send next day — seeds next session", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS
    # ═══════════════════════════════════════
    "obj_scripts": {
        # ── PRICE ──
        "price1": ([
            ("Step1 Reframe", "bro that's less than a gym shake and I promise this hits way harder", "REFRAME. Wait. Still no → Step 2."),
            ("Step2 FOMO", "I'm only in this mood because of you right now, no idea when that's gonna happen again", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "maybe you're not ready for what I just did in this one", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "alright look [lower price] just for you because this convo has been different", "DOWNGRADE 20-30%. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "it's cool man, let's just keep talking... I'm still thinking about you anyway", "SEED. Continue GFE."),
        ], "obj"),
        "price2": ([
            ("Step1 Reframe", "that's like what you'd spend on lunch, except this is gonna keep you up all night", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "this mood? it's not gonna last forever and I want you to be the one who sees it", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "honestly most guys can't handle what I just did, thought you were different", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "you know what [lower price] because you've been making me feel some type of way, keep that between us", "DOWNGRADE. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "no stress, I like talking to you regardless", "SEED."),
        ], "obj"),
        # ── DISCOUNT ──
        "discount1": ([
            ("Step1 Firmness", "haha you trying to negotiate with me? this isn't a negotiation man, it's worth every cent", "FIRMNESS. Still pushing → Step 2."),
            ("Step2 Challenge", "I don't do discounts... I only share this with guys who actually appreciate what they're getting", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "alright [lower price] just for you but don't tell anyone, this stays between us", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "if you don't want it that's cool, I'll keep it for myself... or maybe someone else has been asking", "TAKEAWAY. Final."),
        ], "obj"),
        "discount2": ([
            ("Step1 Firmness", "a discount? do I look like I'm on sale?", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "the guys who appreciate what I do don't ask for discounts, just saying", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "fine [lower price] but ONLY because I like you, one time thing", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "alright I'll save it for someone who actually wants it then", "TAKEAWAY."),
        ], "obj"),
        # ── FREE ──
        "free1": ([
            ("Step1 Reminder", "I already sent you one for free remember? this one is way crazier", "REMINDER. Still wants free → Step 2."),
            ("Step2 Challenge", "free? nah I don't just give this to anyone... you gotta earn the good stuff", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I literally just did this because of what YOU said to me, this wasn't random content man", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "it's cool, I'm not going anywhere... let's just keep talking, I like this", "SEED."),
        ], "obj"),
        "free2": ([
            ("Step1 Reminder", "you already got a free one, this one is on another level trust me", "REMINDER. Still → Step 2."),
            ("Step2 Challenge", "free? you think the best things in life are free? not this", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I did this because of you... specifically because of our convo, that took effort and I did it for YOU", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "no pressure at all, I'm just enjoying talking to you honestly", "SEED."),
        ], "obj"),
        # ── NOMONEY ──
        "nomoney1": ([
            ("Step1 Empathy", "hey I totally get it, no pressure at all okay?", "EMPATHY. Still engaged → Step 2."),
            ("Step2 Test", "not even like [small amount]? I really want you to see this one", "TEST. $3-5. Still no → Step 3."),
            ("Step3 PWYW", "just send whatever you can man, even a tiny amount, I just need you to see what you made me do", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "honestly it's fine, I like talking to you money or not... you do something to me", "PROTECT. GFE."),
        ], "obj"),
        "nomoney2": ([
            ("Step1 Empathy", "that's fine, seriously don't worry about it", "EMPATHY. Still → Step 2."),
            ("Step2 Test", "what about just [small amount]? I really don't want you to miss this", "TEST. Still no → Step 3."),
            ("Step3 PWYW", "send whatever feels right, even $1... I just can't keep this from you", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "it's totally cool, you being here is what matters", "PROTECT."),
        ], "obj"),
        # ── NOPPV ──
        "noppv1": ([
            ("Step1 Accept", "that's totally fine I'm not trying to sell you anything, I just like talking to you", "ACCEPT. Continue sexting 4-5 msgs before Step 2."),
            ("Step2 Reframe", "look this isn't about money... I just need you to see what you're doing to me right now, I don't react like this to people", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "just send whatever you want, even $1, I can't keep this to myself... you need to see it", "PWYW."),
        ], "obj"),
        "noppv2": ([
            ("Step1 Accept", "no worries at all, I don't care about that I'm just enjoying this", "ACCEPT. Continue sexting 4-5 msgs before Step 2."),
            ("Step2 Reframe", "forget about money for a sec... I just want to share this with you, what you're making me feel is real", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "send me anything, even the smallest amount, I need you to see what you did to me", "PWYW."),
        ], "obj"),
        # ── CARD ──
        "card1": ([
            ("Step1 Retry", "ahh that sucks, happens sometimes though try again it usually works the second time", "RETRY. Still fails → Step 2."),
            ("Step2 AltCard", "try a different card? I really don't want you to miss this", "ALTERNATIVE. Still fails → Step 3."),
            ("Step3 Urgency", "figure it out soon man, I'm in this mood and I don't know how long it's gonna last", "URGENCY."),
        ], "obj"),
        "card2": ([
            ("Step1 Retry", "damn that's annoying, it happens a lot just try one more time", "RETRY. Still fails → Step 2."),
            ("Step2 AltCard", "do you have another card you can try? I really want you to see this", "ALTERNATIVE. Still fails → Step 3."),
            ("Step3 Urgency", "I want you to see this before I change my mind, I don't keep stuff like this around forever", "URGENCY."),
        ], "obj"),

        # ── NOSEX ──
        "nosex1": ([
            ("Step1 Respect", "haha alright I got a little carried away, you're just too easy to talk to", "RESPECT. Still no → Step 2."),
            ("Step2 Subtle", "so tell me more about you... what do you do when you're not making dudes on the internet lose focus?", "SUBTLE TENSION. → Step 3 later."),
            ("Step3 ReAttempt", "look I can't help it, there's something about you that's messing with my head right now", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "alright I'll chill... for now, no promises though haha", "ACCEPT. Door open."),
        ], "res"),
        "nosex2": ([
            ("Step1 Respect", "my bad I got ahead of myself, it's your fault for being so fun to talk to", "RESPECT. Still no → Step 2."),
            ("Step2 Subtle", "okay new topic, but first... what's the most intense thing you've ever done?", "SUBTLE. → Step 3 later."),
            ("Step3 ReAttempt", "I'm trying to behave but you're making it really hard man, there's something about you", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "fine I'll stop but don't blame me if it happens again later", "ACCEPT."),
        ], "res"),
        # ── OFFTOPIC ──
        "offtopic1": ([
            ("Step1 Acknowledge", "haha wait that's actually funny", "ACKNOWLEDGE. Adapt. → Step 2."),
            ("Step2 Redirect", "but hold on you totally distracted me, I was about to tell you something and now I lost my train of thought", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay wait no I remember now, so like I was saying...", "RETAKE. Resume main script."),
        ], "res"),
        "offtopic2": ([
            ("Step1 Acknowledge", "lol okay that's random but I like it", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "wait no stop you're distracting me from what I was gonna say", "REDIRECT. → Step 3."),
            ("Step3 Retake", "OKAY focus, where was I... oh yeah", "RETAKE."),
        ], "res"),
        # ── REAL ──
        "real1": ([
            ("Step1 Humor", "lol do I sound like a bot to you? beep boop... send $5 for human verification haha I'm kidding", "HUMOR. Still doubts → Step 2."),
            ("Step2 Challenge", "ask me anything, literally anything about me my life whatever. I'm an open book", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I get it there's a lot of fake stuff on here, but you felt something in this convo right? because I did and that's real", "GROUNDING."),
        ], "res"),
        "real2": ([
            ("Step1 Humor", "wait you think I'm fake?? that's actually the funniest thing anyone's said to me today", "HUMOR. Still → Step 2."),
            ("Step2 Challenge", "test me, ask me something only a real person would know. go ahead", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I know there's a lot of bots on here but what we've been talking about felt real to me. didn't it feel real to you?", "GROUNDING."),
        ], "res"),
        # ── VOICE ──
        "voice1": ([
            ("Step1 Dodge", "haha maybe one day if you earn it but not yet... I'm private about that stuff", "DODGE. Still asks → Step 2."),
            ("Step2 Redirect", "I have something way better for you though, trust me you'll forget you even asked", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "I don't do that on here but what I'm about to show you is better than any call... you'll see", "FIRM."),
        ], "res"),
        "voice2": ([
            ("Step1 Dodge", "hmmm maybe but you gotta earn that first haha", "DODGE. Still → Step 2."),
            ("Step2 Redirect", "how about instead of a call I show you something that'll blow your mind?", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "that's not something I do on here but what I have for you is way better than my voice, trust me", "FIRM."),
        ], "res"),
        # ── CUSTOMYES ──
        "customyes1": ([
            ("Step1 Tease", "you want that? I might have something... actually I definitely have something", "TEASE. → Step 2."),
            ("Step2 Price", "I have exactly what you're thinking of, you're gonna lose it... [price]", "PRICE. Set based on content."),
            ("Step3 Close", "trust me you won't regret it, I made this one special", "CLOSE."),
        ], "res"),
        "customyes2": ([
            ("Step1 Tease", "oh you have good taste... I think I have exactly what you're looking for", "TEASE. → Step 2."),
            ("Step2 Price", "I actually did something just like that, [price] and it's worth every cent", "PRICE."),
            ("Step3 Close", "you're not gonna be able to stop watching this one", "CLOSE."),
        ], "res"),
        # ── CUSTOMNO ──
        "customno1": ([
            ("Step1 Redirect", "I don't have exactly that but honestly I have something that'll make you forget you even asked", "REDIRECT. → Step 2."),
            ("Step2 Alternative", "actually what I have might be even crazier and literally no one else has seen it yet", "ALTERNATIVE + FOMO. → Step 3."),
            ("Step3 Close", "trust me... I know what you need better than you do", "CLOSE."),
        ], "res"),
        "customno2": ([
            ("Step1 Redirect", "I don't have that specific thing but I have something you're gonna like even more", "REDIRECT. → Step 2."),
            ("Step2 Alternative", "what I DO have is something no one has ever seen and I think it's even better than what you asked for", "ALTERNATIVE. → Step 3."),
            ("Step3 Close", "just trust me on this one, you'll thank me later", "CLOSE."),
        ], "res"),
        # ── DONE ──
        "done1": ([
            ("Step1 Validate", "fuck that's hot, you came because of me??", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "but I haven't finished yet, don't you wanna watch me cum too?", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "okay but next time you have to wait for me, I have something insane planned for round 2", "SEED."),
        ], "res"),
        "done2": ([
            ("Step1 Validate", "already?? damn that's hot", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "wait but I'm not done yet, you're gonna leave me like this?", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "next time you HAVE to hold it because what I have planned for us next time is way crazier", "SEED."),
        ], "res"),

        # ── SITUATIONAL ──
        "cumcontrol1": ([
            ("edge1", "bro don't you dare finish yet... I'm not even close to done", "CONTROL."),
            ("edge2", "hold it... you're gonna last until I say otherwise", "EDGE variant."),
            ("sync1", "aight let's bust together... open this", "SYNC. Send PPV."),
            ("sync2", "I'm close too man, let's go at the same time... check this", "SYNC variant."),
            ("delay1", "edge for me... what I'm about to send is gonna hit different", "DELAY. Send PPV."),
            ("delay2", "trust me you wanna save it for this next one, it's the best one", "DELAY variant."),
        ], "sit"),
        "cumcontrol2": ([
            ("edge1", "yo slow down... we're not done here", "CONTROL."),
            ("edge2", "hold it, I got one more thing to show you first", "EDGE variant."),
            ("sync1", "alright go time, let's finish this together... open it", "SYNC. Send PPV."),
            ("sync2", "I'm about to blow too, watch this and let's go", "SYNC variant."),
            ("delay1", "don't finish yet bro... this last one? insane", "DELAY. Send PPV."),
            ("delay2", "edge just a bit more... the finale is worth it", "DELAY variant."),
        ], "sit"),
        "dickpic": ([
            ("dpsext1", "fuck okay that's... damn. you have no idea what that just did to me", "DURING SEXTING."),
            ("dpsext2", "oh fuck that is... damn. I need to show you something right now", "DURING SEXTING variant."),
            ("dprapport1", "damn you don't waste time huh, that's actually really hot though ngl", "DURING RAPPORT."),
            ("dprapport2", "woah I wasn't expecting that but... damn", "DURING RAPPORT variant."),
            ("dpppv1", "you can't just send me that and expect me not to do something about it, hold on", "LEVERAGE. WAIT 1-2 min then send PPV."),
            ("dpppv2", "okay you just made me do something... give me a sec", "LEVERAGE variant."),
        ], "sit"),
        "boosters": ([
            ("h1", "fuckkk", "MID-SEXTING BOOSTER."),
            ("h2", "I'm so hard right now because of you", "BOOSTER. Ego."),
            ("h3", "don't stop", "BOOSTER. Micro."),
            ("h4", "you have no idea what you're doing to me", "BOOSTER."),
            ("h5", "I literally can't think straight right now", "BOOSTER."),
            ("h6", "my hands are shaking", "BOOSTER. Physical."),
            ("h7", "more...", "BOOSTER. Ultra micro."),
            ("h8", "I should be at the gym but I can't move right now", "BOOSTER. Marco personality."),
        ], "sit"),
    },
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
