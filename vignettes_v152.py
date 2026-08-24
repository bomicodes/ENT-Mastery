"""v15.2 — Cross-domain chief-level decision-depth pass.

Nine deliberately nonredundant cases, one per major domain. Each targets a
high-consequence OR, overnight-call, or postoperative decision rather than
simple diagnosis recognition.
"""


def _c(qid,d,t,s,ch,a,e,ww,p,cb,f):
    return {"id":qid,"domain":d,"topic":t,"stem":s,"choices":ch,"answer":a,
            "explanation":e,"why_wrong":ww,"board_pearl":p,"curveball":cb,
            "tier":"Curated chief-level depth","mode":"Vignette","focus":f}

O="Otology / Neurotology"; R="Rhinology / Allergy / Skull Base"; H="Head & Neck Oncology"
T="Thyroid / Parathyroid / Salivary"; P="Pediatric Otolaryngology"; L="Laryngology / Voice / Swallowing"
F="Facial Plastics / Trauma"; S="Sleep Surgery"; G="General ENT / Emergencies"

VIGNETTES_V152=[
_c("v152_oto_01",O,"Chronic Otitis Media / Cholesteatoma",
"During cholesteatoma surgery, matrix overlies a lateral semicircular canal fistula. The patient had serviceable hearing preoperatively. Which operative strategy best balances disease control with inner-ear preservation?",
["Strip all matrix from the fistula immediately with aggressive suction","Leave the fistula unrecognized and close","Control disease around the fistula, avoid suction/trauma over it, and manage adherent matrix deliberately with preservation of the membranous labyrinth as the priority","Convert automatically to labyrinthectomy"],2,
"A labyrinthine fistula turns routine matrix removal into a hearing-preservation problem. The surgeon should define the fistula, minimize pressure and suction trauma, remove disease in a controlled fashion, and avoid violating the membranous labyrinth; technique may be individualized to fistula size, hearing, and adherence.",
["Aggressive suction and traction can transmit pressure or directly injure the membranous labyrinth and convert serviceable hearing to profound SNHL.","Failure to recognize and address the fistula leaves both residual disease and an unplanned inner-ear risk.","Correct.","Labyrinthectomy sacrifices residual vestibular and cochlear function and is not automatic when hearing is serviceable."],
"When cholesteatoma meets labyrinth, disease eradication is still the goal—but atraumatic handling of the fistula becomes the operative discriminator.",
"If the patient already had a dead ear and extensive labyrinthine destruction, how would your priorities change?","OR_prep"),

_c("v152_rh_01",R,"Orbital Complications of Sinusitis",
"A child admitted on IV antibiotics for orbital cellulitis develops worsening proptosis, new afferent pupillary defect, and declining visual acuity over two hours. CT shows a medial subperiosteal collection. What is the best next step?",
["Continue the same antibiotics overnight because most children improve medically","Urgent surgical drainage with ENT/ophthalmology while continuing IV antibiotics","Discharge with oral antibiotics","Delay intervention until repeat CT in 48 hours"],1,
"Objective visual deterioration is an escalation trigger. A drainable orbital collection plus declining acuity or optic-nerve signs requires urgent decompression/drainage and coordinated ENT-ophthalmology management rather than prolonged medical observation.",
["Medical therapy alone is no longer adequate once vision is worsening despite treatment.","Correct.","Discharge is unsafe with an evolving vision-threatening postseptal complication.","Waiting for interval imaging risks irreversible optic neuropathy; the clinical change already answers the management question."],
"In orbital sinusitis, serial vision examinations are treatment-monitoring data; worsening vision changes the plan immediately.",
"How would a stable young child with a small medial collection, normal vision, and rapid clinical improvement differ?","overnight_call"),

_c("v152_hn_01",H,"Free-Flap Monitoring / Compromise / Salvage",
"Eight hours after fibula free-flap reconstruction, the skin paddle is swollen and violaceous with brisk dark bleeding on pinprick and a worsening venous Doppler signal. What should the overnight resident do?",
["Document it and reassess on morning rounds","Apply tight external pressure to reduce swelling","Treat suspected venous congestion as a flap emergency: remove external constriction if present, call the reconstructive team immediately, and prepare for urgent exploration when compromise is suspected","Start diuresis and wait for the color to normalize"],2,
"A congested, violaceous flap with dark brisk bleeding suggests impaired venous outflow. Mechanical causes such as pedicle kinking, compression, or venous thrombosis are time sensitive; bedside correction of obvious external compression should not delay immediate senior notification and operative salvage when indicated.",
["Flap salvage probability falls with delay; morning reassessment is inappropriate for evolving vascular compromise.","Blind tight pressure can worsen venous outflow and pedicle compression.","Correct.","Diuresis does not correct a thrombosed, kinked, or compressed venous pedicle."],
"Pale/cool suggests inflow failure; blue/swollen with dark brisk pinprick bleeding suggests venous congestion. Both are urgent.",
"The implantable Doppler is still audible but the clinical exam is clearly worsening—what should drive the decision?","postoperative_call"),

_c("v152_tps_01",T,"Recurrent Laryngeal Nerve Injury During Thyroidectomy",
"During planned total thyroidectomy, the first lobe is removed and the vagus/RLN loses signal despite troubleshooting. The nerve appears anatomically intact. The contralateral lobe is not oncologically urgent. What is the safest operative strategy?",
["Proceed immediately with the second side because the nerve looks intact","Stage the contralateral thyroidectomy after recovery/assessment rather than risk bilateral vocal-fold paralysis","Transect the intact nerve to inspect it","Perform prophylactic tracheostomy and always complete both sides"],1,
"A true loss of signal after first-side dissection raises concern for functional RLN injury even when the nerve is visually intact. When oncologically acceptable, staging the contralateral side avoids converting a unilateral neuropraxia into bilateral vocal-fold immobility and a major airway problem.",
["Visual continuity does not prove preserved function after a true loss-of-signal event.","Correct.","Intentional nerve transection creates injury rather than diagnosing it.","Prophylactic tracheostomy is not a substitute for avoiding preventable bilateral nerve injury when completion can safely be staged."],
"Intraoperative monitoring is most valuable when it changes behavior; first-side loss of signal should trigger a bilateral-airway risk calculation.",
"What troubleshooting steps should occur before declaring the signal truly lost?","OR_prep"),

_c("v152_ped_01",P,"Tracheomalacia / Bronchomalacia",
"An infant with known severe tracheomalacia has recurrent cyanotic spells and suddenly deteriorates on the ward with marked expiratory collapse despite positioning and oxygen. What is the immediate management priority?",
["Treat this as dynamic airway failure, call airway/ICU help, provide positive-pressure support as needed, and escalate to definitive airway stabilization based on physiology","Wait for the child to outgrow it during the current cyanotic episode","Give cough suppressant and discharge","Schedule an elective hearing test before addressing breathing"],0,
"Severe tracheobronchomalacia can produce life-threatening dynamic airway collapse. Acute management prioritizes oxygenation and pneumatic stenting with positive pressure when needed; recurrent severe events then drive evaluation for procedures such as tracheopexy/aortopexy or other cause-directed intervention.",
["Correct.","Many mild cases improve with growth, but active cyanotic airway failure cannot be managed by observation alone.","Suppressing cough neither stabilizes the collapsing airway nor makes discharge safe after a severe event.","Hearing evaluation does not address the immediate respiratory threat."],
"Operate on physiologic consequences—not the bronchoscopy image—but cyanotic spells are exactly the consequence that moves severe malacia out of simple observation.",
"Bronchoscopy shows dominant anterior vascular compression. Which operative concept becomes particularly relevant?","overnight_call"),

_c("v152_lar_01",L,"Tracheobronchial Endoscopy Principles",
"During rigid bronchoscopy for a right mainstem foreign body, the object fragments and a piece migrates distally. Saturation falls, chest excursion becomes asymmetric, and ventilation through the bronchoscope is poor. What should happen first?",
["Continue repeated blind forceps passes until the fragment is found","Stop extraction attempts, restore effective ventilation/oxygenation with anesthesia, then re-establish visualization and a controlled retrieval plan","Remove the bronchoscope and leave the child apneic","Abandon the airway and obtain CT before doing anything else"],1,
"Rigid bronchoscopy is shared-airway surgery. When ventilation is lost, oxygenation and a patent ventilating pathway take priority over continued extraction. Once stabilized, controlled visualization and retrieval can resume while assessing for obstruction, bleeding, bronchospasm, or pneumothorax.",
["Blind passes can push fragments farther distally, traumatize the airway, and prolong hypoxemia.","Correct.","Removing the ventilating airway without an alternative worsens the emergency.","Imaging cannot precede stabilization in an actively hypoxemic child with a known intrabronchial problem."],
"The foreign body matters; ventilation matters first.",
"After removal, unilateral breath sounds remain diminished with rising airway pressures. What complication must be excluded immediately?","OR_prep"),

_c("v152_fp_01",F,"Mandibular Biomechanics and Occlusion",
"During ORIF of a mandibular angle fracture, the plates look well seated but after releasing maxillomandibular fixation the patient has a new open bite that was not present preinjury. What is the best response before leaving the OR?",
["Accept the bite because radiographic plate position matters more than occlusion","Re-establish the intended occlusion and reassess reduction/condylar seating and fixation before closure","Plan orthodontics months later without checking the reduction","Extract normal opposing teeth to make the bite fit"],1,
"Premorbid occlusion is a key functional reduction endpoint. A new malocclusion after fixation should prompt reassessment for malreduction, condylar malposition, fracture gap, or fixation error before the opportunity for immediate correction is lost.",
["A technically neat plate does not compensate for a functionally malreduced mandible.","Correct.","Deferring a correctable intraoperative malreduction creates a harder secondary deformity problem.","Removing healthy teeth masks rather than corrects the underlying reduction error."],
"In mandibular fixation, the bite is part of the reduction—not merely a postoperative cosmetic detail.",
"How does an edentulous patient change your intraoperative reference for mandibular position?","OR_prep"),

_c("v152_sleep_01",S,"Positional OSA",
"A patient with mild overall OSA has a supine AHI of 32 but a nonsupine AHI of 3. He cannot tolerate CPAP and asks whether multilevel airway surgery is his only option. What is the best next management principle?",
["Offer phenotype-directed positional therapy as a reasonable treatment option while addressing weight and other contributors, with follow-up to confirm efficacy","Recommend multilevel surgery solely because the supine AHI is severe","Tell him position has no relevance to OSA","Prescribe oxygen as definitive treatment for upper-airway collapse"],0,
"The marked position dependence identifies a positional OSA phenotype. In an appropriately selected patient with low nonsupine disease burden, positional therapy can be a rational primary or adjunctive treatment and should be assessed for adherence and objective efficacy before escalating automatically to surgery.",
["Correct.","The severe supine value should not be interpreted without the very low nonsupine AHI; phenotype changes the treatment options.","Body position can substantially alter retropalatal and retrolingual collapsibility in positional OSA.","Supplemental oxygen does not reliably correct the obstructive mechanics and is not a substitute for treating upper-airway collapse."],
"Read the position-specific PSG, not just the overall AHI.",
"If the nonsupine AHI were also 25, how would that change the value of positional therapy?","boards"),

_c("v152_gen_01",G,"ENT Fluids / Electrolytes / Nutrition",
"A profoundly malnourished head-and-neck cancer patient is started on tube feeds. Twelve hours later phosphate falls sharply and the patient develops weakness, tachycardia, and ectopy. What is the best immediate response?",
["Increase calories rapidly to overcome the malnutrition","Recognize refeeding syndrome risk: slow/hold caloric advancement as clinically appropriate, urgently replace phosphate and other deficits, give thiamine, and monitor cardiopulmonary status closely","Stop checking electrolytes because the changes are expected","Treat only with IV fluid bolus regardless of phosphate"],1,
"Refeeding drives insulin-mediated intracellular shifts of phosphate, potassium, and magnesium and increases thiamine demand. Symptomatic hypophosphatemia with cardiac findings requires prompt electrolyte correction, thiamine, monitored care, and controlled nutritional advancement.",
["More aggressive calories can intensify the electrolyte shift and worsen cardiopulmonary instability.","Correct.","Expected physiology is not benign physiology; severe electrolyte shifts can cause arrhythmia, respiratory failure, and neurologic complications.","Volume alone does not correct the defining phosphate and micronutrient derangements."],
"The danger in refeeding is not feeding itself—it is restarting metabolism faster than depleted electrolyte stores can support it.",
"Which baseline features should make you institute prophylactic thiamine and close phosphate/magnesium/potassium monitoring before the first feed?","overnight_call"),
]
