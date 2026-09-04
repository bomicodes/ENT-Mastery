"""v20.6 live-canonical Concept Check depth backlog gate."""
import json,os
from audit_concept_check_depth_backlog_v205 import main as _v205_main

def main():
 _v205_main(); source,target='V205_DEPTH_BACKLOG_AUDIT.json','V206_DEPTH_BACKLOG_AUDIT.json'
 if not os.path.exists(source): raise SystemExit('v20.6 backlog gate did not receive v20.5 resolver output')
 with open(source,'r',encoding='utf-8') as f: report=json.load(f)
 markers=report.get('discovered_depth_markers') or []; failures=list(report.get('failures') or [])
 if 'task_alignment_v206' not in markers: failures.append('missing_dynamic_depth_marker:task_alignment_v206')
 target_id='cc-v112-rec-general-ent-emergencies-tracheostomy-emergency'
 untouched={str(x.get('id') or '') for x in report.get('candidates') or []}; residual={str(x.get('id') or '') for x in report.get('residual_candidates') or []}
 if target_id in untouched: failures.append('deepened_target_still_in_untouched_queue:'+target_id)
 if target_id in residual: failures.append('deepened_target_still_in_residual_queue:'+target_id)
 report['audit_version']='v20.6'; report['failures']=failures
 with open(target,'w',encoding='utf-8') as f: json.dump(report,f,indent=2,ensure_ascii=False)
 print(f"V206_CANONICAL|{report.get('canonical_count')}"); print(f"V206_DEEPENED_CONCEPTS|{report.get('deepened_concept_count')}"); print(f"V206_UNTOUCHED_UNDER_75_WORDS|{report.get('untouched_candidate_count')}"); print(f"V206_RESIDUAL_UNDER_75_WORDS|{report.get('residual_candidate_count')}"); print('V206_DISCOVERED_DEPTH_MARKERS|'+','.join(markers)); print(f'V206_FAILURES|{len(failures)}')
 for x in failures: print('FAIL|'+x)
 if failures: raise SystemExit(1)
if __name__=='__main__': main()
