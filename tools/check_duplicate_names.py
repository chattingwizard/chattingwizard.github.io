"""Scan all XLSX files for duplicate command names within each model."""
import os, sys, glob
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import openpyxl

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def check_xlsx(filepath):
    """Check a single XLSX for duplicate names. Returns list of dupes."""
    wb = openpyxl.load_workbook(filepath, read_only=True)
    all_names = {}  # name -> list of sheets
    
    for ws in wb.worksheets:
        for row in ws.iter_rows(min_row=2, max_col=1, values_only=True):
            name = row[0]
            if name and str(name).strip():
                name_str = str(name).strip()
                if name_str not in all_names:
                    all_names[name_str] = []
                all_names[name_str].append(ws.title)
    
    wb.close()
    
    dupes = {k: v for k, v in all_names.items() if len(v) > 1}
    return dupes

def main():
    pattern = os.path.join(BASE, "*", "*_Complete_Infloww.xlsx")
    files = sorted(glob.glob(pattern))
    
    total_dupes = 0
    models_with_dupes = 0
    
    for f in files:
        model = os.path.basename(os.path.dirname(f))
        dupes = check_xlsx(f)
        if dupes:
            models_with_dupes += 1
            print(f"\n[DUPES] {model}:")
            for name, sheets in sorted(dupes.items()):
                total_dupes += len(sheets) - 1
                print(f"  '{name}' appears {len(sheets)}x in: {', '.join(sheets)}")
    
    print(f"\n{'='*60}")
    print(f"Scanned {len(files)} XLSX files")
    print(f"Models with duplicates: {models_with_dupes}")
    print(f"Total duplicate names: {total_dupes}")

if __name__ == "__main__":
    main()
