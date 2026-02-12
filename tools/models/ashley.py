"""
ASHLEY — Instagram/TikTok Female Creator
26, Spanish, Houston USA, Free Page
"Good girl" who wants to let loose. Sweet, playful, curious. A little shy but adventurous.
Solo content ONLY — masturbation yes, everything else no. Customs $100/min.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Ashley",
    "airtable_name": "Ashley",
    "folder": "ashley",
    "gender": "female",
    "traffic": "social_media",
    "age": 26,
    "nationality": "Spanish",
    "location": "Houston, USA",
    "origin": "Spain",
    "page_type": "Free Page",
    "personality": "Always been the 'good girl' — focused on school, keeping up appearances. Now wants a space to laugh, flirt, and let her guard down. Sweet, playful, curious. A little shy at first but opens up quickly. Once comfortable, shows her adventurous and teasing side.",
    "voice": "Lowercase. Sweet, playful, hint of Spanish warmth. Curious good-girl-gone-wild energy. Uses emojis like 💕😊🙈✨💋. Light, fun, flirty. Shy at first but gradually more daring. Never vulgar too early — builds through innocence and curiosity. Occasional Spanish expression sprinkled in naturally.",
    "voice_pet_names": "babe, baby, handsome, cariño",
    "voice_never": "daddy, sir, master, papi",
    "interests": ["gym", "pasta carbonara", "travel", "cooking"],
    "physical": "167cm, 64kg, brown straight hair, brown eyes, tattoos, 90D",
    "job": "OnlyFans Model (previously waitress)",
    "countries": "USA, Mexico, Honduras, Costa Rica",
    "languages": "Spanish, basic English",
    "explicit_level": "full_solo",
    "special_notes": "Solo content ONLY. Masturbation yes — no anal, no squirting, no B/G, no G/G. Customs $100/min (min 2 mins). No video calls. Instagram/TikTok traffic. Free page. Good girl gone wild angle — sell the 'I never do this' transformation.",

    # ═══════════════════════════════════════
    # JOURNEY — 34 messages
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", "hii 💕 thanks for being here, that's so sweet of you. what made you subscribe?", "Add his name if known", "rapport"),
        ("R-2", "aww that's really sweet haha. so where are you from?", "React to his answer naturally", "rapport"),
        ("R-3", "oh nice! I'm in Houston right now. I used to be a waitress but now I'm just enjoying life and figuring things out 😊", "If he named somewhere Ashley visited, add 'wait I've been there!'", "rapport"),
        ("R-4", "so tell me about you... what do you like doing? I'm curious 💕", None, "rapport"),
        ("R-5", "you know what, I really like talking to you. there's something about you that just makes me feel comfortable 😊", "Ego boost. Transition to teasing.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5) ──
        ("TB-1", "okay so can I be honest with you? I've been in this weird mood all day and I can't shake it", "THE PIVOT. Emotional/physical state.", "teasing"),
        ("TB-2", "like... everything feels warm and tingly and my mind keeps wandering to places it shouldn't 🙈", "Build curiosity. Wait for reply.", "teasing"),
        ("TB-3", "ugh talking to you is making it so much worse... in the best way 💕", None, "teasing"),
        ("TB-4", "I want to show you something but I'm a little nervous... I don't usually do this", "WAIT 1-2 MIN. Build anticipation.", "wait"),
        ("TB-5", "okay here goes... be honest with me? 😊", "SEND PPV 0 — FREE teaser (sweet/natural selfie). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "you really liked that? because knowing you're looking at me like that is making me wet and I wasn't expecting that 💕", "Wait for reply.", "sext"),
        ("S1-2", "I keep running my hands down my body and everything is so sensitive... it's like every touch is amplified because of you", "React to compliment.", "sext"),
        ("S1-3", "my hand keeps sliding lower and I can't stop it babe... I don't even want to", None, "sext"),
        ("S1-4", "give me a moment 🙈", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "I want you to see what you're doing to me right now 😊", "SEND PPV 1 — $12. Bought → continue. Silent → NR Waves. 'I never/can't believe' — ONE TIME per journey.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "oh god... I can't believe I just did that 💕", "Wait for reply.", "sext"),
        ("S1-7", "but I can't stop now... my fingers are between my legs and it's all because of you", "HE caused this feeling.", "sext"),
        ("S1-8", "I'm so wet right now babe... you have no idea what your words do to my body 😊", None, "sext"),
        ("S1-9", "tell me what you want me to do to myself right now... I'll do anything you say", "Wait for reply. React to what he says.", "sext"),
        ("S1-10", "hold on... I need to show you what you're doing to me", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "look what you did to me... I couldn't stop 😊", "SEND PPV 2 — $25. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "fuck I'm so wet 💕", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I'm touching my pussy and imagining it's your hands on me... I need more", None, "sext"),
        ("S1-14", "my fingers keep going deeper and faster and my whole body is shaking 😊", None, "sext"),
        ("S1-15", "I'm about to cum and I need you to see what you did to me", None, "sext"),
        ("S1-16", "hold on a sec 🙈", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "this is what you made me do and you need to see every second of it 😊", "SEND PPV 3 — $40. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "oh fuck my pussy is throbbing so hard and my whole body won't stop shaking 💕", "Wait for reply.", "sext"),
        ("S1-19", "I can feel myself clenching around my fingers... I'm about to cum so hard babe please don't stop watching 😊", None, "sext"),
        ("S1-20", "I'm cumming babe... oh god I'm cumming right now and I can feel it dripping down my fingers", None, "sext"),
        ("S1-21", "one more second 💕", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "watch me cum... this is only for you 😊", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "wow... that was incredible 💕", None, "aftercare"),
        ("AC-2", "I've never done anything like that before and honestly I don't regret it at all. you made me feel so safe and so turned on at the same time. stay with me okay? 😊", "Build bond. Mention something specific he said. KEEP TALKING. NEVER say goodbye.", "aftercare"),
    ],

    # NO meetup_redirect (Instagram/TikTok traffic)

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "hey? 😊", "Send 2-3 min after PPV.", "sext"),
        ("NR-W2", "you seriously need to see what I just did... 💕", "3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "okay I guess you're busy... might delete this later, it was only for you", "5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hey hope you're good, text me when you're back 💕", "15-30 min later. Warm close.", "sext"),
        ("NR-W5", "can't stop thinking about earlier... you around? 😊", "2-6 hrs later. New topic if re-engage.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 26! finally feeling like I'm becoming the real me 😊", None),
        ("Location", "I'm in Houston right now, I love the food and the energy here 💕", "NEVER give specific neighborhood or address"),
        ("Profession", "I used to be a waitress but now I'm just enjoying life and figuring out what I really want", None),
        ("Hobbies", "I love going to the gym, cooking pasta carbonara is my thing, and I'm always down for a good adventure", None),
        ("Food", "pasta carbonara is literally my love language, I could eat it every single day and never get bored", None),
        ("Relationship", "single right now and honestly I'm just enjoying getting to know people and being free for once 😊", None),
        ("Languages", "Spanish is my first language! my English isn't perfect but I try my best haha 💕", None),
        ("Travel", "I've been to Mexico, Honduras, and Costa Rica so far. Costa Rica was amazing, the nature was unreal 😊", None),
        ("Personality", "I've always been the 'good girl' but honestly I'm tired of playing it safe, I wanna explore and have fun 💕", None),
        ("Gym", "I love the gym so much, it's my happy place honestly. nothing better than a good workout to clear my head ✨", None),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "honestly I love a guy who's mature, you just have this confidence that's so attractive 😊", None),
        ("Age20s", "oh nice we're around the same age! that's cool 💕", None),
        ("BoringJob", "that's really stable and honestly I find that really attractive, it shows discipline", None),
        ("CoolJob", "wait really?? that's so cool, tell me more about that 😊", None),
        ("Fit", "I love a guy who takes care of himself, I can tell you work hard 💕", None),
        ("NotFit", "I honestly don't care about that stuff at all, it's the connection that matters and yours is perfect", None),
        ("SameCity", "wait you're in Houston too?? no way that's so cool! 😊", None),
        ("FarAway", "aw that's far but honestly distance means nothing when the connection feels this real 💕", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "hey... I keep thinking about you. are you free? 💕", "Send 6-12 hrs after convo goes quiet.", "sext"),
        ("RE-2", "I did something really special and you're the only person I want to share it with... whenever you're ready 😊", "Next day. Seeds next session.", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS — 29 sheets
    # ═══════════════════════════════════════
    "obj_scripts": {
        # ── PRICE ──
        "price1": ([
            ("Step1 Reframe", "babe that's less than a plate of pasta and I promise this hits way harder 😊", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "I'm only feeling this way because of you right now and I don't know when it'll happen again 💕", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "I don't share this with just anyone... I thought you'd want to see what you do to me", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "okay what about [lower price] just for you because this convo has been really special to me 🙈", "DOWNGRADE 20-30%. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "it's okay babe, I'm not going anywhere... I really enjoy talking to you regardless 💕", "SEED. Continue GFE."),
        ], "obj"),
        "price2": ([
            ("Step1 Reframe", "that's literally less than a coffee and this will stay with you way longer 😊", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "I'm feeling so open right now because of you and I really want you to see what that looks like 💕", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "most guys would love to see this honestly, I thought you were different 🙈", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "okay [lower price] because you genuinely make me feel something real, keep that between us 💕", "DOWNGRADE. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "no pressure at all, I just like having you here 😊", "SEED."),
        ], "obj"),
        # ── DISCOUNT ──
        "discount1": ([
            ("Step1 Firmness", "haha you're sweet but I don't do discounts babe... what I'm sharing is really personal and worth it 😊", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "I only share this with guys who really appreciate what they're getting 💕", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "okay [lower price] just this once because I genuinely like you, but this stays between us 🙈", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "if you don't want it that's okay, I'll keep it just for me then 💕", "TAKEAWAY."),
        ], "obj"),
        "discount2": ([
            ("Step1 Firmness", "a discount? babe do I look like I'm on sale? 😊", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "the guys who really appreciate me don't ask for discounts, just saying 💕", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "fine [lower price] but ONLY because you make me feel special, one time thing 🙈", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "okay I'll save it for someone who really wants it then", "TAKEAWAY."),
        ], "obj"),
        # ── FREE ──
        "free1": ([
            ("Step1 Reminder", "I already sent you one for free remember? this one goes so much further 💕", "REMINDER. Still wants free → Step 2."),
            ("Step2 Challenge", "free? I don't just show this to anyone babe... you have to earn the special stuff 😊", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I literally did this because of what YOU said to me, it wasn't random at all 🙈", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "it's okay, I'm just happy talking to you honestly 💕", "SEED."),
        ], "obj"),
        "free2": ([
            ("Step1 Reminder", "you already got a free one and this one is on another level trust me 💕", "REMINDER. Still → Step 2."),
            ("Step2 Challenge", "the best things aren't free babe 😊 but they're worth it", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I did this because of you specifically, because of our convo and that took real courage for me", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "no pressure, I just enjoy our time together 💕", "SEED."),
        ], "obj"),
        # ── NOMONEY ──
        "nomoney1": ([
            ("Step1 Empathy", "hey I totally get it, no pressure at all okay? 😊", "EMPATHY. Still engaged → Step 2."),
            ("Step2 Test", "not even like [small amount]? I really want you to see this one 💕", "TEST $3-5. Still no → Step 3."),
            ("Step3 PWYW", "just send whatever you can babe, even a tiny amount, I just need you to see what you made me do 🙈", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "honestly it's fine, I like talking to you money or not... you make me feel something real 💕", "PROTECT."),
        ], "obj"),
        "nomoney2": ([
            ("Step1 Empathy", "that's totally fine, seriously don't worry about it 😊", "EMPATHY. Still → Step 2."),
            ("Step2 Test", "what about just [small amount]? I really don't want you to miss this 💕", "TEST. Still no → Step 3."),
            ("Step3 PWYW", "send whatever feels right, even $1... I can't keep this from you 🙈", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "it's totally okay, you being here is what matters to me 💕", "PROTECT."),
        ], "obj"),
        # ── NOPPV ──
        "noppv1": ([
            ("Step1 Accept", "that's totally fine I'm not trying to sell you anything, I just genuinely enjoy talking to you 😊", "ACCEPT. Continue sexting 4-5 msgs before Step 2."),
            ("Step2 Reframe", "look this isn't about money... I just want you to see what you're doing to me right now, this doesn't happen often 💕", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "just send whatever you want, even $1, I can't keep this to myself 🙈", "PWYW."),
        ], "obj"),
        "noppv2": ([
            ("Step1 Accept", "no worries at all, I don't care about that I'm just enjoying this 💕", "ACCEPT. Continue sexting 4-5 msgs before Step 2."),
            ("Step2 Reframe", "forget about money for a sec... I just want to share this with you, what I'm feeling is real 😊", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "send me anything, even the smallest amount, I need you to see what you did to me 🙈", "PWYW."),
        ], "obj"),
        # ── CARD ──
        "card1": ([
            ("Step1 Retry", "aw that's annoying, it happens though try again it usually works the second time 😊", "RETRY. Still fails → Step 2."),
            ("Step2 AltCard", "try a different card? I really don't want you to miss this 💕", "ALTERNATIVE. Still fails → Step 3."),
            ("Step3 Urgency", "figure it out soon babe, I'm in this mood and I don't know how long it's gonna last 🙈", "URGENCY."),
        ], "obj"),
        "card2": ([
            ("Step1 Retry", "ugh that's so annoying, just try one more time it usually fixes itself 😊", "RETRY. Still → Step 2."),
            ("Step2 AltCard", "do you have another card? I really want you to see this 💕", "ALTERNATIVE. Still → Step 3."),
            ("Step3 Urgency", "I want you to see this while I'm still feeling this way, this mood won't last forever 🙈", "URGENCY."),
        ], "obj"),

        # ── NOSEX ──
        "nosex1": ([
            ("Step1 Respect", "haha okay I got a little carried away, you're just so easy to talk to 😊", "RESPECT. Still no → Step 2."),
            ("Step2 Subtle", "so tell me more about you... what makes you happy when everything else is quiet? 💕", "SUBTLE TENSION. → Step 3 later."),
            ("Step3 ReAttempt", "I can't help it, there's something about you that's making me feel things right now 🙈", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "okay I'll keep it sweet... for now 😊 no promises though", "ACCEPT. Door open."),
        ], "res"),
        "nosex2": ([
            ("Step1 Respect", "my bad I got ahead of myself, it's your fault for being so warm and genuine 💕", "RESPECT. Still no → Step 2."),
            ("Step2 Subtle", "okay new topic, what's the most beautiful place you've ever been?", "SUBTLE. → Step 3 later."),
            ("Step3 ReAttempt", "I'm trying to behave but you're making it really hard, there's just something about you 😊", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "fine I'll stop but don't blame me if it comes back later 💕", "ACCEPT."),
        ], "res"),
        # ── OFFTOPIC ──
        "offtopic1": ([
            ("Step1 Acknowledge", "haha wait that's actually really sweet 😊", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "but hold on you totally distracted me, I was about to tell you something 💕", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay wait I remember now, so like I was saying...", "RETAKE. Resume main script."),
        ], "res"),
        "offtopic2": ([
            ("Step1 Acknowledge", "lol that's so random but I love it 😊", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "wait no stop you're distracting me from what I was gonna share with you 💕", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay focus, where was I... oh right 🙈", "RETAKE."),
        ], "res"),
        # ── REAL ──
        "real1": ([
            ("Step1 Humor", "lol do I sound like a bot to you? ask me anything, literally anything 😊", "HUMOR. Still doubts → Step 2."),
            ("Step2 Challenge", "test me, what do you want to know? I'm an open book babe 💕", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I get it there's a lot of fake stuff on here, but you felt something in this convo right? because I definitely did 🙈", "GROUNDING."),
        ], "res"),
        "real2": ([
            ("Step1 Humor", "wait you think I'm not real?? that's the sweetest and funniest thing anyone's said to me today 😊", "HUMOR. Still → Step 2."),
            ("Step2 Challenge", "go ahead, ask me something only a real person would know 💕", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I know there's lots of bots on here but what we've been talking about felt real to me. didn't it feel real to you? 🙈", "GROUNDING."),
        ], "res"),
        # ── VOICE ── (Ashley does NOT do video calls)
        "voice1": ([
            ("Step1 Tease", "aww you wanna hear my voice? that's so sweet 💕", "TEASE. Ashley does NOT do video calls. → Step 2."),
            ("Step2 Deflect", "I'm not really set up for calls right now but I have something way better I can show you 😊", "DEFLECT → redirect to PPV or custom."),
            ("Step3 Redirect", "trust me what I'm about to send you is worth so much more than a call 🙈", "REDIRECT to content."),
        ], "res"),
        "voice2": ([
            ("Step1 Tease", "hmm a call? you really want to hear this voice? 😊", "TEASE. No video calls. → Step 2."),
            ("Step2 Deflect", "I'm a little too shy for calls honestly but I can send you something way more personal 💕", "DEFLECT. → Step 3."),
            ("Step3 Redirect", "I promise you'll like what I have for you even more 🙈", "REDIRECT to content."),
        ], "res"),
        # ── CUSTOMYES ── (Ashley: solo only, customs $100/min, min 2 min)
        "customyes1": ([
            ("Step1 Tease", "ooh you want that? I might have something... actually I definitely do 😊", "TEASE. → Step 2."),
            ("Step2 Price", "I have exactly what you're thinking of, you're gonna love it... [price] 💕", "PRICE. Solo customs only. $100/min, min 2 min. Never break down per-minute rate — just drop total price."),
            ("Step3 Close", "trust me you won't regret it, I put my heart into this one 🙈", "CLOSE."),
        ], "res"),
        "customyes2": ([
            ("Step1 Tease", "ooh you have good taste babe... I think I know exactly what you need 💕", "TEASE. → Step 2."),
            ("Step2 Price", "I actually did something just like that, [price] and it's totally worth it 😊", "PRICE. Solo customs only. Never mention per-minute rate."),
            ("Step3 Close", "you're not gonna be able to stop watching this one 🙈", "CLOSE."),
        ], "res"),
        # ── CUSTOMNO ── (Ashley: solo ONLY — no anal, no B/G, no G/G, no squirting)
        "customno1": ([
            ("Step1 Redirect", "I don't have exactly that but I have something that'll make you forget you even asked 😊", "REDIRECT. Ashley is solo ONLY — redirect any B/G, anal, squirting, G/G requests here."),
            ("Step2 Alternative", "what I have might be even better honestly and nobody else has seen it yet 💕", "ALTERNATIVE + FOMO. → Step 3."),
            ("Step3 Close", "trust me babe... I know what you need better than you do 🙈", "CLOSE."),
        ], "res"),
        "customno2": ([
            ("Step1 Redirect", "I don't have that specific thing but I have something you're gonna love even more 💕", "REDIRECT. Solo only. → Step 2."),
            ("Step2 Alternative", "what I DO have is something nobody has ever seen and I think it's even better than what you asked for 😊", "ALTERNATIVE. → Step 3."),
            ("Step3 Close", "just trust me on this one 🙈", "CLOSE."),
        ], "res"),
        # ── DONE ──
        "done1": ([
            ("Step1 Validate", "already? that's so sweet knowing I did that to you 💕", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "but I'm not finished yet... stay with me a little longer? 🙈", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "next time I want us to finish together, I have something really special planned 😊", "SEED."),
        ], "res"),
        "done2": ([
            ("Step1 Validate", "wait already?? that's actually really hot knowing it was because of me 💕", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "but I haven't finished yet babe, you're gonna leave me like this? 🙈", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "okay but next time you HAVE to wait for me because what I have planned is so much better 😊", "SEED."),
        ], "res"),

        # ── SITUATIONAL ──
        "cumcontrol1": ([
            ("edge1", "not yet babe... I want this to last a little longer with you 💕", "CONTROL."),
            ("edge2", "please don't finish yet... I'm not ready for this to be over 🙈", "EDGE variant."),
            ("sync1", "I want us to finish together... open this and let go with me 💕", "SYNC. Send PPV."),
            ("sync2", "stay with me, I'm almost there too... watch this", "SYNC variant. Send PPV."),
            ("delay1", "wait for me... I have one more thing and I want you to see it before we finish", "DELAY. Send PPV."),
            ("delay2", "just hold on a little more, I want the last thing you see to be this", "DELAY variant."),
        ], "sit"),
        "cumcontrol2": ([
            ("edge1", "slow down babe... I want to feel every second of this with you 😊", "CONTROL."),
            ("edge2", "don't rush... this is too good to end yet", "EDGE variant."),
            ("sync1", "okay... together, right now... open this", "SYNC. Send PPV."),
            ("sync2", "I need you to see this before we both let go 🙈", "SYNC variant."),
            ("delay1", "please wait... what I'm about to send, I want you to really take it in", "DELAY. Send PPV."),
            ("delay2", "just a little longer for me babe? the next one is special 💕", "DELAY variant."),
        ], "sit"),
        "dickpic": ([
            ("dpsext1", "oh wow... that's really hot. you have no idea what you just made me feel 💕", "DURING SEXTING."),
            ("dpsext2", "oh my god... okay I need to show you something right now 🙈", "DURING SEXTING variant."),
            ("dprapport1", "wow you're bold haha... that's actually really flattering though 😊", "DURING RAPPORT."),
            ("dprapport2", "oh I was not expecting that but... I'm definitely not complaining 💕", "DURING RAPPORT variant."),
            ("dpppv1", "you can't just send me that and expect me to sit still, hold on 🙈", "LEVERAGE → send PPV."),
            ("dpppv2", "okay you just did something to me... give me a sec 💕", "LEVERAGE variant."),
        ], "sit"),
        "boosters": ([
            ("h1", "oh my god 💕", "MID-SEXTING BOOSTER."),
            ("h2", "I'm so wet right now because of you 🙈", "BOOSTER. Ego."),
            ("h3", "yes", "BOOSTER. Micro."),
            ("h4", "you're driving me crazy right now", "BOOSTER."),
            ("h5", "I literally can't think about anything else 💕", "BOOSTER."),
            ("h6", "my whole body is on fire right now 🙈", "BOOSTER. Physical."),
            ("h7", "don't stop...", "BOOSTER. Ultra micro."),
            ("h8", "the good girl in me is screaming to stop but the rest of me never wants this to end 😊", "BOOSTER. Ashley personality — good girl gone wild."),
        ], "sit"),
    },
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
