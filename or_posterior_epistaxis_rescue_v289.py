"""v28.9 posterior epistaxis / SPA control and escalation for OR Tomorrow.

Deepens the existing SPA-ligation card from branch awareness into an executable
resident/chief pathway for hemorrhage stabilization, endoscopic localization and
control, failure analysis, and selective endovascular escalation. Foundational nasal
vascular anatomy and operative principles remain grounded in Cummings 7e, K.J. Lee
12e, and Pasha 6e; evolving management is aligned with the AAO-HNSF Nosebleed CPG and
current surgical/endovascular outcome literature.
"""

POSTERIOR_EPISTAXIS_SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7th ed.",
    "K. J. Lee's Essential Otolaryngology: Head and Neck Surgery, 12th ed.",
    "Pasha: Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6th ed.",
    "Tunkel DE, Anne S, Payne SC, et al. Clinical Practice Guideline: Nosebleed (Epistaxis). Otolaryngol Head Neck Surg. 2020;162(1_suppl):S1-S38. doi:10.1177/0194599819890327.",
    "Kitamura T, Takenaka Y, Takeda K, et al. Management of uncontrolled/recurrent epistaxis by ligation or cauterization of the sphenopalatine artery: a scoping review. Eur Arch Otorhinolaryngol. 2024.",
    "Bonnici M, Orabi NA, Gannon M, et al. Complications and Outcomes of Endovascular Embolization for Intractable Epistaxis: A Systematic Review and Meta-analysis. Ann Otol Rhinol Laryngol. 2023;132(10):1233-1248. doi:10.1177/00034894221143187.",
    "Simmen DB, Raghavan U, Briner HR, et al. The anatomy of the sphenopalatine artery for the endoscopic sinus surgeon. Am J Rhinol. 2006;20(5):502-505.",
]

TARGET = {
    "slug": "spa-ligation",
    "title_terms": ("sphenopalatine", "artery"),
}

STABILIZE = (
    "For brisk posterior epistaxis, treat airway and circulation before chasing the vessel: sit the patient forward when feasible, maintain large-bore suction, secure IV access, quantify ongoing blood loss and activate transfusion/resuscitation when physiology warrants. Packing or a balloon can be a temporizing bridge, but continued hemorrhage into the pharynx, hemodynamic instability, aspiration risk, or repeated packing failure is a commitment point for definitive control rather than serial blind repacking. Coordinate anesthesia early when blood in the pharynx, agitation, hypoxemia or anticipated operative control makes airway protection difficult."
)

EXPOSURE = (
    "For endoscopic SPA control, decongest and clear clot until the posterior lateral nasal wall is visible; elevate the mucoperiosteal flap in the posterior middle meatus and use the crista ethmoidalis as the practical landmark just anterior to the sphenopalatine foramen. Expose far enough posteriorly and superior/inferiorly to identify the arterial branches rather than cauterizing one apparent trunk through a narrow window. Multiple branches and accessory foramina are common, so complete control requires deliberate inspection for additional posterior nasal/SPA branches before the flap is replaced."
)

FAILURE = (
    "If bleeding persists or recurs after apparently adequate SPA control, stop assuming the same branch is the source. Re-clear the field and reassess for a missed SPA/posterior nasal branch, contralateral supply, septal source, anterior or posterior ethmoidal contribution, tumor/vascular lesion, or an iatrogenic pseudoaneurysm. A superior source near the roof or bleeding pattern inconsistent with the SPA territory should redirect the operation rather than provoke deeper blind cautery around the skull base or orbit."
)

ESCALATION = (
    "Persistent or recurrent bleeding not controlled by packing/cautery should prompt explicit selection between further surgical arterial control and endovascular embolization based on source localization, hemodynamic stability, prior surgery, comorbidity, anatomy and immediately available expertise; neither modality should be taught as universally mandatory before the other. If embolization is chosen, angiography must account for dangerous external-to-internal carotid and ophthalmic anastomoses because non-target embolization can cause stroke, blindness or tissue necrosis. Suspected internal-carotid injury, pseudoaneurysm or bleeding after skull-base/transsphenoidal surgery is a different major-vessel pathway: use temporizing tamponade/resuscitation and urgent neurointerventional/skull-base escalation rather than blind deep clipping or cautery."
)

POSTOP = (
    "After definitive posterior epistaxis control, observe for recurrent fresh bleeding, posterior pharyngeal blood, aspiration/airway compromise and hemodynamic or hemoglobin trajectory according to the severity of the original hemorrhage. New neurologic deficit, visual change, facial/palatal ischemia or severe focal pain after embolization is not routine recovery and requires urgent neurovascular assessment for non-target ischemic complication."
)


def _resolve(registry, target):
    reg = registry or {}
    if target["slug"] in reg:
        return target["slug"], reg[target["slug"]]
    for slug, op in reg.items():
        hay = (str(slug) + " " + str((op or {}).get("title", ""))).lower()
        if all(term in hay for term in target["title_terms"]):
            return slug, op
    return None, None


def _prepend_unique(values, additions):
    out = list(values or [])
    changed = False
    for text in reversed(additions):
        marker = text[:80].lower()
        if not any(marker in str(x).lower() for x in out):
            out.insert(0, text)
            changed = True
    return out, changed


def _append_unique(values, additions):
    out = list(values or [])
    known = {str(x).strip().lower() for x in out}
    changed = False
    for text in additions:
        key = str(text).strip().lower()
        if key and key not in known:
            out.append(text)
            known.add(key)
            changed = True
    return out, changed


def apply_or_posterior_epistaxis_rescue_v289(registry):
    slug, op = _resolve(registry, TARGET)
    if not op:
        return {"changed": [], "count": 0, "resolved": [], "missing": [TARGET["slug"]]}
    op["setup"], c1 = _prepend_unique(op.get("setup"), [STABILIZE])
    op["steps"], c2 = _prepend_unique(op.get("steps"), [EXPOSURE, FAILURE, ESCALATION])
    op["postop"], c3 = _prepend_unique(op.get("postop"), [POSTOP])
    op["sources"], c4 = _append_unique(op.get("sources"), POSTERIOR_EPISTAXIS_SOURCES)
    op["posterior_epistaxis_rescue_v289"] = True
    changed = [slug] if any((c1, c2, c3, c4)) else []
    return {"changed": changed, "count": len(changed), "resolved": [slug], "missing": []}
