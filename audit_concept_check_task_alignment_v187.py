"""v18.7 hard gate for the next live-canonical Concept Check depth cohort."""
import json,re
import runtime_entry
from concept_check_board_repair_v177 import _find_module
from concept_check_depth_v187 import COHORT
TASK_TERMS={
"cc-v112-rec-sleep-surgery-oral-appliance-therapy":["objective follow-up sleep testing","maximal tolerable advancement","central apnea","tmj"],
"cc-v112-rec-head-neck-oncology-laryngeal-preservation-decision":["functional larynx","aspiration","pulmonary reserve","total laryngectomy"],
"cc-v112-mgt-laryngology-voice-swallowing-subglottic-tracheal-stenosis":["bronchoscopy","cartilage","diminishing durability","definitive reconstruction"],
"cc-v112-rec-sleep-surgery-dise":["polysomnography","complete concentric collapse","epiglottic","re-localized"],
}
def words(v): return re.findall(r"\b\w+[\w'-]*\b",str(v or ""))
def main():
 d=runtime_entry.data; checks=list(d.CONCEPT_CHECKS_V112); by={str(q.get('id') or ''):q for q in checks}; failures=[]; rows=[]; expected=set(COHORT); rr=getattr(runtime_entry,'CONCEPT_CHECK_FINAL_CLINICAL_GATE_V179',{}); align=rr.get('task_alignment_v187') or {}
 if align.get('missing'): failures.append('runtime_missing='+','.join(align['missing']))
 if align.get('link_mismatch'): failures.append('runtime_link_mismatch='+','.join(align['link_mismatch']))
 for qid in sorted(expected):
  q=by.get(qid)
  if not q: failures.append(qid+':missing'); continue
  local=[]
  def fail(x): failures.append(qid+':'+x); local.append(x)
  p=COHORT[qid]; m=_find_module(q,d.DEEP_MODULES_V6,d._v6_item_id); topic=str(m.get('topic') or '') if m else ''; cid=d._v6_item_id(q.get('domain'),topic) if m and q.get('domain') else None
  if not m: fail('no_live_canonical_module')
  if topic!=p['canonical_topic']: fail('resolved_topic_mismatch:'+repr(topic))
  if cid!=p['concept_id'] or q.get('concept_id')!=cid: fail('concept_id_changed_or_unresolved')
  prompt=str(q.get('prompt') or ''); ans=str(q.get('answer_text') or ''); low=ans.lower()
  if not q.get('task_alignment_v187'): fail('missing_v187_marker')
  if len(words(prompt))<35 or '?' not in prompt: fail('weak_prompt:'+str(len(words(prompt))))
  if len(words(ans))<100: fail('weak_answer:'+str(len(words(ans))))
  if q.get('choices') or q.get('answer') is not None: fail('not_free_response')
  if not q.get('reviewed_all_domains_v178') or not q.get('review_basis_v178'): fail('lost_v178_review_metadata')
  if set(q.get('depth_layers_v187') or {})!={'foundation','application','senior_decision'}: fail('missing_three_layer_depth')
  traps=q.get('common_traps_v187') or []
  if len(traps)<2 or any(len(words(x))<8 for x in traps): fail('weak_individualized_trap_reasoning')
  if not str(q.get('deliberate_review_v187') or '').strip(): fail('missing_deliberate_review_metadata')
  miss=[t for t in TASK_TERMS[qid] if t not in low]
  if miss: fail('missing_task_terms:'+','.join(miss))
  rows.append({'id':qid,'concept_id':q.get('concept_id'),'resolved_topic':topic,'prompt_words':len(words(prompt)),'answer_words':len(words(ans)),'trap_count':len(traps),'failures':local})
 repaired=set(align.get('repaired') or [])
 if repaired!=expected: failures.append('runtime_repaired_set_mismatch='+','.join(sorted(expected-repaired))+'|extra='+','.join(sorted(repaired-expected)))
 with open('V187_TASK_ALIGNMENT_AUDIT.json','w',encoding='utf-8') as f: json.dump({'expected_ids':sorted(expected),'runtime_alignment':align,'failures':failures,'items':rows},f,indent=2,ensure_ascii=False)
 print(f'V187_EXPECTED|{len(expected)}'); print(f'V187_REPAIRED|{len(repaired)}'); print(f'V187_FAILURES|{len(failures)}')
 for x in failures: print('FAIL|'+x)
 if failures: raise SystemExit(1)
if __name__=='__main__': main()
