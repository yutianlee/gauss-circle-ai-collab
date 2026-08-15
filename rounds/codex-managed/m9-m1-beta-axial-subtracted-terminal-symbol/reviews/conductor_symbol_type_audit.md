# Conductor audit: the Round-39 symbol has three distinct normalizations

Campaign: `m9-m1-beta-axial-subtracted-terminal-symbol`  
Role: conductor definition and normalization review  
Allocation: 100% analytical/algebraic

The target must distinguish three objects.

First, after the signed top delta/PV limit, constant-numerator face log,
and axial extraction, the separated pre-stationary two-denominator kernel
is

\[
K_{R_1}(L,\nu)
=-\frac{i f_b(L)}{2A\{A+i(L-\nu)/2\}}
+\frac{f_b(\nu)-f_b(L)}
{(L-\nu)\{A+i(L-\nu)/2\}},
\tag{39.C1}
\]

where \(A=\rho_0-i(L+\beta)\).  On a separated saddle
\(|L|\asymp|A|\asymp\lambda\), this is the object with

\[
|K_{R_1}(L,\nu)|\ll_b\lambda^{-2}w_b(\nu),\qquad
|\partial_LK_{R_1}(L,\nu)|\ll_b\lambda^{-3}w_b(\nu),
\tag{39.C2}
\]

where \(\partial_L\) holds physical \(\nu\) fixed.

Second, stationary phase and the post-endpoint radial numerator multiply
(39.C1) by

\[
\frac{D_j}{q}\lambda .
\tag{39.C3}
\]

Consequently (39.C2) becomes local coefficient capacity

\[
\frac{D_j}{q\lambda}
=\frac{D_j}{q^2\theta_j(x)},
\qquad
\lambda=q\theta_j(x),\quad
\theta_j(x)=\frac{\pi\sqrt{Xx}}{D_j}.
\tag{39.C4}
\]

Third, a full beta contribution additionally contains the inherited
\(h,D_j,x\) monomial, scale/profile/floor/star weights, the \(j,h,q,x\)
sums or integrals, and the external
\(-4X^{1/4}\Re(e(1/8)\,\cdot)/\pi\).  These factors do not belong inside
the bare pre-stationary inequality (39.C2).

Accordingly, a claim that one and the same \(K_{\rm term}^\circ\) both
satisfies (39.C2) and already includes all inherited factors is
ill-normalized unless those factors have first been divided out explicitly.
Round 39 must either:

1. define \(K_{\rm term}^\circ\) as the normalized pre-stationary kernel
   and prove (39.C2), then state a separate summation lemma for (39.C3)--
   (39.C4); or
2. define a full amplitude and replace the right side of (39.C2) by the
   exact inherited monomial times \(D_j/(q\lambda)\).

The accepted fixed-height kernel and Round-38 limit settle neither this
normalization choice nor the full quantitative summation.  They do show
that boundary modules, radial sides, artificial/axial residues, and the
global height limit no longer obstruct making the definition.

No computation or external theorem is used.
