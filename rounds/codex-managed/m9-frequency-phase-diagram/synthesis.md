# Round 5 synthesis: M2 frequency phase diagram

## Closing decision

**ACCEPT A PRIMARY-SOURCED EXPONENT-PAIR WEDGE; ACCEPT THE SMOOTH
POISSON DUALITY AS AN EQUIVALENT FORMULATION; REJECT TWO-SHIFT CANCELLATION
AND UNWEIGHTED PRODUCT GROUPING AS CORRIDOR SOLUTIONS.**

The round enlarges the pointwise region proved at the conjectural exponent,
but it does not prove the full M2 estimate. No numerical experiment was used.

## Parameter triangle and elementary baseline

Write

\[
D=X^\delta,\qquad L=X^\ell,\qquad
\Omega=\left\{(\delta,\ell):
\frac14\leq\delta\leq\frac12,\quad
0\leq\ell\leq\delta-\frac14\right\}.
\]

For a target \(X^{\vartheta+\varepsilon}\), the accepted estimates have exact
exponents

\[
\begin{array}{c|c}
\mathrm{T2S}&\delta-\ell\\
\mathrm{second\ derivative}
&(1+\ell-\delta)/2,\quad(3\delta-1-\ell)/2\\
\mathrm{trivial}&\delta\\
\mathrm{exponent\ pair}\ (\kappa,\lambda)
&\kappa(1+\ell-2\delta)+\lambda\delta,
\quad 2\delta-1-\ell.
\end{array}
\]

At \(\vartheta=1/4\), the first three estimates cover exactly the terminal
line \(\ell=\delta-1/4\) and the isolated point
\((\delta,\ell)=(1/2,0)\).

## Certified Tao--Trudgian--Yang wedge

The primary-source theorem in Tao--Trudgian--Yang, arXiv:2501.16779, proves
the exponent pair

\[
(\kappa,\lambda)
=\left(\frac{89}{1282},\frac{997}{1282}\right).
\]

For \(h\asymp L\), complex conjugation puts the reciprocal phase in their
model class with

\[
N=D,\qquad T\asymp \frac{hX}{D},\qquad
F(u)=-u^{-1},\qquad F'(u)=u^{-2}.
\]

For a denominator profile satisfying the uniform discrete BV condition

\[
\sup_d|w_D(d)|+\sum_d|w_D(d+1)-w_D(d)|\ll1,
\]

partial summation gives

\[
|B_L(D;X)|
\ll_\varepsilon
X^{[89(1+\ell)+819\delta]/1282+\varepsilon}.
\]

Hence the project target holds in the exact wedge

\[
\boxed{178\ell+1638\delta\leq463.}
\]

This covers every frequency block through

\[
\delta\leq\frac{1015}{3632}=0.279460\ldots
\]

and a nonempty lower-frequency slice through

\[
\delta\leq\frac{463}{1638}=0.282662\ldots.
\]

The project transfer remains conditional only on writing the actual dyadic
and endpoint profiles with the displayed normalized BV bound. Arbitrary
bounded weights are not covered.

Combining this wedge with T2S and the second-derivative endpoint leaves

\[
\boxed{
\mathcal U=
\left\{(\delta,\ell)\in\Omega:
0\leq\ell<\delta-\frac14,\quad
178\ell+1638\delta>463
\right\}
\setminus\left\{\left(\frac12,0\right)\right\}.}
\]

## Exact two-shift kernel and sharpness scope

The two shifts are a parity projector:

\[
e(h\theta)-e(h(\theta+1/2))
=(1-(-1)^h)e(h\theta).
\]

They reinforce every surviving odd frequency rather than cancel it. Pairing
the positive and negative frequencies gives the exact sine-kernel identity

\[
S_{2,L}
=4\sum_{d\asymp D}w_D(d)\chi_4(r_d)
\sum_{\substack{h>0\\h\ {\rm odd}}}
a_{h,H,L}\sin\!\left(\frac{\pi h(X-dr_d)}{2d}\right),
\]

where \(r_d\) is a nearest odd integer to \(X/d\) and
\(a_{h,H,L}=v_L(h)\Phi(h/(H+1))/(2\pi h)\).

Thus the full two-sided block vanishes at exact product resonance
\(X=dr_d\), but the first annulus

\[
|X-dr_d|\asymp D/L
\]

has constant kernel size. A rigorous coherent-family construction shows
that, for some \(X\asymp Y\), a bounded nonnegative sparse denominator
weight with the actual Vaaler amplitudes satisfies

\[
|S_{2,L}(D;X)|\gg D/L.
\]

Therefore no improvement over T2S can hold uniformly for arbitrary bounded
denominator weights. The adversarial weight has variation
\(\gg D/L\), so this does not obstruct the fixed normalized-BV project
profile.

## Smooth Poisson transform and exact dual target

For \(W\in C_c^\infty((a,b))\), Poisson summation and uniform stationary
phase give, for \(h>0\),

\[
\sum_d W(d/D)e\!\left(\frac{hX}{4d}\right)
=\frac{e(1/8)(hX)^{1/4}}2
\sum_{k\geq1}
\frac{W(\sqrt{hX/(4kD^2)})}{k^{3/4}}
e(\sqrt{hXk})+O_W(1).
\]

The zero mode, nonstationary modes, support crossings, and the transition
\(K\asymp1\) are controlled under the smooth-support hypothesis.

Put

\[
K=\frac{XL}{D^2},\qquad M=LK=\frac{XL^2}{D^2}.
\]

For the positive-frequency Vaaler block the transform becomes

\[
\boxed{
\mathcal B^+_{L,W}
=-\frac{e(1/8)}{2\pi}
X^{1/4}M^{-3/4}\mathcal T_{L,K}+O_W(1),}
\]

where

\[
\mathcal T_{L,K}
=\sum_{h\asymp L}\sum_{k\asymp K}
\chi_4(h)a_{L,K}(h,k)e(\sqrt{Xhk})
\]

has the actual smooth slanted symbol. Consequently

\[
\mathcal T_{L,K}\ll_\varepsilon M^{3/4}X^\varepsilon
\]

is equivalent, up to the transform error, to the positive smooth block
target \(X^{1/4+\varepsilon}\). It is an exact dual formulation, not an
easier consequence.

Grouping by \(m=hk\) produces

\[
\mathcal T_{L,K}
=\sum_{m\asymp M}c_{L,K}(m)e(\sqrt{Xm}),\qquad
c_{L,K}(m)=
\sum_{\substack{h\mid m\\h\asymp L\\m/h\asymp K}}
\chi_4(h)a_{L,K}(h,m/h).
\]

This is an irregular localized divisor coefficient. An unweighted
one-dimensional derivative theorem cannot be applied to it by partial
summation. Elementary one-variable differencing adds no open region beyond
the baseline wedge and endpoint sets.

A stronger, character-erasing Cauchy interface would be

\[
\sum_{h\asymp L}
\left|\sum_{k\asymp K}
a_{L,K}(h,k)e(\sqrt{Xhk})\right|^2
\ll_\varepsilon L^{1/2}K^{3/2}X^\varepsilon.
\]

It is exactly diagonal-critical when \(K=L\), namely on the
\(D=X^{1/2}\) edge. It remains unproved and is stronger than the signed
dual target.

## Research conclusion

Round 5 changes the active problem from the full parameter triangle to the
explicit corridor \(\mathcal U\). The next proof must exploit one of:

1. cancellation of the actual normalized-BV denominator profile in the
   sine-kernel form;
2. the \(\chi_4(h)\) sign before Cauchy in the dual product-phase sum; or
3. a genuinely coefficient-sensitive square-root spacing theorem.

Two-shift residue pairing, arbitrary-weight improvements of \(D/L\), and
coefficient-free product grouping are now rejected. M9-M2 remains open.

## Evidence ledger

- Exact elementary phase diagram:
  reports/blind_phase_diagram.md
- Exact sine kernel, bounded-weight sharpness, and hostile pair audit:
  reports/hybrid_corridor_hostile.md
- Smooth Poisson transform and equivalent dual target:
  reports/dual_three_quarter_attack.md
- Conductor primary-source and region audit:
  reviews/conductor_primary_source_and_region_audit.md
- Primary source card:
  sources/tao_trudgian_yang_2025.md

