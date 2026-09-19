"""Replace generic v137 vignette distractor explanations with clinical reasoning.

Only untouched factory placeholders are replaced; edited questions are preserved.
"""

GENERIC_MARKER_V137 = 'Compare the option with the management principle in the explanation and the specific clinical context.'

WHY_WRONG_FIXES_V137 = {
    'v137_tps_01': [
        'Immediate total parotidectomy is an unnecessarily radical response to an infectious process; surgery in an acutely inflamed, infected gland carries high morbidity and is reserved for recurrent/chronic disease or a mass unresponsive to conservative care, not a first presentation of acute suppurative sialadenitis.',
        'Correct.',
        'Radioactive iodine treats thyroid tissue via the sodium-iodide symporter and has no role in an acute bacterial infection of the parotid gland.',
        'Steroids alone would blunt the immune response to an active bacterial infection without addressing the underlying stasis or providing antimicrobial coverage, risking progression to abscess or sepsis.',
    ],
    'v137_tps_02': [
        'Proceeding straight to lobectomy without tissue diagnosis and multidisciplinary staging risks operating on anaplastic carcinoma without a plan for its aggressive local invasion, and a rapidly enlarging, hoarseness-associated mass needs urgent core/FNA diagnosis before any operative commitment.',
        'Anaplastic thyroid carcinoma has a median survival measured in months; a 6-month observation period in a patient with tracheal compression and rapid growth would allow airway obstruction and metastatic spread to progress unchecked.',
        'Correct.',
        'Anaplastic thyroid carcinoma is typically undifferentiated and does not concentrate iodine, so RAI is not an effective treatment and should not be relied upon as curative therapy.',
    ],
    'v137_tps_03': [
        'Correct.',
        'Berry-picking (excising only palpable/visible nodes without a formal compartment dissection) leaves behind at-risk perithyroidal and paratracheal lymphatic tissue, increasing the risk of persistent or recurrent disease and making any future reoperation more hazardous due to scarring.',
        'Central (level VI) nodal metastases are common in papillary thyroid carcinoma and are clinically significant when biopsy-proven; ignoring biopsy-proven disease is not oncologically sound management.',
        'Radical neck dissection removes the sternocleidomastoid, internal jugular vein and spinal accessory nerve along with lateral neck nodal levels; it is not indicated for isolated central (level VI) nodal disease and is excessive for this presentation.',
    ],
    'v137_tps_04': [
        'Mandatory total thyroidectomy for every papillary carcinoma is outdated; current ATA-based risk stratification permits lobectomy alone for low-risk, small (<4 cm), intrathyroidal, node-negative tumors without aggressive histology.',
        'Correct.',
        'Total laryngectomy removes the larynx and is used for laryngeal malignancy invading cartilage/extralaryngeal structures; it has no role in managing a small, low-risk intrathyroidal papillary thyroid carcinoma.',
        'Surgery is an appropriate and often preferred option for a patient with biopsy-proven differentiated thyroid cancer who desires operative management; withholding all surgical options is not supported when the patient meets criteria and prefers it.',
    ],
    'v137_tps_05': [
        'A biochemically confirmed diagnosis of primary hyperparathyroidism meeting surgical criteria should not be abandoned solely because imaging failed to localize the adenoma; localization studies aid operative planning but do not determine surgical candidacy.',
        'Removing the thyroid gland does not address parathyroid pathology and would expose the patient to unnecessary thyroidectomy-specific risks (RLN injury, hypothyroidism) without treating the hyperparathyroidism.',
        'Excising the first normal-appearing gland encountered risks removing healthy parathyroid tissue while leaving the actual hyperfunctioning gland in place, worsening rather than curing the disease.',
        'Correct.',
    ],
    'v137_tps_06': [
        'Bethesda III (AUS/FLUS) carries only an intermediate malignancy risk (roughly 10-30%); reflexively performing total thyroidectomy on every such nodule would subject many patients with ultimately benign disease to unnecessary surgery and lifelong levothyroxine.',
        'Correct.',
        'RAI is a treatment for confirmed differentiated thyroid cancer (or hyperthyroidism), not a diagnostic tool; giving RAI without a tissue diagnosis in an indeterminate nodule is inappropriate and potentially harmful.',
        'Cytology results directly inform malignancy risk and management pathway; disregarding a Bethesda III result would abandon the evidence base used to counsel the patient on surveillance versus surgery.',
    ],
    'v137_tps_07': [
        'RAI treats differentiated (follicular-cell derived) thyroid cancer, not medullary thyroid carcinoma, which arises from parafollicular C-cells and does not take up iodine; it is not part of the preoperative workup here.',
        'RET pathogenic variants are autosomal dominant, so first-degree relatives have a 50% risk of carrying the same variant; failing to address family implications misses an opportunity for cascade genetic testing and early intervention in relatives.',
        'Parathyroidectomy is only indicated when hyperparathyroidism/hypercalcemia is actually present; MEN2A (not MEN2B) is associated with primary hyperparathyroidism, and prophylactic parathyroidectomy in every RET carrier regardless of subtype and biochemistry is not standard practice.',
        'Correct.',
    ],
    'v137_tps_08': [
        'Piecemeal shelling-out of a suspected parathyroid carcinoma risks tumor spillage and capsular violation, seeding the operative bed and dramatically increasing the risk of local recurrence.',
        'Correct.',
        'Routine needle biopsy through a mass suspicious for parathyroid carcinoma risks tumor seeding along the needle tract and is specifically avoided when malignancy is suspected on clinical grounds (severe hypercalcemia, invasive mass, vocal-fold paralysis).',
        'Vocal-fold paralysis indicates recurrent laryngeal nerve invasion, a hallmark of locally invasive parathyroid carcinoma rather than indolent disease; observation would allow a potentially resectable malignancy to progress and metastasize.',
    ],
    'v137_tps_09': [
        'Pleomorphic adenoma is a benign mixed tumor, not a malignancy, though it carries a small risk of malignant transformation (carcinoma ex pleomorphic adenoma) if left untreated for a prolonged period or if recurrent.',
        'The facial nerve does not need to be sacrificed for pleomorphic adenoma resection; standard parotidectomy technique dissects and preserves the facial nerve while removing the tumor with a surrounding cuff of normal parotid tissue.',
        'Untreated pleomorphic adenoma can continue to enlarge and carries a cumulative risk of malignant transformation over time, so observation without any treatment plan is not appropriate once a diagnosis is established.',
        'Correct.',
    ],
    'v137_tps_10': [
        'Repeated aspiration alone treats the cystic collection transiently but does not address the sublingual gland mucus leak driving fluid reaccumulation, leading to high recurrence rates.',
        "Removing the submandibular gland does not address the sublingual gland, which is the actual source of a ranula's mucus extravasation; submandibular excision alone is not the standard treatment and would leave the causative gland in place.",
        'Correct.',
        'Parotidectomy addresses the parotid gland, which is anatomically and physiologically unrelated to a ranula; ranulas originate from the sublingual gland in the floor of mouth, not the parotid gland.',
    ],
    'v137_tps_11': [
        'Exploring a scarred, previously operated neck without imaging guidance substantially increases the risk of recurrent laryngeal nerve injury and devascularization of remaining normal parathyroid tissue.',
        'Assuming a wrong-lobe thyroidectomy was performed is speculative and does not substitute for confirming the actual diagnosis; persistent hypercalcemia after parathyroid surgery is usually due to a missed hyperfunctioning gland, not a thyroid lobe issue.',
        'Correct.',
        'Prior pathology reports establish which gland(s) were removed and their weight/histology, which is essential information for planning a safe reoperation; proceeding without this record risks re-exploring already-excised sites or missing a supernumerary/ectopic gland.',
    ],
    'v137_tps_12': [
        'A normal-sounding voice does not exclude a subclinically compensated unilateral vocal-fold paralysis; laryngoscopy is mandatory before any thyroid reoperation to establish a true functional baseline.',
        'Correct.',
        'Blind exploration of a previously dissected central neck, without imaging to map disease extent, risks injury to the recurrent laryngeal nerve and remaining parathyroid tissue in a field already distorted by scar.',
        'The prior operative report documents which structures were previously identified, ligated, or placed at risk (e.g., which side the RLN was dissected on, extent of prior dissection), information that is essential for safely planning reoperation.',
    ],
    'v137_tps_13': [
        'Secondary hyperparathyroidism from chronic kidney disease characteristically causes diffuse multigland hyperplasia rather than a single adenoma, so a focused single-gland excision would leave hyperfunctioning tissue behind and fail to control the disease.',
        "Thyroid lobectomy addresses thyroid pathology, not parathyroid hyperplasia, and would not lower PTH or improve the patient's renal osteodystrophy/bone pain.",
        'Surgical parathyroidectomy is an established and effective option for renal hyperparathyroidism refractory to medical therapy (calcimimetics, phosphate binders, vitamin D analogs); stating no surgical option exists is incorrect.',
        'Correct.',
    ],
    'v137_tps_14': [
        'Neck dissection is an oncologic procedure for lymphatic metastases and has no role in managing a benign obstructive sialolithiasis.',
        'Total parotidectomy would remove an unaffected gland (the pathology here is submandibular) and is a far more invasive option than warranted for a small, mobile, hilar stone.',
        'Correct.',
        'RAI targets thyroid follicular cells via the sodium-iodide symporter and has no mechanism of action against a salivary duct stone.',
    ],
    'v137_tps_15': [
        'The optic nerve is not anatomically related to the submandibular triangle and is never at risk during submandibular gland excision; this choice describes an unrelated surgical field entirely.',
        'Correct.',
        'The facial nerve trunk exits the stylomastoid foramen and courses through the parotid gland, not the submandibular triangle; only its marginal mandibular branch, which crosses superficial to the gland region, is at risk during submandibular excision.',
        'The recurrent laryngeal nerve runs in the tracheoesophageal groove near the thyroid gland and is not encountered during submandibular gland surgery, which is a separate anatomic region in the neck.',
    ],
    'v137_tps_16': [
        'Correct.',
        "Mild lid retraction is a common, non-emergent finding in Graves ophthalmopathy from sympathetic overactivity and levator/Müller's muscle involvement; it does not by itself threaten vision or require emergent intervention.",
        'Stable, non-progressive proptosis without visual compromise reflects inactive or mild thyroid eye disease and can typically be managed electively rather than as an emergency.',
        'Dry eye responsive to lubrication reflects exposure keratopathy from lid retraction/proptosis, a manageable and common finding, not the sight-threatening optic nerve compression that defines an ophthalmic emergency.',
    ],
    'v137_slp_01': [
        'UPPP targets retropalatal anatomic obstruction and would not correct apneas that occur without respiratory effort (central events) or address hypoventilation, so it is the wrong intervention for this pattern.',
        'Apneas without respiratory effort are, by definition, central rather than obstructive; assuming tongue-base obstruction ignores the polysomnographic evidence pointing to a non-anatomic mechanism.',
        'Correct.',
        'Sustained nocturnal hypercapnia is a critical physiologic clue pointing toward hypoventilation syndromes (e.g., obesity hypoventilation, neuromuscular disease) that require ventilatory support rather than anatomic airway surgery; disregarding it would miss the diagnosis.',
    ],
    'v137_slp_04': [
        'Jumping to maximum amplitude on postoperative day 1, before tissue swelling has resolved and before the patient has acclimated, risks patient intolerance, arousal from stimulation, and does not follow the standard staged activation protocol.',
        'The sensing lead is a functional component of hypoglossal nerve stimulator systems that detects respiratory effort to synchronize stimulation with inspiration; removing it after an uncomplicated implantation is neither indicated nor part of any recognized protocol.',
        'HNS therapy requires ongoing follow-up for device activation, amplitude titration, and efficacy assessment (often with a follow-up sleep study); stating no follow-up is required contradicts the standard postoperative care pathway.',
        'Correct.',
    ],
    'v137_slp_05': [
        'Automatically explanting a functioning, well-tolerated device without first investigating the cause of residual events discards a potentially salvageable therapy and skips standard troubleshooting.',
        'Increasing amplitude without first evaluating electrode function, tongue-motion pattern, and adherence risks worsening discomfort or arousal without addressing the actual cause of suboptimal response.',
        'Adding sedatives to help a patient tolerate more stimulation does not address why residual AHI remains elevated and can also blunt upper-airway dilator muscle tone, worsening sleep apnea rather than improving titration success.',
        'Correct.',
    ],
    'v137_slp_08': [
        'Correct.',
        'Maxillomandibular advancement is an irreversible, major skeletal procedure; jumping to MMA before addressing correctable interface issues (mask fit, humidification, nasal obstruction, pressure mode) bypasses far less invasive and often effective solutions.',
        'Stopping PAP therapy indefinitely abandons the first-line treatment for severe OSA without exhausting modifiable factors that commonly explain intolerance, leaving significant cardiovascular and neurocognitive risks unaddressed.',
        'Sedating a patient to force mask tolerance does not resolve the underlying causes of discomfort (dryness, leak, pressure intolerance) and can blunt arousal responses needed to correct mask problems overnight, and does not represent standard PAP optimization.',
    ],
    'v137_slp_09': [
        'Retinal detachment is an ophthalmologic emergency unrelated to the pharyngeal anatomy addressed by palatal surgery and is not a recognized complication of UPPP-type procedures.',
        'Correct.',
        'Facial paralysis is not an expected complication of palatal surgery, since the surgical field for palatal procedures does not involve the facial nerve, which courses through the parotid gland and temporal bone, well outside the oropharynx.',
        'Sensorineural hearing loss involves the cochlea or auditory nerve and is not caused by soft-palate surgery, which does not involve the otologic system.',
    ],
    'v137_slp_10': [
        'Tongue-base resection targets retrolingual, not retropalatal, obstruction; performing it as mandatory therapy when DISE shows isolated velum collapse without tongue-base obstruction would treat the wrong anatomic level.',
        'Drug-induced sleep endoscopy is a core tool in modern sleep surgery for identifying the specific site(s) and pattern of collapse under sedation, directly guiding procedure selection; stating it has no role contradicts current phenotype-based practice.',
        'Isolated nasal surgery improves nasal resistance and CPAP tolerance but does not reliably cure OSA on its own, especially when DISE demonstrates the primary obstruction is at the velum, not the nose.',
        'Correct.',
    ],
    'v137_slp_11': [
        'Adult AHI severity thresholds (mild ≥5) do not apply to children; pediatric OSA is typically defined at much lower obstructive AHI thresholds (often ≥1-2 events/hour), so an AHI of 8 with desaturations in a child is clinically significant, not merely borderline-normal by adult standards.',
        'Obstructive events, not just central events, are the primary and most clinically relevant finding here given the obstructive AHI of 8 and adenotonsillar hypertrophy; disregarding obstructive events would miss the actual diagnosis.',
        'Correct.',
        'Pediatric PSG is a validated and essential tool for diagnosing and grading pediatric OSA severity and directly informs decisions such as adenotonsillectomy; dismissing its utility contradicts standard pediatric sleep medicine practice.',
    ],
    'v137_slp_13': [
        'DISE in this patient shows dominant tongue-base collapse without complete concentric palatal collapse, meaning palatal surgery alone would not address the primary obstructive site and would likely yield a suboptimal result.',
        'Multiple validated tongue-base procedures exist (e.g., lingual tonsillectomy, midline glossectomy, genioglossus advancement, tongue-base suspension, hypoglossal nerve stimulation); stating no procedure can target the tongue base is factually incorrect.',
        'Correct.',
        'Tracheostomy bypasses the upper airway entirely and is reserved for severe, refractory OSA or specific failure of other interventions; it is not first-line therapy for a patient who has not yet undergone anatomy-directed surgical treatment.',
    ],
    'v137_fpt_01': [
        'Standardized photography documents anatomy for planning and medicolegal purposes but cannot substitute for a hands-on physical examination assessing skin quality, cartilage strength, and dynamic function.',
        'No preoperative analysis can guarantee a specific cosmetic outcome, since healing, scar formation, and soft-tissue behavior are inherently variable between patients.',
        'Correct.',
        'While photographs support documentation and billing, their primary surgical purpose is establishing objective, reproducible anatomic analysis and goal-setting, not administrative use.',
    ],
    'v137_fpt_02': [
        'Filler alone does not address the underlying muscular hyperactivity causing dynamic glabellar rhytids (corrugator/procerus contraction); it treats volume loss, not muscle-driven movement lines.',
        'Facelift repositions ptotic soft tissue and skin laxity from aging and does not treat epidermal pigmentary changes from photodamage, which require skin-directed therapies like resurfacing or topical treatments.',
        'Dynamic muscle-driven rhytids and static photodamage arise from fundamentally different mechanisms (muscle contraction versus cumulative UV-induced skin injury) and require different, mechanism-matched treatments, so no distinction being needed is incorrect.',
        'Correct.',
    ],
    'v137_fpt_03': [
        'Removing additional lower lateral cartilage would further weaken alar support, worsening the retraction and stenosis rather than correcting the structural deficit created by the original overresection.',
        'Turbinate reduction addresses intranasal airflow at the inferior turbinates and does not correct external nasal valve narrowing or alar retraction, which are structural/support problems of the lower lateral cartilages and alar rim.',
        'Fixed severe vestibular stenosis causing functional and cosmetic deformity warrants active reconstructive intervention rather than observation, since it will not spontaneously resolve once cartilage support has been lost.',
        'Correct.',
    ],
    'v137_fpt_04': [
        'Making the second lobe larger than the primary defect is not a standard design principle and can create excess bulk and unfavorable tension/pincushioning rather than a well-camouflaged, tension-free closure.',
        'Correct.',
        'Ignoring relaxed skin tension lines when planning incisions increases the risk of visible, poorly camouflaged scars, which runs counter to fundamental principles of facial reconstructive flap design.',
        'The bilobed flap is best suited to small-to-moderate defects with adjacent tissue laxity, such as those on the nasal tip/dorsum/sidewall; applying it to every full-thickness defect regardless of size ignores its size limitations and can produce excessive tension or distortion in larger defects.',
    ],
    'v137_fpt_05': [
        'A split-thickness skin graft alone is a reasonable option in some cases but is not the only possible reconstruction for this defect and generally yields inferior color/texture match and contour compared to local flap options with similar vascularity and laxity.',
        'The forehead flap is primarily a workhorse for nasal reconstruction based on the supratrochlear vessels; it is not the standard first choice for a lateral cheek defect, which has different regional donor tissue options with better proximity and match.',
        'Leaving a large cheek defect after cancer resection unclosed would risk infection, poor wound healing, and unacceptable functional/cosmetic outcome; closure is required.',
        'Correct.',
    ],
    'v137_fpt_06': [
        'A static sling only provides passive support/symmetry at rest and cannot generate active, volitional smile movement, since it has no contractile muscle component.',
        'A skin graft only replaces missing skin coverage and has no muscular or neural component, so it cannot restore any active facial movement.',
        'Correct.',
        'Botulinum toxin is a chemodenervating agent that weakens muscle contraction; it is typically used on the contralateral normal side to improve symmetry, not as a treatment to restore movement to the paralyzed side.',
    ],
    'v137_fpt_07': [
        'Correct.',
        'Maximal strengthening of every facial muscle without a targeted approach can worsen synkinesis by reinforcing the same aberrant co-contraction patterns rather than isolating and retraining selective, appropriate movement.',
        'Synkinesis is a recognized, treatable condition; neuromuscular retraining and targeted chemodenervation have well-documented efficacy in reducing unwanted co-contractions, so stating it cannot be treated is incorrect.',
        'A free flap is used for reconstructing tissue loss or providing dynamic reanimation in complete, irreversible paralysis, not for managing synkinesis in a patient who is recovering facial function with an intact, albeit miswired, nerve.',
    ],
    'v137_fpt_08': [
        'The forehead flap provides vascularized external skin cover only; it does not automatically supply missing internal mucosal lining, which must be separately reconstructed with options such as mucosal flaps, grafts, or folded lining flaps.',
        "Successful forehead flap harvest and design specifically depend on detailed knowledge of the supratrochlear artery's course to preserve the vascular pedicle; this knowledge is essential, not irrelevant.",
        'Correct.',
        'The forehead flap is generally reserved for larger or full-thickness nasal defects where its robust vascularity and skin match are advantageous; it is not typically used for very small defects, which are better served by local flaps or grafts.',
    ],
    'v137_fpt_09': [
        'Follicular units harvested from the androgen-resistant occipital donor region retain that resistance after transplantation (donor dominance) and generally do not develop the miniaturization seen in androgen-sensitive recipient-site follicles, which is the biological basis for why transplantation works.',
        'Hair direction and angle at the recipient site are critical to achieving a natural-appearing result; disregarding hair direction leads to unnatural growth patterns and an unnatural cosmetic outcome.',
        'Correct.',
        "Donor hair supply is finite and determined by the patient's stable occipital/parietal fringe; treating it as unlimited leads to poor planning and can exhaust future donor reserve, especially problematic if alopecia progresses further.",
    ],
    'v137_fpt_10': [
        'Selecting a flap before examining the actual defect ignores critical variables like depth, subunit involvement, and lining/support loss that determine which reconstructive option is truly appropriate.',
        'Closing every defect primarily under tension, regardless of size or laxity, risks wound dehiscence, distortion of adjacent free margins (such as the alar rim or nostril), and poor cosmetic outcome.',
        'Correct.',
        'Reconstructing before margins are confirmed clear risks having to revise or take down a completed reconstruction if additional tumor is found on further Mohs stages, wasting tissue and increasing morbidity.',
    ],
    'v137_fpt_11': [
        'Correct.',
        'Open rhinoplasty, like any surgical approach, does not eliminate postoperative edema; in fact, the additional dissection required for full exposure typically results in more prolonged tip edema compared to closed approaches.',
        'The open approach requires a transcolumellar incision, which, while it usually heals inconspicuously, does leave a scar; stating it never leaves a scar is factually inaccurate.',
        'Open rhinoplasty specifically allows the surgeon to directly visualize and often modify tip support mechanisms (e.g., via delivery of the lower lateral cartilages), meaning it does disturb and directly manipulate tip support structures, not avoid them.',
    ],
    'v137_fpt_12': [
        'Excising the entire auricle is a radically inappropriate response to prominent ears from soft-tissue/cartilage contour issues; the ear framework itself is not diseased and should be preserved and reshaped, not removed.',
        'Skin excision alone does not address the underlying cartilaginous deformities (absent antihelical fold, deep conchal bowl) responsible for ear prominence and would not achieve durable correction.',
        'Correct.',
        'Waiting until adulthood is not required in every case; otoplasty is commonly and safely performed in childhood (often around school age) once the ear has reached near-adult size, and earlier correction can reduce psychosocial impact.',
    ],
    'v137_fpt_13': [
        'A skin graft for both lamellae would fail because the posterior lamella requires a mucosalized, rigid structural substitute (e.g., tarsoconjunctival tissue or a graft) to protect the globe; a skin graft on the posterior lamella would cause corneal irritation and lacks the needed structural support.',
        'Correct.',
        'Canthal support (horizontal lid tightening/tensioning) is essential to prevent lid malposition, ectropion, and globe exposure in large eyelid defect reconstruction; disregarding it risks functional failure of the reconstruction.',
        'Leaving the globe exposed risks exposure keratopathy, corneal ulceration, and vision loss; adequate lid reconstruction to protect the cornea is a fundamental goal of eyelid surgery.',
    ],
    'v137_fpt_14': [
        'An auricular composite graft to the earlobe is unrelated to nasal valve reconstruction; composite auricular cartilage grafts are used for structural nasal support (e.g., alar rim/lobule), not applied to the earlobe itself.',
        'Correct.',
        'Bone grafting to the mandible addresses mandibular skeletal deficiency and has no relationship to internal nasal valve support or the nasal middle vault.',
        'Structural cartilage grafts, particularly spreader grafts, are a well-established and classic method for widening and supporting the internal nasal valve; stating no graft can affect the valve contradicts standard rhinoplasty technique.',
    ],
    'v137_fpt_15': [
        'Immediate wide excision of an actively hypertrophic, still-maturing scar risks recurrence and does not allow the scar to complete its natural remodeling process, which can improve appearance without surgery.',
        'Correct.',
        'Radiation therapy is not standard first-line treatment for a benign hypertrophic scar and carries risks (skin atrophy, pigment change, theoretical malignancy risk) that are not justified for this indication; it is generally reserved for high-risk keloid adjuncts, not typical hypertrophic scars.',
        'Multiple treatments (silicone sheeting, pressure therapy, intralesional corticosteroids, laser) have demonstrated efficacy in improving hypertrophic scar symptoms and appearance, so stating no treatment can help is incorrect.',
    ],
}


def apply_why_wrong_fix_vignettes_v137_v1(data_module):
    """Overwrite only the untouched generic v137 explanations; return count updated."""
    byid = {q.get('id'): q for q in data_module.CLINICAL_CHALLENGES_V119 if q.get('id')}
    updated = 0
    skipped_already_edited = []
    missing = []
    for qid, new_why_wrong in WHY_WRONG_FIXES_V137.items():
        q = byid.get(qid)
        if q is None:
            missing.append(qid)
            continue
        current = q.get('why_wrong') or []
        is_untouched_generic = bool(current) and all(
            str(w).strip() in (GENERIC_MARKER_V137, 'Correct.') for w in current
        ) and any(str(w).strip() == GENERIC_MARKER_V137 for w in current)
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
        print(f'why_wrong_fix_vignettes_v137_v1: {len(missing)} ids not found: {missing}')
    if skipped_already_edited:
        print(f'why_wrong_fix_vignettes_v137_v1: {len(skipped_already_edited)} ids already edited, skipped: {skipped_already_edited}')
    return updated
