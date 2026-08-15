# Round 74 derivation packet: the exact top (M2) affine cone

## 1. Frozen quantity and normalization

Let

\[
 y=\lfloor\sqrt X\rfloor,\qquad q_X=X/y^2,
 \qquad H=\lfloor yX^{-1/4}\rfloor,
\]

and let (1\leq L\leq H) be dyadic.  Fix the accepted smooth dyadic
frequency cutoff (\eta_L), the Vaaler function (\Phi), and the accepted
top denominator profile (W), with

\[
 W(u)=0\quad(u\leq1/2),\qquad W(1)=1,
 \qquad W(u)=1\quad(2/3\leq u\leq1).
\]

The exact normalized symbol is

\[
 a_{L,H,X}(h,m)=
 \eta_L(h)\Phi\!\left(\frac{h}{H+1}\right)
 \left(\frac{L^2}{hm}\right)^{3/4}
 W\!\left(\sqrt{\frac{q_Xh}{4m}}\right).
 \tag{74.1}
\]

The frozen target is

\[
 \boxed{
 \mathcal T_L^{\rm end}
 =\sum_{\substack{h\asymp L\\h\ \mathrm{odd}}}
   \sum_{\lceil h/4\rceil\leq m\leq h}
   \chi_4(h)a_{L,H,X}(h,m)e(\sqrt{Xhm})
 \ll_\varepsilon L^{3/2}X^\varepsilon.}
 \tag{74.2}
\]

The exact one-sided transform is

\[
 \sum_{d\leq y}W(d/y)e(hX/(4d))
 =\frac{e(hX/(4y))}{1-e(hX/(4y^2))}
 +\frac{e(1/8)(hX)^{1/4}}2
  \sum_{m=\lceil h/4\rceil}^{h}
  W\!\left(\sqrt{\frac{q_Xh}{4m}}\right)
  m^{-3/4}e(\sqrt{Xhm})
 +O_W(\log(2+h)).
 \tag{74.3}
\]

After the actual (M2) factor is restored, the positive stationary dyadic
block is

\[
 -\frac{2e(1/8)}\pi X^{1/4}L^{-3/2}
 \mathcal T_L^{\rm end}.
 \tag{74.4}
\]

The negative frequency is the conjugate, and the full block is twice the
real part.  The endpoint and transform errors are already target-safe.
Thus (74.2), with the external factor in (74.4) counted exactly once, is
the complete top-endpoint analytic obligation.

## 2. Exact support and inherited closed slices

On (74.2), (h\asymp m\asymp L).  The lower boundary
(m=\lceil h/4\rceil) is hard and has (W(1)=1); it is not licensed by a
smooth full-line Poisson formula.  The upper edge (m=h) lies at the flat
support onset (W(1/2)), with the actual (q_X-1=O(X^{-1/2})) retained.

The accepted direct two-shift theorem already proves the original top
denominator block when (L\asymp H\asymp X^{1/4}).  Combined with
(74.3), it proves (74.2) in that terminal dyadic slice.  Bounded (L) is
trivial.  The new issue is the uniform intermediate range

\[
 1\ll L\ll H.
 \tag{74.5}
\]

No cancellation with the (M1) top cone may be used: the two stationary
constants have the same sign, their Vaaler factors lie on different
variables, and (M1) has an unmatched outer wing.

## 3. Exact shear of the hard affine edge

Put

\[
 r=4m-h.
\]

Then (r) is positive and odd,

\[
 1\leq r\leq3h,\qquad r\equiv-h\pmod4,
 \qquad m=(h+r)/4.
 \tag{74.6}
\]

For odd (h,r), the congruence projector and its character-weighted form
are

\[
 \mathbf1_{r\equiv-h\ (4)}
 =\frac{1-\chi_4(h)\chi_4(r)}2,
 \qquad
 \chi_4(h)\mathbf1_{r\equiv-h\ (4)}
 =\frac{\chi_4(h)-\chi_4(r)}2.
 \tag{74.7}
\]

The phase becomes

\[
 e\!\left(\frac{\sqrt X}{2}\sqrt{h(h+r)}\right).
 \tag{74.8}
\]

This identity is exact, including the first lattice point on the hard
edge.  It exposes a genuine antisymmetric character numerator, but it does
not make the phase or the actual symbol symmetric under (h\leftrightarrow
r).  Any proposed cancellation must retain the dyadic cutoff on the
original (h), the range (r\leq3h), and (74.1).

For fixed (r), the sheared phase (F_r(h)=(\sqrt X/2)\sqrt{h(h+r)})
has

\[
 F_r''(h)=-\frac{\sqrt X\,r^2}
 {8\{h(h+r)\}^{3/2}}.
 \tag{74.9}
\]

Large real curvature is not a derivative-gap theorem modulo one.  In
particular, a termwise second-derivative estimate or an absolute sum over
dual aliases must be power-counted before it is accepted.

## 4. Product grouping and the exact Cauchy target

Grouping (n=hm) gives

\[
 \mathcal T_L^{\rm end}
 =\sum_{n\asymp L^2}A_L(n)e(\sqrt{Xn}),
 \tag{74.10}
\]

where

\[
 A_L(n)=
 \sum_{\substack{h\mid n,\ h\asymp L,\ h\ \mathrm{odd}\\
                  \lceil h/4\rceil\leq n/h\leq h}}
 \chi_4(h)a_{L,H,X}(h,n/h).
 \tag{74.11}
\]

This is a moving near-square truncated divisor coefficient, not the full
(r_2(n)/4\) coefficient and not a multiplicative function.

Cauchy in the original (h)-variable gives

\[
 |\mathcal T_L^{\rm end}|^2
 \leq O(L)\left\{
  \sum_h\sum_m|a(h,m)|^2
 +\sum_h\sum_{m\ne m'}a(h,m)\overline{a(h,m')}
   e\!\left(\sqrt{Xh}(\sqrt m-\sqrt{m'})\right)
 \right\}.
 \tag{74.12}
\]

The first term is (O(L^2)), exactly the (L^3) squared target after the
outer (O(L)).  Therefore a sufficient fixed-row correlation target is

\[
 \sum_h\sum_{m\ne m'}a(h,m)\overline{a(h,m')}
 e\!\left(\sqrt{Xh}(\sqrt m-\sqrt{m'})\right)
 \ll_\varepsilon L^2X^\varepsilon.
 \tag{74.13}
\]

This sufficient estimate loses the explicit (\chi_4(h)), so a proof of
(74.2) may instead retain the character and use a sharper signed route.
Do not present (74.13) as necessary.

## 5. Required controls

Every argument must audit:

1. the exact factor in (74.4) and the real-even conjugate;
2. odd (h), (\chi_4(h)), and the zero contribution of even frequencies;
3. the full hard lower-edge coefficient and ceiling convention;
4. the flat upper support edge and (q_X\ne1);
5. (1\leq L\leq H\), including bounded (L), (L\asymp H), and the
   intermediate range;
6. product grouping multiplicity and the nonmultiplicative truncation;
7. the shear projector (74.7), both character terms, and the original
   cutoff ownership;
8. exact-square and perfect-fourth-power phase resonances;
9. diagonal, near-diagonal, hard-edge, and moving-boundary terms;
10. stationary aliases, transform errors, and any self-return;
11. the false unsigned/arbitrary-coefficient analogue;
12. separation from (M1), smooth-interior packets, (M9), and the global
    exponent.

## 6. Promotion and stopping rule

A full promotion requires a proof of (74.2) for all dyadic
(1\leq L\leq H) with the twelve controls.  A strict new (L)-subrange,
an exact reduction to a smaller actual-symbol correlation, or a rigorous
route-specific no-go is useful progress but does not prove
`M9-M2-top-endpoint-signed-cone`.  Computation may falsify but may not
certify an asymptotic estimate.
