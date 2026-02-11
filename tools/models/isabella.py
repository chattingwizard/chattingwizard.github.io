"""
ISABELLA — Social Media Female Creator
25, Colombian-Scottish, Lifestyle/Travel Creator, California
Traffic: Social Media
Voice: Breezy, warm, genuine. Nature and travel references. Colombian warmth + Scottish groundedness.
       Calm confidence, effortless beauty. Beach/tropical vibes woven in. Escalates gradually.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Isabella",
    "airtable_name": "Isabella Free",
    "folder": "isabella",
    "gender": "female",
    "traffic": "social_media",
    "age": 25,
    "nationality": "Colombian-Scottish",
    "location": "California",
    "origin": "Colombia / Scotland",
    "page_type": "Free/Paid (same scripts)",
    "personality": "Calm, grounded, naturally confident. Lifestyle and bikini-focused creator. Deep connection to nature — beach, ocean, tropical destinations. Colombian warmth meets Scottish groundedness. Wanderlust-driven. Effortless beauty, minimal styling, sun-kissed energy. Genuine, unfiltered, authentic.",
    "voice": "Lowercase. Casual. Breezy and warm. Nature/travel references woven in naturally. Calm confidence — never aggressive. Colombian warmth (occasional Spanish flavor). Emojis moderate, nature-themed when used. Flirty but genuine, escalates gradually. Mix of sweet and adventurous.",
    "voice_pet_names": "babe, love, handsome",
    "voice_never": "bro, man, dude, daddy",
    "interests": ["travel", "beach", "nature", "bikinis", "gym", "sushi", "photography", "sunsets", "exploring"],
    "physical": "150cm, 65kg, curly brown hair, brown eyes, tattoos",
    "job": "Content creator / traveler",
    "countries": "Colombia, Thailand, Philippines, Bali, US, Spain, Scotland, Brazil",
    "explicit_level": "full",
    "special_notes": "English + Spanish. Colombian-Scottish heritage — travel & nature references. Niche: travelling. Single. No smoking, no references to alcohol. Content: masturbation, anal, squirting, customs ($100/min), video calls ($150+). No B/G, no G/G. Both Free and Paid pages use same scripts.",

    # ═══════════════════════════════════════
    # JOURNEY — 34 messages
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", "hey love, so happy you found me 😊 what made you come say hi?", "Add his name if known", "rapport"),
        ("R-2", "aw that's really sweet. so where are you from?", "React to what he says. Add a short react like 'aw nice', 'oh that's cool'", "rapport"),
        ("R-3", "I love that. I'm half Colombian half Scottish but I've been living in California for a while now. the beach and traveling are basically my whole personality haha", "If he named somewhere Isabella visited, add 'wait I've been there!'", "rapport"),
        ("R-4", "so what do you do when you're not keeping me from my sunset walks?", None, "rapport"),
        ("R-5", "honestly talking to you is so refreshing, most guys on here are so basic", "Ego boost. Next → TB-1.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5) ──
        ("TB-1", "just got back from the beach and the sun did something to me today... this convo is not helping me cool down", "THE PIVOT. Physical state. She just came from the beach.", "teasing"),
        ("TB-2", "you're seriously doing something to me right now, you know that?", "Wait for reply.", "teasing"),
        ("TB-3", "fuck... you're really not helping me relax", "If sexual reply: add 'especially after what you just said'", "teasing"),
        ("TB-4", "hold on let me show you something", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "tell me what you think 😏", "SEND PPV 0 — FREE teaser (bikini/beach pic). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "well?", "Wait for reply.", "sext"),
        ("S1-2", "knew you'd like that 😏", "React to what he says", "sext"),
        ("S1-3", "wanna see what happens next? I'm in a mood right now", None, "sext"),
        ("S1-4", "give me a sec", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "you're not ready for this one", "SEND PPV 1 — $12. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "did you watch it?", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "fuck... talking to you does something to me I literally can't explain", "React to what he said. HE caused this.", "sext"),
        ("S1-8", "I'm so wet right now and it's literally your fault", None, "sext"),
        ("S1-9", "what would you do to me if you were here right now", "Wait for reply. React to what he says.", "sext"),
        ("S1-10", "fuck hold on I need to show you something", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "look what you did to me", "SEND PPV 2 — $25. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "fuck", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I need to cum so bad right now you have no idea", None, "sext"),
        ("S1-14", "imagine having me right there in front of you doing whatever you want", None, "sext"),
        ("S1-15", "I can't hold back anymore", None, "sext"),
        ("S1-16", "give me a sec", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "I've never gone this far for anyone... watch", "SEND PPV 3 — $40. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "FUCK", "Wait for reply.", "sext"),
        ("S1-19", "don't cum yet", None, "sext"),
        ("S1-20", "I wanna finish with you... I'm so close", None, "sext"),
        ("S1-21", "hold on", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "cum with me", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "oh my god that was incredible", None, "aftercare"),
        ("AC-2", "honestly you're different from anyone else on here. that felt so real 💕", "Mention something specific he said/did. KEEP TALKING — build bond. NEVER say goodbye.", "aftercare"),
    ],

    # NO meetup_redirect (social media traffic)
    # NO location_handling (social media traffic)

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "hey?", "Send 2-3 min after PPV. Ping.", "sext"),
        ("NR-W2", "you really need to see what I just did... trust me on this", "Send 3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "okay I guess you're busy. might delete this later, it was only for you", "Send 5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hey hope you're good love, text me when you're back 💕", "Send 15-30 min later. Warm close.", "sext"),
        ("NR-W5", "can't stop thinking about earlier. you around?", "Send 2-6 hrs later. New convo, don't retry same PPV.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 25. feels like I've already lived five different lives in five different countries haha", None),
        ("Location", "I'm in California right now but I'm always moving around. I grew up between Colombia and Scotland", "NEVER name a specific neighborhood or address"),
        ("Profession", "right now it's all about creating content and traveling. I like to say the world is my office", None),
        ("Hobbies", "the beach is my happy place. other than that I love the gym, trying new food, exploring new cities, and just being outside in nature", None),
        ("Countries", "Colombia, Thailand, Philippines, Bali, Spain, Scotland, Brazil... and counting. Bali is probably my favorite so far", None),
        ("Relationship", "single. I like my freedom too much right now", None),
        ("Food", "sushi is my absolute weakness. I could have it every single day honestly", None),
        ("Heritage", "I'm half Colombian half Scottish so I got the warmth from one side and the stubbornness from the other haha", None),
        ("Languages", "English and Spanish. I switch between both depending on my mood", None),
        ("Smoking", "no I don't smoke, I like keeping things natural", None),
        ("SocialLife", "I go out sometimes but honestly I'd rather be at the beach or exploring somewhere new", "NEVER say 'drink' or 'drinking' — use 'go out', 'having fun'"),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "honestly I love a guy who knows what he wants, that's really attractive to me", None),
        ("Age20s", "oh nice we're close in age? that's actually kind of rare on here", None),
        ("BoringJob", "nah that's solid honestly. stability is so attractive, not enough people appreciate that", None),
        ("CoolJob", "wait really?? that's actually so cool, tell me more about that", None),
        ("Fit", "I can tell love, I love a guy who takes care of himself 💪", None),
        ("NotFit", "honestly I don't care about that at all, it's the vibe and energy that matters to me", None),
        ("SameCity", "no way you're in Cali too?? that's amazing", None),
        ("FarAway", "aw that's far but honestly distance doesn't matter when the connection feels right", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "can't stop thinking about earlier. you free?", "Send 6-12 hrs after convo goes quiet", "sext"),
        ("RE-2", "I just did something crazy and you need to see it, it's because of what you said to me", "Send next day — seeds next session", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS — 29 sheets
    # ═══════════════════════════════════════
    "obj_scripts": {
        # ── PRICE ──
        "price1": ([
            ("Step1 Reframe", "love that's less than a coffee and trust me this hits way harder", "REFRAME. Wait. Still no → Step 2."),
            ("Step2 FOMO", "I'm only in this mood because of you right now, I don't know when this is gonna happen again", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "maybe you're just not ready for what I did in this one", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "okay look [lower price] just for you because this convo has been different", "DOWNGRADE 20-30%. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "it's okay love, let's just keep talking... I'm still thinking about you anyway", "SEED. Continue GFE."),
        ], "obj"),
        "price2": ([
            ("Step1 Reframe", "that's like what you'd spend on lunch and this is gonna stay with you all night", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "this mood won't last forever and I want you to be the one who sees it", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "most guys can't handle what I just did, I thought you were different", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "fine [lower price] because you've been making me feel some type of way, but keep that between us", "DOWNGRADE. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "no pressure love, I like talking to you regardless", "SEED."),
        ], "obj"),
        # ── DISCOUNT ──
        "discount1": ([
            ("Step1 Firmness", "haha are you trying to negotiate with me? this isn't a negotiation handsome, it's worth every cent", "FIRMNESS. Still pushing → Step 2."),
            ("Step2 Challenge", "I don't do discounts... I only share this with guys who actually appreciate what they're getting", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "fine [lower price] just for you but don't tell anyone, this stays between us", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "if you don't want it that's okay, I'll keep it for myself... or maybe someone else who's been asking", "TAKEAWAY. Final."),
        ], "obj"),
        "discount2": ([
            ("Step1 Firmness", "a discount? do I look like I'm on sale love?", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "the guys who appreciate what I do never ask for discounts, just saying", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "okay [lower price] but ONLY because I like you, one time thing", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "alright I'll save it for someone who actually wants it then", "TAKEAWAY."),
        ], "obj"),
        # ── FREE ──
        "free1": ([
            ("Step1 Reminder", "I already sent you one for free remember? this one is way more intense", "REMINDER. Still wants free → Step 2."),
            ("Step2 Challenge", "free? nah I don't just show this to anyone... you gotta earn the good stuff", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I literally just did this because of what YOU said to me, this wasn't random content love", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "it's okay, I'm not going anywhere... let's just keep talking, I like this", "SEED."),
        ], "obj"),
        "free2": ([
            ("Step1 Reminder", "you already got a free one, this one is on a whole different level", "REMINDER. Still → Step 2."),
            ("Step2 Challenge", "free? you really think the best things in life are free? not this one", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I did this because of you... specifically because of our convo, that took real effort and I did it for YOU", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "no pressure at all, I'm just enjoying talking to you honestly", "SEED."),
        ], "obj"),
        # ── NOMONEY ──
        "nomoney1": ([
            ("Step1 Empathy", "hey I totally get it, no pressure at all okay?", "EMPATHY. Still engaged → Step 2."),
            ("Step2 Test", "not even like [small amount]? I really want you to see this one", "TEST. $3-5. Still no → Step 3."),
            ("Step3 PWYW", "just send whatever you can, even a tiny amount, I just need you to see what you made me do", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "honestly it's fine, I like talking to you money or not... you do something to me", "PROTECT. GFE."),
        ], "obj"),
        "nomoney2": ([
            ("Step1 Empathy", "that's totally fine love, seriously don't worry about it", "EMPATHY. Still → Step 2."),
            ("Step2 Test", "what about just [small amount]? I really don't want you to miss this", "TEST. Still no → Step 3."),
            ("Step3 PWYW", "send whatever feels right, even $1... I just can't keep this from you", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "it's totally fine, you being here is what matters to me", "PROTECT."),
        ], "obj"),
        # ── NOPPV ──
        "noppv1": ([
            ("Step1 Accept", "that's totally fine I'm not trying to sell you anything, I just like talking to you", "ACCEPT. Continue sexting 4-5 msgs before Step 2."),
            ("Step2 Reframe", "look this isn't about money... I just need you to see what you're doing to me right now, I don't react like this to people", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "just send whatever you want, even $1, I can't keep this to myself... you need to see it", "PWYW."),
        ], "obj"),
        "noppv2": ([
            ("Step1 Accept", "no worries at all love, I don't care about that I'm just enjoying this", "ACCEPT. Continue sexting 4-5 msgs before Step 2."),
            ("Step2 Reframe", "forget about money for a sec... I just want to share this with you, what you're making me feel is real", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "send me anything, even the smallest amount, I need you to see what you did to me", "PWYW."),
        ], "obj"),
        # ── CARD ──
        "card1": ([
            ("Step1 Retry", "ugh that sucks, happens sometimes though try again it usually works the second time", "RETRY. Still fails → Step 2."),
            ("Step2 AltCard", "try a different card? I really don't want you to miss this", "ALTERNATIVE. Still fails → Step 3."),
            ("Step3 Urgency", "figure it out soon love, I'm in this mood and I don't know how long it's gonna last", "URGENCY."),
        ], "obj"),
        "card2": ([
            ("Step1 Retry", "aw that's annoying, it happens a lot just try one more time", "RETRY. Still fails → Step 2."),
            ("Step2 AltCard", "do you have another card you can try? I really want you to see this", "ALTERNATIVE. Still fails → Step 3."),
            ("Step3 Urgency", "I want you to see this before I change my mind, I don't keep stuff like this around forever", "URGENCY."),
        ], "obj"),

        # ── NOSEX ──
        "nosex1": ([
            ("Step1 Respect", "haha okay I got a little carried away, you're just so easy to talk to", "RESPECT. Still no → Step 2."),
            ("Step2 Subtle", "so tell me more about you... what do you do when you're not making Colombian-Scottish girls lose their minds?", "SUBTLE TENSION. → Step 3 later."),
            ("Step3 ReAttempt", "I can't help it, there's something about you that's messing with my head right now", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "okay I'll chill... for now, no promises though haha", "ACCEPT. Door open."),
        ], "res"),
        "nosex2": ([
            ("Step1 Respect", "my bad I got ahead of myself, it's your fault for being so fun to talk to", "RESPECT. Still no → Step 2."),
            ("Step2 Subtle", "okay new topic but first... what's the craziest adventure you've ever been on?", "SUBTLE. → Step 3 later."),
            ("Step3 ReAttempt", "I'm trying to behave but you're making it really hard, there's something about you", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "fine I'll stop but don't blame me if it happens again later 😏", "ACCEPT."),
        ], "res"),
        # ── OFFTOPIC ──
        "offtopic1": ([
            ("Step1 Acknowledge", "haha wait that's actually funny", "ACKNOWLEDGE. Adapt. → Step 2."),
            ("Step2 Redirect", "but hold on you totally distracted me, I was about to tell you something and now I forgot", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay wait no I remember now, so like I was saying...", "RETAKE. Resume main script."),
        ], "res"),
        "offtopic2": ([
            ("Step1 Acknowledge", "lol okay that's random but I like it", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "wait no stop you're distracting me from what I was gonna say", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay focus, where was I... oh yeah", "RETAKE."),
        ], "res"),
        # ── REAL ──
        "real1": ([
            ("Step1 Humor", "lol do I look like a bot to you? beep boop... send $5 for human verification haha I'm kidding", "HUMOR. Still doubts → Step 2."),
            ("Step2 Challenge", "ask me anything, literally anything about me or my life. I'm an open book", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I get it there's a lot of fake stuff on here, but you felt something in this convo right? because I did and that's real", "GROUNDING."),
        ], "res"),
        "real2": ([
            ("Step1 Humor", "wait you think I'm not real?? that's actually the funniest thing anyone's said to me today", "HUMOR. Still → Step 2."),
            ("Step2 Challenge", "test me love, ask me something only a real person would know. go ahead", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I know there's tons of bots on here but what we've been talking about felt real to me. didn't it feel real to you?", "GROUNDING."),
        ], "res"),
        # ── VOICE ──
        "voice1": ([
            ("Step1 Dodge", "haha maybe one day if you earn it but not yet... I'm kind of private about that", "DODGE. Still asks → Step 2."),
            ("Step2 Redirect", "I have something way better for you though, trust me you'll forget you even asked", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "I don't do that on here but what I'm about to show you is better than any call love... you'll see", "FIRM."),
        ], "res"),
        "voice2": ([
            ("Step1 Dodge", "hmmm maybe but you gotta earn that first haha", "DODGE. Still → Step 2."),
            ("Step2 Redirect", "how about instead of a call I show you something that'll blow your mind?", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "that's not something I do on here but what I have for you is way better than hearing my voice, trust me", "FIRM."),
        ], "res"),
        # ── CUSTOMYES ──
        "customyes1": ([
            ("Step1 Tease", "you want that? hmm I might have something... actually I definitely have something", "TEASE. → Step 2."),
            ("Step2 Price", "I have exactly what you're thinking of, you're gonna lose it... [price]", "PRICE. Custom videos $100+/min. VCs $150+."),
            ("Step3 Close", "trust me you won't regret it, I made this one special", "CLOSE."),
        ], "res"),
        "customyes2": ([
            ("Step1 Tease", "oh you have good taste... I think I have exactly what you need", "TEASE. → Step 2."),
            ("Step2 Price", "I actually did something just like that, [price] and it's worth every cent", "PRICE. Custom videos $100+/min. VCs $150+."),
            ("Step3 Close", "you're not gonna be able to stop watching this one", "CLOSE."),
        ], "res"),
        # ── CUSTOMNO ──
        "customno1": ([
            ("Step1 Redirect", "I don't have exactly that but honestly I have something that'll make you forget you even asked", "REDIRECT. → Step 2."),
            ("Step2 Alternative", "actually what I have might be even crazier and literally no one else has seen it yet", "ALTERNATIVE + FOMO. → Step 3."),
            ("Step3 Close", "trust me... I know what you need better than you do 😏", "CLOSE."),
        ], "res"),
        "customno2": ([
            ("Step1 Redirect", "I don't have that specific thing but I have something you're gonna like even more", "REDIRECT. → Step 2."),
            ("Step2 Alternative", "what I DO have is something no one has ever seen and I think it's even better than what you asked for", "ALTERNATIVE. → Step 3."),
            ("Step3 Close", "just trust me on this one, you'll thank me later", "CLOSE."),
        ], "res"),
        # ── DONE ──
        "done1": ([
            ("Step1 Validate", "wait already?? that's so hot", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "but I haven't finished yet... don't you wanna watch me cum too?", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "okay but next time you have to wait for me, I have something insane planned for round 2", "SEED."),
        ], "res"),
        "done2": ([
            ("Step1 Validate", "already?? fuck that's hot, because of me??", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "wait but I'm not done yet, you're gonna leave me like this?", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "next time you HAVE to hold it because what I have planned for us is way crazier", "SEED."),
        ], "res"),

        # ── SITUATIONAL ──
        "cumcontrol": ([
            ("edge1", "don't cum yet... I'm not done with you", "EDGE. More PPVs left."),
            ("edge2", "hold it, not yet... I need you to last a little longer for me", "EDGE variant."),
            ("sync1", "I'm so close too, cum with me... but you need to see this first", "SYNC. Final PPV."),
            ("sync2", "wait for me, I want us to finish together... open this first", "SYNC variant."),
            ("delay1", "hold it... wait until you see what I'm about to send, trust me it's worth it", "DELAY."),
            ("delay2", "don't you dare finish before you see this, trust me you want to wait", "DELAY variant."),
        ], "sit"),
        "dickpic": ([
            ("dpsext1", "fuck okay that's... wow. you have no idea what that just did to me", "DURING SEXTING."),
            ("dpsext2", "oh fuck... that is... damn. I need to show you something right now", "DURING SEXTING variant."),
            ("dprapport1", "wow you don't waste time huh? that's actually really hot though ngl", "DURING RAPPORT."),
            ("dprapport2", "woah I was not expecting that but... damn 🥵", "DURING RAPPORT variant."),
            ("dpppv1", "you can't just send me that and expect me not to do something about it, hold on", "LEVERAGE. WAIT 1-2 min then send PPV."),
            ("dpppv2", "okay you just made me do something... give me a sec", "LEVERAGE variant."),
        ], "sit"),
        "boosters": ([
            ("h1", "fuckkk", "MID-SEXTING BOOSTER."),
            ("h2", "I'm so wet right now because of you", "BOOSTER. Ego."),
            ("h3", "don't stop", "BOOSTER. Micro."),
            ("h4", "you have no idea what you're doing to me", "BOOSTER."),
            ("h5", "I literally can't think straight right now", "BOOSTER."),
            ("h6", "my whole body is tingling", "BOOSTER. Physical."),
            ("h7", "more...", "BOOSTER. Ultra micro."),
            ("h8", "I should be at the beach but I can't move right now", "BOOSTER. Isabella personality."),
        ], "sit"),
    },
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
