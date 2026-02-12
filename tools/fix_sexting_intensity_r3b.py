"""
Round 3b — Fix remaining Phase 4 messages that R3 missed.
Uses ACTUAL current text from model files as search strings.
"""
import os, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

MODELS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")

# Exact old → new replacements per (model_key, msg_id)
# Only includes messages NOT already fixed by R3

FIXES = {
    # ── A-2 (Antonella, Lana) ──
    ("antonella", "S1-19"): (
        'I\'m right there babe... don\'t go anywhere, I need you to watch me finish \U0001f49c',
        'I\'m right there babe... my whole body is clenching around my fingers and I need you watching when I cum \U0001f49c',
    ),
    ("lana", "S1-19"): (
        'I\'m right there babe... don\'t go anywhere, I need you to watch me finish \u2728',
        'I\'m right there babe... my whole body is clenching around my fingers and I need you watching when I cum \u2728',
    ),

    # ── A-3 (Vera, Maddison) ──
    ("vera", "S1-19"): (
        'don\'t leave... I\'m so close and I need to feel you right here when I finish \U0001f495',
        'I can feel my pussy tightening around my fingers babe... I\'m about to cum everywhere \U0001f495',
    ),
    ("vera", "S1-20"): (
        'I\'m about to cum so hard babe... watch me, please don\'t look away',
        'I\'m cumming... oh my god I\'m squeezing so hard and it won\'t stop... I can feel it dripping everywhere',
    ),
    ("vera", "S1-22"): (
        'cum with me right now babe... this is just for you \U0001f495',
        'watch me cum for you babe... every single second of it \U0001f495',
    ),
    ("maddison", "S1-19"): (
        'don\'t leave... I\'m so close and I need to feel you right here when I finish \U0001f495',
        'I can feel my pussy tightening around my fingers Daddy... I\'m about to cum everywhere \U0001f495',
    ),
    ("maddison", "S1-20"): (
        'I\'m about to cum so hard Daddy... watch me, please don\'t look away',
        'I\'m cumming... oh my god I\'m squeezing so hard and it won\'t stop... I can feel it dripping everywhere',
    ),
    ("maddison", "S1-22"): (
        'cum with me right now Daddy... this is just for you \U0001f495',
        'watch me cum for you Daddy... every single second of it \U0001f495',
    ),

    # ── B-1 (Chayla, Fernanda) ──
    ("chayla", "S1-19"): (
        'I\'m right there... don\'t you dare cum before you watch me finish first \U0001f60f',
        'my pussy is clenching so hard around my fingers papi... don\'t you dare cum before you watch me finish \U0001f60f',
    ),
    ("fernanda", "S1-19"): (
        'I\'m right there... don\'t you dare cum before you watch me finish first \U0001f60f',
        'my pussy is clenching so hard around my fingers amor... don\'t you dare cum before you watch me finish \U0001f60f',
    ),

    # ── B-2 (Jasmine, Faby) ──
    ("jasmine", "S1-19"): (
        'I\'m so close I can feel it in every part of my body papi... wait for me, I\'m right there',
        'my whole body is squeezing and I need to cum for you right now papi... I can feel every throb',
    ),
    ("jasmine", "S1-20"): (
        'I\'m cumming right now... don\'t look away for a single second',
        'I\'m cumming all over my fingers... FUCK papi my pussy is pulsing so hard right now',
    ),
    ("faby", "S1-19"): (
        'I\'m so close I can feel it in every part of my body amor... wait for me, I\'m right there',
        'my whole body is squeezing and I need to cum for you right now amor... I can feel every throb',
    ),
    ("faby", "S1-20"): (
        'I\'m cumming right now... don\'t look away for a single second',
        'I\'m cumming all over my fingers... FUCK amor my pussy is pulsing so hard right now',
    ),

    # ── B-3 (Eva, Zansi) ──
    ("eva", "S1-19"): (
        'I\'m about to cum and I need you right here watching me when it happens \U0001f60f',
        'I\'m about to cum so hard papi... my pussy is clenching and I need you watching when it happens \U0001f60f',
    ),
    ("zansi", "S1-19"): (
        'I\'m about to cum and I need you right here watching me when it happens \U0001f60f',
        'I\'m about to cum so hard daddy... my pussy is clenching and I need you watching when it happens \U0001f60f',
    ),

    # ── C-1 (EmilyBell, Lina) ──
    ("emilybell", "S1-19"): (
        'I\'m SO close babe... wait for me, I want you to watch the second it happens \U0001f60f',
        'I\'m about to cum so hard babe... my pussy is squeezing around my fingers and I can\'t stop \U0001f60f',
    ),
    ("emilybell", "S1-20"): (
        'I\'m cumming right now... don\'t miss this',
        'I\'m cumming... oh god I can feel my pussy throbbing and everything is dripping babe',
    ),
    ("emilybell", "S1-22"): (
        'cum with me babe... right now, watch \U0001f975',
        'watch me cum babe... this is all yours \U0001f975',
    ),
    ("lina", "S1-19"): (
        'I\'m SO close babe... wait for me, I want you to watch the second it happens \u2728',
        'I\'m about to cum so hard babe... my pussy is squeezing around my fingers and I can\'t stop \u2728',
    ),
    ("lina", "S1-20"): (
        'I\'m cumming right now... don\'t miss this',
        'I\'m cumming... oh god I can feel my pussy throbbing and everything is dripping babe',
    ),
    ("lina", "S1-22"): (
        'cum with me babe... right now, watch \u2728',
        'watch me cum babe... this is all yours \u2728',
    ),

    # ── C-2 (Riri, MiaBrooks) ──
    ("riri", "S1-19"): (
        'I\'m literally right on the edge babe... stay right here, I\'m about to explode \U0001f975',
        'my pussy is clenching so hard I can feel every throb... cum with me babe \U0001f975',
    ),
    ("riri", "S1-20"): (
        'I\'m cumming... holy fuck I\'m cumming for you right now',
        'FUCK I\'m cumming babe... I can feel my pussy pulsing and it\'s dripping everywhere oh my god',
    ),
    ("riri", "S1-22"): (
        'let go with me right now babe... watch every second \U0001f60a',
        'watch me cum... this is for you and only you \U0001f60a',
    ),
    ("miabrooks", "S1-19"): (
        'I\'m literally right on the edge babe... stay right here, I\'m about to explode \U0001f975',
        'my pussy is clenching so hard I can feel every throb... cum with me babe \U0001f975',
    ),
    ("miabrooks", "S1-20"): (
        'I\'m cumming... holy fuck I\'m cumming for you right now',
        'FUCK I\'m cumming babe... I can feel my pussy pulsing and it\'s dripping everywhere oh my god',
    ),
    ("miabrooks", "S1-22"): (
        'let go with me right now babe... watch every second \U0001f975',
        'watch me cum... this is for you and only you \U0001f975',
    ),

    # ── C-3 (MiaLuna) ──
    ("mialuna", "S1-19"): (
        'babe I\'m about to cum... please don\'t go anywhere, I need you watching when it happens',
        'I\'m about to cum everywhere babe... I can feel my pussy clenching so hard around my fingers',
    ),
    ("mialuna", "S1-20"): (
        'I\'m cumming... oh my GOD I\'m cumming right now',
        'I\'m cumming for you babe... holy fuck my pussy is throbbing and I can feel it dripping all over',
    ),

    # ── D-1 (Jessica36) ──
    ("jessica36", "S1-19"): (
        'I\'m on the edge amor... I\'ve been holding back and I can\'t anymore, I need to let go for you',
        'my pussy is squeezing so hard amor... I\'m about to cum and I need you feeling every second',
    ),
    ("jessica36", "S1-20"): (
        'I\'m cumming for you right now... watch me, every second of it',
        'I\'m cumming for you amor... fuck I can feel my pussy pulsing and dripping all over my hand',
    ),
    ("jessica36", "S1-22"): (
        'cum with me amor... right now, don\'t look away \U0001f975',
        'watch me cum amor... every last second of it \U0001f975',
    ),

    # ── D-2 (Isabella) ──
    ("isabella", "S1-19"): (
        'I\'m right there babe... every nerve in my body is on fire and I need you to watch when I let go',
        'I\'m right there babe... my pussy is throbbing so hard and I need your eyes on me when I cum',
    ),
    ("isabella", "S1-20"): (
        'I\'m cumming... god I\'m cumming so hard for you right now',
        'I\'m cumming... right now babe... fuck I can feel it dripping down my fingers and my whole body is pulsing',
    ),
    ("isabella", "S1-22"): (
        'let go with me babe... I\'m done holding back \U0001f975',
        'watch me cum babe... this is what you do to me \U0001f975',
    ),

    # ── E-1 (Marco) ──
    ("marco", "S1-19"): (
        'I\'m right there babe... don\'t stop watching, I need you to see this \U0001f4a6',
        'I\'m so hard it hurts babe... one more stroke and I\'m going to cum everywhere \U0001f4a6',
    ),
    ("marco", "S1-20"): (
        'I\'m about to cum for you... watch every second',
        'I\'m cumming for you... fuck I can feel it shooting everywhere right now',
    ),

    # ── E-2 (Jockurworld) ──
    ("jockurworld", "S1-19"): (
        'I\'m right there bro... don\'t stop watching, I\'m about to blow \U0001f4a6',
        'I\'m so hard I can barely hold it bro... my cock is throbbing and I\'m about to blow \U0001f4a6',
    ),
}


def main():
    total = 0
    for (model_key, msg_id), (old_text, new_text) in sorted(FIXES.items()):
        filepath = os.path.join(MODELS_DIR, model_key + ".py")
        if not os.path.exists(filepath):
            print(f"  SKIP {model_key}: file not found")
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        search = '"%s"' % old_text
        replace = '"%s"' % new_text

        if search in content:
            content = content.replace(search, replace, 1)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            total += 1
            print(f"  {model_key} {msg_id}: FIXED")
        else:
            # Try with truncated text (first 50 chars)
            print(f"  {model_key} {msg_id}: NOT FOUND — old text doesn't match")

    print(f"\nTotal: {total} additional Phase 4 fixes applied")


if __name__ == "__main__":
    main()
