# Round 172 post-application exact reverse audit

- Campaign: `m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate`
- Round: 172
- Role: independent post-application graph and exact-reverse auditor
- Certified pre-patch SHA-256: `c98f95b6b3500d0f48365af338e543f9a0f251b22062f3898df5f448d6b54853`
- Authoritative post-patch SHA-256: `70592c104e0c149485b4fac3fe6582020767631938fe9036f204ae616f188b7f`
- Exact in-memory reversed SHA-256: `c98f95b6b3500d0f48365af338e543f9a0f251b22062f3898df5f448d6b54853`
- Verdict: **GREEN**

## 1. Result

The applied Round-172 State Patch passes the exact post-application reverse
audit.  Reversing its operations only in memory and serializing with the
repository's canonical `dump_graph` function produces SHA-256

`c98f95b6b3500d0f48365af338e543f9a0f251b22062f3898df5f448d6b54853`,

exactly the independently certified starting hash.  The authoritative graph
was not mutated during this audit: its bytes and post-patch hash remained
`70592c104e0c149485b4fac3fe6582020767631938fe9036f204ae616f188b7f`
before and after every check.

The post-patch graph validates with zero issues.  Relative to the exactly
reconstructed starting graph, it contains precisely one fresh obligation, two
changed pre-existing open owner records, and eighteen fresh rejected-claim
records.  There is no other obligation or rejected-ledger mutation, no
pre-existing status change, no theorem-record change, and no new dependency or
combined logical cycle.

## 2. Exact reconstruction inputs

The ephemeral Python object used in the pre-application audit was not persisted
to disk.  The two exact old owner snapshots were therefore reconstructed from
the immutable prior State Patches and their later metadata, then certified by
the required starting-hash equality; no field was guessed.

For `M9-M2-top-endpoint-density-discrepancy-energy`, the old `next_action` is
the exact Round-164 text from
`m9-m2-hard-top-t1-residual-signed-divisor-transport-gate/state_patch.json`:

> Preserve the canonical one-count and completed-real-part connector. Prove
> the actual residual length-L Fejer short-shift theorem and the other
> few-point channels before transferring any scalar result back to this
> energy. The exact reduction is not itself a completed-energy estimate.

Round 167 subsequently appended dependency/evidence without replacing that
text, so the exact pre-Round-172 metadata was
`last_updated_round: 167` and
`last_updated_at: 2026-08-26T15:28:52`.

For `M9-M2-top-endpoint-signed-cone`, the old `next_action` is the exact
Round-169 text from
`m9-m2-hard-top-t1-joint-functional-equation-spectral-gate/state_patch.json`:

> For the complete non-polylogarithmic t=1 face, prove the exact finite active
> signed nonzero-frequency aggregate exposed in Round 169 before every
> positive norm; the residue-completion correction is already target-safe.
> Retain all other t=1 and few-point channels, and use the mandatory Round-170
> strategy review before selecting the next analytic attack.

Its exact pre-Round-172 metadata was `last_updated_round: 169` and
`last_updated_at: 2026-08-26T18:06:38`.

These texts and metadata, together with the inverse of the additive operations
declared in the Round-172 patch, are sufficient to recover the exact old owner
records.  The resulting full-graph hash equals the certified starting hash,
which independently verifies every reconstructed byte after canonical
serialization.

## 3. Exact reverse derivation

Starting from the authoritative post-patch graph, the in-memory inverse did
exactly the following:

1. removed
   `M9-M2-hard-top-t1-residual-maximal-fejer-dyadic-positive-transform-obstruction`;
2. from each of the two declared owner updates, removed only the new obstruction
   dependency and the exact Round-172 inconclusive-evidence additions;
3. restored each owner's exact old `next_action`, `last_updated_round`, and
   `last_updated_at` listed above;
4. removed exactly the eighteen fresh `Round172-*` rejected-claim records; and
5. made no change for the twenty provenance-only `no_change` entries.

Canonical serialization of this in-memory inverse has the exact certified
pre-patch hash.  Both the post-patch and reconstructed pre-patch graphs pass
`validate_graph` with no issue.

The exact cardinalities are:

| graph | obligations | rejected claims |
|---|---:|---:|
| reconstructed pre-patch | 375 | 1,371 |
| authoritative post-patch | 376 | 1,389 |

Exact record comparison gives one created obligation, no removed obligation,
and exactly these two changed pre-existing obligations:

- `M9-M2-top-endpoint-density-discrepancy-energy`;
- `M9-M2-top-endpoint-signed-cone`.

For each owner the only changed keys are `dependencies`, `evidence`,
`next_action`, `last_updated_round`, and `last_updated_at`, exactly as prescribed
by patch application.  Both owners are `open` before and after.  The eighteen
new rejected IDs match the patch exactly, and no pre-existing rejected record
changes.

## 4. Graph, cycle, and status delta

All dependency and implication targets resolve in the post-patch graph.  With
dependency edges oriented prerequisite-to-dependent, the three pre-existing
cyclic strongly connected components remain exactly the same after application:

1. `M9-M1-lower-far-cone-microscopic-cell-reduction` with
   `M9-M1-lower-post-collar-smoothed-far-alias-reduction`;
2. `M9-M1-lower-height-alias-rank-one-product-fibre-obstruction` with
   `M9-M1-lower-incomplete-fibre-dispersion-obstruction`; and
3. `M9-M2-hard-top-product-fibre-mean-obstruction` with
   `M9-M2-hard-top-product-fibre-transform-self-return`.

Adding implication edges in source-to-consequence orientation leaves the same
four pre-existing combined cyclic components.  The additional combined pair is
`M9-M2-LFM-endpoint-degeneracy` with `M9-endpoint-uniformity`.  The Round-172
node belongs to no cyclic component.

No pre-existing obligation changes status.  Every pre-existing theorem record
is byte-for-byte identical as structured data.  Exact sentinel comparison is
GREEN for `GC-target`, `GC-partial-one-third`,
`GC-external-Li-Yang-theta-star`, `Conditional-bridge`,
`GC-global-M1-alternative-bridge`, `M9`, `M9-M1`, and `M9-M2`.
Consequently the internal exponent remains $1/3$, the accepted repaired
external benchmark remains $0.3144831759740614\ldots$, and the quarter target
remains open.

## 5. First doubtful or unproved step

There is no unresolved application, reverse, graph-validation, cycle, owner,
or exponent-scope seam.  The first unproved mathematical step remains a
target-strength bound for the complete literal signed nonzero
ordinary-frequency aggregate, either linkwise or after the full stopped-chain
sum, before any coefficient-uniform positive norm.  The applied obstruction
neither proves nor disproves that aggregate or (165.K26).

## 6. Required controls and outcomes

| Control | Outcome |
|---|---|
| Authoritative post-patch identity | **GREEN.** Exact SHA-256 is `70592c104e0c149485b4fac3fe6582020767631938fe9036f204ae616f188b7f`. |
| Post-patch graph validation | **GREEN.** Zero issues. |
| Exact inverse serialization | **GREEN.** SHA-256 is exactly the certified `c98f95b6...b54853`. |
| Reverse graph validation | **GREEN.** Zero issues. |
| Exact obligation delta | **GREEN.** One create, two and only two changed existing owners, no removal. |
| Rejected ledger delta | **GREEN.** Exactly eighteen fresh claims; no old claim changes. |
| Owner status delta | **GREEN.** Both updated owners remain `open`; no pre-existing status changes. |
| Dependency references | **GREEN.** No missing dependency or implication target. |
| Dependency SCCs | **GREEN.** The same three pre-existing components before and after. |
| Combined logical SCCs | **GREEN.** The same four pre-existing components before and after. |
| Theorems and exponents | **GREEN.** All theorem records and exponent sentinels are unchanged. |
| Authoritative-file preservation | **GREEN.** Post-patch bytes and hash are unchanged by the audit. |

No numerical experiment, web source, or external theorem import was used.

## 7. Dependencies and recommended state effect

This audit used:

1. `protocol.md`;
2. the authoritative post-patch `state/proof_obligations.yml`;
3. the Round-172 `state_patch.json`;
4. `math_collab/proof_obligations.py` for canonical serialization and graph
   validation;
5. the exact Round-164 and Round-169 predecessor update texts identified in
   Section 2;
6. the Round-167 and Round-169 accepted metadata; and
7. the independently certified pre-patch hash from the pre-application reverse
   audit.

**Recommended state effect: retain the applied Round-172 graph without
repair.**  The applied mutation is exactly reversible to the certified source,
is graph-safe, and has only the reviewed evidentiary and strategic scope.  It
licenses no additional owner, parent, bridge, theorem, or exponent promotion.

**Final verdict: GREEN.**
