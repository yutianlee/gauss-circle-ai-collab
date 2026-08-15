# Round 74 conductor adjudication

Campaign: \`m9-m2-top-endpoint-affine-cone\`  
Round: 74  
Starting graph SHA-256: \`6e094849c4bbdeb08bb04771667f64cd6a36f0d56ba2cb811942693c3597e767\`

## Decision

The full affine-cone estimate remains open.  Promote only the exact
row-Cauchy reduction proved independently from the frozen packet.  Retain
the two-dimensional near-product/reciprocal-energy formula as a candidate
for a dedicated statement-only validation round; it is not promoted here.

## Exact promoted kernel

Let \(b_h=\lceil h/4\rceil\), let \(a(h,m)\) be the exact normalized
top-cone symbol, and let

\[
 \mathcal T_L=\sum_{\substack{h\asymp L\\h\ \mathrm{odd}}}
 \chi_4(h)\sum_{m=b_h}^{h}a(h,m)e(\sqrt{Xhm}).
\]

For any fixed \(K_0\geq1\), Cauchy in the outer \(h\)-variable gives

\[
 |\mathcal T_L|^2\ll L\{D+\mathcal C_{\ne}\},
 \qquad D=\sum_h\sum_m|a(h,m)|^2\ll L^2,
\]

and exact one-sided expansion gives

\[
 \mathcal C_{\ne}=\mathcal C_{\mathrm{core}}+O_{K_0}(L^2),
\]

where

\[
 \mathcal C_{\mathrm{core}}
 =2\Re\sum_h\sum_{k=K_0+1}^{h-b_h}
 \sum_{m=b_h+1}^{h-k-1}
 a(h,m)\overline{a(h,m+k)}
 e\!\left(\sqrt{Xh}(\sqrt m-\sqrt{m+k})\right).
\]

The diagonal, every fixed-width near-diagonal, and all pairs touching
either moving endpoint are therefore target-safe absolutely.  The
one-sided upper bound

\[
 \mathcal C_{\mathrm{core}}\ll_\varepsilon L^2X^\varepsilon
\]

is sufficient for \(\mathcal T_L\ll L^{3/2}X^\varepsilon\).  It is not
necessary, because this Cauchy step deletes \(\chi_4(h)\).

The same blind derivation proves the epsilon-trivial unbounded range
\(L\leq(\log(2+X))^A\) for each fixed \(A\).  This is useful bookkeeping,
not a polynomial-range advance.

## Candidate retained for the next round

The discovery and hostile reports independently obtain a rank-one
quarter-shift Poisson normal form.  After target-safe boundary treatment,
the candidate main is

\[
 \mathcal T_{L,\mathrm{int}}
 =e(1/8)L^{3/2}X^{-1/4}\mathcal D_L+\text{safe errors},
\]

\[
 \mathcal D_L
 =\sum_{\substack{j\asymp J\\j\ \mathrm{odd}}}\chi_4(j)
 \sum_{l\asymp J}B_{L,X}(j,l)
 K\!\left(\frac{L(X-jl)}{4l}\right),
 \qquad J=\sqrt X,
\]

with \(|X-jl|\ll JX^\varepsilon/L\) and target
\(\mathcal D_L\ll J^{1/2}X^\varepsilon\).  Poisson in the uncharactered
leg gives the sufficient diagonal-scale energy

\[
 \sum_{|k|\ll LX^\varepsilon}
 \left|\sum_{\substack{j\asymp J\\j\ \mathrm{odd}}}
 \chi_4(j)b_{j,k}e(-kX/j)\right|^2
 \ll_\varepsilon LJX^\varepsilon.
\]

Poisson in the character-bearing leg returns to the original top M2
reciprocal block.  The two selected-context reports agree on this algebra,
but the statement-only report did not receive the candidate formula.
Under the protocol, the constants, boundary collar, actual amplitude,
energy normalization, and self-return therefore require a new blind seam
before graph promotion.

## Source adjudication

Kowalski--Robert--Wu Proposition 5 lawfully gives

\[
 \mathcal T_L\ll_\varepsilon X^\varepsilon
 \left(J^{1/8}L^{13/8}+L^{3/2}+L^{7/4}
 +J^{-1/2}L^{3/2}\right).
\]

It is nontrivial against \(L^2\) only for \(L>J^{1/3}\).  On precisely
that range the already accepted two-shift estimate
\(J^{1/2}L^{1/2}X^\varepsilon\) is no larger.  The imported theorem
therefore gives neither a new bound nor a target subrange.  No source card
was created, and no external-dependency promotion is warranted.

The other audited large-sieve, root-spacing, one-variable exponent-pair,
short-divisor, Kloosterman-fraction, and Kuznetsov theorems do not match
the fixed-centre actual-symbol energy.

## Rejected routes

- Shear antisymmetry does not cancel because the domain and symbol do not
  respect \(h\leftrightarrow r\).
- Product grouping with only divisor bounds proves a false
  arbitrary-coefficient analogue.
- Large real curvature alone does not control fractional aliases.
- Absolute summation after one-variable stationary phase is worse than
  the original row bound.
- Treating the rank-one two-dimensional transform as a nondegenerate
  Hessian estimate is false.
- A second high-character Poisson transform is a self-return, not an
  independent saving.
- The applicable KRW estimate does not improve the accepted T2S envelope.

## Downstream scope

The polynomial intermediate \(L\)-range remains open.  No status changes
are licensed for the full top cone, \(M9\!-\!M2\), \(M9\!-\!M1\), \(M9\),
or the Gauss-circle exponent.

