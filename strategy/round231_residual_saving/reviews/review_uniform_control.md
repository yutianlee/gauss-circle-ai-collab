# Nonauthor review: exact uniform-residual obstruction

Round231 residual-saving packet; task `review_uniform_control`; 2026-10-11. Role: nonauthor arithmetic/source seam reviewer. Starting graph SHA256 `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`. Original assignment report remains frozen. This review changes no shared state.

## 1. Result and seam verdicts

**PASS** for both checked artifacts, within their stated universal-polynomial scope. No repair is required.

* Character tails and strict divisor cutoffs: **PASS**. The leading tail is `1/(2z)`, with the sign fixed by `z=1 mod4`.
* Constant-phase residual: **PASS**. Its leading coefficient is exactly `-34 H/z`.
* Cofactor Fourier density and full `r2` normalization: **PASS**. The phase `e(n/4)` leaves exactly `i H/z` to leading order.
* Every scalar-centering correction: **PASS as an obstruction**. A multiple-of-four interval annihilates the scalar contribution exactly, however large or complex the scalar is.
* Legal lengths and all endpoint errors: **PASS** for both selected interval sequences.
* Source parameter independence and `c<=3/20`: **PASS**, checked against the named primary version.
* Physical-phase scope: **PASS**. Neither artifact asserts that these phases occur among the actual quartic Taylor polynomials or that the physical radius moment has a corresponding lower bound.

The conclusions restrict a uniform exponent; they establish no positive saving at or below the cap. The source's unquantified constant is not thereby numerically determined.

## 2. Exact hypotheses and checked statements

Use the unchanged approximant from `briefs/residual_interface.md`, with `z=x^(1/20)`, the strict small-divisor cutoff `d<z`, middle range `z<=d<z^2`, logarithmic factor

    K_x(t)=(log t-2 log z)/log z,

and residual `v_x=r2-rsharp_x`. The elementary count input is `A(y)=sum_(n<=y)r2(n)=pi y+O(sqrt(y)+1)`.

The blind artifact takes `z=4k+1`, `x=z^20`, and `H=4 floor(x^(24/25)/4)`. It claims

    sum_(x<n<=x+H) v_x(n) = (-34+o(1)) H/z,
    sum_(x<n<=x+H) (v_x(n)-c)e(n/4) = (i+o(1)) H/z

for every scalar `c`, including interval-dependent complex scalars. The second formula is uniform in the scalar because its contribution vanishes identically.

The conductor takes the same starts and `H=x^(2/3)`, without requiring an integer length, and claims

    sum v_x = -34 H/z
      +O(H/z^2+sqrt(x)+H^2/x+z^2).

This is a legal sequence for each fixed `0<epsilon0<1/3` in the source window `x^(1/3+epsilon0)<=H<=x^(1-epsilon0)`. Therefore any epsilon-independent source saving constant `c` in `H x^(-c epsilon0)` must satisfy `c<=3/20`.

## 3. Independent verification

### Exact character tails and the constant -34

For integer `u=1 mod4`, the strict cutoff leaves the tail

    T(u)=sum_(d>=u)chi4(d)/d
        =integral_0^1 t^(u-1)/(1+t^2) dt.

This follows either from nonnegative paired terms or a finite geometric expansion with a vanishing integral remainder. Since

    0<=1/(1+t^2)-1/2<=1-t,

integration gives `1/(2u)<=T(u)<=1/(2u)+1/[u(u+1)]`. The middle reciprocal-divisor sum is `T(z)-T(z^2)`, not the reverse difference. Both `z` and `z^2` satisfy the required congruence.

Writing `J=integral_x^(x+H)K_x(t)dt`, exact floor counts and bounded-variation summation give a middle contribution `4J[T(z)-T(z^2)]+O(z^2)`. The first small-divisor contribution is `4H[pi/4-T(z)]+O(z)`. The small cofactor contribution at the constant phase is `O(z)` by bounded character partial sums. Subtracting from the actual count yields

    sum v_x=4H T(z)-4J[T(z)-T(z^2)]+O(sqrt(x)+z^2).

Here `K_x(x)=18` exactly, so `J=18H+O(H^2/(x log z))`. The coefficient of `H T(z)` is `4-72=-68`, and `T(z)=1/(2z)+O(z^(-2))`; hence the leading constant is `-34`. The `72H T(z^2)` term is of size `O(H/z^2)` and cannot change it.

### Exact Fourier density and the constant i

The divisor formula proves `r2(2m)=r2(m)` and `r2(n)=0` for `n=3 mod4`. Consequently the masses in residue classes `0,1,2,3 mod4` below real `y` are, respectively,

    A(y/4), A(y)-A(y/2), A(y/2)-A(y/4), 0.

Thus

    sum_(n<=y)r2(n)i^n
      =2A(y/4)-A(y/2)+i[A(y)-A(y/2)]
      =i pi y/2+O(sqrt(y)+1).

Every ordinary divisor term of `rsharp` with nonzero `chi4(d)` has odd `d`, so its `i^(dm)` sums have bounded geometric partial sums. Its middle and small contributions are respectively `O(z^2)` and `O(z)`, also with the variable logarithmic weight.

The cofactor term behaves differently. For odd `d`, direct testing of the odd classes `m=1,3 mod4` gives

    chi4(m)i^(dm)=i chi4(d) 1_(m odd).

For `d=0,2 mod4`, the expression is respectively `chi4(m)` and `-chi4(m)` and has bounded partial sums. Counting odd integers with the original real endpoints therefore gives the complete cofactor contribution

    2iH sum_(d<z)chi4(d)/d+O(z).

Subtracting it from the full density `i pi H/2` leaves `2iH T(z)=iH/z+O(H/z^2)`. This checks both the sign and the factor; incorrectly assigning the twisted cofactor term mean zero would miss the cancellation of the large density.

### Endpoints, errors, and scalar centering

The blind interval has integer start and length divisible by four, so `sum i^n=0` exactly. This establishes the assertion for every scalar with no bound on that scalar.

For its `H~x^(24/25)`, the leading size is `H/z~x^(91/100)`. Dividing the four error terms in the blind proof by this size gives respectively

    x^(-1/20),
    O(x^(-1/25)/log z),
    x^(-41/100),
    x^(-81/100),

all tending to zero. The floor in `H` costs at most four and preserves both the claimed asymptotic and the source lower length `x^(28/75)` for large starts.

For the conductor's `H=x^(2/3)`, the main exponent is `37/60`. The four error exponents are `17/30,1/2,1/3,1/10`, all strictly smaller. Its coarser `H^2/x+z^2` bound for the variable weight is valid: the multiplier perturbation is `O(H/(x log z))`, while the total absolute divisor incidence count is `O(H log z+z^2)`. Their product is absorbed by the stated error because `H<=x`. Real noninteger upper endpoints require no correction beyond the retained floor-count errors.

### Primary-source quantifier check and 3/20

I checked Matomaki--Shao--Tao--Teravainen, *Higher uniformity of arithmetic functions in short intervals I. All intervals*, [arXiv:2204.03754v4](https://arxiv.org/html/2204.03754v4), dated 28 February 2024. Theorem 1.1(iii), equation (1.7), gives a constant depending only on `k,d,D`; the implied constant may depend on epsilon. Appendix A.3 displays precisely the tested approximant, and Proposition A.3 transfers the `k=2` assertion to `r2`. The polynomial-phase specialization immediately after Theorem 1.1 includes the fixed phases used here.

For each fixed `epsilon0<1/3`, the conductor sequence forces `c epsilon0<=1/20`. Dependence of the implicit constant on that fixed epsilon does not affect this asymptotic contradiction. If `c>3/20`, choose one fixed `epsilon0<1/3` sufficiently close to `1/3` that `c epsilon0>1/20`; this is impossible. Thus no uniformity of implied constants as epsilon tends to `1/3` is needed. The permitted endpoint epsilon itself need not be used.

The statement concerns a valid constant for the transferred `r2` assertion; it does not require numerical identification with any largest possible `d2` constant. Fixed nilsequence complexity and fixed Lipschitz norm only multiply the implicit constant.

## 4. First doubtful or unproved step

No mathematical defect was found in either asserted obstruction. Their first unsupported extension would be to infer a physical circle-phase lower bound or reject a phase-specific signed estimate. The uniform theorem includes constant and rational linear phases; the actual physical Taylor family is more restricted and needs its own analysis.

Another unsupported extension would claim the endpoint saving `kappa=1/20` is attainable, or that `c=3/20` is the source's available constant. Both are upper restrictions only. Removing a nonconstant periodic correction changes the residual, and its complete payment is a separate obligation.

The complete-ceiling gate comparison is valid as a scoped certificate statement: even the universal cap `kappa<=1/20` lies below `1/4-beta`, which is about `0.12103`. It says nothing against a direct signed moment method.

## 5. Required controls and outcomes

The review repeated the tail integral, factor-four arithmetic, all four cofactor residue classes, exact full-coefficient Fourier identity, scalar geometric sum, and both sets of error exponents analytically. All pass.

The maximal source sum includes the whole interval as one permissible arithmetic progression. Hence a whole-interval lower bound is sufficient to contradict the stronger starred upper bound; no special progression transfer is assumed.

The source-quantifier control passes without taking a simultaneous limit in `x` and epsilon: select epsilon once, then let `x` grow along the legal sequence. This prevents a false requirement of uniform implied constants.

No numerical experiment was used. The review is confined to the two frozen artifacts, earlier assigned context, and the explicit primary theorem check. It does not read sibling attack or source-extraction reports.

## 6. Exact checked artifacts and dependencies

Hashes were read from disk before review and match the review brief:

* `strategy/round231_residual_saving/reports/blind_residual_control.md`: `c78fa696c881c3068541a38ae807fc1de9a58817c87c30716524e471478a2d2b`.
* `strategy/round231_residual_saving/conductor_uniform_saving_limit.md`: `ffebdca4d1e4ea8ccb1358596626a602c9c53e95226bd3f541c68913ac6187b6`.

Additional context: `protocol.md`; the prior assignment context already recorded in this task's frozen `reports/actual_residual_attack.md`; and `briefs/review_uniform_control.md`. The earlier context supplies the literal interface and accepted normalization, not the new obstruction proof.

Primary source inspected on 2026-10-11: [arXiv:2204.03754v4, Theorem 1.1 and Appendix A.3](https://arxiv.org/html/2204.03754v4). The source webpage identifies v4 as 28 February 2024. Its explicit parameter dependence and exact approximant were checked, not inferred from its abstract.

The only newly written artifact is this assigned review. Its final hash is communicated after freezing.

## 7. Recommended state effect

Retain both frozen artifacts as mathematically reviewed obstruction evidence. Reject only proposed universal bounds with `kappa>1/20` for the unchanged residual, the scalar-only repair, and a transferred epsilon-independent constant exceeding `3/20`. Do not reject physical-phase or signed-moment approaches. No complete moment, pointwise, radical, M1/M2, or quarter-theorem claim is promoted. Recommend no graph change unless the conductor separately completes all required promotion and validation steps. No successor is proposed.
