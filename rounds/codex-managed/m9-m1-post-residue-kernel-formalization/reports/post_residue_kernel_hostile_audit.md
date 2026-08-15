# Post-residue kernel hostile audit

## 1. Result

**OBSTRUCTION / REVISE.** The Round-16 functional-equation (FE) remainder cannot presently be separated as a scalar incidence multiplier
\(\mathcal H_{T,X}(h,q)\) with
\(\sup_{T,h,q}|\mathcal H_{T,X}(h,q)|\ll\log X\).
That bound is valid for the *pre-FE physical profile* (and for the bare
symmetric Perron projector), but not for the post-FE expression as recorded.
The first hidden dependence is the radial Mellin/Hankel operator
\[
G_v(1-s)K_{u+v}(1-s),
\]
whose inverse is a kernel in an additional dual radial index. It is neither
a bounded scalar function of the original incidence \((h,q)\) nor shown
uniformly integrable in the coupled \(u,v,s\) heights. The high-\(2\)-adic
tail therefore remains conditional.

## 2. Exact statement and hypotheses

Let \(a,b>0\), \(z=u+v\), and on finite rectangles write
\[
A_j(u,v)=\widehat W_j(u)\widehat\phi(v)
\left(\frac{D_j}{2\sqrt X}\right)^u(H_j+1)^v,
\quad
g_v(x)=x^{-3/4-v/2}e(\sqrt{Xx})1_{[1,N_X]}^*(x).
\]
Round 16 establishes only
\[
\sum_n a_z(n)g_v(n)
=R_z(v)+\frac1{2\pi i}\int G_v(1-s)
K_z(1-s)F_{-z}(s)\,ds,
\tag{1}
\]
with finite horizontal sides retained, where \(R_z(v)\) is the crossed
zeta-pole term. Returning \(u,v\) to the chosen chamber also crosses the
height pole \(v=0\), the unique top pole \(u=0\), and any deliberately
introduced radial endpoint half residue. Gamma poles are not separate
residues when the intact completion and its trivial zeros are retained.

The audited claim would need an identity, uniformly in finite truncations,
\[
\text{post-residue remainder}
=\sum_{\substack{hq\le N_X\\q\ {\rm odd}}}
\chi_4(q)(hq)^{-3/4}e(\sqrt{Xhq})
\mathcal H_{T,X}(h,q),
\tag{2}
\]
followed by a termwise \(O(\log X)\) bound. No supplied artifact proves (2).

## 3. Proof or derivation

The elementary profile pieces are harmless. For \(A>0\),
\[
\frac1{2\pi}\operatorname{PV}\int_{-T}^{T}\frac{A^{it}}{it}\,dt
=\frac1\pi\int_0^T\frac{\sin(t\log A)}t\,dt=O(1)
\]
uniformly in \(A,T\); equality \(A=1\) is handled by the prescribed half
residue. Thus the bare top Perron factor is uniformly bounded only under
symmetric truncation, never by \(\int|dt/t|\). The spatial smooth remainder
\[
-\frac1u\int_0^1W'(t)t^u\,dt
\]
has fixed vertical \(L^1\) norm, while \(\widehat W\) for interior scales is
rapid. Likewise \(\widehat\phi(b+i\nu)\ll_b(1+|\nu|)^{-3}\) on a positive
line; its inverse is exactly
\(\phi(h/(H_j+1))\), so the floor \(H_j\), \(\Phi\), and height endpoint are
bounded. Endpoint stars lie in \(\{0,\frac12,1\}\), and there are
\(J+1=O(\log X)\) actual scales. These facts prove an \(O(\log X)\)
pointwise bound for the direct Round-15 profile sum.

They do **not** prove the same assertion after (1). Expanding
\(F_{-z}(s)=\sum_m a_{-z}(m)m^{-s}\) produces
\[
\sum_m a_{-z}(m)\,
\frac1{2\pi i}\int G_v(1-s)K_z(1-s)m^{-s}\,ds,
\tag{3}
\]
a dual radial transform. The gamma quotient \(K_z\) couples
\(\Im s\) to \(\Im z=\Im u+\Im v\); \(G_v\) also depends on \(v\) and on the
hard finite radial cutoff. Neither Round 15 nor 16 gives an \(L^1\) majorant
for this triple-height kernel uniform in \(u,v,T\), nor a pointwise inverse
that returns the original phase \(e(\sqrt{Xhq})\). Indeed Round 15 explicitly
withheld uniform large-\(|\Im z|\) localization. Consequently absorbing
(3), the finite horizontal sides, or their limit into a scalar
\(\mathcal H_{T,X}(h,q)\) assumes the open vector-valued Voronoi/maximal
control.

Residue subtraction does not repair this. The zeta residue
\(G_v(1-z/2)L(1-z,\chi_4)\) is a global radial quantity, not incidencewise.
The height and top residues leave axial transforms; only the joint
antisymmetric residue vanishes. They must be estimated separately rather
than declared part of a bounded scalar multiplier.

## 4. First doubtful or unproved step

The first invalid step is exchanging the reflected \(s\)-integral and the
\(u,v\) inversions, then naming their inverse a bounded scalar
\(\mathcal H_{T,X}(h,q)\). At finite rectangles this inverse depends on the
dual radial index and all three truncations. Passing to infinite height also
requires the horizontal sides to vanish uniformly. Both demands are exactly
the open complex-shift radial correlation, not consequences of one-variable
Perron or BV inversion.

## 5. Required control test and outcome

Remove the FE and retain only the Round-15 profiles. Symmetric Perron,
height inversion, stars, floors, smooth remainders, and the scale sum give
\[
\sup_{T,h,q}|\mathcal H^{\mathrm{direct}}_{T,X}(h,q)|
\ll\log X .
\]
This control **passes** and identifies the legitimate scope.

Now retain the FE term (3). It contains an extra summation variable \(m\)
and the nonseparable kernel
\(G_v(1-s)K_{u+v}(1-s)m^{-s}\); there is no algebraic
\(\delta_{m=hq}\) or accepted uniform \(L^1\) estimate collapsing it to
\((h,q)\). The proposed scalar post-FE representation therefore **fails
the definition test**. This is an exact structural failure, not a numerical
counterexample.

## 6. Dependencies and exact artifacts used

Used `protocol.md`, `state/proof_obligations.yml`,
`state/active_campaign.yml`; Round-15 `synthesis.md` and
`reports/blind_double_mellin_derivation.md`; Round-16 synthesis and its
three reports; Round-17 `synthesis.md`; and the assigned Round-18 brief.
No other Round-18 work, external source, or numerical experiment was used.

## 7. Recommended state effect

Promote the scoped obstruction: one may promote the \(O(\log X)\) bound only
for the explicitly inverted direct profile/Perron kernel, not for the
post-FE radial remainder. Keep
`M9-M1-high-2adic-kernel-pointwise-bound` open and
`M9-M1-high-2adic-tail-conditional` conditional. Replace the schematic
scalar \(\mathcal H\) by a vector kernel
\(\mathcal K_{T,X}(h,q;m)\) (or a three-contour operator), list the zeta,
height, top, and radial endpoint residues outside it, and require a uniform
Stirling/Hankel plus horizontal-side theorem before any tail promotion.
GAR, the maximal angular-sign kernel, M9-M1, M9, and the target remain open.
