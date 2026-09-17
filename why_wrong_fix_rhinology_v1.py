"""
why_wrong_fix_rhinology_v1.py

Replaces the generic/duplicate `why_wrong` text for the 64 Rhinology /
Allergy / Skull Base items flagged by audit_question_quality.py
(GENERIC_WHY_WRONG). Each wrong choice gets its own specific clinical
reasoning. The correct choice's own slot is "Correct." to match schema.

Usage: same pattern as why_wrong_fix_general_ent_v1.py.

    from why_wrong_fix_rhinology_v1 import apply_why_wrong_fix_rhinology_v1
    WHY_WRONG_FIX_RHINOLOGY_V1 = apply_why_wrong_fix_rhinology_v1(runtime_entry.data)
"""

WHY_WRONG_FIXES = {
    "v136_rhi_01": [
        "Correct.",
        "The pathology explicitly shows no tissue invasion, which is the defining "
        "distinction from invasive fungal rhinosinusitis; treating this as an invasive, "
        "life-threatening emergency with amphotericin applies the wrong disease "
        "framework to a noninvasive, allergic process.",
        "A viral URI does not produce nasal polyps, allergic mucin with fungal hyphae, "
        "or bony sinus expansion; these findings indicate a distinct, chronic "
        "inflammatory fungal-allergic process, not a self-limited viral illness.",
        "Lymphoma would show malignant lymphoid infiltration on pathology, not allergic "
        "mucin containing noninvasive fungal hyphae; the described pathology is specific "
        "to AFRS, not a hematologic malignancy.",
    ],
    "v136_rhi_02": [
        "Fever is an inconsistent finding in both viral and bacterial rhinosinusitis; "
        "the key discriminator here is symptom persistence beyond 10 days without "
        "improvement, which supports a bacterial process regardless of fever.",
        "Twelve days of symptoms falls well short of the chronic (12-week) duration "
        "required to diagnose CRS; this presentation is acute, not chronic.",
        "There is no mention of immunocompromise, orbital or neurologic red flags, or "
        "tissue necrosis; invasive fungal sinusitis is a distinct, rapidly progressive "
        "disease in at-risk hosts, not the expected diagnosis here.",
        "Correct.",
    ],
    "v136_rhi_03": [
        "Some unilateral masses (such as vascular tumors) can bleed dangerously if "
        "biopsied without first understanding vascularity and anatomic relationships; "
        "blind biopsy skips this essential safety step.",
        "Correct.",
        "Inflammatory polyposis is typically bilateral; a unilateral mass with smooth "
        "bony remodeling is a distinct anatomic pattern that should prompt a "
        "neoplasm-focused workup rather than an assumption of routine bilateral disease.",
        "There is no infectious process described; indefinite antibiotics would not "
        "address a mass lesion and would delay the anatomic workup this presentation "
        "actually requires.",
    ],
    "v136_rhi_04": [
        "Seasonal allergic rhinitis does not explain lifelong pansinusitis combined with "
        "recurrent lower respiratory infections and bronchiectasis; this multisystem "
        "pattern points to a mucociliary clearance disorder, not simple seasonal "
        "allergy.",
        "Elective cosmetic surgery does not address the underlying systemic mucociliary "
        "disease driving this patient's sinus and pulmonary symptoms, and pursuing it "
        "first ignores a potentially serious undiagnosed condition.",
        "The combination of chronic pansinusitis and bronchiectasis specifically "
        "suggests a systemic clearance defect; failing to pursue pulmonary evaluation "
        "would miss the opportunity to identify and coordinate care for CF or PCD.",
        "Correct.",
    ],
    "v136_rhi_05": [
        "Correct.",
        "Eosinophilic polyp disease with asthma and purulent non-polyp disease have "
        "different underlying inflammatory drivers and respond differently to topical "
        "steroids, biologics, and surgery; treating them identically ignores this "
        "biological heterogeneity.",
        "Phenotype directly changes real clinical decisions (biologic candidacy, "
        "surgical extent, medical therapy choice), not just administrative coding.",
        "Nasal polyps are one of the two major CRS phenotypes (CRSwNP), not an "
        "exclusion criterion; a patient with polyps still meets CRS diagnostic "
        "criteria.",
    ],
    "v136_rhi_06": [
        "ABRS is by definition an acute process; symptoms persisting beyond 12 weeks "
        "meet the duration criterion for CRS, not ABRS, regardless of chronicity alone.",
        "Indefinite antibiotics are not a standard component of CRSsNP management and "
        "do not address the underlying chronic mucosal inflammation; overuse "
        "contributes to resistance without proven long-term benefit.",
        "Biologic therapy is generally reserved for severe, recurrent CRSwNP with "
        "type-2 inflammation after other options are exhausted; it is not a mandatory "
        "or first-line step for CRSsNP.",
        "Correct.",
    ],
    "v136_rhi_07": [
        "CRSwNP is primarily a type-2 inflammatory process, not a straightforward "
        "bacterial infection; antibiotics alone do not address the polyp burden or "
        "underlying inflammation and are not definitive therapy.",
        "Correct.",
        "Polyps are commonly biopsied when diagnosis is uncertain and are removed "
        "surgically as a standard part of CRSwNP management to restore ventilation and "
        "improve topical therapy delivery; declining to ever address them surgically "
        "ignores an established, effective treatment.",
        "This patient has real, effective treatment options remaining, including "
        "escalation to surgery and/or biologic therapy; stating no further treatment "
        "exists is inaccurate.",
    ],
    "v136_rhi_08": [
        "Packing without first identifying the exact defect location risks incomplete "
        "or misdirected repair and does not achieve a definitive multilayer closure of "
        "the actual leak site.",
        "Vascularized tissue, such as the nasoseptal flap, is specifically favored for "
        "high-flow leaks because it improves healing and reduces recurrence compared to "
        "nonvascularized grafts alone; avoiding it removes one of the most effective "
        "tools for this exact scenario.",
        "Correct.",
        "Enlarging the skull-base defect increases, rather than decreases, the amount "
        "of tissue needed for closure and the risk of persistent leak or further "
        "intracranial exposure; this is the opposite of sound reconstructive principle.",
    ],
    "v136_rhi_09": [
        "The optic nerve is not anatomically related to the maxillary ostium or "
        "antrostomy technique; this rationale does not explain why the natural ostium "
        "should be incorporated.",
        "Septal perforation results from mucosal injury on both sides of the septum, "
        "unrelated to how the maxillary antrostomy is performed; it is not the reason "
        "for incorporating the natural ostium.",
        "This is anatomically incorrect -- the maxillary sinus drains through its own "
        "natural ostium into the ethmoid infundibulum/middle meatus, not through the "
        "sphenoid ostium, which serves the sphenoid sinus.",
        "Correct.",
    ],
    "v136_rhi_10": [
        "The inferior turbinate lies well below the ethmoid complex and is not a "
        "superior boundary at risk during ethmoidectomy; it is unrelated to intracranial "
        "injury risk.",
        "Correct.",
        "The hard palate forms the floor of the nasal cavity, far inferior to the "
        "ethmoid roof, and has no relationship to the superior boundary at risk during "
        "ethmoid dissection.",
        "The anterior nasal spine is an anterior midline structure at the base of the "
        "nasal septum, unrelated to the superior ethmoid roof or intracranial risk.",
    ],
    "v136_rhi_11": [
        "Performing sinus surgery without objective evidence of sinonasal inflammation "
        "exposes the patient to surgical risk without a clear anatomic target, and "
        "would not be expected to address a nonrhinogenic pain generator like migraine.",
        "Correct.",
        "There is no evidence of bacterial infection here (normal endoscopy and CT); "
        "antibiotics would not address a nonrhinogenic headache disorder.",
        "Normal endoscopy and normal CT between episodes are inconsistent with fungal "
        "sinusitis, which typically produces visible mucosal or radiographic "
        "abnormality; this diagnosis does not fit the presentation.",
    ],
    "v136_rhi_12": [
        "Frontal recess anatomy is in fact highly variable between patients due to "
        "differing agger nasi and frontal cell configurations; this is precisely why "
        "individualized preoperative review matters, not because anatomy is fixed.",
        "Reviewing CT only after a complication has already occurred defeats the "
        "purpose of preoperative planning, which is meant to prevent complications by "
        "anticipating patient-specific anatomy in advance.",
        "Correct.",
        "This is anatomically incorrect -- the frontal sinus drains through the frontal "
        "recess into the middle meatus, not through the nasolacrimal duct, which drains "
        "tears from the eye into the inferior meatus.",
    ],
    "v136_rhi_13": [
        "The Draf classification concerns the extent of frontal recess/sinus opening, "
        "not inferior turbinate resection, which is an unrelated procedure.",
        "Increasingly extensive Draf procedures progressively enlarge, not narrow, the "
        "frontal drainage pathway, which is the opposite of what defines escalating "
        "Draf types.",
        "The Draf classification is a surgical/anatomic staging system based on the "
        "extent of bony/mucosal removal to enlarge frontal drainage, not a system "
        "defined by different antibiotic regimens.",
        "Correct.",
    ],
    "v136_rhi_14": [
        "Because there is no mucosal invasion, this is a noninvasive fungal ball, not "
        "an invasive infection; systemic antifungal therapy is generally unnecessary "
        "once the fungal debris is surgically removed and drainage is restored.",
        "Persistent obstruction from dense fungal debris will not resolve without "
        "removing the mass and restoring ventilation; observation leaves the causative "
        "material in place.",
        "AFRS is a distinct, allergic/eosinophilic-mucin-driven, typically bilateral or "
        "polypoid disease; this presentation (unilateral dense fungal ball without "
        "allergic mucin) fits fungal ball, a different entity managed surgically, not "
        "medically like AFRS.",
        "Correct.",
    ],
    "v136_rhi_15": [
        "Recurrent pneumonias and unusually frequent bacterial infections beyond the "
        "sinuses point toward a systemic host-defense problem rather than simply "
        "inadequate local surgical technique; assuming a surgical explanation alone "
        "misses the broader clinical picture.",
        "Vaccination history, including response to vaccines, can be informative when "
        "evaluating for humoral immunodeficiency; deliberately avoiding this history "
        "would remove useful diagnostic information.",
        "Correct.",
        "Topical decongestants provide only short-term symptomatic relief and do not "
        "address either the chronic sinus inflammation or an underlying immune defect "
        "driving recurrent infections.",
    ],
    "v136_rhi_16": [
        "Complete turbinate removal risks long-term complications such as crusting, "
        "dryness, and empty-nose syndrome by eliminating functional mucosa; "
        "volume-reducing techniques that preserve mucosa are generally preferred.",
        "Fracturing the nasal bones addresses external nasal framework/valve issues, "
        "not turbinate tissue volume, and would not be the appropriate technique for "
        "isolated turbinate hypertrophy.",
        "Correct.",
        "Frontal sinusotomy addresses frontal sinus drainage, an entirely different "
        "anatomic problem unrelated to inferior turbinate size or nasal airflow through "
        "the turbinate region.",
    ],
    "v136_rhi_17": [
        "The inferior turbinate head is located anteriorly and inferiorly in the nasal "
        "cavity, far from the sphenoethmoidal recess, which lies posterosuperiorly near "
        "the superior turbinate.",
        "Correct.",
        "The nasolacrimal valve (Hasner's valve) is located in the inferior meatus, "
        "related to tear drainage, and is unrelated to locating the sphenoethmoidal "
        "recess posteriorly.",
        "The anterior nasal spine is an anterior, inferior midline structure at the "
        "nasal base, unrelated to the posterosuperior sphenoethmoidal recess.",
    ],
    "v136_rhi_18": [
        "No single objective measure, including CT-based airflow assessment, should "
        "solely determine surgical candidacy; clinical judgment integrating symptoms, "
        "exam, and testing together is required.",
        "Patient-reported obstruction is a primary driver of the clinical concern and "
        "treatment decision-making; disregarding it would remove essential "
        "information, especially since objective findings and symptoms do not always "
        "correlate perfectly.",
        "A normal Cottle maneuver does not rule out obstruction from other causes (such "
        "as internal valve collapse not captured by the Cottle test); it is one "
        "adjunctive test, not a definitive exclusionary one.",
        "Correct.",
    ],
    "v136_rhi_19": [
        "Correct.",
        "Performing sinus surgery without treating the causative dental infection "
        "leaves the source of the problem in place, which typically leads to "
        "recurrence of the sinusitis.",
        "The unilateral pattern and clear anatomic relationship to a periapical dental "
        "lesion point to a dental source, not allergic rhinitis, which is typically "
        "bilateral and unrelated to dental pathology.",
        "An active dental source of infection adjacent to the sinus will not resolve on "
        "its own and risks continued or worsening sinonasal disease if left untreated.",
    ],
    "v136_rhi_20": [
        "There is no infectious/bacterial process here to treat; postviral olfactory "
        "loss reflects neuroepithelial injury, not an ongoing bacterial infection, so "
        "antibiotics have no therapeutic role.",
        "There is no obstructing turbinate pathology described; the problem is "
        "neurosensory (postviral), not a structural airflow obstruction that turbinate "
        "surgery would address.",
        "Some degree of spontaneous or training-assisted recovery does occur in "
        "postviral olfactory loss; telling the patient recovery is impossible is "
        "inaccurate and denies them an evidence-supported intervention.",
        "Correct.",
    ],
    "v136_rhi_21": [
        "Total turbinectomy is not indicated for pediatric CRS driven by adenoid "
        "hypertrophy and carries significant risk in a growing child's nasal airway; it "
        "does not address the adenoid reservoir described here.",
        "Draf III is an advanced adult frontal sinus procedure reserved for refractory "
        "frontal disease; it is a highly invasive, disproportionate first step for "
        "typical pediatric CRS.",
        "Correct.",
        "Surgery, specifically adenoidectomy, is a well-established, commonly used "
        "option for medically refractory pediatric CRS when adenoid disease is "
        "prominent; stating surgery is never appropriate contradicts standard "
        "practice.",
    ],
    "v136_rhi_22": [
        "A single positive CT finding does not by itself distinguish RARS from CRS; the "
        "defining feature is the temporal pattern of complete symptom resolution "
        "between discrete acute episodes versus persistent chronic symptoms.",
        "Facial pressure can occur in both RARS and CRS and is not the distinguishing "
        "feature; the key difference is the presence of symptom-free intervals.",
        "Antibiotic use occurs in both acute and chronic sinusitis management and does "
        "not itself define or distinguish RARS from CRS.",
        "Correct.",
    ],
    "v136_rhi_23": [
        "Correct.",
        "Repeating the same operation without understanding why the first surgery "
        "failed risks repeating the same technical or anatomic oversight and ignores "
        "patient-specific factors that may require a different approach.",
        "Scar tissue is only one of several possible causes of persistent disease after "
        "ESS (others include residual partitions, lateralized middle turbinate, "
        "inflammatory endotype, or odontogenic source); assuming it is always the sole "
        "cause could lead to an incomplete revision plan.",
        "Stopping topical therapy removes an important component of ongoing medical "
        "management and does not investigate or address the reason the first surgery "
        "failed.",
    ],
    "v136_rhi_24": [
        "Correct.",
        "There is no infectious process described here; antibiotics would not correct "
        "a fixed structural deformity causing mechanical obstruction.",
        "Frontal sinusotomy addresses frontal sinus drainage, an entirely different "
        "anatomic region unrelated to correcting a caudal septal deviation.",
        "Long-term oral decongestants do not correct fixed structural deviation and "
        "carry systemic side-effect risks with chronic use; they would not resolve a "
        "mechanical, decongestant-unresponsive obstruction.",
    ],
    "v136_rhi_25": [
        "Bone destruction, facial numbness, and recurrent epistaxis are concerning "
        "oncologic red flags, not typical CRS findings; treating empirically for months "
        "as CRS would delay diagnosis and treatment of a likely malignancy.",
        "Correct.",
        "Debulking without first establishing a tissue diagnosis risks inappropriate or "
        "incomplete oncologic treatment planning and does not allow selection of the "
        "correct multimodal therapy based on histology.",
        "Sinonasal malignancies are histologically diverse (squamous cell carcinoma, "
        "adenocarcinoma, esthesioneuroblastoma, and others), and treatment approach "
        "varies significantly based on tumor type and extent.",
    ],
    "v136_rhi_26": [
        "The inferior turbinate and lacrimal sac are located anteriorly in the nasal "
        "cavity, far from the sphenoid sinus, and are not at risk during sphenoidotomy "
        "overexpansion.",
        "The anterior nasal spine and hard palate are anterior/inferior midline "
        "structures unrelated to the posterior sphenoid sinus and its adjacent "
        "neurovascular structures.",
        "The parotid duct and facial nerve are extranasal structures in the "
        "cheek/face, entirely unrelated to the sphenoid sinus and its surrounding "
        "anatomy.",
        "Correct.",
    ],
    "v136_rhi_27": [
        "Reconstructing a saddle-nose deformity during active destructive disease (from "
        "a systemic condition) risks graft/flap failure because the underlying disease "
        "process has not been controlled; treating the cause should precede "
        "reconstruction.",
        "Chronic crusting, epistaxis, septal perforation, and progressive saddle-nose "
        "deformity are far beyond the typical findings of simple allergic rhinitis, "
        "which does not cause tissue destruction or septal perforation.",
        "Turbinectomy does not address the underlying destructive process causing "
        "perforation and saddle-nose deformity and would not investigate or treat a "
        "systemic cause.",
        "Correct.",
    ],
    "v141_rhi_01": [
        "Correct.",
        "This is an allergic, not infectious, process; long-term antibiotics do not "
        "address IgE-mediated inflammation and would not improve allergic symptoms.",
        "Surgery is not first-line therapy for typical allergic rhinitis, which is "
        "managed medically; ESS is reserved for structural or refractory sinus disease.",
        "Indefinite systemic steroids carry substantial long-term risks (osteoporosis, "
        "adrenal suppression, metabolic effects) and are not appropriate first-line, "
        "chronic therapy when effective, safer topical options exist.",
    ],
    "v141_rhi_02": [
        "Immunotherapy should be targeted to allergens confirmed by testing to be "
        "clinically relevant; proceeding without any testing risks treating an "
        "irrelevant or unconfirmed sensitization.",
        "Uncontrolled severe asthma is a recognized risk factor for serious systemic "
        "reactions to immunotherapy; starting SCIT in this setting without first "
        "stabilizing asthma control increases safety risk.",
        "Correct.",
        "There is no infectious indication here; antibiotic prophylaxis has no role in "
        "preparing a patient for allergen immunotherapy.",
    ],
    "v141_rhi_03": [
        "Bacterial sinusitis does not explain the combination of asthma, "
        "NSAID-triggered bronchospasm, and recurrent polyps after prior surgery; this "
        "triad is specific to a distinct inflammatory syndrome.",
        "Correct.",
        "JNA is a vascular tumor typically seen in adolescent males with epistaxis and "
        "a posterior nasal mass; it does not involve asthma or NSAID-triggered "
        "bronchospasm and does not fit this presentation.",
        "Septal hematoma is a traumatic collection of blood under the septal mucosa; it "
        "has no relationship to asthma, polyps, or NSAID sensitivity.",
    ],
    "v141_rhi_04": [
        "Inverted papilloma classically recurs when the site of mucosal attachment "
        "(and sometimes the underlying bone) is not completely addressed; simple "
        "polypectomy removes visible tissue but leaves the attachment site behind.",
        "Inverted papilloma carries a recognized risk of synchronous or metachronous "
        "squamous cell carcinoma; stating malignant transformation never occurs is "
        "factually incorrect and could lead to inadequate surveillance.",
        "Correct.",
        "Inverted papilloma is a benign (though locally aggressive) epithelial tumor; "
        "chemotherapy is not standard treatment, and surgical removal of the tumor and "
        "its attachment is the primary therapeutic approach.",
    ],
    "v141_rhi_05": [
        "A subdural empyema with neurologic deficit is a life-threatening intracranial "
        "infection requiring urgent surgical drainage and IV (not oral, outpatient) "
        "antibiotics; home oral therapy is grossly inadequate for this severity.",
        "Nasal steroids treat mucosal inflammation and have no role in treating an "
        "established intracranial infection; this would leave a life-threatening "
        "process completely unaddressed.",
        "Waiting for seizures to develop means waiting for further neurologic "
        "deterioration in an already critically ill patient; this delays necessary "
        "urgent intervention and risks permanent injury or death.",
        "Correct.",
    ],
    "v141_rhi_06": [
        "Preoperative angiography (often with embolization) is a standard, safe, and "
        "useful step in JNA management to characterize and reduce vascularity before "
        "resection -- it is something that should be done, not avoided.",
        "Correct.",
        "Cross-sectional imaging (CT/MRI) is essential and appropriate for "
        "characterizing JNA extent and planning treatment; avoiding it would be "
        "counterproductive to safe, informed management.",
        "Planning the surgical approach based on tumor extent is a necessary, "
        "appropriate step in JNA management, not something to avoid.",
    ],
    "v142_rhi_01": [
        "Packing without identifying the precise defect location risks an incomplete "
        "or misdirected repair that fails to seal the actual site of CSF leakage.",
        "Correct.",
        "A free mucosal graft alone, without vascularized tissue, is generally less "
        "durable for high-flow leaks specifically, which benefit from the improved "
        "healing and lower failure rate that vascularized tissue provides.",
        "Leaving a high-flow skull-base CSF leak open for secondary healing risks "
        "ongoing leak, meningitis, and pneumocephalus; active, deliberate multilayer "
        "closure is required.",
    ],
    "v142_rhi_02": [
        "Draf I is the most limited frontal recess procedure, involving only anterior "
        "ethmoidectomy without significant frontal ostium enlargement; it would be "
        "inadequate for this severely scarred, refractory case.",
        "Correct.",
        "Maxillary antrostomy addresses the maxillary sinus ostium, an entirely "
        "different sinus and anatomic region unrelated to the frontal drainage pathway "
        "described here.",
        "Sphenoidotomy opens the sphenoid sinus, a posterior structure unrelated to the "
        "frontal sinus and its recess; it does not create the described bilateral "
        "frontal drainage pathway.",
    ],
    "v142_rhi_04": [
        "In a patient with distorted landmarks from prior surgery and recurrent "
        "disease, assuming normal anatomy remains where textbook landmarks would "
        "typically be is precisely the assumption that leads to disorientation and "
        "injury during revision surgery.",
        "Correct.",
        "Image-guided navigation is a helpful adjunct but is not a substitute for "
        "genuine anatomic understanding derived from careful CT review; relying on it "
        "alone increases risk if registration is imperfect or misinterpreted.",
        "Beginning dissection blindly in the posterior ethmoid, one of the highest-risk "
        "areas near the skull base and optic nerve, without first establishing a "
        "landmark-based plan significantly increases the risk of serious injury.",
    ],
    "v143_rhi_01": [
        "Eleven days of symptoms is well short of the 12-week duration required to "
        "diagnose chronic rhinosinusitis; this is an acute presentation, not a chronic "
        "one.",
        "There are no red flags (orbital or neurologic) described here that would "
        "mandate urgent surgery; uncomplicated ABRS is managed medically.",
        "Uncomplicated ABRS is a clinical diagnosis based on symptom pattern and "
        "duration; routine imaging is not required and is reserved for cases with red "
        "flags or diagnostic uncertainty.",
        "Correct.",
    ],
    "v143_rhi_02": [
        "Correct.",
        "The pathology explicitly shows no tissue invasion, which distinguishes this "
        "from invasive fungal rhinosinusitis; emergent orbital exenteration is a "
        "drastic, disfiguring intervention entirely disproportionate to this "
        "noninvasive, allergic disease process.",
        "This is a fungal-allergic inflammatory process, not a bacterial infection; "
        "antibiotics alone would not address the allergic mucin, polyps, or underlying "
        "type-2 inflammation driving this disease.",
        "The described eosinophilic mucin, very high IgE, and expansile radiographic "
        "changes represent an active, tissue-damaging inflammatory disease requiring "
        "surgical clearance and anti-inflammatory therapy, not incidental colonization "
        "that can be ignored.",
    ],
    "v143_rhi_03": [
        "Correct.",
        "Creating a separate accessory opening while leaving the natural ostium "
        "isolated is exactly the technical error that causes mucus recirculation, "
        "since mucus can cycle out one opening and back in through the other.",
        "Routine removal of the nasolacrimal duct is unnecessary for maxillary "
        "antrostomy and risks causing epiphora (tearing); it does not relate to "
        "preventing mucus recirculation.",
        "The uncinate process must be identified and addressed to properly locate and "
        "incorporate the natural ostium; avoiding its identification would make this "
        "harder, not easier.",
    ],
    "v143_rhi_04": [
        "Correct.",
        "The hard palate and mandible are inferior oral cavity structures far removed "
        "from the ethmoid complex and are not at risk during ethmoidectomy.",
        "The carotid bifurcation and jugular foramen are deep neck/skull-base "
        "structures unrelated to the ethmoid sinuses, which are approached through the "
        "nasal cavity, not the neck.",
        "The external auditory canal and sigmoid sinus are temporal bone structures "
        "unrelated to the ethmoid complex, a paranasal sinus structure entirely "
        "separate from the ear and lateral skull base.",
    ],
    "v143_rhi_05": [
        "Performing sinus surgery alone without addressing the causative periapical "
        "dental infection leaves the underlying source in place and risks persistent "
        "or recurrent disease.",
        "Topical steroid alone does not treat an active dental infection with "
        "extension into the sinus and ethmoid; it addresses mucosal inflammation, not "
        "the causative odontogenic source.",
        "This presentation is explicitly unilateral with a clear dental source, the "
        "opposite pattern from typical bilateral allergic rhinitis; assuming allergy "
        "would misdirect the workup.",
        "Correct.",
    ],
    "v144_rh_01": [
        "A positive skin-prick wheal demonstrates sensitization, not necessarily that "
        "the allergen is causing the patient's current symptoms; clinical correlation "
        "with exposure and symptom timing is required to establish causation.",
        "Correct.",
        "Total IgE is a nonspecific marker of overall atopic burden and does not "
        "identify which specific allergen (if any) is responsible for symptoms; "
        "specific-IgE or skin testing to individual allergens is needed for that.",
        "CT sinus opacity reflects mucosal thickening or fluid, which can result from "
        "many causes (infection, structural obstruction, inflammation) and is not "
        "diagnostic of allergic rhinitis specifically.",
    ],
    "v144_rh_02": [
        "Correct.",
        "A vascular-appearing unilateral mass could bleed significantly if biopsied "
        "without first understanding its vascularity and extent; immediate blind "
        "biopsy skips this important safety step.",
        "Allergic polyposis is typically bilateral; a unilateral vascular-appearing "
        "mass is a distinct presentation requiring neoplasm-focused evaluation.",
        "Unilateral symptoms, especially with recurrent epistaxis and a visible mass, "
        "are a red flag pattern that specifically should not be ignored, as they may "
        "indicate a vascular tumor or other significant pathology.",
    ],
    "v144_rh_03": [
        "The combination of bronchiectasis, chronic wet cough, and lifelong refractory "
        "pansinusitis with unusually thick secretions suggests a systemic mucociliary "
        "clearance disorder, not an isolated, routine local sinus problem.",
        "Saline irrigation helps clear thick secretions and is generally a helpful, "
        "low-risk adjunct in mucociliary clearance disorders; avoiding it would remove "
        "a useful supportive therapy.",
        "This presentation has objective, well-described physical findings "
        "(bronchiectasis, thick secretions, refractory sinus disease) consistent with "
        "an organic mucociliary disorder; attributing it to psychogenic causes ignores "
        "clear physical evidence of disease.",
        "Correct.",
    ],
    "v144_rh_04": [
        "Phenotype clearly changes prognosis, comorbidity evaluation, and treatment "
        "choice between medical, biologic, and surgical options; it very much matters, "
        "contrary to this statement.",
        "CT score is only one component of overall CRS evaluation; it does not capture "
        "polyp status, comorbid asthma/AERD, or inflammatory endotype, all of which "
        "meaningfully affect management decisions.",
        "Chronic antibiotics are not a standard, mandatory component of CRS management "
        "for either phenotype described here, particularly the polyp/asthma "
        "phenotype, which is driven primarily by type-2 inflammation.",
        "Correct.",
    ],
    "v144_rh_05": [
        "Biologic therapy is generally reserved for severe, refractory CRSwNP after "
        "other options have failed; it is not standard first-line treatment for "
        "CRSsNP, which typically starts with optimized medical therapy.",
        "Correct.",
        "Surgical decisions should integrate the full clinical picture (symptom "
        "burden, endoscopy, contributing factors), not a mildly abnormal CT finding in "
        "isolation, which alone does not justify surgery.",
        "This patient has real remaining options, including reassessing contributing "
        "factors and considering ESS; stating no further treatment is possible is "
        "inaccurate.",
    ],
    "v144_rh_06": [
        "Performing sinus surgery in the absence of any objective sinonasal "
        "abnormality (normal endoscopy and CT) exposes the patient to surgical risk "
        "without an anatomic target and would not address a nonrhinogenic headache "
        "disorder like migraine.",
        "There is no evidence of infection here (normal endoscopy and CT); antibiotics "
        "would not address migrainous features like photophobia, nausea, and episodic "
        "throbbing pain.",
        "Frontal sinus obliteration is a major, destructive procedure reserved for "
        "severe, refractory frontal sinus disease; it is entirely inappropriate when "
        "there is no objective sinonasal disease present at all.",
        "Correct.",
    ],
    "v144_rh_07": [
        "Frontal recess anatomy varies considerably between patients due to differing "
        "frontal cell configurations, which is precisely why individualized review is "
        "needed, not because anatomy is uniform.",
        "CT is specifically valuable because it clearly demonstrates the frontal "
        "cells, skull-base slope, and surrounding structures relevant to safe "
        "dissection; this statement is the opposite of CT's actual utility here.",
        "Correct.",
        "While septal anatomy can matter for access, the primary determinants of safe "
        "frontal recess dissection are the frontal cells, skull-base slope, and "
        "orbital relationships, not the septum alone.",
    ],
    "v144_rh_08": [
        "There is no mucosal invasion described; this noninvasive fungal ball does not "
        "require systemic antifungal therapy, which is reserved for invasive fungal "
        "disease.",
        "A symptomatic fungal ball causing foul drainage and obstruction requires "
        "removal to resolve symptoms and restore drainage; declining any treatment "
        "leaves the causative debris and symptoms in place.",
        "This is a benign, noninvasive fungal colonization, not a malignancy; "
        "chemoradiation has no role and would be an inappropriate, harmful "
        "intervention.",
        "Correct.",
    ],
    "v144_rh_09": [
        "Correct.",
        "Repeating surgery without investigating the broader pattern of recurrent "
        "pneumonias and unusual infection frequency risks missing an underlying immune "
        "defect that repeat local surgery alone will not fix.",
        "Recurrent pneumonias and unusually frequent bacterial infections beyond the "
        "sinuses are not typical of allergy alone; this pattern specifically suggests "
        "a systemic immune problem that allergy would not explain.",
        "Stopping topical therapy removes a helpful component of local disease "
        "management without addressing the systemic immune evaluation this "
        "presentation actually requires.",
    ],
    "v144_rh_10": [
        "Correct.",
        "Aggressive complete resection removes functional mucosa needed for "
        "humidification and sensation, risking crusting, dryness, and empty-nose-type "
        "symptoms; volume-preserving techniques are generally preferred.",
        "The middle turbinate serves different functional and surgical-landmark "
        "purposes; removing it does not address inferior turbinate hypertrophy, which "
        "is the actual cause of this patient's obstruction.",
        "Ablating the septum does not address turbinate tissue volume, which is the "
        "actual source of obstruction described here, and could create its own "
        "separate structural problems.",
    ],
    "v144_rh_11": [
        "The recognized phenomenon of local allergic rhinitis (nasal-mucosal-limited "
        "IgE reactivity without systemic sensitization) means a negative systemic test "
        "does not rule out an allergic mechanism entirely; declaring allergy "
        "impossible ignores this established entity.",
        "Invasive fungal disease presents with tissue necrosis, cranial neuropathy, or "
        "other severe, destructive features, not classic seasonal itching, sneezing, "
        "and watery rhinorrhea; this does not fit the presentation at all.",
        "Correct.",
        "CSF leak presents with unilateral clear rhinorrhea (often positional) without "
        "the itching and sneezing pattern described; it is an unrelated structural "
        "problem, not an allergic phenomenon.",
    ],
    "v144_rh_12": [
        "The slow, progressive, years-long time course and smoothly marginated "
        "expansile appearance are inconsistent with an acute, rapidly destructive "
        "invasive fungal process; this is a chronic obstructive process, not an acute "
        "fungal emergency.",
        "Correct.",
        "A symptomatic mucocele causing proptosis and pressure will not resolve "
        "without draining the obstructed mucus and re-establishing ventilation; "
        "indefinite observation risks progressive orbital or other complications.",
        "A mucocele is a benign, obstruction-related mucus collection, not a "
        "malignancy; radiation therapy has no role and would be inappropriate for this "
        "benign process.",
    ],
    "v144_rh_13": [
        "Correct.",
        "The inferior meatus contains the nasolacrimal duct opening and is unrelated "
        "to the maxillary ostium, which is located superiorly in the middle meatus "
        "region.",
        "The nasal vestibule is the anterior-most portion of the nasal cavity near the "
        "nostril, well anterior to the middle meatus where the maxillary ostium is "
        "located.",
        "The posterior choana is the posterior opening of the nasal cavity into the "
        "nasopharynx, unrelated to the middle meatus/uncinate region where the "
        "maxillary ostium is found.",
    ],
    "v144_rh_14": [
        "Increasing decongestant frequency would worsen, not improve, the rebound "
        "congestion cycle that defines rhinitis medicamentosa; this perpetuates the "
        "very problem causing the symptoms.",
        "There is no fungal infection here; this is a rebound phenomenon from chronic "
        "topical decongestant overuse, and antifungal therapy has no relevant "
        "mechanism of action for this condition.",
        "There is no structural or skull-base pathology described; this is a "
        "reversible, medication-induced mucosal problem that does not require "
        "surgical intervention of any kind.",
        "Correct.",
    ],
    "v144_rh_15": [
        "Correct.",
        "Objective nasal function testing complements but does not replace the "
        "clinical history and physical examination, which remain central to "
        "understanding the multidimensional nature of nasal obstruction.",
        "Nasal airflow/resistance or geometry testing evaluates mechanical/physiologic "
        "nasal function, not immunologic sensitization; it has no capability to prove "
        "or diagnose allergy.",
        "These tests assess nasal airflow and structure, not tumor characteristics; "
        "they have no role in cancer staging.",
    ],
    "v144_rh_16": [
        "There is no obstructing lesion or sinus abnormality described (normal "
        "endoscopy); sinus surgery would have no anatomic target to correct and would "
        "not be expected to restore postviral olfactory function.",
        "This is a postviral neurosensory injury, not a bacterial infection; long-term "
        "antibiotics have no mechanism to address this type of olfactory loss.",
        "Some patients do experience spontaneous or training-assisted recovery from "
        "postviral olfactory loss; declaring recovery impossible is inaccurate and "
        "denies the patient an evidence-supported, low-risk intervention.",
        "Correct.",
    ],
    "v144_rh_17": [
        "Total rhinectomy is an extreme, disfiguring procedure typically reserved for "
        "extensive malignancy; it is entirely disproportionate to medically refractory "
        "pediatric CRS with adenoid hypertrophy.",
        "Frontal sinus obliteration is a major adult procedure for severe refractory "
        "frontal disease; it is not an appropriate or typical early step for pediatric "
        "CRS, especially before simpler interventions have been tried.",
        "Surgery, specifically adenoidectomy, is an established and commonly used "
        "option in appropriately selected children with medically refractory CRS; "
        "stating surgery is never appropriate in children contradicts standard "
        "pediatric practice.",
        "Correct.",
    ],
    "v144_rh_18": [
        "CRS requires persistent symptoms and objective inflammation over a chronic "
        "(12-week) duration; this patient has discrete episodes with complete "
        "resolution between them and normal endoscopy between attacks, which does not "
        "fit CRS criteria.",
        "Invasive fungal sinusitis is a distinct, typically rapidly progressive "
        "disease in immunocompromised patients with tissue necrosis; it does not fit a "
        "pattern of recurring, self-resolving acute bacterial-type episodes.",
        "Correct.",
        "CSF rhinorrhea presents with unilateral clear watery drainage, often "
        "positional, not recurrent acute bacterial-type sinusitis episodes; it is an "
        "unrelated entity.",
    ],
    "v144_rh_19": [
        "Removing excessive cartilage risks destabilizing the L-strut support, "
        "potentially causing saddle-nose deformity or loss of tip support; septoplasty "
        "should remove only the deviated, obstructing cartilage while preserving "
        "structural support.",
        "Complete turbinate ablation is a separate procedure addressing a different "
        "structure (turbinate volume, not septal position) and is not the operative "
        "goal of septoplasty, which targets the septal deviation itself.",
        "Correct.",
        "Opening the frontal sinus addresses an entirely different anatomic region "
        "unrelated to correcting a caudal septal deviation causing nasal obstruction.",
    ],
    "v144_rh_20": [
        "Bone erosion, facial numbness, and epistaxis with an irregular mass are "
        "oncologic red flags, not typical CRS findings; empiric treatment for months "
        "as CRS would delay diagnosis and appropriate treatment of a likely "
        "malignancy.",
        "Correct.",
        "Debulking without a tissue diagnosis first risks inappropriate treatment "
        "planning and does not allow selection of the correct combination of surgery, "
        "radiation, or systemic therapy based on actual histology.",
        "Sinonasal malignancies are histologically and behaviorally diverse; treatment "
        "(endoscopic vs. open surgery, radiation, systemic therapy) is tailored to "
        "specific tumor type and extent, not applied uniformly.",
    ],
    "v144_rh_21": [
        "Correct.",
        "Sphenoid anatomy, including carotid and optic nerve relationships and "
        "pneumatization patterns, varies significantly between patients, which is "
        "precisely why individualized preoperative review is essential.",
        "A lateral plain film provides far less detail than CT and cannot adequately "
        "demonstrate the carotid canal, optic nerve relationships, or septal "
        "insertions critical to safe sphenoidotomy.",
        "Entering through the most lateral wall risks directly injuring the carotid "
        "artery or optic nerve, which can protrude into or dehisce along the lateral "
        "sphenoid wall; this is the opposite of a safe surgical approach.",
    ],
    "v144_rh_22": [
        "Septal perforation, pulmonary symptoms, and renal abnormalities are far "
        "beyond the scope of uncomplicated allergic rhinitis, which does not cause "
        "tissue destruction or involve other organ systems.",
        "Performing cosmetic surgery before identifying and treating an active "
        "systemic disease process risks poor surgical outcomes and, more importantly, "
        "delays diagnosis and treatment of a potentially serious systemic condition.",
        "Topical decongestants provide only symptomatic relief and do not address an "
        "underlying systemic vasculitic or inflammatory process affecting the nose, "
        "lungs, and kidneys.",
        "Correct.",
    ],
    "v144_rh_23": [
        "Unilateral disease specifically differs from typical bilateral inflammatory "
        "polyposis and should prompt consideration of a broader, more concerning "
        "differential; it does have distinct clinical significance.",
        "Allergic rhinitis and typical inflammatory polyposis are usually bilateral "
        "processes; unilateral disease is actually a red flag against a simple "
        "allergic explanation, not proof of it.",
        "Correct.",
        "Tissue diagnosis (biopsy) is often necessary and appropriate for unilateral "
        "disease to distinguish between the broad differential (inverted papilloma, "
        "malignancy, fungal disease, etc.); declining to ever biopsy would prevent "
        "reaching an accurate diagnosis.",
    ],
}


def apply_why_wrong_fix_rhinology_v1(data_module):
    """Overwrite why_wrong for the fixed ids. Returns count actually updated."""
    byid = {q.get("id"): q for q in data_module.CLINICAL_CHALLENGES_V119 if q.get("id")}
    updated = 0
    missing = []
    for qid, new_why_wrong in WHY_WRONG_FIXES.items():
        q = byid.get(qid)
        if q is None:
            missing.append(qid)
            continue
        if len(new_why_wrong) != len(q.get("choices") or []):
            raise ValueError(
                f"{qid}: fix has {len(new_why_wrong)} entries but question has "
                f"{len(q.get('choices') or [])} choices"
            )
        q["why_wrong"] = new_why_wrong
        updated += 1
    if missing:
        print(f"why_wrong_fix_rhinology_v1: {len(missing)} ids not found: {missing}")
    return updated
