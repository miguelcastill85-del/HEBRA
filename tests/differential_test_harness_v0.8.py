"""
HEBRA v0.8 — differential + vector + metamorphic test harness.

It compares the executable specification oracle with the candidate resolver.
It also contains one deliberately buggy evaluator to prove that the harness
actually detects semantic differences.
"""
import json, copy, importlib.util, pathlib

HERE = pathlib.Path(__file__).resolve().parent

def load(name, filename):
    spec=importlib.util.spec_from_file_location(name,HERE/filename)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

oracle=load("oracle","executable_spec_core_v0.8.py")
candidate=load("candidate","candidate_table_resolver_v0.8.py")

def load_json(filename):
    return json.loads((HERE/filename).read_text(encoding="utf-8"))

def buggy_evaluate(event):
    out=candidate.evaluate(event)
    if out["reason_code"]=="MISSING_CHAMBER_QUORUM":
        return {"verdict":"ACCEPT","reason_code":"BUG_ACCEPT",
                "transition_hash":"bug","next_trusted_root":"bug"}
    return out

def run():
    vectors=load_json("golden_vectors_v0.8.json")+load_json("negative_vectors_v0.8.json")
    candidate_mismatches=[]
    buggy_mismatches=[]
    expected_mismatches=[]

    for v in vectors:
        oracle_out=oracle.evaluate(v["event"])
        cand_out=candidate.evaluate(v["event"])
        bug_out=buggy_evaluate(v["event"])

        if oracle_out!=v["expected"]:
            expected_mismatches.append(v["name"])
        if cand_out!=oracle_out:
            candidate_mismatches.append(v["name"])
        if bug_out!=oracle_out:
            buggy_mismatches.append(v["name"])

    base=load_json("golden_vectors_v0.8.json")[0]["event"]
    base_out=oracle.evaluate(base)
    metamorphic={}

    x=copy.deepcopy(base); x["approvals"]=list(reversed(x["approvals"]))
    metamorphic["approval_order_invariant"] = oracle.evaluate(x)==base_out

    x=copy.deepcopy(base); x["approvals"].append(copy.deepcopy(x["approvals"][0]))
    metamorphic["exact_duplicate_invariant"] = oracle.evaluate(x)==base_out

    x=copy.deepcopy(base); x["approvals"].pop()
    metamorphic["remove_required_approval_rejects"] = oracle.evaluate(x)["verdict"]=="REJECT"

    x=copy.deepcopy(base); x["candidate"]["payload_hash"]="2"*64
    xo=oracle.evaluate(x)
    metamorphic["payload_change_changes_root"] = (
        xo["verdict"]=="ACCEPT" and xo["next_trusted_root"]!=base_out["next_trusted_root"]
    )

    x=copy.deepcopy(base); x["unknown"]=1
    metamorphic["unknown_field_rejects"] = oracle.evaluate(x)["reason_code"]=="SCHEMA_TOP"

    return {
        "vector_count":len(vectors),
        "oracle_expected_mismatches":expected_mismatches,
        "candidate_vs_oracle_mismatches":candidate_mismatches,
        "deliberately_buggy_mismatches":buggy_mismatches,
        "metamorphic":metamorphic,
        "all_candidate_checks_pass":(
            not expected_mismatches and not candidate_mismatches and all(metamorphic.values())
        ),
        "harness_detected_bug":bool(buggy_mismatches)
    }

if __name__=="__main__":
    print(json.dumps(run(),indent=2))
