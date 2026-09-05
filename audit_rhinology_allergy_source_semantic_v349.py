#!/usr/bin/env python3
"""v34.9 — fail closed on live Allergic Rhinitis/LAR source and decision semantics.

This gate complements the existing vignette-level v29.7 distinction audit. It protects
exact live Deep Curriculum concepts so textbook provenance, current AAO-HNSF guidance,
and clinically consequential allergy-testing/immunotherapy distinctions cannot silently
fall out of the Render assembly while the topic names still exist.

Important: Render launches runtime_entry_pasha:app. Audit that same final production
boundary directly rather than relying on another audit/import to have applied the
post-v28.4 cumulative curriculum chain first. This keeps standalone and global release
results deterministic and prevents import-order state from producing a false green.
"""

import sys
import runtime_entry_pasha as production

DOMAIN = "Rhinology / Allergy / Skull Base"
TOPICS = ("Allergic Rhinitis", "Local Allergic Rhinitis")
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def fail(message):
    print(f"FAIL: {message}")
    return 1


def module_text(row):
    return " ".join(str(row.get(field) or "") for field in FIELDS).lower()


def source_text(row):
    return " ".join(str(x) for x in (row.get("source_basis") or [])).lower()


def require_any(text, groups, label):
    """Return a readable failure when none of a semantic synonym group is present."""
    for group in groups:
        if all(token in text for token in group):
            return None
    return label


def main():
    data = production.runtime_entry.data
    rows = (getattr(data, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, []) or []
    by_topic = {str(row.get("topic") or ""): row for row in rows}
    failures = 0

    # Use the live canonical inventory, not aliases or a parallel hand-maintained slug list.
    expected_ids = {topic: data._v6_item_id(DOMAIN, topic) for topic in TOPICS}
    if len(rows) != 42:
        failures += fail(f"Rhinology canonical inventory changed: {len(rows)} != 42")

    for topic in TOPICS:
        row = by_topic.get(topic)
        if row is None:
            failures += fail(f"missing exact live canonical topic {topic!r}")
            continue

        cid = data._v6_item_id(DOMAIN, row.get("topic"))
        if cid != expected_ids[topic]:
            failures += fail(f"{topic}: canonical ID drift {cid!r} != {expected_ids[topic]!r}")

        text = module_text(row)
        sources = source_text(row)

        # The connected core-textbook trail must survive final production assembly.
        for token in ("cummings", "k.j. lee", "pasha"):
            if token not in sources:
                failures += fail(f"{topic}: missing connected textbook provenance {token!r}")

        if topic == "Allergic Rhinitis":
            if "allergic rhinitis" not in sources or "2015" not in sources:
                failures += fail("Allergic Rhinitis: missing AAO-HNSF allergic-rhinitis guideline provenance")
            if "immunotherapy for inhalant allergy" not in sources or "2024" not in sources:
                failures += fail("Allergic Rhinitis: missing 2024 AAO-HNSF inhalant-immunotherapy guidance")

            requirements = [
                require_any(text, [("skin-prick", "serum", "specific ige"), ("skin", "serum", "specific ige")], "selective skin/serum specific-IgE testing"),
                require_any(text, [("sensitization", "symptom"), ("sensitization", "exposure")], "sensitization must be clinically relevant"),
                require_any(text, [("food panel",), ("broad food",)], "reject indiscriminate food-panel testing"),
                require_any(text, [("intranasal corticosteroid",), ("intranasal steroid",)], "intranasal corticosteroid first-line framework"),
                require_any(text, [("structural", "surgery"), ("structural", "operative")], "surgery reserved for a separate structural problem"),
                require_any(text, [("immunotherapy", "clinically relevant sensitization"), ("immunotherapy", "relevant sensitization")], "immunotherapy tied to clinically relevant sensitization"),
            ]
            for missing in filter(None, requirements):
                failures += fail(f"Allergic Rhinitis: missing semantic requirement — {missing}")

        else:
            if "local allergic rhinitis" not in sources:
                failures += fail("Local Allergic Rhinitis: missing disease-specific LAR provenance")
            if "immunotherapy for inhalant allergy" not in sources or "2024" not in sources:
                failures += fail("Local Allergic Rhinitis: missing current inhalant-immunotherapy guidance trail")

            requirements = [
                require_any(text, [("negative", "skin", "serum"), ("negative", "systemic testing")], "negative conventional systemic testing phenotype"),
                require_any(text, [("nasal allergen provocation",), ("nasal allergen challenge",)], "nasal allergen provocation/challenge confirmation"),
                require_any(text, [("nares", "nonallergic rhinopathy"), ("nares", "nonallergic")], "LAR versus NARES/nonallergic-rhinopathy discrimination"),
                require_any(text, [("nasal", "specific ige", "not standardized"), ("nasal", "specific ige", "standardized")], "limitations of nasal specific-IgE testing"),
                require_any(text, [("immunotherapy", "specialist"), ("immunotherapy", "carefully confirmed")], "specialist-selected immunotherapy rather than symptom-only escalation"),
            ]
            for missing in filter(None, requirements):
                failures += fail(f"Local Allergic Rhinitis: missing semantic requirement — {missing}")

    if failures:
        print(f"\nRhinology allergy source-semantic gate FAILED with {failures} issue(s).")
        return 1

    print("RHINOLOGY_ALLERGY_PRODUCTION_ENTRYPOINT|runtime_entry_pasha:app")
    print("RHINOLOGY_ALLERGY_CANONICAL_IDS|" + "|".join(f"{topic}={expected_ids[topic]}" for topic in TOPICS))
    print("PASS: exact final-production AR/LAR concepts retain core-textbook provenance, current guideline trails, selective testing, phenotype discrimination, and appropriate immunotherapy/surgical decision boundaries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
