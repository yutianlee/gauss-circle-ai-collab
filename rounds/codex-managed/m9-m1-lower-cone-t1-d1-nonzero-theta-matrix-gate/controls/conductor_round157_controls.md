# Round 157 conductor controls

- Campaign: m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate
- Round: 157
- Starting graph: 3b48c540f7acc5b3e2886279f735072e6c66ee14704e77cd05c74fe24f7b39ea
- Resulting graph: 3acbfaf6fb95047babd19800dee4152fb60cb408197a8ceac93931a20c57491f
- Allocation: 100% analytic, algebraic, and source verification; 0% numerical

## 1. Mathematical control ledger

| Control | Outcome |
|---|---|
| literal_nonzero_theta_matrix | GREEN. Every selector, Fourier factor, theta kernel, odd divisor, sign, profile, transition, and endpoint remains. |
| exact_zero_projection_and_centering | GREEN. The \(v=0\) row is subtracted once and gives the exact \(1/(4N)\) constant. |
| global_constant_tail | GREEN. It is the closed zero row and has zero sampled coefficient at every nonzero frequency. |
| complex_complementary_modes | GREEN. The exact coefficient is \(\widehat B_j(2dv)+\widehat B_j(-2dv)\); no conjugacy is assumed. |
| unique_Nyquist_fold | GREEN. The single fixed point is \(v=H/2=N/d\), with Fourier argument \(q/2\), and it is counted once. |
| literal_spatial_BV | GREEN. Monotone profile sampling, exact phase variation, one cell jump, zero extension, transitions, and endpoints give the required norm. |
| fold_twisted_interval_theorem | GREEN. Demodulation shifts every unit to the nonzero unit frequency \(c/2-u\), including \(c=4\) and long intervals. |
| N_M_V_d_power_ledger | GREEN. Restoring all exterior factors gives exactly \(M^{-1/4}X^\varepsilon\). |
| mixed_j_x_profile_variation | GREEN/no-go. One-variable BV alone permits a diagonal trace of capacity \(VM^{-3/4}X^\varepsilon\). |
| quadratic_root_rectangular_discrepancy | GREEN/no-go. Ordinary centered completion is \(\sqrt N\,\tau(N)\log^2(2N)\) and loses after restoration. |
| fixed_v_Fourier_Parseval_operator_placements | GREEN/no-go. Each named placement retains the documented positive power; none is treated as a lower bound. |
| selected_incidence_count | GREEN/capacity only. \(L_U(V)\ll\min(M,V)X^\varepsilon\); signed square-root cancellation is still unproved. |
| source_theorem_nonzero_match | GREEN/no-match. No audited theorem through 25 August 2026 matches the literal paired matrix. |
| positive_negative_defect_and_endpoints | GREEN. The two blocks are treated separately and strict endpoints are charged. |
| external_scalar_seam | GREEN/conditional. \(B_{1,U}(1)\) remains outside and may be reinserted only through its accepted \(X^\varepsilon\) bound. |
| downstream_scope | GREEN. No complete range, broader owner, M9 statement, bridge, target, or exponent is promoted. |

## 2. Exact accepted proof kernel

The exact centering is

\[
 \mathcal T_{\ne0,U}(V)=
 \sum_{V<|j|\le2V}\sum_{x\bmod4N}
 \left(B_j(x)-\frac{\widehat B_j(0)}{4N}\right)
 G_N(x^2-j).
\tag{157.C1}
\]

For the unique fold \(v=N/d\),

\[
 |\widehat B_j(q/2)|
 \ll_\varepsilon M^{-3/4}X^\varepsilon,
\qquad
 \sup_I\left|
 \sum_{j\in I}(-1)^jK(-(N/d)^2,-j;4N/d)
 \right|
 \ll \frac{4N}{d}\log(2N).
\tag{157.C2}
\]

Restoring every divisor and normalization factor proves

\[
 \mathcal F_U(V)\ll_{\varepsilon,A}
 M^{-1/4}X^\varepsilon.
\tag{157.C3}
\]

The corrected unsigned support theorem is

\[
 L_U(V)\ll_\varepsilon\min(M,V)X^\varepsilon.
\tag{157.C4}
\]

All identities and powers have independent or hostile review.

## 3. Terminal review and source gate

The following orthogonal terminal reviews are GREEN:

- independent centering, completion, incidence, and power mathematics;
- independent Nyquist normalization, spatial BV, twist, and power
  mathematics;
- hostile profile, transition, endpoint, blind-scope, and downstream
  audit; and
- independent source-hypothesis and cutoff-scope audit.

The State Patch scope review is GREEN: all evidence paths exist, the
two corrected rejected records are present, dependency directions are
cycle-safe, and no range or exponent is overpromoted.  The source
report incorporates its two nonfatal
precision corrections: DFI's weakened test condition retains (2.8) and
(2.28)--(2.29), and the standard Frobenius pairing uses
\(\overline A\), without changing any norm power.

## 4. Pre-mutation validation

Before graph mutation:

- completed-campaign validation: PASS;
- starting graph SHA-256 check: PASS;
- State Patch parse and dry validation: PASS for 1 creation, 8 updates,
  2 corrected rejected records, 23 new rejections, and 8 no-change
  decisions;
- terminal State Patch scope review: GREEN, with all evidence paths
  present and no new dependency cycle;
- strict campaign scan: PASS on 21 files, including the combined kernel,
  with 260 per-file-unique equation tags, 738 balanced bracket-display
  tokens, and no double-dollar displays; and
- MathJax preview rendering: PASS for all 19 campaign and kernel
  Markdown files.

No numerical experiment was used.

## 5. State mutation

The dry-validated State Patch applied:

- 1 obligation creation;
- 8 obligation updates;
- 2 corrections to stale Round 155 rejected records;
- 23 new rejected inferences; and
- 8 no-change decisions.

The graph validator passed immediately after mutation.  The resulting
SHA-256 is
3acbfaf6fb95047babd19800dee4152fb60cb408197a8ceac93931a20c57491f.
The proof draft is refreshed only from this accepted graph.

## 6. Complete closure validation

After the manifest, ledger, validation matrix, proof draft, failure
ledger, directives, reading packet, synthesis, controls, and validation
reports were closed:

- completed campaign and patched graph validators: PASS;
- seven structured JSON/YAML files: 7/7 parse;
- Python compilation: PASS;
- unit tests: 6/6 PASS;
- whitespace diff check: PASS, with repository line-ending policy
  warnings only;
- final campaign scan: PASS on 21 files with 260 per-file-unique
  equation tags, 738 balanced bracket-display tokens, and zero
  double-dollar tokens; and
- expanded closure scan: PASS on 35 files with 615 per-file-unique
  equation tags, 1,890 balanced bracket-display tokens, and 854 balanced
  double-dollar tokens.

Both strict scans require valid UTF-8, LF-only files, no BOM, forbidden
C0 or DEL byte, replacement, zero-width or directional code point,
missing final newline, trailing whitespace, duplicate per-file equation
tag, or unbalanced display delimiter.

## 7. Downstream decision

Close, if the terminal patch review and validators remain GREEN, under
\(\mathrm{outer\_defect\_centered\_discrepancy\_no\_go}\) in the
qualified route sense.  Promote exact centering, complementary orbit
normalization, the target-safe Nyquist fold, the corrected unsigned
incidence capacity, and only the named route-scoped no-go statements.
Retain the paired interior matrix, every complete positive-power range,
all other M1 and M2 owners, endpoint uniformity, M9, the bridge, the
quarter target, the internal exponent \(1/3\), and the audited external
Li--Yang exponent as open or unchanged.
