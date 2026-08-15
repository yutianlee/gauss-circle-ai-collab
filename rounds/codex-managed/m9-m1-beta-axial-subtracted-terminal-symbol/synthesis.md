# Round 39 synthesis: the quantitative symbol is cellwise and phase removed

Campaign: `m9-m1-beta-axial-subtracted-terminal-symbol`  
Round type: quantitative terminal-symbol normalization  
Graph SHA-256 before patch: `37028b878c143ca545f2fe0139f171387d1377526d1336b2475c07ac5d16e6fb`

## Conductor decision

The frozen aggregate estimate is not a well-typed statement.  The limiting
endpoint-free vector is already summed over (j,h,q), integrated over the
radial variable (x), and assembled over both saddle signs, while

\[
 \lambda_{j,q,x}=\frac{\pi q\sqrt{Xx}}{D_j}
 \tag{39.1}
\]

varies from cell to cell.  Conversely, a raw cell containing the stationary
phase, the stationary numerator, all arithmetic and scale weights, and the
external (X^{1/4}) factor cannot satisfy a bare
(X^\varepsilon\lambda^{-2}) symbol estimate.  The quantitative interface
must therefore be cellwise, fully phase removed, and pre-numerator.

This is a correction of the obligation, not a failure of the beta strategy.
After the correction, the separated singular-top cell and the smooth
translated-profile cells have the right capacity.  Conditional on one exact
mixed symbol norm for the complete cell, the remaining leading
(h,q,x,j) sums are target-safe.  The first genuinely unproved coefficient
is the complete second translation divided difference, including its moving
traces and exact Morse remainder through saddle entry and exit.

## Exact normalization

On the lawful line (c'=5/4), set

\[
 u=a+i(L-\nu),\qquad v=b+i\nu,\qquad
 s=\frac54+i\left(\frac L2+\beta\right),\qquad
 \lambda=\frac{\pi q\sqrt{Xx}}{D_j}.
 \tag{39.2}
\]

The original measure is

\[
 \frac{ds\,du\,dv}{(2\pi i)^3}
 =\frac{d\beta\,dL\,d\nu}{(2\pi)^3}.
 \tag{39.3}
\]

The signed hard-top identity consumes only the (u)-measure,

\[
 \frac1{2\pi}\frac1{0^++i(L-\nu)}
 =\frac12\delta_0(L-\nu)
  -\frac{i}{2\pi}\operatorname{PV}\frac1{L-\nu},
 \tag{39.4}
\]

so two factors of ((2\pi)^{-1}) remain.  The ordinary PV density is
(-i/(2\pi)^3) before the radial factor (-\pi i\sqrt X).  The blind
aggregate display omitted these two remaining contour factors and placed
all spatial shares under the hard-top regularizer; it is therefore not
promoted as an exact aggregate formula.

Let

\[
 A(L)=-1-\frac b2-i(L+\beta),\qquad
 D(L,\nu)=A(L)+\frac i2(L-\nu)=\rho.
 \tag{39.5}
\]

For the singular (u^{-1}) hard-top share only, after the top delta and
constant-numerator PV/log term have been removed together, the exact
regularizer is

\[
 \mathcal R_A[H](L,\nu)
 =-\frac{iH(L,L)}{2A(L)D(L,\nu)}
 +\frac{H(L,\nu)-H(L,L)}{(L-\nu)D(L,\nu)}.
 \tag{39.6}
\]

Smooth top remainders and interior profiles retain their ordinary
(\mu)-integral and the factor

\[
 \frac{\widehat\phi(b+i\nu)\widehat W_j(a+i(L-\nu))}{D(L,\nu)};
 \tag{39.7}
\]

they receive no second delta, PV, or log subtraction.

At fixed physical height (\nu), put (H_0=H(L,L)) and
(\dot H_0=(\partial_L+\partial_\nu)H(L,L)).  Since
(A'=-i) and (D'=-i/2), direct differentiation gives

\[
\begin{aligned}
 \partial_L\mathcal R_A[H]={}&
 -\frac{i\dot H_0}{2AD}+\frac{H_0}{2A^2D}
 +\frac{H_0}{4AD^2}\\
 &+\frac{\partial_LH(L,\nu)-\dot H_0}{(L-\nu)D}
 -\frac{H(L,\nu)-H_0}{(L-\nu)^2D}
 +\frac{i\{H(L,\nu)-H_0\}}{2(L-\nu)D^2}.
 \tag{39.8}
\end{aligned}
\]

The first unsupported complete coefficient is therefore

\[
 \mathfrak E_H(L,\nu)=
 \frac{\partial_LH(L,\nu)-(\partial_L+\partial_\nu)H(L,L)}{L-\nu}
 -\frac{H(L,\nu)-H(L,L)}{(L-\nu)^2}.
 \tag{39.9}
\]

## Phase removal and the corrected target

For either saddle sign, the complete stationary phase satisfies

\[
 \Psi_\pm'(L)=\log\frac{|L+\beta|}{\lambda}.
 \tag{39.10}
\]

This is order one on a fixed-ratio entry/exit collar.  Leaving
(e^{i\Psi_\pm}) inside the differentiated symbol loses the desired extra
inverse power of (\lambda).  The phase must remain in the oscillatory
operator.

The exact Morse-coordinate representation is a leading incomplete Fresnel
term plus a normalized varying-amplitude remainder; it is not an exact
scalar Fresnel multiplier.  With all stationary phases, the character,
the stationary numerator ((D_j/q)\lambda), the real coefficient
monomial, contour constants, radial integration, floors, stars, and the
external (X^{1/4}) normalization left outside, the corrected sufficient
obligation is

\[
\begin{aligned}
 \mathfrak M_\lambda(K):={}&
 \sup_{L\in I_\lambda}\int |K(L,\nu)|\,d\nu
 +\int_{I_\lambda}\!\int |\partial_LK(L,\nu)|\,d\nu\,dL\\
 &+\sum_{\gamma}\int_{I_\lambda}|K(L,\gamma(L))|\,dL
 +\mathfrak R_\lambda^{\rm Morse}(K)
 \ll_\varepsilon X^\varepsilon\lambda^{-2}.
 \tag{39.11}
\end{aligned}
\]

Here (I_\lambda) is a one-count signed saddle/entry/exit cell,
(\gamma) ranges over every moving regular face, and
(\mathfrak R_\lambda^{\rm Morse}) contains the exact normalized Morse
remainder and its induced endpoint traces.  Formula (39.11), rather than a
single aggregate pointwise weight, is exactly the input needed by the
physical-height Leibniz/BV argument.  A factorized pointwise weight remains
a sufficient special case.

The smooth spatial Mellin profiles do not obstruct (39.11).  Their
translated ridge has fixed-(\nu) derivative (O_b(\lambda^{-4})).  If
one insists on a pointwise weight, the actual range (\lambda\ll X)
permits

\[
 w_{X,b}(\nu)\asymp_b
 \frac{\mathbf 1_{1\le|\nu|\le CX}}{1+|\nu|}
 +(1+|\nu|)^{-2},\qquad
 \|w_{X,b}\|_1\ll_b\log X.
 \tag{39.12}
\]

Thus an (X)-independent product majorant is unnecessary; the complete
hard-top divided difference and moving traces are the actual gap.

## Conditional summation theorem

Write

\[
 r=\frac54-\frac{a+b}{2},\qquad
 p=\frac54+\frac{a+b}{2},\qquad 1<r<2.
 \tag{39.13}
\]

Assuming (39.11), the post-stationary coefficient before the external
(X^{1/4}) factor is

\[
 |\chi_4(q)|h^{-r}q^{-2}D_j^{2-r}
 X^{r/2-1/2+b/4}
 x^{-r/2-b/2-5/4}.
 \tag{39.14}
\]

The radial phases are

\[
 \exp\!\left(i\pi\sqrt{Xx}\left(2\mp\frac q{D_j}\right)\right).
 \tag{39.15}
\]

After (y=\sqrt x), one integration by parts gives the factor

\[
 \min\!\left(1,\frac1{\sqrt X|2\mp q/D_j|}\right).
 \tag{39.16}
\]

Consequently

\[
 \sum_{q\ge1}q^{-2}
 \min\!\left(1,\frac1{\sqrt X|2-q/D_j|}\right)
 \ll X^{-1/2}\log(2X).
 \tag{39.17}
\]

The formal exact resonance (q=2D_j) is even and is annihilated by
(\chi_4(q)).  The nearest nonzero odd term has
(|q-2D_j|\ge1) and capacity (O((D_j\sqrt X)^{-1})).  Since
(\sum_hh^{-r}\ll1), one scale contributes

\[
 D_j^{2-r}X^{r/2-1+b/4}\log(2X)\ll\log^C X,
 \tag{39.18}
\]

and the dyadic scale sum is polylogarithmic.  Restoring the external
normalization gives (O(X^{1/4}\log^C X)).  This is a proved conditional
implication from (39.11), not a proof of (39.11), the bounded-alpha share,
the double-bounded branch, or the complete beta transition.

## State effect

- Promote the exact cellwise normalization, contour measure, singular versus
  smooth split, regularizer, fixed-height derivative, and phase-removal
  reduction.
- Promote the conditional leading-saddle coefficient and resonance
  summation reduction.
- Revise the aggregate terminal-symbol claim to the cellwise mixed norm
  (39.11), and retain it open precisely at (39.9), its moving traces, and
  the exact Morse remainder.
- Extend the already proved physical-height finite-section lemma to its
  direct mixed-norm formulation.
- Reject use of one aggregate (\lambda), applying the Plemelj regularizer
  to smooth shares, dropping two contour measures, differentiating the raw
  stationary phase, replacing a varying cell by a scalar Fresnel factor, or
  inferring a quantitative estimate from Round 38 existence.
- Do not promote the complete beta transition, M9-M1, M9, or the Gauss
  circle target.

