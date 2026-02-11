"""
Fix banned words directly inside XLSX files.
Scans every cell text value and replaces banned phrases.
"""
import sys, os
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import openpyxl

REPLACEMENTS = [
    ("nice to meet you man", "glad you're here man"),
    ("hey man, nice to meet you. so what made you hit subscribe?", "hey man, glad you're here. so what made you hit subscribe?"),
    ("nice to meet you", "glad you're here"),
    ("I can't do shit about it", "I can't do anything about it"),
    ("I'm hard as fuck because of you and I can't do shit about it", "I'm hard as fuck because of you and I can't do anything about it"),
    ("I'm hard and I can't do shit about it because of you", "I'm hard and I can't do anything about it because of you"),
    ("holy shit 🥵 that was... wow", "holy fuck 🥵 that was... wow"),
    ("holy shit that is... fuck. I need to show you something rn", "oh fuck that is... damn. I need to show you something rn"),
    ("holy shit that is... fuckkk. I need to show you something rn", "oh fuck that is... damn. I need to show you something rn"),
    ("holy shit that is... fuck. I need to show you something right now", "oh fuck that is... damn. I need to show you something right now"),
    ("holy shit", "holy fuck"),
    ("I already sent you free shit man", "I already gave you a free one man"),
    ("there's a lot of fake shit on here", "there's a lot of fake stuff on here"),
    ("like you have your shit together", "like you have your life together"),
    ("I won't force you", "no pressure at all"),
    ("cycling vlogger! I record my rides and random moments from the road 🚴‍♀️", "biking vlogger! I record my rides and random moments from the road 🚴‍♀️"),
    ("cycling is my obsession", "biking is my obsession"),
    ("cycling vlogger", "biking vlogger"),
    ("Cycling vlogger", "Biking vlogger"),
    ("Cycling Vlogger", "Biking Vlogger"),
    ("meeting people", "connecting with people"),
    ("I'm 20. young but I know what I'm doing", "I'm 20 but trust me I know what I'm doing"),
    ("bore me to death", "are so boring honestly"),
]

def fix_xlsx(filepath):
    if not os.path.exists(filepath):
        print(f"[SKIP] Not found: {filepath}")
        return
    
    wb = openpyxl.load_workbook(filepath)
    total_fixes = 0
    
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for cell in row:
                if cell.value and isinstance(cell.value, str):
                    original = cell.value
                    for old, new in REPLACEMENTS:
                        if old in cell.value:
                            cell.value = cell.value.replace(old, new)
                    if cell.value != original:
                        total_fixes += 1
                        print(f"  [{ws.title}] Fixed: '{original[:60]}...' → '{cell.value[:60]}...'")
    
    if total_fixes > 0:
        wb.save(filepath)
        print(f"  → Saved {filepath} ({total_fixes} fixes)")
    else:
        print(f"  [OK] No banned words found in {os.path.basename(filepath)}")
    
    wb.close()
    return total_fixes

# Fix all XLSX files
xlsx_files = [
    r"c:\Users\34683\CW-ScriptManager\putri\Putri_Complete_Infloww.xlsx",
    r"c:\Users\34683\CW-ScriptManager\max\Max_Complete_Infloww.xlsx",
    r"c:\Users\34683\CW-ScriptManager\marco\Marco_Complete_Infloww.xlsx",
    r"c:\Users\34683\CW-ScriptManager\scripts\models\putri\Putri_New_Sub_Journey_Infloww.xlsx",
    r"c:\Users\34683\CW-ScriptManager\scripts\models\max\Max_DatingApp_Journey_Infloww.xlsx",
]

for f in xlsx_files:
    print(f"\n{'='*50}")
    print(f"Scanning: {os.path.basename(f)}")
    print(f"{'='*50}")
    fix_xlsx(f)

print("\n[DONE] All XLSX files scanned and fixed!")
