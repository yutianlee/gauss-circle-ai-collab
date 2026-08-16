# Round 80 conductor actual-symbol recoupling

Campaign: `m9-m2-top-endpoint-signed-strict-metric-energy`  
Round: 80  
Starting graph SHA-256:  
`cb007911c1e9d407d9adbc8919ce44cc3eaab411a212d0925e1176f5a154a43a`

## Exact cancellation

Put

\[
 \theta={\Lambda\over k}={X(\sqrt b-\sqrt a)^2\over2k}.
\]

The complete Round-77 coefficient in (80.2) contains the constant phase

\[
 {X(\sqrt b-\sqrt a)^2\over4k}={\theta\over2}.
\]

Hence the phase-removed coefficient

\[
 \widetilde{\mathfrak B}_{a,b,k}(g)
 :=e(-g\theta/2)\mathfrak B^\circ_{a,b,k}(g)
\]

has the exact integral representation

\[
 \widetilde{\mathfrak B}_{a,b,k}(g)
 =g\int_{b/4}^{a}A^\circ_{ga,gb}(gu)
 e\!\left(g\left[ku-J(\sqrt b-\sqrt a)\sqrt u\right]\right)du. \tag{80.R1}
\]

Combining (80.4) with (80.R1), every complete hard summand is therefore

\[
 (-1)^q\widetilde{\mathfrak B}_{a,b,k}(g).          \tag{80.R2}
\]

This identity is finite and exact.  It does not use stationary phase,
discard a collar, extend a lift interval, or replace the actual symbol.

## Consequence for nearest-integer parity

If \(\theta=\ell+\eta\) and \(g\) is odd, factoring only the external
carrier gives

\[
 (-1)^q e(-g\theta/2)
 =(-1)^{q+\ell}e(-g\eta/2).
\]

But the complete coefficient simultaneously satisfies

\[
 \mathfrak B^\circ(g)=e(g\theta/2)
 \widetilde{\mathfrak B}(g).
\]

Thus the factors \((-1)^\ell\) and \(e(-g\eta/2)\) cancel exactly
against the carrier in the actual coefficient.  The proposed quotient
parity \((-1)^{p/k}\), with \(p=\ell k\), is not an independent sign of
the complete summand.  It is an artefact of separating a phase constant
from the coefficient that contains the inverse carrier.

The only remaining explicit arithmetic sign is

\[
 (-1)^q=\chi_4(a)\chi_4(b)
        =\chi_4(ga)\chi_4(gb),                     \tag{80.R3}
\]

because \(a,b,g\) are odd and \(q=(b-a)/2\).  This is exactly the
original two-leg character sign, not a new divisor-fibre character.

## Consequence for the Fourier window

Let \(W_R\) be the period-one strict-metric window.  If one expands
\(W_R(\theta)e(-g\theta/2)\) before restoring the coefficient carrier,
the displayed frequencies are half-integral.  For the complete symbol,
however,

\[
 W_R(\theta)e(-g\theta/2)\mathfrak B^\circ(g)
 =W_R(\theta)\widetilde{\mathfrak B}(g)
 =\mu_R\widetilde{\mathfrak B}(g)
  +\sum_{r\ne0}\widehat W_R(r)e(r\theta)
     \widetilde{\mathfrak B}(g).                  \tag{80.R4}
\]

Integer modes, including the literal density mode \(r=0\), are restored.
Consequently there is no half-integer spectral gap for the actual
coefficient.  Any nonzero-mode estimate must still control the zero mode
in (80.R4); estimating only centered discrepancy cannot imply the hard
sum.

## Exact surviving object

After the Round-78 square-ray removal, the Round-79 exact-center removal,
and the positive-safe condition \(AJD^3\ll L^3\), the strict-metric
restriction leaves the one-count sum

\[
 \sum_{\substack{a,b,k\ \mathrm{residual}\\
                  AJD^3\gg L^3\\
                  0<\|\Lambda/k\|\asymp R^{-1}}}
 \chi_4(a)\chi_4(b)
 \sum_{g\in\mathcal G_{a,b}}
 g\int_{b/4}^{a}A^\circ_{ga,gb}(gu)
 e\!\left(g\left[ku-J(\sqrt b-\sqrt a)\sqrt u\right]\right)du. \tag{80.R5}
\]

Formula (80.R5) is the original transposed two-character energy restricted
to the residual metric blocks.  Reciprocal Fourier expansion, nearest-
integer quotient parity, or reinsertion of the centered constant merely
changes its representation.  None supplies a second independent saving.

This return can be seen without stationary phase.  Set

\[
 h=ga,\qquad s=gb,\qquad x=gu.
\]

Then (80.R1) becomes exactly

\[
 \widetilde{\mathfrak B}_{a,b,k}(g)
 =\int_{s/4}^{h}A^\circ_{h,s}(x)
 e\!\left(kx-J(\sqrt s-\sqrt h)\sqrt x\right)dx.     \tag{80.R6}
\]

Moreover

\[
 {J(\sqrt s-\sqrt h)\over2\sqrt h}<k
 <{J(\sqrt s-\sqrt h)\over\sqrt s},                \tag{80.R7}
\]

and unique primitive-ray factorisation gives a bijection between
\((a,b,g)\) and odd \((h,s)\).  Finally, (80.R3) changes the remaining
sign into \(\chi_4(h)\chi_4(s)\).  Consequently the unrestricted version
of (80.R5) is literally

\[
 \sum_{\substack{h<s<4h\\h,s\ \mathrm{odd}}}
 \chi_4(h)\chi_4(s)
 \sum_{k\ \mathrm{satisfying}\ (80.R7)}
 \int_{s/4}^{h}A^\circ_{h,s}(x)
 e\!\left(kx-J(\sqrt s-\sqrt h)\sqrt x\right)dx,    \tag{80.R8}
\]

with the residual Round-78--79 selectors imposed once.  Thus the
recoupling is an exact adjoint return to the transposed character energy,
not merely a similarity of phases or scales.

## Current adjudication seam

The parity/half-integer-gap route is therefore rejected unless a proof
estimates (80.R5) itself.  A genuine Round-80 advance would now have to
use the surviving \(\chi_4(a)\chi_4(b)\) correlation jointly with the
complete uncentred integral, or close a new explicit subrange of
(80.R5).  A theorem for arbitrary coefficients is inadmissible, and a
theorem only for the nonzero Fourier modes of the metric window is
insufficient.

No status change for the transposed energy, the signed top cone,
\(M9\!-!M2\), \(M9\), endpoint uniformity, or the global exponent is
authorized by this algebra alone.
