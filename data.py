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
  "Attending Follow-Up":[
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


# Otoscopy Interpretation Atlas — source: Sanna et al., Color Atlas of Otoscopy (1999).
# Management pearls here intentionally stay close to the atlas; current practice should be
# cross-checked against contemporary guidelines as ENT Mastery adds newer sources.
OTOSCOPY_CASES = [{'id': 'oto_normal_1',
  'level': 1,
  'image': 'otoscopy/normal_tm.jpg',
  'source': 'Atlas p. 5 (PDF p. 12), Fig. 2.4',
  'prompt': 'Start with description only. What do you see?',
  'findings': ['Intact tympanic membrane',
               'Visible malleus/umbo and cone of light',
               'No obvious middle-ear opacity, perforation, or retraction'],
  'diagnosis': 'Normal tympanic membrane',
  'differential': 'The task here is recognition of normal anatomy before disease labeling.',
  'management': 'No treatment is needed for a normal tympanic membrane. Use the normal card as the baseline for later '
                'comparisons: intact landmarks, normal position/translucency, and no middle-ear effusion or canal disease.',
  'pearl': 'Build your normal template first: canal → pars flaccida → malleus/umbo → pars tensa → middle-ear clues.',
  'followup': 'Which landmarks help you orient right versus left ear?',
  'management_considerations': 'If symptoms are present despite a normal otoscopic appearance, do not force an otoscopic '
                               'diagnosis—localize with history, audiometry/tympanometry, vestibular testing, or imaging as '
                               'clinically indicated.',
  'source_note': 'Atlas baseline anatomy; management is symptom-driven when otoscopy is normal.',
  'visual_strategy': 'Atlas foundation + contemporary normal reference',
  'external_visuals': [{'label': 'Contemporary normal TM reference',
                        'source': 'Merck Manual Professional — Normal Tympanic Membrane',
                        'url': 'https://www.merckmanuals.com/professional/multimedia/image/normal-tympanic-membrane',
                        'why': 'Useful modern reference for pearly color and distinct normal landmarks.',
                        'type': 'normal reference'}],
  'visual_pearl': 'Use this as your visual zero point: before diagnosing pathology, compare color, position, translucency, '
                  'landmarks, and canal appearance with a normal ear.'},
 {'id': 'oto_exostosis',
  'level': 2,
  'image': 'otoscopy/exostosis.jpg',
  'source': 'Atlas p. 7 (PDF p. 14), Fig. 3.1',
  'prompt': 'Describe the canal lesion before naming it.',
  'findings': ['Smooth bony-appearing prominence from the EAC wall',
               'Tympanic membrane remains partly visible',
               'Additional smaller bony prominence may be present'],
  'diagnosis': 'External auditory canal exostosis',
  'differential': 'Osteoma is the key visual differential. The atlas describes exostoses as commonly multiple, bilateral, '
                  'and sessile, whereas osteoma is usually unilateral and pedunculated.',
  'management': 'Observe asymptomatic exostoses. Treat associated cerumen/debris retention or otitis externa as needed. '
                'Consider canalplasty/exostectomy when obstruction causes clinically important conductive hearing loss, '
                'recurrent infections, trapped debris, or prevents adequate examination/treatment of the medial canal or '
                'tympanic membrane.',
  'pearl': 'Multiple + broad-based/sessile should push you toward exostoses; a solitary pedunculated lesion favors osteoma.',
  'followup': 'What structures are at risk during canalplasty?',
  'management_considerations': 'Exostoses are typically broad-based, often multiple/bilateral, and associated with '
                               'cold-water exposure. Surgery is symptom/functional driven—not simply because exostoses are '
                               'visible.',
  'source_note': 'Cross-referenced with the Otoscopy Atlas and Essential Otolaryngology.',
  'visual_strategy': 'Atlas remains primary',
  'external_visuals': [],
  'visual_pearl': 'The atlas image is still highly useful here. Focus on broad-based, often multiple smooth bony '
                  'prominences rather than image age.',
  'look_alike': 'Osteoma: usually solitary, unilateral, and pedunculated rather than multiple/broad-based.'},
 {'id': 'oto_osteoma',
  'level': 3,
  'image': 'otoscopy/osteoma.jpg',
  'source': 'Atlas p. 8 (PDF p. 15), Fig. 3.3',
  'prompt': 'What feature makes this lesion favor osteoma over exostosis?',
  'findings': ['Solitary smooth osseous EAC lesion',
               'Narrow/pedunculated attachment',
               'Otherwise visible tympanic membrane'],
  'diagnosis': 'External auditory canal osteoma',
  'differential': 'Exostosis is the main alternative; the atlas emphasizes the pedunculated narrow base here as favoring '
                  'osteoma.',
  'management': 'Observe an asymptomatic EAC osteoma. Excise when it causes obstruction, conductive hearing loss, recurrent '
                'infection/debris trapping, or interferes with canal access. A small pedunculated lesion may be removed at '
                'its stalk/base; recurrent or broad disease requires adequate removal of the attachment while protecting '
                'canal skin and nearby structures.',
  'pearl': 'Do not call every bony canal lesion an exostosis—look at number, laterality, and the base.',
  'followup': 'How would history of cold-water exposure change your pretest probability?',
  'management_considerations': 'Unlike exostoses, osteomas are classically solitary, unilateral, and pedunculated. The '
                               'indication for surgery is symptoms or functional obstruction, not the diagnosis alone.',
  'source_note': 'Cross-referenced with the Otoscopy Atlas and Essential Otolaryngology.',
  'visual_strategy': 'Atlas remains primary',
  'external_visuals': [],
  'visual_pearl': 'The most important visual discriminator is the attachment: classically a solitary pedunculated lesion.',
  'look_alike': 'Exostoses: generally multiple/bilateral and broad-based.'},
 {'id': 'oto_furuncle',
  'level': 2,
  'image': 'otoscopy/furuncle.jpg',
  'source': 'Atlas p. 10 (PDF p. 17), Fig. 3.9',
  'prompt': 'Localize the abnormality: canal, tympanic membrane, or middle ear?',
  'findings': ['Focal tender-appearing swelling of the cartilaginous EAC',
               'Near-occlusion of the meatus',
               'Central necrotic/pustular focus'],
  'diagnosis': 'Furunculosis of the external auditory canal',
  'differential': 'Diffuse otitis externa is less focal; an EAC mass should prompt a broader differential when the '
                  'appearance or course is atypical.',
  'management': 'Treat this as a localized staphylococcal infection of a hair follicle in the cartilaginous EAC. Provide '
                'analgesia and warm compresses. Small furuncles may drain spontaneously; a large/fluctuant furuncle or '
                'formed abscess should be incised and drained when safely accessible. Culture purulent material when an '
                'abscess is drained, particularly for recurrent disease or when resistance is a concern. Systemic '
                'antistaphylococcal antibiotics are not automatically required after adequate drainage; add them for '
                'systemic illness, surrounding cellulitis/extension, markedly impaired host defenses, multiple/recurrent '
                'lesions, failure of drainage alone, or other high-risk features. Choose MSSA vs MRSA coverage using local '
                'resistance patterns and patient risk factors.',
  'pearl': 'Localization is the first win: this is a focal canal process, not primary middle-ear disease.',
  'followup': 'Why is furunculosis typically so painful?',
  'management_considerations': 'Do not confuse focal furunculosis with diffuse acute otitis externa: furunculosis is a '
                               'focal painful swelling in the hair-bearing lateral/cartilaginous canal, often with '
                               'little/no otorrhea. Diabetes/immunocompromise lowers the threshold for closer evaluation. '
                               'Recurrent S. aureus abscesses should be cultured; selected recurrent cases may warrant a '
                               'decolonization strategy. Reassess worsening, recurrent, or unresolved disease rather than '
                               'repeatedly prescribing empiric drops.',
  'source_note': 'Atlas: staphylococcal folliculitis. Bluestone & Stool: antistaphylococcal therapy for localized disease '
                 'and I&D when abscess develops. Current IDSA purulent-SSTI guidance emphasizes drainage for large '
                 'furuncles/abscesses and reserves adjunct systemic antibiotics for systemic/high-risk disease.',
  'visual_strategy': 'Atlas classic + contemporary phenotype',
  'external_visuals': [{'label': 'Contemporary furuncle example',
                        'source': 'Merck Manual Professional — Otitis Externa with Furuncle',
                        'url': 'https://www.merckmanuals.com/professional/multimedia/image/otitis-externa-with-furuncle',
                        'why': 'Shows a focal erythematous furuncle in an inflamed canal; useful for comparing focal '
                               'disease with diffuse AOE.',
                        'type': 'contemporary clinical image'},
                       {'label': 'Current external-otitis review',
                        'source': 'Merck Manual Professional — External Otitis (reviewed May 2026)',
                        'url': 'https://www.merckmanuals.com/professional/ear-nose-and-throat-disorders/external-ear-disorders/external-otitis-acute',
                        'why': 'Pairs the image with current clinical description: focal painful erythematous swelling, '
                               'sometimes with sanguineous/purulent drainage.',
                        'type': 'current review'}],
  'visual_pearl': 'Furunculosis should look focal. A discrete painful swelling in the hair-bearing lateral canal is a '
                  'different visual pattern from circumferential diffuse canal edema.',
  'look_alike': 'Diffuse acute otitis externa: more generalized canal erythema/edema and debris rather than one focal '
                'follicular swelling.'},
 {'id': 'oto_acute_myringitis',
  'level': 2,
  'image': 'otoscopy/acute_myringitis.jpg',
  'source': 'Atlas p. 10 (PDF p. 17), Fig. 3.10',
  'prompt': 'Describe the tympanic membrane and adjacent canal.',
  'findings': ['Thickened hyperemic tympanic membrane',
               'Hyperemia of adjacent EAC skin',
               'Tympanic membrane appears lateralized'],
  'diagnosis': 'Acute myringitis',
  'differential': 'The atlas notes acute myringitis can accompany external- or middle-ear infection, so the rest of the ear '
                  'exam matters.',
  'management': 'Treat the underlying infectious context rather than the red tympanic membrane in isolation. Determine '
                'whether this is associated with acute otitis media, diffuse otitis externa, or isolated myringitis; '
                'provide analgesia and use antimicrobial therapy appropriate to the associated diagnosis. Avoid assuming '
                'that every erythematous TM requires systemic antibiotics.',
  'pearl': 'Hyperemia alone is weak. Describe thickness, position, landmarks, canal findings, and middle-ear clues.',
  'followup': 'What additional finding would make you more confident there is concomitant acute otitis media?',
  'management_considerations': 'The atlas describes general/local antibiotics and local steroid therapy, but contemporary '
                               'management should be diagnosis-specific. Confirm middle-ear effusion/bulging if diagnosing '
                               'AOM and assess canal inflammation if diagnosing AOE.',
  'source_note': 'Atlas describes acute myringitis as commonly accompanying external- or middle-ear infection; contemporary '
                 'treatment is anchored to the associated disease.',
  'visual_strategy': 'Atlas remains primary; management modernized',
  'external_visuals': [],
  'visual_pearl': 'Do not diagnose from redness alone. Ask whether the TM is merely hyperemic or whether there is true '
                  'middle-ear effusion/bulging or associated canal disease.',
  'look_alike': 'Acute otitis media and diffuse otitis externa can both produce an erythematous TM.'},
 {'id': 'oto_bullous',
  'level': 3,
  'image': 'otoscopy/bullous_myringitis.jpg',
  'source': 'Atlas p. 11 (PDF p. 18), Fig. 3.11',
  'prompt': 'What is the defining visual abnormality?',
  'findings': ['Large fluid-filled bulla on the tympanic membrane',
               'Smaller additional bulla posteriorly',
               'Inflamed tympanic membrane'],
  'diagnosis': 'Bullous myringitis',
  'differential': 'Distinguish true bullae of the tympanic membrane from canal lesions or middle-ear fluid seen through an '
                  'intact membrane.',
  'management': 'Prioritize pain control. Bullous myringitis is generally managed using the same antimicrobial decision '
                'framework as acute otitis media when middle-ear infection is present; the presence of bullae alone does '
                "not establish a separate 'Mycoplasma' treatment pathway. Drainage/incision of a very painful bulla can "
                'provide relief in selected cases.',
  'pearl': "Name the finding before the disease: 'bullae on the tympanic membrane' makes the diagnosis much harder to miss.",
  'followup': 'Where within the tympanic membrane does the atlas state these bullae form?',
  'management_considerations': 'Look for concomitant AOM and document hearing symptoms. The pediatric textbook notes '
                               'typical bacterial AOM organisms and does not support the older Mycoplasma theory.',
  'source_note': "Cross-referenced with Bluestone & Stool's discussion of myringitis; treatment should follow current AOM "
                 'principles when AOM is present.',
  'visual_strategy': 'Atlas remains primary',
  'external_visuals': [],
  'visual_pearl': 'The key visual finding is one or more bullae on the tympanic membrane; then determine whether '
                  'concomitant middle-ear infection is present.',
  'look_alike': 'Simple acute myringitis lacks the discrete blister/bulla morphology.'},
 {'id': 'oto_granulomatous',
  'level': 4,
  'image': 'otoscopy/granulomatous_myringitis.jpg',
  'source': 'Atlas p. 11 (PDF p. 18), Fig. 3.13',
  'prompt': 'What tissue has replaced the normal epithelial surface?',
  'findings': ['Granulation tissue over the tympanic membrane',
               'Extension onto adjacent anterior EAC skin',
               'Loss of the normal smooth epithelial surface'],
  'diagnosis': 'Granulomatous myringitis',
  'differential': 'Persistent granulation should not be treated as a visual diagnosis alone if the clinical course is '
                  'atypical; the atlas repeatedly emphasizes integrating the whole clinical picture.',
  'management': 'Begin with meticulous aural toilet/debridement and topical therapy directed at the inflamed/granulating '
                'tympanic membrane/canal while keeping the ear dry and removing ongoing trauma or irritants. Persistent '
                'focal granulation may require cautery or surgical removal. Refractory disease with epithelial loss, '
                'fibrosis, or meatal/canal stenosis may require excision/canalplasty with skin grafting.',
  'pearl': 'Ask whether granulation is a diagnosis or a sign. Persistent or atypical granulation may demand a broader '
           'workup.',
  'followup': 'What chronic structural complication can develop medially in the EAC?',
  'management_considerations': 'Persistent or atypical granulation deserves reconsideration of the diagnosis—chronic '
                               'infection, foreign body, cholesteatoma, neoplasm, or other inflammatory disease—rather than '
                               'indefinite topical treatment.',
  'source_note': 'Atlas-based management, cross-referenced with textbook principles for chronic external-ear inflammation '
                 'and stenosis.',
  'visual_strategy': 'Atlas remains primary; emphasize mimic recognition',
  'external_visuals': [],
  'visual_pearl': 'Persistent granulation on the TM/canal should trigger a second question: why is this tissue still '
                  'granulating?',
  'look_alike': 'Cholesteatoma, chronic infection, foreign body, EAC malignancy, and necrotizing otitis externa can all '
                'produce granulation.'},
 {'id': 'oto_otomycosis',
  'level': 3,
  'image': 'otoscopy/otomycosis.jpg',
  'source': 'Atlas p. 14 (PDF p. 21), Fig. 3.23',
  'prompt': 'Describe the debris. What diagnosis does its appearance suggest?',
  'findings': ['Black-speckled fungal-appearing debris',
               'Keratin/debris within a chronically abnormal ear',
               'Irregular inflamed canal/cavity surface'],
  'diagnosis': 'Otomycosis (fungal superinfection)',
  'differential': 'The atlas notes Aspergillus and Candida species and emphasizes chronic otorrhea/debris as local risk '
                  'factors.',
  'management': 'The cornerstone is thorough microscopic cleaning/debridement and keeping the canal dry. Add an appropriate '
                'topical antifungal when needed (commonly an azole such as clotrimazole). Stop unnecessary topical '
                'antibiotics/steroids that may be perpetuating fungal overgrowth and address hearing-aid/occlusion or '
                'moisture risk factors.',
  'pearl': 'In otology, debris is information: color, texture, location, and what lies underneath all matter.',
  'followup': 'What patient and local factors does the atlas associate with otomycosis?',
  'management_considerations': 'Always establish whether the tympanic membrane is intact before choosing topical agents. '
                               'The pediatric textbook specifically warns that several acidifying/antiseptic preparations '
                               'are potentially ototoxic with a perforation. Refractory or invasive-appearing disease, '
                               'cellulitis, diabetes, or immunocompromise warrants reassessment and escalation.',
  'source_note': 'Cross-referenced with Bluestone & Stool: debridement is necessary; clotrimazole and other antifungals are '
                 'options; avoid potentially ototoxic preparations when the TM is non-intact.',
  'visual_strategy': 'Atlas + contemporary Aspergillus example',
  'external_visuals': [{'label': 'Contemporary otomycosis example',
                        'source': 'Merck Manual Professional — Otomycosis',
                        'url': 'https://www.merckmanuals.com/en-ca/professional/multimedia/image/otomycosis',
                        'why': 'Clear example of Aspergillus hyphae and conidiophores in the EAC.',
                        'type': 'contemporary clinical image'},
                       {'label': 'Current external-otitis review',
                        'source': 'Merck Manual Professional — External Otitis (reviewed May 2026)',
                        'url': 'https://www.merckmanuals.com/professional/ear-nose-and-throat-disorders/external-ear-disorders/external-otitis-acute',
                        'why': 'Shows the characteristic cotton-like fungal material and contrasts fungal symptoms with '
                               'bacterial AOE.',
                        'type': 'current review'}],
  'visual_pearl': 'Aspergillus often gives the classic cotton-like hyphae with dark/yellow conidiophores. Candida may look '
                  'more like thick creamy white debris, so do not memorize only one fungal appearance.',
  'look_alike': 'Bacterial AOE: usually more painful, with diffuse inflamed canal and purulent debris rather than '
                'characteristic fungal elements.'},
 {'id': 'oto_eczema',
  'level': 3,
  'image': 'otoscopy/eczema.jpg',
  'source': 'Atlas p. 15 (PDF p. 22), Fig. 3.25',
  'prompt': 'Is the primary abnormality in the canal skin or middle ear?',
  'findings': ['Squamous debris coating EAC skin',
               'Dermatitis-like canal surface',
               'Tympanic membrane is not the primary lesion'],
  'diagnosis': 'Chronic eczema of the external auditory canal',
  'differential': 'Otomycosis and other causes of chronic otitis externa can also produce debris; morphology and history '
                  'help separate them.',
  'management': 'Remove the trigger and restore the canal skin barrier: stop mechanical trauma/cotton swabs and identify '
                'contact allergens or irritating ear products/hearing-aid materials. Use a short course of topical '
                'corticosteroid for active dermatitis when appropriate; treat secondary bacterial or fungal infection only '
                'when actually present.',
  'pearl': 'Itch + canal skin disease should pull your localization outward before you anchor on otitis media.',
  'followup': 'What history would you ask for to identify a local irritant or contact trigger?',
  'management_considerations': 'Recurrent disease should prompt consideration of atopic dermatitis, seborrheic dermatitis, '
                               'psoriasis, allergic contact dermatitis, hearing-aid irritation, and chronic moisture. Avoid '
                               'a repeated antibiotic cycle when the primary problem is inflammatory dermatitis.',
  'source_note': "Cross-referenced with Bluestone & Stool's chronic external-otitis discussion: eliminate predisposing "
                 'factors and treat inflammation; topical steroids can interrupt the itch-scratch cycle.',
  'visual_strategy': 'Atlas + contemporary dermatitis context',
  'external_visuals': [{'label': 'Contemporary ear-canal dermatitis review',
                        'source': 'Merck Manual Professional — Dermatitis of the Ear Canal',
                        'url': 'https://www.merckmanuals.com/en-ca/professional/ear-nose-and-throat-disorders/external-ear-disorders/dermatitis-of-the-ear-canal-chronic-otitis-externa',
                        'why': 'Useful contemporary comparison for inflammatory canal disease and contact/eczematoid '
                               'triggers.',
                        'type': 'current review'}],
  'visual_pearl': 'Scaling, flaking and chronic inflamed skin should make you think barrier/dermatitis first, especially '
                  'when itch dominates pain.',
  'look_alike': 'Diffuse AOE can be erythematous and edematous, but pain/otorrhea and infectious debris are usually more '
                'prominent.'},
 {'id': 'oto_eac_chol',
  'level': 5,
  'image': 'otoscopy/eac_cholesteatoma.jpg',
  'source': 'Atlas p. 15 (PDF p. 22), Fig. 3.26',
  'prompt': 'This white canal mass is not simply cerumen. Build the differential.',
  'findings': ['Focal white keratinous mass in the EAC',
               'Surrounding debris/inflammation',
               'Mass appears localized rather than diffuse'],
  'diagnosis': 'External auditory canal cholesteatoma',
  'differential': 'The atlas contrasts EAC cholesteatoma with exostosis and keratosis obturans: cholesteatoma is described '
                  'as soft/tender and often unilateral in older patients; exostosis is bony; keratosis obturans tends to be '
                  'bilateral in younger patients.',
  'management': 'First define extent. Obtain audiometry and high-resolution temporal-bone CT when bony erosion/extension is '
                'suspected. Small, well-visualized EAC cholesteatoma may be managed with meticulous office debridement and '
                'surveillance; topical antibiotic drops can be used when secondary infection is present. Progressive focal '
                'bony erosion or disease not controllable in the office requires surgical removal/canalplasty. Extension '
                'into mastoid or middle ear may require tympanomastoid surgery.',
  'pearl': 'A white canal mass is a differential, not a diagnosis. Ask: bone or keratin? focal or circumferential? '
           'unilateral or bilateral? erosion or no erosion?',
  'followup': 'What imaging finding would make EAC cholesteatoma more convincing?',
  'management_considerations': 'Distinguish EAC cholesteatoma from keratosis obturans and from malignancy/necrotizing '
                               'otitis externa when there is focal erosion or granulation. Assess proximity to the facial '
                               'nerve and tympanic membrane before drilling; facial nerve monitoring is reasonable when '
                               'medial canal/mastoid drilling is anticipated.',
  'source_note': 'Cross-referenced with Operative Otolaryngology: CT defines focal bony erosion and mastoid/facial-nerve '
                 'involvement; limited disease may be serially debrided, while extensive mastoid disease generally requires '
                 'tympanomastoidectomy.',
  'visual_strategy': 'Atlas remains best for true EAC cholesteatoma; add contemporary middle-ear cholesteatoma comparison',
  'external_visuals': [{'label': 'Contemporary cholesteatoma comparison',
                        'source': 'Merck Manual Professional — Cholesteatoma',
                        'url': 'https://www.merckmanuals.com/professional/multimedia/image/cholesteatoma',
                        'why': 'Shows classic keratinous cholesteatoma morphology and helps reinforce the appearance of '
                               'white keratin debris, although this example is middle-ear rather than isolated EAC '
                               'cholesteatoma.',
                        'type': 'important visual comparison'},
                       {'label': 'Current cholesteatoma review',
                        'source': 'Merck Manual Professional — Cholesteatoma (reviewed June 2026)',
                        'url': 'https://www.merckmanuals.com/professional/ear-nose-and-throat-disorders/middle-ear-and-tympanic-membrane-disorders/cholesteatoma',
                        'why': 'Current clinical context for keratin debris, complications, audiometry, imaging, and '
                               'surgical management.',
                        'type': 'current review'}],
  'visual_pearl': "For EAC cholesteatoma, focus on focal keratin debris plus focal bony erosion rather than simply 'white "
                  "debris in the canal.'",
  'look_alike': 'Keratosis obturans tends to produce a circumferential keratin plug/canal widening rather than focal '
                'erosive disease.'}]



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



# ENT Mastery site-wide teaching standard (v2.1)
CURRICULUM_STANDARD = {
    "version": "2.1",
    "principle": "Describe/localize first, diagnose second, explain physiology/pathology, then connect workup to management and operative decision-making.",
    "layers": [
        "Recognition / key findings",
        "Describe before diagnosing",
        "Important mimics / differential",
        "Mental model / why",
        "Workup: what, why, expected result, management impact",
        "Management: observation → medical → procedural → surgical",
        "Management considerations / special populations / escalation",
        "Operative technique when relevant",
        "Danger structures / complications",
        "Evidence basis and freshness",
        "Attending Follow-Up + Reveal Answer",
        "Teach Your Junior"
    ],
    "source_hierarchy": [
        "Current specialty guidelines / consensus / regulatory labeling for current management",
        "Cummings / K.J. Lee / Pasha for comprehensive disease framework",
        "Operative Otolaryngology + specialty operative texts for technique and danger anatomy",
        "Bluestone & Stool for pediatric ENT",
        "Dedicated atlases for visual pattern recognition",
        "Reputable academic/open-access online resources when they add a better visual or newer context"
    ],
    "visual_policy": "Newer is not automatically better. Keep a classic atlas image when it teaches the finding well; add external visuals only for clarity, phenotype diversity, subtle disease, or important mimics. Never re-host copyrighted external media without permission.",
    "terminology": {
        "forbidden_user_label": "legacy oral-exam label",
        "preferred_labels": ["Attending Follow-Up","Teach Your Junior","Clinical Reasoning","Operative Pearl","Danger Zone","Reveal Answer"]
    }
}

SOURCE_LIBRARY = {
    "Cummings": "Cummings Otolaryngology—Head and Neck Surgery, 7th ed. (user library)",
    "Pasha": "Otolaryngology–Head and Neck Surgery Clinical Reference Guide, 6th ed. (user library)",
    "KJLee": "K.J. Lee's Essential Otolaryngology, 12th ed. (user library)",
    "Operative": "Operative Otolaryngology—Head and Neck Surgery, 3rd ed. (user library)",
    "Laryngology2024": "Operative Techniques in Laryngology (2024) (user library)",
    "Bluestone": "Bluestone & Stool's Pediatric Otolaryngology, 5th ed. (user library)",
    "OtoscopyAtlas": "Color Atlas of Otoscopy (user library)"
}

def apply_curriculum_standard(card, domain=None):
    """Normalize a curriculum card without deleting card-specific teaching."""
    if not isinstance(card, dict):
        return card
    card.setdefault("curriculum_version", CURRICULUM_STANDARD["version"])
    card.setdefault("domain", domain or card.get("domain", "ENT"))
    card.setdefault("important_mimics", card.get("differential", ""))
    card.setdefault("clinical_reasoning", card.get("why", card.get("why_it_matters", "")))
    card.setdefault("management_considerations", "")
    card.setdefault("operative_pearl", "")
    card.setdefault("danger_zone", "")
    card.setdefault("evidence_basis", [])
    card.setdefault("evidence_status", "Textbook-grounded; verify time-sensitive management against current guidance.")
    card.setdefault("teach_your_junior", "")
    card.setdefault("follow_answer", card.get("follow_answer", ""))
    card.setdefault("follow_why", card.get("follow_why", ""))
    return card



# Apply the universal schema to every currently defined curriculum card.
try:
    if isinstance(OTOSCOPY_CASES, list):
        OTOSCOPY_CASES = [apply_curriculum_standard(c, "Otology / Otoscopy") for c in OTOSCOPY_CASES]
except NameError:
    pass

try:
    if isinstance(INTERPRETATION_LABS, dict):
        for _lab_key, _lab in INTERPRETATION_LABS.items():
            if isinstance(_lab, dict) and isinstance(_lab.get("cases"), list):
                _lab["cases"] = [apply_curriculum_standard(c, _lab.get("title", _lab_key)) for c in _lab["cases"]]
except NameError:
    pass


# Adaptive Interpretation Atlas expansion (v3)
def expand_lab_case_variants(cases, domain):
    """Create multiple retrieval contexts from each evidence-reviewed seed card.
    Variants reuse the reviewed teaching content rather than inventing new facts.
    """
    expanded=[]
    for seed in cases:
        c=dict(seed)
        base_id=c.get("id")
        c.setdefault("concept_id", f"{domain}:{base_id}")
        c.setdefault("variant_type", "interpret")
        expanded.append(c)

        # Mechanism / reverse-reasoning variant.
        v=dict(c)
        v["id"]=f"{base_id}_reason"
        v["variant_type"]="reason"
        v["prompt"]=("Reason backward from this case: what finding or mechanism is doing the most diagnostic/localizing work, "
                     "and what important mimic would you actively exclude?")
        v["answer"]=c.get("why") or c.get("answer")
        v["why"]="This is the same concept from a different retrieval direction so you learn the mental model rather than memorize one card."
        v["follow"]=c.get("follow") or "What single additional finding would most change your differential or next step?"
        expanded.append(v)

        # Teaching / management-transfer variant.
        t=dict(c)
        t["id"]=f"{base_id}_teach"
        t["variant_type"]="teach"
        t["prompt"]=("Teach this case to a junior resident in 30 seconds: describe the key finding, localize it, explain why it matters, "
                     "and state the next clinical question or management decision.")
        t["answer"]=c.get("answer")
        t["why"]=c.get("why") or "Teaching forces compression of recognition, localization, mechanism, and decision-making into one usable mental model."
        t["follow"]=c.get("follow") or "What mistake would a junior resident be most likely to make here?"
        expanded.append(t)
    return expanded

# Expand every non-otoscopy Interpretation Atlas to three retrieval contexts per seed card.
# Otoscopy keeps its curated visual cards intact; it participates in adaptive scheduling separately.
for _adaptive_slug, _adaptive_lab in INTERPRETATION_LABS.items():
    if isinstance(_adaptive_lab, dict) and isinstance(_adaptive_lab.get("cases"), list):
        _adaptive_lab["seed_case_count"] = len(_adaptive_lab["cases"])
        _adaptive_lab["cases"] = expand_lab_case_variants(_adaptive_lab["cases"], _adaptive_slug)
        _adaptive_lab["adaptive"] = True

for _oto in OTOSCOPY_CASES:
    _oto.setdefault("concept_id", f"otoscopy:{_oto.get('id')}")
    _oto.setdefault("variant_type", "interpret")


# =============================================================================
# ENT Mastery v4 — Chief Engine
# =============================================================================

MASTERY_DIMENSIONS = [
    {"id":"recognition","name":"Recognition","icon":"◉","description":"Recognize the pattern / key finding."},
    {"id":"localization","name":"Localization","icon":"⌖","description":"Localize anatomy, physiology, or lesion level."},
    {"id":"reasoning","name":"Clinical Reasoning","icon":"↯","description":"Explain why the finding means what it means."},
    {"id":"workup","name":"Workup","icon":"⌕","description":"Choose the next test and explain why it changes management."},
    {"id":"management","name":"Management","icon":"→","description":"Choose observation, medical, procedural, or surgical management."},
    {"id":"operative","name":"Operative Reasoning","icon":"⌁","description":"Plan the operation, danger anatomy, and rescue decisions."},
    {"id":"teaching","name":"Teach Your Junior","icon":"♟","description":"Explain the concept clearly from first principles."},
]

ATTENDING_LEVELS = [
    {"id":"junior","name":"PGY-1 / Junior","description":"Recognition, anatomy, first-step workup."},
    {"id":"resident","name":"PGY-2/3","description":"Localization, differential, management decisions."},
    {"id":"senior","name":"Senior","description":"Operative indications, alternatives, complications."},
    {"id":"chief","name":"Chief / Boards","description":"Edge cases, rescue decisions, and teaching from first principles."},
]

INTEGRATED_CASES = [
    {
      "id":"integrated-phpt","title":"Hypercalcemia → Parathyroidectomy","domain":"Head & Neck",
      "concept_id":"primary_hyperparathyroidism",
      "summary":"A progressive endocrine-surgery case from incidental lab abnormality through operative planning.",
      "source_basis":["Current Parathyroid Disease module","Operative Otolaryngology — parathyroidectomy"],
      "stages":[
        {"title":"Presentation","dimension":"reasoning","stimulus":"58-year-old with calcium 11.3 mg/dL found on routine labs.",
         "question":"What is the first physiologic branch point?",
         "answer":"Confirm the calcium abnormality and determine whether the hypercalcemia is PTH-dependent by measuring intact PTH.",
         "why":"The first job is diagnosis of the physiology—not localization."},
        {"title":"Biochemistry","dimension":"reasoning","stimulus":"Intact PTH is 78 pg/mL (lab reference 15–65).",
         "question":"What does this mean in a hypercalcemic patient?",
         "answer":"PTH is not suppressed despite hypercalcemia, supporting PTH-dependent hypercalcemia.",
         "why":"Even a laboratory-normal PTH can be inappropriate when calcium is high because normal physiology should suppress PTH."},
        {"title":"Workup","dimension":"workup","stimulus":"The biochemical pattern is consistent with primary hyperparathyroidism.",
         "question":"What needs to be assessed before localization, and why?",
         "answer":"Assess renal function, vitamin D/phosphorus, urinary calcium/FHH differential, skeletal involvement, and renal stone/nephrocalcinosis involvement. Confirm disease and target-organ impact before using localization to plan surgery.",
         "why":"Localization answers where/how to operate; it does not establish the disease."},
        {"title":"Localization","dimension":"workup","stimulus":"Neck ultrasound and sestamibi are nonlocalizing.",
         "question":"Does the diagnosis disappear? What changes?",
         "answer":"No. PHPT remains a biochemical diagnosis. Nonlocalizing studies change operative planning and may favor additional localization or bilateral exploration by an experienced surgeon.",
         "why":"Negative localization is not a negative diagnostic test."},
        {"title":"Operation","dimension":"operative","stimulus":"The patient proceeds to parathyroidectomy.",
         "question":"What findings would make you broaden from a focused approach to bilateral exploration?",
         "answer":"Discordant/nonlocalizing studies, suspected multigland or hereditary disease, unexpected anatomy, or intraoperative PTH/findings inconsistent with single-gland cure.",
         "why":"The operation should follow the physiology and intraoperative evidence rather than remain locked to the preoperative image."},
        {"title":"Rescue","dimension":"operative","stimulus":"The expected inferior gland is not where you anticipated.",
         "question":"How should embryology guide your search?",
         "answer":"Follow the third-pouch/thymic migration pathway: lower pole/thyrothymic region, cervical thymus, and potentially mediastinal sites when appropriate.",
         "why":"Embryology converts a random search into a structured search strategy."},
        {"title":"Teach Your Junior","dimension":"teaching","stimulus":"A junior asks why a negative sestamibi does not rule out PHPT.",
         "question":"Explain it in 30 seconds.",
         "answer":"PHPT is diagnosed from calcium/PTH physiology. Sestamibi is a localization test used after the diagnosis to help plan surgery, so a negative scan cannot erase a biochemical diagnosis.",
         "why":"If you can separate diagnosis from localization clearly enough to teach it, you understand the decision model."}
      ]
    },
    {
      "id":"integrated-hns","title":"Adult OSA → DISE → HNS","domain":"Sleep","concept_id":"adult_osa_hns",
      "summary":"Interpret the PSG first, then decide whether anatomy and treatment history support hypoglossal nerve stimulation.",
      "source_basis":["Current Sleep / PSG / HNS lab","Current FDA/device-label teaching layer already incorporated in ENT Mastery"],
      "stages":[
        {"title":"PSG","dimension":"recognition","stimulus":"Adult PSG: AHI 26.4/hr, central apnea index 0.8/hr, SpO₂ nadir 82%.",
         "question":"Describe the study before discussing a procedure.",
         "answer":"This is moderate, predominantly obstructive sleep apnea with meaningful desaturation and low central-event burden.",
         "why":"HNS is an upper-airway treatment, so event type matters—not just the total AHI."},
        {"title":"Phenotype","dimension":"reasoning","stimulus":"Supine AHI 31/hr and REM AHI 39/hr.",
         "question":"What information do position and REM add?",
         "answer":"They show when obstruction is most pronounced and help define the physiologic phenotype; overall AHI alone can hide clinically relevant patterns.",
         "why":"Two patients with the same AHI can have different mechanisms and treatment options."},
        {"title":"Treatment history","dimension":"management","stimulus":"The patient cannot tolerate PAP despite an adequate trial.",
         "question":"Why is PAP history part of HNS selection?",
         "answer":"HNS is generally considered for selected patients with clinically significant predominantly obstructive OSA who fail or cannot tolerate PAP rather than as an automatic first-line implant.",
         "why":"Procedure selection depends on both physiology and prior treatment response."},
        {"title":"DISE","dimension":"localization","stimulus":"DISE demonstrates complete concentric collapse at the soft palate.",
         "question":"What does that do to Inspire candidacy?",
         "answer":"It is a key exclusion for Inspire upper-airway stimulation despite otherwise favorable PSG and PAP-history features.",
         "why":"DISE is testing the collapse phenotype—not re-proving that OSA exists."},
        {"title":"Post-implant reasoning","dimension":"management","stimulus":"In a different implanted patient, AHI improves from 42 to 17 but symptoms persist.",
         "question":"Is this simply device failure?",
         "answer":"Not necessarily. Characterize residual obstructive vs central events, positional/REM pattern, oxygen burden, device use/settings, tongue motion, and residual anatomic collapse before deciding on revision or adjunctive therapy.",
         "why":"Residual OSA is a troubleshooting problem, not a binary implant success/failure label."},
        {"title":"Teach Your Junior","dimension":"teaching","stimulus":"A junior quotes one old AHI/BMI cutoff as the entire HNS workup.",
         "question":"What principle should you teach?",
         "answer":"Separate current FDA/device labeling, the clinical evidence base, payer criteria, PSG physiology, PAP history, and DISE phenotype. They answer different questions and can change at different times.",
         "why":"Memorizing one cutoff is fragile; understanding the candidacy framework is durable."}
      ]
    },
    {
      "id":"integrated-airway","title":"Stridor → Endoscopy → Airway Strategy","domain":"Laryngology / Airway","concept_id":"airway_stenosis",
      "summary":"Localize the airway problem, describe its geometry, and let the lesion—not the label—drive treatment.",
      "source_basis":["Airway & Bronchoscopy Lab","Operative Techniques in Laryngology (2024) — stenosis evaluation and treatment planning"],
      "stages":[
        {"title":"Symptom localization","dimension":"localization","stimulus":"A patient presents with progressive biphasic stridor.",
         "question":"What can you infer, and what can you not infer yet?",
         "answer":"A fixed central airway lesion is possible, but the symptom alone does not identify the precise level or cause. Endoscopic localization is required.",
         "why":"Symptoms localize broadly; endoscopy defines anatomy and mechanism."},
        {"title":"Endoscopic description","dimension":"recognition","stimulus":"Endoscopy shows a short subglottic narrowing.",
         "question":"What must you describe besides Cotton-Myer grade?",
         "answer":"Level, length, concentric vs eccentric geometry, mature scar vs inflamed tissue, posterior/glottic involvement, tracheal extension, vocal-fold mobility, and prior reconstruction/treatment.",
         "why":"Grade alone does not tell you whether an endoscopic or open strategy makes sense."},
        {"title":"Mechanics","dimension":"reasoning","stimulus":"The narrowing changes dramatically with respiration and positive pressure.",
         "question":"What conceptual category changes?",
         "answer":"Dynamic collapse becomes more likely than a purely fixed stenosis.",
         "why":"Dynamic disease is a mechanics problem; fixed stenosis is a structural lumen problem."},
        {"title":"Treatment strategy","dimension":"management","stimulus":"Compare a short, soft early stenosis with a long mature circumferential scar involving the cricoid.",
         "question":"Why should the treatment strategy differ?",
         "answer":"The short/soft lesion is more amenable to endoscopic management, while long mature structural scar has a greater likelihood of requiring reconstructive/open strategies depending on the patient and prior treatment.",
         "why":"Treatment follows lesion biology and geometry rather than the diagnostic label alone."},
        {"title":"Danger / planning","dimension":"operative","stimulus":"You are planning airway surgery.",
         "question":"What preoperative information should change the operative plan?",
         "answer":"Exact level and length, posterior glottic involvement, vocal-fold mobility, cartilage framework, tracheal extension, prior procedures, and the ability to safely ventilate/expose the airway.",
         "why":"Airway surgery is simultaneously a lesion operation and an airway-management operation."},
        {"title":"Teach Your Junior","dimension":"teaching","stimulus":"A junior says, 'It's grade III SGS, so I know the operation.'",
         "question":"How do you correct that mental model?",
         "answer":"Cotton-Myer grade describes lumen narrowing, but treatment also depends on length, level, maturity, geometry, posterior/glottic involvement, framework, prior treatment, and patient factors.",
         "why":"A single grade is a descriptor, not a complete surgical plan."}
      ]
    }
]

def get_integrated_case(case_id):
    return next((x for x in INTEGRATED_CASES if x["id"] == case_id), None)

OR_PREP_REGISTRY = {
    op["slug"]: {
        "slug": op["slug"], "title": op["title"], "domain": "Head & Neck",
        "indications": op["indications"], "steps": op["steps"], "danger": op["danger"],
        "attending_followup": op.get("Attending Follow-Up", op.get("viva", [])),
        "linked_topic": op.get("topic"), "status": "audited"
    } for op in OPERATIONS
}

ATTENDING_LEVEL_PROMPTS = {
    "junior": [
        {"domain":"Head & Neck","concept_id":"phpt_diagnosis","prompt":"Hypercalcemia is present. What single physiologic branch point should you establish first?","answer":"Determine whether the hypercalcemia is PTH-dependent by confirming calcium and measuring intact PTH."},
        {"domain":"Otology","concept_id":"otoscopy_normal","prompt":"Before naming ear pathology, what features should you systematically describe on otoscopy?","answer":"Canal findings plus tympanic-membrane integrity, position, color/translucency, landmarks, mobility when assessed, and middle-ear contents."},
        {"domain":"Laryngology","concept_id":"stroboscopy_basics","prompt":"Name the core dynamic parameters assessed on stroboscopy.","answer":"Glottic closure, mucosal wave, amplitude, symmetry, and periodicity, with mobility and supraglottic behavior interpreted in context."}
    ],
    "resident": [
        {"domain":"Head & Neck","concept_id":"phpt_localization","prompt":"Why does negative localization imaging not rule out primary hyperparathyroidism?","answer":"Because PHPT is diagnosed biochemically; localization studies are used to plan the operation."},
        {"domain":"Sleep","concept_id":"hns_selection","prompt":"Why is a high AHI alone insufficient to decide HNS candidacy?","answer":"You also need event type/central burden, PAP failure or intolerance, anatomic collapse phenotype on DISE, and current device/payer criteria."},
        {"domain":"Airway","concept_id":"stenosis_description","prompt":"What information is missing if someone presents an airway lesion only as 'Cotton-Myer grade III'?","answer":"Level, length, geometry, maturity, posterior/glottic involvement, tracheal extension, mobility, prior treatment, and framework/airway context."}
    ],
    "senior": [
        {"domain":"Head & Neck","concept_id":"phpt_operation","prompt":"When should a focused parathyroid operation become a broader exploration?","answer":"When imaging/intraoperative findings are discordant, multigland or hereditary disease is suspected, anatomy is unexpected, or intraoperative physiology does not support cure."},
        {"domain":"Laryngology","concept_id":"glottic_insufficiency","prompt":"Why is vocal-fold augmentation not conceptually the same operation as framework medialization?","answer":"Both improve glottic closure, but injection augments tissue volume while framework surgery changes vocal-fold position through the laryngeal framework/paraglottic space."},
        {"domain":"Airway","concept_id":"airway_strategy","prompt":"Why can two patients with the same stenosis grade need different operations?","answer":"Because length, level, maturity, geometry, framework, mobility, prior treatment, and patient/airway factors determine the strategy."}
    ],
    "chief": [
        {"domain":"Head & Neck","concept_id":"phpt_teaching","prompt":"A junior wants sestamibi before proving PHPT. Teach the diagnostic-vs-localization distinction in 30 seconds.","answer":"Calcium/PTH physiology establishes whether PHPT exists. Imaging comes after the diagnosis to help locate abnormal tissue and choose an operative strategy; a scan cannot diagnose or exclude the biochemical disease."},
        {"domain":"Sleep","concept_id":"hns_framework","prompt":"Teach why FDA labeling, evidence, payer criteria, PSG physiology, and DISE should not be collapsed into one HNS 'cutoff.'","answer":"They answer different questions: approved use, expected outcomes/uncertainty, payment rules, whether events are obstructive, and whether the collapse phenotype is appropriate for the device."},
        {"domain":"Airway","concept_id":"airway_teaching","prompt":"A resident keeps memorizing stenosis grades. Give them a more durable surgical mental model.","answer":"Describe where the lesion is, how long it is, whether it is fixed or dynamic, mature or inflamed, circumferential or focal, whether it involves glottis/posterior glottis/trachea, and what prior treatment/framework/airway factors change the operation."}
    ]
}


# =============================================================================
# ENT Mastery v4.1 — Content Expansion
# New cases are deliberately distinct clinical scenarios, not reworded cards.
# Source labels distinguish uploaded-textbook/atlas concepts from current CPGs.
# =============================================================================

INTEGRATED_CASES_V41 = [
{
"id":"integrated-ssnhl","title":"Sudden Hearing Loss → Audiogram → Urgent Management",
"domain":"Otology / Audiology","concept_id":"ssnhl",
"summary":"Distinguish conductive from sensorineural loss quickly, avoid low-value testing, and manage a time-sensitive otologic presentation.",
"source_basis":["AAO-HNSF Clinical Practice Guideline: Sudden Hearing Loss (Update, 2019)"],
"stages":[
{"title":"Triage","dimension":"recognition","stimulus":"A 52-year-old wakes with abrupt left hearing loss and aural fullness. Otoscopy is normal.","question":"What dangerous assumption should you avoid?","answer":"Do not assume fullness means middle-ear disease. Sudden sensorineural hearing loss must remain high on the differential until hearing type is established.","why":"The key early error is delaying recognition of a time-sensitive sensorineural loss."},
{"title":"Bedside localization","dimension":"localization","stimulus":"There is no obvious cerumen, effusion, or perforation.","question":"What should you do immediately while arranging formal audiometry?","answer":"Use bedside hearing assessment/tuning-fork localization when appropriate and obtain prompt audiometry to distinguish conductive from sensorineural loss.","why":"The first management branch point is hearing type."},
{"title":"Audiogram","dimension":"recognition","stimulus":"Audiometry confirms an acute unilateral sensorineural hearing loss.","question":"What diagnosis now drives the urgent pathway?","answer":"Sudden sensorineural hearing loss; assess for identifiable causes and neurologic red flags while treating it as time-sensitive.","why":"Prompt recognition and management are central goals of the AAO-HNSF guideline."},
{"title":"Imaging strategy","dimension":"workup","stimulus":"The neurologic examination is otherwise reassuring.","question":"Should you order a routine head CT to evaluate idiopathic SSNHL?","answer":"No. Routine head CT is not the preferred retrocochlear evaluation. The workup should be directed rather than a shotgun radiology/laboratory panel.","why":"High-value care means testing for questions that change the differential or management."},
{"title":"Treatment discussion","dimension":"management","stimulus":"The patient presents early after onset.","question":"What treatment conversation should occur promptly?","answer":"Discuss corticosteroid treatment options and the expected benefits, uncertainty, risks, timing, and follow-up audiometry; salvage intratympanic therapy is part of the pathway for incomplete recovery in the appropriate time window.","why":"The disease is time-sensitive, so counseling and shared decision-making should not be deferred."},
{"title":"Teach Your Junior","dimension":"teaching","stimulus":"A junior says, 'The ear feels blocked, so I'll treat ETD first.'","question":"Correct the mental model.","answer":"Aural fullness does not localize the problem to the middle ear. First determine conductive versus sensorineural hearing loss; an acute SNHL changes urgency and management completely.","why":"Symptom labels are weaker than physiologic localization."}
]},
{
"id":"integrated-meniere","title":"Episodic Vertigo → Audiogram → Ménière Framework",
"domain":"Otology / Vestibular","concept_id":"meniere",
"summary":"Use timing, auditory symptoms, audiometry, and competing diagnoses rather than labeling every dizzy patient 'Ménière.'",
"source_basis":["AAO-HNSF Clinical Practice Guideline: Ménière’s Disease (2020)"],
"stages":[
{"title":"History","dimension":"reasoning","stimulus":"A 44-year-old has recurrent spontaneous vertigo with fluctuating unilateral tinnitus and aural pressure.","question":"What history feature matters more than the word 'dizzy'?","answer":"Characterize discrete episode duration, recurrence, associated auditory symptoms, migraine features, triggers, and neurologic symptoms.","why":"Vestibular diagnosis is built around timing/triggers and associated features."},
{"title":"Audiology","dimension":"workup","stimulus":"The history raises concern for Ménière disease.","question":"What core test belongs in the diagnostic evaluation?","answer":"Obtain an audiogram to characterize hearing and document the auditory component of the syndrome.","why":"Ménière disease is an audiovestibular diagnosis; hearing data matter."},
{"title":"Differential","dimension":"reasoning","stimulus":"The patient also has photophobia and a long migraine history.","question":"What common competing diagnosis must be actively considered?","answer":"Vestibular migraine.","why":"Ménière disease has important mimics, and diagnostic accuracy is a major purpose of the guideline."},
{"title":"Testing restraint","dimension":"workup","stimulus":"The diagnosis is clinically plausible.","question":"Do you need an indiscriminate vestibular test battery to make the diagnosis?","answer":"No. Testing should answer a specific diagnostic question; unnecessary vestibular/electrophysiologic testing can add noise without improving diagnostic accuracy.","why":"More tests do not automatically mean a better vestibular diagnosis."},
{"title":"Management","dimension":"management","stimulus":"The patient has persistent bothersome attacks.","question":"How should treatment be conceptualized?","answer":"Separate acute attack treatment from preventive/lifestyle strategies, hearing rehabilitation, and escalation for persistent active disease; use shared decision-making based on severity and treatment response.","why":"Management is longitudinal and symptom-domain specific."},
{"title":"Teach Your Junior","dimension":"teaching","stimulus":"A resident calls any vertigo plus tinnitus 'Ménière.'","question":"What do you teach?","answer":"Build the syndrome: recurrent spontaneous episodes with the appropriate duration pattern, auditory symptoms/hearing findings, and exclusion of better explanations such as vestibular migraine.","why":"Syndrome construction prevents premature closure."}
]},
{
"id":"integrated-bppv","title":"Positional Vertigo → Dix-Hallpike → Repositioning",
"domain":"Vestibular","concept_id":"bppv",
"summary":"Localize positional vertigo at the bedside and treat the mechanics instead of reflexively ordering imaging or medication.",
"source_basis":["AAO-HNSF Clinical Practice Guideline: BPPV (Update, 2017)"],
"stages":[
{"title":"Pattern","dimension":"recognition","stimulus":"A 67-year-old has seconds of spinning when rolling in bed or looking upward, without focal neurologic symptoms.","question":"What diagnosis should be near the top?","answer":"Benign paroxysmal positional vertigo, with canal localization determined by positional testing.","why":"Brief triggered episodes are a mechanical pattern."},
{"title":"Localization","dimension":"localization","stimulus":"Dix-Hallpike produces the characteristic posterior-canal positional nystagmus on the right.","question":"What have you localized?","answer":"Right posterior-canal BPPV.","why":"The eye movement pattern identifies the involved vestibular geometry."},
{"title":"Management","dimension":"management","stimulus":"The patient is otherwise stable.","question":"What is the most direct treatment?","answer":"A canalith repositioning maneuver appropriate for posterior-canal BPPV.","why":"Treat the displaced-particle mechanics rather than suppressing the vestibular system."},
{"title":"Low-value care","dimension":"workup","stimulus":"The history and examination are classic.","question":"Do you need routine CT/MRI or vestibular-suppressant medication as the primary strategy?","answer":"Not for a classic uncomplicated presentation. Additional testing is reserved for atypical features or an alternative diagnosis.","why":"The BPPV guideline emphasizes accurate bedside diagnosis and reducing unnecessary imaging/medication."},
{"title":"Failure","dimension":"reasoning","stimulus":"Symptoms persist after appropriate maneuvers.","question":"What should you reconsider?","answer":"Reassess canal/side, maneuver performance, another BPPV variant, coexisting vestibular disease, or a central/alternative diagnosis when the pattern is atypical.","why":"Treatment failure should trigger re-localization, not automatic repetition forever."},
{"title":"Teach Your Junior","dimension":"teaching","stimulus":"A junior wants meclizine and an MRI for every positional vertigo patient.","question":"Give the 20-second correction.","answer":"Classic BPPV is a bedside localization problem. Identify the canal with positional testing and treat with repositioning; image or broaden the workup when the presentation is atypical.","why":"Mechanism-based care is both more precise and higher value."}
]},
{
"id":"integrated-tubes","title":"Recurrent AOM / OME → Hearing → Tympanostomy Decision",
"domain":"Pediatric Otolaryngology","concept_id":"tympanostomy_tubes",
"summary":"Decide who benefits from tubes by separating recurrent infection from persistent effusion and hearing/developmental risk.",
"source_basis":["AAO-HNSF Clinical Practice Guideline: Tympanostomy Tubes in Children (Update, 2022)"],
"stages":[
{"title":"Presentation","dimension":"reasoning","stimulus":"A 3-year-old is referred for 'recurrent ear infections.'","question":"What distinction changes the tube discussion?","answer":"Determine the true infection history and whether middle-ear effusion is present/persistent, rather than treating the referral label alone.","why":"Tube candidacy depends on the clinical phenotype, not just a count copied from a referral."},
{"title":"Effusion","dimension":"recognition","stimulus":"Pneumatic otoscopy/tympanometry supports persistent bilateral middle-ear effusion.","question":"What additional domain should you assess?","answer":"Hearing status, plus speech/language, learning, balance, discomfort, and developmental risk when relevant.","why":"The consequence of persistent effusion is as important as its presence."},
{"title":"Audiology","dimension":"workup","stimulus":"The effusion has persisted and the child is being considered for surgery.","question":"Why obtain age-appropriate hearing evaluation?","answer":"It quantifies functional impact, identifies unexpected permanent hearing loss, informs counseling, and helps judge benefit from intervention.","why":"A procedure decision should be tied to the problem it is intended to improve."},
{"title":"At-risk child","dimension":"management","stimulus":"A second child has developmental risk factors that make hearing access especially important.","question":"How should that alter your threshold for careful assessment?","answer":"Actively identify children at increased risk for speech, language, or learning problems and incorporate that risk into management rather than using a one-size-fits-all threshold.","why":"The same degree of conductive hearing loss can have different consequences in different children."},
{"title":"Post-tube","dimension":"management","stimulus":"The child later develops uncomplicated acute tube otorrhea.","question":"What treatment principle should guide management?","answer":"For uncomplicated acute tympanostomy-tube otorrhea, topical antibiotic ear drops are generally preferred over routine systemic antibiotics.","why":"The tube provides direct access to the infected middle ear and avoids unnecessary systemic exposure."},
{"title":"Teach Your Junior","dimension":"teaching","stimulus":"A junior says, 'Three ear infections means tubes.'","question":"What is missing?","answer":"Verify the episodes, examine for current/persistent effusion, assess hearing and developmental risk, and use the complete phenotype to decide whether tubes are likely to help.","why":"Counts are not a substitute for candidacy reasoning."}
]},
{
"id":"integrated-cholesteatoma","title":"Retraction Pocket → Cholesteatoma → CT / Operative Planning",
"domain":"Otology","concept_id":"cholesteatoma",
"summary":"Move from otoscopic recognition to extent, complications, hearing, and surgical strategy.",
"source_basis":["Color Atlas of Otoscopy: From Diagnosis to Surgery — uploaded atlas","Current ENT Mastery otoscopy curriculum"],
"stages":[
{"title":"Otoscopy","dimension":"recognition","stimulus":"Otoscopy shows a deep epitympanic retraction pocket with keratin debris.","question":"What disease process must you assume until adequately excluded?","answer":"Acquired cholesteatoma.","why":"Retraction plus trapped squamous debris is a structural disease process, not simply 'chronic fluid.'"},
{"title":"Whole patient","dimension":"reasoning","stimulus":"The patient also has progressive conductive hearing loss.","question":"Why is the otoscopic image only the beginning of the case?","answer":"You must define hearing, disease extent, ossicular/bony complications, facial/labyrinthine symptoms, and prior surgery; the atlas explicitly emphasizes integrating otoscopy with audiologic and neuroradiologic evaluation.","why":"The visible pocket can be the tip of a larger temporal-bone process."},
{"title":"Imaging","dimension":"workup","stimulus":"The extent cannot be confidently determined clinically.","question":"What question should temporal-bone CT answer?","answer":"Define bony anatomy and disease extent/erosion relevant to operative planning and complications rather than merely 'confirming a white mass.'","why":"Imaging is useful when it changes the map of the operation."},
{"title":"Operation","dimension":"operative","stimulus":"Disease extends into epitympanum and mastoid with ossicular erosion.","question":"What determines the operative strategy?","answer":"Extent, anatomy, hearing status, complications, Eustachian-tube/middle-ear environment, ability to achieve safe disease clearance, and the planned surveillance strategy.","why":"The operation is tailored to safe eradication and a maintainable ear, not to one universal mastoidectomy label."},
{"title":"Complication","dimension":"operative","stimulus":"The patient develops facial weakness and vertigo.","question":"How does that change urgency and thinking?","answer":"Treat these as red flags for complicated/advanced disease involving critical temporal-bone structures and escalate evaluation and surgical planning accordingly.","why":"Cranial nerve or labyrinthine symptoms imply disease beyond a simple pocket."},
{"title":"Teach Your Junior","dimension":"teaching","stimulus":"A junior calls the lesion 'just an attic perforation.'","question":"Teach the danger.","answer":"A small attic abnormality can conceal extensive cholesteatoma. Pair the otoscopic finding with hearing, symptoms, imaging when indicated, and an assessment of disease extent and complications.","why":"Surface size does not equal disease volume."}
]},
{
"id":"integrated-retrotympanic","title":"Pulsatile Tinnitus → Retrotympanic Mass → Don't Biopsy",
"domain":"Otology / Skull Base","concept_id":"retrotympanic_mass",
"summary":"Recognize a vascular middle-ear mass, build the differential, and avoid a hazardous office biopsy.",
"source_basis":["Color Atlas of Otoscopy: From Diagnosis to Surgery — uploaded atlas"],
"stages":[
{"title":"Recognition","dimension":"recognition","stimulus":"A patient has pulse-synchronous tinnitus and a reddish inferior retrotympanic mass.","question":"What category should immediately enter the differential?","answer":"A vascular retrotympanic lesion such as a tympanic/jugular paraganglioma, while remembering vascular variants and other middle-ear masses.","why":"Color, location, and pulsatile symptoms are high-value clues."},
{"title":"Anatomy","dimension":"localization","stimulus":"The mass appears centered in the hypotympanic/inferior middle-ear region.","question":"What skull-base anatomy matters?","answer":"Relationship to the jugular bulb/foramen, carotid canal, lower cranial nerves, facial canal, labyrinth, and intracranial/neck extension.","why":"The anatomy determines both diagnosis and procedural risk."},
{"title":"Safety","dimension":"management","stimulus":"Someone suggests office biopsy of the 'aural polyp.'","question":"What is the safer principle?","answer":"Do not blindly biopsy a potentially vascular or skull-base-connected ear-canal/middle-ear mass before appropriate imaging defines the lesion.","why":"The uploaded atlas specifically warns that outpatient biopsy of some EAC polyps without radiologic study can be hazardous."},
{"title":"Imaging","dimension":"workup","stimulus":"You suspect a paraganglioma.","question":"What should imaging characterize?","answer":"Bony involvement on high-resolution CT and soft-tissue/vascular extent on MRI; advanced lesions may require vascular imaging for operative planning.","why":"Imaging defines the lesion's class, critical structure involvement, and treatment options."},
{"title":"Counseling","dimension":"management","stimulus":"Imaging confirms a temporal-bone paraganglioma.","question":"What makes management individualized?","answer":"Tumor size/extent, symptoms, cranial-nerve function, hearing, age/comorbidity, growth, vascular anatomy, and tradeoffs among observation, radiation, and surgery.","why":"The morbidity of treatment can be as important as the morbidity of the tumor."},
{"title":"Teach Your Junior","dimension":"teaching","stimulus":"A junior sees a red mass and reaches for biopsy forceps.","question":"What rule do you teach?","answer":"A pulsatile or suspicious retrotympanic/EAC mass is an anatomy-and-imaging problem before it is a tissue-sampling problem.","why":"Safety starts with recognizing when biopsy is not the next step."}
]},
{
"id":"integrated-neckmass","title":"Adult Neck Mass → Malignancy Risk → Tissue Diagnosis",
"domain":"Head & Neck Oncology","concept_id":"adult_neck_mass",
"summary":"Treat a persistent adult neck mass as a diagnostic problem with malignancy risk until proven otherwise.",
"source_basis":["AAO-HNSF Clinical Practice Guideline: Evaluation of the Neck Mass in Adults (2017)"],
"stages":[
{"title":"Risk","dimension":"reasoning","stimulus":"A 61-year-old has a lateral neck mass present for several weeks without a convincing infectious course.","question":"What is the governing diagnostic mindset?","answer":"Identify whether the patient is at increased risk for malignancy and avoid prolonged empiric treatment that delays diagnosis.","why":"A persistent adult neck mass can be the first manifestation of head and neck cancer."},
{"title":"Examination","dimension":"workup","stimulus":"The mass is firm and persistent.","question":"What examination must extend beyond palpating the lump?","answer":"Perform a targeted head and neck examination, including mucosal evaluation of likely upper aerodigestive primary sites and cranial-nerve/skin/thyroid assessment as appropriate.","why":"The neck mass may be metastatic disease from an occult primary."},
{"title":"Imaging","dimension":"workup","stimulus":"The patient is at increased malignancy risk.","question":"What is the purpose of cross-sectional imaging?","answer":"Characterize the mass/nodal distribution, search for a primary site, and define anatomy for tissue diagnosis and subsequent management.","why":"Imaging should advance diagnosis and staging, not merely document that a lump exists."},
{"title":"Tissue","dimension":"management","stimulus":"A pathologic diagnosis is still needed.","question":"What sampling principle is preferred over jumping to open biopsy?","answer":"Use fine-needle aspiration as the initial tissue-sampling approach when appropriate rather than an unplanned open biopsy.","why":"An open biopsy can complicate definitive oncologic management."},
{"title":"Cystic node","dimension":"reasoning","stimulus":"Imaging calls the mass 'cystic.'","question":"Can you dismiss malignancy?","answer":"No. In an adult at increased risk, a cystic neck mass must not automatically be assumed benign; continue evaluation until a diagnosis is established.","why":"HPV-related oropharyngeal metastases can present as cystic cervical nodes."},
{"title":"Teach Your Junior","dimension":"teaching","stimulus":"A junior wants a third antibiotic course because the mass is painless.","question":"What do you teach?","answer":"Persistence without a convincing bacterial syndrome is a reason to establish a diagnosis, not to keep extending empiric antibiotics. Risk-stratify, examine the mucosa, image appropriately, and obtain tissue.","why":"Diagnostic delay is the preventable harm."}
]},
{
"id":"integrated-dysphonia","title":"Persistent Dysphonia → Laryngoscopy → Mechanism",
"domain":"Laryngology","concept_id":"dysphonia",
"summary":"Get from a voice complaint to visualization, mechanism, and targeted treatment without treating the symptom blindly.",
"source_basis":["AAO-HNSF Clinical Practice Guideline: Hoarseness (Dysphonia) Update (2018)","Current ENT Mastery laryngology/stroboscopy curriculum"],
"stages":[
{"title":"Red flags","dimension":"reasoning","stimulus":"A smoker has persistent dysphonia and mild odynophagia.","question":"What should change your threshold for visualization?","answer":"Risk factors and concerning associated symptoms should accelerate laryngeal visualization rather than prolonged empiric treatment.","why":"The priority is to identify structural, neurologic, inflammatory, or malignant causes."},
{"title":"Visualization","dimension":"workup","stimulus":"The voice remains abnormal.","question":"Why is laryngoscopy central before treatment such as voice therapy for an unexplained persistent problem?","answer":"Visualization establishes the laryngeal diagnosis/mechanism and prevents treatment of an unseen lesion or mobility disorder.","why":"Dysphonia is a symptom; the laryngeal mechanism determines therapy."},
{"title":"Stroboscopy","dimension":"recognition","stimulus":"A small lesion is seen but vibratory behavior is uncertain.","question":"What additional information can stroboscopy add?","answer":"Mucosal wave, amplitude, periodicity, symmetry, closure pattern, and the lesion's effect on vibration.","why":"Static appearance and vibratory function are different layers of diagnosis."},
{"title":"Mechanism","dimension":"localization","stimulus":"One vocal fold is immobile.","question":"What must you now localize?","answer":"Whether the problem is neurogenic versus mechanical and, if neurogenic, the lesion level along the vagus/RLN pathway based on history, examination, and appropriate imaging/workup.","why":"'Paralyzed cord' is a finding; localization determines etiology and next steps."},
{"title":"Management","dimension":"management","stimulus":"The cause is established.","question":"How should treatment be chosen?","answer":"Match treatment to mechanism, functional demand, prognosis, airway/swallow status, and patient goals rather than treating every dysphonic patient with the same medication or procedure.","why":"Voice outcomes depend on solving the actual physiologic problem."},
{"title":"Teach Your Junior","dimension":"teaching","stimulus":"A junior prescribes empiric reflux medication for every hoarse patient.","question":"What do you teach?","answer":"Dysphonia is not synonymous with reflux. Use history and laryngeal visualization to establish a plausible cause before committing to prolonged empiric therapy.","why":"A symptom-based prescription can delay the real diagnosis."}
]},
{
"id":"integrated-epistaxis","title":"Epistaxis → Source Control → Escalation",
"domain":"Rhinology","concept_id":"epistaxis",
"summary":"Control bleeding systematically, identify the source, account for anticoagulation, and know when to escalate.",
"source_basis":["AAO-HNSF Clinical Practice Guideline: Nosebleed (Epistaxis, 2020)"],
"stages":[
{"title":"Immediate control","dimension":"management","stimulus":"An adult presents with active anterior nasal bleeding but is hemodynamically stable.","question":"What is the first procedural principle?","answer":"Use firm sustained compression of the lower nose while assessing severity and preparing visualization/source-directed treatment.","why":"Simple mechanical control is the first step for many anterior bleeds."},
{"title":"Visualization","dimension":"workup","stimulus":"Bleeding slows.","question":"What should you do before blindly cauterizing a large area?","answer":"Clear clot as appropriate, use topical vasoconstriction/anesthesia when appropriate, and identify the bleeding site for focused treatment.","why":"Source-directed treatment is more effective and avoids unnecessary tissue injury."},
{"title":"Medication context","dimension":"reasoning","stimulus":"The patient takes an anticoagulant.","question":"Should that fact replace local control?","answer":"No. Assess severity and thrombotic/bleeding context while pursuing appropriate local hemostatic measures; medication reversal/interruption decisions are individualized.","why":"Anticoagulation changes risk but does not eliminate the need to treat the nose."},
{"title":"Recurrent bleed","dimension":"workup","stimulus":"The patient has recurrent unilateral epistaxis despite prior treatment.","question":"What should the next evaluation consider?","answer":"Nasal endoscopy and evaluation for a persistent source or underlying lesion, especially when the pattern is unilateral/recurrent or otherwise atypical.","why":"Repeated bleeding can be a symptom of focal pathology."},
{"title":"Escalation","dimension":"management","stimulus":"Packing and appropriate local measures fail.","question":"What is the escalation concept?","answer":"Escalate to definitive arterial control strategies such as endoscopic surgical ligation or endovascular treatment based on the clinical setting and expertise.","why":"Persistent bleeding after appropriate first-line treatment is an anatomic vascular-control problem."},
{"title":"Teach Your Junior","dimension":"teaching","stimulus":"A junior wants to cauterize both sides of the septum broadly.","question":"What principle do you teach?","answer":"Identify and treat the bleeding source precisely; avoid excessive bilateral septal injury that can increase tissue damage and perforation risk.","why":"Hemostasis should be targeted, not indiscriminate."}
]},
{
"id":"integrated-tonsil","title":"Pediatric SDB → PSG Decision → Tonsillectomy Safety",
"domain":"Pediatric Otolaryngology / Sleep","concept_id":"pediatric_tonsillectomy",
"summary":"Move from symptoms to indication, decide when PSG adds value, and plan safe perioperative management.",
"source_basis":["AAO-HNSF Clinical Practice Guideline: Tonsillectomy in Children (Update, 2019)","Current ENT Mastery pediatric tonsillectomy evidence curriculum"],
"stages":[
{"title":"Indication","dimension":"reasoning","stimulus":"A 7-year-old has nightly snoring, witnessed obstruction, restless sleep, and enlarged tonsils.","question":"What clinical question comes before 'take the tonsils out'?","answer":"Define the sleep-disordered breathing/OSA phenotype, severity/risk, comorbidities, and whether adenotonsillar disease plausibly contributes.","why":"Surgery should solve a defined clinical problem."},
{"title":"PSG decision","dimension":"workup","stimulus":"Symptoms and examination do not align cleanly.","question":"When is PSG particularly useful?","answer":"When diagnostic/severity uncertainty would change the decision, when symptoms and examination are discordant, or in children with risk factors for whom objective severity informs perioperative planning.","why":"PSG is most valuable when it changes confidence or management."},
{"title":"Counseling","dimension":"management","stimulus":"OSA is confirmed and adenotonsillectomy is planned.","question":"What expectation should families hear?","answer":"Tonsillectomy can improve obstructive symptoms, but sleep-disordered breathing may persist or recur, especially in higher-risk children.","why":"Surgery is effective but not a universal physiologic cure."},
{"title":"Analgesia","dimension":"management","stimulus":"You are writing the postoperative plan.","question":"What is the modern analgesic principle?","answer":"Use multimodal non-opioid analgesia, including acetaminophen and ibuprofen when appropriate, and avoid codeine in children after tonsillectomy.","why":"Pain control and opioid-related safety are both quality targets."},
{"title":"Monitoring","dimension":"management","stimulus":"The child has severe OSA/high-risk features.","question":"Why might postoperative disposition differ?","answer":"Higher-risk children have greater risk of postoperative respiratory events and may require planned inpatient monitoring based on age, PSG severity, comorbidity, and clinical context.","why":"Disposition is part of the operation's safety plan."},
{"title":"Teach Your Junior","dimension":"teaching","stimulus":"A junior says, 'Big tonsils plus snoring equals uncomplicated outpatient T&A.'","question":"What is missing?","answer":"You still need the severity/risk phenotype, relevant comorbidities, whether PSG would change management, analgesic planning, and postoperative monitoring strategy.","why":"The operation is only one part of quality tonsillectomy care."}
]}
]

# Preserve original three and append only once.
_existing_ids = {x["id"] for x in INTEGRATED_CASES}
INTEGRATED_CASES.extend([x for x in INTEGRATED_CASES_V41 if x["id"] not in _existing_ids])

# Broaden Attending Mode with distinct questions across domains and levels.
ATTENDING_LEVEL_PROMPTS["junior"].extend([
{"domain":"Otology","concept_id":"ssnhl","prompt":"A patient says one ear suddenly feels blocked. What bedside distinction must you make before calling it ETD?","answer":"Determine whether the hearing loss is conductive or sensorineural; sudden SNHL changes urgency."},
{"domain":"Vestibular","concept_id":"bppv","prompt":"What feature of the history makes BPPV a mechanics problem rather than a chronic dizziness label?","answer":"Brief, position-triggered episodes that can be localized with positional testing."},
{"domain":"Head & Neck Oncology","concept_id":"adult_neck_mass","prompt":"Why is a persistent adult neck mass different from a child with a reactive node?","answer":"In an adult, persistence without a convincing infectious explanation raises malignancy risk and requires diagnostic evaluation."},
{"domain":"Rhinology","concept_id":"epistaxis","prompt":"Where should your fingers actually compress for first-line control of a typical anterior nosebleed?","answer":"Compress the soft lower third/alae firmly against the septum, not the nasal bones."}
])
ATTENDING_LEVEL_PROMPTS["resident"].extend([
{"domain":"Otology","concept_id":"cholesteatoma","prompt":"Why can a tiny attic abnormality represent a large disease burden?","answer":"Cholesteatoma can extend through epitympanic/mastoid and petrous spaces beyond what is visible otoscopically; symptoms, hearing, and imaging define the rest of the disease."},
{"domain":"Pediatric Otolaryngology","concept_id":"tympanostomy_tubes","prompt":"Why is recurrent AOM not just an infection-count problem?","answer":"Tube benefit depends on the verified phenotype, middle-ear effusion status, hearing impact, developmental risk, and shared decision-making."},
{"domain":"Laryngology","concept_id":"dysphonia","prompt":"What is wrong with treating persistent dysphonia empirically before visualizing the larynx?","answer":"Dysphonia is a symptom with structural, neurologic, inflammatory, functional, and malignant causes; visualization establishes mechanism and avoids diagnostic delay."},
{"domain":"Otology / Vestibular","concept_id":"meniere","prompt":"Why must vestibular migraine stay in the differential for suspected Ménière disease?","answer":"The syndromes can overlap in episodic vertigo and sensory symptoms, so timing, auditory findings, migraine features, and longitudinal pattern are needed to avoid premature closure."}
])
ATTENDING_LEVEL_PROMPTS["senior"].extend([
{"domain":"Otology / Skull Base","concept_id":"retrotympanic_mass","prompt":"Why can an office biopsy of an aural polyp be a major error?","answer":"Some apparent polyps represent vascular or skull-base lesions; imaging/anatomic definition should precede tissue sampling when those possibilities exist."},
{"domain":"Pediatric Otolaryngology / Sleep","concept_id":"pediatric_tonsillectomy","prompt":"What information changes postoperative disposition after pediatric tonsillectomy for OSA?","answer":"Age, PSG severity/oxygenation, comorbidities, airway risk, postoperative course, and local monitoring criteria."},
{"domain":"Rhinology","concept_id":"epistaxis","prompt":"When does epistaxis stop being a packing problem and become an arterial-control problem?","answer":"When appropriate local/source-directed measures and packing fail or the bleeding pattern/localization warrants definitive surgical or endovascular control."},
{"domain":"Head & Neck Oncology","concept_id":"adult_neck_mass","prompt":"Why can an unplanned open biopsy of a cervical node create downstream oncologic problems?","answer":"It can disrupt tissue planes and complicate definitive neck management; FNA is generally preferred for initial sampling when appropriate."}
])
ATTENDING_LEVEL_PROMPTS["chief"].extend([
{"domain":"Otology","concept_id":"ssnhl","prompt":"Teach a junior why a normal otoscopic exam in sudden hearing loss is not reassuring enough.","answer":"A normal tympanic membrane removes some conductive explanations but does not test cochlear or retrocochlear function. The urgent branch point is conductive versus sensorineural loss, established with hearing assessment/audiometry."},
{"domain":"Otology","concept_id":"cholesteatoma","prompt":"A resident asks for the 'cholesteatoma operation.' Why is that the wrong question?","answer":"There is no single operation independent of extent, anatomy, hearing, complications, prior surgery, disease-clearance goals, reconstruction, and surveillance strategy."},
{"domain":"Head & Neck Oncology","concept_id":"adult_neck_mass","prompt":"Teach the diagnostic sequence for a persistent adult lateral neck mass without turning it into a memorized checklist.","answer":"First decide malignancy risk; then search for the primary and define nodal anatomy with targeted examination/imaging; obtain tissue in a way that preserves definitive oncologic options; continue until a diagnosis is established."},
{"domain":"Pediatric Otolaryngology","concept_id":"tympanostomy_tubes","prompt":"Teach why the same bilateral effusion can justify different management in two children.","answer":"Duration, hearing impact, symptoms, developmental/speech-language risk, recurrence pattern, age, and family priorities change the expected benefit of intervention."}
])


# =============================================================================
# ENT Mastery v4.2 — Deep Content Expansion
# =============================================================================

INTEGRATED_CASES_V42 = [
{
"id":"integrated-crs-fess","title":"CRS → CT Map → Endoscopic Sinus Surgery",
"domain":"Rhinology / FESS","concept_id":"crs_fess",
"summary":"Confirm CRS objectively, decide when surgery adds value, then translate CT anatomy into a safe ethmoidectomy map.",
"source_basis":["AAO-HNSF Adult Sinusitis Update (2025)","AAO-HNSF Surgical Management of Chronic Rhinosinusitis (2025)","Operative Otolaryngology — ethmoidectomy landmarks"],
"stages":[
{"title":"Diagnosis","dimension":"reasoning","stimulus":"An adult reports >12 weeks of nasal obstruction, discolored drainage, facial pressure, and reduced smell.","question":"What separates a CRS syndrome from recurrent short viral episodes?","answer":"Use duration plus the characteristic symptom pattern, then seek objective evidence of sinonasal inflammation rather than relying on symptoms alone.","why":"CRS is a chronic inflammatory disease phenotype that should be objectively confirmed before committing to long-term or surgical treatment."},
{"title":"Objective confirmation","dimension":"workup","stimulus":"Symptoms remain persistent despite appropriate initial medical management.","question":"What objective tools help confirm disease and define the phenotype?","answer":"Nasal endoscopy and/or CT can document inflammation, polyps, drainage pathways, and anatomic disease relevant to treatment planning.","why":"Objective confirmation prevents operating on symptoms that may come from another diagnosis."},
{"title":"Surgical candidacy","dimension":"management","stimulus":"The patient has persistent quality-of-life-limiting CRS despite appropriate therapy and elects surgery.","question":"What should the preoperative conversation include besides 'you need FESS'?","answer":"Discuss expected symptom goals, the fact that surgery is usually part of long-term disease management rather than a permanent cure, alternatives, extent of planned surgery, postoperative topical therapy/debridement expectations, and phenotype-specific recurrence risk.","why":"The 2025 surgical CRS guideline emphasizes shared decision-making and expectation setting around ESS."},
{"title":"CT map","dimension":"localization","stimulus":"You review the sinus CT before entering the OR.","question":"Which hazard relationships must be mentally mapped before ethmoidectomy?","answer":"Orbit/lamina papyracea, skull base/lateral lamella, anterior and posterior ethmoid arteries, sphenoid/optic nerve/carotid relationships including Onodi cells, ethmoid height, and any dehiscence or distorted anatomy.","why":"The operative text emphasizes that CT review should identify variations that change the danger map before dissection begins."},
{"title":"Stepwise landmarks","dimension":"operative","stimulus":"The bulla has been entered during ethmoidectomy.","question":"What landmark sequence keeps the dissection spatially organized?","answer":"Identify and preserve the lamina papyracea after bulla removal; recognize the basal lamella as the anterior/posterior ethmoid divider; identify the superior turbinate; then define the posterior skull base and the orbit-skull-base-sphenoid 'corner.'","why":"A reproducible landmark sequence is safer than following diseased cells blindly."},
{"title":"Navigation","dimension":"operative","stimulus":"The case is a revision with extensive polyposis and distorted landmarks.","question":"What is the proper mental model for image guidance?","answer":"Navigation can be helpful when anatomy is distorted or disease approaches critical structures, but it supplements—not replaces—knowledge of CT anatomy and direct surgical landmarks.","why":"Technology should confirm spatial reasoning, not substitute for it."},
{"title":"Teach Your Junior","dimension":"teaching","stimulus":"A junior says, 'I follow the CT navigation dot, so I know where I am.'","question":"What do you teach?","answer":"Know where you are from the anatomy first: lamina laterally, skull base superiorly, basal lamella compartment change, superior turbinate posteriorly. Navigation is a cross-check, not the primary map.","why":"When technology is inaccurate or anatomy changes during surgery, the anatomic mental model is what keeps the patient safe."}
]},
{
"id":"integrated-tympanoplasty","title":"TM Perforation → Audiogram → Tympanoplasty",
"domain":"Otology / Surgery","concept_id":"tympanoplasty",
"summary":"Decide whether a perforation needs surgery, interpret the hearing pattern, and anticipate ossicular and surgical risk.",
"source_basis":["Operative Otolaryngology — Myringoplasty and Tympanoplasty"],
"stages":[
{"title":"Problem definition","dimension":"recognition","stimulus":"A patient has a chronic dry tympanic membrane perforation with intermittent water-triggered otorrhea.","question":"What are the major reasons to consider repair?","answer":"Common goals include creating a safe water-tolerant ear, reducing recurrent otorrhea/infection, and improving a conductive hearing deficit when appropriate.","why":"The operation should be tied to a functional or disease-control goal."},
{"title":"Audiogram","dimension":"reasoning","stimulus":"A small perforation has a 40-dB conductive hearing loss.","question":"Why should that make you suspicious?","answer":"A small perforation alone may not explain that degree of conductive loss; consider ossicular discontinuity or fixation and anticipate possible ossicular reconstruction.","why":"The operative source specifically warns that hearing loss disproportionate to perforation size should change planning."},
{"title":"Imaging","dimension":"workup","stimulus":"The ear is otherwise uncomplicated and there is no cholesteatoma concern.","question":"Is temporal-bone CT routine before simple tympanoplasty?","answer":"No. CT is generally reserved for a specific question such as cholesteatoma, mastoid disease, or anatomy that would change the operation.","why":"Imaging should answer a planning question rather than be automatic."},
{"title":"Mixed loss","dimension":"management","stimulus":"The audiogram instead shows a substantial sensorineural component.","question":"What counseling changes?","answer":"Closing the air-bone gap cannot restore the sensorineural component. Discuss realistic hearing goals and whether amplification may still be needed even after technically successful repair.","why":"Anatomic repair and hearing rehabilitation are related but not identical outcomes."},
{"title":"Risk","dimension":"operative","stimulus":"You consent the patient for tympanoplasty.","question":"Which functional structures must be explicitly in your mental danger map?","answer":"Ossicular chain, chorda tympani/taste, facial nerve, inner ear/hearing, and the graft/ear-canal blood supply, with approach-specific soft-tissue risks.","why":"The operative source highlights hearing loss, vertigo, taste change, facial weakness, infection, and graft failure among important risks."},
{"title":"Teach Your Junior","dimension":"teaching","stimulus":"A junior says, 'The perforation closed, so the operation succeeded.'","question":"What is missing?","answer":"Success includes a durable safe ear and the intended functional outcome; hearing can remain limited by ossicular or sensorineural disease even when the graft heals.","why":"Technical closure is one endpoint, not the whole patient's outcome."}
]},
{
"id":"integrated-laryngomalacia","title":"Infant Stridor → Laryngomalacia → Supraglottoplasty",
"domain":"Pediatric Airway","concept_id":"laryngomalacia",
"summary":"Recognize dynamic supraglottic collapse, distinguish mild disease from physiologic compromise, and select surgery for the right patient.",
"source_basis":["Operative Otolaryngology — pediatric laryngomalacia/supraglottoplasty"],
"stages":[
{"title":"Pattern","dimension":"recognition","stimulus":"A 2-month-old has inspiratory stridor that worsens with feeding and agitation.","question":"What anatomic mechanism should be high on the list?","answer":"Dynamic supraglottic collapse from laryngomalacia is a common consideration, but the airway must be visualized and the child assessed for other/synchronous lesions when indicated.","why":"Stridor tells you airflow is abnormal; flexible laryngoscopy localizes the dynamic mechanism."},
{"title":"Severity","dimension":"reasoning","stimulus":"The infant is gaining weight well and has no cyanosis, apnea, or significant feeding compromise.","question":"Does the sound alone mandate surgery?","answer":"No. Many infants with uncomplicated laryngomalacia can be observed with feeding/growth and respiratory monitoring.","why":"Treat physiologic compromise, not decibels of stridor."},
{"title":"Escalation","dimension":"management","stimulus":"The infant instead has poor weight gain, feeding difficulty, retractions, and recurrent oxygen desaturation.","question":"Why does the treatment threshold change?","answer":"These findings suggest clinically significant airway/feeding burden and make operative intervention such as supraglottoplasty more appropriate after complete evaluation.","why":"Surgery is aimed at meaningful obstruction and its consequences."},
{"title":"Endoscopy","dimension":"workup","stimulus":"Surgery is being considered.","question":"Why might a complete airway evaluation matter?","answer":"Severe or atypical disease can coexist with other airway lesions; define the dynamic supraglottic anatomy and identify synchronous pathology that could limit surgical success.","why":"A single visible supraglottic abnormality may not explain the entire airway."},
{"title":"Operation","dimension":"operative","stimulus":"Supraglottoplasty is planned.","question":"What is the operative concept rather than one rigid recipe?","answer":"Relieve the specific collapsing supraglottic components—often shortened aryepiglottic folds and/or redundant arytenoid mucosa—while preserving enough tissue and sensation to avoid aspiration, scarring, and supraglottic stenosis.","why":"The operation should match the phenotype of collapse and balance airway opening against swallowing protection."},
{"title":"Teach Your Junior","dimension":"teaching","stimulus":"A junior wants to operate because the stridor sounds dramatic.","question":"What do you teach?","answer":"Laryngomalacia severity is defined by physiologic consequences—feeding, growth, work of breathing, apnea/cyanosis, hypoxemia—not by sound alone.","why":"Clinical impact, not noise, determines escalation."}
]},
{
"id":"integrated-peds-sgs","title":"Pediatric SGS → Endoscopy → Reconstruction Strategy",
"domain":"Pediatric Airway","concept_id":"pediatric_sgs",
"summary":"Describe stenosis completely, find synchronous lesions, and choose between endoscopic, expansion, and resection strategies.",
"source_basis":["Operative Otolaryngology — pediatric SGS/LTR","Operative Techniques in Laryngology (2024) — LTR and CTR"],
"stages":[
{"title":"Endoscopy","dimension":"workup","stimulus":"A child with prior prolonged intubation has persistent biphasic stridor.","question":"What is required before calling this an isolated SGS?","answer":"Diagnostic airway endoscopy to define location, severity, length, morphology, mobility, and synchronous lesions.","why":"The operative source explicitly states that airway endoscopy is required to assess SGS and identify synchronous lesions."},
{"title":"Description","dimension":"recognition","stimulus":"Endoscopy shows subglottic narrowing.","question":"What information matters beyond Cotton-Myer grade?","answer":"Length, mature versus inflamed tissue, concentric versus eccentric geometry, posterior/glottic involvement, cartilage framework, tracheal extension, vocal-fold mobility, and prior airway procedures.","why":"Grade alone cannot choose the operation."},
{"title":"Endoscopic candidate","dimension":"management","stimulus":"The lesion is mild, short, and favorable in geometry.","question":"What category of treatment can be reasonable?","answer":"An endoscopic approach may be reasonable for selected mild/focal disease, with technique chosen to the lesion and prior response.","why":"Less structural disease can often be managed without sacrificing airway framework."},
{"title":"Expansion vs resection","dimension":"operative","stimulus":"The stenosis is severe and mature with major framework compromise.","question":"What is the conceptual difference between LTR and CTR?","answer":"LTR expands/reconstructs the airway framework, often with grafting; CTR removes a diseased segment and re-anastomoses healthy airway. Selection depends on stenosis severity, length, framework, vocal-fold proximity, prior reconstruction, and patient factors.","why":"The 2024 laryngology text emphasizes that severe grade 3/4 disease and failed prior reconstruction may favor CTR, while proximity to the vocal folds or framework considerations can favor expansion."},
{"title":"Functional tradeoff","dimension":"operative","stimulus":"You are planning open reconstruction.","question":"What outcome must never be reduced to 'bigger airway'?","answer":"Airway expansion must be balanced against voice and swallowing/airway protection; a technically larger lumen is not a complete success if dysphonia or dysphagia is unacceptable.","why":"The pediatric operative text explicitly frames airway surgery around all three laryngeal functions."},
{"title":"Teach Your Junior","dimension":"teaching","stimulus":"A junior asks, 'What operation is used for grade III SGS?'","question":"How do you answer without giving a misleading one-line rule?","answer":"Grade is only one variable. First define length, level, framework, glottic/posterior involvement, mobility, prior procedures, inflammation, and patient factors; those decide whether endoscopic treatment, LTR, or resection is appropriate.","why":"Procedure selection is anatomy plus biology plus history—not a lookup table."}
]},
{
"id":"integrated-presbycusis","title":"Older Adult Hearing Loss → Audiogram → Rehabilitation",
"domain":"Audiology / Otology","concept_id":"age_related_hearing_loss",
"summary":"Recognize common age-related patterns while looking for asymmetry, functional impact, and opportunities for rehabilitation.",
"source_basis":["AAO-HNSF Clinical Practice Guideline: Age-Related Hearing Loss (2024)","Pasha Clinical Reference Guide — presbycusis patterns"],
"stages":[
{"title":"Recognition","dimension":"recognition","stimulus":"A 72-year-old reports gradually worsening speech understanding, especially in noise. Audiogram shows bilateral symmetric high-frequency SNHL.","question":"What common diagnosis fits the pattern?","answer":"Age-related hearing loss is a common explanation when the history and symmetric audiogram fit and no better cause is evident.","why":"The pattern is common, but the clinician still needs to look for asymmetry, otologic disease, and functional consequences."},
{"title":"Functional impact","dimension":"reasoning","stimulus":"Pure-tone thresholds are only part of the story.","question":"What domains should be assessed in addition to the audiogram?","answer":"Communication difficulty, speech understanding, social isolation, safety/function, patient goals, and the impact on family/care partners.","why":"The 2024 guideline treats hearing loss as a health and communication problem, not just a threshold graph."},
{"title":"Asymmetry","dimension":"workup","stimulus":"One ear has unexpectedly poorer word recognition and asymmetric thresholds.","question":"Why should that interrupt the simple 'presbycusis' label?","answer":"Clinically important asymmetry or disproportionate speech discrimination can suggest another process and may warrant otologic/retrocochlear evaluation.","why":"A common diagnosis should not erase red flags."},
{"title":"Rehabilitation","dimension":"management","stimulus":"The patient is motivated to improve communication.","question":"What is the treatment concept?","answer":"Offer evidence-based hearing rehabilitation matched to severity and goals, including hearing aids/assistive technology and communication strategies, with implant evaluation when hearing is severe enough and benefit from conventional amplification is inadequate.","why":"Untreated hearing loss is not an inevitable consequence of aging that must simply be accepted."},
{"title":"Verification","dimension":"management","stimulus":"The patient receives amplification.","question":"Why is follow-up important?","answer":"Benefit, fit, communication function, and device use should be assessed and adjusted rather than assuming that dispensing a device completes treatment.","why":"Rehabilitation is an iterative process."},
{"title":"Teach Your Junior","dimension":"teaching","stimulus":"A junior says, 'They're old, so this audiogram is expected.'","question":"What do you teach?","answer":"Age-related loss is common, but still evaluate functional burden and red flags, then offer rehabilitation. 'Expected with aging' is not the same as 'nothing to do.'","why":"Normalization of age-related disability can lead to undertreatment."}
]},
{
"id":"integrated-salivary-path","title":"Parotid Mass → FNA → Pathology Features → Surgical Planning",
"domain":"Head & Neck / Pathology","concept_id":"salivary_gland_mass",
"summary":"Use pathology as a surgical decision tool: architecture and grade matter because facial nerve, neck, margins, and adjuvant treatment may change.",
"source_basis":["Bluestone & Stool — salivary neoplasm prognostic features","Current ENT Mastery Pathology Lab"],
"stages":[
{"title":"Presentation","dimension":"reasoning","stimulus":"A patient has a slowly enlarging parotid mass with no facial weakness.","question":"What broad categories should frame the initial differential?","answer":"Benign epithelial tumor, malignant salivary neoplasm, lymphoid disease, inflammatory lesion, and metastatic/intraparotid nodal disease, with age and clinical features refining probability.","why":"A parotid mass is not synonymous with pleomorphic adenoma."},
{"title":"Tissue","dimension":"workup","stimulus":"Imaging shows a discrete parotid lesion.","question":"What is the goal of preoperative tissue sampling?","answer":"Obtain a cytologic/pathologic diagnosis or risk stratification that can change extent of surgery, counseling, facial nerve planning, neck management, and the need for additional imaging.","why":"Pathology is useful when it changes the operation."},
{"title":"Pathology","dimension":"recognition","stimulus":"The report describes a malignant salivary tumor with perineural invasion and high-grade features.","question":"Why are these more than pathology buzzwords?","answer":"High grade and perineural invasion are adverse features associated with more aggressive biology and can affect surgical extent, nerve evaluation, nodal/adjuvant treatment discussions, and prognosis.","why":"Bluestone specifically identifies high grade, PNI, extraglandular extension, vascular/lymphatic spread, and nodal metastasis as poor prognostic features in pediatric salivary malignancy; the same concepts are central in adult salivary oncology."},
{"title":"Facial nerve","dimension":"operative","stimulus":"The patient has normal preoperative facial function despite malignancy.","question":"What is the guiding surgical principle?","answer":"Plan oncologic clearance while preserving a functioning uninvolved facial nerve when oncologically appropriate; suspected/direct nerve invasion changes counseling and reconstructive planning.","why":"The nerve is both a functional structure and a potential route/site of tumor involvement."},
{"title":"Neck / adjuvant","dimension":"management","stimulus":"The tumor is high grade with adverse features.","question":"What additional management domains need discussion?","answer":"Nodal risk/neck management, margin status, perineural spread, and indications for postoperative radiation or multidisciplinary therapy based on final histology and stage.","why":"Salivary cancer care is not completed by removing the primary gland."},
{"title":"Teach Your Junior","dimension":"teaching","stimulus":"A junior asks why they need to care whether a salivary tumor is low grade or high grade before surgery.","question":"Answer in one framework.","answer":"Grade predicts biology and therefore changes how aggressively you think about margins, nerve involvement, the neck, imaging for spread, adjuvant therapy, and prognosis.","why":"Pathology should alter decisions, not just label the specimen."}
]}
]

_v42_ids={x["id"] for x in INTEGRATED_CASES}
INTEGRATED_CASES.extend([x for x in INTEGRATED_CASES_V42 if x["id"] not in _v42_ids])

# Audited OR Tomorrow modules (high-level educational prep, not patient-specific instructions).
OR_PREP_REGISTRY.update({
"endoscopic-sinus-surgery":{
 "slug":"endoscopic-sinus-surgery","title":"Endoscopic Sinus Surgery / Ethmoidectomy","domain":"Rhinology",
 "indications":"CRS or other sinonasal disease in appropriately selected patients when surgery is expected to improve disease control, symptoms, access for topical therapy, or complications after diagnosis/phenotype and alternatives have been established.",
 "steps":["Review CT in axial/coronal/sagittal planes and identify skull base, lamina, ethmoid arteries, sphenoid, optic/carotid relationships and variants.",
          "Achieve endoscopic orientation and preserve the middle turbinate as a key landmark when possible.",
          "Perform disease-appropriate uncinectomy/maxillary work; identify the natural maxillary drainage pathway rather than following accessory openings blindly.",
          "Identify the ethmoid bulla; after entering/removing it, identify and preserve the lamina papyracea.",
          "Recognize and traverse the basal lamella into the posterior ethmoid compartment when indicated.",
          "Identify superior turbinate, posterior skull base, sphenoid face, and the orbit-skull-base-sphenoid corner.",
          "Complete the planned extent of surgery while preserving mucosa/critical structures and creating an accessible postoperative cavity for topical therapy and surveillance."],
 "danger":["Lamina papyracea/orbit","Skull base/lateral lamella","Anterior/posterior ethmoid arteries","Optic nerve","Internal carotid artery","Onodi cell anatomy","Middle turbinate destabilization"],
 "attending_followup":[
   ["Why study the CT before FESS?","Because patient-specific variants and disease alter the relationship of the orbit, skull base, ethmoid arteries, sphenoid, optic nerve and carotid; imaging is the preoperative 3-D map."],
   ["What does the basal lamella tell you?","It is the key divider between anterior and posterior ethmoid compartments and marks a meaningful change in the surgical map."],
   ["Does navigation replace anatomy?","No. It can be valuable in revision/distorted/high-risk cases but is a cross-check for anatomic reasoning, not a substitute."]
 ],"linked_topic":"sinonasal-endoscopy","status":"audited"
},
"tympanostomy-tubes":{
 "slug":"tympanostomy-tubes","title":"Myringotomy with Tympanostomy Tube Placement","domain":"Pediatric Otolaryngology",
 "indications":"Selected children with chronic OME/hearing or symptom burden, recurrent AOM with the appropriate middle-ear phenotype, or other guideline-supported indications after age, hearing, developmental risk and disease course are considered.",
 "steps":["Confirm indication, laterality, hearing/effusion history, and current ear examination.",
          "Visualize the tympanic membrane under microscope/endoscope and clear obstructing cerumen.",
          "Create a controlled myringotomy in an appropriate quadrant while avoiding ossicles and annulus.",
          "Suction middle-ear fluid when present and place the ventilation tube securely in the incision.",
          "Confirm tube patency/position and provide postoperative counseling regarding otorrhea, follow-up, and expected extrusion."],
 "danger":["Ossicular injury","Persistent perforation","Tympanosclerosis","Premature extrusion or retained tube","Otorrhea","Canal/TM trauma"],
 "attending_followup":[
   ["Why isn't recurrent AOM just an infection-count rule?","Because current effusion status, hearing, developmental risk, diagnostic certainty and expected benefit matter."],
   ["How do you treat uncomplicated acute tube otorrhea?","Topical antibiotic ear drops are generally preferred over routine systemic antibiotics."],
   ["Why does hearing testing matter before tubes?","It establishes functional impact and can uncover hearing loss that is not explained by transient middle-ear fluid."]
 ],"linked_topic":"tympanostomy_tubes","status":"audited"
},
"tonsillectomy-adenoidectomy":{
 "slug":"tonsillectomy-adenoidectomy","title":"Pediatric Tonsillectomy ± Adenoidectomy","domain":"Pediatric Otolaryngology / Sleep",
 "indications":"Appropriate recurrent throat infection or obstructive sleep-disordered breathing/OSA indications after guideline-based assessment, modifying factors, comorbidities, and shared decision-making.",
 "steps":["Confirm indication, bleeding/anesthesia risk, sleep severity, comorbidities and postoperative disposition plan.",
          "Expose the oropharynx while protecting teeth/lips/tongue and identify tonsillar pillars and capsule.",
          "Perform the planned tonsil technique with controlled dissection/hemostasis while minimizing unnecessary thermal/deep tissue injury.",
          "Assess the adenoid pad/nasopharynx and perform adenoidectomy when indicated while respecting the Eustachian tube orifices and velopharyngeal anatomy.",
          "Achieve meticulous hemostasis, reassess the operative bed after releasing suspension, and execute the planned multimodal analgesia/airway monitoring strategy."],
 "danger":["Post-tonsillectomy hemorrhage","Airway obstruction/respiratory event","Dehydration/pain","Dental/lip/tongue injury","Velopharyngeal insufficiency risk","Eustachian tube injury during adenoidectomy"],
 "attending_followup":[
   ["What changes postoperative monitoring?","Young age, severe PSG abnormalities/oxygenation, comorbidities and other airway/clinical risk factors can justify planned inpatient monitoring."],
   ["What is the analgesic principle?","Use multimodal non-opioid analgesia such as acetaminophen/ibuprofen when appropriate and avoid codeine after pediatric tonsillectomy."],
   ["Why can SDB persist after adenotonsillectomy?","Obstruction is multifactorial; obesity, craniofacial/neuromuscular factors and non-adenotonsillar collapse can persist."]
 ],"linked_topic":"pediatric_tonsillectomy","status":"audited"
},
"tympanoplasty":{
 "slug":"tympanoplasty","title":"Myringoplasty / Tympanoplasty","domain":"Otology",
 "indications":"Repair of a persistent tympanic membrane perforation to create a safer/drier ear, reduce recurrent otorrhea, and/or improve conductive hearing when the anatomy and hearing goals support surgery.",
 "steps":["Review otoscopy, audiogram and disease status; decide whether imaging or mastoid evaluation is needed for a specific concern.",
          "Choose transcanal/endaural/postauricular exposure based on perforation/anatomy and planned work.",
          "Elevate the tympanomeatal flap while protecting canal skin, annulus and chorda tympani.",
          "Inspect middle ear and ossicular chain; address pathology or ossicular reconstruction when indicated.",
          "Prepare perforation edges and place the selected graft with stable support and appropriate middle-ear/canal packing.",
          "Return flap/canal skin to position and confirm graft stability."],
 "danger":["Chorda tympani/taste","Ossicular chain","Facial nerve","Inner ear/hearing","Persistent perforation/graft failure","Canal stenosis/skin injury"],
 "attending_followup":[
   ["Why can a small perforation with a 40-dB ABG be important?","The hearing loss may be disproportionate to the perforation and should raise concern for ossicular discontinuity or fixation."],
   ["Is CT routine before uncomplicated tympanoplasty?","No. Use it when there is a specific concern such as cholesteatoma or mastoid/anatomic disease that changes planning."],
   ["What do you tell a patient with mixed loss?","Closing the conductive gap cannot restore the sensorineural component, so amplification may still be needed."]
 ],"linked_topic":"tympanoplasty","status":"audited"
},
"direct-laryngoscopy-bronchoscopy":{
 "slug":"direct-laryngoscopy-bronchoscopy","title":"Direct Laryngoscopy & Bronchoscopy / Airway Evaluation","domain":"Pediatric Airway",
 "indications":"Diagnostic or therapeutic evaluation of suspected laryngeal, subglottic, tracheal or bronchial pathology when flexible examination is insufficient or a complete operative airway assessment is required.",
 "steps":["Review symptoms, prior airway history/imaging, anesthesia plan, airway contingency and required scopes/instruments.",
          "Expose the larynx atraumatically while protecting teeth/lips and document supraglottic/glottic anatomy and vocal fold mobility when assessable.",
          "Inspect posterior glottis, subglottis and cricoid; document stenosis level, length, morphology and sizing when relevant.",
          "Pass through trachea to carina and mainstem bronchi when indicated, assessing fixed vs dynamic pathology and synchronous lesions.",
          "Photograph/document key findings and measurements in a reproducible format that can guide future intervention."],
 "danger":["Loss of airway","Dental/lip injury","Laryngospasm/bronchospasm","Airway edema/trauma","Bleeding","Failure to identify synchronous lesions"],
 "attending_followup":[
   ["Why isn't Cotton-Myer grade enough?","Treatment also depends on length, level, maturity, geometry, glottic/posterior involvement, mobility, framework and prior procedures."],
   ["Why look for synchronous lesions?","A second airway lesion can explain persistent symptoms and change the success/risk of treating the obvious lesion."],
   ["What is the first priority during any airway endoscopy?","Maintain a safe ventilation/oxygenation strategy and have a rescue plan before pursuing diagnostic completeness."]
 ],"linked_topic":"airway_stenosis","status":"audited"
},
"supraglottoplasty":{
 "slug":"supraglottoplasty","title":"Supraglottoplasty for Severe Laryngomalacia","domain":"Pediatric Airway",
 "indications":"Laryngomalacia with clinically significant physiologic compromise such as failure to thrive, feeding/aspiration burden, hypoxemia/apnea/cyanosis, or severe work of breathing after appropriate airway evaluation.",
 "steps":["Confirm dynamic supraglottic collapse phenotype and assess for synchronous airway lesions/comorbid contributors.",
          "Expose the supraglottis and identify the specific structures contributing to collapse.",
          "Release shortened aryepiglottic folds and/or reduce obstructing redundant supraglottic tissue as indicated by phenotype.",
          "Preserve protective mucosa and avoid excessive bilateral/deep tissue removal that risks aspiration, scarring or supraglottic stenosis.",
          "Reassess airway dynamics and execute postoperative feeding/airway monitoring appropriate to severity and comorbidity."],
 "danger":["Aspiration/swallow dysfunction","Supraglottic stenosis","Bleeding","Airway edema","Persistent obstruction from synchronous lesions","Thermal injury"],
 "attending_followup":[
   ["What makes laryngomalacia 'severe'?","Physiologic consequences—feeding/growth compromise, significant work of breathing, apnea/cyanosis/hypoxemia—not the loudness of stridor alone."],
   ["Why isn't supraglottoplasty one identical operation in every child?","The collapsing supraglottic anatomy varies, so treatment should address the phenotype while preserving swallowing and sensation."],
   ["Why evaluate the rest of the airway?","Synchronous lesions can coexist and may explain symptoms or reduce the benefit of supraglottoplasty."]
 ],"linked_topic":"laryngomalacia","status":"audited"
}
})

# Add more Interpretation Atlas content without fabricating new visual images.
# These are text/data interpretation scenarios anchored to the uploaded audiology/operative material.
_v42_audio = [
{"id":"aud_mixed_v42","level":3,"track":"all","prompt":"Air and bone thresholds are both elevated, but air thresholds remain >10 dB poorer than bone across several frequencies. Classify the loss.","answer":"Mixed hearing loss: a sensorineural component plus an additional conductive air-bone gap.","why":"Both cochlear sensitivity and sound transmission are impaired.","follow":"Why might surgery improve the air-bone gap without normalizing hearing?","follow_answer":"Because the sensorineural component remains even after the conductive component is corrected.","concept_id":"audiology:mixed_loss","variant_type":"interpret"},
{"id":"aud_carhart_v42","level":4,"track":"all","prompt":"An audiogram shows a conductive pattern with a relative dip in bone conduction near 2 kHz. What classic mechanical phenomenon should you remember?","answer":"A Carhart notch can occur with stapes fixation and can mimic a small sensorineural dip at about 2 kHz.","why":"Mechanical changes in ossicular inertial contribution alter the measured bone threshold.","follow":"Does a Carhart notch by itself prove otosclerosis?","follow_answer":"No. It is a supportive audiometric pattern, not a standalone diagnosis; history, exam and the full audiologic pattern matter.","concept_id":"audiology:carhart_notch","variant_type":"interpret"},
{"id":"aud_thirdwindow_v42","level":4,"track":"all","prompt":"A patient has an apparent low-frequency air-bone gap but normal middle-ear mechanics. What non-middle-ear mechanism can create a pseudoconductive pattern?","answer":"A third-window inner-ear disorder such as superior semicircular canal dehiscence can create a pseudoconductive air-bone gap.","why":"Altered inner-ear mechanics can enhance bone-conducted sensitivity and change air-conduction energy flow despite an intact middle ear.","follow":"What other history/testing would help separate third-window physiology from ossicular disease?","follow_answer":"Look for sound/pressure-induced vestibular symptoms, autophony, appropriate vestibular-evoked responses and high-resolution imaging when clinically indicated.","concept_id":"audiology:third_window","variant_type":"interpret"},
{"id":"aud_soundfield_v42","level":3,"track":"all","prompt":"A toddler's behavioral thresholds were obtained only in the sound field and appear normal. Can you conclude both ears are normal?","answer":"No. Sound-field thresholds reflect the better-hearing ear and are not ear-specific.","why":"A unilateral hearing loss can be hidden when both ears have access to the loudspeaker stimulus.","follow":"What is the next goal if ear-specific status matters?","follow_answer":"Obtain ear-specific behavioral or objective data as developmentally feasible using appropriate transducers/tests.","concept_id":"audiology:soundfield_limit","variant_type":"interpret"},
{"id":"aud_presby_v42","level":2,"track":"all","prompt":"A 74-year-old has symmetric bilateral downsloping high-frequency SNHL and difficulty understanding speech in noise. What common phenotype fits?","answer":"Age-related hearing loss/presbycusis is a common fit when no better cause is evident.","why":"The classic pattern is progressive, often symmetric high-frequency sensorineural loss, but functional impact and red flags still matter.","follow":"What finding would make you stop calling it routine presbycusis?","follow_answer":"Clinically important asymmetry, disproportionate word-recognition decline, sudden change, focal neurologic/otologic symptoms, or another unexpected feature should prompt further evaluation.","concept_id":"audiology:presbycusis","variant_type":"interpret"},
{"id":"aud_wordrec_v42","level":4,"track":"all","prompt":"Pure-tone thresholds are similar between ears, but one ear has markedly poorer word recognition than expected. Why is that important?","answer":"Disproportionately poor speech discrimination can raise concern for neural/retrocochlear dysfunction and should not be explained away by the pure-tone graph alone.","why":"Pure-tone detection and speech-processing performance test different aspects of the auditory system.","follow":"What is the broader principle?","follow_answer":"Interpret the audiogram as a battery—thresholds, speech testing, tympanometry/reflexes and clinical context—not as a single line graph.","concept_id":"audiology:word_recognition","variant_type":"interpret"}
]
INTERPRETATION_LABS["audiology"]["cases"].extend(_v42_audio)

_v42_ct = [
{"id":"ct_ethmoid_map_v42","level":3,"track":"all","external":"https://www.openanatomy.org/atlas-pages/atlas-spl-head-and-neck.html","prompt":"Before anterior/posterior ethmoidectomy, identify the two constant danger boundaries and the compartment divider on CT.","answer":"Orbit/lamina papyracea laterally, skull base superiorly, and the basal lamella as the key divider between anterior and posterior ethmoid compartments.","why":"Safe FESS depends on continuously knowing your relationship to lateral and superior boundaries as you cross compartments.","follow":"What does crossing the basal lamella change?","follow_answer":"You have entered the posterior ethmoid compartment, so your relationship to the superior turbinate, sphenoid, posterior skull base and optic/carotid anatomy becomes increasingly important.","concept_id":"ct:fess_landmarks","variant_type":"interpret"},
{"id":"ct_onodi_v42","level":4,"track":"all","prompt":"A posterior ethmoid cell pneumatizes superior/lateral to the sphenoid and closely relates to the optic nerve. Why do you care?","answer":"This is the kind of Onodi-cell relationship that can place the optic nerve in an unexpected posterior ethmoid position and materially increase surgical risk.","why":"Preoperative CT recognition prevents assuming that all optic nerve risk is confined to the sphenoid sinus wall.","follow":"What should image guidance do here?","follow_answer":"It can supplement the map in complex anatomy but does not replace direct landmark recognition and CT understanding.","concept_id":"ct:onodi_cell","variant_type":"interpret"},
{"id":"ct_chol_v42","level":3,"track":"all","prompt":"Temporal-bone CT shows nondependent epitympanic/mastoid soft tissue with focal ossicular/scutal erosion. What process should be high on the list?","answer":"Cholesteatoma is an important consideration when soft tissue is paired with characteristic bony erosion.","why":"CT is especially useful for the bony disease map and complications rather than tissue-specific diagnosis alone.","follow":"What can CT not reliably tell you by itself?","follow_answer":"Soft-tissue identity can be nonspecific; clinical otoscopy, hearing and sometimes diffusion-weighted MRI/operative findings provide complementary information.","concept_id":"ct:cholesteatoma","variant_type":"interpret"},
{"id":"ct_sgs_v42","level":3,"track":"all","prompt":"CT suggests a short narrowed subglottic segment, but a child is being evaluated for reconstruction. Why is CT not enough to plan the operation?","answer":"Airway endoscopy is required to define dynamic versus fixed disease, mucosal maturity, exact length/grade, glottic/posterior involvement, mobility and synchronous lesions.","why":"Cross-sectional imaging cannot replace direct functional/anatomic airway assessment.","follow":"What does the CT still contribute?","follow_answer":"It can add information about framework, extraluminal anatomy, long-segment disease or other structural questions when those are clinically relevant.","concept_id":"ct:airway_stenosis","variant_type":"interpret"},
{"id":"ct_neckspace_v42","level":2,"track":"all","prompt":"A deep neck mass displaces adjacent structures rather than simply 'sitting next to them.' What is the key radiologic reasoning move?","answer":"Use the epicenter and displacement pattern to identify the anatomic space of origin before naming a tumor.","why":"Space localization narrows the differential more reliably than memorizing one density or signal pattern.","follow":"Why does this matter to surgery?","follow_answer":"The space of origin predicts the vessels, nerves, glands and fascial boundaries that define exposure and operative risk.","concept_id":"ct:neck_spaces","variant_type":"interpret"}
]
INTERPRETATION_LABS["ct-mri"]["cases"].extend(_v42_ct)

_v42_path = [
{"id":"path_scc_pni_v42","level":3,"track":"all","prompt":"A head-and-neck SCC pathology report lists perineural invasion and lymphovascular invasion. Why should the surgeon care?","answer":"These are adverse pathologic features that signal routes of spread/recurrence risk and can influence staging discussion, adjuvant therapy planning and surveillance.","why":"The pathology report is a treatment map, not merely a diagnosis line.","follow":"What other report elements commonly change postoperative planning?","follow_answer":"Margins, depth/extent, nodal burden, extranodal extension, grade/subsite-specific features and other disease-specific risk factors.","concept_id":"path:scc_adverse_features","variant_type":"interpret"},
{"id":"path_mucoep_v42","level":3,"track":"all","prompt":"A salivary tumor shows mixed mucous, epidermoid and intermediate cell populations. What diagnostic family should come to mind?","answer":"Mucoepidermoid carcinoma is an important consideration.","why":"Salivary tumors are more memorable when organized by architecture/cell populations than as a list of names.","follow":"Why does grade matter?","follow_answer":"Grade reflects biologic aggressiveness and can change surgical, neck and adjuvant treatment thinking.","concept_id":"path:mucoepidermoid","variant_type":"interpret"},
{"id":"path_pleomorphic_v42","level":2,"track":"all","prompt":"A well-circumscribed salivary tumor has epithelial/myoepithelial elements in a variable myxochondroid stroma. What classic benign tumor fits?","answer":"Pleomorphic adenoma.","why":"The biphasic cellular/stromal architecture is the reusable recognition pattern.","follow":"Why is simple shelling-out a poor surgical mental model?","follow_answer":"Microscopic pseudopods/satellite extensions and capsular violation can contribute to recurrence; surgical technique should respect the tumor and gland/nerve anatomy.","concept_id":"path:pleomorphic_adenoma","variant_type":"interpret"},
{"id":"path_mtc_v42","level":4,"track":"all","prompt":"A thyroid malignancy is associated with calcitonin production and can be hereditary through RET mutations. What tumor is this?","answer":"Medullary thyroid carcinoma.","why":"The diagnosis connects pathology to biochemical surveillance and hereditary evaluation.","follow":"Why does this diagnosis change the family history/genetic workup?","follow_answer":"Hereditary medullary thyroid carcinoma can occur in MEN2/familial syndromes, so germline RET evaluation has implications for the patient and relatives.","concept_id":"path:medullary_thyroid","variant_type":"interpret"},
{"id":"path_salivary_pni_v42","level":4,"track":"all","prompt":"A salivary malignancy tracks conspicuously along nerves with perineural invasion. What should that trigger beyond naming the histology?","answer":"Think about the clinical/radiographic extent of perineural spread, cranial nerve function, margin strategy and adjuvant treatment implications.","why":"Perineural invasion is both a pathologic prognostic feature and an anatomic route of disease spread.","follow":"What imaging question becomes important?","follow_answer":"Whether there is macroscopic perineural spread along named nerves toward skull-base foramina that changes surgical/radiation planning.","concept_id":"path:salivary_pni","variant_type":"interpret"}
]
INTERPRETATION_LABS["pathology"]["cases"].extend(_v42_path)

# Add attending prompts around new operative content
ATTENDING_LEVEL_PROMPTS["resident"].extend([
{"domain":"Rhinology","concept_id":"crs_fess","prompt":"Why isn't a positive sinus CT by itself an indication for FESS?","answer":"Surgery follows a clinical CRS diagnosis/phenotype, objective disease, symptom/QOL burden, treatment history and shared decision-making—not imaging opacity alone."},
{"domain":"Otology","concept_id":"tympanoplasty","prompt":"Why does conductive loss disproportionate to a small TM perforation matter?","answer":"It suggests additional ossicular fixation/discontinuity and changes surgical counseling/planning."},
{"domain":"Pediatric Airway","concept_id":"laryngomalacia","prompt":"What makes laryngomalacia severe enough to consider supraglottoplasty?","answer":"Physiologic consequences such as feeding/growth compromise, significant work of breathing, apnea/cyanosis or hypoxemia—not stridor volume alone."}
])
ATTENDING_LEVEL_PROMPTS["senior"].extend([
{"domain":"Rhinology","concept_id":"fess_landmarks","prompt":"After removing the ethmoid bulla, what landmark do you deliberately identify and preserve before continuing?","answer":"The lamina papyracea/medial orbital wall, then use the basal lamella, superior turbinate and posterior skull-base/sphenoid corner as subsequent orientation landmarks."},
{"domain":"Pediatric Airway","concept_id":"pediatric_sgs","prompt":"Why can a grade III pediatric SGS be an LTR in one child and CTR in another?","answer":"Length, framework, vocal-fold proximity, posterior/glottic involvement, prior reconstruction, inflammation and patient factors determine whether expansion or resection is the better strategy."},
{"domain":"Otology","concept_id":"tympanoplasty","prompt":"Why is graft closure not equivalent to hearing success?","answer":"Ossicular pathology and sensorineural loss can limit hearing even with an intact healed graft."}
])
ATTENDING_LEVEL_PROMPTS["chief"].extend([
{"domain":"Rhinology","concept_id":"fess_landmarks","prompt":"Teach the ethmoidectomy map without using navigation jargon.","answer":"Bulla opens the anterior ethmoid; identify lamina laterally; basal lamella marks the posterior compartment; superior turbinate brings you toward sphenoid; posterior skull base and the orbit-skull-base-sphenoid corner define the safe posterior map."},
{"domain":"Pediatric Airway","concept_id":"pediatric_sgs","prompt":"Teach why airway reconstruction should not be judged only by decannulation.","answer":"The larynx must provide airway, voice and swallowing protection. A larger lumen/decannulation is incomplete success if dysphonia, aspiration or swallowing morbidity is unacceptable."},
{"domain":"Audiology","concept_id":"age_related_hearing_loss","prompt":"Teach why 'expected for age' is not a management plan for presbycusis.","answer":"Age-related hearing loss has functional, communication and health consequences; screen/evaluate red flags and offer rehabilitation rather than normalizing disability."}
])


# =============================================================================
# ENT Mastery v4.3 — Thyroid-first + Rhinology expansion
# Thyroid content prioritizes Monday case preparation.
# =============================================================================
INTEGRATED_CASES_V43 = [
{
"id":"integrated-thyroid-nodule","title":"Thyroid Nodule → US/FNA → Operation Decision",
"domain":"Thyroid / Endocrine Surgery","concept_id":"thyroid_nodule",
"summary":"Move from nodule discovery to risk stratification, tissue diagnosis, extent-of-surgery reasoning, and safe operative planning.",
"source_basis":["2025 ATA Differentiated Thyroid Cancer Guidelines","ENT Mastery endocrine surgery curriculum"],
"stages":[
{"title":"First pass","dimension":"reasoning","stimulus":"An adult is referred with a thyroid nodule discovered on imaging.","question":"What information do you want before deciding that this is a surgical problem?","answer":"Symptoms, thyroid function, high-risk history, neck examination, dedicated thyroid/neck ultrasound features, nodule size and cervical lymph-node findings. FNA decisions follow the sonographic/risk context rather than size alone.","why":"The first task is malignancy and functional risk stratification, not automatically scheduling thyroidectomy."},
{"title":"Voice","dimension":"workup","stimulus":"The patient reports new dysphonia.","question":"Why does that matter before thyroid surgery?","answer":"Preoperative voice change raises concern for vocal-fold dysfunction or invasive disease and should prompt laryngeal evaluation when appropriate; baseline function changes counseling and operative planning.","why":"You need to know whether a nerve deficit preceded the operation."},
{"title":"Cancer extent","dimension":"management","stimulus":"FNA confirms differentiated thyroid carcinoma apparently confined to one lobe, with no gross extrathyroidal extension or clinical nodal disease.","question":"What changed in the modern extent-of-surgery conversation?","answer":"The 2025 ATA framework is more accepting of lobectomy for appropriately selected low-risk unilateral disease; cancers ≤2 cm confined to one lobe without nodal disease or extrathyroidal extension are generally treated with lobectomy, while selected >2–4 cm tumors may be treated with lobectomy or total thyroidectomy using tumor features, contralateral disease and patient preference.","why":"Total thyroidectomy is no longer the automatic answer for every differentiated cancer >1 cm."},
{"title":"Central neck","dimension":"reasoning","stimulus":"The thyroid primary is small and the central neck is clinically negative.","question":"Is prophylactic central neck dissection automatically part of every thyroid cancer operation?","answer":"No. Therapeutic nodal dissection is different from prophylactic dissection; nodal management should reflect clinical disease, primary-tumor risk and the guideline context rather than being automatic.","why":"Additional dissection adds morbidity and should have an oncologic purpose."},
{"title":"Completion","dimension":"management","stimulus":"Final pathology after lobectomy shows differentiated cancer.","question":"Does cancer on final pathology automatically mandate completion thyroidectomy?","answer":"No. The 2025 ATA guideline moved away from routine completion thyroidectomy; it may be considered when persistent disease, radioactive iodine strategy, thyroglobulin-based follow-up, pathology/risk features, or other patient-specific factors make removal of the remaining lobe useful.","why":"A lobectomy can be definitive therapy for many low-risk cancers."},
{"title":"Teach Your Junior","dimension":"teaching","stimulus":"A junior says, 'Papillary thyroid cancer means total thyroidectomy.'","question":"Correct the mental model.","answer":"First stage the disease: tumor size and confinement, gross extrathyroidal extension, nodal/distant disease, contralateral nodules, pathology/risk and patient goals. Modern thyroid surgery deliberately matches extent of surgery to recurrence risk and downstream treatment needs.","why":"Diagnosis alone does not determine extent."}
]},
{
"id":"integrated-thyroidectomy","title":"Thyroidectomy → RLN / Parathyroids → Post-op Reasoning",
"domain":"Thyroid / OR","concept_id":"thyroidectomy",
"summary":"Build the operative map around nerve function, parathyroid preservation, vascular control, and postoperative complication recognition.",
"source_basis":["ENT Mastery operative/endocrine surgery curriculum","2025 ATA differentiated thyroid cancer framework"],
"stages":[
{"title":"Exposure","dimension":"operative","stimulus":"You are starting a thyroid lobectomy.","question":"What is your core three-dimensional map before dissecting near the gland?","answer":"Orient to strap muscles, thyroid capsule, superior pole/pedicle, trachea, carotid sheath, cricothyroid region, recurrent laryngeal nerve course, Berry ligament, and expected parathyroid locations with their vascular supply.","why":"Safe thyroidectomy is anatomy-driven before it is instrument-driven."},
{"title":"Superior pole","dimension":"operative","stimulus":"You are controlling superior-pole vessels.","question":"Which nerve is especially relevant here and what functional deficit follows injury?","answer":"The external branch of the superior laryngeal nerve is at risk near the superior thyroid pedicle; injury can impair cricothyroid function, pitch elevation and vocal projection.","why":"A patient can have meaningful postoperative voice dysfunction even with normal vocal-fold mobility."},
{"title":"RLN","dimension":"operative","stimulus":"You approach the tracheoesophageal groove/Berry ligament region.","question":"Why is the recurrent laryngeal nerve especially vulnerable here?","answer":"The RLN has variable relationships to the inferior thyroid artery and is closely tethered near its laryngeal entry/Berry ligament region; traction, thermal spread, clamping or transection can injure it.","why":"Knowing the expected course is not enough—you must visually and functionally respect the nerve through the danger zone."},
{"title":"Parathyroids","dimension":"operative","stimulus":"A parathyroid gland appears dusky after mobilization.","question":"What are you trying to preserve besides the gland itself?","answer":"Its vascular pedicle. Parathyroid preservation means preserving viable perfused tissue; a clearly devascularized gland may require consideration of autotransplantation according to the operative context.","why":"An anatomically present but ischemic gland may not function."},
{"title":"PACU emergency","dimension":"management","stimulus":"Several hours after surgery the patient develops neck pressure, swelling, anxiety and progressive respiratory difficulty.","question":"What complication must be treated as an airway emergency?","answer":"A rapidly expanding postoperative neck hematoma with airway compromise. Recognition and immediate airway/wound decompression strategy take priority over routine imaging delays.","why":"Thyroid-bed hematoma can obstruct the airway quickly."},
{"title":"Hypocalcemia","dimension":"management","stimulus":"After total thyroidectomy the patient develops perioral tingling and carpopedal symptoms.","question":"What physiology are you thinking about?","answer":"Postoperative hypocalcemia from reduced parathyroid function; assess calcium/PTH in the appropriate institutional pathway and treat symptomatic or significant hypocalcemia promptly.","why":"Early recognition prevents progression to tetany, arrhythmia or other severe manifestations."},
{"title":"Teach Your Junior","dimension":"teaching","stimulus":"A junior asks what structures they should 'find' during thyroidectomy.","question":"Give the better framework.","answer":"Don't reduce it to a scavenger hunt. Preserve function: identify/protect the RLN through its danger course, protect the external branch at the superior pole, preserve viable parathyroids and their blood supply, and control vessels close to the thyroid when that protects adjacent structures.","why":"The goal is safe functional dissection, not merely seeing named structures."}
]},
{
"id":"integrated-thyroid-cancer-node","title":"Papillary Thyroid Cancer → Lateral Node → Neck Strategy",
"domain":"Thyroid / Head & Neck Oncology","concept_id":"thyroid_nodal_disease",
"summary":"Connect suspicious cervical nodes to tissue confirmation, compartment anatomy, thyroid operation extent, and therapeutic neck dissection.",
"source_basis":["2025 ATA Differentiated Thyroid Cancer Guidelines"],
"stages":[
{"title":"Ultrasound","dimension":"recognition","stimulus":"A patient with papillary thyroid carcinoma has a suspicious lateral cervical node on ultrasound.","question":"What is the next diagnostic principle?","answer":"Confirm that the node represents metastatic thyroid cancer when confirmation will change management, using appropriate ultrasound-guided sampling and adjunct testing in context.","why":"A lateral neck operation should be based on established disease, not appearance alone."},
{"title":"Compartment","dimension":"localization","stimulus":"Metastatic lateral nodal disease is confirmed.","question":"Why should you think in neck levels/compartments rather than 'pluck the positive node'?","answer":"Clinically apparent nodal metastasis represents compartmental disease biology; therapeutic dissection is planned around the involved nodal basin while preserving critical nerves, vessels and lymphatics.","why":"Node picking risks leaving regional disease and complicating future surgery."},
{"title":"Primary operation","dimension":"management","stimulus":"The patient has clinically apparent metastatic nodal disease.","question":"How does that affect the thyroid operation conversation compared with a tiny node-negative unilateral cancer?","answer":"Clinically involved nodes move the patient out of the simplest low-risk lobectomy scenario and affect the extent of thyroid and neck surgery plus downstream radioactive iodine/surveillance planning.","why":"Extent of disease, not just primary-tumor diameter, drives treatment."},
{"title":"Lateral neck danger map","dimension":"operative","stimulus":"You are preparing for a therapeutic lateral neck dissection.","question":"Which structures should be in your mental risk map?","answer":"Spinal accessory nerve, internal jugular vein, carotid/vagus, phrenic nerve, brachial plexus, sympathetic chain, cervical sensory roots, thoracic duct on the left, and other level-specific structures.","why":"Compartmental oncologic clearance must be paired with deliberate functional preservation."},
{"title":"Teach Your Junior","dimension":"teaching","stimulus":"A junior asks why you cannot remove only the ultrasound-positive node.","question":"What do you teach?","answer":"A proven metastatic node is evidence of regional lymphatic disease. Therapeutic surgery is organized by nodal compartments because the goal is durable regional control, not removal of one visible marker of disease.","why":"Oncologic anatomy is compartmental."}
]},
{
"id":"integrated-afrs","title":"CRS with Polyps → AFRS Pattern → Longitudinal Control",
"domain":"Rhinology","concept_id":"afrs",
"summary":"Recognize the allergic fungal rhinosinusitis phenotype and integrate surgery with ongoing inflammatory disease control.",
"source_basis":["ICAR-RS 2021","AAO-HNSF Adult Sinusitis Update 2025","AAO-HNSF Surgical Management of CRS 2025"],
"stages":[
{"title":"Phenotype","dimension":"recognition","stimulus":"A younger patient has chronic rhinosinusitis with polyps, thick eosinophilic-appearing mucin, marked heterogeneous sinus opacification and bony remodeling.","question":"What CRS phenotype should enter the differential?","answer":"Allergic fungal rhinosinusitis is an important consideration; diagnosis integrates clinical, radiographic, operative and pathologic/allergic features rather than one isolated finding.","why":"AFRS behaves differently from routine uncomplicated CRS and often has substantial inflammatory burden."},
{"title":"CT","dimension":"reasoning","stimulus":"CT shows expansion/remodeling around heavily opacified sinuses.","question":"Why is the CT more than a Lund-Mackay score here?","answer":"It defines extent, remodeling/erosion, orbit/skull-base relationships and surgical anatomy altered by chronic expansile inflammatory disease.","why":"Disease phenotype changes both risk and operative planning."},
{"title":"Operation","dimension":"management","stimulus":"The patient has extensive obstructive disease requiring surgery.","question":"What is the surgical goal?","answer":"Clear obstructing inflammatory/fungal mucin and polyposis as appropriate, restore access/ventilation and create anatomy that permits postoperative topical therapy and surveillance while protecting orbit/skull base.","why":"Surgery creates access for long-term disease control; it does not eliminate the inflammatory tendency."},
{"title":"Longitudinal care","dimension":"management","stimulus":"The cavities are open after surgery.","question":"Why is the case not 'finished'?","answer":"AFRS has meaningful recurrence risk and requires postoperative inflammatory control, topical therapy, endoscopic surveillance and individualized allergy/systemic treatment considerations.","why":"ICAR-RS frames CRS as heterogeneous chronic inflammatory disease rather than a one-time mechanical blockage."},
{"title":"Teach Your Junior","dimension":"teaching","stimulus":"A junior calls the CT 'fungal sinusitis' and assumes invasive fungal disease.","question":"What distinction matters?","answer":"AFRS is a noninvasive inflammatory CRS phenotype; invasive fungal rhinosinusitis is a different, potentially fulminant tissue-invasive process with a different host profile, urgency and treatment.","why":"The word fungal does not imply the same biology."}
]},
{
"id":"integrated-crs-biologic","title":"CRSwNP → Endotype/Comorbidity → Surgery vs Biologic Strategy",
"domain":"Rhinology","concept_id":"crs_biologics",
"summary":"Treat severe CRSwNP as chronic inflammatory disease and reason through surgery, topical therapy, comorbid asthma/AERD and biologic options.",
"source_basis":["ICAR-RS 2021","AAO-HNSF Adult Sinusitis Update 2025","AAO-HNSF Surgical Management of CRS 2025"],
"stages":[
{"title":"Phenotype","dimension":"reasoning","stimulus":"An adult has recurrent bilateral nasal polyps, anosmia and asthma despite topical therapy.","question":"What comorbid phenotype should you actively ask about?","answer":"Ask about NSAID/aspirin respiratory reactions and other type-2 inflammatory features; AERD can materially change disease burden and longitudinal treatment planning.","why":"CRSwNP is heterogeneous, and associated lower-airway/systemic inflammatory disease matters."},
{"title":"Surgery","dimension":"management","stimulus":"The patient has obstructive polyposis and poor topical access.","question":"What can ESS accomplish even though it does not cure the inflammatory tendency?","answer":"Reduce inflammatory burden/obstruction, restore sinus access and improve delivery of postoperative topical therapy while providing a cavity that can be surveilled.","why":"For chronic inflammatory CRS, surgery and medical therapy are complementary rather than mutually exclusive."},
{"title":"Biologic discussion","dimension":"management","stimulus":"Disease remains severe/recurrent despite appropriate surgery and medical therapy, with substantial type-2 comorbidity.","question":"How should biologics be framed?","answer":"As one component of individualized long-term management for selected severe CRSwNP, weighing disease severity, prior surgery/medical response, asthma/AERD, systemic steroid burden, patient goals, cost/access and expected benefit.","why":"A biologic is not simply the next rung after a spray; patient selection matters."},
{"title":"Teach Your Junior","dimension":"teaching","stimulus":"A junior asks whether severe polyps should get 'FESS or a biologic.'","question":"Why is that framing too binary?","answer":"CRSwNP is chronic inflammatory disease. Surgery can improve anatomy and topical access while biologic/systemic strategies target inflammatory biology; the best sequence or combination depends on phenotype, severity, prior treatment and patient priorities.","why":"Anatomic and inflammatory treatments solve different parts of the disease."}
]}
]
_v43_ids={x["id"] for x in INTEGRATED_CASES}
INTEGRATED_CASES.extend([x for x in INTEGRATED_CASES_V43 if x["id"] not in _v43_ids])

OR_PREP_REGISTRY.update({
"thyroid-lobectomy":{
 "slug":"thyroid-lobectomy","title":"Thyroid Lobectomy","domain":"Thyroid / Endocrine Surgery",
 "indications":"Diagnostic or therapeutic unilateral thyroid surgery when the nodule/cancer/goiter phenotype and patient goals support lobectomy rather than bilateral surgery.",
 "steps":["Confirm indication, side, imaging/FNA, thyroid function, cervical nodes, voice history and whether preoperative laryngeal examination is indicated.",
          "Position and expose the central neck; divide/retract strap musculature as appropriate and mobilize the thyroid lobe.",
          "Control superior-pole vessels with deliberate attention to the external branch of the superior laryngeal nerve.",
          "Mobilize the lobe while identifying/preserving viable parathyroid glands and their vascular supply.",
          "Identify and protect the recurrent laryngeal nerve through the operative danger zone, particularly near its laryngeal entry/Berry ligament.",
          "Complete capsular dissection/lobectomy, inspect nerve/parathyroid/hemostasis, and close with a plan for postoperative voice/hematoma surveillance."],
 "danger":["Recurrent laryngeal nerve","External branch of superior laryngeal nerve","Parathyroid glands and vascular pedicles","Trachea/esophagus","Postoperative neck hematoma","Thermal/traction injury"],
 "attending_followup":[
   ["Where is the RLN most vulnerable?","Its course is variable, but the laryngeal entry/Berry ligament region is a key tethered danger zone; traction and thermal injury matter as much as transection."],
   ["Why ligate superior-pole vessels deliberately near the gland?","It helps control the pedicle while reducing risk to the external branch of the superior laryngeal nerve."],
   ["What does a dusky parathyroid make you think about?","Whether its blood supply has been compromised; viable perfusion matters, and clearly devascularized tissue may prompt consideration of autotransplantation in context."],
   ["What postoperative finding cannot wait for CT?","Rapid neck swelling/pressure with respiratory compromise suggesting expanding hematoma is an airway emergency."]
 ],"linked_topic":"thyroidectomy","status":"audited"
},
"total-thyroidectomy":{
 "slug":"total-thyroidectomy","title":"Total Thyroidectomy","domain":"Thyroid / Endocrine Surgery",
 "indications":"Bilateral thyroid removal when disease extent, cancer risk, bilateral disease, compressive/toxic disease or downstream treatment strategy makes total thyroidectomy preferable to lobectomy.",
 "steps":["Complete the same preoperative disease, node, voice and calcium-risk assessment used for lobectomy, with explicit bilateral nerve/parathyroid planning.",
          "Perform the first side with capsular dissection, superior-laryngeal/RLN protection and preservation of vascularized parathyroids.",
          "Reassess nerve function/operative safety before committing to the contralateral side when intraoperative findings create concern.",
          "Perform contralateral dissection using the same nerve and parathyroid principles.",
          "Confirm meticulous hemostasis and postoperative plans for airway/hematoma observation, voice assessment and calcium/PTH monitoring per institutional pathway."],
 "danger":["Bilateral RLN dysfunction/airway risk","Hypoparathyroidism/hypocalcemia","External branch injury","Neck hematoma","Tracheal injury","Thermal injury"],
 "attending_followup":[
   ["What complication becomes qualitatively different in total versus lobectomy?","Bilateral RLN dysfunction can create an acute airway problem, and bilateral parathyroid compromise creates much greater hypocalcemia risk."],
   ["Why preserve parathyroid blood supply instead of simply identifying the glands?","A devascularized gland may not function even if left anatomically in place."],
   ["What symptoms suggest postoperative hypocalcemia?","Perioral/digital paresthesias, cramping/carpopedal spasm and more severe neuromuscular/cardiac manifestations as calcium falls."],
   ["Does differentiated thyroid cancer automatically require total thyroidectomy?","No. The 2025 ATA framework supports lobectomy for appropriately selected low-risk unilateral disease; extent depends on disease and patient factors."]
 ],"linked_topic":"thyroidectomy","status":"audited"
}
})

ATTENDING_LEVEL_PROMPTS["resident"].extend([
{"domain":"Thyroid","concept_id":"thyroidectomy","prompt":"Why can a patient have voice trouble after thyroidectomy even if both vocal folds move?","answer":"External branch of the superior laryngeal nerve injury can impair cricothyroid function and pitch/projection; intubation and other laryngeal factors can also affect voice."},
{"domain":"Thyroid","concept_id":"thyroid_nodule","prompt":"Does a papillary thyroid cancer confined to one lobe automatically require total thyroidectomy?","answer":"No. Modern ATA guidance accepts lobectomy for appropriately selected low-risk unilateral disease; tumor extent, nodes, contralateral disease and patient goals matter."},
{"domain":"Rhinology","concept_id":"afrs","prompt":"Why isn't AFRS the same thing as invasive fungal sinusitis?","answer":"AFRS is a noninvasive inflammatory CRS phenotype; invasive fungal disease involves tissue invasion and has different host factors, urgency and treatment."}
])
ATTENDING_LEVEL_PROMPTS["senior"].extend([
{"domain":"Thyroid","concept_id":"thyroidectomy","prompt":"What are the two nerve danger concepts at the superior pole and Berry ligament?","answer":"Protect the external branch of the superior laryngeal nerve at the superior pedicle and the RLN as it courses/enters the larynx near Berry ligament."},
{"domain":"Thyroid","concept_id":"thyroid_nodal_disease","prompt":"Why is node-picking a poor operation for proven lateral metastatic papillary thyroid cancer?","answer":"It treats one visible node rather than the involved lymphatic compartment and risks persistent regional disease and difficult reoperation."},
{"domain":"Rhinology","concept_id":"crs_biologics","prompt":"Why is 'FESS versus biologic' often the wrong framing for severe CRSwNP?","answer":"Surgery improves anatomy/disease burden/topical access while biologics target inflammatory biology; they can be complementary and selection depends on phenotype and prior response."}
])
ATTENDING_LEVEL_PROMPTS["chief"].extend([
{"domain":"Thyroid","concept_id":"thyroidectomy","prompt":"Teach thyroidectomy as a functional-preservation operation rather than a list of steps.","answer":"Every maneuver should preserve voice and calcium physiology while achieving the disease goal: protect RLN and EBSLN function, maintain perfused parathyroids, control vessels without collateral injury, and anticipate hematoma/airway complications."},
{"domain":"Thyroid","concept_id":"thyroid_nodule","prompt":"A junior says completion thyroidectomy is mandatory when cancer is found after lobectomy. What changed?","answer":"The 2025 ATA framework no longer treats completion as routine for many low-risk cancers; consider it when residual disease, RAI strategy, thyroglobulin surveillance or risk features create a meaningful benefit."},
{"domain":"Rhinology","concept_id":"crs_biologics","prompt":"Teach the difference between treating anatomy and treating inflammatory biology in CRSwNP.","answer":"ESS opens and reshapes the sinonasal system for clearance, ventilation, topical delivery and surveillance; anti-inflammatory therapy/biologics address the underlying inflammatory drive. Durable control often requires both concepts."}
])


# =============================================================================
# ENT Mastery v4.4 — Longitudinal Curriculum Expansion
# Adds breadth across the core residency domains and longitudinal sequencing.
# =============================================================================

LONGITUDINAL_CURRICULUM = {
"Otology / Neurotology":[
 "Hearing-loss localization","Otitis externa/media","TM perforation","Cholesteatoma",
 "Tympanoplasty","Mastoid surgery","Otosclerosis","Vestibular disorders","Facial nerve","Cochlear implantation"
],
"Rhinology / Allergy":[
 "Nasal obstruction","Epistaxis","ARS/RARS","CRSsNP","CRSwNP","AFRS","AERD",
 "FESS anatomy","Frontal/sphenoid disease","Complications","Skull-base CSF leak"
],
"Head & Neck Oncology":[
 "Adult neck mass","Mucosal SCC","HPV oropharynx","Oral cavity cancer","Larynx cancer",
 "Salivary tumors","Thyroid cancer","Neck dissection","Unknown primary","Surveillance"
],
"Pediatric Otolaryngology":[
 "Otitis media/tubes","Adenoid disease","Tonsil/SDB","Congenital neck masses","Stridor",
 "Laryngomalacia","SGS","Tracheostomy","Velopharyngeal disease","Pediatric hearing loss"
],
"Laryngology / Airway":[
 "Dysphonia","Vocal-fold paralysis","Benign lesions","Stroboscopy","Dysphagia",
 "Glottic stenosis","SGS","Tracheal stenosis","Airway endoscopy","Open reconstruction"
],
"Facial Plastics / Trauma":[
 "Facial analysis","Nasal obstruction","Septoplasty","Rhinoplasty principles","Facial fractures",
 "Soft-tissue trauma","Scar management","Facial nerve","Local flaps","Skin cancer reconstruction"
],
"Sleep Surgery":[
 "Adult PSG","Pediatric PSG","Anatomic phenotyping","DISE","PAP alternatives",
 "Palatal surgery","Tongue-base surgery","HNS candidacy","HNS programming","Residual OSA"
],
"Endocrine / General ENT":[
 "Thyroid nodule","Thyroidectomy","Thyroid cancer","Parathyroid disease","Parathyroidectomy",
 "Deep-neck infection","Tracheostomy","Sialadenitis","Sialolithiasis","Salivary surgery"
]
}

INTEGRATED_CASES_V44 = [
{
"id":"integrated-oral-cavity-scc","title":"Oral Cavity Lesion → Biopsy → Neck → Reconstruction",
"domain":"Head & Neck Oncology","concept_id":"oral_cavity_scc",
"summary":"Turn a mucosal lesion into an oncologic plan that accounts for primary resection, nodal risk, function, and reconstruction.",
"source_basis":["ENT Mastery head & neck oncology curriculum"],
"stages":[
{"title":"Recognition","dimension":"reasoning","stimulus":"A smoker has a persistent ulcerated lateral tongue lesion with pain and referred otalgia.","question":"What makes this more than a routine oral ulcer?","answer":"Persistence, induration/ulceration, risk factors, pain/referred otalgia and suspicious examination features should trigger malignancy evaluation and tissue diagnosis.","why":"The preventable error is diagnostic delay."},
{"title":"Biopsy","dimension":"workup","stimulus":"The lesion is accessible in clinic.","question":"What is the goal of biopsy?","answer":"Obtain representative tissue adequate for diagnosis while documenting lesion site/size and avoiding a poorly planned excision that compromises definitive margins or reconstruction.","why":"Diagnostic tissue sampling and definitive oncologic resection are different procedures."},
{"title":"Staging","dimension":"workup","stimulus":"Biopsy confirms SCC.","question":"What must staging answer?","answer":"Define local extent/depth, relationship to adjacent structures, cervical nodal disease and distant disease when appropriate; imaging and examination should answer questions that change resection, neck treatment or reconstruction.","why":"The primary tumor and the neck are one oncologic problem."},
{"title":"Neck","dimension":"management","stimulus":"The clinically negative neck has meaningful occult nodal risk.","question":"Why might the neck still require treatment?","answer":"Oral cavity SCC can metastasize occultly; elective neck management depends on primary-site risk features and stage rather than palpability alone.","why":"A cN0 examination does not equal zero nodal risk."},
{"title":"Reconstruction","dimension":"operative","stimulus":"A substantial tongue defect is anticipated.","question":"When should reconstruction enter the plan?","answer":"Before resection. Defect size/location, tongue mobility, speech/swallow goals, dentition, mandibular involvement and adjuvant therapy risk determine whether primary closure, local/regional tissue or free-tissue reconstruction best restores function.","why":"Reconstruction is part of oncologic planning, not an afterthought."},
{"title":"Teach Your Junior","dimension":"teaching","stimulus":"A junior focuses only on obtaining a negative primary margin.","question":"What is missing?","answer":"Oncologic success also requires regional control and preservation/restoration of speech, swallowing and airway function, with reconstruction and adjuvant planning built in from the start.","why":"Head and neck cancer treatment is disease control plus function."}
]},
{
"id":"integrated-parotidectomy","title":"Parotid Mass → Facial Nerve → Parotidectomy Strategy",
"domain":"Head & Neck / Salivary","concept_id":"parotidectomy",
"summary":"Use diagnosis, tumor location and facial-nerve function to plan safe parotid surgery.",
"source_basis":["ENT Mastery salivary pathology and operative curriculum"],
"stages":[
{"title":"Pre-op","dimension":"workup","stimulus":"An adult has a slowly enlarging superficial parotid mass.","question":"What must be documented before surgery?","answer":"Facial nerve function, skin fixation, pain, rapid growth, neck nodes, tumor location/extent and an appropriate tissue diagnosis/risk assessment.","why":"Preoperative nerve dysfunction or aggressive features materially change malignancy risk and counseling."},
{"title":"Landmarks","dimension":"localization","stimulus":"You are exposing the main facial nerve trunk.","question":"What is the operative reasoning goal?","answer":"Use reproducible anatomic landmarks and careful dissection to identify the nerve in a safe plane, then follow the appropriate branches while maintaining tumor integrity.","why":"The nerve is the central functional structure around which parotid surgery is organized."},
{"title":"Tumor relationship","dimension":"operative","stimulus":"The tumor abuts but does not grossly invade a functioning facial nerve branch.","question":"What is the general oncologic-functional principle?","answer":"Preserve a functioning uninvolved nerve when oncologically appropriate; direct tumor invasion may require sacrifice with preoperative counseling and reconstructive planning.","why":"Nerve preservation cannot override cancer clearance, but cancer diagnosis alone does not mandate nerve sacrifice."},
{"title":"After surgery","dimension":"management","stimulus":"The patient asks about long-term effects.","question":"What complications should be anticipated beyond facial weakness?","answer":"Frey syndrome/gustatory sweating, salivary collection/fistula, contour change, numbness, scar issues and first-bite-type symptoms depending on operation and anatomy.","why":"Functional counseling extends beyond the headline complication."},
{"title":"Teach Your Junior","dimension":"teaching","stimulus":"A junior says parotidectomy is 'find the nerve and take the gland off it.'","question":"What is the better model?","answer":"First define tumor biology and extent; then perform an oncologically appropriate resection organized around deliberate facial-nerve identification/preservation, tumor integrity and a plan for nerve reconstruction if invasion requires sacrifice.","why":"The operation is driven by tumor biology plus nerve anatomy."}
]},
{
"id":"integrated-cholesteatoma-op","title":"Cholesteatoma → Mastoid Map → Safe Ear",
"domain":"Otology / Surgery","concept_id":"mastoidectomy",
"summary":"Translate cholesteatoma extent into mastoid surgical anatomy, disease clearance, hearing strategy, and surveillance.",
"source_basis":["ENT Mastery otoscopy and operative otology curriculum"],
"stages":[
{"title":"Goal","dimension":"reasoning","stimulus":"A patient has epitympanic cholesteatoma extending into the mastoid.","question":"What is the primary operative goal?","answer":"Create a safe, dry, maintainable ear by clearing cholesteatoma while preserving or reconstructing hearing when compatible with safe disease control.","why":"Hearing optimization is important but secondary to durable disease control."},
{"title":"Mastoid map","dimension":"localization","stimulus":"You begin cortical mastoidectomy.","question":"Which structures define the safety map?","answer":"Tegmen superiorly, sigmoid sinus posteriorly, external auditory canal anteriorly, mastoid tip inferiorly, with deeper orientation to lateral semicircular canal, facial nerve, incus and digastric ridge.","why":"Mastoid surgery is a progressive three-dimensional localization exercise."},
{"title":"Facial recess","dimension":"operative","stimulus":"Access to the middle ear through the facial recess is planned.","question":"What triangle are you working within?","answer":"The facial recess is bounded by the facial nerve medially/posteriorly, chorda tympani laterally/anteriorly and the fossa incudis superiorly.","why":"The approach trades access for proximity to two important nerves."},
{"title":"Canal wall","dimension":"management","stimulus":"Disease extent and anatomy make you consider canal-wall-up versus canal-wall-down strategy.","question":"Why is this not simply a surgeon-preference binary?","answer":"Extent, location, anatomy, Eustachian-tube/middle-ear environment, ability to clear disease, patient reliability, hearing goals and surveillance strategy all matter.","why":"The best cavity is the one that achieves safe disease control and can be maintained."},
{"title":"Surveillance","dimension":"management","stimulus":"The ear looks well healed.","question":"Why does follow-up remain part of the operation?","answer":"Residual/recurrent cholesteatoma may not be obvious on routine examination depending on reconstruction; clinical surveillance and imaging/second-look strategy are part of the original surgical plan.","why":"A technically successful first operation does not eliminate recurrence risk."},
{"title":"Teach Your Junior","dimension":"teaching","stimulus":"A junior asks whether CWU is 'better' because it preserves anatomy.","question":"What do you teach?","answer":"Preserving anatomy is valuable only if disease can be cleared and reliably surveilled. Choose the strategy that best balances eradication, hearing, maintenance and recurrence risk for that ear and patient.","why":"Anatomic preservation is a means, not the endpoint."}
]},
{
"id":"integrated-septoplasty","title":"Nasal Obstruction → Septum/Valve/Turbinates → Septoplasty",
"domain":"Facial Plastics / Rhinology","concept_id":"septoplasty",
"summary":"Localize nasal obstruction before operating so septoplasty treats the actual bottleneck.",
"source_basis":["ENT Mastery rhinology/facial plastics curriculum"],
"stages":[
{"title":"Localization","dimension":"reasoning","stimulus":"An adult reports chronic unilateral nasal obstruction and has a deviated septum.","question":"Why isn't seeing deviation enough?","answer":"Nasal obstruction can also arise from inferior turbinate hypertrophy, internal/external nasal valve dysfunction, mucosal disease, polyps or masses; determine which structures actually limit airflow.","why":"A septoplasty cannot fix a problem that is not primarily septal."},
{"title":"Valve","dimension":"workup","stimulus":"The patient improves markedly with lateral cheek support.","question":"What should you investigate?","answer":"Nasal valve contribution and dynamic/static lateral-wall support, rather than assuming the septum explains all symptoms.","why":"Valve dysfunction is an important cause of persistent obstruction after otherwise adequate septal surgery."},
{"title":"Operation","dimension":"operative","stimulus":"Septoplasty is appropriate.","question":"What structural principle matters when removing/repositioning cartilage?","answer":"Correct the obstructing deformity while preserving adequate dorsal/caudal structural support and mucoperichondrial integrity.","why":"Over-resection can trade obstruction for collapse, deformity or perforation."},
{"title":"Complications","dimension":"management","stimulus":"The patient calls with severe increasing obstruction and pain after surgery.","question":"What complication should be actively excluded?","answer":"Septal hematoma, particularly when there is bilateral fluctuant septal swelling; it requires prompt recognition and management to protect cartilage.","why":"Untreated hematoma can lead to cartilage necrosis, infection and deformity."},
{"title":"Teach Your Junior","dimension":"teaching","stimulus":"A junior says, 'The septum is crooked, so septoplasty will fix the breathing.'","question":"Correct the reasoning.","answer":"First localize the obstruction across septum, turbinates, valves and mucosa. Then match the operation to the structures actually causing resistance.","why":"Anatomic abnormality is not automatically the symptomatic bottleneck."}
]},
{
"id":"integrated-deep-neck","title":"Deep Neck Infection → Airway → Source Control",
"domain":"General ENT / Emergency","concept_id":"deep_neck_infection",
"summary":"Prioritize airway, localize the involved space, identify source/complications, and decide when drainage is required.",
"source_basis":["ENT Mastery general ENT curriculum"],
"stages":[
{"title":"Triage","dimension":"recognition","stimulus":"A patient has fever, trismus, muffled voice, neck swelling and difficulty handling secretions.","question":"What comes before perfect diagnostic labeling?","answer":"Assess airway stability and trajectory immediately while beginning evaluation/treatment; deep-neck infection can progress rapidly and distort airway anatomy.","why":"Airway deterioration is the time-critical threat."},
{"title":"Imaging","dimension":"workup","stimulus":"The patient is stable enough for imaging.","question":"What should contrast-enhanced neck imaging answer?","answer":"Which deep space is involved, whether there is drainable collection versus phlegmon, source, airway displacement, vascular complications and spread toward mediastinum or other spaces.","why":"The CT should map source control and complications, not just confirm inflammation."},
{"title":"Management","dimension":"management","stimulus":"Imaging shows a mature collection with clinical progression.","question":"What are the major treatment pillars?","answer":"Airway management as needed, appropriate antimicrobial therapy, hydration/supportive care, treatment of the source and drainage/source control when the collection or clinical course warrants it.","why":"Antibiotics cannot substitute for drainage of every established abscess."},
{"title":"Teach Your Junior","dimension":"teaching","stimulus":"A junior wants to send a noisy, drooling patient to CT first because 'we need the diagnosis.'","question":"What do you teach?","answer":"Imaging is valuable only if the patient can safely get it. Airway stability and a rescue plan come before diagnostic completeness in a potentially deteriorating deep-neck infection.","why":"The safest sequence depends on physiology."}
]},
{
"id":"integrated-tracheostomy","title":"Airway Need → Tracheostomy → Tube Emergency",
"domain":"Airway / General ENT","concept_id":"tracheostomy",
"summary":"Understand indications, operative anatomy, fresh-trach risk, and emergency reasoning.",
"source_basis":["ENT Mastery airway curriculum"],
"stages":[
{"title":"Indication","dimension":"reasoning","stimulus":"A patient requires prolonged ventilatory support and has difficult secretion management.","question":"What does tracheostomy change physiologically and practically?","answer":"It creates a direct cervical airway that can reduce upper-airway resistance/dead space, facilitate pulmonary toilet and long-term ventilation, but introduces tube/stoma-specific risks and does not itself treat the underlying disease.","why":"A tracheostomy is an airway-management strategy, not a diagnosis."},
{"title":"Anatomy","dimension":"localization","stimulus":"You expose the anterior trachea.","question":"What structures must remain in the danger map?","answer":"Thyroid isthmus, anterior jugular veins, tracheal rings, cricoid, recurrent laryngeal nerves posterolaterally, esophagus posteriorly, and variant/high-riding great vessels inferiorly.","why":"Midline orientation is central to safe access."},
{"title":"Fresh tube","dimension":"management","stimulus":"A fresh tracheostomy tube becomes displaced and the patient desaturates.","question":"Why is this different from a mature tract?","answer":"A fresh tract can collapse or create a false passage during blind reinsertion; oxygenation/ventilation and expert airway rescue take priority, with management tailored to upper-airway accessibility and time from surgery.","why":"The age of the tract changes the safety of tube replacement."},
{"title":"Teach Your Junior","dimension":"teaching","stimulus":"A junior says, 'If a trach comes out, just put it back in.'","question":"What is the critical correction?","answer":"First ask how old the tract is and whether the patient can be ventilated from above. Blind replacement of a fresh tracheostomy can create a false passage and worsen the emergency.","why":"Emergency algorithms depend on anatomy and tract maturity."}
]}
]

_v44_ids={x["id"] for x in INTEGRATED_CASES}
INTEGRATED_CASES.extend([x for x in INTEGRATED_CASES_V44 if x["id"] not in _v44_ids])

OR_PREP_REGISTRY.update({
"parotidectomy":{
 "slug":"parotidectomy","title":"Parotidectomy","domain":"Head & Neck / Salivary",
 "indications":"Selected benign or malignant parotid lesions requiring resection after appropriate imaging/tissue diagnosis and documentation of facial-nerve function.",
 "steps":["Review pathology/imaging, tumor location, skin/neck findings and baseline facial-nerve function.",
          "Plan incision/flap and expose the parotid while preserving appropriate soft-tissue planes.",
          "Identify the facial nerve using reliable anatomic landmarks and careful dissection.",
          "Follow relevant branches and separate gland/tumor while maintaining tumor integrity and protecting functioning uninvolved nerve.",
          "Complete the oncologically appropriate extent of resection, address the neck when indicated, obtain hemostasis and plan contour/nerve reconstruction when needed."],
 "danger":["Facial nerve","Great auricular nerve","External carotid branches/retromandibular vein","Tumor violation","Frey syndrome","Salivary fistula/seroma"],
 "attending_followup":[["What finding most changes facial-nerve counseling before surgery?","Preoperative facial weakness raises concern for malignant nerve involvement and changes resection/reconstruction planning."],["Does malignancy automatically mean facial-nerve sacrifice?","No. Preserve functioning uninvolved nerve when oncologically appropriate; sacrifice is considered when required for tumor clearance."],["Why obtain tissue diagnosis before many parotid operations?","Tumor biology can change extent, neck planning, counseling and the need for additional workup."]],
 "linked_topic":"parotidectomy","status":"audited"
},
"mastoidectomy":{
 "slug":"mastoidectomy","title":"Mastoidectomy for Cholesteatoma","domain":"Otology",
 "indications":"Cholesteatoma or other selected mastoid/middle-ear disease requiring surgical clearance and creation of a safe maintainable ear.",
 "steps":["Review otoscopy, audiogram and temporal-bone imaging when indicated; map tegmen, sigmoid, canal, labyrinth/facial nerve and disease extent.",
          "Perform cortical mastoidectomy using tegmen, sigmoid sinus and EAC as major boundaries.",
          "Progressively identify deeper landmarks such as lateral semicircular canal, incus/fossa incudis, facial nerve course and digastric ridge.",
          "Clear disease from involved epitympanic/mastoid/middle-ear spaces using an approach matched to extent and safety.",
          "Choose canal-wall/reconstruction strategy based on clearance, anatomy, hearing, maintenance and surveillance needs.",
          "Plan ossicular reconstruction and residual/recurrent disease surveillance as part of the original operation."],
 "danger":["Facial nerve","Lateral semicircular canal/labyrinth","Tegmen/dura","Sigmoid sinus","Chorda tympani","Ossicular chain","CSF leak"],
 "attending_followup":[["What are your three major cortical mastoidectomy boundaries?","Tegmen superiorly, sigmoid sinus posteriorly and external auditory canal anteriorly."],["What is the priority in cholesteatoma surgery?","A safe dry maintainable ear with durable disease clearance; hearing preservation/reconstruction follows that constraint."],["Why is follow-up part of the operation?","Residual/recurrent disease may be hidden by reconstruction, so surveillance strategy must be planned from the outset."]],
 "linked_topic":"mastoidectomy","status":"audited"
},
"septoplasty":{
 "slug":"septoplasty","title":"Septoplasty","domain":"Rhinology / Facial Plastics",
 "indications":"Symptomatic septal obstruction when examination confirms a meaningful septal contribution and other causes of nasal obstruction have been considered.",
 "steps":["Localize obstruction across septum, turbinates, internal/external valve and mucosal disease before operating.",
          "Elevate mucoperichondrial/mucoperiosteal flaps while minimizing opposing tears.",
          "Correct obstructing cartilage/bone selectively while preserving adequate dorsal and caudal support.",
          "Address additional obstructing structures only when indicated by the preoperative functional diagnosis.",
          "Reapproximate mucosa, control bleeding and assess septal support/airway before closure."],
 "danger":["Septal perforation","Septal hematoma","Dorsal/caudal destabilization","Persistent obstruction","Dental/nasal numbness","Bleeding"],
 "attending_followup":[["Why can septoplasty fail despite a straighter septum?","The original obstruction may also come from valve dysfunction, turbinate hypertrophy or mucosal disease."],["Why preserve an L-strut/support framework?","Excessive structural resection can cause dorsal or caudal collapse and cosmetic/functional deformity."],["What postoperative finding requires prompt evaluation?","Bilateral painful/fluctuant septal swelling concerning for septal hematoma."]],
 "linked_topic":"septoplasty","status":"audited"
},
"tracheostomy":{
 "slug":"tracheostomy","title":"Tracheostomy","domain":"Airway / General ENT",
 "indications":"Need for durable airway access, prolonged ventilation, pulmonary toilet, bypass of upper-airway obstruction or other selected airway-management indications.",
 "steps":["Confirm indication, airway rescue plan, anatomy and whether standard open access is appropriate.",
          "Expose the midline cervical trachea while controlling superficial veins and managing the thyroid isthmus as required.",
          "Identify tracheal level and create the planned tracheal opening without losing airway control.",
          "Insert the tracheostomy tube under controlled ventilation/oxygenation conditions and confirm position/ventilation.",
          "Secure the tube, document tube type/size and establish fresh-tracheostomy emergency and first-change plans."],
 "danger":["Loss of airway/false passage","Bleeding","Posterior tracheal/esophageal injury","Pneumothorax/pneumomediastinum","High-riding innominate vessel","Tube obstruction/dislodgement"],
 "attending_followup":[["Why is a fresh trach dislodgement dangerous?","The tract can collapse and blind replacement can create a false passage; airway rescue strategy depends on tract age and upper-airway accessibility."],["Why avoid an excessively high tracheal opening?","Proximity to the cricoid/subglottis can contribute to structural injury/stenosis."],["What information should be obvious at bedside after surgery?","Tube type/size, date/tract maturity, cuff status, upper-airway accessibility and the emergency replacement/rescue plan."]],
 "linked_topic":"tracheostomy","status":"audited"
}
})

ATTENDING_LEVEL_PROMPTS["resident"].extend([
{"domain":"Head & Neck","concept_id":"oral_cavity_scc","prompt":"Why does a cN0 oral cavity cancer still force you to think about the neck?","answer":"The neck can harbor occult metastases; nodal treatment is based on the primary's risk profile, not palpability alone."},
{"domain":"Otology","concept_id":"mastoidectomy","prompt":"Name the three major boundaries that orient a cortical mastoidectomy.","answer":"Tegmen superiorly, sigmoid sinus posteriorly, and external auditory canal anteriorly."},
{"domain":"Facial Plastics","concept_id":"septoplasty","prompt":"Why can a technically straight septum leave a patient obstructed?","answer":"The symptomatic bottleneck may also involve the nasal valve, turbinates or mucosal disease."}
])
ATTENDING_LEVEL_PROMPTS["senior"].extend([
{"domain":"Head & Neck","concept_id":"parotidectomy","prompt":"How does preoperative facial weakness change a parotid-mass case?","answer":"It raises concern for malignant nerve involvement and changes imaging, counseling, oncologic resection and possible nerve-reconstruction planning."},
{"domain":"Otology","concept_id":"mastoidectomy","prompt":"Why isn't canal-wall-up versus canal-wall-down a simple quality ranking?","answer":"The choice depends on disease clearance, anatomy, hearing, maintenance, patient reliability and surveillance; preserving anatomy is only useful if the ear remains safe."},
{"domain":"Airway","concept_id":"tracheostomy","prompt":"What is the first question when a displaced trach arrives in the ED?","answer":"How old/mature is the tract and can the patient be oxygenated/ventilated from above? Those facts determine the safety of replacement and rescue options."}
])
ATTENDING_LEVEL_PROMPTS["chief"].extend([
{"domain":"Head & Neck","concept_id":"oral_cavity_scc","prompt":"Teach an oral-cavity cancer plan in one sentence without turning it into a TNM recital.","answer":"Define resectable primary extent, quantify regional nodal risk/disease, plan oncologic margins and neck treatment, and design reconstruction/adjuvant strategy around preservation of speech, swallow and airway."},
{"domain":"Otology","concept_id":"mastoidectomy","prompt":"Teach mastoidectomy as spatial reasoning.","answer":"Stay continuously oriented to fixed boundaries—tegmen, sigmoid and canal—then earn deeper landmarks such as lateral canal, incus and facial nerve as you remove bone; never drill toward a presumed target without knowing the surrounding danger map."},
{"domain":"Airway","concept_id":"tracheostomy","prompt":"Why is tracheostomy care part of the operation rather than a postoperative nursing detail?","answer":"Tube security, humidification/clearance, tract maturity, first-change timing and an explicit emergency algorithm determine whether the new airway remains safe after the surgeon leaves the OR."}
])


# =============================================================================
# ENT Mastery v5.0 — Comprehensive Longitudinal Curriculum
# =============================================================================

CURRICULUM_V5 = {
"Otology / Neurotology": {
 "sequence":[
  ("Foundations",["Temporal bone anatomy","Hearing physiology","Audiogram interpretation","Tympanometry/acoustic reflexes"]),
  ("Core disease",["Otitis externa","AOM/OME","TM perforation","ET dysfunction","Cholesteatoma","Otosclerosis","SSNHL"]),
  ("Neurotology",["BPPV","Ménière disease","Vestibular neuritis","Vestibular migraine","Vestibular schwannoma","Facial nerve disorders"]),
  ("Operative",["Tympanostomy tubes","Tympanoplasty","Ossiculoplasty","Stapes surgery","Mastoidectomy","Cochlear implantation"]),
  ("Chief / Boards",["Temporal-bone imaging","Skull-base complications","CSF otorrhea","Petrous apex lesions","Complication rescue"])
 ],"competencies":["localize hearing loss","interpret audiometry","read temporal-bone CT","choose medical vs operative therapy","map facial nerve/labyrinth","manage complications"]},
"Rhinology / Allergy / Skull Base": {
 "sequence":[
  ("Foundations",["Nasal/sinus anatomy","Mucociliary physiology","Allergic rhinitis","Nasal obstruction"]),
  ("Inflammatory",["ARS","RARS","CRSsNP","CRSwNP","AERD","AFRS","Pediatric CRS"]),
  ("Other disease",["Epistaxis","Septal disease","Turbinate disease","Sinonasal tumors","CSF rhinorrhea"]),
  ("Operative",["Septoplasty","Turbinate surgery","Maxillary antrostomy","Ethmoidectomy","Sphenoidotomy","Frontal sinus surgery"]),
  ("Chief / Boards",["Revision FESS","Orbit/skull-base complications","Frontal recess anatomy","Endoscopic skull base principles"])
 ],"competencies":["phenotype CRS","interpret sinus CT","localize nasal obstruction","map FESS danger anatomy","choose surgery/biologic strategy","manage epistaxis and complications"]},
"Head & Neck Oncology": {
 "sequence":[
  ("Foundations",["Neck levels","Mucosal anatomy","TNM concepts","HPV/EBV biology","Cancer workup"]),
  ("Primary sites",["Oral cavity","Oropharynx","Larynx","Hypopharynx","Nasopharynx","Sinonasal malignancy","Skin cancer"]),
  ("Neck",["Adult neck mass","Unknown primary","Nodal metastasis","Neck dissection"]),
  ("Treatment",["Surgery","Radiation","Chemoradiation","Immunotherapy concepts","Reconstruction"]),
  ("Chief / Boards",["Margins","ENE/PNI/LVI","Adjuvant decisions","Salvage","Surveillance","Treatment complications"])
 ],"competencies":["stage disease","plan biopsy","interpret pathology","plan primary/neck treatment","anticipate reconstruction","integrate adjuvant therapy"]},
"Thyroid / Parathyroid / Salivary": {
 "sequence":[
  ("Thyroid",["Thyroid nodule","US risk stratification","FNA","Differentiated cancer","Medullary cancer","Anaplastic cancer"]),
  ("Thyroid surgery",["Lobectomy","Total thyroidectomy","Central neck","Lateral neck","RLN/EBSLN","Parathyroid preservation"]),
  ("Parathyroid",["Primary HPT","Secondary/tertiary HPT","Localization","Focused exploration","Four-gland exploration","Hungry bone"]),
  ("Salivary",["Sialadenitis","Sialolithiasis","Benign tumors","Malignant tumors","Parotidectomy","Submandibular surgery"]),
  ("Chief / Boards",["Reoperative thyroid","Invasive thyroid cancer","Nerve reconstruction","Salivary adjuvant therapy"])
 ],"competencies":["interpret thyroid workup","select extent of surgery","protect laryngeal nerves/parathyroids","localize hyperparathyroidism","classify salivary tumors"]},
"Pediatric Otolaryngology": {
 "sequence":[
  ("Ear/hearing",["AOM/OME","Tubes","Pediatric hearing loss","Congenital ear disease"]),
  ("Sleep/infection",["Adenoid disease","Tonsillitis","Pediatric SDB/OSA","Deep neck infection"]),
  ("Congenital",["Branchial anomalies","Thyroglossal duct cyst","Dermoid","Lymphatic/vascular lesions"]),
  ("Airway",["Stridor","Laryngomalacia","Vocal-fold immobility","SGS","Tracheostomy","Foreign body"]),
  ("Chief / Boards",["Airway reconstruction","Decannulation","Craniofacial airway","Complex aspiration","Pediatric tumors"])
 ],"competencies":["age-adjust differential","interpret pediatric audiology","risk-stratify sleep","evaluate stridor","perform complete airway reasoning","plan decannulation"]},
"Laryngology / Voice / Swallowing": {
 "sequence":[
  ("Foundations",["Laryngeal anatomy","Phonation","Swallow physiology","Flexible laryngoscopy","Stroboscopy"]),
  ("Voice",["Nodules/polyps/cysts","Vocal-fold paralysis","Presbyphonia","Spasmodic dysphonia","Reinke edema"]),
  ("Swallow",["FEES","MBS concepts","Aspiration","UES dysfunction","Zenker diverticulum"]),
  ("Airway",["Glottic stenosis","Posterior glottic stenosis","SGS","Tracheal stenosis"]),
  ("Operative",["Microlaryngoscopy","Injection augmentation","Medialization","Airway dilation","Open reconstruction"])
 ],"competencies":["describe stroboscopy","localize dysphonia","interpret swallow studies","choose rehabilitation vs surgery","protect airway/voice/swallow tradeoffs"]},
"Facial Plastics / Trauma": {
 "sequence":[
  ("Foundations",["Facial analysis","Wound healing","Scar biology","Local flap principles"]),
  ("Functional nose",["Septum","Internal valve","External valve","Turbinates","Functional rhinoplasty"]),
  ("Trauma",["Nasal fracture","NOE","ZMC","Orbital fracture","Mandible fracture","Frontal sinus"]),
  ("Reconstruction",["Skin cancer defects","Local/regional flaps","Grafts","Facial nerve rehabilitation"]),
  ("Chief / Boards",["Rhinoplasty mechanics","Complex trauma sequencing","Free tissue interface","Complication revision"])
 ],"competencies":["analyze nasal airway","interpret facial CT","plan fracture repair","choose reconstructive ladder","preserve facial function"]},
"Sleep Surgery": {
 "sequence":[
  ("Foundations",["Sleep physiology","AHI/RDI","Oxygen metrics","Adult PSG","Pediatric PSG"]),
  ("Evaluation",["OSA phenotype","PAP","Oral appliance","Anatomic examination","DISE"]),
  ("Surgery",["Adenotonsillectomy","Palatal procedures","Tongue-base procedures","Skeletal surgery concepts"]),
  ("HNS",["Candidacy","DISE pattern","Implant anatomy","Activation/programming","Troubleshooting"]),
  ("Chief / Boards",["Residual OSA","Multilevel surgery","Comorbidity risk","Outcome interpretation"])
 ],"competencies":["interpret PSG","select candidates","localize collapse","counsel PAP alternatives","understand HNS pathway"]},
"General ENT / Emergencies": {
 "sequence":[
  ("Clinic",["Cerumen","OE","Rhinitis","Sinusitis","Sialadenitis","Dysphonia","Globus"]),
  ("Emergency",["Epistaxis","Peritonsillar abscess","Deep neck infection","Airway foreign body","Post-tonsil bleed","Tracheostomy emergency"]),
  ("Inpatient",["Airway consultation","Neck infection","Postoperative fever","Chyle leak","Electrolyte complications"]),
  ("Procedures",["Flexible scope","I&D","Nasal packing/cautery","Tracheostomy","Bedside airway care"]),
  ("Chief / Boards",["Airway crisis leadership","Bleeding rescue","Complication triage","Disposition"])
 ],"competencies":["recognize emergencies","prioritize airway","choose imaging","perform source control","manage postoperative complications"]}
}

# Explicit prerequisite graph. Used by curriculum UI and future adaptive sequencing.
PREREQUISITES_V5 = {
 "Audiogram interpretation":["Hearing physiology"],
 "Tympanoplasty":["Audiogram interpretation","TM perforation"],
 "Mastoidectomy":["Cholesteatoma","Temporal bone anatomy","Temporal-bone imaging"],
 "Stapes surgery":["Audiogram interpretation","Otosclerosis"],
 "Cochlear implantation":["Pediatric hearing loss","Audiogram interpretation"],
 "Ethmoidectomy":["Nasal/sinus anatomy","CRSsNP","CRSwNP"],
 "Frontal sinus surgery":["Ethmoidectomy","Frontal recess anatomy"],
 "Revision FESS":["Ethmoidectomy","Temporal-bone imaging"],
 "Neck dissection":["Neck levels","Nodal metastasis"],
 "Thyroid lobectomy":["Thyroid nodule","FNA"],
 "Total thyroidectomy":["Thyroid lobectomy","Differentiated cancer"],
 "Airway reconstruction":["SGS","Tracheostomy","Laryngeal anatomy"],
 "Supraglottoplasty":["Laryngomalacia","Flexible laryngoscopy"],
 "Medialization":["Vocal-fold paralysis","Laryngeal anatomy"],
 "HNS candidacy":["Adult PSG","OSA phenotype","DISE"],
 "Functional rhinoplasty":["Internal valve","External valve","Septum"]
}

# Retrieval-spacing tiers: same concept returns with progressively harder task.
SPIRAL_LEVELS_V5 = [
 {"level":1,"name":"Recognize","goal":"Identify the pattern, structure, diagnosis, or emergency."},
 {"level":2,"name":"Localize","goal":"Explain where the problem is and which anatomy/physiology produces it."},
 {"level":3,"name":"Work up","goal":"Choose and interpret the next useful test rather than ordering everything."},
 {"level":4,"name":"Manage","goal":"Choose observation, medical therapy, procedure, surgery, or escalation and explain why."},
 {"level":5,"name":"Operate","goal":"Know indication, setup, landmarks, danger structures, key steps, complications and postoperative plan."},
 {"level":6,"name":"Teach / Boards","goal":"Defend the plan, compare alternatives, rescue complications and teach the mental model."}
]

# Broad, nonduplicative knowledge bank for longitudinal retrieval.
CORE_KNOWLEDGE_V5 = [
# Otology
("Otology","Hearing physiology","Why does an air-bone gap localize to conductive mechanics?","Bone conduction bypasses the external/middle-ear transmission pathway; poorer air than bone thresholds therefore indicates an added conductive component.","Recognize"),
("Otology","Tympanometry","What does a flat tympanogram require you to check before calling it effusion?","Ear-canal volume. A normal volume can support middle-ear effusion; a large volume can indicate a patent tube or TM perforation; a very small volume may reflect probe obstruction.","Work up"),
("Otology","SSNHL","What is the first localization error to avoid in sudden hearing loss?","Do not assume 'blocked ear' is conductive; obtain/confirm audiometry promptly because sudden sensorineural loss is time-sensitive.","Work up"),
("Otology","Otosclerosis","What audiometric pattern should suggest stapes fixation?","A conductive loss with normal-appearing TM, often with a Carhart-type 2-kHz bone-conduction depression; the pattern supports but does not prove the diagnosis.","Localize"),
("Otology","BPPV","What distinguishes BPPV from a persistent vestibular syndrome?","Brief position-triggered episodes with characteristic positional nystagmus rather than continuous spontaneous vertigo lasting days.","Recognize"),
("Otology","Ménière disease","What symptom cluster defines the classic syndrome?","Episodic vertigo with fluctuating sensorineural hearing symptoms, tinnitus and/or aural pressure, after excluding better explanations.","Recognize"),
("Otology","Facial nerve","Why does forehead movement help localize acute facial weakness?","A central supranuclear lesion often spares some forehead movement because of bilateral cortical innervation, whereas a peripheral facial-nerve lesion typically affects the entire ipsilateral face.","Localize"),
("Otology","Cholesteatoma","Why is hearing outcome not the first priority in cholesteatoma surgery?","The first goal is durable eradication/control of unsafe keratinizing disease; hearing preservation/reconstruction must fit within that safety goal.","Manage"),
# Rhinology
("Rhinology","Allergic rhinitis","What separates allergic rhinitis treatment from treating a structural obstruction?","Allergic disease is mucosal/inflammatory and responds to allergen avoidance/pharmacologic or immunologic strategies; fixed septal/valve obstruction requires an anatomic solution when symptomatic.","Localize"),
("Rhinology","ARS","Why should purulent-looking drainage alone not equal bacterial sinusitis?","Color is nonspecific; bacterial likelihood depends on illness pattern such as persistence without improvement or worsening after initial improvement plus the overall clinical context.","Work up"),
("Rhinology","CRS","What makes CRS a diagnosis rather than 'sinus symptoms for a long time'?","Chronic characteristic symptoms plus objective evidence of sinonasal inflammation, with phenotype and alternative diagnoses considered.","Work up"),
("Rhinology","AERD","What triad should trigger AERD thinking?","Asthma, CRSwNP and respiratory reactions to COX-1 inhibiting NSAIDs/aspirin.","Recognize"),
("Rhinology","Epistaxis","Why does identifying anterior versus posterior/severe bleeding matter?","It changes visualization, likelihood of successful local control, airway/hemodynamic risk, disposition and need for procedural/arterial control.","Localize"),
("Rhinology","CSF rhinorrhea","What history should make unilateral clear rhinorrhea more concerning for CSF?","Persistent unilateral watery drainage, positional/salty characteristics, meningitis history, skull-base trauma/surgery or risk factors for spontaneous leak; confirmation requires appropriate fluid testing and localization.","Recognize"),
# H&N
("Head & Neck","Adult neck mass","What is the dangerous assumption in an adult persistent lateral neck mass?","Treating it as a benign cyst without excluding metastatic malignancy, particularly HPV-associated or other head-and-neck cancer.","Recognize"),
("Head & Neck","HPV oropharynx","Why can a small tonsil/base-of-tongue primary present with a large cystic neck node?","HPV-associated oropharyngeal carcinoma commonly presents with nodal disease that may be cystic despite a subtle primary.","Localize"),
("Head & Neck","Oral cavity SCC","Why does depth of invasion matter?","It reflects primary-tumor biology and occult nodal risk and contributes to staging/neck-management reasoning.","Manage"),
("Head & Neck","Larynx cancer","Why does vocal-fold mobility matter in staging and treatment planning?","Impaired/fixed mobility can indicate deeper laryngeal involvement and changes stage, functional prognosis and treatment options.","Localize"),
("Head & Neck","Unknown primary","What is the core objective of unknown-primary workup?","Identify the mucosal primary when possible while staging the neck and preserving treatment options, using directed examination/imaging and appropriately planned tissue evaluation.","Work up"),
("Head & Neck","Neck dissection","Why learn levels instead of memorizing one neck-dissection template?","Primary sites drain predictably but differently; compartment anatomy allows oncologically appropriate clearance while avoiding unnecessary morbidity.","Operate"),
# Endocrine/salivary
("Endocrine","Thyroid nodule","What does a suppressed TSH change in the thyroid-nodule workup?","It raises the possibility of an autonomously functioning nodule and changes the role/sequence of radionuclide functional assessment versus routine FNA logic.","Work up"),
("Endocrine","RLN","What does the RLN innervate functionally?","All intrinsic laryngeal muscles except the cricothyroid; injury therefore affects vocal-fold motion and can affect voice, airway and swallowing protection.","Localize"),
("Endocrine","EBSLN","Why can EBSLN injury be missed if you only look at vocal-fold mobility?","It innervates the cricothyroid; injury may impair pitch and projection despite preserved gross vocal-fold abduction/adduction.","Localize"),
("Endocrine","Primary hyperparathyroidism","Why is localization not the diagnosis?","Biochemical evidence establishes hyperparathyroidism; imaging localizes abnormal gland(s) for operative planning after the biochemical diagnosis is made.","Work up"),
("Salivary","Sialolithiasis","Why is submandibular disease common?","The gland's viscous saliva, mineral composition and long uphill Wharton duct contribute to stone formation/stasis.","Localize"),
("Salivary","Parotid malignancy","Which clinical features raise concern that a parotid mass is malignant?","Facial weakness, pain, rapid growth, fixation/skin involvement, nodal disease and infiltrative imaging features increase concern.","Recognize"),
# Pediatrics
("Pediatrics","OME","Why is middle-ear fluid not synonymous with acute otitis media?","AOM requires acute inflammatory/infectious findings; OME is effusion without the acute inflammatory syndrome.","Recognize"),
("Pediatrics","Tonsil SDB","Why doesn't tonsil size alone quantify pediatric OSA severity?","Obstruction is multilevel and physiologic severity depends on sleep-related airflow/oxygenation plus comorbid anatomy and neuromuscular factors.","Localize"),
("Pediatrics","Branchial anomaly","Why does lesion location help identify congenital neck masses?","Embryologic tracts/cysts occur in reproducible anatomic relationships, so location relative to SCM, hyoid, carotids and pharynx narrows the diagnosis.","Localize"),
("Pediatrics","Laryngomalacia","What makes laryngomalacia severe?","Physiologic consequences such as feeding/growth failure, significant work of breathing, hypoxemia, apnea or cyanosis—not stridor loudness.","Manage"),
("Pediatrics","Airway foreign body","Why can a normal chest radiograph not exclude an aspirated foreign body?","Many foreign bodies are radiolucent and imaging can be normal; history and airway findings determine whether bronchoscopy is needed.","Work up"),
# Laryngology
("Laryngology","Stroboscopy","What does absent mucosal wave suggest?","Marked stiffness or impaired vibratory pliability; interpret it with lesion morphology because scarring, invasive lesions and other pathology can reduce wave.","Localize"),
("Laryngology","Vocal fold paralysis","Why is side and vagal/RLN localization important?","The nerve can be injured anywhere from skull base to mediastinum depending on branch level; localization determines the necessary etiologic workup.","Work up"),
("Laryngology","Injection augmentation","What problem does vocal-fold injection primarily solve?","Glottic insufficiency by improving closure; it does not restore neural motion.","Manage"),
("Laryngology","Aspiration","Why distinguish safety from efficiency in swallowing?","A patient can swallow inefficiently with residue without aspirating, or aspirate despite efficient bolus transit; rehabilitation targets the actual physiologic deficit.","Localize"),
("Laryngology","Posterior glottic stenosis","Why can bilateral vocal-fold immobility be misleading?","Fixation from posterior glottic scar/cricoarytenoid restriction can mimic bilateral neurogenic paralysis; history and operative examination distinguish them.","Work up"),
# Facial plastics/trauma
("Facial Plastics","Nasal valve","Why does valve diagnosis matter before septoplasty?","A septoplasty may straighten the septum but leave the dominant airflow bottleneck untreated if lateral-wall/internal-valve dysfunction is present.","Work up"),
("Trauma","Orbital floor fracture","What functional findings matter more than the CT defect alone?","Diplopia/extraocular motility restriction, entrapment physiology, globe position, vision and oculocardiac symptoms guide urgency and repair decisions.","Manage"),
("Trauma","Mandible fracture","Why is occlusion central to mandibular fracture assessment?","Dental occlusion is a functional readout of mandibular alignment and helps localize displacement and judge reduction.","Localize"),
("Reconstruction","Local flap","Why plan around relaxed skin tension lines and aesthetic units?","Incision/scar placement and tissue recruitment strongly affect contour, distortion and scar visibility.","Operate"),
# Sleep
("Sleep","AHI","Why should AHI not be the only PSG number you read?","Event type, oxygen nadir/burden, arousals, sleep stage/position, hypoventilation and symptoms/comorbidities can materially change clinical interpretation.","Work up"),
("Sleep","DISE","What question does DISE answer?","It characterizes dynamic sleep-state upper-airway collapse patterns to help phenotype obstruction and plan selected non-PAP interventions.","Work up"),
("Sleep","HNS","Why is DISE relevant to hypoglossal nerve stimulation candidacy?","Collapse pattern matters; complete concentric palatal collapse is an important candidacy consideration for conventional HNS pathways.","Manage"),
("Sleep","Pediatric PSG","Why can't adult AHI thresholds simply be applied to children?","Pediatric sleep-disordered breathing uses age-specific interpretation because relatively few events can be clinically meaningful in children.","Work up"),
# General/emergency
("Emergency","Post-tonsil bleed","What is the first mental model for post-tonsillectomy hemorrhage?","Treat it as a potentially unstable airway/hemorrhage problem: assess airway and hemodynamics, obtain appropriate access/resuscitation and escalate for definitive control based on active bleeding and risk.","Manage"),
("Emergency","Deep neck infection","Why can CT wait in an unstable patient?","Imaging does not protect a deteriorating airway; stabilization and a rescue strategy take precedence when physiology is threatened.","Manage"),
("Emergency","Tracheostomy displacement","What single fact changes the replacement strategy most?","Whether the tract is fresh or mature, along with whether the upper airway is usable; blind replacement of a fresh tract can create a false passage.","Manage"),
("Emergency","Chyle leak","Why is a left lower-neck operation particularly associated with chyle leak?","The thoracic duct terminates near the left venous angle and can be injured during low lateral-neck dissection.","Localize")
]

# Make core knowledge available as attending-style retrieval without duplicating IDs.
for i,(domain,concept,prompt,answer,stage) in enumerate(CORE_KNOWLEDGE_V5,1):
    ATTENDING_LEVEL_PROMPTS["resident" if stage in ("Recognize","Localize","Work up") else "senior"].append(
      {"domain":domain,"concept_id":"v5:"+concept.lower().replace(" ","_"),
       "prompt":prompt,"answer":answer}
    )


# =============================================================================
# ENT Mastery v6.0 — Adaptive Daily Path + Deep Curriculum Layer
# =============================================================================

# Structured high-yield teaching modules. These complement (not replace) the
# existing integrated cases, interpretation labs, OR prep, and attending bank.
DEEP_MODULES_V6 = {
"Otology / Neurotology":[
 {"topic":"Acute Otitis Externa","recognize":"Canal pain, tragal/pinna tenderness, edema/debris; distinguish focal furunculosis from diffuse OE and look for extension/red flags.",
  "localize":"External auditory canal skin/subcutaneous tissues; furunculosis classically involves the hair-bearing lateral canal.",
  "workup":"Usually clinical. Clear enough debris for examination when safe; assess TM, diabetes/immunocompromise, cranial neuropathy or disproportionate pain when severe disease is possible.",
  "manage":"Topical therapy and aural toilet/wick when needed for uncomplicated diffuse OE; focal abscess/furunculosis may require drainage when fluctuant plus antistaphylococcal strategy based on severity/local resistance. Escalate suspected necrotizing disease.",
  "operate":"Know canal anatomy, TM status and when manipulation/drainage is appropriate versus harmful.",
  "teach":"Persistent granulation, severe nocturnal pain, immunocompromise or cranial neuropathy should break the 'simple swimmer's ear' frame."},
 {"topic":"Chronic Otitis Media / Cholesteatoma","recognize":"Retraction pocket, keratin debris, attic/posterosuperior disease, chronic drainage or conductive loss; recognize complications.",
  "localize":"Epitympanum, mesotympanum, sinus tympani, facial recess and mastoid pathways determine hidden disease.",
  "workup":"Microscopic/endoscopic exam, audiometry, and temporal-bone CT when extent/complications/anatomy will change surgery; diffusion-weighted MRI can help in selected residual/recurrent disease questions.",
  "manage":"Unsafe keratinizing disease generally requires surgical disease control; tailor approach to extent, anatomy, hearing and surveillance.",
  "operate":"Mastoid map: tegmen, sigmoid, EAC, lateral canal, incus/fossa incudis, facial nerve, digastric ridge; prioritize a safe maintainable ear.",
  "teach":"Canal-wall strategy is not a prestige ranking: disease clearance and reliable surveillance dominate."},
 {"topic":"Sudden Sensorineural Hearing Loss","recognize":"Rapid unilateral sensorineural loss may be described as fullness or a blocked ear; do not mistake it for routine ET dysfunction.",
  "localize":"Cochlear/retrocochlear rather than external or middle ear after bedside/audiometric localization.",
  "workup":"Prompt audiometry; targeted evaluation for retrocochlear pathology and associated neurologic/otologic features. Avoid low-yield shotgun testing.",
  "manage":"Time-sensitive counseling and evidence-based steroid strategy when appropriate; discuss salvage options and hearing rehabilitation/follow-up.",
  "operate":"Not primarily an operative disorder; procedural treatment is adjunctive in selected patients.",
  "teach":"The key resident skill is recognizing the time-sensitive sensorineural phenotype before the treatment window is lost."},
 {"topic":"Otosclerosis / Stapes Fixation","recognize":"Progressive conductive hearing loss with a normal-appearing TM; supportive audiometric patterns may include a Carhart-type notch.",
  "localize":"Mechanical fixation at the stapes/oval-window system; separate from ossicular discontinuity and third-window physiology.",
  "workup":"Complete audiometry, speech testing and middle-ear measures; imaging only when the diagnosis/anatomy is atypical or would change planning.",
  "manage":"Observation, amplification or stapes surgery depending on hearing burden, anatomy, patient goals and operative candidacy.",
  "operate":"Understand oval-window anatomy, facial nerve, chorda, incus/stapes relationships and inner-ear risk.",
  "teach":"A Carhart notch supports a mechanical hypothesis but is not pathognomonic."},
 {"topic":"Vestibular Schwannoma","recognize":"Asymmetric SNHL, disproportionate speech discrimination, unilateral tinnitus or vestibular symptoms can trigger retrocochlear evaluation.",
  "localize":"Vestibular portion of CN VIII in the IAC/CPA with implications for cochlear and facial nerves and brainstem.",
  "workup":"Audiometry and contrast-enhanced MRI/IAC evaluation when indicated; characterize size, growth, hearing and symptoms.",
  "manage":"Observation, radiation or microsurgery depends on size/growth, age/comorbidity, hearing, symptoms and patient goals.",
  "operate":"Know translabyrinthine, retrosigmoid and middle-fossa conceptual tradeoffs; approach choice is driven by tumor/hearing/anatomy.",
  "teach":"Management is not 'tumor present = remove'; natural history and functional goals matter."},
],
"Rhinology / Allergy / Skull Base":[
 {"topic":"Allergic Rhinitis","recognize":"Sneezing, itching, watery rhinorrhea and congestion with allergic triggers; distinguish inflammatory congestion from fixed obstruction.",
  "localize":"IgE-mediated mucosal disease affecting nasal airway resistance and turbinate congestion.",
  "workup":"History/exam often establish the syndrome; allergy testing is useful when confirmation will change avoidance, immunotherapy or diagnostic thinking.",
  "manage":"Environmental strategy, intranasal corticosteroid/antihistamine approaches and immunotherapy in selected patients; treat coexisting structural disease separately.",
  "operate":"Surgery does not treat the allergic mechanism; turbinate/structural procedures target persistent anatomic obstruction in selected patients.",
  "teach":"A large turbinate is a finding; ask whether the driver is reversible mucosal inflammation, fixed tissue/bone, or both."},
 {"topic":"CRS Phenotyping","recognize":"Chronic characteristic sinonasal symptoms plus objective inflammation; distinguish CRSsNP, CRSwNP and special phenotypes such as AERD/AFRS.",
  "localize":"Map disease by sinus drainage pathways and endoscopic/CT distribution rather than treating 'sinusitis' as one cavity.",
  "workup":"Nasal endoscopy and/or CT for objective confirmation and surgical planning; evaluate modifying conditions and inflammatory phenotype when relevant.",
  "manage":"Topical therapy is foundational; systemic therapy, biologics and surgery are selected by phenotype, severity, prior response and patient goals.",
  "operate":"ESS should be disease- and anatomy-specific and create safe access for ventilation, topical delivery and surveillance.",
  "teach":"CRS is chronic inflammatory disease with an anatomic interface, not simply retained mucus that surgery cures."},
 {"topic":"AERD","recognize":"Asthma + CRSwNP + respiratory reactions to aspirin/COX-1 NSAIDs.",
  "localize":"Systemic/type-2 inflammatory phenotype with upper and lower airway manifestations.",
  "workup":"Careful reaction history and multidisciplinary assessment; challenge/testing only in appropriate specialized contexts.",
  "manage":"Optimize topical therapy, asthma care, sinus surgery when indicated, and phenotype-directed options including aspirin desensitization or biologic therapy in selected patients.",
  "operate":"ESS can reduce burden and improve topical access but does not remove the underlying inflammatory tendency.",
  "teach":"Ask about NSAID reactions in severe recurrent polyposis rather than waiting for the patient to volunteer the connection."},
 {"topic":"Frontal Recess / Frontal Sinus","recognize":"Frontal disease demands precise preoperative CT understanding because small anatomic variations change drainage and skull-base/orbital risk.",
  "localize":"Agger nasi/frontal cells, frontal beak, orbit and anterior skull base define the pathway.",
  "workup":"Study multiplanar CT and identify the actual frontal drainage pathway before surgery.",
  "manage":"Operate for appropriate disease burden after diagnosis/medical strategy; extent should match pathology and anatomy.",
  "operate":"Preserve orientation to orbit and skull base, remove obstructing partitions deliberately, and create durable drainage while limiting mucosal trauma.",
  "teach":"Do not 'hunt for the frontal sinus'; reconstruct the drainage pathway from CT and landmarks."},
 {"topic":"CSF Rhinorrhea","recognize":"Persistent unilateral watery rhinorrhea, salty/positional drainage, meningitis, trauma/surgery or spontaneous-leak risk factors should trigger a CSF hypothesis.",
  "localize":"Anterior/central skull-base defect with meningeal communication; site determines endoscopic approach.",
  "workup":"Confirm fluid with appropriate CSF-specific testing when available and localize with high-resolution imaging; evaluate causes such as elevated intracranial pressure in spontaneous leaks.",
  "manage":"Definitive repair strategy depends on site/flow/etiology; address contributing intracranial-pressure physiology when relevant.",
  "operate":"Know skull-base, orbit, olfactory and vascular relationships; multilayer closure concepts depend on defect and flow.",
  "teach":"A successful patch without addressing the reason a spontaneous leak occurred can set up recurrence."},
],
"Head & Neck Oncology":[
 {"topic":"HPV-Associated Oropharyngeal SCC","recognize":"Adult cystic lateral neck node may be the presenting sign of a subtle tonsil/base-of-tongue primary.",
  "localize":"Oropharyngeal lymphoid sites with predictable cervical nodal drainage.",
  "workup":"Complete mucosal examination, appropriate imaging and carefully planned tissue diagnosis; avoid casually excising a presumed branchial cyst in an adult.",
  "manage":"Treatment is stage- and patient-specific and may involve transoral surgery/neck treatment or radiation-based strategies; preserve swallowing and long-term function.",
  "operate":"Understand tonsillar/BOT anatomy, lingual artery risk, pharyngeal constrictor/parapharyngeal relationships and neck compartments.",
  "teach":"In an adult, a new lateral cystic neck mass is metastatic disease until convincingly proven otherwise."},
 {"topic":"Laryngeal SCC","recognize":"Persistent dysphonia, odynophagia, otalgia, airway symptoms or suspicious mucosal lesion require visualization and tissue diagnosis.",
  "localize":"Glottic, supraglottic and subglottic subsites have different lymphatics and functional implications; mobility reflects deeper involvement.",
  "workup":"Flexible exam, direct laryngoscopy/biopsy and stage-appropriate imaging; document vocal-fold mobility and airway.",
  "manage":"Early disease may be treated surgically or with radiation; advanced disease requires organ-preservation versus surgical strategies based on extent/function and patient factors.",
  "operate":"Oncologic margins must be integrated with airway, voice and swallow consequences; neck treatment follows subsite/stage biology.",
  "teach":"An anatomically preserved larynx is not necessarily a functional larynx."},
 {"topic":"Unknown Primary with Cervical Metastasis","recognize":"Metastatic SCC in a cervical node with no obvious mucosal primary is a defined oncologic problem, not merely 'neck cancer.'",
  "localize":"Nodal level, HPV/EBV status and histology point toward likely mucosal sites.",
  "workup":"Directed exam, cross-sectional/PET imaging as appropriate, pathologic viral markers and operative evaluation of likely sites.",
  "manage":"Treatment integrates the neck and likely/identified mucosal site while minimizing unnecessary radiation/surgical morbidity.",
  "operate":"Diagnostic procedures should be planned to maximize primary detection without compromising definitive treatment.",
  "teach":"Use nodal biology to reverse-map the likely primary."},
 {"topic":"Neck Dissection","recognize":"Therapeutic versus elective neck treatment follows primary-site drainage and nodal risk.",
  "localize":"Know levels I–VII and the SAN, IJV, carotid/vagus, phrenic, sympathetic chain, brachial plexus and thoracic duct relationships.",
  "workup":"Map clinical nodal disease by imaging/exam and understand which compartments require treatment.",
  "manage":"Selective, modified radical or radical concepts reflect oncologic extent and structures preserved, not arbitrary naming.",
  "operate":"Perform compartmental clearance while preserving uninvolved critical structures when oncologically safe.",
  "teach":"A neck dissection is lymphatic-compartment surgery, not removal of visible nodes."},
 {"topic":"Cutaneous SCC / Melanoma of Head & Neck","recognize":"Risk depends on histology, site, size/depth, nerve symptoms, recurrence, immunosuppression and nodal findings.",
  "localize":"Understand regional lymphatic basins including parotid/intraparotid nodes for many facial/scalp sites.",
  "workup":"Biopsy that preserves staging information, nodal examination and risk-directed imaging/staging.",
  "manage":"Definitive excision/Mohs pathways, nodal management and adjuvant therapy depend on tumor type and risk.",
  "operate":"Plan oncologic resection and reconstruction together; facial nerve and aesthetic-unit function matter.",
  "teach":"The reconstruction should never obscure whether the cancer operation was adequate."},
],
"Thyroid / Parathyroid / Salivary":[
 {"topic":"Thyroid Nodule","recognize":"A nodule is a risk-stratification problem, not automatically a surgical diagnosis.",
  "localize":"Intrathyroidal lesion plus cervical nodal compartments; assess compressive/invasive relationships.",
  "workup":"TSH, dedicated thyroid/neck ultrasound and risk-directed FNA/functional evaluation; voice assessment when indicated.",
  "manage":"Observation, surveillance, ablation in selected benign contexts, lobectomy or total thyroidectomy depends on diagnosis, risk and goals.",
  "operate":"Match extent to disease; pre-plan RLN/EBSLN, parathyroids and nodal strategy.",
  "teach":"Start with thyroid function and ultrasound risk, then ask what information will actually change treatment."},
 {"topic":"Differentiated Thyroid Cancer","recognize":"Papillary/follicular/oncocytic differentiated cancers have generally favorable biology but heterogeneous recurrence risk.",
  "localize":"Primary extent, gross extrathyroidal extension and central/lateral nodal disease drive surgical planning.",
  "workup":"High-quality ultrasound/nodal mapping, pathology and selective cross-sectional imaging; use contemporary risk stratification.",
  "manage":"2025 ATA guidance emphasizes individualized extent, including lobectomy for selected low-risk unilateral disease and shared decision-making.",
  "operate":"Achieve oncologic resection while preserving RLN/EBSLN and viable parathyroids; perform therapeutic compartmental nodal surgery when indicated.",
  "teach":"Cancer histology alone does not answer lobectomy versus total thyroidectomy."},
 {"topic":"Primary Hyperparathyroidism","recognize":"Biochemical hypercalcemia with inappropriately elevated/non-suppressed PTH establishes the physiologic problem.",
  "localize":"Localization studies identify likely abnormal gland(s) only after the biochemical diagnosis and help plan focused versus broader exploration.",
  "workup":"Confirm calcium/PTH physiology, renal/bone implications and relevant differential; localization may use ultrasound/nuclear or advanced modalities by context.",
  "manage":"Surgical candidacy depends on symptoms/complications and accepted criteria; plan perioperative calcium strategy.",
  "operate":"Know superior/inferior embryology, RLN relationship, thyrothymic ligament/thymic descent and ectopic sites; intraoperative PTH can assess biochemical response.",
  "teach":"Never use a negative localization study to declare that biochemical hyperparathyroidism does not exist."},
 {"topic":"Salivary Gland Malignancy","recognize":"Pain, rapid growth, fixation, facial weakness or nodes increase concern, but indolent malignancies can still look benign.",
  "localize":"Superficial/deep parotid, facial-nerve relationship, submandibular space and regional nodes.",
  "workup":"Imaging and needle-based tissue diagnosis/risk stratification should answer questions that alter extent, nerve/neck planning or adjuvant care.",
  "manage":"Histology, grade, stage, margins, PNI and nodal risk drive surgery and postoperative radiation discussions.",
  "operate":"Preserve functioning uninvolved nerve when oncologically appropriate; plan nerve reconstruction when sacrifice is required.",
  "teach":"Salivary pathology matters because grade and PNI change what the surgeon does."},
],
"Pediatric Otolaryngology":[
 {"topic":"AOM / OME / Tympanostomy Decisions","recognize":"AOM is acute middle-ear inflammation/infection; OME is effusion without the acute syndrome.",
  "localize":"Middle-ear ventilation and Eustachian-tube function affect hearing and recurrent disease.",
  "workup":"Pneumatic otoscopy/tympanometry and hearing evaluation when disease duration/risk makes function important.",
  "manage":"Observation, antimicrobial treatment for appropriate AOM, and tubes for guideline-supported phenotypes rather than infection count alone.",
  "operate":"Safe myringotomy/tube placement requires TM quadrant/ossicular awareness and postoperative otorrhea counseling.",
  "teach":"Ask what the ears look like today and what the child's hearing/developmental risk is before reducing the decision to a number of infections."},
 {"topic":"Pediatric OSA / Adenotonsillar Disease","recognize":"Snoring plus obstructive symptoms, sleep disturbance or daytime consequences; tonsil size alone does not measure severity.",
  "localize":"Adenotonsillar tissue is common but obstruction can be multilevel and modified by obesity, craniofacial or neuromuscular disease.",
  "workup":"History/exam and PSG in indicated/high-risk/discordant contexts; read pediatric oxygenation and event burden with age-appropriate interpretation.",
  "manage":"Adenotonsillectomy is common first-line surgery in appropriate patients; plan residual-disease strategy and postoperative monitoring by risk.",
  "operate":"Balance tonsil/adenoid removal with hemostasis, airway risk, pain control and velopharyngeal/Eustachian anatomy.",
  "teach":"Adenotonsillectomy treats a major anatomic contributor; it does not guarantee cure of every child's OSA."},
 {"topic":"Congenital Neck Masses","recognize":"Age, midline/lateral location, movement with swallowing/tongue protrusion, infection history and skin pits narrow the differential.",
  "localize":"Thyroglossal tract, branchial cleft pathways, dermoid planes and vascular/lymphatic malformations have characteristic relationships.",
  "workup":"Ultrasound is often useful; CT/MRI depends on depth/complexity; confirm normally located thyroid tissue when relevant to thyroglossal disease.",
  "manage":"Observation, infection control, sclerotherapy or surgery depends on lesion biology and symptoms.",
  "operate":"Definitive congenital tract surgery requires embryologic understanding; incomplete tract management drives recurrence.",
  "teach":"Do not memorize masses as names—map them to embryology and neck anatomy."},
 {"topic":"Pediatric Airway Foreign Body","recognize":"Sudden choking/cough, unilateral wheeze or unexplained persistent respiratory symptoms can occur even with a normal radiograph.",
  "localize":"Laryngeal/tracheal foreign bodies threaten the airway; bronchial objects produce asymmetric distal physiology.",
  "workup":"History is crucial; imaging may support but cannot exclude radiolucent aspiration when suspicion is high.",
  "manage":"Escalate unstable obstruction immediately; rigid bronchoscopy remains definitive diagnosis/therapy for appropriate suspected airway foreign body.",
  "operate":"Coordinate anesthesia and bronchoscopy with a shared ventilation/rescue plan; remove the object without converting partial to complete obstruction.",
  "teach":"A normal chest x-ray does not overrule a classic aspiration history."},
],
"Laryngology / Voice / Swallowing":[
 {"topic":"Unilateral Vocal Fold Paralysis","recognize":"Breathy dysphonia, weak cough and aspiration symptoms with unilateral immobility on laryngoscopy.",
  "localize":"Localize vagus versus RLN based on associated palatal/pharyngeal findings and image the nerve course when etiology is unexplained.",
  "workup":"Laryngoscopy/stroboscopy, voice/swallow assessment and etiologic imaging/workup based on localization and surgical history.",
  "manage":"Observation for recovery when appropriate, voice therapy, injection augmentation or durable framework/reinnervation strategies based on prognosis and goals.",
  "operate":"Injection improves closure; medialization changes position; reinnervation targets tone—none simply 'turns the nerve back on.'",
  "teach":"Separate motion recovery, glottic closure, voice quality and swallowing safety as different outcomes."},
 {"topic":"Benign Vocal Fold Lesions","recognize":"Nodules, polyps, cysts and reactive lesions differ in morphology, laterality and vibratory effect.",
  "localize":"Superficial lamina propria and epithelial mechanics determine mucosal wave disturbance.",
  "workup":"Stroboscopy plus voice-use history; identify phonotraumatic and reflux/irritant contributors without attributing everything to reflux.",
  "manage":"Voice therapy is foundational for many phonotraumatic lesions; surgery is selected when lesion biology and functional burden justify it.",
  "operate":"Microlaryngeal surgery should preserve layered vibratory tissue and avoid unnecessary deep injury/scar.",
  "teach":"The operation can remove a lesion and still worsen the voice if it damages the vibratory cover."},
 {"topic":"Dysphagia / Aspiration","recognize":"Coughing, wet voice, recurrent pneumonia, weight loss or prolonged meals can signal impaired swallow safety or efficiency.",
  "localize":"Oral, pharyngeal and esophageal phases; identify timing and mechanism rather than labeling all symptoms 'aspiration.'",
  "workup":"FEES and modified barium swallow answer complementary questions; select based on physiology you need to observe.",
  "manage":"Rehabilitation, diet/strategy modification and procedural/surgical treatment should target the demonstrated deficit.",
  "operate":"Procedures for glottic insufficiency, UES dysfunction or structural disease should have a defined physiologic target.",
  "teach":"A test result is useful only if you can state which swallow impairment it demonstrated and how that changes treatment."},
 {"topic":"Subglottic / Tracheal Stenosis","recognize":"Biphasic stridor, exertional dyspnea or failed extubation can reflect fixed central airway narrowing.",
  "localize":"Define glottic, subglottic and tracheal level; length, circumference, cartilage and posterior involvement matter.",
  "workup":"Endoscopic assessment is central; imaging and pulmonary testing add selected structural/functional information.",
  "manage":"Endoscopic dilation/incision, open expansion or resection depends on stenosis biology, length, grade, framework and prior response.",
  "operate":"Airway enlargement must be balanced against voice, swallowing and framework stability.",
  "teach":"Grade alone never selects the reconstruction."},
],
"Facial Plastics / Trauma":[
 {"topic":"Functional Nasal Obstruction","recognize":"Symptoms can arise from septum, turbinates, internal/external valve, dynamic lateral-wall collapse or mucosal disease.",
  "localize":"Identify the actual narrow segment and whether it is static, dynamic, inflammatory or structural.",
  "workup":"Anterior rhinoscopy/endoscopy, dynamic maneuvers and response to decongestion/support help define contributors.",
  "manage":"Medical therapy treats mucosa; septoplasty/turbinate/valve procedures target distinct structural problems and may need combination treatment.",
  "operate":"Preserve dorsal/caudal support and design valve repair around the mechanical failure rather than a generic graft recipe.",
  "teach":"A deviated septum on exam does not prove it is the dominant cause of obstruction."},
 {"topic":"ZMC / Orbital Trauma","recognize":"Malar flattening, trismus, infraorbital numbness, diplopia or globe displacement suggest zygomaticomaxillary/orbital injury.",
  "localize":"Zygomaticofrontal, zygomaticomaxillary, arch and orbital articulations determine three-dimensional displacement.",
  "workup":"Thin-cut facial CT and complete ocular examination; vision-threatening problems supersede cosmetic fracture planning.",
  "manage":"Observation versus repair depends on displacement and functional/aesthetic consequences, not CT fracture presence alone.",
  "operate":"Restore three-dimensional projection/orbital volume while protecting globe, infraorbital nerve and fixation sites.",
  "teach":"In facial trauma, vision comes before fracture reduction."},
 {"topic":"Mandible Fracture","recognize":"Malocclusion, trismus, step-off, lower-lip numbness or intraoral laceration can signal fracture.",
  "localize":"Symphysis/body/angle/ramus/condyle location predicts displacement and fixation considerations.",
  "workup":"Occlusal exam and CT/panoramic imaging as appropriate; assess dentition, open fracture status and airway.",
  "manage":"Closed versus open reduction/fixation depends on fracture pattern, displacement, occlusion, dentition and patient factors.",
  "operate":"Restore occlusion and stable bony alignment while protecting tooth roots and inferior alveolar nerve.",
  "teach":"Occlusion is the functional reduction guide."},
 {"topic":"Local Flap Reconstruction","recognize":"Defect depth, subunit, exposed critical structures and tissue laxity determine reconstructive options.",
  "localize":"Aesthetic units, relaxed tension lines, vascular territories and free margins matter.",
  "workup":"Plan after definitive oncologic defect is understood; evaluate surrounding tissue quality and prior radiation.",
  "manage":"Use the simplest option that reliably restores function and contour without distorting adjacent landmarks.",
  "operate":"Design tissue movement and standing-cone management before incision; protect pedicle and avoid tension across free margins.",
  "teach":"The reconstructive ladder is not a mandate to use the simplest technique when it gives a predictably poor functional result."},
],
"Sleep Surgery":[
 {"topic":"Adult PSG Interpretation","recognize":"OSA severity cannot be understood from AHI alone.",
  "localize":"PSG quantifies sleep-state physiology but does not directly localize the anatomic site of collapse.",
  "workup":"Read event type, AHI/RDI, oxygen nadir/burden, sleep stage/position, arousals and hypoventilation plus symptoms/comorbidity.",
  "manage":"PAP remains foundational; alternatives are selected by severity, anatomy, tolerance, dentition, weight and patient goals.",
  "operate":"Surgical planning requires phenotype/anatomic evaluation rather than choosing a procedure from AHI.",
  "teach":"Always ask what the PSG says about physiology and what it cannot tell you about anatomy."},
 {"topic":"DISE","recognize":"Drug-induced sleep endoscopy samples dynamic collapse under sedated sleep-like conditions.",
  "localize":"Characterize velum, oropharyngeal lateral wall, tongue base and epiglottic collapse patterns.",
  "workup":"Use when dynamic phenotype will change non-PAP surgical/device planning; interpret within limitations of sedation and scoring.",
  "manage":"DISE can guide palatal/tongue-base/device strategy but is not a stand-alone indication for surgery.",
  "operate":"Maintain a standardized observation and airway plan; document pattern/degree of collapse reproducibly.",
  "teach":"DISE is an anatomic-phenotyping tool, not a sleep-study replacement."},
 {"topic":"Hypoglossal Nerve Stimulation","recognize":"Selected adults with OSA who cannot adequately use PAP may be candidates after physiologic/anatomic screening.",
  "localize":"Stimulation recruits tongue protrusor function through selected hypoglossal branches; sensing coordinates therapy with respiration.",
  "workup":"Confirm PSG eligibility, PAP history, anatomy and DISE collapse pattern; evaluate other program-specific criteria.",
  "manage":"Implantation is followed by activation, titration/programming and longitudinal outcome assessment rather than immediate cure.",
  "operate":"Understand hypoglossal branching, cuff placement concept, respiratory sensor and generator pathway while protecting adjacent nerves/vessels.",
  "teach":"HNS is a pathway—selection, implantation, activation, programming and reassessment—not merely an operation."},
],
"General ENT / Emergencies":[
 {"topic":"Post-Tonsillectomy Hemorrhage","recognize":"Any significant postoperative oral bleeding is potentially dangerous because blood loss may be underestimated and airway risk can evolve.",
  "localize":"Tonsillar fossae with primary versus delayed bleeding patterns; clot does not guarantee hemostasis.",
  "workup":"Assess airway, hemodynamics, bleeding activity, access/labs/type and screen as appropriate without delaying needed control.",
  "manage":"Resuscitate and escalate based on active bleeding/risk; operative control is required for unstable or significant ongoing hemorrhage.",
  "operate":"Airway and hemorrhage teams need a shared plan; suction, exposure and hemostasis must account for a stomach/airway potentially full of blood.",
  "teach":"A normal blood pressure does not prove a child has not lost significant blood."},
 {"topic":"Deep Neck Space Infection","recognize":"Fever, neck swelling, trismus, muffled voice, drooling, toxic appearance or airway symptoms can indicate deep-space infection.",
  "localize":"Peritonsillar, parapharyngeal, retropharyngeal and danger-space anatomy predicts airway, vascular and mediastinal complications.",
  "workup":"If stable, contrast imaging can define space, abscess versus phlegmon, source and complications; unstable airway physiology takes priority.",
  "manage":"Airway strategy, antimicrobials, hydration and source control/drainage when indicated.",
  "operate":"Plan approach around the involved space and carotid/cranial-nerve relationships; obtain cultures when useful without delaying critical treatment.",
  "teach":"Do not send an unstable drooling patient away from airway expertise just to obtain a prettier CT."},
 {"topic":"Tracheostomy Emergency","recognize":"Obstruction, displacement, bleeding and false passage are distinct emergencies with different rescue logic.",
  "localize":"Tube, stoma/tract maturity, tracheal lumen and upper-airway patency determine options.",
  "workup":"Immediate bedside assessment is physiologic: oxygenation/ventilation, tube patency/position and whether the upper airway is usable.",
  "manage":"Remove simple obstruction and restore oxygenation; fresh dislodgement requires extreme caution because blind reinsertion can create a false passage.",
  "operate":"Know tube type/size, date of placement, stay sutures/maturation strategy and rescue equipment before problems occur.",
  "teach":"The first question in a displaced trach is not 'what size tube?'—it is 'how mature is the tract and can I ventilate from above?'."},
 {"topic":"Epistaxis","recognize":"Differentiate minor anterior bleeding from severe/posterior bleeding with airway or hemodynamic consequences.",
  "localize":"Anterior septal plexus is common; posterior/lateral sources and arterial anatomy matter in refractory disease.",
  "workup":"Focused medication/coagulopathy history and visualization after clot clearance/vasoconstriction when safe; labs/imaging are selective.",
  "manage":"Compression/topical vasoconstriction, directed cautery/packing and escalation to endoscopic arterial control or embolization depending on severity and failure.",
  "operate":"Understand sphenopalatine artery branches, posterior septal/lateral nasal anatomy and risks of packing/arterial control.",
  "teach":"Treat the patient and source, not just the blood you can see."},
]
}

# A curriculum item object used by the adaptive planner.
def _v6_item_id(domain, topic):
    import re as _re
    return "v6-" + _re.sub(r"[^a-z0-9]+","-", (domain+"-"+topic).lower()).strip("-")

ADAPTIVE_ITEMS_V6=[]
for _domain,_mods in DEEP_MODULES_V6.items():
    for _m in _mods:
        _id=_v6_item_id(_domain,_m["topic"])
        for _stage in ["recognize","localize","workup","manage","operate","teach"]:
            ADAPTIVE_ITEMS_V6.append({
              "id":_id+"-"+_stage,
              "concept_id":_id,
              "domain":_domain,
              "topic":_m["topic"],
              "stage":_stage,
              "prompt":{
                "recognize":"Recognize the clinical pattern and the dangerous mimic.",
                "localize":"Localize the problem anatomically/physiologically.",
                "workup":"Choose the workup that changes management.",
                "manage":"Build the management plan and escalation threshold.",
                "operate":"Give the operative/procedural mental model: indication, landmarks, danger structures and complications.",
                "teach":"Teach the attending-level mental model in a few sentences."
              }[_stage],
              "answer":_m[_stage],
              "minutes":{"recognize":3,"localize":3,"workup":4,"manage":4,"operate":6,"teach":4}[_stage],
              "level":{"recognize":1,"localize":2,"workup":3,"manage":4,"operate":5,"teach":6}[_stage]
            })

# Review intervals after a successful exposure at each spiral level.
REVIEW_INTERVALS_V6={1:1,2:3,3:7,4:14,5:30,6:60}

# Major-source hierarchy displayed to the learner.
EVIDENCE_HIERARCHY_V6 = [
 {"tier":"Current guidance","use":"Management recommendations and time-sensitive standards","examples":"Current specialty society guidelines/consensus; e.g., 2025 ATA DTC and 2025 AAO-HNSF adult sinusitis/surgical CRS where applicable."},
 {"tier":"Core reference texts","use":"Anatomy, physiology, differential diagnosis, operative mental models","examples":"User-provided ENT references including Pasha, pediatric otolaryngology, operative otolaryngology, otoscopy atlas and other uploaded texts."},
 {"tier":"Visual atlases","use":"Pattern recognition and image interpretation","examples":"Otoscopy atlas and permitted external educational atlases; link externally rather than copying restricted media."},
 {"tier":"Teaching synthesis","use":"Cases, retrieval prompts, attending questions and sequencing","examples":"ENT Mastery synthesis derived from the above; not a substitute for local protocols or attending preference."}
]


# =============================================================================
# ENT Mastery v7.0 — Content Saturation Layer
# =============================================================================
SATURATION_TOPICS_V7 = [('Otology / Neurotology', 'Temporal Bone Anatomy', 'Think in compartments: EAC/TM → middle ear/ossicles → mastoid/epitympanum → otic capsule/IAC; constantly map facial nerve, labyrinth, tegmen, sigmoid and carotid/jugular structures.', 'Use CT for bony anatomy and MRI for soft-tissue/IAC/CPA questions; choose planes/sequences to answer a defined localization question.', 'Management is diagnosis-specific; anatomy determines whether observation, medical treatment, transcanal, mastoid or skull-base access is safe.', 'Board pearl: mastoid drilling is boundary-based spatial reasoning, not drilling toward a memorized target.'), ('Otology / Neurotology', 'Audiogram Interpretation', 'First decide reliability, then air vs bone thresholds, conductive vs SN vs mixed pattern, symmetry, configuration, speech reception/word recognition and whether results fit the exam.', 'Pair pure tones with speech testing and tympanometry; asymmetric SN loss or unexpectedly poor speech performance can trigger retrocochlear evaluation.', 'Treat the cause when reversible; otherwise match amplification, surgery or implantable rehabilitation to type/severity and goals.', 'Never interpret a single threshold in isolation; the audiogram is a localization test.'), ('Otology / Neurotology', 'Tympanometry / Acoustic Reflexes', 'Tympanometry measures middle-ear system behavior, not hearing. Interpret curve shape together with ear-canal volume and otoscopy.', 'Flat tracing + normal volume supports effusion; large volume suggests perforation/patent tube; reflex patterns can add localization but must fit the audiogram.', 'Use results to clarify middle-ear status and avoid unnecessary imaging/testing when the bedside diagnosis is already clear.', 'A Type A tympanogram does not guarantee normal hearing.'), ('Otology / Neurotology', 'Eustachian Tube Dysfunction', 'Separate obstructive pressure-dysregulation from patulous symptoms; do not equate every complaint of fullness with ETD.', 'History, otoscopy and tympanometry during symptoms are central; evaluate nasal/nasopharyngeal contributors when indicated.', 'Treat underlying nasal inflammation when present; pressure equalization, tubes or balloon dilation are selected for appropriate persistent obstructive phenotypes.', 'Unilateral adult effusion requires thought about nasopharyngeal obstruction rather than reflexively labeling ETD.'), ('Otology / Neurotology', 'Tympanic Membrane Perforation', 'Characterize acute vs chronic, size/site, edge, infection, hearing loss and ossicular/inner-ear clues.', 'Otoscopy/microscopy and audiometry; CT only when trauma, cholesteatoma, ossicular injury or other deeper disease is suspected.', 'Keep ear dry, treat infection when present, observe many acute perforations; tympanoplasty for persistent symptomatic/performance-limiting perforation when appropriate.', 'A perforation is a window into middle-ear disease, not always the primary diagnosis.'), ('Otology / Neurotology', 'Ossicular Discontinuity', 'Think mechanical interruption when conductive loss is disproportionate to TM findings, especially after trauma/chronic ear disease.', 'Audiometry plus careful otoscopy; CT can define traumatic/chronic ossicular anatomy when it changes management.', 'Observation/amplification versus ossiculoplasty depends on hearing burden, middle-ear environment and associated disease.', 'Reconstruct only after creating a stable, aerated/safe middle ear.'), ('Otology / Neurotology', 'Superior Canal Dehiscence', 'Recognize a third-window syndrome: sound/pressure-induced vestibular symptoms, autophony and an apparent conductive component despite normal middle ear.', 'High-resolution CT in the correct plane plus physiologic testing such as VEMP when the clinical syndrome supports it; avoid diagnosing from CT alone.', 'Observation for mild symptoms; plugging/resurfacing approaches for disabling well-localized disease in selected patients.', 'Radiographic dehiscence is not synonymous with symptomatic syndrome.'), ('Otology / Neurotology', 'Ménière Disease', 'Episodic spontaneous vertigo plus fluctuating cochlear symptoms; distinguish from vestibular migraine and BPPV.', 'Audiometry documents hearing pattern; imaging is used selectively to exclude alternatives rather than prove Ménière disease.', 'Step from education/dietary-medical symptom control to intratympanic or surgical options for refractory disease while considering hearing status.', "Treat the patient's disabling phenotype, not just the label."), ('Otology / Neurotology', 'Vestibular Migraine', 'Recurrent vestibular symptoms with migraine biology can occur with or without simultaneous headache.', 'Diagnosis is clinical after appropriate exclusion; audiometry/vestibular testing are used when another otologic disorder remains plausible.', 'Migraine trigger/lifestyle strategy and preventive/abortive treatment are individualized; vestibular rehabilitation may help selected patients.', 'Do not force every episodic vertigo syndrome into an inner-ear structural diagnosis.'), ('Otology / Neurotology', 'Vestibular Neuritis', 'Acute prolonged vestibular syndrome with spontaneous nystagmus and gait imbalance but no new cochlear deficit suggests vestibular neuritis after central causes are excluded.', 'Bedside eye-movement examination is critical in the right patient; MRI is driven by central red flags/uncertainty, not routine reassurance.', 'Short-term symptom control, early mobilization/vestibular rehabilitation; avoid prolonged vestibular suppressants.', 'The dangerous mimic is posterior circulation stroke.'), ('Otology / Neurotology', 'BPPV', 'Brief positional vertigo with canal-specific positional nystagmus is a mechanical otolith disorder.', 'Dix-Hallpike or roll testing localizes the canal; routine imaging is unnecessary when classic.', 'Use the canal-appropriate repositioning maneuver rather than chronic vestibular suppressants.', 'Name the canal before choosing the maneuver.'), ('Otology / Neurotology', 'Facial Paralysis', 'Localize central vs peripheral and proximal vs distal; timing, completeness, pain, vesicles, trauma, tumor signs and other cranial neuropathies matter.', 'Document facial function systematically; image/lab selectively based on onset, recurrence, trauma, progressive course or atypical features.', 'Protect the eye immediately when closure is weak; etiology determines steroids/antivirals, decompression, reanimation or tumor treatment.', 'Eye protection is never optional while the diagnostic workup proceeds.'), ('Otology / Neurotology', 'Temporal Bone Fracture', 'Classify by otic-capsule involvement because it better predicts SNHL, facial injury and CSF leak than old longitudinal/transverse labels.', 'Thin-cut CT when indicated; document facial function, hearing, vestibular findings, CSF leak and vascular/neurologic injuries.', 'Manage associated brain/vascular injury first; facial nerve, CSF leak, hearing and vestibular sequelae are treated according to severity/timing.', 'Otic-capsule-violating injury carries higher risk of SNHL, facial nerve injury and CSF otorrhea.'), ('Otology / Neurotology', 'Cochlear Implant Candidacy', 'Think functional aided speech access, not audiogram severity alone; candidacy has expanded over time.', 'Comprehensive audiology with best-aided speech testing, otologic evaluation and imaging; pediatric workup also addresses development/etiology.', 'Implant when appropriately selected hearing aid users lack adequate benefit; rehabilitation and programming are part of treatment.', 'CI is a longitudinal hearing-rehabilitation pathway, not just an operation.'), ('Otology / Neurotology', 'Cochlear Implant Surgery', 'The operation creates atraumatic cochlear access while protecting facial nerve and device position.', 'Pre-op CT/MRI maps cochlear patency, malformations, facial nerve and mastoid anatomy.', 'Mastoidectomy/facial recess or alternative access, receiver placement, round-window/cochleostomy insertion and confirmation are tailored to anatomy/device.', 'Know facial recess boundaries and anticipate CSF gusher/anomalous nerve in malformed ears.'), ('Otology / Neurotology', 'Otosclerosis', 'Stapes fixation causes conductive mechanics with normal TM; cochlear involvement can add SN loss.', 'Audiometry/speech/tympanometry; CT selectively for atypical or revision anatomy.', 'Observation, hearing aid or stapedotomy based on burden, anatomy and preference.', 'Carhart notch is supportive, not diagnostic.'), ('Otology / Neurotology', 'Tinnitus', 'Separate pulsatile from nonpulsatile and unilateral/asymmetric from bilateral; identify hearing loss and neurologic/vascular red flags.', 'Audiometry is foundational; imaging is targeted to pulsatile, asymmetric, focal neurologic or other concerning presentations.', 'Treat reversible causes; hearing rehabilitation, education and evidence-based behavioral strategies often matter more than medication.', 'Pulsatile tinnitus is a vascular/anatomic localization problem until evaluated.'), ('Rhinology / Allergy / Skull Base', 'Nasal Anatomy for Endoscopy', 'Use inferior turbinate/floor, middle turbinate, uncinate, bulla, basal lamella, sphenoethmoidal recess and choana as sequential orientation landmarks.', 'Endoscopy and multiplanar CT should agree; reconstruct drainage pathways before operating.', 'Management depends on pathology; anatomy is the safety framework for office and OR procedures.', 'Never advance an instrument into a space you cannot localize relative to orbit/skull base.'), ('Rhinology / Allergy / Skull Base', 'Inferior Turbinate Hypertrophy', 'Distinguish reversible mucosal congestion from fixed soft-tissue/bony enlargement and from nasal-valve/septal obstruction.', 'Examine before/after decongestion; endoscopy when posterior disease or other pathology is possible.', 'Optimize rhinitis therapy first; reduction is for persistent symptomatic hypertrophy and should preserve mucosal function.', 'Aggressive resection can trade obstruction for dryness/crusting and dysfunctional airflow.'), ('Rhinology / Allergy / Skull Base', 'Septal Deviation', 'A crooked septum matters only if it contributes meaningfully to the symptomatic airflow bottleneck.', 'Anterior rhinoscopy/endoscopy plus valve/turbinate assessment; CT is not required for routine isolated deviation.', 'Septoplasty when symptoms persist and septal anatomy is causal; combine with other functional treatment only when indicated.', 'Preserve dorsal/caudal support and avoid bilateral opposing mucosal injury.'), ('Rhinology / Allergy / Skull Base', 'Recurrent Acute Rhinosinusitis', 'Discrete bacterial-pattern episodes with symptom-free intervals are different from chronic daily symptoms.', 'Confirm the pattern and consider endoscopy/CT when episodes are recurrent and intervention is contemplated; assess dental, immune or anatomic contributors selectively.', 'Treat individual bacterial episodes appropriately; prevention/surgery depends on documented pattern and anatomy rather than symptom count alone.', 'Do not convert every recurrent viral URI into RARS.'), ('Rhinology / Allergy / Skull Base', 'CRSsNP', 'Chronic symptoms require objective inflammation; phenotype comorbid allergy/asthma and structural contributors.', 'Endoscopy and CT establish objective disease and map anatomy when needed.', 'Saline/topical corticosteroid therapy is foundational; ESS for appropriately selected persistent disease after adequate medical strategy.', 'Surgery improves access/ventilation but chronic inflammation still needs longitudinal treatment.'), ('Rhinology / Allergy / Skull Base', 'CRSwNP', 'Bilateral polyposis is an inflammatory phenotype; ask about asthma/AERD and recurrence risk.', 'Endoscopy/CT define burden; consider type-2 inflammatory context and alternative diagnoses for unilateral disease.', 'Topical steroids/irrigation, selected systemic therapy, ESS and biologics are individualized by severity, recurrence, comorbidity and goals.', "Unilateral 'polyp' deserves a broader differential than routine bilateral CRSwNP."), ('Rhinology / Allergy / Skull Base', 'AFRS', 'Think allergic mucin, fungal sensitization and characteristic heterogeneous sinus disease in the appropriate patient rather than invasive fungal infection.', 'Endoscopy, CT and pathologic/allergic evaluation establish the pattern and exclude invasive disease.', 'Surgery clears obstructive allergic mucin and restores access; postoperative anti-inflammatory/allergy strategy is essential.', 'Fungal elements do not automatically mean tissue invasion.'), ('Rhinology / Allergy / Skull Base', 'Invasive Fungal Rhinosinusitis', 'Rapidly progressive disease in immunocompromised/metabolically vulnerable patients is an emergency; necrosis, cranial neuropathy or orbital findings are ominous.', 'Urgent endoscopy/biopsy and contrast imaging define tissue invasion/extent; do not delay treatment for perfect imaging.', 'Reverse predisposing factors when possible, systemic antifungal therapy and urgent repeated surgical debridement with multidisciplinary care.', 'Normal-appearing early mucosa does not fully exclude deep invasive disease when suspicion is high.'), ('Rhinology / Allergy / Skull Base', 'Mucocele', 'Expansile obstructed sinus mucus can remodel bone and compress orbit/skull base.', 'CT defines bony expansion; MRI helps when tumor/soft tissue distinction matters.', 'Endoscopic marsupialization/drainage is common when accessible; address the obstructed pathway.', 'Think years after prior surgery/trauma as well as primary obstruction.'), ('Rhinology / Allergy / Skull Base', 'Sinonasal Inverted Papilloma', 'Unilateral mass with characteristic attachment biology and recurrence/malignancy risk requires oncologic-style mapping.', 'Endoscopy, CT for bony attachment/remodeling and MRI when soft-tissue extent matters; biopsy appropriately.', 'Complete resection including attachment site with long-term surveillance.', 'Treat the attachment, not just the visible polypoid bulk.'), ('Rhinology / Allergy / Skull Base', 'Sinonasal Malignancy', 'Unilateral obstruction/bleeding, cranial neuropathy, facial/orbital symptoms or destructive mass requires malignancy workup.', 'Endoscopic biopsy after imaging when vascularity/skull-base relationships matter; CT + MRI often complementary.', 'Histology and extent drive endoscopic/open surgery, radiation/systemic therapy and skull-base reconstruction.', 'Do not biopsy a potentially vascular lesion blindly.'), ('Rhinology / Allergy / Skull Base', 'Endoscopic Maxillary Antrostomy', 'The goal is to identify and incorporate the natural ostium while protecting orbit and nasolacrimal structures.', 'Pre-op CT maps uncinate, natural ostium, Haller cells and orbital floor.', 'Uncinectomy and antrostomy should restore a physiologic common drainage pathway without creating recirculation.', 'Failure to identify the natural ostium can create accessory-ostium recirculation.'), ('Rhinology / Allergy / Skull Base', 'Ethmoidectomy', 'Proceed cell-by-cell using lamina papyracea laterally and skull base superiorly, with basal lamella separating anterior/posterior ethmoid.', 'CT review must identify Keros depth, dehiscence, AEA course, Onodi cells and asymmetry.', 'Extent matches disease; preserve landmarks and mucosa where possible.', 'Orbital fat or CSF means stop, identify the injury and manage deliberately.'), ('Rhinology / Allergy / Skull Base', 'Sphenoidotomy', 'Localize sphenoid ostium relative to superior turbinate/choana; respect carotid and optic nerve variability.', 'CT must be reviewed for Onodi cells, septal insertion onto carotid/optic canal and pneumatization.', 'Open the natural ostium safely and enlarge according to pathology/approach needs.', 'Never torque a sphenoid septum attached to a carotid canal.'), ('Rhinology / Allergy / Skull Base', 'Epistaxis Surgical Control', 'Refractory posterior bleeding is usually approached by targeted arterial control rather than progressively traumatic packing.', 'Endoscopy localizes; CTA/angiography is selective for unusual, recurrent, traumatic or embolization scenarios.', 'Endoscopic sphenopalatine/posterior nasal arterial control or embolization depending on context and resources.', 'Know that arterial branching can be multiple—control the vascular territory, not one assumed branch.'), ('Head & Neck Oncology', 'Oral Tongue SCC', 'Persistent ulcer/induration, pain or referred otalgia demands biopsy; depth and nodal risk matter.', 'Biopsy primary, map neck, image local extent when it changes resection; stage with current system.', 'Resection with appropriate neck management and reconstruction; adjuvant therapy follows stage/pathologic risk.', 'Plan speech/swallow reconstruction before cutting.'), ('Head & Neck Oncology', 'Floor of Mouth SCC', 'Thin mucosa and proximity to mandible/submandibular ducts/lingual nerve allow early functional spread.', 'Examine bimanually, biopsy, image mandible/deep extent and neck as indicated.', 'Primary resection + neck strategy; marginal/segmental mandible decisions depend on true bone involvement.', 'Mandible proximity is not the same as mandibular invasion.'), ('Head & Neck Oncology', 'Tonsil SCC', 'HPV-associated disease may present as a cystic neck node with subtle tonsil primary.', 'p16/HPV-aware pathology, imaging and directed primary evaluation.', 'Transoral surgery + neck management or radiation-based treatment depending on stage/anatomy/function.', 'Avoid open excision of an adult cystic neck node before metastatic OPSCC is excluded.'), ('Head & Neck Oncology', 'Base of Tongue SCC', 'Subtle BOT primaries can hide in lingual tonsil tissue and present with nodal disease.', 'Flexible exam, imaging, tissue diagnosis and operative evaluation when needed.', 'Surgical versus radiation-based strategy depends on exposure, stage and expected swallow function.', 'BOT resection risk includes lingual artery and major swallow morbidity.'), ('Head & Neck Oncology', 'Supraglottic Cancer', 'Rich lymphatics create nodal risk; symptoms may include dysphagia, otalgia or late voice change.', 'Endoscopy documents subsite/mobility; imaging defines pre-epiglottic/paraglottic spread and nodes.', 'Early selected disease can be treated surgically or with radiation; advanced treatment balances organ preservation and function.', 'Bilateral neck risk rises for midline/supraglottic drainage.'), ('Head & Neck Oncology', 'Glottic Cancer', 'Persistent dysphonia often presents early; mobility and anterior commissure/subglottic extension matter.', 'Laryngoscopy/stroboscopy, operative biopsy and selective imaging.', 'Early lesions: transoral surgery or radiation; advanced disease requires functional organ-preservation versus laryngectomy reasoning.', 'A preserved larynx that chronically aspirates may not represent functional preservation.'), ('Head & Neck Oncology', 'Hypopharyngeal Cancer', 'Often advanced at presentation with dysphagia, weight loss, otalgia and nodal disease.', 'Endoscopy/biopsy plus cross-sectional staging and nutritional/airway assessment.', 'Multimodality treatment is common; reconstruction and swallow rehabilitation are central.', 'Look for synchronous disease and profound baseline nutritional/functional compromise.'), ('Head & Neck Oncology', 'Nasopharyngeal Carcinoma', 'Neck mass, unilateral effusion, epistaxis or cranial neuropathy can be presenting signs; EBV biology matters in endemic/nonkeratinizing disease.', 'Nasopharyngoscopy/biopsy, MRI/CT and systemic staging; EBV-related testing as appropriate.', 'Radiation with systemic therapy by stage is central; surgery is mainly selected salvage/neck management.', 'Adult unilateral effusion should prompt nasopharyngeal evaluation.'), ('Head & Neck Oncology', 'Laryngeal Preservation Decision', 'Separate anatomic organ preservation from a larynx that can actually protect airway, phonate and swallow.', 'Stage tumor and baseline laryngeal function; evaluate cartilage invasion, aspiration, airway and patient factors.', 'Choose surgery versus chemoradiation based on oncologic control and predicted post-treatment function.', 'A nonfunctional pretreatment larynx is a poor organ-preservation target.'), ('Head & Neck Oncology', 'Total Laryngectomy', 'Creates permanent separation of airway and alimentary tract; understand rehabilitation before surgery.', 'Pre-op staging, pulmonary/nutritional assessment, speech rehabilitation planning and counseling about permanent stoma.', 'Resection + pharyngeal closure ± neck treatment/reconstruction; postoperative fistula and swallow management are major issues.', 'After total laryngectomy, oral/nasal oxygen does not ventilate the lungs—oxygenate the stoma.'), ('Head & Neck Oncology', 'Parapharyngeal Space Tumor', 'Prestyoid vs poststyloid localization predicts salivary versus neurovascular origin and operative risk.', 'MRI/CT ± vascular imaging; biopsy strategy depends on vascularity and access.', 'Observe or resect based on diagnosis, growth, symptoms and morbidity; approach tailored to compartment/size.', 'Do not needle a suspected paraganglioma without vascular characterization.'), ('Head & Neck Oncology', 'Carotid Body Paraganglioma', 'Pulsatile hypervascular carotid bifurcation mass; cranial nerve and vascular morbidity increase with size/encasement.', 'CTA/MRA/MRI characterize vascularity and carotid relationships; biochemical/genetic evaluation in selected paraganglioma contexts.', 'Observation, radiation or surgery individualized by age, growth, symptoms, genetics and Shamblin-type complexity.', 'Biopsy is generally unnecessary and potentially hazardous for a classic vascular paraganglioma.'), ('Thyroid / Parathyroid / Salivary', 'Medullary Thyroid Cancer', 'Think calcitonin-producing C-cell cancer with possible hereditary MEN2/RET implications.', 'Calcitonin/CEA, neck mapping and RET testing; evaluate pheochromocytoma before thyroid surgery when hereditary disease is possible.', 'Total thyroidectomy with nodal management based on disease; systemic targeted therapy for selected advanced disease.', 'Rule out pheochromocytoma before operating on MEN2-associated MTC.'), ('Thyroid / Parathyroid / Salivary', 'Anaplastic Thyroid Cancer', 'Rapidly enlarging invasive thyroid mass with airway/swallow/voice symptoms is an oncologic emergency.', 'Urgent tissue diagnosis, airway assessment, cross-sectional staging and molecular testing when it can guide targeted therapy.', 'Multidisciplinary airway, systemic targeted/immunologic, radiation and selective surgery based on resectability and goals.', 'Reflex tracheostomy can be difficult and is not automatically the best airway strategy in bulky invasive disease.'), ('Thyroid / Parathyroid / Salivary', 'Central Neck Dissection', 'Level VI/VII compartment contains pre/paratracheal nodes adjacent to RLNs and parathyroid blood supply.', 'Pre-op US/cross-sectional imaging maps therapeutic disease; prophylactic use is disease/risk specific.', 'Perform compartmental dissection when oncologically indicated while preserving nerve and viable parathyroid tissue.', 'Node picking is not equivalent to a compartment dissection.'), ('Thyroid / Parathyroid / Salivary', 'Reoperative Thyroid Surgery', 'Scar distorts normal planes and increases RLN/parathyroid risk; define the exact target before reentry.', 'High-quality imaging, pathology review and baseline voice/laryngeal function are especially important.', 'Operate only when expected benefit justifies higher morbidity; plan alternative nerve approaches and calcium risk.', 'Reoperative surgery rewards preoperative localization more than heroic intraoperative searching.'), ('Thyroid / Parathyroid / Salivary', 'Secondary / Tertiary Hyperparathyroidism', 'Chronic renal disease drives multigland hyperplasia; tertiary disease becomes autonomous.', 'Interpret calcium, phosphate, PTH, renal status and bone disease; localization is secondary to understanding multigland physiology.', 'Medical renal/mineral management first; subtotal/total-with-autotransplant surgical strategies for appropriate refractory disease.', 'Do not apply a single-adenoma focused-exploration model to diffuse renal hyperparathyroidism.'), ('Thyroid / Parathyroid / Salivary', 'Four-Gland Parathyroid Exploration', 'Systematic bilateral exploration uses embryology and reproducible anatomic relationships rather than random searching.', 'Know prior imaging but do not let it replace systematic anatomy in multigland disease.', 'Identify all expected glands, assess abnormality, choose subtotal/targeted strategy based on disease context and preserve viable tissue when appropriate.', 'Missing inferior glands may descend with thymus; superior glands may fall posteriorly/retroesophageally.'), ('Thyroid / Parathyroid / Salivary', 'Submandibular Sialolithiasis', 'Meal-related swelling/pain localizes obstruction; anterior stones may be palpable in floor of mouth.', 'Exam + ultrasound/CT depending on stone visibility/location; define size, location, ductal stenosis and gland health.', 'Hydration/sialogogues for mild disease; transoral removal, sialendoscopy/lithotripsy or gland excision based on anatomy and chronic damage.', 'Lingual nerve crosses the duct; stone location changes nerve risk.'), ('Thyroid / Parathyroid / Salivary', 'Sialendoscopy', 'Minimally invasive duct endoscopy treats selected stones/strictures and preserves gland function.', 'Imaging and palpation define whether the obstruction is endoscopically accessible.', 'Dilation, endoscopy, basket retrieval, dilation/irrigation or combined approaches; convert when anatomy demands.', 'Do not force an impacted stone and create a duct perforation.'), ('Thyroid / Parathyroid / Salivary', 'Submandibular Gland Excision', 'Used for selected tumors or refractory obstructive/inflammatory gland disease.', 'Define tumor/stone extent and neck anatomy; counsel marginal mandibular, lingual and hypoglossal nerve risks.', 'Identify/protect nerves and facial vessels; ligate duct while protecting lingual nerve.', 'Three nerve relationships should be mentally rehearsed before incision.'), ('Pediatric Otolaryngology', 'Tympanostomy Tube Indications', 'The decision combines current effusion, hearing/developmental risk and recurrent AOM phenotype—not infection count alone.', 'Otoscopy/tympanometry and age-appropriate hearing testing when persistent effusion or risk makes hearing consequential.', 'Observe many transient effusions; tubes for guideline-supported chronic OME/recurrent AOM phenotypes and at-risk children.', 'Document whether middle-ear effusion is actually present when evaluating recurrent AOM for tubes.'), ('Pediatric Otolaryngology', 'Pediatric Hearing Loss Workup', 'Separate conductive, SN and auditory-neural patterns; timing matters because language development is time-sensitive.', 'Age-appropriate behavioral/physiologic audiology, tympanometry, OAEs/ABR, then etiologic imaging/genetic/infectious evaluation by phenotype.', 'Early amplification/CI/communication support and developmental services; treat reversible conductive disease.', 'The goal is access to language, not simply a better audiogram.'), ('Pediatric Otolaryngology', 'Congenital CMV Hearing Loss', 'cCMV can cause congenital or delayed/progressive SNHL, including initially normal hearing.', 'Diagnosis timing matters for proving congenital infection; longitudinal audiologic surveillance is essential.', 'Antiviral decisions depend on neonatal systemic disease/current protocols; hearing rehabilitation follows functional loss.', 'A passed newborn screen does not eliminate later cCMV-related hearing loss.'), ('Pediatric Otolaryngology', 'Thyroglossal Duct Cyst', 'Midline mass near hyoid that moves with swallowing/tongue protrusion reflects persistent embryologic tract.', 'Ultrasound confirms cyst and normally located thyroid tissue when relevant; treat acute infection before definitive surgery.', 'Sistrunk procedure removes cyst, central hyoid and tract toward tongue base to reduce recurrence.', 'Simple cyst excision has a higher recurrence risk because the tract follows the hyoid relationship.'), ('Pediatric Otolaryngology', 'Branchial Cleft Anomalies', 'Lateral neck pits/cysts/fistulae follow reproducible embryologic pathways; first/second/third/fourth anomalies have distinct relationships.', 'Ultrasound/CT/MRI or tract studies selectively based on depth and suspected anomaly.', 'Treat infection first; definitive excision after inflammation settles when indicated.', 'Know facial nerve relationship in first-cleft anomalies and carotid/pharyngeal relationships in second-cleft tracts.'), ('Pediatric Otolaryngology', 'Lymphatic Malformation', 'Soft transilluminating/compressible multicystic lesion can enlarge with infection/hemorrhage and cross spaces.', 'MRI best maps trans-spatial extent; ultrasound helps superficial lesions.', 'Observe asymptomatic lesions; sclerotherapy, surgery or systemic targeted therapy depending on macro/microcystic biology, site and morbidity.', 'Airway involvement changes urgency and may worsen abruptly with hemorrhage/infection.'), ('Pediatric Otolaryngology', 'Laryngomalacia', 'Inspiratory stridor from dynamic supraglottic collapse is common; severity is defined by physiology, not sound.', 'Flexible laryngoscopy confirms pattern; investigate feeding, growth, hypoxemia and synchronous disease when severe/atypical.', 'Observe most; supraglottoplasty for severe disease with meaningful physiologic consequences.', 'Loud stridor with good growth may be less severe than quiet obstruction with failure to thrive.'), ('Pediatric Otolaryngology', 'Supraglottoplasty', 'Target the collapsing supraglottic structures while preserving protective tissue and avoiding bilateral scar.', 'Pre-op endoscopy defines collapse pattern and comorbid airway/neurologic/swallowing issues.', 'Divide shortened aryepiglottic folds and/or reduce redundant tissue selectively; postoperative airway/swallow monitoring by risk.', 'Overaggressive bilateral tissue injury can create supraglottic stenosis.'), ('Pediatric Otolaryngology', 'Pediatric Subglottic Stenosis', 'Congenital or acquired fixed narrowing; grade, length, cartilage quality and comorbidity determine treatment.', 'Endoscopic airway evaluation is definitive; characterize vocal-fold mobility, glottis, subglottis, trachea and dynamic lesions.', 'Observe mild stable disease; endoscopic or open reconstruction based on stenosis architecture and prior response.', 'Cotton-Myer grade is only one variable; length and framework matter.'), ('Pediatric Otolaryngology', 'Laryngotracheal Reconstruction', 'Expand a scarred airway with cartilage grafting when endoscopic therapy is insufficient and anatomy is suitable.', 'Complete airway mapping, pulmonary/swallow status and comorbidity optimization before reconstruction.', 'Single- vs double-stage and anterior/posterior graft strategy depend on glottic/subglottic anatomy and need for stenting/tracheostomy.', 'Successful reconstruction is measured by safe functional airway/decannulation, not lumen size alone.'), ('Pediatric Otolaryngology', 'Choanal Atresia', 'Neonatal bilateral obstruction causes cyclical cyanosis/respiratory distress; unilateral disease presents later with chronic unilateral symptoms.', 'Endoscopy and CT define bony/membranous anatomy after nasal decongestion/suction.', 'Secure neonatal airway first; endoscopic repair timing/technique depends on laterality and stability.', 'A newborn is preferentially nasal breathing, so bilateral atresia is an airway emergency.'), ('Pediatric Otolaryngology', 'Pediatric Deep Neck Infection', 'Retropharyngeal/parapharyngeal infection can progress rapidly and threaten airway/mediastinum.', 'If stable, contrast CT helps define phlegmon vs abscess and complications; airway status overrides imaging.', 'IV antibiotics and supportive care; drain based on airway, size/location, toxicity and failure to improve.', 'Do not sedate or transport an unstable child without an airway plan.'), ('Pediatric Otolaryngology', 'Velopharyngeal Insufficiency', 'Hypernasality/nasal emission can result from structural insufficiency, neuromotor incompetence or mislearning.', 'Perceptual speech evaluation + nasendoscopy/videofluoroscopy as needed to define closure pattern and gap.', 'Speech therapy for mislearning; surgery/prosthetic approaches for structural/physiologic gap based on pattern and airway risk.', 'Before pharyngeal surgery, think about OSA risk.'), ('Laryngology / Voice / Swallowing', 'Laryngeal Anatomy', 'Organize by cartilaginous framework, intrinsic muscles, joints, mucosal spaces and superior/recurrent laryngeal innervation.', 'Flexible exam shows function; CT/MRI/endoscopy answer deeper structural questions.', 'Anatomy predicts voice, airway and swallow deficits and guides every laryngeal procedure.', 'Cricothyroid = EBSLN; other intrinsic muscles = RLN.'), ('Laryngology / Voice / Swallowing', 'Stroboscopy Interpretation', 'Describe closure, symmetry, periodicity, amplitude, mucosal wave and vertical level rather than simply naming a lesion.', 'Strobe requires adequate periodic phonation; use high-speed/other assessment when vibration is too irregular.', 'Management follows the physiologic deficit plus lesion, not image appearance alone.', 'Reduced wave implies stiffness but does not tell you the cause by itself.'), ('Laryngology / Voice / Swallowing', 'Vocal Fold Nodules', 'Typically bilateral symmetric phonotraumatic lesions at the vibratory midpoint with hourglass closure.', 'Stroboscopy and voice evaluation define impact and exclude mimics.', 'Voice therapy/vocal-behavior change first; surgery is uncommon for classic nodules.', 'Treat the behavior that created the lesion or recurrence is predictable.'), ('Laryngology / Voice / Swallowing', 'Vocal Fold Polyp / Cyst', 'Usually focal lesion with asymmetric vibration; cysts often produce greater focal stiffness.', 'Stroboscopy differentiates superficial mass effect and mucosal-wave impairment.', 'Voice therapy may optimize behavior; persistent symptomatic lesions often need precise microlaryngeal surgery.', 'Preserve superficial lamina propria—scar can be worse than the lesion.'), ('Laryngology / Voice / Swallowing', 'Bilateral Vocal Fold Immobility', 'Stridor with near-midline folds may be neurogenic paralysis or mechanical fixation/posterior glottic stenosis.', 'History, flexible exam and operative palpation/EMG selectively distinguish nerve from joint/scar pathology.', 'Secure airway when needed; later treatment balances airway enlargement against voice/swallow.', 'Do not perform irreversible airway-widening surgery before understanding the mechanism.'), ('Laryngology / Voice / Swallowing', 'Spasmodic Dysphonia', 'Task-specific involuntary voice breaks suggest focal laryngeal dystonia; distinguish tremor and muscle tension dysphonia.', 'Diagnosis is clinical by expert perceptual/laryngoscopic assessment; no single imaging test proves it.', 'Botulinum toxin is common first-line procedural treatment; therapy helps associated compensatory behaviors.', 'Adductor and abductor phenotypes require different injection targets.'), ('Laryngology / Voice / Swallowing', 'Zenker Diverticulum', 'Regurgitation, dysphagia, halitosis and aspiration arise from a hypopharyngeal pouch associated with cricopharyngeal dysfunction.', 'Barium swallow defines pouch and anatomy; endoscopy is selective and must avoid perforation.', 'Endoscopic or open diverticular treatment includes addressing the cricopharyngeus.', 'Treating the pouch without the outflow dysfunction invites failure.'), ('Laryngology / Voice / Swallowing', 'FEES', 'Directly assesses pharyngeal secretion management, residue, penetration/aspiration before/after the white-out and response to strategies.', 'Use when bedside repeatability, secretion assessment or real-food trials are valuable; know the white-out limitation.', 'Findings guide diet, therapy and procedural targets; it is complementary to MBS.', 'State the physiologic impairment, not merely the PAS score.'), ('Laryngology / Voice / Swallowing', 'Modified Barium Swallow', 'Dynamic fluoroscopy evaluates oral/pharyngeal bolus transit and selected cervical esophageal events across consistencies.', 'Choose standardized boluses and maneuvers to test hypotheses about timing, strength and airway protection.', 'Use results to target rehabilitation/compensation and determine whether further esophageal workup is needed.', 'MBS is a functional experiment, not a static picture.'), ('Laryngology / Voice / Swallowing', 'Medialization Thyroplasty', 'Framework surgery repositions a weak fold to improve glottic closure while preserving mucosa.', 'Confirm stable unilateral glottic insufficiency and define posterior gap/vertical mismatch; counsel that motion is not restored.', 'Window/implant placement is titrated to voice and closure; arytenoid adduction may address selected posterior/vertical problems.', 'Medialization treats position/closure, not neural recovery.'), ('Laryngology / Voice / Swallowing', 'Microlaryngoscopy', 'Suspension exposure enables diagnosis and phonomicrosurgery; exposure strategy matters as much as instruments.', 'Pre-op airway/dentition/neck mobility and lesion localization predict difficulty.', 'Use atraumatic exposure, magnification and lesion-specific technique while preserving vibratory layers.', 'Poor exposure is a reason to change strategy, not to apply more destructive force.'), ('Facial Plastics / Trauma', 'Nasal Fracture', 'Assess deformity, obstruction, septal hematoma and associated facial/ocular injury rather than relying on x-ray.', 'Clinical exam is usually enough for isolated fracture; CT for broader facial trauma.', 'Observe nondisplaced injury; closed reduction when deformity/obstruction warrants and timing is appropriate.', 'Septal hematoma is the time-sensitive diagnosis.'), ('Facial Plastics / Trauma', 'NOE Fracture', 'Central midface trauma threatens medial canthal tendon, lacrimal system and nasal projection.', 'Thin-cut CT + intercanthal/ocular exam; classify tendon-bearing fragment stability.', 'Restore canthal position and central facial projection with stable fixation; manage associated frontal/orbital injuries.', 'Traumatic telecanthus implies medial canthal tendon complex injury until assessed.'), ('Facial Plastics / Trauma', 'Frontal Sinus Fracture', 'Decisions depend on anterior table, posterior table, nasofrontal outflow tract and CSF/intracranial injury.', 'CT maps displacement, outflow and posterior table; evaluate CSF leak/brain injury.', 'Observation, endoscopic/open repair, obliteration or cranialization depends on these compartments and current practice.', 'Do not choose treatment from anterior-table displacement alone.'), ('Facial Plastics / Trauma', 'Facial Nerve Reanimation', 'Choose strategy from injury level, duration, muscle viability and proximal/distal nerve availability.', 'Serial facial grading, electrodiagnostics selectively, imaging/etiologic workup and ocular assessment.', 'Primary repair/graft when possible acutely; nerve transfers or muscle transfer/static support as denervation duration increases.', 'Time is muscle: prolonged denervation changes reconstructive options.'), ('Facial Plastics / Trauma', 'Mohs Defect Reconstruction', 'Reconstruction begins after margins are clear and must respect subunits, free margins and depth.', 'Assess cartilage/bone exposure, laxity, vascularity and functional structures.', 'Secondary healing, graft, local/regional flap or staged reconstruction chosen by defect—not prestige.', 'A tiny defect at an eyelid/nasal rim can be functionally harder than a larger convex-surface defect.'), ('Facial Plastics / Trauma', 'Scar Management', 'Scar outcome reflects tension, orientation, inflammation, patient biology and time.', 'Assess hypertrophic vs keloid vs widened/depressed/contracted scar and functional distortion.', 'Sun protection, silicone/pressure, steroid/5-FU, laser, revision or flap/Z-plasty based on scar phenotype.', 'Do not revise an immature scar early unless function demands it.'), ('Sleep Surgery', 'Pediatric PSG Interpretation', 'Children require pediatric thresholds; examine obstructive events, oxygenation, CO2, sleep architecture and clinical risk.', 'Confirm study quality and total sleep time; integrate age, obesity, craniofacial/neuromuscular comorbidity.', 'Treatment depends on anatomy/severity and often starts with adenotonsillar therapy when appropriate; residual OSA needs reassessment.', 'A low-looking AHI by adult standards may still be meaningful in a child.'), ('Sleep Surgery', 'PAP Troubleshooting', 'PAP failure is not one diagnosis: pressure intolerance, mask leak, nasal obstruction, claustrophobia, aerophagia and behavioral barriers differ.', 'Review device data, mask, nasal airway and sleep symptoms before declaring intolerance.', 'Fix the limiting factor; alternatives include oral appliance, weight strategy and surgery/device therapy for selected patients.', "Document what 'failed CPAP' actually means."), ('Sleep Surgery', 'Palatal Surgery', 'Palatal procedures target retropalatal collapse but technique must match collapse pattern and preserve swallow/velopharyngeal function.', 'Awake exam + PSG ± DISE; identify tonsils, palate, lateral walls and multilevel disease.', 'Select reconstructive rather than purely ablative technique according to anatomy and overall plan.', 'Palate surgery cannot fix isolated tongue-base collapse.'), ('Sleep Surgery', 'Tongue Base Surgery', 'Targets retroglossal obstruction from lingual tonsil/tongue-base volume or collapse.', 'DISE/imaging/exam selectively define target and multilevel contribution.', 'Lingual tonsillectomy, reduction/suspension or skeletal/device approaches are selected by anatomy and phenotype.', 'Airway edema/bleeding and dysphagia are central perioperative risks.'), ('Sleep Surgery', 'Maxillomandibular Advancement', 'Skeletal advancement enlarges/stabilizes multilevel pharyngeal airway and can be highly effective in selected OSA.', 'Craniofacial analysis, dental/orthognathic planning and PSG establish candidacy.', 'Multidisciplinary orthognathic surgery with counseling about occlusion, facial change and nerve risks.', 'MMA is multilevel airway surgery, not merely a jaw operation.'), ('General ENT / Emergencies', 'Peritonsillar Abscess', 'Unilateral severe sore throat, trismus, muffled voice and peritonsillar swelling suggest abscess/cellulitis spectrum.', 'Usually clinical; imaging for atypical/deep-space concern or uncertain exam.', 'Drain when abscess is present/appropriate, antibiotics, hydration/analgesia; airway assessment always.', 'Trismus + toxic appearance should trigger thought beyond simple tonsillitis.'), ('General ENT / Emergencies', 'Ludwig Angina', 'Rapid bilateral floor-of-mouth/submandibular cellulitis can elevate tongue and threaten airway.', 'Clinical airway assessment first; CT after airway stability to define source/abscess/spread.', 'Early airway strategy, broad antibiotics and dental/source control ± drainage.', 'Do not wait for stridor—late airway signs can precede catastrophe.'), ('General ENT / Emergencies', 'Angioedema', 'Differentiate histamine-mediated from bradykinin-mediated swelling because treatment response differs.', 'Airway examination/trajectory is primary; medication/family history and associated urticaria help mechanism.', 'Secure threatened airway early; mechanism-specific medical treatment and remove triggers.', 'Flexible scope findings and progression matter more than lip size.'), ('General ENT / Emergencies', 'Caustic Ingestion', 'Airway injury and esophageal/gastric injury may coexist; oral burns do not perfectly predict depth.', 'Airway assessment, toxicology/GI collaboration and appropriately timed endoscopic evaluation based on agent/severity.', 'Supportive care and organ-specific management; avoid inducing emesis/neutralization attempts.', 'A normal mouth does not exclude significant distal injury.'), ('General ENT / Emergencies', 'Esophageal Foreign Body', 'Button battery, sharp object and complete obstruction are time-sensitive; location and object type drive urgency.', 'Radiographs for radiopaque objects; endoscopy based on symptoms/object even when imaging is limited.', 'Urgent/emergent removal for batteries/sharp objects/obstruction; otherwise timing follows risk.', 'Button battery in esophagus is an emergency because tissue injury progresses rapidly.'), ('General ENT / Emergencies', 'Airway Foreign Body', 'Sudden choking, cough, unilateral wheeze or unexplained symptoms may occur with normal imaging.', 'History + exam; inspiratory/expiratory films or CT selectively, but high suspicion can justify bronchoscopy.', 'Rigid bronchoscopy for appropriate suspected airway foreign body; unstable complete obstruction requires immediate age-appropriate rescue.', 'Do not let a normal x-ray erase a classic aspiration event.'), ('General ENT / Emergencies', 'Postoperative Neck Hematoma', 'Rapid neck swelling after thyroid/parathyroid/neck surgery can cause lethal airway compression.', 'Diagnosis is clinical; do not delay decompression for imaging in a crashing patient.', 'Call for help, open/decompress immediately when airway threatened and secure airway/OR control.', 'A small external swelling can hide major deep pressure.'), ('General ENT / Emergencies', 'Chyle Leak', 'Milky drain output or rising output with feeding after low left neck surgery suggests thoracic duct injury.', 'Clinical diagnosis; triglyceride/chylomicron testing when uncertain; quantify output and nutritional/electrolyte effects.', 'Dietary modification/pressure/drain strategy, pharmacologic adjuncts and operative/interventional repair based on output/persistence.', 'High-output leak is a systemic nutritional/immunologic problem, not just a drain nuisance.')]

# Convert each saturation topic into the same six-layer learning architecture.
SATURATION_MODULES_V7=[]
for _domain,_topic,_mental,_workup,_management,_pearl in SATURATION_TOPICS_V7:
    SATURATION_MODULES_V7.append({
      "topic":_topic,
      "domain":_domain,
      "recognize":_mental.split(".")[0] + ".",
      "localize":_mental,
      "workup":_workup,
      "manage":_management,
      "operate":("For operative/procedural cases, explicitly state indication, setup, landmarks, danger structures, key steps, "
                 "failure modes and postoperative plan. "+_pearl),
      "teach":_pearl
    })

# Merge into v6 deep modules without duplicate topic names.
for _m in SATURATION_MODULES_V7:
    _bucket=DEEP_MODULES_V6.setdefault(_m["domain"],[])
    if not any(x["topic"].lower()==_m["topic"].lower() for x in _bucket):
        _bucket.append({k:v for k,v in _m.items() if k!="domain"})

# Regenerate adaptive items so all saturated modules participate in daily learning.
ADAPTIVE_ITEMS_V7=[]
for _domain,_mods in DEEP_MODULES_V6.items():
    for _m in _mods:
        _id=_v6_item_id(_domain,_m["topic"])
        for _stage in ["recognize","localize","workup","manage","operate","teach"]:
            ADAPTIVE_ITEMS_V7.append({
              "id":_id+"-"+_stage,"concept_id":_id,"domain":_domain,"topic":_m["topic"],"stage":_stage,
              "prompt":{
                "recognize":"Recognize the pattern and identify the dangerous alternative.",
                "localize":"Localize the disease anatomically and physiologically.",
                "workup":"Choose the next test(s) that actually change management and interpret the result.",
                "manage":"Build a treatment plan, including observation/medical/procedural options and escalation.",
                "operate":"Give the operative mental model: indication, setup, anatomy, danger structures, key steps, complications and postoperative care.",
                "teach":"Teach the core mental model and the attending/boards pearl."
              }[_stage],
              "answer":_m[_stage],
              "minutes":{"recognize":3,"localize":3,"workup":4,"manage":4,"operate":6,"teach":4}[_stage],
              "level":{"recognize":1,"localize":2,"workup":3,"manage":4,"operate":5,"teach":6}[_stage]
            })

# Content-completion targets: operative prep. These are concise OR frameworks and
# intentionally do not replace institution/attending-specific technique.
OR_SATURATION_V7 = {
"tympanostomy-tubes":("Tympanostomy Tubes","Pediatric/Otology",["Confirm indication, ear laterality and current middle-ear status.","Microscope exposure and canal cleaning.","Radial myringotomy in a safe quadrant; suction effusion.","Place tube without medialization/trauma; confirm patency."],["Ossicles","Annulus","Canal trauma","Persistent perforation"]),
"tympanoplasty":("Tympanoplasty","Otology",["Review perforation, hearing and middle-ear disease; choose transcanal/endaural/postauricular access.","Freshen/define perforation and elevate tympanomeatal flap as needed.","Inspect ossicles/middle ear and eradicate disease.","Place graft with stable support and reconstruct canal/TM."],["Chorda tympani","Ossicles","Facial nerve","Graft lateralization/blunting"]),
"stapedotomy":("Stapedotomy","Otology",["Confirm conductive phenotype and counsel SNHL/taste/vertigo risk.","Transcanal exposure; elevate flap and visualize ossicular chain.","Confirm fixation; divide stapedial tendon/posterior crus strategy as technique requires.","Create fenestra and place appropriately measured prosthesis; verify mobility/seal."],["Facial nerve","Chorda","Incus","Vestibule/inner ear"]),
"cochlear-implant":("Cochlear Implantation","Otology",["Confirm candidacy, side, device and imaging.","Postauricular access, mastoidectomy/facial recess or planned alternative.","Create receiver bed/pocket and expose round window.","Atraumatic electrode insertion; secure device and confirm function/position."],["Facial nerve","Chorda","Sigmoid/tegmen","Cochlea/vestibule"]),
"neck-dissection":("Selective Neck Dissection","Head & Neck",["Map required nodal levels from primary/nodal disease.","Raise flaps and identify compartment boundaries.","Preserve uninvolved SAN/IJV/SCM and other critical nerves/vessels as oncologically appropriate.","Remove lymphatic tissue en bloc by planned levels; orient specimen."],["SAN","Carotid/vagus/IJV","Phrenic/brachial plexus","Thoracic duct"]),
"total-laryngectomy":("Total Laryngectomy","Head & Neck",["Confirm extent and permanent-stoma counseling; plan neck/reconstruction/TEP.","Raise flaps and perform indicated neck/thyroid/hyoid exposure.","Separate trachea and create permanent stoma; complete pharyngeal/laryngeal resection.","Close/reconstruct pharynx and establish speech/swallow rehabilitation plan."],["Carotids","Pharyngeal closure/fistula","Stomal recurrence","Hypocalcemia if thyroid/parathyroids affected"]),
"submandibular-gland":("Submandibular Gland Excision","Salivary",["Confirm indication and lesion/stone anatomy.","Incise below mandible; protect marginal mandibular nerve.","Control facial vessels, mobilize gland and identify lingual/hypoglossal relationships.","Ligate duct safely and remove gland/lesion."],["Marginal mandibular","Lingual nerve","Hypoglossal nerve","Facial vessels"]),
"sialendoscopy":("Sialendoscopy","Salivary",["Localize obstruction and select gland/duct.","Dilate papilla and enter duct atraumatically.","Endoscopically map stenosis/stone; irrigate/dilate/retrieve or combine approach.","Confirm duct patency and manage papilla/duct trauma."],["Duct perforation","Lingual nerve in submandibular combined approach","Basket impaction"]),
"DLB":("Direct Laryngoscopy / Bronchoscopy","Pediatric Airway",["Define diagnostic question and shared anesthetic/ventilation plan.","Systematic laryngeal exposure and palpation where appropriate.","Inspect glottis/subglottis/trachea/bronchi; size airway when indicated.","Document complete airway map and perform planned intervention."],["Dental/lip injury","Laryngospasm","Airway edema","Loss of airway"]),
"airway-dilation":("Endoscopic Airway Dilation","Laryngology/Airway",["Define stenosis level/length/grade and etiology.","Suspension exposure and circumferential assessment.","Incision/adjunct strategy when indicated, then controlled balloon dilation.","Reassess lumen, mucosal injury and airway stability."],["Posterior wall injury","Airway fire with laser","Edema","Restenosis"]),
"medialization":("Medialization Thyroplasty","Laryngology",["Confirm stable glottic insufficiency and side.","Expose thyroid ala and design window.","Create pocket while preserving inner perichondrium when technique requires.","Insert/titrate implant to voice/closure; secure and close."],["Airway","Implant extrusion/migration","Over/undermedialization","Hematoma"]),
"zenker":("Endoscopic Zenker Treatment","Laryngology",["Confirm pouch anatomy and candidacy for endoscopic exposure.","Expose common wall between esophagus and pouch.","Divide septum/cricopharyngeal muscle with chosen technique.","Inspect for bleeding/perforation and follow postoperative swallow protocol."],["Mediastinitis/perforation","Bleeding","Dental injury","Recurrence"]),
"tonsillectomy":("Tonsillectomy","Pediatrics/General",["Confirm indication and bleeding/OSA risk.","Expose tonsil and identify capsule/plane.","Dissect while preserving pharyngeal muscle and controlling vessels.","Final hemostasis and postoperative pain/hydration/bleeding counseling."],["Postoperative hemorrhage","Glossopharyngeal injury","Airway/OSA risk","Dehydration"]),
"adenoidectomy":("Adenoidectomy","Pediatrics",["Confirm indication and assess palate/VPI risk.","Expose nasopharynx and identify choanae/Eustachian cushions.","Remove obstructive adenoid tissue while protecting surrounding structures.","Hemostasis and reassessment of nasal airway."],["Velopharyngeal insufficiency","Eustachian tube injury","Bleeding"]),
"thyroglossal":("Sistrunk Procedure","Pediatrics",["Confirm diagnosis and normally located thyroid tissue when relevant.","Expose cyst/tract and central hyoid.","Remove central hyoid with tract directed toward tongue base.","Avoid rupture, achieve hemostasis and close."],["Hypoglossal nerve","Airway/tongue-base entry","Recurrence from incomplete tract"]),
"branchial":("Branchial Cleft Anomaly Excision","Pediatrics",["Define anomaly type and tract relationships; operate after acute infection resolves.","Expose cyst/tract through appropriate neck incision(s).","Follow tract with attention to carotids/cranial nerves/pharynx or facial nerve depending on cleft type.","Remove complete anomaly without rupture where feasible."],["Facial nerve in first-cleft","Carotids","Hypoglossal/glossopharyngeal nerves","Recurrence"]),
"orbital-floor":("Orbital Floor Repair","Facial Trauma",["Confirm functional indication and complete ocular exam.","Transconjunctival/subciliary access per plan; expose orbital rim/floor.","Free entrapped tissue and define defect.","Place stable implant restoring orbital support; confirm free motility."],["Globe","Infraorbital nerve","Inferior rectus","Retrobulbar hematoma"]),
"mandible-orif":("Mandible ORIF","Facial Trauma",["Map fractures and establish preinjury occlusion.","Secure maxillomandibular relationship when appropriate.","Expose fracture, reduce anatomically/occlusally and apply fixation.","Verify occlusion and nerve/tooth safety."],["Inferior alveolar nerve","Tooth roots","Facial nerve by approach","Malocclusion"]),
"zmc-orif":("ZMC ORIF","Facial Trauma",["Assess globe/vision and 3-D displacement.","Expose required buttresses/orbital rim.","Reduce zygoma restoring projection and orbital volume.","Fixate stable points and reassess globe/motility."],["Globe","Infraorbital nerve","Facial nerve","Malposition"]),
"hypoglossal-stimulator":("Hypoglossal Nerve Stimulator Implantation","Sleep",["Confirm candidacy and DISE/PSG requirements.","Expose hypoglossal nerve and identify inclusion/exclusion branches.","Place stimulation cuff and respiratory sensor; create generator pocket.","Connect/test system and plan later activation/programming."],["Hypoglossal nerve injury","Marginal mandibular","Pleura/pneumothorax","Lead migration/infection"]),
}
for _slug,(_title,_domain,_steps,_danger) in OR_SATURATION_V7.items():
    if _slug not in OR_PREP_REGISTRY:
        OR_PREP_REGISTRY[_slug]={
          "slug":_slug,"title":_title,"domain":_domain,
          "indications":"Use for appropriately selected disease after diagnosis, alternatives and patient-specific risk have been reviewed.",
          "steps":_steps,"danger":_danger,
          "attending_followup":[
            ["What should you know before incision?","The exact indication, disease extent, relevant imaging/testing, alternatives, anatomy and rescue plan."],
            ["What makes this operation unsafe?","Losing orientation to the named danger structures or proceeding without a defined functional/oncologic endpoint."],
            ["How do you judge success?","By disease-specific control plus preservation/restoration of the relevant airway, hearing, voice, swallowing, sleep or oncologic function."]
          ],"linked_topic":_slug,"status":"audited-v7"
        }


# =============================================================================
# ENT Mastery v8 — Final Content Completion Pass
# =============================================================================
FINAL_COMPLETION_TOPICS_V8 = [('Otology / Neurotology', 'Hearing Aids and Bone-Conduction Devices', 'Match rehabilitation to conductive, sensorineural or mixed deficit, ear anatomy and speech needs; conventional air-conduction aids require usable ear-canal/middle-ear conditions.', 'Use complete audiometry and aided performance; distinguish conventional aid, CROS/BiCROS, bone-conduction and implantable options.', 'Counsel on realistic speech/hearing goals and choose technology from anatomy plus functional deficit.', 'A device is selected by the hearing problem and usable pathway, not the audiogram label alone.'), ('Otology / Neurotology', 'Vestibular Test Battery', 'VNG/calorics, vHIT and VEMP interrogate different frequencies/end organs; discordance can be physiologically meaningful.', 'Interpret spontaneous/gaze/positional eye movements first, then caloric asymmetry, vHIT gain/saccades and cervical/ocular VEMP in clinical context.', 'Use tests to refine localization and compensation, not to replace the bedside syndrome.', "No single vestibular test is a universal 'inner-ear test'."), ('Otology / Neurotology', 'Ototoxic / Noise-Induced Hearing Loss', 'Exposure history plus characteristic SNHL pattern matters; tinnitus may precede perceived disability.', 'Serial audiometry and medication/exposure review; monitor high-risk therapy using an established ototoxicity protocol.', 'Reduce avoidable exposure, coordinate medication alternatives when possible, and rehabilitate persistent loss.', 'Prevention and serial change are more useful than waiting for profound threshold loss.'), ('Otology / Neurotology', 'Autoimmune Inner Ear Disease', 'Rapidly progressive or fluctuating often bilateral SNHL raises an immune-mediated hypothesis but has no single diagnostic biomarker.', 'Serial audiometry and targeted systemic evaluation when history suggests autoimmune disease; exclude more common mimics.', 'Specialist-directed corticosteroid/immunologic treatment may be considered while preserving hearing rehabilitation options.', 'Treat it as a clinical syndrome of exclusion, not a positive blood-test diagnosis.'), ('Otology / Neurotology', 'CSF Otorrhea / Temporal Encephalocele', 'Clear middle-ear fluid, recurrent meningitis or persistent unilateral effusion can reflect tegmen defect/encephalocele.', 'High-resolution temporal-bone CT plus MRI for soft tissue/encephalocele; assess spontaneous-leak risk factors and intracranial-pressure physiology.', 'Repair symptomatic/persistent leaks using transmastoid, middle-fossa or combined strategy based on site/size/anatomy.', "A 'middle-ear effusion' that is actually CSF changes every subsequent step."), ('Otology / Neurotology', 'Necrotizing Otitis Externa', 'Severe persistent otalgia, granulation and high-risk host features suggest skull-base osteomyelitis rather than simple OE.', 'Culture when useful, inflammatory markers and targeted CT/MRI/nuclear imaging according to the diagnostic question; evaluate cranial nerves.', 'Prolonged antipseudomonal therapy with metabolic optimization and specialist follow-up; surgery is generally for biopsy/source issues rather than routine wide debridement.', 'Cranial neuropathy is a late and serious extension sign.'), ('Otology / Neurotology', 'Petrous Apex Lesions', 'Localize expansile petrous-apex disease by CT density/bone behavior and MRI signal; cholesterol granuloma, cholesteatoma and neoplasm behave differently.', 'Use complementary CT and MRI including diffusion when appropriate; compare serial imaging when observation is plausible.', 'Observe stable incidental lesions or drain/resect according to diagnosis, symptoms, growth and access corridor.', 'The safest route is chosen from lesion biology and available aerated/anatomic corridors.'), ('Rhinology / Allergy / Skull Base', 'Acute Bacterial Rhinosinusitis', 'Differentiate bacterial-pattern persistent/severe/double-worsening illness from viral URI; imaging is not routine in uncomplicated disease.', 'Clinical diagnosis for uncomplicated cases; image when complication, alternative diagnosis or operative planning is relevant.', 'Observation or guideline-concordant antibiotic strategy depending on severity/context, plus symptom care; escalate orbital/intracranial complications urgently.', 'Purulent-colored drainage alone does not prove bacterial sinusitis.'), ('Rhinology / Allergy / Skull Base', 'Odontogenic Sinusitis', 'Unilateral maxillary-predominant disease with dental pathology or dental procedure history should trigger a dental source hypothesis.', 'Endoscopy + CT including maxillary dentition; coordinate dental evaluation.', 'Treat the dental source and sinus disease; ESS when drainage/disease burden warrants.', 'Sinus surgery without source control can predictably fail.'), ('Rhinology / Allergy / Skull Base', 'Fungal Ball', 'Noninvasive dense fungal debris usually occupies one sinus in immunocompetent patients and differs from AFRS/invasive disease.', 'CT often shows heterogeneous/hyperdense material; endoscopy and pathology establish noninvasive fungal debris.', 'Surgical clearance and ventilation; systemic antifungals are not routine for a simple fungal ball.', 'Fungus present does not equal invasive fungal sinusitis.'), ('Rhinology / Allergy / Skull Base', 'Orbital Complications of Sinusitis', 'Preseptal cellulitis, orbital cellulitis, subperiosteal abscess and orbital abscess represent escalating postseptal risk; vision exam is critical.', 'Contrast CT/MRI depending on severity and intracranial concern; serial visual acuity, pupils, motility and color vision.', 'IV antibiotics and urgent ENT/ophthalmology coordination; drain when vision, abscess characteristics, clinical course or complications demand it.', 'A worsening afferent pupillary defect or vision change is an emergency.'), ('Rhinology / Allergy / Skull Base', 'Intracranial Complications of Sinusitis', 'Severe headache, neurologic change, meningismus, frontal swelling or persistent toxicity can signal epidural/subdural abscess, meningitis or venous thrombosis.', 'Urgent contrast MRI/CT with neurosurgical/infectious-disease coordination.', 'Broad IV therapy plus surgical source control of sinus and intracranial disease as indicated.', 'Neurologic deterioration overrides routine sinusitis pathways.'), ('Rhinology / Allergy / Skull Base', 'Revision FESS', 'Failure may reflect residual cells, scarring, recirculation, neo-osteogenesis, persistent inflammatory phenotype or wrong original diagnosis.', 'Re-read CT from scratch and compare prior operative anatomy; endoscopy identifies stenosis/scar/persistent disease.', "Correct the specific mechanical/inflammatory failure and re-establish topical access; do not simply 'make everything bigger'.", 'Revision surgery requires more—not less—preoperative anatomy work.'), ('Rhinology / Allergy / Skull Base', 'Frontal Sinusotomy / Draf Procedures', 'Escalate from opening frontal recess to extended unilateral/bilateral drainage only when disease/anatomy requires it.', 'Multiplanar CT must define frontal drainage pathway, AEA, orbit, skull base, frontal beak and intersinus anatomy.', 'Draf IIa/IIb/III concepts progressively enlarge frontal outflow; postoperative stenosis prevention and topical access matter.', 'Extended frontal surgery is anatomy-driven, not a badge of surgical aggressiveness.'), ('Rhinology / Allergy / Skull Base', 'Endoscopic CSF Leak Repair / Nasoseptal Flap', 'Repair requires localization, defect preparation and reconstruction matched to defect size/flow and intracranial-pressure context.', 'High-resolution CT/MRI ± CSF confirmation; identify vascular pedicle and prior septal surgery before planning a flap.', 'Multilayer closure with free graft or vascularized flap when indicated; address elevated ICP physiology in spontaneous leaks.', 'Protect the posterior septal vascular pedicle before you need the flap.'), ('Rhinology / Allergy / Skull Base', 'Juvenile Nasopharyngeal Angiofibroma', 'Adolescent male with recurrent epistaxis/nasal obstruction and a hypervascular nasopharyngeal mass has a classic high-risk phenotype.', 'CT/MRI and vascular imaging define extension/supply; avoid routine office biopsy of a classic vascular lesion.', 'Preoperative embolization and endoscopic/open resection strategies depend on stage/extension; selected observation/radiation in special contexts.', 'Diagnose radiographically before putting an instrument into it.'), ('Rhinology / Allergy / Skull Base', 'Olfactory Dysfunction', 'Separate conductive loss from sensorineural/postviral/traumatic/neurodegenerative causes; qualitative distortions matter.', 'History, nasal endoscopy and validated smell testing; imaging only for selected unilateral, neurologic or structural concerns.', 'Treat reversible obstruction/inflammation and use olfactory training for appropriate persistent sensorineural loss.', "Subjective 'I can't smell' should be phenotyped and measured."), ('Head & Neck Oncology', 'Adverse Pathology and Adjuvant Therapy', 'Margin status, extranodal extension, nodal burden, PNI/LVI, T stage and site-specific risk alter postoperative therapy.', 'Read the final pathology as a treatment map, not a diagnosis summary; reconcile margins with operative orientation.', 'Discuss radiation versus chemoradiation according to established high-risk features and patient tolerance.', 'The cancer operation is not finished intellectually when the specimen leaves the room.'), ('Head & Neck Oncology', 'Head & Neck Radiation Toxicity / Survivorship', 'Xerostomia, dysphagia, fibrosis, dental injury, hypothyroidism, carotid disease and osteoradionecrosis evolve over years.', 'Longitudinal swallowing, dental, nutrition, thyroid, hearing and recurrence surveillance according to treatment/site.', 'Prevent and rehabilitate toxicity early; coordinate dental care, swallowing therapy and site-specific surveillance.', 'Survivorship is part of cancer treatment, not an afterthought.'), ('Head & Neck Oncology', 'TEP and Alaryngeal Speech', 'After laryngectomy, communication options include electrolarynx, esophageal speech and tracheoesophageal voice.', 'Assess cognition/dexterity, stoma, pharyngoesophageal segment and pulmonary support with SLP.', 'Primary/secondary TEP selection and prosthesis care are longitudinal rehabilitation decisions.', 'A technically successful laryngectomy without communication rehabilitation is incomplete care.'), ('Head & Neck Oncology', 'Neck Lymphoma', 'Persistent lymphadenopathy with systemic symptoms or atypical nodal pattern may require lymphoma-specific tissue handling.', 'Imaging and tissue diagnosis with architecture/flow cytometry planning; FNA alone may be insufficient for classification.', 'Hematologic therapy dominates; surgery is diagnostic or for selected complications rather than routine nodal clearance.', 'Plan the biopsy with pathology before destroying the architecture needed for diagnosis.'), ('Head & Neck Oncology', 'Merkel Cell / High-Risk Cutaneous Cancer', 'Aggressive cutaneous malignancies differ in nodal biology and adjuvant needs; immunosuppression and head/neck drainage increase complexity.', 'Risk-directed imaging, nodal staging and pathology including depth/PNI/grade features.', 'Coordinate dermatologic surgery, nodal management, radiation and systemic therapy by tumor type/stage.', 'Do not apply the same nodal algorithm to melanoma, SCC and Merkel cell carcinoma.'), ('Thyroid / Parathyroid / Salivary', 'Graves Disease / Toxic Goiter', 'Hyperfunction changes preoperative physiology and extent decisions; large goiter adds airway/vascular/anatomic complexity.', 'TSH/free hormones, etiology, ultrasound when structurally relevant and medical optimization; assess compressive symptoms/voice.', 'Antithyroid/radioiodine/surgery selection depends on disease, pregnancy, nodules, goiter, patient goals and contraindications.', 'An uncontrolled thyrotoxic patient is not ready for elective thyroidectomy.'), ('Thyroid / Parathyroid / Salivary', 'Indeterminate Thyroid Cytology / Molecular Testing', 'Bethesda indeterminate categories represent probability, not a cancer diagnosis; molecular tests modify risk in context.', 'Integrate ultrasound phenotype, cytology category, nodule size, clinical risk and test characteristics.', 'Surveillance, diagnostic lobectomy or definitive surgery depends on combined risk and how the result changes management.', 'Never order a molecular test without knowing what decision each possible result will change.'), ('Thyroid / Parathyroid / Salivary', 'MEN2 / RET', 'Hereditary RET disease links medullary thyroid cancer, pheochromocytoma and hyperparathyroidism with genotype-dependent timing.', 'RET testing and biochemical screening; rule out pheochromocytoma before thyroid intervention.', 'Coordinate prophylactic/therapeutic thyroid surgery and family screening with endocrinology/genetics.', 'Pheochromocytoma comes before thyroid surgery.'), ('Thyroid / Parathyroid / Salivary', 'Parathyroid Carcinoma', 'Very high calcium/PTH, firm invasive gland or recurrent disease raises concern; capsule violation can seed recurrence.', 'Biochemical confirmation and localization/staging imaging; avoid FNA of suspected parathyroid carcinoma.', 'En-bloc initial resection when suspected and feasible; recurrent/metastatic disease requires multidisciplinary calcium and tumor control.', 'The first operation is the best chance for complete oncologic resection.'), ('Thyroid / Parathyroid / Salivary', 'Reoperative Hyperparathyroidism', 'Persistent/recurrent disease demands proof of biochemical disease and precise localization before scarred reentry.', 'Reconfirm diagnosis, review prior op/pathology and use complementary localization such as US/nuclear/4D-CT or advanced studies by context.', 'Reoperate when benefit justifies increased RLN/hypoparathyroid risk; plan ectopic/supernumerary possibilities.', 'Do not re-explore a scarred neck because one scan is vaguely positive.'), ('Thyroid / Parathyroid / Salivary', 'Hungry Bone / Post-Thyroid Calcium Management', 'Postoperative hypocalcemia may reflect transient/permanent hypoparathyroidism or hungry-bone remineralization; timing and phosphate/magnesium context help.', 'Trend calcium/PTH and relevant electrolytes based on procedure/risk and symptoms.', 'Calcium ± active vitamin D and magnesium replacement according to physiology/severity with safe follow-up.', 'Perioral tingling after neck endocrine surgery deserves a calcium plan, not reassurance alone.'), ('Thyroid / Parathyroid / Salivary', 'Pleomorphic Adenoma / Warthin Tumor', 'Benign salivary tumors have different recurrence/multifocality/malignant-transformation considerations and must be separated from malignant mimics.', 'Ultrasound/CT/MRI and FNA/core strategy based on site and risk.', 'Observation for selected lesions/patients versus extracapsular/parotid surgery according to diagnosis/location and institutional practice.', 'Enucleating pleomorphic adenoma risks capsular violation and recurrence.'), ('Thyroid / Parathyroid / Salivary', 'Acute Sialadenitis / Sjögren', 'Painful meal-related or infected swelling differs from chronic autoimmune xerostomia; dehydration/obstruction predispose bacterial infection.', 'Exam duct output/stone, ultrasound/CT selectively; autoimmune evaluation when systemic sicca pattern warrants.', 'Hydration, massage/sialogogues, antibiotics for bacterial infection, obstruction treatment; Sjögren needs systemic/dental dry-mouth care.', 'Treat obstruction if it is the reason infections keep returning.'), ('Thyroid / Parathyroid / Salivary', 'Ranula', 'Mucus extravasation from sublingual gland may remain oral or plunge through/around mylohyoid into neck.', 'Exam + ultrasound/CT/MRI for plunging extent.', 'Definitive strategies target the sublingual source; simple aspiration has high recurrence.', 'The cervical component is not the gland producing the mucus.'), ('Pediatric Otolaryngology', 'Recurrent Tonsillitis Decision-Making', 'Count episodes only after verifying qualifying severity/documentation; modifying factors and shared decision-making matter.', 'History/records and exam; PSG is not a recurrent-infection test.', 'Watchful waiting versus tonsillectomy according to guideline-supported burden/modifiers.', "'Seven sore throats' is not equivalent to seven qualifying tonsillitis episodes."), ('Pediatric Otolaryngology', 'Pediatric Tracheostomy / Decannulation', 'Tracheostomy dependence reflects airway, pulmonary, neurologic and secretion/swallowing physiology; decannulation is a pathway.', 'Airway endoscopy, capping/sleep/oxygenation assessment and multidisciplinary readiness criteria according to local pathway.', 'Downsize/cap and decannulate only after the original indication and current airway/respiratory needs are resolved.', 'A normal-looking stoma says nothing about decannulation readiness.'), ('Pediatric Otolaryngology', 'Pediatric Vocal Fold Immobility', 'Unilateral disease causes voice/swallow issues; bilateral immobility can be a neonatal airway emergency.', 'Flexible laryngoscopy and etiologic evaluation along vagal/RLN pathway; distinguish paralysis from fixation.', 'Observation for recovery, feeding support/injection in selected unilateral cases; airway procedures for severe bilateral disease while balancing voice.', 'Before irreversible airway widening, establish mechanism and recovery potential.'), ('Pediatric Otolaryngology', 'Recurrent Respiratory Papillomatosis', 'HPV-related papillomas cause recurrent dysphonia and potentially airway disease; disease burden varies widely.', 'Serial laryngoscopy and operative mapping; biopsy/pathology when diagnosis or transformation concern warrants.', 'Repeated tissue-preserving debulking plus selected adjuvant therapy; maintain airway and voice while minimizing scar.', 'Eradication at one operation is usually not a realistic goal.'), ('Pediatric Otolaryngology', 'Subglottic Hemangioma', 'Progressive biphasic stridor in infancy with vascular lesion phenotype can mimic croup.', 'Flexible/direct airway evaluation and imaging when extent/diagnosis requires it.', 'Systemic beta-blocker therapy is foundational for appropriate infantile hemangioma; airway intervention for severe/refractory disease.', "Repeated 'croup' outside the expected pattern should trigger airway evaluation."), ('Pediatric Otolaryngology', 'Tracheomalacia / Bronchomalacia', 'Dynamic expiratory airway collapse causes noisy breathing, cough, recurrent infection or life-threatening spells depending on severity.', 'Dynamic bronchoscopy is key; CT and pulmonary/cardiac evaluation help define compression/comorbidity.', 'Observe/support mild disease; treat reflux/secretions selectively; positive pressure or aortopexy/tracheopexy for severe physiology.', 'Static airway images can underestimate a dynamic disorder.'), ('Pediatric Otolaryngology', 'Microtia / Aural Atresia', 'External-ear deformity may coexist with canal/middle-ear anomalies and conductive hearing loss; bilateral loss threatens language access.', 'Early audiology, renal/genetic evaluation when syndromic features warrant, and later CT for surgical candidacy/timing.', 'Provide hearing access early; coordinate auricular reconstruction/prosthesis and atresiaplasty or bone-conduction options.', 'Hearing rehabilitation starts long before cosmetic ear reconstruction.'), ('Pediatric Otolaryngology', 'Pediatric Aspiration', 'Aspiration may arise from neurologic discoordination, structural cleft, vocal-fold immobility, airway lesions or reflux-associated factors.', 'Clinical feeding evaluation + FEES/MBS selected to the question; airway endoscopy when structural lesion suspected.', 'Target feeding strategy and the demonstrated mechanism; repair structural lesions and protect pulmonary health.', "Do not label aspiration 'reflux' without defining the swallowing physiology."), ('Laryngology / Voice / Swallowing', 'Reinke Edema', 'Diffuse superficial lamina propria edema produces low-pitched dysphonia and may narrow airway; smoking is a major driver.', 'Stroboscopy defines pliability/extent and excludes suspicious epithelial lesions.', 'Smoking cessation/irritant control and voice care; microlaryngeal reduction for significant voice/airway burden.', 'Preserve vibratory cover—over-resection creates scar.'), ('Laryngology / Voice / Swallowing', 'Presbyphonia', 'Age-related vocal-fold atrophy causes bowing, glottic insufficiency and weak voice but must be distinguished from paresis/systemic disease.', 'Stroboscopy + perceptual/functional voice assessment.', 'Voice therapy first for many; injection or framework augmentation when glottic insufficiency remains limiting.', "Treat the functional complaint, not the patient's age."), ('Laryngology / Voice / Swallowing', 'Muscle Tension Dysphonia', 'Excess supraglottic/phonatory tension may be primary or compensatory to an underlying glottic lesion.', 'Stroboscopy and expert voice evaluation; actively search for the reason the patient is compensating.', 'Voice therapy is central; treat an underlying lesion/paresis when present.', 'Supraglottic squeeze is a behavior/finding, not automatically the primary diagnosis.'), ('Laryngology / Voice / Swallowing', 'Vocal Tremor', 'Rhythmic oscillation may involve palate/pharynx/larynx and differs from task-specific dystonia.', 'Perceptual/laryngoscopic examination across tasks; neurologic evaluation when broader tremor suspected.', 'Voice therapy/support, medication and selected botulinum toxin based on tremor distribution.', 'Look beyond the true vocal folds for tremor.'), ('Laryngology / Voice / Swallowing', 'Leukoplakia / Laryngeal Dysplasia', 'White plaque is a visual descriptor spanning benign keratosis through invasive cancer; vascular/mucosal features alter concern.', 'Stroboscopy and biopsy/excision when risk warrants; pathology grade drives surveillance/treatment.', 'Risk-factor modification and lesion-specific surveillance/excision/ablation while preserving voice.', "Never equate 'leukoplakia' with one histologic diagnosis."), ('Laryngology / Voice / Swallowing', 'Posterior Glottic Stenosis / Arytenoid Fixation', 'Bilateral reduced motion after intubation may be scar/joint fixation rather than RLN paralysis.', 'History, flexible exam and operative palpation ± EMG distinguish fixation from denervation.', 'Scar release, dilation, cordotomy/arytenoid procedures or open reconstruction selected by severity while balancing voice/swallow.', 'Mechanism determines the operation.'), ('Laryngology / Voice / Swallowing', 'Injection Laryngoplasty', 'Temporary or durable injectable augmentation improves glottic closure without restoring nerve movement.', 'Define side, gap, recovery prognosis and material duration; choose office versus OR route.', 'Inject lateral to the vocal ligament into appropriate paraglottic target and titrate closure; monitor airway/voice/swallow.', 'Overinjection and superficial injection are avoidable technical failures.'), ('Laryngology / Voice / Swallowing', 'Arytenoid Adduction / Reinnervation', 'Posterior gap and vertical-level mismatch may need arytenoid repositioning; reinnervation restores tone over time rather than immediate motion.', 'Use laryngoscopy/strobe and prognosis to choose augmentation/framework/reinnervation combinations.', 'Select procedure by age, denervation duration, gap geometry and patient goals.', 'Framework, injection and reinnervation solve different physiologic problems.'), ('Laryngology / Voice / Swallowing', 'Posterior Cordotomy / Arytenoidectomy', 'Airway-widening procedures trade glottic resistance for voice and sometimes swallow function in bilateral immobility.', 'Confirm stable bilateral neurogenic immobility versus fixation and recovery potential.', 'Endoscopic posterior glottic enlargement is titrated to airway need; revisions may be required.', 'Every extra millimeter of airway has a voice/aspiration consequence.'), ('Laryngology / Voice / Swallowing', 'Cricopharyngeal Dysfunction', 'Impaired UES opening may reflect poor relaxation, fibrosis or inadequate hyolaryngeal traction rather than one disease.', 'MBS/esophagram ± manometry/endoscopy according to phenotype.', 'Swallow therapy, dilation, botulinum toxin or myotomy selected by demonstrated mechanism and durability needs.', 'A prominent CP bar on imaging is not automatically the cause of dysphagia.'), ('Facial Plastics / Trauma', 'Functional Septorhinoplasty', 'Correct septal, valve and external-framework contributors while maintaining structural support and nasal aesthetics.', 'Dynamic airway exam, septum/turbinates/valves and photographs; define static vs dynamic collapse.', 'Septoplasty plus spreader/batten/lateral-wall or tip-support maneuvers selected from the mechanical deficit.', 'Use grafts to solve a defined force/vector problem, not because a named graft is fashionable.'), ('Facial Plastics / Trauma', 'Open Rhinoplasty Fundamentals', 'Open approach provides broad framework exposure for complex tip/dorsal/valve work at the cost of more dissection.', 'Preoperative functional/aesthetic analysis and standardized photography; plan septal cartilage needs.', 'Expose framework atraumatically, preserve support, perform planned dorsal/tip/valve modifications and close with symmetry checks.', 'Over-resection is harder to fix than under-correction.'), ('Facial Plastics / Trauma', 'Otoplasty', 'Prominent ear often reflects antihelical underfolding, conchal excess or both.', 'Analyze deformity component and asymmetry before selecting sutures/cartilage techniques.', 'Mustardé/Furnas-type concepts and cartilage modification are tailored to the deformity while avoiding overcorrection.', 'Treat the anatomic cause of prominence, not every ear with the same suture pattern.'), ('Facial Plastics / Trauma', 'Forehead Flap / Nasal Reconstruction', 'Large/deep nasal defects need restoration of lining, structural support and skin cover in layers.', 'Analyze nasal subunit, cartilage/bone loss, lining and vascular pedicle; stage reconstruction deliberately.', 'Paramedian forehead flap provides robust cover; combine cartilage and lining reconstruction when required.', 'A beautiful skin flap collapses if the missing framework was never rebuilt.'), ('Facial Plastics / Trauma', 'Le Fort / Panfacial Trauma', 'Reconstruction requires restoring facial width, height, projection and occlusion in a deliberate sequence.', 'CT + ocular/neurologic/dental assessment; identify stable reference points.', 'Establish occlusion and stable facial buttresses using top-down/bottom-up strategy according to injury pattern.', 'Panfacial repair is three-dimensional framework reconstruction, not independent fracture fixation.'), ('Sleep Surgery', 'Oral Appliance Therapy', 'Mandibular advancement can treat selected OSA by stabilizing/enlarging retrolingual airway and is not simply a snoring device.', 'PSG diagnosis plus dental/TMJ suitability and sleep-dentistry assessment.', 'Custom titratable device with follow-up sleep testing and dental/TMJ surveillance.', 'Effectiveness must be objectively reassessed after titration.'), ('Sleep Surgery', 'HNS Activation / Programming', 'Implantation is only the beginning; stimulation amplitude/electrode configuration/timing are titrated for comfort and airway response.', 'Post-healing activation followed by symptom/device data and sleep-study-guided optimization.', 'Gradual home advancement and formal titration/programming; troubleshoot discomfort, tongue motion and residual events.', 'Do not judge HNS success from the incision or first activation.'), ('Sleep Surgery', 'Residual OSA After Surgery', 'Persistent disease may reflect incomplete anatomic treatment, weight change, multilevel collapse or physiologic factors.', 'Repeat PSG when appropriate and reassess anatomy with exam ± DISE; review adherence to adjunctive therapies.', 'Combine PAP, weight, oral appliance, revision/multilevel surgery or HNS according to new phenotype.', 'A prior operation changes anatomy but does not eliminate the need to re-phenotype.'), ('Sleep Surgery', 'Central Events / Hypoventilation', 'Central apnea and sleep-related hypoventilation are physiologically different from obstructive collapse and may make upper-airway surgery irrelevant.', 'Read central apnea index, CO2 and oxygen pattern plus medications, cardiac/neurologic/pulmonary context.', 'Treat underlying physiology with sleep/pulmonary/cardiology expertise; do not default to obstructive surgery.', 'AHI is a sum—know what kinds of events created it.'), ('General ENT / Emergencies', 'Deep Neck Abscess Drainage', 'Drainage is anatomy-specific source control; airway and carotid relationships matter more than abscess volume alone.', 'Contrast CT when stable; map involved spaces, odontogenic/tonsillar source and vascular complications.', 'Transoral or transcervical drainage according to space/access, with cultures and antibiotics.', 'Choose the route that reaches the infected compartment without traversing avoidable neurovascular danger.')]
FINAL_INTEGRATED_CASES_V8 = [('CI candidate with poor aided speech', 'Adult with progressive bilateral SNHL despite well-fit hearing aids.', 'Localize hearing deficit and assess functional aided benefit.', 'Best-aided speech testing shows limited benefit; CT/MRI show implantable cochlea/nerve.', 'Counsel CI vs continued amplification and select ear.', 'Post-op: activation/programming and auditory rehabilitation; explain why surgery alone does not produce immediate normal hearing.'), ('Temporal bone trauma triad', 'Patient after high-energy trauma has facial weakness, hearing loss and clear otorrhea.', 'Stabilize trauma patient, document facial timing/completeness, hearing and leak.', 'CT shows otic-capsule-violating fracture.', 'Coordinate CSF/facial/hearing management based on trajectory.', 'Complication: meningitis symptoms force urgent reassessment.'), ('Revision cholesteatoma', 'Prior CWU surgery patient develops recurrent conductive loss/retraction.', 'Otoscopy + audiogram; decide residual/recurrent disease likelihood.', 'DWI MRI/CT show hidden epitympanic/mastoid disease.', 'Choose revision approach based on extent and surveillance reliability.', "Attending asks why a 'more aggressive' cavity is not automatically superior."), ('Frontal revision with orbital complication', 'Prior ESS patient with frontal obstruction undergoes revision planning.', 'Reconstruct frontal pathway/AEA/orbit/skull base on CT.', 'During surgery orbital fat is exposed.', 'Stop manipulation, assess eye/orbit and control the situation deliberately.', 'Post-op visual change triggers emergency orbital evaluation.'), ('Invasive fungal rhinosinusitis', 'Immunocompromised patient with facial pain, numbness and dark mucosa.', 'Recognize emergency and obtain urgent biopsy/imaging while reversing risk factors.', 'Pathology shows tissue invasion.', 'Start systemic antifungal + serial debridement.', 'New ophthalmoplegia changes extent/prognosis discussion.'), ('HPV unknown primary', 'Adult with cystic level II node, no obvious mucosal lesion.', 'Needle diagnosis + p16/HPV-directed workup and imaging.', 'No primary on office exam.', 'Plan operative primary search/TORS-directed evaluation and neck strategy.', 'Final pathology adverse features force adjuvant-treatment decision.'), ('Larynx preservation failure', 'Advanced laryngeal cancer treated nonsurgically now has aspiration, chondronecrosis and airway dysfunction.', 'Differentiate recurrence from treatment toxicity and assess functional larynx.', 'Biopsy/imaging exclude or identify recurrence.', 'Discuss salvage laryngectomy for oncologic or functional indication.', 'Build rehabilitation plan including TEP and swallowing.'), ('Invasive thyroid cancer with RLN', 'Thyroid cancer encases one RLN; pre-op voice is normal.', 'Document baseline mobility and map disease.', 'Intraoperatively determine whether nerve can be shaved versus requires oncologic sacrifice.', 'Plan immediate nerve reconstruction/reinnervation when appropriate.', 'Counsel that an anatomically preserved nerve may still be functionally injured.'), ('Reoperative hyperparathyroidism', 'Prior exploration; persistent hypercalcemia/PTH and nonlocalizing initial imaging.', 'Reconfirm biochemical diagnosis and review prior pathology/op note.', 'Complementary localization identifies ectopic mediastinal/retroesophageal target.', 'Plan focused reoperative strategy and RLN risk.', 'Post-op calcium falls dramatically: distinguish hungry bone from permanent hypoparathyroidism.'), ('Parotid malignancy with facial weakness', 'Firm parotid mass and progressive marginal branch weakness.', 'Image + tissue diagnosis and stage neck.', 'High-grade malignancy involves facial nerve.', 'Plan parotidectomy, nerve sacrifice only where oncologically necessary, immediate reconstruction and neck/adjuvant strategy.', 'Explain why pre-op nerve dysfunction changes counseling.'), ('Pediatric trach decannulation', 'Child with prior severe airway disease is clinically improved.', 'Define original indication and current airway/pulmonary/swallow status.', 'DLB shows adequate reconstructed airway; capping/sleep assessment is reassuring.', 'Proceed through local decannulation pathway.', 'Failure during sleep prompts localization rather than automatic recannulation as the only long-term answer.'), ('RRP longitudinal management', 'Child with recurrent hoarseness and papillomas requiring repeated procedures.', 'Prioritize airway, voice and tissue diagnosis.', 'Map disease without circumferential destructive treatment.', 'Debulk selectively and consider adjuvant strategy based on burden.', 'New rapid growth/atypia triggers pathology/transformation workup.'), ('Panfacial trauma sequencing', 'Polytrauma with mandible, ZMC, NOE and frontal injuries.', 'Vision/brain/airway first; define occlusion and stable facial reference points.', 'CT demonstrates loss of facial width/projection.', 'Plan staged ORIF sequence restoring occlusion and buttresses.', 'Post-op malocclusion requires identifying which foundational reduction failed.'), ('Post-tonsil bleed rescue', 'Child presents with active delayed hemorrhage and tachycardia.', 'Airway/resuscitation/IV access/type and screen while mobilizing OR.', 'Bleeding temporarily stops with clot visible.', 'Do not downgrade risk; proceed according to significant bleed pathway.', 'During induction brisk bleeding recurs—describe shared anesthesia/surgical rescue.'), ('Deep neck infection airway', 'Adult with odontogenic infection, floor-of-mouth elevation and parapharyngeal spread.', 'Airway trajectory first; image only if stable.', 'CT shows multiloculated deep-space abscess.', 'Secure airway and perform source control with antibiotics.', 'Persistent fever leads to search for undrained space, mediastinal spread or septic thrombophlebitis.'), ('Bilateral vocal-fold immobility', 'Postoperative patient with stridor and both folds near midline.', 'Differentiate RLN paralysis from posterior glottic fixation.', 'EMG/operative palpation support stable bilateral paralysis.', 'Discuss trach vs posterior cordotomy/arytenoid procedure based on recovery and airway needs.', 'Patient prioritizes decannulation: explicitly counsel voice/swallow tradeoff.'), ('Zenker with recurrence', 'Older adult with regurgitation/aspiration after prior endoscopic treatment.', 'Barium study defines residual pouch/CP dysfunction.', 'Assess exposure and prior scar.', 'Choose revision endoscopic versus open approach based on anatomy.', 'Post-op neck pain/fever triggers perforation/mediastinitis evaluation.'), ('Residual OSA after UPPP', 'Adult remains sleepy with elevated AHI after palate surgery.', 'Re-read PSG and phenotype residual obstruction.', 'DISE shows tongue-base collapse without major residual palate collapse.', 'Choose PAP/oral appliance/HNS/tongue-base strategy according to candidacy.', 'Explain why repeating palate surgery is poorly targeted.'), ('Nasal obstruction after septoplasty', 'Patient remains obstructed despite a straight septum.', 'Dynamic exam shows lateral-wall/internal-valve collapse and turbinate contribution.', 'Decongestion/support maneuvers localize components.', 'Plan functional septorhinoplasty/valve strategy rather than repeat septoplasty.', 'Counsel how grafts alter airflow mechanics.'), ('Orbital sinusitis complication', 'Child with sinusitis develops proptosis, pain with EOM and reduced color vision.', 'Urgent visual exam and contrast imaging.', 'Subperiosteal abscess with worsening optic function.', 'IV antibiotics + urgent drainage/sinus source control.', 'Post-op vision worsens: rule out orbital compartment syndrome/residual abscess immediately.')]

FINAL_MODULES_V8=[]
for _domain,_topic,_mental,_workup,_management,_pearl in FINAL_COMPLETION_TOPICS_V8:
    FINAL_MODULES_V8.append({
      "topic":_topic,"domain":_domain,
      "recognize":_mental.split(".")[0]+".",
      "localize":_mental,
      "workup":_workup,
      "manage":_management,
      "operate":"State whether a procedure is indicated; if so, rehearse setup, landmarks, danger structures, key steps, failure/rescue and postoperative plan. "+_pearl,
      "teach":_pearl
    })
for _m in FINAL_MODULES_V8:
    _bucket=DEEP_MODULES_V6.setdefault(_m["domain"],[])
    if not any(x["topic"].lower()==_m["topic"].lower() for x in _bucket):
        _bucket.append({k:v for k,v in _m.items() if k!="domain"})

# Add high-complexity integrated cases in the schema used by the site.
for _i,(_title,_stem,_s1,_s2,_s3,_s4) in enumerate(FINAL_INTEGRATED_CASES_V8,1):
    INTEGRATED_CASES.append({
      "id":"v8-case-%03d"%_i,
      "title":_title,
      "domain":"Integrated ENT",
      "level":"Senior/Chief",
      "stem":_stem,
      "steps":[
        {"prompt":"First decision","answer":_s1},
        {"prompt":"New data","answer":_s2},
        {"prompt":"Management","answer":_s3},
        {"prompt":"Complication / attending follow-up","answer":_s4}
      ],
      "takeaway":_s4
    })

# Regenerate the adaptive bank after v8 merge.
ADAPTIVE_ITEMS_V8=[]
for _domain,_mods in DEEP_MODULES_V6.items():
    for _m in _mods:
        _id=_v6_item_id(_domain,_m["topic"])
        for _stage in ["recognize","localize","workup","manage","operate","teach"]:
            ADAPTIVE_ITEMS_V8.append({
              "id":_id+"-"+_stage,"concept_id":_id,"domain":_domain,"topic":_m["topic"],"stage":_stage,
              "prompt":{
               "recognize":"Recognize the pattern and dangerous alternative.",
               "localize":"Localize anatomically and physiologically.",
               "workup":"Choose and interpret the workup that changes management.",
               "manage":"Build treatment, escalation and follow-up.",
               "operate":"Give indication, setup, landmarks, danger structures, steps, complications/rescue and postop plan.",
               "teach":"Teach the mental model and board/attending pearl."
              }[_stage],
              "answer":_m[_stage],
              "minutes":{"recognize":3,"localize":3,"workup":4,"manage":4,"operate":6,"teach":4}[_stage],
              "level":{"recognize":1,"localize":2,"workup":3,"manage":4,"operate":5,"teach":6}[_stage]
            })

# Additional OR Tomorrow cases identified by the v7 audit.
OR_FINAL_V8 = {
"ossiculoplasty":("Ossiculoplasty","Otology",["Confirm safe middle ear and define conductive deficit.","Expose ossicular chain and assess malleus/stapes mobility.","Remove diseased/nonfunctional segments and size reconstruction.","Place PORP/TORP or autologous reconstruction with stable TM/cartilage support."],["Facial nerve","Stapes footplate","Chorda","Prosthesis displacement/extrusion"]),
"canalplasty":("Canalplasty / Exostosis","Otology",["Map stenosis/exostoses, TM and hearing.","Transcanal/postauricular exposure according to extent.","Remove bone while protecting canal skin/TM and maintaining orientation.","Redrape skin and stent/pack to prevent restenosis."],["TM","Facial nerve","TMJ","Canal skin loss"]),
"tegmen-repair":("Tegmen CSF Leak / Encephalocele Repair","Otology",["Localize defect and decide transmastoid vs middle-fossa/combined access.","Expose defect while protecting dura/ossicles/brain.","Reduce encephalocele when present and create multilayer closure.","Confirm durable separation and manage ICP context."],["Temporal lobe/dura","Ossicles","Facial nerve","Recurrent CSF leak"]),
"vestibular-schwannoma":("Vestibular Schwannoma Approach Planning","Neurotology",["Review tumor size/IAC extension, hearing and goals.","Choose retrosigmoid, translabyrinthine or middle-fossa concept based on tumor/hearing/anatomy.","Identify facial/cochlear nerve preservation priorities and vascular/brainstem relationships.","Plan postoperative facial, hearing, CSF and balance care."],["Facial nerve","Cochlear nerve","Brainstem/cerebellum","CSF leak"]),
"maxillary-antrostomy":("Endoscopic Maxillary Antrostomy","Rhinology",["Review uncinate/natural ostium/orbit on CT.","Identify uncinate and perform safe uncinectomy.","Find the natural maxillary ostium and enlarge as indicated.","Confirm common drainage pathway without recirculation."],["Orbit","Nasolacrimal duct","Accessory ostium recirculation"]),
"sphenoidotomy":("Endoscopic Sphenoidotomy","Rhinology",["Review Onodi cells, carotid/optic canals and septal insertions.","Identify superior turbinate/sphenoethmoidal recess and natural ostium.","Open and enlarge ostium according to disease.","Maintain orientation to skull base/carotid/optic nerve."],["ICA","Optic nerve","Skull base/CSF"]),
"draf":("Frontal Sinusotomy / Draf II-III","Rhinology",["Reconstruct frontal pathway from CT and define intended extent.","Identify orbit/skull base/AEA/frontal beak.","Remove obstructing cells/bone to planned IIa/IIb/III corridor.","Create durable mucosa-preserving opening and postoperative topical-access plan."],["AEA","Orbit","Skull base","Restenosis"]),
"csf-nasoseptal":("Endoscopic CSF Leak Repair / Nasoseptal Flap","Skull Base",["Localize defect and plan graft/flap before septal work.","Expose and prepare defect margins.","Place multilayer reconstruction and vascularized flap when indicated.","Support repair and manage postoperative leak/ICP precautions."],["ICA by site","Optic apparatus","Olfaction","Flap pedicle"]),
"spa-ligation":("Endoscopic Sphenopalatine Artery Ligation","Rhinology",["Confirm refractory posterior epistaxis indication.","Elevate lateral nasal wall mucosa and identify crista ethmoidalis/foramen.","Identify all SPA branches and clip/cauterize appropriately.","Reinspect for additional bleeding source."],["Orbital contents anteriorly","Multiple SPA branches","Palatal ischemic symptoms"]),
"orbital-abscess":("Endoscopic Orbital / Subperiosteal Abscess Drainage","Rhinology",["Document vision and image abscess relationship to sinuses.","Open source sinus and identify lamina safely.","Drain medial collection with ophthalmology coordination as needed.","Reassess orbital pressure/vision and ensure sinus drainage."],["Optic nerve","Medial rectus","Orbital hematoma","Vision loss"]),
"tors":("TORS Tonsil / Base-of-Tongue Resection","Head & Neck",["Confirm primary/indication, exposure and neck strategy.","Obtain robotic exposure and identify resection planes.","Resect tumor with margin orientation while protecting deep neurovascular structures.","Hemostasis, specimen orientation and postoperative airway/swallow plan."],["Lingual artery","Hypoglossal/glossopharyngeal structures","Hemorrhage","Dysphagia"]),
"oral-composite":("Oral Cavity Composite Resection","Head & Neck",["Map tumor, mandible involvement, neck and reconstruction.","Perform neck/access and define oncologic margins.","Resect primary ± marginal/segmental mandible according to true invasion.","Reconstruct speech/swallow contour and plan adjuvant care."],["Lingual/hypoglossal nerves","Mandible","Carotid/neck vessels","Fistula"]),
"tep":("Tracheoesophageal Puncture","Head & Neck / Laryngology",["Assess laryngectomy anatomy and rehabilitation candidacy.","Select primary vs secondary puncture and prosthesis plan.","Create controlled tract between trachea and esophagus under visualization.","Place prosthesis and initiate SLP-guided voicing/care."],["False passage","Leak/aspiration around prosthesis","Stenosis"]),
"central-neck":("Central Neck Dissection","Endocrine",["Map therapeutic level VI/VII disease.","Expose recurrent nerves and parathyroid vascular anatomy.","Remove pre/paratracheal compartmental nodal tissue.","Preserve viable parathyroids/nerve and orient specimen."],["RLN","Parathyroids","Trachea/esophagus"]),
"reop-thyroid":("Reoperative Thyroid / Central Neck Surgery","Endocrine",["Define exact target and baseline vocal-fold function.","Choose scar-entry strategy and identify nerve in a safer plane.","Perform targeted oncologic resection without unnecessary scar dissection.","Plan calcium/voice surveillance."],["RLN","Parathyroids","Major vessels","Trachea/esophagus"]),
"four-gland":("Four-Gland Parathyroid Exploration","Endocrine",["Confirm multigland physiology/indication.","Systematically identify expected superior/inferior glands using embryology.","Assess all glands and perform planned subtotal/other strategy.","Confirm viable remnant and biochemical response as used locally."],["RLN","Thymic/mediastinal ectopia","Permanent hypoparathyroidism"]),
"reop-parathyroid":("Reoperative Parathyroidectomy","Endocrine",["Reconfirm disease and obtain concordant localization when possible.","Review prior operative anatomy and voice.","Target localized gland using scar-avoidant nerve strategy.","Confirm biochemical response and plan calcium monitoring."],["RLN","Esophagus/trachea","Permanent hypoparathyroidism"]),
"parotid-total":("Total Parotidectomy / Facial Nerve Reconstruction","Salivary",["Map tumor, nerve function, deep-lobe/neck disease.","Identify facial nerve trunk/branches or alternative retrograde strategy.","Resect superficial/deep disease preserving uninvolved nerve when oncologically safe.","If nerve sacrifice required, reconstruct immediately when feasible and plan eye/facial rehabilitation."],["Facial nerve","External carotid branches","Great auricular","Frey syndrome"]),
"peds-ltr":("Pediatric Laryngotracheal Reconstruction","Pediatric Airway",["Map complete airway and decide single/double-stage strategy.","Expose laryngotracheal framework and harvest cartilage graft.","Split/expand anterior ± posterior framework and inset graft(s).","Stent/trach strategy and postoperative airway surveillance/decannulation plan."],["RLNs","Esophagus posteriorly","Graft prolapse","Restenosis"]),
"ctr":("Cricotracheal Resection","Airway",["Define high-grade subglottic stenosis length and glottic involvement.","Expose cricoid/trachea and preserve recurrent nerves.","Resect diseased segment with appropriate posterior mucosal/cricoid strategy.","Perform tension-controlled anastomosis and postoperative airway plan."],["RLN","Esophagus","Anastomotic dehiscence","Restenosis"]),
"tracheal-resection":("Tracheal Resection / Anastomosis","Airway",["Define lesion length and resectability.","Mobilize trachea while preserving segmental blood supply.","Resect disease and perform tension-free end-to-end anastomosis.","Neck-position/tension and airway surveillance postoperatively."],["Recurrent nerves","Blood supply","Anastomotic separation","Innominate artery"]),
"injection-laryngoplasty":("Injection Laryngoplasty","Laryngology",["Confirm side/gap and expected recovery.","Choose material and office/OR route.","Place needle into appropriate lateral/paraglottic target.","Titrate medialization and reassess voice/airway."],["Airway compromise","Superficial injection","Overmedialization"]),
"arytenoid-adduction":("Arytenoid Adduction","Laryngology",["Confirm posterior gap/vertical mismatch indication.","Expose posterior thyroid framework and muscular process region.","Place traction suture to simulate lateral cricoarytenoid vector.","Titrate with medialization strategy and secure."],["Airway","Implant/suture malposition","Overrotation"]),
"cordotomy":("Posterior Cordotomy / Arytenoidectomy","Laryngology",["Confirm stable bilateral immobility/fixation mechanism.","Suspend larynx and identify posterior membranous fold/arytenoid.","Create controlled posterior airway enlargement.","Balance decannulation goal against voice/swallow and manage granulation/restenosis."],["Aspiration","Voice loss","Scar/granulation","Airway fire if laser"]),
"cp-myotomy":("Cricopharyngeal Myotomy","Swallowing",["Demonstrate CP outflow dysfunction and select open/endoscopic route.","Expose CP bar/muscle safely.","Divide dysfunctional muscle without violating deeper esophageal wall.","Postoperative leak/swallow assessment."],["Esophageal perforation","Mediastinitis","RLN in open approach"]),
"laryngeal-botox":("Laryngeal Botulinum Toxin Injection","Laryngology",["Confirm dystonia/tremor phenotype and target muscle.","Localize TA/LCA or PCA depending on disorder.","Inject titrated dose using EMG/endoscopic technique.","Track breathiness/dysphagia/benefit duration for next dose."],["Airway with bilateral abductor weakness","Dysphagia","Dose asymmetry"]),
"septorhino":("Functional Septorhinoplasty / Nasal Valve Repair","Facial Plastics",["Define septal, internal/external valve and turbinate contributors.","Open/endonasal exposure according to planned structural work.","Preserve/rebuild L-strut and place spreader/batten/support grafts as mechanically indicated.","Reassess symmetry, valve stability and airway before closure."],["Septal perforation","Dorsal/caudal destabilization","Valve over/undercorrection"]),
"otoplasty":("Otoplasty","Facial Plastics",["Analyze antihelix/concha/lobule contribution.","Posterior/anterior exposure according to technique.","Create antihelical fold and/or reduce/set back concha with sutures/cartilage modification.","Compare symmetry and avoid excessive setback."],["Hematoma","Chondritis","Suture extrusion","Telephone-ear deformity"]),
"forehead-flap":("Paramedian Forehead Flap","Facial Plastics",["Analyze nasal lining/support/cover and subunit replacement.","Design flap on supratrochlear pedicle.","Transfer cover after reconstructing lining/framework as needed.","Stage thinning/inset and pedicle division."],["Pedicle injury","Distal necrosis","Contour trapdoor","Missing structural support"]),
"deep-neck-drain":("Deep Neck Abscess Drainage","General ENT",["Secure/plan airway and map infected space on imaging.","Choose transoral vs transcervical route from anatomy.","Enter abscess safely, culture, break loculations and drain source.","Reassess for residual spaces/mediastinal spread if not improving."],["Carotid sheath","Cranial nerves","Airway edema","Mediastinitis"]),
}
for _slug,(_title,_domain,_steps,_danger) in OR_FINAL_V8.items():
    if _slug not in OR_PREP_REGISTRY:
        OR_PREP_REGISTRY[_slug]={
          "slug":_slug,"title":_title,"domain":_domain,
          "indications":"Use when disease-specific indications are met after alternatives, anatomy and patient goals are reviewed.",
          "steps":_steps,"danger":_danger,
          "attending_followup":[
           ["What is the operative endpoint?","Achieve the disease-specific objective while preserving the relevant hearing, airway, voice, swallowing, oncologic or reconstructive function."],
           ["What should make you stop?","Loss of anatomic orientation, unexpected danger-structure exposure, uncontrolled bleeding or a change that invalidates the planned risk-benefit balance."],
           ["What complication must you anticipate before incision?","The named danger structures plus the procedure-specific functional failure and rescue pathway."]
          ],
          "linked_topic":_slug,"status":"audited-v8"
        }


# =============================================================================
# ENT Mastery v9 — Interpretation Atlas Expansion
# =============================================================================
INTERPRETATION_LABS_V9_NEW = {'thyroid-ultrasound': {'title': 'Thyroid & Neck Ultrasound Lab', 'icon': '🦋', 'subtitle': 'Describe the nodule/node first → risk-stratify → decide whether the image changes surgery.', 'framework': ['Thyroid vs extrathyroidal', 'Composition', 'Echogenicity', 'Shape', 'Margins', 'Echogenic foci', 'Extrathyroidal extension', 'Cervical nodes', 'Risk category', 'FNA / surveillance / surgical consequence'], 'source_note': 'Use the linked ACR TI-RADS material on the ACR site. ENT Mastery does not reproduce the ACR atlas images.', 'resources': [{'name': 'ACR TI-RADS', 'url': 'https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Reporting-and-Data-Systems/TI-RADS', 'note': 'Official lexicon, atlas, worksheets and case-based education'}, {'name': 'ACR TI-RADS Worksheet', 'url': 'https://cs.acr.org/-/media/ACR/Files/RADS/TI-RADS/Sonographers-Worksheet-TI-RADS.pdf', 'note': 'Composition, echogenicity, shape, margins and echogenic foci'}], 'cases': [{'id': 'us1', 'level': 1, 'external': 'https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Reporting-and-Data-Systems/TI-RADS', 'prompt': 'Open the ACR TI-RADS atlas. Before assigning points, name the five sonographic feature categories you must score.', 'answer': 'Composition, echogenicity, shape, margins, and echogenic foci.', 'why': 'A reproducible lexicon prevents jumping from a visual impression directly to biopsy.', 'follow': 'Which features are descriptors versus management decisions?'}, {'id': 'us2', 'level': 2, 'external': 'https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Reporting-and-Data-Systems/TI-RADS', 'prompt': 'A nodule is purely cystic or almost completely cystic. What is the first risk-stratification move?', 'answer': 'Recognize the benign-leaning composition before allowing dramatic but irrelevant visual details to dominate the assessment.', 'why': 'Composition is the first structured feature in TI-RADS and strongly changes the subsequent risk score.', 'follow': 'Why should a cystic nodule not be managed from size alone?'}, {'id': 'us3', 'level': 2, 'external': 'https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Reporting-and-Data-Systems/TI-RADS', 'prompt': 'Compare isoechoic, hypoechoic and very hypoechoic nodules in the ACR atlas. What tissue should you use as the reference?', 'answer': 'Compare the nodule with normal thyroid parenchyma; very hypoechoic lesions approach or fall below the echogenicity of adjacent strap muscle.', 'why': 'Echogenicity is relative, so an explicit reference tissue improves consistency.', 'follow': 'How can thyroiditis complicate this comparison?'}, {'id': 'us4', 'level': 3, 'external': 'https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Reporting-and-Data-Systems/TI-RADS', 'prompt': 'A solid nodule is taller-than-wide on transverse imaging. Why does that matter?', 'answer': 'Taller-than-wide growth is a suspicious shape feature because it suggests growth across rather than along normal tissue planes.', 'why': 'Shape contributes independent malignancy-risk information.', 'follow': 'On which imaging plane should you judge taller-than-wide?'}, {'id': 'us5', 'level': 3, 'external': 'https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Reporting-and-Data-Systems/TI-RADS', 'prompt': 'Distinguish smooth, ill-defined, lobulated/irregular, and extrathyroidal-extension margins before reading the category.', 'answer': 'The key is whether the interface is merely hard to see versus truly irregular/lobulated or extending beyond the thyroid capsule into adjacent structures.', 'why': 'Ill-defined is not synonymous with infiltrative.', 'follow': 'Which adjacent structures make suspected extrathyroidal extension surgically important?'}, {'id': 'us6', 'level': 3, 'external': 'https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Reporting-and-Data-Systems/TI-RADS', 'prompt': 'Compare comet-tail artifact, macrocalcification, rim calcification and punctate echogenic foci.', 'answer': 'These echogenic foci carry different risk implications; punctate echogenic foci are more suspicious than benign comet-tail artifact.', 'why': "Calling every bright focus a 'calcification' loses useful risk information.", 'follow': 'How can rim calcification affect FNA targeting?'}, {'id': 'us7', 'level': 4, 'external': 'https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Reporting-and-Data-Systems/TI-RADS', 'prompt': 'A nodule has suspicious features but is very small. What two variables must be kept separate before recommending FNA?', 'answer': 'Risk category and size threshold. Sonographic suspicion determines the category; size determines whether that category crosses a biopsy or follow-up threshold.', 'why': 'High suspicion does not automatically mean immediate biopsy at every size.', 'follow': 'What patient-specific factors can still modify the conversation?'}, {'id': 'us8', 'level': 4, 'prompt': 'A lateral neck node is rounded, cystic, has punctate echogenic foci and lacks a normal fatty hilum in a patient with papillary thyroid carcinoma. What is the interpretation?', 'answer': 'This is a suspicious metastatic cervical node phenotype and should be mapped by level and confirmed when confirmation will change management.', 'why': 'Nodal morphology—not size alone—drives concern in differentiated thyroid cancer.', 'follow': 'What adjunct can be added to needle sampling in selected thyroid-cancer nodes?'}, {'id': 'us9', 'level': 4, 'prompt': 'A node is oval with a preserved echogenic hilum and hilar vascularity. How should you describe it?', 'answer': 'Those are reassuring/reactive features, though interpretation still depends on the clinical context and the rest of the neck.', 'why': 'A systematic node description prevents overcalling every enlarged node.', 'follow': 'Which morphology changes would make it suspicious?'}, {'id': 'us10', 'level': 5, 'prompt': "Pre-op ultrasound shows a posterior thyroid lesion abutting the tracheoesophageal groove and a suspicious central node. What does the surgeon need from the study beyond 'thyroid cancer present'?", 'answer': 'Side, size, relationship to capsule/trachea/esophagus, possible extrathyroidal extension, central and lateral nodal map, and any finding that changes nerve/airway or compartment-dissection planning.', 'why': 'For the surgeon, ultrasound is an operative map as well as a malignancy-risk test.', 'follow': 'When would cross-sectional imaging add value?'}, {'id': 'us11', 'level': 4, 'prompt': "A hypoechoic structure posterior to the thyroid is suspected to be parathyroid. Why can't grayscale appearance alone prove it?", 'answer': 'Lymph nodes, thyroid nodules and other structures can mimic parathyroid tissue; biochemical disease and localization context are essential.', 'why': 'Parathyroid disease is diagnosed biochemically; imaging localizes it.', 'follow': 'What complementary localization tests might be used when surgery is planned?'}, {'id': 'us12', 'level': 5, 'prompt': 'After thyroidectomy, ultrasound shows a small indeterminate thyroid-bed focus. What is the disciplined next step?', 'answer': 'Integrate morphology, interval change, thyroglobulin/clinical context and nodal findings before assuming recurrent cancer; sample when the result will change management.', 'why': 'Postoperative anatomy creates benign mimics and surveillance should be risk-directed.', 'follow': 'What imaging feature or trend would raise concern?'}]}, 'temporal-bone-imaging': {'title': 'Temporal Bone CT / MRI Lab', 'icon': '🦴', 'subtitle': 'Trace the ear in compartments and convert the scan into a surgical danger map.', 'framework': ['EAC/TM', 'Ossicles', 'Epitympanum', 'Mastoid', 'Facial nerve canal', 'Labyrinth', 'IAC', 'Tegmen', 'Sigmoid/jugular bulb', 'Carotid canal', 'Disease extent', 'Operative consequence'], 'source_note': 'Cases use interpretation prompts and link to open/educational anatomy or radiology resources rather than copying images.', 'resources': [{'name': 'Open Anatomy — Inner Ear / Head & Neck Atlases', 'url': 'https://www.openanatomy.org/atlas-pages/', 'note': 'Open cross-sectional anatomy'}, {'name': 'Iowa Head & Neck Protocols — Radiology', 'url': 'https://iowaprotocols.medicine.uiowa.edu/', 'note': 'Open educational radiology pages and clinical correlations'}], 'cases': [{'id': 'tb1', 'level': 1, 'external': 'https://www.openanatomy.org/atlas-pages/', 'prompt': 'On axial temporal-bone CT, trace EAC → TM region → ossicles → epitympanum → mastoid before looking for disease.', 'answer': 'Use a fixed compartment sequence so subtle disease is not missed and surgical orientation becomes automatic.', 'why': 'Temporal-bone CT is easiest when read as connected compartments.', 'follow': 'Which structures form your medial danger boundary?'}, {'id': 'tb2', 'level': 2, 'external': 'https://www.openanatomy.org/atlas-pages/', 'prompt': 'Identify malleus head and incus body in the epitympanum. What classic axial configuration do they create?', 'answer': "The malleus head and incus body form the familiar 'ice-cream cone' configuration on axial CT.", 'why': 'Ossicular landmarks help detect erosion or discontinuity.', 'follow': 'What chronic ear disease commonly erodes the incus?'}, {'id': 'tb3', 'level': 3, 'prompt': 'CT shows epitympanic soft tissue with scutal and ossicular erosion. What diagnosis rises and what can CT not prove?', 'answer': 'Cholesteatoma rises on the differential; CT maps bone erosion and extent but soft tissue itself is not specific.', 'why': 'CT is a surgical bony roadmap; diffusion MRI can add tissue characterization in selected cases.', 'follow': 'Which hidden recesses matter for residual disease?'}, {'id': 'tb4', 'level': 3, 'prompt': 'After trauma, the ossicular chain has an abnormal incudostapedial relationship with a large conductive gap. Localize the problem.', 'answer': 'Ossicular discontinuity is likely, with the incudostapedial joint a common site of traumatic disruption.', 'why': 'The imaging finding must fit the conductive mechanics.', 'follow': 'What would make you suspect concomitant inner-ear injury?'}, {'id': 'tb5', 'level': 4, 'prompt': 'High-resolution CT suggests superior semicircular canal dehiscence. What prevents you from diagnosing the syndrome from the scan alone?', 'answer': 'Radiographic thinning/dehiscence requires matching symptoms and physiologic testing; imaging alone can overcall clinically irrelevant defects.', 'why': 'Third-window syndrome is a clinicophysiologic diagnosis supported by CT.', 'follow': 'Which symptoms and vestibular test patterns would support it?'}, {'id': 'tb6', 'level': 4, 'prompt': 'A temporal-bone fracture violates the otic capsule. What complications should move up your list immediately?', 'answer': 'Sensorineural hearing loss, facial nerve injury and CSF leak are especially important complications.', 'why': 'Otic-capsule involvement predicts clinically meaningful injury better than the old longitudinal/transverse labels.', 'follow': 'What must be documented about facial weakness timing?'}, {'id': 'tb7', 'level': 4, 'prompt': 'CT shows a tegmen defect and MRI shows herniating tissue into the epitympanum. Interpret the pair.', 'answer': 'The complementary studies support a temporal encephalocele/CSF-leak pathway: CT defines bone; MRI confirms soft-tissue/meningeal contents.', 'why': 'Using the modality for the structure it depicts best improves operative planning.', 'follow': 'What factors influence transmastoid versus middle-fossa/combined repair?'}, {'id': 'tb8', 'level': 4, 'prompt': 'A retrocochlear MRI shows an enhancing IAC/CPA mass centered on CN VIII. What diagnosis is most typical and what pre-op function matters?', 'answer': 'Vestibular schwannoma is typical; hearing level/speech performance and facial nerve status are major planning variables.', 'why': 'Approach selection is tied to tumor anatomy and hearing goals.', 'follow': 'How do retrosigmoid, translabyrinthine and middle-fossa goals differ conceptually?'}, {'id': 'tb9', 'level': 5, 'prompt': 'Pre-CI CT shows abnormal cochlear partition and an atypical facial nerve course. Why is this more than a radiology curiosity?', 'answer': 'Inner-ear malformation changes electrode access, CSF-gusher risk and expected nerve anatomy; the facial nerve may obstruct a routine facial-recess path.', 'why': 'CI imaging is a procedural hazard map.', 'follow': 'What must MRI establish in severe congenital hearing loss?'}, {'id': 'tb10', 'level': 4, 'prompt': 'A jugular bulb is high and dehiscent beneath the middle ear. What procedure-specific danger does that create?', 'answer': 'Unexpected venous injury can occur during middle-ear or hypotympanic work if the bulb is not recognized.', 'why': 'Normal vascular variants become operative hazards when their bony covering is absent.', 'follow': 'What other vascular variant should be checked near the cochlea/Eustachian tube?'}, {'id': 'tb11', 'level': 5, 'prompt': 'A petrous-apex lesion is expansile with characteristic high T1 signal and smooth bony remodeling. What is your reasoning framework?', 'answer': 'Use CT bone behavior plus MRI signal to separate cholesterol granuloma, cholesteatoma, inflammatory disease and neoplasm before choosing observation, drainage or resection.', 'why': 'Petrous-apex lesions are route-selection problems as much as diagnosis problems.', 'follow': 'Why does aeration of surrounding cells matter?'}, {'id': 'tb12', 'level': 5, 'prompt': 'Postoperative MRI after cholesteatoma surgery shows focal diffusion restriction in a hidden recess. Why is that valuable?', 'answer': 'Non-echo-planar diffusion-weighted imaging can support residual/recurrent cholesteatoma detection where direct otoscopy cannot see.', 'why': 'Surveillance strategy depends on the operation and ability to detect hidden disease.', 'follow': 'How might this affect second-look surgery decisions?'}]}, 'head-neck-imaging': {'title': 'Head & Neck CT / MRI Staging Lab', 'icon': '🧠', 'subtitle': 'Epicenter → displacement → invasion → nodes → perineural spread → what changes the operation.', 'framework': ['Modality/sequence', 'Primary site', 'Deep-space epicenter', 'Tumor extent', 'Bone/cartilage invasion', 'Vascular relationship', 'Perineural spread', 'Nodes', 'Distant/second-primary clue', 'T stage implication', 'Surgical consequence'], 'source_note': 'ENT Mastery links to open educational radiology cases. Images remain on the source sites.', 'resources': [{'name': 'Iowa Head & Neck Protocols', 'url': 'https://iowaprotocols.medicine.uiowa.edu/', 'note': 'Open head-and-neck radiology teaching pages'}, {'name': 'Learn Neuroradiology — Head & Neck Cases', 'url': 'https://learnneuroradiology.com/headneck/board-review-cases-head-and-neck/', 'note': 'Image-first board review'}], 'cases': [{'id': 'hn1', 'level': 2, 'external': 'https://learnneuroradiology.com/headneck/board-review-cases-head-and-neck/', 'prompt': 'Before naming a neck mass, identify its epicenter and which spaces/vessels it displaces.', 'answer': 'Space of origin and displacement pattern should come before tumor name.', 'why': 'Deep-neck spaces constrain the differential and predict surgical relationships.', 'follow': 'How does carotid-space origin alter the differential?'}, {'id': 'hn2', 'level': 3, 'external': 'https://iowaprotocols.medicine.uiowa.edu/protocols/squamous-cell-carcinoma-tonsillar-fossa-radiology', 'prompt': 'Review a tonsillar SCC image. What nodal basin is especially important to inspect and why?', 'answer': 'Upper jugular/level II nodes are common drainage sites; cystic nodal metastasis can be a presenting feature of HPV-associated oropharyngeal cancer.', 'why': 'The neck may reveal an otherwise subtle primary.', 'follow': 'Why is an adult cystic level II mass not presumed to be a benign branchial cyst?'}, {'id': 'hn3', 'level': 4, 'external': 'https://iowaprotocols.medicine.uiowa.edu/protocols/oral-tongue-squamous-cell-carcinoma-radiology', 'prompt': 'For oral tongue SCC, what MRI question matters beyond maximal tumor diameter?', 'answer': 'Depth and deep soft-tissue extent, relation to floor of mouth/extrinsic tongue musculature, and nodal disease affect resection and staging decisions.', 'why': 'Surgical morbidity follows three-dimensional extent, not surface size alone.', 'follow': 'How does mandibular proximity differ from true invasion?'}, {'id': 'hn4', 'level': 4, 'prompt': 'A laryngeal tumor extends into the paraglottic space with impaired vocal-fold mobility. What does the imaging contribute?', 'answer': 'It demonstrates deep submucosal spread and framework involvement that may upstage disease and change partial-larynx versus organ-preservation/laryngectomy options.', 'why': 'Laryngeal staging depends on deep spaces and function, not just visible mucosa.', 'follow': 'What imaging finding suggests cartilage invasion?'}, {'id': 'hn5', 'level': 5, 'prompt': 'MRI shows enhancement tracking along V3 toward foramen ovale from a cutaneous facial malignancy. Name the process.', 'answer': 'Perineural tumor spread along the trigeminal pathway.', 'why': 'Perineural spread changes radiation fields, surgical extent and prognosis.', 'follow': 'Which symptoms might have predicted this before imaging?'}, {'id': 'hn6', 'level': 4, 'prompt': 'A parotid mass has ill-defined margins, deep-lobe extension and stylomastoid-foramen/facial-nerve concern. What should the surgeon infer?', 'answer': 'Features raise concern for malignancy and possible facial-nerve involvement; pre-op nerve function, tissue diagnosis, neck staging and reconstructive planning become important.', 'why': 'Imaging should forecast what structures may need to be preserved, sacrificed or reconstructed.', 'follow': 'What does preoperative facial weakness imply?'}, {'id': 'hn7', 'level': 4, 'prompt': 'A carotid-bifurcation mass splays the internal and external carotid arteries and enhances avidly. What lesion pattern is classic?', 'answer': 'Carotid body paraganglioma.', 'why': 'Vascular displacement pattern is a powerful localization clue.', 'follow': 'Why is routine biopsy a poor first step?'}, {'id': 'hn8', 'level': 4, 'external': 'https://iowaprotocols.medicine.uiowa.edu/protocols/jugularjugulotympanic-paraganglioma-radiology', 'prompt': 'Review jugulotympanic paraganglioma imaging. What skull-base relationships must be mapped before treatment?', 'answer': 'Jugular foramen extent, carotid canal, lower cranial nerves, middle ear, intracranial extension and vascular supply.', 'why': 'Treatment morbidity is driven by neurovascular anatomy and tumor extent.', 'follow': 'Which cranial neuropathies should be documented?'}, {'id': 'hn9', 'level': 4, 'prompt': 'Contrast CT shows a rim-enhancing collection in the parapharyngeal space with carotid sheath displacement. What are the two immediate interpretation tasks?', 'answer': 'Confirm drainable abscess versus phlegmon and map airway/vascular/deep-space extension.', 'why': 'The scan guides both urgency and drainage route.', 'follow': 'What finding would make mediastinal imaging important?'}, {'id': 'hn10', 'level': 5, 'prompt': 'Post-treatment neck imaging shows new focal mucosal enhancement and an enlarging necrotic node. How should you approach it?', 'answer': 'Compare with prior treatment field and expected post-radiation change, then treat progressive focal mass/nodal findings as suspicious for recurrence until appropriately evaluated.', 'why': 'Post-treatment anatomy creates false positives, but interval focal progression is consequential.', 'follow': 'How can PET timing and inflammation complicate interpretation?'}, {'id': 'hn11', 'level': 4, 'prompt': 'Thyroid cancer CT shows tumor contacting the trachea and esophagus and bulky central/lateral nodes. What should be explicitly reported for operative planning?', 'answer': 'Degree of airway/esophageal invasion, vascular encasement, retrosternal extent, nodal levels and any likely RLN-course involvement.', 'why': 'Cross-sectional imaging is most useful when it answers questions ultrasound cannot fully map.', 'follow': 'What baseline functional exam matters before invasive thyroid surgery?'}, {'id': 'hn12', 'level': 5, 'prompt': 'A nasopharyngeal mass extends through skull-base foramina with cranial neuropathy. What modality generally best maps this soft-tissue/perineural extent?', 'answer': 'MRI is particularly valuable for skull-base marrow, intracranial and perineural soft-tissue spread, complemented by CT for bone.', 'why': 'Modality choice should match the staging question.', 'follow': 'What neck nodal pattern is common in nasopharyngeal carcinoma?'}]}, 'swallowing-imaging': {'title': 'FEES / MBS Interpretation Atlas', 'icon': '🥤', 'subtitle': 'Name the physiologic impairment—not just aspiration—and connect it to the intervention.', 'framework': ['Bolus consistency', 'Oral control', 'Trigger/timing', 'Hyolaryngeal excursion', 'Epiglottic inversion', 'Pharyngeal constriction', 'Residue location', 'Penetration/aspiration timing', 'UES opening', 'Response to maneuver', 'Mechanism', 'Treatment target'], 'source_note': 'These are synthetic data-pattern cases designed to train physiologic interpretation; they do not reproduce patient studies.', 'resources': [], 'cases': [{'id': 'sw1', 'level': 1, 'prompt': 'Thin liquid enters the laryngeal vestibule above the vocal folds and is ejected. Name the event before assigning cause.', 'answer': 'Laryngeal penetration with successful clearance.', 'why': 'Describe what happened before explaining why.', 'follow': 'What additional information determines clinical significance?'}, {'id': 'sw2', 'level': 2, 'prompt': 'Thin liquid passes below the vocal folds during the swallow and the patient coughs it out. What is the event and timing?', 'answer': 'Aspiration during the swallow with an effective protective response.', 'why': 'Timing helps localize the physiologic failure.', 'follow': 'What mechanisms can cause aspiration during the swallow?'}, {'id': 'sw3', 'level': 3, 'prompt': 'Aspiration occurs before the swallow because liquid spills from the vallecula/pyriforms before airway closure begins. Localize the deficit.', 'answer': 'Delayed/inefficient swallow initiation or poor bolus control is contributing to pre-swallow aspiration.', 'why': 'Pre-, during-, and post-swallow aspiration imply different mechanisms.', 'follow': 'Which compensatory strategy might be tested rather than assumed?'}, {'id': 'sw4', 'level': 3, 'prompt': 'There is substantial vallecular residue after puree with reduced tongue-base retraction. What mechanism fits?', 'answer': 'Reduced tongue-base driving force/pharyngeal pressure contributes to vallecular residue.', 'why': 'Residue location can point toward the impaired pressure generator.', 'follow': 'Why can residue become an aspiration risk after the swallow?'}, {'id': 'sw5', 'level': 3, 'prompt': 'Pyriform residue persists with restricted UES opening. What two broad mechanisms must be separated?', 'answer': 'True cricopharyngeal/UES outflow resistance versus inadequate hyolaryngeal traction/pharyngeal propulsion.', 'why': 'A CP bar is not automatically the cause of dysphagia.', 'follow': 'What test can add pressure information when needed?'}, {'id': 'sw6', 'level': 4, 'prompt': 'FEES shows pooled secretions and aspiration of secretions before any test bolus. Why is this high-value information?', 'answer': 'It demonstrates impaired baseline secretion management and airway protection independent of food consistency.', 'why': 'FEES can directly assess secretion burden, which MBS may not capture the same way.', 'follow': 'How should this influence diet-only recommendations?'}, {'id': 'sw7', 'level': 3, 'prompt': "During FEES the bolus disappears during the white-out and material is seen below the folds immediately afterward. What can and can't you say?", 'answer': 'Aspiration likely occurred during the obscured pharyngeal swallow, but FEES cannot directly visualize the exact moment during white-out.', 'why': "Know the modality's blind interval rather than overclaiming timing.", 'follow': 'When might MBS complement this?'}, {'id': 'sw8', 'level': 4, 'prompt': 'A chin-tuck eliminates aspiration in one tested patient. What is the correct interpretation?', 'answer': 'The maneuver was effective for that demonstrated physiology under tested conditions; it should not be prescribed as a universal aspiration maneuver.', 'why': 'Compensatory strategies are hypotheses to test, not reflex recommendations.', 'follow': 'What would make you stop using it?'}, {'id': 'sw9', 'level': 4, 'prompt': 'A patient after head-and-neck radiation has reduced hyolaryngeal excursion, pharyngeal residue and limited UES opening. What unifying mechanism should you consider?', 'answer': 'Radiation-associated fibrosis/weakness can impair multiple linked components of pharyngeal propulsion and traction-mediated UES opening.', 'why': 'Multiple abnormalities may share one treatment-related physiology.', 'follow': 'Why might isolated CP dilation fail?'}, {'id': 'sw10', 'level': 4, 'prompt': 'Unilateral pharyngeal weakness leaves residue predominantly on one side. What maneuver can be tested mechanistically?', 'answer': 'Head rotation toward the weak side can be tested to direct bolus toward the stronger side and alter UES mechanics.', 'why': 'Postural maneuvers should be linked to the demonstrated asymmetry.', 'follow': 'How would you verify benefit?'}, {'id': 'sw11', 'level': 5, 'prompt': "A patient aspirates silently with poor laryngeal sensation after skull-base/vagal injury. What does 'silent' tell you?", 'answer': 'The airway invasion is not triggering an effective cough response, suggesting impaired sensation/protective reflex in addition to the motor swallowing deficit.', 'why': 'Aspiration severity depends on both invasion and response.', 'follow': 'Which cranial nerve pathways are relevant?'}, {'id': 'sw12', 'level': 5, 'prompt': 'MBS shows good airway protection but severe cervical esophageal hold-up below the UES. What is the next reasoning move?', 'answer': 'Do not force a pharyngeal diagnosis; the study points toward an esophageal problem requiring appropriate esophageal evaluation.', 'why': 'A swallow study can redirect localization beyond ENT-managed pharyngeal physiology.', 'follow': 'What symptoms in the history would support esophageal localization?'}]}}
INTERPRETATION_EXTRA_V9 = {'pathology': [('p8', 'Oral cavity SCC: identify keratinization, invasive architecture, depth, PNI/LVI and margin relevance.', "The ENT endpoint is not just 'SCC': extract invasive pattern and adverse features that change neck/adjuvant decisions."), ('p9', 'Oropharyngeal SCC: explain why p16/HPV-related classification changes staging context.', 'Site and HPV-associated biology matter; p16 is interpreted in the correct oropharyngeal context rather than as a universal H&N marker.'), ('p10', 'Papillary thyroid carcinoma: identify nuclear features and then state what pathology details alter risk.', 'Diagnosis plus variant, size, extrathyroidal extension, margins, vascular invasion and nodal disease shape postoperative strategy.'), ('p11', 'Medullary thyroid carcinoma: what pathology/marker pattern should trigger hereditary thinking?', 'Neuroendocrine/C-cell phenotype with calcitonin supports MTC and should connect to RET/MEN2 evaluation.'), ('p12', 'Adenoid cystic carcinoma: identify cribriform/tubular architecture and explain why nerves matter.', 'Perineural invasion is a hallmark clinical concern and can extend far beyond the visible primary.'), ('p13', 'Mucoepidermoid carcinoma: what three cellular components help organize the diagnosis?', 'Mucous, epidermoid and intermediate cells in variable cystic/solid architecture; grade changes behavior.'), ('p14', 'Pleomorphic adenoma: why does the capsule/pseudopod concept matter surgically?', 'Capsular violation/enucleation can leave microscopic extensions and increase recurrence.'), ('p15', 'Extranodal extension in metastatic SCC: why is this not a decorative pathology phrase?', 'ENE is an adverse prognostic feature and can materially affect postoperative treatment recommendations.'), ('p16', 'Cutaneous SCC with PNI: connect microscopic nerve invasion to imaging and adjuvant planning.', 'Clinically significant PNI can require mapping named nerve pathways and can alter surgical/radiation fields.'), ('p17', 'Sinonasal inverted papilloma: distinguish endophytic architecture from invasive carcinoma.', 'Inverted growth itself is not malignant invasion; the surgeon must identify attachment and exclude synchronous carcinoma.')], 'vestibular': [('v8', 'Calorics show unilateral weakness but vHIT is normal. Why is this not automatically contradictory?', 'The tests interrogate vestibulo-ocular reflex function at different stimulus frequencies; disease can affect them differently.'), ('v9', 'vHIT shows low gain with corrective saccades on one horizontal canal. What does that localize?', 'Peripheral hypofunction in the tested canal/nerve pathway is supported when the pattern fits the clinical syndrome.'), ('v10', 'cVEMP is absent on one side. What pathway is primarily being interrogated?', 'cVEMP mainly reflects saccular/inferior vestibular nerve–mediated vestibulocollic physiology, interpreted with age/technical context.'), ('v11', 'oVEMP is abnormally large/low-threshold with third-window symptoms. What syndrome does that support?', 'Enhanced VEMP responses can support third-window physiology such as superior canal dehiscence when paired with symptoms and imaging.'), ('v12', 'Positional testing produces persistent direction-changing gaze-evoked nystagmus rather than a canal-specific fatigable pattern. What changes?', 'Central pathology moves higher on the differential; not all positional dizziness is BPPV.'), ('v13', 'Acute vestibular syndrome with a normal head impulse, direction-changing nystagmus and skew. What is the danger?', 'In the appropriate continuously symptomatic patient, this pattern is concerning for a central process such as posterior-circulation stroke.')], 'audiology': [('a8', 'A child has present OAEs but an abnormal/absent ABR. What disorder pattern should you consider?', 'Auditory neuropathy spectrum is a consideration when outer-hair-cell function is preserved but neural synchrony is abnormal.'), ('a9', 'A CI candidate has severe thresholds but surprisingly good best-aided sentence recognition. Why does that matter?', 'Implant candidacy is based on functional aided speech benefit as well as thresholds; the audiogram alone is insufficient.'), ('a10', 'A patient with unilateral profound SNHL has normal hearing contralaterally. Compare CROS and bone-conduction concepts.', 'Both route sound from the poor side toward the better cochlea; neither restores true binaural hearing in the deaf ear.'), ('a11', 'A flat tympanogram has a very large ear-canal volume. What does that suggest?', 'A patent tympanostomy tube or TM perforation is more likely than an intact TM with effusion.'), ('a12', 'A flat tympanogram has normal ear-canal volume in a child with conductive loss. What fits?', 'Middle-ear effusion is a common fit when otoscopy agrees.'), ('a13', 'Bilateral high-frequency SNHL develops during ototoxic therapy. What matters more than one absolute audiogram?', 'Documented serial threshold change from baseline and exposure context are central to ototoxicity monitoring.')], 'laryngeal-endoscopy': [('e8', 'A broad-based white vocal-fold plaque has focal stiffness and reduced wave. What is your next step?', 'Leukoplakia is a descriptor; concerning stiffness/appearance requires risk assessment and often tissue diagnosis rather than assuming benign keratosis.'), ('e9', 'Both folds move poorly after prolonged intubation. What finding would push you toward posterior glottic stenosis rather than bilateral RLN paralysis?', 'Posterior scar/bridging and impaired arytenoid joint mobility on operative palpation support mechanical fixation.'), ('e10', 'Diffuse polypoid edema of the membranous folds with preserved deeper motion. What phenotype fits?', 'Reinke edema, especially with smoking/irritant history; assess airway burden and preserve vibratory cover during treatment.'), ('e11', 'A unilateral fold is bowed with phase asymmetry and compensatory supraglottic squeeze. What must be separated?', 'True paresis/glottic insufficiency from primary muscle-tension dysphonia; compensation may hide the underlying weakness.'), ('e12', 'Papillomatous lesions recur at multiple laryngeal sites. What is the operative visual goal?', 'Map disease and preserve normal mucosa while maintaining airway/voice; repeated destructive eradication attempts increase scar.'), ('e13', 'Rhythmic oscillation involves palate, pharynx and larynx across tasks. What is more likely than task-specific spasmodic dysphonia?', 'A broader vocal/essential tremor phenotype.')]}

# Add new dedicated labs.
for _k,_lab in INTERPRETATION_LABS_V9_NEW.items():
    if _k not in INTERPRETATION_LABS:
        INTERPRETATION_LABS[_k]=_lab

# Add advanced direct cases to existing labs.
for _lab_key,_rows in INTERPRETATION_EXTRA_V9.items():
    _existing={c.get("id") for c in INTERPRETATION_LABS[_lab_key].get("cases",[])}
    for _id,_prompt,_answer in _rows:
        if _id in _existing: continue
        _external=None
        if _lab_key=="pathology": _external="https://www.pathologyatlas.ca/galleries/head-and-neck/"
        elif _lab_key=="laryngeal-endoscopy": _external="https://stroboscopy.org/video-atlas/"
        _case={
          "id":_id,"level":4,"prompt":_prompt,"answer":_answer,
          "why":"Interpret the finding through anatomy/physiology, then state the clinical or operative consequence.",
          "follow":"What important mimic or management-changing finding would you actively look for next?",
          "concept_id":f"{_lab_key}:{_id}","variant_type":"interpret"
        }
        if _external: _case["external"]=_external
        INTERPRETATION_LABS[_lab_key]["cases"].append(_case)

# For the four new labs, create reason-backward and teach variants so the same
# interpretation skill is retrieved from three directions.
for _lab_key in INTERPRETATION_LABS_V9_NEW:
    _seed=list(INTERPRETATION_LABS[_lab_key]["cases"])
    _expanded=[]
    for _c in _seed:
        _c=dict(_c)
        _c.setdefault("concept_id",f"{_lab_key}:{_c['id']}")
        _c.setdefault("variant_type","interpret")
        _expanded.append(_c)
        _r=dict(_c)
        _r["id"]=_c["id"]+"_reason"; _r["variant_type"]="reason"
        _r["prompt"]="Reason backward: which imaging/test feature is doing the most localizing or risk-stratifying work, and what mimic would you exclude?"
        _r["answer"]=_c.get("why",_c["answer"])
        _r["why"]="Reverse reasoning prevents memorizing a single picture-label pair."
        _expanded.append(_r)
        _t=dict(_c)
        _t["id"]=_c["id"]+"_teach"; _t["variant_type"]="teach"
        _t["prompt"]="Teach this study to a junior: describe it systematically, localize the abnormality, and state exactly what it changes in management or surgery."
        _t["answer"]=_c["answer"]
        _t["why"]="The endpoint is clinically actionable interpretation, not image recognition alone."
        _expanded.append(_t)
    INTERPRETATION_LABS[_lab_key]["cases"]=_expanded
    INTERPRETATION_LABS[_lab_key]["seed_case_count"]=len(_seed)


# =============================================================================
# ENT Mastery v9.1 — Integrity + Gap Closure
# =============================================================================

def _v91_slug(s):
    import re as _re
    return _re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

# v8 introduced 20 excellent complex cases using a temporary schema.
# Normalize them into the same progressive schema used by every other case.
for _idx, _c in enumerate(INTEGRATED_CASES):
    if _c.get("id","").startswith("v8-case-") and "stages" not in _c:
        _steps=_c.get("steps",[])
        _s1=_steps[0]["answer"] if len(_steps)>0 else "State the immediate priority."
        _new=_steps[1]["answer"] if len(_steps)>1 else "New clinically important information becomes available."
        _s3=_steps[2]["answer"] if len(_steps)>2 else "Build the disease-specific management plan."
        _s4=_steps[3]["answer"] if len(_steps)>3 else _c.get("takeaway","Reassess and manage the complication deliberately.")
        if ":" in _s4:
            _comp_stim,_comp_answer=_s4.split(":",1)
            _comp_stim=_comp_stim.strip()+"."
            _comp_answer=_comp_answer.strip()
        else:
            _comp_stim="A complication or attending-level follow-up issue arises."
            _comp_answer=_s4
        _concept="integrated:"+_v91_slug(_c["title"])
        _c.clear()
        _c.update({
          "id":"v8-case-%03d"%(_idx-29),
          "title":FINAL_INTEGRATED_CASES_V8[_idx-30][0],
          "domain":"Integrated ENT",
          "concept_id":_concept,
          "summary":FINAL_INTEGRATED_CASES_V8[_idx-30][1],
          "source_basis":[
             "ENT Mastery deep curriculum and OR Tomorrow modules relevant to this case",
             "Senior/Chief complication-and-rescue synthesis"
          ],
          "stages":[
             {"title":"First decision","dimension":"reasoning",
              "stimulus":FINAL_INTEGRATED_CASES_V8[_idx-30][1],
              "question":"What is your first decision or priority before the case progresses?",
              "answer":_s1,
              "why":"The first move should establish safety, localization, or the next decision-changing test rather than prematurely naming an operation."},
             {"title":"Pivotal new information","dimension":"workup",
              "stimulus":"The next pivotal finding is: "+_new,
              "question":"How does this finding change the plan, and what should you do next?",
              "answer":_s3,
              "why":"Progressive cases should force the management plan to respond to new data instead of remaining anchored to the original diagnosis."},
             {"title":"Complication / rescue","dimension":"operative",
              "stimulus":_comp_stim,
              "question":"What is your immediate response and what dangerous alternative must you exclude?",
              "answer":_comp_answer,
              "why":"Chief-level mastery includes recognizing when the original pathway has failed and switching to the appropriate rescue strategy."}
          ]
        })

# ---------------------------------------------------------------------
# 2) Interpretation follow-up answers.
# Every follow-up prompt now has a keyed answer rather than the generic fallback.
# ---------------------------------------------------------------------
FOLLOW_ANSWER_MAP_V91 = {
"What additional information would you want before calling a complete audiologic evaluation normal?":
"Confirm ear-specific pure-tone thresholds, speech reception and word recognition, tympanometry, and other age/indication-appropriate objective data; a single normal component does not establish a normal auditory system.",
"Which tympanogram patterns could accompany conductive hearing loss, and how would each alter your differential?":
"A flat tracing with normal canal volume supports effusion, a flat tracing with large volume supports perforation/patent tube, and a negative-pressure pattern supports pressure dysregulation; correlate every curve with otoscopy.",
"What speech-discrimination pattern would make you worry about pathology beyond typical cochlear loss?":
"Word recognition that is disproportionately poor for the pure-tone thresholds, particularly when asymmetric, should increase concern for neural/retrocochlear dysfunction.",
"What other audiologic and clinical findings would increase your concern for a retrocochlear lesion?":
"Asymmetric SNHL, unilateral tinnitus, disproportionate word-recognition loss, vestibular symptoms, facial/trigeminal symptoms, or other neurologic findings strengthen the need for retrocochlear evaluation.",
"Which pathology report elements most directly change postoperative treatment planning?":
"Margins, nodal burden and extranodal extension, PNI/LVI, tumor grade, depth/extent, and site-specific adverse features are among the findings most likely to alter adjuvant treatment.",
"Which salivary malignancy makes perineural invasion especially important to look for?":
"Adenoid cystic carcinoma is classically associated with perineural invasion, although clinically important PNI can occur in other salivary malignancies as well.",
"Why does the diagnosis of inverted papilloma matter to the surgeon beyond benign vs malignant?":
"It has a characteristic attachment site, recurrence risk, and association with synchronous/metachronous carcinoma, so the attachment must be mapped and definitively treated rather than merely debulking the visible mass.",
"If a mass displaces the carotid artery and internal jugular vein together, what does that tell you about its likely compartment?":
"Moving the carotid sheath contents together suggests the lesion is outside rather than arising between those structures; use the exact direction of displacement and epicenter to refine the deep-space localization.",
"What five imaging findings would you want explicitly described before operating on a deep neck-space mass?":
"Epicenter/space of origin, relationship to carotid/jugular and cranial nerves, airway/pharyngeal displacement, skull-base or bony extension, and nodal/vascular characteristics that change approach or biopsy safety.",
"What imaging feature would make perineural spread clinically important to your operative plan?":
"Enhancement or enlargement tracking along a named nerve toward a skull-base foramen matters because it can extend the surgical/radiation field beyond the visible primary tumor.",
"What is the difference between vocal-fold mobility and mucosal wave?":
"Mobility describes gross fold motion from neuromuscular/joint function; mucosal wave describes vibration of the pliable cover during phonation. One can be abnormal while the other is preserved.",
"Which finding would make you worry that a lesion is more deeply infiltrative?":
"Focal marked stiffness or loss of mucosal wave, submucosal fullness, impaired mobility, ulceration, or deep extension raises concern beyond a superficial epithelial lesion.",
"What features might help distinguish paresis from mechanical fixation, and what additional workup could be needed?":
"Look for position, bowing, phase asymmetry and compensatory behavior versus scar/joint fixation; operative palpation and selected laryngeal EMG or imaging can clarify the mechanism.",
"Does preserved mucosal wave exclude invasive carcinoma? Why not?":
"No. A small or superficially invasive cancer can retain some wave, and stroboscopy samples vibration rather than histology. Suspicious morphology still requires appropriate tissue diagnosis.",
"What findings would help you distinguish dynamic supraglottic collapse from fixed subglottic narrowing?":
"Dynamic collapse varies with respiration/pressure and localizes to supraglottic structures; fixed stenosis remains structurally narrowed. Complete endoscopic airway examination defines both level and mechanics.",
"Which turbinate is your most important constant landmark during routine FESS?":
"The middle turbinate is a central orientation landmark for the middle meatus and ethmoid complex; posteriorly the superior turbinate becomes a key guide to the sphenoid.",
"Why is blindly following an accessory maxillary ostium dangerous as a substitute for finding the natural ostium?":
"It can leave the natural drainage pathway disconnected and create mucus recirculation between openings, producing persistent symptoms despite a technically enlarged hole.",
"What should happen to your mental CT map before you cross the basal lamella?":
"Re-orient to the posterior ethmoid: know the lamina laterally, skull base superiorly, superior turbinate medially, and the expected sphenoid/optic-carotid relationships before proceeding.",
"Which preoperative CT variants would make you slow down before frontal recess or posterior ethmoid work?":
"A low/asymmetric skull base, vulnerable lateral lamella, dehiscent or low AEA, Onodi cells, lamina dehiscence, unusual frontal cells, and optic/carotid variants should all change the danger map.",
"How would purulence from the sphenoethmoidal recess change your localization?":
"It localizes disease toward the posterior ethmoid/sphenoid drainage region rather than the anterior middle-meatal pathway.",
"What imaging or clinical features would make you worry about a vascular lesion such as JNA?":
"Marked enhancement, vascular flow voids, characteristic nasopharyngeal/pterygopalatine epicenter, bony remodeling and recurrent epistaxis—especially in the classic demographic—should stop blind biopsy.",
"Which airway levels are complete cartilaginous rings and why does that matter surgically?":
"The cricoid is the only complete cartilaginous ring of the laryngeal airway; injury or expansion there has major implications for fixed subglottic caliber and reconstruction.",
"What features make you less enthusiastic about repeated endoscopic dilation?":
"Long, mature, circumferential or high-grade scar, cartilage framework compromise, posterior/glottic involvement, rapid recurrence, or repeated prior failure favor broader reconstructive thinking.",
"How do posterior glottic involvement and vocal-fold mobility change reconstructive planning?":
"They determine whether the problem is only subglottic caliber or also glottic fixation/function; that changes grafting, scar release, resection strategy, and expected voice/swallow tradeoffs.",
"Why can positive pressure dramatically change the appearance of malacia during bronchoscopy?":
"Positive pressure splints a collapsible airway open, so malacia can look much less severe unless the examination deliberately assesses spontaneous/dynamic conditions.",
"What endoscopic findings would distinguish subglottic cyst, hemangioma, and cicatricial stenosis?":
"A cyst is a focal smooth lesion, hemangioma has a vascular soft-tissue phenotype, and cicatricial stenosis is fixed scar narrowing; the morphology and dynamic behavior differ.",
"What features make an airway foreign body extraction especially high risk?":
"A nearly obstructing object, sharp/organic material, distal location, airway edema, poor ventilation, long duration, or an object that can fragment or migrate increases risk and requires a shared rescue plan.",
"Which PSG findings and patient factors would change your postoperative monitoring plan after adenotonsillectomy?":
"Age, OSA severity, oxygenation/CO2 abnormalities, obesity, craniofacial or neuromuscular disease, significant cardiopulmonary comorbidity, and the immediate postoperative course can increase monitoring needs.",
"What clinical histories would make central events more concerning?":
"Heart failure, neurologic disease, opioid/sedative exposure, high altitude, treatment-emergent events, or a central burden disproportionate to obstructive disease warrants broader physiologic evaluation.",
"How would suspected hypoventilation alter your preoperative evaluation and perioperative planning?":
"Evaluate CO2 physiology and underlying pulmonary/neuromuscular/obesity-hypoventilation contributors because upper-airway surgery may not correct the primary ventilatory problem and anesthesia risk is higher.",
"What parts of this PSG would you specifically need before discussing hypoglossal nerve stimulation?":
"Overall event burden, obstructive versus central/mixed composition, oxygenation, sleep time/quality and positional/stage pattern must be understood before adding PAP history, anatomy and DISE phenotype.",
"How would a non-supine AHI near normal change your counseling compared with severe non-positional OSA?":
"It suggests a strong positional phenotype and makes positional therapy or other targeted options more relevant than in disease that remains severe in all positions.",
"What threshold for central + mixed events is important in current Inspire labeling?":
"Conventional Inspire candidacy requires predominantly obstructive disease; central plus mixed events should not constitute more than 25% of the total AHI under current labeling.",
"Why does complete concentric collapse at the soft palate matter?":
"It is a key exclusion phenotype for conventional Inspire upper-airway stimulation because the collapse mechanism is less likely to respond adequately to tongue-protrusor stimulation alone.",
"What alternative anatomic or non-anatomic treatments would you consider based on the patient's phenotype?":
"Options include PAP troubleshooting, oral appliance, weight-directed therapy, positional therapy, palate/lateral-wall or tongue-base procedures, skeletal surgery, or other targeted approaches depending on the demonstrated mechanism.",
"What other PSG and DISE features still have to be checked even if AHI and BMI fall within current labeling?":
"Confirm predominantly obstructive events, appropriate PAP failure/intolerance, absence of disqualifying palatal collapse, and an anatomy/airway pattern that can be effectively stimulated.",
"What would you want from a titration study or repeat sleep evaluation before deciding on revision or adjunctive treatment?":
"Define residual event type, position/stage dependence, oxygenation, device use/settings and whether the remaining physiology is actually obstructive and anatomically targetable.",
"How would you explain this distinction to a junior resident presenting an HNS candidate?":
"Labeling, payer rules, evidence, PSG physiology and DISE anatomy answer different questions; candidacy requires all of them rather than memorizing one AHI or BMI cutoff.",
"Why can calorics be abnormal while vHIT is normal?":
"They test vestibulo-ocular reflex function at very different stimulus frequencies, so a disorder may impair low-frequency caloric responses while preserving higher-frequency head-impulse function.",
"What does a corrective saccade mean physiologically?":
"It indicates the eyes did not remain adequately stabilized during head motion and needed a catch-up movement, supporting deficient vestibulo-ocular reflex function in that canal plane.",
"How would horizontal-canal BPPV look different on positional testing?":
"The supine roll test produces direction-changing horizontal nystagmus—typically geotropic or apogeotropic—rather than the torsional upbeat pattern of posterior-canal BPPV.",
"What clinical red flags would make you escalate to neurologic imaging/workup?":
"Focal neurologic deficits, central eye-movement signs, inability to walk out of proportion to vertigo, new severe headache/neck pain, atypical persistent nystagmus or other stroke-risk features should raise concern.",
"Which features are descriptors versus management decisions?":
"Composition, echogenicity, shape, margins and echogenic foci are image descriptors; the resulting risk category plus size and patient context drive FNA or surveillance decisions.",
"Why should a cystic nodule not be managed from size alone?":
"Composition and other sonographic features determine malignancy risk. Size thresholds are applied only after the lesion has been risk-stratified.",
"How can thyroiditis complicate this comparison?":
"Abnormal background thyroid echogenicity can make a nodule appear relatively hypo- or isoechoic, so the interpreter must recognize the diseased parenchymal reference.",
"On which imaging plane should you judge taller-than-wide?":
"On the transverse image, comparing anteroposterior height with transverse width.",
"Which adjacent structures make suspected extrathyroidal extension surgically important?":
"Trachea, esophagus, strap muscles, recurrent-laryngeal-nerve course/tracheoesophageal groove and major vessels are particularly important for operative planning.",
"How can rim calcification affect FNA targeting?":
"A heavily calcified rim can obscure the viable soft-tissue component or impede needle access; target accessible suspicious soft tissue rather than calcification alone.",
"What patient-specific factors can still modify the conversation?":
"Age, comorbidity, radiation/family history, contralateral disease, patient preferences, surgical risk, surveillance feasibility and whether the result would change treatment all matter.",
"What adjunct can be added to needle sampling in selected thyroid-cancer nodes?":
"Thyroglobulin measurement from the FNA needle washout can support metastatic differentiated thyroid-cancer evaluation in appropriate nodes.",
"Which morphology changes would make it suspicious?":
"Round shape, loss of hilum, cystic change, punctate echogenic foci/calcification, abnormal peripheral vascularity or focal cortical abnormalities increase concern.",
"When would cross-sectional imaging add value?":
"When ultrasound cannot adequately map bulky, invasive, retrosternal, retropharyngeal or otherwise deep disease, or when airway/esophageal/vascular relationships will change surgery.",
"What complementary localization tests might be used when surgery is planned?":
"Depending on the parathyroid context, ultrasound, sestamibi/SPECT-CT, 4D-CT, MRI or advanced selective localization can be combined; none replaces the biochemical diagnosis.",
"What imaging feature or trend would raise concern?":
"Interval growth, increasingly suspicious morphology, invasive features or evolving abnormal nodal disease are more concerning than a stable nonspecific postoperative focus.",
"Which structures form your medial danger boundary?":
"At the temporal bone, the otic capsule/inner-ear structures and facial-nerve course become key medial/deep boundaries as dissection progresses.",
"What chronic ear disease commonly erodes the incus?":
"Cholesteatoma, particularly involving the epitympanum/posterosuperior middle ear, commonly erodes the long process of the incus.",
"Which hidden recesses matter for residual disease?":
"Sinus tympani, facial recess, epitympanum, anterior epitympanic spaces and other poorly visualized recesses can harbor residual cholesteatoma.",
"What would make you suspect concomitant inner-ear injury?":
"Sensorineural hearing loss, severe persistent vertigo, pneumolabyrinth or otic-capsule violation raises concern beyond isolated ossicular trauma.",
"Which symptoms and vestibular test patterns would support it?":
"Sound/pressure-induced vertigo or oscillopsia, autophony and enhanced/low-threshold VEMP responses support third-window physiology when CT anatomy agrees.",
"What must be documented about facial weakness timing?":
"Whether weakness was immediate at injury or delayed, plus completeness/severity, because timing changes the likely mechanism and management pathway.",
"What factors influence transmastoid versus middle-fossa/combined repair?":
"Defect size/location/number, encephalocele volume, ossicular/hearing status, mastoid access, prior surgery and the need for broad superior tegmen exposure determine the corridor.",
"How do retrosigmoid, translabyrinthine and middle-fossa goals differ conceptually?":
"Retrosigmoid can preserve hearing in selected tumors while exposing CPA, translabyrinthine sacrifices residual hearing for direct IAC/CPA access, and middle fossa targets selected small intracanalicular tumors with hearing preservation intent.",
"What must MRI establish in severe congenital hearing loss?":
"Presence and caliber of the cochlear nerve and inner-ear soft-tissue anatomy are critical because an absent nerve can fundamentally change implant expectations.",
"What other vascular variant should be checked near the cochlea/Eustachian tube?":
"An aberrant internal carotid artery course/dehiscence in the middle ear is a major vascular hazard to recognize before intervention.",
"Why does aeration of surrounding cells matter?":
"Aerated pathways can create potential drainage corridors to a petrous-apex lesion and influence whether a minimally invasive drainage route is feasible.",
"How might this affect second-look surgery decisions?":
"Reliable non-echo-planar diffusion surveillance can reduce the need for routine second-look surgery in selected ears, whereas uncertain imaging access or high-risk anatomy may still favor operative inspection.",
"How does carotid-space origin alter the differential?":
"It prioritizes lesions arising from vessels, vagus/sympathetic chain, lower cranial nerves or paraganglionic tissue rather than salivary/prestyloid masses.",
"Why is an adult cystic level II mass not presumed to be a benign branchial cyst?":
"HPV-associated oropharyngeal SCC commonly metastasizes as a cystic upper-neck node, so malignancy must be excluded before a benign congenital label is accepted.",
"How does mandibular proximity differ from true invasion?":
"Abutment or inflammatory change does not equal cortical/medullary tumor invasion; true invasion changes resection extent and must be assessed by imaging and operative/pathologic correlation.",
"What imaging finding suggests cartilage invasion?":
"Focal cartilage destruction, replacement/erosion or convincing tumor extension through the laryngeal framework is more concerning than nonspecific sclerosis alone.",
"Which symptoms might have predicted this before imaging?":
"Pain, numbness/paresthesia, progressive motor deficit or other named-nerve symptoms can precede radiographic recognition of perineural spread.",
"What does preoperative facial weakness imply?":
"It strongly raises concern for malignant facial-nerve involvement and changes counseling, resection extent and immediate reanimation planning.",
"Why is routine biopsy a poor first step?":
"A highly vascular paraganglioma can bleed substantially; characteristic imaging/vascular anatomy often establishes the working diagnosis without blind tissue sampling.",
"Which cranial neuropathies should be documented?":
"Lower cranial nerves IX–XII, facial function when relevant, and sympathetic/other skull-base deficits should be documented according to the lesion's extent.",
"What finding would make mediastinal imaging important?":
"Extension through the danger/retropharyngeal spaces below the thoracic inlet, chest symptoms, persistent sepsis or imaging concern for descending infection should prompt mediastinal assessment.",
"How can PET timing and inflammation complicate interpretation?":
"Recent radiation, surgery or infection can produce FDG uptake, so early post-treatment PET can generate inflammatory false positives; correlate with timing, anatomy and interval change.",
"What baseline functional exam matters before invasive thyroid surgery?":
"Preoperative laryngeal examination documenting vocal-fold mobility is especially important when invasive disease or voice symptoms raise concern for RLN involvement.",
"What neck nodal pattern is common in nasopharyngeal carcinoma?":
"Upper cervical and retropharyngeal nodal disease is common and may be bilateral because of nasopharyngeal lymphatic drainage.",
"What additional information determines clinical significance?":
"Depth/frequency of penetration, clearance, sensation/cough response, consistency, residue, patient pulmonary reserve and whether the pattern repeats all affect significance.",
"What mechanisms can cause aspiration during the swallow?":
"Incomplete laryngeal vestibule closure, reduced vocal-fold closure, impaired hyolaryngeal excursion or poor coordination can allow material below the folds during the pharyngeal swallow.",
"Which compensatory strategy might be tested rather than assumed?":
"Depending on the demonstrated physiology, posture such as chin tuck or head turn, bolus-volume/consistency change or swallow maneuver can be trialed and kept only if the study shows benefit.",
"Why can residue become an aspiration risk after the swallow?":
"Material left in the vallecula or pyriforms can spill into the reopened laryngeal vestibule after airway protection relaxes.",
"What test can add pressure information when needed?":
"High-resolution pharyngeal/esophageal manometry can add pressure and UES-relaxation information when fluoroscopic anatomy alone cannot resolve the mechanism.",
"How should this influence diet-only recommendations?":
"Poor secretion management means risk exists even without oral intake, so the plan must address airway protection, sensation, pulmonary status and secretion control rather than only changing food consistency.",
"When might MBS complement this?":
"When exact bolus timing, hyolaryngeal excursion, UES opening or oral-phase mechanics need visualization during the FEES white-out interval.",
"What would make you stop using it?":
"If the maneuver worsens residue/airway invasion, is not reproducibly effective, or is unsafe/unrealistic for the patient, it should not be prescribed.",
"Why might isolated CP dilation fail?":
"If reduced pharyngeal driving force or hyolaryngeal traction—not fixed UES resistance—is the dominant cause, enlarging the UES alone will not correct the physiology.",
"How would you verify benefit?":
"Repeat the maneuver during the same instrumental study and compare residue, airway invasion and bolus flow directly.",
"Which cranial nerve pathways are relevant?":
"Superior-laryngeal/vagal sensory pathways and vagal motor function are central to laryngeal sensation, cough and pharyngeal/laryngeal motor protection.",
"What symptoms in the history would support esophageal localization?":
"Food sticking lower in the chest, regurgitation, delayed passage, reflux symptoms or dysphagia for solids/liquids after the pharyngeal swallow supports an esophageal component."
}

_GENERIC_FOLLOW_BY_LAB_V91 = {
 "audiology":"Look for asymmetry, speech-recognition performance, tympanometric consistency and a finding that would move the problem from routine cochlear/middle-ear loss toward neural, third-window or other nonroutine physiology.",
 "pathology":"Look next for invasion, grade, margins, PNI/LVI, nodal/ENE features or a histologic mimic that would change staging, surgery or adjuvant therapy.",
 "ct-mri":"Re-check the lesion's epicenter, displacement pattern, critical neurovascular relationship, bone invasion and any finding that would change the surgical corridor or biopsy safety.",
 "laryngeal-endoscopy":"Re-check vocal-fold mobility, mucosal wave/stiffness, lesion depth, airway impact and a mechanical or malignant mimic that would change treatment.",
 "sinonasal":"Re-check laterality, vascularity, skull-base/orbital relationship, natural drainage pathways and whether the finding represents inflammatory disease versus a unilateral tumor or complication.",
 "airway-bronchoscopy":"Look for a second airway lesion, dynamic versus fixed behavior, exact level/length, vocal-fold mobility and any finding that changes the ventilation or reconstruction plan.",
 "sleep-psg":"Re-check event type, oxygen/CO2 burden, position/stage dependence, PAP history and whether anatomy or nonobstructive physiology changes the treatment pathway.",
 "vestibular":"Look for central eye-movement red flags, concordance across frequency-specific vestibular tests and a pattern that changes localization or triggers neurologic evaluation.",
 "thyroid-ultrasound":"Re-check invasive features, suspicious cervical nodes and whether the finding actually crosses a risk/size threshold that changes FNA or surgery.",
 "temporal-bone-imaging":"Re-check the facial nerve, labyrinth, tegmen, vascular variants and hidden disease extent that would change hearing counseling or the operative route.",
 "head-neck-imaging":"Re-check deep-space epicenter, perineural spread, vascular encasement, cartilage/bone invasion and nodal disease that changes stage or resection.",
 "swallowing-imaging":"Re-check timing of airway invasion, residue location, sensation/response and whether the proposed maneuver actually improves the demonstrated physiology."
}

for _lab_key,_lab in INTERPRETATION_LABS.items():
    for _case in _lab.get("cases",[]):
        if _case.get("follow") and not _case.get("follow_answer"):
            _case["follow_answer"]=FOLLOW_ANSWER_MAP_V91.get(
                _case["follow"],
                _GENERIC_FOLLOW_BY_LAB_V91.get(_lab_key,
                    "Identify the most important mimic or red flag and state exactly what additional finding would change management.")
            )

# ---------------------------------------------------------------------
# 3) FPRS / Trauma depth based on AO CMF Trauma and thePlasticsFella.
# External content remains linked; ENT Mastery supplies original synthesis.
# ---------------------------------------------------------------------
FPRS_DEPTH_V91 = [
 {"topic":"Structured Facial Trauma Examination","recognize":"In facial trauma, vision, airway, occlusion, facial width/projection, canthal position, sensation and CSF signs are the functional readouts that matter before fracture names.",
  "localize":"Palpate and inspect orbital rims, zygomatic projection, nasal/NOE complex, maxillary/mandibular buttresses and dental occlusion in a reproducible sequence.",
  "workup":"Thin-cut CT with multiplanar/3-D review for complex injury; ophthalmologic and neurologic evaluation are driven by functional findings.",
  "manage":"Stabilize airway/vision/brain injury first, then repair fractures that create functional or meaningful structural deformity.",
  "operate":"Reconstruct the facial framework from stable reference points and restore occlusion, width, height, projection and orbital volume.",
  "teach":"AO emphasizes diagnosis, indications and treatment by facial subunit; never let a dramatic CT distract from vision or occlusion.",
  "source_urls":["https://surgeryreference.aofoundation.org/cmf/trauma"]},
 {"topic":"NOE Fracture Mechanics","recognize":"NOE fractures involve the nose, medial orbit/ethmoid region, frontal-sinus base and the medial canthal tendon-bearing segment; traumatic telecanthus is a major clue.",
  "localize":"Classify by the canthal-bearing fragment: a large stable fragment versus comminution with attached tendon versus tendon avulsion from fragmented bone.",
  "workup":"CT defines comminution and associated frontal/orbital/maxillary injury, but type II versus III can require intraoperative assessment of medial canthal tendon attachment.",
  "manage":"Observe only selected stable injuries; displaced injuries require restoration of medial canthal position, nasal projection and medial buttress anatomy.",
  "operate":"Reduction must control the tendon-bearing fragment and rebuild dorsal/medial support before fixation is accepted.",
  "teach":"NOE is not an isolated nasal-bone fracture—the medial canthal tendon and central facial buttress are the defining functional anatomy.",
  "source_urls":["https://surgeryreference.aofoundation.org/cmf/trauma/midface/noe-type-i/definition","https://surgeryreference.aofoundation.org/cmf/trauma/midface/noe-type-ii/definition","https://surgeryreference.aofoundation.org/cmf/trauma/midface/noe-type-iii/definition"]},
 {"topic":"Frontal Sinus Fracture Decision Model","recognize":"Do not reduce frontal-sinus trauma to anterior-table displacement. Assess anterior table, posterior table, frontal recess/outflow tract, dural injury/CSF leak and comminution.",
  "localize":"The anterior table drives contour; posterior table/dura drive intracranial safety; outflow-tract injury drives future sinus function and mucocele risk.",
  "workup":"CT maps all five variables and associated skull-base injury; longitudinal follow-up is required when the sinus is preserved.",
  "manage":"Observation, ORIF, sinus-preserving endoscopic strategy, obliteration or cranialization are selected from the combined anatomic pattern.",
  "operate":"When cranialization is required, the operative endpoint is a safe intracranialized space with meticulous mucosal removal and definitive management of the posterior wall/outflow pathway.",
  "teach":"AO's decision model is anatomy-based, not a single millimeter cutoff.",
  "source_urls":["https://surgeryreference.aofoundation.org/cmf/trauma/skull-base-cranial-vault/further-reading/indications-for-surgery","https://surgeryreference.aofoundation.org/cmf/trauma/skull-base-cranial-vault/frontal-sinus-posterior-table/cranialization"]},
 {"topic":"Mandibular Biomechanics and Occlusion","recognize":"Mandible fractures are functional skeletal injuries: malocclusion, segment mobility, inferior-alveolar sensory change and condylar mechanics matter.",
  "localize":"Symphysis/parasymphysis, body, angle and condyle have different force environments; a blow to the anterior mandible may transmit force to one or both condyles.",
  "workup":"Occlusal exam plus panoramic/CT imaging according to complexity; identify multiple fractures and dental/open-fracture status.",
  "manage":"Closed versus open treatment depends on site, displacement, occlusion, dentition and stability.",
  "operate":"Fixation must neutralize the local biomechanics; the symphysis experiences torsional forces and complex fractures may require load-bearing rather than simple load-sharing constructs.",
  "teach":"AO's recurring principle is to restore preinjury occlusion and apply fixation that matches the biomechanics of that fracture.",
  "source_urls":["https://surgeryreference.aofoundation.org/cmf/trauma/mandible/further-reading/biomechanics-of-the-mandible","https://surgeryreference.aofoundation.org/cmf/trauma/mandible/symphysis-and-parasymphysis-simple/orif-two-load-sharing-plates"]},
 {"topic":"Rhinoplasty Tip Mechanics","recognize":"Tip shape is the product of lower-lateral-cartilage form, support, projection, rotation and skin/soft-tissue envelope—not simply tip width.",
  "localize":"Medial crura, domes and lateral crura create different vectors; lateral-crural weakness or malposition can also create external-valve dysfunction.",
  "workup":"Standardized functional/aesthetic analysis and photography; define projection, rotation, symmetry, alar support and valve behavior before selecting a maneuver.",
  "manage":"Use cartilage-sparing reshaping, sutures and support grafts according to the mechanical deficit; avoid destructive cephalic over-resection.",
  "operate":"Preserve adequate lateral-crural support and choose columellar/septal-extension, lateral-crural-strut, rim or other grafts only for a defined structural objective.",
  "teach":"ThePlasticsFella's useful framing is support-preserving tip modification: every maneuver should have a projection, rotation, contour or valve purpose.",
  "source_urls":["https://www.theplasticsfella.com/rhinoplasty/"]},
 {"topic":"Rhinoplasty Graft Selection","recognize":"Spreader, batten, rim, lateral-crural-strut, septal-extension, dorsal and tip grafts solve different structural problems.",
  "localize":"Midvault/internal valve, lateral wall/external valve, caudal septum/tip support and dorsal contour are separate mechanical zones.",
  "workup":"Identify the failed zone and available cartilage source before choosing a named graft.",
  "manage":"Septal cartilage is often preferred when adequate; auricular cartilage is useful for curved support, while rib is reserved for larger structural needs.",
  "operate":"Bevel, stabilize and position grafts so the construct solves the intended vector without creating visibility, warping or excessive stiffness.",
  "teach":"Do not memorize graft names as operations—name the mechanical failure first, then pick the graft.",
  "source_urls":["https://www.theplasticsfella.com/rhinoplasty/"]},
 {"topic":"Bilobed Flap","recognize":"A bilobed flap is a random-pattern double-transposition flap useful especially for small-to-moderate nasal defects where adjacent skin provides superior color/texture match.",
  "localize":"The first lobe fills the primary defect and the second closes the first-lobe donor defect around a shared pivot, redistributing tension away from free margins.",
  "workup":"Analyze defect diameter, subunit, skin laxity, alar-margin risk and donor-site direction before drawing the flap.",
  "manage":"Use when local tissue match and tension redistribution outperform a graft or simple closure; avoid it when the arc will distort a critical margin.",
  "operate":"Modern design uses a reduced total rotation arc, a first lobe approximating defect width, a smaller second lobe, broad undermining and careful thinning while preserving subdermal perfusion.",
  "teach":"Major preventable failures are pincushioning, alar retraction/distortion, standing cones and vascular compromise from poor design or excessive thinning.",
  "source_urls":["https://www.theplasticsfella.com/bilobed-flaps/"]},
 {"topic":"Cervicofacial Flap","recognize":"Large cheek/lateral-face defects can be reconstructed by recruiting broad adjacent cervical/facial skin with good color and texture match.",
  "localize":"Design around facial aesthetic units, laxity and the vectors that can pull on eyelid, lip or nasal margins.",
  "workup":"Define defect depth, exposed structures, prior radiation, neck scars and whether regional/free tissue is actually required.",
  "manage":"Use a cervicofacial advancement/rotation concept when local tissue can close the defect without unacceptable tension or free-margin distortion.",
  "operate":"Elevate in a vascularity-preserving plane with broad mobilization and distribute tension away from the eyelid and other critical margins.",
  "teach":"The flap succeeds by recruiting lax tissue over a wide area; concentrating tension at the defect recreates ectropion and contour problems.",
  "source_urls":["https://www.theplasticsfella.com/january-26th/"]},
 {"topic":"Skin Graft Selection","recognize":"Split- and full-thickness grafts differ in contraction, color/texture match, donor closure and take requirements.",
  "localize":"Choose graft thickness from recipient bed vascularity, contour and the functional/aesthetic cost of secondary contraction.",
  "workup":"Ensure a vascular recipient bed, control contamination/bleeding and evaluate whether exposed cartilage/bone lacks a graftable vascular surface.",
  "manage":"Full-thickness grafts often suit smaller facial defects needing better match and less contraction; split-thickness grafts cover larger areas but contract more.",
  "operate":"Precise sizing, complete bed contact, immobilization and hematoma/seroma prevention are central to graft take.",
  "teach":"A graft is only as viable as its recipient bed; the operation is creating reliable contact with vascular tissue.",
  "source_urls":["https://www.theplasticsfella.com/principles/"]},
 {"topic":"Dynamic Facial Reanimation","recognize":"Facial reanimation strategy depends on duration, injury level, available proximal/distal nerve and whether native facial musculature remains viable.",
  "localize":"Direct repair/grafting reconnects facial nerve pathways; nerve transfers provide a new motor source; muscle transfer replaces a nonviable motor unit.",
  "workup":"Document facial zones, ocular protection, synkinesis, denervation duration and electrodiagnostic/anatomic information when it changes reconstruction.",
  "manage":"Tension-free primary repair for suitable acute injury, cable graft for a gap with available stumps, nerve transfer when proximal input is unavailable, and regional/free muscle transfer when native muscle is no longer useful.",
  "operate":"Match donor axons, timing and target muscle to the functional objective while preserving eye protection and resting symmetry.",
  "teach":"ThePlasticsFella's decision model is useful: patient + etiology + timing + lesion location determine whether you repair, graft, transfer nerve, or replace muscle.",
  "source_urls":["https://www.theplasticsfella.com/dynamic-facial-nerve-palsy-reconstruction/"]},
]
for _m in FPRS_DEPTH_V91:
    _bucket=DEEP_MODULES_V6.setdefault("Facial Plastics / Trauma",[])
    if not any(x["topic"].lower()==_m["topic"].lower() for x in _bucket):
        _bucket.append({k:v for k,v in _m.items() if k not in ("source_urls",)})

# ---------------------------------------------------------------------
# 4) High-value operative gap closure.
# ---------------------------------------------------------------------
OR_GAP_CLOSURE_V91 = {
 "microflap":("Microlaryngoscopy / Microflap for Benign Vocal-Fold Lesion","Laryngology",
  ["Confirm lesion, vibratory deficit and nonoperative/voice-therapy role.","Obtain atraumatic suspension exposure and high-magnification view.","Incise/raise a limited microflap and remove the lesion while preserving superficial lamina propria and epithelium.","Redrape the cover and confirm hemostasis with minimal thermal injury."],
  ["Dental/tongue injury","Vocal-fold scar","Ligament injury","Web/granuloma"],[]),
 "rrp-debridement":("RRP Debridement / Laser-Safety Framework","Laryngology",
  ["Map airway disease and define the functional target rather than attempting destructive eradication.","Coordinate laser/fire-safe anesthesia and protective equipment when laser is used.","Debulk papilloma while preserving normal epithelium/commissures and airway caliber.","Document disease burden and plan longitudinal/adjuvant therapy when appropriate."],
  ["Airway fire","Anterior commissure scar/web","Bleeding","Airway edema"],[]),
 "reconstructive-palate":("Reconstructive Palatal Surgery for OSA","Sleep Surgery",
  ["Confirm retropalatal/lateral-wall collapse phenotype and prior PAP/tonsil/anatomic factors.","Expose palate/tonsillar pillars and identify the reconstructive vector planned.","Reposition/reconstruct palatopharyngeal tissue rather than relying on indiscriminate ablation.","Confirm hemostasis and plan postoperative airway/pain/swallow monitoring."],
  ["Bleeding","Velopharyngeal insufficiency","Dysphagia","Airway edema"],[]),
 "lingual-tonsillectomy":("Lingual Tonsillectomy / Tongue-Base Reduction","Sleep / Airway",
  ["Confirm tongue-base/lingual-tonsil contribution by exam/DISE and define airway strategy.","Expose tongue base with transoral system and identify midline/lingual-artery risk zones.","Reduce target tissue while protecting deep tongue musculature and neurovascular structures.","Secure hemostasis and monitor edema/airway/swallowing."],
  ["Lingual artery hemorrhage","Airway edema","Dysphagia","Taste/sensory change"],[]),
 "hyoid-genioglossus":("Hyoid Suspension / Genioglossus Advancement Concepts","Sleep Surgery",
  ["Confirm retrolingual/hypopharyngeal collapse phenotype and role within multilevel treatment.","Map hyoid, mandible, genial tubercle and airway anatomy.","Apply the selected skeletal/soft-tissue advancement vector to stabilize the hypopharyngeal/tongue-base airway.","Confirm airway plan and counsel on multilevel expectations."],
  ["Hypoglossal nerve","Dental roots/mandible","Dysphagia","Under-correction"],[]),
 "closed-nasal-reduction":("Closed Nasal Fracture Reduction","Facial Trauma",
  ["Exclude septal hematoma and complex NOE/orbital/frontal injuries; document preinjury appearance when possible.","Reassess deformity/obstruction after swelling permits reliable examination.","Mobilize and reduce displaced nasal bones/septal components using controlled external/internal forces.","Confirm dorsal alignment, septal airway and stabilize as indicated."],
  ["Septal hematoma","Persistent deformity/obstruction","Epistaxis","Missed NOE injury"],
  ["https://surgeryreference.aofoundation.org/cmf/trauma/midface/nasal-bone/definition"]),
 "noe-orif":("NOE Fracture ORIF","Facial Trauma",
  ["Classify comminution/canthal-bearing segment and map associated frontal/orbital/maxillary fractures.","Expose central facial framework and identify the medial canthal tendon-bearing fragment or tendon avulsion.","Restore nasal/medial orbital buttress projection and secure the canthal complex in the correct three-dimensional position.","Reconstruct dorsal support when comminution has removed stable nasal support."],
  ["Medial canthal malposition/telecanthus","Lacrimal system","Orbit","CSF/skull base"],
  ["https://surgeryreference.aofoundation.org/cmf/trauma/midface/noe-type-i/definition","https://surgeryreference.aofoundation.org/cmf/trauma/midface/noe-type-ii/definition","https://surgeryreference.aofoundation.org/cmf/trauma/midface/noe-type-iii/definition"]),
 "frontal-sinus-trauma":("Frontal Sinus Fracture Repair / Cranialization Framework","Facial Trauma / Skull Base",
  ["Assess anterior table, posterior table, frontal recess/outflow tract, dural injury/CSF leak and comminution.","Choose observation, ORIF, sinus-preserving drainage strategy, obliteration or cranialization from the combined anatomy.","For cranialization, expose the sinus, remove diseased mucosa/posterior wall as required and create a safe intracranialized space.","Restore anterior contour and establish long-term surveillance for sinus/mucocele/intracranial complications."],
  ["Dura/brain","Frontal recess failure","Mucocele","Contour deformity"],
  ["https://surgeryreference.aofoundation.org/cmf/trauma/skull-base-cranial-vault/further-reading/indications-for-surgery","https://surgeryreference.aofoundation.org/cmf/trauma/skull-base-cranial-vault/frontal-sinus-posterior-table/cranialization"]),
 "bilobed-flap":("Bilobed Flap for Nasal Defect","Facial Plastics",
  ["Analyze defect size/subunit, alar-margin risk and available surrounding laxity.","Design the pivot and two lobes with the first approximating defect width and the second smaller, using a limited modern rotation arc.","Elevate with enough thickness to preserve subdermal blood supply and broadly undermine to reduce tension.","Close the secondary donor site first as appropriate, transpose lobes, inset without alar distortion and manage standing cones."],
  ["Pincushion/trapdoor","Alar retraction","Dog-ear","Flap ischemia"],
  ["https://www.theplasticsfella.com/bilobed-flaps/"]),
 "melolabial-flap":("Melolabial / Nasolabial Flap","Facial Plastics",
  ["Define nasal ala/sidewall or perioral defect depth and whether lining/support also need reconstruction.","Design the flap along the melolabial fold with an appropriate superior/inferior base and tension vector.","Elevate in a vascularity-preserving plane and transpose/advance without flattening the fold or distorting the alar margin.","Inset in one or staged fashion according to defect and pedicle design."],
  ["Alar distortion","Trapdoor","Pedicle compromise","Blunted melolabial fold"],[]),
 "cervicofacial-flap":("Cervicofacial Advancement / Rotation Flap","Facial Plastics",
  ["Analyze cheek/lateral-face defect, eyelid/lip free margins, prior radiation and available neck/face laxity.","Design a broad advancement/rotation arc along favorable facial/neck boundaries.","Elevate in a vascularity-preserving plane with wide mobilization.","Inset with tension directed away from eyelid/lip and close donor site without contour distortion."],
  ["Ectropion","Distal flap ischemia","Facial nerve injury by plane","Contour/trapdoor"],
  ["https://www.theplasticsfella.com/january-26th/"]),
 "skin-graft-face":("Facial Full-Thickness / Split-Thickness Skin Graft","Facial Plastics",
  ["Assess recipient-bed vascularity, defect depth/contour and contraction tolerance.","Select donor site/thickness for color, texture and functional need.","Harvest and defat as appropriate; obtain meticulous hemostasis and exact graft-bed contact.","Secure/bolster to prevent shear, hematoma and seroma until inosculation/revascularization occurs."],
  ["Graft loss","Hematoma/seroma","Contraction","Color/contour mismatch"],
  ["https://www.theplasticsfella.com/principles/"]),
 "facial-nerve-reanimation":("Facial Nerve Repair / Cable Graft / Nerve Transfer","Facial Plastics",
  ["Define lesion level, denervation duration, available proximal/distal nerve and muscle viability.","Perform tension-free direct repair when possible; use cable graft when a short gap prevents primary repair.","When proximal facial input is unavailable, select a donor nerve transfer such as masseteric or hypoglossal strategy according to goals.","If native facial muscle is no longer viable, plan regional or free functional muscle transfer and static eye/support procedures as needed."],
  ["Synkinesis","Donor-nerve morbidity","Poor spontaneous smile","Ocular exposure"],
  ["https://www.theplasticsfella.com/dynamic-facial-nerve-palsy-reconstruction/"]),
 "free-flap-basics":("Head & Neck Free-Flap Reconstruction — Core Framework","Head & Neck Reconstruction",
  ["Define the post-ablative defect by lining, soft-tissue bulk, bone, skin and functional goals before choosing a donor.","Match flap tissue characteristics/pedicle to defect and recipient vessels; plan backup recipient/donor options.","Perform inset to restore separation, contour and mobility, then microvascular arterial and venous anastomoses.","Monitor perfusion intensively and return urgently for threatened flap when salvage remains possible."],
  ["Arterial thrombosis","Venous congestion","Fistula","Donor-site morbidity"],[]),
 "pharyngocutaneous-fistula":("Pharyngocutaneous Fistula / Salivary Leak Management","Head & Neck",
  ["Recognize salivary drainage, neck infection, wound breakdown or carotid exposure risk after pharyngeal surgery.","Define leak extent, nutritional status, infection and vascular danger.","Control infection/saliva, provide nutritional support and wound protection; use salivary bypass/negative pressure or operative closure/reconstruction in selected persistent/high-risk leaks.","Protect great vessels and optimize tissue before definitive reconstruction."],
  ["Carotid blowout","Deep-neck infection","Aspiration","Chronic stenosis"],[]),
 "laryngeal-fracture":("Laryngeal Fracture Repair","Laryngology / Trauma",
  ["Airway first; document voice, laryngoscopic mucosal injury/mobility and CT framework disruption.","Classify stable minor injury versus displaced fracture, exposed cartilage or severe endolaryngeal disruption.","Secure airway with the least traumatic strategy; explore/reduce/fix displaced framework and repair mucosa when indicated.","Restore airway framework and mucosal continuity while minimizing scar and long-term voice dysfunction."],
  ["Airway loss","Posterior glottic scar","Vocal-fold immobility","Subglottic stenosis"],[]),
 "pta-drainage":("Peritonsillar Abscess Drainage","General ENT",
  ["Confirm PTA phenotype and exclude impending airway/deep-neck spread.","Position, anesthetize and select needle aspiration versus incision/drainage based on patient/anatomy.","Enter the superior peritonsillar space with controlled depth and lateral orientation away from carotid danger.","Drain, culture selectively, treat with antibiotics/analgesia/hydration and reassess airway."],
  ["Carotid injury","Aspiration","Bleeding","Missed parapharyngeal infection"],[]),
 "airway-fb":("Rigid Bronchoscopy for Airway Foreign Body","Pediatric Airway",
  ["Treat unstable complete obstruction immediately; in stable suspected aspiration, coordinate surgeon/anesthesia shared ventilation plan.","Expose larynx and pass rigid bronchoscope under controlled ventilation while identifying object location and surrounding edema.","Secure the object with appropriate forceps and withdraw bronchoscope/object together when necessary to prevent loss/migration.","Reinspect airway for second fragments, trauma and residual obstruction."],
  ["Complete obstruction","Object migration","Airway edema","Pneumothorax/trauma"],[]),
 "esophageal-fb":("Esophageal Foreign-Body Endoscopy","General ENT / Pediatrics",
  ["Identify object type, level, time since ingestion and signs of perforation/airway compromise.","Escalate batteries, sharp objects and complete obstruction urgently/emergently.","Use rigid/flexible endoscopy according to age/object/expertise; protect airway and remove without pushing hazardous material distally.","Inspect mucosa and determine observation/imaging/diet pathway from injury severity."],
  ["Perforation","Mediastinitis","Airway compromise","Object migration"],[]),
 "button-battery":("Esophageal Button-Battery Emergency","Pediatric / Emergency ENT",
  ["Recognize esophageal button battery as an emergency even when the child initially appears well.","Confirm location rapidly with appropriate radiographs without delaying definitive removal.","Mobilize immediate endoscopic removal and assess depth of tissue injury/adjacent vascular risk afterward.","Plan post-removal imaging/observation and multidisciplinary care according to injury severity and proximity to major vessels."],
  ["Aortoesophageal fistula","Perforation","Tracheoesophageal fistula","Delayed hemorrhage"],[]),
}
for _slug,(_title,_domain,_steps,_danger,_urls) in OR_GAP_CLOSURE_V91.items():
    if _slug not in OR_PREP_REGISTRY:
        OR_PREP_REGISTRY[_slug]={
          "slug":_slug,"title":_title,"domain":_domain,
          "indications":"Use when the disease-specific indication is established and the anatomy, alternatives, functional goals, and rescue plan have been reviewed.",
          "steps":_steps,"danger":_danger,
          "source_urls":_urls,
          "attending_followup":[
            ["What determines whether this is the right operation?","The operation should solve a defined anatomic/physiologic/oncologic problem and offer a better risk-benefit tradeoff than observation, medical therapy, or another procedure."],
            ["What are the danger structures?","Name the procedure-specific structures above and state how the exposure, dissection plane, or fixation vector keeps them safe."],
            ["What is the rescue plan?","Know what finding should make you stop, how you would regain airway/hemostasis/anatomic orientation, and which complication requires urgent reoperation or specialty help."]
          ],
          "linked_topic":_slug,"status":"audited-v9.1"
        }

# Rebuild adaptive items after the FPRS depth additions.
ADAPTIVE_ITEMS_V91=[]
for _domain,_mods in DEEP_MODULES_V6.items():
    for _m in _mods:
        _id=_v6_item_id(_domain,_m["topic"])
        for _stage in ["recognize","localize","workup","manage","operate","teach"]:
            ADAPTIVE_ITEMS_V91.append({
              "id":_id+"-"+_stage,"concept_id":_id,"domain":_domain,"topic":_m["topic"],"stage":_stage,
              "prompt":{
               "recognize":"Recognize the pattern and dangerous alternative.",
               "localize":"Localize anatomically and physiologically.",
               "workup":"Choose and interpret the workup that changes management.",
               "manage":"Build treatment, escalation and follow-up.",
               "operate":"Give indication, setup, landmarks, danger structures, steps, complications/rescue and postop plan.",
               "teach":"Teach the mental model and board/attending pearl."
              }[_stage],
              "answer":_m[_stage],
              "minutes":{"recognize":3,"localize":3,"workup":4,"manage":4,"operate":6,"teach":4}[_stage],
              "level":{"recognize":1,"localize":2,"workup":3,"manage":4,"operate":5,"teach":6}[_stage]
            })


# =============================================================================
# ENT Mastery v9.2 — Production cleanup source layer + full-site search
# =============================================================================
NCCN_GUIDELINES_V92 = [
 {"name":"NCCN Guidelines — Head and Neck Cancers","version":"2.2026","date":"May 12, 2026","role":"Current oncology management, staging-linked treatment, adjuvant and surveillance cross-check","access":"Uploaded private reference; do not reproduce NCCN algorithms/figures"},
 {"name":"NCCN Guidelines — Melanoma: Cutaneous","version":"2.2026","date":"April 17, 2026","role":"Current melanoma workup, treatment and surveillance cross-check","access":"Uploaded private reference; do not reproduce NCCN algorithms/figures"},
 {"name":"NCCN Guidelines — Squamous Cell Skin Cancer","version":"2.2026","date":"March 17, 2026","role":"Current cutaneous SCC risk, treatment and surveillance cross-check","access":"Uploaded private reference; do not reproduce NCCN algorithms/figures"},
 {"name":"NCCN Guidelines — Basal Cell Skin Cancer","version":"2.2026","date":"March 11, 2026","role":"Current BCC risk, treatment and surveillance cross-check","access":"Uploaded private reference; do not reproduce NCCN algorithms/figures"},
]
SITE_SOURCES_V92 = [
 {"name":"Current society guidelines / consensus statements","role":"Primary layer for management recommendations that can change over time."},
 {"name":"NCCN oncology guidelines (2026 uploaded set)","role":"Current cancer-management cross-check for head & neck cancer, melanoma, cutaneous SCC, and BCC. Algorithms are referenced, not reproduced."},
 {"name":"Core ENT reference texts","role":"Anatomy, physiology, differential diagnosis, pathology, and durable clinical foundations."},
 {"name":"Operative otolaryngology references","role":"Preoperative planning, surgical landmarks, danger structures, technique frameworks, complications, and postoperative reasoning."},
 {"name":"AO Surgery Reference — CMF Trauma","role":"Facial-trauma classification, biomechanics, indications, reduction/fixation strategy, and complication framework."},
 {"name":"thePlasticsFella","role":"Open educational FPRS synthesis for rhinoplasty mechanics, local flaps, grafting, and facial reanimation."},
 {"name":"Color Atlas of Otoscopy","role":"Otoscopy pattern recognition and anatomic correlation; older management statements are cross-checked against current guidance."},
 {"name":"Open interpretation resources","role":"ACR TI-RADS, Open Anatomy, Iowa protocols, pathology/stroboscopy resources, and other permitted external atlases used as linked visual references."},
]
if not any("NCCN" in e.get("examples","") for e in EVIDENCE_HIERARCHY_V6):
    EVIDENCE_HIERARCHY_V6.insert(0,{
      "tier":"Current oncology guidance",
      "use":"Cancer management, adjuvant therapy, surveillance, and systemic-treatment cross-checks.",
      "examples":"NCCN 2026 uploaded references: Head and Neck Cancers, Cutaneous Melanoma, Squamous Cell Skin Cancer, and Basal Cell Skin Cancer. Algorithms/figures are not reproduced."
    })

def _search_blob(*parts):
    return " ".join(str(p) for p in parts if p)

def search_index():
    from urllib.parse import quote_plus
    rows=[]
    rows.append({"type":"Topic","title":PARATHYROID["title"],"subtitle":PARATHYROID["subtitle"],"url":"/topic/parathyroid-disease","text":_search_blob(PARATHYROID.get("tags",[]),PARATHYROID.get("subtitle",""))})
    for s in PARATHYROID.get("sections",[]):
        rows.append({"type":"Lesson","title":s["title"],"subtitle":PARATHYROID["title"],"url":f"/topic/parathyroid-disease#{s['id']}","text":_search_blob(s["title"],s.get("content",[]))})
    for op in OPERATIONS:
        rows.append({"type":"Operation","title":op["title"],"subtitle":"Operative Mastery","url":f"/operate/{op['slug']}","text":_search_blob(op["title"],op.get("indications",""),op.get("steps",[]))})
    for a in ANATOMY:
        rows.append({"type":"Anatomy","title":a["title"],"subtitle":a["region"],"url":f"/anatomy#{a['slug']}","text":_search_blob(a["title"],a.get("points",[]))})
    for c in CASES:
        rows.append({"type":"Case","title":c["title"],"subtitle":c["summary"],"url":f"/case/{c['id']}","text":_search_blob(c["title"],c["summary"],[(x.get("q"),x.get("a")) for x in c.get("steps",[])])})
    for c in COMPLICATIONS:
        rows.append({"type":"Complication","title":c["title"],"subtitle":c["prompt"],"url":f"/complications#{c['slug']}","text":_search_blob(c["title"],c["prompt"],c.get("framework",[]))})
    for domain,mods in DEEP_MODULES_V6.items():
        for m in mods:
            rows.append({"type":"Deep curriculum","title":m["topic"],"subtitle":domain,"url":"/curriculum/depth","text":_search_blob(domain,m["topic"],m.get("recognize"),m.get("localize"),m.get("workup"),m.get("manage"),m.get("operate"),m.get("teach"))})
    for c in INTEGRATED_CASES:
        st=[]
        for s in c.get("stages",[]):
            st += [s.get("title",""),s.get("stimulus",""),s.get("question",""),s.get("answer",""),s.get("why","")]
        rows.append({"type":"Integrated case","title":c["title"],"subtitle":c.get("domain","Integrated ENT"),"url":f"/integrated/{c['id']}","text":_search_blob(c.get("summary",""),c.get("source_basis",[]),st)})
    for slug,lab in INTERPRETATION_LABS.items():
        rows.append({"type":"Interpretation lab","title":lab.get("title",slug),"subtitle":lab.get("subtitle","Interpretation Atlas"),"url":f"/lab/{slug}","text":_search_blob(lab.get("framework",[]),lab.get("source_note",""))})
        seen=set()
        for c in lab.get("cases",[]):
            concept=c.get("concept_id") or c.get("id")
            if concept in seen: continue
            seen.add(concept)
            rows.append({"type":"Interpretation case","title":c.get("prompt","Interpretation case")[:120],"subtitle":lab.get("title",slug),"url":f"/lab/{slug}?mode=all","text":_search_blob(c.get("prompt"),c.get("answer"),c.get("why"),c.get("follow"),c.get("follow_answer"))})
    rows.append({"type":"Interpretation lab","title":"Otoscopy Atlas","subtitle":"Otology / Otoscopy","url":"/lab/otoscopy","text":"otoscopy tympanic membrane ear canal middle ear visual diagnosis"})
    for c in OTOSCOPY_CASES:
        rows.append({"type":"Otoscopy case","title":c.get("diagnosis",c.get("prompt","Otoscopy")),"subtitle":"Otoscopy Atlas","url":"/lab/otoscopy","text":_search_blob(c.get("prompt"),c.get("findings",[]),c.get("differential"),c.get("management"),c.get("management_considerations"),c.get("pearl"))})
    for slug,op in OR_PREP_REGISTRY.items():
        rows.append({"type":"OR Tomorrow","title":op["title"],"subtitle":op.get("domain","Operative prep"),"url":"/case-tomorrow?q="+quote_plus(op["title"]),"text":_search_blob(op.get("indications"),op.get("steps",[]),op.get("danger",[]),op.get("attending_followup",[]))})
    for src in NCCN_GUIDELINES_V92:
        rows.append({"type":"Evidence","title":src["name"]+" "+src["version"],"subtitle":"Uploaded current oncology guideline","url":"/evidence","text":_search_blob(src["role"],src["date"],src["access"])})
    return rows


# =============================================================================
# ENT Mastery v9.4 — learner integration / canonical taxonomy
# =============================================================================

CANONICAL_DOMAINS_V94 = [
 "Otology / Neurotology",
 "Rhinology / Allergy / Skull Base",
 "Head & Neck Oncology",
 "Thyroid / Parathyroid / Salivary",
 "Pediatric Otolaryngology",
 "Laryngology / Voice / Swallowing",
 "Facial Plastics / Trauma",
 "Sleep Surgery",
 "General ENT / Emergencies",
]

def canonical_domain_v94(label):
    s=(label or "").lower()
    if any(k in s for k in ["thyroid","parathyroid","salivary","parotid","submandibular"]):
        return "Thyroid / Parathyroid / Salivary"
    if any(k in s for k in ["pediatric","aom","ome","cleft","choanal","microtia"]):
        return "Pediatric Otolaryngology"
    if any(k in s for k in ["rhin","sinus","fess","skull base"]) and not any(k in s for k in ["otology","temporal","vestibular"]):
        return "Rhinology / Allergy / Skull Base"
    if any(k in s for k in ["sleep","osa","hns","hypoglossal"]):
        return "Sleep Surgery"
    if any(k in s for k in ["laryng","voice","swallow","airway"]) and "pediatric" not in s:
        return "Laryngology / Voice / Swallowing"
    if any(k in s for k in ["facial plastics","trauma","reconstruction","rhinoplasty","flap"]):
        return "Facial Plastics / Trauma"
    if any(k in s for k in ["head & neck","oncology","pathology","oral","orophary","laryngeal cancer"]):
        return "Head & Neck Oncology"
    if any(k in s for k in ["otology","audiology","vestib","hearing","temporal"]):
        return "Otology / Neurotology"
    if any(k in s for k in ["general ent","emergency","caustic","foreign body","deep neck"]):
        return "General ENT / Emergencies"
    return label if label in CANONICAL_DOMAINS_V94 else "General ENT / Emergencies"

def _tags_v94(*parts):
    import re as _re
    stop={"and","the","of","to","for","with","after","before","in","a","an","or","vs","from"}
    toks=[]
    for p in parts:
        toks.extend(_re.findall(r"[a-z0-9]+",(p or "").lower()))
    return sorted({t for t in toks if len(t)>2 and t not in stop})

# Normalize the case library without throwing away the useful display labels.
for _c in INTEGRATED_CASES:
    _c["display_domain"]=_c.get("domain","ENT")
    _c["primary_domain"]=canonical_domain_v94(_c.get("domain"))
    _c["domain"]=_c["primary_domain"]
    _c["tags"]=_tags_v94(_c.get("title"),_c.get("summary")," ".join(
        x.get("title","")+" "+x.get("question","") for x in _c.get("stages",[])
    ))

# Every attending prompt now says what competency it is actually testing.
def _attending_dimension_v94(p):
    q=(p.get("prompt","")+" "+p.get("answer","")).lower()
    if any(k in q for k in ["operate","operation","surgery","dissection","approach","nerve at risk",
                              "danger","complication","resection","incision","graft","drill","instrument"]):
        return "operative"
    if any(k in q for k in ["workup","test","imaging","ct","mri","ultrasound","psg","audiogram",
                              "biopsy","lab","evaluation","diagnos"]):
        return "workup"
    if any(k in q for k in ["manage","management","treat","therapy","antibiotic","steroid","observe",
                              "follow-up","surveillance","next step"]):
        return "management"
    if any(k in q for k in ["where","localize","space","anatom","landmark","level","nerve","muscle"]):
        return "localization"
    if any(k in q for k in ["teach","explain to","why does","why is","mechanism","physiology"]):
        return "teaching"
    return "reasoning"

for _level,_prompts in ATTENDING_LEVEL_PROMPTS.items():
    for _p in _prompts:
        _p["domain"]=canonical_domain_v94(_p.get("domain"))
        _p["dimension"]=_attending_dimension_v94(_p)
        _p["tags"]=_tags_v94(_p.get("prompt"),_p.get("answer"))

# Make all six Daily Path layers genuinely distinct. We keep the original source-derived
# teaching statement and add a stage-specific clinical objective where v7-v9 duplicated it.
_STAGE_OBJECTIVES_V94 = {
 "recognize":"Recognition objective: name the pattern, the defining clue, and the dangerous look-alike if one is clinically relevant.",
 "localize":"Localization objective: state the involved structure, compartment, nerve, airway level, drainage pathway, or physiologic mechanism that explains the presentation.",
 "workup":"Evaluation objective: choose only tests or bedside assessments that confirm the localization, define severity, or change the next decision.",
 "manage":"Management objective: sequence observation/medical therapy, escalation, follow-up, and the trigger for procedural or multidisciplinary care.",
 "operate":"Advanced-decision objective: decide whether a procedure has a role. If it does, connect indication, anatomy, danger structures, complications, and rescue; if it does not, focus on refractory disease, complication management, or the next multidisciplinary decision.",
 "teach":"Teaching objective: explain the causal mental model, why the chosen workup/management is appropriate, and one mistake a junior should avoid."
}

DEEP_MODULES_V94={}
for _domain,_mods in DEEP_MODULES_V6.items():
    _out=[]
    for _m in _mods:
        _n=dict(_m)
        seen=set()
        for _stage in ["recognize","localize","workup","manage","operate","teach"]:
            txt=(_n.get(_stage) or "").strip()
            # If the original content is repeated or too generic, preserve it but explicitly
            # add the unique stage objective. This avoids fake new facts while making the
            # curriculum step educationally distinct.
            if txt in seen or len(txt)<55 or (_stage=="operate" and txt.startswith("State whether")):
                txt=(txt+" "+_STAGE_OBJECTIVES_V94[_stage]).strip()
            elif _stage in ("workup","manage","operate","teach"):
                txt=(txt+" "+_STAGE_OBJECTIVES_V94[_stage]).strip()
            # Guarantee uniqueness without adding unsupported medical claims.
            if txt in seen:
                txt=(txt+" "+_STAGE_OBJECTIVES_V94[_stage]).strip()
            _n[_stage]=txt
            seen.add(txt)
        _n["primary_domain"]=canonical_domain_v94(_domain)
        _n["tags"]=_tags_v94(_n.get("topic"),_domain)
        _out.append(_n)
    DEEP_MODULES_V94[_domain]=_out

# Keep the existing public name pointing at the normalized/de-duplicated modules so
# Deep Curriculum, Concept Hub and search all agree.
DEEP_MODULES_V6=DEEP_MODULES_V94

ADAPTIVE_ITEMS_V94=[]
for _domain,_mods in DEEP_MODULES_V94.items():
    for _m in _mods:
        _id=_v6_item_id(_domain,_m["topic"])
        for _stage in ["recognize","localize","workup","manage","operate","teach"]:
            ADAPTIVE_ITEMS_V94.append({
              "id":_id+"-"+_stage,"concept_id":_id,"domain":_domain,"topic":_m["topic"],
              "stage":_stage,
              "display_stage":"advanced" if _stage=="operate" else _stage,
              "prompt":{
                "recognize":"Recognize the pattern.",
                "localize":"Localize the problem.",
                "workup":"Evaluate it efficiently.",
                "manage":"Build the management sequence.",
                "operate":"Make the advanced decision.",
                "teach":"Teach the mental model."
              }[_stage],
              "answer":_m[_stage],
              "minutes":{"recognize":3,"localize":3,"workup":4,"manage":4,"operate":6,"teach":4}[_stage],
              "level":{"recognize":1,"localize":2,"workup":3,"manage":4,"operate":5,"teach":6}[_stage],
              "tags":_m.get("tags",[])
            })

# Alias used by older imports/routes.
ADAPTIVE_ITEMS_V91=ADAPTIVE_ITEMS_V94


# =============================================================================
# ENT Mastery v9.5 — Evidence-Calibrated Depth Pass
# Public-source calibrated. No restricted guideline text is embedded.
# =============================================================================

EVIDENCE_UPDATES_V95 = {
 "Sudden Sensorineural Hearing Loss": {
   "recognize":"Treat a sudden unilateral sensorineural change as time-sensitive even when the patient describes fullness or a blocked ear. First distinguish SNHL from conductive loss and look for bilateral, recurrent, focal-neurologic or other atypical features.",
   "localize":"Use otoscopy plus bedside tuning forks and prompt audiometry to separate external/middle-ear conductive disease from cochlear or retrocochlear sensorineural loss; focal neurologic findings broaden localization beyond the cochlea.",
   "workup":"Obtain audiometry as soon as possible and within 14 days of onset to document SSNHL. Evaluate for retrocochlear pathology with MRI or ABR as appropriate; do not routinely order head CT or indiscriminate laboratory panels for otherwise typical idiopathic SSNHL.",
   "manage":"Counsel about natural history and treatment uncertainty. Corticosteroids may be offered as initial therapy within 2 weeks. HBOT with steroids may be offered within 2 weeks initially or within 1 month as salvage. Offer intratympanic steroid salvage for incomplete recovery 2–6 weeks after onset. Do not routinely prescribe antivirals, thrombolytics, vasodilators or vasoactive drugs.",
   "operate":"This is not primarily an operative disorder. The procedural decision is intratympanic steroid delivery for appropriate salvage treatment; discuss TM anesthesia/access, transient vertigo, otalgia and perforation risk while avoiding delay in the treatment window.",
   "teach":"The board/clinical pearl is timing: recognize SNHL early, document it with audiometry, avoid low-yield shotgun testing, and know the initial-versus-salvage treatment windows. Recheck hearing at treatment completion and within 6 months; address residual hearing loss/tinnitus with rehabilitation."
 },
 "Tympanostomy Tube Indications": {
   "recognize":"Separate AOM (acute inflammatory/infectious syndrome) from OME (middle-ear effusion without acute infection). Tube candidacy depends on current effusion, chronicity, hearing/symptom burden, developmental risk and recurrent-AOM phenotype—not infection count alone.",
   "localize":"The target problem is persistent or recurrent middle-ear ventilation failure behind an intact TM. Pneumatic otoscopy/tympanometry establish effusion; the functional consequence is usually conductive hearing loss, but at-risk children may experience disproportionate speech/language or learning impact.",
   "workup":"Do not place tubes for a single OME episode lasting <3 months. Obtain a hearing evaluation when OME persists ≥3 months or before surgery when the child becomes a tube candidate. Identify children at increased developmental risk and determine whether effusion is likely to persist.",
   "manage":"Offer bilateral tubes for bilateral OME ≥3 months with documented hearing difficulty; tubes may also be considered for chronic OME with attributable symptoms. For recurrent AOM, do not place tubes when no middle-ear effusion is present at candidacy assessment; offer bilateral tubes when recurrent AOM is accompanied by unilateral or bilateral effusion.",
   "operate":"Before myringotomy, confirm indication, laterality and current ear status. Make a controlled incision in a safe TM quadrant, avoid annulus/ossicles, evacuate fluid when present and seat the tube. For uncomplicated acute tube otorrhea, topical antibiotic drops are preferred to routine oral antibiotics.",
   "teach":"Ask three questions before recommending tubes: Is fluid present now? How long has it persisted? What functional/developmental risk does it create? That prevents the common error of treating recurrent AOM as a pure infection-count rule."
 },
 "AOM / OME / Tympanostomy Decisions": {
   "recognize":"AOM requires an acute inflammatory middle-ear syndrome; OME is effusion without acute infection. Recurrent AOM, chronic OME and at-risk-child pathways overlap but are not interchangeable.",
   "localize":"Eustachian-tube dysfunction alters middle-ear pressure and ventilation, producing effusion and conductive hearing effects. The exam should localize disease to the middle ear rather than assuming every ear complaint is infection.",
   "workup":"Use pneumatic otoscopy and tympanometry when needed to establish effusion. For OME persisting ≥3 months, obtain age-appropriate hearing testing; assess speech/language, school performance and developmental risk when clinically relevant.",
   "manage":"Most transient OME is observed. Treat AOM according to age/severity and diagnostic certainty. Consider tubes only for guideline-supported chronic OME or recurrent-AOM phenotypes, with special attention to children at increased developmental risk.",
   "operate":"Tube placement treats middle-ear ventilation, not the child's tendency to acquire every URI. Confirm a present indication, use safe TM anatomy, and counsel regarding otorrhea, extrusion, persistent perforation and follow-up.",
   "teach":"A useful mental model is disease state → duration → hearing/function → risk. Infection count matters, but the current ear examination and functional consequence determine whether ventilation tubes are likely to help."
 },
 "Recurrent Tonsillitis Decision-Making": {
   "recognize":"Confirm that reported 'strep' or sore-throat episodes were true qualifying tonsillitis episodes. Frequency alone is insufficient without severity features and documentation.",
   "localize":"This is recurrent tonsillar/oropharyngeal inflammatory disease; distinguish it from chronic throat symptoms, reflux, viral URI burden, PFAPA and peritonsillar infection.",
   "workup":"Reconstruct the documented episode history. A guideline-supported episode includes sore throat plus qualifying findings such as fever >38.3°C, cervical adenopathy, tonsillar exudate or positive group-A streptococcal testing. PSG is not a recurrent-infection test.",
   "manage":"Below the usual thresholds, favor watchful waiting: fewer than 7 episodes in 1 year, fewer than 5/year for 2 years, or fewer than 3/year for 3 years. Tonsillectomy may be offered when ≥7 in 1 year, ≥5/year for 2 years, or ≥3/year for 3 years are documented with qualifying features. Consider modifying factors such as PFAPA, multiple antibiotic intolerance/allergy or >1 peritonsillar abscess.",
   "operate":"When surgery is chosen, the advanced decision includes expected benefit versus postoperative pain, dehydration and hemorrhage risk, plus perioperative OSA/comorbidity considerations when relevant. The indication must survive chart review before the operation starts.",
   "teach":"The classic error is equating 'seven sore throats' with seven qualifying episodes. Teach the 7/5/3 framework, documentation requirements, and the modifying factors that can change a watchful-waiting recommendation."
 },
 "Differentiated Thyroid Cancer": {
   "recognize":"Differentiate papillary, follicular and oncocytic differentiated thyroid cancers from medullary/anaplastic disease. Most DTC has favorable survival, but local invasion, nodal/distant disease, aggressive pathology and molecular features change recurrence risk and treatment.",
   "localize":"Map the primary tumor to one or both lobes, assess gross extrathyroidal extension, and define central/lateral nodal disease. Contralateral nodules, RLN/tracheoesophageal involvement and distant disease can change the initial surgical strategy.",
   "workup":"Use high-quality thyroid/neck ultrasound with nodal mapping, cytology/pathology and selective cross-sectional imaging for invasive/bulky disease. Incorporate contemporary risk assessment and patient factors; small low-risk cancers may be candidates for active surveillance rather than immediate surgery in selected settings.",
   "manage":"Under 2025 ATA guidance, a cancer confined to one lobe ≤2 cm without extrathyroidal extension or nodal disease should generally be treated with lobectomy when surgery is chosen. For >2 to ≤4 cm similarly confined disease, lobectomy or total thyroidectomy may be appropriate based on tumor features, contralateral nodules and patient preference. Tumors >4 cm, gross extrathyroidal extension, clinically significant nodal disease or distant metastasis generally favor total thyroidectomy with appropriate therapeutic nodal surgery.",
   "operate":"Match extent to disease rather than treating the word 'cancer' as an automatic total thyroidectomy. Preserve RLN/EBSLN and viable parathyroids while obtaining oncologic clearance. Therapeutic compartment-oriented nodal dissection is performed for clinically involved nodal disease; completion thyroidectomy after initial lobectomy is individualized rather than automatic.",
   "teach":"The 2025 shift is de-escalation with structure: selected small unilateral low-risk DTC → lobectomy; 2–4 cm low-risk unilateral disease → shared decision between lobectomy and total; advanced local/nodal/distant disease → broader surgery. Then separately decide whether RAI, TSH goals and surveillance intensity are justified by postoperative risk and response."
 },
 "Hypoglossal Nerve Stimulation": {
   "recognize":"HNS is an alternative pathway for selected obstructive-sleep-apnea patients who cannot obtain adequate benefit from PAP, not a first-line replacement for PAP in every patient.",
   "localize":"The implant recruits protrusor tongue function through selected hypoglossal branches while a respiratory sensor synchronizes stimulation with breathing. DISE is used to characterize collapse because complete concentric palatal collapse predicts poor candidacy for the classic unilateral system.",
   "workup":"Confirm obstructive rather than predominantly central sleep apnea, current PSG severity, PAP failure/intolerance, anatomy and DISE pattern. Current FDA-expanded adult labeling for Inspire includes AHI up to 100 and extends the BMI warning boundary to 40; payer and local-program criteria may be narrower, so distinguish FDA labeling from coverage criteria.",
   "manage":"Selection is only the start: implantation is followed by healing, activation, programming/titration and objective longitudinal outcome assessment. Continue weight, positional and other OSA management when relevant rather than treating the device as an isolated cure.",
   "operate":"Understand inclusion versus exclusion hypoglossal branches, cuff positioning, respiratory-sensor placement and generator routing. Protect hypoglossal/lingual structures and pleura; anticipate infection, tongue weakness/discomfort, stimulation intolerance, pneumothorax and revision/device issues.",
   "teach":"Teach HNS as a five-step pathway: phenotype → PAP history → PSG/DISE selection → implantation → programming/outcomes. Quote current device labeling with its year and remind learners that payer thresholds may be more restrictive."
 },
}

# Curated high-yield new deep modules identified by the v9.4 audit.
NEW_DEEP_MODULES_V95 = {
 "Otology / Neurotology":[
  {"topic":"Age-Related Hearing Loss / Presbycusis",
   "recognize":"Progressive bilateral hearing difficulty—often speech-in-noise first—in an older adult should trigger formal hearing evaluation rather than being dismissed as normal aging.",
   "localize":"Usually bilateral sensorineural dysfunction from age-related cochlear/neural changes; asymmetry, conductive findings, sudden change or focal neurologic symptoms require a different localization pathway.",
   "workup":"Perform otoscopy and audiologic evaluation. Ask about communication goals, tinnitus, falls/cognition and functional impact; pursue additional workup when asymmetry or other atypical findings suggest a non-age-related cause.",
   "manage":"Counsel on communication strategies and hearing-assistive technology; offer or refer for hearing aids when appropriate. Reassess benefit and escalate to cochlear-implant evaluation when appropriately fitted amplification does not provide adequate speech understanding.",
   "operate":"The advanced procedural decision is not routine ear surgery; it is recognizing when severe functional hearing loss warrants implant evaluation and when asymmetric or conductive disease needs a different diagnostic pathway.",
   "teach":"Do not normalize disability because of age. The goal is function: identify hearing loss, treat remediable causes, provide amplification/assistive strategies and recognize when hearing aids are no longer enough."},
  {"topic":"Acute Mastoiditis / Petrous Apicitis",
   "recognize":"Postauricular erythema/swelling, auricular protrusion, persistent fever/otalgia or toxic appearance after AOM suggests mastoid complication; deep facial pain or cranial neuropathy raises concern for petrous apical extension.",
   "localize":"Infection spreads from the middle ear into mastoid air cells; subperiosteal, intracranial, venous-sinus and petrous-apex pathways determine complications.",
   "workup":"Assess ear and neurologic status, obtain cultures when drainage is available, and use contrast CT and/or MRI when complication, abscess, intracranial extension or atypical course is suspected.",
   "manage":"Admit complicated disease, start appropriate IV antibiotics, obtain source control and monitor for intracranial/venous complications. Myringotomy/tube and mastoid surgery depend on abscess, coalescence, complications and response.",
   "operate":"Drain pus and restore ventilation while protecting facial nerve, labyrinth, sigmoid sinus, tegmen and ossicles. Complicated or nonresponding disease requires a deliberate source-control plan rather than repeated antibiotics alone.",
   "teach":"Mastoiditis is not simply 'bad otitis media.' The resident question is always: uncomplicated inflammation, coalescent bone disease, subperiosteal abscess, or intracranial/petrous complication?"}
 ],
 "Rhinology / Allergy / Skull Base":[
  {"topic":"Nonallergic Rhinitis / Rhinitis Medicamentosa",
   "recognize":"Chronic congestion/rhinorrhea without a convincing IgE-mediated pattern suggests nonallergic rhinitis; escalating topical decongestant use with rebound obstruction suggests rhinitis medicamentosa.",
   "localize":"Symptoms arise from dysregulated nasal mucosal vascular/glandular responses rather than allergen-specific inflammation alone; medication rebound perpetuates turbinate congestion.",
   "workup":"Use history, nasal examination/endoscopy when indicated and targeted allergy testing only when the phenotype is uncertain or results would change management. Look for structural obstruction, CRS and medication triggers.",
   "manage":"Remove triggers, use saline and phenotype-directed intranasal therapy; stop the offending topical decongestant in rhinitis medicamentosa and support withdrawal with anti-inflammatory therapy as appropriate.",
   "operate":"Surgery is not first-line for a primarily inflammatory/medication-driven disorder. Consider turbinate or structural procedures only after the inflammatory phenotype and medication dependence are addressed and fixed obstruction remains.",
   "teach":"Not every chronically congested patient has allergy or sinusitis. Ask what triggers symptoms and exactly what sprays the patient is using before ordering more tests or scheduling surgery."},
  {"topic":"Unilateral Sinonasal Disease",
   "recognize":"Unilateral obstruction, bleeding, unilateral polyposis, facial numbness, orbital symptoms or unilateral sinus opacification deserves a different differential than routine bilateral inflammatory CRS.",
   "localize":"Localize to nasal cavity versus specific sinus, then assess orbit, skull base, pterygopalatine/infratemporal spaces and dental origin based on symptoms and imaging.",
   "workup":"Perform endoscopy and review dedicated CT; add contrast MRI when tumor, skull-base/orbital extension, perineural spread or indeterminate soft tissue is a concern. Biopsy suspicious accessible lesions when safe, avoiding blind biopsy of potentially vascular or skull-base lesions.",
   "manage":"Treat the cause: odontogenic/inflammatory disease, fungal disease, benign neoplasm or malignancy each requires a different pathway. Red flags should accelerate tissue diagnosis and multidisciplinary planning.",
   "operate":"Before endoscopic surgery, know whether the lesion could be vascular, encephalocele/CSF-related or malignant. The advanced decision is often choosing biopsy versus definitive resection and defining the safe surgical corridor.",
   "teach":"Unilateral disease is a diagnostic category, not a diagnosis. The board pearl is to resist labeling unilateral polyps/opacification as ordinary CRS until neoplasm, odontogenic disease and skull-base pathology are considered."}
 ],
 "Laryngology / Voice / Swallowing":[
  {"topic":"Inducible Laryngeal Obstruction / PVFM",
   "recognize":"Episodic inspiratory dyspnea/stridor, throat tightness or exercise symptoms with poor response to asthma therapy should raise inducible laryngeal obstruction.",
   "localize":"Paradoxical or inappropriate laryngeal narrowing occurs at the glottic and/or supraglottic level during symptoms rather than fixed subglottic or pulmonary obstruction.",
   "workup":"History and flexible laryngoscopy are central; provocation/exercise laryngoscopy may be needed when the resting exam is normal. Evaluate asthma and other mimics rather than assuming they are mutually exclusive.",
   "manage":"Education, trigger control and respiratory retraining with speech-language pathology are foundational. Treat relevant comorbid airway/reflux/nasal contributors without reflexive escalation of asthma medication.",
   "operate":"There is usually no operative role. Advanced management is recognizing refractory phenotype, confirming the diagnosis during symptoms and avoiding unnecessary intubation/tracheostomy or airway surgery for a functional episodic disorder.",
   "teach":"The key distinction is episodic dynamic laryngeal closure versus fixed obstruction. If the patient sounds obstructed but the story and pulmonary response do not fit asthma, visualize the larynx during the event."},
  {"topic":"Chronic Cough / Laryngeal Hypersensitivity",
   "recognize":"Chronic cough can persist after common pulmonary, sinonasal and reflux causes are addressed; throat tickle, talking/laughing triggers and sensory symptoms can suggest cough hypersensitivity.",
   "localize":"The phenotype reflects an exaggerated laryngeal/cough reflex network rather than a single visible lesion; coexisting rhinitis, asthma, reflux or medication effects may still contribute.",
   "workup":"Exclude red flags and common causes with targeted history/exam and appropriate pulmonary/sinonasal/laryngeal evaluation. Avoid endless empiric treatment when the phenotype and prior response no longer support it.",
   "manage":"Treat identified contributors and use behavioral cough-suppression/voice therapy for hypersensitivity phenotypes; selected refractory cases may warrant neuromodulatory or multidisciplinary management.",
   "operate":"Surgery is generally not the treatment. The advanced decision is recognizing when a structural laryngeal lesion, aspiration or airway disorder—not hypersensitivity—requires a procedural pathway.",
   "teach":"Chronic cough is a syndrome. Once dangerous and common causes are addressed, repeated empiric antibiotics or reflux therapy without evidence can become part of the problem rather than the solution."}
 ],
 "Sleep Surgery":[
  {"topic":"Palatal Surgery Selection for OSA",
   "recognize":"Palatal obstruction is one component of a multilevel OSA phenotype; tonsil size, lateral-wall collapse and palate configuration matter more than simply labeling a patient 'snorer.'",
   "localize":"Use awake exam plus DISE when appropriate to distinguish anteroposterior palatal collapse, lateral-wall contribution and multilevel tongue-base/epiglottic obstruction.",
   "workup":"Confirm OSA severity and PAP history, assess BMI/comorbidity, tonsils, palate and nasal airway, and use DISE when it will change procedure selection or HNS candidacy.",
   "manage":"Select surgery for the patient's collapse pattern and goals rather than defaulting every patient to classic UPPP. Counsel that surgery may improve rather than normalize AHI and that residual OSA requires reassessment.",
   "operate":"Know the conceptual differences between tissue-resection and reconstructive/lateral-wall techniques. Preserve velopharyngeal function, control hemorrhage and plan postoperative airway/pain monitoring.",
   "teach":"Sleep surgery is phenotype surgery: PSG tells you severity; anatomy/DISE tell you where and how the airway collapses; the operation should match that pattern."},
  {"topic":"Lingual Tonsil / Tongue-Base Obstruction",
   "recognize":"Persistent OSA after adenotonsillectomy or adult multilevel OSA may include lingual-tonsil or tongue-base obstruction, especially when awake tonsil size does not explain severity.",
   "localize":"Obstruction can arise from lymphoid tissue, tongue-base bulk or dynamic posterior displacement; distinguish this from epiglottic and palatal collapse.",
   "workup":"Use PSG for severity and flexible examination/DISE to define the obstructing level. In children, consider syndromic/craniofacial and obesity-related contributors.",
   "manage":"Address weight/PAP and other levels as appropriate; consider lingual-tonsil reduction or other tongue-base therapy when the phenotype is clearly localized and expected benefit outweighs dysphagia/bleeding risk.",
   "operate":"Protect lingual artery and tongue-base neurovascular structures, obtain hemostasis and anticipate edema, pain and swallowing effects. The operation should target the demonstrated obstructing tissue rather than a presumed level.",
   "teach":"Residual OSA is often multilevel. A normal-looking oral tonsillar fossa after adenotonsillectomy does not exclude substantial tongue-base or lingual-tonsil obstruction."}
 ],
 "Facial Plastics / Trauma":[
  {"topic":"Septal Perforation",
   "recognize":"Crusting, epistaxis, whistling and obstruction with a visible septal defect suggest perforation; symptoms depend on size and location and may be absent.",
   "localize":"Anterior perforations disrupt laminar nasal airflow and humidification most noticeably. Etiology may be iatrogenic, traumatic, inflammatory/autoimmune, infectious, neoplastic or drug-related.",
   "workup":"Document size/location and remaining mucosa/support. Investigate systemic/infectious/neoplastic causes when history or exam is atypical rather than assuming every perforation is postoperative.",
   "manage":"Humidification, saline, emollient care and avoidance of trauma are first-line; septal buttons help selected symptomatic patients. Repair is individualized to symptoms, size, tissue quality, etiology and available vascularized mucosa.",
   "operate":"Successful closure generally requires tension-free vascularized mucosal coverage, often with an interposition graft, while preserving remaining L-strut/support. Active destructive disease and poor tissue quality predict failure.",
   "teach":"Treat the patient and cause, not the hole. An asymptomatic stable perforation may need no repair; a symptomatic perforation with uncontrolled inflammatory disease is a poor surgical target."},
  {"topic":"Facial Synkinesis / Static-Dynamic Rehabilitation",
   "recognize":"After facial nerve injury, involuntary eye closure with smiling, oral commissure movement with blinking, tightness or asymmetric resting tone suggests synkinetic reinnervation rather than simple flaccid paralysis.",
   "localize":"Aberrant axonal regeneration and maladaptive neuromuscular recruitment create coupled movements; distinguish this from persistent complete denervation because treatment goals differ.",
   "workup":"Document duration, etiology, branch-specific movement, ocular protection, smile/oral competence and patient priorities. Electrodiagnostics and imaging are selective based on cause and timing.",
   "manage":"Neuromuscular retraining and targeted botulinum toxin are core treatments for synkinesis; static procedures address protection/symmetry, while nerve/muscle transfer strategies depend on denervation duration and available donor function.",
   "operate":"Choose static versus dynamic reconstruction based on time from injury, viable motor endplates, proximal nerve availability and goals. Protect the eye first; do not apply a one-operation algorithm to every facial paralysis patient.",
   "teach":"Flaccid paralysis and synkinesis are different phases/problems. The treatment question is not simply 'How weak is the face?' but what viable nerve/muscle exists and what functional deficit matters most."}
 ],
 "General ENT / Emergencies":[
  {"topic":"Carotid Blowout Syndrome",
   "recognize":"Sentinel bleeding from the mouth, pharynx, neck wound or stoma in a previously irradiated, infected, recurrent-cancer or fistula patient can precede catastrophic carotid hemorrhage.",
   "localize":"Risk involves exposed or threatened carotid system in a hostile neck; distinguish external carotid branch bleeding from common/internal carotid rupture while prioritizing airway and hemorrhage control.",
   "workup":"This is an emergency: resuscitate, activate ENT/anesthesia/interventional/vascular resources and obtain CTA only when the patient is sufficiently stable and imaging will not delay definitive control.",
   "manage":"Secure airway with a hemorrhage plan, obtain large-bore access/blood products and proceed to endovascular or operative control based on stability, anatomy and resources. Do not discharge a convincing sentinel bleed.",
   "operate":"Control may require packing/temporary pressure, endovascular embolization or covered stent, or surgical ligation in selected situations. Anticipate stroke, rebleeding, infection and airway contamination.",
   "teach":"A small 'sentinel' bleed in the irradiated neck is not reassuring—it may be the warning. The resident priority is airway + massive hemorrhage activation + definitive vascular control, not prolonged bedside diagnosis."},
  {"topic":"Esophageal Perforation / Cervical Mediastinitis",
   "recognize":"Neck/chest pain, fever, crepitus, dysphagia, tachycardia or sepsis after instrumentation, foreign body or trauma should trigger concern for esophageal perforation.",
   "localize":"Cervical leaks may track through deep neck spaces into the mediastinum; location, containment and contamination determine severity and access.",
   "workup":"Keep the patient NPO, obtain urgent contrast-enhanced cross-sectional imaging and use contrast esophagram/endoscopy selectively with the treating team. Evaluate for pleural/mediastinal contamination and sepsis.",
   "manage":"Begin IV broad-spectrum antimicrobial therapy, resuscitation and early multidisciplinary surgical/thoracic consultation. Selected contained cervical injuries may be managed nonoperatively with close monitoring; uncontrolled leak, sepsis, necrosis or collections require source control.",
   "operate":"Drain contaminated spaces, debride nonviable tissue and repair/divert as appropriate to location and tissue quality. Airway, recurrent laryngeal nerves and great vessels are central cervical hazards.",
   "teach":"Delay kills. The mental model is perforation → contamination → sepsis: define whether the leak is contained, whether source control is adequate, and whether infection is descending into the mediastinum."}
 ]
}

# Apply evidence updates to existing deep modules.
for _domain,_mods in DEEP_MODULES_V6.items():
    for _m in _mods:
        if _m.get("topic") in EVIDENCE_UPDATES_V95:
            _m.update(EVIDENCE_UPDATES_V95[_m["topic"]])
            _m["evidence_calibrated"]="v9.5"

# Add missing high-yield modules without duplicating titles.
_existing={m["topic"] for mods in DEEP_MODULES_V6.values() for m in mods}
for _domain,_mods in NEW_DEEP_MODULES_V95.items():
    for _m in _mods:
        if _m["topic"] not in _existing:
            _m["primary_domain"]=_domain
            _m["tags"]=_tags_v94(_m["topic"],_domain)
            _m["evidence_calibrated"]="v9.5"
            DEEP_MODULES_V6.setdefault(_domain,[]).append(_m)
            _existing.add(_m["topic"])

# OR Tomorrow: replace the generic indication/follow-up shell for the 30 remaining v8 modules.
OR_DEPTH_V95 = {
"ossiculoplasty":("Persistent conductive hearing loss from ossicular discontinuity/fixation after the middle ear is safe and the expected hearing benefit justifies reconstruction.",
 [["What predicts a better ossiculoplasty result?","A stable, aerated middle ear; intact/mobile stapes superstructure when possible; favorable malleus/TM support; and absence of active disease."],["PORP versus TORP?","PORP couples the TM/malleus to an intact stapes superstructure; TORP is used when the superstructure is absent and reconstruction must couple to the footplate."]]),
"canalplasty":("Symptomatic external auditory canal stenosis or obstructing exostoses causing conductive loss, recurrent trapping/infection, or inability to access the TM when conservative care is insufficient.",
 [["What is the major technical risk?","Injury to canal skin/TM, facial nerve or TMJ, with restenosis if skin coverage and canal contour are poor."],["Why leave normal canal skin whenever possible?","Preserved vascularized epithelium improves healing and reduces exposed bone, granulation and restenosis."]]),
"tegmen-repair":("Confirmed lateral skull-base CSF leak and/or meningoencephalocele requiring durable separation of intracranial contents from the middle ear/mastoid, particularly with recurrent meningitis or persistent leak.",
 [["Transmastoid versus middle-fossa approach?","Choose based on defect location/size, hearing status, number of defects, need for superior exposure and surgeon-specific access; combined approaches are useful for selected broad or difficult defects."],["Why address intracranial-pressure physiology?","Unrecognized elevated ICP can contribute to spontaneous leaks and recurrence after technically successful closure."]]),
"vestibular-schwannoma":("Vestibular schwannoma requiring microsurgical management after balancing tumor size/growth, symptoms, hearing, age/comorbidity, observation and radiosurgery.",
 [["What drives approach selection?","Tumor size/location, serviceable hearing, anatomy and the relative goals of hearing preservation, facial-nerve outcome and tumor control."],["Which approach sacrifices residual hearing?","Translabyrinthine access sacrifices labyrinthine hearing but provides direct IAC/CPA exposure without cerebellar retraction."]]),
"maxillary-antrostomy":("Maxillary sinus disease requiring surgical drainage/access—typically CRS or focal pathology—after diagnosis, medical management and imaging define the target.",
 [["Why find the natural ostium?","Opening only an accessory ostium can leave recirculation and fail to address the true drainage pathway."],["What is the classic orbital hazard?","Violation of the lamina/orbit, especially with superior dissection or distorted anatomy."]]),
"sphenoidotomy":("Sphenoid disease requiring surgical drainage, biopsy or access after CT defines sphenoid pneumatization and optic/carotid/skull-base relationships.",
 [["Why is pre-op CT unusually important?","Optic nerve and carotid canal may be dehiscent or protrude into a highly variable sphenoid sinus."],["What landmark helps identify the sphenoid ostium?","The superior turbinate and sphenoethmoidal recess orient the surgeon to the natural ostium."]]),
"draf":("Refractory frontal sinus disease, mucoceles or selected frontal pathology requiring extended frontal drainage after lesser access is inadequate; choose IIa, IIb or III according to disease extent and anatomy.",
 [["What distinguishes Draf IIa, IIb and III conceptually?","They progressively enlarge frontal access from the drainage pathway between lamina and middle turbinate, to unilateral extension toward the septum, to a common bilateral frontal neo-ostium."],["Why does mucosal preservation matter?","Exposed circumferential bone promotes scarring/neo-osteogenesis and restenosis."]]),
"csf-nasoseptal":("Endoscopically accessible anterior skull-base CSF leak or defect requiring multilayer closure; vascularized nasoseptal flap is especially useful for larger/high-flow defects.",
 [["What must be known before raising a nasoseptal flap?","Defect location, prior septal surgery, vascular pedicle availability and whether the flap will reach the target."],["What causes repair failure?","Missed defects, inadequate multilayer support, flap/pedicle compromise, infection and unaddressed elevated intracranial pressure."]]),
"spa-ligation":("Severe posterior epistaxis refractory to appropriate packing/cautery or recurrent bleeding where definitive endoscopic arterial control is preferred.",
 [["Where do you look for the SPA?","At the sphenopalatine foramen in the posterior lateral nasal wall; branching can occur before or after the foramen."],["Why control multiple branches?","Failure to identify accessory/branching vessels is a common reason for persistent bleeding."]]),
"orbital-abscess":("Sinogenic subperiosteal/orbital abscess requiring drainage because of visual compromise, significant collection, intracranial concern or inadequate response to medical therapy.",
 [["What finding makes this an immediate vision emergency?","Declining acuity/color vision, RAPD, ophthalmoplegia/proptosis progression or other evidence of optic compromise."],["What determines endoscopic versus external access?","Abscess location—medial collections are commonly endoscopically accessible; superior/lateral disease may require external or combined drainage."]]),
"tors":("Selected accessible oropharyngeal primary tumors where transoral resection can achieve oncologic margins with acceptable functional morbidity after comparison with nonsurgical treatment.",
 [["What makes TORS inappropriate?","Inadequate exposure or disease whose deep extent/neurovascular involvement prevents a safe oncologic resection."],["What postoperative event is most feared?","Delayed oropharyngeal hemorrhage, which can rapidly threaten both circulation and airway."]]),
"oral-composite":("Resectable oral-cavity malignancy requiring en bloc primary resection with appropriate mandibular/soft-tissue and neck management to obtain oncologic margins and preserve function when possible.",
 [["Marginal versus segmental mandibulectomy?","It depends on the pattern/depth of mandibular involvement and whether oncologic clearance can preserve mandibular continuity."],["Why plan reconstruction before resection?","The anticipated mucosal, bony and soft-tissue defect determines access, vessel needs and functional reconstruction."]]),
"tep":("Voice rehabilitation after total laryngectomy in an appropriate patient with adequate pulmonary support, manual/device ability and a suitable pharyngoesophageal segment; may be primary or secondary.",
 [["What makes TEP speech work?","Pulmonary air is diverted through a one-way prosthesis into the pharyngoesophageal segment, which becomes the sound source."],["What are common failure modes?","Leak through/around the prosthesis, stenosis, poor PE-segment vibration, granulation and inability to manage the prosthesis."]]),
"central-neck":("Therapeutic central compartment dissection for clinically involved level VI/VII thyroid cancer nodes; prophylactic dissection is not a routine substitute for disease-specific risk assessment.",
 [["What are the key structures at risk?","RLNs and parathyroid glands/vascular supply, with trachea/esophagus and thoracic duct on the low left as additional considerations."],["Why is compartment dissection preferred to node plucking?","It treats the nodal basin systematically and reduces fragmented surgery in a scar-prone central neck."]]),
"reop-thyroid":("Persistent/recurrent thyroid disease requiring reoperation when expected oncologic or compressive benefit outweighs the increased RLN/parathyroid risk of a scarred field.",
 [["Why is pre-op laryngoscopy essential?","Baseline vocal-fold function changes risk counseling and the consequences of injuring the remaining functional RLN."],["What is the reoperative principle?","Use imaging to target disease and approach through the safest recognizable tissue planes rather than blindly recreating the original dissection."]]),
"four-gland":("Primary hyperparathyroidism with suspected multigland disease, nonlocalizing/discordant localization, hereditary disease or an intraoperative physiology/anatomy pattern that makes focused excision unreliable.",
 [["What is the goal of bilateral exploration?","Identify the expected glands systematically and treat the hyperfunctioning pattern while preserving viable parathyroid tissue."],["What makes a gland 'missing'?","Embryologic migration creates predictable ectopic sites; search systematically rather than by color or random dissection."]]),
"reop-parathyroid":("Persistent/recurrent hyperparathyroidism with a reconfirmed biochemical diagnosis and a sufficiently localized target to justify the higher-risk reoperative neck.",
 [["What is the first step before reoperation?","Reconfirm the biochemical diagnosis and review the original operative/pathology records; a reoperative neck should not compensate for diagnostic uncertainty."],["Why demand stronger localization?","Scar increases RLN and devascularization risk, so targeted benefit must justify the reoperation."]]),
"parotid-total":("Parotid malignancy or extensive disease requiring removal of superficial and deep gland; facial nerve sacrifice/reconstruction is reserved for oncologic involvement or unavoidable loss of functional continuity.",
 [["When should the facial nerve be sacrificed?","When oncologic clearance requires it—not simply because the tumor is close to the nerve."],["If nerve is sacrificed, what determines reconstruction?","Defect length/location, proximal/distal stump availability, denervation duration and the need for immediate cable graft, nerve transfer or later dynamic/static rehabilitation."]]),
"peds-ltr":("Fixed pediatric laryngotracheal stenosis causing tracheostomy dependence or significant airway limitation when endoscopic options are inadequate and the child is an appropriate reconstructive candidate.",
 [["Single-stage versus double-stage?","Choice depends on airway severity, comorbidity, pulmonary reserve, aspiration/feeding issues and whether a tracheostomy/stent strategy is needed during healing."],["What determines anterior versus posterior grafting?","The location and geometry of the stenosis and the amount/direction of framework expansion required."]]),
"ctr":("High-grade subglottic stenosis where resection of the diseased cricoid/subglottic segment offers a better durable airway than expansion alone in an appropriately selected patient.",
 [["Why is CTR different from LTR?","CTR removes the stenotic segment and reconstructs the airway by anastomosis, whereas LTR expands the existing framework with grafting."],["What threatens the anastomosis?","Tension, devascularization, infection, airway trauma and recurrent stenosis."]]),
"tracheal-resection":("Short-segment tracheal stenosis or selected tracheal tumor amenable to complete resection and tension-controlled primary anastomosis.",
 [["What limits resection length?","Anastomotic tension and blood supply; release maneuvers can increase mobility but do not make unlimited resection safe."],["What is the catastrophic complication?","Anastomotic dehiscence, which can cause airway loss and mediastinal contamination."]]),
"injection-laryngoplasty":("Symptomatic glottic insufficiency—commonly unilateral vocal-fold paresis/paralysis or atrophy—when temporary or durable medialization is expected to improve voice and/or airway protection.",
 [["Why choose temporary material?","When recovery is possible or the desired degree of permanent medialization is uncertain, temporary augmentation can bridge function and test benefit."],["Where should material be placed conceptually?","Deep/lateral enough to medialize the membranous fold rather than superficially distorting the vibratory cover."]]),
"arytenoid-adduction":("Unilateral vocal-fold paralysis with persistent posterior glottic gap, vertical-level mismatch or inadequate result from medialization alone.",
 [["What does arytenoid adduction correct better than a thyroplasty alone?","Posterior glottic closure and arytenoid/vocal-process position, including selected vertical-height mismatch."],["What are important risks?","Airway compromise, over/underrotation, dysphagia and injury to laryngeal framework/neurovascular structures."]]),
"cordotomy":("Bilateral vocal-fold immobility causing clinically significant airway obstruction when enlarging the posterior glottic airway is favored over tracheostomy or reinnervation options.",
 [["What is the tradeoff?","A larger airway is purchased at the cost of voice quality and potentially swallowing protection."],["Why can revision be needed?","Scar/granulation can narrow the created airway, while an overly aggressive opening can worsen voice/aspiration."]]),
"cp-myotomy":("Selected cricopharyngeal/upper-esophageal-sphincter outflow dysfunction causing dysphagia when objective evaluation supports a focal sphincter problem and less invasive treatment is inadequate.",
 [["Why is manometry/swallow physiology important?","Myotomy helps a restrictive UES but will not correct poor pharyngeal driving force or diffuse esophageal disease."],["What complication is most important?","Perforation/leak with deep neck or mediastinal infection."]]),
"laryngeal-botox":("Task-specific laryngeal dystonia or selected hyperfunctional laryngeal disorders where targeted chemodenervation is expected to improve symptoms.",
 [["Why is dosing individualized?","Target muscle, laterality, prior response, breathiness/dysphagia and disease phenotype determine the therapeutic window."],["What should be discussed before injection?","Expected temporary breathiness/weakness, swallowing effects, onset/duration and need for repeat treatment."]]),
"septorhino":("Persistent nasal obstruction from septal deviation and/or internal/external nasal-valve dysfunction when medical contributors are addressed and structural correction is expected to improve airflow.",
 [["Why is septoplasty alone sometimes insufficient?","The septum may be only one component; lateral-wall collapse, narrow valve angle or weak cartilage may require structural grafting/support."],["What is the operative goal?","Improve functional airway while preserving or restoring stable nasal support and acceptable appearance."]]),
"otoplasty":("Prominent-ear deformity causing meaningful patient concern when cartilage shape/position can be corrected with informed expectations and age-appropriate consent.",
 [["What deformities usually contribute?","Underdeveloped antihelical fold, conchal excess and increased conchomastoid angle—often in combination."],["What causes an unnatural result?","Overcorrection, sharp cartilage edges, asymmetry or failure to preserve a smooth helical contour."]]),
"forehead-flap":("Large/deep nasal cutaneous defects—especially involving multiple subunits or requiring replacement of skin plus support/lining—where staged vascularized forehead tissue provides the best color/texture match.",
 [["What must be reconstructed before skin cover?","Internal lining and structural cartilage/bone support when deficient; skin alone cannot prevent collapse or contraction."],["Why respect nasal subunits?","Replacing a substantial subunit to its borders can hide scars and improve contour compared with patching across convex/concave boundaries."]]),
"deep-neck-drain":("Deep neck-space infection with a drainable abscess, airway compromise, sepsis, descending spread or failure of appropriate medical therapy.",
 [["What comes before incision?","Airway strategy and imaging-based localization of the involved spaces and carotid sheath/mediastinal relationships."],["What is the danger of incomplete drainage?","Persistent infection can track across connected fascial spaces into the mediastinum or threaten major vessels/airway."]])
}
for _slug,(_ind,_qs) in OR_DEPTH_V95.items():
    if _slug in OR_PREP_REGISTRY:
        OR_PREP_REGISTRY[_slug]["indications"]=_ind
        OR_PREP_REGISTRY[_slug]["attending_followup"]=_qs
        OR_PREP_REGISTRY[_slug]["status"]="depth-audited-v9.5"

# Rebuild adaptive items after the content additions/updates.
ADAPTIVE_ITEMS_V95=[]
for _domain,_mods in DEEP_MODULES_V6.items():
    for _m in _mods:
        _id=_v6_item_id(_domain,_m["topic"])
        for _stage in ["recognize","localize","workup","manage","operate","teach"]:
            ADAPTIVE_ITEMS_V95.append({
              "id":_id+"-"+_stage,"concept_id":_id,"domain":_domain,"topic":_m["topic"],
              "stage":_stage,"display_stage":"advanced" if _stage=="operate" else _stage,
              "prompt":{"recognize":"Recognize the pattern.","localize":"Localize the problem.","workup":"Evaluate it efficiently.","manage":"Build the management sequence.","operate":"Make the advanced decision.","teach":"Teach the mental model."}[_stage],
              "answer":_m[_stage],"minutes":{"recognize":3,"localize":3,"workup":4,"manage":4,"operate":6,"teach":4}[_stage],
              "level":{"recognize":1,"localize":2,"workup":3,"manage":4,"operate":5,"teach":6}[_stage],
              "tags":_m.get("tags",_tags_v94(_m["topic"],_domain))
            })
ADAPTIVE_ITEMS_V94=ADAPTIVE_ITEMS_V95
ADAPTIVE_ITEMS_V91=ADAPTIVE_ITEMS_V95

PUBLIC_EVIDENCE_V95 = [
 {"topic":"Sudden Sensorineural Hearing Loss","source":"AAO-HNSF Clinical Practice Guideline: Sudden Hearing Loss (Update), 2019","note":"Timing, salvage IT steroid, HBOT and follow-up recommendations."},
 {"topic":"Tympanostomy Tube Indications","source":"AAO-HNSF Clinical Practice Guideline: Tympanostomy Tubes in Children (Update), 2022","note":"Chronic OME, hearing evaluation and recurrent-AOM/effusion decision points."},
 {"topic":"Recurrent Tonsillitis Decision-Making","source":"AAO-HNSF Clinical Practice Guideline: Tonsillectomy in Children (Update), 2019","note":"7/5/3 thresholds, qualifying documentation and modifying factors."},
 {"topic":"Differentiated Thyroid Cancer","source":"American Thyroid Association Management Guidelines for Adult Patients with Differentiated Thyroid Cancer, 2025","note":"Extent of surgery, active surveillance and completion-thyroidectomy framework."},
 {"topic":"Hypoglossal Nerve Stimulation","source":"FDA PMA P130008/S090, 2023 labeling expansion","note":"Adult AHI expansion to 100 and BMI warning boundary to 40; payer criteria may differ."},
 {"topic":"Age-Related Hearing Loss / Presbycusis","source":"AAO-HNSF Clinical Practice Guideline: Age-Related Hearing Loss, 2024","note":"Recognition, audiologic evaluation, amplification/assistive technology and implant referral concepts."},
]


import re
# =============================================================================
# ENT Mastery v9.6 — True Depth + Oncology Pass
# =============================================================================
# Public oncology guidance is synthesized into original educational prose.
# Cummings is used as a scope/organization benchmark; copyrighted textbook
# prose is not copied into the application.

PUBLIC_ONCOLOGY_SOURCES_V96 = [
 {"source":"Cummings Otolaryngology—Head and Neck Surgery, official Elsevier table of contents",
  "use":"Scope benchmark: tumor biology/immunotherapy, radiation/systemic therapy, free tissue transfer, palliative care, cutaneous melanoma, subsite oncology, swallowing and tracheal neoplasms."},
 {"source":"American Academy of Dermatology BCC guideline",
  "use":"Risk-oriented biopsy/treatment framework; surgery as cornerstone; selected nonsurgical therapy; surveillance."},
 {"source":"American Academy of Dermatology cSCC guideline",
  "use":"Localized risk stratification, biopsy, surgery, selected nonsurgical therapy and surveillance."},
 {"source":"American Academy of Dermatology melanoma guideline",
  "use":"Biopsy, surgery, SLNB staging concepts and risk-adapted follow-up."},
 {"source":"ASCO Management of the Neck in SCC of the Oral Cavity and Oropharynx",
  "use":"Elective/therapeutic neck management and post-RT/CRT response-based neck dissection concepts."},
 {"source":"ASCO Transoral Robotic Surgery in Oropharyngeal SCC guideline, 2025",
  "use":"Workup, patient selection, surgical approach, adjuvant and salvage considerations."},
 {"source":"ISOO-MASCC-ASCO Osteoradionecrosis guideline, 2024",
  "use":"Prevention and management framework for jaw osteoradionecrosis after radiation."},
 {"source":"NCI PDQ Merkel Cell Carcinoma",
  "use":"Local-regional surgery/radiation, nodal staging and immunotherapy concepts for advanced disease."},
]

# ---- Dedicated cutaneous oncology modules ----
CUTANEOUS_ONCOLOGY_V96 = [
 {"topic":"Cutaneous Squamous Cell Carcinoma of the Head & Neck",
  "recognize":"Confirm invasive cSCC with a biopsy that captures enough depth and architecture to identify aggressive features. Head/neck location, recurrence, poor differentiation, rapid growth, neurologic symptoms, immunosuppression and suspected deep invasion should immediately raise the risk level.",
  "localize":"Map the primary tumor, depth and named-nerve symptoms, then examine the regional nodal basins—especially parotid/periparotid and upper cervical nodes for many facial/scalp primaries. Pain, numbness or weakness may signal clinically important perineural spread.",
  "workup":"Risk-stratify from clinical and pathologic features rather than diameter alone. Use imaging when deep invasion, bone involvement, significant PNI or nodal disease is suspected; suspicious nodes require tissue diagnosis. The workup should answer whether this remains a local skin problem or has become regional/advanced head-and-neck cancer.",
  "manage":"Surgery is the cornerstone for resectable disease. Standard excision is appropriate for many lower-risk lesions, while margin-controlled surgery is particularly useful for high-risk tumors, recurrent disease, poorly defined borders or tissue-constrained head/neck sites. Regional nodal or extensive PNI disease should trigger multidisciplinary surgery/radiation/systemic discussion.",
  "operate":"Do not reconstruct a complex defect until oncologic clearance is understood. For regional disease, think in terms of the involved parotid and cervical nodal basin rather than removing a single palpable node. Preserve function when oncologically safe, but named-nerve invasion may require sacrifice and a simultaneous reanimation plan.",
  "teach":"Teach cSCC as three linked questions: how risky is the primary, is there nerve/nodal spread, and what margin-control/regional treatment is needed? The common error is treating every facial cSCC as a small dermatologic lesion despite aggressive biology or regional symptoms."},
 {"topic":"Basal Cell Carcinoma of the Head & Neck",
  "recognize":"BCC often presents as a slowly enlarging pearly, ulcerated or scar-like lesion, but infiltrative/morpheaform tumors may be clinically subtle. Recurrent disease, ill-defined borders, aggressive histology, prior radiation and high-value facial sites increase management complexity.",
  "localize":"Define the cutaneous subunit and depth: eyelid/canthus, nose, ear and central face have limited tissue and important cartilage, lacrimal, orbital or nerve relationships. Unlike cSCC, nodal metastasis is rare, so the central problem is usually local destruction and recurrence.",
  "workup":"Biopsy should establish diagnosis and relevant growth pattern. Image selectively for extensive deep invasion, orbital/skull-base involvement or clinically significant perineural disease rather than routinely staging uncomplicated BCC.",
  "manage":"Surgery remains the treatment cornerstone. Standard excision works well for many lower-risk lesions; Mohs/margin-controlled excision is favored when tissue preservation and complete margin assessment matter, including recurrent, aggressive or anatomically constrained head/neck disease. Nonsurgical approaches have lower cure rates and are mainly for selected low-risk disease or when surgery is unsuitable.",
  "operate":"Plan reconstruction after margin status is secure. Reconstruct by defect depth and facial subunit: replace lining/support when necessary before skin cover, avoid distorting free margins and choose local flap, graft or staged regional flap according to the missing tissue.",
  "teach":"BCC is usually a local-control problem, not a nodal-staging problem. The resident pearl is to match treatment intensity to recurrence risk and anatomy, then reconstruct only after the tumor is cleared."},
 {"topic":"Cutaneous Melanoma of the Head & Neck",
  "recognize":"A suspicious pigmented or amelanotic lesion needs biopsy designed to establish Breslow thickness, ulceration and other staging information without compromising definitive surgery. Do not perform a casual superficial shave when invasion depth is clinically important.",
  "localize":"Head/neck melanoma can drain unpredictably to parotid, cervical and occipital basins. Primary-site anatomy matters for excision/reconstruction, but lymphatic mapping—not assumptions from surface location—guides sentinel-node staging when indicated.",
  "workup":"Use final pathology to determine local excision and nodal-staging needs. Sentinel lymph node biopsy is a pathologic-staging tool in appropriate patients; imaging and systemic staging intensity depend on stage, symptoms and recurrence risk rather than being routine for every thin melanoma.",
  "manage":"Wide local excision is the cornerstone for invasive cutaneous melanoma, with margins selected from tumor thickness and anatomy. Consider SLNB when the risk of occult nodal disease justifies staging; advanced or node-positive disease requires multidisciplinary discussion of modern systemic/adjuvant therapy.",
  "operate":"In the head/neck, balance oncologic margins with eyelid, nasal, auricular and facial-nerve function. If SLNB is planned, lymphatic mapping should precede disruption of drainage pathways. Delay definitive reconstruction only when margin uncertainty would make a complex repair unsafe.",
  "teach":"Melanoma management starts with the biopsy: depth drives downstream decisions. The head/neck twist is lymphatic unpredictability and reconstructive constraint, not a different cancer biology."},
 {"topic":"Merkel Cell Carcinoma",
  "recognize":"MCC is an aggressive cutaneous neuroendocrine carcinoma that may look like a rapidly enlarging painless red-violet dermal nodule. Small primary size does not imply low biologic risk, and immunosuppression increases concern.",
  "localize":"Stage both the primary and the regional nodal basin. Clinically occult nodal disease is common enough that sentinel-node staging is important in appropriate node-negative patients; in the head/neck, lymphatic drainage may be complex.",
  "workup":"Confirm histology and perform regional/distant staging appropriate to clinical stage. Sentinel lymph node biopsy is used for pathologic nodal staging in clinically node-negative patients, ideally before wide local surgery disrupts lymphatic channels.",
  "manage":"Local-regional management commonly combines margin-negative excision with consideration of radiation because MCC is radiosensitive and recurrence-prone. Nodal disease requires definitive regional treatment. For advanced/metastatic disease, immune checkpoint therapy is generally favored over historical chemotherapy because responses can be more durable.",
  "operate":"Obtain local control while preserving function, coordinate SLNB timing, and avoid treating the primary in isolation when regional management is unresolved. Reconstruction should not obscure the oncologic plan or delay indicated adjuvant therapy unnecessarily.",
  "teach":"MCC behaves more aggressively than its skin appearance suggests. Teach the triad: local excision, deliberate nodal staging, and early radiation/systemic multidisciplinary thinking."},
]

# Remove the old combined cutaneous cards and replace them with dedicated disease modules.
for _i in range(len(DEEP_MODULES_V6.get("Head & Neck Oncology",[]))-1,-1,-1):
    if DEEP_MODULES_V6["Head & Neck Oncology"][_i].get("topic") in [
        "Cutaneous SCC / Melanoma of Head & Neck",
        "Merkel Cell / High-Risk Cutaneous Cancer"
    ]:
        DEEP_MODULES_V6["Head & Neck Oncology"].pop(_i)
for _m in CUTANEOUS_ONCOLOGY_V96:
    _m["primary_domain"]="Head & Neck Oncology"
    _m["tags"]=_tags_v94(_m["topic"],"cutaneous oncology skin cancer")
    _m["evidence_calibrated"]="v9.6"
    DEEP_MODULES_V6["Head & Neck Oncology"].append(_m)

# ---- Cross-cutting Head & Neck oncology modules ----
HN_ONCOLOGY_DEPTH_V96 = [
 {"topic":"Recurrent / Metastatic HNSCC",
  "recognize":"Recurrence may be local, regional or distant and can present with pain, dysphagia, weight loss, cranial neuropathy, new neck mass or subtle post-treatment imaging change. Distinguish recurrence from treatment effect before committing to salvage.",
  "localize":"Define the exact recurrent compartment and its relationship to carotid, skull base, prevertebral fascia, mandible, larynx/pharynx and previously treated neck. The key question is whether disease is resectable with acceptable function and whether distant disease changes the goal of care.",
  "workup":"Obtain tissue confirmation when feasible, high-quality cross-sectional imaging and chest/distant staging. Review prior radiation fields, pathology, HPV status where relevant, performance status and functional reserve; recurrent disease must be discussed in a multidisciplinary setting.",
  "manage":"Potentially curable isolated recurrence may be treated with salvage surgery and/or carefully selected re-irradiation strategies. Unresectable or metastatic disease shifts toward systemic therapy, trials and symptom-directed care, with immunotherapy now central for many patients.",
  "operate":"Salvage surgery has higher wound, fistula and vascular risk because tissue is irradiated and planes are distorted. Before operating, define the expected defect, reconstruction, vessel options, carotid risk, feeding/airway plan and whether the functional result is worth the morbidity.",
  "teach":"Recurrence is not automatically palliative and not automatically operable. Teach three filters: disease extent, prior treatment constraints, and whether salvage can achieve durable control with an acceptable functional endpoint."},
 {"topic":"Tumor Immunology / Immunotherapy in HNSCC",
  "recognize":"Checkpoint inhibition matters most in recurrent/metastatic HNSCC and selected perioperative/clinical-trial settings, not as a substitute for definitive local therapy in every new cancer.",
  "localize":"The therapeutic target is the tumor-immune interaction rather than an anatomic structure; the clinically relevant biology includes PD-1/PD-L1 signaling, immune evasion and HPV-associated tumor immunology.",
  "workup":"Systemic-treatment planning requires accurate histology, stage, performance status, prior therapy and biomarker testing appropriate to the clinical setting. Biomarkers inform probability and regimen selection but do not replace multidisciplinary assessment of resectability and radiation options.",
  "manage":"Immune checkpoint inhibitors are a core option in recurrent/metastatic HNSCC. Treatment choice depends on disease tempo, symptoms, biomarker profile, prior platinum exposure and need for rapid cytoreduction; immune-related toxicities require prompt recognition and organ-specific management.",
  "operate":"For the surgeon, immunotherapy changes timing, salvage options and perioperative planning rather than surgical anatomy itself. Know whether the patient is receiving neoadjuvant/adjuvant therapy, anticipate wound/medical issues and obtain adequate tissue for molecular/pathologic testing.",
  "teach":"Do not memorize immunotherapy as 'a drug after chemo.' Teach when systemic disease goals dominate, what biomarker information changes decisions, and how immune toxicity differs from cytotoxic chemotherapy toxicity."},
 {"topic":"Salvage Surgery After Radiation / Chemoradiation",
  "recognize":"Persistent or recurrent tumor after RT/CRT must be separated from edema, radionecrosis and inflammatory PET uptake. Symptoms, serial imaging and directed biopsy matter more than a single ambiguous post-treatment study.",
  "localize":"Map recurrence against irradiated tissues and critical structures: carotid, mandible, larynx/pharynx, skull base and prevertebral space. Previously dissected necks and irradiated recipient vessels alter access and reconstruction.",
  "workup":"Confirm viable tumor, stage for distant disease, review prior dose/fields and assess swallowing, pulmonary, nutritional and performance status. If salvage is contemplated, plan reconstruction and vascular access before resection.",
  "manage":"Offer salvage when complete resection is realistically achievable and morbidity is acceptable. Otherwise consider re-irradiation, systemic therapy, trials or palliative interventions based on disease distribution and goals.",
  "operate":"Expect fibrosis, poor tissue perfusion, higher fistula/wound risk and difficult vessel/nerve identification. Bring well-vascularized tissue when needed and plan carotid protection, airway, feeding access and rescue strategy.",
  "teach":"Salvage surgery is not just the original operation performed later. It is a different biologic and reconstructive problem in irradiated tissue."},
 {"topic":"Neck Management by Primary Site",
  "recognize":"The clinically N0 neck can still harbor occult metastasis; treatment depends on primary site, T stage, depth/biology and expected nodal drainage rather than a universal elective neck dissection.",
  "localize":"Know predictable nodal drainage: oral cavity commonly levels I–III; oropharynx frequently II–IV with retropharyngeal considerations; larynx/hypopharynx patterns depend on subsite and midline involvement.",
  "workup":"Use high-quality neck examination and imaging; suspicious nodes require tissue diagnosis when it changes treatment. In oral cavity SCC, depth of invasion contributes to the elective-neck decision. After definitive RT/CRT, response imaging guides whether residual nodal surgery is needed.",
  "manage":"Elective neck treatment may be surgical or radiation-based depending on the primary strategy. Therapeutic neck dissection addresses clinically involved nodal basins; postoperative RT/CRT depends on adverse pathology such as extranodal extension and margins.",
  "operate":"A selective dissection is oncologic only when the selected levels match the disease pattern. Preserve nonlymphatic structures when safe, but do not compromise nodal clearance to spare a structure invaded by tumor.",
  "teach":"Neck management starts with the primary site. Ask: what levels are at risk, is the neck clinically positive, and is the primary being treated surgically or nonsurgically?"},
 {"topic":"Reconstruction Selection After Head & Neck Ablation",
  "recognize":"Reconstruction begins before resection. The defect may require mucosal lining, skin, soft-tissue bulk, bone, tendon/muscle function or separation of contaminated spaces.",
  "localize":"Define what is missing and what function must be restored: oral competence, tongue mobility, mandibular continuity, pharyngeal conduit, laryngeal separation, facial contour or skull-base seal.",
  "workup":"Assess defect estimate, prior radiation/surgery, recipient vessels, nutrition, vascular disease and donor-site limitations. CTA or other vascular imaging is selective when donor/recipient vessel disease is a concern.",
  "manage":"Choose the simplest reconstruction that reliably restores function and withstands the oncologic environment. Local/regional flaps work for selected defects; free tissue is favored when volume, long reach, bone or robust vascularized tissue is required.",
  "operate":"Match flap tissue to defect rather than choosing a favorite flap. Plan recipient vessels and backups, inset to restore function before contour, protect the pedicle from compression and monitor for arterial insufficiency or venous congestion.",
  "teach":"A flap is not the goal; restored function and safe wound healing are. Teach defect analysis first, donor selection second."},
 {"topic":"Osteoradionecrosis of the Jaw",
  "recognize":"Exposed bone, pain, drainage, pathologic fracture, fistula or progressive mandibular/maxillary destruction after head/neck radiation raises ORN, but recurrent tumor and dental infection must remain in the differential.",
  "localize":"Mandibular ORN is common because of dose distribution and vascular/dental factors. Extent ranges from limited exposed bone to full-thickness necrosis with fracture, fistula or inferior-border involvement.",
  "workup":"Obtain dental/maxillofacial examination and imaging sufficient to define bone involvement and exclude recurrent malignancy when suspicious. Prevention begins before radiation with dental risk assessment and minimizing traumatic extractions in high-dose fields when possible.",
  "manage":"Treatment is stage/severity driven: meticulous oral care and conservative measures for limited disease, selective debridement for focal necrosis, and vascularized reconstruction for advanced fracture/fistula or refractory full-thickness disease. Hyperbaric oxygen is not a universal solution.",
  "operate":"Advanced ORN often requires resection back to bleeding viable bone and reconstruction with vascularized tissue, frequently osseous free flap when continuity is lost. Plan vessels carefully in the irradiated neck.",
  "teach":"ORN is radiation-injured bone plus impaired healing, not simply osteomyelitis. Always exclude recurrent cancer and match treatment intensity to structural failure."},
 {"topic":"Nonfunctional Larynx / Chronic Aspiration After Cancer Therapy",
  "recognize":"A cancer survivor may have no recurrent tumor yet remain unsafe because of chronic aspiration, recurrent pneumonias, feeding dependence, airway obstruction or profound fibrosis-related dysphagia.",
  "localize":"Define whether failure arises from glottic closure, laryngeal sensation, pharyngeal propulsion, UES opening, structural stenosis or global radiation fibrosis. Multiple mechanisms often coexist.",
  "workup":"Use flexible laryngoscopy plus instrumental swallow evaluation; assess pulmonary complications, nutrition, voice goals and cancer status. The question is not merely whether aspiration occurs, but whether compensatory strategies can make oral intake safe.",
  "manage":"Begin with rehabilitation, diet/strategy changes and targeted treatment of correctable lesions. Severe refractory aspiration may require feeding modification or aspiration-prevention surgery when quality of life and pulmonary risk justify loss of normal laryngeal function.",
  "operate":"Procedural options range from vocal-fold augmentation or UES intervention to laryngotracheal separation or functional/total laryngectomy in extreme cases. The operation should target the demonstrated mechanism and the patient's priorities.",
  "teach":"Cancer control and organ preservation are not the same as functional preservation. A preserved larynx that repeatedly aspirates can be a failed organ."},
 {"topic":"Head & Neck Cancer Surveillance / Second Primaries",
  "recognize":"New pain, dysphagia, otalgia, weight loss, bleeding, neck mass, cranial neuropathy or changing endoscopic findings after treatment should not be dismissed as chronic treatment effect.",
  "localize":"Surveillance targets the treated primary site, nodal basins, lungs and other mucosal/skin sites at risk for recurrence or second primary disease.",
  "workup":"Use regular symptom-directed examination and endoscopy plus post-treatment imaging according to treatment/site and risk. Thyroid, dental, swallowing, hearing and other late-effect monitoring depend on radiation/surgery exposure.",
  "manage":"Surveillance is not only recurrence detection: address tobacco/alcohol cessation, nutrition, dental care, hypothyroidism, lymphedema, dysphagia, speech/voice, psychosocial health and second-primary prevention.",
  "operate":"Surgery enters when surveillance identifies a resectable recurrence, second primary or treatable late complication. Do not schedule invasive biopsies of clearly stable treatment changes without a diagnostic question.",
  "teach":"Survivorship is active care. The resident should know both what recurrence looks like and what treatment toxicity will harm the patient years later."},
 {"topic":"Sinonasal Malignancies",
  "recognize":"Unilateral obstruction, epistaxis, facial numbness, orbital symptoms, cranial neuropathy or destructive unilateral imaging should raise malignancy rather than routine CRS.",
  "localize":"Define the epicenter—nasal cavity, maxillary, ethmoid, frontal or sphenoid—and extension to orbit, skull base, dura, pterygopalatine/infratemporal spaces and cranial nerves.",
  "workup":"Perform endoscopy, contrast CT/MRI and safe biopsy. Pathology is heterogeneous, so treatment cannot be planned from location alone; histology and skull-base/orbital involvement drive staging and modality selection.",
  "manage":"Most resectable epithelial sinonasal cancers require multidisciplinary surgery and radiation consideration; some histologies favor different systemic/radiation strategies. Orbital preservation depends on true soft-tissue/apical invasion rather than proximity alone.",
  "operate":"Choose endoscopic, open or combined approach based on oncologic access, margins and reconstruction—not on a minimally invasive preference. Plan skull-base reconstruction, orbital management and vascular control before resection.",
  "teach":"Sinonasal cancer is a histology-plus-anatomy problem. Unilateral 'sinus disease' with red flags should trigger tissue diagnosis before routine FESS."},
 {"topic":"Tracheal Malignancy",
  "recognize":"Progressive dyspnea, stridor, hemoptysis or 'refractory asthma' can reflect tracheal tumor, especially when flow-volume loops or imaging show fixed central airway obstruction.",
  "localize":"Define distance from cricoid/carina, longitudinal length, circumferential involvement, extraluminal extension and relationship to esophagus, thyroid, recurrent laryngeal nerves and great vessels.",
  "workup":"Secure a safe airway plan before diagnostic bronchoscopy in a critically narrowed airway. Contrast CT defines length and invasion; endoscopy provides histology and dynamic assessment when it can be performed safely.",
  "manage":"Resectable primary tracheal malignancies may be treated with segmental resection and anastomosis; unresectable disease may require radiation/systemic therapy and airway palliation such as debulking or stenting.",
  "operate":"Resection length is limited by anastomotic tension and blood supply. Preserve recurrent laryngeal nerves and lateral tracheal vascularity, use release maneuvers selectively and protect the anastomosis from tension/infection.",
  "teach":"A tracheal tumor is both an oncologic and airway emergency-planning problem. Never biopsy a critically obstructing lesion without a ventilation/rescue strategy."},
 {"topic":"Palliative / Goals-of-Care Decision-Making in Head & Neck Cancer",
  "recognize":"Advanced head/neck cancer causes uniquely burdensome symptoms—airway threat, bleeding, pain, dysphagia, secretion burden, disfigurement and communication loss—so palliative care should not be reserved for the final days.",
  "localize":"Identify which symptom is driving suffering and whether it comes from tumor, treatment toxicity or both. Local anatomy determines whether a small intervention can meaningfully improve breathing, swallowing, bleeding or pain.",
  "workup":"Clarify prognosis, functional trajectory, decisional capacity, patient priorities and what each proposed intervention can realistically achieve. Avoid diagnostic testing that will not change a goal-concordant plan.",
  "manage":"Integrate palliative and disease-directed care early. Options may include analgesia, secretion management, nutrition, palliative radiation/systemic therapy, limited surgery, airway procedures, hospice and psychosocial support.",
  "operate":"A technically possible operation is not automatically beneficial. Before tracheostomy, debulking or major salvage surgery, define the symptom target, likely recovery burden and whether the intervention supports the patient's stated goals.",
  "teach":"Palliative care is not 'doing nothing.' It is choosing treatments by patient-valued outcomes when cure is impossible or the burden of curative treatment exceeds its benefit."},
]
for _m in HN_ONCOLOGY_DEPTH_V96:
    _m["primary_domain"]="Head & Neck Oncology"
    _m["tags"]=_tags_v94(_m["topic"],"head neck cancer oncology")
    _m["evidence_calibrated"]="v9.6"
    if not any(x["topic"]==_m["topic"] for x in DEEP_MODULES_V6["Head & Neck Oncology"]):
        DEEP_MODULES_V6["Head & Neck Oncology"].append(_m)

# ---- Remove all generic v9.4 objective scaffolding from the source-derived modules ----
_V94_SCAFFOLD_PATTERNS = [
 r"\s*Recognition objective:.*$",
 r"\s*Localization objective:.*$",
 r"\s*Evaluation objective:.*$",
 r"\s*Management objective:.*$",
 r"\s*Advanced-decision objective:.*$",
 r"\s*Teaching objective:.*$",
]
for _domain,_mods in DEEP_MODULES_V6.items():
    for _m in _mods:
        for _stage in ["recognize","localize","workup","manage","operate","teach"]:
            _txt=_m.get(_stage,"")
            for _pat in _V94_SCAFFOLD_PATTERNS:
                _txt=re.sub(_pat,"",_txt).strip()
            _m[_stage]=_txt

# ---- True-depth rewrites of high-yield existing concepts ----
TRUE_DEPTH_REWRITES_V96 = {
"Chronic Otitis Media / Cholesteatoma":{
 "recognize":"Retraction pocket with keratin, attic/posterosuperior debris, chronic foul otorrhea, conductive loss or granulation suggests cholesteatoma. Facial weakness, vertigo, severe headache or neurologic symptoms imply a complication until proven otherwise.",
 "localize":"Track disease from pars flaccida/epitympanum or pars tensa into mesotympanum, sinus tympani, facial recess, aditus and mastoid. Hidden recesses, ossicles, facial nerve, lateral semicircular canal, tegmen and sigmoid sinus determine both risk and residual-disease sites.",
 "workup":"Microscopic/endoscopic ear exam and audiometry are foundational. CT defines bony anatomy, ossicular erosion, fistula and surgical landmarks; non-EPI diffusion MRI is useful for selected residual/recurrent disease questions but does not replace operative judgment in an unsafe ear.",
 "manage":"An unsafe keratinizing ear generally requires surgery for disease control. Choose canal-wall-up, canal-wall-down or endoscopic-assisted strategies from extent, anatomy, Eustachian function, hearing goals and the patient's ability to undergo reliable surveillance.",
 "operate":"The priority hierarchy is safe ear → dry/maintainable ear → hearing. Constantly orient to tegmen, sigmoid, EAC, lateral canal, incus/fossa incudis, facial nerve and digastric ridge; reconstruct hearing only after disease clearance and a stable middle-ear environment are achieved.",
 "teach":"Canal-wall strategy is not a prestige ranking. Explain why cholesteatoma is a three-dimensional disease with hidden recesses and why surveillance strategy is part of the operation."},
"Otosclerosis / Stapes Fixation":{
 "recognize":"Progressive conductive or mixed hearing loss with normal otoscopy, absent acoustic reflexes and a characteristic audiogram suggests stapes fixation; a Carhart notch supports but does not prove otosclerosis.",
 "localize":"The primary mechanical lesion is fixation of the stapes footplate at the oval window. Cochlear otosclerosis can add a sensorineural component, so not every threshold deficit is mechanically reversible.",
 "workup":"Obtain complete audiometry including speech scores and tympanometry/reflexes. CT is selective—useful for atypical conductive loss, congenital fixation, superior canal dehiscence or revision anatomy rather than mandatory for every classic primary case.",
 "manage":"Observation, hearing aids and stapes surgery are all reasonable depending on functional burden, cochlear reserve and patient goals. Counsel that surgery targets the conductive component and does not stop age-related/cochlear hearing decline.",
 "operate":"Create a controlled fenestra, place a prosthesis between incus and vestibule, and avoid excessive vestibular trauma. Know facial nerve position, chorda tympani, incus integrity and the risk of perilymph leak, vertigo, taste change and rare profound SNHL.",
 "teach":"Before operating on 'otosclerosis,' prove the loss is mechanical and exclude third-window/congenital mimics. The operation improves sound transmission; it does not cure cochlear disease."},
"Vestibular Schwannoma":{
 "recognize":"Asymmetric SNHL, unilateral tinnitus or disproportionate word-recognition loss should prompt retrocochlear thinking; larger tumors may cause imbalance, facial/trigeminal symptoms or brainstem/cerebellar effects.",
 "localize":"Vestibular schwannoma usually arises from vestibular nerve within the IAC and may extend into the CPA. Tumor size, fundal extension, brainstem contact and residual hearing shape management.",
 "workup":"MRI with IAC protocol is diagnostic. Document pure-tone thresholds, word recognition, vestibular/facial function and tumor growth on serial imaging when observing; broad laboratory testing is not the workup.",
 "manage":"Observation, stereotactic radiation and microsurgery are all valid in selected patients. Decide from age/comorbidity, size/growth, symptoms, hearing, brainstem effect and patient preference rather than tumor diameter alone.",
 "operate":"Retrosigmoid, middle-fossa and translabyrinthine approaches trade exposure and hearing goals differently. Facial nerve preservation is a major endpoint; continuous monitoring and careful tumor-nerve dissection matter more than forcing gross-total resection when nerve function is threatened.",
 "teach":"The treatment question is not 'How do we remove it?' It is 'What outcome matters most—tumor control, hearing, facial function—and which strategy best balances those goals?'"},
"Ménière Disease":{
 "recognize":"Episodic spontaneous vertigo with fluctuating unilateral sensorineural hearing symptoms, tinnitus and aural pressure suggests Ménière disease; duration and audiometric documentation matter.",
 "localize":"The clinical syndrome reflects inner-ear dysfunction associated with endolymphatic hydrops, but hydrops is not synonymous with the diagnosis. Vestibular migraine and other episodic vestibular disorders can mimic it.",
 "workup":"Obtain audiometry and assess alternative causes based on atypical features. MRI is used when asymmetric SNHL or neurologic features warrant retrocochlear exclusion; vestibular tests support function but are not a single diagnostic gold standard.",
 "manage":"Educate about episodic disease, hearing rehabilitation and trigger/lifestyle measures; use vestibular suppressants only for acute attacks. Escalate from medical prevention to intratympanic therapy and, in disabling refractory disease, ablative options based on hearing status and goals.",
 "operate":"Procedural choices intentionally trade vertigo control against hearing/vestibular function. Intratympanic gentamicin, labyrinthectomy and vestibular neurectomy are not equivalent; residual useful hearing and contralateral vestibular reserve matter.",
 "teach":"Do not label every patient with vertigo+tinnitus as Ménière disease. The syndrome requires a coherent episodic pattern plus hearing evidence, and treatment escalates according to disability and hearing preservation."},
"Vestibular Migraine":{
 "recognize":"Recurrent vertigo, motion sensitivity or visually induced dizziness with migraine history/features can represent vestibular migraine even when headache is absent during some attacks.",
 "localize":"This is a central sensory-network disorder rather than a fixed peripheral vestibular lesion; exam and vestibular testing may be normal between episodes.",
 "workup":"Diagnosis is clinical after confirming compatible migraine/vestibular episodes and excluding alternative peripheral or central causes when red flags exist. Do not order extensive vestibular imaging/labs solely because dizziness is persistent.",
 "manage":"Use migraine education, sleep/exercise/trigger management and preventive or acute migraine therapy tailored to attack frequency and comorbidity. Vestibular rehabilitation can help persistent motion/visual sensitivity.",
 "operate":"There is no operative treatment for vestibular migraine. Advanced decision-making is recognizing comorbid BPPV/Ménière disease or a central red flag rather than escalating to ablative vestibular surgery.",
 "teach":"The pearl is that normal interictal vestibular testing does not rule out vestibular migraine. Treat the migraine network and avoid forcing every dizzy patient into a peripheral lesion."},
"BPPV":{
 "recognize":"Brief vertigo triggered by position change with reproducible canal-specific positional nystagmus is a mechanical otolith disorder. Persistent spontaneous vertigo or atypical neurologic nystagmus should trigger a different differential.",
 "localize":"Use the nystagmus axis and provocative position to identify posterior, horizontal or anterior canal and side. Geotropic versus apogeotropic horizontal nystagmus changes the suspected mechanism and maneuver.",
 "workup":"Dix-Hallpike and supine roll testing are the key diagnostic tests. Routine MRI, CT and vestibular testing are unnecessary in classic BPPV but become appropriate when the phenotype is atypical or neurologic signs are present.",
 "manage":"Use the canal-appropriate repositioning maneuver and avoid chronic vestibular suppressants. Reassess persistent symptoms for wrong-canal localization, recurrence, cupulolithiasis or a central mimic.",
 "operate":"BPPV almost never needs surgery. In truly intractable well-localized disease, rare occlusion procedures exist, but the advanced decision is usually better localization and repeated appropriate maneuvers rather than an operation.",
 "teach":"Name the canal before naming the maneuver. If you cannot describe the nystagmus, you have not localized the disease."},
"Facial Paralysis":{
 "recognize":"First distinguish upper from lower motor-neuron weakness, complete from incomplete paralysis, immediate from delayed onset, and flaccid paralysis from synkinesis. Ear vesicles, trauma, tumor signs, recurrent episodes or progressive weakness are not routine Bell palsy.",
 "localize":"Use forehead involvement, taste/lacrimation symptoms, hyperacusis, ear disease and other cranial neuropathies to localize along the facial nerve from brainstem to parotid branches.",
 "workup":"Typical acute Bell palsy often needs no imaging; atypical, recurrent, progressive, traumatic or tumor-associated palsy requires targeted MRI/CT and etiologic evaluation. Document severity serially with a consistent facial grading system and ocular status.",
 "manage":"Eye protection is immediate. Treat idiopathic acute palsy promptly with corticosteroids; manage Ramsay Hunt, infection, trauma or neoplasm according to cause. Persistent weakness evolves into rehabilitation, synkinesis treatment and reanimation planning.",
 "operate":"Timing determines the reconstructive toolbox: primary repair/cable graft when nerve continuity is lost acutely, nerve transfer while native muscle remains viable, and regional/free muscle transfer when chronic denervation has eliminated useful motor endplates.",
 "teach":"Facial paralysis is not one disease. Every presentation should be classified by lesion level, cause, completeness and time since denervation because those variables determine both prognosis and reconstruction."},
"Temporal Bone Fracture":{
 "recognize":"After head trauma, hemotympanum, otorrhea, hearing loss, vertigo or facial weakness should prompt temporal-bone injury assessment. Modern management is driven by functional complications rather than memorizing longitudinal versus transverse labels alone.",
 "localize":"Determine whether the fracture violates the otic capsule, facial canal, ossicular chain, tegmen or carotid canal. Otic-capsule involvement strongly predicts SNHL/vestibular and CSF complications.",
 "workup":"Use high-resolution CT when temporal-bone injury is suspected and findings will guide management. Document facial function timing, hearing, vestibular symptoms and CSF leak; vascular imaging is required when carotid-canal injury is concerning.",
 "manage":"Most fractures are observed with treatment of specific complications. Persistent conductive loss suggests ossicular injury; CSF leak, complete facial paralysis or vascular injury require dedicated pathways.",
 "operate":"Surgical decisions target complications—not the fracture line itself—such as facial-nerve decompression/repair in selected severe injuries, ossicular reconstruction or CSF-leak repair.",
 "teach":"Ask what the fracture damaged: nerve, labyrinth, ossicles, dura or carotid. That predicts management better than the old orientation terminology."},
"Cochlear Implant Candidacy":{
 "recognize":"Consider CI when appropriately fitted hearing aids no longer provide adequate speech understanding and communication benefit, not only when the audiogram reaches profound thresholds.",
 "localize":"The implant bypasses damaged cochlear hair-cell transduction and electrically stimulates the cochlear nerve. An absent or severely deficient cochlear nerve changes expected benefit and may redirect toward other technologies.",
 "workup":"Use aided speech testing, ear-specific audiology, imaging, medical/surgical evaluation and counseling. In children, integrate language development, educational environment and etiology/genetics; in adults, assess duration of deafness and realistic listening goals.",
 "manage":"Optimize conventional amplification first when appropriate, then refer early when speech performance remains poor. Counseling should cover rehabilitation, residual-hearing tradeoffs, device expectations and lifelong programming.",
 "operate":"Preoperative imaging must define cochlear patency, congenital malformations and facial-nerve/vascular anatomy. Electrode choice/insertion strategy should match anatomy and hearing-preservation goals while minimizing cochlear trauma.",
 "teach":"CI candidacy is a functional speech-understanding decision layered onto anatomy and patient goals—not a pure-tone cutoff."},
"Necrotizing Otitis Externa":{
 "recognize":"Severe persistent otalgia—often worse at night—with otorrhea/granulation in an older diabetic or immunocompromised patient should raise skull-base osteomyelitis. Cranial neuropathy indicates advanced disease.",
 "localize":"Infection begins in the external canal and can spread through skull-base soft tissue and bone to multiple cranial nerves. The disease is not simply 'bad swimmer's ear.'",
 "workup":"Culture canal drainage/tissue when possible, assess inflammatory markers and obtain imaging to define skull-base extension. Biopsy suspicious granulation when malignancy cannot be excluded.",
 "manage":"Use prolonged culture-directed antipseudomonal therapy with glycemic/immunologic optimization and close clinical/marker follow-up. Surgery is limited mainly to biopsy, drainage or focal debridement rather than radical resection of skull-base infection.",
 "operate":"Avoid unnecessary aggressive canal/skull-base surgery; identify abscess, necrotic focus or diagnostic uncertainty that actually requires a procedure. Cranial neuropathy or progression despite therapy warrants multidisciplinary escalation.",
 "teach":"The clue is disproportionate pain in a high-risk patient. Once skull-base osteomyelitis is suspected, treatment duration and follow-up are driven by clinical response—not by a short otitis-externa course."},
"Allergic Rhinitis":{
 "recognize":"Sneezing, itching, watery rhinorrhea and congestion linked to exposures support allergic rhinitis; fixed unilateral obstruction, purulence, recurrent epistaxis or anosmia with other features should broaden the diagnosis.",
 "localize":"IgE-mediated nasal mucosal inflammation produces turbinate vascular engorgement and glandular secretion. Structural septal/valve obstruction may coexist but is mechanistically separate.",
 "workup":"History and exam usually establish the phenotype. Allergy testing is useful when confirmation changes avoidance, immunotherapy or diagnostic uncertainty; sinus CT is not a routine allergic-rhinitis test.",
 "manage":"Use allergen/environmental measures plus intranasal corticosteroid and/or intranasal antihistamine according to symptom pattern. Consider immunotherapy for persistent clinically relevant sensitization despite appropriate treatment or when disease modification is desired.",
 "operate":"Surgery does not treat IgE biology. Septal/turbinate/valve procedures are reserved for persistent structural obstruction after the inflammatory component is treated.",
 "teach":"A large turbinate is a sign, not an etiology. Separate reversible mucosal inflammation from fixed anatomy before offering surgery."},
"CRS Phenotyping":{
 "recognize":"CRS requires ≥12 weeks of compatible symptoms plus objective inflammation; phenotyping by polyps, eosinophilic/type-2 features, asthma/AERD, fungal disease and other modifiers is more useful than treating all CRS as one infection.",
 "localize":"Map disease by sinus drainage pathways and endoscopic phenotype, but also recognize systemic mucosal inflammation. Polyps, olfactory loss and asthma often signal a different inflammatory biology than isolated odontogenic or localized disease.",
 "workup":"Confirm with endoscopy and/or CT; reserve cultures for selected refractory purulence and evaluate immune, ciliary, fungal or odontogenic contributors when history suggests them. CT severity alone does not define symptom burden.",
 "manage":"Saline and topical intranasal corticosteroid therapy are foundational. Add short systemic therapy, biologics or surgery according to phenotype, severity and prior response rather than requiring a rigid 'maximal medical therapy' checklist.",
 "operate":"Surgery opens diseased drainage pathways and creates access for topical treatment; extent should match disease distribution and goals. Preserve mucosa and landmarks while recognizing that surgery controls disease but does not cure the inflammatory tendency.",
 "teach":"CRS management is phenotype → objective disease → treatment response → individualized surgery/biologic decision, not repeated antibiotics for a CT scan."},
"AERD":{
 "recognize":"Adult-onset asthma, CRSwNP and respiratory reactions to COX-1 inhibitors form AERD. Severe recurrent polyposis and anosmia may precede a clearly recognized NSAID reaction history.",
 "localize":"This is systemic dysregulated arachidonic-acid/eicosanoid inflammation affecting upper and lower airways, not simply aspirin allergy plus unrelated polyps.",
 "workup":"Diagnosis is often clinical; aspirin challenge is used when history is uncertain and the result changes management. Evaluate asthma control and objective sinonasal disease before planning surgery/desensitization.",
 "manage":"Use topical sinonasal therapy, guideline-based asthma care and appropriately selected biologic therapy. Aspirin desensitization followed by maintenance therapy is an option in selected patients; FESS is often coordinated to improve sinus access and disease control.",
 "operate":"Surgery treats the anatomic burden and improves topical delivery but recurrence risk remains high without longitudinal inflammatory management. Plan postoperative anti-inflammatory strategy before operating.",
 "teach":"AERD is a chronic upper-and-lower-airway inflammatory syndrome. The operation is one component of a medical-surgical disease-control plan."},
"CSF Rhinorrhea":{
 "recognize":"Clear unilateral watery rhinorrhea that increases with dependent position/strain, recurrent meningitis or a skull-base defect history should raise CSF leak. Do not diagnose by taste alone.",
 "localize":"Leak may arise from cribriform, ethmoid roof, sphenoid or frontal skull base; spontaneous leaks are often associated with elevated intracranial-pressure physiology and may be multifocal.",
 "workup":"Confirm fluid with beta-2 transferrin or beta-trace protein and localize with thin-cut CT plus MRI when encephalocele/soft tissue is suspected. Avoid indiscriminate bedside glucose testing.",
 "manage":"Persistent cranial CSF leak generally requires repair because of meningitis risk. Address contributing intracranial-pressure physiology in spontaneous leaks to reduce recurrence.",
 "operate":"Endoscopic repair uses defect-specific multilayer closure; high-flow/large defects may require vascularized flap support. Identify all defects, preserve flap pedicle and plan postoperative pressure management.",
 "teach":"Two questions: is it truly CSF, and exactly where is the defect? Repair without recognizing elevated ICP is a setup for recurrence."},
"Invasive Fungal Rhinosinusitis":{
 "recognize":"In an immunocompromised, neutropenic or severely uncontrolled diabetic patient, rapidly progressive facial pain, numbness, necrotic mucosa, orbital findings or cranial neuropathy is invasive fungal disease until proven otherwise.",
 "localize":"Angioinvasion allows rapid spread from sinonasal mucosa to orbit, pterygopalatine/infratemporal spaces, skull base, cavernous sinus and brain; the extent may exceed visible necrosis.",
 "workup":"Urgent endoscopy with biopsy for histopathology/culture and contrast CT/MRI should proceed in parallel with stabilization. A normal-looking CT does not safely exclude early invasive disease when clinical suspicion is high.",
 "manage":"Start prompt systemic antifungal therapy, reverse immunosuppression/metabolic derangement when possible and perform serial aggressive-but-goal-directed debridement of nonviable infected tissue.",
 "operate":"Debride until viable bleeding tissue is reached while balancing orbit/skull-base morbidity; repeat examinations/debridements are often necessary because disease evolves after the first operation.",
 "teach":"This is an angioinvasive emergency, not a chronic fungal sinusitis variant. Delay in antifungal therapy or tissue diagnosis can be fatal."},
"Sinonasal Inverted Papilloma":{
 "recognize":"Unilateral papillomatous nasal mass with focal hyperostosis/attachment on CT suggests inverted papilloma; recurrence and synchronous/metachronous SCC risk make simple debulking inadequate.",
 "localize":"Identify the attachment site—often lateral nasal wall/maxillary/ethmoid—and map frontal, sphenoid, orbit or skull-base extension. The attachment, not just the visible bulk, determines the resection.",
 "workup":"Endoscopic biopsy establishes diagnosis after excluding a vascular lesion. CT shows bone/attachment and MRI helps distinguish tumor from retained secretions and assess suspicious malignant transformation.",
 "manage":"Definitive treatment is complete excision including treatment of the attachment site, followed by long-term endoscopic surveillance. Suspected carcinoma changes staging and oncologic planning.",
 "operate":"Use an approach that exposes the entire attachment; drill/remove involved underlying bone when appropriate rather than stripping only mucosa. Protect orbit, skull base, nasolacrimal duct and vascular structures according to site.",
 "teach":"IP recurrence usually reflects residual attachment. The surgical question is 'Where is it attached?' not 'How do I remove the nasal mass?'"},
"Revision FESS":{
 "recognize":"Persistent symptoms after prior sinus surgery may reflect residual inflammatory disease, scarring/stenosis, missed cells/ostia, recirculation, odontogenic disease, migraine or a wrong original diagnosis.",
 "localize":"Reconstruct anatomy from CT and endoscopy before entering the nose. Prior surgery may remove familiar landmarks while leaving dangerous skull-base/orbital relationships unchanged.",
 "workup":"Confirm active CRS objectively and review prior operative notes, pathology/cultures and treatment adherence. CT should be read as a surgical map for residual partitions, frontal recess, sphenoid, orbit, skull base and neo-ostial stenosis.",
 "manage":"Optimize inflammatory phenotype and topical delivery; revise only anatomy that contributes to persistent disease. Biologics may be preferable to repeated surgery in selected severe type-2 CRSwNP.",
 "operate":"Re-establish constant landmarks before crossing scar. Work from known to unknown, preserve viable mucosa and create durable access for postoperative care rather than chasing every radiographic opacity.",
 "teach":"Revision surgery is diagnostic humility plus anatomy. First ask why the first treatment failed; otherwise you may repeat the same failure with fewer landmarks."},
"Thyroid Nodule":{
 "recognize":"A thyroid nodule is a malignancy-risk and symptom problem, not an automatic surgical diagnosis. Suspicious nodes, hoarseness, rapid growth or fixation change urgency.",
 "localize":"Characterize intrathyroidal lesion(s), contralateral gland and central/lateral neck nodes; assess tracheal/esophageal/RLN relationships when compression or invasion is suspected.",
 "workup":"Start with TSH and dedicated thyroid/neck ultrasound. Hyperfunctioning nodules follow a functional pathway; euthyroid/hypothyroid nodules use ultrasound risk and size to determine FNA. Indeterminate cytology may require repeat sampling, molecular testing or diagnostic surgery depending on context.",
 "manage":"Observation, interval ultrasound, ablation in selected benign symptomatic nodules, lobectomy or total thyroidectomy depends on malignancy probability, symptoms, bilateral disease, patient preference and downstream treatment needs.",
 "operate":"Choose extent before incision and plan RLN/EBSLN, parathyroid and nodal strategy. A nodule with no operative indication should not become thyroidectomy simply because localization or technology is available.",
 "teach":"Use a sequence: thyroid function → ultrasound risk → FNA when indicated → ask what result would change treatment. That prevents reflex surgery and unnecessary biopsy."},
"Primary Hyperparathyroidism":{
 "recognize":"PHPT is a biochemical diagnosis: hypercalcemia with an inappropriately high or non-suppressed PTH after excluding important mimics such as medication effects and familial hypocalciuric hypercalcemia.",
 "localize":"Localization studies identify abnormal gland(s) for operative planning only after the biochemical diagnosis is secure. Typical inferior/superior glands and embryologic ectopic sites guide the search.",
 "workup":"Confirm calcium/PTH, renal function and vitamin D; assess urine calcium when FHH is a concern, skeletal density/fracture and renal stone/nephrocalcinosis burden. Ultrasound, sestamibi/SPECT, 4D-CT or other localization is chosen for surgical planning.",
 "manage":"Parathyroidectomy is definitive for symptomatic disease and for guideline-supported asymptomatic indications; observation is possible in selected patients with structured calcium, renal and skeletal follow-up.",
 "operate":"Focused excision is reasonable with concordant single-gland localization and appropriate physiology; bilateral exploration is preferred when multigland disease is suspected or localization is unreliable. Identify RLN and preserve viable normal parathyroid tissue.",
 "teach":"Diagnosis and localization are different questions. A negative sestamibi does not rule out PHPT; it only makes the surgical map less certain."},
"Salivary Gland Malignancy":{
 "recognize":"A firm salivary mass with pain, rapid growth, fixation, skin involvement, trismus, facial weakness or cervical nodes is malignant until proven otherwise; painless slow growth does not exclude low-grade cancer.",
 "localize":"Map superficial/deep parotid or submandibular origin, facial nerve relationship, parapharyngeal extension and cervical nodes. Named-nerve symptoms raise perineural spread toward skull base.",
 "workup":"Ultrasound-guided FNA/core sampling and contrast imaging define diagnosis and extent; MRI is especially useful for PNI/deep-space relationships. Chest/distant staging depends on histology/grade and stage.",
 "manage":"Resectable disease is generally managed surgically with adjuvant RT based on grade, stage, margins, PNI and nodal risk. Systemic/targeted options vary by histology and molecular alterations in recurrent/metastatic disease.",
 "operate":"Preserve a functioning facial nerve unless directly involved; if oncologic clearance requires sacrifice, plan immediate graft/transfer when feasible. Neck management depends on clinical nodes and occult-risk biology.",
 "teach":"Salivary cancer is histology-driven. The same parotid operation can have very different neck, nerve, radiation and systemic implications depending on grade and subtype."},
"Medullary Thyroid Cancer":{
 "recognize":"MTC arises from parafollicular C cells; calcitonin/CEA, family history or MEN2 features distinguish it from differentiated follicular-cell cancers. Always consider hereditary RET-associated disease.",
 "localize":"Assess both thyroid lobes and central/lateral cervical nodes; hereditary MTC may be multifocal/bilateral. Advanced disease may involve mediastinum or distant liver/lung/bone.",
 "workup":"Measure calcitonin/CEA, perform neck ultrasound and obtain RET germline testing. Before thyroid surgery in MEN2, exclude pheochromocytoma; cross-sectional/distant staging is risk- and burden-dependent.",
 "manage":"Total thyroidectomy is the standard primary operation for established MTC, with compartment-oriented nodal surgery based on clinical disease and biochemical/anatomic context. Advanced disease may use RET-targeted/systemic therapy.",
 "operate":"Do not treat MTC like low-risk papillary microcarcinoma. Plan central/lateral disease deliberately, protect RLNs/parathyroids and resolve pheochromocytoma risk before anesthesia.",
 "teach":"The board pearl is sequence: MTC → RET testing → look for pheochromocytoma before thyroid surgery → treat nodal disease compartmentally."},
"Anaplastic Thyroid Cancer":{
 "recognize":"Rapidly enlarging hard thyroid/neck mass, dyspnea, dysphagia, hoarseness and invasive imaging in an older adult is anaplastic cancer until proven otherwise. Airway deterioration can be rapid.",
 "localize":"Map trachea, esophagus, carotid, prevertebral fascia and mediastinal extension; many tumors are unresectable because they invade critical structures rather than because of size alone.",
 "workup":"Obtain rapid tissue diagnosis, airway assessment, staging and urgent molecular testing because actionable alterations can change systemic therapy. Multidisciplinary planning should occur immediately, not after elective clinic workup.",
 "manage":"Treatment is individualized among targeted therapy, radiation, systemic therapy, surgery in selected resectable responders and symptom-focused care. Airway, swallowing and goals-of-care decisions are central from diagnosis.",
 "operate":"Avoid heroic incomplete resection that creates morbidity without control. Surgery is reserved for selected resectable disease or converted responders; tracheostomy itself can be technically hazardous in bulky invasive tumor.",
 "teach":"ATC is an oncologic emergency. Think airway + tissue + molecular testing + multidisciplinary plan simultaneously."},
"Pediatric OSA / Adenotonsillar Disease":{
 "recognize":"Habitual snoring plus labored breathing, witnessed apneas, restless sleep, enuresis, behavioral or growth consequences raises pediatric OSA. Tonsil size alone neither diagnoses nor grades OSA.",
 "localize":"Adenotonsillar hypertrophy is common, but obesity, craniofacial anatomy, neuromuscular disease, nasal obstruction, tongue base and laryngomalacia can create multilevel collapse.",
 "workup":"History/exam may be sufficient before adenotonsillectomy in straightforward cases, but PSG is important in high-risk comorbidity, discordant exam/severity, uncertainty or when results will change postoperative monitoring/treatment.",
 "manage":"Adenotonsillectomy is first-line surgery for appropriate adenotonsillar OSA, with postoperative risk stratification and a plan for residual disease. Weight, nasal therapy, PAP, DISE-directed surgery or HNS in selected syndromic patients may enter later.",
 "operate":"Control tonsillar hemorrhage, protect deep pharyngeal structures and perform adenoidectomy with awareness of velopharyngeal/Eustachian anatomy. High-risk children require appropriate postoperative respiratory monitoring.",
 "teach":"AT treats a major contributor, not every cause. Always tell families and juniors that residual OSA is common in obesity and complex airway disease."},
"Laryngomalacia":{
 "recognize":"Inspiratory stridor beginning in infancy, worse with feeding/supine/agitation and usually improving over time suggests laryngomalacia. Cyanosis, apnea, failure to thrive or significant retractions indicate severe disease.",
 "localize":"Dynamic supraglottic collapse may involve arytenoid mucosa, short aryepiglottic folds and/or epiglottic prolapse; assess synchronous lesions when symptoms are atypical or severe.",
 "workup":"Flexible laryngoscopy establishes the diagnosis in most infants. Severe/atypical cases require broader airway and swallowing evaluation based on symptoms; do not attribute every noisy-breathing infant to reflux.",
 "manage":"Mild disease is observed with feeding/growth monitoring. Severe obstruction, feeding failure, hypoxemia or significant OSA may require supraglottoplasty and evaluation for neurologic/cardiopulmonary contributors.",
 "operate":"Tailor supraglottoplasty to the collapsing structure and avoid over-resection that can cause scar or aspiration. Account for neurologic disease and multilevel airway problems that predict poorer surgical response.",
 "teach":"The diagnosis is dynamic collapse, not simply 'floppy epiglottis.' Severity is defined by breathing, growth, feeding and oxygenation—not stridor loudness."},
"Pediatric Subglottic Stenosis":{
 "recognize":"Persistent/recurrent croup-like stridor, extubation failure or biphasic stridor suggests subglottic narrowing; acquired disease is often related to prior intubation, while congenital stenosis has different history/anatomy.",
 "localize":"Define stenosis level, length, circumferential scar, cartilage framework and glottic/posterior involvement. Vocal-fold mobility changes reconstruction strategy.",
 "workup":"Definitive assessment is endoscopic sizing and characterization, supplemented by history and imaging only when external framework or other airway disease requires it. Grade alone is insufficient without length and scar quality.",
 "manage":"Mild disease may be observed or treated endoscopically; repeated dilation is less attractive for long mature circumferential scar, cartilage compromise or rapid recurrence. Open LTR/CTR is chosen by anatomy and patient factors.",
 "operate":"Endoscopic treatment requires controlled radial scar work and dilation without destabilizing cartilage. Open reconstruction must preserve RLNs, restore framework and account for pulmonary/feeding/tracheostomy status.",
 "teach":"For SGS, say more than the grade: location, length, maturity, framework and glottic involvement determine the operation."},
"Pediatric Tracheostomy / Decannulation":{
 "recognize":"Tracheostomy dependence may persist because of upper-airway obstruction, pulmonary need, aspiration, ventilator dependence or neuromuscular weakness. Decannulation is a physiologic milestone, not just tube downsizing.",
 "localize":"Identify whether the remaining barrier is supraglottic/glottic/subglottic/tracheal airway, lung/ventilation, secretion management or swallowing/aspiration.",
 "workup":"Use interval airway endoscopy and institution-specific capping/sleep/respiratory assessment when clinically indicated. Confirm the child can maintain airway, ventilation and secretion clearance without the tube.",
 "manage":"Progress toward speaking valve/capping/downsizing according to the child's airway and respiratory reserve, treating granulation/stenosis and pulmonary/swallow contributors along the way.",
 "operate":"Before decannulation, correct obstructing suprastomal or airway lesions when necessary and plan rescue. Persistent tracheocutaneous fistula after successful decannulation may require later closure.",
 "teach":"The question is not 'Is the airway big enough?' It is whether the child can breathe, sleep, clear secretions and protect the lungs without the tracheostomy."},
"Unilateral Vocal Fold Paralysis":{
 "recognize":"Breathy dysphonia, weak cough and aspiration symptoms with unilateral immobility require distinction between neurogenic paralysis and cricoarytenoid fixation/scar.",
 "localize":"Trace the vagus/RLN pathway from skull base through neck/chest according to side and associated cranial findings. Position, bowing, phase asymmetry and glottic gap describe functional consequences but do not by themselves localize the lesion.",
 "workup":"Flexible laryngoscopy/stroboscopy documents motion and closure; image along the nerve when etiology is unexplained. Laryngeal EMG is selective for prognosis or differentiating neurogenic from mechanical dysfunction.",
 "manage":"Voice therapy, temporary injection, permanent framework surgery and reinnervation are selected by symptom burden, aspiration, expected nerve recovery and patient goals.",
 "operate":"Temporary augmentation is useful when recovery remains possible; medialization thyroplasty offers adjustable durable closure, arytenoid adduction addresses posterior gap/height mismatch, and reinnervation restores tone rather than immediate position.",
 "teach":"Treat glottic insufficiency, not just immobility. The best operation depends on expected recovery and the specific closure defect."},
"Dysphagia / Aspiration":{
 "recognize":"Coughing/choking, wet voice, recurrent pneumonia, weight loss or prolonged meals suggest dysphagia, but silent aspiration can occur without cough.",
 "localize":"Separate oral preparation, pharyngeal timing/propulsion, laryngeal closure/sensation, UES opening and esophageal transit. Residue location and aspiration timing point to different mechanisms.",
 "workup":"FEES and MBS/VFSS answer complementary questions; choose based on physiology needed, secretion assessment, radiation exposure and patient access. Esophageal testing is added when symptoms/localization extend beyond the pharynx.",
 "manage":"Treat the mechanism with diet/bolus modification, posture/maneuvers, rehabilitation and targeted procedural therapy. Avoid making permanent diet restrictions from a single observation without testing whether an intervention improves physiology.",
 "operate":"Procedures are mechanism-specific: augmentation for glottic insufficiency, UES treatment for true outflow dysfunction, diverticulum surgery for Zenker and aspiration-prevention surgery for refractory life-threatening aspiration.",
 "teach":"Always describe aspiration as before, during or after the swallow and explain why. That converts 'aspiration' from a finding into a treatment plan."},
"Subglottic / Tracheal Stenosis":{
 "recognize":"Progressive exertional dyspnea, stridor or 'refractory asthma' with fixed upper-airway obstruction should trigger laryngotracheal stenosis evaluation, especially after intubation/tracheostomy or in autoimmune disease.",
 "localize":"Define glottic, subglottic and tracheal level, length, circumferential scar, cartilage integrity and distance from vocal folds/carina; posterior glottic fixation changes the diagnosis and surgery.",
 "workup":"Flexible exam plus operative endoscopy characterize lumen and scar; CT helps long-segment/extrinsic anatomy. Evaluate systemic inflammatory causes when history suggests them.",
 "manage":"Short soft stenosis may respond to endoscopic incision/dilation/injection; mature long circumferential or framework disease more often needs open reconstruction/resection. Recurrence pattern matters more than the number of prior dilations.",
 "operate":"Endoscopic treatment should create controlled radial release rather than circumferential mucosal destruction. Resection/reconstruction requires tension control, blood-supply preservation and a postoperative airway/anastomotic plan.",
 "teach":"Describe stenosis by level, length, grade, scar maturity and framework—not grade alone. Those descriptors predict whether dilation is reasonable."},
"Bilateral Vocal Fold Immobility":{
 "recognize":"Biphasic stridor with both folds near midline may be bilateral RLN paralysis or posterior glottic fixation; voice can be deceptively good despite a dangerous airway.",
 "localize":"Differentiate neurogenic bilateral paralysis from cricoarytenoid fixation/posterior glottic scar. History of intubation, surgery and neurologic disease plus endoscopic joint assessment guides localization.",
 "workup":"Flexible laryngoscopy documents motion/airway; CT and laryngeal EMG are selective. Operative palpation of arytenoid joints may be needed when fixation remains uncertain.",
 "manage":"Acute unsafe airway requires secure ventilation/tracheostomy strategy. Longer-term options include observation for recovery, reinnervation/pacing concepts or airway-widening procedures depending on etiology and goals.",
 "operate":"Posterior cordotomy/arytenoid procedures enlarge the airway at the expense of voice and sometimes swallowing; avoid irreversible widening early when meaningful nerve recovery is likely.",
 "teach":"The central tradeoff is airway versus voice. First diagnose paralysis versus fixation, then decide how much posterior glottic airway the patient needs."},
"Zenker Diverticulum":{
 "recognize":"Older patient with dysphagia, regurgitation of undigested food, halitosis, cough or aspiration may have Zenker diverticulum from pharyngoesophageal outflow dysfunction.",
 "localize":"The pouch arises through Killian dehiscence above the cricopharyngeus; the functional problem includes a restrictive/noncompliant CP segment, not simply a bag that needs removal.",
 "workup":"Barium esophagram defines pouch size and anatomy; endoscopy assesses mucosa and alternative pathology when appropriate. Evaluate aspiration/nutrition in frail patients.",
 "manage":"Symptomatic disease is treated by dividing the common wall/CP muscle through endoscopic stapling, flexible septotomy/Z-POEM-type techniques or open diverticulectomy/diverticulopexy with myotomy based on anatomy and expertise.",
 "operate":"Endoscopic treatment requires safe exposure and complete-enough septal/CP division without perforation; open surgery exposes recurrent laryngeal nerve and deep-neck structures.",
 "teach":"If you treat the pouch without addressing the cricopharyngeal dysfunction, you miss the mechanism. Myotomy/septotomy is the key therapeutic principle."},
"ZMC / Orbital Trauma":{
 "recognize":"Malar flattening, trismus, infraorbital numbness, diplopia or palpable step-offs after facial trauma suggests ZMC injury. Vision loss, RAPD or severe orbital pain is an emergency before fracture repair.",
 "localize":"Assess the zygomaticofrontal, infraorbital rim, zygomaticomaxillary buttress and arch plus orbital floor/walls. ZMC displacement changes orbital volume and facial projection in three dimensions.",
 "workup":"Document acuity, pupils, motility, diplopia, globe position and sensation; CT with multiplanar reconstruction defines displacement, orbital defect and associated fractures.",
 "manage":"Observe nondisplaced asymptomatic fractures; repair displaced fractures causing malar deformity, trismus, unstable buttress or clinically important orbital dysfunction once urgent ocular injuries are addressed.",
 "operate":"Restore the zygoma to stable reference points before accepting fixation; verify orbital volume and avoid entrapping tissue. Fixation sequence should reproduce width, projection and rim alignment rather than chasing one CT line.",
 "teach":"ZMC is a three-dimensional facial-frame injury. Vision comes first, then restore projection and orbital volume."},
"Mandible Fracture":{
 "recognize":"Malocclusion, step deformity, mobility, trismus, open gingival wound or V3 numbness after trauma suggests mandibular fracture; anterior blows may also injure one or both condyles.",
 "localize":"Classify symphysis/parasymphysis, body, angle, ramus and condyle and identify multiple fractures. Dentition and muscle pull determine displacement and fixation biomechanics.",
 "workup":"Document preinjury/current occlusion, dental/open-fracture status and inferior alveolar function; panoramic imaging and/or CT define pattern and associated facial injury.",
 "manage":"Closed versus open treatment depends on displacement, stability, occlusion, dentition, fracture location and patient factors. Antibiotic and dental management follow open-fracture principles when appropriate.",
 "operate":"Re-establish occlusion before final fixation. Choose load-sharing versus load-bearing constructs from fracture complexity and bone quality; protect tooth roots and inferior alveolar nerve.",
 "teach":"The endpoint is preinjury occlusion and stable biomechanics, not simply a straight postoperative x-ray."},
"Functional Septorhinoplasty":{
 "recognize":"Persistent nasal obstruction from septal deviation plus internal/external valve narrowing or lateral-wall collapse should be separated from reversible rhinitis and isolated turbinate hypertrophy.",
 "localize":"Assess septum, caudal/dorsal support, internal valve angle, upper lateral cartilage, lateral crus/alar rim and dynamic sidewall collapse; each zone requires a different structural solution.",
 "workup":"History, anterior rhinoscopy/endoscopy, decongestion response and dynamic valve maneuvers define the obstructing components. CT is not routinely needed for isolated functional valve/septal disease.",
 "manage":"Treat mucosal disease first when significant, then offer structural surgery when fixed obstruction persists and symptoms correlate with exam. Counsel that cosmetic changes may occur when support is modified.",
 "operate":"Correct septal obstruction while preserving an adequate L-strut, then use spreader, batten, lateral-crural, rim or septal-extension strategies only for a defined mechanical failure. Avoid destabilizing the nose to improve one narrow segment.",
 "teach":"Name the failed structure before naming the graft. Functional rhinoplasty is biomechanics, not a menu of cartilage pieces."},
"Facial Nerve Reanimation":{
 "recognize":"Determine whether the problem is acute nerve discontinuity, recoverable paralysis, chronic flaccid denervation or synkinesis. Eye protection and oral competence may require immediate treatment even while etiology is being defined.",
 "localize":"Map proximal and distal facial-nerve availability and which facial muscle groups remain viable. Denervation duration predicts whether native mimetic muscles can still respond to reinnervation.",
 "workup":"Document branch-specific facial function, ocular status, duration and cause; use imaging/electrodiagnostics selectively when they change lesion localization or reconstructive timing.",
 "manage":"Use eye protection, therapy and botulinum treatment when appropriate. Repair/graft acute discontinuity, nerve-transfer a viable chronic-but-not-endstage native muscle system, and use muscle transfer/static suspension when native motor units are no longer useful.",
 "operate":"Primary neurorrhaphy should be tension-free; cable graft bridges a gap, masseteric/hypoglossal strategies supply motor input, and free functional muscle transfer restores smile when native muscle is irreversibly denervated.",
 "teach":"Timing is anatomy. The same patient six weeks versus six years after injury has a completely different reconstructive toolbox."},
"DISE":{
 "recognize":"DISE is a dynamic airway-phenotyping tool for selected sleep-surgery planning; it is not a diagnostic substitute for PSG and should answer a specific treatment question.",
 "localize":"Describe collapse by level and pattern—velum, oropharyngeal lateral wall, tongue base and epiglottis—rather than merely saying 'multilevel obstruction.'",
 "workup":"Review PSG, awake anatomy, PAP history and planned therapeutic choices before DISE. Sedation should approximate sleep while avoiding excessive depth that creates nonphysiologic collapse.",
 "manage":"Use DISE findings to choose or avoid targeted surgery and to assess HNS eligibility, especially complete concentric palatal collapse. Do not operate on every observed collapse without considering its clinical importance.",
 "operate":"During DISE, systematically inspect the airway, document pattern/severity, use maneuvers such as jaw/tongue advancement when relevant and maintain safe sedation/airway control.",
 "teach":"PSG tells you how severe OSA is; DISE helps explain how the airway collapses. Neither test alone chooses the entire treatment plan."},
"PAP Troubleshooting":{
 "recognize":"PAP 'failure' may actually be mask leak, pressure intolerance, nasal obstruction, insomnia, aerophagia, poor education or untreated positional/weight factors rather than physiologic inability to use PAP.",
 "localize":"Identify whether the limiting problem is interface, upper-airway resistance, pressure delivery, sleep behavior or residual events despite apparently adequate use.",
 "workup":"Review objective adherence, residual AHI/event type, leak, pressure curves and symptoms. Repeat titration or sleep evaluation when residual physiology is unclear rather than declaring PAP failure from self-report alone.",
 "manage":"Fix interface and nasal issues, adjust mode/pressure/humidification, use behavioral support and address comorbidity. Only after a real optimization attempt should alternative surgery, oral appliance or other therapy be framed as PAP intolerance/failure.",
 "operate":"Surgery may reduce anatomic obstruction or create an alternative pathway, but it should not be used to avoid troubleshooting a correctable mask/pressure problem. The operation is phenotype-driven, not frustration-driven.",
 "teach":"Before sending a patient to sleep surgery, ask to see the PAP data. 'I couldn't tolerate CPAP' is the beginning of the workup, not the end."},
"Residual OSA After Surgery":{
 "recognize":"Persistent snoring, daytime symptoms or abnormal postoperative PSG after adenotonsillectomy, palate surgery or multilevel procedures means residual OSA, not automatically failed technique.",
 "localize":"Residual disease may reflect untreated level(s), weight change, craniofacial structure, tongue-base/epiglottic collapse or nonobstructive events. The residual phenotype can differ from the preoperative phenotype.",
 "workup":"Use postoperative PSG when clinically indicated, reassess weight/anatomy and consider DISE for additional surgery. Verify whether residual events are obstructive, central or positional before choosing another operation.",
 "manage":"Options include PAP re-trial, weight management, oral appliance, positional therapy, targeted revision/multilevel surgery, HNS or skeletal surgery depending on residual mechanism.",
 "operate":"Do not stack procedures blindly. A second operation should have a demonstrated target and a realistic chance of meaningful benefit compared with PAP or other nonsurgical therapy.",
 "teach":"Residual OSA is a new diagnostic problem. Re-phenotype the patient instead of repeating the original treatment."},
"Post-Tonsillectomy Hemorrhage":{
 "recognize":"Any fresh oral bleeding or hematemesis after tonsillectomy is potentially significant even if bleeding has stopped on arrival. Recurrent swallowing, tachycardia or clot in the fossa increases concern.",
 "localize":"Bleeding usually arises from the tonsillar fossae; secondary hemorrhage occurs when eschar separates during healing. The immediate danger is both blood loss and aspiration/airway contamination.",
 "workup":"Assess hemodynamics and airway, establish IV access and obtain CBC/type-and-screen/coagulation testing according to severity. Do not repeatedly traumatize an uncooperative bleeding child with prolonged bedside manipulation.",
 "manage":"Resuscitate, involve anesthesia/OR early for active, recurrent or concerning bleeding and use antifibrinolytic/temporary measures according to local protocol while definitive control is organized.",
 "operate":"Induce anesthesia with a full-stomach/hemorrhage airway plan, evacuate clot, identify the bleeding point and achieve secure cautery/ligation. Reinspect both fossae and stomach/airway contamination before emergence.",
 "teach":"A post-tonsil bleed can look deceptively stable between episodes. Treat the history and clot burden seriously because the next bleed may be brisk."},
"Deep Neck Space Infection":{
 "recognize":"Fever, odynophagia, trismus, muffled voice, neck swelling, toxic appearance or cranial/airway symptoms can indicate infection beyond a simple tonsillar process. Drooling, stridor and rapidly progressive floor-of-mouth swelling are airway warnings.",
 "localize":"Localize to peritonsillar, parapharyngeal, retropharyngeal/danger, submandibular, masticator or carotid spaces because spread patterns determine airway, mediastinal and vascular risk.",
 "workup":"Airway assessment precedes imaging in an unstable patient. Contrast CT defines drainable collection and space involvement; MRI is selective. Obtain cultures from drainage and consider odontogenic source, Lemierre syndrome or mediastinal extension.",
 "manage":"Start IV antibiotics and supportive care, secure the airway when threatened and drain abscesses that are large, complicated, worsening or not responding. Source-control decisions depend on space, size and clinical course.",
 "operate":"Choose transoral versus transcervical drainage from location and vascular relationships. Protect carotid sheath/cranial nerves and open all communicating loculations; persistent sepsis should prompt a search for missed spaces or descending infection.",
 "teach":"Deep neck infection management is airway + antibiotics + source control. If you only name the antibiotic, you have not managed the patient."},
"Tracheostomy Emergency":{
 "recognize":"Sudden desaturation, high airway pressures, absent airflow, bleeding or inability to pass suction catheter in a tracheostomy patient is an airway emergency. Determine whether the tract is mature before manipulating it.",
 "localize":"The problem may be tube obstruction, displacement/false passage, mucus plug, cuff issue, pneumothorax or disease distal/proximal to the tube. Upper-airway patency determines whether oral ventilation is possible.",
 "workup":"Treat first and diagnose simultaneously: remove inner cannula, suction, assess capnography/air entry and inspect tube position. Bronchoscopy/imaging follows stabilization when obstruction/displacement remains uncertain.",
 "manage":"Give oxygen to face and stoma, call for airway help and replace/remove the tube according to tract maturity and the patient's upper-airway status. A fresh tract should not be blindly instrumented.",
 "operate":"If the airway cannot be restored through the stoma, move to the safest alternate ventilation/intubation strategy and obtain endoscopic/surgical control. Significant tracheostomy hemorrhage requires consideration of tracheo-innominate fistula.",
 "teach":"The first lifesaving question is whether air can move through the tube. If not, remove the obstruction/tube and oxygenate by whichever airway route is actually patent."},
}
for _domain,_mods in DEEP_MODULES_V6.items():
    for _m in _mods:
        _r=TRUE_DEPTH_REWRITES_V96.get(_m.get("topic"))
        if _r:
            _m.update(_r)
            _m["evidence_calibrated"]="v9.6"

# Rebuild adaptive bank.
ADAPTIVE_ITEMS_V96=[]
for _domain,_mods in DEEP_MODULES_V6.items():
    for _m in _mods:
        _id=_v6_item_id(_domain,_m["topic"])
        for _stage in ["recognize","localize","workup","manage","operate","teach"]:
            ADAPTIVE_ITEMS_V96.append({
              "id":_id+"-"+_stage,"concept_id":_id,"domain":_domain,"topic":_m["topic"],
              "stage":_stage,"display_stage":"advanced" if _stage=="operate" else _stage,
              "prompt":{"recognize":"Recognize the pattern.","localize":"Localize the problem.","workup":"Evaluate it efficiently.","manage":"Build the management sequence.","operate":"Make the advanced decision.","teach":"Teach the mental model."}[_stage],
              "answer":_m[_stage],
              "minutes":{"recognize":3,"localize":3,"workup":4,"manage":4,"operate":6,"teach":4}[_stage],
              "level":{"recognize":1,"localize":2,"workup":3,"manage":4,"operate":5,"teach":6}[_stage],
              "tags":_m.get("tags",_tags_v94(_m["topic"],_domain))
            })
ADAPTIVE_ITEMS_V95=ADAPTIVE_ITEMS_V96
ADAPTIVE_ITEMS_V94=ADAPTIVE_ITEMS_V96
ADAPTIVE_ITEMS_V91=ADAPTIVE_ITEMS_V96


# =============================================================================
# ENT Mastery v9.7 — Remaining Depth + Surgical Anatomy Pass
# =============================================================================

NEW_DEPTH_MODULES_V97 = {
"Otology / Neurotology":[
 {"topic":"Persistent Postural-Perceptual Dizziness (PPPD)",
  "recognize":"Chronic nonspinning dizziness/unsteadiness present most days for months and worsened by upright posture, motion, complex visual environments or busy stores/screens suggests PPPD, often after a vestibular, migraine, anxiety or medical trigger.",
  "localize":"PPPD is a functional sensory-integration disorder rather than a fixed unilateral vestibular lesion. The problem is maladaptive weighting of visual, vestibular and postural inputs plus heightened threat/vigilance.",
  "workup":"Confirm the characteristic time course and triggers, then look for active vestibular, neurologic or cardiac disease that would better explain symptoms. Vestibular testing may be normal or may show a prior trigger disorder; abnormal tests do not exclude superimposed PPPD.",
  "manage":"Education, graded vestibular rehabilitation, treatment of comorbid migraine/anxiety and selected serotonergic medication are commonly combined. Avoid chronic vestibular suppressants, which can reinforce compensation failure.",
  "operate":"There is no operative treatment for PPPD. The advanced decision is recognizing when persistent symptoms are due to PPPD layered on top of a treated peripheral disorder rather than escalating to destructive vestibular procedures.",
  "teach":"PPPD is real dizziness without a single damaged end organ. The board/clinic pearl is persistent visually/posturally provoked symptoms after a trigger with no better structural explanation."},
 {"topic":"Patulous Eustachian Tube Dysfunction",
  "recognize":"Autophony of voice/breathing, aural fullness and symptoms that improve when supine or worsen with weight loss/dehydration suggest patulous rather than obstructive ET dysfunction.",
  "localize":"The Eustachian tube remains abnormally open, allowing nasopharyngeal pressure and sound transmission into the middle ear; this is physiologically opposite to obstructive ETD.",
  "workup":"Look for TM movement with respiration during symptoms, use tympanometry/endoscopy when helpful and distinguish superior canal dehiscence, middle-ear muscle disorders and ordinary occlusion/autophony complaints.",
  "manage":"Hydration, stopping aggravating decongestants, treating weight-loss or mucosal contributors and selected topical/mechanical therapies are first-line. Procedures are reserved for persistent disabling disease.",
  "operate":"Procedural strategies attempt to narrow or damp the tube/tympanic membrane system without creating permanent obstructive ETD. Counsel that outcomes are variable and symptoms can fluctuate.",
  "teach":"Autophony does not always mean superior canal dehiscence. Ask whether the patient hears breathing and whether lying down improves symptoms."},
 {"topic":"Perilymph Fistula / Inner-Ear Window Leak",
  "recognize":"Sudden or fluctuating hearing loss, vertigo or disequilibrium after barotrauma, penetrating trauma, surgery or major pressure event can suggest a perilymph leak, but symptoms are nonspecific.",
  "localize":"Leak is usually conceptualized at the oval or round window, creating abnormal communication between perilymphatic space and middle ear. Third-window disorders can mimic pressure/sound-induced symptoms.",
  "workup":"Use audiometry and vestibular assessment; CT is useful for trauma/third-window anatomy. There is no single highly reliable bedside test for idiopathic fistula, so diagnosis depends on context and exclusion of better explanations.",
  "manage":"Activity/pressure precautions and observation are reasonable in selected stable cases; urgent surgical exploration is considered for compelling traumatic leaks, progressive SNHL or severe persistent symptoms.",
  "operate":"Middle-ear exploration evaluates oval/round-window regions and allows sealing with soft tissue/fascia when a leak is suspected. Avoid excessive manipulation of the stapes/vestibule.",
  "teach":"Perilymph fistula is a clinical diagnosis with imperfect testing. The strongest cases have a credible pressure/trauma mechanism plus cochleovestibular change."},
 {"topic":"Cochlear Implant Failure / Revision",
  "recognize":"Declining performance, intermittency, pain, facial stimulation, loss of lock/telemetry, infection, extrusion or device integrity concerns after CI warrant systematic evaluation rather than immediate reimplantation.",
  "localize":"Failure may be external hardware/programming, electrode array migration/foldover, receiver-stimulator malfunction, soft failure, infection or biologic cochlear/neural limitation.",
  "workup":"Start with audiology/device integrity testing, programming review and history of performance change. Use imaging for suspected array migration/position problems and evaluate infection/skin integrity when present.",
  "manage":"Correct external/programming causes first. Revision/reimplantation is indicated for confirmed hard failure, unacceptable soft-failure phenotype after multidisciplinary review, infection/extrusion or mechanical electrode problems that cannot be corrected nonoperatively.",
  "operate":"Plan around prior scar, receiver pocket, mastoid/facial-recess anatomy and the possibility of cochlear fibrosis. Preserve cochlear access while removing the old array carefully and have a backup strategy for difficult reinsertion.",
  "teach":"A poor CI user is not automatically a failed implant. Separate device, electrode, programming and neural/rehabilitation causes before revision."},
 {"topic":"Congenital Inner-Ear Malformations",
  "recognize":"Congenital SNHL with characteristic CT/MRI abnormalities may reflect cochlear, vestibular, semicircular-canal, IAC or cochlear-nerve malformation; syndromic clues and CSF-gusher risk matter.",
  "localize":"Classify the malformation by which embryologic structure failed to develop normally and determine whether a functional cochlear nerve is present. Anatomy predicts both hearing potential and surgical risk.",
  "workup":"High-resolution temporal-bone CT defines bony labyrinth and IAC; MRI evaluates cochlear nerve and membranous/brain anatomy. Add genetics and syndromic evaluation when clinically appropriate.",
  "manage":"Amplification, CI or auditory brainstem implantation depends on residual hearing, cochlear anatomy and nerve presence. Early language access remains the functional priority.",
  "operate":"Expect abnormal facial-nerve course, difficult round-window access and increased CSF leak/gusher risk in selected malformations. Electrode choice and insertion strategy should match the malformed cochlea rather than a routine anatomy template.",
  "teach":"For congenital deafness, CT tells you the bony map and MRI tells you whether the nerve exists. Both matter before promising CI benefit."}
],
"Rhinology / Allergy / Skull Base":[
 {"topic":"Pediatric Chronic Rhinosinusitis",
  "recognize":"Persistent nasal obstruction/discharge and cough in a child for ≥12 weeks with objective disease suggests pediatric CRS; adenoid disease, allergy, asthma, reflux symptoms and recurrent viral illness commonly overlap.",
  "localize":"Disease involves sinonasal mucosa but the adenoid can act as an inflammatory/biofilm reservoir, especially in younger children. CF, PCD and immune deficiency change the phenotype.",
  "workup":"Confirm persistent symptoms and use nasal exam/endoscopy when feasible. CT is generally reserved for refractory disease or surgical planning; evaluate allergy, CF/PCD or immune disorder when history suggests unusually severe/recurrent disease.",
  "manage":"Saline and intranasal anti-inflammatory therapy are foundational; prolonged or repeated antibiotics should be phenotype-driven rather than automatic. Adenoidectomy is often the first surgical step in appropriate younger children before full FESS.",
  "operate":"If disease persists after appropriate medical/adenoid management, limited FESS is tailored to involved sinuses and age/anatomy. Protect orbit/skull base and preserve mucosa for long-term sinus development/function.",
  "teach":"Pediatric CRS is not simply adult CRS in a small nose. The adenoid and underlying systemic disease matter much more."},
 {"topic":"CF / Primary Ciliary Dyskinesia Sinonasal Disease",
  "recognize":"Early severe CRS, nasal polyposis, chronic wet cough, bronchiectasis, recurrent otitis or neonatal respiratory history should raise CF or PCD rather than isolated idiopathic CRS.",
  "localize":"Abnormal mucus composition or mucociliary clearance creates diffuse upper- and lower-airway disease; sinus disease is part of a systemic airway phenotype.",
  "workup":"Coordinate sweat/genetic testing for CF or specialized ciliary/nasal nitric oxide/genetic assessment for PCD when suspected. CT/endoscopy define sinonasal burden but do not establish the systemic diagnosis.",
  "manage":"Use aggressive saline/topical therapy and disease-specific pulmonary management. Antibiotics are culture/phenotype driven. Surgery may improve drainage/topical access but cannot correct the underlying clearance defect.",
  "operate":"FESS should create durable, maintainable cavities for irrigation while respecting pediatric anatomy; recurrence is common if postoperative topical therapy is not sustained.",
  "teach":"When CRS starts early and the lungs/ears are involved, think mucociliary disease. The sinus operation treats consequences, not the genetic mechanism."},
 {"topic":"Immunodeficiency-Associated Chronic Rhinosinusitis",
  "recognize":"Frequent bacterial sinus infections, pneumonia, unusual organisms, poor vaccine response or refractory CRS despite appropriate therapy should raise humoral or broader immune deficiency.",
  "localize":"The sinonasal disease is a consequence of impaired host defense rather than purely anatomic ostial obstruction; recurrent bacterial burden may coexist with structural disease.",
  "workup":"Use infection history to guide quantitative immunoglobulins and functional antibody assessment, with immunology referral when abnormalities or strong suspicion persist. Avoid indiscriminate immune panels in ordinary CRS.",
  "manage":"Optimize topical CRS therapy, culture-directed antibiotics and immune-specific treatment such as vaccination strategy or immunoglobulin replacement when indicated by immunology.",
  "operate":"FESS can improve drainage and topical access in refractory objective disease but should be integrated with immune management; surgery alone will not normalize infection susceptibility.",
  "teach":"Refractory CRS plus recurrent lower-airway infection is an immune-history problem before it is a bigger-surgery problem."},
 {"topic":"Olfactory Dysfunction",
  "recognize":"Separate conductive smell loss from inflammatory/neural loss and distinguish anosmia, hyposmia, parosmia and phantosmia. Sudden postviral loss and chronic CRS-associated loss have different trajectories.",
  "localize":"Conductive loss prevents odorant access to olfactory cleft; sensorineural loss reflects olfactory epithelium, bulb/tract or central pathways. Unilateral loss with neurologic or sinonasal red flags deserves targeted imaging.",
  "workup":"Use validated smell testing when diagnosis/severity matters, endoscopy for olfactory-cleft obstruction and imaging selectively for unilateral, traumatic, neurologic or tumor concern. Do not rely only on self-rated smell.",
  "manage":"Treat reversible sinonasal inflammation, counsel safety and use olfactory training for persistent postviral and other appropriate sensorineural loss. Steroid use should match an inflammatory phenotype rather than be universal.",
  "operate":"Surgery is appropriate only for a defined conductive/anatomic cause such as CRS/polyps or tumor; avoid sacrificing olfactory mucosa during skull-base/sinonasal procedures when smell preservation matters.",
  "teach":"Smell loss is localization: can odorant reach the cleft, and if it can, is the neuroepithelium/pathway working?"}
],
"Pediatric Otolaryngology":[
 {"topic":"Congenital Hearing Loss Genetics",
  "recognize":"Permanent congenital/early-onset SNHL should trigger etiologic thinking early because genetic diagnosis can predict progression, syndromic risks and cochlear-implant considerations.",
  "localize":"Genetic hearing loss may affect cochlear ion homeostasis, hair cells, synapses, auditory nerve or syndromic organ systems; phenotype and inheritance pattern guide testing.",
  "workup":"After diagnostic audiology, use comprehensive genetic testing with counseling as a high-yield etiologic tool; add CMV evaluation when age/timing permits and imaging selectively for anatomy/implant planning or syndromic clues.",
  "manage":"Ensure early language access through amplification, CI evaluation and educational support while the etiologic workup proceeds. A genetic result can guide surveillance of vision, thyroid, renal, cardiac or neurologic disease in syndromic conditions.",
  "operate":"Genetic diagnosis can affect CI prognosis—for example, disorders upstream of the cochlear nerve may respond differently than synaptopathy/nerve deficiency—so integrate genetics with imaging rather than using either alone.",
  "teach":"The goal of genetics is not just naming a mutation; it can predict progression, syndromic surveillance and expected auditory rehabilitation."},
 {"topic":"Cleft / Craniofacial Otologic-Airway Care",
  "recognize":"Children with cleft palate/craniofacial syndromes commonly have chronic OME/hearing loss, velopharyngeal dysfunction, nasal obstruction and sleep-disordered breathing that evolve with growth and reconstruction.",
  "localize":"Palatal muscle dysfunction impairs Eustachian-tube opening; craniofacial skeletal relationships affect nasal and pharyngeal airway; prior repairs alter surgical anatomy.",
  "workup":"Use serial audiology/otoscopy, speech/resonance assessment and sleep evaluation when symptoms warrant. Coordinate with cleft/craniofacial teams because ear, speech and airway decisions interact.",
  "manage":"Treat hearing loss proactively, use tubes when indicated, and coordinate VPI/airway treatment with speech outcomes. Avoid fixing one problem in a way that predictably worsens another.",
  "operate":"Adenoid surgery, pharyngeal flap/sphincter procedures and airway interventions require special attention to velopharyngeal competence and OSA risk. Ear surgery should anticipate chronic ET dysfunction.",
  "teach":"Cleft care is longitudinal systems care: ears, speech and sleep share the same altered anatomy."},
 {"topic":"Juvenile Recurrent Parotitis",
  "recognize":"Recurrent painful unilateral or bilateral parotid swelling in a child, often beginning in early childhood and resolving by adolescence, suggests juvenile recurrent parotitis after excluding suppurative infection, stones and autoimmune disease.",
  "localize":"The disorder affects intraparotid ductal/acinar function and can show sialectatic change; recurrent episodes do not necessarily imply a fixed obstructing stone.",
  "workup":"Ultrasound is useful to confirm parotid changes and exclude abscess/stone. Broader autoimmune/immunologic testing is selective for atypical, severe or systemic presentations.",
  "manage":"Acute episodes are treated with hydration, massage, analgesia and antibiotics only when bacterial infection is suspected. Recurrent severe disease may benefit from sialendoscopy with irrigation/dilation.",
  "operate":"Sialendoscopy is gland-preserving and favored over parotidectomy for refractory disease; identify stenotic/inflammatory ducts and avoid unnecessary gland sacrifice.",
  "teach":"Most children improve with age. The management goal is reducing morbidity while preserving the gland, not escalating every recurrence to surgery."},
 {"topic":"Pediatric Head & Neck Tumors",
  "recognize":"A persistent pediatric neck mass is more often inflammatory/congenital than malignant, but hard/fixed nodes, supraclavicular location, B symptoms, cranial neuropathy or progressive growth require oncologic evaluation.",
  "localize":"Use age and anatomic compartment to frame the differential: congenital tract/cyst, nodal disease, salivary/thyroid, vascular malformation, neural tumor or sarcoma.",
  "workup":"Ultrasound is often first-line for superficial masses; CT/MRI and tissue sampling are selected by depth/vascularity and malignancy risk. Avoid open biopsy before appropriate imaging and oncology planning when lymphoma/sarcoma is possible.",
  "manage":"Treatment is histology-specific and often multidisciplinary. Preserve long-term growth, cranial nerve, swallowing, hearing and endocrine function whenever oncologically safe.",
  "operate":"Plan biopsy/resection so the incision and tissue planes do not compromise definitive oncologic surgery; vascular lesions and skull-base tumors demand diagnosis before casual excision.",
  "teach":"In children, the wrong biopsy can complicate the right cancer operation. Diagnose the compartment and histology before cutting."}
],
"Laryngology / Voice / Swallowing":[
 {"topic":"Vocal Fold Sulcus / Scar",
  "recognize":"Persistent dysphonia with reduced mucosal wave, stiffness, spindle gap or a linear furrow despite otherwise normal mobility suggests sulcus/scar.",
  "localize":"The lesion disrupts the superficial lamina propria/vocal-ligament interface, impairing pliability even when gross glottic closure is acceptable.",
  "workup":"High-quality stroboscopy is essential to characterize mucosal-wave loss, closure and contralateral compensation. Voice assessment defines functional burden; imaging rarely diagnoses superficial scar.",
  "manage":"Voice therapy addresses compensatory hyperfunction but does not restore missing lamina propria. Injection/augmentation or scar-directed phonosurgery is individualized because predictable restoration of normal mucosal wave is difficult.",
  "operate":"Set realistic goals: improve closure and/or pliability without creating additional scar. Avoid repeated aggressive epithelial manipulation in a stiff fold.",
  "teach":"Scar is a material-property problem, not simply a gap. A perfectly medialized stiff fold may still vibrate poorly."},
 {"topic":"Vocal Process Granuloma",
  "recognize":"Posterior glottic granuloma on the vocal process often follows intubation, phonotrauma/throat clearing or laryngeal irritation and can cause throat discomfort, cough or dysphonia.",
  "localize":"The lesion forms over the cartilaginous posterior glottis where mechanical contact pressure is high; this differs from a membranous vocal-fold mass.",
  "workup":"Laryngoscopy establishes location; biopsy is reserved for atypical, progressive or suspicious lesions. Identify intubation history, hyperfunctional voice/cough and reflux-related symptoms without assuming reflux is always causal.",
  "manage":"Reduce mechanical trauma with voice/cough therapy and treat relevant inflammatory contributors. Many lesions regress without surgery; recurrence is common when the inciting behavior persists.",
  "operate":"Excision is reserved for airway compromise, diagnostic uncertainty or refractory symptomatic disease and should minimize further perichondrial trauma; adjunct botulinum toxin may be considered in selected recurrent contact lesions.",
  "teach":"If you remove the granuloma but leave the collision force, you have treated the consequence and preserved the cause."},
 {"topic":"Radiation-Associated Dysphagia",
  "recognize":"Progressive solid/liquid dysphagia, aspiration, residue, weight loss or recurrent pneumonia months to years after H&N RT can reflect fibrosis, neuropathy, xerostomia, stenosis or laryngeal dysfunction.",
  "localize":"Common mechanisms include reduced tongue-base drive, pharyngeal constrictor fibrosis, impaired hyolaryngeal excursion, reduced sensation and UES/cervical-esophageal stenosis.",
  "workup":"Use FEES/MBS to define swallow physiology and endoscopy/imaging when recurrence or structural stenosis is possible. Nutritional and pulmonary consequences are part of the severity assessment.",
  "manage":"Swallow therapy, diet/strategy modification, xerostomia/dental care and targeted dilation or glottic/UES intervention are selected by mechanism. Preventive/maintenance swallowing activity during treatment may reduce disuse but does not eliminate fibrosis risk.",
  "operate":"Dilation treats a stenotic segment but not global radiation fibrosis; aspiration-prevention surgery or functional laryngectomy is reserved for severe refractory pulmonary-threatening dysfunction after cancer control is confirmed.",
  "teach":"Post-radiation dysphagia is usually multimechanistic. Treat the demonstrated physiologic failure rather than repeatedly dilating every patient with trouble swallowing."},
 {"topic":"Aspiration-Prevention Surgery",
  "recognize":"Recurrent aspiration pneumonia, inability to protect the airway and failure of rehabilitation/less invasive procedures can make separation of airway and alimentary tract the primary goal.",
  "localize":"Determine whether aspiration is driven by sensory loss, glottic incompetence, global pharyngeal failure or an irreversibly nonfunctional larynx; this determines whether limited or definitive separation is needed.",
  "workup":"Confirm severity with instrumental swallowing assessment, pulmonary history, nutritional status and goals. Exclude recurrent cancer and correctable focal lesions before irreversible surgery.",
  "manage":"Maximize therapy, diet strategies, feeding modification and targeted procedures first when feasible. In life-threatening refractory aspiration, laryngotracheal separation, diversion or functional/total laryngectomy may provide pulmonary protection.",
  "operate":"These procedures intentionally sacrifice or bypass normal laryngeal airflow/voice to protect lungs. Preoperative counseling must include permanent stoma/voice rehabilitation implications and fistula/wound risk in irradiated patients.",
  "teach":"The endpoint is not a prettier swallow study; it is preventing pulmonary injury when the native larynx can no longer protect the airway."}
],
"Facial Plastics / Trauma":[
 {"topic":"Periocular Reconstruction",
  "recognize":"Eyelid defects threaten corneal protection, lid apposition, lacrimal drainage and cosmesis. The reconstruction is determined by lamella, horizontal extent and canthal involvement—not skin size alone.",
  "localize":"Separate anterior lamella (skin/orbicularis) from posterior lamella (tarsus/conjunctiva) and identify medial/lateral canthal or canalicular injury.",
  "workup":"Document visual function, globe injury, lid-margin loss, canthal tendon and lacrimal system before reconstruction. In oncologic defects, confirm margin strategy first.",
  "manage":"Small partial-thickness defects may close primarily; larger full-thickness defects require lamellar reconstruction using local flaps/grafts and stable canthal/lid-margin support.",
  "operate":"At least one reconstructed lamella should generally provide vascularized support when both are replaced. Avoid vertical tension that causes ectropion and restore a smooth margin against the cornea.",
  "teach":"Eyelid reconstruction is function first: protect the globe, restore margin/canthus, then optimize appearance."},
 {"topic":"Auricular Reconstruction",
  "recognize":"Auricular defects vary from skin-only loss to exposed cartilage, rim loss or composite framework injury; the ear's thin skin and three-dimensional cartilage contour limit simple closure.",
  "localize":"Identify helical rim, antihelix, concha, tragus and lobule involvement and whether cartilage support is missing. Posterior auricular skin provides useful local tissue.",
  "workup":"For trauma, assess avulsion viability and canal injury; for oncologic defects, establish margin control. Defect size, cartilage loss and subunit determine reconstruction.",
  "manage":"Options include secondary healing for selected concavities, full-thickness graft, local advancement/rotation flaps, Antia-Buch-type rim advancement and staged cartilage/framework reconstruction.",
  "operate":"Restore the cartilage framework before skin coverage when structural support is lost and avoid flattening the sulcus or narrowing the EAC.",
  "teach":"The ear is cartilage sculpture covered by thin skin. If you reconstruct skin without framework, the contour will fail."},
 {"topic":"Alar Retraction / Nasal Vestibular Stenosis",
  "recognize":"Alar notching/retraction or scar-related vestibular narrowing can cause visible deformity and external-valve obstruction, often after prior rhinoplasty, trauma or skin-cancer reconstruction.",
  "localize":"Determine whether the problem is missing lining, weak/retracted lateral crus, scar contracture, rim support loss or true vestibular skin deficiency.",
  "workup":"Examine at rest and inspiration, assess scar and cartilage support, and determine whether intranasal lining is deficient. Decongestion will not correct a fixed scar/structural narrowing.",
  "manage":"Mild dynamic collapse may respond to support strategies; fixed stenosis/retraction often requires scar release plus lining and/or cartilage support with prolonged stenting in selected cases.",
  "operate":"Recreate a patent vestibular lumen and stable alar margin using the tissue actually missing—lining graft/flap, rim/batten cartilage or lateral-crural repositioning—while avoiding overbulking.",
  "teach":"Alar retraction is not one deformity. Ask whether you lack lining, cartilage support or both before choosing the graft."},
 {"topic":"Static Facial Reanimation",
  "recognize":"When dynamic reinnervation is unavailable, delayed or insufficient, static procedures can improve eye protection, oral competence, nasal airflow and resting symmetry without restoring spontaneous movement.",
  "localize":"Target the functional deficit: upper-lid weight/eyelid tightening, brow ptosis, nasal-valve collapse or oral commissure descent.",
  "workup":"Document facial zones, corneal exposure, oral leakage/speech, nasal obstruction and patient priorities; dynamic options should still be considered based on denervation duration and donor availability.",
  "manage":"Combine therapy/eye care with targeted static support; procedures can complement rather than replace dynamic nerve/muscle reconstruction.",
  "operate":"Choose vectors that restore resting position without excessive tension. Common concepts include eyelid loading/canthoplasty, brow lift and fascia/tendon sling for oral/nasal support.",
  "teach":"Static reanimation does not make the face move—it makes the paralyzed face safer and more functional at rest."}
],
"Sleep Surgery":[
 {"topic":"HNS Troubleshooting / Nonresponse",
  "recognize":"Persistent symptoms, high residual AHI, discomfort, tongue deviation, poor nightly use or loss of benefit after HNS implantation requires troubleshooting before labeling the device a failure.",
  "localize":"Failure can reflect adherence/activation, programming, stimulation pattern, cuff/lead position, residual palatal/lateral-wall collapse, weight change or nonobstructive sleep events.",
  "workup":"Review objective device usage/settings and postoperative sleep testing, examine tongue motion and reassess airway phenotype; DISE with stimulation or imaging is selective for unexplained nonresponse.",
  "manage":"Optimize amplitude, electrode configuration, timing and comfort, address weight/nasal/PAP-combination needs and treat residual anatomic collapse. Revision is reserved for a defined hardware/anatomic problem.",
  "operate":"Before lead revision or repositioning, prove that programming and phenotype optimization cannot solve the problem. Revision carries hypoglossal, pleural, scar and device risks.",
  "teach":"HNS nonresponse is a systems problem: patient use + programming + anatomy + device integrity. Do not jump directly to revision."},
 {"topic":"Down Syndrome Pediatric HNS",
  "recognize":"Adolescents with Down syndrome may have severe persistent OSA after adenotonsillar treatment and poor PAP tolerance because of multilevel hypotonia/anatomic collapse.",
  "localize":"HNS targets tongue-base neuromuscular collapse; DISE is required to exclude complete concentric palatal collapse and identify whether the phenotype is appropriate.",
  "workup":"Current FDA labeling includes selected patients age 13–18 years with Down syndrome and severe OSA with AHI 10–50 who are not effectively treated by/are not candidates for adenotonsillectomy, cannot tolerate/effectively use PAP despite attempts, lack complete concentric palatal collapse, and have considered standard alternatives.",
  "manage":"Selection must occur in an experienced multidisciplinary pediatric sleep/airway program. Implantation is followed by healing, activation, titration and objective outcome assessment rather than immediate therapeutic effect.",
  "operate":"Technical principles mirror HNS implantation but require pediatric/anatomic consideration and careful branch selection, cuff placement and respiratory-sensing lead placement. Counsel regarding tongue weakness, discomfort, infection and revision.",
  "teach":"Pediatric Down-syndrome HNS is a narrow FDA-labeled rescue pathway for persistent severe OSA—not a replacement for adenotonsillectomy or PAP in routine pediatric OSA."},
 {"topic":"Central Sleep Apnea / Treatment-Emergent CSA",
  "recognize":"Central apnea is cessation/reduction of airflow with absent or reduced respiratory effort; it occurs in several phenotypes including heart failure/Cheyne-Stokes, opioid-related, medical-condition, high-altitude, primary and treatment-emergent CSA.",
  "localize":"Most CSA reflects unstable ventilatory control around the CO2 apneic threshold rather than upper-airway collapse. Hypoventilation disorders are mechanistically distinct and should not be mislabeled CSA.",
  "workup":"Use PSG pattern, medication/opioid history, cardiac/neurologic context and gas-exchange data to classify the cause. Persistent hypercapnia points toward hypoventilation rather than classic post-hyperventilation CSA.",
  "manage":"Treat the underlying condition and choose PAP/oxygen/acetazolamide/ASV or other therapy according to CSA phenotype and comorbidity. Current AASM guidance also includes transvenous phrenic-nerve stimulation as an option for selected persistent CSA.",
  "operate":"This is usually medical sleep management, not upper-airway surgery. The procedural advanced decision is recognizing when implantable phrenic-nerve stimulation is appropriate after phenotype-specific noninvasive therapy.",
  "teach":"Do not send central apnea to airway surgery. First ask whether respiratory effort is absent, why ventilatory control is unstable, and whether hypercapnia suggests a different hypoventilation disorder."},
 {"topic":"Sleep-Related Hypoventilation",
  "recognize":"Sustained nocturnal hypoventilation produces prolonged CO2 elevation/hypoxemia rather than discrete obstructive or central apneas and occurs with obesity hypoventilation, neuromuscular weakness, chest-wall disease or medication effects.",
  "localize":"The failure is inadequate alveolar ventilation from reduced drive or ventilatory pump capacity, not primarily pharyngeal collapse.",
  "workup":"Use PSG with CO2 monitoring when indicated, awake bicarbonate/ABG or other gas-exchange assessment, pulmonary/neuromuscular evaluation and medication review to identify the mechanism.",
  "manage":"Treat the underlying disorder, optimize weight/respiratory disease and use bilevel/noninvasive ventilation when ventilatory support is needed; supplemental oxygen alone can fail to correct hypoventilation and may worsen hypercapnia in susceptible patients.",
  "operate":"Upper-airway surgery has limited value when the dominant problem is ventilatory pump failure. Tracheostomy/ventilation or other procedures are reserved for selected severe airway/ventilation situations rather than routine OSA logic.",
  "teach":"Apnea is episodic; hypoventilation is sustained inadequate ventilation. CO2 is the clue that prevents misclassifying a pump problem as an obstructive throat problem."}
]}

_existing_v97={m["topic"] for mods in DEEP_MODULES_V6.values() for m in mods}
for _domain,_mods in NEW_DEPTH_MODULES_V97.items():
    for _m in _mods:
        if _m["topic"] not in _existing_v97:
            _m["primary_domain"]=_domain
            _m["tags"]=_tags_v94(_m["topic"],_domain)
            _m["evidence_calibrated"]="v9.7"
            DEEP_MODULES_V6.setdefault(_domain,[]).append(_m)
            _existing_v97.add(_m["topic"])

# -----------------------------------------------------------------------------
# Surgical Anatomy Atlas
# -----------------------------------------------------------------------------
ANATOMY_ATLAS_V97 = [
 {"region":"Otology / Neurotology","topic":"Temporal Bone Surgical Map","landmarks":["tegmen","sigmoid sinus","external auditory canal","digastric ridge","mastoid antrum","lateral semicircular canal","incus/fossa incudis","facial recess"],"danger":["facial nerve","labyrinth","dura/CSF","sigmoid sinus","jugular bulb"],"or_link":"Mastoidectomy","pearl":"Use constant boundaries—tegmen, sigmoid and EAC—before relying on variable air-cell anatomy."},
 {"region":"Otology / Neurotology","topic":"Middle Ear / Ossicular Anatomy","landmarks":["malleus","incus","stapes","oval window","round window","tensor tympani","pyramidal eminence","sinus tympani","facial recess"],"danger":["facial nerve","chorda tympani","stapes footplate/vestibule"],"or_link":"Ossiculoplasty","pearl":"The sinus tympani and facial recess are classic hidden disease spaces."},
 {"region":"Otology / Neurotology","topic":"Facial Nerve — Intratemporal Course","landmarks":["IAC","labyrinthine segment","geniculate ganglion","tympanic segment","second genu","mastoid segment","stylomastoid foramen"],"danger":["geniculate/labyrinthine narrow segment","dehiscent tympanic segment","mastoid segment during posterior tympanotomy"],"or_link":"Mastoidectomy","pearl":"At the second genu the nerve turns inferiorly just posterior to the oval-window region."},
 {"region":"Rhinology / Skull Base","topic":"Sinonasal Lateral Wall / Ostiomeatal Complex","landmarks":["uncinate","ethmoid bulla","hiatus semilunaris","natural maxillary ostium","middle turbinate basal lamella","lamina papyracea"],"danger":["orbit","nasolacrimal duct","skull base"],"or_link":"FESS","pearl":"Find the natural ostium rather than creating an accessory opening and recirculation."},
 {"region":"Rhinology / Skull Base","topic":"Frontal Recess Anatomy","landmarks":["agger nasi","frontal cells","uncinate insertion","ethmoid bulla","middle turbinate","lamina papyracea","frontal beak"],"danger":["anterior ethmoid artery","orbit","cribriform/lateral lamella"],"or_link":"Draf","pearl":"Frontal drainage is a three-dimensional pathway bounded by variable cells, not a single tube."},
 {"region":"Rhinology / Skull Base","topic":"Sphenoid / Central Skull Base","landmarks":["sphenoid ostium","superior turbinate","opticocarotid recess","sellar bulge","clival recess","vidian canal"],"danger":["optic nerve","internal carotid artery","cavernous sinus"],"or_link":"Sphenoidotomy","pearl":"CT defines whether optic nerve or carotid protrudes/dehisces into the sinus."},
 {"region":"Rhinology / Skull Base","topic":"Pterygopalatine / Infratemporal Spaces","landmarks":["sphenopalatine foramen","pterygopalatine fossa","foramen rotundum/V2","vidian canal","internal maxillary artery branches"],"danger":["V2","vidian nerve","maxillary artery","cavernous/skull-base extension pathways"],"or_link":"JNA","pearl":"The PPF is a neurovascular crossroads and a route of tumor/perineural spread."},
 {"region":"Head & Neck Oncology","topic":"Neck Levels / Fascial Compartments","landmarks":["levels I–VII","SCM","digastric","omohyoid","carotid sheath","prevertebral fascia"],"danger":["CN XI","hypoglossal","vagus","phrenic","sympathetic chain","thoracic duct"],"or_link":"Neck Dissection","pearl":"Nodal levels are oncologic maps laid over fascial and neurovascular anatomy."},
 {"region":"Head & Neck Oncology","topic":"Parapharyngeal / Retropharyngeal Spaces","landmarks":["styloid diaphragm","prestyloid fat","carotid space","retropharyngeal space","danger space"],"danger":["ICA","IJV","CN IX–XII","sympathetic chain","mediastinal spread"],"or_link":"Deep Neck Drainage","pearl":"Prestyloid versus poststyloid displacement patterns help identify tumor origin."},
 {"region":"Thyroid / Parathyroid / Salivary","topic":"Thyroid / RLN / EBSLN Anatomy","landmarks":["Berry ligament","tracheoesophageal groove","inferior thyroid artery","cricothyroid joint","superior pole vessels","tubercle of Zuckerkandl"],"danger":["RLN","EBSLN","parathyroid vascular supply"],"or_link":"Total Thyroidectomy","pearl":"The RLN's relationship to the inferior thyroid artery is variable; identify the nerve rather than relying on a single vessel rule."},
 {"region":"Thyroid / Parathyroid / Salivary","topic":"Parathyroid Embryology / Ectopic Map","landmarks":["superior glands from 4th pouch","inferior glands from 3rd pouch with thymus","thyrothymic ligament","tracheoesophageal groove","retroesophageal region"],"danger":["RLN","recurrent scar plane","mediastinal ectopia"],"or_link":"Parathyroidectomy","pearl":"Inferior glands migrate farther and therefore have more variable ectopic locations."},
 {"region":"Thyroid / Parathyroid / Salivary","topic":"Parotid / Facial Nerve Anatomy","landmarks":["tragal pointer","posterior belly digastric","tympanomastoid suture","stylomastoid foramen","pes anserinus","retromandibular vein"],"danger":["facial nerve branches","great auricular nerve","external carotid system"],"or_link":"Parotidectomy","pearl":"Use multiple landmarks to find the main trunk; no single surface landmark is perfectly reliable."},
 {"region":"Thyroid / Parathyroid / Salivary","topic":"Submandibular Triangle / Floor of Mouth","landmarks":["mylohyoid","hyoglossus","Wharton duct","lingual nerve","hypoglossal nerve","facial artery"],"danger":["lingual nerve","hypoglossal nerve","marginal mandibular nerve"],"or_link":"Submandibular Gland Excision","pearl":"The lingual nerve loops around the submandibular duct; the hypoglossal nerve lies deep to mylohyoid on hyoglossus."},
 {"region":"Laryngology / Voice / Swallowing","topic":"Laryngeal Framework / Intrinsic Muscles","landmarks":["thyroid cartilage","cricoid","arytenoids","cricothyroid joint","thyroarytenoid","PCA","LCA","interarytenoid","cricothyroid"],"danger":["RLN","EBSLN","posterior glottis"],"or_link":"Thyroplasty","pearl":"PCA is the sole true vocal-fold abductor; cricothyroid is primarily supplied by EBSLN."},
 {"region":"Laryngology / Voice / Swallowing","topic":"Pharynx / UES / Cervical Esophagus","landmarks":["superior/middle/inferior constrictors","Killian dehiscence","cricopharyngeus","cervical esophagus","tracheoesophageal party wall"],"danger":["RLN","deep neck/mediastinal contamination"],"or_link":"CP Myotomy","pearl":"Zenker arises above the cricopharyngeus through Killian dehiscence."},
 {"region":"Pediatric Otolaryngology","topic":"Pediatric Laryngotracheal Airway","landmarks":["supraglottis","posterior glottis","subglottis","cricoid","first tracheal rings","thyroid isthmus"],"danger":["RLNs","innominate artery","thin pediatric tracheal wall"],"or_link":"Pediatric LTR","pearl":"In children the cricoid is the complete cartilaginous ring governing fixed subglottic caliber."},
 {"region":"Facial Plastics / Trauma","topic":"Facial Buttresses / Midface Trauma","landmarks":["nasomaxillary buttress","zygomaticomaxillary buttress","pterygomaxillary buttress","frontozygomatic region","orbital rims"],"danger":["orbit","infraorbital nerve","lacrimal system","skull base"],"or_link":"ZMC ORIF","pearl":"Restoring facial projection requires three-dimensional buttress alignment, not just one visible fracture line."},
 {"region":"Facial Plastics / Trauma","topic":"Nasal Support / Valve Anatomy","landmarks":["septal L-strut","upper lateral cartilages","lower lateral cartilages","internal valve","external valve","piriform aperture"],"danger":["loss of dorsal/caudal support","alar retraction","valve collapse"],"or_link":"Functional Septorhinoplasty","pearl":"Name the structural failure before choosing spreader, batten, rim or septal-extension grafting."},
 {"region":"General ENT / Emergencies","topic":"Tracheostomy / Cervical Trachea Anatomy","landmarks":["cricoid","tracheal rings","thyroid isthmus","strap muscles","pretracheal fascia","innominate artery"],"danger":["posterior tracheal wall/esophagus","innominate artery","RLNs","pleura low in neck"],"or_link":"Tracheostomy","pearl":"A low tracheostomy increases proximity to the innominate artery; a fresh tract is not a safe blind pathway."},
 {"region":"Head & Neck Oncology","topic":"Oral Tongue / Floor of Mouth","landmarks":["intrinsic/extrinsic tongue muscles","lingual artery","hypoglossal nerve","lingual nerve","submandibular duct","mylohyoid"],"danger":["lingual artery","CN XII","mandibular periosteum","deep margin"],"or_link":"Oral Composite Resection","pearl":"Depth and deep-muscle involvement drive both oncologic margin and functional reconstruction."},
]

PUBLIC_EVIDENCE_V97 = [
 {"topic":"Down Syndrome Pediatric HNS","source":"FDA Inspire UAS P130008/S089 (2023; current device record updated 2026)","note":"Ages 13–18 with Down syndrome and severe OSA AHI 10–50 plus specific selection requirements."},
 {"topic":"Central Sleep Apnea / Treatment-Emergent CSA","source":"AASM Clinical Practice Guideline: Treatment of Central Sleep Apnea in Adults (2025)","note":"Phenotype-specific treatment and inclusion of transvenous phrenic nerve stimulation for selected CSA."},
]

# Rebuild Daily Path after v9.7 additions.
ADAPTIVE_ITEMS_V97=[]
for _domain,_mods in DEEP_MODULES_V6.items():
    for _m in _mods:
        _id=_v6_item_id(_domain,_m["topic"])
        for _stage in ["recognize","localize","workup","manage","operate","teach"]:
            ADAPTIVE_ITEMS_V97.append({
              "id":_id+"-"+_stage,"concept_id":_id,"domain":_domain,"topic":_m["topic"],
              "stage":_stage,"display_stage":"advanced" if _stage=="operate" else _stage,
              "prompt":{"recognize":"Recognize the pattern.","localize":"Localize the problem.","workup":"Evaluate it efficiently.","manage":"Build the management sequence.","operate":"Make the advanced decision.","teach":"Teach the mental model."}[_stage],
              "answer":_m[_stage],
              "minutes":{"recognize":3,"localize":3,"workup":4,"manage":4,"operate":6,"teach":4}[_stage],
              "level":{"recognize":1,"localize":2,"workup":3,"manage":4,"operate":5,"teach":6}[_stage],
              "tags":_m.get("tags",_tags_v94(_m["topic"],_domain))
            })
ADAPTIVE_ITEMS_V96=ADAPTIVE_ITEMS_V97
ADAPTIVE_ITEMS_V95=ADAPTIVE_ITEMS_V97
ADAPTIVE_ITEMS_V94=ADAPTIVE_ITEMS_V97
ADAPTIVE_ITEMS_V91=ADAPTIVE_ITEMS_V97


# =============================================================================
# ENT Mastery v9.8 — Legacy-Free Integration
# =============================================================================

# Canonical concept mapping for older case/attending identifiers so all modern
# learning modes write into the same deep-curriculum concept graph.
CONCEPT_ALIAS_TOPIC_V98 = {
 "primary_hyperparathyroidism":"Primary Hyperparathyroidism",
 "phpt_diagnosis":"Primary Hyperparathyroidism",
 "phpt_localization":"Primary Hyperparathyroidism",
 "phpt_operation":"Primary Hyperparathyroidism",
 "phpt_teaching":"Primary Hyperparathyroidism",
 "adult_osa_hns":"Hypoglossal Nerve Stimulation",
 "hns_selection":"Hypoglossal Nerve Stimulation",
 "hns_framework":"Hypoglossal Nerve Stimulation",
 "v5:hns":"Hypoglossal Nerve Stimulation",
 "airway_stenosis":"Subglottic / Tracheal Stenosis",
 "airway_strategy":"Subglottic / Tracheal Stenosis",
 "airway_teaching":"Subglottic / Tracheal Stenosis",
 "stenosis_description":"Subglottic / Tracheal Stenosis",
 "ssnhl":"Sudden Sensorineural Hearing Loss",
 "v5:ssnhl":"Sudden Sensorineural Hearing Loss",
 "meniere":"Ménière Disease",
 "v5:ménière_disease":"Ménière Disease",
 "bppv":"BPPV",
 "v5:bppv":"BPPV",
 "tympanostomy_tubes":"Tympanostomy Tube Indications",
 "cholesteatoma":"Chronic Otitis Media / Cholesteatoma",
 "v5:cholesteatoma":"Chronic Otitis Media / Cholesteatoma",
 "retrotympanic_mass":"Tinnitus",
 "adult_neck_mass":"Unknown Primary with Cervical Metastasis",
 "v5:adult_neck_mass":"Unknown Primary with Cervical Metastasis",
 "dysphonia":"Stroboscopy Interpretation",
 "epistaxis":"Epistaxis Surgical Control",
 "v5:epistaxis":"Epistaxis Surgical Control",
 "pediatric_tonsillectomy":"Pediatric OSA / Adenotonsillar Disease",
 "crs_fess":"CRS Phenotyping",
 "tympanoplasty":"Tympanic Membrane Perforation",
 "laryngomalacia":"Laryngomalacia",
 "pediatric_sgs":"Pediatric Subglottic Stenosis",
 "age_related_hearing_loss":"Age-Related Hearing Loss / Presbycusis",
 "salivary_gland_mass":"Pleomorphic Adenoma / Warthin Tumor",
 "thyroid_nodule":"Thyroid Nodule",
 "thyroidectomy":"Differentiated Thyroid Cancer",
 "thyroid_nodal_disease":"Central Neck Dissection",
 "afrs":"AFRS",
 "crs_biologics":"CRSwNP",
 "oral_cavity_scc":"Oral Tongue SCC",
 "parotidectomy":"Salivary Gland Malignancy",
 "mastoidectomy":"Chronic Otitis Media / Cholesteatoma",
 "septoplasty":"Functional Nasal Obstruction",
 "deep_neck_infection":"Deep Neck Space Infection",
 "tracheostomy":"Tracheostomy Emergency",
 "fess_landmarks":"Ethmoidectomy",
 "glottic_insufficiency":"Unilateral Vocal Fold Paralysis",
 "v5:hearing_physiology":"Audiogram Interpretation",
 "v5:tympanometry":"Tympanometry / Acoustic Reflexes",
 "v5:otosclerosis":"Otosclerosis / Stapes Fixation",
 "v5:facial_nerve":"Facial Paralysis",
 "v5:allergic_rhinitis":"Allergic Rhinitis",
 "v5:ars":"Acute Bacterial Rhinosinusitis",
 "v5:crs":"CRS Phenotyping",
 "v5:aerd":"AERD",
 "v5:csf_rhinorrhea":"CSF Rhinorrhea",
 "v5:oral_cavity_scc":"Oral Tongue SCC",
 "v5:neck_dissection":"Neck Dissection",
 "v5:laryngomalacia":"Laryngomalacia",
 "v5:injection_augmentation":"Injection Laryngoplasty",
 "v5:orbital_floor_fracture":"ZMC / Orbital Trauma",
 "v5:local_flap":"Local Flap Reconstruction",
 "v5:post-tonsil_bleed":"Post-Tonsillectomy Hemorrhage",
 "v5:deep_neck_infection":"Deep Neck Space Infection",
 "v5:tracheostomy_displacement":"Tracheostomy Emergency",
 "otoscopy_normal":"Audiogram Interpretation",
 "stroboscopy_basics":"Stroboscopy Interpretation",
}

# Explicit mapping for the 20 later progressive cases that were previously
# dumped into General ENT / Emergencies and disconnected from the concept graph.
INTEGRATED_CASE_TOPIC_V98 = {
 "v8-case-001":"Cochlear Implant Candidacy",
 "v8-case-002":"Temporal Bone Fracture",
 "v8-case-003":"Chronic Otitis Media / Cholesteatoma",
 "v8-case-004":"Revision FESS",
 "v8-case-005":"Invasive Fungal Rhinosinusitis",
 "v8-case-006":"Unknown Primary with Cervical Metastasis",
 "v8-case-007":"Laryngeal Preservation Decision",
 "v8-case-008":"Differentiated Thyroid Cancer",
 "v8-case-009":"Reoperative Hyperparathyroidism",
 "v8-case-010":"Salivary Gland Malignancy",
 "v8-case-011":"Pediatric Tracheostomy / Decannulation",
 "v8-case-012":"Recurrent Respiratory Papillomatosis",
 "v8-case-013":"Le Fort / Panfacial Trauma",
 "v8-case-014":"Post-Tonsillectomy Hemorrhage",
 "v8-case-015":"Deep Neck Space Infection",
 "v8-case-016":"Bilateral Vocal Fold Immobility",
 "v8-case-017":"Zenker Diverticulum",
 "v8-case-018":"Residual OSA After Surgery",
 "v8-case-019":"Functional Nasal Obstruction",
 "v8-case-020":"Orbital Complications of Sinusitis",
}

def _deep_concept_lookup_v98():
    out={}
    for _domain,_mods in DEEP_MODULES_V6.items():
        for _m in _mods:
            out[_m["topic"]]=(_v6_item_id(_domain,_m["topic"]),_domain)
    return out

def canonical_concept_id_v98(raw_id=None, domain=None, topic=None):
    lookup=_deep_concept_lookup_v98()
    target=topic or CONCEPT_ALIAS_TOPIC_V98.get(raw_id)
    if target in lookup:
        return lookup[target][0]
    # Already canonical.
    if raw_id in {x[0] for x in lookup.values()}:
        return raw_id
    return raw_id

def canonical_concept_domain_v98(raw_id=None, domain=None, topic=None):
    lookup=_deep_concept_lookup_v98()
    target=topic or CONCEPT_ALIAS_TOPIC_V98.get(raw_id)
    if target in lookup:
        return lookup[target][1]
    return canonical_domain_v94(domain)

# Normalize all progressive cases into real curriculum concepts/domains.
for _c in INTEGRATED_CASES:
    _topic=INTEGRATED_CASE_TOPIC_V98.get(_c.get("id")) or CONCEPT_ALIAS_TOPIC_V98.get(_c.get("concept_id"))
    if _topic:
        _c["legacy_concept_id"]=_c.get("concept_id")
        _c["concept_id"]=canonical_concept_id_v98(_c.get("concept_id"),_c.get("domain"),_topic)
        _c["domain"]=canonical_concept_domain_v98(_c.get("legacy_concept_id"),_c.get("domain"),_topic)
        _c["primary_domain"]=_c["domain"]

# Normalize Attending/Chief prompts too, so future mastery events join the same graph.
for _level,_prompts in ATTENDING_LEVEL_PROMPTS.items():
    for _p in _prompts:
        _old=_p.get("concept_id")
        _new=canonical_concept_id_v98(_old,_p.get("domain"))
        if _new!=_old:
            _p["legacy_concept_id"]=_old
            _p["concept_id"]=_new
            _p["domain"]=canonical_concept_domain_v98(_old,_p.get("domain"))

# Interpretation Atlas remains granular, but each lab gets a canonical parent concept
# used for unified learner analytics.
LAB_PARENT_TOPIC_V98 = {
 "audiology":"Audiogram Interpretation",
 "pathology":"Adverse Pathology and Adjuvant Therapy",
 "ct-mri":"Head & Neck Cancer Surveillance / Second Primaries",
 "laryngeal-endoscopy":"Stroboscopy Interpretation",
 "sinonasal-endoscopy":"Nasal Anatomy for Endoscopy",
 "airway-bronchoscopy":"Subglottic / Tracheal Stenosis",
 "sleep":"Adult PSG Interpretation",
 "vestibular":"Vestibular Test Battery",
 "thyroid-ultrasound":"Thyroid Nodule",
 "temporal-bone-imaging":"Temporal Bone Anatomy",
 "head-neck-imaging":"Unknown Primary with Cervical Metastasis",
 "swallowing-imaging":"Dysphagia / Aspiration",
 "otoscopy":"Audiogram Interpretation",
}
LAB_PARENT_CONCEPT_V98 = {
    _slug:canonical_concept_id_v98(topic=_topic)
    for _slug,_topic in LAB_PARENT_TOPIC_V98.items()
}

CURRENT_EVIDENCE_CATALOG_V98 = [
 {"area":"Otology / Audiology","title":"AAO-HNSF Sudden Hearing Loss (Update)","year":"2019","kind":"CPG","status":"active management source"},
 {"area":"Otology / Audiology","title":"AAO-HNSF Age-Related Hearing Loss","year":"2024","kind":"CPG","status":"active management source"},
 {"area":"Pediatric Otolaryngology","title":"AAO-HNSF Tympanostomy Tubes in Children (Update)","year":"2022","kind":"CPG","status":"active management source"},
 {"area":"Pediatric Otolaryngology","title":"AAO-HNSF Tonsillectomy in Children (Update)","year":"2019","kind":"CPG","status":"active management source"},
 {"area":"Rhinology","title":"AAO-HNSF Adult Sinusitis (Update)","year":"2025","kind":"CPG","status":"active management source"},
 {"area":"Rhinology","title":"AAO-HNSF Surgical Management of Chronic Rhinosinusitis","year":"2025","kind":"CPG","status":"active management source"},
 {"area":"Thyroid","title":"American Thyroid Association Differentiated Thyroid Cancer Guideline","year":"2025","kind":"Guideline","status":"active management source"},
 {"area":"Sleep","title":"AASM Treatment of Central Sleep Apnea in Adults","year":"2025","kind":"CPG","status":"active management source"},
 {"area":"Sleep","title":"FDA Inspire UAS labeling / expansions","year":"2023–2026","kind":"Regulatory labeling","status":"device-criteria source; payer rules may differ"},
 {"area":"Head & Neck Oncology","title":"ASCO Management of the Neck in Oral Cavity/Oropharyngeal SCC","year":"2019","kind":"Guideline","status":"active management source"},
 {"area":"Head & Neck Oncology","title":"ASCO Transoral Robotic Surgery in Oropharyngeal SCC","year":"2025","kind":"Guideline","status":"active management source"},
 {"area":"Head & Neck Oncology","title":"ISOO-MASCC-ASCO Osteoradionecrosis Guideline","year":"2024","kind":"Guideline","status":"active management source"},
 {"area":"Cutaneous Oncology","title":"American Academy of Dermatology skin cancer guidelines","year":"current public guidance","kind":"Guideline set","status":"BCC/cSCC/melanoma framework"},
 {"area":"Cutaneous Oncology","title":"NCI PDQ Merkel Cell Carcinoma","year":"current public guidance","kind":"Evidence summary","status":"Merkel treatment framework"},
 {"area":"Trauma","title":"AO Surgery Reference — CMF Trauma","year":"living reference","kind":"Surgical reference","status":"fracture mechanics / approach framework"},
 {"area":"Core / Operative","title":"Cummings Otolaryngology—Head and Neck Surgery","year":"7th ed.","kind":"Core textbook","status":"scope/anatomy/operative reference; content incorporated only from user-provided material or permitted sources"},
 {"area":"Interpretation","title":"Color Atlas of Otoscopy + permitted open atlases","year":"various","kind":"Visual references","status":"pattern-recognition source layer"},
]


# =============================================================================
# ENT Mastery v9.9 — Pre-Cummings Textbook Saturation + Anatomy Expansion
# =============================================================================
# Sources used for scope/depth in this pass:
# - K.J. Lee's Essential Otolaryngology, 12th ed.
# - Pasha: Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6th ed.
# - Bluestone & Stool's Pediatric Otolaryngology, 5th ed.
# - Operative Otolaryngology—Head and Neck Surgery, 3rd ed.
# - Operative Techniques in Laryngology, 2nd ed. (2024)
# - Surgical Anatomy of the Head and Neck (Janfaza et al.)
# - Atlas of Head & Neck Surgery
# - Atlas of Endoscopic Sinus and Skull Base Surgery, 2nd ed.
#
# The prose below is original educational synthesis. Textbook wording is not copied.

FOUNDATION_MODULES_V99 = [
 {"topic":"ENT Perioperative Anesthesia / Difficult Airway Planning",
  "recognize":"ENT surgery often shares the airway with anesthesia, so the operative plan must account for anticipated difficult mask ventilation/intubation, airway tumor/stenosis, bleeding, aspiration risk, prior radiation and whether the surgeon needs unobstructed access to the larynx/pharynx.",
  "localize":"Define the threatened level—oral cavity/oropharynx, supraglottis, glottis, subglottis, trachea or extrinsic neck compression—and whether obstruction is fixed, dynamic or distorted by positioning/sedation.",
  "workup":"Review prior airway records, flexible examination/imaging when relevant, mouth opening/neck mobility, oxygenation/ventilation reserve and the planned surgical exposure. A difficult airway plan should include primary technique, backup device/route and front-of-neck rescue before induction.",
  "manage":"Coordinate awake versus asleep airway strategy, spontaneous versus controlled ventilation, neuromuscular blockade and extubation plan with anesthesia. High-risk extubation is a second difficult-airway event and may require staged extubation, ICU monitoring or temporary tracheostomy.",
  "operate":"The surgeon must be prepared for emergency surgical airway and understand how suspension laryngoscopy, laser, rigid bronchoscopy, tracheostomy and head/neck tumors change ventilation options. Never let the surgical position or drapes eliminate rescue access.",
  "teach":"The key OR question is not simply 'Can anesthesia intubate?' It is: where is the obstruction, what happens after sedation/paralysis, and what is the mutually agreed rescue sequence?"},
 {"topic":"Hemostasis / Coagulopathy / Antithrombotic Management in ENT",
  "recognize":"Mucosal ENT procedures can bleed substantially even when routine laboratory values are normal. Medication history, inherited bleeding disorders, liver/renal disease and prior surgical bleeding history can matter more than an isolated screening test.",
  "localize":"Hemostasis depends on platelet function, coagulation factors, fibrin stability and local vessel control. Different operations carry very different consequences of bleeding: tonsillar fossa, neck hematoma, intracranial/skull base and airway bleeding are especially high stakes.",
  "workup":"Take a focused bleeding and antithrombotic history and order testing when history, disease or planned procedure warrants it. Do not reflexively obtain broad coagulation panels in every healthy patient with no bleeding history.",
  "manage":"Balance thrombosis risk against procedural bleeding risk when holding or restarting anticoagulant/antiplatelet therapy; involve the prescribing service for high-risk indications. Correct clinically important coagulopathy and ensure blood products/reversal strategy are available when needed.",
  "operate":"Meticulous local control includes exposure, bipolar/monopolar/ligature/clips/topical adjuncts chosen for anatomy and thermal risk. In the neck or airway, secure hemostasis before closure and recognize that postoperative bleeding can rapidly become an airway emergency.",
  "teach":"A normal INR is not a complete bleeding assessment, and 'stop all blood thinners' is not a safe universal rule. Match the hemostatic plan to patient thrombosis risk and the consequence of bleeding in that operation."},
 {"topic":"ENT Fluids / Electrolytes / Nutrition",
  "recognize":"Major head/neck patients are vulnerable to dehydration, malnutrition, refeeding problems, electrolyte derangement and aspiration-related nutritional failure. Pediatric tonsillectomy, cancer surgery and prolonged dysphagia create very different fluid/nutrition problems.",
  "localize":"Identify whether the deficit is intake failure, swallowing dysfunction, GI access problem, renal/endocrine loss or catabolic demand. Calcium disturbance after thyroid/parathyroid surgery and sodium abnormalities after skull-base surgery require operation-specific thinking.",
  "workup":"Assess weight trend, oral intake, swallowing safety, basic electrolytes/renal function and targeted calcium/magnesium/phosphate or nutrition labs when clinically indicated. Severe malnutrition should be recognized before major oncologic reconstruction.",
  "manage":"Use enteral nutrition when the GI tract is functional, choose NG/PEG/other access according to expected duration and aspiration/anatomy, replace electrolytes deliberately and monitor for refeeding in high-risk patients.",
  "operate":"Feeding access, salivary diversion and reconstruction should be planned with anticipated postoperative swallow rather than added reactively after failure. In endocrine surgery, calcium/PTH strategy is part of discharge planning.",
  "teach":"Nutrition is not supportive trivia in ENT—it changes wound healing, pulmonary complications, treatment tolerance and readiness for reconstruction."},
 {"topic":"Antimicrobial Stewardship in Otolaryngology",
  "recognize":"Many ENT complaints are viral, inflammatory or obstructive rather than bacterial. Purulence alone does not automatically require systemic antibiotics, and chronic disease often needs source control or topical therapy rather than repeated empiric courses.",
  "localize":"Match drug delivery to the infected compartment: external canal, middle ear, sinus, deep neck space, salivary gland, postoperative wound or skull base. Topical therapy can achieve high local concentrations in selected accessible sites.",
  "workup":"Use diagnosis and severity first; obtain culture when disease is severe, recurrent, unusual, immunocompromised, postoperative or failing appropriate empiric therapy. Imaging is for suspected complications/source control, not to prove every uncomplicated infection.",
  "manage":"Choose the narrowest reasonable empiric coverage, adjust to culture and local resistance, and define duration by syndrome and source control. Avoid antibiotics for uncomplicated viral URI, uncomplicated OME or noninfectious CRS phenotypes.",
  "operate":"Drain abscesses and remove infected foreign material or devitalized tissue when antibiotics cannot achieve source control. The antibiotic plan after drainage should reflect organism, residual infection and host factors rather than a fixed ritual duration.",
  "teach":"The stewardship question is: what bacterial syndrome am I treating, what compartment is it in, and do I need source control? If those are unclear, the antibiotic choice is premature."},
 {"topic":"Cranial Nerve Examination / Skull Base Localization",
  "recognize":"Multiple cranial neuropathies, progressive unilateral sensory/motor deficits, dysphagia/dysphonia or tongue/shoulder weakness can localize head-and-neck pathology before imaging is reviewed.",
  "localize":"Use patterns: cavernous sinus/orbital apex (III, IV, V1/V2, VI), jugular foramen (IX–XI), hypoglossal canal (XII), parapharyngeal/carotid space (IX–XII and sympathetic chain), IAC/CPA (VII/VIII), and skull-base foraminal pathways.",
  "workup":"Perform and document a complete directed cranial-nerve exam, then choose imaging that follows the suspected nerve course from brainstem/skull base through neck. Audiometry, laryngoscopy or swallow testing may provide objective end-organ function.",
  "manage":"Treat the underlying lesion, but protect function immediately—cornea, airway/swallow, shoulder and nutrition may require intervention while the diagnostic workup proceeds.",
  "operate":"Preoperative deficits must be documented before skull-base, parotid, neck-dissection and vagal/sympathetic-space surgery because postoperative examination determines whether a deficit is new and may affect reconstruction.",
  "teach":"Cranial nerves are a localization map. A resident should be able to turn the pattern of deficits into a predicted skull-base or neck compartment before opening the MRI."},
 {"topic":"ENT Imaging Fundamentals",
  "recognize":"CT and MRI answer different anatomic questions. CT excels at bone, air spaces, calcification and acute fracture; MRI is superior for soft tissue, marrow, intracranial extension, perineural spread and many skull-base lesions.",
  "localize":"Interpret studies by compartments and surgical boundaries rather than by radiology vocabulary alone: orbit, skull base, carotid space, parapharyngeal space, deep neck spaces, temporal bone, sinonasal drainage pathways and nodal levels.",
  "workup":"Order the study that answers a clinical question: temporal-bone CT for bony labyrinth/ossicles, contrast MRI for nerve/skull-base spread, CTA for vascular injury or relationship, ultrasound for superficial thyroid/salivary/nodal questions.",
  "manage":"Imaging should change diagnosis, staging, operative access or surveillance. Avoid redundant studies when prior imaging already answers the question, but obtain dedicated protocols when general head CT/MRI is inadequate for surgical planning.",
  "operate":"Before entering the OR, personally review side, extent, vascular variants, skull-base height, orbit, carotid/jugular relationships and any anatomy that changes exposure or bailout strategy.",
  "teach":"Do not ask 'What does the scan show?' Ask 'What decision am I trying to make, and which imaging characteristic answers it?'"},
 {"topic":"Wound Healing / Scar Biology in Head & Neck Surgery",
  "recognize":"Wound failure can result from tension, ischemia, infection, radiation injury, salivary contamination, malnutrition, hematoma/seroma or poor patient factors; hypertrophic scar and keloid are distinct excessive-healing phenotypes.",
  "localize":"Healing proceeds through inflammatory, proliferative and remodeling phases. Tissue vascularity and mechanical tension determine whether a closure, graft or flap is likely to survive.",
  "workup":"Before revision, identify why the wound/scar failed: infection, exposed hardware, fistula, recurrent tumor, radiation damage, tension vector or patient predisposition. Do not treat every widened scar as a surface problem.",
  "manage":"Optimize moisture/clean care, infection control, nutrition and tension; use silicone, steroid, laser or other scar treatments selectively. Delay elective scar revision until remodeling and the underlying mechanical problem are understood.",
  "operate":"Use atraumatic handling, appropriate layered closure and everted tension-controlled skin edges. In hostile beds, import vascularized tissue rather than repeatedly closing ischemic irradiated tissue under tension.",
  "teach":"Good scar treatment starts before the incision: incision placement, blood supply and tension matter more than a late cosmetic rescue."},
 {"topic":"Grafts / Implants / Biomaterials in ENT",
  "recognize":"ENT reconstruction uses autograft, allograft and synthetic materials for support, lining, volume, ossicular conduction and implants. Material choice should match mechanical demand, infection risk and long-term biologic behavior.",
  "localize":"Cartilage, fascia, bone, skin, nerve graft, vascularized flap and prosthetic implants each behave differently in mucosal, cutaneous, middle-ear and irradiated environments.",
  "workup":"Define what is missing—structure, lining, cover, conductivity, nerve continuity or volume—and the quality of the recipient bed. Prior infection/radiation and contamination may make permanent foreign material less attractive.",
  "manage":"Prefer the simplest durable material that restores function with acceptable donor morbidity. Counsel about resorption, extrusion, infection, calcification, warping and revision according to material/site.",
  "operate":"Prepare a well-vascularized, tension-free recipient bed; avoid exposed implant edges and dead space. In contaminated or irradiated fields, vascularized autologous tissue often has a biologic advantage.",
  "teach":"Choose a material by the job it must perform, not by habit. Support, lining, conduction and soft-tissue replacement are different reconstructive problems."},
 {"topic":"Systemic / Granulomatous Disease Manifestations in ENT",
  "recognize":"Persistent crusting, septal perforation, subglottic stenosis, salivary enlargement, chronic otitis, facial paralysis, oral lesions or cervical adenopathy can be the presenting manifestation of systemic autoimmune, granulomatous, infectious or infiltrative disease.",
  "localize":"Patterns such as destructive sinonasal disease plus airway stenosis, multisite glandular disease or multiple cranial neuropathies suggest a systemic process rather than isolated local pathology.",
  "workup":"Use history/exam to target serology, chest/renal evaluation, biopsy and infectious testing rather than ordering broad panels indiscriminately. Biopsy the safest active site when tissue diagnosis is needed.",
  "manage":"Coordinate disease-specific immunologic/infectious/oncologic therapy while treating local functional consequences. Avoid irreversible local surgery during uncontrolled destructive inflammatory disease unless airway or other urgent function requires it.",
  "operate":"Surgery is often reconstructive or rescue rather than curative; active vasculitis/granulomatous disease increases restenosis and wound-failure risk. Time elective reconstruction to disease control when possible.",
  "teach":"When ENT disease appears in multiple unrelated sites, stop creating separate diagnoses and ask whether one systemic process connects them."},
 {"topic":"Laser / Energy Safety in Otolaryngology",
  "recognize":"Laser and electrosurgical energy introduce specific risks: airway fire, eye injury, tissue penetration/thermal spread, plume and ignition of drapes/tubes/oxygen-rich environments.",
  "localize":"Risk depends on wavelength/tissue absorption and where energy is delivered—laryngeal airway, skin, sinonasal/skull base or vascular mucosa. Nearby nerves, vessels and cartilage can be injured without direct contact.",
  "workup":"Before use, confirm indication, wavelength/device settings, eye protection, smoke evacuation and airway-fire plan. In airway laser surgery, coordinate inspired oxygen concentration and laser-safe tube/technique with anesthesia.",
  "manage":"Use the lowest effective energy, intermittent activation and visible target control. If airway fire occurs: stop gas/laser, remove burning material/tube, extinguish, re-establish ventilation and evaluate airway injury.",
  "operate":"Understand line-of-sight, backstop and thermal penetration before activation. Keep wet pledgets/appropriate protection where indicated and never activate an unvisualized energy device near critical structures.",
  "teach":"Energy is a surgical instrument with invisible injury potential. The resident should know both the tissue effect and the emergency response before stepping on the pedal."},
 {"topic":"Common ENT Consult Triage / Disposition",
  "recognize":"ENT consultation is often about urgency rather than diagnosis alone: airway compromise, uncontrolled hemorrhage, orbital/vision threat, intracranial spread, deep-space infection, sudden hearing loss and postoperative complications demand different timelines.",
  "localize":"First identify the threatened function—airway, vision, brain/skull base, major vessel, hearing, swallowing/nutrition or facial nerve—then localize the responsible compartment.",
  "workup":"Obtain only studies that influence immediate disposition and treatment. Stable outpatient problems, urgent same-day evaluation and true OR/ICU emergencies should not be managed with the same diagnostic tempo.",
  "manage":"Stabilize first, call the correct services early and decide admission/OR/transfer based on physiologic threat, not merely a named diagnosis. Clear return precautions are part of disposition for patients managed outpatient.",
  "operate":"When definitive treatment may be needed, avoid temporizing steps that complicate later surgery—for example casual incision of an undiagnosed neck mass, repeated traumatic airway manipulation or uncontrolled biopsy of vascular lesions.",
  "teach":"Every consult answer should include three things: what is it, what can deteriorate, and what happens next if the patient worsens."},
]

_existing={m["topic"] for mods in DEEP_MODULES_V6.values() for m in mods}
for _m in FOUNDATION_MODULES_V99:
    if _m["topic"] not in _existing:
        _m["primary_domain"]="General ENT / Emergencies"
        _m["tags"]=_tags_v94(_m["topic"],"general otolaryngology perioperative resident foundations")
        _m["evidence_calibrated"]="v9.9-textbook-saturation"
        DEEP_MODULES_V6["General ENT / Emergencies"].append(_m)
        _existing.add(_m["topic"])

TRUE_DEPTH_REWRITES_V99 = {
"Tympanometry / Acoustic Reflexes":{
 "recognize":"Type A tympanogram reflects near-normal middle-ear pressure/compliance; type B is flat and requires ear-canal volume interpretation; type C indicates negative middle-ear pressure. Acoustic reflex presence/absence adds information about the conductive pathway, cochlea, CN VIII, brainstem and CN VII.",
 "localize":"A conductive lesion can abolish measured reflexes by preventing stimulus delivery or recording of stapedius contraction. Retrocochlear/facial-nerve patterns depend on which ear is stimulated and which ear records the response.",
 "workup":"Interpret tympanometry with otoscopy and audiogram. For a type B tracing, normal canal volume suggests middle-ear effusion while large volume suggests a patent tube/perforation; small volume suggests probe obstruction or canal occlusion.",
 "manage":"Use immittance to refine diagnosis rather than treating the tracing itself. It can confirm effusion, support ossicular/tympanic pathology and identify when additional retrocochlear/facial evaluation is needed.",
 "operate":"Preoperative middle-ear assessment helps determine whether a conductive hearing deficit is due to effusion, TM, ossicles or ventilation. After tube placement, a large-volume flat tympanogram can confirm a patent pathway.",
 "teach":"Never say 'type B equals fluid' without checking canal volume. Tympanometry measures mechanics; reflex testing interrogates a neural-mechanical arc."},
"Ossicular Discontinuity":{
 "recognize":"Large conductive air-bone gap after trauma, chronic ear disease or surgery with relatively normal TM/pressure suggests ossicular discontinuity; hypercompliant tympanometry can support but does not prove it.",
 "localize":"Common disruptions involve incudostapedial joint, long process of incus, malleus/incus fixation or erosion around cholesteatoma. Stapes superstructure and footplate status determine reconstruction options.",
 "workup":"Use otoscopy and complete audiometry; temporal-bone CT may show gross discontinuity but small joint defects can be missed. Definitive diagnosis is sometimes operative.",
 "manage":"Observe or amplify if functional burden is acceptable; reconstruct when hearing benefit is expected and the middle ear is safe/aerated enough for durable mechanics.",
 "operate":"Reconstruction depends on malleus, stapes superstructure, footplate mobility, TM position and middle-ear space. PORP/TORP, cartilage and autologous ossicle techniques should create stable coupling without excessive pressure on the stapes.",
 "teach":"Ossiculoplasty succeeds when mechanics and middle-ear environment are favorable. A technically perfect prosthesis in a poorly ventilated scarred ear may fail."},
"Superior Canal Dehiscence":{
 "recognize":"Sound- or pressure-induced vertigo/oscillopsia, autophony, internal body-sound amplification and an apparent low-frequency conductive gap with intact middle ear suggest a third-window syndrome.",
 "localize":"Dehiscence of the superior semicircular canal creates an additional compliant inner-ear window, altering cochlear and vestibular mechanics despite normal ossicles/TM.",
 "workup":"Use audiometry, VEMP physiology and high-resolution reformatted temporal-bone CT aligned to the superior canal. Imaging alone is insufficient because thin bone/dehiscence can be incidental.",
 "manage":"Observe mild symptoms and counsel trigger avoidance; consider surgical plugging/resurfacing for disabling, physiologically confirmed syndrome after excluding mimics such as patulous ET and ossicular disease.",
 "operate":"Approach can be middle fossa or transmastoid depending on anatomy and goals. Protect membranous labyrinth and recognize the risk of hearing/vestibular change after repair.",
 "teach":"Third-window disease can mimic conductive hearing loss with a normal middle ear. Symptoms + physiology + dedicated CT must agree before surgery."},
"Vestibular Neuritis":{
 "recognize":"Acute prolonged spontaneous vertigo lasting days with nausea, gait imbalance and no new hearing loss or focal neurologic deficit suggests vestibular neuritis, but posterior-circulation stroke is the dangerous mimic.",
 "localize":"The disorder is an acute unilateral vestibular hypofunction, often affecting superior vestibular-nerve pathways. Hearing loss points toward labyrinthitis or another cochleovestibular process rather than pure neuritis.",
 "workup":"Use bedside ocular-motor/head-impulse examination in an appropriate acute vestibular syndrome and obtain MRI/neurologic evaluation when central features, vascular risk or examination uncertainty exists.",
 "manage":"Short-course vestibular suppressants/antiemetics are for the severe initial period only; begin early mobilization and vestibular rehabilitation. Prolonged suppressants delay central compensation.",
 "operate":"There is no operative role. Advanced management is recognizing failure to compensate, recurrent symptoms suggesting another diagnosis, or central red flags rather than escalating to vestibular ablation.",
 "teach":"Acute vestibular syndrome is a stroke-localization problem first and a symptom-control problem second. Hearing should remain intact in classic neuritis."},
"Tinnitus":{
 "recognize":"Classify tinnitus as pulsatile versus nonpulsatile, unilateral versus bilateral and bothersome versus incidental. Unilateral pulsatile tinnitus, objective bruit, asymmetric hearing loss or focal neurologic findings deserve focused evaluation.",
 "localize":"Nonpulsatile tinnitus usually reflects auditory-system activity associated with hearing loss; pulsatile tinnitus can arise from arterial, venous, middle-ear or intracranial pressure mechanisms.",
 "workup":"Obtain audiometry for persistent unilateral/bothersome tinnitus. Pulsatile tinnitus requires exam and targeted vascular/temporal-bone/intracranial imaging based on phenotype; routine imaging is unnecessary for symmetric nonpulsatile tinnitus with symmetric hearing.",
 "manage":"Treat remediable ear/hearing disease, provide hearing aids when indicated and use education/sound strategies/cognitive-behavioral approaches for bothersome chronic tinnitus. Avoid unsupported supplements as routine therapy.",
 "operate":"Surgery/endovascular treatment is reserved for a demonstrated structural vascular or middle-ear cause, not for primary subjective tinnitus.",
 "teach":"The first branch point is pulsatile or not. That single distinction radically changes the differential and imaging strategy."},
"Vestibular Test Battery":{
 "recognize":"Vestibular testing should answer a localization/functional question rather than be ordered as a fixed panel for every dizzy patient.",
 "localize":"VNG/calorics emphasize low-frequency horizontal canal/superior nerve function, vHIT evaluates high-frequency semicircular-canal VOR, VEMP assesses otolith pathways and posturography reflects integrated balance rather than a single end organ.",
 "workup":"Choose tests from the suspected disorder and interpret discordant findings physiologically. Normal testing does not exclude vestibular migraine/PPPD, and an abnormal test may represent a compensated old lesion rather than the current symptom generator.",
 "manage":"Use results to guide rehabilitation, document unilateral/bilateral loss, support third-window/otolith diagnoses or decide whether destructive vestibular treatment is safe.",
 "operate":"Before vestibular-ablative surgery, confirm the target ear and contralateral reserve; before CI/skull-base surgery, baseline function can help counsel about postoperative imbalance.",
 "teach":"Know what frequency and organ each test interrogates. 'Abnormal VNG' is not a diagnosis."},
"CRSsNP":{
 "recognize":"CRS without polyps is ≥12 weeks of compatible symptoms plus objective sinonasal inflammation without visible polyposis. Facial pressure alone or an abnormal CT without symptoms is not sufficient.",
 "localize":"Disease may be diffuse inflammatory, odontogenic, anatomic/recurrent or associated with immune/ciliary disorders. Localized unilateral disease deserves a separate differential.",
 "workup":"Use endoscopy and/or CT to confirm objective disease; evaluate odontogenic, immune, ciliary or fungal contributors when phenotype suggests them. Culture is selective for refractory purulence.",
 "manage":"Saline irrigation and topical intranasal corticosteroid therapy are foundational; additional medical therapy is individualized. Surgery is considered when symptoms/objective disease persist and expected benefit outweighs alternatives.",
 "operate":"FESS should open the involved natural drainage pathways and create access for topical therapy while preserving mucosa. Extent is individualized rather than defined by a mandatory maximal-surgery template.",
 "teach":"CRSsNP is a chronic inflammatory diagnosis with objective evidence. Repeated antibiotics without confirming phenotype is not a longitudinal plan."},
"CRSwNP":{
 "recognize":"Bilateral inflammatory nasal polyps with congestion, smell loss and objective CRS define CRSwNP; asthma/AERD and type-2 inflammatory features predict recurrence and influence biologic discussions.",
 "localize":"Polyps arise from chronically inflamed sinonasal mucosa, often ethmoid-predominant, and can obstruct multiple drainage pathways. Unilateral 'polyp' is a different diagnostic problem until proven benign.",
 "workup":"Document endoscopic/CT burden, smell and quality-of-life effects, prior systemic steroid/surgery history and comorbid asthma/AERD. Evaluate atypical unilateral, bleeding or destructive lesions for neoplasm.",
 "manage":"Topical corticosteroid irrigation/spray is foundational; short systemic steroid courses are selective. Surgery and biologic therapy are chosen from disease burden, recurrence, systemic comorbidity and prior treatment rather than as mutually exclusive pathways.",
 "operate":"Surgery removes obstructing inflammatory tissue and creates durable topical access; preserve landmarks/mucosa and plan postoperative anti-inflammatory maintenance because surgery does not eliminate the type-2 tendency.",
 "teach":"The long-term question is disease control, not whether polyps can be removed. Always pair the operation with a postoperative inflammatory strategy."},
"AFRS":{
 "recognize":"Young atopic patient with severe polyposis, thick eosinophilic allergic mucin and expansile heterogeneous sinus opacification suggests allergic fungal rhinosinusitis rather than invasive fungal disease.",
 "localize":"AFRS is an inflammatory hypersensitivity phenotype with noninvasive fungal elements in allergic mucin; expansion can remodel bone and displace orbit/skull base without tissue invasion.",
 "workup":"Use endoscopy/CT, pathology of allergic mucin/fungal elements and atopic context. Bone erosion does not automatically mean invasive fungal infection; tissue invasion defines invasive disease.",
 "manage":"Surgery clears obstructing allergic mucin and establishes topical access, followed by intensive topical corticosteroid therapy and selective systemic/allergy-directed treatment.",
 "operate":"Open involved sinuses widely enough to remove dense mucin and permit surveillance/irrigation while protecting thinned orbit/skull base from expansile remodeling.",
 "teach":"AFRS is fungal-associated inflammation without invasion. Do not confuse dramatic bone remodeling with angioinvasive fungal sinusitis."},
"Mucocele":{
 "recognize":"Expansile obstructed sinus lesion causing pressure, proptosis, diplopia, frontal headache or bony remodeling suggests mucocele, often after prior surgery/trauma or chronic frontal disease.",
 "localize":"A mucocele is a mucus-filled epithelium-lined expanded sinus behind an obstructed drainage pathway; frontal/ethmoid lesions can threaten orbit and skull base.",
 "workup":"CT defines bony expansion and drainage anatomy; MRI is useful when lesion contents, intracranial/orbital soft tissue or tumor differential is uncertain.",
 "manage":"Symptomatic/expansile mucoceles are generally treated by surgical marsupialization and restoration of drainage rather than complete stripping of sinus mucosa.",
 "operate":"Create a durable opening into the nasal cavity, preserve orbit/skull base and address the cause of obstruction. Frontal anatomy may require extended approaches for a stable neo-ostium.",
 "teach":"The operation is drainage and durable marsupialization, not cyst enucleation from a thin skull-base/orbital shell."},
"Sinonasal Malignancy":{
 "recognize":"Unilateral obstruction/bleeding, facial numbness, loose teeth, orbital symptoms, cranial neuropathy or destructive unilateral imaging should be considered malignant until tissue diagnosis proves otherwise.",
 "localize":"Define the epicenter and extension to orbit, skull base/dura, pterygopalatine/infratemporal fossae, cranial nerves and cervical nodes. These compartments determine resectability and approach.",
 "workup":"Perform endoscopy, contrast CT/MRI and safe biopsy after considering vascular/skull-base lesions. Histology is essential because treatment differs substantially among SCC, adenocarcinoma, melanoma, esthesioneuroblastoma and other entities.",
 "manage":"Use multidisciplinary treatment based on histology/stage: surgery plus radiation is common for resectable epithelial disease, while some histologies favor different systemic/radiation strategies.",
 "operate":"Select endoscopic, open or combined approach for oncologic access and margin control, with skull-base/orbital reconstruction planned before resection. Minimally invasive access is not a reason to compromise oncologic boundaries.",
 "teach":"Sinonasal oncology is anatomy plus histology. Never let 'sinus mass' become a treatment plan before biopsy and compartmental staging."},
"Neck Dissection":{
 "recognize":"Neck dissection is a compartment-oriented oncologic operation used for clinically involved nodes, selected elective nodal risk or salvage—not simply removal of palpable lymph nodes.",
 "localize":"Know nodal levels I–VII and boundaries plus relationships to SCM, carotid sheath, CN XI, hypoglossal/vagus/phrenic/sympathetic chain, brachial plexus and thoracic duct.",
 "workup":"Map nodal burden with examination/imaging and define which levels are at risk from the primary site. Prior radiation/surgery, carotid involvement and contralateral disease alter operative planning.",
 "manage":"Choose selective versus more comprehensive dissection based on primary, nodal stage and treatment context; postoperative RT/CRT depends on pathology such as extranodal extension and margins.",
 "operate":"Preserve CN XI, IJV and SCM when oncologically safe; protect hypoglossal, vagus, phrenic, sympathetic chain and thoracic duct. En bloc compartmental clearance is preferred to nodal 'plucking.'",
 "teach":"A selective neck dissection is still oncologic when the selected levels match the disease. The resident must know every level boundary and what nerve/vessel is endangered there."},
"HPV-Associated Oropharyngeal SCC":{
 "recognize":"Adult neck mass may be the first presentation of HPV-associated tonsil/base-of-tongue SCC; the primary can be small or occult. Cystic level II nodes in an adult are metastatic until proven otherwise.",
 "localize":"Primary sites are palatine tonsil and lingual tonsil/base of tongue with characteristic cervical nodal spread. HPV-mediated staging is biologically distinct from HPV-negative disease.",
 "workup":"Obtain tissue diagnosis with p16/HPV-appropriate testing, contrast imaging and chest/distant staging as indicated; evaluate the oropharynx thoroughly and assess swallowing, dental and treatment-related functional issues.",
 "manage":"Curative therapy may be radiation-based or surgery/TORS-based depending on stage, anatomy, exposure and expected functional/adjuvant burden. Avoid assuming transoral surgery automatically reduces treatment intensity.",
 "operate":"TORS requires safe exposure and ability to obtain meaningful margins without unacceptable neurovascular/functional morbidity; neck management and hemorrhage planning are part of the operation.",
 "teach":"In an adult with a cystic neck node, do not perform 'branchial cyst excision' before excluding HPV-associated oropharyngeal SCC."},
"Laryngeal SCC":{
 "recognize":"Persistent dysphonia, odynophagia, dysphagia, hemoptysis, otalgia or airway symptoms require laryngeal visualization; glottic cancers often present earlier with voice change than supraglottic disease.",
 "localize":"Stage by subsite, vocal-fold mobility, paraglottic/pre-epiglottic space, cartilage invasion and extralaryngeal extension; nodal risk differs greatly by glottic versus supraglottic lymphatics.",
 "workup":"Flexible exam plus direct laryngoscopy/biopsy and contrast imaging define primary extent; chest staging, nutrition and swallow/airway assessment are added according to stage.",
 "manage":"Early disease can often be treated with single-modality transoral surgery or radiation; advanced disease requires larynx-preservation CRT versus total laryngectomy/surgery based on resectability, cartilage/function and patient factors.",
 "operate":"Surgical choices range from transoral laser/partial laryngeal procedures to total laryngectomy with neck treatment and reconstruction. Oncologic control must be balanced against a realistic functional larynx.",
 "teach":"Organ preservation is not the same as functional preservation. A tumor-free but chronically aspirating obstructed larynx may be an unsuccessful organ outcome."},
"Unknown Primary with Cervical Metastasis":{
 "recognize":"Metastatic SCC in a cervical node without obvious mucosal primary requires a structured search, especially for HPV-associated oropharynx and EBV-associated nasopharynx based on pathology and nodal pattern.",
 "localize":"Nodal level and viral markers guide the likely primary site; cystic upper-jugular nodes strongly suggest oropharynx while retropharyngeal/posterior patterns may suggest nasopharynx or other sites.",
 "workup":"Obtain FNA/core with appropriate p16/HPV/EBV assessment, high-quality mucosal exam and cross-sectional/PET imaging as appropriate. Directed examination under anesthesia with tonsillar/lingual-tonsil evaluation can identify occult primaries.",
 "manage":"Treatment fields and surgery depend on whether a primary is found, nodal burden and viral status. Identifying the primary can reduce unnecessary mucosal treatment and tailor surgery/radiation.",
 "operate":"Neck dissection and transoral diagnostic/therapeutic procedures should be coordinated rather than performed as unrelated steps. Avoid open excisional node biopsy before proper workup when possible.",
 "teach":"The goal is not merely to prove the neck node is SCC—it is to find the primary or narrow the likely mucosal source enough to treat intelligently."},
"Oral Tongue SCC":{
 "recognize":"Persistent ulcer, induration, pain, bleeding, tongue dysfunction or ipsilateral otalgia warrants biopsy. Depth of invasion and deep-muscle involvement influence nodal risk and treatment.",
 "localize":"Map lateral/ventral oral tongue, floor-of-mouth proximity, intrinsic/extrinsic muscle involvement, mandible and neurovascular structures; oral tongue is distinct from base of tongue/oropharynx.",
 "workup":"Biopsy, contrast imaging for deeper disease and careful neck staging are central. Pathology should include depth, margins, PNI/LVI and nodal features that drive adjuvant therapy.",
 "manage":"Resectable oral-cavity SCC is commonly treated surgically with appropriate elective/therapeutic neck management; adjuvant RT/CRT is selected from adverse pathologic features.",
 "operate":"Obtain a three-dimensional deep margin while preserving function when oncologically safe; anticipate defect/reconstruction and neck recipient-vessel needs before resection.",
 "teach":"For oral tongue cancer, depth and deep margin matter. A superficial-looking ulcer can have meaningful occult nodal risk."},
"Central Neck Dissection":{
 "recognize":"Central compartment dissection is therapeutic for clinically involved level VI/VII thyroid-cancer nodes; it is not automatically required for every papillary thyroid carcinoma.",
 "localize":"Level VI lies between carotids from hyoid to innominate/suprasternal region and contains prelaryngeal, pretracheal and paratracheal nodes alongside RLNs and parathyroid blood supply.",
 "workup":"Use preoperative neck ultrasound and selective CT for bulky/retrotracheal/mediastinal disease; document vocal-fold function when nerve involvement or reoperation is a concern.",
 "manage":"Treat clinically involved central disease compartmentally and coordinate lateral-neck disease separately. Prophylactic dissection is individualized rather than a default response to microscopic risk.",
 "operate":"Identify and preserve RLN and viable parathyroid glands/vascular supply while clearing the nodal compartment; avoid isolated node plucking in a scar-prone central neck.",
 "teach":"The morbidity is hypoparathyroidism and RLN injury, so the indication must be oncologically meaningful—not simply 'there might be microscopic nodes.'"},
"Submandibular Sialolithiasis":{
 "recognize":"Meal-related submandibular pain/swelling strongly suggests obstructive sialolithiasis, especially with a palpable floor-of-mouth stone or reduced ductal saliva.",
 "localize":"Wharton duct runs from deep gland around posterior mylohyoid into floor of mouth, closely related to lingual nerve; stones may be distal palpable ductal, hilar or intraglandular.",
 "workup":"Ultrasound or noncontrast CT can localize radiopaque stones; sialendoscopy provides direct intraductal assessment. Consider stricture or chronic sialadenitis when no stone is found.",
 "manage":"Hydration, massage and sialogogues help mild episodes; antibiotics are for superimposed infection. Gland-preserving transoral or endoscopic stone removal is favored when feasible.",
 "operate":"Distal stones can be removed transorally; hilar/proximal stones may need combined sialendoscopic/transoral techniques. Protect lingual nerve and avoid gland excision when a duct-preserving solution is realistic.",
 "teach":"Stone location determines the operation. A palpable anterior duct stone should not automatically become submandibular-gland excision."},
"Graves Disease / Toxic Goiter":{
 "recognize":"Hyperthyroid symptoms with diffuse goiter, ophthalmopathy or toxic multinodular disease create a thyroid problem where endocrine control and airway/compressive anatomy both matter.",
 "localize":"Diffuse hypervascular gland or multinodular enlargement can distort RLN/parathyroid relationships and compress/deviate trachea; substernal extension changes exposure.",
 "workup":"Confirm thyroid function and etiology, assess goiter size/nodules and laryngeal/airway symptoms, and obtain imaging when substernal/compressive anatomy requires it.",
 "manage":"Antithyroid medication, radioiodine and surgery are chosen by etiology, gland size, ophthalmopathy, pregnancy considerations, compressive symptoms, malignancy concern and patient preference.",
 "operate":"Achieve safe thyroidectomy after adequate medical preparation, control hypervascular superior/inferior pedicles and preserve RLN/EBSLN/parathyroids. Large/substernal glands require careful airway and thoracic-access planning.",
 "teach":"Do not take an uncontrolled thyrotoxic patient electively to thyroidectomy. The surgery starts with endocrine preparation."},
"Recurrent Respiratory Papillomatosis":{
 "recognize":"Recurrent exophytic papillomatous laryngeal lesions causing dysphonia and sometimes airway symptoms suggest HPV-related RRP; juvenile disease can be especially aggressive.",
 "localize":"Disease commonly affects true/false folds and can involve multiple aerodigestive sites. Repeated surgery can create scar/web and worsen voice independent of papilloma burden.",
 "workup":"Flexible/endoscopic examination defines burden and airway; biopsy confirms pathology and excludes dysplasia/malignant change when atypical. Track disease course and prior procedures rather than treating each recurrence as isolated.",
 "manage":"Goal is functional disease control, not complete mucosal eradication at any cost. Repeated endoscopic debulking and selected adjuvant therapy are individualized for aggressive/high-burden disease.",
 "operate":"Use microdebrider/laser or other precise techniques while preserving normal epithelium/commissure and minimizing thermal injury. Treat airway-threatening disease first and avoid bilateral opposing raw surfaces that promote web.",
 "teach":"RRP is chronic disease management. An aggressive 'remove every last lesion' operation can trade papilloma for permanent scar."},
"Velopharyngeal Insufficiency":{
 "recognize":"Hypernasality, nasal air emission and reduced oral pressure after cleft/palatal or neuromuscular disease suggests velopharyngeal dysfunction; distinguish structural insufficiency from mislearning/articulation errors.",
 "localize":"Closure depends on palate length/motion, lateral pharyngeal-wall motion and posterior wall; gap pattern and size determine procedure selection.",
 "workup":"Perceptual speech evaluation plus nasendoscopy and/or videofluoroscopy defines closure pattern. Sleep history matters because pharyngeal surgery can worsen OSA.",
 "manage":"Speech therapy treats articulation/mislearning but not a structural gap. Surgery or prosthetic management is selected for persistent structural dysfunction according to closure pattern and airway risk.",
 "operate":"Pharyngeal flap, sphincter pharyngoplasty, palatal lengthening/Furlow-type procedures and augmentation solve different patterns. Preserve an airway appropriate to the patient's baseline OSA risk.",
 "teach":"Treat the closure pattern, not just the word 'hypernasal.' A good speech operation can be a bad sleep operation if airway risk is ignored."},
"Spasmodic Dysphonia":{
 "recognize":"Task-specific strained/strangled voice breaks on voiced speech suggest adductor laryngeal dystonia; breathy breaks on voiceless contexts suggest abductor phenotype. Tremor and muscle-tension dysphonia are common mimics/comorbidities.",
 "localize":"This is focal neurologic dystonia affecting task-specific laryngeal motor control rather than a structural vocal-fold lesion.",
 "workup":"Diagnosis is clinical with expert voice evaluation and laryngoscopy during provocative speech; no single imaging or EMG test confirms typical disease, but atypical neurologic findings warrant broader assessment.",
 "manage":"Botulinum toxin injection is standard symptomatic treatment for many patients, with dose/muscle/laterality individualized over repeated cycles; voice therapy helps compensatory behaviors but does not cure dystonia.",
 "operate":"Targeted chemodenervation requires accurate muscle selection and counseling about transient breathiness, dysphagia and variable duration. Surgical denervation procedures are uncommon/selective.",
 "teach":"Spasmodic dysphonia is task-specific. Listen to the phonetic context of the break instead of diagnosing every strained voice as dystonia."},
"Medialization Thyroplasty":{
 "recognize":"Persistent symptomatic glottic insufficiency from unilateral paralysis, atrophy or selected defects can be treated with permanent framework medialization when recovery and symptom trajectory justify it.",
 "localize":"The implant moves the membranous vocal fold medially through a thyroid-cartilage window; posterior gap or vertical mismatch may require arytenoid adduction in addition.",
 "workup":"Stroboscopy/voice and swallow assessment define closure pattern; establish etiology and expected nerve recovery. Temporary injection is often preferable early when spontaneous recovery remains likely.",
 "manage":"Choose therapy, injection, thyroplasty, arytenoid procedure or reinnervation based on gap, aspiration, vocal demand, time course and patient goals.",
 "operate":"Perform under local/light sedation when possible to permit voice tuning, create a safe window without violating inner perichondrium excessively and shape the implant to correct the actual gap without airway compromise.",
 "teach":"Thyroplasty moves a fold; it does not restore nerve tone. If the posterior glottis is the main problem, a larger implant is not always the answer."},
"Posterior Glottic Stenosis / Arytenoid Fixation":{
 "recognize":"Bilateral vocal-fold immobility after prolonged intubation with posterior commissure scar or fused cricoarytenoid joints suggests posterior glottic stenosis, which can mimic bilateral RLN paralysis.",
 "localize":"Scar can bridge the interarytenoid/posterior commissure and progress to cricoarytenoid fixation. The pathology is mechanical restriction rather than absent motor input.",
 "workup":"Flexible laryngoscopy documents motion; history and CT/EMG are selective. Direct laryngoscopy with palpation of arytenoid joints may be required to distinguish fixation from paralysis.",
 "manage":"Mild scar may be treated endoscopically; more advanced fixation may require posterior scar release, dilation, grafting, cordotomy/arytenoid procedures or open reconstruction according to airway and voice goals.",
 "operate":"Avoid repeated traumatic posterior glottic injury. During reconstruction, create stable posterior airway while minimizing new opposing raw surfaces and balancing aspiration/voice tradeoffs.",
 "teach":"Before calling bilateral immobility 'bilateral paralysis,' palpate the joints if the history suggests posterior scar."},
"Cricopharyngeal Dysfunction":{
 "recognize":"Cervical solid/liquid dysphagia, residue at the UES, regurgitation or aspiration can result from impaired cricopharyngeal opening, but poor pharyngeal propulsion can create a similar radiographic appearance.",
 "localize":"The UES is a high-pressure zone centered on cricopharyngeus with contributions from adjacent inferior constrictor/cervical esophagus; opening depends on relaxation plus hyolaryngeal excursion and bolus-driving pressure.",
 "workup":"MBS/VFSS defines opening and pharyngeal physiology; endoscopy and manometry are selective. Diagnose true outflow restriction before cutting a sphincter in a patient whose main problem is weak propulsion.",
 "manage":"Dilation, botulinum toxin or myotomy can be used in selected focal UES dysfunction; treatment of neurologic/global pharyngeal disease and rehabilitation may be more important when restriction is secondary.",
 "operate":"Endoscopic/open myotomy must divide the dysfunctional muscle sufficiently while avoiding esophageal perforation, mediastinitis and RLN injury.",
 "teach":"A cricopharyngeal bar is a radiographic sign, not automatically the cause of dysphagia. Treat physiology, not the image."},
"Nasal Fracture":{
 "recognize":"Post-traumatic deformity, obstruction, epistaxis and tenderness suggest nasal fracture, but the immediate must-not-miss finding is septal hematoma.",
 "localize":"Assess nasal bones, upper lateral cartilages, septum and caudal support; associated NOE/orbital/midface injury changes management.",
 "workup":"Diagnosis is primarily clinical. CT is reserved for suspected complex facial fractures rather than isolated simple nasal injury. Document preinjury appearance/airway when possible.",
 "manage":"Drain septal hematoma urgently. Observe nondisplaced fractures; perform closed reduction within an appropriate edema/timing window when displaced and function/cosmesis warrant it.",
 "operate":"Mobilize the bony/cartilaginous framework without creating new support injury and stabilize internally/externally as needed. Recognize fractures unlikely to be corrected by closed reduction alone.",
 "teach":"If you remember only one emergency pearl: look for a septal hematoma before sending a nasal-fracture patient home."},
"NOE Fracture":{
 "recognize":"Flattened/widened nasal bridge, telecanthus, severe midface injury or epiphora after central facial trauma suggests naso-orbito-ethmoid fracture.",
 "localize":"The key structure is the medial canthal tendon attachment to the central fragment; injury also involves medial orbital walls, nasal bones/frontal process and lacrimal system.",
 "workup":"Thin-cut CT defines comminution and central fragment; document globe/vision, intercanthal distance and lacrimal injury. Classify by medial canthal tendon attachment because it guides reconstruction.",
 "manage":"Displaced unstable fractures require open reduction/fixation and restoration of medial canthal position; associated frontal sinus/skull-base and orbital injuries are managed concurrently.",
 "operate":"Rebuild central facial projection and intercanthal width with stable bony fixation; repair/resuspend the medial canthal tendon when its bony attachment is disrupted.",
 "teach":"NOE surgery is about the medial canthus and central facial framework. A good-looking nasal bone reduction with persistent telecanthus is a failed repair."},
"Frontal Sinus Fracture":{
 "recognize":"Frontal impact with anterior-table deformity, posterior-table injury, CSF leak or nasofrontal drainage-tract injury requires a decision based on each component rather than fracture presence alone.",
 "localize":"Evaluate anterior table, posterior table/dura and frontal sinus outflow tract. The long-term risks are contour deformity, mucocele and intracranial infection/CSF complications.",
 "workup":"High-resolution CT defines displacement, posterior-table comminution and drainage pathway; assess for CSF leak and associated intracranial/orbital injuries.",
 "manage":"Observe selected nondisplaced injuries with intact drainage; repair contour deformity when needed and choose sinus-preserving, obliteration or cranialization strategies according to outflow/posterior-table/dural injury.",
 "operate":"The operation must create a durable future: restore contour, eliminate unsafe mucosa when obliterating/cranializing and establish or intentionally remove the drainage pathway.",
 "teach":"Frontal sinus fracture is three decisions: anterior table, posterior table and outflow tract. Treat those, not the CT label."},
"Adult PSG Interpretation":{
 "recognize":"Read the study as physiology, not only AHI: sleep time/stages, obstructive versus central events, oxygen burden, arousals, position/REM dependence, CO2 when measured and cardiac/limb findings.",
 "localize":"PSG quantifies sleep-disordered breathing but does not directly localize anatomic collapse. Obstructive events imply continued respiratory effort; central events have absent/reduced effort.",
 "workup":"Confirm study quality and total sleep time before accepting indices. Distinguish OSA severity from hypoventilation and central apnea, and note REM/positional clustering that can affect treatment choice.",
 "manage":"Use PSG with symptoms/comorbidity to select PAP, oral appliance, weight/positional therapy or surgical evaluation. Residual study interpretation should determine whether remaining events are obstructive, central or due to inadequate use/settings.",
 "operate":"Sleep-surgery planning requires anatomy/DISE in addition to PSG. The AHI does not tell you whether the palate, tongue base, lateral wall or epiglottis is the surgical target.",
 "teach":"AHI is one column, not the whole sleep study. Always tell me event type, oxygen burden and whether disease is positional/REM dependent."},
"Palatal Surgery":{
 "recognize":"Palatal surgery is considered for selected OSA when retropalatal/lateral-wall anatomy contributes to collapse and nonoperative options are inadequate or undesired.",
 "localize":"Differentiate anteroposterior velar collapse, tonsillar crowding and lateral pharyngeal-wall collapse; these phenotypes are not corrected equally by tissue-resection versus reconstructive techniques.",
 "workup":"Review PSG, tonsils/palate anatomy, BMI/comorbidity, PAP history and DISE when it changes procedure selection or HNS candidacy.",
 "manage":"Choose a procedure that matches collapse pattern and counsel that improvement rather than cure may be realistic; postoperative PSG is appropriate when residual disease risk remains.",
 "operate":"Protect velopharyngeal function and major vessels, control tonsillar/pharyngeal bleeding and avoid excessive scar/nasopharyngeal narrowing. Reconstructive lateral-wall techniques differ conceptually from classic ablative UPPP.",
 "teach":"Sleep surgery is phenotype surgery. 'UPPP' should not be a reflex answer for every retropalatal obstruction."},
"Oral Appliance Therapy":{
 "recognize":"Mandibular-advancement oral appliances are a non-PAP treatment option for selected OSA/snoring patients, especially when PAP is not tolerated or an alternative is preferred.",
 "localize":"Advancing the mandible/tongue increases retrolingual/retropalatal airway dimensions but does not correct every collapse phenotype.",
 "workup":"Confirm OSA with sleep testing, evaluate dentition/TMJ and use a qualified dental sleep provider for fitting/titration. Objective follow-up sleep testing is needed because symptom improvement alone does not prove control.",
 "manage":"Titrate to efficacy/tolerance and monitor dental occlusion, TMJ symptoms and adherence. Severe disease or persistent hypoxemia may require PAP, surgery or combined therapy.",
 "operate":"No surgery is inherent to oral-appliance therapy; the advanced decision is recognizing when craniofacial anatomy makes MMA or another definitive skeletal strategy more appropriate than indefinite appliance advancement.",
 "teach":"An oral appliance is prescribed therapy, not an over-the-counter snoring device. It needs dental assessment, titration and objective efficacy testing."},
"Peritonsillar Abscess":{
 "recognize":"Severe unilateral sore throat, trismus, muffled voice, drooling and soft-palate/peritonsillar bulge suggest PTA; uvular deviation supports but is not required.",
 "localize":"Infection lies in the peritonsillar space between tonsillar capsule and superior constrictor; deeper parapharyngeal spread or airway symptoms change urgency.",
 "workup":"Diagnosis is usually clinical; ultrasound or CT is useful when exam is equivocal, deep-space complication is suspected or the patient cannot be examined adequately.",
 "manage":"Provide drainage when a drainable abscess is present, antibiotics covering common aerobic/anaerobic flora, hydration/analgesia and airway assessment. Selected patients can be managed outpatient if stable and tolerating intake.",
 "operate":"Needle aspiration or incision/drainage should respect carotid depth/lateral direction; avoid blindly directing instruments laterally. Quinsy tonsillectomy is selective rather than routine.",
 "teach":"Trismus plus unilateral peritonsillar swelling is the pattern. Before draining, know where the carotid is relative to your instrument."},
"Ludwig Angina":{
 "recognize":"Rapidly progressive bilateral submandibular/floor-of-mouth swelling, tongue elevation, drooling and muffled voice—often odontogenic—suggest Ludwig angina and can deteriorate into airway obstruction quickly.",
 "localize":"Cellulitis spreads through sublingual/submandibular spaces across the midline, elevating the tongue; early disease may be diffuse without a discrete abscess.",
 "workup":"Airway assessment is first. Contrast CT is obtained only if the patient is stable enough and helps identify drainable abscess, dental source and deeper spread.",
 "manage":"Secure the airway early when threatened, start IV broad-spectrum antibiotics and obtain dental/source control. Observation in an unmonitored setting is inappropriate for progressive airway signs.",
 "operate":"Drain discrete collections and address odontogenic source; airway may require awake intubation or surgical airway depending on anatomy and expertise. Avoid repeated traumatic oral attempts in a critically narrowed floor-of-mouth airway.",
 "teach":"Ludwig angina is an airway diagnosis before it is an antibiotic diagnosis."},
"Angioedema":{
 "recognize":"Rapid tongue/lip/oropharyngeal swelling with or without urticaria can be histaminergic or bradykinin-mediated; stridor, voice change, drooling and progressive tongue/floor-of-mouth involvement signal airway risk.",
 "localize":"Flexible laryngoscopy helps determine whether edema is limited anteriorly or involves tongue base, supraglottis/larynx. Mechanism matters because bradykinin-mediated disease responds poorly to epinephrine/antihistamines/steroids.",
 "workup":"Treat clinically while identifying medication exposure (ACE inhibitor), allergy/anaphylaxis features, hereditary history and airway progression. Do not delay airway management for laboratory confirmation.",
 "manage":"Histaminergic/anaphylactic disease requires IM epinephrine plus appropriate adjuncts; bradykinin-mediated disease uses mechanism-specific therapy when available and discontinuation of culprit medication. Monitor based on airway level/progression.",
 "operate":"Prepare an awake airway or surgical airway when progression threatens oral intubation. Swollen distorted anatomy makes late rescue more difficult, so timing is critical.",
 "teach":"The airway and mechanism are the two questions: how far has edema spread, and is this histamine or bradykinin biology?"},
"Caustic Ingestion":{
 "recognize":"Caustic ingestion can produce severe esophageal/gastric or laryngeal injury despite limited oral burns. Drooling, dysphagia, chest/abdominal pain, stridor or respiratory distress indicate significant risk.",
 "localize":"Assess airway/larynx and GI tract separately; alkali and acid injury patterns differ but both can cause transmural necrosis, perforation and later stricture.",
 "workup":"Stabilize airway/hemodynamics and use endoscopic/cross-sectional assessment according to symptoms and local protocol. Do not induce emesis or attempt neutralization, which can cause additional injury.",
 "manage":"NPO/supportive care, analgesia and multidisciplinary GI/surgical/ENT involvement depend on severity; perforation/mediastinitis requires urgent source control. Long-term follow-up addresses esophageal stricture and swallowing/nutrition.",
 "operate":"ENT involvement focuses on threatened laryngeal airway; GI/thoracic/general surgery manage deeper perforation/necrosis. Airway manipulation should anticipate friable edematous tissue.",
 "teach":"A normal mouth does not clear the esophagus. The must-not-miss problems are airway injury and transmural perforation."},
"Postoperative Neck Hematoma":{
 "recognize":"Neck swelling/tightness, dysphagia, voice change, stridor, anxiety or rapidly increasing drain output after thyroid/parathyroid/neck surgery can represent expanding hematoma and airway compression.",
 "localize":"Bleeding accumulates beneath platysma/strap or deeper fascial layers and can impair venous/lymphatic drainage, causing progressive laryngeal edema even before direct tracheal compression is dramatic.",
 "workup":"This is primarily a bedside clinical diagnosis; do not send an unstable expanding hematoma to CT. Assess airway and incision while mobilizing OR/anesthesia resources.",
 "manage":"For airway compromise or rapid expansion, open the incision immediately at bedside if necessary to decompress while preparing definitive operative hemostasis. Oxygen/intubation attempts must not delay life-saving decompression.",
 "operate":"Evacuate clot, identify/secure bleeding source and reassess airway edema before extubation. Common sources include thyroid pedicles, muscle/skin vessels or slipped ligature/clips.",
 "teach":"Post-thyroid neck hematoma is a 'cut the sutures' emergency when the airway is threatened. Imaging is not the next step."},
}
for _domain,_mods in DEEP_MODULES_V6.items():
    for _m in _mods:
        _r=TRUE_DEPTH_REWRITES_V99.get(_m.get("topic"))
        if _r:
            _m.update(_r)
            _m["evidence_calibrated"]="v9.9-textbook-saturation"

# Expanded anatomy atlas based on regional organization emphasized in Janfaza and operative atlases.
ANATOMY_EXPANSION_V99 = [
 {"region":"Facial Plastics / Trauma","topic":"Superficial Face — Vessels / Facial Nerve / SMAS","landmarks":["facial artery/vein","superficial temporal vessels","parotid duct","SMAS","facial nerve temporal/zygomatic/buccal/marginal mandibular/cervical branches"],"danger":["facial nerve branches","parotid duct","angular/facial vessels"],"or_link":"Cervicofacial Flap","pearl":"Know whether your flap plane is superficial or deep to the facial nerve/SMAS system before lifting it."},
 {"region":"Facial Plastics / Trauma","topic":"Scalp / Forehead Surgical Layers","landmarks":["skin","dense connective tissue","galea","loose areolar plane","pericranium","supraorbital/supratrochlear bundles","frontal branch facial nerve"],"danger":["frontal branch","supraorbital neurovascular bundles","pericranial blood supply"],"or_link":"Forehead Flap","pearl":"The loose areolar plane permits scalp mobility; the frontal facial-nerve branch is vulnerable in temporal dissection."},
 {"region":"Facial Plastics / Trauma","topic":"Orbit — Compartments / Canthi / Lacrimal System","landmarks":["orbital septum","medial/lateral canthal tendons","lamina papyracea","orbital floor","inferior orbital fissure","lacrimal sac/duct","optic canal"],"danger":["optic nerve","globe","medial rectus","inferior rectus","lacrimal drainage"],"or_link":"Orbital Floor Repair","pearl":"Vision and globe integrity are assessed before fracture reconstruction; medial canthal and lacrimal injuries change the plan."},
 {"region":"Facial Plastics / Trauma","topic":"Mandible / TMJ / Masticator Space","landmarks":["condyle","coronoid","ramus","angle/body/symphysis","inferior alveolar canal","TMJ capsule","masseter","medial/lateral pterygoids"],"danger":["inferior alveolar nerve","facial artery","maxillary artery","facial nerve branches"],"or_link":"Mandible ORIF","pearl":"Occlusion is the functional reference frame; fracture fixation restores biomechanics around dental and muscle forces."},
 {"region":"Rhinology / Skull Base","topic":"Ethmoid Skull Base / Lateral Lamella / AEA","landmarks":["cribriform plate","lateral lamella","fovea ethmoidalis","anterior ethmoid artery","posterior ethmoid artery","lamina papyracea"],"danger":["dura/CSF","olfactory fibers","orbit","AEA retraction into orbit"],"or_link":"Ethmoidectomy","pearl":"The lateral lamella is a thin vulnerable skull-base segment; asymmetry in skull-base height must be read on CT before dissection."},
 {"region":"Rhinology / Skull Base","topic":"Pterygopalatine Fossa / Autonomic Pathways","landmarks":["sphenopalatine foramen","V2/foramen rotundum","vidian canal","pterygopalatine ganglion","descending palatine canal","internal maxillary artery"],"danger":["V2","vidian nerve","maxillary artery","orbital/skull-base extension pathways"],"or_link":"SPA Ligation","pearl":"The PPF connects nasal cavity, orbit, middle cranial fossa, palate and infratemporal fossa—making it a major spread corridor."},
 {"region":"Rhinology / Skull Base","topic":"Infratemporal Fossa / Internal Maxillary Artery","landmarks":["lateral/medial pterygoid","mandibular nerve V3","foramen ovale","middle meningeal artery","internal maxillary artery","pterygoid plexus"],"danger":["V3 branches","middle meningeal artery","pterygoid venous plexus","ICA at skull base"],"or_link":"JNA","pearl":"Bleeding can be venous as well as arterial; understand the pterygoid plexus and maxillary artery branches before deep lateral skull-base dissection."},
 {"region":"Rhinology / Skull Base","topic":"Anterior / Central Cranial Base Foramina","landmarks":["cribriform","optic canal","superior orbital fissure","foramen rotundum","foramen ovale","foramen spinosum","foramen lacerum","carotid canal"],"danger":["CN I–VI pathways","ICA","cavernous sinus","middle meningeal artery"],"or_link":"CSF Leak Repair","pearl":"Foraminal anatomy predicts which cranial neuropathy should accompany a skull-base lesion."},
 {"region":"Otology / Neurotology","topic":"Jugular Foramen / Hypoglossal Canal / Lower Cranial Nerves","landmarks":["jugular bulb","sigmoid sinus","pars nervosa/vascularis concepts","CN IX/X/XI","hypoglossal canal/CN XII","ICA"],"danger":["lower cranial nerves","jugular bulb/IJV","ICA"],"or_link":"Vestibular Schwannoma","pearl":"Multiple IX–XII deficits localize to the lower skull base even before imaging."},
 {"region":"Otology / Neurotology","topic":"IAC / CPA / Labyrinth Relationships","landmarks":["IAC fundus","facial nerve","cochlear nerve","superior/inferior vestibular nerves","labyrinth","porus acousticus","CPA"],"danger":["facial nerve","cochlear nerve","brainstem/cerebellum","labyrinth"],"or_link":"Vestibular Schwannoma","pearl":"Approach selection is inseparable from hearing goals and the course of the facial/cochlear nerves in the IAC."},
 {"region":"Head & Neck Oncology","topic":"External Carotid Artery Branches / Major Hemorrhage Anatomy","landmarks":["superior thyroid","lingual","facial","occipital","posterior auricular","maxillary","superficial temporal arteries"],"danger":["hypoglossal nerve","superior laryngeal nerve","facial nerve","major collateral pathways"],"or_link":"Neck Dissection","pearl":"Know the branch pattern before ligation; tumor/radiation can distort relationships and collateral flow."},
 {"region":"Head & Neck Oncology","topic":"Lateral Neck Triangles / CN XI / Brachial Plexus","landmarks":["SCM","posterior triangle","CN XI","Erb point","brachial plexus","phrenic nerve on anterior scalene","transverse cervical vessels"],"danger":["CN XI","phrenic nerve","brachial plexus","thoracic duct low left"],"or_link":"Neck Dissection","pearl":"CN XI becomes particularly superficial in the posterior triangle and is vulnerable during level V dissection."},
 {"region":"Head & Neck Oncology","topic":"Thoracic Inlet / Root of Neck","landmarks":["subclavian artery/vein","brachiocephalic vessels","phrenic/vagus","recurrent laryngeal nerves","thoracic duct","lung apex/pleura"],"danger":["thoracic duct","phrenic nerve","pleura","subclavian vessels","RLNs"],"or_link":"Reoperative Thyroid","pearl":"Low left-neck surgery approaches the thoracic duct; low neck dissection also risks pleura and phrenic nerve."},
 {"region":"General ENT / Emergencies","topic":"Mediastinal Continuity of Deep Neck Spaces","landmarks":["retropharyngeal space","danger space","prevertebral fascia","visceral/pretracheal spaces","superior mediastinum"],"danger":["descending necrotizing mediastinitis","great vessels","airway/esophagus"],"or_link":"Deep Neck Drainage","pearl":"A deep neck infection can descend below the clavicles through fascial planes even when the original dental/pharyngeal source seems localized."},
 {"region":"Head & Neck Oncology","topic":"Vagus / Sympathetic Chain / Carotid Space","landmarks":["ICA/CCA","IJV","vagus within sheath","sympathetic chain posterior medial","CN IX/XI/XII relationships","carotid bifurcation"],"danger":["vagus","sympathetic chain","hypoglossal","carotid vessels"],"or_link":"Parapharyngeal Tumor","pearl":"Displacement of carotid/IJV and postoperative deficits can identify whether a parapharyngeal tumor arose from vagus, sympathetic chain or prestyloid structures."},
 {"region":"Thyroid / Parathyroid / Salivary","topic":"Superior Laryngeal Nerve / Cricothyroid Space","landmarks":["internal SLN with superior laryngeal artery","thyrohyoid membrane","external SLN","cricothyroid muscle","superior thyroid pole"],"danger":["EBSLN during superior pole ligation","internal SLN during transhyoid work"],"or_link":"Total Thyroidectomy","pearl":"EBSLN injury may preserve gross vocal-fold mobility while impairing pitch projection and high-frequency control."},
 {"region":"Laryngology / Voice / Swallowing","topic":"Laryngeal Neurovascular Anatomy","landmarks":["RLN entry near cricothyroid joint","internal/external SLN","superior/inferior laryngeal arteries","paraglottic space","pre-epiglottic space"],"danger":["RLN","EBSLN","laryngeal vessels"],"or_link":"Microlaryngoscopy","pearl":"The paraglottic and pre-epiglottic spaces are tumor-spread compartments, not merely surgical dead space."},
 {"region":"Head & Neck Oncology","topic":"Free-Flap Recipient Vessels / Reconstructive Neck","landmarks":["facial artery/vein","superior thyroid artery","lingual artery","transverse cervical vessels","external jugular/IJV branches"],"danger":["vagus/hypoglossal/phrenic","scarred/radiated carotid sheath","pedicle compression"],"or_link":"Free Flap","pearl":"Recipient-vessel planning starts before ablation, especially in the vessel-depleted or irradiated neck."},
]

_existing_anat={x["topic"] for x in ANATOMY_ATLAS_V97}
for _x in ANATOMY_EXPANSION_V99:
    if _x["topic"] not in _existing_anat:
        ANATOMY_ATLAS_V97.append(_x)
        _existing_anat.add(_x["topic"])

# Rebuild Daily Path.
ADAPTIVE_ITEMS_V99=[]
for _domain,_mods in DEEP_MODULES_V6.items():
    for _m in _mods:
        _id=_v6_item_id(_domain,_m["topic"])
        for _stage in ["recognize","localize","workup","manage","operate","teach"]:
            ADAPTIVE_ITEMS_V99.append({
              "id":_id+"-"+_stage,"concept_id":_id,"domain":_domain,"topic":_m["topic"],
              "stage":_stage,"display_stage":"advanced" if _stage=="operate" else _stage,
              "prompt":{"recognize":"Recognize the pattern.","localize":"Localize the problem.","workup":"Evaluate it efficiently.","manage":"Build the management sequence.","operate":"Make the advanced decision.","teach":"Teach the mental model."}[_stage],
              "answer":_m[_stage],
              "minutes":{"recognize":3,"localize":3,"workup":4,"manage":4,"operate":6,"teach":4}[_stage],
              "level":{"recognize":1,"localize":2,"workup":3,"manage":4,"operate":5,"teach":6}[_stage],
              "tags":_m.get("tags",_tags_v94(_m["topic"],_domain))
            })
ADAPTIVE_ITEMS_V97=ADAPTIVE_ITEMS_V99
ADAPTIVE_ITEMS_V96=ADAPTIVE_ITEMS_V99
ADAPTIVE_ITEMS_V95=ADAPTIVE_ITEMS_V99
ADAPTIVE_ITEMS_V94=ADAPTIVE_ITEMS_V99
ADAPTIVE_ITEMS_V91=ADAPTIVE_ITEMS_V99

TEXTBOOK_SOURCE_SET_V99 = [
 {"title":"K.J. Lee's Essential Otolaryngology","edition":"12th","role":"breadth, board-relevant fundamentals and general otolaryngology"},
 {"title":"Otolaryngology—Head and Neck Surgery Clinical Reference Guide (Pasha)","edition":"6th","role":"resident workup, management, consults and practical pearls"},
 {"title":"Bluestone & Stool's Pediatric Otolaryngology","edition":"5th","role":"pediatric subspecialty depth"},
 {"title":"Operative Otolaryngology—Head and Neck Surgery","edition":"3rd","role":"broad operative indications, exposure, sequence and complications"},
 {"title":"Operative Techniques in Laryngology","edition":"2nd, 2024","role":"modern voice, airway and swallowing procedures"},
 {"title":"Surgical Anatomy of the Head and Neck","edition":"Janfaza et al.","role":"regional surgical anatomy and danger structures"},
 {"title":"Atlas of Head & Neck Surgery","edition":"Cohen/Clayman","role":"head-and-neck operative anatomy and procedural sequence"},
 {"title":"Atlas of Endoscopic Sinus and Skull Base Surgery","edition":"2nd","role":"endoscopic rhinology/skull-base anatomy and technique"},
]



# =============================================================================
# ENT Mastery v10.0 — Cummings 7e Reconciliation Pass
# Durable anatomy/pathophysiology/procedural framing is reconciled to Cummings 7e.
# Management that changes over time remains subordinate to current society/NCCN guidance.
# =============================================================================

def _v10_module(topic, recognize, localize, workup, manage, operate, teach, sources):
    return {"topic":topic,"recognize":recognize,"localize":localize,"workup":workup,
            "manage":manage,"operate":operate,"teach":teach,"source_basis":sources,"v10":True}

CUMMINGS_RECONCILIATION_V10 = {
"General ENT / Emergencies":[
_v10_module("Evidence Interpretation / Outcomes Research",
"A paper can be statistically positive yet clinically unimportant, or clinically important yet underpowered. First identify the question, population, comparator, outcome and study design before trusting a P value.",
"Localize the inference problem: diagnosis, prognosis, treatment effect, harm, or time-to-event. Match the data type and study design to the claim being made.",
"Read absolute event rates, effect size and confidence intervals before P values. Look for selection bias, confounding, loss to follow-up, inappropriate comparison groups, multiplicity and whether the study is powered for its claimed conclusion.",
"Translate evidence into action by combining magnitude/certainty of benefit, harms, patient values and applicability. Distinguish guideline recommendation strength from evidence level and recognize when observational data are the best feasible evidence for surgical questions.",
"For operative literature, ask whether technique, surgeon experience, selection criteria and follow-up make the result transportable to your practice. Surgical case series can teach feasibility but rarely establish superiority.",
"Teach: effect size + uncertainty + applicability beats 'P < .05.' A negative study without adequate power does not prove equivalence.",
["Cummings 7e: Outcomes Research; Interpreting Medical Data; Evidence-Based Performance Measurement"]),
_v10_module("Pain Management in the Head & Neck Patient",
"Separate acute postoperative nociceptive pain, cancer pain, neuropathic pain and referred craniofacial pain; severe new pain can also be a clue to infection, perineural spread or recurrence.",
"Localize pain by tissue and nerve territory: mucosal/somatic, myofascial, trigeminal, glossopharyngeal/vagal, cervical plexus or treatment-related neuropathy.",
"Use focused history/exam to identify red flags, opioid exposure, renal/hepatic constraints, sleep-disordered breathing, neuropathic features and the structural cause that still needs treatment.",
"Use multimodal analgesia when safe; treat the cause, not only the score. Escalate cancer/neuropathic pain with multidisciplinary support and avoid reflex chronic opioid escalation without a defined plan.",
"Perioperative analgesia should anticipate the procedure's pain phenotype, airway/sedation risk, nausea, swallowing and discharge needs. Rescue plans belong in the preoperative plan.",
"Teach the resident to ask: what is generating the pain, what dangerous diagnosis am I missing, and what modality targets that mechanism with the least collateral harm?",
["Cummings 7e: Pain Management in the Head and Neck Patient"]),
_v10_module("Geriatric Otolaryngology / Frailty",
"Older adults often present with interacting hearing, balance, voice, swallowing, cognition, frailty and polypharmacy issues rather than one isolated organ problem.",
"Localize functional failure across sensory, motor and reserve systems: hearing/vestibular, laryngeal, pharyngeal, salivary, airway and reconstructive capacity.",
"Assess baseline function, cognition, falls, nutrition, aspiration risk, medications, social support and goals in addition to disease-specific testing.",
"Treat reversible disease while aligning intensity with physiologic reserve and goals. Hearing rehabilitation, swallowing safety, fall prevention and communication access can be as consequential as surgery.",
"Age alone is not an operative contraindication; frailty, comorbidity, functional reserve and the expected recovery burden are more useful. Plan delirium, aspiration, rehabilitation and caregiver needs.",
"Teach: the geriatric ENT patient is not 'the same case but older'—reserve, recovery and competing risks change the decision.",
["Cummings 7e: Otolaryngology in the Elderly"]),
_v10_module("Immunocompromised Host in Otolaryngology",
"Immune suppression changes both the differential and the tempo: ordinary infections can be aggressive and opportunistic infection, PTLD/lymphoma, unusual cutaneous disease and invasive fungal disease become more plausible.",
"Localize by compartment—sinonasal, oral, salivary, neck, laryngeal, otologic—and by immune defect/transplant context rather than using one generic 'immunocompromised' differential.",
"Clarify transplant/HIV/hematologic status, neutropenia, medications and timing. Obtain targeted cultures/pathology/imaging early when invasive disease is possible; biopsy persistent masses or atypical mucosal/skin lesions.",
"Coordinate antimicrobial, oncologic and immunosuppression decisions with the relevant teams. Escalate rapidly when invasive fungal disease, airway compromise or PTLD is possible.",
"Surgery may be diagnostic, source-control, airway-protective or oncologic. Tissue handling must anticipate cultures, stains, flow cytometry and permanent pathology when the differential is broad.",
"Teach: immune status changes the prior probability. A common-looking ENT problem can require an uncommon workup when the host is uncommon.",
["Cummings 7e: Head and Neck Manifestations in the Immunocompromised Host"]),
_v10_module("Oral Manifestations of Systemic Disease",
"Oral ulceration, bullae, white/red lesions, xerostomia, periodontal change and exposed necrotic bone can reflect systemic autoimmune, infectious, hematologic, metabolic or medication-related disease.",
"Describe the exact oral subsite, mucosal layer/pattern, salivary status, dental/alveolar involvement and whether disease is localized or multisite.",
"Medication review, systemic review, dental evaluation and appropriately handled biopsy are central. Suspected immunobullous disease requires the correct perilesional specimen strategy; MRONJ requires exposure history and jaw assessment.",
"Treat the underlying disorder with the appropriate specialty while addressing pain, infection, oral hygiene, xerostomia and nutrition. Persistent or suspicious red/white/ulcerative lesions still need malignancy exclusion.",
"Operative intervention is selective: biopsy, debridement/source control or management of complications rather than reflex excision of inflammatory disease.",
"Teach: oral mucosa is a window into systemic disease, but a systemic explanation never excuses failure to exclude cancer when the lesion is persistent or atypical.",
["Cummings 7e: Oral Manifestations of Systemic Diseases"]),
],
"Facial Plastics / Trauma":[
_v10_module("Aesthetic Facial Analysis",
"Aesthetic analysis is structured description, not 'looks good/bad': facial thirds/fifths, symmetry, profile, skin envelope, nasal projection/rotation and chin-lip relationships.",
"Localize an aesthetic concern to skeletal framework, cartilage, soft tissue, skin or dynamic muscle and distinguish regional imbalance from an isolated nasal or eyelid problem.",
"Use standardized photography and reproducible measurements/views. Functional nasal, ocular and facial-nerve issues are assessed separately but integrated into the plan.",
"Match intervention to a defined structural objective and patient goal; avoid chasing isolated measurements without considering whole-face balance.",
"Every maneuver should have a predicted vector/volume/support effect and an anticipated tradeoff. Preoperative analysis should be traceable to the operative plan.",
"Teach: describe first, diagnose the structural imbalance second, choose a maneuver third.",
["Cummings 7e: Aesthetic Facial Analysis"]),
_v10_module("Facial Soft-Tissue Lacerations / Burns",
"Prioritize airway, vision, facial nerve, lacrimal system, salivary duct, cartilage exposure and tissue viability before cosmetic closure.",
"Localize injury by facial subunit and deep structure: eyelid/canthus, cheek/parotid duct, lip/vermilion, ear cartilage, nose, brow/frontal branch and scalp.",
"Irrigate/explore enough to define depth and contamination; assess tetanus, foreign body, bite/contamination, associated fracture and specialty-threatening injury.",
"Early meticulous repair restores alignment and function. Devitalized tissue is handled conservatively on the face when viability is uncertain; burns require depth/airway assessment and staged wound strategy.",
"Repair landmarks first—vermilion, lid margin, brow, alar rim—then layered tension-free closure. Repair duct/nerve/canalicular injury when indicated rather than closing over it.",
"Teach: the scar is often determined by what you align and what deep injury you recognize, not by the brand of suture.",
["Cummings 7e: Facial Trauma—Soft Tissue Lacerations and Burns"]),
_v10_module("Aging Face / Injectables / Resurfacing",
"Separate volume loss, skin texture/dyschromia, static rhytids, dynamic rhytids, ptosis/laxity and skeletal support; each requires a different treatment mechanism.",
"Localize aging change by tissue plane and facial danger zones, especially vascular territories and motor-nerve relationships.",
"Standardized photos, medication/bleeding history, prior filler/device history and ocular/facial-nerve function guide safe planning.",
"Neuromodulators address dynamic muscle activity; fillers restore selected volume/support; resurfacing targets skin; surgery repositions deeper tissues. Combine only when the anatomy and goals justify it.",
"Know vascular occlusion, ocular ischemia, skin necrosis, ectropion, nerve injury and pigment/scar complications and have a rescue plan before treatment.",
"Teach: match the aging layer to the treatment layer—muscle, volume, skin and ptosis are not interchangeable problems.",
["Cummings 7e: facial rejuvenation chapters / Facial Plastic and Reconstructive Surgery section"]),
_v10_module("Hair Restoration Fundamentals",
"Patterned androgenetic alopecia differs from scarring/inflammatory alopecia and diffuse shedding; restoration planning begins with a stable diagnosis and realistic donor supply.",
"Localize durable donor hair and understand hairline/temporal framing, density, caliber, curl and direction rather than counting grafts alone.",
"History/exam should identify medical/scarring causes, medication options, progression risk and donor-site quality before surgery.",
"Medical stabilization and camouflage may be appropriate; transplantation redistributes finite donor follicles and must anticipate future loss.",
"Follicular-unit extraction and strip-harvest strategies have different donor/scar tradeoffs. Hairline design, angle and graft handling determine natural appearance.",
"Teach: transplantation cannot create unlimited hair—long-term design protects the patient from a good one-year result and a bad ten-year result.",
["Cummings 7e: Hair Restoration—Medical and Surgical Techniques"]),
],
"Rhinology / Allergy / Skull Base":[
_v10_module("Objective Assessment of Nasal Function",
"Nasal obstruction is subjective; objective tests measure different components of airflow/geometry and do not perfectly substitute for symptoms.",
"Separate mucosal reversibility from fixed septal, valve or bony narrowing and from sensory mismatch where measured resistance is not the whole symptom.",
"Use validated symptom measures and exam/endoscopy first. Rhinomanometry, acoustic rhinometry or peak nasal inspiratory flow can answer selected physiologic/research questions, especially pre/post decongestion or intervention.",
"Treat the identified mechanism and use objective testing when it resolves a real question rather than as a routine prerequisite for every obstructed patient.",
"Surgical planning remains anatomy-driven; a number from an airflow test does not tell you which structure to modify.",
"Teach: symptom, anatomy and physiology are related but not identical. Concordance is useful; discordance is information.",
["Cummings 7e: Objective Assessment of Nasal Function"]),
_v10_module("Facial Pain / Headache vs Rhinogenic Disease",
"Most facial pressure/headache is not automatically sinus disease. Migraine and other primary headache disorders commonly mimic 'sinus headache.'",
"Localize pain by time course, autonomic/migrainous features, triggers, neurologic findings and objective sinonasal inflammation rather than pain location alone.",
"Endoscopy and CT are used when sinus disease is clinically plausible, but incidental mucosal thickening does not prove causality. Red flags may require neurologic/dental/ophthalmic workup.",
"Treat proven sinonasal inflammation when present and route primary headache/TMJ/neuralgia to the correct pathway. Avoid antibiotics or ESS for imaging findings that do not fit the syndrome.",
"Surgery is appropriate when a defined sinonasal disease process and symptom relationship support it—not as an empiric headache procedure.",
"Teach: 'pain over the sinus' is anatomy, not etiology.",
["Cummings 7e: Facial Pain"]),
_v10_module("Benign Sinonasal Tumor Framework",
"Unilateral mass, recurrent epistaxis, remodeling/erosion, cranial neuropathy or atypical 'polyps' should trigger a tumor framework rather than routine CRS assumptions.",
"Localize the epicenter and spread through nasal cavity, sinuses, orbit, skull base, pterygopalatine/infratemporal fossae; infer vascular, neural or epithelial origin from pattern.",
"Endoscopy plus contrast CT/MRI as indicated defines attachment, vascularity and critical extension. Do not biopsy a potentially hypervascular lesion until safety is understood.",
"Management ranges from surveillance to endoscopic/open resection based on histology, growth, attachment, symptoms and skull-base/orbital involvement.",
"Plan the route around attachment and danger structures, with vascular control and reconstruction strategy when needed.",
"Teach: unilateral disease is a diagnostic category. Ask 'what is this?' before treating it as inflammation.",
["Cummings 7e: Benign Tumors of the Sinonasal Tract"]),
_v10_module("Systemic Disease of the Nose / Sinuses",
"Crusting, septal perforation, destructive lesions, refractory inflammation or multisystem symptoms can reflect vasculitis, granulomatous, autoimmune, infectious or toxic disease.",
"Localize destructive disease to septum, turbinates, lateral wall, palate and skull-base/orbital structures, while looking for systemic sites such as lung, kidney, skin and eye.",
"Biopsy viable edge tissue when needed and pair pathology with targeted serology/culture/systemic evaluation; avoid nonspecific panels without a phenotype.",
"Treat the systemic driver with the appropriate specialty while controlling local infection, crusting, bleeding and structural complications.",
"Delay elective reconstruction until destructive activity is controlled when possible; active disease can defeat an otherwise technically sound repair.",
"Teach: a septal perforation is a finding, not a diagnosis.",
["Cummings 7e: Systemic Disease of the Nose and Sinuses"]),
],
"Laryngology / Voice / Swallowing":[
_v10_module("Professional Voice",
"A professional voice user may be disabled by subtle change that would be acceptable to a casual voice user; occupational demand is part of disease severity.",
"Localize limitation to mucosal vibration, glottic closure, motor control, respiratory support, resonance and compensatory muscle tension.",
"Stroboscopy, perceptual/acoustic assessment and task-specific evaluation should reproduce the professional demand when possible.",
"Voice therapy, load modification, amplification, medical treatment and surgery are selected to restore function while protecting the vibratory cover.",
"Microsurgery must minimize epithelial/lamina propria trauma; return-to-performance planning is part of the procedure, not an afterthought.",
"Teach: 'normal speaking voice' does not equal normal occupational function.",
["Cummings 7e: The Professional Voice"]),
_v10_module("Acute / Chronic Laryngopharyngitis",
"Hoarseness/throat symptoms may be infectious, inflammatory, irritant, phonotraumatic or systemic; chronic symptoms should not be reflexively labeled reflux.",
"Localize by laryngeal/pharyngeal exam and distinguish diffuse inflammation from focal lesion, impaired motion or malignancy.",
"Use laryngoscopy when symptoms persist or red flags exist. Target testing to suspected infection/systemic disease; avoid indiscriminate reflux testing or antibiotics.",
"Hydration, voice conservation/therapy and cause-specific treatment are foundational. Address smoking/irritants and treat proven infection/systemic disease.",
"Operative biopsy is reserved for suspicious or persistent focal pathology rather than diffuse uncomplicated inflammation.",
"Teach: inflammation is a phenotype; define the cause before prescribing a chronic label.",
["Cummings 7e: Acute and Chronic Laryngopharyngitis"]),
_v10_module("Esophageal Disease for the Otolaryngologist",
"Differentiate oropharyngeal initiation/airway-protection problems from cervical or distal esophageal dysphagia, regurgitation and motility disease.",
"Localize symptoms above, at or below the UES and recognize that perceived neck sticking can still originate distally.",
"Choose FEES/MBS for pharyngeal physiology, esophagram/endoscopy for structural questions and GI motility evaluation when dysmotility is suspected.",
"Treat ENT-manageable pharyngoesophageal problems while referring distal inflammatory, motility and neoplastic disease appropriately.",
"Endoscopic procedures require perforation awareness and anatomic understanding of UES/cervical esophagus; do not force an instrument against unexplained resistance.",
"Teach: first localize the phase of swallowing failure; then choose the test.",
["Cummings 7e: Diseases of the Esophagus"]),
_v10_module("Transnasal Esophagoscopy",
"TNE provides unsedated office evaluation of selected pharyngeal/esophageal complaints and surveillance questions but is not a universal replacement for conventional endoscopy.",
"Understand nasal passage, hypopharynx, UES and esophageal landmarks while recognizing the limits of office visualization and intervention.",
"Select patients based on the diagnostic question, anatomy, tolerance and need for biopsy/therapy or deeper GI evaluation.",
"Use TNE when it answers the question efficiently; escalate to sedated EGD, imaging or motility testing when the problem exceeds its scope.",
"Topical anesthesia, controlled passage and recognition of resistance/perforation risk are central. Do not let office convenience override safety.",
"Teach: choose TNE for the question it can answer, not because the scope is available.",
["Cummings 7e: Transnasal Esophagoscopy"]),
_v10_module("Tracheobronchial Endoscopy Principles",
"Rigid and flexible bronchoscopy answer different airway questions and provide different control of ventilation, foreign bodies and intervention.",
"Localize lesions by subglottis, cervical/intrathoracic trachea, carina and main bronchi; describe fixed vs dynamic obstruction and length/circumference.",
"Preoperative imaging and airway plan are driven by obstruction severity and suspected pathology. Coordinate ventilation strategy before instrumenting a critical airway.",
"Use flexible bronchoscopy for selected diagnosis/surveillance and rigid bronchoscopy when airway control, foreign-body removal or therapeutic instrumentation requires it.",
"Know teeth/larynx injury, bleeding, hypoxia, pneumothorax, airway fire/laser issues and loss-of-airway rescue. Surgeon-anesthesia communication is the procedure.",
"Teach: airway endoscopy is both visualization and ventilation strategy.",
["Cummings 7e: Tracheobronchial Endoscopy"]),
],
"Head & Neck Oncology":[
_v10_module("Radiation Therapy Principles for Head & Neck Surgeons",
"Radiation is a spatial dose treatment with acute and late toxicity; definitive, adjuvant and palliative intent answer different oncologic questions.",
"Localize target volumes and organs at risk conceptually: primary bed, nodal basins, spinal cord/brainstem, salivary glands, mandible, larynx/pharyngeal constrictors and carotid/skin in salvage contexts.",
"For surgical decision-making, know prior dose/fields, interval, response and late effects. Post-treatment imaging must be interpreted in the context of edema/fibrosis and expected tissue change.",
"Use multidisciplinary stage/risk-based indications. Modern management balances control with swallowing, salivary, mandibular, endocrine and vascular late effects.",
"Prior radiation changes wound healing, vessel quality and reconstructive risk; salvage surgery requires tissue/reconstruction planning beyond the resection itself.",
"Teach: 'the patient had radiation' is incomplete—ask where, how much, when, and what tissue consequence remains.",
["Cummings 7e: Radiotherapy for Head and Neck Cancer—Physics, Radiobiology, Clinical Principles","Current NCCN H&N guidance for treatment selection"]),
_v10_module("Systemic Therapy Foundations in Head & Neck Cancer",
"Cytotoxic chemotherapy, targeted therapy and immunotherapy have different goals, biomarkers and toxicity patterns; systemic treatment may be radiosensitizing, definitive, neoadjuvant, adjuvant or palliative.",
"Localize the treatment decision to tumor biology, disease burden and site rather than using one regimen framework for every HNSCC or salivary/thyroid cancer.",
"Review pathology/viral biomarkers, performance status, renal/hearing/neurologic function and prior treatment when systemic therapy is contemplated.",
"Multidisciplinary selection follows disease state and current guidelines. Surgeons should understand why systemic therapy is chosen, major toxicities and what response/progression means for salvageability.",
"Systemic therapy can change tissue planes, nutrition, cytopenias and timing. Operative planning after therapy should include wound, airway and reconstruction implications.",
"Teach: know the intent of systemic therapy before memorizing the drug.",
["Cummings 7e: Chemotherapy and Targeted Biologic Agents for Head and Neck Cancer","Current NCCN H&N guidance"]),
_v10_module("Free-Flap Monitoring / Compromise / Salvage",
"Venous congestion and arterial insufficiency have different bedside phenotypes, but either is a time-critical threat to a free flap.",
"Think from pedicle macrocirculation to microcirculation and tissue metabolism; identify whether the problem is thrombosis, kinking/compression, hematoma, recipient-vessel issue or systemic perfusion.",
"Serial clinical examination is foundational; Doppler/implantable or perfusion adjuncts support but do not replace it. A concerning trend matters more than waiting for complete necrosis.",
"Correct systemic contributors while activating urgent surgical evaluation. Mechanical/pedicle causes usually require early exploration rather than prolonged observation.",
"Take-back sequence: release compression/hematoma, inspect pedicle and anastomoses, restore inflow/outflow, clear thrombosis as appropriate and reassess tissue viability. Selected venous-congestion rescue may use leech therapy when surgically appropriate and after infection planning.",
"Teach: the best flap-salvage test is early recognition followed by decisive action.",
["Cummings 7e: Skin Flap Physiology and Wound Healing; Free Tissue Transfer"]),
_v10_module("Open Partial / Conservation Laryngectomy",
"Conservation surgery is oncologic resection designed to preserve a functional larynx in carefully selected disease—not a smaller total laryngectomy.",
"Localize tumor relative to true/false cords, ventricle, paraglottic/pre-epiglottic spaces, arytenoids/cricoarytenoid joints, subglottis and cartilage.",
"Endoscopy plus imaging define extent and mobility. Patient pulmonary/swallowing reserve and ability to rehabilitate are part of candidacy.",
"Select transoral, open partial, radiation-based or total-laryngectomy strategies by oncologic extent and expected function. Functional preservation without safe swallowing/airway is not success.",
"Know supraglottic and supracricoid principles, arytenoid preservation, pexy/reconstruction and the major complications of aspiration, edema/stenosis and delayed decannulation.",
"Teach: conservation surgery preserves function only when both tumor anatomy and patient physiology permit it.",
["Cummings 7e: Conservation Laryngeal Surgery"]),
_v10_module("Transoral Laser Microsurgery for Laryngeal Cancer",
"TLM is an exposure- and margin-dependent oncologic technique; the laser is a tool, not the indication.",
"Map the lesion in three dimensions through the laryngeal subsites and deep spaces; exposure determines whether precise transoral resection is feasible.",
"Preoperative endoscopy/imaging define cartilage/deep-space disease and neck treatment needs. Intraoperative orientation and specimen mapping are essential when resection is piecemeal.",
"Use TLM for appropriately selected tumors when oncologic access and functional goals are favorable; choose radiation/open surgery/total laryngectomy when exposure or extent defeats safe margins.",
"Laser safety, airway fire prevention, depth control, margin mapping and preservation of uninvolved functional tissue are core technique principles.",
"Teach: TLM is not 'burning out a tumor'—it is controlled oncologic resection under magnified exposure.",
["Cummings 7e: Transoral Laser Microresection of Advanced Laryngeal Tumors"]),
_v10_module("Complications of Neck Surgery",
"A postoperative neck problem must be triaged by airway, hemorrhage, neurologic deficit, lymphatic/chyle leak, wound/fistula and vascular catastrophe.",
"Localize deficits by CN XI, vagus/RLN, hypoglossal, sympathetic chain, phrenic nerve, brachial plexus, thoracic duct and carotid/IJV anatomy.",
"Use exam and targeted imaging/labs based on the complication; do not delay airway/hematoma treatment for a complete diagnostic workup.",
"Treat time-critical airway/bleeding immediately, then use cause-specific rehabilitation or repair for nerve, chyle, wound and vascular complications.",
"Prevention begins with anatomy and intraoperative recognition. Rescue may require re-exploration, vessel control, flap coverage, drain/nutrition strategy or multidisciplinary endovascular support.",
"Teach: know the expected deficit pattern of each structure before you operate so you can recognize it immediately after.",
["Cummings 7e: Complications of Neck Surgery"]),
],
"Thyroid / Parathyroid / Salivary":[
_v10_module("Thyroid Eye Disease / Graves Ophthalmopathy",
"TED severity and inflammatory activity are different axes; proptosis, diplopia/exposure and optic neuropathy do not all require the same treatment.",
"Localize disease to extraocular muscles and orbital fat within a fixed bony orbit; apical crowding threatens the optic nerve while inferior/medial rectus enlargement drives common motility patterns.",
"Assess visual acuity/color, pupils, cornea, motility/diplopia, proptosis and optic-nerve risk with ophthalmology; CT helps define muscle/apical anatomy when decompression is considered.",
"Coordinate thyroid control, smoking cessation and activity/severity-directed medical/ophthalmic therapy. Urgent vision-threatening disease is different from rehabilitative surgery after inactive disease.",
"Orbital decompression is wall/fat-selective and anatomy-specific; balance decompression against new/worsened diplopia and protect orbit/skull base/sinuses.",
"Teach: active inflammation determines timing; severity determines urgency and the functional problem to solve.",
["Cummings 7e: Management of Thyroid Eye Disease"]),
],
"Otology / Neurotology":[
_v10_module("Auditory Neuroanatomy / Cochlear Physiology",
"Sound becomes neural code through middle-ear transmission, cochlear traveling-wave mechanics, hair-cell transduction and tonotopic auditory pathways.",
"Localize from outer/middle ear to cochlea, spiral ganglion/CN VIII, cochlear nuclei, superior olivary complex, lateral lemniscus, inferior colliculus, medial geniculate and auditory cortex.",
"Use the pattern of audiometry, speech testing, OAEs and electrophysiology to decide whether the deficit is conductive, cochlear, neural or central.",
"Management follows localization: amplify or implant when peripheral access is the problem; pursue neurologic/retrocochlear evaluation when neural/central patterns are discordant.",
"Operative hearing procedures succeed only if the downstream neural pathway can use the delivered signal; counsel accordingly in malformation/neural deficiency.",
"Teach: audiology becomes easier when every test is tied to the structure that generates the response.",
["Cummings 7e: Neuroanatomy of the Auditory System; Physiology of the Auditory System; Cochlear Transduction"]),
_v10_module("Audiologic Electrophysiology / ABR-OAE-ECoG",
"OAEs test outer-hair-cell/cochlear function; ABR tests synchronized neural transmission through the auditory nerve/brainstem; ECoG interrogates cochlear/auditory-nerve potentials near the cochlea.",
"Localize an abnormal pattern by asking what generator is present or absent rather than memorizing 'positive tests.'",
"Interpret thresholds, waveform presence/latency/interaural asymmetry and technical factors in context. Present OAEs with absent/abnormal ABR suggests auditory-neural dyssynchrony when the clinical setting fits.",
"Use electrophysiology for infant/behaviorally limited assessment, neural localization and selected intraoperative/diagnostic questions; do not substitute it blindly for behavioral hearing when reliable behavior is available.",
"Intraoperative monitoring requires baseline signal quality, anesthetic/technical awareness and trend interpretation; a waveform change is a communication event, not an isolated number.",
"Teach: ask 'what tissue made this waveform?' before interpreting it.",
["Cummings 7e: Diagnostic Audiology and Electrophysiologic Assessment of Hearing"]),
_v10_module("Cortical Neuroplasticity in Hearing Loss",
"Auditory deprivation changes central processing; duration and developmental timing influence how effectively restored peripheral input can be used.",
"Localize the problem beyond the cochlea: brainstem/cortical networks adapt to altered sensory input and may reorganize with prolonged deprivation.",
"Integrate duration of loss, age at onset, language development and hearing-device use with standard audiology when counseling rehabilitation.",
"Provide timely hearing access in children and avoid unnecessary prolonged deprivation in implant candidates; pair devices with auditory/language rehabilitation.",
"Surgery restores access, not learned auditory meaning. Postoperative programming and rehabilitation are part of the biologic treatment.",
"Teach: a cochlear implant delivers signal; the brain still has to learn to use it.",
["Cummings 7e: Cortical Neuroplasticity in Hearing Loss"]),
_v10_module("Otologic Manifestations of Systemic Disease",
"Systemic autoimmune, infectious, metabolic, hematologic and skeletal disease can present with hearing loss, vestibular symptoms, middle-ear disease or temporal-bone findings.",
"Localize the audiovestibular phenotype first, then connect it to systemic disease rather than attributing every symptom to the known diagnosis.",
"Use targeted labs/imaging based on phenotype and systemic clues; audiometry documents pattern and trajectory.",
"Treat the systemic driver with the relevant team plus symptom-specific hearing/vestibular rehabilitation; urgent sudden or rapidly progressive deficits keep their time-sensitive pathways.",
"Surgery is selective and anatomy-driven; systemic disease can alter healing, bone quality and recurrence risk.",
"Teach: a systemic diagnosis changes context, not the need to localize the ear problem.",
["Cummings 7e: Otologic Manifestations of Systemic Disease"]),
_v10_module("Hyperacusis / Decreased Sound Tolerance",
"Hyperacusis is abnormal intolerance of ordinary sound and differs from loudness recruitment, misophonia and phonophobia despite overlap.",
"Localize the complaint to auditory gain/central processing after excluding active ear disease, third-window symptoms and neurologic/migraine context.",
"Audiometry and loudness-tolerance testing may support assessment; history should characterize triggers, pain, fear/avoidance, tinnitus and functional impairment.",
"Education, gradual sound desensitization and treatment of comorbid tinnitus/migraine/anxiety mechanisms are more useful than excessive sound avoidance in many patients.",
"Surgery has no routine role unless a specific structural disorder such as a third-window lesion explains the phenotype.",
"Teach: sound intolerance is a symptom family—name the phenotype before treating it.",
["Cummings 7e: Tinnitus and Hyperacusis"]),
_v10_module("Labyrinthitis / Infections of the Labyrinth",
"Acute vestibular syndrome with hearing loss suggests labyrinthine involvement rather than isolated vestibular neuritis; bacterial extension from otitis/mastoid disease can be destructive.",
"Localize to cochlea + vestibular labyrinth and determine whether spread is viral/inflammatory, meningogenic or tympanogenic.",
"Audiometry and otologic/neurologic exam are essential; imaging and infectious workup are driven by meningitis, mastoiditis, cholesteatoma or intracranial concern.",
"Treat the underlying infection/inflammation urgently when bacterial disease is possible, manage vertigo briefly when needed and begin hearing/vestibular rehabilitation as the acute phase resolves.",
"Source control may require mastoid/middle-ear surgery when suppurative disease or cholesteatoma drives labyrinthine infection.",
"Teach: vestibular neuritis should not cause a new cochlear hearing loss; that clue changes localization.",
["Cummings 7e: Infections of the Labyrinth"]),
_v10_module("Central Vestibular Disorders",
"Direction-changing gaze-evoked nystagmus, skew, impaired smooth pursuit/saccades, severe truncal ataxia or neurologic deficits push dizziness toward a central process.",
"Localize by ocular-motor pattern to brainstem/cerebellar pathways rather than relying on the patient's word 'vertigo.'",
"In acute vestibular syndrome, bedside eye movements are interpreted only in the correct clinical context; imaging/neurologic evaluation is urgent when a central pattern is suspected.",
"Treat the underlying neurologic disease and use vestibular rehabilitation selectively; chronic central compensation may still improve with therapy.",
"ENT surgery has no role for most central vestibular disease; the advanced decision is knowing when not to operate and when to escalate to stroke/neurology pathways.",
"Teach: central versus peripheral is an eye-movement/localization problem, not a symptom adjective.",
["Cummings 7e: Central Vestibular Disorders"]),
_v10_module("Vestibular Rehabilitation",
"Persistent imbalance after unilateral or bilateral vestibular loss often reflects incomplete compensation rather than persistent dangerous disease.",
"Identify gaze-instability, motion sensitivity, balance/gait and positional components; different deficits require different exercises.",
"Document vestibular diagnosis, fall risk, vision/proprioception, neuropathy and functional goals before prescribing therapy.",
"Use adaptation, habituation, substitution and balance/gait training tailored to the deficit; prolonged vestibular suppressants can impede compensation in many chronic peripheral cases.",
"Surgery may remove the offending vestibular input but rehabilitation converts that stable deficit into usable function.",
"Teach: vestibular rehab is targeted neuroplastic training, not generic balance exercise.",
["Cummings 7e: Vestibular and Balance Rehabilitation Therapy"]),
_v10_module("Neurotologic Intraoperative Cranial-Nerve Monitoring",
"Monitoring is an adjunct to anatomy and surgical judgment; EMG/evoked-potential changes warn of nerve irritation or loss of pathway function but do not replace direct visualization.",
"Map recording targets to CN V motor, VII, VIII, IX-XII and understand that latency/amplitude depend on stimulation site and pathway length.",
"Establish reliable baselines and recognize anesthetic, electrode and stimulation artifacts before interpreting a change as injury.",
"When a meaningful signal change occurs, stop/reassess the maneuver, irrigate/release traction, verify technical integrity and communicate explicitly with anesthesia/monitoring.",
"Use facial EMG/MEP, cochlear monitoring and lower-CN techniques according to the skull-base operation. ETT electrode position is especially important for vagal/RLN monitoring.",
"Teach: monitoring is a closed-loop communication system attached to anatomy—not a noise machine in the corner.",
["Cummings 7e: Intraoperative Monitoring of Cranial Nerves in Neurotologic Surgery"]),
_v10_module("Lateral Skull-Base Tumor Framework",
"A lateral skull-base mass is approached by epicenter, hearing status, cranial-nerve deficits, vascularity and growth—not by a single generic 'skull-base tumor' algorithm.",
"Differentiate IAC/CPA, jugular foramen, facial nerve, temporal bone, endolymphatic-sac/petrous and paraganglionic corridors by displacement and nerve pattern.",
"High-resolution CT and contrast MRI are complementary; audiometry, facial/lower-CN exam and vascular evaluation are selected by lesion type.",
"Observation, radiation and surgery depend on natural history, size/growth, symptoms, age, hearing and morbidity of the involved cranial nerves.",
"Approach selection—middle fossa, retrosigmoid, translabyrinthine, infratemporal/jugular-foramen variants—follows tumor corridor and functional goals.",
"Teach: first name the epicenter and the function you are trying to preserve; the approach usually follows.",
["Cummings 7e: Surgical Anatomy of the Lateral Skull Base; Temporal Bone Neoplasms and Lateral Cranial Base Surgery; Neoplasms of the Posterior Fossa"]),
],
"Pediatric Otolaryngology":[
_v10_module("Pediatric Speech Disorders",
"Differentiate articulation/phonologic disorder, motor speech disorder, resonance/VPI, hearing-related language effects and voice disorder before assigning an ENT cause.",
"Localize communication failure to hearing input, oral articulators, palate/velopharynx, motor planning/control or language development.",
"Audiology and speech-language evaluation are foundational; nasendoscopy/fluoroscopy is reserved for suspected resonance/velopharyngeal physiology.",
"Treat the mechanism with speech therapy, hearing access, structural surgery or neurologic/developmental support as appropriate.",
"ENT surgery corrects anatomic contributors but cannot replace motor/language learning; operative decisions should be made with the speech team.",
"Teach: 'speech delay' is a symptom—first decide whether the bottleneck is hearing, language, articulation, motor control or resonance.",
["Cummings 7e: Pediatric Speech Disorders"]),
_v10_module("Nonobstructive Pediatric Sleep Disorders",
"Not every sleepy, restless or poorly sleeping child has obstructive sleep apnea; insomnia, parasomnias, circadian disorders, restless sleep and central disorders enter the differential.",
"Localize the sleep complaint to initiation/maintenance, breathing, movement, arousal/parasomnia or excessive sleepiness.",
"History, sleep schedule and targeted PSG/labs are selected by phenotype; iron evaluation may be relevant in movement/restless-sleep syndromes.",
"Use behavioral/sleep-medicine pathways for nonobstructive disorders and avoid adenotonsillectomy when the physiology is not obstructive.",
"The surgical decision is often 'do not operate' until obstructive anatomy is demonstrated.",
"Teach: snoring surgery treats obstruction, not every form of poor sleep.",
["Cummings 7e: Nonobstructive Pediatric Sleep Disorders"]),
_v10_module("Cleft Lip / Palate — ENT Surgical Fundamentals",
"Cleft palate affects feeding, speech/resonance and Eustachian-tube function; the problem is a muscular/anatomic system, not only a visible gap.",
"Localize orbicularis/lip, hard/soft palate, levator sling, tensor/ET relationship and velopharyngeal closure pattern.",
"Coordinate feeding, hearing/OME, speech and craniofacial assessment longitudinally; procedure timing is team-based and developmentally informed.",
"Repair aims to create functional palatal continuity and muscle orientation while anticipating middle-ear and speech outcomes.",
"Palatoplasty technique centers on tension-free closure and levator reconstruction/lengthening concepts while protecting growth and fistula risk.",
"Teach: successful cleft care is longitudinal—hearing and speech outcomes matter as much as closure of the cleft.",
["Cummings 7e: Cleft Lip and Palate"]),
_v10_module("Microtia Reconstruction",
"Microtia management integrates auricular form, hearing status, canal anatomy, craniofacial symmetry and patient/family goals.",
"Localize reconstructive needs to auricular framework/skin envelope while separately assessing canal/middle-ear and facial-nerve anatomy.",
"Audiology is mandatory; CT for atresia surgical candidacy is timed to the treatment question. Coordinate reconstruction choice with any canal surgery to preserve tissue planes.",
"Options include observation/prosthesis, implant-retained prosthesis, autologous rib framework or alloplastic reconstruction, with hearing rehabilitation in parallel.",
"Autologous reconstruction requires framework design, pocket/skin management and staged projection concepts; alloplastic approaches carry different exposure/infection tradeoffs.",
"Teach: ear shape and hearing are two related but separate treatment tracks that must be sequenced together.",
["Cummings 7e: Microtia Reconstruction"]),
_v10_module("Pediatric Vestibular Disorders",
"Children may present with falls, delayed motor milestones, episodic vertigo, motion intolerance or school/sports difficulty rather than a precise dizziness history.",
"Localize peripheral vestibular, migraine, central, visual/proprioceptive and developmental contributors while considering hearing loss and congenital inner-ear disease.",
"Age-appropriate vestibular testing, audiology and neurologic/developmental assessment are selected by phenotype; interpret norms with age/attention limitations.",
"Treat the cause and use vestibular/balance rehabilitation when deficits affect development or safety.",
"Surgery is reserved for specific structural disease; most pediatric vestibular care is diagnostic and rehabilitative.",
"Teach: a child who 'is clumsy' may be describing vestibular dysfunction with the vocabulary available to them.",
["Cummings 7e: Evaluation and Management of Pediatric Vestibular Disorders"]),
_v10_module("Ankyloglossia / Maxillary Frenulum",
"A visible frenulum is not itself an indication for surgery; functional breastfeeding, tongue mobility/speech and dental issues must be demonstrated in context.",
"Localize restriction to the lingual frenulum and distinguish true functional tethering from feeding mechanics, neuromuscular or craniofacial causes.",
"Use feeding/lactation or speech assessment when relevant; avoid anatomy-only scoring as the sole decision maker.",
"Support feeding first and reserve frenotomy/frenuloplasty for selected functionally significant cases after shared decision-making.",
"Procedure planning considers age, bleeding, salivary ducts, tongue musculature and need for simple release versus formal frenuloplasty.",
"Teach: treat function, not a photograph of a frenulum.",
["Cummings 7e: Ankyloglossia and Tight Maxillary Frenula"]),
_v10_module("Pediatric Reflux / Eosinophilic Esophagitis",
"Feeding difficulty, dysphagia, chronic cough/airway symptoms and aspiration may involve reflux or EoE, but nonspecific laryngeal symptoms alone do not establish either diagnosis.",
"Localize symptoms to pharyngeal swallow, esophagus, airway protection and GI inflammatory disease.",
"Use MBS/FEES for aspiration physiology and GI-directed endoscopy/biopsy when EoE or esophageal disease is suspected; avoid empiric diagnostic labels from laryngeal erythema alone.",
"Treat confirmed disease with GI/aerodigestive collaboration while addressing aspiration safety and nutrition.",
"Airway or swallowing surgery should correct a defined structural/functional problem rather than substitute for diagnosis of GI inflammation.",
"Teach: reflux is common and symptoms are nonspecific—prove the mechanism you intend to treat.",
["Cummings 7e: Pediatric Swallowing, LPR/GERD, Eosinophilic Esophagitis, and Aspiration"]),
_v10_module("Laryngotracheal Cleft",
"Recurrent aspiration, cough/choking, pneumonia or feeding-related respiratory symptoms with otherwise unexplained findings should raise concern for a posterior laryngeal/tracheal cleft.",
"Localize the defect along the posterior interarytenoid/cricoid/tracheal wall and distinguish shallow interarytenoid deficiency from deeper cleft extension.",
"Instrumental swallow evaluation defines functional aspiration, but definitive anatomic diagnosis usually requires careful operative palpation/inspection under anesthesia.",
"Conservative feeding/aspiration strategies may suit selected minor defects; injection augmentation or endoscopic/open repair is selected by cleft depth, symptoms and comorbidity.",
"Endoscopic repair requires precise posterior exposure, mucosal preparation/closure and avoidance of injury to adjacent laryngeal structures; deeper defects may require open approaches.",
"Teach: swallowing tests show the consequence; endoscopy defines the cleft anatomy.",
["Cummings 7e: Laryngotracheal Clefts"]),
],
"Sleep Surgery":[
_v10_module("Narcolepsy / Central Hypersomnolence Recognition",
"Excessive daytime sleepiness with cataplexy, sleep paralysis or hypnagogic phenomena points beyond obstructive snoring and toward central hypersomnolence.",
"Localize the problem to sleep-wake regulation rather than upper-airway collapse.",
"Confirm adequate sleep and exclude untreated OSA/medications before sleep-medicine testing such as PSG followed by MSLT when indicated.",
"Refer/manage through sleep medicine; ENT surgery does not treat narcolepsy, though coexisting OSA may still need independent treatment.",
"The operative decision is to avoid attributing hypersomnolence to anatomy when the physiology is central.",
"Teach: sleepiness is not synonymous with OSA.",
["Cummings 7e: Sleep Apnea and Sleep Disorders"]),
_v10_module("Restless Legs / Periodic Limb Movement Disorders",
"RLS is an urge to move the legs with uncomfortable sensations, worse at rest/evening and relieved by movement; PLMS are repetitive movements during sleep and are not the same diagnosis.",
"Localize symptoms to sensorimotor/sleep physiology rather than airway obstruction.",
"Review medications, renal/neurologic contributors and iron status when clinically appropriate; PSG is useful for PLMS but RLS is primarily clinical.",
"Treat reversible contributors and coordinate sleep/neurology management. Avoid surgical OSA pathways unless independent obstruction is present.",
"No ENT operation treats RLS/PLMD; the advanced skill is recognizing the alternate source of disrupted sleep.",
"Teach: a restless sleeper may need iron/sleep-neurology evaluation, not a bigger airway operation.",
["Cummings 7e: Sleep Apnea and Sleep Disorders"]),
_v10_module("Circadian Rhythm Sleep-Wake Disorders",
"Sleep difficulty caused by misalignment of biologic timing differs from insomnia caused by inability to sleep despite appropriate timing.",
"Localize the issue to circadian phase and work/school/light schedule rather than pharyngeal anatomy.",
"Use sleep logs/actigraphy and schedule history; distinguish delayed/advanced phase, shift-work and jet-lag patterns.",
"Behavioral timing, light and melatonin-based strategies belong in sleep medicine; treat coexisting OSA independently.",
"ENT surgery does not correct circadian misalignment.",
"Teach: ask when the patient can sleep normally—not only whether they can sleep.",
["Cummings 7e: Sleep Apnea and Sleep Disorders"]),
],
}

# Add only genuinely new topic titles; when a nearby existing module exists, the new module supplies the missing Cummings dimension.
_existing_v10={m['topic'] for mods in DEEP_MODULES_V6.values() for m in mods}
for _domain,_mods in CUMMINGS_RECONCILIATION_V10.items():
    _bucket=DEEP_MODULES_V6.setdefault(_domain,[])
    for _m in _mods:
        if _m['topic'] not in _existing_v10:
            _bucket.append(_m); _existing_v10.add(_m['topic'])

# ---------- Surgical anatomy: regional -> surgical -> approach anatomy ----------
ANATOMY_EXPANSION_V10 = [
{"region":"Otology / Neurotology","topic":"Auditory Pathway — Cochlea to Cortex","landmarks":["organ of Corti","spiral ganglion/CN VIII","cochlear nuclei","superior olivary complex","lateral lemniscus","inferior colliculus","medial geniculate","auditory cortex"],"danger":["cochlear nerve deficiency","brainstem pathway injury","central auditory processing limitation"],"or_link":"Cochlear Implantation","pearl":"Tie every auditory test to the structure that generates it; hearing restoration depends on an intact usable downstream pathway."},
{"region":"Otology / Neurotology","topic":"Vestibular End Organs / Nerve Divisions / Central Pathways","landmarks":["utricle","saccule","horizontal/superior/posterior canals","Scarpa ganglion","superior/inferior vestibular nerves","vestibular nuclei","cerebellum"],"danger":["vestibular nerve injury","labyrinthine injury","central compensation failure"],"or_link":"Vestibular Schwannoma","pearl":"Canal/otolith anatomy explains why vHIT, calorics and VEMPs can disagree without being contradictory."},
{"region":"Otology / Neurotology","topic":"Eustachian Tube / Tensor–Levator Relationships","landmarks":["bony ET","cartilaginous ET","torus tubarius","tensor veli palatini","levator veli palatini","pterygoid plates"],"danger":["ICA near skull base","palatal muscles","nasopharyngeal mucosa"],"or_link":"Eustachian Tube Dilation","pearl":"The pediatric cleft-palate/OME relationship makes sense only when you understand muscular opening of the cartilaginous tube."},
{"region":"Otology / Neurotology","topic":"Cochlea / Vestibule / Semicircular Canal Microanatomy","landmarks":["basal turn","round window","oval window","vestibule","ampullae","superior canal arcuate eminence","facial nerve labyrinthine segment"],"danger":["cochlea","vestibule","facial nerve","IAC"],"or_link":"Stapedotomy","pearl":"Small millimeters matter: oval/round windows, facial nerve and labyrinth form the inner boundary of middle-ear surgery."},
{"region":"Otology / Neurotology","topic":"Middle Cranial Fossa Approach Corridor","landmarks":["zygomatic root","middle meningeal artery","GSPN","arcuate eminence","IAC","petrous ICA"],"danger":["facial nerve","cochlea","labyrinth","temporal lobe","ICA"],"or_link":"Middle Fossa Skull Base Approach","pearl":"Use multiple landmarks to find the IAC—arcuate eminence alone is not a reliable compass in every patient."},
{"region":"Otology / Neurotology","topic":"Retrosigmoid / CPA Approach Corridor","landmarks":["transverse-sigmoid junction","sigmoid sinus","CPA cistern","CN VII/VIII complex","lower cranial nerves","IAC porus"],"danger":["sigmoid/transverse sinus","brainstem","CN VII/VIII","CN IX-XI","AICA/PICA"],"or_link":"Retrosigmoid Skull Base Approach","pearl":"The corridor preserves the labyrinth but trades for cerebellar/CPA working anatomy and variable hearing preservation."},
{"region":"Otology / Neurotology","topic":"Translabyrinthine Approach Corridor","landmarks":["mastoid","labyrinth","IAC","facial nerve","sigmoid sinus","middle/posterior fossa dura"],"danger":["facial nerve","sigmoid sinus","jugular bulb","ICA","CSF leak"],"or_link":"Translabyrinthine Skull Base Approach","pearl":"Sacrificing labyrinthine hearing creates a direct IAC/CPA corridor when useful hearing is not being preserved."},
{"region":"Otology / Neurotology","topic":"Jugular Foramen / Infratemporal Approach Corridor","landmarks":["jugular bulb","carotid canal","styloid complex","facial nerve mastoid segment","CN IX-XI","hypoglossal canal"],"danger":["ICA","IJV/jugular bulb","facial nerve","lower cranial nerves","CN XII"],"or_link":"Jugular Foramen Tumor Approach","pearl":"Lower-cranial-nerve function often drives morbidity more than the size of the tumor itself."},
{"region":"Laryngology / Voice / Swallowing","topic":"Pharyngeal Constrictors / Superior Laryngeal Neurovascular Relationships","landmarks":["superior/middle/inferior constrictors","thyrohyoid membrane","internal SLN","external SLN","superior laryngeal artery","piriform sinus"],"danger":["internal SLN","EBSLN","superior laryngeal vessels","pharyngeal mucosa"],"or_link":"Conservation Laryngectomy","pearl":"The thyrohyoid membrane is a gateway for internal SLN/vessels and an oncologic boundary around the supraglottis/piriform region."},
{"region":"Facial Plastics / Trauma","topic":"TMJ / Occlusion / Infratemporal Functional Anatomy","landmarks":["condyle","glenoid fossa","articular disc","lateral pterygoid","masseter","medial pterygoid","dental occlusion"],"danger":["auriculotemporal nerve","maxillary artery","facial nerve branches","EAC"],"or_link":"Mandible ORIF","pearl":"Occlusion is the functional readout of the mandibular-TMJ system; referred otalgia often starts here."},
{"region":"Pediatric Otolaryngology","topic":"Cleft Palate Levator Sling / Tensor / Eustachian Tube","landmarks":["levator veli palatini","tensor veli palatini","palatal aponeurosis","hamulus","cartilaginous ET","posterior hard palate"],"danger":["greater palatine neurovascular bundle","ET function","velopharyngeal closure"],"or_link":"Palatoplasty / Cleft Palate Repair","pearl":"Palatoplasty is muscular reconstruction as much as mucosal closure; the same anatomy helps explain chronic middle-ear disease."},
{"region":"Pediatric Otolaryngology","topic":"Auricular Framework / Microtia Reconstruction Anatomy","landmarks":["helix","antihelix","concha","tragus","lobule","temporoparietal fascia","mastoid skin envelope"],"danger":["superficial temporal vessels","facial nerve branches","skin/flap vascularity"],"or_link":"Microtia Reconstruction","pearl":"Framework shape is only half the operation—the vascularized skin/fascial envelope determines whether the reconstruction survives."},
]
_existing_anat={x['topic'] for x in ANATOMY_ATLAS_V97}
for _x in ANATOMY_EXPANSION_V10:
    if _x['topic'] not in _existing_anat:
        ANATOMY_ATLAS_V97.append(_x); _existing_anat.add(_x['topic'])

# ---------- Audiologic electrophysiology Interpretation Lab ----------
INTERPRETATION_LABS['audiologic-electrophysiology']={
 'title':'Audiologic Electrophysiology Lab','icon':'〰️',
 'subtitle':'Waveform generator → technical validity → localization → clinical consequence.',
 'framework':['Question','Signal generator','Technical quality','Threshold/latency/amplitude','Side-to-side pattern','Cochlear vs neural','Clinical consequence'],
 'source_note':'Original teaching cases reconciled to Cummings 7e diagnostic audiology/electrophysiology concepts; waveform examples are schematic/text-based unless an open visual is linked.',
 'resources':[],
 'cases':[
  {'id':'ae1','concept_id':'ae-oae-abr','level':1,'prompt':'OAEs are present but the ABR is absent or grossly abnormal in an infant. What localization pattern should you consider?','answer':'Outer-hair-cell function is present while synchronized neural transmission is abnormal; auditory neuropathy spectrum is a key consideration when the clinical context and technical quality fit.','why':'The tests have different generators, so the discordance is localizing rather than contradictory.','follow':'What technical or middle-ear factors could falsely alter either test?'},
  {'id':'ae2','concept_id':'ae-abr-latency','level':2,'prompt':'One ear has reproducibly prolonged interpeak latency compared with the other despite similar peripheral hearing thresholds. What question does that raise?','answer':'A retrocochlear/brainstem conduction abnormality becomes more plausible and should be interpreted with the full waveform, audiogram and clinical context.','why':'Interpeak timing reflects neural conduction beyond simple audibility.','follow':'Why is a single poorly formed waveform insufficient?'},
  {'id':'ae3','concept_id':'ae-threshold','level':2,'prompt':'A sleeping infant cannot provide reliable behavioral thresholds. What role can frequency-specific electrophysiology play?','answer':'Electrophysiologic threshold estimation can approximate auditory sensitivity and guide early amplification while behavioral confirmation is pursued as development allows.','why':'The goal is timely auditory access without pretending the physiologic estimate is identical to later behavioral hearing.','follow':'What additional cochlear/middle-ear tests make the interpretation stronger?'},
  {'id':'ae4','concept_id':'ae-oae','level':2,'prompt':'OAEs are absent bilaterally. Can you conclude the child has auditory neuropathy?','answer':'No. Absent OAEs can result from cochlear outer-hair-cell dysfunction or conductive/middle-ear factors; auditory neuropathy classically requires evidence of preserved cochlear outer-hair-cell function with abnormal neural synchrony, though OAEs can evolve.','why':'One absent test does not uniquely identify the lesion.','follow':'What middle-ear assessment should accompany OAE interpretation?'},
  {'id':'ae5','concept_id':'ae-ecog','level':3,'prompt':'What is the conceptual difference between ECoG and a far-field ABR?','answer':'ECoG records cochlear/auditory-nerve potentials close to the cochlea, while ABR summarizes synchronized neural activity through auditory nerve and brainstem generators.','why':'Knowing the generator tells you what each test can and cannot localize.','follow':'Why should ECoG never be interpreted in isolation?'},
  {'id':'ae6','concept_id':'ae-io-monitor','level':4,'prompt':'During skull-base surgery the auditory monitoring signal deteriorates abruptly. What is the first reasoning sequence?','answer':'Confirm technical integrity and physiologic/anesthetic factors, communicate the change immediately, stop or reverse the provoking maneuver when appropriate, and reassess the auditory pathway before continuing.','why':'Monitoring is useful only when signal changes trigger rapid, structured communication and action.','follow':'What makes trend more useful than one isolated amplitude?'},
  {'id':'ae7','concept_id':'ae-newborn','level':3,'prompt':'A newborn screen is referred in one ear. What common systems error must you avoid?','answer':'Do not treat a failed screen as a final diagnosis or allow follow-up to disappear; diagnostic audiology and timely tracking are required.','why':'Screening identifies risk; it does not define type/severity of hearing loss.','follow':'Why does developmental timing make follow-up urgent?'},
  {'id':'ae8','concept_id':'ae-integrate','level':5,'prompt':'Behavioral audiometry suggests severe SNHL, OAEs are absent, ABR morphology is appropriate for the degree of loss, and MRI shows an intact cochlear nerve. What is the integrated localization?','answer':'The data are concordant with severe peripheral/cochlear sensorineural loss rather than a primary neural dyssynchrony syndrome.','why':'The strongest interpretation integrates independent tests instead of allowing one modality to dominate.','follow':'How does this inform hearing-device counseling?'}
 ]
}

# ---------- OR Tomorrow additions ----------
def _v10_or(slug,title,domain,indications,steps,danger,follow,linked):
    OR_PREP_REGISTRY[slug]={"slug":slug,"title":title,"domain":domain,"indications":indications,"steps":steps,
        "danger":danger,"attending_followup":follow,"linked_topic":linked,"status":"v10-cummings-reconciled",
        "source_basis":["Cummings Otolaryngology—Head and Neck Surgery, 7th ed."]}

_v10_or('conservation-laryngectomy','Open Partial / Conservation Laryngectomy','Head & Neck Oncology',
'Selected laryngeal cancers where complete oncologic resection is compatible with preservation of a functional larynx and the patient has adequate pulmonary/swallowing reserve.',
['Confirm exposure, tumor extent, mobility and reconstruction plan before incision.','Expose laryngeal framework and perform neck treatment when indicated.','Enter away from tumor and define intralaryngeal extent under direct visualization.','Resect the planned supraglottic/supracricoid or other conservation specimen with oncologic margins and preserve required functional units.','Perform pexy/reconstruction with precise alignment and tension.','Establish postoperative airway/nutrition plan and anticipate aspiration rehabilitation.'],
['tumor violation/margin failure','arytenoid/cricoarytenoid function','RLN','aspiration','airway edema/stenosis','chondronecrosis'],
[['What makes someone a bad conservation candidate?','Tumor extent that cannot be cleared while preserving required functional units, poor pulmonary/swallowing reserve, or inability to rehabilitate safely.'],['Why is one functioning arytenoid so important?','It contributes critically to airway protection and neoglottic function after major partial laryngeal resection.']],
'Open Partial / Conservation Laryngectomy')
_v10_or('transoral-laser-laryngeal-cancer','Transoral Laser Microsurgery — Laryngeal Cancer','Head & Neck Oncology',
'Selected laryngeal tumors with adequate transoral exposure and a resection path that can achieve oncologic control while preserving function.',
['Confirm laser airway/fire protocol and protective setup.','Expose the entire lesion and define deep/anatomic limits.','Map specimen orientation and anticipated margins.','Perform controlled laser incision/resection, using tumor transection only when it improves 3-D mapping and margin assessment.','Orient/send margins deliberately and obtain hemostasis.','Reassess airway, functional tissue preservation and postoperative swallowing/voice needs.'],
['airway fire','deep-space/cartilage extension','anterior commissure orientation','thermal injury','bleeding','margin confusion'],
[['Why can piecemeal resection still be oncologic?','When the surgeon preserves 3-D orientation and maps deep and peripheral margins deliberately rather than treating fragments as unoriented debris.'],['What defeats TLM?','Inadequate exposure or extent that prevents safe visualization/control of margins and critical structures.']],
'Transoral Laser Microsurgery for Laryngeal Cancer')
_v10_or('microtia-reconstruction','Microtia Reconstruction','Pediatric Otolaryngology',
'Patient-selected auricular reconstruction after coordinated counseling on hearing rehabilitation, reconstructive options, timing, donor site and expected staging.',
['Confirm ear position/symmetry plan and coordinate any atresia surgery sequence.','Design/harvest framework material when using autologous reconstruction.','Create precise skin pocket while protecting vascularized envelope.','Assemble/place framework with stable position and projection plan.','Close without compromising skin perfusion and manage drains/bolsters as appropriate.','Stage elevation/projection or revisions according to technique.'],
['skin necrosis/framework exposure','temporoparietal fascia/superficial temporal vessels','facial nerve branches','donor-site morbidity','framework malposition'],
[['Why coordinate with atresia surgery?','Canal surgery can scar or alter the vascularized skin/fascial envelope needed for auricular reconstruction.'],['What is the reconstructive endpoint?','A durable symmetric auricular framework with viable coverage—not simply a technically perfect cartilage sculpture.']],
'Microtia Reconstruction')
_v10_or('palatoplasty','Palatoplasty / Cleft Palate Repair','Pediatric Otolaryngology',
'Cleft palate repair to restore separation of oral/nasal cavities and reconstruct functional palatal musculature for feeding/speech while minimizing fistula and growth burden.',
['Mark cleft anatomy and planned mucosal/muscular flaps.','Elevate oral/nasal layers while preserving vascular pedicles.','Release abnormal levator orientation and reconstruct the levator sling/length as planned.','Close nasal layer without tension.','Complete muscle repair and oral closure.','Check hemostasis, airway and postoperative feeding plan.'],
['greater palatine neurovascular bundle','levator/tensor injury','fistula','velopharyngeal insufficiency','airway obstruction','bleeding'],
[['Why is muscle reconstruction central?','Cleft palate is a maloriented muscular problem as well as a mucosal gap; speech/velopharyngeal function depends on the reconstructed sling.'],['Why does ENT care continue after repair?','OME/hearing and speech/resonance require longitudinal surveillance.']],
'Cleft Lip / Palate — ENT Surgical Fundamentals')
_v10_or('laryngotracheal-cleft-repair','Laryngotracheal Cleft Repair','Pediatric Otolaryngology',
'Symptomatic posterior laryngeal/tracheal cleft with aspiration/respiratory burden that persists despite appropriate conservative strategy or has anatomy requiring repair.',
['Perform complete airway assessment and palpate the posterior interarytenoid/cricoid defect.','Optimize exposure and ventilation plan.','Define the inferior extent of the cleft.','Freshen/separate mucosal edges as required by technique.','Close the defect in precise layers while protecting laryngeal framework/mucosa.','Reassess airway and establish postoperative feeding/swallow plan.'],
['airway loss','posterior glottic scar/stenosis','repair dehiscence','persistent aspiration','RLN-related structures','esophageal injury'],
[['Why is swallow imaging not enough to classify the cleft?','It demonstrates aspiration physiology but not the exact posterior anatomic depth; operative inspection/palpation defines the lesion.'],['When might injection augmentation be considered?','Selected shallow interarytenoid deficiency can be treated diagnostically/therapeutically with augmentation depending on symptoms and center practice.']],
'Laryngotracheal Cleft')
_v10_or('transnasal-esophagoscopy','Transnasal Esophagoscopy','Laryngology / Voice / Swallowing',
'Office evaluation of selected pharyngeal/esophageal symptoms, surveillance or biopsy questions in a patient who can tolerate unsedated transnasal endoscopy.',
['Topicalize/decongest the selected nasal passage.','Advance under continuous visualization through nasopharynx/hypopharynx.','Pass the UES gently with patient cooperation; never force against resistance.','Survey esophageal mucosa and landmarks systematically.','Perform selected biopsy/intervention only within the scope of office safety.','Document findings and decide whether conventional EGD/imaging/motility evaluation is still required.'],
['epistaxis','laryngeal spasm','perforation','missed distal disease','inadequate visualization'],
[['What is TNE best at?','Efficient office evaluation when the question is within its visualization/biopsy limits and sedation can be avoided.'],['When should you stop and escalate?','Unexpected resistance, poor tolerance, inadequate visualization or a problem requiring therapeutic GI endoscopy.']],
'Transnasal Esophagoscopy')
_v10_or('rigid-tracheobronchoscopy','Rigid Tracheobronchoscopy','Laryngology / Voice / Swallowing',
'Diagnostic/therapeutic central-airway evaluation where rigid instrumentation provides superior airway control, foreign-body access, dilation/debridement or large-channel suction.',
['Agree on ventilation plan and backup airway with anesthesia.','Protect teeth/lips and obtain laryngeal exposure.','Pass the rigid scope under direct visualization without levering on laryngeal structures.','Inspect subglottis, trachea, carina and both main bronchi systematically.','Perform planned foreign-body/interventional work while maintaining oxygenation and hemostasis.','Reinspect for trauma/residual lesion and plan postoperative airway monitoring.'],
['hypoxia','airway loss','dental/laryngeal injury','bleeding','pneumothorax','airway fire with laser'],
[['Why use rigid instead of flexible bronchoscopy?','It offers airway control, ventilation options, large working channel and strong instrumentation for selected central-airway problems.'],['What is the key nontechnical step?','Continuous closed-loop communication with anesthesia about ventilation and oxygenation.']],
'Tracheobronchial Endoscopy Principles')
_v10_or('free-flap-takeback','Free-Flap Compromise — Take-Back / Salvage','Head & Neck Oncology',
'Clinical or monitoring evidence of threatened free-flap perfusion where a mechanical/pedicle cause is possible and salvage depends on rapid restoration of flow.',
['Activate the reconstructive team and correct major systemic perfusion/oxygenation issues while preparing the OR.','Open the inset/neck enough to release hematoma or pedicle compression and inspect the entire pedicle.','Determine arterial inflow versus venous outflow problem and identify kinking/thrombosis/anastomotic failure.','Revise/clear the compromised segment according to intraoperative findings and restore flow.','Confirm tissue reperfusion clinically and with available adjuncts.','Re-inset without compression and intensify postoperative monitoring.'],
['delay to re-exploration','carotid/recipient-vessel injury','reperfusion injury','recurrent thrombosis','hematoma','nonviable tissue'],
[['Why is venous congestion time-sensitive?','Progressive stasis leads to microcirculatory failure and thrombosis, making delayed salvage progressively less likely.'],['Can a Doppler replace the exam?','No. Monitoring devices support serial clinical assessment and trend recognition.']],
'Free-Flap Monitoring / Compromise / Salvage')
_v10_or('middle-fossa-skull-base','Middle Fossa Skull-Base Approach','Otology / Neurotology',
'Selected IAC/superior canal/petrous lesions where a superior corridor and potential hearing preservation are appropriate.',
['Position and perform temporal craniotomy with neurotology-neurosurgery coordination.','Elevate middle-fossa dura and identify reliable landmarks including middle meningeal/GSPN and petrous ridge/arcuate region.','Localize the IAC or target corridor using multiple anatomic references.','Drill with constant awareness of cochlea, labyrinth, facial nerve and petrous ICA.','Address the lesion while preserving neural structures according to indication.','Obtain watertight closure and manage CSF/temporal-lobe risks.'],
['facial nerve','cochlea/labyrinth','petrous ICA','temporal lobe','CSF leak','middle meningeal artery'],
[['Why not rely on the arcuate eminence alone?','Its relationship to the superior canal varies; multiple landmarks improve IAC localization.'],['What functional goal often favors this approach?','Selected hearing-preservation access to lateral IAC/superior petrous targets.']],
'Lateral Skull-Base Tumor Framework')
_v10_or('retrosigmoid-skull-base','Retrosigmoid Skull-Base Approach','Otology / Neurotology',
'Selected CPA/posterior-fossa lesions where a posterior corridor provides access while preserving the labyrinth and potentially hearing.',
['Position and identify transverse-sigmoid junction.','Create retrosigmoid craniotomy/craniectomy and open dura with venous-sinus protection.','Release CSF and expose CPA under minimal cerebellar retraction.','Identify tumor relative to CN VII/VIII, lower cranial nerves and vessels; drill posterior IAC when needed.','Resect/decompress according to functional goals and monitoring.','Close dura/mastoid air cells meticulously to reduce CSF leak.'],
['sigmoid/transverse sinus','CN VII/VIII','CN IX-XI','AICA/PICA','brainstem/cerebellum','CSF leak'],
[['What does this approach preserve anatomically?','The labyrinth is preserved, so hearing preservation may be possible depending on tumor and cochlear-nerve function.'],['What is the tradeoff?','Posterior-fossa/cerebellar working anatomy and variable access to the far lateral IAC fundus.']],
'Lateral Skull-Base Tumor Framework')
_v10_or('translabyrinthine-skull-base','Translabyrinthine Skull-Base Approach','Otology / Neurotology',
'IAC/CPA lesions when useful hearing is absent or intentionally sacrificed to obtain direct lateral access and early facial-nerve identification.',
['Perform mastoidectomy and identify sigmoid, tegmen, facial nerve and labyrinth.','Exenterate labyrinth systematically while protecting facial nerve and critical vascular structures.','Skeletonize/open IAC with broad exposure from fundus to porus.','Identify facial nerve and tumor relationships, then perform resection with monitoring.','Obliterate air-cell tracts and reconstruct the defect to prevent CSF leak.','Close with attention to wound and CSF-pressure management.'],
['facial nerve','jugular bulb/sigmoid','petrous ICA','CSF leak','lower cranial nerves/brainstem'],
[['Why choose translabyrinthine?','It provides a direct IAC/CPA corridor without cerebellar retraction when hearing is not being preserved.'],['What must be accepted?','Ipsilateral labyrinthine hearing is sacrificed.']],
'Lateral Skull-Base Tumor Framework')
_v10_or('jugular-foramen-tumor','Jugular Foramen Tumor Approach','Otology / Neurotology',
'Selected jugular-foramen/lower-skull-base tumors requiring surgery after balancing growth, hearing, lower-CN function, vascularity and radiotherapy/observation alternatives.',
['Document baseline IX-XII, facial and hearing function and vascular anatomy.','Plan exposure based on tumor extension and carotid/jugular relationships.','Obtain proximal/distal vascular control strategy before deep dissection.','Identify/preserve or deliberately manage lower cranial nerves according to tumor involvement and goals.','Resect/debulk with strict carotid/jugular/facial-nerve awareness.','Reconstruct skull base and plan swallowing/voice rehabilitation proactively.'],
['ICA','jugular bulb/IJV','CN IX-XII','facial nerve','aspiration','CSF leak'],
[['What predicts morbidity?','Baseline and postoperative lower-cranial-nerve function often drive swallowing/voice morbidity more than tumor size alone.'],['Why might surgery not be first choice?','Some paragangliomas/other lesions can be observed or treated with radiation depending on age, growth and functional risk.']],
'Lateral Skull-Base Tumor Framework')

# Rebuild adaptive items so every v10 topic participates in the same six-level longitudinal path.
ADAPTIVE_ITEMS_V99=[]
for _domain,_mods in DEEP_MODULES_V6.items():
    for _m in _mods:
        _id=_v6_item_id(_domain,_m['topic'])
        for _stage in ['recognize','localize','workup','manage','operate','teach']:
            ADAPTIVE_ITEMS_V99.append({
              'id':_id+'-'+_stage,'concept_id':_id,'domain':_domain,'topic':_m['topic'],
              'stage':_stage,'display_stage':'advanced' if _stage=='operate' else _stage,
              'prompt':{'recognize':'Recognize the pattern.','localize':'Localize the problem.','workup':'Evaluate it efficiently.','manage':'Build the management sequence.','operate':'Make the advanced decision.','teach':'Teach the mental model.'}[_stage],
              'answer':_m[_stage],
              'minutes':{'recognize':3,'localize':3,'workup':4,'manage':4,'operate':6,'teach':4}[_stage],
              'level':{'recognize':1,'localize':2,'workup':3,'manage':4,'operate':5,'teach':6}[_stage],
              'tags':_m.get('tags',_tags_v94(_m['topic'],_domain))})
ADAPTIVE_ITEMS_V97=ADAPTIVE_ITEMS_V99; ADAPTIVE_ITEMS_V96=ADAPTIVE_ITEMS_V99; ADAPTIVE_ITEMS_V95=ADAPTIVE_ITEMS_V99; ADAPTIVE_ITEMS_V94=ADAPTIVE_ITEMS_V99; ADAPTIVE_ITEMS_V91=ADAPTIVE_ITEMS_V99

TEXTBOOK_SOURCE_SET_V10 = TEXTBOOK_SOURCE_SET_V99 + [
 {"title":"Cummings Otolaryngology—Head and Neck Surgery","edition":"7th (2021)","role":"full-volume reconciliation for breadth, durable anatomy/pathophysiology, diagnostic frameworks and operative depth; current management is calibrated to newer guidelines where applicable"}
]



# v10.0.3 anatomy visual mapping
ANATOMY_VISUALS_V1003 = {'Temporal Bone Surgical Map': 'anatomy/01-temporal-bone-surgical-map.svg', 'Middle Ear / Ossicular Anatomy': 'anatomy/02-middle-ear-ossicular-anatomy.svg', 'Facial Nerve — Intratemporal Course': 'anatomy/03-facial-nerve-intratemporal-course.svg', 'Sinonasal Lateral Wall / Ostiomeatal Complex': 'anatomy/04-sinonasal-lateral-wall-ostiomeatal-complex.svg', 'Frontal Recess Anatomy': 'anatomy/05-frontal-recess-anatomy.svg', 'Sphenoid / Central Skull Base': 'anatomy/06-sphenoid-central-skull-base.svg', 'Pterygopalatine / Infratemporal Spaces': 'anatomy/07-pterygopalatine-infratemporal-spaces.svg', 'Neck Levels / Fascial Compartments': 'anatomy/08-neck-levels-fascial-compartments.svg', 'Parapharyngeal / Retropharyngeal Spaces': 'anatomy/09-parapharyngeal-retropharyngeal-spaces.svg', 'Thyroid / RLN / EBSLN Anatomy': 'anatomy/10-thyroid-rln-ebsln-anatomy.svg', 'Parathyroid Embryology / Ectopic Map': 'anatomy/11-parathyroid-embryology-ectopic-map.svg', 'Parotid / Facial Nerve Anatomy': 'anatomy/12-parotid-facial-nerve-anatomy.svg', 'Submandibular Triangle / Floor of Mouth': 'anatomy/13-submandibular-triangle-floor-of-mouth.svg', 'Laryngeal Framework / Intrinsic Muscles': 'anatomy/14-laryngeal-framework-intrinsic-muscles.svg', 'Pharynx / UES / Cervical Esophagus': 'anatomy/15-pharynx-ues-cervical-esophagus.svg', 'Pediatric Laryngotracheal Airway': 'anatomy/16-pediatric-laryngotracheal-airway.svg', 'Facial Buttresses / Midface Trauma': 'anatomy/17-facial-buttresses-midface-trauma.svg', 'Nasal Support / Valve Anatomy': 'anatomy/18-nasal-support-valve-anatomy.svg', 'Tracheostomy / Cervical Trachea Anatomy': 'anatomy/19-tracheostomy-cervical-trachea-anatomy.svg', 'Oral Tongue / Floor of Mouth': 'anatomy/20-oral-tongue-floor-of-mouth.svg', 'Superficial Face — Vessels / Facial Nerve / SMAS': 'anatomy/21-superficial-face-vessels-facial-nerve-smas.svg', 'Scalp / Forehead Surgical Layers': 'anatomy/22-scalp-forehead-surgical-layers.svg', 'Orbit — Compartments / Canthi / Lacrimal System': 'anatomy/23-orbit-compartments-canthi-lacrimal-system.svg', 'Mandible / TMJ / Masticator Space': 'anatomy/24-mandible-tmj-masticator-space.svg', 'Ethmoid Skull Base / Lateral Lamella / AEA': 'anatomy/25-ethmoid-skull-base-lateral-lamella-aea.svg', 'Pterygopalatine Fossa / Autonomic Pathways': 'anatomy/26-pterygopalatine-fossa-autonomic-pathways.svg', 'Infratemporal Fossa / Internal Maxillary Artery': 'anatomy/27-infratemporal-fossa-internal-maxillary-artery.svg', 'Anterior / Central Cranial Base Foramina': 'anatomy/28-anterior-central-cranial-base-foramina.svg', 'Jugular Foramen / Hypoglossal Canal / Lower Cranial Nerves': 'anatomy/29-jugular-foramen-hypoglossal-canal-lower-cranial-nerves.svg', 'IAC / CPA / Labyrinth Relationships': 'anatomy/30-iac-cpa-labyrinth-relationships.svg', 'External Carotid Artery Branches / Major Hemorrhage Anatomy': 'anatomy/31-external-carotid-artery-branches-major-hemorrhage-anatomy.svg', 'Lateral Neck Triangles / CN XI / Brachial Plexus': 'anatomy/32-lateral-neck-triangles-cn-xi-brachial-plexus.svg', 'Thoracic Inlet / Root of Neck': 'anatomy/33-thoracic-inlet-root-of-neck.svg', 'Mediastinal Continuity of Deep Neck Spaces': 'anatomy/34-mediastinal-continuity-of-deep-neck-spaces.svg', 'Vagus / Sympathetic Chain / Carotid Space': 'anatomy/35-vagus-sympathetic-chain-carotid-space.svg', 'Superior Laryngeal Nerve / Cricothyroid Space': 'anatomy/36-superior-laryngeal-nerve-cricothyroid-space.svg', 'Laryngeal Neurovascular Anatomy': 'anatomy/37-laryngeal-neurovascular-anatomy.svg', 'Free-Flap Recipient Vessels / Reconstructive Neck': 'anatomy/38-free-flap-recipient-vessels-reconstructive-neck.svg', 'Auditory Pathway — Cochlea to Cortex': 'anatomy/39-auditory-pathway-cochlea-to-cortex.svg', 'Vestibular End Organs / Nerve Divisions / Central Pathways': 'anatomy/40-vestibular-end-organs-nerve-divisions-central-pathways.svg', 'Eustachian Tube / Tensor–Levator Relationships': 'anatomy/41-eustachian-tube-tensor-levator-relationships.svg', 'Cochlea / Vestibule / Semicircular Canal Microanatomy': 'anatomy/42-cochlea-vestibule-semicircular-canal-microanatomy.svg', 'Middle Cranial Fossa Approach Corridor': 'anatomy/43-middle-cranial-fossa-approach-corridor.svg', 'Retrosigmoid / CPA Approach Corridor': 'anatomy/44-retrosigmoid-cpa-approach-corridor.svg', 'Translabyrinthine Approach Corridor': 'anatomy/45-translabyrinthine-approach-corridor.svg', 'Jugular Foramen / Infratemporal Approach Corridor': 'anatomy/46-jugular-foramen-infratemporal-approach-corridor.svg', 'Pharyngeal Constrictors / Superior Laryngeal Neurovascular Relationships': 'anatomy/47-pharyngeal-constrictors-superior-laryngeal-neurovascular-relationships.svg', 'TMJ / Occlusion / Infratemporal Functional Anatomy': 'anatomy/48-tmj-occlusion-infratemporal-functional-anatomy.svg', 'Cleft Palate Levator Sling / Tensor / Eustachian Tube': 'anatomy/49-cleft-palate-levator-sling-tensor-eustachian-tube.svg', 'Auricular Framework / Microtia Reconstruction Anatomy': 'anatomy/50-auricular-framework-microtia-reconstruction-anatomy.svg'}
for _a in ANATOMY_ATLAS_V97:
    _a['visual']=ANATOMY_VISUALS_V1003.get(_a.get('topic'))


# v10.0.5 — real/open-license anatomy image metadata
ANATOMY_REAL_IMAGE_LIBRARY_V1005 = {'temporal': {'url': 'https://commons.wikimedia.org/wiki/Special:Redirect/file/Gray138.png', 'source': 'https://commons.wikimedia.org/wiki/File:Gray138.png', 'credit': "Gray's Anatomy, Plate 138 · public domain"}, 'middle_ear': {'url': 'https://commons.wikimedia.org/wiki/Special:Redirect/file/Gray911.png', 'source': 'https://commons.wikimedia.org/wiki/File:Gray911.png', 'credit': "Gray's Anatomy, Plate 911 · public domain"}, 'labyrinth': {'url': 'https://commons.wikimedia.org/wiki/Special:Redirect/file/Gray922.png', 'source': 'https://commons.wikimedia.org/wiki/File:Gray922.png', 'credit': "Gray's Anatomy, Plate 922 · public domain"}, 'sinonasal': {'url': 'https://commons.wikimedia.org/wiki/Special:Redirect/file/Gray170.png', 'source': 'https://commons.wikimedia.org/wiki/File:Gray170.png', 'credit': "Gray's Anatomy, Plate 170 · public domain"}, 'larynx': {'url': 'https://commons.wikimedia.org/wiki/Special:Redirect/file/Gray959.png', 'source': 'https://commons.wikimedia.org/wiki/File:Gray959.png', 'credit': "Gray's Anatomy, Plate 959 · public domain"}, 'trachea': {'url': 'https://commons.wikimedia.org/wiki/Special:Redirect/file/Gray961.png', 'source': 'https://commons.wikimedia.org/wiki/File:Gray961.png', 'credit': "Gray's Anatomy, Plate 961 · public domain"}, 'floor_mouth': {'url': 'https://commons.wikimedia.org/wiki/Special:Redirect/file/Gray1013.png', 'source': 'https://commons.wikimedia.org/wiki/File:Gray1013.png', 'credit': "Gray's Anatomy, Plate 1013 · public domain"}, 'pharynx': {'url': 'https://commons.wikimedia.org/wiki/Special:Redirect/file/Gray1028.png', 'source': 'https://commons.wikimedia.org/wiki/File:Gray1028.png', 'credit': "Gray's Anatomy, Plate 1028 · public domain"}, 'auditory': {'url': 'https://commons.wikimedia.org/wiki/Special:Redirect/file/Auditory_Pathway.png', 'source': 'https://commons.wikimedia.org/wiki/File:Auditory_Pathway.png', 'credit': 'Jonathan E. Peelle · CC BY 4.0'}, 'cranial_base': {'url': 'https://commons.wikimedia.org/wiki/Special:Redirect/file/Gray193_-_Cranial_fossae.png', 'source': 'https://commons.wikimedia.org/wiki/File:Gray193_-_Cranial_fossae.png', 'credit': "Gray's Anatomy · cranial fossae · public domain"}, 'eca': {'url': 'https://commons.wikimedia.org/wiki/Special:Redirect/file/External_carotid_artery_with_branches.jpg', 'source': 'https://commons.wikimedia.org/wiki/File:External_carotid_artery_with_branches.jpg', 'credit': 'Sobotta-derived anatomy illustration · public domain'}, 'tmj': {'url': 'https://commons.wikimedia.org/wiki/Special:Redirect/file/Sobo_1909_190.png', 'source': 'https://commons.wikimedia.org/wiki/File:Sobo_1909_190.png', 'credit': 'Sobotta Atlas, 1909 · public domain'}, 'parotid': {'url': 'https://commons.wikimedia.org/wiki/Special:Redirect/file/Gray1023.png', 'source': 'https://commons.wikimedia.org/wiki/File:Gray1023.png', 'credit': "Gray's Anatomy, Plate 1023 · public domain"}, 'thyroid': {'url': 'https://commons.wikimedia.org/wiki/Special:Redirect/file/Thyroid.png', 'source': 'https://commons.wikimedia.org/wiki/File:Thyroid.png', 'credit': "Gray's Anatomy thyroid/neck illustration · public domain"}}
ANATOMY_REAL_IMAGE_TOPIC_MAP_V1005 = {'Temporal Bone Surgical Map': 'temporal', 'Middle Ear / Ossicular Anatomy': 'middle_ear', 'Facial Nerve — Intratemporal Course': 'middle_ear', 'Sinonasal Lateral Wall / Ostiomeatal Complex': 'sinonasal', 'Frontal Recess Anatomy': 'sinonasal', 'Sphenoid / Central Skull Base': 'cranial_base', 'Pterygopalatine / Infratemporal Spaces': 'eca', 'Neck Levels / Fascial Compartments': 'thyroid', 'Parapharyngeal / Retropharyngeal Spaces': 'pharynx', 'Thyroid / RLN / EBSLN Anatomy': 'thyroid', 'Parathyroid Embryology / Ectopic Map': 'thyroid', 'Parotid / Facial Nerve Anatomy': 'parotid', 'Submandibular Triangle / Floor of Mouth': 'floor_mouth', 'Laryngeal Framework / Intrinsic Muscles': 'larynx', 'Pharynx / UES / Cervical Esophagus': 'pharynx', 'Pediatric Laryngotracheal Airway': 'trachea', 'Facial Buttresses / Midface Trauma': 'cranial_base', 'Nasal Support / Valve Anatomy': 'sinonasal', 'Tracheostomy / Cervical Trachea Anatomy': 'trachea', 'Oral Tongue / Floor of Mouth': 'floor_mouth', 'Superficial Face — Vessels / Facial Nerve / SMAS': 'eca', 'Scalp / Forehead Surgical Layers': 'cranial_base', 'Orbit — Compartments / Canthi / Lacrimal System': 'cranial_base', 'Mandible / TMJ / Masticator Space': 'tmj', 'Ethmoid Skull Base / Lateral Lamella / AEA': 'sinonasal', 'Pterygopalatine Fossa / Autonomic Pathways': 'eca', 'Infratemporal Fossa / Internal Maxillary Artery': 'eca', 'Anterior / Central Cranial Base Foramina': 'cranial_base', 'Jugular Foramen / Hypoglossal Canal / Lower Cranial Nerves': 'cranial_base', 'IAC / CPA / Labyrinth Relationships': 'temporal', 'External Carotid Artery Branches / Major Hemorrhage Anatomy': 'eca', 'Lateral Neck Triangles / CN XI / Brachial Plexus': 'thyroid', 'Thoracic Inlet / Root of Neck': 'thyroid', 'Mediastinal Continuity of Deep Neck Spaces': 'pharynx', 'Vagus / Sympathetic Chain / Carotid Space': 'thyroid', 'Superior Laryngeal Nerve / Cricothyroid Space': 'larynx', 'Laryngeal Neurovascular Anatomy': 'larynx', 'Free-Flap Recipient Vessels / Reconstructive Neck': 'eca', 'Auditory Pathway — Cochlea to Cortex': 'auditory', 'Vestibular End Organs / Nerve Divisions / Central Pathways': 'labyrinth', 'Eustachian Tube / Tensor–Levator Relationships': 'middle_ear', 'Cochlea / Vestibule / Semicircular Canal Microanatomy': 'labyrinth', 'Middle Cranial Fossa Approach Corridor': 'cranial_base', 'Retrosigmoid / CPA Approach Corridor': 'cranial_base', 'Translabyrinthine Approach Corridor': 'temporal', 'Jugular Foramen / Infratemporal Approach Corridor': 'cranial_base', 'Pharyngeal Constrictors / Superior Laryngeal Neurovascular Relationships': 'pharynx', 'TMJ / Occlusion / Infratemporal Functional Anatomy': 'tmj', 'Cleft Palate Levator Sling / Tensor / Eustachian Tube': 'pharynx', 'Auricular Framework / Microtia Reconstruction Anatomy': 'temporal'}
for _a in ANATOMY_ATLAS_V97:
    _k=ANATOMY_REAL_IMAGE_TOPIC_MAP_V1005.get(_a.get("topic"))
    _im=ANATOMY_REAL_IMAGE_LIBRARY_V1005.get(_k,{})
    _a["image_url"]=_im.get("url")
    _a["image_source"]=_im.get("source")
    _a["image_credit"]=_im.get("credit")
