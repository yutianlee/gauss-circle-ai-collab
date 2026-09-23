# Round 196 post-apply graph and evidence hygiene audit

- Campaign: `m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate`
- Round: 196
- Role: independent post-apply graph/evidence auditor
- Applied State Patch SHA-256:
  **013eae5d57e3854acf2ef9d4c9d72ab94fa9da2af64e97f27b43c701cdeb7c9d**
- Live post-apply graph SHA-256:
  **b9b95784b097b3e30bed95f418ae14e57bf5f03a4a52975beeefa8db85b7f8ae**
- Status: post-apply control only; no shared-state edit

## 1. Result

**PASS.** The live graph has exactly the requested post-apply SHA-256
`b9b95784b097b3e30bed95f418ae14e57bf5f03a4a52975beeefa8db85b7f8ae`
and passes the repository graph validator.

The terminal footprint is exact:

- the obligation count remains 395;
- exactly two existing obligations were updated, with statuses unchanged;
- the same 24 fresh paths are a contiguous ordered suffix of each
  target's `inconclusive` evidence list;
- all 24 files exist and retain their pre-apply hashes;
- exactly 20 new rejected claims were appended in State Patch order,
  with exact reasons, Round-196 metadata, and the adjudication as evidence;
- the rejected-claim ledger now contains 1,775 pairwise distinct IDs; and
- mechanically reversing only those declared mutations reproduces the
  starting graph byte-for-byte at SHA-256
  `f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`.

The current candidate, durable kernel, adjudication, and synthesis hashes
are mutually consistent. No stale candidate or kernel hash has become the
terminal artifact, and no target, owner, bridge, theorem, or exponent was
promoted.

## 2. Exact statement and hypotheses

The audit compares the applied patch with the live
`state/proof_obligations.yml` after application at
`2026-08-30T12:00:58`.

The two updated records are:

| Obligation | Status | Round/time | New inconclusive suffix |
|---|---|---|---:|
| `M9-M1-hard-top-high-radical-small-t-residual-estimate` | `open` | 196 / `2026-08-30T12:00:58` | 24 paths, positions 227--250 of 250 |
| `M9-M1-hard-top-t1-rho-large-P2-absolute-capacity-sectors` | `proved_internal` | 196 / `2026-08-30T12:00:58` | 24 paths, positions 7--30 of 30 |

Both live `next_action` values equal the applied patch exactly. The first
record still has zero positive and zero negative evidence entries. The
second retains its pre-existing 15 positive entries and zero negative
entries; the Round-196 material is confined to its inconclusive bucket.

The patch created no obligation, corrected no old rejection, and included
27 `no_change` entries. Thus the post-apply claim remains only
`on_shell_carrier_denominator_self_return_no_go`: a mechanism boundary,
not a proof of the remaining literal \(P_2\) estimate.

## 3. Proof or derivation

### 3.1 Exact terminal-footprint replay

Repository validation returns:

`Graph OK: state/proof_obligations.yml`.

For a stronger footprint test, I loaded the live graph, then performed
only the inverse operations stated by the patch:

1. removed the 24 added inconclusive paths from each updated obligation;
2. restored the two `next_action` strings and their Round-195 metadata;
3. removed the 20 appended `Round196-*` rejected-claim records; and
4. changed nothing else.

Serializing that in-memory reversal with the repository's canonical graph
serializer gives

\[
 \operatorname{SHA256}(\text{reversed live graph})
 =
 \texttt{f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2},
\tag{PHA.1}
\]

which is exactly the patch's starting graph hash. The reversed counts are
395 obligations and 1,755 rejected claims. This byte-exact recovery rules
out any hidden graph mutation beyond the declared footprint.

### 3.2 Attached evidence

Let `R/` abbreviate
`rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/`.
The following are the 24 ordered paths now attached to each target. Every
file exists, and every current hash matches the pre-apply provenance audit.

| # | Evidence path | Current SHA-256 |
|---:|---|---|
| 1 | `proofs/kernels/m9_m1_hard_top_t1_p2_on_shell_carrier_normalization_self_return.md` | `51da98a07b52706a510f9ea07c52d952323e8282cb3ab6e100347c71b63f54fb` |
| 2 | `R/candidates/formalized_hard_m1_t1_p2_on_shell_carrier_self_return.md` | `5174129858c2ced67c2d637a0cbdb1153d1b18da7491c1b80316532485497380` |
| 3 | `R/reports/literal_on_shell_carrier_commutator_attack.md` | `5e419a17d867ca8d685b12c23f8e462725894dad4ec3ee78fcbf61eed8ad8684` |
| 4 | `R/reports/carrier_collision_endpoint_hostile_audit.md` | `c7b46cd6e9b5caba1b49a782d3e117ffc349a2aa815771f0ab95fa3d3fac6cdc` |
| 5 | `R/reports/blind_on_shell_phase_rederivation.md` | `a1f0f342c4e19f43cf1e6f216821af46fa51ff6fd134b20f14d22db1fdecd80e` |
| 6 | `R/reviews/conductor_round196_operator_normalization_analysis.md` | `5d3b8ae1acef230a3516c3e042a008bd1bba150f9dec31accd04151050ea1788` |
| 7 | `R/reviews/conductor_round196_report_reconciliation.md` | `208b69cb7905b41e08d4dc004034c1a50434ef8d64175656dad060640ef772d3` |
| 8 | `R/reviews/blind_post_unmask_on_shell_carrier_review.md` | `f4c4045bd512607f7a8617b7e7ce112c90efb91d0eba4fdfe21fe30b51a77949` |
| 9 | `R/reviews/on_shell_normalization_live_wrap_seam_review.md` | `ccce88dcb4c90b60984232e2675d74e9a6c4f98004fdf85320fe8de404208082` |
| 10 | `R/reviews/on_shell_normalization_live_wrap_postrepair_verification.md` | `281782967401cb142f95d4a0d8892b846520689851e31d18104a6a40bea02641` |
| 11 | `R/reviews/commutator_power_owner_scope_seam_review.md` | `acd413701ce21c002a6ca0b3c8bf3d905bd262b1a4283a1ab20721096daed785` |
| 12 | `R/reviews/commutator_power_owner_scope_postrepair_verification.md` | `51b04cb8cf2fba130e37696659e055b071aecb18baa8b18cc06f7ef5d8de786a` |
| 13 | `R/reviews/commutator_power_owner_scope_final_verification.md` | `273afb36679a4b1f24f2dbc7708660079ef474c19130618a6fd5f3d892054cfa` |
| 14 | `R/reviews/blind_candidate_postrepair_consistency_verification.md` | `d1c037c1b4a7190f235101c4b50368a354856a964a47e4103a5b528bc04f2f00` |
| 15 | `R/reviews/final_kernel_normalization_formalization_review.md` | `e4c0d4fc80a64c38e981f930dd7090458f02718bd963a9d605a79d716367c9b4` |
| 16 | `R/reviews/final_kernel_normalization_formalization_postrepair_verification.md` | `c0ffcf6f56fcd9eff5a5063379e0946c2723b39b3d1770618cab5136cdae028c` |
| 17 | `R/reviews/final_kernel_power_owner_scope_review.md` | `fa5c259dfa859620b585eeb0245470e5da8d43a001e2b7b283b54a3650fd8223` |
| 18 | `R/reviews/final_kernel_power_owner_scope_postrepair_verification.md` | `d5855e876a3aa8fa4becb0b0589da9eb960fd7da2273837d82879a8217ea7a66` |
| 19 | `R/reviews/final_kernel_power_owner_scope_final_verification.md` | `0dc0edec1a3bd8d12ce6c52e188211318d52bd2710f3b7346e12e4f67b8b1a78` |
| 20 | `R/reviews/final_kernel_blind_consistency_review.md` | `1f6dd336b77ba610ccb52e59731efd6179fa4aab70ac3c66c423a3d3dcf5d929` |
| 21 | `R/reviews/final_kernel_blind_postrepair_verification.md` | `ed9b9bb6e243edad97dc54c7e79bba540c975d835c9d1912dbff4fa75ff1cdbd` |
| 22 | `R/reviews/conductor_round196_adjudication.md` | `e760c0685789b583e16787fa812320faf608d16775f1abee78d38a610e7ce90d` |
| 23 | `R/controls/conductor_round196_launch_validation.md` | `de548e06a0ad3519efe70c1b4510ab5ddd67df9af6201e1dd9ff20ef1ec5b46f` |
| 24 | `R/synthesis.md` | `02bfb23cb8523d7301e6fc65babe79a695070710b9b045d62c64ab495a53a20c` |

The live lists equal the patch lists element-for-element and occur as
contiguous suffixes. No path was misbucketed into positive or negative
evidence.

### 3.3 Rejected-claim freshness and order

The live rejected-claim ledger grew from 1,755 to 1,775 records and now
has 1,775 distinct IDs. Its final 20 IDs are exactly, in patch order:

1. `Round196-parity-restored-shadow-is-literal-exact-conductor-atom`;
2. `Round196-dropping-EU-preserves-exact-conductor`;
3. `Round196-multiplying-one-mode-by-EU-stays-in-packet`;
4. `Round196-literal-x-step-multiplier-is-minus-eaq`;
5. `Round196-live-wrap-supplies-denominator-cancellation`;
6. `Round196-coprimality-mask-deletes-wrap-without-boundary`;
7. `Round196-actual-height-event-is-uniform-Delta2-in-x`;
8. `Round196-T0-rho-is-never-unit`;
9. `Round196-unit-inverse-T0-rows-prove-the-branch`;
10. `Round196-gamma-may-replace-beta-in-farey-selector`;
11. `Round196-minus-far-step-moves-common-x`;
12. `Round196-primitive-4q-carrier-alone-proves-saving`;
13. `Round196-cumulative-antiderivative-is-cost-free`;
14. `Round196-parity-commutator-is-boundary-only`;
15. `Round196-full-anchor-recombination-estimates-high-conductor`;
16. `Round196-capacity-is-literal-lower-mass`;
17. `Round196-no-go-disproves-literal-P2`;
18. `Round196-no-go-proves-strict-sector`;
19. `Round196-no-go-closes-original-t1-or-owner`; and
20. `Round196-no-go-improves-global-exponent`.

Their reasons equal the State Patch reasons element-for-element. Every
record has `last_updated_round: 196`,
`last_updated_at: 2026-08-30T12:00:58`, and the single evidence path
`R/reviews/conductor_round196_adjudication.md`. Thus they are fresh,
ordered, uniformly sourced, and not duplicates of earlier rejected
claims.

### 3.4 Terminal provenance chain

The current terminal hashes are:

| Artifact | SHA-256 | Embedded provenance |
|---|---|---|
| Formal candidate | `5174129858c2ced67c2d637a0cbdb1153d1b18da7491c1b80316532485497380` | Starting graph `f1f6...cce2` |
| Durable kernel | `51da98a07b52706a510f9ea07c52d952323e8282cb3ab6e100347c71b63f54fb` | Candidate `517412...7380` |
| Adjudication | `e760c0685789b583e16787fa812320faf608d16775f1abee78d38a610e7ce90d` | Candidate `517412...7380` and kernel `51da98...54fb` |
| Synthesis | `02bfb23cb8523d7301e6fc65babe79a695070710b9b045d62c64ab495a53a20c` | Kernel `51da98...54fb` |

All embedded full hashes match the current files. Historical stage hashes
remain only inside repair-chain reviews in the inconclusive suffix; none
is selected by the kernel, adjudication, synthesis, or live graph as the
terminal candidate/kernel provenance.

## 4. First doubtful or unproved step

No post-apply graph or evidence-hygiene defect was found. The first
potential provenance ambiguity remains the historical reviews carrying
preterminal hashes. Their location in the inconclusive bucket and the
current terminal chain in Section 3.4 resolve that ambiguity.

The first mathematical theorem still unproved is the coefficient-sensitive
joint \(++,+-,-+,--\) estimate for the complete literal \(P_2\) remainder
before positive norms. The live graph does not mark it proved.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Requested live SHA | **PASS.** Full graph SHA-256 is `b9b95784b097b3e30bed95f418ae14e57bf5f03a4a52975beeefa8db85b7f8ae`. |
| Graph schema/paths | **PASS.** Repository graph validation returns `Graph OK`. |
| Exact reverse replay | **PASS.** Removing only declared mutations reconstructs the starting graph hash byte-for-byte. |
| Obligation footprint | **PASS.** Count remains 395; exactly two records have the Round-196 update. |
| Status footprint | **PASS.** The open owner remains `open` and the accepted capacity node remains `proved_internal`. |
| Evidence attachment | **PASS.** Both targets contain all 24 paths as the exact ordered suffix in `inconclusive`. |
| Evidence existence | **PASS.** 24/24 paths exist. |
| Evidence currency | **PASS.** 24/24 hashes match the pre-apply audit. |
| Rejected count/uniqueness | **PASS.** 1,775 records have 1,775 distinct IDs. |
| Rejected order/reasons | **PASS.** The final 20 IDs and reasons equal the patch element-for-element. |
| Rejected metadata/source | **PASS.** All 20 share Round 196, the apply timestamp, and the adjudication evidence path. |
| Candidate/kernel hashes | **PASS.** Files and embedded bindings match `517412...7380` and `51da98...54fb`. |
| Adjudication/synthesis hashes | **PASS.** Current files are `e760c0...e90d` and `02bfb2...a20c` and embed current terminal provenance. |
| Stale-hash quarantine | **PASS.** Preterminal hashes occur only in historical inconclusive reviews. |
| Terminal scope | **PASS.** Only the route-scoped no-go was recorded; no target, owner, theorem, bridge, or exponent was promoted. |

## 6. Dependencies and exact artifacts used

This audit used:

1. `state/proof_obligations.yml` at post-apply SHA-256
   `b9b95784b097b3e30bed95f418ae14e57bf5f03a4a52975beeefa8db85b7f8ae`;
2. the applied `state_patch.json` at SHA-256
   `013eae5d57e3854acf2ef9d4c9d72ab94fa9da2af64e97f27b43c701cdeb7c9d`;
3. the 24 attached evidence files and current hashes in Section 3.2;
4. `R/controls/preapply_evidence_provenance_hygiene_audit.md` at
   SHA-256
   `2109891abf0d55678884f4861b7d787ab310274e195f1ef28b7a87db2ec009b7`;
5. `protocol.md`; and
6. the repository graph loader, canonical serializer, and validator.

No shared state, proof draft, validation matrix, synthesis, kernel,
candidate, patch, or other artifact was edited. Reverse replay occurred
only in memory.

## 7. Recommended state effect

**PASS the applied graph for the post-apply graph/evidence hygiene gate.**
The live graph is an exact application of the audited patch and needs no
repair. Retain the terminal graph at SHA-256
`b9b95784b097b3e30bed95f418ae14e57bf5f03a4a52975beeefa8db85b7f8ae`
for subsequent closure controls.

The only new durable mathematical effect is
`on_shell_carrier_denominator_self_return_no_go`. Complete \(P_2\),
\(P_1\), all remaining original-\(t\) incidences, both M1 parents, GAR,
every M2 parent, endpoint uniformity, M9, both bridges, the quarter
theorem, and every exponent remain unchanged.
