# 1. Result and verdict

**Verdict: GREEN. First defect: none.**

The Round-189 State Patch is valid against the exact frozen starting
graph. Strict JSON parsing succeeds with no duplicate key, and the
official dry validator returns exactly “Patch OK”. In-memory execution
through the production applicator gives the exact effect

\[
 \boxed{1/1/0/15/22}
\]

for create/update/correct-rejected/reject/no-change. The operation-derived
inverse, using the declared reversibility record, recovers the starting
object and all 2,052,996 starting bytes exactly. Replay with the same
frozen diagnostic timestamp, round, and judge reference reproduces the
same result counters, object, 2,067,773 canonical bytes, and simulated
post-state SHA-256

da453dfd5f0c2da1999fcd81d61ac53ff5fbd3841000e1e86badeceb5d3f1b6a.

Only one subordinate proved node is created. Only one inherited node
changes, and it remains open. No inherited status, statement,
implication, blocker, owner, theorem, bridge, or exponent field changes.
All evidence paths exist, both direct dependencies exist and are
proved_internal, no relation target is missing, and no new cycle is
introduced.

# 2. Exact audited inputs and effect

The verdict is bound to:

- starting graph state/proof_obligations.yml: 2,052,996 bytes,
  SHA-256
  338060b37c19d849053078e5f6a7775c45c626a16b6f9198fafdf9bb4a62265c;
- Round-189 patch
  rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/state_patch.json:
  17,922 bytes, SHA-256
  88c3a1d944e618e75b8c0bfecd7bd3e8dcffa5f0fdbb054f319906fc2c68024b;
- round_index \(=189\);
- frozen diagnostic timestamp 2026-08-29T23:00:00; and
- judge reference
  rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/reviews/conductor_round189_adjudication.md.

The timestamp is only a deterministic audit fixture. An authoritative
application will use its actual clock value and therefore may have a
different post-state hash.

The patch creates exactly
M9-M1-hard-top-t1-high-h-dual-frequency-projective-reduction with
status proved_internal. Its direct dependencies are:

1. M9-M1-hard-top-t1-high-h-imprimitive-lift-gcd-reduction;
2. Divisor-bound-elementary.

Both exist in the starting graph and are proved_internal.

The patch updates exactly
M9-M1-hard-top-high-radical-small-t-residual-estimate. It adds one
dependency, eighteen novel inconclusive evidence paths, replaces
next_action, and records Round-189 timestamp metadata. The owner remains
open.

It corrects zero rejected claims and appends exactly these fifteen new
rejected-overclaim records:

1. Round189-U-over-Y-is-unique-maximal-cutoff;
2. Round189-projective-cutoff-is-q-over-Y;
3. Round189-projective-map-is-not-bijective-on-live-v;
4. Round189-residue-class-plus-one-causes-power-loss;
5. Round189-lift-weight-does-not-cancel-projective-m;
6. Round189-slow-sector-proves-complete-Round188-complement;
7. Round189-saturated-cutoff-leaves-fast-unit-slopes;
8. Round189-geometric-height-sum-applies-to-literal-weight;
9. Round189-pointwise-bound-implies-target-height-BV;
10. Round189-arithmetic-masks-are-height-invariant;
11. Round189-centered-kernel-has-uniform-polylog-prefixes;
12. Round189-prime-bad-slope-is-literal-lower-mass;
13. Round189-positive-completion-or-large-sieve-gains-Y;
14. Round189-strict-projective-sector-proves-complete-t1;
15. Round189-strict-projective-sector-improves-global-exponent.

It records no change for exactly these twenty-two existing obligations:

1. M9-M1-hard-top-t1-high-h-imprimitive-lift-gcd-reduction;
2. M9-M1-hard-top-t1-high-h-inverse-residue-conductor-reduction;
3. M9-M1-hard-top-t1-residual-fejer-tangent-gcd-reduction;
4. M9-M1-hard-top-t1-comparable-factor-exchange-sector;
5. M9-M1-hard-top-small-t-nonresonant-primitive-ray-sector;
6. M9-M1-top-endpoint-signed-cone;
7. M9-M1-direct-smooth-residual-blockwise-estimate;
8. M9-M1-physical-one-count-assembly;
9. M9-M1-global-angular-radial-estimate;
10. M9-M1;
11. M9-M2-top-endpoint-signed-cone;
12. M9-M2-smooth-balanced-quarter-packet-estimate;
13. M9-M2-smooth-unbalanced-three-quarter-estimate;
14. M9-M2;
15. M9-endpoint-uniformity;
16. M9;
17. Conditional-bridge;
18. GC-global-M1-alternative-bridge;
19. GC-partial-one-third;
20. GC-external-Li-Yang-theta-star;
21. GC-target;
22. Divisor-bound-elementary.

Every operation list has unique IDs, the five operation-ID sets are
pairwise disjoint, the created ID is absent from both inherited ID
sets, the update and no-change IDs exist, and all reject IDs are new.

# 3. Method, application, inverse, and replay

## 3.1 Strict parse and official validation

The read-only official command was:

    python -m math_collab.validate_state_patch
      --graph state/proof_obligations.yml
      --patch rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/state_patch.json

It returned “Patch OK” with exit status zero.

Independently, both files were decoded as strict UTF-8 and the patch was
parsed by json.loads with a duplicate-key-rejecting object_pairs_hook.
The patch is canonical indented JSON with the exact top-level keys
starting_graph_sha256, reversibility, proof_obligations, and
round_assessment, and the exact operation keys create, update,
correct_rejected, reject, and no_change. Its starting_graph_sha256
equals the raw graph hash. The raw graph is already byte-identical to
the production dump_graph serialization.

## 3.2 In-memory production application

The audit imported validate_graph, validate_patch_against_graph,
apply_state_patch, and dump_graph from
math_collab/proof_obligations.py. Only the applicator clock was frozen;
no production mutation rule was reimplemented. The call used round 189,
the fixture timestamp, and the exact judge path above.

The returned counters are:

| Effect | Count |
|---|---:|
| created | 1 |
| updated | 1 |
| corrected_rejected | 0 |
| rejected | 15 |
| no_change | 22 |

Obligations increase from 390 to 391 and rejected-claim records from
1,629 to 1,644. The only added obligation is the declared projective
reduction; none is removed. The only changed inherited obligation is
the declared small-\(t\) owner, with exactly these changed keys:

\[
 \{\text{dependencies},\text{evidence},\text{next_action},
   \text{last_updated_round},\text{last_updated_at}\}.
\]

Its dependency count rises from 6 to 7. Its evidence buckets change
from \(0/0/108\) to \(0/0/126\) for
positive/negative/inconclusive. Its status, statement_tex, implies,
blockers, owner, id, type, track, and title remain byte-equivalent as
parsed values.

The created node exactly equals the patch create record plus
last_updated_round \(=189\), the frozen timestamp, and the production
judge-reference injection. It has 17 positive, 0 negative, and 5
inconclusive evidence entries after that injection.

The inherited status histogram changes only by the new proved_internal
node:

| Status | Before | After |
|---|---:|---:|
| open | 34 | 34 |
| derived_under_assumptions | 15 | 15 |
| proved_internal | 311 | 312 |
| proved_external_dependency | 19 | 19 |
| proposed | 7 | 7 |
| diagnostic_only | 2 | 2 |
| rejected | 2 | 2 |

The fifteen rejected records are an exact new suffix, in patch order,
with only id, reason, round, frozen timestamp, and judge evidence. No
existing obligation is changed to rejected status.

## 3.3 Evidence, relations, and cycles

The patch contains 39 create/update evidence occurrences over 21 unique
paths: 21 entries on the created node and 18 on the updated owner. All
21 paths are regular files and decode as strict UTF-8. All eighteen
owner additions are novel. Production metadata adds one judge reference
to the created node's inconclusive bucket and one to each of the fifteen
new rejection records, so the simulation makes 55 actual evidence
additions in total.

Relation inventories are:

| Relation | Before | After | Delta |
|---|---:|---:|---:|
| dependencies | 1,388 | 1,391 | +3 |
| implies | 326 | 326 | 0 |
| blockers | 70 | 70 | 0 |

The three new dependency edges are exactly the two dependencies of the
created node and the owner's new dependency on it. There are no missing
relation targets and no duplicate dependency, implication, or blocker
entries.

No new cycle is introduced. The only dependency strongly connected
components of size greater than one are the same three inherited pairs
before and after:

- M9-M1-lower-far-cone-microscopic-cell-reduction with
  M9-M1-lower-post-collar-smoothed-far-alias-reduction;
- M9-M1-lower-height-alias-rank-one-product-fibre-obstruction with
  M9-M1-lower-incomplete-fibre-dispersion-obstruction;
- M9-M2-hard-top-product-fibre-mean-obstruction with
  M9-M2-hard-top-product-fibre-transform-self-return.

The implies and blockers graphs remain acyclic.

## 3.4 Declared inverse and deterministic replay

The reversibility record's saved next_action,
last_updated_round \(=188\), and
last_updated_at \(=\) 2026-08-29T17:36:08 exactly match the starting
owner. The inverse was derived only from patch operations, that record,
and the frozen application metadata:

1. assert the exact generated created node and remove it;
2. remove the one novel owner dependency;
3. remove the exact eighteen novel owner evidence additions;
4. restore the recorded next_action and metadata;
5. assert and remove the exact fifteen-record rejected suffix.

The recovered object equals the strict-parsed starting object.
Production canonical serialization equals the raw starting file byte
for byte: 2,052,996 bytes and SHA-256
338060b37c19d849053078e5f6a7775c45c626a16b6f9198fafdf9bb4a62265c.

Reapplication through the same production function, with the same
round, timestamp, and judge path, reproduces the first simulated object,
PatchResult, 2,067,773 bytes, and SHA-256
da453dfd5f0c2da1999fcd81d61ac53ff5fbd3841000e1e86badeceb5d3f1b6a
exactly.

Production graph validation returns zero issues on the start,
post-state, reversed start, and replay.

# 4. First defect or open step

First mechanical defect: **none**. No defect was found in the hashes,
strict JSON, operation counts, IDs, evidence paths, dependency
existence, relation cycles, protected fields, reversibility record,
inverse recovery, or deterministic replay.

The first mathematical open step is unchanged: prove the exact
one-outer-real-part fast complement

\[
 j_q(a,v)>
 \min\!\left\{\frac{q-1}{2},
              \left\lfloor\frac{H_Bmq}{Y}\right\rfloor\right\}
\]

through the actual fixed-\(a\), dyadic-\(J\) coefficient-variation
bound at scale \(H_Bm\kappa uJ/q\), or a genuinely joint signed
substitute with the same ledger. The patch keeps this in next_action
and promotes no complete owner.

The only operational boundary is the actual application timestamp. A
postapplication audit must recover that value and replay with it.

# 5. Controls and exact outcomes

| Control | Outcome |
|---|---|
| starting graph hash/canonical bytes | PASS: 338060b3...2265c, 2,052,996 bytes |
| patch hash/strict canonical JSON | PASS: 88c3a1d9...8024b, 17,922 bytes |
| official dry validator | PASS: exact output “Patch OK” |
| duplicate-key and ID audit | PASS: no duplicate or cross-operation ID |
| production in-memory effect | PASS: exact 1/1/0/15/22 |
| created/update scope | PASS: one subordinate node and one still-open owner |
| protected fields | PASS: no inherited status, statement, implies, blockers, owner, theorem, bridge, or exponent drift |
| no-change obligations | PASS: all 22 exist and remain deeply unchanged |
| rejected controls | PASS: exact 15-record suffix; no obligation rejection |
| evidence paths | PASS: 39 references, 21 unique existing strict-UTF-8 files |
| evidence novelty | PASS: one dependency and all 18 owner evidence additions are novel |
| dependency endpoints | PASS: both created-node dependencies exist and are proved_internal |
| relation integrity | PASS: no missing targets or duplicate relation entries |
| cycle comparison | PASS: no new cycle; three inherited dependency pairs unchanged |
| graph validation | PASS before, after, inverse, and replay |
| operation-derived inverse | PASS: exact starting object and raw bytes recovered |
| frozen-metadata replay | PASS: identical object, counters, bytes, and da453dfd...f1b6a hash |
| authoritative nonmutation | PASS: graph and patch retain their frozen hashes |

All machine work was exact parsing, hashing, path checking, production
in-memory application, graph comparison, inversion, and replay. No
numerical theorem experiment or external source was used.

# 6. Dependencies, evidence paths, and hashes

## 6.1 Core audit artifacts

| Artifact | SHA-256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| state/proof_obligations.yml | 338060b37c19d849053078e5f6a7775c45c626a16b6f9198fafdf9bb4a62265c |
| state/active_campaign.yml | 4d8661258570c3152d464f38d76798f1aadd271e9f4e221c80011d3ec60d68f5 |
| Round-189 state_patch.json | 88c3a1d944e618e75b8c0bfecd7bd3e8dcffa5f0fdbb054f319906fc2c68024b |
| math_collab/proof_obligations.py | 384070a83b4ce1f56ebdceb0711680a6e889d4d43af3a40a8b6002319114a437 |
| math_collab/validate_state_patch.py | cfa914c54bfa172cc94354dc7e904e866d4e69c96cd8be7bfbf68b5a295080e8 |

## 6.2 Unique patch evidence paths

| Evidence path | SHA-256 |
|---|---|
| proofs/kernels/m9_m1_hard_top_t1_high_h_dual_frequency_projective_reduction.md | 31092b28826b9f36ecaedfb5efc5d7625f4caa4da2cf4c37bd48389c6ac6ee58 |
| rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/candidates/formalized_hard_m1_t1_high_h_dual_frequency_projective_reduction.md | 123d697198c3c20d710fe5880db75f09423ff457820694dd8671e5b8564e1e28 |
| rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/reports/dual_height_frequency_signed_attack.md | 65636c38a3b0c3dbd4a26839dbc89daa88ef78dee5638d02d0de1192b9bdfd38 |
| rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/reports/height_variation_projective_hostile_audit.md | b8ec876aebcc6668646880813bad0abf576063f58e71518d29c8e5778d371608 |
| rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/reports/blind_dual_frequency_rederivation.md | 13169505840f9033fb8ddaac6eba62d12988a669127f593a8bc48438543621a3 |
| rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/reviews/conductor_round189_report_reconciliation.md | f7486ccf02a7fb43e1bde82e94e7da410a1d691fc8b629f2b877bc40ca6a902e |
| rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/reviews/dual_frequency_normalization_projective_power_seam_review.md | 5af4ffb3fd3da05287cf217a9ffad412dd888aea716686466bd76fe90c4b8b95 |
| rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/reviews/literal_variation_centered_kernel_scope_seam_review.md | 7b9bd94ba4e229d76b1eca96a0e7d25aa98d6e66c4c81e5c40e07d85c8744d3e |
| rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/reviews/blind_post_unmask_owner_scope_seam_review.md | 37cee21325ed7b1e4892aff6e433f642cac9936cf10ce42e25c53496fd712a93 |
| rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/reviews/blind_post_unmask_quantifier_post_repair_verification.md | 3594bef3890c41d26eb36bdfcae4b5a8f761a5b203b5289ba2889eae91382dda |
| rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/reviews/final_candidate_normalization_post_quantifier_verification.md | 2b85de501fb60e34eadb212c94843b40e8abcde124ef4fe40aecfecfe9ae25e0 |
| rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/reviews/final_candidate_literal_formalization_post_quantifier_verification.md | c2c7135ad43bc98c8b4b26f98779cd5b3601892cca018d3659a0367efdc997ad |
| rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/reviews/final_kernel_candidate_consistency_review.md | ef069ca04efa6f0f8913dc75ea6faad6648b891b7d710d61e24565e5a0fcc684 |
| rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/reviews/final_kernel_power_literal_owner_scope_review.md | e19a1a0f3a23e14bfb40636425cbd698a5b5fef2d4707d1b21c08ca19e3d1354 |
| rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/reviews/final_kernel_formalization_provenance_hygiene_review.md | d4e2667a8bf41c35fd6f646338e688d1982afd06809e5d7a67a7bd850baff69e |
| rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/reviews/conductor_round189_adjudication.md | 37f62c5d974aafb240c599cfe8ee1b79370ef05b56f064aa553039b27550c613 |
| rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/synthesis.md | 6f66eae59a464e8ebff99222320f21bd9d7b8f57ddaa8d021d04e22aa8506fb1 |
| rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/controls/conductor_round189_analytic_controls.md | 2ed8b5a67efb51543239467ec55e285b0f9432b5fc245080b387fec267dd7ffd |
| rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/controls/conductor_round189_wolfram_dual_frequency_check.md | 35bddf8080ceef4acbc6290abe689175f94fc90745a28c707f8147bb5c08adbf |
| rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/controls/dual_frequency_projective_check.wls | 481e7054cce6ad9922f818ff33d11c77265c653608acccbb380a804f34870fff |
| rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/controls/conductor_round189_candidate_tex_byte_repair.md | ece198a579b537723f07a3c775d6386ec0de88ce39b9f2c091cb8051476d1cba |

The judge path is one of these 21 paths and is also injected by the
production applicator into the created node's inconclusive evidence and
each new rejection record. All hashes above were recomputed during this
audit.

# 7. Recommended state effect

Approve application of exactly the patch at
88c3a1d944e618e75b8c0bfecd7bd3e8dcffa5f0fdbb054f319906fc2c68024b
to exactly the graph at
338060b37c19d849053078e5f6a7775c45c626a16b6f9198fafdf9bb4a62265c,
using round_index 189, the official production applicator, and the
declared adjudication path.

The authorized effect is only to create the strict dual-frequency
projective subordinate node, attach it and inconclusive Round-189
evidence to the still-open small-\(t\) owner, narrow that owner's
next_action, append fifteen calibrated overclaim records, and record
twenty-two no-change decisions. No complete residual, M1/M2 parent,
endpoint-uniformity owner, M9 node, bridge, theorem, or exponent may be
promoted.

After authoritative application, require an independent postapplication
field, relation, inverse, and replay audit using the actual recorded
timestamp and judge reference. If either frozen input hash changes,
this verdict is void.
