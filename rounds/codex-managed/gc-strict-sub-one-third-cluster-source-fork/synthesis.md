# Round 95 synthesis: strict sub-one-third cluster/source fork

Campaign: `gc-strict-sub-one-third-cluster-source-fork`

Starting graph SHA-256:
`e3233f94ee0630b28c21ba102a0ee0fc55016858af6fbd61e80ea0e264128104`

## 1. Frozen objective and evidence

Round 95 asked whether the literal (W=Y^{7/16}) M1/M2 cluster
energy could be bounded by (Y^{1/2+\varepsilon}), which would give an
internal exponent (5/16), or whether the claimed Li--Yang exponent
could be certified independently as an external theorem.  The round
completed one clean statement-only rederivation, one literal
actual-symbol reduction, and one primary-source hostile audit.

The internal and external routes were adjudicated separately.  No claim
from one route is used to fill a gap in the other.

## 2. Exact internal cluster reduction

For one fixed M1 or M2 block, reduce (h/d=a/b), ((a,b)=1), and sum
all lifts ((h,d)=(ga,gb)) before taking any absolute value.  The lift
character is (chi_4(g)), while the reduced character is on (b) for
M1 and on (a) for M2.  Bounded sampled variation, including the hard
top jump and stars, gives

\[
 |A_i(a,b)|\ll_\varepsilon Y^\varepsilon L^{-1},
 \qquad
 \sum_{(a,b)=1}|A_i(a,b)|^2
 \ll_\varepsilon Y^\varepsilon D/L.
 \tag{95.1}
\]

Thus every equal-frequency lift cross term is already included in the
safe diagonal.  At the minimax block ((D,L)=(Y^{1/2},Y^{1/6})), the
diagonal is (Y^{1/3+\varepsilon}), below the cluster target.

With (kappa_1=1), (kappa_2=4), and (n=ab'-a'b), the first strict
survivor is the one-sided signed reduced-determinant correlation

\[
 \mathfrak O_i=
 2\Re\!\sum_{0<n<\kappa_i bb'/W}
 A_i(a,b)\overline{A_i(a',b')}
 e\!\left(\frac{cn}{\kappa_i bb'}\right)
 \left(1-\frac{Wn}{\kappa_i bb'}\right),
 \tag{95.2}
\]

with the literal supports, both signs, Vaaler taper, profiles, floors,
hard top, stars, and character placement retained.  The unproved target
is (mathfrak O_i\ll_\varepsilon Y^{1/2+\varepsilon}) for every hard
block.

## 3. Capacity and false-shadow controls

Farey spacing and Schur's test give only

\[
 \mathcal C_i(D,L;c)
 \ll_\varepsilon Y^\varepsilon\frac DL
 \left(1+\min\left(DL,\frac{D^2}{W}\right)\right).
 \tag{95.3}
\]

The coefficient-blind estimate is target-safe outside

\[
 \mathscr H_{95}=
 \left\{(\delta,\ell):
 \frac14\le\delta\le\frac12,
 0\le\ell\le\delta-\frac14,
 3\delta-\ell>\frac{15}{16}\right\}.
 \tag{95.4}
\]

At the minimax point it has capacity (Y^{43/48+\varepsilon}), so it
misses the (Y^{1/2+\varepsilon}) target by (Y^{19/48}).  A
phase-conjugating bounded-coefficient model attains this capacity.
Consequently random cells, exact lift aggregation, and coefficient-blind
rational spacing cannot prove the desired cluster theorem.

The source-audited Popov local moment is much sharper globally:

\[
 Q(Y,Y^{7/16})/Y^{7/16}
 \ll Y^{1/2}+Y^{9/16}(\log Y)^2.
 \tag{95.5}
\]

Its additive term misses the cluster target by only (Y^{1/16}), but
the full discrepancy estimate cannot be reversed into a bound for each
positive fixed-block cluster energy.  It therefore returns exactly the
accepted one-third exponent through persistence.

## 4. Repaired external theorem

The primary-source audit found four uniquely resolvable literal defects
in Li--Yang's v2 argument:

\[
 M<T^{7/16},\qquad H=MT^x,
 \qquad \sqrt{-1-8x}\text{ in (5.27)},
 \tag{95.6}
\]

and the circle identity must be read from Bourgain--Watt v1 (7.2).
The printed general Proposition 3.1 also omits the Guth--Maldague
condition \(\beta_2\ge0\), and the printed general Case-B comparison
misses a logarithm.  Those general statements are not accepted.

The missing small-cap condition is nevertheless valid on the exact final
circle-problem range, because

\[
 50(1-14x)(-1-8x)-(192x+47)^2
 =-(8x+3)(3908x+753)\ge0,
 \tag{95.7}
\]

and the final Case-II inequalities have fixed power slack sufficient to
absorb the missing logarithm.  Independent conductor arithmetic also
gives

\[
 27524\theta^2-13168\theta+1419=0.
 \tag{95.8}
\]

The admissible root is

\[
 \theta_{\rm LY}
 =\frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots .
 \tag{95.9}
\]

Accordingly, only the narrow repaired real-(X), inclusive theorem is
accepted as an external dependency:

\[
 \boxed{P(X)\ll_\varepsilon X^{\theta_{\rm LY}+\varepsilon}}
 \qquad(X\ge2).
 \tag{95.10}
\]

The source card records every repair and the fact that the paper remains
an arXiv preprint.  The withdrawn Bourgain--Watt theorem statements are
not imported; only its exact Section-7 identity and truncation algebra
are used and independently checked.

## 5. Ownership, endpoints, and scope

On a (Y^{7/16}) window, the moving prefix and each height have only
(O(1)) changes per scale.  Polylogarithmically many fixed strata and
blocks are assembled by cellwise Cauchy.  Bottom and R5 remain their
pointwise owners, cross-sign terms are retained, and hard top, floors,
integer jumps, and stars are not smoothed away.

The reduced-determinant theorem is pre-transform and is not either
Round-92 canonical core.  Even if proved, it would give only (5/16),
not M9-M1, M9-M2, M9, or the quarter target.  Conversely, the repaired
Li--Yang theorem is a direct external global theorem; it does not prove
the internal cluster, either canonical core, or any M9 node.

## 6. Conductor decision

Promote:

1. the exact reduced-lift diagonal and determinant reduction;
2. the coefficient-blind safe region and false-shadow no-go;
3. the completed Li--Yang source audit and the narrow repaired theorem
   (95.10).

Retain open:

1. the literal actual reduced-determinant correlation (95.2);
2. the broader non-subcoherent cluster theorem;
3. both canonical M9 cores and every outside packet;
4. M9-M1, M9-M2, M9, the conditional bridge, and the quarter target.

The strongest theorem proved from the project's own M1/M2 architecture
remains (P(X)\ll X^{1/3+\varepsilon}).  The strongest certified global
pointwise theorem overall is now the repaired external exponent
(	heta_{\rm LY}=0.3144831759\ldots).

## 7. Next proof kernel

Coefficient-blind cluster estimates are exhausted.  A future internal
cluster round must act on the literal phase and the different M1/M2
character placements in (95.2), or obtain a fixed power saving in the
additive (Y)-term of the full local discrepancy.  For the full
one-quarter program, the higher-priority terminal obligations remain the
canonical M1 hard actual-symbol Gram estimate and the canonical M2 joint
density--discrepancy energy, including their outside packets.

Round 95 is closed with a graph mutation: a strict global exponent is
certified externally, while the internal signed cluster and both M9
lanes remain open.
