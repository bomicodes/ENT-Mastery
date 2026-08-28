"""v26.4 — Sleep Surgery deliberate ladder pass 2.

Adds five exact canonical Sleep Surgery topics with complete foundation ->
application -> senior-decision ladders. Reuses the existing sleep OR-management
framework for tongue-base surgery and HNS, then adds missing palatal-pattern,
MMA, residual-OSA, complication-rescue, and nonresponse decision layers.
"""
DOMAIN = "Sleep Surgery"


def _q(qid, topic, stage, stem, choices, answer, explanation, reasons, pearl,
       curveball, focus="boards"):
    return {
        "id": qid, "domain": DOMAIN, "topic": topic, "learning_stage": stage,
        "stem": stem, "choices": choices, "answer": answer,
        "explanation": explanation, "why_wrong": reasons,
        "board_pearl": pearl, "curveball": curveball,
        "tier": "Curated learning ladder", "mode": "Vignette", "focus": focus,
        "ladder_reviewed": True, "_coverage_reviewed_v211": True,
    }


VIGNETTES_V264 = [
    _q("v264_sleep_palate_fnd", "Palatal Surgery", "foundation",
       "An adult with PAP-intolerant OSA has dominant retropalatal obstruction with lateral pharyngeal-wall collapse. What is the core principle when choosing palatal surgery?",
       ["Match the reconstruction to the collapse pattern and preserve swallowing/velopharyngeal function rather than simply removing as much soft palate as possible", "Resect the uvula and palate maximally in every patient", "Treat palatal surgery as equivalent to nasal surgery", "Ignore lateral-wall collapse because only the tongue base matters"], 0,
       "Modern palatal surgery is pattern-directed reconstruction. Procedures that reposition or stiffen the palate and lateral pharyngeal walls should be selected according to the demonstrated collapse phenotype while preserving speech and swallowing function.",
       ["Correct. The operation should address the observed palatal/lateral-wall mechanism while minimizing functional injury.", "Maximal tissue excision increases pain, scar, velopharyngeal dysfunction and stenosis without guaranteeing better OSA control.", "Nasal surgery and palatal surgery address different airway segments and therapeutic goals.", "Lateral-wall collapse can be a major driver of retropalatal obstruction and treatment failure."],
       "Think reconstruction and vector, not simply resection, when discussing contemporary palatal surgery.",
       "How would large tonsils alter the operative plan when lateral-wall collapse is also present?", "OR_prep"),
    _q("v264_sleep_palate_app", "Palatal Surgery", "application",
       "DISE shows circumferential retropalatal narrowing driven largely by lateral pharyngeal-wall collapse in a patient with small tonsils and little isolated anteroposterior palatal flutter. What is the best surgical reasoning?",
       ["Favor a palatal/lateral-wall reconstructive strategy directed at the demonstrated collapse rather than assuming a classic tissue-resection UPPP alone will address the phenotype", "Perform isolated nasal valve repair because DISE identified the palate", "Choose tongue-base reduction solely because the AHI is severe", "Skip counseling about dysphagia, voice or velopharyngeal symptoms because these are unrelated to palatal surgery"], 0,
       "Palatal procedures are not interchangeable. Lateral-wall-predominant collapse may be better addressed by reconstructive pharyngoplasty concepts than by indiscriminate central palatal resection, and counseling should reflect procedure-specific functional risks.",
       ["Correct. Collapse configuration should drive the selected palatal vector and extent of surgery.", "Nasal surgery may improve breathing or PAP tolerance but does not directly correct a DISE-demonstrated retropalatal collapse pattern.", "OSA severity does not identify the obstructing level; tongue-base surgery requires a tongue-base target.", "Palatal operations can affect swallowing, resonance, globus and velopharyngeal competence and require explicit counseling."],
       "A high AHI tells you severity; DISE and examination tell you where and how to operate.",
       "When might multilevel rather than isolated palatal surgery be reasonable, and how would you counsel that success is not guaranteed?", "OR_prep"),
    _q("v264_sleep_palate_snr", "Palatal Surgery", "senior_decision",
       "On the first postoperative night after palatal surgery, a patient has repeated bright-red oral bleeding, tachycardia and increasing difficulty handling secretions. What is the best senior response?",
       ["Treat this as a potentially significant postoperative hemorrhage: assess airway/hemodynamics, obtain immediate operative help and proceed to definitive hemostasis when bleeding is ongoing or clinically important", "Reassure the patient that all palatal bleeding is expected", "Give a sedative and wait for the bleeding to stop", "Delay evaluation until a routine postoperative sleep study"], 0,
       "Post-palatal-surgery bleeding can threaten both circulation and the airway. Active or recurrent significant hemorrhage requires airway-aware resuscitation and timely source control rather than routine observation.",
       ["Correct. Airway protection, resuscitation and operative hemostasis take priority when hemorrhage is clinically significant.", "Small blood-tinged secretions may occur, but repeated bright-red bleeding with physiologic change is not routine.", "Sedation can worsen airway protection and does not provide source control.", "A sleep study has no role in managing acute postoperative hemorrhage."],
       "After sleep surgery, bleeding plus impaired secretion handling is an airway problem until proven otherwise.",
       "How would delayed nasopharyngeal stenosis or persistent velopharyngeal insufficiency present differently from an acute hemorrhage?", "overnight_call"),

    _q("v264_sleep_tongue_fnd", "Tongue Base Surgery", "foundation",
       "What should determine whether tongue-base surgery is added to an adult OSA operation?",
       ["Evidence of clinically meaningful tongue-base or hypopharyngeal obstruction from the sleep evaluation and anatomic assessment, with the chosen procedure matched to that mechanism", "The total AHI alone", "The presence of snoring alone", "A desire to perform the same multilevel operation in every patient"], 0,
       "Tongue-base procedures should target a demonstrated obstructive component. Options such as lingual tonsil reduction, genioglossus advancement, hyoid procedures or other tongue-base reduction techniques address different anatomic mechanisms.",
       ["Correct. Target identification precedes procedure selection.", "AHI measures severity but does not localize obstruction.", "Snoring is nonspecific and does not establish tongue-base collapse.", "Fixed procedure bundles ignore patient-specific anatomy and increase unnecessary morbidity."],
       "Do not add a tongue-base operation because OSA is severe; add it because the tongue base is part of the demonstrated mechanism.",
       "How does true lingual-tonsil hypertrophy differ from skeletal retroposition or dynamic tongue-base collapse when choosing an operation?", "OR_prep"),
    _q("v264_sleep_tongue_app", "Tongue Base Surgery", "application",
       "A patient with PAP-intolerant OSA has prominent lingual tonsil tissue filling the vallecula and DISE-confirmed tongue-base obstruction. Which planning point is most important before transoral lingual-tonsil reduction?",
       ["Plan exposure and hemostasis with awareness of postoperative tongue-base edema, bleeding and nearby neurovascular structures, and choose monitored postoperative disposition according to airway risk", "Assume postoperative airway swelling cannot occur because the surgery is transoral", "Resect into deep tongue musculature until the epiglottis is completely skeletonized", "Ignore anticoagulant history because tongue-base bleeding is always minor"], 0,
       "The tongue base is a vascular, airway-critical operative site. Adequate exposure, conservative depth, hemostatic planning and postoperative airway observation are central to safe surgery.",
       ["Correct. Airway edema and hemorrhage are the complications that change immediate perioperative planning.", "Transoral access does not eliminate edema or obstruction risk.", "Excessively deep resection increases bleeding and neural injury without a therapeutic requirement to skeletonize the epiglottis.", "Medication-related bleeding risk matters substantially in a vascular tongue-base field."],
       "For tongue-base surgery, the postoperative airway plan belongs in the preoperative plan.",
       "What findings would favor skeletal advancement or hyoid-based surgery rather than simply removing lingual tonsil tissue?", "OR_prep"),
    _q("v264_sleep_tongue_snr", "Tongue Base Surgery", "senior_decision",
       "Several hours after tongue-base surgery, a patient develops progressive muffled voice, floor-of-mouth fullness, tongue weakness and increasing oxygen requirement. What is the best senior action?",
       ["Urgently evaluate for hematoma, bleeding and airway edema; mobilize airway/OR resources early rather than waiting for complete obstruction", "Attribute all symptoms to routine postoperative pain", "Give oral fluids and discharge if the incision is not visible externally", "Wait for a repeat PSG before deciding whether intervention is needed"], 0,
       "Progressive swelling or neurologic change after tongue-base surgery can rapidly become an airway emergency. Examination, airway control and source control take precedence over routine postoperative pathways.",
       ["Correct. Early escalation is appropriate because a deteriorating tongue-base airway can become difficult to rescue.", "Pain alone does not explain progressive fullness, weakness and oxygen requirement.", "An external incision is not required for a dangerous deep oral or tongue-base hematoma.", "PSG is an outcome test, not an acute airway-rescue tool."],
       "A worsening tongue-base postoperative airway should be rescued before it becomes impossible to access.",
       "How would new dental pain or malocclusion after genioglossus advancement shift the complication differential?", "overnight_call"),

    _q("v264_sleep_mma_fnd", "Maxillomandibular Advancement", "foundation",
       "Why can maxillomandibular advancement improve obstructive sleep apnea?",
       ["Advancing the maxilla and mandible enlarges and tensions the attached retropalatal and retroglossal soft-tissue airway rather than treating only one mucosal subsite", "It produces continuous positive airway pressure", "It treats central apnea by increasing respiratory drive", "Its sole purpose is to remove the tonsils"], 0,
       "MMA is a skeletal framework operation. Forward movement of the facial skeleton advances multiple soft-tissue attachments and can enlarge the airway at more than one pharyngeal level.",
       ["Correct. The multilevel skeletal effect distinguishes MMA from a focal soft-tissue operation.", "MMA changes anatomy; it does not generate positive airway pressure.", "Central respiratory-drive failure is not corrected by facial skeletal advancement.", "Tonsil removal is a separate operation and is not the mechanism of MMA."],
       "MMA treats the airway framework, which is why it can affect both retropalatal and retroglossal dimensions.",
       "Which craniofacial findings make skeletal advancement particularly intuitive even though normal facial proportions do not exclude benefit?"),
    _q("v264_sleep_mma_app", "Maxillomandibular Advancement", "application",
       "A PAP-intolerant patient with severe OSA and mandibular/maxillary retrusion is considering MMA. Which preoperative issue most directly distinguishes responsible planning from simply choosing an advancement distance?",
       ["Coordinate occlusion, dental/orthodontic status, facial skeletal goals, airway objectives and patient-specific anatomy so advancement improves the airway without creating unacceptable bite or facial-function problems", "Ignore preoperative occlusion because airway improvement is the only outcome", "Select the same millimeter advancement for every patient", "Assume DISE or PSG becomes unnecessary once retrognathia is seen"], 0,
       "MMA planning is simultaneously sleep surgery and orthognathic surgery. Occlusion, skeletal relationships, dentition, facial balance, nerve risk and airway goals must be integrated rather than reduced to a universal numeric movement.",
       ["Correct. Functional occlusion and skeletal stability are essential components of an airway operation.", "An operation that improves AHI but leaves disabling malocclusion is not a well-planned result.", "Required movement is individualized to anatomy, occlusion and treatment goals.", "Craniofacial anatomy does not replace objective characterization of the sleep disorder."],
       "MMA is not 'move both jaws forward'; it is a planned skeletal reconstruction with an airway endpoint.",
       "What roles do virtual planning, orthodontics and anticipated nasal/facial change play in informed consent?", "OR_prep"),
    _q("v264_sleep_mma_snr", "Maxillomandibular Advancement", "senior_decision",
       "After MMA, a patient develops rapidly increasing facial/oral swelling, floor-of-mouth fullness, bloody drainage and worsening work of breathing. What is the best senior response?",
       ["Treat this as a threatened postoperative airway and possible hemorrhage: mobilize airway and surgical resources immediately, assess hemodynamics and obtain source control rather than relying on routine postoperative edema management", "Assume all swelling is expected after orthognathic surgery", "Apply elastics more tightly and observe", "Delay airway evaluation until postoperative imaging is routinely obtained"], 0,
       "MMA creates substantial postoperative edema and can bleed into an airway-adjacent field. Progressive swelling with respiratory change requires urgent differentiation of expected edema from hematoma/hemorrhage and a low threshold for airway intervention.",
       ["Correct. Airway deterioration after major skeletal sleep surgery requires immediate escalation.", "Expected edema should not cause progressive respiratory compromise without urgent reassessment.", "Tighter fixation does not treat hemorrhage or an obstructed airway and can impede access.", "Imaging must not delay stabilization of a threatened airway."],
       "In major sleep surgery, normal postoperative swelling and dangerous airway swelling are separated by trajectory and physiology, not by appearance alone.",
       "Which late findings would instead suggest malocclusion, nonunion, hardware infection or inferior-alveolar nerve morbidity?", "overnight_call"),

    _q("v264_sleep_residual_fnd", "Residual OSA After Surgery", "foundation",
       "A patient feels better after OSA surgery but still snores intermittently. What is the best principle for determining whether clinically important OSA remains?",
       ["Use appropriate objective sleep reassessment together with symptoms and treatment goals rather than declaring cure from symptom improvement alone", "Assume improved snoring proves the AHI is normal", "Use office examination alone to calculate residual AHI", "Repeat surgery before measuring the postoperative phenotype"], 0,
       "Symptoms and snoring may improve without complete physiologic resolution. Objective reassessment is important when determining treatment success, residual risk and the need for adjunctive therapy.",
       ["Correct. Postoperative outcome assessment should include physiology when residual disease matters clinically.", "Snoring and OSA overlap but are not interchangeable outcomes.", "Awake examination cannot quantify sleep event burden.", "Reoperation should follow characterization of the residual problem, not precede it."],
       "A successful operation can still leave clinically meaningful OSA; measure the result before planning the next intervention.",
       "How would a large improvement in AHI but persistent severe oxygen burden change your definition of success?", "sleep_interpretation"),
    _q("v264_sleep_residual_app", "Residual OSA After Surgery", "application",
       "Postoperative PSG after palatal and tongue-base surgery shows residual OSA almost entirely when supine, with minimal nonsupine disease. The patient otherwise feels well. What is the best next reasoning step?",
       ["Treat the residual phenotype rather than reflexively repeating the same surgery; consider positional strategy and other appropriate adjuncts before another anatomic operation", "Repeat identical multilevel surgery because any residual AHI means the first operation failed technically", "Ignore the positional distribution and use only the total AHI", "Proceed directly to tracheostomy"], 0,
       "Residual OSA should be re-phenotyped. Position, sleep stage, weight change, central-event burden and remaining anatomic collapse can identify less morbid or more specifically targeted next treatments.",
       ["Correct. The postoperative disease is now strongly position dependent and the next therapy should reflect that new phenotype.", "Persistent disease does not prove a technical failure or justify repeating the same mechanism blindly.", "A global AHI can hide the feature most useful for selecting the next treatment.", "Tracheostomy is not a routine response to otherwise manageable positional residual OSA."],
       "After surgery, treat the OSA the patient still has—not the OSA they had before the operation.",
       "How would residual central events instead redirect the workup away from additional upper-airway surgery?", "sleep_interpretation"),
    _q("v264_sleep_residual_snr", "Residual OSA After Surgery", "senior_decision",
       "A patient has persistent severe OSA after two anatomically targeted operations. Before proposing a third surgery, what is the best senior approach?",
       ["Re-establish the current phenotype with objective sleep data, adherence/weight review and focused airway reassessment, then choose PAP, device, positional, oral-appliance, weight or revision surgery according to the demonstrated failure mechanism", "Assume scar tissue is the cause and schedule revision without new testing", "Choose the most aggressive remaining operation regardless of anatomy", "Use the preoperative DISE from years ago as sufficient evidence of the current obstruction"], 0,
       "Repeated treatment failure is a signal to re-diagnose the problem. Anatomy, weight, sleep position, event type and prior surgical effects can change, and a different therapy class may be more rational than another empiric operation.",
       ["Correct. Senior decision-making localizes why prior treatment failed before adding morbidity.", "Scar may contribute but cannot be assumed without reassessment.", "Escalating invasiveness without a matched target increases risk without improving mechanism-based care.", "Old dynamic anatomy may not represent the current postoperative airway."],
       "Residual OSA is not a mandate for more surgery; it is a mandate for better localization of the remaining problem.",
       "When would repeat DISE, PAP retrial, oral appliance testing or consideration of MMA meaningfully change the decision?", "senior_management"),

    _q("v264_sleep_hnsnr_fnd", "HNS Troubleshooting / Nonresponse", "foundation",
       "A patient uses HNS nightly but the follow-up study shows persistent OSA. What is the first troubleshooting principle?",
       ["Separate adherence, hardware integrity, sensing/timing, stimulation recruitment and residual airway phenotype before labeling the therapy a global failure", "Assume the generator is defective", "Increase amplitude to maximum immediately", "Explanted the system before interrogation"], 0,
       "HNS nonresponse has multiple possible mechanisms. A structured evaluation distinguishes whether therapy is not being delivered, is poorly programmed, recruits an unfavorable tongue pattern, or leaves untreated collapse elsewhere.",
       ["Correct. Troubleshooting is mechanism based rather than a single amplitude adjustment.", "Normal or abnormal hardware must be demonstrated rather than assumed.", "More amplitude can worsen discomfort or tongue recruitment and does not correct every failure mechanism.", "Explantation is premature before noninvasive and anatomic causes are characterized."],
       "HNS nonresponse is a differential diagnosis, not a diagnosis of broken hardware.",
       "What information can remote-use data, examination of tongue motion and device interrogation each contribute?", "device_management"),
    _q("v264_sleep_hnsnr_app", "HNS Troubleshooting / Nonresponse", "application",
       "An HNS patient has excellent nightly use and normal lead impedances. Stimulation produces tongue protrusion, yet residual events cluster supine and repeat airway evaluation shows persistent lateral-wall collapse. What is the best interpretation?",
       ["The device may be functioning technically while the residual airway phenotype remains incompletely treated; optimize programming and address the position/lateral-wall mechanism rather than calling this hardware failure", "Normal impedances prove HNS must normalize the AHI", "Visible tongue protrusion excludes residual palatal or lateral-wall obstruction", "Replace the pulse generator immediately"], 0,
       "Technical function and physiologic efficacy are different endpoints. Persistent non-tongue-base collapse or positional susceptibility can limit response even when the implanted system works normally.",
       ["Correct. The failure mechanism is likely residual airway physiology rather than a simple broken component.", "Electrical integrity does not guarantee whole-airway opening during sleep.", "Tongue motion can coexist with untreated palatal or lateral-wall collapse.", "Generator replacement does not address a demonstrated residual anatomic pattern."],
       "A device can work exactly as programmed and still be the wrong or incomplete solution for the remaining collapse.",
       "How could electrode configuration, timing or adjunctive positional therapy be tested before surgical revision?", "device_management"),
    _q("v264_sleep_hnsnr_snr", "HNS Troubleshooting / Nonresponse", "senior_decision",
       "A previously effective HNS patient has abrupt loss of benefit after months of stable control. Tongue movement is now absent despite commanded stimulation, and interrogation shows an abnormal system parameter. What is the best senior next step?",
       ["Localize a possible hardware/lead problem with device interrogation and targeted imaging/testing as appropriate, while reassessing the airway and planning revision only after the failed component or mechanism is identified", "Treat the abrupt change as inevitable progression of OSA and ignore the device", "Increase amplitude indefinitely despite absent tongue movement", "Perform palatal surgery without investigating the implant"], 0,
       "Abrupt loss of previously demonstrated efficacy is different from primary nonresponse. New absent recruitment plus abnormal device data raises concern for a system problem that should be localized before revision.",
       ["Correct. The timing and objective device abnormality make hardware or lead dysfunction a priority differential.", "A sudden change with abnormal interrogation deserves a device-focused evaluation rather than assumption of natural progression.", "Escalating output without recruitment can cause discomfort and delays localization of the malfunction.", "Unrelated airway surgery should not precede evaluation of a newly abnormal implanted system."],
       "Primary nonresponse asks whether the therapy matches the airway; abrupt secondary failure asks what changed in a previously working system.",
       "How would preserved tongue motion with recurrent OSA shift concern toward weight change, new positional disease or residual airway collapse instead?", "senior_management"),
]


def apply_learning_ladders_v264(challenges, concept_id_fn):
    """Append only missing v26.4 cases and attach exact canonical concept IDs."""
    existing = {str(q.get("id")) for q in challenges}
    added = 0
    for source in VIGNETTES_V264:
        if source["id"] in existing:
            continue
        q = dict(source)
        q["concept_id"] = concept_id_fn(DOMAIN, q["topic"])
        challenges.append(q)
        existing.add(q["id"])
        added += 1
    return added
