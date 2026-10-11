# Actual quadratic twists: a proved divisor estimate and its restored completion cost

Round231 prelaunch admission task `quadratic_remainder_attack`; claimant/deriver; 2026-10-11. Frozen graph SHA256 `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`. The authoritative manifest remains closed Round230. This report is evidence only.

## 1. Result

Quadratic demodulation genuinely changes the local geometry: the bounded-residual length is

\[
 H=c\min(N,N^{5/6}T^{-1/3}).                                      \tag{1}
\]

At the former obstructing shell `N~T^(2/3)`, this is `H~T^(2/9)`, so the former singleton proof no longer applies. The new singleton scale is `N~T^(2/5)`, with absolute-patch certificate floor `T^(1/10)`, below the desired `T^(13/125)`. This smaller shell can be included in the paid norm head.

A genuine signed estimate for the actual arithmetic coefficients is proved here, rather than assumed. If `I` is any half-open interval in `(N,2N]`, of real length at most `H`, `q` is odd, `(a,q)=1`, and `lambda` is any real number, then

\[
 \boxed{\left|\sum_{n\in I}r_2(n)e(an^2/q+\lambda n)\right|
 \ll \tau(q)\log^2(2Nq)
       \left({H\over\sqrt q}+\sqrt{Nq}\right).}                 \tag{2}
\]

It may also be capped by `O_eta((H+1)N^eta)`. The proof uses the actual divisor convolution, the periodic signs of `chi4`, exact hyperbola ownership, and elementary quadratic Gauss completion, including every shortened fibre. It proves nontrivial cancellation in sufficiently long intervals for suitable conductors.

However, on every quadratic Taylor patch with `N<=T`, one has `H<=c sqrt(N)`. The completion term `sqrt(Nq)` in (2) then exceeds the trivial length, for every `q>=1`. Thus this actual signed estimate supplies no improved bound in those central shells. Ordinary norm-lattice rational means have an even larger boundary cost. No complete moment improvement has been obtained: the best rigorously available complete result remains

\[
 M_{12}(B_T)\ll_\epsilon T^{10\beta+\epsilon},\qquad
 10\beta=1.28966351948\ldots,                                  \tag{3}
\]

inherited from the accepted kernel, with all its source qualifications. The new estimate is useful diagnostic evidence, not a successful admission input.

## 2. Exact statements and hypotheses

Use exactly the fixed `rho,Psi,w`, real `T>=2`, and actual `B_T` of the assigned complete interface; `R` ranges over `[T/2,2T]`. Let `e(t)=exp(2pi i t)`, `f_R(x)=R sqrt(x)`, and

\[
 F(x)=x^{-3/4}\Psi(\sqrt{x/T})e(f_R(x)).
\]

The analysis below is uniform for `N>=2`; the initial bounded shell and singleton are retained separately. Partition a norm shell, including any lower-cutoff restriction, into real half-open intervals `I_j=(l_j,u_j]` of length at most (1). Take `x_j=(l_j+u_j)/2` and

\[
 \alpha_j={R\over2\sqrt{x_j}},\qquad
 \beta_j=-{R\over8x_j^{3/2}}.
\]

Choose a power of three `q=3^k` satisfying

\[
 \max(3,H^2)\le q<3\max(3,H^2).
\]

Choose an integer `a_j` not divisible by three with

\[
 |\beta_j-a_j/q|\le {3\over2q},
\]

and then an integer `b_j` with

\[
 |\alpha_j-2a_jx_j/q-b_j/q|\le {1\over2q}.
\]

The first choice follows by rounding `q beta_j` and, if necessary, moving by one. Thus `(a_j,q)=1` is enforced; a rounded nonprimitive numerator is never silently treated as primitive. Put

\[
 P_j(x)=(a_jx^2+b_jx)/q,\quad
 g_j(x)=x^{-3/4}\Psi(\sqrt{x/T})e(f_R(x)-P_j(x)),
\]

\[
 U_j=\sup_{l_j\le y\le u_j}
 \left|\sum_{l_j<n\le y}r_2(n)e(P_j(n))\right|,
 \qquad \mathcal A_N^{(2)}=N^{-3/4}\sum_j U_j.
\]

For every fixed `L`,

\[
 \left|\sum_{n\text{ in the shell}}r_2(n)F(n)\right|
 \ll_L (1+N/T)^{-L}\mathcal A_N^{(2)}.                          \tag{4}
\]

Neither (4) nor (2) asserts cancellation between patches. The fully signed main/remainder identity in Section3 retains that possible cancellation exactly. No arbitrary coefficient mask is granted the actual full-wave supremum.

## 3. Proof, actual arithmetic attack, and complete restoration

### Exact residual and endpoints

Taylor's theorem applied to the derivative, with `f_R'''(x)=3R/(8x^(5/2))`, gives throughout a patch

\[
 (f_R-P_j)'(x)
 =O(T H^2N^{-5/2})+2(\beta_j-a_j/q)(x-x_j)
       +(\alpha_j-2a_jx_j/q-b_j/q).
\]

Consequently

\[
 \int_{I_j}|(f_R-P_j)'(x)|dx
 \ll T H^3N^{-5/2}+H^2/q+H/q\ll1.                             \tag{5}
\]

This bounds the exact residual; no Taylor term has been discarded. It remains valid when `H<1`, since `q>=3`, and for every last partial patch. Derivatives of the fixed Schwartz amplitude give

\[
 |g_j(u_j)|+\int_{I_j}|g_j'(x)|dx
 \ll_L N^{-3/4}(1+N/T)^{-L}.
\]

Abel summation with the partial sum starting at `l_j` proves (4). Real endpoints are literal; the atom at an integer upper endpoint belongs to that interval once. Projection by `Re(e(-3/8) .)` yields the original cosine without additional arithmetic assumptions.

### Elementary completion, including a real linear coefficient

For odd `Q`, `(A,Q)=1`, and arbitrary real `mu`, the finite Fourier expansion of `e(A t^2/Q)` has all coefficient moduli `Q^(-1/2)`. Indeed the square of the complete Gauss modulus is `Q`, by putting the two summation variables into difference/sum coordinates, an invertible substitution because `Q` is odd. The geometric-sum estimate therefore gives, on an integer interval of real length `L0`,

\[
 \left|\sum e(A t^2/Q+\mu t)\right|
 \ll {L_0\over\sqrt Q}+\sqrt Q\log(2Q).                       \tag{6}
\]

To check uniformity in `mu`, the `Q` frequencies `mu+h/Q` are spaced by `1/Q` modulo one. At most one closest term costs `O(L0+1)`; summing the reciprocal distances of the rest costs `O(Q log(2Q))`. Multiplication by `Q^(-1/2)` proves (6), including empty and singleton intervals. For `Q=1` use the trivial `L0+1` bound. This proof imports no exponent-pair or higher-degree theorem.

### Divisor hyperbola with all short fibres owned

Write `r2(n)=4 sum_(dm=n) chi4(d)` and set `D=floor(sqrt(2N))`. Every pair `dm=n<=2N` belongs to exactly one of

\[
 d\le D;\qquad m\le D,\ d>D.                                  \tag{7}
\]

Thus the sum in (2), divided by four, is exactly

\[
 \sum_{d\le D}\chi_4(d)
   \sum_{l/d<m\le u/d}e(ad^2m^2/q+\lambda dm)
 +\sum_{m\le D}
   \sum_{\max(D,l/m)<d\le u/m}
           \chi_4(d)e(am^2d^2/q+\lambda md).                  \tag{8}
\]

Here `I=(l,u]`; when the lower endpoint is at least the upper endpoint the fibre is empty. There is no rectangular completion or silently omitted diagonal in (8).

For the first inner sum, reduce the quadratic conductor to

\[
 q_d={q\over\gcd(d^2,q)}.
\]

Its numerator after cancellation is coprime to `q_d`. Estimate (6), with its arbitrary real linear coefficient, bounds this fibre by

\[
 C\left({H\over d\sqrt{q_d}}+\sqrt{q_d}\log(2q_d)\right).
\]

For the second inner sum split `d` into its four residue classes modulo four. The nonzero character values are constants on these classes. Writing `d=r+4t` multiplies the quadratic coefficient by sixteen. Since `q` is odd, the reduced conductor is still `q_m=q/gcd(m^2,q)`; each resulting interval has length at most `H/(4m)`. Summing the four applications of (6) gives the same displayed bound with `d` replaced by `m`, up to a fixed factor. This step genuinely uses the specified arithmetic weight; it is not a theorem for arbitrary bounded weights.

For either outer variable,

\[
 \sum_{d\le D}{1\over d\sqrt{q_d}}
 ={1\over\sqrt q}\sum_{d\le D}{\sqrt{\gcd(d^2,q)}\over d}
 \le {1\over\sqrt q}\sum_{d\le D}{\gcd(d,q)\over d}
 \ll {\tau(q)\log(2D)\over\sqrt q}.                            \tag{9}
\]

The last inequality follows from `gcd(d,q)=sum_(r|d,r|q) phi(r)` and `phi(r)/r<=1`. Also `sum_(d<=D) sqrt(q_d) <=D sqrt(q)`. Summing (8) proves (2). Directly counting its original `n`-atoms and using `r2(n)<<_eta N^eta` gives the independent cap `(H+1)N^eta`; one must take the smaller bound rather than interpret the completion loss as an actual large value.

### Rational means stay with their errors

For a rational polynomial `P(n)=(a n^2+b n)/q`, define

\[
 C_q(v)=\#\{(s,t)\bmod q:s^2+t^2=v\bmod q\},
\]

\[
 K(a,b;q)=q^{-2}\sum_{v\bmod q}C_q(v)e((av^2+bv)/q),
\]

\[
 E_P(x)=\sum_{1\le n\le x}r_2(n)e(P(n))-\pi K(a,b;q)x.
\]

Translated-lattice square comparison, summed over all vector residues, gives

\[
 |E_P(x)|\ll q\sqrt x+q^2.                                    \tag{10}
\]

The origin correction is included in this bound. This is a signed identity with an unsigned error estimate, not an inference from a density model.

For odd `q`, `(a,q)=1`, the quadratic mean itself has the useful bound

\[
 |K(a,b;q)|\le {\tau(q)\over\sqrt q}.                           \tag{11}
\]

Here is a direct proof retaining its phase. Expand `e((av^2+bv)/q)=sum_h c_h e(hv/q)`; the preceding Gauss argument gives `|c_h|=q^(-1/2)`. The additive norm mean is the algebraic square `G(h,q)^2/q^2`, where `G(h,q)=sum_s e(hs^2/q)`. Difference/sum coordinates give `|G(h,q)|^2=q gcd(h,q)`. Therefore

\[
 |K|\le q^{-1/2}\sum_{h\bmod q}{\gcd(h,q)\over q}
 =q^{-1/2}\sum_{m\mid q}{\varphi(m)\over m}
 \le q^{-1/2}\tau(q).
\]

No absolute square replaces `G(h,q)^2` in the identity; only the displayed bound takes moduli.

The exact patch formula is

\[
 \sum_{n\in I_j}r_2(n)F(n)
 =\pi K(a_j,b_j;q)\int_{I_j}g_j(x)dx
           +\int_{I_j}g_j(x)\,dE_{P_j}(x).                   \tag{12}
\]

For the second term put `E_j(y)=E_(P_j)(y)-E_(P_j)(l_j)`. It equals `g_j(u_j)E_j(u_j)-integral E_j(x)g_j'(x)dx`. Thus every endpoint and actual signed arithmetic error remains. The complete joint sum of (12), followed by the real cosine projection, is exact. Its separate rational mains do not equal the canceled full area transform: both the polynomial and the demodulated multiplier change with the patch. Estimate (2) bounds the whole left side, automatically paying main and error together; using (11) alone would leave (10) unpaid.

For example (10), (11), and (5) provide the separate upper cost

\[
 N^{-3/4}(1+N/T)^{-L}
 \left(H\tau(q)/\sqrt q+q\sqrt N+q^2\right)
\]

per patch. The divisor method (2) improves the latter completion scale from `q sqrt(N)+q^2` to essentially `sqrt(Nq)`, but does not make it smaller than the short-patch mass in the needed range.

### Restoration of the tested estimates

There are `O(N/H+1)` patches. For `H>=1`, applying (2) in (4) gives, with harmless divisor/logarithmic factors displayed as `T^epsilon` when all parameters have the stated polynomial bounds,

\[
 \left|\sum_{N<n\le2N}r_2(n)F(n)\right|
 \ll_{L,\epsilon}(1+N/T)^{-L}T^\epsilon
 \left({N^{1/4}\over\sqrt q}
             +{N^{3/4}\sqrt q\over H}\right).                \tag{13}
\]

For `N<=T`, (1) gives `H<=c sqrt(N)`, so the second term in this available upper bound is at least `c^(-1)N^(1/4)`. This is a statement about the size of the proved upper bound, not a lower bound on the signed shell. Even a magically favorable rational approximant of any conductor cannot make (13), by itself, beat the trivial shell mass there. With the explicit `q~max(1,H^2)`, the loss is larger still. The bound must therefore be capped by

\[
 \sum_{N<n\le2N}r_2(n)n^{-3/4}|\Psi(\sqrt{n/T})|
 \ll_L N^{1/4}(1+N/T)^{-L},                                 \tag{14}
\]

which follows from the elementary area bound. This pays small patches more sharply than summing `(H+1)N^eta` separately.

Summing all shells up to `Z=T^(3/2)` and (14) gives only the elementary complete ceiling `O(T^(1/4))`; the important shell `N~T` is still present. By the accepted complete distribution, that ceiling would give only

\[
 M_{12}(B_T)\ll_\epsilon T^\epsilon
       (T+T^{5/2}+T^{18/13}),                               \tag{15}
\]

which is weaker than (3). The actual inherited ceiling `T^(beta+epsilon)` and accepted distribution give instead

\[
 M_{12}(B_T)\ll T^\epsilon
       (T+T^{10\beta}+T^{1+20\beta/13})
       \ll T^{10\beta+\epsilon};                           \tag{16}
\]

the domination uses the accepted inequality `beta(136/13-2)>1`. These are full real-wave statements, with no claimed complex-wave analogue of the inherited supremum.

For a norm head `n<=X`, its coefficient mass is `O(X^(1/4))` and the accepted finite masked-distribution proof gives

\[
 M_{12}(H_X)\ll_\epsilon T^\epsilon
              (T+X^{5/2}+TX^{5/13}).                        \tag{17}
\]

At `X=T^(52/125)` this is `O(T^(29/25+epsilon))`. The lower-cutoff tail retains its accepted distribution. A new ceiling `T^(13/125+epsilon)` for that actual tail would suffice for the target by layer cake, but (2) does not supply it. This is a norm head, not the accepted squarefree-class head. The accepted distinct-class reduction does not pay any of the rational means or errors of (12).

Finally the infinite tail above `Z` has absolute size `O_K(T^(-K))`, since the divisor/Schwartz estimate is `O(T^(L/2)Z^(1/4+eta-L/2))` and fixed `L` can be increased. Its twelfth moment costs `O(T^(1-12K))`. All partial first and last shells are retained; bounded `T` is absorbed in constants. Recombination by the finite norm inequality pays all mixed terms, with at most powers of `log T` for dyadic shells, absorbed into epsilon. Restoring the sharp discrepancy gives only the inherited `integral_(Y/2)^(3Y)|P(x)|^12 dx << Y^(1+10 theta_LY+epsilon)`; no pointwise exponent is improved.

## 4. First doubtful or unproved step

There is no unproved step in the asserted elementary estimates (1), (2), and (4)--(17), subject to independent review. The first missing improvement is cancellation among the many shortened divisor fibres or among the patch sums in (12) sufficient to remove the `sqrt(Nq)` completion loss in the actual physical range. Keeping those expressions signed is legitimate but does not estimate them.

Uniform square-root cancellation on each patch is also unavailable. The exact resonance control below rules out that stronger local shortcut, but not a mean estimate in `R`, a joint signed patch estimate, or a sharper arithmetic decomposition. This report does not claim a no-go theorem for all quadratic methods. It proves the insufficiency of the displayed fully restored estimates and identifies a false uniform local input.

## 5. Required controls and outcomes

**Changed singleton scale — pass.** At `N~c1 T^(2/5)`, for sufficiently small fixed `c1`, (1) is less than one. Every occupied patch then has `U_j=r2(n)`, independently of its rational phase. The area estimate `sum_(N<n<=2N)r2(n)=pi N+O(sqrt(N))` yields

\[
 \mathcal A_N^{(2)}\gg N^{1/4}\asymp T^{1/10}.
\]

This is an actual-coefficient lower bound for the absolute certificate, not the signed wave. Unlike the prior `T^(1/6)` floor, it is smaller than `T^(13/125)`. Taking the head through `T^(2/5)` costs at most `T^(15/13+epsilon)` by (17), and the preferred head is larger. Thus this control does not reject the new quadratic route. At `N~T^(2/3)`, `H~T^(2/9)` tends to infinity: calling those patches singleton would be false.

**Actual moving quadratic resonance — pass, scoped.** Fix `2/5<sigma<2/3`, put `N~T^sigma`, and take `h=c2 N^(5/6)T^(-1/3)` with small fixed `c2`. Then `h` tends to infinity and is `o(N)`. Averaging the masses of integer-centered windows `|n-m|<=h`, for integer `m` in an interior subinterval of the shell, and using the area estimate on a still smaller interior subinterval, supplies some integer `m~N` with mass at least `c3 h`.

Choose an integer `k` so `R=8k m^(3/2)` lies in `[T/2,2T]`. Such a `k` exists for all large `T`, since `T/m^(3/2)` tends to infinity. The exact second Taylor polynomial at `m` is

\[
 8km^2+4km(n-m)-k(n-m)^2,
\]

which is integral at every integer `n`. Its exact remainder on this window is `O(T h^3/N^(5/2))=O(c2^3)`. With `c2` small, the original terms `e(R sqrt(n))` lie in a fixed small arc about one. Consequently

\[
 \left|\sum_{|n-m|\le h}r_2(n)e(R\sqrt n)\right|\gg h.
\]

In particular no uniform `O(h^(1/2)N^eta)` bound for these actual moving short waves can hold for every eta; choose eta smaller than half the positive exponent of `h` relative to `N`. The integral Taylor polynomial itself has exactly the full unsigned mass. This proves a local resonance, not an absolute-certificate lower bound after the entire shell is summed, and not a lower bound on any full moment. It does not by itself reject averaged or joint signed cancellation. The conductor suggested this control during the task; the averaging, integer-radius choice, and residual check are explicitly supplied here rather than represented as independent discovery.

**Arithmetic weight and reduced conductors — pass.** Formula (8) keeps `chi4` and uses only its actual period four; every fibre reduces `q` to `q/gcd(d^2,q)`. The chosen rationalization has primitive numerator by construction. The proof makes no arbitrary weighted quadratic-sum assertion.

**Gauss phase and rational mains — pass.** The mean contains `G(h,q)^2`, never an absolute square in an identity. Formula (12) pays both main and error. With a nonprimitive zero polynomial, the natural reduced conductor is one and its mean is one, consistent with no forced cancellation. No polynomial additive phase is replaced by a multiplicative character twist.

**Restoration and source scope — pass.** Both complete graph nodes inspected are `proved_internal`. The inherited actual supremum is applied only to the actual full wave; the head uses its own mass bound. Every norm shell, every partial endpoint, the real projection and infinite tail are paid. No new literature theorem is imported. No numerical experimentation was performed; the task was analytical apart from file inspection and hashing.

## 6. Dependencies, exact artifacts, and isolation

Read only the assigned brief and its listed contexts. A graph text search displayed adjacent matching lines incidentally; only the two named complete moment/radical nodes were extracted and used. No sibling report, shared synthesis, validation file, or successor plan was read. The accepted kernel supplies the complete distribution, fixed-order inherited actual moment, qualified Li--Yang input, and full tail restoration. The radical kernel supplies scope checks only. The prior local-remainder report supplies the earlier scoped certificate and exact norm-lattice setup; the new quadratic algebra and divisor estimate are derived here.

Conductor steering during the task concerned the moving integer Taylor resonance, primitive rational numerators, and keeping this task on the quadratic route. A conductor message mentioned a possible unrelated higher-degree source; that source was neither read nor used here.

Input SHA256 values:

```
protocol.md
f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a
state/active_campaign.yml
fd65ce5c6b117aa4ca8ed097f85e2c786621c8054ca81791aa6e5e17006a82fa
state/proof_obligations.yml
a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b
strategy/round231_quadratic_signed_admission/briefs/quadratic_remainder_attack.md
8c7e1279dab8294d4d9dc62d6c446c2682e65e3c10f71fc5da89fc42da8e526a
strategy/round231_quadratic_signed_admission/briefs/complete_interface.md
abaa43deda1db65351578941aec47e2af0aadfedcf0942b95bfea4c8636de83d
proofs/kernels/gc_complete_square_root_large_values_moment_bound.md
942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212
proofs/kernels/gc_complete_distinct_radical_moment_reduction.md
d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee
strategy/round231_local_arithmetic_admission/reports/oscillatory_remainder_gate.md
834954f74200d00a508aeb0d360134a444ea1b3b0b2271d4e3b271ecd95febfe
```

The final report hash is communicated after freezing, rather than embedded in the file it hashes.

## 7. Recommended state effect

Retain the proved actual quadratic-twist estimate and changed patch geometry as reviewed admission evidence if their proof seams pass. Reject only an attempted inference of an improved complete moment from (2), (10), or (11), and reject the stated uniform square-root short-wave shortcut. Do not reject the genuinely signed or averaged quadratic route. No new complete exponent, target distinct-class bound, M1/M2 parent, or quarter theorem has been proved. Recommend no change to the authoritative graph or proof draft. Stop after this report and its hash; any later review or repair requires the conductor's bounded assignment.
