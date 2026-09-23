# Round 174 independent pre-apply State-Patch reverse audit

- Campaign: `full-proof-round171-173-strategy-literature-review`
- Role: independent pre-apply patch, graph, hygiene, and reversibility auditor
- Graph: `state/proof_obligations.yml`
- Patch: `rounds/codex-managed/full-proof-round171-173-strategy-literature-review/state_patch.json`
- Round index used in simulation: 174
- Starting graph SHA-256: `04090ef6aa8d7d28e05a312f1f2f069fe3ab44ad62002d68d6b62c49dc0d962a`
- Current narrowed patch SHA-256: `6f960d277f339893f4142d39a2bb07d6f0522a3ad4600585ab082dde0cc3daed`
- Verdict: **GREEN**

## 1. Result

The current narrowed Round-174 State Patch is mechanically valid, graph-safe,
path-clean, and exactly reversible.  The repository dry validator returned
`Patch OK`.  A direct call to the repository application engine with
`round_index=174`, performed only on an in-memory deep copy, produced exactly
the declared operation result:

- create: **0**;
- update: **1**;
- correct rejected: **0**;
- reject: **22**; and
- no change: **23**.

There is no operation-class overlap.  In particular, the sole update target
is no longer repeated in `no_change`, and the two removed future/nonexistent
evidence paths are absent from the current patch.  All eight remaining
evidence paths are unique, repository-relative, POSIX-normalized, and present.

The in-memory application changed exactly one existing obligation record and
appended exactly twenty-two fresh rejected-claim records.  It created or
removed no obligation, changed no status, dependency, implication, or blocker
edge, and introduced no cycle.  A mechanical inverse restored the updated
obligation's complete preimage and removed the twenty-two fresh rejected
records.  Repository canonical serialization then reproduced the original
graph object, bytes, and starting SHA-256 exactly.

No shared-state file was written or edited.

## 2. Exact statement and hypotheses

### Frozen inputs

The audit froze:

1. the current graph bytes at the required starting hash;
2. the current narrowed patch bytes at the patch hash above;
3. round index \(174\);
4. the repository functions `load_graph`, `validate_graph`,
   `validate_patch_against_graph`, `apply_state_patch`, and `dump_graph`;
5. no judge reference, so no automatic judge-evidence path was injected; and
6. the repository root for source-card and evidence-path existence checks.

The starting graph contains 377 obligations and 1,389 rejected claims.  Its
bytes are already identical to

`json.dumps(graph, indent=2, ensure_ascii=True) + "\\n"`,

the exact serializer used by `dump_graph` and `write_graph`.  This permits a
byte-level reverse test rather than only parsed-data equality.

### Exact operation ledger

The sole update target is:

`M9-M2-hard-top-t1-residual-fejer-parity-gcd-scale-reduction`.

It receives exactly eight fresh `evidence.inconclusive` paths, the exact
declared Round-175 K26 `next_action`, `last_updated_round: 174`, and the
application timestamp.  The update changes no other field.

The twenty-two rejected-record IDs, in exact patch/application order, are:

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

All 22 IDs are pairwise distinct, absent from the 377 obligation IDs, and
absent from the 1,389 pre-existing rejected IDs.  All 23 `no_change` IDs are
pairwise distinct, resolve to existing obligations, and are disjoint from the
sole update ID.

## 3. Proof or derivation

### 3.1 Dry validation and in-memory application

The standard dry command, without `--apply`, returned `Patch OK`:

`python -m math_collab.validate_state_patch --graph state/proof_obligations.yml --patch rounds/codex-managed/full-proof-round171-173-strategy-literature-review/state_patch.json --round-index 174`.

Direct pre-application graph validation, patch-against-graph validation, and
post-application graph validation each returned zero issues.  The input graph
object remained equal to its frozen deep copy after `apply_state_patch`,
confirming that the application engine mutated only its returned copy.

The simulated result contains 377 obligations and 1,411 rejected claims.
Exact structural comparison gives:

- added obligations: none;
- removed obligations: none;
- changed existing obligations: exactly the one declared update target;
- changed top-level keys: exactly `proof_obligations` and
  `rejected_claims`;
- fresh rejected records: exactly the 22 declared records, appended in the
  declared order;
- changed pre-existing rejected records: none; and
- changed non-target obligations: none.

The sole updated record changed exactly these four keys:

1. `evidence`;
2. `next_action`;
3. `last_updated_round`; and
4. `last_updated_at`.

Its exact pre/post ledger in this simulation is:

| Field | Before | In-memory result |
|---|---|---|
| status | `proved_internal` | `proved_internal` |
| last updated round | 167 | 174 |
| last updated at | `2026-08-26T15:28:52` | `2026-08-27T00:43:33` |
| inconclusive evidence count | 14 | 22 |
| next action | frozen preimage | exact patch text |
| dependencies | unchanged | unchanged |
| implies | unchanged | unchanged |
| blockers | unchanged | unchanged |

The eight evidence paths were appended exactly once and in patch order.  The
simulated canonical graph hash was
`cca3bf6209d9147a81faf19099a346b219b3309541bad28d29ba6e40a65b1881`.
That hash is diagnostic for this in-memory timestamp only; a later real
application will normally have different bytes because the engine generates
`last_updated_at` from the wall clock.

Each fresh rejected record has exactly the keys `id`, `reason`,
`last_updated_at`, and `last_updated_round`.  Every reason is copied exactly,
every round is 174, all application timestamps agree, and the first 1,389
rejected records remain data-identical.  The post-application rejected-ID
ledger is unique at all 1,411 positions.

All 23 `no_change` records remain completely data-identical.  The patch's
`round_assessment` contributes only result-summary messages and is not stored
in the graph.

### 3.2 Status, edge, validity, and cycle audit

Across all 377 obligations:

- status changes: **0**;
- dependency-list changes: **0**;
- implication-list changes: **0**; and
- blocker-list changes: **0**.

The authoritative graph contains three pre-existing two-node cyclic strongly
connected components in the dependency orientation:

1. `M9-M1-lower-far-cone-microscopic-cell-reduction` with
   `M9-M1-lower-post-collar-smoothed-far-alias-reduction`;
2. `M9-M1-lower-height-alias-rank-one-product-fibre-obstruction` with
   `M9-M1-lower-incomplete-fibre-dispersion-obstruction`; and
3. `M9-M2-hard-top-product-fibre-mean-obstruction` with
   `M9-M2-hard-top-product-fibre-transform-self-return`.

When explicit `implies` edges are added, there is one additional pre-existing
two-node component:

4. `M9-M2-LFM-endpoint-degeneracy` with `M9-endpoint-uniformity`.

The before/after component lists are exactly identical, and the updated node
belongs to none of them.  Thus the patch introduces no dependency or combined
logical cycle.  The phrase “no cycles” in this audit means no new
patch-induced cycle; the named legacy components are properties of the
authoritative starting graph and are unchanged.

### 3.3 Exact inverse

The inverse was constructed from the patch operation classes and frozen
preimages, not by overwriting the simulation with the starting file:

1. locate the sole updated obligation at its existing list position and
   replace the applied record by its complete frozen preimage;
2. remove exactly the twenty-two fresh rejected records by their certified
   fresh IDs, preserving every pre-existing rejected record and its order;
3. perform no create inverse, because the patch creates no obligation;
4. perform no corrected-rejected inverse, because that list is empty;
5. perform no `no_change` inverse, because those declarations mutate
   nothing; and
6. serialize with repository `dump_graph`.

The reversed graph passes repository graph validation with zero issues.  It
is exactly equal to the starting parsed object.  Its canonical bytes are
byte-for-byte equal to the original graph bytes, and its SHA-256 is exactly

`04090ef6aa8d7d28e05a312f1f2f069fe3ab44ad62002d68d6b62c49dc0d962a`.

## 4. First doubtful or unproved step

There is no unresolved patch, path, uniqueness, graph, cycle, serializer, or
reverse seam.

The simulated applied hash is not a forecast of the future authoritative
post-apply hash because `last_updated_at` is time-dependent.  A real
application must therefore recheck the starting hash immediately, record its
actual post-apply hash, and run a fresh post-apply reverse audit.

This mechanical verdict does not independently prove K26, endorse a source
theorem, or authorize any graph effect beyond the patch's evidentiary update
and rejected-record additions.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| required starting hash | **GREEN:** exact `04090e...d962a` |
| current narrowed patch hash | **GREEN:** exact `6f960d...3daed` |
| repository dry validator | **GREEN:** `Patch OK` |
| declared/observed operation counts | **GREEN:** 0 / 1 / 0 / 22 / 23 |
| operation ID uniqueness | **GREEN:** unique within every class |
| cross-operation overlap | **GREEN:** none |
| sole updated ID exists | **GREEN** |
| exact updated fields | **GREEN:** evidence, next action, round, timestamp only |
| evidence merge | **GREEN:** 8 fresh paths, 14 to 22, exact order |
| evidence-path existence and normalization | **GREEN:** 8/8 unique, relative, POSIX, no parent traversal, present |
| rejected-record freshness | **GREEN:** 22/22 absent from obligations and prior rejected ledger |
| rejected-record uniqueness after apply | **GREEN:** 1,411/1,411 unique |
| rejected record content/order | **GREEN:** IDs, reasons, round, timestamp, and append order exact |
| no-change declarations | **GREEN:** 23/23 resolve, remain data-identical, and do not overlap update |
| obligation count | **GREEN:** 377 to 377 |
| rejected count | **GREEN:** 1,389 to 1,411 |
| status changes | **NONE** |
| dependency, implication, blocker changes | **NONE** |
| graph validation before/after | **GREEN:** zero issues |
| new dependency cycles | **NONE** |
| new combined logical cycles | **NONE** |
| input object mutation | **NONE** |
| inverse object equality | **GREEN** |
| inverse graph validation | **GREEN:** zero issues |
| inverse byte equality | **GREEN** |
| inverse starting-hash recovery | **GREEN** |
| authoritative graph preservation | **GREEN:** bytes/hash unchanged after all tests |

### UTF-8, control-byte, and path hygiene

The graph, current patch, and all eight patch-referenced evidence files are
valid UTF-8 and contain:

- zero bare carriage returns;
- zero forbidden C0 controls other than ordinary tab/line-ending bytes;
- zero raw `0xC0` bytes;
- zero NUL bytes; and
- zero Unicode replacement characters.

The patch itself is 11,401 bytes and the graph is 1,865,400 bytes at the
audited hashes.  No absolute path, backslash path, parent traversal, duplicate
path, missing path, or future/nonexistent path remains in the patch.

## 6. Dependencies and exact artifacts used

This audit used only:

1. `protocol.md`;
2. `state/proof_obligations.yml`;
3. `state/active_campaign.yml`;
4. the current narrowed `state_patch.json`;
5. `math_collab/validate_state_patch.py`;
6. the graph load, validation, application, and canonical serialization
   implementation in `math_collab/proof_obligations.py`; and
7. the eight evidence artifacts named by the current patch, for read-only
   path and byte-hygiene checks.

No web source, numerical mathematical experiment, temporary graph file, or
authoritative-state write was used.  The patch application and inverse
existed only as Python objects in memory.

## 7. Recommended state effect

**GREEN for conductor-authorized application, subject to an immediate fresh
starting-hash check.**  If applied, the exact permitted effect is:

1. update only
   `M9-M2-hard-top-t1-residual-fejer-parity-gcd-scale-reduction` with the
   eight inconclusive evidence paths, Round-175 next action, round 174, and
   application timestamp;
2. append exactly the twenty-two fresh rejected records; and
3. leave all statuses, edges, other obligations, prior rejected records, and
   certified exponents unchanged.

This audit itself applies nothing and authorizes no proof promotion.  After a
real application, record the actual output hash and use the exact inverse
recipe in Section 3.3 for the required post-apply reverse check.

**Final verdict: GREEN.**
