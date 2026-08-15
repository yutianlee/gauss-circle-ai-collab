# Round 33 blind report: finite mask, endpoint, and axial compatibility

Task: blind_mask_endpoint_axial_identity  
Role: statement-only blind rederivation  
Allocation: 100% analytical/algebraic; no computation and no external theorem

## 1. Result: exact finite compatibility identity

For the hierarchical beta mask
\[
 \Theta_\beta=\psi(\beta),\qquad
 \beta=\Im(s-(u+v)/2),
 \qquad \psi=1\ \hbox{near }0,                     \tag{33.1}
\]
endpoint collapse, the beta Cauchy--Green displacement, and finite
\(v\)-axis displacement commute, provided every radial piece uses the same
finite rectangle, mask, endpoint stars, profiles, floors, and residue
convention. The exact masked endpoint identity is
\[
 \boxed{
 T_{\xi}^{\beta}+S_{\xi}^{\beta}+P_{\xi}^{\beta}
 +C_{A,\xi}^{\beta}
 =D_{\xi}^{\beta}-A_{\xi}.}                        \tag{33.2}
\]
Here the upper radial side is left-to-right, the lower radial side is
right-to-left, and
\[
 C_{A,\xi}^{\beta}
 =-\iint_{R_A}\psi'(\beta)\,{\cal F}_{\xi}(A)\,
                  d(\Re A)\,d\beta                \tag{33.3}
\]
in the unnormalized Cauchy--Green convention. The arithmetic share
\(A_\xi\) is unfiltered because its pole is \(A=0\) and
\(\Theta_\beta(0)=1\).

After summing \(\xi\in\{1,N_X\}\), the endpoint artificial residue cancels
the opposite \(R_1\) residue and the arithmetic shares recombine exactly.
If
\[
 B_Q^\beta=T_Q^\beta+S_Q^\beta+C_{A,Q}^\beta ,
\]
then the finite mask-by-mask compatibility identity is
\[
\boxed{
 B_{R_1}^\beta+P_{R_1}^\beta+
 {\mathfrak R}_{\rm ar}^\beta[R_1]
 =
 B_G^\beta+{\mathfrak R}_{\rm ar}[G]
 -\sum_{\xi}D_\xi^\beta .}                         \tag{33.4}
\]
It is an equality of complete finite \(u,v\)-vector coefficients, before
any height limit or estimate.

Moving the \(v\)-line on either side of (33.4) adds, on every displayed
stratum, the upper left-to-right \(v\)-horizontal, minus the lower
left-to-right \(v\)-horizontal, the positive \(v=0\) residue contribution,
and the beta-mask area connector
\[
 C_{v,\beta}[Q]
 =-\iint \partial_\nu\Theta_\beta\,Q\,d(\Re v)\,d\nu
 ={1\over2}\iint\psi'(\beta)Q\,d(\Re v)\,d\nu .     \tag{33.5}
\]
Thus the \(v=0\) residue is a vector residue on the terminal, radial-side,
radial-connector, artificial, arithmetic, and endpoint-direct strata.
The \(u=0\) residue has positive sign, and the joint \(u=v=0\) corner
occurs exactly once.

Consequently the side-collapsed, endpoint-free residual has
\[
 {\cal E}_{\rm own}
 ={\cal H}_G-{\cal H}_{E_1}-{\cal H}_{R_1}=0,       \tag{33.6}
\]
and its ordinary physical \(L\)-derivative is also zero. If the
nonholomorphic axial connector (33.5) is omitted, it is the first explicit
nonzero masked boundary operator; ordinary Cauchy displacement of the
masked \(v\)-line is false.

No terminal symbol estimate follows from this identity.

## 2. Exact statement and hypotheses

### 2.1 Contour and normalization conventions

Use the finite \(A=s-(u+v)/2=x+i\beta\) rectangle from the accepted vector
kernel. Verticals point upward. In any horizontal variable, write
\(H_+\) and \(H_-\) for upper and lower segments both parametrized
left-to-right; their oriented combination is \(H_+-H_-\). Thus the
accepted endpoint notation
\[
 S_\xi=(\hbox{upper left-to-right})
       +(\hbox{lower right-to-left})
\]
is exactly \(H_{A,+}-H_{A,-}\).

Residue symbols below include the appropriate \(2\pi i\) factor or,
when all contour integrals are normalized by \(1/(2\pi i)\), the
corresponding normalized residue. This convention leaves every sign in
(33.2)--(33.5) unchanged.

Let
\[
 E_1=\sum_{\xi\in\{1,N_X\}}E_{\xi},\qquad
 G=E_1+R_1.                                         \tag{33.7}
\]
All three terms must carry identical finite \(u,v,A\) domains and the
same profiles, floors, endpoint stars, arithmetic coefficient,
\(\chi_4(q)\), and external normalization.

### 2.2 Masked endpoint identity

For any complete meromorphic finite integrand \(F(A)\), positive rectangle
orientation and Cauchy--Green give
\[
\begin{split}
 V_{x_0}^{\beta}[F]={}&V_{x_1}^{\beta}[F]
 +H_{A,+}^{\beta}[F]-H_{A,-}^{\beta}[F]\\
 &+\sum_{p\in R_A^\circ}2\pi i\,
       \psi(\Im p)\operatorname {Res}_{A=p}F
 -\iint_{R_A}\psi'(\beta)F\,dx\,d\beta .            \tag{33.8}
\end{split}
\]
Apply (33.8) to \(E_\xi\). Its two crossed poles are the artificial pole
and the arithmetic pole, with the accepted signed residue values
\(P_\xi\) and \(A_\xi\). Rearranging gives (33.2). The sign of
\(C_{A,\xi}^{\beta}\) is negative, and \(A_\xi\) appears with a minus sign
on the right of (33.2).

At the artificial pole \(A=\delta\), the endpoint and \(R_1\) residues
carry the same factor \(\psi(\Im\delta)\), so
\[
 P_{R_1}^{\beta}=-\sum_\xi P_\xi^\beta .            \tag{33.9}
\]
At \(A=0\), the hierarchical mask is one, so
\[
 {\mathfrak R}_{\rm ar}^{\beta}[R_1]
 ={\mathfrak R}_{\rm ar}[G]-\sum_\xi A_\xi .        \tag{33.10}
\]
If the two poles coalesce, (33.9)--(33.10) mean the single derivative
residue of the combined double pole, not two separately counted simple
residues.

### 2.3 Finite v-axis displacement

For every contour stratum \(Q\) in (33.4), moving an upward \(v\)-vertical
from \(\Re v=b>0\) to \(\Re v=\ell<0\), with finite height \(V\), gives
\[
\boxed{
 V_{v,b}^{\beta}[Q]
 =V_{v,\ell}^{\beta}[Q]
 +H_{v,+}^{\beta}[Q]-H_{v,-}^{\beta}[Q]
 +P_v^\beta[Q]+C_{v,\beta}[Q].}                    \tag{33.11}
\]
The two \(v\)-horizontals in (33.11) are both left-to-right. The crossed
\(v=0\) residue contribution \(P_v^\beta\) has positive sign. Since
\[
 \beta=t-(\mu+\nu)/2,\qquad
 \partial_\nu\Theta_\beta=-\frac12\psi'(\beta),
\]
the last term is exactly (33.5), with positive one-half coefficient.

The mask weights on the axial strata are
\[
 \Theta_\beta|_{v=0}=\psi(t-\mu/2),\qquad
 \Theta_\beta|_{u=0}=\psi(t-\nu/2),\qquad
 \Theta_\beta|_{u=v=0}=\psi(t).                    \tag{33.12}
\]
They are not generally one. “Full vector residue” therefore means that
the beta branch retains the residue of every vector stratum with the
weight in (33.12); the complementary hierarchical branches restore the
unmasked axial coefficient. Only the arithmetic \(A=0\) residue is
automatically unfiltered in this branch.

Applying (33.11) to (33.4) yields the exact finite axial compatibility
identity
\[
\begin{split}
 {\cal X}_v^\beta[
 B_{R_1}^\beta+P_{R_1}^\beta+
 {\mathfrak R}_{\rm ar}^\beta[R_1]]
 ={\cal X}_v^\beta[
 B_G^\beta+{\mathfrak R}_{\rm ar}[G]
 -\sum_\xi D_\xi^\beta],                         \tag{33.13}
\end{split}
\]
where \({\cal X}_v^\beta\) denotes the full five-term right side of
(33.11). Equation (33.13) lists the \(v=0\) residue and both finite
height connectors on every term exactly once.

### 2.4 u-axis and corner ledger

If the \(u\)-line is also moved, its upper-minus-lower side orientation is
the same, its \(u=0\) residue has positive sign, and
\[
 C_{u,\beta}[Q]
 =-\iint\partial_\mu\Theta_\beta Q
 ={1\over2}\iint\psi'(\beta)Q.                     \tag{33.14}
\]
Perform the two finite shifts sequentially on the once-masked density.
The nonresidue \(u/v\) boundary and area terms are retained; the residue
ledger is
\[
\begin{array}{c|c|c}
\text{share}&\text{mask value}&\text{sign}\\ \hline
v=0\text{ on each surviving }u\text{ stratum}
 &\psi(t-\mu/2)&+\\
u=0\text{ on each surviving }v\text{ stratum}
 &\psi(t-\nu/2)&+\\
u=v=0\text{ joint corner}&\psi(t)&+\text{, once}.
\end{array}                                                    \tag{33.15}
\]
The corner is the residue of the \(u=0\) share when the remaining
\(v\)-line is moved, or equivalently the residue of the \(v=0\) share
under the \(u\)-move. It is not added again as an independent third
operation.

## 3. Proof or derivation

Equation (33.8) is the accepted Cauchy--Green formula:
\[
 2i\bar\partial\Theta_\beta
 =2i(i/2)\partial_\beta\Theta_\beta
 =-\psi'(\beta).
\]
Its positive boundary is lower left-to-right, right upward, upper
right-to-left, and left downward. Solving for the right vertical gives
upper left-to-right minus lower left-to-right, which proves every
orientation and the negative sign in (33.3).

Sum (33.2) over \(\xi\), and abbreviate the sum by a subscript \(E\):
\[
 B_E^\beta+P_E^\beta=D_E^\beta-A_E.                \tag{33.16}
\]
Linearity of every finite stratum and (33.7) give
\[
 B_{R_1}^\beta=B_G^\beta-B_E^\beta.                \tag{33.17}
\]
Insert (33.16), then use (33.9)--(33.10):
\[
\begin{split}
 B_{R_1}^\beta+P_{R_1}^\beta+
 {\mathfrak R}_{\rm ar}^\beta[R_1]
={}&B_G^\beta-D_E^\beta+A_E+P_E^\beta\\
 &-P_E^\beta+{\mathfrak R}_{\rm ar}[G]-A_E,
\end{split}
\]
which is (33.4). This calculation shows that the artificial residue,
endpoint arithmetic image, and physical arithmetic residue are each
owned once.

For the \(v\)-move, apply the same positive-rectangle calculation to the
nonholomorphic density
\(\Theta_\beta Q\). Since
\(\partial_\nu\Theta_\beta=-\psi'(\beta)/2\), its area term is (33.5).
This proves (33.11). All operations in (33.11) are linear, so applying
them to both sides of (33.4) proves (33.13). In particular,
\[
\begin{split}
 P_v^\beta[B_{R_1}^\beta]
={}&P_v^\beta[T_{R_1}^\beta]
 +P_v^\beta[S_{R_1}^\beta]
 +P_v^\beta[C_{A,R_1}^\beta],                    \tag{33.18}
\end{split}
\]
and \(P_v^\beta\) also acts on
\(P_{R_1}^\beta\), \({\mathfrak R}_{\rm ar}^\beta[R_1]\), and the
endpoint-direct term on the other side. Thus no scalar “terminal-only”
axial residue can replace the required vector residue.

Sequential residue extraction at two transverse simple axes gives
\[
 \operatorname {Res}_{u=0}\operatorname {Res}_{v=0}
 =\operatorname {Res}_{v=0}\operatorname {Res}_{u=0}.
\]
Expanding the two one-variable shifts has four residue classes:
no axis, \(u=0\) only, \(v=0\) only, and \(u=v=0\). This proves
(33.15) and the one-count corner rule. Coupled-pole collisions must instead
use their single combined derivative residue.

Finally, let \({\cal L}_{33}\) be the complete finite linear operation
consisting of: hierarchical masking, both Cauchy--Green connectors,
endpoint collapse, common side removal when licensed, and vector axial
extraction. Then
\[
\begin{split}
 {\cal E}_{\rm own}
 &={\cal L}_{33}G-{\cal L}_{33}E_1-{\cal L}_{33}R_1\\
 &={\cal L}_{33}(G-E_1-R_1)=0.                    \tag{33.19}
\end{split}
\]
Because (33.19) is an exact finite identity as a function of the physical
parameter \(L\), its fixed-\(\nu\) derivative is zero wherever classical
derivatives exist and is zero distributionally across affine switches.
This proves (33.6).

## 4. First doubtful or unproved step

There is no remaining algebraic ownership defect after every term in
(33.3), (33.5), and (33.14) is retained. The first missing step is
analytic: the accepted statements do not bound the axial-subtracted,
connector-completed terminal kernel or its finite-height tails.

If one attempts an ordinary meromorphic \(v\)-shift of the masked
integrand and omits Cauchy--Green, the first explicit surviving boundary
operator is exactly
\[
 {1\over2}\iint\psi'(\beta)Q\,d(\Re v)\,d\nu        \tag{33.20}
\]
on each terminal, radial-side, radial-connector, arithmetic, and endpoint
stratum. Omitting (33.20) would make the claimed commutation false and
would re-create a nonzero \(\rho^0\) ownership defect. The analogous
\(u\)-connector is (33.14).

No estimate for (33.20), no removal of its height boundaries, and no
\(\lambda^{-2}/\lambda^{-3}\) symbol bound is proved here.

## 5. Control tests and outcomes

### Hierarchical-versus-disjoint-mask

**Pass.** The proof uses only \(\Theta_\beta=\psi(\beta)\). It has one
radial connector and gives weight one at \(A=0\). The disjoint mask
\(\psi(\beta)(1-\psi(\alpha))\) has two derivative edges and gives
\(A=0\) weight \(1-\psi(\Im z)\); substituting it into (33.10) would
incorrectly replace a filtered arithmetic share by the accepted full one.

### Cauchy-green-orientation

**Pass.** Radial and axial upper sides enter positively and lower
left-to-right sides negatively. The radial area connector is
\(-\iint\psi'(\beta)F\). Because \(\partial_\nu\beta=-1/2\), the
\(v\)-area connector is \(+\frac12\iint\psi'(\beta)F\).

### Endpoint-artificial-arithmetic-ledger

**Pass.** Equation (33.4) follows by exact cancellation of
\(+P_E-P_E\) and \(+A_E-A_E\). At a pole collision, a single derivative
residue replaces the two simple entries. No endpoint module is inserted
back into the terminal symbol.

### Axial-residue-and-corner-count

**Pass.** Equation (33.18) displays the vector nature of the \(v=0\)
residue. The \(u=0\) and \(v=0\) shares are positive, and their joint
corner appears once with mask \(\psi(t)\). Finite horizontals and mask
area connectors remain.

### Rho-ownership-defect

**Pass algebraically.** Equation (33.19) proves
\({\cal E}_{\rm own}=0\) and
\(\partial_L{\cal E}_{\rm own}=0\) for the fully compatible
endpoint-free residual. This is an identity, not a weighted-symbol
estimate.

### Scope correction: masked endpoint versus accepted physical module

Equations (33.2)--(33.4) route the beta branch to
\(D_\xi^\beta\), not to the accepted unmasked physical endpoint
\(D_\xi\). The hierarchical beta branch has no internal complementary
share: its mask is exactly \(\psi(\beta)\). Therefore the accepted theorem
for \(D_\xi\) cannot be applied to \(D_\xi^\beta\) in isolation.

The exact recombination occurs only in the global three-mask partition:
\[
\begin{split}
 D_\xi={}&D_\xi^{\psi(\beta)}
 +D_\xi^{(1-\psi(\beta))\psi(\alpha)}\\
 &+D_\xi^{(1-\psi(\beta))(1-\psi(\alpha))}.         \tag{33.21}
\end{split}
\]
Since (33.21) is a pointwise partition on the original right-line
endpoint integral, it introduces no additional connector there. If its
three terms are first obtained by separate contour displacements, all
mask-boundary Cauchy--Green connectors must also be recombined before
(33.21) is invoked.

Consequently this report proves two different statements with different
scopes:

1. **Local ownership:** within the same beta mask,
   \({\cal E}_{\rm own}=0\) and
   \(\partial_L{\cal E}_{\rm own}=0\). This remains valid.
2. **Physical endpoint-module compatibility:** not yet proved inside the
   frozen beta operator. The masked survivors
   \(D_\xi^\beta\) must either be estimated by a new masked endpoint
   theorem or be held until the alpha-transition and outer complementary
   shares in (33.21), together with their connectors, are available.

Thus the recommendation to route endpoint terms to existing modules is
conditional on global hierarchical recombination. At the close of the
beta-only identity, \(D_\xi^\beta\) is an exact but unestimated boundary
survivor.

## 6. Dependencies and exact artifacts used

Only the following permitted artifacts were read or used:

1. protocol.md;
2. state/active_campaign.yml;
3. rounds/codex-managed/m9-m1-vector-hankel-kernel/synthesis.md;
4. rounds/codex-managed/m9-m1-endpoint-boundary-cauchy/synthesis.md;
5. rounds/codex-managed/m9-m1-beta-transition-connector/synthesis.md;
6. rounds/codex-managed/m9-m1-beta-complete-physical-height-symbol/synthesis.md.

No proof graph, proof draft, excluded review, Round-33 claimant report,
computation, or web source was read or used.

## 7. Recommended state effect

- **Promote as exact finite beta-mask algebra:** the hierarchical masked
  endpoint identity (33.2), the recombined beta identity (33.4), and the
  finite axial identity (33.11)--(33.13), with the stated signs and
  collision convention.
- **Promote the one-count ledger:** full \(A=0\) arithmetic ownership,
  artificial-pole cancellation, vector \(v=0\) residues on every stratum,
  positive \(u=0\) and \(v=0\) shares, and one positive joint corner.
- **Promote the local ownership conclusion:** under the same beta mask,
  \({\cal E}_{\rm own}=0\) and its physical \(L\)-derivative vanish.
- **Reject:** applying ordinary Cauchy displacement to the nonholomorphic
  beta-masked \(u\)- or \(v\)-line. The missing operator would be
  (33.20).
- **Retain as an exact unestimated survivor:** \(D_\xi^\beta\). Existing
  unmasked endpoint modules apply only after the global three-mask
  recombination (33.21), including cancellation of all connectors.
- **Retain open:** estimates for the connector-completed,
  axial-subtracted side-collapsed terminal symbol, finite-height
  exhaustion, complete beta transition, M9-M1, M9, and the Gauss-circle
  target.
