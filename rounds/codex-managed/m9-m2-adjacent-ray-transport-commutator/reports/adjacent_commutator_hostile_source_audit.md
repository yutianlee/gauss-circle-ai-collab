# Round 111 hostile/source audit: adjacent-ray transport commutator

Campaign: `m9-m2-adjacent-ray-transport-commutator`

Task: `adjacent_commutator_hostile_source_audit`

Role: hostile mathematical and source reviewer

Status: candidate evidence only; no shared proof state is edited.

## 1. Result

The parity high-pass identity and the continuous phase-preserving dilation
are exact.  They do not produce a saved power.  In particular, if

\[
 b=a+2q,\qquad \delta_q=\sqrt b-\sqrt a,\qquad
 \theta_q={\delta_{q+1}\over\delta_q},\qquad
 \lambda_q=\theta_q^{-2},
\]

then

\[
 T_q(x,k)=(\lambda_qx,k/\lambda_q)
\]

has determinant one and preserves simultaneously the physical phase,
the product \(kx\), and the metric ratio \(\Lambda_q/k\).  Thus its
continuous density/Jacobian contributes exactly no gain.

The first hostile seam is discrete.  Pulling the target mixed
\(dx\)-integer-\(k\) sampling measure back by \(T_q\) gives

\[
 dx\sum_{n\in\mathbb Z}\delta_n(dk)
 \quad\longmapsto\quad
 dx\,\lambda_q\sum_{n\in\mathbb Z}\delta_{\lambda_q n}(dk).
\tag{111.H1}
\]

On every common-interior interval of length comparable with the active
dual length \(K\), the total-variation distance between the two combs in
(111.H1) is comparable with \(K\), for rational and irrational
\(\lambda_q\).  It is not \(O(K/q)\), even though
\(\lambda_q=1+O(1/q)\).  The exact lattice commutator is consequently a
bulk, equal-capacity object in every coefficient-blind or
total-variation norm.  It is not merely supported at the endpoints.

The support commutator has additional genuine endpoint slabs.  In a cell
\(a\asymp A, q\asymp D, k\asymp K\asymp JD/A\), both transported
dual endpoints miss the adjacent literal endpoints by

\[
 \asymp {K\over q}\asymp {J\over A}.
\tag{111.H2}
\]

The inherited curvature/collar width is \(K/L\), so one adjacent step
crosses

\[
 {J/A\over K/L}\asymp {L\over D}
\tag{111.H3}
\]

collar widths.  On the physical side, the phase-preserving image and the
neighboring hard interval differ by two slabs of width
\(\asymp gA/q\asymp L/D\).  The untransported sharp lower ceiling itself
has the exact jump

\[
 \left\lceil {g(b+2)\over4}\right\rceil
 -\left\lceil {gb\over4}\right\rceil
 ={g-\chi_4(gb)\over2}.
\tag{111.H4}
\]

Because the lower edge has \(W(1)=1\), none of these atoms is killed by
an endpoint zero.  Classifying all of them as an already-owned fixed
collar would be false.  Per adjacent step their relative phase-space size
is \(1/q\), but absolute summation over \(q\asymp D\) restores the full
original capacity.  No strict polynomial subrange follows.

This is a rigorous no-go for an (O(1/q)), Jacobian, boundary-only,
total-variation, or coefficient-blind transport argument.  It is **not**
an actual-symbol lower bound.  The actual signed vector could still cancel
against the bulk comb discrepancy and the jump atoms before absolute
values.  No such cancellation is proved in the candidate, and the
one-sided Round-75 off-diagonal estimate remains open.

The smallest lawful survivor is therefore the exact parity identity,
the exact continuous transport, and the full signed sampling/support
commutator with every arithmetic and endpoint atom retained.  No external
theorem is invoked.

## 2. Exact statement and hypotheses

Let \(J=X^{1/2}\), \(1\le L\le J^{1/2}\), and use one representative
primitive orientation (a<b<4a), followed only at the energy level by
one outer \(2\Re\).  Put \(b=a+2q\), with \(a,b\) odd and \(q\ge1\), and
zero-extend every row outside its literal finite support.  When comparing
the (q) and (q+1) rows, require (b+2<4a); a collapsing or empty cone
edge is retained separately rather than treated as common interior.

For a common odd lift (g), retain the literal row

\[
\begin{aligned}
 F_{L,a}(q)={}&1_{q\ge1}1_{(a,a+2q)=1}
 \sum_{\substack{g\ \mathrm{odd}\\ga,g(a+2q)\in\mathscr H_L}}
 \sum_{m=\lceil g(a+2q)/4\rceil}^{ga}
 a_{\mathrm{end}}(ga,m)
 \overline{a_{\mathrm{end}}(g(a+2q),m)}\\
 &\qquad\qquad\times
 e\!\left(-J\sqrt g\,\delta_q\sqrt m\right).
\end{aligned}
\tag{111.H5}
\]

All half-open (A,D,K,G,R) ownership, open reciprocal intervals,
finite odd lifts, collars, floors, stars, equality weights, terminal
metric member, exact-centre convention, entry/exit atoms, and empty or
singleton fibres remain literal.

Let

\[
 \eta_q=\sqrt{b+2}-\sqrt b,
 \qquad
 \varepsilon_q={\eta_q\over\delta_q}
 ={\sqrt b+\sqrt a\over
    q(\sqrt{b+2}+\sqrt b)}.
\tag{111.H6}
\]

Then

\[
 \theta_q=1+\varepsilon_q,qquad
 \lambda_q=(1+\varepsilon_q)^{-2},qquad
 {1\over\lambda_q}-1=2\varepsilon_q+\varepsilon_q^2.
\tag{111.H7}
\]

On the cone \(a\le b<b+2\le4a\),

\[
 {1\over2q}\le\varepsilon_q\le {3\over2q},
 \qquad
 1-\lambda_q\asymp {1\over q}.
\tag{111.H8}
\]

Define

\[
 \Phi_q(x)=-J\sqrt g\,\delta_q\sqrt x,
 \qquad
 \Lambda_q={X\delta_q^2\over2}.
\]

The exact continuous identities to be certified are

\[
 \Phi_{q+1}(\lambda_qx)=\Phi_q(x),
 \qquad
 (k/\lambda_q)(\lambda_qx)=kx,
 \qquad
 {\Lambda_{q+1}\over k/\lambda_q}={\Lambda_q\over k},
 \qquad
 |\det DT_q|=1.
\tag{111.H9}
\]

For the dual reciprocal support write

\[
 I_q=(\alpha_q,\beta_q),\qquad
 \alpha_q={J\delta_q\over2\sqrt a},qquad
 \beta_q={J\delta_q\over\sqrt b}.
\tag{111.H10}
\]

Then

\[
 I_{q+1}=
 \left(\theta_q\alpha_q,
 \theta_q\beta_q\sqrt{b\over b+2}\right),
 \qquad
 T_{q,k}I_q=(\theta_q^2\alpha_q,\theta_q^2\beta_q).
\tag{111.H11}
\]

For the physical continuous hulls

\[
 P_q(g)=[gb/4,ga],\qquad
 P_{q+1}(g)=[g(b+2)/4,ga],
\]

one has

\[
 T_{q,x}P_q(g)=[\lambda_qgb/4,\lambda_qga].
\tag{111.H12}
\]

Finally, for a finite zero-extended scalar row (f), set

\[
 C(f)=\sum_{q\in\mathbb Z}(-1)^qf(q),
 \qquad Sf(q)=f(q+1).
\]

The exact norm hierarchy under audit is

\[
 2C(f)=\sum_q(-1)^q(I-S)f(q),
\tag{111.H13}
\]

and hence

\[
 2\Re C(f)=\Re\sum_q(-1)^q(I-S)f(q),
 \qquad
 2|C(f)|\le\sum_q|(I-S)f(q)|.
\tag{111.H14}
\]

The second statement is only a sufficient total-variation upgrade; no
reverse implication is assumed.

## 3. Proof or derivation

Finiteness and zero extension give

\[
 \sum_q(-1)^qSf(q)
 =\sum_r(-1)^{r-1}f(r)=-C(f),
\]

which proves (111.H13).  With one orientation, the energy contribution is
\(2\Re C(f)\), so (111.H14) introduces neither a second orientation nor
a second outer factor.  The sequence \(f(q)=(-1)^qM\) on a long finite
interval shows the hostile norm direction: the parity mode is multiplied
by two in the interior.  Thus \(I-S\) is a high-pass identity, not a
smallness operator.

Equation (111.H6) follows from

\[
 \delta_q={2q\over\sqrt b+\sqrt a},
 \qquad
 \eta_q={2\over\sqrt{b+2}+\sqrt b}.
\]

This proves (111.H7)--(111.H8).  Since
\(\sqrt{\lambda_q}=\delta_q/\delta_{q+1}\) and
\(\Lambda_{q+1}=\Lambda_q/\lambda_q\), all three invariances in
(111.H9) are immediate.  The derivative matrix is

\[
 DT_q=\begin{pmatrix}\lambda_q&0\\0&\lambda_q^{-1}\end{pmatrix},
\]

so its determinant is exactly one.  At the level of a single \(x\)
integral, the substitution \(x'=\lambda_qx\) contributes
\(dx'=\lambda_qdx\).  Treating that factor as a saving is a normalization
error: after the integer \(k'\)-sum is pulled back, its lattice has spacing
\(\lambda_q\), hence density \(1/\lambda_q\), and the two factors cancel.

This cancellation is exact at the distribution level.  For a test
amplitude \(B\),

\[
 \sum_{n\in\mathbb Z}\int B(x',n)\,dx'
 =\int B(\lambda_qx,k/\lambda_q),dx\,
    \lambda_q\sum_{n\in\mathbb Z}\delta_{\lambda_qn}(dk).
\tag{111.H15}
\]

The source measure instead contains
\(\sum_n\delta_n(dk)\).  Distributionally,

\[
 \lambda_q\sum_n\delta_{\lambda_qn}(k)
 =\sum_{r\in\mathbb Z}e(rk/\lambda_q),
 \qquad
 \sum_n\delta_n(k)=\sum_{r\in\mathbb Z}e(rk).
\tag{111.H16}
\]

The zero-frequency densities agree, as they must from
\(|\det DT_q|=1\), but every nonzero discrepancy frequency remains with
unit coefficient.  There is no visible \(1/q\) multiplier.

More strongly, let \(I\subset(0,\infty)\) have length \(K\) and lie in
a common-interior dual interval.  Put

\[
 \mu_I=1_I\sum_n\delta_n,
 \qquad
 \nu_{I,\lambda}=1_I\lambda\sum_n\delta_{\lambda n}.
\]

If \(\lambda\) is irrational, the two supports have no common point in
\(I\), and

\[
 \|\mu_I-\nu_{I,\lambda}\|_{\mathrm{TV}}=2K+O(1).
\tag{111.H17}
\]

If \(\lambda=p/r<1\) in lowest terms, the common support is \(p\mathbb Z\).
There are \(K/p+O(1)\) common atoms, with weights \(1\) and \(p/r\), so

\[
 \|\mu_I-\nu_{I,\lambda}\|_{\mathrm{TV}}
 =2K-{2K\over r}+O(1)\asymp K.
\tag{111.H18}
\]

Here \(r\ge2\), because \(\lambda<1\).  Thus closeness of \(\lambda\) to
one does not make the atomic comb close in total variation.  The same
argument applies directly to the physical \(m\)-comb if the comparison is
made before Poisson completion.  Alternatively, rounding \(k/\lambda_q\)
to an integer restores an integer index but loses the exact \(kx\) phase:
the residual is

\[
 (\lfloor k/\lambda_q\rceil-k/\lambda_q)\lambda_qx,
\]

which has no small uniform size on \(x\asymp gA\).  Exact phase
preservation and exact preservation of both integer lattices are therefore
incompatible unless \(\lambda_q=1\), which never holds for adjacent
\(q\).

The endpoint calculation is separate from this bulk comb defect.  From
(111.H11), the transported lower dual endpoint lies above the literal
neighbor lower endpoint by

\[
 \theta_q^2\alpha_q-\theta_q\alpha_q
 =\theta_q\varepsilon_q\alpha_q,
\tag{111.H19}
\]

and the transported upper endpoint lies above the literal neighbor upper
endpoint by

\[
 \theta_q^2\beta_q
 -\theta_q\beta_q\sqrt{b\over b+2}
 =\theta_q\beta_q
  \left(\theta_q-\sqrt{b\over b+2}\right).
\tag{111.H20}
\]

Both quantities are \(\asymp K/q\asymp J/A\).  Thus, away from the
collapsing cone edge, each endpoint slab contains \(\asymp J/A\) integer
modes, up to the inherited open-endpoint and star conventions.  Near the
collapsing edge the common interval can become empty or singleton; that is
a separate jump, not an improvement.  Comparing \(J/A\) with the accepted
\(K/L\) curvature width proves (111.H3).  In particular, for \(D<L\) an
adjacent step crosses more than a bounded number of fixed collars, while
for \(D\asymp L\) it crosses order one and yields no polynomial saving.

On the physical side, (111.H12) and the target interval give, when the
two intervals overlap, the exact lower and upper mismatch widths

\[
 B_-={g\over4}\{(b+2)-\lambda_qb\}
 ={g\over4}\{2+b(1-\lambda_q)\},
 \qquad
 B_+=ga(1-\lambda_q).
\tag{111.H21}
\]

They are both \(\asymp gA/q\asymp L/D\); if there is no overlap, the
defect is larger.  Before transport, the lower ceiling jump follows by
checking the two possible residues \(gb\equiv1,3\pmod4\): adding \(2g\)
changes the ceiling by \((g-1)/2\) in the first case and \((g+1)/2\) in
the second.  This is exactly (111.H4).

These widths explain why the apparent \(1/q\) is not a saved power.
Away from the cone cusp, a row has phase-space capacity on the scale

\[
 V_q\asymp (gA)K.
\]

Either a physical slab of width \(gA/q\) across the full \(k\)-range or a
dual slab of width \(K/q\) across the full physical range has capacity
\(\asymp V_q/q\).  There are \(\asymp D\) adjacent indices in a cell
\(q\asymp D\), so summing those atoms absolutely has capacity
\(\asymp V_q\).  The bulk comb estimate (111.H17)--(111.H18) is stronger:
without a regularity or cancellation norm it already has full capacity on
each common interior.

The remaining arithmetic jumps are also interior, not endpoint-only.
Since \(a\) is odd,

\[
 1_{(a,a+2q)=1}=1_{(a,q)=1}
 =\sum_{d\mid a}\mu(d)1_{d\mid q},
\tag{111.H22}
\]

and hence the adjacent mask difference is

\[
 \sum_{d\mid a}\mu(d)
 \{1_{d\mid q}-1_{d\mid q+1}\}.
\tag{111.H23}
\]

For every odd prime divisor of \(a\), its two residue transitions recur
throughout the \(q\)-interval.  Möbius inversion preserves
\((-1)^q\) on the progression \(q=du\), because \(d\) is odd, but it does
not make (111.H23) a boundary term.  Likewise, lift births/deaths, height
floors, reciprocal equalities, moving collars, stars, and metric point
atoms can coincide on one tuple.  A lawful decomposition must first take
the common intersection and full symmetric difference of the literal
tuple supports, or impose an explicit priority order.  Merely listing the
jump types double counts their intersections.

Continuous transport does preserve an exact metric centre:
\(\Lambda_{q+1}/(k/\lambda_q)=\Lambda_q/k\).  Discrete transport does not
map an integer centre mode to an admissible integer mode in general.
Consequently the punctured exact-centre atom, terminal member, density,
and discrepancy modes stay inside the sampling commutator; none may be
deleted before the combs are compared.

Finally, the hostile structured controls reject attempts to estimate the
slabs by a uniform phase gap.  At the upper reciprocal corner the assigned
Round-105 identity is

\[
 {\Lambda_q'\over k_+(q)}=J.
\tag{111.H24}
\]

For \(X=T^4\), \(J=T^2\in\mathbb Z\), and the odd complete metric modes
can have integral boundary derivative.  The exact point is open and
collarized, and square rays are prior-owned, so this is a method falsifier,
not a residual lower bound.  Pell and near-square choices similarly rule
out importing a uniform Diophantine separation for the lattice or metric
centres, but no Pell family here proves a lower bound for the complete
actual coefficient.  A bounded phase-conjugating coefficient placed on
the sign of \(\mu_I-\nu_{I,\lambda}\) attains the total variation in
(111.H17)--(111.H18); this falsifies coefficient-blind savings only and is
not the Vaaler/profile symbol.

## 4. First doubtful or unproved step

The first unsupported step is the phrase "define the transported neighbor
on the common interior."  The candidate specifies the continuous map
\(T_q\), but it does not specify an extension of the literal integer
coefficient to the noninteger set
\((\lambda_q\mathbb Z,\lambda_q^{-1}\mathbb Z)\), a sampling measure,
an interpolation rule, or the accompanying Jacobian factor.  Without that
data, \(\Delta_{\mathrm{transport}}F_{L,a}(q)\) is not a defined finite
scalar.

With the canonical continuous pullback, the exact normalization is
(111.H15), and the first resulting term is the full comb commutator

\[
 \sum_n\delta_n-\lambda_q\sum_n\delta_{\lambda_qn},
\tag{111.H25}
\]

not an \(O(1/q)\) error.  Replacing (111.H25) by endpoint insertions and
deletions omits the bulk resampling defect.  Replacing geometric transport
by integer rounding omits the residual phase.  Replacing the target
\(x\)-Jacobian by the visible factor \(\lambda_q\) while ignoring the
changed \(k\)-density creates a false gain.

Even after the lattice transport is defined, the candidate supplies no
one-count Boolean or priority decomposition for simultaneous coprimality,
lift, ceiling, reciprocal-support, collar, entry/exit, floor, star,
equality, terminal, and metric-centre jumps.  Equations (111.H19)--(111.H23)
show that these are not all fixed-size boundary collars.  No signed bound
for their union is proved.

Thus the first exact failed seam is the discrete transport normalization,
and the first analytic open seam after repairing it is cancellation in the
full actual-symbol comb-plus-jump vector.  The equal-capacity conclusion is
a route obstruction in coefficient-blind norms.  It is not an
actual-symbol lower bound for
\(\Re\sum_{a,q}(-1)^qF_{L,a}(q)\).

## 5. Required control test and outcome

| Control | Hostile test and outcome |
|---|---|
| `exact_parity_highpass_identity` | **Pass.** Zero extension gives (111.H13).  At the energy level \(2\Re C=\Re\sum(-1)^q(I-S)F(q)\); no extra factor or orientation is available. |
| `signed_commutator_vs_total_variation_and_Gram` | **Pass as a separation.** Total variation is sufficient and strictly stronger.  An alternating finite row is amplified by \(I-S\), while cancelling blocks or imaginary mass separate the one-sided scalar from modulus, blockwise mass, and Gram energy. |
| `phase_preserving_transport_and_Jacobian` | **Pass.** Equations (111.H7)--(111.H9) are exact and \(|\det DT_q|=1\).  There is no continuous volume gain. |
| `distribution_normalization_under_T` | **Fail for the undeclared candidate transport; repaired by (111.H15).** The \(x\)-Jacobian \(\lambda_q\) is paired with the pulled-back \(k\)-comb of spacing \(\lambda_q\).  Ignoring either factor changes the scalar. |
| `rational_and_irrational_comb_intersections` | **Equal-capacity route obstruction.** Equations (111.H17)--(111.H18) give TV \(\asymp K\) for every \(\lambda_q\ne1\), however close it is to one.  The lattice defect is bulk, not boundary-supported. |
| `integer_rounding_alternative` | **Fail.** Rounding maps to integers but destroys exact \(kx\) preservation by a residual of size \(x\) times a bounded noninteger error.  No accepted oscillatory estimate controls it. |
| `dual_support_entry_exit` | **Fail as a saved-power claim.** Both transported endpoints miss by \(\asymp K/q\asymp J/A\), and the common interval may collapse at the cone cusp. |
| `collar_scale` | **Fail as an ownership shortcut.** The endpoint displacement divided by the accepted \(K/L\) width is \(L/D\gtrsim1\).  It is polynomially large when \(D\) is polynomially below \(L\), and order one on the terminal line, never a proved polynomial saving. |
| `physical_hard_edge_and_ceiling` | **Exact falsifier found.** The transported slabs are (111.H21), and the raw ceiling jump is (111.H4).  Since \(W(1)=1\), they are not killed at the lower edge. |
| `coprimality_and_Mobius` | **Algebraic pass; variation shortcut fails.** Equations (111.H22)--(111.H23) preserve parity on odd divisor progressions but generate recurring interior jumps. |
| `lifts_floors_stars_and_jump_one_count` | **Not certified.** The candidate gives no disjoint priority dictionary.  Simultaneous causes must be assigned once by the full support symmetric difference or an explicit precedence rule. |
| `metric_centres_density_and_discrepancy` | **Continuous pass, discrete fail.** \(\Lambda/k\) is invariant under \(T_q\), but the transported centre generally lies off the integer lattice.  The exact-centre atom, terminal member, density, and all discrepancy modes remain coupled to (111.H25). |
| `q1_and_collapsing_edge` | **No favorable subrange.** For \(q=1\), \(1-\lambda_q\) is order one and the transport can move an entire fibre.  Near \(b=4a\), common reciprocal and physical interiors can be empty or singleton. |
| `fourth_power_control` | **Uniform derivative-gap route rejected.** Equation (111.H24) is integral when \(X=T^4\).  Openness, collars, and prior square ownership prevent promotion to an actual lower bound. |
| `Pell_and_near_centres` | **Method control only.** Near-commensurable square-root data forbid a uniform Diophantine gap, but no complete actual-symbol lower bound or strict subrange is obtained. |
| `false_unsigned_and_phase_conjugating_coefficients` | **False analogue rejected.** Such coefficients attain the comb TV and can neutralize parity.  They are not the actual collared Vaaler/profile coefficient and are used only to refute coefficient-blind estimates. |
| `capacity_gain_or_self_return` | **Equal capacity in the audited norm.** The continuous map is measure preserving; bulk comb TV is \(\asymp K\); absolute endpoint accumulation restores the original phase-space capacity.  Cancellation on the actual signed vector remains open. |
| `primary_source_hypothesis_map` | **No external theorem invoked.** Before any theorem can apply, the candidate would need a fixed interpolation/sampling operator, a common Banach norm, and literal control of every moving arithmetic and support jump.  Those hypotheses are absent, and the exact comb calculation already falsifies smallness in total variation.  Reapplying Poisson only rewrites (111.H16) and is invertible. |
| `downstream_and_exponent_scope` | **Pass.** No one-sided completed scalar estimate, fixed-\(a\) Gram, hard-cone theorem, smooth M2 packet, \(M9\! -\! M2\), \(M9\! -\! M1\), endpoint theorem, \(M9\), conditional bridge, or exponent improvement is proved. |

No numerical experiment was performed.  The controls are exact finite
algebra, distribution normalization, support arithmetic, and capacity
bookkeeping.

## 6. Dependencies and exact artifacts used

The assigned context was read and used:

- `protocol.md`;
- `state/proof_obligations.yml`, in particular the three Round-111 target
  nodes, the Round-110 self-return, and the current rejection ledger;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m2-adjacent-ray-transport-commutator/derivation_packet.md`;
- `rounds/codex-managed/m9-m2-adjacent-ray-transport-commutator/candidates/conductor_adjacent_transport_commutator.md`;
- `rounds/codex-managed/m9-m2-global-signed-completed-directional/reports/completed_directional_hostile_audit.md`;
- `rounds/codex-managed/m9-m2-polynomial-q-maximal-alternation/reports/maximal_q_hostile_source_audit.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/reports/centered_integral_variation_attack.md`;
- `rounds/codex-managed/m9-m2-adjacent-ray-transport-commutator/briefs/adjacent_commutator_hostile_source_audit.md`.

No Round-111 sibling report, proof draft, validation matrix, shared
synthesis, external source, web result, or computational artifact was
used.  No primary source was invoked: the literal discrete transport fails
the hypothesis gate before a discrete commutator, sampling, variational,
large-sieve, or spectral theorem can be mapped to it.  Apart from this
assigned report, no campaign artifact or shared state was edited.

## 7. Recommended state effect

**Promote narrowly, after conductor seam review, only the exact algebraic
and normalization interfaces:** the parity identity (111.H13), the
formulae (111.H6)--(111.H12), the determinant-one transport, the pulled-back
comb normalization (111.H15), the rational/irrational TV calculation
(111.H17)--(111.H18), the dual endpoint displacements
(111.H19)--(111.H20), the physical slabs (111.H21), and the exact ceiling
jump (111.H4).

**Record a scoped route no-go:** the assertion
"\(\lambda_q=1+O(1/q)\) makes the discrete adjacent commutator
\(O(1/q)\), boundary-supported, or polynomially smaller" is false in
coefficient-blind and total-variation norms.  The continuous Jacobian is
one, the atomic comb defect has full \(K\)-capacity, the endpoint shifts
cross \(L/D\) collar widths, and absolute accumulation of jump slabs
restores the original capacity.  Replacing exact transport by rounding
only moves the difficulty into an uncontrolled phase residual.

**Do not record an actual-symbol lower bound.**  Hard-edge, fourth-power,
Pell/near-centre, and phase-conjugating families reject uniform-gap and
coefficient-blind arguments, but the first three are affected by open
endpoints, collars, punctures, or prior owners, while the last is not the
actual coefficient.  Cancellation in the complete signed comb-plus-jump
vector is neither proved nor refuted.

Retain open the one-sided adjacent-ray estimate, the exact actual-symbol
transport commutator, every strict polynomial hard subrange, the canonical
density--discrepancy energy, the signed hard cone, both smooth M2 packets,
\(M9\! -\! M2\), \(M9\! -\! M1\), endpoint uniformity, \(M9\), the
conditional bridge, and the Gauss-circle target.  Make no exponent or
downstream status change.
