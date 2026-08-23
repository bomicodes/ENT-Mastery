"""
v13.1 - New curriculum topics closing genuine gaps surfaced by the
topic-alias audit (v129): real, board- and call-relevant entities that had
existing vignette content but no canonical DEEP_MODULES_V6 topic to attach
to. Adding the topic (with the exact display label already used by the
orphaned vignette) is the honest fix, rather than force-aliasing these into
an unrelated existing topic.

Each entry follows the standard six-stage schema and is appended to the
correct domain's DEEP_MODULES_V6 list at import time.
"""

NEW_TOPICS_V131 = {
    "Thyroid / Parathyroid / Salivary": [
        {
            "topic": "First-Bite Syndrome",
            "recognize": "Severe, cramping pain in the parotid/preauricular region with the very first bite of a meal that eases with subsequent bites, occurring after parapharyngeal space or deep lobe parotid surgery near the sympathetic chain.",
            "localize": "Thought to reflect denervation supersensitivity of residual myoepithelial cells to sympathetic input after injury near the cervical sympathetic chain during deep parotid or parapharyngeal space surgery, not a salivary outflow obstruction.",
            "workup": "Diagnosis is clinical, based on the characteristic first-bite pattern and a surgical history in the right anatomic field; imaging mainly excludes recurrent tumor or an alternative cause if the pattern is atypical.",
            "manage": "Reassurance and expectation-setting are central since symptoms often improve gradually over time; pharmacologic options such as anticonvulsants or botulinum toxin can be considered for persistent, disabling symptoms.",
            "operate": "There is no routine surgical treatment; recognizing the diagnosis avoids an unnecessary re-exploration or workup for recurrent tumor when the pattern is classic.",
            "teach": "First-bite syndrome is a denervation-supersensitivity pain phenomenon, not an obstructive or neoplastic problem - the history makes the diagnosis.",
            "tags": ["parotid", "parapharyngeal", "sympathetic chain", "postoperative pain"]
        },
        {
            "topic": "Frey Syndrome",
            "recognize": "Gustatory sweating and flushing over the preauricular/cheek skin during eating, months to years after parotidectomy.",
            "localize": "Aberrant reinnervation: severed parasympathetic secretomotor fibers destined for the parotid gland regenerate into nearby severed sympathetic fibers supplying sweat glands and cutaneous vessels in the overlying skin.",
            "workup": "Diagnosis is clinical; a starch-iodine (Minor's) test can objectively demonstrate the affected skin distribution when confirmation is needed.",
            "manage": "Topical antiperspirants are first-line for mild symptoms; botulinum toxin injection into the affected skin is effective for more bothersome cases.",
            "operate": "Interposing a barrier such as an SMAS flap or acellular dermal matrix between the parotid bed and overlying skin at the time of parotidectomy reduces incidence and is reasonable in higher-risk dissections.",
            "teach": "Frey syndrome is aberrant parasympathetic-to-sympathetic reinnervation after parotidectomy - prevention with an interposition barrier is easier than treating established symptoms.",
            "tags": ["parotidectomy", "gustatory sweating", "aberrant reinnervation"]
        },
        {
            "topic": "Recurrent Laryngeal Nerve Injury During Thyroidectomy",
            "recognize": "New hoarseness, weak or breathy voice, or aspiration with liquids after thyroid or parathyroid surgery should raise concern for recurrent laryngeal nerve injury; bilateral injury can present with stridor instead of voice change.",
            "localize": "The RLN's course is variable and its relationship to the inferior thyroid artery is inconsistent; injury risk is highest near the ligament of Berry and where the nerve enters the larynx at the cricothyroid joint.",
            "workup": "Flexible laryngoscopy to assess vocal fold mobility is the key postoperative test whenever voice change, aspiration, or breathing concern is present after thyroid or parathyroid surgery.",
            "manage": "Unilateral injury with a mobile contralateral fold is often observed initially with voice therapy since many paresis cases recover; bilateral injury with airway compromise may require urgent airway intervention.",
            "operate": "Intraoperative nerve monitoring can help identify the nerve and detect a loss-of-signal event, prompting a pause to reassess technique, but does not replace direct visual identification.",
            "teach": "Identify, don't just avoid, the RLN - relying on a single landmark such as the inferior thyroid artery is unreliable given normal anatomic variability; document vocal fold mobility before and after thyroid or parathyroid surgery.",
            "tags": ["thyroidectomy", "RLN", "voice change", "nerve monitoring"]
        },
    ],
    "Pediatric Otolaryngology": [
        {
            "topic": "Croup vs Epiglottitis",
            "recognize": "Croup typically presents with a barky cough, hoarseness, and inspiratory stridor after a viral prodrome in a nontoxic child; epiglottitis presents with rapid-onset high fever, drooling, muffled voice, and tripod positioning in a toxic-appearing child.",
            "localize": "Croup involves subglottic edema; epiglottitis involves the supraglottis, which can obstruct the airway rapidly and unpredictably.",
            "workup": "Croup is typically a clinical diagnosis; a toxic-appearing child with suspected epiglottitis should not undergo distressing exams or imaging that could precipitate complete obstruction.",
            "manage": "Croup is managed with corticosteroids and nebulized racemic epinephrine if stridor at rest; suspected epiglottitis requires immediate anesthesia/ENT involvement for controlled airway management plus antibiotics.",
            "operate": "For suspected epiglottitis, airway securement should occur in a controlled setting such as the OR with a team ready for a difficult airway, rather than an awake exam or intubation attempt outside that setting.",
            "teach": "A barky cough with a nontoxic child is croup until proven otherwise; drooling and tripod positioning with a toxic appearance is epiglottitis until proven otherwise - the latter needs a controlled airway plan, not a bedside exam.",
            "tags": ["stridor", "airway emergency", "epiglottitis", "croup"]
        },
        {
            "topic": "Epiglottitis",
            "recognize": "Rapid onset of high fever, sore throat, drooling, muffled voice, and tripod positioning in a toxic-appearing patient should raise immediate concern for epiglottitis.",
            "localize": "Inflammation and edema of the epiglottis and supraglottic structures can progress to complete airway obstruction with little warning.",
            "workup": "Avoid agitating the patient or performing distressing exams outside a controlled setting; imaging should never delay definitive airway planning in a clearly toxic-appearing patient.",
            "manage": "Immediate multidisciplinary airway planning with ENT and anesthesia, likely intubation in a controlled setting such as the OR, plus intravenous antibiotics.",
            "operate": "Direct laryngoscopy to secure the airway should occur in the OR with surgical airway backup available given the risk of sudden complete obstruction during instrumentation.",
            "teach": "The highest-yield action in suspected epiglottitis is keeping the patient calm and moving straight to a controlled airway plan - do not delay for imaging or repeated exams.",
            "tags": ["airway emergency", "supraglottitis", "pediatric airway", "overnight call"]
        },
        {
            "topic": "Button Battery Ingestion",
            "recognize": "Any suspected or witnessed button battery ingestion in a child is a time-critical emergency regardless of symptoms, since severe esophageal injury can occur within hours.",
            "localize": "A battery lodged in the esophagus generates a local electrical current causing liquefactive tissue necrosis, which can progress to perforation, fistula, and mediastinitis if not promptly removed.",
            "workup": "Immediate imaging to localize the battery is essential; a battery in the esophagus requires emergent removal, while one that has passed into the stomach in an asymptomatic child is managed differently.",
            "manage": "An esophageal button battery is an emergency requiring removal typically within 2 hours of presentation; do not wait for symptoms to develop before acting.",
            "operate": "Emergent endoscopic removal is performed, with attention to possible underlying tissue injury, vascular involvement, and delayed complications such as fistula and stricture requiring close follow-up.",
            "teach": "Time is tissue with an esophageal button battery - this is one of the few pediatric foreign bodies where a delay of even a few hours meaningfully changes outcomes.",
            "tags": ["foreign body", "esophagus", "pediatric emergency", "battery"]
        },
    ],
    "Facial Plastics / Trauma": [
        {
            "topic": "Septal Hematoma",
            "recognize": "Bilateral, boggy, fluctuant swelling of the nasal septum after nasal trauma, including in children, should raise concern for septal hematoma, which can be subtle and easily missed.",
            "localize": "Blood collects in the subperichondrial space between the septal cartilage and its perichondrium, cutting off the cartilage's blood supply.",
            "workup": "Diagnosis is clinical, made by anterior rhinoscopy; palpation with a cotton swab can help distinguish a fluctuant hematoma from simple soft-tissue swelling or a deviated septum.",
            "manage": "Prompt drainage is required - untreated septal hematoma can lead to cartilage necrosis within 24 to 48 hours, resulting in saddle-nose deformity, and can become infected with risk of intracranial spread.",
            "operate": "Incision and drainage under local or general anesthesia, followed by nasal packing or a similar technique to prevent reaccumulation, with close follow-up to ensure resolution.",
            "teach": "Every nasal trauma exam, especially in children, should include a specific look for septal hematoma - missing it is one of the more preventable causes of permanent saddle-nose deformity.",
            "tags": ["nasal trauma", "septum", "pediatric emergency", "saddle nose"]
        },
    ],
    "Sleep Surgery": [
        {
            "topic": "Positional OSA",
            "recognize": "Obstructive sleep apnea in which the apnea-hypopnea index is substantially worse supine than non-supine on polysomnography, often in a patient with milder overall disease.",
            "localize": "Supine positioning allows gravity to worsen posterior tongue-base displacement and collapse of the retropalatal/retrolingual airway compared with lateral or prone positioning.",
            "workup": "Confirm with polysomnography reporting position-specific AHI data; a large supine-to-non-supine AHI ratio supports a positional phenotype.",
            "manage": "Positional therapy can be effective as primary or adjunctive treatment in appropriately selected patients with milder positional disease, but is generally insufficient alone for severe, non-positional-predominant OSA.",
            "operate": "Surgical planning, including drug-induced sleep endoscopy, should account for supine-specific collapse patterns since a purely positional phenotype may respond differently than fixed obstruction.",
            "teach": "Positional OSA is a distinct phenotype, not just mild OSA - ask specifically about supine-versus-non-supine AHI before deciding whether positional therapy is reasonable.",
            "tags": ["OSA phenotyping", "positional therapy", "polysomnography"]
        },
    ],
    "General ENT / Emergencies": [
        {
            "topic": "Lemierre Syndrome",
            "recognize": "A young, previously healthy patient with recent oropharyngeal infection who develops persistent fever, neck pain and swelling, and signs of septic emboli should raise concern for Lemierre syndrome.",
            "localize": "Septic thrombophlebitis of the internal jugular vein, typically arising from a peritonsillar or parapharyngeal infection that spreads to the adjacent vein, classically associated with Fusobacterium necrophorum.",
            "workup": "Contrast-enhanced neck CT or ultrasound to identify internal jugular vein thrombosis, blood cultures, and chest imaging to evaluate for septic pulmonary emboli.",
            "manage": "Prolonged intravenous antibiotics with anaerobic coverage are the mainstay; anticoagulation is used selectively rather than routinely in all patients.",
            "operate": "Surgical drainage is indicated for an associated abscess such as a peritonsillar or parapharyngeal collection; operative management of the thrombosed vein itself is rarely needed.",
            "teach": "A young patient with recent sore throat, persistent fever, and neck tenderness who is not getting better deserves consideration of Lemierre syndrome - a classic missed emergency because the initial picture looks like ordinary pharyngitis.",
            "tags": ["deep neck infection", "septic emboli", "internal jugular vein", "overnight call"]
        },
    ],
}
