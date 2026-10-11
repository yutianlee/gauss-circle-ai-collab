# Round 212 independent oscillatory-attack seam review

## 1. Result and verdict

**GREEN for the complete safe-sector estimates, the conditional shell-dispersion interface, the actual residual absolute-mass lemma, and the precisely defined positive radius-Gram certificate obstruction.** The actual signed shell estimate and A4 remain unproved.

Campaign: `gc-complete-four-point-correlation`. Round: 212.
Task: conductor-directed independent oscillatory-attack seam.
Role: **NONBLIND** reviewer, assigned after completing the separate local-arithmetic report.
Generated: 2026-09-28. Effort: entirely analytical; no numerical experiment.
Starting graph hash is inherited from the claimant, not reread in this seam:
`4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.

Claimant artifact:
`rounds/codex-managed/gc-complete-four-point-correlation/reports/four_point_oscillatory_attack.md`.

**Final claimant SHA-256:**
`7c84d41e28c726d39b13cfe6b1e65f6cf8800ff746ca43b56157954908db423f`.

The conductor relayed the claimant's final-hash confirmation before this binding. An independent filesystem hash check agreed. No mathematical repair is required at that hash. The restrictions already stated by the claimant are essential: the absolute-mass and certificate lower bounds concern fixed interior power scales, and the positive radius-Gram quantity is not the actual pointwise A4.

## 2. Exact hypotheses and scope checked

The parameters are the claimant's exact ones:

\[
b=83/650,\quad T\ge2,\quad T^{4b}<N<T^{1-2b},\quad
R\in I=[T/\sqrt2,\sqrt3T],
\]
\[
L=\max(2,\lceil N^{1/2}T^{-2b}\rceil),\qquad
K=\max(2,\lceil NT^{-4b}\rceil).
\]

The mask `v` is fixed, real, smooth, nonzero, and supported in `[1,4]`; the real mollifier transform satisfies `Psi(0)=1`. The claimant retains the actual `r2` coefficients and complete zero extension. The four-point amplitude is normalized to size one. No hidden physical factor `N^(-3/4)` belongs in that amplitude.

Write

\[
Q=N^{3/2}/T,\quad\Lambda_{h,k}=hk/Q,\quad
\Lambda_*=LK/Q\asymp T^{76/325}.
\]

The complete safe set is the union of `h=k` and `hk<=Q`. Its complement is `Omega`. All upper bounds and the conditional shell implication are asserted throughout the full open band, including bounded integer lengths. The lower-mass and lower-certificate results instead require `N asymp T^alpha` for each fixed `4b<alpha<1-2b`. No uniform claim as alpha approaches the lower endpoint with T is reviewed or supplied.

The positive certificate uses

\[
u_n=r_2(n)|g_N(n)|,\quad
B_{h,k}(n)=u_nu_{n+h}u_{n+k}u_{n+h+k},\quad
M_{h,k}=\sum_nB_{h,k}(n).
\]

It further requires a fixed smooth nonnegative weight `w`, supported inside the normalized R-window, with integral one. Its Fourier transform uses the plus convention `hat w_+(y)=integral w(t)e(ty)dt`. The precise certificate is

\[
G_{h,k}=\sum_{n,m}B_{h,k}(n)B_{h,k}(m)
|\widehat w_+(T[\psi_{h,k}(n)-\psi_{h,k}(m)])|,
\quad
\mathcal P_G=(LK)^{-1}\sum_{\Omega}\sqrt{G_{h,k}}.
\]

The no-go concerns this exact quantity and its displayed shell grouping and trivial-mass cap. It does not concern every Gram method, a centered remainder, or a signed off-diagonal estimate.

## 3. Independent derivation and seam checks

### A. Integer lengths, every safe pair, and shell weights

Let `x=N^(1/2)T^(-2b)>1`. The unrounded lengths are `x` and `x^2`, so monotonicity of the ceiling and the maximum with 2 give `K>=L`. Each exact length is between its unrounded value and twice that value. Thus `LK asymp N^(3/2)T^(-6b)` uniformly even when both cutoffs equal 2. Both are `o(N)` uniformly for large T; a bounded T-range is genuinely finite and can be covered by enlarged constants.

The actual divisor bound, with sufficiently small initial epsilon, gives `M_(h,k)<<NT^epsilon` on the full overlap. There are at most L repeated pairs, so their normalized cost is at most `T^epsilon N/K<=T^(4b+epsilon)`. The positive-shift repeated term has the squared middle factor and is not a zero-frequency diagonal.

For the product sector the count is at most

\[
\sum_{1\le h<L}\lfloor Q/h\rfloor\ll Q\log(2L).
\]

When `Q<1` every summand is zero; the same upper bound is valid. Its normalized coefficient cost is

\[
\ll T^\epsilon NQ\log(2L)/(LK)
\ll T^\epsilon NT^{6b-1}\le T^{4b+\epsilon}.
\]

Counting an intersection pair twice only enlarges the upper bound. These prices retain all axes already paid by the inherited differencing inequality and separately pay all repeated positive shifts.

For residual product shells `2^j<Lambda<=2^(j+1)`, the conventions include powers of two exactly once. The elementary product count gives

\[
\delta_j=|\Omega_j|/(LK)
\ll\min(1,2^j\log(2L)/\Lambda_*),\qquad
\sum_j\delta_j\le1.
\]

The number of nonempty shells is `O(log(2+Lambda_*))`. Cauchy on each shell acts on already complete n-sums and gives `sum_j delta_j sqrt(E_j(R))`. Under the displayed hypothetical bound `sqrt(E_j)<<T^epsilon(N/2^j+sqrt(N))`,

\[
\sum_j\delta_j/2^j
\ll\log(2L)\log(2+\Lambda_*)/\Lambda_*.
\]

Consequently the complete price is

\[
T^\epsilon\left(N/K+N/\Lambda_*+\sqrt N\right)
\ll T^{166/325+\epsilon}.
\]

The logarithms can be absorbed by first selecting smaller epsilon budgets. The upper-band powers are `N/Lambda_*<=T^(166/325)` and `sqrt(N)<=T^(121/325)`. No shift complement or shell normalization is missing.

### B. Signed energy and the actual coefficient convention

With `c_(h,k)(n)=a_(h,k)(n)W_(h,k)(n)`, the coefficients are real and

\[
|D_{h,k}(R)|^2=\sum_{n,m}c_{h,k}(n)c_{h,k}(m)
e(R[\psi_{h,k}(n)-\psi_{h,k}(m)]).
\]

Averaging this equality over a shell gives the claimant's energy exactly. Its n=m diagonal is `O(NT^epsilon)`. The remaining sum is real by pairing `(n,m)` with `(m,n)`. Its one-sided upper estimate of order `T^epsilon(N^2 2^(-2j)+N)` is sufficient for the stated shell root-mean-square bound. No absolute off-diagonal estimate is implicitly substituted.

The displayed divisor expansion has all four actual divisors and factor `4^4`; multiplying two copies gives `4^8`. The Gaussian formulation counts all ordered representations. The even-shift, odd-n character product in the claimant is indeed one: adding either even shift either preserves or changes each relevant residue-four sign in matching pairs. This is an algebraic dependence test only; it creates no lower bound for the full signed expansion. The report observes that limitation correctly.

### C. Actual residual mass, including both moving-sum axes

I rederive the main lower-mass lemma from its one-point inputs. The elementary disk-area estimate and a fixed interval on which `|v|` is bounded below give

\[
S:=\sum_nu_n\asymp N,\qquad \max_nu_n\ll_\epsilon N^\epsilon.
\]

The mollifier factor is bounded away from zero on that interval for sufficiently large T because `N/T<=T^(-2b)`. This uses only actual one-point lattice counts, not a four-point density. The support has length `O(N)`.

For a nonnegative sequence z supported on such an interval, set `B_m=sum_(j=0)^(H-1) z_(m+j)`. There are `O(N+H)` nonzero B_m, and `sum_m B_m=H sum z`. Cauchy and exact expansion imply

\[
\sum_nz_n^2+2\sum_{r=1}^{H-1}(1-r/H)
\sum_nz_nz_{n+r}\ge c(H/N)(\sum_nz_n)^2
\tag{R1}
\]

for `H<=O(N)`. This includes all zero-extended boundaries.

Apply (R1) with z=u and H=L. The axis `h=0` contributes `sum u_n^2<<N^(1+epsilon)`. At fixed `alpha>4b`, L grows by a positive power of T, so epsilon can be selected to make `N^epsilon=o(L)`. Removing this axis and using nonnegativity gives

\[
\sum_{1\le h<L}C_h^u\gg LN.
\tag{R2}
\]

Next apply (R1) with `z_n=u_nu_(n+h)` and H=K, and sum in h. Cauchy over the h-range gives

\[
\sum_{h<L}(C_h^u)^2\ge
\frac{(\sum_{h<L}C_h^u)^2}{L-1}\gg LN^2.
\]

The second axis `k=0` is explicitly `sum_h sum_n u_n^2u_(n+h)^2<<L N^(1+epsilon)`. Thus, after dropping only weights at most one from the nonnegative off-axis terms,

\[
\sum_{h<L,k<K}M_{h,k}
\gg LKN-O_\epsilon(LN^{1+\epsilon})\gg LKN,
\tag{R3}
\]

because `N^epsilon=o(K)`. This proves the claimant's total mass, including the crucial subtraction of both moving-sum axes. It neither counts h=0 or k=0 as residual mass nor supposes that each individual correlation is large.

The union of the subsequently paid repeated-shift and small-product sectors has total mass at most

\[
O_\epsilon\left(N^{1+\epsilon}[L+Q\log(2L)]\right).
\]

Dividing by LKN gives

\[
O_\epsilon\left(N^\epsilon/K+
N^\epsilon\log(2L)/\Lambda_*\right)=o(1).
\]

For a fixed interior alpha, one sufficiently small epsilon makes all three needed comparisons hold: `N^epsilon=o(L)`, `N^epsilon=o(K)`, and `N^epsilon log(2L)=o(Lambda_*)`. Hence the actual surviving mass is

\[
\sum_{(h,k)\in\Omega}M_{h,k}\gg LKN.
\tag{R4}
\]

The fixed-interior qualification is necessary. For cutoffs that stay bounded near the lower endpoint, the argument cannot subtract the axes in this way; the claimant does not assert (R4) there.

### D. Exact radius normalization, sign masks, and the Gram lower bound

Changing variables `R=Tt` gives exactly

\[
\frac1T\int w(R/T)|D_{h,k}(R)|^2dR
=\sum_{n,m}c_{h,k}(n)c_{h,k}(m)
\widehat w_+(T[\psi_{h,k}(n)-\psi_{h,k}(m)]).
\tag{R5}
\]

There is no extra T on the right. The measure `T^(-1)w(R/T)dR` has mass one, which is required for the subsequent radius Cauchy inequality. This is a radius mean square, whereas E_j(R) is a shift mean square at fixed R. The two norms are not interchanged in the report.

The equality (R5) keeps every sign of the real mask W. Taking a modulus termwise bounds it by G because `|c_(h,k)(n)|=B_(h,k)(n)`. The sequence u containing `|g_N|` is introduced only for that explicitly positive certificate. This supplies no false sign condition on the original mask, and a positive lower bound for G supplies no lower bound for (R5).

Since `hat w_+(0)=1`, its modulus is at least 1/2 in a fixed neighborhood of zero. The exact third-derivative identity gives

\[
|\psi'_{h,k}(t)|\ll hkN^{-5/2}.
\]

Partitioning the ambient interval into `J<=C(1+Lambda_(h,k))` consecutive bins of length at most `cN/(1+Lambda_(h,k))` makes every within-bin normalized frequency difference at most that fixed neighborhood radius. If b_i is the B-mass in a bin, the complete positive sum obeys

\[
G_{h,k}\ge\tfrac12\sum_i b_i^2
\ge c M_{h,k}^2/(1+\Lambda_{h,k}).
\tag{R6}
\]

All integers, including endpoints, occur in exactly one bin. No cancellation or density is required. Combining (R4), (R6), and `Lambda<Lambda_*` proves

\[
\mathcal P_G\gg N/\sqrt{\Lambda_*}
\asymp N T^{-38/325}.
\tag{R7}
\]

The corresponding target ratio at `N asymp T^alpha` is

\[
T^{\alpha-38/325-166/325}=T^{\alpha-204/325}.
\]

This is a fixed power excess precisely on the asserted upper subband `204/325<alpha<242/325`. Its supremal edge deficit is `38/325`, with no assertion that the open endpoint is attained. For any fixed positive gap, sufficiently small target epsilon cannot absorb it.

### E. Shell grouping, caps, and the exact no-go scope

For each shell, concavity of the square root gives `sqrt(avg G)>=avg sqrt(G)`. After multiplying by delta_j and summing, shell grouping produces a certificate at least P_G. Also `|hat w_+|<=integral w=1`, so `sqrt(G)<=M`; taking the individual minimum with the trivial mass leaves sqrt(G) unchanged. Both advertised modifications preserve (R7).

Radius Cauchy gives an upper bound by P_G for the normalized radius average of the residual absolute correlations. It does not give an upper bound for `sup_R A4`. The report states this explicitly and grants any additional pointwise step optimistically when testing the certificate. A positive certificate already exceeding the target cannot establish the target by proving that same certificate small, even for the weaker radius-average problem. This conclusion is correctly limited to the displayed positive closure. It is neither a lower bound for the actual radius average nor a lower bound for A4.

The inherited finite two-stage inequality and reconstruction are used only conditionally: a proof of the complete shell hypothesis would supply the fixed `102/325` milestone. The report supplies no such proof and no full-quarter consequence.

## 4. First doubtful or unproved step

No defect was found in the finite mass lemma, the safe-sector subtractions, or the exact positive-certificate lower bound at the bound hash.

The first missing arithmetic input remains the complete fixed-R shell bound, claimant equation (16), or its sufficient signed off-diagonal version (19). The exact divisor and Gaussian representations do not estimate that quantity. The averaged mass theorem estimates a different, nonnegative object.

Replacing the signed Fourier kernel in the radius identity by its absolute value and then expecting the positive certificate to be of target size is rigorously excluded on the stated upper subband. This does not exclude retaining its complex signs, proving a suitable centered remainder, or using a different mechanism. A passage from radius average to pointwise supremum remains separate and unproved; the report does not hide its cost.

## 5. Required controls and outcomes

| Control | Verdict |
|---|---|
| Actual four-point coefficients | GREEN: actual r2, all four translated masks, and factors `4^4` / `4^8` are retained. |
| Complete shifts and axes | GREEN: h=0 and k=0 are separately subtracted in the mass proof; h=k>0 is separately paid; the residual includes the complete remaining rectangle. |
| Safe-sector subtraction | GREEN at fixed interior powers: removed absolute mass is o(LKN), with all epsilon requirements compatible. Upper sector prices remain uniform on the full band. |
| Density hypotheses | GREEN: only one-point disk-area counts are used for the mass lemma. No four-point density or mean is presumed. |
| Local versus global information | GREEN: Gram bins lower-bound a positive quantity; they do not prove local discrepancy or a correlation asymptotic. |
| Radius versus shift norm | GREEN: `(1/T) integral w(R/T)` has mass one; fixed-R shell energies are distinct and no implication between the norms is fabricated. |
| Sign-changing mask | GREEN: original signs persist in the exact energy. Absolute masks enter only the defined positive certificate. |
| Shell multiplicity | GREEN: product-shell proportions restore the `N/2^j` cost; no unweighted rectangle Cauchy is substituted. |
| Real endpoints | GREEN: real parameters, zero extension, real-bin conventions, and the disk-area endpoint error are all covered. |
| Restored powers | GREEN: target `166/325`, phase range `76/325`, Gram root loss `38/325`, and threshold `204/325` check independently. |
| Signed versus positive claim | GREEN: the lower bound is solely for P_G and its stated modifications, never for D or A4. |
| Full-quarter scope | GREEN: shell input, milestone, signed tenth moment, M1/M2, and quarter target are not promoted. |
| Statement-only isolation | NONBLIND as assigned. This is not the separate isolated derivation; no blind report or packet was read. |

No experiment or external theorem audit was used in this seam.

## 6. Dependencies, access boundary, and hashes

This seam used only the claimant, `protocol.md`, and the already permitted closed211 finite ledger and review:

| Artifact | SHA-256 |
|---|---|
| `reports/four_point_oscillatory_attack.md` in this campaign | `7c84d41e28c726d39b13cfe6b1e65f6cf8800ff746ca43b56157954908db423f` |
| `rounds/codex-managed/gc-full-source-method-review/controls/conductor_two_stage_strategy.md` | `9bf8f30d240304f88c46a5a93c7d93586b3ade1c674d5a5fdbc61a251fcd176f` |
| `rounds/codex-managed/gc-full-source-method-review/reviews/independent_two_stage_review.md` | `052c3362897ae5185eee0a7afed6242164b3fa0ae6c89edcef90466c5d2adca5` |

The inherited ledger/review supply the accepted finite normalization and conditional reconstruction scope; the key actual mass and Gram arguments were independently rederived above. Files cited by the claimant as historical context were not opened during this seam. No blind report, conductor ledger, other current sibling report, shared state, synthesis, or successor file was read or edited for the seam. The reviewer's earlier finalized local-arithmetic report was not edited or used as a mathematical dependency.

Only this assigned review file was written. The claimant's content hash was independently checked and then confirmed by the conductor as the author's final hash before binding.

## 7. Recommended state effect and final binding

**Retain** the claimant's established finite lemmas, complete conditional shell interface, and scoped actual-coefficient certificate obstruction as reviewed evidence. **No change** to the accepted arithmetic target, pointwise exponent, moments, proof draft, or M1/M2 parents. Do not promote claimant (16) or (19), and do not turn (34) into an actual lower bound for A4.

The GREEN verdict binds only to claimant SHA-256
`7c84d41e28c726d39b13cfe6b1e65f6cf8800ff746ca43b56157954908db423f`.
Any material edit requires a renewed binding. The assigned same-round seam is complete; no successor is designed.
