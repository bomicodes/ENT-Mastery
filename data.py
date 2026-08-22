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
