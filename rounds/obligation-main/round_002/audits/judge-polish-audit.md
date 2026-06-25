# Round 2 Judge Polish And Audit

Source: `handoff/obligation-main/round_002/judge/judge-002.md`

Archived copy: `rounds/obligation-main/round_002/judge/judge-002.md`

## Polished Digest

The Round 2 judge synthesis is conservative and usable. It selects the M2 fourth-moment route as the primary route, keeps direct signed bilinear / residue-interference as backup, and explicitly rejects endpoint or M9-level promotion.

Accepted mathematical progress:

- exact character-factor algebra

$$
C_h=e(h/4)-e(3h/4)=2i\chi_4(h)1_{2\nmid h};
$$

- H4-dependent real-even M2 coefficient

$$
\beta_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)1_{2\nmid h};
$$

- raw two-sided M2 convention, with paired-real formula only under real dyadic weights;
- corrected two-sided fourth-moment numerator

$$
N=
h_1d_2d_3d_4
-
h_2d_1d_3d_4
+
h_3d_1d_2d_4
-
h_4d_1d_2d_3;
$$

- bounded-scope `h`-Cauchy sign-loss and endpoint diagnostics.

Rejected or downgraded:

- no promotion for `M9`, `M9-M2`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, or `GC-target`;
- no promotion for denominator-paired negligibility;
- no exact `D^2/16` constant for the whole diagonal core;
- no A3 computation evidence until actual scripts, commands, tables, logs, and reports exist;
- no route-closing claim from the dual-length observation.

## Polish Applied

The normalized judge file originally had valid State Patch syntax but several stale evidence paths, for example:

- `rounds/obligation-main/round_002/responses/A2.md`;
- `rounds/obligation-main/round_002/responses/A3.md`;
- `rounds/obligation-main/round_002/responses/A1_reasoning_2.md`;
- `rounds/obligation-main/round_002/reviews/A1_review_2.md`.

These were corrected in both handoff and archive copies to the actual archived files:

- `rounds/obligation-main/round_002/responses/A1-002.md`;
- `rounds/obligation-main/round_002/responses/A2-002.md`;
- `rounds/obligation-main/round_002/responses/A3-002.md`;
- `rounds/obligation-main/round_002/reviews/A1.md`.

After this correction, all referenced Round 2 response/review evidence paths resolve locally.

## State Patch Audit

Validation result: `Round State Patch OK`.

Patch operations:

- create: `M9-M2-N0-diagonal-core-bound`;
- update: `M9-M2-character-factor`, `M9-near-collision-taxonomy`, `M9-regression-raw-vs-paired`, `M9-M2-fourth-moment-expansion`;
- reject: six overclaims from A2/A3;
- no_change: `M9`, `M9-M1`, `M9-M2`, `M9-near-collision-estimate`, `M9-endpoint-uniformity`, `GC-target`, `H4`, `H4-source-audit`, `Li-Yang-source-audit`.

Round assessment:

- `mathematical_progress_score`: 3;
- `idea_quality_score`: 7;
- `state_evidence_score`: 3;
- `calibration_score`: 6.

This split score is well calibrated: Round 2 has useful ideas and algebraic cleanup, but little new state-promotable proof evidence.

## Caveats

1. The new `M9-M2-N0-diagonal-core-bound` obligation should remain `open`.

The judge correctly avoids marking the diagonal-core bound proved. It depends on H4 coefficient bounds, overlap bookkeeping, and exact actual `beta_h` weights.

2. The `implies` edge from `M9-M2-N0-diagonal-core-bound` to `M9-near-collision-taxonomy` should be read as a support relation, not as proof that the full taxonomy follows.

The blocker relation added to `M9-near-collision-taxonomy` is more important than the implication edge.

3. `M9-M2-character-factor` remains `open`.

This is conservative. The algebra is strong, but H4/source normalization and downstream analytic use still matter.

4. A3 artifact requirements are now precise.

The next A3 prompt asks for concrete repository artifacts. This should help fix the low state-evidence score.

## Recommendation

The corrected judge patch is safe to apply when the workflow is ready to update the proof graph. It should not be interpreted as endpoint progress. It is a good Stage D update because it records one narrow new obligation, rejects overclaims, and makes Round 3 tasks sharper.
