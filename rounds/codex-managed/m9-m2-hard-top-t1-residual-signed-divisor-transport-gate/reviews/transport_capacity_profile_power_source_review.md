## Result

**Revise before promotion.** The selector-complete residual algebra, the odd and even four-prime controls, the fixed-box count

\[
 \gg \frac{L^2}{(\log L)^4},
\]

the actual-profile bound \(V_N\ll1\), the Fejer identity and all of its \(L,H,J,X\) powers, and the numerical power ledger for the accepted rank-one collar are correct. They prove a route-scoped obstruction to coefficient-uniform positive BV/transport control and an exact reduction to a signed short additive-shift energy. They prove neither a lower bound for the literal profile coefficient nor a lower bound for the oscillatory residual scalar.

Four repairs are required.

1. Candidate (164.C19) is not a necessary literal-profile condition. Applying (164.C14) and the triangle inequality to the actual profile requires the **weighted** estimate
   \[
    \sum_{N\asymp L^2}\operatorname{osc}C_N\,V_N
       \ll_\varepsilon L^{3/2}X^\varepsilon.                 \tag{164.R1}
   \]
   The unweighted sum of \(\operatorname{osc}C_N\) is the sharp envelope only for a theorem uniform over all bounded-variation coefficients with \(V_N\ll1\). The four-prime family refutes that uniform envelope; it does not show that the fixed literal \(V_N\)'s saturate it.
2. Taking absolute values in (164.C27) does not literally recreate the multiplicative character-Poisson collar \(\lvert s\ell-XQR\rvert\ll QRJ/L\). It destroys the signed real-part cancellation and leaves a positive additive-shift form \(d'm'-dm=r\). The rank-one collar is an independently accepted adverse positive route with the same missing-power warning, not the same geometry.
3. The claim that \(R\asymp L\) is minimal is valid for the inherited fixed-relative \(N\asymp L^2\) shell, whose containing integer interval has cardinality \(M_L\asymp L^2\). If only \(M_L\ll L^2\) is stated, one may claim sufficiency, but not literal minimality. State the lower comparison or qualify “minimal for the worst-case \(L^2\)-shell ledger.”
4. The updated literature conclusion must inherit the accepted Li--Yang source qualifier: the project accepts the final exponent only through the five-repair narrow theorem in Li-Yang-source-audit, not Theorem 1.2 or the general source interfaces as printed. The no-drop-in conclusion is only a dated, listed-source search result.

Subject to these repairs, the proposed hard_top_t1_residual_transport_no_go and the Fejer reduction are sound.

## Exact statement and hypotheses

Let \(J=\sqrt X\), \(y=\lfloor J\rfloor\), \(q_X=X/y^2\),

\[
 H=\lfloor yX^{-1/4}\rfloor=J^{1/2}+O(1),
 \qquad 1\ll L\ll H,
\]

and let \(N=2^{\nu_N}M_N\) be squarefree in the inherited fixed-relative half-open shell \(N\asymp L^2\), with \(M_N\) odd. If no pair is selected, set \(\rho_N(d)=1\). If the Round-163 selector chooses distinct odd primes \(p,q\mid M_N\) with \(\chi_4(pq)=-1\), set

\[
 \rho_N(d)=1-\mathbf 1_{p\mid d}-\mathbf 1_{q\mid d}
             +2\mathbf 1_{pq\mid d}.
\]

Thus \(\rho_N\) retains exactly the \(00\) and \(11\) selected-bit patterns. For the complete zero-extended literal amplitude

\[
 A_N(d)=\eta_L(d)\Phi\!\left(\frac d{H+1}\right)
 W\!\left(\frac{\sqrt{q_X}\,d}{2\sqrt N}\right)
\]

with all cone, shell, floor, star, endpoint and parity conventions retained, put

\[
 b_N^{\rm rem}=\sum_{d\mid M_N}\chi_4(d)\rho_N(d)A_N(d),
 \qquad
 c_N^{\rm rem}=\mathbf 1_{\mathcal I_L^{\rm lit}}(N)\mu^2(N)
 \left(\frac{L^2}{N}\right)^{3/4}b_N^{\rm rem}.
\]

The following audited assertions hold.

* The full residual character mass is
  \[
  \sum_{d\mid M_N}\chi_4(d)\rho_N(d)=
  \begin{cases}
  \displaystyle\prod_{r\mid M_N}(1+\chi_4(r)),&\text{no pair},\\[4pt]
  \displaystyle(1+\chi_4(pq))
  \prod_{\substack{r\mid M_N\\r\ne p,q}}(1+\chi_4(r))=0,
  &\text{selected pair}.
  \end{cases}                                                   \tag{164.R2}
  \]
  Products are over odd prime divisors. Hence the selected residual is exactly balanced. The no-pair mass is nonzero exactly when every odd prime divisor is \(1\pmod4\), in which case every divisor sign is positive and the mass is \(2^{\omega(M_N)}\).
* If the residual divisors are ordered and \(V_N\) is the endpoint-zero-extended sampled variation of \(A_N\), then
  \[
  |b_N^{\rm rem}|\le \frac12\operatorname{osc}C_N\,V_N,
  \qquad V_N\ll1.                                               \tag{164.R3}
  \]
* There are odd and even squarefree four-prime families, independent of whether the selector fires, on which the geometric unit-profile residual is \(-1\). In fixed relative prime boxes they have cardinality
  \[
   \gg P^4(\log P)^{-4}\asymp L^2(\log L)^{-4},
   \qquad P\asymp\sqrt L.                                      \tag{164.R4}
  \]
  This is coefficient-uniform BV/transport capacity only.
* If \(I_L\) is an integer interval of cardinality \(M_L\asymp L^2\) containing the literal shell, \(c_N^{\rm rem}\) is zero outside it, \(z_N=c_N^{\rm rem}e(J\sqrt N)\), and \(R=\lceil L\rceil\), then
  \[
  \mathfrak E_R=\frac1R\sum_s\left|\sum_{j=0}^{R-1}z_{s+j}\right|^2
  \]
  has the exact Fejer expansion in (164.C23), and
  \[
   |\mathcal S_{L,1}^{\rm rem}|^2
    \le \frac{M_L+R-1}{R}\mathfrak E_R.                        \tag{164.R5}
  \]
  Consequently the one-sided actual-direction bound
  \[
  \Re\sum_{1\le r<R}\left(1-\frac rR\right)
       \sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
       e\!\left(\frac{Jr}{\sqrt{N+r}+\sqrt N}\right)
       \le C_\varepsilon L^2X^\varepsilon                     \tag{164.R6}
  \]
  implies the target. No absolute value may be inserted around an individual \(r\), divisor opening, selector branch, or parity branch.

The prime-count input in (164.R4) is Bennett--Martin--O'Bryant--Rechnitzer, Theorem 1.2 of arXiv:1802.00085v3 (also *Illinois J. Math.* **62** (2018), 427--532). Its exact hypotheses are: integer \(q\ge3\), \((a,q)=1\), and \(x\ge x_\theta(q)\), with

\[
 \left|\theta(x;q,a)-\frac{x}{\varphi(q)}\right|
 <c_\theta(q)\frac{x}{\log x},
 \quad c_\theta(q)\le\frac1{840}\ (3\le q\le10^4),
 \quad x_\theta(q)\le8\cdot10^9\ (3\le q\le10^5).             \tag{164.R7}
\]

Only \(q=4\), \(a=1,3\), and fixed relative intervals \([\alpha T,\beta T]\), \(0<\alpha<\beta\), are used. Both endpoints must exceed the threshold. No shrinking-interval or close-prime density is imported.

## Proof or derivation

For (164.R2), write \(M_N=pqR_N\) in the selected case. The retained divisors are \(a\) and \(pqa\), \(a\mid R_N\), so their character sum is

\[
 \sum_{a\mid R_N}\chi_4(a)(1+\chi_4(pq))=0.
\]

Without selection, multiplicativity gives the first Euler product. This also confirms that ambient sign balance is complete information only before the physical window and profiles are imposed.

For the odd four-prime control, take

\[
 N=r_1r_2s_1s_2,\qquad r_i\equiv1\pmod4,\quad s_i\equiv3\pmod4,
\]

with all primes in sufficiently short fixed relative boxes inside \([P,(1+\vartheta)P]\), \(0<\vartheta<1\). One-prime divisors are below \(\sqrt N\), three-prime divisors exceed \(2\sqrt N\), and each of the three complementary two-prime partitions has exactly one representative in \([\sqrt N,2\sqrt N]\): the upper-to-lower product ratio is at most \((1+\vartheta)^2<4\). The three physical signs are

\[
 \{+,-,-\}.
\]

With no selector, their sum is \(-1\). If any opposite-character pair is selected, the same-class partition separates the chosen primes and is XOR; exactly one mixed partition also separates them and is XOR; the other mixed partition contains both selected primes on one side and neither on the other. Its physical representative has character \(-1\). Thus the residual remains \(-1\) for every possible selector output, although the full selected divisor cube has equal positive and negative masses.

For the even control, choose fixed \(2<C<8\), a high prime \(h\asymp CP\), low primes \(r,s_1,s_2\asymp P\), and

\[
 N=2hrs_1s_2,\qquad h,r\equiv1\pmod4,\quad s_1,s_2\equiv3\pmod4.
\]

The boxes can be shortened so that the only physical odd divisors are \(hr,hs_1,hs_2\), since uniformly

\[
 1<\frac{(hu)^2}{N}=
 \frac{hu}{2\prod_{v\ne u}v}<4.
\]

Low-low products lie below \(\sqrt N\), three-prime odd products lie above \(2\sqrt N\), and the complementary leg retains the factor \(2\). The high prime is a fixed ratio from every low prime, so a selected pair can only be \(r,s_i\). It deletes \(hr,hs_i\) and leaves \(hs_{3-i}\), of sign \(-1\). This proves selector robustness on the even branch without replacing the physical complement by an odd one.

Apply (164.R7) at \(\alpha T\) and \(\beta T\). For sufficiently large \(T\),

\[
 \theta(\beta T;4,a)-\theta(\alpha T;4,a)
 \ge \frac{(\beta-\alpha)T}{2}
 -\frac{\beta T}{840\log(\beta T)}
 -\frac{\alpha T}{840\log(\alpha T)}
 \gg_{\alpha,\beta}T.
\]

Dividing by \(\log(\beta T)\) gives \(\gg T/\log T\) primes in each fixed box. Four disjoint boxes, unique factorization, and deletion of repeated-prime diagonals give (164.R4), with fixed scale constants chosen so all products lie in the interior of the inherited \(N\)-shell.

The literal profile bound is also valid. On a smooth cell, with \(u=\log d\) and \(d\asymp L\), differentiation gives

\[
 \left|\frac d{du}\eta_L(e^u)\right|\ll1,
 \qquad
 \left|\frac d{du}\Phi\!\left(\frac{e^u}{H+1}\right)\right|
 \ll \frac LH,
 \qquad
 \left|\frac d{du}W\!\left(\frac{\sqrt{q_X}e^u}{2\sqrt N}\right)\right|
 \ll1.                                                        \tag{164.R8}
\]

The factors are bounded, there are only finitely many accepted hard faces, and zero extension contributes only their endpoint jumps. Hence the continuum variation is \(O(1+L/H)\). Ordered sampling on any residual divisor subsequence cannot increase total variation, proving \(V_N\ll1\). This uses the actual fixed \(\eta_L,W\) interfaces and the accepted \(C^1\) bound for \(\Phi\), rather than an unspecified “smooth profile.”

It still does not turn (164.R4) into physical lower mass. The diagnostic replaces the exact sampled product \(\eta_L\Phi W\) by the unit physical-window profile. The accepted upper seminorms do not assert that the chosen prime boxes lie on a common positive lower plateau with a noncancelling literal three-atom sum. More decisively, even a future lower bound for \(|c_N^{\rm rem}|\) would leave

\[
 \mathcal S_{L,1}^{\rm rem}=\sum_Nc_N^{\rm rem}e(J\sqrt N)
\]

free to cancel across \(N\). Thus (164.R4) is a coefficient-uniform positive-route obstruction, not an oscillatory lower bound.

For the Fejer step, write \(Y_s=\sum_{j=0}^{R-1}z_{s+j}\). Each diagonal occurs in \(R\) windows and a pair at gap \(r\) occurs in \(R-r\) windows, giving (164.C23) exactly. Also

\[
 \sum_sY_s=R\sum_Nz_N,\qquad
 \#\{s:Y_s\ne0\}\le M_L+R-1.
\]

Cauchy therefore yields (164.R5), including both shell endpoints. The elementary bound \(|b_N^{\rm rem}|\ll\tau(M_N)\), or the accepted truncated-divisor energy where applicable, gives

\[
 \sum_N|c_N^{\rm rem}|^2\ll_\varepsilon L^2X^\varepsilon.      \tag{164.R9}
\]

With \(M_L\asymp L^2\) and \(R\asymp L\), (164.R5) costs one factor \(L\); (164.R6) and (164.R9) give \(\mathfrak E_R\ll L^2X^\varepsilon\), hence

\[
 |\mathcal S_{L,1}^{\rm rem}|^2\ll L^3X^\varepsilon.
\]

No \(H\) or \(J\) power is lost: \(J\) remains inside the phase and \(H\) only belongs to the bounded literal coefficient. If \(R=o(L)\), the same worst-case \(M_L\asymp L^2\), \(\mathfrak E_R\ll L^2\) ledger gives \(L^4/R>L^3\), explaining the conditional minimality. Opening the two coefficients preserves parity and gives exactly

\[
 N=dm,\qquad N+r=d'm',\qquad d'm'-dm=r,\qquad 1\le r<R,
\]

with the factor \(2\) in \(m\) or \(m'\) on the even branch. The only cancellation now requested is the joint signed real-part cancellation over \(N\) and short shifts \(r\), with the fixed outer phase \(e(J(\sqrt{N+r}-\sqrt N))\). Long-shift terms are not estimated termwise; the sliding-window inequality bypasses them.

Finally, the accepted rank-one ledger is numerically correct. A coefficient has scale \(L^{3/2}/(QR\sqrt J)\), while the collar has

\[
 \ll_\varepsilon\left(\frac{QRJ}{L}+1\right)(XQR)^\varepsilon
\]

factor pairs. Their positive product is

\[
 \sqrt{JL}\,X^\varepsilon
 =L^{3/2}\left(\frac HL+O(L^{-1})\right)X^\varepsilon,
\]

and comparison with the trivial \(L^2\) capacity is

\[
 L^{3/2}\min\{L^{1/2},H/L\}\,X^\varepsilon.
\]

These powers are sound. What is not sound is identifying this multiplicative collar with the additive short-shift geometry obtained by taking moduli in (164.R6).

The updated literature exclusions are also correct at their stated interfaces. Cloitre gives an equivalent Fibonacci encoding, not a new upper estimate; Gao imposes a smooth-number restriction; Haynes--Lutsko and Edwin--Lin count different Penrose or Fourier-quasicrystal point sets; Ehrenborg is computational/heuristic; and Bag--Mazumder assumes polynomial phases with a minor-arc leading coefficient. None accepts the moving literal residual coefficient together with the nonlinear square-root phase and \(d'm'-dm=r\). This is a source-by-source non-placement, not a completeness theorem. The scan's DOI 10.1016/j.jnt.2025.10.013 should be identified precisely as Karak--Mahatab, *The Piltz divisor problem in number fields using the resonance method*; its introduction makes the comparative Li--Yang remark, but it is not a new circle upper theorem. Finally, the arXiv record verifies Li--Yang's version and preprint status, while the accepted project theorem is the separately repaired narrow conclusion with exponent \((3292+25\sqrt{1717})/13762\). The printed general Li--Yang interfaces remain outside scope.

## First doubtful or unproved step

The first doubtful statement in the candidate is the word “require” before (164.C19). Actual-profile BV control naturally produces (164.R1), and \(V_N\ll1\) gives the unweighted sum only as a sufficient coefficient-uniform majorant. The selector-robust four-prime diagnostic proves that this uniform majorant has \(L^{2-o(1)}\) capacity; it does not prove \(V_N\gg1\), \(|b_N^{\rm rem}|\gg1\), or a common literal sign on those rows.

After repairing that scope, the first genuinely unproved affirmative step is (164.R6), equivalently an upper bound \(\mathfrak E_R\ll_\varepsilon L^2X^\varepsilon\) for the actual residual direction. It must retain the aggregate real part, both selector statuses, both parity branches, every literal profile and boundary value, and the arbitrary real centre. It must fail on the phase-aligned arbitrary array \(c_N=e(-J\sqrt N)\). Neither Bennett et al., the BV lemma, the four-prime count, the accepted radical-collision sparsity, nor the rank-one positive collar proves it.

## Required control test and outcome

| Control | Outcome |
|---|---|
| full residual sign mass | **GREEN.** Formula (164.R2) is exact; selected mass is zero, while no-pair mass is positive exactly in the all-\(1\pmod4\) odd-prime case. |
| odd selector-robust four-prime geometry | **GREEN.** Exactly three physical two-prime representatives have signs \(\{+,-,-\}\); every selected opposite pair deletes two XOR representatives and leaves one negative residual. |
| even selector-robust geometry | **GREEN.** The factor \(2\) stays on the complementary leg; \(2<C<8\) gives precisely \(hr,hs_1,hs_2\), and every possible selection leaves one negative atom. |
| fixed-box prime count and squarefreeness | **GREEN.** Bennett et al. is used only at \(q=4\), coprime residues \(1,3\), fixed relative intervals above threshold; unique factorization gives \(L^2/(\log L)^4\). It gives no close-prime density. |
| actual profile variation | **GREEN.** Equation (164.R8), finitely many hard faces, and variation monotonicity under subsequences give \(V_N\ll1\), uniformly in selector and parity. |
| raw capacity versus literal mass | **GREEN only after quarantine.** The unit-profile count refutes coefficient-uniform positive BV/transport closure. It is not a lower profile theorem and cannot remove cross-\(N\) phase cancellation. |
| Abel target formulation | **REPAIR.** Replace unweighted (164.C19) as a literal necessity by weighted (164.R1); retain the unweighted quantity only as the uniform BV envelope. |
| Fejer identities and \(L,H,J,X\) ledger | **GREEN.** Window multiplicities, endpoint count, diagonal \(L^2X^\varepsilon\), \(R\asymp L\), target square \(L^3\), exact phase, and \(d'm'-dm=r\) all check. |
| minimal Fejer length | **GREEN with wording repair.** Use \(M_L\asymp L^2\), or say minimal for the worst-case shell ledger. |
| rank-one comparison | **GREEN powers, REVISE geometry.** The \(\sqrt{JL}\) and \(L^{3/2}\min\{L^{1/2},H/L\}\) powers are exact; the additive and multiplicative collars are not identical. |
| updated literature | **GREEN as a dated scoped scan, REVISE source wording.** No listed source supplies (164.R6). Do not promote “no source exists,” and describe Li--Yang only through the accepted five-repair narrow theorem. |
| outer phase and downstream scope | **GREEN.** Cross-\(N\) cancellation remains possible only in the actual signed aggregate; no hard-TOP parent, M9 node, bridge, quarter target, or exponent changes. |

No numerical or symbolic experiment was used.

## Dependencies and exact artifacts used

Repository artifacts read and used were:

1. protocol.md;
2. state/proof_obligations.yml, especially H4-Phi-regularity, M9-M2-dyadic-weight-nondegeneracy, M9-M2-top-endpoint-actual-symbol-variation, M9-M2-hard-top-truncated-divisor-energy-and-radical-control, Li-Yang-source-audit, and GC-external-Li-Yang-theta-star;
3. state/active_campaign.yml;
4. rounds/codex-managed/m9-m2-hard-top-t1-residual-signed-divisor-transport-gate/candidates/conductor_round164_residual_transport_fejer_reduction.md;
5. all three Round-164 primary reports in the same gate: reports/complete_residual_transport_attack.md, reports/blind_residual_transport_rederivation.md, and reports/unmatched_transport_capacity_hostile_audit.md;
6. rounds/codex-managed/m9-m2-hard-top-t1-residual-signed-divisor-transport-gate/controls/conductor_round164_updated_literature_scan.md;
7. rounds/codex-managed/m9-endpoint-fixed-profile-attack/reports/dyadic_profile_certificate.md;
8. rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/reviews/conductor_round77_adjudication.md and its synthesis.md;
9. rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/reviews/conductor_round163_adjudication.md;
10. proofs/kernels/m9_m2_hard_top_t1_close_opposite_prime_exchange_sector.md;
11. proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md;
12. sources/vaaler_1985.md and rounds/codex-managed/m9-unit-frequency-w1-validation/reports/h4_weight_normalization_review.md for the accepted \(\Phi\) interface; and
13. sources/li_yang_2023.md for the accepted external-exponent/source scope.

Primary-source checks used Bennett--Martin--O'Bryant--Rechnitzer, arXiv:1802.00085v3, Theorem 1.2 and equations (1.10)--(1.12); the official arXiv record for Li--Yang, arXiv:2308.14859v2; and the publisher page for Karak--Mahatab, *The Piltz divisor problem in number fields using the resonance method*, *Journal of Number Theory* **281** (2026), 726--740, DOI 10.1016/j.jnt.2025.10.013. The last article's introduction supports only the comparative literature remark; it is not an independent proof audit of Li--Yang.

## Recommended state effect

**Revise, then promote** a single scoped internal reduction/obstruction node containing the exact residual indicator and sign-mass formula, the sharp BV duality, the selector-robust odd/even \(L^{2-o(1)}\) coefficient-uniform capacity, and the exact Fejer reduction through \(d'm'-dm=r\).

The promoted text should make (164.R1) the literal BV/triangle target, label \(\sum_N\operatorname{osc}C_N\) only as the coefficient-uniform envelope, state \(M_L\asymp L^2\) when claiming minimal \(R\asymp L\), and describe the rank-one collar only as an independent power comparison. It should preserve the outer factor \(e(J\sqrt N)\) and say explicitly that the remaining possible cancellation is the joint signed real part over \(N\) and \(1\le r<L\) in (164.R6).

Do **not** promote the unit-profile count to a literal coefficient lower bound, a lower bound for \(\mathcal S_{L,1}^{\rm rem}\), a selector-density theorem, or a universal literature no-go. Do **not** cite Li--Yang's general theorem as printed; retain the five-repair narrow source node and exact exponent

\[
 \theta_{\rm LY}=\frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots.
\]

Keep (164.R6), the full residual target, all hard-TOP parents, both M9 components, M9, the bridge, endpoint uniformity, the quarter theorem, and both global exponent states open and unchanged.
