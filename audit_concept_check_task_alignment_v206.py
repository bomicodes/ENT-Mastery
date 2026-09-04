"""v20.6 hard gate for exact-canonical Tracheostomy Emergency decision depth and source provenance."""
import json,re
import runtime_entry
from concept_check_board_repair_v177 import _find_module
from concept_check_depth_v206 import COHORT
QID="cc-v112-rec-general-ent-emergencies-tracheostomy-emergency"
TERM_GROUPS={
 "neck_breather_anatomy":("total laryngectomy","upper airway","stoma"),
 "initial_oxygenation":("oxygen to both","face","stoma"),
 "patency_check":("inner cannula","suction catheter","pass"),
 "false_passage":("false passage","positive pressure","pneumothorax"),
 "cuff":("deflate","cuff","airflow"),
 "tube_removal":("remove","blocked","displaced"),
 "stoma_maturity":("fresh","mature","reinsertion"),
 "monitoring":("waveform capnography","etco2"),
 "hemorrhage_boundary":("tracheo innominate fistula","sentinel bleed"),
}
def words(v): return re.findall(r"\b\w+[\w'-]*\b",str(v or ""))
def sem(v):
 s=str(v or "").lower(); s=re.sub(r"[-–—/]"," ",s); return re.sub(r"\s+"," ",s).strip()
def main():
 d=runtime_entry.data; checks=list(d.CONCEPT_CHECKS_V112); by={str(q.get('id') or ''):q for q in checks}; failures=[]; rows=[]; expected=set(COHORT)
 align=getattr(runtime_entry,"CONCEPT_CHECK_TASK_ALIGNMENT_V206",{}) or {}
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
  if str(q.get('domain') or '')!='General ENT / Emergencies': fail('live_domain_changed:'+repr(q.get('domain')))
  prompt,ans=str(q.get('prompt') or ''),str(q.get('answer_text') or ''); text=sem(ans)
  if not q.get('task_alignment_v206'): fail('missing_v206_marker')
  if len(words(prompt))<65 or '?' not in prompt: fail('weak_prompt:'+str(len(words(prompt))))
  if len(words(ans))<900: fail('weak_answer:'+str(len(words(ans))))
  if q.get('choices') or q.get('answer') is not None: fail('not_free_response')
  if not q.get('reviewed_all_domains_v178') or not q.get('review_basis_v178'): fail('lost_v178_review_metadata')
  if set(q.get('depth_layers_v206') or {})!={'foundation','application','senior_decision'}: fail('missing_three_layer_depth')
  traps=q.get('common_traps_v206') or []
  if len(traps)<8 or any(len(words(x))<18 for x in traps): fail('weak_individualized_trap_reasoning')
  refs=q.get('source_refs_v206') or []; types=[x.get('type') for x in refs]
  if len(refs)<7 or types.count('textbook')<3 or 'consensus' not in types or 'society' not in types or 'guideline' not in types: fail('missing_traceable_source_mix')
  if not str(q.get('deliberate_review_v206') or '').strip(): fail('missing_deliberate_review_metadata')
  for label,terms in TERM_GROUPS.items():
   if not all(sem(t) in text for t in terms): fail('missing_semantic_group:'+label)
  if 'oxygenation comes before tube preservation' not in text: fail('missing_oxygenation_priority_boundary')
  if 'resistance is a stop sign, not an invitation to force' not in text: fail('missing_fresh_tract_stop_rule')
  if 'a total laryngectomy permanently disconnects the mouth and nose from the trachea' not in text: fail('missing_laryngectomy_anatomy_boundary')
  rows.append({'id':qid,'concept_id':q.get('concept_id'),'resolved_topic':topic,'domain':q.get('domain'),'prompt_words':len(words(prompt)),'answer_words':len(words(ans)),'trap_count':len(traps),'source_count':len(refs),'failures':local})
 repaired=set(align.get('repaired') or [])
 if repaired!=expected: failures.append('runtime_repaired_set_mismatch='+','.join(sorted(expected-repaired))+'|extra='+','.join(sorted(repaired-expected)))
 with open('V206_TASK_ALIGNMENT_AUDIT.json','w',encoding='utf-8') as f: json.dump({'expected_ids':sorted(expected),'runtime_alignment':align,'failures':failures,'items':rows},f,indent=2,ensure_ascii=False)
 print(f'V206_EXPECTED|{len(expected)}'); print(f'V206_REPAIRED|{len(repaired)}'); print(f'V206_FAILURES|{len(failures)}')
 for r in rows: print('V206_DEPTH_ITEM|{id}|domain={domain}|prompt={prompt_words}|answer={answer_words}|traps={trap_count}|sources={source_count}|topic={resolved_topic}'.format(**r))
 for x in failures: print('FAIL|'+x)
 if failures: raise SystemExit(1)
if __name__=='__main__': main()
