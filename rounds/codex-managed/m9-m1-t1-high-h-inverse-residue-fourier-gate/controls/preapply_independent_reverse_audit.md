# 1. Result

**Verdict: GREEN for application of the exact audited patch to the exact
frozen graph.  First mechanical defect: none.**

The raw starting graph is already in canonical `dump_graph` serialization and
has SHA-256
`d1ace6e362a41f1a08fc09c8e44ce628758040fa91ae39c152113c275f76352a`,
exactly matching `state_patch.json`.  Official dry validation returns
`Patch OK`.

The exact operation inventory is:

| operation | count | audited effect |
|---|---:|---|
| create | 1 | one new subordinate `proved_internal` reduction |
| update | 1 | one existing open hard-M1 small-`t` owner |
| correct rejected | 0 | none |
| append rejected-overclaim record | 14 | all IDs distinct and new |
| record no change | 20 | all IDs distinct, existing, and deeply unchanged |

At a frozen applicator time, the official in-memory application produces 389
obligations and 1,614 rejected-claim records.  Exact operation-derived
inversion recovers the starting object and its 2,025,313 bytes byte for byte.
Replay with the same frozen clock reproduces the identical post-state object,
operation result, 2,036,325 canonical bytes, and SHA-256.  No graph, patch,
lifecycle file, synthesis, proof draft, or validation matrix was written.

# 2. Exact audited effect and hypotheses

This verdict applies only to:

- starting graph hash
  `d1ace6e362a41f1a08fc09c8e44ce628758040fa91ae39c152113c275f76352a`;
- patch hash
  `bc0e7ed8dc758ebf35c92475d4ef1955457ea8666e70102670ba33daa40549bd`;
- `round_index=187`;
- `judge_ref=None`; and
- the official applicator frozen at `2026-08-29T15:46:47` for deterministic
  simulation.

The frozen time is diagnostic.  The actual post-application hash will depend
on the official application timestamp and must be recorded by the required
post-application audit.

The patch creates exactly
`M9-M1-hard-top-t1-high-h-inverse-residue-conductor-reduction`, with status
`proved_internal`, two already-proved dependencies, empty `implies`, empty
`blockers`, 15 positive evidence paths, no negative evidence, and three
inconclusive diagnostic/hygiene paths.  Its statement proves only the strict
transformed packet, exact complement, and self-return controls.  It explicitly
leaves the exact high-conductor one-sided relation open.

The patch updates exactly
`M9-M1-hard-top-high-radical-small-t-residual-estimate`.  Before application it
is `open`, owned by `Codex conductor`, has four dependencies, 74 inconclusive
evidence paths, and no positive or negative evidence.  Application:

1. appends the one new subordinate dependency;
2. appends exactly 16 novel inconclusive evidence paths, producing 90;
3. replaces only its strategy-level `next_action`; and
4. sets Round-187 application metadata.

Its `id`, type, track, title, status, statement, implications, blockers, owner,
positive evidence, and negative evidence remain unchanged.  The new next
action is exactly the still-open joint complement
`U>4H_B`, `q_U(k)>H_B`, `|k|_U>H_B`, under one outer real part with the full
factor `Y` still required.

The 14 rejected records are overclaim controls, not rejected obligations.
They record the failure of zero/low modes, positive high-mode recombination,
conductor centering, raw orientation antisymmetry, positive transform energy,
small retained energy, adversarial lower-mass inference, physical-sector
interpretation, maximal-cutoff inference, complete-target inference,
small-`t` closure, exponent improvement, and the unsigned analogue.  Their
reasons agree with the final kernel, adjudication, and synthesis.

# 3. Method, graph checks, inverse, and replay

## 3.1 Commands and parsing method

The official read-only dry command was:

```text
python -m math_collab.validate_state_patch --graph state/proof_obligations.yml --patch rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/state_patch.json
```

Outcome: `Patch OK`.

An independent in-memory Python replay then:

1. decoded the graph and patch as strict UTF-8 JSON with a duplicate-key
   rejecting `object_pairs_hook`;
2. verified that `dump_graph(graph).encode("utf-8")` equals the raw graph
   bytes;
3. imported `validate_graph`, `validate_patch_against_graph`,
   `apply_state_patch`, and `dump_graph` from
   `math_collab.proof_obligations`;
4. froze the applicator clock, used `round_index=187` and no `judge_ref`, and
   applied the patch only in memory;
5. compared every obligation field, relation edge, status, evidence bucket,
   rejected-record prefix/suffix, and no-change item;
6. executed the declared inverse; and
7. replayed from the recovered graph with the same frozen clock.

The patch itself is canonical JSON: exact top-level keys
`starting_graph_sha256`, `reversibility`, `proof_obligations`, and
`round_assessment`; exact operation keys `create`, `update`,
`correct_rejected`, `reject`, and `no_change`; no duplicate key, CRLF,
trailing-space, or terminal-newline defect.

## 3.2 IDs, evidence, dependencies, and cycles

The starting graph contains 388 unique obligation IDs and 1,600 unique
rejected-claim IDs.  The created ID is absent from both sets.  The update ID
exists exactly once.  All 14 reject IDs are pairwise distinct and absent from
both inherited ID sets.  All 20 no-change IDs are pairwise distinct and exist.
The five operation-ID sets are mutually disjoint.  The starting graph has no
duplicate entries inside any dependency, implication, or blocker list.

The patch contains 34 evidence references to 18 unique paths.  Every path
exists as a file, decodes as strict UTF-8, and has the hash recorded in Section
6.  Evidence lists inside the patch contain no duplicate.  Every one of the 16
update evidence additions is absent from the owner's starting inconclusive
bucket, so inverse removal cannot delete inherited evidence.  The added
dependency is likewise novel.

The two dependencies of the new node exist and both are `proved_internal`:

- `M9-M1-hard-top-t1-residual-fejer-tangent-gcd-reduction`;
- `Divisor-bound-elementary`.

Relation inventories are:

| relation | before | after | delta | missing targets after |
|---|---:|---:|---:|---:|
| dependencies | 1,382 | 1,385 | +3 | 0 |
| implies | 326 | 326 | 0 | 0 |
| blockers | 70 | 70 | 0 | 0 |

The three dependency additions are exactly the new node's two direct
dependencies and the open owner's dependency on the new node.  No dependency
cycle is introduced.  Three inherited two-node dependency strongly connected
components remain unchanged:

- `M9-M1-lower-far-cone-microscopic-cell-reduction` with
  `M9-M1-lower-post-collar-smoothed-far-alias-reduction`;
- `M9-M1-lower-height-alias-rank-one-product-fibre-obstruction` with
  `M9-M1-lower-incomplete-fibre-dispersion-obstruction`;
- `M9-M2-hard-top-product-fibre-mean-obstruction` with
  `M9-M2-hard-top-product-fibre-transform-self-return`.

The implication and blocker graphs have no cycle before or after.  Thus the
patch neither creates a cycle nor hides an inherited one.

## 3.3 Exact mutation and protected transitions

A complete before/after comparison finds exactly one changed inherited
obligation.  Its changed fields are only:

`dependencies`, `evidence`, `next_action`, `last_updated_round`, and
`last_updated_at`.

Every other inherited obligation is deeply identical.  In particular, all 20
no-change obligations remain unchanged.  The status ledger is:

| status | before | after |
|---|---:|---:|
| open | 34 | 34 |
| derived under assumptions | 15 | 15 |
| proved internal | 309 | 310 |
| proved external dependency | 19 | 19 |
| proposed | 7 | 7 |
| diagnostic only | 2 | 2 |
| rejected | 2 | 2 |

The sole status-count change is the newly created subordinate proved node.
No inherited open, proved, bridge, theorem, endpoint, or exponent node changes
status.  In particular, `M9-M1`, `M9-M2`, endpoint uniformity, `M9`, both
bridges, and `GC-target` remain open or conditional exactly as recorded in the
starting graph.  The internal one-third and external Li--Yang exponent nodes
remain unchanged.

The inherited rejected-claim list is an unchanged 1,600-record prefix.  The 14
new records are the exact suffix in patch order, with only their patch IDs and
reasons plus common Round-187 timestamp metadata.  No existing obligation is
changed to status `rejected`.

## 3.4 Operation-derived reverse and deterministic replay

The reversibility record's saved `next_action`, `last_updated_round: 186`, and
`last_updated_at: 2026-08-28T09:12:29` exactly equal the starting owner fields.
The inverse performed these exact operations:

1. remove the one created obligation;
2. remove the one novel dependency and exact 16-path evidence suffix;
3. restore the saved next action and metadata; and
4. remove the exact 14-record rejected-claim suffix.

The recovered object equals the starting object.  Canonical serialization is
byte-equal to the raw starting file and hashes to
`d1ace6e362a41f1a08fc09c8e44ce628758040fa91ae39c152113c275f76352a`.

Reapplication with the same frozen timestamp reproduces the first simulated
object, `PatchResult`, canonical bytes, and SHA-256 exactly:

`163a37debd3645a46327c0a680791b1480407cd37cfdd5bc2fb8d7cdd1b7c580`.

The starting, simulated post-state, reversed, and replayed objects all pass
`validate_graph` with zero issues.

# 4. First defect or open step

**First mechanical defect: none.**  No defect was found in the starting hash,
patch schema, ID inventory, evidence paths, dependency existence, cycle delta,
protected transition, reversibility record, inverse, or deterministic replay.

The first open mathematical step remains kernel (K187.11): prove the one-sided
bound for the exact high-conductor complement at
`O_(B,epsilon)(L^2 X^epsilon)`, recovering the full factor `Y` before positive
recombination while retaining both orientations and every literal field under
one outer real part.  The patch records this as an open next action and does not
promote any complete owner.

# 5. Required controls and exact outcomes

| control | outcome |
|---|---|
| raw starting hash | **PASS**; exact `d1ace...` match |
| raw/canonical starting bytes | **PASS**; all 2,025,313 bytes equal |
| strict patch parse and canonical form | **PASS**; hash `bc0e...`, no duplicate key or whitespace defect |
| official dry validation | **PASS**; `Patch OK` |
| operation inventory | **PASS**; `1/1/0/14/20` |
| graph and patch ID uniqueness | **PASS**; no duplicate or cross-operation ID |
| all evidence paths | **PASS**; 34 references, 18 unique files, all present and UTF-8 |
| update novelty | **PASS**; one dependency and 16 evidence values all novel |
| dependency existence | **PASS**; zero missing dependency, implication, or blocker targets |
| dependency cycles | **PASS**; zero new cycle; exact three inherited SCCs unchanged |
| mutation confinement | **PASS**; one existing node, five authorized fields only |
| protected statuses | **PASS**; no inherited status transition |
| no-change records | **PASS**; 20 existing unique IDs, deeply unchanged |
| rejected overclaims | **PASS**; 14 new unique suffix records, no obligation rejection |
| graph validation | **PASS** before, after, reverse, and replay |
| reverse recovery | **PASS**; object and raw canonical bytes equal starting graph |
| deterministic replay | **PASS**; object, result, bytes, and frozen-time hash equal |

Machine work was confined to exact parsing, hashing, file-existence and UTF-8
checks, official dry validation, in-memory graph mutation, graph traversal,
field comparison, inversion, and replay.  No numerical theorem experiment or
external source was used.

# 6. Dependencies, evidence paths, and hashes

## Core audit artifacts

| artifact | SHA-256 |
|---|---|
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| `state/proof_obligations.yml` | `d1ace6e362a41f1a08fc09c8e44ce628758040fa91ae39c152113c275f76352a` |
| `state/active_campaign.yml` | `aadf701b1725cdd0004bb29e1fc625754e391e5475130df3a08a2a2e18d761d3` |
| `state_patch.json` | `bc0e7ed8dc758ebf35c92475d4ef1955457ea8666e70102670ba33daa40549bd` |
| durable kernel | `a9145455a872d57debaf0f91cc8a518f80acef4c1b1fb9115dc1851765a992f2` |
| conductor adjudication | `c6949ba7089e5d70c377c658771ef4bcf6be1ad603b453739de615cf91862ef5` |
| synthesis | `4e65ce906acbd0e1b7de18d5a6b728e560c7e3641ee4bbc349443566574a37e1` |
| `math_collab/proof_obligations.py` | `384070a83b4ce1f56ebdceb0711680a6e889d4d43af3a40a8b6002319114a437` |
| `math_collab/validate_state_patch.py` | `cfa914c54bfa172cc94354dc7e904e866d4e69c96cd8be7bfbf68b5a295080e8` |

## Unique evidence paths named by the patch

| evidence artifact | SHA-256 |
|---|---|
| `proofs/kernels/m9_m1_hard_top_t1_high_h_inverse_residue_conductor_reduction.md` | `a9145455a872d57debaf0f91cc8a518f80acef4c1b1fb9115dc1851765a992f2` |
| `candidates/formalized_hard_m1_t1_high_h_inverse_residue_conductor_reduction.md` | `c2f01f57a41695d73d0d1f9716a03328147dbe79f0fcdeb7e8e3465b29779b89` |
| `reports/literal_height_fourier_attack.md` | `4433de37846caa4c9ae0d51ba874221851a331e4a6af13043d4da0f0749ac298` |
| `reports/deletion_resonance_capacity_audit.md` | `5a09310baf8574bf1f2c841cd179a66d22aa5834cc50be555a11ad969569db1a` |
| `reports/blind_high_h_rederivation.md` | `abaf181178b56925bec5fa6b624ddd79be528f4e419e2bff7f22adf9593b9992` |
| `reviews/conductor_round187_report_reconciliation.md` | `b3de83554db114db91b33a8e994f0daa3cd9d9c41550eceabd575fbca1250705` |
| `reviews/inverse_residue_normalization_multiplicity_post_repair_verification.md` | `4fa37825aedfa940bb7ca55b0b4f75145770dc4bb007dc68bf5ee69005ea6739` |
| `reviews/candidate_normalization_post_tex_repair_verification.md` | `b357dc049f9ebf0a8b21b6ed1d816426e166fa78347e2b124822342f48b2b458` |
| `reviews/power_literal_scope_post_tex_repair_verification.md` | `52c2397a88577001fe54c1541a5c831e89e29522320bdefc4ce9c4b1c37b57f8` |
| `reviews/blind_post_unmask_owner_scope_seam_review.md` | `38601b87edfb4706a5206bbd7a7fb704e35b14f0c85d6b8704c698c81ce3ed44` |
| `reviews/final_kernel_candidate_consistency_final_hash_verification.md` | `3e9412b4404ca8399ed2350f459117b6b8b84fe479820a4e12a39da7bad1bb4d` |
| `reviews/final_kernel_power_owner_scope_post_repair_verification.md` | `602a56c4ece7fce4a9e415eb9e95ce7e089dd690630e52fc2f28b16b4c08c0cc` |
| `reviews/final_kernel_formalization_provenance_post_repair_verification.md` | `5f3679b342a9210a2e0baa5c27ff82fc1fa5804bc662c8ea6e9c56886e0e417e` |
| `reviews/conductor_round187_adjudication.md` | `c6949ba7089e5d70c377c658771ef4bcf6be1ad603b453739de615cf91862ef5` |
| `synthesis.md` | `4e65ce906acbd0e1b7de18d5a6b728e560c7e3641ee4bbc349443566574a37e1` |
| `controls/conductor_round187_wolfram_inverse_residue_check.md` | `032d8039636b0e4e2040caed7c0d2ade507d111a7f966b9b40f03676fadd1113` |
| `controls/inverse_residue_exact_check.wls` | `e818367a710c4051f9259966133ca48b94810a55544b4b0ec3d3fbab15a06bcd` |
| `reviews/final_kernel_formalization_provenance_hygiene_review.md` | `2b59a686404540dc6a5f566e7118fcd605a0ce0d72ec966964a64f6df030383a` |

Campaign-relative paths in the second table are under
`rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/`, except
for the explicitly rooted kernel path.

# 7. Recommended state effect

Approve application of the exact patch at hash
`bc0e7ed8dc758ebf35c92475d4ef1955457ea8666e70102670ba33daa40549bd`
to the exact graph at hash
`d1ace6e362a41f1a08fc09c8e44ce628758040fa91ae39c152113c275f76352a`,
using `round_index=187`, no extra `judge_ref`, and the official applicator.
Then require an independent post-application field, relation, inverse, and
actual-time replay audit.

The authorized state effect is only: create the strict subordinate proved
reduction; attach it and inconclusive Round-187 evidence to the still-open
hard-M1 small-`t` owner; narrow that owner's next action; append 14 calibrated
overclaim records; and record 20 no-change decisions.  No complete residual,
parent, endpoint theorem, M9 component, bridge, global theorem, or exponent is
promoted.

If either the graph or patch hash changes before application, this verdict is
void and the pre-application audit must be repeated.
