"""v20.7 live-canonical Concept Check depth backlog gate."""
import json,os
from audit_concept_check_depth_backlog_v206 import main as _v206_main

TARGETS={
 'cc-v112-rec-general-ent-emergencies-esophageal-foreign-body',
 'cc-v112-mgt-general-ent-emergencies-esophageal-foreign-body',
}

def main():
 _v206_main(); source,target='V206_DEPTH_BACKLOG_AUDIT.json','V207_DEPTH_BACKLOG_AUDIT.json'
 if not os.path.exists(source): raise SystemExit('v20.7 backlog gate did not receive v20.6 resolver output')
 with open(source,'r',encoding='utf-8') as f: report=json.load(f)
 markers=report.get('discovered_depth_markers') or []; failures=list(report.get('failures') or [])
 if 'task_alignment_v207' not in markers: failures.append('missing_dynamic_depth_marker:task_alignment_v207')
 untouched={str(x.get('id') or '') for x in report.get('candidates') or []}; residual={str(x.get('id') or '') for x in report.get('residual_candidates') or []}
 for qid in sorted(TARGETS):
  if qid in untouched: failures.append('deepened_target_still_in_untouched_queue:'+qid)
  if qid in residual: failures.append('deepened_target_still_in_residual_queue:'+qid)
 report['audit_version']='v20.7'; report['failures']=failures
 with open(target,'w',encoding='utf-8') as f: json.dump(report,f,indent=2,ensure_ascii=False)
 print(f"V207_CANONICAL|{report.get('canonical_count')}"); print(f"V207_DEEPENED_CONCEPTS|{report.get('deepened_concept_count')}"); print(f"V207_UNTOUCHED_UNDER_75_WORDS|{report.get('untouched_candidate_count')}"); print(f"V207_RESIDUAL_UNDER_75_WORDS|{report.get('residual_candidate_count')}"); print('V207_DISCOVERED_DEPTH_MARKERS|'+','.join(markers)); print(f'V207_FAILURES|{len(failures)}')
 for x in failures: print('FAIL|'+x)
 if failures: raise SystemExit(1)
if __name__=='__main__': main()
