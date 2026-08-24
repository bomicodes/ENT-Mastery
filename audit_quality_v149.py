"""ENT Mastery v14.9 resident-level vignette quality audit.

This audit intentionally goes beyond canonical coverage. It asks whether the
linked cases look like useful board/chief-level teaching material rather than
merely satisfying schema fields.

Default mode is informational and exits 0 so quality debt can be surfaced
without generating recurring CI failure emails. Use --strict-quality once the
reported material gaps have been reviewed and closed.
"""

import argparse
import difflib
import re
from collections import Counter, defaultdict

import recognize_stage_v127  # noqa: F401 - applies runtime merges
import data


_GENERIC_WHY_WRONG = (
    "use the mechanism, anatomy, and management priority in the explanation",
    "compare this option with the time-critical management principle in the explanation",
    "compare this option with the management principle and anatomy in the explanation",
    "this option misses the key clinical discriminator described in the explanation",
    "this option does not address the key discriminator in the scenario",
    "this option misses the key discriminator in the scenario",
    "this option misses the key clinical discriminator",
    "does not best address the management discriminator in this scenario",
)

_EMERGENCY_TERMS = {
    "airway", "stridor", "hemorrhage", "bleeding", "hematoma", "epistaxis",
    "foreign body", "button battery", "abscess", "deep neck", "meningitis",
    "mastoiditis", "invasive fungal", "orbital complication", "vision",
    "csf leak", "aspiration", "angioedema", "anaphylaxis", "trauma",
    "fracture", "septic", "lemierre", "necrotizing", "sudden sensorineural",
    "flap compromise", "carotid blowout", "thyroid storm", "hypocalcemia",
}

_OPERATIVE_TERMS = {
    "surgery", "surgical", "operate", "operation", "resection", "excision",
    "dissection", "mastoid", "tympanoplasty", "staped", "cochlear implant",
    "sinus surgery", "fess", "septoplasty", "rhinoplasty", "laryngoscopy",
    "bronchoscopy", "tracheostomy", "laryngectomy", "thyroidectomy",
    "parathyroidectomy", "parotidectomy", "neck dissection", "flap",
    "reconstruction", "orif", "fixation", "tonsillectomy", "adenoidectomy",
    "palatoplasty", "implant", "ablation", "sling", "graft", "ligation",
}

_POSTOP_TERMS = {
    "postoperative", "post-op", "postop", "after surgery", "after thyroidectomy",
    "after tonsillectomy", "after laryngectomy", "fistula", "hematoma",
    "flap compromise", "wound", "salvage", "hypocalcemia", "chyle leak",
    "nerve injury", "csf leak", "infection", "dehiscence",
}

_MANAGEMENT_TERMS = {
    "management", "manage", "treat", "therapy", "next step", "best next",
    "indication", "contraindication", "observe", "surveillance", "antibiotic",
    "steroid", "radiation", "chemotherapy", "surgery", "operative", "drain",
    "biopsy", "workup", "imaging", "admit", "discharge", "airway",
}


def _norm(s):
    return re.sub(r"\s+", " ", str(s or "").strip().lower())


def _word_count(s):
    return len(re.findall(r"[a-z0-9]+", _norm(s)))


def _case_text(q):
    return " ".join(
        str(q.get(k, "") or "")
        for k in ("topic", "stem", "explanation", "board_pearl", "curveball")
    ).lower()


def _has_any(text, terms):
    text = _norm(text)
    return any(term in text for term in terms)


def _generic_why_wrong(q):
    choices = q.get("choices") or []
    reasons = q.get("why_wrong") or []
    try:
        answer = int(q.get("answer", -1))
    except Exception:
        answer = -1
    if len(reasons) != len(choices):
        return True
    wrong = [_norm(r) for i, r in enumerate(reasons) if i != answer]
    if not wrong:
        return True
    if len(set(wrong)) == 1:
        return True
    for r in wrong:
        if _word_count(r) < 7:
            return True
        if any(marker in r for marker in _GENERIC_WHY_WRONG):
            return True
    return False


def _case_quality_flags(q):
    flags = []
    choices = q.get("choices") or []
    try:
        answer = int(q.get("answer", -1))
    except Exception:
        answer = -1
    if len(choices) < 4:
        flags.append("<4 choices")
    if not 0 <= answer < len(choices):
        flags.append("invalid answer")
    if _word_count(q.get("stem")) < 14:
        flags.append("thin stem")
    if _word_count(q.get("explanation")) < 18:
        flags.append("thin explanation")
    if _word_count(q.get("board_pearl")) < 6:
        flags.append("thin pearl")
    if _word_count(q.get("curveball")) < 6:
        flags.append("thin curveball")
    if _generic_why_wrong(q):
        flags.append("generic why_wrong")
    return flags


def _topic_requirements(module):
    text = _norm(" ".join(str(module.get(k, "") or "") for k in
                          ("topic", "recognize", "localize", "workup", "manage", "operate", "teach")))
    return {
        "boards": True,
        "overnight_call": _has_any(text, _EMERGENCY_TERMS),
        "OR_prep": _has_any(_norm(module.get("operate", "")) + " " + _norm(module.get("topic", "")), _OPERATIVE_TERMS),
        "postoperative_call": _has_any(text, _POSTOP_TERMS),
    }


def _case_satisfies_focus(q, focus):
    if q.get("focus") == focus:
        return True
    text = _case_text(q)
    if focus == "boards":
        return bool(q.get("board_pearl")) and _has_any(text, _MANAGEMENT_TERMS)
    if focus == "overnight_call":
        return _has_any(text, _EMERGENCY_TERMS) and _has_any(text, {"urgent", "immediate", "tonight", "airway", "admit", "return to the or", "emergency"})
    if focus == "OR_prep":
        return _has_any(text, _OPERATIVE_TERMS) and _has_any(text, {"anatomy", "nerve", "vessel", "landmark", "dissection", "fixation", "closure", "graft", "flap", "operative", "surgery"})
    if focus == "postoperative_call":
        return _has_any(text, _POSTOP_TERMS) and _has_any(text, {"airway", "bleeding", "hematoma", "fistula", "infection", "compromise", "hypocalcemia", "leak", "wound"})
    return False


def _batch_prefix(qid):
    m = re.match(r"(v\d+)_", str(qid or ""))
    return m.group(1) if m else "legacy"


def build_report():
    cases = list(data.CLINICAL_CHALLENGES_V119)
    by_cid = defaultdict(list)
    for q in cases:
        if q.get("concept_id"):
            by_cid[q["concept_id"]].append(q)

    case_flags = {}
    generic_ids = []
    for q in cases:
        flags = _case_quality_flags(q)
        if flags:
            case_flags[q.get("id")] = flags
        if "generic why_wrong" in flags:
            generic_ids.append(q.get("id"))

    domain_rows = {}
    topic_gaps = []
    for domain, modules in data.DEEP_MODULES_V6.items():
        reviewed = 0
        clean = 0
        gaps = []
        for module in modules:
            topic = module.get("topic")
            if not topic:
                continue
            reviewed += 1
            cid = data._v6_item_id(domain, topic)
            linked = by_cid.get(cid, [])
            reasons = []
            if len(linked) < 2:
                reasons.append("fewer than 2 linked vignettes")

            clean_cases = [q for q in linked if not _case_quality_flags(q)]
            if len(clean_cases) < 1:
                reasons.append("no vignette passes case-quality gate")
            if len(clean_cases) < 2:
                reasons.append("fewer than 2 clean vignettes")

            if len(linked) >= 2:
                sims = []
                for i in range(len(linked)):
                    for j in range(i + 1, len(linked)):
                        sims.append(difflib.SequenceMatcher(None, _norm(linked[i].get("stem")), _norm(linked[j].get("stem"))).ratio())
                if sims and max(sims) >= 0.86:
                    reasons.append("near-duplicate vignette pair")

            req = _topic_requirements(module)
            for focus, needed in req.items():
                if needed and not any(_case_satisfies_focus(q, focus) for q in linked):
                    reasons.append(f"missing {focus} decision depth")

            if reasons:
                gap = {"topic": topic, "concept_id": cid, "reasons": sorted(set(reasons))}
                gaps.append(gap)
                topic_gaps.append((domain, gap))
            else:
                clean += 1
        domain_rows[domain] = {"topics": reviewed, "quality_clean": clean, "gaps": gaps}

    batches = defaultdict(list)
    for q in cases:
        batches[_batch_prefix(q.get("id"))].append(q)
    answer_bias = []
    for batch, qs in sorted(batches.items()):
        if len(qs) < 8:
            continue
        counts = Counter(int(q.get("answer", -1)) for q in qs if str(q.get("answer", "")).lstrip("-").isdigit())
        if not counts:
            continue
        idx, n = counts.most_common(1)[0]
        ratio = n / len(qs)
        if ratio >= 0.70:
            answer_bias.append({"batch": batch, "n": len(qs), "answer_index": idx, "ratio": round(ratio, 3)})

    return {
        "total_cases": len(cases),
        "generic_why_wrong_cases": generic_ids,
        "case_flags": case_flags,
        "domains": domain_rows,
        "topic_gap_count": len(topic_gaps),
        "answer_position_bias": answer_bias,
    }


def print_report(report):
    print("=== ENT MASTERY v14.9 RESIDENT-LEVEL QUALITY AUDIT ===")
    print(f"TOTAL_CASES|{report['total_cases']}")
    print(f"GENERIC_WHY_WRONG|{len(report['generic_why_wrong_cases'])}")
    for qid in report["generic_why_wrong_cases"]:
        print(f"GENERIC_CASE|{qid}")

    for domain, row in report["domains"].items():
        print(f"QUALITY_DOMAIN|{domain}|{row['quality_clean']}|{row['topics']}")
        for gap in row["gaps"]:
            print(f"QUALITY_GAP|{domain}|{gap['topic']}|{' ; '.join(gap['reasons'])}")

    for item in report["answer_position_bias"]:
        print(f"ANSWER_BIAS|{item['batch']}|n={item['n']}|index={item['answer_index']}|ratio={item['ratio']}")

    print(f"QUALITY_TOPIC_GAPS|{report['topic_gap_count']}")
    print("QUALITY_EXIT_STATUS|" + ("0" if report["topic_gap_count"] == 0 and not report["generic_why_wrong_cases"] and not report["answer_position_bias"] else "REVIEW_REQUIRED"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict-quality", action="store_true")
    args = parser.parse_args()
    report = build_report()
    print_report(report)
    has_gaps = bool(report["topic_gap_count"] or report["generic_why_wrong_cases"] or report["answer_position_bias"])
    if args.strict_quality and has_gaps:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
