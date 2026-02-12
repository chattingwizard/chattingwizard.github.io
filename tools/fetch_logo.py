"""Fetch CW logo from various sources."""
import requests, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

sources = [
    ("Wayback 2025", "https://web.archive.org/web/2025/https://chattingwizard.com/wp-content/uploads/2024/05/Logo-1.webp"),
    ("Wayback 2024", "https://web.archive.org/web/2024/https://chattingwizard.com/wp-content/uploads/2024/05/Logo-1.webp"),
    ("Wayback main", "https://web.archive.org/web/2025/https://chattingwizard.com/wp-content/uploads/2024/05/Logo-1.png"),
    ("CW direct png", "https://chattingwizard.com/wp-content/uploads/2024/05/Logo-1.png"),
    ("CW apple-touch", "https://chattingwizard.com/wp-content/uploads/2024/05/cropped-Logo-1-180x180.png"),
]

for label, url in sources:
    try:
        r = requests.get(url, headers=h, timeout=15, allow_redirects=True)
        ct = r.headers.get('content-type', '?')
        print(f"{label}: {r.status_code} | {len(r.content)} bytes | {ct}")
        if r.status_code == 200 and len(r.content) > 1000:
            ext = "webp" if "webp" in ct else "png" if "png" in ct else "jpg"
            fname = f"assets/cw-logo.{ext}"
            with open(fname, "wb") as f:
                f.write(r.content)
            print(f"  -> SAVED: {fname}")
            break
    except Exception as e:
        print(f"{label}: ERROR - {e}")
