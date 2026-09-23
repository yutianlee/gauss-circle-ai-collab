# Conductor Round-197 post-application validation

- Campaign:
  `m9-m1-t1-p2-four-corner-allocation-commutator-gate`
- Round: 197
- Starting graph SHA-256:
  `b9b95784b097b3e30bed95f418ae14e57bf5f03a4a52975beeefa8db85b7f8ae`
- Primary applied graph SHA-256:
  `8192df329a85010676a01bf90d62901d810ae10265762186dd3eab17da7b32ae`
- Final graph SHA-256 after evidence hygiene:
  `8aea2ab5b088a0b29a434347ffc4509c70e79f53e450814920e3c83165a1ab69`
- Primary State Patch SHA-256:
  `a28050a9d157d7d956da336bbdead4296c88eb1b8a3defeb90495b1b37ca2068`
- Evidence-hygiene patch SHA-256:
  `1f9bacf52793fb93093135009e5bbe10f1e80ba5684b88b3af6bea758ba375ef`
- Declared primary footprint:
  1 create / 1 owner update / 0 correct / 22 reject / 28 no-change

## Result

PASS after one disclosed mechanical hygiene repair.

The production primary patch created only
`M9-M1-hard-top-t1-rho-large-P2-common-cell-allocation-commutator-sector`
and updated only
`M9-M1-hard-top-high-radical-small-t-residual-estimate`.  The new node is
`proved_internal`; the owner stays `open`.  The accepted Round-195 node,
all twenty-eight no-change nodes, every parent, M2 obligation, endpoint
statement, bridge, target, and exponent record remain protected.

The primary helper appended the judge reference to
`evidence.inconclusive` even though the validated create record already
classified that same adjudication as positive.  The first postapplication
scope audit correctly returned REPAIR.  A second mechanically validated
State Patch removed only that duplicate inconclusive classification.
The patch helper now suppresses this duplicate on future creates and
supports bucket-specific `evidence_removed`; two focused unit tests cover
both behaviors.

The final created-node buckets have 14 positive, 0 negative, and 11
inconclusive paths, with no duplicate inside a bucket and no pairwise
overlap.  The adjudication occurs only in positive evidence.

## Reverse, replay, and footprint

The final graph has 396 obligations and 1,797 rejected claims.  The
original 1,775 rejected records are an exact prefix, and the twenty-two
Round-197 records have the declared order, reasons, round, timestamp, and
adjudication provenance.

Independent inversion recovers the starting graph exactly at SHA-256
`b9b95784...`.  Replaying the primary patch at its historical timestamp
and then the single evidence-hygiene update reproduces the final object;
the only timestamp split is the created node's later hygiene timestamp.
All primary dependency and evidence suffixes are exact, and every
undeclared field is unchanged.

The final protected-scope verification passes at `8aea2ab5...`.  It also
confirms zero evidence-bucket overlap, no dependency cycle, unchanged
Round-195 provenance direction, and unchanged parent, bridge, target, and
exponent fields.

## Mathematical scope

The graph records only the strict physical common-cell theorem

\[
 |\mathscr R_{\rm core,out}^{\sigma}(P_{\rm cc}W)|
 +|\mathscr R_{\rm open,out}^{\sigma}(P_{\rm cc}W)|
 \ll L^2X^\varepsilon.
\]

The exact open complement remains

\[
\{\kappa<D_L,\ \min(Y,D_L)>H_B\mathfrak m\kappa\}
\cap(P_{\partial\rm lit}\dot\cup P_{s\rm f}\dot\cup P_{g\rm f}).
\]

No nonemptiness or density is claimed for \(P_{\rm cc}\).  The
four-corner conclusion is a mechanism no-go, not a lower bound or a
disproof of complete \(P_2\).

## Evidence

- `controls/postapply_independent_reverse_replay_audit.md`, SHA-256
  `9bc41c07adf2cbbdcd14c759c942b84fc9077053097f05e80fdf4e9c6f6bf347`;
- `controls/postapply_scope_protected_state_postrepair_verification.md`,
  SHA-256
  `214d073c8010ef41505b00ce2cde2a2cae2b9463001343dee8c7ac7868ae6623`;
- `reviews/conductor_round197_adjudication.md`, SHA-256
  `f9b9669a500ca3db760598c392da999aa458d6b5447fc4eef48bc109a41b17d7`;
- `synthesis.md`, SHA-256
  `124430b9605959ddcb9e63d69d6ee1062d43c0fab1c6f2d845d824ae11b6c9a8`.

## Closure decision

The graph mutation is mechanically valid and scope-safe.  Round 197 may
close under `p2_four_corner_orbit_boundary_self_return_no_go`.  Complete
\(P_2\), \(P_1\), original \(t=1\), every owner and parent, endpoint
uniformity, M9, both bridges, the quarter theorem, and every exponent
remain open, conditional, or unchanged.
