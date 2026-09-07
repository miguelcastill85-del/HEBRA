"""
HEBRA v0.6 — systemic dependency model.
Shows why separate accounts are not automatically independent trust domains.
"""
import itertools
CHAMBERS={
 "PROV":["P1","P2","P3"],"MEAS":["M1","M2","M3"],
 "METH":["T1","T2","T3"],"SAFE":["S1","S2","S3"]
}
def succeeds(signers):
    return all(sum(x in signers for x in xs)>=2 for xs in CHAMBERS.values())
def minimum_causes(causes):
    names=list(causes)
    for r in range(1,len(names)+1):
        for combo in itertools.combinations(names,r):
            s=set()
            for c in combo:s.update(causes[c])
            if succeeds(s):return r,combo
    return None,None
