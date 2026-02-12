# -*- coding: utf-8 -*-
"""
SEXTING INTENSITY ESCALATION AUDIT
===================================
Audits ALL model config files against the framework intensity curve.

Framework target:
  Phase 1 (build to PPV 1): 6->7->8  => avg target ~7.0
  Phase 2 (build to PPV 2): 8->9     => avg target ~8.5
  Phase 3 (build to PPV 3): 9->10    => avg target ~9.5
  Phase 4 (build to PPV 4): 10       => avg target ~9.8
"""

import sys
import os
import re
import importlib.util

# ============================================================
# KEYWORD-BASED INTENSITY SCORER
# ============================================================

# Score tiers: highest matching tier wins
KEYWORD_TIERS = [
    # (score, keywords_list) - checked from HIGHEST to LOWEST
    (10, [
        "cumming", "i'm cumming", "im cumming", "coming for you",
        "right there", "don't stop", "dont stop", "oh fuck don't",
        "oh fuck dont", "let go", "i'm about to cum", "im about to cum",
        "about to finish", "about to cum", "finishing", "i'm finishing",
        "cum with me", "cum together", "finish together", "finish with you",
        "cum for me", "cum inside",
    ]),
    (9, [
        "i need to cum", "need to cum", "make me cum", "wanna cum",
        "want to cum", "so close", "i'm close", "im close",
        "can't hold", "cant hold", "i can't take it", "i cant take it",
        "i'm gonna", "im gonna", "orgasm", "climax",
        "cum so bad", "cum so hard",
    ]),
    (8, [
        "fuck my", "ride you", "ride me", "want to ride",
        "your cock", "my cock", "suck", "taste you", "taste me",
        "inside me", "inside you", "pound", "deeper",
        "i need you inside", "put it in", "fill me",
        "your dick", "my dick",
        "pinning you down", "taking control",
        "grab my", "grab your",
    ]),
    (7, [
        "cock", "pussy", "fuck", "dick",
        "mouth on", "i want your", "you want my",
        "so wet", "so hard", "dripping",
        "can feel you", "feel your",
        "moaning", "moan",
        "naked", "undress",
        "stroking", "stroke",
        "barely wearing",
    ]),
    (6, [
        "turned on", "turn me on", "can't stop", "cant stop",
        "touch myself", "touching myself", "touching me",
        "body", "lying here", "lying in bed",
        "getting wet", "i'm wet", "im wet",
        "naughty", "making me feel things",
        "what i do when", "see what i do",
        "i want to show", "want to show you",
        "can't resist", "cant resist",
        "you're doing to me", "doing something to me",
        "you make me feel",
    ]),
    (5, [
        "feel things", "feeling things", "warm", "hot",
        "restless", "in a mood", "in the mood",
        "doing things to me", "this convo",
        "bored in bed", "feel some type of way",
        "making me blush", "can't help it", "cant help it",
    ]),
    (4, [
        "nervous", "thinking about", "want to show",
        "confident", "brave", "push my limits",
        "comfortable", "safe enough",
        "flirty", "tease",
    ]),
    (3, [
        "feel", "vibes", "mood", "energy",
        "something about you", "different",
        "i don't know", "i cant explain",
    ]),
    (2, [
        "you like it", "you like that", "oh my god", "omg",
        "wait", "hold on", "one second", "one sec", "give me a sec",
        "knew you'd like", "knew you would",
    ]),
    (1, [
        "so?", "soo?", "sooo?", "did you", "watch it",
        "you watched", "did you see",
    ]),
]


def score_message(text):
    """Score a message's sexual intensity on 1-10 scale using keyword matching."""
    text_lower = text.lower().strip()

    # Check tiers from highest to lowest
    for score, keywords in KEYWORD_TIERS:
        for kw in keywords:
            if kw in text_lower:
                return score

    # Fallback: no keywords matched
    # Short exclamatory messages (under 15 chars) with punctuation => reaction (2)
    if len(text_lower) < 15:
        if any(c in text_lower for c in ['!', '?', '...']):
            return 2
        # Very short messages are usually reactions
        return 2

    # Medium messages with no sexual keywords => probably 3
    if len(text_lower) < 60:
        return 3

    # Longer descriptive messages without keywords => 4
    return 4


# ============================================================
# PHASE EXTRACTION
# ============================================================

def extract_phases(journey):
    """
    Split journey into 4 sexting phases based on PPV boundaries.

    Phase 1: first S1-* message after last TB PPV, up to first PPV (PPV 1)
    Phase 2: messages after PPV 1 to PPV 2
    Phase 3: messages after PPV 2 to PPV 3
    Phase 4: messages after PPV 3 to PPV 4
    """
    # Find all PPV indices (phase_type == "ppv")
    ppv_indices = []
    for i, msg in enumerate(journey):
        if len(msg) >= 4 and msg[3] == "ppv":
            ppv_indices.append(i)

    if len(ppv_indices) < 2:
        return None  # Not enough PPVs to analyze

    # PPV 0 is the first ppv (TB-5 usually), PPV 1 is second, etc.
    # Phase 1: messages between PPV 0 and PPV 1
    # Phase 2: messages between PPV 1 and PPV 2
    # Phase 3: messages between PPV 2 and PPV 3
    # Phase 4: messages between PPV 3 and PPV 4

    phases = {}
    phase_names = ["Phase 1 (->PPV1)", "Phase 2 (->PPV2)", "Phase 3 (->PPV3)", "Phase 4 (->PPV4)"]

    for phase_idx in range(min(4, len(ppv_indices) - 1)):
        start = ppv_indices[phase_idx] + 1  # after previous PPV
        end = ppv_indices[phase_idx + 1]     # up to (not including) next PPV

        text_messages = []
        for i in range(start, end):
            msg = journey[i]
            if len(msg) >= 4:
                msg_id, text, note, phase_type = msg[0], msg[1], msg[2], msg[3]
            else:
                continue

            # Skip waits and non-text messages
            if phase_type == "wait":
                continue
            if phase_type == "ppv":
                continue

            text_messages.append((msg_id, text, score_message(text)))

        if text_messages:
            phases[phase_names[phase_idx]] = text_messages

    return phases


# ============================================================
# TARGET INTENSITIES (from framework)
# ============================================================
TARGETS = {
    "Phase 1 (->PPV1)": 7.0,   # build 6->7->8
    "Phase 2 (->PPV2)": 8.5,   # build 8->9
    "Phase 3 (->PPV3)": 9.5,   # 9->10
    "Phase 4 (->PPV4)": 9.8,   # maintain 10
}


# ============================================================
# MAIN AUDIT
# ============================================================

def load_model_config(filepath):
    """Dynamically load a model .py file and extract the config dict."""
    spec = importlib.util.spec_from_file_location("model_module", filepath)
    module = importlib.util.module_from_spec(spec)

    # We need to handle the import of model_factory
    # Add the tools directory to path temporarily
    tools_dir = os.path.dirname(os.path.dirname(filepath))
    old_path = sys.path.copy()
    sys.path.insert(0, tools_dir)
    sys.path.insert(0, os.path.dirname(filepath))

    try:
        spec.loader.exec_module(module)
        config = getattr(module, 'config', None)
        return config
    except Exception as e:
        return str(e)
    finally:
        sys.path = old_path


def run_audit():
    models_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")
    skip_files = {"__init__.py", "test_write.py"}

    model_files = sorted([
        f for f in os.listdir(models_dir)
        if f.endswith(".py") and f not in skip_files
    ])

    print("=" * 80)
    print("SEXTING INTENSITY ESCALATION AUDIT")
    print("=" * 80)
    print(f"\nModels found: {len(model_files)}")
    print(f"Framework targets: {TARGETS}")
    print()

    results = []  # (model_name, total_delta, phase_data)

    for filename in model_files:
        filepath = os.path.join(models_dir, filename)
        model_name = filename.replace(".py", "").upper()

        print("-" * 80)
        print(f"MODEL: {model_name}")
        print("-" * 80)

        config = load_model_config(filepath)
        if isinstance(config, str):
            print(f"  ERROR loading: {config}")
            print()
            continue
        if config is None:
            print(f"  ERROR: no config found")
            print()
            continue

        journey = config.get("journey", [])
        if not journey:
            print(f"  ERROR: no journey found")
            print()
            continue

        phases = extract_phases(journey)
        if phases is None:
            print(f"  ERROR: not enough PPV messages to extract phases")
            print()
            continue

        total_delta = 0.0
        phase_data = {}

        for phase_name in ["Phase 1 (->PPV1)", "Phase 2 (->PPV2)", "Phase 3 (->PPV3)", "Phase 4 (->PPV4)"]:
            if phase_name not in phases:
                print(f"  {phase_name}: NO MESSAGES FOUND")
                continue

            messages = phases[phase_name]
            scores = [s for _, _, s in messages]
            avg = sum(scores) / len(scores) if scores else 0
            target = TARGETS[phase_name]
            delta = target - avg
            total_delta += abs(delta)

            phase_data[phase_name] = {
                "messages": messages,
                "avg": avg,
                "target": target,
                "delta": delta,
            }

            status = "OK" if abs(delta) <= 1.0 else ("LOW" if delta > 0 else "HIGH")
            arrow = "^" if delta > 0.5 else ("v" if delta < -0.5 else "=")

            print(f"  {phase_name}:")
            print(f"    AVG intensity: {avg:.1f}/10  |  TARGET: {target:.1f}  |  DELTA: {delta:+.1f}  [{status}] {arrow}")

            # Print individual message scores
            for msg_id, text, score in messages:
                truncated = text[:70] + "..." if len(text) > 70 else text
                print(f"      {msg_id:8s} [{score:2d}/10] \"{truncated}\"")

        # Print Phase 4 messages for manual review
        if "Phase 4 (->PPV4)" in phase_data:
            print()
            print(f"  >>> PHASE 4 (CLIMAX) - FULL MESSAGES FOR MANUAL REVIEW:")
            for msg_id, text, score in phase_data["Phase 4 (->PPV4)"]["messages"]:
                print(f"      [{score:2d}/10] {msg_id}: \"{text}\"")

        results.append((model_name, total_delta, phase_data))
        print()

    # ============================================================
    # SUMMARY: WORST INTENSITY GAPS
    # ============================================================
    print()
    print("=" * 80)
    print("SUMMARY: MODELS RANKED BY TOTAL INTENSITY DELTA (worst first)")
    print("=" * 80)
    print()

    results.sort(key=lambda x: x[1], reverse=True)

    print(f"{'#':<4} {'MODEL':<20} {'TOTAL |DELTA|':<15} {'Ph1 Avg':<10} {'Ph2 Avg':<10} {'Ph3 Avg':<10} {'Ph4 Avg':<10}")
    print(f"{'':4s} {'':20s} {'':15s} {'(tgt 7.0)':<10} {'(tgt 8.5)':<10} {'(tgt 9.5)':<10} {'(tgt 9.8)':<10}")
    print("-" * 89)

    for rank, (model_name, total_delta, phase_data) in enumerate(results, 1):
        ph1 = phase_data.get("Phase 1 (->PPV1)", {}).get("avg", 0)
        ph2 = phase_data.get("Phase 2 (->PPV2)", {}).get("avg", 0)
        ph3 = phase_data.get("Phase 3 (->PPV3)", {}).get("avg", 0)
        ph4 = phase_data.get("Phase 4 (->PPV4)", {}).get("avg", 0)

        # Color coding via text markers
        def mark(avg, target):
            delta = target - avg
            if abs(delta) <= 1.0:
                return f"{avg:.1f}"
            elif delta > 0:
                return f"{avg:.1f} LOW!"
            else:
                return f"{avg:.1f} HIGH"

        print(f"{rank:<4} {model_name:<20} {total_delta:<15.1f} {mark(ph1, 7.0):<10} {mark(ph2, 8.5):<10} {mark(ph3, 9.5):<10} {mark(ph4, 9.8):<10}")

    # Phase-level analysis
    print()
    print("=" * 80)
    print("PHASE-LEVEL ANALYSIS: Which phases are systematically off?")
    print("=" * 80)
    print()

    for phase_name, target in TARGETS.items():
        avgs = []
        for _, _, phase_data in results:
            if phase_name in phase_data:
                avgs.append(phase_data[phase_name]["avg"])

        if avgs:
            overall_avg = sum(avgs) / len(avgs)
            overall_delta = target - overall_avg
            models_low = sum(1 for a in avgs if (target - a) > 1.0)
            models_ok = sum(1 for a in avgs if abs(target - a) <= 1.0)
            models_high = sum(1 for a in avgs if (a - target) > 1.0)

            print(f"  {phase_name}:")
            print(f"    Overall avg: {overall_avg:.1f}  |  Target: {target:.1f}  |  Gap: {overall_delta:+.1f}")
            print(f"    Models OK: {models_ok}  |  Too LOW: {models_low}  |  Too HIGH: {models_high}")
            print()


if __name__ == "__main__":
    run_audit()
