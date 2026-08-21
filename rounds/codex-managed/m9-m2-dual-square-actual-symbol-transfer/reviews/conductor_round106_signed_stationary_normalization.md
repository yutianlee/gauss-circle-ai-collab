# Conductor review: signed stationary normalization and Fresnel gate

Campaign: m9-m2-dual-square-actual-symbol-transfer

Round: 106

## Verdict

The strict smooth-interior calculation is correct after one mandatory
sign repair. For one orientation put

\[
 c=\nu-\tau g/2,\qquad n=2|c|,\qquad
 \epsilon=\operatorname {sgn}(c).
\]

After the exact primitive split \(q=du\), \(d\mid a\), the two Poisson
labels at a joint interior saddle may be written

\[
 m=-\epsilon\ell,\qquad d-2h=-\epsilon r,\qquad
 \ell>0,\quad r>0\text{ odd}.
\]

The stationary data are

\[
 y_*^2={\ell\over n},\qquad
 k_*^2={n\Lambda_{du}\over2\ell},\qquad
 b_*={4d^2Xn\ell\over r^2},
\]

and the stationary value is

\[
 \epsilon\left(J\sqrt{dn\ell/r}
       -{1\over2}\sqrt{ar/d}\right)^2.
\]

Thus the negative square in the Round-105 carrier is only the
\(c<0\) branch. Every fixed orientation contains both signs as \(\nu\)
varies.

## Constant audit

The physical, \(k\)-, and \(u\)-stationary signatures are respectively
\(+1,\epsilon,-\epsilon\). Their Gaussian units therefore multiply to

\[
 e(1/8)e(\epsilon/8)e(-\epsilon/8)=e(1/8).
\]

The three half-density factors and the physical Jacobian give the
strict-interior principal coefficient

\[
 e(1/8){g^{1/2}b_*^{3/4}\over
 dJ^{1/2}n^{3/4}\ell^{1/4}}
 A^\circ_{ga,gb_*}(g\ell/n).
\]

There is no missing factor of \(2\), \(d\), \(g\), \(n\), or \(\ell\),
and no progression-density factor is introduced when the integer \(h\)
is reindexed by the odd integer \(r\).

## Complete physical coefficient

The preceding point value is only the zeroth resolved symbol. With

\[
 Q_{a,b,g}(y)=2gyA^\circ_{ga,gb}(gy^2),
\]

the exact normalized physical Fresnel functional is

\[
 \mathcal C_{a,b,g}(k,z)
 =e(-1/8)\sqrt{2gk}
  \int Q_{a,b,g}(y)e(gk(y-z)^2)\,dy.
\]

It agrees with \(Q(z)\) only to leading order on a strict smooth
interior. At either physical collar, a reciprocal entry or exit, a
maximal endpoint, a lift endpoint, a hard sample, or the collapsing cone
edge, the complete one- or multi-sided Fresnel vector must be retained.
No accepted estimate sums the difference between this vector and its
point value in the per-base maximal norm.

## Capacity check

For the scalar two-variable phase, the stationary half-density is the
inverse square root of the frequency-map Jacobian. Hence local
\(L^2\)-density is preserved. On a nondegenerate shell the dual scalar
packet has natural square-sum capacity \(\asymp\sqrt{LD/d}\), exactly the
primal scalar capacity. Full Hessian rank supplies no additional
\(D^{-1/2}\) or \(D^{-1}\) factor.

## State recommendation

Promote the signed strict-interior normalization and local density
identity. Do not promote a uniform complete actual-symbol expansion,
any transition remainder, a maximal theorem, or a polynomial shell.

