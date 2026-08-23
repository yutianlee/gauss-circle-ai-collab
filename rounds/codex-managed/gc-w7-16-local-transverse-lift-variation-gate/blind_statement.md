# Round 128 statement-only packet: local lift square variation

## Frozen abstract object

Let \(Y\ge2\),

\[
 W=Y^{7/16},\qquad D=Y^{1/2},\qquad L=Y^{1/6}.
\]

Fix a reduced-denominator shell \(D/L\ll B\ll D\) and define

\[
 Q_B=\min\!\left(B,\frac{BD}{WL}\right),\qquad
 J_B=1+\frac{DQ_B}{B^2},\qquad G=\frac DB.
\]

On a divisor progression \(b'=\rho v\), consider a finite interval
\(I\) of \(v\)-length \(N_\rho\asymp Q_B/\rho\) and

\[
 U_\rho(v)=
 \sum_{g\in I_\rho(v)}^{*}\chi_4(g)\,\omega_\rho(g,v).
\tag{128.B1}
\]

Here the star can give an endpoint half-weight.  The integer interval
\(I_\rho(v)\) has length at most \(G\); as \(v\) runs through \(I\), its
floor endpoints have at most \(O(J_B)\) births or exits.  Assume only the
displayed information unless an additional hypothesis is explicitly
introduced and justified.

Define

\[
 \|U_\rho\|_{V^2(I)}^2
 =|U_\rho(v_-)|^2+
 \sum_{v,v+1\in I}|U_\rho(v+1)-U_\rho(v)|^2
 +|U_\rho(v_+)|^2.
\tag{128.B2}
\]

The proposed bound is

\[
 \boxed{
 \|U_\rho\|_{V^2(I)}
 \ll_\varepsilon \frac{J_B^{1/2}}L Y^\varepsilon.}
\tag{128.B3}
\]

## Assignment

Determine whether (128.B3) follows from a moving-endpoint birth count,
the common lift character, and a natural coefficient scale
\(|\omega_\rho(g,v)|\ll L^{-1}Y^\varepsilon\).  If not, give the sharpest
countermodel and formulate minimal additional hypotheses on the
\(g\)-variation, \(v\)-variation, endpoint values, or factorization of
\(\omega_\rho\) under which (128.B3) is rigorously true.

Treat separately:

1. fixed endpoint values in (128.B2);
2. births and exits of \(I_\rho(v)\);
3. continuous or every-step changes of \(\omega_\rho(g,v)\);
4. the order in which \(\chi_4(g)\) cancellation and absolute values are
   used;
5. adversarial phase-conjugating weights and weights of bounded sampled
   variation;
6. the difference between local \(J_B\) and full lift length \(G\).

At the critical longest-lift shell, \(J_B=Y^{1/16+o(1)}\).  A local loss
\(J_B^\theta/L\) has strict conditional capacity only for
\(\theta<2/3\).  The natural square-variation exponent is \(1/2\).

This assignment concerns only the coefficient norm.  It does not ask for
the subsequent oscillatory curvature inequality, does not prove a graded
correlation estimate, and changes no Gauss-circle exponent or M9 status.
