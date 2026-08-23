# Conductor derivation packet: exact dual sectors and candidate inequalities

Campaign: `m9-m2-unbalanced-dual-offproduct-sector-gate`

Starting graph SHA-256:
`27bd4173fbdb16e5689595a02d42d82ffa8bb514b4610ea745ce2da6e2b8b152`

Status: accepted input identities plus candidate proof directions.  No
sector estimate below is accepted unless the reports prove it with every
literal sign, profile, block edge, and capacity seam.

## 1. Exact target

Use (125.B1)--(125.B13) from `blind_statement.md`.  The exact target is

$$
 \mathcal S_{\rm eq}^{\ne0}+\mathcal S_{\rm neq}
 \ll_\varepsilon X^{1/2+\varepsilon}.
\tag{125.D1}
$$

The two sectors may cancel.  Proving each separately is sufficient but may
be strictly stronger.  The identity

$$
 \mathcal D_0+\mathcal S_{\rm eq}^{\ne0}
 =C_H\sum_p\sum_n\left|\sum_{a<H}b_{p,n+a}\right|^2
\tag{125.D2}
$$

must therefore be used with care: the right side is positive, while the
off-zero-shift part alone is not.

## 2. Equal-mode shifted chart

For fixed \(p\), let \(f_p(k)=\sqrt{Mpk}\).  Then

$$
 f_p'(k)\asymp D,\qquad
 f_p''(k)\asymp-D/K,
\tag{125.D3}
$$

on fixed interiors, while (125.B12) describes the exact correlation
derivative.  Its range over \(|h|<H\) reaches

$$
 \frac{DH}{K}\asymp Q\to\infty.
\tag{125.D4}
$$

Thus a uniform first-derivative gap is false.  A candidate estimate may
instead use a block-local curvature decomposition, exact Fejer spectral
localization, or spacing of the integer crossings jointly in \((p,n)\).
It must state whether it bounds (125.B5), the stronger positive quantity
(125.D2), or only a model.  The raw shifted triangle has scale \(R=X/D\),
and the later principal stationary ledger has scale \(D^2/L\); both exceed
\(X^{1/2}\).

## 3. Unequal-mode chart

For \(p\ne q\), retain

$$
 \chi_4(p)\chi_4(q),\qquad
 \mathcal N=(p-q)k+ph,qquad
 \mathcal G=(p-q)k-qh.
\tag{125.D5}
$$

The product-defect progression gives multiplicity information but not a
signed estimate.  Candidate noninvertible routes include a sign-preserving
sum over the mode difference \(p-q\), a complete product-defect
progression estimate with both moving profiles, or a joint inequality that
keeps (125.B5) and (125.B6) together.  Random square-root credit across the
\(L^2\) pairs leaves \(D^2/L=Q\sqrt X\), so any such route must exhibit
the additional factor \(Q\) or a different capacity ledger.

## 4. Required falsifiers

Every claimed estimate must answer:

1. Does it remain true for arbitrary bounded signs?  If so, why does its
   positive diagonal not exceed the target?
2. Does it bound the actual scalar (125.D1), or a stronger \(p\)-row,
   aliaswise, shiftwise, or coefficient-blind norm?
3. Are cancellations between (125.B5) and (125.B6) discarded?
4. Are negative shifts paired only as conjugates, rather than called a
   cancellation?
5. Are the moving \(p/k\) profiles, exact Fejer triangle, and zero-extended
   entries and exits retained?
6. Does any B-process merely return the Round-124 primal alias phase?

No unsigned ledger may be promoted as a lower bound.  If no complete
actual-sign contraction survives, state the narrowest exact functional at
which this UNBAL lane should be parked.
