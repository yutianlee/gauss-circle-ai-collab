# Post-apply scope and protected-state audit

- Campaign: `m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate`
- Round: 196
- Role: independent hostile post-apply protected-scope audit
- Starting graph SHA-256: `f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`
- State Patch SHA-256: `013eae5d57e3854acf2ef9d4c9d72ab94fa9da2af64e97f27b43c701cdeb7c9d`
- Live post-apply graph SHA-256: `b9b95784b097b3e30bed95f418ae14e57bf5f03a4a52975beeefa8db85b7f8ae`
- Verdict: **PASS**

## 1. Result

**Exact post-apply scope lemma.**  The live proof graph is exactly the
declared Round-196 State Patch applied to the graph at the declared starting
SHA-256, including the application evidence reference.  Relative to the
starting graph:

1. the proof-obligation set remains the same 395 records;
2. exactly two obligation records changed, namely
   `M9-M1-hard-top-high-radical-small-t-residual-estimate` and
   `M9-M1-hard-top-t1-rho-large-P2-absolute-capacity-sectors`;
3. each changed record differs only in `evidence`, `next_action`,
   `last_updated_round`, and `last_updated_at`;
4. every obligation's `status`, `dependencies`, `statement_tex`, `implies`,
   `blockers`, and `type` remains unchanged;
5. exactly 20 new rejected-claim records were appended in patch order, with
   the exact patch reasons, round 196 metadata, and the adjudication evidence
   reference; no earlier rejected-claim record changed;
6. all 27 `no_change` obligation objects are exactly unchanged; and
7. endpoint/M9 parents, both bridges, the internal (1/3) theorem, the
   external (0.3144831759740614\ldots) benchmark, and the (1/4) target
   retain their starting statuses, dependencies, and statements.

No repair or rollback is required.

## 2. Exact statement and hypotheses

The audit compares these exact objects:

1. the live `state/proof_obligations.yml` at SHA-256
   `b9b95784b097b3e30bed95f418ae14e57bf5f03a4a52975beeefa8db85b7f8ae`;
2. the current Round-196 `state_patch.json` at SHA-256
   `013eae5d57e3854acf2ef9d4c9d72ab94fa9da2af64e97f27b43c701cdeb7c9d`;
3. the patch-declared starting graph SHA-256
   `f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`;
   and
4. the repository's checked graph serialization, patch-application, and graph
   validation semantics in `math_collab/proof_obligations.py`.

Because no separate starting-graph copy is needed, the comparison is made by
an exact inverse reconstruction: delete precisely the 20 patch rejection IDs,
remove precisely each patch-added inconclusive evidence path from the two
updated nodes, and restore their recorded prior `next_action` and update
metadata.  The resulting object is serialized by the repository's
`dump_graph`.  Equality of its raw SHA-256 with the declared starting hash
certifies the full starting object, not merely selected fields.

## 3. Proof or derivation

### 3.1. Exact reverse reconstruction

The live graph contains 395 obligations and 1,775 rejected claims.  Reversing
only the State Patch operations yields 395 obligations and 1,755 rejected
claims.  Repository serialization of that reconstructed graph has raw
SHA-256

`f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`,

exactly the patch-declared starting graph hash.  Both the live graph and the
reconstructed starting graph pass `validate_graph` with zero issues.

This exact hash recovery excludes any undisclosed change elsewhere in the
graph: if an unrelated field, record order, obligation, rejection, or
top-level graph object had changed, reversal of only the declared patch
operations would not reproduce the starting file hash.

### 3.2. The two changed obligation records

Comparing the live obligations to the exactly reconstructed starting
obligations produces exactly two changed IDs and no created or removed ID.

| Obligation | Starting status | Exact changed fields | Patch conformance |
|---|---:|---|---|
| `M9-M1-hard-top-high-radical-small-t-residual-estimate` | `open` | `evidence`, `next_action`, `last_updated_round`, `last_updated_at` | the 24 inconclusive paths occur exactly once and in patch order; `next_action` equals the patch; metadata is round 196 at `2026-08-30T12:00:58` |
| `M9-M1-hard-top-t1-rho-large-P2-absolute-capacity-sectors` | `proved_internal` | `evidence`, `next_action`, `last_updated_round`, `last_updated_at` | the 24 inconclusive paths occur exactly once and in patch order; `next_action` equals the patch; metadata is round 196 at `2026-08-30T12:00:58` |

For each node, `status`, `dependencies`, `statement_tex`, `implies`,
`blockers`, and `type` compare exactly equal to the reconstructed starting
record.  The same comparison over all 395 obligations is exact.  The
canonical diagnostic SHA-256 of the global map of statuses, dependencies,
statements, implications, and blockers is
`42e4a73b4059e5cd4e174dae842a6a44eb37b7a23bc6431acb9412e5f6fbd009`
for both starting and live graphs.  Therefore the apply performed no
promotion, demotion, dependency edit, statement edit, or hidden owner change.

### 3.3. The 20 appended rejected-claim records

Each of the 20 patch rejection IDs occurs exactly once in the live graph.
They are exactly the final 20 records, in patch order.  Every `reason` equals
the corresponding patch reason.  Every record has exactly the fields
`id`, `reason`, `last_updated_at`, `last_updated_round`, and `evidence`, with

- `last_updated_round: 196`;
- `last_updated_at: 2026-08-30T12:00:58`; and
- the sole evidence entry
  `rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/reviews/conductor_round196_adjudication.md`.

The first 1,755 live rejected-claim records are exactly the reconstructed
starting list.  Their canonical diagnostic SHA-256 is
`00119e20ae0f974ee3ce6304dc94aa4992ca8bed51a541420ad41bae5aec005e`
on both sides.  Thus the operation is a 20-record append, not a correction,
replacement, duplicate insertion, or obligation-status rejection.

### 3.4. All 27 `no_change` objects and protected frontier

All 27 IDs are present, distinct, and complete-object equal between the
reconstructed starting graph and the live graph:

| Protected group | Exact IDs |
|---|---|
| Accepted hard-(t=1) reductions | `M9-M1-hard-top-t1-rho-large-gcd-scaled-close-sector`; `M9-M1-hard-top-t1-rho-large-farey-covector-reduction`; `M9-M1-hard-top-t1-fast-signed-inverse-transport-reduction`; `M9-M1-hard-top-t1-high-h-dual-frequency-projective-reduction`; `M9-M1-hard-top-t1-high-h-imprimitive-lift-gcd-reduction`; `M9-M1-hard-top-t1-high-h-inverse-residue-conductor-reduction`; `M9-M1-hard-top-t1-residual-fejer-tangent-gcd-reduction`; `M9-M1-hard-top-t1-comparable-factor-exchange-sector`; `M9-M1-hard-top-small-t-nonresonant-primitive-ray-sector`; `M9-M1-hard-top-squarefree-radical-sector-reduction` |
| M1 parents and owner | `M9-M1-top-endpoint-signed-cone`; `M9-M1-direct-smooth-residual-blockwise-estimate`; `M9-M1-physical-one-count-assembly`; `M9-M1-global-angular-radial-estimate`; `M9-M1` |
| M2 parents and owner | `M9-M2-top-endpoint-signed-cone`; `M9-M2-smooth-balanced-quarter-packet-estimate`; `M9-M2-smooth-unbalanced-three-quarter-estimate`; `M9-M2` |
| Endpoint/global owner | `M9-endpoint-uniformity`; `M9` |
| Bridges, exponents, target, and elementary support | `Conditional-bridge`; `GC-global-M1-alternative-bridge`; `GC-partial-one-third`; `GC-external-Li-Yang-theta-star`; `GC-target`; `Divisor-bound-elementary` |

The canonical diagnostic SHA-256 of these 27 complete records is
`c2d13675f34c4caf2e50da1d4478b51e77eca82c6ee4cc7ba835c4ff1aca09a4`
for both starting and live graphs.

The especially sensitive frontier records remain:

| Record | Live status | Protected conclusion |
|---|---|---|
| `M9-endpoint-uniformity` | `open` | endpoint uniformity is not promoted |
| `M9` | `open` | still depends on `H1-H3`, `H4`, `R5-Full`, `M9-M1`, and `M9-M2` |
| `Conditional-bridge` | `derived_under_assumptions` | still depends on complete `M9` |
| `GC-global-M1-alternative-bridge` | `derived_under_assumptions` | alternative bridge dependencies unchanged |
| `GC-partial-one-third` | `proved_internal` | statement remains (P(X)\ll_\varepsilon X^{1/3+\varepsilon}) |
| `GC-external-Li-Yang-theta-star` | `proved_external_dependency` | statement retains (0.3144831759740614\ldots) |
| `GC-target` | `open` | target remains (P(X)\ll_\varepsilon X^{1/4+\varepsilon}) via `Conditional-bridge` |
| `Divisor-bound-elementary` | `proved_internal` | elementary support lemma unchanged |

The canonical diagnostic SHA-256 of these eight complete records is
`8f95e1d4802b6b21c0e09b39497e14a22226aad052d9da1c2b6754724befc354`
for both starting and live graphs.  The bridge, target, and exponent
quarantine is exact.

## 4. First doubtful or unproved step

There is no doubtful or unproved state mutation: exact inverse reconstruction
recovers the starting graph's raw hash, and the forward delta matches every
patch field and application metadata field.

The first unproved mathematical step remains outside this state audit: a
coefficient-sensitive joint (++,+-,-+,--) estimate for the complete literal
open (P_2) region before positive norms.  Neither the patch nor the live
graph claims it.  A future edit to the live graph, patch, or application code
would require a fresh audit; this verdict is tied to the hashes above.

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| Live graph validation | PASS: repository validator reports `Graph OK`; direct validation has zero issues. |
| Exact reverse reconstruction | PASS: reversing only patch operations reproduces the declared starting raw SHA-256. |
| Obligation cardinality and identity | PASS: 395 before and after; no obligation created or removed. |
| Exact obligation diff | PASS: exactly the two patch update IDs differ. |
| Allowed-field restriction | PASS: only evidence, next action, and round/time metadata differ on those two nodes. |
| Evidence payload | PASS: exactly 24 fresh inconclusive paths per node, each once and in patch order. |
| Status/dependency/statement quarantine | PASS: all 395 records agree globally, including implications, blockers, and types. |
| Rejected-claim append | PASS: exactly 20 final records, exact IDs/order/reasons, round metadata, and adjudication evidence. |
| Existing rejected-claim protection | PASS: the original 1,755-record prefix is exactly unchanged. |
| All 27 `no_change` objects | PASS: complete-object equality for every declared ID. |
| Exponent/bridge/target protection | PASS: statuses, dependencies, and statements remain exact. |
| Reconstructed graph validation | PASS: zero issues. |

The comparisons and hashes are deterministic structural diagnostics only;
they provide no numerical or asymptotic theorem evidence.

## 6. Dependencies and exact artifacts used

1. `protocol.md`, SHA-256
   `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`.
2. Live `state/proof_obligations.yml`, SHA-256
   `b9b95784b097b3e30bed95f418ae14e57bf5f03a4a52975beeefa8db85b7f8ae`.
3. `state/active_campaign.yml`, SHA-256
   `8aa8f0dea94adc77f6e3e4dbc8a2b43c3a6749aefe7f95c37be0c3867e85dfab`.
4. `rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/state_patch.json`,
   SHA-256
   `013eae5d57e3854acf2ef9d4c9d72ab94fa9da2af64e97f27b43c701cdeb7c9d`.
5. `proofs/kernels/m9_m1_hard_top_t1_p2_on_shell_carrier_normalization_self_return.md`,
   SHA-256
   `51da98a07b52706a510f9ea07c52d952323e8282cb3ab6e100347c71b63f54fb`.
6. `math_collab/proof_obligations.py`, SHA-256
   `384070a83b4ce1f56ebdceb0711680a6e889d4d43af3a40a8b6002319114a437`.
7. `math_collab/validate_state_patch.py`, SHA-256
   `cfa914c54bfa172cc94354dc7e904e866d4e69c96cd8be7bfbf68b5a295080e8`.
8. `rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/reviews/conductor_round196_adjudication.md`,
   SHA-256
   `e760c0685789b583e16787fa812320faf608d16775f1abee78d38a610e7ce90d`.
9. `rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/controls/preapply_hostile_scope_protected_state_audit.md`,
   SHA-256
   `77aaa5647716ceb624ccd033d4c49755d1d82a2c58703b351b3d4b795a404553`.

No web source or theorem computation was used.

## 7. Recommended state effect

**Retain the live graph exactly as applied.**  The application is
scope-correct and reversible:

1. retain the two route-boundary evidence and `next_action` updates;
2. retain the 20 append-only rejected-claim records;
3. make no corrective update to any obligation status, dependency, statement,
   implication, blocker, type, bridge, exponent, endpoint parent, or target;
4. make no change to any of the 27 protected `no_change` objects.

Recommended disposition: **PASS; no state repair and no theorem promotion.**
