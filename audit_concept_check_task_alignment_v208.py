"""v20.8 hard gate for exact-canonical Epistaxis depth and provenance.

This gate intentionally fails production integration until the final clinical gate exposes
``task_alignment_v208``. It also applies the cohort to an isolated copy to validate exact
canonical resolution and the clinical/source contract without mutating production state.
"""
import copy
import re
import runtime_entry
from concept_check_board_repair_v177 import _find_module
from concept_check_depth_v208 import COHORT, apply_concept_check_task_alignment_v208

QIDS=tuple(COHORT)
SEMANTIC_REQUIREMENTS={
 "stabilize":(("airway",),("hemodynamic","hemorrhage","shock")),
 "compression":(("soft cartilaginous","soft nose"),("vasoconstrict",)),
 "anatomy":(("kiesselbach",),("sphenopalatine",),("anterior ethmoid",)),
 "cautery_packing":(("cautery",),("packing",),("resorbable",)),
 "antithrombotic":(("anticoag",),("life threatening","life-threatening"),("first line","first-line")),
 "definitive":(("ligation",),("embolization",),("endoscopy",)),
 "failed_spa":(("missed branch","missed branches","unrecognized spa branch"),("anterior ethmoid","aea")),
 "danger":(("blindness",),("stroke",)),
 "underlying":(("hht",),("tumor",)),
}

def _words(s): return len(re.findall(r"\b\w+[\w'-]*\b",str(s or '')))
def _norm(s): return re.sub(r"[^a-z0-9]+"," ",str(s or '').lower()).strip()

def main():
 d=runtime_entry.data
 failures=[]
 # Validate that the cohort resolves only to the exact live canonical concept.
 isolated=copy.deepcopy(list(d.CONCEPT_CHECKS_V112))
 isolated_result=apply_concept_check_task_alignment_v208(isolated,d.DEEP_MODULES_V6,d._v6_item_id)
 if set(isolated_result.get('repaired') or [])!=set(QIDS): failures.append('isolated_repaired_set_mismatch')
 if isolated_result.get('missing'): failures.append('isolated_missing='+','.join(isolated_result['missing']))
 if isolated_result.get('link_mismatch'): failures.append('isolated_link_mismatch='+','.join(isolated_result['link_mismatch']))
 by={str(q.get('id') or ''):q for q in isolated}
 for qid in QIDS:
  q=by.get(qid)
  if not q: failures.append('missing:'+qid); continue
  p=COHORT[qid]
  m=_find_module(q,d.DEEP_MODULES_V6,d._v6_item_id)
  topic=str(m.get('topic') or '') if m else ''
  cid=d._v6_item_id(q.get('domain'),topic) if m and q.get('domain') else None
  if topic!=p['canonical_topic']: failures.append('topic:'+qid)
  if cid!=p['concept_id'] or q.get('concept_id')!=cid: failures.append('concept_link:'+qid)
  if not q.get('task_alignment_v208'): failures.append('marker:'+qid)
  if '?' not in str(q.get('prompt') or '') or _words(q.get('prompt'))<40: failures.append('weak_prompt:'+qid)
  if _words(q.get('answer_text'))<450: failures.append('shallow_answer:'+qid)
  if q.get('choices') or q.get('answer') is not None: failures.append('not_free_response:'+qid)
  for field in ('depth_layers_v208','common_traps_v208','deliberate_review_v208','source_refs_v208'):
   if not q.get(field): failures.append('missing_'+field+':'+qid)
  traps=q.get('common_traps_v208') or []
  if len(traps)<8 or len(set(map(str,traps)))<8: failures.append('traps:'+qid)
  refs=q.get('source_refs_v208') or []
  cites=' '.join(str(x.get('citation') or '') for x in refs if isinstance(x,dict)).lower()
  for required in ('cummings','pasha','k.j. lee','aaо-hnsf'.replace('о','o'),'2026','hht'):
   if required not in cites: failures.append('source_'+required+':'+qid)
  answer=_norm(q.get('answer_text'))
  for label,groups in SEMANTIC_REQUIREMENTS.items():
   if not all(any(_norm(term) in answer for term in alternatives) for alternatives in groups): failures.append('semantic_'+label+':'+qid)
 # Fail closed until the live final clinical gate actually integrates this cohort.
 final_gate=getattr(runtime_entry,'CONCEPT_CHECK_FINAL_CLINICAL_GATE_V179',{}) or {}
 live_align=final_gate.get('task_alignment_v208') or {}
 if set(live_align.get('repaired') or [])!=set(QIDS): failures.append('runtime_v208_not_integrated')
 print('V208_TARGETS|'+','.join(QIDS)); print(f'V208_FAILURES|{len(failures)}')
 for f in failures: print('FAIL|'+f)
 if failures: raise SystemExit(1)
 print('PASS: v20.8 Epistaxis has exact canonical depth, individualized traps, current guidance and live runtime integration')

if __name__=='__main__': main()
