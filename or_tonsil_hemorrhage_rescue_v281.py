"""v28.1 — post-tonsillectomy hemorrhage recognition and rescue for OR Tomorrow.

Adds executable resident/chief-level rescue to live tonsillectomy/adenotonsillectomy
cards without replacing the existing procedure-specific operative sequence.
"""

SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7e — tonsil/adenoid surgery, tonsillar-bed hemostasis, and postoperative hemorrhage principles",
    "K.J. Lee's Essential Otolaryngology, 12e — tonsil/adenoid surgery and postoperative bleeding principles",
    "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6e — tonsillectomy/adenoidectomy and postoperative complication framework",
    "AAO-HNSF Clinical Practice Guideline: Tonsillectomy in Children (Update). Otolaryngol Head Neck Surg. 2019;160(1 Suppl):S1-S42 — postoperative bleeding surveillance and evidence-based postoperative care",
    "Casey C et al. Tranexamic acid and beyond: A systematic review of pediatric post-tonsillectomy hemorrhage protocols and introduction of a universal management guideline. Int J Pediatr Otorhinolaryngol. 2026;207:112918 — contemporary acute PTH protocol synthesis",
    "The Effectiveness of Tranexamic Acid in Pediatric Posttonsillectomy Hemorrhage: A Systematic Review and Meta-Analysis. 2026 — TXA associated with reduced reoperation; adjunctive rather than definitive source control",
    "van Cruijsen N et al. Post-tonsillectomy pseudoaneurysm: an underestimated entity? J Laryngol Otol. 2008/2009 — recurrent delayed gushing hemorrhage as a pseudoaneurysm warning and angiographic/endovascular management",
]

POSTOP = [
    "POST-TONSILLECTOMY HEMORRHAGE COMMITMENT POINT: any active bleeding, repeated bright-red expectoration/hematemesis, or a convincing sentinel bleed after tonsillectomy is an airway-and-hemorrhage problem, not routine postoperative pain. Keep the patient NPO, position to permit suction and avoid aspiration when clinically feasible, obtain large-bore IV access, assess hemodynamics and blood loss, send CBC/type-and-screen or crossmatch and coagulation studies when the presentation warrants them, and involve ENT plus experienced anesthesia/OR support early. Children may swallow substantial blood before external loss appears; a deceptively normal initial hemoglobin does not exclude important acute hemorrhage.",
    "ACTIVE/MAJOR BLEED RESCUE: ongoing brisk bleeding, hemodynamic compromise, recurrent significant hemorrhage, or a concerning tonsillar-fossa clot requires a low threshold for operative control after simultaneous resuscitation. Anticipate a blood-contaminated/full stomach and a difficult shared-airway induction. In the OR, obtain exposure and suction clot enough to identify the actual bleeding point; use targeted bipolar/monopolar cautery, pressure/topical hemostasis or suture ligation as anatomy and surgeon judgment dictate. Do not substitute blind deep lateral cautery or clamping for visualization, particularly in the inferior/lateral fossa where major vessels may be at risk. After control, irrigate, release suspension briefly and re-inspect both fossae under physiologic conditions before leaving the OR.",
    "ADJUNCT/BAILOUT LOGIC: nebulized/topical/systemic tranexamic acid can be a useful temporizing or protocolized adjunct in selected post-tonsillectomy hemorrhage patients, and recent evidence suggests reduced reoperation, but it must not delay airway protection, resuscitation or definitive operative source control in an unstable or persistently bleeding patient. Recurrent delayed episodes of sudden gushing arterial hemorrhage, especially after prior apparently adequate operative control, should raise concern for an external-carotid branch pseudoaneurysm or other vascular lesion; once stabilized, escalate to CTA/angiography and neurointerventional/vascular expertise when the bleeding pattern warrants it rather than repeatedly cauterizing an unproven source.",
]


def _norm(value):
    return " ".join(str(value or "").lower().replace("-", " ").split())


def _match(slug, op):
    text = _norm(str(slug) + " " + str((op or {}).get("title", "")))
    if "lingual tonsil" in text:
        return False
    return any(term in text for term in ("tonsillectomy", "adenotonsillectomy", "tonsillectomy and adenoidectomy"))


def _append_unique(values, additions):
    out = list(values or [])
    changed = False
    for text in additions:
        marker = _norm(text[:72])
        if not any(marker in _norm(existing) for existing in out):
            out.append(text)
            changed = True
    return out, changed


def apply_or_tonsil_hemorrhage_rescue_v281(registry):
    patched = []
    for slug, op in (registry or {}).items():
        if not _match(slug, op):
            continue
        op["postop"], changed = _append_unique(op.get("postop"), POSTOP)
        op["source_basis"] = list(dict.fromkeys(list(op.get("source_basis") or []) + SOURCES))
        op["tonsil_hemorrhage_rescue_v281"] = True
        patched.append({"slug": slug, "changed": changed})
    return {"patched": patched, "count": len(patched)}
