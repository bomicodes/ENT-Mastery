"""v48.0 guideline-currency patches for legacy practice questions.

The v47 physiology text and concept checks were updated in place (pathophys_v470/,
cc_v471/). This module corrects older practice-bank items whose explanations
predate guideline changes. Each patch is keyed by question id and is a no-op if
the item is absent.
"""

PATCHES = {
    "v143_rhi_01": {
        "choices": {3: "The persistent-without-improvement pattern supports acute bacterial rhinosinusitis; watchful waiting with assured follow-up is the preferred first step, with amoxicillin (with or without clavulanate) if antibiotics are needed"},
        "explanation": "ABRS is a clinical diagnosis when acute rhinosinusitis persists at least about 10 days without improvement or worsens after initial improvement. Imaging is not routine in uncomplicated disease. The 2025 AAO-HNSF adult sinusitis update makes watchful waiting with assured follow-up the recommended initial approach; if antibiotics are used, amoxicillin with or without clavulanate for 5-7 days is first-line.",
    },
    "v128_hn_01": {
        "explanation": "AJCC 8 separated p16-positive oropharyngeal carcinoma because prognosis and nodal behavior differ substantially from p16-negative disease. AJCC Version 9 (in use from 2026) keeps the separate HPV-associated system and adds extranodal-extension upstaging of the N category.",
    },
}


def install_guideline_currency_v480(data):
    applied = []
    banks = [getattr(data, "CLINICAL_CHALLENGES_V119", []) or [], getattr(data, "CONCEPT_CHECKS_V112", []) or []]
    for bank in banks:
        for q in bank:
            p = PATCHES.get(q.get("id"))
            if not p:
                continue
            for i, text in p.get("choices", {}).items():
                if isinstance(q.get("choices"), list) and i < len(q["choices"]):
                    q["choices"][i] = text
            if "explanation" in p:
                q["explanation"] = p["explanation"]
            q["guideline_currency_v480"] = True
            applied.append(q.get("id"))
    data.GUIDELINE_CURRENCY_V480 = {"applied": applied}
    return data.GUIDELINE_CURRENCY_V480
