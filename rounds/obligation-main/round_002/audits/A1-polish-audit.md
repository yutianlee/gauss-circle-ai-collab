# A1 Round 2 Polish And Audit

Source: `handoff/obligation-main/round_002/responses/A1.md`

## Polished Digest

A1 gives a strong algebraic and route-selection response for the active M2 obligations. The response should be treated as useful proof-infrastructure progress, not as an endpoint estimate.

Main accepted content:

1. Under the current H4 coefficient convention

$$
\alpha_{h,H}=-\frac{\Phi(|h|/(H+1))}{2\pi i h},
$$

the frequency-side character factor satisfies

$$
C_h=e(h/4)-e(3h/4)=2i\chi_4(h)1_{2\nmid h}.
$$

2. The actual fixed M2 coefficient is

$$
\beta_{h,H}
=
\alpha_{h,H}C_h
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)1_{2\nmid h}.
$$

Hence

$$
\beta_{-h,H}=\beta_{h,H}\in\mathbb R.
$$

This corrects earlier confusion about the sign and conjugacy of `beta_h`.

3. The raw two-sided M2 formula remains canonical. If the dyadic weight `w_D` is real, the paired real formula is valid. If `w_D` is complex, the paired real formula is not valid without modification.

4. A1 correctly distinguishes two bounded diagnostics:

- Positive `|alpha_h|`-weighted `h`-Cauchy has acceptable diagonal size but loses the `chi_4(h)` sign because `|C_h|^2=4 1_{2\nmid h}`.
- Unweighted `h`-Cauchy has an endpoint diagonal of size `D H_D`, which is `X^(3/4)` at `D ~ X^(1/2)`, exceeding the squared endpoint target.

5. A1 records the corrected two-sided fourth-moment phase

$$
\frac X4
\left(
\frac{h_1}{d_1}
-
\frac{h_2}{d_2}
+
\frac{h_3}{d_3}
-
\frac{h_4}{d_4}
\right)
$$

and the cleared numerator

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

6. A1's route ranking is usable:

- Primary route: fourth-moment near-collision route.
- Backup route: CRI residue-interference route.
- Third route: direct fixed-coefficient signed bilinear route.

The primary route is the best next analytic route because it is the only one in A1's list that keeps the character product through a substantial expansion while giving A2 a concrete taxonomy task.

## Audit

### Strengths

- The `C_h` computation is correct, including negative `h`.
- The `beta_h` calculation is correct under the stated H4 convention.
- The real-weight paired formula is correctly scoped.
- The complex-weight warning is important and should be handed to A3.
- The weighted Cauchy sign-loss diagnostic is correctly bounded in scope.
- The unweighted Cauchy endpoint diagonal calculation is a useful guardrail.
- The fourth-moment expansion and numerator `N` are algebraically consistent.
- The near-collision scale `T_D=D^4/X` is a valuable clarification.
- The route-proposal section satisfies the strengthened prompt better than Round 1.

### Caveats

1. The `beta_h` formula remains conditional on H4 source normalization.

Do not promote this beyond `derived_under_assumptions` until `H4-source-audit` is complete.

2. The source/literature paragraph should not be treated as a completed source audit.

A1 names Vaaler and Li-Yang metadata, but this is not a rendered-page theorem audit. Keep `H4` and `Li-Yang-source-audit` unchanged.

3. The proposed state patch is not validator-ready.

It uses informal keys like `updates` and `no_status_change`. The judge may use the content, but the formal patch must use:

```json
{
  "proof_obligations": {
    "update": [],
    "no_change": []
  }
}
```

4. The complex-weight counterexample should be phrased generically.

The example `w_D(d)=i` shows the conjugacy failure unless the relevant exponential sum happens to vanish. A3 should test a concrete nonzero block.

5. The preliminary collision taxonomy is not complete.

The direct and pair-swapped families look safe. Reduced-fraction, sign-symmetric, denominator-paired, mixed, truncation-edge, and near-collision families remain open. A2 must avoid double-counting overlaps between these families.

6. The fourth-moment route may still be too strong.

The sufficient target

$$
|S_2(D;X)|^4\ll_\epsilon X^{1+\epsilon}
$$

is clean, but A1 has not shown that the exact and near-collision masses can meet it.

## Recommended Use In The Round

### For A2

Use A1's `beta_h` and `N` as the convention. Do not revisit sign conventions unless giving an explicit counterexample.

Priority checks:

- classify exact `N=0` families without double-counting;
- estimate reduced-fraction diagonal mass with actual `1/|h|` weights;
- test sign-symmetric two-sided families;
- define near-collision bands using `T_D=D^4/X`;
- separate rational near-collision from modular phase aliasing.

### For A3

Translate A1's formulas into code:

- verify `C_h`;
- verify real and even `beta_h`;
- verify raw-vs-paired equality for real weights;
- verify paired-real failure for complex weights;
- enumerate small exact `N=0` bins using the corrected numerator.

### For The Judge

The judge should probably accept A1's contribution as:

- `M9-M2-beta-algebra`: keep `derived_under_assumptions`, dependent on `H4`;
- `M9-M2-h-cauchy-sign-loss`: keep as bounded diagnostic;
- `M9-M2-fourth-moment-expansion`: keep as algebraic expansion, analytic estimate open.

No promotion should be made for:

- `M9`;
- `M9-M2`;
- `M9-near-collision-taxonomy`;
- `M9-near-collision-estimate`;
- `GC-target`.

## Bottom Line

A1's response is a useful route-setting artifact. It should raise A1's route-generation score relative to Round 1. The primary next route should be the fourth-moment near-collision route, with CRI retained as a diagnostic backup. The response does not prove any endpoint estimate.
