# Conductor partition/operator check for Round 36

Campaign: `m9-m1-beta-physical-module-transfer`  
Role: conductor independent algebra  
Allocation: 100% analytical/algebraic

Let

\[
 \Theta_1=\psi(\beta),\qquad
 \Theta_2=(1-\psi(\beta))\psi(\alpha),\qquad
 \Theta_3=(1-\psi(\beta))(1-\psi(\alpha)).
\]

Then pointwise

\[
 \sum_{r=1}^3\Theta_r=1.                            \tag{36.C1}
\]

Every first derivative and every mixed derivative also sums to zero:

\[
 \sum_r\partial_\mu\Theta_r
 =\sum_r\partial_\nu\Theta_r
 =\sum_r\partial_\mu\partial_\nu\Theta_r=0.       \tag{36.C2}
\]

For a fixed finite meromorphic density \(Q\), the complete two-axis
Cauchy--Green transfer is linear in the mask and its first/mixed
derivatives. Therefore, if all three branches use identical rectangles,
residue ownership, collisions, endpoint conventions, and regularization,

\[
 \sum_{r=1}^3\mathsf X_{uv}[\Theta_r Q]
 =\mathsf X_{uv}[Q].                               \tag{36.C3}
\]

This equality holds stratumwise:

- pure faces and pure axes use (36.C1), including restrictions to either
  axis and the corner;
- first connector faces and connector-axis residues use the corresponding
  restriction of (36.C2);
- the mixed product-area uses the last identity in (36.C2).

Thus global recombination before the physical limit eliminates all mask
connectors exactly. The remaining question is not a masked limit but the
meaning of the **unmasked transferred endpoint/arithmetic module** in
(36.C3). If finite Cauchy algebra first collapses this unmasked package to
the right-line endpoint prefixes and recombined \(R_1\) arithmetic residue,
then the accepted physical limits may be invoked without commuting a mask
through them. This is a promising exact order:

1. apply the transfer to all three finite shares;
2. sum the shares using (36.C1)--(36.C3);
3. apply the finite unmasked endpoint/artificial/arithmetic Cauchy identity;
4. take the already licensed symmetric physical limits of the unmasked
   endpoint prefixes and recombined \(R_1\) residue.

The seam to audit is whether step 1's outside-axis transfer and step 3's
radial endpoint Cauchy collapse act on independent contour variables and
commute as a finite cell identity, including artificial/arithmetic/axial
collisions. If not, their product boundary has additional mixed faces that
must be retained. No limiting theorem should be assumed merely from
(36.C3).
