"""v19.1 OR Tomorrow concept-link normalization.

Keeps operation titles procedure-specific while ensuring the OR -> Concept button
uses canonical curriculum topic names instead of legacy disease slugs.
"""


def apply_or_concept_link_fix_v191(registry):
    fixed = []
    for slug, op in (registry or {}).items():
        title = str(op.get("title") or "")
        linked = str(op.get("linked_topic") or "").strip()
        key = linked.lower().replace("_", "-").replace(" ", "-")

        # Parathyroidectomy historically pointed to the legacy
        # "parathyroid-disease" search slug. The canonical concept is Parathyroid.
        if "parathyroidectomy" in title.lower() or "parathyroid" in str(slug).lower():
            if key in {"parathyroid-disease", "parathyroid"} or not linked:
                if linked != "Parathyroid":
                    fixed.append({"slug": slug, "from": linked, "to": "Parathyroid"})
                op["linked_topic"] = "Parathyroid"

    return {"fixed": fixed, "count": len(fixed)}
