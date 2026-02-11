"""
Display Max Dating App Journey — Visual Terminal View
Run: python tools/display_journey.py
"""
import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.columns import Columns
from rich.tree import Tree
from rich import box

console = Console(width=130)

# ─── HEADER ───
console.print()
console.rule("[bold bright_cyan]MAX — DATING APP WELCOME JOURNEY v1[/]", style="bright_cyan")
console.print()

header_info = Table(show_header=False, box=None, padding=(0, 2))
header_info.add_column(style="dim")
header_info.add_column(style="bold white")
header_info.add_row("Traffic source", "Dating Apps (Gay Male — Explicit Meetup Promise)")
header_info.add_row("Content set", "First Session (Solo)")
header_info.add_row("Script mode", "Autopilot-safe")
header_info.add_row("Template for", "All dating app male creators")
console.print(Panel(header_info, title="[bold]Info[/]", border_style="dim", width=70))
console.print()

# ─── CHARACTER PROFILE ───
console.rule("[bold yellow]CHARACTER PROFILE[/]", style="yellow")
console.print()

profile = Table(show_header=False, box=box.SIMPLE_HEAVY, border_style="yellow", padding=(0, 1))
profile.add_column("Attr", style="bold yellow", width=14)
profile.add_column("Detail", style="white", max_width=90)
profile.add_row("Name", "Max (MaxDoms)")
profile.add_row("Age", "20")
profile.add_row("Origin", "Rome, Italy")
profile.add_row("Location", "Austin, TX  ⚠️  Dating apps: matches fan's location")
profile.add_row("Personality", "Alpha, dominant, confident, direct, sweet/protective + provocative")
profile.add_row("Physical", "1.85m, 90kg, athletic, tanned, dark brown hair, green eyes, 16 tattoos")
profile.add_row("Interests", "Gym & boxing 5-6x/week, fashion, nightlife, motorcycles, travel, luxury")
profile.add_row("Voice", 'Lowercase. Direct. Short. "bro/dude/man". NEVER "baby/babe". CAPS at peak only.')
console.print(profile)
console.print()

# ─── JOURNEY FLOW ───
console.rule("[bold bright_green]JOURNEY FLOW[/]", style="bright_green")
console.print()

tree = Tree("[bold bright_green]📥 FAN SUBSCRIBES[/]", guide_style="bright_green")

w = tree.add("[bold white]W-1[/] Welcome + photos  [dim](auto)[/]")
w.add("[dim]⏱️  2-3 min[/]")

af = tree.add("[bold white]AF-1 → AF-2[/] Auto follow-ups  [dim](auto, ask name)[/]")
af.add("[dim]⏱️  Wait for response[/]")

branch = tree.add("[bold bright_yellow]⚡ BRANCH — Based on first response[/]")

mr_path = branch.add("[bold red]🚨 MEETING REQUEST[/] → MR-1 to MR-4 [dim](delivers PPV 0)[/]")
mr_path.add("→ R-1 to R-5 [dim](full rapport)[/]")
mr_path.add("→ TB-1 + TB-2 [dim](skip TB-3 to TB-5)[/]")
mr_path.add("→ [bold bright_green]S1 Sexting[/]")

sex_path = branch.add("[bold magenta]🔥 SEXUAL/FLIRTY[/] → TB-1 to TB-5 [dim](fast-track, PPV 0)[/]")
sex_path.add("→ [bold bright_green]S1 Sexting[/]")

normal_path = branch.add("[bold cyan]💬 NORMAL/CASUAL[/] → R-1 to R-5 → TB-1 to TB-5 [dim](PPV 0)[/]")
normal_path.add("→ [bold bright_green]S1 Sexting[/]")

silent_path = branch.add("[dim]🔇 SILENT[/] → NR-W1 to NR-W5")

sexting = tree.add("[bold bright_green]S1-1 to S1-22[/] Sexting Sequence [dim](PPV 1→2→3→4)[/]")
sexting.add("[bold green]$12[/] → [bold green]$25[/] → [bold green]$40[/] → [bold green]$55[/] = [bold bright_green]$132 potential[/]")

ac = tree.add("[bold bright_blue]AC-1 to AC-3[/] Aftercare + Seed")

console.print(Panel(tree, border_style="bright_green", padding=(1, 2)))
console.print()

# ─── WELCOME + AUTO FOLLOW-UPS ───
console.rule("[bold white]WELCOME + AUTO FOLLOW-UPS[/]", style="white")
console.print()

t = Table(box=box.ROUNDED, border_style="white", show_lines=True, width=125)
t.add_column("Cmd", style="bold cyan", width=6)
t.add_column("Message", style="white", width=65)
t.add_column("Note", style="dim", width=45)
t.add_row("W-1", "yo what's up 😏 glad you're here. got something for\nyou before I hit the gym", "Auto-send + Album (5-10 fotos)")
t.add_row("AF-1", "ngl I was about to go train but I keep checking if\nyou replied 😏 that never happens", "Auto 2-3 min after W-1")
t.add_row("AF-2", "yo what's your name", "Auto 1-2 min after AF-1. WAIT.\nMeeting → MR-1 | Sexual → TB-1\nNormal → R-1")
console.print(t)
console.print()

# ─── MEETUP REDIRECT ───
console.rule("[bold red]🚨 MEETUP REDIRECT (MR) — NUEVO[/]", style="red")
console.print()

console.print(Panel(
    "[bold]Cuándo:[/] Fan pide quedar/meeting/hookup\n"
    "[bold]Regla:[/] NUNCA decir 'meet', NUNCA decir 'no', NUNCA decir 'sí'. Solo redirigir.\n"
    "[bold]Entrega:[/] PPV 0 (gratis) aquí para dar valor inmediato",
    border_style="red", title="[bold red]Estrategia[/]", width=90
))
console.print()

t = Table(box=box.ROUNDED, border_style="red", show_lines=True, width=125)
t.add_column("Cmd", style="bold red", width=8)
t.add_column("Message", style="white", width=55)
t.add_column("Note", style="dim", width=50)
t.add_row("MR-1", "haha easy man 😏 slow down. let me show you\nsomething first", "NO echar la palabra 'meet'. Redirigir ya.")
t.add_row("MR-2", "trust me... you're gonna wanna see this 😈", "WAIT 1-2 MIN")
t.add_row("MR-3", "what do you think 😏", "📎 Send PPV 0 — FREE. Wait response.")
t.add_row("MR-4", "yeah? 😏 that's just a taste man", "Positivo → R-1 | Insiste meeting → MR-OBJ-1\nSilent → NR-W1")
console.print(t)
console.print()

# ─── MEETUP OBJECTION ───
t = Table(box=box.ROUNDED, border_style="bright_red", show_lines=True, width=125, title="[bold]MEETUP OBJECTION (MR-OBJ) — Si insiste en quedar[/]")
t.add_column("Step", style="bold", width=5)
t.add_column("Message", style="white", width=60)
t.add_column("Technique", style="italic bright_red", width=25)
t.add_row("1", "patience bro 😏 I don't rush. focus on what's right\nin front of you", "Deflect + Challenge")
t.add_row("2", "you really that impatient? 😈 I promise what I'm\nabout to show you is worth it", "Challenge + Tease")
t.add_row("3", "look I don't do this for just anyone. appreciate what\nyou're getting rn 💪 if that's not your thing it's cool", "Firm redirect + Takeaway")
console.print(t)
console.print("[dim italic]  → After step 3: 'no worries bro 💪 hit me up whenever'. Tag re-engagement. No más tiempo.[/]")
console.print()

# ─── RAPPORT ───
console.rule("[bold cyan]RAPPORT (Mini — 5 msgs)[/]", style="cyan")
console.print()

t = Table(box=box.ROUNDED, border_style="cyan", show_lines=True, width=125)
t.add_column("Cmd", style="bold cyan", width=6)
t.add_column("Block", style="dim", width=10)
t.add_column("Message", style="white", width=58)
t.add_column("Note", style="dim", width=40)
t.add_row("R-1", "Ice-break", "glad you're here man 😏 so be honest,\nwhat caught your eye", "Add nombre antes de 'man'")
t.add_row("R-2", "Ice-break", "haha respect 💪 so where you from?", "React antes ('haha damn', 'oh word?')")
t.add_row("R-3", "Vibe", "nice. I'm from Rome originally but I moved to the\nstates a couple years ago. gym and creating\ncontent is basically my life rn 😏", "Si ha visitado país de Max, add 'oh I've\nbeen there'")
t.add_row("R-4", "Vibe", "so what do you do besides making me check\nmy phone every 5 seconds 😏", "")
t.add_row("R-5", "Heat", "I gotta say... you're actually fun to talk to.\nmost guys on here are boring as fuck 😏", "Ego boost. Next → TB-1.\nMR path: TB-1+TB-2 then → S1-1")
console.print(t)
console.print()

# ─── TEASING BRIDGE ───
console.rule("[bold magenta]TEASING BRIDGE (5 msgs — PPV 0)[/]", style="magenta")
console.print()

t = Table(box=box.ROUNDED, border_style="magenta", show_lines=True, width=125)
t.add_column("Cmd", style="bold magenta", width=6)
t.add_column("Message", style="white", width=58)
t.add_column("Note", style="dim", width=50)
t.add_row("TB-1", "just got back from training and I'm still pumped...\nthis convo is making it worse 😏", "⚡ THE PIVOT")
t.add_row("TB-2", "ngl I'm feeling some type of way rn 😈\nyou ever get that?", "Wait for response.\n[bold]MR path: skip to S1-1 after this[/]")
t.add_row("TB-3", "fuck... you're not helping me calm down 🥵", "If sexual msg, add 'especially after what\nyou just said'")
t.add_row("TB-4", "hold on let me show you something 😏", "WAIT 1-2 MIN")
t.add_row("TB-5", "tell me what you think 😏", "📎 Send PPV 0 — FREE. Wait response.\nBought vibe → S1-1 | Silent → NR-W1")
console.print(t)
console.print()

# ─── SEXTING SEQUENCE ───
console.rule("[bold bright_green]🔥 SEXTING SEQUENCE — PPV 1 to PPV 4[/]", style="bright_green")
console.print()

# Intensity bar helper
def intensity_bar(level, max_level=10):
    filled = "█" * level
    empty = "░" * (max_level - level)
    if level <= 5:
        color = "green"
    elif level <= 7:
        color = "yellow"
    elif level <= 8:
        color = "bright_red"
    else:
        color = "red"
    return f"[{color}]{filled}[/][dim]{empty}[/] {level}/10"

# Phase 1
console.print("[bold yellow]Phase 1: Build to PPV 1  ($12)[/]")
t = Table(box=box.ROUNDED, border_style="yellow", show_lines=True, width=125)
t.add_column("Cmd", style="bold", width=6)
t.add_column("Message", style="white", width=45)
t.add_column("Note", style="dim", width=38)
t.add_column("🔥", width=20, no_wrap=True)
t.add_row("S1-1", "so 😏", "Wait for response", intensity_bar(5))
t.add_row("S1-2", "knew you'd like it 😈", "React to what he said", intensity_bar(6))
t.add_row("S1-3", "you wanna see more? I'm feeling\ngenerous rn", "", intensity_bar(7))
t.add_row("S1-4", "hold on... give me a sec 😏", "⏱️ WAIT 2-3 MIN", intensity_bar(7))
t.add_row("S1-5", "you're not ready for this 🥵", "📎 PPV 1 — $12\n✅→S1-6 | 🔇→NR | ❌→OBJ", intensity_bar(8))
console.print(t)
console.print()

# Phase 2
console.print("[bold bright_red]Phase 2: Build to PPV 2  ($25)[/]")
t = Table(box=box.ROUNDED, border_style="bright_red", show_lines=True, width=125)
t.add_column("Cmd", style="bold", width=6)
t.add_column("Message", style="white", width=45)
t.add_column("Note", style="dim", width=38)
t.add_column("🔥", width=20, no_wrap=True)
t.add_row("S1-6", "you watched it? 😏", "Wait response. Brief cooldown.", intensity_bar(6))
t.add_row("S1-7", "fuck... talking to you is doing\nsomething to me rn 🥵", "React. Sexual vulnerability —\nHE caused this.", intensity_bar(8))
t.add_row("S1-8", "I'm hard as fuck because of you\nand I can't do anything about it", "", intensity_bar(8))
t.add_row("S1-9", "what would you do if you were\nhere rn", "Wait response. 🎯 REACTION SLOT", intensity_bar(8))
t.add_row("S1-10", "fuck 🥵🥵 hold on I need to show\nyou something", "⏱️ WAIT 2-3 MIN", intensity_bar(9))
t.add_row("S1-11", "look what you did to me 🥵", "📎 PPV 2 — $25\n✅→S1-12 | 🔇→NR | ❌→OBJ", intensity_bar(9))
console.print(t)
console.print()

# Phase 3
console.print("[bold red]Phase 3: Build to PPV 3  ($40)  ⚡ NO COOLDOWN[/]")
t = Table(box=box.ROUNDED, border_style="red", show_lines=True, width=125)
t.add_column("Cmd", style="bold", width=6)
t.add_column("Message", style="white", width=45)
t.add_column("Note", style="dim", width=38)
t.add_column("🔥", width=20, no_wrap=True)
t.add_row("S1-12", "🥵🥵", "Wait response. NO cooldown.", intensity_bar(9))
t.add_row("S1-13", "I need to cum so bad rn you have\nno idea", "", intensity_bar(9))
t.add_row("S1-14", "imagine me pinning you down and\nmaking you take every inch while\nyou're begging for more 🥵", "", intensity_bar(10))
t.add_row("S1-15", "fuck I can't hold back anymore", "", intensity_bar(10))
t.add_row("S1-16", "give me a sec 🥵", "⏱️ WAIT 2-3 MIN", intensity_bar(10))
t.add_row("S1-17", "I've never gone this far for\nanyone... watch 🥵💦", "📎 PPV 3 — $40\n'Never done this' = 1/2 max\n✅→S1-18 | 🔇→NR | ❌→OBJ", intensity_bar(10))
console.print(t)
console.print()

# Phase 4
console.print("[bold bright_red on white] Phase 4: CLIMAX — PPV 4  ($55) [/]")
t = Table(box=box.ROUNDED, border_style="bright_red", show_lines=True, width=125)
t.add_column("Cmd", style="bold", width=6)
t.add_column("Message", style="white", width=45)
t.add_column("Note", style="dim", width=38)
t.add_column("🔥", width=20, no_wrap=True)
t.add_row("S1-18", "FUCK 🥵🥵", "Wait response", intensity_bar(10))
t.add_row("S1-19", "don't cum yet", "", intensity_bar(10))
t.add_row("S1-20", "I wanna finish with you...\nI'm close", "", intensity_bar(10))
t.add_row("S1-21", "fuck fuck hold on 🥵", "⏱️ WAIT 1-2 MIN", intensity_bar(10))
t.add_row("S1-22", "cum with me 💦😈", "📎 PPV 4 — $55\n✅→AC-1 | 🔇→NR", intensity_bar(10))
console.print(t)
console.print()

# ─── NR WAVES ───
console.rule("[bold bright_yellow]NO RESPONSE — Wave System[/]", style="bright_yellow")
console.print()

t = Table(box=box.ROUNDED, border_style="bright_yellow", show_lines=True, width=125)
t.add_column("Wave", style="bold bright_yellow", width=6)
t.add_column("Timing", style="dim", width=16)
t.add_column("Message", style="white", width=55)
t.add_column("Technique", style="italic", width=15)
t.add_row("W1", "2-3 min", "yo? 🥵", "Ping")
t.add_row("W2", "3-5 min later", "you need to see what I just did... seriously 🥵", "Curiosity")
t.add_row("W3", "5-10 min later", "aight I guess you're busy 😏 might delete this, it was only for you", "Takeaway")
t.add_row("W4", "15-30 min later", "hey hope you're good bro 💪 hit me up when you're back", "Warm close")
t.add_row("W5", "2-6 hrs later", "can't stop thinking about earlier 😏 you around?", "New convo")
console.print(t)
console.print()

# ─── OBJECTION PROTOCOLS ───
console.rule("[bold bright_magenta]OBJECTION PROTOCOLS[/]", style="bright_magenta")
console.print()

# Too Expensive
t = Table(box=box.ROUNDED, border_style="bright_magenta", show_lines=True, width=125, title='[bold]"TOO EXPENSIVE" (max 6 steps)[/]')
t.add_column("#", style="bold", width=3)
t.add_column("Message", style="white", width=65)
t.add_column("Technique", style="italic bright_magenta", width=20)
t.add_column("+/-", width=5, justify="center")
t.add_row("1", "bro this is like 3 minutes of me going all out...\nyou spend more than this on a night out 😏", "Reframe", "[green]+[/]")
t.add_row("2", "alright I'll do $[price] but ONLY this once.\ndon't get used to it 😏", "Discount (1x)", "[green]+[/]")
t.add_row("3", "I'm in this mood rn... can't promise I'll feel like\nthis again anytime soon 😈", "FOMO temporal", "[red]-[/]")
t.add_row("4", "maybe you can't handle what I did in this one 😏", "Challenge", "[red]-[/]")
t.add_row("5", "your loss man 😏 I'll keep it for someone who\nactually wants it", "Takeaway", "[red]-[/]")
t.add_row("6", "that video tho? just watched it again and fuck 🥵\nlast chance before I delete it", "Seed + Return", "[red]-[/]")
console.print(t)
console.print()

# Send Free
t = Table(box=box.ROUNDED, border_style="bright_magenta", show_lines=True, width=125, title='[bold]"SEND FREE FIRST" (max 4 steps)[/]')
t.add_column("#", style="bold", width=3)
t.add_column("Message", style="white", width=65)
t.add_column("Technique", style="italic bright_magenta", width=20)
t.add_row("1", "I already gave you a free one man 😏 this one is on a whole different level... trust me", "Reminder")
t.add_row("2", "tell you what... $[price]. but you better actually watch it 😏", "Downgrade")
t.add_row("3", "maybe you're not ready for what I really do 😈 it's intense", "Challenge")
t.add_row("4", "trust me bro... what I did in that video? worth every cent 🥵", "Seed + Return")
console.print(t)
console.print()

# Don't buy
t = Table(box=box.ROUNDED, border_style="bright_magenta", show_lines=True, width=125, title='[bold]"I DON\'T BUY PPVs" (max 4 steps)[/]')
t.add_column("#", style="bold", width=3)
t.add_column("Message", style="white", width=65)
t.add_column("Technique", style="italic bright_magenta", width=20)
t.add_row("1", "all good man 😏 no pressure", "Accept")
t.add_row("2", "[dim][Continue explicit text sexting 4-5 msgs — build tension][/]", "Build tension")
t.add_row("3", "fuck... ok I need to show you something. this isn't about money,\nI literally need you to see what you're doing to me rn 🥵", "Emotional reframe")
t.add_row("4", "send whatever you want, I don't care about the price...\nI just need you to watch this 🥵", "Pay what you want")
console.print(t)
console.print()

# Are you real
t = Table(box=box.ROUNDED, border_style="bright_magenta", show_lines=True, width=125, title='[bold]"ARE YOU REAL?" (max 3 steps)[/]')
t.add_column("#", style="bold", width=3)
t.add_column("Message", style="white", width=65)
t.add_column("Technique", style="italic bright_magenta", width=20)
t.add_row("1", "haha bro 😂 you think a bot gets this hard? come on", "Humor")
t.add_row("2", "ask me anything man. go ahead 😏", "Challenge")
t.add_row("3", "I get it, there's a lot of fake stuff on here. but you felt that right?\n💪 let's not overthink this", "Grounding")
console.print(t)
console.print()

# Chat only
t = Table(box=box.ROUNDED, border_style="bright_magenta", show_lines=True, width=125, title='[bold]CHAT-ONLY SUB (max 4 steps)[/]')
t.add_column("#", style="bold", width=3)
t.add_column("Message", style="white", width=65)
t.add_column("Technique", style="italic bright_magenta", width=20)
t.add_row("1", "bro I made this just for you, it would mean a lot if you watched it 💪", "Guilt/investment")
t.add_row("2", "I spent like 10 minutes doing this thinking about YOU...\nat least open it? 😏", "Investment amplif.")
t.add_row("3", "most guys who watch this come back saying it's the best thing\nthey've ever seen on here 😏", "Social proof")
t.add_row("4", "hm I guess you just can't handle what I got 😏\nthat's alright, not everyone can", "Challenge")
console.print(t)
console.print()

# ─── AFTERCARE ───
console.rule("[bold bright_blue]AFTERCARE + RE-ENGAGEMENT[/]", style="bright_blue")
console.print()

t = Table(box=box.ROUNDED, border_style="bright_blue", show_lines=True, width=125)
t.add_column("Cmd", style="bold bright_blue", width=6)
t.add_column("Message", style="white", width=60)
t.add_column("Note", style="dim", width=45)
t.add_row("AC-1", "holy fuck 🥵 that was insane", "")
t.add_row("AC-2", "ngl you're different from most guys on here 💪\nthat was intense", "Mencionar algo específico de la sesión")
t.add_row("AC-3", "I gotta crash but next time? I got something\nway crazier for you 😈 later bro", "END. Seed next session.")
t.add_row("", "", "")
t.add_row("RE-1", "can't stop thinking about earlier 😏 you free?", "6-12 horas después")
t.add_row("RE-2", "remember what I said about something crazier?\nI just did it and you need to see this 😈", "Día siguiente")
console.print(t)
console.print()

# ─── SUMMARY ───
console.rule("[bold bright_cyan]RESUMEN[/]", style="bright_cyan")
console.print()

summary = Table(box=box.DOUBLE_EDGE, border_style="bright_cyan", show_lines=True, width=80)
summary.add_column("Módulo", style="bold", width=25)
summary.add_column("Msgs", justify="center", width=6)
summary.add_column("Revenue", justify="right", style="bold green", width=12)
summary.add_column("Novedad", width=20)
summary.add_row("Welcome + AF", "3", "", "")
summary.add_row("[red]Meetup Redirect[/]", "4", "", "[bold red]⭐ NUEVO[/]")
summary.add_row("[red]Meetup Objection[/]", "3", "", "[bold red]⭐ NUEVO[/]")
summary.add_row("Rapport (mini)", "5", "", "Más corto (5 vs 9)")
summary.add_row("Teasing Bridge", "5", "FREE", "")
summary.add_row("Sexting (PPV 1-4)", "22", "$132", "Gay male dynamics")
summary.add_row("NR Waves", "5", "", "")
summary.add_row("Objection Protocols", "21", "", "Voz alpha")
summary.add_row("Aftercare + Re-eng", "5", "", "")
summary.add_row("[bold]TOTAL[/]", "[bold]73[/]", "[bold bright_green]$132[/]", "")
console.print(summary)
console.print()

# Key rules
rules_text = (
    "[bold red]1.[/] NUNCA decir 'meet/meeting/hookup' en OF\n"
    "[bold red]2.[/] NUNCA usar 'baby/babe/honey' — solo 'bro/dude/man'\n"
    "[bold red]3.[/] PPV 0 se entrega en MR (meeting seekers) o TB (otros)\n"
    "[bold red]4.[/] Monetizar RÁPIDO — dating app traffic churna antes\n"
    "[bold red]5.[/] Max SIEMPRE lidera. Alpha. Nunca pide permiso."
)
console.print(Panel(rules_text, title="[bold red]⚠️  REGLAS CRÍTICAS[/]", border_style="red", width=65))
console.print()
console.rule("[dim]End of journey display[/]", style="dim")
console.print()
