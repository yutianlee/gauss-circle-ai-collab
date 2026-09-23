# Round 188 second preapplication scope, path, and reverse audit

## 1. Result / verdict

**Verdict: GREEN. First defect: none.**

The current State Patch, SHA-256

`5198860aa96b484e46a2e9efd1cd5a89d99435295f237ff5c82adcaa731a6c00`,

applies cleanly in memory to the canonical starting graph, SHA-256

`be0eca9ca93c3534cca958d70b5541d03d28ff993ebfbcbca6be3cd393fae5ff`.

Its exact operation inventory is

`(create, update, correct_rejected, reject, no_change) = (1, 1, 0, 15, 21)`.

Both repository validators return no issue. All 20 distinct current
evidence/judge paths exist and are nonempty. The post-hygiene connector is
GREEN at SHA-256
`1c01697ff1ae7105d937ccb3a48423b9b41e303807cb71b267dc7ee6be1ea17c`;
it proves by exact inverse hashes that the earlier final reviews are usable
only through that connector and that no mathematical or owner-scope content
changed in the hygiene repair chain.

With application time frozen at `2026-08-29T18:00:00`, Round 188, and the
current adjudication path used as judge reference, the isolated applied graph
is 2,052,996 bytes with SHA-256
`26950803795a2a3ccba53d378773d90f23b727c87b411bddde5688ddcea132c9`.
The operation-derived inverse recovers the 2,038,519-byte starting graph
byte-for-byte. Reapplication with the same frozen inputs reproduces the
temporary applied bytes exactly. No authoritative graph or shared state was
written during this audit.

## 2. Exact claim and hypotheses

The audited claim is strictly a preapplication claim about the frozen graph
and patch above. The simulation uses the repository's standard State Patch
applicator with `round_index = 188` and judge reference

`rounds/codex-managed/m9-m1-t1-high-h-imprimitive-lift-gcd-gate/reviews/conductor_round188_adjudication.md`.

The patch does exactly the following:

1. It creates
   `M9-M1-hard-top-t1-high-h-imprimitive-lift-gcd-reduction` with status
   `proved_internal`, direct dependencies
   `M9-M1-hard-top-t1-high-h-inverse-residue-conductor-reduction` and
   `Divisor-bound-elementary`, and empty `implies` and `blockers` lists.
2. It updates only
   `M9-M1-hard-top-high-radical-small-t-residual-estimate` by adding the new
   subordinate dependency, 18 inconclusive evidence paths, and a narrowed
   `next_action`. The owner remains `open`.
3. It appends 15 new, scoped rejected-claim records.
4. It records 21 existing obligations as `no_change`.

The new statement proves only the strict `Qm >= Y` imprimitive-lift sector
of the accepted Round-187 high packet. It records the exact joint `Qm < Y`
complement under one outer real part, its positive capacity, and the scoped
determinant/completion self-return controls, while leaving the required
one-sided estimate open. It explicitly denies closure of the complete
high-height relation, the original `t = 1` residual, the small-`t` owner,
every parent, bridge, theorem, and exponent.

The current kernel/candidate chain is used at its current hashes. Reviews
frozen at the pre-hygiene candidate and kernel hashes are not treated as
direct current-byte attestations; they enter only through the exact
post-hygiene provenance connector listed above.

## 3. Checks / proof

### Schema, identifiers, and paths

The patch has exactly the four top-level families
`starting_graph_sha256`, `reversibility`, `proof_obligations`, and
`round_assessment`. The proof-operation mapping has exactly `create`,
`update`, `correct_rejected`, `reject`, and `no_change`. The create and update
entries use only their declared field families; in particular, the update has
only `id`, `dependencies_added`, `evidence_added`, and `next_action`. It cannot
mutate status, statement, implications, blockers, or owner.

Every operation ID is unique within its class and across classes. The created
ID is absent from the starting graph. The update and all 21 no-change IDs
exist. All 15 rejection IDs are pairwise distinct, have nonempty distinct
reasons, and are absent from both the starting obligations and the 1,614
starting rejected claims. Every dependency, implication, and blocker target
in the simulated graph resolves to an existing obligation.

The create entry contains 16 positive and four inconclusive paths. The owner
update contains 18 inconclusive paths. Standard application adds the
adjudication judge reference to the new node's inconclusive bucket, producing
five there, and adds the same judge reference to each new rejection record.
Deduplication is exact. The union is 20 distinct existing, nonempty paths;
their current hashes appear in section 6.

### Exact isolated delta

The starting counts `(389 obligations, 1,614 rejected claims)` become
`(390, 1,629)`. The created obligation is the sole appended obligation and
the 15 declared rejection IDs are the exact rejected-claim suffix.

Among all 389 inherited obligations, only the named hard-M1 small-`t` owner
changes. Its changed fields are exactly:

- `dependencies`;
- `evidence`;
- `next_action`;
- `last_updated_round`; and
- `last_updated_at`.

Its new dependency was absent before application, and every one of the 18
evidence paths was absent from its previous inconclusive bucket. All 21
no-change obligation objects remain exactly equal to their starting objects.
All other top-level graph data remain equal.

The patch's reverse data equal the starting owner literally:
`last_updated_round = 187`,
`last_updated_at = 2026-08-29T15:59:13`, and the exact 654-byte prior
`next_action`, whose SHA-256 is
`d19c58a021d5ef9161b5c92ff38465fab918bcfd53ab90f717779ae472e9693a`.
No reconstructed or normalized substitute is used in the inverse.

Dependency edges change from 1,385 to 1,388, with exactly these additions:

1. the still-open owner to the new subordinate node;
2. the new node to the accepted Round-187 inverse-residue reduction; and
3. the new node to `Divisor-bound-elementary`.

No dependency is removed. Implication edges remain exactly 326 and blocker
edges exactly 70, with no addition or removal. The dependency graph has the
same three inherited nontrivial strongly connected components, each of size
two, before and after application. The new node is a singleton SCC, and its
only incoming dependency edge is from the still-open owner. Thus the edge
direction is subordinate-to-prerequisite and no new dependency cycle is
created.

### Protected state and overclaim scope

For every inherited obligation, the fields `status`, `statement_tex`,
`implies`, `blockers`, and `owner` are identical before and after the
simulation. A broad protected-family scan covers 372 inherited M9-, bridge-,
and GC-labelled nodes: all are object-identical except the authorized ledger,
evidence, next-action, and metadata fields of the one open owner.

In particular, these statuses remain exact:

| Node | Status |
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

Their statements, owners, implications, blockers, and dependencies are
unchanged. Hence the internal one-third result, the external
`0.3144831759740614...` benchmark, and the quarter target boundary do not
move. The new node's empty implication and blocker lists prevent a hidden
promotion route.

### Current-hash repair chain

The two repaired blind-report sites reverse exactly from current hash
`a524bf81774ac9cdcdd0c423851320da6dc037b8feee5decba541952c996e3b6`
to historical hash
`a8de6402d8a57d22a773d9b763e195f3e959a1a50cf084bb7ffab7205460231e`.
Replacing only that provenance hash recovers the frozen candidate
`683ad5bd...3808` and reconciliation `d67f5a7a...e20b8`; replacing only the
blind and candidate hashes recovers the frozen kernel `0ea2b3c3...8723`.
Replacing only the kernel hash recovers the prior adjudication and synthesis
hashes. The current connector independently checks these whole-file inverse
equalities. Therefore the present candidate, kernel, adjudication, and
synthesis differ from their previously reviewed bodies only in documentary
hash bindings; no formula, hypothesis, conclusion, or scope sentence drifted.

## 4. First doubtful or unproved step

There is no doubtful State Patch, path, dependency, reversibility, or owner
scope step at the frozen hashes.

The first mathematical step remains the intentionally open `188.K12`: prove
the jointly signed actual-coefficient estimate for the exact literal
`Qm < Y` complement and recover the full factor `Y` before positive
recombination. Its present positive estimate is only
`O_epsilon(Y L^2 X^epsilon)`. This open relation is preserved verbatim in the
new node and in the owner's narrowed next action; it is not a defect in this
preapplication audit.

The only hash variability in a real application is the serialized application
timestamp. Any change to the frozen graph, patch, or current evidence chain
would require a new audit.

## 5. Controls and outcomes

| Control | Outcome |
|---|---|
| starting graph and patch freeze | **PASS:** exact `be0eca9c...e5ff` and `5198860a...6c00` |
| canonical starting serialization | **PASS:** parse and canonical reserialization are byte-identical |
| official patch validation | **PASS:** zero issues |
| schema, count, and cross-class ID audit | **PASS:** exact `1/1/0/15/21`; no collision |
| evidence, judge, kernel, and control paths | **PASS:** 20 distinct paths, all existing and nonempty |
| blind-report repair reverse | **PASS:** exactly two byte-local TeX repairs recover `a8de6402...0231e` |
| current-hash provenance connector | **PASS:** GREEN at `1c01697f...a17c` |
| historical final reviews | **PASS with scope:** used only through the exact current-hash connector |
| new-node statement scope | **PASS:** strict `Qm >= Y` reduction only; exact complement and every owner remain open |
| isolated official application | **PASS:** resulting graph validates with zero issues |
| dependency direction and SCCs | **PASS:** exactly three forward additions and no new dependency cycle |
| protected owner/theorem/exponent fields | **PASS:** no status, statement, implication, blocker, or owner drift |
| operation-derived reverse | **PASS:** byte-exact recovery of `be0eca9c...e5ff` |
| frozen-time deterministic replay | **PASS:** byte-exact recovery of `26950803...32c9` |
| authoritative-state nonmutation | **PASS:** graph and patch were read only |

The earlier control
`controls/conductor_round188_preapply_controls.md`, SHA-256
`5de4e187cfd7d9e35959b49437bc26854a0be6bb2914e769870a2835c2c434c9`,
correctly recorded RED for the transient stale-hash snapshot and required a
current-hash connector plus a fresh preapplication audit. The connector and
this fresh audit satisfy that exact repair condition; the historical RED is
not misrepresented as a review of the current frozen chain.

## 6. Dependencies and hashes

Core audit inputs and controls:

| Artifact | SHA-256 |
|---|---|
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| `state/active_campaign.yml` | `0e9e74a383cd32c327b13263c3e489f4bb1c096a54346c231e9a58f0fc1e7669` |
| `state/proof_obligations.yml` | `be0eca9ca93c3534cca958d70b5541d03d28ff993ebfbcbca6be3cd393fae5ff` |
| Round-188 `state_patch.json` | `5198860aa96b484e46a2e9efd1cd5a89d99435295f237ff5c82adcaa731a6c00` |
| `math_collab/proof_obligations.py` | `384070a83b4ce1f56ebdceb0711680a6e889d4d43af3a40a8b6002319114a437` |
| post-hygiene current-hash connector | `1c01697ff1ae7105d937ccb3a48423b9b41e303807cb71b267dc7ee6be1ea17c` |
| blind-report byte-repair control | `5cf5cfce8dade96422d6f8971fc5a73a90e76c6f1e5e49d0000d7707d96c063e` |
| historical stale-snapshot control | `5de4e187cfd7d9e35959b49437bc26854a0be6bb2914e769870a2835c2c434c9` |

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

All paths are nonempty. The final consistency, power/owner, and
formalization reviews in the middle of the table remain frozen historical
evidence at their named old candidate/kernel hashes; the current-hash
connector is the exact and only bridge from those attestations to the current
candidate and kernel. The Wolfram files and repair record remain controls,
not asymptotic theorem evidence.

## 7. Recommended state effect

Permit application of exactly the Round-188 State Patch at SHA-256
`5198860aa96b484e46a2e9efd1cd5a89d99435295f237ff5c82adcaa731a6c00`
to exactly the starting graph at SHA-256
`be0eca9ca93c3534cca958d70b5541d03d28ff993ebfbcbca6be3cd393fae5ff`.

Permit only the one scoped subordinate creation, the one still-open owner
ledger/evidence/next-action update, and the 15 new rejected-claim records.
Retain all 21 no-change nodes exactly. Do not alter any other status,
statement, dependency, implication, blocker, owner, M9-M1/M9-M2/endpoint/M9
node, bridge, GC theorem, target, or exponent boundary. A real applied-graph
hash may differ from the frozen simulation hash solely because of its actual
timestamp; its structural effect must remain the exact audited inventory.

This auditor authorizes no mutation beyond that frozen patch and writes only
this assigned control report.
