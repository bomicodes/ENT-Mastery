"""v20.22 — deepen exact-live Pediatric Otolaryngology Lymphatic Malformation.

Durable anatomy, airway and operative principles are cross-referenced against the
connected Cummings 7e, Pasha 6e and K.J. Lee 12e corpus. Management is updated
against the ISSVA 2025 classification, current FDA alpelisib/PROS indication and
contemporary head-and-neck LM literature.
"""
from concept_check_board_repair_v177 import _find_module

QIDS = ("cc-v112-rec-pediatric-otolaryngology-lymphatic-malformation",)
CID = "v6-pediatric-otolaryngology-lymphatic-malformation"
TOPIC = "Lymphatic Malformation"

SOURCE_REFS_V222 = [
    {"type":"textbook","citation":"Cummings Otolaryngology: Head and Neck Surgery, 7th ed. (2021), connected Google Drive corpus, compressed copy Drive id 18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t; pediatric cervical masses/vascular anomalies and airway/operative principles cross-referenced 2026-09-09.","role":"durable foundation: trans-spatial lymphatic-malformation anatomy, presentation, airway risk, imaging, sclerotherapy/surgery principles and complication avoidance"},
    {"type":"textbook","citation":"Pasha R, Golub JS. Otolaryngology-Head and Neck Surgery: Clinical Reference Guide, 6th ed. (2022), connected Google Drive copy Drive id 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52; pediatric neck mass and vascular-malformation framework cross-referenced 2026-09-09.","role":"resident/board framework: differential, clinical behavior, imaging, observation, sclerotherapy and operative selection"},
    {"type":"textbook","citation":"K.J. Lee's Essential Otolaryngology: Head & Neck Surgery, 12th ed. (2019), connected Google Drive copy Drive id 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR; pediatric head/neck mass and vascular-malformation principles cross-referenced 2026-09-09.","role":"operative cross-check: congenital neck-mass anatomy, airway relationships, treatment goals and morbidity tradeoffs"},
    {"type":"classification","citation":"ISSVA Classification & Glossary for Vascular Anomalies, 2025, International Society for the Study of Vascular Anomalies; official classification page reviewed 2026-09-09.","role":"current terminology/classification: vascular malformation framework and modern molecular classification"},
    {"type":"regulatory","citation":"U.S. FDA. Vijoice (alpelisib): treatment of adults and children age 2 years and older with severe manifestations of PIK3CA-Related Overgrowth Spectrum (PROS) requiring systemic therapy; current FDA accelerated-approval listing reviewed 2026-09-09.","role":"regulatory boundary: alpelisib is not an FDA indication for every lymphatic malformation; candidate selection requires the appropriate PIK3CA-related systemic-therapy context"},
    {"type":"prospective_evidence","citation":"Wenger TL, et al. Alpelisib for the treatment of PIK3CA-related head and neck lymphatic malformations and overgrowth. Genet Med. 2022;24(11):2318-2328. PMID: 36066547.","role":"targeted-therapy evidence: prospective pediatric head/neck PIK3CA-associated LM/overgrowth cohort with lesion and functional improvement"},
    {"type":"systematic_review","citation":"Alqutub A, et al. Sclerotherapy vs surgical excision for lymphatic malformations of the head and neck: a systematic review and meta-analysis. Eur Arch Otorhinolaryngol. 2024;281(11):5571-5617. PMID: 38951201.","role":"current procedural evidence: response varies by macro/microcystic/mixed morphology; no one procedure fits every lesion"},
    {"type":"systematic_review","citation":"Sirolimus treatment for paediatric head and neck lymphatic malformations: a systematic review. Int J Pediatr Otorhinolaryngol. 2023. PMID: 37115326.","role":"systemic-therapy evidence boundary: sirolimus can help selected complex LM but evidence quality and adverse-effect monitoring limit blanket use"},
]

PROMPT = """A 3-year-old with a known trans-spatial cervicofacial lymphatic malformation presents after a viral illness with rapid enlargement, pain, dysphagia and new noisy breathing. MRI previously showed mixed macro- and microcystic disease extending through the submandibular space and tongue base. As the senior pediatric ENT resident, explain the immediate airway and acute-flare priorities; how current lymphatic-malformation classification, cyst morphology, anatomic extent and symptoms guide observation, sclerotherapy, surgery or systemic therapy; what makes tongue-base/pharyngeal disease and post-sclerotherapy swelling dangerous; and when PIK3CA testing or targeted therapy changes management. Include specific rescue, stop/stage and counseling decisions?"""

ANSWER = """Foundation — a lymphatic malformation is a low-flow vascular malformation, not a neoplasm and not simply a 'cystic hygroma.' Head-and-neck lesions can cross fascial spaces, insinuate around nerves and vessels, involve the floor of mouth, tongue, pharynx or larynx, and change dramatically with infection, inflammation or intralesional hemorrhage. Current ISSVA terminology should be used rather than outdated tumor language. Morphology is clinically useful: macrocystic disease contains larger drainable cysts, microcystic disease is infiltrative with many small channels, and mixed lesions contain both. The label predicts treatment behavior but does not replace an anatomic and functional map.

Immediate priority — the child with rapid enlargement, dysphagia and new noisy breathing is first an airway patient. Assess work of breathing, stridor/stertor, voice/cry, secretion handling, oxygenation and progression. Examine the oral cavity and floor of mouth and use flexible nasopharyngolaryngoscopy when it can be performed safely to define tongue-base, pharyngeal and laryngeal narrowing. Do not send a tenuous child away for a perfect MRI before securing a deteriorating airway. Escalate early to pediatric anesthesia/PICU and the vascular-anomalies team. If ventilation or intubation becomes unsafe, use the institution's difficult-airway pathway and prepare a surgical airway rescue appropriate to the child's anatomy rather than repeating traumatic attempts through a progressively narrowed upper airway.

Acute inflammatory or hemorrhagic flare — infection, viral inflammation and bleeding into cysts can abruptly increase lesion volume. Treat a true bacterial infection when supported clinically; provide hydration, analgesia and anti-inflammatory support while monitoring the airway. A hemorrhagic cyst can be painful and rapidly enlarging without bacterial infection. The resident should not reflexively aspirate or incise every enlarging LM: uncontrolled procedures can bleed, infect the lesion, injure traversing structures and offer only transient decompression. Drainage or urgent image-guided intervention is selected when anatomy, airway compromise or a dominant accessible cyst makes decompression beneficial and the procedure can be controlled.

Imaging and map — ultrasound can characterize superficial cystic spaces and guide procedures, but MRI is the workhorse for defining deep trans-spatial extent, macro/microcystic components and relationships to tongue, pharynx, orbit, parotid, neurovascular structures and mediastinum. CT is useful selectively when speed, airway instability, acute hemorrhage, calcification/bone detail or another diagnosis makes it preferable. Imaging is not an excuse to delay airway rescue. Before any definitive intervention, know whether the lesion is circumscribed enough to treat as a target or infiltrative enough that the treatment goal must be symptom/function control rather than complete eradication.

Observation — an asymptomatic or minimally symptomatic lesion with stable function can be observed, especially when intervention would create more morbidity than the malformation. Observation is active: families need a flare plan and follow-up for growth, pain, recurrent infection/bleeding, dysphagia, speech effects, sleep-disordered breathing, cosmetic burden and psychosocial impact. Growth or a new symptom changes the risk-benefit calculation; 'congenital' does not mean harmless, and 'benign' does not mean intervention-free.

Sclerotherapy — image-guided sclerotherapy is commonly first-line procedural therapy for accessible macrocystic components because they can be aspirated and exposed to a sclerosant. Results are less predictable in diffuse microcystic disease, although specialized techniques and multimodal treatment can still help. Choice of sclerosant belongs to an experienced vascular-anomalies/interventional-radiology team because agents differ in inflammatory swelling, nerve/skin toxicity, pulmonary risk and local practice. The senior ENT role is especially important when the lesion is in the tongue, floor of mouth, pharynx or upper airway: post-sclerotherapy edema can transiently make the airway much worse even when the treatment is ultimately effective. Plan airway protection, observation level and rescue before injecting—not after swelling develops.

Surgery — surgery is appropriate when a discrete or surgically favorable component causes important functional/cosmetic morbidity, when residual disease after other therapy has a correctable anatomic target, when tissue diagnosis is needed because the diagnosis is uncertain, or when urgent decompression/control cannot otherwise be achieved. Complete excision is not always the goal. Diffuse microcystic LM may encase the facial, hypoglossal, lingual or other nerves, salivary structures and major vessels; chasing microscopic disease can create paralysis, dysphagia, hemorrhage or disfigurement. A planned subtotal/debulking operation may be the expert choice when it relieves airway, swallowing or bulk morbidity while preserving critical structures. Stop rather than converting symptom-control surgery into an uncontrolled nerve or vessel sacrifice for the sake of an imaging endpoint.

Macro versus micro versus mixed — macrocystic lesions generally respond better to percutaneous sclerotherapy; microcystic disease is more infiltrative and often needs multimodal therapy; mixed disease should be decomposed into treatable components rather than assigned one modality globally. The 2024 systematic review/meta-analysis reinforces that response differs by morphology and that both sclerotherapy and surgery have roles. It should not be misread as a mandate that every lesion be excised or that one sclerosant is universally superior, because anatomy, functional risk, treatment definitions and study heterogeneity matter.

Systemic therapy — sirolimus, an mTOR inhibitor, is used off-label in selected extensive, symptomatic or refractory lymphatic/combined vascular malformations when local therapy is inadequate or excessively morbid. It is not a casual first-line medication for a small asymptomatic macrocyst. Treatment requires a vascular-anomalies team and monitoring for immunosuppression/infection, mucositis, cytopenias, lipid abnormalities and other toxicities. The pediatric head-and-neck systematic review is encouraging but emphasizes limited high-quality evidence, so teach individualized risk-benefit selection rather than a universal regimen.

PIK3CA and alpelisib — somatic PIK3CA pathway mutations explain an important subset of lymphatic malformations and PIK3CA-related overgrowth phenotypes. Consider lesional molecular testing when severe, extensive, atypical or refractory disease may change systemic-therapy options; blood testing can be falsely negative for mosaic disease. Alpelisib is a PI3K-alpha inhibitor with prospective evidence of benefit in children with PIK3CA-associated head-and-neck LM/overgrowth. The FDA regulatory boundary matters: Vijoice is approved for adults and children age 2 years and older with severe manifestations of PIK3CA-Related Overgrowth Spectrum requiring systemic therapy. That is not the same statement as 'alpelisib is FDA-approved for all lymphatic malformations.' A child with isolated LM needs appropriate phenotype/genotype and specialist assessment before extrapolating the PROS indication.

Airway-specific planning — oral tongue, floor-of-mouth, base-of-tongue, pharyngeal and laryngeal involvement can produce chronic sleep obstruction or acute airway compromise during a flare or after treatment. Preoperative endoscopic airway mapping can change where and how treatment is delivered. A lesion that looks modest externally can be dangerous internally. For a procedure expected to swell a narrow tongue base, discuss elective intubation, delayed extubation and PICU observation in advance. If the child cannot safely be extubated because of edema or residual obstruction, maintaining the airway is not a treatment failure; premature extubation can be catastrophic.

Hemorrhage and infection danger zones — rapid expansion after trauma or spontaneously may represent intralesional hemorrhage. Obtain blood counts/coagulation testing when clinically indicated and define whether the child is stable before intervention. Significant systemic infection, cellulitis or abscess-like complication requires antimicrobial/source-control reasoning, but routine antibiotics do not shrink sterile LM inflammation. Avoid blind transoral incision into a vascular-anomaly field. If airway deterioration, uncontrolled bleeding, sepsis or a threatened neurovascular structure emerges, stabilize that threat first and defer elective lesion-reduction goals.

Recurrence and counseling — recurrence or residual disease is common because diffuse LM rarely respects surgical planes. Set goals in terms of breathing, swallowing, speech, pain, infection/bleeding frequency, sleep, function and appearance rather than promising radiographic eradication. Families should understand that several staged sclerotherapy sessions, selective surgery and/or systemic therapy may be needed. Treatment changes as the child grows and as molecular options evolve.

Senior synthesis — make seven decisions: AIRWAY: is this stable, threatened or already failing? FLARE: infection, hemorrhage or sterile inflammation? MAP: which spaces and upper-airway structures are involved? MORPHOLOGY: macro-, micro- or mixed cystic disease? GOAL: observation versus symptom/function control versus a discrete correctable target? MODALITY: sclerotherapy, surgery, systemic therapy or a staged combination? GENETICS: would PIK3CA/other molecular testing change systemic therapy? The expert does not chase every cyst. The expert protects the airway and neurovascular function, targets the component most responsible for morbidity, anticipates treatment-induced swelling and changes course when the intervention becomes more dangerous than the malformation."""

TRAPS = [
    "Calling a lymphatic malformation a lymphangioma/cystic-hygroma tumor and missing the modern ISSVA low-flow vascular-malformation framework.",
    "Being reassured by a small external neck component while unrecognized tongue-base or pharyngeal disease narrows the airway internally.",
    "Sending a child with progressive stridor and secretion intolerance for lengthy imaging before organizing definitive airway rescue.",
    "Assuming rapid painful enlargement is always bacterial infection; intralesional hemorrhage and sterile inflammatory flares can produce the same dramatic volume change.",
    "Blindly incising or aspirating an enlarging lesion without defining anatomy, bleeding risk and whether a controlled image-guided target actually exists.",
    "Treating all LMs as equivalent and ignoring the major treatment-behavior difference between macro-, microcystic and mixed morphology.",
    "Planning sclerotherapy in a tongue/floor-of-mouth/pharyngeal lesion without planning for predictable post-treatment edema and a higher level of airway observation.",
    "Chasing complete excision through an infiltrative microcystic lesion when symptom-control debulking would preserve cranial nerves, vessels and swallowing function.",
    "Calling residual disease after a function-preserving operation a surgical failure when eradication would require unacceptable morbidity.",
    "Using sirolimus as routine first-line therapy for a small asymptomatic LM rather than reserving systemic therapy for appropriately selected complex disease.",
    "Calling sirolimus risk-free because it is commonly used in vascular anomalies; immunologic, mucosal, hematologic and metabolic toxicities require monitoring.",
    "Equating a negative blood PIK3CA test with absence of a mosaic lesional mutation when molecular confirmation could change systemic treatment.",
    "Teaching that Vijoice/alpelisib is FDA-approved for every LM; the FDA indication is severe PIK3CA-Related Overgrowth Spectrum requiring systemic therapy in patients age 2 years and older.",
    "Using an FDA PROS indication as a substitute for multidisciplinary phenotype/genotype confirmation and individualized targeted-therapy counseling.",
    "Prematurely extubating after airway-adjacent sclerotherapy or debulking because the procedure is finished despite expected edema and a marginal preoperative airway.",
    "Defining success only by MRI volume rather than airway, swallowing, speech, pain, bleeding/infection burden, sleep and family-centered function.",
]

COHORT = {QIDS[0]: {
    "concept_id": CID,
    "canonical_topic": TOPIC,
    "prompt": PROMPT,
    "answer_text": ANSWER,
    "explanation": "Head-and-neck lymphatic-malformation care starts with airway/function and a morphology/anatomy map. Observe low-morbidity disease; target accessible macrocysts with image-guided therapy, use surgery selectively when anatomy and goals justify it, and reserve systemic/molecular therapy for appropriate complex disease while anticipating treatment-induced airway swelling.",
    "board_pearl": "For a tongue-base or pharyngeal LM, the most dangerous time may be during an inflammatory/hemorrhagic flare or after sclerotherapy-induced edema. Secure the airway plan first; then treat the component causing morbidity rather than chasing radiographic eradication.",
    "depth_layers_v222": {
        "foundation":"ISSVA terminology, low-flow LM biology, macro/micro/mixed morphology, trans-spatial anatomy and infection/hemorrhage-related expansion.",
        "application":"Airway mapping, MRI/ultrasound selection, observation versus sclerotherapy versus surgery, post-treatment edema planning and function-centered outcomes.",
        "senior_decision":"Rescue a threatened airway, stop function-destructive excision, choose systemic therapy for complex disease, and apply PIK3CA/alpelisib only within the correct molecular and regulatory context."
    },
    "common_traps_v222": TRAPS,
    "deliberate_review_v222": "Selected from the exact successful v20.21 production backlog by clinical priority rather than lexical rank. The live answer was 17 words and omitted pediatric airway rescue, flare/hemorrhage reasoning, morphology-specific procedural selection, treatment-induced edema, function-preserving surgical bailout and the current PIK3CA/alpelisib indication boundary.",
    "source_refs_v222": SOURCE_REFS_V222,
    "evidence_distinction_v222": "Durable Cummings/Pasha/K.J. Lee anatomy, airway, imaging and function-preserving operative principles are retained. ISSVA 2025 supplies current terminology/classification. Contemporary procedural literature refines morphology-specific sclerotherapy-versus-surgery expectations. Sirolimus remains off-label with limited high-quality pediatric HNLM evidence. FDA Vijoice labeling is recorded narrowly: alpelisib is indicated for severe PIK3CA-Related Overgrowth Spectrum requiring systemic therapy in patients age 2 years and older, not generically for every LM; prospective PIK3CA-associated head/neck LM evidence is recorded separately from the regulatory indication.",
    "audit_profile_v222": "pediatric_lymphatic_malformation",
}}

def apply_concept_check_task_alignment_v222(checks, deep_modules, v6_item_id):
    by = {str(q.get("id") or ""): q for q in checks or []}
    repaired, missing, link_mismatch = [], [], []
    for qid, payload in COHORT.items():
        q = by.get(qid)
        if q is None:
            missing.append(qid); continue
        module = _find_module(q, deep_modules, v6_item_id)
        topic = str(module.get("topic") or "") if module else ""
        cid = v6_item_id(q.get("domain"), topic) if module and q.get("domain") else None
        if topic != payload["canonical_topic"] or cid != payload["concept_id"] or q.get("concept_id") != payload["concept_id"]:
            link_mismatch.append(qid); continue
        for key, value in payload.items():
            if key != "canonical_topic": q[key] = value
        q["topic"] = payload["canonical_topic"]
        q["concept_id"] = payload["concept_id"]
        q["choices"] = []
        q["answer"] = None
        q["task_alignment_v222"] = True
        repaired.append(qid)
    return {"repaired": repaired, "missing": missing, "link_mismatch": link_mismatch}
