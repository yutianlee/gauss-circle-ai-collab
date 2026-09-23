# Round 184 pre-application State Patch reverse audit

- Campaign: `m9-m1-hard-top-t1-comparable-factor-exchange-gate`
- Round: `184`
- Role: independent patch, evidence, graph, scope, cycle, and reverse auditor
- Frozen starting graph SHA-256:
  `a8e0e5d84c0c5047e0c96f11128dd215ae035bdd4355bd68ad28dc87afe6cfbd`
- Audited State Patch SHA-256:
  `25cbb1cdb2243ab1d16f1613551102e3df2b7ffb55fc3a336e061cfd4e9cb8ec`
- Candidate SHA-256:
  `c514b10bed4c673618179c158258c362373696730c691900d250ed43e379e97f`
- Repaired durable-kernel SHA-256:
  `3387615b5522deeb4c63021fbdf4a665afa2c405052f2ff0868bed40338e602f`

## 1. Result: GREEN

**Verdict: GREEN.**

The exact on-disk State Patch is schema-valid, evidence-complete,
scope-tight, cycle-neutral, and exactly reversible.  Its operation
inventory is exactly:

| operation | count | simulated result |
|---|---:|---|
| create | 1 | one subordinate `proved_internal` strict-sector node |
| update | 1 | the open complete small-\(t\) owner only |
| correct rejected | 0 | none |
| append rejected-overclaim record | 15 | fifteen new, distinct IDs with nonempty reasons |
| record no change | 27 | all IDs exist and remain deeply equal |

The simulation changes no inherited status or statement.  It adds only
the declared prerequisite, inconclusive evidence, next action, and
generated metadata to the one open owner; creates exactly the declared
strict-sector node; and appends exactly fifteen rejected-claim records.
There is no implication or blocker mutation, dangling reference, new
cyclic strongly connected component, parent promotion, bridge change,
theorem change, or exponent change.

## 2. Exact statement and application hypotheses

This verdict applies only to the audited patch applied to the exact
frozen graph with `round_index=184` and **no `judge_ref`**.  Supplying a
`judge_ref` would make the official applicator add extra evidence and
would fall outside this exact reverse audit.

The created node is
`M9-M1-hard-top-t1-comparable-factor-exchange-sector`.  It fixes real
\(X\ge2\), one literal middle or lower residual hard-M1 shell \(L\),
both signs, and fixed \(\kappa>0\).  On the exact coprime-squarefree
\(t=1\) face it selects, allocation-independently from
\((N,L,\kappa)\), at most one close pair of distinct odd primes with
opposite \(\chi_4\)-product.  It proves only

\[
 |\mathcal T^{\rm cp}_{L,X,\sigma}|
 \ll_{\kappa,\varepsilon}L^{3/2}X^\varepsilon
\]

for the selected-product XOR allocations.  Its statement preserves the
exact exchange invariants, the repaired \(\tau_N\)-closed active support,
the literal M1 smooth/BV/collar proof, the exact no-pair plus neither/both
residual, and the sufficient but unproved one-outer-real-part Fejer
correlation at \(R=\lceil L\rceil\).  It expressly permits an everywhere
empty selector and denies density, complete-\(t=1\), complete-small-\(t\),
parent, bridge, theorem, or exponent consequences.

The created statement is semantically exact against the repaired
candidate, durable kernel, adjudication, and synthesis.  Its seven direct
dependencies match the candidate and repaired kernel exactly, in the
same order:

1. `M9-M1-hard-top-squarefree-radical-sector-reduction`;
2. `M9-M1-hard-top-small-t-nonresonant-primitive-ray-sector`;
3. `M9-M1-top-endpoint-transform`;
4. `M9-M1-frequency-phase-diagram-R10`;
5. `H4-Phi-regularity`;
6. `M9-M2-dyadic-weight-nondegeneracy`; and
7. `Divisor-bound-elementary`.

All seven IDs exist before application and have status
`proved_internal`.  The created node has empty `implies` and `blockers`
arrays.

## 3. Proof and exact derivation

### 3.1 Hash, parser, operation, and evidence audit

The starting graph has 386 obligations and 1,544 rejected-claim records.
Its 1,988,063 raw bytes are byte-identical to
`dump_graph(load_graph(...))`; both raw and canonical SHA-256 are

`a8e0e5d84c0c5047e0c96f11128dd215ae035bdd4355bd68ad28dc87afe6cfbd`,

exactly the hash declared by the patch and Round-184 artifacts.  The
official dry validator returns `Patch OK`.  Independent validation finds
zero issue in the starting graph, the patch against that graph, or the
simulated post-state.

The created ID is absent from both inherited obligations and rejected
claims.  The update ID exists.  All fifteen rejection IDs are absent
from both namespaces, mutually distinct, and have nonempty reasons.  All
twenty-seven no-change IDs exist.  There is no duplicate ID,
cross-operation overlap, or operation-order discrepancy.

The patch contains 32 evidence-path occurrences representing 16 distinct
files.  Every path exists, strict UTF-8 decoding succeeds, and the update
adds no path already present in the owner's target bucket.  The same
sixteen-file package is classified:

- `positive` for the created strict sector, because it contains the
  candidate and repaired kernel, the direct and blind derivations, the
  hostile transfer/scope controls, the repair-and-verification chains,
  final seam reviews, reconciliation, adjudication, and synthesis; and
- `inconclusive` for the complete small-\(t\) owner, because the package
  leaves the exact residual, every \(t\ge2\) small-\(G\) incidence, and
  the large-\(G\) near-resonant complement open.

Those classifications are defensible.  The two `REPAIR` reviews are
paired with exact GREEN post-repair verifications.  The mathematical
final reviews at the earlier kernel hash remain valid because the only
later kernel change restored one dependency ledger entry; the formal
provenance review and its GREEN post-repair verification pin the current
kernel and supersede earlier dependency commentary.  The M2 transfer
audit is positive control evidence for the node's direct-M1 proof and
no-transfer scope, not a claimed M2 theorem dependency.

### 3.2 Exact simulated object delta

At frozen application time, official in-memory application produces 387
obligations and 1,559 rejected-claim records.  The inherited-object delta
is exhausted by
`M9-M1-hard-top-high-radical-small-t-residual-estimate`.  Exactly these
five fields change:

1. `dependencies`: append the created strict-sector ID;
2. `evidence`: append the sixteen paths to `inconclusive`;
3. `next_action`: replace it by the exact residual-focused action in the
   patch;
4. `last_updated_round`: set to 184; and
5. `last_updated_at`: set by the applicator.

Its `id`, type, track, title, status `open`, `statement_tex`, `implies`,
`blockers`, and owner remain exact.  Every other inherited obligation is
deeply equal.  In particular, all twenty-seven declared no-change objects
remain deeply equal, and the existing rejected-claim prefix is unchanged.
The created object equals the patch entry plus only the generated round
and time metadata.  The fifteen appended rejection records equal their
declared IDs and reasons plus only that metadata, in declared order.

The edge and cycle delta is:

| relation | edges before | edges after | added | removed | dangling before/after | cyclic SCCs before/after |
|---|---:|---:|---:|---:|---:|---:|
| dependencies | 1,368 | 1,376 | 8 | 0 | 0 / 0 | 3 / 3 |
| implications | 326 | 326 | 0 | 0 | 0 / 0 | 0 / 0 |
| blockers | 70 | 70 | 0 | 0 | 0 / 0 | 0 / 0 |
| normalized combined proof flow | 1,480 | 1,488 | 8 | 0 | 0 / 0 | 4 / 4 |

Here combined flow orients dependencies and blockers from owner to
prerequisite and reverses `implies` into the same owner-to-prerequisite
direction.  The cyclic SCC sets themselves, not merely their counts, are
identical before and after simulation.  The eight dependency edges are
exactly the new node's seven accepted prerequisites plus the open owner's
one new prerequisite.  No implication points from the proper sector to a
complete owner.

### 3.3 Parent, bridge, theorem, and exponent quarantine

The complete small-\(t\) owner remains `open` with unchanged statement and
implication edge.  The hard signed cone, independent smooth M1 parent,
GAR, M9-M1, all M2 hard/smooth parents, M9-M2, endpoint uniformity, and M9
are deeply unchanged.  The conditional bridge and alternative bridge
remain `derived_under_assumptions` and deeply unchanged.

The exponent objects are also deeply unchanged:

- `GC-partial-one-third` remains `proved_internal` at \(1/3\);
- `GC-external-Li-Yang-theta-star` remains
  `proved_external_dependency` at
  \(0.3144831759740614\ldots\); and
- `GC-target` remains `open` at \(1/4\).

The fifteen rejection records accurately quarantine the audited
coverage, density, ambient-balance, M2-transfer, unrestricted-BV,
one-prime-toggle, involution-average, Abel/BV, shiftwise-triangle, open
correlation, lower-mass, complete-owner, complete-\(t=1\), and exponent
overclaims.  They create no proof-obligation status or edge.

### 3.4 Exact inverse and frozen-time replay

The declared restore next action and restore metadata are byte-for-byte
equal to the corresponding fields in the frozen graph, and the added
dependency and evidence values are absent before application.  The exact
inverse was executed in memory by:

1. removing the one created obligation;
2. removing its one dependency and sixteen inconclusive evidence paths
   from the updated owner;
3. restoring the recorded owner next action and round/time metadata; and
4. removing the fifteen patch-created rejected-claim records.

The reversed graph validates, is deeply equal to the frozen graph,
serializes byte-for-byte to the original `proof_obligations.yml`, and
recovers the exact starting SHA-256.

For replay, the official applicator was frozen at
`2026-08-27T22:25:38`, with round 184 and no `judge_ref`.  The audit-only
post-state hash is

`1d9f1d714f5b643cc2df8fa553e64dfbfa2b3501a1f8259e648878b214584777`.

Reverse followed by reapplication at that same frozen time reproduces
the exact post-state object, canonical bytes, operation-result arrays and
order, and post-state hash.  The post hash is timestamp-dependent; a real
application must receive its own post-application reverse audit.

## 4. First doubtful or unproved step

No doubtful step remains in patch parsing, starting hash, operation
inventory, ID ownership, evidence existence or classification, statement
and dependency parity, inherited-field delta, no-change equality, graph
validity, dangling-reference control, SCC comparison, scope quarantine,
exact inverse, or frozen replay.  **First mechanical defect: none.**

The first unproved mathematical step remains (K184.7), the exact
one-outer-real-part residual correlation at \(R=\lceil L\rceil\), or an
equivalent direct target estimate for all no-pair plus neither/both
allocations.  The patch records this as open and does not promote the
complete \(t=1\) face or complete small-\(t\) owner.

## 5. Required control tests and outcomes

| control | outcome |
|---|---|
| starting raw/canonical hash | **PASS.** Raw bytes equal canonical dump; both hash to exact `a8e0e5d...`. |
| patch JSON/hash and official dry validation | **PASS.** Exact `25cbb1cd...`; validator returns `Patch OK`. |
| operation inventory | **PASS.** Exact `1/1/0/15/27`, with unique, nonoverlapping IDs and preserved order. |
| created statement and status | **PASS.** Exact subordinate, possibly empty, strict XOR sector; `proved_internal`; no `implies` or blocker. |
| seven dependencies | **PASS.** Candidate, repaired kernel, and patch lists are identical; all seven inputs exist and are `proved_internal`. |
| evidence paths and novelty | **PASS.** 32 occurrences, 16 distinct files, zero missing, zero nonnovel owner additions. |
| evidence classification and repair history | **PASS.** Strict-sector positive; complete-owner inconclusive; bounded repairs have GREEN verifications. |
| rejected records | **PASS.** Fifteen new, distinct records with nonempty, scope-correct reasons. |
| no-change decisions | **PASS.** All 27 IDs exist and remain deeply equal after simulation. |
| inherited status/statement/edge drift | **PASS.** None; only the five authorized owner fields change. |
| dangling references | **PASS.** Zero before and after. |
| dependency/implication/blocker/combined cycles | **PASS.** SCC membership sets are unchanged. |
| parent, bridge, theorem, exponent quarantine | **PASS.** All protected objects remain deeply equal. |
| declared restore fields | **PASS.** Exact frozen next action and metadata are recorded. |
| exact inverse object/bytes/hash | **PASS.** Byte-identical starting graph and exact starting SHA recovered. |
| frozen-time apply/reverse/reapply | **PASS.** Exact object, bytes, operation arrays/order, and post hash reproduced. |
| authoritative-state mutation by this audit | **PASS.** None. |

All machine work was bounded hashing, parsing, path, graph, SCC, and exact
reversal control.  No computation was used as theorem evidence.

## 6. Dependencies and exact artifacts used

This audit used:

1. `protocol.md`;
2. `state/proof_obligations.yml`;
3. `state/active_campaign.yml`;
4. `rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/state_patch.json`;
5. `rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/candidates/formalized_hard_m1_t1_comparable_factor_exchange_sector.md`;
6. `proofs/kernels/m9_m1_hard_top_t1_comparable_factor_exchange_sector_and_residual_fejer_reduction.md`;
7. `rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/reviews/conductor_round184_adjudication.md`;
8. `rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/synthesis.md`;
9. the Round-184 reports, reconciliation, seam reviews, and final reviews
   named in the patch's sixteen-path evidence package; and
10. `math_collab/proof_obligations.py` and
    `math_collab/validate_state_patch.py`.

The final-review chain specifically includes the literal/candidate,
power/owner/scope, formalization/provenance, and formalization
post-repair reviews.  No graph, patch, candidate, kernel, synthesis,
validation matrix, lifecycle file, or shared artifact was edited.

## 7. Recommended state effect

Approve application of the exact audited patch to the exact frozen graph,
with `round_index=184` and no `judge_ref`, followed by an independent
post-application graph and exact-reverse audit.

The only authorized promotion is the subordinate `proved_internal`
hard-M1 \(t=1\) canonical comparable-prime XOR incidence sector.  The
only inherited owner change is its new prerequisite, inconclusive
evidence, and residual-focused next action.  Keep the exact residual,
complete \(t=1\) face, all \(t\ge2\) and near-resonant incidences,
complete small-\(t\) owner, hard and smooth M1 parents, GAR, M9-M1, every
M2 owner, endpoint uniformity, M9, both bridges, the Gauss-circle target,
and all certified exponents unchanged.

**Final verdict: GREEN.  Authorized effect:
`strict_hard_m1_t1_comparable_factor_sector`.**
