"""v21.2 — deliberate learning-ladder curation, Rhinology pass 7.

Closes five allergy/rhinitis concepts without duplicating strong existing application
cases. Existing v14.1/v14.4 cases are staged as application where appropriate;
true recognition foundations and senior/chief decisions are added only when missing.
"""
DOMAIN = "Rhinology / Allergy / Skull Base"

REUSED_APPLICATION_IDS_V212 = {
    "v141_rhi_01": "Allergic Rhinitis",
    "v141_rhi_02": "Allergen Immunotherapy — SCIT / SLIT",
    "v144_rh_01": "Allergy Testing & Interpretation",
    "v144_rh_14": "Nonallergic Rhinitis / Rhinitis Medicamentosa",
}
REVIEWED_FOUNDATION_IDS_V212 = {
    "v144_rh_11": "Local Allergic Rhinitis",
}


def _q(qid, topic, stage, stem, choices, answer, explanation, why_wrong,
       pearl, curveball, focus="boards"):
    return {
        "id": qid, "domain": DOMAIN, "topic": topic,
        "learning_stage": stage, "stem": stem, "choices": choices,
        "answer": answer, "explanation": explanation, "why_wrong": why_wrong,
        "board_pearl": pearl, "curveball": curveball,
        "tier": "Curated learning ladder", "mode": "Vignette",
        "focus": focus, "ladder_reviewed": True,
    }


VIGNETTES_V212 = [
    _q(
        "v212_rhi_ar_found", "Allergic Rhinitis", "foundation",
        "A 19-year-old develops recurrent sneezing, nasal itching, clear rhinorrhea, and congestion each spring. Examination during symptoms shows pale boggy turbinates. Which diagnosis best fits?",
        ["Allergic rhinitis", "Acute bacterial rhinosinusitis", "CSF rhinorrhea", "Rhinitis medicamentosa"], 0,
        "Seasonal itching, sneezing, watery rhinorrhea, congestion, and pale edematous mucosa are a classic IgE-mediated allergic rhinitis phenotype. The temporal exposure pattern is especially useful before any testing is ordered.",
        ["Correct. The symptom cluster and seasonal exposure pattern are characteristic of allergic rhinitis.", "ABRS is suggested by a bacterial temporal pattern such as persistence or double worsening with purulent symptoms, not recurrent itching and sneezing tied to a season.", "A CSF leak is usually unilateral, watery, often positional, and does not produce the classic itching/sneezing allergic syndrome.", "Rhinitis medicamentosa requires chronic topical vasoconstrictor exposure and primarily causes rebound obstruction."],
        "Itch plus sneeze plus watery rhinorrhea is an allergy pattern until the history gives you a better mechanism.",
        "Which features would make you test for a specific allergen rather than treat empirically?"
    ),
    _q(
        "v212_rhi_ar_snr", "Allergic Rhinitis", "senior_decision",
        "A patient reports 'severe allergies' despite months of intranasal steroid use. Endoscopy is normal, the spray is aimed directly at the septum and used only on bad days, and symptoms are predominantly congestion without itching or sneezing. What is the best senior-level next step?",
        ["Escalate immediately to chronic systemic corticosteroids", "Correct medication technique/adherence and reassess whether the phenotype is actually allergic before escalating therapy", "Schedule ESS because intranasal steroid failure proves sinus disease", "Begin allergen immunotherapy without establishing clinically relevant sensitization"], 1,
        "Apparent treatment failure should trigger an audit of diagnosis, technique, adherence, and dominant symptom mechanism. Intranasal corticosteroids work best with regular use and correct lateral aiming; a nonclassic symptom phenotype should also reopen structural and nonallergic causes before stronger treatment is added.",
        ["Long-term systemic corticosteroids create substantial harm and are inappropriate before basic diagnosis and topical-delivery problems are corrected.", "Correct. Senior care distinguishes true pharmacologic failure from poor delivery, intermittent use, or the wrong diagnosis.", "ESS treats appropriately selected objective sinus disease, not isolated rhinitis symptoms without sinus inflammation.", "Immunotherapy should target clinically relevant IgE-mediated sensitization rather than an unverified label of allergy."],
        "Before calling allergic rhinitis refractory, verify that the patient has allergic rhinitis and that the medicine actually reaches the lateral nasal wall consistently.",
        "What structural or nonallergic diagnoses become more likely when obstruction dominates without itch, sneeze, or exposure linkage?"
    ),

    _q(
        "v212_rhi_ait_found", "Allergen Immunotherapy — SCIT / SLIT", "foundation",
        "Which patient is the best conceptual candidate for allergen immunotherapy?",
        ["A patient with clinically relevant IgE-mediated allergy whose symptoms remain important despite avoidance/pharmacotherapy or who prefers disease-modifying treatment", "A patient with negative testing and no exposure correlation who wants weekly injections", "A patient with uncontrolled severe asthma presenting for an SCIT dose", "A patient with bacterial sinusitis who wants fewer antibiotic courses"], 0,
        "Allergen immunotherapy is disease-modifying therapy for selected patients with clinically relevant IgE-mediated allergic disease. It requires a match between symptoms, exposure, and sensitization rather than treatment of nonspecific rhinitis.",
        ["Correct. The indication is clinically meaningful allergic disease in an appropriate patient, not a positive test in isolation.", "Without evidence that an allergen drives the symptoms, immunotherapy has no defined target.", "Uncontrolled asthma substantially increases the risk of severe systemic reactions and should be stabilized before SCIT dosing.", "Immunotherapy does not treat ordinary bacterial rhinosinusitis."],
        "Immunotherapy treats an allergen-driven disease relationship, not a laboratory result by itself.",
        "How do SCIT and SLIT differ in administration, systemic-reaction risk, and adherence burden?"
    ),
    _q(
        "v212_rhi_ait_snr", "Allergen Immunotherapy — SCIT / SLIT", "senior_decision",
        "A patient arrives for maintenance SCIT but reports a major asthma flare overnight, frequent rescue-inhaler use, and current wheezing. What is the safest decision?",
        ["Give the full maintenance dose because missing a dose is more dangerous than asthma", "Give twice the dose to overcome the flare", "Withhold the injection, assess/stabilize asthma, and resume with an appropriate dosing plan only when the patient is clinically safe", "Switch to a new allergen vial and inject immediately"], 2,
        "Poorly controlled asthma is a major risk factor for severe systemic reactions to subcutaneous immunotherapy. The correct decision on dosing day is safety assessment first: withhold treatment during a significant exacerbation, stabilize the airway disease, and then resume according to the clinical interval and protocol.",
        ["Administering SCIT during an acute asthma exacerbation increases risk and is not justified by schedule adherence.", "Dose escalation during active lower-airway instability compounds rather than reduces systemic-reaction risk.", "Correct. Immunotherapy is elective disease-modifying treatment; an unstable airway overrides the injection schedule.", "Changing the vial does not correct the patient's current physiologic risk and can introduce additional dosing uncertainty."],
        "For SCIT, today's asthma control matters more than today's place on the dosing calendar.",
        "What should the clinic be prepared to recognize and treat immediately if a systemic reaction develops after SCIT?"
    ),

    _q(
        "v212_rhi_test_found", "Allergy Testing & Interpretation", "foundation",
        "What does a positive skin-prick or serum allergen-specific IgE result establish by itself?",
        ["Sensitization to that allergen, which still requires clinical correlation to establish symptomatic allergy", "That the allergen must be the cause of every nasal symptom", "A diagnosis of chronic rhinosinusitis", "A need for immunotherapy regardless of exposure history"], 0,
        "Allergy testing demonstrates sensitization. Symptomatic allergic disease requires that the test result make sense with the patient's exposure and symptom pattern; otherwise a positive result can be clinically irrelevant.",
        ["Correct. Sensitization is necessary for ordinary IgE-mediated allergy but is not synonymous with clinically relevant disease.", "People can have positive tests to allergens that do not explain their symptoms.", "CRS requires its own chronic symptom and objective inflammatory criteria and is not diagnosed by allergy testing.", "Immunotherapy should be directed at clinically relevant sensitization, not every positive test."],
        "The test tells you what the immune system recognizes; the history tells you whether that recognition matters clinically.",
        "Which medications and skin conditions can make skin testing less reliable or impractical?"
    ),
    _q(
        "v212_rhi_test_snr", "Allergy Testing & Interpretation", "senior_decision",
        "A patient has severe perennial symptoms around a cat at home, but skin testing is completely negative while taking a daily sedating antihistamine and the histamine positive control also fails to react. How should the result be interpreted?",
        ["The negative allergen wheal definitively excludes cat allergy", "Diagnose local allergic rhinitis immediately without further evaluation", "Recognize that the test is uninterpretable because the positive control failed; address antihistamine suppression or use an appropriate alternative testing strategy", "Start cat immunotherapy solely from the exposure history"], 2,
        "Skin-prick testing requires valid controls. Antihistamines can suppress both allergen and histamine wheals, so a failed positive control means the apparent negatives cannot be trusted. The next step is to correct the testing conditions or use an alternative such as serum specific-IgE when appropriate.",
        ["A negative allergen result is not valid when the positive control is also suppressed.", "Local allergic rhinitis is a specialized diagnosis and should not be used to explain an invalid systemic test before correcting the test conditions.", "Correct. Controls determine whether the test itself worked before individual allergen results are interpreted.", "Exposure history is important, but immunotherapy still requires a sufficiently supported allergen-driven diagnosis."],
        "Never interpret the allergen wells before you interpret the controls.",
        "How would marked dermatographism change your preference between skin and serum testing?"
    ),

    _q(
        "v212_rhi_lar_app", "Local Allergic Rhinitis", "application",
        "A patient has reproducible seasonal itching, sneezing, watery rhinorrhea, and congestion, yet repeated skin-prick and serum specific-IgE tests are negative under valid testing conditions. Which next concept best explains a genuinely allergic-appearing phenotype?",
        ["Local allergic rhinitis, in which an IgE-mediated response may be confined to the nasal mucosa", "Bacterial sinusitis by definition", "Rhinitis medicamentosa without decongestant exposure", "Allergic disease is impossible whenever systemic tests are negative"], 0,
        "Local allergic rhinitis describes patients with an allergic nasal phenotype despite absent systemic sensitization on standard testing, with localized nasal allergic reactivity demonstrable in specialized settings. It should be distinguished from nonallergic trigger syndromes rather than used as a catch-all for every negative allergy test.",
        ["Correct. The concept is localized nasal allergic reactivity despite negative conventional systemic sensitization testing.", "The recurrent itching/sneezing/watery pattern lacks the infectious timing and findings expected for bacterial sinusitis.", "Rhinitis medicamentosa requires chronic topical alpha-agonist use.", "Systemic testing can be negative in local allergic rhinitis, although other nonallergic mimics still need consideration."],
        "Negative systemic testing narrows the allergy story; it does not automatically erase a reproducible allergic nasal phenotype.",
        "What specialized testing can support local allergic rhinitis when the distinction would change management?"
    ),
    _q(
        "v212_rhi_lar_snr", "Local Allergic Rhinitis", "senior_decision",
        "A patient with negative systemic allergy testing reports only watery rhinorrhea triggered by cold air, perfume, and eating spicy food, without itching, sneezing paroxysms, or a seasonal exposure pattern. What is the best senior interpretation?",
        ["Label this local allergic rhinitis solely because systemic tests are negative", "The trigger pattern is more consistent with nonallergic/neurogenic rhinitis; treat the dominant symptom mechanism rather than forcing an allergic diagnosis", "Start SCIT to multiple empiric allergens", "Order sinus surgery because rhinorrhea is refractory"], 1,
        "Local allergic rhinitis should retain an allergic clinical phenotype despite negative systemic testing. Irritant-, temperature-, or gustatory-triggered watery rhinorrhea without itch or allergen linkage is more consistent with nonallergic neural/glandular hyperreactivity and should be managed accordingly.",
        ["Negative testing alone does not define local allergic rhinitis; the clinical phenotype still matters.", "Correct. Mechanism-based classification prevents inappropriate immunotherapy and directs treatment such as intranasal anticholinergic therapy when rhinorrhea dominates.", "Empiric immunotherapy without evidence of a relevant allergen target is inappropriate.", "Rhinorrhea from a nonallergic neural mechanism has no routine sinus-surgical target."],
        "Local allergy is not the bucket for every rhinitis patient with a negative blood or skin test.",
        "Which history features would make gustatory rhinitis particularly likely?"
    ),

    _q(
        "v212_rhi_nar_found", "Nonallergic Rhinitis / Rhinitis Medicamentosa", "foundation",
        "A patient has chronic watery rhinorrhea triggered by cold air, strong odors, and temperature changes. There is little itching, systemic allergy testing is negative, and there is no chronic decongestant use. Which diagnosis best fits?",
        ["Nonallergic rhinitis", "Allergic fungal rhinosinusitis", "Acute invasive fungal rhinosinusitis", "Rhinitis medicamentosa"], 0,
        "Nonallergic rhinitis often presents with congestion and/or watery rhinorrhea triggered by irritants, weather, odors, or other non-IgE stimuli. The absence of prominent itching and allergen-specific exposure correlation helps distinguish it from classic allergic rhinitis.",
        ["Correct. Irritant and temperature-triggered symptoms without an IgE pattern are characteristic of nonallergic rhinitis.", "AFRS is a chronic inflammatory sinus/polyposis disorder with characteristic imaging and allergic mucin, not isolated trigger-induced watery rhinorrhea.", "Acute invasive fungal disease occurs in a very different high-risk host with tissue-invasive red flags.", "Rhinitis medicamentosa specifically requires chronic topical vasoconstrictor exposure and rebound congestion."],
        "Trigger pattern is physiology: cold air, odor, and eating often point to neural/glandular rhinitis rather than IgE allergy.",
        "Which medication is especially useful when watery rhinorrhea, rather than congestion, is the dominant complaint?"
    ),
    _q(
        "v212_rhi_nar_snr", "Nonallergic Rhinitis / Rhinitis Medicamentosa", "senior_decision",
        "A patient with rhinitis medicamentosa stops oxymetazoline and uses regular intranasal corticosteroid therapy. Six weeks later the rebound has resolved, but severe unilateral fixed obstruction persists and examination shows a marked caudal septal deviation. What is the best next decision?",
        ["Restart chronic oxymetazoline because persistent obstruction proves withdrawal failed", "Continue treating all obstruction as rhinitis medicamentosa indefinitely", "Reassess the remaining structural mechanism and discuss structural treatment when symptoms and examination remain concordant", "Begin systemic amphotericin"], 2,
        "Rhinitis medicamentosa can coexist with the structural problem that originally prompted decongestant overuse. Once rebound physiology has resolved, persistent fixed unilateral obstruction should be re-localized; a demonstrated caudal septal deformity may merit structural management rather than renewed vasoconstrictor dependence.",
        ["Restarting chronic topical vasoconstrictor use recreates the rebound cycle and does not correct a fixed septal deformity.", "The diagnosis should evolve when the reversible medication-induced component has resolved but a separate mechanism remains.", "Correct. Senior care separates reversible mucosal rebound from persistent structural obstruction and treats each mechanism appropriately.", "There is no invasive fungal syndrome in this scenario."],
        "A decongestant can create a second problem without erasing the first one that made the patient reach for the spray.",
        "How would dynamic nasal-valve collapse on inspiration further change the structural plan?"
    ),
]


def apply_learning_ladders_v212(challenges, item_id_fn):
    by_id = {q.get("id"): q for q in challenges if q.get("id")}
    touched = []
    for qid, topic in REUSED_APPLICATION_IDS_V212.items():
        q = by_id.get(qid)
        if q:
            q["topic"] = topic
            q["learning_stage"] = "application"
            q["ladder_reviewed"] = True
            q["concept_id"] = item_id_fn(DOMAIN, topic)
            touched.append(qid)
    for qid, topic in REVIEWED_FOUNDATION_IDS_V212.items():
        q = by_id.get(qid)
        if q:
            q["topic"] = topic
            q["learning_stage"] = "foundation"
            q["ladder_reviewed"] = True
            q["concept_id"] = item_id_fn(DOMAIN, topic)
            touched.append(qid)

    existing = {q.get("id") for q in challenges}
    added = []
    for q in VIGNETTES_V212:
        if q["id"] in existing:
            continue
        q["concept_id"] = item_id_fn(DOMAIN, q["topic"])
        challenges.append(q)
        existing.add(q["id"])
        added.append(q["id"])
    return {"reviewed_existing": len(touched), "added": len(added), "ids": added}
