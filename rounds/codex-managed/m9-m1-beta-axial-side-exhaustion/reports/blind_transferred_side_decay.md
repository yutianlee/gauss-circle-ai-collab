# Round 35 blind report: exact compact-support exhaustion of every transferred radial side

Task: blind_transferred_side_decay  
Role: statement-only blind rederivation  
Allocation: 100% analytical/algebraic; no computation and no external theorem

## 1. Result

The frozen beta mask gives a stronger conclusion than arbitrary-order radial
decay.  Every one of the sixteen finite axis-transfer images of either
renormalized radial side is identically zero once the radial height is
separated from the two axial heights.

Indeed, the canonical Round-26 hypothesis is
\[
 \psi\in C_c^\infty(\mathbb R),\qquad \psi(-x)=\psi(x),\qquad
 \psi=1\ \hbox{on }[-B_0,B_0],\qquad
 \operatorname {supp}\psi\subset[-2B_0,2B_0].       \tag{35.1}
\]
Consequently every derivative of \(\psi\) vanishes off
\([-2B_0,2B_0]\).  On a reflected radial side,
\[
 t=\Im s=\varepsilon S,\qquad
 \beta=t-\frac{\mu+\nu}{2}
       =\varepsilon S-\frac{\mu+\nu}{2},qquad
 \varepsilon\in\{+1,-1\},                         \tag{35.2}
\]
where \(|\mu|\le U\) and \(|\nu|\le V\).  Thus
\[
 |\beta|\ge S-\frac{U+V}{2}.                       \tag{35.3}
\]
Under the strict separation
\[
 \boxed{S>\frac{U+V}{2}+2B_0},                     \tag{35.4}
\]
the mask, all mask derivatives, and hence every transferred side density
vanish on an open neighborhood of its finite contour.  Therefore, for every
endpoint-renormalization depth \(M\ge1\),
\[
 \boxed{{\mathsf X}_{uv}{\mathfrak S}^{(M)}_{\rm rad}=0}          \tag{35.5}
\]
as a finite-contour identity.  In particular, there is no surviving face,
connector, axis residue, joint corner, mixed \(\psi''\)-area, or combined
artificial/axial collision term to estimate.

One explicit common choice is
\[
 \boxed{M=1,\qquad
 S(X,U,V)=\bigl(2+X+U+V+2B_0\bigr)^2.}             \tag{35.6}
\]
It satisfies (35.4) and dominates \(X+U+V\).  Thus the side contribution is
already zero before taking any nested limit.

## 2. Exact statement and hypotheses

Let \({\mathfrak S}^{(M)}_{\rm rad}\) denote the two reflected,
endpoint-renormalized radial sides at \(\Im s=\pm S\).  Let
\({\mathsf X}_{uv}\) be the accepted finite two-axis transfer, with the same
artificial-pole ownership on faces, connectors, axes, and their intersections.
Assume only:

1. the compact mask hypothesis (35.1);
2. the product height restrictions \(|\Im u|=|\mu|\le U\) and
   \(|\Im v|=|\nu|\le V\) on all transfer faces and connector areas;
3. the beta coordinate is (35.2), also after either real-part shift;
4. combined residues are used when an axial pole and an artificial pole
   coincide; and
5. the support separation (35.4).

No bound for the radial remainder, gamma/profile factors, Mellin norms, or
individual residue coefficients is required.

For an explicit stratum audit, write \(F_j=L_j+B_j\), with
\(B_j=H_{j,+}-H_{j,-}\), let \(P_j\) be the coordinate-axis residue, and let
\(A_j\) be area integration.  Before applying support, the complete transfer
has the following sixteen formal strata; after applying (35.4), the last
column is their exact capacity:
\[
\begin{array}{c|c|c}
\#&\text{stratum}&\text{capacity under (35.4)}\\ \hline
1&L_uL_v[\psi Q]&0\\
2&L_uB_v[\psi Q]&0\\
3&B_uL_v[\psi Q]&0\\
4&B_uB_v[\psi Q]&0\\
5&L_uP_v[\psi Q]&0\\
6&B_uP_v[\psi Q]&0\\
7&P_uL_v[\psi Q]&0\\
8&P_uB_v[\psi Q]&0\\
9&P_uP_v[\psi Q]&0\\
10&\frac12L_uA_v[\psi'Q]&0\\
11&\frac12B_uA_v[\psi'Q]&0\\
12&\frac12P_uA_v[\psi'Q]&0\\
13&\frac12A_uL_v[\psi'Q]&0\\
14&\frac12A_uB_v[\psi'Q]&0\\
15&\frac12A_uP_v[\psi'Q]&0\\
16&\frac14A_uA_v[\psi''Q]&0.
\end{array}                                                     \tag{35.7}
\]
Here \(Q\) denotes the complete radial-side density other than the displayed
mask factor.  Formula (35.7) includes the one joint corner in row 9 and the
connector-axis residues in rows 5--8 and 12, 15.  If a collision convention
differentiates a displayed coefficient further, that coefficient is still
zero: every derivative of \(\psi\) vanishes on the same open neighborhood.

## 3. Proof or derivation

For either sign \(\varepsilon\), the reverse triangle inequality gives
\[
 \left|\varepsilon S-\frac{\mu+\nu}{2}\right|
 \ge S-\frac{|\mu|+|\nu|}{2}
 \ge S-\frac{U+V}{2}.                              \tag{35.8}
\]
By (35.4), the right-hand side is strictly larger than \(2B_0\).  Hence
\(\beta\notin\operatorname {supp}\psi\), with a positive margin uniform in
both finite axial rectangles.  Smooth compact support implies
\[
 \psi^{(k)}(\beta)=0\qquad(k=0,1,2,\ldots)          \tag{35.9}
\]
throughout that neighborhood.

Real-part contour shifts do not alter \(t,\mu,\nu\), so (35.8)--(35.9)
remain true on every face and connector.  Taking an axial residue sets the
corresponding height to its pole height (in particular, the coordinate-axis
residue has \(\mu=0\) or \(\nu=0\)); this only improves (35.8).  Taking both
residues gives the unique corner and again improves it.  The two connector
terms produced by differentiating the sheared beta mask carry \(\psi'/2\),
and their mixed area carries \(\psi''/4\); these vanish by (35.9).

Residue extraction is local.  Since the coefficient is identically zero on
an open neighborhood, an axial/artificial collision cannot resurrect it by
a derivative residue: its full local germ is zero.  Thus every row of
(35.7) is zero separately.  Their oriented sum proves (35.5), independently
of signs internal to the finite transfer and independently of \(M\).

Finally, for nonnegative \(X,U,V,B_0\), the value in (35.6) is strictly
larger than \((U+V)/2+2B_0\); hence it supplies a single explicit nesting
law.  No sheared rectangularization or enlargement of the permitted height
boxes is used.

## 4. First doubtful or unproved step

There is no missing coefficient in the transferred radial-side statement:
compact-support separation annihilates the coefficient before any estimate
of \(Q\) or any residue is invoked.

The first unresolved issue lies outside this scoped lemma.  Equation (35.5)
does not address the endpoint/arithmetic physical module, the unmasked sum
over all hierarchical shares, the axial-subtracted terminal symbol, or the
complete beta estimate.  It would also not apply to a different transfer
that changed \(t\) or enlarged \(|\mu|,|\nu|\) beyond \(U,V\); the accepted
finite two-axis transfer does neither.

## 5. Required control tests and outcomes

### Both reflected signs

**Pass.**  The reverse-triangle estimate (35.8) is independent of
\(\varepsilon\), so the top and bottom radial sides vanish simultaneously.

### All sixteen strata

**Pass.**  Rows 1--9 contain \(\psi\), rows 10--15 contain \(\psi'\), and
row 16 contains \(\psi''\).  All are exactly zero by (35.9).

### Axes, corner, and collision residues

**Pass.**  Axis restriction reduces the admissible height range, the joint
corner is counted once, and a combined derivative residue acts on a zero
local germ.  None leaves a survivor.

### One common \(M\) and nesting law

**Pass.**  Since the identity is independent of endpoint depth, \(M=1\)
suffices.  The polynomial choice (35.6) enforces uniform support separation
for the entire finite product geometry.

### Scope control

**Pass.**  The conclusion is only the renormalized radial-side commutator.
No physical-module or terminal-symbol estimate is inferred from it.

## 6. Dependencies and exact artifacts used

Only the following permitted artifacts were read or used:

1. `protocol.md`;
2. `state/active_campaign.yml`;
3. `rounds/codex-managed/m9-m1-radial-endpoint-renormalization/synthesis.md`;
4. `rounds/codex-managed/m9-m1-beta-complete-axial-connector-ledger/synthesis.md`.

The conductor's Round-35 follow-up identified the canonical compact-support
hypothesis now frozen in `state/active_campaign.yml`; the proof above checks
its coordinate, sign, and scope consequences independently.  No proof graph,
proof draft, excluded report, Round-35 claimant report, computation, or web
source was read or used.

## 7. Recommended state effect

- **Promote**, scoped to the frozen compact beta share: the complete
  transferred renormalized radial-side vector is identically zero under
  (35.4), uniformly in all sixteen strata and for every \(M\ge1\).
- **Promote** the explicit witness \(M=1\) and nesting law (35.6) for this
  side-exhaustion interface.
- **Retain open** the endpoint/arithmetic physical-module commutator, the
  unmasked hierarchical recombination, the axial-subtracted terminal symbol,
  the complete beta transition, M9-M1, M9, and the Gauss-circle target.
