
"""
HEBRA Reference Engine v0.1
Educational/low-risk prototype only.

Design:
1) safety gate
2) integrity / poisoning quarantine
3) context transferability
4) evidence weighting
5) local success estimate
6) contradiction + adverse-event accounting
7) abstention when evidence is insufficient

This intentionally does NOT emit a single public "HEBRA score".
"""

from math import sqrt

TIER_WEIGHT = {
    "H0": 0.00, "H1": 0.15, "H2": 0.35,
    "H3": 0.55, "H4": 0.80, "H5": 1.00, "HX": 0.00
}
VERIFY_WEIGHT = {
    "unverified": 0.20,
    "partially_verified": 0.60,
    "verified": 1.00,
    "contested": 0.00
}
INDEPENDENCE_WEIGHT = {
    "unknown": 0.30,
    "same_actor": 0.20,
    "related_actor": 0.60,
    "independent": 0.85,
    "multi_independent": 1.00
}

QUARANTINE_FLAGS = {"possible_sybil", "possible_poisoning"}
BLOCKING_STATUSES = {"disputed", "withdrawn"}

def _extract_value(x):
    if isinstance(x, dict) and "value" in x:
        return x["value"]
    return x

def similarity(query_context, record_context):
    """Transparent Gower-like similarity for v0.1.

    Query features may include:
      {"value": ..., "weight": ..., "scale": ...}
    Record features may be either raw values or {"value": ...}.
    """
    parts = []
    for name, q in query_context.items():
        if name not in record_context:
            continue

        qv = _extract_value(q)
        rv = _extract_value(record_context[name])
        weight = float(q.get("weight", 1.0)) if isinstance(q, dict) else 1.0

        if (
            isinstance(qv, (int, float)) and not isinstance(qv, bool)
            and isinstance(rv, (int, float)) and not isinstance(rv, bool)
        ):
            scale = float(q.get("scale", max(abs(float(qv)), 1.0))) if isinstance(q, dict) else max(abs(float(qv)), 1.0)
            s = max(0.0, 1.0 - abs(float(qv) - float(rv)) / max(scale, 1e-9))
        else:
            s = 1.0 if qv == rv else 0.0
        parts.append((s, weight))

    if not parts:
        return 0.0
    return sum(s*w for s,w in parts) / sum(w for _,w in parts)

def verification_weight(record):
    items = record["evidence"]["verification"]
    return max(VERIFY_WEIGHT.get(x["status"], 0.0) for x in items)

def base_evidence_weight(record):
    return (
        TIER_WEIGHT.get(record["evidence"]["tier"], 0.0)
        * verification_weight(record)
        * INDEPENDENCE_WEIGHT.get(record["evidence"]["independence"], 0.0)
    )

def eligible(record):
    if record["lifecycle"]["status"] in BLOCKING_STATUSES:
        return False, "blocked_status"
    if QUARANTINE_FLAGS.intersection(record["evidence"]["quality_flags"]):
        return False, "quarantine_integrity"
    if record["safety"]["risk_band"] not in {"R0", "R1"}:
        return False, "risk_gate"
    if not record["safety"]["automated_recommendation_allowed"]:
        return False, "automation_disallowed"
    return True, None

def evaluate_family(records, query_context, min_similarity=0.45):
    accepted, quarantined = [], []

    for r in records:
        ok, reason = eligible(r)
        if not ok:
            quarantined.append({"record_id": r["record_id"], "reason": reason})
            continue

        sim = similarity(query_context, r["context"])
        if sim < min_similarity:
            continue

        w = sim * base_evidence_weight(r)
        if w <= 0:
            continue

        accepted.append((r, sim, w))

    alpha, beta = 1.0, 1.0
    adverse_weight = 0.0
    severe_adverse = 0
    contradiction_weight = 0.0

    for r, sim, w in accepted:
        success = bool(r["success"])
        alpha += w if success else 0.0
        beta += w if not success else 0.0

        if r.get("contradiction", False):
            contradiction_weight += w

        sev = r.get("adverse_severity", "none")
        if sev in {"mild", "moderate", "severe", "critical"}:
            adverse_weight += w
        if sev in {"severe", "critical"}:
            severe_adverse += 1

    n_eff = sum(w for _, _, w in accepted)
    posterior_mean = alpha / (alpha + beta)
    var = (alpha * beta) / (((alpha + beta) ** 2) * (alpha + beta + 1))
    lower_approx = max(0.0, posterior_mean - 1.96 * sqrt(var))
    mean_similarity = (
        sum(sim*w for _, sim, w in accepted) / n_eff if n_eff else 0.0
    )
    contradiction_rate = contradiction_weight / n_eff if n_eff else None
    adverse_rate = adverse_weight / n_eff if n_eff else None

    if severe_adverse:
        status = "SUSPEND"
        reason = "severe_or_critical_adverse_event"
    elif n_eff < 0.75:
        status = "INSUFFICIENT"
        reason = "effective_evidence_too_low"
    elif mean_similarity < 0.60:
        status = "INSUFFICIENT"
        reason = "transferability_too_low"
    elif contradiction_rate is not None and contradiction_rate > 0.35:
        status = "INSUFFICIENT"
        reason = "contradiction_too_high"
    else:
        status = "ELIGIBLE"
        reason = None

    return {
        "status": status,
        "reason": reason,
        "evidence_vector": {
            "accepted_records": len(accepted),
            "effective_evidence": round(n_eff, 4),
            "mean_transferability": round(mean_similarity, 4),
            "posterior_success_mean": round(posterior_mean, 4),
            "approx_95pct_lower_bound": round(lower_approx, 4),
            "weighted_adverse_rate": None if adverse_rate is None else round(adverse_rate, 4),
            "weighted_contradiction_rate": None if contradiction_rate is None else round(contradiction_rate, 4),
            "severe_adverse_events": severe_adverse
        },
        "quarantined": quarantined
    }

def pareto_frontier(results):
    """Return non-dominated eligible interventions."""
    items = [(name, data) for name, data in results.items() if data["status"] == "ELIGIBLE"]

    def dims(data):
        v = data["evidence_vector"]
        return (
            v["posterior_success_mean"],
            v["approx_95pct_lower_bound"],
            v["mean_transferability"],
            v["effective_evidence"],
            -(v["weighted_adverse_rate"] or 0.0),
            -(v["weighted_contradiction_rate"] or 0.0),
        )

    frontier = []
    for i, (name_i, data_i) in enumerate(items):
        di = dims(data_i)
        dominated = False

        for j, (_, data_j) in enumerate(items):
            if i == j:
                continue
            dj = dims(data_j)
            if all(b >= a for a, b in zip(di, dj)) and any(b > a for a, b in zip(di, dj)):
                dominated = True
                break

        if not dominated:
            frontier.append(name_i)

    return frontier
