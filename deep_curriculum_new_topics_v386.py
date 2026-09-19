"""v38.6: Six-stage, source-grounded teaching for canalplasty and laryngeal trauma.

Clinical review: Operative Otolaryngology 3e, ch 8, explicitly favors exploration
within 24-48 h when condition permits; Pasha 6e, head/neck trauma, says ideally
repair within 2-3 days. A literature report of mean repair at 5.6 days (range
3-10) is NOT a recommended waiting period. The uploaded draft's universal
3-10-day directive has therefore been corrected. Percentages are identified
as study-specific, not patient-level guarantees. Both topic cards are
idempotently added and only legacy OR links are changed.
"""

CANALPLASTY_TOPIC = {
    "topic": "EAC Exostoses / Osteoma (Canalplasty)",
    "primary_domain": "Otology / Neurotology",
    "recognize": (
        "A patient with cold-water surfing or diving exposure has bilateral, multiple, smooth, broad-based bony prominences in the medial EAC: exostoses ('surfer's ear'). An EAC osteoma is usually a solitary, unilateral, discrete or pedunculated bony mass, often near a tympanosquamous or tympanomastoid suture; these are typical patterns, not absolute diagnostic rules. Both may be incidental. Symptoms arise when the canal loses its self-cleaning function: trapped water, recurrent otitis externa, retained cerumen or keratin, difficulty inspecting the tympanic membrane (TM), and sometimes conductive hearing loss. Do not assume every obstructing canal lesion is an exostosis: focal otalgia, otorrhea, exposed/eroded bone or disproportionate pain suggests EAC cholesteatoma; a soft-tissue mass, bleeding, ulceration, facial weakness or progressive unilateral lesion merits assessment for neoplasm. Keratosis obturans causes an obstructing keratin plug and usually concentric canal widening, whereas EAC cholesteatoma causes focal bone erosion. The distinction changes imaging, biopsy decisions, and the extent of surgery."
    ),
    "localize": (
        "Separate the lateral cartilaginous one-third of the EAC, with thick mobile skin and hair follicles, from the medial bony two-thirds, with thin tightly adherent skin that is critical to preserve. Identify the narrow isthmus, annulus and TM medially. The anterosuperior bony canal borders the glenoid fossa/TMJ; unintended entry causes joint exposure and possibly prolapse. The posterior-inferior MEDIAL canal wall approaches the mastoid facial nerve: its course is variable and can be lateral to the annular plane. Chorda tympani is vulnerable near the posterosuperior annulus and middle-ear entry. The ossicular chain, particularly malleus, is endangered by force or drilling near the TM. Broad-based exostoses can obscure these reference points entirely; never drill blindly toward a presumed TM, facial nerve, or joint. Maintain awareness of mastoid air cells posteriorly and the temporal-bone boundaries on CT when anatomy is uncertain."
    ),
    "workup": (
        "Document the history (cold-water exposure, infections, wax trapping, previous instrumentation, prior canal surgery, symptom burden and whether it is the only hearing ear), perform bilateral microscopic otoscopy with careful cleaning if safe, and describe site, number, morphology and estimated percentage of obstruction. Document whether the entire TM can be seen, any squamous debris, exposed bone or focal erosion, and the condition of canal skin. Obtain baseline pure-tone audiometry with air/bone thresholds when symptoms, significant stenosis or surgery are contemplated; a large conductive loss may have coexisting middle-ear pathology rather than being wholly due to an exostosis. Typical asymptomatic lesions need no routine imaging or biopsy. High-resolution CT temporal bone is useful for severe occlusion with hidden medial anatomy, concern for cholesteatoma/bony erosion or atypical tumor, revision surgery, and preoperative mapping near the facial nerve/TMJ; individualize rather than ordering CT for every surfer. Biopsy an atypical suspicious soft-tissue lesion when appropriate, not routine classic bony exostoses."
    ),
    "manage": (
        "Observe an asymptomatic patent canal; counsel cold-water exposure reduction and protective earplugs/hood use, and arrange cerumen care when needed. Treat concomitant otitis externa and maintain a dry, clean canal; explain that surgery is not justified by a CT percentage alone without symptoms or an important access/surveillance issue. Consider canalplasty/exostectomy for recurrent obstruction-related infections, persistent symptomatic trapping or impaction despite reasonable conservative care, attributable hearing loss, or inability to safely evaluate/manage the medial canal or TM; canal widening may also be required for access to a separate otologic procedure. For the only-hearing ear, explicitly discuss the small but consequential risk of iatrogenic sensorineural hearing loss. Compare osteotome versus drill with actual tradeoffs, not 'one is universally safer': a 2023 systematic review of 1,788 ears found pooled TM perforation 5.3% versus 3.8%, sensorineural loss 0.69% versus 4.3%, and restenosis 1.1% versus 4.1%, respectively; heterogeneity and nonrandomized studies limit causal comparison. These are published cohort estimates, not guaranteed individual probabilities."
    ),
    "operate": (
        "Plan microscopic/endoscopic transcanal, endaural or postauricular exposure according to stenosis, orientation, skin availability and surgeon experience. Confirm baseline hearing and CT landmarks when indicated, establish TM/annulus location if possible, and raise broad vascularized canal-skin flaps while minimizing tears. Protect the skin in the operative field with an appropriate barrier and adequate irrigation. Remove obstructing bone in controlled thin layers with drill and/or osteotome under direct vision; avoid transmitting osteotome force to the TM/ossicles, excessive heat/noise from drilling, and blind posteroinferior medial drilling near the facial nerve. Beware the anterior TMJ boundary and a hidden medial bony shelf that would perpetuate trapping. Repeatedly check the TM and canal caliber, smooth remaining ridges, preserve or graft epithelial coverage of exposed bone, and use appropriate packing to support skin apposition. Stop or change approach if landmarks are unsafe; additional exposure/CT-guided planning is safer than speculative drilling. Exit checks: visualize an intact TM and patent canal, inspect flap perfusion/coverage and exposed joint or mastoid, confirm hemostasis and packing plan, document any TM injury. Follow-up monitors epithelialization, infection, recurrent keratin trapping and restenosis, with hearing testing if indicated."
    ),
    "teach": (
        "BOARD DECISION: incidental smooth bilateral exostoses plus a patent, dry, self-cleaning canal -> observation, not prophylactic canalplasty. Recurrent water trapping/otitis externa, conductive loss or an unmonitorable TM -> consider surgery after workup and counseling. A solitary pedunculated mass favors osteoma; focal canal erosion/exposed bone is a different problem and warrants cholesteatoma or malignancy evaluation, often CT. In the OR, the high-stakes error is blind medial drilling: posterior-inferior = facial nerve, anterior = TMJ, medial = TM/ossicles; protect thin canal skin to prevent denuded bone and cicatricial stenosis. Never teach restenosis as a universal 4-10% risk: published cohorts vary by procedure, technique and follow-up. Ask a junior why a high air-bone gap despite limited canal obstruction requires a middle-ear differential and why a patient with the only hearing ear needs different counseling."
    ),
    "tags": ["canalplasty", "exostosis", "osteoma", "external auditory canal", "surfer's ear", "EAC cholesteatoma", "conductive hearing loss"],
    "source_basis": [
        "Pasha and Golub, Otolaryngology Head & Neck Surgery Clinical Reference Guide, 6e (2022), ch 7: EAC exostoses/osteoma and EAC cholesteatoma.",
        "Myers and Snyderman, Operative Otolaryngology--Head and Neck Surgery, 3e, external-ear section: medial EAC/annulus and facial nerve anatomy.",
        "Swisher et al. Ann Otol Rhinol Laryngol 2023;132:1249-1260, systematic review and meta-analysis (PMID 36635864): technique-dependent complication estimates.",
        "Outcomes of Drill Canalplasty in Exostoses and Osteoma, Otol Neurotol 2017 (PMID 27755370): 256 ears, 4% postoperative stenosis/prolonged healing in this cohort."
    ],
    "evidence_calibrated": "v38.6-review-2026"
}

LARYNGEAL_FRACTURE_TOPIC = {
    "topic": "Laryngeal Fracture / External Laryngeal Trauma",
    "primary_domain": "Facial Plastics / Trauma",
    "recognize": (
        "After anterior-neck impact (dashboard, sports collision, clothesline, assault/strangulation), or penetrating trauma, suspect an occult laryngotracheal injury with new dysphonia, odynophagia/dysphagia, hemoptysis, dyspnea, neck tenderness/crepitus, subcutaneous emphysema, a flattened thyroid prominence or palpable step-off. Hoarseness is common but symptom severity does NOT reliably grade structural injury; a patient speaking calmly may develop edema and obstruction over hours. Stridor, progressive dyspnea, expanding hematoma, inability to handle secretions, major emphysema or distortion mandates an immediately coordinated airway plan, not a trip to CT first. Assess cervical spine, possible carotid/jugular trauma and pharyngoesophageal perforation as part of multidisciplinary trauma care. Children have a higher, more flexible and less ossified larynx, which lowers obvious fracture frequency but does not exclude serious mucosal injury. A normal-appearing external neck is not a rule-out test."
    ),
    "localize": (
        "Map supraglottic (epiglottis, aryepiglottic structures), glottic (thyroid laminae, true folds, anterior commissure, arytenoids and cricoarytenoid joints), and subglottic/cricoid-tracheal injury. The cricoid is a complete ring, so fracture/hematoma can critically narrow the only airway. Schaefer-Fuhrman: I = minor mucosal edema/hematoma/laceration without significant structural disruption; II = greater edema/hematoma or minor mucosal injury, potentially a stable nondisplaced fracture and no exposed cartilage; III = massive edema, exposed cartilage or substantial laceration, displaced fracture or fold immobility; IV = severe unstable framework/multiple displaced fractures, major mucosal disruption or anterior-commissure avulsion; V = complete laryngotracheal separation. Grade combines endoscopic and CT findings, not radiology alone. Differentiate vocal fold immobility from arytenoid dislocation/cricoarytenoid fixation versus RLN injury; document anterior commissure and mucosal coverage because malrepair causes web/stenosis or dysphonia."
    ),
    "workup": (
        "FIRST assess airway, breathing and circulation with cervical-spine precautions and senior ENT/anesthesia/trauma support. An unstable or rapidly deteriorating airway should be secured by the team using the safest method before imaging; a controlled awake tracheostomy below the injury is often favored for clear major framework disruption. In a stable, cooperative patient, flexible nasolaryngoscopy assesses edema, blood, airway caliber, exposed cartilage, mucosal tears and bilateral vocal fold motion; a seemingly mild scope can miss a framework fracture. CT neck with thin cuts and multiplanar laryngeal reconstruction defines displaced/nondisplaced thyroid/cricoid fractures and associated injury once safe to image; do not impose a 24-hour wait or image a threatened airway. Add CTA neck when mechanism/findings indicate vascular injury and evaluate cervical spine. If deep laceration, air near esophagus, swallowing symptoms or penetrating trajectory raises suspicion, arrange esophagoscopy and/or contrast swallow as clinically indicated. After airway control, direct laryngoscopy/bronchoscopy with arytenoid palpation and esophagoscopy as appropriate delineate extent for repair. Serial bedside airway and flexible-endoscopic checks in monitored care are essential even in conservatively treated injury, typically at least 24 hours."
    ),
    "manage": (
        "Airway FIRST. Do not attempt routine blind rapid-sequence intubation across suspected severe disruption: it may create a false passage or complete separation. Choice among controlled fiberoptic intubation with immediate surgical backup and awake/local tracheostomy depends on anatomy, stability, expertise and associated injuries; with a clearly unstable framework or major separation, secure a surgical airway below injury when feasible. Group I and selected stable II injuries with intact mucosa, no significant displacement or airway compromise generally receive monitored admission, head elevation, humidification, voice rest, analgesia, swallowing assessment and serial endoscopy; steroids/antireflux therapy are adjuncts with variable evidence, not substitutes for airway vigilance. A group II patient with concerning mucosal/fracture findings can require direct endoscopy or exploration. Displaced fractures, exposed cartilage, large mucosal lacerations, anterior-commissure disruption, cricoarytenoid injury, persistent immobility, unstable airway or progressive emphysema require prompt operative assessment/repair. EXPEDITIOUS REPAIR is preferred when clinically feasible: Operative Otolaryngology recommends exploration within 24-48 hours and Pasha describes repair ideally within 2-3 days after stabilization; a published mean of 5.6 days (range 3-10) must not be misread as a required delay. Address immediately life-threatening injuries first and individualize timing."
    ),
    "operate": (
        "After a secure airway below any major disruption and associated trauma/cervical-spine planning, perform direct laryngoscopy plus bronchoscopy, and esophagoscopy if indicated, to map mucosal breaks, exposed cartilage, fold mobility, arytenoid joint integrity, anterior commissure and cricotracheal continuity. For displaced thyroid/cricoid fracture or major soft-tissue disruption, expose through a suitable cervical incision, preserve perichondrium and blood supply, gently reduce cartilage to anatomic contour, fix with appropriate miniplates/sutures or tailored mesh where necessary, repair mucosal lacerations to cover cartilage, restore anterior-commissure attachment and address arytenoid dislocation or vocal-fold avulsion. Stenting/keel is SELECTIVE for unstable comminution, extensive mucosal loss or commissure disruption, not automatic for every fracture; weigh granulation and later removal. Complete laryngotracheal separation is an airway catastrophe: identify distal trachea for secure ventilation, then reconstruct continuity when stabilized; coordinate with trauma/thoracic teams and assess RLN and esophageal injury. Exit checklist: patent secure airway/trach, intact mucosal cover, restored framework and commissure, no unrecognized esophageal or vascular injury, feeding/aspiration plan and staged repeat-endoscopy/stent follow-up. Early issues: airway edema, infection, hematoma, mucosal breakdown. Late: glottic/subglottic stenosis, web, dysphonia, dysphagia/aspiration, vocal fold immobility and decannulation failure."
    ),
    "teach": (
        "BOARD ALGORITHM: suspect after anterior neck trauma plus voice, breathing or swallowing change; do airway/c-spine evaluation BEFORE CT; stable -> flexible scope and CT framework mapping; threatened airway/separation -> expert controlled airway, usually surgical below disruption; then classify with Schaefer-Fuhrman I-V. Minor stable I/selected II -> observed with serial scope at least 24 h; major mucosal/cartilage instability or group III-V -> early operative evaluation, reconstruct cartilage, restore mucosa and anterior commissure, consider stent only when needed. Reiterate key timing correction: early reconstruction when safe (often within 24-48 h) is favored; NEVER teach waiting 3-10 days as the optimal standard. The most important discriminator is exposed cartilage/displacement/commissure or airway instability rather than isolated hoarseness. Attendings may ask why a normal CT does not rule out mucosal injury, how to recognize arytenoid dislocation versus nerve paralysis, why cricoid injury threatens circumferential airway caliber, and what short- and long-term evaluations are needed to preserve breathing, swallowing and voice."
    ),
    "tags": ["laryngeal fracture", "external laryngeal trauma", "Schaefer-Fuhrman", "neck trauma", "airway injury", "laryngotracheal separation", "laryngeal reconstruction"],
    "source_basis": [
        "Myers and Snyderman, Operative Otolaryngology--Head and Neck Surgery, 3e, ch 8 Laryngeal Trauma: early exploration within 24-48 h when feasible, airway and associated-injury planning.",
        "Pasha and Golub, Otolaryngology Head & Neck Surgery Clinical Reference Guide, 6e (2022), ch 10, pp 667-669: scope, CT, injury thresholds and repair ideally within 2-3 days.",
        "Schaefer-Fuhrman group descriptors and management: Rai and Anjum, Laryngeal Fracture, StatPearls (updated 2023), NCBI Bookshelf NBK562276; its retrospective 3-10-day series is descriptive, not a recommended wait.",
        "Review: Management of blunt and penetrating laryngeal trauma (PMID 36264298), early identification and surgery if needed within 24-48 h."
    ],
    "evidence_calibrated": "v38.6-review-2026"
}

OR_PREP_RELINK = {
    "canalplasty": ("canalplasty", CANALPLASTY_TOPIC["topic"]),
    "laryngeal-fracture": ("laryngeal-fracture", LARYNGEAL_FRACTURE_TOPIC["topic"]),
}


def apply_deep_curriculum_new_topics_v386(data_module, app_module=None):
    modules = data_module.DEEP_MODULES_V6
    registry = data_module.OR_PREP_REGISTRY
    missing = [slug for slug in OR_PREP_RELINK if slug not in registry]
    if missing:
        raise RuntimeError(f"v38.6: missing OR prep slugs: {missing}")
    added, relinked, relink_skipped = [], [], []
    for card in (CANALPLASTY_TOPIC, LARYNGEAL_FRACTURE_TOPIC):
        bucket = modules.setdefault(card["primary_domain"], [])
        if not any(x.get("topic") == card["topic"] for x in bucket):
            bucket.append(dict(card))
            added.append(card["topic"])
    for slug, (legacy, topic) in OR_PREP_RELINK.items():
        entry = registry[slug]
        current = (entry.get("linked_topic") or "").strip()
        if current == legacy:
            entry["linked_topic"] = topic
            relinked.append(slug)
        elif current != topic:
            relink_skipped.append(slug)
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = modules
        app_module.OR_PREP_REGISTRY = registry
    return {"topics_added": added, "relinked": relinked, "relink_skipped": relink_skipped}
