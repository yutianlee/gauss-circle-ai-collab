# Actual oscillatory remainder: signed interface and complete local-transfer obstruction

Round231 local-arithmetic admission continuation; analytic Round231 remains unlaunched. Task `oscillatory_remainder_gate`, claimant/deriver, 2026-10-11. Frozen graph SHA256 `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`. This report is evidence, not accepted mathematics.

## 1. Result

There is an exact, complete signed Stieltjes interface for the actual remainder of the norm-lattice count. Ordinary congruence means give a rigorous uniform error for this interface, but absolute partial summation loses the factor `1+R sqrt(N)` on a norm shell `n~N`. At `N~T, R~T` it gives the unhelpful upper-bound scale `q T^(5/4)+q^2 T^(3/4)`; taking the elementary coefficient mass instead gives `T^(1/4)`. Neither improves the accepted complete twelfth moment.

The microscopic continuous norm width is `sqrt(N)/R`, hence `T^(-1/2)` at `N~T`. This is NOT an impossibility theorem for polynomial moduli: exact rational demodulation works on intervals of length `H~N^(3/4)T^(-1/2)` with denominator `q~H`, giving `H,q~T^(1/4)` at `N~T`. The quadratic Taylor remainder and rational-approximation error can both be retained with bounded variation. What is missing is a useful signed short-interval remainder estimate, and payment of the rational main terms.

A narrower no-go result is proved for a concrete elementary transfer: first-order rational demodulation, followed by the sum of absolute short-interval partial-sum bounds. In the actual shell `N~T^(2/3)` that certificate is at least `c T^(1/6)`, because its intervals contain at most one integer. A head large enough to remove this shell cannot be paid at an improved exponent by the stated generic head-moment bound. Thus this complete transfer plus that head bound cannot improve `10 beta`, and in particular cannot reach `29/25`. This is an obstruction to a specified certificate, not a lower bound on the signed circle wave or its moment.

## 2. Exact hypotheses and statements

Use exactly the fixed `rho,Psi,w,B_T` in both complete-target briefs. Put

```
A(x) = sum_(1<=n<=x) r2(n),  E(x)=A(x)-pi x,
F_(T,R)(x)=x^(-3/4) Psi(sqrt(x/T)) e(R sqrt(x)),   x>0.
```

All real endpoints are interpreted with the displayed inclusive convention; Stieltjes integrals below account for atoms at integers. For integers `q>=1`, let

```
C_q(b)=#{(u,v) mod q: u^2+v^2=b mod q},
nu_q(b)=C_q(b)/q^2,
A_q,b(x)=sum_(1<=n<=x, n=b mod q) r2(n),
E_q,b(x)=A_q,b(x)-pi nu_q(b)x.
```

Then, uniformly in `q,b,x>=1`,

\[
 |E_{q,b}(x)|\ll C_q(b)(\sqrt x/q+1)+1,
 \qquad \sum_{b\bmod q}|E_{q,b}(x)|\ll q\sqrt x+q^2. \tag{2.1}
\]

For the supremum over `x` in a fixed shell the same summed bound holds. No error cancellation in `b` is asserted. Exact identities are

\[
 E=\sum_b E_{q,b},\qquad
 B_T(R)=-\operatorname{Re}\left(e(-3/8)\int_0^\infty E(x)F'_{T,R}(x)\,dx\right),
 \quad R>T^{-1/2}. \tag{2.2}
\]

Thus the actual signed coefficient remainder is retained inside its oscillatory transform; no independent-density model is introduced.

For a shell `N<n<=2N`, define

\[
 H_N=c_0\min(N,N^{3/4}T^{-1/2}),\quad 0<c_0<10^{-2},\qquad
 q_N=\max(1,\lceil H_N\rceil).
\]

Partition the shell into real half-open intervals `I_j=(l_j,u_j]` of length at most `H_N`; a last partial interval is retained. For each interval choose its midpoint `x_j`, and choose an integer `a_j` with

\[
 \left|{R\over2\sqrt{x_j}}-{a_j\over q_N}\right|\le {1\over2q_N}.
\]

No reduction of the fraction is required. Define the actual additive partial-sum bound

\[
 U_j(R)=\sup_{l_j\le y\le u_j}
 \left|\sum_{l_j<n\le y}r_2(n)e(a_j n/q_N)\right|,
 \qquad {cal A}_N(R)=N^{-3/4}\sum_j U_j(R).
\]

For every fixed `L`, with constants depending on fixed functions and `L`,

\[
 \left|\sum_{N<n\le2N}r_2(n)F_{T,R}(n)\right|
 \ll_L (1+N/T)^{-L}{\cal A}_N(R),\quad R\in[T/2,2T]. \tag{2.3}
\]

The precise signed remainder version of this transfer, including its rational main, is (3.6) below. Inequality (2.3) is useful for defining a rigorous, falsifiable certificate, not claimed to have a target-sized right side.

For dyadic `N` in `[c_1 T^(2/3),2c_1 T^(2/3)]`, with a fixed sufficiently small `c_1>0`, one has, uniformly in real `R` in the physical window,

\[
 {cal A}_N(R)\gg N^{1/4}\gg T^{1/6}. \tag{2.4}
\]

The same assertion holds for the complete sum of these nonnegative shell certificates. It concerns the actual `r2(n)`, not masked, aligned, or random coefficients.

## 3. Derivation and complete restoration

### Exact congruence error and its signed transform

The elementary disk/unit-square argument on each translate of `q Z^2` gives

\[
 \#\{m\in z+q\mathbb Z^2:|m|\le\sqrt x\}
 ={\pi x\over q^2}+O(\sqrt x/q+1).
\]

Indeed the union of side-`q` squares centered at these points lies between disks whose radii differ from `sqrt(x)` by at most a fixed multiple of `q`; dividing their area difference by `q^2` proves the estimate, also when `sqrt(x)<q`. Sum over the `C_q(b)` allowed vector residues, and subtract the origin when `b=0`. Summing the errors in `b` uses `sum_b C_q(b)=q^2`, proving (2.1). This directly uses the two-dimensional norm lattice underlying `r2(n)=4 sum_(d|n)chi4(d)`.

For every compact subinterval of `(0,infinity)`, integration by parts for `dE=dA-pi dx` gives the signed identity. Its endpoints at zero and infinity are legitimate: near zero `E(x)=-pi x`, so `E(x)F(x)=O(x^(1/4))` and `E(x)F'(x)` is locally integrable for each fixed `T,R`; at infinity Schwartz decay beats the polynomial bounds. Consequently

\[
 \sum_{n\ge1}r_2(n)F(n)-\pi\int_0^\infty F(x)dx
 =-\int_0^\infty E(x)F'(x)dx. \tag{3.1}
\]

The real part of the smooth term after multiplication by `e(-3/8)` vanishes for `R>T^(-1/2)`. This is the previously reviewed continuum cancellation, not a new input: putting `x=y^2` reduces it to a constant times the real part of `e(-3/8) integral y^(-1/2)Psi(y/sqrt(T))e(Ry)dy`. The compact marginal of `rho` writes `Psi` as an integral of `e(-uy/sqrt(T))` for `|u|<=1`. Abel damping evaluates each positive-frequency half-line transform with phase `e^(i pi/4)`, so the product with `e(-3/8)` is purely imaginary. Uniform positivity of `R-u/sqrt(T)` justifies removing the damping. This verifies (2.2) within the current packet without promoting the earlier report.

For a shell, including both endpoint terms of Stieltjes integration by parts,

\[
 \left|\int_{(N,2N]}F\,dE_{q,b}\right|
 \le \sup_{[N,2N]}|E_{q,b}|
       (|F(N)|+|F(2N)|+\int_N^{2N}|F'|).
\]

The last parenthesis is at most

\[
 C_LN^{-3/4}(1+N/T)^{-L}(1+R\sqrt N).
\]

Summation in `b` gives the proved cost

\[
 \left|\int_{(N,2N]}F\,dE\right|
 \ll_L (q\sqrt N+q^2)N^{-3/4}(1+N/T)^{-L}(1+R\sqrt N). \tag{3.2}
\]

At `N~T,R~T` this is `O(qT^(5/4)+q^2T^(3/4))`. Taking `q=1` is already better than increasing `q` in this particular estimate. Independently, the shell coefficient mass is `O(N^(1/4)(1+N/T)^(-L))` by the elementary area bound; the smooth shell integral is no larger than this scale. Thus (3.2) supplies no gain even over this elementary mass estimate. The size of an upper bound is not a lower bound on the signed remainder.

### Frequency resolution and rational demodulation

The derivative of the radial phase is `R/(2sqrt(x))`. Its phase-stable continuous norm width is `h~sqrt(N)/R`. Equivalently a frequency displacement `Delta sqrt(n)` is detected by the physical radius window at scale `1/T`, so `Delta n~sqrt(N)/T`. At `N~T` this is less than one. This explains why replacing a short norm interval by its average can discard all phase information. It does not rule out rational additive analysis on the integer lattice.

Write, exactly on `I_j`,

\[
 F(x)=g_j(x)e(a_jx/q_N),\quad
 g_j(x)=x^{-3/4}\Psi(\sqrt{x/T})
                       e(R\sqrt x-a_jx/q_N).
\]

The derivative of the residual phase differs from its value at `x_j` by `O(T H_N/N^(3/2))`. Hence its total variation on `I_j` is

\[
 O(H_N/q_N+T H_N^2/N^{3/2})=O(1). \tag{3.3}
\]

The amplitude and its variation on the interval are `O_L(N^(-3/4)(1+N/T)^(-L))`. Abel summation against the finite additive sum proves (2.3) with every last interval and endpoint included. No Taylor error is discarded; (3.3) estimates the exact residual derivative.

For `N~T`, this uses `H_N~T^(1/4)`, additive-slope accuracy `O(T^(-1/4))`, and `q_N~T^(1/4)`. Up to the accepted effective truncation `N<=T^(3/2)`, denominators need not exceed `O(T^(5/8))`. When `H_N<1`, choose `q_N=1`; exact demodulation still holds but each interval contains at most one integer. Polynomial moduli therefore suffice to represent the relevant local additive phases; the missing issue is a bound, not representation or nominal resolution.

### Actual additive remainder, with rational main retained

Define

\[
 G(a,q)=\sum_{u\bmod q}e(au^2/q),\qquad
 \kappa(a,q)=q^{-2}G(a,q)^2,
\]

\[
 E_{a/q}(x)=\sum_{1\le n\le x}r_2(n)e(an/q)-\pi\kappa(a,q)x.
\]

Finite orthogonality, followed by (2.1), gives exactly

\[
 E_{a/q}(x)=\sum_b e(ab/q)E_{q,b}(x),\qquad
 |E_{a/q}(x)|\ll q\sqrt x+q^2. \tag{3.4}
\]

The square in `G(a,q)^2` is an algebraic square, not an absolute square. The main can be complex, and its phase must be retained. If `(a,q)=1`, direct differencing of `|G|^2` gives `|G|^2<=2q`, because at most two residues solve `2au=0 mod q`; in general the same argument gives `|kappa(a,q)|<=min(1,2 gcd(a,q)/q)`. This is only a size bound, not main-term cancellation.

For any real `l<y<=u` in a norm shell, direct counting supplies

\[
 |E_{a/q}(y)-E_{a/q}(l)|
 \ll_\eta N^\eta(y-l+1)+|\kappa(a,q)|(y-l), \tag{3.5}
\]

and (3.4) supplies the alternative `O(qsqrt(N)+q^2)`. The first follows from the divisor bound on the at most `y-l+1` integers; it includes empty and one-atom intervals. At `N~T`, `H,q~T^(1/4)`, the ordinary congruence error is `T^(3/4)`, whereas the direct short-sum estimate is `T^(1/4+eta)`. Thus the congruence error is not even nontrivial on this short interval.

Most importantly, the exact local transform is

\[
 \sum_{n\in I_j}r_2(n)F(n)
 =\pi\kappa(a_j,q_N)\int_{I_j}g_j(x)dx
       +\int_{I_j}g_j(x)\,dE_{a_j/q_N}(x). \tag{3.6}
\]

The second integral retains the signed actual additive remainder. For example, with `E_j(y)=E_(a_j/q_N)(y)-E_(a_j/q_N)(l_j)`, it is `g_j(u_j)E_j(u_j)-integral_(l_j)^(u_j)E_j(x)g_j'(x)dx`. Neither factor is replaced by its modulus in this identity.

The first terms in (3.6), summed over `j,N` and then real-projected, are a new main-term owner. They do NOT equal the canceled area integral merely because they use local means: `a_j/q_N` changes, and `g_j` is demodulated. Dropping that owner is invalid. Proving cancellation of it and of the actual signed remainders, with their dependence on `R`, would be substantive arithmetic input. Equations (3.4)--(3.5) do not prove this input.

### Complete shell restoration and an explicit impossible absolute certificate

For any real cutoff `X>=1`, put `H_X=sum_(n<=X)a_n cos(...)` and `B_(T,X)=B_T-H_X`. This head is a norm cutoff, not the accepted squarefree-class head. The accepted finite distribution argument applies to the head mask (alternatively use `H_X=B_(T,0)-B_(T,X)` and a union of level sets). Its supremum is `O(X^(1/4))`. Layer cake therefore proves

\[
 M_{12}(H_X)\ll_\epsilon T^\epsilon
        (T+X^{5/2}+TX^{5/13}). \tag{3.7}
\]

For `X=T^(52/125)`, the three exponents are `1,26/25,29/25`. Thus this entire head, all signs and mixed terms included through the norm inequality, is affordable at the desired target. The complementary lower-cutoff wave has the accepted distribution bound. If a NEW pointwise arithmetic input proved

\[
 \sup_{R\in[T/2,2T]}|B_{(T,X)}(R)|\ll_\epsilon T^{\gamma+\epsilon},
 \qquad \gamma=13/125,
\]

then its moment would be

\[
 M_{12}(B_{(T,X)})\ll T^\epsilon
              (T+T^{10\gamma}+T^{1+20\gamma/13})
              \ll T^{29/25+\epsilon}. \tag{3.8}
\]

Together (3.7)--(3.8) would pay the complete wave. This is a sufficient pointwise input, stronger than necessary; it is not asserted as new evidence.

For clarity, the local additive certificate sufficient to provide that pointwise input is the explicitly different, and testable, condition

\[
 \sup_R\sum_{\substack{N\ {m dyadic}\text{covering }(X,T^{3/2}]}}
        (1+N/T)^{-L}{\cal A}_N(R)
             \ll_\epsilon T^{13/125+\epsilon}. \tag{3.9}
\]

Partial first and last shells are restricted in the sums; every interior shell is retained. This is not a renamed moment or convolution CDF. In fact (3.9) is FALSE for this certificate: take a full interior shell `N~c_1 T^(2/3)`. Choosing `c_1` small ensures `H_N<1`; each nonempty interval has one integer, so `U_j=r2(n)` for that interval, for every `R` and every rational chosen. The area estimate `A(2N)-A(N)=pi N+O(sqrt(N))` yields

\[
 {cal A}_N(R)=N^{-3/4}\sum_{N<n\le2N}r_2(n)\gg N^{1/4}\gg T^{1/6}.
\]

Its Schwartz envelope tends to one. This proves (2.4) and contradicts (3.9), since `1/6>13/125`. It also exceeds `beta<13/100`, so taking the smaller of this certificate and the inherited actual supremum cannot improve `beta`.

This is not cured by enlarging the head within the generic head estimate. To prove any exponent `b<10beta` using (3.7), a power cutoff `X=T^sigma` must at least obey `5sigma/2<=b`, hence `sigma<4beta<0.52<2/3`; the obstructing shell remains outside it. Swallowing that shell would produce the unhelpful `X^(5/2)` term of exponent at least `5/3`. This states the exact scope of the no-go: those upper bounds and that absolute local aggregation cannot certify a gain. It does not assert that the head's true moment has size `T^(5/3)`.

Finally, the infinite tail `n>T^(3/2)` is `O_K(T^(-K))` uniformly in real `R` by Schwartz decay and the divisor bound, exactly as in accepted204. For decay order `L`, its absolute mass is bounded by `T^(L/2)(T^(3/2))^(1/4+eta-L/2)`, and fixed `L` can be increased to achieve any fixed `K`. Its moment is `O(T^(1-12K))`. Combining finitely many dyadic shells uses at most `O(log T)` factors, absorbed into epsilon; combining the complete head/tail by `|x+y|^12<=2^11(|x|^12+|y|^12)` retains all mixed contributions. Real cosine projection never costs more than the complex modulus. The argument makes no claim about an arbitrary complex-wave pointwise exponent. Bounded `T` is covered by enlarging constants.

## 4. First doubtful or unproved step

No target estimate is proved. The first missing input in (2.2) is cancellation of the actual `E(x)` against the rapidly oscillating derivative, beyond its magnitude. In the genuinely rational local formulation (3.6), the missing inputs are signed control of its oscillatory Stieltjes remainders and the complete sum of its rational mains. Both must be uniform for the moving real radius and survive the complete complementary shells.

Attempting to replace these signed inputs by (3.9) is not merely unproved: the actual one-atom shell disproves that sufficient absolute certificate. Longer intervals could retain cancellation among many atoms but would carry an unbounded quadratic residual unless that residual is itself analyzed. Higher-order phases, joint cancellation between intervals, or a stronger head estimate are not covered by this no-go and are not supplied here. Ordinary congruence means, even at polynomial moduli capable of representing additive slopes, do not themselves furnish any of those estimates.

## 5. Required controls and outcomes

- **Actual coefficients and signs:** All identities use `r2`, the norm lattice, and actual rational Gauss phases. No claim for signed arithmetic is inferred from an unsigned tuple count. Pass.
- **Microscopic versus modular resolution:** `sqrt(N)/R` is a continuous phase-stable width; `H~N^(3/4)T^(-1/2)` is a demodulated patch length. Denominators `q~H` are polynomial. No blanket impossibility assertion for polynomial moduli is made. Pass.
- **Zero/rational frequency:** At `q=1`, `kappa=1`, so the additive mean is the area mean. At general `q` it is `G^2/q^2`, not `|G|^2/q^2`. Even `q=1` in a patch can use a nonzero integer `a_j`, whose demodulated continuous main cannot be silently identified with the original area transform. Pass.
- **Actual one-atom control:** In the complete interior shell `N~T^(2/3)` the local absolute certificate is `gg T^(1/6)` for every physical radius. This rigorously falsifies (3.9) for the actual coefficients. It says nothing of that size about the signed shell. Pass.
- **Full restoration:** Norm head cost (3.7), lower-cutoff moment (3.8), all partial shells, real phase, endpoint atoms and infinite Schwartz tail are explicitly retained. Accepted squarefree head and distinct-class reduction are not misused to pay a different norm cutoff. Pass.
- **No computation as proof:** No numerical experiment, asymptotic simulation, external theorem import, or web search was used. Resource allocation is entirely analytical apart from file hashes. Pass.

## 6. Dependencies, exact provenance and isolation

Only the assigned brief, protocol, active-campaign manifest, the two complete-target briefs, the two accepted kernels, the specified conductor signed-cancellation file, and selective graph text were read. The graph check established `proved_internal` for the two named nodes. A line-context search also displayed adjacent graph text incidentally; no neighboring claim was used. No sibling report, blind statement, inherited local report, source file, synthesis, or successor plan was read. The old manifest remains Round230 complete; this report does not alter that status.

Accepted dependencies are the complete distribution/finite coefficient argument and elementary area/divisor bounds in accepted204; accepted216 is used only to identify scope and avoid confusing its squarefree head with (3.7). The conductor's prior smooth cancellation is independently checked in Section3 and is not represented as an accepted new fluctuation estimate. The conductor's only mathematical steering during the task asked to distinguish phase-stable width from rational demodulation, retain Taylor and complement costs, and label short-twist hypotheses as unproved; no sibling derivation was supplied.

Input SHA256 values:

```
protocol.md
f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a
state/active_campaign.yml
fd65ce5c6b117aa4ca8ed097f85e2c786621c8054ca81791aa6e5e17006a82fa
state/proof_obligations.yml
a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b
strategy/round231_local_arithmetic_admission/briefs/oscillatory_remainder_gate.md
68ab59b3bcee9eb73d1c46becd7594e3428a8abcbaa1a92a14eea868924168b3
strategy/round231_local_arithmetic_admission/briefs/complete_target.md
4cd95ec7203420e99e51a4dbf3e0de5c3732fe1e589ed9e3344bb0b96b1fd8d6
strategy/round231_cross_label_admission/briefs/complete_target.md
8ee37ee007ff58b8cda6db3d33205c0896639099a44be159ff930a7e86b19809
proofs/kernels/gc_complete_square_root_large_values_moment_bound.md
942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212
proofs/kernels/gc_complete_distinct_radical_moment_reduction.md
d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee
strategy/round231_cross_label_admission/conductor_signed_cancellation.md
cae74ae9a9e9ea5b85b0aac2a025cf52cdb87ce3f835ce0a1fd36c67f3868db3
```

Final report hash is communicated separately after the file is frozen; it is not self-embedded.

## 7. Recommended state effect

Retain as bounded admission evidence after nonauthor review. Reject only the inference from ordinary local means to a target-sized signed remainder, and the specific absolute short-patch certificate (3.9). Retain the actual signed transform and rational-main/remainder decomposition as exact diagnostic interfaces. No improved complete moment, pointwise exponent, distinct-class estimate, M1/M2 parent, or quarter theorem is established. Make no graph, proof-draft, validation, synthesis, campaign, or successor mutation. Stop after this report and its hash.
