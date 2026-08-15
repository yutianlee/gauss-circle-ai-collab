# Conductor calculation: the separated regular symbol has the target BV scale

Campaign: `m9-m1-beta-regular-finite-part-symbol-bv`  
Role: conductor local derivation  
Allocation: 100% analytical/algebraic

> Hostile-control correction. The original fixed-\(y=L-\nu\)
> product-rule sketch below cannot be estimated term by term:
> differentiating \(f(L-y)\) has absolute mass
> \(\asymp_b\lambda^{-1}\), one power above the target. The total
> separated-kernel BV conclusion survives only after returning to physical
> \((L,\nu)\) coordinates, where the translation derivative is combined
> with the moving-section traces. Section 3 is therefore replaced by the
> corrected calculation below.

## 1. Model and exact regular part

On a separated signed saddle patch put

\[
 A=\rho _0-i\alpha,\qquad L=\alpha-\beta,
 \qquad f(\nu)=\widehat\phi(b+i\nu),
\]

and let \([a(L),c(L)]\) be one affine cell of the exact finite section in
the top variable \(y=L-\nu\).  After removing the explicit Plemelj
delta/log term, the local two-denominator regular part is

\[
 R(\alpha,L)=-\frac1{2A}\int_a^c
 \frac{f(L-y)}{A+iy/2}\,dy
+\int_a^c\frac{f(L-y)-f(L)}{y(A+iy/2)}\,dy .       \tag{31.C1}
\]

This is exactly the sum of the two regular terms in the Round-30 partial
fraction formula.  It is valid away from the artificial \(\rho=0\) seam;
that seam must be treated with the full omega-recombined expression.

## 2. Value bound

Assume \(|\alpha|\asymp\lambda\ge2\), bounded \(\beta,\rho _0\), and

\[
 |f^{(k)}(t)|\ll_b(1+|t|)^{-3-k},\qquad 0\le k\le2. \tag{31.C2}
\]

The first integral in (31.C1) is \(O_b(\lambda^{-1})\), because its
denominator is a Cauchy kernel whose convolution with the integrable
profile has far-field size \(O_b(\lambda^{-1})\). Its outside factor is
\(A^{-1}=O(\lambda^{-1})\). For the second integral, subtracting the
diagonal removes the top pole. In physical height coordinates the two
remaining denominators are each \(\asymp\lambda\) on the main mass of
\(f\), while transform decay handles the complementary regions. Hence it
is also \(O_b(\lambda^{-2})\), and

\[
 |R(\alpha,L)|\ll_b\lambda^{-2}.                    \tag{31.C3}
\]

The same proof works for both signs of the saddle and on every affine
endpoint cell.  Endpoint logarithms were already removed and have the
stronger accepted \(\lambda^{-4}\) coefficient.

## 3. Scaled derivative

With \(\nu=L-y\), write the regular kernel as

\[
 K(L,\nu)=-\frac{i f(L)}{2A\{A+i(L-\nu)/2\}}
 +\frac{f(\nu)-f(L)}{(L-\nu)\{A+i(L-\nu)/2\}}.       \tag{31.C3a}
\]

On a separated saddle cell, \(|L|\asymp|A|\asymp\lambda\). In the main
height region \(|\nu|\ll\lambda\), (31.C2), the divided-difference
identity, and direct differentiation at fixed \(\nu\) give

\[
 |K(L,\nu)|\ll_b\lambda^{-2}(1+|\nu|)^{-3},\qquad
 |\partial_LK(L,\nu)|\ll_b\lambda^{-3}(1+|\nu|)^{-3}. \tag{31.C3b}
\]

Near \(\nu=L\), the numerator \(f(\nu)-f(L)\) removes the apparent
singularity. The far-height region follows from (31.C2), and the
artificial-\(\rho\) neighborhood remains excluded. Leibniz differentiation
of

\[
 \int_{[-V,V]\cap[L-U,L+U]}K(L,\nu)\,d\nu
\]

has an interior total variation \(O_b(\lambda\lambda^{-3})\). Fixed
\(\nu=\pm V\) faces have zero velocity, while the translated
\(\nu=L\mp U\) endpoint traces have \(L^1\) norm
\(O_b(\lambda^{-2})\). This is the translation/endpoint recombination
that is lost by taking absolute values termwise in fixed-\(y\) coordinates.

Consequently, on a saddle patch of alpha-length \(O(\lambda)\),

\[
 \sup |R|+\int |\partial_\alpha R|\,d\alpha
 \ll_b\lambda^{-2}.                                 \tag{31.C4}
\]

Equivalently, after \(y_{\rm M}=\alpha/\lambda\),
\(\|R\|_\infty+\|\partial_{y_{\rm M}}R\|_1\ll_b\lambda^{-2}\).
Restoring the accepted post-endpoint numerator \((D_j/q)\lambda\) gives
the desired separated-symbol scale \(D_j/(q\lambda)\), hence local
\(q^{-2}\).

## 4. Exact scope

This closes the derivative gap for the separated fixed-profile
two-denominator kernel, including affine moving endpoints.  It does not
yet prove the Round-31 obligation.  The remaining factors are the
large-alpha gamma/Stirling symbol, beta connector, scale and radial
profiles, floors and stars, finite tails, and—most importantly—the
artificial-pole-safe combination

\[
 \omega G+(1-\omega)R_1-\omega E_1.                 \tag{31.C5}
\]

Termwise estimates of (31.C5) near \(\rho=0\) are invalid.  Its derivative
must first be combined so that every \(\omega'\) contribution is visibly
multiplied by \(G-R_1-E_1=0\), with identical domains and masks.

## 5. Next conductor seam

The local calculation indicates that the ordinary divided-difference
calculus is not the obstruction.  The decisive Round-31 check is whether
all remaining actual factors are order-zero symbols in the scaled Morse
variable and whether the omega recombination remains exact after the
finite-section subtraction.  A failure there must be recorded factor by
factor; no pointwise estimate may substitute for (31.C4).
