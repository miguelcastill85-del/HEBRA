"""
HEBRA v0.5 root-trust minimum-cut model.
Structural defensive model; not a production security proof.
"""
GROUPS = {
  "provenance":3, "measurement":3, "methodology":3, "safety":3,
  "release_guardians":7, "builders":3, "release_auditors":3,
  "recovery_guardians":9, "recovery_auditors":5
}
THRESHOLDS = {
  "provenance":2, "measurement":2, "methodology":2, "safety":2,
  "release_guardians":4, "builders":2, "release_auditors":2,
  "recovery_guardians":5, "recovery_auditors":3
}
PATHS = {
  "FALSE_EVIDENCE_PROMOTION":["provenance","measurement","methodology","safety"],
  "MALICIOUS_KERNEL_RELEASE":["release_guardians","builders","release_auditors"],
  "EMERGENCY_ROOT_TAKEOVER":["recovery_guardians","recovery_auditors"]
}
def run():
    sizes={p:sum(THRESHOLDS[c] for c in cs) for p,cs in PATHS.items()}
    return {"path_sizes":sizes,"global_minimum":min(sizes.values()),
            "holds_candidate_BTR8":min(sizes.values())>=8}
if __name__=="__main__":
    import json
    print(json.dumps(run(),indent=2))
