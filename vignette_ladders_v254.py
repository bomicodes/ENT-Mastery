"""v25.4 — Laryngology / Voice / Swallowing deliberate ladder pass 5.

Closes five benign/premalignant vocal-fold concepts with explicit foundation ->
application -> senior-decision ladders. The questions emphasize tissue-preserving
phonomicrosurgery, appropriate use of voice therapy, malignancy risk stratification,
and recurrence prevention rather than lesion-name recall alone.
"""
DOMAIN = "Laryngology / Voice / Swallowing"


def _q(qid, topic, stage, stem, choices, answer, explanation, reasons, pearl,
       curveball, focus="boards"):
    return {
        "id": qid, "domain": DOMAIN, "topic": topic, "learning_stage": stage,
        "stem": stem, "choices": choices, "answer": answer,
        "explanation": explanation, "why_wrong": reasons,
        "board_pearl": pearl, "curveball": curveball,
        "tier": "Curated learning ladder", "mode": "Vignette", "focus": focus,
        "ladder_reviewed": True, "_coverage_reviewed_v211": True,
    }


VIGNETTES_V254 = [
    _q("v254_lar_benign_fnd", "Benign Vocal Fold Lesions", "foundation",
       "A teacher has persistent dysphonia. Flexible laryngoscopy shows a small mid-membranous lesion, but the diagnosis remains uncertain. Which next test best characterizes vibratory behavior and helps distinguish a superficial lesion from deeper stiffness?",
       ["Videostroboscopy", "Noncontrast neck CT", "Routine chest radiograph", "Esophageal manometry"], 0,
       "Videostroboscopy assesses mucosal-wave amplitude, periodicity, symmetry, closure pattern, and lesion effect on vibration. These features help distinguish common benign phonotraumatic lesions and identify deeper epithelial or lamina-propria stiffness.",
       ["Correct. Stroboscopy adds functional vibratory information that routine flexible white-light examination cannot provide.", "CT is useful for selected deep or oncologic questions but does not characterize the mucosal wave.", "Chest radiography does not characterize vocal-fold vibration.", "Manometry assesses esophageal pressure physiology, not a membranous vocal-fold lesion."],
       "For benign voice lesions, morphology matters, but the mucosal wave often tells you how deeply the lesion affects the phonatory cover.",
       "How would a focal absent or markedly reduced wave change your concern for a cyst, scar, or epithelial dysplasia?"),
    _q("v254_lar_benign_app", "Benign Vocal Fold Lesions", "application",
       "A professional voice user has a small benign-appearing phonotraumatic lesion, inefficient technique, heavy occupational voice demand, and no airway or cancer red flags. What is the best initial management principle?",
       ["Optimize behavioral contributors and voice therapy before deciding whether surgery is necessary", "Schedule immediate wide excision including the vocal ligament", "Prescribe prolonged complete voice rest as definitive therapy for every lesion", "Treat empirically with antibiotics regardless of examination"], 0,
       "Many benign phonotraumatic lesions improve when collision forces and inefficient technique are addressed. Voice therapy also establishes whether residual structural disease, rather than modifiable behavior, is driving disability before phonomicrosurgery is considered.",
       ["Correct. Initial treatment should match the functional mechanism and preserve the option of surgery for persistent structural disease.", "Wide excision sacrifices normal vibratory tissue and can create permanent scar.", "Short-term relative rest can be useful selectively, but prolonged complete rest is not definitive treatment for every benign lesion.", "Antibiotics do not treat a chronic benign phonotraumatic lesion without evidence of bacterial infection."],
       "The goal is not simply to remove a bump; it is to restore efficient vibration while preserving normal superficial lamina propria.",
       "Which findings would make you bypass prolonged conservative management and obtain tissue diagnosis?", "senior_management"),
    _q("v254_lar_benign_snr", "Benign Vocal Fold Lesions", "senior_decision",
       "After optimized voice therapy, a singer remains significantly limited by a discrete benign lesion. During microlaryngoscopy, what operative principle best protects long-term voice?",
       ["Use the smallest tissue-preserving microflap/dissection needed to remove the lesion while protecting normal epithelium, superficial lamina propria, and vocal ligament", "Resect a broad strip of normal mucosa around every benign lesion", "Deeply cauterize the entire free edge to prevent recurrence", "Remove the vocal ligament whenever the lesion is adherent"], 0,
       "Phonomicrosurgery prioritizes preservation of the layered vocal-fold microstructure. Excess mucosal loss, thermal injury, or ligament trauma can replace a treatable lesion with permanent stiffness and scar.",
       ["Correct. Precise tissue-sparing surgery minimizes the vibratory penalty while treating the structural lesion.", "Broad normal-mucosal resection unnecessarily increases scar risk.", "Diffuse thermal injury damages the pliable cover and can worsen voice permanently.", "Routine ligament sacrifice is incompatible with tissue-preserving phonosurgery and should not be used for a benign lesion."],
       "A technically complete excision is a failure if it destroys the vibratory cover that produced the patient's voice.",
       "How should you counsel a professional voice user when complete lesion removal and maximal mucosal preservation are in tension?", "OR_prep"),

    _q("v254_lar_nodule_fnd", "Vocal Fold Nodules", "foundation",
       "A young adult with heavy voice use has gradually progressive hoarseness. Stroboscopy shows bilateral symmetric lesions at the junction of the anterior and middle thirds of the membranous folds with an hourglass closure pattern. What is the most likely diagnosis?",
       ["Vocal fold nodules", "Unilateral vocal fold polyp", "Vocal process granuloma", "Laryngeal papillomatosis"], 0,
       "Vocal fold nodules classically arise bilaterally and symmetrically at the point of maximal mid-membranous collision and often create hourglass glottic closure.",
       ["Correct. Bilateral symmetric mid-membranous lesions in a phonotraumatic setting are classic for nodules.", "Polyps are more commonly unilateral and asymmetric.", "Granulomas arise posteriorly near the vocal process rather than at the mid-membranous striking zone.", "Papillomatosis usually produces exophytic papillomatous lesions rather than paired smooth collision lesions."],
       "Nodules are usually a collision-force disease before they are a surgical disease.",
       "How does a soft early nodule differ from a mature fibrotic nodule in expected response to therapy?"),
    _q("v254_lar_nodule_app", "Vocal Fold Nodules", "application",
       "A teacher with bilateral nodules has no suspicious epithelial features and has never had voice therapy. Which treatment should be emphasized first?",
       ["Structured voice therapy, vocal-efficiency training, and modification of phonotraumatic behaviors", "Immediate bilateral microflap excision before therapy", "Empiric radiation therapy", "Permanent whispering"], 0,
       "Voice therapy is first-line for typical nodules because the driving problem is repetitive collision and inefficient voice use. Many nodules regress or become functionally insignificant when the behavioral mechanism is corrected.",
       ["Correct. Treating the phonatory behavior addresses the cause and often avoids surgery.", "Surgery without correcting collision behavior risks recurrence and unnecessary scar.", "Radiation has no role for benign nodules.", "Whispering can itself be inefficient and is not a durable treatment strategy."],
       "For classic nodules, the resident should think voice therapy first and surgery selectively, not the reverse.",
       "What occupational accommodations can meaningfully reduce collision dose during a treatment course?"),
    _q("v254_lar_nodule_snr", "Vocal Fold Nodules", "senior_decision",
       "A professional singer has persistent firm fibrotic bilateral nodules after months of high-quality therapy and optimized technique. Voice limitation threatens employment. What is the best next decision?",
       ["Discuss highly conservative phonomicrosurgery with continued perioperative voice therapy after confirming the lesions, goals, and expected tradeoffs", "Perform aggressive bilateral stripping to guarantee no recurrence", "Continue identical therapy indefinitely despite a stable structural limitation", "Inject permanent filler into both normal folds instead of treating the lesions"], 0,
       "Surgery is reasonable for selected mature fibrotic nodules that remain functionally limiting despite expert therapy. The key is conservative lesion treatment integrated with ongoing behavioral correction and realistic counseling about scar and recovery.",
       ["Correct. Persistent structural disease after optimized therapy can justify tissue-sparing surgery in a carefully selected high-demand voice user.", "Aggressive stripping increases scar and can be more disabling than the nodules.", "When a stable fibrotic lesion remains limiting despite appropriate therapy, endless unchanged therapy may not address the residual structural problem.", "Augmenting normal folds does not correct bilateral collision lesions and introduces unnecessary material."],
       "Failure of good therapy does not make surgery mandatory, but it changes the risk-benefit discussion when a mature lesion is clearly the remaining limiter.",
       "How would you stage return to full-performance voice after bilateral phonomicrosurgery?", "senior_management"),

    _q("v254_lar_polycyst_fnd", "Vocal Fold Polyp / Cyst", "foundation",
       "A patient develops persistent unilateral dysphonia after a shouting episode. Stroboscopy shows a unilateral pedunculated mid-membranous lesion with preserved wave in surrounding mucosa. Which diagnosis is most likely?",
       ["Vocal fold polyp", "Bilateral vocal fold nodules", "Posterior vocal process granuloma", "Bilateral vocal fold paralysis"], 0,
       "Polyps are commonly unilateral phonotraumatic lesions and may be sessile or pedunculated. A cyst is typically subepithelial and often causes more focal reduction of the mucosal wave because it is embedded within the vibratory cover.",
       ["Correct. The unilateral exophytic lesion after acute phonotrauma is characteristic of a polyp.", "Nodules are classically bilateral and symmetric.", "Granulomas arise posteriorly over the vocal process.", "Vocal-fold paralysis is a motion disorder and does not produce this discrete lesion."],
       "Polyp versus cyst is not merely a naming exercise: depth and effect on the mucosal wave influence operative difficulty and scar risk.",
       "What stroboscopic feature makes a deeper cyst more likely than a superficial polyp?"),
    _q("v254_lar_polycyst_app", "Vocal Fold Polyp / Cyst", "application",
       "A small unilateral polyp causes moderate dysphonia in a patient with marked phonotraumatic behavior. There is no suspicious mucosal change. What is a reasonable management approach?",
       ["Begin voice therapy and behavior modification, then consider phonomicrosurgery if a persistent structural lesion remains functionally important", "Perform wide cordectomy immediately", "Observe any persistent unilateral lesion forever without reassessment", "Treat with systemic chemotherapy"], 0,
       "Some polyps improve with behavioral treatment, while persistent symptomatic structural lesions often respond well to tissue-preserving excision. Management should account for symptom burden, lesion morphology, voice demands, and response to therapy.",
       ["Correct. Conservative treatment can address the driver and clarify whether surgery is truly needed.", "Wide cordectomy is excessive for a benign-appearing small polyp and sacrifices normal vibratory tissue.", "Persistent unilateral lesions require appropriate follow-up, particularly if morphology changes or risk factors raise concern.", "Chemotherapy has no role for a benign polyp."],
       "Treat the behavior and the lesion as separate but interacting problems; surgery alone does not erase the collision pattern that created the lesion.",
       "Which lesion or patient features would make earlier operative treatment more reasonable?"),
    _q("v254_lar_polycyst_snr", "Vocal Fold Polyp / Cyst", "senior_decision",
       "During microflap excision of a true intracordal cyst, the cyst wall is densely adherent to the surrounding superficial lamina propria. What principle should guide dissection?",
       ["Balance complete cyst-wall removal against preservation of normal cover; avoid sacrificing large amounts of superficial lamina propria or vocal ligament merely to achieve a perfect-looking excision", "Excise the entire vocal ligament with the cyst to eliminate recurrence", "Use broad deep thermal cautery around the cyst bed", "Abandon magnification and remove the lesion blindly"], 0,
       "Cyst recurrence can occur if wall remains, but aggressive dissection that destroys normal lamina propria or ligament may create permanent scar. Senior phonosurgery requires judging when tissue preservation is more important than anatomically aggressive excision.",
       ["Correct. The desired endpoint is the best vibratory result, not maximal tissue removal at any cost.", "Ligament sacrifice creates major stiffness and is not justified for a benign intracordal cyst.", "Thermal injury to the vibratory cover increases fibrosis.", "Magnification and precise microdissection are central to safe cyst surgery."],
       "In phonosurgery, recurrence risk must be weighed against the irreversible cost of scar.",
       "If postoperative stroboscopy shows persistent stiffness despite adequate closure, how would management differ from recurrent mass effect?", "OR_prep"),

    _q("v254_lar_leuko_fnd", "Leukoplakia / Laryngeal Dysplasia", "foundation",
       "A smoker has a white plaque on the true vocal fold. Which statement is most accurate?",
       ["Leukoplakia is a descriptive appearance and does not by itself establish the histologic grade; dysplasia or carcinoma requires tissue-based assessment when clinically indicated", "Every white plaque is invasive squamous cell carcinoma", "Leukoplakia is always candidiasis", "A normal neck CT excludes epithelial dysplasia"], 0,
       "Vocal-fold leukoplakia describes a white epithelial lesion with a differential ranging from benign keratosis/inflammation to dysplasia and invasive carcinoma. Management depends on clinical risk and, when warranted, histopathology.",
       ["Correct. Appearance alone cannot reliably assign histologic grade.", "Many leukoplakic lesions are not invasive cancer, although malignancy must be considered.", "Fungal disease is one differential but not the definition of leukoplakia.", "CT lacks the resolution to exclude superficial epithelial dysplasia."],
       "Leukoplakia is what you see; dysplasia is what pathology tells you.",
       "Which endoscopic features increase concern enough to favor prompt biopsy rather than observation?"),
    _q("v254_lar_leuko_app", "Leukoplakia / Laryngeal Dysplasia", "application",
       "A patient with tobacco exposure has unilateral irregular thick leukoplakia, focal vascular abnormality, and reduced mucosal wave. What is the best next step?",
       ["Obtain tissue diagnosis with a planned biopsy/excision that preserves oncologic orientation while minimizing unnecessary injury to uninvolved vibratory tissue", "Assume benign keratosis and observe indefinitely", "Treat only with empiric reflux medication for a year", "Inject the lesion with filler"], 0,
       "Irregular morphology, vascular change, impaired wave, and carcinogen exposure increase concern for high-grade dysplasia or invasive disease. These findings favor timely tissue diagnosis rather than prolonged empiric treatment alone.",
       ["Correct. Suspicious epithelial disease requires histologic clarification while preserving options for definitive oncologic treatment.", "Indefinite observation risks delaying diagnosis of clinically important dysplasia or carcinoma.", "Reflux management may address a contributor but cannot substitute for biopsy of a suspicious lesion.", "Injection augmentation does not diagnose or treat epithelial dysplasia."],
       "The decision to biopsy is risk-stratified: morphology, vascularity, wave, progression, risk factors, and prior pathology all matter.",
       "How would suspected invasion change the depth and orientation of biopsy compared with a superficial office sample?", "senior_management"),
    _q("v254_lar_leuko_snr", "Leukoplakia / Laryngeal Dysplasia", "senior_decision",
       "A patient has recurrent vocal-fold dysplasia after prior excisions. Current disease is superficial, but repeated procedures are beginning to impair the mucosal wave. What is the best senior-level management principle?",
       ["Balance oncologic control with cumulative voice morbidity using pathology grade, lesion behavior, endoscopic risk, patient factors, and an individualized surveillance/office-or-OR treatment strategy", "Repeat progressively wider cordectomy for every recurrence regardless of grade", "Stop surveillance because prior specimens were not invasive", "Treat all recurrent dysplasia with antibiotics"], 0,
       "Laryngeal dysplasia can recur and progress, yet repeated treatment can scar the vibratory fold. Management therefore requires risk-adapted surveillance and treatment intensity rather than automatic escalation or complacency.",
       ["Correct. The chief-level decision integrates cancer risk, pathology, recurrence pattern, procedural morbidity, and the patient's voice priorities.", "Automatically widening every excision can impose major functional cost without regard to actual oncologic risk.", "Recurrent dysplasia still requires surveillance because future progression remains possible.", "Antibiotics do not treat epithelial dysplasia."],
       "Repeated dysplasia treatment is a longitudinal oncologic problem and a cumulative-function problem at the same time.",
       "Which change in pathology or endoscopic behavior would make organ-preserving surveillance insufficient?", "senior_management"),

    _q("v254_lar_gran_fnd", "Vocal Process Granuloma", "foundation",
       "A recently intubated patient has persistent throat discomfort and hoarseness. Laryngoscopy shows a smooth lesion centered on the posterior vocal process. What is the most likely diagnosis?",
       ["Vocal process granuloma", "Vocal fold nodule", "Reinke edema", "Anterior glottic web"], 0,
       "Vocal process granulomas arise posteriorly over the arytenoid vocal process and are associated with mucosal trauma from intubation, repetitive contact/phonotrauma, and other irritative contributors.",
       ["Correct. The posterior location and recent intubation are classic for a contact/intubation granuloma.", "Nodules occur at the bilateral mid-membranous striking zone.", "Reinke edema is diffuse superficial-lamina-propria swelling along the membranous folds.", "An anterior web is a tissue bridge across the anterior commissure rather than a focal posterior mass."],
       "Posterior vocal-process location should immediately separate granuloma from the common mid-membranous phonotraumatic lesions.",
       "Which atypical features should trigger biopsy rather than assuming a benign granuloma?"),
    _q("v254_lar_gran_app", "Vocal Process Granuloma", "application",
       "A patient has a typical vocal process granuloma after prolonged intubation with no suspicious features. What management best reduces recurrence risk?",
       ["Address mechanical/behavioral drivers with voice therapy and vocal-hygiene measures, treat relevant irritative contributors selectively, and reserve surgery for appropriate refractory or diagnostic situations", "Excise immediately without addressing contact forces", "Perform total laryngectomy", "Use repeated systemic antibiotics indefinitely"], 0,
       "Granulomas recur when the posterior contact/irritative mechanism persists. Initial treatment commonly targets voice behavior, throat clearing/cough, and relevant reflux or inflammatory contributors; excision alone may not solve the mechanism.",
       ["Correct. Mechanism-directed treatment reduces repeated posterior trauma and is central to durable management.", "Excision alone can be followed by rapid recurrence if collision forces remain unchanged.", "Total laryngectomy is grossly disproportionate for a benign-appearing granuloma.", "Chronic antibiotics do not address the usual mechanical pathophysiology."],
       "A granuloma is often a wound-healing response to continued posterior trauma; removing the wound without removing the trauma invites recurrence.",
       "When would airway symptoms, growth pattern, or oncologic uncertainty justify earlier operative evaluation?"),
    _q("v254_lar_gran_snr", "Vocal Process Granuloma", "senior_decision",
       "A large vocal process granuloma recurs twice after technically complete excision. Pathology is benign, but the patient has forceful glottic contact despite therapy. What is the best next strategy?",
       ["Reassess the recurrent mechanism and consider adjunctive reduction of posterior contact force, including selected botulinum toxin treatment, rather than simply repeating identical excisions", "Perform the same excision repeatedly without changing the plan", "Stop follow-up because pathology was benign", "Radiate the posterior glottis"], 0,
       "Recurrent granuloma after adequate excision is a signal to change the mechanism, not merely repeat the operation. In selected refractory cases, botulinum toxin can reduce forceful arytenoid/vocal-process contact while the mucosa heals, alongside continued behavioral management.",
       ["Correct. Refractory disease calls for a mechanism-directed strategy rather than an identical procedure with the same recurrence drivers.", "Repeating the same operation without addressing collision forces predictably preserves the recurrence mechanism.", "Benign pathology does not eliminate the need to manage symptomatic recurrent disease or reassess if morphology changes.", "Radiation is not appropriate treatment for a benign vocal process granuloma."],
       "When a benign lesion keeps recurring, ask what force or exposure is recreating it before reaching for the same instrument again.",
       "How would your plan change if the lesion became ulcerative, infiltrative, or progressively atypical despite prior benign pathology?", "senior_management"),
]


def apply_learning_ladders_v254(challenges, concept_id_fn):
    existing = {q.get("id") for q in challenges}
    added = []
    canonical_topics = set()
    for src in VIGNETTES_V254:
        q = dict(src)
        canonical_topics.add(q["topic"])
        q["concept_id"] = concept_id_fn(DOMAIN, q["topic"])
        if q["id"] in existing:
            continue
        challenges.append(q)
        existing.add(q["id"])
        added.append(q["id"])
    return {"added": added, "count": len(added), "topics": sorted(canonical_topics)}
