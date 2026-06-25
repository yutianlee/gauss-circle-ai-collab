# Round 2 Stage B Review Audit For Judge

Use this note when writing the Round 2 judge synthesis. It is a human/Codex audit of the three Stage B reviews after normalization.

## Consensus

- Accept the algebraic core: `C_h=2i chi_4(h)1_{2\nmid h}`, real-even `beta_h` under the current H4 convention, the raw two-sided M2 convention, the real-weight paired formula as implementation-only, and the corrected fourth-moment numerator

$$
N=
h_1d_2d_3d_4
-
h_2d_1d_3d_4
+
h_3d_1d_2d_4
-
h_4d_1d_2d_3.
$$

- Accept `h`-Cauchy sign-loss and endpoint diagnostics only as bounded guardrails.
- Record the diagonal-core observation only as `O(D^2) <= O(X)` compatibility. Do not use A2's exact `D^2/16` constant for the whole core.
- Reject promotion of `M9-near-collision-taxonomy`; exact taxonomy has unclassified residue and near-collision bands are unproved.
- Reject promotion of `M9`, `M9-M2`, `M9-near-collision-estimate`, and `GC-target`.
- Reject A3 evidence claims unless actual scripts/tables/logs exist.

## Review Weighting

- A1 review is the best calibrated and should guide state mutation.
- A3 review is also well calibrated and independently confirms the main downgrade decisions.
- A2 review has useful technical checks, but it pushes too hard toward a shifted-bilinear pivot. Treat that as a serious backup route, not as the new primary route.

## Recommended State Treatment

- `M9-M2-beta-algebra`: keep `derived_under_assumptions`, H4-dependent.
- `M9-M2-h-cauchy-sign-loss`: keep as bounded diagnostic / `derived_under_assumptions`.
- `M9-M2-fourth-moment-expansion`: keep `derived_under_assumptions` for algebra only.
- `M9-near-collision-taxonomy`: keep open.
- `M9-regression-raw-vs-paired`: keep proposed until actual committed artifacts exist.
- Optional new obligation: `M9-N0-diagonal-bound`, status `proposed` or `open`, for proving the `N=0` diagonal-core bound with actual `beta_h` and weights.

## Next Round

Primary route: M2 fourth moment with exact `N=0` taxonomy and near-collision lemma.

Backup route: direct signed bilinear estimate / residue-interference route, but only after A2 states a precise theorem, matrix norm, and endpoint spacing audit.

A3 must execute actual local diagnostics, not just describe them.

## Score Calibration Addendum

When scoring A2 and A3, separate:

- `idea_quality_score`: useful formulas, routes, diagnostics, or proof objects;
- `state_evidence_score`: evidence safe enough to mutate `state/proof_obligations.yml`;
- `calibration_score`: correct use of statuses and avoidance of overclaiming.

A2 should not be scored low because its route ideas are worthless; it should be scored low on state evidence because broad claims remain unproved and several `[PROVED]` labels are premature. A3 should not be scored low because diagnostics are irrelevant; it should be scored low on state evidence because scripts, commands, tables, logs, and reports are not yet committed.

For the State Patch, keep the single `mathematical_progress_score` conservative. In prose, include the split scores so future prompts can target the right failure mode:

- A2: good idea quality, weak state evidence, weak-to-moderate calibration.
- A3: good diagnostic design, weak state evidence until artifacts exist, moderate calibration.
