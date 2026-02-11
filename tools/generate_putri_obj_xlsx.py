"""
Generate Putri OBJ/RES/SIT XLSX for Infloww import.

Structure:
- Each OBJ/RES protocol → 2 complete sequences (separate sheets)
- Each SIT group → 1 sheet with standalone scripts
- Sheet name = Infloww command (chatter types \sheetname)
- Row order REVERSED (Infloww convention)
- Emojis reduced (~40% of messages)
"""
import openpyxl
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side

wb = openpyxl.Workbook()

# ── STYLES ──
HEADER_FILL = PatternFill("solid", fgColor="1a1a2e")
HEADER_FONT = Font(bold=True, color="e6edf3", size=11)
OBJ_FILL = PatternFill("solid", fgColor="2d1a1a")
RES_FILL = PatternFill("solid", fgColor="1f1a2d")
SIT_FILL = PatternFill("solid", fgColor="1a2a1a")
WRAP = Alignment(wrap_text=True, vertical="top")
THIN = Border(bottom=Side(style="thin", color="30363d"))

def make_sheet(title, rows, fill):
    """Create a sheet with header + reversed rows. Each row: (name, text, note)"""
    ws = wb.create_sheet(title)
    ws.append(["Name", "Text", "Note", "*Guidelines"])
    for c in ["A","B","C","D"]:
        ws[f"{c}1"].fill = HEADER_FILL
        ws[f"{c}1"].font = HEADER_FONT
    ws.column_dimensions["A"].width = 20
    ws.column_dimensions["B"].width = 80
    ws.column_dimensions["C"].width = 50
    ws.column_dimensions["D"].width = 25
    for name, text, note in reversed(rows):
        ws.append([name, text, note, ""])
        r = ws.max_row
        for col in range(1, 5):
            cell = ws.cell(row=r, column=col)
            cell.alignment = WRAP
            cell.border = THIN
            if fill:
                cell.fill = fill

# ═══════════════════════════════════════════
#  A. OBJECTION HANDLING — 6 protocols × 2
# ═══════════════════════════════════════════

# ── PRICE ── (5 steps each)
make_sheet("price1", [
    ("Step1 Reframe", "babe that's less than a smoothie after my ride and trust me this hits wayyyy harder", "REFRAME. Compare to cheap item. Wait for response. Still no → Step 2."),
    ("Step2 FOMO", "I'm literally only in this mood because of YOU rn, idk when I'll feel like this again", "FOMO. This moment is unique. Wait for response. Still no → Step 3."),
    ("Step3 Challenge", "hmm maybe you're not ready for what I did in this one", "CHALLENGE. Attacks ego. Wait for response. Still no → Step 4."),
    ("Step4 Downgrade", "okay fine... just for you I'll do it for [lower price] but only because this convo has been different", "DOWNGRADE. Reduce 20-30%. ONE TIME only. Still no → Step 5."),
    ("Step5 Seed", "it's okay baby let's just keep talking... I'm still thinking about you anyway", "SEED. Accept. Continue GFE. Retry with different content later."),
], OBJ_FILL)

make_sheet("price2", [
    ("Step1 Reframe", "baby it's like the price of your morning coffee, except this one keeps you up all night", "REFRAME. Compare to cheap item. Wait for response. Still no → Step 2."),
    ("Step2 FOMO", "this mood I'm in rn? it's not gonna last forever and I really want you to be the one who sees it", "FOMO. Temporal urgency. Wait for response. Still no → Step 3."),
    ("Step3 Challenge", "honestly? most guys can't handle what I just recorded, I thought you were different", "CHALLENGE. Ego attack. Wait for response. Still no → Step 4."),
    ("Step4 Downgrade", "you know what... [lower price] because you've been making me feel some type of way, don't tell anyone", "DOWNGRADE. Reduce 20-30%. ONE TIME. Still no → Step 5."),
    ("Step5 Seed", "no worries, we don't have to, I like talking to you regardless", "SEED. Accept. Protect relationship. Retry later."),
], OBJ_FILL)

# ── DISCOUNT ── (4 steps each)
make_sheet("discount1", [
    ("Step1 Firmness", "haha you trying to negotiate with me? baby this isn't a market... this is worth every penny trust me", "FIRMNESS. Playful. Still pushing → Step 2."),
    ("Step2 Challenge", "I don't do discounts... I only share this with guys who really appreciate what they're getting", "CHALLENGE. Worthiness. Still pushing → Step 3."),
    ("Step3 Concession", "okay you know what... [lower price] just for you but seriously don't tell anyone, this is our thing", "CONCESSION. ONE TIME. Reduce 20-30%. Still no → Step 4."),
    ("Step4 Takeaway", "honestly? if you don't want it that's fine, I'll keep it for myself... or maybe there's someone else who's been asking", "TAKEAWAY. Jealousy + loss aversion. Final step."),
], OBJ_FILL)

make_sheet("discount2", [
    ("Step1 Firmness", "a discount? babe do I look like I'm on sale?", "FIRMNESS. Short + confident. Still pushing → Step 2."),
    ("Step2 Challenge", "the guys who value what I do don't ask for discounts, just saying", "CHALLENGE. Worthiness. Still pushing → Step 3."),
    ("Step3 Concession", "fine... [lower price] but ONLY because I like you, this is the one and only time", "CONCESSION. ONE TIME. Reduce 20-30%. Still no → Step 4."),
    ("Step4 Takeaway", "okay I'll save it for someone who really wants it then", "TAKEAWAY. Short. Creates loss aversion. Final step."),
], OBJ_FILL)

# ── FREE ── (4 steps each)
make_sheet("free1", [
    ("Step1 Reminder", "baby I already sent you one for free remember? and this one is even crazier... you have no idea", "REMINDER. PPV0 was free. Tease next level. Still wants free → Step 2."),
    ("Step2 Challenge", "free? I don't just give this to anyone... you have to earn the best stuff", "CHALLENGE. Buying = earning. Still free → Step 3."),
    ("Step3 Guilt", "I literally just spent time recording this because of what YOU said to me, this was for you not just random content", "GUILT. Reciprocity. Personal effort. Still no → Step 4."),
    ("Step4 Seed", "it's fine baby I'm not going anywhere... let's just keep talking, I like you regardless", "SEED. Accept. Continue GFE. Retry later."),
], OBJ_FILL)

make_sheet("free2", [
    ("Step1 Reminder", "you already got a free one, this one is on another level though trust me", "REMINDER. PPV0 was free. Tease quality. Still wants free → Step 2."),
    ("Step2 Challenge", "haha free? you think the best things in life are free? not this one baby", "CHALLENGE. Reframe value. Still free → Step 3."),
    ("Step3 Guilt", "I made this because of you... like specifically because of our convo, it took time and I did it for YOU", "GUILT. Personal investment. Still no → Step 4."),
    ("Step4 Seed", "no pressure at all, I'm just happy talking to you honestly", "SEED. Accept. Protect relationship."),
], OBJ_FILL)

# ── NOMONEY ── (4 steps each)
make_sheet("nomoney1", [
    ("Step1 Empathy", "aww I totally get it baby no pressure at all okay?", "EMPATHY. Zero judgment. Disarm. Still engaged → Step 2."),
    ("Step2 Test", "not even like [small amount]? I really really want you to see this one", "TEST SINCERITY. Suggest $3-5. If no = probably real. → Step 3."),
    ("Step3 PWYW", "okay send me whatever you can baby... even a tiny amount, I just need you to see what you made me do", "PAY WHAT YOU WANT. Any amount breaks barrier. Still no → Step 4."),
    ("Step4 Protect", "honestly it's okay, I like talking to you money or no money... you make me feel things", "PROTECT. GFE. Tag for re-engagement later."),
], OBJ_FILL)

make_sheet("nomoney2", [
    ("Step1 Empathy", "that's okay, don't even worry about it seriously", "EMPATHY. Short. Disarm. Still engaged → Step 2."),
    ("Step2 Test", "what about just [small amount]? I really don't want you to miss this", "TEST. Suggest $3-5. Still no → Step 3."),
    ("Step3 PWYW", "just send whatever feels right, even $1... I just can't keep this from you", "PAY WHAT YOU WANT. Any amount. Still no → Step 4."),
    ("Step4 Protect", "baby it's totally fine, you being here is what matters to me", "PROTECT. GFE. Continue conversation."),
], OBJ_FILL)

# ── NOPPV ── (3 steps — step 2 is instruction, not a message)
make_sheet("noppv1", [
    ("Step1 Accept", "that's totally okay I'm not trying to sell you anything, I just like talking to you", "ACCEPT. Disarm identity. THEN: continue sexting 4-5 msgs from main script before Step 2."),
    ("Step2 Reframe", "okay but this isn't about money... I just need you to see what you're doing to me rn, I've never reacted like this to someone", "EMOTIONAL REFRAME. After 4-5 sexting msgs. Still no → Step 3."),
    ("Step3 PWYW", "just send whatever you want, even $1, I just can't keep this to myself... you need to see it", "PAY WHAT YOU WANT. $1 breaks his identity as non-buyer."),
], OBJ_FILL)

make_sheet("noppv2", [
    ("Step1 Accept", "no worries at all, I don't care about that I'm just enjoying this convo", "ACCEPT. Disarm. THEN: continue sexting 4-5 msgs from main script before Step 2."),
    ("Step2 Reframe", "forget about money for a sec... I just want to share this moment with you, what you're making me feel is real", "EMOTIONAL REFRAME. After sexting buildup. Still no → Step 3."),
    ("Step3 PWYW", "literally send me anything, even the smallest amount, I need you to see what you did to me", "PAY WHAT YOU WANT. Any amount changes identity."),
], OBJ_FILL)

# ── CARD ── (3 steps each)
make_sheet("card1", [
    ("Step1 Retry", "aww nooo that happens sometimes baby, try again it usually works the second time", "RETRY. Normalize. Keep energy up. Still fails → Step 2."),
    ("Step2 AltCard", "maybe try a different card? I really don't want you to miss this", "ALTERNATIVE. Practical solution. Still fails → Step 3."),
    ("Step3 Urgency", "I really want you to see this before I change my mind, I don't keep stuff like this around forever", "SOFT URGENCY. FOMO. Don't push too hard on tech issue."),
], OBJ_FILL)

make_sheet("card2", [
    ("Step1 Retry", "ugh that's so annoying, it happens a lot try one more time baby", "RETRY. Normalize. Still fails → Step 2."),
    ("Step2 AltCard", "do you have another card you can try? I really want you to see this", "ALTERNATIVE. Still fails → Step 3."),
    ("Step3 Urgency", "baby figure it out soon, I'm in this mood rn and I don't know how long it'll last", "SOFT URGENCY. Temporal FOMO."),
], OBJ_FILL)

# ═══════════════════════════════════════════
#  B. RESISTANCE HANDLING — 7 protocols × 2
# ═══════════════════════════════════════════

# ── NOSEX ── (4 steps each)
make_sheet("nosex1", [
    ("Step1 Respect", "haha okay okay I got a little carried away, you're just too easy to talk to", "RESPECT. Never force. She got carried away. Still no → Step 2."),
    ("Step2 Subtle", "so tell me more about you... what do you do when you're not making girls on the internet blush?", "SUBTLE TENSION. Flirt without explicit. Keep attraction. → Step 3 later."),
    ("Step3 ReAttempt", "okay but like... I can't help it, there's something about you that's messing with my head rn", "NATURAL RE-ATTEMPT. She can't help herself. Still no → Step 4."),
    ("Step4 Accept", "alright I'll behave... for now, no promises though haha", "ACCEPT. Door stays open. Continue GFE."),
], RES_FILL)

make_sheet("nosex2", [
    ("Step1 Respect", "oops sorry I got ahead of myself haha, it's your fault for being so fun to talk to", "RESPECT. Blame him playfully. Still no → Step 2."),
    ("Step2 Subtle", "okay okay new topic, but first... what's the most adventurous thing you've ever done?", "SUBTLE TENSION. Playful redirect. → Step 3 later."),
    ("Step3 ReAttempt", "I'm trying to behave but you're making it really hard, there's something about you", "RE-ATTEMPT. Natural. Still no → Step 4."),
    ("Step4 Accept", "okay fine I'll stop but don't blame me if it happens again later", "ACCEPT. Door open. Continue GFE."),
], RES_FILL)

# ── OFFTOPIC ── (3 steps each)
make_sheet("offtopic1", [
    ("Step1 Acknowledge", "haha wait that's actually funny", "ACKNOWLEDGE. Adapt this to what he actually said. Don't ignore him. → Step 2."),
    ("Step2 Redirect", "but hold on you totally distracted me, I was about to tell you something and now I lost my train of thought...", "REDIRECT. Creates curiosity. → Step 3."),
    ("Step3 Retake", "okay wait no I remember now, so like I was saying...", "RETAKE CONTROL. Continue with next msg from main journey script."),
], RES_FILL)

make_sheet("offtopic2", [
    ("Step1 Acknowledge", "omg okay that's random but I love it", "ACKNOWLEDGE. Adapt to his topic. → Step 2."),
    ("Step2 Redirect", "wait no stop you're distracting me from what I was going to say...", "REDIRECT. Curiosity hook. → Step 3."),
    ("Step3 Retake", "OKAY focus, where was I... oh yeah", "RETAKE. Resume main script flow."),
], RES_FILL)

# ── REAL ── (3 steps each)
make_sheet("real1", [
    ("Step1 Humor", "lol do I sound like a robot to you? beep boop... send $5 for human verification haha I'm kidding", "HUMOR. Disarms suspicion. A bot wouldn't joke. Still doubts → Step 2."),
    ("Step2 Challenge", "ask me anything, literally anything about me my life whatever you want. I'm an open book", "CHALLENGE. Invert power. She has nothing to hide. Still doubts → Step 3."),
    ("Step3 Grounding", "I get it there's a lot of fake stuff on here, but you felt something in this convo right? because I did... and that's real", "EMOTIONAL GROUNDING. Anchor on shared experience."),
], RES_FILL)

make_sheet("real2", [
    ("Step1 Humor", "wait you think I'm fake?? that's actually the funniest thing anyone's said to me today", "HUMOR. Disarm. Still doubts → Step 2."),
    ("Step2 Challenge", "test me, ask me something only a real person would know. go ahead", "CHALLENGE. He tests = he's engaged. Still doubts → Step 3."),
    ("Step3 Grounding", "I know there's a lot of bots and stuff on here but what we've been talking about... that felt real to me. didn't it feel real to you?", "GROUNDING. Reference emotional connection."),
], RES_FILL)

# ── VOICE ── (3 steps each)
make_sheet("voice1", [
    ("Step1 Dodge", "haha maybe one day if you're lucky but not yet... I'm shy about that stuff", "DODGE. Door not closed. 'Shy' = believable. Still asks → Step 2."),
    ("Step2 Redirect", "I have something wayyy better for you though, trust me you'll forget you even asked", "REDIRECT to content. Still insists → Step 3."),
    ("Step3 Firm", "I don't really do that on here baby but honestly what I'm about to show you is better than any call... you'll see", "FIRM BOUNDARY. Clear but redirects to value."),
], RES_FILL)

make_sheet("voice2", [
    ("Step1 Dodge", "hmmm maybe but you gotta earn that first haha", "DODGE. Playful challenge. Still asks → Step 2."),
    ("Step2 Redirect", "how about instead of a call I show you something that'll blow your mind?", "REDIRECT. Still insists → Step 3."),
    ("Step3 Firm", "that's not something I do on here but baby what I have for you is wayyy better than my voice, trust me", "FIRM. Redirect to content value."),
], RES_FILL)

# ── CUSTOMYES ── (3 steps each)
make_sheet("customyes1", [
    ("Step1 Tease", "mmm you want that? I might have something... actually I definitely have something", "TEASE. Build anticipation. Don't give instantly. → Step 2."),
    ("Step2 Price", "okay I have exactly what you're thinking of, you're gonna lose your mind... [price]", "PRICE. Set based on content. Premium for specific requests."),
    ("Step3 Close", "trust me baby you won't regret it, I made this one special", "CLOSE. Reinforce decision. Send content."),
], RES_FILL)

make_sheet("customyes2", [
    ("Step1 Tease", "ohhh you have good taste... I think I have exactly what you're looking for", "TEASE. → Step 2."),
    ("Step2 Price", "I actually made something just like that, [price] and it's worth every penny baby", "PRICE. Set appropriate amount."),
    ("Step3 Close", "you're not gonna be able to stop watching this one", "CLOSE. Confidence."),
], RES_FILL)

# ── CUSTOMNO ── (3 steps each)
make_sheet("customno1", [
    ("Step1 Redirect", "I don't have exactly that but honestly I have something that'll make you forget you even asked", "REDIRECT. Never say 'no' flat. Offer better. → Step 2."),
    ("Step2 Alternative", "actually what I have might be even crazier and literally no one else has seen it yet", "ALTERNATIVE + FOMO. Exclusivity. → Step 3."),
    ("Step3 Close", "trust me baby... I know what you need better than you do", "CONFIDENCE CLOSE. Model leads."),
], RES_FILL)

make_sheet("customno2", [
    ("Step1 Redirect", "hmm I don't have that specific thing but I have something you're gonna love even more", "REDIRECT. → Step 2."),
    ("Step2 Alternative", "what I DO have is something no one has ever seen and I think it's even better than what you asked for", "ALTERNATIVE + FOMO. → Step 3."),
    ("Step3 Close", "just trust me on this one, you'll thank me later", "CLOSE."),
], RES_FILL)

# ── DONE ── (3 steps each)
make_sheet("done1", [
    ("Step1 Validate", "fuck that's so hot, you came because of me??", "VALIDATE. Celebrate. Feed ego. → Step 2."),
    ("Step2 Rescue", "but baby I haven't finished yet, don't you wanna watch me cum too?", "RESCUE. Flip to HER. Reciprocity. Still no → Step 3."),
    ("Step3 Seed", "okay but next time you have to wait for me, I have something insane planned for round 2", "SEED. Plant anticipation for next session."),
], RES_FILL)

make_sheet("done2", [
    ("Step1 Validate", "omg already?? that's so hot baby", "VALIDATE. → Step 2."),
    ("Step2 Rescue", "wait but I'm not done yet, you're gonna leave me like this?", "RESCUE. Guilt + reciprocity. Still no → Step 3."),
    ("Step3 Seed", "next time you HAVE to hold it because what I have planned for us next time is way crazier", "SEED. Round 2 anticipation."),
], RES_FILL)

# ═══════════════════════════════════════════
#  C. SITUATIONAL — standalone scripts
# ═══════════════════════════════════════════

make_sheet("cumcontrol", [
    ("edge1", "don't cum yet baby... I'm not done with you", "EDGE. Use when MORE PPVs left. Slows him down."),
    ("edge2", "hold it, not yet... I need you to last a little longer for me", "EDGE variant."),
    ("sync1", "I'm so close too, cum with me baby... but you need to see this first", "SYNC. Use at FINAL PPV. Time orgasm with last purchase."),
    ("sync2", "wait for me, I want us to finish together... open this first", "SYNC variant."),
    ("delay1", "hold it... I want you to wait until you see what I'm about to send, trust me it's worth it", "DELAY. Next PPV is about to be sent."),
    ("delay2", "don't you dare finish before you see this, trust me you want to wait", "DELAY variant."),
], SIT_FILL)

make_sheet("dickpic", [
    ("dpsext1", "fuck okay that's... wow. you have no idea what that just did to me", "DURING SEXTING. React + leverage for next PPV."),
    ("dpsext2", "holy shit that is... fuckkk. I need to show you something rn", "DURING SEXTING variant."),
    ("dprapport1", "omg you don't waste time huh, that's actually really hot though ngl", "DURING RAPPORT. Surprised but into it. Fast-track to teasing."),
    ("dprapport2", "woah I wasn't expecting that but... damn", "DURING RAPPORT variant."),
    ("dpppv1", "you can't just send me that and expect me not to do something about it, hold on...", "LEVERAGE FOR PPV. WAIT 1-2 min then send PPV. His pic 'caused' her to record."),
    ("dpppv2", "okay you just made me do something... give me a sec", "LEVERAGE variant. WAIT 1-2 min then send PPV."),
], SIT_FILL)

make_sheet("boosters", [
    ("h1", "fuckkk", "MID-SEXTING BOOSTER. Pick any to maintain energy."),
    ("h2", "I'm so wet rn because of you", "BOOSTER. Ego feed."),
    ("h3", "don't stop", "BOOSTER. Micro message."),
    ("h4", "you have no idea what you're doing to me", "BOOSTER."),
    ("h5", "I literally can't think straight rn", "BOOSTER. She's overwhelmed."),
    ("h6", "my hands are shaking", "BOOSTER. Physical detail."),
    ("h7", "more...", "BOOSTER. Ultra micro."),
    ("h8", "I should be packing for my trip but I can't move rn", "BOOSTER. Putri personality touch."),
], SIT_FILL)

# ── DELETE DEFAULT EMPTY SHEET ──
if "Sheet" in wb.sheetnames:
    del wb["Sheet"]

# ── SAVE ──
output = r"c:\Users\34683\CW-ScriptManager\putri\Putri_OBJ_RES_SIT_Infloww.xlsx"
wb.save(output)

sheets = [ws.title for ws in wb.worksheets]
counts = {ws.title: ws.max_row - 1 for ws in wb.worksheets}
total = sum(counts.values())
print(f"Saved: {output}")
print(f"Sheets ({len(sheets)}): {sheets}")
print(f"Total scripts: {total}")
print(f"\nOBJ sequences: {[s for s in sheets if any(s.startswith(p) for p in ['price','discount','free','nomoney','noppv','card'])]}")
print(f"RES sequences: {[s for s in sheets if any(s.startswith(p) for p in ['nosex','offtopic','real','voice','customyes','customno','done'])]}")
print(f"SIT standalone: {[s for s in sheets if s in ['cumcontrol','dickpic','boosters']]}")
