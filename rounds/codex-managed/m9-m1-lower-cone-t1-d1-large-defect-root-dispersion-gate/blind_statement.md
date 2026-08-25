# Blind statement for Round 154

Work only from this statement and `protocol.md`. Do not inspect strategy,
graph, prior-round, candidate, sibling-report, proof-draft, or validation
artifacts.

Let $R=X^{1/4}$, $N=\lfloor X\rfloor$, $1\ll M\le R^2$, and
$J=M^{3/4}$. Let $A(n)$ be a complex profile extended by zero, supported on
$O_\varepsilon(X^\varepsilon)$ components in a fixed dilation of $[M,2M]$,
with supremum and discrete bounded variation
$O_\varepsilon(X^\varepsilon)$. Put

$$
 Q=\sum_{\substack{n>0\\n\ \mathrm{odd}}}
 {\bf1}_{|k(n)^2-Nn|>J}
 \chi_4(n)n^{-3/4}A(n)e(\sqrt{Nn}),
\tag{154.B1}
$$

where

$$
 k(n)=\left\lfloor\sqrt{Nn}+\frac12\right\rfloor.
\tag{154.B2}
$$

The target is

$$
 |Q|\ll_\varepsilon X^\varepsilon
 \qquad(M^{449}\ll R^{780}),
\tag{154.B3}
$$

uniformly in every parity and factorization of $N$ and every literal support
component and endpoint. An external coefficient of size
$O_\varepsilon(X^\varepsilon)$ remains outside $Q$.

Independently:

1. reparametrize $Q$ exactly by the nearest integer $k$ and signed defect
   $j=k^2-Nn$;
2. derive the exact cell, congruence, quotient parity and character, support,
   and phase formulas, including a lawful modulo-$4N$ Fourier encoding if
   useful;
3. record raw and weighted capacities, injectivity or multiplicity, positive
   and negative branches, all two-adic and imprimitive cases, and every
   endpoint;
4. test incomplete quadratic completion, Gauss evaluation, Poisson,
   dispersion, Cauchy placements, root spacing, and dyadic defect ranges;
5. prove (154.B3), isolate a strict owner-complete range, or identify the
   first exact completion, diagonal, root-spacing, quotient-profile,
   endpoint, or power obstruction.

The small-defect sector $|j|\le J$ is known target-safe only at scalar level
before Cauchy. Do not delete its mask inside a correlation. Do not assume an
upper capacity is a signed lower bound. Do not infer any conclusion for a
different coefficient, $D>1$, $L>1$, another $t$-layer, M2, or a global
theorem.

Return the required seven-section analytic report and stop.
