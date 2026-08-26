"""Temporary/diagnostic inventory for OR Tomorrow v20 procedure-level rewrite."""
import os, tempfile
fd, db = tempfile.mkstemp(prefix='ent_or_inventory_', suffix='.db'); os.close(fd)
os.environ.pop('DATABASE_URL', None); os.environ['SQLITE_PATH'] = db
os.environ.pop('ENT_MASTERY_ACCESS_PASSWORD', None)
try:
    import runtime_entry as rt
    reg = rt.data.OR_PREP_REGISTRY
    print('OR_INVENTORY_BEGIN')
    for slug, op in sorted(reg.items()):
        print(f"{slug}\t{op.get('title','')}\t{op.get('domain','')}")
    print('OR_INVENTORY_END', len(reg))
finally:
    try: os.remove(db)
    except OSError: pass
