"""
HEBRA v0.8 — candidate table-driven resolver for differential testing.

This is a second prototype implementation style, not an independently audited
production implementation.
"""
import json, hashlib, re
ROOMS = ["PROV","MEAS","METH","SAFE"]
H64 = re.compile("^[0-9a-f]{64}$")

def _hash(x):
    b=json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
    return hashlib.sha256(b).hexdigest()

def _no(code):
    return {"verdict":"REJECT","reason_code":code,
            "transition_hash":None,"next_trusted_root":None}

def evaluate(e):
    if not isinstance(e,dict) or set(e)!={"protocol_version","previous_root","epoch","candidate","approvals","root_crypto"}:
        return _no("SCHEMA_TOP")
    if not isinstance(e["candidate"],dict) or set(e["candidate"])!={"id","payload_hash"}:
        return _no("SCHEMA_CANDIDATE")
    if not isinstance(e["approvals"],list):
        return _no("SCHEMA_APPROVALS")
    if not isinstance(e["root_crypto"],dict) or set(e["root_crypto"])!={"suite_a_valid","suite_b_valid"}:
        return _no("SCHEMA_CRYPTO")
    if any(not isinstance(a,dict) or set(a)!={"chamber","signer_id","effective_domain"} for a in e["approvals"]):
        return _no("SCHEMA_APPROVAL_ITEM")
    if e["protocol_version"]!="0.8": return _no("INVALID_VERSION")
    if not isinstance(e["previous_root"],str) or not H64.fullmatch(e["previous_root"]): return _no("INVALID_PREVIOUS_ROOT")
    if isinstance(e["epoch"],bool) or not isinstance(e["epoch"],int) or e["epoch"]<0: return _no("INVALID_EPOCH")

    c=e["candidate"]
    if not isinstance(c["id"],str) or not 1<=len(c["id"])<=128 or not isinstance(c["payload_hash"],str) or not H64.fullmatch(c["payload_hash"]):
        return _no("INVALID_CANDIDATE")

    rows=[]
    for a in e["approvals"]:
        if a["chamber"] not in ROOMS or not isinstance(a["signer_id"],str) or not a["signer_id"] or not isinstance(a["effective_domain"],str) or not a["effective_domain"]:
            return _no("INVALID_APPROVAL")
        rows.append((a["chamber"],a["signer_id"],a["effective_domain"]))
    rows=sorted(set(rows))

    room={r:[] for r in ROOMS}
    for r,s,d in rows: room[r].append((s,d))
    if any(len({s for s,_ in room[r]})<2 or len({d for _,d in room[r]})<2 for r in ROOMS):
        return _no("MISSING_CHAMBER_QUORUM")

    where={}
    for r,s,d in rows: where.setdefault(d,set()).add(r)
    if any(len(v)>1 for v in where.values()):
        return _no("CROSS_CHAMBER_DEPENDENCY")

    if e["root_crypto"]["suite_a_valid"] is not True or e["root_crypto"]["suite_b_valid"] is not True:
        return _no("ROOT_CRYPTO_INCOMPLETE")

    normalized={
        "protocol_version":e["protocol_version"],"previous_root":e["previous_root"],
        "epoch":e["epoch"],"candidate":e["candidate"],
        "approvals":[{"chamber":r,"signer_id":s,"effective_domain":d} for r,s,d in rows],
        "root_crypto":e["root_crypto"]
    }
    th=_hash(normalized)
    nr=_hash({"previous_root":e["previous_root"],"transition_hash":th})
    return {"verdict":"ACCEPT","reason_code":"ACCEPT",
            "transition_hash":th,"next_trusted_root":nr}
