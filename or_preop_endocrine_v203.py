"""v20.3 endocrine preoperative-context refinement for OR Tomorrow."""


def apply_or_preop_endocrine_v203(registry):
    """Make thyroid functional status an explicit night-before setup item."""
    changed = []
    thyroid_slugs = ("thyroid-lobectomy", "total-thyroidectomy", "reop-thyroid")
    functional_status = (
        "Establish thyroid functional status before surgery: review recent TSH and free T4 "
        "(add T3 when clinically indicated) and determine whether the patient is euthyroid, "
        "hyperthyroid, or hypothyroid. In hyperthyroidism/Graves disease, confirm appropriate "
        "preoperative medical optimization and recognize the perioperative risk of uncontrolled thyrotoxicosis."
    )
    for slug in thyroid_slugs:
        op = registry.get(slug)
        if not op:
            continue
        setup = list(op.get("setup") or [])
        if not any("thyroid functional status" in str(x).lower() for x in setup):
            setup.insert(0, functional_status)
            op["setup"] = setup
            changed.append(slug)
        op["preop_functional_status_v203"] = True
    return {"changed": changed, "count": len(changed)}
