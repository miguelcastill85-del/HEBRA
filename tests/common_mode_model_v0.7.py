"""
HEBRA v0.7 — Common-mode resilience model

Purpose:
Show how shared technical dependencies can collapse apparent redundancy,
and test the candidate property CMC-2:

"No single modeled catastrophic technical failure is sufficient to make
an invalid canonical transition."

This is a structural model, not a production security proof.
"""

from itertools import combinations

def accepts_invalid(compromised, topology):
    compromised = set(compromised)
    resolver_roots = set(topology["resolver_roots"])
    crypto_algorithms = set(topology["crypto_algorithm_roots"])
    universal_roots = set(topology.get("universal_shared_roots", []))

    resolver_bypass = resolver_roots.issubset(compromised)
    crypto_bypass = crypto_algorithms.issubset(compromised)
    universal_bypass = bool(universal_roots.intersection(compromised))

    return resolver_bypass or crypto_bypass or universal_bypass

def minimum_cut(topology):
    causes = sorted(
        set(topology["resolver_roots"])
        | set(topology["crypto_algorithm_roots"])
        | set(topology.get("universal_shared_roots", []))
    )
    for r in range(1, len(causes) + 1):
        for combo in combinations(causes, r):
            if accepts_invalid(combo, topology):
                return r, list(combo)
    return None, []

SCENARIOS = {
    "single_resolver_single_crypto": {
        "resolver_roots": ["resolver-A"],
        "crypto_algorithm_roots": ["crypto-A"],
        "universal_shared_roots": [],
    },
    "three_resolvers_single_crypto": {
        "resolver_roots": ["resolver-A", "resolver-B", "resolver-C"],
        "crypto_algorithm_roots": ["crypto-A"],
        "universal_shared_roots": [],
    },
    "three_resolvers_dual_crypto": {
        "resolver_roots": ["resolver-A", "resolver-B", "resolver-C"],
        "crypto_algorithm_roots": ["crypto-A", "crypto-B"],
        "universal_shared_roots": [],
    },
    "three_resolvers_dual_crypto_but_shared_runtime": {
        "resolver_roots": ["resolver-A", "resolver-B", "resolver-C"],
        "crypto_algorithm_roots": ["crypto-A", "crypto-B"],
        "universal_shared_roots": ["shared-runtime-root"],
    },
}

def run():
    out = {}
    for name, topology in SCENARIOS.items():
        n, cut = minimum_cut(topology)
        out[name] = {
            "minimum_catastrophic_technical_causes": n,
            "example_cut": cut,
        }
    return out

if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
