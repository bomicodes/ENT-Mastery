"""v64.0: corrections to main-bank questions found in the Pasha 6e section audit.

Each fix is an exact text replacement on one question, identified by its bank and id
(cc = CONCEPT_CHECKS_V112, challenge = CLINICAL_CHALLENGES_V119). Applied at boot after every
content patch, so the corrected wording shows everywhere the question is used. A fix whose
current text is not found is skipped and reported (never a partial edit).
"""

BANK_FIXES_V640 = [
 {
  "id": "challenge:v11_fprs_05",
  "field": "stem",
  "kind": "full",
  "old": "A 46-year-old woman has 2 years of bilateral nasal obstruction that worsens with exercise and deep breathing and did not improve after septoplasty elsewhere. Endoscopy shows a midline septum and normal inferior turbinates after decongestion. On forced inspiration the lateral nasal wall just above the alar crease draws inward on both sides, and internal support of that area with a cerumen curette (modified Cottle maneuver) markedly improves airflow. Which site best explains her obstruction?",
  "new": "A 46-year-old woman has 2 years of bilateral nasal obstruction that worsens with exercise and deep breathing and did not improve after septoplasty elsewhere. Endoscopy shows a midline septum and normal inferior turbinates after decongestion. Her middle vault is narrow and pinched, with the upper lateral cartilages lying close to the dorsal septum, and on deep inspiration the sidewall collapses inward at the upper lateral cartilage. Lifting the caudal upper lateral cartilage away from the septum with a cerumen curette (modified Cottle maneuver) markedly improves airflow, while supporting the alar lobule does not. Which site best explains her obstruction?"
 },
 {
  "id": "challenge:v11_fprs_05",
  "field": "explanation",
  "kind": "full",
  "old": "The internal nasal valve, bounded by the septum, caudal upper lateral cartilage, inferior turbinate head and nasal floor, is the narrowest part of the airway. With a straight septum and normal decongested turbinates, static causes are largely excluded. Inspiratory collapse of the sidewall above the alar crease reflects weak upper lateral cartilages pulled inward by Bernoulli forces, and targeted internal support that relieves it localizes the problem better than cheek traction. Treatment is valve-directed, such as spreader grafts or lateral wall support, not further septal work.",
  "new": "The internal nasal valve, bounded by the caudal edge of the upper lateral cartilage, the dorsal septum and the head of the inferior turbinate (many texts add the nasal floor), is the narrowest part of the airway. With a straight septum and normal decongested turbinates, static septal and turbinate causes are largely excluded. A narrow middle vault with inspiratory collapse at the upper lateral cartilage, relieved by lifting the upper lateral cartilage away from the septum, localizes the problem to the internal valve. Treatment widens and stiffens the middle vault, for example with spreader grafts or spreader flaps, not further septal work. Collapse of the alar sidewall over weak lateral crura is a different problem, treated with batten or lateral crural strut grafts."
 },
 {
  "id": "challenge:v141_lar_04",
  "field": "explanation",
  "kind": "substring",
  "old": "Surgery also provides tissue for histology if the mucosa looks atypical, given her risk of malignancy.",
  "new": "Surgery also provides tissue for histology if the mucosa looks atypical, given her smoking-related risk of malignancy; Reinke edema itself is not considered premalignant."
 },
 {
  "id": "challenge:v490-laryngology-1-17",
  "field": "explanation",
  "kind": "substring",
  "old": "Prevention relies on high-volume low-pressure cuffs and routine cuff pressure monitoring, typically keeping pressure between about 20 and 30 cm H2O.",
  "new": "Prevention relies on high-volume low-pressure cuffs and routine cuff pressure monitoring. Cuff pressure is usually kept at about 20 to 30 cm H2O, and the tracheostomy clinical consensus statement cited in Pasha advises keeping it below about 25 cm H2O."
 },
 {
  "id": "challenge:v490-rhinology-1-31",
  "field": "explanation",
  "kind": "substring",
  "old": "A paradoxical turbinate curves laterally without pneumatization and can also narrow the middle meatus.",
  "new": "A paradoxical middle turbinate is not pneumatized but is curved the wrong way, with its convexity facing laterally into the middle meatus and its concavity toward the septum, and it can also narrow the middle meatus."
 },
 {
  "id": "challenge:v136_rhi_20",
  "field": "explanation",
  "kind": "substring",
  "old": "Systemic steroids have limited evidence and real toxicity in postviral loss, and zinc has no proven benefit.",
  "new": "Systemic steroids have limited evidence and real toxicity in postviral loss, although some clinicians still offer a short trial (Pasha lists a steroid trial or observation for URI-related loss); zinc has no proven benefit."
 },
 {
  "id": "challenge:v490-rhinology-1-6",
  "field": "explanation",
  "kind": "substring",
  "old": "Many patients continue for about 3 years for durable benefit.",
  "new": "A full course usually runs 3 to 5 years for durable benefit."
 },
 {
  "id": "challenge:v136_rhi_26",
  "field": "explanation",
  "kind": "substring",
  "old": "Safe enlargement proceeds medially and inferiorly from the natural ostium under direct vision, guided by preoperative CT review of pneumatization and septal insertions.",
  "new": "Safe enlargement proceeds medially and inferiorly from the natural ostium under direct vision, guided by preoperative CT review of pneumatization and septal insertions. Inferior enlargement is safe for the optic nerve and carotid but crosses the posterior septal branch of the sphenopalatine artery on the lower sphenoid face, so it can bleed and can divide the pedicle of a future nasoseptal flap; control the vessel, and preserve it if a flap may be needed."
 },
 {
  "id": "challenge:v490-rhinology-2-1",
  "field": "explanation",
  "kind": "substring",
  "old": "Entering at the ostium and enlarging medially and inferiorly keeps instruments away from the lateral sphenoid wall, where the optic nerve and internal carotid artery lie, and away from the skull base superiorly.",
  "new": "Entering at the ostium and enlarging medially and inferiorly keeps instruments away from the lateral sphenoid wall, where the optic nerve and internal carotid artery lie, and away from the skull base superiorly. Taking the opening too far inferiorly, however, reaches the posterior septal branch of the sphenopalatine artery, which bleeds and is the pedicle of the nasoseptal flap."
 },
 {
  "id": "challenge:v137_tps_04",
  "field": "explanation",
  "kind": "substring",
  "old": "Under ATA 2025, lobectomy is an appropriate definitive operation for low-risk tumors up to 2 cm without extrathyroidal extension, nodal disease, or contralateral nodules.",
  "new": "Under the ATA guidelines (the 2015 guideline that Pasha follows, and the 2025 update, which favors lobectomy at least as often), lobectomy is an appropriate definitive operation for low-risk intrathyroidal tumors 1 to 4 cm without extrathyroidal extension, nodal disease, or contralateral nodules."
 },
 {
  "id": "challenge:v137_tps_14",
  "field": "stem",
  "kind": "substring",
  "old": "Ultrasound shows a 4-mm mobile echogenic stone",
  "new": "Ultrasound shows a 3-mm mobile echogenic stone"
 },
 {
  "id": "challenge:v137_tps_14",
  "field": "explanation",
  "kind": "substring",
  "old": "Stones up to about 4 to 5 mm in the submandibular duct can usually be retrieved endoscopically. Larger, fixed, or hilar stones need fragmentation or a combined transoral approach.",
  "new": "Submandibular duct stones smaller than about 4 mm (about 3 mm in the parotid duct) can usually be basket-retrieved endoscopically. Stones of about 5 to 10 mm, and fixed or hilar stones, need laser or mechanical fragmentation or a combined transoral approach."
 },
 {
  "id": "challenge:v116-end-03",
  "field": "stem",
  "kind": "substring",
  "old": "Ultrasound shows a 4-mm mobile echogenic focus",
  "new": "Ultrasound shows a 3-mm mobile echogenic focus"
 },
 {
  "id": "challenge:v116-end-03",
  "field": "explanation",
  "kind": "substring",
  "old": "Small mobile stones of about 4 to 5 mm or less within the submandibular duct are ideal for interventional sialendoscopy.",
  "new": "Small mobile stones smaller than about 4 mm within the submandibular duct (about 3 mm in the parotid duct) are ideal for interventional sialendoscopy."
 },
 {
  "id": "challenge:v143_tps_05",
  "field": "explanation",
  "kind": "substring",
  "old": "Because it is palpable in the mid duct, the best gland-preserving option is transoral removal:",
  "new": "Because it is palpable in the mid duct (palpability, or a stone over about 1 cm, is what makes transoral removal the right choice), the best gland-preserving option is transoral removal:"
 },
 {
  "id": "cc:cc-v112-mgt-general-ent-emergencies-deep-neck-space-infection",
  "field": "explanation",
  "kind": "substring",
  "old": "The retropharyngeal space ends in the upper mediastinum (about T2-T4 depending on the source) where the alar and visceral fascia fuse.",
  "new": "The retropharyngeal space ends in the upper mediastinum, around T1-T2, where the alar and visceral fascia fuse."
 },
 {
  "id": "cc:cc-v112-mgt-head-neck-oncology-head-neck-cancer-surveillance-second-primaries",
  "field": "explanation",
  "kind": "substring",
  "old": "so second primaries arise at about 3-5 percent per year, most often in the lung.",
  "new": "so second primaries arise at roughly 2 to 4 percent per year, most often in the lung."
 },
 {
  "id": "challenge:v490-head-neck-1-65",
  "field": "explanation",
  "kind": "substring",
  "old": "For locoregionally advanced nasopharyngeal carcinoma (stage III-IVA), induction chemotherapy",
  "new": "For locoregionally advanced nasopharyngeal carcinoma (T3-T4 or N2-N3 disease; AJCC 8th edition stage III-IVA excluding T3N0, while under AJCC Version 9, used on this site, this T3N2 tumor is stage II), induction chemotherapy"
 },
 {
  "id": "challenge:v490-head-neck-1-65",
  "field": "explanation",
  "kind": "substring",
  "old": "Radiation alone is reserved for early stage disease.",
  "new": "Radiation alone is reserved for the earliest disease (T1N0, and selected T2N0)."
 },
 {
  "id": "challenge:v431-slnb-oral-cavity-01",
  "field": "explanation",
  "kind": "substring",
  "old": "With depth of invasion over about 4 mm, occult nodal risk",
  "new": "With depth of invasion over 3 mm, occult nodal risk"
 },
 {
  "id": "challenge:v11_hn_03",
  "field": "explanation",
  "kind": "substring",
  "old": "NCCN recommends elective neck dissection when depth exceeds about 4 mm, with clinical judgment between 2 and 4 mm.",
  "new": "Current NCCN guidance recommends elective neck dissection when depth exceeds 3 mm, uses clinical judgment between 2 and 3 mm, and reserves it for highly selected patients below 2 mm (older versions used 4 mm)."
 },
 {
  "id": "challenge:v490-head-neck-2-33",
  "field": "explanation",
  "kind": "substring",
  "old": "NCCN recommends elective neck dissection when depth exceeds about 3 mm.",
  "new": "NCCN recommends elective neck dissection when depth exceeds 3 mm, with clinical judgment between 2 and 3 mm."
 },
 {
  "id": "challenge:v219_hn_hpv_snr",
  "field": "explanation",
  "kind": "substring",
  "old": "Definitive chemoradiation avoids that and is the better recommendation here.",
  "new": "Definitive chemoradiation avoids that and is the better recommendation here. Under AJCC Version 9, this unequivocal imaging ENE (a matted node invading muscle) also raises the node from cN1 to cN2."
 },
 {
  "id": "cc:cc-v112-mgt-otology-neurotology-perilymph-fistula-inner-ear-window-leak",
  "field": "explanation",
  "kind": "full",
  "old": "Forceful Valsalva against a blocked Eustachian tube abruptly raises middle-ear pressure, rupturing the windows inward. Perilymph loss disrupts cochlear and vestibular function.",
  "new": "A sudden rise in middle-ear pressure, for example when a forceful Valsalva abruptly opens the Eustachian tube or ambient pressure changes rapidly, drives the round or oval window inward (implosive rupture). Valsalva against a closed tube instead raises CSF and perilymph pressure through the cochlear aqueduct and blows the window outward (explosive rupture). Perilymph loss disrupts cochlear and vestibular function."
 },
 {
  "id": "challenge:v135_fprs_03",
  "field": "explanation",
  "kind": "substring",
  "old": "native muscle gives the most natural result when reinnervated before end-plate loss, generally within about 18 to 24 months.",
  "new": "native muscle gives the most natural result when reinnervated before end-plate loss, generally within about 12 to 24 months of injury and ideally earlier."
 },
 {
  "id": "challenge:v490-otology-1-97",
  "field": "explanation",
  "kind": "substring",
  "old": "After roughly 18 to 24 months of denervation, the native facial muscles atrophy and fibrose,",
  "new": "Beyond roughly 12 to 24 months of denervation (reinnervation of native muscle is best done earlier), the native facial muscles atrophy and fibrose,"
 },
 {
  "id": "challenge:v458_oto_ramsayhunt_snr",
  "field": "explanation",
  "kind": "substring",
  "old": "is time-sensitive before muscle atrophy, generally within about 1 to 2 years.",
  "new": "is time-sensitive before muscle atrophy, generally within about 12 to 24 months and ideally earlier."
 },
 {
  "id": "challenge:v490-general-ent-1-105",
  "field": "explanation",
  "kind": "substring",
  "old": "A skin graft survives by plasmatic imbibition for the first 24-48 hours, then inosculation",
  "new": "A skin graft survives by plasmatic imbibition for the first 24-48 hours (Pasha describes up to about 72 hours for full-thickness grafts), then inosculation"
 },
 {
  "id": "cc:cc-v112-mgt-pediatric-otolaryngology-laryngomalacia",
  "field": "explanation",
  "kind": "substring",
  "old": "Most laryngomalacia resolves by 12-18 months as laryngeal neuromuscular tone matures.",
  "new": "Most laryngomalacia resolves by 12-18 months, and nearly all by 24 months, as laryngeal neuromuscular tone matures."
 },
 {
  "id": "cc:cc-v112-mgt-pediatric-otolaryngology-pediatric-reflux-eosinophilic-esophagitis",
  "field": "choices",
  "kind": "substring",
  "old": "EoE directly causes subglottic stenosis",
  "new": "EoE contraindicates cartilage grafting"
 },
 {
  "id": "cc:cc-v112-mgt-pediatric-otolaryngology-branchial-cleft-anomalies",
  "field": "explanation",
  "kind": "full",
  "old": "Second branchial cleft tracts pass deep to the second arch structures (external carotid, stylohyoid, digastric) and superficial to the third arch structures (internal carotid, CN IX), ending in the tonsillar fossa.",
  "new": "Second branchial cleft tracts pass deep to the second arch structures (stylohyoid and posterior belly of the digastric) and superficial to the third arch structures (internal carotid artery, CN IX), running between the internal and external carotid arteries and over the hypoglossal nerve to end in the tonsillar fossa."
 },
 {
  "id": "challenge:v146_ped_08",
  "field": "explanation",
  "kind": "substring",
  "old": "A score of about 7 or higher suggests a reasonable candidate, while lower scores favor bone-conduction devices.",
  "new": "A score of 6 or more makes her a candidate (higher scores do better), while lower scores favor bone-conduction devices."
 },
 {
  "id": "challenge:v11_gen_05",
  "field": "explanation",
  "kind": "substring",
  "old": "He needs airway assessment and early upper endoscopy, usually within 12 to 24 hours, to grade the injury.",
  "new": "He needs airway assessment and upper endoscopy to grade the injury, generally within 12 to 48 hours and ideally at about 24 to 48 hours; endoscopy before about 12 hours can underestimate the burn."
 },
 {
  "id": "challenge:v143_gen_01",
  "field": "choices",
  "kind": "substring",
  "old": "Airway assessment, IV fluids, NPO, and endoscopy or CT within 24 hours",
  "new": "Airway assessment, IV fluids, NPO, and endoscopy or CT within 12 to 48 hours"
 },
 {
  "id": "challenge:v143_gen_01",
  "field": "explanation",
  "kind": "substring",
  "old": "esophageal and gastric injury is graded by endoscopy within about 24 hours, or by CT when perforation or transmural necrosis is suspected.",
  "new": "esophageal and gastric injury is graded by endoscopy within 12 to 48 hours (ideally about 24 to 48 hours, since earlier scopes can underestimate the burn), or by CT when perforation or transmural necrosis is suspected."
 },
 {
  "id": "challenge:v11_fprs_04",
  "field": "explanation",
  "kind": "substring",
  "old": "Lateral displacement of this unit causes telecanthus and a rounded canthus, so fixation planning centers on restoring it.",
  "new": "Lateral displacement of this unit causes telecanthus and a rounded canthus, so fixation planning centers on restoring it. Some references, including Pasha, number NOE types differently (by tendon attachment, medial wall comminution and laterality); the Markowitz-Manson scheme used here is the usual board standard."
 },
 {
  "id": "challenge:v431-laryngeal-fracture-02",
  "field": "explanation",
  "kind": "substring",
  "old": "Exposed cartilage, a mucosal tear, vocal fold immobility and a displaced fracture make this a Schaefer-Fuhrman group III injury that requires operative repair.",
  "new": "Exposed cartilage, a mucosal tear, vocal fold immobility and a displaced fracture are indications for operative repair."
 }
]

_FIELDS = {
    "stem": ("stem", "prompt", "question"),
    "explanation": ("explanation", "rationale", "reveal_answer", "answer_text"),
}


def install_bank_fixes_v640(data):
    banks = {"cc": getattr(data, "CONCEPT_CHECKS_V112", None) or [],
             "challenge": getattr(data, "CLINICAL_CHALLENGES_V119", None) or []}
    index = {}
    for prefix, rows in banks.items():
        for q in rows:
            if isinstance(q, dict) and q.get("id") is not None:
                index.setdefault(f"{prefix}:{q['id']}", []).append(q)
    applied, missing = [], []
    for fx in BANK_FIXES_V640:
        hit = False
        for q in index.get(fx["id"], []):
            if fx["field"] == "choices":
                ch = q.get("choices") or []
                for i, c in enumerate(ch):
                    if isinstance(c, str) and fx["old"] in c:
                        ch[i] = c.replace(fx["old"], fx["new"]); hit = True
            else:
                for key in _FIELDS[fx["field"]]:
                    v = q.get(key)
                    if isinstance(v, str) and fx["old"] in v:
                        q[key] = fx["new"] if fx["kind"] == "full" and v == fx["old"] else v.replace(fx["old"], fx["new"])
                        hit = True
                        break
        (applied if hit else missing).append(fx["id"])
    return {"applied": len(applied), "missing": missing}
