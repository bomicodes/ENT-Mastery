"""v35.6 — align odontogenic/unilateral depth to the exact live canonical rows.

v35.5 correctly deepened the CRSsNP differential, but the strict 42-topic Rhinology
inventory already contains dedicated canonical cards for ``Odontogenic Sinusitis`` and
``Unilateral Sinonasal Disease``.  This bounded pass reuses the durable v35.5 teaching in
those exact rows and adds only row-specific foundation -> application -> senior-decision
depth.  It does not add, rename, or remove a canonical topic.

Textbook anchors: Cummings Otolaryngology—Head and Neck Surgery 7e, K.J. Lee's
Essential Otolaryngology 12e, and Pasha Clinical Reference Guide 6e. Contemporary ODS
decisions are cross-checked against multidisciplinary consensus literature; imaging of a
suspected sinonasal mass is cross-checked against the current ACR Appropriateness Criteria.
"""

DOMAIN = "Rhinology / Allergy / Skull Base"
TARGET_TOPICS = ("Odontogenic Sinusitis", "Unilateral Sinonasal Disease")

COMMON_SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7e — rhinosinusitis differential, odontogenic source recognition, CT/endoscopic evaluation, sinonasal tumor and ESS principles",
    "K.J. Lee's Essential Otolaryngology, 12e — Chronic Rhinosinusitis; Diseases of the Nasal Cavity; Tumors of the Paranasal Sinuses",
    "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — Paranasal Sinus Disease; unilateral nasal mass/polyp differential; sinonasal evaluation",
]

ODS_SOURCES = [
    "Craig JR et al. Diagnosing odontogenic sinusitis: an international multidisciplinary consensus statement. Int Forum Allergy Rhinol. 2021;11(8):1235-1248. PMID 33583151. doi:10.1002/alr.22777 — ENT confirmation of sinusitis plus dental confirmation of causal odontogenic pathology",
    "Craig JR et al. Management of odontogenic sinusitis: multidisciplinary consensus statement. Int Forum Allergy Rhinol. 2020;10(7):901-912. PMID 32506807. doi:10.1002/alr.22598 — shared ENT/dental/patient decision-making and individualized treatment strategy",
    "Lin J et al. Expert consensus on odontogenic maxillary sinusitis multi-disciplinary treatment. Int J Oral Sci. 2024;16:11. doi:10.1038/s41368-024-00278-z — multidisciplinary source control and individualized dental/ESS sequencing",
    "Craig JR, Saibene AM, Felisati G. Sinusitis Management in Odontogenic Sinusitis. Otolaryngol Clin North Am. 2024;57(6):1157-1171. PMID 39428206. doi:10.1016/j.otc.2024.06.012 — management by complication status, treatable dental pathology, and symptom burden",
]

UNILATERAL_SOURCES = [
    "American College of Radiology. ACR Appropriateness Criteria: Sinonasal Disease — suspected sinonasal mass: MRI orbits/face/neck with and without contrast and CT maxillofacial are usually appropriate initial imaging options",
]

ODS_RECOGNIZE = (
    " FOUNDATION — ODONTOGENIC SINUSITIS: treat ODS as sinusitis causally linked to adjacent dental pathology or an iatrogenic dental process, not as ordinary inflammatory CRS with an incidental tooth finding. "
    "A unilateral maxillary-centered pattern, unilateral middle-meatal purulence, foul smell/taste, prior endodontic work, extraction, implant/sinus-lift, oroantral communication/fistula, or periapical/periodontal disease should raise suspicion; dental pain can be absent and disease can extend beyond the maxillary sinus."
)

ODS_WORKUP = (
    " APPLICATION: take a targeted dental/procedural history and perform nasal endoscopy to confirm the sinonasal inflammatory component. Review sinus CT with the teeth and sinus floor deliberately in view—looking for periapical disease, periodontal bone loss, displaced material, implant violation, or an oroantral pathway—and obtain dental examination/imaging when a source is suspected. "
    "Use the multidisciplinary diagnostic rule: ENT confirms sinusitis; a dental provider confirms the causal maxillary odontogenic pathology. Neither unilateral opacification alone nor an incidental dental abnormality proves causality."
)

ODS_MANAGE = (
    " SENIOR DECISION: manage the infectious dental source and the purulent sinus disease as linked problems. Repeated antibiotics are not definitive source control while treatable dental pathology, a foreign body, or an oroantral fistula persists. "
    "Use shared ENT/dental/patient decision-making: some uncomplicated patients improve after dental source treatment, while substantial sinus symptom burden, obstructed drainage, persistent disease, complications, or selected implant/foreign-body scenarios can justify ESS plus dental treatment. Do not teach a universal dental-first or ESS-first sequence; sequence and extent depend on the dental lesion, sinus burden, complication status, anatomy, and patient priorities."
)

ODS_OPERATE = (
    " OPERATIVE APPLICATION: when ESS is indicated, create adequate drainage and access for clearance/surveillance without implying that sinus surgery eradicates unresolved dental pathology. Coordinate management of displaced dental material and closure of persistent oroantral communication/fistula with dental/oral surgery when appropriate. "
    "Extrasinus orbital or intracranial spread converts the problem to urgent complicated sinusitis/source control rather than elective sequencing."
)

ODS_TEACH = (
    " Senior pearl: unilateral maxillary disease is a trigger to look for ODS, not proof of ODS. Confirm both halves of the diagnosis, control the source, and individualize dental treatment versus ESS timing. If the unilateral process is destructive, necrotic, bloody, mass-like, neurologically progressive, or otherwise atypical, reopen neoplasm, invasive fungal disease, and orbital/intracranial complication instead of forcing an odontogenic label."
)

UNI_RECOGNIZE = (
    " FOUNDATION — UNILATERAL SINONASAL DISEASE: unilateral disease is a diagnostic phenotype, not a diagnosis. Keep odontogenic disease, fungal ball/invasive fungal disease, benign tumor (including papilloma), malignancy, foreign body/local obstruction, and—when anatomy or history suggests it—skull-base/CSF or vascular pathology in the differential rather than defaulting to routine bilateral inflammatory CRS logic."
)

UNI_WORKUP = (
    " APPLICATION: deliberately ask about epistaxis, foul smell, dental disease/procedures, immunocompromise, facial numbness, vision change, proptosis, cranial neuropathy, severe focal pain, prior surgery/trauma, and clear positional rhinorrhea. Perform nasal endoscopy and obtain CT to define sinus of origin, dentition, calcification/hyperdensity, remodeling versus destructive bone change, and skull-base/orbital relationships. "
    "For a suspected sinonasal mass or concern for skull-base, orbital, intracranial, or perineural extension, add contrast-enhanced MRI for soft-tissue mapping rather than relying on CT alone."
)

UNI_MANAGE = (
    " SENIOR DECISION: route management to the cause instead of treating 'unilateral disease' as one entity. Odontogenic disease needs dual ENT/dental confirmation and source control; fungal disease follows noninvasive versus invasive pathways; a persistent unilateral mass/polyp needs tumor-level evaluation; CSF or vascular concern requires skull-base/vascular-safe planning. "
    "Do not repeatedly prescribe empiric CRS therapy when unilateral red flags or objective focal pathology demand tissue diagnosis or disease-specific treatment."
)

UNI_OPERATE = (
    " SAFE-TISSUE / BAILOUT RULE: before reflexively biopsying a unilateral lesion, review imaging and anatomy for features suggesting vascular pathology or intracranial/skull-base continuity, where an office biopsy could be dangerous. When tissue is appropriate, plan it so pathology can answer the actual differential. "
    "Escalate urgently for necrosis in an at-risk host, orbital findings, cranial neuropathy, major epistaxis, or intracranial signs; these findings override routine elective sinus sequencing."
)

UNI_TEACH = (
    " Senior unilateral rule: asymmetry should widen the differential before it narrows it. Endoscopy + CT localize the process; dental assessment confirms suspected dental causality; MRI adds soft-tissue/skull-base/orbital/perineural definition when a mass or extension is suspected. The bailout is to stop before unsafe biopsy or routine CRS treatment when vascular, intracranial, invasive-fungal, orbital, or malignant disease remains plausible."
)


def _append(row, field, text):
    existing = str(row.get(field) or "")
    if text not in existing:
        row[field] = existing + text


def _add_sources(row, extra):
    sources = list(row.get("source_basis") or [])
    for source in COMMON_SOURCES + extra:
        if source not in sources:
            sources.append(source)
    row["source_basis"] = sources


def apply_rhinology_exact_odontogenic_unilateral_v356(data_module, app_module=None):
    rows = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, []) or []
    by_topic = {str(r.get("topic") or ""): r for r in rows}
    if len(rows) != 42 or len(by_topic) != 42:
        raise RuntimeError(f"v35.6 requires the exact 42-topic Rhinology inventory; got rows={len(rows)} unique={len(by_topic)}")
    missing = [topic for topic in TARGET_TOPICS if topic not in by_topic]
    if missing:
        raise RuntimeError(f"v35.6 missing exact canonical target(s): {missing}")

    patched = []

    ods = by_topic["Odontogenic Sinusitis"]
    if not ods.get("source_grounded_v356"):
        _append(ods, "recognize", ODS_RECOGNIZE)
        _append(ods, "workup", ODS_WORKUP)
        _append(ods, "manage", ODS_MANAGE)
        _append(ods, "operate", ODS_OPERATE)
        _append(ods, "teach", ODS_TEACH)
        _add_sources(ods, ODS_SOURCES)
        ods["source_grounded_v356"] = True
        ods["deliberate_review_v356"] = {
            "foundation": "ODS is a causal dental-source sinusitis phenotype; unilateral maxillary disease is a suspicion trigger, not proof",
            "application": "ENT confirms sinusitis and dental evaluation confirms causal odontogenic pathology using endoscopy plus CT/dental assessment",
            "senior_decision": "source control plus individualized dental/ESS sequencing with complicated-disease and atypical-unilateral bailout",
        }
        patched.append("Odontogenic Sinusitis")

    unilateral = by_topic["Unilateral Sinonasal Disease"]
    if not unilateral.get("source_grounded_v356"):
        _append(unilateral, "recognize", UNI_RECOGNIZE)
        _append(unilateral, "workup", UNI_WORKUP)
        _append(unilateral, "manage", UNI_MANAGE)
        _append(unilateral, "operate", UNI_OPERATE)
        _append(unilateral, "teach", UNI_TEACH)
        _add_sources(unilateral, UNILATERAL_SOURCES)
        unilateral["source_grounded_v356"] = True
        unilateral["deliberate_review_v356"] = {
            "foundation": "unilateral disease is a phenotype requiring a broad focal-source, fungal, neoplastic, skull-base and vascular differential",
            "application": "endoscopy and CT localize; dental assessment and contrast MRI are added when their specific diagnostic questions are present",
            "senior_decision": "cause-directed care with an explicit unsafe-biopsy, invasive-fungal, orbital, neurologic and intracranial bailout",
        }
        patched.append("Unilateral Sinonasal Disease")

    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6

    return {
        "patched": patched,
        "canonical_ids": {topic: data_module._v6_item_id(DOMAIN, topic) for topic in TARGET_TOPICS},
    }
