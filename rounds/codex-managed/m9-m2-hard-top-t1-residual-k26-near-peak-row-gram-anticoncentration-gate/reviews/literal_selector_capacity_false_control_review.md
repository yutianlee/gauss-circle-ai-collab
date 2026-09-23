# Round 180 literal selector, capacity, and false-control review

- Campaign: m9-m2-hard-top-t1-residual-k26-near-peak-row-gram-anticoncentration-gate
- Round: 180
- Role: independent literal-selector/capacity seam reviewer
- Starting graph: e94ef6a364988e47f8a59ca3589f03cb098a04a241ec841afc2efa6e685081b4
- Reviewed exit label: row_gram_offdiagonal_capacity_or_self_return_no_go
- Allocation: 100% analytical/algebraic; 0% numerical

## 1. Result

The narrow obstruction is correct. I find no error in the literal
row-Gram identity, the exact product-collision extraction, the incidence
provenance, the restored capacities, or the stated false controls.

With

\[
 \mathcal E_\nu=\frac12\sum_{\epsilon=0}^1
 \int_{I_\nu}|Z_\epsilon(\theta)|^2\,d\theta,\qquad
 \mathcal D_\nu=\frac12\sum_{\epsilon=0}^1\sum_{d\ {\rm odd}}
 \int_{I_\nu}|R_{\epsilon,d}(\theta)|^2\,d\theta
\]

and

\[
 \mathcal G_\nu=\frac12\sum_{\epsilon=0}^1
 \mathcal O_{\epsilon,\nu},
\]

one has exactly

\[
 \boxed{\mathcal E_\nu=\mathcal D_\nu+\mathcal G_\nu},\qquad
 0\le\mathcal D_\nu\ll_\varepsilon LX^\varepsilon.
 \tag{180.R1}
\]

Consequently the one-sided upper bounds

\[
 \mathcal G_\nu\ll_\varepsilon LX^\varepsilon
 \quad\text{and}\quad
 \mathcal E_\nu\ll_\varepsilon LX^\varepsilon
 \tag{180.R2}
\]

are equivalent at target strength. The reverse direction uses
\(\mathcal G_\nu=\mathcal E_\nu-\mathcal D_\nu\le\mathcal E_\nu\),
and positivity of \(\mathcal E_\nu\) gives
\(\mathcal G_\nu\ge-\mathcal D_\nu\). Thus the negative side is already
target-safe.

The exact cross-row product-collision sector is

\[
 \boxed{
 \mathcal P_\nu=\frac1M\sum_N
 \left\{(c_N^{\rm rem})^2-
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}\lambda_N(d)^2\right\}}
 \ll_\varepsilon X^\varepsilon.
 \tag{180.R3}
\]

After this target-safe sector is removed, the complete nonzero even-gap
literal form remains unproved. Under only the audited support, energy,
row-length, parity, reality, and character-modulation data, the sharp
positive capacity is \(L^2X^\varepsilon\) on one near cell and
\(L^4X^\varepsilon\) after the central Fejer weight. The controls attain
these orders only in coefficient shadows. They give no lower mass for the
literal residual coefficient, \(Q_M^*\), K26, or any downstream owner.

## 2. Exact statement and hypotheses

Let

\[
 J=\sqrt X,\qquad 1\ll L\ll H\le J^{1/2},\qquad
 R_0=\lceil L\rceil,\qquad M\asymp L^2,
\]

where \(M\) is the exact cardinality of the containing integer interval.
The real coefficient \(\lambda_N(d)\) is the complete literal Round-180
coefficient: the selected/no-pair field, squarefree and coprimality
projectors, both two-adic branches, near-square support, profiles, floors,
stars, hard values, endpoints, transitions, support births and deaths, and
full-line zero extension all remain inside it. Put

\[
 R_{\epsilon,d}(\theta)=\sum_m(-1)^{\epsilon m}
 \lambda_{dm}(d)e(J\sqrt{dm}+dm\theta),\qquad
 Z_\epsilon(\theta)=\sum_{d\ {\rm odd}}\chi_4(d)R_{\epsilon,d}(\theta).
 \tag{180.R4}
\]

The two distinct positive ledgers are

\[
 \Lambda_2=\sum_{d,m}|\lambda_{dm}(d)|^2
 \ll_\varepsilon L^2X^\varepsilon,\qquad
 D_L=\sum_N|c_N^{\rm rem}|^2
 =\|Z_\epsilon\|_2^2
 \ll_\varepsilon L^2X^\varepsilon.
 \tag{180.R5}
\]

Their provenance must not be exchanged. The first follows before divisor
recombination: there are \(M\asymp L^2\) possible products, at most
\(\tau(N)\ll_\eta X^\eta\) live odd-divisor incidences above each product,
and \(|\lambda_N(d)|\ll_\eta X^\eta\). Equivalently, near-square support
has \(d,m\asymp L\), hence only \(O(L)\) cofactors in each fixed row.
The bound for \(D_L\) is the accepted recombined coefficient energy and
may contain cancellation among divisor incidences; it does not imply the
bound for \(\Lambda_2\). Both reports preserve this distinction.

For

\[
 I_\nu=[(\nu-1/2)/M,(\nu+1/2)/M)\pmod1,
\]

integer periodicity gives the exact kernel

\[
 K_\nu(h)=\int_{I_\nu}e(h\theta)\,d\theta
 =e(\nu h/M)\frac{\sin(\pi h/M)}{\pi h},\qquad
 K_\nu(0)=\frac1M.
 \tag{180.R6}
\]

This includes the wrapped central cell and all half-open endpoints. Parity
averaging gives

\[
 \frac12\sum_{\epsilon=0}^1(-1)^{\epsilon(m-m')}
 =\mathbf1_{m\equiv m'\pmod2},
 \tag{180.R7}
\]

so both odd-odd and squarefree even-even branches survive, while only the
mixed branch vanishes.

## 3. Proof or derivation

Expanding the square of the fully recombined \(Z_\epsilon\), and only then
splitting \(d=d'\) from \(d\ne d'\), proves (180.R1) with exactly one
outer real part. If
\(r_d=\#\{m:\lambda_{dm}(d)\ne0\}\ll L\), then

\[
 |R_{\epsilon,d}(\theta)|^2
 \le r_d\sum_m|\lambda_{dm}(d)|^2.
\]

Integration over a cell of length \(1/M\) and (180.R5) gives

\[
 \mathcal D_\nu\le\frac{\max_d r_d}{M}\Lambda_2
 \ll_\varepsilon LX^\varepsilon.
 \tag{180.R8}
\]

This is the complete physical row diagonal, including nonzero product
differences within a fixed row. It is not a fixed diagonal created after a
dual transform.

For a cross-row collision \(dm=d'm'=N\), the cofactors have the same
parity because \(d,d'\) are odd. Both oscillatory phases cancel and
\(K_\nu(0)=1/M\). Since the literal coefficients are real,

\[
 2\sum_{d<d'}\chi_4(d)\chi_4(d')
 \lambda_N(d)\lambda_N(d')
 =(c_N^{\rm rem})^2-\sum_d\lambda_N(d)^2,
\]

which proves (180.R3), including its factor. If \(t_N\) is the number of
live incidences above \(N\), then

\[
 \left|(c_N^{\rm rem})^2-\sum_d\lambda_N(d)^2\right|
 \le(t_N-1)\sum_d|\lambda_N(d)|^2.
\]

Using \(t_N\le\tau(N)\ll_\eta X^\eta\), summing over \(N\), and dividing
by \(M\asymp L^2\) proves
\(|\mathcal P_\nu|\ll_\varepsilon X^\varepsilon\). No recombined-energy
cancellation is used here.

For the universal upper capacity, let \(S\le M\) be the number of
supported products. Cauchy in the recombined product variable gives

\[
 \mathcal E_\nu\le\frac{S}{M}D_L
 \ll_\varepsilon L^2X^\varepsilon.
 \tag{180.R9}
\]

This is sharp at the coefficient-uniform interface. Take
\(A\asymp L^2\) incidences in \(\asymp L\) odd rows and
\(\asymp L\) cofactors of one parity, with all products in an interval of
diameter \(O(M)\). For the complex dechirped array

\[
 \lambda_{dm}(d)=\chi_4(d)e(-J\sqrt{dm}),
\]

the character and chirp cancel. On a central subarc of length \(c/M\),
the remaining product phases align, so

\[
 \mathcal E_0\gg A^2/M\asymp L^2,\qquad
 \mathcal D_0\ll L,\qquad
 \mathcal G_0\gg L^2.
 \tag{180.R10}
\]

This first array is deliberately complex. For a real control, put
\(\phi_{dm}=2\pi J\sqrt{dm}\) and

\[
 \lambda_{dm}^{(\alpha)}(d)=\chi_4(d)
 \cos(\phi_{dm}-\alpha).
\]

Writing the resulting sum as one half of the aligned product polynomial
plus a twice-chirped polynomial, averaging over the single global
\(\alpha\) removes their cross term. The aligned part already has cell
mass \(\gg A^2/M\), so some \(\alpha\) gives (180.R10) with real
coefficients. Finally, choosing

\[
 s_{dm}=\operatorname{sgn}\cos(\phi_{dm}-\alpha)
\]

aligns one real projection by at least \((2/\pi)A\) for a suitable
\(\alpha\); the alignment persists on a subarc of length \(c/M\). This
proves the same lower order for an arbitrary-real-sign shadow.

On that subarc \(F_M(\theta)\asymp M\). Hence the corresponding full
physical Fejer energy has order

\[
 M\cdot L^2\asymp L^4.
 \tag{180.R11}
\]

This verifies sharp local \(L^2\) and endpoint \(L^4\) capacities. The
accepted whole-chain kernel separately supplies the same \(L^4\)
coefficient-uniform positive-operator obstruction for the nonzero-mode
endpoint. Neither statement is a literal lower bound.

The remaining controls have the following exact scope.

- Replacing \(\chi_4\) by a constant, or erasing the selector, leaves the
  same controls after absorbing the row character into the chosen
  coefficients. Thus neither datum by itself yields a coefficient-uniform
  contraction.
- On a permitted no-pair row whose odd prime factors are all
  \(1\pmod4\), every surviving divisor has character \(+1\). This rules
  out a formal rowwise character mean-zero identity, but supplies neither
  density nor literal lower mass.
- A one-row array has \(\mathcal G_\nu=0\). A one-incidence array has no
  off-row pair, while multiple incidences above one product give exactly
  the already-safe collision formula. These controls rule out interpreting
  capacity as a universal lower bound.
- The hard rectangular shadows, half-open cells, and full-line zero
  extension retain order-one boundary jumps. Hard boundaries alone do not
  create the missing gain, while the literal hard-boundary complement
  remains inside the open theorem.
- At the centre \(\theta=0\) of the central cell, the product phase
  \(J\sqrt{dm}\) has the rank-one Hessian and radial null direction audited
  in the product-collar kernel. Therefore a uniformly nondegenerate
  positive two-variable stationary-phase closure is unavailable there.
  This is only a no-repeat control: it does not exclude a signed method
  using the full \(\theta\)-cell, selector, endpoints, and character
  simultaneously.

## 4. First doubtful or unproved step

The first unproved step is precisely

\[
 \boxed{
 \mathcal G_\nu-\mathcal P_\nu
 \ll_\varepsilon LX^\varepsilon
 \quad(|\nu|\le\lceil\sqrt L\rceil).}
 \tag{180.R12}
\]

Every nonzero even product difference, sinc factor, cell-centre and
square-root phase, selector, projector, two-adic branch, profile, endpoint,
transition, and zero-extension field must remain in this statement.
Equivalently, by (180.R1)-(180.R3), it is the complete local scalar
estimate \(\mathcal E_\nu\ll_\varepsilon LX^\varepsilon\).

No reviewed identity supplies the required factor \(L^{-1}\). Grouping by
nonzero product shift returns to the unresolved signed shifted correlation;
taking a positive row or shift norm restores (180.R9); and a positive
simultaneous transform at the central peak returns to the rank-one product
collar. The false controls prove only that a theorem based on the listed
coefficient-uniform data cannot establish (180.R12). They neither prove nor
disprove (180.R12) for the complete literal coefficient.

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| exact self-return and one-sided equivalence | **PASS.** Expansion after full recombination gives (180.R1), and positivity gives both directions of (180.R2). |
| product collision and multiplicity | **PASS.** Same-parity collision algebra gives (180.R3); \(\tau(N)\), \(\Lambda_2\), and \(M\asymp L^2\) give \(O(X^\varepsilon)\). |
| literal incidence versus recombined energy | **PASS.** \(\Lambda_2\) comes from opened incidence count and pointwise weights; \(D_L\) is used only after recombination. |
| local and endpoint capacity | **PASS.** The upper scales are \(L^2\) and \(L^4\), and the dechirped shadows attain them. |
| complex dechirped | **PASS as a false control.** It is explicitly nonliteral and tests the enlarged complex coefficient class only. |
| real cosine dechirped | **PASS as a false control.** A global phase average produces a real array of local order \(L^2\). |
| arbitrary real signs | **PASS as a false control.** Projection alignment produces local order \(L^2\) with real signs. |
| constant character and erased selector | **PASS as shadow controls.** The same capacity survives; no literal-density claim is made. |
| all-\(1\pmod4\) no-pair | **PASS warning.** It forbids a formal rowwise mean-zero shortcut but proves no mass statement. |
| one row, one site, and exact collision | **PASS.** They show capacity is attainable but not forced and isolate the safe collision sector. |
| hard boundary | **PASS in the stated scope.** Boundary-insensitive and smooth-interior shortcuts are excluded; the literal boundary complement is not dropped. |
| rank-one product collar | **PASS in the stated scope.** It excludes uniform nondegenerate positive closure at the central point, not all signed cell methods. |
| literal lower-mass quarantine | **PASS.** Both reports label the attaining arrays as nonliteral and leave (180.R12) open. |
| downstream and exponent quarantine | **PASS.** No K26, parent, bridge, quarter theorem, or exponent is claimed. |

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

This review used exactly:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- strategy/round180_m2_hard_top_t1_residual_k26_near_peak_row_gram_strategy.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-k26-near-peak-row-gram-anticoncentration-gate/reports/literal_near_peak_row_gram_attack.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-k26-near-peak-row-gram-anticoncentration-gate/reports/fejer_cell_owner_capacity_audit.md;
- proofs/kernels/m9_m2_hard_top_t1_residual_whole_chain_scale_coboundary_positive_capacity_obstruction.md; and
- proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md.

All derivations above are exact finite algebra or consequences of the
audited dependencies. No web source, external theorem, numerical evidence,
blind artifact, sibling review, synthesis, or unlisted proof kernel was
used. This review edits no report, kernel, shared state, proof draft,
validation matrix, synthesis, or control artifact.

## 7. Recommended state effect

**Promote only the narrow route-scoped obstruction after the remaining
required campaign reviews.** It certifies:

1. the exact self-return (180.R1) and target-strength one-sided equivalence
   (180.R2);
2. the owner-complete, target-safe collision sector (180.R3);
3. sharp coefficient-uniform capacities \(L^2\) locally and \(L^4\) at
   the Fejer endpoint; and
4. failure of the listed coefficient-uniform, realness-only,
   character-only, selector-erased, boundary-insensitive, and positive
   rank-one mechanisms to supply the missing factor \(L\).

Keep the literal estimate (180.R12), K26, the residual scalar, complete
\(t=1\), every other hard-TOP owner, BAL, UNBAL, M9-M2, both M1 routes,
GAR, endpoint uniformity, M9, both bridges, the quarter theorem, and every
exponent unchanged. In particular, do not convert attainable capacity into
literal lower mass.

**Final verdict: GREEN.**
