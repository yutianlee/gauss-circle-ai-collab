# Round 33 synthesis: local rho compatibility, global endpoint recombination, and the axial connector survivor

Campaign: `m9-m1-beta-mask-endpoint-axial-compatibility`  
Round type: beta mask, endpoint, and axial compatibility  
Graph SHA-256 before patch: `62d2197f75b5d0ca1a8c2c320573c678328e8d36bbdad8dba5c997d0c97a2d29`

## Conductor decision

Round 33 proves the exact finite **local** ownership algebra but does not
promote the frozen compatibility obligation. The decisive correction is:
the hierarchical beta branch owns the full moving arithmetic residue, but
not the full endpoint prefix.

For the beta mask \(\Theta_\beta=\psi(\beta)\), the masked endpoint
identity is

\[
 T_\xi^\beta+S_\xi^\beta+P_\xi^\beta+C_{A,\xi}^\beta
 =D_\xi^\beta-A_\xi,                               \tag{33.1}
\]

where

\[
 C_{A,\xi}^\beta=-\iint\psi'(\beta){\cal F}_\xi.
                                                               \tag{33.2}
\]

At \(A=0\), \(\beta=0\) and \(\psi(0)=1\), so \(A_\xi\) is the full
arithmetic share. By contrast, \(D_\xi^\beta=D_\xi[\psi(\beta)]\) is a
masked right-line endpoint prefix. The already proved endpoint theorems
apply only to \(D_\xi[1]\), after the accepted physical profile limits.

The common same-mask operation remains linear. Thus, when the masked
endpoint outputs and every axial connector are retained,

\[
 {\cal E}_{\rm own}
 ={\cal H}[G]-{\cal H}[E_1]-{\cal H}[R_1]
 ={\cal H}[G-E_1-R_1]=0,                           \tag{33.3}
\]

meromorphically, and its physical \(L\)-derivative vanishes
distributionally. This closes the rho-definition seam. It does not close
the map from a beta-masked endpoint to the accepted unmasked module.

Finite displacement of the nonholomorphically masked \(v\)-line has an
additional area operator

\[
 C_{v,\beta}[Q]
 =-\iint\partial_\nu\Theta_\beta Q
 =\frac12\iint\psi'(\beta)Q,                       \tag{33.4}
\]

as well as the upper-minus-lower finite horizontals and the filtered
\(v=0\) residue on every contour stratum. A later \(u\)-shift acts on
(33.4), producing connector-axis terms and the mixed density
\(\psi''(\beta)/4\). The joint \(u=v=0\) corner is counted once. No
accepted estimate controls this connector-completed axial vector.

Therefore the exact remaining architecture has two interfaces:

1. recombine all three hierarchical endpoint masks before invoking the
   proved unmasked endpoint modules;
2. estimate the endpoint-free beta terminal remainder together with its
   complete masked axial/connector operator.

No numerical experiment or external theorem was used.

## Exact masked endpoint algebra

Let

\[
 \Theta_\beta=\psi(\beta),\quad
 \Theta_\alpha=(1-\psi(\beta))\psi(\alpha),\quad
 \Theta_o=(1-\psi(\beta))(1-\psi(\alpha)).          \tag{33.5}
\]

Then \(\Theta_\beta+\Theta_\alpha+\Theta_o=1\). The two internal beta
shares \(\psi(\beta)\psi(\alpha)\) and
\(\psi(\beta)(1-\psi(\alpha))\) cancel their
\(\psi'(\alpha)\) edges and add to \(\Theta_\beta\), not to one.
Consequently they yield (33.1), not the unmasked endpoint identity.

Summing all three global masks gives

\[
 D_\xi^\beta+D_\xi^\alpha+D_\xi^o=D_\xi.          \tag{33.6}
\]

Their radial Cauchy--Green connector densities sum to zero because the
masks sum to one. Equation (33.6), with all branch connectors first
recombined, recovers the accepted unmasked endpoint module. This validates
the Round-32 boundary-first order only in the following precise sense:
collapse the endpoint on the global operator before localization, or keep
all three masked endpoint shares until (33.6) is formed. Deleting
\(D_\xi^\beta\) inside the beta branch by citing the unmasked theorem is
invalid.

The artificial rho residues of \(E_1\) and \(R_1\) carry the same mask
and cancel. At a collision with the arithmetic pole they are taken as one
derivative residue. The arithmetic recombination is full in the beta
branch because \(\Theta_\beta(0)=1\). These facts do not change (33.6).

## Finite axial Cauchy--Green ledger

At fixed \(s,u\), with

\[
 \beta=t-\frac{\mu+\nu}{2},
\]

positive rectangle orientation gives

\[
\begin{aligned}
 V_{b_+}^\beta[Q]={}&V_{b_-}^\beta[Q]
 +H_{v,+}^\beta[Q]-H_{v,-}^\beta[Q]\
 &+2\pi i\operatorname {Res}_{v=0}(\Theta_\beta Q)
 +C_{v,\beta}[Q].                                  \tag{33.7}
\end{aligned}
\]

The axial mask weights are generally filtered:

\[
 \Theta_\beta|_{v=0}=\psi(t-\mu/2),\qquad
 \Theta_\beta|_{u=0}=\psi(t-\nu/2),
 \qquad \Theta_\beta|_{u=v=0}=\psi(t).            \tag{33.8}
\]

Thus the beta branch does not own an unmasked axial coefficient. The
operation in (33.7) must be applied to terminal, radial-side, endpoint,
artificial, arithmetic, and radial-connector strata. If the \(u\)-line is
also moved, it must also be applied to the \(v\)-horizontals and
\(C_{v,\beta}\). This produces the mixed connector and its boundary/axis
traces. Pure \(u=0\), \(v=0\), and corner residues alone are incomplete.

One may use either full-axis inclusion--exclusion
\(R_u+R_v-R_{uv}\), or corner-deleted axis shares plus one positive
corner. The two conventions agree when every connector stratum is kept.

## Exact ownership scope

There are two legitimate common operators:

- a beta-retained operator that keeps \(D_\xi^\beta\) and all its axial
  images explicit;
- a globally collapsed operator that first sums (33.5), invokes (33.6),
  and only then routes \(D_\xi\) to the accepted endpoint module.

For either one, applied identically to \(G,E_1,R_1\), equation (33.3)
holds to every rho Taylor order and after fixed-physical-height
differentiation. It fails as a bookkeeping claim for a hybrid operation
that discards \(D_\xi^\beta\) without its complementary shares or omits
the axial connector (33.4).

The local rho seam is therefore solved. The global mask-to-module
compatibility and the size of the connector-completed axial vector remain
open.

## Smallest survivors

The beta-only endpoint survivor is

\[
 {\cal D}_{\rm end}^\beta
 =-\frac4\pi X^{1/4}\Re\!\left{
 e(1/8)\sum_{\xi\in\{1,N_X\}}D_\xi^\beta\right}.  \tag{33.9}
\]

Round 33 proves no bound for (33.9). It should not be attacked separately
unless global boundary-first recombination cannot be maintained; the
preferred route is to form (33.6) before localization.

After global endpoint removal, the remaining exact analytic survivor is
the endpoint-free, connector-completed masked axial vector: the terminal,
radial-side, and arithmetic \(v=0\) shares; both finite \(v\)-horizontals;
the mask area connector; its \(u=0\) and mixed \(\psi''\) strata; the
top \(u=0\) share; and the joint corner once. It must be reconciled before
the local polar subtraction \((b+i\nu)^{-1}\) can define the actual
axial-subtracted terminal symbol.

## Evidence assessment

- The blind report independently derives the masked endpoint and axial
  Cauchy--Green signs, the one-count residue ledger, and local
  \({\cal E}_{\rm own}=0\). Its addendum correctly isolates
  \(D_\xi^\beta\).
- The discovery report gives the same corrected two-order architecture,
  explicit physical normalization, and smallest endpoint/axial survivors.
- The hostile audit supplies the decisive falsifier: beta-internal
  recombination is not unmasked endpoint recombination, and omitting
  (33.4) changes the finite operator. It also exposes the mixed
  \(\psi''/4\) connector under a second axis shift.
- The conductor independently checked the three-mask derivative
  cancellation, boundary-first order, one-axis connector sign, and
  two-axis corner conventions.

Promotion is scoped to finite algebra, not to endpoint or axial estimates.

## State effect

- promote the finite masked endpoint Cauchy--Green identity and its signs;
- promote the exact three-mask endpoint recombination required before the
  existing unmasked endpoint theorem is invoked;
- promote conditional same-ownership \({\cal E}_{\rm own}=0\), its
  all-order rho cancellation, and its physical \(L\)-derivative;
- promote the finite one-axis mask-connector identity and the requirement
  to carry connector-axis, mixed-connector, and one-corner strata;
- revise and retain open the full mask--endpoint--axial compatibility
  obligation, because the connector-completed axial vector is unestimated;
- reject applying the unmasked endpoint theorem to \(D_\xi^\beta\),
  deleting the mask area connector, or replacing the vector axial operation
  by a scalar local polar subtraction;
- retain the axial-subtracted terminal symbol bound, complete beta
  transition, alpha branch, double-bounded share, M9-M1, M9-M2, M9, and
  the Gauss-circle target as open.
