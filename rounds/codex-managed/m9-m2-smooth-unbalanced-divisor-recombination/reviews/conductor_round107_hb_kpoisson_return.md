# Conductor review: character (h)-process and fixed-centre return

## Scope

This review checks the strict smooth-interior principal transform of the
literal Round-107 symbol.  It does not replace the required accounting of
stationary-entry collars, nonstationary modes, aggregate transform errors,
or previously owned pieces.

Write

\[
 a_{L,K}(h,k)=q_L(h)
 \left({LK\over hk}\right)^{3/4}
 W\!\left(\sqrt{{hX\over4kD^2}}\right),
 \qquad K={XL\over D^2}.
\]

## Exact character branches and the (h)-saddle

Resolve

\[
 \chi_4(h)={e(h/4)-e(3h/4)\over2i}.
\]

For the branch \(\tau\in\{1,3\}\), Poisson summation in \(h\) has phase

\[
 f_{m,\tau}(x)=\sqrt{Xkx}-\left(m-\frac{\tau}{4}\right)x.
\]

Put

\[
 r=4m-\tau>0.
\]

Then

\[
 h_*={4Xk\over r^2},\qquad
 f_{m,\tau}(h_*)={Xk\over r},\qquad
 f''_{m,\tau}(h_*)=-{r^3\over32Xk}.
\]

Since the two branch coefficients are \(+1/(2i)\) and \(-1/(2i)\),
and since \(\tau=-\chi_4(r)\) on the corresponding residue classes, the
two stationary branches combine with the exact leading factor

\[
 2\sqrt2\,i\,e(-1/8)\chi_4(r)
 (Xk)^{1/2}r^{-3/2}.
\]

Thus the character is transferred from the original \(h\)-variable to
the odd reciprocal variable \(r\); it is not lost.

## Cancellation with the literal symbol

At the critical point,

\[
 W\!\left(\sqrt{{h_*X\over4kD^2}}\right)
 =W\!\left({X\over rD}\right),
\]

and direct algebra gives

\[
 (Xk)^{1/2}r^{-3/2}a_{L,K}(h_*,k)
 ={(LK)^{3/4}X^{-1/4}\over2\sqrt2}
 {q_L(4Xk/r^2)\over k}
 W\!\left({X\over rD}\right).
\]

Consequently the strict-interior principal term is

\[
 \mathcal T_{L,K}^{\mathrm{stat}}
 =i e(-1/8)X^{-1/4}(LK)^{3/4}
 \sum_{\substack{r\ge1\\r\ \mathrm{odd}}}
 \chi_4(r)W\!\left({X\over rD}\right)
 \sum_{k\ge1}{q_L(4Xk/r^2)\over k}e(Xk/r).
\]

Multiplying by the already accepted physical prefactor

\[
 -{e(1/8)\over2\pi}X^{1/4}(LK)^{-3/4}
\]

leaves exactly \(-i/(2\pi)\) times the displayed dimensionless row.  No
power of \(X,D,L\), or \(K\) remains available as an additional saving.

## (k)-Poisson and the near-product window

Poisson summation in \(k\), followed by

\[
 h={4Xx\over r^2},
\]

turns one Fourier mode \(d\) into

\[
 \int_0^\infty {q_L(h)\over h}
 e\!\left(h\left[{r\over4}-{dr^2\over4X}\right]\right)\,dh.
\]

The support has

\[
 r\asymp {2X\over D},\qquad d\asymp {D\over2},
\]

up to the fixed support constants, and rapid localization requires

\[
 |dr-X|\ll {D\over L}.
\]

The raw fixed-centre incidence capacity is therefore \(D/L\), up to
divisor and endpoint factors.  After undoing the physical normalization,
this misses the desired bound by

\[
 {D\over LX^{1/4}}={H_D\over L},
 \qquad H_D=DX^{-1/4}.
\]

It becomes target-safe only on the already terminal-scale boundary
\(L\asymp H_D\); it gives no new interior residual corridor by counting.

## Adjudication gate

The calculation proves a coefficient-preserving principal carrier return,
not yet a complete all-symbol identity.  A promotable no-go must retain:

- the stationary-entry and exit collars in the (h)-process;
- all nonstationary Fourier modes and aggregate (B)-process errors;
- the exact distinction between (W(X/(rD))) and a physical
  (W(d/D)) sample inside the near-product window;
- both frequency orientations, floors, stars, height profiles, and prior
  owners.

Subject to those gates, the transform has equal capacity and isolates the
signed fixed-centre one-character product-wavelet correlation as the
smallest visible survivor.  It does not prove the three-quarter target or
change any downstream exponent.
