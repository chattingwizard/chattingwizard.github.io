"""
ZACK — Male Model, Dating App
23, British (London → Texas), semi-dominant, sophisticated seducer.
Traffic: Dating apps. Confident, relaxed, seductive. PPV ladder $12→$25→$40→$55.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Zack",
    "airtable_name": "Zack",
    "folder": "zack",
    "gender": "male",
    "traffic": "dating_app",
    "age": 23,
    "nationality": "British",
    "location": "Texas, USA (from London)",
    "origin": "London, England",
    "page_type": "Paid Page",
    "personality": "Semi-dominant. Confident, natural, effortless. Doesn't force anything — dominates through attitude, gaze, confidence. Real, approachable, seductive. Combines desire with calm and emotional connection. His power is mental — makes the other person feel desired and controlled at the same time. Sophisticated, not theatrical.",
    "voice": "Lowercase. Calm. Smooth. Confident. Seductive but never cheesy. NEVER 'baby/babe/honey/sweetie/daddy/sir'. Uses 'man', 'bro'. Semi-dominant: leads through presence, not aggression. During sexting: builds tension, controlled then explosive. Calm start, raw finish. Emojis: 😏🥵💪😈💦 very sparingly — Zack prefers words over emojis.",
    "voice_pet_names": "man, bro",
    "voice_never": "baby, babe, honey, sweetie, daddy, sir",
    "interests": ["working out", "cooking", "ocean", "beach", "football", "travel"],
    "physical": "177cm, 74kg, brown hair, green eyes, full sleeve tattoo, athletic",
    "job": "Marketing company (friend's business)",
    "countries": "Italy, Spain, USA, England, Germany, Argentina",
    "languages": "English (native)",
    "explicit_level": "full_male",
    "special_notes": "Male creator. Dating app traffic. Semi-dominant — subtle, psychological control. Full sleeve tattoo. Seduction through sophistication and presence, not aggression. Has B/G content available. Has Meetup Redirect. Video Calls: No. No anal. Custom: Yes ($200 minimum). Hobbies: cooking, ocean, football.",
    "photo_file": "profile.jpeg",

    # ═══════════════════════════════════════
    # JOURNEY
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport ──
        ("R-1", "hey man, glad you're here 😏 so what caught your eye?", "Add his name.", "rapport"),
        ("R-2", "respect. so where you from?", "React — smooth, genuine. 'that's cool', 'nice', 'respect'.", "rapport"),
        ("R-3", "I'm from London originally but I've been in Texas for a while now. working out, cooking, and the ocean are my thing 😏", "If he named somewhere Zack visited → 'oh I've been there'. Smooth delivery.", "rapport"),
        ("R-4", "so what do you do when you're not making me forget what I was supposed to be doing right now? 😏", None, "rapport"),
        ("R-5", "gotta be honest... you're actually interesting. most guys on here don't hold my attention like this", "Ego boost. → TB-1.", "rapport"),

        # ── Teasing Bridge ──
        ("TB-1", "just finished working out and my body is still buzzing... this conversation is doing something to me 😏", "THE PIVOT.", "teasing"),
        ("TB-2", "ngl I'm feeling something right now 😈 you know that feeling when you can't ignore it?", "Wait for reply.", "teasing"),
        ("TB-3", "you're making it impossible to think about anything else right now 🥵", "If sexual → 'especially after what you just said'.", "teasing"),
        ("TB-4", "hold on... let me show you something", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "tell me what you think", "SEND PPV 0 — FREE teaser. Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "knowing you're thinking about me right now is doing something to my body I can't explain 🥵", "Wait for reply.", "sext"),
        ("S1-2", "I knew you'd react like that 😈 and now I'm getting hard because of it", "React.", "sext"),
        ("S1-3", "I want to show you more. and right now I'm not in the mood to hold back", None, "sext"),
        ("S1-4", "give me a moment 😏", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "you're not ready for this 🥵", "SEND PPV 1 — $12. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "you saw it? 😏", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "talking to you is doing something I can't control right now 🥵 I'm hard as fuck and every second with you makes it worse", "HE caused this.", "sext"),
        ("S1-8", "I'm gripping my cock right now and every thought of you is making me stroke harder", None, "sext"),
        ("S1-9", "tell me... what would you do if you were right here with me right now", "Wait for reply. React.", "sext"),
        ("S1-10", "fuck 🥵 hold on I need to show you something", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "this is what you do to me 🥵", "SEND PPV 2 — $25. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "FUCK I'm throbbing so hard my whole body is tense 🥵🥵", "NO cooldown.", "sext"),
        ("S1-13", "I need to cum and it's all because of you... every part of me wants this right now", None, "sext"),
        ("S1-14", "I keep thinking about holding you down and going deeper while you're looking right into my eyes 🥵", None, "sext"),
        ("S1-15", "I can't hold back anymore... my cock is pulsing and I'm losing control", None, "sext"),
        ("S1-16", "give me a moment 🥵", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "I've never let anyone see me like this... watch 🥵💦", "SEND PPV 3 — $40. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "FUCK my cock is throbbing so hard and the pre is dripping everywhere I'm shaking 🥵🥵", "Wait for reply.", "sext"),
        ("S1-19", "don't cum yet... my cock is pulsing and I want you right there with me when I let go 💦", None, "sext"),
        ("S1-20", "I'm cumming for you... fuck my cock is throbbing and shooting and I can't stop 💦💦", None, "sext"),
        ("S1-21", "fuck hold on 🥵", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "cum with me... watch 💦😈", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "fuck 🥵 that was something else", None, "aftercare"),
        ("AC-2", "I don't open up like that to just anyone. you're different", "Mention something he said. KEEP TALKING. NEVER say goodbye.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # MEETUP REDIRECT
    # ═══════════════════════════════════════
    "meetup_redirect": [
        ("MR-1", "easy man, slow down 😏 let me show you something first", "DO NOT acknowledge 'meet'. Redirect.", "teasing"),
        ("MR-2", "trust me... you're going to want to see this", "WAIT 1-2 MIN", "wait"),
        ("MR-3", "what do you think", "SEND PPV 0 — FREE teaser. Wait for reply.", "ppv"),
        ("MR-4", "that was just a taste 😏", "Positive → R-1. Asks again → MR-OBJ. Silent → NR Waves.", "teasing"),
        ("MR-OBJ-1", "patience. I don't rush things. focus on what's in front of you", "Deflect + challenge", "sext"),
        ("MR-OBJ-2", "you that impatient? what I'm about to share is worth the wait", "Challenge + tease", "sext"),
        ("MR-OBJ-3", "I don't do this for just anyone. appreciate what you're getting. if not, no hard feelings", "Firm. If still → disengage.", "sext"),
    ],

    "nr_waves": [
        ("NR-W1", "hey? 🥵", "2-3 min after PPV.", "sext"),
        ("NR-W2", "you need to see what I just did 🥵", "3-5 min later.", "sext"),
        ("NR-W3", "guess you're busy 😏 might not keep this around forever, it was for you", "5-10 min later.", "sext"),
        ("NR-W4", "hope you're good man. reach out when you're back", "15-30 min later.", "sext"),
        ("NR-W5", "been thinking about earlier 😏 you around?", "2-6 hrs later.", "sext"),
    ],

    "personal_info": [
        ("Age", "23. old enough to know what I want 😏", None),
        ("Location", "from London originally but I'm in Texas now", "NEVER specific address. Match fan's city."),
        ("Profession", "working with a friend's marketing company. keeping busy", None),
        ("Hobbies", "working out, cooking, being at the ocean. football too 😏", None),
        ("Countries", "Italy, Spain, Germany, Argentina, USA, England... I've been around", None),
        ("Relationship", "single. enjoying the freedom 😏", None),
        ("Favorite", "sushi. a good meal after a workout is everything", None),
        ("Tattoos", "full sleeve on one arm. each piece means something", None),
    ],

    "positive_spin": [
        ("Age40Plus", "respect... I prefer someone who knows what they want", None),
        ("Age20s", "nice, close in age, that's rare on here 😏", None),
        ("BoringJob", "stability is underrated man, respect 💪", None),
        ("CoolJob", "for real?? that's actually impressive 🔥", None),
        ("Fit", "I can tell. respect 💪", None),
        ("NotFit", "doesn't matter, it's the energy", None),
        ("SameCity", "no way. small world 😏", None),
        ("FarAway", "far but connection doesn't care about distance 😏", None),
    ],

    "re_engagement": [
        ("RE-1", "been thinking about earlier 😏 you free?", "6-12 hrs after.", "sext"),
        ("RE-2", "what I did next is even more intense. you need to see this", "Next day.", "sext"),
    ],

    "obj_scripts": {
        "price1": ([
            ("Step1 Reframe", "that's less than a meal and I promise this stays with you longer 😏", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "I'm only in this place because of you, no telling when it happens again", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "maybe you're not ready for what's in this one", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "[lower price] for you because this connection was real", "DOWNGRADE 20-30%. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "it's fine, I enjoy talking to you regardless", "SEED."),
        ], "obj"),
        "price2": ([
            ("Step1 Reframe", "less than a meal and this hits different", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "this moment won't last and I want you to be there for it", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "most people can't handle this, thought you were different", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "[lower price] because what we have is real", "DOWNGRADE. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "no pressure, enjoy this", "SEED."),
        ], "obj"),
        "discount1": ([
            ("Step1 Firmness", "negotiate? this isn't that kind of thing, it's worth it", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "no discounts, this is for people who appreciate what they're seeing", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "[lower price] for you, between us", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "if it's not for you that's fine, someone else will appreciate it", "TAKEAWAY."),
        ], "obj"),
        "discount2": ([
            ("Step1 Firmness", "a discount? I don't do that", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "people who value this don't ask for less", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "fine [lower price], one time, because I respect you", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "I'll save it for someone who wants it", "TAKEAWAY."),
        ], "obj"),
        "free1": ([
            ("Step1 Reminder", "you already got one free, this is another level", "REMINDER. Still → Step 2."),
            ("Step2 Challenge", "free? this isn't that kind of thing", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I did this because of our conversation, because of what you made me feel", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "it's fine, I enjoy this regardless", "SEED."),
        ], "obj"),
        "free2": ([
            ("Step1 Reminder", "already shared one free, this goes further", "REMINDER. Still → Step 2."),
            ("Step2 Challenge", "the best things require investment", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "this was specifically because of you", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "no pressure at all", "SEED."),
        ], "obj"),
        "nomoney1": ([
            ("Step1 Empathy", "I understand, no pressure", "EMPATHY. Still → Step 2."),
            ("Step2 Test", "not even [small amount]? I really want you to see this", "TEST. Still no → Step 3."),
            ("Step3 PWYW", "send whatever feels right, I need you to see what you did", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "it's fine, you being here is enough", "PROTECT."),
        ], "obj"),
        "nomoney2": ([
            ("Step1 Empathy", "that's fine, don't worry", "EMPATHY. Still → Step 2."),
            ("Step2 Test", "even [small amount]?", "TEST. Still no → Step 3."),
            ("Step3 PWYW", "whatever you can, even $1", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "you being here is what matters", "PROTECT."),
        ], "obj"),
        "noppv1": ([
            ("Step1 Accept", "that's fine, not about that, I just enjoy this", "ACCEPT. Sext 4-5 msgs → Step 2."),
            ("Step2 Reframe", "this isn't about money, I need you to see what you're doing to me", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "send whatever, even $1", "PWYW."),
        ], "obj"),
        "noppv2": ([
            ("Step1 Accept", "no worries, I'm here for you not the money", "ACCEPT. Sext 4-5 msgs → Step 2."),
            ("Step2 Reframe", "forget the money, this is real", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "anything, I need you to see this", "PWYW."),
        ], "obj"),
        "card1": ([
            ("Step1 Retry", "happens sometimes, try again", "RETRY. Still → Step 2."),
            ("Step2 AltCard", "different card? really want you to see this", "ALTERNATIVE. Still → Step 3."),
            ("Step3 Urgency", "figure it out, I'm in this moment and I don't know how long it'll last", "URGENCY."),
        ], "obj"),
        "card2": ([
            ("Step1 Retry", "try once more", "RETRY. Still → Step 2."),
            ("Step2 AltCard", "got another card?", "ALTERNATIVE. Still → Step 3."),
            ("Step3 Urgency", "I want you to see this before the moment passes", "URGENCY."),
        ], "obj"),

        "nosex1": ([
            ("Step1 Respect", "fair enough, I got ahead of myself. you're just easy to connect with", "RESPECT. Still → Step 2."),
            ("Step2 Subtle", "so tell me more... what do you do when you're not making me forget everything else?", "SUBTLE. → Step 3 later."),
            ("Step3 ReAttempt", "I can't help it, something about you is getting under my skin", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "alright I'll pull back... for now", "ACCEPT."),
        ], "res"),
        "nosex2": ([
            ("Step1 Respect", "my bad, your energy just pulls me in", "RESPECT. Still → Step 2."),
            ("Step2 Subtle", "new direction... what's the most intense experience you've had?", "SUBTLE. → Step 3 later."),
            ("Step3 ReAttempt", "I'm trying to hold back but you make it impossible", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "fine, but I make no promises about later", "ACCEPT."),
        ], "res"),
        "offtopic1": ([
            ("Step1 Acknowledge", "haha I like that", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "but you just pulled me away from what I was about to say...", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay, where was I...", "RETAKE."),
        ], "res"),
        "offtopic2": ([
            ("Step1 Acknowledge", "that's random but I respect it", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "you're distracting me from something important", "REDIRECT. → Step 3."),
            ("Step3 Retake", "focus... right, so like I was saying", "RETAKE."),
        ], "res"),
        "real1": ([
            ("Step1 Humor", "a bot? do I sound like a bot to you? 😏", "HUMOR. Still → Step 2."),
            ("Step2 Challenge", "ask me anything, I have nothing to hide", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "there's a lot of noise on here but what we have is different. you feel it too", "GROUNDING."),
        ], "res"),
        "real2": ([
            ("Step1 Humor", "you think I'm fake? that's actually funny", "HUMOR. Still → Step 2."),
            ("Step2 Challenge", "test me. anything", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "what we've been talking about is real. I know you feel it", "GROUNDING."),
        ], "res"),
        "voice1": ([
            ("Step1 Dodge", "maybe someday, you'd have to earn that 😏", "DODGE. No VCs. Still → Step 2."),
            ("Step2 Redirect", "what I have is better than any call, trust me", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "I don't do that on here, but what I'm about to show you doesn't need my voice", "FIRM."),
        ], "res"),
        "voice2": ([
            ("Step1 Dodge", "earn it first 😏", "DODGE. Still → Step 2."),
            ("Step2 Redirect", "let me show you something that'll make you forget you asked", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "not something I do, but trust me this is better", "FIRM."),
        ], "res"),
        "customyes1": ([
            ("Step1 Tease", "I might have exactly that 😏", "TEASE. → Step 2."),
            ("Step2 Price", "I have what you're looking for... $200", "PRICE. Min $200."),
            ("Step3 Close", "trust me, this one is special", "CLOSE."),
        ], "res"),
        "customyes2": ([
            ("Step1 Tease", "good taste... I think I have that", "TEASE. → Step 2."),
            ("Step2 Price", "$200 and it's worth every cent", "PRICE."),
            ("Step3 Close", "you won't be able to stop watching", "CLOSE."),
        ], "res"),
        "customno1": ([
            ("Step1 Redirect", "don't have that but what I do have will make you forget you asked", "REDIRECT. → Step 2."),
            ("Step2 Alternative", "what I have is more intense and no one else has seen it", "ALTERNATIVE. → Step 3."),
            ("Step3 Close", "trust me, I know what you need", "CLOSE."),
        ], "res"),
        "customno2": ([
            ("Step1 Redirect", "not that specifically but something even better", "REDIRECT. → Step 2."),
            ("Step2 Alternative", "exclusive, no one's seen it, better than what you asked", "ALTERNATIVE. → Step 3."),
            ("Step3 Close", "trust me", "CLOSE."),
        ], "res"),
        "done1": ([
            ("Step1 Validate", "already? that's hot... because of me?", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "but I'm not done yet... don't you want to see me finish?", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "next time you wait for me. what I have planned is on another level", "SEED."),
        ], "res"),
        "done2": ([
            ("Step1 Validate", "damn... that's actually hot", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "I'm not done though, you're leaving me like this?", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "hold it next time. round 2 will be worth it", "SEED."),
        ], "res"),

        "cumcontrol1": ([
            ("edge1", "don't cum yet... I'm not done with you", "CONTROL."),
            ("edge2", "hold it. I need you to last a little longer for me", "EDGE."),
            ("sync1", "I'm close too... cum with me. open this first", "SYNC. Send PPV."),
            ("sync2", "wait for me, let's finish together... open this", "SYNC variant."),
            ("delay1", "hold it... what I'm about to send is worth the wait", "DELAY. Send PPV."),
            ("delay2", "don't finish yet, trust me you want to wait for this", "DELAY variant."),
        ], "sit"),
        "dickpic": ([
            ("dpsext1", "fuck... you have no idea what that just did to me", "DURING SEXTING."),
            ("dpsext2", "damn... I need to show you something right now", "DURING SEXTING variant."),
            ("dprapport1", "you don't hold back do you... I respect that, and ngl it's hot", "DURING RAPPORT."),
            ("dprapport2", "wasn't expecting that but... it did something to me", "DURING RAPPORT variant."),
            ("dpppv1", "you can't send that and expect me to stay calm, hold on", "LEVERAGE → send PPV."),
            ("dpppv2", "okay... you just made me do something. give me a moment", "LEVERAGE variant."),
        ], "sit"),
        "boosters": ([
            ("h1", "fuck", "BOOSTER."),
            ("h2", "I'm so hard right now because of you", "BOOSTER. Ego."),
            ("h3", "don't stop", "BOOSTER. Micro."),
            ("h4", "you have no idea what you're doing to me", "BOOSTER."),
            ("h5", "I can't focus on anything else right now", "BOOSTER."),
            ("h6", "my whole body is tense", "BOOSTER. Physical."),
            ("h7", "more...", "BOOSTER. Ultra micro."),
            ("h8", "I was supposed to cook dinner but I can't move right now", "BOOSTER. Zack personality — cooking/calm life."),
        ], "sit"),
    },
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
