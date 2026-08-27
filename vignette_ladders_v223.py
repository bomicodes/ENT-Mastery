"""v22.3 — Head & Neck Oncology learning-ladder pass 5.

Reviews five additional canonical topics: cutaneous SCC, BCC, melanoma, Merkel
cell carcinoma, and recurrent/metastatic HNSCC. Existing strong application
cases are reused where available; only missing layers are added.
"""
DOMAIN="Head & Neck Oncology"
REUSED={
    "v135_hn_03":("Cutaneous Squamous Cell Carcinoma of the Head & Neck","application"),
    "v143_hno_04":("Cutaneous Melanoma of the Head & Neck","application"),
}
REUSED_REASON_BY_CHOICE={
"v135_hn_03":{
"Tumor color":"Color is not a major staging determinant.",
"Clinical/radiographic perineural spread along a named nerve toward the skull base":"Correct. Named-nerve perineural spread substantially changes imaging, surgical extent, skull-base planning, and adjuvant radiation.",
"Mild actinic damage nearby":"Background actinic damage does not carry the same prognostic impact as named-nerve perineural spread.",
"A remote history of basal cell carcinoma":"A remote unrelated skin cancer does not define the extent of the current cSCC."},
"v143_hno_04":{
"Discuss sentinel lymph-node biopsy when indicated; head-and-neck lymphatic drainage can be complex and may involve parotid or multiple basins":"Correct. Sentinel-node mapping provides pathologic staging when indicated and is especially useful in the head and neck because drainage can be unpredictable.",
"Perform elective radical neck dissection for every melanoma":"Routine radical neck dissection is not appropriate for every clinically node-negative melanoma.",
"Ignore the neck because melanoma never spreads lymphatically":"Melanoma commonly spreads through lymphatics; nodal staging matters in appropriately selected tumors.",
"Use thyroidectomy for staging":"Thyroid surgery has no role in regional staging of cutaneous melanoma."}}

def _q(qid,topic,stage,stem,choices,answer,explanation,why_wrong,pearl,curveball,focus="boards"):
    return {"id":qid,"domain":DOMAIN,"topic":topic,"learning_stage":stage,"stem":stem,
            "choices":choices,"answer":answer,"explanation":explanation,"why_wrong":why_wrong,
            "board_pearl":pearl,"curveball":curveball,"tier":"Curated learning ladder",
            "mode":"Vignette","focus":focus,"ladder_reviewed":True}

VIGNETTES_V223=[
_q("v223_hn_cscc_fnd","Cutaneous Squamous Cell Carcinoma of the Head & Neck","foundation",
"Which feature most strongly marks a head-and-neck cutaneous SCC as high risk for recurrence or nodal spread?",
["Small well-differentiated lesion on a low-risk site","Clinical perineural symptoms, deep invasion, poor differentiation, recurrent disease, or other major high-risk features","Uniform tan color","Absence of sun exposure history"],1,
"Head-and-neck cSCC risk is driven by tumor size/depth, differentiation, recurrence, perineural invasion, immunosuppression, anatomic site, and other aggressive features rather than appearance alone.",
["A small low-risk lesion lacks the aggressive features in question.","Correct. High-risk pathology and clinical behavior drive staging, nodal evaluation, and adjuvant planning.","Color is not a major oncologic risk classifier.","Sun exposure history does not override tumor-specific adverse features."],
"In cSCC, cranial neuropathy is a staging clue until proven otherwise.","Which named nerves most commonly require skull-base imaging when symptoms suggest perineural spread?"),
_q("v223_hn_cscc_snr","Cutaneous Squamous Cell Carcinoma of the Head & Neck","senior_decision",
"A recurrent temple cSCC has gross perineural spread along V2 to the foramen rotundum, parotid nodal disease, and no distant metastasis. What is the best attending-level principle?",
["Treat only the skin primary","Plan multidisciplinary en bloc regional/skull-base management around the full extent of disease, including parotid/neck and named-nerve pathways, with adjuvant therapy as indicated","Observe because perineural spread is microscopic only","Perform cosmetic excision without margin planning"],1,
"Clinically evident named-nerve perineural spread and nodal disease convert a local skin cancer problem into a regional/skull-base oncologic problem. Surgery, radiation fields, nerve sacrifice/reconstruction, and neck/parotid management must be planned together.",
["Local treatment alone misses the major routes of spread.","Correct. The treatment field must match the actual disease map.","Gross radiographic perineural disease is not a microscopic incidental finding.","Cosmetic excision without oncologic planning risks inadequate disease control."],
"For advanced cSCC, treat the nerve and nodal basin as part of the cancer—not as separate complications.","How would unresectable proximal nerve extension change the role of radiation or systemic immunotherapy?","OR_prep"),

_q("v223_hn_bcc_fnd","Basal Cell Carcinoma of the Head & Neck","foundation",
"Which statement best distinguishes typical basal cell carcinoma from cutaneous SCC?",
["BCC commonly causes early nodal metastasis","BCC is primarily a locally destructive skin cancer; nodal or distant metastasis is rare","BCC arises from mucosal epithelium of the oropharynx","BCC is treated primarily with systemic antibiotics"],1,
"Most BCC behaves as a locally invasive cutaneous malignancy with very low metastatic potential. Morbidity arises from local destruction, recurrence, critical-site involvement, and difficult reconstruction.",
["Early nodal spread is not typical of BCC.","Correct. Local invasion is the major oncologic problem in most BCC.","BCC is a cutaneous rather than oropharyngeal mucosal malignancy.","Antibiotics do not treat BCC."],
"BCC rarely metastasizes, but a neglected facial BCC can still destroy eyelid, nose, ear, orbit, or skull base.","What histologic subtypes or clinical settings make recurrence more likely?"),
_q("v223_hn_bcc_app","Basal Cell Carcinoma of the Head & Neck","application",
"A recurrent infiltrative BCC involves the nasal ala and approaches the internal nasal lining. What is the best treatment principle?",
["Use margin-controlled oncologic excision and reconstruct skin, support, and lining according to the resulting defect","Ignore margins because metastasis is rare","Treat with topical antibiotics only","Perform elective neck dissection routinely"],0,
"High-risk facial BCC often benefits from margin-controlled excision. Reconstruction should be designed after oncologic clearance and must restore the layered nasal defect when skin, structural support, and lining are involved.",
["Correct. Clearance comes first, then defect-driven reconstruction.","Low metastatic risk does not make local margin control optional.","Topical antibiotics do not eradicate invasive BCC.","Routine elective neck dissection is not indicated for typical BCC."],
"For high-risk facial BCC, the reconstructive plan follows the oncologic defect—not the other way around.","When would a forehead flap or cartilage graft become necessary?","OR_prep"),
_q("v223_hn_bcc_snr","Basal Cell Carcinoma of the Head & Neck","senior_decision",
"A patient has multiply recurrent BCC of the medial canthus with orbital extension after several prior resections. What should the senior treatment discussion emphasize?",
["Another superficial shave excision","Define true orbital/skull-base extent and weigh curative surgery, radiation, and pathway-directed systemic therapy in a multidisciplinary setting","Assume all orbital symptoms are infection","Observe indefinitely because BCC never causes serious morbidity"],1,
"Locally advanced BCC can become surgically morbid despite its low metastatic rate. Imaging-defined extent, prior treatment, resectability, vision/orbit consequences, radiation options, and hedgehog-pathway or other systemic therapy all may influence management.",
["Superficial treatment is inadequate for deep recurrent disease.","Correct. Locally advanced BCC requires a broader oncologic strategy.","Tumor extension must be excluded before attributing orbital symptoms to infection.","Neglected locally invasive BCC can cause major functional loss."],
"Rare metastasis does not mean trivial disease; local anatomy can make BCC devastating.","What findings would make orbital exenteration enter the surgical discussion?"),

_q("v223_hn_mel_fnd","Cutaneous Melanoma of the Head & Neck","foundation",
"Which pathologic measurement is central to primary cutaneous melanoma staging and sentinel-node decision-making?",
["Breslow thickness","Tumor color only","Keratinization","Serum calcium"],0,
"Breslow thickness is a core staging variable in cutaneous melanoma and, together with ulceration and other factors, helps determine prognosis and whether sentinel lymph-node biopsy should be discussed.",
["Correct. Breslow depth is fundamental to melanoma staging.","Color alone does not stage melanoma.","Keratinization is relevant to squamous differentiation, not melanoma staging.","Serum calcium is unrelated to primary melanoma staging."],
"For melanoma, measure depth before you plan the nodal conversation.","How does ulceration modify stage and prognosis?"),
_q("v223_hn_mel_snr","Cutaneous Melanoma of the Head & Neck","senior_decision",
"A scalp melanoma maps to an intraparotid sentinel node that is positive. What is the best attending-level principle?",
["The result is irrelevant because parotid nodes do not count","Use the positive sentinel-node result for pathologic staging and multidisciplinary regional/systemic planning rather than automatically performing the same operation for every patient","Perform total laryngectomy","Ignore systemic therapy options"],1,
"A positive sentinel node establishes regional metastatic disease and changes stage and adjuvant discussions. Contemporary management is individualized by nodal burden, imaging, systemic therapy options, and basin-specific surgical morbidity rather than reflexively applying one historical operation to all patients.",
["Intraparotid nodes are true regional lymph nodes for many head-and-neck skin primaries.","Correct. The nodal result should drive risk-adapted multidisciplinary planning.","Laryngectomy is unrelated to scalp melanoma nodal disease.","Modern melanoma care commonly includes systemic therapy considerations."],
"In head-and-neck melanoma, the map may run through the parotid; regional treatment must follow the biology and basin.","What additional imaging or systemic staging is appropriate once regional nodal disease is identified?"),

_q("v223_hn_merkel_fnd","Merkel Cell Carcinoma","foundation",
"Which description best fits Merkel cell carcinoma?",
["An indolent keratin cyst","An aggressive neuroendocrine cutaneous carcinoma with substantial nodal and distant metastatic risk","A benign salivary tumor","A fungal skin infection"],1,
"Merkel cell carcinoma is an aggressive primary cutaneous neuroendocrine malignancy with a high propensity for regional nodal and distant spread, particularly in older or immunosuppressed patients.",
["Merkel cell carcinoma is malignant and aggressive, not a keratin cyst.","Correct. Regional and distant staging matter early.","It is a cutaneous neuroendocrine carcinoma, not a benign salivary neoplasm.","It is not an infectious process."],
"Merkel cell carcinoma behaves more aggressively than its often-small skin primary suggests.","What patient factors increase risk and how does immune suppression affect prognosis?"),
_q("v223_hn_merkel_app","Merkel Cell Carcinoma","application",
"A clinically node-negative patient has a newly diagnosed head-and-neck Merkel cell carcinoma. What regional-staging principle is most appropriate?",
["Ignore nodal staging because the primary is small","Consider sentinel lymph-node biopsy when feasible because occult nodal disease is common and can change treatment","Perform bilateral radical neck dissection in every case","Observe until a node becomes palpable"],1,
"Merkel cell carcinoma has a meaningful occult nodal risk. Sentinel-node staging can provide important prognostic and treatment information in clinically node-negative patients, though head-and-neck drainage can be complex.",
["Small primary size does not eliminate occult nodal risk.","Correct. Pathologic nodal staging often changes regional management.","Routine bilateral radical dissection is excessive.","Waiting for clinically apparent disease forfeits useful staging information."],
"For Merkel cell carcinoma, a clinically negative neck is not necessarily a pathologically negative neck.","How does a positive sentinel node alter regional radiation or surgery discussions?"),
_q("v223_hn_merkel_snr","Merkel Cell Carcinoma","senior_decision",
"A frail older patient has unresectable recurrent Merkel cell carcinoma with regional and distant disease. What is the best senior-level framework?",
["Pursue morbid local surgery regardless of systemic spread","Prioritize systemic immune-based therapy and symptom-directed local treatment within multidisciplinary goals-of-care planning","Use antibiotics alone","Observe without discussing prognosis"],1,
"Advanced Merkel cell carcinoma is often managed with immune checkpoint therapy when appropriate, with surgery or radiation used selectively for local control, palliation, or limited disease. Treatment intensity should reflect systemic extent, performance status, and patient goals.",
["Extensive distant disease can make highly morbid local surgery a poor tradeoff.","Correct. Systemic disease requires a systemic strategy plus selective local control.","Antibiotics do not treat Merkel cell carcinoma.","Prognosis and goals should be discussed explicitly."],
"Aggressive skin cancer still requires proportional treatment: control the disease that threatens the patient most.","When can radiation provide useful palliation even when cure is not realistic?"),

_q("v223_hn_rm_fnd","Recurrent / Metastatic HNSCC","foundation",
"A patient develops biopsy-proven recurrent HNSCC after prior definitive treatment. What is the first broad management question?",
["Is the recurrence isolated and potentially curable with salvage local therapy, or is disease unresectable/metastatic and better approached systemically?","Which antibiotic should be used?","Should all patients undergo laryngectomy?","Can surveillance be stopped?"],0,
"Recurrent HNSCC management begins by defining extent, resectability, prior treatment, performance status, and whether a realistic curative salvage option exists. That distinction separates local salvage pathways from systemic/palliative strategies.",
["Correct. The treatment intent must be established before selecting modality.","Antibiotics do not define cancer treatment strategy.","The salvage operation depends on site and extent.","Recurrence requires more, not less, structured surveillance and planning."],
"At recurrence, decide intent first: salvageable local disease and disseminated disease are different problems.","What imaging is most useful before committing to major salvage surgery?"),
_q("v223_hn_rm_app","Recurrent / Metastatic HNSCC","application",
"A patient has unresectable recurrent HNSCC with distant metastases and good performance status. What should guide first-line systemic treatment selection?",
["Tumor biomarkers, prior therapy, disease burden, symptoms, performance status, and current evidence-based systemic options including immunotherapy","Primary-site surgery regardless of metastases","Long-term antibiotics","Observation until airway obstruction"],0,
"Modern recurrent/metastatic HNSCC treatment is individualized using PD-L1-related biomarkers where relevant, prior platinum exposure, symptom burden, pace of disease, comorbidity, and suitability for immune checkpoint therapy with or without chemotherapy.",
["Correct. Systemic therapy selection is risk- and biomarker-informed.","Major local surgery does not control widespread metastatic disease by itself.","Antibiotics do not treat metastatic carcinoma.","Delay can allow avoidable symptom progression."],
"Recurrent/metastatic HNSCC is not one regimen for everyone; biology, prior therapy, and urgency matter.","How would rapidly progressive symptomatic disease influence the choice between immunotherapy alone and combination therapy?"),
_q("v223_hn_rm_snr","Recurrent / Metastatic HNSCC","senior_decision",
"A patient with metastatic HNSCC has progressive cachexia, poor performance status, repeated admissions, and limited likelihood of benefiting from further anticancer therapy. What is the best attending-level decision?",
["Continue toxic therapy because stopping is abandonment","Reassess goals, expected benefit, symptom burden, and hospice/palliative options while continuing active symptom control","Avoid discussing prognosis","Offer radical salvage surgery despite disseminated disease"],1,
"Senior oncologic decision-making includes recognizing when treatment burden exceeds realistic benefit. Early goals-of-care and palliative involvement can improve symptom control and align care with patient priorities without abandoning active management of pain, airway, nutrition, bleeding, or other symptoms.",
["Treatment without plausible benefit can increase harm.","Correct. Prognosis, values, and symptom priorities belong in the treatment plan.","Avoiding prognosis prevents informed decisions.","Disseminated disease generally cannot be cured by morbid local salvage surgery."],
"Knowing when not to escalate cancer-directed therapy is part of head-and-neck oncology expertise.","Which airway or bleeding symptoms still require urgent ENT intervention even in a comfort-focused plan?","overnight_call"),
]

def apply_learning_ladders_v223(challenges,item_id_fn):
    by_id={str(q.get("id")):q for q in challenges}
    touched=0
    for qid,(topic,stage) in REUSED.items():
        q=by_id.get(qid)
        if not q: raise RuntimeError("v223 missing reused case: "+qid)
        q["topic"]=topic; q["learning_stage"]=stage; q["ladder_reviewed"]=True
        q["concept_id"]=item_id_fn(DOMAIN,topic)
        mapping=REUSED_REASON_BY_CHOICE.get(qid,{})
        q["why_wrong"]=[mapping.get(choice,"Use the clinical mechanism and risk framework to distinguish this choice.") for choice in q.get("choices",[])]
        touched+=1
    existing={str(q.get("id")) for q in challenges}; added=0
    for q in VIGNETTES_V223:
        row=dict(q); row["concept_id"]=item_id_fn(DOMAIN,row["topic"])
        if not row["concept_id"]: raise RuntimeError("v223 orphan: "+row["topic"])
        if row["id"] not in existing:
            challenges.append(row); existing.add(row["id"]); added+=1
    return {"reused":touched,"added":added,"reviewed_topics":5}
