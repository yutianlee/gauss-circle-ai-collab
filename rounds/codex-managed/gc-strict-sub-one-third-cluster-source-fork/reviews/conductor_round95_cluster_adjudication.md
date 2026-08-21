# Conductor review: actual rational-cluster reduction

Campaign: `gc-strict-sub-one-third-cluster-source-fork`

Starting graph SHA-256:
`e3233f94ee0630b28c21ba102a0ee0fc55016858af6fbd61e80ea0e264128104`

## Decision

Promote the exact lift aggregation, diagonal estimate, determinant
decomposition, coefficient-blind capacity classification, and scoped
no-go. Retain the actual signed determinant correlation open. No internal
strict sub-one-third exponent is proved.

## Lift and diagonal seam

For a literal M1 or M2 fixed-symbol block, reduce \(h/d=a/b\) and sum all
lifts \((h,d)=(ga,gb)\). The actual character factor is
\(\chi_4(gb)=\chi_4(g)\chi_4(b)\) in M1 and
\(\chi_4(|ga|)=\chi_4(g)\chi_4(|a|)\) in M2. The lift symbol has bounded
sampled variation, including the hard-top jump and star. Abel summation
therefore gives

\[
 |A_i(a,b)|\ll_\varepsilon Y^\varepsilon L^{-1},
 \qquad
 \sum_{(a,b)=1}|A_i(a,b)|^2
 \ll_\varepsilon Y^\varepsilon D/L.
 \tag{R95.C1}
\]

This is the complete equal-frequency diagonal after all lift cross terms,
not merely the raw \((h,d)=(h',d')\) diagonal. At the minimax block it is
\(Y^{1/3+\varepsilon}\), below the \(Y^{1/2+\varepsilon}\) cluster
target.

## Exact survivor

With \(\kappa_1=1\), \(\kappa_2=4\), and
\(n=ab'-a'b\), the non-diagonal triangular form is

\[
 2\Re\sum_{0<n<\kappa_i bb'/W}
 A_i(a,b)\overline{A_i(a',b')}
 e\!\left(\frac{cn}{\kappa_i bb'}\right)
 \left(1-\frac{Wn}{\kappa_i bb'}\right),
 \tag{R95.C2}
\]

with the literal reduced supports, both signs, Vaaler taper, profiles,
floors, hard top, stars, and character placement retained. The first
unproved statement is the one-sided signed bound

\[
 \mathfrak O_i(D,L;c,Y^{7/16})
 \ll_\varepsilon Y^{1/2+\varepsilon}
 \tag{R95.C3}
\]

on every hard block.

## Capacity and all-block audit

Farey spacing and Schur's test give

\[
 \mathcal C_i(D,L;c)
 \ll_\varepsilon Y^\varepsilon\frac DL
 \left(1+\min\left(DL,\frac{D^2}{W}\right)\right).
 \tag{R95.C4}
\]

Writing \(D=Y^\delta\), \(L=Y^\ell\), the coefficient-blind target is
safe outside

\[
 \mathscr H_{95}
 =\left\{(\delta,\ell):
 \frac14\le\delta\le\frac12,
 0\le\ell\le\delta-\frac14,
 3\delta-\ell>\frac{15}{16}\right\}.
 \tag{R95.C5}
\]

At \((\delta,\ell)=(1/2,1/6)\), (R95.C4) is
\(Y^{43/48+\varepsilon}\). Thus the strict signed gain required there is
\(Y^{-19/48}\) relative to this coefficient-blind form. A
phase-conjugating bounded-coefficient model attains the same capacity, so
random cells plus rational spacing cannot prove (R95.C3).

The accepted full-discrepancy Popov estimate is much sharper:

\[
 Q(Y,Y^{7/16})/Y^{7/16}
 \ll Y^{1/2}+Y^{9/16}(\log Y)^2.
\]

It misses the desired local mass by only \(Y^{1/16}\), but it does not
upper-bound each fixed block's positive triangular energy and therefore
cannot be reversed into (R95.C3).

## Ownership and scope

The moving prefix and height have only \(O(1)\) changes per scale on a
length-\(Y^{7/16}\) window. Polylogarithmically many fixed strata and
blocks are assembled by cellwise Cauchy. The bottom and R5 owners are
pointwise \(O(Y^{1/4+\varepsilon})\), hence target-safe in local square
mass. Cross-sign terms vanish at the minimax block and are charged to the
same-sign energies elsewhere. No owner is deleted.

This reduction is pre-transform and is not either Round-92 canonical
core. Even a proof of (R95.C3) would give only the internal exponent
\(5/16\), not M9-M1, M9-M2, M9, or \(1/4\).

Evidence reviewed:

- `reports/blind_fixed_cluster_rederivation.md`;
- `reports/actual_rational_cluster_attack.md`;
- `candidates/conductor_reduced_farey_cluster.md`;
- `reviews/conductor_round95_normalization.md`.
