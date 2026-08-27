"""v24.0 — final TPS canonical alignment and runtime-quality repair.

Retargets three v23.8/v23.9 display-topic paraphrases to the exact live
canonical module names and strengthens the completion-thyroidectomy foundation
stem caught by the runtime ladder quality gate. No new questions are created.
"""
DOMAIN = "Thyroid / Parathyroid / Salivary"

TOPIC_REMAP = {
    "v238_tps_rai_": "Radioactive Iodine and TSH Suppression in DTC",
    "v239_tps_famhpt_": "Familial Hyperparathyroidism and Parathyromatosis",
    "v239_tps_acc_": "Salivary Adenoid Cystic Carcinoma and Perineural Spread",
}

COMPLETION_STEM = (
    "A patient previously underwent thyroid lobectomy and final pathology now "
    "raises the question of removing the remaining lobe. What does the term "
    "completion thyroidectomy mean?"
)


def apply_tps_final_alignment_v240(challenges, item_id_fn):
    remapped = 0
    stem_repaired = False
    for q in challenges:
        qid = str(q.get("id") or "")
        for prefix, topic in TOPIC_REMAP.items():
            if qid.startswith(prefix):
                cid = item_id_fn(DOMAIN, topic)
                if not cid:
                    raise RuntimeError("v240 canonical TPS target missing: " + topic)
                q["domain"] = DOMAIN
                q["topic"] = topic
                q["concept_id"] = cid
                remapped += 1
                break
        if qid == "v238_tps_completion_fnd":
            q["stem"] = COMPLETION_STEM
            stem_repaired = True
    return {"remapped": remapped, "stem_repaired": stem_repaired}
