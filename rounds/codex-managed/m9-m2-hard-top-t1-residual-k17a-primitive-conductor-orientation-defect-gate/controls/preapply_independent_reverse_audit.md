# Pre-application independent reverse audit

## 1. Verdict

**GREEN.**  The proposed `state_patch.json` validates against the exact
starting graph, applies cleanly in memory with Round index 179, has the
declared effect

\[
\boxed{1\ \mathrm{create}/2\ \mathrm{update}/0\
\ \mathrm{correct\text{-}rejected}/14\ \mathrm{reject}/18\
\ \mathrm{no\text{-}change}},
\]

and reverses byte-for-byte to the canonical starting graph

`e04380a1965e57971bb68d8169d8a8d8e5349edb535e01b343c8b25ecdcd4e27`.

The simulated post-patch graph validates, has no dangling reference or
new directed cycle, changes no pre-existing status or theorem statement,
and leaves every exponent owner byte-identical.  No graph or shared-state
file was written or edited.

## 2. Starting graph and patch integrity

The SHA-256 of the current canonical
`state/proof_obligations.yml` is exactly

`e04380a1965e57971bb68d8169d8a8d8e5349edb535e01b343c8b25ecdcd4e27`,

matching `starting_graph_sha256` in the patch.  Parsing the graph and
serializing it with the repository's canonical serializer reproduces the
same bytes and hash.  Thus the audit did not begin from a merely
semantically equivalent or later graph.

The repository validator reports `Patch OK`.  Independent preflight
checks also found:

- no collision between the created obligation ID and the 380 starting
  obligation IDs;
- no collision between any of the 14 new rejected-claim IDs and either a
  starting obligation or one of the 1,472 starting rejected claims;
- neither the added dependency nor any added evidence value was already
  present in its target list; and
- every evidence path named by the created obligation or either update
  exists.

These noncollision checks are essential for exact reversal: removing an
`*_added` value cannot accidentally remove pre-existing graph data.

## 3. Exact in-memory application

The patch was applied only to a deep in-memory copy using the repository
`apply_state_patch` semantics with `round_index=179`.  The returned IDs,
including their order, agree exactly with the five operation arrays in
the patch:

| Operation | Declared | Applied in memory |
|---|---:|---:|
| `create` | 1 | 1 |
| `update` | 2 | 2 |
| `correct_rejected` | 0 | 0 |
| `reject` | 14 | 14 |
| `no_change` | 18 | 18 |

The simulated graph has 381 obligations and 1,486 rejected claims.  The
14 `reject` directives append 14 new rejected-claim records; none targets
an obligation, so none changes an obligation status.

Among pre-existing obligations, exactly two objects change:

1. `M9-M2-hard-top-t1-residual-k17a-primitive-alias-conductor-reduction`
   changes only `evidence.inconclusive`, `next_action`,
   `last_updated_round`, and `last_updated_at`.
2. `M9-M2-top-endpoint-signed-cone` changes only `dependencies`,
   `evidence.inconclusive`, `next_action`, `last_updated_round`, and
   `last_updated_at`.

The first update appends six inconclusive evidence paths.  The second
appends the one declared dependency and six inconclusive evidence paths.
No `status`, `statement_tex`, `implies`, `blockers`, promotion rule, or
other hidden field changes in either object.  All 18 `no_change` objects
remain exactly equal to their starting versions.

## 4. Exact reverse reconstruction

The simulated patch was reversed strictly from the recorded inverse data:

1. remove the one created obligation;
2. remove the one `dependencies_added` value;
3. remove the six `evidence_added.inconclusive` values from each updated
   obligation;
4. restore the two `next_action` strings from
   `reversibility.restore_next_action`;
5. restore the two pairs of `last_updated_round` and `last_updated_at`
   values from `reversibility.restore_metadata`; and
6. remove the 14 newly appended rejected-claim records.

The round assessment and 18 no-change directives write no graph data and
therefore need no reverse operation.  The runtime application timestamp
is fully removed by restoring the recorded metadata.

After these operations, the reversed in-memory object is exactly equal to
the initially loaded graph.  Canonical serialization gives SHA-256

`e04380a1965e57971bb68d8169d8a8d8e5349edb535e01b343c8b25ecdcd4e27`,

and its bytes equal the original state file byte-for-byte.  The reversed
graph also passes the repository validator with zero issues.

## 5. Graph, status, owner, and exponent audit

The new obligation has the single declared dependency on
`M9-M2-hard-top-t1-residual-k17a-primitive-alias-conductor-reduction`.
The open hard-TOP owner gains the single declared dependency on the new
obligation.  In normalized dependency direction, the only new chain is

\[
\text{primitive-alias reduction}
\longrightarrow
\text{primitive-conductor parity self-return}
\longrightarrow
\text{hard-TOP signed-cone owner}.
\]

No dependency, blocker, or implication reference is dangling before or
after simulation.  No new cyclic strongly connected component appears
in the dependency graph, the implication graph, or the combined
dependency/blocker/implication graph.  No implication edge is added.

The only new `proved_internal` status belongs to the newly created,
subordinate reduction.  Every pre-existing obligation retains its exact
status and statement.  In particular, the following exponent-bearing
owners are byte-identical before and after simulation:

- `GC-partial-one-third`;
- `GC-external-Li-Yang-theta-star`; and
- `GC-target`.

The patch therefore introduces no hidden promotion of (177.K34), complete
K17a, hard TOP, M9--M2, M9, either bridge, the quarter theorem, or an
exponent.  The update to the hard-TOP owner is documentary dependency,
evidence, and next-action provenance only; its open status is unchanged.

## 6. Controls and outcomes

| Control | Outcome |
|---|---|
| Starting-hash match | **PASS.** Recorded, raw-file, and canonical-object hashes are identical. |
| Canonical starting bytes | **PASS.** Canonical serialization equals the current state file byte-for-byte. |
| Official graph validation | **PASS.** Starting graph has zero issues. |
| Official patch validation | **PASS.** Validator returns `Patch OK`. |
| Operation counts and order | **PASS.** `1/2/0/14/18`, with exact ID-list agreement. |
| ID collision | **PASS.** No created or rejected ID collides with starting graph data. |
| Added-value freshness | **PASS.** Added dependency and evidence values are not pre-existing. |
| Evidence-path existence | **PASS.** No named added or created evidence artifact is missing. |
| In-memory post-graph validation | **PASS.** Zero validator issues. |
| Exact changed-field scope | **PASS.** Only the two declared updates and one created object mutate obligation data. |
| No-change directives | **PASS.** All 18 named objects remain exactly unchanged. |
| Rejected-claim scope | **PASS.** Exactly 14 records append; no obligation status is rejected. |
| Dangling references | **PASS.** None before or after. |
| Dependency/implication cycles | **PASS.** No new cyclic component; no implication edge is added. |
| Existing statuses/statements | **PASS.** No existing status or `statement_tex` changes. |
| Exponent quarantine | **PASS.** All three exponent owners remain byte-identical. |
| Reverse object equality | **PASS.** Reversed object equals the starting object exactly. |
| Reverse canonical hash | **PASS.** Exact starting SHA-256 recovered. |
| Reverse byte equality | **PASS.** Canonical reverse bytes equal the original file. |
| No state mutation | **PASS.** Application and reversal occurred only in memory. |

## 7. Exact first issue and recommendation

There is **no patch repair issue**.  The first remaining mathematical
issue is external to this mechanical patch: the literal centered defect
(179.K19), equivalently (177.K34) after safe terms, remains open exactly
as the new node and updated next actions state.

Operationally, application should use the repository validator/applicator
with `round_index=179`; otherwise the optional helper would not stamp the
intended Round-179 metadata on the created and updated records.  This is
an application precondition, not a defect in the reviewed patch.

Recommendation: **approve the State Patch for conductor application**.
Apply no additional status, dependency, implication, blocker, bridge,
theorem, or exponent mutation.  This reviewer made no graph or shared-
state edit; the only written artifact is this control report.

### Exact artifacts and machinery used

- `state/proof_obligations.yml`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-primitive-conductor-orientation-defect-gate/state_patch.json`;
- `math_collab/proof_obligations.py`; and
- `math_collab/validate_state_patch.py`.

No numerical theorem experiment or external source was used.
