"""v20.31 evidence hardening for cleft/craniofacial otologic-airway care."""
import concept_check_depth_v231 as _base

QIDS = _base.QIDS
CID = _base.CID
TOPIC = _base.TOPIC
COHORT = _base.COHORT
_q = COHORT[QIDS[0]]

answer = str(_q.get("answer_text") or "")
update = (
    "\n\n**2026 evidence boundary: anatomy does not guarantee surgical physiology.** "
    "The tensor veli palatini remains central to normal Eustachian-tube opening, but a 2026 randomized trial of 81 nonsyndromic children undergoing Furlow palatoplasty found that adding tensor veli palatini tenopexy did not reduce OME from ages 2-7 years or reduce subsequent ear procedures. The teaching point is to understand the tensor/ET mechanism without assuming that surgically altering the tensor reliably normalizes middle-ear disease. Otologic surveillance remains necessary after palate repair."
)
if "pmid 41930721" not in answer.lower():
    answer += update
_q["answer_text"] = answer

refs = list(_q.get("source_refs_v231") or [])
reftext = " ".join(str(x.get("citation") or "") for x in refs if isinstance(x, dict)).lower()
if "pmid 41930721" not in reftext:
    refs.append({"type":"randomized_trial","citation":"Alper CM et al. Tensor Veli Palatini Muscle Tenopexy During Furlow Palatoplasty. Cleft Palate Craniofac J. 2026 Apr 3. PMID 41930721; DOI 10.1177/10556656261438891. Randomized trial of 81 nonsyndromic children; added tensor tenopexy did not reduce OME from ages 2-7 years. Used to separate durable tensor/ET anatomy from assumed otologic benefit."})
if "pmid 42213516" not in reftext:
    refs.append({"type":"peer_reviewed","citation":"Bachini S et al. Hearing and Otologic Outcomes After Routine Versus Selective Ventilation Tube Insertions in Children With Cleft Palate. Cleft Palate Craniofac J. 2026 May 29. PMID 42213516; DOI 10.1177/10556656261450120. Forty-one children; no significant differences in re-tympanostomy, hearing outcomes, or surgical complications between routine and selective VTI over two years; not treated as a universal mandate."})
_q["source_refs_v231"] = refs

_q["evidence_distinction_v231"] = (
    "Durable textbook anatomy and operative foundations are preserved. Current management is updated with the 2024 ACPA Parameters/2026 team standards and 2022 AAO-HNSF tube guideline. Universal prophylactic tube timing, exact palatoplasty timing and any one Robin-sequence airway operation remain individualized rather than universal. The 2026 tensor-tenopexy randomized trial (PMID 41930721) prevents anatomy from being over-translated into an assumed otologic benefit, while the 2026 routine-versus-selective VTI cohort (PMID 42213516) refines counseling without establishing a universal tube mandate. New 2026 tube-complication and ETD data further refine counseling but do not replace guideline-based decision-making."
)

apply_concept_check_task_alignment_v231 = _base.apply_concept_check_task_alignment_v231
