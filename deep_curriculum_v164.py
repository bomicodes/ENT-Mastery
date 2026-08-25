"""v16.4 — Cross-domain Deep Curriculum enrichment, pass 5.

Another in-place pass across all non-Otology domains, emphasizing common board
traps and overnight-call pivots that are easy to under-teach in a six-layer
summary.
"""


def _entry(candidates, recognize, localize, workup, manage, operate, teach, tags, sources=None):
    return {
        "candidates": tuple(candidates),
        "fields": {
            "recognize": recognize, "localize": localize, "workup": workup,
            "manage": manage, "operate": operate, "teach": teach,
            "tags": list(tags),
            **({"source_basis": list(sources)} if sources else {}),
        },
    }


PATCHES_V164 = {
    "Rhinology / Allergy / Skull Base": [
        _entry(
            ["Orbital Complications of Sinusitis", "Orbital Cellulitis vs Preseptal Cellulitis", "Orbital Complication of Sinusitis"],
            "Differentiate preseptal cellulitis from postseptal/orbital disease. Preseptal disease causes eyelid erythema/edema with preserved vision, pupils, motility, and no proptosis. Orbital cellulitis adds pain with eye movement, ophthalmoplegia, proptosis, diplopia, decreased vision, RAPD, chemosis, or systemic toxicity. Subperiosteal/orbital abscess and cavernous-sinus/intracranial extension are escalation states, not merely more severe eyelid swelling.",
            "Ethmoid sinusitis commonly reaches the medial orbit through the thin lamina papyracea and ethmoidal vascular foramina. The orbital septum separates preseptal from postseptal disease; once infection is postseptal, optic nerve perfusion, extraocular muscles, superior orbital fissure/cavernous sinus and intracranial structures become relevant. Medial subperiosteal abscess is common in children, but superior/inferior or intraconal location can change drainage approach and risk.",
            "Perform and serially document visual acuity, pupils/RAPD, color vision when feasible, extraocular motility, proptosis and neurologic status. Contrast CT of sinuses/orbits is the rapid first-line map when orbital complication is suspected; MRI is favored when optic nerve, cavernous sinus, intracranial or complex soft-tissue extension is a concern. Obtain cultures from operative drainage rather than relying on superficial nasal swabs. Ophthalmology and ENT should be involved early for true orbital disease.",
            "Preseptal disease without orbital signs can often be treated medically according to age/severity. Orbital cellulitis requires IV antibiotics and close serial examinations. Surgery is favored with visual compromise, large/organized abscess, intracranial extension, clinical deterioration or failure to improve appropriately; age, abscess size/location, frontal sinus involvement and organism risk modify the threshold. Vision decline is an emergency and should not wait for a routine morning reassessment.",
            "Drain the infected sinus source and orbital collection through the safest corridor. Medial subperiosteal abscesses are often amenable to endoscopic ethmoidectomy with lamina exposure/drainage; superior/lateral/intraconal collections may require ophthalmic external or combined approaches. Preserve periorbita unless entry is required, identify skull base and orbital boundaries, and avoid traction on orbital contents. The endpoint is source control plus protection of vision, not simply opening an ethmoid cell.",
            "Boards/chief framework: eyelid edema is not the discriminator—vision, pupils, motility, pain with movement and proptosis are. Postseptal disease demands serial eye exams. A child whose visual function worsens has crossed from 'sinusitis treatment' to a vision-saving source-control emergency.",
            ["orbital cellulitis", "preseptal", "subperiosteal abscess", "lamina papyracea", "RAPD", "vision", "ethmoid sinusitis"],
            ["Pasha 6e", "KJ Lee 12e"],
        ),
    ],
    "Head & Neck Oncology": [
        _entry(
            ["Osteoradionecrosis of the Jaw", "Osteoradionecrosis"],
            "Osteoradionecrosis (ORN) is devitalized irradiated bone that fails to heal, most often mandible, and may present with exposed bone, pain, drainage, fracture, fistula, trismus or secondary infection. It is not simply osteomyelitis after radiation: radiation creates hypovascular, hypocellular, fibrotic tissue with impaired remodeling, and infection may be secondary. Risk rises with mandibular dose, dental trauma/extraction, poor dentition, smoking and larger irradiated bone volume.",
            "Mandibular ORN often affects body/angle because of dose distribution, dental-bearing bone and relatively limited blood supply compared with maxilla. Disease may remain superficial or progress to full-thickness cortical/medullary necrosis, pathologic fracture, inferior-alveolar-nerve symptoms and cutaneous fistula. Distinguish recurrent tumor from ORN whenever pain, mass, progressive destruction or atypical soft tissue is present.",
            "Evaluate oral/dental status, exposed bone extent, fistula, fracture, sensory change and nutritional impact. CT defines sequestra, cortical destruction and fracture; MRI/PET can be difficult to interpret because inflammation and recurrence overlap. Biopsy suspicious soft tissue or atypical progressive lesions when recurrence cannot be excluded. Culture is useful for superimposed infection but does not define ORN itself.",
            "Early limited disease is managed with meticulous oral hygiene, smoking cessation, pain control, treatment of superinfection, dental/maxillofacial collaboration and selected medical regimens such as pentoxifylline/tocopherol-based antifibrotic approaches. Hyperbaric oxygen is not a universal default and its role is selective. Progressive full-thickness disease, fracture, fistula, uncontrolled pain/infection or failure of conservative therapy shifts management toward resection and vascularized reconstruction.",
            "Debridement/sequestrectomy is appropriate when limited necrotic bone can be removed back to bleeding viable margins. Segmental mandibulectomy is required for advanced structural disease/pathologic fracture or diffuse full-thickness necrosis; reconstruction generally needs well-vascularized tissue, commonly osseous free flap when continuity is lost. In an irradiated field, durable soft-tissue coverage is as important as bone fixation. Do not perform repeated small debridements indefinitely when the mandible has structurally failed.",
            "Boards/chief framework: ORN is radiation-injured bone biology, sometimes secondarily infected, and recurrence must remain in the differential. Limited superficial disease can be conservative; pathologic fracture/fistula/full-thickness necrosis is a reconstructive problem. The cure for a dead segment is viable vascularized tissue, not endless antibiotics.",
            ["osteoradionecrosis", "mandible", "radiation", "pathologic fracture", "PENTO", "free flap", "recurrent cancer"],
            ["NCCN Head & Neck v2.2026", "Pasha 6e", "KJ Lee 12e"],
        ),
    ],
    "Thyroid / Parathyroid / Salivary": [
        _entry(
            ["Recurrent Laryngeal Nerve Injury During Thyroidectomy", "RLN Injury During Thyroidectomy"],
            "After thyroid/parathyroid surgery, unilateral recurrent-laryngeal-nerve injury usually causes breathy dysphonia, weak cough and sometimes aspiration; bilateral injury can cause stridor/airway obstruction with a surprisingly preserved voice. Not every postoperative immobile fold is a transected nerve—traction neuropraxia, edema, arytenoid injury and preexisting paresis are alternatives. Baseline voice/vocal-fold status matters because a preoperative paralysis changes both oncologic staging and contralateral operative risk.",
            "The RLN has variable relation to the inferior thyroid artery but becomes predictably vulnerable near the ligament of Berry and laryngeal entry point. The right nerve has a more oblique course; the left ascends in the tracheoesophageal groove. Nonrecurrent nerve is uncommon but important, especially on the right with vascular anomaly. External branch of the superior laryngeal nerve is a separate risk that affects pitch projection rather than fold mobility.",
            "Document preoperative laryngeal function when voice symptoms, prior neck surgery, invasive/posterior tumor or other risk factors are present; many practices obtain broader baseline exams. New postoperative dysphonia, aspiration or breathing difficulty warrants flexible laryngoscopy. Intraoperative nerve monitoring helps identify/assess function but does not replace visual identification. A true loss-of-signal event should prompt troubleshooting of tube/equipment, stimulation proximal/distal to localize injury, and reconsideration of staged bilateral surgery when contralateral nerve risk remains.",
            "Many unilateral neuropraxic injuries recover over months; early voice therapy and temporary injection augmentation can improve voice/swallow while recovery is awaited. Persistent unilateral paralysis can be treated with durable medialization/arytenoid procedures or selected reinnervation according to age, glottic gap and prognosis. Bilateral immobility with respiratory compromise is an airway problem first and may require reintubation/tracheostomy or later glottic-widening procedures.",
            "Identify the RLN deliberately, minimize traction/thermal injury and preserve its blood supply. If a clean transection is recognized, primary repair or cable graft/reinnervation should be considered when feasible; it may restore tone/bulk even if normal motion does not return. When invasive cancer requires nerve sacrifice, plan voice/airway rehabilitation at the same operation. After loss of signal on the first side of a planned bilateral thyroidectomy, staging the contralateral side can prevent catastrophic bilateral paralysis in selected circumstances.",
            "Boards/chief framework: the dangerous thyroidectomy nerve problem is not merely hoarseness—it is bilateral airway obstruction. Know the Berry-ligament/laryngeal-entry danger zone, distinguish RLN from EBSLN deficits, and treat intraoperative loss of signal as information that can change whether you proceed to the second side.",
            ["RLN", "thyroidectomy", "loss of signal", "bilateral paralysis", "Berry ligament", "injection laryngoplasty", "nerve repair"],
            ["Pasha 6e", "KJ Lee 12e"],
        ),
    ],
    "Pediatric Otolaryngology": [
        _entry(
            ["Button Battery Ingestion", "Button Battery"],
            "An esophageal button battery is a true time-critical emergency because electrical hydrolysis generates hydroxide at the negative pole and causes rapid liquefactive necrosis; severe injury can occur even in a child who initially looks well. On radiographs, look for the double-ring/halo sign on AP and step-off on lateral view to distinguish a button battery from a coin. Symptoms may include drooling, dysphagia, chest discomfort, cough or refusal to eat, but absence of symptoms does not make an esophageal battery safe.",
            "Damage occurs where the battery contacts mucosa and can extend into trachea, mediastinum, recurrent laryngeal nerve or major vessels. Batteries lodged near the aortic arch or other vascular structures raise concern for delayed catastrophic fistula even after removal. Orientation matters because the negative pole produces the most severe caustic injury, but immediate removal takes priority over elaborate orientation analysis.",
            "Obtain urgent AP/lateral imaging from neck through abdomen to localize the battery and distinguish it from a coin. Do not delay removal of an esophageal battery for fasting status. In selected children older than 12 months with ingestion within about 12 hours and ability to swallow, prehospital/ED honey may reduce injury while definitive care is mobilized, but it never replaces removal. After extraction, grade mucosal injury and use CT/CTA/endoscopy/esophagram selectively when deep injury or vascular/tracheal involvement is suspected.",
            "Remove an esophageal button battery emergently, ideally within 2 hours of recognition. Gastric/distal batteries are managed according to age, size, symptoms and high-risk circumstances rather than the esophageal algorithm. After removal, ongoing tissue injury can continue; diet, observation, repeat endoscopy/imaging and follow-up depend on injury severity. Counsel families about delayed complications including stricture, vocal-fold paralysis, tracheoesophageal fistula and aortoenteric fistula.",
            "Rigid or flexible endoscopic removal should minimize additional mucosal trauma while ensuring the battery is completely retrieved. Inspect the esophageal injury and consider irrigation according to current institutional protocol after removal. Severe circumferential/deep injury near major vessels requires multidisciplinary planning and may justify prolonged monitored observation and vascular imaging. Never assume successful extraction ends the emergency—the post-removal injury trajectory can be the dangerous phase.",
            "Boards/chief framework: esophageal button battery = remove now, symptoms or NPO status do not buy time. The double-ring sign distinguishes it from a coin. The most frightening complication—major vascular fistula—can present days later, so post-removal injury severity determines surveillance and counseling.",
            ["button battery", "double ring", "hydroxide", "esophagus", "aortoenteric fistula", "honey", "foreign body"],
            ["Pasha 6e", "KJ Lee 12e"],
        ),
    ],
    "Laryngology / Voice / Swallowing": [
        _entry(
            ["Vocal Fold Polyp / Cyst", "Vocal Fold Nodules, Polyps, and Cysts", "Benign Vocal Fold Lesions"],
            "Benign phonotraumatic lesions are not interchangeable. Nodules are typically bilateral symmetric callus-like lesions at the mid-membranous striking zone and strongly linked to repetitive phonotrauma. Polyps are usually unilateral, often hemorrhagic or translucent, and may follow acute or chronic phonotrauma. Cysts are subepithelial lesions (mucus-retention or epidermoid) that can markedly impair mucosal wave and are less likely than nodules to resolve with voice therapy alone. Reinke edema is a separate diffuse superficial-lamina-propria process strongly associated with smoking/irritants.",
            "Normal vibration depends on pliable epithelium/superficial lamina propria over the vocal ligament/muscle. Lesion depth predicts the stroboscopic effect: superficial nodules/polyps may preserve some wave, whereas a cyst tethering the cover often creates focal stiffness and reduced/absent wave over the lesion. A contralateral reactive lesion can develop opposite a unilateral primary lesion and should not automatically be excised as a second primary pathology.",
            "Use flexible laryngoscopy with videostroboscopy when available to assess lesion morphology, symmetry, mucosal wave, closure pattern and surrounding inflammation. Ask about occupational voice demands, acute phonotrauma, smoking, anticoagulation, reflux/rhinitis symptoms and prior surgery. Persistent unilateral irregular, leukoplakic, ulcerative or vascular lesions require a neoplasm/dysplasia pathway rather than being labeled a benign polyp by appearance alone.",
            "Voice therapy, vocal-behavior modification and treatment of relevant irritants are foundational, especially for nodules and many polyps. Observation is reasonable when symptoms are mild and the lesion is improving. Persistent symptomatic polyps/cysts, professional-voice limitations or lesions with diagnostic uncertainty may require microlaryngoscopic excision. Steroids/antibiotics are not routine substitutes for treating phonotrauma or a structural lesion.",
            "Phonomicrosurgery aims to remove the lesion while preserving as much normal cover and superficial lamina propria as possible. For cysts, careful microflap dissection reduces recurrence while minimizing scar; rupture can make complete removal difficult. For polyps, remove only pathologic tissue and preserve adjacent epithelium. Excessive stripping creates scar/sulcus-like stiffness that may be more disabling than the original lesion, so postoperative voice outcome depends on tissue preservation, not just lesion disappearance.",
            "Boards/chief framework: nodules = usually bilateral and therapy-responsive; polyp = usually unilateral phonotraumatic mass; cyst = subepithelial stiffness with reduced wave and often a surgical lesion when symptomatic. The operative goal is not 'take the bump off'—it is preserve the vibratory cover while eliminating pathology.",
            ["vocal fold nodule", "polyp", "cyst", "stroboscopy", "mucosal wave", "microflap", "phonotrauma"],
            ["Pasha 6e", "KJ Lee 12e"],
        ),
    ],
    "Facial Plastics / Trauma": [
        _entry(
            ["Nasal Fracture", "Nasal Bone Fracture"],
            "Nasal fracture evaluation is clinical and should separate cosmetic deformity, airway/septal injury and the true emergency of septal hematoma. Examine for new deviation, mobility/step-off, epistaxis, obstruction and septal swelling. A septal hematoma is boggy/fluctuant rather than a firm deviated septum and requires urgent drainage because cartilage loses its blood supply from the perichondrium, risking abscess and saddle-nose deformity.",
            "The paired nasal bones articulate with frontal bone and upper lateral cartilages; lower septum provides key L-strut support. Trauma can fracture bone, dislocate the septum off the maxillary crest, injure upper lateral attachments/internal valve, or create a septal hematoma without dramatic external deformity. Children are especially vulnerable to growth-related consequences of septal cartilage injury.",
            "CT is not routinely required for an isolated uncomplicated nasal fracture; obtain imaging when broader midface/NOE/orbital/skull-base injury is suspected. Document preinjury appearance if photographs are available, nasal airway, septum, ocular findings and CSF-leak signs. Reassess after edema subsides if initial swelling obscures deformity, but never defer evaluation of a possible septal hematoma.",
            "Observe fractures without meaningful deformity/obstruction. Closed reduction is generally performed after enough swelling subsides for assessment but before fragments consolidate, commonly within roughly 1–2 weeks in adults (earlier healing in children may shorten the window). Septal fracture/dislocation may require concomitant septal reduction. Delayed persistent deformity/obstruction is treated with definitive septorhinoplasty after healing rather than repeated late closed manipulation.",
            "Closed reduction restores bony alignment using intranasal/external manipulation while protecting mucosa and septum; stabilize as needed. A severely displaced caudal septum or unstable septal fracture may require open/septoplasty techniques to restore airway and support. Preserve adequate dorsal/caudal L-strut when removing cartilage. Drain septal hematoma immediately with measures to prevent reaccumulation and treat infection risk according to context.",
            "Boards/chief framework: the emergency in a 'simple nasal fracture' is the septal hematoma. CT is usually unnecessary for an isolated fracture. Timing matters: reduce after swelling permits assessment but before fixation; late deformity belongs to septorhinoplasty, not heroic delayed closed reduction.",
            ["nasal fracture", "closed reduction", "septal hematoma", "septal fracture", "L strut", "nasal obstruction"],
            ["Pasha 6e", "KJ Lee 12e"],
        ),
    ],
    "Sleep Surgery": [
        _entry(
            ["Oral Appliance Therapy", "Mandibular Advancement Device", "Mandibular Advancement Device Therapy"],
            "Mandibular advancement devices treat OSA by protruding/stabilizing the mandible and tongue-base complex, increasing upper-airway caliber. They are most useful in selected patients with snoring or mild-to-moderate OSA and in patients with more severe disease who cannot tolerate PAP, but efficacy is variable and cannot be predicted from AHI alone. Dentition, periodontal health, TMJ status, mandibular range and ability to retain/titrate a device are essential candidacy factors.",
            "Advancement tensions genioglossus/suprahyoid attachments and can improve retrolingual and sometimes retropalatal collapse. Response is less reliable when global concentric/lateral-wall collapse, severe obesity or markedly unfavorable anatomy dominates. DISE or other phenotyping can support selection in complex cases but is not required for every patient receiving an oral appliance.",
            "Review diagnostic sleep testing, positional dependence, oxygen burden, PAP experience and dental/TMJ examination. A qualified dental sleep provider fits a custom titratable device; over-the-counter noncustom devices are not equivalent. Assess baseline bite/occlusion because long-term therapy can change overjet/overbite and tooth position. Objective follow-up sleep testing after titration is needed to confirm efficacy rather than relying only on reduced snoring.",
            "Use a custom titratable mandibular advancement device when oral-appliance therapy is chosen and titrate to balance efficacy with comfort. Counsel about jaw discomfort, salivation/dry mouth, tooth movement, bite change and TMJ symptoms. Continue weight/nasal/comorbidity management. If residual OSA remains clinically important despite maximal tolerable advancement, change the treatment strategy rather than endlessly increasing protrusion.",
            "This is primarily a nonsurgical therapy, but the surgical connection is diagnostic: a good response may support the importance of tongue-base/mandibular mechanics, while failure can prompt reassessment for palate/lateral-wall/epiglottic or skeletal obstruction. Severe dental/TMJ limitations may make MMA, HNS, PAP or other therapies more appropriate. Surgery should not be chosen solely because a mandibular device was uncomfortable without re-phenotyping the airway and patient goals.",
            "Boards/chief framework: oral appliances are real OSA therapy, not just anti-snoring devices. Selection requires usable dentition/TMJ mechanics and follow-up testing. Symptom improvement does not prove physiologic control, and long-term occlusal change is a genuine counseling point.",
            ["oral appliance", "mandibular advancement", "MAD", "OSA", "TMJ", "occlusion", "follow-up sleep study"],
            ["Pasha 6e", "KJ Lee 12e"],
        ),
    ],
    "General ENT / Emergencies": [
        _entry(
            ["Lemierre Syndrome", "Lemierre's Syndrome"],
            "Lemierre syndrome is septic thrombophlebitis of the internal jugular vein after an oropharyngeal/deep-neck infection, classically in an otherwise healthy adolescent or young adult and commonly associated with Fusobacterium necrophorum. Think of it when a recent sore throat initially improves or seems routine but is followed by recurrent high fever, unilateral neck pain/swelling, toxicity, pleuritic symptoms or pulmonary septic emboli.",
            "Infection typically spreads from tonsillar/peritonsillar or parapharyngeal tissue into the carotid sheath/internal jugular vein. Septic thrombus can shower the lungs, causing multiple peripheral nodules, cavitation, effusions or empyema, and can less commonly seed joints or other organs. Because the IJV lies near carotid artery and lower cranial nerves, extensive parapharyngeal infection can produce additional vascular/neural complications.",
            "Obtain blood cultures before antibiotics when this does not delay treatment, CBC/metabolic/inflammatory assessment, contrast CT neck to evaluate IJV thrombosis and deep-neck source, and chest imaging for septic emboli. Ultrasound can identify accessible IJV thrombosis but may miss high skull-base or low thoracic segments. Culture/drain any abscess. A negative throat culture does not exclude Lemierre syndrome because the relevant infection is deep/vascular.",
            "Treat promptly with prolonged systemic antibiotics covering anaerobes and oral flora, adjusted to cultures and clinical response. Drain peritonsillar/parapharyngeal or other collections when present. Anticoagulation is individualized rather than automatic; consider it with extensive/progressive thrombosis, intracranial extension, persistent embolization or other selected circumstances in multidisciplinary discussion. Persistent fever should trigger reassessment for undrained source, resistant organism or ongoing septic thrombosis.",
            "Surgery targets the infectious source, not routine removal of the thrombosed IJV. Drain accessible abscesses and secure the airway when swelling/trismus threatens it. IJV ligation/excision is rarely required in the antibiotic/endovascular era and is reserved for uncontrolled septic source or hemorrhagic/vascular complications not manageable otherwise. Thoracic drainage may be needed for empyema or other metastatic infection.",
            "Boards/chief framework: young patient + recent pharyngitis + recurrent fever/neck tenderness + septic pulmonary lesions = Lemierre until disproven. Diagnose the deep infection and IJV thrombosis, treat anaerobes, and drain source control. The thrombosed vein is usually treated medically; the abscess is what you operate on.",
            ["Lemierre", "Fusobacterium", "IJV thrombosis", "septic emboli", "parapharyngeal", "anaerobes"],
            ["Pasha 6e", "KJ Lee 12e"],
        ),
    ],
}


def apply_cross_domain_depth_v164(deep_modules):
    applied, missing = [], []
    for domain, patches in PATCHES_V164.items():
        modules = deep_modules.get(domain, [])
        for patch in patches:
            found = next((m for m in modules if m.get("topic") in patch["candidates"]), None)
            if found is None:
                missing.append((domain, patch["candidates"]))
                continue
            found.update(patch["fields"])
            applied.append((domain, found.get("topic")))
    return {"applied": applied, "missing": missing}
