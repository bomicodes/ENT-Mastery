"""v99.0: data-driven installer for new curriculum topics found in the textbook gap review.

Each topic lives in new_topics_v990/<slug>.py as TOPIC = {...} with:
  domain, topic, overview, physiology, pathophysiology, recognize, localize, workup, manage,
  operate, teach, tags, source_basis, textbook_refs, literature_refs, case_label, or_slugs,
  concept_check (one MCQ: stem, choices, answer, explanation, why_wrong, board_pearl, curveball),
  ladder (three items: foundation, application, senior_decision, v49 vignette fields),
  vignettes (four or more v49-format items).
It installs them the same way the v50.1 Eagle topic was installed (Deep Curriculum entry, blind case
label, OR map, Concept Check, learning ladder, board vignettes) and, after the v47.2 cross-reference
layer, their textbook and literature references. Install before the v47 installers.
"""
from __future__ import annotations

import importlib
import pkgutil

DEEP_FIELDS = ("overview", "physiology", "pathophysiology", "recognize", "localize", "workup",
               "manage", "operate", "teach")
STAGES = ("foundation", "application", "senior_decision")


import re as _re

_ACTION = _re.compile(
    r"^(proceed|perform|start|begin|give|add|switch|stop|continue|observe|observation|repeat|obtain|order|"
    r"refer|reassure|cancel|abort|defer|accept|resect|excis|excision|incision|enucleat|biopsy|incisional|"
    r"deep biopsy|fine-needle|ct|mri|pet|imaging|echocardiogram|bartonella|ppd|urgent|immediate|emergency|"
    r"emergent|endoscopic|open|total|subtotal|partial|lateral|radical|segmental|marginal|sleeve|revise|"
    r"revision|tracheotomy|tracheostomy|balloon|serial|simple|primary|concurrent|multimodal|multiagent|"
    r"radiation|radiotherapy|chemo|systemic|iv |oral |topical|suppressive|four-drug|multidrug|curettage|"
    r"arthrocentesis|occlusal|gap arthroplasty|condylar|bilateral coronoid|wide local|craniofacial|orbital|"
    r"leave|pack|upsize|lacrimal|probing|lester|botulinum|silicone|warm|free mucosal|fat plug|multilayer|"
    r"tympanostomy|nasopharyngoscopy|panendoscopy|empiric|clarithromycin|azithromycin|benzathine|doxycycline|"
    r"intratympanic|prolonged|daily|tonsillectomy|adenoidectomy|decline|distraction|costochondral|ear reconstruction|"
    r"increase|routine|genetic testing|laser|decompression|somatostatin|proceed|transoral|slide|resection|"
    r"palliative|canal wall|dacryo|external|steroid|avoid|lmwh|fresh frozen|start the|smaller dose|"
    r"superficial parotid|ampicillin|vancomycin|awake|humidified)", _re.I)


def _question_for(q):
    choices = q.get("choices") or []
    acts = sum(1 for c in choices if _ACTION.match(str(c).strip()))
    if sum(1 for c in choices if _re.match(r"^T[0-4][abis]*\b", str(c).strip())) >= 2:
        return "What is the correct stage?"
    if acts >= 2:
        return "What is the most appropriate next step?"
    if q.get("focus") == "diagnosis":
        return "What is the most likely diagnosis?"
    return "Which of the following is the best answer?"


def _ask(q):
    """Some authored stems end on the findings; add a question matched to the choices so every stem asks one."""
    if isinstance(q, dict) and "?" not in q.get("stem", ""):
        q = dict(q, stem=q["stem"].rstrip() + " " + _question_for(q))
    return q


def load_topics():
    import new_topics_v990_data as pkg
    out = []
    for info in sorted(pkgutil.iter_modules(pkg.__path__), key=lambda i: i.name):
        mod = importlib.import_module("new_topics_v990_data." + info.name)
        t = getattr(mod, "TOPIC", None)
        if t:
            t = dict(t, _slug=info.name)
            t["concept_check"] = _ask(t.get("concept_check"))
            t["ladder"] = [_ask(q) for q in t.get("ladder", [])]
            t["vignettes"] = [_ask(q) for q in t.get("vignettes", [])]
            out.append(t)
    return out


def _vignette_ok(q, cid):
    from clinical_challenge_vignettes_v490 import REQUIRED
    return (all(k in q for k in REQUIRED) and len(q["choices"]) == 4 and isinstance(q["answer"], int)
            and 0 <= q["answer"] < 4 and len(q["why_wrong"]) == 4 and q["why_wrong"][q["answer"]] == "Correct."
            and q.get("concept_id", cid) == cid)


def install_new_topics_v990(data, app_mod):
    import textbook_curriculum_v470
    import daily_curriculum_quality_v368
    from clinical_challenge_vignettes_v490 import MODE, REQUIRED

    result = {"topics": [], "vignettes": 0, "ladder": 0, "checks": 0, "rejected": []}
    deep = data.DEEP_MODULES_V6
    have_topics = {m.get("topic") for mods in deep.values() for m in mods}
    checks = data.CONCEPT_CHECKS_V112
    have_checks = {q.get("id") for q in checks}
    bank = data.CLINICAL_CHALLENGES_V119
    have_q = {q.get("id") for q in bank}

    for t in load_topics():
        dom, name = t["domain"], t["topic"]
        cid = app_mod._v6_item_id(dom, name)
        slug = t["_slug"]
        if name not in have_topics:
            entry = {"topic": name, "primary_domain": dom, "tags": list(t.get("tags", [])),
                     "source_basis": list(t.get("source_basis", [])),
                     "source_metadata_v408": {"canonical_domain": dom, "canonical_topic": name,
                                              "scope": "chapter/page textbook locator plus topic-specific literature",
                                              "locator_level": "topic", "reviewed_after": "v99.0"},
                     "depth_reviewed_v408": True}
            for f in DEEP_FIELDS:
                entry[f] = t.get(f, "")
            deep.setdefault(dom, []).append(entry)
            have_topics.add(name)
            result["topics"].append(name)
        if t.get("case_label"):
            daily_curriculum_quality_v368.TOPIC_CASE_LABELS.setdefault(name, t["case_label"])
        textbook_curriculum_v470.TOPIC_OR_MAP_V470.setdefault(name, list(t.get("or_slugs", [])))

        cc = t.get("concept_check")
        if cc:
            ccid = "cc-v112-mgt-" + cid[len("v6-"):] if cid.startswith("v6-") else "cc-v990-" + slug
            if ccid not in have_checks:
                cc = dict(cc, prompt=cc["stem"])
                row = dict(cc, id=ccid, domain=dom, topic=name, concept_id=cid, tier="Concept check",
                           mode="Manage", assessment_class="decision", graded_discrimination=True,
                           choices=list(cc["choices"]), why_wrong=list(cc["why_wrong"]),
                           reviewed_all_domains_v178=True, board_review_standard_v178="clinical decision-making",
                           review_basis_v178=list(t.get("source_basis", [])), canonical_topic=name)
                checks.append(row)
                have_checks.add(ccid)
                result["checks"] += 1

        for stage, q in zip(STAGES, t.get("ladder", [])):
            qid = f"v990_{slug}_{stage[:3]}"
            if qid in have_q:
                continue
            if not _vignette_ok(dict(q, concept_id=cid, learning_stage=stage), cid):
                result["rejected"].append(qid)
                continue
            row = {k: q[k] for k in REQUIRED if k in q}
            row.update({"id": qid, "domain": dom, "topic": name, "tier": "Curated learning ladder",
                        "mode": "Vignette", "concept_id": cid, "ladder_reviewed": True,
                        "_coverage_reviewed_v211": True, "learning_stage": stage,
                        "choices": list(q["choices"]), "why_wrong": list(q["why_wrong"])})
            bank.append(row)
            have_q.add(qid)
            result["ladder"] += 1

        for n, q in enumerate(t.get("vignettes", []), 1):
            qid = f"v990-{slug.replace('_', '-')}-{n}"
            if qid in have_q:
                continue
            q = dict(q, concept_id=cid, topic=name)
            if not _vignette_ok(q, cid):
                result["rejected"].append(qid)
                continue
            row = {k: q[k] for k in REQUIRED}
            row.update({"id": qid, "domain": dom, "topic": name, "tier": "Curated board-style",
                        "mode": MODE.get(q["focus"], "Reasoning"), "authored_v490": True})
            bank.append(row)
            have_q.add(qid)
            result["vignettes"] += 1

    by_id = {q["id"]: q for q in checks if q.get("id")}
    data.CONCEPT_CHECK_BY_ID_V112 = by_id
    app_mod.CONCEPT_CHECKS_V112 = checks
    app_mod.CONCEPT_CHECK_BY_ID_V112 = by_id
    if getattr(app_mod, "DEEP_MODULES_V6", None) is not deep:
        app_mod.DEEP_MODULES_V6 = deep
    if getattr(app_mod, "CLINICAL_CHALLENGES_V119", None) is not bank:
        app_mod.CLINICAL_CHALLENGES_V119 = bank
    for holder in (data, app_mod):
        index = getattr(holder, "CLINICAL_CHALLENGE_BY_ID_V119", None)
        if isinstance(index, dict):
            index.update({q["id"]: q for q in bank if str(q.get("id", "")).startswith("v990")})
    data.NEW_TOPICS_V990 = result
    return result


def install_new_topics_refs_v990(data):
    lit = getattr(data, "LITERATURE_REFS_V472", None)
    books = getattr(data, "TEXTBOOK_REFS_V472", None)
    n = 0
    for t in load_topics():
        if isinstance(lit, dict) and t.get("literature_refs"):
            lit.setdefault(t["topic"], list(t["literature_refs"]))
        if isinstance(books, dict):
            lst = books.setdefault(t["topic"], [])
            for label in t.get("textbook_refs", []):
                if label not in lst:
                    lst.append(label)
        n += 1
    return {"topics": n}
