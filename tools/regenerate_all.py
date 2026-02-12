"""
REGENERATE ALL — Rebuilds HTML & XLSX for every model after QA fixes.
Skips photo download (already done), only regenerates XLSX + HTML.
"""
import os, sys, importlib, glob

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from model_factory import ModelFactory

MODELS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")

# Get all model config files
model_files = sorted(glob.glob(os.path.join(MODELS_DIR, "*.py")))

# Exclude __init__.py
model_files = [f for f in model_files if not f.endswith("__init__.py")]

print(f"Found {len(model_files)} model configs to regenerate\n")

success = []
errors = []

for mf in model_files:
    module_name = os.path.basename(mf).replace(".py", "")
    try:
        # Import or reload the module
        if module_name in sys.modules:
            mod = importlib.reload(sys.modules[module_name])
        else:
            spec = importlib.util.spec_from_file_location(module_name, mf)
            mod = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = mod
            spec.loader.exec_module(mod)
        
        # Try both CONFIG and config
        config = getattr(mod, 'CONFIG', None) or getattr(mod, 'config', None)
        if not config:
            raise AttributeError("No CONFIG or config found")
        factory = ModelFactory(config)
        factory.ensure_dirs()
        
        # Skip photo download, just regenerate XLSX + HTML
        # Check if photo already exists
        web_dir = factory.web_dir
        for ext in [".jpg", ".jpeg", ".png"]:
            photo_path = os.path.join(web_dir, f"profile{ext}")
            if os.path.exists(photo_path):
                config["photo_file"] = f"profile{ext}"
                break
        
        factory.generate_merged_xlsx()
        factory.generate_guide_html()
        factory.generate_objections_html()
        
        success.append(config["name"])
        print(f"  [OK] {config['name']}\n")
        
    except Exception as e:
        errors.append((module_name, str(e)))
        print(f"  [ERROR] {module_name}: {e}\n")

print(f"\n{'='*60}")
print(f"REGENERATION COMPLETE")
print(f"{'='*60}")
print(f"Success: {len(success)}/{len(model_files)}")
if errors:
    print(f"\nERRORS ({len(errors)}):")
    for name, err in errors:
        print(f"  - {name}: {err}")
else:
    print("No errors!")
print(f"\nModels regenerated: {', '.join(success)}")
