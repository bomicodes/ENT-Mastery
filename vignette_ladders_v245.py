"""v24.5 — Pediatric Otolaryngology deliberate ladder pass 5.

Five exact canonical high-yield topics: pediatric hearing-loss workup, congenital
CMV hearing loss, congenital neck masses, button-battery ingestion, and
microtia/aural atresia. Questions emphasize early developmental intervention,
etiologic decisions, emergency escalation, anatomy, and reconstruction timing.
"""
DOMAIN="Pediatric Otolaryngology"

def _q(qid,topic,stage,stem,choices,answer,explanation,reasons,pearl,curveball,focus="boards"):
    return {"id":qid,"domain":DOMAIN,"topic":topic,"learning_stage":stage,"stem":stem,
            "choices":choices,"answer":answer,"explanation":explanation,"why_wrong":reasons,
            "board_pearl":pearl,"curveball":curveball,"tier":"Curated learning ladder",
            "mode":"Vignette","focus":focus,"ladder_reviewed":True,"_coverage_reviewed_v211":True}

VIGNETTES_V245=[
_q("v245_ped_hl_fnd","Pediatric Hearing Loss Workup","foundation",
"A newborn fails bilateral hearing screening and diagnostic ABR confirms bilateral sensorineural hearing loss. What is the best overall next principle?",
["Start etiologic evaluation and hearing habilitation in parallel without waiting for speech delay","Wait until school age before intervention","Place tympanostomy tubes for every confirmed SNHL","Repeat screening indefinitely before discussing amplification"],0,
"Confirmed congenital SNHL is time-sensitive because auditory access supports language development. Etiologic workup should proceed while amplification/communication services are initiated rather than delaying one for the other.",
["Correct. Diagnostic investigation and habilitation are parallel tracks.","Waiting for visible language delay loses developmental time.","Tubes treat middle-ear ventilation disease, not sensorineural loss.","Diagnostic ABR has already established hearing loss; repeated screening should not postpone care."],
"For infant hearing loss, do not make etiology a prerequisite for intervention.","What early-intervention timing benchmarks are commonly used after newborn screening?"),
_q("v245_ped_hl_app","Pediatric Hearing Loss Workup","application",
"A 5-month-old has bilateral congenital SNHL. CMV testing in the newborn period was negative and there is no obvious syndromic diagnosis. Which workup strategy is most appropriate?",
["Use a structured etiologic pathway including genetics, targeted imaging when it will affect diagnosis/implant planning, ophthalmologic assessment when appropriate, and ongoing audiology while maintaining amplification","Order every laboratory test available before providing hearing aids","Assume the loss is idiopathic and stop evaluation","Obtain temporal-bone CT in every infant regardless of severity or clinical question"],0,
"Modern pediatric SNHL workup is targeted: genetic testing has high diagnostic yield, imaging is selected according to severity and surgical/etiologic questions, and associated-system evaluation is driven by phenotype while hearing access continues.",
["Correct. The workup should answer actionable etiologic and management questions without delaying habilitation.","Broad indiscriminate testing adds burden and can delay useful intervention.","A negative initial history does not exclude genetic or structural causes.","Routine CT exposes infants to radiation and is not required for every hearing-loss phenotype."],
"Ask what each test will change: etiology, prognosis, associated-risk screening, or hearing-device planning.","How would auditory neuropathy physiology change counseling about behavioral thresholds and cochlear implantation?","senior_management"),
_q("v245_ped_hl_snr","Pediatric Hearing Loss Workup","senior_decision",
"A child with severe bilateral SNHL has poor aided speech access despite well-fit hearing aids and intensive therapy. The family is waiting for the complete genetic workup before considering cochlear implantation. What is the best senior-level recommendation?",
["Proceed with timely cochlear-implant candidacy evaluation while the etiologic workup continues, because prolonged auditory deprivation can worsen language opportunity","Delay implantation until every etiologic test returns","Increase hearing-aid output indefinitely despite inadequate aided access","Defer all intervention until the child can complete adult behavioral audiometry"],0,
"Cochlear-implant timing is driven by demonstrated functional access and developmental need, not completion of every etiologic test. Imaging and genetics can inform planning and prognosis but should not create avoidable auditory deprivation.",
["Correct. Candidacy and etiologic investigation can proceed simultaneously.","Completing every diagnostic branch is not worth delaying effective auditory access.","More gain cannot overcome inadequate cochlear speech access and may exceed safe fitting targets.","Infants and young children can be evaluated with age-appropriate objective and behavioral methods."],
"The chief-level question is whether the child has useful aided access now—not whether the chart has a final etiologic label.","What findings such as cochlear nerve deficiency or severe inner-ear malformation would materially change implant counseling?","senior_management"),

_q("v245_ped_cmv_fnd","Congenital CMV Hearing Loss","foundation",
"An infant is being evaluated for possible congenital CMV-associated SNHL. Why does the timing of virologic confirmation matter?",
["CMV must be demonstrated within the congenital diagnostic window to distinguish congenital from later postnatal infection reliably","A positive CMV test at age 2 years always proves congenital infection","CMV causes only hearing loss present at birth","CMV status has no relevance after diagnostic ABR"],0,
"Congenital CMV must be confirmed from appropriately timed neonatal specimens; later positivity cannot reliably distinguish congenital from postnatal acquisition. CMV hearing loss may also be delayed, fluctuating, or progressive.",
["Correct. Timing determines whether infection can be attributed to the congenital period.","Late positivity alone cannot establish congenital timing.","Congenital CMV can produce delayed-onset or progressive SNHL.","Etiology affects surveillance, counseling, and multidisciplinary management."],
"CMV is a classic reason a passed newborn hearing screen does not end surveillance.","How can a stored newborn dried-blood-spot result sometimes contribute when the early testing window was missed?"),
_q("v245_ped_cmv_app","Congenital CMV Hearing Loss","application",
"A newborn has laboratory-confirmed congenital CMV but passes the hearing screen. What counseling is most appropriate?",
["Arrange longitudinal audiologic surveillance because hearing loss can emerge or progress after a normal newborn screen","Discharge from hearing follow-up because the screen was normal","Place prophylactic ear tubes","Assume any later hearing loss must have a different cause"],0,
"Congenital CMV has an important delayed/progressive hearing-loss phenotype. Normal newborn hearing does not eliminate later risk, so serial age-appropriate audiology is required.",
["Correct. Surveillance is necessary even after an initially normal screen.","A normal screen captures one time point, not the future trajectory.","Middle-ear tubes do not prevent CMV-related cochlear injury.","Later SNHL is a recognized manifestation of congenital CMV."],
"In congenital CMV, hearing is a trajectory, not a single screening result.","What developmental or vestibular concerns should broaden follow-up beyond pure-tone thresholds?"),
_q("v245_ped_cmv_snr","Congenital CMV Hearing Loss","senior_decision",
"A child with congenital CMV develops rapidly progressive bilateral SNHL and is losing aided speech access despite optimized hearing aids. What is the best escalation principle?",
["Accelerate cochlear-implant evaluation rather than waiting for thresholds to stabilize, while counseling that CMV-related hearing can continue to evolve","Wait several years for a permanently stable audiogram","Treat the sensorineural loss with tympanostomy tubes","Avoid implantation because CMV is an infectious etiology"],0,
"Progressive CMV-related SNHL can narrow the window for effective hearing-aid benefit. Implant evaluation should respond to functional aided performance and developmental trajectory rather than demanding prolonged threshold stability.",
["Correct. Progressive loss should prompt timely reassessment of auditory access and candidacy.","Waiting for stability can sacrifice language-development opportunity.","Tubes do not treat cochlear CMV injury.","Congenital CMV does not itself preclude cochlear implantation."],
"Escalate based on declining access, not on a requirement that a progressive disease stop progressing first.","How would significant neurodevelopmental comorbidity change outcome counseling without automatically excluding implantation?","senior_management"),

_q("v245_ped_neck_fnd","Congenital Neck Masses","foundation",
"A child has a painless midline neck mass that elevates with swallowing and tongue protrusion. What diagnosis should be presumed until proven otherwise?",
["Thyroglossal duct cyst","Second branchial cleft cyst","Lymphatic malformation","Reactive posterior-triangle node"],0,
"A thyroglossal duct remnant follows the embryologic descent tract from tongue base and classically moves with swallowing or tongue protrusion because of its hyoid relationship.",
["Correct. Midline position and tongue-motion tethering are classic for a thyroglossal duct lesion.","Second branchial lesions are typically lateral along the anterior SCM/carotid-space pathway.","Lymphatic malformations are usually soft and trans-spatial rather than tethered to tongue motion.","Reactive nodes are generally lateral and do not move with tongue protrusion."],
"Pediatric neck masses become easier when you first classify midline versus lateral and cystic versus solid.","What must be confirmed before excision if ultrasound does not show a normal orthotopic thyroid?"),
_q("v245_ped_neck_app","Congenital Neck Masses","application",
"A child presents with a first infected lateral cystic neck mass. Imaging shows a lesion near the carotid bifurcation. What is the best management sequence when the airway is stable?",
["Treat the acute infection first, define the congenital tract/anatomic relationships, then perform definitive excision after inflammation subsides when feasible","Perform blind bedside excision through inflamed tissue","Observe indefinitely because congenital lesions never recur","Aspirate repeatedly as definitive treatment"],0,
"Acute infection distorts planes and increases operative risk. Stabilize/treat infection and drain if source control is needed, then return for definitive excision after anatomy and likely branchial origin are defined.",
["Correct. Control infection before elective tract dissection when the child is stable.","Operating through acute inflammation can obscure carotid and nerve planes and increase incomplete excision.","Congenital epithelial tracts often reinfect if the source remains.","Aspiration may temporize a collection but does not remove the tract."],
"Do not confuse emergency source control with definitive congenital-mass surgery.","How would a recurrent left low-neck infection with pyriform sinus opening change the embryologic diagnosis and operative plan?","OR_prep"),
_q("v245_ped_neck_snr","Congenital Neck Masses","senior_decision",
"A child has a large trans-spatial cystic neck lesion that enlarges during viral illnesses and surrounds rather than displaces multiple structures. There is no acute airway compromise. What is the best senior-level framework?",
["Treat it as a lymphatic-malformation phenotype and choose observation, sclerotherapy, surgery, or combined therapy based on symptoms, macrocystic/microcystic anatomy, airway risk, and morbidity of complete excision","Attempt radical excision of every infiltrated plane regardless of nerve or vessel morbidity","Diagnose a branchial cyst solely because the lesion is cystic","Give repeated antibiotics as definitive therapy without infection"],0,
"Trans-spatial encasement and episodic enlargement favor lymphatic malformation. Treatment is individualized; sclerotherapy is especially useful for many macrocystic lesions, while surgery is selected for accessible symptomatic disease or residual components.",
["Correct. Therapy is driven by lesion architecture, symptoms, and functional risk.","Aggressive pursuit of complete excision can create disproportionate cranial-nerve or vascular morbidity.","Branchial lesions follow more defined embryologic tracts rather than diffuse trans-spatial infiltration.","Antibiotics treat superinfection, not the malformation itself."],
"For congenital neck disease, complete removal is not automatically the best outcome if function is the price.","What airway strategy would you need if rapid intralesional hemorrhage or infection suddenly caused tongue-base or pharyngeal compression?","overnight_call"),

_q("v245_ped_batt_fnd","Button Battery Ingestion","foundation",
"A toddler has a round radiopaque esophageal foreign body with an AP double-ring/halo sign. What is the correct diagnosis and urgency?",
["Esophageal button battery requiring emergent removal","Coin that can routinely wait overnight","Radiopaque food bolus","Benign gastric calcification"],0,
"The double-ring sign is characteristic of a button battery. Esophageal batteries cause rapid hydroxide-mediated liquefactive injury and require emergency removal even when the child initially appears well.",
["Correct. An esophageal button battery is time-critical because tissue injury begins rapidly.","A coin does not have the same electrochemical injury mechanism or double-ring appearance.","Food boluses are not typically a round double-ring radiopaque object.","The object is localized to the esophagus and has classic battery morphology."],
"Button battery in the esophagus means remove now; symptoms and NPO duration do not buy time.","What lateral-radiograph feature can further distinguish a button battery from a coin?","overnight_call"),
_q("v245_ped_batt_app","Button Battery Ingestion","application",
"A 2-year-old swallowed a button battery about one hour ago and can swallow safely while the endoscopy team mobilizes. The battery is confirmed in the esophagus. What is the best immediate plan?",
["Proceed to emergent endoscopic removal; age-appropriate honey may be used as a temporizing mitigation when criteria are met but must never delay extraction","Delay removal until a full fasting interval has elapsed","Give honey and discharge home","Push the battery into the stomach blindly"],0,
"Esophageal battery removal should not be delayed for NPO status. In selected children older than 12 months with recent ingestion, honey can reduce alkaline injury while definitive removal is being organized, but it is not treatment by itself.",
["Correct. Definitive removal remains the priority and mitigation must not delay it.","Fasting rules do not supersede a time-critical caustic esophageal emergency.","Honey cannot neutralize the continuing electrical injury sufficiently to replace removal.","Blind advancement risks perforation and deeper injury."],
"Mitigation buys biology, not time: it never converts an emergency into observation.","Which circumstances make honey inappropriate, including age and inability to swallow safely?","overnight_call"),
_q("v245_ped_batt_snr","Button Battery Ingestion","senior_decision",
"An esophageal button battery is removed after prolonged impaction. Endoscopy shows deep circumferential injury adjacent to the aortic arch. The child is currently stable. What is the best senior-level next step?",
["Treat the post-removal period as high risk: obtain multidisciplinary evaluation and targeted vascular/deep-injury imaging and monitored follow-up because delayed fistula can occur","Discharge immediately because the battery is out","Repeat routine chest radiography only if fever develops","Start oral antibiotics and assume they prevent vascular fistula"],0,
"Severe injury can continue after extraction. Deep esophageal damage near major vessels carries risk of delayed aorto-esophageal fistula, perforation, TE fistula, stricture, and vocal-fold dysfunction; surveillance must match injury severity.",
["Correct. Successful extraction does not end the emergency when deep injury threatens adjacent vessels or airway.","Catastrophic delayed hemorrhage can occur after an initially stable interval.","Plain radiographs do not adequately assess threatened vascular or deep soft-tissue complications.","Antibiotics do not reverse necrosis or eliminate fistula risk."],
"The most dangerous button-battery complication may occur after the foreign body is already gone.","What sentinel bleeding history would require immediate vascular-emergency escalation rather than routine endoscopic follow-up?","senior_management"),

_q("v245_ped_micro_fnd","Microtia / Aural Atresia","foundation",
"A newborn has unilateral microtia with congenital external auditory canal atresia. What is the most important early hearing principle?",
["Establish ear-specific hearing status and ensure the child has reliable access to sound, especially if the opposite ear is abnormal","Wait until cosmetic reconstruction age before obtaining audiology","Assume the inner ear is normal because the pinna is small","Perform canalplasty in the newborn period"],0,
"Microtia/atresia often causes conductive loss, but management begins with diagnostic audiology and assessment of the contralateral ear. Bilateral or functionally significant loss requires prompt hearing-access planning.",
["Correct. Hearing development precedes cosmetic reconstruction decisions.","Waiting years risks missing bilateral or mixed hearing impairment.","External-ear phenotype does not establish cochlear or neural function.","Neonatal canalplasty is not the routine first intervention."],
"Microtia is a hearing-development problem before it is a reconstruction problem.","What syndromic craniofacial findings should prompt broader evaluation?"),
_q("v245_ped_micro_app","Microtia / Aural Atresia","application",
"A school-age child with unilateral complete aural atresia and normal cochlear function is being evaluated for hearing rehabilitation. What information most directly guides whether atresiaplasty is a reasonable option?",
["High-resolution temporal-bone anatomy assessing middle-ear space, ossicles, facial-nerve course, oval/round windows and mastoid pneumatization, integrated with hearing goals","Pinna size alone","A normal brain MRI alone","Age without any anatomic assessment"],0,
"Canal reconstruction succeeds only when the temporal-bone anatomy is favorable. CT-based anatomy, traditionally summarized with systems such as Jahrsdoerfer scoring, helps estimate feasibility and risk, particularly facial-nerve and ossicular relationships.",
["Correct. Surgical candidacy depends on reconstructable anatomy and realistic functional benefit.","Auricular appearance does not reveal middle-ear reconstructability.","Brain MRI does not map the bony canal, ossicles, or facial-nerve course needed for atresiaplasty planning.","Age matters for timing but cannot substitute for anatomy."],
"Atresiaplasty is an anatomy-driven operation, not an automatic consequence of having atresia.","Why should CT timing be coordinated with actual surgical decision-making rather than obtained routinely in infancy?","OR_prep"),
_q("v245_ped_micro_snr","Microtia / Aural Atresia","senior_decision",
"A child with microtia and aural atresia is considering both auricular reconstruction and hearing surgery. Why must the sequence be planned jointly?",
["Canal surgery and auricular reconstruction use overlapping skin, vascular territories and incision planes, so sequencing depends on whether reconstruction is autologous cartilage or alloplastic and on the chosen hearing strategy","The procedures are unrelated and can be scheduled independently","Atresiaplasty must always precede every form of auricular reconstruction","Cosmetic reconstruction should always occur before any hearing rehabilitation"],0,
"Atresiaplasty can compromise tissue needed for auricular reconstruction, while alloplastic and autologous techniques have different sequencing constraints. Bone-conduction devices may provide hearing without canal surgery and also affect implant-site planning.",
["Correct. The reconstruction and hearing plans share anatomy and should be designed together.","Independent planning can jeopardize skin coverage, blood supply, or future incisions.","There is no universal sequence across reconstruction methods and hearing options.","Auditory access should not be deferred merely for cosmetic timing."],
"The chief-level microtia decision is a coordinated lifetime plan for hearing plus auricular reconstruction, not two isolated operations.","How would poor atresiaplasty anatomy shift counseling toward bone-conduction implantation or nonsurgical hearing technology?","senior_management"),
]

def apply_learning_ladders_v245(challenges, concept_id_fn):
    existing={q.get("id") for q in challenges}
    added=[]
    for src in VIGNETTES_V245:
        if src["id"] in existing: continue
        q=dict(src); q["concept_id"]=concept_id_fn(q["domain"],q["topic"])
        challenges.append(q); existing.add(q["id"]); added.append(q["id"])
    return added
