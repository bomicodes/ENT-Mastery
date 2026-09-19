"""v39.1 -- General ENT / Emergencies depth repair (content-staleness sweep, batch 2/9).

Same two defects as v39.0: recognize/localize duplication and an unfilled
operate placeholder. See thyroglossal_duct_cyst_depth_v389 for the pattern
and rationale.
"""

DOMAIN = "General ENT / Emergencies"

DEPTH_V391 = {
    "Esophageal Foreign Body": {
        "recognize": (
            "Suspect an esophageal foreign body with new dysphagia, drooling, chest/throat pain, "
            "refusal to eat (children), or a witnessed/reported ingestion. Urgency is dictated by "
            "object type and location, not by symptom severity alone: a button battery or sharp "
            "object anywhere in the esophagus, or any object causing complete obstruction (unable "
            "to handle secretions), is an emergency regardless of how well the patient otherwise looks."
        ),
        "localize": (
            "Most esophageal foreign bodies lodge at one of three physiologic narrowings: the "
            "cricopharyngeus (most common, especially in children), the level of the aortic arch/"
            "left mainstem bronchus crossing, or the lower esophageal sphincter. Lateral and AP neck/"
            "chest radiographs localize radiopaque objects and, for a coin, the flat orientation on "
            "AP view is what distinguishes an esophageal from a tracheal foreign body (which appears "
            "flat on lateral view instead)."
        ),
        "operate": (
            "Indication: any button battery or sharp object in the esophagus (remove emergently, "
            "ideally within 2 hours for a battery), complete obstruction, or a symptomatic/persistent "
            "foreign body. Setup: rigid or flexible esophagoscopy under general anesthesia with the "
            "airway secured. Key steps: assess the mucosa for injury before extraction, remove the "
            "object under direct/endoscopic visualization with an appropriate retrieval instrument "
            "for its shape, and re-inspect the esophagus circumferentially after removal for "
            "perforation, burn, or pressure necrosis. Danger structures: the tracheal membranous "
            "wall and great vessels immediately posterior/anterior to the esophagus, especially at "
            "the level of battery-related injury, since a battery held against the wall can perforate "
            "into the airway or aorta. Failure mode: underestimating how fast battery injury "
            "progresses (liquefactive necrosis begins within hours) and delaying removal, or missing "
            "a deep mucosal burn that later perforates. Postoperative plan: for battery-related injury, "
            "admit for observation, serial exam/imaging to watch for delayed perforation or vascular "
            "injury (which can occur days later), and staged advancement of diet only once the injury "
            "is judged stable."
        ),
    },
    "Airway Foreign Body": {
        "recognize": (
            "Classic presentation is a witnessed choking episode with sudden coughing, followed by "
            "the choking triad of cough, wheeze, and decreased breath sounds, most often unilateral. "
            "A completely normal chest x-ray does not exclude aspiration -- most aspirated foreign "
            "bodies are radiolucent (food, plastic), so a convincing history of a choking event "
            "should drive further evaluation even with a normal film."
        ),
        "localize": (
            "Objects most often lodge in a mainstem bronchus (right more often than left, due to its "
            "wider, more vertical takeoff), producing unilateral air trapping (hyperinflation on "
            "expiratory or decubitus films) or, if more proximal, tracheal/laryngeal symptoms with "
            "stridor. Bilateral wheeze or a normal exam does not rule out an airway foreign body, "
            "particularly early or with a partially obstructing object."
        ),
        "operate": (
            "Indication: witnessed or strongly suspected foreign body aspiration -- history alone "
            "can justify bronchoscopy even with normal imaging and exam. Setup: rigid bronchoscopy "
            "under spontaneous or controlled ventilation general anesthesia, with a range of "
            "retrieval forceps and rigid telescopes available for the suspected object type. Key "
            "steps: systematic airway survey from larynx to segmental bronchi before assuming a "
            "single object or location, gentle grasping and en-bloc removal preserving the airway "
            "outside the scope, and re-inspection after removal for residual fragments or mucosal "
            "injury. Danger structures: the airway itself -- an object pushed distally during "
            "instrumentation, or bleeding/edema obscuring the field, can convert a partial "
            "obstruction into a complete one. Failure mode: a complete, unstable airway obstruction "
            "requires immediate age-appropriate rescue (back blows/chest thrusts in an infant, "
            "abdominal thrusts or direct laryngoscopy with Magill forceps in an older child/adult) "
            "before any controlled OR bronchoscopy is possible. Postoperative plan: observe for "
            "post-obstructive edema/stridor, especially after a prolonged or traumatic retrieval, and "
            "repeat imaging or bronchoscopy if a fragment is suspected to remain."
        ),
    },
    "Chyle Leak": {
        "recognize": (
            "Suspect thoracic duct injury when drain output becomes milky/turbid (classically after "
            "enteral feeding, when chylomicron content rises) or when output volume increases rather "
            "than trends down after neck dissection, especially level IV/low-left-neck surgery where "
            "the thoracic duct terminates near the left jugulo-subclavian confluence."
        ),
        "localize": (
            "The thoracic duct enters the venous system at the left jugulo-subclavian angle, so it "
            "is at greatest risk during left-sided low neck (level IV/VB) dissection; a right-sided "
            "leak is possible but less common, from the smaller right lymphatic duct or an aberrant "
            "duct anatomy. Leaks are graded by daily output, which drives management more than the "
            "anatomic injury itself."
        ),
        "operate": (
            "Indication for operative/interventional repair: high-output leak (commonly cited "
            "threshold around 500-1000 mL/day, though practice varies) or persistence despite "
            "conservative measures. Initial management is non-operative: low-fat/medium-chain-"
            "triglyceride diet or complete enteral fasting with TPN, pressure dressing, and drain "
            "management to control output while watching nutritional and electrolyte status. Key "
            "steps if operative: re-explore the site of injury, ligate or clip the identified duct "
            "end (intraoperative cream/fat feeding can help visualize the leak), and consider fibrin "
            "sealant or muscle flap reinforcement; interventional radiology thoracic duct embolization "
            "is an alternative to open re-exploration in selected cases. Danger structures: the "
            "phrenic nerve, subclavian vessels, and brachial plexus in the reoperative low-neck field "
            "where scarring from the index dissection is already present. Failure mode: treating "
            "chyle leak as a simple drain problem rather than a systemic issue -- prolonged high-"
            "output leak causes lymphopenia, hypoalbuminemia, and immunosuppression from loss of "
            "lymphocytes and protein, which changes the urgency of definitive control. Postoperative "
            "plan: trend drain output and nutritional labs, advance diet stepwise only once output "
            "has resolved, and document immunologic/nutritional recovery before considering the leak "
            "closed."
        ),
    },
    "Deep Neck Abscess Drainage": {
        "recognize": (
            "Suspect a deep neck space abscess with fever, neck swelling/pain, trismus, odynophagia, "
            "or torticollis, particularly following dental infection, tonsillitis, or penetrating "
            "trauma; the anatomic space involved -- not simply the presence of pus -- determines both "
            "risk (airway, mediastinum, carotid sheath) and surgical approach."
        ),
        "localize": (
            "Contrast CT maps the involved deep neck space(s) -- peritonsillar, parapharyngeal, "
            "retropharyngeal, submandibular/Ludwig's, or the danger space/prevertebral space -- and "
            "their relationship to the airway and carotid sheath. Retropharyngeal and danger-space "
            "infections carry direct mediastinal-spread risk; parapharyngeal space infection carries "
            "carotid sheath risk; these anatomic relationships, not abscess volume, dictate urgency "
            "and the safest surgical route."
        ),
        "operate": (
            "Indication: a drainable, organized abscess (vs. phlegmon, which may respond to "
            "antibiotics alone), airway compromise, or failure to improve on IV antibiotics. Setup: "
            "route is chosen by space involved -- transoral for peritonsillar/parapharyngeal "
            "prestyloid collections accessible without crossing the great vessels, external "
            "(transcervical) for submandibular, retropharyngeal in a young child, or poststyloid "
            "parapharyngeal disease near the carotid sheath. Key steps: secure the airway first if "
            "compromised (awake fiberoptic intubation or tracheostomy may be needed before drainage "
            "in severe trismus/distortion), open the space along a plane that avoids the carotid "
            "sheath and cranial nerves, break up loculations, obtain cultures, and leave a drain when "
            "appropriate. Danger structures: internal carotid artery and internal jugular vein in the "
            "poststyloid parapharyngeal space, the facial artery/lingual and hypoglossal nerves in the "
            "submandibular space, and the prevertebral fascia bounding the danger space above the "
            "mediastinum. Failure mode: choosing a route based on where the swelling is most visible "
            "rather than which route reaches the actual infected compartment without traversing "
            "avoidable neurovascular structures, or failing to escalate to open drainage when "
            "antibiotics alone are not controlling a true abscess. Postoperative plan: continue "
            "targeted antibiotics per culture, serial airway and clinical reassessment, and repeat "
            "imaging if improvement stalls to exclude a residual or new-space collection."
        ),
    },
}


def apply_depth_content_general_ent_v391(data_module):
    modules = {m.get("topic"): m for m in data_module.DEEP_MODULES_V6.get(DOMAIN, [])}
    missing = [t for t in DEPTH_V391 if t not in modules]
    if missing:
        raise RuntimeError(f"v39.1: expected {DOMAIN} topics not found: {missing}")
    for topic, fields in DEPTH_V391.items():
        modules[topic].update(fields)
    return {"enriched": list(DEPTH_V391.keys())}
