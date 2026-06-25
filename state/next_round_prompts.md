# Next Round Prompts

Generated after round 1 in run `obligation-main`.

Source judge synthesis: `rounds/obligation-main/round_001/judge/judge-001.md`.

## For A1

Target obligations: `M9-M2-beta-algebra`, `M9-M2-h-cauchy-sign-loss`, and `M9-M2-fourth-moment-expansion`.

Objectives:

1. Write a proof-draft-ready coefficient-normalization note using the actual H4 coefficient convention

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h}.
$$

2. Prove

$$
C_h=e(h/4)-e(3h/4)
=
2i\chi_4(h)1_{2\nmid h}
$$

and

$$
\beta_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)1_{2\nmid h}.
$$

3. State the paired real $\mathcal M_2$ formula for real dyadic weights only, and explicitly state why complex weights are outside that formula's hypotheses.

4. Write the weighted $h$-Cauchy sign-loss diagnostic and the unweighted $h$-Cauchy endpoint diagonal check as bounded-scope diagnostics, not no-go theorems.

5. Insert the corrected two-sided fourth-moment expansion and cleared numerator $N$ into the proof draft.

6. Do not promote `M9`, `M9-M2`, or `M9-near-collision-taxonomy`.

Exploratory allocation: give a one-page comparison of fourth moment, CRI, and direct signed bilinear routes for $\mathcal M_2$, with one falsification criterion for each.

Route-strengthening requirement: include `## Route proposals` with at least two serious proof routes. For each route, state the exact lemma it would prove, why it might work, which obstruction it attacks, dependencies, the first proof step, a fast falsification test, and a ranking against the other route.

## For A2

Target obligations: `M9-near-collision-taxonomy` and `M9-M2-fourth-moment-expansion`.

Objectives:

1. Rewrite the fourth-moment taxonomy using the actual $\Phi$-weighted coefficient $\beta_h$, not a Fejer-linear surrogate.

2. Use exactly one convention: preferably the two-sided convention

$$
1\le |h|\le H_D.
$$

3. Use the corrected phase

$$
\frac X4
\left(
\frac{h_1}{d_1}
-\frac{h_2}{d_2}
+\frac{h_3}{d_3}
-\frac{h_4}{d_4}
\right)
$$

and the corrected numerator

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

4. Classify exact $N=0$ families: exact diagonal, pair-swapped, semi-diagonal, denominator-paired, mixed, sign-symmetric, truncation-edge, and unclassified.

5. For every claimed class, give either a proof, a counterexample, or a status label from the allowed reasoning labels: `[PROVED]`, `[DERIVED-UNDER-ASSUMPTIONS]`, `[HEURISTIC]`, `[CONJECTURED]`, `[ASSUMED]`, `[LIKELY-FALSE]`.

6. Remove or repair the Gallagher obstruction. If retained, state a precise theorem with hypotheses and explain exactly how the M2 variables violate it.

7. Do not claim that A2-2's Poisson diagonal-capacity model proves M9. If used, restate it as exploratory and connect it back to the actual reciprocal $\mathcal M_2$ formula.

Exploratory allocation: define one CRI statistic under the two-sided convention and state what numerical behavior would falsify CRI as a serious route.

Route-strengthening requirement: include `## Repair or alternative route`. Do not only reject A1's route. Either repair the strongest criticized route into a narrower lemma, or propose one alternative route with exact hypotheses, proof-obligation impact, and a fast falsification test.

## For A3

Target obligation: `M9-regression-raw-vs-paired`.

Objectives:

1. Produce actual files, not only a protocol:

- `computations/m9_regression/run.py`
- `outputs/table_small.csv`
- a precision log
- `computations/m9_regression/report.md`

2. Use the actual raw two-sided M1/M2 formulas and actual Vaaler coefficients.

3. For real dyadic weights, verify raw two-sided sums equal the paired formulas to numerical precision.

4. For complex dyadic weights, verify that the paired real formulas fail unless modified.

5. Include explicit checks for

$$
C_h=2i\chi_4(h)1_{2\nmid h},
\qquad
|C_h|=2 \text{ for odd } h,
\qquad
\beta_{-h}=\beta_h.
$$

6. Include a weighted $h$-Cauchy sign-loss regression showing that $|C_h|^2=4\,1_{2\nmid h}$.

7. Include a small fourth-moment binning routine using the corrected $N$ formula. Label results diagnostic only.

8. Do not use surrogate kernels as official evidence. Toy kernels may appear only in a separate exploratory appendix.

Exploratory allocation: add one complex-weight failure test and one small exact-bin enumeration for A2's corrected taxonomy.

Route-strengthening requirement: translate the leading A1/A2 routes into executable checks where possible. If a route cannot be tested computationally, say exactly why and propose the closest diagnostic-only proxy.

## Round Assessment

Round 1 is useful but not proof-progress at the endpoint. The correct state update is narrow:

- Accept the exact $C_h$ and $\beta_h$ algebra, conditional on H4.
- Accept the weighted $h$-Cauchy sign-loss diagnostic.
- Accept the fourth-moment expansion and corrected numerator as algebraic reductions.
- Keep `M9`, `M9-M2`, and `M9-near-collision-taxonomy` open.
- Keep `M9-regression-raw-vs-paired` proposed until actual files exist.
- Reject A2's and A2-2's broad state promotions.
- Reject A3's algebraic premise about $\beta_{-h}$ and its surrogate-kernel evidence.

Scores for the reviewed non-judge agents, using the Stage B assessment:

| Agent | Score | Reason |
|---|---:|---|
| A2 | 5.0 | Correct base $C_h$ direction and useful fourth-moment instinct, but several central claims are false or unsupported, including the $16(-1)^{N/2}$ rule, denominator parity sieve, Gallagher obstruction, and state-patch promotions. |
| A3 | 5.5 | Correctly targets executable diagnostics, but the main premise about $\beta_{-h}$ is wrong, the official computation is not executed, and the surrogate kernel is not state evidence. |
