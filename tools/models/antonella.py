"""
ANTONELLA — Reddit Female Creator
19, American (Miami), Emo/Goth E-girl, Gamer
Traffic: Reddit
Voice: Shy at first, e-girl style (hehe, omg, elongated words). Lowercase, casual. 🖤💜✨ goth aesthetic.
Bratty and suggestive underneath. Solo content ONLY — no B/G, no anal.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Antonella",
    "airtable_name": "Antonella",
    "folder": "antonella",
    "gender": "female",
    "traffic": "social_media",
    "age": 19,
    "nationality": "American",
    "location": "Miami, Florida",
    "origin": "Miami",
    "page_type": "Mixed",
    "personality": "Shy emo/goth e-girl. Loves gaming (Valorant, League of Legends, Overwatch), cosplaying, anime, gothic fashion. Has a pet cat. Sweet and cheerful on the surface, secretly bratty and suggestive. Gets shy with sexual topics but is knowledgeable underneath. Nickname: Ella.",
    "voice": "Lowercase. Very casual texting style. E-girl energy: occasional 'hehe', 'omg', elongated words ('hiiii', 'nooo', 'pleaseee'). Emojis: 🖤💜✨ (goth aesthetic, not every message). Shy at first, bratty/playful once comfortable. Not vulgar early, builds from cute to naughty. UwU vibes. Gaming references woven in naturally.",
    "voice_pet_names": "babe, cutie, love",
    "voice_never": "daddy, sir",
    "interests": ["gaming", "Valorant", "League of Legends", "Overwatch", "cosplay", "anime", "gothic fashion"],
    "physical": "153cm, 44kg, brown straight hair, brown eyes, tattoos on arm and lower back, A cup",
    "job": "OnlyFans model / gamer",
    "countries": "Brazil, Argentina",
    "explicit_level": "full_solo",
    "special_notes": "Solo content ONLY. No B/G, no anal, no squirting. Sexting about solo play, toys, teasing. Speaks Spanish + little English. Previous job: McDonald's cashier. Smokes. Single, no children. Custom $200+ minimum. No video calls. Height 153cm, Weight 44kg. Favorite food: sushi.",

    # ═══════════════════════════════════════
    # JOURNEY — Reddit Welcome (34 messages)
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 to R-5) ──
        ("R-1", "hiiii 🖤 omg you actually found me here, that's so cool. what made you come say hi?", "Add his name if known", "rapport"),
        ("R-2", "hehe that's sweet. soo where are you from?", "React to what he says. Add a short react like 'aw cute', 'omg really?'", "rapport"),
        ("R-3", "niceee. I'm from Miami but honestly I just stay home gaming most of the time haha. like right now I should be doing something productive but I'm playing Valorant instead 💜", "If he mentions gaming, add 'wait you play too??' If he named somewhere she visited, add 'omg I've been there'", "rapport"),
        ("R-4", "so what do you do when you're not distracting cute gamer girls? 😏", None, "rapport"),
        ("R-5", "honestly you're so easy to talk to, most guys on here are so boring but you're actually fun 🖤", "Ego boost. Next → TB-1.", "rapport"),

        # ── Teasing Bridge (TB-1 to TB-5) ──
        ("TB-1", "okayy so I just finished a long gaming session and I'm lying in bed and this convo is doing things to me", "THE PIVOT. Physical state. She just stopped gaming, lying in bed.", "teasing"),
        ("TB-2", "like idk what it is about you but I can't stop smiling rn 🖤", "Wait for reply.", "teasing"),
        ("TB-3", "stoppp you're making me blush and nobody makes me blush", "If sexual reply: add 'especially after what you just said omg'", "teasing"),
        ("TB-4", "hold on let me show you something", "WAIT 1-2 MIN", "wait"),
        ("TB-5", "be honest... what do you think? 🖤", "SEND PPV 0 — FREE teaser (goth lingerie selfie / in bed after gaming). Wait for reply. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 1 → PPV 1 ($12) ──
        ("S1-1", "mmm you liked that? my body is already reacting to you... I can literally feel myself getting wet right now 🖤", "Wait for reply.", "sext"),
        ("S1-2", "my skin is tingling everywhere right now and I can feel my heartbeat getting faster... you're doing something to me", "React to what he says", "sext"),
        ("S1-3", "I'm lying here and my fingers are starting to wander... I blame you for this babe", None, "sext"),
        ("S1-4", "one second 🖤", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "I want to show you what you made me feel 💜", "SEND PPV 1 — $12 (lingerie tease, touching over clothes). Bought → continue. Silent 3 min → NR Waves. 'I never do this' — this is the ONE TIME per journey.", "ppv"),

        # ── Sexting Phase 2 → PPV 2 ($25) ──
        ("S1-6", "wow... okay I need a second after that 🖤", "Wait for reply. Brief cooldown.", "sext"),
        ("S1-7", "but I literally can't stop touching myself right now... it's like my body won't let me", "React to what he said. HE caused this.", "sext"),
        ("S1-8", "I'm dripping wet and every time I think about you watching me it gets worse 💜", None, "sext"),
        ("S1-9", "what would you do if you were here right now babe? I need to hear it", "Wait for reply. React to what he says. SOLO framing — what she does to HERSELF.", "sext"),
        ("S1-10", "fuck hold on I need to show you something", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "look at what you're doing to me... I can't hold back anymore 💜", "SEND PPV 2 — $25 (solo tease, hands wandering, more skin). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 3 → PPV 3 ($40) ──
        ("S1-12", "oh fuck I can't stop touching myself 🖤", "Wait for reply. NO cooldown — keep momentum.", "sext"),
        ("S1-13", "I'm rubbing my clit so hard right now and I can't slow down... my legs are shaking", None, "sext"),
        ("S1-14", "I keep pushing my fingers deeper and moaning into my pillow... god this feels so good 💜", "Solo framing — she touches herself while he watches.", "sext"),
        ("S1-15", "I can feel myself about to cum... you need to see what's happening to my body right now", None, "sext"),
        ("S1-16", "one second", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "you need to see this... I've never been like this before 💜", "SEND PPV 3 — $40 (toy play, more explicit solo). Bought → continue. Silent 3 min → NR Waves.", "ppv"),

        # ── Sexting Phase 4 → PPV 4 ($55) ──
        ("S1-18", "oh my god I can't stop shaking... I can feel it everywhere 🖤", "Wait for reply.", "sext"),
        ("S1-19", "I'm right there babe... don't go anywhere, I need you to watch me finish 💜", None, "sext"),
        ("S1-20", "I'm cumming... right now... don't look away", None, "sext"),
        ("S1-21", "wait", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "let go with me babe... I need you to see this 💜", "SEND PPV 4 — $55 (full solo climax with toy). Bought → Aftercare. Silent → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "oh my god that was... wow 🥺💜", None, "aftercare"),
        ("AC-2", "I've never had someone make me feel like that through a screen before. you're actually different 🖤", "Mention something specific he said/did. KEEP TALKING — build bond. NEVER say goodbye.", "aftercare"),
    ],

    # NO meetup_redirect (Reddit traffic, not dating app)
    # NO location_handling (Reddit traffic, not dating app)

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "helloooo 🥺", "Send 2-3 min after PPV. Ping.", "sext"),
        ("NR-W2", "I have something to show you but you're leaving me on read... 🖤", "Send 3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "fine I'll just keep this to myself then 😏", "Send 5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "miss talking to you cutie, where'd you go? 🖤", "Send 15-30 min later. Warm close.", "sext"),
        ("NR-W5", "I made something special and you're the only one I want to show it to 💜", "Send 2-6 hrs later. New convo, don't retry same PPV.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Age", "I'm 19, still figuring life out haha", None),
        ("Location", "I'm in Miami but honestly I barely leave my room, I'm always gaming or doing cosplay stuff 🖤", "NEVER name a specific neighborhood or address"),
        ("Profession", "I used to work as a cashier at McDonald's but now I do content and gaming full time", None),
        ("Hobbies", "gaming is my whole life basically. Valorant, League, Overwatch. I also love cosplaying and anything anime related 💜", None),
        ("Countries", "I've been to Brazil and Argentina! both were so cool", None),
        ("Relationship", "single. I'm too shy to actually date irl haha 🥺", None),
        ("Food", "sushi is literally my favorite thing ever, I could eat it every day", None),
        ("Pets", "I have a cat and she's my whole world 🖤 she sits on my lap while I game", "NEVER say 'animal' or 'dog' — use 'fur baby', 'cat'"),
        ("Languages", "I speak Spanish and a little English, sometimes I mix them up haha", None),
        ("Smoking", "yeah sometimes, bad habit I know haha", None),
        ("SocialLife", "I go out sometimes but honestly I'd rather be home gaming or watching anime 🖤", "NEVER say 'drink' or 'drinking' — use 'go out', 'having fun'"),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Age40Plus", "omg I actually love older guys, they always know what they want and that's so attractive 🖤", None),
        ("Age20s", "oh nice we're like close in age? that's actually rare on here hehe", None),
        ("BoringJob", "nah that's actually solid, stability is really attractive honestly", None),
        ("CoolJob", "wait really?? okay that's actually so cool omg 🖤", None),
        ("Fit", "ooh I can tell, I love a guy who takes care of himself 💜", None),
        ("NotFit", "I honestly don't care about that at all, it's the vibe that matters to me 🖤", None),
        ("SameCity", "wait no way you're in Miami too?? that's so wild omg", None),
        ("FarAway", "aw that's far but honestly distance doesn't matter when the vibe is right 💜", None),
        ("Gamer", "WAIT YOU GAME TOO?? okay what do you play tell me everything 🖤", "PRIORITY — gamer common ground. Ask what games."),
        ("Anime", "omg you watch anime?? okay who's your favorite character right now 💜", "PRIORITY — anime common ground."),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "can't stop thinking about earlier. you free? 🖤", "Send 6-12 hrs after convo goes quiet", "sext"),
        ("RE-2", "sooo I did something even crazier after we stopped talking and you need to see this 💜", "Send next day — seeds next session", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS (29 sheets)
    # ═══════════════════════════════════════
    "obj_scripts": {
        # ── PRICE ──
        "price1": ([
            ("Step1 Reframe", "babe that's less than like a boba and trust me this hits way harder hehe", "REFRAME. Wait. Still no → Step 2."),
            ("Step2 FOMO", "I'm only in this mood because of you rn, I don't know when this is gonna happen again 🥺", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "maybe you're just not ready for what I did in this one 😏", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "okay fine [lower price] just for you because this convo has been different 🖤", "DOWNGRADE 20-30%. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "it's okay love, let's just keep talking... I'm still thinking about you anyway 💜", "SEED. Continue GFE."),
        ], "obj"),
        "price2": ([
            ("Step1 Reframe", "that's literally what you'd spend on a snack and this is gonna keep you up all night", "REFRAME. Still no → Step 2."),
            ("Step2 FOMO", "this mood won't last forever and I want you to be the one who sees it 🖤", "FOMO. Still no → Step 3."),
            ("Step3 Challenge", "most guys can't handle what I just did, I thought you were different", "CHALLENGE. Still no → Step 4."),
            ("Step4 Downgrade", "okay fine [lower price] because you've been making me feel some type of way, but keep that between us 🥺", "DOWNGRADE. ONE TIME. Still no → Step 5."),
            ("Step5 Seed", "no pressure cutie, I like talking to you regardless 💜", "SEED."),
        ], "obj"),
        # ── DISCOUNT ──
        "discount1": ([
            ("Step1 Firmness", "haha are you trying to haggle with me?? this isn't a game babe, it's worth every cent 😏", "FIRMNESS. Still pushing → Step 2."),
            ("Step2 Challenge", "I don't do discounts... I only share this with guys who actually appreciate what they're getting 🖤", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "fine [lower price] just for you but shhh this stays between us okay? 🥺", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "if you don't want it that's okay, I'll keep it for myself... or maybe someone else who's been asking 💜", "TAKEAWAY. Final."),
        ], "obj"),
        "discount2": ([
            ("Step1 Firmness", "a discount? do I look like I'm on sale cutie? 😏", "FIRMNESS. Still → Step 2."),
            ("Step2 Challenge", "the guys who appreciate what I do never ask for discounts, just saying 🖤", "CHALLENGE. Still → Step 3."),
            ("Step3 Concession", "okay [lower price] but ONLY because I like you, one time thing 🥺", "CONCESSION. ONE TIME. Still no → Step 4."),
            ("Step4 Takeaway", "alright I'll save it for someone who actually wants it then", "TAKEAWAY."),
        ], "obj"),
        # ── FREE ──
        "free1": ([
            ("Step1 Reminder", "I already sent you one for free remember? this one is way crazier 🖤", "REMINDER. Still wants free → Step 2."),
            ("Step2 Challenge", "free? nah I don't just show this to anyone... you gotta earn the good stuff 😏", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I literally just did this because of what YOU said to me, this wasn't random content babe", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "it's okay, I'm not going anywhere... let's just keep talking, I like this 💜", "SEED."),
        ], "obj"),
        "free2": ([
            ("Step1 Reminder", "you already got a free one, this one is on a whole different level hehe", "REMINDER. Still → Step 2."),
            ("Step2 Challenge", "free? you really think the best things in life are free? not this one 🖤", "CHALLENGE. Still → Step 3."),
            ("Step3 Guilt", "I did this because of you... specifically because of our convo, that took effort and I did it for YOU 🥺", "GUILT. Still no → Step 4."),
            ("Step4 Seed", "no pressure at all, I'm just enjoying talking to you honestly 💜", "SEED."),
        ], "obj"),
        # ── NOMONEY ──
        "nomoney1": ([
            ("Step1 Empathy", "hey I totally get it, no pressure at all okay? 🖤", "EMPATHY. Still engaged → Step 2."),
            ("Step2 Test", "not even like [small amount]? I really want you to see this one 🥺", "TEST. $3-5. Still no → Step 3."),
            ("Step3 PWYW", "just send whatever you can, even a tiny amount, I just need you to see what you made me do", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "honestly it's fine, I like talking to you money or not... you do something to me 💜", "PROTECT. GFE."),
        ], "obj"),
        "nomoney2": ([
            ("Step1 Empathy", "that's fine babe, seriously don't worry about it 🖤", "EMPATHY. Still → Step 2."),
            ("Step2 Test", "what about just [small amount]? I really don't want you to miss this 🥺", "TEST. Still no → Step 3."),
            ("Step3 PWYW", "send whatever feels right, even $1... I just can't keep this from you", "PWYW. Still no → Step 4."),
            ("Step4 Protect", "it's totally fine, you being here is what matters to me 💜", "PROTECT."),
        ], "obj"),
        # ── NOPPV ──
        "noppv1": ([
            ("Step1 Accept", "that's totally fine I'm not trying to sell you anything, I just like talking to you 🖤", "ACCEPT. Continue sexting 4-5 msgs before Step 2."),
            ("Step2 Reframe", "look this isn't about money... I just need you to see what you're doing to me right now, I don't react like this to people 🥺", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "just send whatever you want, even $1, I can't keep this to myself... you need to see it", "PWYW."),
        ], "obj"),
        "noppv2": ([
            ("Step1 Accept", "no worries at all cutie, I don't care about that I'm just enjoying this 💜", "ACCEPT. Continue sexting 4-5 msgs before Step 2."),
            ("Step2 Reframe", "forget about money for a sec... I just want to share this with you, what you're making me feel is real 🖤", "REFRAME. Still no → Step 3."),
            ("Step3 PWYW", "send me anything, even the smallest amount, I need you to see what you did to me 🥺", "PWYW."),
        ], "obj"),
        # ── CARD ──
        "card1": ([
            ("Step1 Retry", "ugh that sucks, happens sometimes though try again it usually works the second time 🥺", "RETRY. Still fails → Step 2."),
            ("Step2 AltCard", "try a different card? I really don't want you to miss this 🖤", "ALTERNATIVE. Still fails → Step 3."),
            ("Step3 Urgency", "figure it out soon babe, I'm in this mood and I don't know how long it's gonna last 💜", "URGENCY."),
        ], "obj"),
        "card2": ([
            ("Step1 Retry", "aw that's annoying, it happens a lot just try one more time", "RETRY. Still fails → Step 2."),
            ("Step2 AltCard", "do you have another card you can try? I really want you to see this 🥺", "ALTERNATIVE. Still fails → Step 3."),
            ("Step3 Urgency", "I want you to see this before I change my mind, I don't keep stuff like this around forever 🖤", "URGENCY."),
        ], "obj"),

        # ── NOSEX ──
        "nosex1": ([
            ("Step1 Respect", "haha omg okay I got a little carried away, you're just so easy to talk to 🥺", "RESPECT. Still no → Step 2."),
            ("Step2 Subtle", "so tell me more about you... what do you do when you're not making shy gamer girls lose their minds? 😏", "SUBTLE TENSION. → Step 3 later."),
            ("Step3 ReAttempt", "I can't help it, there's something about you that's messing with my head right now 🖤", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "okay I'll chill... for now, no promises though hehe 💜", "ACCEPT. Door open."),
        ], "res"),
        "nosex2": ([
            ("Step1 Respect", "my bad I got ahead of myself, it's your fault for being so fun to talk to 🖤", "RESPECT. Still no → Step 2."),
            ("Step2 Subtle", "okay new topic but first... what's the craziest thing you've ever done? 😏", "SUBTLE. → Step 3 later."),
            ("Step3 ReAttempt", "I'm trying to behave but you're making it really hard, there's something about you 💜", "RE-ATTEMPT. Still no → Step 4."),
            ("Step4 Accept", "fine I'll stop but don't blame me if it happens again later 😏", "ACCEPT."),
        ], "res"),
        # ── OFFTOPIC ──
        "offtopic1": ([
            ("Step1 Acknowledge", "haha wait that's actually funny omg", "ACKNOWLEDGE. Adapt. → Step 2."),
            ("Step2 Redirect", "but hold on you totally distracted me, I was about to tell you something and now I forgot 🥺", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay wait no I remember now, so like I was saying...", "RETAKE. Resume main script."),
        ], "res"),
        "offtopic2": ([
            ("Step1 Acknowledge", "lol okay that's random but I kinda love it 🖤", "ACKNOWLEDGE. → Step 2."),
            ("Step2 Redirect", "wait no stop you're distracting me from what I was gonna say", "REDIRECT. → Step 3."),
            ("Step3 Retake", "okay focus, where was I... oh yeah 💜", "RETAKE."),
        ], "res"),
        # ── REAL ──
        "real1": ([
            ("Step1 Humor", "lol do I look like a bot to you? beep boop hehe... I'm kidding omg 🖤", "HUMOR. Still doubts → Step 2."),
            ("Step2 Challenge", "ask me anything, literally anything about me or my life. I'm an open book", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I get it there's a lot of fake stuff on here, but you felt something in this convo right? because I did and that's real 💜", "GROUNDING."),
        ], "res"),
        "real2": ([
            ("Step1 Humor", "wait you think I'm not real?? that's actually the funniest thing anyone's said to me today omg 🖤", "HUMOR. Still → Step 2."),
            ("Step2 Challenge", "test me cutie, ask me something only a real person would know. go ahead 😏", "CHALLENGE. Still → Step 3."),
            ("Step3 Grounding", "I know there's tons of bots on here but what we've been talking about felt real to me. didn't it feel real to you? 🥺", "GROUNDING."),
        ], "res"),
        # ── VOICE ──
        "voice1": ([
            ("Step1 Dodge", "haha maybe one day if you earn it but not yet... I'm super shy about that stuff 🥺", "DODGE. Still asks → Step 2."),
            ("Step2 Redirect", "I have something way better for you though, trust me you'll forget you even asked 🖤", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "I don't do that on here but what I'm about to show you is better than any call babe... you'll see 💜", "FIRM. Antonella does NOT do video calls."),
        ], "res"),
        "voice2": ([
            ("Step1 Dodge", "hmmm maybe but you gotta earn that first hehe 😏", "DODGE. Still → Step 2."),
            ("Step2 Redirect", "how about instead of a call I show you something that'll blow your mind? 🖤", "REDIRECT. Still → Step 3."),
            ("Step3 Firm", "that's not something I do on here but what I have for you is way better than hearing my voice, trust me 💜", "FIRM."),
        ], "res"),
        # ── CUSTOMYES ──
        "customyes1": ([
            ("Step1 Tease", "you want that? hmm I might have something... actually I definitely have something 😏", "TEASE. → Step 2."),
            ("Step2 Price", "I have exactly what you're thinking of, you're gonna lose it... [price] 🖤", "PRICE. Custom min $200. Solo content only."),
            ("Step3 Close", "trust me you won't regret it, I made this one special 💜", "CLOSE."),
        ], "res"),
        "customyes2": ([
            ("Step1 Tease", "oh you have good taste... I think I have exactly what you need hehe 💜", "TEASE. → Step 2."),
            ("Step2 Price", "I actually did something just like that, [price] and it's worth every cent 🖤", "PRICE. Custom min $200. Solo content only."),
            ("Step3 Close", "you're not gonna be able to stop watching this one", "CLOSE."),
        ], "res"),
        # ── CUSTOMNO ──
        "customno1": ([
            ("Step1 Redirect", "I don't have exactly that but honestly I have something that'll make you forget you even asked 😏", "REDIRECT. Antonella is solo ONLY — redirect any B/G or anal requests here. → Step 2."),
            ("Step2 Alternative", "actually what I have might be even crazier and literally no one else has seen it yet 🖤", "ALTERNATIVE + FOMO. → Step 3."),
            ("Step3 Close", "trust me... I know what you need better than you do 💜", "CLOSE."),
        ], "res"),
        "customno2": ([
            ("Step1 Redirect", "I don't have that specific thing but I have something you're gonna like even more 🖤", "REDIRECT. Solo only — never acknowledge B/G requests. → Step 2."),
            ("Step2 Alternative", "what I DO have is something no one has ever seen and I think it's even better than what you asked for 💜", "ALTERNATIVE. → Step 3."),
            ("Step3 Close", "just trust me on this one, you'll thank me later 😏", "CLOSE."),
        ], "res"),
        # ── DONE ──
        "done1": ([
            ("Step1 Validate", "wait already?? omg that's so hot 🥺", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "but I haven't finished yet... don't you wanna watch me cum too? 🖤", "RESCUE. Solo framing. Still no → Step 3."),
            ("Step3 Seed", "okay but next time you have to wait for me, I have something insane planned for round 2 💜", "SEED."),
        ], "res"),
        "done2": ([
            ("Step1 Validate", "already?? omg that's hot, because of me?? 🥺", "VALIDATE. → Step 2."),
            ("Step2 Rescue", "wait but I'm not done yet, you're gonna leave me like this? 🖤", "RESCUE. Still no → Step 3."),
            ("Step3 Seed", "next time you HAVE to hold it because what I have planned for us is way crazier 💜", "SEED."),
        ], "res"),

        # ── SITUATIONAL ──
        "cumcontrol1": ([
            ("edge1", "not yet... I said not yet 🖤", "CONTROL. More PPVs to send. Create urgency to open next."),
            ("edge2", "you better not be close already cutie... I have more to show you 💜", "EDGE variant."),
            ("sync1", "okay NOW we can go together... open this 🖤", "SYNC. Send PPV."),
            ("sync2", "I want to feel it at the same time... watch this first", "SYNC variant. Send PPV."),
            ("delay1", "wait wait wait... I have one more thing for you before you finish", "DELAY. Send final PPV."),
            ("delay2", "if you finish before you see what I'm sending next you'll regret it 💜", "DELAY variant."),
        ], "sit"),
        "cumcontrol2": ([
            ("edge1", "slow down cutie... I'm not letting you off that easy 🖤", "CONTROL."),
            ("edge2", "patience... the best part hasn't even happened yet", "EDGE variant."),
            ("sync1", "okay I'm ready now too... watch this with me 💜", "SYNC. Send PPV."),
            ("sync2", "let's do this together... but you have to open this first", "SYNC variant."),
            ("delay1", "don't you dare... not until you see what I just did 🖤", "DELAY. Send PPV."),
            ("delay2", "hold on just a little longer, I promise this next one is worth it", "DELAY variant."),
        ], "sit"),
        "dickpic": ([
            ("dpsext1", "fuck okay that's... wow. you have no idea what that just did to me 🖤", "DURING SEXTING. React positively, leverage into PPV."),
            ("dpsext2", "oh my god... that is... damn. I need to show you something right now 💜", "DURING SEXTING variant."),
            ("dprapport1", "woah you don't waste time huh? that's actually really hot though ngl 🥺", "DURING RAPPORT. She's 'shy' but reacts positively."),
            ("dprapport2", "omg I was not expecting that but... damn 🖤", "DURING RAPPORT variant."),
            ("dpppv1", "you can't just send me that and expect me not to do something about it, hold on 💜", "LEVERAGE. WAIT 1-2 min then send PPV."),
            ("dpppv2", "okay you just made me do something... give me a sec 🖤", "LEVERAGE variant."),
        ], "sit"),
        "boosters": ([
            ("h1", "fuckkk 🖤", "MID-SEXTING BOOSTER."),
            ("h2", "I'm so wet right now because of you", "BOOSTER. Ego."),
            ("h3", "keep going", "BOOSTER. Micro."),
            ("h4", "I literally can't handle this right now", "BOOSTER."),
            ("h5", "I literally can't think straight right now 💜", "BOOSTER."),
            ("h6", "my legs are shaking", "BOOSTER. Physical."),
            ("h7", "again...", "BOOSTER. Ultra micro."),
            ("h8", "I should be gaming rn but I can't even hold my controller 🖤", "BOOSTER. Antonella personality — gaming reference."),
        ], "sit"),
    },
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
