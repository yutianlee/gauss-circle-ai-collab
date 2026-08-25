# Conductor control: moving determinant wedge versus a standard S rectangle

Campaign: `gc-w7-16-bombieri-iwaniec-two-spacing-source-map`

Starting graph SHA-256:
`465093c00a388ff9e49583a8016e0e580f74beea4656b15884fdd9dc9247be5a`.

This is an independent geometric and capacity control.  It makes no source
applicability claim.

## 1. Fixed-outer moving wedge

Fix one top-shell outer ray \(r=(a,b)\).  From

\[
 0<n=ab'-a'b\lesssim{bb'\over W}
\]

one obtains

\[
 0<{a\over b}-{a'\over b'}\lesssim{1\over W}.             \tag{133.W1}
\]

For each \(b'\asymp D\), the allowed inner numerator lies in the one-sided
interval

\[
 a'={a\over b}b'-{n\over b},
 \qquad 0<{n\over b}\lesssim {D\over W}.                 \tag{133.W2}
\]

of length

\[
 H_0={D\over W}=Y^{3/48}.                                \tag{133.W3}
\]

The centre in (133.W2) drifts at slope \(a/b\asymp L/D\).
To keep this drift within \(O(H_0)\), a denominator cell may have length at
most

\[
 M_0={H_0D\over L}={D^2\over WL}=Y^{19/48}.              \tag{133.W4}
\]

Thus a full \(b'\asymp D\) shell needs

\[
 {D\over M_0}={WL\over D}=Y^{5/48}                       \tag{133.W5}
\]

such cells.  These are the same cell-count scales already present in the
accepted capacity ledger.

## 2. Why this is not a source S box for free

On one cell, \(a'\) has **absolute scale** \(L=Y^{8/48}\) but available
length \(H_0=Y^{3/48}\); \(b'\) has absolute scale \(D=Y^{24/48}\) but
cell length \(M_0=Y^{19/48}\).  A fixed-BV source weight can localize a
shorter interval inside its ambient dyadic scale, so short support alone
is not an obstruction.  The issue is that the interval in (133.W2) moves
with \(b'\), and the source estimate gives no automatic credit for its
shorter length.

Translating \(a'=a_0+u\) does not simply create the source phase with
\(H=H_0\):

\[
 e\!\left(-{ca'\over\kappa_i b'}\right)
 =e\!\left(-{ca_0\over\kappa_i b'}\right)
  e\!\left(-{cu\over\kappa_i b'}\right).                 \tag{133.W6}
\]

The first factor in (133.W6) is a reciprocal oscillation in \(b'\), not a
bounded-variation amplitude.  Keeping the original source scale
\(H=L,M=D\) avoids this translation seam but gives no \(H_0,M_0\) length
credit.  Treating the moving boundary by rectangle decomposition must price
the \(Y^{5/48}\) cells and all owner changes.

## 3. Source final-range control

If one formally used \(H_0\) and \(M=D\), then

\[
 {H_0\over M}=Y^{-7/16},                                  \tag{133.W7}
\]

which lies below the source final hard range
\(H/M>T^{-3/8}\).  This does not prove that the cell is unestimable: the
source uses elementary one-dimensional estimates below that range.  It does
prove that the optimized \(q>4\) first-spacing conclusion cannot simply be
reused with \(H=H_0\).

Using the full single-wave scales instead gives

\[
 {H\over M}=Y^{-1/3}                                      \tag{133.W8}
\]

and the exact optimized one-wave exponent

\[
 \Phi(-1/3)={29+5\sqrt{170}\over300}.                    \tag{133.W9}
\]

The source conclusion is then a bound for one separably weighted
\(S/H\).  The project target is a joint determinant-restricted pair scalar.
Any comparison of (133.W9) with \(35/48\), \(27/48\), or \(24/48\) must
first state whether the connector uses one source sum, two source sums, a
row sum, or a spacing energy, and must include every normalization.  No such
connector is assumed here.

## 4. Variable-role control

The project ray \((a,b)\) maps to the source summation point \((h,m)\) in
the exact single-wave identity.  The source reduced fraction
\(a_{\rm BI}/r_{\rm BI}\) is created only later as an approximation to a
derivative on an \(m\)-interval of length \(N\).  At the critical source
tuple,

\[
 {a_{\rm BI}\over r_{\rm BI}}\asymp {T\over M^2}\asymp1,
 \qquad {a\over b}\asymp Y^{-1/3},
 \qquad r_{\rm BI}\asymp Q\le H=Y^{1/6},
 \qquad b\asymp Y^{1/2}.                                  \tag{133.W10}
\]

Therefore the determinant restriction between project rays supplies no
automatic proximity in the four second-spacing coordinates involving
\(\bar a_{\rm BI}/r_{\rm BI}\), \(c_0\), \(\mu\), and \(\kappa_0\).

## 5. Control outcome

The exact phase match survives, but the determinant restriction produces a
moving short wedge rather than a source rectangle, and the source spacing
rationals are not project rays.  The first prospective connector must
simultaneously control moving-boundary decomposition, separated BV weights,
the joint coefficient, and the derivative-approximant role map.  Without
that connector no source or exponent effect is licensed.

No numerical experiment was used.
