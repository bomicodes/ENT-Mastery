"""v43.3: Mock oral-board case simulator.

Requested 2026-09-22: a structured oral-board-style format -- a case that escalates
through examiner-style follow-up questions, self-tested by reveal (read, think out
loud, reveal the model answer, move to the next escalation) rather than multiple
choice. Per the user's explicit direction, this reuses existing curriculum content
rather than authoring new case scripts:

- Clinical Challenges (CLINICAL_CHALLENGES_V119) already carry a case stem, a correct
  answer + explanation, and an "attending curveball" follow-up with its own answer --
  exactly a two-step escalating oral-board exchange.
- OR_PREP_REGISTRY cards already carry landmarks/danger points (a natural opening
  "name the danger structures" pimp question) followed by a chain of 3-4 attending
  follow-up Q&A pairs (now uniformly >=3 after the v43.2 gap-fill) -- exactly a
  multi-step OR-pimping escalation.

This module adds no new curriculum content. It adds one new route, `/oral-boards`,
that randomly (or specifically, via ?id=) selects one item from either source,
reshapes it into a linear list of escalating {prompt, reveal} steps, and renders it
one case at a time for self-testing, with domain/source filters and a "new case"
control. No answer grading or mastery-tracking is added -- this is a self-test/reveal
study format, not a scored assessment, per the user's explicit choice.
"""

import random

from flask import render_template, request


# OR-prep uses shorter procedure domains than the deep curriculum's nine domains.
OR_DOMAIN_MAP = {
    "Otology": "Otology / Neurotology", "Neurotology": "Otology / Neurotology",
    "Skull Base": "Otology / Neurotology",
    "Rhinology": "Rhinology / Allergy / Skull Base",
    "Rhinology / Facial Plastics": "Rhinology / Allergy / Skull Base",
    "Head & Neck": "Head & Neck Oncology",
    "Head & Neck Reconstruction": "Head & Neck Oncology",
    "Head & Neck / Laryngology": "Laryngology / Voice / Swallowing",
    "Head & Neck / Salivary": "Thyroid / Parathyroid / Salivary",
    "Salivary": "Thyroid / Parathyroid / Salivary",
    "Endocrine": "Thyroid / Parathyroid / Salivary",
    "Thyroid / Endocrine Surgery": "Thyroid / Parathyroid / Salivary",
    "Pediatrics": "Pediatric Otolaryngology",
    "Pediatrics/General": "Pediatric Otolaryngology",
    "Pediatric Airway": "Pediatric Otolaryngology",
    "Pediatric / Emergency ENT": "Pediatric Otolaryngology",
    "Pediatric Otolaryngology / Sleep": "Pediatric Otolaryngology",
    "General ENT / Pediatrics": "Pediatric Otolaryngology",
    "Laryngology": "Laryngology / Voice / Swallowing",
    "Laryngology / Trauma": "Laryngology / Voice / Swallowing",
    "Laryngology/Airway": "Laryngology / Voice / Swallowing",
    "Swallowing": "Laryngology / Voice / Swallowing",
    "Facial Plastics": "Facial Plastics / Trauma",
    "Facial Trauma": "Facial Plastics / Trauma",
    "Facial Trauma / Skull Base": "Facial Plastics / Trauma",
    "Sleep": "Sleep Surgery", "Sleep / Airway": "Sleep Surgery",
    "Airway": "General ENT / Emergencies",
    "Airway / General ENT": "General ENT / Emergencies",
    "General ENT": "General ENT / Emergencies",
}


def _or_domain(card):
    label = card.get("domain") or ""
    return OR_DOMAIN_MAP.get(label, label)


def _clinical_case(q):
    steps = []
    try:
        correct_choice = q["choices"][q["answer"]]
    except (KeyError, IndexError, TypeError):
        correct_choice = None
    answer_reveal = q.get("explanation") or ""
    if correct_choice:
        answer_reveal = f"Best answer: {correct_choice}\n\n{answer_reveal}"
    prompt = q.get("stem") or ""
    # A few source questions ask the learner to choose among patients/options;
    # include those options so the prompt remains answerable without the quiz UI.
    if prompt.lower().startswith(("which patient", "which of the following")) and q.get("choices"):
        prompt += "\n\n" + "\n".join(
            f"{chr(65 + i)}. {choice}" for i, choice in enumerate(q["choices"])
        )
    steps.append({"label": "Case", "prompt": prompt, "reveal": answer_reveal})
    if q.get("curveball"):
        steps.append({
            "label": "Attending curveball",
            "prompt": q["curveball"],
            "reveal": q.get("curveball_answer") or "",
        })
    return {
        "source": "clinical",
        "id": q.get("id"),
        "title": q.get("topic") or "Clinical Challenge",
        "domain": q.get("domain") or "",
        "subtitle": q.get("tier") or "Clinical vignette",
        "steps": [s for s in steps if s["prompt"]],
        "pearl": q.get("board_pearl"),
        "concept_id": q.get("concept_id"),
        "context": None,
    }


def _or_prep_case(slug, card):
    steps = []
    landmarks = card.get("landmarks") or []
    danger = card.get("danger") or []
    if landmarks or danger:
        parts = []
        if landmarks:
            parts.append("Landmarks: " + "; ".join(str(x) for x in landmarks))
        if danger:
            parts.append("Danger points: " + "; ".join(str(x) for x in danger))
        steps.append({
            "label": "Set the stage",
            "prompt": "Before you start: what are the key landmarks and danger structures for this case?",
            "reveal": "\n\n".join(parts),
        })
    for i, pair in enumerate(card.get("attending_followup") or []):
        if not isinstance(pair, (list, tuple)) or len(pair) < 2:
            continue
        steps.append({"label": f"Attending pimp #{i + 1}", "prompt": pair[0], "reveal": pair[1]})
    return {
        "source": "or_prep",
        "id": slug,
        "title": card.get("title") or "OR Case",
        "domain": _or_domain(card),
        "subtitle": "OR-prep / attending pimping",
        "steps": [s for s in steps if s["prompt"]],
        "pearl": None,
        "concept_id": card.get("linked_topic") if (card.get("linked_topic") or "").startswith("v6-") else None,
        "context": card.get("indications"),
    }


def _build_pool(data_module, source, domain):
    pool = []
    if source in ("all", "clinical"):
        for q in data_module.CLINICAL_CHALLENGES_V119:
            if domain != "all" and q.get("domain") != domain:
                continue
            if q.get("id"):
                pool.append(("clinical", q["id"]))
    if source in ("all", "or_prep"):
        for slug, card in (data_module.OR_PREP_REGISTRY or {}).items():
            if not isinstance(card, dict):
                continue
            if domain != "all" and _or_domain(card) != domain:
                continue
            pool.append(("or_prep", slug))
    return pool


def _load_case(data_module, src, cid):
    if src == "clinical":
        q = next((x for x in data_module.CLINICAL_CHALLENGES_V119 if x.get("id") == cid), None)
        return _clinical_case(q) if q else None
    if src == "or_prep":
        card = (data_module.OR_PREP_REGISTRY or {}).get(cid)
        return _or_prep_case(cid, card) if card else None
    return None


def _make_view(data_module):
    def oral_boards_view():
        source = request.args.get("source", "all")
        if source not in ("all", "clinical", "or_prep"):
            source = "all"
        domain = request.args.get("domain", "all")
        if domain not in data_module.CANONICAL_DOMAINS_V94:
            domain = "all"
        case_id = request.args.get("id", "").strip()

        pool = _build_pool(data_module, source, domain)
        previous = request.args.get("exclude", "")
        if not case_id and len(pool) > 1:
            alternatives = [item for item in pool if item[1] != previous]
            if alternatives:
                pool_for_random = alternatives
            else:
                pool_for_random = pool
        else:
            pool_for_random = pool

        case = None
        if case_id:
            for src, cid in pool:
                if cid == case_id:
                    case = _load_case(data_module, src, cid)
                    break
        if case is None and pool:
            src, cid = random.choice(pool_for_random)
            case = _load_case(data_module, src, cid)

        return render_template(
            "oral_board.html",
            case=case,
            source=source,
            domain=domain,
            domains=data_module.CANONICAL_DOMAINS_V94,
            pool_size=len(pool),
        )

    return oral_boards_view


def apply_oral_board_simulator_v433(data_module, app_module):
    flask_app = app_module.app
    view = _make_view(data_module)
    if "oral_boards_v433" not in flask_app.view_functions:
        flask_app.add_url_rule("/oral-boards", "oral_boards_v433", view, methods=["GET"])
    return {"route": "/oral-boards"}
