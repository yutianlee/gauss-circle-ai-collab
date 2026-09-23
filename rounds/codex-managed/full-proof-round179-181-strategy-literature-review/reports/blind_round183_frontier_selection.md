# Blind Round-183 frontier selection

- Campaign: `full-proof-round179-181-strategy-literature-review`
- Task: `blind_round183_frontier_selection`
- Round role: statement-only blind rederiver selecting one Round-183 objective
- Blind status: no graph, campaign, strategy, source-card, prior-round, sibling-report, or synthesis context consulted
- Generated: `2026-08-27T17:47:49.5302863+08:00`
- Graph hash: not supplied in the permitted statement-only context

## 1. Result

The unique recommended Round-183 analytic objective is the **complete hard-M1 small-\(t\) residual**, with the original signed coefficients and product geometry left intact:

\[
 \boxed{
 \left|\sum_{\substack{s>L,\ \mu^2(s)=1\\
                         1\le t<\lceil\sqrt L\rceil}}
 C_{L,X}^{\sigma}(st^2)e(\sigma t\sqrt{Xs})\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon
 }
 \qquad(\sigma\in\{+1,-1\}).
\]

Here “complete” means the displayed sum itself, not a coefficient-uniform majorant, a positive joint-\(t\) lift, a central-Mellin surrogate, or a complete Möbius recombination. Its exposed bottleneck is the \(t=1\) row: target capacity \(L^{3/2}X^\varepsilon\), coefficient-uniform capacity \(L^2X^\varepsilon\), and therefore an exact missing saving \(L^{1/2}\).

This choice has the best combination of a literal formula, a quantified deficit, a proved target-safe complement, and parent-level leverage. If proved and successfully seamed to the two already-safe sectors, it would complete the direct hard-M1 parent. It would not by itself prove blockwise M1, the M2 parents, endpoint uniformity, either global bridge, or the quarter theorem.

## 2. Exact statement and hypotheses

Define, for each sign,

\[
S_{\sigma}(L,X):=
\sum_{\substack{s>L,\ \mu^2(s)=1\\
                  1\le t<\lceil\sqrt L\rceil}}
C_{L,X}^{\sigma}(st^2)e(\sigma t\sqrt{Xs}).
\]

The proposed theorem is: for every \(\varepsilon>0\), both signs \(\sigma\in\{+1,-1\}\), and every \((L,X)\) in the underlying hard-M1 block's admissible range,

\[
|S_\sigma(L,X)|\le C_\varepsilon L^{3/2}X^\varepsilon,
\]

with \(C_\varepsilon\) uniform in the full admissible range, including its endpoints. The numerical admissible range and the internal definition of \(C_{L,X}^{\sigma}\) are not present in the allowed blind packet, so they must be imported verbatim into the Round-183 brief before work begins; no range or coefficient convention may be guessed. The fixed hypotheses visible here are:

1. \(s>L\) and \(s\) is squarefree, expressed by \(\mu^2(s)=1\);
2. \(1\le t<\lceil\sqrt L\rceil\), with the ceiling and strict upper inequality unchanged;
3. the coefficient is the literal \(C_{L,X}^{\sigma}(st^2)\), not an arbitrary sequence satisfying only a size bound;
4. the oscillation is the literal signed phase \(e(\sigma t\sqrt{Xs})\);
5. the estimate is required separately for both signs;
6. no external theorem is assumed.

The promotion gate is all of the following, conjunctively:

- a complete analytic proof of the displayed bound with no hidden \(L^\delta\) loss;
- uniformity over the exact hard-M1 range and its endpoints;
- an explicit use of a genuine property of the Vaaler coefficients and/or \(\chi_4\) that is destroyed by the unsigned or adversarial-coefficient controls;
- a seam derivation showing that this bound plus the proved \(s\le L\) and \(s>L,\ t\ge\lceil\sqrt L\rceil\) estimates yields \(\mathcal T_{L,\sigma}^{M1}\ll_\varepsilon L^{3/2}X^\varepsilon\) for each sign;
- independent checks of normalization, coefficient/character algebra, the squarefree-product multiplicity, exponent bookkeeping, and endpoint uniformity.

Only that gate could justify promotion of the direct hard-M1 parent. The present selection report meets none of those proof gates and changes no status.

## 3. Proof or derivation

The ranking uses a lexicographic rule suited to one frozen analytic round: (i) the frontier must be upstream and lawful now; (ii) it should have a literal, falsifiable interface; (iii) success should discharge the largest exact owner available from that interface; (iv) the missing saving and known obstructions should be quantified; and (v) the conclusion obtained from this frontier alone should materially advance the quarter-theorem route. Powers of \(L\), \(X\), and \(Y\) are not compared across frontiers unless the statement itself supplies their relation.

| Rank | Frontier | Exact target, exposed capacity, and missing saving | Strongest conclusion from this frontier alone | Why it ranks here |
|---:|---|---|---|---|
| 1 | Hard-M1 small-\(t\) residual | Literal \(S_\sigma(L,X)\ll_\varepsilon L^{3/2}X^\varepsilon\); the \(t=1\) coefficient-uniform capacity is \(L^2\), so the missing saving is \(L^{1/2}\). | Completes the direct hard-M1 parent after the exact product-split seam to the two safe sectors. | It is the only listed parent-level residual having simultaneously a displayed formula, exact safe complement, exact bottleneck, and smaller stated \(L\)-power than the other displayed \(L\)-frontiers. |
| 2 | K26 unequal-product near-cell form | \(\mathcal U_\nu\ll_\varepsilon LX^\varepsilon\); coefficient-uniform positivity has local capacity \(L^2\) and endpoint capacity \(L^4\); the packet states that one factor \(L\) is missing. | Completes the remaining unequal-product part of K26 because the physical diagonal and equal-product cross-row collisions are safe; other hard-TOP channels remain. | It is the next most literal and falsifiable interface, but asks for a larger stated \(L\)-saving and closes a subowner rather than the direct hard-M1 parent. |
| 3 | Critical BAL | Target \(L^3\), capacity \(L^4\), missing saving \(L\), on the persistent critical \(j=1\) double-far energy. | Closes one of two open BAL scopes. | The deficit is exact, but no literal energy formula is exposed and the independent remaining-label/quantifier owner would still prevent BAL closure. |
| 4 | Smooth direct M1 | Exact displayed formula and capacity are absent; the stated deficit is \(X^{1/12}\). | Completes the independent smooth direct-M1 parent. | Parent leverage is high, but the blind packet does not contain a freezeable formula or enough scale information to compare its \(X^{1/12}\) gap with an \(L\)-gap. |
| 5 | GAR | Complete global angular-radial theorem; bound, capacity, and deficit are not stated. The live obstruction is a low-two-adic lower-radial survivor. | Replaces the conjunction of both direct M1 parents, but does not prove blockwise M1. | Its leverage is the strongest M1 leverage, but its remaining survivor has no literal interface in the packet, so it is too broad to be a controlled one-round objective. The hidden connector is substitution for the conjunction, not an implication to either direct parent. |
| 6 | UNBAL | A complete signed varying-modulus literal-matrix vector theorem; no quantitative capacity or missing power is supplied. | Completes the UNBAL M2 parent. | This is a full-parent payoff, but “complete theorem” is not yet a bounded analytic interface. Arbitrary-coefficient or fixed-modulus substitutes would miss the signed varying-modulus connector. |
| 7 | Remaining hard TOP | Independent \(t=1\), few-point, and collar channels; no common formula, capacity, or single missing saving is supplied. | At most closes those residual TOP channels; K17a and K26 still have their own survivors. | It is a bundle of independent problems rather than one frozen objective and therefore violates the desired mathematical-interface granularity. |
| 8 | Graded exponent/local moment | Cluster target \(Y^{1/2+\varepsilon}\); best complete internal bound \(Y^{35/48+\varepsilon}\); missing saving \(Y^{11/48}\). | Certifies an exponent below \(1/3\), but not the quarter theorem. | It is quantitative and self-contained, but its stated conclusion neither reaches \(1/4\) nor is stated to improve the separately accepted \(0.3144831759740614\ldots\) exponent. |
| 9 | Remaining-label BAL | Separate remaining-label/quantifier owner; formula, capacity, and missing saving are not supplied. | Closes only the second BAL scope; the critical \(j=1\) scope remains. | Its logical connector may be necessary, but it is not yet a sharp analytic statement and cannot be conflated with the critical-energy estimate. |
| 10 | K17a | The complete high-conductor centered defect returns exactly to the original literal orientation block after safe terms are removed; no reduced capacity or missing saving is exposed. | A genuinely new direct estimate could close the K17a survivor, but the recorded reductions alone do not advance it. | Every named simple mechanism is parked, and the current “reduction” is circular at the hard core. It is less ready than the objectives with an actual reduced form. |
| 11 | Endpoint/assembly and global bridges | Uniform endpoint/bridge/assembly interface; no independent capacity or saving is stated. | Supplies downstream wiring only after the upstream M1 and M2 parents exist. | It is strictly downstream. Proving a formal implication with open antecedents cannot promote an analytic parent or improve the exponent. |

The rank-1 choice follows directly. Compared with K26 and critical BAL, it asks for \(L^{1/2}\), rather than the stated \(L\), beyond the respective coefficient-uniform capacities, and success reaches a whole direct parent through an already exact split. Compared with smooth M1, GAR, and UNBAL, it is fully specifiable from the blind packet. Compared with graded improvement, its success lies on a necessary quarter-theorem route. Compared with K17a and the aggregate remaining-TOP/BAL scopes, it has a noncircular single kernel. Endpoint assembly is not eligible until its inputs exist.

The hidden connector that makes the selection valuable is

\[
\begin{aligned}
\mathcal T_{L,\sigma}^{M1}
={}&\bigl(s\le L\bigr)
+\bigl(s>L, t\ge\lceil\sqrt L\rceil\bigr)
+S_\sigma(L,X),
\end{aligned}
\]

where the first two sectors are already target-safe. This is a genuine complementary partition of the exact product split. In contrast, complete Möbius recombination is not a connector to a smaller problem: it returns to the original cone modulo a target-safe correction.

## 4. First doubtful or unproved step

The first unproved step is a concrete \(L^{1/2}\) cancellation mechanism at the \(t=1\) bottleneck (or a rigorously coupled signed mechanism in the full small-\(t\) sum that compensates for that bottleneck) which depends on the actual \(C_{L,X}^{\sigma}\), Vaaler, and/or \(\chi_4\) structure. In its isolated form the obstruction is

\[
\sum_{\substack{s>L\\\mu^2(s)=1}}
C_{L,X}^{\sigma}(s)e(\sigma\sqrt{Xs}),
\]

whose coefficient-uniform treatment has capacity \(L^2\) against the required \(L^{3/2}\). No identity in the permitted statement supplies the required cancellation. Merely using squarefreeness, taking absolute values, summing positive \(t\) rows, applying only a central Mellin estimate, or undoing the product split does not prove it.

The exact admissible \((L,X)\)-range and the explicit coefficient formula are also withheld by the blind protocol. They are not mathematical gaps in the selected statement's source context, but they are mandatory inputs to the Round-183 frozen brief; without them, endpoint uniformity and the claimed use of special coefficients cannot be audited.

## 5. Required control test and outcome

1. **Unsigned/adversarial coefficient control.** Replace the signed summand by its absolute value, or allow coefficients of the same permitted pointwise size to align with \(e(-\sigma t\sqrt{Xs})\). The supplied \(t=1\) capacity is \(L^2\), so a coefficient-uniform proof misses the target by \(L^{1/2}\). **Outcome:** the control rejects every proof that would also establish the unsigned or arbitrary-coefficient analogue. A successful proof must identify the exact Vaaler/\(\chi_4\) identity it loses under this replacement.
2. **Complete Möbius-recombination control.** Recombine all product variables and compare the resulting hard term to the input cone. **Outcome:** the hard term is the original cone modulo a target-safe correction, so the operation gives no missing \(L^{1/2}\) and is rejected as circular.
3. **Positive joint-\(t\) and central-Mellin controls.** Test whether the proposed gain remains after replacing signed \(t\) interaction by a positive lift, or whether it comes solely from a central Mellin estimate. **Outcome:** both mechanisms are parked in the allowed statement and cannot serve as the missing step.
4. **Boundary and sign control.** Re-run the final inequalities for each sign separately and at both endpoints of the exact admissible \((L,X)\)-range, retaining \(t<\lceil\sqrt L\rceil\) literally. **Outcome:** pending because the range and coefficient definition are deliberately absent from the blind packet; this must be a mandatory Round-183 exit gate, not silently assumed.

No numerical experiment is proposed: these are algebraic false controls, and computation could not certify the uniform asymptotic estimate.

The stop rule is immediate and falsifiable. Stop the Round-183 route and record a no-go result as soon as its hard estimate is shown to be coefficient-uniform/positive at \(t=1\), to rely only on either parked mechanism, or to reproduce the original cone after recombination. Also stop without promotion if the result is only average in \(X\), covers only one sign, excludes an endpoint, changes the coefficient sequence, or incurs any uncompensated power beyond \(L^{3/2}X^\varepsilon\). Do not roll from this failed objective into another frontier inside the same round.

## 6. Dependencies and exact artifacts used

Only these two artifacts were read or used:

1. `protocol.md`
2. `rounds/codex-managed/full-proof-round179-181-strategy-literature-review/blind_statement.md`

No proof graph, active campaign, strategy file, source card, prior-round artifact, sibling report, computation, or external source was read. Accordingly, this report assumes no source theorem and does not claim a graph hash, hidden normalization, parameter range, or coefficient formula not contained in those two files.

## 7. Recommended state effect

**No change.** Freeze the displayed hard-M1 small-\(t\) estimate as the sole Round-183 analytic objective, after the conductor supplies the exact coefficient definition and admissible endpoint range in its brief. Retain every current proof status and every current exponent.

If the promotion gate is later met, the strongest justified state effect is promotion of the **direct hard-M1 parent only**, via the exact three-sector product split. Smooth direct M1, GAR, K17a, K26, remaining hard TOP, both BAL scopes, UNBAL, endpoint/assembly, both global bridges, and the unrestricted quarter theorem all remain outside that promotion. If the stop rule fires, retain the parent as open and add only the resulting obstruction/no-go statement.
