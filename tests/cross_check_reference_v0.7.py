"""
HEBRA v0.7 — deterministic cross-check reference

Security rule:
Canonical promotion requires exact agreement from three independent resolver
families. Any disagreement -> HALT_DIVERGENCE.

This is a prototype of the comparison rule, not production code.
"""

import json, hashlib

def h(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

def resolver_output(family, candidate, previous_root, mode="correct"):
    input_hash = h({"candidate":candidate,"previous_root":previous_root})

    if mode == "correct":
        verdict = "ACCEPT" if candidate.get("authorized") else "REJECT"
        transition_hash = h({"input_hash":input_hash,"verdict":verdict})
        next_root = (
            h({"previous_root":previous_root,"transition":transition_hash})
            if verdict == "ACCEPT" else previous_root
        )
    elif mode == "wrong_root":
        verdict = "ACCEPT"
        transition_hash = h({"input_hash":input_hash,"verdict":"ACCEPT"})
        next_root = h({"malicious":"different"})
    elif mode == "false_accept":
        verdict = "ACCEPT"
        transition_hash = h({"input_hash":input_hash,"verdict":"ACCEPT"})
        next_root = h({"previous_root":previous_root,"transition":transition_hash})
    else:
        raise ValueError(mode)

    return {
        "resolver_family": family,
        "input_hash": input_hash,
        "verdict": verdict,
        "transition_hash": transition_hash,
        "next_trusted_root": next_root
    }

def cross_check(outputs, independence_ok=True, root_crypto_ok=True):
    if len(outputs) != 3:
        return {"status":"HALT_CONFIGURATION"}

    if not independence_ok:
        return {"status":"HALT_DEPENDENCY"}

    if not root_crypto_ok:
        return {"status":"HALT_CRYPTO"}

    fields = ["input_hash","verdict","transition_hash","next_trusted_root"]
    for field in fields:
        vals = {o[field] for o in outputs}
        if len(vals) != 1:
            return {"status":"HALT_DIVERGENCE","field":field,"values":sorted(vals)}

    if outputs[0]["verdict"] != "ACCEPT":
        return {"status":"NO_PROMOTION","verdict":outputs[0]["verdict"]}

    return {
        "status":"PROMOTION_ELIGIBLE",
        "transition_hash":outputs[0]["transition_hash"],
        "next_trusted_root":outputs[0]["next_trusted_root"]
    }

if __name__ == "__main__":
    previous = "root-0"
    valid = {"record_id":"good","authorized":True}
    invalid = {"record_id":"bad","authorized":False}

    cases = {}
    good_outputs = [
        resolver_output("A",valid,previous),
        resolver_output("B",valid,previous),
        resolver_output("C",valid,previous),
    ]
    cases["all_agree_valid"] = cross_check(good_outputs)

    divergent = [
        resolver_output("A",valid,previous),
        resolver_output("B",valid,previous),
        resolver_output("C",valid,previous,"wrong_root"),
    ]
    cases["one_wrong_root"] = cross_check(divergent)

    false_accept = [
        resolver_output("A",invalid,previous),
        resolver_output("B",invalid,previous),
        resolver_output("C",invalid,previous,"false_accept"),
    ]
    cases["one_false_accept"] = cross_check(false_accept)

    rejected = [
        resolver_output("A",invalid,previous),
        resolver_output("B",invalid,previous),
        resolver_output("C",invalid,previous),
    ]
    cases["all_agree_reject"] = cross_check(rejected)
    cases["shared_dependency_detected"] = cross_check(good_outputs, independence_ok=False)
    cases["root_crypto_incomplete"] = cross_check(good_outputs, root_crypto_ok=False)

    print(json.dumps(cases, indent=2))
