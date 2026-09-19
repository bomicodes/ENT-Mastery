"""v39.7 -- Pediatric Otolaryngology depth repair (content-staleness sweep, batch 8/9).

Same two defects as prior batches. Choanal Atresia already has rich,
distinct recognize/localize content (not flagged for duplication) -- only
its operate placeholder is replaced. See thyroglossal_duct_cyst_depth_v389
for the pattern and rationale.
"""

DOMAIN = "Pediatric Otolaryngology"

DEPTH_V397 = {
    "Pediatric Hearing Loss Workup": {
        "recognize": (
            "Separate conductive (outer/middle ear pathway), sensorineural (cochlear), and auditory "
            "neuropathy spectrum disorder (present cochlear function but disordered neural "
            "transmission -- normal otoacoustic emissions with an abnormal auditory brainstem "
            "response) patterns, since each has a different natural history and intervention "
            "pathway; timing is uniquely urgent in children because spoken-language development has "
            "a sensitive early window that does not wait for a leisurely diagnostic pace."
        ),
        "localize": (
            "Newborn hearing screening (otoacoustic emissions or automated ABR) localizes only to "
            "'pass/refer,' not to a specific diagnosis, so a refer result requires diagnostic "
            "audiologic testing (typically ABR) to determine degree, type, and configuration of loss, "
            "and, when sensorineural, appropriate etiologic workup (genetic testing, CMV testing in "
            "the newborn period when still possible, imaging when indicated) to localize a cause."
        ),
        "operate": (
            "This is primarily a diagnostic pathway, but the pace and endpoint are what matter most. "
            "Key steps: screen by 1 month, confirm diagnosis by 3 months and enroll in early "
            "intervention by 6 months (1-3-6); programs already meeting those milestones should "
            "strive for 1-2-3 (screen by 1, diagnose by 2, intervene by 3 months), consistent with "
            "JCIH 2019. Hearing technology and cochlear implant referral follow audiologic "
            "findings and candidacy without delaying early language access; "
            "any conductive component identified (e.g., middle-ear effusion) should be addressed "
            "without letting it delay assessment or management of a coexisting sensorineural "
            "component. Failure mode: treating a 'better audiogram number' as the goal rather than "
            "functional access to spoken language -- device selection, timing, and family engagement "
            "with early intervention services matter more to language outcome than incremental "
            "threshold improvement. Postoperative/ongoing plan: serial audiologic and "
            "developmental/speech-language monitoring, since some etiologies (e.g., connexin-related, "
            "CMV-related) can be progressive and require ongoing surveillance rather than a one-time "
            "diagnosis."
        ),
    },
    "Branchial Cleft Anomalies": {
        "recognize": (
            "Lateral neck pits, cysts, or fistulae follow reproducible embryologic pathways tied to "
            "the branchial (pharyngeal) apparatus; first cleft anomalies present near the ear/"
            "parotid region, second (the most common by far) present along the anterior border of "
            "the sternocleidomastoid, third and fourth anomalies present lower in the neck and are "
            "associated with the piriform sinus, each with a distinct clinical pattern and risk of "
            "recurrent infection."
        ),
        "localize": (
            "Each type has a defining anatomic relationship that dictates surgical risk: first cleft "
            "anomalies relate intimately to the facial nerve and parotid gland (Work classification "
            "further distinguishes relationship to the nerve); second cleft tracts classically course "
            "between the internal and external carotid arteries toward the tonsillar fossa; third and "
            "fourth cleft anomalies track near the recurrent laryngeal nerve and communicate with the "
            "piriform sinus, which is why they recur after simple excision unless the piriform sinus "
            "tract/opening is addressed (often via endoscopic cauterization of the sinus opening)."
        ),
        "operate": (
            "Indication: confirmed or strongly suspected branchial anomaly, especially with recurrent "
            "infection, since infected tissue is harder to dissect safely and increases recurrence "
            "risk. Setup: preoperative imaging (ultrasound, CT/MRI, sometimes an esophagram for "
            "suspected piriform sinus tracts) to define the tract's course, and treat active "
            "infection before elective excision when possible. Key steps: complete excision of the "
            "cyst/sinus tract along its full course -- for first cleft anomalies, this means "
            "identifying and preserving the facial nerve (often requiring parotid dissection); for "
            "second cleft tracts, following the tract between the carotid vessels toward the tonsil; "
            "for third/fourth anomalies, addressing the piriform sinus opening endoscopically, often "
            "combined with open excision of the tract. Danger structures: facial nerve (first cleft), "
            "internal/external carotid arteries (second cleft), and recurrent laryngeal nerve/carotid "
            "sheath (third/fourth cleft). Failure mode: excising only the visible cyst/external "
            "opening without tracing and removing the full tract, or failing to address a piriform "
            "sinus origin in third/fourth cleft disease -- both are the leading causes of recurrence. "
            "Postoperative plan: watch for infection/seroma, and counsel that a missed or incompletely "
            "treated tract will likely recur, sometimes years later."
        ),
    },
    "Lymphatic Malformation": {
        "recognize": (
            "A lymphatic malformation typically presents as a soft, compressible, often "
            "transilluminating mass (macrocystic disease transilluminates well; microcystic disease "
            "less so) that can be present at birth or noted in early childhood, and characteristically "
            "enlarges acutely with intercurrent infection or intralesional hemorrhage rather than "
            "growing at a steady, predictable rate."
        ),
        "localize": (
            "Lymphatic malformations do not respect normal anatomic boundaries and can cross multiple "
            "fascial planes and neck spaces (e.g., extending from the floor of mouth through the neck "
            "into the mediastinum), which is why imaging (MRI is preferred for full extent) is used to "
            "map the malformation's true boundaries rather than relying on the visible/palpable "
            "portion alone; airway or floor-of-mouth/tongue base involvement in particular changes the "
            "urgency of management."
        ),
        "operate": (
            "Indication for intervention: symptomatic disease (airway compromise, feeding difficulty, "
            "disfigurement, recurrent infection/hemorrhage) rather than presence of the lesion alone; "
            "asymptomatic, stable disease can be observed. Setup: sclerotherapy (particularly "
            "effective for macrocystic disease) is often first-line, with surgical debulking/excision "
            "reserved for lesions not amenable to or that fail sclerotherapy, especially "
            "microcystic or diffuse disease. Key steps: when surgery is chosen, plan for the "
            "malformation's tendency to be more extensive than externally apparent, stage debulking "
            "when complete excision would risk major structures, and coordinate with interventional "
            "radiology when combining sclerotherapy and surgery. Danger structures: depend entirely "
            "on location -- lingual/hypoglossal nerves and airway structures for floor-of-mouth/tongue "
            "base disease, facial nerve for parotid-region disease, and great vessels for deep neck "
            "extension. Failure mode: treating the lesion's baseline size as a stable predictor of "
            "urgency -- a lymphatic malformation involving the airway can enlarge abruptly with "
            "infection or intralesional bleeding, converting an elective plan into an airway emergency "
            "with little warning. Postoperative plan: monitor for recurrent swelling with future "
            "infections (residual malformation tissue remains prone to this), and plan staged "
            "treatment when a single intervention cannot safely address the full extent."
        ),
    },
    "Supraglottoplasty": {
        "recognize": (
            "Supraglottoplasty targets the specific collapsing supraglottic structures identified on "
            "flexible laryngoscopy in laryngomalacia -- typically foreshortened aryepiglottic folds, "
            "redundant arytenoid mucosa, or a posteriorly displaced/omega-shaped epiglottis -- rather "
            "than performing a generic supraglottic resection; the operation is tailored to the "
            "specific anatomic pattern of collapse seen preoperatively."
        ),
        "localize": (
            "Collapse localizes to one or more of three sites -- aryepiglottic folds, "
            "arytenoid/cuneiform mucosa, or the epiglottis itself -- and preoperative awake flexible "
            "laryngoscopy (supplemented by dynamic assessment at the time of surgery) identifies "
            "which site(s) actually collapse during inspiration in that specific patient, which "
            "determines exactly what tissue is addressed."
        ),
        "operate": (
            "Indication: laryngomalacia causing significant symptoms -- failure to thrive, "
            "significant apnea/desaturation, feeding difficulty -- refractory to conservative "
            "management. Setup: microlaryngoscopy/bronchoscopy under spontaneous ventilation to "
            "confirm the diagnosis, rule out synchronous airway lesions, and dynamically assess which "
            "supraglottic structures collapse. Key steps: divide foreshortened aryepiglottic folds "
            "and/or trim redundant arytenoid mucosa as indicated by the specific collapse pattern, "
            "using carefully limited, symmetric or staged treatment as anatomy warrants, and preserve enough "
            "normal tissue and mucosal cover to protect against aspiration. Danger structures: the "
            "airway itself (edema is the main early postoperative risk) and the interarytenoid "
            "mucosa/posterior structures whose function protects against aspiration during "
            "swallowing. Failure mode: overly aggressive bilateral tissue removal in a single "
            "sitting, which can scar the two sides together and create supraglottic stenosis -- a "
            "avoiding opposing raw mucosal surfaces and excessive resection reduces this risk. "
            "Postoperative plan: monitor for airway edema (occasionally requiring "
            "overnight observation), and reassess feeding/growth and stridor resolution rather than "
            "just endoscopic appearance alone."
        ),
    },
    "Laryngotracheal Reconstruction": {
        "recognize": (
            "Laryngotracheal reconstruction (LTR) is considered when subglottic or tracheal stenosis "
            "has not responded adequately to endoscopic management (balloon dilation, endoscopic "
            "scar lysis) and the airway anatomy is suitable for open cartilage-grafting "
            "reconstruction rather than continued endoscopic attempts."
        ),
        "localize": (
            "The stenosis level and grade (commonly graded by the Cotton-Myer system for subglottic "
            "stenosis) determine graft strategy: anterior grafting alone may suffice for milder "
            "anterior stenosis, while combined anterior and posterior cartilage grafting is needed "
            "for more severe or circumferential disease, and the stenosis's exact craniocaudal extent "
            "determines how much airway needs to be reconstructed."
        ),
        "operate": (
            "Indication: symptomatic, endoscopically refractory laryngotracheal stenosis in a patient "
            "with airway anatomy suitable for cartilage grafting (single-stage vs. staged with a "
            "temporary stent/T-tube, depending on severity and comorbidities). Setup: costal "
            "cartilage is the most common graft source; preoperative assessment includes full airway "
            "endoscopy to define stenosis extent and rule out additional lesions. Key steps: incise "
            "the stenotic segment (anterior cricoid split or more extensive laryngofissure depending "
            "on severity), place shaped cartilage graft(s) to expand the airway lumen anteriorly "
            "and/or posteriorly, and decide between single-stage closure (extubating soon after) "
            "versus staged reconstruction with a stent left in place, based on stenosis severity and "
            "patient factors. Danger structures: the recurrent laryngeal nerves (particularly with "
            "posterior grafting near the cricoid), and the airway itself, which can restenose if graft "
            "healing or postoperative scarring is unfavorable. Failure mode: judging the operation a "
            "success by lumen size on a single postoperative look rather than by whether the child "
            "achieves a safe, functional airway and, when that is the goal, successful decannulation -- "
            "these are related but not identical endpoints, and a widened lumen that still can't "
            "support decannulation has not met the actual goal of surgery. Postoperative plan: staged "
            "endoscopic surveillance for restenosis or granulation tissue, and a defined plan/timeline "
            "for stent removal and decannulation attempts when a staged approach was used."
        ),
    },
    "Choanal Atresia": {
        "operate": (
            "Indication: confirmed choanal atresia; bilateral atresia in a neonate is an airway "
            "emergency requiring urgent intervention because newborns are obligate/preferential nasal "
            "breathers, while unilateral atresia can typically be repaired electively once the child "
            "is older and larger. Setup: secure the airway (oral airway/McGovern nipple, sometimes "
            "intubation) for bilateral disease while arranging definitive repair, and complete CHARGE-"
            "association evaluation before or alongside surgical planning given the association's "
            "frequency. Key steps: endoscopic transnasal perforation and widening of the atretic "
            "plate (bony, membranous, or mixed) using powered instrumentation, with stenting used "
            "selectively rather than routinely, since chronic stenting itself can cause granulation "
            "and restenosis. Danger structures: the skull base superiorly (risk of CSF leak with "
            "overly aggressive posterior/superior drilling) and the orbit laterally. Failure mode: "
            "treating a newborn's bilateral obstruction as a lower-urgency problem because the infant "
            "otherwise appears comfortable at rest -- the cyclical cyanosis pattern (worse with "
            "feeding, relieved by crying, since crying converts to mouth breathing) can mask how "
            "immediately dangerous the obstruction is between episodes. Postoperative plan: serial "
            "dilation/debridement to prevent restenosis, which is common enough that a single "
            "procedure is not always curative, and continued CHARGE-association-directed "
            "surveillance and specialist coordination."
        ),
    },
    "Pediatric Vocal Fold Immobility": {
        "recognize": (
            "Unilateral vocal fold immobility typically presents with a weak/breathy cry and "
            "possible aspiration with thin liquids, while bilateral immobility presents with a "
            "relatively normal or near-normal voice/cry but significant stridor and respiratory "
            "distress -- because both folds obstruct the airway in a near-midline or paramedian "
            "position, bilateral disease can be a neonatal airway emergency even when the voice "
            "sounds deceptively unremarkable."
        ),
        "localize": (
            "The lesion can be central (neurologic, e.g., Arnold-Chiari malformation causing bilateral "
            "immobility) or peripheral (surgical/traumatic injury to the recurrent laryngeal nerve, "
            "as after cardiac or esophageal surgery, or idiopathic); distinguishing central from "
            "peripheral causes, and determining whether immobility reflects true paralysis versus a "
            "fixed cricoarytenoid joint, directs both prognosis and workup (brain imaging for "
            "suspected central causes, laryngeal EMG to help clarify recovery potential)."
        ),
        "operate": (
            "Indication for airway-widening surgery (e.g., posterior cordotomy, "
            "partial arytenoidectomy, or tracheostomy) in bilateral immobility: persistent, "
            "symptomatic airway obstruction after allowing adequate time (often up to 12 months, since "
            "spontaneous recovery is common, especially in idiopathic or perioperative-injury cases) "
            "for potential neural recovery, unless the airway compromise is too severe to wait. Setup: "
            "establish mechanism (central vs. peripheral, true paralysis vs. joint fixation) and "
            "estimate recovery potential (laryngeal EMG, serial exam) before committing to an "
            "irreversible airway-widening procedure. Key steps: any lateralizing/widening procedure "
            "(cordotomy, arytenoidectomy) trades airway improvement for some voice/swallowing "
            "function, so the extent is titrated to what is needed to achieve a safe airway, not "
            "maximized reflexively; tracheostomy remains an option that avoids permanently altering "
            "glottic anatomy while awaiting recovery. Danger structures: the airway itself (both "
            "under- and over-treatment carry risk) and the arytenoid cartilage/cricoarytenoid joint. "
            "Failure mode: proceeding to an irreversible glottic-widening procedure before adequately "
            "establishing the mechanism and true recovery potential -- a paralysis that would have "
            "recovered does not need a permanent structural sacrifice of voice/airway-protection "
            "tissue. Postoperative plan: serial laryngoscopy to track recovery or confirm the airway "
            "result, and voice/swallow therapy given the functional trade-offs of most "
            "airway-widening procedures."
        ),
    },
    "Subglottic Hemangioma": {
        "recognize": (
            "Suspect subglottic hemangioma in an infant with progressive biphasic stridor typically "
            "emerging around 6-12 weeks of life (as the lesion proliferates), which can be mistaken "
            "for recurrent croup; a cutaneous hemangioma in a 'beard' distribution (chin, lower lip, "
            "mandible, neck) raises concern for an associated airway hemangioma and should "
            "prompt targeted airway evaluation when symptoms or distribution warrant it; PHACE "
            "screening is a separate consideration for large segmental facial hemangiomas."
        ),
        "localize": (
            "The lesion is typically located in the posterolateral subglottis and, being a true "
            "vascular proliferative lesion (infantile hemangioma) rather than a vascular malformation, "
            "follows a proliferative-then-involuting natural history; imaging (contrast-enhanced CT or "
            "MRI) and, definitively, direct laryngoscopy/bronchoscopy characterize the extent of "
            "airway narrowing before treatment planning."
        ),
        "operate": (
            "Indication: symptomatic airway obstruction from a confirmed or strongly suspected "
            "subglottic hemangioma. Setup: propranolol has become first-line medical therapy for "
            "problematic infantile hemangiomas, including airway lesions, and has substantially "
            "reduced the need for surgical intervention; endoscopic evaluation confirms the diagnosis "
            "and extent and allows monitoring of response. Key steps: when medical therapy is "
            "insufficient or urgent airway control is needed, options include endoscopic laser/"
            "resection (with attention to avoiding circumferential injury that risks stenosis), open "
            "excision, or, historically, tracheostomy for temporary airway support while awaiting "
            "involution or treatment response. Danger structures: the airway itself, given the risk of "
            "iatrogenic subglottic stenosis from aggressive endoscopic treatment of a circumferential "
            "or near-circumferential lesion. Failure mode: repeatedly treating recurrent stridor "
            "episodes as croup without escalating to airway evaluation when the pattern is atypical "
            "(age outside typical croup range, biphasic rather than inspiratory-predominant stridor, "
            "recurrent/persistent rather than self-limited course) -- an atypical 'croup' pattern "
            "should trigger direct airway evaluation. Postoperative/ongoing plan: monitor response to "
            "propranolol with serial exam/endoscopy as needed, and follow the expected proliferative-"
            "then-involuting course, since many lesions substantially improve without ever requiring "
            "surgery."
        ),
    },
    "Tracheomalacia / Bronchomalacia": {
        "recognize": (
            "Suspect tracheomalacia/bronchomalacia (excessive dynamic collapse of the airway wall "
            "during, classically, expiration) with noisy breathing, a barky or 'seal-like' cough, "
            "recurrent lower respiratory infections, or, in severe cases, life-threatening 'dying "
            "spells' (acute apparent life-threatening events from severe airway collapse); severity "
            "ranges widely from an incidental finding to a life-threatening presentation."
        ),
        "localize": (
            "Primary (intrinsic cartilage weakness, often related to prematurity) tracheomalacia is "
            "diffuse, while secondary tracheomalacia localizes to a site of extrinsic compression or "
            "prior injury -- vascular ring/sling, mediastinal mass, or a segment weakened after "
            "prolonged intubation or tracheoesophageal fistula repair -- so identifying an underlying "
            "compressive or structural cause changes management from purely supportive to potentially "
            "correctable."
        ),
        "operate": (
            "Indication for intervention: severe, symptomatic malacia (recurrent life-threatening "
            "events, significant respiratory compromise, failure to wean from respiratory support) "
            "that has not responded to conservative management, or malacia caused by a correctable "
            "extrinsic compressive lesion. Setup: dynamic airway evaluation (awake, spontaneously "
            "ventilating bronchoscopy) is essential, because static imaging (standard CT) can miss or "
            "underestimate a collapse that only manifests during active breathing; identify and "
            "address any extrinsic compressive cause first when present (e.g., vascular ring "
            "division). Key steps: for severe, refractory malacia, options include prolonged positive "
            "airway pressure support, aortopexy (suspending the airway anteriorly via anterior "
            "displacement of the aorta) for tracheal malacia, tracheostomy (splinting the airway open "
            "with positive pressure past the malacic segment), or external/internal airway stenting "
            "in select severe cases. Danger structures: great vessels adjacent to the trachea "
            "(relevant to both the cause and the aortopexy procedure itself) and the airway's own "
            "fragile malacic wall. Failure mode: relying on a standard, non-dynamic CT or a single "
            "static airway view to rule out malacia -- because the defining feature is dynamic "
            "collapse, static imaging can appear reassuringly normal in a truly symptomatic patient. "
            "Postoperative plan: reassess symptom burden and growth, since many children with mild-"
            "moderate primary tracheomalacia improve as the airway grows and cartilage matures, "
            "reducing the eventual need for intervention."
        ),
    },
    "Microtia / Aural Atresia": {
        "recognize": (
            "External-ear microtia commonly coexists with ear canal atresia and middle-ear anomalies, "
            "producing a conductive hearing loss on the affected side; because bilateral involvement "
            "threatens spoken-language access the same way any bilateral conductive loss in infancy "
            "does, hearing status -- not just the cosmetic ear deformity -- must be assessed and "
            "addressed early, independent of the timeline for any ear reconstruction."
        ),
        "localize": (
            "Grade the external ear deformity (e.g., Marx or similar microtia grading) separately from "
            "the middle/inner ear status on temporal bone CT, since the two do not always correlate "
            "in severity; CT defines whether the middle ear, ossicular chain, and inner ear are "
            "suitable candidates for atresia repair versus better served by a non-surgical or "
            "implantable hearing pathway."
        ),
        "operate": (
            "Indication and sequencing: hearing rehabilitation (bone-conduction hearing device -- "
            "softband initially in infancy, later a bone-anchored option -- for unilateral or "
            "especially bilateral conductive loss) begins in infancy, well before any consideration of "
            "cosmetic ear reconstruction, which is typically staged for later childhood once "
            "sufficient costal cartilage is available (for autologous rib-cartilage reconstruction) "
            "or a prosthetic/synthetic framework approach is chosen. Setup: multidisciplinary "
            "planning between otology (hearing rehabilitation, atresia repair candidacy) and facial "
            "plastics (auricular reconstruction timing/technique). Key steps: for atresia repair "
            "candidates, create a new ear canal and reconstruct/mobilize the ossicular chain where "
            "anatomy allows; for auricular reconstruction, harvest and carve costal cartilage (or use "
            "an alternative framework) staged with skin coverage and eventual lobule/tragus "
            "detailing. Danger structures: facial nerve, which frequently has an anomalous course in "
            "atretic temporal bones, and the inner ear if drilling proceeds medially. Failure mode: "
            "sequencing cosmetic reconstruction before hearing needs are addressed, or assuming a "
            "unilateral deformity does not need timely hearing evaluation -- even unilateral loss has "
            "real developmental and educational impact and should not simply wait for the cosmetic "
            "timeline. Postoperative plan: audiologic follow-up regardless of which reconstructive "
            "path is chosen, and staged revision of the reconstructed ear as the child grows."
        ),
    },
    "Pediatric Aspiration": {
        "recognize": (
            "Aspiration in children arises from several distinct mechanisms -- neurologic "
            "discoordination of the swallow (e.g., cerebral palsy), a structural laryngeal cleft "
            "allowing direct communication between the airway and esophagus, vocal fold immobility "
            "impairing glottic closure, an airway lesion altering laryngeal mechanics, or "
            "reflux-associated laryngeal irritation -- and the correct workup and treatment differ "
            "substantially by mechanism, so recognizing which pattern is present matters more than "
            "confirming that aspiration is occurring."
        ),
        "localize": (
            "Localize the swallowing dysfunction with functional testing -- modified barium swallow "
            "or FEES to see the mechanics of oral/pharyngeal/laryngeal coordination -- and, when a "
            "structural cause is suspected, direct laryngoscopy/bronchoscopy to look specifically for "
            "a laryngeal cleft or other anatomic lesion, rather than assuming reflux is the cause "
            "without characterizing the actual swallow physiology."
        ),
        "operate": (
            "Indication for procedural intervention: a confirmed structural cause amenable to repair "
            "(laryngeal cleft repair, addressing vocal fold immobility as above) or, for severe, "
            "persistent aspiration risking recurrent aspiration pneumonia, feeding-route changes "
            "(gastrostomy tube) while the underlying mechanism is treated or the child matures. Setup: "
            "complete functional swallow assessment and endoscopic airway evaluation before assuming "
            "a specific mechanism. Key steps: repair a laryngeal cleft endoscopically (injection "
            "augmentation for milder clefts, endoscopic or open closure for more extensive disease) "
            "when this is the identified cause, or address vocal fold immobility per its own workup if "
            "that is the mechanism. Danger structures: the airway itself and the recurrent laryngeal "
            "nerves near the interarytenoid area during cleft repair. Failure mode: labeling "
            "aspiration or chronic respiratory symptoms as 'reflux' and starting acid suppression "
            "without ever characterizing swallowing physiology -- reflux and aspiration can coexist "
            "or be confused for one another, and treating presumed reflux will not fix an unaddressed "
            "structural or neuromuscular swallowing problem. Postoperative plan: repeat functional "
            "swallow study to confirm improvement before liberalizing diet texture, and continued "
            "multidisciplinary (speech-language pathology, GI, pulmonology as indicated) follow-up "
            "given how often multiple contributing factors coexist."
        ),
    },
}


def apply_depth_content_pediatric_ent_v397(data_module):
    modules = {m.get("topic"): m for m in data_module.DEEP_MODULES_V6.get(DOMAIN, [])}
    missing = [t for t in DEPTH_V397 if t not in modules]
    if missing:
        raise RuntimeError(f"v39.7: expected {DOMAIN} topics not found: {missing}")
    for topic, fields in DEPTH_V397.items():
        modules[topic].update(fields)
    return {"enriched": list(DEPTH_V397.keys())}
