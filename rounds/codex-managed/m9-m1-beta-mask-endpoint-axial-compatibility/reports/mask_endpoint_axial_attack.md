# Round 33 discovery report: mask, endpoint, and axial compatibility

## 1. Result

The beta-internal recombination is **not** an unmasked endpoint
recombination. It gives the hierarchical beta mask
\(\Theta_\beta=\psi(\beta)\), hence the endpoint collapse produces the
masked prefixes \(D_{\xi}^{\beta}=D_\xi[\psi(\beta)]\), not the proved
unmasked prefixes \(D_\xi\). Only the \(A=0\) arithmetic residue is already
full inside the beta branch, because there \(\beta=0\) and
\(\psi(0)=1\).

There is nevertheless no intrinsic rho defect. At finite \(U,V,S\), beta
masking, Cauchy--Green displacement, endpoint collapse, and finite
\(v\)-axis displacement commute after their area connectors, horizontal
connectors, residue strata, and mixed corners are retained. For a common
finite operator \({\cal H}_{\rm com}\) which either retains
\(D_\xi^\beta\) explicitly, or first recombines all three global masks
before removing the unmasked endpoint modules,
\[
\boxed{
 {\cal E}_{\rm own}
 ={\cal H}_{\rm com}[G]-{\cal H}_{\rm com}[E_1]
  -{\cal H}_{\rm com}[R_1]
 ={\cal H}_{\rm com}[G-E_1-R_1]=0 .
}
\tag{33.1}
\]
The equality is meromorphic in \(\rho\), so every rho Laurent/Taylor
coefficient vanishes. On every affine physical-height cell,
\[
 \partial_L{\cal E}_{\rm own}=0,
\tag{33.2}
\]
and the equality also holds distributionally across the common switches.

The exact global masks are
\[
 \Theta_\beta=\psi(\beta),\qquad
 \Theta_\alpha=(1-\psi(\beta))\psi(\alpha),\qquad
 \Theta_{\rm out}=(1-\psi(\beta))(1-\psi(\alpha)),
\tag{33.2a}
\]
and sum to one. Therefore
\[
 D_\xi^\beta+D_\xi^\alpha+D_\xi^{\rm out}=D_\xi.
\tag{33.2b}
\]
This three-branch recombination, including all three connector ledgers, is
required before the proved unmasked endpoint estimates can be invoked.
The beta-internal split alone suffices only for the full \(A=0\)
arithmetic residue.

Thus the smallest beta-only boundary survivor is
\[
 {\cal D}_{\rm end}^{\beta}
 =-\frac4\pi X^{1/4}\Re\!\left\{
 e(1/8)\sum_{\xi\in\{1,N_X\}}D_\xi^\beta\right\}.
\tag{33.2c}
\]
It is generally nonzero and has no proved estimate from the unmasked
endpoint modules. After its global reconciliation, the next survivor is
the full finite \(v=0\) vector residue and its connector-completed axial
operator. Equation (33.1) is only an ownership identity; it estimates
neither survivor.

## 2. Exact statement and hypotheses

Put
\[
 A=s-\frac{u+v}{2}=\sigma_A+i\beta,\qquad
 B=s+\frac{u+v}{2},
\tag{33.3}
\]
and work on the accepted finite \(u,v,A\) rectangles. Assume that no
genuine pole lies on a boundary; a collision of the arithmetic and
artificial poles is interpreted as its single derivative residue. All
Mellin profiles, \(H_j+1\) floors, endpoint stars, scale factors, and
coefficient factors remain inside the finite meromorphic integrand.

Let \(\psi\) be the accepted compact beta cutoff and define
\[
 \Theta_{\rm db}=\psi(\beta)\psi(\alpha),\qquad
 \Theta_{\rm ah}=\psi(\beta)\{1-\psi(\alpha)\},
 \qquad \alpha=\beta+\Im(u+v).
\tag{33.4}
\]
Then
\[
 \Theta_{\rm db}+\Theta_{\rm ah}=\Theta_\beta=\psi(\beta),
\tag{33.5}
\]
and
\[
 \partial_\beta\Theta_{\rm db}
 =\psi'(\beta)\psi(\alpha)+\psi(\beta)\psi'(\alpha),
\]
\[
 \partial_\beta\Theta_{\rm ah}
 =\psi'(\beta)\{1-\psi(\alpha)\}-\psi(\beta)\psi'(\alpha).
\tag{33.6}
\]
Thus the internal \(\psi'(\alpha)\) connectors cancel and the sum has the
single connector \(\psi'(\beta)\).

For a complete finite \(A\)-integrand \(F\), let \(V_x^\Theta[F]\) denote
an upward vertical and let \(H_\pm^\Theta[F]\) denote the two horizontals
in left-to-right orientation. Define the beta area connector
\[
 C_A^\Theta[F]=-\iint_{R_A}
 \partial_\beta\Theta(\beta)\,F(A)\,d\sigma_A\,d\beta .
\tag{33.7}
\]
Positive rectangle orientation gives the exact identity
\[
 V_{x_0}^\Theta[F]
 =V_{x_1}^\Theta[F]+H_+^\Theta[F]-H_-^\Theta[F]
 +2\pi i\sum_{p\in R_A^\circ}\Theta(\Im p)\Res_{A=p}F
 +C_A^\Theta[F].
\tag{33.8}
\]

For each radial endpoint \(\xi\in\{1,N_X\}\), use the accepted
orientation and notation
\[
 T_{\xi,\Theta},\quad S_{\xi,\Theta},\quad
 P_{\xi,\Theta},\quad D_{\xi,\Theta},\quad A_{\xi,\Theta}.
\]
Here \(S_\xi\) is upper left-to-right minus lower left-to-right,
\(P_\xi\) is the artificial-pole residue, and \(A_\xi\) is the
arithmetic-pole share with the convention of the accepted endpoint
identity. The masked form of that identity is
\[
\boxed{
 T_{\xi,\Theta}+S_{\xi,\Theta}+P_{\xi,\Theta}
 +C_{A,\xi}^{\Theta}
 =D_{\xi,\Theta}-A_{\xi,\Theta}.
}
\tag{33.9}
\]
At \(\Theta=1\), the connector vanishes and (33.9) is exactly
\(T_\xi+S_\xi+P_\xi=D_\xi-A_\xi\).

For the finite \(v\)-displacement, first retain \(s,u\) as independent
coordinates. Then
\[
 \beta=\Im s-\frac{\Im u+\Im v}{2},
\qquad \partial_{\Im v}\Theta_\beta=-\frac12\psi'(\beta).
\tag{33.10}
\]
Let \(J_b^\Theta[F]\) be the upward \(v\)-vertical on \(\Re v=b>0\), and
let \(b_-<0\). With \(Q_{v,\pm}\) oriented left-to-right, define
\[
 C_v^\Theta[F]
 =2i\iint_{R_v}\bar\partial_v\Theta_\beta\,F\,dA_v
 =\frac12\iint_{R_v}\psi'(\beta)F\,dA_v .
\tag{33.11}
\]
The finite displacement is
\[
\boxed{
 J_b^\Theta[F]
 =J_{b_-}^\Theta[F]+Q_{v,+}^\Theta[F]-Q_{v,-}^\Theta[F]
 +2\pi i\,\Res_{v=0}\{\Theta F\}
 +C_v^\Theta[F].
}
\tag{33.12}
\]
If the change of variables \((s,v)\mapsto(A,v)\) is made first, the mask is
independent of \(v\); then (33.11) is replaced by the corresponding
sheared \(A\)-face and corner terms. These are the same formula under
change of variables and cannot both be discarded.

The analogous \(u\)-displacement has
\[
 C_u^\Theta[F]=\frac12\iint_{R_u}\psi'(\beta)F\,dA_u
\tag{33.13}
\]
at fixed \(s,v\). Writing \(\Delta_v\) and \(\Delta_u\) for, respectively,
horizontal-difference plus area-connector plus \(2\pi i\) residue in
(33.12) and its \(u\)-analogue, the full two-axis ledger is
\[
 (1+\Delta_u)(1+\Delta_v)
 =1+\Delta_u+\Delta_v+\Delta_u\Delta_v.
\tag{33.14}
\]
The mixed term contains
\[
 (2\pi i)^2\Res_{u=0}\Res_{v=0}F
\tag{33.15}
\]
exactly once, together with the induced endpoints of the finite
horizontal and area connectors.

The theorem is that (33.8)--(33.15), applied with identical finite
rectangles, masks, endpoint conventions, and residue ownership to
\(G,E_1,R_1\), imply (33.1)--(33.2).

## 3. Proof or derivation

### 3.1 Mask and Cauchy--Green signs

For positive orientation, the \(A\)-boundary is
\[
 V_{x_0}-V_{x_1}-H_++H_-.
\]
Away from the excised poles,
\[
 2i\bar\partial_A\Theta_\beta
 =-\partial_\beta\Theta_\beta.
\]
Cauchy--Green therefore gives (33.8), including the minus sign in
(33.7). Applying it to the endpoint factor \(E_{\xi,v}\), and using the
accepted residue conventions, gives
\[
 D_{\xi,\Theta}
 =T_{\xi,\Theta}+S_{\xi,\Theta}
  +P_{\xi,\Theta}+A_{\xi,\Theta}
  +C_{A,\xi}^{\Theta},
\]
which is equivalent to (33.9). Thus the beta area connector belongs with
the terminal/side endpoint operator when it is collapsed back to the
right-line endpoint.

Equations (33.5)--(33.6) show that the two **internal beta shares** add
only to \(\Theta_\beta=\psi(\beta)\). At the arithmetic pole \(A=0\),
\(\beta=0\) and \(\psi(0)=1\). The two internal residue weights are
\[
 \psi(\Im(u+v)),\qquad 1-\psi(\Im(u+v)),
\tag{33.16}
\]
so they sum to the full residue. Their \(\psi'(\alpha)\) connectors also
cancel. This fullness is special to the arithmetic pole. At an endpoint
prefix, \(\beta\) is integrated and \(\psi(\beta)\) is not identically
one; consequently the same internal sum gives \(D_\xi^\beta\), not
\(D_\xi\). In contrast, the isolated disjoint share has only the second
weight in (33.16), and even its arithmetic full-residue replacement would
be false.

### 3.2 Endpoint, artificial, and arithmetic recombination

The identity \(G=E_1+R_1\) holds meromorphically before masking. Because
the same mask multiplies all three terms, the opposite artificial
\(\rho=0\) residues satisfy
\[
 P_{\Theta}[E_1]+P_{\Theta}[R_1]=0.
\tag{33.17}
\]
This remains true when the pole lies on any terminal, connector, or axial
stratum, because the weight and orientation are identical. At a collision
with the arithmetic pole, (33.17) is read inside the one combined
derivative residue rather than as two simple residues.

At the arithmetic pole, linearity gives
\[
 R_{\Theta}^{\rm ar}[G]-\sum_{\xi}A_{\xi,\Theta}
 =R_{\Theta}^{\rm ar}[R_1].
\tag{33.18}
\]
After the complementary shares (33.16) are added, (33.18) is the full
unmasked recombined \(R_1\) residue. Only at that point may the accepted
physical arithmetic-residue module be invoked.

For endpoints, the exact conclusion is instead
\[
 D_{\xi,{\rm db}}+D_{\xi,{\rm ah}}
 =D_\xi^\beta:=D_\xi[\psi(\beta)].
\tag{33.18a}
\]
Introduce the other two global branches from (33.2a). Linearity of the
right-line endpoint functional and
\(\Theta_\beta+\Theta_\alpha+\Theta_{\rm out}=1\) give
\[
 \boxed{
 D_\xi^\beta+D_\xi^\alpha+D_\xi^{\rm out}=D_\xi.
 }
\tag{33.18b}
\]
Moreover, differentiating the three masks shows that their complete
Cauchy--Green area connectors sum to zero. Hence the proved unmasked
endpoint modules, with their original profiles, floors, and stars, may be
invoked only after (33.18b). The selected beta branch does not contain the
two complementary endpoint prefixes, so \(D_\xi^\beta\) remains explicit
in a beta-only collapse.

### 3.3 Axial displacement and one-count corners

The same positive-rectangle calculation in the \(v\)-plane yields
(33.12). The sign in (33.11) follows from
\[
 2i\bar\partial_v\Theta_\beta
 =-\partial_{\Im v}\Theta_\beta
 =\frac12\psi'(\beta).
\tag{33.19}
\]
Consequently the \(v=0\) residue cannot be taken only on the terminal
vertical. Apply \(\Res_{v=0}\), and separately each horizontal and area
connector operation, to (33.9). Linearity gives
\[
\begin{aligned}
 &R_v(T_{\xi,\Theta})+R_v(S_{\xi,\Theta})
  +R_v(P_{\xi,\Theta})+R_v(C_{A,\xi}^{\Theta})\\
 &\hspace{35mm}
 =R_v(D_{\xi,\Theta})-R_v(A_{\xi,\Theta}).
\end{aligned}
\tag{33.20}
\]
Thus the terminal, radial-side, artificial, right-endpoint, and
arithmetic axial shares are the strata of one vector identity. The same
equation holds with \(R_v\) replaced by either
\(Q_{v,+}-Q_{v,-}\) or \(C_v\). This proves that both finite
\(v\)-horizontals and the mask connector are owned once, not discarded.

If the \(u\)-line is then displaced, apply (33.14). The \(v=0\) residue
is first left on the unshifted \(u\)-line; shifting that line contributes
the joint residue (33.15). The separate \(u=0\) residue is evaluated on
the already shifted \(v\)-line. Hence the corner occurs once rather than
once in each axial residue. Reversing the order gives the same result,
because the mixed boundary and connector terms in \(\Delta_u\Delta_v\)
are retained. This is the finite Stokes/Fubini commuting diagram.

### 3.4 Conditional vanishing of the ownership defect

There are two legitimate common operators.

The beta-retained operator \({\cal H}_\beta^{\rm ret}\) sums the two
internal beta shares, applies (33.8)--(33.14), and retains
\(D_\xi^\beta\), its axial images, and all other masked boundary strata
explicitly. It does not invoke the unmasked endpoint theorem.

The globally collapsed operator \({\cal H}_{\rm glob}^{\rm free}\) first
performs the same finite operations on all three masks in (33.2a), then
uses (33.18b), and only then routes the resulting unmasked \(D_\xi\) to
the accepted endpoint modules. It retains every horizontal, axial, and
corner stratum until the same global recombination has been made.

For either common operator, every step is linear and is applied with
identical ownership. Therefore
\[
 {\cal H}_{\rm com}[G]-{\cal H}_{\rm com}[E_1]
 -{\cal H}_{\rm com}[R_1]
 ={\cal H}_{\rm com}[G-E_1-R_1]=0.
\tag{33.21}
\]
This proves (33.1) for \({\cal H}_\beta^{\rm ret}\) and for
\({\cal H}_{\rm glob}^{\rm free}\). It does **not** prove (33.1) for a
hybrid operator that deletes \(D_\xi^\beta\) by citing the unmasked
endpoint estimate. Such an operator has changed ownership and is not
common.

Under either legitimate order, every rho coefficient vanishes, not merely
the constant term. Since (33.21) is an identity of exact finite
physical-height functions, differentiating at fixed physical \(\nu\)
gives (33.2). Common moving endpoints contribute identical trace terms and
cancel; at cell switches the equality remains valid as a distribution.

## 4. First doubtful or unproved step

The first exact beta-only survivor is the masked endpoint prefix
\({\cal D}_{\rm end}^{\beta}\) in (33.2c). Algebraically,
\[
 D_\xi^\beta-D_\xi
 =-D_\xi^\alpha-D_\xi^{\rm out},
\tag{33.21a}
\]
and none of the two terms on the right belongs to the beta-only operator.
The selected artifacts give no identity setting this difference to zero
and no estimate transferring the proved unmasked endpoint bound to
\(D_\xi^\beta\). This is a genuine ownership operator, not a rho
singularity.

After the exact three-branch reconciliation (33.18b), the next unproved
object is the nonzero connector-completed axial vector operator
\[
\boxed{
 {\cal V}_{\rm ax}^{\beta}
 =
 2\pi i\,R_v^{\rm term}
 +2\pi i\,R_v^{\rm side}
 +2\pi i\,R_v^{\rm ar}
 +(Q_{v,+}-Q_{v,-})
 +C_v
 +2\pi i\,R_u
 +(2\pi i)^2R_{uv},
}
\tag{33.22}
\]
where each symbol denotes the corresponding globally recombined and
endpoint-collapsed vector stratum, not a scalar local polar subtraction.
Beta-masked endpoint axial terms are not removed separately; they reach
the proved endpoint modules only through (33.18b). The remaining axial
vector is paired with the globally endpoint-image-free terminal operator.

The selected artifacts do not prove a target-size estimate for
(33.22), nor the weighted
\(\lambda^{-2}/\lambda^{-3}\) symbol estimate for the resulting
axial-subtracted terminal kernel. They also do not license applying the
physical endpoint and arithmetic estimates at arbitrary finite top Mellin
height: those estimates begin only after their accepted physical-profile
limits. Thus the finite algebra identifies the exact global commuting
order, but the beta-only endpoint ownership, axial estimation, and height
exhaustion remain open.

## 5. Required control tests and outcomes

### Hierarchical versus disjoint mask

**Partial pass; the original endpoint claim fails.** Equations
(33.5)--(33.6) give one beta connector and the full arithmetic residue
after the double-bounded and alpha-high shares are added. They give only
\(D_\xi^\beta\) at the endpoints. The full endpoint requires all three
global masks in (33.18b). An isolated disjoint share has two edges and a
filtered arithmetic residue, so neither an unmasked endpoint nor an
unmasked residue bound can be applied to it.

### Cauchy--Green orientation

**Pass.** Upward verticals and left-to-right horizontals give
\(V_R-V_L-H_++H_-\) on the positively oriented boundary. Hence the
horizontal ledger is \(H_+-H_-\), the beta area term is
\(-\iint\psi'F\), and the fixed-\(s,u\) \(v\)-mask connector has the
opposite displayed sign \(+\frac12\iint\psi'F\).

### Endpoint, artificial, and arithmetic ledger

**Pass for the exact finite ledger; endpoint closure remains
conditional.** The masked identity is (33.9). The \(E_1/R_1\) artificial
residues cancel with the same mask; the arithmetic pieces recombine as
(33.18). A pole collision uses one derivative residue. The beta endpoint
is \(D_\xi^\beta\) and cannot be replaced by \(D_\xi\) before
(33.18b).

### Axial residue and corner count

**Pass algebraically.** Equation (33.20) takes the \(v=0\) residue on
every contour stratum. Formula (33.14) assigns the \(u=0\) share and the
joint \(u=v=0\) residue once. It does not assert that their sum is small.

### Finite-height connector ownership

**Pass.** Both \(v\)-horizontals occur as
\(Q_{v,+}-Q_{v,-}\). The beta mask area connector (33.11), and the
induced mixed connector boundaries in (33.14), are retained. No
\(U,V,S\) limit is taken in this report.

### Rho ownership defect

**Pass only under common ownership.** Equation (33.21) proves
\({\cal E}_{\rm own}=0\), all of its rho Laurent/Taylor coefficients are
zero, and its physical \(L\) derivative is zero for the beta-retained
operator or the globally collapsed operator. It does not apply to the
hybrid operation that discards \(D_\xi^\beta\) using an unmasked theorem.

### Profiles, stars, and normalization

**Pass algebraically.** Every profile, \(H_j+1\) floor, \(q\)-character,
top equality star, and height endpoint convention remains inside the same
finite integrand on all sides of the identities. Endpoint
integration-by-parts coefficients retain full weight; the half-star
belongs only to symmetric physical inversion. The external factor
\[
 -\frac4\pi X^{1/4}
 \Re\{e(1/8)(\cdots)\}
\tag{33.23}
\]
is applied once after all strata are recombined. No local \(q\)-power or
terminal symbol estimate is inferred from the ownership algebra.

### One-count ledger

| Object | Exact owner | Count |
|---|---|---:|
| hierarchical beta connector | sum of (33.6) | one |
| internal alpha connectors | opposite signs in (33.6) | zero after recombination |
| \(A=0\) arithmetic residue | complementary weights (33.16) | one full share |
| artificial \(\rho=0\) residue | \(E_1+R_1\) pair | zero after cancellation |
| \(D_1^\beta,D_{N_X}^\beta\) | beta right-line prefixes after (33.9) | one each; remain open |
| full \(D_1,D_{N_X}\) | three-branch sum (33.18b) | one each only globally |
| recombined \(R_1\) arithmetic residue | (33.18) | one |
| terminal/side/arithmetic \(v=0\) shares | vector equation (33.20) | one each |
| \(v\)-horizontals | \(Q_{v,+}-Q_{v,-}\) | one oriented pair |
| \(v\)-mask area connector | (33.11) | one |
| \(u=0\) share | \(\Delta_u\) in (33.14) | one |
| \(u=v=0\) corner | \(\Delta_u\Delta_v\) | one |
| external \(X^{1/4}\) normalization | after recombination | one |

## 6. Dependencies and exact artifacts used

The work was entirely analytical. No numerical experiment, computer
algebra, web source, or external theorem was used. The exact selected
artifacts were:

1. protocol.md;
2. state/proof_obligations.yml, graph SHA-256
   62d2197f75b5d0ca1a8c2c320573c678328e8d36bbdad8dba5c997d0c97a2d29;
3. state/active_campaign.yml;
4. rounds/codex-managed/m9-m1-vector-hankel-kernel/synthesis.md;
5. rounds/codex-managed/m9-m1-endpoint-boundary-cauchy/synthesis.md;
6. rounds/codex-managed/m9-m1-beta-transition-connector/reports/blind_beta_connector_identity.md;
7. rounds/codex-managed/m9-m1-beta-transition-connector/synthesis.md;
8. rounds/codex-managed/m9-m1-r1-arithmetic-residue/synthesis.md;
9. rounds/codex-managed/m9-m1-beta-complete-physical-height-symbol/reviews/conductor_endpoint_ownership_map.md;
10. rounds/codex-managed/m9-m1-beta-complete-physical-height-symbol/reviews/conductor_axial_vector_ownership.md;
11. rounds/codex-managed/m9-m1-beta-complete-physical-height-symbol/synthesis.md;
12. the Round-33 task brief.

The imported facts are the finite vector kernel, the unmasked endpoint
identity, the hierarchical beta convention, the artificial/arithmetic
recombination, the physical scope of the proved endpoint and \(R_1\)
residue modules, and the boundary-first architecture. The masked endpoint
formula (33.9), the fixed-coordinate \(v\)-connector sign, the commuting
residue identity (33.20), the global endpoint requirement (33.18b), and
the conditional zero-defect conclusion are derived here.

## 7. Recommended state effect

**Promote, after the required independent audits,** only the following
scoped finite identities:

1. promote the masked endpoint identity (33.9);
2. promote that beta-internal recombination gives the full arithmetic
   residue but only the masked endpoint \(D_\xi^\beta\);
3. promote the vector axial one-count identity (33.20) and the
   \(u,v\)-corner convention (33.14)--(33.15);
4. promote the exact three-branch endpoint recombination (33.18b);
5. promote \({\cal E}_{\rm own}=0\), all-order rho coefficient
   cancellation, and \(\partial_L{\cal E}_{\rm own}=0\) only for the
   beta-retained or globally boundary-collapsed common operator.

**Retain open first** the masked endpoint prefix
\({\cal D}_{\rm end}^{\beta}\), or equivalently the completion of its
ownership by the alpha and outer branches. Then retain open the size of
the connector-completed axial vector (33.22), the axial-subtracted terminal
\(\lambda^{-2}/\lambda^{-3}\) symbol bound, finite-height connector
estimates, joint exhaustion, complete beta sums, and the double-bounded
share.

**Reject** the original claim that the two beta-internal shares return the
unmasked \(D_1,D_{N_X}\) modules. Also reject applying an unmasked endpoint
or arithmetic theorem to one filtered disjoint share, dropping the mask
area connector during \(v\)-displacement, counting the joint corner in
both axial residues, or replacing the vector \(v=0\) operation by the
local scalar subtraction \((b+i\nu)^{-1}\).
