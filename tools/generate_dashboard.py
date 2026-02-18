"""Generate the main dashboard index.html with all models."""
import sys, os, glob
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE = r"c:\Users\34683\CW-ScriptManager"

# Define all models in display order
FEMALE_MODELS = [
    {"name": "Putri", "folder": "putri", "age": 25, "nationality": "Indonesian", "page": "Free Page", "traffic": "OFTV", "xlsx": "Putri_Complete_Infloww.xlsx"},
    {"name": "Riri VIP", "folder": "riri", "age": 22, "nationality": "Italian", "page": "Paid Page", "traffic": "OFTV / Others", "xlsx": "Riri_Complete_Infloww.xlsx"},
    {"name": "Eva Martinez", "folder": "eva", "age": 24, "nationality": "Colombian", "page": "Paid Page", "traffic": "IG/TikTok + Others", "xlsx": "Eva_Complete_Infloww.xlsx"},
    {"name": "Antonella", "folder": "antonella", "age": 19, "nationality": "American", "page": "Mixed", "traffic": "Reddit", "xlsx": "Antonella_Complete_Infloww.xlsx"},
    {"name": "Jasmine", "folder": "jasmine", "age": 25, "nationality": "Dominican", "page": "Free/Paid", "traffic": "IG/TikTok + Reddit", "xlsx": "Jasmine_Complete_Infloww.xlsx"},
    {"name": "Fernanda", "folder": "fernanda", "age": 46, "nationality": "Brazilian", "page": "Paid Page", "traffic": "IG/TikTok", "xlsx": "Fernanda_Complete_Infloww.xlsx"},
    {"name": "Isabella", "folder": "isabella", "age": 25, "nationality": "Colombian/Scottish", "page": "Free/Paid", "traffic": "Social Media", "xlsx": "Isabella_Complete_Infloww.xlsx"},
    {"name": "Jessica", "folder": "jessica", "age": 34, "nationality": "American", "page": "Mixed", "traffic": "Reddit", "xlsx": "Jessica_Complete_Infloww.xlsx", "tag": "non-explicit"},
    {"name": "Jessica FP", "folder": "jessica-fp", "age": 36, "nationality": "Argentinian", "page": "Free/Paid", "traffic": "Reddit + IG", "xlsx": "JessicaFP_Complete_Infloww.xlsx"},
    {"name": "Maddison", "folder": "maddison", "age": 18, "nationality": "American", "page": "Paid Page", "traffic": "Reddit", "xlsx": "Maddison_Complete_Infloww.xlsx"},
    {"name": "Vera", "folder": "vera", "age": 19, "nationality": "American", "page": "Free Page", "traffic": "Reddit", "xlsx": "Vera_Complete_Infloww.xlsx"},
    {"name": "Mia Luna", "folder": "mialuna", "age": 20, "nationality": "Argentinian", "page": "Free Page", "traffic": "Reddit", "xlsx": "MiaLuna_Complete_Infloww.xlsx"},
    {"name": "Mia Brooks", "folder": "miabrooks", "age": 23, "nationality": "Spanish", "page": "Free Page", "traffic": "IG/TikTok", "xlsx": "MiaBrooks_Complete_Infloww.xlsx"},
    {"name": "Ashley", "folder": "ashley", "age": 26, "nationality": "Spanish", "page": "Free Page", "traffic": "IG/TikTok", "xlsx": "Ashley_Complete_Infloww.xlsx"},
    {"name": "Chayla Grey", "folder": "chayla", "age": 24, "nationality": "Brazilian", "page": "Free Page", "traffic": "IG/TikTok", "xlsx": "ChaylaGrey_Complete_Infloww.xlsx"},
    {"name": "Emily Bell", "folder": "emilybell", "age": 21, "nationality": "Argentinian", "page": "Free Page", "traffic": "IG/TikTok", "xlsx": "EmilyBell_Complete_Infloww.xlsx"},
    {"name": "Lana Monroe", "folder": "lana", "age": 18, "nationality": "Argentinian", "page": "Free Page", "traffic": "IG/TikTok", "xlsx": "Lana_Complete_Infloww.xlsx"},
    {"name": "Lia Kuroki", "folder": "lia", "age": 22, "nationality": "Japanese", "page": "Free Page", "traffic": "IG/TikTok", "xlsx": "Lia_Complete_Infloww.xlsx"},
    {"name": "Lina", "folder": "lina", "age": 24, "nationality": "Spanish", "page": "Free Page", "traffic": "IG/TikTok", "xlsx": "Lina_Complete_Infloww.xlsx"},
    {"name": "Faby Monteiro", "folder": "faby", "age": 45, "nationality": "Brazilian", "page": "Paid Page", "traffic": "Other", "xlsx": "Faby_Complete_Infloww.xlsx"},
    {"name": "Irina", "folder": "irina", "age": 23, "nationality": "American/Russian", "page": "Free Page", "traffic": "IG/TikTok", "xlsx": "Irina_Complete_Infloww.xlsx", "tag": "non-explicit"},
    {"name": "Zansi", "folder": "zansi", "age": 26, "nationality": "American", "page": "Free Page", "traffic": "Social Media", "xlsx": "Zansi_Complete_Infloww.xlsx"},
    {"name": "Adriana Meran", "folder": "adrianameran", "age": 42, "nationality": "Ecuadorian", "page": "Paid Page", "traffic": "Reddit + IG", "xlsx": "Adriana_Meran_Complete_Infloww.xlsx"},
]

MALE_DATING_APP = [
    {"name": "Max", "folder": "max", "age": 20, "nationality": "Italian", "page": "Paid Page", "traffic": "Dating Apps (Gay)", "xlsx": "Max_Complete_Infloww.xlsx"},
    {"name": "Marco", "folder": "marco", "age": 25, "nationality": "Turkish", "page": "Paid Page", "traffic": "Dating Apps (Gay) + Others", "xlsx": "Marco_Complete_Infloww.xlsx"},
    {"name": "Lucas Passione", "folder": "lucas", "age": 24, "nationality": "Argentinian", "page": "Paid Page", "traffic": "Dating Apps", "xlsx": "Lucas_Passione_Complete_Infloww.xlsx"},
    {"name": "Liam", "folder": "liam", "age": 20, "nationality": "Argentinian", "page": "Paid Page", "traffic": "Dating Apps + Others", "xlsx": "Liam_Complete_Infloww.xlsx"},
    {"name": "Peter", "folder": "peter", "age": 20, "nationality": "American", "page": "Paid Page", "traffic": "Dating Apps", "xlsx": "Peter_Complete_Infloww.xlsx"},
    {"name": "Damon", "folder": "damon", "age": 24, "nationality": "Argentinian", "page": "Paid Page", "traffic": "Dating Apps + Others", "xlsx": "Damon_Complete_Infloww.xlsx"},
    {"name": "Stefan", "folder": "stefan", "age": 18, "nationality": "Argentinian", "page": "Paid Page", "traffic": "Dating Apps + Others", "xlsx": "Stefan_Complete_Infloww.xlsx"},
    {"name": "Zack", "folder": "zack", "age": 23, "nationality": "British", "page": "Paid Page", "traffic": "Dating Apps", "xlsx": "Zack_Complete_Infloww.xlsx"},
    {"name": "Noah", "folder": "noah", "age": 21, "nationality": "Italian", "page": "Paid Page", "traffic": "Dating Apps + Twitter/X", "xlsx": "Noah_Complete_Infloww.xlsx"},
    {"name": "Jack Hollywood", "folder": "jack", "age": 20, "nationality": "American", "page": "Paid Page", "traffic": "Dating Apps + Others", "xlsx": "Jack_Hollywood_Complete_Infloww.xlsx"},
]

MALE_OTHER = [
    {"name": "Jockurworld", "folder": "jockurworld", "age": 26, "nationality": "American", "page": "Paid Page", "traffic": "Twitter/X + Others", "xlsx": "Jockurworld_Complete_Infloww.xlsx"},
]

def _auto_discover_models():
    """Auto-discover model configs not yet in the hardcoded lists."""
    known_folders = set()
    for lst in [FEMALE_MODELS, MALE_DATING_APP, MALE_OTHER]:
        for m in lst:
            known_folders.add(m["folder"])

    models_dir = os.path.join(BASE, "tools", "models")
    new_models = []
    for py_file in sorted(glob.glob(os.path.join(models_dir, "*.py"))):
        if os.path.basename(py_file) == "__init__.py":
            continue
        folder = os.path.basename(py_file).replace(".py", "")
        if folder in known_folders:
            continue
        # Try to import config
        try:
            sys.path.insert(0, os.path.join(BASE, "tools"))
            mod = __import__(f"models.{folder}", fromlist=["config"])
            c = mod.config
            clean_name = c.get("name", folder).strip()
            xlsx_name = f"{clean_name.replace(' ', '_')}_Complete_Infloww.xlsx"
            entry = {
                "name": clean_name,
                "folder": c.get("folder", folder),
                "age": c.get("age", "?"),
                "nationality": c.get("nationality", "Unknown"),
                "page": c.get("page_type", "Mixed"),
                "traffic": c.get("traffic", "Social Media").replace("_", " ").title(),
                "xlsx": xlsx_name,
            }
            if c.get("explicit_level") in ("non_explicit", "soft"):
                entry["tag"] = "non-explicit"

            gender = c.get("gender", "female")
            traffic = c.get("traffic", "")
            if gender == "female":
                FEMALE_MODELS.append(entry)
            elif "dating" in traffic.lower():
                MALE_DATING_APP.append(entry)
            else:
                MALE_OTHER.append(entry)
            new_models.append(clean_name)
        except Exception as e:
            print(f"[WARN] Could not load {folder}: {e}")

    if new_models:
        print(f"[AUTO] Discovered {len(new_models)} new model(s): {', '.join(new_models)}")

_auto_discover_models()


def find_photo(folder):
    """Find profile photo in folder, return relative path or empty."""
    folder_path = os.path.join(BASE, folder)
    for ext in ["jpg", "jpeg", "png", "webp"]:
        for name in ["profile"]:
            p = os.path.join(folder_path, f"{name}.{ext}")
            if os.path.exists(p):
                return f"{folder}/{name}.{ext}"
    return ""

def make_card(m):
    tag_html = ""
    if m.get("tag") == "non-explicit":
        tag_html = '<span class="meta-tag ne-tag">NON-EXPLICIT</span>'

    # Photo thumbnail
    photo = find_photo(m["folder"])
    if photo:
        thumb_html = f'<img class="card-thumb" src="{photo}" alt="{m["name"]}" onerror="this.style.display=\'none\'">'
    else:
        # Fallback: initials circle
        initials = "".join(w[0].upper() for w in m["name"].split()[:2])
        thumb_html = f'<div class="card-thumb-fallback">{initials}</div>'

    # Data attributes for filtering
    page_lower = m["page"].lower()
    traffic_lower = m["traffic"].lower()
    is_ne = "true" if m.get("tag") == "non-explicit" else "false"
    search_text = f'{m["name"]} {m["nationality"]} {m["traffic"]} {m["page"]}'.lower()

    return f'''    <div class="card" data-name="{m["name"].lower()}" data-page="{page_lower}" data-traffic="{traffic_lower}" data-ne="{is_ne}" data-search="{search_text}">
      <div class="card-header">
        {thumb_html}
        <div class="card-name-wrap">
          <span class="card-name">{m["name"]}</span>
        </div>
        <span class="card-badge badge-live">LIVE</span>
      </div>
      <div class="card-meta">
        <span class="meta-tag">{m["age"]} yrs</span>
        <span class="meta-tag">{m["nationality"]}</span>
        <span class="meta-tag">{m["page"]}</span>
        {tag_html}
      </div>
      <div class="card-traffic">Traffic: <strong>{m["traffic"]}</strong></div>
      <div class="card-actions">
        <a href="{m["folder"]}/" class="btn-guide">Guide</a>
        <a href="{m["folder"]}/objections.html" class="btn-obj">OBJ/RES</a>
        <a href="{m["folder"]}/{m["xlsx"]}" download class="btn-xlsx">XLSX</a>
      </div>
    </div>'''


female_cards = "\n\n".join(make_card(m) for m in FEMALE_MODELS)
male_dating_cards = "\n\n".join(make_card(m) for m in MALE_DATING_APP)
male_other_cards = "\n\n".join(make_card(m) for m in MALE_OTHER)

total = len(FEMALE_MODELS) + len(MALE_DATING_APP) + len(MALE_OTHER)

# CW Logo — real logo
CW_LOGO_HEADER = '<img class="cw-logo" src="assets/cw-logo.png" alt="Chatting Wizard">'
CW_LOGO_FOOTER = '<img class="cw-logo-sm" src="assets/cw-logo.png" alt="Chatting Wizard">'

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CW Scripts — Chatting Wizard</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ background: #0d1117; color: #e6edf3; font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; min-height: 100vh; }}

  /* ── Header ── */
  .header {{ text-align: center; padding: 40px 20px 24px; }}
  .header-brand {{ display: flex; align-items: center; justify-content: center; gap: 14px; margin-bottom: 6px; }}
  .cw-logo {{ height: 44px; width: auto; }}
  .header h1 {{ font-size: 2em; color: #58a6ff; }}
  .header p {{ color: #8b949e; font-size: 0.95em; max-width: 500px; margin: 0 auto; }}
  .header .count {{ color: #3fb950; font-weight: 700; font-size: 1.05em; margin-top: 6px; }}

  /* ── Search + Filters ── */
  .search-bar {{ max-width: 500px; margin: 16px auto 0; position: relative; }}
  .search-bar input {{ width: 100%; background: #161b22; border: 1px solid #30363d; color: #e6edf3; padding: 10px 16px 10px 40px; border-radius: 10px; font-size: 0.95em; outline: none; transition: 0.15s; }}
  .search-bar input:focus {{ border-color: #58a6ff; box-shadow: 0 0 0 2px rgba(88,166,255,0.15); }}
  .search-bar input::placeholder {{ color: #484f58; }}
  .search-bar .s-icon {{ position: absolute; left: 14px; top: 50%; transform: translateY(-50%); color: #484f58; font-size: 0.9em; }}
  .filters {{ display: flex; gap: 6px; justify-content: center; margin: 14px 0 0; flex-wrap: wrap; }}
  .filter-btn {{ background: #161b22; border: 1px solid #30363d; color: #8b949e; padding: 4px 12px; border-radius: 20px; font-size: 0.73em; cursor: pointer; transition: 0.15s; white-space: nowrap; }}
  .filter-btn:hover {{ border-color: #58a6ff; color: #58a6ff; }}
  .filter-btn.active {{ background: #58a6ff; color: #0d1117; border-color: #58a6ff; font-weight: 600; }}

  /* ── Layout ── */
  .container {{ max-width: 1100px; margin: 0 auto; padding: 20px; }}
  .section-title {{ font-size: 1em; color: #8b949e; text-transform: uppercase; letter-spacing: 1px; margin: 36px 0 14px 0; padding-bottom: 8px; border-bottom: 1px solid #21262d; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 14px; }}

  /* ── Cards ── */
  .card {{ background: #161b22; border: 1px solid #30363d; border-radius: 12px; padding: 16px; transition: all 0.2s; }}
  .card:hover {{ border-color: #58a6ff; box-shadow: 0 4px 20px rgba(88,166,255,0.08); transform: translateY(-1px); }}
  .card-header {{ display: flex; align-items: center; gap: 10px; margin-bottom: 10px; }}
  .card-thumb {{ width: 36px; height: 36px; border-radius: 50%; object-fit: cover; border: 2px solid #30363d; flex-shrink: 0; }}
  .card-thumb-fallback {{ width: 36px; height: 36px; border-radius: 50%; background: #21262d; border: 2px solid #30363d; display: flex; align-items: center; justify-content: center; font-size: 0.7em; font-weight: 700; color: #8b949e; flex-shrink: 0; }}
  .card-name-wrap {{ flex: 1; min-width: 0; }}
  .card-name {{ font-size: 1.15em; font-weight: 700; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; display: block; }}
  .card-badge {{ font-size: 0.65em; padding: 2px 8px; border-radius: 20px; font-weight: 600; text-transform: uppercase; flex-shrink: 0; }}
  .badge-live {{ background: #3fb95022; color: #3fb950; border: 1px solid #3fb95044; }}
  .card-meta {{ display: flex; flex-wrap: wrap; gap: 5px; margin-bottom: 8px; }}
  .meta-tag {{ font-size: 0.7em; color: #8b949e; background: #1c2129; padding: 2px 7px; border-radius: 4px; }}
  .ne-tag {{ background: #f8514922; color: #f85149; }}
  .card-traffic {{ font-size: 0.8em; color: #8b949e; margin-bottom: 6px; }}
  .card-traffic strong {{ color: #e6edf3; }}
  .card-actions {{ display: flex; gap: 6px; margin-top: 10px; padding-top: 10px; border-top: 1px solid #21262d; }}
  .btn-guide, .btn-obj, .btn-xlsx {{ flex: 1; text-align: center; padding: 6px 8px; border-radius: 8px; font-size: 0.72em; font-weight: 600; text-decoration: none; transition: all 0.15s; }}
  .btn-guide {{ background: #58a6ff18; color: #58a6ff; border: 1px solid #58a6ff33; }}
  .btn-guide:hover {{ background: #58a6ff28; }}
  .btn-obj {{ background: #f8514918; color: #f85149; border: 1px solid #f8514933; }}
  .btn-obj:hover {{ background: #f8514928; }}
  .btn-xlsx {{ background: #3fb95018; color: #3fb950; border: 1px solid #3fb95033; }}
  .btn-xlsx:hover {{ background: #3fb95028; }}

  /* ── Alert bar ── */
  .alert-bar {{ background: #161b22; border: 1px solid #f8514933; border-radius: 10px; padding: 12px 18px; margin: 0 0 14px 0; display: flex; align-items: center; gap: 10px; }}
  .alert-bar .icon {{ font-size: 1.2em; }}
  .alert-bar .text {{ font-size: 0.85em; color: #f85149; }}
  .alert-bar .text strong {{ color: #e6edf3; }}

  /* ── Utilities ── */
  .card.hide {{ display: none; }}
  .no-results {{ text-align: center; padding: 40px 20px; color: #484f58; display: none; }}
  .footer {{ text-align: center; padding: 40px 20px; color: #484f58; font-size: 0.75em; }}
  .footer-brand {{ display: flex; align-items: center; justify-content: center; gap: 8px; margin-bottom: 4px; }}
  .cw-logo-sm {{ height: 20px; width: auto; }}
  @media (max-width: 600px) {{ .grid {{ grid-template-columns: 1fr; }} .header h1 {{ font-size: 1.5em; }} }}
</style>
</head>
<body>

<div class="header">
  <div class="header-brand">
    {CW_LOGO_HEADER}
  </div>
  <h1>Script Manager</h1>
  <p>Script guides &amp; XLSX exports for chatters</p>
  <div class="count">{total} creators live</div>
  <div class="search-bar">
    <span class="s-icon">&#128269;</span>
    <input type="text" id="dash-search" placeholder="Search by name, nationality, or traffic..." autocomplete="off">
  </div>
  <div class="filters">
    <button class="filter-btn active" data-filter="all">All</button>
    <button class="filter-btn" data-filter="free">Free Page</button>
    <button class="filter-btn" data-filter="paid">Paid Page</button>
    <button class="filter-btn" data-filter="nonexplicit">Non-Explicit</button>
    <button class="filter-btn" data-filter="reddit">Reddit</button>
    <button class="filter-btn" data-filter="ig">IG/TikTok</button>
    <button class="filter-btn" data-filter="dating">Dating Apps</button>
    <button class="filter-btn" data-filter="social">Social Media</button>
    <button class="filter-btn" data-filter="twitter">Twitter/X</button>
    <button class="filter-btn" data-filter="oftv">OFTV</button>
    <button class="filter-btn" data-filter="other">Other</button>
  </div>
</div>

<div class="container">

  <div class="section-title">Female Creators ({len(FEMALE_MODELS)})</div>
  <div class="grid">

{female_cards}

  </div>

  <div class="section-title">Male Creators — Dating App Traffic ({len(MALE_DATING_APP)})</div>
  <div class="alert-bar">
    <div class="icon">&#9888;&#65039;</div>
    <div class="text"><strong>Dating App Traffic:</strong> These creators have the Meetup Redirect (MR) module. NEVER say "meet/meeting" on OnlyFans.</div>
  </div>
  <div class="grid">

{male_dating_cards}

  </div>

  <div class="section-title">Male Creators — Other Traffic ({len(MALE_OTHER)})</div>
  <div class="grid">

{male_other_cards}

  </div>

</div>

<div class="footer">
  <div class="footer-brand">
    {CW_LOGO_FOOTER}
  </div>
  Script Manager — 2026 — Internal use only
</div>

<script>
// Search
const searchInput = document.getElementById('dash-search');
const cards = document.querySelectorAll('.card');

searchInput.addEventListener('input', () => {{
  const q = searchInput.value.toLowerCase().trim();
  // Reset active filter to "All" when searching
  document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
  document.querySelector('.filter-btn[data-filter="all"]').classList.add('active');
  cards.forEach(c => {{
    if (!q || c.dataset.search.includes(q)) {{
      c.classList.remove('hide');
    }} else {{
      c.classList.add('hide');
    }}
  }});
}});

// Filters
const filterBtns = document.querySelectorAll('.filter-btn');
filterBtns.forEach(btn => {{
  btn.addEventListener('click', () => {{
    filterBtns.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const f = btn.dataset.filter;
    cards.forEach(c => {{
      const t = c.dataset.traffic;
      const p = c.dataset.page;
      if (f === 'all') {{ c.classList.remove('hide'); return; }}
      if (f === 'free' && p.includes('free')) {{ c.classList.remove('hide'); return; }}
      if (f === 'paid' && p.includes('paid') && !p.includes('free')) {{ c.classList.remove('hide'); return; }}
      if (f === 'nonexplicit' && c.dataset.ne === 'true') {{ c.classList.remove('hide'); return; }}
      if (f === 'reddit' && t.includes('reddit')) {{ c.classList.remove('hide'); return; }}
      if (f === 'ig' && (t.includes('ig') || t.includes('tiktok'))) {{ c.classList.remove('hide'); return; }}
      if (f === 'dating' && t.includes('dating')) {{ c.classList.remove('hide'); return; }}
      if (f === 'social' && t.includes('social')) {{ c.classList.remove('hide'); return; }}
      if (f === 'twitter' && t.includes('twitter')) {{ c.classList.remove('hide'); return; }}
      if (f === 'oftv' && t.includes('oftv')) {{ c.classList.remove('hide'); return; }}
      if (f === 'other' && t.includes('other')) {{ c.classList.remove('hide'); return; }}
      c.classList.add('hide');
    }});
    searchInput.value = '';
  }});
}});
</script>

</body>
</html>
'''

output = os.path.join(BASE, "index.html")
with open(output, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Dashboard generated: {output}")
print(f"Female: {len(FEMALE_MODELS)} | Male Dating: {len(MALE_DATING_APP)} | Male Other: {len(MALE_OTHER)}")
print(f"Total: {total} creators")
