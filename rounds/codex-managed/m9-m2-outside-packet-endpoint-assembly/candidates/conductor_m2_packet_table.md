# Conductor candidate: exact M2 outside-packet table

Campaign: m9-m2-outside-packet-endpoint-assembly

Starting graph SHA-256:
a2b3387c43d467aaa2223ecb31807cd09cf0d429dcebd9b7bde0db6f14cf3657

This is working evidence until the Round-97 gates close.

## Physical owner order

Use the exact denominator partition
\(D_j=2^{-j}\sqrt X\), with its fixed rescalings, and the dyadic odd
frequency partition \(1\le L\le H_{D_j}\). Assign owners in this order:

| Order | Physical set | Owner or target |
|---|---|---|
| 1 | bottom \(d\ll X^{1/4}\) | accepted pre-Fourier bound |
| 2 | every Vaaler Fejer residual | accepted R5-Full |
| 3 | main blocks with \(\ell=\delta-1/4\) | accepted T2S |
| 4 | remaining main blocks with \(178\ell+1638\delta\le463\) | accepted TTY wedge |
| 5 | remaining isolated \((\delta,\ell)=(1/2,0)\) cell | accepted full second-derivative bound |
| 6 | remaining cells in the single hard top physical band \(j=0\) | canonical hard-top density--discrepancy theorem |
| 7 | remaining cells in every smooth physical band \(j\ge1\) | open smooth dual three-quarter bound |

The remaining parameter set before the physical split is exactly

\[
 \mathcal U=
 \{(\delta,\ell)\in\Omega:
 \ell<\delta-1/4,\ 178\ell+1638\delta>463\}
 \setminus\{(1/2,0)\}.
\]

The distinction between rows 6 and 7 is physical, not visible solely in
the limiting exponents. A fixed number of smooth bands \(j\ge1\) also
has \(\delta=1/2+o(1)\), but it has no hard cutoff \(d\le y\) and does
not belong to the one-sided top transform.

## Exact smooth survivor

For each smooth residual cell, set

\[
 K=\frac{XL}{D^2},\qquad M=LK.
\]

The accepted transform is

\[
 \mathcal B^+_{D,L}
 =-\frac{e(1/8)}{2\pi}X^{1/4}M^{-3/4}
 \mathcal T_{L,K}+O(1),
\]

with the complete slanted actual symbol and

\[
 \mathcal T_{L,K}
 =\sum_{h\asymp L}\sum_{k\asymp K}
 \chi_4(h)a_{L,K}(h,k)e(\sqrt{Xhk}).
\]

Thus the uniform outside-packet target is

\[
 \mathcal T_{L,K}\ll_\varepsilon M^{3/4}X^\varepsilon
\]

on every smooth physical cell left in \(\mathcal U\). Logarithmically
many cells then assemble.

When \(K/L=X/D^2\asymp1\), the balanced gcd decomposition reduces this
target further to

\[
 \left|\sum_GG\mathscr P_G\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\]

That is a subregion normal form, not a theorem and not a substitute for
the unbalanced smooth corridor.

## Exact hard-top survivor

On the one physical hard top band, the accepted one-sided transform and
errors reduce the remaining main blocks to

\[
 \mathcal T_{\rm end,L}\ll_\varepsilon
 L^{3/2}X^\varepsilon.
\]

The canonical hard-top density--discrepancy theorem implies this bound
after its internal one-count owners. It has no termwise or transform
implication for row 7.

## Conditional implication

The candidate minimal direct implication is:

\[
 \boxed{
 \text{accepted owners}
 +\text{canonical hard-top theorem}
 +\text{uniform smooth residual three-quarter theorem}
 \Longrightarrow \text{M9-M2}.}
\]

The proof is the physical owner table followed by the
\(O(\log^2X)\) dyadic assembly. It should be promoted only after the
profile, endpoint, and one-count seams are independently checked.

## Graph-hygiene candidate

The identity

\[
 e(h/4)-e(3h/4)=2i\chi_4(h)
\]

for odd \(h\), and zero for even \(h\), is an accepted algebraic rule,
not an additional analytic estimate. The near-collision taxonomy,
fourth-moment pointwise upgrade, and local fourth moment are alternative
routes to a smooth signed bound. They are not logically required if the
direct smooth three-quarter theorem and the hard-top theorem are proved.

The conductor will not remove those legacy routes or change their status
until the blind and hostile graph audits confirm the one-count
implication.

## Current conclusion

The canonical hard-top theorem alone is insufficient. Even after it is
assumed, every smooth residual cell in row 7 remains. In particular, the
balanced outside-absolute quarter packet and the unbalanced
\(M^{3/4}\) product-phase corridor are independent analytic survivors.
