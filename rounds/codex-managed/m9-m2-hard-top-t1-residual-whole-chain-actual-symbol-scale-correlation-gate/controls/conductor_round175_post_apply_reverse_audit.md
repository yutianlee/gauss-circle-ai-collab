# Round 175 conductor post-application reverse audit

- Campaign: `m9-m2-hard-top-t1-residual-whole-chain-actual-symbol-scale-correlation-gate`
- Starting graph: `e40c214351d06bf05212e25fffbec0f1a4808be21cb9098ba25823f0d9bbf211`
- Applied graph: `9409651dccbbd1c69547546b245ba04c21d2a280173733ae37b693f9894c8b03`
- State-Patch SHA-256: `0c46a31499e6a9f93a972c50e1b60a5911301987c53caed3142bd44e424b81d2`
- Application mode: raw patch, Round 175, `judge_ref=None`
- Verdict: **GREEN**

## 1. Result

The authoritative graph is the exact canonical result of the reviewed raw
State Patch. The observed operation counts are
`1 create / 3 update / 0 correct-rejected / 13 reject / 18 no-change`.
There are 378 obligations and 1,424 rejected-claim records. Graph validation
passes with no issue.

The independent post-application review reconstructs the starting graph,
reapplies the patch with the observed application timestamp, and obtains
exact two-way byte and hash equality. No undeclared graph mutation remains.

## 2. Exact applied statement and hypotheses

The sole created node is
`M9-M2-hard-top-t1-residual-whole-chain-scale-coboundary-positive-capacity-obstruction`.
It is a `proved_internal` obstruction with three proved dependencies, no
implication, no blocker, and evidence buckets of exact sizes `18/0/0`.

The proved residual Fejer parity/gcd/scale reduction receives seven
inconclusive paths and a revised next action only. Each of the two open
endpoint owners receives the new obstruction once as a dependency, seven
inconclusive paths, and a revised next action. All three pre-existing
statuses are unchanged.

## 3. Exact forward and reverse derivation

The raw application timestamp is `2026-08-27T02:39:54`. The only five new
dependency edges are

\[
 \{\mathrm{R164},\mathrm{R165},\mathrm{R172}\}
 \longrightarrow \mathrm{R175\ obstruction}
 \longrightarrow \{\mathrm{density},\mathrm{signed\ cone}\}.
\]

The new node is acyclic. Dependency-only and dependency-plus-implication
strongly connected component memberships are unchanged.

For the exact inverse, remove the new node; remove the seven evidence paths
and two owner dependencies; restore the Round-174 residual-reduction action
and metadata and the Round-173 endpoint-owner actions and metadata; and
remove the thirteen terminal rejected records. Canonical serialization is
then exactly

`e40c214351d06bf05212e25fffbec0f1a4808be21cb9098ba25823f0d9bbf211`.

Reapplying the unchanged patch in memory with `judge_ref=None` and the
observed timestamp reproduces the current bytes and
`9409651dccbbd1c69547546b245ba04c21d2a280173733ae37b693f9894c8b03`.

## 4. First doubtful or unproved step

No mechanical application or reversal step is doubtful. The first unproved
mathematical statement remains

\[
 Q_M^*\ll_\varepsilon L^3X^\varepsilon,
\]

equivalently K26 after the target-safe lower endpoint, collective
ordinary-zero restoration, and once-only short correction. The applied
obstruction proves neither this estimate nor its negation.

## 5. Controls and outcomes

- Patch and graph validation: GREEN.
- Current graph canonical bytes and hash: GREEN.
- Exact operation and record counts: GREEN.
- Created evidence `18/0/0`: GREEN.
- Three update fields and seven-path evidence additions: GREEN.
- Thirteen rejected records without automatic evidence: GREEN.
- Eighteen no-change records and all unlisted records: unchanged.
- Evidence paths: 39 occurrences, 18 distinct, all resolve.
- Dependency, implication, blocker, SCC, and status scope: GREEN.
- M9--M1, M9--M2, endpoint uniformity, M9, both bridges, theorem, and
  exponent sentinels: unchanged.
- Exact canonical reverse and timestamp-controlled forward readback: GREEN.

## 6. Dependencies and exact artifacts used

The decisive independent audit is
`reviews/postapply_graph_scope_verification.md`. It uses the authoritative
graph, final patch, durable kernel, synthesis, conductor controls and
adjudication, all final reviews, the Round-173 and Round-174 predecessor
patches for exact inverse metadata, and the repository graph implementation.
No numerical theorem evidence or external source is used.

## 7. Recommended state effect

Retain the applied graph without repair. Close Round 175 under
`whole_chain_actual_symbol_capacity_or_self_return_no_go`. Promote no target,
parent, bridge, theorem, or exponent.
