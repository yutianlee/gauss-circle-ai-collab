# Round 180 conductor report reconciliation

- Campaign: `m9-m2-hard-top-t1-residual-k26-near-peak-row-gram-anticoncentration-gate`
- Round: 180
- Role: independent conductor report reconciler
- Starting graph: `e94ef6a364988e47f8a59ca3589f03cb098a04a241ec841afc2efa6e685081b4`
- Allocation: 100% analytical/algebraic; 0% numerical

## 1. Result

The reports reconcile, by exact algebra rather than vote, to the terminal
label

`row_gram_offdiagonal_capacity_or_self_return_no_go`.

The selected conclusion is not the near-cell target (180.G). It is the
following route-scoped obstruction and exact decomposition. With

\[
 \mathcal G_\nu=\frac12\sum_{\epsilon=0}^1\mathcal O_{\epsilon,\nu},
 \qquad
 \mathcal D_\nu=\frac12\sum_{\epsilon=0}^1\sum_{d\ {\rm odd}}
 \int_{I_\nu}|R_{\epsilon,d}(\theta)|^2\,d\theta,
\]

and

\[
 \mathcal E_\nu=\frac12\sum_{\epsilon=0}^1
 \int_{I_\nu}|Z_\epsilon(\theta)|^2\,d\theta,
\]

one has exactly

\[
 \mathcal E_\nu=\mathcal D_\nu+\mathcal G_\nu,
 \qquad
 0\le \mathcal D_\nu\ll_\varepsilon LX^\varepsilon.
\tag{180.C1}
\]

The complete cross-row exact-product sector is

\[
 \mathcal P_\nu
 =\frac1M\sum_N\left\{(c_N^{\rm rem})^2
 -\sum_{\substack{d\mid N\\d\ {\rm odd}}}\lambda_N(d)^2\right\}
 \ll_\varepsilon X^\varepsilon.
\tag{180.C2}
\]

It is a strict literal target-safe sector. Its exact complement is the
one-outer-real-part unequal-product form with every nonzero even difference
\(0<|dm-d'm'|<M\) retained. That complement remains unproved.

The positive coefficient-uniform scales are sharp at
\(L^2X^\varepsilon\) in one near cell and \(L^4X^\varepsilon\) after the
central Fejer weight. Complex dechirped, real cosine-dechirped, and
arbitrary-real-sign arrays attain these scales only in enlarged coefficient
classes. They rule out feature-insensitive positive closures; they are not
literal residual arrays and give no literal lower mass.

The statement-only report is valid for its abstract B180 packet. Its
literal interpretation needs the scope repairs already supplied by the
post-unmask review: the abstract exact-product counterexample is not
literal, its proposed fiber-Bessel condition is automatic at literal
scale, its abstract far-arc limitation is repaired by the accepted
recombined energy \(D_L\), and its dechirped arrays are false controls only.
With those repairs imposed, there is no remaining conflict among the three
reports or the three completed seam reviews.

## 2. Exact statement and hypotheses

Let

\[
 J=\sqrt X,\qquad 1\ll L\ll H\le J^{1/2},\qquad
 R_0=\lceil L\rceil,
\]

and let \(M\) be the exact integer cardinality of the containing product
interval, with \(M\asymp L^2\). Put
\(K=\lceil\sqrt L\rceil\). The complete real coefficient
\(\lambda_N(d)\) retains the selected/no-pair value, squarefree and
coprimality projectors, both two-adic branches, near-square and Vaaler
profiles, floors, stars, hard values, endpoints, transitions, support
births and deaths, and full-line zero extension. On its literal support,
\(d,m\asymp L\), and the distinct positive ledgers are

\[
 \Lambda_2:=\sum_{d\ {\rm odd}}\sum_m|\lambda_{dm}(d)|^2
 \ll_\varepsilon L^2X^\varepsilon,
 \qquad
 r_d:=\#\{m:\lambda_{dm}(d)\ne0\}\ll L,
\tag{180.C3}
\]

and

\[
 c_N^{\rm rem}=\sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi_4(d)\lambda_N(d),
 \qquad
 D_L:=\sum_N|c_N^{\rm rem}|^2
 \ll_\varepsilon L^2X^\varepsilon.
\tag{180.C4}
\]

The first ledger comes from opened incidence counting and bounded literal
weights; the second is the accepted recombined coefficient energy. Neither
may be inferred from the other.

For \(\epsilon\in\{0,1\}\), define

\[
 R_{\epsilon,d}(\theta)
 =\sum_m(-1)^{\epsilon m}\lambda_{dm}(d)
 e(J\sqrt{dm}+dm\theta),
 \qquad
 Z_\epsilon(\theta)=\sum_{d\ {\rm odd}}\chi_4(d)R_{\epsilon,d}(\theta),
\tag{180.C5}
\]

and, for \(|\nu|\le K\),

\[
 I_\nu=[(\nu-1/2)/M,(\nu+1/2)/M)\pmod1.
\]

For every integer \(h\), including a cell wrapping through zero,

\[
 K_\nu(h):=\int_{I_\nu}e(h\theta)\,d\theta
 =\begin{cases}
 e(\nu h/M)\dfrac{\sin(\pi h/M)}{\pi h},&h\ne0,\\[5pt]
 M^{-1},&h=0.
 \end{cases}
\tag{180.C6}
\]

Half-open endpoints contribute no mass. Parity averaging is exactly

\[
 \frac12\sum_{\epsilon=0}^1(-1)^{\epsilon(m-m')}
 =\mathbf 1_{m\equiv m'\pmod2}.
\tag{180.C7}
\]

Because \(d,d'\) are odd, this retains both odd--odd and squarefree
even--even product branches and removes only mixed parity. No rowwise,
shiftwise, cellwise, or modewise modulus is part of the literal target.

## 3. Proof and reconciliation

### 3.1 Row identity and physical diagonal

Expanding \(|Z_\epsilon|^2\) after the complete row sum, and only then
separating \(d=d'\), gives (180.C1) with exactly one outer real part. For
each row, pointwise Cauchy gives

\[
 |R_{\epsilon,d}(\theta)|^2
 \le r_d\sum_m|\lambda_{dm}(d)|^2.
\]

The cell length is \(1/M\), so (180.C3) yields

\[
 \mathcal D_\nu
 \le \frac{\max_dr_d}{M}\Lambda_2
 \ll_\varepsilon \frac{L}{M}L^2X^\varepsilon
 \ll_\varepsilon LX^\varepsilon.
\tag{180.C8}
\]

This is the complete physical row diagonal, including unequal products
within a fixed row. It is not a diagonal introduced after a dual transform.
Since \(\mathcal E_\nu\ge0\), one also has
\(\mathcal G_\nu\ge-\mathcal D_\nu\). Therefore only the one-sided upper
bound for \(\mathcal G_\nu\) is open, and

\[
 \mathcal G_\nu\ll_\varepsilon LX^\varepsilon
 \quad\Longleftrightarrow\quad
 \mathcal E_\nu\ll_\varepsilon LX^\varepsilon
\tag{180.C9}
\]

at target strength.

### 3.2 Exact products and the unequal-product complement

At \(dm=d'm'=N\), both cofactors have the same parity, both oscillatory
phases cancel, and \(K_\nu(0)=1/M\). Since the literal coefficients are
real,

\[
 2\sum_{d<d'}\chi_4(d)\chi_4(d')\lambda_N(d)\lambda_N(d')
 =(c_N^{\rm rem})^2-\sum_d\lambda_N(d)^2,
\]

which proves the exact formula in (180.C2). If \(t_N\) is the number of
live odd-divisor incidences over \(N\), then

\[
 \left|(c_N^{\rm rem})^2-\sum_d\lambda_N(d)^2\right|
 \le (t_N-1)\sum_d|\lambda_N(d)|^2.
\]

The literal bound \(t_N\le\tau(N)\ll_\eta X^\eta\), (180.C3), and
\(M\asymp L^2\) give \(|\mathcal P_\nu|\ll_\varepsilon X^\varepsilon\),
uniformly in \(\nu\). Thus the blind construction with arbitrarily many
freely signed rows over one unrestricted product is a valid counterexample
to B180, but it is not a literal counterexample.

After (180.C2), the exact complement is

\[
\begin{aligned}
 \mathcal G_\nu-\mathcal P_\nu
 =2\Re\sum_{\substack{d<d'\\d,d'\ {\rm odd}}}
 \sum_{\substack{m\equiv m'\pmod2\\dm\ne d'm'}}
 &\chi_4(d)\chi_4(d')\lambda_{dm}(d)\lambda_{d'm'}(d')\\
 &\times e\!\left(J(\sqrt{dm}-\sqrt{d'm'})
 +\frac{\nu(dm-d'm')}{M}\right)\\
 &\times\frac{\sin(\pi(dm-d'm')/M)}
 {\pi(dm-d'm')}.
\end{aligned}
\tag{180.C10}
\]

Every surviving gap is even and satisfies \(0<|dm-d'm'|<M\). Every
literal field remains inside (180.C10).

### 3.3 Near/far powers and the conditional K26 connector

Exact product recombination gives

\[
 Z_\epsilon(\theta)=\sum_N(-1)^{\epsilon N}c_N^{\rm rem}
 e(J\sqrt N+N\theta),
 \qquad \|Z_\epsilon\|_2^2=D_L.
\tag{180.C11}
\]

The near cells are disjoint for large \(L\), and their complement obeys
\(M\|\theta\|\ge K+1/2>\sqrt L\). On a near cell and on the complement,
respectively,

\[
 F_M(\theta)\ll\frac{M}{1+\nu^2},
 \qquad
 F_M(\theta)\ll\frac ML.
\tag{180.C12}
\]

If the still-open bound (180.C10) is assumed at
\(O_\varepsilon(LX^\varepsilon)\), then (180.C1), (180.C2), and
(180.C8) give \(\mathcal E_\nu\ll_\varepsilon LX^\varepsilon\) on every
near cell. Positivity after complete recombination and
\(\sum_\nu(1+\nu^2)^{-1}\ll1\) give the near contribution

\[
 \ll_\varepsilon MLX^\varepsilon
 \ll_\varepsilon L^3X^\varepsilon.
\tag{180.C13}
\]

Parseval and (180.C4) give the full far contribution

\[
 \ll_\varepsilon \frac ML D_L
 \ll_\varepsilon L^3X^\varepsilon.
\tag{180.C14}
\]

This is the precise literal repair of the blind packet's far-arc
limitation: opened incidence energy alone does not control the recombined
far norm, but the accepted \(D_L\) does.

For the ordinary-zero component, the accepted collective estimate
\(A_0\ll_\eta L^2J^{-1}X^\eta\) gives

\[
 M(A_0D_L^{1/2}+A_0^2)
 \ll_\varepsilon L^3X^\varepsilon
\tag{180.C15}
\]

because \(M\asymp L^2\) and \(L^2\le J\). The short correction is paid
once at \(O_\varepsilon(R_0D_L)\ll_\varepsilon L^3X^\varepsilon\), and
the exact endpoint \(M\), including a strict terminal stopped-chain link,
is never rounded. Hence (180.C10) at target strength conditionally gives
\(Q_M^*\ll_\varepsilon L^3X^\varepsilon\), and the accepted endpoint
identity gives the one-sided K26 estimate. This verifies an implication;
it proves neither its hypothesis nor K26.

### 3.4 Capacity and self-return

If \(S\le M\) is the number of supported products, Cauchy in the
recombined product variable gives

\[
 \mathcal E_\nu\le\frac SM D_L
 \ll_\varepsilon L^2X^\varepsilon.
\tag{180.C16}
\]

On \(A\asymp L^2\) incidence shadows with \(O(L)\) cofactors per row,
complex dechirping, a single-global-phase real cosine dechirping, and a
real-sign projection each make the central-cell energy
\(\gg A^2/M\asymp L^2\), while the row diagonal remains \(O(L)\).
On a smaller central subarc \(F_M\asymp M\), so these controls attain
endpoint order \(L^4\). Restriction to one parity, constant character, or
an erased selector does not repair a proof using only these uniform data.

These arrays do not equal the fixed literal coefficient. Conversely, one
row or one global incidence makes the off-row form zero. Thus capacity is
attainable but not forced. Grouping (180.C10) by positive even shifts and
then taking shiftwise absolute values returns to the unresolved signed
shifted correlation; positive simultaneous dualization at the central cell
returns to the rank-one product collar. These are exact route-scoped
self-returns, not literal lower bounds or impossibility theorems for
(180.C10).

## 4. First doubtful or unproved step

The first open literal theorem is exactly

\[
 \boxed{\mathcal G_\nu-\mathcal P_\nu
 \ll_\varepsilon LX^\varepsilon
 \quad\text{uniformly for }|\nu|\le\lceil\sqrt L\rceil,}
\tag{180.C17}
\]

with the left side given without abbreviation by (180.C10). Equivalently
at target strength, it is
\(\mathcal E_\nu\ll_\varepsilon LX^\varepsilon\). It requires a new
selector-, phase-, parity-, cell-, and endpoint-stable signed relation
before any positive norm.

The blind proposed fiber relation is not this first open theorem. With

\[
 T_N=\sum_{d\mid N,\ d\ {\rm odd}}\chi_4(d)\lambda_N(d)
 =c_N^{\rm rem},
 \qquad
 E_N=\sum_{d\mid N,\ d\ {\rm odd}}|\lambda_N(d)|^2,
\]

divisor Cauchy gives \(|T_N|^2\le t_NE_N\), hence
\(\sum_N|T_N|^2\ll_\eta X^\eta\sum_NE_N\), while (180.C4) supplies the
accepted recombined estimate directly. Exact fibers are therefore paid.
The unknown begins at unequal products. Fixed-shift regrouping is an exact
restatement of (180.C17), not an estimate, and no reviewed result supplies
the missing factor \(L^{-1}\).

## 5. Control outcomes and required scope repairs

| Seam or control | Reconciled outcome |
|---|---|
| exact row identity, one outer real part | **GREEN.** Equation (180.C1) follows before any positive row operation. |
| sinc kernel, zero difference, wraparound, half-open cells | **GREEN.** Equation (180.C6) is exact, including \(K_\nu(0)=1/M\). |
| both parity branches | **GREEN.** Equation (180.C7) retains both same-parity branches. |
| incidence provenance, row length, physical diagonal | **GREEN.** \(\Lambda_2\) is opened-incidence energy, and the complete row diagonal has power \(L^3/M\asymp L\). |
| exact cross-row product collisions | **GREEN LITERALLY.** Equation (180.C2) is owner-complete and \(O_\varepsilon(X^\varepsilon)\). |
| blind exact-product construction | **REPAIR SCOPE.** It refutes the abstract B180 class only; it is not a literal residual counterexample. |
| blind fiber-Bessel proposal | **REPLACE.** It is automatic after divisor multiplicity and epsilon rebudgeting; the first open literal theorem is (180.C17). |
| blind far-arc limitation | **REPAIR BY LITERAL HYPOTHESIS.** It is correct abstractly; (180.C4) and Parseval prove (180.C14). |
| near/far Fejer powers | **GREEN.** Near target \(L\) and far height \(M/L\) both restore endpoint target \(L^3\). |
| ordinary zero, short correction, exact endpoint | **GREEN.** Ordinary zero is restored collectively, the short term is paid once, and no terminal link is rounded. |
| complex dechirped | **GREEN AS FALSE CONTROL.** It excludes magnitude-only and positive coefficient-uniform closure and is nonliteral. |
| real cosine dechirped | **REPAIR LABEL, THEN GREEN.** It is a real abstract false control, not a failure of the literal coefficient theorem. |
| arbitrary signs, constant character, erased selector | **GREEN AS FALSE CONTROLS.** They exclude only mechanisms insensitive to the fixed literal symbol. |
| all-\(1\pmod4\) no-pair support | **GREEN WITH QUARANTINE.** It forbids a formal rowwise mean-zero identity but proves no density or lower mass. |
| one row, one site, and exact collision | **GREEN.** The first two show capacity is not forced; the literal exact-collision sector is already paid. |
| hard boundaries and zero extension | **GREEN.** They remain in (180.C10); no smooth-interior theorem is substituted. |
| fixed shift and product collar | **SELF-RETURN.** Positive closure restores capacity; neither check disproves a new literal signed method. |
| restored powers | **GREEN.** Diagonal \(L\), local target \(L\), local positive capacity \(L^2\), endpoint target \(L^3\), and endpoint positive capacity \(L^4\) are consistent. |
| downstream and exponent scope | **GREEN.** Only the conditional K26 connector is verified; no open owner or exponent changes. |

The four blind-to-literal qualifications above are mandatory whenever the
blind report is cited. They are scope repairs, not defects in its abstract
proof. The completed post-unmask review already states them, so no report
rewrite is required for a repaired Round-180 synthesis.

## 6. Dependencies and exact artifacts used

The mathematical reconciliation used:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/round180_m2_hard_top_t1_residual_k26_near_peak_row_gram_strategy.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k26-near-peak-row-gram-anticoncentration-gate/blind_statement.md`;
- all three Round-180 reports:
  `literal_near_peak_row_gram_attack.md`,
  `fejer_cell_owner_capacity_audit.md`, and
  `blind_row_gram_rederivation.md`; and
- all three completed Round-180 reviews:
  `row_identity_fejer_connector_review.md`,
  `blind_post_unmask_row_gram_review.md`, and
  `literal_selector_capacity_false_control_review.md`.

No web source, external theorem, or numerical experiment was used. The
equalities above were rechecked directly rather than accepted by reviewer
count. This review changes no report, kernel, graph, proof draft, validation
matrix, synthesis, control artifact, or successor-round artifact.

## 7. Recommended state effect

Promote only a subordinate proved-internal, route-scoped
row-Gram capacity/self-return obstruction, after the conductor supplies the
usual mechanically valid State Patch. Its exact content may include
(180.C1), the target-strength equivalence (180.C9), the strict literal
collision sector (180.C2), the conditional connector from (180.C17) to
K26, the sharp coefficient-uniform \(L^2/L^4\) capacities, and the named
false-control and self-return boundaries.

Do not promote (180.C17), (180.G), \(Q_M^*\ll L^3X^\varepsilon\), K26,
the complete residual scalar, full \(t=1\), another hard-TOP channel,
complete hard TOP, BAL, UNBAL, M9--M2, either M1 route, GAR, endpoint
uniformity, M9, either bridge, the quarter theorem, or any exponent. The
accepted internal \(1/3\) theorem, external Li--Yang exponent, and target
\(1/4\) ledger remain unchanged.

The exact-product sector is retained as a subordinate strict safe sector,
but the round closes under only the no-go label because its principal new
result is the row-Gram capacity/self-return obstruction and its exact
unequal-product complement remains open. Do not start Round 181 from this
review.

**Final verdict: GREEN.**
