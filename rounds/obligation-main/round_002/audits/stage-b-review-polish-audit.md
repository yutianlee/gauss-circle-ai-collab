# Round 2 Stage B Review Polish And Audit

Sources:

- `rounds/obligation-main/round_002/reviews/A1.md`
- `rounds/obligation-main/round_002/reviews/A2.md`
- `rounds/obligation-main/round_002/reviews/A3.md`

## Polished Digest

The three reviews now converge on a conservative Round 2 synthesis:

1. The algebraic core is good progress.

The judge can safely credit the following as algebraic or diagnostic progress, still conditional where H4 normalization is involved:

- `C_h=e(h/4)-e(3h/4)=2i chi_4(h) 1_{2\nmid h}`;
- the H4-dependent real-even coefficient formula for `beta_h`;
- the raw two-sided M2 convention and the real-weight paired formula as an implementation-only specialization;
- the corrected fourth-moment numerator

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

- the weighted and unweighted `h`-Cauchy sign-loss/endpoint diagnostics.

2. The diagonal `N=0` core is probably compatible with the target, but not yet a promoted theorem.

A2's official response and the reviews identify exact diagonal, pair-swapped, and sign-symmetric families as genuine exact resonances. Their mass should be recorded as `O(D^2) <= O(X)` under bounded weights and `|beta_h| << 1/|h|`. Do not record A2's `D^2/16` constant for the union; the safer bound before overlap corrections is `O(D^2)`.

3. The near-collision taxonomy remains open.

All reviews reject promotion of `M9-near-collision-taxonomy`. The exact taxonomy still has unclassified residue, denominator-paired and semi-diagonal estimates are not proved, and no estimate exists for `0<|N| <= D^4/X`.

4. A3's regression direction is useful, but prose is not evidence.

A3's real-weight and complex-weight raw-vs-paired tests target the right formulas. However, no state promotion should rely on simulated or described files. The existing `M9-regression-raw-vs-paired` obligation should remain proposed until actual scripts, commands, tables, precision logs, and reports are committed.

5. The primary route should not be forcibly pivoted.

A1 and A3 recommend continuing the M2 fourth-moment route with sharper exact-resonance and near-collision tasks. A2's review argues for an immediate shifted bilinear pivot. Treat that as a serious backup route, not as the new primary route until it has a theorem statement, matrix norm, and endpoint spacing audit.

## Reviewer Audit

### A1 Review

Best calibrated review. A1 gives the most judge-ready accept/reject list:

- accept algebraic fourth-moment expansion and corrected `N`;
- accept `h`-Cauchy diagnostics as bounded guardrails;
- accept diagonal-core compatibility only as a revised `O(D^2)` observation;
- reject near-collision taxonomy promotion;
- reject denominator-paired negligibility as proved;
- reject A3 artifact claims until files exist;
- keep `M9`, `M9-M2`, `M9-near-collision-estimate`, `GC-target`, `H4`, and `Li-Yang-source-audit` unchanged.

Use A1's scores as reasonably calibrated: A2 around 6.4, A3 around 5.8.

### A2 Review

Technically useful but too aggressive strategically. A2 correctly rechecks A1's `C_h`, `beta_h`, and fourth-moment numerator. It also gives useful stress-test ideas for reduced fractions, continuous spacing, dynamic complex weights, and CRI covariance.

Caveats:

- A2 pushes too hard to discard the fourth-moment route as primary.
- The continuous Montgomery-Vaughan spacing issue is a diagnostic obstruction to naive smoothing, not a theorem-level route closure.
- A2's score of A1 at 9.0 and A3 at 8.0 is too generous for state mutation because H4 and actual A3 artifacts remain unresolved.
- A2's "A3 constructed executable diagnostics" phrasing should be read as a plan/prose artifact unless repository files exist.

Use A2's review for technical tests and backup-route pressure, not for state-promotion decisions.

### A3 Review

Well calibrated and useful as an independent proof-audit voice. A3 agrees with A1 that:

- coefficient algebra and Cauchy diagnostics can be accepted with proper scope;
- A2's `[PROVED]` labels are premature;
- the diagonal bound is plausible but not fully proved;
- the unclassified exact resonance and near-collision estimates are the central gaps;
- no endpoint or M9-level promotion is justified.

A3's recommendation to create a granular `M9-N0-diagonal-bound` obligation is useful. If the judge adds it, give it conservative status such as `proposed` or `open`, not `proved_internal`.

## Judge Instructions

### Accept Or Keep

- Keep `M9-M2-beta-algebra` as `derived_under_assumptions`, with explicit dependency on H4 normalization/source audit.
- Keep `M9-M2-h-cauchy-sign-loss` as a bounded diagnostic or `derived_under_assumptions`.
- Keep `M9-M2-fourth-moment-expansion` as algebraically useful, but not an analytic estimate.
- Add or update a note that the direct diagonal, pair-swapped, and sign-symmetric `N=0` families are compatible with `O(D^2) <= O(X)` under the actual reciprocal coefficient decay.

### Reject Or Downgrade

- Reject promotion of `M9`, `M9-M2`, `M9-near-collision-estimate`, and `GC-target`.
- Reject promotion of `M9-near-collision-taxonomy`; it remains open.
- Reject denominator-paired negligibility as proved.
- Reject any exact `D^2/16` constant for the whole diagonal core.
- Reject A3 evidence claims unless actual files exist.
- Reject route-closing language about dual-length/continuous-spacing obstruction.

### Next Round Tasks

- A1: draft the judge synthesis and a precise near-collision lemma statement with actual dependencies on `D`, `X`, `H_D`, `beta_h`, and `N`.
- A2: complete the exact `N=0` taxonomy with actual `beta_h` weights; resolve or explicitly isolate the unclassified class; prove or downgrade denominator-paired and semi-diagonal bounds.
- A3: produce actual committed diagnostics for raw-vs-paired formulas, exact `N=0` bins, near-collision bands, CRI tables, and bilinear gradient-spacing checks. Computation remains diagnostic only.

## Bottom Line

The reviews are usable after normalization. The judge should credit Round 2 as real algebraic progress and route sharpening, not as proof progress on the endpoint. The primary route remains M2 fourth moment plus exact-resonance/near-collision taxonomy; the direct signed bilinear route should be preserved as the backup.

## Score Calibration Addendum

The low A2 and A3 scores should be interpreted as low state-evidence scores, not as a claim that the outputs have no research value.

Suggested split scoring for the judge prose:

| Agent | Idea quality | State evidence | Calibration | Main reason |
|---|---:|---:|---:|---|
| A2 | 7 | 4 | 5 | Useful fourth-moment and backup-route ideas, but incomplete taxonomy and premature `[PROVED]` labels. |
| A3 | 7 | 3 | 6 | Useful diagnostics, but no committed executable artifacts yet. |

The formal `mathematical_progress_score` in the State Patch should stay conservative because it measures graph-safe progress. The prose score table should expose the split so the next prompts repair the right weakness: A2 needs narrow proof, A3 needs actual artifacts.
