# Round 172 independent State Patch reverse audit

- Campaign: `m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate`
- Round: 172
- Role: independent mechanical, graph, downstream-scope, and reverse auditor
- Starting graph SHA-256: `c98f95b6b3500d0f48365af338e543f9a0f251b22062f3898df5f448d6b54853`
- Patch SHA-256: `704d51393ee78d6d0edf27cbb143aea3c0d3f6fd08643b07d4112ec149b020f1`
- Verdict: **GREEN**

## 1. Result

The proposed Round-172 State Patch is mechanically valid, graph-safe, and
semantically confined to the reviewed residual maximal parity--Fejer route.
An in-memory application creates exactly one proof-obligation node and changes
exactly the two declared pre-existing open owner records.  It also appends the
eighteen declared fresh rejected-claim records; those are not obligation
updates.  The twenty `no_change` entries cause no mutation.

No pre-existing obligation changes status.  No theorem record changes.  In
particular, the internal exponent remains $1/3$, the accepted repaired
external Li--Yang exponent remains
$0.3144831759740614\ldots$, and the quarter target remains open.

The patch was never applied to `state/proof_obligations.yml`.  Applying it to a
deep in-memory copy leaves the input object unchanged.  Reversing the in-memory
create, the two updates, and the eighteen rejected-claim additions by exact
pre-patch snapshots reproduces the source graph exactly.  The authoritative
file hash before and after all tests is identical to the starting hash above.

## 2. Exact statement and hypotheses audited

The sole fresh obligation is

`M9-M2-hard-top-t1-residual-maximal-fejer-dyadic-positive-transform-obstruction`.

It is an `obstruction` with status `proved_internal`.  Its two and only direct
dependencies are

1. `M9-M2-hard-top-t1-residual-fejer-parity-gcd-scale-reduction`; and
2. `M9-M2-hard-top-t1-character-poisson-product-collar-obstruction`.

Both exist and have status `proved_internal`.  Their transitive prerequisite
closure has twenty-two nodes: twenty are `proved_internal` and two are
`proved_external_dependency` (`H4` and `H4-source-audit`).  No open, proposed,
blocked, diagnostic, rejected, or missing prerequisite occurs.  The fresh node
has `implies: []` and `blockers: []`.

The statement agrees with the repaired durable kernel.  It retains the literal
residual sequence and exact parity--Fejer stopped chain, makes the ordinary-zero
estimate collective in all odd character frequencies, leaves the complete
signed nonzero-frequency aggregate open, and restricts the no-go to a
coefficient-uniform positive closure before a proved actual-symbol gain.  It
expressly preserves cross-link cancellation and a coefficient-sensitive
literal positive theorem as possible continuations.  The $MD_L/8\asymp L^4$
sharpness family is identified as nonliteral and is not promoted to physical
lower mass.

The two and only update targets are

- `M9-M2-top-endpoint-density-discrepancy-energy`; and
- `M9-M2-top-endpoint-signed-cone`.

Both are `open` before and after the in-memory application.  Each receives
exactly one new dependency, namely the fresh obstruction, together with the
declared inconclusive evidence and revised route-specific next action.  No
dependency is removed and no implication edge is added.

## 3. Mechanical derivation and reverse comparison

The following read-only command established the source and patch identities:

```powershell
Get-FileHash -Algorithm SHA256 state/proof_obligations.yml
Get-FileHash -Algorithm SHA256 rounds/codex-managed/m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate/state_patch.json
```

The repository dry validator was then run without `--apply`:

```powershell
python -m math_collab.validate_state_patch --graph state/proof_obligations.yml --patch rounds/codex-managed/m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate/state_patch.json
```

It returned `Patch OK`.  Direct calls to `validate_graph` and
`validate_patch_against_graph` likewise returned empty issue lists before the
application, and `validate_graph` returned an empty issue list on the patched
in-memory copy.

The source graph contains 375 obligations and 1,371 rejected claims.  The
in-memory result contains 376 obligations and 1,389 rejected claims.  Exact
record comparison gives:

- created obligations: exactly the one declared obstruction;
- changed pre-existing obligations: exactly the two declared open owners;
- removed obligations: none;
- fresh rejected claims: exactly the eighteen declared IDs;
- changed pre-existing rejected claims: none; and
- pre-existing obligation status changes: none.

All operation IDs are unique.  The create ID is fresh, both update IDs exist,
all eighteen rejected-claim IDs are fresh relative to obligations and the
existing rejected ledger, and all twenty `no_change` IDs resolve.  All
dependency and implication references resolve after the in-memory patch.  The
twenty-nine evidence-path occurrences in the create and updates represent
seventeen distinct files, all of which exist.

For the reverse control, the in-memory result was deep-copied, the fresh node
and fresh rejected claims were removed, and the two changed owners were
restored from exact pre-application snapshots.  The reversed object is exactly
equal to the original graph, including order and metadata.  A fresh byte read
of the authoritative file remained identical to the initial byte string and
retained SHA-256
`c98f95b6b3500d0f48365af338e543f9a0f251b22062f3898df5f448d6b54853`.

## 4. Cycle and downstream-scope audit

With dependency edges oriented prerequisite-to-dependent, the dependency graph
has three pre-existing cyclic strongly connected components, each of size two,
both before and after the in-memory application:

1. `M9-M1-lower-far-cone-microscopic-cell-reduction` with
   `M9-M1-lower-post-collar-smoothed-far-alias-reduction`;
2. `M9-M1-lower-height-alias-rank-one-product-fibre-obstruction` with
   `M9-M1-lower-incomplete-fibre-dispersion-obstruction`; and
3. `M9-M2-hard-top-product-fibre-mean-obstruction` with
   `M9-M2-hard-top-product-fibre-transform-self-return`.

Adding implication edges in their logical source-to-consequence orientation
gives four pre-existing two-node cyclic components before the patch and the
identical four afterward; the additional one is
`M9-M2-LFM-endpoint-degeneracy` with `M9-endpoint-uniformity`.  The fresh node
belongs to no cyclic component.  Thus the patch introduces no dependency or
combined semantic cycle.

Exact record identity checks show that `GC-target`, `Conditional-bridge`,
`GC-global-M1-alternative-bridge`, `M9`, `M9-M1`, `M9-M2`,
`GC-partial-one-third`, and `GC-external-Li-Yang-theta-star` are unchanged.
Every pre-existing record of type `theorem` is unchanged.  The patch therefore
closes no residual target, hard-TOP parent, BAL or UNBAL parent, M9--M2,
M9--M1/GAR, endpoint assembly, M9, bridge, theorem, or exponent.

## 5. First doubtful or unproved step

There is no unresolved State Patch, graph, cycle, reverse, or downstream-scope
seam.  The first unproved affirmative analytic step remains a target-strength
estimate for the complete literal signed nonzero ordinary-frequency aggregate,
either linkwise or after the complete stopped-chain sum, before taking a
positive norm over modes, cells, arithmetic openings, endpoints, transitions,
or common frequency.  Round 172 neither proves nor disproves that estimate or
(165.K26).

## 6. Required controls and outcomes

| Control | Outcome |
|---|---|
| Starting graph identity | **GREEN.** Exact SHA-256 is `c98f95b6b3500d0f48365af338e543f9a0f251b22062f3898df5f448d6b54853`. |
| Standard dry validator | **GREEN.** `Patch OK`; no application flag was used. |
| In-memory graph validation | **GREEN.** Zero issues before and after. |
| Exact obligation delta | **GREEN.** One create, two declared open-owner updates, no removal, no other pre-existing mutation. |
| Rejected and no-change operations | **GREEN.** Eighteen fresh rejected records; twenty provenance-only no-change entries. |
| Direct and transitive prerequisites | **GREEN.** Two direct proved dependencies; all twenty-two transitive prerequisites have accepted proof statuses. |
| ID and reference integrity | **GREEN.** All IDs are unique where required; no missing dependency or implication target. |
| Evidence paths | **GREEN.** Seventeen distinct referenced files, all present. |
| Dependency cycles | **GREEN.** Three pre-existing components remain identical; none is added. |
| Combined logical cycles | **GREEN.** Four pre-existing components remain identical; none is added. |
| Owner statuses | **GREEN.** Both updated owners remain `open`; no pre-existing status changes. |
| Theorem and exponent scope | **GREEN.** All theorem records and all exponent sentinels are exactly unchanged. |
| Reverse equality | **GREEN.** Exact in-memory reversal equals the source graph. |
| Authoritative-file preservation | **GREEN.** Bytes and SHA-256 are unchanged after all tests. |

No numerical experiment, web result, or external theorem import was used.

## 7. Dependencies, artifacts, and recommended state effect

This audit used:

1. `protocol.md`;
2. `state/proof_obligations.yml` at the starting hash above;
3. `state/active_campaign.yml`;
4. `math_collab/proof_obligations.py` and the repository dry validator;
5. `proofs/kernels/m9_m2_hard_top_t1_residual_maximal_fejer_dyadic_positive_transform_obstruction.md`;
6. the final kernel reviews and post-repair verification;
7. the conductor Round-172 adjudication and synthesis; and
8. `rounds/codex-managed/m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate/state_patch.json`.

**Recommended state effect: apply the proposed Round-172 State Patch without
repair.**  Create exactly the one route-scoped proved obstruction, add it only
as the declared inconclusive dependency/evidence constraint to the two open
hard-TOP owners, append the eighteen rejected-claim records, and make no other
obligation change.  The permitted effect is evidentiary and strategic only.

**Final verdict: GREEN.**
