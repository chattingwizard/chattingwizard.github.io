"""Generate Justin Daniels scripts, compress, dashboard."""
import sys, os
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from onboard_model import generate_model, update_dashboard

print("=== Generating Justin Daniels scripts ===")
success = generate_model("justindaniels")
if success:
    print("[OK] Generation complete")
    print("\n=== Compressing photos ===")
    import compress_photos
    compress_photos.main()
    print("\n=== Updating dashboard ===")
    update_dashboard()
    print("[OK] All done")
else:
    print("[FAILED] Generation error")
