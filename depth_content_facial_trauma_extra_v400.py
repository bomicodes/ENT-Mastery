"""v40.0 -- Deepen the nine thinner trauma-adjacent curriculum topics that were
identified as accurate but under-sourced (generic "Pasha 6e"/"KJ Lee 12e"
citations, auto-generated single-word tags) compared to the rest of the
Facial Plastics/Trauma domain.

Cross-referenced against:
  - Resident Manual of Trauma to the Face, Head, and Neck (AAO-HNS/ENTNET),
    chapters 2-4 (general principles, upper/midfacial trauma) and 9
    (soft-tissue injuries), and 10 (foreign bodies/caustic ingestion).
  - Cummings Otolaryngology--Head and Neck Surgery, 7e, ch 19-20 (facial
    trauma) and ch 30 (nasal fractures) -- confirmed timing windows against
    primary text (e.g., "ideal timing for closed nasal reduction is between
    2 and 10 days after injury," p.554).
  - ESGE 2016 Clinical Guideline, "Removal of foreign bodies in the upper
    gastrointestinal tract in adults" -- emergent/urgent/elective triage by
    object type and location.
  - NASPGHAN Endoscopy Committee clinical report, "Management of Ingested
    Foreign Bodies in Children" (2015) -- pediatric timing framework and
    coin-observation windows.
  - Gordon, Barfield & Gold, "Early management of acute caustic ingestion in
    pediatrics," J Pediatr Gastroenterol Nutr 2025 (PMID 39887462) -- current
    (2025) recommendation that EGD within 24h is optimal, that steroid/
    antibiotic/acid-suppression use remains an open evidence question rather
    than a settled recommendation, and early NGT placement under direct
    endoscopic visualization for Zargar >=2b injury.

This batch adds depth and cited decision frameworks. The v40.0
text should be reviewed against current guidelines and source texts before
being considered fully clinically validated (contrast nonfunctional_larynx_duplicate_merge_v399.py
and depth_content_pediatric_ent_v397.py, which did fix genuine errors).
"""

DEPTH_V400 = {
    "Facial Plastics / Trauma": {
        "ZMC / Orbital Trauma": {
            "recognize": (
                "Vision first: check acuity, pupils/RAPD, color vision and globe position before "
                "palpating the fracture. A tense, proptotic orbit with severe pain, rapidly worsening "
                "vision or elevated intraocular pressure (when globe rupture is excluded) indicates orbital "
                "compartment syndrome until proven otherwise -- a true ophthalmic emergency, not an "
                "elective fracture problem. Malar flattening, infraorbital numbness, trismus, palpable "
                "step-offs and diplopia define the ZMC injury itself once the eye is confirmed safe. "
                "A child with minimal external bruising, nausea/vomiting and restricted upgaze after "
                "seemingly minor orbital trauma has a trapdoor fracture with muscle entrapment until "
                "proven otherwise -- the oculocardiac reflex (bradycardia, nausea) is a red flag, not "
                "a coincidental vagal response."
            ),
            "localize": (
                "The ZMC is a tetrapod suspended at the zygomaticofrontal, zygomaticomaxillary, "
                "zygomaticosphenoid and zygomaticotemporal (arch) articulations; accurate reduction of "
                "the sphenozygomatic suture in particular is the key to restoring three-dimensional "
                "projection, since it is the most reliable stable reference point. Do not interpret "
                "a relatively soft orbit or an equivocal initial exam as exclusion of a developing "
                "orbital compartment syndrome; reassess vision and pupils urgently and check pressure "
                "only if an open-globe injury is excluded. In an orbital fracture with suspected "
                "entrapment, safe forced-duction testing by a trained examiner objectively tests "
                "passive motility: restriction supports mechanical entrapment, whereas preserved "
                "passive movement despite abnormal active movement suggests paresis or another "
                "nonrestrictive cause; interpret results with the clinical examination and CT."
            ),
            "workup": (
                "Document acuity, pupils/RAPD, extraocular movements, diplopia fields and globe position "
                "without delaying emergency decompression; assess intraocular pressure only when an open "
                "globe is not suspected. "
                "Thin-cut maxillofacial/orbital CT defines ZMC displacement and orbital-wall/floor "
                "defect. When entrapment is suspected from restricted motility, a trapdoor pattern or oculocardiac symptoms, "
                "arrange prompt ophthalmology/orbital specialist evaluation and forced-duction testing to objectify mechanical restriction when safe after excluding an open globe; it is particularly valuable if the patient cannot cooperate and should not delay urgent release for compelling clinical entrapment. "
                "Diplopia immediately after trauma is not by itself an indication for floor repair, "
                "since edema alone can transiently restrict movement -- reassess after edema resolves "
                "unless there is a hard sign (entrapment, oculocardiac reflex, non-resolving "
                "restriction) that mandates urgent action."
            ),
            "manage": (
                "Observe nondisplaced fractures without functional or aesthetic consequence. Repair "
                "ZMC fractures for malar deformity, unstable facial width/projection, trismus or "
                "meaningful orbital-volume change. Orbital repair is for persistent functionally "
                "significant diplopia with restrictive findings, clinically meaningful enophthalmos/"
                "hypoglobus, or a volume-changing defect; pediatric trapdoor entrapment is more urgent "
                "because incarcerated muscle can become ischemic within hours. Treat suspected orbital "
                "compartment syndrome immediately with decompression -- do not wait for CT or "
                "definitive fracture planning."
            ),
            "operate": (
                "For ZMC ORIF, restore three-dimensional position starting from the most reliable "
                "stable reference point (commonly the sphenozygomatic suture and zygomatic arch) before "
                "committing to orbital floor reconstruction; the number and location of fixation points "
                "follow instability/displacement rather than a fixed recipe. Recheck globe position and "
                "forced ductions before orbital manipulation, after releasing entrapped tissue, and after implant placement to document restored passive motility. Orbital implants restore "
                "the posterior ledge/contour without entrapping soft tissue or impinging the orbital "
                "apex. Lateral canthotomy with inferior cantholysis is the vision-saving bedside "
                "decompression for orbital compartment syndrome and should never be delayed for "
                "imaging when the clinical diagnosis is clear; reattach the canthal tendon to the "
                "lateral orbital rim, inside and behind it, once decompression and definitive repair "
                "are complete."
            ),
            "teach": (
                "Boards/chief framework: vision first, fracture second. ZMC repair restores "
                "three-dimensional projection from a stable reference point; orbital-floor repair "
                "treats entrapment and volume change, not CT defect size alone. A firm, proptotic "
                "orbit with worsening pain and vision is canthotomy-now, not CT-first. A child with "
                "nausea/bradycardia and restricted upgaze after minor-appearing orbital trauma is a "
                "trapdoor fracture until proven otherwise."
            ),
            "source_basis": [
                "Cummings Otolaryngology--Head and Neck Surgery, 7e, facial trauma chapters -- orbital evaluation and forced ductions when an unconscious patient cannot participate; forced ductions before and after orbital operative maneuvers",
                "Resident Manual of Trauma to the Face, Head, and Neck (AAO-HNS), ch 3 -- retrobulbar hematoma presentation, forced duction testing, canthotomy/cantholysis technique, medial canthal tendon laxity as partial self-decompression",
                "Pasha & Golub, Otolaryngology--Head and Neck Surgery Clinical Reference Guide, 6e -- ZMC tetrapod concept and orbital fracture management thresholds",
            ],
            "evidence_calibrated": "v40.1-cummings-2026-guideline-reconciliation",
        },
        "Nasal Fracture": {
            "workup": (
                "CT is not routinely required for an isolated uncomplicated nasal fracture; obtain "
                "imaging when broader midface/NOE/orbital/skull-base injury is suspected. Document "
                "preinjury appearance if photographs are available, nasal airway, septum, ocular "
                "findings and CSF-leak signs. Reexamine 2-3 days after injury once swelling has begun "
                "to subside if the initial exam is obscured, but never defer evaluation of a possible "
                "septal hematoma to that follow-up visit."
            ),
            "manage": (
                "Observe fractures without meaningful deformity or obstruction. When reduction is "
                "indicated, timing is the central decision: per Cummings 7e, the ideal window for "
                "closed reduction in adults is between 2 and 10 days after injury -- early enough that "
                "fibrous union and early osseous remodeling (which begin around 10 days to 2 weeks and "
                "progressively limit successful realignment) have not yet set in, and later attempts are less predictable. Children heal faster and generally need earlier reassessment and reduction, "
                "commonly within approximately 3-7 days, individualized to swelling and age. Septal "
                "fracture/dislocation may require concomitant septal reduction, since failing to "
                "reduce the septum is a leading cause of failed or relapsed nasal reduction. Delayed "
                "persistent deformity or obstruction after this window is treated with definitive "
                "septorhinoplasty rather than a late closed-reduction attempt."
            ),
            "operate": (
                "Closed reduction restores bony alignment with intranasal/external manipulation "
                "(Boies or Joker elevator, or Asch/Walsham forceps for the septum), reducing the "
                "septum before the nasal bones since septal tension is a common cause of relapse; "
                "outcomes are similar with local or general anesthesia. Splint and tape "
                "post-reduction (packing is not routinely required, though it can support a depressed "
                "or unstable segment); a dorsal splint is typically left 5-7 days. Open reduction is "
                "reserved for bilateral fractures with significant dorsal/septal pathology, comminuted "
                "or unstable injuries, and late presentations where bony union has already begun -- it "
                "allows aggressive mobilization/osteotomy that closed technique cannot achieve. "
                "Preserve adequate dorsal/caudal L-strut support whenever cartilage is manipulated or "
                "resected. Drain septal hematoma immediately regardless of timing considerations for "
                "the bony fracture."
            ),
            "teach": (
                "Boards/chief framework: the emergency in a 'simple nasal fracture' is the septal "
                "hematoma, not the bone. CT is usually unnecessary for an isolated fracture. Timing "
                "matters and has real numbers behind it: reduce within roughly 2-10 days in adults "
                "(before fibrous consolidation begins around 10 days-2 weeks), earlier in children, often within a week; late deformity belongs to septorhinoplasty, not a heroic delayed closed "
                "attempt."
            ),
            "source_basis": [
                "Cummings Otolaryngology--Head and Neck Surgery, 7e, ch 30 (Nasal Fractures) -- adult reduction timing, earlier pediatric management as healing progresses, septal-reduction-before-bone principle, splint duration; pediatric timing individualized to age, swelling, and deformity",
                "Pasha & Golub, Otolaryngology--Head and Neck Surgery Clinical Reference Guide, 6e -- closed vs open reduction indications",
                "Resident Manual of Trauma to the Face, Head, and Neck (AAO-HNS), ch 4 -- closed vs open reduction technique and instrumentation",
            ],
            "evidence_calibrated": "v40.1-cummings-2026-guideline-reconciliation",
        },
        "Le Fort / Panfacial Trauma": {
            "recognize": (
                "Panfacial trauma involves fractures across multiple facial thirds/buttresses "
                "simultaneously, so restoring any single fracture in isolation risks reconstructing "
                "the face onto a displaced, unstable foundation. Recognition requires assessing "
                "occlusion, facial width/height/projection and ocular/neurologic status together, not "
                "fracture by fracture; a mobile maxilla on bimanual manipulation (grasping the anterior "
                "maxillary alveolus and gently rocking it against a hand stabilizing the frontal bone) "
                "confirms a Le Fort-pattern fracture even when swelling obscures the exam."
            ),
            "localize": (
                "Le Fort I is a low, horizontal fracture separating the maxillary alveolus/hard palate "
                "from the rest of the midface, running through the pyriform aperture and lateral "
                "maxillary sinus walls to the pterygoid plates. Le Fort II is a pyramidal fracture "
                "running through the nasal bones, medial orbital floor/rim and zygomaticomaxillary "
                "buttress to the pterygoid plates -- it separates the central midface, nose and "
                "maxilla together as one mobile segment. Le Fort III is complete craniofacial "
                "disjunction, extending through the zygomaticofrontal sutures, orbits and "
                "nasofrontal junction so the entire midface separates from the skull base. Few "
                "fractures match these patterns exactly (they are frequently asymmetric or mixed), "
                "but the classification remains clinically useful for anticipating which pterygoid, "
                "orbital and buttress structures are involved. Panfacial injury layers mandible, "
                "naso-orbito-ethmoid and frontal sinus fractures onto this framework, so full "
                "localization means mapping every disrupted vertical buttress (nasomaxillary, "
                "zygomaticomaxillary, pterygomaxillary) and horizontal buttress (frontal bar, "
                "infraorbital rim, maxillary alveolus/palate) on CT before planning fixation order."
            ),
            "workup": (
                "Thin-cut facial CT with multiplanar reconstruction, combined with ocular/neurologic "
                "and dental/occlusal assessment. Identify at least one stable, uninjured reference "
                "point (an intact mandibular condyle-ramus unit, or an uninjured hemiface) before "
                "planning fixation sequence, since panfacial repair is built outward from whatever "
                "structure is not displaced."
            ),
            "manage": (
                "Establish occlusion and stable facial buttresses using either a bottom-up strategy "
                "(fix the mandible first, then build the midface up against it) or a top-down/"
                "outside-in strategy (fix stable cranial/zygomatic reference points first, then work "
                "inward) depending on which structures remain stable in a given patient; there is no "
                "single correct order for every panfacial injury, only a stable-reference-point-first "
                "principle."
            ),
            "teach": (
                "Panfacial repair is three-dimensional framework reconstruction, not independent "
                "fracture fixation. Le Fort I/II/III describe the level of midface separation from the "
                "skull base and predict which buttresses and pterygoid plates are involved, but real "
                "injuries are frequently mixed or asymmetric -- use the classification to anticipate "
                "structures at risk, not to force-fit the exam."
            ),
            "source_basis": [
                "Resident Manual of Trauma to the Face, Head, and Neck (AAO-HNS), ch 4 -- Le Fort I/II/III fracture-line anatomy and bimanual maxillary mobility testing",
                "Cummings Otolaryngology--Head and Neck Surgery, 7e, ch 20 -- panfacial buttress framework and fixation sequencing principles",
            ],
            "evidence_calibrated": "v40.0-targeted-guideline-review",
        },
        "Structured Facial Trauma Examination": {
            "recognize": (
                "In facial trauma, vision, airway, occlusion, facial width/projection, canthal "
                "position, sensation and CSF signs are the functional readouts that matter before "
                "fracture names -- a structured exam exists precisely so a dramatic-looking laceration "
                "or swelling does not distract from a vision- or airway-threatening finding underneath "
                "it."
            ),
            "localize": (
                "Palpate and inspect in a reproducible sequence from superior to inferior: frontal "
                "bone/brow contour, orbital rims and globe position, zygomatic projection and arch, "
                "nasal/NOE complex (including bimanual mobility testing of the midface), maxillary "
                "buttresses, and mandible/dental occlusion. When an orbital fracture raises clinical concern for entrapment, examine active ductions and arrange safe forced ductions by a trained clinician (after excluding open-globe injury) to demonstrate passive restriction; this is not a routine maneuver for all uncomplicated fractures."
            ),
            "workup": (
                "Thin-cut CT with multiplanar/3-D reconstruction for complex injury; ophthalmologic "
                "and neurologic evaluation are driven by functional findings rather than ordered "
                "reflexively for every facial fracture. A standardized 6-view photographic series "
                "(frontal, both laterals, both obliques, base view) taken before any manipulation or "
                "surgical intervention documents baseline deformity for later comparison and for "
                "surgical planning."
            ),
            "manage": (
                "Stabilize airway, vision and brain injury first, then repair fractures that create "
                "functional or meaningful structural deformity. A wound or fracture that looks urgent "
                "on inspection is not necessarily the priority -- the sequence is always driven by "
                "which structure is actually threatened (airway/vision/brain), not by which injury is "
                "most visually dramatic."
            ),
            "operate": (
                "Reconstruct the facial framework from stable reference points and restore occlusion, "
                "width, height, projection and orbital volume, using the structured exam findings to "
                "decide which buttresses and which functional systems (vision, occlusion, nasolacrimal, "
                "facial nerve) need explicit intraoperative reassessment before closure."
            ),
            "teach": (
                "AO principles emphasize diagnosis, indications and treatment organized by facial "
                "subunit -- never let a dramatic CT finding distract from vision or occlusion, and "
                "never let a dramatic laceration distract from the structured exam underneath it."
            ),
            "source_basis": [
                "Resident Manual of Trauma to the Face, Head, and Neck (AAO-HNS), ch 2 -- general principles of facial trauma evaluation, standardized 6-view photographic documentation, bimanual/forced duction testing",
                "AO Foundation CMF Surgery Reference -- subunit-based diagnosis and treatment framework",
            ],
            "evidence_calibrated": "v40.1-cummings-2026-guideline-reconciliation",
        },
        "Facial Soft-Tissue Lacerations / Burns": {
            "recognize": (
                "Prioritize airway, vision, facial nerve, lacrimal system, parotid (Stensen) duct, "
                "cartilage exposure and tissue viability before cosmetic closure. Any laceration "
                "crossing a line drawn vertically from the lateral canthus to the corner of the mouth, "
                "over the parotid/masseter region, should raise suspicion for buccal branch facial "
                "nerve or parotid duct injury even when the wound looks superficial."
            ),
            "localize": (
                "Localize injury by facial subunit and the deep structure at risk in that subunit: "
                "eyelid/canthus (lacrimal canaliculus), cheek (parotid duct and buccal/zygomatic "
                "facial nerve branches), lip/vermilion (the white roll and wet-dry mucosal junction, "
                "which must be aligned first), ear cartilage (perichondrial blood supply), nose "
                "(cartilage exposure and airway), and brow/forehead (frontal branch of the facial "
                "nerve, which runs superficially here and has no crossing collaterals if transected)."
            ),
            "workup": (
                "Irrigate and explore enough to define depth and contamination without extending "
                "injury. Assess tetanus status, foreign-body contamination, bite-wound risk, "
                "associated fracture, and specialty-threatening injury (cannulate and probe the "
                "parotid duct with a lacrimal probe or angiocatheter when a deep cheek wound is medial "
                "to a line from the tragus to the mid-upper-lip; test facial nerve motor function "
                "before local anesthetic is injected, since anesthetic itself can mimic a nerve "
                "injury)."
            ),
            "manage": (
                "Early, meticulous repair restores alignment and function -- facial wounds tolerate "
                "delayed primary closure beyond traditional short closure windows in selected clean wounds because "
                "of the face's excellent blood supply, but sooner is still better when feasible. "
                "Devitalized tissue is handled conservatively on the face when viability is uncertain, "
                "since even marginal-appearing tissue often survives given the vascularity. Burns "
                "require depth and airway assessment (singed nasal hairs, carbonaceous sputum, facial "
                "burns with a closed-space fire history raise concern for inhalational injury) and a "
                "staged wound-care strategy rather than immediate definitive closure."
            ),
            "operate": (
                "Repair landmarks first -- vermilion border, eyelid margin, brow, alar rim -- since "
                "even a 1-2 mm malalignment at these edges is visually obvious, then perform layered, "
                "tension-free closure. Repair a lacerated parotid duct over a stent, a transected "
                "facial nerve branch lateral to a vertical line at the lateral canthus (branches "
                "medial to this line are not reliably repairable given their small caliber and dense "
                "collateralization, so exploration there is less critical), and a lacrimal "
                "canalicular laceration with ophthalmic/oculoplastic involvement and stenting when indicated -- do not simply close skin over any of these "
                "without addressing the deep structure."
            ),
            "teach": (
                "The scar is often determined by what you align (vermilion, lid margin, brow, alar "
                "rim) and what deep injury you recognize (nerve, duct, canaliculus), not by the brand "
                "of suture. A visibly transected major facial nerve branch lateral to the lateral canthus line "
                "generally warrants exploration and repair when feasible; one medial to it usually is not, because of "
                "small caliber and rich collateralization there."
            ),
            "source_basis": [
                "Cummings Otolaryngology--Head and Neck Surgery, 7e, ch 19 (Facial Trauma: Soft Tissue Lacerations and Burns)",
                "Resident Manual of Trauma to the Face, Head, and Neck (AAO-HNS), ch 9 (Soft Tissue Injuries of the Face, Head, and Neck) -- parotid duct/facial nerve zone of concern, delayed primary closure window",
            ],
            "evidence_calibrated": "v40.0-targeted-guideline-review",
        },
        "Septal Hematoma": {
            "recognize": (
                "Unilateral or bilateral boggy, fluctuant swelling of the nasal septum after nasal trauma -- "
                "including in children, where it can be especially subtle -- should raise concern for "
                "septal hematoma. Because it can look like simple soft-tissue swelling or a deviated "
                "septum on cursory exam, it is one of the more preventable causes of permanent "
                "saddle-nose deformity when missed."
            ),
            "localize": (
                "Blood collects in the subperichondrial space between the septal cartilage and its "
                "perichondrium, cutting off the cartilage's sole blood supply (cartilage itself is "
                "avascular and depends entirely on perichondrial diffusion)."
            ),
            "workup": (
                "Diagnosis is clinical, made by anterior rhinoscopy; palpation with a cotton swab or "
                "gentle instrument helps distinguish a fluctuant hematoma from firm bony/cartilaginous "
                "deviation or simple edema."
            ),
            "manage": (
                "Prompt drainage is required. Cartilage ischemia, necrosis and secondary infection "
                "can evolve over days, so do not use an estimated necrosis or abscess timeline as a "
                "safe observation interval; delay risks septal abscess and rarely intracranial infection. "
                "Cartilage necrosis produces the classic saddle-nose deformity from loss of dorsal/"
                "caudal septal support."
            ),
            "operate": (
                "Incision and drainage under local or general anesthesia (general is often preferred "
                "in children), followed by nasal packing, quilting sutures, or a similar technique to "
                "coapt the mucoperichondrium to the septal cartilage and prevent reaccumulation, with "
                "close follow-up to confirm resolution and rule out reaccumulation or infection."
            ),
            "teach": (
                "Every nasal trauma exam, especially in children, should include a specific, "
                "deliberate look for septal hematoma -- missing it is one of the more preventable "
                "causes of permanent saddle-nose deformity. Drain promptly; an apparently well child may still develop cartilage loss or abscess."
            ),
            "source_basis": [
                "Cummings Otolaryngology--Head and Neck Surgery, 7e, ch 30 -- subperichondrial hematoma, cartilage ischemia, need for prompt drainage (historical timelines are not a safe observation interval)",
                "Resident Manual of Trauma to the Face, Head, and Neck (AAO-HNS), ch 4 -- emergent evacuation and mucoperichondrium coaptation technique",
            ],
            "evidence_calibrated": "v40.1-cummings-2026-guideline-reconciliation",
        },
    },
    "General ENT / Emergencies": {
        "Caustic Ingestion": {
            "recognize": (
                "Caustic ingestion can produce severe esophageal/gastric or laryngeal injury despite "
                "limited or absent oral burns -- up to 30% of patients with significant esophageal "
                "injury show no visible oropharyngeal damage, so a clean-looking mouth does not clear "
                "the esophagus. Drooling, dysphagia, chest/abdominal pain, stridor or respiratory "
                "distress indicate significant risk; acids are more likely than alkalis to cause "
                "chemical epiglottitis and airway obstruction."
            ),
            "localize": (
                "Assess airway/larynx and GI tract separately. Strong acids can cause coagulation "
                "necrosis with eschar formation that limits deeper penetration, so esophageal injury "
                "is comparatively less common than gastric injury (pooling and reflex pylorospasm "
                "increase stomach contact time). Strong alkalis cause liquefaction necrosis that "
                "breaks down cell membranes and penetrates deeply, with injury related to concentration, amount and tissue contact time -- areas of anatomic narrowing (cricopharyngeus, "
                "aortic-arch crossing, left mainstem bronchus, diaphragmatic hiatus) are at highest "
                "risk because of prolonged contact time."
            ),
            "workup": (
                "Stabilize airway/hemodynamics; do not induce emesis or attempt neutralization, both "
                "of which can worsen injury. Do not attempt routine dilution with oral fluids; consult poison control and "
                "the treating team regarding substance-specific immediate management. Barium esophagram is inadequate as a first-line study "
                "(high false-negative rate for mucosal injury) and should not substitute for "
                "specialist-directed evaluation; late presentations require individualized imaging "
                "and procedural decisions because friable tissue can increase endoscopy risk. "
                "Per the 2025 update to pediatric caustic-ingestion management, EGD within 24 hours "
                "is the optimal window for evaluating injury severity and prognosis in symptomatic "
                "patients; in adults, endoscopy decisions depend on exposure and risk even when symptoms are mild, while asymptomatic children warrant individualized "
                "risk assessment, poison-control input and observation rather than routine radionuclide screening."
            ),
            "manage": (
                "NPO/supportive care, analgesia and multidisciplinary GI/surgical/ENT involvement "
                "depend on injury grade (endoscopic staging, e.g., Zargar); perforation or "
                "mediastinitis requires urgent source control. For higher-grade injury (roughly "
                "Zargar 2b and above), specialists may consider early nasogastric tube placement under direct endoscopic "
                "visualization to maintain enteral access; evidence that this prevents stricture "
                "is limited and placement must not be blind. The role of corticosteroids, prophylactic antibiotics and "
                "acid-suppression remains an unresolved evidence question as of the 2025 review -- "
                "these are not settled standard-of-care interventions, and none should be taught as a "
                "required step. Long-term follow-up addresses esophageal stricture (dilation, and in "
                "refractory cases adjuncts such as intralesional steroid or mitomycin C) and "
                "swallowing/nutrition."
            ),
            "operate": (
                "ENT involvement focuses on the threatened laryngeal airway (friable, edematous "
                "tissue changes intubation risk and technique); GI/thoracic/general surgery manage "
                "deeper esophagogastric perforation or necrosis, which can carry substantial mortality "
                "and demands prompt multidisciplinary source control."
            ),
            "teach": (
                "A normal mouth does not clear the esophagus -- up to 30% of significant esophageal "
                "injuries show no visible oral burns. The must-not-miss problems are airway injury "
                "and transmural perforation. Do not teach steroids or prophylactic antibiotics as a "
                "required step; current review states the evidence for both remains unresolved."
            ),
            "source_basis": [
                "Gordon, Barfield & Gold. Early management of acute caustic ingestion in pediatrics. J Pediatr Gastroenterol Nutr. 2025 (PMID 39887462) -- EGD within 24h as optimal window, consider selective NGT under direct visualization for Zargar >=2b, unresolved evidence for steroids/antibiotics/acid-suppression",
                "FISPGHAN expert panel, Global insights on diagnosis, management and prevention of pediatric ingestions, JPGN Reports, 2025 -- individualized endoscopy timing and foreign-body triage",
                "Resident Manual of Trauma to the Face, Head, and Neck (AAO-HNS), ch 10 -- acid/alkali injury mechanism, fluid-dilution guidance, endoscopic timing and indications",
            ],
            "evidence_calibrated": "v40.0-targeted-guideline-review",
        },
        "Esophageal Foreign Body": {
            "recognize": (
                "Suspect an esophageal foreign body with new dysphagia, drooling, chest/throat pain, "
                "refusal to eat (children), or a witnessed/reported ingestion. Urgency is dictated by "
                "object type and location, not by how well the patient otherwise looks: a button "
                "battery, impacted or symptomatic sharp object in the esophagus, or any object causing complete "
                "obstruction (inability to handle secretions), is an emergency regardless of "
                "symptom severity. Esophageal button-battery injury begins within 15-30 minutes and "
                "can progress rapidly to deep necrosis and perforation -- this is one of the few "
                "true minutes-matter emergencies in otolaryngology."
            ),
            "localize": (
                "Most esophageal foreign bodies lodge at one of three physiologic narrowings: the "
                "cricopharyngeus (most common, especially in children), the level of the aortic "
                "arch/left mainstem bronchus crossing, or the lower esophageal sphincter. Lateral and "
                "AP neck/chest radiographs localize radiopaque objects; for a coin, flat orientation "
                "on the AP view (versus flat on lateral for a tracheal foreign body) distinguishes "
                "esophageal from airway location."
            ),
            "workup": (
                "Radiographs for radiopaque objects; proceed to endoscopy based on symptoms and "
                "object type even when imaging is unrevealing (most food and organic material is "
                "radiolucent)."
            ),
            "manage": (
                "Triage by object, location, symptoms and elapsed time. EMERGENT (ideally within 2 hours "
                "of presentation): esophageal button batteries, complete obstruction/inability to handle "
                "secretions, impacted esophageal sharp objects or sharp objects causing symptoms, and "
                "multiple magnets (or a magnet plus another metallic object) when reachable endoscopically. "
                "Urgent specialist and surgical involvement is needed for multiple magnets beyond "
                "endoscopic reach. URGENT (within 24 hours): an asymptomatic nonimpacted esophageal "
                "sharp object and blunt esophageal objects such as coins (some esophageal coins pass "
                "spontaneously; repeat imaging before removal if stable); an isolated confirmed single "
                "magnet follows the blunt-object pathway. Gastric sharp objects generally warrant a low "
                "threshold for retrieval, individualized to shape, symptoms and procedural risk; gastric "
                "batteries require individualized "
                "assessment by age, size, symptoms, co-ingestion, and possible prior esophageal lodgment. Once "
                "past the pylorus, small blunt objects (under roughly 2-2.5 cm) can be observed "
                "clinically with serial stool checks if asymptomatic; if retained after 2-4 weeks, "
                "elective removal is reasonable. Long or wide objects, or objects in patients with altered GI anatomy, require "
                "specialist-guided retrieval timing based on size, symptoms and obstruction risk."
            ),
            "operate": (
                "Indication: any button battery or sharp object in the esophagus, complete "
                "obstruction, or a symptomatic/persistent foreign body. Setup: choose rigid or flexible "
                "esophagoscopy and airway protection according to location, age and aspiration risk; have both a "
                "bronchoscope and esophagoscope assembled, since an object can be dislodged into "
                "either tract during the case. Key steps: assess mucosa for injury before extraction, "
                "remove under direct visualization with a retrieval instrument suited to the object's "
                "shape (protect the esophagus from sharp edges during retrieval; avoid blind advancement), and re-inspect "
                "the esophagus circumferentially after removal for perforation, burn, or pressure "
                "necrosis. Danger structures: the membranous tracheal wall and great vessels "
                "immediately adjacent to the esophagus, especially at a battery-injury site, since a "
                "battery held against the wall can perforate into the airway or aorta. Failure mode: "
                "underestimating how fast battery injury progresses and delaying removal, or missing "
                "a deep mucosal burn that perforates later. Postoperative plan: for battery-related "
                "injury, admit for observation with serial exam/imaging (delayed perforation or "
                "vascular injury can occur days later), and advance diet only once the injury is "
                "judged stable."
            ),
            "teach": (
                "An esophageal button battery is an immediate emergency; clinical stability does not "
                "justify delay. Multiple high-powered magnets or a magnet plus another metal object "
                "are emergent if endoscopically reachable, whereas a confirmed single magnet may be "
                "managed as a blunt foreign body. Impacted or symptomatic esophageal sharp objects "
                "are emergent; stable, nonimpacted asymptomatic esophageal sharp objects require urgent "
                "removal under the 2026 pediatric framework. Timing is object-, location-, symptom- "
                "and delay-specific, not one rule for all foreign bodies."
            ),
            "source_basis": [
                "European Society of Gastrointestinal Endoscopy (ESGE) Clinical Guideline, Removal of foreign bodies in the upper gastrointestinal tract in adults, 2016 (PMID 26862844) -- emergent/urgent/elective triage thresholds by object and location",
                "NASPGHAN Endoscopy Committee, Management of Ingested Foreign Bodies in Children, clinical report, 2015 -- pediatric coin observation and esophageal coin removal",
                "Ledder et al. Foreign body ingestions in children and adolescents: ESPGHAN endoscopy SIG position paper. JPGN 2026;83:539-554. doi:10.1002/jpn3.70485 -- multiple magnets emergent within endoscopic reach, impacted/symptomatic sharp objects emergent, asymptomatic sharp objects urgent; position paper not formally endorsed as ESPGHAN policy",
                "Resident Manual of Trauma to the Face, Head, and Neck (AAO-HNS), ch 10 -- battery injury timeline (1h mucosal injury, 4-6h perforation risk)",
            ],
            "evidence_calibrated": "v40.1-cummings-2026-guideline-reconciliation",
        },
        "Airway Foreign Body": {
            "recognize": (
                "Classic presentation is a witnessed choking episode with sudden coughing, followed "
                "by the choking triad of cough, wheeze and decreased breath sounds, most often "
                "unilateral. A completely normal chest x-ray does not exclude aspiration -- most "
                "aspirated foreign bodies are radiolucent (food, plastic), so a convincing history of "
                "a choking event should drive further evaluation even with a normal film and a "
                "reassuring exam."
            ),
            "localize": (
                "Objects most often lodge in a mainstem bronchus (with variable right-versus-left predominance in children), producing unilateral air trapping (hyperinflation "
                "on expiratory or decubitus films) or, if more proximal, tracheal/laryngeal symptoms "
                "with stridor. Bilateral wheeze or a normal exam does not rule out an airway foreign "
                "body, particularly early or with a partially obstructing object."
            ),
            "workup": (
                "History and exam drive the decision more than imaging: inspiratory/expiratory or "
                "decubitus films (or CT selectively) can support the diagnosis, but a sufficiently "
                "convincing choking history justifies proceeding to bronchoscopy even when imaging "
                "and exam are unremarkable."
            ),
            "manage": (
                "Rigid bronchoscopy remains the diagnostic and therapeutic gold standard for "
                "suspected airway foreign body. An unstable, completely obstructed airway requires "
                "immediate age-appropriate rescue maneuvers before any controlled operating-room "
                "bronchoscopy is possible."
            ),
            "operate": (
                "Indication: witnessed or strongly suspected foreign body aspiration -- history alone "
                "can justify bronchoscopy even with normal imaging and exam. Setup: rigid bronchoscopy "
                "under spontaneous or controlled ventilation general anesthesia, with a range of "
                "retrieval forceps and rigid telescopes available for the suspected object type. Key "
                "steps: systematic airway survey from larynx to segmental bronchi before assuming a "
                "single object or location, gentle grasping and en-bloc removal preserving the airway "
                "outside the scope, and re-inspection after removal for residual fragments or mucosal "
                "injury. Danger structures: the airway itself -- an object pushed distally during "
                "instrumentation, or bleeding/edema obscuring the field, can convert a partial "
                "obstruction into a complete one. Failure mode: a complete, unstable airway "
                "obstruction requires immediate age-appropriate rescue (back blows/chest thrusts in "
                "an infant, abdominal thrusts or direct laryngoscopy with Magill forceps in an older "
                "child/adult) before any controlled OR bronchoscopy is attempted. Postoperative plan: "
                "observe for post-obstructive edema/stridor, especially after a prolonged or "
                "traumatic retrieval, and repeat imaging or bronchoscopy if a fragment is suspected "
                "to remain."
            ),
            "teach": (
                "Do not let a normal x-ray erase a classic aspiration event -- history drives the "
                "decision to scope, not imaging. Mainstem lodging and unilateral air trapping are useful localizing clues; "
                "laterality is less reliable in young children, but their absence does not rule out "
                "aspiration."
            ),
            "source_basis": [
                "Resident Manual of Trauma to the Face, Head, and Neck (AAO-HNS), ch 10 -- age-based bronchoscope selection and equipment preparation, bronchoscopy indications despite negative imaging",
                "Cummings Otolaryngology--Head and Neck Surgery, 7e -- airway foreign body localization and rigid bronchoscopy technique",
            ],
            "evidence_calibrated": "v40.0-targeted-guideline-review",
        },
    },
}


def apply_depth_content_facial_trauma_extra_v400(data_module):
    enriched = []
    for domain, topics in DEPTH_V400.items():
        modules = {m.get("topic"): m for m in data_module.DEEP_MODULES_V6.get(domain, [])}
        missing = [t for t in topics if t not in modules]
        if missing:
            raise RuntimeError(f"v40.0: expected {domain} topics not found: {missing}")
        for topic, fields in topics.items():
            modules[topic].update(fields)
            enriched.append(f"{domain} | {topic}")
    return {"enriched": enriched}
