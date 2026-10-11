# Round212 synthesis: actual sectors, local arithmetic and the remaining signed input

Campaign:gc-complete-four-point-correlation. Date:2026-09-28.
Conductor decision takes effect only after final-hash closure validation.
Graph SHA256:4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.

## 1. Result

The complete actual four-point upper bound remains open. This round pays
two whole sectors, derives bounded candidate local densities on distinct
shifts, proves a sharp conditional local-error transfer, and rejects an
absolute radius-Gram estimate using actual residual arithmetic mass.
No complete moment or pointwise exponent improves.

The next candidate is an actual signed estimate on the full remaining
four-point remainder, using the now-explicit bounded local product as a
model if helpful. A model can be subtracted algebraically without claiming
that it is the true mean. Any asserted small arithmetic error must still
be proved. Another unestimated partition or absolute Gram bound is not a
positive advance.

## 2. Exact complete target and paid sectors

Keep b=83/650, T^(166/325)<N<T^(242/325), every real R in I, and the
actual frozen D_(h,k), with L~N^(1/2)T^-2b, K~NT^-4b. Put
U=N^(3/2)/T and Lambda=hk/U. The full target is

    A4=(LK)^(-1)sum_(h<L,k<K)|D_(h,k)|<<T^(166/325+epsilon).

The union h=k or hk<=U is completely paid by the divisor envelope:
N/K<=T^(4b), and N U/(LK)<<N T^(6b-1)<=T^(4b), with logarithms
absorbed. The two sets need not be disjoint to prove this upper bound.
All remaining shifts form Omega={h!=k,Lambda>1}.

There is also an exact zero coefficient sector when one shift is odd
and the other is2 modulo4. It removes only a fixed proportion, not a
power. No other shift sector is discarded without a proved cost.

## 3. Mathematical findings and independent seams

For h!=k, let beta_p be the Haar average of four actual p-adic norm
representation densities at n,n+h,n+k,n+h+k. At an odd prime not
dividing Delta=hk(h-k)(h+k),

    beta_p=(1-chi4(p)/p)^3(1+3chi4(p)/p)
          =1-6/p^2+8chi4(p)/p^3-3/p^4.

Bad-prime Holder bounds use the exact fourth moment of one local density;
they yield beta_p<=1+C/p, and beta_2<=16. Thus
rho_loc=pi^4 product_p beta_p converges, is nonnegative, and is at most
T^epsilon. This is a constructed local model, not an integer asymptotic.
At h=k the good-prime expansion is instead1+1/p+O(p^-2). Its positive
product diverges at h=k=1, invalidating a naive copy of the constant
distinct-root model. That repeated sector is already paid directly.

The elementary local baseline H(1) follows from a_(h,k)<<T^epsilon
and rho_loc<<T^epsilon. A genuinely stronger local statement is missing.
If every real interval of length at most ell=N/(1+Lambda) has error
O(T^epsilon ell^theta) against rho_loc, then complete local partial
summation, with every reset boundary retained, gives remainder
N^theta(1+Lambda)^(1-theta). Averaging the full rectangle costs
T^((76+166theta)/325+epsilon). The sufficient threshold is
theta<=45/83. The hypothetical square-root case costsT^(159/325),
with7/325 margin. Its input has not been proved.

The isolated derivation establishes the more general criterion
b>=(1+eta)/(10-4nu+2eta) for local error N^eta ell^nu. Its artificial,
nonnegative countermodel fixes R0 before choosing the coefficients and
shows the criterion is sharp for that abstract input class. It is not
an r2 counterexample. Even a uniform local square-root input has only
the5/16 limiting exponent through this particular transfer; this family
does not prove quarter by taking b to zero.

The sole full external application audit is Matthiesen1106.4690v3,
Theorem1.1, counting all representations. The fixed one-variable
translated forms fail its pairwise affine-independence hypothesis.
The legitimate three-variable lift has a qualitative o(N^3) error,
not an error scaled to the short-box volume, and does not supply the
absolute fiber norm or oscillatory weights. Thin convex bodies are not
declared forbidden; the conclusion's rate and norm are insufficient.

For the alternative direct attack, product shells Omega_j with
2^j<Lambda<=2^(j+1) have fractions
delta_j<<min(1,2^j log(2L)/Lambda_*), Lambda_*=T^(76/325) up to constants.
The complete shellwise RMS input

    [mean_(Omega_j)|D_(h,k)(R)|^2]^(1/2)
                         <<T^epsilon(N/2^j+sqrt(N))

would suffice. The n=m diagonal costs onlyN^(1+epsilon); the required
one-sided signed eight-factor off-diagonal estimate is still open.

The absolute radius-Gram attempt cannot provide it. Two finite Fejer
inequalities and the elementary circle first moment prove actual absolute
four-point mass >=cLKN after both safe sectors have been removed, at each
fixed interior scale. Binning the exact radius kernel at its true phase
resolution makes its positive certificate at least
N/sqrt(Lambda_*)=N T^-38/325. It exceeds the target for
N=T^alpha with alpha>204/325. This is a lower bound on the specified
uncentered positive certificate only, even if a pointwise transfer were
granted free; it does not lower-bound the signed radius energy or A4.

Independently, the conductor proves an actual small-phase A4-sector lower
bound cN^(5/2)/(T L K) on fixed interior scales above2/3. Positive mass
and phase cosine are used together, with signed-mask zero crossings paid.
This precludes a uniform fixed power saving belowT^(4b) for that sector
across the full open band. It neither identifies a smooth main term nor
excludes moving-edge little-oh. It is consistent with the selected bound.

## 4. First unproved estimate and successor candidate

For h!=k define exactly

    R_(h,k)(R)=D_(h,k)(R)-rho_loc_(h,k) I_(h,k)(R).

This is an identity using a proved bounded model. Its full smooth main
contribution is target-safe. The complete normalized average of |R| on
Omega is therefore a concrete sufficient target for213, as is a complete
signed shell dispersion bound with all model terms paid. It does not
require calling rho_loc an established mean; a proof of local discrepancy
against it would be one stronger way to succeed.

No such arithmetic error estimate is established. The trivial H(1)
and its N-sized correlation bound remain the unconditional baseline in
this local route. Preserve the original tenth gate and all independent
M1/M2, endpoint and GAR routes. The full goal is still quarter, not one
fixed-b milestone.

## 5. Controls and validation

Three seven-section reports and a statement-only derivation are complete.
The three independent reviews check actual-sector mass/phase control,
local factors/source normalization, and the direct signed/absolute norm
distinction. The conductor separately checks the isolated transfer and
countermodel. Every verdict is bound to the final artifact hash.

Exact ceilings, real endpoints, local prefixes, number of cells, all
small products, repeated factors, mask signs, density assumptions,
positive-certificate scope and full-goal limits are explicit. Work was
analytical and source-based; no mathematical numerical experiment was
run. Finite identities were proved directly; formalizing them would not
resolve the missing arithmetic cancellation and is not substituted for it.

Closure validates frozen212 inputs, all200--211 archives, graph/campaign
schemas, the identity State Patch and replay, graph/draft bytes, the prior
ledger prefix and immutable legacy paths. Schema checks do not certify
unproved analytic estimates.

## 6. Artifacts

Reports: four_point_local_arithmetic.md, four_point_oscillatory_attack.md,
blind_local_interval_transfer.md. Conductor calculation:
controls/conductor_actual_sector_ledger.md. All are in this campaign.
The exact final-hash bindings are in
reviews/conductor_round212_reconciliation.md and the independent reviews.
The frozen strategy is strategy/round212_complete_four_point_attack.md.
Closed211 supplies the finite bridge; closed208 supplies the concrete
reconstruction and every complementary scale. Their archives are unchanged.

## 7. State effect

Identity patch only: no graph creation, update, correction or rejection;
all399 nodes and proof-draft bytes unchanged. Retain the actual controls,
local model and conditional transfer as reviewed strategy evidence.
Design213 only after closure around the complete actual signed remainder,
without repeating the invalid source import or absolute Gram closure.
Next mandatory broad strategy/current-source review214.
