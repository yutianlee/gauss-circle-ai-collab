# Round 176 post-application graph verification

## 1. Result

\[
\boxed{\mathbf{GREEN}}
\]

The actually applied canonical graph is exactly the Round-176 State Patch
image of the declared starting graph.  Its raw and canonical SHA-256 is

`e3927f0ace0f3d74e9e9f5116a319159e3508838c7f7bd14b086fa851cad82b8`.

The patch effect is exactly
`1 create / 3 update / 0 correct-rejected / 16 reject / 18 no-change`.
The current graph contains 379 obligations and
1,440 rejected-claim records.  There is no patch-local cycle, dangling
reference, hidden exponent implication, parent promotion, or unrecorded
Round-176 mutation.  Exact canonical inversion recovers the declared
starting hash

`9409651dccbbd1c69547546b245ba04c21d2a280173733ae37b693f9894c8b03`.

No repair is required.

## 2. Exact statement and hypotheses

Let \(G_1\) be the current byte-for-byte contents of
`state/proof_obligations.yml`, and let \(P_{176}\) be the current campaign
`state_patch.json`.  The verification uses the repository's canonical
serialization `json.dumps(G, indent=2, ensure_ascii=True) + "\n"`.

The raw bytes of \(G_1\) equal \(\operatorname{dump}(G_1)\).  The patch and
active manifest both declare the same starting hash above, and the patch
contains exact preimages for all three replaced `next_action` values and
their six last-update metadata fields.

Under these hypotheses, the claim checked is that applying \(P_{176}\)
once at round 176 to its reconstructed preimage \(G_0\) yields exactly
\(G_1\), while the declared inverse yields exactly the canonical bytes of
\(G_0\).

## 3. Proof and derivation

### Exact operation and state ledger

Direct parsing gives:

| Item | Starting graph | Applied graph | Exact change |
|---|---:|---:|---:|
| Proof obligations | 378 | 379 | +1 |
| Rejected claims | 1,424 | 1,440 | +16 |
| `proved_internal` obligations | 300 | 301 | +1 |
| `open` obligations | 33 | 33 | 0 |

Every other status count is also unchanged.  The complete current status
ledger is 15 `derived_under_assumptions`, 2 `diagnostic_only`, 33 `open`,
7 `proposed`, 19 `proved_external_dependency`, 301 `proved_internal`, and
2 `rejected`.

Exactly four obligations have `last_updated_round: 176`: the created node
and the three named update targets.  Exactly sixteen rejected claims have
that round stamp.  All twenty records have timestamp
`2026-08-27T08:20:19`.  No other obligation or rejected claim carries a
Round-176 mutation.

### Created node

After removing only the automatically applied `last_updated_round` and
`last_updated_at` fields, the current node

`M9-M2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-reduction`

is object-identical to the patch's create record.  In particular:

- its status is `proved_internal`, type is `reduction`, track is
  `M9_analytic`, and owner is `Codex conductor`;
- its sole dependency is
  `M9-M2-hard-top-t1-residual-determinant-endpoint-polylog-shift-reduction`;
- its `implies` and `blockers` lists are both empty;
- its statement is exactly the patch statement: the two-orientation
  multiplicity-one cross-gcd fibre, fibre-stable original gcd, sawtooth
  Fourier identities, fixed-\(\delta\) strict sector, and route-scoped
  positive-recombination no-go are proved, while full K17a and all parents
  remain open;
- its evidence ledger is exactly 15 positive, 0 negative, and 0
  inconclusive paths, with 15 unique paths and no missing file; and
- its next action is string-identical to the patch: retain
  \(\kappa_*\geq\delta L\) for fixed \(\delta\), and on
  \(\kappa_*<\delta L\) prove the literal selector-aware signed joint
  inverse-residue estimate (176.K35), including the near-half alias and the
  full literal amplitude before absolute recombination.

### Three updates

| Updated node | Current status | Exact applied effect |
|---|---|---|
| `M9-M2-hard-top-t1-residual-determinant-endpoint-polylog-shift-reduction` | `proved_internal` | Five specified inconclusive evidence paths occur exactly once; the next action is string-identical to the patch and routes only the remaining K17a complement to (176.K35). |
| `M9-M2-hard-top-t1-residual-fejer-parity-gcd-scale-reduction` | `proved_internal` | The same five paths occur exactly once; the exact next action keeps K17a's complement and the complete K26 endpoint theorem open. |
| `M9-M2-top-endpoint-signed-cone` | `open` | The new reduction occurs exactly once as an added dependency, the same five paths occur exactly once as inconclusive evidence, and the exact next action retains the complete hard-TOP owner. |

All three retain owner `Codex conductor`; none receives a status or
implication edit.  All sixteen rejected-claim ids are present exactly once,
their reasons are string-identical to the patch, and their only fields are
the expected id, reason, and Round-176 timestamp metadata.  All eighteen
no-change ids exist and receive no mutation.

### Exact forward and inverse check

In memory, I inverted \(G_1\) exactly as declared: delete the one created
obligation and sixteen appended rejected claims; remove the one added
dependency and all fifteen field-level evidence additions; restore the
three previous next actions; and restore the six previous metadata values.
Canonical serialization of the result has SHA-256

`9409651dccbbd1c69547546b245ba04c21d2a280173733ae37b693f9894c8b03`.

Applying the repository patch routine to that reconstructed object at
round 176, and setting the recorded application timestamp, returns an
object exactly equal to the current graph.  The repository graph validator
also reports `Graph OK` with no schema or reference issue.

## 4. First doubtful or unproved step

There is no doubtful patch-local or post-application graph step.  The first
unproved mathematical step remains exactly (176.K35): a literal
selector-aware signed joint inverse-residue estimate on
\(\kappa_*<\delta L\), uniform in the large near-half Fourier alias, both
orientations, all determinants, squarefree/Möbius openings, Fejer weight,
hard endpoints, displacement conditions, and zero extension before
absolute recombination.

The current graph is not globally acyclic.  That is inherited graph debt,
not a Round-176 effect, as detailed next.

## 5. Required control test and outcome

The dependency-only SCC audit finds the same three two-node components
before and after application:

1. `M9-M2-hard-top-product-fibre-transform-self-return` and
   `M9-M2-hard-top-product-fibre-mean-obstruction`;
2. `M9-M1-lower-far-cone-microscopic-cell-reduction` and
   `M9-M1-lower-post-collar-smoothed-far-alias-reduction`; and
3. `M9-M1-lower-incomplete-fibre-dispersion-obstruction` and
   `M9-M1-lower-height-alias-rank-one-product-fibre-obstruction`.

After normalizing each implication \(A\Rightarrow B\) as the prerequisite
edge \(B\to A\), both graphs have the same one additional inherited SCC:
`M9-M2-LFM-endpoint-degeneracy` with `M9-endpoint-uniformity`.  The complete
before/after SCC multisets are identical under both conventions.  Thus the
patch-local cycle delta is zero.

The created node's raw implication reachability set is empty.  The patch
adds no implication field anywhere.  The signed-cone owner's pre-existing
implication chain toward the physical assembly, M9--M2, M9, the standard
bridge, and the target is unchanged, and that owner remains `open`.
M9--M2, M9--M1/GAR, endpoint uniformity, M9, both bridges, and `GC-target`
retain their pre-Round-176 timestamps and statuses.  `GC-partial-one-third`
remains `proved_internal`, and `GC-external-Li-Yang-theta-star` remains
`proved_external_dependency`; neither has an implication or Round-176
edit.

**Control outcome: PASS.**  The controls and the earlier scope/cycle review
match the actually applied graph.  The four inherited SCCs should remain
recorded as separate global graph debt, but they provide no reason to undo
or downgrade this patch.

## 6. Dependencies and exact artifacts used

This verification used:

- `protocol.md`;
- `state/active_campaign.yml`;
- the actually applied `state/proof_obligations.yml`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-gate/briefs/post_apply_graph_verification.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-gate/state_patch.json`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-gate/controls/conductor_round176_controls.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-gate/reviews/state_patch_scope_cycle_review.md`; and
- `math_collab/proof_obligations.py` and
  `math_collab/validate_state_patch.py` for the canonical serializer,
  application semantics, and validator.

All checks were deterministic, read-only graph computations.  No external
source or numerical theorem evidence was used, and no file other than this
assigned review was edited.

## 7. Recommended state effect

**Retain the applied graph without repair.**  Accept the one subordinate
proved-internal reduction, three status-preserving updates, sixteen
rejected-claim records, and eighteen no-change decisions as the exact
Round-176 effect.  Keep (176.K35), the low-cross-gcd complement, full K17a,
K26, every hard-TOP and physical parent, M9--M2, M9--M1/GAR, endpoint
uniformity, M9, both bridges, the quarter target, and both exponent records
unchanged.  Track the inherited SCC debt separately from Round 176.
