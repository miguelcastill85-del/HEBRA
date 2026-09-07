"""
HEBRA v0.6 — Independence Validator

Known shared failure roots collapse signers into one effective component.
Unknown critical dependency information is conservative: it does not prove independence.
"""

HARD_FIELDS = [
    "operator_control_id",
    "organization_control_id",
    "key_custody_root_id",
    "identity_root_id",
    "signing_service_root_id",
    "recovery_controller_id",
]

def build_components(certificates):
    ids = [c["signer_id"] for c in certificates]
    parent = {x:x for x in ids}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a,b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for field in HARD_FIELDS:
        buckets = {}
        unknown = []
        for c in certificates:
            value = c.get(field)
            if value in (None, "", "unknown"):
                unknown.append(c["signer_id"])
            else:
                buckets.setdefault(value, []).append(c["signer_id"])

        for members in buckets.values():
            for x in members[1:]:
                union(members[0], x)

        if len(unknown) > 1:
            for x in unknown[1:]:
                union(unknown[0], x)

    return {x:find(x) for x in ids}

def validate_transition(certificates, approvals):
    cert_by_id = {c["signer_id"]:c for c in certificates}
    comps = build_components(certificates)
    required = ["PROV","MEAS","METH","SAFE"]

    selected = []
    failures = []

    for chamber in required:
        members = [s for s in approvals.get(chamber,[]) if s in cert_by_id]
        distinct = {}
        for s in members:
            distinct.setdefault(comps[s], s)
        if len(distinct) < 2:
            failures.append(f"{chamber}: fewer than 2 effective independent approvals")
        selected.extend(distinct.values())

    component_chambers = {}
    for chamber, members in approvals.items():
        for s in members:
            if s not in comps:
                continue
            component_chambers.setdefault(comps[s], set()).add(chamber)
    overlapping = {k:v for k,v in component_chambers.items() if len(v)>1}
    if overlapping:
        failures.append("At least one effective failure domain appears across multiple chambers")

    total_components = {comps[s] for s in selected}
    if len(total_components) < 8:
        failures.append(f"Only {len(total_components)} effective domains; 8 required")

    return {
        "valid": not failures,
        "effective_domain_count": len(total_components),
        "failures": failures,
        "components": comps
    }
