"""v62.0: OR Tomorrow cards for three operations that had only a curriculum topic.

Revision FESS, Endoscopic Pituitary / Anterior Skull Base Approach and Completion
Thyroidectomy (Supraglottoplasty already had a card and is merged with it by or_merge_v610). Each card is written from its canonical Deep Curriculum module (same
facts, operative framing) and merged with that topic by or_merge_v610 (the topic page opens the
card, and the card carries the topic's teaching). Installed before or_merge_v610.
"""

RHINO = "Rhinology"
ABX_SINUS = {
    "indicated": "Not routinely indicated",
    "regimen": "No routine preoperative antibiotic for this nasal/sinus procedure. If non-absorbable packing is left in place, follow institutional protocol for coverage during the packing period.",
    "rationale": "Evidence does not support routine perioperative antibiotics for endoscopic sinus surgery; any use is typically tied to a specific nonabsorbable-packing practice or culture-directed treatment of active purulence, not the surgery itself. Confirm against current institutional protocol.",
}

CARDS_V620 = {
    "revision-fess": {
        "title": "Revision FESS (Revision Endoscopic Sinus Surgery)",
        "domain": RHINO,
        "linked_topic": "Revision FESS",
        "or_family_v190": "sinus",
        "indications": (
            "Persistent or recurrent CRS after prior sinus surgery with a defined, surgically correctable target that is "
            "causing disease, after the failure mechanism has been named and medical therapy optimized: residual uncinate, "
            "maxillary recirculation through an antrostomy that misses the natural ostium, retained ethmoid, agger nasi or "
            "frontal cells, middle-turbinate lateralization, synechiae or ostial stenosis, or untreated frontal/sphenoid "
            "disease. A patent cavity with discordant symptoms is a reason to reconsider the diagnosis, not to operate again."
        ),
        "setup": [
            "Name the failure mechanism before booking: residual anatomy, scar/stenosis/recirculation, recurrent type 2 inflammation (CRSwNP, AERD, AFRS), an untreated focal or host source (odontogenic, fungal, tumor, immune, CF/PCD), poor topical delivery or adherence, or a nonrhinogenic cause such as migraine.",
            "Review the prior operative note, pathology and cultures, prior and current imaging, and postoperative endoscopy. Obtain a current fine-cut sinus CT and read it as a surgical map: natural maxillary ostium vs prior antrostomy, residual uncinate, retained partitions, frontal recess, sphenoid, middle-turbinate position, and lamina/skull-base integrity.",
            "Lower the threshold for image guidance: altered or dehiscent lamina or skull base, prior turbinate loss, osteitis, or distorted optic/carotid relationships. Navigation supplements, and does not replace, fixed anatomic landmarks.",
            "On CT, assess olfactory fossa depth and lateral lamella height (Keros) and side-to-side skull-base asymmetry, the main CSF-leak risk in revision surgery.",
            "Optimize inflammation and bleeding risk before surgery (topical or systemic steroid per disease, antithrombotics, AERD plan) and decide in advance which prior openings are working and will be preserved.",
        ],
        "landmarks": [
            "maxillary sinus roof and medial orbital wall (reliable even when turbinates are gone)",
            "natural maxillary ostium (posterior to the nasolacrimal duct, behind the uncinate)",
            "skull base, followed from posterior (sphenoid/posterior ethmoid) to anterior",
            "lamina papyracea / medial orbital wall",
            "anterior ethmoid artery and frontal recess",
            "sphenoid face, optic nerve and carotid prominences",
        ],
        "steps": [
            "Decongest and examine with 0- and angled endoscopes; lyse synechiae to restore the middle meatus while preserving working openings and viable mucosa.",
            "Re-establish constant landmarks before crossing scar: find the maxillary sinus roof and medial orbital wall, then the skull base, using navigation to confirm when anatomy is distorted.",
            "Correct maxillary recirculation by connecting the prior or accessory opening to the true natural ostium; remove residual uncinate and enlarge only as needed.",
            "Complete residual anterior and posterior ethmoidectomy along the lamina and skull base, removing retained or osteitic partitions while working from known to unknown.",
            "Address frontal recess disease (residual agger nasi or frontal cells, scar, neo-osteogenesis) only when it is part of the failure mechanism; escalate to a Draf procedure if indicated.",
            "Open or revise the sphenoid when diseased, using its natural ostium medial to the superior turbinate and the preoperative optic/carotid map.",
            "Medialize or stabilize a lateralized middle turbinate (for example controlled synechia or suture) to keep the middle meatus open.",
            "Keep both eyes uncovered in the field and ballotte the globe while watching the lamina to detect a breach. If orbital fat appears, stop the microdebrider, do not pull on the fat, and avoid tight packing. Repair a recognized CSF leak at the time.",
            "If orientation becomes uncertain near the orbit, skull base, optic nerve or carotid: stop, control bleeding, re-localize with fixed landmarks, navigation and angled views, and defer unsafe tissue removal.",
        ],
        "danger": [
            "Skull base / lateral lamella (CSF leak)",
            "Lamina papyracea / orbit and medial rectus",
            "Anterior ethmoid artery (retro-orbital hematoma)",
            "Optic nerve and internal carotid in a revised sphenoid or Onodi cell",
            "Nasolacrimal duct anterior to the maxillary ostium",
        ],
        "exit_check": [
            "Inspect orbit, skull base and each opened sinus for hemostasis, CSF and exposed orbital fat; check the eye for proptosis or a tense orbit before waking the patient.",
            "Confirm the intended drainage pathways are open and connected to natural ostia, the middle turbinate is stable, and mucosa is preserved; place spacers or steroid-eluting stents only if planned.",
        ],
        "postop": [
            "Treat sudden visual decline, a relative afferent pupillary defect, proptosis, ophthalmoplegia, severe orbital pain or a tense orbit as orbital compartment syndrome: examine immediately and decompress (lateral canthotomy and cantholysis) without waiting for imaging when vision is threatened.",
            "Clear unilateral rhinorrhea, severe headache, meningismus or altered mental status suggests CSF leak or intracranial injury and needs urgent evaluation.",
            "Start saline irrigation and resume phenotype-directed topical steroid therapy; schedule endoscopic debridement and surveillance to prevent synechiae.",
            "Long-term success includes maintenance medical therapy and symptom/QOL plus endoscopic outcome assessment over roughly 3 to 12 months; biologics are an option for selected severe type 2 CRSwNP.",
        ],
        "complications": {
            "early": [
                "Orbital hematoma or orbital injury (anterior ethmoid artery, lamina breach) with vision threat: immediate exam and decompression pathway.",
                "CSF leak or intracranial injury from a lateral lamella or skull-base breach in scarred anatomy.",
                "Significant epistaxis, including sphenopalatine or ethmoidal bleeding.",
            ],
            "late": [
                "Recurrent synechiae, ostial restenosis or middle-turbinate lateralization.",
                "Recurrent inflammatory disease (CRSwNP, AERD, AFRS) despite technically complete surgery.",
                "Nasolacrimal duct injury with epiphora; mucocele from obstructed frontal or ethmoid outflow.",
            ],
        },
        "attending_followup": [
            ["Why did the first operation fail?",
             "Name the mechanism before operating: residual uncinate or partitions, maxillary recirculation, scar or stenosis, middle-turbinate lateralization, osteitis, recurrent type 2 disease, an untreated focal or host source, poor topical delivery, or a nonrhinogenic diagnosis."],
            ["What is maxillary recirculation and how do you fix it?",
             "Mucus leaves the natural ostium and re-enters through a separate (prior or accessory) opening. Connect the antrostomy to the true natural ostium rather than enlarging the wrong window."],
            ["Which landmarks are reliable in a revision cavity?",
             "The maxillary sinus roof, medial orbital wall/lamina and skull base remain constant even when turbinates and partitions are gone; re-establish them before crossing scar."],
            ["Does image guidance make revision surgery safe?",
             "It helps confirm position when anatomy is distorted, but it supplements fixed landmarks. If orientation is lost near a danger zone, stop and re-map rather than dissecting harder."],
            ["When is more surgery the wrong answer?",
             "When the cavity is patent and symptoms are not explained by objective sinonasal disease, or when type 2 inflammation is the driver and maintenance therapy or a biologic is the better tool."],
        ],
        "antibiotics": ABX_SINUS,
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — revision endoscopic sinus surgery, residual anatomy, scar/osteitis, image-guided orientation.",
            "Shin JJ et al. Clinical Practice Guideline: Surgical Management of Chronic Rhinosinusitis. Otolaryngol Head Neck Surg. 2025;172 Suppl 2:S1-S47 (PMID 40424072).",
            "Bewick J et al. Anatomic findings in revision endoscopic sinus surgery: case series and review of contributory factors. Allergy Rhinol (Providence). 2016;7(3):e151-e157 (PMID 28107148).",
            "Pasha & Golub, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — revision sinus evaluation and operative safety.",
        ],
    },
    "endoscopic-pituitary": {
        "title": "Endoscopic Endonasal Pituitary / Anterior Skull Base Approach",
        "domain": RHINO,
        "linked_topic": "Endoscopic Pituitary / Anterior Skull Base Approach",
        "or_family_v190": "skull_base",
        "indications": (
            "Sellar and selected midline anterior skull-base lesions that need tissue, decompression or resection after "
            "multidisciplinary review: macroadenomas compressing the optic chiasm, functional adenomas for which surgery is "
            "first-line (Cushing disease, acromegaly, TSH-secreting adenomas), prolactinomas that do not respond to or cannot "
            "tolerate dopamine agonists, pituitary apoplexy with visual loss, and selected planum, cribriform or clival lesions via "
            "extended approaches. Most prolactinomas are treated with dopamine agonists, and appropriate incidental, "
            "noncompressive lesions are observed. The rhinologist builds the corridor and the reconstruction; neurosurgery "
            "treats the lesion."
        ),
        "setup": [
            "Confirm the plan with neurosurgery and endocrinology: dedicated pituitary MRI, complete pituitary hormone testing (with correction of deficits, especially cortisol, before surgery), and formal visual-field testing when the chiasm is involved.",
            "Review CT for sphenoid pneumatization (sellar, presellar, conchal), intersinus septa that insert on the carotid canal, carotid or optic canal dehiscence, Onodi cells and septal anatomy. Plan navigation.",
            "Decide the reconstruction before dural entry: if a high-flow intraoperative CSF leak is plausible (extended approach, large or suprasellar tumor, planned arachnoid opening), raise or preserve a vascularized nasoseptal flap on the posterior septal artery at the start.",
            "Agree on a carotid-injury plan (packing material, team roles, endovascular availability), type and crossmatch, a perioperative glucocorticoid plan agreed with endocrinology (stress dosing for preoperative adrenal insufficiency; selective or withheld with an intact axis and in Cushing disease, with a morning cortisol on postoperative day 1-2), and sodium/fluid monitoring orders.",
            "Agree on the lumbar-drain policy for high-flow leaks (a randomized trial found fewer postoperative leaks with a perioperative lumbar drain after high-flow defects).",
        ],
        "landmarks": [
            "sphenoid ostia medial to the superior turbinates, about 1.5 cm above the choana",
            "sellar floor, planum sphenoidale and clival recess",
            "carotid prominences (paraclival and parasellar)",
            "optic protuberances and lateral opticocarotid recesses",
            "posterior septal artery at the sphenoid face (nasoseptal flap pedicle)",
            "cavernous sinuses laterally and the optic chiasm superiorly",
        ],
        "steps": [
            "Decongest, lateralize the middle turbinates (resecting one only if access requires), and identify both sphenoid ostia in the sphenoethmoidal recesses.",
            "Raise the nasoseptal flap when indicated, preserving its posterior pedicle across the sphenoid rostrum, and store it in the nasopharynx or maxillary sinus; otherwise preserve the pedicle with a rescue-flap incision.",
            "Perform a posterior septectomy and wide bilateral sphenoidotomy so both nostrils can be used (binarial, two-surgeon technique).",
            "Take down intersinus septa without twisting (drill rather than torque any septum that inserts on a carotid canal) and identify the sella, planum, clival recess, carotid and optic prominences, and opticocarotid recesses.",
            "Open the sellar floor in the midline between the carotids; neurosurgery opens the dura and resects or decompresses the lesion, staying within the corridor bounded by carotids laterally and the chiasm superiorly.",
            "Inspect for CSF leak (Valsalva) and reconstruct by defect and flow: no leak or low flow with free grafts or a dural substitute; high flow with a multilayer repair covered by the vascularized nasoseptal flap placed on bare bone.",
            "Support the reconstruction with absorbable packing and/or a balloon or splints per protocol, and cover the septal donor site if mucosa was harvested.",
        ],
        "danger": [
            "Internal carotid artery (paraclival/parasellar; dehiscence and septa on the carotid canal)",
            "Optic nerves and chiasm",
            "Cavernous sinus and cranial nerves III, IV, V1-V2, VI",
            "CSF leak and meningitis",
            "Pituitary stalk and gland (diabetes insipidus, hypopituitarism)",
            "Sphenopalatine/posterior septal arteries (flap pedicle, epistaxis)",
        ],
        "exit_check": [
            "Confirm hemostasis in the sella and corridor, flap position on bare bone with the pedicle untwisted, and a watertight multilayer reconstruction appropriate to the leak grade.",
            "Agree on postoperative orders before leaving: neurologic and visual checks, strict input/output and serial sodium, steroid replacement, nasal precautions, and when to image.",
        ],
        "postop": [
            "Check vision and neurologic status early and repeatedly; new visual loss or decreased consciousness can mean hematoma in the sella and needs urgent imaging and return to the OR.",
            "Monitor urine output, urine specific gravity and serum sodium for the triphasic response: early diabetes insipidus (for example urine output over about 250-300 mL/h for 2 hours with specific gravity below 1.005 and rising sodium; treat with as-needed desmopressin rather than a fixed schedule), then SIADH with hyponatremia around days 5 to 10, then sometimes permanent diabetes insipidus.",
            "Follow the agreed glucocorticoid protocol (replacement if deficient; otherwise a morning cortisol on day 1-2; in Cushing disease steroids are withheld to assess remission), retest pituitary function, and arrange endocrine and visual follow-up.",
            "No CPAP, BiPAP or mask ventilation and no blind nasal instrumentation (nasogastric tube, nasal suction, nasal trumpet) after skull-base reconstruction, because they risk tension pneumocephalus and flap displacement.",
            "CSF-leak precautions after skull-base reconstruction (no nose blowing, straining or straws; sneeze with the mouth open); clear rhinorrhea, headache or fever prompts evaluation for leak or meningitis.",
            "Saline irrigation and scheduled endoscopic debridement; crusting is expected while the septal donor site re-mucosalizes.",
        ],
        "complications": {
            "early": [
                "Internal carotid artery injury with catastrophic bleeding: pack, maintain perfusion, and go directly to angiography/endovascular treatment.",
                "Postoperative CSF leak, tension pneumocephalus or meningitis.",
                "Visual decline from hematoma or chiasmal injury.",
                "Diabetes insipidus, adrenal insufficiency, or later SIADH with hyponatremia.",
            ],
            "late": [
                "Hypopituitarism requiring hormone replacement; residual or recurrent tumor.",
                "Sinonasal morbidity: crusting, synechiae, olfactory loss, septal perforation, nasal dorsum change after flap harvest.",
                "Carotid pseudoaneurysm presenting with delayed epistaxis.",
            ],
        },
        "attending_followup": [
            ["What bounds the endonasal corridor to the sella?",
             "Carotid arteries and cavernous sinuses laterally, the optic apparatus superiorly, and the clivus posteriorly; the sella bulges into the posterosuperior wall of the sphenoid sinus, below the planum and above the clival recess, between the carotid prominences."],
            ["When do you raise the nasoseptal flap before the resection?",
             "When a high-flow intraoperative CSF leak is plausible: extended approaches, large or suprasellar tumors, or a planned arachnoid opening. Otherwise preserve the pedicle so a rescue flap remains possible."],
            ["How do you handle an intersinus septum that inserts on the carotid canal?",
             "Never twist or fracture it; drill it down carefully, because torque can tear a dehiscent carotid."],
            ["What sodium problems follow pituitary surgery?",
             "Diabetes insipidus early (dilute polyuria, rising sodium, treated with desmopressin) and SIADH later (hyponatremia around days 5 to 10)."],
            ["What do you do for a carotid injury?",
             "Communicate, control with packing and suction, maintain blood pressure and perfusion, and transfer directly to angiography for endovascular control; later imaging screens for pseudoaneurysm."],
        ],
        "antibiotics": {
            "indicated": "Commonly given -- a short perioperative course",
            "regimen": "A preoperative IV dose (commonly a first-generation cephalosporin or per institutional protocol), sometimes continued briefly while packing is in place.",
            "rationale": "Common practice for endonasal skull-base surgery that crosses the sinonasal tract and exposes the subarachnoid space, although the evidence base is limited and practices vary. Confirm against institutional neurosurgical protocol.",
        },
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — endoscopic endonasal skull-base anatomy and reconstruction.",
            "Hadad G, Bassagasteguy L, Carrau RL, et al. A novel reconstructive technique after endoscopic expanded endonasal approaches: vascular pedicle nasoseptal flap. Laryngoscope. 2006;116(10):1882-1886.",
            "Zwagerman NT, Wang EW, Shin SS, et al. Does lumbar drainage reduce postoperative cerebrospinal fluid leak after endoscopic endonasal skull base surgery? A prospective, randomized controlled trial. J Neurosurg. 2019;131(4):1172-1178.",
            "Atlas of Endoscopic Sinus and Skull Base Surgery, 2nd ed. — endonasal corridor, sphenoid anatomy and reconstruction.",
            "Pasha & Golub, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — sphenoid anatomy and skull-base complications.",
        ],
    },
    "completion-thyroidectomy": {
        "title": "Completion Thyroidectomy",
        "domain": "Thyroid / Parathyroid / Salivary",
        "linked_topic": "Completion Thyroidectomy",
        "or_family_v190": "thyroid",
        "indications": (
            "Removal of the remaining lobe after lobectomy when final pathology or new findings change the plan: features that "
            "would have warranted total thyroidectomy upfront (tumor larger than 4 cm, gross extrathyroidal extension, "
            "clinically evident or extensive nodal disease, distant metastasis, extensive vascular invasion, or aggressive "
            "histology), when radioactive iodine is planned (normal thyroid would take up the dose meant for residual "
            "cancer), contralateral disease, or when thyroglobulin-based surveillance would materially benefit. It is "
            "selective, not routine: cancer found after lobectomy does not by itself require completion."
        ),
        "setup": [
            "Confirm the indication from final pathology (size, margins, extrathyroidal extension, vascular invasion, histology, nodes) and current contralateral and neck ultrasound; agree with endocrinology on whether RAI or thyroglobulin surveillance changes management.",
            "Document vocal fold mobility with preoperative laryngoscopy. If the first-side recurrent laryngeal nerve is paralyzed, the operation risks bilateral paralysis and airway compromise, so reconsider or defer the operation, consider leaving a small remnant at the ligament of Berry, use nerve monitoring, and consent for possible tracheostomy.",
            "Review the first operative note for which parathyroids were seen or preserved, nerve findings and any central neck dissection.",
            "Choose timing: early (within about a week, before dense scar) or delayed (about 3 months, after inflammation settles), avoiding the period of peak inflammation. These intervals come from surgical series; comparative series show little difference in complications by timing, and timing is often driven by RAI planning and surgeon preference.",
            "Check baseline calcium, PTH and vitamin D, and review the first-side pathology for inadvertently removed parathyroid tissue, which raises the risk of hypoparathyroidism.",
            "Plan intraoperative nerve monitoring, consider parathyroid identification aids, and arrange postoperative calcium or PTH protocol.",
        ],
        "landmarks": [
            "recurrent laryngeal nerve in the tracheoesophageal groove and at the cricothyroid joint (laryngeal entry point)",
            "inferior thyroid artery crossing the RLN",
            "ligament of Berry",
            "external branch of the superior laryngeal nerve near the superior pole vessels",
            "superior and inferior parathyroid glands of the remaining side",
            "trachea and cricoid",
        ],
        "steps": [
            "Reopen the prior incision, raise subplatysmal flaps, and enter the unoperated side through fresh planes, often lateral to the strap muscles if the midline is scarred.",
            "Obtain baseline vagal and recurrent nerve signals with intraoperative monitoring before dissection.",
            "Mobilize the superior pole, ligating vessels close to the gland to protect the external branch of the superior laryngeal nerve.",
            "Identify the recurrent laryngeal nerve (in unscarred territory, or at its laryngeal entry deep to the inferior edge of the inferior constrictor, posterior to the cricothyroid joint) before dividing tissue near the ligament of Berry.",
            "Identify and preserve both parathyroids on their blood supply; autotransplant a devascularized gland into the sternocleidomastoid after frozen-section confirmation that the tissue is parathyroid, so thyroid or tumor is not implanted.",
            "Remove the lobe completely, including the pyramidal lobe and any isthmus remnant, since residual thyroid defeats RAI and thyroglobulin follow-up.",
            "Confirm the nerve signal after resection, check hemostasis with a Valsalva maneuver, and close in layers.",
        ],
        "danger": [
            "Contralateral recurrent laryngeal nerve (bilateral paralysis risk)",
            "Remaining parathyroid glands (permanent hypoparathyroidism)",
            "External branch of the superior laryngeal nerve",
            "Postoperative neck hematoma",
        ],
        "exit_check": [
            "Confirm final nerve signal; if the signal is lost and the other side is already weak, plan the airway and extubation with anesthesia before leaving the OR.",
            "Confirm hemostasis and parathyroid viability or autotransplantation, and order postoperative calcium or PTH monitoring.",
        ],
        "postop": [
            "Watch for neck hematoma (swelling, pain, stridor, dysphagia): open the wound at the bedside and evacuate if the airway is threatened.",
            "Assess voice and airway; stridor after extubation raises concern for bilateral vocal fold paralysis and needs urgent laryngoscopy and airway management.",
            "Follow PTH and calcium per protocol and treat symptomatic or significant hypocalcemia with calcium and calcitriol.",
            "Coordinate RAI preparation with endocrinology: recombinant TSH lets levothyroxine start right after surgery, whereas withdrawal means 3 to 4 weeks off hormone; use a low-iodine diet and avoid iodinated contrast before RAI.",
        ],
        "complications": {
            "early": [
                "Neck hematoma with airway compromise.",
                "Recurrent laryngeal nerve injury; bilateral paralysis with stridor if the first-side nerve is impaired.",
                "Transient hypocalcemia from parathyroid devascularization.",
            ],
            "late": [
                "Permanent hypoparathyroidism.",
                "Permanent vocal fold paralysis or voice change from external branch injury.",
                "Residual thyroid tissue limiting RAI and thyroglobulin surveillance.",
            ],
        },
        "attending_followup": [
            ["Why scope the larynx before completion thyroidectomy?",
             "If the first-side nerve is paralyzed, injuring the second nerve causes bilateral paralysis and airway compromise; knowing this changes the indication, technique and extubation plan."],
            ["Why do early or delayed timing instead of operating at 3 to 4 weeks?",
             "Surgical series suggest operating either early, before dense scar forms, or after about 3 months when inflammation has settled, Comparative series show little difference in complications by timing, so RAI planning and surgeon preference often decide."],
            ["Why does residual thyroid matter for radioactive iodine?",
             "Normal thyroid concentrates iodine much more than cancer cells, so a remnant absorbs the dose meant for residual cancer and keeps thyroglobulin from being a useful marker."],
            ["Can you ablate the remaining lobe with radioactive iodine instead of operating?",
             "Not routinely advised: ablating an intact lobe needs high doses, works less reliably and can cause radiation thyroiditis; surgery is preferred when completion is indicated."],
            ["How do you find the nerve in a reoperated field?",
             "Start in unscarred tissue, often laterally, or find it at its laryngeal entry deep to the inferior edge of the inferior constrictor, posterior to the cricothyroid joint, and use nerve monitoring."],
        ],
        "antibiotics": {
            "indicated": "Not routinely indicated",
            "regimen": "No preoperative antibiotic required for this clean neck procedure.",
            "rationale": "Thyroidectomy is a clean procedure without mucosal entry; prophylactic antibiotics are not routinely given. Confirm against institutional protocol.",
        },
        "source_basis": [
            "Ringel MD et al. 2025 American Thyroid Association Management Guidelines for Adult Patients with Differentiated Thyroid Cancer. Thyroid. 2025;35(8):841-985 (PMID 40844370).",
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — management of differentiated thyroid cancer and completion thyroidectomy.",
            "Pasha & Golub, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e, Ch 3 Endocrinology.",
            "K.J. Lee's Essential Otolaryngology, 12e — thyroid surgery and reoperative thyroid surgery.",
        ],
    },
}


def install_or_cards_v620(data, app_mod):
    import textbook_curriculum_v470
    registry = data.OR_PREP_REGISTRY
    added = []
    for slug, card in CARDS_V620.items():
        if slug in registry:
            continue
        c = {k: (list(v) if isinstance(v, list) else dict(v) if isinstance(v, dict) else v) for k, v in card.items()}
        c["attending_followup"] = [list(p) for p in card["attending_followup"]]
        c["complications"] = {k: list(v) for k, v in card["complications"].items()}
        c.update({"slug": slug, "status": "authored-v62.0", "review_status_v190": "operative-depth reviewed",
                  "sequence_status_v200": "procedure-specific", "sources": list(card["source_basis"])})
        registry[slug] = c
        added.append(slug)
        textbook_curriculum_v470.TOPIC_OR_MAP_V470.setdefault(card["linked_topic"], [])
        if slug not in textbook_curriculum_v470.TOPIC_OR_MAP_V470[card["linked_topic"]]:
            textbook_curriculum_v470.TOPIC_OR_MAP_V470[card["linked_topic"]].append(slug)
    if getattr(app_mod, "OR_PREP_REGISTRY", None) is not registry:
        app_mod.OR_PREP_REGISTRY = registry
    return {"added": added}
