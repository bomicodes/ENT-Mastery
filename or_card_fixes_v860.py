"""v86.0: accuracy review of every OR card.

Six independent reviewers audited every rendered field of all OR cards (indications, setup,
operative steps, landmarks, danger, exit check, post-op, complications, attending questions)
for accuracy against current US practice, placeholder or copied content, contradictions and
thin step lists. Their findings live in or_card_fixes_v860.json as field-level edits and are
applied here, at the end of boot, to the final registry.
"""
import json
import os

_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "or_card_fixes_v860.json")


def _load():
    with open(_PATH, encoding="utf-8") as fh:
        return json.load(fh)


def _sync_steps(card):
    pairs = card.get("steps_v840")
    if pairs:
        card["steps"] = [f"{t}. {d}" for t, d in pairs]


def _apply_list(lst, index, value):
    if index == "append":
        lst.append(value)
    elif isinstance(index, str) and index.startswith("insert:"):
        lst.insert(int(index.split(":", 1)[1]), value)
    elif value == "DELETE":
        lst[int(index)] = None
    else:
        lst[int(index)] = value


def install_or_card_fixes_v860(data):
    registry = data.OR_PREP_REGISTRY
    applied, skipped = 0, []
    fixes = _load()
    # Whole-field replacements first, then item edits (in reverse index order so deletes and
    # inserts don't shift later targets), then compact deleted items.
    def order(f):
        idx = f.get("index")
        whole = idx is None
        sub = str(idx).rpartition(":")[2] if idx is not None else ""
        pos = idx if isinstance(idx, int) else (int(sub) if sub.isdigit() and not str(idx).startswith("insert") else -1)
        # item edits high-to-low; appends/inserts last so they can't shift edit targets
        return (0 if whole else 1, f["slug"], f["field"], -pos)
    touched = set()
    for f in sorted(fixes, key=order):
        card = registry.get(f["slug"])
        field, idx, val = f["field"], f.get("index"), f.get("new_value")
        if card is None:
            skipped.append((f["slug"], field, "no card"))
            continue
        try:
            if idx is None and val == "DELETE":
                if field != "steps":  # old plain steps are rebuilt from steps_v840
                    card.pop(field, None)
                applied += 1
                continue
            if field == "steps" and (card.get("steps_v840") or (idx is None and val and isinstance(val[0], list))):
                field = "steps_v840"
                card.setdefault("steps_v840", [[s, ""] for s in card.get("steps", [])])
            if idx is None:
                card[field] = val
            elif field == "complications":
                key, _, sub = str(idx).partition(":")
                lst = card.setdefault("complications", {}).setdefault(key, [])
                _apply_list(lst, sub if sub in ("append",) or sub.startswith("insert") else (int(sub) if sub else "append"), val)
            else:
                lst = card.setdefault(field, [])
                if isinstance(lst, str):
                    card[field] = val
                else:
                    _apply_list(lst, idx, val)
            touched.add(f["slug"])
            applied += 1
        except (IndexError, ValueError, TypeError, KeyError) as exc:
            skipped.append((f["slug"], field, f"{type(exc).__name__}: {idx}"))
    for slug in touched:
        card = registry[slug]
        for k, v in list(card.items()):
            if isinstance(v, list):
                card[k] = [x for x in v if x is not None]
            elif k == "complications" and isinstance(v, dict):
                card[k] = {kk: [x for x in vv if x is not None] if isinstance(vv, list) else vv for kk, vv in v.items()}
        _sync_steps(card)
    return {"applied": applied, "skipped": skipped, "cards": len(touched)}
