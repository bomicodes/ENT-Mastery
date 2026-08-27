"""v23.8 — Thyroid / Parathyroid / Salivary pass 6.

Repairs one v23.7 rationale caught by the runtime quality gate, then reviews
canonical topics 26-30: RLN injury during thyroidectomy, completion
thyroidectomy, RAI/TSH suppression in DTC, radioiodine-refractory DTC, and
primary thyroid lymphoma.
"""
DOMAIN="Thyroid / Parathyroid / Salivary"

def _q(qid,topic,stage,stem,choices,answer,explanation,reasons,pearl,curveball,focus="boards"):
    return {"id":qid,"domain":DOMAIN,"topic":topic,"learning_stage":stage,"stem":stem,
            "choices":choices,"answer":answer,"explanation":explanation,"why_wrong":reasons,
            "board_pearl":pearl,"curveball":curveball,"tier":"Curated learning ladder",
            "mode":"Vignette","focus":focus,"ladder_reviewed":True}

VIGNETTES_V238=[
_q("v238_tps_rln_fnd","Recurrent Laryngeal Nerve Injury During Thyroidectomy","foundation",
"After thyroidectomy, a patient has new breathy dysphonia. Flexible laryngoscopy shows one immobile true vocal fold. What is the key first distinction?",
["Unilateral vocal-fold immobility from RLN dysfunction versus a mechanical fixation or arytenoid problem","Whether the thyroid specimen was benign","Whether calcium is normal","Whether the incision is painful"],0,
"Post-thyroidectomy dysphonia requires laryngeal examination. True unilateral immobility suggests RLN dysfunction, but cricoarytenoid fixation, arytenoid dislocation, edema, or other laryngeal causes must remain in the differential.",
["Correct. Localization of the immobility mechanism guides prognosis and rehabilitation.","Pathology does not localize the new voice deficit.","Calcium status matters after thyroid surgery but does not explain isolated vocal-fold immobility.","Incisional pain does not establish the mechanism of dysphonia."],
"After thyroid surgery, new voice change deserves a laryngeal exam—not an assumption.","How does immediate versus delayed onset affect the suspected mechanism?"),
_q("v238_tps_rln_app","Recurrent Laryngeal Nerve Injury During Thyroidectomy","application",
"During total thyroidectomy, a verified loss of nerve-monitoring signal occurs on the first side before the opposite lobe is removed. What is the safest general principle?",
["Always complete the second side immediately","Troubleshoot and confirm true loss of signal, then strongly consider staging the contralateral operation to avoid bilateral vocal-fold paralysis","Ignore monitoring completely","Perform prophylactic tracheostomy before evaluating the event"],1,
"A true first-side loss of signal changes the risk of proceeding contralaterally. After checking the endotracheal electrodes, vagal/RLN stimulation, equipment, and operative field, staging can avoid converting a unilateral injury into a bilateral airway catastrophe.",
["Automatic completion can create bilateral immobility.","Correct. Verified first-side signal loss is one of the situations in which monitoring can appropriately change the operative plan.","Monitoring does not replace visualization, but a verified event is clinically meaningful.","Tracheostomy is not automatic before the loss is confirmed and the airway assessed."],
"The first-side signal matters because the second nerve is now the patient's airway reserve.","What technical checks distinguish equipment failure from a true neural event?","OR_prep"),
_q("v238_tps_rln_snr","Recurrent Laryngeal Nerve Injury During Thyroidectomy","senior_decision",
"A patient has persistent unilateral vocal-fold paralysis months after thyroidectomy with poor voice and aspiration but an adequate airway. What should drive definitive rehabilitation?",
["Observation forever regardless of function","Expected neural recovery, laryngeal EMG/clinical trajectory when useful, glottic insufficiency, aspiration burden, voice goals, and patient preference when selecting temporary injection versus durable medialization/reinnervation","Immediate bilateral cordotomy","Total laryngectomy"],1,
"Management is function- and prognosis-driven. Early temporary injection can improve voice and swallowing while recovery remains possible; persistent deficits can be treated with framework surgery or reinnervation in appropriately selected patients.",
["Persistent symptomatic glottic insufficiency can merit rehabilitation.","Correct. Timing and procedure choice should match recovery potential and the functional deficit.","Cordotomy enlarges the airway and is not the treatment for unilateral glottic insufficiency with aspiration.","Total laryngectomy is grossly disproportionate to isolated unilateral RLN paralysis."],
"Treat the patient's glottic function, not merely the laryngoscopy image.","When would immediate intraoperative nerve repair or reinnervation be considered?"),

_q("v238_tps_completion_fnd","Completion Thyroidectomy","foundation",
"What is a completion thyroidectomy?",
["Removal of the remaining thyroid lobe after a prior lobectomy when subsequent risk assessment creates a reason for total-thyroid management","Routine central neck dissection","Parathyroid exploration","Revision tracheostomy"],0,
"Completion thyroidectomy removes residual thyroid after prior unilateral surgery. The indication depends on final pathology, residual disease, need for radioactive iodine or surveillance strategy, contralateral disease, and patient-specific risk rather than the word cancer alone.",
["Correct. It is a second-stage removal of residual thyroid tissue when the oncologic plan warrants it.","Central neck dissection addresses lymph nodes, not the remaining thyroid lobe.","Parathyroid exploration is a different endocrine operation.","Tracheostomy has no definitional relationship to completion thyroidectomy."],
"Completion thyroidectomy is a risk-adapted second operation, not an automatic consequence of every cancer diagnosis.","Which postoperative pathology findings most often reopen the extent-of-thyroidectomy decision?"),
_q("v238_tps_completion_app","Completion Thyroidectomy","application",
"A patient underwent lobectomy for a small apparently low-risk papillary thyroid carcinoma. Final pathology confirms completely excised low-risk intrathyroidal disease with no adverse features or contralateral lesion. What is the best principle?",
["Completion thyroidectomy is mandatory for every papillary carcinoma","Lobectomy may remain definitive; completion surgery should be reserved for features that create a meaningful benefit from total-thyroid management","Give empiric chemotherapy","Perform bilateral neck dissection"],1,
"Modern differentiated-thyroid management is risk-adapted. Selected low-risk cancers can be definitively managed with lobectomy, so completion thyroidectomy is not obligatory when final pathology remains favorable.",
["Automatic completion overtreats many low-risk patients.","Correct. Extent should follow recurrence risk, adjuvant needs, contralateral disease, surveillance implications, and patient preference.","Cytotoxic chemotherapy is not routine adjuvant therapy for low-risk DTC.","There is no indication for radical bilateral nodal surgery in this scenario."],
"Final pathology can confirm that the original lobectomy was enough.","How would gross extrathyroidal extension or significant nodal disease change the discussion?"),
_q("v238_tps_completion_snr","Completion Thyroidectomy","senior_decision",
"A patient needs completion thyroidectomy after a difficult prior lobectomy and has ipsilateral vocal-fold paralysis. What should dominate planning?",
["Proceed as if this were a virgin neck","Document contralateral vocal-fold function, review prior operative/pathology details, define why completion is necessary, and explicitly plan around the catastrophic consequence of injuring the only functioning RLN","Ignore preoperative laryngoscopy","Remove the remaining lobe without discussing alternatives"],1,
"Reoperative thyroid surgery has altered planes and higher nerve risk. Preoperative laryngeal function is essential when one nerve may already be compromised, and the strength of the completion indication must justify risking the contralateral nerve.",
["Reoperative anatomy is not equivalent to primary surgery.","Correct. The remaining RLN may be the patient's only mobile vocal fold and must shape the risk-benefit decision.","Skipping laryngoscopy can miss a pre-existing paralysis and obscure the true airway risk.","Alternative surveillance/adjuvant strategies may matter when surgical risk is unusually high."],
"Before a second-side thyroid operation, know whether the first nerve still works.","When might a multidisciplinary nonoperative strategy be favored despite a theoretical completion indication?","OR_prep"),

_q("v238_tps_rai_fnd","Radioactive Iodine / TSH Suppression in Differentiated Thyroid Cancer","foundation",
"What is the basic purpose of radioactive iodine in differentiated thyroid cancer?",
["To exploit iodine uptake by differentiated thyroid tissue for selected remnant ablation or treatment of iodine-avid disease","To treat medullary thyroid cancer","To replace thyroid hormone","To ablate parathyroid glands"],0,
"RAI uses the iodine-handling biology of differentiated follicular-cell-derived thyroid cancer. It is selectively used according to recurrence risk, residual disease, metastatic burden, iodine avidity, and treatment goals rather than routinely for every patient.",
["Correct. RAI is a selective adjuvant/therapeutic tool for iodine-avid differentiated thyroid tissue.","Medullary carcinoma arises from C cells and is not treated with RAI.","Levothyroxine replaces thyroid hormone; RAI does not.","RAI is not a parathyroid treatment."],
"RAI follows biology and recurrence risk—not simply the presence of a thyroid-cancer label.","Why is preparation with elevated TSH useful before some RAI treatments?"),
_q("v238_tps_rai_app","Radioactive Iodine / TSH Suppression in Differentiated Thyroid Cancer","application",
"A disease-free low-risk DTC survivor has an excellent response to therapy. What is the best long-term TSH principle?",
["Suppress TSH to undetectable levels forever in every patient","Individualize the TSH target to recurrence risk and response, avoiding unnecessary aggressive suppression when oncologic benefit is small and cardiac/bone risks matter","Stop levothyroxine entirely","Use TSH alone to diagnose recurrence"],1,
"TSH suppression is dynamic risk management. Stronger suppression may be useful in selected higher-risk or persistent disease, whereas excellent-response low-risk patients generally do not need indefinite profound suppression that increases atrial and skeletal toxicity.",
["Universal intense suppression exposes low-risk patients to avoidable harm.","Correct. The target should evolve with oncologic risk, response, age, bone health, and cardiovascular risk.","Most patients after total thyroidectomy require thyroid-hormone replacement.","Recurrence assessment integrates thyroglobulin, antibodies, imaging, and clinical context."],
"TSH suppression has a therapeutic dose-response and a toxicity dose-response; balance both.","How would atrial fibrillation or osteoporosis alter the target?"),
_q("v238_tps_rai_snr","Radioactive Iodine / TSH Suppression in Differentiated Thyroid Cancer","senior_decision",
"A patient with metastatic DTC has lesions that are iodine-avid but has already received substantial prior RAI. What should determine whether additional RAI is worthwhile?",
["Repeat RAI indefinitely while any uptake exists","Evidence of meaningful prior response, disease burden and tempo, dosimetry/toxicity, competing local/systemic options, and whether additional treatment is likely to produce clinical benefit","Serum TSH alone","Patient age alone"],1,
"Iodine uptake does not guarantee useful tumor response. Repeated treatment should have a plausible therapeutic benefit and account for cumulative marrow, salivary, pulmonary, and secondary-malignancy risks.",
["Uptake alone is not enough to justify unlimited retreatment.","Correct. Senior treatment decisions integrate biologic response and cumulative toxicity.","TSH is part of preparation, not a standalone treatment-selection metric.","Age informs risk but cannot replace assessment of disease biology and prior response."],
"RAI should earn each repeat dose by showing a realistic chance of benefit.","What findings suggest the disease is becoming radioiodine refractory?"),

_q("v238_tps_rrdtc_fnd","Radioiodine-Refractory Differentiated Thyroid Cancer","foundation",
"Which pattern most strongly suggests radioiodine-refractory differentiated thyroid cancer?",
["Progressive metastatic disease that does not meaningfully take up iodine or continues to progress despite appropriately delivered RAI","A tiny stable thyroid remnant after lobectomy","Normal calcium","Transient postoperative hoarseness"],0,
"RAI-refractory disease includes tumors that lose iodine avidity, have discordant non-avid progressive lesions, or progress despite appropriate RAI such that further treatment is unlikely to help.",
["Correct. The defining issue is loss of clinically useful iodine responsiveness.","A stable remnant does not establish refractory metastatic cancer.","Calcium status does not determine iodine sensitivity.","Hoarseness is unrelated to tumor iodine avidity."],
"Refractory means RAI is no longer a useful anticancer tool—not merely that cancer persists.","How can FDG avidity and lesion-to-lesion heterogeneity support this assessment?"),
_q("v238_tps_rrdtc_app","Radioiodine-Refractory Differentiated Thyroid Cancer","application",
"A patient has slowly progressive, asymptomatic, low-volume RAI-refractory pulmonary metastases. What is the best treatment principle?",
["Start systemic kinase therapy immediately for every measurable lesion","Consider active surveillance until disease tempo, symptoms, threat to critical structures, or tumor burden justify systemic treatment; use local therapy selectively for focal threats","Continue ineffective RAI indefinitely","Perform total laryngectomy"],1,
"Systemic therapy has meaningful toxicity. In indolent asymptomatic RAI-refractory disease, observation can be appropriate until progression becomes clinically meaningful; local ablative treatment can control selected threatening sites.",
["Immediate systemic therapy can expose an indolent patient to years of toxicity without clear near-term benefit.","Correct. Treatment timing should be driven by clinically meaningful progression and threat.","Persisting with ineffective RAI adds toxicity without benefit.","Laryngectomy does not treat pulmonary metastatic disease."],
"RAI-refractory does not automatically mean 'start a TKI today.'",
"Which disease sites make delay unsafe even when total tumor volume is modest?"),
_q("v238_tps_rrdtc_snr","Radioiodine-Refractory Differentiated Thyroid Cancer","senior_decision",
"A patient with progressive RAI-refractory DTC is being considered for systemic therapy. What modern principle should guide selection?",
["Use the same drug sequence regardless of tumor biology","Obtain actionable molecular information when appropriate and integrate targetable alterations, prior therapy, disease tempo, toxicity profile, comorbidity, and patient goals into treatment selection","Choose treatment solely by primary tumor size","Give more RAI first even after clear refractoriness"],1,
"Multikinase inhibitors remain important, but molecularly targeted therapies can produce major responses in selected tumors with actionable alterations. Therapy should be individualized rather than reflexively sequenced.",
["Tumor biology can materially change the best systemic option.","Correct. Molecular selection and patient-level toxicity considerations belong in the same decision.","Primary size does not capture metastatic treatment biology.","Additional ineffective RAI delays more appropriate therapy and adds toxicity."],
"In advanced thyroid cancer, sequence treatment by biology, threat, and toxicity—not habit.","When can neoadjuvant targeted therapy change surgical resectability in locally advanced disease?"),

_q("v238_tps_lymph_fnd","Primary Thyroid Lymphoma","foundation",
"An older patient with Hashimoto thyroiditis develops rapidly enlarging painless thyroid swelling with compressive symptoms over weeks. What diagnosis should be high on the differential?",
["Primary thyroid lymphoma","Benign colloid nodule","First-bite syndrome","Ranula"],0,
"Primary thyroid lymphoma often presents as a rapidly enlarging thyroid mass, frequently in a background of autoimmune thyroiditis. Compressive symptoms may develop quickly despite a relatively short history.",
["Correct. Rapid enlargement plus Hashimoto background is a classic warning pattern.","A benign colloid nodule usually does not enlarge this rapidly with new compression.","First-bite syndrome is parotid-region pain with meals.","A ranula is a sublingual mucus collection."],
"Rapid thyroid enlargement is a tissue-diagnosis problem until proven otherwise.","Which competing diagnosis is especially urgent when the mass is painful, fixed, and rapidly progressive?"),
_q("v238_tps_lymph_app","Primary Thyroid Lymphoma","application",
"A patient has suspected primary thyroid lymphoma with airway-stable compressive symptoms. What is the best diagnostic principle?",
["Obtain adequate tissue for lymphoma classification—often core biopsy with flow/immunophenotyping or surgical biopsy when needed—rather than defaulting to total thyroidectomy","Perform total thyroidectomy before tissue diagnosis in every case","Treat empirically with radioactive iodine","Observe for a year"],0,
"Lymphoma treatment is primarily systemic and/or radiation-based, so accurate histologic classification is the goal. FNA may suggest lymphoma but may be insufficient for full architecture and phenotyping.",
["Correct. The operation should obtain the diagnosis, not automatically remove the gland.","Routine total thyroidectomy adds morbidity without being the primary treatment for most thyroid lymphomas.","Lymphoma is not treated with RAI.","Rapid progressive compression requires timely diagnosis."],
"When lymphoma is suspected, the biopsy is the operation unless airway rescue demands more.","When does open biopsy become preferable to repeated nondiagnostic needle sampling?"),
_q("v238_tps_lymph_snr","Primary Thyroid Lymphoma","senior_decision",
"A patient with suspected thyroid lymphoma has severe orthopnea and a critically narrowed trachea. What should dominate the diagnostic plan?",
["Routine induction of general anesthesia for thyroidectomy","Coordinate the safest airway-preserving tissue strategy with anesthesia, oncology, pathology, and interventional teams; avoid a diagnostic maneuver that precipitates loss of the airway","Wait months for spontaneous improvement","Give RAI before biopsy"],1,
"A rapidly enlarging thyroid/neck mass can produce a precarious airway. Tissue is necessary, but the biopsy strategy must be subordinate to airway physiology; awake/local approaches or alternative accessible tissue may be safer than routine induction in selected patients.",
["Induction can destabilize a critically narrowed airway.","Correct. Diagnostic adequacy and airway safety must be planned together.","Delay risks sudden airway compromise and delays disease-specific treatment.","RAI is not appropriate therapy for lymphoma and does not replace diagnosis."],
"The safest biopsy is the one that gets enough tissue without losing the airway.","What symptoms or imaging findings should make routine supine induction particularly hazardous?","overnight_call")]

def apply_learning_ladders_v238(challenges,item_id_fn):
    # Repair the single v23.7 quality defect before runtime audits inspect the bank.
    for q in challenges:
        if q.get("id")=="v237_tps_ranula_snr":
            reasons=list(q.get("why_wrong") or [])
            if len(reasons)>=4:
                reasons[2]="Removing the thyroid does not address the sublingual-gland mucus leak that produces a plunging ranula and would add major unrelated endocrine and nerve morbidity."
                q["why_wrong"]=reasons
            break
    existing={q.get("id") for q in challenges if q.get("id")}; added=0
    for q in VIGNETTES_V238:
        if q["id"] in existing: continue
        row=dict(q); row["concept_id"]=item_id_fn(DOMAIN,row["topic"])
        if not row["concept_id"]: raise RuntimeError("v238 orphan: "+row["topic"])
        challenges.append(row); existing.add(row["id"]); added+=1
    return {"added":added,"reviewed_topics":5,"repaired":"v237_tps_ranula_snr"}
