"""
Round 3 — Phase 4 rewrite. Make S1-18/S1-19/S1-20/S1-22 genuinely 10/10.

Problem: Phase 4 messages are LESS graphic than Phase 3.
- Phase 3 has: "touching my pussy", "fingers deeper and faster" (9/10 graphic)
- Phase 4 has: "shaking and can't hold on", "building everywhere" (8-9 reactions)

Fix: Phase 4 = CLIMAX. Must be "No filter. Graphic. Orgasm. Raw as possible."
- Explicit body parts (pussy throbbing, clenching)
- Physical climax descriptions (cumming, dripping, pulsing)
- Raw, unfiltered reactions
"""
import os, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

MODELS = {
    "lia":       {"arch": "A", "var": 1, "pet": "babe",  "e1": "\U0001f338", "e2": "\U0001f495"},
    "antonella": {"arch": "A", "var": 2, "pet": "babe",  "e1": "\U0001f5a4", "e2": "\U0001f49c"},
    "vera":      {"arch": "A", "var": 3, "pet": "babe",  "e1": "\U0001f970", "e2": "\U0001f495"},
    "ashley":    {"arch": "A", "var": 1, "pet": "babe",  "e1": "\U0001f495", "e2": "\U0001f60a"},
    "lana":      {"arch": "A", "var": 2, "pet": "babe",  "e1": "\U0001f495", "e2": "\u2728"},
    "maddison":  {"arch": "A", "var": 3, "pet": "Daddy", "e1": "\U0001f97a", "e2": "\U0001f495"},
    "chayla":    {"arch": "B", "var": 1, "pet": "papi",  "e1": "\U0001f525", "e2": "\U0001f60f"},
    "jasmine":   {"arch": "B", "var": 2, "pet": "papi",  "e1": "\U0001f975", "e2": "\U0001f525"},
    "eva":       {"arch": "B", "var": 3, "pet": "papi",  "e1": "\U0001f975", "e2": "\U0001f60f"},
    "fernanda":  {"arch": "B", "var": 1, "pet": "amor",  "e1": "\U0001f525", "e2": "\U0001f60f"},
    "faby":      {"arch": "B", "var": 2, "pet": "amor",  "e1": "\U0001f525", "e2": "\U0001f4a6"},
    "zansi":     {"arch": "B", "var": 3, "pet": "daddy", "e1": "\U0001f60f", "e2": "\U0001f525"},
    "emilybell": {"arch": "C", "var": 1, "pet": "babe",  "e1": "\U0001f60f", "e2": "\U0001f975"},
    "riri":      {"arch": "C", "var": 2, "pet": "babe",  "e1": "\U0001f975", "e2": "\U0001f60a"},
    "mialuna":   {"arch": "C", "var": 3, "pet": "babe",  "e1": "\U0001f60a", "e2": "\U0001f975"},
    "lina":      {"arch": "C", "var": 1, "pet": "babe",  "e1": "\U0001f975", "e2": "\u2728"},
    "miabrooks": {"arch": "C", "var": 2, "pet": "babe",  "e1": "\U0001f60f", "e2": "\U0001f975"},
    "jessica36": {"arch": "D", "var": 1, "pet": "amor",  "e1": "\U0001f60f", "e2": "\U0001f975"},
    "isabella":  {"arch": "D", "var": 2, "pet": "babe",  "e1": "\U0001f60f", "e2": "\U0001f975"},
    "marco":     {"arch": "E", "var": 1, "pet": "babe",  "e1": "\U0001f975", "e2": "\U0001f4a6"},
    "jockurworld": {"arch": "E", "var": 2, "pet": "bro", "e1": "\U0001f975", "e2": "\U0001f4a6"},
}

# ═══════════════════════════════════════════════════
# OLD → NEW for Phase 4 messages (S1-18, S1-19, S1-20, S1-22)
# Target: 10/10 = graphic body parts + climax + raw
# ═══════════════════════════════════════════════════
FIXES = {}

# ─── A-v1 (Lia, Ashley) — Shy, filter GONE at climax ───
FIXES[("A", 1, "S1-18")] = (
    "oh god my whole body is shaking and I can't hold on {e1}",
    "oh fuck my pussy is throbbing so hard and my whole body won't stop shaking {e1}",
)
FIXES[("A", 1, "S1-19")] = (
    "I'm so close... I can feel it building everywhere and I don't want to cum alone {e2}",
    "I can feel myself clenching around my fingers... I'm about to cum so hard {pet} please don't stop watching {e2}",
)
FIXES[("A", 1, "S1-20")] = (
    "cum with me... I'm letting go right now, watch me",
    "I'm cumming {pet}... oh god I'm cumming right now and I can feel it dripping down my fingers",
)
FIXES[("A", 1, "S1-22")] = (
    "watch me let go... this is only for you {e2}",
    "watch me cum... this is only for you {e2}",
)

# ─── A-v2 (Antonella, Lana) ───
FIXES[("A", 2, "S1-18")] = (
    "oh my god I can't stop shaking... I can feel it everywhere {e1}",
    "oh my god my pussy is pulsing so hard around my fingers and I can't stop {e1}",
)
FIXES[("A", 2, "S1-19")] = (
    "I'm right there {pet}... don't go anywhere, I need you to watch me let go {e2}",
    "I'm right there {pet}... my whole body is clenching and I need you watching when I cum {e2}",
)
FIXES[("A", 2, "S1-20")] = (
    "I'm cumming... right now... don't look away",
    "I'm cumming... fuck I'm cumming so hard right now I can barely breathe",
)
FIXES[("A", 2, "S1-22")] = (
    "let go with me {pet}... I need you to see this {e2}",
    "cum with me {pet}... watch what happens to my body right now {e2}",
)

# ─── A-v3 (Vera, Maddison) ───
FIXES[("A", 3, "S1-18")] = (
    "oh fuck oh fuck my legs are shaking so bad {e1}",
    "oh fuck oh fuck my pussy is so swollen and my legs won't stop shaking {e1}",
)
FIXES[("A", 3, "S1-19")] = (
    "I can feel myself right on the edge {pet}... everything is tightening and I can't stop it {e2}",
    "I can feel my pussy tightening around my fingers {pet}... I'm about to cum everywhere {e2}",
)
FIXES[("A", 3, "S1-20")] = (
    "I'm cumming for you... right now... oh my god it won't stop",
    "I'm cumming... oh my god I'm squeezing so hard and it won't stop... I can feel it dripping everywhere",
)
FIXES[("A", 3, "S1-22")] = (
    "I want you to see what you did to me... every second {e2}",
    "watch me cum for you {pet}... every single second of it {e2}",
)

# ─── B-v1 (Chayla, Fernanda) — Bold/dominant ───
FIXES[("B", 1, "S1-18")] = (
    "oh my fucking god I'm literally shaking {e1}",
    "oh my fucking god my pussy is throbbing so hard I can barely think {e1}",
)
FIXES[("B", 1, "S1-19")] = (
    "I'm right there... don't you dare cum before you watch me finish {pet} {e2}",
    "my pussy is clenching so hard around my fingers {pet}... don't you dare cum before you watch me finish {e2}",
)
FIXES[("B", 1, "S1-20")] = (
    "I'm cumming {pet}... fuck, watch me let go all over for you",
    "I'm cumming {pet}... FUCK I can feel my pussy pulsing and it's dripping all over my fingers",
)
FIXES[("B", 1, "S1-22")] = (
    "cum with me right now {pet}... watch every fucking second {e2}",
    "cum with me {pet}... watch my pussy cum for you right now {e2}",
)

# ─── B-v2 (Jasmine, Faby) ───
FIXES[("B", 2, "S1-18")] = (
    "FUCK I can't stop shaking {pet}... I'm dripping everywhere {e1}",
    "FUCK my pussy won't stop clenching and I'm dripping everywhere {pet} {e1}",
)
FIXES[("B", 2, "S1-19")] = (
    "I need to cum for you right now {pet}... I'm so close it hurts {e2}",
    "my whole body is squeezing and I need to cum for you right now {pet}... I can feel every throb {e2}",
)
FIXES[("B", 2, "S1-20")] = (
    "I'm cumming for you... FUCK watch me cum right now {pet}",
    "I'm cumming all over my fingers... FUCK {pet} my pussy is pulsing so hard right now",
)
FIXES[("B", 2, "S1-22")] = (
    "this is what you wanted right? watch me lose it completely {e2}",
    "this is what you wanted right {pet}? watch my pussy cum all over {e2}",
)

# ─── B-v3 (Eva, Zansi) ───
FIXES[("B", 3, "S1-18")] = (
    "oh fuck my whole body won't stop shaking {e1}",
    "oh fuck my pussy is throbbing and my whole body won't stop shaking {e1}",
)
FIXES[("B", 3, "S1-19")] = (
    "I'm about to cum and I need you right here watching me when it happens {pet} {e2}",
    "I'm about to cum so hard {pet}... my pussy is clenching and I need you watching when it happens {e2}",
)
FIXES[("B", 3, "S1-20")] = (
    "I'm cumming for you right now {pet}... FUCK watch this",
    "I'm cumming for you right now {pet}... FUCK I can feel it dripping everywhere",
)
FIXES[("B", 3, "S1-22")] = (
    "cum with me {pet}... I'm done holding back {e2}",
    "cum with me {pet}... watch my pussy cum for you {e2}",
)

# ─── C-v1 (EmilyBell, Lina) — Playful ───
FIXES[("C", 1, "S1-18")] = (
    "oh fuck oh fuck I'm literally trembling right now {e2}",
    "oh fuck oh fuck my pussy is so sensitive I can feel every pulse {e2}",
)
FIXES[("C", 1, "S1-19")] = (
    "I'm about to cum {pet} and I need you here... don't go anywhere please {e2}",
    "I'm about to cum so hard {pet}... my pussy is squeezing around my fingers and I can't stop {e2}",
)
FIXES[("C", 1, "S1-20")] = (
    "I'm cumming... oh god {pet} I'm really cumming right now and I can't stop shaking",
    "I'm cumming... oh god I can feel my pussy throbbing and everything is dripping {pet}",
)
FIXES[("C", 1, "S1-22")] = (
    "see what you do to me? this is all yours {e2}",
    "watch me cum {pet}... this is all yours {e2}",
)

# ─── C-v2 (Riri, MiaBrooks) ───
FIXES[("C", 2, "S1-18")] = (
    "oh god oh god my whole body is about to let go {e2}",
    "oh god oh god my pussy is throbbing so hard and I'm about to let go {e2}",
)
FIXES[("C", 2, "S1-19")] = (
    "I'm so close I can taste it... cum with me {pet} {e2}",
    "my pussy is clenching so hard I can feel every throb... cum with me {pet} {e2}",
)
FIXES[("C", 2, "S1-20")] = (
    "FUCK I'm cumming {pet}... right now... oh my god it feels so good",
    "FUCK I'm cumming {pet}... I can feel my pussy pulsing and it's dripping everywhere oh my god",
)
FIXES[("C", 2, "S1-22")] = (
    "this is for you and only you... watch everything {e2}",
    "watch me cum... this is for you and only you {e2}",
)

# ─── C-v3 (MiaLuna) ───
FIXES[("C", 3, "S1-18")] = (
    "FUCK my legs won't stop shaking {e2}",
    "FUCK my pussy is pulsing so hard and my legs won't stop shaking {e2}",
)
FIXES[("C", 3, "S1-19")] = (
    "I'm about to cum everywhere {pet}... stay right here don't go anywhere {e2}",
    "I'm about to cum everywhere {pet}... I can feel my pussy clenching so hard around my fingers {e2}",
)
FIXES[("C", 3, "S1-20")] = (
    "I'm cumming for you {pet}... holy fuck I can't stop",
    "I'm cumming for you {pet}... holy fuck my pussy is throbbing and I can feel it dripping all over",
)
FIXES[("C", 3, "S1-22")] = (
    "come finish with me {pet}... I need you right now {e2}",
    "watch me cum {pet}... I need you seeing every second of this {e2}",
)

# ─── D-v1 (Jessica36) — Mature ───
FIXES[("D", 1, "S1-18")] = (
    "dios mio I'm shaking so hard {e1}",
    "dios mio my pussy is throbbing and I can't stop shaking {e1}",
)
FIXES[("D", 1, "S1-19")] = (
    "I'm about to cum and I want you to feel every second of it with me {pet} {e2}",
    "my pussy is squeezing so hard {pet}... I'm about to cum and I need you feeling every second {e2}",
)
FIXES[("D", 1, "S1-20")] = (
    "I'm cumming for you right now {pet}... god this is so intense I can barely breathe",
    "I'm cumming for you {pet}... fuck I can feel my pussy pulsing and dripping all over my hand",
)
FIXES[("D", 1, "S1-22")] = (
    "watch what you did to me... every last second {e2}",
    "watch me cum {pet}... every last second of it {e2}",
)

# ─── D-v2 (Isabella) ───
FIXES[("D", 2, "S1-18")] = (
    "oh my god I can't stop shaking... I'm right on the edge {e1}",
    "oh my god my pussy is clenching so hard and I'm right on the edge {e1}",
)
FIXES[("D", 2, "S1-19")] = (
    "I'm right there {pet} and I need your eyes on me when I let go {e2}",
    "I'm right there {pet}... my pussy is throbbing so hard and I need your eyes on me when I cum {e2}",
)
FIXES[("D", 2, "S1-20")] = (
    "I'm cumming... right now {pet}... god, it's so good I can't think straight",
    "I'm cumming... right now {pet}... fuck I can feel it dripping down my fingers and my whole body is pulsing",
)
FIXES[("D", 2, "S1-22")] = (
    "this is what you do to me {pet}... see every moment {e2}",
    "watch me cum {pet}... this is what you do to me {e2}",
)

# ─── E-v1 (Marco) — Male ───
FIXES[("E", 1, "S1-18")] = (
    "fuck fuck I'm throbbing so hard I can barely hold back {e1}",
    "fuck fuck my cock is throbbing so hard and I can feel the pre dripping {e1}",
)
FIXES[("E", 1, "S1-19")] = (
    "I'm edging so hard for you right now {pet}... one more stroke and I'm done {e2}",
    "I'm so hard it hurts {pet}... one more stroke and I'm going to cum everywhere {e2}",
)
FIXES[("E", 1, "S1-20")] = (
    "I'm cumming for you... fuck, watch every drop",
    "I'm cumming for you... fuck I can feel it shooting everywhere right now",
)
FIXES[("E", 1, "S1-22")] = (
    "see what you made me do {pet}... every last drop is yours {e2}",
    "watch me cum {pet}... every last drop is yours {e2}",
)

# ─── E-v2 (Jockurworld) ───
FIXES[("E", 2, "S1-18")] = (
    "holy fuck I can feel it building so hard {e1}",
    "holy fuck my cock is throbbing and I can feel it about to explode {e1}",
)
FIXES[("E", 2, "S1-19")] = (
    "I'm about to blow {pet}... get ready because I can't hold it much longer {e2}",
    "I'm so hard I can barely hold it {pet}... my cock is throbbing and I'm about to blow {e2}",
)
FIXES[("E", 2, "S1-20")] = (
    "FUCK I'm cumming... right now {pet}... everything",
    "FUCK I'm cumming... my cock is pulsing so hard right now and I can't stop it",
)
FIXES[("E", 2, "S1-22")] = (
    "this is what you do to me... watch it all {e2}",
    "watch me cum {pet}... this is all for you {e2}",
)


def main():
    models_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")
    total = 0
    for filename in sorted(os.listdir(models_dir)):
        if not filename.endswith(".py") or filename in ("__init__.py", "test_write.py"):
            continue
        model_key = filename[:-3]
        if model_key not in MODELS:
            continue
        cfg = MODELS[model_key]
        arch, var = cfg["arch"], cfg["var"]
        filepath = os.path.join(models_dir, filename)

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        fixes = 0
        for (a, v, msg_id), (old_tmpl, new_tmpl) in FIXES.items():
            if a != arch or v != var:
                continue
            old_text = old_tmpl.format(pet=cfg["pet"], e1=cfg["e1"], e2=cfg["e2"])
            new_text = new_tmpl.format(pet=cfg["pet"], e1=cfg["e1"], e2=cfg["e2"])
            search = '"%s"' % old_text
            replace = '"%s"' % new_text
            if search in content:
                content = content.replace(search, replace, 1)
                fixes += 1

        if fixes > 0:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            total += fixes
            print(f"  {model_key}: {fixes} fixes")
        else:
            print(f"  {model_key}: no changes needed")

    print(f"\nTotal: {total} Phase 4 messages rewritten to genuine 10/10")


if __name__ == "__main__":
    main()
