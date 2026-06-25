# Next Round Prompts

Generated after round 2 in run `obligation-main`.

Source judge synthesis: `rounds/obligation-main/round_002/judge/judge-002.md`.

## For A1

Target obligations: `M9-M2-beta-algebra`, `M9-M2-fourth-moment-expansion`, `M9-M2-N0-diagonal-core-bound`, and state maintenance.

Objectives:

1. Insert the proof-draft-ready $\mathcal M_2$ coefficient normalization into the proof draft, preserving H4 dependency:
$$
   C_h=2i\chi_4(h)1_{2\nmid h},
   \qquad
   \beta_{h,H}
   =
   -\frac{\Phi(|h|/(H+1))}{\pi |h|}
   \chi_4(|h|)1_{2\nmid h}.
$$

2. State the raw two-sided formula and the paired real formula, with the real-weight hypothesis explicit.

3. Write the fourth-moment expansion using the exact coefficient product and corrected numerator $N$.

4. Add a small lemma-bank entry for `M9-M2-N0-diagonal-core-bound` as open, not proved. State exactly what A2 must prove.

5. Keep `M9`, `M9-M1`, `M9-M2`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, and `GC-target` open.

6. Exploratory allocation: compare fourth moment, CRI, and direct signed bilinear routes in one page, with one falsification criterion for each.

Verification tasks:

- Check H4 source-card dependency before any coefficient bound such as $|\Phi(u)|\le C$ is used.
- Confirm that any paired implementation formula is labelled invalid for complex weights.

## For A2

Target obligations: `M9-near-collision-taxonomy`, `M9-M2-N0-diagonal-core-bound`, and `M9-M2-fourth-moment-expansion`.

Objectives:

1. Use one fixed two-sided convention:
$$
   1\le |h|\le H_D.
$$

2. Use the actual $\beta_h$ coefficients and the corrected numerator
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

3. Prove or explicitly mark open the `M9-M2-N0-diagonal-core-bound` lemma. Do not use the incorrect $\frac{1}{16}D^2$ constant for the whole core.

4. Produce a taxonomy table with columns:
   - family name;
   - defining equations;
   - proof that $N=0$;
   - coefficient product;
   - mass bound;
   - status;
   - remaining edge cases.

5. Resolve or preserve as open the unclassified exact $N=0$ residue reported in the small enumeration.

6. Downgrade denominator-paired negligibility unless a proof is supplied.

7. Define near-collision bands using
$$
   |N|\lesssim D^4/X
$$
   and state the first exact theorem needed to bound them.

8. Repair or alternative route: formulate the direct signed bilinear route as a precise lemma with coefficient class, matrix or spacing norm, dependency on a named theorem if any, and a fast falsification test.

Verification tasks:

- Supply either proof or reproducible computation for every numerical claim.
- Label central claims only as `[PROVED]`, `[DERIVED-UNDER-ASSUMPTIONS]`, `[HEURISTIC]`, `[CONJECTURED]`, `[ASSUMED]`, or `[LIKELY-FALSE]`.

## For A3

Target obligation: `M9-regression-raw-vs-paired`.

Objectives:

1. Produce actual repository-ready artifacts, not only a protocol:
   - `computations/m9_regression/run.py`;
   - `outputs/table_small.csv`;
   - `computations/m9_regression/precision.log`;
   - `computations/m9_regression/report.md`.

2. Use the official raw two-sided M1/M2 formulas and actual Vaaler coefficients. If H4 source audit is not final, clearly mark the coefficient as provisional and separate structural tests from quantitative tests.

3. For real dyadic weights, verify raw two-sided sums equal the paired real formulas.

4. For complex weights, verify paired real formulas fail unless modified.

5. Include explicit checks:
$$
   C_h=2i\chi_4(h)1_{2\nmid h},
   \qquad
   |C_h|^2=4\,1_{2\nmid h},
   \qquad
   \beta_{-h}=\beta_h.
$$

6. Implement small exact fourth-moment binning with the corrected $N$ and actual $\beta_h$ weights. Report exact $N=0$ bins, unclassified bins, and near-collision bands.

7. Compute CRI ratios:
$$
   R_{\rm CRI}
   =
   \frac{|\Sigma_1-\Sigma_3|^2}
   {|\Sigma_1|^2+|\Sigma_3|^2}.
$$

8. Compute one bilinear gradient-spacing diagnostic using
$$
   \nabla f(h,d)=
   \left(
   \frac{X}{4d},
   -\frac{hX}{4d^2}
   \right).
$$

Verification tasks:

- Record command line, Python version, precision settings, table schema, and pass/fail assertions.
- Label all output `diagnostic_only`.
- Do not use surrogate kernels as official evidence; put any toy kernel in a separate exploratory appendix.

## Round Assessment

| Agent | Idea quality | State evidence | Calibration | Assessment |
|---|---:|---:|---:|---|
| A1 | 8.0 | 7.0 | 8.0 | Strong algebraic normalization and conservative state handling. Best basis for the judge synthesis. |
| A2 | 7.5 | 3.0 | 4.5 | Strong route ideas and useful fourth-moment focus, but overpromotes incomplete taxonomy, numerical claims, and unproved denominator-paired estimates. |
| A3 | 6.5 | 2.5 | 6.0 | Good diagnostic design, but evidence is not committed/executed and uses provisional or possibly non-official normalizations. |

Overall, Round 2 is useful but not proof-level endpoint progress. The fourth-moment route is now the primary M2 research direction. The direct signed bilinear route remains the backup. Computation remains diagnostic only until actual files and outputs exist.
