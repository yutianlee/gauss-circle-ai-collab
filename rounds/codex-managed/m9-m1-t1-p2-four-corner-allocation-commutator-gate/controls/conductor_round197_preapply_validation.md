# Conductor Round-197 preapply validation

- Starting graph SHA-256:
  `B9B95784B097B3E30BED95F418AE14E57BF5F03A4A52975BEEEFA8DB85B7F8AE`
- Final State Patch SHA-256:
  `A28050A9D157D7D956DA336BBDEAD4296C88EB1B8A3DEFEB90495B1B37CA2068`
- Final candidate SHA-256:
  `285EA0975EB3D48691FFB27B5A83E251D33A68062EB4D14DD54972F6AF6296C0`
- Durable kernel SHA-256:
  `6CAF8DC3A027A4548C7059546F117868B45CE51C23F05A5148B78AA995415467`
- Intended operations: 1 create / 1 update / 0 corrected rejection /
  22 reject / 28 no change

## Result

PASS.  The repository State-Patch validator accepts the patch against the
exact live starting graph.  Independent in-memory application produces no
graph issue.  The only changed pre-existing obligation is the still-open
`M9-M1-hard-top-high-radical-small-t-residual-estimate`; one subordinate
common-cell node is created.  The accepted Round-195 node is byte-for-byte
unchanged and is explicitly protected by the no-change list.

The declared inverse removes the created node and rejected suffix, removes
the added owner dependency and 25-path evidence suffix, and restores the
owner action and metadata.  It recovers the exact parsed starting graph.
Replay is exact after ignoring only the applicator's wall-clock timestamp.
The original rejected-claim prefix is preserved.

All 25 evidence paths exist and are unique.  The created node has 14 positive,
0 negative, and 11 inconclusive paths.  The owner receives the same 25 paths
once as inconclusive strict-sector evidence.  The corrected theorem statement
matches the kernel's arithmetic, support, and zero-extension dead-code rule.
No computation is theorem evidence.

The six repository unit tests pass, Python bytecode compilation passes,
campaign validation passes, and the active campaign and plan remain
structurally equal after mechanical LF normalization of the generated plan
and three briefs.

Independent audits:

1. `controls/preapply_independent_reverse_replay_audit.md`: GREEN;
2. `controls/preapply_hostile_graph_scope_protection_audit.md`: GREEN;
3. `controls/preapply_evidence_power_hygiene_audit.md`: GREEN.

The patch introduces no new graph cycle.  All 28 declared protected objects,
including the Round-195 ancestor, every parent, M2, endpoint uniformity, M9,
both bridges, the external benchmark, and the target are unchanged.  The
internal \(1/3\), accepted external
\(0.3144831759740614\ldots\), and target \(1/4\) exponent records are
quarantined.

The patch is approved for mechanical application at Round 197 with
`reviews/conductor_round197_adjudication.md` as the judge reference.
