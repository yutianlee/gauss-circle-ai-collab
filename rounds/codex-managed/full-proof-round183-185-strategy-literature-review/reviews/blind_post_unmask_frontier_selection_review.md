# Blind post-unmask frontier-selection review

- Campaign: full-proof-round183-185-strategy-literature-review
- Round: 186
- Role: post-unmask seam reviewer
- Starting graph SHA-256: f43248060d7876a96d4554cd13372dbf267387bcbe44a832b87cd5f571801575
- Access mode: selected context from the task brief only
- Verdict: **REPAIR, then retain the selection and ranking**

## 1. Result: bounded repair, not rejection

The blind report has one substantive but bounded target mismatch. Its
displayed (R187-HH) asks for

\[
 \left|\Re \mathfrak C^{\rm high}_{Y,\sigma}\right|
 \ll_{\varepsilon,B}L^2X^\varepsilon.
\]

The accepted Fejer connector needs only a **one-sided upper bound** on the
single outer real part. The exact Round-187 target should instead be

\[
 \Re \mathfrak C^{\rm high}_{Y,\sigma}
 \le C_{\varepsilon,B}L^2X^\varepsilon.
\tag{R187-HH$^+$}
\]

The absolute value in the blind report is outside, not inside, the joint
sum. It therefore does not erase the two orientations or literal signs,
but it does demand an unnecessary lower bound for each dyadic block. The
stronger assertion would imply the required one; it must not be the
promotion gate or a stop rule.

This repair makes the first-ranked objective narrower and exactly
owner-compatible. It is not a reason to reject or reorder the blind
ranking. No seam is RED.

| Review seam | Verdict | Finding |
|---|---|---|
| Statement-only provenance | **GREEN** | The report declares and uses only protocol.md and blind_statement.md. It presents no graph status, source theorem, or hidden kernel formula as blind knowledge. |
| Exact high-\(h\) carrier, range, orientations, rows, and fields | **GREEN** | Its schematic carrier matches (K185.37): \(Y>H_B\), both \(\omega=\pm\), every primitive label and literal endpoint field, and one real part outside the complete sum. Round 187 must expand the schematic notation from the kernel. |
| Absolute-value placement | **REPAIR** | Replace \(\lvert\Re\mathfrak C_Y\rvert\ll\cdots\) by the explicit one-sided inequality (R187-HH\(^+\)). |
| Fejer owner connector | **GREEN after repair** | The sign in (K185.11) is \(+4\Re\mathfrak C_{R_0}^{(2)}\), so an upper bound, not a two-sided bound, is exactly sufficient. |
| Target, capacity, and missing power | **GREEN** | Positive capacity is \(O(YL^2X^\varepsilon)\), target is \(O(L^2X^\varepsilon)\), and the improvement over positive recombination is the full factor \(Y\). |
| Downstream scope | **GREEN** | Success closes only the exact \(t=1\) residual after accepted seams. Every \(t\ge2\) small-\(G\) incidence, the large-\(G\) near-resonant complement, and every parent remain separate. |
| Ranking versus current graph status | **REPAIR (labels only)** | The order remains defensible. K17a and K26 are unproved targets inside proved reduction/no-go nodes, not standalone open obligations; the two global bridges are derived under assumptions, not open analytic estimates. |

## 2. Exact statement and hypotheses

Fix real \(X\ge2\), one literal middle or lower hard-M1 residual shell
\(L\ge2\), \(\sigma\in\{+1,-1\}\), and fixed \(B>0\). Put

\[
 R_0=\lceil L\rceil,\qquad
 H_B=\lfloor(\log(2X))^B\rfloor .
\]

For each nonempty dyadic block \(Y<h\le2Y\), with \(Y>H_B\), define

\[
 \mathcal S_{Y,\sigma}=
 \sum_{\omega\in\{+,-\}}
 \sum_{\substack{\mathfrak f=(\kappa,g,h,U,v)\ {\rm satisfying}\ ({\rm K185.27})\\
                   Y<h\le2Y}}
 (-1)^{S_{0,\omega}}
 \sum_{t\in I_{\mathfrak f,\omega}}
 (-1)^tB_{\mathfrak f,\omega}^{\sigma}(t).
\]

The primitive domain is

\[
 \kappa,g,h,U,v>0,\quad
 \kappa,g,U\ {\rm odd},\quad
 (gU,v)=1,\quad (U,h)=1,\quad
 0<2\kappa gh<R_0.
\]

Here the canonical anchors, the separate \(U=1\) convention, the oriented
positive index sets, and \(B_{\mathfrak f,\omega}^{\sigma}\) are exactly
(K185.30)--(K185.35). Thus the Round-184 residual mask, zero extensions,
Fejer factor, both endpoint coefficients, phase, selector states, support
predicates, and both orientations remain inside one sum.

The corrected theorem is

\[
 \boxed{\Re\mathcal S_{Y,\sigma}
 \le C_{\varepsilon,B}L^2X^\varepsilon}
\tag{186.R1}
\]

uniformly throughout this literal range, including truncated terminal
blocks. No assertion about \(-\Re\mathcal S_{Y,\sigma}\) is required. A
proof of the stronger absolute estimate is admissible evidence, but
failure to prove it is not failure of (186.R1).

## 3. Proof/derivation and full ranking audit

Let \(D_{L,\sigma}\) and \(\mathfrak E_{R_0}\) be (K185.8)--(K185.9).
The accepted connector is

\[
 \mathfrak E_{R_0}
 \le 2D_{L,\sigma}+4\Re\mathfrak C_{R_0}^{(2)}.
\tag{K185.11}
\]

The diagonal is \(O(L^2X^\varepsilon)\), and the monotone plus
\(h\le H_B\) sectors have absolute contribution
\(O_{B,\varepsilon}(L^2X^\varepsilon)\). Since the real part is linear,
summing (186.R1) over \(O(\log X)\) nonempty dyadic blocks, with epsilon
rebudgeting, gives precisely the upper estimate needed in (K185.11).
Negative dyadic real parts help that upper estimate and need no control.
Then (K185.12), using \(M_L\asymp L^2\) and \(R_0\asymp L\), gives the
target \(L^{3/2}X^\varepsilon\) scalar estimate for the exact Round-184
residual.

For the complete correlation, positivity of \(\mathfrak E_{R_0}\) also
forces a target-scale lower bound after restoring the safe pieces. It does
not give such a lower bound for each separate high-\(h\) dyadic block.
Thus the bars in the blind blockwise theorem are genuinely stronger, not
merely cosmetic.

For fixed \((\kappa,g,h)\), each orientation has
\(O(L^2/(\kappa g))\) incidences. Positive summation over
\(Y<h\le2Y\), \(\kappa\), and \(g\), with logarithms absorbed in
\(X^\varepsilon\), is \(O(YL^2X^\varepsilon)\). Hence (186.R1) still
requires the complete factor \(Y\).

The twelve ranked frontiers reconcile with the graph as follows.

| Rank | Current graph status and exact scope | Verdict |
|---:|---|---|
| 1. Round-185 high-\(h\) | The finite reduction is proved internally; (186.R1) is its open next action inside the open hard-M1 small-\(t\) residual owner. | **GREEN after repair** |
| 2. Critical BAL | The double-far energy and its oscillatory remainder are open; the remaining-label owner is separately open. | **GREEN** |
| 3. K26 | Its reduction/no-go node is proved internally, while the literal unequal-product \(U_\nu\) estimate remains unproved and feeds the open hard-TOP density owner. | **REPAIR label; retain rank** |
| 4. Smooth M1 | The literal smooth blockwise parent is open, with the recorded \(X^{1/12}\) witness deficit. | **GREEN** |
| 5. GAR | GAR and its lower-radial blocker are open; total-active equivalence is proved and the alternative bridge is derived under assumptions. | **GREEN** |
| 6. UNBAL | The literal signed three-quarter parent remains open; its reductions and obstructions do not prove it. | **GREEN** |
| 7. Remaining hard TOP | The density-discrepancy owner and signed cone are open; K17a, K26, other \(t=1\), few-point, and collar scopes remain distinct. | **GREEN** |
| 8. Graded exponent lane | The local-moment and determinant-correlation nodes are open; internal \(1/3\) is proved and the Li--Yang benchmark is a separate accepted external dependency. | **GREEN** |
| 9. Remaining \(t\ge2\)/near resonance | These remain in the open hard-M1 small-\(t\) owner and are untouched by a complete \(t=1\) theorem. | **GREEN** |
| 10. Remaining-label BAL | This distinct owner is open and is not implied by the critical BAL child. | **GREEN** |
| 11. K17a | Its reductions and centered self-return are proved internally; the literal high-conductor estimate remains unproved inside those nodes. | **REPAIR label; retain rank** |
| 12. Endpoint/assembly | Endpoint uniformity is open; the standard and GAR bridges are already derived under assumptions and await their analytic hypotheses. | **REPAIR status wording; retain rank** |

Post-unmasking sharpens the K17a and K26 interfaces but also confirms
their self-return barriers. It gives no graph-based reason to displace the
smaller, newly exposed Round-185 target. Selection retention follows from
interface and owner leverage, not report agreement.

## 4. First doubtful or unproved step

The first unproved mathematical step remains (186.R1): no accepted
identity or estimate supplies the factor \(Y\) while retaining the literal
coefficient and complete high-\(h\) aggregate.

The blind report goes beyond the evidence when it says that every future
mechanism must couple all \(O(Y)\) height slices and must lose its saving
if the two orientations are separated. Positive capacity rules out the
listed positive recombinations; it does not prove that every possible
per-height or per-orientation signed estimate fails. Separate one-sided
orientation estimates would be stronger than needed and would imply
(186.R1). Round 187 should freeze the joint conclusion without prescribing
cross-orientation cancellation as the only possible proof mechanism.

## 5. Required controls and outcomes

1. **One-sided real part — REPAIR/PASS.** Replace every promotion-gate and
   stop-rule use of \(\lvert\Re\mathcal S_Y\rvert\) by (186.R1). A large
   negative dyadic real part is not a failure.
2. **Literal expansion — GREEN.** Freeze (K185.27) and
   (K185.30)--(K185.35), not only the schematic carrier. Retain both
   orientations, every row label, selector, zero extension, endpoint,
   Fejer weight, and sign.
3. **Capacity — GREEN.** Reproduce \(O(YL^2X^\varepsilon)\) and require
   the complete factor \(Y\). The recorded positive and self-return
   mechanisms remain parked only in their proved scopes.
4. **Orientation — REPAIR/PASS.** Reject moving absolute values inside
   orientation, row, or field sums and reject positive recombination at
   capacity. Do not reject a genuinely proved stronger signed bound merely
   because its proof treats orientations separately.
5. **Selector and endpoint — GREEN.** Retain the selector-empty case,
   \(R_0=\lceil L\rceil\), exact even-parity terminal weights, first block
   above \(H_B\), final truncated blocks, the \(U=1\) convention, and
   multiplicity one.
6. **Self-return and scope — GREEN.** A candidate must leave a strictly
   stronger signed estimate than the original product wave. Success
   propagates only through the accepted Fejer and Round-184 seams to the
   exact \(t=1\) residual; all siblings and parents remain separate.

No numerical control was needed or used.

## 6. Dependencies and exact artifacts used

Only the task brief and its permitted context were used:

1. protocol.md;
2. state/proof_obligations.yml, whose SHA-256 matches the frozen hash;
3. state/active_campaign.yml;
4. strategy/round186_full_proof_strategy_current_literature_review.md;
5. rounds/codex-managed/full-proof-round183-185-strategy-literature-review/blind_statement.md;
6. rounds/codex-managed/full-proof-round183-185-strategy-literature-review/reports/blind_round187_frontier_selection.md;
7. rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/synthesis.md; and
8. proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md.

No source card, web result, sibling Round-186 report, proof draft, prior
review, validation matrix, or unlisted artifact was used.

## 7. Recommended state effect and stop rule

**Recommended effect: revise the Round-187 objective wording, retain the
blind ranking and first-place selection, and make no proof-state or
exponent change.** Use (186.R1) with the literal carrier (K185.37). Record
K17a and K26 as open analytic frontiers inside proved reductions, and the
two global bridges as derived under assumptions.

Stop Round 187 if the best literal joint upper bound retains
\(Y^\theta\) for any fixed \(\theta>0\), if the gain appears only after
positive recombination or suppression of literal fields, or if the
argument self-returns. Do **not** stop merely because a dyadic lower bound
is unavailable, or because a valid stronger proof separately establishes
signed upper estimates for the two orientations.

Final recommendation: **REPAIR and retain**; no RED seam and no analytic,
parent, bridge, theorem, or exponent promotion.
