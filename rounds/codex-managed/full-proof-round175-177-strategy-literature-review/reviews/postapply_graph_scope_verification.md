# Round 178 post-application graph and scope verification

- Campaign: `full-proof-round175-177-strategy-literature-review`
- Round: 178
- Role: independent post-application graph/scope verifier
- Starting graph SHA-256: `47c628b3e4b5086391fb3dbd885865ab21bd7470541099f696044bd2d3b609f7`
- Reviewed patch SHA-256: `654ce2c4a45ce3268fed04a8c95d68e57cef0766bec8c6c7c0bad22096cbc3cd`
- Resulting graph SHA-256: `e04380a1965e57971bb68d8169d8a8d8e5349edb535e01b343c8b25ecdcd4e27`
- Mode: read-only post-application verification; state was not edited

## 1. Result

**Verdict: GREEN.**

The applied Round-178 State Patch has exactly the reviewed effect:

\[
\boxed{0\text{ create}/1\text{ update}/0\text{ corrected rejected}/16\text{ new rejected}/20\text{ no-change}.}
\]

The current graph hash and patch hash exactly match the supplied expected hashes. The official graph validator reports the resulting graph `OK`.

The application changes only the strategy/evidence fields of
`M9-M2-hard-top-t1-residual-k17a-primitive-alias-conductor-reduction`, appends the sixteen reviewed rejected-overclaim records, and leaves all 380 obligation records, analytic statuses, statements, dependencies, blockers, implications, bridges, and exponent values unchanged. The selected Round-179 objective is exactly the aggregate high-conductor K17a estimate (177.K34), not (177.K35), K26, or another owner.

An exact in-memory reverse reconstruction serializes to the original starting hash. This proves that no unreviewed graph mutation accompanied the application.

## 2. Exact statement and hypotheses

The applied target remains `proved_internal`. Its Round-178 next action freezes

\[
q=\frac{u_0}{(\ell,u_0)},
\qquad Q_B=(\log(2X))^B,
\]

and the exact objective

\[
\boxed{
\left|
\sum_{u_0\mid u}
\sum_{\substack{\ell\bmod u_0\\u_0/(\ell,u_0)>Q_B}}
c_{u_0}(\ell)\mathcal H_{\kappa,u,u_0,\ell}
\right|
\ll_{B,\delta,\gamma,\varepsilon}LX^\varepsilon
}
\tag{177.K34}
\]

uniformly for every supported \((\kappa,u)\). The single outer absolute value occurs only after the exact \(u\to u_0\) gcd fold, all high-\(q\) aliases, both orientations, determinants, incomplete \(v\)- and \(n_0\)-lifts, fibre sites, literal selected/no-pair and squarefree fields, phases, parity branches, hard endpoints, and zero extensions have been recombined.

The applied next action retains the exact capacity ledger

\[
Lq\log(2q)
\]

at conductor \(q\), records that one reciprocal square root leaves \(L\sqrt q\log(2q)\), and requires a full conductor saving, two coupled square-root savings, or an equivalent signed average before positivity. It parks rank-one \(TT^*\), positive alias Parseval/bucket closure, lift-erasing completion, one-square-root recombination, and complementary-divisor orientation pairing. It explicitly prohibits an in-round pivot to the stronger aliaswise (177.K35), K26, another hard-TOP channel, BAL, UNBAL, either M1 route, GAR, the graded lane, or endpoint assembly.

Success is correctly limited to the residual K17a route and has no exponent implication without separate accepted connectors.

## 3. Proof / derivation

### 3.1 Hash and validator checks

Direct hashing gives:

- current `state/proof_obligations.yml`:
  `e04380a1965e57971bb68d8169d8a8d8e5349edb535e01b343c8b25ecdcd4e27`;
- applied `state_patch.json`:
  `654ce2c4a45ce3268fed04a8c95d68e57cef0766bec8c6c7c0bad22096cbc3cd`.

Both equal the expected values. The repository's official graph validator returns no issue.

### 3.2 Exact applied operation count

The current graph has 380 obligations, unchanged from the starting graph. Its rejected-claim count is 1,472, exactly

\[
1456+16.
\]

All sixteen new IDs are exactly the patch's sixteen `Round178-*` rejected-overclaim IDs. Each has the reviewed reason, `last_updated_round: 178`, and the common application timestamp `2026-08-27T11:49:51`. None collides with an obligation or an earlier rejected claim. There are no duplicate obligation or rejected-claim IDs.

The twenty `no_change` directives perform no mutation, as specified by the patch semantics. There is no created obligation and no corrected prior rejected claim.

### 3.3 Sole target mutation

The sole updated obligation has:

- unchanged status `proved_internal`;
- `last_updated_round` changed from 177 to 178;
- application timestamp `2026-08-27T11:49:51`;
- inconclusive evidence count changed from 1 to 11; and
- the reviewed (177.K34)-only next action.

Its positive evidence count remains 16 and its negative evidence count remains 0. The ten added inconclusive paths are exactly the three Round-178 reports, five accepted pre-patch reviews, conductor control, and synthesis reviewed in the patch-scope audit. No extra evidence path was inserted.

### 3.4 Exact reverse-hash proof

The applied graph was reversed in memory by only:

1. removing the ten reviewed inconclusive evidence paths from the sole target;
2. restoring its Round-177 next action, `last_updated_round`, and timestamp; and
3. deleting the sixteen new rejected-overclaim records.

The repository's canonical serializer then produced SHA-256

`47c628b3e4b5086391fb3dbd885865ab21bd7470541099f696044bd2d3b609f7`,

exactly the starting graph hash. The reverse graph validates cleanly, has 380 obligations, 1,456 rejected claims, and the original single inconclusive target-evidence entry. Because the complete serialized object returns byte-for-byte to the starting hash, there is no hidden change to any other field or record.

### 3.5 Edge, cycle, dangling-reference, and exponent scope

The exact reverse-hash comparison proves that every status, `statement_tex`, dependency, blocker, implication, promotion rule, bridge, and exponent-bearing record differs from the starting graph only by the reviewed non-edge fields above. Therefore the complete edge signature is unchanged.

No dependency, blocker, or implication reference is dangling. No cycle is introduced; in particular, the forward implication relation remains acyclic. There is no new edge from K17a to a residual scalar, full \(t=1\), hard TOP, M9--M2, M9, either bridge, GC-target, or an exponent owner.

`GC-partial-one-third` and `GC-external-Li-Yang-theta-star` remain unchanged. The exponent ledger is still

\[
\theta_{\rm internal}=\frac13,
\qquad
\theta_{\rm external}=0.3144831759740614\ldots,
\qquad
\theta_{\rm target}=\frac14.
\]

## 4. First doubtful or unproved step

No post-application graph defect remains. The first unproved step is still the analytic inequality (177.K34).

The applied next action does not treat the strategy selection, source audit, conductor reduction, one-square-root bound, or capacity ledger as evidence for (177.K34). A future proof must obtain the full signed saving with the complete literal coefficient, then pass local-to-global summation, sector assembly, seam review, false controls, and a separate conductor-owned State Patch before any higher owner changes.

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| Starting, patch, and resulting hashes | **PASS:** all three exact values match |
| Official current-graph validation | **PASS:** graph OK |
| Exact `0/1/0/16/20` effect | **PASS** |
| Obligation/rejected counts | **PASS:** 380 unchanged; 1,456 to 1,472 |
| Sole updated target | **PASS:** only primitive alias-conductor reduction strategy/evidence metadata changed |
| Evidence | **PASS:** exactly ten reviewed paths, inconclusive count 1 to 11; positive/negative unchanged |
| New rejected records | **PASS:** exactly sixteen reviewed IDs/reasons; no collision or duplicate |
| Status and statement drift | **PASS:** none |
| Dependency/blocker/implication drift | **PASS:** none |
| Dangling references and new cycles | **PASS:** none |
| (177.K34) objective fidelity | **PASS:** exact aggregate target, capacity, controls, no K35 pivot, residual-only scope |
| Exponent drift | **PASS:** none |
| Exact reverse reconstruction | **PASS:** canonical reverse hash equals starting hash |

No numerical theorem experiment was performed. All checks were read-only hashing, exact graph parsing, canonical reversal, and validation.

## 6. Dependencies and exact artifacts used

This verification used:

- `protocol.md`;
- current `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/full-proof-round175-177-strategy-literature-review/state_patch.json`;
- `reviews/state_patch_scope_cycle_review.md`;
- the accepted Round-178 reports, reviews, conductor control, adjudication, and synthesis referenced by the applied evidence; and
- the repository graph loader, canonical serializer, patch semantics, and validator in `math_collab/proof_obligations.py` and `math_collab/validate_state_patch.py`.

The supplied starting, patch, and resulting hashes were independently recomputed where files were available. The starting object was reconstructed only in memory from the exact reviewed inverse operations and verified by its canonical hash. No state, patch, report, control, synthesis, validation matrix, or proof draft was edited.

## 7. Recommended state effect

**GREEN: retain the applied Round-178 graph exactly as written and close the post-application verification gate.**

The authoritative state now records only strategy/evidence progress and the unique Round-179 objective (177.K34). It does not promote K17a, the residual scalar, full \(t=1\), hard TOP, BAL, UNBAL, M9--M2, either M1 route, GAR, endpoint uniformity, M9, either bridge, GC-target, or an exponent.

No corrective State Patch is required. The Gauss circle conjecture remains open.
