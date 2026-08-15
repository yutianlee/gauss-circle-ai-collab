# Round 64 derivation packet: reciprocal cone as a product wavelet

## Accepted input

Let \(e(t)=e^{2\pi i t}\), \(N=X^\nu\), \(0<\nu\leq2/5\), and
\(T=\sqrt{X/N}\). Fix \(\Xi\in C_c^\infty((0,1))\); it owns a smooth
interior part of the exact condition \(j\leq\sqrt X\). Round 63 proves
that the positive-frequency interior
stationary contribution to the exact one-sided divisor radial sum is,
apart from the fixed factor \(2X^{-1/4}e(-1/8)\),

\[
 \mathcal R_{X,N}[V,\Xi]
 =\sum_{h,j\geq1}\frac{\chi_4(j)}h
 \Xi(j/\sqrt X)V\!\left(\frac{4Xh^2}{j^2N}\right)e(Xh/j).
\tag{64.1}
\]

Without \(j\leq\sqrt X\), (64.1) is not the stationary cone and is not
even an admissible infinite bulk sum. The full Round-63 identity contains
the sharp owner \(j\leq\sqrt X\), a target-safe square boundary,
an exact \(j^{-1}\) subtraction, negative-frequency nonstationary terms,
and stationary entry/exit pieces. None may be silently discarded when a
full radial estimate is claimed. This round first freezes a smooth
interior bulk and then audits its implication back to the complete cone.

The normalized radial target requires

\[
 \boxed{\mathcal R_{X,N}[V,\Xi]\ll_{\varepsilon,V,\Xi}X^{1/4+\varepsilon}.}
\tag{64.2}
\]

Termwise absolute summation has size \(X^{1/2+o(1)}\), so (64.2) asks
for a square-root cancellation gain.

## Exact product-wavelet identity to prove

Put

\[
 g(t)=\begin{cases}V(t^2)/t,&t>0,\\0,&t\leq0,\end{cases}
 \qquad \widehat g(\xi)=\int_{\mathbb R}g(t)e(-\xi t)\,dt.
\tag{64.3}
\]

Because \(V\in C_c^\infty((0,\infty))\), \(g\) is Schwartz and
vanishes on a neighborhood of zero. For fixed \(j\), let
\(H_j=j/(2T)\). Then

\[
 \frac1hV\!\left(\frac{4Xh^2}{j^2N}\right)
 =\frac1{H_j}g(h/H_j).
\]

The candidate exact Poisson identity is

\[
 \boxed{
 \mathcal R_{X,N}[V,\Xi]
 =\sum_{j\geq1}\chi_4(j)\Xi(j/\sqrt X)
 \sum_{m\in\mathbb Z}
 \widehat g\!\left(\frac{jm-X}{2T}\right).}
\tag{64.4}
\]

The exact bulk geometry is

\[
 j\asymp Th,\quad 1\leq h\ll\sqrt N,
 \quad T\ll j\ll\sqrt X,
 \quad m\asymp X/j,
 \quad |jm-X|\lesssim T.
\tag{64.5}
\]

Moreover every algebraic moment of the product kernel vanishes:

\[
 \int_{\mathbb R}\xi^r\widehat g(\xi)\,d\xi=0
 \qquad(r=0,1,2,\ldots).
\tag{64.6}
\]

The identity (64.4), its signs, measures, negative \(m\), cutoff
ownership, and moment statement must be checked rather than assumed.

## Frozen objective

Prove (64.2) for a nonempty fixed interval \(0<\nu\leq2/5\), or derive
the sharpest exact product-wavelet/nearest-product reduction and a
rigorous obstruction showing why zero moments, period-four character,
or available shifted-divisor theorems do not supply the required
square-root gain.

A positive route may use:

1. cancellation in \(j\) across the signed residuals \(jm-X\);
2. a coefficient-preserving short shifted-divisor or spectral theorem;
3. a bilinear decomposition retaining \(\chi_4(j)\) and the zero-moment
   kernel;
4. a second Poisson/Voronoi transformation, but only if it does not
   merely return to the accepted lower-radial sum;
5. exact character pairing with full unmatched and transition owners.

## Required controls

- Poisson normalization and sign;
- target power \(X^{1/4}\) before the external \(X^{-1/4}\);
- support endpoints and the \(j=\sqrt X\) saddle collision;
- negative \(m\) and zero product;
- exact versus near products;
- all moment cancellations and cutoff commutators;
- perfect-square/fourth-power coherence;
- comparison with the accepted near-product/PSC kernel;
- primary-source hypotheses for any imported short-divisor theorem;
- full-cone implication, including subtraction and entry/exit.

## Forbidden shortcuts

- Do not take absolute values before the \((j,m)\)-sum and call the
  result cancellation.
- Do not replace the truncated character-divisor incidence by
  \(r_2(n)/4\).
- Do not infer a short-interval theorem merely from the vanishing mean
  of \(\widehat g\); all its moments vanish, but the arithmetic
  coefficient is not smooth.
- Do not cite Hessian determinant, generic irrationality, or a
  separable shifted-convolution theorem without matching the moving
  product window and actual character.
- A self-return is a useful exact no-go, not a proof of (64.2).

## Promotion gate

A new radial interval requires (64.2), uniform entry/exit and
subtraction control, and recombination with Round 62. An exact identity,
self-return, or source obstruction may be promoted only as a scoped
reduction/no-go. No exponent changes without a proved radial interval.
