# Round 180 pre-application independent reverse audit

- Campaign: `m9-m2-hard-top-t1-residual-k26-near-peak-row-gram-anticoncentration-gate`
- Round: 180
- Role: independent State Patch, graph, and exact-reversal auditor
- Graph mutation: none; application and reversal were performed only in memory

## 1. Verdict

**GREEN.** The proposed `state_patch.json` validates against the exact
frozen graph, applies cleanly in memory with Round index 180, has the exact
declared inventory

\[
 \boxed{1\ \mathrm{create}/4\ \mathrm{update}/0\
 \ \mathrm{correct\text{-}rejected}/16\ \mathrm{reject}/21\
 \ \mathrm{no\text{-}change}},
\]

and reverses exactly to the canonical starting graph

`e94ef6a364988e47f8a59ca3589f03cb098a04a241ec841afc2efa6e685081b4`.

The simulated post-patch graph passes the repository validator. The patch
introduces no dangling dependency, no new dependency, implication, or
combined proof-flow cycle, and no change to any pre-existing status,
statement, or exponent owner. The durable kernel, final review,
adjudication, synthesis, and patch agree on the narrow obstruction and on
the still-open unequal-product theorem.

## 2. Frozen graph and patch integrity

The raw SHA-256 of `state/proof_obligations.yml` is exactly

`e94ef6a364988e47f8a59ca3589f03cb098a04a241ec841afc2efa6e685081b4`,

matching `starting_graph_sha256`. Loading the graph and serializing it with
the repository's canonical serializer reproduces the original bytes and
the same hash. Thus the audit used the exact frozen graph, not merely a
semantically equivalent graph.

The official repository checks report both `Graph OK` and `Patch OK`.
Independent inventory checks found:

- one new obligation ID, absent from the 381 starting obligations;
- four distinct update IDs, all present in the graph;
- sixteen distinct rejected-claim IDs, absent from the 1,486 starting
  rejected claims and from the obligation IDs;
- twenty-one distinct no-change IDs, all present in the graph;
- no duplicate within an operation array and no ID shared by two operation
  arrays; and
- clean JSON bytes: UTF-8 without BOM, terminal LF, and no CR, TAB, FF,
  NUL, DEL, or other disallowed C0 byte.

All thirteen positive evidence paths on the created node exist. Each of
the four updates adds six existing Round-180 artifacts to
`evidence.inconclusive`; all twenty-four path occurrences exist, none was
already present in any evidence bucket of its target, and there is no
within-list duplicate. The classification is correct: the complete
reviewed kernel package is positive evidence for the proved, narrowly
scoped obstruction, whereas its attachment to the inherited reductions
and open parents is inconclusive route evidence only. The blind report is
positive only under the explicit post-unmask repair bundled in the same
evidence packet; neither the patch statement nor the reviewed synthesis
treats its abstract exact-product construction as literal mass.

## 3. Dependency direction and graph structure

The created node

`M9-M2-hard-top-t1-residual-k26-near-peak-row-gram-self-return-obstruction`

has exactly the two declared prerequisites:

1. `M9-M2-hard-top-t1-residual-whole-chain-scale-coboundary-positive-capacity-obstruction`;
2. `M9-M2-hard-top-t1-character-poisson-product-collar-obstruction`.

This direction is mathematically correct. The Round-175 whole-chain node
supplies the recombined energy, near/far endpoint framework,
ordinary-zero restoration, short-correction seam, and exact K26 endpoint
identity. The Round-162 product-collar node supplies the named central
rank-one no-repeat boundary. Neither prerequisite acquires a back edge to
the Round-180 node.

The two open parent owners

- `M9-M2-top-endpoint-density-discrepancy-energy`; and
- `M9-M2-top-endpoint-signed-cone`

gain the new obstruction as a dependency. The two proved residual nodes
receive evidence and revised next actions only, not a backwards
dependency. In normalized proof-flow direction, the new edges therefore
run

\[
 \{\text{whole-chain},\text{product-collar}\}
 \longrightarrow \text{Round-180 obstruction}
 \longrightarrow \{\text{density owner},\text{signed-cone owner}\}.
\]

Every new reference resolves. The dependency graph has three pre-existing
cyclic strongly connected components before simulation and the same three
afterward; no new component appears. The implication graph has zero before
and after. The normalized combined dependency/blocker/implication graph
has four pre-existing cyclic components before and the same four after.
Thus the patch adds no cycle in any audited orientation. It also adds no
implication or blocker edge and leaves the count of dangling dependency
references at zero.

## 4. Exact in-memory application and mutation scope

I applied the patch to a deep in-memory copy with the official
`apply_state_patch` function, `round_index=180`, and the conductor
adjudication as `judge_ref`. The returned operation lists agree exactly,
including order, with the five arrays in the patch:

| Operation | Declared | Applied in memory |
|---|---:|---:|
| `create` | 1 | 1 |
| `update` | 4 | 4 |
| `correct_rejected` | 0 | 0 |
| `reject` | 16 | 16 |
| `no_change` | 21 | 21 |

The simulated graph has 382 obligations and 1,502 rejected claims. All
sixteen reject directives append new rejected-claim records; none targets
an obligation, so no obligation is assigned rejected status.

Among the 381 pre-existing obligations, exactly four objects change:

1. the Fejer parity/gcd/scale reduction changes only
   `evidence.inconclusive`, `next_action`, `last_updated_round`, and
   `last_updated_at`;
2. the whole-chain obstruction changes only those same four fields;
3. the density/discrepancy owner changes only `dependencies`,
   `evidence.inconclusive`, `next_action`, `last_updated_round`, and
   `last_updated_at`; and
4. the signed-cone owner changes only those same five fields.

No existing `status`, `statement_tex`, `title`, `type`, `track`, owner,
promotion field, implication, or blocker changes. Every no-change object
is exactly equal to its starting version. In particular,
`GC-partial-one-third`, `GC-external-Li-Yang-theta-star`, and `GC-target`
are byte-identical as graph objects before and after simulation. The
internal exponent remains (1/3), the accepted external exponent remains
(0.3144831759740614\ldots), and the target remains (1/4).

## 5. Exact reverse reconstruction

The simulated result was reversed solely from the patch's declared
operations and inverse data:

1. remove the one created obligation;
2. remove the two added owner dependencies;
3. remove the six added inconclusive evidence values from each of the four
   updated obligations;
4. restore all four recorded `next_action` strings;
5. restore the exact prior metadata pairs:
   - Fejer reduction: Round 177 at `2026-08-27T10:20:58`;
   - whole-chain obstruction: Round 175 at `2026-08-27T02:39:54`;
   - density/discrepancy owner: Round 175 at `2026-08-27T02:39:54`;
   - signed-cone owner: Round 179 at `2026-08-27T13:28:40`; and
6. remove the sixteen newly appended rejected-claim records.

The assessment and no-change directives write no graph data and need no
inverse operation. Restoring the four metadata pairs removes every runtime
timestamp introduced by the applicator.

The reversed object is deeply equal to the initially loaded graph.
Canonical serialization is byte-for-byte equal to the original state file
and recovers SHA-256

`e94ef6a364988e47f8a59ca3589f03cb098a04a241ec841afc2efa6e685081b4`.

## 6. Mathematical and evidence boundary

The patch statement matches the durable kernel and its final GREEN review:

- the exact identity is
  \(\mathcal E_\nu=\mathcal D_\nu+\mathcal G_\nu\), with
  \(0\le\mathcal D_\nu\ll_\varepsilon LX^\varepsilon\);
- the one-sided off-row target is therefore equivalent at target strength
  to the original local scalar concentration bound;
- the exact cross-row equal-product sector has the displayed formula and
  is \(O_\varepsilon(X^\varepsilon)\);
- the complete unequal-product bound for \(\mathcal U_\nu\) remains the
  first open theorem;
- the connector from that open theorem to \(Q_M^*\) and K26 is explicitly
  conditional; and
- the \(L^2\) local and \(L^4\) endpoint capacities are nonliteral
  mechanism controls, not physical lower mass.

The adjudication and synthesis preserve the same quarantine. Nothing in
the patch promotes \(\mathcal U_\nu\), \(Q_M^*\), K26, complete hard TOP,
M9--M2, M9, either bridge, the quarter theorem, or an exponent. The new
node is correctly typed as a subordinate `proved_internal` obstruction,
has no implication edge, and is owned only by the conductor.

## 7. Recommendation

There is **no patch repair issue**. Approve the State Patch for conductor
application with `round_index=180` and the reviewed adjudication reference.
Apply no additional status, implication, blocker, theorem, bridge, or
exponent mutation.

The first remaining mathematical issue is external to this mechanical
patch: the complete literal unequal-product estimate
\(\mathcal U_\nu\ll_\varepsilon LX^\varepsilon\) remains open exactly as
the kernel, final review, adjudication, synthesis, and updated next actions
state.

### Exact artifacts and machinery used

- `state/proof_obligations.yml`;
- the Round-180 `state_patch.json`;
- `proofs/kernels/m9_m2_hard_top_t1_residual_k26_near_peak_row_gram_self_return_obstruction.md`;
- `reviews/final_kernel_mathematical_scope_review.md`;
- `reviews/conductor_round180_adjudication.md`;
- `synthesis.md`;
- `math_collab/proof_obligations.py`; and
- `math_collab/validate_state_patch.py`.

No numerical theorem experiment or external source was used.
