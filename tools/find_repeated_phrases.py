"""
Find Repeated Phrases Across Model Journeys
Analyzes all model configs to find exact and near-duplicate journey messages.
"""

import importlib.util
import os
import sys
import re
from collections import defaultdict
from itertools import combinations

# â”€â”€ Setup â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
MODELS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")
SKIP_FILES = {"__init__.py", "test_write.py"}
MIN_MODELS = 3  # Only show phrases in 3+ models
SIMILARITY_THRESHOLD = 0.80

# Add tools/ to path so model_factory can be imported
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def load_all_models():
    """Load all model configs and return {model_name: [(msg_id, text), ...]}"""
    models = {}
    for fname in sorted(os.listdir(MODELS_DIR)):
        if not fname.endswith(".py") or fname in SKIP_FILES:
            continue
        fpath = os.path.join(MODELS_DIR, fname)
        mod_name = fname[:-3]
        try:
            spec = importlib.util.spec_from_file_location(mod_name, fpath)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            config = mod.config
            journey = config.get("journey", [])
            name = config.get("name", mod_name)
            messages = []
            for entry in journey:
                msg_id = entry[0]
                text = entry[1]
                messages.append((msg_id, text))
            models[name] = messages
            print(f"  Loaded {name}: {len(messages)} messages")
        except Exception as e:
            print(f"  ERROR loading {fname}: {e}")
    return models


def normalize_text(text):
    """Normalize text for comparison: lowercase, strip emojis, collapse whitespace."""
    t = text.lower().strip()
    # Remove emojis (Unicode ranges for common emoji blocks)
    t = re.sub(
        r'[\U0001F300-\U0001FAFF\U00002702-\U000027B0\U0000FE00-\U0000FE0F\U0000200D]+',
        '', t
    )
    # Collapse whitespace
    t = re.sub(r'\s+', ' ', t).strip()
    return t


def get_words(text):
    """Extract word set from normalized text."""
    normalized = normalize_text(text)
    # Split on non-alphanumeric, keep words 2+ chars
    words = re.findall(r'[a-z]{2,}', normalized)
    return words


def word_similarity(text1, text2):
    """Calculate word-level Jaccard-like similarity between two texts."""
    words1 = get_words(text1)
    words2 = get_words(text2)
    if not words1 or not words2:
        return 0.0
    # Use multiset (bag) intersection over union for better accuracy
    from collections import Counter
    c1, c2 = Counter(words1), Counter(words2)
    intersection = sum((c1 & c2).values())
    union = sum((c1 | c2).values())
    if union == 0:
        return 0.0
    return intersection / union


def find_exact_duplicates(models):
    """Find texts that appear exactly (normalized) in 3+ models."""
    # Map normalized_text -> [(model_name, msg_id, original_text)]
    text_map = defaultdict(list)
    for model_name, messages in models.items():
        for msg_id, text in messages:
            norm = normalize_text(text)
            text_map[norm].append((model_name, msg_id, text))

    # Filter to 3+ models (not just 3+ occurrences - must be distinct models)
    duplicates = {}
    for norm, entries in text_map.items():
        unique_models = set(e[0] for e in entries)
        if len(unique_models) >= MIN_MODELS:
            duplicates[norm] = entries

    # Sort by number of unique models (desc)
    sorted_dups = sorted(
        duplicates.items(),
        key=lambda x: len(set(e[0] for e in x[1])),
        reverse=True
    )
    return sorted_dups


def find_near_duplicates(models, exact_norms):
    """Find clusters of texts with 80%+ word similarity across 3+ models."""
    # Collect all unique (model, msg_id, text, norm) combos
    all_msgs = []
    for model_name, messages in models.items():
        for msg_id, text in messages:
            norm = normalize_text(text)
            all_msgs.append((model_name, msg_id, text, norm))

    # Skip messages that are already exact duplicates
    non_exact = [m for m in all_msgs if m[3] not in exact_norms]

    # Also include exact dupes as potential cluster seeds but we'll report separately
    # For near-dupes, compare all messages including exact ones
    # But we skip pairs that are exact matches

    # Build clusters using greedy approach
    # For efficiency, group by msg_id prefix (same position = more likely similar)
    clusters = []
    used = set()

    for i in range(len(all_msgs)):
        if i in used:
            continue
        cluster = [i]
        for j in range(i + 1, len(all_msgs)):
            if j in used:
                continue
            # Skip if both are exact same normalized text (already covered above)
            if all_msgs[i][3] == all_msgs[j][3]:
                continue
            sim = word_similarity(all_msgs[i][2], all_msgs[j][2])
            if sim >= SIMILARITY_THRESHOLD:
                cluster.append(j)

        if len(cluster) > 1:
            # Check unique models
            models_in_cluster = set(all_msgs[idx][0] for idx in cluster)
            if len(models_in_cluster) >= MIN_MODELS:
                clusters.append(cluster)
                for idx in cluster:
                    used.add(idx)

    # Sort clusters by size (desc)
    clusters.sort(key=lambda c: len(set(all_msgs[idx][0] for idx in c)), reverse=True)

    # Convert to readable format
    result = []
    for cluster in clusters:
        entries = [(all_msgs[idx][0], all_msgs[idx][1], all_msgs[idx][2]) for idx in cluster]
        # Use first entry as "base phrase"
        base = entries[0][2]
        unique_models = len(set(e[0] for e in entries))
        result.append((base, unique_models, entries))

    return result


def main():
    print("=" * 70)
    print("REPEATED JOURNEY PHRASES ACROSS MODELS")
    print("=" * 70)
    print(f"\nLoading models from: {MODELS_DIR}\n")

    models = load_all_models()
    print(f"\nTotal models loaded: {len(models)}")
    total_msgs = sum(len(msgs) for msgs in models.values())
    print(f"Total journey messages: {total_msgs}\n")

    # â”€â”€ EXACT DUPLICATES â”€â”€
    print("=" * 70)
    print("=== EXACT DUPLICATES ===")
    print("(Same text after removing emojis + normalizing case/whitespace)")
    print("=" * 70)

    exact_dups = find_exact_duplicates(models)
    exact_norms = set(norm for norm, _ in exact_dups)

    if not exact_dups:
        print("\nNo exact duplicates found across 3+ models.\n")
    else:
        print(f"\nFound {len(exact_dups)} phrases repeated across 3+ models:\n")
        for norm, entries in exact_dups:
            unique_models = sorted(set(e[0] for e in entries))
            # Show original text from first entry
            sample_text = entries[0][2]
            print(f'"{sample_text}" (appears in {len(unique_models)} models)')
            for model_name, msg_id, orig_text in sorted(entries, key=lambda x: x[0]):
                print(f"  - {model_name}: {msg_id}")
            print()

    # â”€â”€ NEAR DUPLICATES â”€â”€
    print("=" * 70)
    print("=== NEAR DUPLICATES (80%+ similar) ===")
    print("(Texts that share 80%+ words, allowing for pet name/emoji swaps)")
    print("=" * 70)

    near_dups = find_near_duplicates(models, exact_norms)

    if not near_dups:
        print("\nNo near-duplicate clusters found across 3+ models.\n")
    else:
        print(f"\nFound {len(near_dups)} clusters of near-duplicates:\n")
        for base, unique_count, entries in near_dups:
            # Truncate base for header
            base_short = base[:80] + "..." if len(base) > 80 else base
            print(f'Cluster: "{base_short}" (~{unique_count} models)')
            for model_name, msg_id, text in sorted(entries, key=lambda x: x[0]):
                text_short = text[:90] + "..." if len(text) > 90 else text
                print(f'  - {model_name} {msg_id}: "{text_short}"')
            print()

    # â”€â”€ SUMMARY â”€â”€
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Models analyzed: {len(models)}")
    print(f"Total messages: {total_msgs}")
    print(f"Exact duplicate phrases (3+ models): {len(exact_dups)}")
    print(f"Near-duplicate clusters (3+ models): {len(near_dups)}")


if __name__ == "__main__":
    main()
