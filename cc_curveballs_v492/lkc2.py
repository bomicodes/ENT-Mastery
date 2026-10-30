"""v49.2 attending curveballs, batch lkc2 (locked concept checks; audits do not read curveball fields)."""

CURVEBALLS = {
    'cc-v112-rec-laryngology-voice-swallowing-muscle-tension-dysphonia': {
        "curveball": "After a month of voice therapy the supraglottic squeeze is gone, but stroboscopy now clearly shows a right vocal fold that lags and bows. What do you do next?",
        "curveball_answer": "The squeeze was compensatory, and therapy has unmasked the real driver: probable unilateral vocal fold paresis. Confirm with careful mobility assessment and laryngeal EMG where available, and image along the vagus and recurrent laryngeal nerve course if the cause is unexplained. If glottic insufficiency still limits the voice, offer injection augmentation or medialization, and continue therapy so the compensatory pattern does not return.",
    },
    'cc-v112-rec-laryngology-voice-swallowing-posterior-cordotomy-arytenoidectomy': {
        "curveball": "At direct laryngoscopy, palpation shows both cricoarytenoid joints are fixed and there is a dense interarytenoid scar. Is posterior cordotomy still the right operation?",
        "curveball_answer": "Not by itself. Fixed joints with an interarytenoid scar band are posterior glottic stenosis, a mechanical problem, not neural paralysis. A cordotomy that leaves the posterior scar in place tends to underperform or restenose. Treat the scar: endoscopic division with mucosal flap advancement, posterior cricoid split with a costal cartilage graft, or arytenoidectomy for fixed joints, usually keeping the tracheostomy until the airway is stable.",
    },
    'cc-v112-rec-laryngology-voice-swallowing-posterior-glottic-stenosis-arytenoid-fixation': {
        "curveball": "The patient asks why you can't just dilate and inject steroid again, as was done twice before. When does dilation alone reasonably work, and why is it likely to fail here?",
        "curveball_answer": "Dilation, steroid injection or a simple scar division can help a limited interarytenoid scar band with mobile joints (Bogdasarian type I). It cannot free cricoarytenoid joints that are fixed or replace missing posterior commissure mucosa, so mature scar with fixation recontracts. That requires restoring posterior glottic width: mucosal flap coverage, a posterior cricoid graft, or arytenoidectomy or cordotomy, often with a tracheostomy in place during healing.",
    },
    'cc-v112-rec-laryngology-voice-swallowing-reinke-edema': {
        "curveball": "Biopsy of the focal irregularity returns severe dysplasia. How does that change your operation on these bilateral polypoid folds, and what technical complication must you avoid?",
        "curveball_answer": "Treatment now centers on the premalignant lesion. Excise the dysplastic epithelium completely for histology, and reduce the Reinke edema with a lateral microflap that evacuates the gelatinous material while preserving the vocal ligament. Avoid raw mucosa on both sides of the anterior commissure at once, which risks an anterior glottic web; staging the sides is an option. Smoking cessation and close laryngoscopic surveillance are mandatory.",
    },
    'cc-v112-rec-laryngology-voice-swallowing-stroboscopy-interpretation': {
        "curveball": "Stroboscopy will not lock on because the singer's voice is severely aperiodic. How should you interpret that study, and what imaging would you use instead?",
        "curveball_answer": "Stroboscopy builds an apparent slow-motion image by sampling successive cycles, so it needs a stable fundamental frequency. With marked aperiodicity the image fails to track and apparent wave loss or asymmetry may be artifact, so do not label a lesion from it. Use high-speed digital imaging or videokymography, which capture real cycle-to-cycle vibration, and correlate with perceptual and acoustic findings.",
    },
    'cc-v112-rec-laryngology-voice-swallowing-tracheobronchial-endoscopy-principles': {
        "curveball": "During rigid bronchoscopy for the toddler, the object fragments, a piece lodges in the trachea, and the child cannot be ventilated. What is your immediate rescue maneuver?",
        "curveball_answer": "If an object occluding the trachea cannot be grasped and removed at once, push it back down into a mainstem bronchus with the bronchoscope so at least one lung can be ventilated. Ventilate through the scope, let the saturation recover with anesthesia, then retrieve it in a controlled way. Afterward, inspect both bronchial trees for residual fragments, mucosal injury or a second object.",
    },
    'cc-v112-rec-laryngology-voice-swallowing-transnasal-esophagoscopy': {
        "curveball": "TNE is normal, but the patient still has solid-food dysphagia and regurgitation. What study comes next, and what disorders could an endoscopy miss?",
        "curveball_answer": "Obtain a barium esophagram, often with a modified barium swallow, to look for a Zenker diverticulum, a cricopharyngeal bar, a subtle stricture or web, extrinsic compression, or the bird-beak sign of achalasia. Endoscopy shows mucosa but can miss dynamic and motility disorders. Add high-resolution esophageal manometry when a motility disorder is suspected. After radiation, a pharyngoesophageal stricture or fibrotic dysmotility are common causes.",
    },
    'cc-v112-rec-laryngology-voice-swallowing-unilateral-vocal-fold-paralysis': {
        "curveball": "Six weeks after surgery the patient develops aspiration pneumonia, and the family wants the voice permanently fixed now. What do you offer?",
        "curveball_answer": "Offer temporary injection augmentation now with a resorbable material. It medializes the fold, improves glottic closure, cough and swallowing safety, and preserves the chance of spontaneous recovery or later reinnervation. Defer permanent framework medialization until recovery is unlikely, typically after many months of observation or when laryngeal EMG predicts a poor prognosis. Early injection may also reduce the later need for open surgery.",
    },
    'cc-v112-rec-laryngology-voice-swallowing-vocal-fold-nodules': {
        "curveball": "After three months of well-adhered voice therapy, the nodules are smaller but the teacher still cannot get through a workday. What are the next options and what would surgery require?",
        "curveball_answer": "First repeat stroboscopy to confirm the diagnosis, since a cyst, polyp or sulcus can masquerade as nodules. If they are persistent true nodules causing significant disability despite good therapy, phonomicrosurgery with superficial microflap excision is reasonable. It must preserve the underlying lamina propria and avoid scarring, and be followed by postoperative voice rest and resumed therapy, because continued phonotrauma causes recurrence.",
    },
    'cc-v112-rec-laryngology-voice-swallowing-vocal-fold-polyp-cyst': {
        "curveball": "At microlaryngoscopy the lesion turns out to be a subepithelial cyst. How do you remove it while protecting the voice, and what do you warn the patient about?",
        "curveball_answer": "Use a microflap: incise lateral to the lesion, elevate the epithelium, dissect the cyst intact out of the superficial lamina propria without entering the vocal ligament, and redrape the epithelium. Rupture or incomplete removal leaves remnant and recurrence. Counsel about possible stiffness or scar with persistent dysphonia, recurrence, a period of voice rest and postoperative therapy, and a possible contralateral reactive lesion needing its own management.",
    },
    'cc-v112-rec-otology-neurotology-ototoxic-noise-induced-hearing-loss': {
        "curveball": "Serial monitoring shows a significant threshold shift in a patient receiving cisplatin. What do you tell the oncology team, and what protective drug exists for children?",
        "curveball_answer": "Report the shift promptly, using criteria such as ASHA's (a 20 dB shift at one frequency or 10 dB at two adjacent frequencies, confirmed on retest), so oncology can weigh dose modification or an alternative agent against cancer control. The otolaryngologist does not stop chemotherapy unilaterally. Sodium thiosulfate is FDA approved to reduce cisplatin ototoxicity in children with localized, non-metastatic solid tumors.",
    },
    'cc-v112-rec-otology-neurotology-temporal-bone-anatomy': {
        "curveball": "The mastoid is sclerotic and you cannot find the lateral semicircular canal. Which landmarks keep you safe, and where is the facial nerve once the canal is identified?",
        "curveball_answer": "Widen the cavity broadly rather than drilling deep. Follow the tegmen, which is reliably superior, and keep the sigmoid sinus posterior and the canal wall anterior, working toward the antrum, which lies deep to Macewen's triangle. A persistent Koerner septum can mimic the floor of the antrum. Once found, the lateral canal marks the second genu of the facial nerve just anterior and inferior to it.",
    },
    'cc-v112-mgt-pediatric-otolaryngology-ankyloglossia-maxillary-frenulum': {
        "curveball": "Feeding assessment confirms tongue-tie related breastfeeding dysfunction and the parents consent to frenotomy. What complications do you counsel about, and what anatomy limits the depth of release?",
        "curveball_answer": "Frenotomy divides only the thin anterior frenulum. Risks are low but include bleeding, infection, ulceration, reattachment needing revision, and failure to improve feeding, which is not guaranteed. Cutting deep risks the submandibular duct openings, lingual vessels and genioglossus. A thick, posterior or fibrous band, or an older child with speech concerns, is better treated with formal frenuloplasty under anesthesia.",
    },
    'cc-v112-mgt-pediatric-otolaryngology-microtia-reconstruction': {
        "curveball": "The family chooses rib-cartilage auricular reconstruction and also wants atresia repair later. Which operation goes first, and why does the order matter?",
        "curveball_answer": "Auricular reconstruction generally comes first. Canal surgery scars and devascularizes the mastoid-region skin that the cartilage framework depends on, so doing atresiaplasty first compromises the ear. The atresia surgeon then works through the reconstructed auricle in coordination with the reconstructive surgeon. Rib-cartilage framework surgery is usually done in mid-childhood, once enough costal cartilage has grown to carve a framework.",
    },
    'cc-v112-rec-pediatric-otolaryngology-cleft-lip-palate-ent-surgical-fundamentals': {
        "curveball": "At age four the child has hypernasal speech and nasal air emission despite an intact palate repair. How do you evaluate this and choose a surgical option?",
        "curveball_answer": "This suggests velopharyngeal dysfunction. Get a speech-language pathology perceptual assessment, rule out an oronasal fistula, and image closure with nasopharyngoscopy or multiview videofluoroscopy. Match surgery to anatomy and gap: Furlow palatoplasty or levator re-repair for a malpositioned levator and short palate, a posterior pharyngeal flap for a central gap, or sphincter pharyngoplasty for lateral gaps. Screen for 22q11.2 deletion, which can medialize the carotids.",
    },
    'cc-v112-rec-pediatric-otolaryngology-congenital-cmv-hearing-loss': {
        "curveball": "By age two the child with congenital CMV has progressed to bilateral severe-to-profound loss. What rehabilitation do you plan, and why does imaging matter for counseling?",
        "curveball_answer": "Refer promptly for cochlear implant candidacy evaluation, after a trial of appropriate amplification, and vaccinate against pneumococcus before implantation. Obtain MRI to confirm the cochlear nerves and to assess the brain. Congenital CMV may cause white-matter abnormalities, calcifications or cortical malformations, which signal neurodevelopmental comorbidity. Many children do well with implants, but these findings make outcomes more variable, so set expectations accordingly.",
    },
    'cc-v112-rec-pediatric-otolaryngology-congenital-neck-masses': {
        "curveball": "The swelling lies along the anterior border of the sternocleidomastoid and there is a draining skin pit just above the clavicle. What anomaly is this, and where does the tract run?",
        "curveball_answer": "This is a second branchial cleft sinus or fistula. Its tract ascends along the carotid sheath, passes between the internal and external carotid arteries, runs superficial to the hypoglossal and glossopharyngeal nerves, and ends at the tonsillar fossa. Excise it once the infection has quieted, using stepladder incisions as needed and removing the complete tract to prevent recurrence.",
    },
    'cc-v112-rec-pediatric-otolaryngology-laryngotracheal-reconstruction': {
        "curveball": "Endoscopy shows grade IV subglottic stenosis that also involves the glottis. Would a single-stage reconstruction with an anterior graft alone be appropriate?",
        "curveball_answer": "Generally not. An anterior graft alone suits lower-grade isolated anterior stenosis. Severe stenosis with glottic or posterior involvement usually needs anterior and posterior costal cartilage grafts, often as a double-stage operation with stenting and the tracheostomy retained. Partial cricotracheal resection is favored for severe isolated subglottic stenosis with an adequate margin below the vocal folds. Glottic involvement predicts a harder decannulation.",
    },
    'cc-v112-rec-pediatric-otolaryngology-microtia-reconstruction': {
        "curveball": "Temporal-bone CT gives a Jahrsdoerfer score of 5 and shows an anomalous facial nerve course. Would you still offer atresiaplasty?",
        "curveball_answer": "Usually not. A Jahrsdoerfer score of 5 or below predicts a poor hearing result, while about 7 or higher identifies better candidates. An anomalous facial nerve, often displaced anterolaterally in the mastoid segment, adds injury risk. With normal hearing in the other ear, offer observation with classroom support or a bone-conduction device, starting on a softband and moving to an implantable device when the child is older.",
    },
    'cc-v112-rec-pediatric-otolaryngology-pediatric-airway-foreign-body': {
        "curveball": "The parents ask whether a flexible bronchoscopy could remove the peanut, because it sounds less invasive than rigid bronchoscopy. How do you answer?",
        "curveball_answer": "Rigid bronchoscopy under general anesthesia remains the standard for extracting pediatric airway foreign bodies. It ventilates through the scope and allows optical forceps and larger instruments, so the team can rescue the airway if the object fragments or migrates. Flexible bronchoscopy is useful diagnostically when the history is equivocal or to look for distal fragments, but it is not the default retrieval tool.",
    },
    'cc-v112-rec-pediatric-otolaryngology-pediatric-aspiration': {
        "curveball": "Rigid laryngoscopy with palpation shows the interarytenoid cleft extends below the vocal folds into, but not through, the cricoid lamina. What type is this and how is it managed?",
        "curveball_answer": "This is a Benjamin-Inglis type II laryngeal cleft. Type I clefts reach only to the level of the vocal folds, and types III and IV extend through the cricoid and into the trachea. Persistent aspiration from a type II cleft is usually treated by endoscopic repair, suturing the interarytenoid mucosa in layers. Deeper clefts need open repair.",
    },
    'cc-v112-rec-pediatric-otolaryngology-pediatric-deep-neck-infection': {
        "curveball": "After 48 hours of IV antibiotics the child is still febrile and now has an ipsilateral Horner syndrome. What complications must you exclude, and how?",
        "curveball_answer": "Failure to improve warrants repeat contrast imaging and drainage of a maturing abscess, usually transorally under a controlled airway. Horner syndrome implies carotid sheath involvement, so obtain CT angiography to look for internal carotid narrowing or pseudoaneurysm and internal jugular thrombosis. Involve vascular or interventional teams for arterial injury. Also check for mediastinal extension and atlantoaxial instability (Grisel syndrome).",
    },
    'cc-v112-rec-pediatric-otolaryngology-pediatric-reflux-eosinophilic-esophagitis': {
        "curveball": "Esophageal biopsies show dense eosinophilic infiltration, above the diagnostic threshold, despite PPI therapy. How is eosinophilic esophagitis treated, and what acute complication should the ENT recognize?",
        "curveball_answer": "EoE is diagnosed by symptoms of esophageal dysfunction plus at least 15 eosinophils per high-power field after excluding other causes. Treatment is coordinated with GI and allergy: PPI, swallowed topical steroids such as budesonide or fluticasone, elimination diets, or dupilumab in eligible children. Untreated disease remodels into fibrostenotic strictures. A child with an acute food impaction needs urgent endoscopic removal, not watchful waiting.",
    },
    'cc-v112-rec-pediatric-otolaryngology-pediatric-tracheostomy-decannulation': {
        "curveball": "The child tolerates daytime capping, but capped polysomnography shows significant obstructive apnea. What do you look for next, and do you proceed with decannulation?",
        "curveball_answer": "Do not decannulate. Re-examine the airway, ideally with direct laryngoscopy and bronchoscopy plus a dynamic assessment, looking for suprastomal granulation or collapse, subglottic stenosis, adenotonsillar hypertrophy, laryngomalacia, or pharyngeal collapse with hypotonia. Treat the cause, for example with granuloma excision, adenotonsillectomy or airway reconstruction, then repeat capped polysomnography before a monitored inpatient decannulation.",
    },
    'cc-v112-rec-pediatric-otolaryngology-pediatric-vocal-fold-immobility': {
        "curveball": "If the immobility followed PDA ligation, which side is typically affected and why, and how long do you observe for recovery before considering durable intervention?",
        "curveball_answer": "The left side, because the left recurrent laryngeal nerve loops under the aortic arch beside the ductus arteriosus. Many infants recover function or compensate, often within the first year, so initial management is observation with feeding modification and an injection laryngoplasty if aspiration is significant. Reinnervation such as ansa cervicalis to recurrent laryngeal nerve is reserved for persistent paralysis with poor voice or glottic insufficiency.",
    },
    'cc-v112-rec-pediatric-otolaryngology-recurrent-respiratory-papillomatosis': {
        "curveball": "Chest CT now shows new cavitating pulmonary nodules in this child with juvenile RRP. What does that mean, and how do you counsel the family?",
        "curveball_answer": "This is distal pulmonary spread, which is uncommon but serious. It is associated with HPV 11 and aggressive disease, causes progressive lung destruction, and carries a higher risk of malignant transformation to squamous cell carcinoma. Laryngeal debulking cannot reach it. Arrange pulmonology and oncology care, serial CT, biopsy of enlarging solid nodules, and systemic therapy such as bevacizumab. Note that PAPZIMEOS is approved only for adults.",
    },
    'cc-v112-rec-pediatric-otolaryngology-subglottic-hemangioma': {
        "curveball": "Before starting propranolol, what screening and safety counseling do you need, and what changes if the infant also has a large segmental facial hemangioma in a beard distribution?",
        "curveball_answer": "Check heart rate and blood pressure, and obtain an ECG if there is bradycardia, an arrhythmia, or a relevant family history. Counsel about hypoglycemia, giving doses with feeds and holding them when the infant is not eating, and about bronchospasm. A beard-distribution segmental hemangioma raises airway involvement and possible PHACE syndrome, so obtain MRI and MRA of the head and neck and echocardiography before propranolol because of cerebrovascular risk.",
    },
    'cc-v112-rec-pediatric-otolaryngology-supraglottoplasty': {
        "curveball": "Two days after supraglottoplasty the infant still has stridor and desaturations. What explains persistent obstruction, and what is the feared late complication of an over-aggressive procedure?",
        "curveball_answer": "Consider postoperative edema, inadequate release, a missed synchronous lesion such as subglottic stenosis, tracheomalacia or vocal fold paralysis, and neurologic or syndromic hypotonia, which predicts poorer response. Support the airway in a monitored setting and re-endoscope with full laryngoscopy and bronchoscopy if not improving. Supraglottic stenosis is the feared complication. Avoid it by preserving interarytenoid mucosa and not over-resecting bilaterally.",
    },
    'cc-v112-rec-pediatric-otolaryngology-tracheomalacia-bronchomalacia': {
        "curveball": "Dynamic bronchoscopy shows severe anterior compression where the innominate artery crosses, plus posterior membranous intrusion. Which operations address each component, and what is the bailout?",
        "curveball_answer": "Anterior compression responds to aortopexy, which pulls the aorta and innominate artery forward and lifts the anterior tracheal wall, or to anterior tracheopexy. Posterior membranous intrusion, common after esophageal atresia repair, is treated with posterior tracheopexy that fixes the membrane to the anterior longitudinal ligament of the spine. Many centers address both in one procedure. The bailout is tracheostomy with a long tube and positive pressure; stents are a last resort.",
    },
    'cc-v112-mgt-rhinology-allergy-skull-base-frontal-recess-frontal-sinus': {
        "curveball": "Mid-dissection you find a suprabulla frontal cell extending along the skull base into the frontal sinus. Why is it dangerous, and how do you remove it safely?",
        "curveball_answer": "It forms the posterior wall of the drainage pathway, where the skull base is thinnest and the anterior ethmoid artery often runs, sometimes in a mesentery below the skull base. Locate the artery on CT first. Work anterior to it with angled endoscopes and curved instruments, fracturing the cell wall forward and medially away from the skull base. Preserve mucosa circumferentially to prevent stenosis.",
    },
    'cc-v112-mgt-rhinology-allergy-skull-base-frontal-sinusotomy-draf-procedures': {
        "curveball": "The disease is a far-lateral supraorbital frontal mucocele, and the sinus is narrow front to back. Would a Draf III reach it, or what approach would you choose?",
        "curveball_answer": "Possibly not. Far-lateral disease beyond the plane of the lamina papyracea may be unreachable with angled instruments even after a Draf III, and a narrow anteroposterior dimension with a thick frontal beak limits how wide the neo-ostium can be made. Options include a combined endoscopic approach with an above-and-below trephination, or an osteoplastic flap, with or without obliteration, when endoscopic access is inadequate.",
    },
    'cc-v112-mgt-rhinology-allergy-skull-base-sphenoidotomy': {
        "curveball": "While removing an intersinus septum you get brisk pulsatile bleeding from the lateral sphenoid wall. What do you do in the next few minutes and afterward?",
        "curveball_answer": "Assume an internal carotid artery injury. Call for help, tell anesthesia, keep normotension, secure blood, and use two suctions in a four-hand technique to see the site. Pack it with a crushed muscle patch or targeted packing, avoiding total nasal packing that hides ongoing bleeding. Proceed directly to angiography for stenting, coiling or occlusion, then repeat angiography to exclude a pseudoaneurysm. Prevent this by never twisting septa off.",
    },
    'cc-v112-rec-rhinology-allergy-skull-base-endoscopic-csf-leak-repair-nasoseptal-flap': {
        "curveball": "Six weeks after an apparently successful repair the leak recurs, and lumbar puncture shows an elevated opening pressure. How do you manage it?",
        "curveball_answer": "Treat this as idiopathic intracranial hypertension, a major driver of recurrence and of new leaks at other sites. Coordinate with neurosurgery and neuro-ophthalmology to lower intracranial pressure through weight loss, acetazolamide, and, when needed, a CSF shunt or venous sinus stenting. Check for papilledema. Revise the repair with a robust multilayer or vascularized reconstruction, and image for additional skull-base defects.",
    },
    'cc-v112-rec-rhinology-allergy-skull-base-endoscopic-maxillary-antrostomy': {
        "curveball": "During the uncinectomy, orbital fat suddenly appears in the field. What happened, and how do you manage it intraoperatively and afterward?",
        "curveball_answer": "The lamina papyracea has been breached. Stop working there. Do not pull on the fat or use the microdebrider near it, which risks medial rectus injury. Ballot the globe while watching the defect, check pupils, and leave the fat alone. Avoid packing against the orbit, instruct no nose blowing, and monitor vision and pain. An expanding hematoma requires lateral canthotomy and cantholysis.",
    },
    'cc-v112-rec-rhinology-allergy-skull-base-epistaxis-surgical-control': {
        "curveball": "This bleed becomes hemodynamically significant on apixaban. Should you reverse the anticoagulation, and with what?",
        "curveball_answer": "The 2020 Epistaxis CPG advises first controlling bleeding with local measures and not reversing anticoagulation routinely. Reversal is reserved for life-threatening bleeding, decided with the prescribing clinician because of thrombotic risk. For an apixaban-related life-threatening hemorrhage, give four-factor prothrombin complex concentrate. Meanwhile, protect the airway, resuscitate, and move to endoscopic sphenopalatine artery ligation or embolization if local control fails.",
    },
    'cc-v112-rec-rhinology-allergy-skull-base-ethmoidectomy': {
        "curveball": "Twenty minutes after surgery the patient has painful proptosis, a tense orbit and declining vision. What do you do immediately?",
        "curveball_answer": "Treat it as an orbital hematoma causing compartment syndrome. Perform an immediate bedside lateral canthotomy with inferior cantholysis, without waiting for imaging, and remove any nasal packing. Medical adjuncts such as mannitol, acetazolamide and steroids support but do not replace decompression. Get urgent ophthalmology involvement. If pressure stays high, do an endoscopic medial orbital decompression and control the bleeding vessel, often the anterior ethmoid artery.",
    },
    'cc-v112-rec-rhinology-allergy-skull-base-frontal-recess-frontal-sinus': {
        "curveball": "Before surgery the patient develops a soft, fluctuant forehead swelling with fever. What is it, and how does your plan change?",
        "curveball_answer": "This is Pott puffy tumor, a subperiosteal abscess from frontal bone osteomyelitis. Obtain urgent contrast CT and MRI, since epidural abscess, subdural empyema and venous sinus thrombosis frequently coexist. Start IV antibiotics and drain promptly, combining endoscopic frontal sinusotomy with external drainage or trephination as needed. Involve neurosurgery for any intracranial collection. Expect a prolonged antibiotic course for osteomyelitis.",
    },
    'cc-v112-rec-rhinology-allergy-skull-base-frontal-sinusotomy-draf-procedures': {
        "curveball": "Six months after a Draf III, the neo-ostium has narrowed and symptoms are returning. What predisposes to stenosis, and how do you manage it?",
        "curveball_answer": "Risk factors include a small initial opening, circumferential exposed bone, an incompletely drilled frontal beak, and ongoing eosinophilic polyp disease. Prevent it with a maximal opening, mucosal flaps or free grafts over exposed bone, and topical steroid irrigation. For restenosis, optimize medical therapy, including type 2 biologics when appropriate, and revise endoscopically. Osteoplastic flap with obliteration remains the salvage option.",
    },
    'cc-v112-rec-rhinology-allergy-skull-base-fungal-ball': {
        "curveball": "The same CT picture appears in a neutropenic patient with pale, insensate middle-turbinate mucosa and new facial numbness. How does management change?",
        "curveball_answer": "Suspect acute invasive fungal sinusitis, which is an emergency. Perform urgent endoscopic biopsy with frozen section of the abnormal mucosa, and get MRI for orbital, pterygopalatine and intracranial extent. Start empiric liposomal amphotericin B until the organism is known, and reverse the immune deficit or acidosis where possible. Debride to bleeding, viable tissue, repeating as needed with multidisciplinary infectious disease input.",
    },
    'cc-v112-rec-rhinology-allergy-skull-base-intracranial-complications-of-sinusitis': {
        "curveball": "MRI shows a frontal subdural empyema, and the teenager has a seizure. Who drains what, and in what order?",
        "curveball_answer": "Subdural empyema is a neurosurgical emergency. Neurosurgery evacuates it promptly, usually by craniotomy, while otolaryngology performs endoscopic sinus surgery for source control and cultures, ideally under the same anesthetic. Give high-dose IV antibiotics with CNS penetration, typically covering streptococci, staphylococci including MRSA, and anaerobes, and start antiseizure medication. Watch for venous sinus thrombosis and reimage if the neurologic status changes.",
    },
    'cc-v112-rec-rhinology-allergy-skull-base-juvenile-nasopharyngeal-angiofibroma': {
        "curveball": "Imaging shows extension into the cavernous sinus with feeding vessels from the internal carotid artery. How does that change your plan and counseling?",
        "curveball_answer": "Internal carotid supply cannot be reduced by external carotid embolization, and cavernous sinus extension raises the risk of bleeding, residual disease and cranial nerve injury. Plan with a skull-base team for a staged or combined endoscopic resection. Deliberately leaving a small cavernous remnant under MRI surveillance, or radiotherapy for unresectable residual tumor, are accepted options. Counsel about recurrence, which is highest with skull-base or intracranial extension.",
    },
    'cc-v112-rec-rhinology-allergy-skull-base-olfactory-dysfunction': {
        "curveball": "The patient asks what treatment actually helps postviral smell loss and whether the parosmia means things are getting worse. What do you tell her?",
        "curveball_answer": "Olfactory training has the best supporting evidence: sniffing several distinct odors twice daily for months. Systemic steroids are not routinely recommended for established postviral loss. Parosmia commonly appears during regeneration and often accompanies recovery rather than signaling decline. Recovery can be slow and incomplete. Advise smoke and gas detectors, checking food dates, and nutritional and mood support.",
    },
    'cc-v112-rec-rhinology-allergy-skull-base-sinonasal-malignancy': {
        "curveball": "Biopsy returns esthesioneuroblastoma, high Hyams grade, Kadish C, with a clinically negative neck. How do you treat it, and how long should surveillance continue?",
        "curveball_answer": "Standard treatment is surgical resection with negative margins, endoscopic or combined craniofacial depending on extent, including the cribriform plate, dura and olfactory bulb as needed, followed by adjuvant radiotherapy. Consider chemotherapy for high-grade or advanced disease. Elective neck irradiation is often considered for the cN0 neck given the nodal failure risk. Because recurrences can appear very late, surveillance should continue for decades.",
    },
    'cc-v112-rec-rhinology-allergy-skull-base-sphenoidotomy': {
        "curveball": "Why is the sphenoidotomy usually enlarged medially and inferiorly, and what bleeding risk comes with taking it down toward the choana?",
        "curveball_answer": "The optic nerve and internal carotid artery lie superolaterally, so medial and inferior enlargement keeps instruments away from them. Inferior enlargement, however, crosses the posterior septal branch of the sphenopalatine artery, which runs across the sphenoid face below the ostium. Injuring it causes brisk bleeding, usually controlled with bipolar cautery, and sacrifices the pedicle of a future nasoseptal flap, so preserve it when skull-base work is possible.",
    },
    'cc-v231-rhinology-allergic-rhinitis-ar': {
        "curveball": "Despite intranasal steroid and antihistamine, cat symptoms remain uncontrolled. The patient asks for sublingual tablets instead of shots. Is that an option?",
        "curveball_answer": "Not for cat. In the US, sublingual tablets are approved only for grass, short ragweed and house dust mite. For cat sensitization that correlates with symptoms, subcutaneous immunotherapy with standardized cat extract is the immunotherapy option, as discussed in the 2024 immunotherapy CPG. It is given where anaphylaxis can be treated, and exposure reduction remains part of the plan. Nasal surgery does not treat the allergy.",
    },
    'cc-v231-rhinology-local-allergic-rhinitis-lar': {
        "curveball": "Nasal allergen provocation is positive for grass pollen and symptoms persist despite intranasal steroids. Is allergen immunotherapy reasonable, and how strong is the evidence?",
        "curveball_answer": "It can be considered for selected patients with demonstrated local reactivity and inadequate control. Small randomized trials of immunotherapy with grass pollen and house dust mite in local allergic rhinitis have shown symptom and provocation-test benefit. The evidence is limited and immunotherapy for this phenotype is not yet standard, so counsel it as an emerging option and continue intranasal steroids, antihistamines and avoidance.",
    },
    'cc-v112-rec-sleep-surgery-central-events-hypoventilation': {
        "curveball": "The patient has heart failure with a reduced ejection fraction and predominantly central apnea. Is adaptive servo-ventilation an option, and would hypoglossal stimulation help?",
        "curveball_answer": "Adaptive servo-ventilation is contraindicated in symptomatic heart failure with reduced ejection fraction and predominantly central apnea, because SERVE-HF showed increased cardiovascular mortality. Optimize heart failure therapy and consider CPAP, supplemental oxygen, or transvenous phrenic nerve stimulation with sleep and cardiology colleagues. Hypoglossal nerve stimulation treats obstructive collapse only; a high central or mixed event burden excludes candidacy.",
    },
    'cc-v112-rec-sleep-surgery-dise': {
        "curveball": "DISE shows complete concentric collapse at the velum. How does that affect hypoglossal nerve stimulation candidacy, and what can you offer instead?",
        "curveball_answer": "Complete concentric velopharyngeal collapse is an exclusion for hypoglossal nerve stimulation, because it predicted poor response in the pivotal trials. Options include palatal surgery such as expansion sphincter pharyngoplasty to convert the pattern, followed by repeat DISE, or alternatives such as maxillomandibular advancement, an oral appliance or renewed PAP efforts. Weight loss may also change the collapse pattern.",
    },
    'cc-v112-rec-sleep-surgery-hns-activation-programming': {
        "curveball": "At the titration study, the tongue protrudes well but the palate still collapses and the apnea index stays high. What programming steps come before declaring failure?",
        "curveball_answer": "Confirm adherence and weight stability, then retitrate. Change the electrode configuration, amplitude, pulse width or rate to favor protrusor recruitment and improve palatal coupling. Awake or drug-induced endoscopy during stimulation shows whether the palate opens. If palatal collapse persists despite good protrusion, consider adjuncts such as palatal surgery, an oral appliance or combined PAP, rather than simply raising the voltage.",
    },
    'cc-v112-rec-sleep-surgery-maxillomandibular-advancement': {
        "curveball": "What is the most common lasting sensory complication after maxillomandibular advancement, which osteotomy causes it, and how do you counsel the patient?",
        "curveball_answer": "Lower lip and chin numbness from inferior alveolar nerve injury during the bilateral sagittal split osteotomy of the mandible. Altered sensation is very common early and usually improves, but some patients keep permanent hypoesthesia. The Le Fort I osteotomy can affect infraorbital sensation less often. Also discuss malocclusion, relapse, nonunion, facial appearance change and the need for orthodontic coordination.",
    },
    'cc-v112-rec-sleep-surgery-oral-appliance-therapy': {
        "curveball": "After titration, his snoring has stopped and he feels more rested. Is that enough to confirm the appliance is working?",
        "curveball_answer": "No. Symptom improvement and absent snoring do not reliably reflect the residual apnea index. Guidelines recommend follow-up sleep testing with the appliance in place after final titration to verify efficacy. If residual disease remains, adjust or change therapy. Continue dental follow-up for bite change, tooth movement and temporomandibular symptoms, because these develop over years of use.",
    },
    'cc-v112-rec-sleep-surgery-pap-troubleshooting': {
        "curveball": "The mask and nasal problems are fixed and adherence is good, but the download now shows central events emerging after the pressure was raised. What is happening, and what do you do?",
        "curveball_answer": "This is treatment-emergent central sleep apnea, which can follow PAP initiation or over-titration. It often settles with continued CPAP over weeks, so avoid further pressure increases and consider lowering the pressure. If it persists and causes symptoms, a sleep medicine review can consider bilevel PAP with a backup rate or adaptive servo-ventilation, after confirming the ejection fraction is not reduced.",
    },
    'cc-v112-rec-sleep-surgery-tongue-base-surgery': {
        "curveball": "DISE shows the epiglottis folding back against the posterior pharyngeal wall instead of tongue-base collapse. Does tongue-base reduction still make sense?",
        "curveball_answer": "Only if the epiglottis is being pushed back by the tongue base. If the collapse is primary to a floppy epiglottis, tongue-base reduction alone often fails, and a targeted epiglottic procedure such as partial epiglottectomy or epiglottopexy is more logical. Primary epiglottic collapse may also limit the response to hypoglossal stimulation and can make PAP uncomfortable, so define the mechanism before choosing a procedure.",
    },
    'cc-v112-mgt-thyroid-parathyroid-salivary-four-gland-parathyroid-exploration': {
        "curveball": "You find three normal glands and cannot locate a missing inferior parathyroid. Where do you search, and where would you look for a missing superior gland?",
        "curveball_answer": "Inferior glands, from the third pharyngeal pouch, have a long descent with the thymus. Search the thyrothymic ligament and cervical thymus, the most common ectopic site, then the anterior mediastinum, an intrathyroidal position, or an undescended site near the carotid bifurcation. Superior glands, from the fourth pouch, hide in the tracheoesophageal groove, retroesophageal space, posterior mediastinum or carotid sheath. Cervical thymectomy is a reasonable step.",
    },
    'cc-v112-mgt-thyroid-parathyroid-salivary-parathyroid-carcinoma': {
        "curveball": "Two years later calcium rises again and imaging shows unresectable lung metastases. How do you control the hypercalcemia, and what drives prognosis?",
        "curveball_answer": "Hypercalcemia, not tumor bulk, causes most morbidity and death in parathyroid carcinoma. Treat with hydration, the calcimimetic cinacalcet, which is approved for this indication, and bisphosphonates or denosumab. Resect or ablate metastases when feasible, since debulking lowers PTH. Conventional chemotherapy and radiotherapy have limited roles. Prognosis depends on complete initial en bloc resection and on the ability to control calcium.",
    },
    'cc-v112-mgt-thyroid-parathyroid-salivary-reoperative-hyperparathyroidism': {
        "curveball": "Ultrasound, sestamibi and 4D CT all fail to localize the culprit gland. What other tests should you consider before reoperating, and why not explore blindly?",
        "curveball_answer": "First recheck the diagnosis, including a urine calcium to creatinine clearance ratio to exclude familial hypocalciuric hypercalcemia. Then consider choline PET/CT where available, or selective venous sampling for PTH gradients to lateralize the gland. A blind scarred-neck exploration has a lower cure rate and higher risks of recurrent laryngeal nerve injury and permanent hypoparathyroidism. Cryopreserve resected parathyroid tissue when available.",
    },
    'cc-v112-mgt-thyroid-parathyroid-salivary-secondary-tertiary-hyperparathyroidism': {
        "curveball": "Years after total parathyroidectomy with forearm autotransplantation, PTH rises again. How do you tell graft-dependent recurrence from a missed neck gland?",
        "curveball_answer": "Compare PTH drawn from the grafted arm with the opposite arm, or measure PTH before and during tourniquet occlusion of the graft arm (the Casanova test). A clear gradient or a fall with occlusion points to graft hyperplasia, which can be partly excised under local anesthesia. No gradient suggests a supernumerary or remnant cervical or mediastinal gland, which needs neck and mediastinal imaging.",
    },
    'cc-v112-mgt-thyroid-parathyroid-salivary-submandibular-gland-excision': {
        "curveball": "Final pathology shows adenoid cystic carcinoma with perineural invasion in the excised submandibular gland. What further treatment and surveillance do you plan?",
        "curveball_answer": "Review the margins and obtain MRI to look for perineural spread along the lingual and hypoglossal nerves. Re-resect clearly positive margins when feasible. Adjuvant radiotherapy is standard with perineural invasion or close or positive margins, and covers the nerve pathways. Neck management depends on grade, nodes and team practice. Surveillance is long term, with chest imaging, because lung metastases and late recurrence are characteristic.",
    },
    'cc-v112-rec-thyroid-parathyroid-salivary-anaplastic-thyroid-cancer': {
        "curveball": "The BRAF V600E result is positive. What treatment do you start, and can surgery come back into the plan later?",
        "curveball_answer": "Start dabrafenib plus trametinib promptly, coordinated with oncology, since it is approved for BRAF V600E anaplastic thyroid cancer and responses can be rapid. Reassess resectability on treatment. Neoadjuvant targeted therapy can turn initially unresectable disease into disease that can be completely resected, followed by adjuvant radiation or chemoradiation, with better local control. Avoid an elective tracheostomy through tumor when the airway is maintainable.",
    },
    'cc-v112-rec-thyroid-parathyroid-salivary-graves-disease-toxic-goiter': {
        "curveball": "On the second postoperative day she has perioral tingling and a positive Chvostek sign. Why is this more common after thyroidectomy for Graves disease, and how do you treat it?",
        "curveball_answer": "Graves disease raises the risk of transient hypocalcemia, both from parathyroid devascularization in a hypervascular gland and from hungry bone remineralization after thyrotoxic bone turnover. Check calcium, PTH and magnesium. Give oral calcium, adding calcitriol if PTH is low. Use IV calcium gluconate with cardiac monitoring for tetany, severe symptoms or QT prolongation. Repleting vitamin D before surgery lowers the risk.",
    },
    'cc-v112-rec-thyroid-parathyroid-salivary-indeterminate-thyroid-cytology-molecular-testing': {
        "curveball": "The molecular panel reports a BRAF V600E mutation. How does that change the operation compared with a RAS-mutated result?",
        "curveball_answer": "BRAF V600E is highly specific for papillary carcinoma, so treat the nodule as cancer and size the operation by ATA 2025 risk. For a 2.1-cm nodule without nodes or extrathyroidal extension, lobectomy is acceptable, with total thyroidectomy reserved for higher-risk features. A RAS mutation carries intermediate risk across follicular adenoma, NIFTP, follicular-variant papillary and follicular carcinoma, so diagnostic lobectomy is usually appropriate.",
    },
    'cc-v112-rec-thyroid-parathyroid-salivary-men2-ret': {
        "curveball": "Workup confirms a pheochromocytoma. How do you prepare for adrenalectomy, and what do preoperative calcitonin and CEA tell you about the thyroid operation?",
        "curveball_answer": "Start alpha-adrenergic blockade, such as phenoxybenzamine or doxazosin, with liberal salt and fluid intake. Add beta-blockade only after adequate alpha-blockade, and perform adrenalectomy before thyroidectomy. Calcitonin and CEA estimate the burden of medullary carcinoma: rising levels predict nodal metastases and guide central and lateral neck dissection, and markedly elevated calcitonin calls for imaging to detect distant metastases before surgery.",
    },
    'cc-v112-rec-thyroid-parathyroid-salivary-reoperative-thyroid-surgery': {
        "curveball": "On waking from surgery the patient has stridor, and laryngoscopy shows both vocal folds near the midline. What do you do now, and how could intraoperative monitoring have changed the plan?",
        "curveball_answer": "Bilateral vocal fold paralysis is an airway emergency. Reintubate or perform a tracheostomy as needed, give steroids, and observe if neuropraxia is likely, since function may return. Persistent paralysis can be treated with posterior cordotomy, partial arytenoidectomy, suture lateralization or selective reinnervation. With a pre-existing paresis, loss of signal on neuromonitoring should have prompted stopping before the contralateral dissection or staging the operation.",
    },
    'cc-v112-rec-thyroid-parathyroid-salivary-sialendoscopy': {
        "curveball": "The stone measures several millimeters and is palpable at the submandibular hilum, too large for basket retrieval. Can you still preserve the gland?",
        "curveball_answer": "Often, yes. A sialendoscopy-assisted transoral approach opens the duct along the floor of the mouth over the palpable stone, removes it, and confirms ductal clearance endoscopically. Protect the lingual nerve, which crosses Wharton duct near the hilum. Intraductal laser or other lithotripsy is an alternative where available. Gland function often recovers after the obstruction is relieved, so reserve excision for failure or a nonfunctional gland.",
    },
}
