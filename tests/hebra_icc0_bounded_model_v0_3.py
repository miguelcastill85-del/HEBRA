
"""
HEBRA ICC-0 bounded state explorer v0.3

Goal:
Explore all sequences up to a bounded depth from an initial state and verify:
untrusted actions never change the trusted root.

This is bounded model checking, not a complete mathematical proof.
"""

from dataclasses import dataclass
from hashlib import sha256
import json
from collections import deque

def H(x):
    return sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

@dataclass(frozen=True)
class State:
    promoted: tuple = ()
    inert_count: int = 0
    invalid_attestations: int = 0
    active_policy: str = "P0"

def trusted_root(s: State) -> str:
    return H({
        "promoted": sorted(s.promoted),
        "policy": s.active_policy,
        "resolver": "v0.3"
    })

# Attacker actions: none possess a valid transition capability.
def submit_untrusted(s):
    return State(s.promoted, s.inert_count + 1, s.invalid_attestations, s.active_policy)

def forge_attestation(s):
    return State(s.promoted, s.inert_count, s.invalid_attestations + 1, s.active_policy)

def inject_policy_as_data(s):
    return State(s.promoted, s.inert_count + 1, s.invalid_attestations, s.active_policy)

def prompt_injection(s):
    return State(s.promoted, s.inert_count + 1, s.invalid_attestations, s.active_policy)

def duplicate_sybil_record(s):
    return State(s.promoted, s.inert_count + 1, s.invalid_attestations, s.active_policy)

ATTACKS = {
    "submit_untrusted": submit_untrusted,
    "forge_attestation": forge_attestation,
    "inject_policy_as_data": inject_policy_as_data,
    "prompt_injection": prompt_injection,
    "duplicate_sybil_record": duplicate_sybil_record,
}

def explore(max_depth=8):
    initial = State(promoted=("legitimate-claim-hash",))
    expected = trusted_root(initial)
    q = deque([(initial, [])])
    seen = {initial}
    checked_transitions = 0

    while q:
        s, trace = q.popleft()
        if trusted_root(s) != expected:
            return {
                "ok": False,
                "counterexample": trace,
                "state": repr(s),
                "expected_root": expected,
                "actual_root": trusted_root(s),
                "states": len(seen),
                "transitions": checked_transitions,
            }
        if len(trace) >= max_depth:
            continue

        for name, fn in ATTACKS.items():
            ns = fn(s)
            checked_transitions += 1

            # Strong local form: EACH unauthorized transition preserves root.
            if trusted_root(ns) != trusted_root(s):
                return {
                    "ok": False,
                    "counterexample": trace + [name],
                    "state_before": repr(s),
                    "state_after": repr(ns),
                    "root_before": trusted_root(s),
                    "root_after": trusted_root(ns),
                    "states": len(seen),
                    "transitions": checked_transitions,
                }

            if ns not in seen:
                seen.add(ns)
                q.append((ns, trace + [name]))

    return {
        "ok": True,
        "max_depth": max_depth,
        "attack_types": list(ATTACKS),
        "states_explored": len(seen),
        "transitions_checked": checked_transitions,
        "trusted_root": expected,
        "property": "Every modeled unauthorized transition preserves trusted_root exactly."
    }

if __name__ == "__main__":
    import json
    print(json.dumps(explore(10), indent=2))
