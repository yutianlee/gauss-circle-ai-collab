# Round 197 post-apply scope/protected-state audit

- Actual post-apply graph SHA-256:
  `8192DF329A85010676A01BF90D62901D810AE10265762186DD3EAB17DA7B32AE`
- Applied State Patch SHA-256:
  `A28050A9D157D7D956DA336BBDEAD4296C88EB1B8A3DEFEB90495B1B37CA2068`
- Reconstructed starting graph SHA-256:
  `B9B95784B097B3E30BED95F418AE14E57BF5F03A4A52975BEEEFA8DB85B7F8AE`
- Verdict: **REPAIR**
- Shared-state mutation by this audit: none

## 1. Result

**REPAIR for one post-apply evidence-classification hygiene defect only.**
Every requested graph, dependency, owner, Round-195, protected-scope, cycle,
parent, target, and exponent control passes on the actual graph.  Exact inverse
reconstruction also passes.  The applied graph contains:

- exactly one new `proved_internal` obligation;
- exactly one changed pre-existing obligation, the still-open hard-small-$t$
  owner;
- exactly twenty-two new rejected-claim records; and
- all twenty-eight explicit `no_change` obligations deep-equal to their
  reconstructed pre-apply values.

The single defect is that production application supplied the adjudication as
`judge_ref`.  The created node already classified that same path as positive,
so the automatic merge appended it to `evidence.inconclusive` as well.  Thus

`rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/reviews/conductor_round197_adjudication.md`

appears in both positive and inconclusive evidence.  The final State Patch had
removed this cross-class overlap; production application reintroduced it.
This does not change mathematics or graph reachability, but it must be removed
through a mechanically validated hygiene correction before post-apply closure.

## 2. Exact statement and hypotheses

The actual created node is

`M9-M1-hard-top-t1-rho-large-P2-common-cell-allocation-commutator-sector`.

It has status `proved_internal`, `implies: []`, `blockers: []`, and exactly the
four accepted direct prerequisites from Rounds 184, 185, 193, and 195.  Its
statement retains the repaired theorem fidelity: the dead sharp code is
determined only by named arithmetic, support, and zero-extension predicates,
while coefficient values and the values of $\rho_N$, $\eta_L$, and the smooth
factors are excluded.  It proves only $P_{\rm cc}$ and its exact Round-195
open-packet intersection.  It asserts no nonemptiness, density, lower mass,
complete $P_2$, $P_1$, owner, parent, bridge, target, or exponent result.

The only updated old node is

`M9-M1-hard-top-high-radical-small-t-residual-estimate`.

It remains `open`.  Its added dependency is the new node, exactly once.  Its
new action retains the three-piece physical $P_2$ complement, all of $P_1$,
complete original-$t=1$ and original-$t\ge2$ gaps, the near-resonant
complement, smooth M1, GAR, M2, endpoint uniformity, M9, and both bridges as
open.

## 3. Proof or derivation

### 3.1 Actual mutation census and exact reconstruction

The actual state file has the requested post-apply hash and passes the
repository graph validator.  Reversing the State Patch in memory by

1. removing the one created obligation;
2. removing the twenty-two newly appended rejected-claim records;
3. removing the new owner dependency and inconclusive-evidence additions; and
4. restoring the saved Round-196 owner `next_action`, `last_updated_round`,
   and `last_updated_at`

produces a validator-clean graph whose canonical SHA-256 is exactly
`B9B95784B097B3E30BED95F418AE14E57BF5F03A4A52975BEEEFA8DB85B7F8AE`.
The reconstructed graph is therefore the exact declared starting graph.

Comparing actual post-apply obligations with that reconstruction, the only
changed pre-existing obligation is the declared owner.  Its exact diff paths
are:

- `dependencies`;
- `evidence.inconclusive`;
- `next_action`;
- `last_updated_round`; and
- `last_updated_at`.

Its actual status is still `open`, its `last_updated_round` is 197, and the new
dependency occurs once.  No old rejected-claim record changed; the twenty-two
Round-197 rejection IDs occur once each and are appended after all old
records.

### 3.2 Direct dependencies and graph cycles

The actual created node depends exactly on:

1. `M9-M1-hard-top-t1-comparable-factor-exchange-sector`;
2. `M9-M1-hard-top-t1-residual-fejer-tangent-gcd-reduction`;
3. `M9-M1-hard-top-t1-rho-large-gcd-scaled-close-sector`; and
4. `M9-M1-hard-top-t1-rho-large-P2-absolute-capacity-sectors`.

Each exists and remains `proved_internal`.  The owner reaches the new node,
while the new node does not reach the owner.  None of the four prerequisites
reached the owner in the reconstructed starting graph.

An independent strongly-connected-component computation finds the same three
pre-existing cyclic SCCs before and after application.  Their member sets are
identical, and the new node belongs to none.  In particular, Round 197 depends
on Round 195, Round 195 does not depend on Round 197, and no two-cycle or
longer new cycle was created.

### 3.3 Round 195 and the twenty-eight protected obligations

All twenty-eight unique `no_change` IDs exist in the actual and reconstructed
graphs and are pairwise deep-equal.  Round 195 is explicitly among them:

`M9-M1-hard-top-t1-rho-large-P2-absolute-capacity-sectors`.

Its status remains `proved_internal`; its statement, dependencies, evidence,
next action, terminal history, and metadata are unchanged.  The refined
remainder occurs only in the new node and open owner's action, so historical
Round-195 scope has not been rewritten.

The same deep-equality check passes for both M1 parents, GAR, M1, all M2
parents, endpoint uniformity, M9, both bridges, both theorem records, the
target, and the elementary divisor bound.

### 3.4 Parent, target, and exponent quarantine

`M9-M1`, `M9-M2`, `M9-endpoint-uniformity`, `M9`, and `GC-target` remain
`open`.  `Conditional-bridge` and `GC-global-M1-alternative-bridge` remain
`derived_under_assumptions`; neither is strengthened.  `GC-partial-one-third`
and `GC-external-Li-Yang-theta-star` remain respectively `proved_internal`
and `proved_external_dependency`, with their full objects deep-equal.

Consequently the internal $1/3$, accepted external
$0.3144831759740614\ldots$, and target $1/4$ records are unchanged.  No new
path to a parent, bridge, theorem, or target is introduced by the subordinate
common-cell node.

### 3.5 Isolated post-apply hygiene defect

The created node's evidence buckets have exactly one nonempty cross-bucket
intersection:

\[
 \texttt{positive}\cap\texttt{inconclusive}
 =\{\texttt{conductor\_round197\_adjudication.md}\}.
\]

The positive/negative and negative/inconclusive intersections are empty.  All
evidence paths exist.  The duplicate arose from the production `judge_ref`
merge, not from the final State Patch.  The repository graph validator does
not test cross-bucket disjointness, which is why structural validation still
returns clean.

The adjudication is intentionally positive evidence for the created proved
node.  The repair is therefore to remove only its duplicate occurrence from
that node's `evidence.inconclusive` bucket.  No other evidence classification
or graph field should change.

## 4. First doubtful or unproved step

The first post-apply state defect is the one evidence path classified both
positive and inconclusive.  It is a provenance-hygiene defect, not a
mathematical or scope defect.

The first unproved mathematical region remains exactly the recorded open
complement
$P_{\partial\rm lit}\dot\cup P_{s\rm f}\dot\cup P_{g\rm f}$ inside the
Round-195 open packets, together with all of $P_1$ and the other owner gaps.
The actual graph does not promote any of those regions.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| actual post-apply hash | **PASS.** Exact SHA-256 `8192DF329A85010676A01BF90D62901D810AE10265762186DD3EAB17DA7B32AE`. |
| repository graph validator | **PASS.** The actual graph is structurally valid. |
| created-node census | **PASS.** Exactly one Round-197 obligation exists with the intended status and statement. |
| old-obligation mutation surface | **PASS.** Only the open hard-small-$t$ owner changed. |
| owner status and edge | **PASS.** Status remains `open`; the new dependency occurs once. |
| direct dependencies | **PASS.** Exactly four existing accepted ancestors. |
| graph cycles | **PASS.** The three pre-existing SCCs are identical; no new cycle exists. |
| Round-195 immutability | **PASS.** Explicitly protected and deep-equal. |
| twenty-eight `no_change` nodes | **PASS.** Unique, existing, and all deep-equal. |
| exact inverse reconstruction | **PASS.** Canonical hash returns exactly to `B9B95784...B7F8AE`. |
| parent and target quarantine | **PASS.** Every protected parent, bridge, theorem, and target object is unchanged. |
| exponent quarantine | **PASS.** $1/3$, $0.3144831759740614\ldots$, and $1/4$ are unchanged. |
| old rejected claims | **PASS.** Deep-preserved; exactly twenty-two new records were appended. |
| evidence paths | **PASS.** Every path exists. |
| evidence-bucket disjointness | **REPAIR.** The adjudication is both positive and inconclusive on the created node. |

## 6. Dependencies and exact artifacts used

1. `state/proof_obligations.yml`, actual SHA-256
   `8192DF329A85010676A01BF90D62901D810AE10265762186DD3EAB17DA7B32AE`.
2. `rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/state_patch.json`,
   SHA-256
   `A28050A9D157D7D956DA336BBDEAD4296C88EB1B8A3DEFEB90495B1B37CA2068`.
3. `rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/controls/preapply_hostile_graph_scope_protection_audit.md`.
4. `rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/reviews/conductor_round197_adjudication.md`.
5. `rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/synthesis.md`.
6. `math_collab/proof_obligations.py` and
   `math_collab/validate_state_patch.py`.

All comparison, SCC, reconstruction, and validation work was read-only or
in-memory.  This audit did not edit the graph, State Patch, synthesis, kernel,
candidate, or any other shared state.

## 7. Recommended state effect

**Apply one mechanically validated Round-197 hygiene correction, then
re-audit the resulting graph hash.**  Remove only

`rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/reviews/conductor_round197_adjudication.md`

from the created node's `evidence.inconclusive` bucket, retaining it in
`evidence.positive`.  Do not change the created theorem, status, dependencies,
owner update, rejected claims, Round 195, any protected obligation, terminal
scope, parent, bridge, theorem, target, or exponent record.

After that one-field hygiene correction, require a fresh exact-hash,
cross-bucket-disjointness, protected-state, cycle, and reverse audit before
closing Round 197.
