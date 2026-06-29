# Next Round Prompts

Generated after round 3 in run `obligation-main`.

Source judge synthesis: `rounds/obligation-main/round_003/judge/judge-003.md`.

## For A1

Target obligations: `H4-source-audit`, `R5-Full-reconciliation`, `M9-M2-beta-algebra`, `M9-M2-fourth-moment-expansion`, and proof-draft consolidation.

Objectives:

1. Complete the rendered-source H4 audit from Vaaler 1985. Verify:
   - Theorem 6, equation (2.28), for $\widehat J(t)$;
   - Section 7, equations (7.1)--(7.3), for $i_N,j_N,k_N$;
   - Theorem 18, equations (7.13)--(7.17), especially (7.14);
   - coefficient sign in
$$
     \alpha_{h,H}=-\frac{\Phi(|h|/(H+1))}{2\pi i h};
$$
   - residual constant $(2H+2)^{-1}$;
   - Fejer normalization;
   - integer endpoint convention.

2. Write `R5-Full-reconciliation` into `best_proof_draft.md`. Compare the old H5r/DDP-trap concern with the product-count proof. The output must state exactly why using the positive Fejer majorant before Fourier expansion avoids the older arbitrary-coefficient trap, or else propose a downgrade.

3. Insert into `best_proof_draft.md`:
   - H1-H3 statement;
   - H4 statement, still source-audit-dependent;
   - R5-Full proof or reconciliation gap;
   - conditional bridge;
   - official M9 definitions;
   - $\mathcal M_2$ raw two-sided, paired real, and complex-weight cosine formulas;
   - fourth-moment numerator $N$;
   - open blockers.

4. State the first near-collision theorem exactly:
$$
   0<|N|\lesssim D^4/X
$$
   with coefficient weights, dyadic ranges, threshold convention, and whether the estimate is signed or absolute.

5. Do not promote `M9`, `M9-M2`, `M9-M2-N0-diagonal-core-bound`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, or `GC-target`.

Verification tasks:

- Cite exact rendered pages and equations.
- Preserve the floor-compatible convention $\psi_F(n)=-1/2$.
- Explicitly distinguish proof, conditional infrastructure, diagnostic computation, and open estimates.

Exploratory allocation:

- Write a one-page comparison between the denominator-paired fourth-moment route and the direct signed bilinear backup. Include one precise falsification criterion for each.

## For A2

Target obligations: `M9-M2-denominator-paired-weighted-bound`, `M9-M2-N0-diagonal-core-bound`, and `M9-near-collision-taxonomy`.

Objectives:

1. Prove or refute the weighted denominator-paired exact resonance lemma. Work in the subfamily
$$
   d_1=d_2=a,\qquad d_3=d_4=b,
$$
   where
$$
   (h_1-h_2)b+(h_3-h_4)a=0.
$$

2. Use the fixed two-sided convention:
$$
   1\le |h|\le H_D,
   \qquad
   H_D\asymp D X^{-1/4}.
$$

3. Use the actual H4-dependent coefficient class:
$$
   \beta_{h,H_D}
   =
   -\frac{\Phi(|h|/(H_D+1))}{\pi |h|}
   \chi_4(|h|)1_{2\nmid h}.
$$

4. Give a complete gcd decomposition. At minimum, set $g=(a,b)$, $a=ga'$, $b=gb'$, and parameterize frequency differences from
$$
   (h_1-h_2)b'=-(h_3-h_4)a'.
$$
   Track equality cases $h_1=h_2$, $h_3=h_4$, sign choices, endpoint truncation, and odd-frequency support.

5. Produce a bound for the absolute weighted mass. If the desired bound fails, give a counterexample construction and state the corrected obstruction.

6. Include a taxonomy table only for families actually treated this round. Mark all other families open.

7. Referee R5-Full against the older DDP-trap concern in one section, but do not make it the main proof unless A1's source audit exposes a real contradiction.

8. Any direct exponent-pair or Poisson alternative must be a proposed route only. It must include a named theorem statement, derivative scale, dual length $m\asymp hX/D^2$, boundary terms, actual $\beta_h$ weights, and uniformity over active $D$.

Verification tasks:

- Use only the allowed status labels.
- Do not label a central claim `[PROVED]` unless the proof is complete.
- Numerical examples are diagnostic only.
- The exact output should make clear whether the denominator-paired weighted bound is proved, refuted, or still open.

Exploratory allocation:

- If the weighted denominator-paired estimate stalls, formulate the smallest signed bilinear statistic that would imply M2, and state a fast A3 falsification test.

## For A3

Target obligations: `M9-regression-raw-vs-paired`, `M9-M2-denominator-paired-weighted-bound` diagnostics, `R5-Full-reconciliation` diagnostics.

Objectives:

1. Verify the committed Round 3 artifacts:
   - `rounds/obligation-main/round_003/artifacts/m9_regression/run.py`;
   - `rounds/obligation-main/round_003/artifacts/m9_regression/table_small.csv`;
   - `rounds/obligation-main/round_003/artifacts/m9_regression/precision.log`;
   - `rounds/obligation-main/round_003/artifacts/m9_regression/report.md`.

2. Update the raw-vs-paired script to include:
   - official $\mathcal M_1$ formula with $\chi_4(d)$;
   - official $\mathcal M_2$ raw two-sided formula;
   - paired real formula;
   - complex-weight cosine pairing;
   - explicit failure of the $\operatorname{Re}B_h$ formula for complex weights.

3. After A1 completes H4, replace any provisional kernel by the exact
$$
   \Phi(u)=\pi u(1-u)\cot(\pi u)+u.
$$

4. Scale the exact fourth-moment enumeration. Report:
   - total exact $N=0$ mass;
   - pair-equality mass;
   - denominator-paired mass;
   - semi-diagonal mass if classified;
   - unclassified exact $N=0$ mass;
   - near-collision mass for $0<|N|\le cD^4/X$;
   - signed and absolute versions;
   - normalization by $D^2$ and $X$.

5. Build a denominator-paired-only diagnostic table matching A2's variables $a,b,g,a',b'$ and frequency-difference parameter.

6. Run R5 residual product-count diagnostics for first leg and shifted legs $\rho=1,3$, with square, near-square, nonsquare, and divisor-rich $X$, and exact resonance handling.

7. Continue CRI and gradient-spacing diagnostics, but label all results `diagnostic_only`.

Verification tasks:

- Record command line, Python version, precision, exact table schema, pass/fail assertions, and H4 coefficient status.
- Use high precision near Fejer spikes and exact integer arithmetic for $N$.
- Do not infer asymptotic proof from finite tables.

Exploratory allocation:

- Compare fixed $\beta_h$ coefficients against unsigned, random-sign, and adversarial coefficients to test whether the signed route has visible structure.

## Round Assessment

| Agent | Idea quality | State evidence | Calibration | Assessment |
|---|---:|---:|---:|---|
| A1 | 8.5 | 8.0 | 9.0 | Strong algebraic normalization, conservative proof-state handling, useful route proposals, and correct separation of pair-equality core from full diagonal-core obligation. |
| A2 | 7.0 | 2.0 | 3.0 | Useful focus on denominator-paired and alternative direct routes, but central claims were overpromoted and several `[PROVED]` labels lacked complete proof. |
| A3 | 7.0 | 6.5 | 8.0 | Useful executed diagnostic artifacts and good diagnostic-only calibration; quantitative outputs remain provisional until H4 and larger runs. |

Overall mathematical-progress score is conservative: Round 3 sharpened the target and created usable diagnostic evidence, but it did not prove any endpoint estimate or complete a taxonomy.
