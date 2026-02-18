"""Compress all profile photos to max 200KB for faster GitHub Pages builds."""
import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import os
import glob
from PIL import Image

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAX_SIZE_KB = 200
MAX_DIMENSION = 800  # px — profile photos don't need to be huge

def compress_photo(path, max_kb=MAX_SIZE_KB, max_dim=MAX_DIMENSION):
    """Compress a photo to fit within max_kb and max_dim."""
    original_size = os.path.getsize(path)
    if original_size <= max_kb * 1024:
        return False, original_size, original_size

    img = Image.open(path)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    # Resize if too large
    w, h = img.size
    if max(w, h) > max_dim:
        ratio = max_dim / max(w, h)
        img = img.resize((int(w * ratio), int(h * ratio)), Image.LANCZOS)

    # Save with decreasing quality until under max_kb
    for quality in [85, 75, 65, 55, 45]:
        img.save(path, "JPEG", quality=quality, optimize=True)
        new_size = os.path.getsize(path)
        if new_size <= max_kb * 1024:
            return True, original_size, new_size

    # Last resort: even smaller
    img.save(path, "JPEG", quality=35, optimize=True)
    return True, original_size, os.path.getsize(path)


def main():
    patterns = [os.path.join(BASE, "*/profile.jpg"), os.path.join(BASE, "*/profile.png")]
    photos = []
    for pat in patterns:
        photos.extend(glob.glob(pat))

    total_saved = 0
    compressed_count = 0

    for path in sorted(photos):
        folder = os.path.basename(os.path.dirname(path))
        changed, old_size, new_size = compress_photo(path)
        if changed:
            saved = old_size - new_size
            total_saved += saved
            compressed_count += 1
            print(f"  [{folder}] {old_size//1024}KB → {new_size//1024}KB (saved {saved//1024}KB)")
        else:
            print(f"  [{folder}] {old_size//1024}KB — OK")

    print(f"\nCompressed {compressed_count} photos, saved {total_saved//1024}KB total")


if __name__ == "__main__":
    main()
