"""Fetch Justin Daniels profile photo from Airtable — handle HEIC conversion."""
import sys, os, requests
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from airtable_cli import get_headers, API_BASE

headers = get_headers()
r = requests.get(API_BASE, headers=headers, params={
    'filterByFormula': '{Model Name} = "Justin Daniels"',
})
r.raise_for_status()
records = r.json().get('records', [])

for rec in records:
    f = rec.get('fields', {})
    for key in sorted(f.keys()):
        val = f[key]
        if isinstance(val, list) and len(val) > 0 and isinstance(val[0], dict) and 'url' in val[0]:
            for att in val:
                fname = att.get('filename', 'unknown')
                if any(ext in fname.lower() for ext in ['.jpg', '.jpeg', '.png', '.webp', '.heic']):
                    url = att.get('url', '')
                    out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'justindaniels')
                    os.makedirs(out_dir, exist_ok=True)
                    
                    ext = os.path.splitext(fname)[1].lower()
                    temp_path = os.path.join(out_dir, f"profile_raw{ext}")
                    out_path = os.path.join(out_dir, "profile.jpg")
                    
                    print(f"Downloading {fname} -> {temp_path}")
                    img_r = requests.get(url)
                    if img_r.status_code == 200:
                        with open(temp_path, 'wb') as fp:
                            fp.write(img_r.content)
                        print(f"Saved! ({len(img_r.content)} bytes)")
                        
                        # Convert HEIC to JPG if needed
                        if ext == '.heic':
                            try:
                                from PIL import Image
                                import pillow_heif
                                pillow_heif.register_heif_opener()
                                img = Image.open(temp_path)
                                img = img.convert('RGB')
                                img.save(out_path, 'JPEG', quality=90)
                                print(f"Converted HEIC -> {out_path}")
                                os.remove(temp_path)
                            except ImportError:
                                print("[WARN] pillow-heif not installed. Trying raw save...")
                                # Try just renaming — sometimes Airtable serves JPG with HEIC extension
                                from PIL import Image
                                try:
                                    img = Image.open(temp_path)
                                    img = img.convert('RGB')
                                    img.save(out_path, 'JPEG', quality=90)
                                    print(f"Converted -> {out_path}")
                                    os.remove(temp_path)
                                except Exception as e2:
                                    print(f"[ERROR] Cannot convert: {e2}")
                        else:
                            # Already a supported format
                            if temp_path != out_path:
                                from PIL import Image
                                img = Image.open(temp_path)
                                img = img.convert('RGB')
                                img.save(out_path, 'JPEG', quality=90)
                                os.remove(temp_path)
                                print(f"Saved as {out_path}")
                    else:
                        print(f"FAILED: HTTP {img_r.status_code}")
                    break
            break
