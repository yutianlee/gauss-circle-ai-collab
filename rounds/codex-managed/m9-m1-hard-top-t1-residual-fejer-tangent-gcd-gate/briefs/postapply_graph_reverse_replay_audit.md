# Round 185 postapplication graph reverse and replay audit brief

- Campaign: m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate
- Role: independent postapplication graph, inverse, and frozen-time replay auditor
- Starting graph SHA-256:
  f16b7a43f8b0261671b39bdd4a59a3f06926cdfe3513d5910e56b89c6b1ab2e0
- Applied graph SHA-256:
  f43248060d7876a96d4554cd13372dbf267387bcbe44a832b87cd5f571801575
- Application timestamp: 2026-08-28T02:16:28
- State Patch SHA-256:
  2d4734c8a4b61acdd2081a4cad785ab56d05aac112c464935cf6916a3e9d6e4e
- Judge reference:
  rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/reviews/conductor_round185_adjudication.md
- Expected inventory: 1/1/0/20/31
- Output: controls/postapply_independent_graph_reverse_audit.md

Read `protocol.md`, the actual graph, patch, preapply reverse audit,
adjudication, synthesis, durable kernel, and final kernel reviews.  Verify
all frozen hashes.  Audit the actual graph delta and operation inventory,
all created/updated/rejected records, evidence and judge-reference fields,
dependency direction, references, SCCs, and complete protected scope.

Construct the exact inverse in memory and require canonical byte-identical
recovery of the starting graph and its SHA-256.  Separately reapply the
frozen patch to that recovered starting graph at exactly
2026-08-28T02:16:28 with Round 185 and the stated judge reference, and
require canonical byte-identical reproduction of the actual applied graph
and SHA-256.  Do not modify any shared state.

Write one seven-section report only to the assigned output.  Return GREEN
only if actual delta, inverse, replay, graph validation, scope, and exponent
quarantine all pass; otherwise REPAIR with the first failing item.
