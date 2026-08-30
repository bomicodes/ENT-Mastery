"""v19.9 hard gate for exact-canonical Epistaxis Surgical Control decision depth."""
import json
import re
import runtime_entry
from concept_check_board_repair_v177 import _find_module
from concept_check_depth_v199 import COHORT

QID = "cc-v112-rec-rhinology-allergy-skull-base-epistaxis-surgical-control"
TERM_GROUPS = {
    "stabilization": ("airway, breathing, circulation", "resuscitation"),
    "visible_source_boundary": ("discrete bleeding point", "cauterizing blindly"),
    "posterior_failure": ("posterior or otherwise refractory source", "packing is a temporizing hemostatic tool"),
    "antithrombotic_boundary": ("not experiencing life-threatening bleeding", "before reflexively transfusing", "withdrawing antithrombotic therapy"),
    "definitive_escalation": ("not controlled by appropriate packing or nasal cauterization", "surgical arterial control", "endovascular embolization"),
    "spa_control": ("sphenopalatine artery control", "relevant branches"),
    "parallel_pathways": ("parallel definitive pathways", "not a mandatory sequence"),
    "airway_rescue": ("protect the airway", "never let pursuit of the bleeding point delay oxygenation and circulation"),
}


def words(v):
    return re.findall(r"\b\w+[\w'-]*\b", str(v or ""))


def sem(v):
    s = str(v or "").lower()
    s = re.sub(r"[-–—/]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def main():
    d = runtime_entry.data
    checks = list(d.CONCEPT_CHECKS_V112)
    by = {str(q.get("id") or ""): q for q in checks}
    failures, rows = [], []
    expected = set(COHORT)
    rr = getattr(runtime_entry, "CONCEPT_CHECK_FINAL_CLINICAL_GATE_V179", {})
    align = rr.get("task_alignment_v199") or {}
    if align.get("missing"):
        failures.append("runtime_missing=" + ",".join(align["missing"]))
    if align.get("link_mismatch"):
        failures.append("runtime_link_mismatch=" + ",".join(align["link_mismatch"]))

    for qid in sorted(expected):
        q = by.get(qid)
        if not q:
            failures.append(qid + ":missing")
            continue
        local = []

        def fail(x):
            failures.append(qid + ":" + x)
            local.append(x)

        p = COHORT[qid]
        m = _find_module(q, d.DEEP_MODULES_V6, d._v6_item_id)
        topic = str(m.get("topic") or "") if m else ""
        cid = d._v6_item_id(q.get("domain"), topic) if m and q.get("domain") else None
        if not m:
            fail("no_live_canonical_module")
        if topic != p["canonical_topic"]:
            fail("resolved_topic_mismatch:" + repr(topic))
        if cid != p["concept_id"] or q.get("concept_id") != cid:
            fail("concept_id_changed_or_unresolved")
        prompt = str(q.get("prompt") or "")
        ans = str(q.get("answer_text") or "")
        text = sem(ans)
        if not q.get("task_alignment_v199"):
            fail("missing_v199_marker")
        if len(words(prompt)) < 65 or "?" not in prompt:
            fail("weak_prompt:" + str(len(words(prompt))))
        if len(words(ans)) < 550:
            fail("weak_answer:" + str(len(words(ans))))
        if q.get("choices") or q.get("answer") is not None:
            fail("not_free_response")
        if not q.get("reviewed_all_domains_v178") or not q.get("review_basis_v178"):
            fail("lost_v178_review_metadata")
        if set(q.get("depth_layers_v199") or {}) != {"foundation", "application", "senior_decision"}:
            fail("missing_three_layer_depth")
        traps = q.get("common_traps_v199") or []
        if len(traps) < 6 or any(len(words(x)) < 25 for x in traps):
            fail("weak_individualized_trap_reasoning")
        if not str(q.get("deliberate_review_v199") or "").strip():
            fail("missing_deliberate_review_metadata")
        for label, terms in TERM_GROUPS.items():
            if not all(sem(term) in text for term in terms):
                fail("missing_semantic_group:" + label)
        if "blood seen anteriorly does not establish that the source is anterior" not in text:
            fail("missing_source_localization_trap")
        if "posterior packing can compromise the airway" not in text:
            fail("missing_posterior_pack_airway_boundary")
        if "repeated bedside repacking without a stop rule" not in text:
            fail("missing_repacking_stop_rule")
        if "life-threatening" not in text or "thromboembolic indication" not in text:
            fail("missing_antithrombotic_risk_balance")
        if "neurologic or ophthalmic ischemic complications" not in text:
            fail("missing_embolization_harm_boundary")
        rows.append({
            "id": qid,
            "concept_id": q.get("concept_id"),
            "resolved_topic": topic,
            "prompt_words": len(words(prompt)),
            "answer_words": len(words(ans)),
            "trap_count": len(traps),
            "failures": local,
        })

    repaired = set(align.get("repaired") or [])
    if repaired != expected:
        failures.append(
            "runtime_repaired_set_mismatch=" + ",".join(sorted(expected - repaired))
            + "|extra=" + ",".join(sorted(repaired - expected))
        )
    with open("V199_TASK_ALIGNMENT_AUDIT.json", "w", encoding="utf-8") as f:
        json.dump({"expected_ids": sorted(expected), "runtime_alignment": align, "failures": failures, "items": rows}, f, indent=2, ensure_ascii=False)
    print(f"V199_EXPECTED|{len(expected)}")
    print(f"V199_REPAIRED|{len(repaired)}")
    print(f"V199_FAILURES|{len(failures)}")
    for r in rows:
        print("V199_DEPTH_ITEM|{id}|prompt={prompt_words}|answer={answer_words}|traps={trap_count}|topic={resolved_topic}".format(**r))
    for x in failures:
        print("FAIL|" + x)
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
