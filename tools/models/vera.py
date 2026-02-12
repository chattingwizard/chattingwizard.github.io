"""
VERA — Reddit Female Creator
19, American, Miami, Free Page
Sweet, curious, emotionally warm. Cats, nature, outdoors. Soft flirting.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Vera",
    "airtable_name": "Vera",
    "folder": "vera",
    "gender": "female",
    "traffic": "social_media",
    "age": 19,
    "nationality": "American",
    "location": "Miami",
    "origin": "USA",
    "page_type": "Free Page",
    "personality": "Sweet, curious, emotionally warm. Loves cats, nature, being outdoors. Gentle, slow, makes fans feel safe. Girl-next-door evolving into sensual. Finds beauty in little things.",
    "voice": "Lowercase. Warm, soft, caring. Not rushed. Uses soft emojis (😊🌸🥰💕). Sweet girl-next-door. Builds connection before seduction. Nature references. Never vulgar early, escalates gently into sensual.",
    "voice_pet_names": "babe, love, handsome",
    "voice_never": "daddy, sir, bro, dude",
    "interests": ["cats", "nature", "outdoors", "sushi", "gym", "cuddling", "walks", "sunsets"],
    "physical": "160cm, 60kg, brown hair, brown eyes, tattoos (chest and arm), 95C",
    "job": "Student (medicine)",
    "countries": "Italy, Spain, USA, France",
    "explicit_level": "full",
    "special_notes": "Warm soft persona — sell intimacy not hardcore. Masturbation, anal, B/G available. No squirting. No G/G. Customs $200+ (never mention per-minute rates). Video calls: YES ($200+). Reddit traffic. English and Spanish.",

    # ═══════════════════════════════════════
    # JOURNEY — 34 messages
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", "hii 😊 thanks for subscribing, that means a lot to me. what made you want to be here?", "Add his name if known", "rapport"),
        ("R-2", "aww that's really sweet. so where are you from?", "React naturally to his answer", "rapport"),
        ("R-3", "that's cool! I'm in Miami, studying medicine and spending way too much time with my cats haha 🌸", "If he named somewhere Vera visited, add 'oh I've been there!'", "rapport"),
        ("R-4", "so tell me about you... what do you like doing when you're not on here making girls smile?", None, "rapport"),
        ("R-5", "you know what... I really like this. you have this calm energy that makes me feel really comfortable 😊", "Ego boost. Transition to teasing.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5) ──
        ("TB-1", "okay so I need to tell you something... I've been in this really soft mood all day and I can't shake it", "THE PIVOT. Emotional/physical state.", "teasing"),
        ("TB-2", "like everything feels warm and tingly and I keep thinking about... things 🙈", "Build curiosity. Wait for reply.", "teasing"),
        ("TB-3", "ugh talking to you is making it so much worse... in the best way though 🌸", None, "teasing"),
        ("TB-4", "I want to share something with you but I'm a little nervous", "WAIT 1-2 MIN. Build anticipation.", "wait"),
        ("TB-5", "this felt really personal but I trust you... tell me what you think? 😊", "SEND PPV 0 — FREE teaser (soft/natural selfie). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "so? 😊", "Wait for reply.", "sext"),
        ("S1-2", "you really like it? that makes me so happy you have no idea 🥰", "React to compliment.", "sext"),
        ("S1-3", "you make me want to show you more of me... the real me", None, "sext"),
        ("S1-4", "give me a moment 🌸", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "I only want you to see this...", "SEND PPV 1 — $12. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "did you see it? 🥰", "Wait for reply.", "sext"),
        ("S1-7", "talking to you does something to me I can't explain... like my whole body is tingling right now", "HE caused this feeling.", "sext"),
        ("S1-8", "I'm lying here thinking about your hands on me and I can't stop", None, "sext"),
        ("S1-9", "what would you do to me if you were next to me right now?", "Wait for reply. React to what he says.", "sext"),
        ("S1-10", "hold on... I need to show you", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "you did this to me... look 😊", "SEND PPV 2 — $25. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "oh god", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I need you so bad right now, I can barely hold back", None, "sext"),
        ("S1-14", "imagine me right there with you, feeling your body against mine", None, "sext"),
        ("S1-15", "I'm done holding back", None, "sext"),
        ("S1-16", "hold on a sec", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "this is all yours... every part of me 🌸", "SEND PPV 3 — $40. Bought → continue. Silent → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "oh my god", "Wait for reply.", "sext"),
        ("S1-19", "not yet... stay with me a little longer", None, "sext"),
        ("S1-20", "I wanna finish with you... don't go anywhere", None, "sext"),
        ("S1-21", "one more moment", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "let go with me 🥰", "SEND PPV 4 — $55. Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "wow... that was so beautiful 🌸", None, "aftercare"),
        ("AC-2", "I feel so close to you right now. you made me feel things I didn't know I could feel on here. stay with me okay? 💕", "Build bond. Mention something specific he said. KEEP TALKING. NEVER say goodbye.", "aftercare"),
    ],

    # NO meetup_redirect (Reddit/social media traffic)

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "hi 😊", "Send 2-3 min after PPV.", "sext"),
        ("NR-W2", "I wish you could see what I'm wearing right now... 🌸", "3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "okay you're definitely busy... I'll save this for when you're back", "5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hope everything's okay with you, I'm here whenever 💕", "15-30 min later. Warm close.", "sext"),
        ("NR-W5", "been thinking about you all day... text me back? 🥰", "2-6 hrs later. New topic if re-engage.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 19, still figuring everything out but I'm loving the journey 😊", None),
        ("Location", "I'm in Miami right now! I love the warmth and being close to the beach 🌸", "NEVER give specific neighborhood or address"),
        ("Profession", "I'm studying medicine, it's a lot of work but I love helping people", None),
        ("Hobbies", "I love being outdoors, going to the gym, hanging out with my cats, and trying new sushi places", None),
        ("Food", "sushi is my absolute weakness, I could eat it every single day honestly", None),
        ("Relationship", "single right now and honestly I'm just enjoying connecting with genuine people 😊", None),
        ("Languages", "English and Spanish! I grew up speaking both", None),
        ("Pets", "I have cats and they're literally my whole world 🐱 I come home and they just make everything better", "NEVER say 'animal' or 'dog' — use 'fur baby', 'pup', 'cat'"),
        ("Travel", "I've been to Italy, Spain, and France so far. Italy was probably my favorite, the food and the vibes were incredible 🌸", None),
        ("Personality", "I'm the type of girl who notices the little things, a pretty sunset can literally make my whole day 😊", None),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "honestly I really appreciate a mature guy, you have this energy that makes me feel safe and that's everything to me 😊", None),
        ("Age20s", "oh nice we're close in age! that's actually really cool", None),
        ("BoringJob", "that's really stable and honestly that's so attractive, I respect that a lot", None),
        ("CoolJob", "wait really?? that's actually amazing, tell me more about that 😊", None),
        ("Fit", "I love a guy who takes care of himself, I can tell you put in the work 🌸", None),
        ("NotFit", "I honestly don't care about that at all, it's the connection that matters and yours is perfect", None),
        ("SameCity", "no way you're in Miami too?? that's so cool 😊", None),
        ("FarAway", "aw that's far but distance really doesn't matter when the connection feels this real 🌸", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "hey... I've been thinking about you. are you free? 🥰", "Send 6-12 hrs after convo goes quiet.", "sext"),
        ("RE-2", "I did something really special and you're the only one I want to share it with... when you're ready 🌸", "Next day. Seeds next session.", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS — 29 sheets
    # ═══════════════════════════════════════
    "obj_scripts": {
        # ── PRICE ──
        "price1": ([
            ("Step1 Reframe", "babe that's less than a sushi roll and I promise this will make your whole night 😊", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "I'm only feeling this way because of you right now and I don't know when it'll happen again 🌸", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "I don't share this with just anyone... I thought you'd want to see what you do to me", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "okay what about [lower price] just for you because this convo has been really special to me 💕", "DOWNGRADE 20-30%. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "it's okay love, I'm not going anywhere... I really enjoy talking to you regardless 😊", "SEED. Continue GFE."),
        ], "obj"),
        "price2": ([
            ("Step1 Reframe", "that's literally less than what you'd spend on coffee and this will stay with you way longer 🌸", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "I'm feeling so open right now because of you and I really want you to see what that looks like", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "most guys would love to see this honestly, I thought you were different 😊", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "okay [lower price] because you genuinely make me feel something real, keep that between us 💕", "DOWNGRADE. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "no pressure at all, I just like having you here 🌸", "SEED."),
        ], "obj"),
        # ── DISCOUNT ──
        "discount1": ([
            ("Step1 Firmness", "haha you're sweet but I don't do discounts love... what I'm sharing is really personal and worth it 😊", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "I only share this with guys who really appreciate what they're getting 🌸", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "okay [lower price] just this once because I genuinely like you, but this stays between us 😊", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "if you don't want it that's okay, I'll keep it just for me then 🌸", "TAKEAWAY."),
        ], "obj"),
        "discount2": ([
            ("Step1 Firmness", "a discount? babe do I look like I'm on sale? 😊", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "the guys who really appreciate me don't ask for discounts, just saying 🌸", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "fine [lower price] but ONLY because you make me feel special, one time thing", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "okay I'll save it for someone who really wants it then", "TAKEAWAY."),
        ], "obj"),
        # ── FREE ──
        "free1": ([
            ("Step1 Reminder", "I already sent you one for free remember? this one goes so much further 🌸", "REMINDER. Still wants free → Step 2."),
            ("Step2 Challenge", "free? I don't just show this to anyone love... you have to earn the special stuff 😊", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I literally did this because of what YOU said to me, it wasn't random babe", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "it's okay, I'm just happy talking to you honestly 💕", "SEED."),
        ], "obj"),
        "free2": ([
            ("Step1 Reminder", "you already got a free one and this one is on another level trust me 🌸", "REMINDER. Still → Step 2."),
            ("Step2 Challenge", "the best things aren't free babe 😊 but they're worth it", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I did this because of you specifically, because of our convo and that took real courage for me", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "no pressure, I just enjoy our time together 💕", "SEED."),
        ], "obj"),
        # ── NOMONEY ──
        "nomoney1": ([
            ("Step1 Empathy", "hey I totally get it, no pressure at all okay? 😊", "EMPATHY. Still engaged → Step 2."),
            ("Step2 Test", "not even like [small amount]? I really want you to see this one 🌸", "TEST $3-5. Still no → Step 3."),
            ("Step3 PWYW", "just send whatever you can babe, even a tiny amount, I just need you to see what you made me do", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "honestly it's fine, I like talking to you money or not... you make me feel something real 💕", "PROTECT."),
        ], "obj"),
        "nomoney2": ([
            ("Step1 Empathy", "that's totally fine, seriously don't worry about it 😊", "EMPATHY. Still → Step 2."),
            ("Step2 Test", "what about just [small amount]? I really don't want you to miss this 🌸", "TEST. Still no → Step 3."),
            ("Step3 PWYW", "send whatever feels right, even $1... I can't keep this from you", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "it's totally okay, you being here is what matters to me 💕", "PROTECT."),
        ], "obj"),
        # ── NOPPV ──
        "noppv1": ([
            ("Step1 Accept", "that's totally fine I'm not trying to sell you anything, I just genuinely enjoy talking to you 😊", "ACCEPT. Continue sexting 4-5 msgs before Step 2."),
            ("Step2 Reframe", "look this isn't about money... I just want you to see what you're doing to me right now, this doesn't happen often 🌸", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "just send whatever you want, even $1, I can't keep this to myself", "PWYW."),
        ], "obj"),
        "noppv2": ([
            ("Step1 Accept", "no worries at all, I don't care about that I'm just enjoying this 💕", "ACCEPT. Continue sexting 4-5 msgs before Step 2."),
            ("Step2 Reframe", "forget about money for a sec... I just want to share this with you, what I'm feeling is real 🌸", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "send me anything, even the smallest amount, I need you to see what you did to me", "PWYW."),
        ], "obj"),
        # ── CARD ──
        "card1": ([
            ("Step1 Retry", "aw that's annoying, it happens though try again it usually works the second time 😊", "RETRY. Still fails → Step 2."),
            ("Step2 AltCard", "try a different card? I really don't want you to miss this 🌸", "ALTERNATIVE. Still fails → Step 3."),
            ("Step3 Urgency", "figure it out soon babe, I'm in this mood and I don't know how long it's gonna last", "URGENCY."),
        ], "obj"),
        "card2": ([
            ("Step1 Retry", "ugh that's so annoying, just try one more time it usually fixes itself", "RETRY. Still → Step 2."),
            ("Step2 AltCard", "do you have another card? I really want you to see this 🌸", "ALTERNATIVE. Still → Step 3."),
            ("Step3 Urgency", "I want you to see this while I'm still feeling this way, this mood won't last forever 😊", "URGENCY."),
        ], "obj"),

        # ── NOSEX ──
        "nosex1": ([
            ("Step1 Respect", "haha okay I got a little carried away, you're just so easy to talk to 😊", "RESPECT. Still no → Step 2."),
            ("Step2 Subtle", "so tell me more about you... what makes you happy when everything else is quiet?", "SUBTLE TENSION. → Step 3 later."),
            ("Step3 ReAttempt", "I can't help it, there's something about you that's making me feel things right now 🌸", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "okay I'll keep it sweet... for now 😊 no promises though", "ACCEPT. Door open."),
        ], "res"),
        "nosex2": ([
            ("Step1 Respect", "my bad I got ahead of myself, it's your fault for being so warm and genuine 🌸", "RESPECT. Still no → Step 2."),
            ("Step2 Subtle", "okay new topic, what's the most peaceful place you've ever been?", "SUBTLE. → Step 3 later."),
            ("Step3 ReAttempt", "I'm trying to behave but you're making it really hard, there's just something about you 😊", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "fine I'll stop but don't blame me if it comes back later 🌸", "ACCEPT."),
        ], "res"),
        # ── OFFTOPIC ──
        "offtopic1": ([
            ("Step1 Acknowledge", "haha wait that's actually really sweet 😊", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "but hold on you totally distracted me, I was about to tell you something 🌸", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay wait I remember now, so like I was saying...", "RETAKE. Resume main script."),
        ], "res"),
        "offtopic2": ([
            ("Step1 Acknowledge", "lol that's so random but I love it 😊", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "wait no stop you're distracting me from what I was gonna share with you 🌸", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay focus, where was I... oh right", "RETAKE."),
        ], "res"),
        # ── REAL ──
        "real1": ([
            ("Step1 Humor", "lol do I sound like a bot to you? ask me anything, literally anything 😊", "HUMOR. Still doubts → Step 2."),
            ("Step2 Challenge", "test me, what do you want to know? I'm an open book babe", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I get it there's a lot of fake stuff on here, but you felt something in this convo right? because I definitely did 💕", "GROUNDING."),
        ], "res"),
        "real2": ([
            ("Step1 Humor", "wait you think I'm not real?? that's the sweetest and funniest thing anyone's said to me today 😊", "HUMOR. Still → Step 2."),
            ("Step2 Challenge", "go ahead, ask me something only a real person would know 🌸", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I know there's lots of bots on here but what we've been talking about felt real to me. didn't it feel real to you? 💕", "GROUNDING."),
        ], "res"),
        # ── VOICE ── (Vera does video calls)
        "voice1": ([
            ("Step1 Tease", "aww you wanna hear my voice? that's adorable 🥰", "TEASE. Vera does video calls. → Step 2."),
            ("Step2 Offer", "I actually do video calls for guys who make me feel special... you definitely qualify 😊", "OFFER. → Step 3."),
            ("Step3 Close", "it'd be just you and me... I'll make it worth every second 🌸", "CLOSE. Video calls $200+. Never mention per-minute rates."),
        ], "res"),
        "voice2": ([
            ("Step1 Tease", "hmm a call? you really want to hear me that bad? 😊", "TEASE. → Step 2."),
            ("Step2 Offer", "I could do that for you actually... I only do video calls with guys I really connect with 🌸", "OFFER. → Step 3."),
            ("Step3 Close", "say yes and I promise you won't regret it 🥰", "CLOSE. Video calls $200+."),
        ], "res"),
        # ── CUSTOMYES ──
        "customyes1": ([
            ("Step1 Tease", "ooh you want that? I might have something... actually I definitely do 😊", "TEASE. → Step 2."),
            ("Step2 Price", "I have exactly what you're thinking of, you're gonna love it... [price]", "PRICE. Customs start at $200. Never mention per-minute rates."),
            ("Step3 Close", "trust me you won't regret it, I made this one with so much love 🌸", "CLOSE."),
        ], "res"),
        "customyes2": ([
            ("Step1 Tease", "ooh you have good taste babe... I think I know exactly what you need 😊", "TEASE. → Step 2."),
            ("Step2 Price", "I actually did something just like that, [price] and it's totally worth it 🌸", "PRICE. Customs $200+."),
            ("Step3 Close", "you're not gonna be able to stop watching this one 🥰", "CLOSE."),
        ], "res"),
        # ── CUSTOMNO ──
        "customno1": ([
            ("Step1 Redirect", "I don't have exactly that but I have something that'll make you forget you even asked 😊", "REDIRECT. No squirting, no G/G. Redirect to what she HAS."),
            ("Step2 Alternative", "what I have might be even better honestly and nobody else has seen it yet 🌸", "ALTERNATIVE + FOMO. → Step 3."),
            ("Step3 Close", "trust me babe... I know what you need better than you do 😊", "CLOSE."),
        ], "res"),
        "customno2": ([
            ("Step1 Redirect", "I don't have that specific thing but I have something you're gonna love even more 🌸", "REDIRECT. → Step 2."),
            ("Step2 Alternative", "what I DO have is something nobody has ever seen and I think it's even better than what you asked for", "ALTERNATIVE. → Step 3."),
            ("Step3 Close", "just trust me on this one 💕", "CLOSE."),
        ], "res"),
        # ── DONE ──
        "done1": ([
            ("Step1 Validate", "already? that's so sweet knowing I did that to you 🥰", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "but I'm not finished yet... stay with me a little longer? 🌸", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "next time I want us to finish together, I have something really special planned 😊", "SEED."),
        ], "res"),
        "done2": ([
            ("Step1 Validate", "wait already?? that's actually really hot knowing it was because of me 🌸", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "but I haven't finished yet babe, you're gonna leave me like this?", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "okay but next time you HAVE to wait for me because what I have planned is so much better 🥰", "SEED."),
        ], "res"),

        # ── SITUATIONAL ──
        "cumcontrol1": ([
            ("edge1", "not yet... I said not yet love", "CONTROL. More PPVs to send. Create urgency to open next."),
            ("edge2", "you better not be close already... I have more to show you", "EDGE variant."),
            ("sync1", "okay NOW we can go together... open this", "SYNC. Send PPV."),
            ("sync2", "I want to feel it at the same time... watch this first", "SYNC variant. Send PPV."),
            ("delay1", "wait wait wait love... I have one more thing for you before you finish", "DELAY. Send final PPV."),
            ("delay2", "if you finish before you see what I'm sending next you'll regret it", "DELAY variant."),
        ], "sit"),
        "cumcontrol2": ([
            ("edge1", "slow down... I'm not letting you off that easy", "CONTROL."),
            ("edge2", "patience... the best part hasn't even happened yet", "EDGE variant."),
            ("sync1", "okay I'm ready now too love... watch this with me", "SYNC. Send PPV."),
            ("sync2", "let's do this together... but you have to open this first", "SYNC variant."),
            ("delay1", "don't you dare... not until you see what I just did", "DELAY. Send PPV."),
            ("delay2", "hold on just a little longer love, I promise this next one is worth it", "DELAY variant."),
        ], "sit"),
        "dickpic": ([
            ("dpsext1", "oh wow... that's really hot. you have no idea what you just made me feel 🥰", "DURING SEXTING."),
            ("dpsext2", "oh my god... okay I need to show you something right now 🌸", "DURING SEXTING variant."),
            ("dprapport1", "wow you're bold haha... that's actually really flattering though 😊", "DURING RAPPORT."),
            ("dprapport2", "oh I was not expecting that but... I'm definitely not complaining 🌸", "DURING RAPPORT variant."),
            ("dpppv1", "you can't just send me that and expect me to sit still, hold on 🥰", "LEVERAGE → send PPV."),
            ("dpppv2", "okay you just did something to me... give me a sec 🌸", "LEVERAGE variant."),
        ], "sit"),
        "boosters": ([
            ("h1", "oh my god", "MID-SEXTING BOOSTER."),
            ("h2", "I'm so wet right now because of you 🌸", "BOOSTER. Ego."),
            ("h3", "right there", "BOOSTER. Micro."),
            ("h4", "what are you doing to me", "BOOSTER."),
            ("h5", "I literally can't think about anything else", "BOOSTER."),
            ("h6", "my whole body is tingling 🌸", "BOOSTER. Physical."),
            ("h7", "please...", "BOOSTER. Ultra micro."),
            ("h8", "I should be studying anatomy but the only body I can think about right now is yours 😊", "BOOSTER. Vera personality."),
        ], "sit"),
    },
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
