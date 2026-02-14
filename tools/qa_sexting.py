"""QA check for sexting sequences across all models."""
import os, sys, glob
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import openpyxl

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def check_xlsx(filepath):
    wb = openpyxl.load_workbook(filepath, read_only=True)
    model = os.path.basename(os.path.dirname(filepath))
    
    sexting_sheets = [ws for ws in wb.worksheets if ws.title in ("sex2","sex3","sex4","sex5")]
    
    issues = []
    
    for ws in sexting_sheets:
        rows = list(ws.iter_rows(min_row=2, values_only=True))
        if not rows:
            issues.append(f"  {ws.title}: EMPTY SHEET")
            continue
        
        names = [r[0] for r in rows if r[0]]
        texts = [r[1] for r in rows if r[1]]
        
        # Check row count (should be ~27)
        if len(rows) < 20:
            issues.append(f"  {ws.title}: Only {len(rows)} rows (expected ~27)")
        
        # Check for unreplaced placeholders
        for r in rows:
            text = str(r[1]) if r[1] else ""
            note = str(r[2]) if r[2] else ""
            if "{pet}" in text or "{emoji}" in text or "{pet2}" in text:
                issues.append(f"  {ws.title}: Unreplaced placeholder in text: {text[:50]}")
            if "{pet}" in note or "{emoji}" in note:
                issues.append(f"  {ws.title}: Unreplaced placeholder in note: {note[:50]}")
        
        # Check PPV pricing in notes
        ppv_count = sum(1 for r in rows if r[2] and "SEND PPV" in str(r[2]))
        if ppv_count < 4:
            issues.append(f"  {ws.title}: Only {ppv_count} PPVs (expected 5 including PPV 0)")
        
        # Check unique names within sheet
        name_set = set()
        for n in names:
            if n in name_set:
                issues.append(f"  {ws.title}: Duplicate name within sheet: {n}")
            name_set.add(n)
    
    wb.close()
    return len(sexting_sheets), issues

def main():
    pattern = os.path.join(BASE, "*", "*_Complete_Infloww.xlsx")
    files = sorted(glob.glob(pattern))
    
    total_models = 0
    models_with_sexting = 0
    total_issues = 0
    
    for f in files:
        model = os.path.basename(os.path.dirname(f))
        total_models += 1
        n_sheets, issues = check_xlsx(f)
        
        if n_sheets > 0:
            models_with_sexting += 1
            status = "OK" if not issues else "ISSUES"
            print(f"[{status}] {model}: {n_sheets} sexting sheets")
            if issues:
                for i in issues:
                    print(f"  {i}")
                total_issues += len(issues)
        else:
            print(f"[SKIP] {model}: No sexting sheets (non-explicit)")
    
    print(f"\n{'='*60}")
    print(f"Models: {total_models}")
    print(f"Models with sexting: {models_with_sexting}")
    print(f"Models without (non-explicit): {total_models - models_with_sexting}")
    print(f"Issues found: {total_issues}")

if __name__ == "__main__":
    main()
