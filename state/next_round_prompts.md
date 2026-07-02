# Next Round Prompts

Generated after round 7 in run `obligation-main`.

Source judge synthesis: `rounds/obligation-main/round_007/judge/judge-007.md`.

## For A1

Target obligations: `H4-source-audit`, `M9-M2-exact-N0-total-mass`, `M9-M2-URES-representation-divisor-bound`, `M9-M2-URES-energy-reduction`, `M9-M2-unpaired-residual-URES`, `M9-near-collision-estimate`, proof-draft maintenance.

Objectives:

1. Insert the Round 7 exact-resonance suite into `state/best_proof_draft.md` and the lemma bank:
   - `Divisor-bound-elementary`;
   - `M9-M2-URES-representation-divisor-bound`;
   - `M9-M2-URES-energy-reduction`;
   - `M9-M2-exact-N0-total-mass`;
   - updated NF/DP/OB statements.

2. Reconcile the exact definition of \(R(r)\) with the Round 6 state:
   - ordered versus unordered pairs;
   - signed versus absolute weights;
   - reduced-fraction support;
   - dyadic lift convention \(h=gp,d=gq\);
   - parity restriction from beta support.

3. Write the short divisor-bound proof explicitly.

4. Keep all actual beta-weighted exact-resonance conclusions blocked by `H4-source-audit`.

5. Finalize `sources/vaaler_1985.md` with:
   - DOI;
   - local PDF path;
   - Theorem 6 equation (2.28);
   - Section 7 equations (7.1)--(7.3);
   - Theorem 18 equations (7.13)--(7.17);
   - coefficient sign;
   - Fejer normalization;
   - residual constant;
   - floor-compatible endpoint convention;
   - \(\Phi\) regularity;
   - M2 single-parity support.

6. State the next near-collision theorem in proof-draft-ready form:
$$
\Sigma_{\mathrm{abs}}(0<|N|\le M)
\ll_\epsilon
D^2\max(1,MX/D^4)X^\epsilon,
$$
or explain why this absolute version should be replaced by a signed variant.

7. Do not promote `M9`, `M9-M1`, `M9-M2`, `M9-near-collision-estimate`, `M9-endpoint-uniformity`, `GC-target`, or `H4`.

Exploratory allocation: write a one-page route map comparing the graded near-collision/global-moment route against the sign-preserving Poisson/SPD endpoint route.

## For A2

Target obligations: `M9-near-collision-estimate`, `M9-M2-GM4-from-exact-plus-graded`, `M9-M2-sign-preserving-poisson-voronoi-route`, `M9-M2-endpoint-algebraic-phase`.

Objectives:

1. Retract or repair the Round 7 URES obstruction:
   - explicitly include \(q_1\le2D\);
   - identify where the \(D^4\) or \(D^6\) inflation entered;
   - state the corrected divisor-sum estimate.

2. Attack the interval analogue of URES-D. Replace exact equality by
$$
\left|
\frac{p_1}{q_1}+\frac{p_3}{q_3}-\frac{\mu}{Q}
\right|
\le \eta.
$$
Derive the resulting inequality after multiplying denominators and identify the divisor/lattice-count theorem needed.

3. Determine whether the graded estimate
$$
\Sigma_{\mathrm{abs}}(0<|N|\le M)
\ll_\epsilon
D^2\max(1,MX/D^4)X^\epsilon
$$
is plausible for URES-type residual classes.

4. Restate the Poisson/B-process route as a smooth-weight theorem:
   - exact Fourier convention;
   - stationary point;
   - phase;
   - amplitude;
   - \(m\asymp hX/D^2\);
   - boundary terms;
   - \(k=0\) terms;
   - support-edge stationary points;
   - signed post-transform estimate required.

5. Keep `M9-M2-endpoint-algebraic-phase` as an identity only. Do not use it to imply endpoint uniformity.

Exploratory allocation: compare the sign-preserving endpoint route with the graded near-collision route and state one falsification test for each.

## For A3

Target obligations: `M9-fourth-moment-enumeration`, `M9-regression-raw-vs-paired`, `M9-M2-reciprocal-SPD-route` diagnostics.

Objectives:

1. Materialize executable diagnostics. The first line of the report must include:
   - command line;
   - Python version;
   - dependency versions;
   - precision settings;
   - exact dyadic convention;
   - H4 coefficient status.

2. Require `python -m py_compile` to pass before running.

3. Use exact rational arithmetic for \(N\), \(\lambda\), and URES factorization checks whenever exactness is claimed.

4. Standardize dyadic convention across all diagnostics, preferably \(d\in[D,2D)\), and state it in every table.

5. Correct the complex-weight regression:
   - raw two-sided formula;
   - complex-weight cosine pairing;
   - real-weight \(\operatorname{Re}B_h\) formula;
   - deliberate failure using genuinely complex \(d\)-weights or asymmetric \(h\)-weights.

6. Run URES-D tests:
   - random exact-resonance identities;
   - injectivity recovery of \(q_1,q_3\);
   - \(R(r)^2/D^2\) concentration for increasing toy ranges;
   - include the \((6,10,15,5)k\) family.

7. Run DP thin-band tests:
$$
0<|N|\le C_0D^4/X.
$$

8. Run endpoint sign diagnostics:
   - true beta;
   - unsigned beta;
   - random signs;
   - adversarial signs.

9. Archive script, command, tables, precision log, report, and pass/fail assertions. Keep all output `diagnostic_only`.

Exploratory allocation: one smooth-weight Poisson numerical sanity check near \(D\asymp X^{1/2}\), but only after the exact formula-regression bundle is complete.

## For A4

Target obligations: `M9-near-collision-estimate`, `M9-M2-URES-representation-divisor-bound`, `M9-M2-exact-N0-total-mass`, `M9-M2-unpaired-residual-URES`.

Objectives:

1. Transcribe the URES-D proof in lemma-bank form:
   - exact factorization;
   - injectivity;
   - divisor-bound count;
   - zero/nonzero numerator cases;
   - reducedness constraints;
   - dyadic denominator constraints.

2. Verify the lift-weight summation for actual beta magnitudes:
$$
\sum_{gq\in[D,2D)}|\beta_{gp,H_D}|
\ll_\epsilon \frac{X^\epsilon}{|p|}.
$$

3. Extend URES-D to a short-interval inequality if possible. Starting from
$$
\left|
\frac{p_1}{q_1}+\frac{p_3}{q_3}-\frac{\mu}{Q}
\right|
\le \eta,
$$
derive the corresponding near-factorization or lattice-strip condition.

4. Identify the first obstruction to proving
$$
\Sigma_{\mathrm{abs}}(0<|N|\le M)
\ll_\epsilon
D^2\max(1,MX/D^4)X^\epsilon.
$$

5. If the absolute near-collision estimate fails, construct a concrete lower-bound family with beta-weighted mass above budget. If it does not fail, propose the next exact divisor/lattice lemma.

6. Keep all exact \(N=0\) claims conditional on H4 when actual beta weights are used.

Exploratory allocation: formulate a signed variant of the near-collision estimate only after the absolute interval analogue has a clear obstruction.

## Round Assessment

| Agent | Idea quality | State evidence | Calibration | Assessment |
|---|---:|---:|---:|---|
| A1 | 8.4 | 7.3 | 9.0 | Strong source-discipline, beta algebra, R5/LFM route filtering, and accurate no-promotion stance. The main value is synthesis and proof-draft maintenance rather than a new analytic lemma. |
| A2 | 7.1 | 4.2 | 6.2 | Useful Poisson and endpoint-coordinate structure, but the URES obstruction is rejected and several Poisson/boundary claims were over-statused. |
| A3 | 7.1 | 2.5 | 7.4 | Good diagnostic design and some useful formula-audit instincts, but no accepted execution evidence; code/regression design must be repaired. |
| A4 | 9.6 | 9.0 | 8.8 | Strongest Round 7 contributor. The URES divisor factorization and exact \(N=0\) mass closure are proof-graph-safe under H4, with good scope discipline. |

Overall Round 7 assessment: substantial exact-resonance progress, no endpoint theorem. The state may gain conditional exact \(N=0\) closure, but not `M9-M2`, `M9`, or the final Gauss circle bound.
