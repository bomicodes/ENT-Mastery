"""v20.9 live-canonical Concept Check depth backlog gate."""
import json,os
from audit_concept_check_depth_backlog_v208 import main as _v208_main

TARGETS={'cc-v112-rec-general-ent-emergencies-peritonsillar-abscess'}

def main():
 _v208_main(); source,target='V208_DEPTH_BACKLOG_AUDIT.json','V209_DEPTH_BACKLOG_AUDIT.json'
 if not os.path.exists(source): raise SystemExit('v20.9 backlog gate did not receive v20.8 resolver output')
 with open(source,'r',encoding='utf-8') as f: report=json.load(f)
 markers=report.get('discovered_depth_markers') or []; failures=list(report.get('failures') or [])
 if 'task_alignment_v209' not in markers: failures.append('missing_dynamic_depth_marker:task_alignment_v209')
 untouched={str(x.get('id') or '') for x in report.get('candidates') or []}; residual={str(x.get('id') or '') for x in report.get('residual_candidates') or []}
 for qid in sorted(TARGETS):
  if qid in untouched: failures.append('deepened_target_still_in_untouched_queue:'+qid)
  if qid in residual: failures.append('deepened_target_still_in_residual_queue:'+qid)
 report['audit_version']='v20.9'; report['failures']=failures
 with open(target,'w',encoding='utf-8') as f: json.dump(report,f,indent=2,ensure_ascii=False)
 print(f"V209_CANONICAL|{report.get('canonical_count')}"); print(f"V209_DEEPENED_CONCEPTS|{report.get('deepened_concept_count')}"); print(f"V209_UNTOUCHED_UNDER_75_WORDS|{report.get('untouched_candidate_count')}"); print(f"V209_RESIDUAL_UNDER_75_WORDS|{report.get('residual_candidate_count')}"); print('V209_DISCOVERED_DEPTH_MARKERS|'+','.join(markers)); print(f'V209_FAILURES|{len(failures)}')
 for x in failures: print('FAIL|'+x)
 if failures: raise SystemExit(1)
if __name__=='__main__': main()
