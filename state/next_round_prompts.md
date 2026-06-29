# Next Round Prompts

Generated after round 4 in run `obligation-main`.

Source judge synthesis: `rounds/obligation-main/round_004/judge/judge-004.md`.

## For A1

Target obligations: `H4-source-audit`, `H4`, `R5-Full-reconciliation`, `M9-M2-beta-algebra`, `M9-M2-fourth-moment-average-to-pointwise`, and proof-draft consolidation.

Objectives:

1. Commit or draft the exact Vaaler source card `sources/vaaler_1985.md`. Include:
   - bibliographic data for Vaaler 1985;
   - local PDF path;
   - Theorem 6, equation (2.28), for $\widehat J(t)$;
   - Section 7, equations (7.1)--(7.3), for $i_N,j_N,k_N$;
   - Theorem 18, equations (7.13)--(7.17), especially the residual inequality;
   - coefficient sign
$$
\alpha_{h,H}=-\frac{\Phi(|h|/(H+1))}{2\pi i h};
$$
   - Fejer normalization $K_H(0)=H+1$;
   - floor-compatible endpoint convention $\psi_F(n)=-1/2$.

2. Insert A1's R5 product-count proof into `best_proof_draft.md`. The proof must use the positive Fejer majorant before Fourier expansion and must prove pointwise bounds for:
$$
T_d=X/d,
\qquad
T_d=(X/d+\rho)/4,\quad \rho\in\{1,3\}.
$$

3. Insert official M9 definitions:
$$
\mathcal M_1(D;X)
=
-4\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}
\sum_d\chi_4(d)w_D(d)e(hX/d),
$$

$$
\mathcal M_2(D;X)
=
4\sum_{1\le |h|\le H_D}
\beta_{h,H_D}
\sum_d w_D(d)e(hX/(4d)).
$$

4. Insert raw two-sided, real-weight paired, and complex-weight cosine formulas for $\mathcal M_2$.

5. Formulate the new `M9-M2-fourth-moment-average-to-pointwise` obligation precisely. Include a candidate local inequality, derivative estimate for $S_2(D;X)$, window length variable, and expected loss.

6. Do not promote `M9`, `M9-M1`, `M9-M2`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, or `GC-target`.

Exploratory allocation:

- Write a short comparison of three routes: absolute exact-resonance taxonomy, average-to-pointwise fourth moment, and direct signed bilinear estimate. State the proof obligation and falsification criterion for each.

## For A2

Target obligations: `M9-M2-paired-core-weighted-bound`, `M9-M2-N0-diagonal-core-bound`, and `M9-near-collision-taxonomy`.

Objectives:

1. Do not re-prove the denominator-paired subcase except as a cited sublemma.

2. Write proof-draft-ready proofs for the pair-swapped and semi-diagonal exact $N=0$ families.

## For A3

Target obligations: `M9-regression-raw-vs-paired`, `M9-fourth-moment-enumeration`, `M9-M2-fourth-moment-average-to-pointwise` diagnostics, and signed-vs-unsigned diagnostics.

Objectives:

1. Produce a complete executable artifact bundle. Include:
   - script path and full script contents;
   - exact command lines;
   - Python version and package versions;
   - precision log;
   - CSV table schema;
   - generated tables;
   - report.md;
   - pass/fail assertions.

2. Fix formula and API issues before execution:
   - define $e(t)=\exp(2\pi i t)$ explicitly;
   - use the official M1 phase $e(hX/d)$;
   - use the official M2 phase $e(hX/(4d))$;
   - parse integer parameters exactly for fourth-moment numerator calculations;
   - use high precision near Fejer spikes.

3. Run raw-vs-paired checks:
   - raw two-sided M2;
   - real-weight paired formula;
   - complex-weight cosine formula;
   - deliberate failure of $\operatorname{Re}B_h$ for complex weights.

4. Run exact $N=0$ enumeration with true beta weights:
   - pair-equality;
   - denominator-paired;
   - pair-swapped;
   - semi-diagonal;
   - mixed;
   - unclassified.

Report absolute weighted mass and signed mass normalized by $D^2$ and $X$.

5. Run denominator-paired identity checks using:
$$
a=ga',
\qquad
b=gb',
\qquad
h_1-h_2=ta',
\qquad
h_3-h_4=-tb'.
$$

6. Run near-collision bins:
$$
0<|N|\le C_0D^4/X
$$

at $D=X^{1/4}$, $X^{3/8}$, and $X^{1/2}$.

7. Run signed-vs-unsigned tests:
   - true $\beta_h$;
   - unsigned $|\beta_h|$;
   - random signs;
   - adversarial signs.

8. Run average-to-pointwise diagnostics:
   - local sup of $|S_2(D;X)|$ over short $X$ windows;
   - local fourth-moment average;
   - numerical derivative bound;
   - ratio of local sup to average-based upper bound.

All outputs remain `diagnostic_only`.

## For A4

Target obligations: `M9-M2-fourth-moment-average-to-pointwise`, `M9-near-collision-estimate`, and unclassified exact $N=0$ obstruction search.

Objectives:

1. Treat the harmonic-convolution lemma and denominator-paired bound as settled. Do not spend the round re-proving them.

2. Formulate a proof-level average-to-pointwise lemma for $S_2(D;X)$. Start from

$$
S_2(D;X)=
\sum_{1\le |h|\le H_D}
\beta_{h,H_D}
\sum_{d\asymp D}w_D(d)e(hX/(4d)).
$$

Derive a rigorous candidate inequality relating $|S_2(D;X_0)|^4$ to an average over $X\in I$ plus derivative loss. Track:
   - $|I|$;
   - $\sup_I |S_2|$;
   - $\sup_I |S_2'|$;
   - active range $X^{1/4}\le D\le X^{1/2}$;
   - $H_D\asymp DX^{-1/4}$;
   - whether the resulting bound can reach $X^{1+\epsilon}$ at fourth-moment scale.

3. Attack denominator-paired near-collisions. Use

$$
N=abL,
\qquad
L=(h_1-h_2)b+(h_3-h_4)a,
$$

so

$$
0<|N|\le C_0D^4/X
$$

implies

$$
0<|L|\ll C_0D^2/X.
$$

Since $D^2/X\le1$, determine whether this is just finitely many shifted exact linear equations and prove the corresponding weighted bound if possible.

4. If time remains, begin a structural obstruction search for mixed/unclassified exact $N=0$ solutions. State one exact parameterization attempt or one lower-bound construction.

5. Keep all claims calibrated. Do not claim `M9-M2`, `M9`, or `GC-target`.

Exploratory allocation:

- Propose one sign-preserving spacing or large-sieve theorem that would imply the direct signed bilinear estimate. State its exact variables and falsification test.

## Round Assessment

| Agent | Idea quality | State evidence | Calibration | Assessment |
|---|---:|---:|---:|---|
| A1 | 8.5 | 8.0 | 8.5 | Strong H4 formula audit, correct R5 pointwise product-count proof, useful M2 algebra, and good route framing. Slight overpromotion risk if H4/source-card completion is treated as already committed. |
| A2 | 7.5 | 6.5 | 5.5 | Correct denominator-paired proof core and useful paired-family extensions. Calibration is weaker because several `[PROVED]` labels overreach, and the R5 RMS discussion uses the wrong norm for pointwise R5. |
| A3 | 7.0 | 3.0 | 8.0 | Diagnostic design is well targeted and appropriately labeled `diagnostic_only`, but the artifact bundle is not yet executable state-positive evidence. |
| A4 | 8.5 | 8.0 | 9.0 | Best narrow analytic contribution: clean harmonic-convolution proof, correct H4 dependency, sharp scale $T\asymp D^2$, and important identification of the average-to-pointwise gap. |

Overall progress is moderate but real. The proof graph gains one reusable internal lemma and one H4-dependent exact-resonance sublemma. It does not gain an endpoint M2 estimate.
