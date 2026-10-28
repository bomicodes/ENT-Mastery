"""v47.1 authored Concept Checks — General ENT / Emergencies (part E)."""

CHECKS = [
("Evidence Interpretation / Outcomes Research",
 "A screening test for nasopharyngeal carcinoma has 95 percent sensitivity and 95 percent specificity. It is applied to a low-risk US population where prevalence is 1 in 10,000. Why will most positive results be false positives?",
 "Low prevalence lowers PPV",
 [("Sensitivity is too low to detect cancer", "Sensitivity is high; the problem is the rarity of disease."),
  ("Specificity falls when prevalence is low", "Specificity is a property of the test and does not change with prevalence."),
  ("The test was validated in the wrong country", "Validation setting is not the core reason; the arithmetic of prevalence is.")],
 "With 10,000 people tested, about 1 true case is found while 5 percent of 9,999 healthy people (about 500) test positive, so PPV is about 0.2 percent. Predictive values depend on prevalence; sensitivity and specificity do not.",
 "Rare disease + good test = mostly false positives."),

("Pain Management in the Head & Neck Patient",
 "A 5-year-old with obstructive sleep apnea is being discharged after adenotonsillectomy. A family member asks why the surgeon will not prescribe the acetaminophen-codeine syrup that worked for an older sibling. What is the reason?",
 "Unpredictable morphine conversion",
 [("Codeine is too weak to control tonsil pain", "Potency is not the reason; the risk is unpredictable morphine exposure."),
  ("Codeine increases post-tonsillectomy bleeding", "Codeine does not increase hemorrhage risk; the danger is respiratory depression."),
  ("Codeine is poorly absorbed after surgery", "Absorption is not the problem; metabolism is.")],
 "CYP2D6 converts codeine to morphine. Ultrarapid metabolizers produce high morphine levels, and children with OSA are especially sensitive to respiratory depression, which led to deaths and an FDA contraindication. Scheduled acetaminophen and ibuprofen are standard.",
 "No codeine or tramadol after pediatric tonsillectomy."),

("Geriatric Otolaryngology / Frailty",
 "An 84-year-old with slow gait, unintentional 6 kg weight loss, and weak grip is being considered for a long head and neck resection. Why is frailty assessment more useful than age alone?",
 "Frailty predicts complications",
 [("Age determines eligibility for surgery", "Chronological age alone is a poor predictor of outcomes."),
  ("Frailty only predicts length of stay", "Frailty predicts complications, delirium, and mortality too."),
  ("Frail patients always do better with surgery", "Frailty increases surgical risk.")],
 "Frailty reflects reduced physiologic reserve across systems. Frailty scores predict postoperative complications, delirium, discharge to care facilities, and mortality better than age, guiding shared decision-making and prehabilitation.",
 "Measure frailty, not just age."),

("Immunocompromised Host in Otolaryngology",
 "A liver transplant recipient on tacrolimus has 2 weeks of sinus pain and a black lesion on the middle turbinate. Why must this be treated differently than sinusitis in a healthy patient?",
 "Invasive fungal infection is much more likely",
 [("Transplant patients cannot receive antibiotics", "Antibiotics are allowed but insufficient here."),
  ("Immunosuppression makes CT unreliable", "CT remains useful."),
  ("Bacterial sinusitis is impossible in transplant patients", "Bacterial sinusitis still occurs.")],
 "Impaired neutrophil and T-cell immunity allows angioinvasive fungi. Black or pale insensate mucosa requires urgent biopsy, debridement, antifungals, and reducing immunosuppression.",
 "Immunocompromised + dark nasal mucosa = invasive fungal disease until proven otherwise."),

("Oral Manifestations of Systemic Disease",
 "A 55-year-old has painful oral erosions that peel with minimal pressure (positive Nikolsky sign). Biopsy shows intraepithelial blisters with acantholysis. What is the diagnosis?",
 "Pemphigus vulgaris",
 [("Mucous membrane pemphigoid", "Pemphigoid shows subepithelial blisters without acantholysis."),
  ("Oral lichen planus", "Lichen planus shows lace-like white striae and band-like lymphocytes."),
  ("Recurrent aphthous ulcers", "Aphthae are discrete ulcers without blistering or acantholysis.")],
 "Antibodies against desmoglein 3 disrupt cell adhesion within the epithelium, causing acantholysis and fragile intraepithelial blisters. Oral lesions often precede skin lesions; systemic immunosuppression is required.",
 "Intraepithelial blisters with acantholysis = pemphigus."),

]
