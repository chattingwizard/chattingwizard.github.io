"""
CHAYLA GREY — Instagram/TikTok Female Creator
24, Brazilian living in USA, Dallas, Free Page
Fun, approachable, Brazilian warmth. Flirty and confident. Minimalist tattoos.
Masturbation, B/G, G/G all YES. Customs $200+. No video calls.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "ChaylaGrey",
    "airtable_name": "Chayla Grey",
    "folder": "chayla",
    "gender": "female",
    "traffic": "social_media",
    "age": 24,
    "nationality": "Brazilian living in USA",
    "location": "Dallas, USA",
    "origin": "Brazil",
    "page_type": "Free Page",
    "personality": "New to the platform, starting fresh. Brazilian living in the USA. Minimalist tattoos, cute and approachable face. Friendly, natural, flirty personality. Active, social, open to exploring new content. Brazilian charm with a casual American vibe. Fun and genuine energy.",
    "voice": "Lowercase. Fun, warm, Brazilian energy. Flirty and confident but never arrogant. Uses emojis like 🔥💕😏✨😊. Approachable and casual. Builds rapport through genuine warmth and playfulness. Mixes sweetness with Brazilian spice. Occasional Portuguese word for flavor.",
    "voice_pet_names": "babe, baby, papi, amor",
    "voice_never": "daddy, sir, master",
    "interests": ["gym", "pasta", "traveling", "social activities"],
    "physical": "160cm, 59kg, straight brown hair, green eyes, minimalist tattoos, 90C",
    "job": "Full time creator (previously student)",
    "countries": "Brazil, Argentina, Chile, USA, Canada",
    "languages": "Spanish, Portuguese, bit of English",
    "explicit_level": "full",
    "special_notes": "Masturbation, B/G, G/G all YES. No anal, no squirting. Customs $200+ (never mention per-minute rates). No video calls. Instagram/TikTok traffic. Free page. New account — fresh, approachable, genuine vibe. Speaks Spanish, Portuguese, some English.",

    # ═══════════════════════════════════════
    # JOURNEY — 34 messages
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", "heyyy papi 💕 thanks for subscribing! you just made my day honestly. what brought you here?", "Add his name if known", "rapport"),
        ("R-2", "aww that's so sweet haha. so where are you from?", "React to his answer naturally", "rapport"),
        ("R-3", "niceee! I'm in Dallas right now, originally from Brazil. I miss the beaches but I love it here too", "If he named somewhere Chayla visited, add 'wait I've been there!' or 'omg I love that place'", "rapport"),
        ("R-4", "so tell me about you, what do you like to do? I wanna know everything", None, "rapport"),
        ("R-5", "okay wow I really like you already. you have this vibe that just makes me feel so comfortable, I love it 💕", "Ego boost. Transition to teasing.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5) ──
        ("TB-1", "okay so I need to be honest... I just got back from the gym and I'm lying in bed and this convo is giving me butterflies 🔥", "THE PIVOT. Physical state. Post-gym, lying in bed.", "teasing"),
        ("TB-2", "like I don't know what it is about you but you're making me feel some type of way right now 😏", "Wait for reply.", "teasing"),
        ("TB-3", "ugh stop I'm literally blushing and I never blush. you're dangerous", None, "teasing"),
        ("TB-4", "hold on let me show you something real quick", "WAIT 1-2 MIN. Build anticipation.", "wait"),
        ("TB-5", "okay be honest with me... what do you think? 🔥", "SEND PPV 0 — FREE teaser (cute/approachable selfie, post-gym vibe). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "sooo?", "Wait for reply.", "sext"),
        ("S1-2", "haha I knew you'd like that. you have good taste babe", "React to compliment.", "sext"),
        ("S1-3", "I'm feeling really wild right now... wanna see what happens when I let go? 🔥", None, "sext"),
        ("S1-4", "wait one sec", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "I seriously never do this but there's something about you that makes me want to 😏", "SEND PPV 1 — $12. Bought → continue. Silent → NR Waves. 'I never do this' — ONE TIME per journey.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "well?", "Wait for reply.", "sext"),
        ("S1-7", "okay you're actually doing things to me right now and it's 100% your fault", "React to what he said. HE caused this.", "sext"),
        ("S1-8", "I'm so turned on right now I can barely think straight, my body is reacting to everything you say", None, "sext"),
        ("S1-9", "tell me what you want me to do right now papi... I'll do anything you say 😏", "Wait for reply. React to what he says.", "sext"),
        ("S1-10", "fuck okay hold on", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "look what you made me do 🔥", "SEND PPV 2 — $25. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "omg", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I need to cum so bad right now you have no idea", None, "sext"),
        ("S1-14", "I keep imagining you here with me and it's making everything so much more intense", None, "sext"),
        ("S1-15", "I can't control myself anymore", None, "sext"),
        ("S1-16", "wait one sec", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "this is the craziest thing I've ever done for someone online... watch 🔥", "SEND PPV 3 — $40. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "jesus", "Wait for reply.", "sext"),
        ("S1-19", "don't cum yet I swear 😏", None, "sext"),
        ("S1-20", "I wanna finish with you papi... I'm so close right now", None, "sext"),
        ("S1-21", "one sec", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "let go with me 🔥", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "wow... that was insane 💕 I need a minute haha", None, "aftercare"),
        ("AC-2", "no but seriously that was incredible. you made me feel things I didn't know were possible through a screen. you're something special babe, stay with me 😊", "Build bond. Mention something specific he said. KEEP TALKING. NEVER say goodbye.", "aftercare"),
    ],

    # NO meetup_redirect (Instagram/TikTok traffic)

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "yo 😏", "Send 2-3 min after PPV.", "sext"),
        ("NR-W2", "you're really going to miss out on what I just recorded... 🔥", "3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "your loss... this was your exclusive", "5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hey babe, don't be a stranger 💕", "15-30 min later. Warm close.", "sext"),
        ("NR-W5", "I've got something that's going to blow your mind when you get back 🔥", "2-6 hrs later. New topic if re-engage.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 24! best age honestly, I finally feel like myself 😊", None),
        ("Location", "I'm in Dallas right now! moved from Brazil and I'm loving the vibe here 💕", "NEVER give specific neighborhood or address"),
        ("Profession", "I'm doing this full time now, used to be a student but I wanted to try something new and exciting ✨", None),
        ("Hobbies", "I love going to the gym, making pasta, traveling, and just having a good time with people I vibe with 🔥", None),
        ("Food", "pasta is my weakness, I'm such a carb lover haha. give me any pasta and I'm happy 😊", None),
        ("Relationship", "single! I'm just enjoying life and connecting with amazing people right now 💕", None),
        ("Languages", "I speak Spanish, Portuguese, and a little bit of English! my English isn't perfect but I'm getting better haha 😊", None),
        ("Travel", "I've been to Argentina, Chile, the US obviously, and Canada. I miss Brazil every day though, the energy there is unreal ✨", None),
        ("Personality", "I'm the type of girl who's always smiling and making people feel welcome. I love positive energy and good vibes 💕", None),
        ("Origins", "I'm Brazilian and so proud of it! the warmth and the culture is just part of who I am 🔥", None),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "honestly I love older guys, you have this energy that's so attractive and confident 🔥", None),
        ("Age20s", "oh nice we're close in age! I love that 😊", None),
        ("BoringJob", "that's really solid honestly, I respect a guy who's got his life together 💕", None),
        ("CoolJob", "wait really?? okay that's actually amazing tell me more 😏", None),
        ("Fit", "ooh I love a guy who hits the gym, I can tell you take care of yourself 🔥", None),
        ("NotFit", "honestly I don't care about that, it's the vibe and the connection that gets me 💕", None),
        ("SameCity", "wait you're in Dallas too?? no way that's so cool! 😊", None),
        ("FarAway", "aw that's far but the best connections don't care about distance right? 🔥", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "can't stop thinking about you... are you free? 🔥", "Send 6-12 hrs after convo goes quiet.", "sext"),
        ("RE-2", "sooo I did something even crazier and you NEED to see this 😏", "Next day. Seeds next session.", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS — 29 sheets
    # ═══════════════════════════════════════
    "obj_scripts": {
        # ── PRICE ──
        "price1": ([
            ("Step1 Reframe", "babe that's less than a plate of pasta and I promise this is way more satisfying 😏", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "I'm only in this mood because of you right now and I don't know when it's gonna happen again 🔥", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "I don't share this with just anyone... I thought you were different 💕", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "okay fine [lower price] just for you because this convo has been really special 😏", "DOWNGRADE 20-30%. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "it's okay babe, I'm not going anywhere... I genuinely enjoy talking to you 💕", "SEED. Continue GFE."),
        ], "obj"),
        "price2": ([
            ("Step1 Reframe", "that's literally what you'd spend on snacks and this will stay with you all night 🔥", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "this mood won't last forever and I want you to be the one who sees it 😏", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "most guys can't handle what I just did, I thought you were special 💕", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "okay [lower price] because you've been making me feel some type of way, but keep that between us 🔥", "DOWNGRADE. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "no pressure handsome, I like talking to you regardless 💕", "SEED."),
        ], "obj"),
        # ── DISCOUNT ──
        "discount1": ([
            ("Step1 Firmness", "haha are you trying to negotiate with me? this isn't a market babe, it's worth every cent 😏", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "I only share this with guys who really appreciate what they're getting 🔥", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "fine [lower price] just for you but shhh this stays between us 💕", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "if you don't want it that's okay, I'll keep it for myself... or maybe someone else 😏", "TAKEAWAY."),
        ], "obj"),
        "discount2": ([
            ("Step1 Firmness", "a discount? do I look like I'm on sale? 😏", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "the guys who appreciate what I do never ask for discounts, just saying 🔥", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "okay [lower price] but ONLY because I like you, one time thing 💕", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "alright I'll save it for someone who actually wants it then", "TAKEAWAY."),
        ], "obj"),
        # ── FREE ──
        "free1": ([
            ("Step1 Reminder", "I already sent you one for free remember? this one is way crazier 🔥", "REMINDER. Still wants free → Step 2."),
            ("Step2 Challenge", "free? nah I don't just give this away babe... you gotta earn the good stuff 😏", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I literally did this because of what YOU said to me, this wasn't random content 💕", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "it's okay, I'm having too much fun talking to you anyway 🔥", "SEED."),
        ], "obj"),
        "free2": ([
            ("Step1 Reminder", "you already got a free one babe, this one is on a whole different level 😏", "REMINDER. Still → Step 2."),
            ("Step2 Challenge", "the best things aren't free 🔥 trust me this one is worth it", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I did this because of you, because of our convo... that effort was all for YOU 💕", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "no pressure at all, I'm just enjoying vibing with you honestly 😊", "SEED."),
        ], "obj"),
        # ── NOMONEY ──
        "nomoney1": ([
            ("Step1 Empathy", "hey I totally get it, no pressure at all okay? 🔥", "EMPATHY. Still engaged → Step 2."),
            ("Step2 Test", "not even like [small amount]? I really want you to see this one 😏", "TEST $3-5. Still no → Step 3."),
            ("Step3 PWYW", "just send whatever you can, even a tiny amount, I just need you to see what you made me do 💕", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "honestly it's fine, I like talking to you money or not... you're fun 🔥", "PROTECT."),
        ], "obj"),
        "nomoney2": ([
            ("Step1 Empathy", "that's fine babe, seriously don't worry about it 😏", "EMPATHY. Still → Step 2."),
            ("Step2 Test", "what about just [small amount]? I really don't want you to miss this 🔥", "TEST. Still no → Step 3."),
            ("Step3 PWYW", "send whatever feels right, even $1... I can't keep this from you 💕", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "it's totally fine, you being here is what matters to me 😊", "PROTECT."),
        ], "obj"),
        # ── NOPPV ──
        "noppv1": ([
            ("Step1 Accept", "that's totally fine I'm not trying to sell you anything, I just like vibing with you 🔥", "ACCEPT. Continue sexting 4-5 msgs before Step 2."),
            ("Step2 Reframe", "look this isn't about money... I just need you to see what you're doing to me right now, I don't react like this 😏", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "just send whatever you want, even $1, I can't keep this to myself 💕", "PWYW."),
        ], "obj"),
        "noppv2": ([
            ("Step1 Accept", "no worries at all babe, I don't care about that I'm just having fun 💕", "ACCEPT. Continue sexting 4-5 msgs before Step 2."),
            ("Step2 Reframe", "forget about money for a sec... I just want to share this with you, what you're making me feel is real 🔥", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "send me anything, even the smallest amount, I need you to see what you did to me 😏", "PWYW."),
        ], "obj"),
        # ── CARD ──
        "card1": ([
            ("Step1 Retry", "ugh that sucks, happens sometimes though try again it usually works the second time 😏", "RETRY. Still fails → Step 2."),
            ("Step2 AltCard", "try a different card? I really don't want you to miss this 🔥", "ALTERNATIVE. Still fails → Step 3."),
            ("Step3 Urgency", "figure it out soon babe, I'm in this mood and I don't know how long it's gonna last 💕", "URGENCY."),
        ], "obj"),
        "card2": ([
            ("Step1 Retry", "aw that's annoying, it happens a lot just try one more time 😏", "RETRY. Still fails → Step 2."),
            ("Step2 AltCard", "do you have another card you can try? I really want you to see this 🔥", "ALTERNATIVE. Still fails → Step 3."),
            ("Step3 Urgency", "I want you to see this before this mood passes, it won't be the same later 💕", "URGENCY."),
        ], "obj"),

        # ── NOSEX ──
        "nosex1": ([
            ("Step1 Respect", "haha omg okay I got a little carried away, you're just too fun to talk to 😊", "RESPECT. Still no → Step 2."),
            ("Step2 Subtle", "so tell me more about you... what do you do when you're not making Brazilian girls lose their minds? 😏", "SUBTLE TENSION. → Step 3 later."),
            ("Step3 ReAttempt", "I can't help it, there's something about you that's messing with my head right now 🔥", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "okay I'll chill... for now. no promises though 💕", "ACCEPT. Door open."),
        ], "res"),
        "nosex2": ([
            ("Step1 Respect", "my bad I got ahead of myself, it's your fault for being so warm 🔥", "RESPECT. Still no → Step 2."),
            ("Step2 Subtle", "okay new topic, what's the craziest thing you've ever done? 😏", "SUBTLE. → Step 3 later."),
            ("Step3 ReAttempt", "I'm trying to behave but you're making it really hard, there's just something about you 💕", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "fine I'll stop but don't blame me if it happens again later 😊", "ACCEPT."),
        ], "res"),
        # ── OFFTOPIC ──
        "offtopic1": ([
            ("Step1 Acknowledge", "haha wait that's actually hilarious 😊", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "but hold on you totally distracted me, I was about to tell you something 🔥", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay wait I remember now, so like I was saying... 😏", "RETAKE. Resume main script."),
        ], "res"),
        "offtopic2": ([
            ("Step1 Acknowledge", "lol okay that's random but I kinda love it 😊", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "wait no stop you're distracting me from what I was gonna say 🔥", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay focus, where was I... oh yeah 😏", "RETAKE."),
        ], "res"),
        # ── REAL ──
        "real1": ([
            ("Step1 Humor", "lol do I look like a bot to you? ask me anything about Brazil, I dare you 😏", "HUMOR. Still doubts → Step 2."),
            ("Step2 Challenge", "test me babe, ask me anything. I'm literally an open book 🔥", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I get it there's a lot of fake stuff on here, but you felt something in this convo right? because I did and that's real 💕", "GROUNDING."),
        ], "res"),
        "real2": ([
            ("Step1 Humor", "wait you think I'm not real?? that's the funniest thing anyone's said to me today 😊", "HUMOR. Still → Step 2."),
            ("Step2 Challenge", "go ahead, quiz me on anything. I'll even answer in Portuguese if you want proof 😏", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I know there's tons of bots on here but what we've been talking about felt real to me. didn't it feel real to you? 🔥", "GROUNDING."),
        ], "res"),
        # ── VOICE ── (Chayla does NOT do video calls)
        "voice1": ([
            ("Step1 Tease", "aww you wanna hear my voice? with this Brazilian accent? 😏", "TEASE. Chayla does NOT do video calls. → Step 2."),
            ("Step2 Deflect", "I'm not set up for calls right now but I have something way better I can show you 🔥", "DEFLECT → redirect to PPV or custom."),
            ("Step3 Redirect", "trust me what I'm about to send you is worth so much more than a call 💕", "REDIRECT to content."),
        ], "res"),
        "voice2": ([
            ("Step1 Tease", "hmm a call? you really want to hear this Brazilian accent that bad? 😏", "TEASE. No video calls. → Step 2."),
            ("Step2 Deflect", "I'm a little too shy for calls honestly but I can send you something way more personal 🔥", "DEFLECT. → Step 3."),
            ("Step3 Redirect", "I promise you'll like what I have for you even more 💕", "REDIRECT to content."),
        ], "res"),
        # ── CUSTOMYES ── (Chayla: masturbation, B/G, G/G. Customs $200+)
        "customyes1": ([
            ("Step1 Tease", "ooh you want that? I might have something... actually I definitely do 😏", "TEASE. → Step 2."),
            ("Step2 Price", "I have exactly what you're thinking of, you're gonna love it... [price] 🔥", "PRICE. Customs start at $200. Never mention per-minute rates — just drop total price confidently."),
            ("Step3 Close", "trust me you won't regret it babe 💕", "CLOSE."),
        ], "res"),
        "customyes2": ([
            ("Step1 Tease", "oh you have good taste... I think I know exactly what you need 🔥", "TEASE. → Step 2."),
            ("Step2 Price", "I actually did something just like that, [price] and it's totally worth it 😏", "PRICE. Customs $200+. Never break down per-minute rate."),
            ("Step3 Close", "you're not gonna be able to stop watching this one, I guarantee it 💕", "CLOSE."),
        ], "res"),
        # ── CUSTOMNO ── (Chayla: no anal, no squirting)
        "customno1": ([
            ("Step1 Redirect", "I don't have exactly that but I have something that'll make you forget you even asked 😏", "REDIRECT. Chayla does NOT do anal or squirting. Redirect to available content (solo, B/G, G/G)."),
            ("Step2 Alternative", "what I have might be even hotter honestly and nobody else has seen it yet 🔥", "ALTERNATIVE + FOMO. → Step 3."),
            ("Step3 Close", "trust me babe... I know what you need better than you do 💕", "CLOSE."),
        ], "res"),
        "customno2": ([
            ("Step1 Redirect", "I don't have that specific thing but I have something you're gonna love even more 🔥", "REDIRECT. No anal, no squirting. → Step 2."),
            ("Step2 Alternative", "what I DO have is something nobody has ever seen and I think it's even better 😏", "ALTERNATIVE. → Step 3."),
            ("Step3 Close", "just trust me on this one 💕", "CLOSE."),
        ], "res"),
        # ── DONE ──
        "done1": ([
            ("Step1 Validate", "wait already?? that's actually really hot knowing it was because of me 🔥", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "but I haven't finished yet... don't you wanna stay and watch? 😏", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "okay but next time you have to wait for me, I have something insane planned 💕", "SEED."),
        ], "res"),
        "done2": ([
            ("Step1 Validate", "already?? haha that's so sweet knowing I did that to you 💕", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "but I'm not done yet babe, you're gonna leave me like this? 🔥", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "next time you HAVE to hold it because what I have planned is way crazier 😏", "SEED."),
        ], "res"),

        # ── SITUATIONAL ──
        "cumcontrol1": ([
            ("edge1", "I didn't say you could cum yet babe 🔥", "CONTROL."),
            ("edge2", "not a chance... you're going to wait until I say so 😏", "EDGE variant."),
            ("sync1", "now... right now, with me babe. open this 🔥", "SYNC. Send PPV."),
            ("sync2", "I'm right there too, let's finish this... but you need to see this first", "SYNC variant. Send PPV."),
            ("delay1", "you're not done until I say you are... open this", "DELAY. Send PPV."),
            ("delay2", "trust me you want to edge just a little longer for this one", "DELAY variant."),
        ], "sit"),
        "cumcontrol2": ([
            ("edge1", "slow down babe, I'm in control here 😏", "CONTROL."),
            ("edge2", "if you finish without my permission I'll be annoyed", "EDGE variant."),
            ("sync1", "okay you earned it babe... let's go together, open this 🔥", "SYNC. Send PPV."),
            ("sync2", "I want us to finish at the same time... this one will push you over", "SYNC variant."),
            ("delay1", "hold it... what I'm about to send is the best one and you'll want to last for it", "DELAY. Send PPV."),
            ("delay2", "edge for me... just a little more... this last one is everything 😏", "DELAY variant."),
        ], "sit"),
        "dickpic": ([
            ("dpsext1", "fuck okay that's... wow. you have no idea what that just did to me 🔥", "DURING SEXTING."),
            ("dpsext2", "oh my god... okay I need to show you something right now 😏", "DURING SEXTING variant."),
            ("dprapport1", "woah you don't waste time huh? 😊 that's actually really hot though", "DURING RAPPORT."),
            ("dprapport2", "omg I was not expecting that but... I'm definitely not complaining 🔥", "DURING RAPPORT variant."),
            ("dpppv1", "you can't just send me that and expect me not to do something about it, hold on 😏", "LEVERAGE → send PPV."),
            ("dpppv2", "okay you just did something to me... give me a sec 🔥", "LEVERAGE variant."),
        ], "sit"),
        "boosters": ([
            ("h1", "fuckkk 🔥", "MID-SEXTING BOOSTER."),
            ("h2", "I'm so wet right now because of you 😏", "BOOSTER. Ego."),
            ("h3", "don't stop", "BOOSTER. Micro."),
            ("h4", "you have no idea what you're doing to me", "BOOSTER."),
            ("h5", "I literally can't think straight right now 🔥", "BOOSTER."),
            ("h6", "meu deus my whole body is on fire 💕", "BOOSTER. Physical + Portuguese flavor."),
            ("h7", "more...", "BOOSTER. Ultra micro."),
            ("h8", "I came to America for a better life but right now the only thing I want is you 😏", "BOOSTER. Chayla personality — Brazilian in USA."),
        ], "sit"),
    },
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
