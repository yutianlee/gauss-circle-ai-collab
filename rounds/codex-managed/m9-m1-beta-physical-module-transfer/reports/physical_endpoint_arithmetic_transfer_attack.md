# Round 36 discovery report: global routing of the physical boundary module

## 1. Result

**Exact aggregate-routing theorem.**  The complete two-axis transfer does
not have to be commuted term by term through the physical endpoint and
arithmetic limits.  At every fixed finite stage, use the original \(w\)
coordinate, apply the transfer to all three hierarchical mask shares, and
sum the shares before taking any limit.  The masks and all their first and
mixed derivatives then recombine pointwise to

\[
 \sum_{\kappa\in\{\beta,\alpha,o\}}\Theta_\kappa=1,
 \qquad
 \sum_\kappa\partial_\mu\Theta_\kappa
 =\sum_\kappa\partial_\nu\Theta_\kappa
 =\sum_\kappa\partial_\mu\partial_\nu\Theta_\kappa=0.       \tag{36.1}
\]

Consequently every first-derivative connector, connector-axis image, and
mixed connector cancels in the three-share sum.  The ordinary faces,
axes, and joint corner do **not** vanish.  They reassemble, by the exact
finite product Stokes identity, into the original unmasked positive-line
finite module:

\[
 \boxed{
 \sum_\kappa {\mathsf X}_{uv}[\Theta_\kappa {\cal M}_{\rm fin}]
 ={\mathsf X}_{uv}[{\cal M}_{\rm fin}]
 ={\mathsf R}_u{\mathsf R}_v[{\cal M}_{\rm fin}]. }
                                                               \tag{36.2}
\]

Here the common finite module has either of the exactly equal forms

\[
\begin{aligned}
 {\cal M}_{\rm fin}
 &:=\sum_{\xi\in\{1,N_X\}}
       (T_\xi+S_\xi+P_\xi)+{\mathfrak R}^{\rm ar}[G]\\
 &=\sum_{\xi\in\{1,N_X\}}D_\xi
       +{\mathfrak R}^{\rm ar}[R_1].                         \tag{36.3}
\end{aligned}
\]

Thus one first performs the exact finite recombination (36.1)--(36.3),
and only then takes the already licensed symmetric physical limits of the
unmasked \(D_1,D_{N_X}\), and recombined \(R_1\) terms.  No uniform
finite-height estimate for an individual masked connector or off-centred
Perron tail is needed.  The physical module is target-safe:

\[
 -\frac4\pi X^{1/4}\Re\{e(1/8){\cal M}_{\rm phys}\}
 =O_W(X^{1/4}\log X).                                       \tag{36.4}
\]

This proves the endpoint/arithmetic module-transfer interface.  It does
not estimate the remaining endpoint-free axial vector or the terminal
beta symbol.

## 2. Exact statement and hypotheses

Fix finite \(U,V,S\), the accepted \(u,v,w\) rectangles, and contours with
no pole on their boundaries.  All transfers below are performed at fixed
\(w\), not at fixed \(r=w-\gamma_v\), where

\[
 z=u+v,\qquad \gamma_v=\frac34+\frac v2.                    \tag{36.5}
\]

The actual outside multiplier is retained throughout:

\[
 {\cal A}_j(u,v)=\widehat W_j(u)\widehat\phi(v)
 \left(\frac{D_j}{2\sqrt X}\right)^u(H_j+1)^v,
 \qquad H_j=\lfloor D_jX^{-1/4}\rfloor .                   \tag{36.6}
\]

For \(\xi\in\{1,N_X\}\), put
\(\varepsilon_{N_X}=1\), \(\varepsilon_1=-1\), and define the finite
right-line endpoint representative

\[
\begin{aligned}
 D_\xi^{\rm fin}:={}&
 \sum_j\frac1{(2\pi i)^2}\int_{\Gamma_{a,U}}
 \int_{\Gamma_{b,V}}{\cal A}_j(u,v)
 \varepsilon_\xi e(\sqrt{X\xi})\xi^{-\gamma_v}\\
 &\quad\times\sum_{h,q\ge1}\chi_4(q)
 \left(\frac qh\right)^{z/2}
 {\mathscr P}_{c,S,\gamma_v}\!\left(\frac\xi{hq}\right),dv,du,
                                                               \tag{36.7}
\end{aligned}
\]

where

\[
 {\mathscr P}_{c,S,\gamma}(A)
 =\frac1{2\pi i}\int_{c-iS}^{c+iS}\frac{A^w}{w-\gamma}\,dw. \tag{36.8}
\]

At this stage (36.8) is an off-centred finite Perron kernel; it has no
sharp support and no half-star.  The finite recombined arithmetic
representative is

\[
 {\mathfrak R}^{\rm ar}_{\rm fin}[R_1]
 =\sum_j\frac1{(2\pi i)^2}\int\!\!\int
 {\cal A}_j(u,v)R_{1,v}(1-z/2)L(1-z,\chi_4)\,dv\,du.          \tag{36.9}
\]

Equations (36.7) and (36.9) define the second line of (36.3).  The first
line is its common pre-collapse antecedent.  At the same finite stage the
accepted endpoint Cauchy identities are

\[
 T_\xi+S_\xi+P_\xi=D_\xi-A_\xi,
 \qquad
 {\mathfrak R}^{\rm ar}[G]-\sum_\xi A_\xi
 ={\mathfrak R}^{\rm ar}[R_1].                              \tag{36.10}
\]

Use the hierarchical partition

\[
 \Theta_\beta=\psi(\beta),\quad
 \Theta_\alpha=(1-\psi(\beta))\psi(\alpha),\quad
 \Theta_o=(1-\psi(\beta))(1-\psi(\alpha)),                 \tag{36.11}
\]

with \(\beta=\Im(s-(u+v)/2)\) and
\(\alpha=\Im(s+(u+v)/2)\).  Every residue collision is defined by one
combined iterated or derivative coefficient of the common meromorphic
integrand.  The physical limit is taken only in the already accepted
symmetric order for the endpoint prefixes and (36.9).

Under these hypotheses, (36.2)--(36.4) hold.

## 3. Proof or derivation

### 3.1 Cancellation on all transfer strata

Equation (36.11) is a pointwise smooth partition of unity, so (36.1)
follows by differentiation.  Restriction to a horizontal face, to
\(u=0\), to \(v=0\), or to \(u=v=0\) commutes with this finite sum.
Thus (36.1) remains true on every boundary, connector-axis, and corner
trace.

Apply the accepted product transfer formula to a common finite density
\(Q\):

\[
\begin{aligned}
{\mathsf X}_{uv}[\Theta Q]={}&F_uF_v[\Theta Q]
 +F_uP_v[\Theta Q]+P_uF_v[\Theta Q]+P_uP_v[\Theta Q]\\
&+\tfrac12F_uA_v[(\partial^\sharp_v\Theta)Q]
 +\tfrac12P_uA_v[(\partial^\sharp_v\Theta)Q]\\
&+\tfrac12A_uF_v[(\partial^\sharp_u\Theta)Q]
 +\tfrac12A_uP_v[(\partial^\sharp_u\Theta)Q]
 +A_uA_v[(\partial^\sharp_{uv}\Theta)Q],                  \tag{36.12}
\end{aligned}
\]

where for the beta share the displayed normalized derivatives are
\(\psi'\), \(\psi'\), and \(\psi''/4\), with the accepted positive
connector signs.  Summing (36.12) over (36.11), all terms containing a
first or mixed mask derivative vanish by (36.1).  The remaining terms are

\[
 F_uF_v[Q]+F_uP_v[Q]+P_uF_v[Q]+P_uP_v[Q].                  \tag{36.13}
\]

These are the unmasked ordinary faces, axis residues, and joint corner.
They are not zero.  Applying the finite one-axis Cauchy identities in
either order shows that (36.13) equals the original right positive-line
product \({\mathsf R}_u{\mathsf R}_v[Q]\).  This proves (36.2).  It also
shows why no estimate of an ordinary transferred horizontal image is
missing: it is retained until it has reassembled the positive-line
antecedent.

### 3.2 Endpoint and arithmetic recombination

Sum the first identity in (36.10) over the two endpoints and add
\({\mathfrak R}^{\rm ar}[G]\).  The arithmetic shares then combine by
the second identity in (36.10), giving exactly (36.3).  This is an
identity at finite \(U,V,S\); no radial side, Perron tail, or artificial
residue has been discarded in deriving it.

The artificial residues of \(E_1\) and \(R_1\) cancel because
\(G=E_1+R_1\) as a meromorphic identity and the same transfer and mask
share act on all three terms.  If an artificial divisor meets an axial or
arithmetic divisor, coefficient extraction is applied only after this
common identity.  Therefore the collision contributes once and cannot
create a remainder.  The same argument applies to the joint
\(u=v=0\) corner.

The fixed-\(w\) qualification is essential.  Replacing \(w\) by
\(r=w-\gamma_v\) and then shifting \(v\) at fixed \(r\) moves the
physical \(w\)-path.  That sheared representation has additional moving
boundary traces and is not the common antecedent used in (36.2).  Holding
the original \(w\) rectangle fixed avoids this false interchange.

### 3.3 Passage to the physical module

For every finite truncation, the complete three-share transferred module
equals the unmasked positive-line object in (36.3).  Hence the correct
order is

\[
 \lim_{\rm phys}\left\{
   \sum_\kappa {\mathsf X}_{uv}[\Theta_\kappa{\cal M}_{\rm fin}]
 \right\}
 =\lim_{\rm phys}{\cal M}_{\rm fin}
 ={\cal M}_{\rm phys}.                                      \tag{36.14}
\]

This is not an assertion that the limit passes through each summand.
Rather, the braces are simplified by a finite identity before the limit.
The accepted symmetric Perron inversion then supplies the lower endpoint
equality half-weight, the upper product star (hq=N_X), and the top
spatial half-star.  The height endpoint stays unstarred because
\(\phi(1)=0\).  It gives

\[
 D_1^{\rm phys}=O_W(\log X),\qquad
 D_{N_X}^{\rm phys}=O_W(1),\qquad
 {\mathfrak R}^{\rm ar}_{\rm phys}[R_1]=O_W(1).              \tag{36.15}
\]

The last term has the accepted physical (y)-return and period-four
\(\chi_4\) Abel cancellation; the upper endpoint uses the analogous
fixed-((j,h)) character-Abel bound.  Restoring the external factor once
gives (36.4).  All (D_j,H_j+1,W_j,\phi,\chi_4), hard-top, and product
conventions remain inside the common object throughout.

### 3.4 Endpoint-free complement

Let \({\cal V}_{\rm pre}^{\rm fin}\) be the complete finite axial vector
from the accepted pre-limit ledger, including all faces, connectors,
axes, collisions, and the one corner.  Its unique globally endpoint-free
finite representative is

\[
 \boxed{
 {\cal V}_{\rm ef}^{\rm fin}
 := {\cal V}_{\rm pre}^{\rm fin}
 -\sum_\kappa{\mathsf X}_{uv}[\Theta_\kappa{\cal M}_{\rm fin}]
 = {\cal V}_{\rm pre}^{\rm fin}-{\cal M}_{\rm fin}. }      \tag{36.16}
\]

In the post-module physical ledger, the second term is replaced by the
single accepted \({\cal M}_{\rm phys}\) from (36.14), with the external
normalization applied once.  Equation (36.16) defines the complement; it
does not assert a bound or an outside-height limit for that complement.

## 4. First doubtful or unproved step

There is no remaining limit interchange inside the aggregate physical
module: (36.14) routes around it by an exact finite identity.  What is
not proved is a physical or target-size estimate for
\({\cal V}_{\rm ef}^{\rm fin}\), nor convergence of all of its remaining
outside faces and axial terms.  In particular, this report does not turn
(36.16) into the axial-subtracted terminal symbol and does not prove the
beta transition estimate.

The theorem also does not license either of the stronger statements

\[
 \lim_{\rm phys}{\mathsf X}_{uv}[\Theta_\kappa{\cal M}_{\rm fin}]
 ={\mathsf X}_{uv}[\lim_{\rm phys}\Theta_\kappa{\cal M}_{\rm fin}]
\]

for an individual share, or a fixed-\(r=w-\gamma_v\) displacement.  The
finite off-centred kernels in (36.8) have tails, so these assertions would
still require a new uniform theorem.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| three-mask sixteen-stratum cancellation | Pass.  The partition sums to one on every restriction; first and mixed derivative sums are zero.  Connector, connector-axis, and mixed strata cancel. |
| ordinary face/axis/corner ledger | Pass.  These strata survive and reassemble the full original positive-line module; they are never declared zero. |
| finite representative and order | Pass with the fixed-\(w\) antecedent (36.3), (36.7)--(36.9).  Recombine first, take the licensed symmetric physical limit second. |
| endpoint/arithmetic recombination | Pass by (36.10); the two arithmetic endpoint shares return exactly the single recombined \(R_1\) residue. |
| finite Perron versus stars | Pass.  No star is attached to (36.8); all half-values appear only after symmetric physical inversion. |
| collision and corner ownership | Pass.  Common combined coefficients are extracted once; full-axis inclusion--exclusion leaves one joint corner. |
| actual profiles, character, normalization | Pass.  All profiles, floors, \(\chi_4\), hard top, and stars remain attached; \(-4X^{1/4}\Re(e(1/8)\cdot)/\pi\) is applied once after recombination. |
| unsigned/adversarial check | Pass as a scope check.  The endpoint and \(R_1\) bounds use period-four \(\chi_4\) Abel cancellation; the unsigned analogue is not inferred. |
| no terminal-symbol overreach | Pass.  Only the boundary module and the definition (36.16) are obtained; no estimate of the remaining vector is claimed. |

No numerical experiment or external result was used.

## 6. Dependencies and exact artifacts used

The derivation used only the selected context:

1. `protocol.md`;
2. `state/proof_obligations.yml`, graph SHA-256
   `9bf9658abcbc762eba2a829c4b8ff982e2fd4a563b593bdec2373c5b1645b411`;
3. `state/active_campaign.yml`;
4. `rounds/codex-managed/m9-m1-endpoint-boundary-cauchy/reports/blind_M1_boundary_cauchy.md`;
5. `rounds/codex-managed/m9-m1-upper-endpoint-character-abel/reports/blind_upper_endpoint_abel.md`;
6. `rounds/codex-managed/m9-m1-r1-arithmetic-residue/reports/blind_r1_residue_return.md`;
7. `rounds/codex-managed/m9-m1-beta-mask-endpoint-axial-compatibility/reports/mask_endpoint_axial_attack.md`;
8. `rounds/codex-managed/m9-m1-beta-complete-axial-connector-ledger/reports/actual_axial_connector_ledger_attack.md`;
9. `rounds/codex-managed/m9-m1-beta-axial-side-exhaustion/synthesis.md`;
10. the Round-36 task brief.

The imported accepted facts are the finite endpoint identity, the three
hierarchical masks, the complete finite product transfer, common collision
ownership, the compact-beta radial-side result, and the physical endpoint
and \(R_1\) formulas.  Equations (36.2), (36.14), and (36.16), together
with the fixed-\(w\) representation caveat, are the new conclusions.

## 7. Recommended state effect

**Promote after the required independent audits** the scoped aggregate
physical-module transfer theorem (36.2), (36.14): the full three-mask
transfer of the common finite endpoint/arithmetic module is simplified
before the physical limit and equals the accepted unmasked physical
module.  Promote the exact endpoint-free complement definition (36.16)
and record fixed \(w\) as part of its hypotheses.

Close `M9-M1-beta-axial-transfer-physical-module-commutation` and, together
with Round 35, the boundary-module limit-compatibility interface.  Reject
termwise masked-connector convergence, fixed-(r) freezing, early stars,
or deletion of the surviving ordinary faces.  Retain the endpoint-free
axial-vector estimate, beta terminal-symbol estimate, complete transition,
M9-M1, M9, and the Gauss target as open.
