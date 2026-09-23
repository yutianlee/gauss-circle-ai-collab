# Round 185 preapplication patch scope and path second-audit brief

- Campaign: m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate
- Role: second independent patch-scope, evidence-path, and inverse auditor
- Starting graph SHA-256:
  f16b7a43f8b0261671b39bdd4a59a3f06926cdfe3513d5910e56b89c6b1ab2e0
- State Patch SHA-256:
  2d4734c8a4b61acdd2081a4cad785ab56d05aac112c464935cf6916a3e9d6e4e
- Expected inventory: 1 create, 1 update, 0 correct, 20 reject,
  31 no_change
- Output: controls/preapply_scope_path_second_audit.md

Read `protocol.md`, the full starting graph, patch, adjudication,
synthesis, durable kernel, and three final reviews.  Verify hashes.
Without editing state, apply the patch in memory at Round 185 with the
adjudication as judge reference; run full graph validation; verify every
evidence path, dependency, protected ID, status, statement, implication,
blocker, parent, bridge, target, and exponent boundary.  Then remove the
created node and new rejected records, remove the one added dependency and
all added evidence, restore the exact prior next_action and metadata, and
require the canonical serialized graph to be byte-identical to the
starting graph.  Report the simulated patched graph hash and exact edge
delta.

Write one seven-section report only to the assigned output.  Return GREEN
only if every check passes; otherwise REPAIR with the first failure.  Do
not apply or edit the graph or any shared state.
