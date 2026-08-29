"""v28.8 — semantic hard gate for the live Head & Neck salvage ladder.

The canonical inventory has one salvage concept: "Salvage Surgery After Radiation / Chemoradiation".
This gate protects two clinically distinct jobs inside that one card:
1) broad salvage candidacy, irradiated-field planning/reconstruction, and complication risk;
2) post-definitive-CRT response-directed neck management, including PET timing and avoidance of
   routine planned neck dissection after complete response.

The ordinary ladder-completeness gate validates links/stages/schema. This gate ensures the actual
question set teaches both jobs rather than satisfying coverage with generic salvage questions.
"""

import re
import runtime_entry

DOMAIN = "Head & Neck Oncology"
TOPIC = "Salvage Surgery After Radiation / Chemoradiation"
POST_CRT_QID = "v225_hn_salv_postcrt_app"


def norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def case_text(q):
    parts = [q.get("stem"), q.get("explanation"), q.get("board_pearl"), q.get("curveball"),
             " ".join(q.get("choices") or []), " ".join(q.get("why_wrong") or [])]
    return norm(" ".join(str(x or "") for x in parts))


def has_any(text, terms):
    return any(norm(term) in text for term in terms)


def require_groups(label, text, groups, failures):
    for group, terms in groups:
        if not has_any(text, terms):
            failures.append(f"{label}:missing_semantic_group:{group}")


def main():
    data = runtime_entry.data
    failures = []
    modules = [m for m in data.DEEP_MODULES_V6.get(DOMAIN, []) if m.get("topic")]
    module = next((m for m in modules if norm(m.get("topic")) == norm(TOPIC)), None)
    if module is None:
        failures.append("missing_live_salvage_canonical")
        linked = []
    else:
        actual_topic = str(module.get("topic"))
        cid = data._v6_item_id(DOMAIN, actual_topic)
        linked = [q for q in data.CLINICAL_CHALLENGES_V119
                  if q.get("domain") == DOMAIN and q.get("concept_id") == cid and q.get("ladder_reviewed")]
        stages = {q.get("learning_stage") for q in linked}
        missing = {"foundation", "application", "senior_decision"} - stages
        if missing:
            failures.append("missing_stages:" + ",".join(sorted(missing)))
        if not module.get("post_crt_response_sublayer_v287"):
            failures.append("concept_hub_missing_post_crt_response_sublayer_v287")

    for q in linked:
        print("HN_SALVAGE_CASE|{}|{}|{}".format(q.get("learning_stage"), q.get("id"), norm(q.get("stem"))))

    text = " ".join(case_text(q) for q in linked)
    require_groups("broad_salvage", text, (
        ("irradiated_field", ("irradiated", "prior radiation", "chemoradiation")),
        ("candidacy", ("resectable", "oncologic benefit", "distant metastases", "functional outcome")),
        ("reconstruction_or_wound_risk", ("reconstruction", "vascularized", "fistula", "wound")),
    ), failures)
    require_groups("post_crt_management", text, (
        ("response_assessment", ("metabolic response", "pet ct", "pet")),
        ("timing", ("12 weeks", "12 week", "approximately 12")),
        ("avoid_planned_neck_dissection", ("planned neck dissection", "surveillance", "complete response")),
        ("equivocal_or_persistent_workup", ("equivocal", "persistent", "progressive", "biopsy", "re imaging")),
        ("selected_salvage", ("salvage", "resectable")),
    ), failures)

    post_case = next((q for q in linked if q.get("id") == POST_CRT_QID), None)
    if not post_case:
        failures.append("missing_post_crt_management_case")
    else:
        if post_case.get("learning_stage") != "application":
            failures.append("post_crt_case_wrong_stage")
        if not post_case.get("management_layer_v288"):
            failures.append("post_crt_case_missing_review_marker")
        reasons = list(post_case.get("why_wrong") or [])
        choices = list(post_case.get("choices") or [])
        if len(reasons) != len(choices):
            failures.append("post_crt_case_rationale_alignment_error")

    print(f"HN_SALVAGE_REVIEWED|{len(linked)}")
    print(f"HN_SALVAGE_POST_CRT_CASE|{int(post_case is not None)}")
    print(f"HN_SALVAGE_SEMANTIC_FAILURES|{len(failures)}")
    for failure in failures:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)
    print("PASS: live salvage ladder preserves broad irradiated-field reasoning and adds a distinct post-CRT response-management layer")


if __name__ == "__main__":
    main()
