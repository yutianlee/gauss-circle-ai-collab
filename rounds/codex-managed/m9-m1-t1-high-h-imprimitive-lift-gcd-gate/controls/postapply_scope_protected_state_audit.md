# Round 188 postapplication protected-scope and reverse/replay audit

## 1. Result / verdict

**Verdict: GREEN. First defect: none.**

The live graph is canonical JSON, 2,052,996 bytes, and has the required
SHA-256

`338060b37c19d849053078e5f6a7775c45c626a16b6f9198fafdf9bb4a62265c`.

It realizes exactly the Round-188 State Patch at SHA-256
`5198860aa96b484e46a2e9efd1cd5a89d99435295f237ff5c82adcaa731a6c00`
against starting graph
`be0eca9ca93c3534cca958d70b5541d03d28ff993ebfbcbca6be3cd393fae5ff`,
using application timestamp `2026-08-29T17:36:08` and the current
Round-188 adjudication as judge reference.

The realized inventory is exactly

`(create, update, correct_rejected, reject, no_change) = (1, 1, 0, 15, 21)`.

There is one appended proved subordinate obligation, one still-open owner
whose five authorized fields changed, and the exact 15-record rejection
suffix. All 21 no-change objects are identical to their reconstructed
starting objects. Every inherited status, statement, implication, blocker,
and owner field is unchanged. Dependency direction and SCC confinement are
correct, and all 20 evidence/judge paths resolve at their current hashes.

The operation-derived inverse produces the canonical 2,038,519-byte starting
graph at its exact hash. Reapplying with the actual timestamp and judge path
reproduces the live graph byte-for-byte at `338060b3...265c`. The audit used
only in-memory copies and did not write shared state.

## 2. Exact claim and hypotheses

The live graph is compared with the exact inverse of the frozen patch, not
with a prose reconstruction. The official applicator semantics are used with

- `round_index = 188`;
- `last_updated_at = 2026-08-29T17:36:08`; and
- judge reference
  `rounds/codex-managed/m9-m1-t1-high-h-imprimitive-lift-gcd-gate/reviews/conductor_round188_adjudication.md`.

The only created ID must be

`M9-M1-hard-top-t1-high-h-imprimitive-lift-gcd-reduction`.

It must be the final obligation, have status `proved_internal`, depend
directly and only on
`M9-M1-hard-top-t1-high-h-inverse-residue-conductor-reduction` and
`Divisor-bound-elementary`, and have no implication or blocker.

The only updated inherited ID must be

`M9-M1-hard-top-high-radical-small-t-residual-estimate`.

Its changed fields are permitted to be exactly `dependencies`, `evidence`,
`next_action`, `last_updated_round`, and `last_updated_at`. Its status,
statement, implications, blockers, and owner must remain unchanged, and its
status must remain `open`.

The 15 declared rejection IDs must form the exact new rejected-claim suffix,
with the patch reasons, Round-188 metadata, actual timestamp, and current
adjudication evidence. Every one of the 21 declared no-change IDs must be
object-identical across the inverse comparison.

The mathematical scope is subordinate only: the strict `Qm >= Y`
imprimitive-lift packet is proved, while the exact one-outer-real-part
`Qm < Y` complement, the complete high-height relation, the original
`t = 1` residual, every owner, parent, bridge, theorem, and exponent remain
open or retain their previous status.

## 3. Checks / proof

### Exact live realization

The live counts are 390 obligations and 1,629 rejected claims, versus 389 and
1,614 after exact inverse. The final obligation is the declared new node. Its
fields equal the patch create record exactly, with only the applicator's
`last_updated_round = 188` and actual `last_updated_at` added. Its evidence is
exactly:

- 16 positive paths from the patch;
- no negative path; and
- the four patch-inconclusive paths followed by the adjudication judge
  reference, for five inconclusive paths total.

The live owner remains `open`. Its new subordinate dependency is present
exactly once and is the final dependency. Its 18 new inconclusive evidence
paths form the exact appended suffix. Its narrowed next action equals the
patch value, and its metadata equal Round 188 and the actual timestamp.

The final 15 rejected-claim records have the exact declared IDs in patch
order. Each record consists of its declared reason, Round 188, timestamp
`2026-08-29T17:36:08`, and the one-element adjudication evidence list. No
earlier rejected claim changes.

### Exact inverse and inherited diff

The inverse removes the final obligation and rejection suffix, removes the
one added owner dependency and 18 evidence values, and restores the patch's
recorded next action and metadata. The reverse record matches the recovered
owner literally:

- `last_updated_round = 187`;
- `last_updated_at = 2026-08-29T15:59:13`; and
- a 654-byte prior `next_action` with SHA-256
  `d19c58a021d5ef9161b5c92ff38465fab918bcfd53ab90f717779ae472e9693a`.

The resulting canonical bytes have SHA-256
`be0eca9ca93c3534cca958d70b5541d03d28ff993ebfbcbca6be3cd393fae5ff`.
Both the inverse graph validator and the patch validator return no issue.

Comparing all 389 reconstructed inherited obligations with the live graph,
the only unequal object is the named hard-M1 small-`t` owner. Its unequal
fields are exactly:

1. `dependencies`;
2. `evidence`;
3. `last_updated_at`;
4. `last_updated_round`; and
5. `next_action`.

All 21 no-change objects are equal. Every other top-level graph value is
equal. For every inherited obligation, including the updated owner, the
fields `status`, `statement_tex`, `implies`, `blockers`, and `owner` are
equal.

### Edges and cycle safety

Dependency edges change from 1,385 to 1,388. The additions are exactly:

1. the still-open owner to the new subordinate node;
2. the new node to the accepted Round-187 inverse-residue reduction; and
3. the new node to `Divisor-bound-elementary`.

There is no removed dependency. Implication edges remain exactly 326 and
blocker edges exactly 70, with no set delta. All relationship targets resolve.

The dependency graph retains the same three inherited nontrivial SCCs, each
of size two. The new obligation is a singleton SCC and has exactly one
incoming dependency edge, from the still-open owner. Hence no new dependency
cycle or reversed prerequisite direction is present.

### Protected owner, theorem, and exponent scope

A broad protected-family comparison covers 372 inherited M9-, bridge-, and
GC-labelled IDs. Every such object is identical except for the five authorized
fields of the one open owner. In particular:

| Node | Live and starting status |
|---|---|
| `M9-M1` | `open` |
| `M9-M2` | `open` |
| `M9-endpoint-uniformity` | `open` |
| `M9` | `open` |
| `Conditional-bridge` | `derived_under_assumptions` |
| `GC-global-M1-alternative-bridge` | `derived_under_assumptions` |
| `GC-partial-one-third` | `proved_internal` |
| `GC-external-Li-Yang-theta-star` | `proved_external_dependency` |
| `GC-target` | `open` |

Their statements, dependencies, implications, blockers, and owners are
unchanged. Thus neither internal exponent one third, the external
`0.3144831759740614...` benchmark, nor the target exponent one quarter moves.
The created node has empty implication and blocker lists, so it supplies no
hidden promotion edge.

### Actual-time replay

The official applicator was run on the inverse graph with the actual timestamp,
Round 188, and the current adjudication path. The resulting object equals the
parsed live object, and its canonical serialization equals the live raw bytes.
Its SHA-256 is exactly
`338060b37c19d849053078e5f6a7775c45c626a16b6f9198fafdf9bb4a62265c`.

## 4. First doubtful or unproved step

There is no doubtful application, path, scope, inverse, or replay step.

The first mathematical step remains exactly `188.K12`: obtain the jointly
signed actual-coefficient estimate for the literal `Qm < Y` complement and
recover the full factor `Y` before positive recombination. The available
positive estimate remains only `O_epsilon(Y L^2 X^epsilon)`. The live new-node
statement and the still-open owner's next action retain this deficit; no
completion, reciprocity, determinant, sieve, or positive-energy control is
promoted into a disproof or a substitute estimate.

Residual uncertainty is limited to future mutation: this audit binds the live
graph, patch, and evidence bytes at the hashes recorded here. Any later byte
change requires a new hash-bound audit.

## 5. Controls and outcomes

| Control | Outcome |
|---|---|
| live graph identity and canonical serialization | **PASS:** 2,052,996 bytes, `338060b3...265c` |
| patch identity and realized counts | **PASS:** `5198860a...6c00`, exact `1/1/0/15/21` |
| official live graph validation | **PASS:** zero issues |
| appended proved subordinate node | **PASS:** exact create record plus actual metadata |
| still-open owner delta | **PASS:** exactly five authorized fields |
| rejected-claim suffix | **PASS:** exact 15 IDs, reasons, timestamp, round, and judge evidence |
| 21 no-change objects | **PASS:** all object-identical |
| evidence/judge paths | **PASS:** 20 distinct current paths, all existing and nonempty |
| current-hash provenance connector | **PASS:** `1c01697f...a17c` |
| dependency and SCC delta | **PASS:** three forward edges, no new cycle |
| implication and blocker sets | **PASS:** exactly unchanged |
| inherited status/statement/owner scope | **PASS:** no drift |
| M9, bridge, GC, and exponent quarantine | **PASS:** all protected objects retain scope |
| operation-derived inverse | **PASS:** exact canonical starting hash `be0eca9c...e5ff` |
| actual-time official replay | **PASS:** byte-equal live graph `338060b3...265c` |
| shared-state nonmutation by auditor | **PASS:** all simulations were in memory |

## 6. Dependencies and hashes

Core inputs and controls:

| Artifact | SHA-256 |
|---|---|
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| reconstructed starting graph | `be0eca9ca93c3534cca958d70b5541d03d28ff993ebfbcbca6be3cd393fae5ff` |
| live `state/proof_obligations.yml` | `338060b37c19d849053078e5f6a7775c45c626a16b6f9198fafdf9bb4a62265c` |
| Round-188 `state_patch.json` | `5198860aa96b484e46a2e9efd1cd5a89d99435295f237ff5c82adcaa731a6c00` |
| `math_collab/proof_obligations.py` | `384070a83b4ce1f56ebdceb0711680a6e889d4d43af3a40a8b6002319114a437` |
| second preapplication scope/path audit | `8ebb4b7482fea22dbb69875bfe98573d2b4fdcd90def2df95c1915bc281fbf9c` |
| current-hash provenance connector | `1c01697ff1ae7105d937ccb3a48423b9b41e303807cb71b267dc7ee6be1ea17c` |
| blind-report repair control | `5cf5cfce8dade96422d6f8971fc5a73a90e76c6f1e5e49d0000d7707d96c063e` |

The patch's 20 distinct current evidence/judge paths have these hashes. Paths
beginning with `R/` are relative to
`rounds/codex-managed/m9-m1-t1-high-h-imprimitive-lift-gcd-gate/`.

| Evidence or judge path | SHA-256 |
|---|---|
| `proofs/kernels/m9_m1_hard_top_t1_high_h_imprimitive_lift_gcd_reduction.md` | `ca313d2ed11884bdb3ff237c51380de7aadd713a5dc01b565935fbdb8fe9744a` |
| `R/candidates/formalized_hard_m1_t1_high_h_imprimitive_lift_gcd_reduction.md` | `c6f0939ffe5153d38ded0205ec4ee0f211f1de711ea81068194082dd66122f65` |
| `R/reports/imprimitive_lift_signed_attack.md` | `c77fe83e1c04042c221a1132121c50d8e745aaaca274d1284ec385e0bd3b8ca7` |
| `R/reports/lift_power_completion_hostile_audit.md` | `1f27281d91fd7290f548e3c1dfa696f2a6a9b82e184f8bc878747a29f1a3dce1` |
| `R/reports/blind_lift_gcd_rederivation.md` | `a524bf81774ac9cdcdd0c423851320da6dc037b8feee5decba541952c996e3b6` |
| `R/reviews/conductor_round188_report_reconciliation.md` | `cd29b356a80f14fe35e06f067c13c345e5258a51a4012c48cd3010f319c01997` |
| `R/reviews/conductor_inherited_hard_m1_shell_support_connector.md` | `9791a4224dff4f2067e331060b39d0c742ee4c20785a9350d81bd7382d18b9ac` |
| `R/reviews/lift_normalization_and_multiplicity_post_repair_verification.md` | `097226ab0d8acf98f65502b3163f1d5c5a384289725aa06379d5e6a27be0401e` |
| `R/reviews/lift_power_literal_scope_completion_seam_review.md` | `2ec3c9c0d96303400348fd3b2682e72dac4eeb955b0e558ab2f4dbad91548a01` |
| `R/reviews/blind_post_unmask_owner_scope_post_repair_verification.md` | `79e0be1854c9e61f643081a42e300a766f1829826ecf97ac6ac7dd313e051c26` |
| `R/reviews/final_kernel_candidate_consistency_review.md` | `054fdb430868c337825529f4e22cfa4b3457a4d1c8fc9c6c5873154ee0a8603f` |
| `R/reviews/final_kernel_power_owner_scope_review.md` | `3eaaf1327c6f54ffa2a731e3047537961dd4727617cb0d5141be873b19d1df98` |
| `R/reviews/final_kernel_formalization_provenance_hygiene_review.md` | `1ce46c6a984f6f1678042bc1f180b9a1e5a06e9b46d3e565fb0bbf76e15f53a6` |
| `R/reviews/final_kernel_candidate_provenance_post_hygiene_verification.md` | `1c01697ff1ae7105d937ccb3a48423b9b41e303807cb71b267dc7ee6be1ea17c` |
| `R/reviews/conductor_round188_adjudication.md` | `aea9de44bb8090200ef473d39d95a93db8096471bb1123c97218162be8e68406` |
| `R/synthesis.md` | `014ba753442a53ec72ab92a28df452778ca98cf20ab2f0dd3e3770729b742647` |
| `R/reviews/lift_normalization_and_multiplicity_seam_review.md` | `6c29cf14987029a3279c595ca38f051a29d5f7efbfb63ebe89e8b2e7ac56b899` |
| `R/controls/conductor_round188_blind_report_control_character_repair.md` | `5cf5cfce8dade96422d6f8971fc5a73a90e76c6f1e5e49d0000d7707d96c063e` |
| `R/controls/conductor_round188_wolfram_lift_partition_check.md` | `4d6173c31bfe63e158f5d07d90488808e65d6b81a58d5e428ed1e01ae69bcb42` |
| `R/controls/lift_partition_exact_check.wls` | `7bad1b482654e69325feaf844d359d1643a3245c8e990742ecfc83141e995b99` |

All are nonempty. The earlier final consistency, power/owner, and
formalization reviews remain historical hash-bound evidence and are carried
to the current candidate/kernel bytes only through the exact post-hygiene
connector. The two finite Wolfram artifacts and the byte-repair record remain
controls, not asymptotic theorem evidence.

## 7. Recommended state effect

Retain the live graph at SHA-256
`338060b37c19d849053078e5f6a7775c45c626a16b6f9198fafdf9bb4a62265c`
as the exact authorized realization of the Round-188 patch.

Retain only the new subordinate `proved_internal` node, the five authorized
field changes on the still-open owner, and the exact 15 rejected-claim suffix.
Do not alter any no-change object or any inherited status, statement,
dependency beyond the three declared additions, implication, blocker, owner,
M9-M1/M9-M2/endpoint/M9 node, bridge, GC theorem, target, or exponent.

Keep `188.K12`, the complete high-height relation, the original `t = 1`
residual, every `t >= 2` and large-`G` remainder, all parents, both bridges,
the target theorem, and every exponent claim open at their previous scope.
This audit recommends no further graph mutation and writes only this assigned
control report.
