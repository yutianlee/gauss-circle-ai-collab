# Formalized near-peak divisor-row Gram self-return and capacity obstruction

- Campaign: m9-m2-hard-top-t1-residual-k26-near-peak-row-gram-anticoncentration-gate
- Round: 180
- Role: conductor-requested finite candidate
- Starting graph: e94ef6a364988e47f8a59ca3589f03cb098a04a241ec841afc2efa6e685081b4
- Candidate label: row_gram_offdiagonal_capacity_or_self_return_no_go
- Evidence status: candidate pending conductor adjudication and State Patch
- Allocation: 100% analytical/algebraic; 0% numerical

## 1. Result

The following is the smallest durable Round-180 conclusion.

Let \(\mathcal E_\nu\) be the complete physical scalar energy in one
near-peak cell, \(\mathcal D_\nu\) its complete physical divisor-row
diagonal, and \(\mathcal G_\nu\) its one-outer-real-part cross-row form.
Then

\[
 \boxed{\mathcal E_\nu=\mathcal D_\nu+\mathcal G_\nu},
 \qquad
 0\le\mathcal D_\nu\ll_\varepsilon LX^\varepsilon.
 \tag{180.C1}
\]

Therefore, uniformly for \(|\nu|\le\lceil\sqrt L\rceil\),

\[
 \boxed{
 \mathcal G_\nu\ll_\varepsilon LX^\varepsilon
 \quad\Longleftrightarrow\quad
 \mathcal E_\nu\ll_\varepsilon LX^\varepsilon}
 \tag{180.C2}
\]

at one-sided target strength. The exact cross-row product-collision sector
is

\[
 \boxed{
 \mathcal P_\nu=\frac1M\sum_N
 \left\{(c_N^{\rm rem})^2-
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}\lambda_N(d)^2\right\}
 \ll_\varepsilon X^\varepsilon.}
 \tag{180.C3}
\]

Thus the first open theorem is the complete literal unequal-product bound

\[
 \boxed{
 \mathcal U_\nu:=\mathcal G_\nu-\mathcal P_\nu
 \ll_\varepsilon LX^\varepsilon
 \quad\text{uniformly for }
 |\nu|\le\lceil\sqrt L\rceil.}
 \tag{180.C4}
\]

Conditionally, (180.C4) implies

\[
 \mathfrak E_M^{(2)}\ll_\varepsilon L^3X^\varepsilon,
 \qquad
 Q_M^*\ll_\varepsilon L^3X^\varepsilon,
 \qquad
 T_{26}\ll_\varepsilon L^3X^\varepsilon,
 \tag{180.C5}
\]

and hence the one-sided K26 endpoint after the already accepted
ordinary-zero and once-only short-correction seams.

No proof of (180.C4) is supplied. Under only coefficient-uniform support,
energy, row length, parity, reality, character modulation, and hard-boundary
data, local positive capacity is \(L^2X^\varepsilon\) and central Fejer
endpoint capacity is \(L^4X^\varepsilon\). Both orders are attained by
explicit nonliteral coefficient shadows. This proves a route-scoped
self-return/capacity obstruction, not literal lower mass and not K26.

## 2. Exact statement, hypotheses, and provenance

Put

\[
 e(t)=e^{2\pi it},\qquad
 J=\sqrt X,\qquad
 1\ll L\ll H\le J^{1/2},\qquad
 R_0=\lceil L\rceil.
 \tag{180.C6}
\]

Let \(M\) be the exact cardinality of the containing integer interval, so
\(cL^2\le M\le CL^2\), and put \(K=\lceil\sqrt L\rceil\). The literal
coefficient \(\lambda_N(d)\in\mathbb R\) retains:

- the selected/no-pair Boolean field;
- the squarefree and coprimality projectors;
- both two-adic branches and both absolute-parity gauges;
- the near-square, Vaaler, and inherited profile factors;
- every floor, star, hard value, endpoint, transition, and support
  birth/death convention; and
- full-line zero extension.

The live products \(N=dm\) occupy the exact \(M\)-site interval and satisfy
\(N\asymp L^2\); live near-square incidences have \(d,m\asymp L\). Define

\[
 c_N^{\rm rem}
 =\sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi_4(d)\lambda_N(d),\qquad
 z_N=c_N^{\rm rem}e(J\sqrt N).
 \tag{180.C7}
\]

The exact rows and recombined sums are

\[
 \begin{aligned}
 R_{\epsilon,d}(\theta)
 &=\sum_m(-1)^{\epsilon m}\lambda_{dm}(d)
 e(J\sqrt{dm}+dm\theta),\\
 Z_\epsilon(\theta)
 &=\sum_{d\ {\rm odd}}\chi_4(d)R_{\epsilon,d}(\theta)
 =\sum_N(-1)^{\epsilon N}c_N^{\rm rem}
 e(J\sqrt N+N\theta).
 \end{aligned}
 \tag{180.C8}
\]

The last equality uses oddness of \(d\), hence
\((-1)^{\epsilon m}=(-1)^{\epsilon N}\) on \(N=dm\).

The incidence and recombined ledgers are distinct:

\[
 \begin{aligned}
 \#\Omega
 &:=\#\{(d,m):d\ {\rm odd},\lambda_{dm}(d)\ne0\}
 \ll_\eta L^2X^\eta,\\
 |\lambda_{dm}(d)|&\ll_\eta X^\eta,\\
 \Lambda_2
 &:=\sum_{d\ {\rm odd}}\sum_m|\lambda_{dm}(d)|^2
 \ll_\varepsilon L^2X^\varepsilon,\\
 r_d&:=\#\{m:\lambda_{dm}(d)\ne0\}\ll L,\\
 D_L
 &:=\sum_N|c_N^{\rm rem}|^2
 =\|Z_\epsilon\|_{L^2(\mathbb T)}^2
 \ll_\varepsilon L^2X^\varepsilon.
 \end{aligned}
 \tag{180.C9}
\]

The first four statements have literal opened-incidence provenance:
there are \(M\asymp L^2\) product sites, at most
\(\tau(N)\ll_\eta X^\eta\) live odd-divisor incidences over each site,
and bounded literal weights; alternatively a fixed \(d\asymp L\) permits
only \(O(M/d)=O(L)\) cofactors. The \(D_L\) bound is the accepted
recombined-energy input from the Round-175 kernel. It can contain divisor
cancellation and is not used to manufacture \(\Lambda_2\).

For integer \(|\nu|\le K\), define the circular half-open cell

\[
 I_\nu=
 \left[(\nu-1/2)/M,(\nu+1/2)/M\right)\pmod1
 \tag{180.C10}
\]

and

\[
 \begin{aligned}
 \mathcal O_{\epsilon,\nu}
 &=2\Re\sum_{\substack{d<d'\\d,d'\ {\rm odd}}}
 \chi_4(d)\chi_4(d')
 \int_{I_\nu}R_{\epsilon,d}(\theta)
 \overline{R_{\epsilon,d'}(\theta)}\,d\theta,\\
 \mathcal G_\nu&=\frac12\sum_{\epsilon=0}^1
 \mathcal O_{\epsilon,\nu},\\
 \mathcal D_\nu&=\frac12\sum_{\epsilon=0}^1
 \sum_{d\ {\rm odd}}\int_{I_\nu}
 |R_{\epsilon,d}(\theta)|^2\,d\theta,\\
 \mathcal E_\nu&=\frac12\sum_{\epsilon=0}^1
 \int_{I_\nu}|Z_\epsilon(\theta)|^2\,d\theta.
 \end{aligned}
 \tag{180.C11}
\]

## 3. Proof or derivation

### 3.1 Exact cell kernel and parity

For every integer \(h\), periodicity permits the lift
\(\theta=(\nu+u)/M\pmod1\), \(-1/2\le u<1/2\), and gives

\[
 \boxed{
 K_\nu(h):=\int_{I_\nu}e(h\theta)\,d\theta
 =
 \begin{cases}
 e(\nu h/M)\dfrac{\sin(\pi h/M)}{\pi h},&h\ne0,\\[6pt]
 M^{-1},&h=0.
 \end{cases}}
 \tag{180.C12}
\]

No boundary mass or wraparound phase is introduced. Moreover

\[
 \frac12\sum_{\epsilon=0}^1(-1)^{\epsilon(m-m')}
 =\mathbf1_{m\equiv m'\pmod2}.
 \tag{180.C13}
\]

Thus both odd-odd and squarefree even-even branches remain, while only
mixed parity is removed. Because both products lie in one \(M\)-site
interval, every unequal surviving difference is even and satisfies
\(0<|dm-d'm'|<M\).

### 3.2 Exact self-return and target-strength equivalence

Expanding the square of the fully recombined \(Z_\epsilon\), before taking
any rowwise modulus, yields

\[
 \int_{I_\nu}|Z_\epsilon|^2
 =\sum_{d\ {\rm odd}}\int_{I_\nu}|R_{\epsilon,d}|^2
 +\mathcal O_{\epsilon,\nu}.
 \tag{180.C14}
\]

Averaging over \(\epsilon\) proves the identity in (180.C1). Also
\[
 |R_{\epsilon,d}(\theta)|^2
 \le r_d\sum_m|\lambda_{dm}(d)|^2,
\]
so the cell length \(1/M\) and (180.C9) give

\[
 0\le\mathcal D_\nu
 \le\frac{\max_d r_d}{M}\Lambda_2
 \ll_\varepsilon LX^\varepsilon.
 \tag{180.C15}
\]

If \(\mathcal G_\nu\ll LX^\varepsilon\), then
\(\mathcal E_\nu=\mathcal D_\nu+\mathcal G_\nu
\ll LX^\varepsilon\). Conversely,
\(\mathcal G_\nu=\mathcal E_\nu-\mathcal D_\nu\le\mathcal E_\nu\).
Finally \(\mathcal E_\nu\ge0\) gives
\(\mathcal G_\nu\ge-\mathcal D_\nu\). This proves (180.C2), including
the one-sided convention.

### 3.3 Exact cross-row product collisions

At \(dm=d'm'=N\), oddness of \(d,d'\) makes the cofactors have the same
parity, both oscillatory phases cancel, and \(K_\nu(0)=1/M\).
Since the literal coefficients are real,

\[
 2\sum_{d<d'}\chi_4(d)\chi_4(d')
 \lambda_N(d)\lambda_N(d')
 =(c_N^{\rm rem})^2-
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}\lambda_N(d)^2.
 \tag{180.C16}
\]

This proves the exact formula in (180.C3). If

\[
 t_N=\#\{d:d\mid N,\ d\ {\rm odd},\lambda_N(d)\ne0\},
\]

then

\[
 \left|(c_N^{\rm rem})^2-\sum_d\lambda_N(d)^2\right|
 \le(t_N-1)\sum_d|\lambda_N(d)|^2.
 \tag{180.C17}
\]

Since \(t_N\le\tau(N)\ll_\eta X^\eta\), (180.C9) and
\(M\asymp L^2\) give

\[
 |\mathcal P_\nu|
 \ll_\eta\frac{X^\eta}{M}\Lambda_2
 \ll_\varepsilon X^\varepsilon
 \tag{180.C18}
\]

uniformly in \(\nu\). This argument uses literal incidence energy, not
recombined cancellation. The alternative bound
\((D_L+\Lambda_2)/M\ll X^\varepsilon\) is compatible but unnecessary.

### 3.4 Exact unequal-product complement

After (180.C3), the retained form is

\[
 \begin{aligned}
 \mathcal U_\nu
 =2\Re\sum_{\substack{d<d'\\d,d'\ {\rm odd}}}
 \sum_{\substack{m\equiv m'\pmod2\\dm\ne d'm'}}
 &\chi_4(d)\chi_4(d')
 \lambda_{dm}(d)\lambda_{d'm'}(d')\\
 &\times e\!\left(
 J(\sqrt{dm}-\sqrt{d'm'})
 +\frac{\nu(dm-d'm')}{M}\right)\\
 &\times
 \frac{\sin(\pi(dm-d'm')/M)}
 {\pi(dm-d'm')}.
 \end{aligned}
 \tag{180.C19}
\]

Every selector, phase, endpoint, transition, hard value, and zero extension
is still inside (180.C19). Equivalently, for \(0<h<M\), \(2\mid h\), put

\[
 \begin{aligned}
 C_h^{\rm off}
 :=\sum_N e\!\left(J(\sqrt{N+h}-\sqrt N)\right)
 \sum_{\substack{d\mid N+h,\ d'\mid N\\
 d,d'\ {\rm odd},\ d\ne d'}}
 \chi_4(d)\chi_4(d')
 \lambda_{N+h}(d)\lambda_N(d').
 \end{aligned}
 \tag{180.C20}
\]

Full-line zero extension makes this endpoint-complete, and conjugate
pairing gives exactly

\[
 \mathcal U_\nu
 =2\Re\sum_{\substack{0<h<M\\2\mid h}}K_\nu(h)C_h^{\rm off}.
 \tag{180.C21}
\]

Taking \(|C_h^{\rm off}|\) separately is not licensed: it deletes the
single outer real part and restores the known shifted-correlation capacity.

### 3.5 Conditional Fejer and K26 connector

The cells with \(|\nu|\le K\) form

\[
 U_K=\left[-(K+1/2)/M,(K+1/2)/M\right)\pmod1.
 \tag{180.C22}
\]

For large \(L\), these cells are disjoint. The exact Fejer formula gives

\[
 F_M(\theta)\ll\frac{M}{1+\nu^2}
 \quad(\theta\in I_\nu),\qquad
 F_M(\theta)\ll\frac ML
 \quad(\theta\in U_K^c).
 \tag{180.C23}
\]

Assume (180.C4). Equations (180.C2)-(180.C3) then give
\(\mathcal E_\nu\ll LX^\varepsilon\) in every near cell. Hence

\[
 \frac12\sum_\epsilon\int_{U_K}F_M|Z_\epsilon|^2
 \ll_\varepsilon
 \sum_{|\nu|\le K}\frac{M}{1+\nu^2}LX^\varepsilon
 \ll_\varepsilon L^3X^\varepsilon.
 \tag{180.C24}
\]

On the far set, Parseval must use the literal recombined energy:

\[
 \frac12\sum_\epsilon\int_{U_K^c}F_M|Z_\epsilon|^2
 \ll\frac ML D_L
 \ll_\varepsilon L^3X^\varepsilon.
 \tag{180.C25}
\]

Thus the full physical energy

\[
 \mathfrak E_M^{(2)}
 :=\frac12\sum_{\epsilon=0}^1
 \int_0^1F_M(\theta)|Z_\epsilon(\theta)|^2\,d\theta
 \ll_\varepsilon L^3X^\varepsilon.
 \tag{180.C26}
\]

Write \(Z_\epsilon=Z_{\epsilon,0}+Z_{\epsilon,*}\), and define

\[
 Q_M^*=\frac12\sum_\epsilon
 \int_0^1F_M|Z_{\epsilon,*}|^2.
 \tag{180.C27}
\]

The accepted collective ordinary-zero estimate is

\[
 A_0:=\sup_{\epsilon,\theta}|Z_{\epsilon,0}(\theta)|
 \ll_\eta\frac{L^2}{J}X^\eta.
 \tag{180.C28}
\]

Consequently, using \(F_M\le M\), \(M\asymp L^2\), and \(L^2\le J\),
the complete zero-containing sector satisfies

\[
 |\mathcal Z_M|
 \ll M\{A_0D_L^{1/2}+A_0^2\}
 \ll_\varepsilon
 \left(\frac{L^5}{J}+\frac{L^6}{J^2}\right)X^\varepsilon
 \ll_\varepsilon L^3X^\varepsilon.
 \tag{180.C29}
\]

Since \(\mathfrak E_M^{(2)}=Q_M^*+\mathcal Z_M\), equations
(180.C26)-(180.C29) give \(Q_M^*\ll L^3X^\varepsilon\).

The exact accepted endpoint identity is

\[
 Q_M^*-Q_{R_0}^*
 =2(T_{26}+B_{\rm short})-\mathcal Z_{R_0,M},
 \tag{180.C30}
\]

where

\[
 Q_{R_0}^*\ge0,\qquad
 |B_{\rm short}|\le R_0D_L\ll_\varepsilon L^3X^\varepsilon,\qquad
 |\mathcal Z_{R_0,M}|\ll_\varepsilon L^3X^\varepsilon.
 \tag{180.C31}
\]

Solving (180.C30) and discarding only
\(-Q_{R_0}^*/2\le0\) proves
\(T_{26}\ll_\varepsilon L^3X^\varepsilon\), which is the one-sided K26
endpoint. The short correction is paid once, and every formula uses the
exact terminal cardinality \(M\).

### 3.6 Coefficient-uniform capacities and nonliteral controls

Let \(S\le M\) be the number of supported product sites. Cauchy after
complete product recombination gives

\[
 \mathcal E_\nu\le\frac{S}{M}D_L
 \ll_\varepsilon L^2X^\varepsilon.
 \tag{180.C32}
\]

This positive capacity is sharp in the coefficient-uniform class. Choose
\(A\asymp L^2\) incidences in \(\asymp L\) odd rows and
\(\asymp L\) cofactors of one fixed parity, with all products in one
\(O(M)\)-diameter interval.

The nonliteral complex dechirped control

\[
 \lambda_{dm}^{\rm cx}(d)=\chi_4(d)e(-J\sqrt{dm})
 \tag{180.C33}
\]

cancels the character and chirp. On a central subarc of length
\(c/M\), all product phases align, so

\[
 \mathcal E_0^{\rm cx}\gg A^2/M\asymp L^2,\qquad
 \mathcal D_0^{\rm cx}\ll L,\qquad
 \mathcal G_0^{\rm cx}\gg L^2.
 \tag{180.C34}
\]

For the nonliteral real cosine-dechirped control, write
\(\phi_{dm}=2\pi J\sqrt{dm}\) and take

\[
 \lambda_{dm}^{(\alpha)}(d)
 =\chi_4(d)\cos(\phi_{dm}-\alpha).
 \tag{180.C35}
\]

Averaging the squared cell norm over the one global phase \(\alpha\)
removes the cross term between the aligned and twice-chirped polynomials.
Thus some \(\alpha\) also gives (180.C34). For the nonliteral arbitrary
real-sign control, choose

\[
 \lambda_{dm}^{\rm sign}(d)
 =\chi_4(d)\operatorname{sgn}\cos(\phi_{dm}-\alpha).
 \tag{180.C36}
\]

A suitable \(\alpha\) aligns one real projection by at least
\((2/\pi)A\), and this persists on a central subarc of length \(c/M\).
It again yields (180.C34).

Since \(F_M(\theta)\asymp M\) on a smaller central subarc, all three
nonliteral controls attain full physical Fejer order

\[
 M\cdot L^2\asymp L^4.
 \tag{180.C37}
\]

The accepted Round-175 kernel gives the same \(L^4\)
coefficient-uniform positive-operator obstruction at the nonzero-mode
endpoint. Equations (180.C32)-(180.C37) are capacity statements, not
literal lower bounds.

### 3.7 Blind-scope reconciliation

The statement-only blind derivation is retained with the following exact
post-unmask repairs.

1. Its finite sinc kernel, wraparound, parity projector, row identity,
   row-diagonal bound, and abstract Gram-capacity boundary agree with
   (180.C12)-(180.C15) and (180.C32).
2. Its exact-product counterexample is nonliteral: it permits an
   arbitrarily large product, unrestricted divisor scales, freely chosen
   signs, and fiber multiplicity outside (180.C9). Literal exact products
   instead satisfy (180.C3).
3. Its proposed twisted-fiber Bessel relation is automatic in the literal
   setting:

   \[
    |c_N^{\rm rem}|^2
    \le t_N\sum_d|\lambda_N(d)|^2,\qquad
    t_N\ll_\eta X^\eta.
    \tag{180.C38}
   \]

   It is not the missing theorem; (180.C4) is.
4. Its abstract packet correctly lacked a far-arc bound. The literal
   recombined input \(D_L\), not \(\Lambda_2\) alone, supplies (180.C25).
5. Every blind dechirped, arbitrary-sign, or constant-character array is
   retained only as a nonliteral coefficient-uniform false control. None is
   the residual coefficient or evidence of literal lower mass.

The blind report's statement-only provenance remains intact; these are
post-unmask scope corrections, not retroactive changes to its derivation.

## 4. First doubtful or unproved step

The first unproved statement is exactly (180.C4), equivalently (180.C19)
or (180.C21). It asks for one factor \(L\) of signed anti-concentration
across distinct divisor rows and unequal products, uniformly in every
near-peak cell, before any row, shift, mode, cell, opening, or divisor norm.

No accepted identity correlates simultaneously:

- the selected/no-pair Boolean field;
- squarefree and coprimality projectors;
- both two-adic and parity branches;
- the complete zero-extended profile and hard endpoints;
- \(\chi_4(d)\chi_4(d')\);
- the square-root and cell-centre phases;
- the sinc kernel; and
- the single outer real part.

Exact product fibers are already target-safe. Fixed-shift regrouping
self-returns to the unresolved signed shifted correlation. Positive local
closure restores \(L^2\), and positive endpoint closure restores \(L^4\).
The product phase has a rank-one radial direction at the centre
\(\theta=0\), so a uniformly nondegenerate positive two-variable
stationary-phase argument is unavailable there. None of these facts
disproves a new complete literal signed theorem.

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| sinc kernel, wraparound, and zero difference | **PASS.** Equation (180.C12) is exact, including \(K_\nu(0)=1/M\). |
| both parity branches | **PASS.** Equation (180.C13) retains odd-odd and squarefree even-even pairs. |
| literal incidence provenance | **PASS.** \(\Lambda_2\) and \(r_d\) come from opened incidences and pointwise weights, not \(D_L\). |
| recombined-energy provenance | **PASS.** \(D_L\) is used for Parseval, far arcs, and coefficient-uniform scalar capacity only. |
| physical row diagonal | **PASS.** The entire \(d=d'\) block is \(O(LX^\varepsilon)\); no transformed diagonal is deleted. |
| self-return and equivalence | **PASS.** Equations (180.C1)-(180.C2) are exact at one-sided target strength. |
| exact cross-row product collision | **PASS.** Equations (180.C16)-(180.C18) give the exact formula and \(O(X^\varepsilon)\). |
| unequal products | **OPEN.** Equation (180.C19) retains every nonzero even gap and every literal field. |
| near and far Fejer arcs | **PASS CONDITIONALLY.** Assuming (180.C4), equations (180.C24)-(180.C26) give \(L^3X^\varepsilon\). |
| ordinary zero and short correction | **PASS.** They are restored collectively and paid once in (180.C29)-(180.C31). |
| complex dechirped | **PASS AS NONLITERAL FALSE CONTROL.** It attains local \(L^2\) but is outside the real literal class. |
| real cosine dechirped | **PASS AS NONLITERAL FALSE CONTROL.** It excludes realness-only contraction, not a literal theorem. |
| arbitrary real signs | **PASS AS NONLITERAL FALSE CONTROL.** It excludes arbitrary-sign-uniform contraction, not literal cancellation. |
| constant character and erased selector | **PASS AS NONLITERAL SHADOWS.** The controls survive, so neither feature alone gives a uniform gain. |
| all-\(1\pmod4\) no-pair row | **PASS AS A LITERAL ALGEBRAIC WARNING.** Character is constant on such an allowed row; no density or lower mass follows. |
| one row and one site | **PASS.** Their off-row forms vanish, showing capacity is attainable but not universal lower mass. |
| hard boundary | **PASS IN SCOPE.** Nonliteral hard rectangles defeat boundary-insensitive closure; the literal hard complement remains open. |
| rank-one product collar | **PASS IN SCOPE.** It blocks uniform nondegenerate positive closure at the central point, not all signed cell methods. |
| blind post-unmask repair | **PASS.** Exact products, fiber Bessel, and far arcs are reconciled as in Section 3.7. |
| owner and exponent quarantine | **PASS.** Only the conditional K26 connector is stated; no owner is closed. |

No numerical experiment was used. Every attaining array in this table is
explicitly marked nonliteral unless it is only the quarantined
all-\(1\pmod4\) algebraic warning.

## 6. Dependencies and exact artifacts used

This candidate uses:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- strategy/round180_m2_hard_top_t1_residual_k26_near_peak_row_gram_strategy.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-k26-near-peak-row-gram-anticoncentration-gate/reports/literal_near_peak_row_gram_attack.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-k26-near-peak-row-gram-anticoncentration-gate/reports/fejer_cell_owner_capacity_audit.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-k26-near-peak-row-gram-anticoncentration-gate/reports/blind_row_gram_rederivation.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-k26-near-peak-row-gram-anticoncentration-gate/reviews/row_identity_fejer_connector_review.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-k26-near-peak-row-gram-anticoncentration-gate/reviews/literal_selector_capacity_false_control_review.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-k26-near-peak-row-gram-anticoncentration-gate/reviews/blind_post_unmask_row_gram_review.md;
- proofs/kernels/m9_m2_hard_top_t1_residual_whole_chain_scale_coboundary_positive_capacity_obstruction.md; and
- proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md.

No web source, external theorem, or numerical computation is a dependency.
This candidate edits no report, review, shared state, proof draft,
validation matrix, proof kernel, strategy, synthesis, control, or
successor-round artifact.

## 7. Recommended state effect

Promote, after final conductor review, only the finite route-scoped
obstruction:

1. exact local self-return (180.C1) and target-strength equivalence
   (180.C2);
2. exact target-safe cross-row product collisions (180.C3);
3. the conditional connector (180.C4) implies (180.C5);
4. sharp coefficient-uniform capacities \(L^2\) locally and \(L^4\) at
   the endpoint, with every attaining control nonliteral; and
5. the blind post-unmask repairs in Section 3.7.

Keep (180.C4), \(Q_M^*\), K26, the complete residual scalar, full
\(t=1\), every other hard-TOP channel, complete hard TOP, BAL, UNBAL,
M9-M2, both M1 routes, GAR, endpoint uniformity, M9, both bridges, the
quarter theorem, and every exponent owner unchanged. This candidate has no
implication edge unless the literal unequal-product theorem is separately
proved and validated. Do not infer literal lower mass from any capacity
control, and do not start Round 181 from this candidate.
