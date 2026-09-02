"""v20.4 live-canonical Concept Check depth backlog gate."""
import json,os
from audit_concept_check_depth_backlog_v203 import main as _v203_main

def main():
 _v203_main(); source,target='V203_DEPTH_BACKLOG_AUDIT.json','V204_DEPTH_BACKLOG_AUDIT.json'
 if not os.path.exists(source): raise SystemExit('v20.4 backlog gate did not receive v20.3 resolver output')
 with open(source,'r',encoding='utf-8') as f: report=json.load(f)
 markers=report.get('discovered_depth_markers') or []; failures=list(report.get('failures') or [])
 if 'task_alignment_v204' not in markers: failures.append('missing_dynamic_depth_marker:task_alignment_v204')
 target_id='cc-v112-mgt-rhinology-allergy-skull-base-sphenoidotomy'
 untouched={str(x.get('id') or '') for x in report.get('candidates') or []}; residual={str(x.get('id') or '') for x in report.get('residual_candidates') or []}
 if target_id in untouched: failures.append('deepened_target_still_in_untouched_queue:'+target_id)
 if target_id in residual: failures.append('deepened_target_still_in_residual_queue:'+target_id)
 report['audit_version']='v20.4'; report['failures']=failures
 with open(target,'w',encoding='utf-8') as f: json.dump(report,f,indent=2,ensure_ascii=False)
 print(f"V204_CANONICAL|{report.get('canonical_count')}"); print(f"V204_DEEPENED_CONCEPTS|{report.get('deepened_concept_count')}"); print(f"V204_UNTOUCHED_UNDER_75_WORDS|{report.get('untouched_candidate_count')}"); print(f"V204_RESIDUAL_UNDER_75_WORDS|{report.get('residual_candidate_count')}"); print('V204_DISCOVERED_DEPTH_MARKERS|'+','.join(markers)); print(f'V204_FAILURES|{len(failures)}')
 for x in failures: print('FAIL|'+x)
 if failures: raise SystemExit(1)
if __name__=='__main__': main()
