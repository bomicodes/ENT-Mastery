"""v20.23 — deepen exact-live General ENT / Emergencies Fluids, Electrolytes & Nutrition.

Durable physiology and perioperative principles are cross-referenced against the connected
Cummings 7e, Pasha 6e and K.J. Lee 12e corpus. Current management is reconciled with
AAP pediatric maintenance-IV-fluid guidance, NICE adult IV-fluid guidance, ESPEN cancer
nutrition guidance and ASPEN refeeding consensus. Textbook rules are treated as foundations,
not substitutes for patient-specific renal/cardiac/endocrine physiology or current guidance.
"""
from concept_check_board_repair_v177 import _find_module

QIDS = ("cc-v112-rec-general-ent-emergencies-ent-fluids-electrolytes-nutrition",)
CID = "v6-general-ent-emergencies-ent-fluids-electrolytes-nutrition"
TOPIC = "ENT Fluids / Electrolytes / Nutrition"

SOURCE_REFS_V223 = [
    {"type":"textbook","citation":"Cummings Otolaryngology: Head and Neck Surgery, 7th ed. (2021), connected Google Drive corpus; full-volume copy verified in the ENT Boards Library on 2026-09-10 (Drive copy 1aR0zp4dvruYaPvGtc7YWd2bciKfXOUBJ; alternate compressed copy 18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t).","role":"durable perioperative/head-and-neck foundation and nutrition principles; source identity is traceable, while direct whole-volume connector extraction is size-limited and current management is therefore independently verified against specialty-independent guidelines"},
    {"type":"textbook","citation":"Pasha R, Golub JS. Otolaryngology-Head and Neck Surgery: Clinical Reference Guide, 6th ed. (2022), connected Google Drive copy 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52, reviewed 2026-09-10.","role":"resident-level ENT perioperative framework and cross-check that general fluid/electrolyte prescriptions must be individualized rather than treated as a procedure-specific fixed recipe"},
    {"type":"textbook","citation":"K.J. Lee's Essential Otolaryngology: Head & Neck Surgery, 12th ed. (2019), connected Google Drive copy 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR, Chapter 8 'Nutrition, Fluid, and Electrolytes' (p.160 ff), reviewed 2026-09-10.","role":"durable physiology/board foundation: volume assessment, maintenance calculations, sodium disorders, potassium disorders and nutrition; chapter explicitly emphasizes volume-status classification in hyponatremia"},
    {"type":"guideline","citation":"Feld LG, et al. Clinical Practice Guideline: Maintenance Intravenous Fluids in Children. Pediatrics. 2018;142(6):e20183083. AAP guidance reviewed 2026-09-10.","role":"current pediatric boundary: most hospitalized postoperative children age 28 days-18 years who fall within guideline scope should receive isotonic maintenance fluid with appropriate dextrose/KCl to reduce hyponatremia risk"},
    {"type":"guideline","citation":"NICE CG174. Intravenous fluid therapy in adults in hospital. Current recommendations reviewed 2026-09-10.","role":"adult framework: distinguish resuscitation, routine maintenance, replacement, redistribution and reassessment; routine maintenance is not the same as resuscitation or nutrition"},
    {"type":"guideline","citation":"Muscaritoli M, et al. ESPEN practical guideline: Clinical Nutrition in cancer. Clin Nutr. 2021;40:2898-2913. Current ESPEN guideline listing reconfirmed 2026-09-10.","role":"head-and-neck cancer nutrition: screen and intervene early; preserve enteral use when feasible and do not wait for severe depletion before nutrition planning"},
    {"type":"consensus","citation":"da Silva JSV, et al. ASPEN Consensus Recommendations for Refeeding Syndrome. Nutr Clin Pract. 2020;35:178-195. PMID:32115791; erratum PMID:32383800.","role":"refeeding safety: phosphorus, potassium and magnesium decline within 5 days of calorie reintroduction defines severity tiers and should trigger prevention/monitoring in high-risk patients"},
]

PROMPT = """A postoperative ENT patient is NPO after a major head-and-neck procedure and has poor intake, rising nausea, oliguria and new electrolyte abnormalities. As the senior resident, explain how you separate resuscitation from routine maintenance and replacement; how you assess volume status rather than treating a laboratory value in isolation; how you approach postoperative hyponatremia, potassium/magnesium/phosphate abnormalities and refeeding risk; how adult and pediatric maintenance-fluid principles differ; and how you decide when oral, enteral or parenteral nutrition is appropriate. Include specific danger signs, correction traps, monitoring, escalation and stop/reassess decisions relevant to ENT patients."""

ANSWER = """Foundation — fluids, electrolytes and nutrition are three linked but different prescriptions. A crystalloid bolus treats suspected intravascular hypovolemia; maintenance fluid covers ongoing basal water/electrolyte needs when oral intake is inadequate; replacement addresses measured or estimated abnormal losses; nutrition supplies calories, protein and micronutrients. One bag should not be asked to do all four jobs. The senior resident first asks why the patient cannot maintain homeostasis and what physiologic problem is being treated, then writes a prescription with an endpoint and a reassessment time.

Start with the patient, not the sodium — assess airway and breathing first, then circulation, mental status, urine output, weight trend, mucous membranes, edema, orthostasis when appropriate, drain/NG/ostomy losses, bleeding, fever, medications and comorbid cardiac/renal/hepatic/endocrine disease. Review intake/output but do not assume the chart is complete. Tachycardia and oliguria can reflect hypovolemia, pain, sepsis, urinary retention, low cardiac output or renal injury. Edema does not prove adequate effective circulating volume. A fluid challenge is a diagnostic/therapeutic maneuver only when the patient is likely fluid responsive and the harm of additional volume is acceptable.

Resuscitation versus maintenance — shock or clinically important hypovolemia requires prompt isotonic crystalloid resuscitation with frequent reassessment of perfusion, blood pressure, mental status, lactate when relevant and urine output; do not slowly 'maintain' a patient in shock. Conversely, a stable NPO patient does not need repeated liters because urine output dipped for one hour. For adult routine maintenance, contemporary guidance uses roughly 25-30 mL/kg/day of water with about 1 mmol/kg/day each of sodium, potassium and chloride as an initial framework, then reduces volume for frailty, renal/cardiac dysfunction or other risk. This is a starting prescription, not a rule. Count IV medications, tube feeds and flushes toward total intake.

Pediatric maintenance — classic Holliday-Segar 4-2-1 hourly calculations remain useful for estimating maintenance volume, but old hypotonic-fluid dogma is not the current default for most hospitalized postoperative children. The AAP recommends isotonic maintenance solutions with appropriate dextrose and potassium for most patients 28 days to 18 years within guideline scope because this reduces hospital-acquired hyponatremia. The recommendation has exclusions and does not dictate the optimal rate for every child. Neurosurgical disease, renal/cardiac/hepatic disease, diabetes insipidus, major ongoing free-water losses and other excluded states require individualized physiology rather than automatic application.

Postoperative hyponatremia — classify severity, symptoms, tonicity and volume status before assigning a cause. Head-and-neck patients can have postoperative nonosmotic ADH from pain, nausea, stress and medications; they may also be truly hypovolemic from poor intake, bleeding or external losses. Obtain serum osmolality and, when the diagnosis is unclear, urine osmolality and urine sodium in clinical context. Severe neurologic symptoms such as seizure, marked confusion or declining consciousness make hyponatremia an emergency requiring monitored hypertonic-saline treatment according to institutional/current endocrine protocols. Do not wait for perfect etiologic classification before treating a patient with severe symptomatic cerebral edema risk.

The sodium bailout is to avoid both undertreatment and overcorrection. Rapid uncontrolled correction of chronic or high-risk hyponatremia can cause osmotic demyelination. Correction targets depend on acuity, symptoms and risk factors; use a current institutional/endocrine protocol and check sodium frequently during active correction rather than memorizing an aggressive one-size-fits-all number. If sodium is rising faster than intended, stop the driver of correction, escalate early and use a controlled relowering/antidiuresis strategy such as desmopressin plus free water when indicated by the treating team. A sudden water diuresis after restoring volume can accelerate sodium unexpectedly, so urine output is part of the safety monitor.

Do not call every postoperative low sodium 'SIADH.' SIADH is a diagnosis made in an appropriately evaluated euvolemic patient with hypotonic hyponatremia and inappropriately concentrated urine after considering adrenal, thyroid, renal and medication causes. Giving repeated normal-saline boluses to a truly euvolemic SIADH patient may fail to solve the problem and can add volume; fluid restriction or cause-specific therapy may be appropriate. Conversely, fluid-restricting a genuinely hypovolemic patient because the sodium is low can worsen perfusion. Volume status changes management.

Potassium — identify the mechanism and ECG/clinical risk. Hypokalemia may follow poor intake, GI losses, diuretics, alkalosis or intracellular shifts. Check magnesium because refractory hypokalemia often will not correct until magnesium is repleted. Significant symptoms, arrhythmia, ECG change or severe derangement require monitored replacement and attention to renal function. Never give an unmonitored rapid IV potassium push. Hyperkalemia with ECG changes is a stabilization emergency: membrane stabilization with IV calcium is conceptually separate from shifting potassium intracellularly and from removing potassium from the body. Verify unexpected results for hemolysis when the patient is clinically discordant, but do not delay treatment of convincing dangerous hyperkalemia.

Magnesium and phosphate — both matter after major oncologic surgery and prolonged poor intake. Hypomagnesemia promotes arrhythmia and makes potassium difficult to correct. Hypophosphatemia can impair diaphragmatic/respiratory muscle function, myocardial function and ATP-dependent cellular processes. In a tracheostomy, laryngectomy or tenuous-airway patient, profound phosphate depletion is not a trivial chemistry abnormality if respiratory strength is worsening. Replace based on severity, symptoms, renal function and route, with repeat testing after substantial replacement.

Refeeding syndrome — a malnourished head-and-neck cancer patient who has had minimal intake is a classic risk context. The danger comes when carbohydrate/calorie reintroduction drives insulin-mediated intracellular shifts of phosphate, potassium and magnesium and increases thiamine demand. ASPEN defines severity by falls in phosphorus, potassium and/or magnesium occurring within 5 days of calorie reintroduction, with organ dysfunction/thiamine deficiency marking severe disease. Screen before feeding: weight loss, duration of minimal intake, alcohol use, baseline electrolytes and other risk factors. In a high-risk patient, give thiamine as indicated, correct/closely monitor electrolytes and advance calories deliberately rather than reflexively starting full-goal feeds.

Nutrition route — use the gut when it is functional and safe. Oral intake is preferred when swallowing and aspiration risk allow; enteral tube feeding is preferred over parenteral nutrition when the GI tract works but oral intake cannot meet needs. A fresh free flap, mandibulotomy, pharyngeal repair or severe dysphagia may determine timing and route, but NPO status itself is not an indication for parenteral nutrition. Parenteral nutrition is reserved for situations where enteral nutrition is not feasible, is contraindicated or remains insufficient for a clinically meaningful period. Head-and-neck cancer nutrition should be planned early because dysphagia, odynophagia, tumor burden, surgery and chemoradiation can compound pre-existing malnutrition.

Replacement losses — measure what is measurable. High NG output, emesis, diarrhea, salivary fistula-related losses, fever and drains can alter water/electrolyte needs. Replace substantial ongoing losses separately from maintenance and reassess their composition and rate. Do not hide replacement inside an ever-increasing 'maintenance' rate, because that makes it impossible to know what problem is being treated. New polyuria should trigger evaluation for osmotic diuresis, post-obstructive diuresis or diabetes insipidus rather than automatic liter-for-liter hypotonic fluid without diagnostic reasoning.

ENT-specific perioperative traps — after thyroid/parathyroid surgery, paresthesias, tetany, QT prolongation or laryngospasm can represent hypocalcemia and require calcium/PTH-focused evaluation rather than generic fluid treatment. After skull-base surgery, polyuria with hypernatremia raises concern for diabetes insipidus, whereas hyponatremia can reflect SIADH or other mechanisms; trends and urine studies matter. In a patient with a neck hematoma, tachycardia and anxiety are not indications to 'try fluids first' while the airway is being compressed. Airway rescue and hemorrhage control supersede electrolyte elegance.

Monitoring and stop/reassess — every fluid/electrolyte prescription needs an endpoint. Trend vitals, examination, weight, urine output, renal function and the specific electrolyte being corrected. Stop escalating crystalloid when perfusion does not improve or pulmonary/peripheral edema is accumulating; reassess the diagnosis and escalate to critical care, medicine/nephrology/endocrinology or nutrition support as appropriate. Stop routine potassium supplementation when renal function deteriorates or hyperkalemia emerges. Slow or stop calorie advancement when refeeding abnormalities develop. A senior resident is defined less by calculating 4-2-1 quickly than by recognizing when the formula no longer fits the physiology.

Senior synthesis — make seven explicit decisions: RESUSCITATION: is there shock/hypovolemia needing immediate isotonic volume? MAINTENANCE: what basal volume/composition is appropriate for this adult or child? REPLACEMENT: what abnormal losses are occurring and should be replaced separately? ELECTROLYTES: which abnormalities are symptomatic or immediately dangerous? SODIUM SAFETY: what is the likely chronicity/volume state and how will overcorrection be prevented? NUTRITION: can the patient eat, can the gut be used, and is refeeding risk present? REASSESSMENT: what objective endpoint will make you continue, change or stop the plan? The dangerous answer is not a wrong memorized maintenance rate; it is continuing a formula after the patient's physiology has declared that it is wrong."""

TRAPS = [
    "Using a maintenance-fluid formula to treat shock instead of giving monitored resuscitation with explicit perfusion endpoints.",
    "Giving repeated boluses for isolated oliguria without considering pain, retention, renal injury, low cardiac output or inaccurate intake/output documentation.",
    "Treating edema as proof of adequate effective circulating volume or, conversely, treating every edematous patient with more crystalloid.",
    "Using old hypotonic postoperative pediatric maintenance fluid by habit despite the AAP isotonic-fluid recommendation for most children within guideline scope.",
    "Applying the pediatric isotonic-fluid recommendation to an excluded renal, cardiac, hepatic, neurosurgical or diabetes-insipidus physiology without individualization.",
    "Calling every postoperative hyponatremia SIADH without establishing hypotonicity, volume status and the relevant urine/endocrine context.",
    "Fluid-restricting a truly hypovolemic hyponatremic patient because the sodium is low, thereby worsening perfusion.",
    "Correcting chronic/high-risk hyponatremia too quickly and failing to watch for sudden water diuresis and osmotic-demyelelination risk.",
    "Continuing a sodium correction that is overshooting rather than stopping, escalating and using a controlled prevention/relowering strategy when indicated.",
    "Replacing refractory potassium repeatedly without checking and correcting magnesium.",
    "Treating dangerous hyperkalemia as a single-step problem and forgetting that cardiac membrane stabilization, intracellular shift and potassium removal are different goals.",
    "Ignoring severe hypophosphatemia in a tenuous-airway patient despite the potential for impaired respiratory-muscle function.",
    "Starting full-goal calories immediately in a severely malnourished head-and-neck cancer patient without refeeding screening, thiamine/electrolyte planning and close monitoring.",
    "Equating NPO status with an indication for parenteral nutrition even when the GI tract is functional and enteral feeding is feasible.",
    "Hiding ongoing NG/drain/GI losses inside an ever-higher maintenance rate instead of prescribing and reassessing replacement separately.",
    "Trying to correct tachycardia with fluids while a postoperative neck hematoma is threatening the airway and requires immediate rescue/source control.",
]

COHORT = {QIDS[0]: {
    "concept_id": CID,
    "canonical_topic": TOPIC,
    "prompt": PROMPT,
    "answer_text": ANSWER,
    "explanation": "Separate resuscitation, maintenance, replacement and nutrition; assess volume status and physiology before treating numbers; use current pediatric isotonic-maintenance guidance, protect against sodium overcorrection and refeeding, and choose enteral nutrition whenever a functional gut can be used safely.",
    "board_pearl": "Postoperative hyponatremia is not synonymous with SIADH. Establish symptoms, tonicity and volume status; treat severe symptomatic hyponatremia urgently while preventing overcorrection, and remember that restoration of volume can trigger a sudden water diuresis.",
    "depth_layers_v223": {
        "foundation":"Fluid compartments, resuscitation versus maintenance versus replacement, volume assessment, sodium/potassium/magnesium/phosphate physiology and oral/enteral/parenteral nutrition hierarchy.",
        "application":"Adult and pediatric maintenance prescriptions, postoperative hyponatremia workup, safe electrolyte correction, quantified loss replacement, head-and-neck cancer nutrition and refeeding prevention.",
        "senior_decision":"Recognize shock, symptomatic sodium emergencies, dangerous potassium derangements, refeeding physiology, airway/hemorrhage problems masquerading as fluid issues, and know when to stop formula-based treatment and escalate."
    },
    "common_traps_v223": TRAPS,
    "deliberate_review_v223": {"priority":"high","review_after_days":[2,7,21,60],"reason":"high-frequency inpatient/OR management with low-frequency but catastrophic sodium, potassium, refeeding and airway-adjacent failure modes"},
    "source_refs_v223": SOURCE_REFS_V223,
    "evidence_distinction_v223":"Durable textbook physiology (volume status, compartment reasoning, classic maintenance calculations and enteral-first principles) is retained. Current guidance supersedes older reflexive hypotonic pediatric maintenance practice: AAP recommends isotonic maintenance fluid for most postoperative children within scope. Adult NICE quantities are initial routine-maintenance frameworks, not resuscitation targets. ASPEN refeeding criteria and ESPEN cancer-nutrition guidance update monitoring/feeding decisions. Cummings source identity is traceable in the connected Drive corpus, but whole-volume extraction is connector-size-limited; no unsupported Cummings-specific numeric prescription is asserted.",
    "task_alignment_v223": True,
}}

def apply_concept_check_task_alignment_v223(checks, deep_modules, v6_item_id):
    by = {str(q.get("id") or ""): q for q in checks or []}
    repaired=[]; missing=[]; link_mismatch=[]
    for qid, patch in COHORT.items():
        q=by.get(qid)
        if q is None: missing.append(qid); continue
        module=_find_module(q, deep_modules, v6_item_id)
        topic=str(module.get("topic") or "") if module else ""
        cid=v6_item_id(q.get("domain"), topic) if module and q.get("domain") else None
        if topic != patch["canonical_topic"] or cid != patch["concept_id"]:
            link_mismatch.append(qid); continue
        for key,val in patch.items():
            if key not in ("canonical_topic",): q[key]=val
        q["choices"]=[]; q["answer"]=None
        repaired.append(qid)
    return {"repaired":repaired,"missing":missing,"link_mismatch":link_mismatch}
