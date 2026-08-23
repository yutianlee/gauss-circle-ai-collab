# Conductor Round-114 review: literal energy and target-safe corridors

Campaign: `m9-m2-balanced-literal-energy-connector-fork`
Starting recorded graph: `411adc0c93d2451dfc1235840f27063b3ef4869d0c67aebfbbc74fe9ef04387c`

## Decision

The three reports independently validate the full-product correction and
the two elementary corridor bounds.  Promote these facts as a proved
reduction, not as the balanced estimate.

For one literal Round-113 block put

\[
a_B^<(h,k)=\chi_4(h)
\eta\!\left(\frac{\gcd(h,k)}{\sqrt L/2}\right)A_B(h,k).
\]

The exact smooth gcd telescope and quarter-shift identity give

\[
Z_B(R):=\sum_\sigma G_\sigma Q_{B,\sigma}^{\rm full}(R)
=2i\sum_{h,k}a_B^<(h,k)e(R\sqrt{hk}).
\tag{114.R1}
\]

This is an exact coefficientwise recombination before any modulus.  It is
not a shellwise triangle inequality and does not discard either quarter
shift.

## Full-product diagonal

After squaring (114.R1), the phase diagonal is

\[
hk=h'k',
\]

or `g^2uv=g'^2u'v'` in primitive coordinates.  The strategy-memo shadow
`uv=u'v'` is not literal because it drops both live gcd lifts.

With

\[
c_B(n)=\sum_{hk=n}a_B^<(h,k),
\]

the equal-product contribution is

\[
E_0=\sum_n|c_B(n)|^2.
\]

Since `|a_B^<|<<1`, there are `O(LK)=O(L^2)` atoms, and every product
fibre has divisor multiplicity `O_epsilon(X^epsilon)`, Cauchy on each
fibre gives

\[
E_0\ll_\varepsilon L^2X^\varepsilon.
\tag{114.R2}
\]

Thus the genuine phase diagonal has one factor of `L` of room inside the
`L^3` energy budget.

## Radial and determinant corridors

For two atoms define

\[
\Delta=h'k'-hk,
\qquad
\rho=hk'-h'k.
\]

The radial count is

\[
\#\{|\Delta|\le U\}
\le\sum_{n\asymp L^2}\tau(n)
\sum_{|r|\le U}\tau(n+r)
\ll_\varepsilon L^2(U+1)X^\varepsilon.
\tag{114.R3}
\]

For the determinant count, fix `(h,k)`, put `d=gcd(h,k)`, and solve

\[
hk'-h'k=\rho.
\]

For nonzero `rho` there are no solutions unless `d|rho`; when one exists,
all solutions differ by `(h/d,k/d)`, so a fixed support box contains
`O(1+d)` of them.  Summing over base points of gcd `d` gives, for fixed
nonzero `rho`,

\[
O\!\left(L^2\sum_{d\mid\rho}(d^{-2}+d^{-1})\right)
\ll_\varepsilon L^2X^\varepsilon.
\]

The zero determinant costs `O(L^2 log L)`.  Therefore

\[
\#\{|\rho|\le Q\}
\ll_\varepsilon L^2(Q+1)X^\varepsilon.
\tag{114.R4}
\]

Equations (114.R3)--(114.R4) remain true for the absolute weighted masses.
Taking `U=Q=L` shows that

\[
\mathcal N_B={|\Delta|\le L\}\cup\{|\rho|\le L\}
\tag{114.R5}
\]

is target-safe at energy `L^3X^epsilon`.

## Literal ray identity

Writing `(h',k')=(h+p,k+q)`, direct rationalization gives

\[
\sqrt{h'k'}-\sqrt{hk}
-\frac12\sqrt{\frac kh}p
-\frac12\sqrt{\frac hk}q
=-\frac{\rho^2}
{4(hk)^{3/2}(P+\sqrt{Q_0})},
\tag{114.R6}
\]

where `P=1+(p/h+q/k)/2` and
`Q_0=(1+p/h)(1+q/k)`.  This is the lawful square-root-cone connector.
The model identity for `u^2/m` remains only an analogy unless separately
mapped to these atoms.

The exact companion chart

\[
\Delta+\rho=q(h+h'),
\qquad
\Delta-\rho=p(k+k')
\tag{114.R7}
\]

shows divisor-bounded multiplicity for fixed generic `(Delta,rho)`.  It
does not lower global capacity because the invariant pair ranges over a
two-dimensional `L^4` family.

## Smallest survivor

Removing (114.R5), and harmlessly assigning the coordinate-parallel axes
to the target-safe side, leaves the real actual-symbol energy

\[
\mathcal E_{B,\rm df}
=\sum_{|r|>L}\sum_n e\!\left(R(\sqrt n-\sqrt{n+r})\right)
\sum_{\substack{hk=n,\ h'k'=n+r\\|hk'-h'k|>L}}
a_B^<(h,k)\overline{a_B^<(h',k')}.
\tag{114.R8}
\]

Up to the proved target-safe corridors, the balanced packet follows from

\[
\mathcal E_{B,\rm df}\ll_\varepsilon L^3X^\varepsilon.
\tag{114.R9}
\]

This estimate is open.  Large determinant supplies no oscillation inside
a fixed product pair because the outer phase in (114.R8) depends only on
`n` and `r`.  A phase-adapted bounded coefficient array has double-far
energy of order `L^4`, so generic geometry and divisor multiplicity cannot
prove (114.R9).  The next mechanism must use the literal smooth symbol and
the signed twisted-divisor coefficient.

## Scope

The proved content is (114.R1)--(114.R7) and the target-safe reduction to
(114.R8).  It closes neither (114.R9) nor the balanced parent, and it makes
no change to TOP, UNBAL, M1, endpoint uniformity, M9, or any exponent.
