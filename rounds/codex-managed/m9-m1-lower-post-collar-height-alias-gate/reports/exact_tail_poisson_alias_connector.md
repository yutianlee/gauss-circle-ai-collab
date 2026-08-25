# Round 140 discovery report: exact post-collar Poisson connector

## 1. Result

**strict_height_alias_reduction**

There is an owner-complete route from the literal post-collar tail to one
smooth signed height--alias scalar. The hard endpoint must first be
displayed with its half weight; it cannot be silently replaced by the
interior stationary family. After that exact display, a second fixed
collar parameter may be used to smooth the endpoint at target-safe cost.
For either sign,

\[
 \boxed{\mathcal S_N^\pm
 =\mathcal P_{N,W}^\pm+O_{\rho,V}\!\left(R\log^3(2X)\right),}
\tag{140.1}
\]

where \(\mathcal P_{N,W}^-=\overline{\mathcal P_{N,W}^+}\) and

\[
 \begin{split}
 \mathcal P_{N,W}^+
 ={}&e(-1/8)N^{1/4}
 \sum_{h\geq1}\sum_{\substack{r\geq1\\r\ {\rm odd}}}
 \chi_4(r)(hr)^{-3/4}
 V_{\rm low}\!\left({R^2hr\over N}\right)\\
 &\qquad\qquad\cdot
 W\!\left(
 \sqrt h\left(1-{2\sqrt{Nh/r}\over y}\right)\right)
 e\!\left(\sqrt{Nhr}\right).
 \end{split}
\tag{140.2}
\]

Here \(W\) is a fixed smooth step which is zero up to the original
collar parameter \(\rho\) and one after a second parameter
\(\rho_1\in(\rho,1/8)\). Every discarded term in (140.1) is
\(RX^\varepsilon\)-safe. Thus (140.2), rather than a principal-only
formula for the literal hard interval, is a strict signed survivor
equivalent to the target.

The target estimate for (140.2) is not proved. Its phase has a rank-one
Hessian, its exact product fibres have no height phase at all, and the
height weight cancels under the exact substitution \(x=hz\). Reindexing
\(m=hr\) gives

\[
 \mathcal P_{N,W}^+
 =e(-1/8)N^{1/4}
 \sum_{m\geq1}m^{-3/4}
 V_{\rm low}\!\left({R^2m\over N}\right)
 B_W(m)e(\sqrt{Nm}),
\tag{140.3}
\]

\[
 B_W(m)=
 \sum_{\substack{h\mid m\\m/h\ {\rm odd}}}
 \chi_4(m/h)\,
 W\!\left(
 \sqrt h\left(1-{2h\sqrt N\over y\sqrt m}\right)\right).
\tag{140.4}
\]

The coefficient-blind capacity of (140.3) is
\(R^{3/2+o(1)}\), still \(R^{1/2}\) above target. Exact radical modes are
target-safe, but near radicals and the aggregate of product fibres remain
open. This is the first rigorous joint-sum obstruction: ordinary
two-dimensional curvature and independent height cancellation are both
unavailable.

## 2. Exact statement and hypotheses

Let

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad
 N=\lfloor X\rfloor=y^2+q,\qquad 0\leq q\leq2y,
\]

fix \(0<\rho<1/8\), and put

\[
 L_h=\left\lfloor{\rho y\over\sqrt h}\right\rfloor,\qquad
 a_h=L_h+1,\qquad D_h=y-a_h.
\tag{140.5}
\]

The supplied profile is fixed, real and smooth, is zero for sufficiently
large argument, and has its literal endpoint values and near-zero
plateau. In particular a nonzero physical sample forces
\(h\leq C_Vd/R\). Therefore all height sums below are finite, with
\(h\leq H_V:=\lfloor C_Vy/R\rfloor\). If \(y=1\), then \(D_h=0\) and
the literal tail is empty. If \(y\geq2\), then \(D_h\geq1\). No
asymptotic argument is needed for the finitely many remaining small
values of \(y\).

For the positive sign define

\[
 T_h^+={1\over h}\sum_{1\leq d\leq D_h}
 \chi_4(d)V_{\rm low}\!\left({4R^2h^2\over d^2}\right)e(Nh/d),
\qquad
 \mathcal S_N^+=\sum_hT_h^+.
\tag{140.6}
\]

The negative scalar is its conjugate. Put

\[
 A_h(x)=V_{\rm low}\!\left({4R^2h^2\over x^2}\right)
\quad (x>0),
\]

with the literal zero extension at \(x\leq0\). Poisson summation on the
inclusive hard interval, using symmetric summation in each branch, gives
the exact identity below when \(D_h\geq1\). When \(D_h=0\), the whole
right-hand side is defined to be zero before any \(D_h\)-dependent
factor is evaluated:

\[
 \begin{split}
 T_h^+
 ={}&{\mathbf 1_{D_h\geq1}\over2h}\,
 \chi_4(D_h)A_h(D_h)e(Nh/D_h)\\
 &+{1\over2ih}\sum_{\tau=\pm1}\tau
 \lim_{K\to\infty}\sum_{|k|\leq K}
 \int_0^{D_h}A_h(x)
 e\!\left({Nh\over x}+\left({\tau\over4}-k\right)x\right)\,dx .
 \end{split}
\tag{140.7}
\]

The first line is the literal half-endpoint correction. The lower
endpoint contributes zero. Formula (140.7) retains both mod-four
branches; it follows from

\[
 \chi_4(d)={e(d/4)-e(-d/4)\over2i}.
\]

With

\[
 r=\tau-4k,
\tag{140.8}
\]

the branch and integer are in bijection with odd \(r\), and
\(\tau=\chi_4(r)\). Any \(r\)-sum representing (140.7) is understood
in the induced branchwise symmetric order, not as an unlicensed
absolutely convergent rearrangement.

For \(r>0\), the phase

\[
 \phi_{h,r}(x)={Nh\over x}+{rx\over4}
\]

has the unique stationary point

\[
 x_{h,r}=2\sqrt{Nh/r},\qquad
 \phi_{h,r}(x_{h,r})=\sqrt{Nhr},\qquad
 \phi_{h,r}''(x_{h,r})={r^{3/2}\over4(Nh)^{1/2}}.
\tag{140.9}
\]

The exact literal entry condition is

\[
 r\geq r_0(h):={4Nh\over D_h^2}.
\tag{140.10}
\]

Writing \(r=4h+s\), where \(s\) is odd, gives

\[
 s\geq\vartheta_h,\qquad
 \vartheta_h={4h(N-D_h^2)\over D_h^2}
 ={4h(2a_hy-a_h^2+q)\over(y-a_h)^2}.
\tag{140.11}
\]

Let \(r_h\) be the least positive odd integer with
\(r_h\geq r_0(h)\). Equality \(r_h=r_0(h)\) is an endpoint stationary
mode, not an interior mode. The two adjacent odd modes
\(r_h-2,r_h\) contain every possible incomplete-Fresnel endpoint
transition. Since

\[
 \phi_{h,r}''(D_h)={2Nh\over D_h^3}\asymp_\rho {h\over y},
\tag{140.12}
\]

the transition width in the \(r\)-coordinate is
\[
 |r-r_0(h)|\asymp
 \sqrt{\,2Nh/D_h^3\,}\asymp_\rho\sqrt{h/y}<1
\tag{140.13}
\]
for all sufficiently large active \(X\). A second-derivative integral
bound gives each of these at most
\(O_\rho(\sqrt{y/h})\); their complete weighted height sum is
\(O_\rho(R)\). For \(r\geq r_h+2\), the saddle is
\(\gg_\rho\sqrt{y/h}\) Gaussian widths below \(D_h\).

The floor and \(q\) ledger in (140.11) is uniform. Since
\[
 {\rho y\over\sqrt h}<a_h\leq{\rho y\over\sqrt h}+1,
\tag{140.14}
\]
one has, for \(y\geq16\),
\[
 4\rho\sqrt h<\vartheta_h
 \leq13\rho\sqrt h+{26h\over y}.
\tag{140.15}
\]
Indeed \(D_h\geq13y/16\),
\(N-D_h^2\leq2y(a_h+1)\), and
\(N-D_h^2\geq a_hy\). On active heights \(h\ll R\), the final term is
\(O(R^{-1})\). At \(q=0\) the same inequalities hold; replacing
\(q=0\) by \(q=2y\) changes \(\vartheta_h\) by exactly
\[
 {8hy\over D_h^2}=O_\rho(h/y).
\tag{140.16}
\]
Thus the heuristic \(s\asymp\sqrt h\) is now an exact floor-uniform
statement, while (140.11), not the heuristic, owns equality cases.

## 3. Proof or derivation

Choose once and for all

\[
 \rho_1={\rho+1/8\over2}\in(\rho,1/8)
\]

and a fixed \(W\in C^\infty(\mathbb R)\) such that
\[
 0\leq W\leq1,\qquad
 W(u)=0\ (u\leq\rho),\qquad
 W(u)=1\ (u\geq\rho_1).
\tag{140.17}
\]
Define the smooth physical tail
\[
 \widetilde{\mathcal S}_N^+
 =\sum_{h\geq1}{1\over h}\sum_{d\geq1}
 \chi_4(d)V_{\rm low}\!\left({4R^2h^2\over d^2}\right)
 W\!\left({(y-d)\sqrt h\over y}\right)e(Nh/d).
\tag{140.18}
\]

There are no new samples beyond the literal interval: if \(d>D_h\),
then \(y-d\leq L_h\), so the argument of \(W\) is at most \(\rho\).
On the other hand, the difference
\(\mathcal S_N^+-\widetilde{\mathcal S}_N^+\) is supported where
\[
 L_h<y-d<{\rho_1y\over\sqrt h}.
\tag{140.19}
\]
Every integer in (140.19) lies in the \(\rho_1\)-curvature collar.
The extra factor \(1-W\) has uniformly bounded sampled variation. The
exact Round-139 second-derivative argument therefore applies without a
new endpoint loss and gives
\[
 \mathcal S_N^\pm-\widetilde{\mathcal S}_N^\pm
 \ll_{\rho,V}R\log(2X).
\tag{140.20}
\]
This is the only noninvertible step in the derivation.

For real \(x\), set
\[
 A_{h,W}(x)=
 V_{\rm low}\!\left({4R^2h^2\over x^2}\right)
 W\!\left({(y-x)\sqrt h\over y}\right),
\tag{140.21}
\]
with zero extension. It is smooth and compactly supported inside
\((0,y)\): the profile kills the lower endpoint and \(W\) kills a
neighborhood of the upper endpoint. Hence ordinary Poisson summation
has no half-endpoint and is absolutely convergent after any fixed number
of integrations by parts:
\[
 \widetilde{\mathcal S}_N^+
 ={1\over2i}\sum_{h\leq H_V}{1\over h}
 \sum_{\substack{r\in\mathbb Z\\r\ {\rm odd}}}\chi_4(r)
 \int_0^\infty A_{h,W}(x)
 e\!\left({Nh\over x}+{rx\over4}\right)\,dx .
\tag{140.22}
\]
Thus the hard half-endpoint and its conditionally summed dual boundary
tail have not been dropped: they were first retained in (140.7), and
then the complete hard-to-smooth difference was estimated in (140.20).

For completeness, the one-dimensional transformation used on (140.22)
is the following elementary smooth \(B\)-process lemma in the present
normalization:
\[
 \begin{split}
 &{1\over2ih}\sum_{\substack{r\in\mathbb Z\\r\ {\rm odd}}}\chi_4(r)
 \int_0^\infty A_{h,W}(x)e(\phi_{h,r}(x))\,dx\\
 &\quad =
 e(-1/8)N^{1/4}
 \sum_{\substack{r\geq1\\r\ {\rm odd}}}\chi_4(r)(hr)^{-3/4}
 A_{h,W}(x_{h,r})e(\sqrt{Nhr})
 +O_{\rho,V}\!\left({\log^2(2X)\over h}\right).
 \end{split}
\tag{140.23}
\]

Here every \(r\leq0\), every positive nonstationary mode, every profile
crossing, and every stationary remainder belongs to the displayed error.
To prove (140.23), take a smooth dyadic partition \(x\asymp Z\) of the
support. On one block,
\[
 \phi''\asymp {Nh\over Z^3},\qquad
 w_Z:=(\phi'')^{-1/2}\asymp\left({Z^3\over Nh}\right)^{1/2}.
\tag{140.24}
\]
For each derivative alias whose stationary point lies in the block,
isolate \(|x-x_{h,r}|\ll w_Z\). Taylor expansion there has cubic
parameter
\[
 {Nh\over Z^4}w_Z^3\ll\sqrt{Z\over Nh}
 \leq {1\over\sqrt{yh}},
\tag{140.25}
\]
and the profile varies by \(O(w_Z/Z)\). The new smooth cutoff varies by
\[
 O\!\left({\sqrt h\over y}w_Z\right)
 \leq O(y^{-1/2}).
\tag{140.26}
\]
The Gaussian integral is therefore uniform, including every profile and
smooth-cutoff crossing, and contributes
\[
 {e(1/8)\over\sqrt{\phi''(x_{h,r})}}\,
 A_{h,W}(x_{h,r})e(\sqrt{Nhr}).
\tag{140.27}
\]
The number of stationary aliases on the block is
\(O(1+Nh/Z^2)\); multiplying this count by the Taylor remainders from
(140.25)--(140.26) gives \(O_{\rho,V}(1)\) per block.

Off the stationary neighborhoods, \(\phi'\) is monotone. One
integration by parts and summation over the distance to the nearest odd
alias gives \(O(\log(2X))\) on a block. Smooth vanishing at both physical
ends removes the \(1/r\) hard-boundary series which made (140.7) only
branchwise symmetric. There are \(O(\log(2X))\) blocks, proving the
error in (140.23). Finally,
\[
 {1\over\sqrt{\phi''(x_{h,r})}}
 =2(Nh)^{1/4}r^{-3/4},
\]
and \((2i)^{-1}\cdot2e(1/8)=e(-1/8)\), which proves the constant.

At the stationary point,
\[
 A_{h,W}(x_{h,r})
 =V_{\rm low}\!\left({R^2hr\over N}\right)
 W\!\left(
 \sqrt h\left(1-{2\sqrt{Nh/r}\over y}\right)\right).
\tag{140.28}
\]
Summing (140.23) over \(h\leq H_V\) costs only
\(O_{\rho,V}(\log^3(2X))\). Combining this with (140.20) proves
(140.1)--(140.2), including the conjugate sign.

The smooth stationary multiplier has an exact alias-offset ledger. For
\(\eta\in\{\rho,\rho_1\}\), put
\[
 \Theta_\eta(h)
 =4h\left\{
 {1+q/y^2\over(1-\eta/\sqrt h)^2}-1
 \right\}
 ={8\eta\sqrt h-4\eta^2+4hq/y^2
 \over(1-\eta/\sqrt h)^2}.
\tag{140.29}
\]
Then the multiplier in (140.28) is zero unless
\(s=r-4h>\Theta_\rho(h)\), and it is one in its cutoff coordinate once
\(s\geq\Theta_{\rho_1}(h)\). These are real smooth thresholds; the
literal integer and equality owner remains (140.11). Their discrepancy
is only the already-priced collar (140.20), not an omitted endpoint
term.

The exact product geometry is visible even before stationary phase.
With \(m=hr\) and \(x=hz\),
\[
 {1\over h}\int_0^{D_h}A_h(x)
 e\!\left({Nh\over x}+{rx\over4}\right)\,dx
 =
 \int_0^{D_h/h}V_{\rm low}\!\left({4R^2\over z^2}\right)
 e\!\left({N\over z}+{mz\over4}\right)\,dz .
\tag{140.30}
\]
The \(h^{-1}\) weight cancels exactly; only the height-dependent endpoint
remembers \(h\). In the smooth principal family, reindexing \(m=hr\)
is finite because the profile forces \(m\ll N/R^2\ll y\), and gives
(140.3)--(140.4).

## 4. First doubtful or unproved step

The first unproved estimate is precisely
\[
 \boxed{|\mathcal P_{N,W}^\pm|
 \ll_\varepsilon RX^\varepsilon.}
\tag{140.31}
\]
This is equivalent to the literal tail target by (140.1), but it does
not follow from two-dimensional curvature.

For
\[
 F(h,r)=\sqrt{Nhr},
\]
one has
\[
 \nabla^2F={\sqrt N\over4}
 \begin{pmatrix}
 -r^{1/2}h^{-3/2}&(hr)^{-1/2}\\
 (hr)^{-1/2}&-h^{1/2}r^{-3/2}
 \end{pmatrix},
\qquad
 \det\nabla^2F=0.
\tag{140.32}
\]
Euler homogeneity gives
\(\nabla^2F\,(h,r)^{\mathsf T}=0\). Along every rational ray
\((h,r)=\ell(a,b)\),
\[
 F(\ell a,\ell b)=\ell\sqrt{Nab},
\tag{140.33}
\]
so exact coherent rays occur whenever \(Nab\) is a square.

This is not merely a differential warning. If \(N=M^4\) with \(M\)
odd, take \(a=1,b=9\), \(h=\ell,r=9\ell\), and
\(\ell\equiv1\pmod4\). Then
\[
 e(\sqrt{Nhr})=1,\qquad
 W\!\left(\sqrt\ell/3\right)=1
\]
after a fixed initial segment, \(\chi_4(r)=1\), and the profile is on its
plateau for \(\ell\leq cM\). This subray is coherently signed. Its absolute
principal mass is \(O(R)\), so it does not refute the target, but it
does refute any appeal to a nondegenerate two-variable Hessian or
automatic cancellation along rays.

Product fibres are an independent exact degeneracy. If the smooth
cutoff in (140.4) were identically one, then
\[
 \sum_{\substack{h\mid m\\m/h\ {\rm odd}}}\chi_4(m/h)
 =\sum_{r\mid m}\chi_4(r)={r_2(m)\over4}\geq0.
\tag{140.34}
\]
The actual cutoff does not restore uniform character cancellation. At
the same fourth-power centres, let \(m=p^{2a}\) with
\(p\equiv1\pmod4\), \(p\geq5\). For the factor pairs
\[
 h=p^{2a-j},\qquad r=p^j,\qquad a+1\leq j\leq2a,
\]
the cutoff argument in (140.4) is at least
\(\sqrt h(1-2/p)>\rho_1\), while all factors on the opposite side of
the square root have negative cutoff argument. Hence
\[
 B_W(p^{2a})=a,
\qquad e(\sqrt{Np^{2a}})=1.
\tag{140.35}
\]
Thus height aggregation can be positive and divisor-sized on literal
product fibres.

The complete coefficient-blind ledger is
\[
 |\mathcal P_{N,W}^+|
 \leq N^{1/4}\sum_{m\ll N/R^2}
 m^{-3/4}\tau(m)
 \ll_\varepsilon R^{3/2}X^\varepsilon.
\tag{140.36}
\]
It loses \(R^{1/2}\) against (140.31). Exact radicals do not account for
this loss. Write \(N=Du^2\) with \(D\) squarefree. Then
\(e(\sqrt{Nm})=1\) exactly only when \(m=Dt^2\), and
\[
 N^{1/4}\sum_{t\ll R/\sqrt D}
 (Dt^2)^{-3/4}|B_W(Dt^2)|
 \ll_\varepsilon RD^{-3/4}X^\varepsilon.
\tag{140.37}
\]
The first genuinely open arithmetic step is a uniform signed estimate
for the nonsquare and near-radical part of (140.3), including its
incomplete divisor coefficient \(B_W(m)\). Grouping by \(m\) and taking
moduli returns (140.36); applying a second \(B\)-process self-returns,
because the Legendre stationary point of
\[
 \sqrt{Nm}-{mz\over4}
\]
is \(m=4N/z^2\), and the stationary value is \(N/z\), the original
reciprocal phase.

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| exact_tail_cutoff_floor_empty_rows_and_both_signs | Equations (140.5)--(140.6) retain the literal floor. \(y=1\) is the only empty-\(D_h\) case; \(y\geq2\) has \(D_h\geq1\). The negative scalar is kept as the exact conjugate. |
| mod_four_character_poisson_branches | Equation (140.7) keeps \(\tau=\pm1\) separately with symmetric \(k\)-limits. Equation (140.8) is a bijection to odd \(r\), with \(\tau=\chi_4(r)\). |
| hard_endpoint_half_weight_and_zero_extension | The half-endpoint is the first line of (140.7), and the lower zero extension is explicit. Smoothing occurs only after the complete difference is bounded in (140.20). |
| stationary_entry_offset_s_exact_floor_q_ledger | Equations (140.10)--(140.16) give the exact threshold, least odd alias, equality case, floor inequalities, and the \(q=0\) to \(q=2y\) change. |
| profile_stationary_entry_exit_and_crossings | The exact hard transition modes are \(r_h-2,r_h\) and are \(O(R)\) in total. In the smooth connector every entry, exit, and profile crossing is retained by the two literal multipliers in (140.28); smooth flatness removes any unowned hard crossing. |
| nonstationary_transition_and_remainder_owner_ledger | All nonstationary modes and stationary remainders are included in the proved error of (140.23); the hard endpoint transition is priced separately by (140.12)--(140.13), and the total errors give (140.1). |
| joint_phase_Hessian_rank_and_rational_rays | The Hessian determinant vanishes identically in (140.32). The ray \((h,r)=(\ell,9\ell)\) at odd fourth powers is an exact coherent control. |
| product_fibre_exact_and_near_radical_controls | Equations (140.30), (140.34), and (140.35) show exact phase constancy and failure of uniform height-character cancellation. Equation (140.37) bounds the unique exact radical channel; near radicals remain open. |
| height_weight_dyadic_capacity_and_target_return | The substitution \(x=hz\) cancels \(h^{-1}\) exactly. Equation (140.36) is the \(R^{3/2+o(1)}\) survivor capacity, versus target \(R\); every discarded owner is \(RX^\varepsilon\)-safe. |
| fourth_power_q_zero_and_q_max_controls | The coherent ray and prime-square fibre use literal odd fourth powers with \(q=0\). Equation (140.16) proves that \(q=2y\) perturbs entry by only \(O(h/y)\). |
| transform_noninvertibility_and_self_return | The only noninvertible operation is the proved collar replacement (140.20). Poisson, \(m=hr\), and the \(B\)-process are invertible; the displayed Legendre calculation returns \(N/z\). |
| round138_residual_directionality_and_downstream_scope | Equation (140.1) is scalar target equivalence only. It supplies no identity for \(|\mathcal S_N|^2\), no collar--tail cross-term bound, and no deletion from the Round-138 residual. |

All tests are analytic. No numerical experiment, centre average,
probabilistic model, external source, or desired circle estimate is used.

## 6. Dependencies and exact artifacts used

This report uses exactly the assigned brief and the permitted context:

- protocol.md;
- state/proof_obligations.yml, restricted to the three active
  obligations and their stated directionality;
- state/active_campaign.yml;
- strategy/conductor_0823_full_proof_strategy.md;
- rounds/codex-managed/m9-m1-lower-gar-signed-farey-scalar-gate/reports/farey_scalar_self_return_hostile_audit.md;
- rounds/codex-managed/m9-m1-lower-gar-signed-farey-scalar-gate/synthesis.md;
- rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/candidates/conductor_round139_curvature_collar_and_quadratic_obstruction.md;
- rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/synthesis.md;
- rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/blind_statement.md;
- rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/briefs/exact_tail_poisson_alias_connector.md.

The only analytic inputs are Poisson summation with the stated endpoint
convention, elementary first- and second-derivative integral bounds, the
Gaussian stationary-phase calculation proved in (140.23)--(140.27), and
the already accepted Round-139 curvature-collar lemma.

## 7. Recommended state effect

Promote, after independent seam review, the strict reduction
(140.1)--(140.4): the literal hard tail is target-equivalent to the
smooth signed product-fibre scalar, with every endpoint, transition,
nonstationary, profile-crossing, and stationary-remainder owner priced.
Also retain (140.11)--(140.16) as the exact integer alias-entry
dictionary.

Record as an obstruction, not as a lower bound, that the survivor has
rank-one joint phase, exact coherent rays, divisor-sized positive product
fibres, and \(R^{3/2+o(1)}\) coefficient-blind capacity. Park any
nondegenerate two-dimensional Hessian argument, any independent
height-character saving, any principal-family modulus, and any second
transform advertised as a gain. The next legitimate objective is the
signed near-radical/nonsquare estimate for (140.3) with the exact
coefficient (140.4).

Retain as open the tail target, the full lower-radial signed estimate,
lower GAR, both direct M1 parents, M9-M1, all M2 parents, endpoint
uniformity, M9, the quarter theorem, and the Gauss-circle target. No
tail-square identity or exponent improvement follows from this report.
