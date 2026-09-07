# HEBRA Threat Model v0.1

## Security goals
1. A completed result cannot silently rewrite its preregistered success criteria.
2. Unverified records cannot gain the same influence as independently verified replications.
3. A coordinated group of accounts cannot cheaply dominate recommendations.
4. Private raw context is not required for public aggregation.
5. Every recommendation can be traced to records, transformations, model/software versions, and contradictions.
6. High-risk domains cannot silently inherit the automation rules of low-risk domains.

## Principal adversaries
- Sybil farm creating fabricated successes.
- Vendor or organization manufacturing favorable evidence.
- Insider altering historical records.
- Model/data poisoning attacker.
- Curious analyst trying to re-identify participants.
- Well-meaning user producing biased or incomplete measurements.
- Compromised software agent generating invalid transformations.

## Mandatory controls in v0.1
- Preregistered locked fields and commitment hash.
- Append-only transparency-log receipt before a result can reach `verified`.
- Evidence independence tracked separately from user reputation.
- New sources enter quarantine; anomaly and cluster checks precede aggregation.
- Contradictions are first-class records and cannot be deleted by a favorable result.
- Raw sensitive context defaults to local-only or encrypted private storage.
- Public statistics require minimum cohort size and a privacy review; differential privacy is optional in v0.1 but budget fields are reserved.
- R0/R1 may be automatically recommended; R2+ requires a domain-specific governance profile and human review.
- AI-generated text is never treated as evidence merely because an AI generated it.
- Recommendation output must expose uncertainty, adverse outcomes, transferability, and provenance.

## Kill switches
HEBRA must suspend a recommendation family when:
- a severe/critical adverse event is plausibly linked to it;
- poisoning or coordinated manipulation is detected;
- contradiction rate crosses a domain-defined threshold;
- provenance/integrity checks fail;
- transferability to the current context is below the minimum threshold;
- the system cannot distinguish correlation from intervention effect sufficiently for the requested decision.
