# Independent review of the collision-sector ledger

## 1. Result and precise verdict

Round 232; campaign `gc-upper-tail-separated-products`; role: bounded nonauthor reviewer, following a separately completed statement-only assignment. The original blind report remains byte-for-byte frozen at SHA-256 `e377760753ee31525af78ced5b0ed488b779070b1822231bcea3fa8d5cb5d087`. The present review was explicitly authorized only after that freeze and does not alter its isolation provenance.

**PASS at the stated component and conditional-restoration scope.** The reviewed conductor candidate, SHA-256 `153228f0f23256fb7c65a8e155d5134c53b6c11ad643fef2494b3cb7fbd28085`, correctly pays the close-product sector at `T^(-3/250+epsilon)` and the distinct-product high-reciprocal-gcd sector at `T^(-9/500+epsilon)`. The real-interval count, divisor multiplicity, selected-set error, disjoint partition, and complete conditional moment restoration are valid.

The high-gcd proof requires its local product truncation to be made on the sum of absolute elementary labels, not merely on the absolute value of grouped packets. Section 3 below supplies this detail directly from the reviewed uniform Schwartz symbols. It resolves the candidate's instruction to pay the mixed tails; it is not a new unproved premise or a change of exponents. No correction of the frozen originals is required, provided the candidate is used with this explicit audit supplement.

The signed separated small-gcd sector remains unproved. Neither complete `32/25` nor any pointwise improvement follows unconditionally.

## 2. Exact statement and hypotheses reviewed

Use the literal full band F and nonnegative measure `dmu=w(R/T)dR` from the actual interface, with `R in [T/2,2T]`, `gamma=16/125`, `V0=T^gamma`, and `E={|F|>V0}`. Retain the inherited actual estimates

\[
\mu(E)\ll T^{-2\gamma+\delta},\qquad
Q_E(F)\ll T^\delta,\qquad
\|F\|_\infty\ll T^{\beta+\delta},
\]

where input losses delta can be chosen after the requested output epsilon, and

\[
\beta=\frac{50\sqrt{1717}-297}{13762},\qquad
a_*=10\beta-\frac{32}{25}>0.
\]

The reviewed all-q representation is

\[
F=G+e,\qquad \|e\|_\infty\ll T^{-1/2+\delta},\qquad
G=\sum_\alpha t_\alpha,
\]

with elementary labels `alpha=(j,h,q)`, h positive in its fixed enlarged stationary range, q any odd integer, and

\[
p(\alpha)=hq,\qquad
t_\alpha(R)=4T^{-1/2}\chi_4(q)
K_{j,h,R}\left(\frac{R^2-hq}{W_j}\right).
\]

The divisor factor four occurs once. There are `O(log^2 T)` rectangles, the kernels have every fixed Schwartz seminorm uniformly bounded, and `W_j<=W=C T^(1-2gamma)` for a fixed large C. The bounded T range is covered by constants. The original cosine branches are already represented by these real terms; no second branch is added.

The reviewed payments concern the ordered elementary-pair partition

1. `|p(alpha)-p(alpha')|<=sqrt(T)`;
2. `|p(alpha)-p(alpha')|>sqrt(T)` and `gcd(h,h')>=T^(1/4)`;
3. `|p(alpha)-p(alpha')|>sqrt(T)` and `gcd(h,h')<T^(1/4)`.

In sector 1 grouping by p is exact, with `P_p=sum_(alpha:p(alpha)=p)t_alpha`. Sectors 2 and 3 retain the elementary h labels. The first two sectors have the stated absolute bounds. A one-sided upper bound for the signed third sector at `T^(-a_*+epsilon)` is an additional, open hypothesis.

For full restoration, the separate inherited interface supplies the exact `B=L_head+F+H_high` and the two complementary twelfth-moment bounds at `32/25`. This review checks use and preservation of those owners; it does not purport to reprove their earlier accepted estimates.

## 3. Independent derivation and seam audit

**Absolute elementary envelope and both tail operations.** Define

\[
A_p(R)=\sum_{\alpha:p(\alpha)=p}|t_\alpha(R)|.
\]

It is essential that this quantity majorizes every elementary-sector product, whether or not there is cancellation within P_p. For p nonzero, each rectangle contributes at most `d(|p|)` eligible h. Uniform Schwartz decay and the elementary divisor bound give, for every fixed B and arbitrarily small delta>0,

\[
A_p(R)\ll T^{-1/2+\delta}
\left(1+\frac{|R^2-p|}{W}\right)^{-B}.
\tag{1}
\]

For unbounded or negative p this follows with the same care as in the actual-payment report: start with `d(|p|)<<_eta |p|^eta`, use

\[
|p|\ll T^2\left(1+\frac{|R^2-p|}{W_j}\right),
\]

and spend eta additional Schwartz powers before summing the rectangle logarithms. Thus (1) is not an assertion that `d(p)<<T^delta` uniformly for unbounded p. The proof of (1) uses absolute values at every step, so the actual-payment report's packet argument also proves this stronger elementary-majorant version.

The elementary lattice estimates are uniform in real `s=R^2`:

\[
\sum_p A_p\ll T^{-1/2+\delta}W,
\qquad
\sum_p A_p^2\ll T^{-1+\delta}W.
\tag{2}
\]

For the fixed exterior `p<T^2/8` or `p>8T^2`, its distance from s is at least a fixed multiple of T squared. Equation (1) therefore makes its elementary l1 tail smaller than every prescribed inverse power. Its absolute mixed products with the full wave are at most twice that tail times the first bound in (2), which has polynomial size. The full radius window has measure O(T), so this also pays the mixed products after integration, even without using the smaller measure of E.

For the second, R-dependent truncation used specifically in the high-gcd count, fix an arbitrarily small positive eta and put

\[
I_R=[R^2-T^\eta W,R^2+T^\eta W],\qquad U=2T^\eta W.
\]

The lattice tail estimate from (1) gives

\[
\sum_{p\notin I_R}A_p(R)
\ll T^{-1/2+\delta}W\,T^{-\eta(B-1)}.
\tag{3}
\]

Together with (2), the integrated absolute sum of products with at least one discarded p is at most

\[
T\cdot T^{-1+2\delta}W^2T^{-\eta(B-1)}
\ll T^{2-4\gamma+2\delta-\eta(B-1)}.
\tag{4}
\]

Given any requested inverse power, choose the fixed B sufficiently large after eta is fixed. This pays every mixed tail in every sub-sector, because the sub-sector sum is bounded by the absolute unrestricted sum. No derivative of the moving cutoff or of the indicator of E is used. In particular, no slow-test hypothesis is hidden in this step. Removing the cutoff afterward changes each restricted sector by a negligible quantity.

**Close products.** For real L>=0, every integer p has at most `2 floor(L)+1` neighbors within L. Hence

\[
\sum_{|p-p'|\le L}A_pA_{p'}
\le(2\lfloor L\rfloor+1)\sum_pA_p^2.
\]

Combining this with the full l1 square in (2) and integrating over the actual E proves

\[
\int_E\sum_{|p-p'|\le L}A_pA_{p'}\,d\mu
\ll T^{-4\gamma+\epsilon}\min(1+L,W).
\tag{5}
\]

This is even an absolute payment before internal elementary-label cancellation, and therefore also bounds the candidate's grouped-packet expression. At L=0 it is `T^(-64/125+epsilon)`. At `L=sqrt(T)`, since W has exponent `93/125>1/2`, it is

\[
T^{1/2-4\gamma+\epsilon}=T^{-3/250+\epsilon}.
\]

Cross rectangles and exact product collisions are retained; neither is treated as orthogonal. The general cutoff exponent `4gamma-a_*=224/125-10beta` is correct as the range certified by (5), without claiming it is an arithmetic obstruction to larger cutoffs.

**High reciprocal gcd and real endpoints.** Work first with the finite fixed product range and the local interval I_R. For distinct p,p', any common divisor g divides their nonzero difference. Thus `g<=|p-p'|<=U`. If `gcd(h,h')>=G0`, taking `g=gcd(h,h')` gives an actual common divisor of p,p' of size at least G0. The implication is one-way; no sector is redefined by the grouped products' gcd.

Let n_g count the integer multiples of g in the closed real interval I_R of length U. Integer spacing proves

\[
n_g\le\lfloor U/g\rfloor+1,\qquad
n_g(n_g-1)\le(U/g+1)(U/g).
\]

The latter counts ordered distinct pairs, and remains true at integer or noninteger endpoints, including n_g equal to zero or one. Summing over integers `ceil(G0)<=g<=floor(U)` gives

\[
\#\{(p,p'):p\ne p',\ \exists g\ge G_0,\ g\mid p,p'\}
\ll U^2/G_0+U\log(2+U)
\tag{6}
\]

for `1<=G0<=U`. This follows from `sum_(g>=G0)g^(-2)<<1/G0` and the harmonic-sum bound. If G0>U, the set is empty. Counting a pair once for each qualifying divisor can only enlarge this upper bound. Omitting the distinction p!=p' would invalidate the g<=U argument; the candidate correctly excludes exact products and pays them in sector 1.

Each product p in the fixed range has at most `O(log^2 T)d(p)<<T^delta` elementary labels, and each elementary term has magnitude `O(T^(-1/2))`. Thus a product pair contributes at most `T^(-1+delta)` after renaming the arbitrarily small multiplicity loss. Multiplying (6) by this factor and by `mu(E)<<T^(-2gamma+delta)` gives

\[
\ll T^{1-6\gamma+\epsilon}/G_0+T^{-4\gamma+\epsilon},
\tag{7}
\]

where the `T^(2eta)` and `T^eta` factors in U are allocated inside output epsilon. At `G0=T^(1/4)`, the first exponent is

\[
1-6\gamma-\tfrac14
=1-\tfrac{96}{125}-\tfrac14=-\tfrac9{500}.
\]

The second exponent `-64/125` is smaller. Equations (3)-(4) restore every excluded tail, so (7) applies to the original high-gcd sector, not merely the sharply localized approximation. The choice `G0=T^(1/4)` is below the common W for large T. All finite T exceptions are absorbed in constants.

**Disjoint restoration of the quadratic energy.** The three predicates in Section 2 are mutually exclusive and exhaustive for every ordered elementary pair. Grouping all of sector 1 by p is permitted because its predicate is independent of h and of j. The bound (7) enlarges sector 2 to all distinct high-gcd product pairs, including some pairs already in sector 1; this is only an upper bound for sector 2. It does not add those pairs twice to the exact partition.

Let S_3(E) denote the signed third-sector integral with all original terms restored. Absolute convergence and the two sector bounds show

\[
Q_E(G)=S_3(E)+O(T^{-3/250+\epsilon})
+O(T^{-9/500+\epsilon}).
\]

The actual error obeys

\[
\|e\|_{L^2(E)}\ll T^{-1/2-\gamma+\delta},
\]

and the accepted `Q_E(F)<<T^delta` yields

\[
|Q_E(F)-Q_E(G)|
\le2\|F\|_{L^2(E)}\|e\|_{L^2(E)}+\|e\|_{L^2(E)}^2
\ll T^{-1/2-\gamma+\epsilon}=T^{-157/250+\epsilon}.
\tag{8}
\]

The indicator remains the original full-F indicator throughout. Equations (5)-(8) establish the useful exact reduction

\[
\boxed{Q_E(F)=S_3(E)+O(T^{-3/250+\epsilon}).}
\tag{9}
\]

Thus a one-sided upper bound for S_3 suffices. Positivity of the full energy also implies `S_3(E)>=-O(T^(-3/250+epsilon))`; positivity of a truncated band is not used.

**Epsilon and complete moment ledger.** Choose positive eta sufficiently small relative to output epsilon and then all divisor, rectangle, ceiling, and distribution losses smaller still. Choose B for (4) afterward. Fixed Schwartz constants may depend on epsilon through these choices, as permitted. This order avoids an uncharged `T^eta` or a ceiling loss multiplied by ten.

The paid exponents lie below `-a_*`: `a_*<3/250<9/500`. This can be certified without trusting decimals: `sqrt(1717)<83/2` implies `beta<1778/13762<323/2500`, which is exactly `10beta-32/25<3/250`. Positivity of a_* is part of the frozen interface and also follows from an elementary lower rational bound on the same square root.

Assuming the open upper bound on S_3, equation (9) gives `Q_E(F)<<T^(-a_*+epsilon)`. The actual ceiling then pays the high twelfth moment at `10beta-a_*=32/25`. The old distribution with `q=136/13` pays low amplitudes and the threshold by

\[
\max\{1,10\gamma,1+(12-q)\gamma\}
=\max\{1,32/25,389/325\}=32/25.
\]

The generic second quadratic tail has exponent

\[
1+(2-q)\gamma=-27/325,
\]

and its high twelfth contribution has exponent `1+(20/13)beta<32/25`. Hence no second distribution tail or threshold mass is omitted. The separate L_head and full infinite H_high owners restore B by the finite L12 norm inequality. The literal F contains all of its factor modes; no additional masked remainder is silently discarded.

Finally the accepted sharp reconstruction multiplies a twelfth B moment by `T^7`, and its smoothing contribution is `O(T^(8+epsilon))`. With `Z=T^2`, a conditional B exponent `32/25` gives sharp moment exponent `(7+32/25)/2=207/50`, hence persistence exponent `207/650`. This is weaker than the accepted pointwise benchmark, as stated. Without the bound on S_3, the complete accepted moment remains at `10beta` in the normalized B variable.

## 4. First doubtful or unproved step

The first unproved step is the actual signed estimate

\[
S_3(E)\ll_\epsilon T^{-a_*+\epsilon}
\]

for separated products with small reciprocal gcd, with E selected by the complete original F. Neither the close payment nor the high-gcd divisor count supplies that estimate.

No unresolved repair remains in the reviewed component estimates after the explicit absolute-elementary local-tail argument above. The reviewed representation and complementary moment owners retain their inherited status; this review does not promote them or replace their earlier dependencies. In particular a complete-moment claim would still fail at S_3 even if all finite packet bookkeeping were accepted.

## 5. Controls and outcomes

- **All-q representation and normalization: PASS.** The Round 231 report and its independent review agree on one factor four, real phase, distinct odd Fourier labels, fixed h ranges, uniform symbols, and total stationary error.
- **Close-sector and cross rectangles: PASS.** Equation (5) pays every ordered elementary pair, including same-product cross terms; no family orthogonality is assumed.
- **High-gcd multiplicity and real interval: PASS.** Equation (6) counts ordered distinct pairs and retains the endpoint correction `U/g`. For G0>U the sector is empty. Original h labels are retained, and product gcd is used only for upper enlargement.
- **Exterior and local tails: PASS with explicit audit supplement.** Equations (1)-(4) work for the sum of absolute elementary labels and pay all mixed products, even on the full radius window. They do not rely on cancellation inside a grouped packet or smoothness of the moving cutoff.
- **Overlap-free partition: PASS.** Exact membership is disjoint; only a numerical upper bound is enlarged across sector boundaries.
- **Non-PSD control: PASS.** The three-center matrix with L=1 sends `(1,-2,1)` to `(-1,0,-1)` and has quadratic value -2. Equation (9) does not assume positive close or complementary forms.
- **Selected set and error: PASS.** The original E is kept, its weighted measure is used, and the mixed representation error has exponent `-157/250`.
- **Both tails, epsilon, and complete restoration: PASS CONDITIONALLY.** The threshold, actual ceiling, full L/H owners, infinite high-frequency tail, amplitude, Jacobian, and smoothing error are retained. Only the stated additional S_3 estimate would complete the moment gain.
- **Isolation and provenance: PASS.** This is a newly authorized nonblind review. The earlier isolated report's hash was rechecked and is unchanged. No graph, active manifest, sibling review, or unlisted historical source was read for this review. There was no numerical experiment; all checks above are analytic or exact algebraic calculations.

## 6. Dependencies and reviewed hashes

The authorized candidate and supporting files were read at the following SHA-256 values. The actual-payment report's hash matches the expressly supplied frozen hash.

| Artifact | SHA-256 |
|---|---|
| `rounds/codex-managed/gc-upper-tail-separated-products/candidates/conductor_collision_ledger.md` | `153228f0f23256fb7c65a8e155d5134c53b6c11ad643fef2494b3cb7fbd28085` |
| `rounds/codex-managed/gc-upper-tail-separated-products/briefs/actual_interface.md` | `c52e963aa8836fc7663c0528e170f4271396a907eafbee1ecc682db5d5885607` |
| `rounds/codex-managed/gc-upper-tail-separated-products/reports/actual_near_product_payment.md` | `a4943d33174f49270506dcde6fb81a58412870daeec3dcf2c2686e175985a92a` |
| `rounds/codex-managed/gc-actual-upper-tail-a/reports/signed_upper_tail_attack.md` | `ccd6592b215eecd1c38909fb088d40de2f0ea0b1916b1e568a58d54ba3c94e20` |
| `rounds/codex-managed/gc-actual-upper-tail-a/reviews/independent_signed_tail_review.md` | `dbcb1eb37c35c50e9cf69220ed235708de8252e9fde7737f79809bd6c93e8235` |
| `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md` | `942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212` |
| Earlier frozen `reports/blind_packet_band.md` in this campaign, hash rechecked only | `e377760753ee31525af78ced5b0ed488b779070b1822231bcea3fa8d5cb5d087` |

The already-read `protocol.md` hash is `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`. The graph hash `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b` is metadata inherited from the briefs, not a new graph read. An initially combined display truncated part of the historical review; that exact review was then read in full separately. No theorem was inferred from truncated output.

This review uses the accepted complete kernel for generic distribution, actual full-series reconstruction, and inherited moment scope. Its cited external sources were not newly invoked or searched; this is not a fresh audit of those already accepted theorems. The present elementary sector proofs and exact power bookkeeping are reproduced in Section 3.

The only new output is this review. Its digest is computed after the final write and returned separately. No original artifact or shared-state file was edited.

## 7. Recommended state effect

Retain the conductor collision ledger and actual-payment report as reviewed component evidence, with this review supplying the explicit absolute-elementary local-tail implementation. The close and high-gcd payments may be considered for a narrow graph entry only through the conductor's required validation and State Patch procedure.

Do not promote the open separated small-gcd estimate, complete `32/25`, a pointwise gain, or any parent target. The complete conditional implication is valid, but the substantive signed correlation remains open. No original repair, new round, or successor task is initiated. Freeze this review and stop.
