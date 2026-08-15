## 1. Result

**Scoped certification by aggregate-before-limit routing, not termwise commutation.** Let the endpoint and recombined \(R_1\)-arithmetic terms be kept as one common finite meromorphic package, and apply the same finite \(u,v\) rectangles and combined-residue convention to all three hierarchical masks. Then, at every finite \(U,V,S\), the sum of the three complete sixteen-stratum transfers is exactly the unmasked finite package. All first-derivative, connector-axis, and mixed-derivative connectors cancel before any limit. The remaining unmasked complete transfer equals the original positive-line package by finite Cauchy--Green, so its already-licensed physical limit is target-safe.

This proves
\[
 \lim_{\rm phys}\sum_{\kappa}\mathsf X_{uv}
       [\Theta_\kappa\mathfrak M_{\rm fin}]
 =\mathfrak M_{\rm phys},                                                \tag{36.1}
\]
but does **not** prove that any individual masked stratum has a physical limit or may be bounded by the physical module theorem. Finite Perron tails are not canceled; they stay inside the recombined unmasked endpoint and become sharp support/stars only in the licensed symmetric limit. The lawful architecture is therefore to remove the global module before localization and transfer only the finite endpoint-free remainder.

## 2. Exact statement and hypotheses

Put
\[
 \Theta_\beta=p,\qquad
 \Theta_\alpha=(1-p)q,\qquad
 \Theta_o=(1-p)(1-q),                                                     \tag{36.2}
\]
where \(p=\psi(\beta)\), \(q=\psi(\alpha)\),
\[
 \alpha=t+\frac{\mu+\nu}{2},\qquad
 \beta=t-\frac{\mu+\nu}{2}.
\]
Thus \(\sum_\kappa\Theta_\kappa=1\).

Let \(\mathfrak M_{\rm fin}(U,V,S)\) be the common finite \(M=1\) package obtained from
\[
 T_\xi+S_\xi+P_\xi=D_{\xi;U,V,S}-A_{\xi;U,V},\qquad
 R^{\rm ar}[G]-\sum_\xi A_\xi=R^{\rm ar}[R_1],                           \tag{36.3}
\]
after pairing the opposite artificial \(E_1/R_1\) residue, but before any physical profile limit. Equivalently,
\[
 \mathfrak M_{\rm fin}
 =\left[\sum_{\xi\in\{1,N_X\}}D_{\xi;U,V,S}
       +R^{\rm ar}_{U,V}[R_1]\right]_{\rm common},                        \tag{36.4}
\]
where “common” means that an artificial/arithmetic/axial collision is evaluated from the unsplit meromorphic antecedent as one combined derivative residue, not by shifting the displayed summands independently.

Assume the three masks use identical finite rectangles, directions, profiles, floors, endpoint conventions, and regulators, and sum their complete transfer cell complexes before taking the accepted symmetric physical net. Then (36.1) holds. It is an aggregate theorem only.

The finite representative used for the transfer must be the original
fixed-\(w\)-segment meromorphic integral underlying \(D_{\xi;U,V,S}\), not
the off-centred Perron formula with its moving \(r=w-p(v)\) path treated as
an ordinary fixed-domain function of \(v\). In the latter coordinates both
the real part and endpoints of the \(r\)-path move with \(v\); freezing them
would omit path-boundary terms.

## 3. Proof or derivation

For a general \(C^2\) weight \(c(\mu,\nu)\), the finite two-axis formula can be written
\[
\begin{aligned}
\mathsf X_{uv}[cQ]={}&F_uF_v[cQ]+F_uP_v[cQ]+P_uF_v[cQ]+P_uP_v[cQ]\\
&-F_uA_v[(\partial_\nu c)Q]-P_uA_v[(\partial_\nu c)Q]\\
&-A_uF_v[(\partial_\mu c)Q]-A_uP_v[(\partial_\mu c)Q]\\
&+A_uA_v[(\partial_\mu\partial_\nu c)Q],                                 \tag{36.5}
\end{aligned}
\]
where \(F_j\) is final vertical plus upper-minus-lower horizontals,
\(P_j\) is the coordinate-axis residue, and \(A_j\) is positive area integration. Every collision is included in \(P_j\) through the common-residue convention.

On functions of \((\alpha,\beta)\),
\[
 \partial_\mu=\partial_\nu
 =\frac12(\partial_\alpha-\partial_\beta).
\]
Therefore (36.2) gives pointwise on the full product and on every face, axis, and corner,
\[
 \sum_\kappa\Theta_\kappa=1,\qquad
 \sum_\kappa\partial_\mu\Theta_\kappa
 =\sum_\kappa\partial_\nu\Theta_\kappa=0,\qquad
 \sum_\kappa\partial_\mu\partial_\nu\Theta_\kappa=0.                      \tag{36.6}
\]
Restriction commutes with these identities. At \(v=0\), \(u=0\), and \(u=v=0\), the three restricted masks still sum to one; all restricted connector densities still sum to zero. At a higher-order collision, the Leibniz terms involving derivatives of the masks cancel because every positive-order derivative of their sum is zero.

Summing (36.5) over \(\kappa\) consequently yields
\[
 \sum_\kappa\mathsf X_{uv}[\Theta_\kappa Q]
 =\mathsf X_{uv}[Q].                                                      \tag{36.7}
\]
The right side contains the unmasked final faces and axial/corner residues but no mask connectors. The ordinary outside-axis faces do **not** vanish
termwise: every pure-boundary and boundary-axis term survives with
unmasked coefficient one. They have no independent survivor because,
together with the shifted verticals and combined residues, they are exactly
the full unmasked contour identity. Since \(\mathsf X_{uv}\) is the
complete, not truncated, contour transfer,
\[
 \mathsf X_{uv}[Q]=V_{u,+}V_{v,+}[Q].                                   \tag{36.8}
\]
Apply (36.7)--(36.8) to the common package (36.4). The artificial \(E_1/R_1\) residues cancel before separate extraction. If the artificial and arithmetic poles coincide, (36.7) applies to their single derivative coefficient; if an axial divisor also meets it, one common iterated coefficient is used. Hence no residue or corner is counted twice.

The finite endpoint representative contains the off-centred kernel
\[
 \mathcal P^\gamma_{S,\nu}(y)
 =\frac1{2\pi i}\int_{\gamma-i(S+\nu/2)}^{\gamma+i(S-\nu/2)}
   \frac{y^r}{r}\,dr.                                                     \tag{36.9}
\]
At finite \(S\), (36.9) has neither sharp support nor a half tie. Equation (36.7) does not remove its tails; it reconstructs the exact unmasked \(D_{\xi;U,V,S}\). Now take the same symmetric physical net used in the accepted endpoint and \(R_1\) theorems. Since (36.7) is an equality at every finite stage, no exchange of a limit with any of the sixteen terms is needed. The aggregate limit is:

- the lower and upper original-sector endpoint prefixes, with the product star and hard-top half-star appearing only after symmetric inversion;
- the physical \(R_1\) \(y\)-return, with the one-sided top half-star, height endpoint zero, and lower-minus-upper radial phase.

The exact \(H_j+1\) floors, actual profiles, \(\chi_4(q)\), scale sum, and
\[
 -\frac4\pi X^{1/4}\Re\{e(1/8)(\cdot)\}
\]
remain common. The normalized package is \(O_W(\log X)\) (the logarithm is only the accepted lower endpoint), hence physically
\(O_W(X^{1/4}\log X)\).

Finally, if \(\mathfrak V_{\rm fin}\) denotes the full finite vector package, define its exact global complement by
\[
 \mathfrak R_{\rm fin}:=\mathfrak V_{\rm fin}-\mathfrak M_{\rm fin},
\qquad
 \mathfrak A_{\beta,\rm fin}
 :=\mathsf X_{uv}[\Theta_\beta\mathfrak R_{\rm fin}].                    \tag{36.10}
\]
This is the lawful endpoint-free beta axial vector at finite height. The physical module is kept outside (36.10); Round 35 separately annihilates its beta radial-side image. Equation (36.10) defines no limiting symbol and asserts no bound for the remainder.

## 4. First doubtful or unproved step

The stronger termwise commutator remains false as a proved statement:
\[
 \sum_\kappa\lim_{\rm phys}\mathsf X_{uv}
 [\Theta_\kappa\mathfrak M_{\rm fin}]
 \quad\text{is not licensed}.                                           \tag{36.11}
\]
At finite top Mellin height, the one-sided profile has noncompact Perron tails, and neither the upper-endpoint sampled-BV lemma nor the \(R_1\) fixed-\(y\) BV lemma applies to an isolated face, connector, axis, or mask share. Thus one must sum all masks and all sixteen strata **before** the physical limit.

Likewise, shifting the displayed \(R^{\rm ar}[R_1]\) alone through its artificial pole is invalid. Formula (36.4) must be represented by the common pre-cancellation meromorphic package, or avoided entirely by the boundary-first definition (36.10). The permitted accepted results do not prove a beta-only physical module transfer, and this report does not claim one.

There is an analogous representation warning for (36.9). After the change
\(r=w-p(v)\), its path is
\[
 \Re r=c-\frac34-\frac{\Re v}{2},\qquad
 \Im r\in[-S-\nu/2,S-\nu/2].
\]
Naively holding this path fixed while moving \(v\), or differentiating
only the displayed Perron kernel, loses its moving-path faces. The aggregate
theorem is certified only from the fixed-\(w\) meromorphic antecedent. With
that antecedent, the ordinary faces are already in (36.8), and no additional
finite-Perron face survives.

## 5. Control tests and outcomes

- **Three-mask sixteen-stratum cancellation:** pass, pointwise on faces, axes, connector axes, mixed areas, collisions, and the corner by (36.6).
- **Finite representative and limit order:** pass only for the common fixed-\(w\) package (36.4) and aggregate-before-limit order; termwise limits or a frozen off-centred \(r\)-path fail the audit.
- **Endpoint/arithmetic recombination:** pass under (36.3) with artificial poles paired and collision residues combined once.
- **Finite Perron versus physical star:** pass. Perron tails survive at finite \(S\); no star is inserted until the licensed symmetric physical inversion.
- **Collision and corner ownership:** pass under the sequential one-corner/common-residue convention. Restricting the partition before summing still gives one.
- **Profiles, character, normalization:** pass. No profile is replaced, no floor is smoothed, \(\chi_4\) stays on \(q\), and the external \(X^{1/4}\) factor is restored exactly.
- **No terminal-symbol overreach:** pass. Equation (36.10) is a finite algebraic definition, not a limit or estimate.

## 6. Dependencies and exact artifacts used

Used only protocol.md, state/proof_obligations.yml, state/active_campaign.yml, the permitted Round-22, Round-23, Round-24 syntheses, Round-33 and Round-34 hostile audits, and Round-35 synthesis. No Round-36 claimant report, numerical experiment, or external source was used.

## 7. Recommended state effect

**Promote the aggregate physical-module routing theorem (36.1), (36.7), and the boundary-first finite complement (36.10); close the physical-module commutator only in this global scope.** Explicitly reject individual masked/stratum physical limits, sharp finite Perron support, and transfer of isolated \(R_1\) across its artificial pole. With the Round-35 radial-side result, the endpoint/arithmetic boundary modules may be kept wholly outside the beta axial transfer. Retain the existence and estimate of the physical endpoint-free axial remainder, the axial-subtracted terminal symbol, and the beta transition bound as open.
