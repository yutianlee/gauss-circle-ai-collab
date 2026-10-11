# Round 209 — independent tenth-power review

Campaign: `gc-complete-signed-tenth-moment`  
Task: `independent_tenth_power_review`  
Role: separate **nonblind** review of the conductor's ledger and its round-208 bridge  
Generated: 2026-09-27  
Graph hash reported by the source ledgers: `4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`

## 1. Result: GREEN for the conditional certificate and obstruction

The mathematics of C1--C9, including the hypothetical C5-to-C6 implication, the thresholds 61/572 and 574/45, and the open-band endpoint bookkeeping, checks independently. The exact accepted beta must satisfy b<beta<1/6; this hypothesis has now been made explicit in the source and is verified algebraically below.

Two small source clarifications were requested and checked in the final version: the exact-mass paragraph now explicitly requires nonnegative envelope weights, and the first-unproved-step paragraph correctly refers to the high-level integral following C4. Final verdict: **GREEN** for C1--C9 as the stated conditional certificate and absolute-majorant obstruction, bound to the exact hashes in section 6. This does not certify C5 or the actual signed tenth-moment gate.

This is a new nonblind assignment. The earlier `reports/blind_ten_root_audit.md` was completed using only `protocol.md` and the isolated statement packet, before this assignment. Its historical statement-only isolation is preserved; that report has not been edited or retroactively supplemented with this review's context.

## 2. Exact statement and hypotheses

Use the actual H_N, its complete centered shell Z_N, I=[T/sqrt(2),sqrt(3)T], and J=[T^2/2,3T^2] from the assigned round-208 source. Put

\[
 b=\frac{83}{650},\qquad q=\frac{136}{13},\qquad
 \alpha_-=4b=\frac{166}{325},\quad
 \alpha_+=1-2b=\frac{242}{325},
\]

\[
 \beta=\frac{50\sqrt{1717}-297}{13762},\qquad
 \omega=\min\{\alpha/4,\beta,(1-\alpha)/2\},\quad N=T^\alpha.
\]

The reviewed claims concern alpha_-<alpha<alpha_+, real T>=2, with uniform constants and arbitrarily small power losses. In particular an occurrence of T^epsilon in an input does not fix the epsilon used in the final output: choose smaller input losses first and relabel their finite sum.

Retained source hypotheses are the variance/Chebyshev bound

\[
 D(V)\ll_\eta T^\eta A V^{-2}\quad(V>0),\qquad
 A=TN^{-1/2},
\]

the reviewed large-value bound for V>=1, and a supremum bound |H_N|<=W_* with W_*<<_eta T^(omega+eta). The additional C5 hypothesis is

\[
 D(V)\ll_\eta T^\eta(aV^{-2}+BV^{-q})\quad(V\ge1),
 \qquad a=T^{-\sigma},\quad B=TN^{-\lambda},
\]

where 0<=lambda<=1/2 and sigma>=0 are fixed. C5 remains hypothetical for the actual coefficients. Fixed constants in W_* cause only fixed factors in the integrals below.

The transfer to the pointwise exponent is conditional on the stated complete shell bridge, its error, the global coefficient bound, and all complementary reconstruction bounds in the assigned round-208 source. This review checks their use and powers; it does not re-open the external theorems or earlier graph validation that supply those inputs.

## 3. Proof and derivation

### Exact beta range, C1--C3, and the deficit profile

The elementary squared inequalities

\[
 (207/5)^2<1717<(83/2)^2
\]

give 1773/13762<beta<1778/13762. The lower bound exceeds b because

\[
 1773\cdot650-83\cdot13762=10204>0,
\]

and the upper bound is below 1/6 because 6*1778=10668<13762. Thus

\[
 \alpha_-=4b<4\beta<\frac23<1-2\beta<1-2b=\alpha_+.
                                                               \tag{R1}
\]

All three omega branches and both junctions therefore occur in the required band. The more general condition b<min(beta,1/6), without the actual beta range, would not alone establish this ordering; the updated source correctly states the needed range.

The integration below, with lambda=sigma=0, proves C1. Dividing its two terms by U=T^(10b)N^(-1/2) gives exactly

\[
 d_A=1-10b+\frac{26}{55}\alpha,
 \qquad d_B=8\omega-10b+\frac\alpha2,
\]

which verifies C2. Since 10b-1=18/65,

\[
 d_A>0\iff \alpha>\frac{18}{65}\frac{55}{26}
 =\frac{99}{169}.
\]

The threshold is strictly inside (alpha_-,alpha_+), verifying C3. The endpoint values are

\[
 d_A(\alpha_-)=-\frac{634}{17875},\quad
 d_A(\alpha_+)=\frac{1342}{17875},\quad
 d_B(\alpha_-)=0,\quad d_B(\alpha_+)=\frac{38}{325}.
                                                               \tag{R2}
\]

On the three successive omega branches, d_B has slopes 5/2, 1/2, and -7/2. Its maximum occurs at the interior junction alpha=1-2beta and equals

\[
 8\beta-10b+\frac{1-2\beta}{2}
 =7\beta-\frac{101}{130}.                                \tag{R3}
\]

The slopes of d_B-d_A are 223/110, 3/110, and -437/110. Its minimum over the closed band is at an outer endpoint, where it equals respectively 634/17875 and 748/17875. Thus d_B>d_A throughout, including the endpoints. These facts justify the statement that deleting only the second summand of C1 leaves the first certificate insufficient on a nonempty final portion of the band. They do not show that a successful arithmetic proof must have two separate improvements.

### C4: low amplitudes and the exact layer-cake boundary

For L=T^(9/260), the pointwise inequality |H|^10 1_(|H|<=L)<=L^8|H|^2 gives the asserted low-amplitude bound, using the retained variance input:

\[
 L^8M_2\ll_\eta T^\eta T^{1+72/260}N^{-1/2}
 =T^\eta U.
\]

The same conclusion follows directly from the all-V Chebyshev bound by integrating to L, so there is no need to extend the large-value input below 1. With D(V)=measure{|H|>V}, the exact identity is

\[
 \int_{|H|>L}|H|^{10}
 =L^{10}D(L)+10\int_L^\infty V^9D(V)\,dV.                \tag{R4}
\]

It remains valid if the level set {|H|=L} has positive measure. The strict inequality in D excludes that set from both sides. The boundary term is at most T^eta A L^8<<T^eta U. Consequently M10<<T^epsilon U is equivalent, at the stated power-loss level, to the bound for the remaining nonnegative tail integral in (R4), or to the bound for the full high-amplitude part. This is a reduction, not a proof of that bound.

### C5--C6: both tails, the subunit region, and W_*<V0

Set

\[
 V_0=(B/A)^{1/(q-2)}
 =N^{(1/2-\lambda)/(q-2)}\ge1.
\]

The inequality V0>=1 is precisely where lambda<=1/2 is needed in this proof. Since M10=10 integral_0^infinity V^9D(V)dV, if W_*>=V0 then, apart from a common fixed constant and an input T^eta factor, the bound is

\[
 \frac{10}{8}A V_0^8
 +\frac{10}{8}a(W_*^8-V_0^8)
 +\frac{10}{q-10}B(V_0^{10-q}-W_*^{10-q}).              \tag{R5}
\]

The first integral uses variance on the entire interval (0,V0), including (0,1); it converges because its integrand is proportional to V^7. The other two integrals use C5 only on [V0,W_*], where V>=1. Both subtracted endpoints in (R5) have the correct signs because q>10. Dropping them for an upper bound gives

\[
 M_{10}\ll_\eta T^\eta(A V_0^8+aW_*^8+B V_0^{10-q}).
\]

The matching boundary relation is specifically

\[
 B V_0^{10-q}=A V_0^8.
\]

It concerns the q-tail and variance; it does not identify the separate a-tail with either of them.

If W_*<V0, variance alone gives

\[
 M_{10}\ll_\eta T^\eta A W_*^8
 \le T^\eta A V_0^8.
\]

Thus no reversed integration interval or illicit negative term is introduced in this case. For lambda=1/2, V0=1 exactly, and the same argument covers the boundary without using C5 below 1. The formulas also agree continuously at W_*=V0.

Finally, q-2=110/13, and therefore

\[
 A V_0^8
 =T N^{-1/2+8(1/2-\lambda)/(q-2)}
 =T N^{-3/110-(52/55)\lambda}.
\]

Also aW_*^8<<_eta T^(-sigma+8omega+8eta). Choosing the input eta sufficiently small and relabeling the combined loss proves C6. Setting lambda=sigma=0 proves C1 with both of its terms retained.

### C7 and the alternative q' threshold

The first C6 summand is at most U if

\[
 \lambda\ge\frac{55}{52}
 \left(\frac{26}{55}-\frac{10b-1}{\alpha}\right).
\]

The right side increases with alpha. Its supremum over the open band is its limit at alpha_+=242/325, where

\[
 \frac{10b-1}{\alpha_+}=\frac{45}{121},\qquad
 \frac{26}{55}-\frac{45}{121}=\frac{61}{605},\qquad
 \frac{55}{52}\frac{61}{605}=\frac{61}{572}.              \tag{R6}
\]

This value belongs to [0,1/2]. Equality at the sufficient threshold is allowed: it controls the closed limiting endpoint and hence gives a uniform estimate on the open band. For any fixed smaller lambda, this first explicit summand exceeds U on some interior scales near the upper endpoint.

The second C6 summand is at most U if sigma>=max d_B, which is (R3). Its maximum is attained at an interior alpha, not merely approached at an excluded endpoint. This threshold is positive since beta>b and 7b-101/130=38/325>0. Thus both inequalities in C7 are valid sufficient conditions for the displayed separable certificate. Neither is asserted necessary for the true moment.

For fixed q'>10 and lambda=0, the same integration gives the first summand

\[
 T N^{-(q'-10)/(2(q'-2))}.
\]

Its excess over U has exponent 1-10b+4alpha/(q'-2). Requiring this explicit term to meet U uniformly over the band is equivalent to

\[
 q'-2\ge\frac{4\alpha_+}{10b-1}
 =\frac{484}{45},\qquad q'\ge\frac{574}{45}.             \tag{R7}
\]

Equality is again sufficient; q'=10 is excluded because the high-tail integration becomes logarithmic. Constants can depend on the fixed positive number q'-10. This alternative does not remove the unchanged V^-2 tail and makes no assertion that such a q' bound is available.

### C8--C9, centering, and the complete bridge

The exact-mass and close-five-root-sum arguments agree with the independently completed statement-only report. With nonnegative envelope weights, A_d<<N^(-1/4+eta)d^(-1/2), including d near 4N, so sum_d A_d^2<<N^(-1/2+2eta)log(2N). Every exact relation partitions into squarefree-class blocks of size at least two. Bounding the mass of a block of size m by sum_d A_d^m<=(sum_d A_d^2)^(m/2), then summing finitely many index partitions, proves the required exact mass without restricting to pairings. This also provides a direct check of the cited kernel's use without needing its historical proof.

The exact tenth integral is O(TN^(-5/2+epsilon)). Relative to U its size is O(T^(-18/65)N^(-2+epsilon)), hence harmless on the complete selected band. Weighted pigeonholing of all five-root sums gives C8, and

\[
 \frac{N^2}{U}
 =T^{(5/2)\alpha-83/65}
 =T^{(5/2)(\alpha-166/325)}
\]

verifies C9. Exact-frequency removal is negligible uniformly even on the closed selected alpha interval, for sufficiently small fixed epsilon. The positive power in C9, however, has no uniform positive lower bound as alpha approaches the lower boundary. Thus the absolute-majorant obstruction applies at every fixed interior exponent, and uniformly with a fixed power margin only on compact subintervals bounded away from that lower endpoint. It supplies no obstruction at the lower endpoint itself. If the proposed upper bound includes T^rho, the comparison requires rho<(5/2)(alpha-166/325).

For the conditional physical coefficient replacement r2(n)-pi, r2(n) belongs to 4Z and |r2(n)-pi|>=4-pi>0. Moreover |r2(n)-pi|<=(4+pi)tau(n). The same lower coefficient mass and exact upper envelope therefore apply. This is a statement about that absolute expansion if that representation is used; it does not assert that subtracting a discrete mean alone gives an exact centered-shell representation or controls signed correlations.

For completeness, the assigned bridge gives, at power ten,

\[
 M_{10}\ll T^{-6}K_{10}+T^{-4+\epsilon}N^{-10}+O_A(T^{-A}),
\]

and its inverse gives

\[
 K_{10}\ll T^6M_{10}+T^{2+\epsilon}N^{-10}+O_A(T^{-A}).
\]

Thus M10<<T^(83/65+epsilon)N^(-1/2) and K10<<T^(473/65+epsilon)N^(-1/2) are equivalent sufficient gates with harmless explicit errors. Local reproduction contributes N^(1/20)M10^(1/10), whose N powers cancel at this gate and whose T power is b=83/650. The real-radius endpoints retain the positive distance to the complement of I needed for the reproduction tail. At alpha=4b use the known N^(1/4) bound; at alpha=1-2b use the known (T/N)^(1/2) bound. Both equal T^b. The singleton and infinite high-N tail are retained as the round-208 input states. Reconstruction then gives the conditional pointwise exponent 1/4+b/2=102/325, not the quarter theorem.

## 4. First doubtful or unproved step

The first unproved arithmetic input is C5, or another bound that establishes the nonnegative high-amplitude integral after C4 for the actual coefficients. C6 is a proved implication from C5; it does not prove C5. The analogous q' large-value improvement is likewise unproved.

The source variance, large-value distribution theorem, shell bridge, and reconstruction bounds are retained as explicitly reviewed hypotheses supplied by the assigned round-208 source. Their external provenance and graph promotion are outside this nonblind power review. No additional literature result is imported.

An absolute-majorant lower bound cannot be substituted for a signed-moment lower bound. The completed isolated report's displaced real Dirichlet-kernel example already gives a tenth moment O(T) and a nonzero-frequency absolute expansion at least cTL^9, even after collecting equal frequencies. It proves the logical possibility of cancellation between aggregated frequencies. Its full moment includes its exact term; its separately signed off-diagonal part need not be O(T). These distinctions remain essential here.

## 5. Required controls and outcomes

1. **C1--C3 exponent ledger:** pass. Both summands survive integration; the interior threshold is 99/169; endpoint deficits and the dominance of d_B were recomputed explicitly.
2. **Beta branches:** pass after the source made the exact beta value and b<beta<1/6 explicit. The ordered breakpoints are (R1); the maximum used for sigma is interior.
3. **C4 boundary:** pass. The term L^10D(L) is present and paid by variance; low amplitudes are already paid and the remaining tail is unproved.
4. **C5--C6 subunit and endpoint controls:** pass. Variance covers V<1; lambda=1/2 gives V0=1; W_*<V0 uses variance only; both high-tail endpoints occur in (R5); epsilon losses are relabeled only after summing them.
5. **C7 and q' arithmetic:** pass. Exact thresholds are 61/572 and 574/45, with endpoint equality permitted and with the unchanged V^-2 tail explicitly retained in the alternative.
6. **C8--C9 exact removal and centering:** pass for nonnegative envelope weights. All sign patterns and non-pairing squarefree classes are covered. The centered absolute envelope has the same obstruction. No signed lower bound follows.
7. **Bridge and scope:** pass as a conditional implication with the assigned round-208 inputs. Both Jacobian directions, shell errors, real-radius endpoints, complementary N endpoints, singleton, and infinite tail are accounted for. No external source or actual new moment theorem is certified.

All controls are analytical. No mathematical numerical experiment was run. Hashing files is an artifact-integrity operation, not mathematical evidence.

## 6. Dependencies and final SHA256 bindings

The final round-209 ledger was read again after all three clarifications (beta range, nonnegative weights, and the C4 reference), and the following SHA256 bindings were then checked:

| Artifact | SHA256 | Role in this review |
|---|---|---|
| `rounds/codex-managed/gc-complete-signed-tenth-moment/controls/conductor_tenth_power_ledger.md` | `c41087e887dbae00f8c721eab507588414d33d74202f3eb902b8a901048dbca3` | Final reviewed C1--C9 source; GREEN within stated scope |
| `rounds/codex-managed/gc-full-proof-signed-arithmetic-review/controls/conductor_bandlimited_strategy.md` | `6aa17dd35e2d930cedadfb489adf8e042b6aed61ed5882ae8e2eb0cd36fbd552` | Assigned bridge and retained-input source; unchanged during this review |
| `rounds/codex-managed/gc-complete-signed-tenth-moment/reports/blind_ten_root_audit.md` | `a940318a6fe7fd48a66d670ee8c0f9acbe3c8b035fce96f1b53b3639a06f4b8d` | Previously completed isolated report; unchanged; original statement-only provenance retained |

The isolated report's hash matched both integrity checks in this assignment. The current review's GREEN verdict applies only to these bound source versions; any later mathematical edit requires an updated review binding.

The newly read mathematical sources in this separate assignment are only:

- `rounds/codex-managed/gc-complete-signed-tenth-moment/controls/conductor_tenth_power_ledger.md`.
- `rounds/codex-managed/gc-full-proof-signed-arithmetic-review/controls/conductor_bandlimited_strategy.md`.

`protocol.md` and the isolated statement packet had been read in the previous assignment. The already completed isolated derivation is identified as earlier evidence, not reclassified as nonblind. No active graph, historical kernel, other agent report, external paper, or rational-convolution report was read for this assignment. The conductor supplied the exact accepted beta formula, subsequently inserted into and checked against the ledger.

## 7. Recommended state effect

Retain this **GREEN** conditional power-ledger and method-obstruction review at the exact final bindings above. It supports the sufficiency calculations and the failure of the specified absolute majorant at the target scale. It does not establish C5, the complete signed tenth moment, a pointwise improvement, or the quarter theorem.

No proof graph, proof draft, validation matrix, synthesis, or earlier isolated report was edited. Any identity State Patch and graph-node count remain the conductor's responsibility. This assignment stops with this review and does not design a successor round.
