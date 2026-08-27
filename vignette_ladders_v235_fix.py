"""v23.5 follow-up: close the application layer for indeterminate thyroid cytology.

The legacy v143 case remains valuable but its authored choice wording differs from
the reuse map in v235. Rather than silently marking a generic-rationale row as
reviewed, add one clean application case with individualized rationales.
"""
DOMAIN="Thyroid / Parathyroid / Salivary"
TOPIC="Indeterminate Thyroid Cytology / Molecular Testing"

def apply_learning_ladders_v235_fix(challenges,item_id_fn):
    qid="v235_tps_indet_app"
    if any(str(q.get("id"))==qid for q in challenges): return {"added":0}
    row={
      "id":qid,"domain":DOMAIN,"topic":TOPIC,"learning_stage":"application",
      "stem":"A 2.2 cm Bethesda III thyroid nodule remains indeterminate on repeat FNA. Ultrasound is not highly suspicious and the patient strongly prefers to avoid unnecessary surgery. What is the best role for molecular testing?",
      "choices":["Use a validated molecular assay as an adjunct to refine malignancy probability and help choose surveillance versus diagnostic surgery in the context of ultrasound, pretest risk, and patient preference","Treat any molecular result as a perfect stand-alone cancer diagnosis","Ignore ultrasound and clinical context once a molecular result returns","Give radioactive iodine before establishing a diagnosis"],
      "answer":0,
      "explanation":"Molecular testing is most useful when its result can change management of an indeterminate nodule. Assay performance and positive/negative predictive values depend on the platform and pretest prevalence, so the result should update—not replace—the clinical, cytologic, and sonographic risk assessment.",
      "why_wrong":["Correct. Molecular testing is a probability-refining decision aid for selected indeterminate nodules.","No molecular classifier is perfectly diagnostic in every population or nodule.","Ultrasound phenotype and clinical risk remain important after molecular testing.","Radioactive iodine is not a diagnostic treatment for an unresolved thyroid nodule."],
      "board_pearl":"A molecular thyroid test changes probability; it does not replace clinical reasoning.",
      "curveball":"How would a strongly suspicious ultrasound phenotype change your confidence in a reassuring molecular result?",
      "tier":"Curated learning ladder","mode":"Vignette","focus":"boards","ladder_reviewed":True,
      "concept_id":item_id_fn(DOMAIN,TOPIC),
    }
    if not row["concept_id"]: raise RuntimeError("v235 fix orphan: "+TOPIC)
    challenges.append(row); return {"added":1}
