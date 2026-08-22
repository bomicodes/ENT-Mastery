DOMAINS = [
    {"id":"head-neck","name":"Head & Neck","icon":"🧬"},
    {"id":"otology","name":"Otology / Neurotology","icon":"👂"},
    {"id":"rhinology","name":"Rhinology / Skull Base","icon":"👃"},
    {"id":"laryngology","name":"Laryngology","icon":"🗣️"},
    {"id":"pediatrics","name":"Pediatric ENT","icon":"🧸"},
    {"id":"facial-plastics","name":"Facial Plastics / Reconstruction","icon":"🪡"},
    {"id":"sleep","name":"Sleep","icon":"🌙"},
    {"id":"general","name":"General / Trauma / Consults","icon":"🩺"},
]

PARATHYROID = {
 "slug":"parathyroid-disease",
 "title":"Parathyroid Disease",
 "domain":"Head & Neck",
 "subtitle":"Build a surgical mental model from embryology → calcium physiology → diagnosis → localization → operation → rescue.",
 "tags":["parathyroid","hyperparathyroidism","hypercalcemia","PTH","parathyroidectomy","endocrine","hungry bone","intraoperative PTH"],
 "one_minute":{
   "model":"PTH is the body's rapid defense against falling ionized calcium. Primary hyperparathyroidism is autonomous PTH secretion: calcium rises despite PTH that should be suppressed. Diagnosis is biochemical; imaging is for localization after the decision to operate.",
   "chain":[
      "Low ionized Ca²⁺ sensed by CaSR → ↑ PTH",
      "PTH → kidney retains calcium, wastes phosphate, activates vitamin D",
      "Calcitriol → increases intestinal calcium absorption",
      "PTH increases bone turnover through osteoblast-mediated RANKL signaling",
      "Autonomous gland(s) break the feedback loop → hypercalcemia + inappropriately high/normal PTH"
   ],
   "pearl":"The most useful board distinction: diagnosis tells you WHETHER disease is present; localization tells you WHERE to operate."
 },
 "sections":[
   {"id":"embryology","title":"Embryology: predict where the missing gland went","type":"mental_model",
    "badge":"STOP & RECALL",
    "recall_prompt":"Without looking: why are inferior parathyroids more variable than superior glands?",
    "recall_answer":"Inferior glands migrate farther with the thymus from the third pouch; superior glands arise from the fourth pouch and migrate less.",
    "content":[
      "Superior glands arise from the 4th pharyngeal pouch and have a shorter migration, so their location is more consistent.",
      "Inferior glands arise from the 3rd pouch with the thymus and migrate farther; this explains their wider positional variability and potential thymic/mediastinal location.",
      "Think migration path, not a memorized list: a missing inferior gland can lie along the thyrothymic tract or within thymic tissue."
    ],
    "why":[
      ["Why are inferior glands more variable?","They migrate farther with the thymus from the third pouch."],
      ["So what surgically?","If an inferior gland is missing, search the migration pathway—thyrothymic ligament, cervical thymus, and potentially mediastinum—rather than randomly exploring."]
    ]},
   {"id":"anatomy","title":"Surgical anatomy: a 3-D search strategy","type":"anatomy",
    "badge":"OR PEARL",
    "recall_prompt":"You cannot find the expected inferior gland. What migration pathway should guide your search?",
    "recall_answer":"Think lower pole/thyrothymic region \u2192 cervical thymus \u2192 mediastinal pathway when appropriate.",
    "content":[
      "Normal glands are usually posterior to the thyroid, but their relationship to the recurrent laryngeal nerve and embryologic migration pattern is more useful than memorizing a single coordinate.",
      "Superior glands are classically posterior and relatively fixed near the cricothyroid junction / posterior upper-to-mid thyroid region.",
      "Inferior glands are more variable and often associated with the lower pole, thyrothymic ligament, or thymus.",
      "Key danger structures during exploration include the recurrent laryngeal nerve, inferior thyroid arterial branches, esophagus, and thyroid capsule."
    ],
    "pearl":"Before chasing an ectopic gland, ask: superior or inferior embryology? Then search the expected migration pathway."},
   {"id":"physiology","title":"PTH / calcium physiology","type":"mental_model",
    "badge":"STOP & RECALL",
    "recall_prompt":"What are the three major target organs of PTH, and what does it do at each?",
    "recall_answer":"Kidney: retain calcium, waste phosphate, activate vitamin D. Bone: increase turnover. Gut: indirectly increase calcium absorption through calcitriol.",
    "content":[
      "PTH is secreted in response to low ionized calcium detected by the calcium-sensing receptor (CaSR).",
      "Kidney: increases distal calcium reabsorption, decreases proximal phosphate reabsorption, and stimulates 1α-hydroxylase → calcitriol.",
      "Bone: PTH acts on osteoblast-lineage cells, increasing RANKL and osteoclast activation; chronic excess raises bone turnover.",
      "The biochemical signature of primary hyperparathyroidism is hypercalcemia with PTH that is elevated or inappropriately non-suppressed."
    ]},
   {"id":"diagnosis","title":"Diagnosis: prove the physiology first","type":"decision",
    "badge":"BOARD",
    "recall_prompt":"Why can a 'normal' PTH still be abnormal in a hypercalcemic patient?",
    "recall_answer":"Because hypercalcemia should suppress PTH. A non-suppressed value is physiologically inappropriate.",
    "content":[
      "Confirm hypercalcemia (albumin-adjusted total calcium or ionized calcium when appropriate) and measure intact PTH.",
      "If calcium is high, PTH should be suppressed. A high or 'normal' PTH in that setting is inappropriate and points toward PTH-dependent hypercalcemia.",
      "Check renal function, 25-OH vitamin D, phosphorus, and urinary calcium when differentiating primary hyperparathyroidism from mimics such as familial hypocalciuric hypercalcemia (FHH).",
      "Do not use localization imaging to diagnose primary hyperparathyroidism."
    ],
    "pitfall":"A negative sestamibi scan does not rule out primary hyperparathyroidism."},
   {"id":"workup","title":"Workup: quantify end-organ impact","type":"workup",
    "badge":"GUIDELINE",
    "recall_prompt":"Before localization, what are the three questions your workup must answer?",
    "recall_answer":"Is this truly PHPT? Is there kidney/bone target-organ involvement? Does the patient meet an indication for surgery?",
    "content":[
      "Assess renal function and structural renal involvement. Renal imaging (commonly ultrasound as a radiation-free option; CT when clinically appropriate) looks for nephrolithiasis or nephrocalcinosis, including silent disease. A 24-hour urine calcium evaluates hypercalciuria and contributes to the PHPT vs FHH differential.",
      "Assess skeletal effects with DXA; the distal 1/3 radius matters because cortical bone may be prominently affected.",
      "Review medications and secondary causes that can distort calcium/PTH interpretation, including lithium, thiazides, chronic kidney disease, vitamin D deficiency, and malabsorption."
    ],
    "pearl":"Use the sequence: confirm the physiology → exclude important mimics → assess kidney/bone target-organ effects → decide whether surgery is indicated → then localize."},
   {"id":"indications","title":"When to operate: current framework","type":"practice_update",
    "badge":"GUIDELINE",
    "recall_prompt":"Name the major asymptomatic PHPT surgery buckets without looking.",
    "recall_answer":"Calcium severity, skeletal involvement, renal involvement, and age <50.",
    "content":[
      "Symptomatic primary hyperparathyroidism is a surgical disease in an appropriate operative candidate.",
      "For asymptomatic disease, the 2022 Fifth International Workshop recommends surgery when any one major criterion is met: serum calcium >1 mg/dL above the upper limit of normal; skeletal involvement (vertebral fracture or T-score ≤−2.5); renal involvement (eGFR/CrCl <60, nephrolithiasis/nephrocalcinosis, or hypercalciuria >250 mg/day in women or >300 mg/day in men); or age <50 years.",
      "Parathyroidectomy remains an option for patients who prefer definitive cure even when they do not meet a guideline threshold, assuming no contraindication and shared decision-making."
    ],
    "practice_update":"Older sources may quote >400 mg/day urinary calcium. The 2022 international workshop uses sex-specific thresholds (>250 mg/day women, >300 mg/day men) as a renal surgical criterion."},
   {"id":"localization","title":"Localization: plan the operation, don't make the diagnosis","type":"decision",
    "badge":"BOARD",
    "recall_prompt":"What is the one sentence distinction between diagnosis and localization?",
    "recall_answer":"Diagnosis proves the disease biochemically; localization helps plan where/how to operate.",
    "content":[
      "First-line localization commonly uses high-resolution neck ultrasound and sestamibi-based imaging.",
      "4D-CT can be especially useful for nonlocalizing, discordant, reoperative, or anatomically complex disease, balanced against radiation and contrast considerations.",
      "Concordant localization can support a focused/selective operation; nonlocalizing imaging does not eliminate the possibility of cure with bilateral exploration by an experienced surgeon."
    ]},
   {"id":"operation","title":"Focused vs bilateral exploration","type":"operative",
    "badge":"OR PEARL",
    "recall_prompt":"What finding would make you broaden from a focused operation to bilateral exploration?",
    "recall_answer":"Discordant/nonlocalizing studies, suspected multigland/hereditary disease, unexpected anatomy, or ioPTH inconsistent with cure.",
    "content":[
      "Focused/selective parathyroidectomy is attractive when biochemical disease is established and localization is convincing.",
      "Bilateral four-gland exploration remains important when imaging is nonlocalizing/discordant, multigland disease is suspected, familial syndromes are present, or intraoperative findings do not fit the preoperative hypothesis.",
      "The operation is a hypothesis test: localization predicts a gland; anatomy and intraoperative physiology tell you whether the hypothesis was correct."
    ]},
   {"id":"iopth","title":"Intraoperative PTH: physiology as navigation","type":"operative",
    "badge":"ATTENDING",
    "recall_prompt":"What are the first three categories when ioPTH fails to fall?",
    "recall_answer":"Sampling/timing issue, wrong tissue removed, or additional hyperfunctioning tissue.",
    "content":[
      "PTH has a short half-life, allowing intraoperative measurements to test whether the dominant hypersecreting tissue has been removed.",
      "A commonly used Miami-style criterion is a >50% fall from the highest pre-incision or pre-excision value at approximately 10 minutes after excision; local protocols vary.",
      "Failure to drop should trigger a structured response: confirm timing/sample validity, reconsider the removed tissue, consider additional hyperfunctioning glands, and continue exploration when appropriate."
    ],
    "pearl":"Pre-incision and pre-excision baselines protect against a misleading baseline caused by manipulation-induced PTH spikes."},
   {"id":"complications","title":"Complications: understand the mechanism","type":"complication",
    "badge":"EMERGENCY",
    "recall_prompt":"Expanding neck swelling with respiratory distress after endocrine neck surgery: what comes before imaging?",
    "recall_answer":"Airway rescue and immediate wound decompression when the airway is threatened.",
    "content":[
      "Neck hematoma: airway emergency—recognition and immediate decompression take priority over elegant diagnostics when the airway is threatened.",
      "RLN injury: prevention depends on disciplined anatomy and tissue handling; postoperative voice change deserves appropriate evaluation.",
      "Hypocalcemia can reflect transient hypoparathyroidism or hungry bone syndrome.",
      "Persistent hyperparathyroidism suggests disease never cured; recurrent disease means return of hypercalcemia after a period of documented cure."
    ]},
   {"id":"hungry-bone","title":"Hungry bone syndrome","type":"mental_model",
    "badge":"BOARD",
    "recall_prompt":"Explain hungry bone syndrome in one phrase.",
    "recall_answer":"After removal of chronic PTH drive, high-turnover bone becomes an avid calcium sink.",
    "content":[
      "Chronically PTH-stimulated bone has high turnover. After removal of the PTH drive, remineralization can become rapid and calcium fluxes from blood into bone.",
      "The result can be prolonged hypocalcemia, often with hypophosphatemia and hypomagnesemia, despite recovery/removal of the hyperfunctioning gland.",
      "Risk rises with more severe skeletal disease/high bone turnover. The mental model is 'bone suddenly becomes a calcium sink.'"
    ]},
 ],
 "sources":[
   {"name":"Cummings Otolaryngology—Head and Neck Surgery, 7th ed.","role":"Deep disease framework, anatomy, operative context"},
   {"name":"Pasha: Otolaryngology–Head and Neck Surgery Clinical Reference Guide, 6th ed.","role":"Board-focused synthesis; dedicated Parathyroids section"},
   {"name":"K.J. Lee's Essential Otolaryngology, 12th ed.","role":"Comprehensive second source; Thyroid and Parathyroid Glands chapter"},
   {"name":"Surgical Anatomy of the Head and Neck","role":"Surgical spatial relationships"},
   {"name":"Operative Otolaryngology—Head and Neck Surgery, 3rd ed.","role":"Operative technique"},
   {"name":"Fifth International Workshop on Primary Hyperparathyroidism (2022)","role":"Current evaluation and surgical-indication framework"},
 ]
}

QUESTIONS = [
 {"id":"q1","concept_id":"pth_feedback","topic":"parathyroid-disease","kind":"recall",
  "prompt":"A patient has hypercalcemia and a PTH within the laboratory 'normal' range. Why can this still indicate primary hyperparathyroidism?",
  "choices":["The PTH assay is always unreliable in hypercalcemia","PTH should be suppressed by hypercalcemia, so a normal value can be inappropriately non-suppressed","Primary hyperparathyroidism always produces normal PTH","Albumin raises PTH directly"],
  "answer":1,
  "explanation":"Hypercalcemia should suppress PTH. A PTH that remains measurable in the normal range can therefore be physiologically inappropriate and support PTH-dependent hypercalcemia.",
  "why_it_matters":"Calcium and PTH must be interpreted as a feedback pair. When calcium is high, a normal parathyroid gland should nearly shut PTH off. A laboratory-normal PTH is therefore physiologically abnormal when calcium is elevated.",
  "what_to_look_for":"Confirm the calcium abnormality and ask whether PTH is appropriately suppressed.",
  "management_change":"Suppressed PTH sends you toward non-PTH causes of hypercalcemia. Non-suppressed PTH keeps you in the PTH-dependent pathway: PHPT, FHH, medication effects, and selected renal/tertiary states.",
  "board_pearl":"Never interpret a PTH value without looking at the calcium beside it.",
  "attending_followup":"If calcium is 11.2 mg/dL and PTH is 42 pg/mL (normal 15\u201365), is the PTH normal?",
  "why_wrong":["Assay interference exists but is not the core physiology.","Correct.","PTH is often elevated, but the key is appropriateness for the calcium level.","Albumin affects interpretation of total calcium, not PTH secretion this way."]},
 {"id":"q2","concept_id":"inferior_embryology","topic":"parathyroid-disease","kind":"recall",
  "prompt":"Why are inferior parathyroid glands more variable in location than superior glands?",
  "choices":["They are larger","They migrate with the thymus from the third pharyngeal pouch","They arise from neural crest","They cross the carotid bifurcation during development"],
  "answer":1,"explanation":"Inferior glands share third-pouch origin and migration with the thymus. Their longer migration creates greater positional variability.",
  "why_wrong":["Size does not explain variability.","Correct.","Parathyroid epithelium derives from pharyngeal pouch endoderm.","That is not their developmental pathway."]},
 {"id":"q3","concept_id":"imaging_role","topic":"parathyroid-disease","kind":"board",
  "prompt":"A patient has repeatedly elevated calcium and inappropriately elevated PTH. Sestamibi is negative. What is the best interpretation?",
  "choices":["Primary hyperparathyroidism is excluded","Repeat sestamibi until positive before surgery","The biochemical diagnosis can still be valid; imaging is for localization, not diagnosis","This proves familial hypocalciuric hypercalcemia"],
  "answer":2,"explanation":"Primary hyperparathyroidism is a biochemical diagnosis. Localization studies plan an operation; negative imaging does not negate the diagnosis.",
  "why_wrong":["Negative localization does not exclude biochemical disease.","Repeated imaging is not required to validate the diagnosis.","Correct.","FHH requires biochemical/urinary context; a negative sestamibi does not prove it."]},
 {"id":"q4","concept_id":"surgery_criteria","topic":"parathyroid-disease","kind":"board",
  "prompt":"Which asymptomatic patient meets a 2022 Fifth International Workshop criterion for parathyroidectomy?",
  "choices":["Age 55 with Ca 0.4 mg/dL above ULN and normal kidneys/bone","Age 47 with otherwise mild disease","Age 63 with T-score −1.8","Age 68 with urine calcium 180 mg/day and no stones"],
  "answer":1,"explanation":"Age <50 years is by itself a recommended surgical criterion.",
  "why_wrong":["This alone does not meet the listed thresholds.","Correct.","The skeletal threshold is T-score ≤−2.5 or vertebral fracture.","This does not meet the sex-specific hypercalciuria threshold cited by the workshop."]},
 {"id":"q5","concept_id":"iopth","topic":"parathyroid-disease","kind":"operative",
  "prompt":"After removal of a localized adenoma, intraoperative PTH does not fall as expected. What is the best next mental model?",
  "choices":["The operation has failed and should always end","Assume the lab is wrong","Verify timing/sample validity, then consider remaining hyperfunctioning tissue and continue a structured exploration","Immediately perform thyroidectomy"],
  "answer":2,"explanation":"A failed PTH drop is new data. First verify the measurement, then reassess whether the culprit tissue was removed or whether multigland/ectopic disease remains.",
  "why_wrong":["A failed drop should trigger reassessment, not automatic termination.","Lab/sample issues are one possibility, not an assumption.","Correct.","Thyroidectomy is not the default response."]},
 {"id":"q6","concept_id":"hungry_bone","topic":"parathyroid-disease","kind":"mechanism",
  "prompt":"What is the best mental model for hungry bone syndrome after successful parathyroidectomy?",
  "choices":["The kidney suddenly excretes all calcium","Bone rapidly remineralizes and becomes a calcium sink after removal of chronic PTH drive","Calcitonin secretion stops","The removed gland releases stored calcium"],
  "answer":1,"explanation":"High-turnover bone can avidly take up calcium after the PTH stimulus disappears, producing prolonged postoperative hypocalcemia.",
  "why_wrong":["Renal calcium loss is not the central mechanism.","Correct.","Loss of calcitonin is not the mechanism.","Parathyroid tissue does not serve as a calcium reservoir."]},
 {"id":"q7","concept_id":"pth_renal","topic":"parathyroid-disease","kind":"recall",
  "prompt":"Which renal effect of PTH helps explain the typical phosphate pattern in primary hyperparathyroidism?",
  "choices":["Increased proximal phosphate reabsorption","Decreased proximal phosphate reabsorption","Blocked vitamin D activation","Decreased distal calcium reabsorption"],
  "answer":1,"explanation":"PTH causes phosphaturia by reducing proximal tubular phosphate reabsorption.",
  "why_wrong":["PTH does the opposite.","Correct.","PTH stimulates 1α-hydroxylase.","PTH increases renal calcium reabsorption."]},
 {"id":"q8","concept_id":"fhh","topic":"parathyroid-disease","kind":"case",
  "prompt":"Why is familial hypocalciuric hypercalcemia important to consider before parathyroidectomy?",
  "choices":["It is always malignant","Surgery usually does not correct the inherited calcium-sensing physiology","It causes severe hypocalcemia","It always localizes to four glands"],
  "answer":1,"explanation":"FHH is usually caused by altered calcium sensing; parathyroidectomy generally does not fix the underlying physiology and can lead to unnecessary surgery.",
  "why_wrong":["FHH is generally benign.","Correct.","FHH causes hypercalcemia.","Localization is not the defining issue."]},
]

CASES = [
 {"id":"case-phpt-1","topic":"parathyroid-disease","title":"The Incidental Calcium",
  "summary":"58-year-old with calcium 11.3 mg/dL found on routine labs.",
  "steps":[
   {"q":"What is your first physiologic branch point?","a":"Determine whether the hypercalcemia is PTH-dependent: measure intact PTH and confirm the calcium abnormality."},
   {"q":"PTH is 78 pg/mL (lab normal 15–65). What does that tell you?","a":"PTH is not suppressed despite hypercalcemia, strongly supporting PTH-dependent hypercalcemia."},
   {"q":"What should you evaluate before sending the patient for localization?","a":"Renal function, vitamin D, phosphorus, urinary calcium/FHH differential, skeletal status and renal stone involvement; confirm the diagnosis before localization."},
   {"q":"Ultrasound and sestamibi are negative. Does the diagnosis disappear?","a":"No. Primary hyperparathyroidism is biochemical. Imaging localizes disease for surgery."},
  ]},
 {"id":"case-phpt-2","topic":"parathyroid-disease","title":"PTH Won't Drop",
  "summary":"Focused parathyroidectomy for concordant left-inferior localization; intraoperative PTH remains elevated.",
  "steps":[
   {"q":"What are your immediate categories?","a":"Sampling/timing problem; wrong tissue removed; additional hyperfunctioning gland(s); ectopic disease; altered PTH kinetics/clinical context."},
   {"q":"Why might a pre-excision value exceed the pre-incision value?","a":"Manipulation of the gland can transiently release PTH, so the highest appropriate baseline may be used in a Miami-style interpretation."},
   {"q":"What does the anatomy tell you if an inferior gland is missing?","a":"Follow its third-pouch/thymic migration pathway: lower pole/thyrothymic region, cervical thymus, and potentially mediastinal sites."}
  ]},
]

OPERATIONS = [
 {"slug":"parathyroidectomy","title":"Parathyroidectomy","topic":"parathyroid-disease",
  "indications":"Biochemically confirmed primary hyperparathyroidism in an appropriate surgical candidate; apply symptom/end-organ/age criteria and shared decision-making.",
  "steps":[
   "Verify biochemical diagnosis and localization strategy before incision.",
   "Position with gentle neck extension; prep for possible broader exploration than the initial target.",
   "Enter the central neck through a low transverse incision; divide/raise subplatysmal planes as needed and separate strap musculature.",
   "Mobilize the thyroid strategically to expose the posterior capsule while respecting RLN and parathyroid vascular anatomy.",
   "Identify the candidate gland using expected embryologic/anatomic relationships rather than color alone.",
   "Control the gland's vascular pedicle close to the gland when feasible and remove without violating surrounding critical structures.",
   "Use intraoperative PTH if part of the operative strategy; interpret in context of the institution's protocol.",
   "If physiology/local findings do not confirm cure, broaden to a structured exploration rather than random searching.",
   "Achieve meticulous hemostasis; reassess the field and close."
  ],
  "danger":["Recurrent laryngeal nerve","Inferior thyroid arterial branches","Esophagus/trachea during deep exploration","Devascularization of normal parathyroid tissue","Neck hematoma"],
  "viva":[
    ["Why might you choose bilateral exploration despite a localized lesion?","Concern for multigland disease, discordant/nonlocalizing studies, hereditary disease, or intraoperative findings/PTH inconsistent with single-gland cure."],
    ["Where would you look for a missing inferior gland?","Along the third-pouch/thymic migration path: thyrothymic ligament/cervical thymus and, when appropriate, mediastinum."],
    ["What is the conceptual purpose of ioPTH?","It converts the operation into a physiologic test of whether the hypersecreting tissue has been adequately removed."]
  ]},
]

COMPLICATIONS = [
 {"slug":"post-thyroid-neck-hematoma","title":"Expanding neck hematoma after thyroid/parathyroid surgery",
  "prompt":"POD0: increasing neck pressure, swelling, dysphonia and respiratory distress.",
  "framework":["Recognize impending airway compromise","Call for help / airway and OR resources","Immediate wound decompression when airway is threatened—do not delay for imaging","Definitive hemostasis and airway management","Post-event review of bleeding source and prevention"]},
 {"slug":"hungry-bone","title":"Hungry bone syndrome",
  "prompt":"After parathyroidectomy: persistent symptomatic hypocalcemia in a patient with severe preoperative bone disease.",
  "framework":["Check calcium (preferably ionized when clinically appropriate), magnesium, phosphate and PTH context","Recognize high-turnover bone as a calcium sink","Replace calcium; active vitamin D is often required","Correct magnesium and monitor closely","Distinguish from permanent hypoparathyroidism using time course and biochemical context"]},
]

ANATOMY = [
 {"slug":"parathyroid-embryology","title":"Parathyroid embryology & migration","region":"Neck",
  "points":["Superior: 4th pouch → shorter migration → more consistent position",
            "Inferior: 3rd pouch + thymus → longer migration → more variable",
            "Use embryology to search for ectopic glands."]},
 {"slug":"recurrent-laryngeal-nerve","title":"Recurrent laryngeal nerve in endocrine surgery","region":"Neck",
  "points":["Course and branching are variable.","The nerve's relationship to the inferior thyroid artery is not perfectly constant.","Identify/protect according to operative exposure and local anatomy rather than relying on one memorized relation."]},
]

CHIEF_PROMPTS = [
 {"id":"chief1","topic":"parathyroid-disease","prompt":"Your PGY-2 asks: 'Why can't we just order a sestamibi scan first to see if the patient has hyperparathyroidism?'",
  "must":["biochemical diagnosis","localization","negative imaging"],
  "model":"Primary hyperparathyroidism is diagnosed biochemically. Imaging answers a different question: where the abnormal gland may be once surgery is being considered. A negative localization study therefore does not rule out the disease."},
 {"id":"chief2","topic":"parathyroid-disease","prompt":"Teach an intern in 30 seconds why an inferior parathyroid adenoma can be found in the thymus.",
  "must":["third pharyngeal pouch","thymus","migration"],
  "model":"Inferior parathyroids and the thymus both arise from the third pharyngeal pouch and descend together. Because the inferior glands travel farther than superior glands, they have more variable final positions and can remain associated with cervical or mediastinal thymic tissue."}
]

ATTENDING_PROMPTS = [
 ("Where do the inferior parathyroids come from?","Third pharyngeal pouch, migrating with the thymus."),
 ("Why does that matter in the OR?","Their longer migration produces wider positional variability and predicts ectopic sites."),
 ("Hypercalcemia with 'normal' PTH—why is that abnormal?","The PTH should be suppressed, so a normal result is inappropriately non-suppressed."),
 ("What is localization for?","Planning the operation after biochemical diagnosis, not establishing the diagnosis."),
 ("What does PTH do to phosphate in the kidney?","Decreases proximal phosphate reabsorption, causing phosphaturia."),
]

def search_index():
    rows = []
    rows.append({"type":"Topic","title":PARATHYROID["title"],"subtitle":PARATHYROID["subtitle"],"url":"/topic/parathyroid-disease",
                 "text":" ".join(PARATHYROID["tags"])+" "+PARATHYROID["subtitle"]})
    for s in PARATHYROID["sections"]:
        rows.append({"type":"Lesson","title":s["title"],"subtitle":PARATHYROID["title"],"url":f"/topic/parathyroid-disease#{s['id']}",
                     "text":s["title"]+" "+" ".join(s.get("content",[]))})
    for op in OPERATIONS:
        rows.append({"type":"Operation","title":op["title"],"subtitle":"Operative Mastery","url":f"/operate/{op['slug']}",
                     "text":op["title"]+" "+op["indications"]+" "+" ".join(op["steps"])})
    for a in ANATOMY:
        rows.append({"type":"Anatomy","title":a["title"],"subtitle":a["region"],"url":f"/anatomy#{a['slug']}",
                     "text":a["title"]+" "+" ".join(a["points"])})
    for c in CASES:
        rows.append({"type":"Case","title":c["title"],"subtitle":c["summary"],"url":f"/case/{c['id']}",
                     "text":c["title"]+" "+c["summary"]+" "+" ".join(x["q"]+" "+x["a"] for x in c["steps"])})
    for c in COMPLICATIONS:
        rows.append({"type":"Complication","title":c["title"],"subtitle":c["prompt"],"url":f"/complications#{c['slug']}",
                     "text":c["title"]+" "+c["prompt"]+" "+" ".join(c["framework"])})
    return rows


# Otoscopy Interpretation Lab — source: Sanna et al., Color Atlas of Otoscopy (1999).
# Management pearls here intentionally stay close to the atlas; current practice should be
# cross-checked against contemporary guidelines as ENT Mastery adds newer sources.
OTOSCOPY_CASES = [
 {"id":"oto_normal_1","level":1,"image":"otoscopy/normal_tm.jpg","source":"Atlas p. 5 (PDF p. 12), Fig. 2.4","prompt":"Start with description only. What do you see?","findings":["Intact tympanic membrane","Visible malleus/umbo and cone of light","No obvious middle-ear opacity, perforation, or retraction"],"diagnosis":"Normal tympanic membrane","differential":"The task here is recognition of normal anatomy before disease labeling.","management":"No pathology is identified in this image.","pearl":"Build your normal template first: canal → pars flaccida → malleus/umbo → pars tensa → middle-ear clues.","followup":"Which landmarks help you orient right versus left ear?"},
 {"id":"oto_exostosis","level":2,"image":"otoscopy/exostosis.jpg","source":"Atlas p. 7 (PDF p. 14), Fig. 3.1","prompt":"Describe the canal lesion before naming it.","findings":["Smooth bony-appearing prominence from the EAC wall","Tympanic membrane remains partly visible","Additional smaller bony prominence may be present"],"diagnosis":"External auditory canal exostosis","differential":"Osteoma is the key visual differential. The atlas describes exostoses as commonly multiple, bilateral, and sessile, whereas osteoma is usually unilateral and pedunculated.","management":"The atlas reserves surgery for obstructing disease associated with hearing loss or recurrent otitis externa/debris retention.","pearl":"Multiple + broad-based/sessile should push you toward exostoses; a solitary pedunculated lesion favors osteoma.","followup":"What structures are at risk during canalplasty?"},
 {"id":"oto_osteoma","level":3,"image":"otoscopy/osteoma.jpg","source":"Atlas p. 8 (PDF p. 15), Fig. 3.3","prompt":"What feature makes this lesion favor osteoma over exostosis?","findings":["Solitary smooth osseous EAC lesion","Narrow/pedunculated attachment","Otherwise visible tympanic membrane"],"diagnosis":"External auditory canal osteoma","differential":"Exostosis is the main alternative; the atlas emphasizes the pedunculated narrow base here as favoring osteoma.","management":"The atlas notes removal can be performed with a curette; recurrent lesions may require wider removal around the base.","pearl":"Do not call every bony canal lesion an exostosis—look at number, laterality, and the base.","followup":"How would history of cold-water exposure change your pretest probability?"},
 {"id":"oto_furuncle","level":2,"image":"otoscopy/furuncle.jpg","source":"Atlas p. 10 (PDF p. 17), Fig. 3.9","prompt":"Localize the abnormality: canal, tympanic membrane, or middle ear?","findings":["Focal tender-appearing swelling of the cartilaginous EAC","Near-occlusion of the meatus","Central necrotic/pustular focus"],"diagnosis":"Furunculosis of the external auditory canal","differential":"Diffuse otitis externa is less focal; an EAC mass should prompt a broader differential when the appearance or course is atypical.","management":"The atlas identifies this as staphylococcal folliculitis; treatment details should be checked against current practice.","pearl":"Localization is the first win: this is a focal canal process, not primary middle-ear disease.","followup":"Why is furunculosis typically so painful?"},
 {"id":"oto_acute_myringitis","level":2,"image":"otoscopy/acute_myringitis.jpg","source":"Atlas p. 10 (PDF p. 17), Fig. 3.10","prompt":"Describe the tympanic membrane and adjacent canal.","findings":["Thickened hyperemic tympanic membrane","Hyperemia of adjacent EAC skin","Tympanic membrane appears lateralized"],"diagnosis":"Acute myringitis","differential":"The atlas notes acute myringitis can accompany external- or middle-ear infection, so the rest of the ear exam matters.","management":"The atlas discusses antimicrobial/local therapy; use contemporary guidance for present-day treatment decisions.","pearl":"Hyperemia alone is weak. Describe thickness, position, landmarks, canal findings, and middle-ear clues.","followup":"What additional finding would make you more confident there is concomitant acute otitis media?"},
 {"id":"oto_bullous","level":3,"image":"otoscopy/bullous_myringitis.jpg","source":"Atlas p. 11 (PDF p. 18), Fig. 3.11","prompt":"What is the defining visual abnormality?","findings":["Large fluid-filled bulla on the tympanic membrane","Smaller additional bulla posteriorly","Inflamed tympanic membrane"],"diagnosis":"Bullous myringitis","differential":"Distinguish true bullae of the tympanic membrane from canal lesions or middle-ear fluid seen through an intact membrane.","management":"The atlas associates this with upper respiratory infection and describes medical treatment; current treatment should be verified with contemporary sources.","pearl":"Name the finding before the disease: 'bullae on the tympanic membrane' makes the diagnosis much harder to miss.","followup":"Where within the tympanic membrane does the atlas state these bullae form?"},
 {"id":"oto_granulomatous","level":4,"image":"otoscopy/granulomatous_myringitis.jpg","source":"Atlas p. 11 (PDF p. 18), Fig. 3.13","prompt":"What tissue has replaced the normal epithelial surface?","findings":["Granulation tissue over the tympanic membrane","Extension onto adjacent anterior EAC skin","Loss of the normal smooth epithelial surface"],"diagnosis":"Granulomatous myringitis","differential":"Persistent granulation should not be treated as a visual diagnosis alone if the clinical course is atypical; the atlas repeatedly emphasizes integrating the whole clinical picture.","management":"The atlas describes removal of granulation tissue and topical therapy, with canalplasty/skin grafting for refractory stenotic disease.","pearl":"Ask whether granulation is a diagnosis or a sign. Persistent or atypical granulation may demand a broader workup.","followup":"What chronic structural complication can develop medially in the EAC?"},
 {"id":"oto_otomycosis","level":3,"image":"otoscopy/otomycosis.jpg","source":"Atlas p. 14 (PDF p. 21), Fig. 3.23","prompt":"Describe the debris. What diagnosis does its appearance suggest?","findings":["Black-speckled fungal-appearing debris","Keratin/debris within a chronically abnormal ear","Irregular inflamed canal/cavity surface"],"diagnosis":"Otomycosis (fungal superinfection)","differential":"The atlas notes Aspergillus and Candida species and emphasizes chronic otorrhea/debris as local risk factors.","management":"The atlas emphasizes cleaning/debridement before topical antifungal treatment.","pearl":"In otology, debris is information: color, texture, location, and what lies underneath all matter.","followup":"What patient and local factors does the atlas associate with otomycosis?"},
 {"id":"oto_eczema","level":3,"image":"otoscopy/eczema.jpg","source":"Atlas p. 15 (PDF p. 22), Fig. 3.25","prompt":"Is the primary abnormality in the canal skin or middle ear?","findings":["Squamous debris coating EAC skin","Dermatitis-like canal surface","Tympanic membrane is not the primary lesion"],"diagnosis":"Chronic eczema of the external auditory canal","differential":"Otomycosis and other causes of chronic otitis externa can also produce debris; morphology and history help separate them.","management":"The atlas emphasizes removal of an offending irritant when present and topical anti-inflammatory treatment.","pearl":"Itch + canal skin disease should pull your localization outward before you anchor on otitis media.","followup":"What history would you ask for to identify a local irritant or contact trigger?"},
 {"id":"oto_eac_chol","level":5,"image":"otoscopy/eac_cholesteatoma.jpg","source":"Atlas p. 15 (PDF p. 22), Fig. 3.26","prompt":"This white canal mass is not simply cerumen. Build the differential.","findings":["Focal white keratinous mass in the EAC","Surrounding debris/inflammation","Mass appears localized rather than diffuse"],"diagnosis":"External auditory canal cholesteatoma","differential":"The atlas contrasts EAC cholesteatoma with exostosis and keratosis obturans: cholesteatoma is described as soft/tender and often unilateral in older patients; exostosis is bony; keratosis obturans tends to be bilateral in younger patients.","management":"The atlas notes that EAC cholesteatoma may require removal of involved bone and reconstruction depending on extent.","pearl":"A white canal mass is a differential, not a diagnosis. Ask: bone or keratin? focal or circumferential? unilateral or bilateral? erosion or no erosion?","followup":"What imaging finding would make EAC cholesteatoma more convincing?"}
]



INTERPRETATION_LABS = {
 "audiology": {
   "title":"Audiology Lab","icon":"🎧","subtitle":"Read the test systematically, localize the lesion, then decide what the result changes.",
   "framework":["Reliability","Right vs left","Air conduction","Bone conduction / air-bone gap","Degree + configuration","Symmetry","Speech testing","Tympanometry / reflexes","Localization","Next step"],
   "source_note":"Synthetic audiograms in ENT Mastery are generated for practice; use ASHA/clinical audiology references for standardized symbols and your institutional standards for clinical decisions.",
   "resources":[
     {"name":"Practical Audiology for Otorhinolaryngologists","url":"https://audiology.medlogicai.org/","note":"ENT-oriented audiology teaching and cases"},
     {"name":"ASHA — Audiometric Symbols","url":"https://www.asha.org/policy/gl1990-00006/","note":"Standard audiometric notation"}
   ],
   "cases":[
     {"id":"aud1","level":1,"visual":"lab_assets/audio_normal.svg","prompt":"Interpret this audiogram in one sentence before revealing.","answer":"Hearing thresholds are essentially within normal limits bilaterally with no meaningful asymmetry.","why":"Always establish a normal template before trying to recognize disease.","follow":"What additional information would you want before calling a complete audiologic evaluation normal?"},
     {"id":"aud2","level":2,"visual":"lab_assets/audio_conductive.svg","prompt":"Where is the lesion localized by the air-bone relationship?","answer":"There is an air-bone gap with relatively preserved bone thresholds, consistent with conductive hearing loss.","why":"An air-bone gap means the cochlea can detect sound better through bone than the external/middle-ear pathway can deliver it.","follow":"Which tympanogram patterns could accompany conductive hearing loss, and how would each alter your differential?"},
     {"id":"aud3","level":3,"visual":"lab_assets/audio_snhl.svg","prompt":"Describe type, configuration, and symmetry.","answer":"Bilateral sloping high-frequency sensorineural hearing loss without a major air-bone gap.","why":"Air and bone thresholds fall together when the deficit is sensorineural.","follow":"What speech-discrimination pattern would make you worry about pathology beyond typical cochlear loss?"},
     {"id":"aud4","level":4,"visual":"lab_assets/audio_asym.svg","prompt":"What is the clinically important feature here?","answer":"Asymmetric sensorineural hearing loss, worse on the left, particularly at higher frequencies.","why":"Asymmetry changes the workup because retrocochlear pathology enters the differential.","follow":"What other audiologic and clinical findings would increase your concern for a retrocochlear lesion?"}
   ]
 },
 "pathology": {
   "title":"Head & Neck Pathology Lab","icon":"🔬","subtitle":"Low power → architecture → cells → diagnosis → marker → what the ENT surgeon needs to know.",
   "framework":["Site / specimen","Low-power architecture","High-power cytology","Keratinization / differentiation","Key differential","IHC / molecular clue","Diagnosis","Margin / PNI / LVI / nodal implication","Clinical consequence"],
   "source_note":"ENT Mastery links to open-access pathology collections rather than mirroring their images. This keeps the original attribution and interactive whole-slide viewers intact.",
   "resources":[
     {"name":"Ottawa Atlas of Pathology — Head & Neck","url":"https://www.pathologyatlas.ca/galleries/head-and-neck/","note":"Open-access gross and microscopic H&N pathology images"},
     {"name":"Juan Rosai Collection — Head & Neck","url":"https://rosaicollection.net/collection/headneck/?context=link","note":"Virtual slides and historical teaching cases"},
     {"name":"UPMC Digital Slide Viewer — Head & Neck","url":"https://image.upmc.edu/UPMC-Pathology-Center-of-Excellence/Head%20and%20Neck/view.apml","note":"Whole-slide teaching collection"}
   ],
   "cases":[
     {"id":"path1","level":1,"external":"https://www.pathologyatlas.ca/galleries/head-and-neck/","prompt":"Open the Oral Cavity gallery and choose a conventional squamous cell carcinoma image. Describe before diagnosing.","answer":"Look for invasive nests/cords of atypical squamous cells, variable keratinization and stromal invasion. Then connect grade, depth/invasion, PNI/LVI and margins to surgical implications.","why":"For ENT, the pathology task is not merely naming SCC; it is extracting features that change staging, adjuvant therapy, and re-resection decisions.","follow":"Which pathology report elements most directly change postoperative treatment planning?"},
     {"id":"path2","level":2,"external":"https://www.pathologyatlas.ca/galleries/head-and-neck/salivary-glands/","prompt":"Choose a salivary-gland case. First decide: biphasic? cystic? cribriform? mucinous? high-grade?","answer":"Use architecture first to narrow the salivary differential before reaching for immunostains or molecular labels.","why":"Salivary tumors are easier to retain when organized by architecture and cell type rather than memorized as a list.","follow":"Which salivary malignancy makes perineural invasion especially important to look for?"},
     {"id":"path3","level":3,"external":"https://rosaicollection.net/collection/headneck/?context=link","prompt":"Choose an inverted papilloma or salivary case from the virtual-slide list and explain the low-power architecture aloud.","answer":"The goal is localization and architecture before cytology: where does it arise, how does it grow, and is the border pushing, endophytic, or frankly invasive?","why":"Board questions often give you one hallmark, but operative pathology requires a mental model of the whole lesion.","follow":"Why does the diagnosis of inverted papilloma matter to the surgeon beyond benign vs malignant?"}
   ]
 },
 "ct-mri": {
   "title":"CT / MRI Lab","icon":"🧠","subtitle":"Orient → localize by space → describe → differential → extract the surgical map.",
   "framework":["Modality / sequence","Laterality","Anatomic space","Epicenter","Enhancement / density / signal","Bone change","Perineural / vascular / skull-base spread","Nodes","Differential","What changes the operation?"],
   "source_note":"The schematic orientation image is generated by ENT Mastery. Use the linked Open Anatomy atlases for real labeled cross-sectional anatomy.",
   "resources":[
     {"name":"Open Anatomy — SPL Head & Neck CT Atlas","url":"https://www.openanatomy.org/atlas-pages/atlas-spl-head-and-neck.html","note":"Open CT-based labeled head-and-neck anatomy"},
     {"name":"Open Anatomy — SPL Inner Ear Atlas","url":"https://www.openanatomy.org/atlas-pages/","note":"High-resolution CT inner-ear atlas"},
     {"name":"Learn Neuroradiology — Head & Neck","url":"https://learnneuroradiology.com/headneck/board-review-cases-head-and-neck/","note":"Image-first head-and-neck teaching cases"}
   ],
   "cases":[
     {"id":"ct1","level":1,"visual":"lab_assets/ct_orientation.svg","prompt":"Before pathology: orient yourself. What are your fixed anchors on an axial neck CT?","answer":"Airway, vertebral body/prevertebral muscles, carotid spaces, major glands, visceral compartment and fascial spaces. Exact landmarks depend on level.","why":"Space localization dramatically narrows the differential before you describe signal or enhancement.","follow":"If a mass displaces the carotid artery and internal jugular vein together, what does that tell you about its likely compartment?"},
     {"id":"ct2","level":3,"external":"https://www.openanatomy.org/atlas-pages/atlas-spl-head-and-neck.html","prompt":"Launch the real CT atlas. Pick one axial level and identify airway, carotid/jugular, SCM, thyroid/glandular tissue and vertebral column without labels.","answer":"Repeat until the unlabeled anatomy is automatic. Then add the surgical question: which structure would be encountered first from your planned approach?","why":"A radiology finding becomes surgically useful only when you can translate it into 3-D relationships.","follow":"What five imaging findings would you want explicitly described before operating on a deep neck-space mass?"},
     {"id":"ct3","level":4,"external":"https://learnneuroradiology.com/headneck/board-review-cases-head-and-neck/","prompt":"Choose a H&N board case. Commit to the anatomic space before reading the diagnosis.","answer":"Use epicenter and displacement pattern first, then lesion characteristics. Do not begin with a memorized tumor name.","why":"Localization by space is the reusable mental model across dozens of head-and-neck lesions.","follow":"What imaging feature would make perineural spread clinically important to your operative plan?"}
   ]
 },
 "laryngeal-endoscopy": {
   "title":"Laryngeal Endoscopy & Stroboscopy Lab","icon":"🎥","subtitle":"Describe motion and mucosal behavior before naming the lesion.",
   "framework":["Anatomic site","Laterality","Gross lesion","Vocal-fold mobility","Glottic closure","Mucosal wave","Amplitude","Periodicity / symmetry","Supraglottic compression","Diagnosis / next step"],
   "tracks":[
     {"id":"normal","name":"Normal Physiology"},
     {"id":"benign","name":"Benign Lesions"},
     {"id":"neuro","name":"Neurolaryngology"},
     {"id":"malignant","name":"Premalignant / Malignant"},
     {"id":"peds","name":"Pediatric"}
   ],
   "source_note":"ENT Mastery does not copy or re-host Stroboscopy.org videos. It sends you to the free atlas and wraps the viewing experience with our own interpretation prompts, active recall, and teaching questions.",
   "resources":[
     {"name":"Stroboscopy.org — Free Video Atlas","url":"https://stroboscopy.org/video-atlas/","note":"External atlas; use their videos on their site"},
     {"name":"Stroboscopy.org — Self Assessment","url":"https://stroboscopy.org/","note":"External self-assessment / video flashcards"}
   ],
   "cases":[
     {"id":"endo1","track":"normal","level":1,"external":"https://stroboscopy.org/video-atlas/","prompt":"Open a normal stroboscopy example. Narrate mobility, closure, wave, amplitude and symmetry aloud.","answer":"Build the normal motion template first; otherwise pathology labels become memorization without physiology.","why":"Stroboscopy is a dynamic test. The key information is how the cover vibrates, not just what the fold looks like in a still frame.","follow":"What is the difference between vocal-fold mobility and mucosal wave?"},
     {"id":"endo2","track":"benign","level":2,"external":"https://stroboscopy.org/video-atlas/","prompt":"Choose a benign phonotraumatic lesion. Describe whether the mucosal wave is preserved, reduced, absent, or asymmetric before reading the diagnosis.","answer":"Use lesion depth and effect on the superficial lamina propria to reason about the wave rather than memorizing one appearance.","why":"The wave helps distinguish superficial cover abnormalities from lesions that tether deeper layers.","follow":"Which finding would make you worry that a lesion is more deeply infiltrative?"},
     {"id":"endo3","track":"neuro","level":4,"external":"https://stroboscopy.org/video-atlas/","prompt":"Choose a paresis/paralysis example. Separate position, motion, closure pattern and compensatory supraglottic behavior.","answer":"A motion disorder should be described anatomically and functionally before deciding etiology or treatment.","why":"The same symptom—dysphonia—can arise from impaired motion, closure, vibration, or compensation.","follow":"What features might help distinguish paresis from mechanical fixation, and what additional workup could be needed?"},
     {"id":"endo4","track":"malignant","level":4,"external":"https://stroboscopy.org/video-atlas/","prompt":"Choose a leukoplakia/dysplasia or carcinoma example. Focus first on the mucosal wave and depth behavior, not the label.","answer":"Preserved wave may suggest a more superficial process, whereas focal stiffness or absent wave raises concern for deeper involvement; no single stroboscopic sign alone rules cancer in or out.","why":"The strobe adds functional information about lesion depth and pliability that complements the visual surface appearance.","follow":"Does preserved mucosal wave exclude invasive carcinoma? Why not?"},
     {"id":"endo5","track":"peds","level":3,"external":"https://stroboscopy.org/video-atlas/","prompt":"Choose a pediatric laryngeal example. First identify the anatomic level and motion abnormality before diagnosing.","answer":"Pediatric endoscopy still begins with localization: supraglottis, glottis, subglottis, then dynamic motion and airway effect.","why":"The same noisy breathing symptom can come from different levels and mechanisms.","follow":"What findings would help you distinguish dynamic supraglottic collapse from fixed subglottic narrowing?"}
   ]
 },

 "sinonasal-endoscopy": {
   "title":"Sinonasal Endoscopy & FESS Navigation Lab","icon":"👃","subtitle":"Endoscopic view ↔ CT location ↔ surgical landmark ↔ danger structure.",
   "framework":["Orientation","Septum / floor","Inferior turbinate / meatus","Middle turbinate","Middle meatus / OMC","Uncinate / bulla","Basal lamella","Superior turbinate / sphenoethmoidal recess","Skull base / orbit","What happens if you go too far?"],
   "tracks":[
     {"id":"normal","name":"Normal Endoscopy"},
     {"id":"inflammatory","name":"Inflammatory Disease"},
     {"id":"postop","name":"Post-FESS Anatomy"},
     {"id":"surgical","name":"FESS Navigation"},
     {"id":"masses","name":"Masses / Skull Base"}
   ],
   "source_note":"ENT Mastery links to University of Iowa endoscopy/FESS teaching pages and uses original schematic training visuals. It does not copy their videos or images.",
   "resources":[
     {"name":"University of Iowa — Medical Management of Sinusitis / Endoscopic Exam","url":"https://iowaprotocols.medicine.uiowa.edu/protocols/medical-management-sinusitis","note":"Systematic nasal endoscopy examination"},
     {"name":"University of Iowa — Endoscopic Sinus Surgery","url":"https://iowaprotocols.medicine.uiowa.edu/protocols/endoscopic-sinus-surgery","note":"FESS concepts and surgical landmarks"},
     {"name":"Open Anatomy — Head & Neck CT Atlas","url":"https://www.openanatomy.org/atlas-pages/atlas-spl-head-and-neck.html","note":"Cross-sectional CT anatomy for view-to-CT correlation"}
   ],
   "cases":[
     {"id":"sinus1","track":"normal","level":1,"visual":"lab_assets/sinonasal_orientation.svg","prompt":"Trace the normal endoscopic route from anterior nose to sphenoethmoidal recess. What structures should you expect in sequence?","answer":"Orient to septum and floor, identify inferior turbinate/meatus, then middle turbinate and middle meatus, and finally superior turbinate/sphenoethmoidal recess and nasopharynx depending on the pass.","why":"If normal orientation is automatic, pathology and postoperative anatomy become much easier to localize.","follow":"Which turbinate is your most important constant landmark during routine FESS?"},
     {"id":"sinus2","track":"surgical","level":2,"visual":"lab_assets/uncinate_to_bulla.svg","prompt":"You have just completed uncinectomy. What structure or space are you trying to expose next, and what are your lateral and superior danger boundaries?","answer":"You are opening access to the natural maxillary ostium/infundibular region and anterior ethmoid pathway. The orbit/lamina papyracea is lateral; the skull base becomes the superior danger boundary as dissection proceeds.","why":"FESS safety is about maintaining constant awareness of the orbit laterally and skull base superiorly while using reproducible landmarks.","follow":"Why is blindly following an accessory maxillary ostium dangerous as a substitute for finding the natural ostium?"},
     {"id":"sinus3","track":"surgical","level":3,"visual":"lab_assets/basal_lamella.svg","prompt":"What is the basal lamella telling you during ethmoidectomy?","answer":"It is the key landmark separating anterior from posterior ethmoid compartments and marks the transition deeper toward the posterior ethmoid/sphenoid region.","why":"The basal lamella is a navigation checkpoint: crossing it changes your compartment and therefore your relationship to skull base, orbit and sphenoid.","follow":"What should happen to your mental CT map before you cross the basal lamella?"},
     {"id":"sinus4","track":"surgical","level":4,"external":"https://www.openanatomy.org/atlas-pages/atlas-spl-head-and-neck.html","prompt":"Open the CT atlas. Find the same surgical level you are imagining endoscopically and identify orbit, skull base, middle turbinate region and sphenoid. Then explain the 3-D relationship aloud.","answer":"The goal is not one exact slice; it is being able to translate a coronal/axial CT location into the endoscopic direction of travel and the nearest danger structures.","why":"CT and endoscopy are two views of the same 3-D anatomy. Linking them reduces memorization and improves operative spatial reasoning.","follow":"Which preoperative CT variants would make you slow down before frontal recess or posterior ethmoid work?"},
     {"id":"sinus5","track":"inflammatory","level":2,"prompt":"Purulence is seen draining from the middle meatus. What does that localize, and what does it not prove?","answer":"It localizes disease to drainage pathways associated with the anterior sinus system/OMC region, but it does not by itself identify the exact sinus or establish chronicity/etiology.","why":"Endoscopy gives an anatomic clue, not a complete diagnosis. The history and CT may still be required.","follow":"How would purulence from the sphenoethmoidal recess change your localization?"},
     {"id":"sinus6","track":"masses","level":4,"prompt":"A unilateral friable nasal mass is encountered endoscopically. What is the safe mental sequence before biopsy?","answer":"Localize the attachment/site, assess vascular appearance and skull-base relationship, review imaging when appropriate, then decide whether office biopsy is safe or whether a controlled setting is needed.","why":"Not every nasal mass should be biopsied reflexively in clinic; vascular or skull-base lesions can make that hazardous.","follow":"What imaging or clinical features would make you worry about a vascular lesion such as JNA?"}
   ]
 },

 "airway-bronchoscopy": {
   "title":"Airway & Bronchoscopy Lab","icon":"🫁","subtitle":"Travel the airway level by level, describe the lesion, then decide whether it is dynamic, fixed, focal, long-segment, or reconstructive.",
   "framework":["Supraglottis","Glottis","Posterior glottis","Subglottis","Cricoid","Cervical trachea","Thoracic trachea","Carina","Mainstem bronchi","Dynamic vs fixed","Length / grade / maturity","Endoscopic vs open treatment"],
   "tracks":[
     {"id":"normal","name":"Normal Airway"},
     {"id":"stenosis","name":"Stenosis / Reconstruction"},
     {"id":"dynamic","name":"Dynamic Collapse"},
     {"id":"peds","name":"Pediatric Airway"},
     {"id":"foreign","name":"Foreign Body / Mass"}
   ],
   "source_note":"ENT Mastery links to University of Iowa airway/bronchoscopy protocols and uses original schematic training visuals. The goal is to learn a reusable airway description framework rather than memorize one disease photo.",
   "resources":[
     {"name":"University of Iowa — Adult Flexible Bronchoscopy","url":"https://iowaprotocols.medicine.uiowa.edu/protocols/adult-flexible-bronchoscopy","note":"Flexible bronchoscopy workflow"},
     {"name":"University of Iowa — Airway / Laryngotracheal Procedures","url":"https://iowaprotocols.medicine.uiowa.edu/protocols/protocols","note":"Airway, stenosis, reconstruction and operative protocols"}
   ],
   "cases":[
     {"id":"air1","track":"normal","level":1,"visual":"lab_assets/airway_journey.svg","prompt":"Name the airway levels in order from supraglottis to mainstem bronchi.","answer":"Supraglottis → glottis → posterior glottis → subglottis/cricoid → cervical trachea → thoracic trachea → carina → mainstem bronchi.","why":"A stenosis diagnosis is meaningless until you can say exactly where the abnormal segment begins and ends.","follow":"Which airway levels are complete cartilaginous rings and why does that matter surgically?"},
     {"id":"air2","track":"stenosis","level":2,"visual":"lab_assets/sgs_framework.svg","prompt":"Describe this subglottic stenosis using a surgeon's framework rather than only a Cotton-Myer grade.","answer":"State level, length, percent/grade, concentric vs eccentric morphology, mature scar vs inflamed tissue, posterior involvement, glottic involvement, tracheal extension and previous reconstruction history.","why":"Cotton-Myer grade compresses a complex 3-D lesion into one number and does not tell you whether endoscopic or open reconstruction is appropriate.","follow":"What features make you less enthusiastic about repeated endoscopic dilation?"},
     {"id":"air3","track":"stenosis","level":3,"prompt":"A short, soft, early subglottic stenosis is compared with a long, mature, circumferential scar involving the cricoid. Why should treatment differ?","answer":"The first lesion is more amenable to endoscopic management; the second has greater structural scar burden and may require open reconstruction depending on patient factors and prior treatment.","why":"Treatment follows lesion biology and geometry, not grade alone.","follow":"How do posterior glottic involvement and vocal-fold mobility change reconstructive planning?"},
     {"id":"air4","track":"dynamic","level":3,"visual":"lab_assets/dynamic_airway.svg","prompt":"How do you distinguish tracheomalacia/bronchomalacia from fixed stenosis endoscopically?","answer":"Dynamic collapse changes with respiration and pressure, whereas fixed stenosis remains structurally narrowed. The location, phase of collapse and extent should be documented.","why":"Dynamic disease is a mechanics problem; fixed stenosis is a structural lumen problem. They require different treatment thinking.","follow":"Why can positive pressure dramatically change the appearance of malacia during bronchoscopy?"},
     {"id":"air5","track":"peds","level":3,"prompt":"A child has biphasic stridor. Why is that symptom alone insufficient to call the lesion 'subglottic stenosis'?","answer":"Biphasic stridor suggests a fixed central airway lesion but does not precisely identify the level or cause. Endoscopic localization is still required.","why":"Symptoms localize broadly; endoscopy defines the actual anatomy and mechanism.","follow":"What endoscopic findings would distinguish subglottic cyst, hemangioma, and cicatricial stenosis?"},
     {"id":"air6","track":"foreign","level":4,"prompt":"During bronchoscopy for suspected foreign body, what must you describe besides 'foreign body present'?","answer":"Side, exact bronchial level, degree of obstruction, mucosal edema/granulation, distal secretions/atelectatic context, object shape/orientation and extraction hazards.","why":"The procedure plan depends on geometry, airway effect and distal consequences—not just the label.","follow":"What features make an airway foreign body extraction especially high risk?"}
   ]
 },
 "sleep": {
   "title":"Sleep / PSG Lab","icon":"🌙","subtitle":"Pediatric and adult PSG interpretation, OSA treatment selection, DISE, and hypoglossal nerve stimulation.",
   "framework":["Study quality","Sleep time / architecture","Obstructive vs central burden","Oxygenation","Ventilation / CO₂","Position / REM effects","Severity","Anatomic phenotype","Treatment selection","What changes for ENT?"],
   "tracks":[
     {"id":"pediatric","name":"Pediatric PSG"},
     {"id":"adult","name":"Adult PSG"},
     {"id":"hns","name":"HNS / DISE"}
   ],
   "source_note":"Synthetic PSG and HNS cases are for learning. Device candidacy, payer criteria, scoring definitions, and institutional pathways can change; ENT Mastery flags current FDA/device criteria separately from older historical thresholds.",
   "resources":[
     {"name":"AASM Education","url":"https://learn.aasm.org/","note":"Sleep scoring and interpretation education"},
     {"name":"AAO-HNS — Treatment of OSA","url":"https://www.entnet.org/resource/position-statement-treatment-of-obstructive-sleep-apnea/","note":"Adult/pediatric ENT treatment framework"},
     {"name":"AAO-HNS — Hypoglossal Nerve Stimulation","url":"https://www.entnet.org/resource/position-statement-hypoglossal-nerve-stimulation-for-treatment-of-obstructive-sleep-apnea-osa/","note":"HNS as second-line therapy for selected PAP-intolerant adults"},
     {"name":"FDA — Inspire UAS","url":"https://www.fda.gov/medical-devices/recently-approved-devices/inspire-upper-airway-stimulation-p130008s090","note":"Current FDA indication summary"}
   ],
   "practice_update":"Current Inspire labeling includes moderate-to-severe OSA with AHI 15–100, PAP failure/intolerance, and absence of complete concentric collapse at the soft palate. Central + mixed apneas should be <25% of the total AHI. BMI >40 has limited safety/effectiveness data; insurance criteria may be narrower than FDA labeling.",
   "cases":[
     {"id":"sleep1","track":"pediatric","level":2,"visual":"lab_assets/sleep_psg.svg","prompt":"Interpret the pediatric report systematically. Do not jump straight to the OAHI.","answer":"The synthetic study shows clinically meaningful obstructive sleep-disordered breathing with desaturation; central events are low and peak CO₂ shown here does not by itself establish hypoventilation. Integrate age, symptoms, comorbidities and current pediatric criteria.","why":"OAHI is important, but oxygenation, ventilation, arousals, sleep time and comorbid risk determine the real clinical picture.","follow":"Which PSG findings and patient factors would change your postoperative monitoring plan after adenotonsillectomy?"},
     {"id":"sleep2","track":"pediatric","level":3,"prompt":"A child has frequent respiratory events but many are central rather than obstructive. What is your first conceptual move?","answer":"Separate central from obstructive physiology before attributing the study to adenotonsillar obstruction. Central-predominant disease changes the differential and often the referral/workup pathway.","why":"ENT surgery treats anatomic obstruction; it does not solve every elevated apnea index.","follow":"What clinical histories would make central events more concerning?"},
     {"id":"sleep3","track":"pediatric","level":4,"prompt":"Why should CO₂ be reviewed even when oxygen saturation looks acceptable?","answer":"Ventilation and oxygenation are different physiologic variables. A patient can retain CO₂ without dramatic desaturation, particularly in sleep-related hypoventilation patterns.","why":"Reading only the O₂ nadir can miss clinically important ventilatory disease.","follow":"How would suspected hypoventilation alter your preoperative evaluation and perioperative planning?"},
     {"id":"sleepA1","track":"adult","level":2,"visual":"lab_assets/adult_psg_moderate.svg","prompt":"Interpret this adult PSG in one sentence, then list the pieces of the report that matter beyond the AHI.","answer":"This synthetic study shows moderate, predominantly obstructive OSA with meaningful desaturation and a low central-event burden. Also inspect positional/REM dependence, sleep time, arousals, oxygen burden, comorbidities and PAP history.","why":"Two adults with the same AHI can have very different physiology, symptoms, cardiovascular risk and surgical options.","follow":"What parts of this PSG would you specifically need before discussing hypoglossal nerve stimulation?"},
     {"id":"sleepA2","track":"adult","level":3,"visual":"lab_assets/adult_positional.svg","prompt":"The overall AHI is elevated, but nearly all events occur supine. What treatment implication should you recognize?","answer":"This is a strongly positional phenotype in the synthetic case. Positional therapy may be clinically relevant, and anatomy/PAP tolerance still determine whether other treatment is appropriate.","why":"Overall AHI can hide a mechanistic phenotype. Position, REM, and event type help explain why the patient obstructs.","follow":"How would a non-supine AHI near normal change your counseling compared with severe non-positional OSA?"},
     {"id":"sleepA3","track":"adult","level":4,"visual":"lab_assets/adult_central.svg","prompt":"Why is this study a poor HNS pattern despite a high total AHI?","answer":"A large fraction of events are central/mixed rather than obstructive. HNS is designed to treat upper-airway obstruction, not central respiratory-control failure.","why":"For HNS, total AHI is not enough—you need to know what fraction is actually obstructive.","follow":"What threshold for central + mixed events is important in current Inspire labeling?"},
     {"id":"hns1","track":"hns","level":2,"visual":"lab_assets/hns_pathway.svg","prompt":"Walk through HNS candidacy in the correct order. Do not start with DISE.","answer":"Confirm clinically significant predominantly obstructive OSA → document PAP failure/intolerance → review AHI and central/mixed burden → consider BMI/device/payer limits and anatomy → perform DISE to assess collapse pattern, especially the palate → discuss alternatives and patient goals.","why":"DISE is not a substitute for PSG or PAP history; it answers the anatomic-phenotype question after the physiologic candidacy is established.","follow":"Why does complete concentric collapse at the soft palate matter?"},
     {"id":"hns2","track":"hns","level":3,"prompt":"Adult with AHI 38, PAP intolerance, central + mixed events 8% of AHI, BMI 31. DISE shows complete concentric palatal collapse. Candidate for Inspire under current labeling?","answer":"No. Complete concentric collapse at the soft palate is a key exclusion for Inspire UAS despite otherwise favorable PSG/PAP features.","why":"HNS advances/stiffens tongue-related airway mechanics; a concentric palatal collapse phenotype predicts poor response to this therapy.","follow":"What alternative anatomic or non-anatomic treatments would you consider based on the patient's phenotype?"},
     {"id":"hns3","track":"hns","level":3,"prompt":"Adult with AHI 72 and BMI 35 is told they are automatically outside FDA labeling because 'Inspire only goes to AHI 65 and BMI 32.' What is outdated in that statement?","answer":"The FDA indication was expanded: AHI can be up to 100, and the BMI warning/data boundary was expanded to 40. Coverage policies may still be more restrictive, so FDA labeling and payer criteria must be separated.","why":"This is exactly why ENT Mastery should date-stamp device criteria instead of teaching old STAR-trial thresholds forever.","follow":"What other PSG and DISE features still have to be checked even if AHI and BMI fall within current labeling?"},
     {"id":"hns4","track":"hns","level":4,"visual":"lab_assets/hns_response.svg","prompt":"Post-implant follow-up shows AHI improvement from 42 to 17 but persistent symptoms. Is this simply 'device failure'?","answer":"Not necessarily. First characterize residual events: obstructive vs central, positional/REM pattern, oxygen burden, adherence/usage, stimulation settings, tongue motion, anatomy and possible residual collapse at other levels.","why":"HNS response is a physiology-and-anatomy troubleshooting problem, not a binary implant success/failure label.","follow":"What would you want from a titration study or repeat sleep evaluation before deciding on revision or adjunctive treatment?"},
     {"id":"hns5","track":"hns","level":5,"prompt":"Why should you separate FDA labeling, clinical evidence, and insurance criteria when teaching HNS candidacy?","answer":"They answer different questions. FDA labeling defines approved use; evidence describes expected outcomes and uncertainty; insurers may impose narrower coverage rules. A patient may fit the label yet not fit a payer policy or may require individualized clinical judgment.","why":"Device eligibility is a moving target. Teaching one memorized BMI/AHI cutoff creates outdated practice knowledge.","follow":"How would you explain this distinction to a junior resident presenting an HNS candidate?"}
   ]
 },
 "vestibular": {
   "title":"Vestibular Lab","icon":"🌀","subtitle":"Ask what each test interrogates, at what frequency, and how the pattern localizes.",
   "framework":["Symptom / timing","Spontaneous nystagmus","Oculomotor testing","Positional testing","Calorics","vHIT","VEMP","Central vs peripheral pattern","Localization","Next step"],
   "source_note":"Synthetic traces are for teaching physiology. Use current laboratory norms because thresholds and protocols vary by equipment and center.",
   "resources":[
     {"name":"Vestibular Disorders Association — Diagnosis / Testing","url":"https://vestibular.org/article/diagnosis-treatment/diagnosis/","note":"Overview of vestibular testing"},
     {"name":"MUSC — Introduction to Vestibular Testing","url":"https://medicine.musc.edu/-/sm/medicine/education/cme/current/handouts/2025-vestibular/cassels_introduction-to-vestibular-testing.pdf","note":"VNG, calorics, rotary chair, vHIT and VEMP teaching"}
   ],
   "cases":[
     {"id":"vest1","level":2,"visual":"lab_assets/vest_caloric.svg","prompt":"Do not calculate first. Which ear appears weaker by inspection?","answer":"The left warm/cool responses are smaller overall than the right in this synthetic example, suggesting a left-sided caloric weakness pattern. Apply your lab's validated formula/norms for the actual numeric interpretation.","why":"Calorics test each horizontal-canal/superior-vestibular-nerve pathway independently at a very low-frequency stimulus.","follow":"Why can calorics be abnormal while vHIT is normal?"},
     {"id":"vest2","level":3,"visual":"lab_assets/vest_vhit.svg","prompt":"Which canal pathway is abnormal in this synthetic vHIT plot?","answer":"The left horizontal canal has reduced gain in this example; in real testing, also inspect overt/covert corrective saccades and lab-specific norms.","why":"vHIT interrogates high-frequency vestibulo-ocular reflex function, complementing rather than duplicating calorics.","follow":"What does a corrective saccade mean physiologically?"},
     {"id":"vest3","level":3,"prompt":"Dix-Hallpike produces a transient torsional upbeating nystagmus after a short latency. What mental model should fire?","answer":"A canal-specific positional peripheral pattern—classically posterior-canal BPPV—should be considered, while confirming that the direction, latency, duration and fatigability fit.","why":"The geometry of the nystagmus is the output of the stimulated canal/extraocular-muscle pathways.","follow":"How would horizontal-canal BPPV look different on positional testing?"},
     {"id":"vest4","level":4,"prompt":"Abnormal smooth pursuit and direction-changing gaze-evoked nystagmus appear on VNG. Why should that change your localization?","answer":"Oculomotor abnormalities can signal central pathology rather than an isolated peripheral labyrinthine lesion, depending on medications, vision, age and test quality.","why":"VNG includes tests that interrogate central ocular-motor networks, not just the labyrinth.","follow":"What clinical red flags would make you escalate to neurologic imaging/workup?"}
   ]
 }
}
