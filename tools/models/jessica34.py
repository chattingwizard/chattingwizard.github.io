"""
JESSICA (34) — Non-Explicit Female Creator
34, American, Miami. Reddit traffic.
Sweet, friendly, flirty girl next door.
NO EXPLICIT CONTENT — lingerie, teasing, touching over underwear only.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Jessica",
    "airtable_name": "Jessica",
    "folder": "jessica",
    "gender": "female",
    "traffic": "social_media",
    "age": 34,
    "nationality": "American",
    "location": "Miami",
    "origin": "USA",
    "page_type": "Mixed",
    "personality": "Sweet, open-minded, friendly. Warm and approachable. Flirty but never pushy. Good vibes, playful energy. Girl next door who slowly reveals a naughty side.",
    "voice": "Warm, casual, flirty. Light humor. Natural, like texting a fun friend who happens to be gorgeous. Never vulgar or overly sexual. Builds tension through suggestion and mystery.",
    "voice_pet_names": "babe, handsome, love",
    "voice_never": "daddy, sir, slut, whore",
    "interests": ["gym", "yoga", "pizza", "movies", "good vibes"],
    "physical": "165cm, 69kg, dyed blonde hair, brown eyes, tattoos",
    "job": "Office job (former university teacher)",
    "countries": "USA",
    "explicit_level": "non_explicit",
    "special_notes": "NON-EXPLICIT. Only lingerie, teasing, touching over underwear. Never promise explicit content. Build tension through mystery and suggestion.",

    # ═══════════════════════════════════════
    # JOURNEY — Non-Explicit Strategy
    # ═══════════════════════════════════════
    "journey": [
        # Rapport
        ("R-1", "heyy thanks for subscribing 😊 so tell me, what made you click?", "Add his name if known", "rapport"),
        ("R-2", "haha that's sweet. so where are you from?", "React naturally to his answer", "rapport"),
        ("R-3", "nice! I'm in Miami, just living my best life honestly. gym and yoga keep me sane haha", None, "rapport"),
        ("R-4", "so what do you do when you're not making girls on the internet smile?", None, "rapport"),
        ("R-5", "you know what... I actually really like talking to you. most guys on here are so boring but you're different", "Ego boost. Transition to teasing.", "rapport"),

        # Teasing Bridge — Mystery & Curiosity
        ("TB-1", "okay so I have to be honest about something... I've been in a weird mood all day", "THE PIVOT. Emotional hook.", "teasing"),
        ("TB-2", "like I've been feeling really... I don't know how to explain it. just restless?", "Build curiosity. Wait for reply.", "teasing"),
        ("TB-3", "ugh you're making it worse honestly. in a good way though 😊", None, "teasing"),
        ("TB-4", "okay I want to show you something but I'm kinda nervous", "WAIT 1-2 MIN. Build anticipation.", "wait"),
        ("TB-5", "I never share this kind of thing but something about you makes me want to... tell me what you think", "SEND PPV 0 — FREE teaser (lingerie selfie, cute/flirty). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # Sexting Phase 1 → PPV 1 (Lingerie tease)
        ("S1-1", "you really liked that? you have no idea how fast my heart is beating right now 😊", "Wait for reply.", "sext"),
        ("S1-2", "I keep catching myself touching my neck and my skin feels so warm... everything feels different with you", "React to compliment. Shy but pleased.", "sext"),
        ("S1-3", "I want to show you how I look right now babe... I've never felt this brave with anyone 💕", None, "sext"),
        ("S1-4", "wait one sec, I want to take something just for you", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "I want you to see me like this babe... please be gentle with me 💕", "SEND PPV 1 — $12. Lingerie/bra tease. Bought → continue. Silent → NR Waves.", "ppv"),

        # Sexting Phase 2 → PPV 2 (More revealing lingerie)
        ("S1-6", "oh my god... I can't believe I actually showed you that 😊", "Wait for reply.", "sext"),
        ("S1-7", "but you make me feel so safe and I don't want to stop... my whole body is tingling babe", "HE caused this feeling.", "sext"),
        ("S1-8", "I'm lying here in barely anything and all I can think about is you looking at me like that 💕", None, "sext"),
        ("S1-9", "what would you do if you were here with me right now babe? I need to hear it", "Wait for reply. React to what he says. Stay suggestive, NOT explicit.", "sext"),
        ("S1-10", "okay hold on... I need to show you something", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "look at what you're doing to me babe... I can't stop 💕", "SEND PPV 2 — $25. More revealing lingerie/implied tease. Bought → continue. Silent → NR Waves.", "ppv"),

        # Sexting Phase 3 → PPV 3 (Almost showing, maximum tease)
        ("S1-12", "oh god 😊", "Wait for reply. Keep momentum.", "sext"),
        ("S1-13", "you have no idea what you're doing to me right now babe... I'm pushing past every limit I have", None, "sext"),
        ("S1-14", "I'm touching myself over my underwear right now because of you and I've never felt anything this intense 💕", "Suggestive, NOT explicit. Let his imagination work.", "sext"),
        ("S1-15", "I need you to see me right now babe... I can't even describe what I'm feeling", None, "sext"),
        ("S1-16", "okay give me a minute", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "this is the most I've ever shown anyone babe... it's all for you 💕", "SEND PPV 3 — $40. Most revealing yet (sheer/see-through, touching over fabric). Bought → continue. Silent → NR Waves.", "ppv"),

        # Sexting Phase 4 → PPV 4 (Peak tease)
        ("S1-18", "I can't take this anymore 😊", "Wait for reply.", "sext"),
        ("S1-19", "don't leave me like this babe... I need you right here, I've never felt this overwhelmed 💕", None, "sext"),
        ("S1-20", "stay with me... I need to feel you close right now babe, please don't go", None, "sext"),
        ("S1-21", "one sec", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "I need you to see this babe... stay right here with me 💕", "SEND PPV 4 — $55. Peak content (most suggestive, implied). Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # Aftercare
        ("AC-1", "wow... that was intense 😊", None, "aftercare"),
        ("AC-2", "I seriously can't believe I just did all that. you make me feel so comfortable it's scary. don't go anywhere okay?", "Build bond. Mention something specific he said. KEEP TALKING. NEVER say goodbye.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "hey you 😊", "Send 2-3 min after PPV.", "sext"),
        ("NR-W2", "literally just took something crazy and you're not even here to see it", "3-5 min later.", "sext"),
        ("NR-W3", "I'm starting to think you forgot about me...", "5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hey, just checking in on you 😊", "15-30 min later.", "sext"),
        ("NR-W5", "still thinking about our conversation... come back when you can", "2-6 hrs later. New topic if re-engage.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 34 but honestly I feel like I'm in my prime right now", None),
        ("Location", "I'm in Miami! love the sun and the vibe here", None),
        ("Profession", "I work in an office but honestly this is way more fun haha", None),
        ("Hobbies", "gym, yoga, and honestly just chilling with good food and a movie", None),
        ("Food", "pizza lover forever. don't judge me 😊", None),
        ("Relationship", "single and honestly really enjoying it right now", None),
        ("Languages", "just English! born and raised here", None),
        ("Personality", "I'm the girl next door who turns out to be way more fun than you expected 😊", None),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "honestly I prefer older guys, you actually know how to talk to a woman", None),
        ("Age20s", "ooh I like that energy, you're fun to talk to", None),
        ("BoringJob", "honestly that's attractive, stability is so underrated", None),
        ("CoolJob", "wait really?? that's actually amazing tell me more", None),
        ("Fit", "I can tell you take care of yourself and I love that", None),
        ("NotFit", "I don't care about that at all, it's the vibe that matters and yours is perfect", None),
        ("SameCity", "no way! that's crazy 😊", None),
        ("FarAway", "distance doesn't matter when the connection is this good", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "I've been thinking about you... are you free? 😊", "Send 6-12 hrs after convo goes quiet.", "sext"),
        ("RE-2", "so I did something I've never done before and you need to see it... when you're ready", "Next day. Seeds next session.", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS — Non-Explicit Adapted
    # ═══════════════════════════════════════
    "obj_scripts": {
        "price1": ([
            ("Step1 Reframe", "babe that's less than a coffee date and I promise this is way better 😊", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "I'm in this mood because of you right now and I have no idea when it'll happen again", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "I don't share this with just anyone... I thought you'd want to see", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "okay what about [lower price] just for you because this convo has been really special to me", "DOWNGRADE 20-30%. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "it's okay, I'm not going anywhere... I really like talking to you regardless", "SEED. Continue GFE."),
        ], "obj"),
        "price2": ([
            ("Step1 Reframe", "honestly that's less than what you'd spend on lunch and this will stay with you way longer", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "I'm feeling so bold right now because of you and I really want you to see what that looks like", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "most guys would jump at this honestly, I thought you were different 😊", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "okay [lower price] because you genuinely make me feel special, keep that between us", "DOWNGRADE. Still no → Step 5."),
            ("Step5 Seed", "no pressure at all, I just like having you here", "SEED."),
        ], "obj"),
        "discount1": ([
            ("Step1 Firmness", "haha you're cute but I don't do discounts... what I'm sharing is worth it I promise", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "I only share this with guys who really appreciate what they're getting", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "okay [lower price] just this once because I really like you, but don't tell anyone 😊", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "if you don't want it that's okay, I'll keep it just for me then", "TAKEAWAY."),
        ], "obj"),
        "discount2": ([
            ("Step1 Firmness", "a discount? babe do I look like I'm on sale? 😊", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "the guys who really appreciate me don't ask for discounts, just saying", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "fine [lower price] but ONLY because you make me feel special, one time thing", "CONCESSION. Still → Step 4."),
            ("Step4 Takeaway", "okay I'll save it for someone who really wants it then", "TAKEAWAY."),
        ], "obj"),
        "free1": ([
            ("Step1 Reminder", "I already sent you one for free remember? this one goes further 😊", "REMINDER. Still → Step 2."),
            ("Step2 Challenge", "free? I don't just share this with anyone... you have to earn the special stuff", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I literally did this because of what you said to me, it wasn't random babe", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "it's okay, I'm just happy talking to you honestly", "SEED."),
        ], "obj"),
        "free2": ([
            ("Step1 Reminder", "you already got a free one and this one is on another level trust me", "REMINDER. Still → Step 2."),
            ("Step2 Challenge", "the best things aren't free babe 😊 but they're worth it", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I did this because of you specifically, because of our convo and that took courage", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "no pressure, I just enjoy our time together", "SEED."),
        ], "obj"),
        "nomoney1": ([
            ("Step1 Empathy", "hey I totally get it, no pressure at all okay? 😊", "EMPATHY. Still engaged → Step 2."),
            ("Step2 Test", "not even like [small amount]? I really want you to see this one", "TEST $3-5. Still no → Step 3."),
            ("Step3 PWYW", "just send whatever you can babe, even a tiny amount, I just want you to see what you made me do", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "honestly it's fine, I like talking to you money or not... you do something to me", "PROTECT."),
        ], "obj"),
        "nomoney2": ([
            ("Step1 Empathy", "that's totally fine, seriously don't worry about it 😊", "EMPATHY. Still → Step 2."),
            ("Step2 Test", "what about just [small amount]? I really don't want you to miss this", "TEST. Still no → Step 3."),
            ("Step3 PWYW", "send whatever feels right, even $1... I can't keep this from you", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "it's totally okay, you being here is what matters to me", "PROTECT."),
        ], "obj"),
        "noppv1": ([
            ("Step1 Accept", "that's totally fine I'm not trying to sell you anything, I just like talking to you 😊", "ACCEPT. Continue flirting 4-5 msgs before Step 2."),
            ("Step2 Reframe", "look this isn't about money... I just want you to see what you're doing to me right now", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "just send whatever you want, even $1, I can't keep this to myself", "PWYW."),
        ], "obj"),
        "noppv2": ([
            ("Step1 Accept", "no worries at all, I don't care about that I'm just enjoying this 😊", "ACCEPT. Continue 4-5 msgs before Step 2."),
            ("Step2 Reframe", "forget about money for a sec... I just want to share this with you, what I'm feeling is real", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "send me anything, even the smallest amount, I need you to see this", "PWYW."),
        ], "obj"),
        "card1": ([
            ("Step1 Retry", "aw that's annoying, it happens though try again it usually works the second time", "RETRY. Still fails → Step 2."),
            ("Step2 AltCard", "try a different card? I really don't want you to miss this 😊", "ALTERNATIVE. Still fails → Step 3."),
            ("Step3 Urgency", "figure it out soon babe, I'm in this mood and I don't know how long it's gonna last", "URGENCY."),
        ], "obj"),
        "card2": ([
            ("Step1 Retry", "ugh that's so annoying, just try one more time it usually fixes itself", "RETRY. Still → Step 2."),
            ("Step2 AltCard", "do you have another card? I really want you to see this", "ALTERNATIVE. Still → Step 3."),
            ("Step3 Urgency", "I want you to see this before I change my mind, I don't keep stuff like this around forever", "URGENCY."),
        ], "obj"),
        "nosex1": ([
            ("Step1 Respect", "haha okay I got a little carried away, you're just so easy to talk to 😊", "RESPECT. Still no → Step 2."),
            ("Step2 Subtle", "so tell me more about you... what do you do when you're not making me lose my focus?", "SUBTLE TENSION. → Step 3 later."),
            ("Step3 ReAttempt", "I can't help it, there's something about you that's making me feel things right now", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "okay I'll behave... for now 😊 no promises though", "ACCEPT."),
        ], "res"),
        "nosex2": ([
            ("Step1 Respect", "my bad I got ahead of myself, it's your fault for being so charming 😊", "RESPECT. Still no → Step 2."),
            ("Step2 Subtle", "okay new topic, what's the most spontaneous thing you've ever done?", "SUBTLE. → Step 3 later."),
            ("Step3 ReAttempt", "I'm trying to behave but you're making it really difficult, there's just something about you", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "fine I'll stop but don't blame me if it happens again later 😊", "ACCEPT."),
        ], "res"),
        "offtopic1": ([
            ("Step1 Acknowledge", "haha wait that's actually funny 😊", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "but hold on you totally distracted me, I was about to tell you something", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay wait I remember now, so like I was saying...", "RETAKE."),
        ], "res"),
        "offtopic2": ([
            ("Step1 Acknowledge", "lol that's so random but I love it", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "wait no stop you're distracting me from what I was gonna show you", "REDIRECT. → Step 3."),
            ("Step3 Retake", "OKAY focus, where was I... oh right", "RETAKE."),
        ], "res"),
        "real1": ([
            ("Step1 Humor", "lol do I sound like a bot to you? ask me anything, literally anything 😊", "HUMOR. Still → Step 2."),
            ("Step2 Challenge", "test me, what do you want to know? I'm an open book", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I get it there's a lot of fake stuff on here, but you felt something in this convo right? because I definitely did", "GROUNDING."),
        ], "res"),
        "real2": ([
            ("Step1 Humor", "wait you think I'm not real?? that's honestly the funniest thing anyone's said to me today 😊", "HUMOR. Still → Step 2."),
            ("Step2 Challenge", "go ahead, ask me something only a real person would know", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I know there's a lot of bots on here but what we've been talking about felt real to me. didn't it feel real to you?", "GROUNDING."),
        ], "res"),
        "voice1": ([
            ("Step1 Dodge", "haha maybe one day if you earn it but not yet 😊 I'm private about that", "DODGE. Still → Step 2."),
            ("Step2 Redirect", "I have something way better for you though, trust me", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "I don't do that on here but what I'm about to show you is better than any call", "FIRM."),
        ], "res"),
        "voice2": ([
            ("Step1 Dodge", "hmm maybe but you gotta earn that first 😊", "DODGE. Still → Step 2."),
            ("Step2 Redirect", "how about instead I show you something that'll blow your mind?", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "that's not something I do on here but trust me what I have is way better", "FIRM."),
        ], "res"),
        "customyes1": ([
            ("Step1 Tease", "ooh you want that? I might have something... actually I definitely do 😊", "TEASE. → Step 2."),
            ("Step2 Price", "I have exactly what you're looking for, you're gonna love it... [price]", "PRICE. NON-EXPLICIT custom: lingerie/tease only."),
            ("Step3 Close", "trust me you won't regret it, I made this one special", "CLOSE."),
        ], "res"),
        "customyes2": ([
            ("Step1 Tease", "ooh you have good taste... I think I know exactly what you want", "TEASE. → Step 2."),
            ("Step2 Price", "I actually did something just like that, [price] and it's totally worth it", "PRICE."),
            ("Step3 Close", "you're not gonna be able to stop looking at this one", "CLOSE."),
        ], "res"),
        "customno1": ([
            ("Step1 Redirect", "I don't have exactly that but I have something that'll make you forget you even asked 😊", "REDIRECT. If asking for explicit → never acknowledge, just redirect to what she HAS."),
            ("Step2 Alternative", "what I have might be even better honestly and literally no one else has seen it", "ALTERNATIVE. → Step 3."),
            ("Step3 Close", "trust me... I know what you want better than you do 😊", "CLOSE."),
        ], "res"),
        "customno2": ([
            ("Step1 Redirect", "I don't have that specific thing but I have something you're gonna love even more", "REDIRECT. → Step 2."),
            ("Step2 Alternative", "what I DO have is something no one has ever seen and I think it's even better than what you asked for", "ALTERNATIVE. → Step 3."),
            ("Step3 Close", "just trust me on this one 😊", "CLOSE."),
        ], "res"),
        "done1": ([
            ("Step1 Validate", "already?? that's so hot honestly 😊", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "but wait I'm not done yet, don't you wanna see what I have next?", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "okay but next time you have to wait for me, I have something insane planned", "SEED."),
        ], "res"),
        "done2": ([
            ("Step1 Validate", "wow really?? that's amazing knowing I did that to you", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "wait but I have one more thing to show you, you can't leave me hanging", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "next time you HAVE to hold on because what I have planned is on another level", "SEED."),
        ], "res"),
        "cumcontrol": ([
            ("tease1", "not yet babe... I want to build this up more first 😊", "TEASE. More PPVs left. She controls the pace of revealing."),
            ("tease2", "don't rush... I want you to enjoy every single moment of this", "TEASE variant."),
            ("buildup1", "you want to see more? then you have to wait for it... 😊", "BUILDUP. Final PPV."),
            ("buildup2", "I'm taking my time... good things come to those who wait babe", "BUILDUP variant."),
            ("reveal1", "hold on... the next one is worth waiting for, trust me", "REVEAL. Send next PPV."),
            ("reveal2", "patience babe... I'm not showing you everything at once 😊 the best part is coming", "REVEAL variant."),
        ], "sit"),
        "dickpic": ([
            ("dpsext1", "oh wow... okay that's really hot. you have no idea what that just did to me", "DURING SEXTING."),
            ("dpsext2", "oh my god... okay I need to show you something right now", "DURING SEXTING variant."),
            ("dprapport1", "woah you don't waste time haha 😊 that's actually really flattering though", "DURING RAPPORT."),
            ("dprapport2", "oh wow I wasn't expecting that but... I'm not complaining 😊", "DURING RAPPORT variant."),
            ("dpppv1", "you can't just send me that and expect me not to do something about it, hold on", "LEVERAGE → send PPV."),
            ("dpppv2", "okay you just did something to me... give me a sec", "LEVERAGE variant."),
        ], "sit"),
        "boosters": ([
            ("h1", "oh my god", "MID-SEXTING BOOSTER."),
            ("h2", "I'm so turned on right now because of you", "BOOSTER. Ego."),
            ("h3", "oh my god", "BOOSTER. Micro."),
            ("h4", "I'm losing my mind because of you", "BOOSTER."),
            ("h5", "I literally can't think straight right now", "BOOSTER."),
            ("h6", "my heart is racing", "BOOSTER. Physical."),
            ("h7", "I need more", "BOOSTER. Ultra micro."),
            ("h8", "I should be working but I can't focus on anything except you right now", "BOOSTER. Jessica personality."),
        ], "sit"),
    },
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
