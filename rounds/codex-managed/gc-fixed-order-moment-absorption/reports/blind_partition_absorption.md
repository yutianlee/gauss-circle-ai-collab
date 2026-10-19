# Round 233: blind fixed-order partition absorption

- Campaign: `gc-fixed-order-moment-absorption`
- Task: `blind_partition_absorption`
- Role: statement-only independent rederiver
- Generated UTC: `2026-10-12T00:10:38.4329486Z`
- Graph SHA-256 supplied by the brief: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b` (not independently inspected or verified, to preserve isolation).
- Status: frozen candidate evidence; no shared state edited.
- Effort: analytical/algebraic only; no numerical experiment or external source import.

## 1. Result: proved lemma and a limitation

The proposed relative inequality is true, for every fixed even integer m >= 2 and every delta > 0. One explicit, size-independent choice is

    A_m = m! - 1,
    C_(m,delta) = A_m max{1, (A_m/delta)^((m-2)/2)}.

This constant is deliberately loose and entirely constructive. For m = 2 it equals 1, and the exact identity is E_2 = Z^2 - V.

The result extends to every absolutely summable real family. On a measure space, the negative part of E_m is bounded pointwise by C_(m,1) V^(m/2). Consequently, if J = integral V^(m/2) is finite, the signed integral I = integral E_m is well-defined in R union {+infinity}; it cannot be minus infinity. For 0 < delta < 1, a finite upper bound I <= B implies

    integral |Z|^m <= (B + C_(m,delta) J)/(1-delta).

One need not assume the moment finite before using this implication. The signed integral can genuinely be negative. The algebra supplies no small upper bound on I, and none is asserted here.

## 2. Exact statements and hypotheses

### 2.1 Pointwise algebra

Let m >= 2 be an integer, and let (x_i) be a finite family of real numbers or an absolutely summable real family. Define

    Z = sum_i x_i,
    V = sum_i x_i^2,
    P_r = sum_i x_i^r,
    E_m = sum_{i_1,...,i_m pairwise distinct} x_(i_1)...x_(i_m),

where the last sum is over ordered tuples. The infinite tuple sum is absolutely convergent. Then

    |Z^m - E_m| <= delta |Z|^m + C_(m,delta) V^(m/2)

for the constant in Section 1 and every delta > 0. Evenness is unnecessary for this absolute pointwise statement; it is necessary for identifying Z^m with the nonnegative moment |Z|^m in the signed integral conclusions below.

### 2.2 Measurable and signed integral form

Let (Omega, Sigma, mu) be a finite measure space. Let (x_i(omega)) be a fixed finite or countable family of measurable real functions such that

    S(omega) = sum_i |x_i(omega)| < infinity

almost everywhere. Define Z, V and E_m pointwise as above, with arbitrary zero definitions on any exceptional null set. Fix even m >= 2, and set

    F = V^(m/2),  J = integral F,  M = integral |Z|^m.

Suppose J < infinity. Then E_m^- is integrable, I = integral E_m is well-defined with possible value +infinity, and

    integral E_m^- <= C_(m,1) J = A_m^(m/2) J.

For every 0 < delta < 1, the extended-valued inequalities

    (1-delta) M <= I + C_(m,delta) J,
    I <= (1+delta) M + C_(m,delta) J

hold. Therefore M is finite if and only if I is finite. When they are finite,

    integral | |Z|^m - E_m | <= delta M + C_(m,delta) J,
    |M-I| <= delta M + C_(m,delta) J,
    (I - C_(m,delta) J)/(1+delta) <= M
        <= (I + C_(m,delta) J)/(1-delta).

The lower bound may be negative and then is merely weaker than M >= 0. No replacement of I by a nonnegative quantity is needed for the upper bound. If I <= B is supplied independently, then M <= (B + C J)/(1-delta); actual hypotheses necessarily make that numerator nonnegative.

These statements only require pointwise absolute summability and J < infinity, followed by a finite bound on I if a finite bound on M is desired. Stronger domination assumptions sufficient to pass integrals directly through finite truncations are specified in Section 3.5.

## 3. Proof and derivation

### 3.1 Exact finite partition identity

For a finite index family, sum over permutations sigma of {1,...,m}:

    E_m = sum_{sigma in S_m} sign(sigma)
              product_{cycles B of sigma} P_(|B|).

To verify this without importing a partition-inversion theorem, expand the product of power sums. Fix an ordered index tuple (i_1,...,i_m). Its coefficient in the displayed expression is the sum of sign(sigma) over permutations sigma preserving the tuple: i_(sigma(k)) = i_k for every k. Partition the positions into blocks on which the index is equal. The preserving permutations form the product of the permutation groups on these equality blocks. Thus the coefficient factors as the product, over the equality blocks of sizes b, of

    sum_{tau in S_b} sign(tau).

For b = 1 this sum is 1. For b >= 2, composition with a fixed transposition pairs every permutation with one of opposite sign, so the sum is 0. Hence the coefficient is 1 precisely for pairwise distinct indices and otherwise is 0. This proves the identity, including the ordered-tuple normalization.

Grouping permutations by their sets of cycles gives the equivalent set-partition identity

    E_m = sum_{pi partition of {1,...,m}}
             (-1)^(m-|pi|) [product_{B in pi} (|B|-1)!]
             [product_{B in pi} P_(|B|)].

Indeed, a block of size b supports exactly (b-1)! cycles, each of sign (-1)^(b-1). The all-singleton partition is exactly Z^m; every other partition has at most m-2 singletons.

### 3.2 Bounding every repeated-index term

Assume V > 0. For r >= 2,

    |P_r| <= sum_i |x_i|^r
           <= (max_i |x_i|)^(r-2) sum_i |x_i|^2
           <= V^(r/2).

The same bound follows using a supremum in place of the maximum. A permutation with s fixed points therefore contributes in absolute value at most

    |Z|^s V^((m-s)/2).

Let D_n be the number of permutations of n elements having no fixed point, with D_0 = 1 and D_1 = 0. The number of permutations of m elements having exactly s fixed points is

    a_(m,s) = binom(m,s) D_(m-s).

This is constructive; if desired D_n = n! sum_{k=0}^n (-1)^k/k!, by elementary inclusion-exclusion. Subtracting the identity permutation and taking absolute values gives the sharper intermediate inequality

    |Z^m-E_m| <= sum_{s=0}^{m-2} a_(m,s) |Z|^s V^((m-s)/2).  (1)

The coefficients are nonnegative and their sum is A_m = m!-1. Put t = |Z|/sqrt(V). Since every exponent s is between 0 and m-2,

    V^(-m/2) |Z^m-E_m|
        <= A_m max{1,t^(m-2)}.                              (2)

Here t^0 is 1, including when t = 0. If V = 0, every x_i is zero and the target inequality holds directly.

### 3.3 Explicit relative absorption

Set

    R = max{1,sqrt(A_m/delta)}.

For 0 <= t <= R, the right side of (2) is at most

    A_m R^(m-2) = C_(m,delta).

For t >= R, it is at most A_m t^(m-2) <= delta t^m. Thus in either region

    A_m max{1,t^(m-2)} <= delta t^m + C_(m,delta).

Multiplication by V^(m/2) proves the claimed inequality. The argument uses no positivity of x_i and has no dependence on the number of indices. For m = 2 the same calculation is valid with exponent zero and C = 1.

### 3.4 Absolutely summable passage

For a countable absolutely summable family, let S = sum_i |x_i| and use the first N terms. Then Z_N tends to Z, V_N tends increasingly to V, and the infinite ordered tuple sum defining E_m converges absolutely because

    sum_{ordered distinct tuples} |x_(i_1)...x_(i_m)| <= S^m.

In fact, writing S_tail,N = sum_{i>N} |x_i|, a union bound over the position of an index outside the first N gives

    |E_m-E_(m,N)| <= m S^(m-1) S_tail,N,

with the zero-family case interpreted separately. This tends to zero. The finite inequality has a constant independent of N, so its ordinary pointwise limit proves the infinite inequality. Absolute convergence makes the result independent of the enumeration. An absolutely summable family over an arbitrary index set has at most countably many nonzero terms, so the same pointwise conclusion applies to it after restricting to that support. The measurable statement deliberately assumes a fixed finite or countable index set.

### 3.5 Integration, negative parts, and domination

The aggregates Z, V and E_m in Section 2.2 are measurable as pointwise limits of measurable finite sums. Since m is even, the pointwise result at delta = 1 gives

    E_m >= -C_(m,1) F,
    E_m^- <= C_(m,1) F.

Thus J < infinity guarantees an integrable negative part even when M has not yet been shown finite. In particular I is unambiguous and never minus infinity.

For 0 < delta < 1, the relative inequality gives the two pointwise inequalities

    (1-delta)|Z|^m <= E_m + C_(m,delta) F,
    E_m <= (1+delta)|Z|^m + C_(m,delta) F.

The right side of the first one is nonnegative pointwise. Integrating is legitimate in the extended sense because E_m^- and F are integrable; it yields precisely the two extended integral inequalities in Section 2.2. If I has a finite upper bound, the first proves M finite. Conversely M finite implies E_m is integrable, using the pointwise absolute remainder bound and J finite. Once both are finite, integrating the absolute remainder and applying the triangle inequality proves all the finite comparisons.

This proof applies the already established infinite pointwise inequality directly. It does not silently interchange an infinite tuple sum and a signed integral.

For a direct dominated-convergence passage from finite truncations, the simple sufficient condition is S^m in L^1. Indeed,

    |Z_N|^m <= S^m,  |E_(m,N)| <= S^m,
    V_N^(m/2) <= S^m.

A more flexible sufficient condition is J < infinity together with a measurable D such that D^m is integrable and |Z_N| <= D for every N almost everywhere. Applying the finite relative bound at delta = 1 gives

    |E_(m,N)| <= 2D^m + C_(m,1) F,

an integrable dominator. These conditions justify convergence of all three integrals. Pointwise absolute summability alone is not being claimed to justify exchanging signed integrals with limits.

## 4. First doubtful or unproved step

There is no unproved step in the finite identity, the relative absorption inequality, its pointwise absolutely summable extension, or the signed integral consequences under the stated hypotheses.

For an application, the first additional unproved step is an independent, suitably uniform upper bound on the actual signed quantity I = integral E_m. The present statement supplies none. One must also verify the application's real-valued measurable family, absolute summability or another justified limiting construction, and the required J estimate. If the application passes through finite truncations, the needed domination or convergence must be checked separately.

There is no coefficient-specific cancellation here: the argument works for positive, unsigned, and adversarial real sequences as well. It therefore cannot, by itself, establish any special cancellation estimate that would fail for those controls. The theorem is a fixed-order algebraic reduction, not a bound on the remaining signed distinct-index integral and not an asymptotic theorem.

## 5. Required controls and outcomes

All controls below are exact analytical calculations; none is a numerical experiment.

### 5.1 `finite_partition_identity`: PASS

The coefficient argument in Section 3.1 is an exact check for every finite index tuple. Low-order normalizations are

    E_2 = Z^2 - V,
    E_4 = Z^4 - 6Z^2 V + 3V^2 + 8Z P_3 - 6P_4.

For m = 4, permutations grouped by their number of fixed points give the bound (1) with coefficients 6, 8 and 9 for s = 2, 1 and 0 respectively; they sum to 23 = 4!-1. This checks the ordered-tuple factorial and cycle coefficients.

### 5.2 `relative_absorption`: PASS, with fixed-order limitation

- Zero family: V = Z = E_m = 0; both sides vanish.
- Fewer than m indices: E_m = 0. For n < m indices, Cauchy-Schwarz gives |Z|^m <= n^(m/2) V^(m/2). Thus no contradiction occurs; for delta < 1 equal nonzero values show that any valid constant must be at least (1-delta)n^(m/2).
- Equal positive values: with N >= m and x_i = a > 0, Z = Na, V = Na^2 and E_m = (N)_m a^m, where (N)_m = N(N-1)...(N-m+1). For fixed m,

      |Z^m-E_m|/|Z|^m
          = 1-product_{j=0}^{m-1}(1-j/N)
          = binom(m,2)/N + O_m(N^(-2)).

  This agrees with absorption when t = sqrt(N) is large. For every fixed m > 2, setting delta = 0 would fail: |Z^m-E_m|/V^(m/2) grows like binom(m,2) N^(m/2-1). The small relative term is substantively necessary at higher orders.
- Opposite signs: for (a,-a), Z = 0 and V = 2a^2. At m = 2, E_2 = -2a^2 = -V, and C = 1 is exact. For m >= 4 this two-element family has E_m = 0. More general mixed-sign families are covered without alteration because each P_r was bounded in absolute value.
- m = 2: the remainder is exactly V. Integrating gives I = M-J, including the possibility I < 0.
- Large |Z|/sqrt(V): for t >= 1, (2) gives |Z^m-E_m|/|Z|^m <= A_m/t^2. In particular the error is at most delta |Z|^m whenever t >= max{1,sqrt(A_m/delta)}.
- Fixed m versus growing m: the constants are not uniform in m. With N = m-1 equal unit entries and 0 < delta < 1, E_m = 0 forces

      C_(m,delta) >= (1-delta)(m-1)^(m/2).

  This diverges along even m. Thus a statement with m increasing with another parameter requires explicit accounting for its constants; the fixed-order result does not authorize a uniform-order inference.

### 5.3 `signed_integral_negative_part`: PASS

On a one-point probability space, take exactly m values, m-1 equal to a > 0 and one equal to -a. For every even m,

    E_m = -m! a^m,
    Z = (m-2)a,
    V = ma^2.

Hence the signed integral I is strictly negative; for m >= 4 the moment M is nevertheless strictly positive. This refutes any unjustified assertion that I must be nonnegative. It is consistent with E_m^- <= C_(m,1) V^(m/2), and the integrated comparison retains I with its actual sign.

A separate adversarial positive control shows what remains missing. On the same one-point space, take N equal unit entries. Then

    I/J = (N)_m/N^(m/2) ~ N^(m/2)

as N tends to infinity at fixed m. Thus no size-independent upper bound I <= constant_m J follows from the hypotheses. The relative absorption inequality does not conceal such a bound.

### 5.4 `blind_isolation`: PASS

Only protocol.md, this task's brief, and isolated_absorption.md were read. No graph, active campaign manifest, actual application, history, sibling report, or prior derivation was inspected. The graph hash above is provenance supplied by the brief, not a claim of independent graph verification. No external literature or computational experiment was used. Only this assigned report was written, and the task ends upon its freeze and hash return.

## 6. Dependencies and exact artifacts used

The mathematical proof is self-contained: finite expansion, parity-pairing cancellation, elementary power-sum bounds, absolute convergence, and basic integration of nonnegative functions. No external theorem/source card or arithmetic property is imported.

Exact context file SHA-256 values, computed from the bytes actually read:

| Context artifact | SHA-256 |
| --- | --- |
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| `rounds/codex-managed/gc-fixed-order-moment-absorption/briefs/blind_partition_absorption.md` | `c34aaeeaf7f25d8ee5fe1cf83fe149ed98e6226c30b3a1fe3fac11ce4b82ec63` |
| `rounds/codex-managed/gc-fixed-order-moment-absorption/briefs/isolated_absorption.md` | `bcc451ae8c29d9a8c5623b90a6d8fb84c99eb98543189de8c2fdebe93c851422` |

Written artifact: `rounds/codex-managed/gc-fixed-order-moment-absorption/reports/blind_partition_absorption.md`, explicitly encoded as UTF-8 without BOM. The final byte hash is returned to the conductor outside this file, to avoid self-reference.

Limitations: constants are loose, fixed-order dependence is substantial, the signed integral estimate remains an independent application obligation, and no source/application or shared-state validity audit was within this isolated task.

## 7. Recommended state effect

Recommend promotion, after the conductor's independent seam review and state validation, of only the narrow finite/summable relative-absorption lemma and the signed integral implication with their exact hypotheses. Retain every application-dependent signed integral estimate and parent target as unresolved unless separately established. Do not promote a uniform-in-m statement. No authoritative graph, proof draft, validation matrix, or synthesis was edited by this task. No successor round is proposed or started.