# Full harmonic pooling: actual-coefficient obstruction

## 1. Result

Task: `harmonic_pooling_discovery`. Role: arithmetic cancellation discovery, nonblind. Date: 2026-10-11. This is the user-requested bounded prelaunch admission screen; analytic Round231 is not launched. Frozen graph SHA256: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.

**Candidate scoped no-go lemma.** For the actual fixed mollifier and physical window in the target brief, there are constants `c_(rho,w)>0` and `T_0(rho,w)` such that, for every real `T>=T_0`,

```text
C_harm(T) >= c_(rho,w) T^(5/2).                         (H1)
```

Here every cosine sign and every harmonic has already been summed at each fixed ordered squarefree-label tuple before the modulus. Thus this new certificate also cannot satisfy the preferred complete `T^(29/25+epsilon)` estimate. This is a fresh argument for this ordering of operations; no inequality transfers the previous `C_cos` lower bound to `C_harm`.

The new ingredients are an actual squarefree base shell with coefficient mass `T^(1/4)`, simultaneous removal of every bounded nonproportional harmonic relation, an exact arithmetic bound that keeps all common multiples from cancelling the fundamental balanced pair, and a uniform estimate for the infinite harmonic tail. In particular, common multiples are retained and estimated as one packet, rather than being incorrectly discarded by a rank-two argument. No new signed estimate for `I12` is proved. The obstruction is to `C_harm`, not to the signed distinct-class integral or a physical moment.

## 2. Exact statement and hypotheses

Use exactly the fixed `rho`, `Psi`, `w`, `a_n(T)`, `f_d`, `Q`, `J_d`, `C_harm` and `I12` of `briefs/complete_target.md`. Write

```text
e(t) = exp(2pi i t),
w_hat(xi) = integral w(u)e(-u xi)du,
W = integral w(u)du > 0,
epsilon0 = (+1,+1,+1,+1,+1,+1,-1,-1,-1,-1,-1,-1).
```

The functions are fixed independently of `T`. The mollifier assumptions give `Psi` real, even and Schwartz, `|Psi|<=1`, and `Psi(0)=1`. The window need not be even. All ordered class tuples consist of pairwise distinct squarefree positive integers greater than `Q=floor(T^(2/5))`.

For a supported squarefree label `d` (equivalently, no prime `3 modulo 4` divides `d`), define

```text
L_d = r2(d)d^(-3/4),
g_d(s) = product_(p=1 modulo 4)
             (2v_p(s)+1+1_(p|d))/(1+1_(p|d)),
g(s) = product_(p=1 modulo 4)(2v_p(s)+1).
```

Empty products are 1. Prime 2 and primes `3 modulo 4` dividing `s` supply no factor. Then the exact harmonic coefficient is

```text
a_(d s^2)(T) = L_d g_d(s)s^(-3/2)Psi(s sqrt(d/T)),
0 < g_d(s) <= g(s) <= tau(s^2) <= tau_3(s).           (H2)
```

If an unsupported prime divides squarefree `d`, the entire class is zero. The theorem includes these zero classes without division by their coefficient.

More precisely than (H1), the proof constructs a collection `G_T` of ordered pairwise distinct supported squarefree labels `d_j in [cT,2cT]` such that, with `b_d=a_d(T)>0`,

```text
sum_(d tuple in G_T) product_j b_(d_j) >> T^(3/2),
J_d(T) >= (W/8192) T product_j b_(d_j)   on G_T       (H3)
```

for all sufficiently large real `T`. Every `J_d` in (H3) is the full, untruncated harmonic integral. The constants may depend on the fixed functions and the auxiliary fixed shell parameter `c`.

## 3. Proof or derivation

### Actual squarefree shell mass

Choose `c>0` fixed so small that `Psi(x)>=1/2` for `sqrt(c)<=x<=sqrt(2c)`. We need only the elementary weighted squarefree shell estimate

```text
sum_(cT<=d<=2cT; d squarefree) r2(d) asymp_c T.        (H4)
```

Here is a short self-contained derivation, to make the new arithmetic premise explicit. Let `h` be the multiplicative function specified by the following local formal series, all other nonconstant coefficients being zero:

```text
1 + sum_(a>=1) h(p^a)z^a =
  1-z^2                 if p=2 or p=3 modulo 4,
  1-3z^2+2z^3           if p=1 modulo 4.
```

The exact prime-factor formula for `r2` verifies coefficient by coefficient that

```text
r2(n) mu(n)^2 = sum_(m|n) h(m)r2(n/m).               (H5)
```

For every fixed `sigma>1/2`, the Euler product shows `sum_m |h(m)|m^(-sigma)<infinity`, since every nonconstant local term has degree at least 2 and bounded coefficient. The elementary disk area comparison gives `sum_(n<=x)r2(n)=pi x+O(sqrt(x)+1)` for real `x>=1`. Sum (H5), and use that comparison. Both the accumulated error and the tail in the main coefficient are `O_sigma(x^sigma)`, because

```text
sqrt(x) sum_(m<=x)|h(m)|m^(-1/2) + sum_(m<=x)|h(m)|
  + x sum_(m>x)|h(m)|/m <= C_sigma x^sigma.
```

It follows, for any fixed `1/2<sigma<1`, that

```text
sum_(d<=x; d squarefree)r2(d) = kappa x+O_sigma(x^sigma),
kappa = pi(1-2^(-2))
   product_(p=1 modulo 4)(1-3p^(-2)+2p^(-3))
   product_(p=3 modulo 4)(1-p^(-2)) > 0.              (H6)
```

The positivity follows from `1-3z^2+2z^3=(1-z)^2(1+2z)` and absolute convergence at `z=1/p`. Subtracting the two endpoint formulas proves (H4); including or excluding a single integer endpoint changes only a divisor-sized term. No prime-distribution theorem or unproved squarefree-density assertion is being used.

Let `D_T` be the squarefree labels in `[cT,2cT]` with nonzero `r2`, and put `b_d=a_d(T)`. For large enough real `T`, every label in this shell is greater than `Q`. Formula (H4), the shell size and `1/2<=Psi<=1` give

```text
M := sum_(d in D_T)b_d asymp T^(1/4),
b_max := max_(d in D_T)b_d <<_eta T^(-3/4+eta),
S2 := sum_(d in D_T)b_d^2 <= b_max M
                                      <<_eta T^(-1/2+eta). (H7)
```

### A balanced near mass with distinct squarefree labels

Fix `delta>0` so small that `Re w_hat(xi)>=3W/4` whenever `|xi|<=delta`. Place the product weight of each ordered six-tuple from `D_T` at the sum of its six square roots. These sums occupy an interval of length `O_c(sqrt(T))`. Partition the interval into half-open bins of width `delta/T`. Cauchy--Schwarz on the bin masses gives a weighted twelve-tuple mass at least

```text
M^12/O_(c,delta)(T^(3/2)) >> T^(3/2)                 (H8)
```

on tuples satisfying `|Delta0|<=delta/T`, where `Delta0=sum_j epsilon0_j sqrt(d_j)`.

To remove a fixed repeated-label pair of positions, leave a third position for last. After the other labels are fixed, its square root lies in an interval of length `2delta/T`, hence its integer label lies in an interval of length `O(T^(-1/2))<1`. There is at most one possible label. The mass with this pair repeated is therefore at most

```text
S2 M^9 b_max <<_eta T^(1+2eta).                      (H9)
```

The union over the 66 pairs is `o(T^(3/2))`, with an arbitrarily small fixed divisor exponent. This removes all repeated labels, including configurations with several repeats. No unweighted squarefree count is substituted for the actual weights.

### Remove bounded nonproportional harmonic relations

Set

```text
H=floor(T^(1/100)),    K=T^(1/4).
```

For every integer vector `k=(k_1,...,k_12)` with `1<=|k_j|<=H` which is not a scalar multiple of `epsilon0`, remove tuples from the preceding distinct near collection if

```text
|sum_j k_j sqrt(d_j)| <= K/T.                        (H10)
```

The two rows `epsilon0,k` have a nonzero 2-by-2 integer minor. Fix the other ten labels and invert the corresponding two-variable system. Since the determinant has absolute value at least 1, each remaining square root is confined to an interval of length

```text
O((H delta+K)/T)=O(T^(-3/4)).
```

On the shell this confines each integer label to an interval of length `O(T^(-1/4))<1`. There is at most one ordered label pair. For any one vector `k`, the removed weighted mass is at most `M^10 b_max^2 <<_eta T^(1+2eta)`. There are at most `(2H)^12` vectors. Thus every removal together costs

```text
O_eta(T^(28/25+2eta)) = o(T^(3/2)).                  (H11)
```

The remaining set `G_T` satisfies the first line of (H3). By construction, on it every retained bounded vector not proportional to `epsilon0` has displacement greater than `K/T`. Importantly, proportional vectors have not been removed: they are exactly `k=+h epsilon0` and `k=-h epsilon0`, with common positive harmonic `h`.

### The complete common-multiple packet cannot cancel its fundamental

For `h>=1`, (H2) gives the product coefficient bound `product_j g_(d_j)(h)<=g(h)^12`. Its required scalar tail has the following exact elementary bound:

```text
S := sum_(h>=2)g(h)^12 h^(-18) < 1/200000.            (H12)
```

Indeed, `g(2)=g(3)=g(4)=1`. For every prime `p=1 modulo 4` and every `e>=1`, `2e+1<=p^(3e/4)`: at `e=1` this follows from `3<=5^(3/4)`, and each subsequent ratio `(2e+3)/(2e+1)` is at most `5/3<5^(3/4)`. Multiplicativity gives `g(h)<=h^(3/4)`. Therefore

```text
S <= 2^(-18)+3^(-18)+4^(-18)+sum_(h>=5)h^(-9)
  <= 2^(-18)+3^(-18)+4^(-18)+5^(-9)+1/(8*5^8)
  < 1/200000.
```

The final comparison is an inequality of displayed rational numbers; no computed Euler product or numerical experiment is used. For example the first three terms are less than `382/10^8`, `3/10^9`, and `2/10^11`, respectively, while the last two sum to `832/10^9`, which already proves the strict comparison.

The exact Fourier expansion is

```text
J_d/T = 2^(-12) sum_(s_j>=1; epsilon_j=+/-1)
   [product_j a_(d_j s_j^2)(T)] e(-3 sum_j epsilon_j/8)
           w_hat(-T sum_j epsilon_j s_j sqrt(d_j)).  (H13)
```

For common harmonic `s_j=h` and signs `epsilon=+epsilon0` or `-epsilon0`, the cosine phase is exactly 1. Their pair is

```text
2 Re w_hat(T h Delta0) product_j a_(d_j h^2)(T).      (H14)
```

At `h=1`, this is at least `(3W/2) product_j b_(d_j)`. For every larger `h`, the signs of the factors `Psi(h sqrt(d_j/T))` may be arbitrary. We bound their entire signed contribution, using `|w_hat|<=W`, `|Psi|<=1`, (H2) and (H12), by

```text
2W S product_j L_(d_j)
 <= 2W 2^12 S product_j b_(d_j)
 < (W/2) product_j b_(d_j).                          (H15)
```

Here `L_d<=2b_d` follows only from the chosen fundamental shell. Consequently the complete infinite common-multiple packet, before the `2^(-12)` normalization, is at least `W product_j b_(d_j)`. No positivity, equal signs, or compact support is imposed on `Psi` at higher harmonics.

### Every nonproportional vector and infinite harmonic tail

Put `Z=sum_(s>=1)g(s)s^(-3/2)<=zeta(3/2)^3`. For the nonproportional vectors with all harmonics at most `H`, construction gives `|T Delta|>K`. The sum of the absolute coefficient products over all harmonics is at most `Z^12 product_j L_(d_j)`, and summing the `4096` signs cancels the normalization `2^(-12)` in the upper bound. Thus this part of `J_d/T` has modulus at most

```text
C_(A,w) Z^12 K^(-A) product_j L_(d_j).               (H16)
```

For the remaining nonproportional vectors, at least one harmonic is greater than `H`. The lower shell bound `d/T>=c` is decisive: for every fixed `B>0`, the Schwartz estimate gives uniformly in this shell

```text
sum_(s>H) g(s)s^(-3/2)|Psi(s sqrt(d/T))|
 <= C_(B,rho,c) H^(-B) Z.                           (H17)
```

A union over the twelve possible large harmonics, with all other harmonic sums bounded by `Z`, proves an absolute bound

```text
12W C_(B,rho,c) Z^12 H^(-B) product_j L_(d_j)        (H18)
```

for this part of `J_d/T`. In (H18) the actual sum is only over nonproportional vectors; bounding it by every vector with a large harmonic is a harmless enlargement, not double counting in the decomposition. All common multiples were already assigned to (H14)--(H15).

Take `A=8` in (H16) and `B=200` in (H17)--(H18). Since `H>=T^(1/100)/2` for large real `T`, both bounds are `O_(rho,w,c)(T^(-2) product_j b_(d_j))`. Combined with the common packet lower bound and (H13), this yields

```text
J_d/T >= (W/4096-O(T^(-2))) product_j b_(d_j)
        >= (W/8192) product_j b_(d_j)                (H19)
```

on `G_T` for sufficiently large `T`. This proves the second line of (H3). Summing (H19) over `G_T` proves (H1), with the physical Jacobian `T` retained.

As an independent complete cost check, `sum_(G_T)product b_d<=M^12<<T^3`; hence (H16) and (H18), after multiplying by `T`, have aggregate modulus `O(T^2)`, below the positive `T^(5/2)` selected mass. The exact constants can be large but are independent of real `T`.

Finally, all harmonic/class expansions and integrations above are legitimate at fixed `T`. The accepted coefficient bound and the elementary area estimate, with Schwartz decay, give `sum_n|a_n(T)|<<T^(1/4)`. Therefore the full sum of integrated absolute products is at most `TW(sum_n|a_n|)^12<<T^4`. In particular `C_harm` is finite, all rearrangements are absolutely convergent, and every other label tuple or mixed block remains in its original full definition. Only a positive subcollection of already fully pooled `J_d` is used for the lower bound.

## 4. First doubtful or unproved step

The proof above is a candidate theorem requiring independent review of its new arithmetic and pooling seams. It has no intentionally unpaid analytic term inside the scoped `C_harm` lower bound. Its first unpaid term for the research target is instead cancellation **between different fixed label tuples**.

Define the exact selected contribution `P_G(T)=sum_(d in G_T)J_d(T)` and its full complement `R_G(T)=sum_(d outside G_T)J_d(T)`, with the same ordered distinct-class domain as `I12`. Then

```text
P_G(T) >= c T^(5/2),
I12(T) = P_G(T)+R_G(T).                              (H20)
```

The preferred target requires `R_G=-P_G+O_epsilon(T^(29/25+epsilon))`, or the corresponding one-sided bound allowed by the accepted reduction. This is an exact description of the first missing signed estimate, not a newly proved mechanism. The required cancellation relative to the selected positive scale spans `5/2-29/25=67/50` in powers. The inherited complete bound already supplies cancellation down to `T^(10 beta+epsilon)`; the additional open gain over that bound is only `10 beta-29/25`.

For complete restoration, any proved bound `|I12|<<T^(b+epsilon)` enters the accepted reduction with head cost `15/13` and repeated-class cost `8 beta-1/5`. The resulting complete twelfth-moment exponent is at most

```text
max(b,15/13,8 beta-1/5).                             (H21)
```

At `b=29/25`, the head is smaller by `2/325`, and the repeated-class exponent is below `21/25`. That target would give the stated pointwise milestone `102/325`, not the quarter exponent. The present obstruction establishes none of these upper bounds. The accepted fallback remains `10 beta=1.28966351948...`; strict moment gain needs a restored exponent below `10 beta`, and strict pointwise gain needs it below `13 beta-1/2`. No sufficient family at unbounded fixed order has been derived.

## 5. Required controls and outcomes

| Control | Exact outcome |
| --- | --- |
| Actual squarefree support | (H5)--(H6) prove weighted shell mass; no assumed density of represented squarefree integers |
| Actual harmonic coefficients | (H2) retains every prime factor and explains why primes 2 and 3 modulo 4 do not contribute to the ratio |
| Fundamental shell | `M asymp T^(1/4)` and `L_d<=2b_d`; every label is greater than the literal floor `Q` eventually |
| Six-sum bin count | `O(T^(3/2))`; weighted near mass `>>T^(3/2)` |
| All repeated labels | At most 66 copies of `S2 M^9 b_max<<T^(1+epsilon)` |
| All bounded nonparallel vectors | At most `(2H)^12`, total removal `<<T^(28/25+epsilon)` |
| Two-variable completion | Integer minor at least 1; root uncertainty `O(T^(-3/4))`, norm uncertainty `O(T^(-1/4))<1` |
| Common multiples | Explicitly retained at every `h`; their entire higher-harmonic relative coefficient sum is bounded by (H12) |
| Sign-changing mollifier transform | Higher `Psi` signs are allowed freely in (H15); only the fundamental shell is positive |
| Non-even window | Complementary common signs give `2 Re w_hat`; no even-window assumption |
| All nonparallel small harmonics | Fourier decay order 8 yields relative `O(T^(-2))` |
| Every infinite harmonic tail | Smoothing decay order 200 yields relative `O(T^(-2))`, uniformly for `d/T in [c,2c]` |
| Aggregate remainder | `O(T^2)` after complete coefficient sums and the physical Jacobian |
| Full pooling order | (H19) is a lower bound for the already complete `J_d`, before its modulus |
| Full target restoration | (H21), all mixed terms through the accepted reduction, and the fixed-order limitation are retained |
| Mathematical scope | Lower bound for `C_harm` only; `I12`, its high values and the quarter target are not refuted |

All these controls are analytical or exact algebraic inequalities. There was no numerical experiment, simulation, source search, Euler-product truncation, or attempt to certify an asymptotic statement computationally. The exact display (H12) is deliberately stronger than needed; only `2^13 S<1/2` is required in (H15).

## 6. Dependencies and exact artifacts used

Only the assigned brief and its named contexts were read. The initial graph read was too long for the tool output; the relevant accepted target, reduction, complete-moment and absolute-certificate nodes were then queried selectively. No blind statement, sibling report, unlisted kernel or historical report was read. The full graph hash agrees with the frozen provenance tag.

| Artifact | SHA256 |
| --- | --- |
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| `state/proof_obligations.yml` | `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b` |
| `state/active_campaign.yml` | `fd65ce5c6b117aa4ca8ed097f85e2c786621c8054ca81791aa6e5e17006a82fa` |
| `strategy/round231_harmonic_admission/briefs/harmonic_pooling_discovery.md` | `758643e8118fcce63b46d19c20a8d01f13ba22a1b3ad497520c519e7fb0f2136` |
| `strategy/round231_harmonic_admission/briefs/complete_target.md` | `e60630a708df31a6e5baaf8ef484498e989727192394a31dc9ae2ecb0249ed34` |
| `proofs/kernels/gc_complete_distinct_radical_moment_reduction.md` | `d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee` |
| `proofs/kernels/gc_distinct_radical_absolute_certificate_obstruction.md` | `603aa69cb4b757707d6eb89bb8290b05190b6b6d5cae83be52ddc19658ef68bb` |
| `strategy/round231_admission/reports/radical_packet_cancellation.md` | `6554e39da0ae6177ecd4244859a0b9f4b4198b32c703e3a1eb32ea139bca384d` |

The accepted reduction supplies the full coefficient convergence and finite-order restoration. The prior named obstruction/report supplies the bounded near-relation framework, rederived here at squarefree fundamental labels. The squarefree convolution, arithmetic dominance of common multiples, bounded nonparallel harmonic removal and infinite-tail restoration above are the new candidate seams. No external theorem is imported.

Conductor communication disclosure: after the independent arithmetic-dominance route and its two seam statements had been sent to the conductor, the conductor requested that the proof remain minimal and offered a different fixed-cutoff, constant-sign-interval strategy. That alternative and a suggested independently checked shell lower bound were not used in this derivation. The conductor's scope instruction was followed; no other agent's proof or findings were received. All research effort was analytical/algebraic; tools were used only to read permitted files, write this assigned report and freeze its hash.

## 7. Recommended state effect

**No graph mutation and no analytic launch.** Subject to independent statement-level and final-hash review, retain (H1) as a new scoped obstruction to full harmonic pooling followed by one modulus per distinct squarefree-label tuple. Do not infer it from the earlier `C_cos` report, and do not promote any full moment, pointwise, parent obligation or quarter target.

The user-requested pooling test has a negative candidate outcome for its stronger positive certificate. It leaves signed cancellation among different label tuples open, with the precise missing term (H20) and the complete restoration costs (H21). No new quantitative signed input passes the analytic admission gate. The proof graph, draft, validation matrices, active campaign, previous admission packet and all other reports are untouched. Stop after this report and its SHA256; no successor is designed.
