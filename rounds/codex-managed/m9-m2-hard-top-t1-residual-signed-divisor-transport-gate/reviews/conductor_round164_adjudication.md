# Round 164 conductor adjudication

## 1. Result

Round 164 closes under

\[
 \boxed{\texttt{hard\_top\_t1\_residual\_transport\_no\_go}.}
\tag{164.A1}
\]

The complete residual target is not proved.  The selected durable result is
one proved-internal reduction:

M9-M2-hard-top-t1-residual-transport-fejer-energy-reduction.

It contains the exact residual Boolean and sign-mass algebra, the sharp
zero-extended unequal-mass BV dual bound, a selector-robust
coefficient-uniform positive-transport obstruction, and an endpoint-exact
sliding Fejer reduction to one open actual-coefficient short-shift theorem.

The no-go is route-scoped.  It parks coefficient-uniform positive
within-product transport, cemetery charging, bounded variation, and the
accepted positive rank-one collar.  It is not a lower bound for the literal
residual and does not disprove cancellation across distinct products.

## 2. Exact statement and hypotheses

Let \(J=\sqrt X\), \(y=\lfloor J\rfloor\), \(q_X=X/y^2\),
\(H=\lfloor yX^{-1/4}\rfloor\), and \(1\ll L\ll H\leq J^{1/2}\).
For a supported squarefree row

\[
 N=2^{\nu_N}M_N\asymp L^2,\qquad \nu_N\in\{0,1\},\qquad M_N
 \text{ odd},
\tag{164.A2}
\]

retain the complete literal hard-TOP \(t=1\) amplitude \(A_N(d)\), with
every profile, cone, half-open shell, parity branch, floor, star, point
value, endpoint, and zero extension.

If the accepted Round-163 selector is absent, put \(\rho_N(d)=1\) for
every \(d\mid M_N\).  If it selects \(p_N,q_N\), put

\[
 \rho_N(d)
 =1-\mathbf1_{p_N\mid d}-\mathbf1_{q_N\mid d}
 +2\mathbf1_{p_N\mid d}\mathbf1_{q_N\mid d}.
\tag{164.A3}
\]

This has values \((1,0,0,1)\) on the selected-prime bit patterns
\((00,10,01,11)\), exactly complementary to the accepted XOR sector.
Define

\[
\begin{aligned}
 b_N^{\rm rem}
 &=\sum_{d\mid M_N}\chi_4(d)\rho_N(d)A_N(d),\\
 c_N^{\rm rem}
 &=\mathbf1_{\mathcal I_L^{\rm lit}}(N)\mu^2(N)
   \left(\frac{L^2}{N}\right)^{3/4}b_N^{\rm rem},\\
 \mathcal S_{L,1}^{\rm rem}
 &=\sum_Nc_N^{\rm rem}e(J\sqrt N).
\end{aligned}
\tag{164.A4}
\]

The residual sign mass is

\[
 \sum_{d\mid M_N}\chi_4(d)\rho_N(d)
 =\begin{cases}
 \displaystyle\prod_{r\mid M_N}(1+\chi_4(r)),
      &\text{no pair selected},\\[5pt]
 \displaystyle(1+\chi_4(p_Nq_N))
   \prod_{\substack{r\mid M_N\\r\ne p_N,q_N}}
      (1+\chi_4(r))=0,
      &\text{a pair selected},
 \end{cases}
\tag{164.A5}
\]

where the products are over odd prime divisors.  Thus a selected residual
is ambient-balanced.  A no-pair residual is balanced if a
\(3\pmod4\) prime occurs and wholly positive otherwise.

Order the residual divisors as \(d_1<\cdots<d_r\), put
\(\sigma_i=\chi_4(d_i)\), \(C_j=\sum_{i\leq j}\sigma_i\), \(C_0=0\),
\(a_i=A_N(d_i)\), and \(a_0=a_{r+1}=0\).  Then

\[
 b_N^{\rm rem}
 =C_ra_r+\sum_{j<r}C_j(a_j-a_{j+1})
 =-\sum_{j=0}^{r}C_j(a_{j+1}-a_j),
\tag{164.A6}
\]

and, for the real literal amplitude,

\[
 \boxed{
 |b_N^{\rm rem}|
 \leq\frac12\operatorname{osc}(C_N)
       \sum_{j=0}^{r}|a_{j+1}-a_j|.}
\tag{164.A7}
\]

The sampled total variation \(V_N\) in (164.A7) is \(O(1)\).  The direct
literal BV/triangle target is the weighted estimate

\[
 \sum_N\operatorname{osc}(C_N)V_N
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{164.A8}
\]

The unweighted sum is only the envelope for a theorem uniform over all
bounded-variation profiles.

Let an integer interval of cardinality \(M_L\asymp L^2\) contain the
literal row shell, extend \(c_N^{\rm rem}\) by zero, set
\(z_N=c_N^{\rm rem}e(J\sqrt N)\), and take \(R=\lceil L\rceil\).  Define

\[
\begin{aligned}
 \mathfrak E_R^{\rm rem}
 &:={1\over R}\sum_{s\in\mathbb Z}
       \left|\sum_{j=0}^{R-1}z_{s+j}\right|^2\\
 &=\sum_N|c_N^{\rm rem}|^2
 +2\Re\sum_{1\leq r<R}\left(1-\frac rR\right)
   \sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
   e\!\left(\frac{Jr}{\sqrt{N+r}+\sqrt N}\right).
\end{aligned}
\tag{164.A9}
\]

Then

\[
 \boxed{
 |\mathcal S_{L,1}^{\rm rem}|^2
 \leq\frac{M_L+R-1}{R}\mathfrak E_R^{\rm rem}.}
\tag{164.A10}
\]

## 3. Proof and review synthesis

Equation (164.A3) is the exact Boolean complement of XOR, so Round 163 is
subtracted once and only once.  Multiplicativity proves (164.A5).  In the
selected branch, writing \(M_N=p_Nq_NR_N\) pairs \(a\mid R_N\) with
\(p_Nq_Na\), which reverses the character because
\(\chi_4(p_Nq_N)=-1\).  This residual pair has ratio \(p_Nq_N\geq15\);
the close \(p_Na\leftrightarrow q_Na\) displacement belongs wholly to the
removed XOR sector.

Telescoping proves (164.A6).  The zero-extended increments sum to zero, so
subtracting the midpoint of the range of \(C_j\) gives (164.A7) with the
sharp factor \(1/2\), without assuming equal total sign mass.  The
full-line regulated Stieltjes form has no extra terminal term and weights
incoming and outgoing point jumps by the left and inclusive cumulative
values respectively.  Fixed smooth profiles and finitely many literal hard
faces give \(V_N\ll1\).

The hostile audit chooses four odd primes of scale
\(P\asymp\sqrt L\), two in each odd residue class modulo four.  The three
physical two-prime partitions have signs \(\{+,-,-\}\).  With no selector
their unit-profile residual is \(-1\); with any selected opposite-character
pair, two partitions are XOR and the remaining neither/both partition is
negative.  The even construction preserves the factor \(2\) on the
complementary leg and has the same property.  The audited fixed-\(q=4\)
prime theorem gives

\[
 \gg\frac{L^2}{(\log L)^4}=L^{2-o(1)}
\tag{164.A11}
\]

diagnostic products.  This rejects the coefficient-uniform unweighted BV
envelope.  It is not a lower plateau for \(\eta_L\Phi W\) and not an
oscillatory lower bound.

For (164.A9), each pair at positive gap \(r<R\) occurs in exactly \(R-r\)
sliding windows.  Also every \(z_N\) occurs in exactly \(R\) windows, and
at most \(M_L+R-1\) window starts can meet the support.  Cauchy's inequality
therefore proves (164.A10) with no endpoint error.  The elementary divisor
bound, or the accepted hard-TOP energy, gives

\[
 \sum_N|c_N^{\rm rem}|^2
 \ll_\varepsilon L^2X^\varepsilon.
\tag{164.A12}
\]

Hence the residual target follows from the single one-sided open theorem

\[
 \boxed{
 \Re\sum_{1\leq r<R}\left(1-\frac rR\right)
 \sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
 e\!\left(\frac{Jr}{\sqrt{N+r}+\sqrt N}\right)
 \leq C_\varepsilon L^2X^\varepsilon.}
\tag{164.A13}
\]

Opening both supported squarefree rows gives exactly

\[
 N=dm,\qquad N+r=d'm',\qquad
 d'm'-dm=r,\qquad1\leq r<R\asymp L,
\tag{164.A14}
\]

with both selectors, parity branches, profiles, and square-root phase
retained.  Taking moduli leaves a positive additive-shift form.  It does
not literally become the separate multiplicative character-Poisson collar
\(\lvert s\ell-XQR\rvert\ll QRJ/L\); the two routes share only an adverse
positive-power warning.

The statement-only rederivation independently verified the Boolean,
sign-mass, Abel, BV, Fejer, endpoint, power, and product-shift algebra.  Its
post-unmask review found the original Stieltjes convention ambiguity,
\(M_L\)-scale omission, one-sided-inequality notation, and off-domain
selector ambiguity; all were repaired and reverified.  The independent
transport/profile/power/source review found the weighted-versus-unweighted,
additive-versus-multiplicative, Fejer-length, and Li--Yang/JNT source
wording seams; all were repaired and reverified.  The downstream graph
review certifies exactly one child, two inconclusive parent attachments,
twenty-three rejected overclaims, and twenty no-change decisions.

Round 164 used no numerical or symbolic experiment.

## 4. First doubtful or unproved step

The first unproved affirmative statement is exactly (164.A13), or any
weaker direct theorem implying
\(\mathfrak E_R^{\rm rem}\ll_\varepsilon L^2X^\varepsilon\).
It must use the actual residual coefficient and fail on phase-aligned
arbitrary arrays.  Coarse \(L^2\) energy, exact radical-collision sparsity,
positive transport, coefficient-uniform BV, shiftwise absolute values, and
the accepted rank-one collar do not prove it.

Even a proof of (164.A13) would close only the complete residual
\(t=1,D\asymp L^2\) face when combined with Round 163.  The compatible
\(L\ll D\ll L^2,\ t\ll\sqrt L\) channels and near collars would still
remain before hard TOP could close.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| one-time residual subtraction | Green: \((1,0,0,1)\) exactly complements XOR. |
| odd/even divisor universe | Green: \(d\) stays odd and the factor \(2\) stays in the complementary leg. |
| sign mass and unmatched atoms | Green: exact selected/no-pair dichotomy. |
| ordered Abel and terminal convention | Green: discrete identity plus full-line regulated form with no duplicate terminal term. |
| sharp BV duality | Green for unequal mass and every literal hard jump. |
| literal profile power | Green: \(V_N\ll1\); actual weighted target distinguished from the unweighted uniform envelope. |
| multiprime capacity | Green at coefficient-uniform diagnostic level only. |
| fixed-modulus source | Green for \(q=4\), reduced residues, fixed relative boxes above threshold. |
| outer phase | Green: retained in the aggregate short-shift correlation. |
| Fejer weights and endpoints | Green: \(1-r/R\) and \((M_L+R-1)/R\) are exact. |
| diagonal and \(R\)-scale | Green: \(M_L\asymp L^2\), \(R\asymp L\), and diagonal \(L^2\) give the target square. |
| additive versus multiplicative geometry | Green: compared by power warning only, never identified. |
| updated literature | Green as a dated listed-source scan with the five-repair Li--Yang narrow theorem retained. |
| downstream graph scope | Green: two open parents receive only dependency and inconclusive evidence. |
| computation | Not used. |

## 6. Dependencies and exact artifacts

The accepted kernel is
proofs/kernels/m9_m2_hard_top_t1_residual_transport_fejer_energy_reduction.md.

The five graph dependencies are:

1. M9-M2-hard-top-t1-close-opposite-prime-exchange-sector;
2. M9-M2-hard-top-truncated-divisor-energy-and-radical-control;
3. M9-M2-hard-top-t1-character-poisson-product-collar-obstruction;
4. M9-M2-top-endpoint-actual-symbol-variation; and
5. H4-Phi-regularity.

Primary reports:

- reports/complete_residual_transport_attack.md;
- reports/blind_residual_transport_rederivation.md; and
- reports/unmatched_transport_capacity_hostile_audit.md.

Independent reviews:

- reviews/blind_post_unmask_residual_fejer_review.md;
- reviews/blind_repair_verification.md;
- reviews/transport_capacity_profile_power_source_review.md;
- reviews/transport_source_repair_verification.md; and
- reviews/downstream_graph_state_scope_review.md.

Source and conductor controls:

- sources/bennett_martin_obryant_rechnitzer_2018.md;
- controls/conductor_round164_reproduction_and_selection.md; and
- controls/conductor_round164_updated_literature_scan.md.

## 7. State decision and next action

Create only the reduction node named in Section 1.  Attach it only as a
dependency and inconclusive evidence to
M9-M2-top-endpoint-signed-cone and
M9-M2-top-endpoint-density-discrepancy-energy.  Both remain open.

Record the twenty-three fresh rejected overclaims and twenty explicit
no-change decisions in the State Patch.  Preserve the residual target,
full \(t=1\) face, remaining channels, hard-TOP parents, both smooth M2
packets, physical assembly, M9--M2, M9--M1, endpoint uniformity, M9,
conditional bridge, quarter theorem, and both global exponent states.

After patch validation and application, the next objective is (164.A13)
in its aggregate one-sided actual direction.  Do not insert absolute values
around individual shifts, divisor openings, selector branches, or parity
branches before exploiting the residual arithmetic.

