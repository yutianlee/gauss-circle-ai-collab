# Round 64 conductor adjudication

## Decision

Promote only the fixed-interior product-wavelet reduction and its exact
self-return/no-go. Retain the signed product estimate, full reciprocal
cone, GAR, M9-M1, M9, and the exponent open.

## Accepted kernel

For \(T=\sqrt{X/N}\), fixed \(V\in C_c^\infty((0,\infty))\), and
\(\Xi\in C_c^\infty((0,1))\),

\[
 \mathcal R_{X,N}[V,\Xi]
 =\sum_{n\ge1}\left(\sum_{j\mid n}\chi_4(j)\Xi(j/\sqrt X)\right)
 \widehat g\!\left(\frac{n-X}{2T}\right)+O_B(X^{-B}),
\]

where \(g(t)=\mathbf1_{t>0}V(t^2)/t\). All continuous moments vanish;
for large \(T\), the entire sampled kernel annihilates every polynomial
exactly. Exact products nevertheless survive because \(\widehat g(0)\)
need not vanish.

Inverse Poisson reconstructs the original reciprocal cone. The absolute
product ledger is \(TX^\varepsilon\), so the target needs
\(T/X^{1/4}=X^{1/4-\nu/2}\), exactly the accepted \(H/L\) deficit at
\((D,L,H)=(\sqrt X,\sqrt N,X^{1/4})\).

## Gates

The exact identity, signs, cutoff, moments, product grouping,
nonpositive-product tail, sampled annihilation, perfect-power control,
source audit, and PSC-scale ledger pass. No applicable primary theorem
was found. The sharp \(j=\sqrt X\) collision, lower \(j\)-scales,
entry/exit, negative frequencies, and subtraction remain outside the
fixed interior theorem.

## Scope

This is a meaningful normalization and no-go: it exposes the precise
arithmetic discrepancy required. It is not a radial bound and changes no
Gauss-circle exponent.
