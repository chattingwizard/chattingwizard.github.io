"""
Default OBJ/RES/SIT scripts — tone 7/10 (challenging, confident, dominant but playful).

Three base templates by gender:
  - DEFAULT_OBJ_FEMALE  → female creators
  - DEFAULT_OBJ_MALE    → male creators (straight / dating app women)
  - DEFAULT_OBJ_MALE_GAY → male creators targeting gay audience

Tone guidelines (7/10):
  - Model NEVER apologizes for selling
  - Frame control: "this is worth what it's worth, period"
  - Challenge is direct but playful, not aggressive
  - FOMO is real, temporal, specific
  - Seed without weakness: "we'll talk" NOT "it's okay baby I like you anyway"
  - Downgrade as a FAVOR, not desperation
  - Alternate positive/negative motivation
"""

# ═══════════════════════════════════════════════════════════════
# FEMALE CREATORS — DEFAULT OBJ SCRIPTS (7/10 tone)
# ═══════════════════════════════════════════════════════════════

DEFAULT_OBJ_FEMALE = {
    # ── PRICE ──
    "price1": ([
        ("Step1 Reframe", "babe that's less than your morning coffee and I promise this is gonna keep you up way longer", "REFRAME. Still no → Step 2."),
        ("Step2 FOMO", "I'm literally dripping rn because of what you said and this mood isn't gonna last, don't miss it", "FOMO. Still no → Step 3."),
        ("Step3 Challenge", "honestly? most guys couldn't handle what I just recorded... I thought you were different", "CHALLENGE. Still no → Step 4."),
        ("Step4 Downgrade", "fine, [lower price] but only because you've been making me feel some type of way, don't tell anyone I did this", "DOWNGRADE 20-30%. ONE TIME. Still no → Step 5."),
        ("Step5 Seed", "alright, I'll keep it then... but next time I'm in this mood you better be ready", "SEED. Continue GFE."),
    ], "obj"),
    "price2": ([
        ("Step1 Reframe", "baby it's literally nothing for what you're about to see, trust me you'll be thanking me after", "REFRAME. Still no → Step 2."),
        ("Step2 FOMO", "this mood won't last and I already picked YOU to share it with, don't make me regret that", "FOMO. Still no → Step 3."),
        ("Step3 Challenge", "maybe you're just not ready for what I did... it's a lot", "CHALLENGE. Still no → Step 4."),
        ("Step4 Downgrade", "look, [lower price] because I actually want YOU to have this one, I'm not doing this for anyone else", "DOWNGRADE. ONE TIME. Still no → Step 5."),
        ("Step5 Seed", "I'll hold onto it for now, but I know you're gonna come back for it", "SEED."),
    ], "obj"),

    # ── DISCOUNT ──
    "discount1": ([
        ("Step1 Firmness", "haha negotiate? baby this isn't a flea market... you already know this is worth every penny", "FIRMNESS. Still → Step 2."),
        ("Step2 Challenge", "the guys who get my best stuff don't ask for discounts, they know what they're getting", "CHALLENGE. Still → Step 3."),
        ("Step3 Concession", "ugh fine, [lower price] ONLY because I like you but don't ever ask me this again", "CONCESSION. ONE TIME. Still no → Step 4."),
        ("Step4 Takeaway", "okay I'll just save this for someone who actually wants it then, their loss isn't your gain though", "TAKEAWAY."),
    ], "obj"),
    "discount2": ([
        ("Step1 Firmness", "a discount? babe do I look like I'm on sale? you know exactly what you're getting", "FIRMNESS. Still → Step 2."),
        ("Step2 Challenge", "I don't do this for just anyone, and the ones who get it never complain about the price after", "CHALLENGE. Still → Step 3."),
        ("Step3 Concession", "okay [lower price] and that's ONLY because this convo has been different, first and last time", "CONCESSION. ONE TIME. Still no → Step 4."),
        ("Step4 Takeaway", "no worries, I'll keep it... someone else has been asking and they won't hesitate", "TAKEAWAY."),
    ], "obj"),

    # ── FREE ──
    "free1": ([
        ("Step1 Reminder", "baby I already gave you one for free remember? this one is on another level and you know it", "REMINDER. Still → Step 2."),
        ("Step2 Challenge", "free? I don't just hand this out, you have to earn the best stuff from me", "CHALLENGE. Still → Step 3."),
        ("Step3 Guilt", "I literally spent time making this because of what YOU said to me, this wasn't random content, this was for you", "GUILT. Still no → Step 4."),
        ("Step4 Seed", "I'll keep it then, but just know I made it thinking about you", "SEED."),
    ], "obj"),
    "free2": ([
        ("Step1 Reminder", "you already got a free preview and this is ten times crazier, you know I don't do free twice", "REMINDER. Still → Step 2."),
        ("Step2 Challenge", "the best things aren't free baby, especially not what I just did", "CHALLENGE. Still → Step 3."),
        ("Step3 Guilt", "I recorded this because of our conversation, specifically because of YOU, it took effort and I did it for you", "GUILT. Still no → Step 4."),
        ("Step4 Seed", "okay I'll hold onto it, but it's got your name on it", "SEED."),
    ], "obj"),

    # ── NOMONEY ──
    "nomoney1": ([
        ("Step1 Empathy", "I hear you baby, that's okay", "EMPATHY. Still → Step 2."),
        ("Step2 Test", "not even [small amount]? I really want you to be the one who sees this", "TEST $3-5. Still no → Step 3."),
        ("Step3 PWYW", "send whatever you can, even something small, I just need you to see what you made me do", "PWYW. Still no → Step 4."),
        ("Step4 Protect", "it's fine, you're still here and that's what matters to me right now", "PROTECT."),
    ], "obj"),
    "nomoney2": ([
        ("Step1 Empathy", "okay don't stress about it", "EMPATHY. Still → Step 2."),
        ("Step2 Test", "what about just [small amount]? I'd hate for you to miss this one", "TEST. Still no → Step 3."),
        ("Step3 PWYW", "just send whatever feels right, I can't keep this from you", "PWYW. Still no → Step 4."),
        ("Step4 Protect", "you being here talking to me is enough for now", "PROTECT."),
    ], "obj"),

    # ── NOPPV ──
    "noppv1": ([
        ("Step1 Accept", "that's fine, I'm not trying to sell you anything, I'm just enjoying this", "ACCEPT. Continue sexting 4-5 msgs before Step 2."),
        ("Step2 Reframe", "okay forget about money, this isn't about that, I need you to see what you're doing to me rn because I've never reacted like this", "REFRAME. Still no → Step 3."),
        ("Step3 PWYW", "send me whatever you want, literally anything, I just can't keep this to myself, you need to see it", "PWYW."),
    ], "obj"),
    "noppv2": ([
        ("Step1 Accept", "no worries, I don't care about that rn, this convo is what I care about", "ACCEPT. Continue sexting 4-5 msgs before Step 2."),
        ("Step2 Reframe", "forget the money part for a sec, I want to share this moment with you because what you're making me feel is real", "REFRAME. Still no → Step 3."),
        ("Step3 PWYW", "send anything, even the smallest amount, you need to see what you did to me", "PWYW."),
    ], "obj"),

    # ── CARD ──
    "card1": ([
        ("Step1 Retry", "ugh that's annoying, try again baby it usually works the second time", "RETRY. Still → Step 2."),
        ("Step2 AltCard", "maybe try a different card? I really don't want you to miss this", "ALTERNATIVE. Still → Step 3."),
        ("Step3 Urgency", "figure it out soon because this mood I'm in right now isn't gonna last and I want you to have it", "URGENCY."),
    ], "obj"),
    "card2": ([
        ("Step1 Retry", "that happens sometimes, try one more time for me", "RETRY. Still → Step 2."),
        ("Step2 AltCard", "do you have another card? because you really don't want to miss what I made for you", "ALTERNATIVE. Still → Step 3."),
        ("Step3 Urgency", "baby fix it quick, I don't keep stuff like this around forever", "URGENCY."),
    ], "obj"),

    # ── NOSEX ──
    "nosex1": ([
        ("Step1 Respect", "haha okay I got a little carried away, you're too easy to talk to", "RESPECT. Still → Step 2."),
        ("Step2 Subtle", "so tell me more about you... what do you do when you're not making girls on the internet lose focus?", "SUBTLE. → Step 3 later."),
        ("Step3 ReAttempt", "okay but I can't help it, there's something about you that keeps messing with my head", "RE-ATTEMPT. Still no → Step 4."),
        ("Step4 Accept", "alright I'll behave, for now... no promises though", "ACCEPT. Door open."),
    ], "res"),
    "nosex2": ([
        ("Step1 Respect", "my bad I got ahead of myself, it's your fault for being this fun to talk to", "RESPECT. Still → Step 2."),
        ("Step2 Subtle", "okay new topic, what's the most adventurous thing you've ever done?", "SUBTLE. → Step 3 later."),
        ("Step3 ReAttempt", "I'm trying so hard to behave but you make it impossible", "RE-ATTEMPT. Still no → Step 4."),
        ("Step4 Accept", "fine I'll stop, but don't blame me when it happens again", "ACCEPT."),
    ], "res"),

    # ── OFFTOPIC ──
    "offtopic1": ([
        ("Step1 Acknowledge", "haha okay that's actually funny", "ACKNOWLEDGE. Adapt to what he said. → Step 2."),
        ("Step2 Redirect", "but wait you totally distracted me, I was about to say something and now you made me lose my train of thought", "REDIRECT. → Step 3."),
        ("Step3 Retake", "okay wait I remember now, so like I was saying...", "RETAKE. Resume main script."),
    ], "res"),
    "offtopic2": ([
        ("Step1 Acknowledge", "omg okay random but I love it", "ACKNOWLEDGE. Adapt. → Step 2."),
        ("Step2 Redirect", "wait no stop, you're distracting me from what I was going to tell you", "REDIRECT. → Step 3."),
        ("Step3 Retake", "OKAY focus, where was I... oh yeah", "RETAKE."),
    ], "res"),

    # ── REAL ──
    "real1": ([
        ("Step1 Humor", "lol do I sound like a robot to you? beep boop... send $5 for human verification haha I'm kidding", "HUMOR. Still → Step 2."),
        ("Step2 Challenge", "ask me anything, literally anything about my life, I'm an open book, go ahead", "CHALLENGE. Still → Step 3."),
        ("Step3 Grounding", "I get why you'd think that, there's a lot of fake stuff on here, but what we've been talking about felt real to me... didn't it feel real to you?", "GROUNDING."),
    ], "res"),
    "real2": ([
        ("Step1 Humor", "wait you think I'm fake?? that might be the funniest thing anyone's said to me today", "HUMOR. Still → Step 2."),
        ("Step2 Challenge", "test me then, ask me something only a real person would know, go ahead", "CHALLENGE. Still → Step 3."),
        ("Step3 Grounding", "I know there's a lot of bots out here but what we've been talking about... that felt different, you felt it too right?", "GROUNDING."),
    ], "res"),

    # ── VOICE ──
    "voice1": ([
        ("Step1 Dodge", "haha maybe one day if you earn it, but not yet", "DODGE. Model does NOT do video calls. Still → Step 2."),
        ("Step2 Redirect", "I have something way better for you though, trust me you'll forget you even asked", "REDIRECT. Still → Step 3."),
        ("Step3 Firm", "I don't do that on here but what I'm about to show you is better than any call, you'll see", "FIRM. No video calls."),
    ], "res"),
    "voice2": ([
        ("Step1 Dodge", "hmmm you gotta earn that first", "DODGE. Still → Step 2."),
        ("Step2 Redirect", "how about instead of a call I show you something that'll actually blow your mind?", "REDIRECT. Still → Step 3."),
        ("Step3 Firm", "I don't do that here but trust me what I have is way better than my voice", "FIRM."),
    ], "res"),

    # ── CUSTOMYES ──
    "customyes1": ([
        ("Step1 Tease", "mmm you want that? I might have exactly what you're thinking of", "TEASE. → Step 2."),
        ("Step2 Price", "I have it and you're gonna lose your mind... [price]", "PRICE. Set based on content."),
        ("Step3 Close", "trust me you won't regret it, I made this one special", "CLOSE."),
    ], "res"),
    "customyes2": ([
        ("Step1 Tease", "ohhh you have good taste, I think I know exactly what you need", "TEASE. → Step 2."),
        ("Step2 Price", "I made something just like that, [price] and it's worth every penny", "PRICE."),
        ("Step3 Close", "you're not gonna be able to stop watching this one", "CLOSE."),
    ], "res"),

    # ── CUSTOMNO ──
    "customno1": ([
        ("Step1 Redirect", "I don't have exactly that but I have something that'll make you forget you even asked", "REDIRECT. → Step 2."),
        ("Step2 Alternative", "what I have might be even crazier and literally no one else has seen it", "ALTERNATIVE + FOMO. → Step 3."),
        ("Step3 Close", "trust me, I know what you need better than you do", "CLOSE."),
    ], "res"),
    "customno2": ([
        ("Step1 Redirect", "hmm not exactly that but what I DO have is gonna hit even harder", "REDIRECT. → Step 2."),
        ("Step2 Alternative", "nobody has seen what I'm about to show you and I think it's better than what you asked for", "ALTERNATIVE. → Step 3."),
        ("Step3 Close", "just trust me on this one, you'll thank me after", "CLOSE."),
    ], "res"),

    # ── DONE ──
    "done1": ([
        ("Step1 Validate", "fuck that's so hot, you came because of me??", "VALIDATE. → Step 2."),
        ("Step2 Rescue", "but I haven't finished yet... you're really gonna leave me like this?", "RESCUE. Still no → Step 3."),
        ("Step3 Seed", "next time you HAVE to wait for me, I have something insane planned for round 2", "SEED."),
    ], "res"),
    "done2": ([
        ("Step1 Validate", "already?? damn that's hot", "VALIDATE. → Step 2."),
        ("Step2 Rescue", "wait but I'm not done yet, don't you wanna watch me finish too?", "RESCUE. Still no → Step 3."),
        ("Step3 Seed", "okay but next time you hold it, because what I have planned is way crazier", "SEED."),
    ], "res"),

    # ── SITUATIONAL ──
    "cumcontrol": ([
        ("edge1", "don't cum yet, I'm not done with you", "CONTROL."),
        ("edge2", "hold it, not yet... I need you to last longer for me", "EDGE variant."),
        ("sync1", "I'm so close too, cum with me... but you need to see this first", "SYNC. Send PPV."),
        ("sync2", "wait for me, I want us to finish together, open this first", "SYNC variant."),
        ("delay1", "hold it, I want you to wait until you see what I'm about to send, trust me it's worth the wait", "DELAY. Send PPV."),
        ("delay2", "don't you dare finish before you see this", "DELAY variant."),
    ], "sit"),
    "dickpic": ([
        ("dpsext1", "fuck okay that's... wow, you have no idea what that just did to me", "DURING SEXTING."),
        ("dpsext2", "oh fuck that is... damn, I need to show you something rn", "DURING SEXTING variant."),
        ("dprapport1", "omg you don't waste time huh, that's actually really hot ngl", "DURING RAPPORT."),
        ("dprapport2", "woah I wasn't expecting that but... damn okay", "DURING RAPPORT variant."),
        ("dpppv1", "you can't just send me that and expect me to do nothing about it, hold on...", "LEVERAGE. WAIT 1-2 min then send PPV."),
        ("dpppv2", "okay you just made me do something, give me a sec", "LEVERAGE variant."),
    ], "sit"),
    "boosters": ([
        ("h1", "fuckkk", "MID-SEXTING BOOSTER."),
        ("h2", "I'm so wet rn because of you", "BOOSTER. Ego."),
        ("h3", "don't stop", "BOOSTER. Micro."),
        ("h4", "you have no idea what you're doing to me", "BOOSTER."),
        ("h5", "I can't think straight rn", "BOOSTER."),
        ("h6", "my hands are shaking", "BOOSTER. Physical."),
        ("h7", "more", "BOOSTER. Ultra micro."),
        ("h8", "I literally can't focus on anything else rn", "BOOSTER."),
    ], "sit"),
}


# ═══════════════════════════════════════════════════════════════
# MALE CREATORS (straight / dating app women) — DEFAULT OBJ SCRIPTS (7/10 tone)
# ═══════════════════════════════════════════════════════════════

DEFAULT_OBJ_MALE = {
    # ── PRICE ──
    "price1": ([
        ("Step1 Reframe", "that's less than your morning coffee and trust me this hits way harder", "REFRAME. Still no → Step 2."),
        ("Step2 FOMO", "I'm only in this mood because of you rn, no guarantee it happens again", "FOMO. Still no → Step 3."),
        ("Step3 Challenge", "maybe you're not ready for what I just did in this one", "CHALLENGE. Still no → Step 4."),
        ("Step4 Downgrade", "alright [lower price] but only because this convo has been different, don't tell anyone", "DOWNGRADE 20-30%. ONE TIME. Still no → Step 5."),
        ("Step5 Seed", "I'll hold onto it then, but next time I'm feeling like this you better be ready", "SEED. Continue."),
    ], "obj"),
    "price2": ([
        ("Step1 Reframe", "it's literally nothing for what you're about to see, you'll be replaying this one", "REFRAME. Still no → Step 2."),
        ("Step2 FOMO", "this doesn't happen often and I already chose you to share it with, don't make me regret it", "FOMO. Still no → Step 3."),
        ("Step3 Challenge", "I don't think you're ready for this one honestly, it's a lot", "CHALLENGE. Still no → Step 4."),
        ("Step4 Downgrade", "[lower price] because I actually want you to have this one, I'm not making this offer to anyone else", "DOWNGRADE. ONE TIME. Still no → Step 5."),
        ("Step5 Seed", "I'll keep it for now, but I know you'll come back for it", "SEED."),
    ], "obj"),

    # ── DISCOUNT ──
    "discount1": ([
        ("Step1 Firmness", "haha negotiate? this isn't a sale babe, you know exactly what you're getting", "FIRMNESS. Still → Step 2."),
        ("Step2 Challenge", "the girls who get my best stuff never ask for discounts, they know what it's worth", "CHALLENGE. Still → Step 3."),
        ("Step3 Concession", "fine [lower price] ONLY because I like you, but don't ever ask me this again", "CONCESSION. ONE TIME. Still no → Step 4."),
        ("Step4 Takeaway", "okay I'll keep it then, someone else has been asking and they won't hesitate", "TAKEAWAY."),
    ], "obj"),
    "discount2": ([
        ("Step1 Firmness", "a discount? do I look like I'm on sale?", "FIRMNESS. Still → Step 2."),
        ("Step2 Challenge", "the ones who really want it don't ask for discounts, just saying", "CHALLENGE. Still → Step 3."),
        ("Step3 Concession", "[lower price] because you've been making me feel a type of way, first and last time", "CONCESSION. ONE TIME. Still no → Step 4."),
        ("Step4 Takeaway", "no problem, I'll save it for someone who really wants it", "TAKEAWAY."),
    ], "obj"),

    # ── FREE ──
    "free1": ([
        ("Step1 Reminder", "I already gave you one for free remember? this one is way crazier, you know I don't do free twice", "REMINDER. Still → Step 2."),
        ("Step2 Challenge", "free? I don't just hand this out, you have to earn the best stuff", "CHALLENGE. Still → Step 3."),
        ("Step3 Guilt", "I made this because of what YOU said to me, this wasn't random, I did it for you", "GUILT. Still no → Step 4."),
        ("Step4 Seed", "I'll keep it then, but it's got your name on it", "SEED."),
    ], "obj"),
    "free2": ([
        ("Step1 Reminder", "you already got the free preview, this one is ten times better", "REMINDER. Still → Step 2."),
        ("Step2 Challenge", "the best things aren't free babe, especially not what I just recorded", "CHALLENGE. Still → Step 3."),
        ("Step3 Guilt", "I recorded this because of our conversation, specifically because of you, and it took time", "GUILT. Still no → Step 4."),
        ("Step4 Seed", "okay I'll hold onto it for now", "SEED."),
    ], "obj"),

    # ── NOMONEY ──
    "nomoney1": ([
        ("Step1 Empathy", "I hear you, that's okay", "EMPATHY. Still → Step 2."),
        ("Step2 Test", "not even [small amount]? I really want you to be the one who sees this", "TEST $3-5. Still no → Step 3."),
        ("Step3 PWYW", "send whatever you can, even something small, I just need you to see what you made me do", "PWYW. Still no → Step 4."),
        ("Step4 Protect", "it's fine, you're here and that's what counts right now", "PROTECT."),
    ], "obj"),
    "nomoney2": ([
        ("Step1 Empathy", "don't stress about it", "EMPATHY. Still → Step 2."),
        ("Step2 Test", "what about just [small amount]? would hate for you to miss this one", "TEST. Still no → Step 3."),
        ("Step3 PWYW", "send whatever feels right, I can't keep this from you", "PWYW. Still no → Step 4."),
        ("Step4 Protect", "you being here is enough for now", "PROTECT."),
    ], "obj"),

    # ── NOPPV ──
    "noppv1": ([
        ("Step1 Accept", "that's fine, I'm just enjoying this", "ACCEPT. Continue sexting 4-5 msgs before Step 2."),
        ("Step2 Reframe", "forget about money, this isn't about that, I need you to see what you're doing to me rn because I've never reacted like this", "REFRAME. Still no → Step 3."),
        ("Step3 PWYW", "send whatever you want, literally anything, you need to see this", "PWYW."),
    ], "obj"),
    "noppv2": ([
        ("Step1 Accept", "no worries, I don't care about that, this convo is what I care about", "ACCEPT. Continue sexting 4-5 msgs before Step 2."),
        ("Step2 Reframe", "forget the money part, I want to share this with you because what you're making me feel is real", "REFRAME. Still no → Step 3."),
        ("Step3 PWYW", "send anything, even the smallest amount, you need to see what you did to me", "PWYW."),
    ], "obj"),

    # ── CARD ──
    "card1": ([
        ("Step1 Retry", "ugh that's annoying, try again it usually works the second time", "RETRY. Still → Step 2."),
        ("Step2 AltCard", "maybe try a different card? you really don't want to miss this", "ALTERNATIVE. Still → Step 3."),
        ("Step3 Urgency", "figure it out soon because this mood isn't gonna last and I want you to have it", "URGENCY."),
    ], "obj"),
    "card2": ([
        ("Step1 Retry", "that happens sometimes, try one more time", "RETRY. Still → Step 2."),
        ("Step2 AltCard", "you have another card? because you don't want to miss what I made for you", "ALTERNATIVE. Still → Step 3."),
        ("Step3 Urgency", "fix it quick, I don't keep stuff like this around forever", "URGENCY."),
    ], "obj"),

    # ── NOSEX ──
    "nosex1": ([
        ("Step1 Respect", "haha okay I got carried away, you're too easy to talk to", "RESPECT. Still → Step 2."),
        ("Step2 Subtle", "so tell me more about you, what do you do when you're not driving guys on the internet crazy?", "SUBTLE. → Step 3 later."),
        ("Step3 ReAttempt", "I can't help it though, there's something about you that keeps messing with my head", "RE-ATTEMPT. Still no → Step 4."),
        ("Step4 Accept", "alright I'll behave, for now, no promises", "ACCEPT. Door open."),
    ], "res"),
    "nosex2": ([
        ("Step1 Respect", "my bad I got ahead of myself, your fault for being this fun", "RESPECT. Still → Step 2."),
        ("Step2 Subtle", "okay new topic, what's the craziest thing you've ever done?", "SUBTLE. → Step 3 later."),
        ("Step3 ReAttempt", "I'm trying so hard to behave but you make it impossible honestly", "RE-ATTEMPT. Still no → Step 4."),
        ("Step4 Accept", "fine I'll stop, don't blame me when it happens again though", "ACCEPT."),
    ], "res"),

    # ── OFFTOPIC ──
    "offtopic1": ([
        ("Step1 Acknowledge", "haha okay that's actually funny", "ACKNOWLEDGE. Adapt. → Step 2."),
        ("Step2 Redirect", "but wait you totally distracted me, I was about to say something and now you made me lose my thought", "REDIRECT. → Step 3."),
        ("Step3 Retake", "okay wait I remember, so like I was saying...", "RETAKE. Resume main script."),
    ], "res"),
    "offtopic2": ([
        ("Step1 Acknowledge", "okay that's random but I'm here for it", "ACKNOWLEDGE. Adapt. → Step 2."),
        ("Step2 Redirect", "wait no stop, you're distracting me from what I was gonna tell you", "REDIRECT. → Step 3."),
        ("Step3 Retake", "OKAY focus, where was I... oh yeah", "RETAKE."),
    ], "res"),

    # ── REAL ──
    "real1": ([
        ("Step1 Humor", "lol a robot? do robots make you feel like this? didn't think so", "HUMOR. Still → Step 2."),
        ("Step2 Challenge", "ask me anything, literally anything about me or my life, I'll prove it, go ahead", "CHALLENGE. Still → Step 3."),
        ("Step3 Grounding", "I get why you'd think that, there's a lot of fake stuff on here, but what we've been talking about felt real to me, didn't it feel real to you?", "GROUNDING."),
    ], "res"),
    "real2": ([
        ("Step1 Humor", "wait you think I'm fake?? that's the funniest thing I've heard all day", "HUMOR. Still → Step 2."),
        ("Step2 Challenge", "test me then, ask me something only a real person would know", "CHALLENGE. Still → Step 3."),
        ("Step3 Grounding", "I know there's a lot of bots on here but what we've been talking about felt different, you felt it too right?", "GROUNDING."),
    ], "res"),

    # ── VOICE ──
    "voice1": ([
        ("Step1 Dodge", "haha maybe if you earn it, not yet though", "DODGE. Still → Step 2."),
        ("Step2 Redirect", "I have something way better for you, trust me you'll forget you even asked", "REDIRECT. Still → Step 3."),
        ("Step3 Firm", "I don't do that on here but what I'm about to show you is better than any call", "FIRM. No video calls."),
    ], "res"),
    "voice2": ([
        ("Step1 Dodge", "you gotta earn that first", "DODGE. Still → Step 2."),
        ("Step2 Redirect", "how about instead of a call I show you something that'll blow your mind?", "REDIRECT. Still → Step 3."),
        ("Step3 Firm", "that's not something I do here but trust me what I have is way better", "FIRM."),
    ], "res"),

    # ── CUSTOMYES ──
    "customyes1": ([
        ("Step1 Tease", "mmm you want that? I might have exactly what you're thinking of", "TEASE. → Step 2."),
        ("Step2 Price", "I have exactly what you need and you're gonna lose your mind, [price]", "PRICE. Set based on content."),
        ("Step3 Close", "trust me you won't regret it, this one is special", "CLOSE."),
    ], "res"),
    "customyes2": ([
        ("Step1 Tease", "ohhh good taste, I think I know exactly what you need", "TEASE. → Step 2."),
        ("Step2 Price", "I have it, [price] and it's worth every penny", "PRICE."),
        ("Step3 Close", "you're not gonna be able to stop watching", "CLOSE."),
    ], "res"),

    # ── CUSTOMNO ──
    "customno1": ([
        ("Step1 Redirect", "I don't have exactly that but I have something that'll make you forget you asked", "REDIRECT. → Step 2."),
        ("Step2 Alternative", "what I have might be even crazier and nobody else has seen it", "ALTERNATIVE + FOMO. → Step 3."),
        ("Step3 Close", "trust me, I know what you need better than you do", "CLOSE."),
    ], "res"),
    "customno2": ([
        ("Step1 Redirect", "not exactly that but what I DO have is gonna hit even harder", "REDIRECT. → Step 2."),
        ("Step2 Alternative", "nobody has seen what I'm about to show you and it's better than what you asked for", "ALTERNATIVE. → Step 3."),
        ("Step3 Close", "just trust me on this, you'll thank me after", "CLOSE."),
    ], "res"),

    # ── DONE ──
    "done1": ([
        ("Step1 Validate", "fuck that's hot, you came because of me??", "VALIDATE. → Step 2."),
        ("Step2 Rescue", "but I haven't finished yet, you're really gonna leave me like this?", "RESCUE. Still no → Step 3."),
        ("Step3 Seed", "next time you have to wait for me, I have something insane planned for round 2", "SEED."),
    ], "res"),
    "done2": ([
        ("Step1 Validate", "already?? damn that's hot", "VALIDATE. → Step 2."),
        ("Step2 Rescue", "wait I'm not done yet, you're just gonna leave me hanging?", "RESCUE. Still no → Step 3."),
        ("Step3 Seed", "next time you hold it because what I have planned is way crazier", "SEED."),
    ], "res"),

    # ── SITUATIONAL ──
    "cumcontrol": ([
        ("edge1", "don't cum yet, I'm not done with you", "CONTROL."),
        ("edge2", "hold it, not yet, I need you to last longer for me", "EDGE variant."),
        ("sync1", "I'm close too, cum with me, but you need to see this first", "SYNC. Send PPV."),
        ("sync2", "wait for me, I want us to finish together, open this first", "SYNC variant."),
        ("delay1", "hold it, wait until you see what I'm about to send, trust me it's worth it", "DELAY. Send PPV."),
        ("delay2", "don't you dare finish before you see this", "DELAY variant."),
    ], "sit"),
    "dickpic": ([
        ("dpsext1", "fuck okay that's... wow, you have no idea what that just did to me", "DURING SEXTING."),
        ("dpsext2", "damn that is... I need to show you something rn", "DURING SEXTING variant."),
        ("dprapport1", "omg you don't waste time huh, that's actually really hot ngl", "DURING RAPPORT."),
        ("dprapport2", "woah wasn't expecting that but... damn", "DURING RAPPORT variant."),
        ("dpppv1", "you can't send me that and expect me to do nothing about it, hold on", "LEVERAGE. WAIT 1-2 min then send PPV."),
        ("dpppv2", "okay you just made me do something, give me a sec", "LEVERAGE variant."),
    ], "sit"),
    "boosters": ([
        ("h1", "fuckkk", "MID-SEXTING BOOSTER."),
        ("h2", "I'm so hard rn because of you", "BOOSTER. Ego."),
        ("h3", "don't stop", "BOOSTER. Micro."),
        ("h4", "you have no idea what you're doing to me", "BOOSTER."),
        ("h5", "I can't think straight rn", "BOOSTER."),
        ("h6", "my hands are shaking", "BOOSTER. Physical."),
        ("h7", "more", "BOOSTER. Ultra micro."),
        ("h8", "I can't focus on anything else rn", "BOOSTER."),
    ], "sit"),
}


# ═══════════════════════════════════════════════════════════════
# MALE CREATORS (gay audience) — DEFAULT OBJ SCRIPTS (7/10 tone)
# ═══════════════════════════════════════════════════════════════

# Gay male = same as straight male but with bro/dude language tweaks
DEFAULT_OBJ_MALE_GAY = {**DEFAULT_OBJ_MALE}

# Override only the scripts that need gendered language changes
DEFAULT_OBJ_MALE_GAY["boosters"] = ([
    ("h1", "fuckkk", "MID-SEXTING BOOSTER."),
    ("h2", "I'm so hard rn because of you", "BOOSTER. Ego."),
    ("h3", "don't stop", "BOOSTER. Micro."),
    ("h4", "you have no idea what you're doing to me bro", "BOOSTER."),
    ("h5", "I can't think straight rn", "BOOSTER."),
    ("h6", "my hands are shaking", "BOOSTER. Physical."),
    ("h7", "more", "BOOSTER. Ultra micro."),
    ("h8", "I can't focus on anything rn", "BOOSTER."),
], "sit")

DEFAULT_OBJ_MALE_GAY["discount1"] = ([
    ("Step1 Firmness", "haha negotiate? bro this isn't a sale, you know what you're getting", "FIRMNESS. Still → Step 2."),
    ("Step2 Challenge", "the guys who get my best stuff don't ask for discounts, they know what it's worth", "CHALLENGE. Still → Step 3."),
    ("Step3 Concession", "fine [lower price] ONLY because I like you, but don't ever ask me this again", "CONCESSION. ONE TIME. Still no → Step 4."),
    ("Step4 Takeaway", "okay I'll keep it then, someone else has been asking and they won't hesitate", "TAKEAWAY."),
], "obj")

DEFAULT_OBJ_MALE_GAY["discount2"] = ([
    ("Step1 Firmness", "a discount? do I look like I'm on sale? you know what you're getting", "FIRMNESS. Still → Step 2."),
    ("Step2 Challenge", "the ones who really want it don't ask for discounts", "CHALLENGE. Still → Step 3."),
    ("Step3 Concession", "[lower price] because this convo has been different, first and last time", "CONCESSION. ONE TIME. Still no → Step 4."),
    ("Step4 Takeaway", "no problem, I'll save it for someone who really wants it", "TAKEAWAY."),
], "obj")

DEFAULT_OBJ_MALE_GAY["nosex1"] = ([
    ("Step1 Respect", "haha okay I got carried away, you're too easy to talk to", "RESPECT. Still → Step 2."),
    ("Step2 Subtle", "so tell me more about you, what do you do when you're not driving guys on the internet crazy?", "SUBTLE. → Step 3 later."),
    ("Step3 ReAttempt", "I can't help it though, there's something about you that keeps messing with my head", "RE-ATTEMPT. Still no → Step 4."),
    ("Step4 Accept", "alright I'll behave, for now, no promises", "ACCEPT. Door open."),
], "res")

DEFAULT_OBJ_MALE_GAY["nosex2"] = ([
    ("Step1 Respect", "my bad I got ahead of myself, your fault for being this fun", "RESPECT. Still → Step 2."),
    ("Step2 Subtle", "okay new topic, what's the craziest thing you've ever done?", "SUBTLE. → Step 3 later."),
    ("Step3 ReAttempt", "I'm trying so hard to behave but you make it impossible honestly", "RE-ATTEMPT. Still no → Step 4."),
    ("Step4 Accept", "fine I'll stop, don't blame me when it happens again though", "ACCEPT."),
], "res")

# Done entries for gay audience — same structure, "bro" language
DEFAULT_OBJ_MALE_GAY["done1"] = ([
    ("Step1 Validate", "fuck that's hot, you came because of me??", "VALIDATE. → Step 2."),
    ("Step2 Rescue", "but I haven't finished yet bro, you're really gonna leave me like this?", "RESCUE. Still no → Step 3."),
    ("Step3 Seed", "next time you have to wait for me, I have something insane planned for round 2", "SEED."),
], "res")

DEFAULT_OBJ_MALE_GAY["done2"] = ([
    ("Step1 Validate", "already?? damn that's hot", "VALIDATE. → Step 2."),
    ("Step2 Rescue", "wait I'm not done yet, you're just gonna leave me hanging?", "RESCUE. Still no → Step 3."),
    ("Step3 Seed", "next time you hold it because what I have planned is way crazier", "SEED."),
], "res")
