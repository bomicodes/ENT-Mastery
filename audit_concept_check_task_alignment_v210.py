"""v20.10 hard gate for exact-canonical Facial Soft-Tissue Lacerations / Burns depth."""
import re
import runtime_entry
from concept_check_board_repair_v177 import _find_module
from concept_check_depth_v210 import COHORT

QIDS=tuple(COHORT)
SEMANTIC_REQUIREMENTS={
 "preanesthetic_exam":(("before injecting local anesthetic","before local anesthetic"),("facial nerve",)),
 "parotid":(("stensen",),("second molar",),("stent",)),
 "layered_repair":(("layered closure",),("vermilion",),("dead space","tension")),
 "special_structures":(("canalicular",),("cartilage",),("eyelid",)),
 "burn_airway":(("inhalation injury",),("soot","hoarseness","stridor"),("airway",)),
 "burn_referral":(("american burn association",),("deep partial",),("full thickness",),("face",)),
 "failure":(("sialocele",),("new facial weakness",),("dehiscence",)),
}

def _words(s): return len(re.findall(r"\b\w+[\w'-]*\b",str(s or '')))
def _norm(s): return re.sub(r"[^a-z0-9]+"," ",str(s or '').lower()).strip()

def main():
 d=runtime_entry.data; checks=list(d.CONCEPT_CHECKS_V112); by={str(q.get('id') or ''):q for q in checks}; failures=[]
 final_gate=getattr(runtime_entry,'CONCEPT_CHECK_FINAL_CLINICAL_GATE_V179',{}) or {}; align=final_gate.get('task_alignment_v210') or {}
 if align.get('missing'): failures.append('runtime_missing='+','.join(align['missing']))
 if align.get('link_mismatch'): failures.append('runtime_link_mismatch='+','.join(align['link_mismatch']))
 for qid in QIDS:
  q=by.get(qid)
  if not q: failures.append('missing:'+qid); continue
  p=COHORT[qid]; m=_find_module(q,d.DEEP_MODULES_V6,d._v6_item_id); topic=str(m.get('topic') or '') if m else ''; cid=d._v6_item_id(q.get('domain'),topic) if m and q.get('domain') else None
  if topic!=p['canonical_topic']: failures.append('topic:'+qid)
  if cid!=p['concept_id'] or q.get('concept_id')!=cid: failures.append('concept_link:'+qid)
  if not q.get('task_alignment_v210'): failures.append('marker:'+qid)
  if '?' not in str(q.get('prompt') or '') or _words(q.get('prompt'))<55: failures.append('weak_prompt:'+qid)
  if _words(q.get('answer_text'))<650: failures.append('shallow_answer:'+qid)
  if q.get('choices') or q.get('answer') is not None: failures.append('not_free_response:'+qid)
  for field in ('depth_layers_v210','common_traps_v210','deliberate_review_v210','source_refs_v210'):
   if not q.get(field): failures.append('missing_'+field+':'+qid)
  traps=q.get('common_traps_v210') or []
  if len(traps)<10 or len(set(map(str,traps)))<10: failures.append('traps:'+qid)
  refs=q.get('source_refs_v210') or []; cites=' '.join(str(x.get('citation') or '') for x in refs if isinstance(x,dict)).lower()
  for required in ('cummings','pasha','k.j. lee','american burn association','braun'):
   if required not in cites: failures.append('source_'+required+':'+qid)
  answer=_norm(q.get('answer_text'))
  for label,groups in SEMANTIC_REQUIREMENTS.items():
   if not all(any(_norm(term) in answer for term in alternatives) for alternatives in groups): failures.append('semantic_'+label+':'+qid)
 repaired=set(align.get('repaired') or [])
 if repaired!=set(QIDS): failures.append('runtime_repaired_set_mismatch')
 print('V210_TARGETS|'+','.join(QIDS)); print(f'V210_FAILURES|{len(failures)}')
 for f in failures: print('FAIL|'+f)
 if failures: raise SystemExit(1)
 print('PASS: v20.10 facial soft-tissue trauma check has functional anatomy, layered repair, nerve/duct and burn-airway depth')

if __name__=='__main__': main()
