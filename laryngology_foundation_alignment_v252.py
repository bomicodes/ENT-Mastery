"""v25.2 — canonical/quality repair for reused v12.8 Laryngology foundations.

The live registry uses newer canonical names for two legacy display topics. Once
those older cases are deliberately reviewed, the strict runtime contract rightly
requires their displayed topic and concept link to agree with the canonical node.
This repair also strengthens one terse legacy sulcus distractor rationale.
"""

REPAIRS = {
    "v128_lar_09": "Vocal Fold Sulcus / Scar",
    "v128_lar_10": "Inducible Laryngeal Obstruction / PVFM",
}


def apply_laryngology_foundation_alignment_v252(challenges, item_id_fn):
    by_id = {q.get("id"): q for q in challenges if q.get("id")}
    changed = []
    for qid, canonical_topic in REPAIRS.items():
        q = by_id.get(qid)
        if not q:
            raise RuntimeError(f"v25.2 alignment missing foundation {qid}")
        q["topic"] = canonical_topic
        q["canonical_topic"] = canonical_topic
        q["concept_id"] = item_id_fn("Laryngology / Voice / Swallowing", canonical_topic)
        changed.append(qid)

    sulcus = by_id["v128_lar_09"]
    reasons = list(sulcus.get("why_wrong") or [])
    if len(reasons) != len(sulcus.get("choices") or []):
        raise RuntimeError("v25.2 sulcus foundation rationale/choice mismatch")
    if len(reasons) > 2:
        reasons[2] = "BPPV is a peripheral vestibular disorder causing brief positional vertigo; it does not explain focal vocal-fold stiffness or loss of mucosal wave."
    sulcus["why_wrong"] = reasons
    return changed
