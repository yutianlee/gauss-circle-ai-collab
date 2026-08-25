# Round 162 terminal State Patch scope audit

- Campaign: `m9-m2-hard-top-t1-close-factor-bilinear-gate`
- Round: 162
- Review: `state_patch_scope_round162`
- Verdict: **GREEN**
- Scope: terminal State Patch counts, node calibration, graph direction,
  evidence, parent scope, and downstream quarantine only
- Mutation: none

## 1. Result

**GREEN.**  The mechanically validated State Patch is also mathematically
and graph-theoretically calibrated.  Its operation counts are exactly

\[
 \boxed{1\ {
m create},\quad 2\ {
m updates},\quad
 12\ {
m rejects},\quad 16\ {
m no\text{-}change entries}.}
\tag{162.SP1}
\]

It has no `correct_rejected` operation.  The created identifier is absent
from the current graph, all three dependencies and both update targets are
present, all sixteen no-change identifiers are present, and none of the
twelve rejected identifiers is already recorded.

The new statement is conservative at the two sensitive seams:

1. every literal hard edge, star, endpoint transition, nonstationary piece,
   collar tail, and the full signed Möbius aggregate remains open; only a
   compact smooth-interior positive route capacity is asserted;
2. Bettin--Chandee is not described as having no formal embedding.  The
   statement records its integral-subcase one-point-inverse placement and
   parks it because the printed factor is already \((JL)^{1/2}\) and the
   coefficient is separated.

The dependency direction is forward and acyclic.  The new obstruction
depends on the accepted Round-137 self-return and the two accepted
Round-161 radical nodes.  Exactly two open hard-TOP parents then depend on
the new node.  No accepted antecedent receives a reverse edge.

## 2. Exact statement and hypotheses

### 2.1 Operation ledger

The patch has the following exact shape.

| Operation | Count | Exact target |
|---|---:|---|
| `create` | 1 | `M9-M2-hard-top-t1-character-poisson-product-collar-obstruction` |
| `update` | 2 | `M9-M2-top-endpoint-signed-cone`; `M9-M2-top-endpoint-density-discrepancy-energy` |
| `reject` | 12 | the twelve Round-162 overclaims listed in Section 2.3 |
| `no_change` | 16 | the sixteen quarantined antecedent/downstream nodes listed in Section 2.4 |
| `correct_rejected` | 0 | none |

The new node has

```text
type: obstruction
track: M9_analytic
status: proved_internal
dependencies:
  - M9-M2-hard-top-product-fibre-transform-self-return
  - M9-M2-hard-top-radical-long-channel-exact-collision-control
  - M9-M2-hard-top-radical-frequency-common-test-source-obstruction
implies: []
blockers: []
```

All three dependencies currently have `proved_internal` status.  Both
update targets currently have `open` status.

### 2.2 Statement calibration

The created statement retains the literal \(t=1\) scalar, exact projector,
even-\(d_2\) branch, and character orientation.  With

\[
 Q=[a^2,c],\qquad R=[b^2,c],\qquad d_1=Qm,\quad d_2=Rn,
\]

it records the exact character transform

\[
 \sum_m\chi_4(m)g(m)
 =\frac i2\sum_{s\ {
m odd}}\chi_4(s)\widehat g(s/4),
\tag{162.SP2}
\]

the saddle \(d_1^*=4XQ^2d_2/s^2\), phase \(XQd_2/s\), exact dual cone,
and the compact smooth-interior collar

\[
 |s\ell-XQR|\ll QRJ/L.
\tag{162.SP3}
\]

The per-pair scale \(L^{3/2}/(QR\sqrt J)\) and factor-pair count
\((QRJ/L+1)(XQR)^\varepsilon\) give only the termwise positive capacity

\[
 \sqrt{JL}\,X^\varepsilon
 =L^{3/2}\bigl(H/L+O(L^{-1})\bigr)X^\varepsilon.
\tag{162.SP4}
\]

The statement immediately quarantines the interpretation of (162.SP4): it
is neither physical mass, an upper bound for the complete scalar, nor a
lower bound.  It also says explicitly that literal hard boundaries and the
full signed Möbius aggregate remain open.  This matches the selected kernel
and adjudication and does not promote the rejected blanket hard-edge safety
claim.

The source sentence is equally calibrated.  It parks only the six audited
placements after literal coefficient and power restoration.  In particular,
it states that Bettin--Chandee has a formal integral-subcase degenerate
placement but an adverse \((JL)^{1/2}\) printed factor.  The corresponding
reject entry separately forbids the stronger false reading that no
Kloosterman source has any formal degenerate embedding.

### 2.3 The twelve rejects

The reject array contains exactly these distinct identifiers:

1. `Round162-t1-close-factor-target-is-proved`;
2. `Round162-positive-product-collar-is-physical-mass-or-lower-bound`;
3. `Round162-positive-product-collar-bounds-the-complete-physical-scalar`;
4. `Round162-Mobius-opening-has-free-QR-decay`;
5. `Round162-local-divisor-completion-proves-the-window`;
6. `Round162-second-character-Poisson-transform-contracts`;
7. `Round162-standard-positive-differencing-exploits-chi4`;
8. `Round162-all-literal-hard-boundaries-are-target-safe`;
9. `Round162-no-Kloosterman-source-has-any-formal-degenerate-embedding`;
10. `Round162-named-source-no-match-excludes-future-theorems`;
11. `Round162-t1-no-go-closes-remaining-few-point-channels-or-hard-TOP`;
12. `Round162-t1-no-go-improves-a-global-exponent`.

Together they quarantine target, mass, upper-bound, opening-cost,
completion, involution, differencing, hard-edge, source, remaining-channel,
parent, and exponent overclaims without rejecting the proved obstruction.

### 2.4 The sixteen no-change entries

The no-change array contains exactly:

1. `M9-M2-hard-top-product-fibre-transform-self-return`;
2. `M9-M2-hard-top-radical-long-channel-exact-collision-control`;
3. `M9-M2-hard-top-radical-frequency-common-test-source-obstruction`;
4. `M9-M2-hard-top-truncated-divisor-energy-and-radical-control`;
5. `M9-M2-hard-top-square-product-entry-sector`;
6. `M9-M2-physical-one-count-assembly`;
7. `M9-M2-smooth-balanced-quarter-packet-estimate`;
8. `M9-M2-smooth-unbalanced-three-quarter-estimate`;
9. `M9-M2`;
10. `M9-M1`;
11. `M9-endpoint-uniformity`;
12. `M9`;
13. `Conditional-bridge`;
14. `GC-partial-one-third`;
15. `GC-external-Li-Yang-theta-star`;
16. `GC-target`.

This is the correct antecedent, sibling-owner, assembly, bridge, theorem,
and exponent quarantine.

## 3. Proof and graph derivation

### 3.1 Dependency direction and cycle audit

Let \(C\) denote the created node, let \(P_1,P_2\) be the two updated open
parents, and let \(D_1,D_2,D_3\) be the three accepted dependencies.  The
only new dependency edges are

\[
 C\longrightarrow D_i\quad(1\le i\le3),\qquad
 P_j\longrightarrow C\quad(1\le j\le2).
\tag{162.SP5}
\]

In the current graph no \(D_i\) reaches either \(P_j\), and after inserting
the proposed edges \(C\) reaches neither \(P_1\) nor \(P_2\).  Therefore
neither parent-to-new edge closes a directed cycle.  Conversely, both open
parents reach \(C\), exactly as intended.  The patch adds no `implies` edge,
so it cannot create an implication cycle or a reverse promotion path.

The omission of a direct dependency on
`M9-M2-hard-top-truncated-divisor-energy-and-radical-control` is safe: that
accepted node already lies upstream of the Round-137 and Round-161
dependencies.  Adding it again would be redundant, not corrective.

### 3.2 Evidence audit

The created node has ten distinct positive evidence paths.  Every path
exists.  They comprise:

- the selected proof kernel;
- three primary Round-162 reports;
- the selected candidate and conductor reproduction control;
- three independent seam/scope reviews;
- the conductor adjudication.

There are no negative or inconclusive entries on the created node.  This is
appropriate because the evidence proves the narrowly stated obstruction,
not the physical target.

Each open parent receives the same seven existing artifacts as
`evidence.inconclusive`: the kernel, candidate, three reports, source/graph
review, and adjudication.  All seven paths exist.  The classification is
correct: those artifacts identify an obstruction and the next signed
interface but prove no parent estimate.  The patch does not add them as
parent-positive evidence and does not erase any existing evidence.

Across the create and two update arrays there are 24 evidence references
and ten unique paths; the repetition is intentional because the same
validated packet supports the node and scopes both parents.

### 3.3 Parent scope

Only the two open hard-TOP parents are updated.  The signed-cone next action
retains the literal \(t=1\) target and then the
\(L\ll D\ll L^2,t\ll\sqrt L\) few-point channels.  The
density-discrepancy next action preserves the accepted one-count and
completed-real-part connector and explicitly says that the positive collar
is not a completed-real-part estimate.

No parent status, statement, implication, or blocker is changed.  No update
is sent directly to `M9-M2-physical-one-count-assembly`, either smooth M2
packet, `M9-M2`, or a more distant owner.  This is the narrowest valid graph
placement.

### 3.4 Downstream and exponent quarantine

The created statement itself denies every downstream inference: it proves
no \(t=1\) target, other few-point channel, hard TOP, smooth packet,
M9--M2, M9, bridge, quarter theorem, or exponent.  Rejects 11--12 enforce
the same limit, while the sixteen no-change entries preserve all relevant
statuses.  In particular:

- the internal theorem remains `GC-partial-one-third`;
- the external Li--Yang benchmark remains
  \((3292+25\sqrt{1717})/13762\);
- `GC-target` remains open.

The round-assessment scores are metadata only and do not alter this graph
scope.

## 4. First doubtful or unproved step

The first affirmative statement still missing is a target-strength bound
for the full signed Möbius-coupled family whose compact smooth principal
interface is

\[
\frac{L^{3/2}}{\sqrt J}
\sum_{a,b,c}\frac{\mu(a)\mu(b)\mu(c)\chi_4(Q)}{QR}
\sum_{N\approx XQR}
\sum_{\substack{s\mid N,\ s\ {
m odd}\\
\sqrt{QN/R}\le s\le2\sqrt{QN/R}}}
\chi_4(s)\mathcal K_{Q,R}(N;s),
\tag{162.SP6}
\]

with arbitrary-real-centre uniformity, even \(d_2\), actual profiles, hard
edges, floors, stars, endpoint transitions, nonstationary pieces, and collar
tails retained before every positive norm.

Equation (162.SP6) is not a complete formula for the omitted hard pieces.
Neither the kernel nor the State Patch claims otherwise.  Even a later proof
of this \(t=1\) face would leave the compatible remaining few-point channels
open.  This is exactly the next action recorded on the new node and both
parents.

## 5. Required control tests and outcomes

| Required control | Outcome |
|---|---|
| `operation_counts_1_2_12_16` | **Pass.** Counts are exactly 1 create, 2 updates, 12 rejects, and 16 no-change entries; `correct_rejected` is empty. |
| `new_id_fresh_and_refs_exist` | **Pass.** The created ID is absent; all dependencies, update targets, and no-change IDs exist; all reject IDs are fresh. |
| `node_statement_matches_kernel` | **Pass.** Projector, parity, character sign, saddle, profile, normalization, involution, collar, factor count, and positive capacity match the selected kernel and adjudication. |
| `hard_edge_calibration` | **Pass.** Smooth-interior capacity is separated from literal hard-edge ownership; hard pieces remain open in statement, next action, and Reject 8. |
| `Bettin_Chandee_calibration` | **Pass.** Formal integral-subcase embedding is acknowledged; only target-strength use is parked, with the adverse \((JL)^{1/2}\) factor recorded. |
| `source_no_go_scope` | **Pass.** Only audited placements are parked; future and bespoke coefficient-sensitive theorems remain possible. |
| `dependency_direction` | **Pass.** New node points to three accepted antecedents; two open parents point to the new node. |
| `cycle_check` | **Pass.** No antecedent reaches either updated parent, and the new node reaches neither parent. |
| `evidence_paths_and_classification` | **Pass.** Ten distinct node-positive paths and both seven-path parent-inconclusive sets exist; no parent-positive promotion occurs. |
| `parent_scope` | **Pass.** Exactly the signed-cone and density-discrepancy parents are updated; both remain open. |
| `remaining_few_point_scope` | **Pass.** The \(L\ll D\ll L^2,t\ll\sqrt L\) channels remain explicit in the next actions. |
| `downstream_and_exponent_quarantine` | **Pass.** Physical assembly, smooth packets, M9--M2, M9--M1, endpoint uniformity, M9, bridge, internal theorem, external benchmark, and target remain unchanged. |

The reported mechanical dry-validator result and this independent scope
audit agree.

## 6. Dependencies and exact artifacts used

This audit used exactly:

1. `rounds/codex-managed/m9-m2-hard-top-t1-close-factor-bilinear-gate/state_patch.json`;
2. `proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md`;
3. `rounds/codex-managed/m9-m2-hard-top-t1-close-factor-bilinear-gate/reviews/conductor_round162_adjudication.md`;
4. `state/proof_obligations.yml` in its current pre-Round-162-patch state.

Read-only checks independently reproduced the operation counts, current-ID
presence, freshness of created/rejected IDs, hypothetical dependency
reachability, update-target statuses, and existence/classification of every
evidence path.  No source card, proof kernel, candidate, report,
adjudication, patch, graph, synthesis, strategy, validation file, or other
artifact was edited.

## 7. Recommended state effect

**Apply the State Patch exactly as written.  No repair is required.**

The exact effect is:

1. create the one calibrated `proved_internal` obstruction node;
2. add it as a dependency and add the selected packet only as inconclusive
   evidence to the two open hard-TOP parents;
3. record all twelve rejects;
4. preserve all sixteen no-change nodes;
5. make no other status, statement, implication, blocker, evidence,
   downstream, bridge, theorem, or exponent change.

Terminal decision:
`hard_top_t1_close_factor_bilinear_no_go`.
