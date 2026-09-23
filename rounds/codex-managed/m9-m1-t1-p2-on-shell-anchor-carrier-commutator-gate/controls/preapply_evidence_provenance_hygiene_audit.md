# Round 196 pre-apply evidence-provenance and hygiene audit

- Campaign: `m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate`
- Round: 196
- Role: independent pre-apply provenance/hygiene auditor
- State Patch SHA-256:
  **013eae5d57e3854acf2ef9d4c9d72ab94fa9da2af64e97f27b43c701cdeb7c9d**
- Live graph SHA-256:
  **f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2**
- Status: pre-apply control only; no shared-state edit

## 1. Result

**PASS.** The current `state_patch.json` is valid JSON, passes the
repository State Patch validator, and produces a graph with zero
validation issues in an in-memory Round-196 dry run. Its starting hash
matches the live graph exactly.

Both updated obligations receive the same 24-path evidence set solely in
the `inconclusive` bucket. All 24 paths exist, are pairwise unique
within each update, are absent from the targets' existing evidence, and
support the claimed route-scoped no-go or its repair/review provenance.
The patch creates no obligation, changes no status, and promotes no
sector, owner, theorem, bridge, or exponent.

The 20 rejected-claim IDs are pairwise unique, absent from both the
1,755 live rejected-claim IDs and the 395 live obligation IDs, and
therefore genuinely new. The current candidate/kernel/adjudication/
synthesis provenance chain is consistent. Older candidate and kernel
hashes occur only inside explicitly historical repair-chain reviews
which are themselves added as inconclusive evidence; no stale hash is
presented as the terminal candidate or durable kernel.

## 2. Exact statement and hypotheses

The audited patch is
`rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/state_patch.json`.

Its operative mutation has exactly:

- `create`: 0;
- `update`: 2;
- `correct_rejected`: 0;
- `reject`: 20;
- `no_change`: 27.

The two update targets are:

1. `M9-M1-hard-top-high-radical-small-t-residual-estimate`, currently
   `open`; and
2. `M9-M1-hard-top-t1-rho-large-P2-absolute-capacity-sectors`,
   currently `proved_internal`.

Neither update contains a `status` field. Each adds exactly the same 24
fresh paths under `evidence_added.inconclusive` and replaces only
`next_action`. The reversibility block reproduces both current
`next_action` strings byte-for-byte and both current metadata pairs:
`last_updated_round: 195` and
`last_updated_at: 2026-08-30T04:40:21`.

The patch's mathematical classification is therefore precise: Round 196
adds a durable obstruction to one proposed completion mechanism without
changing the accepted absolute-capacity result, proving the remaining
\(P_2\) region, or changing the open hard small-\(t\) owner.

## 3. Proof or derivation

### 3.1 Evidence existence and classification

Let `R/` abbreviate
`rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/`.
The following table checks every unique evidence path. “Historical
repair” means the artifact is useful provenance for a failed or repaired
intermediate version; it is not being used to certify the terminal hash.

| # | Evidence path | Current SHA-256 | Why `inconclusive` is supported |
|---:|---|---|---|
| 1 | `proofs/kernels/m9_m1_hard_top_t1_p2_on_shell_carrier_normalization_self_return.md` | `51da98a07b52706a510f9ea07c52d952323e8282cb3ab6e100347c71b63f54fb` | Terminal route-scoped no-go; expressly not target-safe. |
| 2 | `R/candidates/formalized_hard_m1_t1_p2_on_shell_carrier_self_return.md` | `5174129858c2ced67c2d637a0cbdb1153d1b18da7491c1b80316532485497380` | Recommends only no-go/inconclusive evidence and leaves the target open. |
| 3 | `R/reports/literal_on_shell_carrier_commutator_attack.md` | `5e419a17d867ca8d685b12c23f8e462725894dad4ec3ee78fcbf61eed8ad8684` | Finds the target unproved and retains complete \(P_2\) open. |
| 4 | `R/reports/carrier_collision_endpoint_hostile_audit.md` | `c7b46cd6e9b5caba1b49a782d3e117ffc349a2aa815771f0ab95fa3d3fac6cdc` | Exact mechanism-scoped no-go; recommends no graph promotion. |
| 5 | `R/reports/blind_on_shell_phase_rederivation.md` | `a1f0f342c4e19f43cf1e6f216821af46fa51ff6fd134b20f14d22db1fdecd80e` | Independently derives the shadow and self-return, but says revise and do not promote. |
| 6 | `R/reviews/conductor_round196_operator_normalization_analysis.md` | `5d3b8ae1acef230a3516c3e042a008bd1bba150f9dec31accd04151050ea1788` | Establishes the normalization obstruction and explicitly withholds every promotion. |
| 7 | `R/reviews/conductor_round196_report_reconciliation.md` | `208b69cb7905b41e08d4dc004034c1a50434ef8d64175656dad060640ef772d3` | Selects only a route no-go and directs inconclusive evidence on the open owner. |
| 8 | `R/reviews/blind_post_unmask_on_shell_carrier_review.md` | `f4c4045bd512607f7a8617b7e7ce112c90efb91d0eba4fdfe21fe30b51a77949` | Repairs the literal normalization and passes only the route-scoped no-go. |
| 9 | `R/reviews/on_shell_normalization_live_wrap_seam_review.md` | `ccce88dcb4c90b60984232e2675d74e9a6c4f98004fdf85320fe8de404208082` | Historical REPAIR review; permits only later inconclusive/no-go use. |
| 10 | `R/reviews/on_shell_normalization_live_wrap_postrepair_verification.md` | `281782967401cb142f95d4a0d8892b846520689851e31d18104a6a40bea02641` | PASSes the repaired route no-go and forbids a target-safe obligation. |
| 11 | `R/reviews/commutator_power_owner_scope_seam_review.md` | `acd413701ce21c002a6ca0b3c8bf3d905bd262b1a4283a1ab20721096daed785` | Historical REPAIR review; owner boundary is inconclusive only. |
| 12 | `R/reviews/commutator_power_owner_scope_postrepair_verification.md` | `51b04cb8cf2fba130e37696659e055b071aecb18baa8b18cc06f7ef5d8de786a` | Historical repair-chain review; explicitly says no graph promotion before final repair. |
| 13 | `R/reviews/commutator_power_owner_scope_final_verification.md` | `273afb36679a4b1f24f2dbc7708660079ef474c19130618a6fd5f3d892054cfa` | Final candidate PASS with only inconclusive evidence on the existing owner. |
| 14 | `R/reviews/blind_candidate_postrepair_consistency_verification.md` | `d1c037c1b4a7190f235101c4b50368a354856a964a47e4103a5b528bc04f2f00` | Historical candidate-stage PASS; accepts internal consistency only, not the target. |
| 15 | `R/reviews/final_kernel_normalization_formalization_review.md` | `e4c0d4fc80a64c38e981f930dd7090458f02718bd963a9d605a79d716367c9b4` | Historical kernel review; recommends only route-no-go/inconclusive evidence. |
| 16 | `R/reviews/final_kernel_normalization_formalization_postrepair_verification.md` | `c0ffcf6f56fcd9eff5a5063379e0946c2723b39b3d1770618cab5136cdae028c` | Current-hash PASS; retains complete \(P_2\) and all owners open. |
| 17 | `R/reviews/final_kernel_power_owner_scope_review.md` | `fa5c259dfa859620b585eeb0245470e5da8d43a001e2b7b283b54a3650fd8223` | Historical kernel-stage PASS of power/scope only; assigns inconclusive evidence. |
| 18 | `R/reviews/final_kernel_power_owner_scope_postrepair_verification.md` | `d5855e876a3aa8fa4becb0b0589da9eb960fd7da2273837d82879a8217ea7a66` | Historical post-repair PASS; still withholds the complete \(P_2\) target. |
| 19 | `R/reviews/final_kernel_power_owner_scope_final_verification.md` | `0dc0edec1a3bd8d12ce6c52e188211318d52bd2710f3b7346e12e4f67b8b1a78` | Current-hash final PASS; owner evidence remains inconclusive. |
| 20 | `R/reviews/final_kernel_blind_consistency_review.md` | `1f6dd336b77ba610ccb52e59731efd6179fa4aab70ac3c66c423a3d3dcf5d929` | Historical REPAIR at a preterminal kernel hash; no target promotion. |
| 21 | `R/reviews/final_kernel_blind_postrepair_verification.md` | `ed9b9bb6e243edad97dc54c7e79bba540c975d835c9d1912dbff4fa75ff1cdbd` | Current-hash PASS; promotes/retains only the route-scoped no-go. |
| 22 | `R/reviews/conductor_round196_adjudication.md` | `e760c0685789b583e16787fa812320faf608d16775f1abee78d38a610e7ce90d` | Adjudicates no new sector and orders only inconclusive evidence. |
| 23 | `R/controls/conductor_round196_launch_validation.md` | `de548e06a0ad3519efe70c1b4510ab5ddd67df9af6201e1dd9ff20ef1ec5b46f` | Launch/provenance control; records no graph or exponent change and quarantines promotion. |
| 24 | `R/synthesis.md` | `02bfb23cb8523d7301e6fc65babe79a695070710b9b045d62c64ab495a53a20c` | Closes only the mechanism and states that the patch adds inconclusive evidence. |

Every row exists as a regular file. Both update lists contain these 24
rows in the same order, contain no duplicates, and are entirely fresh
relative to the current evidence of each target.

### 3.2 Current hash chain and stale-hash quarantine

The terminal chain is:

\[
\begin{array}{c|c}
\text{artifact} & \text{current SHA-256}\\ \hline
\text{formal candidate} &
5174129858c2ced67c2d637a0cbdb1153d1b18da7491c1b80316532485497380\\
\text{durable kernel} &
51da98a07b52706a510f9ea07c52d952323e8282cb3ab6e100347c71b63f54fb\\
\text{conductor adjudication} &
e760c0685789b583e16787fa812320faf608d16775f1abee78d38a610e7ce90d\\
\text{synthesis} &
02bfb23cb8523d7301e6fc65babe79a695070710b9b045d62c64ab495a53a20c
\end{array}
\tag{PHA.1}
\]

The durable kernel embeds the current candidate hash. The adjudication
embeds both the current candidate and current kernel hashes. The
synthesis embeds the current kernel hash. All embedded values match the
files byte-for-byte.

Three obsolete stage hashes remain only as historical text:

- candidate `d996d60d09ed8b6b58cf9cc3e7462215843780f00938840ed425247ec92e9bf9`
  in two candidate repair-chain reviews;
- kernel `2e82adeced8bdd734328a107c435a9db775e1d40e10b14c02a31530d00bf96d8`
  in one first-stage kernel scope review; and
- kernel `dd1da266a32701f3e6f727feeec8868247a9aac6f56e36e613f3e721fc8b5ee8`
  in three intermediate kernel reviews.

Those review files document the repair sequence and sit only in the
`inconclusive` bucket. The patch's direct candidate and kernel paths
resolve to the current hashes in (PHA.1), while adjudication, synthesis,
and all three final current-hash post-repair verifications select those
same hashes. Hence no stale candidate/kernel hash is promoted.

### 3.3 Rejected IDs, reversibility, and dry-run graph

The 20 `Round196-*` reject IDs have:

- 20 distinct values;
- zero overlap with current rejected claims;
- zero overlap with current proof-obligation IDs; and
- zero overlap with either update or any `no_change` ID.

Their reasons are all consequences of the audited kernel/adjudication:
literal versus parity-restored atom, \(E_U\) conductor mixing, live/dead
wrap, \(T=0\) unit inverses, \(\beta/\gamma\), orientation geometry,
capacity versus lower mass, and the no-target/no-exponent boundary.

The two restoration records exactly match the live graph. An in-memory
application at Round 196 updates the two named obligations, appends the
20 new rejected claims, records all 27 `no_change` IDs, and yields zero
`validate_graph` issues. No filesystem state was written.

## 4. First doubtful or unproved step

No blocking provenance or hygiene defect was found. The first potential
trap is the presence of historical PASS/REPAIR reviews carrying obsolete
candidate or kernel hashes. They cannot certify the terminal files in
isolation. Here that trap is resolved because the patch classifies every
such path as inconclusive, and the current-hash kernel, three independent
current-hash final verifications, adjudication, and synthesis explicitly
supersede them.

Mathematically, the first unproved theorem remains the coefficient-
sensitive joint \(++,+-,-+,--\) estimate for the complete literal
\(P_2\) remainder before positive norms. The patch does not claim it.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| JSON parse | **PASS.** PowerShell JSON parsing succeeds. |
| Repository patch validator | **PASS.** `python -m math_collab.validate_state_patch --patch ...` returns `Patch OK`. |
| In-memory application | **PASS.** Round-196 dry run completes and the resulting graph has zero validation issues. |
| Starting graph | **PASS.** Live graph SHA-256 equals the patch's `starting_graph_sha256`. |
| Evidence paths | **PASS.** 24/24 unique paths exist; both target lists are identical and duplicate-free. |
| Evidence freshness | **PASS.** All 24 paths are new to both target evidence ledgers. |
| Inconclusive support | **PASS.** Every path records the route no-go, a repair/review seam, or launch/closure provenance; none proves the remaining target. |
| Target statuses | **PASS.** No `status` mutation occurs; the open owner remains open and the accepted capacity node remains `proved_internal`. |
| Reversibility | **PASS.** Both restored `next_action` values and metadata records match the live graph exactly. |
| Rejected IDs | **PASS.** 20/20 are unique and new, with zero collision against rejected claims or obligations. |
| Other IDs | **PASS.** The 2 update and 27 `no_change` IDs are unique, disjoint where required, and recognized by the validator. |
| Candidate/kernel binding | **PASS.** Current candidate `517412...7380` is embedded by current kernel `51da98...54fb`. |
| Adjudication/synthesis currency | **PASS.** Adjudication embeds current candidate/kernel hashes; synthesis embeds the current kernel hash. |
| Stale-hash quarantine | **PASS.** Obsolete hashes occur only in historical repair-chain reviews added as inconclusive evidence. |
| Promotion scope | **PASS.** `create` is empty; no sector, owner, theorem, bridge, or exponent is promoted. |

## 6. Dependencies and exact artifacts used

This audit used:

1. the State Patch at SHA-256
   `013eae5d57e3854acf2ef9d4c9d72ab94fa9da2af64e97f27b43c701cdeb7c9d`;
2. `state/proof_obligations.yml` at SHA-256
   `f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`;
3. all 24 evidence files and hashes enumerated in Section 3.1;
4. `protocol.md`; and
5. the repository's `math_collab.validate_state_patch` and
   `math_collab.proof_obligations` validation/apply routines.

No web source, numerical theorem evidence, or unlisted proof artifact was
used. The patch and graph were read and dry-run in memory only; no shared
state, proof draft, validation matrix, synthesis, kernel, candidate, or
other artifact was edited.

## 7. Recommended state effect

**PASS the current State Patch for the provenance/hygiene gate.** No
repair is required by this audit. It may proceed to the conductor's
remaining pre-apply controls and mechanical application, provided the
live graph still hashes to
`f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`
and the patch still hashes to
`013eae5d57e3854acf2ef9d4c9d72ab94fa9da2af64e97f27b43c701cdeb7c9d`
at apply time.

After application, retain only
`on_shell_carrier_denominator_self_return_no_go` as durable route-boundary
evidence. Complete \(P_2\), \(P_1\), all remaining original-\(t\)
incidences, both M1 parents, GAR, every M2 parent, endpoint uniformity,
M9, both bridges, the quarter theorem, and every exponent remain
unchanged.
