"""Deep scan all XLSX for any remaining banned words in message text."""
import sys, os
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import openpyxl
import re

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

XLSX_FILES = [
    r"c:\Users\34683\CW-ScriptManager\putri\Putri_Complete_Infloww.xlsx",
    r"c:\Users\34683\CW-ScriptManager\max\Max_Complete_Infloww.xlsx",
    r"c:\Users\34683\CW-ScriptManager\marco\Marco_Complete_Infloww.xlsx",
]

found_any = False
for fpath in XLSX_FILES:
    if not os.path.exists(fpath):
        print(f"[SKIP] {fpath}")
        continue
    print(f"\n{'='*50}")
    print(f"Scanning: {os.path.basename(fpath)}")
    print(f"{'='*50}")
    wb = openpyxl.load_workbook(fpath)
    file_clean = True
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for cell in row:
                if cell.value and isinstance(cell.value, str):
                    # Skip header row (Name, Text, Note)
                    if cell.row == 1:
                        continue
                    # Only check Text column (column B = 2) - the actual message
                    if cell.column != 2:
                        continue
                    text = cell.value.lower()
                    words = re.findall(r'\b\w+\b', text)
                    for w in BANNED:
                        if w in words:
                            print(f"  [!] [{ws.title}] Row {cell.row}: BANNED '{w}' in: {cell.value[:80]}")
                            found_any = True
                            file_clean = False
    if file_clean:
        print(f"  [OK] Clean!")
    wb.close()

if not found_any:
    print(f"\n{'='*50}")
    print("ALL XLSX FILES ARE CLEAN!")
    print(f"{'='*50}")
