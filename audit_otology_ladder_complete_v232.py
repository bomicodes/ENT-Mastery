"""v23.2 — full-domain Otology / Neurotology learning-ladder hard gate."""
from collections import Counter, defaultdict
import runtime_entry as rt

DOMAIN = "Otology / Neurotology"
STAGES = {"foundation", "application", "senior_decision"}
EXPECTED_CANONICAL = 47


def main():
    data = rt.data
    modules = [m for m in data.DEEP_MODULES_V6.get(DOMAIN, []) if m.get("topic")]
    cases = list(data.CLINICAL_CHALLENGES_V119)
    ids = [q.get("id") for q in cases if q.get("id")]
    dupes = [qid for qid, n in Counter(ids).items() if n > 1]
    by_cid = defaultdict(list)
    for q in cases:
        if q.get("concept_id"):
            by_cid[q["concept_id"]].append(q)

    failures=[]; complete=0
    if len(modules) != EXPECTED_CANONICAL:
        failures.append(f"canonical count {len(modules)} != {EXPECTED_CANONICAL}")
    if dupes:
        failures.append("duplicate vignette IDs: " + ",".join(sorted(dupes)))

    for module in modules:
        topic=module["topic"]; cid=data._v6_item_id(DOMAIN,topic); linked=by_cid.get(cid,[])
        stage_counts=Counter(q.get("learning_stage") for q in linked if q.get("learning_stage") in STAGES)
        missing=sorted(STAGES-set(stage_counts)); reviewed=any(q.get("ladder_reviewed") for q in linked)
        print(f"OTOLOGY_COMPLETE_LADDER|{topic}|cases={len(linked)}|foundation={stage_counts['foundation']},application={stage_counts['application']},senior_decision={stage_counts['senior_decision']}|reviewed={int(reviewed)}")
        if missing: failures.append(f"{topic}: missing {','.join(missing)}")
        elif not reviewed: failures.append(f"{topic}: complete stages but no deliberate-review metadata")
        else: complete+=1

    print(f"OTOLOGY_CANONICAL_TOPICS|{len(modules)}"); print(f"OTOLOGY_COMPLETE_TOPICS|{complete}"); print(f"OTOLOGY_COMPLETE_LADDER_GAPS|{len(failures)}")
    if failures:
        for failure in failures: print("OTOLOGY_COMPLETE_LADDER_FAILURE|"+failure)
        raise SystemExit(1)
    print("PASS: all 47 canonical Otology / Neurotology topics have deliberate foundation, application, and senior-decision coverage")

if __name__=="__main__": main()
