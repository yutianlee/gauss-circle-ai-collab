# Round 129 conductor adjudication: direct birth-block curvature closes the long-lift shell seam

Campaign: `gc-w7-16-joint-stieltjes-reciprocal-curvature-gate`

Starting graph SHA-256:
`476b1445ef73d86627fd87de8bd2dd76a5efa53564a5b195230f2ad33ba2bbe8`

## 1. Decision

Promote the direct character/Stieltjes theorem, not the proposed
norm-relative theorem.  For each exact character-split M1/M2 package and
each divisor progression, put

\[
 \Lambda_\rho=\lambda_B\rho^2,\qquad
 N_\rho\asymp Q_B/\rho,\qquad
 K_\rho=\min\!\left(N_\rho,
 N_\rho\sqrt{\Lambda_\rho}+\Lambda_\rho^{-1/2}\right).
\]

Then the literal physical sum satisfies

\[
 \boxed{
 \left|\sum_{v\in I}^{*}U_{i,\rho,\eta}(v)
 e\!\left(-{ca'\over\kappa_i\rho v}
          +\vartheta_{i,\eta}\rho v\right)\right|
 \ll_\varepsilon {K_\rho\over L}Y^\varepsilon .}
 \tag{129.J1}
\]

Here \(\vartheta_{1,\pm}=\pm1/4\),
\(\vartheta_{2,0}=0\), \(\kappa_1=1\), and \(\kappa_2=4\).
The proof is thresholdwise and absolute in the fixed Stieltjes mass; it
does not assert

\[
 |S(U)|\ll \|U\|_{V^2}K_\rho Y^\varepsilon.
 \tag{129.J2}
\]

In fact (129.J2) is false for the displayed abstract BV-threshold class.
The blind and hostile audits independently give a one-lift stationary-
alias triangle for which the ratio in (129.J2) fails by \(Y^{1/48}\).
This no-go is compatible with (129.J1), whose right side uses the fixed
Stieltjes mass rather than the potentially smaller norm of the completed
coefficient.

After the already audited outer ledger, (129.J1) proves for the complete
critical fixed block, uniformly over every reduced-denominator shell,

\[
 \boxed{|\mathfrak O_i|\ll_\varepsilon
 Y^{35/48+\varepsilon}.}
 \tag{129.J3}
\]

This extends the previously top-shell-only \(Y^{35/48}\) estimate to all
\(D/L\le B\le D\).  It improves the former complete
\(Y^{37/48}\) envelope by \(Y^{1/24}\), and is stronger than the
Round-127 conditional \(Y^{73/96}\) forecast.

## 2. Exact threshold kernel

Round 128 gives, before any norm, the exact branch formula

\[
 U(v)=\zeta_{i,\rho,\eta}T_i(v)
 \sum_t c_{i,t}
 \sum_{g\le t/(\rho v)}^{*}{\chi_4(g)\over g}P_{i,a'}(g),
 \qquad \sum_t|c_{i,t}|\ll1.
 \tag{129.J4}
\]

The zero-extended frequency factor \(P_{i,a'}\) is sampled BV on
\(g\asymp G=D/B\), \(|a'|G\asymp L\), and \(T_i\) is the exact
bounded-BV product of the triangular determinant taper, clipped
determinant interval, fixed cell and sign sector, and half-open shell
owner.  The two M1 reduced-character branches have already been moved
into the phases \(e(\pm\rho v/4)\); the M2 reduced character is fixed.

Fix one threshold \(t\).  On every plateau of

\[
 M_t(v)=\left\lfloor {t\over\rho v}\right\rfloor,
\]

character Abel summation is performed before a modulus and gives

\[
 \left|{\zeta_{i,\rho,\eta}}
 \sum_{g\le M}^{*}{\chi_4(g)\over g}P_{i,a'}(g)\right|
 \ll_\varepsilon L^{-1}Y^\varepsilon.
 \tag{129.J5}
\]

There are

\[
 R_t\ll 1+{DQ_B\over B^2}=J_B
 \tag{129.J6}
\]

nonempty plateaux, and their total length is at most \(N_\rho\).  The
weighted second-derivative estimate on each plateau, uniform at every
integer first-derivative crossing and both M1 quarter aliases, gives

\[
 {1\over L}\min\!\left(
 N_\rho,
 N_\rho\sqrt{\Lambda_\rho}
 +J_B\Lambda_\rho^{-1/2}\right)Y^\varepsilon.
 \tag{129.J7}
\]

The endpoint count in (129.J7) is absorbed without Cauchy.  With
\(J_{0,B}=J_B-1=DQ_B/B^2\), the critical scales give

\[
 {N_\rho\Lambda_\rho\over J_{0,B}}\asymp L\rho,
 \qquad
 N_\rho\Lambda_\rho\asymp {Y\rho\over WB}
 \ge {D\over W}=Y^{1/16}.
 \tag{129.J8}
\]

If \(J_{0,B}\ge1\), (129.J8) implies
\(J_B\ll N_\rho\Lambda_\rho\); if \(J_{0,B}<1\), then
\(J_B\asymp1\) and the second part of (129.J8) gives the same
absorption.  Hence (129.J7) is at most \(K_\rho/L\).

Exact discrete Stieltjes recombination now costs only
\(\sum_t|c_{i,t}|\ll1\), proving (129.J1).  This ordering is essential:
character Abel first, reciprocal curvature on literal floor plateaux
second, and Stieltjes Minkowski last.

## 3. Literal equality, divisor, and owner seams

Strict, weak, or half-star threshold equality differs from the weak
plateau formula only at points \(t=\rho vg\).  For fixed \(t\) these are
divisor pairs of \(t\); (129.J5) and the divisor bound give a total
residual \(O_\varepsilon(L^{-1}Y^\varepsilon)\) after summing the
Stieltjes mass.  Outer endpoint stars are already in the weighted
second-derivative estimate.  Thus no floor or equality term is omitted.

The proof is uniform for each \(\rho\mid a'\) after the accepted
nonprimitive extension.  Summing divisors after (129.J1) gives

\[
 \sum_{\rho\mid a'}K_\rho
 \ll_\varepsilon K_B Y^\varepsilon,
 \qquad
 K_B=\min\!\left(Q_B,
 Q_B\sqrt{\lambda_B}+\lambda_B^{-1/2}\right).
 \tag{129.J9}
\]

The physical \(Q_B\)-window meets only \(O(1)\) adjacent half-open
\(B\)-owners.  The original denominator profile remains inside (129.J4),
so no inner coefficient or outer ray is duplicated.

## 4. Complete fixed-block assembly

The accepted complete cross-shell ledger has
\(O(LD)\) outer rays, \(O(L)\) inner numerator increments, outer
coefficient \(O(L^{-1})\), and the inner estimate
\(O(L^{-1}K_B)\).  Therefore

\[
 (LD)\cdot L\cdot L^{-1}\cdot L^{-1}K_B=DK_B.
 \tag{129.J10}
\]

For \(B=Y^b\), \(1/3\le b\le1/2\),

\[
 Q_B=Y^{b-5/48},\qquad
 \lambda_B=Y^{2/3-2b},\qquad
 Q_B\sqrt{\lambda_B}=Y^{11/48},\qquad
 \lambda_B^{-1/2}\le Y^{1/6}.
 \tag{129.J11}
\]

Thus \(K_B\ll Y^{11/48+o(1)}\) uniformly.  Logarithmically many
half-open shells and the equality residual are absorbed in
\(Y^\varepsilon\), proving (129.J3).

## 5. Exact norm obstruction

For the endpoint-inclusive norm

\[
 \|u\|_{V^2}^2=|u_1|^2+
 \sum_{j<N}|u_{j+1}-u_j|^2+|u_N|^2,
\]

the exact dual is the square root of the variance of all prefix sums.
Equivalently, its squared kernel is

\[
 (L_N^{-1})_{jk}={\min(j,k)(N+1-\max(j,k))\over N+1}.
 \tag{129.J12}
\]

At a reciprocal integer-derivative alias on a one-lift top-shell packet,
a real triangular sampled-BV profile of coherent width
\(\Lambda^{-1/2}\) has both endpoint values zero and violates (129.J2)
by \(Y^{1/48}\).  Hence no proof may replace the fixed Stieltjes mass in
(129.J1) by the completed \(V^2\) norm under the displayed abstract
hypotheses.  The no-go rejects only that normalization; it does not weaken
the direct physical theorem.

## 6. Scope and state decision

Promote (129.J1), the all-shell fixed-block consequence (129.J3), and the
norm-relative obstruction (129.J12 plus its structured alias packet).
Revise the Round-127 connector from a conditional norm statement to the
proved direct theorem.  Retain the full determinant target
\(Y^{1/2+\varepsilon}\) open: (129.J3) is still larger by
\(Y^{11/48}\).

Under the accepted persistence map, even a complete correlation exponent
\(35/48\) gives \(7/18>1/3\), so there is no global exponent change.
M9-M1, M9-M2, endpoint uniformity, M9, the conditional bridge, and the
quarter target remain unchanged.  The campaign used no computation or
external result.

