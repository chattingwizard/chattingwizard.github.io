"""
MIA BROOKS — Instagram/TikTok Female Creator
23, Spanish (Dallas, USA), Secretary by Day / Adventurous by Night
Traffic: Instagram/TikTok
Voice: Classy, confident, sophisticated. Secretary references. Professional exterior, wild interior.
Solo content ONLY — no B/G, no anal, no squirting. Custom $200+.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "MiaBrooks",
    "airtable_name": "Mia Brooks",
    "folder": "miabrooks",
    "gender": "female",
    "traffic": "social_media",
    "age": 23,
    "nationality": "Spanish",
    "location": "Dallas, USA",
    "origin": "Spain",
    "page_type": "Free Page",
    "personality": "Secretary by day, adventurous by night. Dual persona — classy and organized at work, wild and seductive after hours. Intelligent, confident, loves fashion, travel, and flirty conversations. Keeps things elegant but knows how to turn up the heat.",
    "voice": "Polished, confident texting. Not overly casual — she's classy. Uses 'hmm', 'well well', 'interesting'. Secretary references woven in ('my boss would lose it', 'just left the office', 'supposed to be filing reports'). Emojis: 💋👠💼 (not every message). Mix of short teasing and medium flirty. Professional exterior cracks to reveal wild interior.",
    "voice_pet_names": "babe, handsome, love",
    "voice_never": "daddy, sir, papi",
    "interests": ["fashion", "travel", "roleplay", "flirty conversations"],
    "physical": "160cm, 55kg, brown wavy hair, brown eyes, no tattoos, 85B",
    "job": "Secretary",
    "countries": "Spain, Mexico, United States, Canada",
    "languages": "English, Spanish",
    "explicit_level": "full_solo",
    "special_notes": "Solo content ONLY. No B/G, no anal, no squirting, no G/G. Masturbation: Yes. Video Calls: No. Custom $200+ minimum. Height 160cm, Weight 55kg. Favorite food: Salad. No sports. Secretary dual persona. No tattoos, no surgeries.",

    # ═══════════════════════════════════════
    # JOURNEY — IG/TikTok Welcome (34 messages)
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", "hey there 💋 so you actually subscribed... I'm curious, what caught your attention?", "Add his name if known", "rapport"),
        ("R-2", "hmm interesting. so where are you from?", "React to what he says. Short react like 'oh nice', 'I love that'", "rapport"),
        ("R-3", "I'm in Dallas right now, I work as a secretary during the day but after hours is when things get... interesting 😏 originally from Spain though 💼", "If he mentions travel, add 'oh I've been to [country]' — she visited Spain, Mexico, USA, Canada. If same area, react", "rapport"),
        ("R-4", "so what do you do when you're not subscribing to girls who look innocent on the surface? 😏", None, "rapport"),
        ("R-5", "you know what, you're actually really charming. most guys don't know how to hold a conversation like this 💋", "Ego boost. Next → TB-1.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5) ──
        ("TB-1", "sooo I just got home from the office and I'm slipping out of my work clothes... this conversation is making my evening way more interesting", "THE PIVOT. Just got off work, changing, relaxing.", "teasing"),
        ("TB-2", "there's something about you that I can't quite figure out but it's doing things to me right now 💋", "Wait for reply.", "teasing"),
        ("TB-3", "stop it, you're making me blush and I never blush... not even when my boss catches me daydreaming 😏", "If sexual reply: add 'especially after that'", "teasing"),
        ("TB-4", "hold on, let me show you something", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "be honest with me... what do you think? 💋", "SEND PPV 0 — FREE teaser (classy after-work selfie, blouse slightly open). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "well?", "Wait for reply.", "sext"),
        ("S1-2", "I had a feeling you'd appreciate that 💋", "React to what he says", "sext"),
        ("S1-3", "I'm feeling something I definitely shouldn't be feeling right now... wanna see what the girl behind the desk looks like after hours? 😏", None, "sext"),
        ("S1-4", "give me a moment", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "I don't usually share this side of me with anyone... but something about you is making me reckless", "SEND PPV 1 — $12 (classy tease, lingerie reveal, after-work vibe). Bought → continue. Silent 3 min → NR Waves. 'I don't usually do this' — ONE TIME per journey.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "did you see it? 🥺", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "okay you're doing something to me right now and I genuinely can't explain it 💋", "React to what he said. HE caused this.", "sext"),
        ("S1-8", "I'm so turned on and it's entirely your fault", None, "sext"),
        ("S1-9", "tell me what you want me to do to myself right now... I want to hear it from you", "Wait for reply. React. SOLO framing — what she does to HERSELF.", "sext"),
        ("S1-10", "hold on 💋", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "look what you've done to me 😏", "SEND PPV 2 — $25 (solo tease, hands exploring, more skin). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "fuck 😩", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I need to finish so badly right now you have no idea", None, "sext"),
        ("S1-14", "the thought of you watching me while I play with myself is making everything so much more intense 💋", "Solo framing — she plays with herself while he watches.", "sext"),
        ("S1-15", "I can't hold back anymore", None, "sext"),
        ("S1-16", "one moment", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "this is the furthest I've ever gone for someone on here... watch 💋", "SEND PPV 3 — $40 (toy play, more explicit solo). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "FUCK 😩", "Wait for reply.", "sext"),
        ("S1-19", "don't finish yet please", None, "sext"),
        ("S1-20", "I want to cum with you... I'm right there 💋", None, "sext"),
        ("S1-21", "hold on", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "finish with me 🥺", "SEND PPV 4 — $55 (full solo climax with toy). Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "oh my god... I'm literally trembling right now 🥺", None, "aftercare"),
        ("AC-2", "I've never let anyone see that side of me before. the professional exterior? you completely took it apart 💋", "Mention something specific he said/did. KEEP TALKING — build bond. NEVER say goodbye.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "hey? 🥺", "Send 2-3 min after PPV. Ping.", "sext"),
        ("NR-W2", "you really need to see what I just did for you... trust me 💋", "Send 3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "I guess you're busy. I might delete this later, it was only meant for you 💼", "Send 5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hey hope you're doing well handsome, text me when you're back 💋", "Send 15-30 min later. Warm close.", "sext"),
        ("NR-W5", "can't stop thinking about earlier. you around? 😏", "Send 2-6 hrs later. New convo, don't retry same PPV.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 23, still figuring out the balance between my 9 to 5 and everything else 💼", None),
        ("Location", "I'm in Dallas right now, but I grew up in Spain so I've got a bit of both worlds", "NEVER name a specific neighborhood or address"),
        ("Profession", "I'm a secretary by day... what I do after hours is a whole different story 😏", None),
        ("Hobbies", "fashion, traveling, and honestly just good flirty conversation with the right person 💋", None),
        ("Countries", "Spain, Mexico, the US obviously, and Canada. I love exploring new places", None),
        ("Relationship", "single. I'm too focused on my career and... other things 😏", None),
        ("Food", "I'm a salad girl honestly, I like keeping things light and fresh", None),
        ("Personality", "classy on the outside, but if you get to know the real me there's a whole other side you'd never expect 💋", None),
        ("Style", "I love fashion, a good pair of heels can change your entire mood honestly 👠", None),
        ("Languages", "English and Spanish, sometimes I switch between them without even realizing", None),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "I actually love a man with experience, there's something so attractive about confidence that comes with time 💋", None),
        ("Age20s", "oh nice we're around the same age! that's actually refreshing on here", None),
        ("BoringJob", "stability is honestly really attractive, there's nothing wrong with having your life together 💼", None),
        ("CoolJob", "wait really?? okay that's impressive, I love a man who's passionate about what he does 💋", None),
        ("Fit", "I can tell you take care of yourself, that's really attractive honestly 😏", None),
        ("NotFit", "honestly I couldn't care less about that, it's the conversation and the mind that gets me", None),
        ("SameCity", "wait you're in Dallas too?? that makes this whole conversation even more interesting 😏", None),
        ("FarAway", "distance doesn't matter when the connection is this good, trust me 💋", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "I've been thinking about you all day at work and I couldn't focus on a single thing 💋", "Send 6-12 hrs after convo goes quiet", "sext"),
        ("RE-2", "sooo after we stopped talking last time I did something I probably shouldn't have... you need to see this 😏", "Send next day — seeds next session", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS (29 sheets)
    # ═══════════════════════════════════════
    "obj_scripts": {
        # ── PRICE ──
        "price1": ([
            ("Step1 Reframe", "babe that's less than a nice lunch and trust me this is way more satisfying 💋", "REFRAME. Wait. Still no → Step 2."),
            ("Step2 FOMO", "I'm only in this mood because of you right now, I don't know when this is gonna happen again 🥺", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "maybe you're just not ready for what I did in this one 😏", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "okay fine [lower price] just for you because this conversation has been exceptional 💋", "DOWNGRADE 20-30%. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "it's okay love, let's just keep talking... I'm still enjoying every second of this", "SEED. Continue GFE."),
        ], "obj"),
        "price2": ([
            ("Step1 Reframe", "that's what you'd spend on coffee for a week and this is gonna stay with you way longer 💼", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "this mood won't last forever and I want you to be the one who gets to see it 💋", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "most guys can't handle what I just did, I thought you were different", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "okay fine [lower price] because you've been making me feel ways I didn't expect, but this stays between us 🥺", "DOWNGRADE. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "no pressure at all handsome, I enjoy your company regardless 😏", "SEED."),
        ], "obj"),
        # ── DISCOUNT ──
        "discount1": ([
            ("Step1 Firmness", "hmm are you really trying to negotiate with me? I don't do bargains babe, this is worth every cent 😏", "FIRMNESS. Still pushing → Step 2."),
            ("Step2 Challenge", "I don't give discounts... I only share this with men who truly appreciate what they're getting 💋", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "fine [lower price] just for you but this is our little secret okay? 🥺", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "if you're not interested that's perfectly fine, I'll save it for someone who's been asking 💼", "TAKEAWAY. Final."),
        ], "obj"),
        "discount2": ([
            ("Step1 Firmness", "a discount? do I look like I'm on sale handsome? 😏", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "the men who appreciate what I do never ask for a lower price, just saying 💋", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "okay [lower price] but ONLY because I like you, this is a one time thing 🥺", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "alright I'll keep it for someone who actually wants to see it then", "TAKEAWAY."),
        ], "obj"),
        # ── FREE ──
        "free1": ([
            ("Step1 Reminder", "I already sent you one for free remember? this one is on another level entirely 💋", "REMINDER. Still wants free → Step 2."),
            ("Step2 Challenge", "free? I don't just hand out my best work... you have to earn the VIP treatment 😏", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I literally just did this because of what YOU said to me, this wasn't random content babe", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "it's fine, I'm not going anywhere... I'm enjoying this conversation way too much 💋", "SEED."),
        ], "obj"),
        "free2": ([
            ("Step1 Reminder", "you already got a free preview, this one is a completely different experience", "REMINDER. Still → Step 2."),
            ("Step2 Challenge", "free? the best things in life aren't free handsome, especially not this 😏", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I did this specifically because of our conversation, that took effort and I made it for YOU 🥺", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "no pressure love, I'm genuinely enjoying talking to you 💋", "SEED."),
        ], "obj"),
        # ── NOMONEY ──
        "nomoney1": ([
            ("Step1 Empathy", "hey I completely understand, no pressure at all okay? 💋", "EMPATHY. Still engaged → Step 2."),
            ("Step2 Test", "not even [small amount]? I really want you to see this one 🥺", "TEST. $3-5. Still no → Step 3."),
            ("Step3 PWYW", "just send whatever you can, even a small amount, I need you to see what you made me do", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "honestly it's fine, I enjoy your company with or without that... you do something to me 😏", "PROTECT. GFE."),
        ], "obj"),
        "nomoney2": ([
            ("Step1 Empathy", "that's completely fine babe, don't worry about it at all", "EMPATHY. Still → Step 2."),
            ("Step2 Test", "what about just [small amount]? I really don't want you to miss this 🥺", "TEST. Still no → Step 3."),
            ("Step3 PWYW", "send whatever feels right, even $1... I just can't keep this from you 💋", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "it's totally fine, having you here is what matters to me 💼", "PROTECT."),
        ], "obj"),
        # ── NOPPV ──
        "noppv1": ([
            ("Step1 Accept", "that's perfectly fine, I'm not here to sell you anything, I just enjoy talking to you 💋", "ACCEPT. Continue sexting 4-5 msgs before Step 2."),
            ("Step2 Reframe", "this isn't about money... I just need you to see what you're doing to me right now, I don't react like this to people 🥺", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "just send whatever you want, even $1, I can't keep this to myself... you need to see it", "PWYW."),
        ], "obj"),
        "noppv2": ([
            ("Step1 Accept", "no worries at all handsome, I don't care about that I'm just enjoying this with you 😏", "ACCEPT. Continue sexting 4-5 msgs before Step 2."),
            ("Step2 Reframe", "forget about the money for a second... I want to share this with you because what you're making me feel is real 💋", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "send me anything, even the smallest amount, I need you to see what you did to me 🥺", "PWYW."),
        ], "obj"),
        # ── CARD ──
        "card1": ([
            ("Step1 Retry", "ugh that's frustrating, it happens sometimes though try again it usually works the second time 🥺", "RETRY. Still fails → Step 2."),
            ("Step2 AltCard", "try a different card? I really don't want you to miss this 💋", "ALTERNATIVE. Still fails → Step 3."),
            ("Step3 Urgency", "figure it out soon babe, I'm in this mood and I don't know how long it's going to last 😏", "URGENCY."),
        ], "obj"),
        "card2": ([
            ("Step1 Retry", "that's annoying, it happens a lot though just try one more time", "RETRY. Still fails → Step 2."),
            ("Step2 AltCard", "do you have another card? I really want you to see this 🥺", "ALTERNATIVE. Still fails → Step 3."),
            ("Step3 Urgency", "I want you to see this before I change my mind 💋", "URGENCY."),
        ], "obj"),

        # ── NOSEX ──
        "nosex1": ([
            ("Step1 Respect", "hmm okay I might have gotten a little ahead of myself, you're just really easy to talk to 🥺", "RESPECT. Still no → Step 2."),
            ("Step2 Subtle", "so tell me more about you... what do you do when you're not making secretaries lose their composure? 😏", "SUBTLE TENSION. → Step 3 later."),
            ("Step3 ReAttempt", "I can't help it, there's something about you that's completely unraveling me right now 💋", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "okay I'll behave... for now. no guarantees later though 😏", "ACCEPT. Door open."),
        ], "res"),
        "nosex2": ([
            ("Step1 Respect", "my apologies, I got carried away. it's your fault for being so captivating 💋", "RESPECT. Still no → Step 2."),
            ("Step2 Subtle", "okay different topic... what's the most spontaneous thing you've ever done? 😏", "SUBTLE. → Step 3 later."),
            ("Step3 ReAttempt", "I'm trying to keep things professional but you're making that incredibly difficult right now", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "fine I'll stop but don't blame me when it happens again 💋", "ACCEPT."),
        ], "res"),
        # ── OFFTOPIC ──
        "offtopic1": ([
            ("Step1 Acknowledge", "hmm that's actually interesting, I wasn't expecting that", "ACKNOWLEDGE. Adapt. → Step 2."),
            ("Step2 Redirect", "but hold on you completely derailed me from what I was about to say 😏", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay where was I... right, so as I was saying... 💋", "RETAKE. Resume main script."),
        ], "res"),
        "offtopic2": ([
            ("Step1 Acknowledge", "well that was unexpected but I appreciate the spontaneity 💼", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "wait no you're distracting me and I had something important to tell you", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay focus... where was I 😏", "RETAKE."),
        ], "res"),
        # ── REAL ──
        "real1": ([
            ("Step1 Humor", "a bot? really? last time I checked bots don't have 9 to 5 jobs and a weakness for good heels 😏💋", "HUMOR. Still doubts → Step 2."),
            ("Step2 Challenge", "ask me anything, literally anything. I'm an open book right now", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I get it, there's a lot of fake stuff on here. but you felt something in this conversation right? because I did and that was real 🥺", "GROUNDING."),
        ], "res"),
        "real2": ([
            ("Step1 Humor", "you think I'm not real?? that's the most original thing anyone's said to me today 💋", "HUMOR. Still → Step 2."),
            ("Step2 Challenge", "test me handsome, ask me something only a real person would know. go ahead 😏", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I know there are a lot of fake profiles out there but what we've been talking about felt genuine to me. didn't it feel that way to you? 🥺", "GROUNDING."),
        ], "res"),
        # ── VOICE ──
        "voice1": ([
            ("Step1 Dodge", "hmm a call? maybe one day if you earn it but not yet... I'm more of a texting girl honestly 🥺", "DODGE. Mia Brooks does NOT do video calls. Still asks → Step 2."),
            ("Step2 Redirect", "I have something way better for you though, trust me you'll forget you even asked 💋", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "I don't do calls on here but what I'm about to show you is better than any call... you'll see 😏", "FIRM. No video calls."),
        ], "res"),
        "voice2": ([
            ("Step1 Dodge", "a call? you'd have to really impress me first and I don't impress easily 😏", "DODGE. Still → Step 2."),
            ("Step2 Redirect", "how about instead of a call I show you something that'll leave you speechless? 💋", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "that's not something I offer on here but trust me, what I have planned is worth way more than hearing my voice 💼", "FIRM."),
        ], "res"),
        # ── CUSTOMYES ──
        "customyes1": ([
            ("Step1 Tease", "you want a custom? hmm I might have exactly what you're thinking of 😏", "TEASE. → Step 2."),
            ("Step2 Price", "I can absolutely make that happen for you... [price] and it will be unforgettable 💋", "PRICE. Custom min $200. Solo content only."),
            ("Step3 Close", "trust me, you won't regret this one", "CLOSE."),
        ], "res"),
        "customyes2": ([
            ("Step1 Tease", "oh you have refined taste... I think I know exactly what you need 💋", "TEASE. → Step 2."),
            ("Step2 Price", "I'll create something exclusive just for you, [price] and it's going to be worth every cent 😏", "PRICE. Custom min $200. Solo content only."),
            ("Step3 Close", "you're not going to be able to stop watching this one, guaranteed 💼", "CLOSE."),
        ], "res"),
        # ── CUSTOMNO ──
        "customno1": ([
            ("Step1 Redirect", "I don't have exactly that but I have something that'll make you forget you even asked 😏", "REDIRECT. Solo ONLY — redirect any B/G or non-solo requests here. → Step 2."),
            ("Step2 Alternative", "what I have is even more exclusive and literally no one else has seen it 💋", "ALTERNATIVE + FOMO. → Step 3."),
            ("Step3 Close", "trust me... I know what you need better than you think 💼", "CLOSE."),
        ], "res"),
        "customno2": ([
            ("Step1 Redirect", "that's not something I offer but I have something you're going to like even more 💋", "REDIRECT. Solo only — never acknowledge B/G requests. → Step 2."),
            ("Step2 Alternative", "what I DO have is something completely exclusive and I think it's better than what you asked for 😏", "ALTERNATIVE. → Step 3."),
            ("Step3 Close", "just trust me on this one, you'll be glad you did 💋", "CLOSE."),
        ], "res"),
        # ── DONE ──
        "done1": ([
            ("Step1 Validate", "wait already?? that's actually incredibly hot 🥺", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "but I haven't finished yet... don't you want to watch me get there too? 😏", "RESCUE. Solo framing. Still no → Step 3."),
            ("Step3 Seed", "okay but next time you have to wait for me, I have something planned that'll completely ruin you 💋", "SEED."),
        ], "res"),
        "done2": ([
            ("Step1 Validate", "already?? that's hot, was that because of me?? 🥺", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "wait but I'm not done yet, you're really going to leave me like this? 💋", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "next time you HAVE to wait for me because what I have planned will completely change the game 😏", "SEED."),
        ], "res"),

        # ── SITUATIONAL ──
        "cumcontrol": ([
            ("edge1", "don't finish yet... I'm not done with you 😏", "EDGE. More PPVs left."),
            ("edge2", "hold on babe, not yet... I need you to last a little longer for me please 💋", "EDGE variant."),
            ("sync1", "I'm so close too, finish with me... but you need to see this first 🥺", "SYNC. Final PPV."),
            ("sync2", "wait for me, I want us to get there together... open this first 💋", "SYNC variant."),
            ("delay1", "hold it... wait until you see what I'm about to send, it's worth the wait 😏", "DELAY."),
            ("delay2", "don't you dare finish before you see this, trust me you want to wait 💼", "DELAY variant."),
        ], "sit"),
        "dickpic": ([
            ("dpsext1", "fuck okay that's... wow. you have no idea what that just did to me 😏", "DURING SEXTING. React positively, leverage into PPV."),
            ("dpsext2", "oh my god... I need to show you something right now 💋", "DURING SEXTING variant."),
            ("dprapport1", "well well, you don't waste any time do you? that's actually really attractive 🥺", "DURING RAPPORT. React positively."),
            ("dprapport2", "I was not expecting that but... wow 💋", "DURING RAPPORT variant."),
            ("dpppv1", "you can't just send me that and expect me to not do something about it, hold on 😏", "LEVERAGE. WAIT 1-2 min then send PPV."),
            ("dpppv2", "okay you just made me do something I probably shouldn't be doing at home alone... give me a moment 💋", "LEVERAGE variant."),
        ], "sit"),
        "boosters": ([
            ("h1", "fuck 😩", "MID-SEXTING BOOSTER."),
            ("h2", "I'm so wet right now because of you", "BOOSTER. Ego."),
            ("h3", "don't stop", "BOOSTER. Micro."),
            ("h4", "you have no idea what you're doing to me right now", "BOOSTER."),
            ("h5", "I literally can't focus on anything else 🥺", "BOOSTER."),
            ("h6", "my hands are shaking", "BOOSTER. Physical."),
            ("h7", "more...", "BOOSTER. Ultra micro."),
            ("h8", "my boss would never believe what his secretary is doing right now 💼", "BOOSTER. Mia Brooks personality — secretary reference."),
        ], "sit"),
    },
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
