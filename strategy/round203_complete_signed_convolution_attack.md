# Round 203: complete signed convolution attack

Date: 2026-09-23. Predecessor: closed Round 202. This document freezes
one analytic attempt, not a claim or a change to accepted mathematics.

## Objective

For the actual circle coefficients prove, or identify the first precise
unproved estimate in a serious attempt to prove,

\[
 \|K_T*\mu_{T,>U}^{*6}\|_2\ll_\epsilon T^{29/50+\epsilon},
 \qquad U=\lfloor T^{1/2047}\rfloor.
\]

Here \(a_n=r_2(n)n^{-3/4}\Psi(\sqrt{n/T})\), with the fixed radial
smooth probability mollifier from Round 201; \(\Psi\) is real even
Schwartz and \(\Psi(0)=1\). Fix nonnegative
\(\chi\in C_c^\infty((0,\infty))\), equal to one on
\([1/\sqrt2,\sqrt3]\). With \(e(t)=\exp(2\pi it)\), put

\[
 \mu_{T,>U}=\tfrac12\sum_{n>U}a_n
 \{e(-3/8)\delta_{\sqrt n}+e(3/8)\delta_{-\sqrt n}\},
 \qquad K_T(\xi)=T\widehat\chi(T\xi).
\]

Plancherel gives the exact tail moment as the square of this norm.
The low head has twelfth moment \(O(T)\), by the Round-202 reviewed
separation proof. Thus the target would give discrepancy twelfth
moment \(Y^{4+2/25+\epsilon}\) and pointwise exponent \(102/325\).
It would not prove the quarter conjecture.

## Bounded analytic approaches

1. Subtract a continuous density from the actual sixfold convolution.
   Derive the density from the arithmetic coefficients, estimate its
   filtered norm, and bound the entire remainder. A single counting
   asymptotic cannot silently become a sixfold approximation theorem.
2. Use the exact arithmetic identity
   \(r_2(n)=4\sum_{d\mid n}\chi_4(d)\), or the equivalent radial
   lattice sum, to estimate the complete signed tail. An oscillatory
   integral transformation must produce a net saving after both its
   main term and error are restored. Quantify any self-return.
3. Independently audit the smoothing scale and remainder interface in
   a statement-only task. Establish exactly when smoothing commutes
   with the filter and whether its removed part is controlled.

The conductor independently examines radial Poisson duality and the
local lattice shell at the physical scale. Each task ends after one
bounded report and, if needed, one specific review/repair cycle.
Effort: 100 percent analytical/algebraic; no numerical experiments.

## Inherited bounds and boundaries

The repaired Li--Yang bound remains the accepted benchmark
\(\theta=(3292+25\sqrt{1717})/13762\).
Writing \(\beta=2\theta-1/2\) and \(q_0=262/27\), the source-reviewed
moment plus supremum gives tail moment
\(T^{1+(12-q_0)\beta+\epsilon}\), or norm
\(T^{1/2+(12-q_0)\beta/2+\epsilon}\).
The target needs an additional norm saving
\((12-q_0)\beta/2-2/25=0.068072478\ldots\).
This printed moment benchmark remains candidate source evidence;
this round does not import a stronger external theorem.

The graph-proved physical majorant obstruction forbids termwise
absolute Fourier estimates: even nonzero actual near resonances have
positive mass of order \(T^{5/2}\). This does not lower-bound the
complete signed moment. Exact resonances have accepted mass \(O(T)\).
All upper tails and mixed head/tail terms must be accounted for.
The existing M1/M2 frontier and all exponent claims remain unchanged.

## Exit gates

The target is established only with a complete proof, independent
seam review, all arithmetic coefficients and tails, exact powers,
and a mechanically valid State Patch. Otherwise record precisely
which bounded mechanism fails and its quantitative first gap; do not
promote an identity or an unsuccessful method as an exponent gain.
At least one important interface gets statement-only rederivation.
Do not open a successor until this round has closed. The next broad
strategy and current-literature checkpoint is Round 205.
