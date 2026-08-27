"""v23.7 — Thyroid / Parathyroid / Salivary learning-ladder pass 5.

Reviews canonical topics 21-25 from the live inventory: Acute Sialadenitis /
Sjögren, Ranula, Thyroid Eye Disease / Graves Ophthalmopathy, First-Bite
Syndrome, and Frey Syndrome.
"""
DOMAIN="Thyroid / Parathyroid / Salivary"

def _q(qid,topic,stage,stem,choices,answer,explanation,why_wrong,pearl,curveball,focus="boards"):
    return {"id":qid,"domain":DOMAIN,"topic":topic,"learning_stage":stage,"stem":stem,
            "choices":choices,"answer":answer,"explanation":explanation,"why_wrong":why_wrong,
            "board_pearl":pearl,"curveball":curveball,"tier":"Curated learning ladder",
            "mode":"Vignette","focus":focus,"ladder_reviewed":True}

VIGNETTES_V237=[
_q("v237_tps_sialad_fnd","Acute Sialadenitis / Sjögren","foundation",
"An older dehydrated inpatient develops sudden painful parotid swelling, fever, and purulence expressed from Stensen duct. What is the most likely diagnosis?",
["Acute bacterial suppurative sialadenitis","Warthin tumor","Thyroglossal duct cyst","Graves disease"],0,
"Acute bacterial sialadenitis is favored by salivary stasis from dehydration, poor oral intake, medications, or obstruction. Tender gland swelling with purulent ductal drainage is classic, with Staphylococcus aureus among common pathogens.",
["Correct. The acute inflammatory syndrome plus ductal pus localizes bacterial salivary infection.","Warthin tumor is usually a painless parotid mass rather than febrile suppurative disease.","A thyroglossal cyst is a midline neck lesion.","Graves disease does not cause purulent parotid drainage."],
"Tender gland plus pus from the duct is suppurative sialadenitis until proven otherwise.","What findings suggest abscess formation or deep-neck extension requiring imaging and drainage?","overnight_call"),
_q("v237_tps_sialad_app","Acute Sialadenitis / Sjögren","application",
"A patient with acute suppurative parotitis is stable without abscess. What is the best initial management bundle?",
["Hydration, gland massage, sialogogues when safe, oral hygiene, analgesia, and appropriate antistaphylococcal antimicrobial therapy while addressing obstruction or stasis","Immediate total parotidectomy","Steroids alone despite purulence","No treatment because salivary infection is self-limited"],0,
"Treatment reverses salivary stasis and treats infection simultaneously. Hydration, massage, sialogogues, oral care, and antibiotics are typical initial therapy; imaging and drainage are added when abscess, stone, treatment failure, or deep extension is suspected.",
["Correct. Source physiology and bacterial infection both need treatment.","Parotidectomy is excessive for uncomplicated acute infection.","Steroids alone can worsen untreated bacterial infection.","Suppurative disease can progress to abscess or sepsis if neglected."],
"For acute sialadenitis, make saliva move again while treating the infection.","How would a palpable duct stone change source-control planning?"),
_q("v237_tps_sjog_snr","Acute Sialadenitis / Sjögren","senior_decision",
"A patient with Sjögren syndrome has chronic xerostomia and now develops persistent unilateral firm parotid enlargement rather than the usual fluctuating bilateral swelling. What is the best senior-level principle?",
["Assume this is routine autoimmune swelling","Investigate for a focal neoplasm, including salivary lymphoma, rather than attributing persistent asymmetric enlargement automatically to Sjögren disease","Start indefinite antibiotics without imaging","Perform thyroidectomy"],1,
"Sjögren syndrome causes chronic salivary dysfunction and recurrent gland swelling but also increases lymphoma risk. Persistent unilateral enlargement, a discrete mass, adenopathy, or systemic red flags should trigger imaging and tissue evaluation rather than diagnostic anchoring.",
["Persistent asymmetric disease is not the typical benign fluctuation pattern.","Correct. Autoimmune disease does not protect against—and can increase risk of—salivary lymphoproliferative disease.","Antibiotics do not diagnose a chronic focal mass.","Thyroid surgery does not evaluate a parotid lesion."],
"In Sjögren, a new persistent unilateral gland mass deserves a new diagnosis.","Which biopsy strategy best preserves tissue architecture when lymphoma is suspected?"),

_q("v237_tps_ranula_fnd","Ranula","foundation",
"A young adult has a painless fluctuant bluish swelling in the lateral floor of mouth arising from the sublingual region. What is the most likely diagnosis?",
["Simple ranula","Peritonsillar abscess","Parathyroid adenoma","Branchial cleft cyst"],0,
"A ranula is a mucus extravasation phenomenon arising most often from the sublingual gland. A simple ranula remains above the mylohyoid in the oral floor, whereas a plunging ranula extends through or around the mylohyoid into the neck.",
["Correct. The location and translucent cystic phenotype are classic.","A peritonsillar abscess is a painful pharyngeal infection.","Parathyroid adenoma does not present as a blue floor-of-mouth cyst.","Branchial anomalies are typically lateral neck lesions rather than sublingual mucus collections."],
"Simple ranula lives above the mylohyoid; plunging ranula escapes into the neck.","What imaging sign can show continuity between a plunging ranula and the sublingual space?"),
_q("v237_tps_ranula_app","Ranula","application",
"A patient has a recurrent simple ranula after prior aspiration. What treatment principle best addresses the source?",
["Treat the responsible sublingual gland rather than repeatedly aspirating only the mucus collection","Repeat aspiration indefinitely","Excise the submandibular gland routinely","Give radioactive iodine"],0,
"Aspiration or marsupialization alone can recur because the leaking sublingual gland remains. Definitive management often includes removal of the ipsilateral sublingual gland with evacuation or management of the ranula, tailored to size and anatomy.",
["Correct. Source control reduces recurrence.","Repeated aspiration drains the result but leaves the leak source.","The submandibular gland is usually not the source of a ranula.","RAI has no role in a mucus extravasation cyst."],
"A ranula is a gland-leak problem, not merely a cyst-wall problem.","Which nerves and Wharton duct relationships matter during transoral sublingual gland excision?","OR_prep"),
_q("v237_tps_ranula_snr","Ranula","senior_decision",
"A large plunging ranula extends into the upper neck but imaging clearly traces it to the ipsilateral sublingual space. What is the best surgical principle?",
["A transcervical neck excision is always mandatory","Address the ipsilateral sublingual gland, often through a transoral approach, because the cervical component can resolve once the mucus source is controlled; add neck access selectively for anatomy or diagnostic uncertainty","Remove both thyroid lobes","Observe despite progressive airway displacement"],1,
"The driving source is usually the sublingual gland even when most of the collection is cervical. Transoral sublingual gland excision with decompression can control many plunging ranulas and avoids unnecessary cervical dissection, though very large, infected, recurrent, or diagnostically uncertain lesions may require modified access.",
["Cervical size alone does not prove the source is in the neck.","Correct. Treat the source and tailor access to the actual anatomy.","Thyroidectomy is unrelated.","Progressive mass effect may require active treatment."],
"For a plunging ranula, follow the tail back to the sublingual source.","When would a neck approach become reasonable despite a clear sublingual origin?","OR_prep"),

_q("v237_tps_ted_fnd","Thyroid Eye Disease / Graves Ophthalmopathy","foundation",
"Which finding is most characteristic of thyroid eye disease?",
["Extraocular-muscle enlargement with orbital inflammation causing proptosis, lid retraction, exposure, or diplopia","Purulent Wharton-duct drainage","Isolated lower-lip weakness","A mobile parotid-tail mass"],0,
"Thyroid eye disease is an autoimmune orbital process associated most commonly with Graves disease. Expansion of extraocular muscles and orbital fat can cause proptosis, lid retraction, exposure keratopathy, restrictive diplopia, and in severe cases compressive optic neuropathy.",
["Correct. The orbit, not the salivary glands or facial nerve, is the target organ.","Purulent duct drainage indicates salivary infection.","Lower-lip weakness localizes to the marginal mandibular nerve.","A parotid mass is a salivary lesion."],
"Thyroid eye disease is an orbital autoimmune disease; thyroid hormone level alone does not describe its activity or severity.","Which symptoms suggest sight-threatening disease requiring urgent ophthalmologic evaluation?"),
_q("v237_tps_ted_app","Thyroid Eye Disease / Graves Ophthalmopathy","application",
"A patient with active thyroid eye disease has new color desaturation, decreased visual acuity, and an afferent pupillary defect. What is the best next principle?",
["Urgently evaluate and treat possible dysthyroid optic neuropathy rather than managing this as routine cosmetic proptosis","Reassure and recheck in a year","Treat with oral antibiotics only","Perform parotidectomy"],0,
"Visual decline, dyschromatopsia, afferent pupillary defect, or apical crowding can signal compressive optic neuropathy. This is sight-threatening thyroid eye disease and requires urgent specialty treatment, often systemic anti-inflammatory therapy and/or orbital decompression depending on response and severity.",
["Correct. Optic-nerve compromise is an emergency endpoint of TED.","Delay can produce irreversible visual loss.","Antibiotics do not treat autoimmune orbital compression.","Parotid surgery is unrelated."],
"In TED, vision change outranks proptosis—the optic nerve sets the urgency.","How does corneal breakdown create a second sight-threatening pathway?","overnight_call"),
_q("v237_tps_ted_snr","Thyroid Eye Disease / Graves Ophthalmopathy","senior_decision",
"A patient has disfiguring proptosis and diplopia from thyroid eye disease but the orbital inflammation is still active and changing. What is the best senior-level rehabilitative principle?",
["Perform all elective rehabilitative orbital, strabismus, and eyelid surgery immediately","Control active disease first when possible; stage rehabilitative surgery after stability, generally addressing orbital decompression before strabismus and eyelid procedures when those are needed","Ignore disease activity","Use radioactive iodine solely to correct diplopia"],1,
"Rehabilitative surgery is most predictable after the inflammatory phase stabilizes. When multiple operations are required, orbital decompression can alter globe position and extraocular balance, so it generally precedes strabismus and then eyelid refinement.",
["Operating during rapidly changing active disease can make results unpredictable.","Correct. Timing and sequence are part of TED surgical judgment.","Activity strongly affects treatment selection and timing.","Radioiodine does not mechanically correct established restrictive diplopia and can worsen eye disease in susceptible patients."],
"TED rehabilitation has an order because each operation can change the geometry for the next.","When is urgent decompression appropriate even during active disease?"),

_q("v237_tps_firstbite_fnd","First-Bite Syndrome","foundation",
"After parapharyngeal-space surgery, a patient develops severe ipsilateral parotid-region pain with the first bite of each meal that rapidly fades with continued chewing. What is the diagnosis?",
["First-bite syndrome","Frey syndrome","Sialolithiasis","Trigeminal neuralgia"],0,
"First-bite syndrome produces intense parotid-region pain at the first salivary stimulus, then diminishes with subsequent bites. It often follows surgery near the sympathetic chain, deep parotid, or parapharyngeal space and reflects autonomic imbalance affecting myoepithelial contraction.",
["Correct. The first-bite-only temporal pattern is distinctive.","Frey syndrome causes gustatory sweating/flushing rather than pain.","Sialolithiasis typically causes swelling and pain throughout salivary stimulation.","Trigeminal neuralgia causes brief electric facial pain triggered by touch or movement rather than a meal-start parotid pattern."],
"First-bite syndrome is gustatory pain; Frey syndrome is gustatory sweating.","Which operations are most associated with first-bite syndrome?"),
_q("v237_tps_firstbite_app","First-Bite Syndrome","application",
"A patient has persistent disabling first-bite syndrome months after surgery despite observation and conservative analgesia. What treatment can be considered?",
["Botulinum toxin injection into the affected parotid gland","Total thyroidectomy","Long-term IV antibiotics","Carotid ligation"],0,
"Many patients improve over time, but persistent severe symptoms can be treated with intraparotid botulinum toxin to reduce salivary/myoepithelial stimulation. Other neuropathic-pain approaches may be used with variable success.",
["Correct. Botulinum toxin is a useful gland-directed option for refractory symptoms.","Thyroid surgery does not address the mechanism.","There is no bacterial infection to treat.","Carotid ligation is dangerous and unrelated."],
"For refractory first-bite syndrome, reducing parotid secretory drive can reduce the pain trigger.","Why might xerostomia risk influence dose and injection distribution?"),
_q("v237_tps_firstbite_snr","First-Bite Syndrome","senior_decision",
"A patient being counseled before a large poststyloid parapharyngeal tumor resection asks about first-bite syndrome. What is the best attending-level counseling principle?",
["It cannot occur unless the parotid gland is removed","Explain that sympathetic-chain or external-carotid/deep-parotid dissection can produce the syndrome even with an intact gland, and that severity is variable and may improve over time","Promise it is always permanent","State that it causes facial paralysis"],1,
"First-bite syndrome reflects loss of sympathetic input with unopposed parasympathetic stimulation of the parotid myoepithelial system. It can follow upper-neck/parapharyngeal operations without parotidectomy and should be included when the planned dissection threatens those autonomic pathways.",
["The gland can remain anatomically present while autonomic input is altered.","Correct. Risk follows the neural dissection, not simply gland removal.","Symptoms can diminish substantially over months in some patients.","Facial paralysis is a different complication involving CN VII."],
"Counsel first-bite risk from the anatomy you will disturb, not the operation label.","How does preoperative sympathetic dysfunction affect the expected risk?","OR_prep"),

_q("v237_tps_frey_fnd","Frey Syndrome","foundation",
"Months after parotidectomy, a patient develops sweating and flushing over the preauricular skin whenever eating. What is the diagnosis?",
["Frey syndrome","First-bite syndrome","Sjögren syndrome","Horner syndrome"],0,
"Frey syndrome is gustatory sweating and flushing caused by aberrant regeneration of postganglionic parasympathetic fibers to cutaneous sweat glands after parotid-region surgery or trauma.",
["Correct. Gustatory sweating is the hallmark.","First-bite syndrome causes pain rather than sweating.","Sjögren syndrome causes salivary/lacrimal dryness.","Horner syndrome causes ptosis, miosis, and anhidrosis rather than meal-triggered sweating."],
"Frey syndrome is a wiring error after parotid surgery: salivary signals get rerouted to sweat glands.","What bedside test can map gustatory sweating objectively?"),
_q("v237_tps_frey_app","Frey Syndrome","application",
"A patient has socially disabling Frey syndrome after parotidectomy. What is a commonly effective treatment?",
["Intradermal botulinum toxin injection to the symptomatic skin mapped by history or testing","Repeat parotidectomy routinely","Radioactive iodine","Systemic antibiotics"],0,
"Botulinum toxin blocks acetylcholine release at sweat glands and can provide durable symptomatic relief. The treated field can be mapped clinically or with a Minor starch-iodine test, and repeat treatment may be required over time.",
["Correct. Botulinum toxin directly interrupts the aberrant cholinergic sweating response.","Repeat gland surgery adds morbidity without correcting cutaneous aberrant innervation reliably.","RAI has no role.","There is no infection."],
"Frey syndrome is one of the clearest examples of botulinum toxin treating aberrant autonomic signaling.","How does treatment near the oral commissure change injection planning?"),
_q("v237_tps_frey_snr","Frey Syndrome","senior_decision",
"During parotidectomy, what reconstructive principle may reduce clinically significant Frey syndrome in selected patients?",
["Interpose a vascularized or other tissue barrier between the parotid bed and skin when appropriate while balancing contour and flap morbidity","Suture skin directly to exposed facial nerve intentionally","Sacrifice the facial nerve","Avoid closing the incision"],0,
"Interposition techniques such as SMAS, temporoparietal fascia, SCM, or other local tissue can create a barrier between regenerating parasympathetic fibers and cutaneous sweat glands, while also addressing contour. Choice depends on defect, oncologic safety, prior treatment, and donor morbidity.",
["Correct. A barrier can reduce aberrant reinnervation of the skin.","Direct nerve-to-skin contact is not a preventive strategy.","Facial-nerve sacrifice is not justified to prevent a benign autonomic complication.","Leaving the wound open creates unnecessary morbidity."],
"Frey prevention is a reconstruction problem: separate the parotid bed from the skin when the operation and defect justify it.","How does oncologic margin uncertainty affect the choice to place interposition tissue?","OR_prep")]

def apply_learning_ladders_v237(challenges,item_id_fn):
    existing={str(q.get("id")) for q in challenges if q.get("id")}
    added=0
    for q in VIGNETTES_V237:
        if q["id"] in existing: continue
        row=dict(q); row["concept_id"]=item_id_fn(DOMAIN,row["topic"])
        if not row["concept_id"]: raise RuntimeError("v237 orphan: "+row["topic"])
        challenges.append(row); existing.add(row["id"]); added+=1
    return {"added":added,"reviewed_topics":5}
