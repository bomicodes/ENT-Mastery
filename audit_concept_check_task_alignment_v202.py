"""v20.2 hard gate for exact-canonical Ludwig Angina decision depth and source provenance."""
import json
import re
import runtime_entry
from concept_check_board_repair_v177 import _find_module
from concept_check_depth_v202 import COHORT

QID = "cc-v112-rec-general-ent-emergencies-ludwig-angina"
TERM_GROUPS = {
    "space_anatomy": ("submandibular", "sublingual", "submental", "mylohyoid"),
    "clinical_airway": ("wooden", "tongue", "drooling", "airway"),
    "airway_before_imaging": ("supine CT", "must never delay", "threatened airway"),
    "awake_rescue": ("awake", "spontaneous ventilation", "invasive airway", "attempt limit"),
    "antimicrobial_source": ("oral streptococci", "anaerobic oral flora", "odontogenic source"),
    "drainage_boundary": ("Cummings 7e", "mandatory", "selected clinically stable patients", "drainable collection"),
    "deterioration": ("abscess", "sepsis", "progression", "failed medical therapy"),
    "complications": ("mediastinitis", "internal jugular", "carotid"),
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
    align = rr.get("task_alignment_v202") or {}
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
        if str(q.get("domain") or "") != "General ENT / Emergencies":
            fail("live_domain_changed:" + repr(q.get("domain")))
        prompt, ans = str(q.get("prompt") or ""), str(q.get("answer_text") or "")
        text = sem(ans)
        if not q.get("task_alignment_v202"):
            fail("missing_v202_marker")
        if len(words(prompt)) < 65 or "?" not in prompt:
            fail("weak_prompt:" + str(len(words(prompt))))
        if len(words(ans)) < 750:
            fail("weak_answer:" + str(len(words(ans))))
        if q.get("choices") or q.get("answer") is not None:
            fail("not_free_response")
        if not q.get("reviewed_all_domains_v178") or not q.get("review_basis_v178"):
            fail("lost_v178_review_metadata")
        if set(q.get("depth_layers_v202") or {}) != {"foundation", "application", "senior_decision"}:
            fail("missing_three_layer_depth")
        traps = q.get("common_traps_v202") or []
        if len(traps) < 7 or any(len(words(x)) < 25 for x in traps):
            fail("weak_individualized_trap_reasoning")
        refs = q.get("source_refs_v202") or []
        types = [x.get("type") for x in refs]
        if len(refs) < 6 or types.count("textbook") < 2 or "guideline" not in types or "systematic_review" not in types or "evidence" not in types or "review" not in types:
            fail("missing_traceable_source_mix")
        if not str(q.get("deliberate_review_v202") or "").strip():
            fail("missing_deliberate_review_metadata")
        for label, terms in TERM_GROUPS.items():
            if not all(sem(term) in text for term in terms):
                fail("missing_semantic_group:" + label)
        if "CT is an anatomic tool, not a prerequisite" not in ans:
            fail("missing_airway_imaging_boundary")
        if "Awake flexible intubation is a strategy, not a guarantee" not in ans:
            fail("missing_awake_failure_boundary")
        if "selected clinically stable patients without a discrete drainable collection" not in ans:
            fail("missing_selective_conservative_boundary")
        if "do not swing to the opposite error" not in ans:
            fail("missing_antibiotics_only_boundary")
        if "Steroids are sometimes used as an adjunct" not in ans or "not an airway plan" not in ans:
            fail("missing_steroid_boundary")
        rows.append({"id": qid, "concept_id": q.get("concept_id"), "resolved_topic": topic, "domain": q.get("domain"), "prompt_words": len(words(prompt)), "answer_words": len(words(ans)), "trap_count": len(traps), "source_count": len(refs), "failures": local})
    repaired = set(align.get("repaired") or [])
    if repaired != expected:
        failures.append("runtime_repaired_set_mismatch=" + ",".join(sorted(expected - repaired)) + "|extra=" + ",".join(sorted(repaired - expected)))
    with open("V202_TASK_ALIGNMENT_AUDIT.json", "w", encoding="utf-8") as f:
        json.dump({"expected_ids": sorted(expected), "runtime_alignment": align, "failures": failures, "items": rows}, f, indent=2, ensure_ascii=False)
    print(f"V202_EXPECTED|{len(expected)}")
    print(f"V202_REPAIRED|{len(repaired)}")
    print(f"V202_FAILURES|{len(failures)}")
    for r in rows:
        print("V202_DEPTH_ITEM|{id}|domain={domain}|prompt={prompt_words}|answer={answer_words}|traps={trap_count}|sources={source_count}|topic={resolved_topic}".format(**r))
    for x in failures:
        print("FAIL|" + x)
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
