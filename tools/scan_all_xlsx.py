"""Scan ALL XLSX files in the project for banned words."""
import sys, os, re
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import openpyxl

BANNED = [
    'shit', 'meet', 'drink', 'drinking', 'drunk', 'drunken', 'dog', 'cycle', 'cycling',
    'young', 'golden', 'slave', 'slavery', 'knock', 'knocked', 'knocking', 'showers',
    'toilet', 'animal', 'forced', 'force', 'forcing', 'teen', 'child', 'blood',
    'bleeding', 'whipped', 'whipping', 'jail', 'jailed', 'bait', 'consent',
    'entrance', 'farm', 'twelve', 'eleven', 'fifteen', 'pee', 'piss', 'poop',
    'vomit', 'dead', 'death', 'rape', 'choke', 'choking', 'slave', 'torture',
    'abduct', 'kidnap', 'strangle', 'suffocate', 'chloroform', 'unconscious',
    'bareback', 'fisting', 'gangbang', 'scat', 'incest', 'escort', 'hooker',
    'prostitute', 'underage', 'lolita', 'lactation', 'menstrual', 'pedo',
]

BASE = r"c:\Users\34683\CW-ScriptManager"
found_any = False
total_files = 0

for root, dirs, files in os.walk(BASE):
    dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '__pycache__', '.cursor']]
    for fname in files:
        if not fname.endswith('.xlsx'):
            continue
        fpath = os.path.join(root, fname)
        total_files += 1
        try:
            wb = openpyxl.load_workbook(fpath)
        except:
            continue
        file_clean = True
        for ws in wb.worksheets:
            for row in ws.iter_rows():
                for cell in row:
                    if cell.value and isinstance(cell.value, str) and cell.row > 1 and cell.column == 2:
                        words = re.findall(r'\b\w+\b', cell.value.lower())
                        for w in BANNED:
                            if w in words:
                                rel = os.path.relpath(fpath, BASE)
                                print(f"[!] {rel} [{ws.title}] Row {cell.row}: '{w}' in: {cell.value[:80]}")
                                found_any = True
                                file_clean = False
        wb.close()
        if file_clean:
            rel = os.path.relpath(fpath, BASE)
            print(f"  [OK] {rel}")

print(f"\n{'='*50}")
print(f"Scanned {total_files} XLSX files")
if not found_any:
    print("ALL CLEAN!")
else:
    print("VIOLATIONS FOUND - FIX REQUIRED")
