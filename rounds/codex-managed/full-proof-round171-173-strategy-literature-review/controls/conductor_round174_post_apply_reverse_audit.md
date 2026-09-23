# Round 174 independent post-apply reverse audit

- Campaign: `full-proof-round171-173-strategy-literature-review`
- Role: independent post-apply graph and reversibility auditor
- Authoritative graph: `state/proof_obligations.yml`
- Applied patch: `rounds/codex-managed/full-proof-round171-173-strategy-literature-review/state_patch.json`
- Round index: 174
- Starting graph SHA-256: `04090ef6aa8d7d28e05a312f1f2f069fe3ab44ad62002d68d6b62c49dc0d962a`
- Expected and observed post-apply SHA-256: `e40c214351d06bf05212e25fffbec0f1a4808be21cb9098ba25823f0d9bbf211`
- Applied timestamp: `2026-08-27T00:52:12`
- Verdict: **GREEN**

## 1. Result

The authoritative graph is exactly the expected Round-174 post-apply graph.
Its SHA-256 is
`e40c214351d06bf05212e25fffbec0f1a4808be21cb9098ba25823f0d9bbf211`,
its bytes are already in repository-canonical serialization, and repository
graph validation returns no issue.

The exact applied operation counts are:

- create: **0**;
- update: **1**;
- correct rejected: **0**;
- reject: **22**; and
- no change: **23**.

The sole obligation update changed exactly `evidence`, `next_action`,
`last_updated_round`, and `last_updated_at`.  Exactly twenty-two rejected
records form the current rejected-ledger suffix in patch order.  No obligation
was created or removed; no status, dependency, implication, or blocker edge
changed; and no cycle was introduced.

An inverse constructed in memory from the frozen sole-node preimage and the
certified current rejected suffix passes graph validation and serializes to
exactly 1,865,400 bytes with SHA-256
`04090ef6aa8d7d28e05a312f1f2f069fe3ab44ad62002d68d6b62c49dc0d962a`.
Because the frozen starting graph was itself repository-canonical, this is
exact recovery of the starting graph data and bytes, not merely semantic
equivalence.  No shared-state file was edited.

## 2. Exact statement and hypotheses

### Frozen inputs and comparison rule

This audit freezes:

1. the authoritative post-apply graph bytes at the expected hash above;
2. the current narrowed patch bytes at SHA-256
   `6f960d277f339893f4142d39a2bb07d6f0522a3ad4600585ab082dde0cc3daed`;
3. the pre-apply graph hash and sole-node preimage certified in
   `controls/preapply_independent_reverse_audit.md`;
4. the current twenty-two-record rejected suffix;
5. round index 174 and the actual common application timestamp
   `2026-08-27T00:52:12`; and
6. repository `load_graph`, `validate_graph`, and `dump_graph` semantics.

The applied graph is compared with the graph obtained by the exact inverse in
Section 3.  Thus an “applied change” below means a data difference between the
reconstructed starting graph and the current authoritative graph, not an
inference from the patch declaration alone.

### Sole updated obligation

The sole updated ID is

`M9-M2-hard-top-t1-residual-fejer-parity-gcd-scale-reduction`.

Its exact applied field ledger is:

| Field | Starting value | Applied value |
|---|---|---|
| `status` | `proved_internal` | `proved_internal` |
| `last_updated_round` | 167 | 174 |
| `last_updated_at` | `2026-08-26T15:28:52` | `2026-08-27T00:52:12` |
| inconclusive evidence count | 14 | 22 |
| `dependencies` | one frozen dependency | unchanged |
| `implies` | empty | unchanged |
| `blockers` | empty | unchanged |

The dependency remains exactly
`M9-M2-hard-top-t1-residual-transport-fejer-energy-reduction`.

The applied `next_action` equals the patch text byte-for-byte:

> Round 174 retains K26 as the sole Round-175 analytic frontier. Prove the exact one-sided whole-stopped-chain nonzero ordinary-frequency bound sum_(j=0)^(K-1) N_(R_j,R_(j+1)) <<_epsilon L^3 X^epsilon, with the complete literal residual coefficient, both parity branches, constants i/2 and 1/8, the collectively recombined ordinary-zero sector, strict terminal link, once-only short correction, every cardinal cell, endpoint, transition, and zero-extension value retained until a factor-L actual-symbol saving is obtained. Stop at the first coefficient, normalization, endpoint, positive-capacity, rank-one, or Round-173 self-return failure and do not pivot in-round. Success would close only the complete residual scalar through the accepted K26 implication; it would not close full t=1, hard TOP, M9-M2, a bridge, or an exponent.

Exactly these eight fresh entries were appended once, in this order, to
`evidence.inconclusive`:

1. `rounds/codex-managed/full-proof-round171-173-strategy-literature-review/reports/full_graph_frontier_reconstruction.md`;
2. `rounds/codex-managed/full-proof-round171-173-strategy-literature-review/reports/current_primary_literature_reassessment.md`;
3. `rounds/codex-managed/full-proof-round171-173-strategy-literature-review/reports/blind_round175_frontier_selection.md`;
4. `rounds/codex-managed/full-proof-round171-173-strategy-literature-review/reviews/dependency_power_selection_seam_review.md`;
5. `rounds/codex-managed/full-proof-round171-173-strategy-literature-review/reviews/source_hypotheses_currency_interface_review.md`;
6. `rounds/codex-managed/full-proof-round171-173-strategy-literature-review/reviews/blind_post_unmask_frontier_selection_review.md`;
7. `rounds/codex-managed/full-proof-round171-173-strategy-literature-review/reviews/full_graph_post_repair_verification.md`; and
8. `rounds/codex-managed/full-proof-round171-173-strategy-literature-review/reviews/source_report_post_repair_verification.md`.

All eight paths are unique, relative, POSIX-normalized, free of parent
traversal, and present.

### Rejected-record suffix

The current graph's final twenty-two rejected records have exactly the patch
IDs and reasons, in patch order:

1. `Round174-frontier-ranking-proves-K26`;
2. `Round174-cross-link-cancellation-is-proved-to-exist`;
3. `Round174-whole-chain-recombination-alone-saves-a-factor-L`;
4. `Round174-Round173-self-return-disproves-K26`;
5. `Round174-coefficient-uniform-positive-capacity-is-physical-lower-mass`;
6. `Round174-K26-closes-full-t1`;
7. `Round174-K26-closes-hard-TOP`;
8. `Round174-one-hard-TOP-face-closes-M9-M2`;
9. `Round174-critical-BAL-closes-full-BAL`;
10. `Round174-hard-TOP-BAL-and-UNBAL-are-interchangeable`;
11. `Round174-one-direct-M1-parent-closes-M9-M1`;
12. `Round174-GAR-proves-blockwise-M9-M1`;
13. `Round174-endpoint-uniformity-is-an-independent-cancellation-theorem`;
14. `Round174-equal-local-deficits-merge-owners`;
15. `Round174-local-moment-Y-one-sixth-saving-is-strict-sub-one-third`;
16. `Round174-local-moment-five-sixteenths-is-proved`;
17. `Round174-current-source-search-is-universal-literature-nonexistence`;
18. `Round174-averaged-smoothed-fixed-modulus-or-exceptional-spectrum-results-prove-a-project-owner`;
19. `Round174-Bourgain-Watt-withdrawal-erases-rederived-algebraic-identities`;
20. `Round174-Li-Yang-preprint-is-published`;
21. `Round174-current-literature-improves-the-certified-exponent`; and
22. `Round174-strategy-review-proves-the-quarter-target`.

Every suffix record has exactly the fields `id`, `reason`, `last_updated_at`,
and `last_updated_round`; every round is 174; every timestamp is
`2026-08-27T00:52:12`.  The 1,389-record prefix is data-identical to the
starting rejected ledger.

## 3. Proof or derivation

### 3.1 Direct post-apply comparison

The current graph has 377 obligations and 1,411 rejected records.  The
reconstructed starting graph has 377 obligations and 1,389 rejected records.
An ID-indexed structural comparison gives:

- added obligations: none;
- removed obligations: none;
- changed obligations: exactly the sole declared update target;
- changed fields on that target: exactly `evidence`, `next_action`,
  `last_updated_round`, and `last_updated_at`;
- changed top-level graph keys: exactly `proof_obligations` and
  `rejected_claims`;
- changed pre-existing rejected records: none; and
- current rejected suffix: exactly the twenty-two declared records.

The patch's 23 `no_change` IDs are pairwise distinct, all resolve in both
graphs, are disjoint from the update ID, and are completely data-identical
across the comparison.  Every operation class is internally unique, and
there is no ID overlap between operation classes.

The authoritative obligation IDs are unique at 377/377.  The current
rejected IDs are unique at 1,411/1,411, and no rejected ID equals an
obligation ID.  The twenty-two new IDs are therefore fresh relative to both
starting ledgers.

### 3.2 Status, edge, validity, and cycle audit

Repository validation of the current graph returns zero issues.  Across all
377 obligations, exact starting/current comparison gives:

- status changes: **0**;
- dependency-list changes: **0**;
- implication-list changes: **0**; and
- blocker-list changes: **0**.

The dependency orientation has exactly three pre-existing two-node cyclic
strongly connected components before and after application:

1. `M9-M1-lower-far-cone-microscopic-cell-reduction` with
   `M9-M1-lower-post-collar-smoothed-far-alias-reduction`;
2. `M9-M1-lower-height-alias-rank-one-product-fibre-obstruction` with
   `M9-M1-lower-incomplete-fibre-dispersion-obstruction`; and
3. `M9-M2-hard-top-product-fibre-mean-obstruction` with
   `M9-M2-hard-top-product-fibre-transform-self-return`.

When `implies` is converted to the same logical dependency orientation, one
additional pre-existing two-node component occurs before and after:

4. `M9-M2-LFM-endpoint-degeneracy` with `M9-endpoint-uniformity`.

The before/after component lists are exactly equal, and the updated node lies
in none of them.  Hence Round 174 introduces no dependency or combined
logical cycle.  This audit does not incorrectly call the historical graph
cycle-free; it certifies zero new patch-induced cycles.

### 3.3 Exact in-memory inverse

The inverse was constructed without writing a graph file:

1. locate the sole updated obligation at its unchanged list position;
2. remove the exact eight-entry suffix from `evidence.inconclusive`;
3. restore the frozen `next_action`:
   “The exact determinant endpoint representation and every fixed-B
   polylogarithmic shift sector are now proved. K17a remains open for the
   non-polylogarithmic even opposing low-gcd range. The audited direct 2024,
   fixed-shift-triangle, and current Part-I interfaces are parked; compare a
   genuinely new full-scalar signed mechanism with the maximal-scale K26
   alternative before choosing the next owner.”;
4. restore `last_updated_round: 167` and
   `last_updated_at: 2026-08-26T15:28:52`;
5. remove exactly the final twenty-two rejected records after first checking
   their IDs, reasons, order, round, timestamp, and freshness;
6. make no create, corrected-rejected, or no-change inverse mutation; and
7. serialize using repository `dump_graph`.

The inverse graph validates with zero issues, contains 377 obligations and
1,389 rejected records, and produces 1,865,400 canonical bytes.  Its SHA-256
is exactly
`04090ef6aa8d7d28e05a312f1f2f069fe3ab44ad62002d68d6b62c49dc0d962a`.
This agrees with the frozen starting bytes and hash from the pre-apply audit.

## 4. First doubtful or unproved step

There is no unresolved application, node-field, timestamp, evidence,
rejected-suffix, uniqueness, status, edge, cycle, validation, serializer, or
inverse seam.

The cycle statement is deliberately scoped: four historical strongly
connected components remain under the two tested edge interpretations, but
the applied patch changes no edge and creates none.  The audit is mechanical
and does not prove K26, promote an analytic estimate, or authorize Round 175.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| expected post-apply hash | **GREEN:** exact `e40c2143...bbf211` |
| current patch hash | **GREEN:** exact `6f960d27...3daed` |
| canonical current serialization | **GREEN:** byte-identical to `dump_graph` |
| exact operation counts | **GREEN:** 0 / 1 / 0 / 22 / 23 |
| operation uniqueness/disjointness | **GREEN:** all internal IDs unique; no cross-class overlap |
| obligation counts | **GREEN:** 377 to 377 |
| rejected counts | **GREEN:** 1,389 to 1,411 |
| exact changed obligation | **GREEN:** sole declared update target |
| exact changed fields | **GREEN:** evidence, next action, round, timestamp only |
| update timestamp | **GREEN:** exact `2026-08-27T00:52:12` |
| evidence application | **GREEN:** 8 fresh entries, exact suffix/order, 14 to 22 |
| evidence paths | **GREEN:** 8/8 unique, normalized, present |
| rejected suffix | **GREEN:** 22 exact IDs/reasons/order; common timestamp and round |
| rejected uniqueness | **GREEN:** 1,411/1,411; no obligation-ID collision |
| pre-existing rejected prefix | **GREEN:** all 1,389 records unchanged |
| no-change declarations | **GREEN:** 23/23 resolve and remain data-identical |
| status changes | **NONE** |
| dependency/implication/blocker changes | **NONE** |
| current graph validation | **GREEN:** zero issues |
| new dependency cycles | **NONE** |
| new combined logical cycles | **NONE** |
| inverse graph validation | **GREEN:** zero issues |
| inverse canonical byte count | **GREEN:** 1,865,400 |
| inverse starting-hash recovery | **GREEN:** exact `04090ef6...d962a` |
| authoritative-state write by this audit | **NONE** |

The current graph and patch are valid UTF-8 with zero bare carriage returns,
zero forbidden C0 controls, zero raw `0xC0` bytes, zero NUL bytes, and zero
Unicode replacement characters.  The graph is 1,873,361 bytes and the patch
is 11,401 bytes.

## 6. Dependencies and exact artifacts used

This audit used only:

1. `protocol.md`;
2. `state/proof_obligations.yml`;
3. `state/active_campaign.yml`;
4. the current `state_patch.json`;
5. `controls/preapply_independent_reverse_audit.md`;
6. the Round-167 `state_patch.json`, solely to cross-check the frozen prior
   `next_action` text;
7. `math_collab/validate_state_patch.py`;
8. `math_collab/proof_obligations.py`; and
9. the eight evidence paths named in Section 2, for read-only existence and
   path checks.

All graph application comparison, cycle analysis, and reversal occurred only
in memory.  No web source or numerical mathematical experiment was used.

## 7. Recommended state effect

**No change.**  The already-applied authoritative graph is mechanically
consistent with the current Round-174 patch and exactly reversible to the
frozen starting graph.  This post-apply audit licenses no additional graph
mutation, status change, proof promotion, exponent change, or next-round
start.

**Final verdict: GREEN.**
