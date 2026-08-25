# Joint cluster-defect broad--narrow attack: exact character gauge and cylindrical-ruling obstruction

## 1. Result: lemma or no-go result

**Result (`broad_narrow_no_go`).**  There is an exact arithmetic gauge
identity in the literal divisor progression.  If

\[
 h+2s_d=d\ell_d,\qquad \mu=\tfrac12-m,\qquad
 \lambda=\mu/d,
\]

then, with all four integers \(h,d,\ell_d,2\mu\) odd,

\[
 \boxed{
 e\!\left(-{\lambda h\over2}
       +s_d(\tfrac12-\lambda)\right)
 =-i(-1)^m\chi _4(d)\chi _4(h).}
 \tag{136.A1}
\]

Consequently the literal bulk kernel is exactly

\[
 \begin{aligned}
 \mathcal K_B^{\rm bulk}
 ={}&-i\sum_{h\ {\rm odd},k,k'}
   \chi _4(h)b_B(h,k)e(R\sqrt{hk})
   \sum_{\substack{d\mid k'\\d\ {\rm odd}}}
   \gamma_d\chi _4(d)                                      \\
 &\quad\times
   \sum_J\sum_{\substack{\mu=1/2-m>0\\t_*\in J}}^{\rm bulk}
   (-1)^m\mathcal A_{d,J}(h,k,k';\mu)
   e\!\left(-{Xk'\over2\lambda}\right).
 \end{aligned}
 \tag{136.A2}
\]

No lift, gate, profile, or owner has been removed in (136.A2).

At the natural gate resolution \(\delta=L^{-1}\), put
\(r=\sqrt{k/h}\) and \(z=\lambda/R\).  After the exact gauge (136.A1),
the normalized joint phase-gradient surface is

\[
 \Sigma(r,z)=(r,r^{-1},-z^{-1}).
 \tag{136.A3}
\]

Its normal is proportional to \((1,r^2,0)\), independently of \(z\).
Thus the determinant of every three normals is identically zero in the
chosen gauged surface-normal chart.  The explicit three-normal broad
part defined below is therefore empty at every positive resolution, and
that particular partition assigns every literal atom to its narrow
part.  This is not an intrinsic or gauge-invariant assertion that the
kernel is universally narrow.  A two-normal split in the same chart can
separate different \(r\)-strips, but leaves the complete \(z\)-ruling;
its positive diagonal has \(L^4\) capacity, one factor \(L\) above the
scalar target.

The arithmetic inside this assigned narrow part does not repair the
method defect automatically.  If
\(\lambda=a/(2b)\) is reduced with \(a,b\) odd, its distinct lifts are

\[
 (d,\mu)=(cb,ca/2),\qquad c\ {\rm odd},
\]

and their literal character factor satisfies

\[
 \boxed{(-1)^m\chi _4(d)=\chi _4(a)\chi _4(b),}
 \tag{136.A4}
\]

independently of \(c\).  Equal-rational-\(\lambda\) lifts are therefore
character-coherent, not character-canceling.  For the subclass \(b=1\),
the exact odd-divisor sum \(\sum_{d\mid n}\gamma_d/d\) is strictly
positive by (136.A18).  This yields a positive lift coefficient only in
a leading model with common profile and common admissibility; it says
nothing comparable about the full literal amplitudes.  The remaining
\((-1)^m\) carrier also gives a canonical phase self-return:
Poisson/B-process in \(\mu\) returns
\(h'=d(2n+1)\), \(k'=dv\), and the reciprocal phase.  A return of all
profiles, gates, \(J\)-owners, boundaries, and remainders is not proved
here.

Hence neither the apparent unfactored curvature nor the actual
\(\chi _4\)/residue signs supply a literal broad--narrow proof of
\(|\mathcal K_B^{\rm bulk}|\ll L^3X^\varepsilon\).  The result is a
scoped no-go for a transversality/positive-cap closure, not a lower bound
for the physical scalar and not a disproof of the target.

## 2. Exact statement and hypotheses

Let \(X\ge4096\), \(R=\sqrt X\), and \(L\asymp X^{1/6}\).  Fix one
persistent \(j=1\) Round-113 smooth balanced physical block \(B\).  The
first literal low-gcd coefficient is

\[
 b_B(h,k)=\eta((h,k)/G_0)A_B(h,k),\qquad G_0=\sqrt L/2,
 \tag{136.A5}
\]

where \(A_B\) is the fixed real slanted profile, with every Vaaler taper,
floor, star, and support crossing retained.  The second low-gcd weight is
expanded only through

\[
 \gamma_d=\sum_{e\mid d}\mu(e)
       \eta\!\left({d/e\over G_0}\right),
 \qquad
 \sum_{d\mid k'}|\gamma_d|\ll_\varepsilon X^\varepsilon.
 \tag{136.A6}
\]

For each odd \(d\mid k'\), retain

\[
 h'=h+2s=d(\ell_d+2t),\quad s=s_d+dt,
 \quad h+2s_d=d\ell_d,
 \tag{136.A7}
\]

and the exact half-lattice \(\mu=1/2-m>0\), \(\lambda=\mu/d\).  Every
atom keeps its label

\[
 \alpha=(h,k,k',d,\mu,J),
\]

even when another atom has the same reduced rational \(\lambda\).  Its
stationary point, phase, and gates are

\[
 x_*={Xk'\over\lambda^2},
 \qquad
 \Theta_{d,\mu}=R\sqrt{hk}-{Xk'\over2\lambda}
 -{\lambda h\over2}+s_d(\tfrac12-\lambda),
 \tag{136.A8}
\]

\[
 \rho=hk'-x_*k={hk'\over\lambda^2}
      (\lambda^2-\lambda_0^2),\qquad
 \Delta=x_*k'-hk={hk\over\lambda^2}
      (\lambda_r^2-\lambda^2),
 \tag{136.A9}
\]

where \(\lambda_0=R\sqrt{k/h}\),
\(\lambda_r=Rk'/\sqrt{hk}\), and every retained atom obeys the two
strict conditions \(|\rho|>L\), \(|\Delta|>L\).  The label \(J\) keeps
the exact support components and the strict equality convention.  Only
the already-isolated interior bulk is considered; boundary, crossing,
transition, nonstationary, and stationary-remainder owners are not
reopened.

On this support

\[
 \mu\asymp dL^3,\qquad
 \#\{\mu:t_*\in J\}\asymp dL^3,\qquad
 |\mathcal A_{d,J}|\ll(dL)^{-1},
 \tag{136.A10}
\]

and there are \(O(L^3)\) outer triples \((h,k,k')\).

Here is the promised literal partition.  Let \(\delta=L^{-1}\), and
partition the fixed compact \((r,z)\)-support into half-open rectangles

\[
 \tau_{u,v}=[u\delta,(u+1)\delta)
             \times[v\delta,(v+1)\delta),\qquad
 r=\sqrt{k/h},\quad z={\lambda\over R}.
 \tag{136.A11}
\]

An atom belongs to exactly one \(\tau\); a cell meeting a gate is split
by its original \(J\)-labels, rather than by smoothing or changing the
gate.  Write \(\mathcal K_\tau\) for the sum of the original atoms in
that cell.  At a cell center define

\[
 N_\tau={ (1,r_\tau^2,0)\over\sqrt{1+r_\tau^4}},
 \qquad
 \operatorname{Tr}(\tau_1,\tau_2,\tau_3)
 =|\det(N_{\tau_1},N_{\tau_2},N_{\tau_3})|.
 \tag{136.A12}
\]

Call an atom **broad** if its cell occurs in a triple with
\(\operatorname{Tr}\ge\delta^2\); call it **narrow** otherwise.  This
gives the exact disjoint identity

\[
 \mathcal K_B^{\rm bulk}=\mathcal K_{B,\rm br}
                         +\mathcal K_{B,\rm nar}.
 \tag{136.A13}
\]

Finally, every narrow atom has a unique exact arithmetic class.  Reduce

\[
 {k\over h}={v\over u},\quad (u,v)=1,\quad h=gu,\ k=gv,
 \qquad
 2\lambda={a\over b},\quad (a,b)=1,\quad a,b\ {\rm odd}.
 \tag{136.A14}
\]

Then necessarily \(d=bc\), \(2\mu=ac\) for an odd \(c\), and
\(k'=bcw\).  The tuple \((u,v;a,b;c,g,w,J)\), with (136.A9) still
imposed, is the literal aligned-ruling classification.  No sum over
\(c\), \(g\), or \(J\) is merged or put outside an absolute value.

## 3. Proof or derivation

**Exact character gauge.**  From (136.A7),

\[
 -{\lambda h\over2}+s_d(\tfrac12-\lambda)
 ={s_d\over2}-{\mu\ell_d\over2}.
 \tag{136.A15}
\]

Since \(\mu=1/2-m\) and \(\ell_d\) is odd,

\[
 e(s_d/2-\mu\ell_d/2)
 =(-1)^{s_d+m}e(-\ell_d/4)
 =-i(-1)^{s_d+m}\chi _4(\ell_d).
\]

Also \(h=d\ell_d-2s_d\), so
\(dh\equiv\ell_d-2s_d\pmod4\), and hence

\[
 \chi _4(d)\chi _4(h)=(-1)^{s_d}\chi _4(\ell_d).
\]

This proves (136.A1), and substitution in (136.A8) proves the exact
rewrite (136.A2).  In particular, the two original \(\chi _4\) factors
have not been dropped: their shifted product is precisely the factor on
the right of (136.A1).

**Collapse of the chosen gauged surface-normal broad part.**  The smooth
exponential left after (136.A1) is

\[
 \Psi(h,k,k';\lambda)=R\sqrt{hk}-{Xk'\over2\lambda}.
\]

Direct differentiation gives

\[
 {2\over R}\nabla_{h,k,k'}\Psi
 =(r,r^{-1},-z^{-1})=\Sigma(r,z).
\]

The two tangent vectors are

\[
 \partial_r\Sigma=(1,-r^{-2},0),\qquad
 \partial_z\Sigma=(0,0,z^{-2}),
\]

whose cross product is proportional to \((1,r^2,0)\).  Therefore

\[
 \operatorname{Tr}(\tau_1,\tau_2,\tau_3)=0
 \quad\hbox{for every triple},
 \tag{136.A16}
\]

so (136.A13) has

\[
 \boxed{\mathcal K_{B,\rm br}=0,
 \qquad \mathcal K_{B,\rm nar}=\mathcal K_B^{\rm bulk}.}
 \tag{136.A17}
\]

Equation (136.A17) is exact for the partition (136.A11)--(136.A13):
(136.A16) holds at every resolution in this chosen gauged
surface-normal chart.  It is not an intrinsic or gauge-invariant
classification of the literal kernel, and it does not imply that every
other gradient-based partition is narrow.

If instead one differentiates the unfactored real expression in
(136.A8), one gets

\[
 \Sigma_0(r,z)=(r-z,r^{-1},-z^{-1}),
 \qquad N_0(r,z)\parallel(1,r^2,z^2),
\]

and the corresponding surface-normal determinant

\[
 (r_2^2-r_1^2)(z_3^2-z_1^2)
 -(r_3^2-r_1^2)(z_2^2-z_1^2).
\]

But (136.A1) moves exactly the \(z\)-dependent first coordinate into a
literal unit-modulus arithmetic modulation.  Thus this
**surface-normal** determinant is not invariant under an exact
rewriting of the same lattice sum.  It is distinct from the raw
gradient-vector determinants
\(\det(\Sigma_0(r_i,z_i))_{i=1}^3\) and
\(\det(\Sigma(r_i,z_i))_{i=1}^3\), either of which may be nonzero.
A coefficient-modulation-invariant broad or positive square-function
inequality cannot charge the unfactored normal determinant as physical
curvature without an interface that retains the arithmetic modulation.
A theorem that does charge it would first have to exploit, rather than
discard, the precise factor
\((-1)^m\chi _4(d)\chi _4(h)\); that is the missing signed theorem.

The one-body Hessian is a third determinant.  With \(v=k'/d\) and
\[
 \Phi_d(v,m)=-{Xd^2v\over2\mu}-{\ell_d\mu\over2}+{s_d\over2},
 \qquad \mu=\tfrac12-m,
\]
one has
\[
 \det D^2_{v,m}\Phi_d=-{X^2d^4\over4\mu^4}\asymp-1.
\]
This certifies only a locally invertible canonical Jacobian on one
index sheet.  It supplies neither a gradient-vector broad determinant
nor a multilinear surface-normal transversality statement.

There remains bilinear rank in \(r\):
\(|N(r_1)\times N(r_2)|\asymp|r_1-r_2|\) on the fixed support.  It does
not separate the \(z\)-ruling because \(N\) is independent of \(z\).

**Exact aligned-ruling arithmetic.**  In (136.A14), write
\(d=bc\), \(2\mu=ac\).  Then

\[
 m={1-ac\over2},\qquad
 (-1)^m=\chi _4(ac)=\chi _4(a)\chi _4(c),
\]

and therefore

\[
 (-1)^m\chi _4(d)
 =\chi _4(a)\chi _4(b)\chi _4(c)^2
 =\chi _4(ab),
\]

which proves (136.A4).  Within the class, the exponential is

\[
 -i\chi _4(h)\chi _4(ab)
 e\!\left(Rg\sqrt{uv}-{Xbk'\over a}\right).
\]

The lift label \(c\) still changes \(\gamma_{bc}\), the progression,
the exact amplitude, and admissibility, so the lifts remain distinct;
only their actual character direction has been computed.

There is a narrower exact divisor check on the \(b=1\) subclass.  Let
\(n\) be the odd part of \(k'\).  Directly from (136.A6), the exact
odd-divisor sum is

\[
 \begin{aligned}
 \sum_{d\mid n}{\gamma_d\over d}
 &=\sum_{r\mid n}{\eta(r/G_0)\over r}
   \sum_{e\mid n/r}{\mu(e)\over e}  \\
 &=\sum_{r\mid n}{\eta(r/G_0)\over r}
   {\varphi(n/r)\over n/r}>0.
 \end{aligned}
 \tag{136.A18}
\]

Here strict positivity uses the fixed nonnegative cutoff and its
nonzero \(r=1\) term.  If a separately justified leading model has
common admissibility for every \(d\mid n\) and factors its lift
amplitude as \(W/d\) with one common profile/Fresnel factor \(W\), then
its divisor coefficient is
\(W\sum_{d\mid n}\gamma_d/d\) and has the common direction of \(W\).
Neither common admissibility nor this \(W/d\) factorization has been
proved for the full literal
\(\mathcal A_{d,J}(h,k,k';\mu)\).  Equation (136.A18) therefore gives
no positivity, nonvanishing, or lower bound for the exact owner-complete
packet.

**The factorization gives only a canonical phase self-return.**  Put
\(k'=dv\).
Since \((-1)^m=e(1/4-\mu/2)\), the smooth \(\mu\)-phase in (136.A2), up
to a constant, is

\[
 g(\mu)=-{Xd^2v\over2\mu}-{\mu\over2}.
\]

Poisson in the half-lattice, with dual integer \(n\), has stationary
equation

\[
 g'(\mu)=n,\qquad
 {Xd^2v\over2\mu^2}-{1\over2}=n,\qquad
 x_*={Xd^3v\over\mu^2}=d(2n+1).
\]

At that point

\[
 g(\mu)-n\mu=-dR\sqrt{v(2n+1)}
             =-R\sqrt{h'k'},
\]

with \(h'=d(2n+1)\), \(k'=dv\).  The half-lattice factor and
\(\chi _4(d)\) have the formal character direction
\(\chi _4(h')\).  These equations certify the stationary relation and
the canonical phase self-return only.  They do not constitute a full
owner ledger for reciprocal Jacobians, literal profiles, \(J\)-support,
the two gates, boundary terms, or stationary remainders.  Thus (136.A1)
exposes the character but, at the level proved here, creates no
independent alternating-sum saving.

**Complete capacity ledger.**  The scale \(\delta=L^{-1}\) is also the
literal gate scale: from (136.A9), with \(r,z,z_r\asymp1\), each strict
gate removes a \(z\)-neighborhood of width comparable with \(L^{-1}\),
while its exact boundary remains in \(J\).

For one \((r,z)\)-cell there are

\[
 \begin{array}{c|c}
 \text{item}&\text{capacity}\ \\ \hline
 (h,k)\text{ in an }r\text{-strip}&O(L)\\
 k'&O(L)\\
 \mu\text{ in a }z\text{-strip for fixed }d&O(dL^2)\\
 |\mathcal A_{d,J}|&O((dL)^{-1})\\
 \sum_{d\mid k'}|\gamma_d|&O_\varepsilon(X^\varepsilon).
 \end{array}
\]

The first line follows because, for each \(h\asymp L\), an
\(L^{-1}\)-interval in \(r\) permits only \(O(1)\) integers \(k\) on
the balanced scale; the first low-gcd mask only decreases this count.
Hence one cap already has triangle capacity

\[
 L\cdot L\cdot(dL^2)\cdot(dL)^{-1}=L^3.
 \tag{136.A19}
\]

There are \(O(L)\) cells in each of \(r,z\), so capwise \(\ell^1\)
returns \(L^5\), while a coefficient-blind square sum has \(L^4\)
capacity.  The latter agrees with the exact \(d=1\) positive diagonal

\[
 L^2\ \text{outer }(h,k)\text{ rows}
 \times L\ k'\text{ values}
 \times L^3\ \mu\text{ values}
 \times L^{-2}\ \text{amplitude square}=L^4.
 \tag{136.A20}
\]

Thus even after all available bilinear \(r\)-transversality, a positive
norm over the unresolved \(z\)-rulings is one factor \(L\) too large.
Equation (136.A4) shows that this factor cannot be assigned to automatic
divisor-lift character cancellation.  Equation (136.A18) supplies only
the additional exact divisor-sum check, with a positive coefficient
interpretation restricted to the common-profile/common-admissibility
leading model described above.

## 4. First doubtful or unproved step

There is no unproved determinant estimate inside the chosen partition:
its gauged surface-normal determinant is exactly zero.  This is not a
gauge-invariant statement about raw gradient-vector determinants or
about all possible broad interfaces.  The first genuinely unproved step
would be a signed, non-positive inequality that gains a factor \(L\)
across the classes assigned narrow by (136.A11)--(136.A13),

\[
 (u,v;a,b;c,g,w,J)\longmapsto
 \chi _4(gu)\chi _4(ab)
 e\!\left(Rg\sqrt{uv}-{Xb^2cw\over a}\right)
 \tag{136.A21}
\]

with the exact \(\gamma_{bc}\), \(\mathcal A_{bc,J}\), both gates, and
all profiles retained.  Neither a three-cap theorem applied to this
gauged surface-normal partition (which has no broad triple), a two-cap
positive square function (capacity \(L^4\)), nor liftwise character
orthogonality (false by (136.A4)) proves this.

Equivalently, the unresolved scalar is still

\[
 |\mathcal K_{B,\rm nar}|
 =|\mathcal K_B^{\rm bulk}|
 \ll_\varepsilon L^3X^\varepsilon.
\]

Opposite \(\chi _4(h)\chi _4(ab)\) classes may cancel only after the full
fixed-block scalar is assembled.  Taking a modulus of any ruling, lift,
residue, cap, or row destroys precisely that possible cancellation.  No
actual-symbol lower bound is asserted.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| `literal_bulk_kernel_and_owner_ledger` | **Pass.** Equations (136.A2), (136.A5)--(136.A10) retain the full bulk atom, fixed block, literal amplitude, every \(J\), and both strict gates. Only already-owned boundary/transition/remainder packages stay outside. |
| `divisor_progression_and_distinct_lifts` | **Pass.** The progression (136.A7) is retained. Equal reduced \(\lambda\) is parameterized by distinct \(c\)-lifts; (136.A4) computes their signs but does not identify their coefficients or amplitudes. |
| `joint_broad_partition_resolution` | **Pass.** The half-open \((r,z)\)-partition (136.A11) has the explicit resolution \(\delta=L^{-1}\), and gate-crossing cells retain the original \(J\)-split. |
| `broad_transversality_determinant` | **Exact failure in the chosen interface.** Every gauged surface-normal determinant (136.A12) is zero. The unfactored surface-normal determinant is gauge-dependent; raw gradient-vector determinants may be nonzero, and the one-body Hessian is a distinct canonical Jacobian. |
| `broad_capacity_to_L3` | **Vacuous broad bound, failed closure for this partition.** By (136.A17), \(\mathcal K_{B,\rm br}=0\) and \(\mathcal K_{B,\rm nar}=\mathcal K_B^{\rm bulk}\) for the chosen gauged surface-normal partition. A cap has \(L^3\) triangle capacity and the positive cap/row diagonal is \(L^4\). |
| `narrow_rational_ruling_classification` | **Pass.** Equation (136.A14) gives the unique primitive outer ratio and reduced half-rational \(\lambda\); \(d=bc,\mu=ca/2,k'=bcw\) lists every literal lift. |
| `actual_chi4_and_residue_phase` | **Pass, with scoped obstruction.** Identity (136.A1) is exact, and (136.A4) shows character coherence across equal-rational lifts. Equation (136.A18) is exactly the positive sum \(\sum_{d\mid n}\gamma_d/d\); it represents a lift coefficient only in a common-profile/common-admissibility leading model, never the full literal amplitudes. |
| `second_B_self_return` | **Canonical phase only.** The stationary equations recover \(h'=d(2n+1)\), \(k'=dv\), and the reciprocal phase. No full return ledger for profiles, \(J\)-support, gates, boundaries, or remainders is proved. |
| `coupled_rho_Delta_far_gates` | **Pass.** Both exact formulas (136.A9) remain inside every class. In the same-denominator test \(k'=k\), one has \(\Delta=-\rho\); the diagonal \(x_*=h\) fails both gates, while the strict double-far same-denominator remainder is assigned to the narrow part of this partition. |
| `coherent_and_opposite_character_packets` | **Pass as a method control.** Equal-\(\lambda\) lifts are literally coherent by (136.A4). Opposite \(h\) or \(ab\) residue classes have opposite signs but no gate/profile-preserving involution; separating their moduli is illegal. A fully phase-adapted coefficient array still saturates the \(L^4\) positive shadow, but this is used only to falsify coefficient-uniform closure, not as a physical lower bound. |
| `boundary_and_transition_scope` | **Pass.** The partition does not reclaim gate equality, incomplete Fresnel, support-crossing, nonstationary, or stationary-remainder terms. Their accepted \(O_\varepsilon(L^3X^\varepsilon)\) owner is unchanged. |
| `scalar_vs_positive_energy` | **Pass.** Equation (136.A20) is a capacity obstruction for a positive norm. It is not substituted for the signed scalar and does not imply that the scalar is large. |
| `full_BAL_owner_and_downstream_scope` | **Pass.** The result concerns only one persistent \(j=1\) balanced double-far bulk owner. The exact-square \(j=2\) boundary, the rest of BAL, TOP, UNBAL, M9-M2, endpoint uniformity, M9, and every global exponent remain unchanged. |
| Diagonal packet | **Excluded exactly.** \(k'=k,\lambda=\lambda_0\) gives \(x_*=h\), \(\rho=\Delta=0\), and is not in the bulk. |
| Same-rational-\(\lambda\) packet | **Character-coherent.** Equation (136.A4) is independent of the lift \(c\). For \(b=1\), (136.A18) proves positivity only of \(\sum_{d\mid n}\gamma_d/d\), with the leading lift interpretation conditional on common profile and common admissibility. |
| Same-denominator packet | **Survives in the assigned narrow part away from the diagonal.** For \(k'=k\), \(\Delta=-\rho\), so both strict gates survive or fail together; no extra character cancellation appears. |
| Gate-boundary packet | **No ownership change.** Width \(L^{-1}\) motivates the cap scale, but exact inequalities and \(J\)-ownership, not cap approximations, decide membership. |

## 6. Dependencies and exact artifacts used

This analytic derivation used only the permitted context, read before the
attack:

- `protocol.md`;
- `state/proof_obligations.yml`, including the accepted Round-113 literal
  dictionary, Round-114 double-corridor connector, Round-115 phase-free
  owner, and Round-116 divisor-progressive reduction and obstruction;
- `state/active_campaign.yml`;
- `strategy/conductor_0823_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m2-balanced-smooth-literal-atom-dictionary-reconciliation/synthesis.md`;
- `rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/synthesis.md`;
- `rounds/codex-managed/m9-m2-balanced-nonzero-alias-defect-gate/synthesis.md`;
- `rounds/codex-managed/m9-m2-balanced-nonzero-alias-defect-gate/reports/literal_alias_local_energy_attack.md`;
- `rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/blind_statement.md`;
- the generated task brief
  `rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/briefs/joint_cluster_defect_broad_narrow_attack.md`.

No sibling Round-136 report, computation, numerical experiment, web
source, or unstated external theorem was used in the original
derivation.  The later artifact-repair pass additionally used
reviews/blind_post_unmask_gauge_and_scalar_interface_audit.md and
reviews/discovery_post_unmask_ruling_and_capacity_audit.md, relative to
this round directory, solely to correct determinant, divisor-model, and
canonical-self-return scope.  The argument remains algebraic and
analytic.  The phase-free mode and the finite-Poisson error owners are
invoked only in their already accepted direction and exactly once; they
are not recombined with the bulk.

## 7. Recommended state effect

**Recommendation: retain the three target obligations as open and record
this candidate as `broad_narrow_no_go` after seam review.**  The exact
identity (136.A1), the cylindrical normal-rank identity (136.A16) in the
chosen gauged surface-normal chart, and the equal-rational-lift
coherence law (136.A4) are the proposed new scoped facts.  They show
that this standard three-cap surface-normal partition has no broad
input.  They do not show gauge-invariant or intrinsic universal
narrowness.  The remaining classes in this partition cannot be closed
by automatic \(\chi _4\)/residue cancellation.

Do not promote `M9-M2-balanced-double-far-oscillatory-remainder`,
`M9-M2-balanced-double-far-actual-energy`, or
`M9-M2-smooth-balanced-quarter-packet-estimate`.  A continuation must
prove a new gauge-sensitive signed inequality for (136.A21), before any
rulingwise modulus or positive cap norm.  No BAL parent, M9-M2, endpoint,
M9, quarter theorem, or global-exponent change is licensed.
