"""
Fix all OnlyFans banned words across the project.
Scans and replaces in HTML files and Python generators.
Only fixes TEXT fields (messages chatters send), not Notes or descriptions.
"""
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE = r"c:\Users\34683\CW-ScriptManager"

# Replacements: (old_exact, new_exact) — only in message/text context
REPLACEMENTS = [
    # "meet" in greetings
    ("glad you're here man", "glad you're here man"),
    ("glad you're here man 😏", "glad you're here man 😏"),
    ("hey man, glad you're here. so what made you hit subscribe?", "hey man, glad you're here. so what made you hit subscribe?"),
    ("glad you're here...", "glad you're here..."),
    
    # "shit" in sexting
    ("I can't do anything about it", "I can't do anything about it"),
    ("I'm hard as fuck because of you and I can't do anything about it", "I'm hard as fuck because of you and I can't do anything about it"),
    ("I'm hard and I can't do anything about it because of you", "I'm hard and I can't do anything about it because of you"),
    
    # "holy shit" → "holy fuck" (fuck is allowed on OF)
    ("holy fuck 🥵 that was... wow", "holy fuck 🥵 that was... wow"),
    ("oh fuck that is... damn. I need to show you something rn", "oh fuck that is... damn. I need to show you something rn"),
    ("oh fuck that is... damn. I need to show you something rn", "oh fuck that is... damn. I need to show you something rn"),
    ("oh fuck that is... damn. I need to show you something right now", "oh fuck that is... damn. I need to show you something right now"),
    
    # "shit" in other messages
    ("I already gave you a free one man", "I already gave you a free one man"),
    ("there's a lot of fake stuff on here", "there's a lot of fake stuff on here"),
    ("like you have your life together", "like you have your life together"),
    ("that's okay baby 😊 no pressure at all", "that's okay baby 😊 no pressure at all"),
    
    # "cycling" → "biking" / "riding" for Putri
    ("biking vlogger! I record my rides and random moments from the road 🚴‍♀️", "biking vlogger! I record my rides and random moments from the road 🚴‍♀️"),
    ("biking is my obsession 😅 that and exploring new places, trying food, connecting with people", "biking is my obsession 😅 that and exploring new places, trying food, connecting with people"),
    ("Biking vlogger 🚴‍♀️", "Biking vlogger 🚴‍♀️"),
    ("Biking, travel, exploring 🌍", "Biking, travel, exploring 🌍"),
    ("Biking Vlogger 🚴‍♀️", "Biking Vlogger 🚴‍♀️"),
    ("biking vlogger", "biking vlogger"),
    
    # "young" in personal info  
    ("I'm 20 but trust me I know what I'm doing 😏", "I'm 20 but trust me I know what I'm doing 😏"),
    
    # "connecting with people" in hobbies
    ("connecting with people", "connecting with people"),
]

# Files to scan (HTML + Python generators)
EXTENSIONS = [".html", ".py", ".md"]

def scan_and_fix():
    fixed_files = []
    
    for root, dirs, files in os.walk(BASE):
        # Skip node_modules, .git, etc
        dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '__pycache__', '.cursor']]
        
        for fname in files:
            if not any(fname.endswith(ext) for ext in EXTENSIONS):
                continue
            
            fpath = os.path.join(root, fname)
            try:
                with open(fpath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except:
                continue
            
            original = content
            changes = []
            
            for old, new in REPLACEMENTS:
                if old in content:
                    count = content.count(old)
                    content = content.replace(old, new)
                    changes.append(f"  '{old[:50]}...' → '{new[:50]}...' ({count}x)")
            
            if content != original:
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                rel = os.path.relpath(fpath, BASE)
                fixed_files.append(rel)
                print(f"\n[FIXED] {rel}")
                for c in changes:
                    print(c)
    
    print(f"\n{'='*60}")
    print(f"Total files fixed: {len(fixed_files)}")
    return fixed_files

if __name__ == "__main__":
    scan_and_fix()
