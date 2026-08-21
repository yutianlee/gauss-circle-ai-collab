# Round 93 conductor review: moving coefficients and assembly

## Exact fixed partition

On \(Y\leq t\leq2Y\), set \(D_j=2^{-j}\sqrt Y\), let
\(W(u)=\eta(u)-\eta(2u)\), and choose \(J\) maximal with
\(D_J\geq(2Y)^{1/4}\). Since \(d/(2\sqrt Y)<1\) for
\(d\leq\sqrt t\),

\[
 \mathbf1_{d\leq\sqrt t}
 =\mathbf1_{d\leq\sqrt t}
 \left\{\sum_{j=0}^{J}W\!\left(\frac d{2D_j}\right)
 +\eta\!\left(\frac d{2D_{J+1}}\right)\right\}.
 \tag{R93.M1}
\]

This is the accepted telescoping profile with a different fixed anchor,
not a new approximation. The bottom term is supported on
\(d\ll Y^{1/4}\). Every active profile is fixed in \(t\), supported on a
fixed-ratio \(D_j\)-shell, and multiplied only by the literal ordered
prefix \(d\leq\lfloor\sqrt t\rfloor\).

## Height increments

For \(H_D(t)=\lfloor Dt^{-1/4}\rfloor\), extend the M2 coefficient by zero
and set

\[
 \gamma_{h,r}=\beta_{h,r}-\beta_{h,r-1}.
\]

The accepted \(C^1\) regularity of \(\Phi\), including \(\Phi(1)=0\),
gives

\[
 |\gamma_{h,r}|\ll r^{-2}\mathbf1_{0<|h|\leq r},
 \qquad
 \beta_{h,H_D(t)}
 =\sum_{r\geq1}\gamma_{h,r}\mathbf1_{t\leq(D/r)^4}.
 \tag{R93.M2}
\]

For a denominator interval containing \(N\) samples, exact equality
grouping and Cauchy within a class give

\[
 \sum_{a,b}|A^{(r)}_{a,b}|^2\ll N/r^2.
 \tag{R93.M3}
\]

## Maximal prefix

Every prefix of an ordered \(D\)-shell is the disjoint union of at most
one canonical interval at each binary-tree level. Pointwise Cauchy,
followed by the frozen large sieve for every tree node, yields

\[
 \int_{I'}\max_n|F_{r,n}(t)|^2dt
 \ll(\log(2D))^2(|I'|+D^2)\frac D{r^2}.
 \tag{R93.M4}
\]

At each level the nodes partition the shell, so their coefficient masses
sum to \(O(D/r^2)\); there is no number-of-prefixes loss. Apply this on
\([Y,2Y]\cap(-\infty,(D/r)^4]\) and use Minkowski in \(r\). This proves,
with polylogarithmic loss only,

\[
 \int_Y^{2Y}|S_{i,D}^{\rm mov}(t)|^2dt
 \ll_\varepsilon Y^\varepsilon(Y+D^2)D,
 \qquad i=1,2.
 \tag{R93.M5}
\]

For M1 the same Vaaler increment estimate holds, while the spatial
\(\chi_4(d)\) is unit modulus. Floors, both signs, the full endpoint
sample, and every partial prefix are retained.

## Global moment

Because \(D\leq\sqrt Y\) and \(\sum_D\sqrt D\ll Y^{1/4}\),
Minkowski over the geometric scale family gives

\[
 \left\|\sum_D S_{i,D}^{\rm mov}\right\|_{L^2[Y,2Y]}
 \ll_\varepsilon Y^{3/4+\varepsilon}.
\]

The bottom owner is \(O(Y^{1/4})\) pointwise. The accepted R5
product-count proof applies to the fixed bounded shell profile multiplied
by the moving hard prefix; the prefix only restricts its positive
majorant. Therefore the Fejer residual is also
\(O_\varepsilon(Y^{1/4+\varepsilon})\) pointwise. H1--H4 now give

\[
 \boxed{\int_Y^{2Y}|P(t)|^2dt\ll_\varepsilon Y^{3/2+\varepsilon}.}
 \tag{R93.M6}
\]

Consequently, for fixed \(\eta>0\),

\[
 \left|\{t\in[Y,2Y]:
 |P(t)|>Y^{1/4+\eta}\}\right|
 \ll_\varepsilon Y^{1-2\eta+\varepsilon}.
 \tag{R93.M7}
\]

## Scope decision

This is a real-variable global metric theorem. It says nothing about a
prescribed real or integer point and does not estimate the Round-92
fixed-\(X\) density--discrepancy core. It creates no implication to
M9-M1, M9-M2, endpoint uniformity, M9, the conditional bridge, or
GC-target.
