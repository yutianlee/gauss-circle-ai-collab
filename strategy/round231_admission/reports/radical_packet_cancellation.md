# Radical packet cancellation: prelaunch admission report

## 1. Result

Task: `radical_packet_cancellation`. Role: orthogonal arithmetic mechanism scout, nonblind. Generated: 2026-10-11T02:29:21Z. This is bounded selection work under the closed Round230 state; analytic Round231 is not launched. Starting graph SHA256: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.

**Scoped no-go lemma.** With the actual coefficients and pairwise distinct large squarefree classes, the positive certificate obtained by summing **all 4096 Fourier cosine signs at each fixed ordered norm tuple**, and only then taking a modulus, is at least a positive constant times `T^(5/2)`. Thus fixed-tuple Galois-orbit pooling, or even complete fixed-tuple sign pooling, cannot close the `T^(29/25+epsilon)` target by this certificate. This strengthens the permitted Round217 termwise-sign certificate control at exactly the indicated ordering of operations.

The proof uses actual sum-of-two-squares mass, not a random or arbitrary-coefficient model. Most of a positive six-versus-six near-resonance mass can be chosen to have no second noncomplementary signed near relation. On each surviving tuple, the balanced complementary pair has positive Fourier real part and all other cosine signs are Schwartz-small. The coefficient factorization provides no sign cancellation within this surviving pair.

This does **not** cover taking the modulus after summing harmonic tuples for a fixed tuple of squarefree classes, or after grouping different norm tuples. Both are cross-norm-tuple operations. No new complete signed upper bound or quantitative arithmetic input passing the admission gate is found.

## 2. Exact statement and hypotheses

Use precisely the fixed nonnegative radial unit-mass mollifier `rho`, its real even Schwartz transform `Psi`, and the fixed nonnegative smooth window `w` in `briefs/complete_target.md`. In particular `W=integral w>0`; `w` is not assumed even. Put

```text
a_n(T) = r2(n) n^(-3/4) Psi(sqrt(n/T)),
Q = floor(T^(2/5)),
D_T = {ordered (n_1,...,n_12): sf(n_j)>Q pairwise distinct},
A_T(n) = product_j a_(n_j)(T),
Delta_epsilon(n) = sum_j epsilon_j sqrt(n_j),
Phi_T(n) = 2^(-12) sum_(epsilon in {+1,-1}^12)
                 e(-3 sum_j epsilon_j/8) w_hat(-T Delta_epsilon(n)).
```

Every `n_j` is a positive integer and has its unique decomposition `n_j=d_j s_j^2`. There is no harmonic truncation in `D_T`. The Fourier convention is `w_hat(xi)=integral w(u)e(-u xi)du`. The exact identities are

```text
integral w(R/T) product_j cos(2pi R sqrt(n_j)-3pi/4) dR
    = T Phi_T(n),
I12(T) = T sum_(n in D_T) A_T(n) Phi_T(n).
```

The complete fixed-norm-tuple cosine certificate is

```text
C_cos(T) = sum_(n in D_T)
  |integral w(R/T) product_j [a_(n_j)(T)
                      cos(2pi R sqrt(n_j)-3pi/4)] dR|
         = T sum_(n in D_T) |A_T(n)| |Phi_T(n)|.
```

**Lemma.** There exist `c_(rho,w)>0` and `T_0(rho,w)` such that for every real `T>=T_0`,

```text
C_cos(T) >= c_(rho,w) T^(5/2).                         (1)
```

More specifically, there is an explicitly defined positive-block subcollection `G_T subset D_T` such that `Phi_T(n)>=c_w>0` on `G_T` and

```text
sum_(n in G_T) A_T(n) >= c_(rho,w) T^(3/2).            (2)
```

For each fixed norm tuple, partition its Fourier sign cube in any manner into packets `O`. The more finely grouped positive certificate

```text
C_packets(T) = T 2^(-12) sum_(n in D_T) |A_T(n)|
  sum_O |sum_(epsilon in O)
       e(-3 sum epsilon_j/8) w_hat(-T Delta_epsilon(n))|
```

satisfies `C_packets>=C_cos` by the triangle inequality. Consequently (1) applies to true Galois orbits and to any sign-packet partition **at a fixed norm tuple**. Permuting the twelve positions merely changes fixed multiplicities. The statement does not place a modulus after summing different `s` tuples for fixed `d` tuples.

## 3. Proof or derivation

### Actual support and coefficient algebra

For squarefree `d`, `r2(d s^2)=0` if any prime `3 mod 4` divides `d`. Otherwise the exact factorization is

```text
r2(d s^2) = 4 product_(p=1 mod 4)
                       (2 v_p(s)+1+1_(p|d)).          (3)
```

The prime 2 supplies no additional factor. Thus every nonzero factor in (3) is positive. Expanding `r2=4(1*chi4)` introduces divisor signs, but after summation at a fixed norm they equal the positive number (3). They supply no additional character on the Fourier sign vector. The argument below preserves the actual support and actual factorization throughout.

Choose fixed `c>0` small enough that `Psi(s)>=1/2` for `sqrt(c)<=s<=sqrt(2c)`. Set

```text
N_T = {n integer: cT<=n<=2cT, sf(n)>Q},
b_n = a_n(T) for n in N_T,
M = sum_(n in N_T) b_n,
b_max = max_(n in N_T) b_n.
```

All `b_n` are nonnegative. The elementary area comparison gives
`sum_(cT<=n<=2cT)r2(n)=pi cT+O_c(sqrt(T)+1)`, with literal real endpoints. Consequently the coefficient mass of the full positive block is comparable to `T^(1/4)`. Removing all classes `d<=Q` costs at most `C Q^(1/4)=C T^(1/10)`, by the complete class mass bound (D5)--(D6) of the permitted accepted reduction. In particular

```text
M asymp T^(1/4),    b_max <<_eta T^(-3/4+eta).         (4)
```

For each retained squarefree class let

```text
B_d = sum_(s: d s^2 in N_T) b_(d s^2).
```

There are at most `C_c sqrt(T/d)` possible `s` in a nonempty class, and that class has `d<=2cT`. The divisor bound therefore gives

```text
B_d <<_eta T^(-1/4+eta) d^(-1/2),
sum_d B_d^2 <<_eta T^(-1/2+3eta).                     (5)
```

This sums all harmonics in the block, including different harmonics in the same class. No distribution of squarefree supported integers is assumed.

### A positive six-versus-six near mass

Let `epsilon0=(+,+,+,+,+,+,-,-,-,-,-,-)`. By continuity and `W>0`, fix `delta>0` so small that

```text
Re w_hat(xi) >= 3W/4     whenever |xi|<=delta.         (6)
```

Place the product weight of every ordered six-tuple from `N_T` at its root sum. The total mass is `M^6`, and these sums lie in an interval of length `O_c(sqrt(T))`. Partition into half-open bins of width `delta/T`. The number of bins is `O_(c,delta)(T^(3/2))`. For their masses `mu_j`, Cauchy--Schwarz yields

```text
sum_j mu_j^2 >= M^12 / O(T^(3/2)) >> T^(3/2).         (7)
```

Each same-bin pair is an ordered twelve-tuple satisfying `|Delta_epsilon0|<=delta/T`. Equation (7) is a weighted lower bound before imposing distinct classes.

For a fixed repeated-class pair of positions `u,v`, leave one other position `ell` for last. Fix the same-class pair and the other nine positions. The near relation confines `sqrt(n_ell)` to an interval of length `2delta/T`; inside the block the corresponding `n_ell` interval has length `O(T^(-1/2))<1`. There is at most one integer. Dropping all remaining restrictions, the repeated-class weighted mass is at most

```text
(sum_d B_d^2) M^9 b_max <<_epsilon T^(1+epsilon).      (8)
```

The union over the 66 position pairs removes every repeated-class configuration. Therefore the set `H_T` of pairwise-distinct-class block tuples with `|Delta_epsilon0|<=delta/T` has weighted mass at least `c T^(3/2)` for all sufficiently large real `T`.

### Removing every second noncomplementary near relation

Put `K=T^(1/4)`. For each `epsilon notin {epsilon0,-epsilon0}`, remove tuples in `H_T` additionally satisfying

```text
|Delta_epsilon| <= K/T.                               (9)
```

The two rows `epsilon0,epsilon` are not proportional. Hence some two columns `i,j` form a 2-by-2 matrix with determinant `+2` or `-2`. Fix the other ten norms. The first near relation has uncertainty `O(delta/T)` and the second uncertainty `O(K/T)`. Inverting this fixed matrix confines each of `sqrt(n_i),sqrt(n_j)` to an interval of length `O(K/T)=O(T^(-3/4))`. In the block each resulting interval for the integer `n_i` or `n_j` has length

```text
O(sqrt(T) K/T) = O(T^(-1/4)) < 1.                    (10)
```

Thus at most one ordered integer pair is possible. The weighted mass for this second relation is bounded by

```text
M^10 b_max^2 <<_epsilon T^(1+epsilon).                (11)
```

This argument is valid for every unbalanced pattern as well as every other balanced pattern; no pattern is discarded by a size heuristic. Sum (11) over the other 4094 sign vectors. For any fixed `epsilon<1/2`, the result is `o(T^(3/2))`. The surviving set

```text
G_T = {n in H_T: |T Delta_epsilon(n)|>T^(1/4)
                   for every epsilon != +/-epsilon0}
```

satisfies (2). All implied constants depend only on fixed data and the chosen divisor exponent. The thresholds are inequalities at literal real `T`, not asymptotic integer substitutions.

### Sum every cosine sign before the modulus

For `epsilon0` and its negative, `sum epsilon_j=0`, so both cosine coefficients equal 1. Since `w` is real, their Fourier terms add to

```text
w_hat(-T Delta_epsilon0)+w_hat(T Delta_epsilon0)
   = 2 Re w_hat(T Delta_epsilon0) >= 3W/2.            (12)
```

Every other sign on `G_T` has `|T Delta_epsilon|>K`. Smooth compact support implies, for every fixed `A`,

```text
|w_hat(-T Delta_epsilon)| <= C_(A,w) K^(-A).
```

The total contribution of the other 4094 signs has modulus at most `4094 C_(A,w) T^(-A/4)`. The entire sign sum is real by complementary-sign pairing, even though `w` need not be even. For sufficiently large `T`, equations (12) and this remainder bound give

```text
Phi_T(n) >= W/4096 > 0       for every n in G_T.       (13)
```

Equations (2) and (13), multiplied by the physical Jacobian `T`, prove (1). As a separate aggregate cost check, `sum_(G_T) A_T<=M^12<<T^3`, so with `A=8` the far-sign contribution to the integrated selected sum is at most `O(T^(4-8/4))=O(T^2)`, below its positive `T^(5/2)` main contribution.

All full sums in the statement converge absolutely for each fixed `T`: partial summation of `sum_(n<=x)r2(n)<<x` and Schwartz decay give `sum_n|a_n(T)|<<T^(1/4)`. Hence `C_cos<=C T^4<infinity`, Fourier expansion and integration commute, and the full certificate contains the selected block as a positive subcollection. No infinite tail is dropped from the definition or estimated as a signed error.

### Legal Fourier signs versus field automorphisms

For a fixed class tuple, let `V` be the F2-span of the squareclasses of `d_1,...,d_12`, with rank `r`. The multiquadratic field has automorphism group `Hom(V,{+1,-1})`. Its image on the twelve radicals is

```text
H_d = {eta in {+1,-1}^12:
       product_(j in J) eta_j=1 whenever product_(j in J)d_j
                                                  is a square}. (14)
```

One proof chooses a squareclass basis: the `2^r` radical monomials represent distinct squareclasses, so their rational independence gives a basis; prescribing signs on the basis generators preserves multiplication and supplies exactly (14). This uses the same distinct-squarefree-root independence present in the permitted accepted reduction.

The original Fourier expansion independently chooses all 4096 signs. Its Galois orbits are the cosets of `H_d`, each of size `2^r`; one must not identify the whole cube with one orbit when multiplicative relations occur. For example the supported classes `5,13,65` force `eta_5 eta_13 eta_65=1`; simultaneous negation is then not a field automorphism. Tail-compatible examples use three pair products `pq,pr,qr` of distinct sufficiently large primes `1 mod 4`, with additional distinct supported classes. Distinct roots are linearly independent, while their squareclasses may have this multiplicative relation. The two assertions are different.

For the nonzero algebraic integer `Delta`, the norm only gives

```text
1 <= |Norm(Delta)| <= |Delta| S^(2^r-1),
S = sum_j s_j sqrt(d_j),
|Delta| >= S^(-(2^r-1)).                              (15)
```

Here `r>=4` for twelve distinct nontrivial classes and `S asymp sqrt(T)` on the control block. Even rank 4 gives only a separation of order `T^(-15/2)`, far below the physical width `1/T`. Norm nonvanishing gives neither an analytic sign relation for `w_hat` nor cancellation. The arbitrary smooth Fourier kernel is not a polynomial to which an algebraic trace identity can simply be applied. More decisively, (1) holds even after the full sign cube is pooled, so splitting it into genuine conjugate orbits cannot improve this positive certificate.

## 4. First doubtful or unproved step

No unproved analytic step is used in the scoped lemma, but its candidate status still requires independent review. The first missing step for the research target is a bound on the **signed sum across different norm tuples**, including the possibility of summing harmonic tuples before any modulus. Neither support, (3), the Galois action, nor (15) supplies that bound.

An exact way to state the missing arithmetic estimate is to define, for `0<=k<=12`,

```text
F_k(T) = sum_(n in D_T) A_T(n)
  w_hat(-T[sum_(j<=k)sqrt(n_j)-sum_(j>k)sqrt(n_j)]).
```

Ordering symmetry, with every harmonic and unequal block retained, gives

```text
I12(T) = T/4096 sum_(k=0)^12 binom(12,k) i^(k-6) F_k(T),
F_(12-k) = conjugate(F_k),
F_6 is real.                                         (16)
```

The preferred complete input is the one-sided bound

```text
sum_(k=0)^12 binom(12,k) i^(k-6) F_k(T)
                         <<_epsilon T^(4/25+epsilon). (17)
```

The left side is real. Equation (17) is an exact restatement of the remaining signed target, not a newly proved estimate or an admission candidate. It involves both within-pattern cross-tuple correlations and the correlations among different `k`; no termwise target bound is asserted. In particular the six-versus-six near pairs have coefficient `+1`, so redistributing the twelve fixed entries among the two groups cannot create an algebraic minus sign on the surviving core. Cancellation with other norm tuples remains possible and is necessary.

The selected contribution is positive at scale at least `T^(5/2)`; a target-sized total would need cancellation against its complementary signed contribution to residual `T^(29/25+epsilon)`, a difference of `67/50` in these powers. This is not a new global impossibility claim: the accepted complete `T^(10 beta+epsilon)` bound already certifies substantial cancellation unavailable to this positive certificate. The unresolved improvement over that accepted bound is only `10 beta-29/25`, with `beta` exactly as frozen in the target brief.

## 5. Required control tests and outcomes

All controls here are exact analytical derivations; no numerical experiment or external source was used.

| Control or restoration | Complete cost or outcome |
| --- | --- |
| Actual retained one-factor block mass | `M asymp T^(1/4)`; removing every small class costs `T^(1/10)` |
| Twelve-factor mass versus six-sum bins | `M^12 / T^(3/2) >> T^(3/2)` |
| All repeated-class configurations | `66 (sum B_d^2) M^9 b_max << T^(1+epsilon)` |
| Every second noncomplementary sign relation | At most 4094 copies of `M^10 b_max^2 << T^(1+epsilon)` |
| Integer uniqueness | Root interval `O(T^(-3/4))`; norm interval `O(T^(-1/4))<1` |
| Non-even physical window | Complementary balanced signs use `2 Re w_hat`; (6) gives positivity |
| Every remaining sign | Schwartz bound; aggregate integrated error `O(T^2)` with fixed decay order 8 |
| Physical Jacobian and cosine normalization | `T` and `2^(-12)` are both retained; certificate lower power `5/2` |
| Every harmonic, endpoint, unequal block and tail | Present in `C_cos`, `I12`, and (16); the positive selected block only proves a certificate lower bound |
| Galois legality | (14) enforces every multiplicative relation; all Fourier signs remain legal independently |
| Accepted complete fallback | `M12(B_T)<<T^(10 beta+epsilon)` remains unchanged |
| Restoring the finite target from a proved (17) | Head `15/13`, repeat error `8 beta-1/5`, target `29/25`; all fit the accepted twelve-only equivalence |
| Pointwise scope | The target would give `102/325`; strict pointwise gain requires `b12<13 beta-1/2`; no quarter or all-order claim |

The actual-coefficient control rejects the proposed universal saving from fixed-tuple orbit averaging. It does not substitute an unsigned model for the signed problem, and it does not claim that (1) is a lower bound for `I12`, the physical moment, or its high-value tail. In particular it does not reject a cross-harmonic estimate at fixed class tuple.

## 6. Dependencies and exact artifacts used

Only the assigned brief and the following permitted contexts were read. The graph was queried selectively for the target and relevant accepted nodes; its hash matches the frozen admission hash. No sibling report, new external theorem, or historical file beyond the exact named synthesis was used.

| Artifact | SHA256 |
| --- | --- |
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| `state/active_campaign.yml` | `fd65ce5c6b117aa4ca8ed097f85e2c786621c8054ca81791aa6e5e17006a82fa` |
| `state/proof_obligations.yml` | `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b` |
| `strategy/round231_admission/briefs/radical_packet_cancellation.md` | `47224505c6b5367bc0534ad49efe053bea3ffea22adb1c49aa3e8e4af745559c` |
| `strategy/round231_admission/briefs/complete_target.md` | `6a26238ec9bdf5b7e92cb2278234b316d1bba26ef87b9b75fc5f0a8b5561853c` |
| `proofs/kernels/gc_complete_distinct_radical_moment_reduction.md` | `d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee` |
| `proofs/kernels/gc_distinct_radical_absolute_certificate_obstruction.md` | `603aa69cb4b757707d6eb89bb8290b05190b6b6d5cae83be52ddc19658ef68bb` |
| `rounds/codex-managed/gc-complete-signed-radical-kernel/synthesis.md` | `d34cf58dd298f4d50641c5135f24bec222106129d2d827929f16eafc6b49c814` |

The accepted reduction supplies actual class bounds, absolute convergence conventions, and twelve-only restoration. The accepted Round217 kernel supplies the already validated binning and repeated-class framework, rederived here for clarity. The new additional step is removal of simultaneous nonproportional signed near relations before pooling every sign. The Round218 synthesis fixes the separate existing dual-tuple modulus obstruction; no claim is imported from its unlisted underlying reports. All work was analytical/algebraic; filesystem reads, report writing, and hashes were the only computation.

## 7. Recommended state effect

**No graph change and no analytic launch.** Retain this report as a narrowly scoped candidate obstruction, subject to independent statement-level rederivation and exact-hash review if the conductor elects to archive it as validated evidence. Do not promote the open signed target or any complete moment/pointwise improvement.

The fixed-norm-tuple sign/Galois pooling mechanism fails its stated falsifying control. Summation across different harmonic tuples at fixed class tuple, and genuine cross-tuple arithmetic cancellation in (16), remain unestimated and are not rejected. No independently checkable new signed upper-bound input with a complete improved exponent has been supplied; hence this task does not meet Round231's admission gate. The graph, proof draft, validation matrices, active campaign, legacy evidence, and all other reports remain untouched. Stop after the assigned report and its SHA256.
