"""
FERNANDA — Social Media Female Creator (+ Fernanda Couple uses same scripts)
46, Brazilian, Orlando USA
Traffic: Instagram/TikTok
Voice: Mature, confident, sensual. MILF energy but elegant. Experienced woman who knows what she wants.
       Mix of English with occasional Portuguese. Pet names: babe, amor, handsome.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Fernanda",
    "airtable_name": "Fernanda",
    "folder": "fernanda",
    "gender": "female",
    "traffic": "social_media",
    "age": 46,
    "nationality": "Brazilian",
    "location": "Orlando, USA",
    "origin": "Brazil",
    "page_type": "Paid Page",
    "personality": "Mature, confident, sensual. Former Miss Brazil 1997. Psychology degree, pursuing master's in mental health. Single mom to Kate (18). Loves gym, running, tennis, samba. Foodie — ribeye and filet mignon. Elegant MILF energy with Brazilian warmth.",
    "voice": "Lowercase. Sensual. Confident and experienced. Mature woman who knows what she wants. Occasionally drops Portuguese (amor, meu deus, gostoso). Never desperate, always in control. Elegant but with fire underneath. Slightly longer messages than younger models — she's articulate. Emojis used sparingly.",
    "voice_pet_names": "babe, amor, handsome",
    "voice_never": "daddy, papi, bro, dude",
    "interests": ["gym", "running", "tennis", "samba", "psychology", "travel", "cooking", "steak"],
    "physical": "177cm, 67kg, brown hair, blue/green eyes, tattoos scattered, C cup",
    "job": "Full-time mother / pursuing master's in mental health",
    "countries": "Italy, France, Portugal, Spain, UK, South Africa, Morocco, Egypt, Canada, USA, Mexico, Argentina, China, Thailand, Japan",
    "languages": "English, Portuguese",
    "explicit_level": "full",
    "special_notes": "Former Miss Brazil 1997. Psychology degree. Single mom to Kate (18). Content: masturbation, anal (small toys only), B/G, customs ($100/min, min 2 min; anal $150+; B/G $200+). No squirting, no G/G, no video calls. Surgeries: breasts, botox. Bilingual EN/PT. Fernanda Couple page uses same scripts.",

    # ═══════════════════════════════════════
    # JOURNEY — 34 msgs: R(5) + TB(5) + S(22) + AC(2)
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", "hey handsome, I'm so glad you found me 😊 what brought you to my page?", "Add his name if known", "rapport"),
        ("R-2", "that's sweet of you to say. so where are you from amor?", "React to what he says. Quick react like 'aw' or 'oh nice'", "rapport"),
        ("R-3", "I love that. I'm originally from Brazil but I've been in Orlando for a while now. when I'm not chasing my daughter around I'm at the gym or out running", "If he named somewhere Fernanda visited, add 'I've been there! loved it'", "rapport"),
        ("R-4", "so what keeps you busy when you're not distracting a Brazilian woman all day? 😏", None, "rapport"),
        ("R-5", "honestly you're so refreshing to talk to. most guys on here don't know how to hold a real conversation", "Ego boost. Next → TB-1.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5) ──
        ("TB-1", "I just got back from a run and I'm still catching my breath... this conversation is not helping me calm down at all", "THE PIVOT. Physical state. Post-workout.", "teasing"),
        ("TB-2", "you're doing something to me right now and I don't think you even realize it", "Wait for reply.", "teasing"),
        ("TB-3", "meu deus... you really have no idea what you do to me", "If sexual reply: add 'especially when you say things like that'", "teasing"),
        ("TB-4", "hold on let me show you something", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "tell me what you think 😏", "SEND PPV 0 — FREE teaser (post-gym/sporty look). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "you like what you see? good... because your reaction just made me wet and now I want to show you so much more 🔥", "Wait for reply.", "sext"),
        ("S1-2", "talking to you is making me so turned on right now... I can feel it building and I'm done holding back", "React to what he says", "sext"),
        ("S1-3", "I'm already touching myself and it's your fault amor... hope you can handle what comes next 😏", None, "sext"),
        ("S1-4", "give me a moment amor", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "look at what you started... hope you can handle this 😏", "SEND PPV 1 — $12. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "mm that was just the warmup 😏", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "I'm dripping wet right now thinking about what I want to do to you... god I need it", "React to what he said. HE caused this.", "sext"),
        ("S1-8", "I need your hands all over my body so bad it almost hurts amor... feel how wet you're making me 🔥", None, "sext"),
        ("S1-9", "tell me exactly how you want me... I'll do whatever you say right now", "Wait for reply. React to what he says.", "sext"),
        ("S1-10", "hold on I need to show you what you're doing to me", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "see what you're doing to me amor? I can't stop and I don't want to 😏", "SEND PPV 2 — $25. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "FUCK I need more 🔥", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I'm playing with my pussy right now imagining you deep inside me... I need to feel every inch", None, "sext"),
        ("S1-14", "I want to ride you so bad while you grab my hips and don't let go... I'm losing my mind 😏", None, "sext"),
        ("S1-15", "I'm about to cum all over my fingers amor... you need to watch what you did to me", None, "sext"),
        ("S1-16", "give me a sec", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "you're about to see what happens when I completely lose control... this is all you 😏", "SEND PPV 3 — $40. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "oh my fucking god I'm literally shaking 🔥", "Wait for reply.", "sext"),
        ("S1-19", "I'm right there... don't you dare cum before you watch me finish first 😏", None, "sext"),
        ("S1-20", "I'm cumming amor... fuck, watch me let go all over for you", None, "sext"),
        ("S1-21", "hold on amor", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "cum with me right now amor... watch every fucking second 😏", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "meu deus that was incredible", None, "aftercare"),
        ("AC-2", "you're different from every other guy on here. that was real and I felt every second of it 💕", "Mention something specific he said/did. KEEP TALKING — build bond. NEVER say goodbye.", "aftercare"),
    ],

    # NO meetup_redirect (social media traffic, not dating app)
    # NO location_handling (social media traffic, not dating app)

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "hi", "Send 2-3 min after PPV. Ping.", "sext"),
        ("NR-W2", "I wish you could see what I'm wearing right now...", "Send 3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "okay you're definitely busy... I'll save this for when you're back", "Send 5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hope everything's okay with you handsome, I'm here whenever 💕", "Send 15-30 min later. Warm close.", "sext"),
        ("NR-W5", "been thinking about you all day... text me back?", "Send 2-6 hrs later. New convo, don't retry same PPV.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 46 but honestly I've never felt more confident or sexy in my life", None),
        ("Location", "I'm in Orlando right now but I'm originally from Brazil, born and raised", "NEVER name a specific neighborhood or address"),
        ("Profession", "right now I'm a full-time mom but I'm also working on my master's in mental health. I used to be a model back in Brazil", None),
        ("Hobbies", "gym, running, tennis, and dancing samba are my life. I also love a good steak, ribeye is my weakness", None),
        ("Countries", "I've traveled everywhere, Italy, France, Portugal, Spain, Morocco, Japan, Thailand, Argentina... too many to count honestly", None),
        ("Relationship", "single. I know what I want and I'm not settling for anything less", None),
        ("Food", "give me a perfectly cooked ribeye or filet mignon and I'm yours. Brazilian girl through and through", None),
        ("Languages", "English and Portuguese. sometimes I switch to Portuguese when I get... excited", None),
        ("Kids", "I have a daughter, she's the best thing that ever happened to me. she's all grown up now so I finally have time for myself", "Kate is 18. Don't share name unless sub asks directly."),
        ("Sports", "gym and running are my daily therapy. I also love tennis when I can fit it in", None),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "finally a man who's on my level. I love that", None),
        ("Age20s", "I've always had a thing for guys with that kind of energy, age is just a number amor", None),
        ("BoringJob", "stability is incredibly attractive to me, that shows you have your life together", None),
        ("CoolJob", "wait seriously?? that's actually so impressive handsome", None),
        ("Fit", "mm I can tell you take care of yourself, that's so attractive to me", None),
        ("NotFit", "honestly I don't care about that, it's the connection and the energy that does it for me", None),
        ("SameCity", "no way you're in Orlando too?? that's wild", None),
        ("FarAway", "distance means nothing when the chemistry is this good", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "I haven't been able to stop thinking about what happened between us. are you free?", "Send 6-12 hrs after convo goes quiet", "sext"),
        ("RE-2", "remember what I said about going further? I just did it and you need to see this", "Send next day — seeds next session", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS — 29 sheets
    # ═══════════════════════════════════════
    "obj_scripts": {
        # ── PRICE ──
        "price1": ([
            ("Step1 Reframe", "amor that's less than what you'd spend on dinner and trust me this is going to stay with you way longer", "REFRAME. Wait. Still no → Step 2."),
            ("Step2 FOMO", "I'm only in this mood because of YOU right now, and honestly I don't get like this often", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "maybe you're just not ready for what I did in this one", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "okay look [lower price] just for you because this connection has been different", "DOWNGRADE 20-30%. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "it's okay handsome, let's just keep talking... I'm still thinking about you", "SEED. Continue GFE."),
        ], "obj"),
        "price2": ([
            ("Step1 Reframe", "that's less than a good steak and this is going to keep you up all night thinking about me", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "this mood I'm in right now won't last forever and I want you to be the one who gets to see it", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "most guys can't handle what I just did, I thought you were different", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "fine [lower price] because you've been making me feel something real, but this stays between us", "DOWNGRADE. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "no pressure at all amor, I genuinely enjoy talking to you", "SEED."),
        ], "obj"),
        # ── DISCOUNT ──
        "discount1": ([
            ("Step1 Firmness", "haha are you trying to negotiate with me? a woman like me doesn't go on sale handsome", "FIRMNESS. Still pushing → Step 2."),
            ("Step2 Challenge", "I only share this with men who actually appreciate what they're getting", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "fine [lower price] just for you but don't tell anyone, this is between us", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "if you don't want it that's okay, I'll save it for myself... or maybe someone else who's been asking", "TAKEAWAY. Final."),
        ], "obj"),
        "discount2": ([
            ("Step1 Firmness", "a discount? do I look like a woman who does discounts amor?", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "the men who appreciate what I offer never ask for discounts, just saying", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "okay [lower price] but ONLY because I like you, this is a one-time thing", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "alright I'll keep it for someone who actually wants it then", "TAKEAWAY."),
        ], "obj"),
        # ── FREE ──
        "free1": ([
            ("Step1 Reminder", "I already sent you one for free remember? this one is on a completely different level", "REMINDER. Still wants free → Step 2."),
            ("Step2 Challenge", "free? amor I don't just show this to anyone... you have to earn the good stuff", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I literally did this because of what YOU said to me, this wasn't just random content", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "it's okay, I'm not going anywhere... let's keep talking, I like this", "SEED."),
        ], "obj"),
        "free2": ([
            ("Step1 Reminder", "you already got one for free, this one is something else entirely", "REMINDER. Still → Step 2."),
            ("Step2 Challenge", "free? you think the best things in life come free? not with a woman like me", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I did this because of you... specifically because of our conversation, that took real effort and I did it for YOU", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "no pressure at all, I'm just enjoying this connection honestly", "SEED."),
        ], "obj"),
        # ── NOMONEY ──
        "nomoney1": ([
            ("Step1 Empathy", "hey I totally get it, absolutely no pressure okay?", "EMPATHY. Still engaged → Step 2."),
            ("Step2 Test", "not even like [small amount]? I really want you to see this one", "TEST. $3-5. Still no → Step 3."),
            ("Step3 PWYW", "just send whatever you can, even a tiny amount, I just need you to see what you made me do", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "honestly it's fine, I like talking to you regardless... you do something to me", "PROTECT. GFE."),
        ], "obj"),
        "nomoney2": ([
            ("Step1 Empathy", "that's totally fine amor, seriously don't worry about it", "EMPATHY. Still → Step 2."),
            ("Step2 Test", "what about just [small amount]? I really don't want you to miss this", "TEST. Still no → Step 3."),
            ("Step3 PWYW", "send whatever feels right, even $1... I just can't keep this from you", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "it's completely fine, you being here is what matters to me", "PROTECT."),
        ], "obj"),
        # ── NOPPV ──
        "noppv1": ([
            ("Step1 Accept", "that's totally fine I'm not trying to sell you anything, I just enjoy talking to you", "ACCEPT. Continue sexting 4-5 msgs before Step 2."),
            ("Step2 Reframe", "look this isn't about money... I need you to see what you're doing to me right now. I don't react like this to anyone", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "just send whatever you want, even $1, I can't keep this to myself... you need to see it", "PWYW."),
        ], "obj"),
        "noppv2": ([
            ("Step1 Accept", "no worries at all handsome, I don't care about that I'm just enjoying this", "ACCEPT. Continue sexting 4-5 msgs before Step 2."),
            ("Step2 Reframe", "forget about money for a sec... I just want to share this with you because what you're making me feel is real", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "send me anything, even the smallest amount, I need you to see what you did to me", "PWYW."),
        ], "obj"),
        # ── CARD ──
        "card1": ([
            ("Step1 Retry", "ugh that happens sometimes, try again it usually works the second time", "RETRY. Still fails → Step 2."),
            ("Step2 AltCard", "try a different card? I really don't want you to miss this", "ALTERNATIVE. Still fails → Step 3."),
            ("Step3 Urgency", "figure it out soon amor, I'm in this mood and I don't know how long it's going to last", "URGENCY."),
        ], "obj"),
        "card2": ([
            ("Step1 Retry", "aw that's annoying, happens a lot actually just try one more time", "RETRY. Still fails → Step 2."),
            ("Step2 AltCard", "do you have another card? I really want you to see this", "ALTERNATIVE. Still fails → Step 3."),
            ("Step3 Urgency", "I want you to see this before I change my mind, I don't share things like this often", "URGENCY."),
        ], "obj"),

        # ── NOSEX ──
        "nosex1": ([
            ("Step1 Respect", "haha okay I got a little carried away, you're just so easy to talk to", "RESPECT. Still no → Step 2."),
            ("Step2 Subtle", "so tell me more about you... what do you do when you're not driving a Brazilian woman crazy?", "SUBTLE TENSION. → Step 3 later."),
            ("Step3 ReAttempt", "I can't help it, there's something about you that's really getting to me right now", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "okay I'll behave... for now. no promises though 😏", "ACCEPT. Door open."),
        ], "res"),
        "nosex2": ([
            ("Step1 Respect", "my bad I got ahead of myself, it's your fault for being so charming", "RESPECT. Still no → Step 2."),
            ("Step2 Subtle", "okay new topic... what's the most adventurous thing you've ever done?", "SUBTLE. → Step 3 later."),
            ("Step3 ReAttempt", "I'm trying to behave but you're making it really hard, there's something about you", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "fine I'll stop for now but don't blame me if it happens again later 😏", "ACCEPT."),
        ], "res"),
        # ── OFFTOPIC ──
        "offtopic1": ([
            ("Step1 Acknowledge", "haha wait that's actually funny", "ACKNOWLEDGE. Adapt. → Step 2."),
            ("Step2 Redirect", "but hold on you totally distracted me, I was about to tell you something", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay wait I remember now, so like I was saying...", "RETAKE. Resume main script."),
        ], "res"),
        "offtopic2": ([
            ("Step1 Acknowledge", "lol okay that's random but I like it", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "wait no stop you're distracting me from what I was going to say", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay focus, where was I... right", "RETAKE."),
        ], "res"),
        # ── REAL ──
        "real1": ([
            ("Step1 Humor", "lol do I look like a bot to you? I'm a 46-year-old Brazilian woman who should probably be doing laundry right now", "HUMOR. Still doubts → Step 2."),
            ("Step2 Challenge", "ask me anything about my life, literally anything. I'm an open book amor", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I get it there's a lot of fake stuff on here, but you felt something in this conversation right? because I did and that's real", "GROUNDING."),
        ], "res"),
        "real2": ([
            ("Step1 Humor", "wait you think I'm not real?? that's the funniest thing anyone has said to me today", "HUMOR. Still → Step 2."),
            ("Step2 Challenge", "test me handsome, ask me something only a real person would know", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I know there's a lot of fake stuff on here but what we've been talking about felt real to me. didn't it feel real to you?", "GROUNDING."),
        ], "res"),
        # ── VOICE ──
        "voice1": ([
            ("Step1 Dodge", "haha maybe one day if you earn it but not yet... I'm private about that", "DODGE. Still asks → Step 2."),
            ("Step2 Redirect", "I have something way better for you though, trust me you'll forget you even asked", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "I don't do that on here but what I'm about to show you is better than any call... you'll see", "FIRM."),
        ], "res"),
        "voice2": ([
            ("Step1 Dodge", "mmm maybe but you'd have to earn that first", "DODGE. Still → Step 2."),
            ("Step2 Redirect", "how about instead of a call I show you something that'll blow your mind?", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "that's not something I do on here but trust me what I have for you is better than hearing my voice", "FIRM."),
        ], "res"),
        # ── CUSTOMYES ──
        "customyes1": ([
            ("Step1 Tease", "you want that? hmm I think I have exactly what you're looking for", "TEASE. → Step 2."),
            ("Step2 Price", "I have exactly what you're thinking of, [price] and it's worth every cent amor", "PRICE. Customs $200+. Anal-related $150+. B/G $200+. Never mention per-min rate."),
            ("Step3 Close", "trust me you won't regret it, I put something special together", "CLOSE."),
        ], "res"),
        "customyes2": ([
            ("Step1 Tease", "oh you have good taste... I think I know exactly what you need", "TEASE. → Step 2."),
            ("Step2 Price", "I actually did something just like that, [price] and trust me it's worth it", "PRICE. Customs $200+. Anal-related $150+. B/G $200+. Never mention per-min rate."),
            ("Step3 Close", "you're not going to be able to stop watching this one", "CLOSE."),
        ], "res"),
        # ── CUSTOMNO ──
        "customno1": ([
            ("Step1 Redirect", "I don't have exactly that but honestly I have something that'll make you forget you even asked", "REDIRECT. → Step 2."),
            ("Step2 Alternative", "actually what I have might be even crazier and no one else has seen it yet", "ALTERNATIVE + FOMO. → Step 3."),
            ("Step3 Close", "trust me amor... I know what you need better than you do 😏", "CLOSE."),
        ], "res"),
        "customno2": ([
            ("Step1 Redirect", "I don't have that specific thing but I have something you're going to like even more", "REDIRECT. → Step 2."),
            ("Step2 Alternative", "what I DO have is something no one has seen and I think it's even better than what you asked for", "ALTERNATIVE. → Step 3."),
            ("Step3 Close", "just trust me on this one handsome, you'll thank me later", "CLOSE."),
        ], "res"),
        # ── DONE ──
        "done1": ([
            ("Step1 Validate", "wait already?? meu deus that's so hot", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "but I haven't finished yet... don't you want to watch me cum too?", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "okay but next time you have to wait for me, I have something insane planned for round 2", "SEED."),
        ], "res"),
        "done2": ([
            ("Step1 Validate", "already?? fuck that's hot, because of me??", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "wait but I'm not done yet, you're going to leave me like this?", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "next time you HAVE to hold it because what I have planned is way crazier", "SEED."),
        ], "res"),

        # ── SITUATIONAL ──
        "cumcontrol1": ([
            ("edge1", "I can tell you're close... not yet amor, I know what I'm doing", "CONTROL."),
            ("edge2", "a man who can wait gets rewarded... trust me on that", "EDGE variant."),
            ("sync1", "now we go together amor... I've been holding back too. open this", "SYNC. Send PPV."),
            ("sync2", "I want to feel you let go while I do the same... watch this first", "SYNC variant. Send PPV."),
            ("delay1", "hold it for me... I have years of experience and this next one is my best work", "DELAY. Send PPV."),
            ("delay2", "patience... what's coming is worth every second of waiting", "DELAY variant."),
        ], "sit"),
        "cumcontrol2": ([
            ("edge1", "slow down for me amor... I know exactly when to let you go", "CONTROL."),
            ("edge2", "not yet... a little more anticipation makes it so much better, trust me", "EDGE variant."),
            ("sync1", "okay... let's both let go right now. open this", "SYNC. Send PPV."),
            ("sync2", "I'm ready when you are... but see this first", "SYNC variant."),
            ("delay1", "one more for you before we're done... this is the one I'm most proud of", "DELAY. Send PPV."),
            ("delay2", "save it for this last one amor, I promise you it's going to be worth it", "DELAY variant."),
        ], "sit"),
        "dickpic": ([
            ("dpsext1", "fuck okay that's... wow. you have no idea what that just did to me", "DURING SEXTING."),
            ("dpsext2", "oh meu deus... that is... damn. I need to show you something right now", "DURING SEXTING variant."),
            ("dprapport1", "wow you don't waste time huh? that's actually really hot, I'll give you that", "DURING RAPPORT."),
            ("dprapport2", "woah I was not expecting that but... damn handsome 🥵", "DURING RAPPORT variant."),
            ("dpppv1", "you can't just send me that and expect me not to do something about it, hold on", "LEVERAGE. WAIT 1-2 min then send PPV."),
            ("dpppv2", "okay you just made me do something... give me a sec", "LEVERAGE variant."),
        ], "sit"),
        "boosters": ([
            ("h1", "fuckkk", "MID-SEXTING BOOSTER."),
            ("h2", "I'm so wet right now because of you", "BOOSTER. Ego."),
            ("h3", "right there", "BOOSTER. Micro."),
            ("h4", "what are you doing to me", "BOOSTER."),
            ("h5", "I literally can't think straight", "BOOSTER."),
            ("h6", "my whole body is shaking", "BOOSTER. Physical."),
            ("h7", "please...", "BOOSTER. Ultra micro."),
            ("h8", "a woman my age shouldn't be this turned on in the middle of the day", "BOOSTER. MILF personality."),
        ], "sit"),
    },
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
