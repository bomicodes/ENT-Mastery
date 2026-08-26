"""v19.2 OR Tomorrow concept-link normalization.

Keeps operation titles procedure-specific while ensuring the OR -> Concept button
uses canonical curriculum topic names instead of legacy disease/reoperative slugs.
"""


def apply_or_concept_link_fix_v191(registry):
    fixed = []
    for slug, op in (registry or {}).items():
        title = str(op.get("title") or "")
        linked = str(op.get("linked_topic") or "").strip()

        # Every parathyroid operation belongs to the canonical Parathyroid
        # curriculum concept, including focused, bilateral and reoperative cases.
        if "parathyroid" in title.lower() or "parathyroid" in str(slug).lower():
            if linked != "Parathyroid":
                fixed.append({"slug": slug, "from": linked, "to": "Parathyroid"})
            op["linked_topic"] = "Parathyroid"

    return {"fixed": fixed, "count": len(fixed)}
