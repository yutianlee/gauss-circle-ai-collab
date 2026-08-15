# Round 37 blind report: the fixed-box endpoint-free vector is canonical, but its outside-height limit has an exact survivor

Task: blind_endpoint_free_limit_identity  
Role: statement-only blind rederivation  
Allocation: 100% analytical/algebraic; no computation and no external theorem

## 1. Result

The endpoint-free complement has a unique exact finite definition on the
original fixed-\(w\) meromorphic antecedent.  Write the accepted radial
decomposition as
\[
 G_v=E_{1,v}+R_{1,v},
 \qquad
 \mathfrak P_\rho[E_1]+\mathfrak P_\rho[R_1]=0,     \tag{37.1}
\]
where \(\mathfrak P_\rho\) is the artificial-pole coefficient with the
accepted contour orientation.  If \(\mathfrak T,\mathfrak S\) denote the
finite terminal line and its two radial sides, then the common
positive-line module has the pre-collapse representative
\[
 \mathfrak M_{\rm fin}
 =\mathfrak T[E_1]+\mathfrak S[E_1]
  +\mathfrak P_\rho[E_1]+\mathfrak R^{\rm ar}[G].   \tag{37.2}
\]
Consequently the frozen subtraction gives the finite identity
\[
\boxed{
 \mathfrak V_{\rm ef}^{\rm fin}
 :=\mathfrak V_{\rm pre}^{\rm fin}-\mathfrak M_{\rm fin}
 =\mathfrak T[R_1]+\mathfrak S[R_1]
  +\mathfrak P_\rho[R_1].}                         \tag{37.3}
\]
No off-centred Perron variable, sharp support, or physical star is inserted
in (37.3).

After beta localization and the complete two-axis transfer, the radial-side
term in (37.3) is identically zero under the accepted compact-support
separation.  The remaining terminal/artificial vector has exactly the
sixteen strata in Section 2.  At every fixed finite \(U,V\), their **signed
sum** has the accepted Plemelj limit as the hard-top line approaches its
physical boundary.  This defines a canonical finite-box distribution.

The permitted results do not prove the subsequent symmetric
\(U,V\to\infty\) physical-profile limit.  The first exact survivor is the
polytope-aware principal-value functional
\(\mathcal J^{\rm ef}_{U,V}\) in (37.12).  Its moving logarithmic faces are
locally integrable at each fixed box, but no permitted estimate makes
\(\mathcal J^{\rm ef}_{H,H}\) Cauchy as \(H\to\infty\).  Thus existence and
uniqueness of the full endpoint-free axial-vector limit remain open; this is
a height-tail obstruction, not a failure of the finite definition or of the
signed Plemelj limit.

## 2. Exact statement and hypotheses

All operations are performed at finite \(U,V,S\) on the original
fixed-\(w\) contours.  The terminal endpoint-free density is
\[
\begin{aligned}
 Q_{\rm ef}(s,u,v;h,q,m)={}&\mathbf1_{hq=m}\chi_4(q)
 \sum_j\widehat W_j(u)\widehat\phi(v)
 \left(\frac{D_j}{2\sqrt X}\right)^u(H_j+1)^v
 \left(\frac hq\right)^{(u+v)/2}\\
 &\times R_{1,v}(1-s)K_{u+v}(1-s)m^{-s},           \tag{37.4}
\end{aligned}
\]
together with its single oriented artificial-pole component
\(\mathfrak P_\rho[R_1]\).  Put
\[
 \mathbf Q_{\rm ef}:=\mathfrak T[Q_{\rm ef}]
                     +\mathfrak P_\rho[R_1],
 \qquad
 \Theta_\beta=\psi\!\left(t-\frac{\mu+\nu}{2}\right).             \tag{37.5}
\]
The actual profiles \(W_j,\phi\), scales \(D_j\), floors \(H_j+1\), hard
top, \(\chi_4\), and all finite equality conventions remain in (37.4).
The external functional
\[
 \mathcal N_X[Z]:=-\frac4\pi X^{1/4}
 \operatorname {Re}\!\{e(1/8)Z\}                 \tag{37.6}
\]
is applied once, after the complete vector is assembled.

Let \(B_j=H_{j,+}-H_{j,-}\), \(F_j=L_j+B_j\), let \(P_j\) be the
coordinate-axis residue, and let \(A_j\) be positive area integration.
The full post-module finite beta vector is
\[
\begin{aligned}
\mathfrak B_{\rm ef}^{\rm fin}={}&
 L_uL_v[\Theta_\beta\mathbf Q_{\rm ef}]
 +L_uB_v[\Theta_\beta\mathbf Q_{\rm ef}]
 +B_uL_v[\Theta_\beta\mathbf Q_{\rm ef}]
 +B_uB_v[\Theta_\beta\mathbf Q_{\rm ef}]\\
&+L_uP_v[\Theta_\beta\mathbf Q_{\rm ef}]
 +B_uP_v[\Theta_\beta\mathbf Q_{\rm ef}]
 +P_uL_v[\Theta_\beta\mathbf Q_{\rm ef}]
 +P_uB_v[\Theta_\beta\mathbf Q_{\rm ef}]\\
&+P_uP_v[\Theta_\beta\mathbf Q_{\rm ef}]\\
&+\frac12L_uA_v[\psi'\mathbf Q_{\rm ef}]
 +\frac12B_uA_v[\psi'\mathbf Q_{\rm ef}]
 +\frac12P_uA_v[\psi'\mathbf Q_{\rm ef}]\\
&+\frac12A_uL_v[\psi'\mathbf Q_{\rm ef}]
 +\frac12A_uB_v[\psi'\mathbf Q_{\rm ef}]
 +\frac12A_uP_v[\psi'\mathbf Q_{\rm ef}]\\
&+\frac14A_uA_v[\psi''\mathbf Q_{\rm ef}].       \tag{37.7}
\end{aligned}
\]
This is the complete inventory: four ordinary boundary products, four
boundary-axis terms, one joint corner, four connector-boundary terms, two
connector-axis terms, and one mixed area.  The artificial component in
\(\mathbf Q_{\rm ef}\) is carried through these same sixteen cells; it is
not a seventeenth cell.  If an artificial, arithmetic, and/or axial divisor
coincides, the relevant row contains one combined local coefficient.  The
corner \(P_uP_v\) is counted once.

The module (37.2) has already been subtracted globally.  Hence no
\(D_\xi\), \(\mathfrak R^{\rm ar}[R_1]\), finite Perron tail, or physical
endpoint star is to be subtracted again from any row of (37.7).

For a concrete prescribed exhaustion set
\[
 U=V=H,\qquad
 S_H=(2+X+2H+2B_0)^2,                              \tag{37.8}
\]
form all fixed-\(w\) finite identities first, take the signed hard-top
boundary limit at fixed \(H\), and only then let \(H\to\infty\) through the
original Mellin/profile contours.  Condition (37.8) both contains the
beta-supported terminal \(t\)-section and annihilates every transferred
radial side.

## 3. Proof or derivation

The finite pre-vector furnished by the fixed-\(w\) contour shift is
\[
 \mathfrak V_{\rm pre}^{\rm fin}
 =\mathfrak T[G]+\mathfrak S[G]+\mathfrak R^{\rm ar}[G].          \tag{37.9}
\]
Round-36 aggregate routing permits (37.2) to be subtracted from (37.9)
before any physical limit.  Linearity, \(G=E_1+R_1\), and the zero local
germ in (37.1) give (37.3).  This also fixes the artificial-residue sign:
the residual term \(-\mathfrak P_\rho[E_1]\) is precisely
\(+\mathfrak P_\rho[R_1]\).  The full arithmetic residue cancels in the
subtraction, so retaining a separate arithmetic cell afterward would double
count the boundary module.

Apply the finite product Cauchy--Green identity to
\(\Theta_\beta\mathbf Q_{\rm ef}\).  Since
\[
 \partial_\mu\Theta_\beta=\partial_\nu\Theta_\beta
 =-\frac12\psi'(\beta),\qquad
 \partial_\mu\partial_\nu\Theta_\beta
 =\frac14\psi''(\beta),                            \tag{37.10}
\]
the two first connectors have coefficient \(+1/2\), and the mixed connector
has coefficient \(+1/4\).  Expanding both \(F_j\)'s produces (37.7), with no
missing connector-axis image.  Sequential residue ownership produces one
corner.  Local combined residues make (37.1) valid even at a collision.

On a radial side \(t=\pm S_H\), whereas \(|\mu|,|\nu|\le H\); hence
\[
 |\beta|\ge S_H-H>2B_0.
\]
The mask and all of its derivatives vanish on an open neighborhood of each
side stratum.  Thus the complete transfer of \(\mathfrak S[R_1]\) is zero
before any limit, justifying its absence from (37.5)--(37.7).

It remains to examine the physical top boundary.  At fixed \(U,V\), sum
all cells first and write its regular numerator as \(F(\mu,\nu)\).  The
accepted signed finite-box identity is
\[
\lim_{a\downarrow0}\int_{-V}^{V}\int_{-U}^{U}
 \frac{F(\mu,\nu)}{a+i\mu}\,d\mu\,d\nu
 =\pi\int_{-V}^{V}F(0,\nu)\,d\nu
 -i\int_{-V}^{V}\operatorname {PV}\!\int_{-U}^{U}
   \frac{F(\mu,\nu)}{\mu}\,d\mu\,d\nu .          \tag{37.11}
\]
The delta and principal-value pieces in (37.11) are the limit of the
complete finite operator.  They must not be added again to the explicit
\(P_u\) rows of (37.7); finite Stokes already reconciles those rows with the
right-line expression before (37.11) is taken.

Put \(L=\mu+\nu\) and
\(I_{U,V}(L)=[-V,V]\cap[L-U,L+U]\).  Absorbing the exact two signed
phases, beta mask, \(t\)-integration, sums, profiles, floors, character,
and the artificial component into \(\mathcal H_{\rm ef}(L,\nu)\), the
post-Plemelj finite-box functional is
\[
\boxed{\begin{aligned}
 \mathcal J^{\rm ef}_{U,V}:=\mathcal N_X\!\int
 \Bigg\{&\pi\mathbf1_{|L|<V}\mathcal H_{\rm ef}(L,L)\\
 &-i\operatorname {PV}\!\int_{I_{U,V}(L)}
   \frac{\mathcal H_{\rm ef}(L,\nu)}{L-\nu}\,d\nu
 \Bigg\}\,dL .                                    \tag{37.12}
\end{aligned}}\]
This is not a model kernel: \(\mathcal H_{\rm ef}\) denotes the assembled
actual vector (37.7) with every factor in (37.4)--(37.6) retained.

At the upper moving face the vertical and the oriented upper horizontal
have the same logarithmic coefficient; at the lower face the vertical and
the negative lower horizontal have the same coefficient.  Therefore the
faces transfer rather than cancel the edge.  When the numerator is nonzero,
the prelimit section satisfies
\[
 C_{a;U,V}^{\rm ef}(V)
 =-i\mathcal H_{\rm ef}(V,V)\log(1/a)+O(1),         \tag{37.13}
\]
and after (37.11) this becomes a locally integrable
\(\log|L-V|\) singularity.  Local integrability proves (37.12) for each
finite box; it gives no control of the mass transported to
\(L=\pm H\) as \(H\to\infty\).

Thus the desired remaining statement is exactly the Cauchy property
\[
 \mathcal J^{\rm ef}_{2H,2H}-\mathcal J^{\rm ef}_{H,H}\longrightarrow0.
 \tag{37.14}
\]
No permitted theorem bounds (37.14), and the finite identities do not
cancel it.  This isolates the first exact survivor.

## 4. First doubtful or unproved step

The first unproved step is the outside-height/profile exhaustion (37.14).
The finite-box Plemelj theorem controls the singularity locally in \(L\),
but its constants supply no decay as the polytope faces move to infinity.
Nor can the upper and lower \(v\)-horizontals be called missing height tails:
their signs reproduce the moving logarithmic edges.  Compact beta support
controls the radial \(s\)-sides, not the unbounded diagonal
\(L=\mu+\nu\).

Proving (37.14) requires a uniform distribution-first oscillatory estimate
for the actual logarithmic amplitude on moving faces, together with its
outside-axis and collision traces.  The permitted fixed-order Hankel result
does not provide such an estimate because the two conductor-transition
planes sweep the outside heights.  This is the first precise analytic
survivor; no claim of actual divergence is made.

## 5. Required controls and outcomes

### Fixed-\(w\) finite-complement definition

**Pass.**  Equations (37.1)--(37.3) define the complement before the moving
change \(r=w-3/4-v/2\).  Freezing the resulting off-centred \(r\)-path would
omit \(v\)-dependent path-boundary terms and is not used.

### Complete post-module stratum inventory

**Pass.**  Equation (37.7) lists all sixteen terminal/artificial strata:
four boundary products, four boundary-axis cells, one corner, four
connector-boundary cells, two connector-axis cells, and one mixed area.
Radial sides are zero by support; arithmetic and endpoint modules were
removed globally.

### No boundary-module double count

**Pass.**  \(\mathfrak M_{\rm fin}\) is subtracted once in (37.3).  No
\(D_\xi\), recombined \(R_1\) arithmetic term, Perron tail, or physical
star is removed row by row.

### Signed Plemelj and moving logarithmic faces

**Finite-box pass.**  Equation (37.11) has the positive delta and negative
principal-value signs.  Equations (37.12)--(37.13) retain both moving faces;
their logarithms are locally integrable but do not cancel.

### Outside-height tail and face limit

**Open.**  The exact remaining condition is (37.14).  Neither local
\(L^p\) control nor finite Stokes yields uniform decay on the expanding
polytope.

### Collision, corner, and artificial-residue ownership

**Pass at finite level.**  Artificial cancellation fixes the sign in
(37.3); a collision uses one combined coefficient, connector-axis residues
remain in (37.7), and \(P_uP_v\) occurs once.  No separate limit of these
pieces is asserted.

### Actual normalization and no terminal-symbol overreach

**Pass.**  Equations (37.4)--(37.6) retain the actual profiles, scales,
floors, hard top, \(\chi_4\), equality conventions, and the external
\(X^{1/4}\) multiplier once.  No \(\lambda^{-2}\), \(\lambda^{-3}\), or
target-size estimate is claimed.

## 6. Dependencies and exact artifacts used

Only the following permitted artifacts were read or used:

1. `protocol.md`;
2. `state/active_campaign.yml`;
3. `rounds/codex-managed/m9-m1-vector-hankel-kernel/synthesis.md`;
4. `rounds/codex-managed/m9-m1-beta-outside-v-side-reconciliation/synthesis.md`;
5. `rounds/codex-managed/m9-m1-beta-complete-axial-connector-ledger/synthesis.md`;
6. `rounds/codex-managed/m9-m1-beta-axial-side-exhaustion/synthesis.md`;
7. `rounds/codex-managed/m9-m1-beta-physical-module-transfer/synthesis.md`.

No proof graph, proof draft, excluded report, Round-37 claimant report,
computation, or web source was read or used.

## 7. Recommended state effect

- **Promote** the exact fixed-\(w\) finite-complement identity (37.3), its
  artificial-residue sign, and the complete post-module inventory (37.7).
- **Promote**, at fixed finite \(U,V\), the signed aggregate Plemelj limit
  (37.11) and the locally integrable polytope representation (37.12).
- **Retain open** existence and uniqueness of the full symmetric
  outside-height/physical-profile limit.  Its first exact survivor is the
  Cauchy difference (37.14), including the noncancelling moving logarithmic
  faces and all actual vector factors.
- **Reject** a frozen off-centred Perron path, termwise face limits,
  duplicate boundary-module subtraction, deletion of moving sides, or any
  inference of a terminal-symbol estimate.
