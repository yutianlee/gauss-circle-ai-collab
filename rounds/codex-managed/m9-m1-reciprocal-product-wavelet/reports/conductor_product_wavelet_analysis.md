# Conductor analysis of the reciprocal product wavelet

## 1. Result

For fixed \(V\in C_c^\infty((0,\infty))\) and
\(\Xi\in C_c^\infty((0,1))\), put \(T=\sqrt{X/N}\),

\[
 g(t)=\mathbf1_{t>0}\frac{V(t^2)}t,qquad K=\widehat g.
\]

The fixed interior reciprocal cone has the exact product form

\[
 \mathcal R_{X,N}[V,\Xi]
 =\sum_{n\ge1}A_{X,\Xi}(n)K\!\left(\frac{n-X}{2T}\right)
 +O_B(X^{-B}),
\]

where

\[
 A_{X,\Xi}(n)=\sum_{j\mid n}\chi_4(j)\Xi(j/\sqrt X).
\]

Beyond the continuous moment cancellation, the sampled wavelet itself
annihilates every polynomial exactly once \(T\) is large enough. This
does not close the sum because \(A_{X,\Xi}\) is an atomic truncated
divisor coefficient. The remaining saving is exactly
\(T/X^{1/4}=X^{1/4-\nu/2}\), the accepted \(H/L\) near-product deficit.

## 2. Exact statement and hypotheses

Use \(e(t)=e^{2\pi i t}\) and
\(\widehat f(\xi)=\int f(t)e(-\xi t)\,dt\). Then

\[
 \mathcal R_{X,N}[V,\Xi]
 =\sum_{j\ge1}\chi_4(j)\Xi(j/\sqrt X)
 \sum_{m\in\mathbb Z}K\!\left(\frac{jm-X}{2T}\right).
\tag{2.1}
\]

For every integer \(r\ge0\),

\[
 \int_{\mathbb R}\xi^rK(\xi)\,d\xi=0.
\tag{2.2}
\]

More strongly, if \(2T\) exceeds the radius of
\(\operatorname{supp}g\), then for every real \(X\),

\[
 \boxed{\sum_{n\in\mathbb Z}(n-X)^r
 K\!\left(\frac{n-X}{2T}\right)=0.}
\tag{2.3}
\]

The target remains

\[
 \left|\sum_nA_{X,\Xi}(n)K((n-X)/(2T))\right|
 \ll X^{1/4+\varepsilon}.
\tag{2.4}
\]

## 3. Proof or derivation

For fixed \(j\), take \(H_j=j/(2T)\). Since

\[
 H_j^{-1}g(h/H_j)=h^{-1}V(4Xh^2/(j^2N)),
\]

Poisson summation in \(h\) gives (2.1) with argument
\((jm-X)/(2T)\). Regrouping positive products \(n=jm\) gives the stated
coefficient; nonpositive products are Schwartz-negligible.

Equation (2.2) follows from
\(g^{(r)}(0)=0\). For (2.3), apply Poisson summation to

\[
 F_r(x)=(x-X)^rK((x-X)/(2T)).
\]

Its Fourier transform at integer \(k\) is, up to the fixed Fourier
constant and sign, a linear combination of derivatives of
\(g(-2Tk)\), multiplied by \(e(-kX)\). The \(k=0\) term vanishes
because all derivatives of \(g\) vanish at zero. When \(k\ne0\),
\(|2Tk|\) lies outside \(\operatorname{supp}g\), so every derivative
also vanishes. Hence every Poisson mode is zero.

On the other hand, divisor bounds and Schwartz decay give only

\[
 \sum_n|A_{X,\Xi}(n)K((n-X)/(2T))|
 \ll_\varepsilon TX^\varepsilon.
\]

Thus the exact missing factor is \(T/X^{1/4}\).

## 4. First doubtful or unproved step

The first open statement is (2.4). Polynomial annihilation helps only
after decomposing the arithmetic coefficient into a sufficiently smooth
main term plus a signed discrepancy. No such local expansion of the
moving truncated divisor coefficient, with error
\(O(X^{1/4+\varepsilon})\) on every length-\(T\) interval, is proved.

Inverse Poisson in \(m\) reconstructs the original reciprocal cone
exactly. Therefore another formal Poisson or moment argument is a
self-return unless it introduces a new arithmetic estimate.

## 5. Required control test and outcome

- Poisson sign and scale: pass; the argument is \((jm-X)/(2T)\).
- Dual support: rapid localization, not compact support.
- Exact products: survive through \(K(0)A_{X,\Xi}(X)\), but are
  divisor-bounded and target-safe.
- Polynomial annihilation: pass under the stated support-radius condition.
- Zero moments alone: fail for arbitrary bounded arithmetic sequences;
  one can align their signs with sampled \(K\) and attain size \(T\).
- Perfect powers: exclude any generic irrationality shortcut.
- PSC scale: \(D=\sqrt X\), \(L=\sqrt N\), \(H=X^{1/4}\), so the
  deficit is exactly \(H/L\).
- Full cone: fixed \(\Xi\) omits low \(j\), the sharp
  \(j=\sqrt X\) half-saddle, entry/exit, and subtraction ownership.

## 6. Dependencies and exact artifacts used

This conductor derivation used the Round-64 packet, the two independent
Round-64 reports, the accepted Round-63 synthesis, and the accepted
near-product/PSC syntheses. No numerical experiment was used. It is
fully analytic and does not import an external theorem.

## 7. Recommended state effect

Promote the exact product-wavelet identity, product regrouping, sampled
polynomial annihilation, and inverse-Poisson self-return. Retain the
signed short-product estimate and full reciprocal cone open. Record that
the remaining power is \(X^{1/4-\nu/2}=H/L\), equal to \(X^{1/20}\) at
\(\nu=2/5\). No radial interval or exponent changes.
