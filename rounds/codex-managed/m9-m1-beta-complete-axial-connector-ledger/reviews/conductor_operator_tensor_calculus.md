# Conductor product-operator calculus for Round 34

Campaign: `m9-m1-beta-complete-axial-connector-ledger`  
Role: conductor independent algebra  
Allocation: 100% analytical/algebraic

## 1. Normalized one-axis transfer

Let \(R_u=[a_-,a_+]\times[-U,U]\) and
\(R_v=[b_-,b_+]\times[-V,V]\), with right vertical minus left vertical
as the transfer direction. For a density \(M(u,v)=\Theta(u,v)Q(u,v)\),
where \(Q\) is separately meromorphic and no pole lies on a boundary,
define

\[
 \mathcal X_v M
 :=H_{v,+}M-H_{v,-}M
   +2\pi i\operatorname {Res}_{v=0}M
   +2i\iint_{R_v}\bar\partial_vM.                 \tag{34.C1}
\]

Then \(V_{v,b_+}M=V_{v,b_-}M+\mathcal X_vM\). Away
from poles, \(2i\bar\partial_vM=-\partial_\nu\Theta\,Q\).
For

\[
 \Theta=\psi(\beta),\qquad
 \beta=t-\frac{\mu+\nu}{2},
\]

this is \(+\frac12\psi'(\beta)Q\). Define \(\mathcal X_u\)
symmetrically.

## 2. Full product expansion

Apply the two identities sequentially. In schematic tensor notation,

\[
 V_{u,+}V_{v,+}M
 =V_{u,-}V_{v,-}M
  +V_{u,-}\mathcal X_vM
  +\mathcal X_uV_{v,-}M
  +\mathcal X_u\mathcal X_vM.                     \tag{34.C2}
\]

The mixed term \(\mathcal X_u\mathcal X_vM\) contains nine
classes:

\[
 H_uH_v,quad H_uR_v,quad H_uC_v,quad
 R_uH_v,quad R_uR_v,quad R_uC_v,quad
 C_uH_v,quad C_uR_v,quad C_uC_v.                 \tag{34.C3}
\]

Here \(H\) denotes the oriented horizontal-pair operator, \(R\) the
axis residue, and \(C\) the nonholomorphic area connector. Each class
inherits its own finite boundary. In particular, \(R_uC_v\) is the
\(u=0\) residue of the first connector, and \(C_uC_v\) is not merely a
scalar mixed derivative unless all four real directions and their faces
are spelled out.

For a smooth separately holomorphic \(Q\), the interior density in
\(C_uC_v\) includes

\[
 (-\partial_\mu)(-\partial_\nu)\Theta\,Q
 =\partial_\mu\partial_\nu\Theta\,Q
 =\frac14\psi''(\beta)Q.                          \tag{34.C4}
\]

If one expands by product rule before excising poles, derivatives of
\(Q\) appear and obscure (34.C4). The safer definition is the sequential
Cauchy--Green operator on the full meromorphic density, with small tubes
around axes; their boundaries generate the connector-axis residues.

## 3. Order reversal

The underlying four-real-dimensional boundary identity is symmetric in
the two rectangles. Hence the complete expansions of
\(\mathcal X_u\mathcal X_v\) and
\(\mathcal X_v\mathcal X_u\) agree after relabelling faces. But equality
is not termwise between only \(H,R,C\) labels: a horizontal of one order
may be a boundary of an area connector in the other. A valid proof must
match the full oriented cell complex, not just the pure residues.

For transverse simple poles, one may choose:

\[
 R_u+R_v-R_{uv}                                    \tag{34.C5}
\]

with full axes, or corner-deleted axes plus \(+R_{uv}\). Equation
(34.C2) naturally uses a sequential/corner-deleted convention if the
second residue is taken inside the first residue stratum. The final graph
statement should specify the convention rather than merely say the corner
is positive.

## 4. Actual-kernel scope

Linearity applies stratumwise to the terminal, renormalized radial sides,
and residual arithmetic pieces only before any of those strata is removed
by a limiting theorem. After global endpoint collapse, the endpoint
prefixes must not be reinserted. Conversely, an artificial \(R_1\) pole
cannot be assigned to the endpoint-free terminal share unless its
canceling endpoint ledger remains referenced across every axis shift.

The external factor

\[
 -\frac4\pi X^{1/4}\Re\{e(1/8)(\cdots)\}
\]

is applied once after the finite vector identity is recombined.

No estimate or computation is claimed.
