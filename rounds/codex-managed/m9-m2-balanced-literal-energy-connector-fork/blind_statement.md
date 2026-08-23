# Round 114 statement-only packet

This file is the complete mathematical context for the blind rederivation.
It is candidate data, not accepted proof state.

Let `e(t)=exp(2 pi i t)`, let `X>=4096` be real, and put `R=sqrt X`.
Fix one persistent balanced smooth block with positive scales `h asymp L`,
`k asymp K`, and `1<=K/L<=16`.  At the critical scale `L asymp R^(1/3)`.
Let `A(h,k)` be real, supported in fixed compact rescalings of those two
intervals, and uniformly bounded with its accepted smooth rescaled
derivatives.

Put `G_0=sqrt(L)/2`.  Let the finite smooth gcd atoms satisfy, on positive
integers,

\[
\sum_\sigma \psi_\sigma(g)=\eta(g/G_0),
\]

where `eta` is bounded, equals one below its inner cutoff, and vanishes
above a fixed multiple of `G_0`.  For `(u,v)=1`, define

\[
F_{\sigma,u,v}(t)=\vartheta_\sigma(t)
A(G_\sigma t u,G_\sigma t v).
\]

The exact quarter packet is

\[
\begin{aligned}
Q_\sigma(R)=
\sum_{(u,v)=1}\chi_4(u)\sum_{n\in\mathbb Z}\big[&
\widehat F_{\sigma,u,v}
(G_\sigma(n-R\sqrt{uv}-1/4))\\
-&\widehat F_{\sigma,u,v}
(G_\sigma(n-R\sqrt{uv}-3/4))\big],
\end{aligned}
\]

and Poisson summation gives the supplied exact identity

\[
Z(R):=\sum_\sigma G_\sigma Q_\sigma(R)=2iT_{\rm low}(R),
\]

\[
T_{\rm low}(R)=
\sum_{\substack{g,u,v\ge1\\(u,v)=1}}
\eta(g/G_0)\chi_4(g)\chi_4(u)
A(gu,gv)e(Rg\sqrt{uv}).
\tag{B114.1}
\]

Zero character values enforce odd `g,u`.  Equivalently, by the unique map
`g=gcd(h,k)`, `u=h/g`, `v=k/g`,

\[
T_{\rm low}(R)=\sum_{h,k\ge1}a(h,k)e(R\sqrt{hk}),
\quad
a(h,k)=\chi_4(h)\eta(\gcd(h,k)/G_0)A(h,k).
\tag{B114.2}
\]

The direct target is

\[
|Z(R)|\ll_\varepsilon L^{3/2}X^\varepsilon,
\quad\text{equivalently}\quad
|Z(R)|^2\ll_\varepsilon L^3X^\varepsilon.
\tag{B114.3}
\]

All high-gcd, exact-square, near-square, transform-error, hard-profile, and
isolated exact-square-boundary terms have separate owners.  They may not be
inserted into the smooth packet or counted again.  Distinct physical blocks
may not cancel.

Independently prove or refute the following proposed interfaces.

1. Expand `|T_low|^2` coefficientwise with both gcd lifts retained, and
   identify the true phase diagonal.  Decide whether it is `uv=u'v'` or the
   full equality `g^2uv=g'^2u'v'`, equivalently `hk=h'k'`.
2. Group the exact expansion by the full product difference
   `r=hk-h'k'`.  Bound the `r=0` contribution at the energy scale.
3. Test the two sufficient mean squares

   \[
   \sum_h\left|\sum_k b(h,k)e(R\sqrt{hk})\right|^2,
   \qquad
   \sum_k\left|\sum_h\chi_4(h)b(h,k)e(R\sqrt{hk})\right|^2,
   \]

   including the Cauchy cost, the required right side, the literal choice
   of `b`, and which orientation retains the character inside the modulus.
4. For two points `(h,k)` and `(h',k')=(h+p,k+q)`, test whether the
   determinant

   \[
   \rho=hk'-h'k=hq-kp
   \]

   is an exact transverse ray defect.  Derive an exact tangent-remainder
   identity for `sqrt(h'k')-sqrt(hk)` and determine the absolute capacity of
   `|rho|<=Q` for a lawful threshold `Q`.
5. Decide whether the different model identity for `f(u,m)=u^2/m` is by
   itself an exact connector to (B114.1).  Do not infer a connector from
   phase resemblance.

The report must distinguish the direct scalar energy, stronger Gram norms,
shellwise absolute values, and arbitrary-coefficient false shadows.  A
rigorous failure at any connector is a successful result.
