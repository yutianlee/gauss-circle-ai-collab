# Conductor candidate: exact determinant split and its structural ceiling

- Campaign: m9-m2-determinant-weighted-actual-gram
- Round: 102
- Starting graph SHA-256: fbe0e9b9e4db078128f75d97b790dd78a6adc8216c7b0b14c4fad928925637ca
- Status: candidate pending blind and hostile review

## 1. Exact Gram and phase derivatives

For the literal zero-extended row in the derivation packet, put

\[
 \mathcal C_s^{\rm act}
 =\sum_{a,q}F_a(q+s)\overline{F_a(q)}.
\]

Finite expansion gives exactly

\[
 \mathcal G_H^{\rm act}
 =H\mathcal C_0^{\rm act}
  +2\Re\sum_{1\le s<H}(H-s)(-1)^s
       \mathcal C_s^{\rm act}.
\]

Write

\[
 b=a+2q,\qquad b_s=b+2s,
 \qquad
 \Lambda_{a,q}={X(\sqrt b-\sqrt a)^2\over2}.
\]

Then

\[
 \Lambda_{a,q}''={X\sqrt a\over b^{3/2}},
 \qquad
 \Lambda_{a,q}'''=-{3X\sqrt a\over b^{5/2}}.
\]

The stationary phase in a correlation is

\[
 \Psi_s(q)=-{g'\Lambda_{a,q+s}\over2k'}
             +{g\Lambda_{a,q}\over2k},
\]

up to a constant unit and the retained complete moving amplitude. Hence

\[
 \Psi_s''(q)=-{X\sqrt a\over2}\Delta_s(q),
\]

where

\[
 \Delta_s(q)
 ={g'\over k'b_s^{3/2}}-{g\over kb^{3/2}},
\]

and

\[
 \Psi_s'''(q)
 ={3X\sqrt a\over2}
 \left({g'\over k'b_s^{5/2}}-{g\over kb^{5/2}}\right).
\]

These identities are exact for the stationary carrier. They do not by
themselves smooth the primitive or prior-owner masks in the complete
coefficient.

## 2. Exact zero-determinant classification

Let \(u=g'k\) and \(v=gk'\). Then

\[
 \Delta_s(q)=0
 \quad\Longleftrightarrow\quad
 {u\over v}=\left({b_s\over b}\right)^{3/2}.
\]

Since \(u/v\) is rational, this happens only when \(b\) and \(b_s\)
have the same squarefree kernel. Equivalently, for one squarefree
\(d\) and positive integers \(x,y\),

\[
 b=dx^2,\qquad b_s=dy^2,
 \qquad d(y^2-x^2)=2s,
\]

and the remaining product equation is

\[
 g'k x^3=gk' y^3.
\]

For fixed nonzero \(s\), divisor factorization of
\((y-x)(y+x)=2s/d\) gives \(O_\varepsilon(s^\varepsilon)\) possible
\((b,b_s)\). For each one, reduced-product parametrization and the
divisor bound give

\[
 \#\{g,k,g',k':\Delta_s(q)=0\}
 \ll_\varepsilon X^\varepsilon GK.
\]

Thus the exact zero locus is arithmetically thin. This is a raw tuple
count, not yet a bound for its complete actual coefficient.

## 3. Near-determinant incidence

On dyadic intervals \(g,g'\asymp G\), \(k,k'\asymp K\), put
\(N=GK\) and

\[
 \alpha_{b,s}=\left({b_s\over b}\right)^{3/2}.
\]

For every \(0<\eta\le1\), reduced-product grouping gives the uniform
raw incidence bound

\[
 \#\left\{(g,k,g',k'):
 \left|{g'k\over gk'}-\alpha_{b,s}\right|\le\eta
 \right\}
 \ll_\varepsilon X^\varepsilon(\eta N^2+N).
\]

Indeed, after setting \(u=g'k\), \(v=gk'\), each \(v\asymp N\) admits
only \(O(\eta N+1)\) integers \(u\), and every product has
\(X^\varepsilon\) factorizations. On \(b,b_s\asymp A\), the band
\(|\Delta_s(q)|\le\lambda\) corresponds, up to dyadic constants, to

\[
 \eta\asymp\lambda {K\over G}A^{3/2}.
\]

Varying \(q\) provides the complementary monotonicity estimate

\[
 \#\{q,u,v:\ |u/v-\alpha_{b,s}|\le\eta\}
 \ll_\varepsilon X^\varepsilon
 \min\left\{
 D(\eta N^2+N),
 N^2\left(1+{\eta A^2\over |s|}\right)
 \right\}.
\]

This again counts tuples only. Using it in the target requires the
literal per-component actual weights, entry/exit, and owner masks; the
accepted per-ray envelope alone does not permit division by the raw
tuple density.

## 4. What happens at a carrier zero

For \(s\ne0\), a zero of \(\Delta_s(q)\) is not a flat carrier phase.
If

\[
 {g'\over k'b_s^{3/2}}={g\over kb^{3/2}}=c,
\]

then

\[
 |\Psi_s'''(q)|
 ={3X\sqrt a\over2}|c|\left|{1\over b_s}-{1\over b}\right|
 \asymp {JL|s|\over DA^3}
\]

on \(b,b_s\asymp A\), \(g,g'\asymp G\asymp L/A\), and
\(k,k'\asymp K\asymp JD/A\). Thus a lawful treatment of the near-zero
locus should use a transition between second- and third-derivative
geometry rather than declare exact determinant zeros automatically
coherent. The complete \(q\)-amplitude, however, contains sharp
arithmetic owner masks, and the coupled metric expansion replaces
\(g,g'\) by the odd mode parameters \(g-2\ell,g'-2\ell'\). A smooth
weighted derivative theorem is not available from the accepted inputs.

## 5. Structural ceiling of post-split absolute estimates

The accepted ray ledger is

\[
 P\asymp L^2\sqrt\rho,
 \qquad E_0\asymp LJD_{\rm ray}^2,
 \qquad \rho={AJD_{\rm ray}^3\over L^3}.
\]

The diagonal in the Gram is \(H\mathcal C_0^{\rm act}\). If it is
owned separately at its accepted envelope, the linear bound obtained
after the exact Cauchy bridge is \(P^2/H\). Therefore such a route
requires

\[
 H\gtrsim\rho.
\]

Because \(H\le D_{\rm ray}\), every post-expansion method that takes
absolute values after separating the diagonal is structurally confined
to the formal wedge \(\rho\lesssim D_{\rm ray}\). The actual hard cone
contains \(D_{\rm ray}\asymp1\), \(q=1\), and Pell/near-square blocks
with unbounded \(\rho\); there the nonzero determinant split has no
shift length at all. A uniform proof therefore must either obtain an
actual-symbol diagonal saving or preserve signed cancellation between
the diagonal and nonzero shifts.

Moreover, a real lower bound on \(|\Delta|\) is not a lattice
cancellation theorem when \(|\Psi''|\gtrsim1\). Discrete derivative
aliases and fourth-power recurrences must be retained; applying a
second transform to remove them is the previously accepted equal-
capacity self-return.

## 6. Weakest remaining estimates

For the capacity-compatible wedge \(1<\rho\lesssim D_{\rm ray}\), set
\(H\asymp\rho\). A sufficient nonzero-shift theorem is

\[
 \left|
 \sum_{1\le s<H}(H-s)(-1)^s
 \mathcal C_s^{\rm act}
 \right|
 \ll_\varepsilon X^\varepsilon H E_0.
\]

The determinant split reduces this to two jointly weighted tasks:

1. a separated-determinant correlation estimate with the complete
   arithmetic \(q\)-mask and discrete derivative aliases;
2. a near-determinant estimate which converts the incidence bounds
   above into coefficient-weighted mass without discarding the actual
   carrier, metric density, discrepancy modes, or entry/exit.

For \(\rho>D_{\rm ray}\), even these two post-diagonal tasks cannot
meet the frozen target. The strictly necessary extra object is the
complete half-frequency spectral projection of the actual row,
including its diagonal, on the \(D_{\rm ray}\asymp1\) sector.

## 7. Controls and provisional state effect

- The arbitrary-coefficient model \(F_a(q)=(-1)^qM_0\) saturates
  \(\mathcal G_H\asymp H^2E_0\); therefore the incidence statements
  alone cannot prove the target.
- The unsigned shadow has the same capacity.
- \(D_{\rm ray}\asymp1\), \(q=1\), and Pell/near-square rows defeat any
  uniform reliance on a nonzero shift.
- Exact determinant zeros are thin but need not be absent, and the
  weighted near locus remains open.
- Entry/exit and all profile, floor, star, metric, primitive, and owner
  factors remain inside \(F_a\); no smoothness is inferred for them.
- The fourth-power control prevents interpreting large real curvature
  as automatic discrete cancellation.
- No source theorem, canonical energy bound, M9-M2 statement, M9
  statement, or exponent follows.

Provisional recommendation: promote only the exact derivative, zero-
locus classification, and raw near-incidence lemmas if independently
certified. Retain the actual Gram open. Record the diagonal/short-ray
ceiling as a scoped mechanism obstruction, not as an actual-symbol
lower bound.
