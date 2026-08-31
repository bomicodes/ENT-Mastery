"""v33.3 — source-grounded pediatric otitis-media versus tympanostomy-candidacy rebuild.

AOM / OME / Tympanostomy Decisions owns disease-state diagnosis, longitudinal natural history,
hearing/development surveillance, and escalation. Tympanostomy Tube Indications assumes the
otitis phenotype is already established and teaches current guideline candidacy, counseling,
perioperative choices, and post-tube care.
"""

import re

FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


PEDS_OTITIS_REBUILD_V333 = {
    "aom ome tympanostomy decisions": {
        "recognize": (
            "Start by naming the MIDDLE-EAR STATE correctly. Acute otitis media (AOM) requires acute symptoms plus middle-ear effusion with inflammatory tympanic-membrane findings—classically moderate/severe bulging or new otorrhea not caused by otitis externa; a red TM alone is not AOM. Otitis media with effusion (OME) is fluid behind the TM WITHOUT acute infection. After AOM, an asymptomatic effusion can persist for weeks and should not be mislabeled treatment failure. Recurrent AOM is a longitudinal recurrence phenotype (classically >=3 well-documented episodes in 6 months or >=4 in 12 months with one in the preceding 6 months), but infection count alone does not determine tube candidacy."
        ),
        "localize": (
            "Localize the problem to ventilation/inflammation of the MIDDLE EAR and then define the consequence. Use pneumatic otoscopy to establish effusion; tympanometry is useful when the examination is uncertain, and audiology quantifies conductive hearing effect. AOM is an acute inflammatory event; OME is a persistent ventilation/effusion state. Look separately for structural sequelae—progressive retraction, atelectasis, ossicular erosion or cholesteatoma—and for higher-risk Eustachian-tube contexts such as cleft palate/craniofacial disorders or other developmental vulnerabilities. Those findings can change surveillance urgency even when the child is not acutely infected."
        ),
        "workup": (
            "Build a TIMELINE, not a diagnosis from one visit. For suspected recurrent AOM, verify that prior episodes actually met AOM criteria and document whether middle-ear effusion is present TODAY. For OME, establish onset/duration when possible; if effusion persists >=3 months, obtain age-appropriate hearing evaluation, or obtain hearing testing earlier when the child is becoming a surgical candidate or developmental concern is present. Identify children at increased risk for speech, language, or learning problems because of baseline sensory, physical, cognitive, behavioral, craniofacial, or developmental factors. Routine imaging is not part of uncomplicated AOM/OME; image when complications or another structural process are suspected."
        ),
        "manage": (
            "Manage the DISEASE STATE before jumping to tubes. Treat AOM pain and use observation versus antibiotics according to age, laterality, severity, follow-up reliability, recent antibiotic exposure and allergy; do not use chronic prophylactic antibiotics for recurrent AOM. For uncomplicated OME in a child who is not at increased developmental risk, watchful waiting for about 3 months is appropriate because most effusions resolve; antibiotics, antihistamines/decongestants, and systemic or intranasal steroids are not routine treatments for isolated OME. If chronic OME is observed without tubes, reassess every 3-6 months until it resolves, significant hearing loss appears, or structural TM/middle-ear abnormality is suspected."
        ),
        "operate": (
            "The operative handoff is: WHAT PHENOTYPE + WHAT CURRENT EAR STATUS + WHAT CONSEQUENCE? Chronic bilateral OME >=3 months with documented hearing difficulty is a guideline-supported tube pathway; chronic OME with attributable vestibular, school/behavioral, ear-discomfort or quality-of-life symptoms may also justify tubes. Recurrent AOM becomes a tube pathway only when unilateral or bilateral middle-ear effusion is present at the candidacy assessment. A child with recurrent AOM but NO effusion at that assessment should not receive tubes solely because the historical episode count is high. At-risk children with OME likely to persist deserve a lower threshold for intervention. The separate Tympanostomy Tube Indications card owns the exact candidacy and perioperative rules."
        ),
        "teach": (
            "Chief/boards framework: AOM = ACUTE INFECTION + EFFUSION; OME = EFFUSION WITHOUT ACUTE INFECTION. After AOM, persistent fluid does not equal persistent bacterial infection. For OME, the 3-MONTH CLOCK triggers hearing assessment and chronic-disease decisions. For recurrent AOM, the decisive surgical discriminator is not merely '3 in 6 or 4 in 12'—it is whether MIDDLE-EAR EFFUSION IS PRESENT when tube candidacy is assessed. This parent card follows disease over time; the tube card answers whether and how to ventilate surgically."
        ),
        "tags": ["acute otitis media", "AOM", "otitis media with effusion", "OME", "recurrent AOM", "pneumatic otoscopy", "tympanometry", "conductive hearing loss", "middle ear effusion", "pediatric otology"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — pediatric otitis media, Eustachian-tube physiology, middle-ear complications, and longitudinal hearing framework",
            "K.J. Lee's Essential Otolaryngology, 12e — AOM diagnostic/management framework; recurrent AOM definition; OME as effusion without acute inflammation; hearing and tube decision points",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — AOM diagnostic criteria and treatment; OME watchful waiting, at-risk children, and tube/adenoid framework",
            "AAO-HNSF Clinical Practice Guideline: Tympanostomy Tubes in Children (Update), 2022 — current OME duration, hearing, recurrent-AOM effusion, at-risk, surveillance, adenoid, and follow-up KASs",
            "AAO-HNSF Clinical Practice Guideline: Otitis Media with Effusion (Update), 2016 — OME diagnosis, natural history, watchful waiting, hearing/speech surveillance, and surgery framework",
            "AAP Clinical Practice Guideline: The Diagnosis and Management of Acute Otitis Media, 2013 — AOM diagnostic criteria, observation/antibiotic selection, and recurrent-AOM framework",
        ],
    },
    "tympanostomy tube indications": {
        "recognize": (
            "Use this card only after the otitis phenotype has been established. It is a CANDIDACY + COUNSELING module, not another AOM/OME overview. The first branch is duration/current ear status: do NOT place tubes for a single OME episode lasting <3 months; do NOT place tubes for recurrent AOM when neither ear has middle-ear effusion at the candidacy visit. Conversely, offer bilateral tubes for recurrent AOM when unilateral or bilateral effusion is present at that assessment, and offer bilateral tubes for bilateral OME >=3 months with documented hearing difficulty."
        ),
        "localize": (
            "Localize the REASON FOR VENTILATION. In chronic OME, the target is persistent middle-ear fluid and its hearing, developmental, vestibular, comfort, school-performance, quality-of-life, or structural consequence. In recurrent AOM, current effusion is evidence of ongoing Eustachian-tube/middle-ear disease that identifies the guideline-supported surgical phenotype. In an at-risk child, persistent OME may impose disproportionate communication/developmental cost. Do not convert every ear infection history, isolated type-C tympanogram, or transient post-AOM effusion into an operation."
        ),
        "workup": (
            "Before scheduling tubes, document the indication in the variables the guideline actually uses: OME duration, unilateral versus bilateral disease, hearing evaluation when OME is >=3 months or before surgery, attributable symptoms, developmental-risk status, recurrent-AOM history, and presence/absence of effusion at the candidacy examination. A type-B tympanogram or documented effusion >=3 months can support persistence in an at-risk child. Examine the TM for retraction/atelectasis or other structural disease and consider whether adenoid symptoms or age >=4 years change the operative plan. Long-term tubes are not routine first-line tubes unless prolonged ventilation is specifically anticipated."
        ),
        "manage": (
            "Use shared decision-making where the guideline gives an OPTION rather than pretending every chronic effusion mandates surgery. Tubes may be offered for unilateral or bilateral OME >=3 months with symptoms plausibly attributable to OME, and may be offered to at-risk children with OME likely to persist. If tubes are deferred in chronic OME, return to 3-6 month surveillance. Adenoidectomy may be added when there is a separate adenoid indication such as nasal obstruction/chronic adenoid infection, or in children >=4 years to reduce future recurrent otitis media or repeat tube placement; do not add adenoidectomy routinely to first-time tube placement in a younger child without an adenoid indication."
        ),
        "operate": (
            "For routine first placement, choose a short-term ventilation tube unless a specific reason predicts prolonged ventilation need. Counsel before surgery about expected tube duration, otorrhea, early extrusion, obstruction, granulation, tympanosclerosis and persistent perforation, plus the possibility of repeat tubes. After placement, the surgeon/designee should examine the ears within 3 months and continue periodic follow-up until extrusion. Do not routinely prescribe postoperative antibiotic ear drops and do not recommend routine prophylactic water precautions. For uncomplicated acute tympanostomy-tube otorrhea, use TOPICAL antibiotic ear drops without oral antibiotics."
        ),
        "teach": (
            "2022 AAO-HNSF boards grid: OME <3 months -> NO tube for that episode. OME >=3 months -> HEARING TEST. Bilateral OME >=3 months + hearing difficulty -> OFFER bilateral tubes. Chronic OME + attributable symptoms -> tubes are an OPTION. Recurrent AOM + NO effusion today -> NO tubes. Recurrent AOM + unilateral/bilateral effusion today -> OFFER bilateral tubes. At-risk child + OME likely to persist -> tubes are an OPTION. First post-tube ear exam is within 3 months; uncomplicated tube otorrhea gets topical drops alone; routine water precautions and routine postoperative antibiotic drops are not recommended."
        ),
        "tags": ["tympanostomy tubes", "PE tubes", "tube indications", "2022 AAO-HNSF", "chronic OME", "recurrent AOM", "middle ear effusion", "at-risk child", "tube otorrhea", "adenoidectomy"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — pediatric middle-ear ventilation, otitis-media surgery, complications, and hearing/development context",
            "K.J. Lee's Essential Otolaryngology, 12e — chronic OME, recurrent AOM, hearing loss, and tympanostomy concepts; current guideline supersedes older shorthand where recommendations differ",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — recurrent AOM with effusion, persistent OME, developmental-risk, adenoidectomy, and tube complication framework",
            "Rosenfeld et al., AAO-HNSF Clinical Practice Guideline: Tympanostomy Tubes in Children (Update), Otolaryngology–Head and Neck Surgery 2022;166(1_suppl):S1-S55 — current candidacy, perioperative counseling, otorrhea, water-precaution, adenoid and follow-up KASs",
        ],
    },
}


def apply_peds_otitis_rebuild_v333(data_module, app_module=None):
    patched = []
    for modules in (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).values():
        for module in modules or []:
            key = _norm(module.get("topic"))
            payload = PEDS_OTITIS_REBUILD_V333.get(key)
            if not payload:
                continue
            for field in FIELDS:
                module[field] = payload[field]
            module["tags"] = list(payload["tags"])
            module["source_basis"] = list(payload["source_basis"])
            module["source_grounded_v333"] = True
            module["semantic_role_v333"] = (
                "longitudinal AOM/OME disease-state diagnosis, hearing/development surveillance, and escalation"
                if key == "aom ome tympanostomy decisions"
                else "2022 AAO-HNSF tympanostomy candidacy, operative counseling, and post-tube care"
            )
            patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
