# Round 34 blind report: complete finite two-axis connector identity

Task: blind_two_axis_connector_identity  
Role: statement-only blind rederivation  
Allocation: 100% analytical/algebraic; no computation and no external theorem

## 1. Result: the two shift orders agree exactly

Let \(Q(u,v)\) be separately meromorphic on finite rectangular
\(u\)- and \(v\)-contours, and put
\[
 \Theta(\mu,\nu)=\psi(\beta),\qquad
 \beta=t-\frac{\mu+\nu}{2},
 \quad u=\sigma+i\mu,\quad v=\tau+i\nu.             \tag{34.1}
\]
Assume the only coordinate-axis poles are \(u=0\) and \(v=0\), with
collisions treated by their combined local residue. Then the complete
finite Cauchy--Green transfer of the right-right integral has sixteen
terms:
\[
\boxed{
\begin{aligned}
R_uR_v[\Theta Q]={}&
L_uL_v[\Theta Q]+L_uB_v[\Theta Q]
+B_uL_v[\Theta Q]+B_uB_v[\Theta Q]\\
&+L_uP_v[\Theta Q]+B_uP_v[\Theta Q]
+P_uL_v[\Theta Q]+P_uB_v[\Theta Q]\\
&+P_uP_v[\Theta Q]\\
&+\frac12L_uA_v[\psi'Q]
+\frac12B_uA_v[\psi'Q]
+\frac12P_uA_v[\psi'Q]\\
&+\frac12A_uL_v[\psi'Q]
+\frac12A_uB_v[\psi'Q]
+\frac12A_uP_v[\psi'Q]\\
&+\frac14A_uA_v[\psi''Q].
\end{aligned}}                                                   \tag{34.2}
\]
Here \(B_j=H_{j,+}-H_{j,-}\), with both horizontal faces
parametrized left-to-right; \(A_j\) is area integration over the finite
\(j\)-rectangle; and \(P_j\) includes the appropriate \(2\pi i\)
coordinate-axis residue. Formula (34.2) contains:

- all four nonresidual boundary products;
- both axis residues on every surviving boundary stratum;
- one joint corner \(P_uP_v\);
- both one-axis mask connectors and all their boundary faces;
- both connector-axis residues;
- the mixed positive density
  \(\frac14\psi''(\beta)\).

Expanding first in \(v\) and then in \(u\), or first in \(u\) and then in
\(v\), gives exactly (34.2). There is no sign mismatch. The equality uses
Fubini for finite strata and commutation of the two iterated residues.

Applied stratumwise after global endpoint collapse, (34.2) is the exact
axial ledger for the endpoint-free beta vector: terminal \(R_1\), every
still-retained renormalized radial side, and every residual arithmetic
stratum. It introduces no endpoint prefix. Artificial-pole cancellation,
profiles, floors, stars, \(\chi_4(q)\), and the external \(X^{1/4}\)
factor remain attached unchanged. No size estimate or height limit is
proved.

## 2. Exact statement and hypotheses

### 2.1 One-axis operators

For \(j=u,v\), let the right and left verticals be upward. Let
\[
 B_j=H_{j,+}-H_{j,-},\qquad F_j=L_j+B_j,             \tag{34.3}
\]
where \(H_{j,+}\) and \(H_{j,-}\) are both left-to-right. Let \(A_j\)
denote integration over the corresponding real-height rectangle with
positive Lebesgue area measure.

For a smooth scalar coefficient \(c(\mu,\nu)\) multiplying a meromorphic
density \(Q\), define
\[
 P_u[cQ]=2\pi i\,\operatorname {Res}_{u=0}(cQ),\qquad
 P_v[cQ]=2\pi i\,\operatorname {Res}_{v=0}(cQ).      \tag{34.4}
\]
All other crossed poles, if present, are entered as additional residue
operators and obey the same product formula. To keep the requested axial
ledger readable, (34.2) displays only \(u=0,v=0\).

The one-axis finite identity is
\[
 R_j[cQ]=F_j[cQ]+P_j[cQ]-A_j[(\partial_jc)Q],        \tag{34.5}
\]
where \(\partial_u c\) means \(\partial_\mu c\) and
\(\partial_v c\) means \(\partial_\nu c\). For (34.1),
\[
 \partial_\mu\Theta=\partial_\nu\Theta=-\frac12\psi'(\beta),
 \qquad
 \partial_\mu\partial_\nu\Theta=\frac14\psi''(\beta). \tag{34.6}
\]
Consequently each first connector has positive coefficient \(1/2\), and
the mixed connector has positive coefficient \(1/4\).

### 2.2 Residue and corner convention

Use the following iterated convention throughout. If the \(v\)-shift is
performed first, \(P_v[\Theta Q]\) is retained as a meromorphic function
of \(u\). The subsequent \(u\)-transfer splits it into
\[
 F_uP_v[\Theta Q]+P_uP_v[\Theta Q]
 +\frac12A_uP_v[\psi'Q].                         \tag{34.7}
\]
Thus the \(v\)-axis term initially contains its possible \(u=0\) pole,
but the final expansion assigns that pole only to \(P_uP_v\). The
reversed convention gives the same result. In particular,
\[
\begin{aligned}
P_v[\Theta Q]&=2\pi i\,
 \psi(t-\mu/2)\operatorname {Res}_{v=0}Q,\\
P_u[\Theta Q]&=2\pi i\,
 \psi(t-\nu/2)\operatorname {Res}_{u=0}Q,\\
P_uP_v[\Theta Q]&=(2\pi i)^2
 \psi(t)\operatorname {Res}_{u=0}\operatorname {Res}_{v=0}Q.
                                                               \tag{34.8}
\end{aligned}
\]
The last line is the joint corner and occurs exactly once.

The connector-axis residues are
\[
\begin{aligned}
\frac12P_uA_v[\psi'Q]
&=\frac12A_v\!\left[
 2\pi i\,\psi'(t-\nu/2)\operatorname {Res}_{u=0}Q\right],\\
\frac12A_uP_v[\psi'Q]
&=\frac12A_u\!\left[
 2\pi i\,\psi'(t-\mu/2)\operatorname {Res}_{v=0}Q\right].
                                                               \tag{34.9}
\end{aligned}
\]
They are distinct from the pure axis terms in (34.8).

### 2.3 Fully expanded v-then-u form

First transfer the \(v\)-line:
\[
 R_v[\Theta Q]
 =F_v[\Theta Q]+P_v[\Theta Q]
 +\frac12A_v[\psi'Q].                            \tag{34.10}
\]
Applying the \(u\)-transfer to all three terms gives
\[
\begin{aligned}
R_uR_v[\Theta Q]={}&
\underbrace{F_uF_v[\Theta Q]+P_uF_v[\Theta Q]
+\frac12A_uF_v[\psi'Q]}_{\text{\(u\)-shift of \(v\) boundaries}}\\
&+\underbrace{F_uP_v[\Theta Q]+P_uP_v[\Theta Q]
+\frac12A_uP_v[\psi'Q]}_{\text{\(u\)-shift of \(v=0\) axis}}\\
&+\underbrace{\frac12F_uA_v[\psi'Q]
+\frac12P_uA_v[\psi'Q]
+\frac14A_uA_v[\psi''Q]}_{\text{\(u\)-shift of \(v\) connector}}.
                                                               \tag{34.11}
\end{aligned}
\]
Expanding every \(F_j=L_j+B_j\) gives (34.2). In particular, the last
line of (34.11) contains both boundary faces of the \(v\)-area connector,
its \(u=0\) residue, and the mixed interior.

### 2.4 Fully expanded u-then-v form

Starting instead with
\[
 R_u[\Theta Q]
 =F_u[\Theta Q]+P_u[\Theta Q]
 +\frac12A_u[\psi'Q],                            \tag{34.12}
\]
the \(v\)-transfer gives
\[
\begin{aligned}
R_vR_u[\Theta Q]={}&
\underbrace{F_vF_u[\Theta Q]+P_vF_u[\Theta Q]
+\frac12A_vF_u[\psi'Q]}_{\text{\(v\)-shift of \(u\) boundaries}}\\
&+\underbrace{F_vP_u[\Theta Q]+P_vP_u[\Theta Q]
+\frac12A_vP_u[\psi'Q]}_{\text{\(v\)-shift of \(u=0\) axis}}\\
&+\underbrace{\frac12F_vA_u[\psi'Q]
+\frac12P_vA_u[\psi'Q]
+\frac14A_vA_u[\psi''Q]}_{\text{\(v\)-shift of \(u\) connector}}.
                                                               \tag{34.13}
\end{aligned}
\]
This is the independent reversed-order expansion.

## 3. Proof or derivation

For one variable, positive rectangle orientation and
Cauchy--Green give
\[
 R_j=L_j+H_{j,+}-H_{j,-}+P_j
 -A_j\partial_j.                                  \tag{34.14}
\]
This proves (34.5). Substituting the first identities in (34.6) proves
(34.10) and (34.12).

When the \(u\)-transfer acts on the \(v\)-connector,
\[
 \frac12A_v[\psi'(\beta)Q],
\]
its new area term is
\[
 -\frac12A_uA_v[
 \partial_\mu\{\psi'(\beta)\}Q]
 =-\frac12A_uA_v[-\tfrac12\psi''(\beta)Q]
 =\frac14A_uA_v[\psi''(\beta)Q].                  \tag{34.15}
\]
This proves the sign and coefficient of the mixed term in (34.11).
The same calculation with \(u,v\) reversed proves the last term of
(34.13).

On finite products, the following pairs commute:
\[
\begin{gathered}
F_uF_v=F_vF_u,\quad
F_uP_v=P_vF_u,\quad P_uF_v=F_vP_u,\quad
P_uP_v=P_vP_u,\\
F_uA_v=A_vF_u,\quad A_uF_v=F_vA_u,\quad
P_uA_v=A_vP_u,\quad A_uP_v=P_vA_u,\quad
A_uA_v=A_vA_u.                                      \tag{34.16}
\end{gathered}
\]
The boundary/area equalities are Fubini identities. The residue
equalities follow from the Laurent coefficient of \(u^{-1}v^{-1}\).
Matching (34.11) to (34.13) with (34.16) proves shift-order commutation
term by term.

For clarity, the final strata and their multiplicities are:
\[
\begin{array}{c|c|c}
\text{class}&\text{terms in (34.2)}&\text{multiplicity}\\ \hline
\text{boundary by boundary}
 &L_uL_v,L_uB_v,B_uL_v,B_uB_v&1\text{ each}\\
\text{\(v=0\) on \(u\) boundary}
 &L_uP_v,B_uP_v&1\text{ each}\\
\text{\(u=0\) on \(v\) boundary}
 &P_uL_v,P_uB_v&1\text{ each}\\
\text{joint corner}&P_uP_v&1\\
\text{\(v\)-connector on \(u\) boundary}
 &\frac12L_uA_v,\frac12B_uA_v&1\text{ each}\\
\text{\(u=0\) residue of \(v\)-connector}
 &\frac12P_uA_v&1\\
\text{\(u\)-connector on \(v\) boundary}
 &\frac12A_uL_v,\frac12A_uB_v&1\text{ each}\\
\text{\(v=0\) residue of \(u\)-connector}
 &\frac12A_uP_v&1\\
\text{mixed interior}&\frac14A_uA_v[\psi''Q]&1.
\end{array}                                                     \tag{34.17}
\]

### Endpoint-free vector application

After the global three-mask endpoint prefixes have recombined and been
routed to the accepted unmasked endpoint module, let
\[
 Q_{\rm ef}
 =Q_{\rm term}^{R_1}
 +\sum_{\pm}Q_{\rm side,\pm}^{\rm ren}
 +Q_{\rm ar}^{\rm res}                               \tag{34.18}
\]
denote the remaining finite endpoint-free vector density. Equation
(34.2) is applied separately to every stratum in (34.18), before any
side or height limit, and the results are summed.

On the residual arithmetic stratum \(A=0\), the pulled-back beta
coordinate is zero. Since \(\psi=1\) near zero, the mask is one and its
tangential connector derivatives vanish on that stratum. Its boundary and
axis-residue images remain. On terminal and radial-side strata the full
sixteen-term ledger is retained.

The relation \(G=E_1+R_1\) and artificial-pole cancellation are imposed
with the same mask before (34.2). Therefore the transfer is linear and
preserves the zero ownership defect. All factors
\[
 \widehat W_j(u),\quad\widehat\phi(v),\quad
 (D_j/(2\sqrt X))^u,\quad(H_j+1)^v,\quad
 \chi_4(q),\quad\text{floors and stars}
\]
remain inside \(Q\). The physical multiplier
\(-4X^{1/4}\Re\{e(1/8)(\cdot)\}/\pi\) is applied once after the vector
identity. None of these factors changes the finite algebra.

## 4. First doubtful or unproved step

The abstract finite identity has no unresolved sign or multiplicity.
Its first project-specific open step is analytic: no permitted statement
bounds the sum of the sixteen strata for \(Q_{\rm ef}\), removes the
renormalized radial sides, or takes the joint \(U,V,S\) limit.

The formula also assumes transverse separately meromorphic coordinate
poles. If an axial pole collides with an artificial, arithmetic, or other
moving pole, the colliding entries in (34.2) must be replaced by the
single local derivative residue before taking a limit. The permitted
statements prescribe this collision convention but do not enumerate every
actual collision parameter. This is a scope condition, not a mismatch in
(34.2).

## 5. Control tests and outcomes

### One-axis-orientation-and-area-sign

**Pass.** Each upper horizontal is positive and each lower
left-to-right horizontal is negative. Since
\(\partial_\mu\Theta=\partial_\nu\Theta=-\psi'/2\), the one-axis area
term \(-A_j\partial_j\Theta\) is \(+\frac12A_j\psi'\).

### Two-axis-mixed-derivative-sign

**Pass.** Equation (34.15) gives
\[
 (-1)(-1)\partial_\mu\partial_\nu\Theta
 =+\frac14\psi''(\beta).
\]
The mixed stratum has positive sign and occurs once.

### Connector-axis-and-boundary-strata

**Pass.** The last line of (34.11) and its reversed analogue include both
connector boundaries, one connector-axis residue, and the mixed interior.
Equation (34.17) lists all of them explicitly.

### Corner-inclusion-exclusion

**Pass.** The fixed iterated convention produces
\(P_uP_v[\Theta Q]\) exactly once, with weight \(\psi(t)\). It is not
also inserted as a separate independent corner.

### Shift-order-commutation

**Pass.** Every term of (34.11) has the unique reversed-order partner in
(34.13), as listed in (34.16). There is no first mismatch.

## 6. Dependencies and exact artifacts used

Only the following permitted artifacts were read or used:

1. protocol.md;
2. state/active_campaign.yml;
3. rounds/codex-managed/m9-m1-vector-hankel-kernel/synthesis.md;
4. rounds/codex-managed/m9-m1-beta-mask-endpoint-axial-compatibility/synthesis.md.

No proof graph, proof draft, excluded review, Round-34 claimant report,
computation, or web source was read or used.

## 7. Recommended state effect

- **Promote as exact finite algebra:** the one-axis operator (34.5), the
  complete sixteen-term identity (34.2), its mixed
  \(+\psi''/4\) coefficient, and the two independent sequential
  expansions (34.11), (34.13).
- **Promote the one-count ledger:** all horizontal faces, two pure axis
  families, both connector-axis families, both connector-boundary
  families, one mixed stratum, and one joint corner.
- **Promote the endpoint-free application scope:** apply (34.2)
  stratumwise only after global endpoint-prefix recombination, with
  artificial-pole cancellation and all actual factors retained.
- **Retain open:** estimates for the connector-completed axial vector,
  collision-uniform bounds, renormalized-side removal, joint height
  exhaustion, the axial-subtracted terminal symbol, complete beta
  transition, M9-M1, M9, and the Gauss-circle target.
