# Blind post-unmask frontier-selection review

- Campaign: `full-proof-round187-189-strategy-literature-review`
- Round: 190 post-unmask seam review
- Reviewed graph SHA-256: `15c770023b649a95596b223e15370657836e230580f0d2f31f5d30c615a98568`
- Role: former blind rederiver, now post-unmask reviewer
- Verdict: **REPAIR**
- Numerical theorem evidence: none

## 1. Result

**Post-unmask reconciliation lemma.** The blind report selected the correct unique frontier: the exact Round-189 projectively fast complement remains the best single Round-191 objective. Its owner scope, deficit, and downstream limitation agree with the authoritative graph. However, the displayed blind estimate

\[
 \sum_{\omega,v}\mathsf V(W_{\kappa,u,mq,v,\omega}^{\sigma})
 \ll_{B,\varepsilon}
 \frac{H_Bm\kappa uJ}{q}X^\varepsilon
 \tag{R191-FB}
\]

is a **positive total-variation gate**. It cannot be called a signed orientation-paired seam: every `\mathsf V(W)` is nonnegative and separately absolutized before the `\omega,v` sum, and no outer real part or cross-`(\omega,v,h)` cancellation remains on its left-hand side.

The selection therefore survives, but its proposed mechanism and formula require repair. The single objective should be the exact fast-complement relation (190.6), attacked through the joint signed height-jump packet (190.9) and estimate (190.10). Estimate (R191-FB) should remain only as the sufficient positive-BV benchmark recovered by taking absolute values in the signed packet.

This is **REPAIR**, not GREEN, because the blind report conflated a valid positive sufficient condition with the genuinely new signed seam. It is not RED because the frontier choice, exact local deficit `Y/(H_Bm)`, owner limitation to the original-`t=1` residual, false-control direction, and no-promotion recommendation are all retained.

## 2. Exact statement and hypotheses

Put `Q=H_B=\lfloor(\log(2X))^B\rfloor`. Fix a nonempty literal hard-M1 residual shell, a dyadic block `Y<h\le2Y` with `Y>Q`, `\sigma\in\{\pm1\}`, and an admissible tuple

\[
 U=mq>4Q,\qquad q>Q,\qquad Qm<Y,
 \qquad (a,q)=1,qquad m|a|_q>Q.
\]

Let

\[
 j_q(a,v)=|a\bar v_q|_q,qquad
 T_Q=\min\!\left\{\frac{q-1}{2},
 \left\lfloor\frac{Qmq}{Y}\right\rfloor\right\},
\]

and restrict to the exact fast complement `j_q(a,v)>T_Q`. The literal aggregate from the full-graph report is

\[
\begin{aligned}
 \mathscr F_{Y,Q}^{\sigma}
 :=\sum_{\omega\in\{+,-\}}
 \sum_{\substack{\mathfrak f:\,Y<h\le2Y\\
                  U=mq>4Q,\ q>Q,\ Qm<Y}}
 \sum_{\substack{a\bmod q:\,(a,q)=1\\
                  m|a|_q>Q\\j_q(a,v)>T_Q}}
 \frac1m c_q(a)
 e\!\left(\frac{\epsilon_\omega a\bar v_qh}{q}\right)
 A_{\mathfrak f,\omega}^{\sigma}.
\end{aligned}
\]

The **one and only Round-191 objective** is

\[
 \boxed{\Re\mathscr F_{Y,Q}^{\sigma}
 \ll_{B,\varepsilon}L^2X^\varepsilon.}
 \tag{190.6}
\]

For a fixed admissible `(\kappa,u,m,q,a)` and a nonempty dyadic fast band

\[
 J\le j_q(a,v)<2J,
\]

let `W_{\kappa,u,mq,v,\omega}^{\sigma}(h)` be the exact zero-extended height sequence, including every common-range term, affine birth/death, arithmetic mask, selector, profile, floor, star, crossing, endpoint, phase, sign, and zero extension. Define

\[
 \Delta^-W(h)=W(h)-W(h-1),\qquad
 z_{\omega,v}=e(\epsilon_\omega a\bar v_q/q).
 \tag{190.7}
\]

Fast-band admissibility gives `z_{\omega,v}\ne1`, and zero extension gives the endpoint-exact Abel identity

\[
 \sum_hW_v(h)z_{\omega,v}^h
 =\frac1{1-z_{\omega,v}}
   \sum_h\Delta^-W_v(h)z_{\omega,v}^h.
 \tag{190.8}
\]

The repaired joint packet is

\[
 \mathscr J_{\kappa,u,m,q,a,J}^{\sigma}
 :=\sum_{\substack{\omega,v\ {\rm literal}\\
                    J\le j_q(a,v)<2J}}
 \frac1{1-z_{\omega,v}}
 \sum_h\Delta^-W_{\kappa,u,mq,v,\omega}^{\sigma}(h)
 z_{\omega,v}^{h},
 \tag{190.9}
\]

and the genuinely new sufficient seam is

\[
 \boxed{
 |\mathscr J_{\kappa,u,m,q,a,J}^{\sigma}|
 \ll_{B,\varepsilon}Qm\kappa uX^\varepsilon.}
 \tag{190.10}
\]

The modulus in (190.10) is outside the complete joint `\omega,v,h` jump aggregate. Thus (190.10) may be called a **joint signed both-orientation height-jump coboundary seam**. It should not yet be called an “orientation pairing” or “projective-difference” theorem in the stronger sense of an explicit involutive pairing or a discrete difference across neighboring projective slopes: neither such identity is present in (190.9).

**Promotion gate.** Prove (190.10), or an exactly ledger-equivalent joint signed estimate, uniformly for every admissible tuple and nonempty fast band; independently verify (190.8), `|1-z|^{-1}\asymp q/J`, the `m^{-1}` lift, coefficient mass, divisor ledger, band partition, saturated empty case, endpoints, and final summation with only logarithmic losses; then deduce (190.6). The maximal downstream effect is closure of the subordinate exact original-`t=1` residual after accepted connectors. Every original `t\ge2` small-`G` incidence, the large-`G` near-resonant complement, and both direct-M1 parents remain unproved.

**Stop rule.** Stop when an absolute value is moved inside the joint jump packet, orientations are separately absolutized, masks or endpoints are frozen without proof, the primitive `Y/Q` deficit reappears, a positive power is hidden in `X^\varepsilon`, the known bad prime slope would be contradicted by a uniform prefix lemma, or an unstated source theorem or connector is required. Do not pivot within Round 191 to another owner.

## 3. Proof or derivation

### 3.1 Why (R191-FB) is positive, not signed

For one literal row, (190.8) and the triangle inequality give

\[
 \left|\sum_hW_v(h)z_{\omega,v}^h\right|
 \le |1-z_{\omega,v}|^{-1}
     \sum_h|\Delta^-W_v(h)|.
\]

On `J\le j_q(a,v)<2J`,

\[
 |1-z_{\omega,v}|^{-1}\asymp \frac qJ.
\]

Therefore

\[
 |\mathscr J|
 \le \frac qJ
 \sum_{\omega,v}\mathsf V(W_v).
\]

If (R191-FB) holds, this yields (190.10) at scale

\[
 \frac qJ\cdot\frac{Qm\kappa uJ}{q}X^\varepsilon
 =Qm\kappa uX^\varepsilon.
\]

This proves that (R191-FB) is a valid sufficient positive gate. It also proves the terminology defect: the derivation obtains it only after the jump of each row is replaced by its absolute variation and then summed positively over orientations and projective residues. Cross-row, cross-orientation, and cross-height cancellation has already been discarded. Conversely, (190.10) can hold because of cancellation inside (190.9) even when (R191-FB) is false. The two statements are not equivalent.

The blind sentence claiming that every literal field remains “coupled under the single outer real part” inside (R191-FB) is consequently inconsistent with its displayed left-hand side. Literal fields may remain present inside each `W`, but their interactions are separately normed and no common outer real part survives.

### 3.2 Ranking audit against the full graph

The authoritative graph has 391 obligation records and 1,644 rejected-claim records at the stated hash. The selected packet is a strict proved-reduction child of the open `M9-M1-hard-top-high-radical-small-t-residual-estimate`, which in turn feeds the open hard direct-M1 parent `M9-M1-top-endpoint-signed-cone`. The graph's next action expressly allows either the positive fixed-`a` BV target or a genuinely joint signed substitute with the same final ledger. Hence (190.10) is owner-compatible.

| Blind frontier/rank | Full-graph audit | Reconciled effect |
|---|---|---|
| Fast complement, 1 | Correct first choice. Exact target is (190.6); fixed-band positive gate has deficit `Y/(Qm)`, primitive `Y/Q`. | **Retain rank 1; repair the seam to (190.9)--(190.10).** |
| GAR, 2 | Owner leverage was correctly identified: complete GAR replaces total active M1 only on the alternative route. But the actual lower-radial survivor has absolute `R^2` against `R` and a deep face `M` against `M^{3/4}`, and its literal scope covers many layers and the cross owner. | Over-ranked in the blind table; place below the two remaining hard-M1 incidence leaves for round-level tractability. |
| UNBAL, 3 | It is a full M2 parent, but the full graph supplies target `M^{3/4}` against raw `M`, missing `M^{1/4}`, for a complete varying-modulus literal matrix. | Correct high nominal leverage, but over-ranked as a one-round objective because its interface is much larger than the selected leaf. |
| K26, 4 | Full graph confirms local `L^2` versus `L`, missing `L`, and that success closes only K26, one residual-scalar route; other TOP channels survive. | Scope assessment retained; exact formula remains too broad for reselection. |
| Critical BAL, 5 | Full graph confirms `L^4` capacity versus `L^3`, missing `L`, and a separate BAL-rest owner. | Scope and power retained. |
| Merged `t\ge2`/near-resonant hard-M1, 6 | The blind packet grouped two graph-independent leaves. Small-`G`, `t\ge2` has `L^2` versus `L^{3/2}`, missing `L^{1/2}`. Large-`G` near resonance has `L^{7/4}` versus `L^{3/2}`, missing `L^{1/4}`. | **Statement repair:** split them. They rank immediately after the fast complement because they are the other leaves nearest the same hard-M1 owner. |
| Smooth M1, 7 | Full graph confirms capacity `X^{1/3+o(1)}` against target `X^{1/4+\varepsilon}`, missing `X^{1/12}`, and independence from hard M1. | Retain as a major but broader frontier. |
| Remaining hard TOP, 8 | Full graph separates residual `t=1`/few-point/collar channels from complete hard TOP. Typical scalar capacity is `L^2` against `L^{3/2}`; complete energy has `L^3` against `L^2`. K17a/K26 alone close neither complete TOP nor its density owner. | **Statement repair:** distinguish residual channels from the complete hard-TOP parent. |
| Graded lane, 9 | Full graph confirms `Y^{35/48}` versus the `Y^{24/48}` local target, missing `Y^{11/48}`; strict sub-`1/3` begins below `Y^{27/48}`. The lane belongs to neither quarter tree. | Retain low quarter-route rank and exponent quarantine. |
| Remaining-label BAL, 10 | Full graph supplies target `L^{3/2}` against worst packet `L^2`, missing `L^{1/2}` or `X^{1/12}` at the worst physical scale, plus a separate exact-square boundary. | Blind scope was right but quantitatively incomplete; repair the ledger. |
| K17a, 11 | Full graph gives exact-`q` capacity `Lq\log(2q)` versus `L`; even square-root conductor gain leaves `L\sqrt q\log q`. The centered defect self-returns and K17a is only one residual route. | Low rank retained. |
| Endpoint/assembly, 12 | The graph confirms it inherits open analytic parents and supplies no independent cancellation. Standard and GAR route endpoint quantifiers are distinct. | Last rank retained. |

The post-unmask refinement changes several internal ranks and splits two grouped frontiers, but it does not create a competitor that beats the fast complement. The literature report also supplies no exact theorem import through the dated 2026-08-29 corpus that would force reselection. Thus the campaign still has exactly one selected objective, not a vote or a hybrid route.

### 3.3 Owner scope and single-objective check

The selected fast complement is only one strict leaf inside the hard high-radical small-`t` residual. Even complete success closes at most the exact original-`t=1` residual after the accepted Round-184--189 connectors. It does not close the original `t\ge2` small-`G` leaf or the large-`G` near-resonant leaf, so it does not prove `M9-M1-hard-top-high-radical-small-t-residual-estimate`, `M9-M1-top-endpoint-signed-cone`, `M9-M1`, `M9`, either bridge, the quarter theorem, or any exponent.

There is no two-objective conflict if the campaign is worded correctly:

\[
 \text{objective: (190.6)}
 \quad\text{via the one proposed sufficient seam (190.10)}.
\]

Treating (R191-FB) and (190.10) as two coequal Round-191 targets would violate the single-objective rule. The former is only a benchmark showing what a positive proof would have to achieve; the latter is the new analytic seam.

## 4. First doubtful or unproved step

The first unproved step is (190.10): no accepted result gives correlation among the literal height jumps after common-range differences, births, deaths, masks, profiles, floors, endpoints, Fejer factors, phases, orientations, and zero extensions are retained. The phrase “orientation-paired” in the blind report did not supply such a correlation or an actual pairing map. Pointwise boundedness gives only the available `Y\kappa uJ/q` variation scale, and the known odd-prime slope control rules out a uniform polylogarithmic centered-kernel prefix substitute.

After (190.10), the next seam requiring independent replay is the implication to (190.6): exact Abel normalization, `q/J`, `m^{-1}c_q(a)`, lift uniqueness, `q\mid U\mid u`, coefficient mass, `\tau_3(u)`, saturated bands, dyadic summation, and endpoint conventions must lose only logarithms. Round 190 proposes this ledger; it does not prove the analytic estimate.

## 5. Required control tests and outcomes

1. **Positive-variation placement — FAIL for the blind terminology, PASS after repair.** In (R191-FB), total variation occurs before summing `\omega,v`; it is not signed. In (190.9), the absolute value occurs only after the full literal jump aggregate.
2. **Outer-real-part/orientation control — FAIL for “coupled under one real part” in the blind display, PASS for (190.9)--(190.10).** Both orientations are joint only in the repaired packet. Separately bounding them returns positive capacity.
3. **Abel normalization — PASS algebraically.** Zero extension gives `\sum_h\Delta^-W(h)z^h=(1-z)\sum_hW(h)z^h`; fast bands have `z\ne1`; and `|1-z|^{-1}\asymp q/J` on the centered dyadic band.
4. **Primitive deficit — PASS as a diagnostic.** At `m=1`, the seam must recover the full `Y/Q` factor. Neither lift averaging nor `X^\varepsilon` may conceal it.
5. **Bad-slope false control — PASS.** The repaired objective does not assert a uniform centered-kernel prefix theorem; the odd-prime linear prefix remains compatible with possible cancellation in the complete literal joint packet.
6. **Unsigned/adversarial control — PASS after repair.** If actual signs, `\chi_4`, phases, or orientations are replaced by positive/adversarial coefficients, the route must break and revert to the `Y`-scale. A proof surviving that replacement is not owner-compatible.
7. **Scope control — PASS.** Original `t\ge2`, near resonance, smooth M1, GAR, all M2 owners, endpoints, bridges, and exponents remain separate.
8. **Single-objective control — PASS after wording repair.** Select (190.6) through (190.10) only; retain (R191-FB) as a benchmark and do not open a second frontier.
9. **Source control — PASS.** The current-primary report finds no exact import in its dated corpus; no source theorem is assumed here.

## 6. Dependencies and exact artifacts used

This post-unmask review used exactly:

1. `protocol.md`;
2. `state/proof_obligations.yml`;
3. `state/active_campaign.yml`;
4. `rounds/codex-managed/full-proof-round187-189-strategy-literature-review/reports/full_graph_frontier_reconstruction.md`;
5. `rounds/codex-managed/full-proof-round187-189-strategy-literature-review/reports/current_primary_literature_reassessment.md`;
6. `rounds/codex-managed/full-proof-round187-189-strategy-literature-review/reports/blind_round191_frontier_selection.md`;
7. `rounds/codex-managed/full-proof-round187-189-strategy-literature-review/reviews/conductor_round190_report_reconciliation.md`.

The graph was parsed read-only at the stated hash; its 391 obligation and 1,644 rejected-claim records were checked only for this seam and owner audit. No source theorem was imported, no numerical experiment was used, and no graph or shared-state file was edited.

## 7. Recommended state effect

**REPAIR.** Retain `strategy_frontier_retained` and the exact fast complement as the unique Round-191 selection, but repair the Round-191 statement as follows:

1. relabel (R191-FB) the **positive total-variation sufficient benchmark**, not the signed seam;
2. remove the claim that its left-hand side preserves one outer real part or cross-orientation cancellation;
3. freeze the single objective as (190.6), attacked through (190.9)--(190.10);
4. name the new seam the **joint literal signed height-jump coboundary seam**; avoid claiming a projective-difference or explicit orientation-pairing identity until one is proved;
5. split the blind merged `t\ge2` and near-resonant frontier into two independent graph leaves, refine the full-graph power ledger, and rank both directly below the selected fast complement;
6. permit no analytic, parent, endpoint, bridge, source, theorem, or exponent promotion in Round 190.

The repair changes strategy wording and the proposed analytic interface only. It does not change any accepted mathematical status or exponent.
