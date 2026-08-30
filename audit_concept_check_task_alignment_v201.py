"""v20.1 hard gate for exact-canonical RRP decision depth and source provenance."""
import json
import re
import runtime_entry
from concept_check_board_repair_v177 import _find_module
from concept_check_depth_v201 import COHORT

QID = "cc-v112-rec-laryngology-voice-swallowing-recurrent-respiratory-papillomatosis"
TERM_GROUPS = {
    "biology_goal": ("HPV 6 and 11", "safe airway and useful voice", "least iatrogenic injury"),
    "mucosal_preservation": ("anterior commissure", "bilateral opposing raw surfaces", "web"),
    "airway_boundary": ("tracheostomy is not routine", "distal tracheobronchial spread", "lifesaving airway"),
    "adult_papzimeos": ("August 14, 2025", "PAPZIMEOS", "adults with RRP"),
    "trial_label_boundary": ("three surgeries per year", "false label restriction", "FDA indication is adults with RRP"),
    "adult_guidance": ("2026 RRP Foundation adult position statement", "discussed early", "position statement"),
    "bevacizumab": ("systemic bevacizumab", "second-line medical therapy", "2024 consensus"),
    "pediatric_boundary": ("adult FDA indication", "do not silently extrapolate", "child"),
    "pulmonary": ("HPV typing", "chest CT", "biopsy", "pulmonary"),
    "fire_rescue": ("airway fire", "stop ventilation and oxidizer flow", "remove the burning"),
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
    align = rr.get("task_alignment_v201") or {}
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

        prompt, ans = str(q.get("prompt") or ""), str(q.get("answer_text") or "")
        text = sem(ans)
        if not q.get("task_alignment_v201"):
            fail("missing_v201_marker")
        if len(words(prompt)) < 60 or "?" not in prompt:
            fail("weak_prompt:" + str(len(words(prompt))))
        if len(words(ans)) < 650:
            fail("weak_answer:" + str(len(words(ans))))
        if q.get("choices") or q.get("answer") is not None:
            fail("not_free_response")
        if not q.get("reviewed_all_domains_v178") or not q.get("review_basis_v178"):
            fail("lost_v178_review_metadata")
        if set(q.get("depth_layers_v201") or {}) != {"foundation", "application", "senior_decision"}:
            fail("missing_three_layer_depth")

        traps = q.get("common_traps_v201") or []
        if len(traps) < 7 or any(len(words(x)) < 25 for x in traps):
            fail("weak_individualized_trap_reasoning")
        refs = q.get("source_refs_v201") or []
        types = [x.get("type") for x in refs]
        if len(refs) < 8 or types.count("textbook") < 3 or "regulatory" not in types or "position_statement" not in types or "consensus" not in types:
            fail("missing_traceable_source_mix")
        if not str(q.get("deliberate_review_v201") or "").strip():
            fail("missing_deliberate_review_metadata")

        for label, terms in TERM_GROUPS.items():
            if not all(sem(term) in text for term in terms):
                fail("missing_semantic_group:" + label)

        if "trial population, not the wording of the adult indication" not in ans:
            fail("missing_trial_vs_label_boundary")
        if "PAPZIMEOS currently has an adult FDA indication" not in ans:
            fail("missing_pediatric_regulatory_boundary")
        if "medical therapy never substitutes for immediate airway rescue" not in ans:
            fail("missing_medical_vs_airway_rescue_boundary")
        if "influential contemporary guidance, not a substitute" not in ans:
            fail("missing_position_statement_evidence_boundary")

        rows.append({
            "id": qid,
            "concept_id": q.get("concept_id"),
            "resolved_topic": topic,
            "prompt_words": len(words(prompt)),
            "answer_words": len(words(ans)),
            "trap_count": len(traps),
            "source_count": len(refs),
            "failures": local,
        })

    repaired = set(align.get("repaired") or [])
    if repaired != expected:
        failures.append("runtime_repaired_set_mismatch=" + ",".join(sorted(expected - repaired)) + "|extra=" + ",".join(sorted(repaired - expected)))

    with open("V201_TASK_ALIGNMENT_AUDIT.json", "w", encoding="utf-8") as f:
        json.dump({"expected_ids": sorted(expected), "runtime_alignment": align, "failures": failures, "items": rows}, f, indent=2, ensure_ascii=False)
    print(f"V201_EXPECTED|{len(expected)}")
    print(f"V201_REPAIRED|{len(repaired)}")
    print(f"V201_FAILURES|{len(failures)}")
    for r in rows:
        print("V201_DEPTH_ITEM|{id}|prompt={prompt_words}|answer={answer_words}|traps={trap_count}|sources={source_count}|topic={resolved_topic}".format(**r))
    for x in failures:
        print("FAIL|" + x)
    if failures:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
