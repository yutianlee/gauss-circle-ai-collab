# Round 175 post-application graph scope verification

- Campaign: `m9-m2-hard-top-t1-residual-whole-chain-actual-symbol-scale-correlation-gate`
- Round: 175
- Role: independent post-application delta, cycle, sentinel, and reverse auditor
- Starting graph SHA-256: `e40c214351d06bf05212e25fffbec0f1a4808be21cb9098ba25823f0d9bbf211`
- Applied graph SHA-256: `9409651dccbbd1c69547546b245ba04c21d2a280173733ae37b693f9894c8b03`
- Final State-Patch SHA-256: `0c46a31499e6a9f93a972c50e1b60a5911301987c53caed3142bd44e424b81d2`
- Application mode: raw patch, round index 175, `judge_ref=None`
- Allocation: 100% analytical/algebraic; 0% numerical
- Verdict: **GREEN**

## 1. Result

The authoritative post-application graph is **GREEN**. Its raw bytes are
already in repository canonical form and have exactly the announced SHA-256

`9409651dccbbd1c69547546b245ba04c21d2a280173733ae37b693f9894c8b03`.

Independent reversal of the final State Patch produces canonical bytes with
exactly the starting SHA-256

`e40c214351d06bf05212e25fffbec0f1a4808be21cb9098ba25823f0d9bbf211`.

Reapplying the patch in memory to that reconstructed starting graph, using
raw mode and the observed application timestamp
`2026-08-27T02:39:54`, reproduces the authoritative post-application object,
canonical bytes, and `9409651...b03` hash exactly. This two-way equality
excludes an undeclared graph mutation.

The declared and observed operation counts are both exactly

| Operation | Declared | Observed |
|---|---:|---:|
| `create` | 1 | 1 |
| `update` | 3 | 3 |
| `correct_rejected` | 0 | 0 |
| `reject` | 13 | 13 |
| `no_change` | 18 | 18 |

The obligation count is 377 before and 378 after. The separate
rejected-claim ledger is 1,411 before and 1,424 after. Exactly one obligation
was created, exactly three pre-existing obligation records changed, exactly
thirteen rejected-claim records were appended, and nothing was deleted.
There is no pre-existing status drift, theorem change, exponent change,
dependency cycle, or unlisted record mutation.

## 2. Exact applied statement and hypotheses

The sole created record is

`M9-M2-hard-top-t1-residual-whole-chain-scale-coboundary-positive-capacity-obstruction`.

It is exactly the patch-declared `obstruction` on track `M9_analytic`, with
status `proved_internal`, owner `Codex conductor`, three dependencies, no
implication, and no blocker. Its evidence buckets have the exact applied
cardinalities

\[
 (\#\mathrm{positive},\#\mathrm{negative},\#\mathrm{inconclusive})
 =(18,0,0).
\]

Its only fields beyond the literal create record are
`last_updated_round: 175` and
`last_updated_at: 2026-08-27T02:39:54`. In particular, raw application added
no adjudication path to the inconclusive bucket.

The mathematical statement retains the complete literal residual sequence,
full-line zero extension, both absolute-parity branches, exact character and
ordinary-frequency transform, every cardinal cell and arithmetic opening,
all endpoint and transition values, the collectively restored ordinary-zero
sector, the once-only short correction, and a strict terminal Fejer link only
when (M) is not reached by exact doubling. It records

\[
 \mathcal N_{R,S}=Q_S^*-Q_R^*,\qquad
 \sum_{j<K}\mathcal N_{R_j,R_{j+1}}=Q_M^*-Q_{R_0}^*,
\]

\[
 |\mathcal Z_{R_0,M}|+|B_{\rm short}|
 \ll_\varepsilon L^3X^\varepsilon,
 \qquad
 \sum_{j<K}\mathcal N_j
 =2(T_{26}+B_{\rm short})-\mathcal Z_{R_0,M},
\]

and (Q_{R_0}^*\ll_\varepsilon L^3X^\varepsilon). Thus the
one-sided chain target is equivalent at target strength to the still-open
literal theorem (Q_M^*\ll_\varepsilon L^3X^\varepsilon), hence to K26
after the paid seams. Coefficient-independent positivity reaches only
(L^4X^\varepsilon). The node is therefore a route obstruction: it proves
neither K26 nor its negation and leaves a direct literal coefficient-sensitive
endpoint theorem admissible.

The three exact direct dependencies are the proved Round-164 transport
reduction, proved Round-165 parity/gcd/scale reduction, and proved Round-172
maximal positive-transform obstruction:

1. `M9-M2-hard-top-t1-residual-transport-fejer-energy-reduction`;
2. `M9-M2-hard-top-t1-residual-fejer-parity-gcd-scale-reduction`; and
3. `M9-M2-hard-top-t1-residual-maximal-fejer-dyadic-positive-transform-obstruction`.

All three resolve and remain `proved_internal`.

## 3. Proof or derivation

### 3.1 Exact reverse reconstruction

I parsed the current graph and final patch independently. To avoid assuming
the desired delta, the inverse was reconstructed from exact append seams and
the last patches that touched the three updated records.

For every Round-175 update, the seven declared inconclusive evidence paths
are the exact terminal suffix of the current target list, in declared order.
For each of the two open endpoint owners, the new obstruction is likewise the
exact terminal dependency. The pre-Round-175 `next_action` values were read
from the last patches that set them: Round 174 for the residual Fejer
reduction and Round 173 for the two endpoint owners. Their prior metadata was
recovered from the unchanged records made by those same raw applications:

| Record | Prior round | Prior timestamp |
|---|---:|---|
| residual Fejer parity/gcd/scale reduction | 174 | `2026-08-27T00:52:12` |
| density-discrepancy-energy owner | 173 | `2026-08-26T23:36:23` |
| signed-cone owner | 173 | `2026-08-26T23:36:23` |

The inverse then performs only four operations:

1. remove the single new obligation;
2. remove the exact evidence and dependency suffixes and restore the prior
   next actions and metadata on the three updates;
3. remove the exact thirteen-record rejected-claim suffix, whose IDs occur
   in patch order; and
4. leave every no-change and unlisted record untouched.

The reconstructed object passes repository graph validation. Canonical
serialization has SHA-256 `e40c2143...bbf211`, exactly the authoritative
starting hash.

### 3.2 Exact forward readback

I then reapplied the unchanged patch only in memory to the reconstructed
starting graph with `round_index=175`, `judge_ref=None`, and the observed
timestamp frozen at `2026-08-27T02:39:54`. The repository apply result is
exactly `1/3/0/13/18`. The resulting object equals the current parsed graph,
its canonical serialization equals the current raw bytes, and its SHA-256 is
exactly `9409651...b03`.

The only changed pre-existing records and fields are:

| Record | Exact changed fields | Evidence/dependency effect | Status |
|---|---|---|---|
| residual Fejer parity/gcd/scale reduction | `evidence.inconclusive`, `next_action`, `last_updated_round`, `last_updated_at` | inconclusive 22 to 29; dependencies 1 to 1 | `proved_internal` unchanged |
| density-discrepancy-energy owner | `dependencies`, `evidence.inconclusive`, `next_action`, `last_updated_round`, `last_updated_at` | inconclusive 85 to 92; dependencies 26 to 27 | `open` unchanged |
| signed-cone owner | `dependencies`, `evidence.inconclusive`, `next_action`, `last_updated_round`, `last_updated_at` | inconclusive 103 to 110; dependencies 24 to 25 | `open` unchanged |

Each update has precisely the seven declared new inconclusive paths. The
proved reduction gains no dependency. Each open owner gains the new
obstruction once. No update changes `status`, `implies`, or `blockers`.

Each of the thirteen new rejected records has exactly four fields:
`id`, its patch-declared `reason`, `last_updated_round: 175`, and the common
application timestamp. None has an `evidence` field. They form the exact
terminal suffix of the rejected ledger, and every one of the 1,411 prior
rejected records is unchanged.

### 3.3 Edge, cycle, status, and sentinel audit

With dependency edges oriented prerequisite to dependent, the only five new
edges are

\[
 \{\mathrm{R164},\mathrm{R165},\mathrm{R172}\}
 \longrightarrow \mathrm{R175\ obstruction}
 \longrightarrow
 \{\mathrm{density},\mathrm{signed\ cone}\}.
\]

Dependency edges increase from 1,335 to 1,340. The dependency graph has
three nontrivial strongly connected components before and after, with
identical membership. Adding implication edges in source-to-consequence
direction changes total combined edges from 1,409 to 1,414; the combined
graph has four nontrivial SCCs before and after, again with identical
membership. The new node is a singleton SCC in both graphs. All dependency,
implication, and blocker references resolve before and after.

No pre-existing obligation changes status. The exact status ledger is:

| Status | Before | After |
|---|---:|---:|
| `derived_under_assumptions` | 15 | 15 |
| `diagnostic_only` | 2 | 2 |
| `open` | 33 | 33 |
| `proposed` | 7 | 7 |
| `proved_external_dependency` | 19 | 19 |
| `proved_internal` | 299 | 300 |
| obligation-status `rejected` | 2 | 2 |

The sole increase is the created obstruction. All eighteen declared
no-change obligation objects are data-identical. Exact object comparison also
confirms that `GC-target`, both bridges, M9, M9--M1, GAR, M9--M2, and
endpoint uniformity are unchanged. The internal (1/3) theorem, accepted
external (0.3144831759740614\ldots) benchmark, and open (1/4) target are
unchanged in statement and status. Top-level schema, allowed statuses,
tracks, collaboration metadata, and round selection are identical.

## 4. First doubtful or unproved step

There is no doubtful post-application mechanical step. The current raw graph
is canonical; graph and patch validation succeed; the exact reverse reaches
the starting hash; the timestamp-controlled forward application reproduces
the current bytes; every declared append seam is exact; and SCC and sentinel
checks are invariant.

The first unproved mathematical statement remains

\[
 Q_M^*\ll_\varepsilon L^3X^\varepsilon
\]

for the complete literal residual transform, equivalently K26 after the
target-safe lower endpoint, collective ordinary-zero restoration, and
once-only short correction. The applied obstruction neither proves nor
disproves it. No residual target, hard-TOP parent, smooth packet, M9 owner,
bridge, quarter theorem, or exponent is promoted.

## 5. Required controls and outcomes

| Required control | Outcome |
|---|---|
| authoritative post-apply hash | **GREEN:** exact `9409651...b03` |
| canonical current bytes | **GREEN:** raw bytes equal repository serialization |
| final patch identity | **GREEN:** exact `0c46a314...b81d2` |
| patch and graph validation | **GREEN:** zero issues |
| application mode | **GREEN:** raw, round 175, `judge_ref=None` |
| operation counts | **GREEN:** exact `1/3/0/13/18` |
| obligation/reject counts | **GREEN:** 377 to 378 and 1,411 to 1,424 |
| created record | **GREEN:** exact declaration plus round/timestamp metadata only |
| created evidence | **GREEN:** exact `18/0/0` buckets |
| update evidence | **GREEN:** seven exact fresh inconclusive paths on each target |
| update dependencies | **GREEN:** none on the proved reduction; one exact new dependency on each open owner |
| reject records | **GREEN:** thirteen exact fresh suffix records, no evidence field |
| no-change records | **GREEN:** 18/18 data-identical |
| undeclared changes | **GREEN by exact forward equality:** none |
| evidence paths | **GREEN:** 39 occurrences, 18 distinct, all resolve, no within-list duplicate |
| reference integrity | **GREEN:** all dependency, implication, and blocker IDs resolve |
| SCC scope | **GREEN:** nontrivial memberships unchanged; new node acyclic |
| existing statuses | **GREEN:** no drift |
| theorem/exponent sentinels | **GREEN:** all exact and unchanged |
| canonical inverse | **GREEN:** exact starting hash `e40c2143...bbf211` |
| graph bytes | **GREEN:** zero CR, TAB, NUL, and Unicode-replacement bytes |

No numerical mathematical experiment, web source, or external theorem was
used in this audit.

## 6. Dependencies and exact artifacts used

This audit used:

1. `protocol.md`;
2. the current authoritative `state/proof_obligations.yml`;
3. `rounds/codex-managed/m9-m2-hard-top-t1-residual-whole-chain-actual-symbol-scale-correlation-gate/state_patch.json`;
4. `proofs/kernels/m9_m2_hard_top_t1_residual_whole_chain_scale_coboundary_positive_capacity_obstruction.md`;
5. the campaign `synthesis.md` and
   `controls/conductor_round175_controls.md`;
6. the campaign `reviews/conductor_round175_adjudication.md`;
7. the campaign `reviews/final_kernel_mathematical_verification.md`;
8. the campaign `reviews/final_power_owner_scope_review.md` and
   `reviews/final_power_owner_scope_post_repair_verification.md`;
9. the campaign `reviews/state_patch_scope_cycle_review.md` and
   `controls/preapply_independent_reverse_audit.md`;
10. `rounds/codex-managed/m9-m2-hard-top-t1-residual-tangent-fejer-commutator-gate/state_patch.json`, solely to recover the last pre-Round-175 endpoint-owner next actions;
11. `rounds/codex-managed/full-proof-round171-173-strategy-literature-review/state_patch.json`, solely to recover the last pre-Round-175 residual-reduction next action; and
12. `math_collab/proof_obligations.py` for parsing, graph validation, raw
   in-memory application, and canonical serialization.

The final patch contains 39 evidence occurrences across four lists and 18
distinct evidence artifacts. All resolve in the post-application workspace.
The current graph and patch were read only. This audit wrote only the present
report and did not edit shared state, the patch, a kernel, synthesis, control,
or sibling review.

## 7. Recommended state effect

**Retain the applied graph without repair.** The exact authoritative graph
with SHA-256 `9409651dccbbd1c69547546b245ba04c21d2a280173733ae37b693f9894c8b03`
is the correct raw application of the final patch to starting graph
`e40c214351d06bf05212e25fffbec0f1a4808be21cb9098ba25823f0d9bbf211`.

The accepted effect is exactly one proved-internal route obstruction, three
declared existing-record updates with no status change, thirteen new rejected
overclaims, eighteen no-change guards, and no theorem or exponent mutation.
No graph rollback, corrective patch, evidence injection, or further
obligation mutation is recommended.

**Final verdict: GREEN.**
