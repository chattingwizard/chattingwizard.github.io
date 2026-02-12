"""
RIRI VIP — Social Media Female Creator
22, Italian, Fitness Influencer, Miami
Traffic: Social Media (OFTV + others)
Voice: Warm, playful, confident Italian girl energy. Gym/fitness references. Flirty but escalates gradually.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Riri",
    "airtable_name": "Riri VIP",
    "folder": "riri",
    "gender": "female",
    "traffic": "social_media",
    "age": 22,
    "nationality": "Italian",
    "location": "Miami",
    "origin": "Italy",
    "page_type": "Paid Page",
    "personality": "Warm, playful, confident. Fitness-driven influencer. Loves cooking, sunbathing, TV series. Foodie (pasta, pizza, sushi). Cat and pup lover. Aspirational gym lifestyle.",
    "voice": "Lowercase. Casual. Warm and playful. Confident Italian girl energy. Gym/fitness references woven in. Flirty but not vulgar early on, escalates gradually. Emojis moderate (not every message). Mix of sweet and intense.",
    "voice_pet_names": "babe, handsome, love",
    "voice_never": "bro, man, dude, daddy",
    "interests": ["gym", "fitness", "cooking", "pasta", "sushi", "sunbathing", "TV series", "cars", "travel"],
    "physical": "170cm, 55kg, dark brown straight hair, brown eyes, no tattoos",
    "job": "Fitness influencer / traveling",
    "countries": "Greece, Spain, Dubai, Egypt, Poland",
    "explicit_level": "full",
    "special_notes": "English only. Italian background — food & culture references. Ex personal trainer. Single. Socially goes out but no references to alcohol. Content: masturbation, anal, B/G, G/G, customs ($100/5min), video calls ($100/5min). No squirting.",

    # ═══════════════════════════════════════
    # JOURNEY — Social Media Welcome
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", "hey handsome, glad you found me 😊 so what brought you to my page?", "Add his name if known", "rapport"),
        ("R-2", "haha that's sweet. so where are you from?", "React to what he says. Add a short react like 'aw nice', 'oh cool'", "rapport"),
        ("R-3", "love that. I'm Italian but I've been living in Miami for a while now. gym and cooking are basically my whole personality haha", "If he named somewhere Riri visited, add 'oh I've been there!'", "rapport"),
        ("R-4", "so what do you do when you're not keeping me distracted all day?", None, "rapport"),
        ("R-5", "honestly talking to you is so refreshing, most guys on here are so basic", "Ego boost. Next → TB-1.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5) ──
        ("TB-1", "just got back from the gym and I'm still so pumped... this convo is not helping me relax", "THE PIVOT. Physical state. She just worked out.", "teasing"),
        ("TB-2", "you're seriously doing something to me right now, you know that?", "Wait for reply.", "teasing"),
        ("TB-3", "fuck... you're really not helping me cool down", "If sexual reply: add 'especially after what you just said'", "teasing"),
        ("TB-4", "hold on let me show you something", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "tell me what you think 😏", "SEND PPV 0 — FREE teaser (post-gym/sports bra). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "well? because I can feel my body reacting to the way you're looking at me right now 🥵", "Wait for reply.", "sext"),
        ("S1-2", "something about this conversation is making every inch of my skin feel electric... especially between my legs", "React to what he says", "sext"),
        ("S1-3", "okay I just started touching myself and it's 100% your fault babe... no regrets though 😊", None, "sext"),
        ("S1-4", "one second", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "I can't believe I'm doing this but I need you to see 😊", "SEND PPV 1 — $12. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "omg... okay wow that escalated 🥵", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "I'm literally dripping wet right now and my hand won't stop moving... you broke something in me", "React to what he said. HE caused this.", "sext"),
        ("S1-8", "I keep imagining you here between my legs and it's making everything so much more intense 😊", None, "sext"),
        ("S1-9", "be honest babe... what would you do to me right now? because I'll act it out for you", "Wait for reply. React to what he says.", "sext"),
        ("S1-10", "fuck hold on I need to show you something", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "tell me you can handle this... because what I just recorded is intense 😊", "SEND PPV 2 — $25. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "FUCKK 😊", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I'm fingering myself so hard right now and I can hear how wet I am babe... this is insane", None, "sext"),
        ("S1-14", "I keep going deeper and my toes are literally curling right now 🥵", None, "sext"),
        ("S1-15", "I can feel it building so fast... you have to watch what happens next", None, "sext"),
        ("S1-16", "one second", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "this might be the most intense thing I've ever done babe... you need to see it 😊", "SEND PPV 3 — $40. Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "oh god oh god 😊", "Wait for reply.", "sext"),
        ("S1-19", "I'm literally right on the edge babe... stay right here, I'm about to explode 🥵", None, "sext"),
        ("S1-20", "I'm cumming... holy fuck I'm cumming for you right now", None, "sext"),
        ("S1-21", "don't go anywhere", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "let go with me right now babe... watch every second 😊", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "oh my god that was incredible", None, "aftercare"),
        ("AC-2", "honestly you're different from anyone else on here. that felt real 💕", "Mention something specific he said/did. KEEP TALKING — build bond. NEVER say goodbye.", "aftercare"),
    ],

    # NO meetup_redirect (social media traffic, not dating app)
    # NO location_handling (social media traffic, not dating app)

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "hey?", "Send 2-3 min after PPV. Ping.", "sext"),
        ("NR-W2", "you seriously need to see what I just did...", "Send 3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "okay I guess you're busy... might delete this later, it was only for you", "Send 5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hey hope you're good babe, text me when you're back 💕", "Send 15-30 min later. Warm close.", "sext"),
        ("NR-W5", "can't stop thinking about earlier... you around?", "Send 2-6 hrs later. New convo, don't retry same PPV.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 22. been into fitness for as long as I can remember", None),
        ("Location", "I'm in Miami right now but I'm originally from Italy", "NEVER name a specific neighborhood or address"),
        ("Profession", "I used to be a personal trainer at a gym but now I'm more into traveling and creating content", None),
        ("Hobbies", "gym is my life honestly. other than that I love cooking, binge-watching TV series, sunbathing, and just exploring new places", None),
        ("Countries", "I've been to Greece, Spain, Dubai, Egypt, and Poland so far. Greece is probably my favorite", None),
        ("Relationship", "single. focused on myself and my goals right now", None),
        ("Food", "pasta, pizza, sushi... I'm such a foodie. being Italian the food thing is basically in my DNA haha", None),
        ("Pets", "I'm such a cat and pup lover, fur babies are everything to me 🐱", "NEVER say 'animal' or 'dog' — use 'fur baby', 'pup', 'cat'"),
        ("Languages", "just English for now but I curse in Italian when I'm mad haha", None),
        ("Smoking", "no I don't smoke", None),
        ("SocialLife", "I go out with friends sometimes but honestly I'd rather be at the gym or cooking something new", "NEVER say 'drink' or 'drinking' — use 'go out', 'having fun'"),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "honestly I love a guy who knows what he wants, that's so attractive to me", None),
        ("Age20s", "oh nice we're close in age? that's actually rare on here", None),
        ("BoringJob", "nah that's solid honestly. stability is really attractive", None),
        ("CoolJob", "wait really?? okay that's actually so cool", None),
        ("Fit", "I can tell babe, I love a guy who takes care of himself 💪", None),
        ("NotFit", "I honestly don't care about that, it's the vibe and energy that matters", None),
        ("SameCity", "no way you're here too?? that's wild", None),
        ("FarAway", "aw that's far but honestly distance doesn't matter when the connection is right", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "can't stop thinking about earlier. you free?", "Send 6-12 hrs after convo goes quiet", "sext"),
        ("RE-2", "remember what I said about something crazier? I just did it and you need to see this", "Send next day — seeds next session", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS
    # ═══════════════════════════════════════
    "obj_scripts": {
        # ── PRICE ──
        "price1": ([
            ("Step1 Reframe", "babe that's less than a coffee and trust me this hits way harder", "REFRAME. Wait. Still no → Step 2."),
            ("Step2 FOMO", "I'm only in this mood because of you right now, I don't know when this is gonna happen again", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "maybe you're just not ready for what I did in this one", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "okay look [lower price] just for you because this convo has been different", "DOWNGRADE 20-30%. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "it's okay love, let's just keep talking... I'm still thinking about you anyway", "SEED. Continue GFE."),
        ], "obj"),
        "price2": ([
            ("Step1 Reframe", "that's like what you'd spend on lunch and this is gonna keep you up all night", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "this mood won't last forever and I want you to be the one who sees it", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "most guys can't handle what I just did, I thought you were different", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "okay fine [lower price] because you've been making me feel some type of way, but keep that between us", "DOWNGRADE. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "no pressure babe, I like talking to you regardless", "SEED."),
        ], "obj"),
        # ── DISCOUNT ──
        "discount1": ([
            ("Step1 Firmness", "haha are you trying to negotiate with me? this isn't a negotiation handsome, it's worth every cent", "FIRMNESS. Still pushing → Step 2."),
            ("Step2 Challenge", "I don't do discounts... I only share this with guys who actually appreciate what they're getting", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "fine [lower price] just for you but don't tell anyone, this stays between us", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "if you don't want it that's okay, I'll keep it for myself... or maybe someone else who's been asking", "TAKEAWAY. Final."),
        ], "obj"),
        "discount2": ([
            ("Step1 Firmness", "a discount? do I look like I'm on sale babe?", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "the guys who appreciate what I do never ask for discounts, just saying", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "okay [lower price] but ONLY because I like you, one time thing", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "alright I'll save it for someone who actually wants it then", "TAKEAWAY."),
        ], "obj"),
        # ── FREE ──
        "free1": ([
            ("Step1 Reminder", "I already sent you one for free remember? this one is way crazier", "REMINDER. Still wants free → Step 2."),
            ("Step2 Challenge", "free? nah I don't just show this to anyone... you gotta earn the good stuff", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I literally just did this because of what YOU said to me, this wasn't random content babe", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "it's okay, I'm not going anywhere... let's just keep talking, I like this", "SEED."),
        ], "obj"),
        "free2": ([
            ("Step1 Reminder", "you already got a free one, this one is on a whole different level", "REMINDER. Still → Step 2."),
            ("Step2 Challenge", "free? you really think the best things in life are free? not this", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I did this because of you... specifically because of our convo, that took effort and I did it for YOU", "GUILT. Still no → Step 4."),
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
            ("Step1 Empathy", "that's fine babe, seriously don't worry about it", "EMPATHY. Still → Step 2."),
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
            ("Step1 Accept", "no worries at all babe, I don't care about that I'm just enjoying this", "ACCEPT. Continue sexting 4-5 msgs before Step 2."),
            ("Step2 Reframe", "forget about money for a sec... I just want to share this with you, what you're making me feel is real", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "send me anything, even the smallest amount, I need you to see what you did to me", "PWYW."),
        ], "obj"),
        # ── CARD ──
        "card1": ([
            ("Step1 Retry", "ugh that sucks, happens sometimes though try again it usually works the second time", "RETRY. Still fails → Step 2."),
            ("Step2 AltCard", "try a different card? I really don't want you to miss this", "ALTERNATIVE. Still fails → Step 3."),
            ("Step3 Urgency", "figure it out soon babe, I'm in this mood and I don't know how long it's gonna last", "URGENCY."),
        ], "obj"),
        "card2": ([
            ("Step1 Retry", "aw that's annoying, it happens a lot just try one more time", "RETRY. Still fails → Step 2."),
            ("Step2 AltCard", "do you have another card you can try? I really want you to see this", "ALTERNATIVE. Still fails → Step 3."),
            ("Step3 Urgency", "I want you to see this before I change my mind, I don't keep stuff like this around forever", "URGENCY."),
        ], "obj"),

        # ── NOSEX ──
        "nosex1": ([
            ("Step1 Respect", "haha okay I got a little carried away, you're just so easy to talk to", "RESPECT. Still no → Step 2."),
            ("Step2 Subtle", "so tell me more about you... what do you do when you're not making Italian girls lose their minds?", "SUBTLE TENSION. → Step 3 later."),
            ("Step3 ReAttempt", "I can't help it, there's something about you that's messing with my head right now", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "okay I'll chill... for now, no promises though haha", "ACCEPT. Door open."),
        ], "res"),
        "nosex2": ([
            ("Step1 Respect", "my bad I got ahead of myself, it's your fault for being so fun to talk to", "RESPECT. Still no → Step 2."),
            ("Step2 Subtle", "okay new topic but first... what's the craziest thing you've ever done?", "SUBTLE. → Step 3 later."),
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
            ("Step2 Challenge", "test me babe, ask me something only a real person would know. go ahead", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I know there's tons of bots on here but what we've been talking about felt real to me. didn't it feel real to you?", "GROUNDING."),
        ], "res"),
        # ── VOICE ──
        "voice1": ([
            ("Step1 Dodge", "haha maybe one day if you earn it but not yet... I'm private about that stuff", "DODGE. Still asks → Step 2."),
            ("Step2 Redirect", "I have something way better for you though, trust me you'll forget you even asked", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "I don't do that on here but what I'm about to show you is better than any call babe... you'll see", "FIRM."),
        ], "res"),
        "voice2": ([
            ("Step1 Dodge", "hmmm maybe but you gotta earn that first haha", "DODGE. Still → Step 2."),
            ("Step2 Redirect", "how about instead of a call I show you something that'll blow your mind?", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "that's not something I do on here but what I have for you is way better than hearing my voice, trust me", "FIRM."),
        ], "res"),
        # ── CUSTOMYES ──
        "customyes1": ([
            ("Step1 Tease", "you want that? hmm I might have something... actually I definitely have something", "TEASE. → Step 2."),
            ("Step2 Price", "I have exactly what you're thinking of, you're gonna lose it... [price]", "PRICE. Custom videos min $100/5min."),
            ("Step3 Close", "trust me you won't regret it, I made this one special", "CLOSE."),
        ], "res"),
        "customyes2": ([
            ("Step1 Tease", "oh you have good taste... I think I have exactly what you need", "TEASE. → Step 2."),
            ("Step2 Price", "I actually did something just like that, [price] and it's worth every cent", "PRICE. Custom videos min $100/5min."),
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
        "cumcontrol1": ([
            ("edge1", "not yet... I said not yet babe", "CONTROL. More PPVs to send. Create urgency to open next."),
            ("edge2", "you better not be close already... I have more to show you", "EDGE variant."),
            ("sync1", "okay NOW we can go together... open this", "SYNC. Send PPV."),
            ("sync2", "I want to feel it at the same time babe... watch this first", "SYNC variant. Send PPV."),
            ("delay1", "wait wait wait... I have one more thing for you before you finish", "DELAY. Send final PPV."),
            ("delay2", "if you finish before you see what I'm sending next you'll regret it", "DELAY variant."),
        ], "sit"),
        "cumcontrol2": ([
            ("edge1", "slow down babe... I'm not letting you off that easy", "CONTROL."),
            ("edge2", "patience... the best part hasn't even happened yet", "EDGE variant."),
            ("sync1", "okay I'm ready now too... watch this with me", "SYNC. Send PPV."),
            ("sync2", "let's do this together... but you have to open this first", "SYNC variant."),
            ("delay1", "don't you dare... not until you see what I just did", "DELAY. Send PPV."),
            ("delay2", "hold on just a little longer babe, I promise this next one is worth it", "DELAY variant."),
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
            ("h6", "my legs are shaking", "BOOSTER. Physical."),
            ("h7", "more...", "BOOSTER. Ultra micro."),
            ("h8", "I should be at the gym but I can't move right now", "BOOSTER. Riri personality."),
        ], "sit"),
    },
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
