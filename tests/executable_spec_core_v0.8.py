"""
HEBRA v0.8 — Executable Specification Core

Purpose:
A small deterministic oracle for the promotion-gate semantics used by tests.
It is an executable specification prototype, not the production Crystal Core.

Important:
The canonicalizer here is a constrained prototype. Production must use the
project's exact canonicalization standard once frozen.
"""

import json, hashlib, re

CHAMBERS = ("PROV", "MEAS", "METH", "SAFE")
TOP_FIELDS = {
    "protocol_version", "previous_root", "epoch",
    "candidate", "approvals", "root_crypto"
}
CANDIDATE_FIELDS = {"id", "payload_hash"}
APPROVAL_FIELDS = {"chamber", "signer_id", "effective_domain"}
CRYPTO_FIELDS = {"suite_a_valid", "suite_b_valid"}
HEX64 = re.compile(r"^[0-9a-f]{64}$")

def canonical(obj):
    return json.dumps(
        obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")

def sha256_hex(b):
    return hashlib.sha256(b).hexdigest()

def reject(code):
    return {
        "verdict": "REJECT",
        "reason_code": code,
        "transition_hash": None,
        "next_trusted_root": None
    }

def _exact_fields(obj, allowed):
    return isinstance(obj, dict) and set(obj.keys()) == allowed

def evaluate(event):
    # Validation order is part of the specification.
    if not isinstance(event, dict) or set(event.keys()) != TOP_FIELDS:
        return reject("SCHEMA_TOP")
    if not _exact_fields(event["candidate"], CANDIDATE_FIELDS):
        return reject("SCHEMA_CANDIDATE")
    if not isinstance(event["approvals"], list):
        return reject("SCHEMA_APPROVALS")
    if not _exact_fields(event["root_crypto"], CRYPTO_FIELDS):
        return reject("SCHEMA_CRYPTO")
    for a in event["approvals"]:
        if not _exact_fields(a, APPROVAL_FIELDS):
            return reject("SCHEMA_APPROVAL_ITEM")

    if event["protocol_version"] != "0.8":
        return reject("INVALID_VERSION")

    if not isinstance(event["previous_root"], str) or not HEX64.fullmatch(event["previous_root"]):
        return reject("INVALID_PREVIOUS_ROOT")

    if (
        not isinstance(event["epoch"], int)
        or isinstance(event["epoch"], bool)
        or event["epoch"] < 0
    ):
        return reject("INVALID_EPOCH")

    c = event["candidate"]
    if (
        not isinstance(c["id"], str) or not (1 <= len(c["id"]) <= 128)
        or not isinstance(c["payload_hash"], str)
        or not HEX64.fullmatch(c["payload_hash"])
    ):
        return reject("INVALID_CANDIDATE")

    normalized = []
    for a in event["approvals"]:
        if (
            a["chamber"] not in CHAMBERS
            or not isinstance(a["signer_id"], str) or not a["signer_id"]
            or not isinstance(a["effective_domain"], str) or not a["effective_domain"]
        ):
            return reject("INVALID_APPROVAL")
        normalized.append(
            (a["chamber"], a["signer_id"], a["effective_domain"])
        )

    normalized = sorted(set(normalized))

    by_chamber = {x: [] for x in CHAMBERS}
    for chamber, signer, domain in normalized:
        by_chamber[chamber].append((signer, domain))

    for chamber in CHAMBERS:
        signers = {s for s, _ in by_chamber[chamber]}
        domains = {d for _, d in by_chamber[chamber]}
        if len(signers) < 2 or len(domains) < 2:
            return reject("MISSING_CHAMBER_QUORUM")

    domain_chambers = {}
    for chamber, _, domain in normalized:
        domain_chambers.setdefault(domain, set()).add(chamber)
    if any(len(cs) > 1 for cs in domain_chambers.values()):
        return reject("CROSS_CHAMBER_DEPENDENCY")

    rc = event["root_crypto"]
    if rc["suite_a_valid"] is not True or rc["suite_b_valid"] is not True:
        return reject("ROOT_CRYPTO_INCOMPLETE")

    semantic_event = {
        "protocol_version": event["protocol_version"],
        "previous_root": event["previous_root"],
        "epoch": event["epoch"],
        "candidate": event["candidate"],
        "approvals": [
            {"chamber": ch, "signer_id": s, "effective_domain": d}
            for ch, s, d in normalized
        ],
        "root_crypto": event["root_crypto"],
    }
    transition_hash = sha256_hex(canonical(semantic_event))
    next_root = sha256_hex(canonical({
        "previous_root": event["previous_root"],
        "transition_hash": transition_hash
    }))

    return {
        "verdict": "ACCEPT",
        "reason_code": "ACCEPT",
        "transition_hash": transition_hash,
        "next_trusted_root": next_root
    }
