# Round 212: local arithmetic of the complete actual four-point correlation

## 1. Result: exact local-factor lemmas and a scoped source obstruction

Campaign: `gc-complete-four-point-correlation`. Task: `four_point_local_arithmetic`.
Role: discovery, selected-context, NONBLIND. Generated: 2026-09-28.
Starting graph SHA-256: `4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.
Status: candidate evidence only. Effort was entirely analytical; no mathematical computation was run.

The actual local arithmetic supplies the following rigorous results.

* An explicit congruence sector has identically zero four-point coefficients: one shift odd and the other congruent to 2 modulo 4.
* For distinct shifts, the genuine prime-adic norm representation densities define a convergent, nonnegative **candidate** singular product of size `T^epsilon`. Its existence and size do not establish an integer correlation asymptotic.
* The repeated-shift local product behaves differently: its good-prime factors are `1+1/p+O(1/p^2)`. In particular the naive constant singular product diverges for `h=k=1`. No bounded, fixed-density formula can simply be copied from the distinct-shift calculation. The complete repeated-shift contribution is nevertheless paid by the actual divisor envelope.
* A real-interval discrepancy bound of size `T^epsilon ell^theta`, with `theta<=45/83`, against the derived distinct-shift candidate would suffice for the frozen A4 target. The square-root instance gives the fully restored remainder bound `T^(159/325+epsilon)`, below the target by `7/325`.

No such actual discrepancy estimate is proved. The one audited primary correlation theorem fails on the fixed-shift system before any power comparison; its valid three-variable version supplies neither the required absolute shift norm nor a usable short-box error. This is a scoped obstruction to that import, not a refutation of A4 or of the quarter theorem.

## 2. Exact statements and hypotheses

Use the frozen parameters

\[
b=83/650,\quad T\ge2,\quad T^{166/325}<N<T^{242/325},\quad
R\in[T/\sqrt2,\sqrt3T],
\]
\[
L=\max(2,\lceil N^{1/2}T^{-2b}\rceil),\qquad
K=\max(2,\lceil NT^{-4b}\rceil).
\]

For integer `1<=h<L`, `1<=k<K`, let

\[
a_{h,k}(n)=r_2(n)r_2(n+h)r_2(n+k)r_2(n+h+k),\qquad
\Lambda_{h,k}=Thk/N^{3/2},\quad
\ell_{h,k}=N/(1+\Lambda_{h,k}).
\]

The actual identity is

\[
D_{h,k}(R)=\sum_n a_{h,k}(n)W_{h,k}(n)e(\phi_{h,k}(n)),
\]

with the four real smooth factors and the exact square-root second difference in the frozen strategy. Every sequence is zero extended. Its ambient overlap is `[N,4N-h-k]`; integer endpoints and internal zeros are retained. The raw amplitude `W` has size one, with `W^(j)=O_j(N^(-j))`.

For a prime `p`, normalized Haar measure on `Z_p`, and nonzero `z in Z_p`, define

\[
\lambda_p(z)=\lim_{m\to\infty}p^{-m}
 \#\{(x,y)\bmod p^m:x^2+y^2\equiv z\pmod {p^m}\}.
\]

Values at zero may be assigned arbitrarily for the integrals below; the exceptional points have measure zero. Put `A=(0,h,k,h+k)` and

\[
\beta_p(h,k)=\int_{\mathbb Z_p}\prod_{a\in A}\lambda_p(x+a)\,dx.
\tag{L1}
\]

The product is over the four entries with multiplicity. For `h!=k`, define the candidate

\[
\rho^{\rm loc}_{h,k}=\pi^4\prod_p\beta_p(h,k).
\tag{L2}
\]

**Lemma A.** Formula (L2) converges for every pair of positive distinct shifts, and

\[
0\le\rho^{\rm loc}_{h,k}\ll_\eta
 |hk(h-k)(h+k)|^\eta\ll_\epsilon T^\epsilon.
\tag{L3}
\]

If one shift is odd and the other is 2 modulo 4, both `a_(h,k)` and `rho^loc_(h,k)` vanish.

**Lemma B.** For `h=k` and `p` odd with `p` not dividing `h`, writing `q=1/p`,

\[
\beta_p(h,h)=
\begin{cases}
1+q-7q^2+7q^3-2q^4,&p\equiv1\pmod4,\\
1+q-3q^2-5q^3-2q^4,&p\equiv3\pmod4.
\end{cases}
\tag{L4}
\]

For `h=k=1` the full product of these factors diverges. This assertion concerns the local product, not an established asymptotic for the repeated-shift integer sum. Regardless of any density,

\[
\frac1{LK}\sum_{1\le h<\min(L,K)}|D_{h,h}(R)|
 \ll_\epsilon T^{166/325+\epsilon}.
\tag{L5}
\]

**Conditional local input H(theta).** For every positive distinct pair, and every real `u<v` in `[N,4N-h-k]` with `v-u<=ell_(h,k)`, suppose

\[
\left|\sum_{u<n\le v}a_{h,k}(n)
   -\rho^{\rm loc}_{h,k}(v-u)\right|
 \ll_\epsilon T^\epsilon\ell_{h,k}^{\theta},
\qquad 0\le\theta\le1.
\tag{H}
\]

The constant is uniform in `T,N,h,k,u,v`. This includes all subintervals of a cell, not merely one sum per cell. Endpoints are real. Formula (H) at the required exponent is the first unproved arithmetic input, and includes the assertion that (L2) is the correct mean to its stated accuracy. The endpoint `theta=1` follows trivially from the actual divisor envelope, (L3), and `ell` bounded below by a positive power of `T`; it is too weak and does not identify a mean asymptotically. The formal local calculation does not supply a power saving in (H).

**Lemma C, conditional.** Input (H) with `theta<=45/83`, plus the inherited smooth amplitude properties, implies the frozen complete A4 estimate. With `theta=1/2`, the average absolute oscillatory remainder of the distinct-shift terms is `O(T^(159/325+epsilon))`.

## 3. Proof and derivation

### 3.1 Local norm counts, with the normalization retained

Write `chi=chi_4(p)` for odd primes. Elementary norm counting gives

\[
\lambda_p(z)=(1-\chi/p)F_p(v_p(z)),\qquad
F_p(v)=\sum_{j=0}^{v}\chi^j.
\tag{P1}
\]

For split primes, choose a square root of `-1` modulo every prime power. The invertible change `(x,y)->(x+iy,x-iy)` reduces the count to `uv=z`. If `v_p(z)=v<m`, summing the `v+1` possible valuations of the first factor gives `(v+1)(p-1)p^(m-1)` solutions. Thus `F_p(v)=v+1` and (P1) follows.

For inert primes, a norm has even valuation. A unit norm congruence has `p+1` solutions modulo `p`, each with `p` lifts at each further level. Removing a common factor `p^j` from both coordinates when `v=2j` shows that the normalized count is `1+1/p`, independent of `j`. Consequently `F_p(v)` is the indicator that `v` is even, again proving (P1).

At 2 the stabilized count is

\[
\lambda_2(z)=2\,1_{\{\text{odd part of }z\equiv1\pmod4\}}.
\tag{P2}
\]

One may verify (P2) first for odd `z`: primitive representations have one odd coordinate, and the two possible odd residue classes `1,5 mod 8` each have normalized count 2. If the norm is even, the two coordinates have the same parity; the Gaussian change dividing by `1+i` removes one factor of 2 and preserves the stabilized normalized count. Iteration proves (P2). In particular `0<=lambda_2<=2` almost everywhere and `beta_2<=16`.

These are actual congruence counts for the form `x^2+y^2`, not probabilities assigned to a surrogate coefficient. The real factor in (L2) is also normalized: the area of `x^2+y^2<=t` is `pi t`, so the real representation density per norm coordinate is `pi`. Four coordinates give `pi^4`. Combining real and local densities into an integer asymptotic remains a separate step.

### 3.2 Distinct shifts: good primes, bad primes, and an exact zero sector

Let

\[
\Delta=hk(h-k)(h+k)\ne0.
\]

For odd `p` not dividing `Delta`, the four entries of `A` are distinct modulo `p`. At most one `x+a` is divisible by `p`. If `V` has distribution `P(V=v)=(1-1/p)p^(-v)`, then

\[
\mathbb E F_p(V)=\frac1{1-\chi/p}.
\]

Decomposing `x mod p` among the four roots and their complement therefore gives exactly

\[
\begin{aligned}
\beta_p(h,k)
&=(1-\chi/p)^4
 \left[1+4\left(\frac1{1-\chi/p}-1\right)\right]\\
&=(1-\chi/p)^3(1+3\chi/p)\\
&=1-6p^{-2}+8\chi p^{-3}-3p^{-4}.
\end{aligned}
\tag{P3}
\]

Thus the good-prime product converges absolutely. Good primes cannot include `p=3` with four distinct roots; the displayed zero at that impossible configuration is not used. Every actual local factor is nonnegative by its definition.

For a bad odd prime, translation invariance and Holder give

\[
\beta_p(h,k)\le\int_{\mathbb Z_p}\lambda_p(x)^4\,dx.
\]

The latter moments are explicit:

\[
\int\lambda_p^4=
\begin{cases}
1+11/p+11/p^2+1/p^3,&\chi=1,\\
(1+1/p)^3,&\chi=-1.
\end{cases}
\tag{P4}
\]

For the first identity use `(1-q)^5 sum_(v>=0)(v+1)^4 q^v=1+11q+11q^2+q^3`. For the second use the probability `1/(1+q)` that `V` is even. Hence each bad factor is at most `1+C/p`, with an absolute `C`. For every fixed `eta>0`,

\[
\prod_{p\mid\Delta}(1+C/p)\ll_\eta |\Delta|^\eta.
\]

Indeed, outside finitely many small primes, `1+C/p<=p^eta`; the finite exceptional product is an `eta`-dependent constant. Since the shifts are `O(N)` and `N` is bounded by a fixed power of `T`, (L3) follows after choosing smaller epsilon budgets. A zero local factor simply makes the convergent product zero.

If one shift is odd and the other is 2 modulo 4, the four translates cover all four residues modulo 4. One translate is therefore 3 modulo 4, and its actual `r2` is zero. This proves `a_(h,k)(n)=0` for every integer `n`; the same residue obstruction makes `beta_2=0`. For large rectangular shift ranges this removes a positive fraction of pairs, not a power of `T`. No density saving beyond that is claimed.

### 3.3 Repeated shifts require a different local model, but their full cost is safe

When `h=k` and `p` does not divide `2h`, the three distinct roots have multiplicities `(1,2,1)`. Therefore the bracket before the common normalization `(1-chi/p)^4` is

\[
2\mathbb EF_p(V)+\mathbb EF_p(V)^2-2.
\tag{P5}
\]

For split primes, `EF=1/(1-q)` and `EF^2=(1+q)/(1-q)^2`. This gives `(1-q)^2(1+3q-2q^2)`, the first polynomial in (L4). For inert primes `F^2=F`, so (P5) is `(1-2q)/(1+q)`; multiplication by `(1+q)^4` gives the second polynomial. Both are `1+1/p+O(p^-2)`.

For `h=1`, all odd primes are good in this repeated-root calculation and their factors are positive. Also `x=8 mod 32` makes `x,x+1,x+2` have 2-adic odd parts congruent to 1 modulo 4. Consequently `beta_2(1,1)>=16/32>0`. Since `sum_p 1/p` diverges and `sum_p 1/p^2` converges, the positive partial products diverge. This proves the asserted failure of the naive constant singular product. It does **not** prove a logarithmic integer mean or rule out a suitable slowly varying density.

For the actual target there is no need to guess that mean. The divisor bound gives, uniformly on the support,

\[
|D_{h,h}(R)|\ll_\epsilon NT^\epsilon.
\]

There are fewer than `min(L,K)` repeated pairs. Hence

\[
\frac1{LK}\sum_h|D_{h,h}|\ll_\epsilon
T^\epsilon\frac{N\min(L,K)}{LK}
=T^\epsilon\frac{N}{\max(L,K)}
\le T^\epsilon\frac NK\le T^{4b+\epsilon}.
\]

This includes every repeated positive shift and all its overlap. Such a term is not a zero-phase diagonal; only its complete contribution has been bounded.

### 3.4 Conditional local transport with every restored power

The exact derivative is

\[
\phi'_{h,k}(t)=\frac{3R}{8}\int_0^h\int_0^k
(t+u+v)^{-5/2}\,dv\,du,
\]

so `|phi'|=O(Lambda/N)` on the overlap. Partition the real overlap into `O(N/ell)=O(1+Lambda)` consecutive cells of length at most `ell`. In each cell, (H) controls the error primitive from its real left endpoint to every real partial endpoint by `E=T^epsilon ell^theta`. Abel summation gives the cell contribution at most

\[
E\left(\|W\|_\infty+\int_{\rm cell}
\bigl(|W'|+2\pi|W\phi'|\bigr)dt\right)\ll E,
\]

because `ell/N<=1` and `Lambda ell/N<=1`. Real cell boundaries create no missing atoms when sums are assigned consistently as half-open intervals. Smooth exterior boundaries have zero amplitude. A possible global endpoint atom can also be handled separately with the actual divisor envelope; it costs `T^epsilon` and does not change any bound.

The distinct-shift oscillatory remainder therefore obeys, conditionally,

\[
|D_{h,k}-\rho^{\rm loc}_{h,k} I_{h,k}|
 \ll_\epsilon T^\epsilon N^\theta(1+\Lambda_{h,k})^{1-\theta},
\tag{P6}
\]

where `I` is the full smooth integral. Since `0<=theta<=1`, averaging the upper bound over the complete rectangle gives

\[
\frac1{LK}\sum_{h\ne k}|D_{h,k}-\rho^{\rm loc}_{h,k}I_{h,k}|
\ll_\epsilon T^\epsilon
N^\theta(1+TLK/N^{3/2})^{1-\theta}.
\tag{P7}
\]

The integer lengths satisfy `LK asymp N^(3/2)T^(-6b)`, including bounded cutoffs at the lower endpoint. Thus

\[
1+TLK/N^{3/2}\asymp T^{1-6b}=T^{76/325},
\]

and the worst upper-band power in (P7) is

\[
\frac{242\theta+76(1-\theta)}{325}
=\frac{76+166\theta}{325}.
\tag{P8}
\]

It is at most `166/325` precisely when `theta<=45/83`. At `theta=1/2` it is `159/325`. The smallest local scale is comparable to `NT^(-76/325)`; throughout the band it is at least a constant times `T^(90/325)`. Thus (H) asks for substantial, uniform short-interval information, not microscopic intervals. The subinterval endpoints within each such cell are nevertheless essential for Abel summation.

There is an unconditional baseline: the actual divisor envelope bounds a cell sum by `T^epsilon(ell+1)`, while (L3) bounds its candidate main term by `T^epsilon ell`. Thus (H) with `theta=1` is valid. Substitution in (P7) gives only `NT^epsilon`, exactly the trivial complete correlation bound. A positive saving in the local error is therefore the substantive missing arithmetic assertion; choosing a bounded candidate mean and partitioning do not provide it.

The nonzero candidate main terms have all their costs paid using (L3) and the inherited, directly checked smooth integral bound:

\[
|I_{h,k}|\ll_A N(1+Thk/N^{3/2})^{-A},
\]
\[
\frac1{LK}\sum_{h\ne k}|\rho^{\rm loc}_{h,k}I_{h,k}|
\ll_\epsilon T^\epsilon\frac{N^{5/2}}{TLK}
\ll_\epsilon T^\epsilon NT^{6b-1}\le T^{4b+\epsilon}.
\tag{P9}
\]

This sum includes every small product. For comparison, those with `hk<=N^(3/2)/T` can themselves be paid without a mean: their number is `O((N^(3/2)/T)log(2L))` when the cutoff is at least 1, and zero otherwise. Multiplying by `NT^epsilon/(LK)` gives the same safe bound as (P9). Removing them is optional and does not supply the discrepancy for the remaining pairs.

Combining (L5), (P7), and (P9) proves Lemma C. This argument never places a modulus inside an arithmetic `n`-sum. The triangle inequality is applied to complete local error integrals only after the hypothetical discrepancy has been stated with its full cost.

### 3.5 One primary theorem audit and its precise limits

**Source card.** Lilian Matthiesen, *Linear correlations amongst numbers represented by positive definite binary quadratic forms*, [arXiv:1106.4690v3, 19 June 2012](https://arxiv.org/pdf/1106.4690v3), Theorem 1.1, PDF pages 4--5. The functions count all integer representations. The theorem assumes primitive positive definite forms, a fixed bounded linear part, pairwise non-affinely-dependent affine forms, a convex body inside `[-M,M]^d`, and output norms in `[0,M]`. It gives a real-volume factor times prime-adic representation factors, with error `o(M^d)` and no explicit error rate. The adjacent discussion explicitly separates fixed translated one-variable correlations from the theorem's scope. Only this primary theorem was audited; no theorem from the search-result corpus is imported.

Here is the independent hypothesis and cost comparison.

For fixed `h,k`, the four affine forms in one variable are `n,n+h,n+k,n+h+k`. Every two have identical linear part and differ by a constant. They are affinely dependent. This is the **first failed hypothesis**, even for fixed, distinct, small shifts and full-length intervals. The failure is not repaired by our candidate local product.

If instead `(n,h,k)` are all variables, the coefficient vectors are

\[
(1,0,0),\ (1,1,0),\ (1,0,1),\ (1,1,1).
\]

No two are proportional. The form `x^2+y^2` is primitive positive definite and the coefficients are fixed. Intersecting the actual ranges with the overlap inequalities gives a convex body, and `M=C N` for a fixed large `C` pays both coordinate and norm ranges. Thus these geometrical hypotheses can genuinely be met, including an anisotropic box. The defect is not that every thin convex body is forbidden; it is the scale and norm of the conclusion.

An `o(N^3)` signed total error, even granted uniformly over all such bodies, becomes

\[
o\left(\frac{N^3}{LK}\right)
=o\left(N^{3/2}T^{6b}\right)
\tag{P10}
\]

after the shift normalization. The upper-band reference power of this envelope is `T^(612/325)`. A little-oh with no rate cannot be turned into `T^(166/325+epsilon)`. Even an arbitrarily fixed logarithmic saving in (P10) would not repair this power gap. Subdividing the `n`-range does not establish a better theorem: the source norm values remain of size `N`, and summing individual absolute errors pays the number of cells.

There is also an independent norm mismatch. The required quantity is a sum of moduli of full fiber sums, equivalently a supremum over arbitrary unit complex weights assigned separately to `(h,k)`. An unweighted count in a convex body does not supply those weights. Cancellation of errors after adding fibers says nothing about the sum of their absolute values. The oscillatory phase is a further weight, not one of the source's stated conclusions. These observations remain valid even if the long-box error were quantitatively improved without addressing its norm.

Finally the source's three-variable local density averages over the shift variables as well as `n`; it does not identify the one-variable density (L2) with a uniform integer mean on every fiber. Passing from one to the other is exactly part of the missing arithmetic work, not a consequence of the existence of either local integral.

## 4. First doubtful or unproved step

The first missing mathematical assertion is (H) with `theta<=45/83`, including the identification of `rho^loc` as the actual distinct-shift mean at the required local scale. Local solvability, convergence of local factors, and the elementary size bound (L3) do not prove that power-saving input. The trivial `theta=1` estimate proved above creates no improvement. No global prefix estimate has been promoted to a local one by partitioning.

For the single audited theorem, the first failed assumption on the direct fixed-shift application is pairwise non-affine dependence. Its legitimate three-variable use then has the separate absolute-norm and quantitative-error failures recorded in (P10). The theorem is not claimed false, and no statement about all literature is made.

The repeated-shift calculation rejects only a naive constant local-product formula. It proves neither the true repeated-shift mean nor an obstruction to a slowly varying mean. Repeated shifts have already been paid directly, so they are not left as an unpriced exception.

No unconditional improvement of A4 is obtained from these arguments. In particular `theta=1/2` is an arithmetic hypothesis, not a square-root heuristic used as evidence. The exact congruence zero sector yields no power saving by itself.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| `actual_four_point_coefficients` | PASS for the established lemmas. Actual `r2` and actual congruence counts are used. Factors of 4 are not lost: the norm density is for all representations, with real factor `pi^4`. The discrepancy remains OPEN. |
| `complete_shifts_overlap` | PASS. All four translated factors, ordered shift pairs, repeated positive shifts, all small products, and the full zero-extended overlap are retained or explicitly paid. |
| `local_global_discrepancy` | PASS as a distinction. (H) controls every subinterval at the local scale; a long-prefix error or one estimate per cell does not imply it with the same size. |
| `density_hypotheses` | PASS for local counts, candidate convergence, and size. OPEN for the actual integer mean. The `h=k=1` divergence is an exact control against copying the distinct-root density. |
| `real_endpoints` | PASS conditionally. All local primitives start and end at real points, half-open cell conventions retain atoms, and endpoint atoms cost `T^epsilon`. The phase estimates hold for the entire real R-window. |
| `all_restored_powers` | PASS. Repeated shifts cost at most `T^(166/325+epsilon)`; the smooth main terms have the same bound; the local remainder costs `(76+166 theta)/325`, giving threshold `45/83` and square-root exponent `159/325`. |
| `signed_absolute_distinction` | PASS. The source's total signed error is not converted to an absolute shift average. No actual lower bound is inferred from a failed positive upper certificate. The modulo-4 zero uses the actual arithmetic and need not hold for arbitrary coefficients. |
| `full_quarter_scope` | PASS. Even proving (H) in the displayed fixed-b setting supplies at most the inherited `102/325` milestone. It closes no full quarter, M1, M2, or tenth-moment obligation. |
| `statement_only_control` | NOT CLAIMED for this discovery report. No sibling or isolated packet was read. The conductor's separately isolated derivation must check the important conditional transfer. |

Additional exact controls: the inert local factor is an even-valuation indicator, not an unsigned divisor weight; the squared repeated middle factor changes the Euler tail; the modulus-4 obstruction kills the integer coefficient pointwise and its local candidate together. All are analytical. No numerical falsification was needed.

## 6. Dependencies and exact artifacts used

Read only the assigned brief, the following permitted context, and the single primary theorem cited above:

1. `protocol.md`.
2. `state/proof_obligations.yml` (authoritative status and relevant GC/M9 obligations; cited child artifacts were not opened).
3. `state/active_campaign.yml`.
4. `strategy/round212_complete_four_point_attack.md`.
5. `strategy/gauss_circle_strategy_checkpoint_round211_2026-09-28.md`.
6. `rounds/codex-managed/gc-full-source-method-review/controls/conductor_two_stage_strategy.md`.
7. `rounds/codex-managed/gc-full-source-method-review/reviews/independent_two_stage_review.md`.
8. `rounds/codex-managed/gc-complete-four-point-correlation/briefs/four_point_local_arithmetic.md`.

The exact local counts, good-prime expansion, Holder bound, repeated-root expansion, congruence-zero sector, and the local arithmetic hypothesis above are independent work in this report. The inherited material supplies the exact A4 interface, fixed masks and their derivative bounds, the reviewed diagonal normalization, and the scope of the conditional reconstruction. The local transport and all rational powers were rederived here without access to the current blind task.

The primary source was inspected through its versioned PDF, particularly its notation about fixed linear parts and variable affine constants, Theorem 1.1, local-factor definitions, and its immediate scope discussion. Search results for other papers were not used as theorem dependencies or audited. This report writes no separate source artifact because the assigned write scope is this file only.

## 7. Recommended state effect

**Retain** the local-factor lemmas, exact zero sector, repeated-shift payment, and fully costed conditional arithmetic interface as candidate evidence for seam review. **Reject** the specific direct import of Matthiesen Theorem 1.1 into fixed-shift local discrepancy, and reject the naive constant singular product on the repeated-shift sector.

**No change** to accepted analytic parents or exponents. The correct exit is `essential_local_transfer_actual_input_open`, with a scoped source obstruction and a precise remaining arithmetic statement. Do not promote (H), A4, the `102/325` milestone, any M1/M2 parent, or the full quarter target. No successor is designed. The task stops after this report.
