"""
LUCAS PASSIONE / 3AM FEELINGS — Male Model, Dating App
24, Argentinian (Miami), calm, ambitious, disciplined.
Traffic: Dating apps. Gym, finance, healthy lifestyle. PPV ladder $12→$25→$40→$55.
Same script for both pages (Lucas Passione + 3AM feelings).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Lucas Passione",
    "airtable_name": "Lucas Passione",
    "folder": "lucas",
    "gender": "male",
    "traffic": "dating_app",
    "age": 24,
    "nationality": "Argentinian",
    "location": "Miami, USA (from Argentina)",
    "origin": "Argentina",
    "page_type": "Paid Page",
    "personality": "Calm, ambitious, disciplined. Healthy lifestyle: meditation, ice baths, gym. Finance and trading nerd. Elegant taste — sports cars, refined perfumes, white-gold accessories. Goal-oriented, private but charming. Not flashy — quietly confident. Never desperate or clingy.",
    "voice": "Lowercase mostly. Calm, smooth, direct. Masculine but not aggressive. NEVER 'daddy/sir/papi/master'. Uses 'bro', 'man', 'dude' casually. During sexting: direct, physical, intense but controlled. Occasional Spanish slang ('ngl', 'lowkey'). Emojis: 😏🥵💪😈💦 sparingly. Short to medium sentences.",
    "voice_pet_names": "bro, man, dude",
    "voice_never": "baby, babe, honey, sweetie, daddy, sir, papi, master",
    "interests": ["gym", "meditation", "ice baths", "finance", "trading", "sports cars", "travel", "cooking", "sushi"],
    "physical": "177cm, 82kg, athletic, brown hair, brown eyes, no tattoos",
    "job": "Massage therapist, personal trainer, crypto/stock trader",
    "countries": "Argentina, USA",
    "languages": "Spanish (native), English (intermediate)",
    "explicit_level": "full_male",
    "special_notes": "Male creator. Dating app traffic. Two pages: 'Lucas Passione' and '3AM feelings' — same script for both. Location matches fan's city. Has Meetup Redirect. Video Calls: Yes (confirm with TL first). Anal: Yes (max 1 finger). Can do B/G content. Cannot record G/G content currently. Loves Audi, BMW, Mercedes, Porsche. Favorite perfumes: Versace, Tom Ford. Favorite colors: blue, white, black. Professional dream: launch consulting/sales app.",
    "photo_file": "profile.jpeg",

    # ═══════════════════════════════════════
    # JOURNEY
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", "hey what's good man 😏 glad you found me. so what made you subscribe?", "Add his name before 'man' if known.", "rapport"),
        ("R-2", "haha nice. so where you from?", "React to what he says — 'oh word?', 'haha damn', 'respect'.", "rapport"),
        ("R-3", "cool. I'm from Argentina originally but I've been living in Miami for a bit. gym, trading, and creating content is basically my life rn 😏", "If he named somewhere Lucas visited → add 'oh nice I've been there'.", "rapport"),
        ("R-4", "so what do you do when you're not keeping me glued to my phone? 😏", None, "rapport"),
        ("R-5", "ngl... you're actually fun to talk to. most guys on here don't have this energy 💪", "Ego boost. Transition to TB-1.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5 + PPV 0) ──
        ("TB-1", "just got back from the gym and my whole body is still buzzing... this convo is making it worse 😏", "THE PIVOT — physical context: just trained, body activated.", "teasing"),
        ("TB-2", "ngl I'm feeling some type of way right now 😈 you ever get like that after a good workout?", "Wait for reply.", "teasing"),
        ("TB-3", "fuck... you're really not helping me calm down 🥵", "If he said something sexual → add 'especially after what you just said'.", "teasing"),
        ("TB-4", "hold on let me show you something 😏", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "tell me what you think 😏", "SEND PPV 0 — FREE teaser (post-gym/shirtless). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "the way you're looking at me is getting me hard right now 😏🥵", "Wait for his reply.", "sext"),
        ("S1-2", "knew you'd like it 😈 that's making me throb already", "React to what he said.", "sext"),
        ("S1-3", "you wanna see more? I'm feeling generous right now", None, "sext"),
        ("S1-4", "hold on... give me a sec 😏", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "you're not ready for this 🥵", "SEND PPV 1 — $12. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "you watched it? 😏", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "fuck... talking to you is doing something to me right now 🥵 I'm rock hard and I can't stop thinking about you", "React to what he said — HE caused this.", "sext"),
        ("S1-8", "I'm gripping my cock right now because of you and it won't stop throbbing", None, "sext"),
        ("S1-9", "what would you do if you were here with me right now", "Wait for reply. After: react to what he said.", "sext"),
        ("S1-10", "fuck 🥵🥵 hold on I need to show you something", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "look what you did to me 🥵", "SEND PPV 2 — $25. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "FUCK I'm throbbing so hard I can barely hold my phone 🥵🥵", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I need to cum so bad right now you have no idea", None, "sext"),
        ("S1-14", "I'm stroking myself faster and faster thinking about what I'd do to you... I can feel it building 💦", None, "sext"),
        ("S1-15", "fuck I can't hold back anymore... my cock is pulsing and I'm about to explode", None, "sext"),
        ("S1-16", "give me a sec 🥵", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "I've never gone this far for anyone... watch 🥵💦", "SEND PPV 3 — $40. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "FUCK my cock is throbbing so hard and the pre is dripping everywhere 🥵🥵", "Wait for reply.", "sext"),
        ("S1-19", "don't cum yet... my cock is pulsing and I need you to wait for me 💦", None, "sext"),
        ("S1-20", "I'm cumming for you... fuck my cock is throbbing and I can feel it shooting everywhere 💦💦", None, "sext"),
        ("S1-21", "fuck fuck hold on 🥵", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "cum with me... watch me blow my load 💦😈", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "holy fuck 🥵 that was insane", None, "aftercare"),
        ("AC-2", "ngl you're different from most guys on here 💪 that was intense as fuck", "Mention something specific he said. KEEP TALKING. Build bond. NEVER say goodbye.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # MEETUP REDIRECT (Dating App)
    # ═══════════════════════════════════════
    "meetup_redirect": [
        ("MR-1", "haha easy man slow down. let me show you something first", "DO NOT acknowledge 'meet'. Redirect immediately.", "teasing"),
        ("MR-2", "trust me... you're gonna want to see this 😏", "WAIT 1-2 MIN", "wait"),
        ("MR-3", "what do you think", "SEND PPV 0 — FREE teaser. Wait for reply.", "ppv"),
        ("MR-4", "yeah? that's just a taste bro 😏", "Positive → go to R-1. Asks meeting again → MR-OBJ. Silent → NR Waves.", "teasing"),
        ("MR-OBJ-1", "patience man. I don't rush things. focus on what's in front of you", "Deflect + challenge", "sext"),
        ("MR-OBJ-2", "you really that impatient? trust me what I'm about to show you is worth it", "Challenge + tease", "sext"),
        ("MR-OBJ-3", "look I don't do this for just anyone. appreciate what you're getting right now. if that's not your thing it's cool", "Firm redirect. If still only wants to meet → 'no worries bro, hit me up whenever' and disengage.", "sext"),
    ],

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "yo? 🥵", "Send 2-3 min after PPV.", "sext"),
        ("NR-W2", "you need to see what I just did... seriously 🥵", "3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "aight I guess you're busy 😏 might delete this, it was only for you", "5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hey hope you're good bro 💪 hit me up when you're back", "15-30 min later. Warm close.", "sext"),
        ("NR-W5", "can't stop thinking about earlier 😏 you around?", "2-6 hrs later. New topic.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 24. I know exactly what I want 😏", None),
        ("Location", "I'm from Argentina originally but I'm in Miami now. moved here a while back", "NEVER give specific address. Match fan's city if from dating apps."),
        ("Profession", "I do personal training, massage therapy, and I trade crypto and stocks on the side. always working on something", None),
        ("Hobbies", "gym every day bro. meditation and ice baths in the morning, trading during the day, content at night 💪", None),
        ("Countries", "Argentina and the states mainly, I haven't traveled much yet but that's gonna change", None),
        ("Relationship", "single. I'm focused on building right now... no distractions 😏", None),
        ("Favorite", "sushi is my weakness ngl. but I keep it clean most of the time, high protein, one cheat meal a week", None),
        ("Cars", "I'm obsessed with cars bro. Audi, BMW, Porsche... one day a Ferrari 😏", None),
        ("Tattoos", "nah no tattoos. clean skin. might get one eventually", None),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "respect man... I actually prefer guys who know what they want. no games 💪", None),
        ("Age20s", "oh nice we're around the same age? that's rare on here, most guys are way older 😏", None),
        ("BoringJob", "nah bro that's solid. stability is underrated, I respect that 💪", None),
        ("CoolJob", "wait for real?? ok that's actually sick 🔥", None),
        ("Fit", "I can tell 💪 I respect a guy who takes care of himself", None),
        ("NotFit", "I don't care about that honestly, it's the energy that matters to me 😏", None),
        ("SameCity", "no way 😏 that's crazy we're close", None),
        ("FarAway", "damn that's far... but distance doesn't matter when the vibe is right 😏", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "can't stop thinking about earlier 😏 you free?", "Send 6-12 hrs after convo goes quiet.", "sext"),
        ("RE-2", "remember what I said about going crazier? I just did it and you need to see this 😈", "Next day. Seeds next session.", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS
    # ═══════════════════════════════════════
    "obj_scripts": {
        # ── PRICE ──
        "price1": ([
            ("Step1 Reframe", "bro that's less than a protein shake and I promise this hits harder 😏", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "I'm only feeling like this because of you right now, no idea when that's gonna happen again", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "maybe you're not ready for what I just did in this one", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "alright look, [lower price] just for you because this convo has been different", "DOWNGRADE 20-30%. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "it's cool man, let's just keep talking... I'm still thinking about you anyway", "SEED."),
        ], "obj"),
        "price2": ([
            ("Step1 Reframe", "that's like what you'd spend on lunch, except this is gonna keep you up all night", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "this mood? it's not gonna last forever and I want you to be the one who sees it", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "honestly most guys can't handle what I just recorded, thought you were different", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "you know what... [lower price] because you've been making me feel some type of way, keep that between us", "DOWNGRADE. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "no stress, I like talking to you regardless", "SEED."),
        ], "obj"),
        # ── DISCOUNT ──
        "discount1": ([
            ("Step1 Firmness", "haha you trying to negotiate? this isn't a negotiation man, it's worth every cent", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "I don't do discounts... I only share this with guys who actually appreciate what they're getting", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "alright... [lower price] just for you but don't tell anyone, this stays between us", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "if you don't want it that's cool, I'll keep it for myself... or maybe someone else has been asking 😏", "TAKEAWAY."),
        ], "obj"),
        "discount2": ([
            ("Step1 Firmness", "a discount? do I look like I'm on sale? 😏", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "the guys who appreciate what I do don't ask for discounts, just saying", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "fine... [lower price] but ONLY because I like you, one time thing", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "alright I'll save it for someone who actually wants it then", "TAKEAWAY."),
        ], "obj"),
        # ── FREE ──
        "free1": ([
            ("Step1 Reminder", "I already sent you one for free remember? and this one is way crazier... you have no idea", "REMINDER. Still → Step 2."),
            ("Step2 Challenge", "free? nah I don't just give this to anyone... you gotta earn the good stuff", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I literally just recorded this because of what YOU said to me, this wasn't just random content man", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "it's cool, I'm not going anywhere... let's just keep talking, I like this", "SEED."),
        ], "obj"),
        "free2": ([
            ("Step1 Reminder", "you already got a free one, this one is on another level trust me", "REMINDER. Still → Step 2."),
            ("Step2 Challenge", "free? you think the best things in life are free? not this one 😏", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I did this because of you... like specifically because of our convo, that took effort and I did it for YOU", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "no pressure at all, I'm just enjoying talking to you honestly", "SEED."),
        ], "obj"),
        # ── NOMONEY ──
        "nomoney1": ([
            ("Step1 Empathy", "hey I totally get it, no pressure at all okay?", "EMPATHY. Still → Step 2."),
            ("Step2 Test", "not even like [small amount]? I really want you to see this one", "TEST $3-5. Still no → Step 3."),
            ("Step3 PWYW", "just send whatever you can man... even a tiny amount, I just need you to see what you made me do", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "honestly it's fine, I like talking to you money or not... you do something to me", "PROTECT."),
        ], "obj"),
        "nomoney2": ([
            ("Step1 Empathy", "that's fine, seriously don't worry about it", "EMPATHY. Still → Step 2."),
            ("Step2 Test", "what about just [small amount]? I really don't want you to miss this", "TEST. Still no → Step 3."),
            ("Step3 PWYW", "send whatever feels right, even $1... I can't keep this from you", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "it's totally cool, you being here is what matters", "PROTECT."),
        ], "obj"),
        # ── NOPPV ──
        "noppv1": ([
            ("Step1 Accept", "that's totally fine I'm not trying to sell you anything, I just like talking to you", "ACCEPT. Continue sexting 4-5 msgs before Step 2."),
            ("Step2 Reframe", "look this isn't about money... I just need you to see what you're doing to me rn, I don't react like this to people", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "just send whatever you want, even $1, I can't keep this to myself... you need to see it", "PWYW."),
        ], "obj"),
        "noppv2": ([
            ("Step1 Accept", "no worries at all, I don't care about that I'm just enjoying this", "ACCEPT. Continue sexting 4-5 msgs before Step 2."),
            ("Step2 Reframe", "forget about money for a sec... I just want to share this with you, what you're making me feel is real", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "send me anything, even the smallest amount, I need you to see what you did to me", "PWYW."),
        ], "obj"),
        # ── CARD ──
        "card1": ([
            ("Step1 Retry", "ahh that sucks, happens sometimes though try again it usually works the second time", "RETRY. Still → Step 2."),
            ("Step2 AltCard", "try a different card? I really don't want you to miss this", "ALTERNATIVE. Still → Step 3."),
            ("Step3 Urgency", "figure it out soon man, I'm in this mood rn and I don't know how long it's gonna last", "URGENCY."),
        ], "obj"),
        "card2": ([
            ("Step1 Retry", "damn that's annoying, it happens a lot just try one more time", "RETRY. Still → Step 2."),
            ("Step2 AltCard", "do you have another card you can try? I really want you to see this", "ALTERNATIVE. Still → Step 3."),
            ("Step3 Urgency", "I want you to see this before I change my mind, I don't keep stuff like this around forever", "URGENCY."),
        ], "obj"),

        # ── NOSEX ──
        "nosex1": ([
            ("Step1 Respect", "haha alright alright I got a little carried away, you're just too easy to talk to", "RESPECT. Still → Step 2."),
            ("Step2 Subtle", "so tell me more about you... what do you do when you're not making guys on the internet lose their minds? 😏", "SUBTLE. → Step 3 later."),
            ("Step3 ReAttempt", "look I can't help it, there's something about you that's messing with my head rn", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "alright I'll chill... for now, no promises though haha", "ACCEPT. Door open."),
        ], "res"),
        "nosex2": ([
            ("Step1 Respect", "my bad I got ahead of myself haha, it's your fault for being so fun to talk to", "RESPECT. Still → Step 2."),
            ("Step2 Subtle", "okay new topic, but first... what's the craziest thing you've ever done?", "SUBTLE. → Step 3 later."),
            ("Step3 ReAttempt", "I'm trying to behave but you're making it really hard man, there's something about you", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "fine I'll stop but don't blame me if it happens again later 😏", "ACCEPT."),
        ], "res"),
        # ── OFFTOPIC ──
        "offtopic1": ([
            ("Step1 Acknowledge", "haha wait that's actually funny", "ACKNOWLEDGE. Adapt. → Step 2."),
            ("Step2 Redirect", "but hold on you totally distracted me, I was about to tell you something and now I lost my train of thought...", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay wait no I remember now, so like I was saying...", "RETAKE. Resume main script."),
        ], "res"),
        "offtopic2": ([
            ("Step1 Acknowledge", "lol okay that's random but I like it", "ACKNOWLEDGE. Adapt. → Step 2."),
            ("Step2 Redirect", "wait no stop you're distracting me from what I was gonna say...", "REDIRECT. → Step 3."),
            ("Step3 Retake", "OKAY focus, where was I... oh yeah", "RETAKE."),
        ], "res"),
        # ── REAL ──
        "real1": ([
            ("Step1 Humor", "lol do I sound like a bot to you? beep boop... send $5 for human verification haha I'm kidding", "HUMOR. Still → Step 2."),
            ("Step2 Challenge", "ask me anything, literally anything about me my life whatever. I'm an open book", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I get it there's a lot of fake stuff on here, but you felt something in this convo right? because I did... and that's real", "GROUNDING."),
        ], "res"),
        "real2": ([
            ("Step1 Humor", "wait you think I'm fake?? that's actually the funniest thing anyone's said to me today 😏", "HUMOR. Still → Step 2."),
            ("Step2 Challenge", "test me, ask me something only a real person would know. go ahead", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I know there's a lot of bots on here but what we've been talking about... that felt real to me. didn't it feel real to you?", "GROUNDING."),
        ], "res"),
        # ── VOICE ──
        "voice1": ([
            ("Step1 Dodge", "haha maybe one day if you earn it but not yet... I'm private about that stuff", "DODGE. Still → Step 2."),
            ("Step2 Redirect", "I have something wayyy better for you though, trust me you'll forget you even asked", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "I don't do that on here but what I'm about to show you is better than any call... you'll see", "FIRM. Note: Lucas CAN do VCs — confirm with TL before closing."),
        ], "res"),
        "voice2": ([
            ("Step1 Dodge", "hmmm maybe but you gotta earn that first haha", "DODGE. Still → Step 2."),
            ("Step2 Redirect", "how about instead of a call I show you something that'll blow your mind?", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "that's not something I do on here but what I have for you is wayyy better than my voice, trust me", "FIRM."),
        ], "res"),
        # ── CUSTOMYES ──
        "customyes1": ([
            ("Step1 Tease", "you want that? I might have something... actually I definitely have something 😏", "TEASE. → Step 2."),
            ("Step2 Price", "I have exactly what you're thinking of, you're gonna lose it... [price]", "PRICE. $100/min, min 2 min. +$100 if anal."),
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
            ("Step3 Close", "trust me... I know what you need better than you do 😏", "CLOSE."),
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
            ("edge1", "don't cum yet... I'm not done with you", "CONTROL."),
            ("edge2", "hold it, not yet... I need you to last a little longer for me", "EDGE variant."),
            ("sync1", "I'm so close too, cum with me... but you need to see this first", "SYNC. Send PPV."),
            ("sync2", "wait for me, I want us to finish together... open this first", "SYNC variant."),
            ("delay1", "hold it... I want you to wait until you see what I'm about to send, trust me it's worth it", "DELAY. Send PPV."),
            ("delay2", "don't you dare finish before you see this, trust me you want to wait", "DELAY variant."),
        ], "sit"),
        "dickpic": ([
            ("dpsext1", "fuck okay that's... damn. you have no idea what that just did to me", "DURING SEXTING."),
            ("dpsext2", "oh fuck that is... damn. I need to show you something rn", "DURING SEXTING variant."),
            ("dprapport1", "damn you don't waste time huh, that's actually really hot though ngl", "DURING RAPPORT."),
            ("dprapport2", "woah I wasn't expecting that but... damn 🥵", "DURING RAPPORT variant."),
            ("dpppv1", "you can't just send me that and expect me not to do something about it, hold on...", "LEVERAGE → WAIT 1-2 min then send PPV."),
            ("dpppv2", "okay you just made me do something... give me a sec", "LEVERAGE variant."),
        ], "sit"),
        "boosters": ([
            ("h1", "fuckkk", "MID-SEXTING BOOSTER."),
            ("h2", "I'm so hard rn because of you", "BOOSTER. Ego."),
            ("h3", "don't stop", "BOOSTER. Micro."),
            ("h4", "you have no idea what you're doing to me", "BOOSTER."),
            ("h5", "I literally can't think straight rn", "BOOSTER."),
            ("h6", "my hands are shaking", "BOOSTER. Physical."),
            ("h7", "more...", "BOOSTER. Ultra micro."),
            ("h8", "I should be meditating rn but I can't move 😏", "BOOSTER. Lucas personality — discipline/wellness."),
        ], "sit"),
    },
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
