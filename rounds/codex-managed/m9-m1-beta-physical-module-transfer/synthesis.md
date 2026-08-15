# Round 36 synthesis: aggregate finite routing closes the physical boundary-module interface

Campaign: `m9-m1-beta-physical-module-transfer`  
Round type: beta physical-module transfer commutation  
Graph SHA-256 before patch: `9bf9658abcbc762eba2a829c4b8ff982e2fd4a563b593bdec2373c5b1645b411`

## Conductor decision

Round 36 closes the endpoint/arithmetic boundary-module interface, but only
in the exact aggregate sense permitted by the frozen objective. It does not
prove termwise physical limits for masked faces, axes, connectors, or the
corner, and it does not yet construct the limiting endpoint-free beta axial
remainder.

At every finite (U,V,S), use one common fixed-(w) meromorphic antecedent
for the endpoint and recombined (R_1)-arithmetic package

\[
 \mathfrak M_{\rm fin}
 =\sum_{\xi\in\{1,N_X\}}D_{\xi;U,V,S}
   +\mathfrak R^{\rm ar}_{U,V,S}[R_1].                 \tag{36.1}
\]

Equivalently, before endpoint collapse,

\[
 \mathfrak M_{\rm fin}
 =\sum_\xi(T_\xi+S_\xi+P_\xi)+\mathfrak R^{\rm ar}[G],
\]

because

\[
 T_\xi+S_\xi+P_\xi=D_\xi-A_\xi,
 \qquad
 \mathfrak R^{\rm ar}[G]-\sum_\xi A_\xi
 =\mathfrak R^{\rm ar}[R_1].                         \tag{36.2}
\]

For the hierarchical partition

\[
 \Theta_\beta=\psi(\beta),\qquad
 \Theta_\alpha=(1-\psi(\beta))\psi(\alpha),\qquad
 \Theta_o=(1-\psi(\beta))(1-\psi(\alpha)),           \tag{36.3}
\]

one has, on the full product and after every face, axis, collision, and
corner restriction,

\[
 \sum_\kappa\Theta_\kappa=1,
 \quad \sum_\kappa\partial_\mu\Theta_\kappa
 =\sum_\kappa\partial_\nu\Theta_\kappa
 =\sum_\kappa\partial_\mu\partial_\nu\Theta_\kappa=0. \tag{36.4}
\]

Linearity of the complete finite two-axis product Cauchy--Green operator
(\mathsf X_{uv}) therefore gives

\[
 \boxed{
 \sum_{\kappa\in\{\beta,\alpha,o\}}
 \mathsf X_{uv}[\Theta_\kappa\mathfrak M_{\rm fin}]
 =\mathsf X_{uv}[\mathfrak M_{\rm fin}]
 =\mathfrak M_{\rm fin}.}                            \tag{36.5}
\]

The last equality is the complete finite Stokes identity: the surviving
ordinary final verticals, horizontal faces, axes, and single corner are an
alternate-contour representation of the original positive-line functional.
They do not vanish separately and are not estimated separately.

Thus the lawful order is:

1. retain finite contours and the common fixed-(w) antecedent;
2. apply every transfer stratum to all three mask shares;
3. sum the three shares, canceling all first and mixed mask connectors;
4. use finite Stokes and (36.2) to return the aggregate to
   (\mathfrak M_{\rm fin});
5. only then invoke the already accepted symmetric physical limits.

Consequently

\[
 \lim_{\rm phys}\sum_\kappa
 \mathsf X_{uv}[\Theta_\kappa\mathfrak M_{\rm fin}]
 =\lim_{\rm phys}\mathfrak M_{\rm fin}
 =\mathfrak M_{\rm phys}.                            \tag{36.6}
\]

The normalized pieces satisfy

\[
 D_1^{\rm phys}=O_W(\log X),\qquad
 D_{N_X}^{\rm phys}=O_W(1),\qquad
 \mathfrak R_{\rm phys}^{\rm ar}[R_1]=O_W(1),        \tag{36.7}
\]

so after restoring the external multiplier once,

\[
 -\frac4\pi X^{1/4}\Re\!\left(e(1/8)\mathfrak M_{\rm phys}\right)
 =O_W(X^{1/4}\log X).                                \tag{36.8}
\]

This is target-safe. The logarithm is harmless inside (X^\varepsilon).

## Exact connector, residue, and Perron scope

For a common density (Q), write (F_j) for final vertical plus
upper-minus-lower horizontals, (P_j) for the coordinate-axis residue,
and (A_j) for positive area integration. The complete masked identity is

\[
\begin{aligned}
\mathsf X_{uv}[cQ]={}&F_uF_v[cQ]+F_uP_v[cQ]+P_uF_v[cQ]+P_uP_v[cQ]\\
&-F_uA_v[(\partial_\nu c)Q]-P_uA_v[(\partial_\nu c)Q]\\
&-A_uF_v[(\partial_\mu c)Q]-A_uP_v[(\partial_\mu c)Q]\\
&+A_uA_v[(\partial_\mu\partial_\nu c)Q].          \tag{36.9}
\end{aligned}
\]

Summing (36.9) over (36.3) deletes every connector-bearing group by
(36.4). The four unmasked groups remain and together equal the original
positive-line functional. Restriction commutes with the partition identity,
so the same cancellation holds on connector axes and collision germs. A
combined artificial/arithmetic/axial residue is extracted once, and the
(P_uP_v) corner occurs once. Applying the same common operation to
(G=E_1+R_1) preserves the artificial-pole cancellation before residue
separation.

At finite height the endpoint contains an off-centred Perron kernel, not a
sharp indicator and not a starred half tie. Its tails remain inside the
aggregate until (36.5) returns them to the positive-line module. Product and
top stars arise only under the accepted symmetric physical inversion. Every
actual (W_j,phi,D_j,H_j+1), hard-top convention, (chi_4(q)), and floor
is retained.

The fixed-(w) condition is essential. After the change
(r=w-3/4-v/2), both the real part and endpoints of the (r)-path move
with (v). Freezing that path during an outside-axis displacement omits
path-boundary terms and is not covered by (36.5).

## Evidence assessment

- The statement-only blind derivation independently obtains the full
  partition/derivative cancellation and, after a conductor scope challenge,
  correctly identifies the surviving ordinary cells as the complete finite
  Stokes representation rather than a new physical remainder.
- The discovery report constructs the common finite endpoint/arithmetic
  package, preserves all actual factors, verifies the target-safe physical
  normalization, and gives the finite complement definition.
- The hostile audit independently certifies aggregate-before-limit routing,
  exposes the fixed-(w) requirement, and rejects termwise masked limits,
  early stars, and isolated (R_1) displacement.
- The conductor separately checked the partition derivative identities, the
  product-Stokes order, and the common-module convention.

No numerical experiment or external theorem was used.

## Remaining interface

Let (\mathfrak V_{\rm pre}^{\rm fin}) denote the already accepted complete
finite pre-limit vector. Round 36 gives the exact finite complement

\[
 \mathfrak V_{\rm ef}^{\rm fin}
 :=\mathfrak V_{\rm pre}^{\rm fin}-\mathfrak M_{\rm fin}. \tag{36.10}
\]

It does not prove that (36.10) has the required symmetric outside-height and
physical-profile limit, nor does it identify a limiting endpoint-free axial
symbol or estimate that symbol. This is the smallest remaining interface.
Termwise limits of the masked module cells are neither proved nor needed.

## State effect

- promote the exact global three-mask aggregate routing theorem (36.5);
- close the physical endpoint/arithmetic module interface by the exact
  finite replacement (36.6), not by termwise commutation;
- combine this with Round 35 to close boundary-module compatibility in its
  scoped sense;
- create a separate open obligation for the limit and identification of the
  endpoint-free finite complement (36.10);
- retain the complete post-module axial vector, mask compatibility, axial
  symbol bound, beta transition, M9-M1, M9-M2, M9, and the Gauss target as
  open;
- reject deletion of the ordinary unmasked cells, termwise masked physical
  limits, a frozen off-centred Perron path, finite-height stars, isolated
  (R_1) transfer through its artificial pole, and any inference that
  aggregate module routing proves the remainder limit.

Round 37 should attack exactly the existence and identity of the limiting
endpoint-free axial remainder arising from (36.10), before attempting its
weighted terminal-symbol bound.
