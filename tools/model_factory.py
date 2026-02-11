"""
MODEL FACTORY — Master generator for Chatting Wizard
Generates complete package for any model:
  1. Journey XLSX (all sheets)
  2. OBJ/RES/SIT XLSX (29 sheets)
  3. Merged single XLSX
  4. HTML chatter guide
  5. HTML objections guide
  6. Downloads profile photo
  7. Updates dashboard

Usage:
  from model_factory import ModelFactory
  m = ModelFactory(model_config)
  m.generate_all()
"""
import os, sys, json, requests
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import openpyxl
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from copy import copy

# ══════════════════════════════════════════
# STYLE CONSTANTS
# ══════════════════════════════════════════
HEADER_FILL = PatternFill("solid", fgColor="FF4472C4")
HEADER_FONT = Font(bold=True, color="FFFFFF", size=11)
PPV_FILL = PatternFill("solid", fgColor="FFF6B26B")
WAIT_FILL = PatternFill("solid", fgColor="FFFFF2CC")
GREEN_FILL = PatternFill("solid", fgColor="FFD9EAD3")
PURPLE_FILL = PatternFill("solid", fgColor="FFD9D2E9")
AC_FILL = PatternFill("solid", fgColor="FFD0E0E3")
BLUE1 = PatternFill("solid", fgColor="FFCFE2F3")
BLUE2 = PatternFill("solid", fgColor="FFE0F7FA")
OBJ_HDR = PatternFill("solid", fgColor="1a1a2e")
OBJ_HDR_FONT = Font(bold=True, color="e6edf3", size=11)
OBJ_FILL = PatternFill("solid", fgColor="2d1a1a")
RES_FILL = PatternFill("solid", fgColor="1f1a2d")
SIT_FILL = PatternFill("solid", fgColor="1a2a1a")
WRAP = Alignment(wrap_text=True, vertical="top")
THIN = Border(bottom=Side(style="thin", color="30363d"))

GUIDELINES = """Character limits
Name: Up to 64 characters
Tag: Up to 32 characters
Text: Up to 1000 characters
Note: Up to 246 characters

Each sheet serves as a tag. Simply replace the sheet name with your desired tag name, and all scripts added to the sheet will be automatically assigned that tag once imported."""


def setup_journey_sheet(ws):
    ws.append(["Name", "Text", "Note", "*Guidelines"])
    for cell in ws[1]:
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(horizontal="center")
    ws.column_dimensions['A'].width = 16
    ws.column_dimensions['B'].width = 80
    ws.column_dimensions['C'].width = 45
    ws.column_dimensions['D'].width = 20


def add_rows_reversed(ws, rows):
    reversed_rows = list(reversed(rows))
    fill_map = {
        "ppv": PPV_FILL, "wait": WAIT_FILL, "rapport": GREEN_FILL,
        "teasing": PURPLE_FILL, "aftercare": AC_FILL
    }
    for idx, (name, text, note, row_type) in enumerate(reversed_rows):
        row_num = idx + 2
        ws.cell(row=row_num, column=1, value=name)
        ws.cell(row=row_num, column=2, value=text)
        ws.cell(row=row_num, column=3, value=note or "")
        if idx == 0:
            ws.cell(row=row_num, column=4, value=GUIDELINES)
        fill = fill_map.get(row_type)
        if row_type == "sext":
            fill = BLUE1 if idx % 2 == 0 else BLUE2
        if fill:
            for col in range(1, 4):
                ws.cell(row=row_num, column=col).fill = fill
        for col in range(1, 4):
            ws.cell(row=row_num, column=col).alignment = WRAP


def make_obj_sheet(wb, title, rows, fill):
    ws = wb.create_sheet(title)
    ws.append(["Name", "Text", "Note", "*Guidelines"])
    for c in ["A","B","C","D"]:
        ws[f"{c}1"].fill = OBJ_HDR
        ws[f"{c}1"].font = OBJ_HDR_FONT
    ws.column_dimensions["A"].width = 20
    ws.column_dimensions["B"].width = 80
    ws.column_dimensions["C"].width = 50
    ws.column_dimensions["D"].width = 25
    for name, text, note in reversed(rows):
        ws.append([name, text, note, ""])
        r = ws.max_row
        for col in range(1, 5):
            cell = ws.cell(row=r, column=col)
            cell.alignment = WRAP
            cell.border = THIN
            if fill:
                cell.fill = fill


def add_standalone_rows(ws, rows):
    """Add rows without reversing (for Personal Info, Positive Spin)."""
    for idx, (name, text, note) in enumerate(rows):
        row_num = idx + 2
        ws.cell(row=row_num, column=1, value=name)
        ws.cell(row=row_num, column=2, value=text)
        ws.cell(row=row_num, column=3, value=note or "")
        if idx == 0:
            ws.cell(row=row_num, column=4, value=GUIDELINES)
        for col in range(1, 4):
            ws.cell(row=row_num, column=col).alignment = WRAP


def merge_workbooks(wb_journey, wb_obj, output_path):
    """Merge two workbooks into one."""
    wb_out = openpyxl.Workbook()
    
    first = True
    for wb in [wb_journey, wb_obj]:
        for ws in wb.worksheets:
            if first:
                dst = wb_out.active
                dst.title = ws.title
                first = False
            else:
                dst = wb_out.create_sheet(ws.title)
            
            for col_letter, col_dim in ws.column_dimensions.items():
                dst.column_dimensions[col_letter].width = col_dim.width
            
            for row in ws.iter_rows():
                for cell in row:
                    new_cell = dst.cell(row=cell.row, column=cell.column, value=cell.value)
                    if cell.has_style:
                        new_cell.font = copy(cell.font)
                        new_cell.fill = copy(cell.fill)
                        new_cell.alignment = copy(cell.alignment)
                        new_cell.border = copy(cell.border)
                        new_cell.number_format = cell.number_format
    
    wb_out.save(output_path)
    sheets = [ws.title for ws in wb_out.worksheets]
    total = sum(ws.max_row - 1 for ws in wb_out.worksheets)
    return len(sheets), total


def download_photo(model_name, dest_folder):
    """Download profile photo from Airtable."""
    token = os.environ.get("AIRTABLE_TOKEN", "")
    if not token:
        print(f"  [SKIP] No AIRTABLE_TOKEN for photo download")
        return None
    
    base_id = "appy0qGaMEfyDz9LZ"
    table_id = "tbl97sE9V8wbcgjAJ"
    
    formula = f"{{Model Name}} = '{model_name}'"
    r = requests.get(
        f"https://api.airtable.com/v0/{base_id}/{table_id}",
        headers={"Authorization": f"Bearer {token}"},
        params={"filterByFormula": formula, "fields[]": ["Profile Picture"]}
    )
    data = r.json()
    records = data.get("records", [])
    if not records:
        print(f"  [SKIP] No Airtable record for '{model_name}'")
        return None
    
    pics = records[0].get("fields", {}).get("Profile Picture", [])
    if not pics:
        print(f"  [SKIP] No profile picture for '{model_name}'")
        return None
    
    url = pics[0].get("url", "")
    if not url:
        return None
    
    ext = ".jpg"
    if "png" in url.lower():
        ext = ".png"
    elif "jpeg" in url.lower() or "jpg" in url.lower():
        ext = ".jpeg"
    
    dest = os.path.join(dest_folder, f"profile{ext}")
    img_data = requests.get(url).content
    with open(dest, "wb") as f:
        f.write(img_data)
    print(f"  [OK] Photo saved: {dest}")
    return f"profile{ext}"


# ══════════════════════════════════════════
# MAIN FACTORY CLASS
# ══════════════════════════════════════════

class ModelFactory:
    """
    config = {
        "name": "Marco",
        "airtable_name": "Marco",       # Name in Airtable
        "folder": "marco",              # Folder name for web
        "gender": "male",               # male/female
        "traffic": "dating_app",        # dating_app / social_media
        "age": 25,
        "nationality": "Turkish",
        "location": "Texas, USA",
        "page_type": "Paid Page",
        "personality": "Masculine, confident, in control...",
        "voice": "Lowercase. Direct. Short. Confident...",
        "voice_pet_names": "bro, man, dude",
        "voice_never": "baby, babe, honey",
        "interests": ["gym", "meat", "travel", "role-play"],
        "physical": "175cm, 82kg, brown hair, brown eyes, no tattoos",
        "job": "Gym instructor",
        "countries": "USA, Turkey, Spain, Poland, France",
        "key_phrases": ["...", "..."],
        "explicit_level": "full",       # full / non_explicit / soft
        "special_notes": "...",
        
        # Content for scripts (provided per model)
        "journey": [...],               # List of journey messages
        "obj_scripts": {...},           # OBJ/RES/SIT data
        "personal_info": [...],
        "positive_spin": [...],
        "nr_waves": [...],
        # Dating app specific:
        "meetup_redirect": [...],
        "location_handling": [...],
        "re_engagement": [...],
    }
    """
    
    def __init__(self, config):
        self.c = config
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.web_dir = os.path.join(self.base_dir, self.c["folder"])
        self.scripts_dir = os.path.join(self.base_dir, "scripts", "models", self.c["folder"])
        
    def ensure_dirs(self):
        os.makedirs(self.web_dir, exist_ok=True)
        os.makedirs(self.scripts_dir, exist_ok=True)
        print(f"[DIRS] {self.web_dir}, {self.scripts_dir}")
    
    def generate_journey_xlsx(self):
        """Generate the journey workbook (returns wb, not saved yet)."""
        wb = openpyxl.Workbook()
        
        # Sheet 1: Main Journey
        sheet_name = f"{self.c['name']}Journey"
        if len(sheet_name) > 31:
            sheet_name = sheet_name[:31]
        ws1 = wb.active
        ws1.title = sheet_name
        setup_journey_sheet(ws1)
        add_rows_reversed(ws1, self.c["journey"])
        
        # Meetup Redirect (dating app only)
        if self.c.get("meetup_redirect"):
            ws = wb.create_sheet("MeetupRedirect")
            setup_journey_sheet(ws)
            add_rows_reversed(ws, self.c["meetup_redirect"])
        
        # NR Waves
        if self.c.get("nr_waves"):
            ws = wb.create_sheet("NRWaves")
            setup_journey_sheet(ws)
            add_rows_reversed(ws, self.c["nr_waves"])
        
        # Personal Info
        if self.c.get("personal_info"):
            ws = wb.create_sheet(f"Personal{self.c['name']}"[:31])
            setup_journey_sheet(ws)
            add_standalone_rows(ws, self.c["personal_info"])
        
        # Positive Spin
        if self.c.get("positive_spin"):
            ws = wb.create_sheet("PositiveSpin")
            setup_journey_sheet(ws)
            add_standalone_rows(ws, self.c["positive_spin"])
        
        # Location Handling (dating app only)
        if self.c.get("location_handling"):
            ws = wb.create_sheet("LocationHandling")
            setup_journey_sheet(ws)
            add_standalone_rows(ws, self.c["location_handling"])
        
        # Re-Engagement
        if self.c.get("re_engagement"):
            ws = wb.create_sheet("ReEngagement")
            setup_journey_sheet(ws)
            add_rows_reversed(ws, self.c["re_engagement"])
        
        return wb
    
    def generate_obj_xlsx(self):
        """Generate OBJ/RES/SIT workbook (returns wb)."""
        wb = openpyxl.Workbook()
        
        obj = self.c.get("obj_scripts", {})
        for sheet_name, (rows, category) in obj.items():
            fill = {"obj": OBJ_FILL, "res": RES_FILL, "sit": SIT_FILL}.get(category, OBJ_FILL)
            make_obj_sheet(wb, sheet_name, rows, fill)
        
        if "Sheet" in wb.sheetnames:
            del wb["Sheet"]
        
        return wb
    
    def generate_merged_xlsx(self):
        """Generate and save the merged XLSX."""
        wb_j = self.generate_journey_xlsx()
        wb_o = self.generate_obj_xlsx()
        
        output = os.path.join(self.web_dir, f"{self.c['name']}_Complete_Infloww.xlsx")
        n_sheets, n_scripts = merge_workbooks(wb_j, wb_o, output)
        print(f"[XLSX] {output} — {n_sheets} sheets, {n_scripts} scripts")
        return output
    
    def download_profile_photo(self):
        """Download profile photo from Airtable."""
        photo = download_photo(self.c["airtable_name"], self.web_dir)
        if photo:
            self.c["photo_file"] = photo
        return photo
    
    def generate_all(self):
        """Generate everything for this model."""
        print(f"\n{'='*60}")
        print(f"GENERATING: {self.c['name']}")
        print(f"{'='*60}")
        
        self.ensure_dirs()
        self.download_profile_photo()
        xlsx_path = self.generate_merged_xlsx()
        # HTML generation would go here (guide + objections pages)
        
        print(f"[DONE] {self.c['name']} complete!")
        return xlsx_path


if __name__ == "__main__":
    print("ModelFactory ready. Import and use with model configs.")
    print("Example: from model_factory import ModelFactory")
