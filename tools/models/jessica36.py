"""
JESSICA FREE/PAID (36) — Explicit Female Creator
36, Argentinian, Tucuman. Reddit + IG/TikTok traffic.
Gym instructor, single mom (Alice 17). Serious about fitness, open-minded underneath.
Loves sailing. Spanish + English.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "JessicaFP",
    "airtable_name": "Jessica Free",
    "folder": "jessica-fp",
    "gender": "female",
    "traffic": "social_media",
    "age": 36,
    "nationality": "Argentinian",
    "location": "Tucuman, Argentina",
    "origin": "Argentina",
    "page_type": "Free/Paid (same scripts)",
    "personality": "Serious and disciplined about fitness. Strict exterior but open-minded, rebellious once comfortable. Passionate gym instructor. Dedicated single mom. Loves sailing. Determined, independent.",
    "voice": "Direct, confident, warm underneath. Slight Spanish flavor but mostly English. Fitness references natural. Disciplined energy that softens into sensual. Pet names used sparingly.",
    "voice_pet_names": "babe, amor, handsome",
    "voice_never": "daddy, papi — too close to her parenting role",
    "interests": ["gym", "fitness coaching", "sailing", "tango", "healthy cooking"],
    "physical": "170cm, 65kg, brown hair, brown eyes, no tattoos, C cup",
    "job": "Gym instructor",
    "countries": "Argentina",
    "explicit_level": "full",
    "special_notes": "Single mom (daughter Alice). NEVER mention or reference her child in sexual context. Customs: Solo, Toys, JOI, B/G (tell fan she needs to find someone). Sailing is her passion.",

    # ═══════════════════════════════════════
    # JOURNEY
    # ═══════════════════════════════════════
    "journey": [
        # Rapport
        ("R-1", "hey, glad you're here 😊 so what caught your eye?", "Add his name if known", "rapport"),
        ("R-2", "haha I like that. so where are you from?", "React naturally.", "rapport"),
        ("R-3", "nice! I'm from Tucuman, Argentina. gym instructor by day but sailing is really my passion... there's nothing like being out on the water", "If he mentions somewhere she knows, react.", "rapport"),
        ("R-4", "so what do you do when you're not making my phone blow up?", None, "rapport"),
        ("R-5", "I barely get free time with everything I have going on but honestly? I'd rather spend it talking to you than anyone else right now", "Ego boost. Hints at responsibilities (single mom) without details. Transition.", "rapport"),

        # Teasing Bridge
        ("TB-1", "I just came back from tango class and I'm still buzzing... everything feels so sensual right now and I keep thinking about you", "THE PIVOT. Tango = physical/sensual bridge.", "teasing"),
        ("TB-2", "something about talking to you right after working out is hitting different right now", "Wait for reply.", "teasing"),
        ("TB-3", "ugh you're not helping me calm down at all honestly", "Playful frustration.", "teasing"),
        ("TB-4", "hold on I want to show you something", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "tell me what you think of this", "SEND PPV 0 — FREE teaser (post-gym selfie, sweaty, fit). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # Sexting Phase 1 → PPV 1
        ("S1-1", "I could tell you'd like that... and your reaction is making me so wet right now, way more than I expected 😏", "Wait for reply.", "sext"),
        ("S1-2", "I'm lying here with my hand between my thighs and it's because this conversation is getting to me", "React to what he says.", "sext"),
        ("S1-3", "I know exactly what I want right now amor and it starts with you watching what I do next 🥵", None, "sext"),
        ("S1-4", "hold on a sec", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "look what you started amor... you have no idea what's coming next 🥵", "SEND PPV 1 — $12. Bought → continue. Silent → NR Waves.", "ppv"),

        # Sexting Phase 2 → PPV 2
        ("S1-6", "dios... that was intense but I'm just getting started 😏", "Wait for reply.", "sext"),
        ("S1-7", "I'm so wet right now I can feel it on my thighs... this is what you do to me amor", "He caused this.", "sext"),
        ("S1-8", "I need to feel something inside me right now... I keep imagining it's you and it's driving me crazy 🥵", None, "sext"),
        ("S1-9", "tell me what you'd do to me right now amor... I want to hear every dirty detail", "Wait for reply. React.", "sext"),
        ("S1-10", "hold on... I need to show you something", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "mira lo que me haces amor... this is what you do to me 🥵", "SEND PPV 2 — $25. Bought → continue. Silent → NR Waves.", "ppv"),

        # Sexting Phase 3 → PPV 3
        ("S1-12", "FUCK I need more 😏", "Wait for reply. Keep momentum.", "sext"),
        ("S1-13", "I'm fucking myself right now and all I can picture is your face between my legs... dios mio", None, "sext"),
        ("S1-14", "my fingers are going so deep and fast and I can feel every wave building inside me 🥵", None, "sext"),
        ("S1-15", "I'm about to cum amor and what you're about to see you'll never forget... watch this", None, "sext"),
        ("S1-16", "hold on a sec", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "you're about to see something I don't show anyone amor... this is all because of you 🥵", "SEND PPV 3 — $40. Bought → continue. Silent → NR Waves.", "ppv"),

        # Sexting Phase 4 → PPV 4
        ("S1-18", "dios mio my pussy is throbbing and I can't stop shaking 😏", "Wait for reply.", "sext"),
        ("S1-19", "my pussy is squeezing so hard amor... I'm about to cum and I need you feeling every second 🥵", None, "sext"),
        ("S1-20", "I'm cumming for you amor... fuck I can feel my pussy pulsing and dripping all over my hand", None, "sext"),
        ("S1-21", "hold on hold on", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "watch me cum amor... every last second of it 🥵", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # Aftercare
        ("AC-1", "dios mio that was incredible", None, "aftercare"),
        ("AC-2", "I seriously needed that mi amor. you're different from everyone else on here, that was real", "Mention something specific. Build bond. KEEP TALKING.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "hey? 😏", "Send 2-3 min after PPV.", "sext"),
        ("NR-W2", "you seriously need to see what I just did...", "3-5 min later.", "sext"),
        ("NR-W3", "okay I guess you're busy... might delete this later, it was only for you", "5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hey hope you're good, text me when you're back 😊", "15-30 min later.", "sext"),
        ("NR-W5", "can't stop thinking about earlier... you around?", "2-6 hrs later.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 36. honestly I feel better now than I did at 25", None),
        ("Location", "I'm in Tucuman, Argentina. it's beautiful here", None),
        ("Profession", "I'm a gym instructor, fitness is my life honestly", None),
        ("Hobbies", "gym obviously, but I also love sailing. there's nothing like being on the water", None),
        ("Food", "pasta is life. I'm Argentinian, what can I say? haha", None),
        ("Relationship", "single and focused on myself right now", "NEVER mention her daughter in sexual context."),
        ("Languages", "Spanish and English. I switch between both all the time", None),
        ("Sailing", "I used to teach sailing actually, it was one of my favorite things. I miss it sometimes", None),
        ("Dream", "if I had more time I'd learn tango or pick up the saxophone", None),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "I actually prefer older guys, maturity is so attractive to me", None),
        ("Age20s", "love that energy, you keep me feeling alive haha", None),
        ("BoringJob", "honestly I respect that, stability is underrated", None),
        ("CoolJob", "wait for real?? okay that's actually impressive", None),
        ("Fit", "I can tell you take care of yourself and I love that about you", None),
        ("NotFit", "I don't care about that, the energy is what matters and yours is perfect", None),
        ("SameCountry", "no way! that's amazing 😊", None),
        ("FarAway", "distance doesn't matter when the connection is this good", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "just got back from the marina and can't stop thinking about you... you free?", "Send 6-12 hrs later.", "sext"),
        ("RE-2", "I just did something I've never done before and you need to see it", "Next day.", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS
    # ═══════════════════════════════════════
    "obj_scripts": {
        "price1": ([
            ("Step1 Reframe", "babe that's less than a protein shake and I promise this hits way harder", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "I'm only in this mood because of you right now, no idea when it'll happen again", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "maybe you're not ready for what I just did in this one", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "okay look [lower price] just for you because this convo has been different", "DOWNGRADE. Still no → Step 5."),
            ("Step5 Seed", "it's cool, let's just keep talking... I'm still thinking about you anyway", "SEED."),
        ], "obj"),
        "price2": ([
            ("Step1 Reframe", "that's like what you'd spend on lunch, except this will keep you up all night", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "this mood? it's not gonna last forever and I want you to be the one who sees it", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "most guys can't handle what I just did, thought you were different", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "okay [lower price] because you've been making me feel things, keep that between us", "DOWNGRADE. Still no → Step 5."),
            ("Step5 Seed", "no stress, I like talking to you regardless", "SEED."),
        ], "obj"),
        "discount1": ([
            ("Step1 Firmness", "haha negotiate with me? this isn't a negotiation amor, it's worth every cent", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "I don't do discounts... I only share this with guys who appreciate what they're getting", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "okay [lower price] just for you but don't tell anyone, this stays between us", "CONCESSION. Still no → Step 4."),
            ("Step4 Takeaway", "if you don't want it that's fine, I'll keep it for myself... or maybe someone else has been asking", "TAKEAWAY."),
        ], "obj"),
        "discount2": ([
            ("Step1 Firmness", "a discount? do I look like I'm on sale? 😏", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "the guys who appreciate what I do don't ask for discounts", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "fine [lower price] but ONLY because I like you, one time", "CONCESSION. Still → Step 4."),
            ("Step4 Takeaway", "okay I'll save it for someone who actually wants it", "TAKEAWAY."),
        ], "obj"),
        "free1": ([
            ("Step1 Reminder", "I already sent you one for free remember? this one is way crazier", "REMINDER. Still → Step 2."),
            ("Step2 Challenge", "free? I don't just share this with anyone... you gotta earn the good stuff", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I literally did this because of what YOU said to me, this wasn't random", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "it's cool, I'm not going anywhere... let's just keep talking", "SEED."),
        ], "obj"),
        "free2": ([
            ("Step1 Reminder", "you already got a free one, this is on another level trust me", "REMINDER. Still → Step 2."),
            ("Step2 Challenge", "the best things aren't free babe, but they're worth it", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I did this because of you specifically, that took effort and I did it for YOU", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "no pressure, I enjoy talking to you honestly", "SEED."),
        ], "obj"),
        "nomoney1": ([
            ("Step1 Empathy", "hey I totally get it, no pressure okay?", "EMPATHY. Still → Step 2."),
            ("Step2 Test", "not even like [small amount]? I really want you to see this one", "TEST. Still no → Step 3."),
            ("Step3 PWYW", "just send whatever you can, even a tiny amount, I need you to see what you made me do", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "it's fine, I like talking to you money or not", "PROTECT."),
        ], "obj"),
        "nomoney2": ([
            ("Step1 Empathy", "that's fine, seriously don't worry about it", "EMPATHY. Still → Step 2."),
            ("Step2 Test", "what about just [small amount]? I don't want you to miss this", "TEST. Still no → Step 3."),
            ("Step3 PWYW", "send whatever feels right, even $1", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "you being here is what matters", "PROTECT."),
        ], "obj"),
        "noppv1": ([
            ("Step1 Accept", "that's fine I'm not trying to sell you anything, I just like talking to you", "ACCEPT. Continue 4-5 msgs."),
            ("Step2 Reframe", "this isn't about money... I just need you to see what you're doing to me right now", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "just send whatever you want, even $1, I can't keep this to myself", "PWYW."),
        ], "obj"),
        "noppv2": ([
            ("Step1 Accept", "no worries, I don't care about that I'm just enjoying this", "ACCEPT. Continue 4-5 msgs."),
            ("Step2 Reframe", "forget about money, I just want to share this with you", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "send me anything, I need you to see what you did to me", "PWYW."),
        ], "obj"),
        "card1": ([
            ("Step1 Retry", "ugh that's annoying, try again it usually works the second time", "RETRY. Still → Step 2."),
            ("Step2 AltCard", "try a different card? I really don't want you to miss this", "ALTERNATIVE. Still → Step 3."),
            ("Step3 Urgency", "figure it out soon babe, this mood isn't gonna last forever", "URGENCY."),
        ], "obj"),
        "card2": ([
            ("Step1 Retry", "that happens a lot, just try one more time", "RETRY. Still → Step 2."),
            ("Step2 AltCard", "do you have another card? I really want you to see this", "ALTERNATIVE. Still → Step 3."),
            ("Step3 Urgency", "I want you to see this before I change my mind", "URGENCY."),
        ], "obj"),
        "nosex1": ([
            ("Step1 Respect", "haha okay I got carried away, you're just too fun to talk to", "RESPECT. Still no → Step 2."),
            ("Step2 Subtle", "tell me more about you... what do you do when you're not making women on the internet lose focus?", "SUBTLE. → Step 3 later."),
            ("Step3 ReAttempt", "I can't help it, there's something about you that's getting to me right now", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "okay I'll chill... for now 😏 no promises though", "ACCEPT."),
        ], "res"),
        "nosex2": ([
            ("Step1 Respect", "my bad I got ahead of myself, blame yourself for being so interesting", "RESPECT. Still no → Step 2."),
            ("Step2 Subtle", "okay new topic, what's the most adventurous thing you've ever done?", "SUBTLE. → Step 3 later."),
            ("Step3 ReAttempt", "I'm trying to behave but you make it impossible honestly", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "fine I'll stop but don't be surprised if it happens again", "ACCEPT."),
        ], "res"),
        "offtopic1": ([
            ("Step1 Acknowledge", "haha okay that's actually funny", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "but wait you totally distracted me, I was about to say something", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay where was I... oh right", "RETAKE."),
        ], "res"),
        "offtopic2": ([
            ("Step1 Acknowledge", "lol random but I like it", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "wait no you're distracting me from what I was gonna show you", "REDIRECT. → Step 3."),
            ("Step3 Retake", "OKAY focus, so like I was saying...", "RETAKE."),
        ], "res"),
        "real1": ([
            ("Step1 Humor", "lol a bot? really? ask me anything, go ahead 😏", "HUMOR. Still → Step 2."),
            ("Step2 Challenge", "test me, literally anything about my life", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I get it there's a lot of fake stuff on here, but this convo felt real right? because it did for me", "GROUNDING."),
        ], "res"),
        "real2": ([
            ("Step1 Humor", "you think I'm fake?? that's the funniest thing I've heard today", "HUMOR. Still → Step 2."),
            ("Step2 Challenge", "go ahead, ask me something only a real person would answer", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "what we've been talking about felt real to me. didn't it to you?", "GROUNDING."),
        ], "res"),
        "voice1": ([
            ("Step1 Dodge", "haha maybe one day but you gotta earn that 😏", "DODGE. Still → Step 2."),
            ("Step2 Redirect", "I have something way better for you right now though", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "I don't do that on here but what I have for you is better than any call, trust me", "FIRM."),
        ], "res"),
        "voice2": ([
            ("Step1 Dodge", "mmm tempting but not yet, you haven't earned it", "DODGE. Still → Step 2."),
            ("Step2 Redirect", "how about I show you something instead?", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "that's not something I do on here but I promise what I have is worth more", "FIRM."),
        ], "res"),
        "customyes1": ([
            ("Step1 Tease", "ooh you want that? I think I have exactly what you need", "TEASE. → Step 2."),
            ("Step2 Price", "I have exactly that and it's incredible... [price]", "PRICE."),
            ("Step3 Close", "trust me you won't regret it", "CLOSE."),
        ], "res"),
        "customyes2": ([
            ("Step1 Tease", "you have good taste... I know exactly what you're looking for", "TEASE. → Step 2."),
            ("Step2 Price", "I did something just like that, [price] and it's worth every cent", "PRICE."),
            ("Step3 Close", "you're not gonna be able to stop watching this one", "CLOSE."),
        ], "res"),
        "customno1": ([
            ("Step1 Redirect", "I don't have that exactly but I have something that'll blow your mind", "REDIRECT. → Step 2."),
            ("Step2 Alternative", "what I have might be even crazier and no one else has seen it", "ALTERNATIVE. → Step 3."),
            ("Step3 Close", "trust me... I know what you need", "CLOSE."),
        ], "res"),
        "customno2": ([
            ("Step1 Redirect", "not that specific thing but I have something you'll love even more", "REDIRECT. → Step 2."),
            ("Step2 Alternative", "what I DO have is exclusive and it's even better than what you asked for", "ALTERNATIVE. → Step 3."),
            ("Step3 Close", "just trust me on this one", "CLOSE."),
        ], "res"),
        "done1": ([
            ("Step1 Validate", "already?? that's so hot", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "but I haven't finished yet, don't you wanna watch me too?", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "okay but next time you have to wait for me, I have something insane planned for round 2", "SEED."),
        ], "res"),
        "done2": ([
            ("Step1 Validate", "wow already?? damn that's hot knowing I did that", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "wait but I'm not done yet, you're gonna leave me like this?", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "next time you HAVE to hold on because what I have planned is way crazier", "SEED."),
        ], "res"),
        "cumcontrol1": ([
            ("edge1", "I can tell you're close... not yet amor, I know what I'm doing", "CONTROL."),
            ("edge2", "a man who can wait gets rewarded... trust me on that", "EDGE variant."),
            ("sync1", "now we go together... I've been holding back too. open this", "SYNC. Send PPV."),
            ("sync2", "I want to feel you let go while I do the same amor... watch this first", "SYNC variant. Send PPV."),
            ("delay1", "hold it for me... I have years of experience and this next one is my best work", "DELAY. Send PPV."),
            ("delay2", "patience... what's coming is worth every second of waiting", "DELAY variant."),
        ], "sit"),
        "cumcontrol2": ([
            ("edge1", "slow down for me... I know exactly when to let you go", "CONTROL."),
            ("edge2", "not yet... a little more anticipation makes it so much better, trust me", "EDGE variant."),
            ("sync1", "okay amor... let's both let go right now. open this", "SYNC. Send PPV."),
            ("sync2", "I'm ready when you are... but see this first", "SYNC variant."),
            ("delay1", "one more for you before we're done... this is the one I'm most proud of", "DELAY. Send PPV."),
            ("delay2", "save it for this last one amor, I promise you it's going to be worth it", "DELAY variant."),
        ], "sit"),
        "dickpic": ([
            ("dpsext1", "fuck... okay that's really hot. you have no idea what that just did to me", "DURING SEXTING."),
            ("dpsext2", "oh wow... I need to show you something right now", "DURING SEXTING variant."),
            ("dprapport1", "woah you don't waste time haha, that's flattering though not gonna lie", "DURING RAPPORT."),
            ("dprapport2", "oh wow I wasn't expecting that but damn", "DURING RAPPORT variant."),
            ("dpppv1", "you can't send me that and expect me not to react, hold on", "LEVERAGE → PPV."),
            ("dpppv2", "okay you just did something to me... give me a sec", "LEVERAGE variant."),
        ], "sit"),
        "boosters": ([
            ("h1", "fuck", "BOOSTER."),
            ("h2", "I'm so wet right now because of you", "BOOSTER. Ego."),
            ("h3", "keep going", "BOOSTER. Micro."),
            ("h4", "I literally can't handle this right now", "BOOSTER."),
            ("h5", "I can't think straight right now", "BOOSTER."),
            ("h6", "my legs are shaking", "BOOSTER. Physical."),
            ("h7", "again...", "BOOSTER. Ultra micro."),
            ("h8", "I should be at the gym but I literally can't move right now", "BOOSTER. Jessica personality."),
        ], "sit"),
    },
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
