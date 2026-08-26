"""v21.3 — deliberate learning-ladder curation, Rhinology pass 8.

Closes five high-confidence remaining canonical concepts. Strong v14.x cases are
reused as application layers. New questions supply recognition foundations and
senior/chief decisions without duplicating the application decision axis.
"""
DOMAIN = "Rhinology / Allergy / Skull Base"

REUSED_APPLICATION_IDS_V213 = {
    "v144_rh_12": "Mucocele",
    "v141_rhi_04": "Sinonasal Inverted Papilloma",
    "v141_rhi_05": "Intracranial Complications of Sinusitis",
    "v141_rhi_06": "Juvenile Nasopharyngeal Angiofibroma",
    "v143_rhi_05": "Odontogenic Sinusitis",
}


def _q(qid, topic, stage, stem, choices, answer, explanation, why_wrong,
       pearl, curveball, focus="boards"):
    return {
        "id": qid, "domain": DOMAIN, "topic": topic,
        "learning_stage": stage, "stem": stem, "choices": choices,
        "answer": answer, "explanation": explanation, "why_wrong": why_wrong,
        "board_pearl": pearl, "curveball": curveball,
        "tier": "Curated learning ladder", "mode": "Vignette",
        "focus": focus, "ladder_reviewed": True,
    }


VIGNETTES_V213 = [
    _q(
        "v213_rhi_mucocele_found", "Mucocele", "foundation",
        "Years after frontal sinus surgery, a patient develops slowly progressive frontal pressure and unilateral proptosis. CT shows an expansile, smoothly marginated frontal sinus lesion with bony remodeling rather than an infiltrative destructive mass. What diagnosis best fits?",
        ["Frontal sinus mucocele", "Acute invasive fungal rhinosinusitis", "Allergic rhinitis", "Juvenile nasopharyngeal angiofibroma"], 0,
        "A mucocele is an epithelium-lined, mucus-filled expansile sinus lesion caused by obstructed drainage. Chronic pressure produces smooth expansion and bony remodeling and can displace the orbit or skull base.",
        ["Correct. Prior surgery, slow expansion, and smooth bony remodeling are classic for a mucocele.", "Invasive fungal disease has a high-risk host, rapid tempo, tissue ischemia or invasion, and a very different emergency phenotype.", "Allergic rhinitis does not create an expansile frontal sinus mass with orbital displacement.", "JNA occurs in a characteristic adolescent male demographic and arises from the posterior nasal cavity rather than as a postoperative frontal sinus cystic lesion."],
        "Think obstruction plus expansion: a mucocele behaves like a slowly enlarging pressure lesion, not an infiltrative tumor.",
        "Which orbital or intracranial symptoms would make decompression urgent?",
        "boards",
    ),
    _q(
        "v213_rhi_mucocele_snr", "Mucocele", "senior_decision",
        "A symptomatic frontal mucocele extends far lateral over the orbit after prior frontal surgery. The medial frontal drainage pathway is scarred and a standard endoscopic corridor will not safely reach the lateral compartment. What is the best senior planning principle?",
        ["Force a purely endoscopic approach regardless of access", "Choose the least morbid approach that can completely marsupialize the lesion and create durable drainage, adding trephination or a combined corridor when lateral anatomy makes standard endoscopy inadequate", "Perform radiation therapy", "Observe because all mucoceles remain benign"], 1,
        "The treatment goal is durable drainage of the obstructed sinus while protecting orbit and skull base. Most mucoceles are amenable to endoscopic marsupialization, but extreme lateral frontal location, unfavorable postoperative anatomy, or inaccessible compartments can justify a combined or external adjunct rather than unsafe persistence with one corridor.",
        ["A route is only useful if it permits safe, durable access to the entire obstructed compartment.", "Correct. Approach selection follows lesion location and the ability to establish lasting drainage, not ideology about endoscopic purity.", "Radiation does not correct a mucus-retention lesion caused by blocked sinus ventilation.", "Benign pathology does not eliminate the need to treat progressive orbital, neurologic, or symptomatic mass effect."],
        "For a frontal mucocele, the operation is successful when the cavity can stay ventilated—not when the surgeon proves one approach is always enough.",
        "How would a posterior-table defect or active CSF leak change reconstruction planning?",
        "OR_prep",
    ),

    _q(
        "v213_rhi_ip_found", "Sinonasal Inverted Papilloma", "foundation",
        "An adult has persistent unilateral nasal obstruction. Endoscopy shows a unilateral papillomatous mass, and MRI demonstrates a convoluted cerebriform pattern. Which diagnosis should be strongly suspected?",
        ["Sinonasal inverted papilloma", "Diffuse allergic polyposis", "Acute bacterial rhinosinusitis", "Rhinitis medicamentosa"], 0,
        "Inverted papilloma is a benign but locally aggressive Schneiderian papilloma that typically presents as unilateral disease. A cerebriform imaging pattern and focal hyperostosis at an attachment site are useful clues; recurrence and synchronous or metachronous squamous carcinoma are important concerns.",
        ["Correct. Unilateral papillomatous disease with a cerebriform imaging pattern is classic for inverted papilloma.", "Inflammatory polyposis is usually bilateral and diffuse rather than a focal unilateral attachment-oriented lesion.", "ABRS is an acute infectious syndrome and does not produce this chronic papillomatous mass pattern.", "Rhinitis medicamentosa causes rebound mucosal congestion after topical decongestant overuse, not a focal tumor."],
        "A unilateral polypoid mass should earn the diagnosis of inflammation; inverted papilloma is one of the reasons.",
        "What CT finding can help predict the tumor's attachment site?",
        "boards",
    ),
    _q(
        "v213_rhi_ip_snr", "Sinonasal Inverted Papilloma", "senior_decision",
        "An inverted papilloma arises from the frontal sinus and extends lateral to the orbit. Imaging suggests a discrete attachment on the far lateral frontal sinus floor. What is the best senior operative principle?",
        ["Debulk the visible intranasal component and leave the attachment untreated", "Select an access strategy—extended endoscopic, trephine-assisted, or combined—that permits direct treatment of the attachment and underlying bone while preserving orbit and skull base", "Treat with antibiotics alone", "Avoid pathologic review because the lesion is benign"], 1,
        "Recurrence risk is driven heavily by failure to identify and treat the attachment. Frontal sinus disease is an access problem: the correct corridor is the one that permits direct attachment-oriented resection without unacceptable orbital or skull-base morbidity.",
        ["Bulk removal without attachment control is the classic setup for recurrence.", "Correct. The attachment dictates the required access and may justify a combined corridor when anatomy is lateral or otherwise inaccessible.", "Antibiotics do not eradicate a Schneiderian papilloma.", "Inverted papilloma has an association with squamous carcinoma, so complete pathologic evaluation remains important."],
        "For inverted papilloma, the visible tumor is the map; the attachment is the target.",
        "How would synchronous squamous carcinoma change margins, staging, and adjuvant planning?",
        "OR_prep",
    ),

    _q(
        "v213_rhi_ic_found", "Intracranial Complications of Sinusitis", "foundation",
        "A teenager with frontal sinusitis develops severe progressive headache, vomiting, fever, and a new focal neurologic deficit. What is the safest interpretation?",
        ["Possible intracranial extension such as epidural or subdural empyema that requires urgent imaging and escalation", "Routine sinus pressure", "Allergic rhinitis", "Isolated septal deviation"], 0,
        "Neurologic findings, meningismus, altered mental status, seizures, or severe progressive headache in sinusitis are red flags for intracranial spread. Frontal disease can produce epidural or subdural empyema, meningitis, brain abscess, or venous sinus complications.",
        ["Correct. A focal neurologic deficit changes the problem from uncomplicated sinusitis to a potentially life-threatening intracranial infection.", "Routine sinonasal pressure does not explain focal neurologic dysfunction or systemic deterioration.", "Allergic rhinitis does not produce intracranial suppurative complications.", "A septal deviation cannot account for this acute neurologic infectious syndrome."],
        "Sinusitis plus a neurologic deficit is not a stronger sinus headache; it is an intracranial-complication problem until proven otherwise.",
        "Which venous sinus complication is especially associated with sphenoid or posterior ethmoid infection?",
        "overnight_call",
    ),
    _q(
        "v213_rhi_ic_snr", "Intracranial Complications of Sinusitis", "senior_decision",
        "A patient with frontal sinusitis has a subdural empyema and early cerebritis. Neurosurgery is preparing urgent drainage. What is the best ENT-level source-control principle?",
        ["Defer all sinus treatment because neurosurgical drainage alone always eliminates the source", "Coordinate timely treatment of the involved sinonasal source with neurosurgery and infectious disease while broad IV antimicrobials and intracranial drainage proceed", "Use intranasal steroid alone", "Wait for neurologic recovery before addressing the sinus disease"], 1,
        "Intracranial drainage and antimicrobial therapy treat the life-threatening extension, but persistent infected sinonasal disease can continue to seed the complication. Management is multidisciplinary and often includes contemporaneous or closely coordinated sinus source control based on stability and anatomy.",
        ["Ignoring an active sinonasal source risks ongoing contamination or recurrence.", "Correct. Intracranial and sinonasal source control are complementary parts of the same infection pathway.", "Topical anti-inflammatory therapy is not adequate treatment for a subdural empyema.", "Delaying source control solely until neurologic recovery can permit continued infection when operative treatment is otherwise feasible."],
        "For complicated sinusitis, treat both ends of the pathway: the intracranial consequence and the sinonasal source.",
        "When might frontal trephination or an external adjunct be needed despite endoscopic sinus surgery?",
        "overnight_call",
    ),

    _q(
        "v213_rhi_jna_found", "Juvenile Nasopharyngeal Angiofibroma", "foundation",
        "A 15-year-old boy has progressive unilateral nasal obstruction and recurrent brisk epistaxis. CT shows an avidly enhancing posterior nasal cavity mass expanding the sphenopalatine foramen and pterygopalatine fossa. What is the most likely diagnosis?",
        ["Juvenile nasopharyngeal angiofibroma", "Antrochoanal polyp", "Allergic rhinitis", "Septal hematoma"], 0,
        "JNA classically occurs in adolescent males and presents with recurrent epistaxis and nasal obstruction. It arises near the sphenopalatine foramen and can extend into the pterygopalatine and infratemporal fossae; diagnosis is usually made from the characteristic demographic and imaging pattern rather than routine office biopsy.",
        ["Correct. The demographic, bleeding history, vascular enhancement, and pterygopalatine extension are classic for JNA.", "An antrochoanal polyp is not typically a highly vascular recurrent-epistaxis lesion with this skull-base extension pattern.", "Allergic rhinitis causes diffuse mucosal symptoms rather than a hypervascular posterior nasal mass.", "Septal hematoma follows trauma and arises from the septum, not the sphenopalatine region."],
        "Teenage boy plus recurrent epistaxis plus a hypervascular posterior nasal mass is JNA until imaging proves otherwise.",
        "Why is routine office biopsy usually avoided?",
        "boards",
    ),
    _q(
        "v213_rhi_jna_snr", "Juvenile Nasopharyngeal Angiofibroma", "senior_decision",
        "A large JNA extends through the pterygopalatine fossa into the infratemporal fossa with skull-base contact. The patient is stable and surgery is planned. What is the best senior preoperative framework?",
        ["Proceed directly to resection without vascular planning", "Map arterial supply and extent, consider preoperative embolization when appropriate, plan an approach that controls the vascular pedicle early, and counsel about skull-base, orbital, cranial-nerve, and transfusion risks", "Biopsy repeatedly until the lesion shrinks", "Treat with long-term oral antibiotics"], 1,
        "Large JNAs are vascular-anatomy operations. Cross-sectional imaging and angiographic assessment can define feeding vessels and dangerous collaterals; selective preoperative embolization is often used to reduce blood loss, while surgical corridor selection follows lateral and skull-base extension.",
        ["Unplanned entry into a highly vascular tumor can cause major hemorrhage and poor visualization.", "Correct. Senior preparation is about vascular control, extent, collateral anatomy, and access before the first incision.", "Repeated biopsy adds bleeding risk and does not treat the tumor.", "Antibiotics do not treat a benign vascular neoplasm."],
        "With JNA, the operation starts before the OR: understand the feeders, the extensions, and where you will gain control.",
        "Which external-carotid to ophthalmic or intracranial anastomoses can make embolization dangerous?",
        "OR_prep",
    ),

    _q(
        "v213_rhi_odont_found", "Odontogenic Sinusitis", "foundation",
        "An adult has unilateral foul-smelling maxillary drainage and facial pressure. CT shows unilateral maxillary opacification centered around a diseased maxillary molar with a periapical lucency. What diagnosis best fits?",
        ["Odontogenic sinusitis", "Diffuse allergic rhinitis", "Vestibular migraine", "Juvenile nasopharyngeal angiofibroma"], 0,
        "Odontogenic sinusitis should be suspected in unilateral maxillary-predominant disease, especially with foul drainage, dental symptoms or procedures, periapical disease, oroantral communication, or adjacent dental pathology on CT.",
        ["Correct. The unilateral maxillary distribution plus a clear dental source is the defining pattern.", "Allergic disease is usually bilateral and does not explain a focal periapical source.", "Migraine can mimic facial pressure but does not produce unilateral purulent sinus disease with dental pathology.", "JNA occurs in adolescent males and presents as a hypervascular posterior nasal mass rather than dental-source maxillary infection."],
        "Unilateral maxillary sinusitis deserves a dental history and a deliberate look at the tooth roots on CT.",
        "Which dental procedures can create an oroantral communication and change source-control planning?",
        "boards",
    ),
    _q(
        "v213_rhi_odont_snr", "Odontogenic Sinusitis", "senior_decision",
        "A patient has persistent odontogenic maxillary and anterior ethmoid sinusitis plus an oroantral fistula after molar extraction. Antibiotics repeatedly improve symptoms but disease recurs. What is the best senior management principle?",
        ["Continue antibiotics indefinitely without correcting the source", "Coordinate definitive dental/fistula source control with endoscopic treatment of the obstructed diseased sinus pathway when both components require intervention", "Perform frontal sinus obliteration", "Treat with biologic therapy as first-line because all CRS is inflammatory"], 1,
        "Durable treatment requires elimination of the dental source. When infection has extended beyond the tooth into persistently obstructed sinonasal compartments, coordinated dental and rhinologic treatment can be necessary; sequencing depends on fistula, dental procedure, disease extent, and local expertise.",
        ["Antibiotics suppress the bacterial burden temporarily but cannot close a fistula or remove a persistent dental nidus.", "Correct. Source control and restoration of sinus drainage address both mechanisms maintaining the infection.", "Frontal obliteration is unrelated to a maxillary dental-source process unless separate frontal disease independently warrants treatment.", "Biologic therapy does not correct an oroantral fistula or an infected dental source."],
        "Odontogenic sinusitis fails when only one side of the tooth-sinus problem is treated.",
        "How does a displaced dental implant or foreign body within the maxillary sinus alter the operative plan?",
        "OR_prep",
    ),
]


def apply_learning_ladders_v213(challenges, item_id_fn):
    by_id = {q.get("id"): q for q in challenges if q.get("id")}
    touched = []
    for qid, topic in REUSED_APPLICATION_IDS_V213.items():
        q = by_id.get(qid)
        if q:
            q["topic"] = topic
            q["learning_stage"] = "application"
            q["ladder_reviewed"] = True
            q["concept_id"] = item_id_fn(DOMAIN, topic)
            touched.append(qid)
    existing = {q.get("id") for q in challenges}
    added = []
    for q in VIGNETTES_V213:
        if q["id"] not in existing:
            q["concept_id"] = item_id_fn(DOMAIN, q["topic"])
            challenges.append(q)
            existing.add(q["id"])
            added.append(q["id"])
    return {"reviewed_topics": 5, "reused": touched, "added": len(added), "ids": added}
