# Blind post-unmask cross-gcd consistency review

- Campaign: `m9-m1-t1-p2-cross-gcd-cellular-boundary-gate`
- Round: 199
- Role: independent blind post-unmask reviewer
- Numerical theorem evidence: none

## 1. Result

The complete-allocation $B$--$E$--$C$ triangle, its literal
character holonomy, and its missing-product-corner residual are exact.
The triangle is genuinely $P_2$-preserving and is not the distinct
partial-block construction whose masks fail to commute.

One advertised owner is not exact.  The fourth corner has recomputed gcd
$Aq$, but the candidate proves at most its lower-far inequality (and
even that uses a live-shell lower bound not stated in the blind packet).
Membership in the two-far mask $P_1$ also requires

\[
 Aq|y-v|>D_L,
\]

and neither the candidate nor the reconciliation proves this.  It does
not follow from the common triangle condition
$A|qy-v|>D_L$.  Thus the formal candidate requires repair.  The
mechanism-scoped no-go itself survives the repair because the corner's
changed gcd $Aq\ne A$ is exact and an unpriced changed-gcd allocation is
independently declared unsafe by the frozen mechanism.

## 2. Blind derivation before unmasking

Using only `protocol.md` and `blind_statement.md`, decompose a squarefree
source as

\[
 d=ACx,\qquad m=BEu,\qquad d'=ABy,\qquad m'=CEv,
\]

where $A=G_{00}$, $B=G_{10}$, $C=G_{01}$, $E=G_{11}$, and the
displayed factors are pairwise coprime.  At current gcd $A$, the two
defects are

\[
 A|Cx-BEu|\le D_L,\qquad A|By-CEv|>D_L.
\]

A whole lower, upper, or simultaneous allocation reversal retains gcd
$A$ precisely on $B=1$, $C=1$, or $E=1$, respectively.  If one
odd block $q>1$ is placed successively in $B,E,C$, the three whole
allocations are

\[
 (Ax,qu,Aqy,v),\qquad (Ax,qu,Av,qy),\qquad
 (Aqu,x,Av,qy).
\]

At every vertex the recomputed gcd is $A$, and both defect magnitudes
are exactly

\[
 A|x-qu|,\qquad A|qy-v|.
\]

Hence this three-cycle preserves $P_2$ without transporting its mask.
If

\[
 p=\chi_4(qxu),\qquad t=\chi_4(qyv),
\]

the actual edge quotients are $t,p,tp$; their product is $1$.  Thus a
pair of negative ordinary edges forces a positive simultaneous edge.

This whole-allocation cycle must be kept separate from moving only a
cross block $\kappa$ while holding the other allocation factors fixed.
For

\[
 (g\kappa a,hb,gc,\kappa he),
\]

the three projected masks contain, in succession,

\[
\begin{aligned}
 &g|\kappa a-hb|,\quad g|c-\kappa he|,\\
 &g|a-\kappa hb|,\quad g|c-\kappa he|,\\
 &g|a-\kappa hb|,\quad g|\kappa c-he|.
\end{aligned}
\]

They are not a common $P_2$ event.  Their differences are literal
transported-mask commutators, so this partial-block construction cannot
be substituted for the whole-allocation triangle.

## 3. Post-unmask allocation and incidence audit

The factorization and all three maps in (199.K8) are product-preserving
involutions on their stated domains.  Direct gcd recomputation gives
$A$ on those domains and $AB,AC,AE$ when the corresponding unit-state
hypothesis is removed.  Equations (199.K9)--(199.K11) therefore pass the
$P_2$-preservation check.

Let

\[
 \ell_0=\lambda_N(Ax),\quad \ell_1=\lambda_N(Aqu),\quad
 u_0=\lambda_{N+r}(Aqy),\quad u_1=\lambda_{N+r}(Av).
\]

After extracting the actual character and phase at the $B$-vertex,
the three contributions are exactly

\[
 \Sigma_{BEC}
 =u_0\overline{\ell_0}
 +t u_1\overline{\ell_0}
 +tp u_1\overline{\ell_1}.
\]

The unique fourth endpoint product is the allocation

\[
 V_A=(Aqu,x,Aqy,v),\qquad (Aqu,Aqy)=Aq,
\]

and its relative character is $p$.  Expansion gives

\[
 \Sigma_{BEC}
 =(u_0+t u_1)\overline{(\ell_0+p\ell_1)}
 -p u_0\overline{\ell_1}.
\]

Consequently, on $p=-1$, deleting $V_A$ leaves
$u_0\overline{\ell_1}$ with relative coefficient $+1$.  In the
unfactored physical expression this residual is multiplied by the common
character and $\Phi_{r,\sigma}(N)$; no sign or conjugation is missing.
The endpoint/character residual in (199.K17)--(199.K18) is therefore
exact.

The candidate also correctly keeps the partial-block commutators
(199.K21)--(199.K22) separate from this calculation.  It does not use
them to claim that the whole triangle preserves $P_2$.

## 4. First doubtful step: the asserted \(P_1\) owner

At $V_A$, the recomputed defects are both required:

\[
 \Delta_L(V_A)=Aq|u-x|,
 \qquad
 \Delta_U(V_A)=Aq|y-v|.
\]

Equation (199.K19) computes only $\Delta_L(V_A)$.  Even if the invoked
live-shell lower bound is supplied and proves
$\Delta_L(V_A)>D_L$, the original upper condition
$A|qy-v|>D_L$ does not imply
$\Delta_U(V_A)>D_L$.

An exact arithmetic control shows the distinction on the aligned
character-reversing sector.  Take

\[
\begin{gathered}
 A=1,\quad q=3,\quad L=10^6,\quad D_L=1000,\\
 u=253978973,\quad x=761936821,\\
 y=439904455,\quad v=439904459.
\end{gathered}
\]

The five nonunit factors are odd, squarefree, and pairwise coprime:

\[
 \begin{aligned}
 u&=2131\cdot119183,\\
 x&=17\cdot3691\cdot12143,\\
 y&=5\cdot4327\cdot20333,
 \end{aligned}
\]

while $q$ and $v$ are prime.  Moreover

\[
 yv-ux=12,\qquad r=q(yv-ux)=36<L,\qquad 2\mid r,
\]

and $q<D_L$.  The common triangle satisfies

\[
 |x-qu|=98\le1000,\qquad
 |qy-v|=879808906>1000,
\]

with
\(\chi_4(qxu)=\chi_4(qyv)=-1\).  At the fourth corner, however,

\[
 q|u-x|=1523873544>1000,\qquad
 q|y-v|=12\le1000.
\]

Thus the corner is lower-far but upper-close, not two-far $P_1$.  This
finite exact control is used only to falsify the claimed mask implication;
it asserts no literal endpoint nonvanishing, density, lower mass, or
failure of the target estimate.

## 5. Controls and outcomes

1. **Whole-swap gcd and inverse control:** pass.  Every map in (199.K8)
   has the displayed inverse and recomputed gcd.
2. **Whole-triangle \(P_2\) control:** pass.  The two absolute defects are
   identical at all three vertices.
3. **Actual character control:** pass.  The quotients are \(t,p,tp\), so
   the simultaneous sign is not assigned falsely.
4. **Endpoint and conjugation control:** pass.  The missing atom and its
   relative coefficient are exactly those in (199.K17)--(199.K18).
5. **Partial-block/common-event control:** pass.  The candidate records
   the three unequal masks and does not conflate that construction with
   the lawful triangle.
6. **Fourth-corner owner control:** fail as written.  Gcd \(Aq\) is exact;
   two-far \(P_1\) membership is not.
7. **Scope and power control:** pass after the owner repair.  The report
   uses capacities only as upper capacities, takes no premature positive
   norm, claims no nonemptiness or nonvanishing, and restricts the result
   to the frozen cellular-boundary mechanism.

## 6. Exact repairs and state recommendation

1. In candidate Sections 1 and 4 and reconciliation Sections 5 and 6,
   replace “the fourth corner lies in \(P_1\)” by: “the fourth corner has
   recomputed gcd \(Aq\ne A\); its upper near/far status is not fixed by
   the triangle, so it is an unpriced changed-gcd boundary.”
2. Display the missing recomputed upper defect
   \(Aq|y-v|\) next to (199.K19)/(199.R14).  Do not infer it is \(>D_L\)
   from \(A|qy-v|>D_L\).
3. Either remove the lower-far asymptotic assertion as unnecessary, or
   state and cite an exact licensed live-shell inequality sufficient for
   \(Aq|u-x|>D_L\).  The blind packet alone does not state the invoked
   \(qu\gg L\) hypothesis.
4. Base the unsafe-corner conclusion on the frozen changed-gcd gate,
   which already suffices.  Retain the coefficient-one residual and the
   mechanism-scoped conclusion unchanged.  Do not promote a \(P_2\),
   \(P_1\), parent, endpoint, bridge, global, or exponent claim.

Recommended state effect: **revise** the formal candidate and
reconciliation, then retain the corrected result only as a durable
mechanism-scoped route boundary.

## 7. Dependencies

The blind phase used only `protocol.md` and
`rounds/codex-managed/m9-m1-t1-p2-cross-gcd-cellular-boundary-gate/blind_statement.md`.
The post-unmask audit then used only
`candidates/formalized_hard_m1_t1_p2_cross_gcd_cellular_boundary_self_return.md`
and `reviews/conductor_round199_report_reconciliation.md` in the same
campaign.  No sibling report, proof graph, strategy file, source card,
control artifact, kernel, or synthesis was read.

REPAIR
