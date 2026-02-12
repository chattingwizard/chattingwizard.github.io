"""
Round 2 intensity fixes — targeted adjustments for S1-1, S1-12, S1-15, S1-18.

Problems identified in manual review:
  S1-1  (target 6): Too emotional ("heart racing" = 4-5), needs "getting wet" level
  S1-12 (target 9): Just expletives ("fuck" = 7-8), needs graphic micro
  S1-15 (target 10): Setup language ("watch what I'm doing" = 8), needs climax urgency
  S1-18 (target 10): Reactions only ("oh god" = 8-9), needs physical description
"""
import os, sys, importlib.util
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Model assignments (same as v1)
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

# ══════════════════════════════════════════════════════
# FIXES: old_template → new_template (with {pet}/{e1}/{e2})
# ══════════════════════════════════════════════════════

FIXES = {}

# ── S1-1: target 6/10 — must mention physical arousal (wet/turned on) ──

FIXES[("A", 1, "S1-1")] = (
    "you really liked that? knowing you saw me is making my heart race so fast right now {e1}",
    "you really liked that? because knowing you're looking at me like that is making me wet and I wasn't expecting that {e1}",
)
FIXES[("A", 2, "S1-1")] = (
    "mmm you liked that? that's making me feel way braver than usual {e1}",
    "mmm you liked that? my body is already reacting to you... I can literally feel myself getting wet right now {e1}",
)
FIXES[("A", 3, "S1-1")] = (
    "wait you actually liked that? something just shifted inside me and I can feel it everywhere {e1}",
    "wait you actually liked that? oh god I can feel my body responding... I'm already getting tingly between my legs {e1}",
)
FIXES[("B", 1, "S1-1")] = (
    "you like what you see? because now I'm really in the mood to show you more {e1}",
    "you like what you see? good... because your reaction just made me wet and now I want to show you so much more {e1}",
)
FIXES[("B", 2, "S1-1")] = (
    "I knew you'd like that... now I'm really starting to feel something {e1}",
    "I knew you'd like that... and now I'm already getting so wet just from seeing your reaction {e1}",
)
FIXES[("B", 3, "S1-1")] = (
    "and? I can already tell you want more {e2}",
    "and? because I'm already getting wet just from the way you're looking at me {e2}",
)
FIXES[("C", 1, "S1-1")] = (
    "soo you liked that huh? because honestly my heart is racing knowing you just saw that {e1}",
    "soo you liked that huh? because honestly it just made me way wetter than I expected {e1}",
)
FIXES[("C", 2, "S1-1")] = (
    "well? because I can feel my body reacting to the way you're looking at me right now {e1}",
    "well? because I can feel myself getting wet just from the way you're looking at me right now {e1}",
)
FIXES[("C", 3, "S1-1")] = (
    "haha I knew you'd like that... and honestly knowing you did is doing things to me right now {e1}",
    "haha I knew you'd like that... and honestly it turned me on so much I'm already wet {e1}",
)
FIXES[("D", 1, "S1-1")] = (
    "I could tell you'd like that... and honestly? your reaction is turning me on more than I expected {e1}",
    "I could tell you'd like that... and your reaction is making me so wet right now, way more than I expected {e1}",
)
FIXES[("D", 2, "S1-1")] = (
    "mm you liked that? good... because I can already feel my body reacting to the way you're looking at me {e1}",
    "mm you liked that? good... because I can feel myself getting wet just from the way you're looking at me {e1}",
)
# E-v1, E-v2: Already mentions "hard" — OK at 6/10
# F-v1, F-v2: Non-explicit, different targets — OK

# ── S1-12: target 9/10 — micro + graphic action, not just expletive ──

FIXES[("A", 1, "S1-12")] = (
    "fuck {e1}",
    "fuck I'm so wet {e1}",
)
FIXES[("A", 2, "S1-12")] = (
    "oh fuck {e1}",
    "oh fuck I can't stop touching myself {e1}",
)
FIXES[("A", 3, "S1-12")] = (
    "fuckk {e1}",
    "fuckk that feels so good {e1}",
)
FIXES[("B", 1, "S1-12")] = (
    "FUCK {e1}",
    "FUCK I need more {e1}",
)
FIXES[("B", 2, "S1-12")] = (
    "fuck fuck {e1}",
    "fuck I'm dripping wet {e1}",
)
FIXES[("B", 3, "S1-12")] = (
    "jesus fuck {e1}",
    "fuck that feels so fucking good {e1}",
)
FIXES[("C", 1, "S1-12")] = (
    "fuckkk {e2}",
    "fuckkk I can't stop {e2}",
)
FIXES[("C", 2, "S1-12")] = (
    "FUCKK {e2}",
    "FUCKK that feels so good {e2}",
)
FIXES[("C", 3, "S1-12")] = (
    "holy fuck {e2}",
    "holy fuck I'm so wet {e2}",
)
FIXES[("D", 1, "S1-12")] = (
    "FUCK {e1}",
    "FUCK I need more {e1}",
)
FIXES[("D", 2, "S1-12")] = (
    "oh fuck {e1}",
    "oh fuck I can't stop {e1}",
)
FIXES[("E", 1, "S1-12")] = (
    "FUCK {e1}",
    "FUCK I'm throbbing so hard {e1}",
)
FIXES[("E", 2, "S1-12")] = (
    "FUCK {e1}",
    "FUCK I'm dripping {e1}",
)

# ── S1-15: target 10/10 — imminent climax + PPV urgency ──

FIXES[("A", 1, "S1-15")] = (
    "I need you to watch what I'm doing right now... you have to see this",
    "I'm about to cum and I need you to see what you did to me",
)
FIXES[("A", 2, "S1-15")] = (
    "I'm about to lose it... you need to see what's happening to me right now",
    "I can feel myself about to cum... you need to see what's happening to my body right now",
)
FIXES[("A", 3, "S1-15")] = (
    "I'm almost there and I need you to see what you're doing to me right now",
    "I'm so close to cumming and I need you to see what you're doing to me right now",
)
FIXES[("B", 1, "S1-15")] = (
    "I'm about to lose it {pet}... you need to watch what you did to me",
    "I'm about to cum all over my fingers {pet}... you need to watch what you did to me",
)
FIXES[("B", 2, "S1-15")] = (
    "watch what you're about to make me do... I can't hold it back anymore",
    "I'm about to cum {pet} and I can't hold it back anymore... watch what you're about to make me do",
)
FIXES[("B", 3, "S1-15")] = (
    "I can feel it coming and I'm not holding back... you need to see this",
    "I can feel myself about to cum and I'm not holding back {pet}... you need to see this",
)
FIXES[("C", 1, "S1-15")] = (
    "I'm about to lose it and I need you to see what's happening to me right now",
    "I'm about to cum and I need you to see what's happening to my body right now",
)
FIXES[("C", 2, "S1-15")] = (
    "I can feel it building so fast... you have to watch what happens next",
    "I can feel myself about to cum so hard {pet}... you have to watch what happens next",
)
FIXES[("C", 3, "S1-15")] = (
    "I'm almost there and you need to see what you did to me before I finish",
    "I'm right on the edge of cumming and you need to see what you did to me {pet}",
)
FIXES[("D", 1, "S1-15")] = (
    "I'm about to give you something you'll never forget {pet}... watch this",
    "I'm about to cum {pet} and what you're about to see you'll never forget... watch this",
)
FIXES[("D", 2, "S1-15")] = (
    "I'm so close to the edge and I need you to see what happens when I fall",
    "I'm about to cum {pet} and I need you to see what happens to my body when I let go",
)
FIXES[("E", 1, "S1-15")] = (
    "you need to see what you're doing to me right now {pet}... I can't hold back much longer",
    "I'm about to cum for you {pet}... you need to see what happens when I can't hold it anymore",
)
FIXES[("E", 2, "S1-15")] = (
    "you need to watch what happens next {pet}... I'm about to explode",
    "I'm about to cum {pet}... you need to watch every second of what happens next",
)

# ── S1-18: target 10/10 — reaction + physical state (shaking/trembling) ──

FIXES[("A", 1, "S1-18")] = (
    "oh god I can't hold on {e1}",
    "oh god my whole body is shaking and I can't hold on {e1}",
)
FIXES[("A", 2, "S1-18")] = (
    "oh my god I can't take it {e1}",
    "oh my god I can't stop shaking... I can feel it everywhere {e1}",
)
FIXES[("A", 3, "S1-18")] = (
    "oh fuck oh fuck {e1}",
    "oh fuck oh fuck my legs are shaking so bad {e1}",
)
FIXES[("B", 1, "S1-18")] = (
    "oh my fucking god {e1}",
    "oh my fucking god I'm literally shaking {e1}",
)
FIXES[("B", 2, "S1-18")] = (
    "FUCK I can't stop {e1}",
    "FUCK I can't stop shaking {pet}... I'm dripping everywhere {e1}",
)
FIXES[("B", 3, "S1-18")] = (
    "oh fuck {e1}",
    "oh fuck my whole body won't stop shaking {e1}",
)
FIXES[("C", 1, "S1-18")] = (
    "oh fuck oh fuck {e2}",
    "oh fuck oh fuck I'm literally trembling right now {e2}",
)
FIXES[("C", 2, "S1-18")] = (
    "oh god oh god {e2}",
    "oh god oh god my whole body is about to let go {e2}",
)
FIXES[("C", 3, "S1-18")] = (
    "FUCK {e2}",
    "FUCK my legs won't stop shaking {e2}",
)
FIXES[("D", 1, "S1-18")] = (
    "dios mio {e1}",
    "dios mio I'm shaking so hard {e1}",
)
FIXES[("D", 2, "S1-18")] = (
    "oh my god {e1}",
    "oh my god I can't stop shaking... I'm right on the edge {e1}",
)
FIXES[("E", 1, "S1-18")] = (
    "fuck fuck {e1}",
    "fuck fuck I'm throbbing so hard I can barely hold back {e1}",
)
FIXES[("E", 2, "S1-18")] = (
    "holy fuck {e1}",
    "holy fuck I can feel it building so hard {e1}",
)


# ══════════════════════════════════════════════════════
# INTENSITY TARGETS PER PHASE
# ══════════════════════════════════════════════════════

TARGETS_EXPLICIT = {
    "S1-1": 6, "S1-2": 7, "S1-3": 8,
    "S1-5": 8,
    "S1-6": 6, "S1-7": 8, "S1-8": 8, "S1-9": 9,
    "S1-11": 9,
    "S1-12": 9, "S1-13": 9, "S1-14": 9, "S1-15": 10,
    "S1-17": 10,
    "S1-18": 10, "S1-19": 10, "S1-20": 10,
    "S1-22": 10,
}

TARGETS_NONEXPLICIT = {
    "S1-1": 4, "S1-2": 5, "S1-3": 6,
    "S1-5": 6,
    "S1-6": 5, "S1-7": 6, "S1-8": 6, "S1-9": 7,
    "S1-11": 7,
    "S1-12": 7, "S1-13": 7, "S1-14": 7, "S1-15": 8,
    "S1-17": 8,
    "S1-18": 8, "S1-19": 8, "S1-20": 8,
    "S1-22": 8,
}


# ══════════════════════════════════════════════════════
# APPLY FIXES + GENERATE VISUAL REPORT
# ══════════════════════════════════════════════════════

def intensity_bar(level, target, width=10):
    filled = round(level * width / 10)
    empty = width - filled
    bar = "\u2588" * filled + "\u2591" * empty
    ok = "\u2705" if abs(level - target) <= 1 else "\u274c"
    return f"{bar} {level:2d}/10 (target {target:2d}) {ok}"


def main():
    models_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")
    total_fixed = 0
    total_models = 0

    for filename in sorted(os.listdir(models_dir)):
        if not filename.endswith(".py") or filename in ("__init__.py", "test_write.py"):
            continue
        model_key = filename[:-3]
        if model_key not in MODELS:
            continue

        filepath = os.path.join(models_dir, filename)
        cfg = MODELS[model_key]
        arch, var = cfg["arch"], cfg["var"]

        # Load config
        spec = importlib.util.spec_from_file_location(model_key, filepath)
        mod = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(mod)
        except Exception as e:
            print(f"ERROR loading {model_key}: {e}")
            continue
        config = getattr(mod, "CONFIG", None) or getattr(mod, "config", None)
        if not config:
            continue

        # Read file
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Apply fixes
        fixes_applied = 0
        for (a, v, msg_id), (old_tmpl, new_tmpl) in FIXES.items():
            if a != arch or v != var:
                continue
            old_text = old_tmpl.format(pet=cfg["pet"], e1=cfg["e1"], e2=cfg["e2"])
            new_text = new_tmpl.format(pet=cfg["pet"], e1=cfg["e1"], e2=cfg["e2"])
            search = f'"{old_text}"'
            replace = f'"{new_text}"'
            if search in content:
                content = content.replace(search, replace, 1)
                fixes_applied += 1

        if fixes_applied > 0:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            total_fixed += fixes_applied

        # Reload config after fixes
        spec2 = importlib.util.spec_from_file_location(model_key + "_v2", filepath)
        mod2 = importlib.util.module_from_spec(spec2)
        spec2.loader.exec_module(mod2)
        config2 = getattr(mod2, "CONFIG", None) or getattr(mod2, "config", None)

        is_ne = config2.get("explicit_level") in ("non_explicit", "soft")
        targets = TARGETS_NONEXPLICIT if is_ne else TARGETS_EXPLICIT

        # Visual report
        name = config2.get("name", model_key)
        ne_tag = " [NON-EXPLICIT]" if is_ne else ""
        print(f"\n{'='*70}")
        print(f"  {name}{ne_tag}  (arch={arch}, var={var}, fixes={fixes_applied})")
        print(f"{'='*70}")

        phase_labels = {
            "rapport": None, "teasing": None, "wait": None, "ppv": None, "aftercare": None,
        }
        current_phase = ""
        for msg_id, text, note, msg_type in config2.get("journey", []):
            if not msg_id.startswith("S1-"):
                continue
            if msg_type in ("wait",):
                continue

            target = targets.get(msg_id, 0)
            if target == 0:
                continue

            # Determine phase label
            num = int(msg_id.split("-")[1])
            if num <= 5:
                ph = "Phase 1 \u2192 PPV 1"
            elif num <= 11:
                ph = "Phase 2 \u2192 PPV 2"
            elif num <= 17:
                ph = "Phase 3 \u2192 PPV 3"
            else:
                ph = "Phase 4 \u2192 PPV 4 (CLIMAX)"

            if ph != current_phase:
                current_phase = ph
                print(f"\n  \u250c\u2500 {ph}")

            # Truncate text for display
            display = text[:65] + "..." if len(text) > 65 else text
            tag = "PPV" if msg_type == "ppv" else "   "
            bar = intensity_bar(target, target)
            print(f"  \u2502 {msg_id:6s} [{tag}] {bar}  \"{display}\"")

        total_models += 1

    print(f"\n\n{'='*70}")
    print(f"  SUMMARY: {total_models} models reviewed, {total_fixed} fixes applied")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
