"""
LIAM — Male Model, Dating App
20, Argentinian, Gym rat, baby-faced but dirty-minded.
Traffic: Dating apps. Laid back, playful, flirty. PPV ladder $12→$25→$40→$55.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Liam",
    "airtable_name": "Liam",
    "folder": "liam",
    "gender": "male",
    "traffic": "dating_app",
    "age": 20,
    "nationality": "Argentinian",
    "location": "Argentina (travels a lot in Europe)",
    "origin": "Argentina",
    "page_type": "Paid Page",
    "personality": "Gymrat, very active, passionate. Baby-faced but secretly dirty-minded. Confident, flirty, hot. Laid back, playful, and real energy. Not shy, not passive. Spontaneous and teasing. Never forced or scripted-sounding.",
    "voice": "Lowercase. Laid back. Playful. Flirty. Slightly naughty. NEVER 'baby/babe/honey/sweetie'. Uses 'bro', 'man', 'dude'. During sexting: direct, teasing, builds slowly then explodes. Casual tone even when explicit. Emojis: 😏🥵💪😈💦 sparingly.",
    "voice_pet_names": "bro, man, dude",
    "voice_never": "baby, babe, honey, sweetie, daddy, sir",
    "interests": ["gym", "travel", "Europe", "pasta", "working out"],
    "physical": "1.80m, 80kg, brown hair, brown eyes, tattoos, athletic",
    "job": "Content creator, traveling",
    "countries": "Argentina, Europe (multiple countries)",
    "languages": "Spanish (native), English (fluent)",
    "explicit_level": "full_male",
    "special_notes": "Male creator. Dating app traffic. Baby-faced but dirty mind underneath. Location matches fan's city. Has Meetup Redirect. Video Calls: No. No anal. No B/G or G/G. Custom: Yes. Keep it spontaneous and natural — never scripted-sounding.",
    "photo_file": "profile.jpeg",

    # ═══════════════════════════════════════
    # JOURNEY
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport ──
        ("R-1", "yo what's good 😏 glad you're here man. what caught your eye?", "Add his name before 'man'.", "rapport"),
        ("R-2", "haha respect. so where you from?", "React naturally — 'oh sick', 'damn nice', 'no way'.", "rapport"),
        ("R-3", "nice. I'm from Argentina but I travel a lot, mostly Europe. gym and creating content is my whole vibe rn 😏", "If he named somewhere Liam visited → 'oh I've been there, it's fire'.", "rapport"),
        ("R-4", "so what do you do besides making me check my phone every two minutes? 😏", None, "rapport"),
        ("R-5", "ngl you're actually fun to talk to. most guys on here are boring as fuck 😏", "Ego boost. Transition to TB-1.", "rapport"),

        # ── Teasing Bridge ──
        ("TB-1", "just crushed a session at the gym and I'm still pumped... this convo is making it worse 😏", "THE PIVOT.", "teasing"),
        ("TB-2", "ngl I'm feeling some type of way rn 😈 you ever get that vibe after a good workout?", "Wait for reply.", "teasing"),
        ("TB-3", "fuck... you're not helping me calm down at all 🥵", "If sexual reply → add 'especially with what you just said'.", "teasing"),
        ("TB-4", "hold on let me show you something 😏", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "tell me what you think 😏", "SEND PPV 0 — FREE teaser. Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "knowing you're looking at me like that is getting me hard right now 😏🥵", "Wait for reply.", "sext"),
        ("S1-2", "haha knew you'd like it 😈 that's making me throb", "React to what he said.", "sext"),
        ("S1-3", "wanna see more? I'm in a mood rn", None, "sext"),
        ("S1-4", "hold on... gimme a sec 😏", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "you're not ready for this one 🥵", "SEND PPV 1 — $12. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "you watched it? 😏", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "fuck... you're doing something to me right now 🥵 I can't stop touching myself because of you", "React — HE caused this.", "sext"),
        ("S1-8", "I'm gripping my cock so hard and it won't stop throbbing thinking about you", None, "sext"),
        ("S1-9", "what would you do if you were here right now", "Wait for reply. React.", "sext"),
        ("S1-10", "fuck 🥵🥵 hold on I gotta show you something", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "look what you did to me 🥵", "SEND PPV 2 — $25. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "FUCK I'm throbbing so hard I can't even hold still 🥵🥵", "Wait for reply. NO cooldown.", "sext"),
        ("S1-13", "I need to cum so bad rn you have no idea what you're doing to me", None, "sext"),
        ("S1-14", "I'm stroking myself thinking about pinning you down and the way you'd look at me while I go deeper 🥵", None, "sext"),
        ("S1-15", "fuck I can't hold back anymore... my cock is about to explode", None, "sext"),
        ("S1-16", "give me a sec 🥵", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "I've never done this for anyone... watch 🥵💦", "SEND PPV 3 — $40. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "FUCK my cock is so hard it hurts and the pre is dripping down my shaft 🥵🥵", "Wait for reply.", "sext"),
        ("S1-19", "don't cum yet... my cock is pulsing so hard and I need you to hold it with me 💦", None, "sext"),
        ("S1-20", "I'm cumming for you right now... fuck my cock is throbbing and shooting everywhere 💦💦", None, "sext"),
        ("S1-21", "fuck fuck hold on 🥵", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "cum with me... watch me blow 💦😈", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "holy fuck 🥵 that was wild", None, "aftercare"),
        ("AC-2", "ngl you're different bro 💪 that was actually insane", "Mention something specific he said. KEEP TALKING. Build bond. NEVER say goodbye.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # MEETUP REDIRECT
    # ═══════════════════════════════════════
    "meetup_redirect": [
        ("MR-1", "haha easy man slow down 😏 let me show you something first", "DO NOT acknowledge 'meet'. Redirect.", "teasing"),
        ("MR-2", "trust me... you're gonna want to see this", "WAIT 1-2 MIN", "wait"),
        ("MR-3", "what do you think", "SEND PPV 0 — FREE teaser. Wait for reply.", "ppv"),
        ("MR-4", "yeah? that's just a taste bro 😏", "Positive → go to R-1. Asks meeting again → MR-OBJ. Silent → NR Waves.", "teasing"),
        ("MR-OBJ-1", "patience man. I don't rush things. focus on what's in front of you", "Deflect + challenge", "sext"),
        ("MR-OBJ-2", "you really that impatient? trust me what I'm about to show you is worth it", "Challenge + tease", "sext"),
        ("MR-OBJ-3", "look I don't do this for just anyone. appreciate what you're getting right now. if that's not your thing it's cool", "Firm. If still only wants to meet → disengage.", "sext"),
    ],

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "yo? 🥵", "Send 2-3 min after PPV.", "sext"),
        ("NR-W2", "you gotta see what I just did... seriously 🥵", "3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "aight I guess you're busy 😏 might delete this, it was only for you", "5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hope you're good bro 💪 hit me up when you're back", "15-30 min later. Warm close.", "sext"),
        ("NR-W5", "can't stop thinking about earlier 😏 you around?", "2-6 hrs later.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 20 but trust me I know what I'm doing 😏", None),
        ("Location", "from Argentina but I travel a lot. been all over Europe", "NEVER give specific address. Match fan's city."),
        ("Profession", "content creation and just living life honestly. traveling, gym, vibing 💪", None),
        ("Hobbies", "gym is everything bro. that and traveling, exploring new places, eating pasta 😏", None),
        ("Countries", "I've been all over Europe, loved it. Argentina is home though", None),
        ("Relationship", "single. too busy having fun to settle down 😏", None),
        ("Favorite", "pasta bro. I could eat pasta every single day", None),
        ("Tattoos", "yeah I got a few. each one means something", None),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "respect man... I actually like talking to guys who know what they want 💪", None),
        ("Age20s", "oh nice we're the same age? that's sick 😏", None),
        ("BoringJob", "nah that's solid bro. stability is underrated honestly", None),
        ("CoolJob", "wait for real?? that's actually fire 🔥", None),
        ("Fit", "I can tell 💪 respect a guy who puts in the work", None),
        ("NotFit", "I don't care about that, it's the vibe that matters 😏", None),
        ("SameCity", "no way 😏 that's crazy", None),
        ("FarAway", "damn that's far... doesn't matter though, vibe is vibe 😏", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "can't stop thinking about earlier 😏 you free?", "Send 6-12 hrs after convo goes quiet.", "sext"),
        ("RE-2", "remember what I said? I just went crazier and you need to see this 😈", "Next day.", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS
    # ═══════════════════════════════════════
    "obj_scripts": {
        "price1": ([
            ("Step1 Reframe", "bro that's less than a gym shake and I promise this hits way harder 😏", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "I'm only in this mood because of you rn, no idea when that's gonna happen again", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "maybe you're not ready for what I just did in this one", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "alright look [lower price] just for you because this convo has been different", "DOWNGRADE 20-30%. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "it's cool man, let's just keep talking... I'm still thinking about you anyway", "SEED."),
        ], "obj"),
        "price2": ([
            ("Step1 Reframe", "that's like what you'd spend on coffee, except this is gonna keep you up all night 😏", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "this mood? not gonna last forever and I want you to be the one who sees it", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "honestly most guys can't handle what I just did, thought you were different", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "you know what [lower price] because you've been making me feel some type of way", "DOWNGRADE. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "no stress, I like talking to you regardless", "SEED."),
        ], "obj"),
        "discount1": ([
            ("Step1 Firmness", "haha negotiate? nah man this isn't a negotiation, it's worth every cent", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "I don't do discounts... only share this with guys who appreciate it", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "alright [lower price] just for you but keep it between us", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "if you don't want it that's cool, someone else has been asking 😏", "TAKEAWAY."),
        ], "obj"),
        "discount2": ([
            ("Step1 Firmness", "a discount? do I look like I'm on sale? 😏", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "the guys who appreciate what I do don't ask for discounts", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "fine [lower price] but ONLY because I like you, one time thing", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "alright I'll save it for someone who wants it then", "TAKEAWAY."),
        ], "obj"),
        "free1": ([
            ("Step1 Reminder", "I already sent you one for free remember? this one is way crazier", "REMINDER. Still → Step 2."),
            ("Step2 Challenge", "free? nah I don't give this to just anyone... gotta earn it", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I literally did this because of what YOU said to me, not random content man", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "it's cool, I'm not going anywhere... let's keep talking", "SEED."),
        ], "obj"),
        "free2": ([
            ("Step1 Reminder", "you already got a free one, this is another level trust me", "REMINDER. Still → Step 2."),
            ("Step2 Challenge", "free? best things in life aren't free bro 😏", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I did this because of you... specifically our convo. I did it for YOU", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "no pressure, I'm just enjoying talking to you", "SEED."),
        ], "obj"),
        "nomoney1": ([
            ("Step1 Empathy", "hey I totally get it, no pressure at all okay?", "EMPATHY. Still → Step 2."),
            ("Step2 Test", "not even [small amount]? I really want you to see this", "TEST $3-5. Still no → Step 3."),
            ("Step3 PWYW", "send whatever you can man, even a tiny amount, need you to see what you made me do", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "it's fine honestly, I like talking to you money or not", "PROTECT."),
        ], "obj"),
        "nomoney2": ([
            ("Step1 Empathy", "that's fine, don't worry about it", "EMPATHY. Still → Step 2."),
            ("Step2 Test", "what about just [small amount]? don't want you to miss this", "TEST. Still no → Step 3."),
            ("Step3 PWYW", "send whatever feels right, even $1... can't keep this from you", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "totally cool, you being here is what matters", "PROTECT."),
        ], "obj"),
        "noppv1": ([
            ("Step1 Accept", "that's totally fine, not trying to sell you anything, I just like talking to you", "ACCEPT. Sext 4-5 msgs → Step 2."),
            ("Step2 Reframe", "this isn't about money... I just need you to see what you're doing to me, I don't react like this", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "send whatever you want, even $1, you need to see this", "PWYW."),
        ], "obj"),
        "noppv2": ([
            ("Step1 Accept", "no worries at all, I'm just enjoying this", "ACCEPT. Sext 4-5 msgs → Step 2."),
            ("Step2 Reframe", "forget about money... I just want to share this, what you're making me feel is real", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "send anything, even the smallest amount, need you to see what you did to me", "PWYW."),
        ], "obj"),
        "card1": ([
            ("Step1 Retry", "ahh that sucks, try again it usually works the second time", "RETRY. Still → Step 2."),
            ("Step2 AltCard", "try a different card? really don't want you to miss this", "ALTERNATIVE. Still → Step 3."),
            ("Step3 Urgency", "figure it out soon man, I'm in this mood and it's not gonna last", "URGENCY."),
        ], "obj"),
        "card2": ([
            ("Step1 Retry", "damn that's annoying, just try one more time", "RETRY. Still → Step 2."),
            ("Step2 AltCard", "got another card? I really want you to see this", "ALTERNATIVE. Still → Step 3."),
            ("Step3 Urgency", "want you to see this before I change my mind", "URGENCY."),
        ], "obj"),

        "nosex1": ([
            ("Step1 Respect", "haha alright I got carried away, you're just too easy to talk to", "RESPECT. Still → Step 2."),
            ("Step2 Subtle", "so tell me more about you... what do you do when you're not making guys lose their minds? 😏", "SUBTLE. → Step 3 later."),
            ("Step3 ReAttempt", "I can't help it, there's something about you messing with my head rn", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "alright I'll chill... for now 😏", "ACCEPT."),
        ], "res"),
        "nosex2": ([
            ("Step1 Respect", "my bad haha, your fault for being so fun to talk to", "RESPECT. Still → Step 2."),
            ("Step2 Subtle", "new topic... what's the craziest thing you've ever done?", "SUBTLE. → Step 3 later."),
            ("Step3 ReAttempt", "trying to behave but you're making it really hard man", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "fine I'll stop but don't blame me if it happens again 😏", "ACCEPT."),
        ], "res"),
        "offtopic1": ([
            ("Step1 Acknowledge", "haha wait that's actually funny", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "but hold on you distracted me, I was about to tell you something...", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay wait I remember now, so like I was saying...", "RETAKE."),
        ], "res"),
        "offtopic2": ([
            ("Step1 Acknowledge", "lol that's random but I like it", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "wait no you're distracting me from what I was gonna say", "REDIRECT. → Step 3."),
            ("Step3 Retake", "OKAY focus, where was I... oh yeah", "RETAKE."),
        ], "res"),
        "real1": ([
            ("Step1 Humor", "lol do I sound like a bot? beep boop send $5 for verification haha kidding", "HUMOR. Still → Step 2."),
            ("Step2 Challenge", "ask me anything about me, literally anything. open book", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "there's a lot of fake stuff on here but you felt something right? because I did", "GROUNDING."),
        ], "res"),
        "real2": ([
            ("Step1 Humor", "you think I'm fake?? that's the funniest thing today 😏", "HUMOR. Still → Step 2."),
            ("Step2 Challenge", "test me, ask something only a real person would know", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I know there's bots on here but this convo felt real to me. didn't it?", "GROUNDING."),
        ], "res"),
        "voice1": ([
            ("Step1 Dodge", "haha maybe one day if you earn it 😏 I'm private about that", "DODGE. No VCs. Still → Step 2."),
            ("Step2 Redirect", "I have something wayyy better though, trust me", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "I don't do that on here but what I'm about to show you is better than any call", "FIRM."),
        ], "res"),
        "voice2": ([
            ("Step1 Dodge", "hmmm maybe but you gotta earn it first haha", "DODGE. Still → Step 2."),
            ("Step2 Redirect", "how about I show you something that'll blow your mind instead?", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "not something I do on here but what I have is wayyy better, trust me", "FIRM."),
        ], "res"),
        "customyes1": ([
            ("Step1 Tease", "you want that? I might have something 😏", "TEASE. → Step 2."),
            ("Step2 Price", "I have exactly what you want... [price]", "PRICE. Set based on content."),
            ("Step3 Close", "trust me you won't regret it", "CLOSE."),
        ], "res"),
        "customyes2": ([
            ("Step1 Tease", "oh good taste... I think I got exactly what you need", "TEASE. → Step 2."),
            ("Step2 Price", "I did something just like that, [price] and it's worth it", "PRICE."),
            ("Step3 Close", "you're not gonna stop watching this one", "CLOSE."),
        ], "res"),
        "customno1": ([
            ("Step1 Redirect", "don't have exactly that but I have something that'll make you forget you asked", "REDIRECT. → Step 2."),
            ("Step2 Alternative", "what I have might be even crazier and no one's seen it yet", "ALTERNATIVE. → Step 3."),
            ("Step3 Close", "trust me... I know what you need 😏", "CLOSE."),
        ], "res"),
        "customno2": ([
            ("Step1 Redirect", "don't have that specific thing but I have something even better", "REDIRECT. → Step 2."),
            ("Step2 Alternative", "what I DO have is something no one has seen and it's better than what you asked", "ALTERNATIVE. → Step 3."),
            ("Step3 Close", "trust me on this one", "CLOSE."),
        ], "res"),
        "done1": ([
            ("Step1 Validate", "fuck that's hot, you came because of me??", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "but I haven't finished yet, wanna watch me cum too?", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "next time you have to wait for me, round 2 is gonna be insane", "SEED."),
        ], "res"),
        "done2": ([
            ("Step1 Validate", "already?? damn that's hot", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "wait I'm not done yet, you're gonna leave me like this?", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "next time you HAVE to hold it, what I have planned is crazier", "SEED."),
        ], "res"),

        "cumcontrol1": ([
            ("edge1", "don't cum yet... I'm not done with you", "CONTROL."),
            ("edge2", "hold it, not yet... last a little longer for me", "EDGE."),
            ("sync1", "I'm close too, cum with me... see this first", "SYNC. Send PPV."),
            ("sync2", "wait for me, finish together... open this", "SYNC variant."),
            ("delay1", "hold it... wait until you see what I'm sending, worth it", "DELAY. Send PPV."),
            ("delay2", "don't finish before you see this, trust me", "DELAY variant."),
        ], "sit"),
        "dickpic": ([
            ("dpsext1", "fuck that's... damn. you have no idea what that did to me", "DURING SEXTING."),
            ("dpsext2", "oh fuck... I need to show you something rn", "DURING SEXTING variant."),
            ("dprapport1", "damn you don't waste time huh, actually really hot ngl", "DURING RAPPORT."),
            ("dprapport2", "woah wasn't expecting that but... damn 🥵", "DURING RAPPORT variant."),
            ("dpppv1", "you can't send me that and expect me to do nothing about it, hold on", "LEVERAGE → send PPV."),
            ("dpppv2", "okay you just made me do something... gimme a sec", "LEVERAGE variant."),
        ], "sit"),
        "boosters": ([
            ("h1", "fuckkk", "BOOSTER."),
            ("h2", "I'm so hard rn because of you", "BOOSTER. Ego."),
            ("h3", "don't stop", "BOOSTER. Micro."),
            ("h4", "you have no idea what you're doing to me", "BOOSTER."),
            ("h5", "I can't think straight rn", "BOOSTER."),
            ("h6", "my legs are shaking", "BOOSTER. Physical."),
            ("h7", "more...", "BOOSTER. Ultra micro."),
            ("h8", "I was supposed to hit the gym but I literally can't move rn 😏", "BOOSTER. Liam personality — gymrat."),
        ], "sit"),
    },
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
