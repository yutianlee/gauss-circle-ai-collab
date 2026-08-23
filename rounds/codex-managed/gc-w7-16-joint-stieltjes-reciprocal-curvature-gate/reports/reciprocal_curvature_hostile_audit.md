# Round 129 hostile review: the norm-relative Stieltjes curvature inequality fails at a reciprocal stationary alias

Campaign: `gc-w7-16-joint-stieltjes-reciprocal-curvature-gate`
Task: `reciprocal_curvature_hostile_audit`
Role: hostile seam reviewer
Starting graph SHA-256:
`476b1445ef73d86627fd87de8bd2dd76a5efa53564a5b195230f2ad33ba2bbe8`

Status: candidate evidence only.  No shared proof state is changed.

## 1. Result: an exact dual obstruction, with a strict surviving single-threshold theorem

The displayed norm-relative inequality is **false under its displayed
Stieltjes hypotheses**.  The failure already occurs on the top reduced
shell, on the legal progression \(\rho=1\), in a one-lift interior packet.
At an exact integer first-derivative alias, a bounded-variation Stieltjes
profile can follow the conjugate reciprocal chirp on its natural coherent
length.  Its two \(V^2\) endpoint values are zero, and yet

\[
 \frac{\left|\sum_{v\in I}U(v)e(f(v))\right|}
      {\|U\|_{V^2(I)}}
 \gg \mu^{-3/4},
 \qquad \mu:=|f''(v_0)|\asymp Y^{-1/3}.
 \tag{129.H1}
\]

On that shell

\[
 N\asymp Q_B=Y^{19/48},\qquad
 F:=N\sqrt\mu+\mu^{-1/2}\asymp Y^{11/48},
 \tag{129.H2}
\]

whereas \(\mu^{-3/4}=Y^{1/4}=Y^{12/48}\).  Thus the proposed
right side is too small by \(Y^{1/48}\), and it fails for every fixed
\(\varepsilon<1/48\).  The same construction works for M2 and for either
M1 quarter branch: the quarter term merely changes the alias equation from
\(c a'/(\kappa v_0^2)\in\mathbb Z\) to
\(c a'/(\kappa v_0^2)\pm1/4\in\mathbb Z\).

This is not merely a generic sequence outside the displayed threshold
class.  On the one-lift packet, every compactly supported sampled-BV
sequence is an exact Stieltjes superposition
\(w(v)=\sum_{t\ge v}c_t\), and homogeneous rescaling enforces
\(\sum_t|c_t|\ll1\) without changing the ratio in (129.H1).

There is an important scope restriction.  The constructed denominator
profile is phase-adapted.  It is allowed by the hypotheses
\(\sum|c_t|\ll1\), but the selected context does not show that it is one
of the fixed physical smooth/hard M1/M2 profiles.  Consequently this
review refutes the proposed theorem as stated and any proof based only on
the Stieltjes mass and \(V^2\) norm; it does **not** prove a lower bound for
the narrower fixed physical family.

A strict positive result survives.  Every **single threshold** satisfies
the required reciprocal-curvature bound.  Indeed its birth plateaux may
be estimated separately by the second-derivative test, and the sum of the
plateau endpoint terms is absorbed by the main curvature term.  Minkowski
therefore gives the lawful absolute estimate

\[
 \left|\sum_{v\in I}^{*}U(v)e(f(v))\right|
 \ll_\varepsilon {Y^\varepsilon\over L}
 \min\!\left(N,N\sqrt{\lambda_B\rho^2}
                 +(\lambda_B\rho^2)^{-1/2}\right).
 \tag{129.H3}
\]

Estimate (129.H3) does not imply the claimed norm-relative estimate:
the alias construction has \(\|U\|_{V^2}\ll L^{-1}\mu^{1/4}\).
Under the round's stop rule, the norm-relative graded continuation is not
certified.

## 2. Exact statements and hypotheses

### 2.1 Exact discrete dual norm

Let \(I=\{1,\ldots,N\}\), after translating the physical interval, and
put

\[
 \|u\|_{V^2(I)}^2
 =|u_1|^2+\sum_{j=1}^{N-1}|u_{j+1}-u_j|^2+|u_N|^2.
 \tag{129.H4}
\]

Let \(D_Nu=(u_1,u_2-u_1,\ldots,u_N-u_{N-1},u_N)\).  Then
\(L_N=D_N^*D_N\) is the Dirichlet path Laplacian with diagonal \(2\)
and adjacent entries \(-1\).  Its inverse is the exact Green kernel

\[
 G_N(j,k)=\frac{\min(j,k)\bigl(N+1-\max(j,k)\bigr)}{N+1}.
 \tag{129.H5}
\]

For \(z_j=e(f(v_j))\), the exact dual norm of
\(u\mapsto\sum_j u_jz_j\) is

\[
 \boxed{
 \|z\|_{(V^2)^*}^2
 =\sum_{j,k=1}^N G_N(j,k)z_j\overline{z_k}.}
 \tag{129.H6}
\]

The extremizer is the normalized vector
\(G_N\overline z\).  In particular, for \(z_j=1\),

\[
 \|z\|_{(V^2)^*}^2
 ={N(N+1)(N+2)\over12}\asymp N^3.
 \tag{129.H7}
\]

Thus the generic \(V^2\) loss is structural, not an artefact of one
partial-summation proof.

### 2.2 Literal threshold family being audited

For one character-split branch write

\[
 U(v)=\tau(v)\sum_t c_t R_t(v),\qquad
 R_t(v)={1\over a'}
 \sum_{g\le t/(\rho v)}^{*}{\chi_4(g)\over g}P_{a'}(g),
 \qquad \sum_t|c_t|\ll1,
 \tag{129.H8}
\]

and

\[
 f(v)=-{c a'\over\kappa_i\rho v}
       +\vartheta_{i,\eta}\rho v,
 \quad
 \vartheta_{1,\pm}=\pm\tfrac14,
 \quad \vartheta_{2,0}=0.
 \tag{129.H9}
\]

Here \(b'=\rho v\asymp B\), \(|a'|\asymp LB/D\),
\(N\asymp Q_B/\rho\), and
\(|f''(v)|\asymp\mu:=\lambda_B\rho^2\) on a clipped interval.
The multiplier \(\tau\) contains the determinant taper, strict/weak
faces, star, and half-open shell owner and has bounded sampled supremum
plus variation on \(O(1)\) clipped intervals.

### 2.3 Counterexample hypotheses

Take \(B\asymp D\), \(\rho=1\), an odd \(a'\asymp L\), and the interior
one-lift packet used in the accepted Round-128 top-shell control, so that
only \(g=1\) is active and \(P_{a'}(1)/a'\asymp L^{-1}\).  Choose
\(v_0\asymp D\) strictly inside one owner interval.  For any of the three
branches choose an integer \(m\asymp L\) and the real centre

\[
 c={\kappa_i\bigl(m-\vartheta_{i,\eta}\bigr)v_0^2\over a'}.
 \tag{129.H10}
\]

Then \(c\asymp Y\), \(f'(v_0)=m\in\mathbb Z\), and

\[
 \mu:=|f''(v_0)|
 ={2|m-\vartheta_{i,\eta}|\over v_0}
 \asymp {L\over D}=Y^{-1/3}.
 \tag{129.H11}
\]

Let \(M=\lfloor\delta\mu^{-1/2}\rfloor\), where \(\delta>0\) is a
small fixed constant.  Since \(M\asymp L\ll Q_B\), this packet lies
strictly inside the physical reciprocal window.

## 3. Proof and derivation

### 3.1 Proof of the exact dual formula

Equation (129.H4) is \(u^*L_Nu\).  Therefore the Riesz vector of the
functional \(u\mapsto\sum u_jz_j\) is \(L_N^{-1}\overline z\), and its
squared norm is (129.H6).  Direct multiplication shows that (129.H5) is
the inverse of the tridiagonal matrix: it is affine in either index away
from the diagonal, has the unit diagonal jump, and vanishes at the two
fictitious boundary vertices \(0,N+1\).  For \(z=1\), solving
\(L_Nx=1\) gives \(x_j=j(N+1-j)/2\); summing \(x_j\) proves (129.H7).

This calculation is also an exact threshold-span control.  On the
one-lift top shell, away from a zero of \(\tau\),
\(U(v)=A\tau(v)w(v)\), \(A\asymp L^{-1}\), and every compactly
supported vector \(w\) has the exact representation

\[
 w(v)=\sum_{t\ge v}c_t,\qquad c_t=w(t)-w(t+1).
 \tag{129.H12}
\]

Rescaling \(w\) makes \(\sum|c_t|\le1\), while both sides of a
norm-relative inequality rescale equally.  Hence bounded Stieltjes mass
alone cannot shrink the dual space.

### 3.2 Reciprocal stationary-alias counterexample

Choose a nonnegative triangular cutoff \(\psi_v\), supported on
\(|v-v_0|\le M\), equal to one on the middle half, and satisfying
\(|\Delta\psi_v|\ll M^{-1}\).  On this interior packet \(\tau\) is
bounded away from zero.  Define the sampled denominator profile

\[
 w(v)={\overline A\over|A|}\,\tau(v)^{-1}\psi_v e(-f(v)).
 \tag{129.H13}
\]

The exact Stieltjes coefficients from (129.H12) have bounded total mass.
Indeed, because \(f'(v_0)=m\in\mathbb Z\), Taylor's formula gives, for
\(|s|\le M\),

\[
 f(v_0+s+1)-f(v_0+s)-m=O(\mu(|s|+1)),
 \tag{129.H14}
\]

while \(\mu M^2\asymp1\); the cubic remainder is
\(O(\mu M^3/D)=o(1)\).  Thus the sampled variation of the chirp factor
in (129.H13) is \(O(\mu M^2)=O(1)\).  The cutoff and \(\tau^{-1}\)
also have bounded variation.  Hence \(\sum_t|c_t|\ll1\) exactly as
required in (129.H8).

For this profile the full amplitude is

\[
 U(v)=|A|\psi_v e(-f(v)),
\]

so

\[
 \left|\sum_vU(v)e(f(v))\right|
 =|A|\sum_v\psi_v\gg |A|M\asymp |A|\mu^{-1/2}.
 \tag{129.H15}
\]

Both displayed \(V^2\) endpoints vanish.  Moreover, (129.H14) and
\(|\Delta\psi|\ll M^{-1}\) give

\[
 \begin{aligned}
 \|U\|_{V^2}^2
 &\ll |A|^2\left(M^{-1}
       +\mu^2\sum_{|s|\le M}(|s|+1)^2\right)\\
 &\ll |A|^2\mu^{1/2},
 \qquad
 \|U\|_{V^2}\ll |A|\mu^{1/4}.
 \end{aligned}
 \tag{129.H16}
\]

Equations (129.H15)--(129.H16) prove (129.H1).  At the top shell,

\[
 Q_B={D^2\over WL}=Y^{19/48},\quad
 \lambda_B={YL\over D^3}=Y^{-1/3},\quad
 Q_B\sqrt{\lambda_B}+\lambda_B^{-1/2}\asymp Y^{11/48}.
 \tag{129.H17}
\]

The proposed estimate would require
\(\mu^{-3/4}\ll Y^{11/48+\varepsilon}\), but its left side is
\(Y^{1/4}=Y^{12/48}\).  This is the claimed \(Y^{1/48}\) contradiction.

The construction is insensitive to reciprocal aliases and quarter
phases: (129.H10) places the alias at an integer after the literal M1
quarter shift, and (129.H14) subtracts precisely that integer linear
phase.  It uses no endpoint, star, parity, Möbius, or shell ambiguity.

### 3.3 Exact single-threshold birth/alias control

The failure is caused by threshold superposition relative to the
\(V^2\) norm, not by a single threshold.  Fix \(t\asymp D\) and put
\(M_t(v)=\lfloor t/(\rho v)\rfloor\).  Character Abel summation before
modulus, with the accepted BV frequency factor, gives

\[
 \sup_v|R_t(v)|\ll_\varepsilon L^{-1}Y^\varepsilon.
 \tag{129.H18}
\]

Across the same physical \(b'\)-window, the number of constant
\(M_t\)-plateaux is

\[
 K_t\ll_\varepsilon
 1+{DQ_B\over B^2}.
 \tag{129.H19}
\]

Strict/weak choices change a boundary convention only.  A starred equality
adds at most a divisor number of singleton pieces, absorbed by
\(Y^\varepsilon\).

On each plateau, the second-derivative estimate, including an arbitrary
integer first-derivative alias, gives

\[
 \left|\sum_{v\in J}^{*}\tau(v)e(f(v))\right|
 \ll (\|\tau\|_\infty+\operatorname {Var}_J\tau)
 \min\bigl(|J|,|J|\sqrt\mu+\mu^{-1/2}\bigr).
 \tag{129.H20}
\]

If \(\mu\ge1\), the trivial bound gives \(N/L\), which is the first
branch of the proposed minimum.  If \(\mu<1\), sum (129.H20) over the
plateaux.  Their lengths sum to \(N\), and the total variation of
\(\tau\) is \(O(1)\).  The only apparent extra term is
\(K_t\mu^{-1/2}\).  Its nonconstant part is absorbed exactly because

\[
 \begin{aligned}
 {DQ_B\over B^2}\,\mu^{-1/2}
 &= {DQ_B\over B^2\rho\sqrt{\lambda_B}}\\
 &= {1\over\rho L}\,Q_B\sqrt{\lambda_B},
 \end{aligned}
 \tag{129.H21}
\]

where \(D^2=Y\) and \(\lambda_B=YL/(DB^2)\).  The constant part of
\(K_t\) is the displayed \(\mu^{-1/2}\) endpoint term.  Consequently

\[
 \left|\sum_{v\in I}^{*}R_t(v)\tau(v)e(f(v))\right|
 \ll_\varepsilon {Y^\varepsilon\over L}
 \min\bigl(N,N\sqrt\mu+\mu^{-1/2}\bigr).
 \tag{129.H22}
\]

This is uniform in \(\rho\), in M1's two quarter shifts, in M2, and at
every reciprocal stationary alias.  It is the requested exact
birth-lattice/alias control.

### 3.4 Threshold superposition: what Minkowski does and does not prove

Minkowski and \(\sum|c_t|\ll1\) lawfully sum (129.H22), proving
(129.H3).  This step loses no \(D\), \(G\), \(J_B\), or
\(N^{1/2}\), and it keeps \(\chi_4(g)\) inside (129.H18) until after
character cancellation.

What fails is the subsequent replacement

\[
 {1\over L}\sum_t|c_t|
 \stackrel{\rm false}{\ll}\|U\|_{V^2(I)}.
 \tag{129.H23}
\]

The alias profile has left side \(\asymp L^{-1}\) and right side
\(\ll L^{-1}\mu^{1/4}\).  Thus an absolute threshold-Minkowski estimate
cannot be advertised as the proposed norm-relative theorem.  Formula
(129.H3) is candidate evidence for a differently normalized continuation,
but that continuation is outside this round's frozen promotion rule and
has not been assembled here.

### 3.5 Literal owners

The counterexample is supported strictly inside one clipped determinant
interval, one half-open \(B\)-shell, one frequency sign, and one
moving-symbol stratum.  It has \(g=1\), \(\rho=1\), no shell crossing,
no endpoint mass, and no starred equality at its support boundary.
Therefore adding the omitted literal faces cannot cancel it.  Conversely,
the single-threshold proof charges each such face once: bounded-BV taper
and cell faces enter \(\tau\), equality stars give divisor-many
singletons, and half-open shells give one owner.  The Möbius sum is taken
only after the uniform progression bound; \(\rho=1\) alone already
falsifies the universal norm statement.

## 4. First doubtful or unproved step

The first false step is (129.H23), equivalently the claim that the exact
dual norm (129.H6) is bounded by the unweighted second-derivative factor
\(F\) on the whole bounded-mass Stieltjes span.  The top-shell threshold
span contains the reciprocal chirp packet (129.H13), and (129.H15)--
(129.H17) disprove that claim by \(Y^{1/48}\).

For the narrower **fixed physical** M1/M2 denominator profiles, the first
unproved step is different: one must use an exact property excluding
(129.H13), not merely bounded sampled variation, Stieltjes mass, the common
character, or the already proved upper bound on \(\|U\|_{V^2}\).  The
selected context identifies the physical profiles as fixed smooth
rescalings plus one hard sample, but supplies no norm-relative
reciprocal-phase theorem for them.  Hence this hostile review cannot
certify that narrower assertion and also cannot claim that the physical
profiles attain the counterexample.

## 5. Control tests, seam matrix, and outcomes

| Required seam/control | Hostile test | Outcome |
|---|---|---|
| `branchwise_literal_dictionary` | Used exactly the two M1 phases \(\vartheta=\pm1/4\) and the M2 phase \(0\), with the common lift character left in the threshold partial sum. | **Pass as normalization.** No unsplit M1 character was put back into \(U\). |
| `generic_V2_dual_countermodel` | Computed the exact Green kernel (129.H5)--(129.H7). | **Fail for the proposed generic inference.** The dual loss is intrinsic. |
| `single_threshold_birth_phase` | Partitioned by \(\lfloor t/(\rho v)\rfloor\) and proved (129.H22). | **Pass.** A single threshold survives every integer alias. |
| `character_before_modulus` | Applied character Abel to obtain (129.H18) before estimating plateaux. | **Pass.** Replacing \(\chi_4\) by an unsigned lift would invalidate this step. |
| `M1_quarter_phase_aliases` | Solved \(c a'/(\kappa v_0^2)\pm1/4=m\) exactly. | **Fail for the norm theorem; pass for single thresholds.** Quarter shifts move but do not remove stationary aliases. |
| `reciprocal_second_derivative_and_stationary_lattice` | Alias packet (129.H10)--(129.H17); plateau endpoint identity (129.H21). | **Exact obstruction plus exact control.** The norm theorem loses \(Y^{1/48}\); the single-threshold stationary costs are fully priced. |
| `threshold_superposition_and_Minkowski` | Summed (129.H22) using \(\sum|c_t|\ll1\). | **Absolute pass, norm-relative fail.** Minkowski proves (129.H3), not (129.H23). |
| `V2_endpoint_terms` | Chose the alias packet to vanish at both endpoints. | **Fail remains.** The counterexample does not exploit missing endpoint terms. |
| `mobius_progressions` | Used the legal divisor \(\rho=1\); (129.H22) is uniform for general \(\rho\). | **Pass/decisive.** One legal progression suffices to refute a universal claim. |
| `floors_stars_taper_and_shell_owners` | Interior one-lift packet for the obstruction; bounded-BV and singleton accounting for (129.H22). | **Pass.** No duplicated or omitted owner causes the failure. |
| `actual_vs_phase_adapted_coefficients` | The profile (129.H13) is bounded-mass Stieltjes but phase-adapted; fixed physical profiles were not shown to realize it. | **Strict scope restriction.** Reject the displayed abstract theorem; retain the narrower physical question open. |
| `N_rho_square_root_stop_rule` | Exact dual ratio exceeds the claimed curvature factor by \(Y^{1/48}\), even though the crude generic \(N^{1/2}\) upper loss is not needed. | **Stop.** No norm-relative certification. |
| `theta_two_thirds_capacity_threshold` | Round-128 still proves the coefficient exponent \(\theta=1/2\), but that upper norm does not repair the false dual estimate. | **No capacity promotion.** The \(\theta<2/3\) check is necessary, not sufficient. |
| `no_exponent_or_M9_promotion` | Applied the frozen failure rule. | **Pass.** No \(Y^{73/96}\) block, global exponent, M9 parent, endpoint theorem, M9, or quarter theorem is claimed. |

All controls are analytical/algebraic.  No numerical experiment and no
external theorem were used.

## 6. Dependencies and exact artifacts used

This review used exactly the generated brief and its selected context:

1. `protocol.md`, for graph authority, signed/unsigned separation, hostile
   controls, and the seven-section report contract;
2. `state/proof_obligations.yml`, especially the accepted reduced-Farey
   dictionary, original-variable bound, top-shell curvature lemma,
   character-split local \(V^2\) lemma, normalization obstruction, and
   conditional connector;
3. `state/active_campaign.yml`, for the frozen scales, branch phases,
   completion tests, and stop rule;
4. `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/reviews/conductor_round117_actual_savings.md`, for the accepted top-shell
   progression and curvature normalization;
5. `rounds/codex-managed/full-proof-frontier-inequality-selection-gate/reports/graded_determinant_long_lift_feasibility.md`, for the proposed
   norm-relative inequality, \(Q_B,\lambda_B,J_B\), and capacity scope;
6. `rounds/codex-managed/gc-w7-16-local-transverse-lift-variation-gate/reports/blind_local_v2_feasibility.md`, for the abstract \(V^2\) warning and
   endpoint convention;
7. `rounds/codex-managed/gc-w7-16-local-transverse-lift-variation-gate/reports/literal_lift_coefficient_variation_attack.md`, for the exact
   character-split dictionary and discrete Stieltjes formula;
8. `rounds/codex-managed/gc-w7-16-local-transverse-lift-variation-gate/reviews/conductor_round128_literal_v2_adjudication.md`, for the accepted
   physical coefficient scope and remaining open theorem; and
9. `rounds/codex-managed/gc-w7-16-local-transverse-lift-variation-gate/controls/conductor_round128_controls.md`, for character, endpoint,
   Möbius, star, and owner controls.

The generated task brief was used only to enforce this exact context and
output contract.  No Round-129 sibling report, unlisted historical
artifact, web source, or computation was used.

## 7. Recommended state effect

**Reject** the displayed norm-relative reciprocal-curvature theorem under
the stated assumptions \(\sum_t|c_t|\ll1\) and
\(\|U\|_{V^2}\): the exact stationary-alias Stieltjes profile
(129.H13) is a counterexample with a power gap \(Y^{1/48}\).  Retain the
exact Green-kernel dual formula and the phase-adapted top-shell packet as
the smallest rigorous obstruction.

**Retain open, with a strict scope restriction,** a theorem for the fixed
physical smooth/hard denominator profiles.  Such a theorem must state and
use the precise non-phase-adaptation property that excludes (129.H13).
Bounded variation, bounded Stieltjes mass, the common lift character, the
birth count, and the Round-128 \(V^2\) upper bound do not suffice.

**Retain as candidate evidence only** the single-threshold lemma
(129.H22) and its lawful absolute Minkowski consequence (129.H3).  They do
not certify the norm-relative claim.  Any continuation based on the
different normalization in (129.H3) requires a separately frozen round
and a fresh outer-owner adjudication; it is not promoted here.

Under the frozen Round-129 stop rule, park this graded norm-relative
continuation.  Make no change to the actual \(Y^{1/2}\) determinant
correlation, M9-M1, M9-M2, endpoint uniformity, M9, the conditional
quarter bridge, the global pointwise exponent, or the Gauss-circle target.
