# Round 129 statement-only joint curvature problem

Let

\[
 W=Y^{7/16},\qquad D=Y^{1/2},\qquad L=Y^{1/6},
 \qquad D/L\le B\le D,
\]

and put

\[
 Q_B=\min\left(B,{BD\over WL}\right),\qquad
 J_B=1+{DQ_B\over B^2},\qquad
 \lambda_B={YL\over DB^2}.
\]

Fix integers \(a'\ne0\), \(\rho\mid a'\), and an interval \(I\) such
that \(b'=\rho v\asymp B\), the \(b'\)-length is at most \(Q_B\), and
\(|a'|\asymp LB/D\).  Let

\[
 f(v)=-{ca'\over\kappa\rho v}+\vartheta\rho v,
 \qquad c\asymp Y,
\]

where \(\kappa\in\{1,4\}\) and
\(\vartheta\in\{-1/4,0,1/4\}\).

Let \(P\) be supported on \(g\asymp G=D/B\), with zero-extended
supremum plus discrete variation \(O(1)\).  Let \(w\) be supported on
\(d\asymp D\), with zero-extended supremum plus discrete variation
\(O(1)\).  Put

\[
 c_t=w(t)-w(t+1),\qquad \sum_t|c_t|\ll1,
\]

and define the exact Stieltjes-character amplitude

\[
 U(v)=\tau(v)\sum_t c_t\,U_t(v),\qquad
 U_t(v)={1\over a'}
 \sum_{g\le t/(\rho v)}{\chi_4(g)\over g}P(g).
\]

Here \(\tau\) is supported on \(O(1)\) clipped subintervals and its zero
extension has bounded supremum plus total variation.  Literal endpoint
values are included.  It is already known, and may be used, that

\[
 \|U\|_{V^2(I)}
 \ll {J_B^{1/2}\over L},\qquad
 \|U\|_{V^2(I)}^2
 =|U(v_-)|^2+\sum_v|U(v+1)-U(v)|^2+|U(v_+)|^2.
\]

The question is whether the structured family uniformly satisfies

\[
 \left|\sum_{v\in I}^{*}U(v)e(f(v))\right|
 \ll_\varepsilon
 \|U\|_{V^2(I)}
 \min\left(
 N_\rho,\,
 N_\rho\sqrt{\lambda_B\rho^2}
(\lambda_B\rho^2)^{-1/2}
 \right)Y^\varepsilon,
\qquad N_\rho\asymp Q_B/\rho.
\]

First derive the exact dual norm and show what happens for arbitrary
\(V^2\) amplitudes.  Then prove or refute the displayed estimate for the
supplied Stieltjes-character threshold class.  A counterexample must obey
all of its hypotheses; a generic phase-adapted sequence is only a control.
Treat both endpoint values, all first-derivative integer crossings,
quarter-linear shifts, divisor progressions, threshold superposition, and
clipped multipliers.  No numerical or external theorem is allowed.

Even a proof would yield only a conditional fixed-block exponent
\(73/96\), not a global Gauss-circle exponent, M9 statement, or quarter
theorem.
