"""Verify Zansi and Jockurworld configs."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

banned = ['meet','drink','drinking','drunk','dog','cycle','cycling','young','golden',
          'slave','knock','knocked','showers','toilet','animal','forced','force',
          'choking','teen','child','blood','whipped','jail','bait','consent',
          'entrance','farm','twelve','eleven','fifteen','pee','piss','poop',
          'vomit','bareback','fisting','gangbang','scat','escort','death','dead']

def check_model(name, module_path):
    ns = {"__file__": module_path, "__name__": "test"}
    with open(module_path, encoding='utf-8') as f:
        code = f.read().split('if __name__')[0]
    exec(code, ns)
    c = ns['config']
    j = c['journey']
    nr = c['nr_waves']
    pi = c['personal_info']
    ps = c['positive_spin']
    re = c['re_engagement']
    obj = c['obj_scripts']
    
    print(f"\n=== {name.upper()} ===")
    print(f"Journey: {len(j)} msgs")
    print(f"NR Waves: {len(nr)}")
    print(f"Personal Info: {len(pi)}")
    print(f"Positive Spin: {len(ps)}")
    print(f"Re-engagement: {len(re)}")
    print(f"OBJ sheets: {len(obj)}")
    print(f"Gender: {c['gender']}")
    print(f"Traffic: {c['traffic']}")
    
    issues = []
    # Check journey
    for mid, txt, note, mtype in j:
        words = txt.lower().replace(',', ' ').replace('.', ' ').replace('?', ' ').replace('!', ' ').split()
        for b in banned:
            if b in words:
                issues.append(f"JOURNEY {mid}: '{b}' in '{txt[:50]}'")
    # Check NR
    for mid, txt, note, mtype in nr:
        words = txt.lower().replace(',', ' ').replace('.', ' ').replace('?', ' ').replace('!', ' ').split()
        for b in banned:
            if b in words:
                issues.append(f"NR {mid}: '{b}' in '{txt[:50]}'")
    # Check PI
    for label, txt, note in pi:
        words = txt.lower().replace(',', ' ').replace('.', ' ').replace('?', ' ').replace('!', ' ').split()
        for b in banned:
            if b in words:
                issues.append(f"PI {label}: '{b}' in '{txt[:50]}'")
    # Check PS
    for label, txt, note in ps:
        words = txt.lower().replace(',', ' ').replace('.', ' ').replace('?', ' ').replace('!', ' ').split()
        for b in banned:
            if b in words:
                issues.append(f"PS {label}: '{b}' in '{txt[:50]}'")
    # Check RE
    for mid, txt, note, mtype in re:
        words = txt.lower().replace(',', ' ').replace('.', ' ').replace('?', ' ').replace('!', ' ').split()
        for b in banned:
            if b in words:
                issues.append(f"RE {mid}: '{b}' in '{txt[:50]}'")
    # Check OBJ
    for sn, (rows, cat) in obj.items():
        for step_name, txt, note in rows:
            words = txt.lower().replace(',', ' ').replace('.', ' ').replace('?', ' ').replace('!', ' ').split()
            for b in banned:
                if b in words:
                    issues.append(f"OBJ {sn}/{step_name}: '{b}' in '{txt[:50]}'")
    
    if issues:
        print("BANNED WORD ISSUES:")
        for i in issues:
            print(f"  {i}")
    else:
        print("NO banned words found in Text fields!")

check_model("Zansi", os.path.join(os.path.dirname(__file__), "zansi.py"))
check_model("Jockurworld", os.path.join(os.path.dirname(__file__), "jockurworld.py"))
