"""Replace generic v139 vignette distractor explanations without overwriting edits."""

GENERIC_MARKER_V139 = 'Compare this option with the triage, anatomy, or management principle in the explanation.'

WHY_WRONG_FIXES_V139 = {
    'v139_ped_01': [
        'A visible frenulum is common anatomic variation seen in many normally feeding infants; performing frenotomy on every one of them exposes infants with no functional problem to an unnecessary procedure and bleeding/infection risk.',
        'Tracheostomy addresses airway obstruction requiring a surgical airway, which has no relationship to an asymptomatic lingual frenulum with normal latch and weight gain.',
        'Adenoidectomy removes nasopharyngeal lymphoid tissue for nasal obstruction or middle-ear disease; it does nothing for a tongue-tie and is not indicated here.',
        'Correct.',
    ],
    'v139_ped_02': [
        'Bilateral choanal atresia is a fixed anatomic obstruction (bony or membranous) that will not open on its own; neonates are obligate nasal breathers, so waiting risks progressive hypoxia and cardiorespiratory arrest.',
        'Correct.',
        'Tonsillectomy removes oropharyngeal lymphoid tissue and has no effect on posterior nasal choanal obstruction.',
        'Topical nasal steroid can shrink mucosal edema but cannot open a bony or thick membranous choanal plate, so it will not relieve the obstruction acutely.',
    ],
    'v139_ped_03': [
        'The cochlea and sensorineural pathway are typically normal in cleft palate; the hearing loss produced by chronic effusion is conductive, not sensorineural, so cochlear malformation is not the mechanism.',
        'Correct.',
        'Ossicles usually form normally in isolated cleft palate; the conductive loss comes from fluid behind an intact but poorly ventilated tympanic membrane, not from arrested ossicular development.',
        'Cleft palate is strongly and consistently associated with chronic otitis media with effusion because of abnormal tensor veli palatini insertion and eustachian tube dysfunction, so this option contradicts well-established pathophysiology.',
    ],
    'v139_ped_04': [
        'Deliberately shortening the palate reduces the length available for velopharyngeal contact against the pharyngeal wall, worsening rather than improving speech outcomes.',
        'The uvula is not the functional determinant of velopharyngeal closure; removing it does not address the malpositioned levator muscle sling that causes VPI.',
        'Intravelar veloplasty specifically reorients the abnormally oriented, sagittally inserted levator veli palatini into a transverse sling; avoiding this repair leaves the muscle malpositioned and perpetuates poor speech outcomes.',
        'Correct.',
    ],
    'v139_ped_05': [
        'Congenital SNHL affects the critical window for auditory and language development; deferring any evaluation or habilitation until school age causes irreversible delay.',
        'Noise-induced loss requires significant environmental exposure and does not explain congenital bilateral SNHL identified via newborn screening in an infant.',
        'Correct.',
        'Tympanostomy tubes treat conductive pathology from middle-ear effusion; they do not address sensorineural hearing loss, so tubes alone would leave the underlying deficit and its etiology unaddressed.',
    ],
    'v139_ped_06': [
        'Juvenile recurrent parotitis is typically self-limited and often improves by puberty; proceeding to parotidectomy after a single episode exposes the child to facial nerve risk that is disproportionate to a benign, often self-resolving condition.',
        'Radioactive iodine ablation treats thyroid tissue and has no role in a salivary gland disorder.',
        'Correct.',
        'Neck dissection addresses nodal metastatic disease and is entirely inappropriate for benign recurrent parotid swelling in a child.',
    ],
    'v139_ped_07': [
        'Paralyzing the vocal folds would worsen airway obstruction and voice outcome; LTR is intended to enlarge the airway lumen while preserving or improving vocal fold mobility, not eliminate it.',
        'Correct.',
        'Otitis media is a middle-ear disease unrelated to the laryngotracheal framework being reconstructed in LTR.',
        'Tongue-base reduction addresses obstructive sleep apnea from lingual tonsil or base-of-tongue hypertrophy, not fixed subglottic cartilage stenosis.',
    ],
    'v139_ped_08': [
        'A lymphatic malformation is not a bacterial abscess; incising it like one risks a chronic draining fistula and does not treat the underlying malformed lymphatic channels or address recurrence.',
        'Radical neck dissection is an oncologic operation for malignant nodal disease and is never indicated for a benign congenital vascular malformation.',
        'Correct.',
        'Antibiotics can help during superimposed infection or inflammatory flares but indefinite antibiotic use does not shrink or resolve the malformation itself.',
    ],
    'v139_ped_09': [
        'Correct.',
        'Delaying audiologic evaluation until the child is old enough for auricular reconstruction ignores the separate, time-sensitive window for hearing access and language development, which should not wait for a cosmetic-timeline decision.',
        'The contralateral ear cannot be assumed normal; unilateral microtia/atresia can occur with occult contralateral pathology or as part of a broader craniofacial/syndromic process, so it must be formally tested.',
        "Audiology is essential here because atresia produces a conductive loss and the contralateral ear's status is unknown; skipping testing risks missing bilateral hearing impairment during a critical developmental period.",
    ],
    'v139_ped_10': [
        'Modern techniques (including porous polyethylene frameworks) allow ear reconstruction earlier in childhood, so autologous rib grafting is a timing choice driven by donor tissue, not a statement that reconstruction is impossible before adulthood.',
        'Hearing rehabilitation (for atresia or contralateral ear) proceeds on its own timeline independent of when auricular framework surgery is performed; it is not a prerequisite for costal cartilage harvest.',
        'Facial nerve maturation is not a limiting factor for costal cartilage donor site readiness; the facial nerve is relevant to atresia repair, not to rib cartilage volume for the auricular framework.',
        'Correct.',
    ],
    'v139_ped_11': [
        'Correct.',
        'Adenotonsillectomy treats adenotonsillar hypertrophy causing obstructive breathing; it is not indicated when the presentation is behavioral bedtime resistance and irregular sleep schedules without witnessed obstruction.',
        'Hypoglossal nerve stimulation is reserved for select patients (e.g., with Down syndrome) with confirmed obstructive sleep apnea refractory to other measures, not for a nonobstructive behavioral/circadian sleep complaint.',
        'Tracheostomy is an airway-bypass procedure for severe obstructive disease and has no role in a child whose problem is behavioral insomnia rather than airway obstruction.',
    ],
    'v139_ped_12': [
        'Assuming reflux without evaluation risks missing a structural or neurologic cause of aspiration (e.g., laryngeal cleft, dysphagia, airway anomaly) that requires a different treatment approach and continues to cause pneumonia if untreated.',
        'Correct.',
        'Tonsillectomy addresses lymphoid tissue causing airway obstruction, not the swallowing mechanism responsible for aspiration with feeds.',
        'Given documented desaturation with feeds and recurrent pneumonia, withholding any feeding modification while awaiting evaluation leaves the infant at ongoing aspiration risk.',
    ],
    'v139_ped_13': [
        'Assuming all pediatric neck masses are reactive ignores red-flag features here (firm, fixed, rapidly enlarging) that are classic for malignancy such as lymphoma or rhabdomyosarcoma.',
        'Excising a mass without prior imaging risks incomplete margins, tumor seeding, or injury to unrecognized vascular/neural structures, and forgoes information needed to plan an oncologic operation appropriately.',
        'A year of observation for a rapidly enlarging, firm, fixed mass unacceptably delays diagnosis and staging of a potential malignancy, worsening prognosis.',
        'Correct.',
    ],
    'v139_ped_14': [
        'BPPV is a peripheral vestibular disorder causing positional vertigo and has no relationship to solid-food dysphagia or impaction.',
        'Correct.',
        'Croup is a viral laryngotracheobronchitis presenting with barky cough and stridor, not with dysphagia or food impaction.',
        'Otitis externa is an external ear canal infection and is unrelated to esophageal dysphagia.',
    ],
    'v139_ped_15': [
        'The vignette specifies normal hearing, so assuming hearing loss contradicts the given findings and would misdirect the workup.',
        'Tonsils are not the cause of hypernasal resonance; in fact large tonsils can mask an underlying velopharyngeal insufficiency, and removing them without addressing resonance can unmask or worsen hypernasality.',
        'Correct.',
        'Ignoring speech-language assessment removes the key tool for distinguishing an articulation/language disorder from a structural resonance problem, which is essential before deciding on any intervention.',
    ],
    'v139_ped_16': [
        'Otosclerosis causes a slowly progressive conductive hearing loss, typically in adults, and does not produce episodic vertigo with headache and photophobia in a child with normal interictal hearing.',
        'Cholesteatoma typically presents with conductive hearing loss, chronic otorrhea, or a retraction pocket on exam, not with recurrent migraine-type episodic vertigo and normal hearing between attacks.',
        'Correct.',
        'Acute mastoiditis presents with fever, postauricular erythema, swelling and tenderness from an active infection, not a chronic recurrent pattern of episodic vertigo with headache.',
    ],
    'v139_ped_17': [
        'Three documented episodes in one year falls below standard thresholds (such as 7 episodes in one year, 5/year for two years, or 3/year for three years) generally used to justify tonsillectomy for recurrent infection, so immediate surgery is not indicated.',
        'Correct.',
        'Chronic IV antibiotic prophylaxis is not standard practice for recurrent tonsillitis; it carries unnecessary line-related and resistance risks compared with oral treatment of individual documented episodes.',
        'Objective documentation of episode frequency and severity (fever, exudate, tender adenopathy, positive culture) is required to determine whether surgical thresholds are met; deciding without it risks operating on inadequate grounds.',
    ],
    'v139_ped_18': [
        'Failure to thrive, apnea and severe retractions are indications for surgical intervention; continuing pure observation regardless of severity risks ongoing growth failure and hypoxic events.',
        'Adenoidectomy addresses nasopharyngeal obstruction, not the supraglottic prolapse of arytenoid/aryepiglottic tissue that causes laryngomalacia, so it will not relieve the obstruction.',
        'Cochlear implantation treats severe-to-profound sensorineural hearing loss and has no bearing on a supraglottic airway obstruction problem.',
        'Correct.',
    ],
    'v139_ped_19': [
        'Cyst excision alone leaves the central hyoid bone and tract remnant behind, which is associated with recurrence rates as high as 50% because the tract can extend embryologically through or around the hyoid to the foramen cecum.',
        'Total thyroidectomy removes the normal functioning thyroid gland unnecessarily; the Sistrunk procedure only removes the central hyoid segment and tract, and imaging should first confirm normal thyroid tissue exists elsewhere rather than sacrificing the gland.',
        'Correct.',
        'Neck dissection addresses regional lymph node metastasis and is not indicated for a benign thyroglossal duct cyst.',
    ],
    'v139_ped_20': [
        'Tonsillectomy treats oropharyngeal lymphoid obstruction and has no effect on dynamic tracheal wall collapse.',
        'Correct.',
        'Attributing the wheeze and cyanotic spells to asthma alone overlooks the bronchoscopically confirmed structural finding of dynamic tracheal collapse, which reactive airway therapy will not fix.',
        'Rigid stenting every infant is excessive; most tracheomalacia is mild and improves with growth, and stents carry risks of granulation tissue, erosion and migration that make them a last resort for severe, refractory disease.',
    ],
    'v139_ped_21': [
        'This statement is factually incorrect; persistent OME commonly causes measurable conductive hearing loss, which is exactly what has been documented in this child.',
        'Correct.',
        'Mastoidectomy is reserved for chronic mastoid or cholesteatoma disease and is a disproportionate, unindicated procedure for uncomplicated bilateral OME.',
        'Cochlear implantation is for severe-to-profound sensorineural hearing loss, not the conductive loss produced by middle-ear effusion.',
    ],
    'v139_ped_22': [
        'Choosing a specific pharyngeal-flap procedure without first defining the closure pattern (coronal, sagittal, circular) and gap size risks selecting the wrong operation, under- or over-correcting the defect, or creating airway obstruction.',
        'Adenoid tissue can contribute to velopharyngeal closure, especially after cleft repair; removing it automatically can worsen rather than improve hypernasality and is not a default step in VPI workup.',
        'Articulation testing is essential to separate compensatory misarticulations (a speech-therapy target) from true structural velopharyngeal insufficiency (a surgical target); ignoring it risks operating on a problem that is actually articulatory.',
        'Correct.',
    ],
    'v139_gen_01': [
        'A normal chest x-ray is well known to miss radiolucent foreign bodies and can show a normal exam even after aspiration; discharging based on imaging alone ignores the compelling history and asymmetric exam findings.',
        'Correct.',
        'Oral antibiotics do not remove a mechanical obstruction; a retained foreign body will continue to risk erosion, granulation tissue, atelectasis and infection regardless of antibiotic therapy.',
        'Tonsillectomy addresses oropharyngeal lymphoid tissue and has no role in retrieving a tracheobronchial foreign body.',
    ],
    'v139_gen_02': [
        'Correct.',
        'Broad-spectrum antibiotics provide no benefit against a viral illness and expose the patient to unnecessary adverse effects and selection for resistant organisms.',
        'IV vancomycin is reserved for serious, often resistant bacterial infections; using it for an uncomplicated viral URI is a major stewardship violation with no benefit.',
        'There is no fungal disease process implicated by a routine viral URI, so antifungal therapy is irrelevant.',
    ],
    'v139_gen_05': [
        'Isolated facial nerve (CN VII) dysfunction would produce facial weakness alone and does not explain the palate, shoulder and tongue findings, which localize to CN IX/X, XI, and XII respectively.',
        'Cochlear pathology produces hearing loss or tinnitus, not motor deficits of the palate, shoulder, or tongue.',
        'Correct.',
        'Optic chiasm lesions cause visual field defects (e.g., bitemporal hemianopia), which is unrelated to this lower cranial nerve motor pattern.',
    ],
    'v139_gen_06': [
        'Continuing antibiotics alone is inadequate for a large, organized, rim-enhancing collection with trismus, sepsis, and worsening airway symptoms; medical therapy alone does not drain a mature abscess causing airway compromise.',
        'Blind needle aspiration through the carotid space risks catastrophic injury to the carotid artery or jugular vein; drainage of a parapharyngeal abscess should be performed via a defined surgical approach with knowledge of the compartment anatomy.',
        'Discharge is unsafe in a septic patient with an unresolved abscess and worsening airway symptoms.',
        'Correct.',
    ],
    'v139_gen_07': [
        'Meniere disease is an inner-ear disorder causing episodic vertigo, hearing loss, and tinnitus and has no relationship to electrolyte shifts after refeeding.',
        'BPPV is a peripheral vestibular disorder from otoconial displacement, unrelated to metabolic/nutritional status.',
        'Correct.',
        'Bell palsy is an acute peripheral facial nerve paralysis, unrelated to the metabolic and electrolyte derangements of refeeding.',
    ],
    'v139_gen_08': [
        'Correct.',
        'A noncontrast skull x-ray provides essentially no soft-tissue resolution and cannot delineate a deep-space abscess, airway displacement, or vascular complications.',
        'DEXA measures bone mineral density and has no application to acute infectious or vascular pathology of the neck.',
        'PET without CT provides functional/metabolic information useful mainly in oncologic staging over time; it is far too slow and nonspecific to evaluate a potentially life-threatening acute infection with vascular risk.',
    ],
    'v139_gen_11': [
        'Randomization, which balances known and unknown confounders between groups, was not performed in this retrospective study; its absence is precisely why confounding by indication is a problem here, not a protective feature that is present.',
        'Blinding relates to outcome/assessment bias, not to the underlying imbalance in baseline health and age between treated and untreated groups described in this scenario.',
        'Correct.',
        'External validity concerns how well results generalize to other populations; even a study with excellent generalizability can still suffer from internal confounding, which is the specific flaw described here.',
    ],
    'v139_gen_12': [
        'Correct.',
        'Age alone does not predict surgical tolerance; ignoring documented severe frailty, falls, cognitive impairment, and ADL dependence would lead to underestimating real perioperative risk.',
        'Denying treatment based solely on chronologic age is ageist and ignores the fact that some elderly patients with good functional reserve tolerate surgery well; the decision should be individualized, not age-based alone.',
        "Caregiver and social support directly affect a frail patient's ability to recover safely from treatment and should be actively assessed, not ignored, when planning care.",
    ],
    'v139_gen_13': [
        'Correct.',
        'Leaving infected, exposed hardware in place indefinitely risks ongoing sepsis, progressive soft-tissue breakdown, and eventual reconstructive failure rather than resolution.',
        "Steroids are immunosuppressive and would impair the body's ability to control the underlying infection, worsening rather than helping the situation.",
        'Vascularized tissue transfer is often essential in irradiated, infected fields because native tissue has impaired perfusion and healing capacity; dismissing its role ignores standard reconstructive salvage principles.',
    ],
    'v139_gen_15': [
        'Correct.',
        'Routine outpatient sinusitis management dangerously delays recognition of acute invasive fungal rhinosinusitis, which can progress to orbital and intracranial invasion within hours in a neutropenic host.',
        "Steroids are immunosuppressive and would further impair an already neutropenic patient's ability to fight the fungal invasion, accelerating disease progression.",
        'Waiting for neutrophil recovery before evaluating black necrotic mucosa and ophthalmoplegia risks death from a rapidly progressive infection that requires immediate diagnosis and debridement, not delay.',
    ],
    'v139_gen_16': [
        'Using 100% oxygen with flammable drapes maximizes both the oxidizer and fuel components of the fire triad, directly increasing rather than reducing airway-fire risk.',
        'Ignoring laser eye protection exposes the patient and OR staff to serious corneal or retinal injury from stray or reflected laser energy, a core and preventable safety failure.',
        'Correct.',
        'Activating the laser before a team timeout skips verification of settings, protective measures, and readiness, removing a critical safeguard against preventable injury.',
    ],
    'v139_gen_17': [
        'Correct.',
        'BPPV is a peripheral vestibular disorder from otoconial debris and has no connection to recurrent oral ulcers, genital ulcers, or uveitis.',
        'Otosclerosis causes progressive conductive hearing loss from otic capsule bone remodeling and is unrelated to this mucocutaneous-ocular symptom triad.',
        'Meniere disease is an inner-ear disorder causing vertigo, hearing loss, and tinnitus, unrelated to oral/genital ulceration and uveitis.',
    ],
    'v139_gen_18': [
        'Escalating opioids without examining the patient risks missing a surgical complication (such as hematoma, infection, or ischemia) driving the pain, while also worsening the somnolence toward respiratory depression.',
        "Renal and hepatic function directly affect opioid metabolite clearance; ignoring them risks drug accumulation and toxicity, which may already be contributing to this patient's somnolence.",
        'Assuming all postoperative pain is expected dismisses the red flag of pain escalating despite increasing opioids alongside new somnolence, which should instead prompt reassessment for a complication.',
        'Correct.',
    ],
    'v139_gen_19': [
        'Correct.',
        'Isolated allergic rhinitis is a mucosal, IgE-mediated process that does not cause septal perforation, subglottic stenosis, or renal dysfunction, so it cannot account for this multisystem destructive presentation.',
        'BPPV is a peripheral vestibular disorder and is unrelated to sinonasal destruction, airway stenosis, or renal disease.',
        'Otosclerosis causes conductive hearing loss from otic capsule remodeling and has no relationship to this necrotizing multisystem process.',
    ],
    'v139_gen_20': [
        'Correct.',
        'This is the opposite of the actual pathophysiology; radiation causes progressive endarteritis obliterans and fibrosis, producing chronically reduced, not increased, tissue vascularity over time.',
        'Perfusion and oxygenation are fundamental drivers of collagen synthesis and cellular repair, so scar biology is directly and heavily dependent on blood supply.',
        'Healing rate varies substantially based on tissue vascularity, radiation history, nutritional status, infection, and mechanical stability, so this uniform claim is false.',
    ],
}


def apply_why_wrong_fix_vignettes_v139_v1(data_module):
    """Overwrite only untouched generic v139 explanations; return count updated."""
    byid = {q.get('id'): q for q in data_module.CLINICAL_CHALLENGES_V119 if q.get('id')}
    updated = 0
    skipped_already_edited = []
    missing = []
    for qid, new_why_wrong in WHY_WRONG_FIXES_V139.items():
        q = byid.get(qid)
        if q is None:
            missing.append(qid)
            continue
        current = q.get('why_wrong') or []
        is_untouched_generic = bool(current) and all(
            str(w).strip() in (GENERIC_MARKER_V139, 'Correct.') for w in current
        ) and any(str(w).strip() == GENERIC_MARKER_V139 for w in current)
        if is_untouched_generic:
            if len(new_why_wrong) != len(q.get('choices') or []):
                raise ValueError(f"{qid}: fix has {len(new_why_wrong)} entries but question has {len(q.get('choices') or [])} choices")
            q['why_wrong'] = new_why_wrong
            updated += 1
        elif current == new_why_wrong:
            pass
        else:
            skipped_already_edited.append(qid)
    if missing:
        print(f'why_wrong_fix_vignettes_v139_v1: {len(missing)} ids not found: {missing}')
    if skipped_already_edited:
        print(f'why_wrong_fix_vignettes_v139_v1: {len(skipped_already_edited)} ids already edited, skipped: {skipped_already_edited}')
    return updated
