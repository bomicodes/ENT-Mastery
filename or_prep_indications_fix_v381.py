"""v38.1: Replace exact generic OR-prep indication placeholders with procedure-specific criteria.

Only changes entries that still match the original placeholder. The ACI Alliance
60/60 referral guideline and FDA-expanded Inspire labeling are distinguished from
implant candidacy and insurance coverage, respectively.
"""

GENERIC_PLACEHOLDER = (
    "Use for appropriately selected disease after diagnosis, alternatives "
    "and patient-specific risk have been reviewed."
)

INDICATIONS_BY_SLUG = {
    "stapedotomy": (
        "Otosclerosis (or other fixed-stapes disease) causing conductive or mixed hearing "
        "loss with an air-bone gap, a Rinne/Weber pattern consistent with conductive "
        "pathology, and audiometric confirmation (classically a Carhart notch at 2 kHz on "
        "bone conduction). Generally offered after informed discussion of hearing-aid "
        "alternatives, in a patient with adequate cochlear reserve and no active middle-ear "
        "infection; bilateral disease is staged, operating the worse or more symptomatic ear "
        "first."
    ),
    "cochlear-implant": (
        "Sensorineural hearing loss with insufficient benefit from appropriately fitted "
        "hearing aids; assess each ear individually, including asymmetric hearing loss and "
        "single-sided deafness rather than restricting evaluation to bilateral profound loss. "
        "The ACI Alliance revised 60/60 guideline is a REFERRAL screen, not an implantation "
        "requirement: refer when the same ear has an unaided pure-tone average (500, 1000, "
        "2000 Hz) >=60 dB HL AND unaided monosyllabic word recognition <=60%; refer for "
        "formal evaluation whenever aided benefit is limited even if the screen is not met. "
        "The implant center performs optimized-aid, ear-specific speech testing and applies "
        "device, age and payer criteria. Medicare's expanded adult coverage uses <=60% "
        "best-aided open-set sentence recognition in the relevant coverage population; "
        "this is not interchangeable with the unaided 60/60 referral screen. Pediatric "
        "candidacy follows development, functional benefit and applicable device criteria."
    ),
    "neck-dissection": (
        "A clinically or radiographically node-positive neck (therapeutic dissection), or an "
        "N0 neck with occult-metastasis risk high enough to warrant elective treatment "
        "(commonly cited threshold: roughly >=15-20% occult nodal risk, e.g. oral cavity SCC "
        "with depth of invasion >=4 mm). Selective dissection preserves the nodal level(s) at "
        "low risk for the specific primary site and preserves the SCM, internal jugular vein "
        "and spinal accessory nerve when not directly involved by tumor."
    ),
    "total-laryngectomy": (
        "T4a laryngeal or hypopharyngeal squamous cell carcinoma with cartilage invasion or "
        "extralaryngeal extension not amenable to organ-preservation therapy; laryngeal "
        "cancer that has failed or recurred after chemoradiation (salvage laryngectomy); or a "
        "non-functional larynx with chronic aspiration/airway compromise even without active "
        "malignancy. Organ-preservation chemoradiation (see RTOG 91-11 framework) may be "
        "considered when function can be preserved without compromising oncologic control; "
        "high-volume T4a disease was not represented in the pivotal preservation trial."
    ),
    "submandibular-gland": (
        "Recurrent obstructive sialadenitis or sialolithiasis refractory to conservative "
        "management or sialendoscopic stone retrieval/duct treatment, chronic obstructive "
        "gland disease, or a suspected/confirmed neoplasm of the submandibular gland. A "
        "suspected malignancy shifts planning toward oncologic margins and neck management "
        "rather than routine inflammatory-disease excision."
    ),
    "sialendoscopy": (
        "Recurrent obstructive sialadenitis from ductal stones (most reliably retrievable when "
        "roughly <=4 mm, though larger stones can sometimes be managed with combined/" 
        "lithotripsy approaches) or ductal strictures, in a patient who does not yet need or "
        "want gland excision. Also used diagnostically for unexplained recurrent gland "
        "swelling when imaging is inconclusive."
    ),
    "DLB": (
        "Diagnostic evaluation of a laryngeal or airway abnormality beyond what awake flexible "
        "exam can characterize -- unexplained persistent hoarseness/dysphonia, a visualized or "
        "suspected laryngeal lesion needing biopsy, stridor or a suspected airway lesion, or "
        "suspected aerodigestive foreign body. Also used therapeutically (lesion excision, "
        "balloon/rigid dilation of stenosis) when direct instrumentation is required."
    ),
    "airway-dilation": (
        "Symptomatic subglottic or tracheal stenosis (commonly Myer-Cotton grade II-III, "
        "roughly 51-99% narrowing) causing exertional dyspnea or stridor, used either as "
        "primary treatment for short/soft immature stenosis or as a temporizing/bridge measure "
        "before a planned definitive open reconstruction."
    ),
    "medialization": (
        "Unilateral vocal fold paralysis or severe paresis with glottic insufficiency causing "
        "breathy dysphonia and/or aspiration. Voice therapy and early temporary injection "
        "augmentation can improve voice or swallowing when neural recovery is possible; "
        "permanent framework medialization may be considered based on etiology, prognosis "
        "and patient goals rather than enforcing a universal 6-12 month delay. Earlier "
        "definitive treatment is reasonable for known irreversible injury; clinically "
        "important aspiration warrants prompt intervention."
    ),
    "zenker": (
        "Symptomatic Zenker diverticulum -- dysphagia, regurgitation of undigested food, "
        "aspiration risk, or halitosis -- generally with a pouch large enough (commonly cited "
        "threshold roughly >=2-3 cm) to allow safe endoscopic stapling, laser, or "
        "harmonic-scalpel septotomy access; very small pouches or unfavorable anatomy may "
        "favor an open approach instead."
    ),
    "tonsillectomy": (
        "Recurrent acute tonsillitis meeting frequency criteria (classically Paradise "
        "criteria: >=7 episodes in 1 year, >=5/year for 2 consecutive years, or >=3/year for 3 "
        "consecutive years), obstructive sleep-disordered breathing/OSA with tonsillar "
        "hypertrophy, recurrent peritonsillar abscess, suspected malignancy, or clinically "
        "significant tonsillar asymmetry when accompanied by concerning findings."
    ),
    "adenoidectomy": (
        "Adenoid hypertrophy causing nasal obstruction or contributing to obstructive sleep "
        "apnea, chronic adenoiditis, recurrent otitis media with effusion as an adjunct to "
        "tympanostomy tube placement (particularly in children over about 4 years old or with "
        "recurrent disease after a first tube set), or chronic rhinosinusitis unresponsive to "
        "medical therapy where the adenoid acts as an inflammatory/bacterial reservoir."
    ),
    "thyroglossal": (
        "A confirmed thyroglossal duct cyst, after ultrasound (and thyroid function testing "
        "when relevant) has excluded the possibility that the cyst represents the patient's "
        "only functioning thyroid tissue. Generally offered even when currently asymptomatic "
        "because of recurrent-infection risk and a small but real risk of thyroglossal duct "
        "carcinoma, and definitively for recurrent infection or growth."
    ),
    "branchial": (
        "A confirmed branchial cleft cyst, sinus, or fistula with recurrent infection, "
        "cosmetic concern, or diagnostic uncertainty about a lateral neck mass. In adults, "
        "exclude a cystic metastatic lymph node, particularly HPV-associated oropharyngeal "
        "carcinoma, before presuming a congenital branchial cyst. Elective excision is "
        "generally deferred until any acute infection has resolved."
    ),
    "orbital-floor": (
        "Orbital floor fracture with true entrapment (positive forced duction testing, "
        "diplopia in primary or reading gaze that does not improve), enophthalmos greater than "
        "roughly 2 mm, or a large floor defect (commonly cited threshold roughly >50% of the "
        "floor or >2 cm^2) that risks late enophthalmos. A pediatric 'trapdoor' fracture with "
        "oculocardiac reflex (bradycardia, nausea, vomiting with globe/gaze restriction) is a "
        "surgical emergency regardless of the radiographic defect size."
    ),
    "mandible-orif": (
        "A displaced or mobile mandible fracture causing malocclusion, an unstable fracture "
        "pattern, a condylar fracture with malocclusion or significantly limited mandibular "
        "range of motion, or comminution requiring formal reduction and fixation rather than "
        "observation or closed treatment alone."
    ),
    "zmc-orif": (
        "A displaced zygomaticomaxillary complex fracture producing a functional deficit "
        "(trismus from coronoid/temporalis impingement, diplopia, enophthalmos) or a clinically "
        "significant cosmetic deformity (malar flattening/asymmetry), generally confirmed with "
        "CT to define the degree of displacement and comminution before committing to an "
        "approach."
    ),
    "hypoglossal-stimulator": (
        "Adult moderate-to-severe obstructive sleep apnea (Inspire FDA-expanded AHI 15-100) "
        "with documented PAP failure or intolerance, appropriate anatomy without complete "
        "concentric soft-palate collapse on drug-induced sleep endoscopy (DISE), and acceptable "
        "central/mixed apnea burden. FDA-expanded labeling increased the recommended BMI upper "
        "limit to 40, although payer/program thresholds may be more restrictive. Evaluate "
        "device-specific eligibility and coverage rather than using the older AHI 15-65 limit."
    ),
}


def apply_or_prep_indications_fix_v381(registry):
    """Replace exact placeholders without overwriting manually edited content."""
    if not registry:
        raise RuntimeError("v38.1: OR_PREP_REGISTRY not found")
    patched = []
    skipped_already_edited = []
    missing_slugs = []
    for slug, new_text in INDICATIONS_BY_SLUG.items():
        entry = registry.get(slug)
        if entry is None:
            missing_slugs.append(slug)
            continue
        current = (entry.get("indications") or "").strip()
        if current == GENERIC_PLACEHOLDER:
            entry["indications"] = new_text
            patched.append(entry.get("title", slug))
        elif current == new_text:
            pass
        else:
            skipped_already_edited.append(entry.get("title", slug))
    if missing_slugs:
        raise RuntimeError(f"v38.1: expected OR-prep slug(s) not found: {missing_slugs}")
    return {"patched": patched, "count": len(patched),
            "skipped_already_edited": skipped_already_edited}
