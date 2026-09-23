# Round 166 blind post-unmask frontier-selection review

Role: post-unmask seam reviewer
Object reviewed: `reports/full_graph_frontier_strategy_audit.md`
Blind comparator: `reports/blind_frontier_priority_rederivation.md`
Kernel comparator: `proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md`

## 1. Result

**Verdict: REVISE locally, while retaining the frontier and making no graph change.**

The full-graph audit's principal decision is independently confirmed: the unique next analytic inequality should be the exact minimal-window signed aggregate

\[
 \Re\mathfrak C_{R_0,2,{\rm opp},\,g<\gamma L}^{\rm rem}
 \ll_{\gamma,\varepsilon}L^2X^\varepsilon,
 \qquad R_0=\lceil L\rceil .
 \tag{167.F}
\]

This agrees with the blind selection, and its normalization, factor-(L) deficit, and residual-only implication agree with the Round-165 kernel. The determinant-orbit proposal is genuinely route-novel relative to the rowwise and positive methods excluded by that kernel. The report also correctly leaves source applicability, the analytic inequality, every parent, and every exponent open.

Four local exactness defects should be repaired before the report is used to freeze Round 167:

1. the displayed coefficient condition contains a literal carriage-return corruption, `d\ {<CR>m odd}`, and must read (d\ \mathrm{odd});
2. the determinant dictionary must preserve exact multiplicity and weights, not merely have bounded multiplicity;
3. the phase-aligned arbitrary-(c_N) control is not literally defined on the post-opening ({\rm opp},g<\gamma L) subaggregate and must be scoped as a coefficient-blind/pre-filter diagnostic, or replaced by an explicitly lifted incidence-level adversarial control; and
4. the rank-4 object is enlarged from “remaining hard-TOP channels” to a complete all-channel hard-TOP parent theorem. That is a different frontier and must be labelled as such or split from the remaining-channel frontier.

There is no contradiction that overturns (167.F), its residual-only scope, or the no-promotion decision.

## 2. Exact statement and hypotheses

The comparison uses the following exact Round-165 identities:

\[
 \mathfrak E_R=D_L+2\Re\mathfrak C_R,
 \qquad
 \mathfrak E_R\le2\mathfrak E_R^{(2)},
 \tag{165.K4, 165.K8}
\]

\[
 |\mathcal S_{L,1}^{\rm rem}|^2
 \le {M_L+R-1\over R}\mathfrak E_R,
 \qquad M_L\asymp L^2,
 \tag{165.K6}
\]

with

\[
 \mathfrak C_R=
 \sum_{1\le r<R}\left(1-{r\over R}\right)
 \sum_N c_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
 e\!\left(J(\sqrt{N+r}-\sqrt N)\right),
 \tag{165.K5}
\]

and (D_L\ll_\varepsilon L^2X^\varepsilon). At (R_0=\lceil L\rceil), the kernel proves that odd gaps can be removed through the parity-energy connector, that the monotone displacement sector is (O(L^2)), and that the opened divisor-incidence sector (g=(d,d')\ge\gamma L) is (O_{\gamma,\varepsilon}(L^2X^\varepsilon)). Its sole remaining minimal-scale inequality is precisely (165.K17a), identical to (167.F).

The exact literal coefficient in the kernel is

\[
 c_N^{\rm rem}
 =\sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)\lambda_N(d).
 \tag{2.1}
\]

The audit intends (2.1), but its displayed formula has a carriage-return character in place of `\r` in `\rm`. This is a transcription defect in the frozen statement, not a mathematical disagreement elsewhere in the report. It is nevertheless promotion-blocking until corrected because the campaign requires an exact literal coefficient.

The low-gcd and opposing-displacement conditions are incidence-level conditions introduced only after the exact signed divisor opening:

\[
 N=dm,\quad N+r=d'm',\quad
 (d'-d)(m'-m)<0,\quad (d,d')<\gamma L.
 \tag{2.2}
\]

Accordingly, a source dictionary must give an exact equality to the weighted sum in (167.F). “Bounded multiplicity” is insufficient unless every multiplicity is explicitly retained and the equality, including signs, Fejer weights, selectors, endpoints, and the one outer real part, is proved. The natural gate is: exact multiplicity one as in the kernel's divisor opening, or an explicit multiplicity weight that restores exact equality.

## 3. Proof or derivation

### 3.1 K17a normalization and implication

The full audit defines the Fejer weight (1-r/R_0), restricts to even (r), makes the ({\rm opp}) and (g<\gamma L) cuts after divisor opening, keeps the actual (c_N^{\rm rem}), and retains one outer real part. Except for the malformed `odd` condition, this matches (165.K5), (165.K13), and (165.K17a) exactly.

Assuming (167.F), add the kernel's accepted diagonal, monotone sector, and high-gcd sector. Then

\[
 \mathfrak E_{R_0}^{(2)}\ll_{\gamma,\varepsilon}L^2X^\varepsilon,
 \qquad
 \mathfrak E_{R_0}\ll_{\gamma,\varepsilon}L^2X^\varepsilon.
\]

Since

\[
 {M_L+R_0-1\over R_0}\asymp L,
\]

(165.K6) gives

\[
 |\mathcal S_{L,1}^{\rm rem}|^2
 \ll_{\gamma,\varepsilon}L^3X^\varepsilon,
 \qquad
 |\mathcal S_{L,1}^{\rm rem}|
 \ll_{\gamma,\varepsilon}L^{3/2}X^\varepsilon,
\]

after the standard renaming of epsilon on taking a square root. The audit's implication is therefore correct. It is also correctly limited to the residual scalar: the Round-165 kernel explicitly excludes the full (t=1) face, other few-point channels, near collars, hard TOP, BAL, UNBAL, both M1 routes, endpoint uniformity, M9, and any improved global exponent.

### 3.2 Factor-(L) deficit

For each shift,

\[
 \left|\sum_N c_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
 e\!\left(J(\sqrt{N+r}-\sqrt N)\right)\right|
 \le D_L.
\]

There are (O(R_0)=O(L)) short shifts, so coefficient-blind fixed-shift Cauchy and triangle inequality give (R_0D_L\ll L^3X^\varepsilon), whereas (167.F) asks for (L^2X^\varepsilon). At maximal scale there are (O(M_L)=O(L^2)) shifts, giving (M_LD_L\ll L^4X^\varepsilon), whereas (165.K26) asks for (L^3X^\varepsilon). Both alternatives therefore lack exactly one factor (L), and the maximal-scale connector spends its entire (L^3) allowance on (r<R_0). The audit and blind derivation agree exactly on this ledger.

The phrase “capacity (L^3)” must remain an upper-capacity or hostile-model scale, not a lower bound for the literal filtered scalar. The audit states this convention in its matrix, which is correct.

### 3.3 Determinant-mechanism novelty

The Round-165 kernel already proves

\[
 r=d'm'-dm
\]

and records that even cofactor rows have frozen character, no modulo-one first-difference separation is known, the positive real second-derivative bound is adverse, and absolute completion of stationary dual modes is adverse. Crucially, it expressly leaves joint ((r,N)) transforms and signed spectral formulas open. A joint determinant-orbit spectral treatment that preserves the aggregate real part is therefore genuinely new relative to the excluded routes; it is not a relabelling of rowwise completion.

Two wording corrections are needed. First, the exact signed divisor opening must occur before the determinant matrix and the filters (2.2) exist. The proposed method should act **after the exact signed opening but before any positive majorization, shiftwise modulus, rowwise completion, or separated spectral norm**. Second, the cited source presently matches only the determinant skeleton. The audit itself lists the unresolved selector, coefficient-class, two-adic, smoothness, orbit-correlation, main-term, and restored-power seams, so the phrase that the source geometry “lands literally” on (165.K17a) is too strong. “Matches the determinant skeleton of (165.K17a)” is exact.

### 3.4 Ranking comparison and contradictions

The blind and unmasked rankings agree on the decisive prefix:

1. (165.K17a)/(167.F);
2. (165.K26);
3. direct residual scalar;
4. work at hard TOP rather than a remote M1/M2 theorem.

They also agree that (167.F) has only residual ownership, that (165.K26) has the same owner with a broader connector, and that no theorem or exponent is promoted. The unmasked audit's ordering of GAR, the two direct M1 parents, BAL, and UNBAL differs from the blind ordering, but this is not a contradiction: the unmasked report supplies graph-specific deficits, historical obstructions, and owner reductions that the statement-only packet deliberately withheld.

There is one scope mismatch in the fourth row. The blind candidate is “the remaining hard-TOP channels,” which leaves the residual open. The audit's row 4 instead proposes a complete all-channel hard-TOP theorem owning the residual and every remaining few-point channel. Those statements have different size and leverage. The audit should either relabel row 4 as a **direct complete hard-TOP parent shortcut** and separately rank the remaining-channel frontier, or replace it by the actual remaining-channel statement. This mismatch does not affect the selected rank 1, but it prevents the lower ranking from being an exact comparison as written.

The description of (167.F) as the “smallest exact surviving theorem” should also be read as “smallest exact, mechanistically specified aggregate frontier.” The direct scalar theorem is an exact owner-level target and has a smaller raw power deficit; the audit's real reason for preferring (167.F) is the accepted determinant interface and a concrete hypothesis gate, not theorem-strength minimality.

## 4. First doubtful or unproved step

The first mathematical gap remains the audit's proposed source/interface lemma: after exact signed divisor opening, represent every literal weighted determinant incidence in an admissible joint spectral framework, preserve the single aggregate real part, and prove that all main, orbit-correlation, smoothness, two-adic, boundary, completion, and recombination terms total (O_{\gamma,\varepsilon}(L^2X^\varepsilon)).

The first review-level defect occurs even earlier: the full audit has not yet written an exact multiplicity-preserving source dictionary. A coincidence of determinant equations does not supply one. The neither/both residual selector and the square-root phase are correctly identified as likely first failure points. Until that dictionary and its restored-power ledger exist, determinant-spectral novelty is strategy evidence only.

## 5. Required controls and outcomes

| Check requested | Outcome | Required action |
|---|---|---|
| K17a normalization | **AMBER.** Fejer weight, parity, opposing sector, low divisor-gcd cut, real-part placement, and scale are correct; the displayed odd-divisor condition is corrupted | Replace the corrupted condition by (d\ \mathrm{odd}), and demand exact multiplicity equality in the determinant dictionary |
| Factor-(L) deficit | **GREEN.** (L^3\to L^2) at minimal scale and (L^4\to L^3) at maximal scale are correct | Preserve the no-positive-power-loss gate |
| Residual-only implication | **GREEN.** The derivation to (L^{3/2}) and every downstream non-implication agree with the kernel | Promote at most the residual child after all seams pass |
| Determinant novelty | **GREEN/OPEN.** Joint signed determinant-orbit treatment is outside the kernel's rejected rowwise routes, but no literal source match is proved | Say “determinant skeleton,” preserve the signed opening, and complete the source/interface lemma |
| Promotion gate | **AMBER but structurally sound.** It covers dictionary, signs, source hypotheses, restored powers, false controls, uniformity, and independent validation | Tighten multiplicity and adversarial-control wording as stated above |
| Stop rule | **GREEN.** It stops on the first exact hypothesis/power failure, forbids an automatic pivot, and does not overgeneralize the no-go | Retain unchanged after the wording repairs |
| Contradictions | **NO FATAL CONTRADICTION.** Only the rank-4 scope mismatch and terminology issues remain | Relabel or split the hard-TOP row; do not alter rank 1 |

The aligned-array control needs precise scoping. An arbitrary product-site array (c_N) has no canonical divisor variables (d,d',m,m'), hence no literal ({\rm opp}) or (g<\gamma L) restriction. The phase-aligned construction validly falsifies an energy-only estimate for the unfiltered short Fejer form and any proof step that has already erased the incidence filters. It is not, without an additional lifted construction, a direct counterexample to (165.K17a). The promotion gate should say exactly this. A stronger incidence-level adversarial control is welcome only if its literal atoms, energy, selectors, and filters are all explicitly defined.

No numerical test is needed; every control here is algebraic or logical.

## 6. Dependencies and exact artifacts used

This post-unmask review used exactly:

1. `protocol.md` (already read for the blind assignment);
2. `rounds/codex-managed/full-proof-round164-166-strategy-literature-review/reports/blind_frontier_priority_rederivation.md`;
3. `rounds/codex-managed/full-proof-round164-166-strategy-literature-review/reports/full_graph_frontier_strategy_audit.md`;
4. `proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md`.

No shared proof-state file was edited, no sibling report was used, and no external source claim was independently audited in this review.

## 7. Recommended state effect

**REVISE the strategy report; RETAIN the selected frontier; NO GRAPH CHANGE.**

Before freezing the Round-167 brief, correct the odd-divisor typography, require an exact multiplicity-preserving determinant dictionary, scope the aligned-array control to the level where it is defined, replace “lands literally” by “matches the determinant skeleton,” and relabel or split the rank-4 hard-TOP frontier. After those local repairs, retain (167.F) as the sole Round-167 inequality with the existing source-specific promotion gate and stop rule. This review licenses no source dependency, lemma promotion, parent closure, exponent improvement, or shared-state edit.
