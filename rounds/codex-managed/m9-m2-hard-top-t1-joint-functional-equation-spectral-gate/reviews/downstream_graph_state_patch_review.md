# Round 169 downstream graph State Patch review

## 1. Result

**VERDICT: PASS AFTER APPLY.**

The applied Round-169 State Patch has exactly the authorized graph scope:

\[
 (\mathrm{create},\mathrm{update},\mathrm{correct},\mathrm{reject},
   \mathrm{no\ change})=(1,1,0,7,22).
\]

It creates one `proved_internal` self-return reduction, updates only the
still-open signed-cone owner, records seven scoped rejected readings, and
does not mutate any of the 22 declared no-change obligations.  The raw
SHA-256 of the resulting authoritative graph is

`111809875d911d279ae22bee2ce44f0dba97130eeedcdca0dc65f53f163283ae`.

No unrelated obligation, parent status, bridge, theorem, or exponent was
changed.

## 2. Exact statement and hypotheses

The created obligation is exactly

`M9-M2-hard-top-t1-joint-functional-equation-double-poisson-self-return`.

It has type `reduction`, track `M9_analytic`, status `proved_internal`,
empty `implies` and `blockers`, and exactly the two direct dependencies

1. `M9-M2-hard-top-t1-mellin-euler-polylog-and-signed-moment-reduction`;
2. `M9-M2-hard-top-t1-character-poisson-product-collar-obstruction`.

Both dependencies exist and have status `proved_internal`.  The accepted
statement agrees with the reviewed candidate and kernel: it retains the
literal hard-TOP \(t=1\) cardinal scalar, the exact local and collapsed
\(g(Q,R)\) laws including \(p=2\), the completed zeta/\(\chi _4\)
kernels, the finite physical double-Poisson identity, and the correction

\[
 E_0=Z_{\rm phys}-R_\zeta,
 \qquad Z_{\rm phys},R_\zeta,E_0\ll L^2/J.
\]

It records the exact product stationary relation and the coefficientwise
return to the accepted Round-162 family, while expressly withholding the
open signed estimate, every parent conclusion, and every exponent
conclusion.

The sole updated obligation is
`M9-M2-top-endpoint-signed-cone`.  It remains `open`; its statement,
`implies` edge to `M9-M2-physical-one-count-assembly`, blocker, type,
track, and owner are unchanged.  The patch adds the new reduction once
as a dependency, adds the ten Round-169 paths once as inconclusive
evidence, and replaces only its `next_action` plus automatic round/time
metadata.

The dependency direction is correct: the open signed-cone owner depends
on the new reduction, and the new reduction depends on its two accepted
upstream reductions.  The new node has no implication edge.  It is
referenced nowhere else in `dependencies`, `implies`, or `blockers`, so
there is no attachment to the density-discrepancy energy and no local
cycle or reverse dependency path.

## 3. Proof or derivation

The graph was parsed independently and checked against the State Patch
object field by field.  The created node is byte-for-byte equal, as a
structured object, to the patch entry after adding only the validator's
automatic `last_updated_round`, `last_updated_at`, and judge-reference
metadata.  The owner contains exactly one copy of the new dependency and
exactly one copy of every requested inconclusive evidence path.  The
seven Round-169 rejected-claim IDs and reasons are exactly those in the
patch, each with the adjudication recorded as application evidence.

There are exactly two obligations with `last_updated_round: 169`: the
new node and the intended signed-cone owner.  There are exactly seven
rejected claims with that round marker, namely the seven patch entries.
All 22 no-change IDs exist, and none other than the separately authorized
owner has Round-169 mutation metadata.

As a stronger whole-file control, the patch was reversed in memory:

- remove the one created obligation;
- remove the seven new rejected claims;
- remove the one owner dependency and the ten owner evidence additions;
- restore the Round-168 owner action and its Round-168 application
  metadata.

Canonical graph serialization then has SHA-256

`a360b2913563c9c288438751729c5033acd2e91ee613e44f171e1d31bc7441be`,

exactly the declared Round-169 starting graph hash.  Therefore every
byte-level structured change from the starting graph is accounted for by
the authorized State Patch and its automatic application metadata.

The official graph validator returns `Graph OK`.  The graph now has 373
obligations and 1335 rejected claims, versus 372 and 1328 before this
patch.  Every evidence path on the new node exists.  The reviewed file
hashes also reproduce exactly:

- conductor candidate:
  `9edceafb9db77a2b2e2dcbb6e8c5b8e0308874fbf51048b883d363ac6d0013df`;
- accepted kernel:
  `b4c5e17aab5e586c1234af92f606dad1a8ccf199a108f3afc0ad5fd5977a37dc`.

## 4. First doubtful or unproved step

There is no remaining graph-application doubt.  The first unproved
mathematical step remains precisely the target-strength estimate of the
complete finite signed nonzero-frequency aggregate

\[
 \frac i2\sum_{Q,R}^{\rm phys}\frac{g(Q,R)}{QR}
 \sum_{k\ {m odd}}\chi _4(k)\sum_{\ell\ne0}
 \widetilde{\mathcal B}\!\left(\frac{k}{4Q},\frac{\ell}{R}\right)
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\]

The correction \(E_0\) is already target-safe.  Neither bare functional
equations, post-shift absolute resummation of the infinite \(G\)-series,
the favorable smooth positive collar, nor the dated audited spectral
placements prove this aggregate.  The applied graph correctly leaves
that interface, the full polynomial \(t=1\) face, and every downstream
owner open.

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| Raw resulting graph hash | **PASS:** `111809875d911d279ae22bee2ce44f0dba97130eeedcdca0dc65f53f163283ae`. |
| Exact operation counts | **PASS:** \((1,1,0,7,22)\). |
| Whole-graph reverse reconstruction | **PASS:** recovers the exact starting hash `a360b2913563c9c288438751729c5033acd2e91ee613e44f171e1d31bc7441be`. |
| Created-node object | **PASS:** exact patch content plus automatic round/time and judge-reference metadata. |
| Updated-owner scope | **PASS:** only the new dependency, ten inconclusive paths, next action, and automatic metadata changed; status remains `open`. |
| Rejected claims | **PASS:** seven exact fresh records with exact reasons and adjudication evidence. |
| Dependency direction and status | **PASS:** two accepted upstream dependencies, one downstream open-owner reference, empty `implies`/`blockers`, no local cycle. |
| No-change and unrelated nodes | **PASS:** all 22 IDs exist and are unmutated by Round 169. |
| Exponent quarantine | **PASS:** `M9-direct-menu-one-third-optimality`, `GC-partial-one-third`, `GC-external-Li-Yang-theta-star`, and `GC-target` are unchanged. |
| Evidence and artifact integrity | **PASS:** every new evidence path exists; candidate and kernel hashes match their reviewed values. |
| Authoritative graph validation | **PASS:** official validator reports `Graph OK`. |

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

This independent applied-state audit used:

1. `protocol.md`;
2. `state/proof_obligations.yml`;
3. `rounds/codex-managed/m9-m2-hard-top-t1-joint-functional-equation-spectral-gate/state_patch.json`;
4. `rounds/codex-managed/m9-m2-hard-top-t1-joint-functional-equation-spectral-gate/candidates/conductor_round169_joint_fe_double_poisson_self_return.md`;
5. `proofs/kernels/m9_m2_hard_top_t1_joint_functional_equation_double_poisson_self_return.md`;
6. `rounds/codex-managed/m9-m2-hard-top-t1-joint-functional-equation-spectral-gate/reviews/conductor_round169_adjudication.md`;
7. `rounds/codex-managed/m9-m2-hard-top-t1-joint-functional-equation-spectral-gate/reviews/downstream_graph_scope_review.md`;
8. the accepted Round-168 State Patch, used only to reconstruct the exact
   pre-Round-169 owner metadata for the whole-file hash control.

No state file, proof draft, validation matrix, campaign manifest,
synthesis, or mathematical kernel was edited.

## 7. Recommended state effect

**Retain the applied State Patch exactly as written.**  The resulting
graph is valid, acyclic at the new attachment, and fully scope-preserving.
Record the resulting hash
`111809875d911d279ae22bee2ce44f0dba97130eeedcdca0dc65f53f163283ae`
in Round-169 closure artifacts.  Make no further Round-169 graph change,
do not promote a parent or exponent, and proceed only after closing this
round to the mandatory Round-170 full-proof strategy and current-
literature review.
