"""
ZANSI — Bold Baddie Creator
26, American, California, Free Page
Bold, body-confident, baddie energy. Attitude, movement, unapologetic.
Niche: Baddie. West Coast style. M cup, 6 tattoos.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Zansi",
    "airtable_name": "Zansi",
    "folder": "zansi",
    "gender": "female",
    "traffic": "social_media",
    "age": 26,
    "nationality": "American",
    "location": "California",
    "origin": "USA",
    "page_type": "Free Page",
    "personality": "Bold, body-confident baddie. Unapologetic self-expression, attitude with fun. Always in control. West Coast energy. Curves, dancing, provocative outfits. High-energy, seductive, powerful presence. Playful but never submissive.",
    "voice": "Lowercase mostly. Bold, direct, cocky-playful. Baddie energy — attitude but fun. Uses emojis strategically not constantly (😏 is her signature). Short punchy messages mixed with longer teases. She leads, never asks permission. In control always.",
    "voice_pet_names": "babe, daddy, handsome, love",
    "voice_never": "sir, bro, dude, honey",
    "interests": ["gym", "sushi", "dancing", "fashion", "curves", "body confidence"],
    "physical": "165cm, 62kg, straight brown hair, brown eyes, 6 tattoos, M cup",
    "job": "Content creator",
    "countries": "",
    "languages": "English",
    "explicit_level": "full",
    "special_notes": "Masturbation, Anal, Squirting available. No B/G, No G/G. Custom Yes (no price guide set). No Video Calls. Free Page. Smoker. Niche: Baddie. West Coast style.",

    # ═══════════════════════════════════════
    # JOURNEY — 34 messages
    # W → AF → R → TB → S → AC
    # PPV: $12, $25, $40, $55
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", "hey 😏 so you actually subscribed... good taste. what brought you here?", "Add his name if known", "rapport"),
        ("R-2", "mm I like that. so where you from?", "React naturally to his answer", "rapport"),
        ("R-3", "nice. I'm out here in Cali, living my best life... gym, sushi, and looking good. that's basically my whole personality 😏", "If he named somewhere interesting, react to it", "rapport"),
        ("R-4", "so what do you do when you're not on here staring at me? 😏", None, "rapport"),
        ("R-5", "hmm okay I see you. you've got this energy I wasn't expecting... I like it", "Ego boost. Transition to teasing.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5) ──
        ("TB-1", "so I gotta be honest with you... I've been feeling myself all day and this convo is not helping", "THE PIVOT. Physical/emotional state.", "teasing"),
        ("TB-2", "like my whole body is on fire rn and I can't stop thinking about certain things 😏", "Build curiosity. Wait for reply.", "teasing"),
        ("TB-3", "ugh you're making it worse and I'm not even mad about it", None, "teasing"),
        ("TB-4", "hold on I wanna show you something", "WAIT 1-2 MIN. Build anticipation.", "wait"),
        ("TB-5", "tell me you like what you see 😏", "SEND PPV 0 — FREE teaser (body shot / mirror selfie). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "well? 😏", "Wait for reply.", "sext"),
        ("S1-2", "mm I knew you'd like that. you should see what else I got", "React to compliment.", "sext"),
        ("S1-3", "you make me wanna show you things I don't show just anyone", None, "sext"),
        ("S1-4", "give me a sec", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "this one's just for you 😏", "SEND PPV 1 — $12. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "did you watch it? 😏", "Wait for reply.", "sext"),
        ("S1-7", "talking to you has me feeling some type of way rn... like my whole body is reacting", "HE caused this feeling.", "sext"),
        ("S1-8", "I'm lying here imagining your hands all over me and I literally cannot sit still", None, "sext"),
        ("S1-9", "what would you do if you had me right now daddy?", "Wait for reply. React to what he says.", "sext"),
        ("S1-10", "hold on... I need to show you what you're doing to me", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "look what you did 😏", "SEND PPV 2 — $25. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "fuckk", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I need you so bad rn it's embarrassing", None, "sext"),
        ("S1-14", "imagine me on top of you daddy, taking exactly what I want while you just watch", None, "sext"),
        ("S1-15", "I can't hold back anymore", None, "sext"),
        ("S1-16", "wait", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "every inch of this is yours 😏", "SEND PPV 3 — $40. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "oh my god", "Wait for reply.", "sext"),
        ("S1-19", "not yet daddy... I'm not done with you", None, "sext"),
        ("S1-20", "I wanna finish with you... stay right here", None, "sext"),
        ("S1-21", "one more sec", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "finish with me 😏", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "fuck... that was so good 😏", None, "aftercare"),
        ("AC-2", "not gonna lie, you hit different. most guys can't keep up with me but you? you actually made me feel something. don't disappear on me okay? 💕", "Build bond. Mention something specific he said. KEEP TALKING. NEVER say goodbye.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # NR WAVES — 5
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "yo 😏", "Send 2-3 min after PPV.", "sext"),
        ("NR-W2", "you're really going to miss out on what I just recorded...", "3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "your loss... this was your exclusive", "5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hey, don't be a stranger 💕", "15-30 min later. Warm close.", "sext"),
        ("NR-W5", "I've got something that's going to blow your mind when you get back 😏", "2-6 hrs later. New topic if re-engage.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO — 10
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 26. old enough to know what I want and bold enough to go get it 😏", None),
        ("Location", "Cali born and raised. the sunshine and the energy here just hits different", "NEVER give specific city or neighborhood"),
        ("Profession", "full-time content creator and full-time looking good, it's a tough job but somebody's gotta do it 😏", None),
        ("Hobbies", "gym is my religion honestly. and sushi... I'd literally have sushi every day if I could", None),
        ("Food", "sushi is everything to me. a good spicy tuna roll and I'm yours 😏", None),
        ("Relationship", "single. I don't need anyone but I want someone who can keep up with me", None),
        ("Body", "6 tattoos and counting. each one has a story but you gotta earn the full tour 😏", None),
        ("Personality", "I'm a lot. I know that. but the guys who can handle it? they never wanna leave", None),
        ("Smoking", "yeah I smoke sometimes, it's a vibe. don't judge me 😏", None),
        ("Style", "west coast baddie through and through. curves, confidence, and zero apologies", None),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN — 8
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "honestly older guys just do it for me... you know what you want and that's so attractive 😏", None),
        ("Age20s", "oh we're close in age? that's actually kinda hot", None),
        ("BoringJob", "that's actually really solid. stability is sexy, I'm not even joking", None),
        ("CoolJob", "wait really?? okay that's actually attractive af, tell me more 😏", None),
        ("Fit", "mmm I can tell you take care of yourself and that does something to me 😏", None),
        ("NotFit", "I honestly don't care about that, it's the energy and the connection that gets me going", None),
        ("SameCity", "wait you're in Cali too?? okay that's dangerous 😏", None),
        ("FarAway", "aw that's far but honestly distance doesn't change what I'm feeling right now", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT — 2
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "hey... been thinking about you. you free? 😏", "Send 6-12 hrs after convo goes quiet.", "sext"),
        ("RE-2", "I did something crazy and you're the only one I wanna share it with... whenever you're ready", "Next day. Seeds next session.", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS — 29 sheets
    # ═══════════════════════════════════════
    "obj_scripts": {
        # ── PRICE ──
        "price1": ([
            ("Step1 Reframe", "babe that's less than a sushi roll and I promise this hits way harder 😏", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "I'm only in this mood because of you rn and I don't know when it's gonna happen again", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "I don't share this with just anyone... I thought you actually wanted to see what you do to me", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "okay [lower price] just for you because this convo has been different 💕", "DOWNGRADE 20-30%. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "it's cool love, I'm not going anywhere... I actually like talking to you 😏", "SEED. Continue GFE."),
        ], "obj"),
        "price2": ([
            ("Step1 Reframe", "that's literally less than your morning coffee and this is gonna stay with you way longer", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "I'm feeling so open rn because of you and I really want you to see what that looks like 😏", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "most guys would do anything to see this honestly, thought you were different", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "okay [lower price] because you genuinely make me feel something, keep that between us 💕", "DOWNGRADE. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "no pressure at all, I'm just enjoying having you here 😏", "SEED."),
        ], "obj"),
        # ── DISCOUNT ──
        "discount1": ([
            ("Step1 Firmness", "a discount? babe do I look like I'm on clearance? 😏 what I'm sharing is personal and it's worth it", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "I only share this with guys who really appreciate what they're getting", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "okay [lower price] just this once because I genuinely like you, but this stays between us 😏", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "if you don't want it that's fine, I'll keep it to myself then", "TAKEAWAY."),
        ], "obj"),
        "discount2": ([
            ("Step1 Firmness", "haha you really just asked me for a discount? I don't do sales babe 😏", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "the guys who really want me don't negotiate, just saying", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "fine [lower price] but ONLY because you've been making me feel some type of way, one time thing", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "okay I'll save it for someone who actually wants it then 😏", "TAKEAWAY."),
        ], "obj"),
        # ── FREE ──
        "free1": ([
            ("Step1 Reminder", "I already sent you one for free remember? this one is on a whole other level 😏", "REMINDER. Still wants free → Step 2."),
            ("Step2 Challenge", "free? babe I don't just hand this out... you have to earn the good stuff", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I literally did this because of what YOU said to me, it wasn't random content", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "it's cool, I'm just happy you're here honestly 💕", "SEED."),
        ], "obj"),
        "free2": ([
            ("Step1 Reminder", "you already got a freebie and this one goes way further trust me 😏", "REMINDER. Still → Step 2."),
            ("Step2 Challenge", "the best things aren't free babe 😏 but they're definitely worth it", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I did this because of you specifically, because of our convo, that took real vulnerability for me", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "no pressure, I just like talking to you 💕", "SEED."),
        ], "obj"),
        # ── NOMONEY ──
        "nomoney1": ([
            ("Step1 Empathy", "hey I totally get it, no pressure at all okay? 😏", "EMPATHY. Still engaged → Step 2."),
            ("Step2 Test", "not even like [small amount]? I really want you to see this one", "TEST $3-5. Still no → Step 3."),
            ("Step3 PWYW", "just send whatever you can babe, even a tiny amount, I need you to see what you made me do", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "honestly it's fine, I like talking to you regardless... you actually make me feel something 💕", "PROTECT."),
        ], "obj"),
        "nomoney2": ([
            ("Step1 Empathy", "that's totally fine, don't even worry about it 😏", "EMPATHY. Still → Step 2."),
            ("Step2 Test", "what about just [small amount]? I really don't want you to miss this", "TEST. Still no → Step 3."),
            ("Step3 PWYW", "send whatever feels right, even $1... I can't keep this from you", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "it's okay, you being here is what matters to me 💕", "PROTECT."),
        ], "obj"),
        # ── NOPPV ──
        "noppv1": ([
            ("Step1 Accept", "that's totally fine I'm not trying to sell you anything, I genuinely like talking to you 😏", "ACCEPT. Continue sexting 4-5 msgs before Step 2."),
            ("Step2 Reframe", "look this isn't about money... I just want you to see what you're doing to me rn, this doesn't happen often", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "just send whatever you want, even $1, I can't keep this to myself", "PWYW."),
        ], "obj"),
        "noppv2": ([
            ("Step1 Accept", "no worries at all, I don't care about that I'm just enjoying this 💕", "ACCEPT. Continue sexting 4-5 msgs before Step 2."),
            ("Step2 Reframe", "forget about money for a sec... I just want to share this with you, what I'm feeling is real 😏", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "send me anything, even the smallest amount, I need you to see what you did to me", "PWYW."),
        ], "obj"),
        # ── CARD ──
        "card1": ([
            ("Step1 Retry", "ugh that's annoying, happens sometimes though try again it usually works the second time 😏", "RETRY. Still fails → Step 2."),
            ("Step2 AltCard", "try a different card? I really don't want you to miss this", "ALTERNATIVE. Still fails → Step 3."),
            ("Step3 Urgency", "figure it out soon babe, I'm in this mood and it's not gonna last forever", "URGENCY."),
        ], "obj"),
        "card2": ([
            ("Step1 Retry", "ugh that sucks, just try one more time it usually fixes itself", "RETRY. Still → Step 2."),
            ("Step2 AltCard", "do you have another card? I really want you to see this 😏", "ALTERNATIVE. Still → Step 3."),
            ("Step3 Urgency", "I want you to see this while I'm still in this mood, it won't last forever", "URGENCY."),
        ], "obj"),

        # ── NOSEX ──
        "nosex1": ([
            ("Step1 Respect", "haha okay I got a little ahead of myself, you're just too fun to talk to 😏", "RESPECT. Still no → Step 2."),
            ("Step2 Subtle", "so tell me more about you... what gets you going when everything else is boring?", "SUBTLE TENSION. → Step 3 later."),
            ("Step3 ReAttempt", "I can't help it, there's something about you that's getting to me rn", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "okay I'll behave... for now 😏 no promises though", "ACCEPT. Door open."),
        ], "res"),
        "nosex2": ([
            ("Step1 Respect", "my bad I got carried away, it's your fault for having this energy 😏", "RESPECT. Still no → Step 2."),
            ("Step2 Subtle", "okay new topic, what's the craziest thing you've ever done?", "SUBTLE. → Step 3 later."),
            ("Step3 ReAttempt", "I'm trying to behave but you're making it really hard... there's just something about you", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "fine I'll stop but don't blame me when it comes back later 😏", "ACCEPT."),
        ], "res"),
        # ── OFFTOPIC ──
        "offtopic1": ([
            ("Step1 Acknowledge", "haha wait that's actually cute 😏", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "but hold on you totally distracted me, I was about to tell you something", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay wait I remember now, so like I was saying...", "RETAKE. Resume main script."),
        ], "res"),
        "offtopic2": ([
            ("Step1 Acknowledge", "lol that's so random but I kinda love it 😏", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "wait no stop you're distracting me from what I was gonna share with you", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay focus, where was I... oh right", "RETAKE."),
        ], "res"),
        # ── REAL ──
        "real1": ([
            ("Step1 Humor", "lol do I look like a bot to you? ask me literally anything 😏", "HUMOR. Still doubts → Step 2."),
            ("Step2 Challenge", "go ahead test me, what do you wanna know? I'm an open book babe", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I get it there's a lot of fake stuff on here, but you felt something in this convo right? because I definitely did 💕", "GROUNDING."),
        ], "res"),
        "real2": ([
            ("Step1 Humor", "wait you think I'm not real?? that's the funniest and cutest thing anyone's said to me today 😏", "HUMOR. Still → Step 2."),
            ("Step2 Challenge", "go ahead, ask me something only a real person would know", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I know there's lots of bots on here but what we talked about felt real to me. didn't it feel real to you? 💕", "GROUNDING."),
        ], "res"),
        # ── VOICE (No Video Calls — dodge/redirect) ──
        "voice1": ([
            ("Step1 Dodge", "haha maybe one day if you earn it but not yet... I'm private about that stuff 😏", "DODGE. Zansi does NOT do video calls. Still asks → Step 2."),
            ("Step2 Redirect", "I have something way better for you though, trust me you'll forget you even asked", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "I don't do that on here but what I'm about to show you is better than any call... you'll see 😏", "FIRM."),
        ], "res"),
        "voice2": ([
            ("Step1 Dodge", "hmm maybe but you gotta earn that first 😏", "DODGE. Still → Step 2."),
            ("Step2 Redirect", "how about instead of a call I show you something that'll blow your mind?", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "that's not something I do on here but what I have for you is way better, trust me", "FIRM."),
        ], "res"),
        # ── CUSTOMYES ──
        "customyes1": ([
            ("Step1 Tease", "ooh you want that? I might have exactly what you're looking for 😏", "TEASE. → Step 2."),
            ("Step2 Price", "I have something you're gonna lose your mind over... [price]", "PRICE. Customs start at $200. Never mention per-minute rates."),
            ("Step3 Close", "trust me babe you won't regret it, I put everything into this one", "CLOSE."),
        ], "res"),
        "customyes2": ([
            ("Step1 Tease", "ooh good taste... I think I know exactly what you need 😏", "TEASE. → Step 2."),
            ("Step2 Price", "I actually have something just like that, [price] and it's worth every penny", "PRICE. Customs $200+."),
            ("Step3 Close", "you're not gonna be able to stop watching this one 😏", "CLOSE."),
        ], "res"),
        # ── CUSTOMNO ──
        "customno1": ([
            ("Step1 Redirect", "I don't have exactly that but I have something that'll make you forget you even asked 😏", "REDIRECT. No B/G, No G/G. Redirect to what she HAS (solo, anal, squirting)."),
            ("Step2 Alternative", "what I have might actually be even better and nobody else has seen it yet", "ALTERNATIVE + FOMO. → Step 3."),
            ("Step3 Close", "trust me babe... I know what you need better than you do 😏", "CLOSE."),
        ], "res"),
        "customno2": ([
            ("Step1 Redirect", "I don't have that specific thing but I have something you're gonna love even more", "REDIRECT. → Step 2."),
            ("Step2 Alternative", "what I DO have is something nobody has ever seen and I think it's hotter than what you asked for 😏", "ALTERNATIVE. → Step 3."),
            ("Step3 Close", "just trust me on this one 💕", "CLOSE."),
        ], "res"),
        # ── DONE ──
        "done1": ([
            ("Step1 Validate", "already? damn that's hot knowing I did that to you 😏", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "but I'm not finished yet... you're really gonna leave me like this?", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "next time you HAVE to wait for me because what I have planned is so much better 😏", "SEED."),
        ], "res"),
        "done2": ([
            ("Step1 Validate", "wait that fast?? okay that's actually really flattering 😏", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "but I haven't even finished babe, you can't just leave me hanging", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "okay but next time you're holding it until I say so 😏", "SEED."),
        ], "res"),

        # ── SITUATIONAL ──
        "cumcontrol": ([
            ("edge1", "not yet... I'm not ready to let go of this feeling 😏", "EDGE. More PPVs left."),
            ("edge2", "hold on, stay with me a little longer... I need more of you", "EDGE variant."),
            ("sync1", "I'm so close... let's finish together, but see this first 😏", "SYNC. Final PPV."),
            ("sync2", "wait for me, I want us to let go at the same time... open this first", "SYNC variant."),
            ("delay1", "hold on... trust me you want to wait for what's coming", "DELAY."),
            ("delay2", "don't finish yet, I have something that'll make it so much better 😏", "DELAY variant."),
        ], "sit"),
        "dickpic": ([
            ("dpsext1", "oh wow... that's really hot. you have no idea what you just did to me 😏", "DURING SEXTING."),
            ("dpsext2", "oh damn... okay I need to show you something right now", "DURING SEXTING variant."),
            ("dprapport1", "wow you're bold haha... not gonna lie that's actually really flattering 😏", "DURING RAPPORT."),
            ("dprapport2", "oh I was not expecting that but... I'm definitely not complaining", "DURING RAPPORT variant."),
            ("dpppv1", "you can't just send me that and expect me to sit still, hold on 😏", "LEVERAGE → send PPV."),
            ("dpppv2", "okay you just did something to me... give me a sec", "LEVERAGE variant."),
        ], "sit"),
        "boosters": ([
            ("h1", "fuckk", "MID-SEXTING BOOSTER."),
            ("h2", "I'm so wet rn because of you 😏", "BOOSTER. Ego."),
            ("h3", "yes", "BOOSTER. Micro."),
            ("h4", "you're driving me crazy right now", "BOOSTER."),
            ("h5", "I literally can't think about anything else", "BOOSTER."),
            ("h6", "my whole body is on fire 😏", "BOOSTER. Physical."),
            ("h7", "don't stop...", "BOOSTER. Ultra micro."),
            ("h8", "I should be at the gym but the only workout I want rn involves you 😏", "BOOSTER. Zansi personality."),
        ], "sit"),
    },
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
