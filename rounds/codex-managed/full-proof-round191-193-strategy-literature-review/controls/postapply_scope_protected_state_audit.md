# Round 194 post-application protected-scope audit

## 1. Result

**Verdict: PASS.** The applied Round 194 State Patch is confined to its declared strategy/evidence scope. The live graph has SHA-256

`815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89`,

exactly as required. A mechanical inverse recovers byte-for-byte the declared starting graph with SHA-256

`cbbb68b5bb7dd324ca60b1e099cf5787fa57639b5970d76464c2bce18cfcdd9e`,

and production replay recovers byte-for-byte the live graph. The applied patch has SHA-256

`918a9ff96cdeb0a603ee56646b9aa728c33fd45c242de761a5d593c6e8fccfe6`.

Among all 394 obligations present before application, exactly one obligation changed:

`M9-M1-hard-top-high-radical-small-t-residual-estimate`.

It remains `open`. Its only changed fields are `evidence.inconclusive`, `next_action`, `last_updated_round`, and `last_updated_at`. Exactly 20 new rejected-claim records were added, matching the patch IDs and reasons. No pre-existing rejection record changed. All 26 declared no-change obligations are deeply equal before and after application. No analytic status, statement, dependency, implication, blocker, ownership field, parent/interface field, theorem, bridge, or exponent changed, and no strategy conclusion was promoted to accepted mathematics.

## 2. Exact statement and hypotheses

This audit tests the following post-application claim under the repository's production graph representation and State Patch semantics:

1. The live bytes are the result of applying the repaired Round 194 patch to the declared starting bytes.
2. The operation cardinalities are exactly `create/update/correct_rejected/reject/no_change = 0/1/0/20/26`.
3. The sole update is the already-open hard-M1 small-t owner named above, and it changes only the four permitted paths.
4. The 20 rejection dispositions are additions only, with their patch-declared IDs and reasons.
5. Every object named by `no_change` is deeply equal across the reconstructed starting and live graphs.
6. Protected analytic content and all exponent-bearing theorem nodes are invariant.
7. The Round 194 P2 selection is stored only as inconclusive evidence and a next action, not as a theorem.

The recovered application metadata are:

- application time: `2026-08-30T02:58:26`;
- judge reference: `rounds/codex-managed/full-proof-round191-193-strategy-literature-review/reviews/conductor_round194_adjudication.md`.

Each of the 20 new rejection records has that round-194 timestamp and that single judge reference. The ten evidence additions on the selected owner all exist and all occur under `evidence.inconclusive`.

## 3. Proof or derivation

I first hashed the live file directly. Its bytes give the required live SHA-256. I then inverted precisely the reversible patch operations in memory:

- removed the 20 newly introduced rejected-claim records;
- removed the ten patch-declared inconclusive evidence paths from the selected owner;
- restored the patch-declared prior `next_action`;
- restored `last_updated_round: 193` and `last_updated_at: 2026-08-30T02:10:41`.

Serializing that inverse with the repository production graph dumper produced bytes identical to the starting graph bytes and the exact starting SHA-256 `cbbb68b5...`. Applying the patch through the production State Patch implementation to this reconstructed start, using the recovered application time and judge reference, produced bytes identical to the live file and the exact live SHA-256 `815c15c4...`. Thus the inverse and replay are byte-equivalent, not merely semantically or canonically equivalent.

A deep diff over all 394 pre-existing obligations found one changed obligation and four changed paths only:

| Object | Changed path | Applied effect |
|---|---|---|
| selected hard-M1 owner | `evidence.inconclusive` | append exactly ten existing Round 194 artifacts |
| selected hard-M1 owner | `next_action` | freeze the complete physical P2 determinant-fibre/vector objective |
| selected hard-M1 owner | `last_updated_round` | `193` to `194` |
| selected hard-M1 owner | `last_updated_at` | `2026-08-30T02:10:41` to `2026-08-30T02:58:26` |

The owner status is `open` on both sides. A global comparison of every pre-existing obligation found no change in `status`, `statement_tex`, `dependencies`, `implies`, `blockers`, `owner`, `type`, `track`, or `title`. The 26 no-change IDs in the patch were each checked as complete objects and were deeply equal. They comprise the accepted Round 183--193 hard-t reductions and sectors, their hard and smooth parents and assemblies, all M9-M2 parents, M9 and endpoint uniformity, both bridges, the internal one-third theorem, the external Li--Yang benchmark, the quarter target, and the elementary divisor-bound node.

The rejected-claim map gained exactly the following 20 patch records and nothing else: report agreement proves P2; Boolean ordering forces P1 first; one-close geometry proves P2 cancellation; relative positive-mass contraction is the target; arbitrary-coefficient dispersion proves P2; separate orientation norms retain the sign; a post-expansion scalar mask equals the physical P2 operator; width beyond square-root L estimates the complements; static Farey refinement proves P2; the scaled-orientation involution controls actual P2 coefficients; an MRS or Shen theorem imports to the first-failure masks; fixed-modulus Kloosterman saving removes the project deficit; no source match proves universal nonexistence; the GAR route passes through blockwise M9; the remaining BAL label has the critical energy ledger; P2 closes original t=1; P2 closes hard M1 or M9-M1; P2 closes M9 or the quarter target; the strategy review improves the global exponent; and an in-round owner pivot is authorized. Their exact stored IDs and reasons equal the patch entries.

Finally, the exponent-bearing nodes were compared directly. `GC-partial-one-third` remains `proved_internal` with its one-third statement unchanged; `GC-external-Li-Yang-theta-star` remains `proved_external_dependency` with exponent `0.3144831759740614...` and statement unchanged; and `GC-target` remains `open` with its quarter statement unchanged. Since all obligation statuses are invariant, the P2 strategy selection cannot have been promoted through any other theorem node.

## 4. First doubtful or unproved step

There is no doubtful step in the protected-scope accounting: direct byte hashes, complete deep diffs, exact inverse, and exact production replay agree.

The first mathematically unproved seam remains exactly the one recorded as the next action: for the physical lower-close/upper-far complement P2, obtain the full determinant-fibre/vector-dispersion saving while retaining the literal endpoint, carry, mask, phase, orientation, and one-outer-real-part structure. Round 194 selected this objective; it did not prove it. This audit makes no assertion that the proposed method succeeds.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| direct live-file SHA-256 | PASS: exact `815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89` |
| repaired patch SHA-256 | PASS: exact `918a9ff96cdeb0a603ee56646b9aa728c33fd45c242de761a5d593c6e8fccfe6` |
| in-memory inverse and production serialization | PASS: byte-identical starting graph, exact `cbbb68b5bb7dd324ca60b1e099cf5787fa57639b5970d76464c2bce18cfcdd9e` |
| production apply replay | PASS: byte-identical live graph and exact live hash |
| operation counts | PASS: `0/1/0/20/26` |
| pre-existing-obligation deep diff | PASS: one of 394 changed; only the declared owner |
| selected-owner path diff | PASS: only inconclusive evidence, next action, and two update-metadata fields |
| selected-owner status | PASS: `open` before and after |
| 26 declared no-change objects | PASS: all deeply equal |
| rejection dispositions | PASS: exactly 20 additions; IDs and reasons exact; no old record changed |
| evidence existence/classification | PASS: all ten appended paths exist and are inconclusive |
| protected analytic fields | PASS: no statement, dependency, implication, blocker, owner, type, track, title, or status drift |
| dependency/cycle validation | PASS: repository graph validation reports no issue |
| exponent quarantine | PASS: one-third, Li--Yang benchmark, and quarter-target nodes are byte-semantically unchanged |
| theorem-promotion control | PASS: no proof evidence or proved status added; strategy remains a next action only |

## 6. Dependencies and exact artifacts used

The audit used only these repository artifacts and implementations:

- `state/proof_obligations.yml` at live SHA-256 `815c15c4...`;
- `rounds/codex-managed/full-proof-round191-193-strategy-literature-review/state_patch.json` at SHA-256 `918a9ff9...`;
- the patch-named Round 194 evidence paths, for existence and classification checks;
- `rounds/codex-managed/full-proof-round191-193-strategy-literature-review/reviews/conductor_round194_adjudication.md`, the recovered judge reference;
- the repository production graph dumper, validator, and State Patch apply implementation.

The declared starting graph was reconstructed only in memory by the patch's explicit inverse rule. No authoritative state, patch, report, synthesis, or validation artifact was edited during the audit.

## 7. Recommended state effect

**Retain** the applied Round 194 State Patch without repair. Its state effect is exactly the intended one-owner strategy update plus 20 rejection dispositions, with all 26 protected no-change obligations and every theorem/exponent interface preserved. Round 195 may address the frozen P2 objective, but no Round 194 strategy, source, ranking, or report-agreement conclusion should be promoted as a theorem without a separate accepted analytic proof and mechanically valid future State Patch.
