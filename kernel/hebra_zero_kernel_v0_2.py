
"""
HEBRA ZERO v0.2 — reference kernel (educational prototype)

Security property demonstrated:
Untrusted submissions and invalid attestations cannot change the trusted root.

This is NOT a production cryptographic implementation and is not a proof that
external claims are true. It demonstrates the architecture/invariant.
"""

import json, hashlib
from dataclasses import dataclass, field
from typing import Dict, List, Set, Tuple

try:
    from cryptography.hazmat.primitives.asymmetric.ed25519 import (
        Ed25519PrivateKey, Ed25519PublicKey
    )
except Exception as e:
    raise RuntimeError("cryptography with Ed25519 support is required") from e


def canonical(obj) -> bytes:
    # Demonstration canonicalization. Production: RFC 8785 JCS.
    return json.dumps(
        obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


@dataclass(frozen=True)
class Attestation:
    claim_hash: str
    role: str
    key_id: str
    verdict: str
    signature_hex: str

    def signed_payload(self) -> bytes:
        return canonical({
            "claim_hash": self.claim_hash,
            "role": self.role,
            "key_id": self.key_id,
            "verdict": self.verdict
        })


@dataclass
class Policy:
    # Minimum positive signatures required for each heterogeneous role.
    thresholds: Dict[str, int]
    authorized_keys: Dict[str, Set[str]]
    policy_id: str = "hebra-zero-policy-v0.2"

    def digest(self) -> str:
        serializable = {
            "policy_id": self.policy_id,
            "thresholds": self.thresholds,
            "authorized_keys": {
                role: sorted(keys) for role, keys in sorted(self.authorized_keys.items())
            }
        }
        return sha256_hex(canonical(serializable))


class HebraZeroKernel:
    def __init__(self, policy: Policy, public_keys: Dict[str, Ed25519PublicKey]):
        self.policy = policy
        self.public_keys = public_keys

        # Untrusted ocean: content-addressed, no authority.
        self.inert_store: Dict[str, dict] = {}

        # Attestations remain evidence; invalid ones simply cannot authorize transitions.
        self.attestations: List[Attestation] = []

        # Append-only promoted event hashes. No arbitrary setter exists.
        self._promoted: List[str] = []

    def submit_inert(self, payload: dict) -> str:
        b = canonical(payload)
        h = sha256_hex(b)
        self.inert_store.setdefault(h, payload)
        return h

    def add_attestation(self, a: Attestation) -> None:
        self.attestations.append(a)

    def _valid_positive_attestations(self, claim_hash: str) -> Dict[str, Set[str]]:
        by_role: Dict[str, Set[str]] = {r: set() for r in self.policy.thresholds}

        for a in self.attestations:
            if a.claim_hash != claim_hash or a.verdict != "approve":
                continue
            if a.role not in self.policy.thresholds:
                continue
            if a.key_id not in self.policy.authorized_keys.get(a.role, set()):
                continue
            pub = self.public_keys.get(a.key_id)
            if pub is None:
                continue

            try:
                pub.verify(bytes.fromhex(a.signature_hex), a.signed_payload())
            except Exception:
                continue

            by_role[a.role].add(a.key_id)

        return by_role

    def promotion_ready(self, claim_hash: str) -> Tuple[bool, dict]:
        if claim_hash not in self.inert_store:
            return False, {"reason": "missing_claim"}

        by_role = self._valid_positive_attestations(claim_hash)
        deficits = {}

        for role, needed in self.policy.thresholds.items():
            have = len(by_role.get(role, set()))
            if have < needed:
                deficits[role] = {"have": have, "need": needed}

        return (len(deficits) == 0, {
            "policy_hash": self.policy.digest(),
            "deficits": deficits,
            "valid_signers": {r: sorted(v) for r, v in by_role.items()}
        })

    def promote(self, claim_hash: str) -> bool:
        ok, _ = self.promotion_ready(claim_hash)
        if not ok:
            return False
        if claim_hash not in self._promoted:
            self._promoted.append(claim_hash)
        return True

    def trusted_snapshot(self) -> dict:
        # Deterministic and derived only from promoted hashes + active policy.
        items = sorted(self._promoted)
        payload = {
            "policy_hash": self.policy.digest(),
            "resolver_version": "0.2",
            "promoted_claim_hashes": items,
        }
        return {
            "payload": payload,
            "trusted_root": sha256_hex(canonical(payload))
        }


def make_keypair():
    priv = Ed25519PrivateKey.generate()
    return priv, priv.public_key()


def sign_attestation(priv, claim_hash: str, role: str, key_id: str, verdict="approve"):
    unsigned = Attestation(
        claim_hash=claim_hash,
        role=role,
        key_id=key_id,
        verdict=verdict,
        signature_hex=""
    )
    sig = priv.sign(unsigned.signed_payload()).hex()
    return Attestation(
        claim_hash=claim_hash,
        role=role,
        key_id=key_id,
        verdict=verdict,
        signature_hex=sig
    )
