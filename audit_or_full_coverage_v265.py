"""v26.5 comprehensive OR Tomorrow coverage inventory.

Diagnostic + structural hard gate. Prints every live procedure with its depth fields and
review-layer markers so clinical gaps can be judged from the actual production registry.
"""
import os, tempfile
from collections import Counter

fd, db = tempfile.mkstemp(prefix='ent_or_full_', suffix='.db'); os.close(fd)
os.environ.pop('DATABASE_URL', None); os.environ['SQLITE_PATH'] = db
os.environ.pop('ENT_MASTERY_ACCESS_PASSWORD', None)

try:
    import runtime_entry as rt
    reg = rt.data.OR_PREP_REGISTRY
    assert reg, 'OR_PREP_REGISTRY is empty'
    client = rt.app.test_client()
    failures=[]
    domains=Counter()
    specific=[]
    generic_only=[]
    marker_keys=(
        'preop_decision_v212','otology_management_v217','laryngology_management_v218',
        'pediatric_airway_management_v220','reconstruction_management_v225',
        'sleep_management_v229','laryngectomy_management_v233','neck_dissection_management_v234',
        'major_oncologic_resection_management_v235','skull_base_management_v236',
        'arytenoid_adduction_management_v237','adenotonsillar_management_v238',
        'septoplasty_management_v239','cochlear_implant_management_v2310',
        'salivary_management_v2311','thyroid_management_v2312','parathyroid_management_v2313',
        'tors_management_v2314','tracheostomy_management_v2314',
        'csf_nasoseptal_management_v2314','vestibular_schwannoma_management_v2314',
    )
    print('OR_FULL_COVERAGE_BEGIN')
    for slug, op in sorted(reg.items()):
        domain=str(op.get('domain') or 'UNSPECIFIED'); domains[domain]+=1
        counts={k:len(op.get(k) or []) for k in ('setup','landmarks','steps','danger','exit_check','postop')}
        comp=op.get('complications') or {}
        counts['early']=len(comp.get('early') or []); counts['late']=len(comp.get('late') or [])
        counts['sources']=len(op.get('source_basis') or [])
        markers=[k for k in marker_keys if op.get(k)]
        if markers: specific.append(slug)
        else: generic_only.append(slug)
        required={'setup':2,'landmarks':3,'steps':6,'danger':2,'exit_check':2,'postop':2,'early':1,'late':1,'sources':2}
        for key,n in required.items():
            if counts[key] < n: failures.append(f'{slug}: {key} {counts[key]} < {n}')
        linked=str(op.get('linked_topic') or '').strip()
        if not linked: failures.append(f'{slug}: missing linked_topic')
        r=client.get('/case-tomorrow', query_string={'q':op.get('title',slug)}, follow_redirects=True)
        if r.status_code >= 500: failures.append(f'{slug}: route HTTP {r.status_code}')
        print(f"{slug}\t{op.get('title','')}\t{domain}\tlinked={linked}\t" + ','.join(f'{k}={v}' for k,v in counts.items()) + f"\tspecific={','.join(markers) or 'NONE'}")
    print('OR_FULL_COVERAGE_END', len(reg))
    print('DOMAIN_COUNTS', dict(sorted(domains.items())))
    print('SPECIFIC_REVIEWED', len(specific))
    print('GENERIC_ONLY', len(generic_only), ','.join(generic_only))
    if failures:
        print('OR_FULL_COVERAGE_FAILURES')
        print('\n'.join(failures))
        raise SystemExit(1)
    print(f'PASS: {len(reg)} live OR Tomorrow modules satisfy structural, canonical-link, and route contract')
finally:
    try: os.remove(db)
    except OSError: pass