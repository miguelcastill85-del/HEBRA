---------------------------- MODULE HEBRA_ICC0_v0_3 ----------------------------
EXTENDS Naturals, Sequences, FiniteSets

(*
  HEBRA ICC-0 abstract model.
  Goal: unauthorized inputs may alter the inert ocean, never trusted state.
*)

CONSTANTS LegitClaim

VARIABLES promoted, inert, invalidAtt, policy

vars == <<promoted, inert, invalidAtt, policy>>

Init ==
    /\ promoted = {LegitClaim}
    /\ inert = 0
    /\ invalidAtt = 0
    /\ policy = "P0"

TrustedState == <<promoted, policy>>

SubmitUntrusted ==
    /\ inert' = inert + 1
    /\ UNCHANGED <<promoted, invalidAtt, policy>>

ForgeAttestation ==
    /\ invalidAtt' = invalidAtt + 1
    /\ UNCHANGED <<promoted, inert, policy>>

InjectPolicyAsData ==
    /\ inert' = inert + 1
    /\ UNCHANGED <<promoted, invalidAtt, policy>>

PromptInjection ==
    /\ inert' = inert + 1
    /\ UNCHANGED <<promoted, invalidAtt, policy>>

SybilDuplicate ==
    /\ inert' = inert + 1
    /\ UNCHANGED <<promoted, invalidAtt, policy>>

Next ==
    \/ SubmitUntrusted
    \/ ForgeAttestation
    \/ InjectPolicyAsData
    \/ PromptInjection
    \/ SybilDuplicate

Spec == Init /\ [][Next]_vars

ICC0 ==
    promoted = {LegitClaim} /\ policy = "P0"

=============================================================================
