"""v39.6 -- Head & Neck Oncology depth repair (content-staleness sweep, batch 7/9).

Same two defects as prior batches. See thyroglossal_duct_cyst_depth_v389
for the pattern and rationale.
"""

DOMAIN = "Head & Neck Oncology"

DEPTH_V396 = {
    "Floor of Mouth SCC": {
        "recognize": (
            "Floor-of-mouth mucosa is thin and lies directly against the mandible, submandibular "
            "(Wharton's) ducts, and lingual/hypoglossal nerves, so even a modest-appearing lesion can "
            "have already reached these structures; a non-healing ulcer, induration, or pain out of "
            "proportion to visible size should raise concern regardless of lesion diameter."
        ),
        "localize": (
            "Anterior floor-of-mouth lesions risk early mandibular periosteal/bone contact and duct "
            "involvement; posterior/lateral lesions risk lingual nerve and deep tongue musculature "
            "invasion. Proximity to the mandible on exam or imaging is not the same as true bony "
            "invasion -- cortical erosion on imaging, fixation to bone on exam, or intraoperative "
            "findings are what confirm invasion, not adjacency alone."
        ),
        "operate": (
            "Indication: biopsy-confirmed floor-of-mouth SCC. Setup: transoral resection for "
            "accessible early-stage disease, with mandibulotomy or other approaches reserved for "
            "larger/posteriorly extending tumors; neck dissection is performed for the clinically or "
            "radiographically at-risk neck, and often electively even in a clinically negative neck "
            "given the floor of mouth's occult metastasis rate. Key steps: obtain adequate 3-D "
            "margins (deep margin is often the limiting one in floor-of-mouth resection), assess the "
            "mandible intraoperatively when adjacency was noted preoperatively (marginal vs segmental "
            "mandibulectomy depending on whether true invasion is confirmed), and reconstruct the "
            "resulting defect (local flap, free flap) matched to defect size and functional need "
            "(tongue mobility, swallowing). Danger structures: lingual and hypoglossal nerves, "
            "lingual artery, submandibular duct, and the mandible itself. Failure mode: assuming "
            "mandibular invasion from radiographic or clinical proximity alone and performing an "
            "unnecessarily morbid segmental mandibulectomy, or conversely under-resecting a truly "
            "invaded mandible with a marginal resection alone. Postoperative plan: adjuvant "
            "radiation/chemoradiation per final pathology (margins, extranodal extension, "
            "perineural/lymphovascular invasion), and early involvement of speech/swallow therapy "
            "given the floor of mouth's central role in oral phase swallowing and articulation."
        ),
    },
    "Tonsil SCC": {
        "recognize": (
            "HPV-associated oropharyngeal SCC (tonsil being the most common subsite) frequently "
            "presents not as an obvious tonsil lesion but as a cystic-appearing neck mass, sometimes "
            "in a relatively young, non-smoking patient, with a primary tonsil lesion that can be "
            "small or clinically inapparent -- this pattern is different enough from classic "
            "smoking-associated head and neck cancer that it should not be dismissed as a benign "
            "branchial cleft cyst by demographics alone."
        ),
        "localize": (
            "Because a cystic neck mass in an adult has a meaningfully different differential than in "
            "a child (metastatic HPV-associated OPSCC must be actively excluded, not assumed benign), "
            "localization work starts with identifying the primary -- exam, imaging, and directed "
            "biopsy/tonsillectomy of the suspected side -- before the neck mass itself is approached "
            "surgically."
        ),
        "operate": (
            "Indication: biopsy- or FNA-confirmed tonsil SCC, or a cystic neck mass in an adult where "
            "metastatic OPSCC has not yet been excluded. Setup: for a cystic neck node of unclear "
            "origin, FNA (with HPV/p16 and EBV testing as appropriate) and directed search for a "
            "primary (exam, PET/CT, exam under anesthesia with diagnostic tonsillectomy) come before "
            "any open neck procedure. Key steps: primary treatment is transoral (robotic or laser) "
            "resection or definitive (chemo)radiation depending on stage/patient factors, with neck "
            "dissection or nodal irradiation addressing the nodal disease found on workup. Danger "
            "structures: for transoral tonsil resection, the internal carotid artery and lingual "
            "artery are within the deep dissection field. Failure mode: performing an open excisional "
            "biopsy of an adult cystic neck node before excluding metastatic OPSCC -- this can seed "
            "the surgical field, complicate future neck dissection planning, and delay correct "
            "diagnosis and staging. Postoperative plan: adjuvant treatment per final pathology "
            "(margins, extranodal extension), with HPV/p16 status now factored into prognosis and, in "
            "treatment de-intensification only in an appropriate clinical trial, not routine care."
        ),
    },
    "Hypopharyngeal Cancer": {
        "recognize": (
            "Hypopharyngeal SCC is often locally advanced at diagnosis because the pyriform "
            "sinus/hypopharynx has a large lumen that tolerates significant tumor growth before "
            "producing symptoms; dysphagia, weight loss, referred otalgia, or a neck mass from nodal "
            "disease are common presenting complaints, often at a stage well past what a patient with "
            "an early glottic cancer would present with."
        ),
        "localize": (
            "Subsites (pyriform sinus, postcricoid region, posterior pharyngeal wall) have different "
            "spread patterns and functional stakes -- postcricoid disease is closer to the "
            "cricopharyngeus and esophageal inlet, and disease here or in the pyriform apex more "
            "readily threatens laryngeal function and airway, which is central to planning organ-"
            "preservation versus laryngectomy-inclusive treatment."
        ),
        "operate": (
            "Indication: biopsy-confirmed hypopharyngeal SCC; because of typically advanced stage at "
            "diagnosis, multidisciplinary discussion of organ-preservation chemoradiation versus "
            "primary surgical resection (partial or total laryngopharyngectomy, depending on extent) "
            "with reconstruction is standard. Setup: full endoscopic evaluation under anesthesia to "
            "define true extent (often greater than seen on exam alone), and evaluation for "
            "synchronous second primary tumors, which occur at meaningfully higher rates in this "
            "population. Key steps: when surgery is chosen, resection margins must account for "
            "submucosal spread beyond visible tumor, and reconstruction (regional or free flap) is "
            "planned to restore a functional conduit for swallowing. Danger structures: carotid "
            "sheath contents posterolaterally, and the larynx itself when preservation is attempted. "
            "Failure mode: underestimating baseline nutritional and functional compromise -- many "
            "patients present with significant pre-treatment weight loss and dysphagia, which changes "
            "perioperative risk and the urgency/feasibility of a feeding tube before definitive "
            "treatment begins, and failing to look for a synchronous aerodigestive tract primary. "
            "Postoperative plan: aggressive nutritional support, swallowing rehabilitation, and "
            "adjuvant chemoradiation per final pathology, with close surveillance given this "
            "subsite's higher recurrence risk."
        ),
    },
    "Nasopharyngeal Carcinoma": {
        "recognize": (
            "Presenting signs reflect the nasopharynx's central skull-base location: a neck mass "
            "(often the presenting complaint), unilateral middle-ear effusion (from eustachian tube "
            "obstruction -- any new unilateral effusion in an adult should prompt nasopharyngeal "
            "evaluation), epistaxis/nasal obstruction, or cranial neuropathy from skull-base "
            "extension. Nonkeratinizing/undifferentiated histology is strongly associated with "
            "Epstein-Barr virus, particularly in endemic regions, which also informs surveillance "
            "(EBV DNA) and, in some cases, treatment."
        ),
        "localize": (
            "Local extension patterns follow skull-base foramina and adjacent spaces -- superiorly "
            "into the skull base and cavernous sinus (producing cranial neuropathies, especially "
            "CN V/VI), laterally into the parapharyngeal space, and via the eustachian tube orifice "
            "producing the classic unilateral effusion -- so imaging (MRI for skull-base/soft-tissue "
            "extent) is centered on these specific routes rather than the primary site alone."
        ),
        "operate": (
            "Indication: biopsy-confirmed nasopharyngeal carcinoma; primary treatment is "
            "radiation-based (definitive chemoradiation for most stages) rather than primary surgical "
            "resection, given the nasopharynx's skull-base location and radiosensitivity of this "
            "histology. Setup/key steps: the surgeon's primary procedural role is diagnostic "
            "(nasopharyngoscopy with biopsy) and staging (exam, MRI, EBV DNA when relevant); surgery "
            "as primary treatment is reserved for select cases, and salvage nasopharyngectomy "
            "(endoscopic or open) is considered for persistent/recurrent disease after radiation "
            "failure. Danger structures: internal carotid artery, cranial nerves at the skull base, "
            "and the eustachian tube/middle ear. Failure mode: attributing a unilateral adult "
            "middle-ear effusion to routine eustachian tube dysfunction without nasopharyngeal "
            "examination, delaying diagnosis of an underlying nasopharyngeal mass. Postoperative/"
            "ongoing plan: post-treatment surveillance combines exam, imaging, and EBV DNA trend "
            "(where applicable) to detect recurrence, and long-term monitoring for radiation-related "
            "sequelae given the skull-base radiation field."
        ),
    },
    "Total Laryngectomy": {
        "recognize": (
            "Total laryngectomy permanently separates the airway (via a stoma) from the alimentary "
            "tract, a fundamental anatomic change that must be understood and counseled before "
            "surgery, not discovered afterward -- rehabilitation planning (voice restoration option, "
            "stoma care, swallowing expectations) is part of informed consent, not an afterthought."
        ),
        "localize": (
            "The new anatomy routes air exclusively through the tracheostoma to the lungs, while the "
            "pharyngoesophageal segment (reconstructed from remaining pharyngeal mucosa or a flap) "
            "carries food/liquid to the esophagus; this separation is precisely what makes "
            "tracheoesophageal puncture (connecting the trachea to the neopharynx through a controlled "
            "fistula) a viable voice-restoration option without risking aspiration through an intact "
            "airway."
        ),
        "operate": (
            "Indication: laryngeal cancer not amenable to (or that has failed) organ-preservation "
            "therapy, or a non-functional larynx from prior treatment/disease. Setup: preoperative "
            "counseling on stoma care and voice rehabilitation options (electrolarynx, esophageal "
            "speech, tracheoesophageal puncture). Key steps: remove the larynx en bloc with "
            "appropriate margins, create a permanent tracheostoma, and reconstruct the pharynx "
            "(primary closure, regional, or free flap depending on remaining mucosa and prior "
            "treatment/radiation history) to restore a swallowing conduit; a tracheoesophageal "
            "puncture may be performed primarily or staged for later voice restoration. Danger "
            "structures: the reconstructed pharyngoesophageal segment (leak/fistula risk, especially "
            "in previously irradiated tissue) and the great vessels if neck dissection is performed "
            "concurrently. Failure mode: applying standard oral/nasal supplemental oxygen after "
            "surgery -- the airway no longer connects to the mouth/nose at all, so oxygen and any "
            "airway intervention must be directed at the stoma, not the face; failing to recognize "
            "this is an immediate, potentially fatal error in postoperative or emergency care of a "
            "laryngectomy patient. Postoperative plan: stoma care education, swallow evaluation before "
            "advancing diet (watching for pharyngocutaneous fistula, especially in irradiated "
            "patients), and staged voice rehabilitation."
        ),
    },
    "Parapharyngeal Space Tumor": {
        "recognize": (
            "A parapharyngeal space mass is first characterized by its relationship to the styloid "
            "process/tensor-vascular-styloid fascia, dividing the space into prestyloid "
            "(predominantly salivary gland tissue, so tumors here are usually pleomorphic adenoma or "
            "other salivary neoplasms) and poststyloid (containing the carotid sheath and lower "
            "cranial nerves, so tumors here are more often neurogenic -- paraganglioma, schwannoma) "
            "compartments; this distinction predicts both likely pathology and operative risk before "
            "any biopsy is performed."
        ),
        "localize": (
            "Prestyloid masses displace the parapharyngeal fat and tonsil medially and the carotid "
            "sheath posteriorly; poststyloid masses generally displace prestyloid fat anteriorly and "
            "medially; vessel displacement distinguishes vagal schwannoma (separates ICA and IJV), "
            "sympathetic-chain schwannoma (moves both together), and carotid-body tumors "
            "(splay ICA and ECA at the bifurcation). Imaging (contrast CT/MRI, with MRA/"
            "CTA or catheter angiography when a vascular lesion is suspected) defines this "
            "relationship precisely before any tissue sampling is attempted."
        ),
        "operate": (
            "Indication: symptomatic or growing parapharyngeal space mass, or diagnostic uncertainty "
            "requiring resection. Setup: full vascular characterization (CTA/MRA, sometimes catheter "
            "angiography) before any needle biopsy when a paraganglioma or other vascular lesion is "
            "in the differential -- needling a hypervascular lesion risks significant hemorrhage and "
            "adds little diagnostic value when imaging is already characteristic. Key steps: approach "
            "(transcervical, transcervical-transparotid, or transoral, occasionally with mandibulotomy "
            "for very large lesions) is chosen based on prestyloid/poststyloid location and tumor "
            "size, with careful identification and preservation of the lower cranial nerves and "
            "carotid sheath vessels for poststyloid lesions. Danger structures: internal carotid "
            "artery, internal jugular vein, and cranial nerves IX-XII, all concentrated in the "
            "poststyloid compartment. Failure mode: proceeding to needle biopsy of a suspected "
            "paraganglioma without first characterizing its vascularity -- this is both hazardous and "
            "usually unnecessary when imaging is already diagnostic. Postoperative plan: monitor for "
            "new lower cranial neuropathy (can occur even with careful dissection given proximity), "
            "and swallow/voice assessment when nerves IX/X were at risk."
        ),
    },
    "Carotid Body Paraganglioma": {
        "recognize": (
            "Classic presentation is a slow-growing, painless, pulsatile, hypervascular mass at the "
            "carotid bifurcation, sometimes with a bruit, that is mobile side-to-side but not "
            "vertically (Fontaine's sign) due to its origin at the bifurcation; larger or "
            "longer-standing lesions are more likely to encase the carotid vessels and involve "
            "adjacent cranial nerves (X, XII, sympathetic chain)."
        ),
        "localize": (
            "The tumor arises from paraganglion cells at the carotid bifurcation itself, splaying the "
            "internal and external carotid arteries apart (the classic 'lyre sign' on angiography); "
            "the Shamblin classification grades the tumor by degree of carotid vessel encasement "
            "(I: minimal contact, II: partial encasement, III: complete encasement), which predicts "
            "resection difficulty and vascular morbidity more directly than size alone."
        ),
        "operate": (
            "Indication: growing or symptomatic carotid body paraganglioma, or definitive diagnosis/"
            "treatment in a good surgical candidate; some small, stable, asymptomatic tumors in "
            "older or higher-risk patients may instead be observed. Setup: cross-sectional imaging "
            "(CT/MR angiography) to grade Shamblin class and assess bilaterality (associated with "
            "hereditary paraganglioma syndromes); biopsy is generally unnecessary and potentially "
            "hazardous given hemorrhage risk from this classically hypervascular lesion, and "
            "biochemical screening for catecholamine secretion is performed since a minority are "
            "functional. Key steps: subadventitial dissection plane along the carotid vessels, "
            "working from a less involved area toward the more encased portion, with early control of "
            "feeding vessels; higher Shamblin class predicts a higher likelihood of needing vascular "
            "reconstruction or, rarely, sacrifice. Danger structures: internal and external carotid "
            "arteries, vagus and hypoglossal nerves, and the sympathetic chain, all intimately "
            "associated with the tumor capsule. Failure mode: proceeding to biopsy a classic "
            "vascular-appearing carotid bifurcation mass rather than relying on characteristic imaging "
            "for diagnosis -- biopsy adds bleeding risk without changing management in a "
            "radiographically classic case. Postoperative plan: monitor for new cranial neuropathy "
            "(vagus/hypoglossal) and, for high Shamblin-class resections, vascular surveillance."
        ),
    },
    "Head & Neck Radiation Toxicity / Survivorship": {
        "recognize": (
            "Radiation-related toxicity evolves over years, not just the acute treatment period: "
            "xerostomia and dysphagia can persist or worsen, fibrosis progressively limits neck/jaw "
            "mobility, dental injury and osteoradionecrosis risk accumulate (particularly after "
            "dental extraction in a previously irradiated field), hypothyroidism develops from "
            "incidental thyroid radiation, and accelerated carotid atherosclerosis raises long-term "
            "stroke risk -- each requires its own surveillance timeline rather than a single "
            "post-treatment check."
        ),
        "localize": (
            "Toxicities localize to whatever tissue fell within the radiation field and its dose: "
            "salivary glands (xerostomia), mandible/maxilla (osteoradionecrosis risk, particularly "
            "with dental trauma), pharyngeal constrictors (dysphagia/fibrosis), thyroid gland "
            "(hypothyroidism), and carotid arteries (accelerated atherosclerotic disease) -- reviewing "
            "the actual treatment fields and doses received helps target surveillance rather than "
            "screening generically."
        ),
        "operate": (
            "Most survivorship issues are managed medically/rehabilitatively rather than surgically, "
            "but recognizing when a procedure is needed matters. Key steps: coordinate dental "
            "clearance and extraction planning before radiation when possible, and use extreme "
            "caution and oral surgery/head-and-neck co-management for extractions in irradiated "
            "bone; the 2024 ISOO-MASCC-ASCO guideline does not support routine prophylactic "
            "hyperbaric oxygen, and its use is individualized rather than a default protocol. Established "
            "osteoradionecrosis may eventually require debridement or free-flap reconstruction if "
            "conservative management fails. Failure mode: treating routine post-treatment follow-up "
            "as complete once the cancer surveillance exam is done, without a parallel plan for "
            "thyroid function testing, dental surveillance, dysphagia/fibrosis management, and carotid "
            "disease risk assessment -- survivorship care is a defined, ongoing part of treatment, not "
            "an informal afterthought. Postoperative/ongoing plan: periodic thyroid function testing, "
            "dental surveillance, swallow therapy for progressive fibrosis/dysphagia, and cardiovascular "
            "risk-factor management given elevated carotid disease risk in this population."
        ),
    },
    "TEP and Alaryngeal Speech": {
        "recognize": (
            "After total laryngectomy, voice options are electrolarynx (external mechanical device), "
            "esophageal speech (swallowed air used to vibrate the pharyngoesophageal segment), and "
            "tracheoesophageal puncture (TEP) voice (a prosthesis-controlled fistula shunting "
            "pulmonary air into the pharyngoesophageal segment) -- TEP voice is generally regarded as "
            "producing the most natural-sounding, fluent speech of the three and is now the most "
            "commonly used method where available."
        ),
        "localize": (
            "The TEP itself is a controlled fistula between the posterior tracheal wall and the "
            "anterior wall of the pharyngoesophageal segment, fitted with a one-way valve prosthesis; "
            "voice quality and reliability depend heavily on the pharyngoesophageal segment's tone "
            "(too tight causes hyperfunction/poor voice or requires myotomy; too flaccid causes "
            "poor, wet-sounding voice), so problems localize either to the puncture/prosthesis itself "
            "or to that segment's muscular tone."
        ),
        "operate": (
            "Indication: discuss TEP alongside electrolarynx and esophageal speech with each "
            "laryngectomy candidate, but select puncture based on patient preference, ability to "
            "manage the prosthesis, anatomy, reconstruction and aspiration/leak risk; perform it "
            "primarily (at the time of laryngectomy) or "
            "secondarily (as a later staged procedure). Setup: assess pharyngoesophageal segment tone "
            "preoperatively when possible; a pharyngeal plexus neurectomy or cricopharyngeal myotomy "
            "may be added at the time of laryngectomy in patients thought to be at risk for segment "
            "spasm. Key steps: create the puncture between trachea and pharyngoesophageal segment at "
            "a standardized location, fit and size the voice prosthesis, and train the patient in "
            "digital occlusion of the stoma to direct air through the prosthesis for speech. Danger "
            "structures: the puncture tract itself can leak around the prosthesis or enlarge over "
            "time; aspiration through a failing or displaced prosthesis is the key mechanical risk to "
            "watch for. Failure mode: treating the laryngectomy as technically complete once the "
            "airway/oncologic resection is done, without a concrete plan for voice rehabilitation -- a "
            "technically successful cancer operation that leaves a patient without a communication "
            "plan is incomplete care. Postoperative plan: prosthesis sizing/replacement as it wears, "
            "monitoring for periprosthetic leak (which may need a larger or different prosthesis, or "
            "evaluation for candida overgrowth degrading the valve), and speech-language pathology "
            "follow-up for ongoing voice optimization."
        ),
    },
    "Neck Lymphoma": {
        "recognize": (
            "Consider lymphoma when cervical lymphadenopathy is persistent, associated with systemic "
            "('B') symptoms (fever, night sweats, weight loss), or shows an atypical pattern for "
            "reactive or metastatic squamous disease (e.g., multiple, non-tender, rubbery nodes "
            "across multiple levels, or disease in a patient without a typical head and neck cancer "
            "risk profile) -- this clinical suspicion should change how the node is biopsied, not "
            "just what is on the differential."
        ),
        "localize": (
            "Unlike metastatic SCC, where FNA cytology is usually adequate, lymphoma diagnosis and "
            "subtyping require preserved nodal architecture (immunophenotyping, sometimes molecular/"
            "flow cytometry studies), so the 'localization' question that matters most here is which "
            "node to sample and by what method, not which anatomic level is involved."
        ),
        "operate": (
            "Indication: persistent lymphadenopathy suspicious for lymphoma, especially with systemic "
            "symptoms or an atypical nodal pattern. Setup: discuss the suspected diagnosis with "
            "pathology before biopsy, since the biopsy technique itself is a key decision point here. "
            "Key steps: obtain tissue for morphology, immunophenotyping and flow cytometry; "
            "excisional biopsy of an accessible representative node is preferred when feasible, "
            "but an adequate image-guided core biopsy with multiple cores can establish many "
            "lymphoma diagnoses when excision is unsafe or impractical. FNA alone is generally "
            "insufficient for initial lymphoma classification. Danger structures: standard for whatever neck level is biopsied (spinal "
            "accessory nerve in level V, marginal mandibular nerve near the submandibular region, "
            "etc.) -- the anatomic risk is not disease-specific, but choosing the wrong biopsy "
            "technique is. Failure mode: performing FNA alone (yielding insufficient architecture for "
            "subtyping) or a piecemeal/core biopsy that destroys the nodal architecture needed for "
            "definitive diagnosis, leading to a delayed or repeat procedure -- plan the biopsy "
            "approach with pathology input before, not after, obtaining tissue. Postoperative plan: "
            "expedite pathology review and staging workup, and route the patient to "
            "hematology-oncology promptly once lymphoma is confirmed, since surgery's role here is "
            "diagnostic, not therapeutic."
        ),
    },
}


def apply_depth_content_head_neck_oncology_v396(data_module):
    modules = {m.get("topic"): m for m in data_module.DEEP_MODULES_V6.get(DOMAIN, [])}
    missing = [t for t in DEPTH_V396 if t not in modules]
    if missing:
        raise RuntimeError(f"v39.6: expected {DOMAIN} topics not found: {missing}")
    for topic, fields in DEPTH_V396.items():
        modules[topic].update(fields)
    return {"enriched": list(DEPTH_V396.keys())}
