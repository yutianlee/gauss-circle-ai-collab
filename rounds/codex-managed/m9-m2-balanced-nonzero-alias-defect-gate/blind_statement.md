# Round 116 statement-only problem

Let (L\ge16), (R\asymp L^3), and (K\asymp L). Fix one real smooth
literal block symbol (A(h,k)), supported on (h\asymp L), (k\asymp K),
with uniformly bounded rescaled derivatives and all support crossings kept.
Put

\[
 a(h,k)=\chi_4(h)\eta\!\left({(h,k)\over \sqrt L/2}\right)A(h,k).
\]

All sums below are finite, over positive integers, and remain inside this
one fixed block. Define

\[
 \Delta=h'k'-hk,\qquad \rho=hk'-h'k,
\]

and let `df` mean the two strict gates

\[
 |\Delta|>L,\qquad |\rho|>L.
\]

The exact open remainder is

\[
 \mathcal R^{\mathrm{osc}}
 =\sum_{\mathrm{df}}a(h,k)\overline{a(h',k')}
 \left[e\!\left(R(\sqrt{hk}-\sqrt{h'k'})\right)-1\right].
\tag{116.B1}
\]

The fully assembled phase-free double-far sum, obtained by deleting the
bracketed exponential and retaining only (1), is already known to be
(O_\varepsilon(L^3X^\varepsilon)). Therefore the requested target is

\[
 |\mathcal R^{\mathrm{osc}}|
 \ll_\varepsilon L^3X^\varepsilon.
\tag{116.B2}
\]

You must independently determine whether a half-shifted Poisson, stationary
alias, reciprocal-frequency, or local-energy formulation produces a lawful
inequality at this budget. Begin from (h'=h+p), (k'=k+q), derive the
character and parity exactly, and retain both gcd weights, both copies of
the literal symbol, both far gates, boundary pieces, and all alias errors.

The raw energy capacity is (L^4), so a proof needs one factor (L). No
absolute value over residues, shifts, divisors, aliases, or gcd shells is
allowed unless its complete cost is displayed. A transformed identity is
not a saving. A rigorous no-go must name the precise class of inequalities
it excludes and may not be reported as a lower bound for (116.B1).

Your report must contain exactly the seven contract sections: result; exact
statement and hypotheses; proof or derivation; first doubtful or unproved
step; required controls and outcomes; dependencies and exact artifacts;
recommended state effect.

