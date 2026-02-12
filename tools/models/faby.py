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
    "obj_scripts": {
        # ── PRICE ──
        "price1": ([
            ("Step1 Reframe", "amor that's less than a good churrasco and trust me this will stay with you way longer", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "I'm only in this mood because of YOU right now, and honestly a woman like me doesn't get worked up for just anyone", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "maybe you're just not ready for what I did in this one 😏", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "okay look [lower price] just for you because this connection has been different from the rest", "DOWNGRADE 20-30%. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "it's fine handsome, let's just keep talking... I'm still thinking about you", "SEED. Continue GFE."),
        ], "obj"),
        "price2": ([
            ("Step1 Reframe", "that's less than what you'd spend on a night out and I promise this is going to keep you up thinking about me", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "this mood I'm in won't last forever and I want you to be the one who sees what happens next", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "most guys can't handle a woman like me, I thought you were different", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "fine [lower price] because you make me feel something real, but this stays between us amor", "DOWNGRADE. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "no pressure at all, I genuinely enjoy talking to you", "SEED."),
        ], "obj"),
        # ── DISCOUNT ──
        "discount1": ([
            ("Step1 Firmness", "haha a discount? amor I'm a 45-year-old architect with a lifestyle most people can only dream about. I don't go on sale", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "I only share this with men who truly appreciate what they're getting", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "fine [lower price] just for you because I like you, but this is between us", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "if you don't want it that's okay, I'll save it for someone who does", "TAKEAWAY."),
        ], "obj"),
        "discount2": ([
            ("Step1 Firmness", "a discount? do I look like a woman who gives discounts? 😏", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "the guys who appreciate me never ask for discounts amor, just saying", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "okay [lower price] but ONLY because you make me feel special, one time thing", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "alright I'll keep it for someone who's actually ready for it then", "TAKEAWAY."),
        ], "obj"),
        # ── FREE ──
        "free1": ([
            ("Step1 Reminder", "I already sent you one for free remember? this one is on a completely different level", "REMINDER. Still wants free → Step 2."),
            ("Step2 Challenge", "free? amor I don't just show this to anyone... you have to earn the real stuff", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I literally did this because of what YOU said to me, this wasn't just random content", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "it's okay, I'm not going anywhere... I like talking to you", "SEED."),
        ], "obj"),
        "free2": ([
            ("Step1 Reminder", "you already got one for free and this one is something else entirely", "REMINDER. Still → Step 2."),
            ("Step2 Challenge", "the best things in life aren't free amor, especially not with a woman like me", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I did this because of you specifically, because of what you said to me, that took effort", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "no pressure, I just enjoy this connection honestly", "SEED."),
        ], "obj"),
        # ── NOMONEY ──
        "nomoney1": ([
            ("Step1 Empathy", "hey I totally get it, no pressure at all okay?", "EMPATHY. Still engaged → Step 2."),
            ("Step2 Test", "not even like [small amount]? I really want you to see this one amor", "TEST $3-5. Still no → Step 3."),
            ("Step3 PWYW", "just send whatever you can, even a tiny amount, I just need you to see what you made me do", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "honestly it's fine, I like talking to you regardless... you do something to me", "PROTECT."),
        ], "obj"),
        "nomoney2": ([
            ("Step1 Empathy", "that's totally fine amor, seriously don't worry about it", "EMPATHY. Still → Step 2."),
            ("Step2 Test", "what about just [small amount]? I really don't want you to miss this", "TEST. Still no → Step 3."),
            ("Step3 PWYW", "send whatever feels right, even $1... I can't keep this from you", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "it's completely fine, you being here is what matters to me", "PROTECT."),
        ], "obj"),
        # ── NOPPV ──
        "noppv1": ([
            ("Step1 Accept", "that's totally fine I'm not trying to sell you anything, I'm just enjoying this conversation", "ACCEPT. Continue sexting 4-5 msgs before Step 2."),
            ("Step2 Reframe", "look this isn't about money... I need you to see what you're doing to me right now. a woman like me doesn't react like this to just anyone", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "just send whatever you want, even $1, I can't keep this to myself", "PWYW."),
        ], "obj"),
        "noppv2": ([
            ("Step1 Accept", "no worries at all handsome, I don't care about that I'm just enjoying this", "ACCEPT. Continue 4-5 msgs before Step 2."),
            ("Step2 Reframe", "forget about money for a sec... what I'm feeling right now is real and I want you to see it", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "send me anything, even the smallest amount, I need you to see what you did to me", "PWYW."),
        ], "obj"),
        # ── CARD ──
        "card1": ([
            ("Step1 Retry", "ugh that happens sometimes, try again it usually works the second time", "RETRY. Still fails → Step 2."),
            ("Step2 AltCard", "try a different card? I really don't want you to miss this amor", "ALTERNATIVE. Still fails → Step 3."),
            ("Step3 Urgency", "figure it out soon, I'm in this mood and I don't know how long it's going to last", "URGENCY."),
        ], "obj"),
        "card2": ([
            ("Step1 Retry", "aw that's annoying, happens a lot actually just try one more time", "RETRY. Still fails → Step 2."),
            ("Step2 AltCard", "do you have another card? I really want you to see this", "ALTERNATIVE. Still fails → Step 3."),
            ("Step3 Urgency", "I want you to see this before I change my mind, a woman in this mood doesn't wait around forever 😏", "URGENCY."),
        ], "obj"),

        # ── NOSEX ──
        "nosex1": ([
            ("Step1 Respect", "haha okay I got carried away, you're just so easy to talk to", "RESPECT. Still no → Step 2."),
            ("Step2 Subtle", "so tell me more about you... what do you do when you're not getting a married Brazilian woman all worked up?", "SUBTLE TENSION. → Step 3 later."),
            ("Step3 ReAttempt", "I can't help it, there's something about you that really gets to me", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "okay I'll behave... for now 😏 no promises though", "ACCEPT. Door open."),
        ], "res"),
        "nosex2": ([
            ("Step1 Respect", "my bad I got ahead of myself, it's your fault for being so charming amor", "RESPECT. Still no → Step 2."),
            ("Step2 Subtle", "okay new topic... what's the craziest experience you've ever had?", "SUBTLE. → Step 3 later."),
            ("Step3 ReAttempt", "I'm trying to behave but you're making it impossible, there's just something about you", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "fine I'll stop for now but don't blame me when it comes back 😏", "ACCEPT."),
        ], "res"),
        # ── OFFTOPIC ──
        "offtopic1": ([
            ("Step1 Acknowledge", "haha wait that's actually funny", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "but hold on you totally distracted me, I was about to tell you something good", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay where was I... right", "RETAKE. Resume main script."),
        ], "res"),
        "offtopic2": ([
            ("Step1 Acknowledge", "lol that's random but I like it", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "wait no stop you're distracting me from what I was going to show you", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay focus amor, where was I...", "RETAKE."),
        ], "res"),
        # ── REAL ──
        "real1": ([
            ("Step1 Humor", "lol do I look like a bot to you? I'm a 45-year-old architect from Brazil who should probably be finishing blueprints right now", "HUMOR. Still doubts → Step 2."),
            ("Step2 Challenge", "ask me anything about my life, literally anything. I'm an open book amor", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I get it there's a lot of fake stuff on here, but you felt something in this conversation right? because I definitely did", "GROUNDING."),
        ], "res"),
        "real2": ([
            ("Step1 Humor", "wait you think I'm not real?? that's hilarious. ask my husband, he'll confirm I'm very real 😏", "HUMOR. Still → Step 2."),
            ("Step2 Challenge", "test me handsome, ask me something only a real person would know", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I know there's a lot of bots on here but what we talked about felt real to me. didn't it feel real to you?", "GROUNDING."),
        ], "res"),
        # ── VOICE ──
        "voice1": ([
            ("Step1 Dodge", "haha maybe one day if you earn it but not yet... I'm not there yet amor", "DODGE. No video calls. Still asks → Step 2."),
            ("Step2 Redirect", "I have something way better for you though, trust me", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "I don't do calls on here but what I'm about to show you is better than hearing my voice", "FIRM."),
        ], "res"),
        "voice2": ([
            ("Step1 Dodge", "mmm maybe but you'd have to really earn that first 😏", "DODGE. Still → Step 2."),
            ("Step2 Redirect", "how about instead I show you something that'll blow your mind?", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "that's not something I do on here but trust me what I have for you is worth more than any call", "FIRM."),
        ], "res"),
        # ── CUSTOMYES ──
        "customyes1": ([
            ("Step1 Tease", "oh you want that? mm I think I know exactly what you need", "TEASE. → Step 2."),
            ("Step2 Price", "I have exactly what you're looking for, [price] and it's worth every cent amor", "PRICE. Coordinate with model for scheduling. Same-day delivery usually not possible (3 daughters)."),
            ("Step3 Close", "trust me you won't regret it, I put something really special together for you", "CLOSE."),
        ], "res"),
        "customyes2": ([
            ("Step1 Tease", "ooh you have great taste... I think I know exactly what you need 😏", "TEASE. → Step 2."),
            ("Step2 Price", "I actually know exactly what to do for that, [price] and trust me it's worth it", "PRICE. Coordinate scheduling with model. Plan ahead for delivery."),
            ("Step3 Close", "you're not going to be able to stop watching this one", "CLOSE."),
        ], "res"),
        # ── CUSTOMNO ──
        "customno1": ([
            ("Step1 Redirect", "I don't have exactly that but honestly I have something that'll make you forget you even asked", "REDIRECT. No squirting. Redirect to what she HAS (masturbation, anal, B/G, G/G)."),
            ("Step2 Alternative", "actually what I have might be even hotter and nobody else has seen it", "ALTERNATIVE + FOMO. → Step 3."),
            ("Step3 Close", "trust me amor... a woman with my experience knows exactly what you need 😏", "CLOSE."),
        ], "res"),
        "customno2": ([
            ("Step1 Redirect", "I don't have that specific thing but I have something you're going to love even more", "REDIRECT. → Step 2."),
            ("Step2 Alternative", "what I DO have is something no one has seen and I think it's better than what you asked for", "ALTERNATIVE. → Step 3."),
            ("Step3 Close", "just trust me on this one handsome, I know what I'm doing 😏", "CLOSE."),
        ], "res"),
        # ── DONE ──
        "done1": ([
            ("Step1 Validate", "already?? meu deus that's so hot amor", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "but I haven't finished yet... don't you want to see me cum too?", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "okay but next time you have to wait for me, I have something insane planned", "SEED."),
        ], "res"),
        "done2": ([
            ("Step1 Validate", "already?? fuck that's hot, because of me??", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "wait but I'm not done yet, you're going to leave a woman like me hanging?", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "next time you HAVE to hold on because what I have planned will blow your mind", "SEED."),
        ], "res"),

        # ── SITUATIONAL ──
        "cumcontrol1": ([
            ("edge1", "I can tell you're close... not yet amor, I know what I'm doing", "CONTROL."),
            ("edge2", "a man who can wait gets rewarded gostoso... trust me on that", "EDGE variant."),
            ("sync1", "now we go together amor... I've been holding back too. open this 😏", "SYNC. Send PPV."),
            ("sync2", "I want to feel you let go while I do the same... watch this first", "SYNC variant. Send PPV."),
            ("delay1", "hold it for me... I have years of experience and this next one is my best work", "DELAY. Send PPV."),
            ("delay2", "patience... what's coming is worth every second of waiting", "DELAY variant."),
        ], "sit"),
        "cumcontrol2": ([
            ("edge1", "slow down for me gostoso... I know exactly when to let you go", "CONTROL."),
            ("edge2", "not yet... a little more anticipation makes it so much better, trust me", "EDGE variant."),
            ("sync1", "okay amor... let's both let go right now. open this 😏", "SYNC. Send PPV."),
            ("sync2", "I'm ready when you are... but see this first", "SYNC variant."),
            ("delay1", "one more for you before we're done... this is the one I'm most proud of", "DELAY. Send PPV."),
            ("delay2", "save it for this last one amor, I promise you it's going to be worth it 😏", "DELAY variant."),
        ], "sit"),
        "dickpic": ([
            ("dpsext1", "fuck... okay that's hot. meu deus you have no idea what that just did to me", "DURING SEXTING."),
            ("dpsext2", "oh wow... que delicia. I need to show you something right now", "DURING SEXTING variant."),
            ("dprapport1", "wow you're bold huh? that's actually really hot, I'll give you that 😏", "DURING RAPPORT."),
            ("dprapport2", "woah I was not expecting that but... my husband isn't the only one who can impress me apparently", "DURING RAPPORT variant. Swinger angle."),
            ("dpppv1", "you can't just send me that and expect me to sit still, hold on", "LEVERAGE → send PPV."),
            ("dpppv2", "okay you just did something to me... give me a sec amor", "LEVERAGE variant."),
        ], "sit"),
        "boosters": ([
            ("h1", "fuckkk", "MID-SEXTING BOOSTER."),
            ("h2", "I'm so wet right now because of you", "BOOSTER. Ego."),
            ("h3", "don't stop", "BOOSTER. Micro."),
            ("h4", "you have no idea what you're doing to me", "BOOSTER."),
            ("h5", "I literally can't concentrate on anything", "BOOSTER."),
            ("h6", "meu deus my whole body is trembling", "BOOSTER. Physical + Portuguese."),
            ("h7", "more...", "BOOSTER. Ultra micro."),
            ("h8", "a married architect shouldn't be this turned on in the middle of the day but here I am 😏", "BOOSTER. Faby personality — MILF/swinger angle."),
        ], "sit"),
    },
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
