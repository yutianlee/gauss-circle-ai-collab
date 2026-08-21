# Conductor review: literal owner dictionary and blockwise norms

Campaign: `m9-m2-blockwise-owner-completion`

Starting graph SHA-256:
`f861f43d46bec112682a73e4c6062cbebf82f83fdcf0639e6fe122c6a123ad0d`

This review fixes the objects whose absence is correctly identified by
the statement-only report.  It is a linear scalar completion, before a
second Gram lift.

## 1. Atomic completion and priority

Fix a half-open dyadic label

\[
 B=(A,D,K,G,R,\sigma)
\]

and inherit every Round-92 tie convention.  The orientation tag records
only the representative (a<b); the single outer (2\Re) supplies its
conjugate.  It is not a second full orientation sum.  An atom of the completed
collared block is a tuple

\[
 z=(B,a,b,k,g)
\]

with primitive odd \(a<b<4a\), the literal dyadic cutoffs, the actual
finite odd lift support, \(k\) on the fixed half-open lattice
\(k\asymp K\), the complete centred integral, and one smooth
metric member \(W_R(\Lambda/k)\).  The metric density is part of this
coefficient.  It is not an owner.

Here is an exact smooth reconstruction.  Choose a nonincreasing
\(\eta\in C^\infty([0,\infty))\), constant one on
\([0,1/2]\) and zero on \([1,\infty)\), and put

\[
 V_R(t)=\eta(R\|t\|),\qquad
 W_R(t)=V_R(t)-V_{2R}(t).
\]

For the dyadic lift scale \(G_*\asymp G\), telescope over dyadic
\(1\le R<G_*\) and retain the smooth terminal member \(V_{G_*}\):

\[
 1_{t\notin\mathbb Z}
 =\sum_{1\le R<G_*}^{\rm dyadic}W_R(t)
   +V_{G_*}(t)-1_{t\in\mathbb Z}.
\tag{109.D0}
\]

The choice makes \(V_1\equiv1\) on the circle.  All terms before the
last point selector are smooth, have Fourier scale \(R\le G_*\), and
include their mean.  The terminal member equals one at an exact centre;
the final arithmetic atom removes that value exactly.  Thus (109.D0)
avoids the impossible requirement that a continuous terminal window be
one arbitrarily close to an exact centre and zero at the centre.

Give every nonzero atom the following first-applicable label:

1. `77-ext`: \(k\) is outside the strict reciprocal saddle interval,
   including equality and zero-extension jumps;
2. `78-square`: \(k\) is inside that interval and \(ab\) is a square,
   with the exact-centre subtraction in (109.D0) retained;
3. `79-centre`: \(ab\) is nonsquare and \(\Lambda/k\in\mathbb Z\),
   again as the point subtraction in (109.D0);
4. `79-safe`: the block lies in the fixed bounded \(\rho\)-boundary
   region, with the half-open tie assigned to the safe side;
5. `103-104-short`: the row lies in the prescribed singleton or
   polylogarithmic \(q=(b-a)/2\) range, after the preceding owners;
6. `res`: every remaining atom.

The original Round-75 diagonal and the Round-77 primal endpoint/collar
samples are not atoms of this oriented completed sum.  They remain in
the already accepted positive owner term.  This prevents their being
counted a second time.  Likewise, finite orientations are represented
by \(\sigma\); the energy contains one positive orientation followed
by the single outer \(2\Re\).

Let \(\mathfrak O_{B,\nu}\) be the sum of the complete amplitudes of
the atoms carrying label \(\nu\), and let
\(\mathfrak Q_B^{\rm res}\) and
\(\mathfrak Q_B^{\rm comp}\) be the `res` and all-atom sums.  Then the
priority partition gives coefficient by coefficient

\[
 \mathfrak Q_B^{\rm res}
 =\mathfrak Q_B^{\rm comp}
  -\sum_{\nu\ne{\rm res}}\mathfrak O_{B,\nu}.
\tag{109.D1}
\]

No cancellation or estimate is used in (109.D1).

## 2. Round-77 fixed-lattice extension

For one collared ordered pair, the accepted Round-77 first-derivative
bound for the nearby nonstationary modes and two integrations by parts
for the tails give \(O(\log(2+L))\).  The proof takes absolute values
per ordered pair.  Multiplication by one smooth \(W_R\), zero
extension to a half-open dyadic \(k\)-lattice, and locally finite
summation in \(R\) preserve this bound.  There are \(O(L^2)\) ordered
pairs and only logarithmically many dyadic labels.  Therefore

\[
 \sum_B|\mathfrak O_{B,77\text{-ext}}|
 \ll_\varepsilon L^2X^\varepsilon.
\tag{109.D2}
\]

The original Poisson zero mode is in the accepted Round-77 error.  The
Fourier coefficient \(\widehat W_R(0)\) remains inside every completed
atom, so (109.D2) does not delete the metric density.

The physical integration interval also causes no new sharp mask.  The
two real-affine collars are literal factors of the separated amplitude;
after zero extension the integrand vanishes outside the physical
range.  Original full samples and stars remain in the Round-77 owner.

## 3. Square, exact-centre, and safe owners

The smooth annular and terminal square owner is treated by the
metric-resolved refinement
in `conductor_round109_preliminary_owner_bridge.md`.  It gives

\[
 \sum_B|\mathfrak O_{B,78\text{-square}}^{\rm smooth}|
 \ll_\varepsilon L^2X^\varepsilon.
\tag{109.D3}
\]

The point selector in (109.D0) is inserted separately.  For square rays
its absolute cost is directly target-safe: an exact centre forces
\(2Xu^2\in\mathbb Z\) and \(k\mid2Xu^2\), so divisor counting and the
Round-78 supremum give

\[
 \sum_{s,u,g}\sum_{\substack{k\in I_{s,u}\cap\mathbb Z\\
                         2Xu^2/k\in\mathbb Z}}
 \sqrt{gt^2/K}
 \ll_\varepsilon {L^{3/2}\over\sqrt J}X^\varepsilon
 \ll L^2X^\varepsilon.
\tag{109.D4}
\]

For nonsquare rays, the accepted Round-79 exact-centre total is
\(O_\varepsilon(LX^\varepsilon)\).

The \(\rho\)-boundary is assigned by a fixed half-open dyadic priority:
every block meeting \(\rho\asymp1\) is put on the positive-safe side,
and the strict residual begins only beyond the fixed overlap.  The
accepted positive capacity is

\[
 A\sqrt G\sqrt J D^{3/2}
 =\sqrt{ALJD^3}\le C L^2
\]

on this bounded-safe region.  Hence

\[
 \sum_B|\mathfrak O_{B,79\text{-safe}}|
 \ll_\varepsilon L^2X^\varepsilon.
\tag{109.D5}
\]

This is an outside-absolute positive bound, not a signed-to-absolute
conversion.

## 4. Singleton and prescribed short rows

On the singleton owner, Cauchy and the accepted Round-103 energy give

\[
 \left|\sum_{a\asymp A}F_a(1)\right|
 \le A^{1/2}
 \left(\sum_{a\asymp A}|F_a(1)|^2\right)^{1/2}
 \ll_\varepsilon L^2X^\varepsilon.
\tag{109.D6}
\]

On a fixed short shell \(q\asymp D\), Round 104 similarly gives

\[
 \left|\sum_{a,q}(-1)^qF_a(q)\right|
 \le (AD)^{1/2}
 \left({DL^4\over A}\right)^{1/2}X^\varepsilon
 \ll_\varepsilon D L^2X^\varepsilon.
\tag{109.D7}
\]

For the prescribed polylogarithmic range, the final factor \(D\) and
all dyadic shells are absorbed in \(X^\varepsilon\).  The accepted
short-row statements already retain primitivity, prior-owner masks,
punctured density plus discrepancies, floors, stars, collars, both
orientations, and zero extension.  With the priority in Section 1,
there is no overlap with square, exact-centre, or safe atoms.

## 5. Projective costs and strong norm

The smooth difference cutoff separates with bounded Fourier
\(L^1\)-cost.  Möbius separation of primitivity costs
\(\sum_d d^{-3/2}<\infty\) after the actual denominator weights.
Finite orientations and logarithmically many dyadic and metric labels
cost \(X^\varepsilon\).  These operations preserve the direct scalar
norms (109.D2)--(109.D7); they do not create those norms.

Combining the disjoint owners yields

\[
 \boxed{
 \sum_B\sum_{\nu\ne{\rm res}}
 |\mathfrak O_{B,\nu}|
 \ll_\varepsilon L^2X^\varepsilon.}
\tag{109.D8}
\]

Consequently

\[
 \sum_B|\mathfrak Q_B^{\rm res}|
 \le \sum_B|\mathfrak Q_B^{\rm comp}|
      +O_\varepsilon(L^2X^\varepsilon).
\tag{109.D9}
\]

The weaker sharp block-transfer norm is
\(\sum_B|\sum_\nu\mathfrak O_{B,\nu}|\).  The proof above establishes
the stronger ownerwise norm rather than inferring it from the accepted
aggregate energy.

## 6. Scope

Equations (109.D1)--(109.D9) license only the fixed-lattice completed
linear scalar vector.  They do not estimate that vector.  They do not
commute a sharp owner through a Fejer or positive Gram operator, and
they give no cross energy for reinserted owners.  Round 108 therefore
still rules out a free \(\rho\)-gain from Gaussian functional calculus.

The canonical hard density-discrepancy estimate, the hard signed cone,
the balanced and unbalanced smooth packets, \(M9\! -\! M2\),
\(M9\! -\! M1\), endpoint uniformity, \(M9\), and every new exponent
remain open pending hostile adjudication of this dictionary.
