# Conductor correction: contour and scale selectors

Campaign: `m9-m1-beta-double-bounded-explicit-validation`

## Contour correction

The frozen packet omitted the inherited lower condition \(a\ge0\). The
actual beta-slab line used in the accepted Round-38 through Round-42
artifacts has

\[
0\le a<a_0,\qquad a+b<\frac12,\qquad \frac a2+b<\frac14.
\]

Therefore the negative-\(a\) counterexamples refute the packet as written,
not the actual contour. Every later statement must print this full domain.

## Exact scale selectors

The packet also used a single smooth profile at every scale. The physical
decomposition instead has three disjoint selector classes:

| class | selector | profile | top treatment |
|---|---:|---|---|
| hard singular top | \(\mathbf1_{j=0}\) | \(u^{-1}\) share | signed Plemelj |
| regular top | \(\mathbf1_{j=0}\) | fixed top remainder \(W_{0,r}\) | ordinary \(\mu\) |
| dyadic interior | \(\mathbf1_{j\ge1}\) | actual \(W_j\) rescaling | ordinary \(\mu\) |

Consequently a lawful finite family needs an explicit
\(\varepsilon_\tau(j)\in\{\mathbf1_{j=0},\mathbf1_{j\ge1},1\}\)
for every type. A single fixed \(W_\tau\) attached to all \(j\) is not the
actual one-count identity, even though both pieces have the same
polylogarithmic analytic bound.

## Derivative correction

Because connector multipliers may contain fixed-degree monomials in
\(\log x\), the packet must assume and use

\[
 |x\partial_xM_\tau|\ll\log^C(2Xhq),
\]

not merely \(\partial_LM_\tau\). This changes no exponent but is necessary
for an exact derivative ledger.

## State recommendation

Reject the literal schematic family as an identity. The corrected analytic
class is viable; construct its actual selector table next.

