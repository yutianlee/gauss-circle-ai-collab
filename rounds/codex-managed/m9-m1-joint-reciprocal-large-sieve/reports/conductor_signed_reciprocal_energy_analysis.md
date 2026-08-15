# Signed reciprocal energy analysis

## 1. Result

RSLS remains a plausible new theorem, but no proof or counterexample was
found. Its exact B-process image is a second moment of shifted
square-root-product rows whose diagonal is already the full target.

## 2. Exact statement and hypotheses

For (k\asymp Q), the normalized (j)-B-process gives

\[
 S_k=(J/k)^{1/2}\sum_{\rho\in\{1,3\}}\epsilon_\rho
 \sum_{r\asymp k}c_\rho(k,r)
 e(2\sqrt{kX(r-\rho/4)})+O(X^{-A}),
\]

with fixed smooth symbols. Thus RSLS is equivalent, up to controlled
errors, to

\[
 \sum_{k\asymp Q}|P_k|^2\ll Q^2X^\varepsilon.
\tag{2.1}
\]

## 3. Proof or derivation

Stationary phase for (kX/j+\rho j/4) gives the displayed phase and
amplitude ((J/k)^{1/2}). Since (k\asymp Q), inserting this into the
energy factors out (J/Q); the target (QJ) becomes (2.1). Expanding
(2.1), the exact diagonal is (\asymp Q^2). Grouping (k(4r-\rho))
leaves a moving residue-restricted truncated divisor coefficient and the
common-(k) constraint; it is not a complete divisor convolution.

## 4. First doubtful or unproved step

The exact missing bound is

\[
 \sum_{k\asymp Q}|P_k|^2_{\rm off}\ll Q^2X^\varepsilon.
\]

It requires essentially lossless signed square-root-product spacing.

## 5. Required control test and outcome

- Energy normalization and diagonal: pass.
- Reciprocal Poisson character sign: pass.
- Alternating half-difference pairing: fail; one step moves the alias on
  unit scale, much larger than kernel width (Q^{-1}).
- Perfect powers: coherent fibers are at most diagonal-sized; no
  counterexample found.
- B-process: strict structural return to the subcritical one-sided
  square-root-product architecture, not a proof.

## 6. Dependencies and exact artifacts used

The discovery agent supplied this final result message after interruption;
the conductor materialized it. Inputs were the Round-67 packet and
Round-66 synthesis. No numerical experiment or external theorem was used.

## 7. Recommended state effect

Promote the exact energy/B-process reduction only after adjudication.
Retain RSLS and all downstream claims open.
