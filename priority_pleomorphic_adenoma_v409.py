"""ENT Mastery v40.9 — evidence-calibrated pleomorphic-adenoma transformation risk."""

from copy import deepcopy


DOMAIN = "Thyroid / Parathyroid / Salivary"
TOPIC = "Pleomorphic Adenoma / Warthin Tumor"

HISTORICAL_SOURCE = (
    "Eneroth CM, Zetterberg A. Malignancy in pleomorphic adenoma: a clinical and "
    "microspectrophotometric study. Acta Otolaryngol. 1974;77:426-432. "
    "doi:10.3109/00016487409124645."
)
CONTEMPORARY_SOURCE = (
    "Levyn H et al. Risk of Carcinoma in Pleomorphic Adenomas of the Parotid. "
    "JAMA Otolaryngol Head Neck Surg. 2023;149:1034-1041. "
    "doi:10.1001/jamaoto.2023.3212."
)

MANAGEMENT_RATE = (
    "Quantify the risk without overstating certainty. The classic board/counseling "
    "figures from historical series are approximately 1.5% malignant transformation "
    "within 5 years and 9.5%-10% after more than 15 years untreated. Label these as "
    "historical estimates rather than a validated modern actuarial curve. In a modern "
    "cohort of clinically benign untreated parotid PAs, 5 of 156 tumors with benign "
    "preoperative cytology harbored CXPA at excision (3.2%; 95% CI, 1.4%-7.3%) and "
    "high-grade CXPA was found in 1.3%. Older age and larger tumor size were associated "
    "with CXPA detection, but observed tumor duration from 1-30 years was not."
)

TEACHING_RATE = (
    "Transformation-rate answer: quote the classic approximately 1.5% at 5 years and "
    "9.5%-10% beyond 15 years for boards, then add the contemporary qualifier: 3.2% "
    "CXPA detection (95% CI, 1.4%-7.3%) in a modern benign-cytology cohort, without an "
    "independent duration association. Detection at excision cannot prove when malignant "
    "transformation occurred."
)


def _append(row, field, text):
    prior = row.get(field) or ""
    if not isinstance(prior, str):
        raise RuntimeError(f"v40.9: nontext {field} field on {TOPIC}")
    marker = "v40.9 transformation risk: " + text
    if marker not in prior:
        row[field] = prior.rstrip() + ("\n\n" if prior.strip() else "") + marker


def apply_pleomorphic_adenoma_transformation_v409(data_module, app_module=None):
    deep = getattr(data_module, "DEEP_MODULES_V6", None)
    if not isinstance(deep, dict) or not isinstance(deep.get(DOMAIN), list):
        raise RuntimeError("v40.9: production Deep Curriculum registry unavailable")

    matches = [
        (index, row)
        for index, row in enumerate(deep[DOMAIN])
        if str(row.get("topic") or "").strip() == TOPIC
    ]
    if len(matches) != 1:
        raise RuntimeError(f"v40.9: expected one {TOPIC} row; found {len(matches)}")

    index, current = matches[0]
    updated = deepcopy(current)
    _append(updated, "manage", MANAGEMENT_RATE)
    _append(updated, "teach", TEACHING_RATE)

    sources = updated.get("source_basis") or []
    if isinstance(sources, str):
        sources = [sources]
    if not isinstance(sources, list):
        raise RuntimeError(f"v40.9: malformed source_basis on {TOPIC}")
    updated["source_basis"] = list(
        dict.fromkeys(sources + [HISTORICAL_SOURCE, CONTEMPORARY_SOURCE])
    )
    updated["transformation_risk_reviewed_v409"] = {
        "historical_board_estimate": "approximately 1.5% at 5 years; 9.5%-10% beyond 15 years",
        "contemporary_detection_rate": "3.2% (95% CI, 1.4%-7.3%); high-grade CXPA 1.3%",
        "interpretation": "duration was not independently associated; detection does not establish transformation timing",
    }

    deep[DOMAIN][index] = updated
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = deep
    return {
        "topic": TOPIC,
        "historical_rate_retained": True,
        "contemporary_rate_added": True,
    }
