# Round 187 postapplication scope and protected-state audit

## 1. Result

**Verdict: GREEN.** The applied proof graph is the canonical graph with SHA-256

`be0eca9ca93c3534cca958d70b5541d03d28ff993ebfbcbca6be3cd393fae5ff`,

exactly as expected. Relative to the frozen Round-187 starting graph

`d1ace6e362a41f1a08fc09c8e44ce628758040fa91ae39c152113c275f76352a`,

the only changes are the State Patch's authorized footprint: one appended obligation, the five authorized field families on one inherited owner, and the fourteen new rejected-claim records as an exact suffix. The exact effect ledger is

`create/update/correct_rejected/reject/no_change = 1/1/0/14/20`.

The inherited small-t owner `M9-M1-hard-top-high-radical-small-t-residual-estimate` remains `open`. No inherited status, statement, implication, blocker, or `owner` field changed. In particular there is no M9-M1, M9-M2, M9, endpoint, bridge, GC, or exponent drift.

## 2. Exact statement and hypotheses

Let:

- `G0` be the canonical preapplication graph whose SHA-256 is the patch's declared starting hash `d1ace6e...`;
- `P187` be `state_patch.json` with SHA-256 `bc0e7ed8dc758ebf35c92475d4ef1955457ea8666e70102670ba33daa40549bd`;
- `G187` be the current canonical `state/proof_obligations.yml`;
- `J187` be the judge reference `rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/reviews/conductor_round187_adjudication.md`;
- the application parameters be `round_index=187` and the applied timestamp recovered from the created, updated, and rejected records, namely `2026-08-29T15:59:13`.

The claim audited here is the exact byte-level pair of identities

`Reverse_P187(G187) = G0`

and

`Apply_P187(G0; round_index=187, judge_ref=J187, timestamp=2026-08-29T15:59:13) = G187`,

together with the following scope conditions:

1. the only created obligation is `M9-M1-hard-top-t1-high-h-inverse-residue-conductor-reduction`;
2. the only changed inherited obligation is `M9-M1-hard-top-high-radical-small-t-residual-estimate`, and its changed keys are exactly `dependencies`, `evidence`, `next_action`, `last_updated_round`, and `last_updated_at`;
3. the rejected-claim delta is exactly the fourteen patch records, in patch order, as a terminal suffix;
4. for every inherited obligation, the protected fields `status`, `statement_tex`, `implies`, `blockers`, and `owner` are identical before and after application;
5. all evidence and judge-reference paths introduced or cited by the patch resolve to nonempty files.

The comparison uses the repository's canonical serializer and the implementation in `math_collab/proof_obligations.py`; it does not edit the live graph.

## 3. Proof and checks

### 3.1 Hash freeze and canonical form

The current graph's raw bytes equal its canonical `dump_graph` bytes. Both have SHA-256 `be0eca9c...`. The patch bytes have SHA-256 `bc0e7ed8...`. Thus the audit is bound to the exact applied graph and exact patch named in the brief.

The current counts are 389 obligations and 1614 rejected claims. Exact reversal gives 388 obligations and 1600 rejected claims, and the canonical reversed bytes hash to `d1ace6e3...`, exactly the frozen starting hash.

### 3.2 Exact delta

The created obligation is the final obligation and is byte-for-byte the patch record after the authorized application metadata and judge-reference merge. It has:

- status `proved_internal`;
- dependencies exactly `M9-M1-hard-top-t1-residual-fejer-tangent-gcd-reduction` and `Divisor-bound-elementary`;
- empty `implies` and `blockers`;
- the patch's literal strict-packet statement, including the explicit open high-conductor complement and the express denial of any complete high-h, t=1, small-t owner, parent, bridge, theorem, or exponent conclusion;
- `last_updated_round=187` and `last_updated_at=2026-08-29T15:59:13`;
- the judge reference added once to `evidence.inconclusive` under the application rule.

Among all 388 inherited obligations, exactly one object differs:

`M9-M1-hard-top-high-radical-small-t-residual-estimate`.

Its differing keys are exactly:

`dependencies`, `evidence`, `next_action`, `last_updated_round`, `last_updated_at`.

Within those keys the application adds exactly one dependency, the sixteen `evidence.inconclusive` paths declared by the patch, the new patch `next_action`, and Round-187 metadata. No existing dependency or evidence value is deleted or reordered. The current `next_action` is exactly the patch value (654 UTF-8 bytes; SHA-256 `d19c58a021d5ef9161b5c92ff38465fab918bcfd53ab90f717779ae472e9693a`).

The fourteen final rejected claims are, in exact patch order:

1. `Round187-U1-or-zero-mode-proves-high-h`
2. `Round187-low-exact-conductors-prove-high-h`
3. `Round187-positive-high-complement-is-target-safe`
4. `Round187-conductor-centering-gains-Y`
5. `Round187-orientation-antisymmetry-pairs-literal-amplitudes`
6. `Round187-positive-Fourier-Poisson-or-alias-energy-gains-Y`
7. `Round187-high-mode-Fourier-energy-is-small`
8. `Round187-adversarial-capacity-is-literal-lower-mass`
9. `Round187-Fourier-packets-are-physical-incidence-sectors`
10. `Round187-HB-is-a-maximal-fixed-polylogarithmic-cutoff`
11. `Round187-exact-high-conductor-one-sided-relation-is-proved`
12. `Round187-complete-t1-would-prove-the-small-t-owner`
13. `Round187-strict-Fourier-sector-improves-a-global-exponent`
14. `Round187-unsigned-anchor-has-the-same-zero-mode-gain`

Each has exactly the patch reason, Round-187 metadata, and `J187` as its sole evidence item. The preceding 1600 rejected claims are unchanged.

### 3.3 Protected state and ledgers

The stronger all-inherited-node comparison found zero drift in `status`, `statement_tex`, `implies`, `blockers`, or `owner` across all 388 inherited obligations. Pattern-indexed cross-checks also found zero drift in each overlapping protected family:

| Protected family | Inherited nodes checked | Nodes with protected-field drift |
|---|---:|---:|
| `M9` and all `M9-*` nodes | 341 | 0 |
| endpoint-labelled or endpoint-scoped nodes | 185 | 0 |
| bridge-labelled or bridge-scoped nodes | 31 | 0 |
| `GC-*` nodes | 29 | 0 |
| exponent/quarter/one-third/theta-labelled or scoped nodes | 80 | 0 |

These families overlap; their counts are cross-check indices, not a partition. The object-level comparison of all inherited nodes is decisive.

The owner node's status is `open` both before and after application, and its `owner` remains `Codex conductor`. The global edge and status ledgers are:

| Ledger | Frozen start | Applied graph | Authorized explanation |
|---|---:|---:|---|
| dependency edges | 1382 | 1385 | two dependencies on the new node plus its one owner edge |
| implication edges | 326 | 326 | no change; new node has `implies: []` |
| blocker edges | 70 | 70 | no change; new node has `blockers: []` |
| `open` obligations | 34 | 34 | owner remains open |
| `proved_internal` obligations | 309 | 310 | exactly the created strict-packet node |

Every other status count is identical. Because every inherited statement is identical and the new statement explicitly quarantines downstream scope, there is no theorem or exponent drift.

### 3.4 Reverse metadata and replay

The reverse operation removed only the appended created node, the exact fourteen-record rejected suffix, the one added owner dependency, and the sixteen added owner evidence values. It then restored:

- `last_updated_round=186`;
- `last_updated_at=2026-08-28T09:12:29`;
- the exact 949-byte old `next_action`, SHA-256 `85f47b99fa5ae3b17fc7145a939990f94b4bffd9d46bc524639db06c4bb7b785`.

That reversed object serialized to the exact frozen bytes and SHA-256 `d1ace6e3...`. Reapplying the unmodified patch in memory with the frozen application timestamp and exact judge reference produced the exact current object, exact current bytes, and SHA-256 `be0eca9c...`. Official validation returned no issues for the reversed graph, the patch against that graph, the current graph, or the replayed graph.

## 4. First doubtful or unproved step

No defect was found in the postapplication seam. The first place that could have failed was evidence reversal: `J187` is both an explicit owner evidence addition and the runtime judge reference, while the created node also already cites the adjudication positively. The application's unique-list merge adds no duplicate to the owner, adds the authorized inconclusive judge citation to the created node, and adds it to each new rejected record. Removing precisely the patch-added owner values recovers `d1ace6e3...`, and exact replay recovers `be0eca9c...`; therefore this seam closes.

The first mathematical relation still unproved is the exact one-outer-real-part high-conductor complement stated by the created node. That is intentionally open and is not a defect in this scope/lifecycle audit.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Current graph hash and canonical-byte identity | PASS: raw = canonical, SHA-256 `be0eca9c...` |
| Exact patch identity | PASS: SHA-256 `bc0e7ed8...` |
| Exact operation counts | PASS: `1/1/0/14/20` |
| Created-node identity and terminal position | PASS |
| Rejected-claim exact suffix and order | PASS: 14 records, prior 1600 unchanged |
| Only authorized inherited object changes | PASS: one owner; five exact changed keys |
| Owner remains open | PASS: `open -> open` |
| All inherited status/statement/implication/blocker/owner fields | PASS: zero drift across 388 nodes |
| M9-M1/M9-M2/M9/endpoint/bridge/GC/exponent quarantine | PASS |
| Dependency/implication/blocker ledgers | PASS: only authorized `+3/0/0` |
| Evidence and judge paths | PASS: 18 distinct paths, all nonempty |
| Reverse metadata and old `next_action` | PASS: exact |
| Isolated reverse/replay | PASS: byte-exact `d1ace6e3... -> be0eca9c...` |
| Graph and patch validators | PASS: no issues |

The simulation was read-only and in memory; the shared graph and patch were not mutated.

## 6. Dependencies and exact artifacts used

Control inputs:

| Artifact | SHA-256 |
|---|---|
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| `state/proof_obligations.yml` | `be0eca9ca93c3534cca958d70b5541d03d28ff993ebfbcbca6be3cd393fae5ff` |
| `state/active_campaign.yml` (completed Round-187 manifest) | `3a1eebd636a85a39eea3ae05cc82fb750308cedadb7cf836bec26b755640ff45` |
| `rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/state_patch.json` | `bc0e7ed8dc758ebf35c92475d4ef1955457ea8666e70102670ba33daa40549bd` |
| `math_collab/proof_obligations.py` | `384070a83b4ce1f56ebdceb0711680a6e889d4d43af3a40a8b6002319114a437` |
| `rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/controls/preapply_scope_path_second_audit.md` | `53ba67c1e8be795c61479d71629568cd73b37cb1097063ee5b790335eb317f27` |

All 18 distinct evidence/judge paths were re-resolved after application and hashed:

| Evidence or judge artifact | SHA-256 |
|---|---|
| `proofs/kernels/m9_m1_hard_top_t1_high_h_inverse_residue_conductor_reduction.md` | `a9145455a872d57debaf0f91cc8a518f80acef4c1b1fb9115dc1851765a992f2` |
| `rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/candidates/formalized_hard_m1_t1_high_h_inverse_residue_conductor_reduction.md` | `c2f01f57a41695d73d0d1f9716a03328147dbe79f0fcdeb7e8e3465b29779b89` |
| `rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/reports/literal_height_fourier_attack.md` | `4433de37846caa4c9ae0d51ba874221851a331e4a6af13043d4da0f0749ac298` |
| `rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/reports/deletion_resonance_capacity_audit.md` | `5a09310baf8574bf1f2c841cd179a66d22aa5834cc50be555a11ad969569db1a` |
| `rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/reports/blind_high_h_rederivation.md` | `abaf181178b56925bec5fa6b624ddd79be528f4e419e2bff7f22adf9593b9992` |
| `rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/reviews/conductor_round187_report_reconciliation.md` | `b3de83554db114db91b33a8e994f0daa3cd9d9c41550eceabd575fbca1250705` |
| `rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/reviews/inverse_residue_normalization_multiplicity_post_repair_verification.md` | `4fa37825aedfa940bb7ca55b0b4f75145770dc4bb007dc68bf5ee69005ea6739` |
| `rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/reviews/candidate_normalization_post_tex_repair_verification.md` | `b357dc049f9ebf0a8b21b6ed1d816426e166fa78347e2b124822342f48b2b458` |
| `rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/reviews/power_literal_scope_post_tex_repair_verification.md` | `52c2397a88577001fe54c1541a5c831e89e29522320bdefc4ce9c4b1c37b57f8` |
| `rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/reviews/blind_post_unmask_owner_scope_seam_review.md` | `38601b87edfb4706a5206bbd7a7fb704e35b14f0c85d6b8704c698c81ce3ed44` |
| `rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/reviews/final_kernel_candidate_consistency_final_hash_verification.md` | `3e9412b4404ca8399ed2350f459117b6b8b84fe479820a4e12a39da7bad1bb4d` |
| `rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/reviews/final_kernel_power_owner_scope_post_repair_verification.md` | `602a56c4ece7fce4a9e415eb9e95ce7e089dd690630e52fc2f28b16b4c08c0cc` |
| `rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/reviews/final_kernel_formalization_provenance_post_repair_verification.md` | `5f3679b342a9210a2e0baa5c27ff82fc1fa5804bc662c8ea6e9c56886e0e417e` |
| `rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/reviews/conductor_round187_adjudication.md` | `c6949ba7089e5d70c377c658771ef4bcf6be1ad603b453739de615cf91862ef5` |
| `rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/synthesis.md` | `4e65ce906acbd0e1b7de18d5a6b728e560c7e3641ee4bbc349443566574a37e1` |
| `rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/controls/conductor_round187_wolfram_inverse_residue_check.md` | `032d8039636b0e4e2040caed7c0d2ade507d111a7f966b9b40f03676fadd1113` |
| `rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/controls/inverse_residue_exact_check.wls` | `e818367a710c4051f9259966133ca48b94810a55544b4b0ec3d3fbab15a06bcd` |
| `rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/reviews/final_kernel_formalization_provenance_hygiene_review.md` | `2b59a686404540dc6a5f566e7118fcd605a0ce0d72ec966964a64f6df030383a` |

Every listed path exists and is nonempty. The historical preapplication graph is bound by the exact recovered canonical hash `d1ace6e3...`; no separate mutable copy was trusted.

## 7. Recommended state effect

**Retain the applied Round-187 graph unchanged.** This postapplication audit warrants GREEN lifecycle closure for the exact `1/1/0/14/20` patch. No repair, rollback, additional graph mutation, owner promotion, parent promotion, bridge change, theorem claim, or exponent change is indicated.
