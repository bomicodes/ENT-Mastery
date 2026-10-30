"""v50.1: new canonical topic -- Eagle Syndrome (General ENT / Emergencies).

Eagle syndrome (symptomatic elongated styloid process / calcified stylohyoid ligament)
had no home in the curriculum: "styloid" appeared only as the prestyloid/poststyloid
parapharyngeal landmark. This module installs it as a full topic, the same way the
v44.1 batch did, plus the pieces later layers expect every topic to carry:

  * Deep Curriculum entry (recognize / localize / workup / manage / operate / teach,
    tags, source_basis, source_metadata_v408) with the v47 textbook sections
    (overview / physiology / pathophysiology) set directly on the module. The text is
    deliberately NOT added to pathophys_v470/: textbook_xref/ids.py numbers topics by
    sorted position inside each pathophys file, so inserting a topic there would shift
    the reviewer's T-general_ent-<n> citation keys onto the wrong topics.
  * TOPIC_OR_MAP_V470 entry and a new "styloidectomy" OR_PREP_REGISTRY card.
  * Two Concept Checks (free-text Recognize + MCQ Manage), matching v44.1.
  * A three-stage learning ladder (foundation / application / senior_decision,
    ladder_reviewed) so the ladder-inventory gates see a complete topic.
  * Ten board-style vignettes in the v49.0 format, validated with the v49.0 rules
    (clinical_challenge_vignettes_v490.REQUIRED, four choices, int answer, four
    why_wrong entries, live concept_id).
  * Literature references and page-level textbook citations for the "Textbook references"
    panel (install_eagle_refs_v501, called after the v47.2 cross-reference layer). Eagle is
    not keyed in the reviewer CSVs, so its page citations (TEXTBOOK_REFS_V501) are added
    here. The v50.1 cross-reference read K.J. Lee 12e p 12 directly and reused confirmed
    reviewer-CSV pages for the shared anatomy. The Cummings and Pasha PDFs could not be
    text-searched, so no Eagle-specific passage from those books is claimed.

install_eagle_topic_v501 must run before the v47 textbook/Daily Path installers (they
index DEEP_MODULES_V6, the question bank and the OR map at install time).

There is no society clinical practice guideline for Eagle syndrome; the evidence base is
case series, retrospective cohorts and narrative/systematic reviews, and the content says
so where it matters (length threshold, approach choice, vascular-type timing).
"""
from __future__ import annotations

DOMAIN_V501 = "General ENT / Emergencies"
TOPIC_V501 = "Eagle Syndrome"
CONCEPT_ID_V501 = "v6-general-ent-emergencies-eagle-syndrome"
OR_SLUG_V501 = "styloidectomy"
BLIND_CASE_LABEL_V501 = "Chronic one-sided throat and ear pain worse with swallowing and head turning"

SOURCE_BASIS_V501 = [
    "K.J. Lee's Essential Otolaryngology, 12e (2019), Ch 1 Syndromes and Eponyms, p 12 — Eagle syndrome entry (elongated styloid / ossified stylohyoid ligament irritating CN V, VII, IX and X; throat discomfort, foreign-body sensation, dysphagia, facial pain; carotid impingement; surgical shortening).",
    "Cummings Otolaryngology—Head and Neck Surgery, 7e (2021) — prestyloid/poststyloid compartments (Ch 84, p 1177), CN IX referred otalgia (Ch 91, p 1294), Arnold nerve otalgia (Ch 110, p 1680), hypoglossal nerve medial to the posterior digastric and stylohyoid (Ch 119, p 1837). Cummings has no Eagle-specific passage confirmed in this review.",
    "Pasha & Golub, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e (2022), Ch 6 Head and Neck Cancer, p 327 — parapharyngeal space anatomy. No Eagle-specific passage confirmed in this review.",
    "Eagle WW. Elongated styloid process: further observations and a new syndrome. Arch Otolaryngol. 1948;47(5):630-640. doi:10.1001/archotol.1948.00690030654006.",
    "Badhey A, Jategaonkar A, Anglin Kovacs AJ, et al. Eagle syndrome: a comprehensive review. Clin Neurol Neurosurg. 2017;159:34-38. PMID 28527976.",
    "Hassani M, Grønlund EW, Albrechtsen SS, Kondziella D. Neurological phenotypes and treatment outcomes in Eagle syndrome: systematic review and meta-analysis. PeerJ. 2024;12:e17423. doi:10.7717/peerj.17423.",
]

DEEP_ENTRY_V501 = {
    "topic": TOPIC_V501,
    "primary_domain": DOMAIN_V501,
    "overview": (
        "Eagle syndrome is cervicofacial pain or neurovascular symptoms caused by an elongated styloid "
        "process or a calcified (ossified) stylohyoid ligament. It matters because it is a treatable cause "
        "of chronic unilateral throat pain, referred otalgia and dysphagia that is easy to miss, and because "
        "its vascular (stylocarotid) form can cause carotid dissection, transient ischemic attack or stroke. "
        "It is also a diagnosis of exclusion: an elongated styloid is a common incidental finding, so a "
        "persistent unilateral throat pain with otalgia in an adult must not be attributed to the styloid "
        "until pharyngeal and tongue-base malignancy has been excluded."
    ),
    "physiology": (
        "**Embryology**: the styloid process, stylohyoid ligament and lesser cornu of the hyoid all derive "
        "from Reichert cartilage of the second pharyngeal arch, so the complex can ossify along any part of "
        "its length. **Normal anatomy**: the styloid projects anteroinferiorly and medially from the "
        "undersurface of the temporal bone, just anteromedial to the stylomastoid foramen. Normal length is "
        "usually quoted as about 20-30 mm (Eagle's often-cited normal is about 25 mm); a process longer than "
        "about 25-30 mm is commonly called elongated, but the threshold varies between studies and "
        "measurement methods. **Prevalence**: elongation is classically quoted in about 4% of the population, "
        "and only a small minority of those (classically about 4%) have symptoms. These figures are old and "
        "contested, and imaging series report much wider ranges depending on method and cutoff. "
        "**Attachments**: three muscles (styloglossus, CN XII; stylohyoid, CN VII; stylopharyngeus, the only "
        "muscle supplied by CN IX) and two ligaments (stylohyoid to the lesser hyoid cornu; stylomandibular "
        "to the mandibular angle). **Relations**: the styloid and its fascia divide the parapharyngeal space "
        "into prestyloid and poststyloid compartments. The tip lies just lateral to the tonsillar fossa, "
        "with the internal carotid artery medial/posterior and the external carotid artery lateral; the "
        "internal jugular vein lies posterior to the styloid base, against the C1 transverse process. The "
        "facial nerve trunk leaves the stylomastoid foramen posterolateral to the styloid base and crosses "
        "superficial (lateral) to it. The glossopharyngeal nerve curves around the stylopharyngeus to reach "
        "the lower tonsillar bed."
    ),
    "pathophysiology": (
        "**Why it elongates (contested)**: proposed mechanisms include ossification of the stylohyoid "
        "ligament, persistence of ossified Reichert cartilage segments, and reactive ossifying hyperplasia "
        "or metaplasia after trauma such as tonsillectomy. None is proven, and elongation itself is usually "
        "asymptomatic. **Classic type pain**: Eagle attributed post-tonsillectomy pain to scar fibrosis in "
        "the tonsillar fossa stretching or entrapping terminal branches of the trigeminal (V3), facial "
        "(including the chorda tympani), glossopharyngeal and vagal nerves against the styloid tip. CN IX "
        "irritation explains tonsillar fossa pain, odynophagia and referred otalgia through its tympanic "
        "(Jacobson) branch. V3 irritation, including through the stylomandibular ligament near the angle, "
        "explains jaw, preauricular and temporomandibular-region pain. Chorda tympani and lingual nerve "
        "involvement is proposed for tongue pain or taste change. CN X (Arnold) contributes otalgia and "
        "globus. **Vascular (stylocarotid) type**: a long or medially angulated styloid can compress or "
        "repeatedly injure the internal or external carotid artery, often during head rotation. This "
        "irritates the periarterial sympathetic plexus, producing pain along the carotid distribution (ICA: "
        "eye and parietal pain; ECA: face and infraorbital pain). Repeated impact can cause intimal injury "
        "with dissection, pseudoaneurysm, thromboembolism, TIA or stroke, and Horner syndrome if the "
        "sympathetic chain is involved. **Venous variant (emerging, contested)**: compression of the "
        "internal jugular vein between the styloid and the C1 transverse process has been linked to "
        "headache, pulsatile tinnitus and intracranial hypertension in case series."
    ),
    "recognize": (
        "**Classic (stylohyoid) type**: usually an adult in the 30s to 50s. Older series report a female "
        "predominance, but a 2024 meta-analysis of 497 reported patients found about half were women "
        "overall, with the vascular type about 70% male. The classic patient has persistent unilateral dull throat or tonsillar fossa pain, foreign-body sensation, dysphagia "
        "or odynophagia and referred otalgia. Symptoms are worse with swallowing, yawning, tongue movement "
        "or head rotation. Many patients had a tonsillectomy, sometimes years earlier. **Vascular "
        "(stylocarotid) type**: often no tonsillectomy history, with neck pain along the carotid, pain "
        "radiating to the eye or face, and transient neurologic symptoms, presyncope or syncope provoked by "
        "head turning. TIA, stroke or Horner syndrome can be the first presentation. **Exam clue**: a hard, "
        "linear bony prominence palpable in the tonsillar fossa (normally the styloid is not palpable), "
        "which reproduces the patient's pain. Bilateral elongation is common on imaging even when symptoms "
        "are one-sided."
    ),
    "localize": (
        "**Where the pain comes from**: the styloid tip sits lateral to the tonsillar fossa, so pharyngeal "
        "and tonsillar pain with otalgia points to CN IX (tympanic branch) with CN X contributions; jaw-angle "
        "and preauricular pain points to V3 and the stylomandibular ligament; carotid-distribution pain "
        "points to the periarterial sympathetic plexus. **Danger relations**: ICA medial/posterior to the "
        "tip, ECA lateral, IJV posterior to the base, facial nerve trunk at the stylomastoid foramen "
        "superficial to the base, and CN IX, X, XI and XII passing through the poststyloid space. These "
        "relations drive both the vascular symptoms and the operative risk."
    ),
    "workup": (
        "**History and exam first**: full head and neck exam with flexible laryngoscopy and tongue-base "
        "palpation. Persistent unilateral throat pain with otalgia in an adult, especially with weight loss, "
        "dysphagia, smoking or a neck mass, needs malignancy excluded (tonsil, tongue base, hypopharynx, "
        "larynx) with contrast imaging and biopsy of any lesion before the styloid is blamed. **Bedside "
        "tests**: transoral palpation of the styloid tip in the tonsillar fossa that reproduces the pain, "
        "and infiltration of local anesthetic (for example lidocaine) at the tip that temporarily relieves "
        "it. Both support the diagnosis but are not specific. **Imaging**: a panoramic radiograph or "
        "lateral film can show elongation but is a screening view only. Thin-section CT of the neck with 3D "
        "reconstruction is the reference study. It measures length from the temporal bone to the tip, shows "
        "angulation (medial deviation matters for vascular contact) and segmentation, and maps relations to "
        "the carotid arteries and IJV. Langlais radiographic types are I elongated, II pseudoarticulated and "
        "III segmented. **Vascular type**: CT angiography (with head-rotation views when dynamic compression "
        "is suspected) or MRI/MRA for dissection, and urgent neurology/stroke evaluation for any TIA or "
        "stroke. Catheter angiography is reserved for selected cases. **Differential**: glossopharyngeal "
        "neuralgia (paroxysmal lancinating pain triggered by swallowing, responsive to carbamazepine; the "
        "two can coexist), trigeminal neuralgia, TMJ disorder, carotidynia (TIPIC syndrome), spontaneous "
        "cervical artery dissection, myofascial and cervical spine pain, odontogenic pain, hyoid bone "
        "syndrome, Ernest (stylomandibular ligament) syndrome, giant cell arteritis in older patients, "
        "chronic tonsillitis, and oropharyngeal or tongue-base malignancy. **Contested**: length correlates "
        "poorly with symptoms. In one 3D CT study, mean length was 48 mm in Eagle syndrome and about 40 mm in "
        "both glossopharyngeal neuralgia and asymptomatic controls, a nonsignificant difference. The "
        "tip-to-tonsillar-fossa distance was shorter in Eagle syndrome (about 13 mm versus 21-25 mm). A "
        "length number alone never makes the diagnosis."
    ),
    "manage": (
        "**Incidental elongation without symptoms**: no treatment; reassure. **Classic type, mild to "
        "moderate symptoms**: start conservative therapy. Options are analgesics/NSAIDs, neuropathic agents "
        "(gabapentin, pregabalin, a tricyclic such as amitriptyline or nortriptyline, or carbamazepine when "
        "pain is neuralgic) and transoral injection of local anesthetic with corticosteroid into the "
        "tonsillar fossa at the styloid tip. Injection is diagnostic and therapeutic, but relief is often "
        "temporary. Evidence for all medical options is low-level (case series). Historical manual "
        "transpharyngeal fracture of the styloid is not recommended because the fragments and great vessels "
        "are uncontrolled. **Refractory or severe classic type**: partial styloidectomy. In a 2024 "
        "meta-analysis of published cases, surgery improved or resolved symptoms in about 98% of patients "
        "versus about 66% with medical treatment. That evidence is case reports and series with publication "
        "bias. **Vascular type**: treat as a neurovascular problem. Manage dissection with antithrombotic "
        "therapy alongside stroke neurology (antiplatelet versus anticoagulant choice follows cervical "
        "dissection practice), and remove the compressive styloid, usually transcervically. In a 2025 "
        "systematic review of vascular complications, initial styloidectomy cured about 79% with about 3% "
        "recurrence, while medical treatment alone cured about 25% with about 47% recurrence. Carotid "
        "stents left against a persisting styloid have deformed, fractured or fragmented. Some vascular "
        "series stent the ICA first and then remove the styloid. The timing of styloidectomy relative to "
        "the acute dissection, and whether to stent first, are contested and individualized. "
        "**Contested**: K.J. Lee calls surgical shortening the only effective treatment, while "
        "medical-therapy series report benefit in a majority of patients. Also contested are whether a "
        "positive lidocaine test predicts surgical success and how long to persist with medical therapy "
        "before surgery."
    ),
    "operate": (
        "**Goal**: shorten the styloid (partial styloidectomy) and release the attached ligament and "
        "muscles, without dissecting up to the base at the stylomastoid foramen. **Transoral approach**: "
        "through the tonsillar fossa, with tonsillectomy if the tonsil is present. Palpate the tip, incise "
        "the mucosa and constrictor over it, strip periosteum and attachments with an elevator, and resect "
        "with a rongeur as far proximally as can be seen safely. Advantages are no external scar and "
        "shorter operating time. Drawbacks are a narrow, deep field, no proximal vascular control, deep "
        "neck infection risk and incomplete resection. Endoscope- or robot-assisted transoral techniques "
        "improve visualization. It suits a classic-type patient with a tip palpable in the fossa. "
        "**Transcervical approach**: horizontal incision about two fingerbreadths below the mandibular "
        "angle (or a parotidectomy-type incision), subplatysmal flap below the marginal mandibular branch, "
        "retract the submandibular gland anteriorly and the sternocleidomastoid posteriorly, and identify "
        "and retract the posterior belly of digastric. Palpate and dissect along the styloid subperiosteally, "
        "detach muscles and ligament, and resect. Advantages are wide exposure, proximal and distal "
        "vascular control and more complete resection. It is preferred for the vascular type, a long or "
        "medially angulated process, revision, or failed transoral surgery. Drawbacks are the scar, "
        "marginal mandibular weakness and longer stay. **Danger structures**: ECA lateral to the tip; ICA "
        "and IJV medial and posterior; facial nerve trunk at the base; CN IX around stylopharyngeus; CN XII "
        "crossing below; CN X and XI in the poststyloid space. **Complications**: hemorrhage or great-vessel "
        "injury, hematoma, facial nerve weakness (marginal mandibular from the cervical approach; trunk "
        "injury from dissection near the base), hypoglossal, glossopharyngeal or vagal injury (dysphagia, "
        "taste change, hoarseness), parapharyngeal or deep neck infection (especially transoral), trismus, "
        "and persistent or recurrent pain from incomplete resection or a wrong diagnosis. **Contested**: "
        "whether transoral or transcervical gives better long-term relief. Comparative data are small "
        "retrospective series without consistent superiority; for example, one 8-patient series (4 transoral, "
        "4 transcervical) reported similar relief. In pooled case reports, classic cases were mostly operated "
        "transorally and vascular cases mostly transcervically, which confounds any head-to-head comparison."
    ),
    "teach": (
        "Boards/chief framework: unilateral throat pain + otalgia + pain on swallowing or head turning + a "
        "palpable bony tip in the tonsillar fossa = classic Eagle syndrome; the same anatomy with "
        "head-rotation TIA, carotid-distribution pain or dissection = the stylocarotid type. Three "
        "teaching rules: (1) exclude tonsil, tongue-base and hypopharyngeal cancer before blaming an "
        "incidental long styloid; (2) confirm with palpation, local anesthetic infiltration and CT with 3D "
        "reconstruction, remembering that length alone correlates poorly with symptoms and the 25-30 mm "
        "cutoff varies; (3) choose transoral styloidectomy for a classic-type tip palpable in the fossa and "
        "transcervical for vascular, long or medially angulated processes, with the ICA medial, ECA lateral "
        "and facial nerve trunk at the base as the anatomy to recite."
    ),
    "tags": ["Eagle syndrome", "elongated styloid process", "stylohyoid ligament", "stylocarotid syndrome",
             "styloidectomy", "glossopharyngeal neuralgia differential", "referred otalgia",
             "carotid dissection"],
    "source_basis": list(SOURCE_BASIS_V501),
    "source_metadata_v408": {
        "canonical_domain": DOMAIN_V501,
        "canonical_topic": TOPIC_V501,
        "scope": "verified domain/chapter textbook locator; not a claim-level citation. Time-sensitive or numeric claims require the attached topic-specific guideline/source.",
        "locator_level": "domain-foundational",
        "reviewed_after": "v50.1",
    },
    "depth_reviewed_v408": True,
}

LITERATURE_REFS_V501 = [
    "No society clinical practice guideline exists for Eagle syndrome; recommendations rest on case series and reviews.",
    "Eagle WW. Elongated styloid processes: report of two cases. Arch Otolaryngol. 1937;25(5):584-587. doi:10.1001/archotol.1937.00650010656008.",
    "Eagle WW. Elongated styloid process: further observations and a new syndrome. Arch Otolaryngol. 1948;47(5):630-640. doi:10.1001/archotol.1948.00690030654006.",
    "Langlais RP, Miles DA, Van Dis ML. Elongated and mineralized stylohyoid ligament complex: a proposed classification and report of a case of Eagle's syndrome. Oral Surg Oral Med Oral Pathol. 1986;61(5):527-532. doi:10.1016/0030-4220(86)90400-7. PMID 3459129.",
    "Kent DT, Rath TJ, Snyderman C. Conventional and 3-dimensional computerized tomography in Eagle's syndrome, glossopharyngeal neuralgia, and asymptomatic controls. Otolaryngol Head Neck Surg. 2015;153(1):41-47. doi:10.1177/0194599815583047. PMID 25917666.",
    "Raser JM, Mullen MT, Kasner SE, Cucchiara BL, Messé SR. Cervical carotid artery dissection is associated with styloid process length. Neurology. 2011;77:2061-2066. doi:10.1212/WNL.0b013e31823b4729. PMID 22116948.",
    "Müderris T, Bercin S, Sevil E, Beton S, Kırış M. Surgical management of elongated styloid process: intraoral or transcervical? Eur Arch Otorhinolaryngol. 2014;271(6):1709-1713. doi:10.1007/s00405-013-2664-0. PMID 23982667.",
    "Badhey A, Jategaonkar A, Anglin Kovacs AJ, Kadakia S, De Deyn PP, Ducic Y, Schantz S, Shin E. Eagle syndrome: a comprehensive review. Clin Neurol Neurosurg. 2017;159:34-38. PMID 28527976.",
    "Hassani M, Grønlund EW, Albrechtsen SS, Kondziella D. Neurological phenotypes and treatment outcomes in Eagle syndrome: systematic review and meta-analysis. PeerJ. 2024;12:e17423. doi:10.7717/peerj.17423.",
    "Thielen A, Brizzi V, Majoufre C, et al. Eagle syndrome and vascular complications: a systematic review. Int J Oral Maxillofac Surg. 2025;54(1):31-42. doi:10.1016/j.ijom.2024.09.011. PMID 39406633.",
    "Pagano S, Ricciuti V, Mancini F, et al. Eagle syndrome: an updated review. Surg Neurol Int. 2023. doi:10.25259/SNI_666_2023.",
    "Kumono T, Tanaka T, Naito T, Matsuno A. Eagle syndrome as a delayed vascular complication: carotid stent deformation after stenting for high cervical stenosis. Cureus. 2025. doi:10.7759/cureus.85205.",
]

# Page-level textbook citations for the "Textbook references" panel. Eagle is not in
# pathophys_v470/, so it has no reviewer-CSV key; these are added by install_eagle_refs_v501.
#   * K.J. Lee 12e p 12 was read directly in this review (the Eagle syndrome entry).
#   * The others come from the v47.2 reviewer CSVs (textbook_xref/corrections/), whose quoted
#     excerpts support the general anatomy these Eagle sections rely on: compartments, CN IX/X
#     referred otalgia, the hypoglossal course and malignancy presenting with referred otalgia.
TEXTBOOK_REFS_V501 = [
    "Cummings 7e, Ch 84 Benign Neoplasms of the Salivary Glands, p 1177",
    "Cummings 7e, Ch 91 Malignant Neoplasms of the Oral Cavity, p 1294",
    "Cummings 7e, Ch 110 Radiation Therapy for Cancer of the Larynx and Hypopharynx, p 1680",
    "Cummings 7e, Ch 119 Complications of Neck Surgery, p 1837",
    "Pasha & Golub 6e, Ch 6 Head and Neck Cancer, p 327",
    "K.J. Lee 12e, Ch 1 Syndromes and Eponyms, p 12",
    "K.J. Lee 12e, Ch 45 Tumors of the Oral Cavity, Pharynx, and Esophagus, p 826",
]

# --------------------------------------------------------------------------
# Concept Checks (same shape as the v44.1 new-topic checks)
# --------------------------------------------------------------------------
CONCEPT_CHECKS_V501 = [
    {
        "id": "cc-v112-rec-general-ent-emergencies-eagle-syndrome",
        "domain": DOMAIN_V501,
        "topic": TOPIC_V501,
        "choices": [],
        "answer": None,
        "explanation": "This check tests recognition and the confirmatory workup of a symptomatic elongated styloid process.",
        "board_pearl": "Unilateral throat pain and otalgia that worsen with swallowing or head turning, plus a hard bony tip palpable in the tonsillar fossa, suggest Eagle syndrome. Exclude oropharyngeal cancer before blaming the styloid.",
        "curveball": "An elongated styloid is a common incidental CT finding, and length correlates poorly with symptoms.",
        "tier": "Concept check",
        "mode": "Recognize",
        "concept_id": CONCEPT_ID_V501,
        "assessment_class": "recall",
        "graded_discrimination": False,
        "prompt": (
            "A 44-year-old woman who had a tonsillectomy 12 years ago has 8 months of right-sided throat "
            "pain, a foreign-body sensation and right otalgia that worsen when she swallows or turns her "
            "head. Otoscopy is normal. A hard, linear structure is palpable in the right tonsillar fossa and "
            "pressing on it reproduces her pain. What is the likely cause, how would you confirm it, and what "
            "must be excluded first?"
        ),
        "answer_text": (
            "This is the classic (stylohyoid) type of Eagle syndrome: a symptomatic elongated styloid "
            "process or calcified stylohyoid ligament whose tip lies lateral to the tonsillar fossa. Pain and "
            "otalgia come from irritation of CN IX (referred to the ear through Jacobson's nerve), with V3, "
            "chorda tympani and CN X contributions, often in post-tonsillectomy scar. Confirm it with "
            "transoral palpation that reproduces the pain, temporary relief after local anesthetic "
            "infiltration at the tip, and thin-section CT with 3D reconstruction to measure length "
            "(commonly over about 25-30 mm, a variable threshold), angulation, segmentation and relation to "
            "the carotid arteries. Before attributing chronic unilateral throat pain with otalgia to the "
            "styloid, complete a head and neck exam with flexible laryngoscopy and tongue-base palpation to "
            "exclude tonsil, tongue-base or hypopharyngeal malignancy. Also consider glossopharyngeal "
            "neuralgia, TMJ disorder and carotidynia."
        ),
        "recall_source": "Deep Curriculum",
        "curveball_answer": (
            "Ask about head-rotation-provoked presyncope, transient neurologic symptoms or eye/face pain: "
            "these suggest the vascular (stylocarotid) type, which needs CT angiography or MRA for carotid "
            "compression or dissection and urgent neurovascular evaluation, not just pain management."
        ),
        "gapfill_v501": True,
    },
    {
        "id": "cc-v112-mgt-general-ent-emergencies-eagle-syndrome",
        "domain": DOMAIN_V501,
        "topic": TOPIC_V501,
        "stem": (
            "A 38-year-old man presents 2 days after transient left arm weakness and slurred speech that "
            "began while he was turning his head to reverse his car. He has no tonsillectomy history and has "
            "had intermittent right neck pain radiating to the eye. CT angiography shows a 41 mm medially "
            "angulated right styloid process whose tip abuts the cervical internal carotid artery, with a "
            "small intimal flap at that level. Which management plan is most appropriate?"
        ),
        "choices": [
            "Transoral styloidectomy through the tonsillar fossa this week, with no antithrombotic therapy so the field stays dry",
            "Antithrombotic therapy with stroke neurology for the dissection, then transcervical styloidectomy with vascular control to remove the compressive source",
            "Carotid stenting alone, leaving the styloid in place because the dissection is the only treatable lesion",
            "Gabapentin and a transoral steroid-lidocaine injection, with repeat imaging in 6 months",
        ],
        "answer": 1,
        "explanation": (
            "This is the vascular (stylocarotid) type of Eagle syndrome with an ICA dissection and a TIA. "
            "The dissection is managed like any cervical artery dissection, with antithrombotic therapy "
            "under stroke neurology. The compressive styloid is then removed, usually transcervically, "
            "because that approach gives proximal and distal vascular control and better exposure of a long, "
            "medially angulated process. Some vascular series stent the ICA first and then remove the styloid. "
            "Stenting without styloidectomy risks stent deformation or fracture. The exact timing of surgery "
            "relative to the acute dissection is individualized and contested."
        ),
        "why_wrong": [
            "The transoral route gives no vascular control next to an injured ICA, and withholding antithrombotic therapy in a symptomatic dissection increases stroke risk.",
            "Correct.",
            "A stent left against a persisting styloid has been reported to be compressed or to fracture; stenting can be an adjunct but does not remove the cause.",
            "Neuropathic medication and injection treat classic-type pain; they leave a symptomatic dissection and the compressive styloid untreated.",
        ],
        "board_pearl": "Head-rotation TIA plus a long, medially angulated styloid touching the ICA is stylocarotid Eagle syndrome: treat the dissection medically and remove the styloid, usually transcervically.",
        "curveball": "A stent placed against a persisting styloid can be compressed or fracture.",
        "tier": "Concept check",
        "mode": "Manage",
        "concept_id": CONCEPT_ID_V501,
        "assessment_class": "recall",
        "graded_discrimination": False,
        "curveball_answer": (
            "If endovascular treatment is needed for a flow-limiting dissection or pseudoaneurysm, "
            "styloidectomy is still recommended so the stent is not repeatedly compressed by the styloid tip. "
            "Case reports describe stent deformation and fracture when the styloid is left in place."
        ),
        "gapfill_v501": True,
    },
]

# --------------------------------------------------------------------------
# Three-stage learning ladder (same shape as deep_curriculum_ladder_general_ent_v466)
# --------------------------------------------------------------------------
_LADDER_COMMON = {"domain": DOMAIN_V501, "topic": TOPIC_V501, "tier": "Curated learning ladder",
                  "mode": "Vignette", "concept_id": CONCEPT_ID_V501, "ladder_reviewed": True,
                  "_coverage_reviewed_v211": True}

LADDER_V501 = [
    dict(_LADDER_COMMON, **{
        "id": "v501_gent_eagle_fnd",
        "stem": (
            "A 47-year-old woman has 6 months of left throat pain and left otalgia since a tonsillectomy "
            "several years ago. Otoscopy and flexible laryngoscopy are normal. During the oral exam, which "
            "finding most strongly supports a styloid source for her pain?"
        ),
        "choices": [
            "Tenderness over the left temporomandibular joint with clicking on mouth opening",
            "A tender pulsatile neck mass at the carotid bifurcation",
            "A hard, linear prominence palpable in the left tonsillar fossa that reproduces her pain",
            "Pain triggered by light touch of the upper lip lasting a few seconds",
        ],
        "answer": 2,
        "explanation": (
            "The styloid tip is normally not palpable. An elongated process or calcified stylohyoid "
            "ligament can be felt as a hard, linear structure in the tonsillar fossa, and pressing on it "
            "reproduces the patient's pain. That is the key bedside sign of classic Eagle syndrome."
        ),
        "why_wrong": [
            "Joint tenderness and clicking point to a temporomandibular disorder, one of the main mimics.",
            "A pulsatile bifurcation mass suggests a carotid body tumor or carotid aneurysm (carotidynia gives tenderness without a mass); neither points to a styloid source.",
            "Correct.",
            "Brief pain triggered by light touch in V2 territory is trigeminal neuralgia.",
        ],
        "board_pearl": "A palpable, pain-reproducing bony tip in the tonsillar fossa is the bedside sign of classic Eagle syndrome.",
        "curveball": "What simple office test can add support before imaging?",
        "curveball_answer": (
            "Infiltrate local anesthetic (for example lidocaine) at the palpable tip. Temporary relief "
            "supports a styloid source, although the test is not specific. Then obtain CT with 3D "
            "reconstruction."
        ),
        "learning_stage": "foundation",
        "focus": "diagnosis",
    }),
    dict(_LADDER_COMMON, **{
        "id": "v501_gent_eagle_app",
        "stem": (
            "A 39-year-old man has right throat pain and otalgia when swallowing. A bony tip is palpable in "
            "the right tonsillar fossa. Flexible laryngoscopy and tongue-base palpation are normal. Lidocaine "
            "infiltration at the tip abolishes the pain for 2 hours. Which study is best to confirm the "
            "diagnosis and plan treatment?"
        ),
        "choices": [
            "Thin-section CT of the neck with 3D reconstruction of the styloid process",
            "Noncontrast MRI of the brain and internal auditory canals",
            "Neck ultrasound of the submandibular triangle",
            "Panoramic dental radiograph as the definitive study",
        ],
        "answer": 0,
        "explanation": (
            "CT with 3D reconstruction is the reference study. It measures styloid length, shows angulation "
            "and segmentation (Langlais types I-III), and maps the process to the carotid arteries and IJV, "
            "which shapes the approach. A panoramic radiograph can suggest elongation but is a screening "
            "view."
        ),
        "why_wrong": [
            "Correct.",
            "MRI of the brain and IACs images neither calcified ligament nor styloid length well, and is aimed at a retrocochlear question he does not have.",
            "Ultrasound cannot measure the styloid or show its relation to the skull base and carotids.",
            "A panoramic film can show elongation but cannot define angulation or vascular relations well enough to plan surgery.",
        ],
        "board_pearl": "Confirm Eagle syndrome with CT and 3D reconstruction, which shows length, angulation and vascular relations, rather than plain films.",
        "curveball": "Why is a measured length of 32 mm alone not enough to make the diagnosis?",
        "curveball_answer": (
            "Elongation is common in asymptomatic people and length correlates poorly with symptoms. "
            "Commonly used cutoffs of about 25-30 mm vary by study and measurement method. The diagnosis "
            "needs compatible symptoms, a reproducing exam and exclusion of mimics such as malignancy and "
            "glossopharyngeal neuralgia."
        ),
        "learning_stage": "application",
        "focus": "imaging",
    }),
    dict(_LADDER_COMMON, **{
        "id": "v501_gent_eagle_snr",
        "stem": (
            "A 51-year-old woman has classic Eagle syndrome confirmed by exam and CT: a 36 mm left styloid "
            "whose tip is palpable in the tonsillar fossa, with no vascular contact on CT angiography. Pain "
            "persists despite 4 months of pregabalin and two steroid-anesthetic injections. She wants "
            "surgery and would prefer to avoid a neck scar. What is the most appropriate senior-level plan?"
        ),
        "choices": [
            "Transcervical styloidectomy with resection up to the stylomastoid foramen to prevent regrowth",
            "Manual transpharyngeal fracture of the styloid in clinic under local anesthesia",
            "Further medical therapy indefinitely because surgery has no role in classic-type disease",
            "Transoral partial styloidectomy through the tonsillar fossa, counseling on infection, bleeding and conversion to a cervical approach",
        ],
        "answer": 3,
        "explanation": (
            "For refractory classic-type disease with a tip palpable in the fossa and no vascular contact, "
            "transoral partial styloidectomy is reasonable and avoids a scar. Counseling should cover deep "
            "neck infection, bleeding without proximal vascular control, incomplete resection and possible "
            "conversion to a transcervical approach. Comparative evidence between approaches is limited."
        ),
        "why_wrong": [
            "Resecting up to the stylomastoid foramen endangers the facial nerve trunk at the styloid base; partial styloidectomy is the goal.",
            "Manual fracture leaves fragments and nearby great vessels uncontrolled and is no longer recommended.",
            "Partial styloidectomy improves symptoms in most well-selected patients whose disease does not respond to medical therapy.",
            "Correct.",
        ],
        "board_pearl": "Transoral for a palpable classic-type tip; transcervical for vascular, long or medially angulated processes, revision, or failed transoral surgery.",
        "curveball": "What intraoperative finding should prompt conversion to a transcervical approach?",
        "curveball_answer": (
            "Brisk deep bleeding that cannot be controlled under direct vision, a process that cannot be "
            "followed safely toward its base, or unexpected vascular contact all justify converting so the "
            "great vessels can be controlled."
        ),
        "learning_stage": "senior_decision",
        "focus": "OR_prep",
    }),
]

# --------------------------------------------------------------------------
# Ten board-style vignettes in the v49.0 format (vignettes_v490/*.py)
# --------------------------------------------------------------------------
VIGNETTES_V501 = [
    {'topic': TOPIC_V501, 'concept_id': CONCEPT_ID_V501,
     'stem': 'A 46-year-old woman had a tonsillectomy 15 years ago. She now has 9 months of right-sided throat pain, '
             'a sensation of something stuck in the throat, and right ear pain. All are worse with swallowing and '
             'when she turns her head to the left. Otoscopy and flexible laryngoscopy are normal. A firm, linear '
             'bony structure is palpable in the right tonsillar fossa, and pressing on it reproduces her pain. What '
             'is the most likely diagnosis?',
     'choices': ['Classic (stylohyoid) Eagle syndrome',
                 'Glossopharyngeal neuralgia',
                 'Temporomandibular joint disorder',
                 'Carotidynia (TIPIC syndrome)'],
     'answer': 0,
     'explanation': 'An elongated styloid process or calcified stylohyoid ligament projecting toward the tonsillar fossa '
                    'causes classic Eagle syndrome. Its features are unilateral throat pain, foreign-body sensation, '
                    'odynophagia and referred otalgia, worse with swallowing or head rotation, often after '
                    'tonsillectomy. The key sign is a palpable bony tip in the fossa that reproduces the pain. '
                    'Confirm with local anesthetic infiltration and CT with 3D reconstruction after excluding '
                    'malignancy.',
     'why_wrong': ['Correct.',
                   'Glossopharyngeal neuralgia causes seconds-long paroxysms of lancinating pain triggered by swallowing, '
                   'with pain-free intervals and no palpable bony tip.',
                   'TMJ disorders cause preauricular pain with chewing, joint tenderness and clicking, not a palpable '
                   'pain-reproducing structure in the tonsillar fossa.',
                   'Carotidynia causes tenderness over the carotid bifurcation with perivascular inflammation on '
                   'imaging, not tonsillar fossa pain.'],
     'board_pearl': 'Throat pain + otalgia + pain on swallowing or head turning + a palpable bony tip in the tonsillar '
                    'fossa = classic Eagle syndrome.',
     'curveball': 'Her CT shows bilateral styloid elongation but symptoms only on the right. Does this argue against the '
                  'diagnosis?',
     'curveball_answer': 'No. Bilateral elongation is common, and symptoms are often unilateral. The decision rests on '
                         'the symptomatic side, where the exam reproduces the pain, not on imaging symmetry. Elongation '
                         'is also common in asymptomatic people, which is why imaging alone does not make the diagnosis.',
     'learning_stage': 'foundation', 'focus': 'diagnosis'},

    {'topic': TOPIC_V501, 'concept_id': CONCEPT_ID_V501,
     'stem': 'While teaching a junior resident about a patient with an ossified stylohyoid ligament, you review the '
             'embryology of the stylohyoid complex. Which structure develops from the same pharyngeal arch cartilage '
             'as the styloid process and stylohyoid ligament?',
     'choices': ['Greater cornu of the hyoid bone',
                 'Thyroid cartilage lamina',
                 'Lesser cornu of the hyoid bone',
                 'Head of the malleus'],
     'answer': 2,
     'explanation': 'Reichert cartilage of the second pharyngeal arch forms the stapes superstructure, the styloid '
                    'process, the stylohyoid ligament, the lesser cornu and the upper body of the hyoid. Because the '
                    'whole stylohyoid chain is one embryologic unit, ossification can occur anywhere along it. That '
                    'explains elongated, pseudoarticulated and segmented patterns on imaging (Langlais types I-III).',
     'why_wrong': ['The greater cornu and lower hyoid body come from the third arch.',
                   'The thyroid cartilage derives from the fourth arch (the laryngeal cartilages as a group come from the fourth and sixth arches).',
                   'Correct.',
                   'The malleus head and incus body come from Meckel cartilage of the first arch.'],
     'board_pearl': 'Second arch (Reichert): stapes, styloid, stylohyoid ligament, lesser hyoid cornu. Its nerve is CN '
                    'VII, which supplies the stylohyoid muscle.',
     'curveball': 'Which of the three styloid muscles is the only muscle supplied by the glossopharyngeal nerve?',
     'curveball_answer': 'Stylopharyngeus. It derives from the third arch, and CN IX curves around it on its way to the '
                         'tonsillar bed and tongue base. That course is why styloid-region pathology and surgery can '
                         'irritate or injure CN IX. Styloglossus is supplied by CN XII and stylohyoid by CN VII.',
     'learning_stage': 'foundation', 'focus': 'anatomy'},

    {'topic': TOPIC_V501, 'concept_id': CONCEPT_ID_V501,
     'stem': 'A 52-year-old man with an elongated left styloid process has left tonsillar fossa pain and deep left ear '
             'pain. Otoscopy, tympanometry and audiometry are normal. Which nerve most directly explains the referred '
             'otalgia from the tonsillar fossa?',
     'choices': ['Chorda tympani branch of the facial nerve',
                 'Tympanic (Jacobson) branch of the glossopharyngeal nerve',
                 'Great auricular nerve from C2-C3',
                 'Lesser occipital nerve'],
     'answer': 1,
     'explanation': 'CN IX supplies the tonsillar fossa and, through its tympanic (Jacobson) branch, the middle ear '
                    'mucosa. Irritation at the tonsillar fossa is therefore felt in the ear. Eagle attributed classic-type '
                    'pain to scar tissue stretching terminal branches of CN V, VII, IX and X against the styloid tip. '
                    'CN X (Arnold nerve) and V3 can also contribute otalgia, but tonsillar fossa pain referred to the ear '
                    'is the classic CN IX pathway.',
     'why_wrong': ['The chorda tympani carries taste and parasympathetic fibers; it is proposed for tongue symptoms in '
                   'Eagle syndrome but does not carry tonsillar fossa sensation to the ear.',
                   'Correct.',
                   'The great auricular nerve supplies the auricle and skin over the parotid and angle, not the tonsillar '
                   'fossa.',
                   'The lesser occipital nerve supplies the scalp behind the ear and causes occipital neuralgia, not '
                   'pharyngeal referred otalgia.'],
     'board_pearl': 'Throat pain with normal otoscopy and otalgia means look at the pharynx: CN IX through Jacobson nerve '
                    'and CN X through Arnold nerve refer pain to the ear.',
     'curveball': 'The same patient reports burning of the left lateral tongue and altered taste. Which nerve pathway is '
                  'proposed?',
     'curveball_answer': 'Irritation of the lingual nerve and the chorda tympani fibers traveling with it, near the medial '
                         'mandible and stylomandibular ligament, is proposed for lingual pain and taste change. This '
                         'mechanism is hypothesized rather than proven, and new tongue symptoms in a middle-aged man '
                         'still need examination and imaging to exclude a tongue or tongue-base lesion.',
     'learning_stage': 'foundation', 'focus': 'mechanism'},

    {'topic': TOPIC_V501, 'concept_id': CONCEPT_ID_V501,
     'stem': 'A 58-year-old man who smoked for 35 years has 4 months of right throat pain, right otalgia and mild '
             'dysphagia, with a 4 kg weight loss. A dental panoramic radiograph obtained by his dentist shows a 34 mm '
             'right styloid process. He asks whether he needs a styloidectomy. What is the best next step?',
     'choices': ['Book a transoral styloidectomy, since the radiograph shows elongation',
                 'Start gabapentin and reassess in 3 months',
                 'Inject lidocaine and corticosteroid into the right tonsillar fossa',
                 'Complete head and neck exam with flexible laryngoscopy and tongue-base palpation, contrast neck imaging, and biopsy of any lesion'],
     'answer': 3,
     'explanation': 'Persistent unilateral throat pain with referred otalgia, dysphagia and weight loss in a long-term '
                    'smoker is a red-flag pattern for tonsil, tongue-base, hypopharyngeal or laryngeal cancer. An elongated '
                    'styloid is a common incidental finding, so Eagle syndrome is a diagnosis of exclusion. Complete the '
                    'examination, image with contrast and biopsy any lesion before attributing his symptoms to the '
                    'styloid.',
     'why_wrong': ['Operating on an incidental long styloid without excluding malignancy risks delaying a cancer diagnosis.',
                   'Empiric neuropathic therapy delays the cancer workup this red-flag history requires.',
                   'Injection may mask symptoms and does not exclude a mucosal or submucosal malignancy.',
                   'Correct.'],
     'board_pearl': 'Unilateral throat pain + otalgia in an adult is a pharyngeal or laryngeal cancer until proven '
                    'otherwise; an incidental long styloid does not end the workup.',
     'curveball': 'Flexible laryngoscopy is normal but his symptoms persist. Is a normal laryngoscopy enough to exclude a '
                  'tongue-base or tonsil primary?',
     'curveball_answer': 'Not entirely. Small tongue-base and tonsillar crypt cancers can be submucosal, so careful '
                         'bimanual palpation, contrast CT or MRI, and PET-CT or examination under anesthesia with biopsy '
                         'when suspicion remains are used before the pain is labeled styloid in origin.',
     'learning_stage': 'application', 'focus': 'workup'},

    {'topic': TOPIC_V501, 'concept_id': CONCEPT_ID_V501,
     'stem': 'A 41-year-old woman with suspected Eagle syndrome has a palpable bony tip in the left tonsillar fossa. '
             'Malignancy has been excluded. You are planning treatment and need to define the length, angulation and '
             'relation of the process to the great vessels. Which imaging study is most appropriate?',
     'choices': ['Lateral soft-tissue neck radiograph',
                 'Noncontrast MRI of the neck',
                 'Thin-section CT of the neck with 3D reconstruction',
                 'Neck ultrasound with Doppler'],
     'answer': 2,
     'explanation': 'Thin-section CT with 3D reconstruction is the reference study for Eagle syndrome. It measures length '
                    'from the temporal bone to the tip, shows medial or anterior angulation and segmentation (Langlais '
                    'types I-III), and shows the relation to the ICA, ECA and IJV. Add CT angiography when vascular '
                    'symptoms are present.',
     'why_wrong': ['Plain radiographs can suggest elongation but superimpose structures and cannot map vascular relations.',
                   'MRI shows soft tissue well but depicts calcified ligament and cortical bone poorly.',
                   'Correct.',
                   'Ultrasound cannot show the styloid along its length or its skull-base origin.'],
     'board_pearl': 'CT with 3D reconstruction shows length, angulation and vascular relations, which together guide '
                    'diagnosis and approach.',
     'curveball': 'Her styloid measures 27 mm. A colleague says that is too short to be Eagle syndrome. How do you '
                  'respond?',
     'curveball_answer': 'Length thresholds are not fixed. Many studies use about 25 mm and others about 30 mm, '
                         'measurement methods differ, and CT studies show wide overlap between symptomatic and '
                         'asymptomatic people; in one 3D CT study, asymptomatic controls averaged about 40 mm. Angulation '
                         'and the distance from the tip to the tonsillar fossa or vessels can matter as much as length. The diagnosis rests on symptoms, a reproducing exam and exclusion '
                         'of mimics.',
     'learning_stage': 'application', 'focus': 'imaging'},

    {'topic': TOPIC_V501, 'concept_id': CONCEPT_ID_V501,
     'stem': 'A 63-year-old woman has 2 months of right throat and ear pain. She describes 5- to 20-second electric-shock '
             'paroxysms triggered by swallowing cold liquids, yawning and talking, with completely pain-free intervals. '
             'One episode was followed by brief lightheadedness. No bony prominence is palpable in the tonsillar fossa, '
             'and CT shows styloid processes of 22 mm bilaterally. What is the most likely diagnosis?',
     'choices': ['Classic Eagle syndrome',
                 'Glossopharyngeal neuralgia',
                 'Temporomandibular joint disorder',
                 'Carotidynia'],
     'answer': 1,
     'explanation': 'Glossopharyngeal neuralgia causes brief, lancinating paroxysms in the tonsillar fossa, tongue base and '
                    'ear, triggered by swallowing, talking or yawning, with pain-free intervals. Vagal involvement can cause '
                    'bradycardia or syncope. Most cases come from neurovascular compression at the root entry zone, so MRI '
                    'of the posterior fossa is indicated, and carbamazepine or oxcarbazepine is first-line. Eagle syndrome '
                    'is usually a duller, persistent pain with a palpable tip and an elongated process.',
     'why_wrong': ['Classic Eagle pain is usually dull and persistent with a palpable, pain-reproducing tip; her styloids '
                   'are normal length and not palpable.',
                   'Correct.',
                   'TMJ pain is preauricular and related to chewing, with joint tenderness, not swallow-triggered '
                   'electric paroxysms.',
                   'Carotidynia causes continuous tenderness over the carotid bifurcation rather than swallow-triggered '
                   'shocks.'],
     'board_pearl': 'Paroxysmal, electric, swallow-triggered throat and ear pain with pain-free intervals is '
                    'glossopharyngeal neuralgia; dull, persistent pain with a palpable tip is Eagle syndrome.',
     'curveball': 'Can an elongated styloid cause glossopharyngeal neuralgia-type pain?',
     'curveball_answer': 'Yes. An elongated styloid can irritate CN IX and produce neuralgic features, and the two '
                         'conditions can coexist. When CT shows a long process contacting the nerve course and the pain is '
                         'neuralgic, posterior fossa MRI for a vascular loop is still needed. Treatment targets whichever '
                         'compression the workup supports, so the distinction is not always absolute.',
     'learning_stage': 'application', 'focus': 'diagnosis'},

    {'topic': TOPIC_V501, 'concept_id': CONCEPT_ID_V501,
     'stem': 'A 36-year-old woman has 3 months of moderate left throat pain and otalgia. A bony tip is palpable in the left '
             'tonsillar fossa and lidocaine infiltration relieves the pain. CT shows a 33 mm left styloid with no vascular '
             'contact. Malignancy has been excluded. She has no neurologic symptoms. What is the most appropriate initial '
             'management?',
     'choices': ['Immediate transcervical styloidectomy',
                 'Manual transpharyngeal fracture of the styloid under local anesthesia',
                 'Long-term opioid analgesia',
                 'A neuropathic agent such as gabapentin, pregabalin or a tricyclic, with tonsillar fossa steroid-anesthetic injection, and surgical referral if refractory'],
     'answer': 3,
     'explanation': 'Mild to moderate classic-type Eagle syndrome without vascular features is usually treated '
                    'conservatively first. Options are analgesics, neuropathic agents (gabapentin, pregabalin, '
                    'amitriptyline or nortriptyline, or carbamazepine for neuralgic pain) and transoral injection of local '
                    'anesthetic with corticosteroid at the styloid tip. Relief is often temporary and the evidence is '
                    'low-level, so persistent or severe pain leads to partial styloidectomy.',
     'why_wrong': ['Surgery is reserved for refractory or severe symptoms or the vascular type; she has not tried '
                   'conservative therapy.',
                   'Manual fracture leaves fragments and nearby carotid and jugular vessels uncontrolled and is no longer '
                   'recommended.',
                   'Opioids do little for neuropathic pain and carry dependence risk; they are not appropriate long-term '
                   'therapy here.',
                   'Correct.'],
     'board_pearl': 'Classic Eagle syndrome without vascular features: neuropathic agents and steroid-anesthetic injection '
                    'first, partial styloidectomy if refractory.',
     'curveball': 'Does a strong response to the diagnostic lidocaine injection guarantee a good surgical result?',
     'curveball_answer': 'No. A positive injection supports a styloid source, but its predictive value for surgical '
                         'success has not been well established; this remains contested. Counsel that most selected '
                         'patients improve after styloidectomy but some have persistent pain.',
     'learning_stage': 'application', 'focus': 'pharmacology'},

    {'topic': TOPIC_V501, 'concept_id': CONCEPT_ID_V501,
     'stem': 'A 44-year-old man has three episodes of transient right monocular visual loss and left hand numbness, each '
             'triggered by turning his head sharply to the left. He has right neck pain radiating to the eye. CT '
             'angiography with head-rotation views shows a 45 mm medially angulated right styloid whose tip compresses '
             'the cervical ICA during rotation, without dissection. MRI shows no infarct. Stroke neurology has started '
             'antiplatelet therapy. Which surgical plan is most appropriate?',
     'choices': ['Transcervical styloidectomy with exposure and control of the carotid system',
                 'Transoral styloidectomy through the tonsillar fossa',
                 'Carotid stenting alone, leaving the styloid in place',
                 'Observation with a soft collar to limit head rotation'],
     'answer': 0,
     'explanation': 'This is the vascular (stylocarotid) type with dynamic ICA compression causing transient ischemic '
                    'symptoms. The compressive styloid should be removed. A transcervical approach is preferred because it '
                    'gives wide exposure of a long, medially angulated process and proximal and distal control of the ICA, '
                    'ECA and IJV. Antithrombotic therapy is coordinated with stroke neurology.',
     'why_wrong': ['Correct.',
                   'The transoral route has no proximal vascular control and limited reach for a long, medially angulated '
                   'process next to the ICA.',
                   'A stent left against a persisting styloid can be compressed or fracture; it does not remove the cause.',
                   'Recurrent head-rotation TIAs mean ongoing embolic or flow-related stroke risk; observation is not '
                   'adequate.'],
     'board_pearl': 'Head-rotation TIA plus a styloid compressing the ICA: transcervical styloidectomy with vascular '
                    'control.',
     'curveball': 'Which artery lies lateral and which medial to the styloid tip, and why does that matter here?',
     'curveball_answer': 'The ECA usually lies lateral and the ICA medial/posterior to the tip, with the IJV posterior '
                         'to the base. A medially angulated process therefore points at the ICA, which explains '
                         'ICA-territory TIAs and is why exposure and control of the ICA come before the bone is resected.',
     'learning_stage': 'mastery', 'focus': 'surgery'},

    {'topic': TOPIC_V501, 'concept_id': CONCEPT_ID_V501,
     'stem': 'The morning after a right transcervical styloidectomy for a long, segmented styloid that was followed toward '
             'its base, a patient cannot close the right eye, cannot raise the right brow and has a flat right nasolabial '
             'fold and drooping mouth corner. Tongue protrusion and swallowing are normal. What is the most likely '
             'mechanism?',
     'choices': ['Traction on the marginal mandibular branch from the submandibular flap',
                 'Injury to the facial nerve trunk near the stylomastoid foramen during dissection toward the styloid base',
                 'Embolic stroke from ICA manipulation',
                 'Hypoglossal nerve injury where it crosses below the posterior belly of digastric'],
     'answer': 1,
     'explanation': 'Complete ipsilateral facial weakness involving the forehead is a peripheral lesion of the main trunk. '
                    'The trunk leaves the stylomastoid foramen posterolateral to the styloid base and crosses superficial '
                    'to it, so dissection or resection near the base puts it at risk. The goal of styloidectomy is partial '
                    'resection that stops short of the base. Document House-Brackmann grade, protect the eye and plan '
                    'facial nerve follow-up.',
     'why_wrong': ['Marginal mandibular injury weakens only the lower lip depressors and spares the eye and brow.',
                   'Correct.',
                   'A central stroke typically spares the forehead because of bilateral cortical supply to the upper face.',
                   'Hypoglossal injury causes tongue deviation and weakness, which this patient does not have.'],
     'board_pearl': 'Styloidectomy should be partial; the facial nerve trunk lies superficial to the styloid base at the '
                    'stylomastoid foramen.',
     'curveball': 'Which other cranial nerve injuries should be checked after styloidectomy, and how do they present?',
     'curveball_answer': 'CN IX (dysphagia, taste change, reduced gag), CN X (hoarseness or aspiration), CN XI (shoulder '
                         'weakness) and CN XII (tongue deviation). All pass through the poststyloid space or near the '
                         'stylopharyngeus. The marginal mandibular branch is the most common facial branch at risk from the '
                         'cervical incision.',
     'learning_stage': 'mastery', 'focus': 'complication'},

    {'topic': TOPIC_V501, 'concept_id': CONCEPT_ID_V501,
     'stem': 'During a transoral left styloidectomy, after the constrictor is opened and the styloid tip is exposed, brisk '
             'pulsatile bleeding wells up from deep and posterior to the tip as the rongeur is applied. The anesthesia '
             'team reports falling blood pressure. What is the best immediate action?',
     'choices': ['Apply firm packing and pressure in the fossa, secure the airway, call for help and blood, and obtain vascular control through a transcervical exposure or emergency endovascular treatment',
                 'Use deep monopolar cautery blindly in the fossa until the bleeding stops',
                 'Place a hemostatic clip blindly into the depth of the fossa without visualization',
                 'Finish resecting the styloid quickly so the vessel can be seen better'],
     'answer': 0,
     'explanation': 'Pulsatile bleeding deep and posterior to the styloid tip suggests great-vessel injury, most '
                    'concerningly the ICA, with the IJV also posterior. The transoral field has no proximal control, so the '
                    'priorities are tamponade, airway protection and resuscitation, then definitive control by a '
                    'transcervical approach with proximal and distal exposure or by endovascular treatment.',
     'why_wrong': ['Correct.',
                   'Blind deep cautery near the carotid sheath can enlarge the injury and damage the lower cranial nerves.',
                   'Blind clipping risks occluding or tearing the ICA and injuring CN IX, X and XII without controlling the '
                   'bleed.',
                   'Continuing the resection worsens the injury and delays hemorrhage control.'],
     'board_pearl': 'Transoral styloidectomy has no proximal vascular control: pack, protect the airway, resuscitate, then '
                    'get proximal control by neck exploration or endovascular treatment.',
     'curveball': 'How should this risk shape preoperative selection and counseling for the transoral approach?',
     'curveball_answer': 'Review CT or CT angiography for medial angulation or contact with the ICA and choose a '
                         'transcervical approach when the process is long, medially angulated, vascular-type or a '
                         'revision. Counsel transoral candidates about bleeding, deep neck infection, incomplete resection '
                         'and conversion to an open approach.',
     'learning_stage': 'mastery', 'focus': 'complication'},
]

# --------------------------------------------------------------------------
# OR card (same shape as bucket6_data_hygiene_v442.NEW_OR_PREP_ENTRIES_V442)
# --------------------------------------------------------------------------
_OR_SOURCES_V501 = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7th ed. — Ch 84 p 1177 (prestyloid/poststyloid compartments and carotid position); Ch 119 p 1837 (hypoglossal nerve medial to the posterior digastric and stylohyoid).",
    "K. J. Lee's Essential Otolaryngology, 12th ed. — Ch 1 Syndromes and Eponyms, p 12 (Eagle syndrome; surgical shortening of the styloid).",
    "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6th ed. — Ch 6 Head and Neck Cancer, p 327 (parapharyngeal space anatomy).",
    "Müderris T, et al. Surgical management of elongated styloid process: intraoral or transcervical? Eur Arch Otorhinolaryngol. 2014;271(6):1709-1713. doi:10.1007/s00405-013-2664-0.",
    "Badhey A, et al. Eagle syndrome: a comprehensive review. Clin Neurol Neurosurg. 2017;159:34-38. PMID 28527976.",
    "Hassani M, et al. Neurological phenotypes and treatment outcomes in Eagle syndrome: systematic review and meta-analysis. PeerJ. 2024;12:e17423. doi:10.7717/peerj.17423.",
    "Thielen A, et al. Eagle syndrome and vascular complications: a systematic review. Int J Oral Maxillofac Surg. 2025;54(1):31-42. doi:10.1016/j.ijom.2024.09.011.",
]

OR_CARD_V501 = {
    "slug": OR_SLUG_V501,
    "title": "Styloidectomy (Transoral / Transcervical)",
    "domain": DOMAIN_V501,
    "indications": (
        "Classic-type Eagle syndrome with pain that persists despite medical therapy and steroid-anesthetic "
        "injection, after malignancy and mimics have been excluded; or vascular (stylocarotid) Eagle syndrome "
        "with carotid compression, dissection, TIA or stroke attributable to the styloid. Transoral partial "
        "styloidectomy suits a classic-type tip palpable in the tonsillar fossa. Transcervical styloidectomy "
        "is preferred for the vascular type, a long or medially angulated process, revision, or failed "
        "transoral surgery. The choice of approach is contested and based on small series."
    ),
    "setup": [
        "Confirm the diagnosis before booking: compatible symptoms, a pain-reproducing palpable tip, response to "
        "local anesthetic infiltration, exclusion of oropharyngeal, tongue-base and hypopharyngeal malignancy, and "
        "consideration of glossopharyngeal neuralgia, TMJ disorder and carotidynia.",
        "Review thin-section CT with 3D reconstruction for length, angulation, segmentation and the course of the "
        "ICA, ECA and IJV. Obtain CT angiography (with head-rotation views if symptoms are positional) when there "
        "are any vascular symptoms. A medially angulated process pointing at the ICA favors a transcervical approach.",
        "For the vascular type, coordinate antithrombotic management and timing with stroke neurology and, when "
        "dissection or pseudoaneurysm is present, vascular or endovascular colleagues. Type and screen, and have "
        "vascular instruments available.",
        "Transoral: nasotracheal or oral RAE intubation, mouth gag as for tonsillectomy, and a plan for conversion "
        "to a cervical approach. Transcervical: neck extended and turned away, facial nerve monitoring considered, "
        "and the mandibular angle, mastoid tip and sternocleidomastoid marked.",
    ],
    "landmarks": [
        "styloid tip palpable lateral to the tonsillar fossa (transoral) or deep to the posterior belly of digastric (transcervical)",
        "external carotid artery lateral to the styloid tip",
        "internal carotid artery medial and posterior to the styloid tip; internal jugular vein posterior to the base against the C1 transverse process",
        "facial nerve trunk at the stylomastoid foramen, superficial (lateral) to the styloid base",
        "glossopharyngeal nerve curving around the stylopharyngeus toward the tonsillar bed",
        "hypoglossal nerve crossing the carotids below the posterior belly of digastric; marginal mandibular branch in the submandibular flap",
    ],
    "steps": [
        "Transoral: suspend with a mouth gag, perform tonsillectomy if the tonsil is present, and palpate the styloid tip in the fossa.",
        "Transoral: incise the mucosa and superior constrictor directly over the tip, then strip periosteum and the stylohyoid ligament and muscle attachments circumferentially with an elevator.",
        "Transoral: follow the process superiorly under direct (or endoscopic/robotic) vision, resect it with a rongeur as far proximally as can be seen safely, smooth the stump, and close the mucosa.",
        "Transcervical: make a horizontal incision about two fingerbreadths below the mandibular angle, raise a subplatysmal flap deep to the investing fascia to protect the marginal mandibular branch, and retract the submandibular gland anteriorly and sternocleidomastoid posteriorly.",
        "Transcervical: identify and retract the posterior belly of digastric, palpate the styloid, and identify the ECA, ICA, IJV and hypoglossal nerve before dissecting on the bone.",
        "Transcervical: dissect subperiosteally along the styloid, detach the stylohyoid ligament, stylohyoid, styloglossus and stylopharyngeus, and resect with a rongeur, stopping short of the base so the facial nerve trunk is not endangered.",
        "Irrigate, confirm hemostasis with a Valsalva maneuver, consider a drain after cervical exposure, and close in layers.",
    ],
    "danger": [
        "Internal carotid artery (medial/posterior to the tip)",
        "External carotid artery (lateral to the tip)",
        "Internal jugular vein (posterior to the base)",
        "Facial nerve trunk at the stylomastoid foramen; marginal mandibular branch in the cervical flap",
        "Glossopharyngeal, vagus, accessory and hypoglossal nerves in the poststyloid space",
    ],
    "exit_check": [
        "Confirm hemostasis in the fossa or neck and inspect the stump for sharp edges or residual segments that reproduce the palpable tip.",
        "Before extubation, check for oropharyngeal swelling or hematoma that could threaten the airway, and plan a facial nerve check as soon as the patient is awake.",
    ],
    "complications": {
        "early": [
            "Hemorrhage or great-vessel injury (ICA, ECA, IJV), neck or parapharyngeal hematoma with airway compromise.",
            "Facial nerve weakness (marginal mandibular from the cervical approach; trunk from dissection near the base).",
            "Glossopharyngeal, vagal or hypoglossal injury with dysphagia, taste change, hoarseness or tongue weakness.",
            "Parapharyngeal or deep neck infection, especially after the transoral approach.",
        ],
        "late": [
            "Persistent or recurrent pain from incomplete resection, regrowth or ossification, or a wrong diagnosis.",
            "Trismus and scar or contour change; first bite syndrome has been reported after parapharyngeal-space dissection.",
        ],
    },
    "postop": [
        "Monitor the airway and neck for expanding hematoma or oropharyngeal bleeding; treat new stridor, swallowing difficulty or neck swelling as a possible hematoma.",
        "After vascular-type surgery, perform scheduled neurologic checks and continue antithrombotic therapy as agreed with stroke neurology; new focal deficits need urgent vascular imaging.",
        "Examine facial, glossopharyngeal, vagal and hypoglossal function on the first postoperative day and document any deficit.",
        "Transoral: soft diet and analgesia as after tonsillectomy, with return precautions for bleeding, fever, trismus or neck swelling that could signal parapharyngeal infection.",
        "Review symptom response at follow-up; persistent identical pain should prompt CT for a residual segment and reconsideration of the diagnosis.",
    ],
    "attending_followup": [
        ["Which vessels lie lateral and medial to the styloid tip?",
         "The ECA usually lies lateral and the ICA medial/posterior, with the IJV posterior to the base. A medially angulated process points at the ICA, which is why vascular-type disease favors a transcervical approach with vascular control."],
        ["Why stop short of the styloid base?",
         "The facial nerve trunk leaves the stylomastoid foramen posterolateral to the base and crosses superficial to it. The aim is partial styloidectomy that removes the symptomatic segment without dissecting at the foramen."],
        ["When do you choose transoral over transcervical?",
         "Transoral suits a classic-type process whose tip is palpable in the tonsillar fossa without vascular contact; it avoids a scar but has no proximal vascular control. Transcervical is preferred for vascular-type, long or medially angulated processes, revision, or failed transoral surgery. Comparative data are limited."],
    ],
    "linked_topic": TOPIC_V501,
    "status": "v50.1 added",
    "or_family_v190": "headneck",
    "antibiotics": {
        "indicated": "Transoral: indicated (mucosal entry); transcervical: clean, single dose optional",
        "regimen": "For the transoral approach, a single preoperative IV dose covering oral/pharyngeal flora (ampicillin-sulbactam, or clindamycin if penicillin-allergic). For a clean transcervical approach, a single dose covering skin flora (cefazolin) is reasonable but not mandatory.",
        "rationale": "The transoral route opens the pharyngeal mucosa into the parapharyngeal space, so it is clean-contaminated, and deep neck infection is a recognized complication. Reflects general teaching (ASHP/IDSA/SHEA/SIS surgical antibiotic-prophylaxis principles), not a fixed rule -- confirm against current institutional protocol and attending preference.",
    },
    "source_basis": list(_OR_SOURCES_V501),
    "sources": list(_OR_SOURCES_V501),
}


# --------------------------------------------------------------------------
# Installers
# --------------------------------------------------------------------------
def _validated_vignettes():
    """Apply the v49.0 validation rules to the Eagle vignettes and build bank rows."""
    from clinical_challenge_vignettes_v490 import MODE, REQUIRED
    rows, rejected = [], []
    for n, q in enumerate(VIGNETTES_V501, 1):
        qid = "v501-general-ent-eagle-%d" % n
        ok = all(k in q for k in REQUIRED) and len(q["choices"]) == 4 and isinstance(q["answer"], int) \
            and 0 <= q["answer"] < 4 and len(q["why_wrong"]) == 4 and q["concept_id"] == CONCEPT_ID_V501 \
            and q["why_wrong"][q["answer"]] == "Correct."
        if not ok:
            rejected.append(qid)
            continue
        row = {k: q[k] for k in REQUIRED}
        row.update({"id": qid, "domain": DOMAIN_V501, "topic": TOPIC_V501, "tier": "Curated board-style",
                    "mode": MODE.get(q["focus"], "Reasoning"), "authored_v490": True})
        rows.append(row)
    if rejected:
        raise RuntimeError("v50.1 Eagle vignettes failed v49.0 validation: %s" % rejected)
    return rows


def install_eagle_topic_v501(data, app_mod):
    """Install the topic, its questions and its OR card. Run before the v47 installers."""
    import textbook_curriculum_v470

    result = {"topic_added": False, "concept_checks_added": 0, "ladder_added": 0,
              "vignettes_added": 0, "or_card_added": False}

    if app_mod._v6_item_id(DOMAIN_V501, TOPIC_V501) != CONCEPT_ID_V501:
        raise RuntimeError("v50.1 Eagle concept id drifted")

    # ---- Deep Curriculum (mutate the shared dict/list so data and app_mod stay aligned)
    deep = data.DEEP_MODULES_V6
    if not any(m.get("topic") == TOPIC_V501 for mods in deep.values() for m in mods):
        deep.setdefault(DOMAIN_V501, []).append(dict(DEEP_ENTRY_V501, tags=list(DEEP_ENTRY_V501["tags"]),
                                                     source_basis=list(SOURCE_BASIS_V501),
                                                     source_metadata_v408=dict(DEEP_ENTRY_V501["source_metadata_v408"])))
        result["topic_added"] = True
    if getattr(app_mod, "DEEP_MODULES_V6", None) is not deep:
        app_mod.DEEP_MODULES_V6 = deep

    # ---- Curated, diagnosis-neutral blind-case label (v40.2 pattern). Without it the
    # generic keyword bucket ("Swallowing symptoms") collides with existing topics and
    # the v40.3 boot check refuses duplicate blind labels.
    import daily_curriculum_quality_v368
    daily_curriculum_quality_v368.TOPIC_CASE_LABELS.setdefault(TOPIC_V501, BLIND_CASE_LABEL_V501)

    # ---- OR card and curated topic -> OR map (the v47.0 installer validates every slug)
    registry = data.OR_PREP_REGISTRY
    if OR_SLUG_V501 not in registry:
        card = dict(OR_CARD_V501)
        for key in ("setup", "landmarks", "steps", "danger", "exit_check", "postop", "source_basis", "sources"):
            card[key] = list(card[key])
        card["attending_followup"] = [list(p) for p in OR_CARD_V501["attending_followup"]]
        card["complications"] = {k: list(v) for k, v in OR_CARD_V501["complications"].items()}
        card["antibiotics"] = dict(OR_CARD_V501["antibiotics"])
        registry[OR_SLUG_V501] = card
        result["or_card_added"] = True
    if getattr(app_mod, "OR_PREP_REGISTRY", None) is not registry:
        app_mod.OR_PREP_REGISTRY = registry
    textbook_curriculum_v470.TOPIC_OR_MAP_V470.setdefault(TOPIC_V501, [OR_SLUG_V501])

    # ---- Concept Checks (authored MCQ + free-text; no template stem, so v47.1 leaves them alone)
    checks = data.CONCEPT_CHECKS_V112
    have = {q.get("id") for q in checks}
    for entry in CONCEPT_CHECKS_V501:
        if entry["id"] not in have:
            check = dict(entry)
            for key in ("choices", "why_wrong"):
                if key in check:
                    check[key] = list(check[key])
            # Same review metadata the v17.8 all-domain curation layer stamps on every check.
            check.update({"reviewed_all_domains_v178": True,
                          "board_review_standard_v178": "clinical decision-making",
                          "review_basis_v178": list(SOURCE_BASIS_V501),
                          "canonical_topic": TOPIC_V501})
            checks.append(check)
            result["concept_checks_added"] += 1
    by_id = {q["id"]: q for q in checks if q.get("id")}
    data.CONCEPT_CHECK_BY_ID_V112 = by_id
    app_mod.CONCEPT_CHECKS_V112 = checks
    app_mod.CONCEPT_CHECK_BY_ID_V112 = by_id

    # ---- Learning ladder + v49.0-format vignettes into the practice bank
    bank = data.CLINICAL_CHALLENGES_V119
    have = {q.get("id") for q in bank}
    for q in LADDER_V501:
        if q["id"] not in have:
            row = dict(q, choices=list(q["choices"]), why_wrong=list(q["why_wrong"]))
            bank.append(row)
            result["ladder_added"] += 1
    for row in _validated_vignettes():
        if row["id"] not in have:
            bank.append(row)
            result["vignettes_added"] += 1
    if getattr(app_mod, "CLINICAL_CHALLENGES_V119", None) is not bank:
        app_mod.CLINICAL_CHALLENGES_V119 = bank
    for holder in (data, app_mod):
        index = getattr(holder, "CLINICAL_CHALLENGE_BY_ID_V119", None)
        if isinstance(index, dict):
            index.update({q["id"]: q for q in bank if q.get("concept_id") == CONCEPT_ID_V501})

    data.EAGLE_TOPIC_V501 = result
    return result


def install_eagle_refs_v501(data):
    """Add literature references to the v47.2 "Textbook references" panel. Run after v47.2."""
    lit = getattr(data, "LITERATURE_REFS_V472", None)
    if not isinstance(lit, dict):
        raise RuntimeError("v50.1 Eagle refs: v47.2 cross-reference layer has not run")
    lit.setdefault(TOPIC_V501, list(LITERATURE_REFS_V501))
    books = getattr(data, "TEXTBOOK_REFS_V472", None)
    if not isinstance(books, dict):
        raise RuntimeError("v50.1 Eagle refs: v47.2 textbook citations are missing")
    # Mutate the shared dict in place: the textbook_refs_v472 Jinja global closes over it.
    lst = books.setdefault(TOPIC_V501, [])
    for label in TEXTBOOK_REFS_V501:
        if label not in lst:
            lst.append(label)
    return {"literature_refs": len(lit[TOPIC_V501]), "textbook_refs": len(lst)}
