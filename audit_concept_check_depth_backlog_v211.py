"""v20.11 live-canonical Concept Check depth backlog gate."""
import json,os
from audit_concept_check_depth_backlog_v210 import main as _v210_main

TARGETS={
 'cc-v112-rec-facial-plastics-trauma-facial-soft-tissue-lacerations-burns',
 'cc-v112-mgt-pediatric-otolaryngology-microtia-reconstruction',
 'cc-v112-rec-laryngology-voice-swallowing-tracheobronchial-endoscopy-principles',
 'cc-v112-mgt-general-ent-emergencies-laser-energy-safety-in-otolaryngology',
 'cc-v112-mgt-rhinology-allergy-skull-base-frontal-sinusotomy-draf-procedures',
 'cc-v112-rec-rhinology-allergy-skull-base-frontal-sinusotomy-draf-procedures',
 'cc-v112-mgt-thyroid-parathyroid-salivary-four-gland-parathyroid-exploration',
 'cc-v112-rec-facial-plastics-trauma-local-flap-reconstruction',
}

def main():
 _v210_main(); source,target='V210_DEPTH_BACKLOG_AUDIT.json','V211_DEPTH_BACKLOG_AUDIT.json'
 if not os.path.exists(source): raise SystemExit('v20.11 backlog gate did not receive v20.10 resolver output')
 with open(source,'r',encoding='utf-8') as f: report=json.load(f)
 markers=report.get('discovered_depth_markers') or []; failures=list(report.get('failures') or [])
 if 'task_alignment_v211' not in markers: failures.append('missing_dynamic_depth_marker:task_alignment_v211')
 untouched={str(x.get('id') or '') for x in report.get('candidates') or []}; residual={str(x.get('id') or '') for x in report.get('residual_candidates') or []}
 for qid in sorted(TARGETS):
  if qid in untouched: failures.append('deepened_target_still_in_untouched_queue:'+qid)
  if qid in residual: failures.append('deepened_target_still_in_residual_queue:'+qid)
 report['audit_version']='v20.11'; report['failures']=failures
 with open(target,'w',encoding='utf-8') as f: json.dump(report,f,indent=2,ensure_ascii=False)
 print(f"V211_CANONICAL|{report.get('canonical_count')}"); print(f"V211_DEEPENED_CONCEPTS|{report.get('deepened_concept_count')}"); print(f"V211_UNTOUCHED_UNDER_75_WORDS|{report.get('untouched_candidate_count')}"); print(f"V211_RESIDUAL_UNDER_75_WORDS|{report.get('residual_candidate_count')}"); print('V211_DISCOVERED_DEPTH_MARKERS|'+','.join(markers)); print(f'V211_FAILURES|{len(failures)}')
 for x in failures: print('FAIL|'+x)
 if failures: raise SystemExit(1)
if __name__=='__main__': main()
