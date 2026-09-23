# Round 166 statement-only blind frontier priority rederivation

Role: statement-only blind rederiver
Round assessed: 166
Prospective round: 167

## 1. Result

**Priority result.** The unique recommended Round-167 target is the minimal-window actual-coefficient signed inequality

\[
 \boxed{
 \Re\mathfrak C_{R_0,2,{\rm opp},\,g<\gamma L}^{\rm rem}
 \ll_{\gamma,\varepsilon}L^2X^\varepsilon,
 \qquad R_0=\lceil L\rceil .}
 \tag{R167.1}
\]

This is exactly (B166.1), with neither an absolute value nor an unsigned/adversarial replacement. It is ranked first because it is the smallest explicit inequality with an already-declared connector to an open owner, it asks for the same one-power saving as the maximal-window alternative, and it avoids the latter's additional long-shift and budget-saturation seam. This is a priority recommendation, not a proof of (R167.1), and it changes no proof status.

There is also a precise method-level no-go conclusion: coefficient energy, support length, parity, and fixed-shift Cauchy alone cannot supply the required estimate. They stop one factor (L) above both explicit targets. A successful Round 167 must therefore exhibit cancellation tied to the actual signed coefficients and/or their phase-arithmetic structure.

The research-priority ranking is as follows. It ranks expected useful progress from the information in the blind statement, not the logical importance of the parent nodes.

| Rank | Frontier | Exact owner leverage | Visible saving and connector risk | Why it is below the preceding frontier |
|---:|---|---|---|---|
| 1 | (B166.1) | Closes the stated hard-TOP residual scalar, and only that scalar | Requires a factor (L) beyond short-shift fixed-Cauchy summation; minimal-window connector is already stated | Unique recommendation |
| 2 | (B166.2) | Closes the same residual scalar, and only that scalar | Also requires a factor (L); the maximal-window route adds (\asymp L^2) possible shifts and its (r<R_0) Cauchy contribution already lives at the full (L^3) target scale | Same owner leverage and saving as rank 1, but strictly more summation and connector exposure |
| 3 | Direct residual-scalar attack | Potentially closes exactly the same scalar and could be weaker than either sufficient aggregate | Neither the scalar formula nor a quantitative saving mechanism is supplied | It is not yet a freezeable analytic inequality; any advantage from cross-piece cancellation is only hypothetical |
| 4 | Remaining hard-TOP channels | Advances other pieces of the hard-TOP parent | Required saving is unspecified; the residual and near collars still remain, followed by recombination | Solving one such channel cannot remove the presently isolated residual obstruction, and no new cancellation mechanism is visible |
| 5 | Balanced smooth M2 | Would close one of three indispensable M2 parents if a complete theorem were proved | Required saving and exact signed inequality are unspecified | Higher nominal owner leverage than a residual lemma, but no bounded proof kernel or new cancellation mechanism is exposed |
| 6 | Unbalanced smooth M2 | Would close one of three indispensable M2 parents if a complete theorem were proved | Same absence of a quantified saving; unbalanced-to-endpoint assembly is an additional likely seam | It is essentially tied with balanced M2 on the supplied evidence; the ordering is only a scope/endpoint tie-break, not a mathematical claim |
| 7= | First direct M1 parent | Closes only one of the two independent M1 parents on the standard route | Exact inequality and saving are unspecified; the other M1 parent, all three M2 parents, and endpoints remain | No local mechanism is visible and the residual hard-TOP frontier is much more sharply isolated |
| 7= | Second direct M1 parent | Same as the first direct M1 parent | Same | The statement gives no basis for distinguishing the two direct parents |
| 9 | Global M1 alternative | A complete theorem would replace both direct M1 parents | It is a global angular-radial theorem with the largest hidden assembly surface; it still leaves all three M2 parents and does not prove standard blockwise M1 | Its formal leverage is high, but no new global cancellation mechanism is visible and its breadth makes it the least controlled next-round target |

The balanced/unbalanced and two-direct-parent orderings should not be read as confidence comparisons stronger than the statement permits. All are strictly below (R167.1) because none comes with an equally exact, local, quantitatively calibrated inequality.

## 2. Exact statement and hypotheses

The blind priority proposition uses only the following hypotheses.

1. The target theorem is conditional on M9.
2. The standard M9 route needs two independent M1 parents, hard-TOP M2, balanced smooth M2, unbalanced smooth M2, and endpoint-uniform assembly. The alternative global M1 theorem replaces the two direct M1 parents but none of the three M2 parents.
3. At hard TOP, the residual coefficients occupy (M_L\asymp L^2) sites and have energy
   \[
   D_L\ll_\varepsilon L^2X^\varepsilon.
   \]
4. The minimum diagonal-safe window is (R_0=\lceil L\rceil), and the already-stated parity/strict-sector reduction makes (R167.1) sufficient for the residual scalar.
5. At the maximal window (R=M_L), fixed-shift Cauchy handles (r<R_0), and (B166.2) is an alternative sufficient inequality for the same scalar.
6. The desired estimate must be uniform in every parameter and endpoint range inherited by the residual reduction. In particular, (J) is not to be frozen unless the inherited statement permits that. The coefficients must be the actual (c_N^{\rm rem}), and the real-part, parity, opposite-sector, and (g<\gamma L) restrictions must retain their exact meanings and normalizations.

The Round-167 promotion gate for (R167.1) is conjunctive:

1. prove (R167.1) at the exact normalization used by the residual reduction, uniformly over the full inherited ranges;
2. identify the actual-coefficient or phase/arithmetic identity that yields the complete factor (L) missing from energy-only summation, and show why the same proof does not prove the false arbitrary-sign or unsigned analogue;
3. recompute the minimal-window connector and verify that diagonals, sector boundaries, near collars, dyadic summation, and endpoint passage introduce no positive power of (L) or (X) beyond the allowed (X^\varepsilon);
4. pass an independent normalization/sign seam review and the adversarial controls in Section 5; and
5. promote, if all of the above pass, only the residual scalar. Do not promote the remaining hard-TOP channels, the hard-TOP parent, any other M2 parent, either M1 route, M9, or the target theorem.

**Stop rule.** Stop Round 167 with a rigorous no-go/retain outcome as soon as the proposed proof is seen to use only energy, support cardinality, parity/sector counting, triangle inequality, or fixed-shift Cauchy at its decisive step, or if its final connector loses any fixed positive power (L^\delta). Do not pivot inside that round to (B166.2), a different hard-TOP channel, or a parent-level theorem. A new round may be designed only after closing this one.

## 3. Proof or derivation

Write the explicit fixed-shift correlation appearing in (B166.2) as

\[
 S_r=\sum_N c_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
 e\!\left(J(\sqrt{N+r}-\sqrt N)\right).
\]

The phase has modulus one. Fixed-shift Cauchy therefore gives

\[
 |S_r|
 \le
 \left(\sum_N|c_{N+r}^{\rm rem}|^2\right)^{1/2}
 \left(\sum_N|c_N^{\rm rem}|^2\right)^{1/2}
 \le D_L.
\tag{3.1}
\]

At the minimal window there are (O(R_0)=O(L)) candidate shifts. Thus termwise Cauchy followed by a triangle inequality has scale

\[
 R_0D_L\ll_\varepsilon L^3X^\varepsilon.
\tag{3.2}
\]

The desired scale in (R167.1) is (L^2X^\varepsilon). Hence the short aggregate requires a full factor (L) beyond (3.2). Parity removes only a constant proportion of shifts. The blind statement supplies no power-saving cardinality estimate for the opposite-sector or (g<\gamma L) filters, so no (L)-saving may be credited to them without a new lemma.

For (B166.2), there are (O(M_L)=O(L^2)) candidate shifts and (0\le 1-r/M_L\le1). Equations (3.1) and (M_L\asymp L^2) give only

\[
 \left|\sum_{\substack{R_0\le r<M_L\\2\mid r}}
 \left(1-\frac r{M_L}\right)S_r\right|
 \ll M_LD_L
 \ll_\varepsilon L^4X^\varepsilon.
\tag{3.3}
\]

Its requested (L^3X^\varepsilon) bound therefore also needs a factor (L). Meanwhile the omitted range (r<R_0), paid by fixed-shift Cauchy in the maximal-window connector, already has the (R_0D_L\asymp L^3X^\varepsilon) scale. This leaves no positive-power slack in that connector. The two explicit options consequently have equal power-saving demand, but (R167.1) has fewer shifts and no maximal-window short/medium-long splice. That proves the rank-1 versus rank-2 decision.

The rank-3 direct attack has the same formal owner leverage and might exploit cancellation discarded by either sufficient aggregate. But the blind statement supplies no exact scalar expression, so its required saving, normalization, and cancellation locus cannot be frozen. It is not an analytic task yet. The remaining hard-TOP channels are ranked next because they at least stay near the current parent, but the residual and near collars would still block that parent. Balanced and unbalanced M2 each have greater nominal parent leverage, while each lacks a stated inequality or mechanism and leaves the other two M2 parents plus an M1 route and endpoints. The two direct M1 tasks each remove only one of two independent parents and leave all M2 work. The global M1 alternative removes both direct M1 requirements if completely proved, but its theorem is the broadest, contains an angular-radial assembly seam, leaves all M2 parents, and supplies no blockwise M1 result. With no visible new cancellation principle, breadth is a liability rather than evidence of feasibility. This establishes the remaining priority order.

Finally, neither the internally proved exponent (1/3) nor the audited external exponent (0.3144831759740614\ldots) reaches (1/4). Their gaps from (1/4) are respectively (1/12) and (0.0644831759740614\ldots). Thus the statement supplies no basis for treating interpolation, epsilon bookkeeping, or an already-audited theorem as the missing factor-(L) mechanism.

## 4. First doubtful or unproved step

The first unproved step is exactly the passage from the energy-scale short-shift bound (3.2) to (R167.1). Nothing supplied in the blind statement correlates the signs/phases of the actual coefficients across (r), and neither parity nor the stated sector restrictions is asserted to save a power of (L). Consequently there is presently no proof of the required (L)-fold cancellation.

This is also the first place a proposed proof should be stopped and audited. If its decisive estimate remains valid for arbitrary coefficients having the same energy, then it has almost certainly erased the only structure capable of producing the saving.

## 5. Required controls and outcomes

1. **Fixed-shift Cauchy control — completed analytically; fails by one power.** Equations (3.2) and (3.3) give (L^3X^\varepsilon) for the short range and (L^4X^\varepsilon) for the medium/long range. Both are one factor (L) above their respective targets.

2. **Adversarial dephasing control — completed analytically; the arbitrary-coefficient analogue fails.** On a consecutive support (1\le N\le M), take
   \[
   c_N=e(-J\sqrt N).
   \]
   Then every summand in (S_r) equals (1). For even (r) in a fixed positive-proportion subrange of (R_0\le r<M),
   \[
   \left(1-\frac rM\right)\sum_{N\le M-r}1\asymp M,
   \]
   and summing over (\asymp M) such shifts gives (\asymp M^2\asymp L^4), although the energy is (D=M\asymp L^2). Thus (B166.2) is false for arbitrary energy-bounded coefficients by precisely the missing factor (L). For a short-shift aggregate with (\asymp R_0) surviving shifts and (\asymp M) overlaps, the same model has scale (R_0M\asymp L^3), not (L^2). The latter conditional statement is a control on energy-only reasoning, not a counterexample to the actual restricted aggregate, because the blind statement does not specify the cardinality created by the (g) and sector filters.

3. **Parity/counting control — completed logically; no power saving is available from the supplied facts.** Restriction to even (r) changes the number of shifts only by a constant factor. No quantitative sparse-count lemma for the other filters is in the permitted context. Treating those filters as an (L)-saving would therefore be an unproved connector.

4. **Actual-coefficient sign control — required and pending.** A candidate proof must isolate a property of the actual coefficients (for example, if applicable under their exact definitions, a Vaaler- or (\chi_4)-driven identity) that breaks the adversarial model. The control passes only if the proof explicitly fails when coefficients are replaced by arbitrary phases or absolute values. No such mechanism is visible in the blind statement, so the current outcome is **not passed**.

5. **Endpoint/normalization control — required and pending.** Test the smallest admissible (L), (R_0=\lceil L\rceil), the transition (r=R_0), sector boundaries, and every inherited endpoint value of (J). Re-expand the exact normalization of (\mathfrak C) and check that all dyadic or collar sums cost only (X^\varepsilon), never (L^\delta). These checks cannot be performed from the statement-only packet; hence promotion remains closed.

No numerical experiment was used. The decisive controls are algebraic and expose the exact power deficit.

## 6. Dependencies and exact artifacts used

Only the following two artifacts were read:

1. `protocol.md`;
2. `rounds/codex-managed/full-proof-round164-166-strategy-literature-review/blind_statement.md`.

No proof-state file, strategy, nonblind artifact, sibling report, source card, web result, candidate, synthesis, conductor work, or legacy round was consulted. The derivation uses no external theorem.

## 7. Recommended state effect

**RETAIN, with no proof-status change.** Retain (B166.1) as the sole Round-167 analytic frontier and freeze it as (R167.1) with the promotion gate and stop rule above. Do not promote (B166.1), the residual scalar, hard TOP, any M1/M2 parent, M9, or the target theorem on the basis of this report. Deprioritize, but do not reject, (B166.2), a direct residual attack, the remaining hard-TOP channels, balanced/unbalanced M2, both direct M1 parents, and the global M1 alternative.
