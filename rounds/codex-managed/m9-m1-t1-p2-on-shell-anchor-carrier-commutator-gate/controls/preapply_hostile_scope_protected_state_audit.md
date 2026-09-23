# Pre-apply hostile scope and protected-state audit

- Campaign: `m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate`
- Round: 196
- Role: independent hostile pre-apply protected-scope audit
- Starting graph SHA-256: `f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`
- State Patch SHA-256: `013eae5d57e3854acf2ef9d4c9d72ab94fa9da2af64e97f27b43c701cdeb7c9d`
- Durable kernel SHA-256: `51da98a07b52706a510f9ea07c52d952323e8282cb3ab6e100347c71b63f54fb`
- Verdict: **PASS**

## 1. Result

**Protected-scope lemma.**  Apply the current State Patch to the current
graph by the repository's `apply_state_patch` semantics with round index
196.  Then:

1. no obligation is created, removed, promoted, demoted, or rejected;
2. exactly two proof-obligation records change:
   `M9-M1-hard-top-high-radical-small-t-residual-estimate` and
   `M9-M1-hard-top-t1-rho-large-P2-absolute-capacity-sectors`;
3. in each of those two records, the only changed fields are the append to
   `evidence.inconclusive`, `next_action`, `last_updated_round`, and
   `last_updated_at`;
4. every obligation's `status`, `dependencies`, `statement_tex`, `implies`,
   and `blockers` is identical before and after the simulated application;
5. all 27 declared `no_change` obligation records are byte-for-structure
   identical under canonical JSON serialization before and after application;
6. the existing 1,755 rejected-claim records are unchanged and 20 new,
   pairwise distinct, kernel-supported route-falsifier records are appended;
   and
7. the internal exponent (1/3), external benchmark
   (0.3144831759740614\ldots), both quarter bridges, endpoint/M9 parents,
   and the (1/4) target remain exactly protected.

Thus the requested statement "only two intended nodes mutate" is correct
when "nodes" means proof-obligation nodes.  It must not be strengthened to
"only two graph records change": the patch intentionally appends 20 new
records to `rejected_claims`.  Those appends neither alter an existing
rejection nor change an obligation status.

## 2. Exact statement and hypotheses

The conclusion is conditional on the following exact inputs and application
semantics.

1. The graph is the current `state/proof_obligations.yml` at the starting
   SHA-256 displayed above.  It contains 395 proof obligations and 1,755
   rejected claims.
2. The patch is the current Round-196 `state_patch.json` at the displayed
   SHA-256.  Its operation counts are

$$
   (\#\mathrm{create},\#\mathrm{update},\#\mathrm{correct\_rejected},
     \#\mathrm{reject},\#\mathrm{no\_change})=(0,2,0,20,27).
$$
3. Application uses the checked repository implementation in
   `math_collab/proof_obligations.py`.  A supplied `judge_ref`, if any, can
   add evidence only inside the newly appended rejected-claim records in
   this patch; it cannot mutate a protected obligation.
4. The mathematical meaning of each rejection is tested only against the
   durable kernel at its displayed SHA-256.  The kernel is a route-scoped
   normalization/support no-go, not a proof of the complete (P_2) estimate,
   a strict sector, a literal lower bound, an owner closure, or an exponent
   improvement.
5. Any change to the graph, patch, kernel, or state-application code after
   the hashes recorded here invalidates this pre-apply verdict and requires
   replay.

## 3. Proof or derivation

### 3.1. Operation and namespace audit

The five patch categories contain no duplicate IDs internally and no ID
occurs in two categories.  Both update entries have exactly the fields
`id`, `evidence_added`, and `next_action`; neither contains `status`,
`dependencies`, `statement_tex`, `implies`, `blockers`, `type`, or any
promotion field.  `create` and `correct_rejected` are empty.

Each update appends the same 24 evidence paths to the inconclusive bucket.
All 24 paths exist, are pairwise distinct, and were absent from every evidence
bucket of the corresponding current node.  The prior `next_action`,
`last_updated_round`, and `last_updated_at` values recorded by the patch's
reversibility block exactly equal the current graph values for both nodes.

An in-memory application gives the following complete obligation diff.

| Obligation | Prior status | Changed fields | Inconclusive evidence delta | Protected fields |
|---|---:|---|---:|---|
| `M9-M1-hard-top-high-radical-small-t-residual-estimate` | `open` | `evidence`, `next_action`, `last_updated_round`, `last_updated_at` | +24 | status, dependencies, statement, implications, blockers unchanged |
| `M9-M1-hard-top-t1-rho-large-P2-absolute-capacity-sectors` | `proved_internal` | `evidence`, `next_action`, `last_updated_round`, `last_updated_at` | +24 | status, dependencies, statement, implications, blockers unchanged |

There are no created or removed obligations.  A comparison across all 395
obligations proves that all statuses, dependency lists, statements,
implication lists, and blocker lists remain equal.  The canonical diagnostic
SHA-256 of this global protected-field map is
`42e4a73b4059e5cd4e174dae842a6a44eb37b7a23bc6431acb9412e5f6fbd009`
both before and after the simulated application.  Hence there is no explicit
or implicit promotion.

### 3.2. The 27 `no_change` records

Every declared ID exists in the starting graph, the 27 IDs are distinct,
and none overlaps an update or rejection.  Exact before/after object equality
holds for all of the following.

| Protected group | Exact IDs |
|---|---|
| Accepted hard-(t=1) reductions | `M9-M1-hard-top-t1-rho-large-gcd-scaled-close-sector`; `M9-M1-hard-top-t1-rho-large-farey-covector-reduction`; `M9-M1-hard-top-t1-fast-signed-inverse-transport-reduction`; `M9-M1-hard-top-t1-high-h-dual-frequency-projective-reduction`; `M9-M1-hard-top-t1-high-h-imprimitive-lift-gcd-reduction`; `M9-M1-hard-top-t1-high-h-inverse-residue-conductor-reduction`; `M9-M1-hard-top-t1-residual-fejer-tangent-gcd-reduction`; `M9-M1-hard-top-t1-comparable-factor-exchange-sector`; `M9-M1-hard-top-small-t-nonresonant-primitive-ray-sector`; `M9-M1-hard-top-squarefree-radical-sector-reduction` |
| M1 parents and owner | `M9-M1-top-endpoint-signed-cone`; `M9-M1-direct-smooth-residual-blockwise-estimate`; `M9-M1-physical-one-count-assembly`; `M9-M1-global-angular-radial-estimate`; `M9-M1` |
| M2 parents and owner | `M9-M2-top-endpoint-signed-cone`; `M9-M2-smooth-balanced-quarter-packet-estimate`; `M9-M2-smooth-unbalanced-three-quarter-estimate`; `M9-M2` |
| Endpoint/global owner | `M9-endpoint-uniformity`; `M9` |
| Bridges, exponent records, target, and elementary support | `Conditional-bridge`; `GC-global-M1-alternative-bridge`; `GC-partial-one-third`; `GC-external-Li-Yang-theta-star`; `GC-target`; `Divisor-bound-elementary` |

The canonical diagnostic SHA-256 of these 27 complete records is
`c2d13675f34c4caf2e50da1d4478b51e77eca82c6ee4cc7ba835c4ff1aca09a4`
both before and after application.  The highlighted frontier statuses also
remain exact: `M9` and `GC-target` are `open`; both bridge records are
`derived_under_assumptions`; `GC-partial-one-third` is `proved_internal`;
and `GC-external-Li-Yang-theta-star` is
`proved_external_dependency`.  Their complete-record diagnostic hash,
together with `Divisor-bound-elementary`, is
`d750c9ae2c4d6bb9e0114b111dee13e8d4cb5f290cf6667959d871f0d4ce8ae3`
before and after.  No exponent statement or dependency changes.

### 3.3. Rejected-claim audit against the kernel

None of the 20 rejection IDs is a proof-obligation ID, so the applier cannot
take its status-changing rejection branch.  None is already present in
`rejected_claims`, so no duplicate or correction is created.  The original
1,755-record prefix remains exact, with canonical diagnostic SHA-256
`00119e20ae0f974ee3ce6304dc94aa4992ca8bed51a541420ad41bae5aec005e`
before and after; the total count becomes 1,775.

Every rejection has a direct durable-kernel basis:

| # | New rejected claim | Exact kernel basis and justification |
|---:|---|---|
| 1 | `Round196-parity-restored-shadow-is-literal-exact-conductor-atom` | K196.11 versus K196.17 and K196.22: the literal atom has ((-1)^t), while the primitive carrier is the parity-restored shadow and requires the extra (E_U(S_0)). |
| 2 | `Round196-dropping-EU-preserves-exact-conductor` | K196.20--K196.23: (E_U(S_0)) is the nonconstant factor connecting affine and Fourier parity, so deleting it changes the literal operator. |
| 3 | `Round196-multiplying-one-mode-by-EU-stays-in-packet` | K196.23: multiplication convolves all (U)-frequencies and mixes exact conductors, reduced numerators, bands, and safe/core packets. |
| 4 | `Round196-literal-x-step-multiplier-is-minus-eaq` | K196.24--K196.25: every live-to-live adjacent step has multiplier (+e(a/q)), and the near-half coefficient remains order one. |
| 5 | `Round196-live-wrap-supplies-denominator-cancellation` | K196.24: the negative wrap lands at (S_0=0), hence at a dead coprimality site, and is not a live-to-live pair. |
| 6 | `Round196-coprimality-mask-deletes-wrap-without-boundary` | K196.24 and K196.26--K196.27: zero extension leaves an unpaired boundary atom; it does not erase the event. |
| 7 | `Round196-actual-height-event-is-uniform-Delta2-in-x` | K196.28--K196.29: genuine transport displaces (x) by (2\epsilon_\omega\rho), not by one common step two. |
| 8 | `Round196-T0-rho-is-never-unit` | K196.29: the \(T=0\) branch explicitly permits \(\rho=\pm1\). |
| 9 | `Round196-unit-inverse-T0-rows-prove-the-branch` | K196.1's no-submask clause and K196.29: unit-inverse rows cannot replace their unestimated complement, and physical commutators remain. |
| 10 | `Round196-gamma-may-replace-beta-in-farey-selector` | K196.7: the canonical Farey selector uses \(\beta\), while literal transport uses \(\gamma=\beta+n\rho\). |
| 11 | `Round196-minus-far-step-moves-common-x` | K196.29: (x) is plus-far but minus-close; the literal minus-far step leaves (x) fixed. |
| 12 | `Round196-primitive-4q-carrier-alone-proves-saving` | K196.12 and K196.17--K196.19: the primitive (4q) algebra is exact only for the shadow and proves neither the fixed target nor a sector. |
| 13 | `Round196-cumulative-antiderivative-is-cost-free` | K196.31--K196.34 and the closing paragraph of K196.5: a cumulative primitive is an artificial method control, not a literal divisor-supported identity; its endpoints, births/deaths, and other product-rule terms have no estimate below the inherited capacity. |
| 14 | `Round196-parity-commutator-is-boundary-only` | K196.26--K196.27: the parity product-rule coefficient has modulus two on every live-to-live nonwrap edge, in addition to the wrap boundary. |
| 15 | `Round196-full-anchor-recombination-estimates-high-conductor` | K196.23: full recombination restores pre-conductor physical parity and removes the distinguished (c_q(a)). |
| 16 | `Round196-capacity-is-literal-lower-mass` | K196.25 and the final paragraph of K196.5: the near-half and positive-capacity checks are method falsifiers only and establish no nonvanishing or literal lower mass. |
| 17 | `Round196-no-go-disproves-literal-P2` | The final paragraph of K196.1: the result is mechanism-specific and does not refute a different coefficient-sensitive joint estimate. |
| 18 | `Round196-no-go-proves-strict-sector` | K196.12 and K196.24: no new target-safe sector is proved, and the formal wrap is live/dead rather than a paired sector. |
| 19 | `Round196-no-go-closes-original-t1-or-owner` | The final paragraph of K196.6: complete (P_2), (P_1), other original-(t) incidences, and the hard small-(t) owner are expressly unpromoted. |
| 20 | `Round196-no-go-improves-global-exponent` | K196.35--K196.38 and the final paragraph of K196.6: the fixed deficit persists; no parent, bridge, target, or exponent is promoted. |

The reasons are rejection of false route inferences, not promotion of their
negations into stronger lower-bound theorems.  This matches the kernel's
capacity-versus-literal-mass and owner/exponent quarantine.

### 3.4. Replay and validation

The repository validator returned `Patch OK`.  Applying the patch in memory
at round 196 and validating the resulting graph produced zero graph issues.
Manually executing the patch's reversal rule in memory--remove the 20 newly
introduced rejected-claim records, remove all 24 appended evidence paths from
each updated node, and restore the two saved `next_action` and metadata
records--recovered the starting graph exactly.

## 4. First doubtful or unproved step

There is no doubtful or unproved mutation inside the current patch scope.
The first invalid overstatement would be that only two records of any kind
change: 20 new rejected-claim records are also intentionally appended.  The
first unproved mathematical step remains the coefficient-sensitive joint
(++,+-,-+,--) estimate for the complete literal open (P_2) region before
positive norms, exactly as K196.6 states.  The patch does not claim that step.

The only temporal caveat is hash stability: applying after any intervening
edit to the graph or patch would fall outside this audit.

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| Starting-hash check | PASS: patch hash field equals the current graph SHA-256. |
| Repository patch validator | PASS: `Patch OK`. |
| Operation counts and uniqueness | PASS: (0/2/0/20/27); every category internally unique; zero cross-category overlaps. |
| Exact in-memory apply diff | PASS: exactly two proof-obligation IDs change; no create/remove. |
| Global status/dependency/statement/promotion quarantine | PASS: all 395 protected-field tuples compare equal before/after. |
| All 27 `no_change` objects | PASS: all exist, are distinct, and compare exactly equal before/after. |
| Bridge/exponent/target protection | PASS: complete records and exact exponent statements are unchanged. |
| Rejected-claim collision and prefix test | PASS: 20 fresh IDs, zero obligation collisions, zero prior-rejection collisions, original prefix exact. |
| Kernel justification of each rejection | PASS: all 20 have the direct K196 basis listed in Section 3.3. |
| Evidence append audit | PASS: 24 paths per updated node; all exist, are distinct, and are not already present. |
| Reversibility values and replay | PASS: saved old values match the graph and exact reverse replay returns the starting graph. |
| Post-apply graph validation | PASS: zero issues. |

All computation here was deterministic structural replay and hashing.  It is
diagnostic only and supplies no asymptotic theorem evidence.

## 6. Dependencies and exact artifacts used

1. `protocol.md`, SHA-256
   `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`.
2. `state/proof_obligations.yml`, SHA-256
   `f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`.
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
8. `rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/synthesis.md`,
   SHA-256
   `02bfb23cb8523d7301e6fc65babe79a695070710b9b045d62c64ab495a53a20c`.
9. `rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/reviews/conductor_round196_adjudication.md`,
   SHA-256
   `e760c0685789b583e16787fa812320faf608d16775f1abee78d38a610e7ce90d`.

No source, literature, or numerical theorem evidence was used.

## 7. Recommended state effect

**Apply the patch without repair, but only against the graph and patch hashes
recorded above.**  The lawful state effect is exactly:

1. append the 24 inconclusive evidence paths and replace `next_action` on the
   two named proof-obligation nodes, with ordinary round/time metadata update;
2. append the 20 fresh route-falsifier records to `rejected_claims`;
3. create, promote, demote, reject, or otherwise alter no proof obligation;
4. leave all 27 `no_change` records, every existing rejected claim, all
   bridges, endpoint/global parents, exponent records, and `GC-target`
   untouched.

Recommended disposition: **promote no theorem; apply the route-boundary
evidence and rejections; preserve every protected record.**
