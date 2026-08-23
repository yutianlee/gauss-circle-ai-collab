# Round 117 derivation packet: determinant fibres and character high-pass

Campaign: gc-w7-16-actual-determinant-fibre-gate

Starting graph SHA-256:
`a27a89fd4e688cae719a28fec8f48dd74190bafb64d0345c590f1caadc2805d9`.

## 1. Accepted bridge and literal kernel

At (W=Y^{7/16}), a uniform fixed-stratum cluster bound

\[
 \mathcal C_i(c)\ll_\varepsilon Y^{1/2+\varepsilon}
\]

for every literal M1/M2 block gives local square mass
(Y^{15/16+\varepsilon}) and hence

\[
 P(X)\ll_\varepsilon X^{5/16+\varepsilon}.
\]

This would improve both the internal (1/3) and the audited external
(0.3144831759740614\ldots), but it would not prove M9 or the quarter
theorem.

After reducing (h/d=a/b) and summing all lifts, the exact coefficients
satisfy

\[
 |A_i(a,b)|\ll_\varepsilon L^{-1}Y^\varepsilon,
 \qquad
 \sum|A_i(a,b)|^2\ll_\varepsilon {D\over L}Y^\varepsilon.
\tag{117.D1}
\]

The complete equal-lift diagonal is therefore owned. The open one-sided
correlation is

\[
 \mathfrak O_i=2\Re
 \sum_{0<n=ab'-a'b<\kappa_i bb'/W}
 A_i(a,b)\overline{A_i(a',b')}
 e\!\left({cn\over\kappa_i bb'}\right)
 \left(1-{Wn\over\kappa_i bb'}\right),
\tag{117.D2}
\]

where (kappa_1=1), (kappa_2=4). Every sign, profile, floor, hard
top, star, and moving-symbol stratum remains.

The complete lift formulas are

\[
 A_1(a,b)={2\chi_4(b)\over\pi i a}
 \sum_g{\chi_4(g)\over g}U_{1,a,b}(g),
\qquad
 A_2(a,b)=-{4\chi_4(|a|)\over\pi|a|}
 \sum_g{\chi_4(g)\over g}U_{2,a,b}(g).
\tag{117.D3}
\]

The lift transforms in (117.D3) are actual sampled-BV sums in (g).
Round 95 proves their individual and square bounds, but does not prove
smooth variation in (a) or (b).

## 2. Accepted capacity frontier

Coefficient-blind Farey spacing gives

\[
 \mathcal C_i\ll_\varepsilon {D\over L}
 \left(1+\min\left(DL,{D^2\over W}\right)\right)Y^\varepsilon.
\tag{117.D4}
\]

It is target-safe outside

\[
 \mathscr H_{95}=\{(\delta,\ell):
 1/4\le\delta\le1/2,\ 0\le\ell\le\delta-1/4,\
 3\delta-\ell>15/16\}.
\]

At the minimax point ((D,L)=(Y^{1/2},Y^{1/6})), (117.D4) is
(Y^{43/48+\varepsilon}); the target is (Y^{24/48+\varepsilon}).
A phase-conjugated coefficient array attains the former scale, so any
saving must use the literal phase or coefficients.

Popov's full local discrepancy ceiling gives divided cluster capacity
(Y^{1/2}+Y^{9/16}\log^2Y). It cannot be reversed into a positive
fixed-block estimate. A strict exponent improvement through persistence
requires a complete cluster exponent below (9/16); the full Round-117
target is (1/2).

## 3. Exact increment and character chart

Put

\[
 a'=a+p,\qquad b'=b+q.
\]

Then

\[
 n=ab'-a'b=aq-bp,
\tag{117.D5}
\]

and

\[
 {cn\over\kappa_i b(b+q)}
 ={c\over\kappa_i}\left({a\over b}-{a+p\over b+q}\right).
\tag{117.D6}
\]

For M1, nonzero terms have (b,b') odd, so (q=2r) and

\[
 \chi_4(b)\chi_4(b')=(-1)^r.
\tag{117.D7}
\]

For M2, nonzero same-sign terms have (a,a') odd, so (p=2s) and

\[
 \chi_4(|a|)\chi_4(|a'|)=(-1)^s.
\tag{117.D8}
\]

Thus the M1 character high-pass lies in the denominator increment, while
the M2 high-pass lies in the numerator increment. These identities do not
control the remaining lift transforms in (117.D3).

## 4. Reduced-denominator shell ledger

Split (b,b'\asymp B\le D). On a same-sign interior shell,

\[
 |a|,|a'|\asymp A:={LB\over D},
 \qquad
 N_B:={B^2\over W}.
\tag{117.D9}
\]

The determinant strip (0<n\ll N_B) has the two exact local widths

\[
 q\text{-width at fixed }p:\quad
 Q_B\asymp {N_B\over A}={BD\over WL},
\tag{117.D10}
\]

\[
 p\text{-width at fixed }q:\quad
 P_B\asymp {N_B\over B}={B\over W}.
\tag{117.D11}
\]

At (B=D=Y^{1/2}), (L=Y^{1/6}),

\[
 N_B=Y^{9/16},\qquad Q_B=Y^{19/48},\qquad P_B=Y^{1/16}.
\tag{117.D12}
\]

The ray energy on this (B)-shell is at most

\[
 {B^2\over DL}Y^\varepsilon,
\tag{117.D13}
\]

and the coefficient-blind off-diagonal capacity is

\[
 {B^4\over DLW}Y^\varepsilon,
\tag{117.D14}
\]

dominated by (B=D). Any proof that uses (117.D10)--(117.D14) must keep
the congruence (aq-bp=n), primitivity of both rays, the triangular
weight, and the literal variation of (117.D3).

## 5. Transform diagnostic

For fixed (a,b), the phase in ((p,q)) is

\[
 \phi(p,q)={c\over\kappa_i}
 \left({a\over b}-{a+p\over b+q}\right).
\]

It is exactly linear in (p), while

\[
 \det\nabla^2_{p,q}\phi
 =-{c^2\over\kappa_i^2(b+q)^4}.
\tag{117.D15}
\]

At the top shell (B\asymp Y^{1/2}), this determinant is order one.
Consequently an unqualified two-dimensional B-process is a likely
capacity-preserving transform, not automatically a saving. The character
half-shifts one dual coordinate. This is a diagnostic to prove or refute,
not an accepted obstruction.

For fixed (q), the (p)-phase has frequency
(-c/(\kappa_i(b+q))). A geometric-sum estimate on the short
(P_B=B/W) strip suggests a reciprocal product-window count, but any
gain must survive the (q,a,b) sums and the nonsmooth lift coefficient.

## 6. Required outcome

The round must produce a complete actual bound, strict target-safe block
region, quantified saving, or a rigorous scoped no-go. Identities alone
do not change the graph. No determinantwise, raywise, or character-sector
absolute value may be hidden, and no block result may be promoted as M9 or
the quarter theorem.
