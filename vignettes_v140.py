"""v14.0 — high-risk depth pass after canonical coverage reached 100%.

Adds second, management-escalation cases for topics where one vignette is not
sufficient for overnight-call or OR readiness. Focus: airway, hemorrhage,
foreign body, deep neck infection, free-flap salvage, laryngectomy, neck
oncology, and pediatric airway emergencies.
"""


def Q(qid, domain, topic, stem, choices, answer, explanation, pearl, curveball, focus):
    return {
        "id": qid, "domain": domain, "topic": topic, "stem": stem,
        "choices": choices, "answer": answer, "explanation": explanation,
        "why_wrong": ["Compare this option with the time-critical management principle in the explanation." for _ in choices],
        "board_pearl": pearl, "curveball": curveball,
        "focus": focus, "tier": "Curated chief/call/OR", "mode": "Vignette",
    }

GEN = "General ENT / Emergencies"
HN = "Head & Neck Oncology"
PED = "Pediatric Otolaryngology"

VIGNETTES_V140 = [
    # General ENT / Emergencies — overnight call safety
    Q("v140_gen_01", GEN, "Post-Tonsillectomy Hemorrhage",
      "A 19-year-old presents 7 days after tonsillectomy after spitting a cup of bright-red blood. Bleeding has stopped on arrival, but there is a fresh clot in the tonsillar fossa. What is the safest next step?",
      ["Treat as a significant sentinel bleed: resuscitate, obtain IV access/labs, keep NPO, involve anesthesia and proceed to operative control when indicated", "Discharge because bleeding stopped", "Scrape the clot off at bedside", "Give food and observe at home"], 0,
      "Secondary post-tonsillectomy bleeding can recur briskly. A convincing bleed with fresh clot requires serious disposition and often OR control rather than false reassurance from temporary hemostasis.",
      "A tonsil bleed is an airway hemorrhage: resuscitation and definitive control planning occur together.",
      "The patient suddenly vomits blood and becomes hypotensive. How does induction and airway planning change?", "overnight_call"),

    Q("v140_gen_02", GEN, "Tracheostomy Emergency",
      "A tracheostomy placed 2 days ago becomes dislodged and the patient is desaturating. The stoma is immature. What is the safest principle?",
      ["Call for airway help and oxygenate from above when possible; avoid blind forceful reinsertion into an immature tract", "Force a tube through the stoma repeatedly", "Cover the mouth and nose", "Wait for the tract to mature"], 0,
      "Early tracheostomy dislodgement can create a false passage. A fresh tract may not be safely recannulated blindly; secure oxygenation and use direct visualization or controlled replacement.",
      "Know whether the tract is mature before treating a dislodged trach as a simple tube change.",
      "How does management differ in a mature laryngectomy stoma?", "overnight_call"),

    Q("v140_gen_03", GEN, "Angioedema",
      "A patient on an ACE inhibitor develops rapidly progressive tongue and floor-of-mouth swelling with a muffled voice but no urticaria. What is the priority?",
      ["Early airway assessment and controlled airway planning before obstruction becomes complete", "Wait for stridor before calling anesthesia", "Treat only with antibiotics", "Perform oral examination repeatedly until swelling worsens"], 0,
      "Bradykinin-mediated angioedema may not respond reliably to antihistamines/epinephrine; airway trajectory is the critical decision.",
      "Do not wait for oxygen saturation to fall—upper-airway obstruction can progress suddenly while saturation remains normal.",
      "Which anatomic sites on flexible laryngoscopy most strongly predict need for airway intervention?", "overnight_call"),

    Q("v140_gen_04", GEN, "Deep Neck Space Infection",
      "A patient with submandibular cellulitis has tongue elevation, drooling and a woody floor of mouth but no drainable collection on CT. What is the best next step?",
      ["Manage as Ludwig angina with early airway strategy and broad IV antibiotics; absence of abscess does not remove airway risk", "Discharge because there is no abscess", "Needle the floor of mouth blindly", "Wait for fluctuance"], 0,
      "Ludwig angina is a rapidly spreading cellulitis; airway compromise can occur without a discrete abscess.",
      "In deep-neck infection, airway risk is determined by anatomy and trajectory—not whether radiology uses the word abscess.",
      "What features would push you toward awake intubation versus awake tracheostomy?", "overnight_call"),

    Q("v140_gen_05", GEN, "Carotid Blowout Syndrome",
      "A previously irradiated patient with recurrent neck cancer has a self-limited episode of pulsatile oral bleeding. CTA shows tumor encasing an irregular exposed carotid segment. What is this event until proven otherwise?",
      ["A sentinel carotid bleed requiring urgent endovascular/surgical planning", "Benign mucositis", "Routine epistaxis", "Dental bleeding only"], 0,
      "Sentinel bleeding can precede catastrophic carotid rupture. Secure the airway as needed, resuscitate, reverse coagulopathy when appropriate and obtain urgent vascular/interventional support.",
      "The warning bleed is the opportunity to act before exsanguination.",
      "If the patient exsanguinates through the mouth, what bedside temporizing maneuvers can buy time?", "overnight_call"),

    Q("v140_gen_06", GEN, "Airway Foreign Body",
      "During rigid bronchoscopy for a peanut, the object slips proximally and completely obstructs the glottis. What is the immediate priority?",
      ["Maintain visualization and remove or push the object to re-establish ventilation rather than losing it blindly", "Stop the case and obtain CT", "Extubate and observe", "Wait for spontaneous passage"], 0,
      "Foreign-body bronchoscopy can convert partial into complete obstruction. Equipment, optical forceps and a shared rescue plan must be ready before manipulation.",
      "The most dangerous moment may be extraction across the glottis.",
      "What ventilation strategies can be used during rigid bronchoscopy?", "OR_prep"),

    Q("v140_gen_07", GEN, "Esophageal Foreign Body",
      "A child swallowed a button battery 90 minutes ago. AP and lateral films show it in the upper esophagus. What is the correct timing?",
      ["Emergent endoscopic removal now", "Observe overnight", "Wait for symptoms", "Push it into the stomach blindly"], 0,
      "An esophageal button battery can cause severe liquefactive necrosis within hours; removal is an emergency even if the child looks well.",
      "With batteries, symptoms lag behind tissue injury—time since ingestion is an operative variable.",
      "After removal, what injury patterns require vascular imaging or prolonged surveillance for delayed fistula?", "overnight_call"),

    Q("v140_gen_08", GEN, "Chyle Leak",
      "A patient has persistent 1.2-L/day chylous drainage despite fat restriction, pressure dressing and octreotide. What is the next management principle?",
      ["Escalate to procedural control such as neck re-exploration/ligation or thoracic-duct embolization depending on anatomy and resources", "Continue the same plan indefinitely", "Remove the drain", "Give anticoagulation as definitive treatment"], 0,
      "High-output persistent chyle leaks cause major nutritional and metabolic morbidity and frequently need definitive control.",
      "Output trend and physiology—not just the presence of milky fluid—drive escalation.",
      "Where is the thoracic duct typically encountered during left low-neck re-exploration?", "OR_prep"),

    Q("v140_gen_09", GEN, "ENT Perioperative Anesthesia / Difficult Airway Planning",
      "A patient with severe trismus and a large base-of-tongue tumor cannot tolerate lying flat. Which plan is most dangerous?",
      ["Routine IV induction and neuromuscular blockade before confirming ability to ventilate or access the airway", "Awake flexible intubation with surgical backup when feasible", "Awake tracheostomy in selected anatomy", "Multidisciplinary airway briefing"], 0,
      "Loss of spontaneous ventilation in a predicted impossible airway can turn partial obstruction into a cannot-intubate/cannot-oxygenate emergency.",
      "The safest difficult-airway plan preserves options until the airway is secured.",
      "What topicalization and sedation principles help an awake intubation succeed without losing ventilation?", "OR_prep"),

    Q("v140_gen_10", GEN, "Hemostasis / Coagulopathy / Antithrombotic Management in ENT",
      "Four hours after thyroidectomy, a patient on recently resumed anticoagulation develops neck pressure, dysphagia and expanding swelling. What should happen first?",
      ["Release the compressing wound immediately if airway compromise is evolving while mobilizing OR/anesthesia and reversal", "Wait for coagulation labs before touching the neck", "Send for routine ultrasound", "Observe for voice change"], 0,
      "A compressive postoperative neck hematoma is a clinical emergency; decompression cannot wait for imaging or perfect reversal when the airway is threatened.",
      "In a neck hematoma, the incision can become the fastest route to saving the airway.",
      "What specific bedside wound-opening sequence should the on-call resident know?", "overnight_call"),

    # Head & Neck Oncology — OR and postoperative salvage
    Q("v140_hn_01", HN, "Free-Flap Monitoring / Compromise / Salvage",
      "A free flap becomes pale and cool with absent Doppler signal and no bleeding on pinprick 4 hours after surgery. What vascular problem is most likely?",
      ["Arterial inflow compromise requiring urgent exploration", "Venous congestion", "Normal postoperative edema", "Chyle leak"], 0,
      "Pallor, coolness, absent capillary refill and absent pinprick bleeding suggest arterial compromise; salvage is time-dependent.",
      "Know arterial and venous failure phenotypes before you are the person called at 2 AM.",
      "At takeback, what sequence should be used to inspect geometry, anastomoses and thrombus?", "overnight_call"),

    Q("v140_hn_02", HN, "Total Laryngectomy",
      "On postoperative day 5 after total laryngectomy, saliva appears in the neck drain and erythema develops around the incision. What complication is most likely?",
      ["Pharyngocutaneous fistula", "Otitis externa", "BPPV", "Parotid fistula"], 0,
      "Pharyngocutaneous fistula typically presents with salivary drainage, erythema, wound breakdown or neck infection; management depends on size, sepsis, vessel exposure and prior radiation.",
      "After laryngectomy, protect major vessels from salivary contamination—fistula can become a carotid problem.",
      "When does vascularized tissue coverage become important rather than conservative wound care alone?", "postoperative_call"),

    Q("v140_hn_03", HN, "Neck Dissection",
      "During a level IV left neck dissection, a thin-walled structure is injured near the venous angle and clear lymphatic fluid appears. What is the best intraoperative response?",
      ["Control the thoracic duct leak with clips/ligation and test the field before closure", "Ignore it because drains will fix it", "Sacrifice the vagus nerve", "Pack with bone wax only"], 0,
      "Thoracic-duct injury is a known left low-neck risk; intraoperative recognition and secure control reduce postoperative high-output chyle leak.",
      "Know the complication before closing: ask anesthesia for positive pressure/Valsalva and inspect the low neck.",
      "What diet and drain strategy would you use if a low-output leak appears postoperatively?", "OR_prep"),

    Q("v140_hn_04", HN, "Laryngeal Preservation Decision",
      "A patient with T4a laryngeal SCC has tumor through thyroid cartilage into strap muscles and a poorly functional aspirating larynx. What is the strongest treatment principle?",
      ["Primary total laryngectomy is generally favored over nonsurgical organ preservation", "Chemoradiation always because the larynx is still anatomically present", "Observation", "Endoscopic excision only"], 0,
      "Gross extralaryngeal extension and poor baseline laryngeal function reduce the likelihood that chemoradiation will yield a useful preserved organ.",
      "Preserve function, not just anatomy.",
      "How would a T3 tumor with good swallowing and no cartilage penetration change the discussion?", "boards"),

    Q("v140_hn_05", HN, "Supraglottic Cancer",
      "A patient with supraglottic SCC has no palpable neck nodes. Why is elective bilateral neck treatment often still considered?",
      ["The supraglottis has rich bilateral lymphatic drainage and meaningful occult nodal risk", "The true vocal folds drain bilaterally at the same rate", "All larynx tumors require radical neck dissection", "It prevents aspiration"], 0,
      "Supraglottic tumors have much greater nodal risk than early glottic cancers; midline/epiglottic disease can drain bilaterally.",
      "Subsite anatomy predicts neck behavior.",
      "Which neck levels are typically at greatest risk for supraglottic SCC?", "boards"),

    Q("v140_hn_06", HN, "Oral Tongue SCC",
      "A 1.8 cm oral tongue SCC has a depth of invasion of 9 mm and a clinically N0 neck. What management issue becomes important?",
      ["Elective treatment of the ipsilateral neck because occult nodal risk rises with depth of invasion", "No neck treatment because the primary is under 2 cm", "Treat as HPV-positive oropharynx", "RAI"], 0,
      "Depth of invasion predicts occult nodal metastasis in oral cavity SCC and influences elective neck management.",
      "Do not confuse surface diameter with biologic depth.",
      "How close to midline must the primary be before contralateral neck risk materially changes?", "boards"),

    Q("v140_hn_07", HN, "Adverse Pathology and Adjuvant Therapy",
      "After oral cavity SCC resection, pathology shows a positive margin and extranodal extension. What adjuvant treatment is generally indicated for a fit patient?",
      ["Postoperative concurrent chemoradiation", "Observation", "Radiation is never useful after surgery", "RAI"], 0,
      "Positive margins and extranodal extension are classic high-risk features supporting postoperative chemoradiation when the patient can tolerate it.",
      "Know which pathology findings change RT to chemoradiation.",
      "How do close but negative margins, PNI, LVI and multiple nodes differ in adjuvant implications?", "boards"),

    Q("v140_hn_08", HN, "Carotid Blowout Syndrome",
      "During salvage neck surgery in an irradiated field, the carotid is exposed after infected tumor removal. What reconstructive principle reduces later blowout risk?",
      ["Cover the vessel with healthy vascularized tissue and eliminate salivary/infectious contamination", "Leave the vessel exposed under skin graft", "Pack infected gauze against it indefinitely", "No reconstruction is needed"], 0,
      "Radiation, infection, fistula and exposed vessel are major blowout risks; vascularized coverage is protective.",
      "Carotid blowout prevention begins in the OR by separating vessel from contaminated wounds.",
      "Which flap choices can provide robust vessel coverage when local tissue is irradiated?", "OR_prep"),

    Q("v140_hn_09", HN, "Nonfunctional Larynx / Chronic Aspiration After Cancer Therapy",
      "A disease-free patient has feeding-tube dependence and recurrent pneumonias despite intensive swallow therapy. What outcome should define whether further 'organ preservation' is successful?",
      ["Safe functional swallowing and pulmonary health, not simply an intact larynx on imaging", "Avoiding any surgery at all costs", "Voice quality only", "CT appearance only"], 0,
      "When the larynx cannot protect the lungs, definitive aspiration-prevention surgery may improve survival and quality of life despite loss of native voice.",
      "A preserved organ that cannot perform its essential function is not true functional preservation.",
      "What preoperative counseling distinguishes functional laryngectomy from cancer laryngectomy?", "boards"),

    Q("v140_hn_10", HN, "Reconstruction Selection After Head & Neck Ablation",
      "After total glossectomy with large oral cavity volume loss but preserved mandible, what reconstructive characteristic is most important?",
      ["Adequate soft-tissue bulk shaped to restore oral containment and facilitate swallowing", "Bone-only reconstruction", "Thin skin graft alone", "No reconstruction"], 0,
      "Defect-based reconstruction considers missing tissue and functional task; tongue-volume defects need soft tissue capable of separating oral cavity and assisting bolus propulsion.",
      "The best flap is the one whose tissue properties match the function you need to rebuild.",
      "How would segmental mandibulectomy change donor-site selection?", "OR_prep"),

    # Pediatric — airway and emergency depth
    Q("v140_ped_01", PED, "Epiglottitis",
      "A toxic 5-year-old is drooling, tripod-positioned and stridulous. The child becomes more distressed when staff approach with a tongue depressor. What should happen next?",
      ["Stop agitating the child and move with ENT/anesthesia to a controlled airway setting with surgical backup", "Force an oropharyngeal exam", "Send alone for CT", "Nebulize and discharge"], 0,
      "Suspected epiglottitis can deteriorate with agitation; airway planning takes precedence over proving the diagnosis at bedside.",
      "The safest exam may be the one you do after the airway is secured.",
      "What equipment and personnel should be in the OR before induction?", "overnight_call"),

    Q("v140_ped_02", PED, "Button Battery Ingestion",
      "After removal of a 20-mm esophageal button battery that had been impacted for 8 hours, endoscopy shows deep circumferential necrosis. What is the next principle?",
      ["Plan high-risk post-removal surveillance for delayed perforation, stricture and vascular fistula rather than assuming removal ends the danger", "Discharge immediately", "Resume solid food without assessment", "No follow-up imaging can ever be useful"], 0,
      "Battery injury can progress after removal; severe injury near great vessels can lead to delayed catastrophic aorto-esophageal fistula.",
      "With button batteries, the second emergency can occur days after the first one is removed.",
      "Which location and injury severity should prompt vascular imaging and prolonged monitoring?", "overnight_call"),

    Q("v140_ped_03", PED, "Pediatric Airway Foreign Body",
      "A toddler has a classic choking episode but now appears comfortable; chest x-ray is normal. What is the best next step if unilateral wheeze persists?",
      ["Proceed to bronchoscopy because a normal film does not exclude aspiration", "Discharge with reassurance", "Treat as asthma for months", "Order hearing test"], 0,
      "Radiolucent foreign bodies may produce a normal chest film; history and focal findings can justify bronchoscopy.",
      "The choking story is often more sensitive than the x-ray.",
      "What radiographic expiratory or decubitus findings may reveal air trapping?", "overnight_call"),

    Q("v140_ped_04", PED, "Pediatric Subglottic Stenosis",
      "A tracheostomy-dependent child with grade III subglottic stenosis is being considered for reconstruction. Which preoperative factor is essential?",
      ["Complete airway endoscopy assessing glottis, stenosis length, trachea and dynamic lesions before choosing reconstruction", "Stenosis grade alone determines the operation", "No swallow/neurologic assessment", "CT alone replaces endoscopy"], 0,
      "Successful airway reconstruction depends on the whole airway, vocal-fold mobility, pulmonary status, reflux/inflammation context and decannulation readiness—not a single grade.",
      "Never plan pediatric airway reconstruction from the subglottis alone.",
      "How does posterior glottic stenosis alter an LTR plan?", "OR_prep"),

    Q("v140_ped_05", PED, "Laryngotracheal Reconstruction",
      "During anterior cartilage-graft LTR, what is the structural purpose of the graft?",
      ["Expand and stabilize the cricoid/subglottic framework after splitting the stenotic segment", "Narrow the airway", "Paralyze the recurrent laryngeal nerves", "Close the tracheostomy permanently before testing the airway"], 0,
      "LTR enlarges a scarred cartilaginous framework; graft orientation, mucosal coverage, stenting and staging depend on the stenosis pattern.",
      "Cartilage is used as structural expansion, not as a patch over untreated scar alone.",
      "What donor sites are commonly used for pediatric airway cartilage grafts?", "OR_prep"),

    Q("v140_ped_06", PED, "Supraglottoplasty",
      "After supraglottoplasty for severe laryngomalacia, an infant has new coughing with feeds and oxygen desaturation. What is the best next step?",
      ["Assess for postoperative dysphagia/aspiration and airway edema rather than assuming the surgery failed", "Immediate repeat supraglottoplasty without evaluation", "Discharge", "Start solid food"], 0,
      "Transient dysphagia can occur after supraglottoplasty, especially in medically complex infants; evaluate swallowing and airway status when symptoms arise.",
      "Pediatric airway surgery can trade obstruction for temporary swallowing dysfunction—anticipate both systems.",
      "Which neurologic or syndromic comorbidities increase risk of persistent aspiration?", "postoperative_call"),

    Q("v140_ped_07", PED, "Pediatric OSA / Adenotonsillar Disease",
      "A child with severe OSA, obesity and trisomy 21 is scheduled for adenotonsillectomy. What disposition issue matters most?",
      ["Plan postoperative monitored observation because severe OSA and comorbidities increase respiratory risk", "Routine unmonitored discharge", "No anesthesia planning needed", "OSA severity does not affect postoperative risk"], 0,
      "High-risk pediatric OSA patients can have postoperative obstruction and opioid sensitivity; disposition should reflect PSG severity, age and comorbidities.",
      "Adenotonsillectomy is common surgery, but severe OSA makes it high-acuity postoperative care.",
      "How should opioid-sparing analgesia be approached in severe OSA?", "OR_prep"),

    Q("v140_ped_08", PED, "Tympanostomy Tube Indications",
      "A child has recurrent AOM but no middle-ear effusion in either ear at the candidacy visit. What is the best recommendation?",
      ["Do not place tubes solely for recurrent AOM when no effusion is present at assessment", "Place tubes automatically", "Mastoidectomy", "Cochlear implant"], 0,
      "Current tube guidance distinguishes recurrent AOM with versus without effusion; the latter generally does not benefit from routine tube insertion.",
      "Verify the disease state on the day you decide to operate.",
      "How does persistent bilateral OME with hearing difficulty change the indication?", "boards"),

    Q("v140_ped_09", PED, "Pediatric Deep Neck Infection",
      "A 3-year-old with a retropharyngeal phlegmon is stable, moving the neck and has no airway symptoms. CT shows no mature abscess. What is a reasonable initial plan?",
      ["Admit for IV antibiotics and close airway/clinical observation, reserving drainage for deterioration or organized abscess", "Immediate open drainage in every case", "Discharge without antibiotics", "Tonsillectomy"], 0,
      "Selected stable pediatric deep-neck infections without a drainable collection can respond to IV antibiotics, but airway and progression must be watched closely.",
      "Not every CT low-density area is an abscess, and not every child needs immediate surgery.",
      "What clinical changes mandate repeat imaging or operative drainage?", "overnight_call"),

    Q("v140_ped_10", PED, "Choanal Atresia",
      "During endoscopic repair of bilateral choanal atresia, what is the key surgical objective?",
      ["Create a patent posterior nasal airway while preserving mucosa and minimizing restenosis", "Remove the entire posterior septum and turbinates indiscriminately", "Narrow the choana", "Avoid postoperative surveillance"], 0,
      "Endoscopic repair removes the atretic plate and enlarges the choana; mucosal preservation and postoperative care help limit restenosis.",
      "The long-term problem after technically successful repair is restenosis, so follow-up is part of the operation.",
      "When are stents considered, and why are they controversial?", "OR_prep"),
]
