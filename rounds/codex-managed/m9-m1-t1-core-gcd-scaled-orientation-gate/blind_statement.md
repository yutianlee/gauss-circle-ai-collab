# Round 193 statement-only packet

This packet is self-contained.  Do not consult any strategy, graph, prior
report, candidate, review, computation, or source card.

Let (L\ge2), (D=\lceil L^{1/2}\rceil), and let an opened incidence be

\[
 N=dm,\qquad N+r=d'm',\qquad 0<r<\lceil L\rceil,
\]

where (d,d') are positive odd integers, (r) is even, and both factor
pairs lie in fixed (O(L)) boxes.  The summand has the form

\[
 \chi_4(d')\chi_4(d)\,P_r(N)\,
 A_{N+r}(d')\overline{A_N(d)},
\]

where (P_r(N)) depends only on (N,N+r,r), and every (A_N(d)) is
zero-extended off its literal arithmetic and geometric support.

Put (g=(d,d')) and (k=(m,m')).  On (k=1), consider

\[
 \tau_g(d,m,d',m')=(gm,d/g,gm',d'/g).
\]

Restrict to opposing incidences, (r\equiv2\pmod4), and

\[
 |d-gm|\le D,\qquad |d'-gm'|\le D.
\]

In plus primitive coordinates one may write

\[
 d=\kappa gU,quad d'=g(\kappa U+2S),quad
 m'=\kappa v,quad m=\kappa v+2w,quad
 Sv-Uw=h>0,
\]

with the usual coprimality conditions and all variables positive.

Independently determine:

1. the exact integrality, gcd, parity, orientation, involution, product,
   phase, and character-sign identities for (\tau_g);
2. the transformed primitive coordinates and every extra hypothesis needed
   for them to be canonical;
3. the strongest count implied by the two close inequalities, including
   floors, small variables, and (D\ge U) cases;
4. for abstract bounded (A_N(d)), whether the algebra alone proves any
   cancellation;
5. under an explicit common-cell (O(D/L)) difference hypothesis plus a
   scale-normalized discrete-BV and finite-boundary-collar hypothesis, the
   exact multiplicity bound required for an (O(L^2L^\epsilon)) estimate;
6. the first doubtful or unproved step and a finite control capable of
   falsifying the identities or count.

Do not infer density, nonemptiness, a parent theorem, or an asymptotic result
from the algebra.  Your report must use the seven-section repository report
contract.
