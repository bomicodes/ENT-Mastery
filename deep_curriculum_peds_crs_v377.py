"""v37.7 - Pediatric Chronic Rhinosinusitis: operationalize surgical escalation.

Adds the adenoidectomy-first versus ESS escalation logic behind vague "selected patients"
language. The evidence does not support an invented universal antibiotic-duration, CT-score,
or age cutoff for surgery; decisions remain phenotype- and response-based.

Sources: AAO-HNSF Pediatric CRS Clinical Consensus Statement (2014, PMID 25274375),
contemporary pediatric CRS reviews including PMID 39392410 and PMID 38400707.
Idempotent.
"""

TOPIC = "Pediatric Chronic Rhinosinusitis"
MARKER = "PEDIATRIC CRS SURGICAL LADDER"

OPERATE_ADDENDUM = (
    " PEDIATRIC CRS SURGICAL LADDER: first confirm persistent pediatric CRS rather than recurrent "
    "viral URIs/adenoiditis and address appropriate medical therapy and important modifiers such "
    "as allergy, asthma, immune deficiency, cystic fibrosis or primary ciliary dyskinesia when the "
    "history suggests them. For uncomplicated medically refractory pediatric CRS, ADENOIDECTOMY is "
    "generally the first-line operation, particularly in younger/pre-adolescent children, because "
    "the adenoid can function as an inflammatory/bacterial reservoir; adenoid size alone is not the "
    "criterion. Persistent objective/symptomatic CRS after appropriate medical management and "
    "adenoidectomy is the usual pathway to ENDOSCOPIC SINUS SURGERY (ESS), with CT obtained for "
    "operative planning and extent tailored to involved sinuses/anatomy rather than a mandatory "
    "Lund-Mackay cutoff. ESS may reasonably move earlier in children with cystic fibrosis, primary "
    "ciliary dyskinesia, significant nasal polyposis, or complications when disease biology and "
    "clinical need justify it. Balloon dilation is not a required step between adenoidectomy and "
    "ESS; current evidence has not established it as a superior or mandatory first-line pediatric "
    "CRS operation. There is likewise no evidence-based universal number of antibiotic weeks or "
    "single age threshold that must be met before surgery: document persistent symptoms plus "
    "objective disease, prior therapy, comorbidity and expected benefit instead of using a ritual "
    "checklist."
)


def apply_pediatric_crs_surgery_v377(data_module, app_module=None):
    patched = []
    for modules in (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).values():
        for module in modules or []:
            if module.get("topic") != TOPIC:
                continue
            current = module.get("operate", "") or ""
            if MARKER not in current:
                module["operate"] = current.rstrip() + OPERATE_ADDENDUM
            tags = module.setdefault("tags", [])
            for tag in ("adenoidectomy first-line", "pediatric ESS", "surgical escalation", "no fixed medical-therapy cutoff"):
                if tag not in tags:
                    tags.append(tag)
            patched.append(TOPIC)
    if not patched:
        raise RuntimeError("v37.7: could not find canonical Pediatric Chronic Rhinosinusitis topic")
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
