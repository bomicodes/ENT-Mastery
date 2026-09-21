"""ENT Mastery v41.0 — evidence-calibrated trauma context for first-bite syndrome."""

from copy import deepcopy


DOMAIN = "Thyroid / Parathyroid / Salivary"
TOPIC = "First-Bite Syndrome"

STEEL_SOURCE = (
    "Steel SJ, Robertson CE. First Bite Syndrome: What Neurologists Need to Know. "
    "Curr Pain Headache Rep. 2021;25(5):31. doi:10.1007/s11916-021-00950-7 — "
    "review supporting the sympathetic/parasympathetic imbalance model and identifying "
    "postsurgical and neoplastic disease as the established secondary settings."
)
TRAUMA_EVIDENCE_NOTE = (
    "v41.0 evidence note — Direct evidence for nonoperative blunt or penetrating trauma "
    "as a cause of first-bite syndrome is sparse; do not present external trauma as a "
    "common or equally established etiology. A causal attribution is anatomically plausible "
    "only when the injury could disrupt the upper cervical sympathetic chain, the peri-carotid/"
    "external-carotid sympathetic plexus, or postganglionic sympathetic fibers entering the parotid."
)

DIAGNOSIS_TRAUMA = (
    "Trauma nuance: specifically ask about recent blunt or penetrating parotid, retromandibular, "
    "upper-neck, or carotid-space trauma, but distinguish this from the far better established "
    "postoperative syndrome. "
    "External trauma is a rare, sparsely documented consideration—not a default explanation—and "
    "is anatomically plausible only when the mechanism could injure the cervical sympathetic "
    "chain, peri-carotid/external-carotid sympathetic plexus, or postganglionic sympathetic fibers "
    "entering the gland. A deep-lobe or retromandibular parotid injury is especially plausible, "
    "although a sufficiently deep direct parotid injury need not be confined to the deep lobe. "
    "Superficial bruising alone is not the classic mechanism."
)

WORKUP_TRAUMA = (
    "For new first-bite-pattern pain after nonoperative neck trauma, examine for Horner syndrome "
    "and cranial neuropathies and ask about focal neck swelling, neurologic deficits, dysphagia, "
    "dysphonia, or vascular symptoms. Use anatomy- and mechanism-directed contrast CT or MRI when "
    "the syndrome lacks a clear operative cause; add CTA/MRA when the trauma history or examination "
    "raises concern for carotid-space vascular injury. Do not label the syndrome idiopathic—or "
    "attribute it to trauma—before excluding an occult deep parotid, parapharyngeal, carotid-space, "
    "or skull-base lesion."
)

TEACHING_TRAUMA = (
    "TRAUMA PEARL: operative injury is the classic traumatic insult. Nonoperative upper-neck or "
    "direct parotid trauma may be considered when the depth and location map to the sympathetic "
    "pathway; deep-lobe/retromandibular injury is most intuitive but is not an absolute requirement. "
    "The published evidence is sparse, so treat trauma as an uncommon secondary context and "
    "investigate unexplained cases structurally."
)


def _append(row, field, text):
    prior = row.get(field) or ""
    if not isinstance(prior, str):
        raise RuntimeError(f"v41.0: nontext {field} field on {TOPIC}")
    marker = "v41.0 trauma context: " + text
    if marker not in prior:
        row[field] = prior.rstrip() + ("\n\n" if prior.strip() else "") + marker


def apply_first_bite_trauma_v410(data_module, app_module=None):
    deep = getattr(data_module, "DEEP_MODULES_V6", None)
    if not isinstance(deep, dict) or not isinstance(deep.get(DOMAIN), list):
        raise RuntimeError("v41.0: production Deep Curriculum registry unavailable")

    matches = [
        (index, row)
        for index, row in enumerate(deep[DOMAIN])
        if str(row.get("topic") or "").strip() == TOPIC
    ]
    if len(matches) != 1:
        raise RuntimeError(f"v41.0: expected one {TOPIC} row; found {len(matches)}")

    index, current = matches[0]
    updated = deepcopy(current)
    _append(updated, "diagnose", DIAGNOSIS_TRAUMA)
    _append(updated, "diagnose", WORKUP_TRAUMA)
    _append(updated, "teach", TEACHING_TRAUMA)

    tags = updated.get("tags") or []
    if not isinstance(tags, list):
        raise RuntimeError(f"v41.0: malformed tags on {TOPIC}")
    updated["tags"] = list(dict.fromkeys(tags + [
        "upper neck trauma",
        "cervical sympathetic injury",
        "trauma imaging red flag",
    ]))

    sources = updated.get("source_basis") or []
    if isinstance(sources, str):
        sources = [sources]
    if not isinstance(sources, list):
        raise RuntimeError(f"v41.0: malformed source_basis on {TOPIC}")
    updated["source_basis"] = list(
        dict.fromkeys(sources + [STEEL_SOURCE, TRAUMA_EVIDENCE_NOTE])
    )
    updated["trauma_context_reviewed_v410"] = {
        "established_context": "iatrogenic sympathetic injury after surgery",
        "external_trauma": "rare and sparsely documented; require an anatomically plausible injury",
        "safety_rule": "image unexplained cases and evaluate possible vascular injury when indicated",
    }

    deep[DOMAIN][index] = updated
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = deep
    return {
        "topic": TOPIC,
        "trauma_context_added": True,
        "evidence_limit_explicit": True,
    }
