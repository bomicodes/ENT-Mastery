"""v26.9 anterior skull-base CSF leak decision/rescue layer.

Adds chief-level intraoperative commitment points to the live OR Tomorrow CSF-leak
repair case without replacing the existing procedure-specific sequence. The goal is
to make defect-flow classification, reconstruction escalation, selective CSF
diversion, and vascular bailout explicit while preserving clinically equivalent
technique choices.
"""

TARGET = {
    "preferred_slug": "csf-nasoseptal",
    "aliases": ("csf leak", "nasoseptal flap", "skull base repair"),
    "steps": [
        "When the skull-base defect is exposed or an unexpected intraoperative CSF leak is encountered, stop nonessential dissection and define the exact defect, its low- versus high-flow character, surrounding bony/dural margins, and adjacent orbit, optic nerve and carotid anatomy before enlarging or manipulating the site further.",
        "Match reconstruction to the defect rather than using one closure for every leak: a small low-flow defect may be closed with a deliberate multilayer free-graft construct, whereas a large/high-flow defect or high-risk tissue bed should escalate to multilayer reconstruction with a vascularized pedicled flap when available. Seat each layer on stable healthy margins and preserve the flap pedicle without twist, tension or compression.",
        "After reconstruction, inspect the entire defect and flap contact, support the construct without excessive orbital or pedicle pressure, and assess for persistent leakage under an appropriate physiologic challenge. A lumbar drain is selective adjunctive CSF diversion for chosen high-risk situations—not a substitute for a mechanically sound closure and not an automatic requirement for every endonasal leak.",
        "If brisk arterial hemorrhage obscures the field or raises concern for carotid or another major-vessel injury, abandon the routine leak-repair sequence and execute the vascular-injury rescue plan. Maintain controlled visualization/temporary hemostasis and obtain vascular/skull-base help rather than applying blind deep cautery or unplanned instrumentation adjacent to a suspected arterial injury.",
    ],
}


def _norm(value):
    return " ".join(str(value).lower().replace("-", " ").split())


def _resolve(registry):
    reg = registry or {}
    preferred = TARGET["preferred_slug"]
    if preferred in reg:
        return preferred, reg[preferred]
    for slug, op in reg.items():
        hay = _norm(str(slug) + " " + str((op or {}).get("title", "")))
        if any(_norm(alias) in hay for alias in TARGET["aliases"]):
            return slug, op
    return None, None


def _append_unique(values, additions):
    out = list(values or [])
    changed = False
    for text in additions:
        marker = _norm(text[:80])
        if not any(marker in _norm(existing) for existing in out):
            out.append(text)
            changed = True
    return out, changed


def apply_or_csf_rescue_v269(registry):
    slug, op = _resolve(registry)
    if not op:
        return {"changed": [], "count": 0, "resolved": None, "missing": [TARGET["preferred_slug"]]}
    op["steps"], changed = _append_unique(op.get("steps"), TARGET["steps"])
    op["csf_rescue_v269"] = True
    return {
        "changed": [slug] if changed else [],
        "count": 1 if changed else 0,
        "resolved": slug,
        "missing": [],
    }
