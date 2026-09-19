"""v39.5 -- Rhinology / Allergy / Skull Base depth repair (content-staleness
sweep, batch 6/9).

Same two defects as v39.0-v39.4. Three topics (Sphenoidotomy, Odontogenic
Sinusitis, Endoscopic CSF Leak Repair / Nasoseptal Flap) already carry rich,
specific operate content from earlier refinement patches -- only the
unfilled placeholder sentence prefixing that content is stripped for those,
preserving the good material after it. The remaining topics get full
recognize/localize/operate rewrites. See thyroglossal_duct_cyst_depth_v389
for the pattern and rationale.
"""

DOMAIN = "Rhinology / Allergy / Skull Base"

B1 = "For operative/procedural cases, explicitly state indication, setup, landmarks, danger structures, key steps, failure modes and postoperative plan. "
B2 = "State whether a procedure is indicated; if so, rehearse setup, landmarks, danger structures, key steps, failure/rescue and postoperative plan. "

FULL_REWRITES = {
    "Nasal Anatomy for Endoscopy": {
        "recognize": (
            "Endoscopic orientation proceeds from the nasal floor/inferior turbinate anteriorly, "
            "along the middle turbinate and its axilla, to the uncinate process and ethmoid bulla, "
            "through the basal lamella (the true boundary between anterior and posterior ethmoid), "
            "and back to the sphenoethmoidal recess and choana -- each landmark confirms position "
            "before advancing to the next."
        ),
        "localize": (
            "The lamina papyracea marks the lateral limit toward orbit throughout the anterior and "
            "posterior ethmoid, the skull base/fovea ethmoidalis marks the superior limit, and the "
            "basal lamella of the middle turbinate is the single most reliable internal landmark "
            "separating anterior ethmoid cells (draining to the middle meatus) from posterior "
            "ethmoid cells (draining to the superior meatus)."
        ),
        "operate": (
            "This module is anatomic orientation underlying every endoscopic sinus procedure rather "
            "than a standalone operation. Key steps: identify each landmark in sequence before any "
            "instrumentation, and use image guidance/navigation when anatomy is distorted by prior "
            "surgery, extensive polyposis, or tumor. Danger structures: orbit (lamina papyracea) and "
            "skull base (fovea ethmoidalis/cribriform plate), both of which are thin and can be "
            "asymmetric or dehiscent, especially after prior surgery. Failure mode: advancing an "
            "instrument into any space -- a cell, a recess -- without first confirming its position "
            "relative to the orbit and skull base; disorientation, not technical difficulty, is the "
            "leading cause of orbital and skull-base injury in sinus surgery. Postoperative "
            "relevance: accurate anatomic documentation at the index procedure (which cells were "
            "opened, where the skull base was identified) materially changes the safety of any "
            "future revision surgery."
        ),
    },
    "Inferior Turbinate Hypertrophy": {
        "recognize": (
            "Distinguish reversible mucosal/vascular congestion (responsive to decongestion, allergy "
            "treatment, or the nasal cycle) from fixed soft-tissue or bony turbinate enlargement that "
            "will not improve medically, and from a nasal-valve or septal problem that only mimics "
            "turbinate-driven obstruction -- decongestion testing on exam helps separate these before "
            "committing to turbinate-directed treatment."
        ),
        "localize": (
            "Obstruction is localized to the inferior meatus/nasal floor level; because the septum, "
            "internal nasal valve, and inferior turbinate all contribute to airflow at roughly the "
            "same anterior nasal segment, an isolated turbinate reduction in a patient whose real "
            "problem is septal deviation or valve collapse will under-deliver on symptom relief."
        ),
        "operate": (
            "Indication: fixed turbinate hypertrophy causing nasal obstruction refractory to medical "
            "therapy (topical steroid, antihistamine/decongestant trial), confirmed not to be primarily "
            "valve or septal in origin. Setup: options range from submucosal reduction "
            "(radiofrequency, microdebrider-assisted submucosal resection) to partial turbinectomy for "
            "more severe/bony hypertrophy. Key steps: preserve the functional mucosa and as much of "
            "the turbinate's normal architecture as possible while reducing bulk, since the turbinate "
            "performs real physiologic humidification/warming function. Danger structures: excessive "
            "or overly aggressive resection risks empty nose syndrome -- a paradoxical sensation of "
            "obstruction despite a wide-open airway, from loss of the mucosa's airflow-sensing "
            "function -- as well as chronic crusting and dryness. Failure mode: treating turbinate "
            "size as the only variable and resecting aggressively rather than conservatively; more "
            "tissue removed does not reliably mean more symptom relief and can trade one problem "
            "(obstruction) for another (dryness/crusting/dysfunctional airflow). Postoperative plan: "
            "saline irrigation and humidification during healing, with realistic counseling that "
            "conservative techniques preserve function even if initial obstruction relief feels less "
            "dramatic."
        ),
    },
    "Septal Deviation": {
        "recognize": (
            "A deviated septum is a common incidental imaging/exam finding and only becomes a "
            "surgical target when it meaningfully contributes to symptomatic nasal obstruction -- "
            "correlate the side and location of deviation with the patient's actual obstructive "
            "symptoms rather than treating any visible deviation as inherently pathologic."
        ),
        "localize": (
            "Localize the deviation's level (caudal/columellar, mid-septal, or high dorsal/bony) and "
            "direction, since this determines both its functional impact (caudal deviation affects "
            "the internal/external nasal valve most directly) and the technical approach needed to "
            "correct it, including whether cartilage support near the keystone or caudal strut must "
            "be preserved."
        ),
        "operate": (
            "Indication: symptomatic nasal obstruction attributable to septal deviation, refractory to "
            "medical management or with a clearly mechanical component unlikely to respond to "
            "medical therapy. Setup: septoplasty via a hemitransfixion or similar incision, elevating "
            "mucoperichondrial flaps bilaterally. Key steps: resect or reposition the deviated "
            "cartilage/bone while preserving an adequate dorsal and caudal strut (typically at least "
            "1-1.5 cm) for structural support, and avoid creating opposing mucosal tears on both "
            "sides at the same location, which risks a septal perforation. Danger structures: the "
            "septal cartilage's blood supply (subperichondrial dissection preserves it) and the "
            "keystone area, where overly aggressive cartilage removal destabilizes the nasal dorsum. "
            "Failure mode: over-resecting cartilage for a cosmetically 'straighter' septum at the "
            "cost of losing structural support, producing saddle nose deformity or valve collapse "
            "later, or creating bilateral mucosal injury at the same site leading to perforation. "
            "Postoperative plan: splints or quilting sutures to prevent hematoma, saline care during "
            "healing, and reassessment of the functional (not just cosmetic) result."
        ),
    },
    "Endoscopic Maxillary Antrostomy": {
        "recognize": (
            "The functional goal of maxillary antrostomy is enlarging and incorporating the natural "
            "maxillary ostium (found posterior/inferior to the uncinate process, within the "
            "hiatus semilunaris) rather than creating an arbitrary new opening -- recognizing the "
            "true ostium versus surrounding mucosa is the first technical decision of the case."
        ),
        "localize": (
            "The natural ostium sits high on the medial maxillary wall, close to the orbital floor "
            "and nasolacrimal duct anteriorly and the posterior fontanelle (an accessory-ostium-prone "
            "area) posteriorly, so the antrostomy is enlarged posteriorly and inferiorly from the "
            "natural ostium rather than anteriorly, to avoid the nasolacrimal duct."
        ),
        "operate": (
            "Indication: maxillary sinus disease (chronic rhinosinusitis, recurrent acute sinusitis, "
            "antrochoanal polyp, fungal ball) requiring surgical drainage/access. Setup: uncinectomy "
            "first to expose the ethmoid infundibulum and natural ostium. Key steps: positively "
            "identify the natural ostium (often confirmed with a probe/seeker before opening), then "
            "enlarge it posteriorly and inferiorly along the fontanelle rather than working "
            "anteriorly. Danger structures: the nasolacrimal duct anteriorly and the orbital floor "
            "superiorly/laterally. Failure mode: failing to identify and incorporate the true natural "
            "ostium and instead creating a separate accessory opening -- mucus can recirculate "
            "between the two openings (in through one, out and back in through the other), causing "
            "persistent symptoms despite a technically patent antrostomy. Postoperative plan: "
            "endoscopic debridement and saline irrigation during healing, with follow-up endoscopy to "
            "confirm the antrostomy remains open and is not stenosing."
        ),
    },
    "Ethmoidectomy": {
        "recognize": (
            "Ethmoidectomy is performed cell-by-cell rather than as a single maneuver, using the "
            "lamina papyracea as the constant lateral boundary and the skull base as the constant "
            "superior boundary throughout, with the basal lamella marking the transition from "
            "anterior to posterior ethmoid cells."
        ),
        "localize": (
            "Anterior ethmoid cells lie anterior to the basal lamella and drain to the middle meatus; "
            "posterior ethmoid cells lie posterior to it and drain to the superior meatus, sitting "
            "closer to the optic nerve and sphenoid, which is why entering the posterior ethmoid "
            "carries a different risk profile (optic nerve proximity, sometimes a dehiscent or "
            "Onodi-cell-related nerve) than anterior work."
        ),
        "operate": (
            "Indication: ethmoid sinus disease (chronic rhinosinusitis with or without polyps, "
            "access for further posterior procedures) requiring surgical clearance. Setup: proceed "
            "systematically from anterior to posterior ethmoid, keeping the lamina papyracea and "
            "skull base continuously in view. Key steps: open cells working medially away from the "
            "lamina papyracea, identify the basal lamella and cross it deliberately (not by blunt "
            "instrumentation) to enter the posterior ethmoid, and follow the skull base posteriorly "
            "toward the sphenoid face. Danger structures: lamina papyracea (orbit) laterally, fovea "
            "ethmoidalis/cribriform plate (skull base and CSF) superiorly and medially, and the "
            "anterior ethmoidal artery, which can retract into the orbit if transected. Failure mode: "
            "continuing dissection after encountering orbital fat or clear fluid (CSF) rather than "
            "stopping immediately -- either finding means stop, identify the injury precisely, and "
            "manage it deliberately (orbital fat: stop lateral dissection and inspect for hematoma; "
            "CSF: prepare for skull-base repair) rather than pressing forward. Postoperative plan: "
            "endoscopic debridement to prevent adhesion/scarring between raw mucosal surfaces, and "
            "saline irrigation during healing."
        ),
    },
    "Frontal Sinusotomy / Draf Procedures": {
        "recognize": (
            "Frontal sinus surgery escalates along a spectrum -- from simple frontal recess/ostium "
            "opening (Draf I/IIa-type dissection) to extended unilateral (Draf IIb) or bilateral "
            "(Draf III/modified Lothrop) drainage -- and the correct starting point is the least "
            "extensive procedure that will adequately address the disease and anatomy present, not "
            "the most extensive option available."
        ),
        "localize": (
            "The frontal recess is a three-dimensional, often narrow and cell-crowded corridor "
            "bounded by the orbit laterally, skull base/anterior ethmoidal artery posteriorly, and "
            "variable agger nasi/frontal cells anteriorly-superiorly; understanding a given patient's "
            "specific frontal cell anatomy on CT before entering the recess is what prevents "
            "disorientation in this the most technically difficult corridor in sinus surgery."
        ),
        "operate": (
            "Indication: frontal sinus disease refractory to medical therapy or requiring surgical "
            "access (mucocele, tumor, recalcitrant chronic rhinosinusitis); the extent of surgery "
            "(Draf I through III) is chosen by disease burden and anatomy, escalating only when a "
            "less extensive opening will not achieve adequate drainage or access. Setup: detailed "
            "preoperative CT review of frontal recess cell anatomy, ideally with image guidance for "
            "extended procedures. Key steps: clear frontal recess cells working from a known "
            "landmark (agger nasi, skull base) toward the frontal ostium, preserving mucosa on bone "
            "circumferentially around the neo-ostium when possible to reduce restenosis; a Draf III/"
            "modified Lothrop removes the intersinus septum and floor between frontal sinuses to "
            "create one common large drainage pathway when bilateral extensive disease or revision "
            "anatomy requires it. Danger structures: anterior ethmoidal artery, skull base/anterior "
            "cranial fossa, and orbit, all converging in this narrow corridor. Failure mode: "
            "defaulting to the most extended procedure as a mark of surgical aggressiveness rather "
            "than matching extent to what the anatomy and disease actually require -- unnecessary "
            "extension adds risk and increases the raw bony surface area prone to restenosis without "
            "added benefit. Postoperative plan: frequent early debridement is critical for frontal "
            "recess procedures specifically, since this corridor scars and restenoses more readily "
            "than other sinus openings."
        ),
    },
    "Juvenile Nasopharyngeal Angiofibroma": {
        "recognize": (
            "The classic phenotype is an adolescent male with recurrent, often significant epistaxis "
            "and progressive unilateral nasal obstruction; a hypervascular nasopharyngeal mass on "
            "exam or imaging in this demographic should be treated as juvenile nasopharyngeal "
            "angiofibroma (JNA) until proven otherwise."
        ),
        "localize": (
            "JNA classically originates near the sphenopalatine foramen/pterygopalatine fossa and can "
            "extend into the nasal cavity, maxillary sinus, pterygopalatine and infratemporal fossae, "
            "orbit, and skull base/cavernous sinus; staging systems grade extent specifically by which "
            "of these compartments are involved, since that dictates both operability and the vessels "
            "at risk."
        ),
        "operate": (
            "Indication: confirmed JNA causing symptoms or growth; biopsy is generally avoided given "
            "hemorrhage risk once imaging (contrast CT/MRI showing the characteristic hypervascular "
            "mass with pterygopalatine fossa widening/anterior bowing of the posterior maxillary "
            "sinus wall) is diagnostic. Setup: preoperative angiography with embolization of feeding "
            "vessels (typically internal maxillary artery branches) 24-48 hours before resection "
            "substantially reduces intraoperative blood loss. Key steps: endoscopic or open "
            "resection (approach chosen by stage/extent) working to control the vascular pedicle "
            "early and removing the tumor from its origin at the sphenopalatine foramen/pterygopalatine "
            "fossa outward. Danger structures: internal carotid artery and optic nerve for "
            "skull-base-extending disease, and the significant vascularity of the tumor itself, which "
            "is the dominant intraoperative hazard at every stage. Failure mode: attempting biopsy or "
            "instrumentation before diagnostic imaging confirms JNA -- placing an instrument into an "
            "unrecognized angiofibroma risks severe, hard-to-control hemorrhage. Postoperative plan: "
            "surveillance imaging for recurrence, which is more likely with more extensive/skull-base "
            "involving disease and incomplete resection."
        ),
    },
}

STRIP_PREFIX_ONLY = {
    "Recurrent Acute Rhinosinusitis": B1,
    "Sphenoidotomy": B1,
    "Odontogenic Sinusitis": B2,
    "Endoscopic CSF Leak Repair / Nasoseptal Flap": B2,
}


def apply_depth_content_rhinology_v395(data_module):
    modules = {m.get("topic"): m for m in data_module.DEEP_MODULES_V6.get(DOMAIN, [])}
    missing = [t for t in list(FULL_REWRITES) + list(STRIP_PREFIX_ONLY) if t not in modules]
    if missing:
        raise RuntimeError(f"v39.5: expected {DOMAIN} topics not found: {missing}")
    for topic, fields in FULL_REWRITES.items():
        modules[topic].update(fields)
    for topic, prefix in STRIP_PREFIX_ONLY.items():
        mod = modules[topic]
        op = mod.get("operate") or ""
        if prefix in op:
            mod["operate"] = op.replace(prefix, "", 1)
    return {"enriched": list(FULL_REWRITES) + list(STRIP_PREFIX_ONLY)}
