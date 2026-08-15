# Round 16 synthesis: reflection completes the angular sector; it does not cancel it

Campaign: `m9-m1-reflected-mode-correlation`  
Round type: reflected-mode correlation attack  
Graph SHA-256 before patch: `7619a6b552347ce9b522018a104aeaa048304e2913ea1e072e583c0a2ace2c86`

## Conductor decision

Promote the finite-height reflected-sector identity and the scoped Perron
completion obstruction. Retain the top maximal angular correlation and GAR
as open. Functional-equation reflection has root number (+1); after exact
profile matching, the two principal-value parts are complementary and their
half residues reconstruct the completed angular coefficient. The actual M1
scale and height profiles are not reflection-invariant, so even that ideal
completion is unavailable without a new maximal angular-ratio correlation
estimate.

All three independent reports agree on the sign, crossed residues, absent
reflected scale, endpoint half weight, and failure of automatic cancellation.
No numerical experiment or new external theorem was used. No part of the
Gauss-circle target is promoted.

## Finite-height reflection and residue ledger

Let (z=u+v),

\[
 F_z(s)=\zeta(s+z/2)L(s-z/2,\chi_4),
 \qquad \Lambda_z(s)=\Lambda_{-z}(1-s),
\]

and write (G_v) for the radial Mellin transform of the exact finite radial
cutoff. On finite contour rectangles, moving the radial line through the
functional equation gives

\[
 \frac1{2\pi i}\int_{(c)}G_v(s)F_z(s)\,ds
 =G_v(1-z/2)L(1-z,\chi_4)
 +\frac1{2\pi i}\int G_v(1-s)K_z(1-s)F_{-z}(s)\,ds,
\]

with the terminal line and finite horizontal pieces retained until the
rectangle is closed. Here (K_z) is the exact quotient of completed gamma
factors. Gamma poles are not counted separately when their paired trivial
zeros are kept in the intact completion.

Putting the reflected integral back into the original positive Mellin
chamber crosses the following nonzero terms:

1. the arithmetic pole (s=1-z/2) of the zeta factor;
2. the height pole (v=0) of (widehat\phi(v));
3. at the unique hard top, the spatial Perron pole (u=0) of
   (widehat W_+(u)=1/u+widehat W_{+,r}(u));
4. any radial endpoint half residue introduced by an auxiliary Perron
   representation.

The completed root number is (+1): (	au(\chi_4)/(i\sqrt4)=1), and
zeta also has sign (+1). There is consequently no global minus sign that
could remove these residues. The limit of the finite rectangles, including
their horizontal sides and the top (1/u) truncation, remains an open
maximal problem.

## Exact profile-sector comparison

For a divisor incidence (n=hq), set

\[
 d_{h,q}=2\sqrt X\sqrt{h/q},
 \qquad A_D(h,q)=\frac{D}{d_{h,q}}.
\]

In the original centered mode, the (u)-factor is (A_D(h,q)^u) and the
(v)-factor is (((H_D+1)/h)^v). Replacing (a_z) by (a_{-z}) reverses
both divisor-ratio powers, producing

\[
 \left(\frac{D}{2\sqrt X}\sqrt{h/q}\right)^u
 \left(\frac{H_D+1}{q}\right)^v
 =A_{4X/D}(h,q)^{-u}
 \left(\frac{H_D+1}{q}\right)^v.
\]

Thus exact angular complementarity would require (D\mapsto4X/D), a
height cutoff on the other divisor, and reflected floor/Vaaler profiles.
For every actual M1 scale (D\le\sqrt X), the required scale satisfies
(4X/D\ge4\sqrt X) and is absent. Reindexing (h\leftrightarrow q)
moves (chi_4) to the other variable, but still does not reproduce actual
M2: the factor-four lattice, cone, Vaaler variable, and endpoint profile
differ, and the accepted top transform has the same leading sign as M1.

## Perron completion law

For a finite exponential polynomial (F(u)=\sum_\nu c_\nu A_\nu^u),
symmetric Perron inversion gives

\[
 \mathscr P(F)=\sum_\nu c_\nu
 \left(\mathbf1_{A_\nu>1}+\tfrac12\mathbf1_{A_\nu=1}\right).
\]

Consequently

\[
 \boxed{\mathscr P(F)+\mathscr P(F(-\cdot))=\sum_\nu c_\nu,}
\]

whereas their difference is the angular-sign projector. The principal-value
integrals reverse sign, but the two (1/2) residues have the same sign.
Therefore perfect reflection gives the full angular completion, not zero.
At the joint zero mode that completion has (a_0(n)=r_2(n)/4), the already
accepted Hardy--Voronoi return. Exact controls agree: (a_z(5)=a_{-z}(5)),
and the active incidence ((h,q)=(1,5)) has no actual reflected partner.

## Smallest surviving kernel

After the completed residues are separated, the remaining top route is a
maximally truncated angular-sign sum of the form

\[
 \sup_T\left|
 \sum_{hq\le16\sqrt X}\chi_4(q)(hq)^{-3/4}e(\sqrt{Xhq})
 \mathcal H_{T,X}(h,q)
 \right|\ll_\varepsilon X^\varepsilon,
\]

where (mathcal H_{T,X}) is the exact scale sum with height floors,
(Phi), endpoint stars, smooth remainders, and the truncated Perron kernel
in (log(D/d_{h,q})). Plancherel alone replaces this by a near-equal-ratio
correlation with no accepted spacing theorem; pointwise fixed-mode Voronoi
bounds likewise do not control the maximal limit.

The next useful algebraic question is whether the local coefficients
(a_z(n)) and (a_{-z}(n)) admit an exact arithmetic eigenspace
decomposition, including the prime (2), that simplifies this maximal
kernel before another analytic estimate is attempted. That possible
identity is not promoted in Round 16.

## State effect

- promote the finite-height reflected-sector and residue identity;
- promote the Perron-completion/profile-mismatch no-go;
- retain the exact maximal angular-sign kernel as open;
- reject automatic (z/-z), (1/u), M1/M2, and generic Hilbert-space
  cancellation claims;
- leave GAR, M9-M1, M9-M2, M9, and the target open.

