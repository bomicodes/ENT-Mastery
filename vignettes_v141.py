"""v14.1 — second-case depth pass across Otology, Rhinology, Laryngology,
Sleep, Thyroid/Salivary and Facial Plastics. Targets common/high-consequence
singleton topics with a different decision axis from their first vignette.
"""


def Q(qid, domain, topic, stem, choices, answer, explanation, pearl, curveball, focus="boards"):
    return {
        "id": qid, "domain": domain, "topic": topic, "stem": stem,
        "choices": choices, "answer": answer, "explanation": explanation,
        "why_wrong": ["Compare this option with the management principle and anatomy in the explanation." for _ in choices],
        "board_pearl": pearl, "curveball": curveball, "focus": focus,
        "tier": "Curated chief/call/OR", "mode": "Vignette",
    }

OTO = "Otology / Neurotology"
RHI = "Rhinology / Allergy / Skull Base"
LAR = "Laryngology / Voice / Swallowing"
SLP = "Sleep Surgery"
TPS = "Thyroid / Parathyroid / Salivary"
FPT = "Facial Plastics / Trauma"

VIGNETTES_V141 = [
    # Otology
    Q("v141_oto_01", OTO, "BPPV",
      "A patient has brief vertigo when rolling right in bed. Right Dix-Hallpike produces torsional upbeating nystagmus after a short latency that fatigues. What is the best treatment?",
      ["Canalith repositioning maneuver for right posterior-canal BPPV", "Chronic meclizine", "MRI before treatment in every case", "Labyrinthectomy"], 0,
      "Classic posterior-canal BPPV is diagnosed at bedside and treated with a repositioning maneuver; routine imaging and chronic vestibular suppressants are unnecessary.",
      "The nystagmus direction localizes the canal; the maneuver should follow the canal involved.",
      "What nystagmus pattern on supine roll testing suggests horizontal-canal BPPV?"),

    Q("v141_oto_02", OTO, "Ménière Disease",
      "A patient with definite Ménière disease continues disabling vertigo despite diet/lifestyle counseling and maintenance therapy, but still has useful hearing in the affected ear. What escalation is most hearing-preserving?",
      ["Consider intratympanic steroid before destructive therapy", "Immediate labyrinthectomy", "Cochlear nerve section for every patient", "No further treatment"], 0,
      "For persistent attacks, intratympanic steroids can be used while preserving hearing; gentamicin and labyrinthectomy are more vestibulotoxic/destructive options for selected refractory disease.",
      "Escalate from nondestructive to destructive therapy according to vertigo burden and hearing value.",
      "How does nonserviceable hearing alter the role of labyrinthectomy?"),

    Q("v141_oto_03", OTO, "Vestibular Schwannoma",
      "A healthy 42-year-old has a 1.2-cm intracanalicular vestibular schwannoma, good hearing and minimal symptoms. Which management options are reasonable?",
      ["Observation with serial MRI, stereotactic radiation, or microsurgery depending on growth, hearing goals and patient factors", "Mandatory immediate translabyrinthine surgery", "Chemotherapy", "No follow-up"], 0,
      "Small vestibular schwannomas can be observed or treated; age, growth, hearing, tumor size and patient preference drive selection.",
      "The treatment question is not merely tumor control—it is tumor control plus hearing, facial function and lifetime surveillance burden.",
      "What documented interval growth would change the balance toward treatment?"),

    Q("v141_oto_04", OTO, "Cochlear Implant Candidacy",
      "An adult with bilateral severe sensorineural hearing loss has poor aided sentence recognition despite appropriately fitted hearing aids. What is the next step?",
      ["Refer for formal cochlear implant candidacy evaluation", "Increase hearing-aid gain indefinitely", "Stapedectomy", "No rehabilitation is available"], 0,
      "CI candidacy depends on aided speech performance, ear-specific hearing, medical/anatomic suitability and patient goals—not pure-tone threshold alone.",
      "When amplification is optimized but speech understanding remains poor, evaluate for implantation rather than simply making sounds louder.",
      "How do single-sided deafness and asymmetric hearing loss expand modern CI indications?"),

    Q("v141_oto_05", OTO, "Acute Mastoiditis / Petrous Apicitis",
      "A child with acute mastoiditis develops a lateral rectus palsy and deep retro-orbital pain. What complication should be suspected?",
      ["Petrous apicitis with Gradenigo syndrome", "BPPV", "Otosclerosis", "Patulous Eustachian tube"], 0,
      "Otitis/mastoid infection can extend to the petrous apex, classically producing otorrhea, deep facial/retro-orbital pain and abducens palsy.",
      "A cranial neuropathy changes uncomplicated mastoiditis into complicated temporal-bone infection requiring urgent imaging and escalation.",
      "What surgical drainage routes may be considered when medical therapy is insufficient?", "overnight_call"),

    Q("v141_oto_06", OTO, "CSF Otorrhea / Temporal Encephalocele",
      "An obese middle-aged patient has recurrent clear unilateral otorrhea through a tympanostomy tube and CT shows a tegmen defect. What is the best next step?",
      ["Confirm CSF with beta-2 transferrin/beta-trace testing and map the skull-base defect for repair", "Treat indefinitely as serous otitis", "Remove the tube and ignore recurrence", "Stapedectomy"], 0,
      "Spontaneous temporal-bone CSF leaks can masquerade as chronic effusion and carry meningitis risk; diagnosis requires fluid confirmation and anatomic localization.",
      "Adult unilateral 'effusion' that becomes continuous clear drainage after a tube deserves a CSF-leak differential.",
      "How do defect size/location and encephalocele influence transmastoid versus middle-fossa repair?", "OR_prep"),

    # Rhinology
    Q("v141_rhi_01", RHI, "Allergic Rhinitis",
      "A patient has seasonal sneezing, itching and watery rhinorrhea with pale edematous turbinates. Which is an appropriate first-line controller for persistent symptoms?",
      ["Intranasal corticosteroid with allergen avoidance and technique counseling", "Long-term oral antibiotics", "Routine ESS", "Systemic steroids indefinitely"], 0,
      "Intranasal corticosteroids are highly effective for persistent allergic rhinitis; antihistamines and other therapies are tailored to symptom pattern.",
      "Medication failure is often technique failure—watch the patient use the spray.",
      "When should allergy testing be added?"),

    Q("v141_rhi_02", RHI, "Allergen Immunotherapy — SCIT / SLIT",
      "A patient with confirmed grass allergy remains symptomatic despite appropriate medication and wants disease-modifying therapy. What is required before immunotherapy?",
      ["Confirm clinically relevant IgE sensitization and assess asthma/control and anaphylaxis risk", "No allergy testing", "Start SCIT during uncontrolled severe asthma", "Antibiotic prophylaxis"], 0,
      "SCIT and SLIT can reduce symptoms/medication use in selected allergic rhinitis patients; safety requires matching treatment to clinically relevant sensitization and asthma stability.",
      "Uncontrolled asthma is a major safety concern for systemic reactions to immunotherapy.",
      "What observation and epinephrine counseling differ between SCIT and SLIT?"),

    Q("v141_rhi_03", RHI, "CRSwNP",
      "A patient with prior ESS has rapidly recurrent bilateral polyps, asthma and NSAID-triggered bronchospasm. What phenotype should be recognized?",
      ["Aspirin-exacerbated respiratory disease", "Simple bacterial sinusitis", "JNA", "Septal hematoma"], 0,
      "AERD is the triad of asthma, CRSwNP and respiratory reactions to COX-1 inhibitors; recognition influences counseling about aspirin desensitization, biologics and recurrence risk.",
      "Polyps plus asthma should always trigger the NSAID reaction history.",
      "How do biologics versus aspirin desensitization fit into postoperative management?"),

    Q("v141_rhi_04", RHI, "Sinonasal Inverted Papilloma",
      "A unilateral papillomatous mass is attached to the lateral nasal wall and biopsy confirms inverted papilloma. What surgical principle reduces recurrence?",
      ["Identify and completely treat the site of attachment, including underlying bone when appropriate", "Simple polypectomy without attachment work", "Observe because malignant transformation never occurs", "Chemotherapy alone"], 0,
      "Inverted papilloma recurs when its attachment is not addressed and carries synchronous/metachronous SCC risk.",
      "The operation is attachment-oriented, not bulk-debulking oriented.",
      "How does frontal-sinus attachment change access planning?", "OR_prep"),

    Q("v141_rhi_05", RHI, "Intracranial Complications of Sinusitis",
      "A teenager with frontal sinusitis develops severe headache, vomiting and focal neurologic deficit. MRI shows a subdural empyema. What is the correct management?",
      ["Urgent multidisciplinary neurosurgical drainage, IV antibiotics and control of the sinonasal source", "Oral antibiotics at home", "Nasal steroid alone", "Observe until seizures occur"], 0,
      "Intracranial sinus complications are life-threatening and require rapid imaging, broad IV antimicrobials and source control with neurosurgery/ENT.",
      "Neurologic symptoms in sinusitis are never routine sinus pressure.",
      "What venous sinus complication can occur with sphenoid/ethmoid infection?", "overnight_call"),

    Q("v141_rhi_06", RHI, "Juvenile Nasopharyngeal Angiofibroma",
      "A teenage boy has recurrent brisk epistaxis and nasal obstruction. CT shows a hypervascular posterior nasal mass with pterygopalatine fossa extension. What should be avoided?",
      ["Routine office biopsy", "Preoperative angiographic evaluation", "Cross-sectional imaging", "Planning endoscopic or open resection by extent"], 0,
      "JNA is diagnosed by classic demographic and imaging features; biopsy can cause major hemorrhage because the tumor is highly vascular.",
      "Teenage boy + recurrent epistaxis + hypervascular posterior nasal mass = image first, do not biopsy reflexively.",
      "When and why is preoperative embolization considered?", "OR_prep"),

    # Laryngology
    Q("v141_lar_01", LAR, "Dysphagia / Aspiration",
      "A patient aspirates thin liquids before the swallow because of delayed pharyngeal initiation but handles thicker consistencies safely. What rehabilitation principle is most appropriate?",
      ["Use instrumental-study-guided compensatory strategy/diet modification while treating the underlying timing deficit", "Total laryngectomy for every aspiration event", "Ignore aspiration if silent", "Antibiotics prophylactically forever"], 0,
      "Aspiration timing identifies mechanism; treatment may include bolus modification, postural maneuvers, exercise and sensory strategies rather than one universal diet.",
      "Ask when aspiration happens—before, during or after the swallow—because the answer localizes the failure.",
      "How does aspiration after the swallow from residue change therapy?"),

    Q("v141_lar_02", LAR, "Subglottic / Tracheal Stenosis",
      "An adult has a short, thin web-like subglottic stenosis with no cartilage framework collapse. What treatment is most appropriate initially?",
      ["Endoscopic dilation/incision with adjuncts as appropriate", "Open tracheal resection for every stenosis", "Observation despite severe dyspnea", "Injection laryngoplasty"], 0,
      "Short simple stenoses may respond to endoscopic treatment; long, mature, cartilaginous or repeatedly recurrent stenoses may require open reconstruction/resection.",
      "Length, grade, cartilage integrity and recurrence history matter more than the label 'stenosis.'",
      "Which features make cricotracheal resection more appropriate?", "OR_prep"),

    Q("v141_lar_03", LAR, "Spasmodic Dysphonia",
      "A patient has task-specific strained voice breaks during voiced speech but improves when whispering or laughing. What is the standard first-line procedural therapy?",
      ["Targeted botulinum toxin injection for adductor spasmodic dysphonia", "Vocal-fold stripping", "Antibiotics", "Tracheostomy"], 0,
      "Spasmodic dysphonia is a focal laryngeal dystonia; botulinum toxin reduces pathologic muscle overactivity and is titrated to voice response.",
      "Task specificity helps distinguish dystonia from muscle tension dysphonia and tremor.",
      "Which muscles are typically targeted for abductor spasmodic dysphonia?"),

    Q("v141_lar_04", LAR, "Reinke Edema",
      "A smoker has a very low-pitched voice and bilateral polypoid swelling of the superficial lamina propria. What treatment principle is correct?",
      ["Smoking cessation and voice optimization are foundational; surgery is considered for persistent functional burden or airway concern", "Radiation therapy", "Antibiotics alone", "No need to inspect the larynx for coexistent lesions"], 0,
      "Reinke edema is strongly linked to smoking and phonotrauma; surgery can improve vibration but recurrence risk remains if irritants continue.",
      "Treat the behavior and the lesion; doing only one produces disappointing outcomes.",
      "How does severe bulky edema threatening the airway change timing?"),

    Q("v141_lar_05", LAR, "Benign Vocal Fold Lesions",
      "A singer has a unilateral translucent mid-membranous cyst with a focal absent mucosal wave and persistent dysphonia despite voice therapy. What is reasonable?",
      ["Microlaryngoscopic microflap excision with maximal preservation of the vocal-fold cover", "Wide cordectomy", "Radiation", "No intervention can help"], 0,
      "A true cyst often persists despite behavioral optimization and may require phonomicrosurgery; precise dissection limits scar.",
      "In benign vocal-fold surgery, the disease is small but the functional tissue is microscopic—preserve the superficial lamina propria.",
      "Why is postoperative voice rehabilitation important?", "OR_prep"),

    Q("v141_lar_06", LAR, "Cricopharyngeal Dysfunction",
      "An older patient has a prominent cricopharyngeal bar, significant pharyngeal residue and impaired UES opening on MBS. What treatment options can be considered after confirming the mechanism?",
      ["Dilation, botulinum toxin or cricopharyngeal myotomy depending on cause and durability needed", "Tonsillectomy", "Vocal-fold injection", "No treatment"], 0,
      "UES dysfunction treatment depends on whether the problem is hypertonicity, fibrosis, poor hyolaryngeal excursion or global pharyngeal weakness.",
      "A cricopharyngeal bar on imaging is not automatically the cause of dysphagia; correlate physiology and symptoms.",
      "When does poor pharyngeal propulsion predict limited benefit from myotomy?"),

    # Sleep
    Q("v141_slp_01", SLP, "Adult PSG Interpretation",
      "A PSG shows AHI 18/hour overall, AHI 52/hour supine, AHI 4/hour lateral, normal CO2 and mostly obstructive events. What phenotype is present?",
      ["Moderate positional OSA with marked supine dependence", "Central sleep apnea", "Sleep-related hypoventilation", "Normal study"], 0,
      "PSG interpretation should include event type, severity, position, REM dependence, oxygenation and CO2 rather than reporting AHI alone.",
      "The same AHI can represent very different treatable phenotypes.",
      "What adherence limitation makes positional therapy less durable in some patients?"),

    Q("v141_slp_02", SLP, "Maxillomandibular Advancement",
      "A young PAP-intolerant patient with severe OSA, retrognathia and multilevel collapse wants a highly effective skeletal option. What procedure should be discussed?",
      ["Maxillomandibular advancement", "Turbinate reduction alone", "Tonsillectomy only regardless of anatomy", "No surgery"], 0,
      "MMA advances both maxilla and mandible, enlarging retropalatal and retrolingual airway and can be highly effective in appropriately selected severe OSA.",
      "Skeletal anatomy can be the dominant airway problem; soft-tissue surgery is not always enough.",
      "What occlusal, sensory and aesthetic risks require counseling?", "OR_prep"),

    Q("v141_slp_03", SLP, "Positional OSA",
      "A patient with mild positional OSA asks whether positional therapy is curative. What is the best counseling?",
      ["It can be effective when nonsupine AHI is low, but long-term adherence and weight/disease progression should be reassessed", "It cures all severe OSA", "It is contraindicated in every patient", "No follow-up is needed"], 0,
      "Positional therapy works best in a true positional phenotype and requires adherence; residual disease should be objectively reassessed when symptoms or risk remain.",
      "Treat the phenotype, then verify the treatment actually controls it.",
      "How would substantial non-supine OSA change therapy?"),

    Q("v141_slp_04", SLP, "Sleep-Related Hypoventilation",
      "An obese patient has daytime hypercapnia and sustained nocturnal CO2 elevation rather than discrete obstructive events alone. What syndrome should be considered?",
      ["Obesity hypoventilation syndrome", "BPPV", "Isolated positional OSA", "Narcolepsy"], 0,
      "Hypoventilation is a gas-exchange disorder and may require PAP modes/ventilatory support and weight treatment beyond conventional upper-airway surgery.",
      "Look at CO2, not just AHI.",
      "Why can supplemental oxygen alone worsen hypercapnia in selected hypoventilation patients?"),

    Q("v141_slp_05", SLP, "HNS Activation / Programming",
      "A newly activated HNS patient has painful tongue pulling and awakens with stimulation. What is the best next step?",
      ["Reprogram amplitude/electrode configuration and acclimatization rather than simply escalating stimulation", "Maximize amplitude", "Explant immediately", "Stop follow-up"], 0,
      "Comfort and effective tongue protrusion depend on individualized programming; excessive stimulation can reduce adherence without improving airway opening.",
      "HNS is titrated therapy, not a fixed-output implant.",
      "What tongue-motion pattern suggests poor electrode recruitment?"),

    Q("v141_slp_06", SLP, "PAP Troubleshooting",
      "A CPAP user has good mask seal but persistent central apneas that emerged after obstructive events were controlled. What should happen next?",
      ["Recognize treatment-emergent central sleep apnea and reassess PAP mode/underlying contributors with sleep medicine", "Increase fixed CPAP pressure indefinitely", "Palatal surgery immediately", "Ignore residual events"], 0,
      "Persistent central events after obstructive control require physiologic reassessment rather than treating them as residual pharyngeal collapse.",
      "Read the residual event type before changing pressure.",
      "Which cardiac condition changes the safety of some adaptive servo-ventilation strategies?"),

    # Thyroid / salivary
    Q("v141_tps_01", TPS, "Graves Disease / Toxic Goiter",
      "A patient with uncontrolled Graves disease requires urgent nonthyroid surgery and develops fever, severe tachycardia, agitation and heart failure. What emergency should be treated?",
      ["Thyroid storm with beta blockade as appropriate, thionamide, iodine after thionamide, steroids and supportive care", "Hungry bone syndrome", "Myxedema coma", "Sialadenitis"], 0,
      "Thyroid storm is a clinical diagnosis of decompensated thyrotoxicosis and requires immediate multimodal treatment; iodine is given after blocking new hormone synthesis.",
      "Sequence matters: block synthesis before iodine to avoid providing new substrate.",
      "How is preoperative preparation different for elective thyroidectomy in controlled Graves disease?", "overnight_call"),

    Q("v141_tps_02", TPS, "Hungry Bone / Post-Thyroid Calcium Management",
      "After parathyroidectomy for severe hyperparathyroidism, a patient develops prolonged symptomatic hypocalcemia with low phosphate and high bone-turnover history. What is most likely?",
      ["Hungry bone syndrome requiring aggressive calcium and vitamin D replacement", "Recurrent hyperparathyroidism within hours", "Thyroid storm", "Sialocele"], 0,
      "Rapid skeletal remineralization after removal of excess PTH can produce prolonged hypocalcemia, often with hypophosphatemia and high preoperative bone turnover.",
      "Hungry bone is a skeletal sink, not simply transient hypoparathyroidism.",
      "Which preoperative features predict higher risk and justify anticipatory replacement?", "postoperative_call"),

    Q("v141_tps_03", TPS, "Medullary Thyroid Cancer",
      "A patient with a thyroid nodule has markedly elevated calcitonin and FNA consistent with medullary thyroid carcinoma. What preoperative issue is mandatory?",
      ["Evaluate for germline RET/MEN2 and exclude pheochromocytoma before surgery when hereditary disease is possible", "Give RAI", "Use thyroglobulin as the primary marker", "Ignore family history"], 0,
      "MTC arises from C cells and is followed with calcitonin/CEA; RAI is ineffective. Hereditary disease changes family and perioperative management.",
      "Pheochromocytoma comes before thyroidectomy in MEN2.",
      "How does a high calcitonin level influence nodal and distant staging?"),

    Q("v141_tps_04", TPS, "Salivary Gland Malignancy",
      "A parotid mass is firm, fixed and associated with new facial weakness. What is the best next framework?",
      ["Treat as malignant until proven otherwise: image extent/perineural disease, obtain tissue diagnosis and plan facial-nerve/neck management by histology and stage", "Assume Warthin tumor", "Enucleate blindly", "Observe for years"], 0,
      "Pain, fixation, skin involvement or facial weakness are malignant salivary red flags; treatment depends heavily on histology, grade and nerve involvement.",
      "New facial paralysis with a parotid mass is cancer until proven otherwise.",
      "When can an involved facial nerve be sacrificed, and what reconstruction should be planned simultaneously?", "OR_prep"),

    Q("v141_tps_05", TPS, "Primary Thyroid Lymphoma",
      "A patient with rapidly enlarging thyroid lymphoma has progressive dyspnea but remains oxygenating. What airway principle is safest?",
      ["Coordinate urgent tissue diagnosis and oncologic therapy while planning a controlled airway if deterioration occurs; avoid unnecessary thyroidectomy", "Routine total thyroidectomy as first-line lymphoma treatment", "Wait for complete obstruction", "RAI"], 0,
      "Lymphoma can shrink quickly with systemic therapy, but airway compromise may require temporizing securement; extensive thyroid surgery is usually not definitive treatment.",
      "The correct biopsy must provide lymphoma architecture without turning diagnosis into an unnecessary thyroid operation.",
      "What biopsy method is preferred when FNA is nondiagnostic?", "overnight_call"),

    Q("v141_tps_06", TPS, "Completion Thyroidectomy",
      "A patient after lobectomy has a 1.5 cm intrathyroidal papillary carcinoma with negative margins and no adverse features. Why might completion thyroidectomy be avoided?",
      ["The incremental oncologic benefit may be small while reoperation adds RLN/parathyroid risk", "Completion is prohibited in all cancer", "RAI is mandatory without it", "Because pathology does not matter"], 0,
      "Completion thyroidectomy is selective; it should provide a defined benefit such as treating residual disease, enabling chosen RAI strategy or improving surveillance in higher-risk settings.",
      "If you cannot name the benefit of the second operation, do not perform it by reflex.",
      "How would gross extrathyroidal extension or significant nodal disease change the balance?"),

    # Facial Plastics / Trauma
    Q("v141_fpt_01", FPT, "Mandible Fracture",
      "A displaced angle fracture crosses an infected third molar and the patient has malocclusion. What is the operative priority?",
      ["Restore premorbid occlusion and achieve stable reduction/fixation while addressing teeth in the fracture line based on infection and stability", "Plate the fracture without checking occlusion", "Remove every tooth in every fracture line", "Observe all displaced fractures"], 0,
      "Mandible fracture repair is fundamentally an occlusion-and-bone-stability operation; dental management is individualized.",
      "Establish the bite before accepting the plate position.",
      "How do favorable versus unfavorable muscle vectors affect fixation?", "OR_prep"),

    Q("v141_fpt_02", FPT, "Nasal Fracture",
      "A patient with a displaced nasal fracture presents 3 weeks after injury with fixed bony deformity and nasal obstruction. What is the best plan?",
      ["Allow healing and plan delayed functional septorhinoplasty/osteotomies rather than force late closed reduction", "Closed reduction is equally effective months later", "No treatment is possible", "Turbinate reduction alone"], 0,
      "Once nasal bones have consolidated, late closed reduction is unreliable; definitive correction is delayed until tissues stabilize.",
      "Know the closed-reduction window—and know when it has closed.",
      "How does a septal hematoma at initial injury change urgency regardless of fracture timing?"),

    Q("v141_fpt_03", FPT, "Forehead Flap / Nasal Reconstruction",
      "During staged paramedian forehead-flap reconstruction, why is thinning often delayed or carefully staged?",
      ["Aggressive early thinning can jeopardize the supratrochlear-based vascular supply before neovascularization", "The flap has no vascular pedicle", "Cartilage never needs coverage", "Staging has no biologic rationale"], 0,
      "Forehead-flap stages balance contour with vascular reliability; inset, intermediate thinning and pedicle division are timed around neovascularization.",
      "A beautiful thin flap that dies is worse than a bulky flap that can be safely refined later.",
      "What determines when the pedicle can be divided?", "OR_prep"),

    Q("v141_fpt_04", FPT, "Dynamic Facial Reanimation",
      "A patient has recent proximal facial-nerve sacrifice with viable distal branches and no tension-free primary repair. What is the best reconstructive principle?",
      ["Immediate interposition nerve grafting when feasible to preserve native muscle reinnervation", "Wait years until muscles atrophy", "Static sling only in every patient", "Botulinum toxin into the paralyzed side"], 0,
      "When distal facial musculature remains viable, timely nerve repair/grafting can restore native movement; free muscle transfer is reserved for longstanding denervation or unavailable native targets.",
      "Reanimation strategy is driven by time since denervation and what neural/muscular infrastructure remains.",
      "When is masseteric-to-facial nerve transfer preferred over cross-face grafting?", "OR_prep"),

    Q("v141_fpt_05", FPT, "Functional Septorhinoplasty",
      "A patient has severe internal nasal-valve collapse and a narrow middle vault after prior hump reduction. What reconstruction best addresses the mechanism?",
      ["Restore middle-vault width/support with spreader grafts or equivalent structural technique", "Remove more upper lateral cartilage", "Inferior turbinectomy alone", "Nasal steroids alone"], 0,
      "Middle-vault collapse after hump reduction can narrow the internal valve; structural reconstruction restores the dorsal septum-upper lateral cartilage relationship.",
      "Functional rhinoplasty is airflow mechanics plus framework—not simply septal straightening.",
      "What maneuver treats lateral-wall insufficiency at the external valve instead?", "OR_prep"),

    Q("v141_fpt_06", FPT, "Frontal Sinus Fracture Decision Model",
      "A frontal sinus fracture has an intact posterior table but a clearly obstructed nasofrontal outflow tract and displaced anterior table. What long-term complication drives management of the outflow tract?",
      ["Mucocele/mucopyocele from trapped sinus mucosa", "BPPV", "Otosclerosis", "Parotid fistula"], 0,
      "Frontal sinus fracture decisions center on anterior contour, posterior-table/dural injury and outflow-tract patency; obstructed drainage can produce delayed mucoceles years later.",
      "Frontal sinus trauma is a long-term drainage problem as much as an acute fracture problem.",
      "When is sinus obliteration or cranialization considered?", "OR_prep"),
]
