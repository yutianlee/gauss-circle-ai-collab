# Round 102 synthesis: determinant-weighted fixed-a actual Gram

Starting graph SHA-256:
fbe0e9b9e4db078128f75d97b790dd78a6adc8216c7b0b14c4fad928925637ca

Resulting graph SHA-256:
902eb43bc0fc72b1c3e080dac5cd89757d17e2eaa1f72d606b89afbecff92935

## 1. Frozen objective

Round 102 tested whether the stationary determinant in the complete
fixed-\(a\) primitive-ray Gram could supply the missing
\(\rho^{-1/2}\) linear gain, close a strict hard subrange, or yield a
smaller exact survivor.

The evidence consists of a statement-only rederivation, discovery proof,
hostile/source audit, conductor determinant calculation, normalization
review, owner/control review, and adjudication.

## 2. Exact Gram and scale ledger

For the literal zero-extended row,

\[
 \mathcal G_H^{\rm act}
 =H E_{\rm act}
 +2\Re\sum_{1\le s<H}(H-s)(-1)^s C_s^{\rm act}.
\]

The accepted scales are

\[
 E_0\asymp LJD_{\rm ray}^2,\qquad
 \rho={AJD_{\rm ray}^3\over L^3},
\]

and the exact Cauchy bridge converts

\[
 \mathcal G_H^{\rm act}
 \ll_\varepsilon X^\varepsilon {H^2E_0\over\rho}
\]

to the desired \(L^2X^\varepsilon\) linear block bound. The normalization
is correct.

A separately bounded diagonal requires \(H\gtrsim\rho\). Since
\(H\le D_{\rm ray}\), post-diagonal absolute estimates cannot cover
\(\rho>D_{\rm ray}\).

## 3. Carrier determinant and mode correction

Put

\[
 b=a+2q,\qquad b_s=b+2s,\qquad
 \Lambda_q={X(\sqrt b-\sqrt a)^2\over2}.
\]

The extracted saddle carrier has

\[
 \Psi_s''(q)
 =-{X\sqrt a\over2}
 \left({g'\over k'b_s^{3/2}}-{g\over kb^{3/2}}\right).
\]

This is exact, but it is not the determinant of the complete
density-discrepancy phase. Expanding the coupled metric factors replaces
\(g,g'\) by \(g-2\ell,g'-2\ell'\), so the mode-resolved determinant is

\[
 {g'-2\ell'\over k'b_s^{3/2}}
 -{g-2\ell\over kb^{3/2}}.
\]

Keeping the metric factors unexpanded leaves them in a rapidly moving
\(q\)-amplitude. Round 77 proves variation in \(g\), not in \(q\);
primitive and owner masks, moving reciprocal intervals, profiles,
floors, stars, collars, and centred entry/exit remain non-smooth in
that variable.

## 4. Exact and near determinant incidence

For the density carrier, exact zero is equivalent to

\[
 b=dx^2,\qquad b_s=dy^2,\qquad
 d(y^2-x^2)=2s,\qquad
 g'kx^3=gk'y^3
\]

with \(d\) squarefree. For fixed \(a,s\), this gives
\(O_\varepsilon(s^\varepsilon)\) possible base points and
\(O_\varepsilon(GKX^\varepsilon)\) lift quadruples per base point.

On common dyadic boxes, if \(N=GK\),

\[
 \#\left\{(g,k,g',k'):
 \left|{g'k\over gk'}-\left({b_s\over b}\right)^{3/2}\right|
 \le\eta\right\}
 \ll_\varepsilon X^\varepsilon(\eta N^2+N).
\]

At the natural density-carrier quadratic threshold, this is
\(O_\varepsilon(NX^\varepsilon)\) per fixed base. It is a genuine raw
incidence saving.

It does not estimate the complete actual tube: mode resolution changes
the effective numerators, Fourier modes have weighted multiple
representations, and no component-mass or signed diagonal-cancellation
inequality converts the raw count to \(E_0/\rho\). Even in an ideal
coefficient-blind model the raw square-root gain would require
\(\rho\lesssim GK\), which is not a frozen block condition.

Algebraic nonzero spacing is only

\[
 |\Psi_s''|\gg(LJD_{\rm ray}^3)^{-1},
\]

so the guaranteed quadratic phase change on the full row is below one.
At a density zero, the carrier has the exact cubic scale

\[
 |\Psi_s'''|\asymp {JL s\over D_{\rm ray}A^3},
\]

but no complete moving-amplitude derivative theorem follows.

## 5. Strict short-ray survivor and no-go

The residual hard cone has a disjoint half-open bottom block containing
only \(q=1\). Zero extension kills every nonzero shifted correlation.
Thus

\[
 \mathcal G_1^{\rm act}
 =\sum_a|F_a(1)|^2,
\]

and the target becomes the independent actual-symbol energy theorem

\[
 \boxed{\;
 \sum_a|F_a(1)|^2
 \ll_\varepsilon X^\varepsilon {L^4\over A}.
 \;}
\]

Primitive nonsquare near-square and Pell rows show that this block is
not geometrically empty and can have unbounded \(\rho\). Fourth-power
and strict-metric recurrences are method controls only; no lower bound
for the complete coefficient is known.

Therefore nonzero-shift determinant separation is not a uniform
mechanism. This is a route obstruction, not a disproof of the fixed-
\(a\) Gram. On longer rows the strict survivor is the signed complete
mode-resolved near tube jointly with a literal separated complement.

## 6. Conductor decision

Promote one narrowly scoped proved obstruction:

- the density carrier determinant is incomplete for the coupled metric
  phase;
- raw determinant incidence does not imply weighted actual cancellation;
- algebraic spacing is below the active oscillatory scale;
- separate diagonal ownership is confined to
  \(\rho\lesssim D_{\rm ray}\);
- the singleton \(q=1\) block has no determinant shift.

Create the \(q=1\) actual diagonal as an open candidate lemma. Keep the
fixed-\(a\) Gram and canonical density-discrepancy energy open, and order
their next work as:

1. prove the complete short-ray diagonal;
2. estimate the complete longer-row mode-resolved near tube and
   separated complement jointly.

Reject density-determinant-only, algebraic-spacing-only,
Round-77-implies-\(q\)-BV, coefficient-blind, unsigned, and
determinant-covers-singleton claims.

## 7. Global proof status after Round 102

There is no new hard-subrange estimate and no global exponent
improvement. The strongest certified external pointwise exponent remains

\[
 \theta_{\rm LY}
 ={3292+25\sqrt{1717}\over13762}
 =0.3144831759740614\ldots,
\]

while the strongest theorem proved entirely through the internal
architecture remains exponent \(1/3\). The quarter target, M9-M2,
M9-M1, M9, and endpoint-uniform assembly remain open.
