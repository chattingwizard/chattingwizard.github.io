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
        ("S1-1", "wait you actually liked that? oh god I can feel my body responding... I'm already getting tingly between my legs 🥺", "Wait for reply.", "sext"),
        ("S1-2", "my breathing is getting heavier and I keep arching my back... my body wants something and I think it's you", "React to compliment. Shy but pleased.", "sext"),
        ("S1-3", "I'm touching myself right now and I want you to know it's because of you Daddy", None, "sext"),
        ("S1-4", "gimme a minute", "WAIT 2-3 MIN", "wait"),
        ("S1-5", "this is what you're making me do... I can't believe I'm showing you this 💕", "SEND PPV 1 -- $12 (lingerie tease). Bought -> continue. Silent -> NR Waves. 'I never do this' -- ONE TIME per journey.", "ppv"),

        # Sexting Phase 2 -> PPV 2 ($25)
        ("S1-6", "omg... I can't believe that just happened 🥺", "Wait for reply.", "sext"),
        ("S1-7", "I can't stop now even if I wanted to... my hand is already between my thighs and I'm soaked", "HE caused this. Virgin discovery angle.", "sext"),
        ("S1-8", "every part of me is on fire right now and it keeps getting more intense because of you 💕", None, "sext"),
        ("S1-9", "tell me exactly what you're thinking right now Daddy... I want to hear everything while I touch myself", "Wait for reply. React to what he says. Stay innocent but curious.", "sext"),
        ("S1-10", "oh god hold on... I need to show you something", "WAIT 2-3 MIN", "wait"),
        ("S1-11", "see what you did to me? I can't stop 💕", "SEND PPV 2 -- $25 (more skin, hands wandering, innocent exploration). Bought -> continue. Silent -> NR Waves.", "ppv"),

        # Sexting Phase 3 -> PPV 3 ($40)
        ("S1-12", "fuckk that feels so good 🥺", "Wait for reply. Keep momentum.", "sext"),
        ("S1-13", "my fingers are inside my pussy and I'm moaning so loud right now... I hope nobody can hear me", "Virgin discovering arousal.", "sext"),
        ("S1-14", "I'm going faster and faster and I can feel myself getting closer... my whole body is trembling 💕", None, "sext"),
        ("S1-15", "I'm so close to cumming and I need you to see what you're doing to me right now", None, "sext"),
        ("S1-16", "give me a minute", "WAIT 2-3 MIN", "wait"),
        ("S1-17", "I've never gone this far with anyone Daddy... watch what you made me do 💕", "SEND PPV 3 -- $40 (touching herself, more explicit solo). Bought -> continue. Silent -> NR Waves.", "ppv"),

        # Sexting Phase 4 -> PPV 4 ($55)
        ("S1-18", "oh fuck oh fuck my pussy is so swollen and my legs won't stop shaking 🥺", "Wait for reply.", "sext"),
        ("S1-19", "I can feel my pussy tightening around my fingers Daddy... I'm about to cum everywhere 💕", None, "sext"),
        ("S1-20", "I'm cumming... oh my god I'm squeezing so hard and it won't stop... I can feel it dripping everywhere", None, "sext"),
        ("S1-21", "don't go anywhere", "WAIT 1-2 MIN", "wait"),
        ("S1-22", "watch me cum for you Daddy... every single second of it 💕", "SEND PPV 4 -- $55 (climax). Bought -> Aftercare. Silent -> NR Waves.", "ppv"),

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
    "obj_scripts": {},
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
