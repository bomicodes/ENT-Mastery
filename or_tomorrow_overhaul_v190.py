"""v19.0 OR Tomorrow operative-depth layer.

Adds a consistent resident night-before structure to every live OR_PREP_REGISTRY
entry without discarding procedure-specific core steps already curated upstream.
Content is paraphrased/synthesized from standard operative references; no textbook
question or prose is reproduced.
"""

BOOKS = {
    "operative": "Operative Otolaryngology—Head and Neck Surgery, 3rd ed.",
    "hn_atlas": "Atlas of Head & Neck Surgery (Cohen/Clayman)",
    "sinus_atlas": "Atlas of Endoscopic Sinus and Skull Base Surgery, 2nd ed.",
    "cummings": "Cummings Otolaryngology—Head and Neck Surgery, 7th ed.",
    "laryngology": "Operative Techniques in Laryngology, 2nd ed. (2024)",
}

# Each profile supplies procedure-family setup, exit checks, postoperative priorities,
# and complications. Existing procedure-specific steps remain the central sequence.
PROFILES = {
"otology": {
 "setup":["Confirm ear/laterality, hearing status, imaging and operative goal; review facial-nerve course and prior surgery.","Position for stable microscope/endoscope access; prep a field that permits graft harvest or postauricular extension if needed."],
 "landmarks":["facial nerve","chorda tympani","ossicular chain","tegmen and sigmoid sinus","round/oval windows"],
 "exit":["Inspect for hemostasis, facial-nerve/ossicular integrity and unintended labyrinthine or dural violation.","Confirm graft/prosthesis/implant position and secure canal packing or closure without excessive pressure."],
 "postop":["Document immediate facial-nerve function, vertigo/nystagmus, hearing symptoms and wound/packing status.","Give procedure-specific dry-ear/wound/activity precautions; escalate severe vertigo, new facial weakness, CSF-like drainage or sudden hearing change."],
 "early":["Facial weakness/paralysis — examine immediately; distinguish anesthetic effect from nerve injury and escalate urgently if unexpected.","Severe vertigo or sensorineural hearing decline — assess for inner-ear injury/perilymphatic problem and obtain urgent otologic evaluation.","Hematoma, wound infection, otorrhea or CSF leak — inspect wound/canal and manage according to source and severity."],
 "late":["Persistent perforation or graft failure, recurrent/retraction disease, canal stenosis or chronic otorrhea.","Conductive deficit from ossicular/prosthesis problem; taste disturbance from chorda injury; device extrusion/infection when applicable."],
 "sources":[BOOKS["operative"],BOOKS["cummings"]]},
"sinus": {
 "setup":["Review CT in three planes and identify skull base, orbit, carotid/optic risk, frontal recess and anatomic variants before incision.","Topical decongestion/local vasoconstriction, image guidance when indicated, and a plan that preserves mucosa and landmarks."],
 "landmarks":["orbit/lamina papyracea","skull base/cribriform","anterior ethmoid artery","optic nerve","internal carotid artery"],
 "exit":["Perform a deliberate orbit/skull-base/hemostasis check; confirm intended sinus/skull-base exposure and patency.","Preserve or replace mucosa where possible and secure graft/flap/packing only as required by the reconstruction."],
 "postop":["Monitor vision, extraocular movement, bleeding, mental status and clear rhinorrhea; vision change or orbital pain is an emergency.","Use procedure-specific saline care/debridement and activity restrictions; skull-base repairs require CSF-leak precautions and multidisciplinary follow-up."],
 "early":["Orbital hematoma/vision compromise — immediate eye exam and urgent decompression pathway; do not delay for routine imaging if vision is threatened.","CSF leak or intracranial complication — recognize clear rhinorrhea, severe headache, meningismus or neurologic change and escalate urgently.","Significant epistaxis, orbital emphysema/injury, postoperative infection or toxic shock (rare)."],
 "late":["Synechiae, ostial stenosis, recurrent inflammatory disease or mucocele.","Persistent CSF leak, graft/flap failure, crusting or delayed stenosis depending on approach."],
 "sources":[BOOKS["sinus_atlas"],BOOKS["operative"],BOOKS["cummings"]]},
"headneck": {
 "setup":["Review pathology, imaging, stage/extent, reconstructive plan, consented functional deficits and airway strategy.","Position to expose primary and neck as needed; mark incisions and preserve options for regional/free-flap reconstruction."],
 "landmarks":["carotid sheath","cranial nerves","thoracic duct on the left","marginal mandibular/facial nerve when relevant","airway and major vascular pedicles"],
 "exit":["Inspect oncologic bed and margins/specimen orientation, then perform meticulous hemostasis before reconstruction/closure.","Verify preserved nerves/vessels where applicable, drain placement, airway plan and viability/perfusion of reconstruction."],
 "postop":["Airway, bleeding and flap/neck checks are the first priorities; document cranial-nerve function and drain character/output.","Advance nutrition, speech/swallow rehabilitation, calcium/chyle monitoring or tracheostomy care according to the operation."],
 "early":["Neck hematoma or airway compromise — immediate bedside assessment and decompression/return to OR when indicated.","Chyle leak, salivary leak/fistula, cranial-nerve deficit, wound infection or flap vascular compromise.","Aspiration, pneumonia, electrolyte/nutrition problems or major-vessel complication in high-risk resections."],
 "late":["Fistula/stenosis, dysphagia/aspiration, shoulder dysfunction, lymphedema, chronic cranial-nerve deficit or reconstructive donor-site morbidity.","Oncologic recurrence and treatment-related functional impairment require surveillance and rehabilitation."],
 "sources":[BOOKS["hn_atlas"],BOOKS["operative"],BOOKS["cummings"]]},
"thyroid": {
 "setup":["Confirm indication, imaging/cytology, vocal-fold status when indicated, calcium/PTH context and extent of planned surgery.","Supine with controlled neck extension; plan nerve monitoring if used and ensure exposure allows safe capsular dissection."],
 "landmarks":["recurrent laryngeal nerve","external branch superior laryngeal nerve","parathyroid glands and blood supply","Berry ligament","tracheoesophageal groove"],
 "exit":["Confirm hemostasis with the neck in a physiologic/Valsalva state; reassess RLN integrity/monitoring signal when used.","Preserve viable parathyroid tissue or autotransplant clearly devascularized tissue when appropriate; document specimens and drain decision."],
 "postop":["Watch closely for neck swelling, respiratory distress or stridor; an expanding post-thyroidectomy hematoma is an airway emergency.","Assess voice and calcium symptoms; trend calcium/PTH according to institutional pathway and operation extent."],
 "early":["Expanding neck hematoma/airway compromise — immediate decompression and definitive control.","Hypocalcemia/hypoparathyroidism — recognize perioral/acral paresthesia, cramps or tetany and treat based on severity.","RLN dysfunction, bilateral vocal-fold immobility, EBSLN dysfunction, seroma or wound infection."],
 "late":["Persistent hypoparathyroidism or vocal-fold dysfunction; scar/adhesion symptoms and disease recurrence where applicable."],
 "sources":[BOOKS["hn_atlas"],BOOKS["operative"],BOOKS["cummings"]]},
"parathyroid": {
 "setup":["Confirm biochemical diagnosis before localization; review ultrasound/nuclear/4D imaging, prior neck surgery and baseline calcium/PTH.","Plan focused versus bilateral exploration and intraoperative PTH strategy; position as for central neck surgery."],
 "landmarks":["RLN","inferior thyroid artery","thyrothymic tract","tracheoesophageal groove","parathyroid vascular pedicle"],
 "exit":["Confirm removal of the intended abnormal tissue and interpret intraoperative PTH in clinical context when used.","Inspect remaining glands/nerve and obtain meticulous hemostasis before closure."],
 "postop":["Monitor for neck hematoma and symptomatic hypocalcemia; give calcium/vitamin D strategy according to disease burden and local pathway.","High bone-turnover patients need awareness of hungry-bone physiology and potentially prolonged supplementation."],
 "early":["Neck hematoma/airway compromise.","Hypocalcemia, hungry-bone syndrome, RLN dysfunction or persistent hyperparathyroidism from missed/multigland disease."],
 "late":["Recurrent/persistent hyperparathyroidism, permanent hypoparathyroidism after extensive exploration, or chronic nerve dysfunction."],
 "sources":[BOOKS["hn_atlas"],BOOKS["operative"],BOOKS["cummings"]]},
"salivary": {
 "setup":["Review imaging/FNA when appropriate and determine superficial/deep-lobe, nerve, duct and skull-base relationships.","Plan incision and nerve monitoring when relevant; counsel for facial/lingual/hypoglossal deficits and salivary complications."],
 "landmarks":["facial nerve and branches","retromandibular vein/external carotid","lingual nerve","hypoglossal nerve","Wharton/Stensen duct"],
 "exit":["Confirm nerve integrity and hemostasis; manage duct/oral communication as needed and place drain selectively.","Close without compressing preserved nerve or vascular structures."],
 "postop":["Document facial, tongue and lower-cranial nerve function appropriate to the gland; monitor drain and salivary swelling.","Watch for hematoma, infection and meal-related salivary leak; initiate wound care and shoulder/nerve rehabilitation as needed."],
 "early":["Hematoma, infection, facial weakness after parotid surgery, lingual/hypoglossal injury after submandibular surgery.","Sialocele or salivary fistula; duct edema/stenosis after endoscopic work."],
 "late":["Frey syndrome, gustatory sweating, contour deformity, persistent facial weakness, recurrent obstruction/stone or scar-related stenosis."],
 "sources":[BOOKS["hn_atlas"],BOOKS["operative"],BOOKS["cummings"]]},
"laryngology": {
 "setup":["Review laryngoscopy/stroboscopy/swallow findings and define the exact functional target before surgery.","Coordinate airway/anesthesia and exposure strategy; protect dentition and document baseline voice/airway/swallow function."],
 "landmarks":["vocal fold layered microstructure","anterior commissure","cricoarytenoid joint","recurrent laryngeal nerve","posterior glottis/subglottis"],
 "exit":["Reinspect the airway and treated tissue under magnification; confirm hemostasis while minimizing unnecessary mucosal trauma.","Document the airway/extubation plan and any voice rest, reflux, antibiotic, steroid or swallow instructions specific to the procedure."],
 "postop":["Airway is the immediate priority after stenosis/framework/laser work; assess stridor, work of breathing, bleeding and aspiration risk.","Give procedure-specific voice use and swallow instructions and arrange laryngoscopic follow-up to assess healing and function."],
 "early":["Airway edema/obstruction, bleeding, aspiration or dysphagia; dental/oral injury from suspension laryngoscopy.","Vocal-fold hemorrhage, mucosal injury or granuloma; implant displacement/airway issue after framework surgery when applicable."],
 "late":["Scar/web/stenosis, dysphonia from stiffness or over/under-correction, granuloma, recurrent lesion or persistent aspiration/dysphagia."],
 "sources":[BOOKS["laryngology"],BOOKS["operative"],BOOKS["cummings"]]},
"pediatric_airway": {
 "setup":["Confirm airway history, prior endoscopy, sizing/grade and comorbid pulmonary/reflux/swallow issues; coordinate a shared-airway anesthetic plan.","Prepare age-appropriate endoscopes, airway rescue equipment and postoperative ICU/airway plan before starting."],
 "landmarks":["glottis/posterior commissure","subglottis/cricoid","recurrent laryngeal nerves","tracheostomy tract if present","carina/bronchi"],
 "exit":["Reassess lumen and mucosa, bleeding and edema; document tube/stent size and position when present.","Make extubation versus planned postoperative intubation/tracheostomy strategy explicit before leaving the OR."],
 "postop":["Continuous airway observation appropriate to reconstruction severity; monitor stridor, retractions, tube/stent position and secretion clearance.","Coordinate feeding/swallow plan and manage reflux/infection/inflammation according to the reconstruction."],
 "early":["Airway obstruction from edema, crust, tube/stent issue or bleeding; pneumothorax/pneumomediastinum after airway injury.","Aspiration, infection, granulation or accidental decannulation/extubation."],
 "late":["Restenosis, granulation, suprastomal collapse, dysphonia, aspiration or failure to decannulate."],
 "sources":[BOOKS["operative"],BOOKS["laryngology"],BOOKS["cummings"]]},
"pediatric": {
 "setup":["Confirm age/weight-specific indication, bleeding/airway risk, developmental comorbidities and postoperative disposition before induction.","Use age-appropriate positioning, instrumentation and medication dosing; define airway rescue plan."],
 "landmarks":["airway","carotid/parapharyngeal space","Eustachian tube orifice when relevant","facial nerve when relevant"],
 "exit":["Obtain meticulous hemostasis and perform procedure-specific airway/bleeding check before emergence.","Set explicit postoperative observation, analgesia, hydration and feeding plan based on age and disease severity."],
 "postop":["Monitor airway, bleeding, hydration and pain; higher-risk OSA/airway patients need appropriate monitored disposition.","Give caregivers clear return precautions for respiratory difficulty, hemorrhage, dehydration or fever."],
 "early":["Airway obstruction/desaturation, bleeding, dehydration, nausea/vomiting or infection depending on operation."],
 "late":["Scar/stenosis, recurrence or persistent functional deficit depending on the procedure."],
 "sources":[BOOKS["operative"],BOOKS["cummings"]]},
"facial_trauma": {
 "setup":["Review thin-cut CT, ocular exam, occlusion, facial nerve/sensation and soft-tissue injury before repair.","Plan reduction/fixation sequence to restore facial width, height, projection and dental occlusion while protecting the globe."],
 "landmarks":["globe/optic nerve","infraorbital nerve","facial nerve","tooth roots","frontal outflow tract/skull base"],
 "exit":["Confirm stable reduction/fixation, occlusion and globe position/motility; repeat forced ductions when indicated.","Obtain hemostasis and tension-free layered closure; document postoperative vision and occlusion."],
 "postop":["Repeat vision/pupil/EOM exam after orbital work; acute vision loss, proptosis or severe orbital pain is an emergency.","Monitor occlusion, infection, wound integrity and sensory/nerve function; use sinus/diet precautions according to fracture pattern."],
 "early":["Retrobulbar hematoma/orbital compartment syndrome, vision loss, entrapment, malocclusion, infection or hardware/wound problem."],
 "late":["Diplopia/enophthalmos, malocclusion, facial asymmetry, sensory deficit, hardware exposure/infection or frontal sinus mucocele depending on injury."],
 "sources":[BOOKS["hn_atlas"],BOOKS["operative"],BOOKS["cummings"]]},
"reconstruction": {
 "setup":["Define defect requirements before incision: lining, support, cover, dead space, function and anticipated adjuvant therapy.","Confirm donor-site anatomy, recipient vessels when applicable and backup reconstructive plan."],
 "landmarks":["vascular pedicle","recipient vessels","facial nerve/critical motor nerves","functional sphincters and ducts"],
 "exit":["Confirm flap/graft perfusion or inset stability without kinking/compression; obtain meticulous hemostasis.","Document drain, pressure-dressing and flap-monitoring plan plus donor-site neurovascular status."],
 "postop":["For vascularized flaps, serial perfusion checks and rapid response to venous or arterial compromise are essential.","Monitor hematoma, infection, fistula, wound tension and donor-site function; protect pedicle from external compression."],
 "early":["Flap vascular compromise, hematoma, infection, dehiscence, fistula or graft loss."],
 "late":["Contour deformity, contracture, stenosis, poor scar, donor-site morbidity or need for revision."],
 "sources":[BOOKS["hn_atlas"],BOOKS["operative"],BOOKS["cummings"]]},
"sleep": {
 "setup":["Confirm OSA phenotype, PAP history, anatomy/DISE findings when relevant and procedure-specific candidacy.","Review airway plan and device/anatomic target; counsel regarding expected residual OSA and need for follow-up sleep testing."],
 "landmarks":["hypoglossal nerve branches","lingual artery","pharyngeal musculature","airway collapse level"],
 "exit":["Confirm hemostasis and intended airway/device effect; check device function when implanted.","Set airway observation and pain/swallow plan based on extent of multilevel surgery."],
 "postop":["Monitor airway obstruction, desaturation, bleeding and swallowing; determine monitored disposition from OSA severity/comorbidity.","For implanted devices, inspect wounds and follow activation/titration schedule rather than immediate therapeutic use."],
 "early":["Airway edema/obstruction, bleeding, dysphagia, tongue weakness or device-related pneumothorax/hematoma depending on operation."],
 "late":["Residual OSA, dysphagia, scar/stenosis, hardware migration/infection or stimulation intolerance."],
 "sources":[BOOKS["operative"],BOOKS["cummings"]]},
"emergency": {
 "setup":["Stabilize airway/hemodynamics first; review imaging/endoscopy only insofar as it does not delay treatment of a threatened airway or hemorrhage.","Prepare definitive and rescue airway/bleeding equipment before manipulating the pathology."],
 "landmarks":["airway","great vessels","esophagus","recurrent laryngeal nerves","mediastinal extension pathways"],
 "exit":["Confirm source control, hemostasis and a safe airway; leave drains or airway adjuncts when clinically required.","Define ICU/floor disposition, repeat imaging/endoscopy needs and antimicrobial plan when infection is present."],
 "postop":["Serial airway and bleeding assessment; monitor for sepsis, mediastinal spread, perforation or re-accumulation according to pathology.","Keep escalation thresholds explicit: stridor, expanding swelling, recurrent hemorrhage, chest pain or toxicity require immediate reassessment."],
 "early":["Recurrent airway compromise or bleeding, sepsis, mediastinitis, perforation, pneumothorax or aspiration depending on case."],
 "late":["Stenosis, fistula, recurrent infection or functional deficit from the underlying injury."],
 "sources":[BOOKS["operative"],BOOKS["cummings"]]},
}


def _profile_for(slug, op):
    t=(slug+" "+str(op.get("title",""))+" "+str(op.get("domain",""))).lower()
    if any(x in t for x in ("thyroidectomy","thyroid lobectomy","reop-thyroid","central-neck")): return "thyroid"
    if "parathyroid" in t or "four-gland" in t: return "parathyroid"
    if any(x in t for x in ("parotid","submandibular","sialendosc","salivary")): return "salivary"
    if any(x in t for x in ("sinus","ethmoid","sphenoid","frontal","draf","nasoseptal","csf","spa-ligation","orbital-abscess")): return "sinus"
    if any(x in t for x in ("tymp","mastoid","staped","cochlear","ossicul","canalplasty","tegmen","vestibular-schwannoma","ear")): return "otology"
    if any(x in t for x in ("microflap","laryng","cordotomy","arytenoid","medialization","injection","botox","zenker","cricophary","tep")): return "laryngology"
    if any(x in t for x in ("ltr","ctr","tracheal-resection","airway-dilation","dlb")): return "pediatric_airway"
    if any(x in t for x in ("tonsil","adenoid","thyroglossal","branchial")): return "pediatric"
    if any(x in t for x in ("orbital-floor","mandible","zmc","nasal-reduction","noe-orif","frontal-sinus-trauma","laryngeal-fracture")): return "facial_trauma"
    if any(x in t for x in ("flap","graft","reanimation","reconstruct","forehead","bilobed","melolabial","cervicofacial")): return "reconstruction"
    if any(x in t for x in ("hypoglossal","sleep","palate","lingual-tonsil","hyoid","geniogloss")): return "sleep"
    if any(x in t for x in ("foreign body","button-battery","pta","deep-neck","abscess")): return "emergency"
    if any(x in t for x in ("neck-dissection","laryngectomy","tors","oral-composite","free-flap","pharyngocutaneous","cancer")): return "headneck"
    d=str(op.get("domain","")).lower()
    if "otology" in d: return "otology"
    if "rhinology" in d: return "sinus"
    if "laryng" in d: return "laryngology"
    if "pediatric" in d: return "pediatric"
    if "sleep" in d: return "sleep"
    if "facial" in d or "trauma" in d: return "facial_trauma"
    if "thyroid" in d or "parathyroid" in d: return "thyroid"
    if "head" in d or "oncology" in d: return "headneck"
    return "emergency"


# High-yield exact procedure refinements. These supplement—not replace—the upstream core sequence.
EXACT = {
 "neck-dissection": {"landmarks":["CN XI","IJV","SCM","carotid/vagus","phrenic nerve","thoracic duct (left)"],"postop_add":["Specifically examine shoulder abduction/CN XI and inspect drain output for chyle, especially after low left-neck dissection."]},
 "total-laryngectomy": {"landmarks":["carotids","hypoglossal/vagus","pharyngeal mucosa","tracheal blood supply","thyroid/parathyroids"],"postop_add":["The patient is a permanent neck breather: oxygenation/ventilation and emergency airway access are through the stoma, not the mouth/nose.","Watch closely for pharyngocutaneous fistula, stomal compromise, hypocalcemia when thyroid/parathyroid tissue is affected, and wound/flap issues."]},
 "cochlear-implant": {"landmarks":["facial nerve","chorda tympani","round window/cochleostomy","sigmoid sinus","tegmen"],"postop_add":["Document facial function and vestibular symptoms; inspect receiver/stimulator wound and counsel that activation occurs later after healing."]},
 "stapedotomy": {"landmarks":["facial nerve","chorda tympani","incus long process","stapes footplate","oval window"],"postop_add":["Sudden profound hearing change or severe persistent vertigo after stapes surgery warrants urgent otologic reassessment."]},
 "maxillary-antrostomy": {"landmarks":["natural maxillary ostium","uncinate","orbit","nasolacrimal duct","posterior fontanelle"],"postop_add":["Ensure the antrostomy incorporates the natural ostium to avoid mucus recirculation."]},
 "draf": {"landmarks":["frontal beak","first olfactory fiber/skull base","orbit","anterior ethmoid artery","frontal outflow tract"],"postop_add":["Long-term patency depends on mucosal preservation, postoperative debridement and prevention of cicatricial stenosis."]},
 "csf-nasoseptal": {"landmarks":["vascular pedicle of nasoseptal flap","skull-base defect","carotids/optic nerves by approach","orbit","sphenoid/clival landmarks"],"postop_add":["Clear rhinorrhea, meningitic symptoms or pneumocephalus-type neurologic change after skull-base repair require urgent evaluation for reconstruction failure/CSF leak."]},
 "thyroidectomy": {"postop_add":["An expanding neck hematoma after thyroidectomy is time-critical; respiratory distress or rapidly progressive swelling should trigger immediate decompression and definitive hemostasis."]},
 "parotid-total": {"postop_add":["Grade and document every facial-nerve division postoperatively; protect the cornea if eye closure is incomplete."]},
 "tonsillectomy": {"postop_add":["Any post-tonsillectomy hemorrhage is potentially significant; assess airway/hemodynamics, establish IV access, and escalate operative control according to active bleeding and local protocol."]},
 "orbital-floor": {"postop_add":["Repeat visual acuity/pupils/EOM immediately; new vision loss or tense proptosis requires emergency orbital-compartment management."]},
 "microflap": {"postop_add":["Protect the superficial lamina propria: postoperative voice-use instructions and follow-up stroboscopy are part of the operation’s functional result."]},
 "medialization": {"postop_add":["Observe for airway compromise/hematoma and assess voice plus swallowing; implant malposition can produce undercorrection, overcorrection or airway symptoms."]},
 "injection-laryngoplasty": {"postop_add":["Observe for rare airway compromise from overinjection/edema and reassess voice/swallow; expected durability depends on injectate."]},
 "peds-ltr": {"postop_add":["Stent/ETT position, secretion clearance and planned airway duration are critical postoperative variables; accidental displacement can be catastrophic."]},
 "ctr": {"postop_add":["Protect the cricotracheal anastomosis from tension; document neck-position precautions and watch for dehiscence, restenosis and recurrent laryngeal nerve dysfunction."]},
 "tracheal-resection": {"postop_add":["Anastomotic protection is central: avoid neck hyperextension and monitor for subcutaneous emphysema, respiratory deterioration or signs of dehiscence."]},
 "hypoglossal-stimulator": {"postop_add":["Check tongue motion and wounds; chest pain/dyspnea should prompt evaluation for pneumothorax. Device activation/titration occurs after wound healing."]},
 "free-flap-basics": {"postop_add":["A change in flap color, turgor, temperature or Doppler signal is a surgical emergency until proven otherwise; early salvage depends on rapid re-exploration."]},
}


def _dedupe(seq):
    out=[]; seen=set()
    for x in seq or []:
        s=str(x).strip()
        if not s or s.lower() in seen: continue
        seen.add(s.lower()); out.append(s)
    return out


def apply_or_overhaul_v190(registry):
    report={"total":0,"profiles":{},"exact":0}
    for slug,op in (registry or {}).items():
        report["total"]+=1
        family=_profile_for(slug,op); p=PROFILES[family]
        report["profiles"][family]=report["profiles"].get(family,0)+1
        op["or_family_v190"]=family
        op["setup"]=_dedupe(p["setup"])
        op["landmarks"]=_dedupe((op.get("landmarks") or [])+p["landmarks"])
        core=_dedupe(op.get("steps") or [])
        # Make the live sequence explicitly start with exposure/verification and end with a safe-exit check.
        if not core: core=["Expose the operative target using the procedure-appropriate approach while preserving critical landmarks."]
        opener="Perform the planned exposure and positively identify the critical anatomy before the irreversible portion of the operation."
        closer="Reinspect the operative field for hemostasis, anatomic integrity and completion of the procedure-specific objective before closure/emergence."
        if len(core)<6: core=[opener]+core+[closer]
        op["steps"]=_dedupe(core)
        op["exit_check"]=_dedupe(p["exit"])
        op["postop"]=_dedupe(p["postop"])
        op["complications"]={"early":_dedupe(p["early"]),"late":_dedupe(p["late"])}
        op["source_basis"]=_dedupe((op.get("source_basis") or [])+p["sources"])
        op["review_status_v190"]="operative-depth reviewed"
        ex=EXACT.get(slug)
        if ex:
            report["exact"]+=1
            if ex.get("landmarks"): op["landmarks"]=_dedupe(ex["landmarks"]+op["landmarks"])
            if ex.get("postop_add"): op["postop"]=_dedupe(op["postop"]+ex["postop_add"])
    return report
