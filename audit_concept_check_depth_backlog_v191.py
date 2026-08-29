"""v19.1 deterministic post-completion Concept Check depth backlog audit."""
from collections import Counter
import json,re
import runtime_entry
from concept_check_board_repair_v177 import _find_module
DATA=runtime_entry.data
MARKERS=("task_alignment_v180","task_alignment_v181","task_alignment_v182","task_alignment_v183","task_alignment_v184","task_alignment_v185","task_alignment_v186","task_alignment_v187","task_alignment_v188","task_alignment_v189","task_alignment_v190","task_alignment_v191")
PRIORITY_GROUPS=((5,("airway","hemorrhage","bleed","hematoma","carotid","epistaxis","foreign body","deep neck","abscess")),(4,("complication","postoperative","post-op","rescue","emergency","escalat","unstable","aspiration")),(3,("surgery","operative","operation","resection","dissection","laryngoscopy","cordotomy","arytenoid","flap","skull base","sphenoid","parathyroid")),(2,("physiology","nerve","vascular","anatom","staging","margin","radiation","chemotherapy","systemic therapy")),(1,("management","treatment","workup","diagnostic","imaging","surveillance")))
def words(v): return len(re.findall(r"\b\w+[\w'-]*\b",str(v or "")))
def prompt(q): return str(q.get("prompt") or q.get("question") or q.get("stem") or "").strip()
def answer(q): return str(q.get("answer_text") or q.get("model_answer") or q.get("correct_answer") or "").strip()
def priority(topic,p):
 h=f"{topic} {p}".lower(); score=0; hits=[]
 for weight,terms in PRIORITY_GROUPS:
  gh=[t for t in terms if t in h]
  if gh: score+=weight; hits.extend(gh)
 return score,sorted(set(hits))
def sort_key(r): return (-r["priority_score"],r["answer_words"],r["prompt_words"],r["concept_id"],r["id"])
def main():
 checks=list(DATA.CONCEPT_CHECKS_V112); failures=[]; ids=Counter(str(q.get("id") or "") for q in checks)
 for qid,count in ids.items():
  if not qid: failures.append("missing_concept_check_id")
  elif count>1: failures.append(f"duplicate_concept_check_id:{qid}:count={count}")
 canonical={}
 for domain,modules in DATA.DEEP_MODULES_V6.items():
  for module in modules:
   topic=str(module.get("topic") or "").strip()
   if not topic: continue
   cid=DATA._v6_item_id(domain,topic)
   if cid in canonical: failures.append(f"duplicate_canonical_id:{cid}")
   canonical[cid]={"domain":domain,"topic":topic,"module":module}
 resolved=[]; deepened_concepts=set()
 for q in checks:
  if not q.get("reviewed_all_domains_v178"): continue
  qid=str(q.get("id") or ""); module=_find_module(q,DATA.DEEP_MODULES_V6,DATA._v6_item_id)
  if not module: failures.append(f"reviewed_orphan:{qid}:no_canonical_module"); continue
  domain=str(q.get("domain") or ""); topic=str(module.get("topic") or ""); cid=DATA._v6_item_id(domain,topic)
  if q.get("concept_id") is not None and q.get("concept_id")!=cid: failures.append(f"canonical_link_mismatch:{qid}:{q.get('concept_id')!r}!={cid!r}"); continue
  if cid not in canonical: failures.append(f"reviewed_orphan:{qid}:expected_id_not_live:{cid}"); continue
  resolved.append((q,module,cid))
  if any(q.get(m) for m in MARKERS): deepened_concepts.add(cid)
 primary=[]; residual=[]; reviewed_fr=0; individually_deepened=0
 for q,module,cid in resolved:
  if q.get("choices"): continue
  a=answer(q)
  if not a: continue
  reviewed_fr+=1
  if words(a)>=75: continue
  if any(q.get(m) for m in MARKERS): individually_deepened+=1; continue
  p=prompt(q); topic=str(module.get("topic") or ""); score,hits=priority(topic,p)
  row={"id":str(q.get("id") or ""),"concept_id":cid,"domain":str(q.get("domain") or ""),"canonical_topic":topic,"board_dimension":q.get("board_dimension_v178"),"prompt_words":words(p),"answer_words":words(a),"priority_score":score,"priority_hits":hits,"prompt":p,"answer_text":a}
  (residual if cid in deepened_concepts else primary).append(row)
 primary.sort(key=sort_key); residual.sort(key=sort_key)
 for i,r in enumerate(primary,1): r["rank"]=i
 for i,r in enumerate(residual,1): r["residual_rank"]=i
 report={"canonical_count":len(canonical),"concept_check_count":len(checks),"reviewed_free_response_count":reviewed_fr,"deepened_v180_v191_concept_count":len(deepened_concepts),"individually_deepened_questions_under_75_words":individually_deepened,"untouched_candidate_count":len(primary),"residual_candidate_count":len(residual),"selection_contract":"exact live canonical IDs; primary untouched concepts then residual weak siblings; priority desc, answer words asc, prompt words asc, concept_id, question id; clinical priority may override misleading lexical rank","failures":failures,"candidates":primary,"residual_candidates":residual}
 with open("V191_DEPTH_BACKLOG_AUDIT.json","w",encoding="utf-8") as f: json.dump(report,f,indent=2,ensure_ascii=False)
 print(f"V191_CANONICAL|{len(canonical)}"); print(f"V191_CONCEPT_CHECKS|{len(checks)}"); print(f"V191_REVIEWED_FREE_RESPONSE|{reviewed_fr}"); print(f"V191_DEEPENED_CONCEPTS|{len(deepened_concepts)}"); print(f"V191_UNTOUCHED_UNDER_75_WORDS|{len(primary)}"); print(f"V191_RESIDUAL_UNDER_75_WORDS|{len(residual)}")
 for r in primary[:12]: print("V191_CANDIDATE|{rank}|priority={priority_score}|answer={answer_words}|prompt={prompt_words}|{domain}|{canonical_topic}|{id}|{concept_id}".format(**r))
 for x in failures[:200]: print("FAIL|"+x)
 print(f"V191_FAILURES|{len(failures)}")
 if failures: raise SystemExit(1)
if __name__=="__main__": main()
