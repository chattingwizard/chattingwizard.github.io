#!/usr/bin/env python3
"""
diversify_sexting.py -- Diversify top 7 repeated sexting phrases across model configs.

Problem: Identical phrases appear in 11-18 different models. Subscribers who follow
multiple models will notice the copy-paste pattern.

Solution: Assign different variant phrasings to each model, ensuring cross-model variety.

Skips: putri, max, marco (custom configs), test_write.
Non-explicit models (jessica34, irina): no crude variants (cum, FUCK, fuuuck).
"""

import os
import re

# ═══════════════════════════════════════
# PATHS & CONFIG
# ═══════════════════════════════════════

MODELS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")
SKIP_FILES = {"putri.py", "max.py", "marco.py", "test_write.py", "__init__.py"}
NON_EXPLICIT = {"jessica34.py", "irina.py"}


def replace_phrase_in_step(content, step_id, old_phrase, new_phrase):
    """
    In the tuple for step_id, find old_phrase inside the text field (2nd element)
    and replace it with new_phrase. Preserves any emoji/suffix after the phrase.

    Returns (new_content, replacement_count).
    """
    escaped_sid = re.escape(step_id)
    escaped_old = re.escape(old_phrase)

    # Match: ("STEP_ID", "___old_phrase___", ...)
    # [^"]*? = non-greedy: any non-quote chars BEFORE the phrase (preserves prefix)
    # [^"]*  = greedy: any non-quote chars AFTER the phrase + closing quote (preserves suffix/emoji)
    pattern = rf'(\("{escaped_sid}",\s*")([^"]*?)({escaped_old})([^"]*")'

    count = 0

    def replacer(m):
        nonlocal count
        count += 1
        return m.group(1) + m.group(2) + new_phrase + m.group(4)

    new_content = re.sub(pattern, replacer, content)
    return new_content, count


# ═══════════════════════════════════════════════════════════════
# PHRASE DEFINITIONS & VARIANT ASSIGNMENTS
# ═══════════════════════════════════════════════════════════════
#
# For each phrase:
#   "original": the exact phrase to match inside tuple text fields
#   "step_ids": which tuple step IDs to search in
#   "models":   {filename: replacement_text}
#
# Variant legend:
#   A = keep original (no file change needed)
#   B-E = different variants, distributed via round-robin
#
# Distribution: ~even split across 5 variants per phrase.
# Non-explicit models get safe variants only (no cum, FUCK, fuuuck).
# ═══════════════════════════════════════════════════════════════

PHRASES = [
    # ──────────────────────────────────────────────
    # 1. "I can't hold back anymore" (S1-15, 18 models)
    # Variants: A=original, B=resist, C=done holding, D=control, E=screw it
    # ──────────────────────────────────────────────
    {
        "name": "I can't hold back anymore",
        "original": "I can't hold back anymore",
        "step_ids": ["S1-15"],
        "models": {
            "antonella.py":   "I can't resist you anymore",       # B
            "ashley.py":      "I'm done holding back",            # C
            "chayla.py":      "I can't control myself anymore",   # D
            "eva.py":         "screw it I'm done waiting",        # E
            "faby.py":        "I can't hold back anymore",        # A
            "fernanda.py":    "I can't resist you anymore",       # B
            "isabella.py":    "I'm done holding back",            # C
            "jessica36.py":   "I can't control myself anymore",   # D
            "jockurworld.py": "screw it I'm done waiting",        # E
            "lana.py":        "I can't hold back anymore",        # A
            "lia.py":         "I can't resist you anymore",       # B
            "lina.py":        "I'm done holding back",            # C
            "maddison.py":    "I can't control myself anymore",   # D
            "miabrooks.py":   "screw it I'm done waiting",        # E
            "mialuna.py":     "I can't hold back anymore",        # A
            "riri.py":        "I can't resist you anymore",       # B
            "vera.py":        "I'm done holding back",            # C
            "zansi.py":       "I can't control myself anymore",   # D
        },
    },

    # ──────────────────────────────────────────────
    # 2. "give me a sec" (S1-4 and/or S1-16, 13 models)
    # Variants: A=original, B=one second, C=hold on a sec, D=wait one sec, E=gimme a minute
    # ──────────────────────────────────────────────
    {
        "name": "give me a sec",
        "original": "give me a sec",
        "step_ids": ["S1-4", "S1-16"],
        "models": {
            "antonella.py":   "one second",           # B
            "ashley.py":      "hold on a sec",        # C  (has it at S1-16 with emoji)
            "chayla.py":      "wait one sec",         # D
            "emilybell.py":   "gimme a minute",       # E  (missed in first pass)
            "eva.py":         "give me a sec",        # A
            "faby.py":        "gimme a minute",       # E
            "fernanda.py":    "give me a sec",        # A
            "irina.py":       "one second",           # B  (missed in first pass)
            "isabella.py":    "one second",           # B
            "jasmine.py":     "hold on a sec",        # C  (missed in first pass)
            "jessica34.py":   "wait one sec",         # D  (missed in first pass)
            "jessica36.py":   "hold on a sec",        # C
            "jockurworld.py": "wait one sec",         # D
            "lina.py":        "gimme a minute",       # E  (missed in first pass)
            "maddison.py":    "gimme a minute",       # E
            "mialuna.py":     "give me a sec",        # A
            "riri.py":        "one second",           # B
            "vera.py":        "hold on a sec",        # C
            "zansi.py":       "wait one sec",         # D
        },
    },

    # ──────────────────────────────────────────────
    # 3. "hold on" at S1-21 (14 models)
    # Variants: A=original, B=wait, C=one sec, D=hold on hold on, E=don't go anywhere
    # ──────────────────────────────────────────────
    {
        "name": "hold on (S1-21)",
        "original": "hold on",
        "step_ids": ["S1-21"],
        "models": {
            "antonella.py":   "wait",                 # B
            "chayla.py":      "one sec",              # C
            "emilybell.py":   "hold on hold on",      # D
            "eva.py":         "don't go anywhere",    # E
            "faby.py":        "hold on",              # A
            "fernanda.py":    "hold on",              # A  (missed in first pass)
            "irina.py":       "wait",                 # B  (missed in first pass)
            "isabella.py":    "wait",                 # B
            "jasmine.py":     "one sec",              # C
            "jessica34.py":   "one sec",              # C  (missed in first pass)
            "jessica36.py":   "hold on hold on",      # D
            "jockurworld.py": "don't go anywhere",    # E
            "lana.py":        "hold on",              # A
            "lia.py":         "wait",                 # B
            "maddison.py":    "don't go anywhere",    # E  (missed in first pass)
            "miabrooks.py":   "one sec",              # C
            "mialuna.py":     "hold on hold on",      # D
            "riri.py":        "don't go anywhere",    # E
        },
    },

    # ──────────────────────────────────────────────
    # 4. "did you watch it?" at S1-6 (12 models)
    # Variants: A=original, B=see it, C=tell me what you think, D=well?, E=so what do you think?
    # ──────────────────────────────────────────────
    {
        "name": "did you watch it?",
        "original": "did you watch it?",
        "step_ids": ["S1-6"],
        "models": {
            "antonella.py":  "did you see it?",             # B
            "ashley.py":     "tell me what you think",      # C
            "chayla.py":     "well?",                       # D
            "emilybell.py":  "so what do you think?",       # E
            "eva.py":        "did you watch it?",           # A
            "isabella.py":   "did you see it?",             # B
            "lana.py":       "tell me what you think",      # C
            "lina.py":       "well?",                       # D
            "mialuna.py":    "so what do you think?",       # E
            "riri.py":       "did you watch it?",           # A
            "vera.py":       "did you see it?",             # B
            "zansi.py":      "tell me what you think",      # C
        },
    },

    # ──────────────────────────────────────────────
    # 5. "FUCK" at S1-18 (9 models)
    # Non-explicit models don't have this phrase.
    # Variants: A=FUCK, B=oh fuck, C=fuckkkk, D=god, E=oh god
    # ──────────────────────────────────────────────
    {
        "name": "FUCK",
        "original": "FUCK",
        "step_ids": ["S1-18"],
        "models": {
            "antonella.py":   "fuckkkk",     # C  (missed in first pass, has emoji suffix)
            "eva.py":         "FUCK",        # A
            "faby.py":        "oh fuck",     # B
            "fernanda.py":    "fuckkkk",     # C
            "isabella.py":    "god",         # D
            "jasmine.py":     "oh god",      # E
            "jessica36.py":   "FUCK",        # A
            "jockurworld.py": "oh fuck",     # B
            "miabrooks.py":   "oh god",      # E  (missed in first pass, has emoji suffix)
            "mialuna.py":     "fuckkkk",     # C
            "riri.py":        "god",         # D
        },
    },

    # ──────────────────────────────────────────────
    # 6. "cum with me" at S1-22 (12 models)
    # Non-explicit models don't have this phrase.
    # Models with suffixes (gostoso, Daddy, emojis) — only "cum with me" is replaced.
    # Variants: A=original, B=finish with me, C=I want us to finish together,
    #           D=let go with me, E=I'm about to finish... stay with me
    # ──────────────────────────────────────────────
    {
        "name": "cum with me",
        "original": "cum with me",
        "step_ids": ["S1-22"],
        "models": {
            "antonella.py":   "I want us to finish together",          # C
            "chayla.py":      "let go with me",                        # D
            "eva.py":         "I'm about to finish... stay with me",   # E
            "faby.py":        "finish with me",                        # B
            "fernanda.py":    "cum with me",                           # A
            "isabella.py":    "I want us to finish together",          # C
            "jasmine.py":     "let go with me",                        # D
            "jessica36.py":   "I'm about to finish... stay with me",   # E
            "jockurworld.py": "cum with me",                           # A
            "maddison.py":    "finish with me",                        # B
            "mialuna.py":     "let go with me",                        # D
            "riri.py":        "I want us to finish together",          # C
        },
    },

    # ──────────────────────────────────────────────
    # 7. "oh my god" at S1-12 or S1-18 (11 models)
    # Non-explicit: irina → "omg", jessica34 → "oh god" (safe variants)
    # Variants: A=original, B=omg, C=jesus, D=oh god, E=fuuuck
    # ──────────────────────────────────────────────
    {
        "name": "oh my god",
        "original": "oh my god",
        "step_ids": ["S1-12", "S1-18"],
        "models": {
            "ashley.py":     "omg",           # B
            "chayla.py":     "jesus",         # C
            "emilybell.py":  "oh god",        # D
            "irina.py":      "omg",           # B  (non-explicit safe)
            "jessica34.py":  "oh god",        # D  (non-explicit safe)
            "lana.py":       "fuuuck",        # E
            "lia.py":        "oh my god",     # A
            "lina.py":       "jesus",         # C
            "maddison.py":   "fuuuck",        # E
            "vera.py":       "oh my god",     # A
            "zansi.py":      "omg",           # B
        },
    },
]


def main():
    print("=" * 70)
    print("DIVERSIFY SEXTING PHRASES -- Cross-Model Diversity Fix")
    print("=" * 70)

    if not os.path.isdir(MODELS_DIR):
        print(f"ERROR: Models directory not found: {MODELS_DIR}")
        return

    total_changes = 0
    files_modified = set()
    skipped = []

    for phrase_def in PHRASES:
        name = phrase_def["name"]
        original = phrase_def["original"]
        step_ids = phrase_def["step_ids"]
        models = phrase_def["models"]

        print(f"\n{'-' * 70}")
        print(f"PHRASE: \"{original}\"  |  Steps: {', '.join(step_ids)}")
        print(f"{'-' * 70}")

        changed = 0
        kept = 0

        for model_file in sorted(models.keys()):
            replacement = models[model_file]

            # Skip if keeping original (variant A)
            if replacement == original:
                kept += 1
                print(f"  = {model_file:<20} KEEP original")
                continue

            filepath = os.path.join(MODELS_DIR, model_file)
            if not os.path.exists(filepath):
                print(f"  X {model_file:<20} FILE NOT FOUND")
                skipped.append((name, model_file, "file not found"))
                continue

            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            new_content = content
            hit_count = 0

            for sid in step_ids:
                new_content, hits = replace_phrase_in_step(
                    new_content, sid, original, replacement
                )
                hit_count += hits

            if hit_count > 0:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                suffix = "s" if hit_count > 1 else ""
                print(f"  > {model_file:<20} -> \"{replacement}\"  ({hit_count} hit{suffix})")
                total_changes += hit_count
                changed += 1
                files_modified.add(model_file)
            else:
                print(f"  - {model_file:<20} phrase not found at {step_ids}")
                skipped.append((name, model_file, f"not found at {step_ids}"))

        print(f"  [{changed} changed, {kept} kept original]")

    # ═══════════════════════════════════════
    # SCAN for models with phrases NOT in assignments (catches missed models)
    # ═══════════════════════════════════════
    print(f"\n{'-' * 70}")
    print("SCANNING for missed models (phrase present but not in assignments)...")
    print(f"{'-' * 70}")

    missed_any = False
    for filename in sorted(os.listdir(MODELS_DIR)):
        if not filename.endswith(".py") or filename in SKIP_FILES:
            continue
        filepath = os.path.join(MODELS_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        for phrase_def in PHRASES:
            if filename in phrase_def["models"]:
                continue  # Already handled
            original = phrase_def["original"]
            for sid in phrase_def["step_ids"]:
                escaped_sid = re.escape(sid)
                escaped_old = re.escape(original)
                pattern = rf'\("{escaped_sid}",\s*"[^"]*?{escaped_old}[^"]*"'
                if re.search(pattern, content):
                    print(f"  !! {filename} has \"{original}\" at {sid} -- NOT in assignments!")
                    missed_any = True

    if not missed_any:
        print("  All models covered. No missed phrases.")

    # ═══════════════════════════════════════
    # FINAL REPORT
    # ═══════════════════════════════════════
    print(f"\n{'=' * 70}")
    print("FINAL REPORT")
    print(f"{'=' * 70}")
    print(f"Total replacements made:  {total_changes}")
    print(f"Files modified:           {len(files_modified)}")
    if files_modified:
        print(f"Modified files:           {', '.join(sorted(files_modified))}")

    if skipped:
        print(f"\nSkipped ({len(skipped)}):")
        for phrase, model, reason in skipped:
            print(f"  [{phrase}] {model}: {reason}")

    print(f"\n{'=' * 70}")
    print("DONE -- Phrases diversified across models!")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()
