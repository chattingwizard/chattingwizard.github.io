"""Fix the 8 remaining S1-19 messages that didn't match in R3b."""
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIXES = {
    "faby": (
        "I'm so close I can feel it in every part of my body amor... wait for me, I'm right there \U0001f4a6",
        "my whole body is squeezing and I need to cum for you right now amor... I can feel every throb \U0001f4a6",
    ),
    "isabella": (
        "I'm right there babe... every nerve in my body is on fire and I need you to watch me \U0001f975",
        "I'm right there babe... my pussy is throbbing so hard and I need your eyes on me when I cum \U0001f975",
    ),
    "jasmine": (
        "I'm so close I can feel it in every part of my body papi... wait for me, I'm right there \U0001f525",
        "my whole body is squeezing and I need to cum for you right now papi... I can feel every throb \U0001f525",
    ),
    "jessica36": (
        "I'm on the edge amor... I've been holding back and I can't anymore, I need to let go \U0001f975",
        "my pussy is squeezing so hard amor... I'm about to cum and I need you feeling every second \U0001f975",
    ),
    "lina": (
        "I'm SO close babe... wait for me, I want you to watch the second it happens \U0001f975",
        "I'm about to cum so hard babe... my pussy is squeezing around my fingers and I can't stop \U0001f975",
    ),
    "miabrooks": (
        "I'm literally right on the edge babe... stay right here, I'm about to explode \U0001f60f",
        "my pussy is clenching so hard I can feel every throb... cum with me babe \U0001f60f",
    ),
    "mialuna": (
        "babe I'm about to cum... please don't go anywhere, I need you watching when it happens \U0001f60a",
        "I'm about to cum everywhere babe... I can feel my pussy clenching so hard around my fingers \U0001f60a",
    ),
    "zansi": (
        "I'm about to cum and I need you right here watching me when it happens \U0001f525",
        "I'm about to cum so hard daddy... my pussy is clenching and I need you watching when it happens \U0001f525",
    ),
}

total = 0
for model, (old, new) in FIXES.items():
    fp = "tools/models/%s.py" % model
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()
    search = '"%s"' % old
    replace = '"%s"' % new
    if search in content:
        content = content.replace(search, replace, 1)
        with open(fp, "w", encoding="utf-8") as f:
            f.write(content)
        total += 1
        print("  %s S1-19: FIXED" % model)
    else:
        print("  %s S1-19: NOT FOUND" % model)

print("\nTotal: %d/8 remaining fixes applied" % total)
