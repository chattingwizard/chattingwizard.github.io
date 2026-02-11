"""Generate the main dashboard index.html with all models."""
import sys, os
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE = r"c:\Users\34683\CW-ScriptManager"

# Define all models in display order
FEMALE_MODELS = [
    {"name": "Putri", "folder": "putri", "age": 25, "nationality": "Indonesian", "page": "Free Page", "traffic": "Social Media", "xlsx": "Putri_Complete_Infloww.xlsx"},
    {"name": "Riri VIP", "folder": "riri", "age": 22, "nationality": "Italian", "page": "Paid Page", "traffic": "OFTV / Social", "xlsx": "Riri_Complete_Infloww.xlsx"},
    {"name": "Eva Martinez", "folder": "eva", "age": 24, "nationality": "Colombian", "page": "Paid Page", "traffic": "IG/TikTok", "xlsx": "Eva_Complete_Infloww.xlsx"},
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
    {"name": "Irina", "folder": "irina", "age": 23, "nationality": "American/Russian", "page": "Paid Page", "traffic": "IG/TikTok", "xlsx": "Irina_Complete_Infloww.xlsx", "tag": "non-explicit"},
    {"name": "Zansi", "folder": "zansi", "age": 26, "nationality": "American", "page": "Free Page", "traffic": "Social Media", "xlsx": "Zansi_Complete_Infloww.xlsx"},
]

MALE_DATING_APP = [
    {"name": "Max", "folder": "max", "age": 20, "nationality": "Italian", "page": "Paid Page", "traffic": "Dating Apps (Gay)", "xlsx": "Max_Complete_Infloww.xlsx"},
    {"name": "Marco", "folder": "marco", "age": 25, "nationality": "Turkish", "page": "Paid Page", "traffic": "Dating Apps (Gay)", "xlsx": "Marco_Complete_Infloww.xlsx"},
]

MALE_OTHER = [
    {"name": "Jockurworld", "folder": "jockurworld", "age": 26, "nationality": "American", "page": "Paid Page", "traffic": "Twitter/X", "xlsx": "Jockurworld_Complete_Infloww.xlsx"},
]

def make_card(m):
    tag_html = ""
    if m.get("tag") == "non-explicit":
        tag_html = '<span class="meta-tag" style="background:#f8514922;color:#f85149">NON-EXPLICIT</span>'
    
    return f'''    <div class="card">
      <div class="card-header">
        <span class="card-name">{m["name"]}</span>
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
        <a href="{m["folder"]}/" class="btn-guide">📖 Guide</a>
        <a href="{m["folder"]}/objections.html" class="btn-guide" style="background:#f8514922;color:#f85149;border-color:#f8514944">🛡️ OBJ/RES</a>
        <a href="{m["folder"]}/{m["xlsx"]}" download class="btn-xlsx">📥 XLSX</a>
      </div>
    </div>'''


female_cards = "\n\n".join(make_card(m) for m in FEMALE_MODELS)
male_dating_cards = "\n\n".join(make_card(m) for m in MALE_DATING_APP)
male_other_cards = "\n\n".join(make_card(m) for m in MALE_OTHER)

# Pending males placeholder
pending_males = '''    <div class="empty-card">
      <div class="icon">🔜</div>
      <p>Lucas, Liam, Peter, Damon, Stefan, Zack, Noah, Jack Hollywood<br>Coming soon</p>
    </div>'''

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CW Scripts — Chatting Wizard</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ background: #0d1117; color: #e6edf3; font-family: 'Segoe UI', system-ui, sans-serif; min-height: 100vh; }}
  .header {{ text-align: center; padding: 50px 20px 30px; }}
  .header h1 {{ font-size: 2.2em; color: #58a6ff; margin-bottom: 8px; }}
  .header p {{ color: #8b949e; font-size: 1em; max-width: 500px; margin: 0 auto; }}
  .header .count {{ color: #3fb950; font-weight: 700; font-size: 1.1em; margin-top: 8px; }}
  .container {{ max-width: 1100px; margin: 0 auto; padding: 20px; }}
  .section-title {{ font-size: 1.1em; color: #8b949e; text-transform: uppercase; letter-spacing: 1px; margin: 40px 0 16px 0; padding-bottom: 8px; border-bottom: 1px solid #21262d; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 16px; }}
  .card {{ background: #161b22; border: 1px solid #30363d; border-radius: 12px; padding: 20px; transition: all 0.2s; }}
  .card:hover {{ border-color: #58a6ff; box-shadow: 0 4px 20px rgba(88,166,255,0.1); }}
  .card-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; }}
  .card-name {{ font-size: 1.3em; font-weight: 700; }}
  .card-badge {{ font-size: 0.7em; padding: 3px 10px; border-radius: 20px; font-weight: 600; text-transform: uppercase; }}
  .badge-live {{ background: #3fb95022; color: #3fb950; border: 1px solid #3fb95044; }}
  .card-meta {{ display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 10px; }}
  .meta-tag {{ font-size: 0.75em; color: #8b949e; background: #1c2129; padding: 2px 8px; border-radius: 4px; }}
  .card-traffic {{ font-size: 0.85em; color: #8b949e; margin-bottom: 8px; }}
  .card-traffic strong {{ color: #e6edf3; }}
  .card-actions {{ display: flex; gap: 8px; margin-top: 12px; padding-top: 12px; border-top: 1px solid #21262d; }}
  .btn-guide, .btn-xlsx {{ flex: 1; text-align: center; padding: 7px 10px; border-radius: 8px; font-size: 0.75em; font-weight: 600; text-decoration: none; transition: all 0.2s; }}
  .btn-guide {{ background: #58a6ff22; color: #58a6ff; border: 1px solid #58a6ff44; }}
  .btn-guide:hover {{ background: #58a6ff33; }}
  .btn-xlsx {{ background: #3fb95022; color: #3fb950; border: 1px solid #3fb95044; }}
  .btn-xlsx:hover {{ background: #3fb95033; }}
  .empty-card {{ background: #161b22; border: 1px dashed #30363d; border-radius: 12px; padding: 20px; text-align: center; color: #484f58; }}
  .empty-card .icon {{ font-size: 2em; margin-bottom: 8px; }}
  .alert-bar {{ background: #161b22; border: 1px solid #f8514933; border-radius: 10px; padding: 14px 20px; margin: 0 0 16px 0; display: flex; align-items: center; gap: 12px; }}
  .alert-bar .icon {{ font-size: 1.3em; }}
  .alert-bar .text {{ font-size: 0.9em; color: #f85149; }}
  .alert-bar .text strong {{ color: #e6edf3; }}
  .footer {{ text-align: center; padding: 50px 20px; color: #484f58; font-size: 0.8em; }}
  @media (max-width: 600px) {{ .grid {{ grid-template-columns: 1fr; }} .header h1 {{ font-size: 1.6em; }} }}
</style>
</head>
<body>

<div class="header">
  <h1>CW Scripts</h1>
  <p>Script guides for chatters — Chatting Wizard</p>
  <div class="count">{len(FEMALE_MODELS) + len(MALE_DATING_APP) + len(MALE_OTHER)} creators live</div>
</div>

<div class="container">

  <div class="section-title">Female Creators ({len(FEMALE_MODELS)})</div>
  <div class="grid">

{female_cards}

  </div>

  <div class="section-title">Male Creators — Dating App Traffic ({len(MALE_DATING_APP)})</div>
  <div class="alert-bar">
    <div class="icon">⚠️</div>
    <div class="text"><strong>Dating App Traffic:</strong> These creators have the Meetup Redirect (MR) module. NEVER say "meet/meeting" on OnlyFans.</div>
  </div>
  <div class="grid">

{male_dating_cards}

{pending_males}

  </div>

  <div class="section-title">Male Creators — Other Traffic ({len(MALE_OTHER)})</div>
  <div class="grid">

{male_other_cards}

  </div>

</div>

<div class="footer">
  Chatting Wizard — Script Manager — 2026<br>
  Internal use only
</div>

</body>
</html>
'''

output = os.path.join(BASE, "index.html")
with open(output, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Dashboard generated: {output}")
print(f"Female: {len(FEMALE_MODELS)} | Male Dating: {len(MALE_DATING_APP)} | Male Other: {len(MALE_OTHER)}")
print(f"Total: {len(FEMALE_MODELS) + len(MALE_DATING_APP) + len(MALE_OTHER)} creators")
