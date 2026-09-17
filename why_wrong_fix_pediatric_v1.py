"""
why_wrong_fix_pediatric_v1.py

Replaces the generic/duplicate `why_wrong` text for the 38 Pediatric
Otolaryngology items flagged by audit_question_quality.py
(GENERIC_WHY_WRONG). Each wrong choice gets its own specific clinical
reasoning. The correct choice's own slot is "Correct." to match schema.

Usage: same pattern as why_wrong_fix_general_ent_v1.py.

    from why_wrong_fix_pediatric_v1 import apply_why_wrong_fix_pediatric_v1
    WHY_WRONG_FIX_PEDIATRIC_V1 = apply_why_wrong_fix_pediatric_v1(runtime_entry.data)
"""

WHY_WRONG_FIXES = {
    "v140_ped_01": [
        "Correct.",
        "Forcing an exam in a child with suspected epiglottitis can trigger "
        "agitation-induced complete airway obstruction; the exam itself is dangerous "
        "and should be deferred until the airway is secured in a controlled setting.",
        "Sending a child with a potentially unstable airway alone for CT removes them "
        "from immediate airway support and monitoring; imaging is not the priority when "
        "clinical suspicion for epiglottitis is this high.",
        "This presentation (drooling, tripod positioning, stridor, worsening with "
        "agitation) is concerning for a life-threatening airway emergency, not a "
        "condition managed with nebulized medication and outpatient discharge.",
    ],
    "v140_ped_02": [
        "Deep circumferential necrosis carries risk of delayed complications "
        "(perforation, stricture, vascular fistula) that can develop after removal; "
        "immediate discharge without a surveillance plan ignores this ongoing danger.",
        "Correct.",
        "Resuming solid food without reassessing the injured, necrotic esophageal "
        "tissue risks worsening injury or precipitating perforation in a wall already "
        "severely damaged.",
        "Follow-up imaging can be useful for monitoring for stricture formation or "
        "identifying vascular involvement in a high-risk injury; declaring it never "
        "useful ignores a legitimate role in surveillance.",
    ],
    "v140_ped_03": [
        "Persistent unilateral wheeze after a classic choking episode is a red flag "
        "for a retained foreign body even with a normal chest film; discharging "
        "without further evaluation risks missing a retained object.",
        "Unilateral wheeze localized to one side after a choking episode is "
        "inconsistent with asthma, which typically causes bilateral, diffuse wheeze; "
        "treating empirically for months would delay identification and removal of a "
        "retained foreign body.",
        "A hearing test evaluates auditory function and has no relevance to evaluating "
        "a suspected airway foreign body or unilateral wheeze.",
        "Correct.",
    ],
    "v140_ped_04": [
        "Reconstruction success depends on multiple factors beyond stenosis grade "
        "alone, including vocal-fold mobility, the rest of the airway, and "
        "pulmonary/swallowing status; grade alone is an incomplete basis for surgical "
        "planning.",
        "Correct.",
        "Swallowing and neurologic status directly affect a child's ability to "
        "tolerate reconstruction, recover safely, and avoid aspiration; omitting this "
        "assessment would miss factors that influence surgical candidacy and outcome.",
        "CT provides structural information but cannot dynamically assess vocal-fold "
        "mobility the way direct endoscopy can; it complements but does not replace "
        "endoscopic evaluation.",
    ],
    "v140_ped_05": [
        "The entire purpose of laryngotracheal reconstruction is to enlarge, not "
        "narrow, a stenotic airway; this describes the opposite of the graft's "
        "function.",
        "Correct.",
        "The graft is a structural/cartilaginous framework addition; it has no "
        "pharmacologic or surgical relationship to recurrent laryngeal nerve function "
        "and does not paralyze the nerves.",
        "Permanently closing the tracheostomy before confirming the reconstructed "
        "airway is adequate risks leaving the child without a safe airway if the "
        "reconstruction has not yet achieved sufficient patency; staged testing before "
        "permanent closure is standard practice.",
    ],
    "v140_ped_06": [
        "Repeating surgery without first determining whether the new symptoms reflect "
        "transient postoperative dysphagia versus true surgical failure risks an "
        "unnecessary second procedure and does not address the actual, potentially "
        "reversible cause.",
        "Correct.",
        "New coughing with feeds and desaturation are concerning findings that "
        "require evaluation before discharge; sending the infant home without "
        "addressing a possible swallowing or airway problem risks ongoing aspiration.",
        "Introducing solid food in an infant now showing signs of aspiration with "
        "liquids would be premature and could worsen aspiration risk before the "
        "swallowing problem is even evaluated.",
    ],
    "v140_ped_07": [
        "Correct.",
        "A child with severe OSA, obesity, and trisomy 21 has elevated risk for "
        "postoperative respiratory complications, including opioid sensitivity and "
        "airway obstruction; routine unmonitored discharge does not account for this "
        "risk.",
        "These comorbidities specifically increase anesthetic and perioperative risk, "
        "making careful anesthesia planning essential, not unnecessary.",
        "This is factually incorrect -- OSA severity, along with age and "
        "comorbidities, is a primary determinant of postoperative respiratory risk "
        "after adenotonsillectomy and directly informs disposition planning.",
    ],
    "v140_ped_08": [
        "Current guidance specifically distinguishes recurrent AOM with effusion from "
        "recurrent AOM without effusion at the time of assessment; automatically "
        "placing tubes regardless of this distinction does not reflect appropriate, "
        "guideline-based candidacy criteria.",
        "Mastoidectomy is a much more invasive procedure reserved for different "
        "indications (such as cholesteatoma or mastoiditis), not for straightforward "
        "recurrent AOM without effusion.",
        "Correct.",
        "Cochlear implantation addresses severe-to-profound sensorineural hearing "
        "loss, an entirely different condition; it has no relevance to recurrent AOM "
        "or middle-ear effusion decisions.",
    ],
    "v140_ped_09": [
        "A stable child with a phlegmon (not yet a mature, drainable abscess) and no "
        "airway compromise can often be managed with IV antibiotics and close "
        "observation first; proceeding directly to surgery in every case exposes "
        "children to unnecessary surgical risk when medical therapy may suffice.",
        "Correct.",
        "This child has an active deep neck infection requiring antibiotic treatment; "
        "sending home without antibiotics risks progression to a mature abscess or "
        "airway compromise.",
        "Tonsillectomy addresses tonsillar tissue and does not treat a retropharyngeal "
        "phlegmon, an entirely separate deep neck space process.",
    ],
    "v140_ped_10": [
        "Indiscriminate removal of surrounding structures beyond what is needed "
        "causes unnecessary tissue trauma and increases scarring/restenosis risk "
        "without improving the surgical outcome.",
        "The surgical goal is to enlarge, not narrow, the choana; narrowing would "
        "recreate the very obstruction the surgery is meant to correct.",
        "Correct.",
        "Choanal atresia repair has a recognized risk of restenosis; avoiding "
        "postoperative surveillance would miss early recurrent narrowing that could be "
        "addressed before it becomes symptomatic again.",
    ],
    "v142_ped_01": [
        "This infant has red-flag features (poor weight gain, cyanotic spells, "
        "significant collapse) indicating severe disease; reassurance alone regardless "
        "of these findings ignores signs this case has moved beyond the typical "
        "self-limited presentation of laryngomalacia.",
        "Tonsillectomy addresses the tonsils, an entirely different anatomic "
        "structure from the supraglottic collapse causing laryngomalacia; it does not "
        "treat this condition.",
        "Racemic epinephrine provides only temporary symptomatic relief for airway "
        "edema and is not a definitive or appropriate chronic home therapy for severe "
        "laryngomalacia with failure to thrive and hypoxemia.",
        "Correct.",
    ],
    "v142_ped_02": [
        "Age alone does not confirm that the original indication for tracheostomy has "
        "resolved or that the airway is now safe without the tube; decannulation must "
        "be based on actual physiologic readiness, not age.",
        "Suprastomal collapse can cause airway obstruction after decannulation; "
        "ignoring it risks a failed decannulation and respiratory compromise.",
        "Correct.",
        "An acute respiratory infection temporarily increases secretions and airway "
        "reactivity, making this the worst possible time to remove airway support; "
        "decannulation should occur when the child is at their baseline, stable state.",
    ],
    "v142_ped_03": [
        "Biopsy of a vascular subglottic lesion risks significant bleeding and is "
        "generally unnecessary when the clinical picture (cutaneous hemangioma plus "
        "compressible subglottic lesion) is already characteristic; repeated traumatic "
        "biopsy adds risk without benefit.",
        "Radiation therapy is not standard therapy for infantile hemangioma and "
        "carries substantial risk of harm to a developing child's tissues; propranolol "
        "has become the established first-line medical therapy instead.",
        "Total laryngectomy is a radical, function-destroying procedure entirely "
        "disproportionate to a proliferative but typically medically responsive lesion "
        "like infantile subglottic hemangioma.",
        "Correct.",
    ],
    "v143_ped_01": [
        "First branchial cleft anomalies typically relate to the external auditory "
        "canal and parotid region, not a tract coursing between the carotid arteries "
        "toward the tonsillar fossa, which is the classic course of a second branchial "
        "cleft anomaly.",
        "A thyroglossal duct cyst is a midline mass that elevates with tongue "
        "protrusion, following the thyroid descent tract; it does not present as a "
        "lateral neck pit with a tract between the carotid arteries.",
        "A dermoid cyst is typically a midline, non-tract-forming lesion; it does not "
        "follow the described lateral course between the internal and external carotid "
        "arteries toward the tonsillar fossa.",
        "Correct.",
    ],
    "v143_ped_02": [
        "CMV-related hearing loss can be delayed-onset or progressive, meaning a "
        "normal initial newborn screen does not guarantee normal hearing later; "
        "stopping surveillance after a single pass would miss subsequently developing "
        "loss.",
        "Cochlear implantation is reserved for confirmed severe-to-profound hearing "
        "loss that does not benefit from amplification; performing it prophylactically, "
        "before any hearing loss has even been documented, is not appropriate.",
        "Correct.",
        "Tympanostomy tubes treat middle-ear effusion/conductive problems, not the "
        "sensorineural hearing loss caused by congenital CMV; this would not address "
        "the actual mechanism of CMV-related hearing loss.",
    ],
    "v143_ped_03": [
        "Correct.",
        "A chest x-ray may show nonspecific findings like aspiration pneumonia but "
        "cannot directly visualize or diagnose a laryngeal cleft, which requires direct "
        "visualization and palpation of the interarytenoid region.",
        "Tympanometry assesses middle-ear function and has no capability to evaluate "
        "the larynx or diagnose a laryngeal cleft.",
        "Allergy testing evaluates for allergic sensitization and has no role in "
        "diagnosing a structural laryngeal anomaly like a laryngeal cleft.",
    ],
    "v143_ped_04": [
        "Correct.",
        "Sinus CT evaluates the paranasal sinuses and has no capability to assess "
        "swallowing physiology or determine whether aspiration occurs during a "
        "swallow.",
        "A pure-tone audiogram assesses hearing function and has no relevance to "
        "evaluating swallowing safety or aspiration risk.",
        "A sleep study evaluates breathing patterns during sleep and does not assess "
        "swallowing physiology or aspiration during feeding, which is the specific "
        "clinical question here.",
    ],
    "v143_ped_05": [
        "Correct.",
        "RRP is a benign (though recurrent) disease; aggressive excision into normal "
        "laryngeal tissue in an attempt to eradicate HPV causes unnecessary scarring "
        "and voice/airway damage without curing the underlying viral process, which "
        "persists in adjacent mucosa regardless.",
        "Creating permanent raw surfaces on both sides of the anterior commissure "
        "risks anterior glottic web formation from opposing healing surfaces, a "
        "well-recognized complication that conservative technique specifically aims to "
        "avoid.",
        "Tracheostomy is reserved for cases with severe, refractory airway "
        "compromise, not routine first-line management of RRP, which is typically "
        "managed with repeated endoscopic debulking while preserving the native "
        "airway.",
    ],
    "v146_ped_01": [
        "This is a well-feeding infant with no reported nipple pain or growth "
        "concerns; performing frenotomy based solely on the visible anatomic frenulum, "
        "without an actual functional feeding problem, treats an anatomic finding "
        "rather than a real clinical issue.",
        "There is no indication for any surgical intervention at all in this "
        "well-feeding infant, so general anesthesia for frenectomy is an unnecessary "
        "and disproportionate step.",
        "Correct.",
        "Breastfeeding is going well in this scenario (good weight gain, no maternal "
        "pain); stopping it removes a successful feeding method without any indication "
        "to do so.",
    ],
    "v146_ped_02": [
        "Cleft palate primarily affects palatal muscle mechanics and Eustachian tube "
        "function; it does not inherently cause cochlear malformation, which is a "
        "separate, unrelated inner-ear developmental issue.",
        "Correct.",
        "Cholesteatoma is an acquired or congenital keratinizing lesion that is not a "
        "universal feature of cleft palate at birth; this statement is factually "
        "incorrect.",
        "Facial nerve development is a separate embryologic process unrelated to "
        "cleft palate; facial nerve agenesis is not a feature of cleft palate.",
    ],
    "v146_ped_03": [
        "Correct.",
        "Removing the soft palate would eliminate the very structure needed for "
        "velopharyngeal closure and normal speech, which is the opposite of the "
        "functional goal of palatoplasty.",
        "A palatal fistula is a recognized complication to be avoided, not a surgical "
        "goal; intentionally creating one would cause nasal air escape and "
        "feeding/speech problems.",
        "Adequate palatal length is important for velopharyngeal competence; "
        "deliberately shortening the palate would worsen, not improve, speech and "
        "closure function.",
    ],
    "v146_ped_04": [
        "Correct.",
        "Genetic diagnosis can identify syndromic associations, predict progression, "
        "and inform family counseling and recurrence risk, directly influencing "
        "management; this statement is inaccurate.",
        "CT can identify structural inner-ear anomalies but cannot diagnose the many "
        "genetic causes of hearing loss that have no structural correlate on imaging; "
        "it does not identify all causes.",
        "Early identification of etiology and any associated risks is valuable in "
        "infancy for surveillance and counseling; waiting until adolescence delays "
        "potentially important interventions and information.",
    ],
    "v146_ped_05": [
        "Agitating a child with suspected epiglottitis can precipitate sudden, "
        "complete airway obstruction; a detailed exam should be deferred until the "
        "airway is secured in a controlled setting, not pursued at the bedside.",
        "This presentation (toxic appearance, tripod positioning, drooling, muffled "
        "voice) is inconsistent with simple croup, which humidified air treats; "
        "sending this child home would fail to address a potential life-threatening "
        "airway emergency.",
        "Obtaining a throat culture requires oropharyngeal instrumentation, which "
        "risks the same agitation-triggered obstruction that any oral exam does; "
        "airway security must take priority over obtaining a culture.",
        "Correct.",
    ],
    "v146_ped_06": [
        "Correct.",
        "Total parotidectomy is a major operation with facial nerve risk that is "
        "disproportionate to a condition many children outgrow with conservative "
        "management; it is not indicated after just one episode.",
        "Radiation therapy is not indicated for this benign, typically self-limited "
        "inflammatory condition and would expose a child to unnecessary radiation "
        "risk.",
        "While the condition often improves with age, recurrent symptomatic episodes "
        "still warrant supportive management and monitoring; declaring it should be "
        "ignored entirely could miss a case that would benefit from directed "
        "intervention like sialendoscopy.",
    ],
    "v146_ped_07": [
        "Radical neck dissection is an oncologic cancer operation with significant "
        "morbidity; it is entirely disproportionate to a benign lymphatic "
        "malformation, which has effective, less invasive treatment options like "
        "sclerotherapy.",
        "Correct.",
        "While antibiotics may be used if there is a superimposed infection, they do "
        "not treat the underlying macrocystic lymphatic malformation itself, which "
        "requires directed therapy like sclerotherapy or surgery.",
        "Radioactive iodine treats thyroid tissue and has no role in treating a "
        "lymphatic malformation, an entirely different type of tissue and pathology.",
    ],
    "v146_ped_08": [
        "Operating without first assessing inner-ear function and temporal-bone "
        "anatomy risks proceeding with a canal reconstruction in an ear that may not "
        "have adequate inner-ear function to benefit, or anatomy unsuitable for safe "
        "surgery.",
        "Inner-ear (cochlear) function should be specifically assessed rather than "
        "assumed, since atresia can occasionally be associated with inner-ear "
        "anomalies that would change the management approach.",
        "Hearing and speech-development counseling is important early in childhood, "
        "when intervention (such as bone-conduction devices) can support development; "
        "delaying all counseling until adulthood would miss this critical "
        "developmental window.",
        "Correct.",
    ],
    "v146_ped_09": [
        "Correct.",
        "Autologous rib-cartilage reconstruction requires adequate costal cartilage "
        "size, which is not present in infancy; performing this technique too early "
        "would not provide sufficient graft material for a durable result.",
        "Age directly affects the amount of available costal cartilage and chest "
        "development, both central to timing this specific reconstruction technique; "
        "age clearly does matter.",
        "There is no requirement to wait until after age 25; timing is based on "
        "adequate cartilage availability (typically achieved in later childhood) "
        "balanced with psychosocial considerations, not an arbitrary late-adult age "
        "cutoff.",
    ],
    "v146_ped_10": [
        "Correct.",
        "This child's PSG is normal for OSA, meaning there is no obstructive "
        "pathology for adenotonsillectomy to address; performing surgery automatically "
        "without an obstructive diagnosis would not target the actual underlying cause "
        "of daytime sleepiness.",
        "CPAP treats obstructive sleep apnea specifically; since this child's sleep "
        "study does not show OSA, starting CPAP would not address a nonobstructive "
        "cause like circadian rhythm disruption from irregular sleep habits.",
        "Daytime sleepiness affecting a child's functioning warrants evaluation; "
        "ignoring symptoms would leave a treatable behavioral/circadian problem "
        "unaddressed.",
    ],
    "v146_ped_11": [
        "Rapid growth with constitutional symptoms and no response to infectious "
        "treatment are concerning features that should prompt malignancy-focused "
        "evaluation, not continued empiric antibiotics that delay diagnosis.",
        "Correct.",
        "Assuming a benign congenital cyst without appropriate imaging and tissue "
        "evaluation risks missing a malignancy in a mass with concerning growth "
        "pattern and systemic symptoms.",
        "Performing a radical, disfiguring cancer operation before establishing a "
        "tissue diagnosis is inappropriately aggressive and does not allow selection "
        "of the correct treatment based on the actual pathology.",
    ],
    "v146_ped_12": [
        "Waiting for school-age screening delays identification of hearing loss "
        "during a critical period for speech and language development; formal "
        "audiologic evaluation should happen promptly, not be deferred.",
        "Hearing function should be established first with audiologic testing; "
        "imaging is reserved for characterizing structural causes once a hearing loss "
        "is identified, not performed before determining if hearing loss is even "
        "present.",
        "Speech therapy without first assessing hearing status risks missing an "
        "underlying hearing loss that is the actual cause of the speech delay, which "
        "would need to be addressed for therapy to be maximally effective.",
        "Correct.",
    ],
    "v146_ped_13": [
        "Croup is an acute viral illness causing stridor and barky cough, unrelated "
        "to chronic solid-food dysphagia, food impactions, eczema, or feeding "
        "avoidance.",
        "BPPV is a vestibular disorder causing positional vertigo; it has no "
        "relationship to dysphagia, food impaction, or atopic symptoms like eczema.",
        "Correct.",
        "Otitis externa is an external ear canal infection with no connection to "
        "esophageal symptoms like dysphagia and food impaction.",
    ],
    "v146_ped_14": [
        "This child has normal hearing; a hearing aid would not be indicated and "
        "would not address the described hypernasality and nasal air escape, which "
        "stem from velopharyngeal dysfunction, not hearing loss.",
        "Tonsillectomy performed solely for speech concerns, without addressing the "
        "actual suspected velopharyngeal insufficiency, would not correct the "
        "structural/functional closure problem causing hypernasality.",
        "Correct.",
        "There is no infectious process described; antibiotics would not address a "
        "structural/functional velopharyngeal closure problem.",
    ],
    "v146_ped_15": [
        "Otosclerosis causes progressive conductive hearing loss from stapes "
        "fixation, typically in adults; it does not cause episodic vertigo with "
        "headache, photophobia, and motion sensitivity, and hearing here is normal.",
        "Acute mastoiditis is an infectious complication of otitis media presenting "
        "with fever, postauricular swelling, and often otorrhea, not recurrent vertigo "
        "with migrainous features and normal hearing.",
        "Correct.",
        "Isolated conductive hearing loss is a hearing finding, not a balance "
        "disorder, and would not explain recurrent vertigo, headaches, photophobia, or "
        "motion sensitivity.",
    ],
    "v146_ped_16": [
        "Correct.",
        "Voice therapy addresses vocal quality and does not address the acute airway "
        "risk posed by bilateral vocal-fold immobility, which can critically narrow "
        "the glottic airway in a neonate.",
        "Observation regardless of respiratory status ignores the potential for "
        "critical airway narrowing; management must be guided by the infant's actual "
        "work of breathing, with intervention available if the airway is compromised.",
        "Adenoidectomy addresses adenoid tissue in the nasopharynx and has no "
        "relationship to vocal-fold mobility or the laryngeal airway.",
    ],
    "v146_ped_17": [
        "Performing tonsillectomy after only two poorly documented episodes, without "
        "meeting established frequency/severity criteria, exposes the child to "
        "surgical risk without confirmed benefit from an inadequately characterized "
        "history.",
        "Correct.",
        "For children who do meet well-documented, guideline-based criteria for "
        "recurrent tonsillitis, surgery is an appropriate and effective option; "
        "categorically ruling it out ignores this established treatment pathway.",
        "Continuous antibiotics are not standard management for recurrent tonsillitis "
        "and contribute to resistance without addressing the underlying pattern of "
        "recurrent infection or informing the actual surgical decision.",
    ],
    "v146_ped_18": [
        "Simple aspiration does not remove the cyst wall or the embryologic tract, so "
        "the cyst typically recurs; it is not definitive treatment.",
        "The ultrasound confirms a normal thyroid gland is present separately from "
        "this midline cyst; total thyroidectomy would remove functioning normal "
        "thyroid tissue unnecessarily and does not address the actual thyroglossal "
        "tract.",
        "Correct.",
        "This is a benign congenital cyst, not a malignancy; radiation therapy has no "
        "role and would be an inappropriate, harmful intervention.",
    ],
    "v146_ped_19": [
        "The loudness of stridor/wheeze does not correlate reliably with the "
        "physiologic severity of airway collapse or its clinical consequences; it is "
        "not the determining factor for whether surgery is needed.",
        "Age alone does not capture the actual severity of a child's symptoms or "
        "physiologic consequences; management decisions should be based on the "
        "clinical impact of the malacia, not chronologic age in isolation.",
        "Some degree of dynamic airway collapse on bronchoscopy is common and often "
        "physiologically insignificant; the presence of any collapse alone, without "
        "correlating physiologic consequences, does not by itself indicate the need "
        "for surgery.",
        "Correct.",
    ],
    "v146_ped_20": [
        "The pattern and location of the velopharyngeal closure gap directly "
        "determines which surgical technique (such as pharyngeal flap versus "
        "sphincter pharyngoplasty) will actually correct the specific closure defect; "
        "it is highly relevant to treatment planning.",
        "Hearing aid candidacy is determined by audiologic hearing status, an "
        "entirely separate issue unrelated to velopharyngeal closure pattern or "
        "resonance disorders.",
        "Correct.",
        "A central gap with good lateral-wall motion describes velopharyngeal "
        "closure dynamics, not adenoid tissue size; it does not by itself prove or "
        "indicate adenoid hypertrophy.",
    ],
}


def apply_why_wrong_fix_pediatric_v1(data_module):
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
        print(f"why_wrong_fix_pediatric_v1: {len(missing)} ids not found: {missing}")
    return updated
