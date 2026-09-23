# Round 191 post-application independent reverse-replay and protected-scope audit

- Campaign: m9-m1-t1-fast-height-jump-coboundary-gate
- Live graph:
  state/proof_obligations.yml
- Live graph SHA-256:
  75b44fe68f9c6e094d2ab6e643be3c0309320ef84e73ca22d692698440eeed13
- Patch:
  rounds/codex-managed/m9-m1-t1-fast-height-jump-coboundary-gate/state_patch.json
- Audit role: independent post-application inverse, production replay,
  graph relation, evidence-path, and protected-scope control
- Status: diagnostic state audit only; no state mutation

## 1. Result and final verdict

**PASS.** The live graph has the required SHA-256
75b44fe68f9c6e094d2ab6e643be3c0309320ef84e73ca22d692698440eeed13
and is byte-for-byte the canonical production serialization of the
loaded graph. An operation-derived inverse recovers the exact Round 191
starting graph:

\[
 \operatorname{SHA256}(G_{190})
 =
 306425e79ef6d5e25ed037b77d25a0cc180bfc3b68c4a17ef833da7be1a573fa.
\]

The actual application metadata recovered from the live created node,
updated owner, and all fifteen rejection records is:

- round index: 191;
- application timestamp: 2026-08-29T22:59:10;
- judge reference:
  rounds/codex-managed/m9-m1-t1-fast-height-jump-coboundary-gate/reviews/conductor_round191_adjudication.md.

Applying the unchanged patch to the recovered starting graph through
the production apply function, with exactly that round, timestamp, and
judge reference, reproduces all 2,094,835 live bytes and the live hash
above. The exact operation effect is

\[
 \boxed{1\ {\rm create}/1\ {\rm update}/0\ {\rm corrections}/
 15\ {\rm rejections}/23\ {\rm no\!-\!change}.}
\tag{191.A1}
\]

Only the intended existing owner changed, and it remains open. No
protected owner, bridge, target, or exponent changed. No new invalid
relation or cycle was introduced, and every patch evidence path exists.

## 2. Exact audited statement and application hypotheses

This audit treats state/proof_obligations.yml as authoritative and
checks the application of the Round 191 State Patch with the production
semantics:

1. append the one created obligation;
2. update the one named owner by unique list addition and exact field
   replacement;
3. append the fifteen new rejected-claim records;
4. record the round and one common second-resolution timestamp;
5. inject the judge reference into the created node's inconclusive
   evidence and into each newly rejected record; and
6. serialize with insertion-order, two-space JSON, LF newlines, and one
   final LF.

The created obligation is exactly
M9-M1-hard-top-t1-fast-signed-inverse-transport-reduction. It occurs
once and has:

- type candidate_lemma and status proved_internal;
- owner Codex conductor;
- direct dependencies
  M9-M1-hard-top-t1-high-h-dual-frequency-projective-reduction and
  Divisor-bound-elementary;
- empty implies and blockers lists;
- a statement restricted to the signed-inverse-small sector, the exact
  terminal and isolated Fejer projections, and the exact rho-large
  remainder reduction;
- an explicit declaration that the complete fast packet, complete
  original \(t=1\) residual, small-\(t\) owner, parents, bridges,
  theorem, and exponents are not proved.

The sole updated obligation is
M9-M1-hard-top-high-radical-small-t-residual-estimate. Its status is
open both before and after application. The update adds one subordinate
dependency and eighteen inconclusive evidence paths, replaces only its
next action, and updates only its round/time metadata.

## 3. Proof and derivation

### 3.1 Recovery of the actual application metadata

The created node, updated owner, and all fifteen Round191 rejection
records have the same last_updated_round \(191\) and timestamp
2026-08-29T22:59:10. The adjudication path is:

- the unique extra inconclusive item beyond the created-node patch
  payload; and
- the singleton evidence item on every new rejection.

Thus the live graph itself determines the round, timestamp, and judge
arguments needed for production replay. The created node has fifteen
positive, zero negative, and nine inconclusive evidence items: the
eight patch-specified inconclusive items plus the validator-injected
judge reference. The adjudication consequently occurs once in positive
and once in inconclusive evidence, exactly as production semantics
requires.

### 3.2 Operation-derived inverse

Starting only from the live graph and patch operations, the inverse was
constructed in memory by:

1. removing the one created obligation;
2. removing the fifteen Round191 rejected records;
3. removing the newly appended owner dependency;
4. removing the exact eighteen added owner inconclusive-evidence
   entries;
5. restoring the owner next action from the reversibility payload; and
6. restoring owner metadata to last_updated_round \(190\) and
   last_updated_at 2026-08-29T20:38:31.

No other object or top-level field was touched. Canonical serialization
of the inverse has 2,079,053 bytes and SHA-256
306425e79ef6d5e25ed037b77d25a0cc180bfc3b68c4a17ef833da7be1a573fa,
exactly the patch's recorded starting hash. The recovered graph passes
the production graph validator, and the unchanged patch passes its
precondition validator against that graph.

### 3.3 Production forward replay

The recovered graph was passed in memory to the production
apply_state_patch operation with:

\[
 {\rm round}=191,\qquad
 {\rm timestamp}=2026\text{-}08\text{-}29{\rm T}22{:}59{:}10,
\]

and the recovered adjudication judge reference. Production dump_graph
then produced:

- 2,094,835 bytes;
- SHA-256
  75b44fe68f9c6e094d2ab6e643be3c0309320ef84e73ca22d692698440eeed13;
- exact byte equality and deep structural equality with the live file.

The production PatchResult independently reports the same counts
\(1/1/0/15/23\). The live graph also passes production validation.

### 3.4 Exact structural effect

The recovered start has 391 unique obligations and 1,667 unique
rejected claims. The live graph has 392 and 1,682 respectively, with no
duplicate ID and no cross-namespace collision. The exact obligation
diff is:

- added:
  M9-M1-hard-top-t1-fast-signed-inverse-transport-reduction;
- modified existing:
  M9-M1-hard-top-high-radical-small-t-residual-estimate;
- removed: none.

The exact rejected-claim diff is fifteen additions, with no removed or
modified pre-existing record. Each new rejection has the patch's exact
ID and reason, round 191, the common timestamp, and singleton
adjudication evidence.

The created live node is deep-equal to the production replay node; its
canonical object SHA-256 is
03632f42f7545e2e3467694ddf9c9ff5fcbb6dc7539c5a8c8df5e8a214247f67.
The owner changes only in these five keys:

- dependencies: \(7\to8\), adding the created node once;
- evidence: inconclusive \(136\to154\), the exact eighteen-item suffix;
- next_action;
- last_updated_round;
- last_updated_at.

Its status remains open, its implies list remains
\([{\rm M9\!-\!M1\!-\!top\!-\!endpoint\!-\!signed\!-\!cone}]\), and its
blockers list remains empty.

### 3.5 Protected scopes

All twenty-three no-change obligations are deep-equal before and after
application. Their ordered aggregate canonical SHA-256 is

\[
 6dae0d97ae151a7a971772eaca4e28a4a31203b58d0e4a06a14d4d8c8a4abc32
\]

on both graphs. Their statuses remain exactly:

- nine proved_internal;
- eleven open;
- two derived_under_assumptions;
- one proved_external_dependency.

In particular, M9-M1, M9-M2, M9-endpoint-uniformity, M9, and GC-target
remain open. Conditional-bridge and GC-global-M1-alternative-bridge
remain derived_under_assumptions. The hard and smooth M1 parents, GAR,
and every named M2 parent are deeply unchanged.

The exponent nodes are also deep-equal:

- GC-partial-one-third remains proved_internal with exponent \(1/3\);
- GC-external-Li-Yang-theta-star remains
  proved_external_dependency with
  \(0.3144831759740614\ldots\);
- GC-target remains open with exponent \(1/4\).

Their individual canonical object hashes are respectively
891b50b236929d5e3a5735fea9a1c1223b38f7860c643297d6c95823ee73948f,
c37fa333b3db206429cd8e0a8d650a8a26a66190cc5071684af6d36afd2b9321,
and
9f5f3ccf1700273d4381dda09ff38e7e40a939b98d7b741a73ccf3ce2f07ec95.

### 3.6 Relations, cycles, and evidence paths

All dependency, implies, and blocker targets resolve both before and
after application; the invalid-relation count is zero in both graphs.
Relation totals change only as production predicts:

| Relation | Recovered start | Live |
|---|---:|---:|
| dependencies | 1,391 | 1,394 |
| implies | 326 | 326 |
| blockers | 70 | 70 |

The three new dependency edges are the created node's two direct
dependencies and the owner's one edge to the created node. The created
node has no implies edge. Its dependency closure excludes the owner, so
the new owner edge cannot close a cycle.

The graph contains three pre-existing two-node dependency strongly
connected components, and the identical three occur after application:

- M9-M1-lower-far-cone-microscopic-cell-reduction with
  M9-M1-lower-post-collar-smoothed-far-alias-reduction;
- M9-M1-lower-height-alias-rank-one-product-fibre-obstruction with
  M9-M1-lower-incomplete-fibre-dispersion-obstruction;
- M9-M2-hard-top-product-fibre-mean-obstruction with
  M9-M2-hard-top-product-fibre-transform-self-return.

Thus Round 191 creates no new dependency cycle. There is no implies
cycle before or after.

The patch contains forty-one evidence occurrences over twenty-three
unique paths. All twenty-three paths exist, as does the recovered judge
reference. Evidence-path existence was checked without treating the
finite controls as asymptotic proof.

## 4. First doubtful or unproved step

No State Patch application, reversibility, replay, relation, path, or
protected-scope defect was found. The first mathematical step still
unproved is the exact rho-large signed remainder

\[
 \Re\mathscr R_{Y,Q}^{\sigma}
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\]

Positive control remains at \(Y\kappa uX^\varepsilon\), against target
\(Qm\kappa uX^\varepsilon\), with exact deficit \(Y/(Qm)\). The created
node and updated owner's next action both preserve this obstruction.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Live graph hash | PASS: exact required hash 75b44fe68f9c6e094d2ab6e643be3c0309320ef84e73ca22d692698440eeed13. |
| Live canonical bytes | PASS: raw bytes equal production dump_graph bytes. |
| Actual metadata recovery | PASS: round 191, timestamp 2026-08-29T22:59:10, and adjudication judge reference are uniquely recovered. |
| Operation-derived inverse | PASS: 2,079,053 bytes and exact starting hash 306425e79ef6d5e25ed037b77d25a0cc180bfc3b68c4a17ef833da7be1a573fa. |
| Production forward replay | PASS: 2,094,835 bytes, byte/deep equality, exact live hash. |
| Effect count | PASS: exactly \(1/1/0/15/23\). |
| Created node | PASS: one exact proved_internal node, two proved_internal dependencies, empty implies/blockers, correct evidence and metadata. |
| Updated owner | PASS: only modified existing obligation; remains open; exact dependency/evidence/action/metadata changes only. |
| Rejected namespace | PASS: fifteen exact additions, no pre-existing rejection changed. |
| No-change nodes | PASS: all twenty-three deep-equal; aggregate hash identical. |
| M1/M2/M9/bridges/target | PASS: every protected status and body deeply unchanged. |
| Exponents | PASS: \(1/3\), \(0.3144831759740614\ldots\), and \(1/4\) nodes deeply unchanged. |
| Relation targets | PASS: zero invalid relations before and after. |
| Cycles | PASS: no new dependency or implies cycle; three pre-existing dependency SCCs unchanged. |
| Evidence paths | PASS: 41 occurrences, 23 unique, zero missing; judge path exists. |
| Production validation | PASS: recovered start, patch preconditions, and live graph all validate with zero issue. |

## 6. Dependencies and exact artifacts used

The five assigned evidence artifacts were read completely:

1. protocol.md — SHA-256
   f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a.
2. state/proof_obligations.yml — SHA-256
   75b44fe68f9c6e094d2ab6e643be3c0309320ef84e73ca22d692698440eeed13.
3. rounds/codex-managed/m9-m1-t1-fast-height-jump-coboundary-gate/state_patch.json
   — SHA-256
   071b87d0a81dc8bf257eab6c2e5c79de5a02a352960c46971d0e5daa9fa8f3b6.
4. rounds/codex-managed/m9-m1-t1-fast-height-jump-coboundary-gate/controls/preapply_independent_reverse_replay_audit.md
   — SHA-256
   37b912ecaad83d34e51e3efded1a2038f70047fdb5d5e82d83466bbfa9dfa960.
5. rounds/codex-managed/m9-m1-t1-fast-height-jump-coboundary-gate/reviews/conductor_round191_adjudication.md
   — SHA-256
   89a2c793e4ca1e693322e363834c19ebfcaf175718ed3e61cbe98d8ff2a32bda.

The production implementation used for the in-memory replay was:

6. math_collab/proof_obligations.py — SHA-256
   384070a83b4ce1f56ebdceb0711680a6e889d4d43af3a40a8b6002319114a437.
7. math_collab/validate_state_patch.py — SHA-256
   cfa914c54bfa172cc94354dc7e904e866d4e69c96cd8be7bfbf68b5a295080e8.

Patch-referenced evidence paths were checked for existence only. No
State Patch, live state, proof draft, validation matrix, synthesis, or
other shared artifact was edited. All inverse, replay, comparison, and
cycle computations were performed in memory.

## 7. Recommended state effect

Retain the live Round 191 graph unchanged. The application is exactly
reversible, byte-reproducible, and protected-scope safe. No corrective
patch is required.

Keep M9-M1-hard-top-high-radical-small-t-residual-estimate open, with
the rho-large remainder and exact \(Y/(Qm)\) deficit as its next
analytic target. Keep every no-change owner, bridge, target, and
exponent at its present status.

**PASS**
