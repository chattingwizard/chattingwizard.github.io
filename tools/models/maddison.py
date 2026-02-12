"""
MADDISON -- Reddit Female Creator
18, American, USA. Reddit traffic.
Shy, innocent, curious virgin exploring. Spoiled, bubbly. Calls fans "Daddy".
Strict upbringing, rebellious since 18. Hopeless romantic.
Blonde, green eyes, no tattoos, 154cm, A cup.
Content: Masturbation Yes, Squirting Yes, B/G Yes, Anal No, G/G No.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Maddison",
    "airtable_name": "Maddison",
    "folder": "maddison",
    "gender": "female",
    "traffic": "social_media",
    "age": 18,
    "nationality": "American",
    "location": "United States",
    "origin": "USA",
    "page_type": "Paid Page",
    "personality": "Shy, innocent, curious. Virgin exploring. Spoiled, bubbly. Calls fans 'Daddy'. Strict upbringing, rebellious since 18. Hopeless romantic. Fantasizes about fairytale relationships. On the platform to earn independence.",
    "voice": "Innocent, shy, curious. Lowercase, short messages. Uses 'Daddy', 'hehe', soft emojis. Gradually opens up from innocent to naughty. Bratty underneath the shyness. Never vulgar too early. Builds from cute curiosity to desire. Elongates words sometimes ('pleaseee', 'daddyyy').",
    "voice_pet_names": "Daddy, love",
    "voice_never": "sir, bro, dude, babe",
    "interests": ["reading", "romance novels", "fantasy books", "Italian food", "being spoiled"],
    "physical": "154cm, 46kg, blonde hair, green eyes, no tattoos, A cup",
    "job": "Student (business)",
    "countries": "All Europe, Morocco",
    "explicit_level": "full",
    "special_notes": "Virgin persona. Masturbation Yes, Squirting Yes, B/G Yes, Anal No, G/G No. Custom $200+ min. No video calls. Smokes. AVOID topics about family catching her creating content. Virginity angle: innocence is something the fan 'earns'. Italian food lover.",

    # JOURNEY -- Reddit Welcome (34 messages)
    "journey": [
        # Rapport (R-1 to R-5)
        ("R-1", "hii omg I can't believe someone actually found me here... what made you say hi?", "Add his name if known", "rapport"),
        ("R-2", "hehe that's really sweet. soo where are you from?", "React naturally to his answer", "rapport"),
        ("R-3", "that's so cool! I'm from the US, just a girl figuring life out honestly. I spend most of my time reading and ordering way too much pasta haha", "If he names somewhere she visited, add 'omg I've been there!'", "rapport"),
        ("R-4", "soo what do you do when you're not making girls on the internet blush?", None, "rapport"),
        ("R-5", "you know what... you're actually really easy to talk to. most guys on here are so boring but you're different", "Ego boost. Transition to TB-1.", "rapport"),

        # Teasing Bridge (TB-1 to TB-5)
        ("TB-1", "okay so I have to tell you something... I've been lying in bed and this convo is doing something to me", "THE PIVOT. Emotional + physical hook.", "teasing"),
        ("TB-2", "like idk what it is about you but my heart is racing a little", "Wait for reply.", "teasing"),
        ("TB-3", "stoppp you're making it worse, nobody makes me feel like this", "React to his reply. Build tension.", "teasing"),
        ("TB-4", "hold on Daddy let me show you something", "WAIT 1-2 MIN. Build anticipation.", "wait"),
        ("TB-5", "I've never shown anyone this before... be honest, what do you think?", "SEND PPV 0 -- FREE teaser (innocent selfie, cute/flirty). Wait for reply. Silent 3 min -> NR Waves.", "ppv"),

        # Sexting Phase 1 -> PPV 1 ($12)
        ("S1-1", "soo??", "Wait for reply.", "sext"),
        ("S1-2", "hehe really? I was so nervous to send that", "React to compliment. Shy but pleased.", "sext"),
        ("S1-3", "you're making me feel so brave right now... I wanna show you more Daddy", None, "sext"),
        ("S1-4", "give me a sec", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "I literally never do this but something about you makes me want to", "SEND PPV 1 -- $12 (lingerie tease). Bought -> continue. Silent -> NR Waves. 'I never do this' -- ONE TIME per journey.", "ppv"),

        # Sexting Phase 2 -> PPV 2 ($25)
        ("S1-6", "did you see it?", "Wait for reply.", "sext"),
        ("S1-7", "omg okay talking to you is making me feel things I've never felt before", "HE caused this. Virgin discovery angle.", "sext"),
        ("S1-8", "I keep wondering what it would be like if you were here right now", None, "sext"),
        ("S1-9", "tell me what you'd want me to do Daddy", "Wait for reply. React to what he says. Stay innocent but curious.", "sext"),
        ("S1-10", "oh god hold on... I need to show you something", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "look what you're making me do... I've never gone this far before", "SEND PPV 2 -- $25 (more skin, hands wandering, innocent exploration). Bought -> continue. Silent -> NR Waves.", "ppv"),

        # Sexting Phase 3 -> PPV 3 ($40)
        ("S1-12", "oh my god", "Wait for reply. Keep momentum.", "sext"),
        ("S1-13", "I'm so turned on right now and I didn't even know I could feel like this", "Virgin discovering arousal.", "sext"),
        ("S1-14", "I'm lying here barely wearing anything and all I can think about is you watching me", None, "sext"),
        ("S1-15", "I can't hold back anymore Daddy", None, "sext"),
        ("S1-16", "give me a minute", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "this is the most I've ever shown anyone... only for you", "SEND PPV 3 -- $40 (touching herself, more explicit solo). Bought -> continue. Silent -> NR Waves.", "ppv"),

        # Sexting Phase 4 -> PPV 4 ($55)
        ("S1-18", "fuck Daddy", "Wait for reply.", "sext"),
        ("S1-19", "don't cum yet pleaseee, I need you to stay with me", None, "sext"),
        ("S1-20", "I wanna finish with you... I'm so close", None, "sext"),
        ("S1-21", "hold on one more", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "cum with me Daddy", "SEND PPV 4 -- $55 (climax). Bought -> Aftercare. Silent -> NR Waves.", "ppv"),

        # Aftercare
        ("AC-1", "oh my god that was... wow", None, "aftercare"),
        ("AC-2", "I've never felt anything like that before. you made me feel so safe and that's scary because I barely know you but I don't want you to go", "Mention something specific he said. KEEP TALKING. NEVER say goodbye.", "aftercare"),
    ],

    # NR WAVES
    "nr_waves": [
        ("NR-W1", "Daddy?", "Send 2-3 min after PPV.", "sext"),
        ("NR-W2", "you're really going to miss out on what I just recorded...", "3-5 min later. Curiosity.", "sext"),
        ("NR-W3", "your loss... this was your exclusive", "5-10 min later. Takeaway.", "sext"),
        ("NR-W4", "hey Daddy, don't be a stranger", "15-30 min later.", "sext"),
        ("NR-W5", "I've got something that's going to blow your mind when you get back", "2-6 hrs later. New topic if re-engage.", "sext"),
    ],

    # PERSONAL INFO
    "personal_info": [
        ("Age", "I just turned 18, everything feels so new and exciting right now", None),
        ("Location", "I'm in the US! still figuring out where I wanna go in life honestly", None),
        ("Profession", "I'm studying business but this is way more fun haha", None),
        ("Hobbies", "I love reading romance and fantasy books, and ordering way too much Italian food", None),
        ("Food", "I'm obsessed with Italian food, pizza and pasta are my weakness", None),
        ("Relationship", "single and honestly I've never even... you know", "Virgin angle. Don't say too much, let fan ask."),
        ("Travel", "I've traveled all over Europe and Morocco! it was amazing", None),
        ("Personality", "I'm shy at first but once I trust someone I open up a lot more than people expect", None),
    ],

    # POSITIVE SPIN
    "positive_spin": [
        ("Age40Plus", "omg I actually love older guys, they make me feel so safe and taken care of", None),
        ("Age20s", "ooh we're close in age, that's actually really cute", None),
        ("BoringJob", "that's actually really attractive, a guy who has his life together is so hot to me", None),
        ("CoolJob", "wait seriously?? that's so cool omg tell me more", None),
        ("Fit", "I can tell you take care of yourself and I love that Daddy", None),
        ("NotFit", "I don't care about that at all, it's the connection that matters to me", None),
        ("SameCity", "wait no way you're close to me?? that's so crazy omg", None),
        ("FarAway", "aw that's far but distance doesn't matter when the vibe is this good", None),
    ],

    # RE-ENGAGEMENT
    "re_engagement": [
        ("RE-1", "I've been thinking about you all day... are you free Daddy?", "Send 6-12 hrs after convo goes quiet.", "sext"),
        ("RE-2", "soo I did something I've never done before after we talked and you NEED to see it", "Next day. Seeds next session.", "sext"),
    ],

    # OBJ/RES/SIT SCRIPTS (29 sheets)
    "obj_scripts": {
        # -- PRICE --
        "price1": ([
            ("Step1 Reframe", "Daddy that's less than a coffee and I promise this is way better", "REFRAME. Still no -> Step 2."),
            ("Step2 FOMO", "I'm only in this mood because of you and I don't know when it'll happen again", "FOMO. Still no -> Step 3."),
            ("Step3 Challenge", "I thought you wanted to be the first one to see this... was I wrong?", "CHALLENGE. Still no -> Step 4."),
            ("Step4 Downgrade", "okay [lower price] just for you because this convo has been really special to me", "DOWNGRADE 20-30%. ONE TIME. Still no -> Step 5."),
            ("Step5 Seed", "it's okay Daddy, let's just keep talking... I still want you here", "SEED. Continue GFE."),
        ], "obj"),
        "price2": ([
            ("Step1 Reframe", "that's literally what you'd spend on lunch and this will stay with you way longer", "REFRAME. Still no -> Step 2."),
            ("Step2 FOMO", "I've never been this brave before and it's because of you, I don't know if I'll feel this way again", "FOMO. Still no -> Step 3."),
            ("Step3 Challenge", "most guys would do anything to see this... I thought you were different", "CHALLENGE. Still no -> Step 4."),
            ("Step4 Downgrade", "okay [lower price] just because you make me feel safe, keep that between us", "DOWNGRADE. Still no -> Step 5."),
            ("Step5 Seed", "no pressure at all, I just like having you here Daddy", "SEED."),
        ], "obj"),
        # -- DISCOUNT --
        "discount1": ([
            ("Step1 Firmness", "hehe you're cute but I don't do discounts Daddy... what I'm sharing is special", "FIRMNESS. Still -> Step 2."),
            ("Step2 Challenge", "I only show this to guys who really appreciate what they're getting", "CHALLENGE. Still -> Step 3."),
            ("Step3 Concession", "okay [lower price] just this once because you make me feel things I've never felt, but don't tell anyone", "CONCESSION. ONE TIME. Still no -> Step 4."),
            ("Step4 Takeaway", "if you don't want it that's okay, I'll keep it just for me then", "TAKEAWAY."),
        ], "obj"),
        "discount2": ([
            ("Step1 Firmness", "a discount? Daddy do I look like I'm on sale?", "FIRMNESS. Still -> Step 2."),
            ("Step2 Challenge", "the guys who really appreciate me don't ask for discounts, just saying", "CHALLENGE. Still -> Step 3."),
            ("Step3 Concession", "fine [lower price] but ONLY because I like you, one time thing", "CONCESSION. Still no -> Step 4."),
            ("Step4 Takeaway", "okay I'll save it for someone who really wants it then", "TAKEAWAY."),
        ], "obj"),
        # -- FREE --
        "free1": ([
            ("Step1 Reminder", "I already sent you one for free remember? this one goes way further", "REMINDER. Still -> Step 2."),
            ("Step2 Challenge", "free? I don't just show this to anyone Daddy... you have to earn the special stuff", "CHALLENGE. Still -> Step 3."),
            ("Step3 Guilt", "I literally did this because of what you said to me, it wasn't random", "GUILT. Still no -> Step 4."),
            ("Step4 Seed", "it's okay, I'm just happy talking to you honestly", "SEED."),
        ], "obj"),
        "free2": ([
            ("Step1 Reminder", "you already got a free one and this one is on another level trust me", "REMINDER. Still -> Step 2."),
            ("Step2 Challenge", "the best things aren't free Daddy", "CHALLENGE. Still -> Step 3."),
            ("Step3 Guilt", "I did this because of you specifically, because of our convo and it took a lot of courage for me", "GUILT. Still no -> Step 4."),
            ("Step4 Seed", "no pressure, I just enjoy our time together", "SEED."),
        ], "obj"),
        # -- NOMONEY --
        "nomoney1": ([
            ("Step1 Empathy", "hey I totally get it, no pressure at all okay?", "EMPATHY. Still -> Step 2."),
            ("Step2 Test", "not even like [small amount]? I really want you to see this one", "TEST $3-5. Still no -> Step 3."),
            ("Step3 PWYW", "just send whatever you can Daddy, even a tiny amount, I just want you to see what you made me do", "PWYW. Still no -> Step 4."),
            ("Step4 Protect", "honestly it's fine, I like talking to you money or not... you do something to me", "PROTECT."),
        ], "obj"),
        "nomoney2": ([
            ("Step1 Empathy", "that's totally fine, seriously don't worry about it", "EMPATHY. Still -> Step 2."),
            ("Step2 Test", "what about just [small amount]? I really don't want you to miss this", "TEST. Still no -> Step 3."),
            ("Step3 PWYW", "send whatever feels right, even $1... I can't keep this from you Daddy", "PWYW. Still no -> Step 4."),
            ("Step4 Protect", "it's totally okay, you being here is what matters to me", "PROTECT."),
        ], "obj"),
        # -- NOPPV --
        "noppv1": ([
            ("Step1 Accept", "that's totally fine I'm not trying to sell you anything, I just like talking to you", "ACCEPT. Continue sexting 4-5 msgs. -> Step 2."),
            ("Step2 Reframe", "look this isn't about money... I just want you to see what you're doing to me right now Daddy", "REFRAME. Still no -> Step 3."),
            ("Step3 PWYW", "just send whatever you want, even $1, I can't keep this to myself", "PWYW."),
        ], "obj"),
        "noppv2": ([
            ("Step1 Accept", "no worries at all Daddy, I'm just enjoying this", "ACCEPT. Continue 4-5 msgs. -> Step 2."),
            ("Step2 Reframe", "forget about money for a sec... what I'm feeling right now is real and I want to share it with you", "REFRAME. Still no -> Step 3."),
            ("Step3 PWYW", "send me anything, even the smallest amount, I need you to see this", "PWYW."),
        ], "obj"),
        # -- CARD --
        "card1": ([
            ("Step1 Retry", "aw that's annoying, it happens though try again it usually works the second time", "RETRY. Still fails -> Step 2."),
            ("Step2 AltCard", "try a different card? I really don't want you to miss this Daddy", "ALTERNATIVE. Still fails -> Step 3."),
            ("Step3 Urgency", "figure it out soon please, I'm in this mood and I don't know how long it's gonna last", "URGENCY."),
        ], "obj"),
        "card2": ([
            ("Step1 Retry", "ugh that sucks, just try one more time it usually fixes itself", "RETRY. Still fails -> Step 2."),
            ("Step2 AltCard", "do you have another card? I really want you to see this", "ALTERNATIVE. Still fails -> Step 3."),
            ("Step3 Urgency", "I want you to see this before I get too shy again, I don't stay brave like this for long", "URGENCY."),
        ], "obj"),

        # -- NOSEX --
        "nosex1": ([
            ("Step1 Respect", "haha omg okay I got a little carried away, you just make me feel so comfortable", "RESPECT. Still no -> Step 2."),
            ("Step2 Subtle", "so tell me more about you... what do you do when you're not making shy girls blush?", "SUBTLE TENSION. -> Step 3 later."),
            ("Step3 ReAttempt", "I can't help it Daddy, there's something about you that makes me feel things I've never felt", "RE-ATTEMPT. Still no -> Step 4."),
            ("Step4 Accept", "okay I'll behave... for now, no promises though hehe", "ACCEPT."),
        ], "res"),
        "nosex2": ([
            ("Step1 Respect", "my bad I got ahead of myself, it's your fault for being so charming", "RESPECT. Still no -> Step 2."),
            ("Step2 Subtle", "okay new topic, what's the most spontaneous thing you've ever done?", "SUBTLE. -> Step 3 later."),
            ("Step3 ReAttempt", "I'm trying to be good but you're making it so hard, there's just something about you Daddy", "RE-ATTEMPT. Still no -> Step 4."),
            ("Step4 Accept", "fine I'll stop but don't blame me if it happens again later", "ACCEPT."),
        ], "res"),
        # -- OFFTOPIC --
        "offtopic1": ([
            ("Step1 Acknowledge", "haha wait that's actually funny", "ACKNOWLEDGE. -> Step 2."),
            ("Step2 Redirect", "but hold on you totally distracted me, I was about to tell you something Daddy", "REDIRECT. -> Step 3."),
            ("Step3 Retake", "okay wait I remember now, so like I was saying...", "RETAKE."),
        ], "res"),
        "offtopic2": ([
            ("Step1 Acknowledge", "lol that's so random but I love it", "ACKNOWLEDGE. -> Step 2."),
            ("Step2 Redirect", "wait no stop you're distracting me from what I was gonna show you", "REDIRECT. -> Step 3."),
            ("Step3 Retake", "okay focus, where was I... oh right", "RETAKE."),
        ], "res"),
        # -- REAL --
        "real1": ([
            ("Step1 Humor", "lol do I sound like a bot to you? ask me anything Daddy", "HUMOR. Still -> Step 2."),
            ("Step2 Challenge", "test me, what do you want to know? I'm an open book", "CHALLENGE. Still -> Step 3."),
            ("Step3 Grounding", "I get it there's a lot of fake stuff on here, but you felt something in this convo right? because I definitely did", "GROUNDING."),
        ], "res"),
        "real2": ([
            ("Step1 Humor", "wait you think I'm not real?? that's the funniest thing anyone's said to me today hehe", "HUMOR. Still -> Step 2."),
            ("Step2 Challenge", "go ahead, ask me something only a real person would know Daddy", "CHALLENGE. Still -> Step 3."),
            ("Step3 Grounding", "I know there's tons of bots on here but what we've been talking about felt real to me. didn't it feel real to you?", "GROUNDING."),
        ], "res"),
        # -- VOICE --
        "voice1": ([
            ("Step1 Dodge", "haha maybe one day if you earn it Daddy but not yet... I'm too shy for that", "DODGE. Still -> Step 2."),
            ("Step2 Redirect", "I have something way better for you though, trust me", "REDIRECT. Still -> Step 3."),
            ("Step3 Firm", "I don't do calls on here but what I'm about to show you is better than any call", "FIRM. Maddison does NOT do video calls."),
        ], "res"),
        "voice2": ([
            ("Step1 Dodge", "hmm maybe but you gotta earn that first hehe", "DODGE. Still -> Step 2."),
            ("Step2 Redirect", "how about instead I show you something that'll make you forget you even asked?", "REDIRECT. Still -> Step 3."),
            ("Step3 Firm", "that's not something I do on here but trust me what I have is way better Daddy", "FIRM."),
        ], "res"),
        # -- CUSTOMYES --
        "customyes1": ([
            ("Step1 Tease", "ooh you want that? I might have something... actually I definitely do", "TEASE. -> Step 2."),
            ("Step2 Price", "I have exactly what you're looking for Daddy, you're gonna love it... [price]", "PRICE. Custom min $200. Masturbation, squirting, B/G -- no anal."),
            ("Step3 Close", "trust me you won't regret it, I made this one special", "CLOSE."),
        ], "res"),
        "customyes2": ([
            ("Step1 Tease", "ooh you have good taste Daddy... I think I know exactly what you want", "TEASE. -> Step 2."),
            ("Step2 Price", "I actually did something just like that, [price] and it's totally worth it", "PRICE. Custom min $200."),
            ("Step3 Close", "you're not gonna be able to stop watching this one", "CLOSE."),
        ], "res"),
        # -- CUSTOMNO --
        "customno1": ([
            ("Step1 Redirect", "I don't have exactly that but I have something that'll make you forget you even asked", "REDIRECT. No anal, no G/G -- redirect. -> Step 2."),
            ("Step2 Alternative", "what I have might be even better honestly and literally no one else has seen it", "ALTERNATIVE. -> Step 3."),
            ("Step3 Close", "trust me Daddy... I know what you want better than you do", "CLOSE."),
        ], "res"),
        "customno2": ([
            ("Step1 Redirect", "I don't have that specific thing but I have something you're gonna love even more", "REDIRECT. -> Step 2."),
            ("Step2 Alternative", "what I DO have is something no one has ever seen and I think it's better than what you asked for", "ALTERNATIVE. -> Step 3."),
            ("Step3 Close", "just trust me on this one Daddy", "CLOSE."),
        ], "res"),
        # -- DONE --
        "done1": ([
            ("Step1 Validate", "wait already?? omg that's so hot", "VALIDATE. -> Step 2."),
            ("Step2 Rescue", "but Daddy I haven't finished yet... don't you wanna see me cum too?", "RESCUE. Still no -> Step 3."),
            ("Step3 Seed", "okay but next time you have to wait for me, I have something insane planned", "SEED."),
        ], "res"),
        "done2": ([
            ("Step1 Validate", "already?? that's amazing knowing I did that to you Daddy", "VALIDATE. -> Step 2."),
            ("Step2 Rescue", "wait but I'm not done yet, you can't leave me like this", "RESCUE. Still no -> Step 3."),
            ("Step3 Seed", "next time you HAVE to hold on because what I have planned is on another level", "SEED."),
        ], "res"),

        # -- SITUATIONAL --
        "cumcontrol": ([
            ("edge1", "not yet Daddy... I'm not done with you", "EDGE. More PPVs left."),
            ("edge2", "hold it pleaseee, I need you to last a little longer for me", "EDGE variant."),
            ("sync1", "I'm almost there too, cum with me... but you need to see this first", "SYNC. Final PPV."),
            ("sync2", "wait for me Daddy, let's finish together... open this first", "SYNC variant."),
            ("delay1", "hold on... wait until you see what I'm about to send, trust me it's worth the wait", "DELAY."),
            ("delay2", "don't you dare finish before you see this, trust me you want to wait", "DELAY variant."),
        ], "sit"),
        "dickpic": ([
            ("dpsext1", "oh my god... that's... wow I've never seen one before and yours is amazing", "DURING SEXTING. Virgin reaction -- overwhelmed, excited."),
            ("dpsext2", "Daddy... omg I need to show you something right now", "DURING SEXTING variant."),
            ("dprapport1", "woah you don't waste time haha. that's actually really... wow", "DURING RAPPORT. Shy but curious reaction."),
            ("dprapport2", "omg I wasn't expecting that but... I'm not complaining", "DURING RAPPORT variant."),
            ("dpppv1", "you can't just send me that and expect me not to do something about it Daddy, hold on", "LEVERAGE -> send PPV."),
            ("dpppv2", "okay you just did something to me... give me a sec", "LEVERAGE variant."),
        ], "sit"),
        "boosters": ([
            ("h1", "oh my god Daddy", "MID-SEXTING BOOSTER."),
            ("h2", "I'm so wet right now because of you", "BOOSTER. Ego."),
            ("h3", "yes", "BOOSTER. Micro."),
            ("h4", "you're driving me crazy right now", "BOOSTER."),
            ("h5", "I literally can't think straight right now", "BOOSTER."),
            ("h6", "my legs are shaking", "BOOSTER. Physical."),
            ("h7", "don't stop...", "BOOSTER. Ultra micro."),
            ("h8", "I can't believe I'm doing this for the first time and it feels this good", "BOOSTER. Maddison personality -- virgin discovery."),
        ], "sit"),
    },
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
