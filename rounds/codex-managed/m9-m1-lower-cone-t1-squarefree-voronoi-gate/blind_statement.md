# Statement-only Round 147 problem

Let (R=X^{1/4}), (N=\lfloor X\rfloor), and let
\(\mathcal I_M=\mathbb N\cap[M,B_M)\), (B_M\le2M), be disjoint
half-open product blocks with (M\ll R^2). Consider the exact scalar

\[
\mathfrak U_N^{(1)}=
\sum_M\sum_{\substack{s\in\mathcal I_M\\\mu^2(s)=1}}
s^{-3/4}V_{\rm low}(R^2s/N)C(s)e(+\sqrt{Ns}),
\]

where

\[
C(s)=\sum_{\substack{de=s\\e\ {\rm odd}\\e>4d}}\chi_4(e).
\]

The desired bound is
\(\mathfrak U_N^{(1)}\ll_{\varepsilon,V}X^\varepsilon\), uniformly
for real (X). It is enough, after partial summation, to prove for every
clipped prefix (M\le U\le B_M)

\[
\left|\sum_{\substack{M\le s<U\\\mu^2(s)=1}}
V_{\rm low}(R^2s/N)C(s)e(+\sqrt{Ns})\right|
\ll_{\varepsilon,V}M^{3/4}X^\varepsilon.
\]

Independently derive the exact odd/even and (\chi_4)-sector structure
of (C(s)). Before the cone is inserted, determine the ratio-Mellin
Euler product

\[
\sum_{\substack{d,e\ge1\\e\ {\rm odd}\\\mu^2(de)=1}}
\frac{\chi_4(e)}{d^{w+z}e^{w-z}},
\]

including its local factor at (2), its convergence domain, and the
support and size of the residual Euler coefficients after removing
(\zeta(w+z)L(w-z,\chi_4)\).

Then decide whether a lawful generalized-divisor Voronoi transform can
prove the prefix target. Retain a nonzero compact smooth radial test,
the strict cone or a separately proved target-safe smoothing, every
clipped prefix, the full residual Euler convolution, the exact conductor
and cusp normalization, all polar terms and Bessel branches, and
uniformity in every Mellin order required by the cone.

Check the resonance centre, width, and amplitude directly. Price the
complete block range, including (M\asymp R^2), (M=R^{4/3}), lower
blocks, (D=1), primes, even squarefree inputs, exact radicals, and
slowly rotating fixed-centre families. Preserve the individual positive
direction (e(+\sqrt{Ns})); cosine, centre averages, arbitrary
coefficients, and termwise dual moduli are not substitutes.

Return a seven-section report containing a proof, a strict
owner-complete reduction, or an exact no-go. An upper-capacity failure is
not a signed lower bound. Do not consult the proof graph, strategy files,
claimant artifacts, or sibling reports.
