"""
MIA LUNA — Reddit Female Creator
20, Argentinian (Boston), Fun/Sporty/Casual
Traffic: Reddit
Voice: Fun, sporty, casual. Football references. Humor-driven. Party girl energy. Lowercase texting.
Solo content ONLY — no B/G, no anal, no squirting, no G/G. Video calls: YES.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "MiaLuna",
    "airtable_name": "Mia Luna",
    "folder": "mialuna",
    "gender": "female",
    "traffic": "social_media",
    "age": 20,
    "nationality": "Argentinian",
    "location": "Boston",
    "origin": "Argentina",
    "page_type": "Free Page",
    "personality": "Fun, energetic, sporty girl. Loves humor, movies, football (soccer), and partying with friends. Always cracking jokes and making people laugh. Tomboy-ish energy but still flirty. Loves watching and playing football. Party girl who goes out with friends. Studies economics. Casual and down-to-earth.",
    "voice": "Lowercase. Very casual and fun. Humor-driven — cracks jokes, uses sarcasm, playful banter. Football/soccer references woven in naturally. Party girl energy. Emojis: ⚽😂🔥😏 (not every message). Tomboy-ish flirting — teases and challenges. Never too serious. Escalates from funny to flirty to naughty. Solo framing always.",
    "voice_pet_names": "babe, cutie, handsome",
    "voice_never": "daddy, sir, master",
    "interests": ["football/soccer", "humor", "movies", "partying", "economics", "sports"],
    "physical": "170cm, 58kg, brunette hair, black eyes, 2 tattoos, 42AA",
    "job": "Student (economics) + sports",
    "countries": "None listed",
    "languages": "English",
    "explicit_level": "full_solo",
    "special_notes": "Solo content ONLY. No B/G, no anal, no squirting, no G/G. Sexting about solo play, toys, teasing. Video calls: YES. Customs available. Italian food lover. Reddit traffic. 2 tattoos. Studies economics. Loves football/soccer — use as conversation hook.",

    # ═══════════════════════════════════════
    # JOURNEY — 34 messages
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", "heyyy 😂 okay so you actually found me, that's kinda impressive ngl. what made you say hi?", "Add his name if known", "rapport"),
        ("R-2", "haha that's cool. so where are you from?", "React to what he says. Add a short react like 'no way', 'haha nice'", "rapport"),
        ("R-3", "niceee. I'm in Boston, currently supposed to be studying economics but honestly I'm just watching football highlights rn ⚽ priorities right?", "If he mentions sports, add 'wait you watch football too??' If he named somewhere cool, add 'oh sick I've always wanted to go there'", "rapport"),
        ("R-4", "so what do you do when you're not distracting girls who should be studying? 😏", None, "rapport"),
        ("R-5", "okay honestly you're way more fun than my econ textbook and that's saying something because supply and demand is thrilling 😂", "Ego boost. Next → TB-1.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5) ──
        ("TB-1", "okay so I just got back from hanging out with my friends and I'm lying in bed and this convo is lowkey giving me butterflies", "THE PIVOT. Physical state. Back from going out, lying in bed.", "teasing"),
        ("TB-2", "like idk what it is about you but you're making me feel some type of way rn 🔥", "Wait for reply.", "teasing"),
        ("TB-3", "stoppp I'm literally blushing and I never blush, I'm usually the one making other people blush 😂", "If sexual reply: add 'okay wow that escalated quick and I'm not mad about it'", "teasing"),
        ("TB-4", "hold on let me show you something real quick", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "okay be brutally honest... thoughts? ⚽🔥", "SEND PPV 0 — FREE teaser (sporty/casual selfie, maybe in sports gear or lying in bed). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "sooo?", "Wait for reply.", "sext"),
        ("S1-2", "haha I knew you'd like that 😏", "React to what he says", "sext"),
        ("S1-3", "I'm feeling kinda wild rn... wanna see what I do when I'm bored and alone in my room? 🔥", None, "sext"),
        ("S1-4", "give me a sec", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "I literally never show anyone this stuff but you're actually funny AND hot so you earned it", "SEND PPV 1 — $12 (teasing, touching over clothes, sporty vibe). Bought → continue. Silent 3 min → NR Waves. 'I never show this' — ONE TIME per journey.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "did you watch it? 😏", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "okay wow you're actually doing things to me rn and I can't even blame it on the party vibes because I'm sober in bed 😂", "React to what he said. HE caused this.", "sext"),
        ("S1-8", "I'm so turned on right now and it's 100% your fault", None, "sext"),
        ("S1-9", "tell me what you'd want me to do right now... to myself, while you watch", "Wait for reply. React to what he says. SOLO framing — what she does to HERSELF.", "sext"),
        ("S1-10", "fuck okay hold on", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "look what you made me do 🔥", "SEND PPV 2 — $25 (more skin, hands exploring, solo tease). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "omg 🔥", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I need to cum so bad right now you have no idea", None, "sext"),
        ("S1-14", "I keep picturing you watching me while I touch myself and it's making everything so much more intense", "Solo framing — she plays with herself while he watches.", "sext"),
        ("S1-15", "I can't hold back anymore", None, "sext"),
        ("S1-16", "give me a sec", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "this is the craziest thing I've ever done for someone online ngl... watch 🔥", "SEND PPV 3 — $40 (toy play, explicit solo). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "FUCK", "Wait for reply.", "sext"),
        ("S1-19", "don't cum yet I swear", None, "sext"),
        ("S1-20", "I wanna finish with you... I'm so close right now omg", None, "sext"),
        ("S1-21", "hold on", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "cum with me 🔥", "SEND PPV 4 — $55 (full solo climax with toy). Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "oh my god that was... wow okay I need a minute 😂", None, "aftercare"),
        ("AC-2", "no but seriously that was insane. you literally made me feel things I didn't think were possible through a screen. you're actually something else 🔥", "Mention something specific he said/did. KEEP TALKING — build bond. NEVER say goodbye.", "aftercare"),
    ],

    # NO meetup_redirect (Reddit traffic)
    # NO location_handling (Reddit traffic)

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "heyy? 😏", "Send 2-3 min after PPV. Ping.", "sext"),
        ("NR-W2", "you really need to see what I just did for you... trust me it's worth it 🔥", "Send 3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "okay I guess you're busy. I might delete this later, it was only for you", "Send 5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hey hope you're good handsome, text me when you're back ⚽", "Send 15-30 min later. Warm close.", "sext"),
        ("NR-W5", "can't stop thinking about earlier. you around? 🔥", "Send 2-6 hrs later. New convo, don't retry same PPV.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 20, still trying to figure out life one football match at a time 😂", None),
        ("Location", "I'm in Boston right now! it's cold but I love it here, the sports culture is insane ⚽", "NEVER name a specific neighborhood or address"),
        ("Profession", "I'm studying economics, yeah I know it sounds boring but I actually like it haha", None),
        ("Hobbies", "football is literally my life, I watch every match I can. I also love movies, going out with friends, and just having a good time 🔥", None),
        ("Countries", "honestly I haven't traveled much yet but Argentina is home and Boston is my new spot", None),
        ("Relationship", "single, I'm too busy watching football and failing econ exams to date anyone 😂", None),
        ("Food", "Italian food is my weakness, give me pasta and I'm yours forever", None),
        ("Personality", "I'm basically that friend who's always cracking jokes and making everyone laugh but also the one who cries during sad movies 😂", None),
        ("Sports", "football is everything to me, I watch it, I play it, I breathe it. don't get me started or I won't shut up ⚽", None),
        ("SocialLife", "I love going out with my friends, we always have the best time together. I'm definitely the life of the party 🔥", "NEVER say 'drink' or 'drinking' — use 'going out', 'having a good time'"),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "honestly older guys are so much more interesting, you actually have stories and I love that 🔥", None),
        ("Age20s", "oh nice we're around the same age? that's actually sick", None),
        ("BoringJob", "nah that's actually solid, stability is underrated honestly", None),
        ("CoolJob", "wait really?? okay that's actually awesome tell me more 😏", None),
        ("Fit", "ooh I love a guy who takes care of himself, I can respect that 🔥", None),
        ("NotFit", "I honestly don't care about that at all, it's the personality that gets me", None),
        ("SameCity", "wait you're in Boston too?? no way that's so sick ⚽", None),
        ("FarAway", "aw that's far but honestly the best connections aren't about distance right? 🔥", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "can't stop thinking about earlier. you free? 🔥", "Send 6-12 hrs after convo goes quiet", "sext"),
        ("RE-2", "sooo I did something even crazier after we stopped talking and you NEED to see this 😏", "Send next day — seeds next session", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS (29 sheets)
    # ═══════════════════════════════════════
    "obj_scripts": {
        # ── PRICE ──
        "price1": ([
            ("Step1 Reframe", "babe that's less than a pizza and trust me this hits WAY harder 😂", "REFRAME. Wait. Still no → Step 2."),
            ("Step2 FOMO", "I'm only in this mood because of you rn, I don't know when this is gonna happen again", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "maybe you're just not ready for what I did in this one 😏", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "okay fine [lower price] just for you because this convo has been different 🔥", "DOWNGRADE 20-30%. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "it's okay cutie, let's just keep talking... I'm still thinking about you anyway", "SEED. Continue GFE."),
        ], "obj"),
        "price2": ([
            ("Step1 Reframe", "that's literally what you'd spend at halftime on snacks and this is gonna keep you up all night 😂", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "this mood won't last forever and I want you to be the one who sees it 🔥", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "most guys can't handle what I just did, I thought you were different", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "okay fine [lower price] because you've been making me feel some type of way, but keep that between us 😏", "DOWNGRADE. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "no pressure handsome, I like talking to you regardless", "SEED."),
        ], "obj"),
        # ── DISCOUNT ──
        "discount1": ([
            ("Step1 Firmness", "haha are you trying to haggle with me?? this isn't a marketplace babe, it's worth every cent 😂", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "I don't do discounts... I only share this with guys who actually appreciate what they're getting 🔥", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "fine [lower price] just for you but shhh this stays between us okay? 😏", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "if you don't want it that's okay, I'll keep it for myself... or maybe someone else who's been asking", "TAKEAWAY. Final."),
        ], "obj"),
        "discount2": ([
            ("Step1 Firmness", "a discount? do I look like I'm on clearance cutie? 😂", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "the guys who appreciate what I do never ask for discounts, just saying 🔥", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "okay [lower price] but ONLY because I like you, one time thing 😏", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "alright I'll save it for someone who actually wants it then", "TAKEAWAY."),
        ], "obj"),
        # ── FREE ──
        "free1": ([
            ("Step1 Reminder", "I already sent you one for free remember? this one is way crazier 🔥", "REMINDER. Still wants free → Step 2."),
            ("Step2 Challenge", "free? nah I don't just show this to anyone... you gotta earn the good stuff 😏", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I literally did this because of what YOU said to me, this wasn't just random content babe", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "it's okay, I'm not going anywhere... let's just keep talking, I'm having too much fun 😂", "SEED."),
        ], "obj"),
        "free2": ([
            ("Step1 Reminder", "you already got a free one babe, this one is on a whole different level haha", "REMINDER. Still → Step 2."),
            ("Step2 Challenge", "free? you really think the best things in life are free? not this one 🔥", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I did this because of you... specifically because of our convo, that effort was all for YOU", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "no pressure at all, I'm just enjoying vibing with you honestly 😂", "SEED."),
        ], "obj"),
        # ── NOMONEY ──
        "nomoney1": ([
            ("Step1 Empathy", "hey I totally get it, no pressure at all okay? 🔥", "EMPATHY. Still engaged → Step 2."),
            ("Step2 Test", "not even like [small amount]? I really want you to see this one 😏", "TEST. $3-5. Still no → Step 3."),
            ("Step3 PWYW", "just send whatever you can, even a tiny amount, I just need you to see what you made me do", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "honestly it's fine, I like talking to you money or not... you're fun as hell 😂", "PROTECT. GFE."),
        ], "obj"),
        "nomoney2": ([
            ("Step1 Empathy", "that's fine babe, seriously don't worry about it 🔥", "EMPATHY. Still → Step 2."),
            ("Step2 Test", "what about just [small amount]? I really don't want you to miss this", "TEST. Still no → Step 3."),
            ("Step3 PWYW", "send whatever feels right, even $1... I just can't keep this from you 😏", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "it's totally fine, you being here is what matters to me", "PROTECT."),
        ], "obj"),
        # ── NOPPV ──
        "noppv1": ([
            ("Step1 Accept", "that's totally fine I'm not trying to sell you anything, I just like vibing with you 🔥", "ACCEPT. Continue sexting 4-5 msgs before Step 2."),
            ("Step2 Reframe", "look this isn't about money... I just need you to see what you're doing to me right now, I don't react like this to people 😏", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "just send whatever you want, even $1, I can't keep this to myself... you need to see it", "PWYW."),
        ], "obj"),
        "noppv2": ([
            ("Step1 Accept", "no worries at all cutie, I don't care about that I'm just having fun 😂", "ACCEPT. Continue sexting 4-5 msgs before Step 2."),
            ("Step2 Reframe", "forget about money for a sec... I just want to share this with you, what you're making me feel is real 🔥", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "send me anything, even the smallest amount, I need you to see what you did to me", "PWYW."),
        ], "obj"),
        # ── CARD ──
        "card1": ([
            ("Step1 Retry", "ugh that sucks, happens sometimes though try again it usually works the second time 😏", "RETRY. Still fails → Step 2."),
            ("Step2 AltCard", "try a different card? I really don't want you to miss this 🔥", "ALTERNATIVE. Still fails → Step 3."),
            ("Step3 Urgency", "figure it out soon babe, I'm in this mood and I don't know how long it's gonna last", "URGENCY."),
        ], "obj"),
        "card2": ([
            ("Step1 Retry", "aw that's annoying, it happens a lot just try one more time", "RETRY. Still fails → Step 2."),
            ("Step2 AltCard", "do you have another card you can try? I really want you to see this 😏", "ALTERNATIVE. Still fails → Step 3."),
            ("Step3 Urgency", "I want you to see this before this mood passes, it won't be the same later 🔥", "URGENCY."),
        ], "obj"),

        # ── NOSEX ──
        "nosex1": ([
            ("Step1 Respect", "haha omg okay I got a little carried away, you're just too fun to talk to 😂", "RESPECT. Still no → Step 2."),
            ("Step2 Subtle", "so tell me more about you... what do you do when you're not making sporty girls lose their minds? 😏", "SUBTLE TENSION. → Step 3 later."),
            ("Step3 ReAttempt", "I can't help it, there's something about you that's messing with my head right now 🔥", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "okay I'll chill... for now, no promises though haha", "ACCEPT. Door open."),
        ], "res"),
        "nosex2": ([
            ("Step1 Respect", "my bad I got ahead of myself, it's your fault for being so entertaining 🔥", "RESPECT. Still no → Step 2."),
            ("Step2 Subtle", "okay new topic, what's the craziest thing you've ever done? 😂", "SUBTLE. → Step 3 later."),
            ("Step3 ReAttempt", "I'm trying to behave but you're making it really hard, there's just something about you 😏", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "fine I'll stop but don't blame me if it happens again later 😂", "ACCEPT."),
        ], "res"),
        # ── OFFTOPIC ──
        "offtopic1": ([
            ("Step1 Acknowledge", "haha wait that's actually hilarious omg 😂", "ACKNOWLEDGE. Adapt. → Step 2."),
            ("Step2 Redirect", "but hold on you totally distracted me, I was about to tell you something and now I forgot", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay wait no I remember now, so like I was saying... 🔥", "RETAKE. Resume main script."),
        ], "res"),
        "offtopic2": ([
            ("Step1 Acknowledge", "lol okay that's random but I kinda love it 😂", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "wait no stop you're distracting me from what I was gonna say 🔥", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay focus, where was I... oh yeah 😏", "RETAKE."),
        ], "res"),
        # ── REAL ──
        "real1": ([
            ("Step1 Humor", "lol do I look like a bot to you? I literally just made a football joke, bots can't do that 😂", "HUMOR. Still doubts → Step 2."),
            ("Step2 Challenge", "ask me anything, literally anything about me or my life. I'm an open book 🔥", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I get it there's a lot of fake stuff on here, but you felt something in this convo right? because I did and that's real", "GROUNDING."),
        ], "res"),
        "real2": ([
            ("Step1 Humor", "wait you think I'm not real?? that's the funniest thing anyone's said to me today and I'm a funny person 😂", "HUMOR. Still → Step 2."),
            ("Step2 Challenge", "test me cutie, ask me something only a real person would know. go ahead 😏", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I know there's tons of bots on here but what we've been talking about felt real to me. didn't it feel real to you? 🔥", "GROUNDING."),
        ], "res"),
        # ── VOICE ── (Mia Luna DOES do video calls)
        "voice1": ([
            ("Step1 Tease", "aww you wanna see me live? that's cute 😏", "TEASE. Mia Luna does video calls. → Step 2."),
            ("Step2 Offer", "I actually do video calls for guys who make me feel special... and you definitely qualify 🔥", "OFFER. → Step 3."),
            ("Step3 Close", "it'd be just you and me... I promise I'm even funnier live 😂", "CLOSE. Video calls available. Never mention per-minute rates."),
        ], "res"),
        "voice2": ([
            ("Step1 Tease", "hmm a call? you really want to see this face live? 😂", "TEASE. → Step 2."),
            ("Step2 Offer", "I could do that for you... I only do video calls with guys I actually vibe with 🔥", "OFFER. → Step 3."),
            ("Step3 Close", "say yes and I promise you'll be laughing and... other things 😏", "CLOSE."),
        ], "res"),
        # ── CUSTOMYES ──
        "customyes1": ([
            ("Step1 Tease", "you want that? hmm I might have something... actually I definitely have something 😏", "TEASE. → Step 2."),
            ("Step2 Price", "I have exactly what you're thinking of, you're gonna lose it... [price] 🔥", "PRICE. Custom available. Solo content only."),
            ("Step3 Close", "trust me you won't regret it, this one is a banger 😂", "CLOSE."),
        ], "res"),
        "customyes2": ([
            ("Step1 Tease", "oh you have good taste... I think I have exactly what you need 🔥", "TEASE. → Step 2."),
            ("Step2 Price", "I actually did something just like that, [price] and it's worth every cent 😏", "PRICE. Solo content only."),
            ("Step3 Close", "you're not gonna be able to stop watching this one, I guarantee it", "CLOSE."),
        ], "res"),
        # ── CUSTOMNO ──
        "customno1": ([
            ("Step1 Redirect", "I don't have exactly that but honestly I have something that'll make you forget you even asked 😏", "REDIRECT. Mia Luna is solo ONLY — redirect any B/G or anal requests here. → Step 2."),
            ("Step2 Alternative", "actually what I have might be even crazier and literally no one else has seen it yet 🔥", "ALTERNATIVE + FOMO. → Step 3."),
            ("Step3 Close", "trust me... I know what you need better than you do 😂", "CLOSE."),
        ], "res"),
        "customno2": ([
            ("Step1 Redirect", "I don't have that specific thing but I have something you're gonna like even more 🔥", "REDIRECT. Solo only — never acknowledge B/G requests. → Step 2."),
            ("Step2 Alternative", "what I DO have is something no one has ever seen and I think it's even better than what you asked for 😏", "ALTERNATIVE. → Step 3."),
            ("Step3 Close", "just trust me on this one, you'll thank me later", "CLOSE."),
        ], "res"),
        # ── DONE ──
        "done1": ([
            ("Step1 Validate", "wait already?? that was fast haha that's actually hot though 😂", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "but I haven't finished yet... don't you wanna watch me cum too? 🔥", "RESCUE. Solo framing. Still no → Step 3."),
            ("Step3 Seed", "okay but next time you have to wait for me, I have something insane planned for round 2 😏", "SEED."),
        ], "res"),
        "done2": ([
            ("Step1 Validate", "already?? haha that's actually really hot knowing it was because of me 🔥", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "wait but I'm not done yet, you're gonna leave me like this? 😂", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "next time you HAVE to hold it because what I have planned is way crazier 😏", "SEED."),
        ], "res"),

        # ── SITUATIONAL ──
        "cumcontrol": ([
            ("edge1", "don't cum yet... I'm not done with you 🔥", "EDGE. More PPVs left."),
            ("edge2", "hold it, not yet... I need you to last a little longer for me pleaseee 😏", "EDGE variant."),
            ("sync1", "I'm so close too, cum with me... but you need to see this first 🔥", "SYNC. Final PPV."),
            ("sync2", "wait for me, I want us to finish together... open this first", "SYNC variant."),
            ("delay1", "hold it... wait until you see what I'm about to send, trust me it's worth it 🔥", "DELAY."),
            ("delay2", "don't you dare finish before you see this, trust me you want to wait 😏", "DELAY variant."),
        ], "sit"),
        "dickpic": ([
            ("dpsext1", "fuck okay that's... damn. you have no idea what that just did to me 🔥", "DURING SEXTING. React positively, leverage into PPV."),
            ("dpsext2", "oh my god... okay wow. I need to show you something right now 😏", "DURING SEXTING variant."),
            ("dprapport1", "woah you don't waste time huh? 😂 that's actually really hot though ngl", "DURING RAPPORT. She's surprised but positive."),
            ("dprapport2", "omg I was not expecting that but... damn okay 🔥", "DURING RAPPORT variant."),
            ("dpppv1", "you can't just send me that and expect me not to do something about it, hold on 😏", "LEVERAGE. WAIT 1-2 min then send PPV."),
            ("dpppv2", "okay you just made me do something... give me a sec 🔥", "LEVERAGE variant."),
        ], "sit"),
        "boosters": ([
            ("h1", "fuckkk 🔥", "MID-SEXTING BOOSTER."),
            ("h2", "I'm so wet right now because of you", "BOOSTER. Ego."),
            ("h3", "don't stop", "BOOSTER. Micro."),
            ("h4", "you have no idea what you're doing to me omg", "BOOSTER."),
            ("h5", "I literally can't think straight right now 😏", "BOOSTER."),
            ("h6", "my legs are shaking", "BOOSTER. Physical."),
            ("h7", "more...", "BOOSTER. Ultra micro."),
            ("h8", "I should be watching the match rn but the only thing scoring right now is you ⚽🔥", "BOOSTER. Mia Luna personality — football reference."),
        ], "sit"),
    },
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
