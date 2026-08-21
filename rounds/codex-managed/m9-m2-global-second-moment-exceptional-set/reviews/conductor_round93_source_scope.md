# Round 93 conductor review: sources and scope

## Source findings

The frozen large-sieve inequality is proved self-containedly in the blind
report, so no external theorem is a graph dependency. The hostile audit
independently maps the same normalization to Montgomery--Vaughan,
*Hilbert's Inequality*, Theorem 2 (1974), including the project's
\(e(x)=e^{2\pi ix}\) convention.

Vaaler's Theorems 6 and 18 are used only through the already audited H4
coefficient and the accepted \(C^1\) regularity of \(\Phi\).

Xiao's 2026 results average the unweighted sum

\[
 S(h,n)=\sum_{n/2\leq a\leq n}e(h\sqrt a)
\]

over an independent integer height \(h\). Their coefficient, support,
moving-endpoint, and fixed-\(X\) interfaces do not map to either canonical
M9 core. The primary-source audit is complete as a guardrail and supplies
no proof dependency.

## False-shadow controls

- Arbitrary bounded \(t\)-dependent denominator weights can align
  pointwise with the phases and produce moment \(\gg YD^2\). The theorem
  relies essentially on ordered-prefix or fixed-BV motion.
- Freezing separately on every height-floor interval loses
  \(Y^{1/4}\) at \(D\asymp\sqrt Y\); the exact increment telescope avoids
  that loss.
- The metric theorem is coefficient-blind after exact equality grouping.
  It therefore cannot provide the signed \(\rho^{-1/2}\) gain in the
  canonical M2 pointwise core.
- At threshold \(Y^{1/4}\), the top block has root-mean-square size
  \(Y^{1/4}\). A positive margin \(\eta>0\) is essential for density
  saving.

## Decision

Mark the Xiao audit complete as a non-importable guardrail. Record
Montgomery--Vaughan as corroborating source evidence only. Promote the
frozen and exact moving second moments and the assembled real-variable
global moment, but reject every pointwise or one-quarter graph edge.
