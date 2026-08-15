# Round 34 discovery report: actual two-axis axial connector ledger

## 1. Result

The complete **pre-limit finite** two-axis ledger is exact and independent
of the order of the \(u\)- and \(v\)-shifts. For every separately
meromorphic stratum \(Q(u,v)\) of the finite reflected vector package,
multiplied by
\[
 \Theta_\beta=\psi(\beta),\qquad
 \beta=t-\frac{\mu+\nu}{2},
 \quad u=a+i\mu,\quad v=b+i\nu,
\tag{34.1}
\]
the two sequential Cauchy--Green operations contain:

1. all pure \(u\)- and \(v\)-horizontal faces;
2. each axis residue with its filtered mask;
3. the two one-axis area connectors;
4. the shift of every first-axis horizontal and residue;
5. connector boundary faces and connector-axis residues;
6. the mixed density \(+\psi''(\beta)/4\); and
7. one joint \(u=v=0\) corner.

With one fixed full-axis inclusion--exclusion convention, the expansions
\({\mathsf X}_u{\mathsf X}_v[\Theta_\beta Q]\) and
\({\mathsf X}_v{\mathsf X}_u[\Theta_\beta Q]\) agree term by term after
interchanging \(u\) and \(v\). This applies linearly to the actual finite
terminal vector integrand, every renormalized radial-side stratum, and the
finite arithmetic stratum. The artificial \(E_1/R_1\) pole cancels under
the same operation, and a collision is represented by the corresponding
combined iterated/derivative residue.

The stronger requested **post-module endpoint-free identity is not
defined by the accepted artifacts**. The unmasked endpoint and
recombined \(R_1\) arithmetic theorems begin only after accepted physical
profile limits, while the finite two-axis shift creates horizontal faces,
area connectors, and connector-axis residues before those limits. The
accepted nested theorem removes renormalized radial sides only after a
specific joint exhaustion. No accepted interchange theorem shows that an
outside \(u\)- or \(v\)-shift commutes with either operation.

Accordingly, the first exact actual obstruction is the commutator
\[
 \boxed{
 {\cal C}_{\rm lim}^{u,v}
 =
 {\mathsf X}_u{\mathsf X}_v\,{\mathsf P}_{\rm phys}
 -
 {\mathsf P}_{\rm phys}\,{\mathsf X}_u{\mathsf X}_v ,
 }
\tag{34.2}
\]
together with the analogous commutator for nested radial-side exhaustion.
Here \({\mathsf P}_{\rm phys}\) is the accepted joint endpoint/arithmetic
physical-limit and module-removal operation. The selected context neither
defines (34.2) as zero nor bounds it. Thus the abstract finite ledger is
proved, but the claimed actual endpoint-free axial vector cannot yet be
promoted.

## 2. Exact statement and hypotheses

### 2.1 Actual finite strata before licensed limits

For \(z=u+v\), \(m=hq\), and
\[
 {\cal A}_j(u,v)
 =\widehat W_j(u)\widehat\phi(v)
 \left(\frac{D_j}{2\sqrt X}\right)^u(H_j+1)^v,
\tag{34.3}
\]
define the actual terminal density
\[
\begin{aligned}
 Q_{\rm T}(u,v,s;h,q,m)
 ={}&{\bf1}_{hq=m}\chi_4(q)\sum_j
 {\cal A}_j(u,v)\left(\frac hq\right)^{z/2}\\
 &\times G_v(1-s)K_z(1-s)m^{-s}.
\end{aligned}
\tag{34.4}
\]
The exact gamma quotient is
\[
 K_z(1-s)=2^{2s+z-1}\pi^{1-2s}
 \frac{\Gamma((s-z/2)/2)\Gamma((1+s+z/2)/2)}
 {\Gamma((1-s+z/2)/2)\Gamma((2-s-z/2)/2)}.
\tag{34.5}
\]
The two radial-side densities are the same complete finite integrand on
the upper path \(\lambda+iS\to c+iS\) and lower path
\(c-iS\to\lambda-iS\). Their common left-to-right ledger is upper minus
lower. After endpoint subtraction, replace \(G_v\) by the complete
renormalized \(R_{M,v}\), but do not yet send \(S\) to infinity.

The finite arithmetic density is
\[
 Q_{\rm ar}(u,v)
 =\sum_j{\cal A}_j(u,v)
 G_v(1-z/2)L(1-z,\chi_4).
\tag{34.6}
\]
If the accepted global endpoint collapse has been performed only as a
finite identity, all returned \(D_\xi,A_\xi,P_\xi\) strata remain in this
pre-limit package. They may not yet be replaced by their physical-limit
bounds.

Let \({\mathfrak S}_{\rm fin}\) denote the direct sum of (34.4), the two
renormalized radial-side densities, (34.6), and every still-retained
finite endpoint/artificial/arithmetic stratum. The following theorem is
stratumwise on \({\mathfrak S}_{\rm fin}\).

### 2.2 One-axis transfer

For a separately meromorphic \(Q(u,v)\) on finite rectangles, assume no
pole lies on a boundary. Let \(V_v^+\) and \(V_v^-\) be the right and left
upward \(v\)-verticals, and let \(H_{v,+},H_{v,-}\) be top and bottom
horizontals in left-to-right orientation. Define
\[
 {\cal A}_v[Q]
 =-\iint_{R_v}\partial_\nu\Theta_\beta\,Q\,dA_v
 =\frac12\iint_{R_v}\psi'(\beta)Q\,dA_v,
\tag{34.7}
\]
and similarly
\[
 {\cal A}_u[Q]
 =\frac12\iint_{R_u}\psi'(\beta)Q\,dA_u.
\tag{34.8}
\]
Positive orientation gives
\[
\boxed{
 V_v^+[\Theta_\beta Q]
 =V_v^-[\Theta_\beta Q]
 +H_{v,+}[\Theta_\beta Q]-H_{v,-}[\Theta_\beta Q]
 +2\pi i\,R_v[\Theta_\beta Q]
 +{\cal A}_v[Q],
}
\tag{34.9}
\]
and the analogous identity with \(u\) and \(v\) interchanged.

At the axes the weights are
\[
 \Theta_\beta|_{v=0}=\psi(t-\mu/2),\quad
 \Theta_\beta|_{u=0}=\psi(t-\nu/2),\quad
 \Theta_\beta|_{u=v=0}=\psi(t).
\tag{34.10}
\]

### 2.3 Full two-axis identity

Use the full-axis convention
\[
 R_u^{\rm full}+R_v^{\rm full}-R_{uv},
\tag{34.11}
\]
where the two full axis residues each contain the joint corner and
\(R_{uv}\) is subtracted once. Let \({\cal B}_u,{\cal B}_v\) denote the
oriented horizontal-difference operators, and let
\({\cal R}_u=2\pi iR_u\), \({\cal R}_v=2\pi iR_v\).
Then the complete transfer is
\[
\begin{aligned}
 {\mathsf X}_{uv}[\Theta_\beta Q]
 ={}&
 \Theta_\beta Q
 +({\cal B}_u+{\cal R}_u+{\cal A}_u)[Q]
 +({\cal B}_v+{\cal R}_v+{\cal A}_v)[Q]\\
 &+{\cal B}_u{\cal B}_v[Q]
 +{\cal B}_u{\cal R}_v[Q]+{\cal R}_u{\cal B}_v[Q]
 +{\cal B}_u{\cal A}_v[Q]+{\cal A}_u{\cal B}_v[Q]\\
 &+{\cal R}_u{\cal A}_v[Q]+{\cal A}_u{\cal R}_v[Q]
 +{\cal A}_{uv}[Q]
 -{\cal R}_{uv}[Q],
\end{aligned}
\tag{34.12}
\]
where every composition retains the induced finite faces and
\[
 {\cal A}_{uv}[Q]
 =\frac14\iiiint_{R_u\times R_v}
 \psi''(\beta)Q\,dA_u\,dA_v.
\tag{34.13}
\]
In (34.12), \({\cal R}_u{\cal A}_v\) and
\({\cal A}_u{\cal R}_v\) are the connector-axis residues; the two
\({\cal B}{\cal A}\) terms contain the connector boundary faces. Formula
(34.12) is schematic only in suppressing the unchanged outer \(s,j,h,q,m\)
integrations; no stratum is suppressed.

The theorem is
\[
 \boxed{
 {\mathsf X}_u{\mathsf X}_v[\Theta_\beta Q]
 =
 {\mathsf X}_v{\mathsf X}_u[\Theta_\beta Q]
 =
 {\mathsf X}_{uv}[\Theta_\beta Q]
 }
\tag{34.14}
\]
for every \(Q\in{\mathfrak S}_{\rm fin}\), subject to the common collision
convention below.

## 3. Proof or derivation

### 3.1 One-axis signs and actual-factor insertion

On a positively oriented \(v\)-rectangle the boundary is
\[
 V_v^+-V_v^- -H_{v,+}+H_{v,-}.
\]
Since
\[
 2i\bar\partial_v\Theta_\beta
 =-\partial_\nu\Theta_\beta
 =\frac12\psi'(\beta),
\tag{34.15}
\]
Cauchy--Green gives (34.9). The same computation at fixed \(s,v\) gives
(34.8) and its \(u\)-version. Every factor in (34.3)--(34.6) is merely
carried by \(Q\); hence the formula applies without altering the
\(\chi_4(q)\), floor \(H_j+1\), radial star, top half-star, or endpoint
convention.

### 3.2 Expand \(v\) then \(u\)

First use (34.9). The \(u\)-shift must then be applied to four outputs:
the new \(v\)-vertical, the pair \(H_{v,+}-H_{v,-}\), the filtered
\(v=0\) residue, and \({\cal A}_v\). These give, respectively:

1. the pure \(u\) faces, \(u=0\) residue, and \({\cal A}_u\);
2. \({\cal B}_u{\cal B}_v\), \({\cal R}_u{\cal B}_v\), and
   \({\cal A}_u{\cal B}_v\);
3. \({\cal B}_u{\cal R}_v\), the joint corner, and the derivative of the
   filtered residue weight;
4. \({\cal B}_u{\cal A}_v\), \({\cal R}_u{\cal A}_v\), and the derivative
   of the first connector density.

Because
\[
 \partial_\mu\partial_\nu\Theta_\beta
 =\frac14\psi''(\beta),
\tag{34.16}
\]
the last derivative is precisely (34.13), with positive sign. The
derivative of the filtered \(v=0\) residue is the boundary trace of the
same mixed Stokes stratum, not an additional corner.

### 3.3 Expand \(u\) then \(v\)

Starting with the \(u\)-identity gives the same four classes with
\(u,v\) interchanged. Mixed partials commute, so (34.16) is unchanged.
The product faces satisfy
\({\cal B}_u{\cal B}_v={\cal B}_v{\cal B}_u\); residue/face and
connector/face compositions match by Fubini on finite rectangles. For
separate simple axes the iterated residues commute. Thus both orders give
the terms of (34.12).

Under convention (34.11), each full axis contains the corner and the
subtraction \(-{\cal R}_{uv}\) leaves it once. Equivalently one may use
corner-deleted axes and add \(+{\cal R}_{uv}\). No line of the proof mixes
the two conventions. This proves (34.14).

### 3.4 Artificial poles and collisions

Apply the full operator (34.12) identically to \(G,E_1,R_1\). Linearity
and \(G=E_1+R_1\) give
\[
 {\mathsf X}_{uv}[\Theta_\beta G]
 -{\mathsf X}_{uv}[\Theta_\beta E_1]
 -{\mathsf X}_{uv}[\Theta_\beta R_1]=0.
\tag{34.17}
\]
Therefore artificial rho residues cancel on terminal, side, face,
connector, connector-axis, and corner strata. If an artificial pole
coincides with \(u=0\), \(v=0\), or the arithmetic pole, do not add
separate simple residues. Excise one small product neighborhood and use
the corresponding iterated or derivative coefficient of the combined
meromorphic integrand. Equation (34.17) remains valid because it precedes
the coefficient extraction.

### 3.5 Why the post-module actual claim does not follow

The endpoint theorems and the \(R_1\) arithmetic bound are statements
after symmetric physical inversion. Their finite antecedents contain
off-centred Perron tails and cannot invoke the compact-support
profile/character-BV argument. Conversely, (34.12) introduces new finite
\(u\)- and \(v\)-horizontals and area connectors. The accepted artifacts
contain no dominated-convergence, uniform-BV, or vector maximal lemma
passing these strata through the physical limit.

Similarly, the renormalized radial side is removed only for an accepted
nested relation \(S=S(X,U,V)\) after sufficiently many endpoint
subtractions. The new axis faces and connector-axis residues alter the
height boundary data. No cited theorem says their side limit is zero or
that the two-axis transfer commutes with this exhaustion. Hence deleting
the endpoint/arithmetic/side strata first and then writing (34.12) is not
an identity licensed by the selected context. This proves the scoped
no-go (34.2).

## 4. First doubtful or unproved step

There is no doubtful step in the finite product-Cauchy--Green identity.
The first undefined actual coefficient is the physical-limit commutator
\[
\begin{aligned}
 {\cal C}_{\rm lim}^{u,v}
 ={}&
 \lim_{\rm phys}
 {\mathsf X}_{uv}\!\left[
 {\mathfrak S}_{\rm end}+{\mathfrak S}_{\rm ar}\right]\\
 &-
 {\mathsf X}_{uv}\!\left[
 \lim_{\rm phys}
 ({\mathfrak S}_{\rm end}+{\mathfrak S}_{\rm ar})\right],
\end{aligned}
\tag{34.18}
\]
where the second line routes the physical limit to the already-proved
unmasked modules. A matching side commutator is
\[
 {\cal C}_{\rm side}^{u,v}
 =
 \lim_{\substack{U,V,S\to\infty\\S=S(X,U,V)}}
 {\mathsf X}_{uv}{\mathfrak S}_{\rm rad}^{(M)}
 -
 {\mathsf X}_{uv}
 \lim_{\substack{U,V,S\to\infty\\S=S(X,U,V)}}
 {\mathfrak S}_{\rm rad}^{(M)}.
\tag{34.19}
\]
The accepted graph proves neither commutator is zero. The new terms one
must control are exactly the physical limits of the connector boundary
faces, connector-axis residues, mixed \(\psi''/4\) density, and filtered
corner on the endpoint/arithmetic/side strata.

Until (34.18)--(34.19) are defined and shown to vanish (or explicitly
retained), there is no unique endpoint-free connector-completed actual
axial vector to subtract from the terminal kernel.

## 5. Required control tests and outcomes

### One-axis orientation and area sign

**Pass.** Right minus left and upper minus lower give (34.9). Since
\(\partial_\nu\Theta_\beta=-\psi'/2\), the connector has
\(+\frac12\iint\psi'Q\). The \(u\)-connector has the same sign.

### Two-axis mixed derivative sign

**Pass.**
\(\partial_\mu\partial_\nu\Theta_\beta=\psi''/4\), so the mixed density
has positive sign. It is a product-area stratum, not a scalar corner.

### Connector-axis and boundary strata

**Pass in the finite ledger.** Formula (34.12) includes
\({\cal R}_u{\cal A}_v\), \({\cal A}_u{\cal R}_v\),
\({\cal B}_u{\cal A}_v\), and \({\cal A}_u{\cal B}_v\). Omitting any of
them destroys the order-reversal match.

### Corner inclusion--exclusion

**Pass.** The report consistently uses full axis residues and subtracts
one joint corner. The equivalent corner-deleted convention is not mixed
into the derivation.

### Shift-order commutation

**Pass before limits.** Finite Fubini, commuting mixed derivatives, and
commuting simple iterated residues prove (34.14). **Open after module
limits:** (34.18)--(34.19) are not controlled.

### Actual factors and residue ownership

**Pass for the pre-limit package.** Equations (34.3)--(34.6) retain the
actual vector gamma quotient, radial transform/remainder, character,
profiles, floors, and arithmetic factor. Identical transfer gives
artificial-pole cancellation (34.17). Collisions use one combined
coefficient. The supposed post-module endpoint-free coefficient is the
first undefined object.

### Endpoint-first normalization

**Pass as a ledger; no estimate claimed.** Global three-mask endpoint
collapse must precede beta localization. At finite height the returned
endpoint strata remain in \({\mathfrak S}_{\rm fin}\); they are not
silently replaced by physical-limit modules. The factor
\[
 -\frac4\pi X^{1/4}\Re\{e(1/8)(\cdots)\}
\tag{34.20}
\]
is restored exactly once after summing all vector strata. Endpoint IBP
coefficients retain full weight; the top half-star belongs only to the
licensed symmetric inversion.

### Stratum ledger

| Stratum | Mask/derivative | Orientation or coefficient | Status |
|---|---|---|---|
| terminal \(u,v\) face | \(\psi(\beta)\) | right minus left | finite exact |
| \(u\), \(v\) horizontals | \(\psi(\beta)\) | upper minus lower | finite exact |
| \(u=0\) axis | \(\psi(t-\nu/2)\) | \(2\pi i\) | filtered, retained |
| \(v=0\) axis | \(\psi(t-\mu/2)\) | \(2\pi i\) | filtered, retained |
| joint corner | \(\psi(t)\) | once by (34.11) | retained |
| \(u\), \(v\) connectors | \(\psi'(\beta)/2\) | positive area | retained |
| connector boundaries | \(\psi'(\beta)/2\) | induced upper-minus-lower | retained |
| connector-axis residues | \(\psi'(t-\cdot/2)/2\) | \(2\pi i\) times area trace | retained |
| mixed connector | \(\psi''(\beta)/4\) | positive product area | retained |
| artificial rho pole | common mask | cancels \(E_1/R_1\) | exact |
| physical endpoint/arithmetic limits | all actual profiles/stars | external (34.20) once | commutation open |
| renormalized side exhaustion | \(R_{M,v}\) | accepted nested order only | commutation open |

## 6. Dependencies and exact artifacts used

No numerical experiment, symbolic computation, web source, or external
theorem was used. The exact selected artifacts were:

1. protocol.md;
2. state/proof_obligations.yml, graph SHA-256
   09d4a1cb1664719cb8df255f371d496b5bbcb112f5611d63c742055bf495f193;
3. state/active_campaign.yml;
4. rounds/codex-managed/m9-m1-vector-hankel-kernel/reports/blind_finite_vector_kernel.md;
5. rounds/codex-managed/m9-m1-radial-endpoint-renormalization/synthesis.md;
6. rounds/codex-managed/m9-m1-r1-arithmetic-residue/synthesis.md;
7. rounds/codex-managed/m9-m1-beta-radial-pushforward-bv/reports/blind_hierarchical_recombined_identity.md;
8. rounds/codex-managed/m9-m1-beta-mask-endpoint-axial-compatibility/reports/mask_endpoint_axial_attack.md, including its scope correction;
9. rounds/codex-managed/m9-m1-beta-mask-endpoint-axial-compatibility/reviews/conductor_two_axis_connector_ledger.md;
10. rounds/codex-managed/m9-m1-beta-mask-endpoint-axial-compatibility/synthesis.md;
11. the Round-34 task brief.

The accepted inputs are the exact finite vector factors, finite radial
side orientation, endpoint subtraction and nested removal scope, physical
\(R_1\) residue scope, hierarchical split, finite one-axis connector
sign, three-mask endpoint recombination, and common-ownership rho
cancellation. The product ledger (34.12)--(34.14) and the limit
commutators (34.18)--(34.19) are derived here.

## 7. Recommended state effect

**Promote after independent audit, with finite pre-limit scope only:**

1. the actual finite stratum schema (34.3)--(34.6);
2. the complete product-Cauchy--Green ledger (34.12)--(34.13);
3. order independence (34.14);
4. artificial-pole cancellation and the combined collision convention
   under the full transfer.

**Retain open / revise:** the proposed actual endpoint-free axial vector
must be conditioned on a theorem proving or replacing the commutators
(34.18)--(34.19). Until then, the unique removable axial vector exists
only in the full pre-limit package, not after independently invoking the
physical endpoint/arithmetic and side-removal modules.

**Do not promote:** any target-size axial estimate, deletion of connector
faces, interchange of outside shifts with physical profile limits,
interchange with nested side exhaustion, or the axial-subtracted terminal
symbol. The complete beta transition and downstream theorem remain open.
