# Round 180 final kernel mathematical and scope review

- Campaign: `m9-m2-hard-top-t1-residual-k26-near-peak-row-gram-anticoncentration-gate`
- Round: 180
- Role: independent final durable-kernel reviewer
- Starting graph: `e94ef6a364988e47f8a59ca3589f03cb098a04a241ec841afc2efa6e685081b4`
- Reviewed kernel: `proofs/kernels/m9_m2_hard_top_t1_residual_k26_near_peak_row_gram_self_return_obstruction.md`
- Allocation: 100% analytical/algebraic; 0% numerical

## 1. Result

The proposed durable kernel is mathematically correct and properly scoped.
I find no missing factor $2$, $M$, parity branch, collision multiplicity,
or endpoint sign. The circular-cell kernel, physical row decomposition,
one-sided equivalence, exact cross-row collision formula, conditional
near/far Fejer connector, ordinary-zero restoration, once-only short
correction, coefficient-uniform capacities, blind-scope repairs, and owner
quarantine all agree with the formalized candidate, the three reports, and
the four final on-disk reviews.

The kernel proves only the authorized terminal result

`row_gram_offdiagonal_capacity_or_self_return_no_go`.

It does not prove the literal unequal-product estimate, $Q_M^*$, K26, or
any downstream analytic or exponent owner. The $L^2$ local and $L^4$
endpoint examples are explicitly nonliteral capacity controls; none is
promoted as physical lower mass.

## 2. Exact statement and hypotheses

The audited setting is

\[
 e(t)=e^{2\pi it},\qquad J=\sqrt X,\qquad
 1\ll L\ll H\le J^{1/2},\qquad R_0=\lceil L\rceil,
 \qquad M\asymp L^2,
\]

where $M$ is the exact containing-interval cardinality. The literal real
incidence $\lambda_N(d)$ retains the selected/no-pair field, squarefree and
coprimality projectors, both two-adic branches, profiles, floors, stars, hard
values, endpoints, transitions, births, deaths, and full-line zero
extension. The kernel keeps distinct the opened-incidence ledger

\[
 \Lambda_2=\sum_{d\ {\rm odd},m}|\lambda_{dm}(d)|^2
 \ll_\varepsilon L^2X^\varepsilon,
 \qquad r_d\ll L,
\]

and the accepted recombined ledger

\[
 c_N^{\rm rem}=\sum_{d\mid N,\ d\ {\rm odd}}
 \chi_4(d)\lambda_N(d),\qquad
 D_L=\sum_N|c_N^{\rm rem}|^2
 \ll_\varepsilon L^2X^\varepsilon.
\]

With the kernel's definitions of $R_{\epsilon,d}$, $Z_\epsilon$, and
$I_\nu$, direct expansion gives exactly

\[
 \mathcal E_\nu=\mathcal D_\nu+\mathcal G_\nu,
 \qquad 0\le\mathcal D_\nu
 \le {\max_dr_d\over M}\Lambda_2
 \ll_\varepsilon LX^\varepsilon.
\]

Therefore, with $\ll$ explicitly interpreted as the campaign's
one-sided upper bound,

\[
 \mathcal G_\nu\ll_\varepsilon LX^\varepsilon
 \Longleftrightarrow
 \mathcal E_\nu\ll_\varepsilon LX^\varepsilon.
\]

The reverse implication is
$\mathcal G_\nu=\mathcal E_\nu-\mathcal D_\nu\le\mathcal E_\nu$;
the forward implication adds the target-safe nonnegative diagonal. Also
$\mathcal G_\nu\ge-\mathcal D_\nu$, so no unproved two-sided estimate is
being smuggled into the equivalence.

## 3. Proof and formula audit

For every integer $h$, periodic lifting of the half-open circular cell
gives

\[
 \int_{I_\nu}e(h\theta)\,d\theta
 =\begin{cases}
 e(\nu h/M)\dfrac{\sin(\pi h/M)}{\pi h},&h\ne0,\\[5pt]
 M^{-1},&h=0.
 \end{cases}
\]

Thus wraparound creates no extra phase or mass. The parity average is

\[
 {1\over2}\sum_{\epsilon=0}^1(-1)^{\epsilon(m-m')}
 =\mathbf1_{m\equiv m'\pmod2}.
\]

Since both row divisors are odd, both odd--odd and squarefree even--even
product branches survive, and each unequal surviving gap is even with
$0<|dm-d'm'|<M$.

At an exact cross-row collision $dm=d'm'=N$, the parity and both phases
cancel and the cell kernel is $1/M$. Realness gives

\[
 2\sum_{d<d'}\chi_4(d)\chi_4(d')
 \lambda_N(d)\lambda_N(d')
 =(c_N^{\rm rem})^2-\sum_d\lambda_N(d)^2.
\]

If $t_N$ is the number of live odd-divisor incidences above $N$, then

\[
 \left|(c_N^{\rm rem})^2-\sum_d\lambda_N(d)^2\right|
 \le (t_N-1)\sum_d|\lambda_N(d)|^2.
\]

Using $t_N\le\tau(N)\ll_\eta X^\eta$, $M\asymp L^2$, and
$\Lambda_2\ll L^2X^\varepsilon$ proves the kernel's exact uniform bound

\[
 |\mathcal P_\nu|\ll_\varepsilon X^\varepsilon.
\]

No recombined cancellation is used in that estimate. Subtracting
$\mathcal P_\nu$ leaves exactly the displayed one-outer-real-part form
$\mathcal U_\nu$, with all nonzero even gaps and all literal fields still
present.

The K26 connector is also exact and only conditional. If
$\mathcal U_\nu\ll LX^\varepsilon$ on every near cell, then the collision
bound and row diagonal imply $\mathcal E_\nu\ll LX^\varepsilon$. The
near-cell Fejer envelopes sum to

\[
 \sum_{|\nu|\le\lceil\sqrt L\rceil}
 {M\over1+\nu^2}LX^\varepsilon
 \ll L^3X^\varepsilon.
\]

On the complement, $F_M\ll M/L$, and literal Parseval with $D_L$, not
incidence energy alone, gives $(M/L)D_L\ll L^3X^\varepsilon$. The
collective ordinary-zero term has the checked size

\[
 M(A_0D_L^{1/2}+A_0^2)
 \ll_\varepsilon L^3X^\varepsilon,
 \qquad A_0\ll_\eta L^2J^{-1}X^\eta,
\]

using $L^2\le J$. Finally

\[
 Q_M^*-Q_{R_0}^*
 =2(T_{26}+B_{\rm short})-\mathcal Z_{R_0,M}
\]

has the correct factor and sign. Solving for $T_{26}$ discards exactly
$-Q_{R_0}^*/2\le0$, and pays $B_{\rm short}$ once. Hence the kernel
verifies only the implication from its still-open local theorem to the
one-sided K26 endpoint.

## 4. First doubtful or unproved step

First issue found: **none**. The first unproved analytic step, rather than
an error in the kernel, is exactly (180.K8), equivalently (180.K14):

\[
 \mathcal U_\nu=\mathcal G_\nu-\mathcal P_\nu
 \ll_\varepsilon LX^\varepsilon
 \quad (|\nu|\le\lceil\sqrt L\rceil).
\]

It requires one factor $L$ of signed anti-concentration across distinct
divisor rows and unequal products before any rowwise, shiftwise, cellwise,
modewise, or divisorwise positive norm. The kernel consistently marks this
statement open. Its exact-product lemma, capacity controls, and self-return
identities neither prove nor disprove it.

## 5. Required controls and final-byte hygiene

| Control | Final outcome |
|---|---|
| physical row identity and one outer real part | **GREEN.** The $d=d'$ block is separated only after full row recombination. |
| one-sided equivalence | **GREEN.** Both directions and the safe negative floor use the correct signs. |
| half-open cells, wraparound, sinc, and zero gap | **GREEN.** The kernel is exact at $h=0$ and for wrapped cells. |
| parity and exact collisions | **GREEN.** Both same-parity branches survive; the collision factor and $O(X^\varepsilon)$ bound are correct. |
| near/far Fejer and Parseval | **GREEN CONDITIONALLY.** Near and far powers both restore $L^3$, assuming only the displayed open local theorem. |
| ordinary zero, short correction, exact terminal $M$ | **GREEN.** Zero modes are restored collectively, the correction is paid once, and no terminal link is rounded. |
| local and endpoint capacities | **GREEN.** Cauchy gives $L^2$ locally; the central Fejer height restores $L^4$. |
| complex, cosine, sign, constant-character, erased-selector controls | **GREEN AS NONLITERAL CONTROLS.** They exclude only coefficient-uniform or feature-insensitive mechanisms. |
| one row, one site, no-pair, hard boundary, product collar | **GREEN WITH THE STATED QUARANTINE.** None supplies literal density, lower mass, or an impossibility theorem. |
| blind-scope repair | **GREEN.** The unrestricted exact-product example is nonliteral, fiber Bessel is automatic at literal scale, and $D_L$ repairs the abstract far-arc gap. |
| literal and exponent quarantine | **GREEN.** No open owner or analytic target is promoted. |

The final kernel is valid UTF-8 without a BOM, ends in LF, and contains no
CR, TAB, FF, NUL, DEL, or other disallowed C0 byte. It has no replacement
character. Its 29 display-math openings and closings match, and its 149
left and right braces match. Final-byte hygiene is GREEN.

## 6. Dependencies and owner boundary

I read the final on-disk versions of the kernel, the formalized candidate,
all three reports, and all four reviews, including
`conductor_report_reconciliation.md` after its control-byte repair. I also
checked the Round-180 strategy, active campaign, authoritative graph, and
the accepted Round-175 endpoint kernel. The current graph hash is exactly
the campaign's frozen hash.

For graph purposes, reports, candidates, and reviews are evidence rather
than mathematical owners. The durable node's direct accepted mathematical
dependencies are the Round-175 whole-chain/endpoint obstruction, which
supplies $D_L$, the collective ordinary-zero and short-correction seams,
and the exact endpoint identity, and the Round-162 product-collar
obstruction for the named no-repeat control. Their earlier dependencies are
already represented transitively in the authoritative graph.

The new durable node may be owned only by `Codex conductor`; no temporary
Round-180 task ID belongs in an owner field. It is a subordinate
`proved_internal` obstruction with no implication edge and no blocker. It
may be attached only as inconclusive route evidence to the open hard-TOP
density/discrepancy owner, without changing that owner's status. This
matches the kernel's lines 437--442 and the reconciler's final state
boundary.

The exact artifacts audited were:

- `protocol.md`, `state/proof_obligations.yml`, and
  `state/active_campaign.yml`;
- `strategy/round180_m2_hard_top_t1_residual_k26_near_peak_row_gram_strategy.md`;
- the formalized Round-180 candidate;
- `literal_near_peak_row_gram_attack.md`,
  `fejer_cell_owner_capacity_audit.md`, and
  `blind_row_gram_rederivation.md`;
- `row_identity_fejer_connector_review.md`,
  `literal_selector_capacity_false_control_review.md`,
  `blind_post_unmask_row_gram_review.md`, and the repaired
  `conductor_report_reconciliation.md`; and
- the accepted Round-175 whole-chain and Round-162 product-collar kernels.

No external theorem, web source, or numerical experiment is a dependency.

## 7. Recommended state effect

Accept the durable kernel as GREEN evidence for exactly one subordinate
route-scoped obstruction:

`M9-M2-hard-top-t1-residual-k26-near-peak-row-gram-self-return-obstruction`.

Its promotable content is limited to the exact local self-return and
one-sided equivalence, the strict target-safe exact-product sector, the
conditional connector from the still-open unequal-product theorem to K26,
the sharp nonliteral $L^2/L^4$ capacity controls, and the repaired blind
scope. It has no implication edge.

Keep (180.K8), $Q_M^*$, K26, the complete residual scalar, full $t=1$,
every other hard-TOP channel, complete hard TOP, BAL, UNBAL, M9--M2, both
M1 routes, GAR, endpoint uniformity, M9, both bridges, the quarter theorem,
and every exponent owner unchanged. Do not infer literal lower mass from
any capacity control, and do not start Round 181 from this review.

**Final verdict: GREEN.**
