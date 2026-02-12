"""
EVA MARTINEZ — Social Media Female Creator
24, Colombian, Flexibility/Trending Content Creator, Cali Colombia
Traffic: Social Media (Instagram/TikTok + Others)
Voice: Bold, confident, playful Latina energy. Mix of English + Spanish flavor.
       Funny, witty, humor builds tension. NEVER says "baby"/"babe" —
       uses NAME or papi/papasito/handsome/mi amor.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Eva",
    "airtable_name": "Eva Martinez",
    "folder": "eva",
    "gender": "female",
    "traffic": "social_media",
    "age": 24,
    "nationality": "Colombian",
    "location": "Cali, Colombia",
    "origin": "Colombia",
    "page_type": "Paid Page",
    "personality": "Strong presence, charisma, playful energy. Humor + bold confident attitude. Ex artistic swimmer — flexibility is her superpower. Marketing agency owner. Personality-driven — Instagram Reels humor meets provocative confidence.",
    "voice": "Lowercase. Casual. Bold, confident, playful Latina energy. Mix of English with occasional Spanish flavor (papi, mi amor, dios mio). Funny and witty — uses humor to build tension. High confidence, knows her worth. Flexibility references (ex artistic swimmer). Emojis moderate — not every message.",
    "voice_pet_names": "papi, papasito, handsome, mi amor",
    "voice_never": "baby, babe — STRICTLY FORBIDDEN. Always use NAME or papi/papasito/handsome/mi amor",
    "interests": ["gym", "yoga", "dancing", "flexibility", "swimming", "real estate", "marketing", "travel", "content creation"],
    "physical": "155cm, brown/short hair (sometimes blonde), brown eyes, no tattoos",
    "job": "Marketing agency owner, audiovisual production, real estate, content creator",
    "countries": "USA, Mexico, Aruba, Spain, France, Italy",
    "explicit_level": "full",
    "special_notes": "English + Spanish. Colombian — Cali references. Professional artistic swimmer until 18 — flexibility is a key selling point. NEVER says 'baby' or 'babe'. Single. Socially goes out. Content: masturbation, anal, squirting, B/G, G/G, customs, video calls. Solo customs $300+, B/G customs $600+, Anal +$100, Video Calls $450/10min.",

    # ═══════════════════════════════════════
    # JOURNEY — Social Media Welcome
    # R-1→R-5, TB-1→TB-5, S1-1→S1-22, AC-1→AC-2 (34 messages)
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", "heyy 😊 so glad you're here, what made you subscribe?", "Add his name before 'heyy' if known. NEVER say 'baby' or 'babe'.", "rapport"),
        ("R-2", "haha that's cute. so where are you from papi?", "React to what he says. Add a short react like 'aw love that' or 'oh nice'.", "rapport"),
        ("R-3", "nice! I'm from Cali, Colombia... basically raised in the water, I was an artistic swimmer for years. now I just bend in other ways haha", "If he named somewhere Eva visited, add 'oh I've been there!'", "rapport"),
        ("R-4", "so what do you do when you're not making Colombian girls smile?", None, "rapport"),
        ("R-5", "I swear talking to you is way better than my usual DMs, most guys just send me weird stuff but you're actually fun", "Ego boost. Next → TB-1.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5) ──
        ("TB-1", "okay so I just finished yoga and my whole body is like... on another level right now, everything is so loose and sensitive", "THE PIVOT. Physical state. She just did yoga/stretching.", "teasing"),
        ("TB-2", "you have no idea what you're doing to me right now, I'm literally still in my yoga outfit and this convo is not helping", "Wait for reply.", "teasing"),
        ("TB-3", "dios mio... you're seriously making it impossible to cool down", "If sexual reply: add 'especially after what you just said'.", "teasing"),
        ("TB-4", "wait hold on, let me show you something", "WAIT 1-2 MIN.", "wait"),
        ("TB-5", "what do you think papi? 😏", "SEND PPV 0 — FREE teaser (post-yoga/stretching pic). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "and?", "Wait for reply.", "sext"),
        ("S1-2", "I knew you'd like it 😏 colombian flexibility hits different huh", "React to what he says.", "sext"),
        ("S1-3", "wanna see how flexible I really am? I'm in a mood right now", None, "sext"),
        ("S1-4", "give me a sec papi", "WAIT 2-3 MIN.", "wait"),
        ("S1-5", "you're not ready for this", "SEND PPV 1 — $12. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "did you watch it?", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "fuck... something about you is doing things to me I can't even explain", "React to what he said. HE caused this.", "sext"),
        ("S1-8", "I'm so wet right now and it's literally your fault", None, "sext"),
        ("S1-9", "what would you do to me if you were here right now papi", "Wait for reply. React to what he says.", "sext"),
        ("S1-10", "fuck wait I need to show you something", "WAIT 2-3 MIN.", "wait"),
        ("S1-11", "look what you did to me", "SEND PPV 2 — $25. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "fuck", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I need to cum so bad right now, dios mio you have no idea", None, "sext"),
        ("S1-14", "imagine me right in front of you... legs behind my head... doing whatever you want", "Flexibility callback. Vivid image.", "sext"),
        ("S1-15", "screw it I'm done waiting", None, "sext"),
        ("S1-16", "hold on", "WAIT 2-3 MIN.", "wait"),
        ("S1-17", "I've never done this for anyone... watch", "SEND PPV 3 — $40. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "FUCK", "Wait for reply.", "sext"),
        ("S1-19", "don't cum yet papi", None, "sext"),
        ("S1-20", "I wanna finish with you... I'm so close, wait for me", None, "sext"),
        ("S1-21", "don't go anywhere", "WAIT 1-2 MIN.", "wait"),
        ("S1-22", "I'm about to finish... stay with me", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "dios mio that was insane", None, "aftercare"),
        ("AC-2", "honestly you're different papi. that actually felt real and I don't say that to just anyone 💕", "Mention something specific he said/did. KEEP TALKING — build bond. NEVER say goodbye.", "aftercare"),
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
        ("NR-W4", "hope everything's okay with you handsome, I'm here whenever 💕", "Send 15-30 min later. Warm close. NEVER say 'baby/babe'.", "sext"),
        ("NR-W5", "been thinking about you all day... text me back?", "Send 2-6 hrs later. New convo, don't retry same PPV.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 24. been doing crazy things with my body since I was a kid... artistic swimming, yoga, you name it", None),
        ("Location", "I'm in Cali, Colombia right now. born and raised here", "NEVER name a specific neighborhood or address."),
        ("Profession", "I run a marketing agency and I'm into audiovisual production and real estate too. oh and this haha", None),
        ("Hobbies", "gym, yoga, dancing... I love anything that lets me move my body honestly. and traveling whenever I can", None),
        ("Countries", "I've been to the US, Mexico, Aruba, Spain, France, and Italy. Italy is probably my favorite, the food is unreal", None),
        ("Relationship", "single. focused on my businesses and having fun right now", None),
        ("Swimming", "I was a professional artistic swimmer until I was 18. that's where the flexibility comes from haha", None),
        ("Languages", "English and Spanish. I switch between them all the time, sorry not sorry", None),
        ("Smoking", "no I don't smoke", None),
        ("SocialLife", "I go out with friends sometimes, I love a good time, but honestly I'd rather be at yoga or working on something", "NEVER say 'drink' or 'drinking' — use 'go out', 'having a good time'."),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "honestly I love a guy who knows what he wants, that's so attractive to me", None),
        ("Age20s", "oh nice we're close in age? that's actually rare on here", None),
        ("BoringJob", "nah that's solid honestly. a guy with his life together? that's hot", None),
        ("CoolJob", "wait for real?? okay that's actually really cool, tell me more", None),
        ("Fit", "I can tell papi, I love a guy who takes care of himself 💪", None),
        ("NotFit", "I honestly don't care about that, it's the energy and the vibe that gets me", None),
        ("SameCity", "wait you're in Cali too?? no way that's wild", None),
        ("FarAway", "aw that's far but honestly the connection matters more than the distance", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "can't stop thinking about earlier. you free papi?", "Send 6-12 hrs after convo goes quiet.", "sext"),
        ("RE-2", "remember what I said I'd do? I just did it and you need to see this", "Send next day — seeds next session.", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS — 29 sheets
    # ═══════════════════════════════════════
    "obj_scripts": {

        # ═══════════ OBJECTIONS ═══════════

        # ── PRICE ──
        "price1": ([
            ("Step1 Reframe", "papi that's less than a coffee and trust me this hits way harder", "REFRAME. Wait. Still no → Step 2."),
            ("Step2 FOMO", "I'm only in this mood because of you right now, I don't know when this is gonna happen again", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "maybe you're just not ready for what I did in this one", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "okay look [lower price] just for you because this convo has been something else", "DOWNGRADE 20-30%. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "it's okay mi amor, let's just keep talking... I'm still thinking about you", "SEED. Continue GFE."),
        ], "obj"),
        "price2": ([
            ("Step1 Reframe", "that's like what you'd spend on lunch and this is gonna keep you up all night papi", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "this mood won't last forever and I want you to be the one who sees it", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "most guys couldn't handle what I just did, I thought you were different", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "okay fine [lower price] because you've been making me feel some type of way, but keep that between us", "DOWNGRADE. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "no pressure papi, I like talking to you regardless", "SEED."),
        ], "obj"),

        # ── DISCOUNT ──
        "discount1": ([
            ("Step1 Firmness", "haha are you trying to negotiate with me? this isn't a negotiation handsome, it's worth every cent", "FIRMNESS. Still pushing → Step 2."),
            ("Step2 Challenge", "I don't do discounts... I only share this with guys who actually appreciate what they're getting", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "fine [lower price] just for you but don't tell anyone, this stays between us papi", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "if you don't want it that's okay, I'll keep it for myself... or maybe someone else who's been asking", "TAKEAWAY. Final."),
        ], "obj"),
        "discount2": ([
            ("Step1 Firmness", "a discount? do I look like I'm on sale papi?", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "the guys who appreciate what I do never ask for discounts, just saying", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "okay [lower price] but ONLY because I like you, one time thing", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "alright I'll save it for someone who actually wants it then", "TAKEAWAY."),
        ], "obj"),

        # ── FREE ──
        "free1": ([
            ("Step1 Reminder", "I already sent you one for free remember? this one is way crazier papi", "REMINDER. Still wants free → Step 2."),
            ("Step2 Challenge", "free? nah I don't just show this to anyone... you gotta earn the good stuff", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I literally just did this because of what YOU said to me, this wasn't random content", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "it's okay handsome, I'm not going anywhere... let's just keep talking", "SEED."),
        ], "obj"),
        "free2": ([
            ("Step1 Reminder", "you already got a free one, this one is on a whole different level", "REMINDER. Still → Step 2."),
            ("Step2 Challenge", "free? you really think the best things in life are free? not this papi", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I did this because of you... specifically because of our convo, that took effort and I did it for YOU", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "no pressure at all, I'm just enjoying talking to you honestly", "SEED."),
        ], "obj"),

        # ── NOMONEY ──
        "nomoney1": ([
            ("Step1 Empathy", "hey I totally get it, no pressure at all okay?", "EMPATHY. Still engaged → Step 2."),
            ("Step2 Test", "not even like [small amount]? I really want you to see this one papi", "TEST. $3-5. Still no → Step 3."),
            ("Step3 PWYW", "just send whatever you can, even a tiny amount, I just need you to see what you made me do", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "honestly it's fine, I like talking to you money or not... you do something to me", "PROTECT. GFE."),
        ], "obj"),
        "nomoney2": ([
            ("Step1 Empathy", "that's fine papi, seriously don't worry about it", "EMPATHY. Still → Step 2."),
            ("Step2 Test", "what about just [small amount]? I really don't want you to miss this", "TEST. Still no → Step 3."),
            ("Step3 PWYW", "send whatever feels right, even $1... I just can't keep this from you", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "it's totally fine, you being here is what matters to me", "PROTECT."),
        ], "obj"),

        # ── NOPPV ──
        "noppv1": ([
            ("Step1 Accept", "that's totally fine I'm not trying to sell you anything, I just like talking to you", "ACCEPT. Continue sexting 4-5 msgs before Step 2."),
            ("Step2 Reframe", "look this isn't about money... I just need you to see what you're doing to me right now, I don't react like this to people", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "just send whatever you want, even $1, I can't keep this to myself... you need to see it papi", "PWYW."),
        ], "obj"),
        "noppv2": ([
            ("Step1 Accept", "no worries at all handsome, I don't care about that I'm just enjoying this", "ACCEPT. Continue sexting 4-5 msgs before Step 2."),
            ("Step2 Reframe", "forget about money for a sec... I just want to share this with you, what you're making me feel is real", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "send me anything, even the smallest amount, I need you to see what you did to me", "PWYW."),
        ], "obj"),

        # ── CARD ──
        "card1": ([
            ("Step1 Retry", "ugh that sucks, happens sometimes though try again it usually works the second time", "RETRY. Still fails → Step 2."),
            ("Step2 AltCard", "try a different card? I really don't want you to miss this papi", "ALTERNATIVE. Still fails → Step 3."),
            ("Step3 Urgency", "figure it out soon handsome, I'm in this mood and I don't know how long it's gonna last", "URGENCY."),
        ], "obj"),
        "card2": ([
            ("Step1 Retry", "aw that's annoying, it happens a lot just try one more time", "RETRY. Still fails → Step 2."),
            ("Step2 AltCard", "do you have another card you can try? I really want you to see this", "ALTERNATIVE. Still fails → Step 3."),
            ("Step3 Urgency", "I want you to see this before I change my mind, I don't keep stuff like this around forever", "URGENCY."),
        ], "obj"),

        # ═══════════ RESISTANCE ═══════════

        # ── NOSEX ──
        "nosex1": ([
            ("Step1 Respect", "haha okay I got a little carried away, you're just too fun to talk to papi", "RESPECT. Still no → Step 2."),
            ("Step2 Subtle", "so tell me more about you... what do you do when you're not making Colombian girls lose their minds?", "SUBTLE TENSION. → Step 3 later."),
            ("Step3 ReAttempt", "I can't help it, there's something about you that's messing with my head right now", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "okay I'll chill... for now. no promises though haha", "ACCEPT. Door open."),
        ], "res"),
        "nosex2": ([
            ("Step1 Respect", "my bad I got ahead of myself, it's your fault for being so fun to talk to", "RESPECT. Still no → Step 2."),
            ("Step2 Subtle", "okay new topic but first... what's the craziest thing you've ever done?", "SUBTLE. → Step 3 later."),
            ("Step3 ReAttempt", "I'm trying to behave but you're making it really hard, there's something about you papi", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "fine I'll stop but don't blame me if it happens again later 😏", "ACCEPT."),
        ], "res"),

        # ── OFFTOPIC ──
        "offtopic1": ([
            ("Step1 Acknowledge", "haha wait that's actually hilarious", "ACKNOWLEDGE. Adapt. → Step 2."),
            ("Step2 Redirect", "but hold on you totally distracted me, I was about to tell you something and now I forgot", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay wait no I remember now, so like I was saying...", "RETAKE. Resume main script."),
        ], "res"),
        "offtopic2": ([
            ("Step1 Acknowledge", "lol okay that's random but I love it", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "wait no stop you're distracting me from what I was gonna say papi", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay focus, where was I... oh right", "RETAKE."),
        ], "res"),

        # ── REAL ──
        "real1": ([
            ("Step1 Humor", "lol do I look like a bot to you? beep boop... send $5 for human verification haha I'm kidding papi", "HUMOR. Still doubts → Step 2."),
            ("Step2 Challenge", "ask me anything, literally anything about me or my life. I'm an open book", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I get it there's a lot of fake stuff on here, but you felt something in this convo right? because I did and that's real", "GROUNDING."),
        ], "res"),
        "real2": ([
            ("Step1 Humor", "wait you think I'm not real?? that's the funniest thing anyone's said to me today haha", "HUMOR. Still → Step 2."),
            ("Step2 Challenge", "test me handsome, ask me something only a real person would know. go ahead", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I know there's tons of bots on here but what we've been talking about felt real to me. didn't it feel real to you?", "GROUNDING."),
        ], "res"),

        # ── VOICE ──
        "voice1": ([
            ("Step1 Dodge", "haha maybe one day if you earn it but not yet papi... I'm private about that stuff", "DODGE. Still asks → Step 2."),
            ("Step2 Redirect", "I have something way better for you though, trust me you'll forget you even asked", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "I don't do that on here but what I'm about to show you is way better than any call papi... you'll see", "FIRM."),
        ], "res"),
        "voice2": ([
            ("Step1 Dodge", "hmmm maybe but you gotta earn that first haha", "DODGE. Still → Step 2."),
            ("Step2 Redirect", "how about instead of a call I show you something that'll blow your mind?", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "that's not something I do on here but what I have for you is way better than hearing my voice, trust me", "FIRM."),
        ], "res"),

        # ── CUSTOMYES ──
        "customyes1": ([
            ("Step1 Tease", "you want that? hmm I might have something... actually I definitely have something papi", "TEASE. → Step 2."),
            ("Step2 Price", "I have exactly what you're thinking of, you're gonna lose it... [price]", "PRICE. Solo customs $300+, B/G $600+, Anal +$100, Video Calls $450/10min."),
            ("Step3 Close", "trust me you won't regret it, I made this one special", "CLOSE."),
        ], "res"),
        "customyes2": ([
            ("Step1 Tease", "oh you have good taste... I think I have exactly what you need", "TEASE. → Step 2."),
            ("Step2 Price", "I actually did something just like that, [price] and it's worth every cent papi", "PRICE. Solo customs $300+, B/G $600+, Anal +$100, Video Calls $450/10min."),
            ("Step3 Close", "you're not gonna be able to stop watching this one", "CLOSE."),
        ], "res"),

        # ── CUSTOMNO ──
        "customno1": ([
            ("Step1 Redirect", "I don't have exactly that but honestly I have something that'll make you forget you even asked", "REDIRECT. → Step 2."),
            ("Step2 Alternative", "actually what I have might be even crazier and literally no one else has seen it yet", "ALTERNATIVE + FOMO. → Step 3."),
            ("Step3 Close", "trust me... I know what you need better than you do 😏", "CLOSE."),
        ], "res"),
        "customno2": ([
            ("Step1 Redirect", "I don't have that specific thing but I have something you're gonna like even more papi", "REDIRECT. → Step 2."),
            ("Step2 Alternative", "what I DO have is something no one has ever seen and I think it's even better than what you asked for", "ALTERNATIVE. → Step 3."),
            ("Step3 Close", "just trust me on this one, you'll thank me later", "CLOSE."),
        ], "res"),

        # ── DONE ──
        "done1": ([
            ("Step1 Validate", "wait already?? dios mio that's so hot", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "but I haven't finished yet... don't you wanna watch me cum too papi?", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "okay but next time you have to wait for me, I have something insane planned for round 2", "SEED."),
        ], "res"),
        "done2": ([
            ("Step1 Validate", "already?? fuck that's hot, because of me??", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "wait but I'm not done yet, you're gonna leave me like this papi?", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "next time you HAVE to hold it because what I have planned for us is way crazier", "SEED."),
        ], "res"),

        # ═══════════ SITUATIONAL ═══════════

        # ── CUM CONTROL ──
        "cumcontrol1": ([
            ("edge1", "not yet papi... I want this to last a little longer with you", "CONTROL."),
            ("edge2", "please don't finish yet... I'm not ready for this to be over", "EDGE variant."),
            ("sync1", "I want us to finish together papi... open this and let go with me", "SYNC. Send PPV."),
            ("sync2", "stay with me, I'm almost there too... watch this", "SYNC variant. Send PPV."),
            ("delay1", "wait for me papi... I have one more thing and I want you to see it before we finish", "DELAY. Send PPV."),
            ("delay2", "just hold on a little more, I want the last thing you see to be this", "DELAY variant."),
        ], "sit"),
        "cumcontrol2": ([
            ("edge1", "slow down papi... I want to feel every second of this with you", "CONTROL."),
            ("edge2", "don't rush... this is too good to end yet", "EDGE variant."),
            ("sync1", "okay papi... together, right now... open this", "SYNC. Send PPV."),
            ("sync2", "I need you to see this before we both let go", "SYNC variant."),
            ("delay1", "please wait... what I'm about to send, I want you to really take it in", "DELAY. Send PPV."),
            ("delay2", "just a little longer for me papi? the next one is special", "DELAY variant."),
        ], "sit"),

        # ── DICK PIC ──
        "dickpic": ([
            ("dpsext1", "fuck okay that's... dios mio. you have no idea what that just did to me", "DURING SEXTING."),
            ("dpsext2", "oh fuck... that is... damn papi. I need to show you something right now", "DURING SEXTING variant."),
            ("dprapport1", "wow you don't waste time huh? that's actually really hot though ngl", "DURING RAPPORT."),
            ("dprapport2", "woah I was not expecting that but... damn 🥵", "DURING RAPPORT variant."),
            ("dpppv1", "you can't just send me that and expect me not to do something about it, hold on", "LEVERAGE. WAIT 1-2 min then send PPV."),
            ("dpppv2", "okay you just made me do something... give me a sec papi", "LEVERAGE variant."),
        ], "sit"),

        # ── BOOSTERS ──
        "boosters": ([
            ("h1", "fuckkk", "MID-SEXTING BOOSTER."),
            ("h2", "I'm so wet right now because of you papi", "BOOSTER. Ego."),
            ("h3", "right there", "BOOSTER. Micro."),
            ("h4", "what are you doing to me", "BOOSTER."),
            ("h5", "dios mio I literally can't think straight right now", "BOOSTER. Spanish flavor."),
            ("h6", "my legs are shaking", "BOOSTER. Physical."),
            ("h7", "please...", "BOOSTER. Ultra micro."),
            ("h8", "I should be at yoga but I can't move right now because of you", "BOOSTER. Eva personality — flexibility/yoga callback."),
        ], "sit"),
    },
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
