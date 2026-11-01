"""v53.2: real-image Interpretation Atlas studies and image questions in the bank.

Loads labs_v532/*.py. Each file adds cases to an existing lab (TARGET_LAB) or
creates a new lab (LAB dict). Every case's "mcq" becomes:
  * a Quick check in the lab (objective, scored, replaces the self-rating), and
  * a board-style image question in the Clinical Challenges bank and exam mode.
labs_v532/existing_mcq.py may hold MCQ_BY_CASE = {case_id: mcq} for image
cases that predate this release.
"""
import importlib
import pkgutil

ALLOWED_HOSTS = ("https://cdn.ncbi.nlm.nih.gov/", "https://upload.wikimedia.org/", "https://www.ncbi.nlm.nih.gov/", "https://europepmc.org/")
REQUIRED = ("id", "level", "prompt", "answer", "why", "image_url", "image_credit", "image_source")


def _valid_mcq(m):
    return (isinstance(m, dict) and isinstance(m.get("choices"), list) and len(m["choices"]) == 4
            and isinstance(m.get("answer"), int) and 0 <= m["answer"] <= 3 and m.get("question"))


def _bank_item(case, lab_slug, lab_title):
    m = case["mcq"]
    ans = m["answer"]
    return {
        "id": "img_" + case["id"],
        "domain": m.get("domain") or "General ENT / Emergencies",
        "topic": m.get("topic") or lab_title,
        "stem": m["question"],
        "choices": list(m["choices"]),
        "answer": ans,
        "explanation": m.get("explanation") or case.get("answer", ""),
        "why_wrong": [("" if i == ans else w) for i, w in enumerate(m.get("why_wrong") or ["", "", "", ""])],
        "board_pearl": case.get("why", ""),
        "curveball": case.get("follow", ""),
        "curveball_answer": case.get("follow_answer", ""),
        "concept_id": case.get("concept_id") or f"{lab_slug}:{case['id']}",
        "tier": "Curated board-style",
        "mode": "Recognize",
        "focus": "boards",
        "image_url": case["image_url"],
        "image_credit": case["image_credit"],
        "image_source": case["image_source"],
        "image_question_v532": True,
        "source_lab": lab_slug,
    }


def install_interpretation_labs_v532(data, app=None):
    labs = data.INTERPRETATION_LABS
    report = {"files": [], "added": 0, "rejected": [], "new_labs": [], "bank_added": 0}
    import labs_v532 as pkg
    mods = []
    for info in pkgutil.iter_modules(pkg.__path__):
        mods.append(importlib.import_module(f"labs_v532.{info.name}"))

    extra_mcq = {}
    for mod in mods:
        extra_mcq.update(getattr(mod, "MCQ_BY_CASE", {}) or {})

    seen = {c.get("id") for lab in labs.values() for c in lab.get("cases", [])}
    bank = data.CLINICAL_CHALLENGES_V119
    by_id = data.CLINICAL_CHALLENGE_BY_ID_V119

    for mod in mods:
        cases = getattr(mod, "CASES", None)
        target = getattr(mod, "TARGET_LAB", None)
        if not cases or not target:
            continue
        lab_def = getattr(mod, "LAB", None)
        if target not in labs:
            if not lab_def:
                report["rejected"].append((mod.__name__, "unknown lab and no LAB definition"))
                continue
            labs[target] = {
                "title": lab_def["title"], "icon": lab_def.get("icon", "◈"), "subtitle": lab_def.get("subtitle", ""),
                "framework": lab_def.get("framework", []), "source_note": lab_def.get("source_note", ""),
                "resources": lab_def.get("resources", []), "cases": [], "fundamentals": [], "new_v532": True,
            }
            report["new_labs"].append(target)
        lab = labs[target]
        n = 0
        for c in cases:
            missing = [k for k in REQUIRED if not c.get(k)]
            if missing:
                report["rejected"].append((c.get("id"), "missing " + ",".join(missing)))
                continue
            if not c["image_url"].startswith(ALLOWED_HOSTS):
                report["rejected"].append((c["id"], "image host not allowed"))
                continue
            if c["id"] in seen:
                report["rejected"].append((c["id"], "duplicate id"))
                continue
            if c.get("mcq") is not None and not _valid_mcq(c["mcq"]):
                report["rejected"].append((c["id"], "bad mcq"))
                c = dict(c, mcq=None)
            c = dict(c)
            c.setdefault("variant_type", "interpret")
            c.setdefault("concept_id", f"{target}:{c['id']}")
            c["new_v532"] = True
            lab["cases"].append(c)
            seen.add(c["id"])
            n += 1
        lab["seed_case_count"] = len(lab["cases"])
        report["files"].append((mod.__name__, target, n))
        report["added"] += n

    # attach extra MCQs to older image cases
    for lab in labs.values():
        for c in lab.get("cases", []):
            if not c.get("mcq") and c.get("id") in extra_mcq and _valid_mcq(extra_mcq[c["id"]]):
                c["mcq"] = extra_mcq[c["id"]]

    # image questions into the bank
    for slug, lab in labs.items():
        for c in lab.get("cases", []):
            if c.get("mcq") and c.get("image_url") and _valid_mcq(c["mcq"]):
                item = _bank_item(c, slug, lab.get("title", slug))
                if item["id"] in by_id:
                    continue
                bank.append(item)
                by_id[item["id"]] = item
                report["bank_added"] += 1
    data.INTERPRETATION_LABS_V532 = report
    return report
