# Round 197 post-apply scope/protected-state post-repair verification

- Corrected authoritative graph SHA-256:
  `8AEA2AB5B088A0B29A434347FFC4509C70E79F53E450814920E3C83165A1AB69`
- Pre-correction post-apply graph SHA-256:
  `8192DF329A85010676A01BF90D62901D810AE10265762186DD3EAB17DA7B32AE`
- Evidence-hygiene correction SHA-256:
  `1F9BACF52793FB93093135009E5BBE10F1E80BA5684B88B3AF6BEA758BA375EF`
- Original State Patch SHA-256:
  `A28050A9D157D7D956DA336BBDEAD4296C88EB1B8A3DEFEB90495B1B37CA2068`
- Verdict: **PASS**
- Shared-state mutation by this audit: none

## 1. Result

**PASS / GREEN.**  The single post-apply evidence overlap identified in
`postapply_scope_protected_state_audit.md` is repaired exactly.  The conductor
adjudication remains positive evidence for the created Round-197 node and no
longer also appears in its inconclusive bucket.  The created node now has
evidence counts

`positive/negative/inconclusive = 14/0/11`

with all three pairwise bucket intersections empty.

The correction changes no theorem text, status, dependency, implication,
blocker, owner update, rejection, protected obligation, parent, bridge,
target, terminal scope, or exponent.  The authoritative graph validates
cleanly, retains exactly one Round-197 created node and only one changed
pre-Round-197 obligation, preserves Round 195 and all twenty-eight
`no_change` objects, introduces no new cycle, and still reverses exactly to
the declared Round-197 starting graph.

## 2. Exact statement and hypotheses

The created obligation remains

`M9-M1-hard-top-t1-rho-large-P2-common-cell-allocation-commutator-sector`

with status `proved_internal`, `implies: []`, `blockers: []`, and exactly the
accepted Round-184, Round-185, Round-193, and Round-195 dependencies.  Its
statement is unchanged: the common-cell dead code depends only on named
arithmetic, support, and zero-extension predicates, excludes coefficient and
smooth-factor values, and proves only $P_{\rm cc}$ and its exact Round-195
open-packet intersection.

The sole pre-existing obligation changed by the original Round-197 patch is
still

`M9-M1-hard-top-high-radical-small-t-residual-estimate`.

It remains `open`, depends on the new node exactly once, and retains the exact
three-piece $P_2$ complement, $P_1$, and every other owner gap in its
`next_action`.  The hygiene correction does not touch this owner.

## 3. Proof or derivation

### 3.1 Exact correction replay

Starting from the corrected graph, restoring the adjudication path to the
created node's inconclusive evidence and restoring that node's pre-correction
timestamp reconstructs the exact pre-correction graph hash

`8192DF329A85010676A01BF90D62901D810AE10265762186DD3EAB17DA7B32AE`.

The hygiene correction validates against that reconstructed object.  Applying
it in memory and normalizing the dynamic timestamp to the actual stored value
`2026-08-31T00:16:13` reproduces the corrected authoritative graph exactly.
The correction's complete graph footprint is therefore:

1. remove the adjudication path from the created node's
   `evidence.inconclusive` bucket; and
2. update that created node's application timestamp.

The path remains in `evidence.positive`.  No other evidence path or bucket
changes.

### 3.2 Evidence disjointness and existence

For the corrected created node,

\[
 E_+\cap E_-=E_+\cap E_{?}=E_-\cap E_{?}=\varnothing.
\]

The conductor adjudication belongs to $E_+$ and not $E_{?}$.  All 25 evidence
paths are distinct across the classified union and exist as repository files.
The three bounded finite-orbit controls remain inconclusive only; no diagnostic
artifact is promoted into theorem evidence.

### 3.3 Original Round-197 footprint and reconstruction

Applying the original Round-197 inverse directly to the corrected graph—remove
the created node and twenty-two Round-197 rejected claims, remove the one owner
dependency and its evidence additions, and restore the saved Round-196 owner
action and metadata—produces a validator-clean graph with exact canonical hash

`B9B95784B097B3E30BED95F418AE14E57BF5F03A4A52975BEEEFA8DB85B7F8AE`.

Relative to that reconstructed start, the corrected graph contains exactly
one created obligation and exactly one changed pre-existing obligation, the
still-open owner.  All twenty-two Round-197 rejections remain the intended new
records, and all older rejected claims remain unchanged.

### 3.4 Dependencies, cycles, and protected scope

All four direct prerequisites of the created node exist and remain
`proved_internal`.  The owner reaches the new node; the new node does not
reach the owner.  Round 197 depends on Round 195, while Round 195 has no
reverse dependency.

The corrected graph has exactly the same three pre-existing cyclic SCCs as
the reconstructed starting graph.  Their member sets are identical, and the
new node belongs to none.  The evidence correction changes no edge, so it
cannot create a graph cycle.

All twenty-eight explicit `no_change` obligations are unique, exist, and are
deep-equal to their reconstructed starting objects.  This includes the
accepted Round-195 node, whose status, theorem, dependencies, evidence,
metadata, and historical scope remain unchanged.

### 3.5 Parent, target, terminal, and exponent quarantine

Both M1 parents, GAR, M1, all M2 parents, endpoint uniformity, M9, both
bridges, the theorem records, and `GC-target` remain deep-equal to their
starting objects.  M1, M2, endpoint uniformity, M9, and the target remain
open; neither bridge is strengthened.

The internal $1/3$, accepted external $0.3144831759740614\ldots$, and target
$1/4$ records are unchanged.  The correction adds no conclusion and leaves
the truthful frozen terminal scope
`p2_four_corner_orbit_boundary_self_return_no_go` intact.

## 4. First doubtful or unproved step

No post-repair evidence, scope, dependency, cycle, protection, or reversal
defect remains.  The first unproved mathematical step is still the exact
physical complement
$P_{\partial\rm lit}\dot\cup P_{s\rm f}\dot\cup P_{g\rm f}$ inside the
Round-195 open packets, together with all of $P_1$ and the other declared
owner gaps.  The corrected graph does not promote any part of that boundary.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| corrected graph hash | **PASS.** Exact SHA-256 `8AEA2AB5B088A0B29A434347FFC4509C70E79F53E450814920E3C83165A1AB69`. |
| repository graph validation | **PASS.** Zero issues. |
| correction-patch validation/replay | **PASS.** Normalized replay reproduces the corrected graph exactly. |
| evidence counts | **PASS.** Exactly `14/0/11`. |
| cross-bucket evidence overlap | **PASS.** All three pairwise intersections are empty. |
| adjudication classification | **PASS.** Positive only, not inconclusive. |
| evidence path existence | **PASS.** All classified paths exist. |
| created-node scope/status | **PASS.** Unchanged `proved_internal` subordinate theorem. |
| dependency and implication fields | **PASS.** Four accepted ancestors; `implies` and `blockers` remain empty. |
| owner-only old-node mutation | **PASS.** The sole changed pre-existing obligation remains open. |
| Round-195 immutability | **PASS.** Explicitly protected and deep-equal. |
| twenty-eight protected objects | **PASS.** Unique and all deep-equal. |
| graph cycles | **PASS.** The pre-existing SCC set is unchanged; the new node is acyclic. |
| parent/bridge/target quarantine | **PASS.** No protected status, statement, edge, or evidence drift. |
| exponent quarantine | **PASS.** $1/3$, $0.3144831759740614\ldots$, and $1/4$ are unchanged. |
| original-start reconstruction | **PASS.** Exact canonical hash `B9B95784...B7F8AE`. |

## 6. Dependencies and exact artifacts used

1. `state/proof_obligations.yml`, corrected SHA-256
   `8AEA2AB5B088A0B29A434347FFC4509C70E79F53E450814920E3C83165A1AB69`.
2. `rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/state_patch_evidence_hygiene_correction.json`,
   SHA-256
   `1F9BACF52793FB93093135009E5BBE10F1E80BA5684B88B3AF6BEA758BA375EF`.
3. `rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/state_patch.json`,
   SHA-256
   `A28050A9D157D7D956DA336BBDEAD4296C88EB1B8A3DEFEB90495B1B37CA2068`.
4. `rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/controls/postapply_scope_protected_state_audit.md`.
5. `rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/reviews/conductor_round197_adjudication.md`.
6. `math_collab/proof_obligations.py` and
   `math_collab/validate_state_patch.py`.

All validation, comparison, reconstruction, SCC, and replay work was read-only
or in-memory.  This audit did not edit the graph, either State Patch, kernel,
candidate, synthesis, or any other shared state.

## 7. Recommended state effect

**Retain authoritative graph SHA-256
`8AEA2AB5B088A0B29A434347FFC4509C70E79F53E450814920E3C83165A1AB69`
unchanged.**  The evidence hygiene defect is closed, all original Round-197
scope and dependency protections remain intact, and no further corrective
graph mutation is warranted.

Round 197 may close under
`p2_four_corner_orbit_boundary_self_return_no_go`, subject to the remaining
independent post-apply controls.  Do not alter Round 195, the open owner, any
protected parent, bridge, theorem, target, or exponent record.
