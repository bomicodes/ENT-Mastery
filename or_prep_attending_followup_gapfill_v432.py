"""v43.2: OR-prep "attending follow-up" pimp-question depth gap-fill.

Requested 2026-09-22 (self-directed audit, confirmed with user): 42 of the 93
OR_PREP_REGISTRY cards sat at only 2 attending-followup Q&A pairs, while the more
developed cards in the same registry carry 3-4. This adds exactly one new,
card-specific Q&A pair to each of the 42 thin cards, grounded directly in that
card's own indications/landmarks/danger/complications fields (all re-read in full
immediately before authoring), bringing every OR-prep card to >=3 pairs. No new
cards, fields, or source_basis citations are added -- this is assessment-depth
parity, not new curriculum content.
"""

# Map: OR_PREP_REGISTRY title -> new [question, answer] pair to append.
NEW_FOLLOWUP_BY_TITLE = {
    "Ossiculoplasty": [
        "What must be checked before choosing a PORP or TORP when stapes mobility is uncertain?",
        "Confirm footplate mobility without forceful manipulation: a PORP couples to a usable stapes "
        "superstructure, whereas a TORP may couple to a mobile footplate when the superstructure is absent. "
        "A fixed footplate requires evaluation and treatment of the fixation itself, potentially staged, "
        "rather than simply placing a PORP or TORP on an immobile endpoint.",
    ],
    "Canalplasty / Exostosis": [
        "Why counsel differently in the only-hearing ear?",
        "Even a small, published risk of iatrogenic sensorineural hearing loss is far more consequential when "
        "it is the patient's only functional ear, so the threshold for surgery and the informed-consent "
        "conversation both shift.",
    ],
    "Tegmen CSF Leak / Encephalocele Repair": [
        "What intraoperative finding should prompt a search for additional defects?",
        "A single repaired defect with persistent or disproportionate leak, or multilobulated dural herniation, "
        "should prompt wider tegmen exposure to rule out a second, unrecognized defect rather than assuming "
        "one repair is sufficient.",
    ],
    "Vestibular Schwannoma Approach Planning": [
        "When is observation preferred over any surgical approach?",
        "Small, asymptomatic, slow-growing tumors -- especially in older or comorbid patients, or where "
        "hearing/facial function is good and growth is unproven -- are reasonable to observe with serial MRI "
        "rather than committing to an approach immediately.",
    ],
    "Middle Fossa Skull-Base Approach": [
        "What structure defines the anterior limit of safe dissection along the middle fossa floor?",
        "The petrous internal carotid artery anteriorly and the greater superficial petrosal "
        "nerve/geniculate-ganglion region define the anterior danger zone; straying anterior to expected "
        "landmarks risks carotid or facial-nerve injury.",
    ],
    "Retrosigmoid Skull-Base Approach": [
        "Why is cerebellar retraction itself a named risk of this approach?",
        "Excessive or prolonged retraction can injure the cerebellum or compromise venous drainage (including "
        "the superior petrosal vein complex), so CSF drainage/positioning to relax the cerebellum before "
        "retraction is part of safe technique.",
    ],
    "Translabyrinthine Skull-Base Approach": [
        "Why consider this approach for a large tumor when hearing is nonserviceable?",
        "It provides direct lateral exposure with early facial-nerve identification at the fundus. The "
        "approach sacrifices residual hearing, so serviceable hearing and a realistic chance of preserving "
        "it remain important considerations when selecting among skull-base approaches.",
    ],
    "Jugular Foramen Tumor Approach": [
        "Why is preoperative vascular imaging essential before any biopsy or resection here?",
        "Jugular foramen masses (classically paraganglioma) can be highly vascular; unplanned biopsy or "
        "dissection without characterizing the ICA/jugular bulb relationship and vascularity risks "
        "catastrophic hemorrhage.",
    ],
    "Endoscopic Maxillary Antrostomy": [
        "What anatomic variant increases the risk of missing the true natural ostium?",
        "An accessory ostium in the posterior fontanelle can be mistaken for the natural ostium; failing to "
        "identify and join it to the true ostium risks a mucus-recirculation pattern that perpetuates disease.",
    ],
    "Endoscopic Sphenoidotomy": [
        "What CT finding should specifically change the operative plan before entering the sphenoid?",
        "A dehiscent optic nerve or carotid artery protruding into the sphenoid lumen (or a markedly asymmetric/"
        "conchal sphenoid) should prompt more cautious, image-guided dissection and altered instrument "
        "orientation to avoid these structures.",
    ],
    "Frontal Sinusotomy / Draf II-III": [
        "Why is the agger nasi cell important to address in most frontal approaches?",
        "The agger nasi cell forms the anterior-inferior boundary of the frontal recess in most patients; "
        "leaving it unaddressed is a common cause of persistent frontal outflow obstruction after an "
        "otherwise adequate-appearing frontal sinusotomy.",
    ],
    "Endoscopic CSF Leak Repair / Nasoseptal Flap": [
        "What should be done if the nasoseptal flap is unexpectedly unavailable (e.g., from prior septal surgery)?",
        "Alternative vascularized options (e.g., a contralateral flap if the pedicle is intact, a "
        "middle-turbinate or other local flap) or a free mucosal/fascial graft with multilayer support should "
        "be planned preoperatively whenever prior septal surgery raises doubt about pedicle integrity.",
    ],
    "Endoscopic Sphenopalatine Artery Ligation": [
        "What should be done if bleeding persists despite clipping/cauterizing the visualized SPA trunk?",
        "Search for and control accessory branches (including a separate posterior septal branch) before "
        "assuming the procedure has failed; unrecognized branching, not technique failure at the main trunk, is "
        "a potential reason for persistent bleeding.",
    ],
    "Endoscopic Orbital / Subperiosteal Abscess Drainage": [
        "Why involve ophthalmology before and after the procedure rather than relying on ENT exam alone?",
        "Serial formal visual-acuity, color-vision, and pupillary assessment are more sensitive for evolving "
        "optic-nerve compromise than a general surgical exam, and a documented ophthalmology baseline is needed "
        "to judge postoperative improvement or deterioration.",
    ],
    "Functional Septorhinoplasty / Nasal Valve Repair": [
        "Why must the L-strut be preserved or reconstructed even when the deviation itself is easily resected?",
        "An inadequate dorsal/caudal L-strut after aggressive septal resection risks delayed saddle-nose "
        "deformity and further destabilizes the very valve support the operation is meant to improve.",
    ],
    "Central Neck Dissection": [
        "Why is the parathyroid blood supply, not just the gland itself, the thing to protect?",
        "A parathyroid gland can appear grossly preserved yet become devascularized if its individual feeding "
        "vessel is sacrificed during meticulous central-compartment clearance, so vascular pedicle "
        "preservation (or deliberate autotransplantation if compromised) matters as much as leaving the gland "
        "in place.",
    ],
    "Reoperative Thyroid / Central Neck Surgery": [
        "Why might intraoperative nerve monitoring be used liberally in this setting even though it does not "
        "replace visual identification?",
        "In a scarred field where normal planes are obliterated, monitoring provides an additional real-time "
        "signal to help localize a nerve segment before it is visually confirmed, complementing rather than "
        "substituting for direct identification.",
    ],
    "Four-Gland Parathyroid Exploration": [
        "What intraoperative adjunct helps confirm that hyperfunctioning tissue has actually been removed?",
        "Intraoperative PTH monitoring converts the operation into a physiologic test: an appropriate "
        "post-excision PTH drop supports adequate resection, while a failure to drop should prompt continued "
        "search rather than closure.",
    ],
    "Reoperative Parathyroidectomy": [
        "Why is imaging particularly important before a reoperative parathyroid case, more so than for a first operation?",
        "Reoperative exploration carries substantially higher RLN and devascularization risk than a first "
        "operation, so strong, ideally concordant localization is required to justify re-entering a scarred "
        "field rather than performing a broader blind re-exploration.",
    ],
    "Total Parotidectomy / Facial Nerve Reconstruction": [
        "Why is facial nerve monitoring used even though the surgeon plans to identify the nerve visually throughout?",
        "Monitoring provides an early warning of nerve irritation or impending injury before visible or "
        "permanent damage occurs, complementing (not replacing) careful visual dissection along the trunk and "
        "branches.",
    ],
    "Arytenoid Adduction": [
        "Why can arytenoid adduction be combined with medialization thyroplasty rather than used alone?",
        "Thyroplasty medializes the membranous vocal fold but does not reliably correct a posterior glottic gap "
        "or vertical-height mismatch at the arytenoid; combining the two procedures addresses both the "
        "membranous and cartilaginous glottic deficits in the same setting.",
    ],
    "Injection Laryngoplasty": [
        "Why is injection laryngoplasty often chosen as a temporizing rather than definitive procedure after acute "
        "vocal-fold paralysis?",
        "Because early spontaneous neural recovery is possible after acute paralysis, a temporary or "
        "resorbable material can support voice/airway protection during the recovery window without committing "
        "to a permanent medialization before the true, stable deficit is known.",
    ],
    "Posterior Cordotomy / Arytenoidectomy": [
        "Why might a staged or conservative approach be favored over an aggressive single-stage posterior opening?",
        "Because voice and swallowing function are traded for airway caliber, a staged or more limited initial "
        "approach lets the surgeon assess the functional result before committing to a wider, less reversible "
        "opening.",
    ],
    "Cricopharyngeal Myotomy": [
        "What preoperative finding would make this procedure unlikely to help?",
        "Poor pharyngeal driving force (weak pharyngeal contraction) or diffuse esophageal body dysmotility on "
        "swallow physiology testing predicts limited benefit, since myotomy only addresses a restrictive UES, "
        "not a pump-failure or diffuse motility problem.",
    ],
    "Laryngeal Botulinum Toxin Injection": [
        "Why is bilateral injection approached more cautiously than unilateral injection?",
        "Bilateral thyroarytenoid/adductor weakness can meaningfully compromise airway protection and cause "
        "significant breathiness or aspiration, so bilateral dosing is typically more conservative or staged "
        "compared with a straightforward unilateral injection.",
    ],
    "Open Partial / Conservation Laryngectomy": [
        "Why does preoperative pulmonary function matter as much as tumor anatomy in patient selection?",
        "Conservation laryngectomy preserves a functional larynx but still risks aspiration during "
        "swallowing/airway-protection recovery; a patient with poor pulmonary reserve may not tolerate even "
        "transient aspiration well enough to be a safe candidate regardless of favorable tumor anatomy.",
    ],
    "Transoral Laser Microsurgery — Laryngeal Cancer": [
        "Why is anterior commissure involvement a specific technical challenge for TLM?",
        "The anterior commissure is a tight, hard-to-visualize angle where depth and orientation are easy to "
        "lose; tumor there raises the risk of positive deep margins and makes maintaining 3-D orientation "
        "during piecemeal resection especially difficult.",
    ],
    "Transnasal Esophagoscopy": [
        "What patient factor is most likely to make TNE technically difficult or unsafe?",
        "Severe nasal obstruction/septal deviation, an overactive gag reflex, or poor patient cooperation can "
        "prevent adequate unsedated passage and visualization, in which case escalation to sedated or "
        "operative endoscopy is appropriate.",
    ],
    "Tracheoesophageal Puncture": [
        "Why does pharyngoesophageal (PE) segment spasm matter for TEP candidacy and outcome?",
        "A hypertonic or spastic PE segment can prevent adequate vibration for voicing even with a "
        "well-functioning prosthesis, which is why some centers assess or treat PE-segment tone (e.g., with "
        "myotomy or chemodenervation) as part of achieving usable speech.",
    ],
    "Rigid Tracheobronchoscopy": [
        "Why is a clear, pre-briefed ventilation plan with anesthesia established before the scope enters the airway?",
        "Rigid instrumentation shares the airway with the anesthesia team in a way that flexible bronchoscopy "
        "does not, so ventilation strategy (jet ventilation, apneic technique, or intermittent ventilation) "
        "must be agreed upon in advance to avoid a crisis mid-procedure.",
    ],
    "Pediatric Laryngotracheal Reconstruction": [
        "Why is a preoperative swallow/aspiration evaluation particularly important in this population?",
        "Many children being considered for LTR have comorbid feeding/aspiration risk, and a graft or "
        "reconstruction that succeeds anatomically but leaves the child unable to protect the airway during "
        "swallowing undermines the goal of decannulation.",
    ],
    "Laryngotracheal Cleft Repair": [
        "Why is a layered, two-plane closure (airway and esophageal mucosa separately) emphasized rather than a single-layer repair?",
        "A single shared closure line between the airway and esophagus is prone to dehiscence and fistula "
        "recurrence; separating the airway and esophageal mucosal closures into distinct layers with "
        "interposed tissue reduces the risk of the cleft reopening.",
    ],
    "Cricotracheal Resection": [
        "Why is CTR reserved for high-grade stenosis rather than used as a first-line option for milder disease?",
        "CTR carries anastomotic and RLN risk that is not justified when expansion techniques (e.g., LTR with "
        "grafting) can achieve an adequate airway with lower risk; resection is reserved for stenosis severe "
        "enough that expansion alone is unlikely to succeed.",
    ],
    "Tracheal Resection / Anastomosis": [
        "Why is the innominate artery specifically discussed in the danger list for tracheal surgery?",
        "The innominate artery crosses the trachea anteriorly at a variable level and is at risk both during "
        "dissection and from a low tracheostomy/anastomosis site eroding into it postoperatively "
        "(tracheoinnominate fistula), which is catastrophic if unrecognized.",
    ],
    "Otoplasty": [
        "Why is postoperative hematoma treated as a surgical emergency rather than observed?",
        "An expanding auricular hematoma can compromise the cartilage's blood supply and lead to chondritis or "
        "cartilage necrosis (a 'cauliflower ear' deformity) within hours, so prompt evacuation is required "
        "rather than watchful waiting.",
    ],
    "Paramedian Forehead Flap": [
        "Why is the flap typically left pedicled and divided in a second stage rather than transferred as a free graft or single-stage flap?",
        "Staged pedicled transfer preserves the vascular supply through the pedicle until the distal flap has "
        "revascularized from the recipient bed, which is what allows reliable survival of a flap covering "
        "large or structurally complex nasal defects.",
    ],
    "Deep Neck Abscess Drainage": [
        "Why might a stable-appearing patient with a deep neck abscess still need urgent airway planning before drainage?",
        "Airway anatomy can be distorted by the abscess itself, and induction of anesthesia or subsequent "
        "swelling can precipitate sudden obstruction even in a patient who appears stable preoperatively, so an "
        "explicit airway plan (awake fiberoptic intubation, tracheostomy availability) should be established "
        "before induction.",
    ],
    "Microtia Reconstruction": [
        "Why does rib cartilage graft harvest carry a specific risk beyond the auricular reconstruction itself?",
        "Harvesting costal cartilage risks pneumothorax if the underlying pleura is violated, so the chest "
        "should be examined/imaged postoperatively when there is any intraoperative concern for pleural injury.",
    ],
    "Palatoplasty / Cleft Palate Repair": [
        "Why assess postoperative airway risk after palatoplasty, particularly in a child with micrognathia?",
        "Palatal surgery and perioperative swelling can worsen upper-airway obstruction in a child with an "
        "already narrow airway; tongue displacement by a retractor and postoperative edema add to this risk. "
        "Furlow and pushback techniques use palatal tissue, not tongue-based flaps, so plan postoperative "
        "airway observation according to the child's baseline obstruction and operative course.",
    ],
    "TORS Tonsil / Base-of-Tongue Resection": [
        "Why is delayed postoperative oropharyngeal hemorrhage specifically feared after TORS?",
        "The lingual artery and its branches run close to the resection bed; a delayed bleed from this "
        "vascular territory can be sudden, large-volume, and simultaneously threaten the airway (from "
        "blood/clot) and circulation, demanding immediate airway and hemorrhage management.",
    ],
    "Oral Cavity Composite Resection": [
        "Why is the inferior alveolar nerve/canal specifically assessed preoperatively when mandibular involvement is suspected?",
        "Its involvement changes both the extent of bony resection needed for oncologic clearance and the "
        "expected postoperative sensory deficit, and its course helps define whether a marginal or segmental "
        "mandibulectomy is oncologically adequate.",
    ],
    "Free-Flap Compromise — Take-Back / Salvage": [
        "Why do both arterial insufficiency and venous congestion require urgent flap evaluation and take-back?",
        "Either can rapidly cause irreversible flap loss, and salvage falls as recognition and re-exploration "
        "are delayed. Arterial failure limits inflow; venous obstruction raises pressure, impairs perfusion, "
        "and can progress to thrombosis. Do not assume venous congestion has a reliably safe waiting period.",
    ],
}


def apply_or_prep_attending_followup_gapfill_v432(data_module, app_module=None):
    orp = data_module.OR_PREP_REGISTRY
    result = {"updated": []}

    by_title = {card.get("title"): card for card in orp.values() if isinstance(card, dict)}

    for title, pair in NEW_FOLLOWUP_BY_TITLE.items():
        card = by_title.get(title)
        if card is None:
            raise RuntimeError(f"v43.2: OR-prep card missing from registry: {title}")
        followups = card.setdefault("attending_followup", [])
        existing_questions = {q for q, _ in followups}
        if pair[0] not in existing_questions:
            followups.append(pair)
            result["updated"].append(title)

    if app_module is not None:
        app_module.OR_PREP_REGISTRY = orp
    return result
