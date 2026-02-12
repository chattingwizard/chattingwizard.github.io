import os, sys, importlib.util
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
models_dir = os.path.join(os.path.dirname(__file__), 'models')
for f in sorted(os.listdir(models_dir)):
    if not f.endswith('.py') or f in ('__init__.py','test_write.py'): continue
    path = os.path.join(models_dir, f)
    spec = importlib.util.spec_from_file_location(f[:-3], path)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
        c = getattr(mod,'CONFIG',None) or getattr(mod,'config',None)
        if not c: continue
        pet = c.get('voice_pet_names','?')
        expl = c.get('explicit_level','?')
        gender = c.get('gender','?')
        pers = c.get('personality','')[:70]
        print(f'{c["name"]:15s} | {expl:15s} | {gender:6s} | {pet:30s} | {pers}')
    except Exception as e:
        print(f'{f:15s} | ERROR: {e}')
