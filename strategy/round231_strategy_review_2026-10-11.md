# Gauss circle project: review through the Round-231 preparatory packets

Date: 11 October 2026
Repository: yutianlee/gauss-circle-ai-collab
Fixed snapshot: 6447f8fe12a5c2cd6f3bf6bf1a5feb2755177ae0
Commit timestamp: 2026-10-11 14:12:30 UTC
Review only: no repository files, accepted claims, or campaign statuses were changed.

## 1. Assessment

The project has made substantial progress in identifying the actual arithmetic quantity that must be estimated. It has not proved a new complete moment bound since Round 204 or improved its qualified external pointwise benchmark. The October 11 snapshot contains completed preparatory packets labelled Round231; the numbered analytic campaign itself remains pending_design.

Retain the new adaptive divisor decomposition, the exact central norm-and-factor owner, and the corrected real-phase reciprocal analysis. Do not count the independently reconstructed high-norm tail as a new gain: its antecedents are explicitly identified in Rounds203/205/208. Do not promote the reviewed full continuous spectral component into a complete spectral theorem or a bound for its unestimated cuspidal partner.

The strategic adjustment is to target actual-coefficient large values in a specified amplitude range. A small complete moment improvement is a useful first milestone, but it must be distinguished from an improvement of the Gauss pointwise exponent. Do not restart another generic source-transfer or normalization campaign without a new quantitative mechanism.

## 2. Normalization and thresholds

Use the actual fixed mollifier and radial window in the repository. In particular,

\[
B_T(R)=\sum_{n\ge1}r_2(n)n^{-3/4}\Psi(\sqrt{n/T})
\cos(2\pi R\sqrt n-3\pi/4),\qquad R\asymp T,
\]

and

\[
M_{12}(F)=\int w(R/T)|F(R)|^{12}\,dR.
\]

The window is fixed, nonnegative, and large enough for the sharp-discrepancy restoration; in the restoration argument it majorizes the needed interior radial interval. The moment is UNNORMALIZED. Constants may depend on fixed smooth functions and on epsilon.

Set

\[
\theta=\frac{3292+25\sqrt{1717}}{13762}=0.314483175974061407\ldots,
\qquad \beta=2\theta-\frac12=0.128966351948122813\ldots.
\]

The repository's qualified external benchmark is theta. The internally derived fallback remains 1/3. Its accepted complete twelfth-moment bound is

\[
M_{12}(B_T)\ll_\varepsilon T^{10\beta+\varepsilon},
\qquad 10\beta=1.289663519481228135\ldots.
\]

For a COMPLETE bound with exponent b >= 1, the sharp pointwise consequence is

\[
\theta_{12}(b)=\frac14+\frac{b+1/2}{26}=\frac{7+b}{26}.
\]

Indeed, x=R^2 and the leading sqrt(R) amplitude give a sharp x-variable moment of exponent (7+b)/2. Monotonicity of the counting function implies that a discrepancy of magnitude V persists on a one-sided interval of length comparable to V. The pointwise exponent is therefore the sharp moment exponent divided by 13. Smoothing and interval endpoints must remain as in the accepted restoration.

| Complete b | Pointwise consequence of this moment alone | Interpretation |
|---|---|---|
| 10 beta | 0.318833212287739544... | Existing moment bound; weaker than the external pointwise benchmark |
| 32/25 = 1.28 | 207/650 = 0.318461538461538462... | Strict complete moment improvement only |
| 23/18 | 149/468 = 0.318376068376068376... | Conditional inverse-theorem milestone; still no pointwise record |
| 5/4 | 33/104 = 0.317307692307692308... | Stronger moment milestone, still no pointwise record |
| 29/25 | 102/325 = 0.313846153846153846... | Beats the reviewed external benchmark |
| 1 | 4/13 = 0.307692307692307692... | Optimal twelfth moment; still not the quarter theorem |

To improve the benchmark through the twelfth moment, one needs

\[
b<26\theta-7=13\beta-\frac12=1.176562575325596582\ldots.
\]

These implications were independently rederived and their numerical values checked with exact symbolic arithmetic. None proves a new moment estimate.

## 3. What the Round-231 narrowing buys

For 13/125 <= gamma < beta, the reviewed combined-owner packet defines

\[
X_\gamma=T^{4\gamma},\quad Y_\gamma=T^{1-2\gamma},\quad
\phi_\gamma(n)=\eta(n/X_\gamma)-\eta(n/Y_\gamma),
\]

with eta the fixed smooth cutoff used there, and

\[
D_\gamma(x)=T^{2\gamma-13/42}x^{29/84}.
\]

Its central owner C_gamma has coefficients

\[
4\phi_\gamma(n)\sum_{dm=n,\ d,m\ge D_\gamma(x(n))}\chi_4(d),
\]

with all original radius-independent patch starts and cutoff equality conventions retained. Its support lies in

\[
T^{4\gamma}<n<2T^{1-2\gamma}.
\]

The exact decomposition B=L+H+U+C has three paid complementary pieces, each with an independently established ceiling T^(gamma+epsilon). The accepted coefficient-uniform distribution then yields the budget

\[
m(\gamma)=\max\{1,10\gamma,1+20\gamma/13\}.
\]

Consequently, at this budget, the complete B bound and the C bound are equivalent as upper bounds, not equal as moments.

### Representation choice

For reciprocal analysis, use the SMOOTH FULL NORM BAND

\[
F_\gamma(R)=\sum_n\phi_\gamma(n)r_2(n)n^{-3/4}\Psi(\sqrt{n/T})
\cos(2\pi R\sqrt n-3\pi/4).
\]

It satisfies exactly F_gamma=C_gamma+U_gamma and B=L_gamma+F_gamma+H_gamma. Since U,L,H are already paid at m(gamma), estimating F_gamma or C_gamma at that budget is equivalent. This is not a new localization theorem. It is a choice of the already available representation that avoids an unnecessary sharp divisor mask during a smooth Poisson calculation.

Use C_gamma where the factor restrictions materially help the arithmetic. Use F_gamma where the exact r2 identity, smoothness, and real phase matter more. Never change representations without restoring the paid correction in the norm.

## 4. A precise first complete-gain target

For F equal to either of these actual coefficient families, define

\[
D_F(V)=\int w(R/T)\mathbf1_{|F(R)|>V}\,dR.
\]

The accepted generic estimate is

\[
D_F(V)\ll_\varepsilon T^\varepsilon
\bigl(V^{-2}+TV^{-136/13}\bigr),\qquad V\ge1.
\]

The actual ceiling follows from the exact decomposition and paid complements:

\[
\|F\|_\infty\ll_\varepsilon T^{\beta+\varepsilon}.
\]

This ceiling is NOT granted for arbitrary coefficient masks.

### Proposed sufficient lemma A: upper-tail improvement

Take gamma=16/125 and the literal F_gamma or C_gamma. Prove, for V >= T^(16/125),

\[
D_F(V)\ll_\varepsilon T^\varepsilon
\left(T^{-1/100}V^{-2}+TV^{-136/13}\right).
\tag{A}
\]

This is an OPEN, sufficient research target, not a result of this review. It is stronger than necessary near the bottom of its amplitude range; a level-dependent or integrated saving reaching the same budget would also suffice.

**Conditional consequence, proved here.** Use the old distribution below V0=T^gamma and (A) above it. Layer cake gives

\[
M_{12}(F)\ll T^\varepsilon\left[
T+T^{10\gamma}+T^{1+20\gamma/13}
+T^{10\beta-1/100}+T^{1+20\beta/13}\right].
\]

At gamma=16/125 these five exponents are

\[
1,\quad1.28,\quad1.196923076923\ldots,
\quad1.279663519481\ldots,\quad1.198409772228\ldots.
\]

Therefore (A) implies the COMPLETE bound M12(B_T) << T^(32/25+epsilon), after restoring the complementary pieces. The required additional saving is concentrated in the amplitude range between T^0.128 and the available ceiling T^0.128966351948... . This is an exponent range, not a claim that a fixed small number of samples controls it.

The minimal constant saving in the first term for this calculation is 10 beta - 32/25 = 0.009663519481... . Choosing 1/100 gives a small positive margin.

### Proposed sufficient lemma B: pointwise-record milestone

Take gamma=13/125. A simple sufficient actual-coefficient upper-tail estimate is

\[
D_F(V)\ll_\varepsilon T^\varepsilon
\left(T^{-13/100}V^{-2}+T^{24/25}V^{-136/13}\right),
\qquad V\ge T^{13/125}.
\tag{B}
\]

This is also OPEN and sufficient, not necessary. The same calculation gives the complete exponent

\[
\max\{29/25,10\beta-13/100,24/25+20\beta/13\}=29/25.
\]

The two last exponents are 1.159663519481... and 1.158409772228... . Hence (B) would imply theta=102/325 for the sharp discrepancy.

IMPORTANT: improving only the V^-2 term is not enough for this second milestone. The unchanged second term contributes exponent 1+20 beta/13=1.198409772228... >29/25. A claim that suppresses one contribution must still price the other.

## 5. Mechanism to test first: signed reciprocal resonances

The corrected reciprocal calculation is a useful starting representation, but its current bound is insufficient. For a smooth rectangle DM comparable to N, Poisson in m gives stationary terms

\[
I_h(d)=b_h(d)e(R^2d/(4h)-1/8)+\text{controlled error},
\quad h\asymp RD/\sqrt N.
\]

The circle phase contributes e(-3/8), so the real leading term is

\[
-\operatorname{Re}\sum_d\chi_4(d)b_h(d)e(R^2d/(4h)).
\]

For real b_h, choose an odd q and write Delta=R^2-hq. The elementary exact identity

\[
\chi_4(d)e(qd/4)=i\chi_4(q)\mathbf1_{d\ \mathrm{odd}}
\]

gives

\[
-\operatorname{Re}\sum_d\chi_4(d)b_h(d)e(R^2d/(4h))
=\chi_4(q)\sum_{d\ \mathrm{odd}}b_h(d)
\sin\!\left(\frac{\pi\Delta d}{2h}\right).
\tag{C}
\]

This identity concerns the stationary leading term; it does not erase higher Bessel terms or stationary errors. At Delta=0 the term vanishes. At detuning of order h/D it need not be small. The verified individual-fibre counterexample remains valid, but it has size only of order T^(-1/2), not a lower bound for the complete high-amplitude event.

The next calculation should keep the odd kernel, the actual character signs, and the radius average. The natural product window is |R^2-hq| of order h/D, comparable to T/sqrt(N). Its integer products are arithmetically correlated; no independence or reflection symmetry may be assumed.

The proof task is to estimate the aggregate or its large-value set, with (A) as the first complete test. Merely obtaining (C), counting products after absolute values, or applying Poisson back to the original wave does not meet the objective. All smooth rectangles, errors, norm scales, and paid corrections must be restored. A truncated Taylor bound for the sine must not be used outside its small-detuning range.

## 6. Revised roles of other methods

### Decoupling

Retain it as a possible large-value and concentration tool, not an automatic norm upgrade. The target measure is the actual exceptional-radius set, not an arbitrary point mass. Its tube or cap concentration must be proved, not assumed. A lift to an auxiliary frequency variable must price restriction back to the physical radial trace. Use arithmetic structure to deal with configurations that saturate the geometric estimate.

### Additive combinatorics and probability

Investigate an inverse description of the actual large-value set: many simultaneously aligned near-products should impose quantitative arithmetic structure. The project already rules out the relevant unchanged all-polynomial residual saving beyond 1/20, even after scalar centering. That is not a prohibition on phase-specific analysis or direct moments. Do not assume an unspecified inverse-theorem constant gives the necessary power.

A probabilistic comparison must randomize the radius of the fixed lattice and preserve squarefree-class dependence. A theorem for random lattices, independent signs, or merely convergence in distribution does not control these finite-scale tails. Any cumulant or correlation argument needs quantitative errors at V growing as a power of T.

The separate-exponent physical inverse interface A=3, B=4 remains a legitimate alternative sufficient target, with conditional complete exponent 23/18. Those powers have not been proved; extracting them is a distinct problem. It is not yet a pointwise-improvement route.

### Kloosterman and spectral approaches

Downgrade the previous blanket Kloosterman-first recommendation. The all-modulus bilinear theorem is real, but a useful application requires a complete matched kernel, weights, moduli, and restored saving. A coefficient-norm saving alone is excluded by the actual balanced semiprime energy control. The KRW proposition is applicable but quantitatively insufficient: its normalized first term is T^(1/8)N^(1/16); with the head and known tail, the tested envelope still meets at exponent 1/6.

The complete continuous spectral component is useful reviewed evidence. It does not estimate the cusp term. Retain the spectral route as a reserve requiring a new matched signed input, not another normalization-only campaign.

## 7. Full-proof route and research discipline

A twelfth moment, even optimal, does not prove the quarter conjecture. For direct COMPLETE-wave moments M_p(B_T) << T^(b_p+epsilon), an unbounded sequence of fixed even orders with b_p=o(p) suffices. Select p for the desired epsilon and then keep p fixed as T tends to infinity. The accepted Round216 distinct-radical reduction is only twelfth-order; its extension to all orders must be proved separately.

Measure progress by a new complete estimate, a reusable arithmetic theorem with an explicit application, or a sharply scoped obstruction. Do not relabel another equivalent unestimated transform as a complete improvement. Conversely, do not require a new theorem already to be known before permitting exploratory mathematics: admit a precise conjectured lemma with a mechanism, a complete implication, and genuine falsification tests. After two attempts with unchanged assumptions, review the premise rather than automatically refine the same interface.

First proposed exercise: actual-coefficient upper-tail estimate (A), working with the smooth full band when it removes unnecessary masks, and retaining the real signed reciprocal kernel during the radius analysis. Keep the preferred (B) milestone as a distinct stronger target.

## 8. Evidence inspected and limits

Repository files inspected, wholly or in the mathematical ranges stated in the review:

- state/current_round.md
- manifests/reading_packet.md, current status and opening historical packet
- strategy/gauss_circle_strategy_checkpoint_round230_2026-10-11.md
- proofs/kernels/gc_complete_square_root_large_values_moment_bound.md, including finite duality, reconstruction, and coherent-vector control
- strategy/round231_residual_saving/conductor_decision.md
- strategy/round231_residual_saving/conductor_adaptive_factor_cutoff.md
- strategy/round231_balanced_cancellation/briefs/balanced_interface.md
- strategy/round231_balanced_cancellation/conductor_decision.md
- strategy/round231_balanced_cancellation/conductor_combined_owner.md
- strategy/round231_balanced_cancellation/conductor_seam_repairs.md
- strategy/round231_balanced_cancellation/reports/balanced_reciprocal_attack.md, mathematical derivation through the reciprocal estimate and restoration

The entire 401-node graph and all historical proofs were not independently audited. The large proof_obligations.yml could not be retrieved in full through the available file endpoint. Round201/216/227/228 statuses above are therefore attributed to the current checkpoint, not claimed as newly reverified proofs.

Primary external records inspected: Li–Yang arXiv2308.14859; Blomer–Pascadi arXiv2607.24311v1, Theorem1.1; KRW Proposition5 in the parsed primary journal/preprint texts; MSTT arXiv2204.03754 version record. PDF screenshot requests failed, so no visual PDF verification is claimed. The claimed Kim–Ko October2 v3 could not be independently fetched; the served arXiv abstract record showed v2 while a secondary index indicated a later update. Do not treat that version discrepancy as proof that the repository is wrong, or as a verified new input. It does not affect the conditional exponent calculations in this report.

This review proves only the elementary transfer calculations and identities explicitly derived above. The proposed tail bounds, their arithmetic mechanism, the complete pointwise improvement, and the quarter theorem remain unproved.
