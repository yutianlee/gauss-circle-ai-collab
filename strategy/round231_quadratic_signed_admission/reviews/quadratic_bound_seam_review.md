# Nonauthor review of the exact quadratic-twist estimate

Round231 prelaunch admission; reviewer task `quadratic_bound_review`; 2026-10-11. Graph SHA256 `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`. Reviewed report SHA256 `abff6860790aba4cda537ad9e81af504c1f175844a2c252479e685077dd1eb24`. This review makes no state change.

## 1. Result and verdict

**PASS.** The elementary bound in equation (2) of the assigned report is valid for positive odd conductor `q`, coprime numerator `a`, arbitrary real linear coefficient, and every half-open subinterval of the indicated shell. The rationalization, exact hyperbola partition, reduction of possibly degenerate fibre conductors, rational main identity, and complete restoration all pass. No mathematical correction to the frozen report is required.

The conclusion is correctly limited: the proved estimate does not certify a complete improvement in the required short-patch range. Its oversized completion term is an upper-bound cost, not a lower bound for the signed wave. The local resonance control refutes the specified uniform square-root local estimate, not the complete polynomial route or a moment estimate.

## 2. Exact statement and hypotheses checked

For `N>=2`, a real half-open interval `I=(l,u]` contained in `(N,2N]`, `u-l<=H`, positive odd integer `q`, integer `a` with `(a,q)=1`, and arbitrary `lambda in R`, the claim is

\[
\left|\sum_{n\in I}r_2(n)e(an^2/q+\lambda n)\right|
\ll\tau(q)\log^2(2Nq)
\left(Hq^{-1/2}+\sqrt{Nq}\right).
\]

The independently available cap is `O_eta((H+1)N^eta)`. The arithmetic coefficient is the actual `r2=4(1*chi4)`, and `e(t)=exp(2pi i t)`. No arbitrary-weight version is claimed.

In the physical application, `T>=2`, `R in [T/2,2T]`, and
`H=c min(N,N^(5/6)T^(-1/3))`. The report retains the full shell, all partial endpoints, the exact smooth multiplier, the prescribed real cosine projection, and the infinite Schwartz tail.

## 3. Independent seam derivation

### Primitive rationalization and the exact residual

The integers coprime to a power of three have successive gaps at most two. Therefore every real number is within one, and hence within the claimed `3/2`, of a numerator coprime to `3^k`. Choosing `q=3^k` in the report's factor-three interval enforces `q>=max(3,H^2)` and `(a_j,q)=1`; there is no denominator reduction loss hidden in this construction. The separate nearest-integer choice of `b_j` gives the stated slope error `1/(2q)` even for nonintegral patch centers.

The exact derivatives are
`f'=R/(2sqrt(x))`, `f''=-R/(4x^(3/2))`, and `f'''=3R/(8x^(5/2))`. Thus the derivative of the residual has three costs whose integrated sizes are

\[
TH^3N^{-5/2},\qquad H^2/q,\qquad H/q.
\]

All are bounded. For the last term, use `H/q<=1` when `H>=1`, and `H/q<=1/3` when `H<1`. The amplitude variation and Abel summation consequently justify equation (4), including a final partial interval. A potentially large constant phase in `f-P` is irrelevant to variation and has not been discarded from the identity.

### Composite Gauss sums and a real linear coefficient

Let `Q` be positive and odd and `(A,Q)=1`. Completing the square modulo `Q`, followed by the invertible difference/sum change of variables, gives

\[
\left|\sum_{t\bmod Q}e((At^2-ht)/Q)\right|=\sqrt Q
\]

for every integer `h`, with no primality or squarefreeness assumption. Therefore the discrete Fourier coefficients of `e(At^2/Q)` all have modulus `Q^(-1/2)`.

After multiplying by `e(mu t)`, the frequencies remain spaced by `1/Q` modulo one, for every real `mu`. A geometric sum on an interval of real length `L0` is bounded by a constant times `min(L0+1,1/||theta||)`, with the zero-distance case interpreted by the first entry. Separate one closest frequency; all remaining distances have reciprocal sum `O(Q log(2Q))`. It follows that

\[
\left|\sum_{t\in J}e(At^2/Q+\mu t)\right|
\ll (L0+1)/\sqrt Q+\sqrt Q\log(2Q).
\]

The extra `1/sqrt(Q)` is absorbed by the second term, proving the report's (6). For `Q=1`, the same displayed conclusion follows from the trivial `L0+1` bound. Thus empty, singleton, and degenerate-conductor fibres are covered, and no rationality of `mu` is used.

### Hyperbola ownership and the gcd sum

With `D=floor(sqrt(2N))`, a pair `dm<=2N` cannot have both `d>D` and `m>D`, since `(D+1)^2>2N`. Consequently the two sets in the report's (7) form a disjoint complete partition. The cutoff in the second fibre is exactly `d>max(D,l/m)`, with the upper endpoint included. This produces equation (8) with no diagonal correction or omitted boundary.

For an outer integer `d`, cancel the quadratic coefficient to conductor
`q_d=q/gcd(d^2,q)`. Its numerator is coprime to `q_d`. The real linear coefficient may change but remains allowed by the preceding bound. In the second hyperbola piece, `d=r+4t` multiplies the leading coefficient by16; because `q` is odd, the cancelled conductor remains `q/gcd(m^2,q)`. The two nonzero character classes have constant signs; their shortened fibres cost only a fixed factor.

For every prime power `p^e||q`, writing `v=v_p(d)` gives
`min(2v,e)/2<=min(v,e)`. Hence

\[
\sqrt{\gcd(d^2,q)}\le\gcd(d,q).
\]

Using `gcd(d,q)=sum_(r|d,r|q) phi(r)` and writing `d=rk` then yields

\[
\sum_{d\le D}\frac{\sqrt{\gcd(d^2,q)}}d
\le\sum_{r\mid q}\frac{\varphi(r)}r
\sum_{k\le D/r}\frac1k
\ll\tau(q)\log(2D).
\]

Together with `sum_(d<=D)sqrt(q_d)<=D sqrt(q)`, this proves the claimed bound. The logarithms and the extra `tau(q)` multiplying the second term in the report only enlarge the valid upper bound. Directly counting the original norm atoms gives the stated independent cap.

### Exact rational main and remainder

The residue-count identity is exact because an integer polynomial modulo `q` depends only on `n mod q`. For a translated lattice of spacing `q`, the disk-square comparison costs `O(sqrt(x)/q+1)` per vector residue; summing `q^2` vector residues gives `O(qsqrt(x)+q^2)`. Removing the origin is absorbed. Thus equation (10) is valid for the rational polynomial mean as defined.

For arbitrary `h mod q`, including nonprimitive `h`, the difference/sum calculation gives
`|G(h,q)|^2=q gcd(h,q)`. The identity for the additive norm mean is the algebraic square `G(h,q)^2/q^2`. Taking moduli only at the inequality stage and summing yields

\[
|K|\le q^{-1/2}\sum_{h\bmod q}\frac{\gcd(h,q)}q
=q^{-1/2}\sum_{r\mid q}\frac{\varphi(r)}r
\le q^{-1/2}\tau(q).
\]

This verifies (11) without changing a complex square into an absolute square inside an identity. Since `dE_P` is the actual atomic measure minus `pi K dx`, the exact Stieltjes formula (12) follows directly, with both boundary terms retained through `E_P(y)-E_P(l_j)`. Its local main is not asserted to vanish. Applying the whole-sum estimate (2) pays both main and remainder together.

### Complete restoration and its logical scope

For `H>=1`, there are `O(N/H+1)=O(N/H)` patches because `H<=cN`. Summing the proved bound and restoring `N^(-3/4)` gives exactly

\[
N^{1/4}/\sqrt q+N^{3/4}\sqrt q/H.
\]

For `N<=T`, `H<=c sqrt(N)`, so the second expression in this available bound is at least `c^(-1)N^(1/4)` for every positive conductor. This compares the numerical upper-bound certificate with the elementary shell mass; it does not compare that mass with the signed sum from below. Capping the estimate by the direct shell mass is necessary and is correctly done.

The complete ceiling `T^(1/4)` and the accepted distribution restore to exponents `1,5/2,18/13`. The inherited actual ceiling restores to `1,10beta,1+20beta/13`; the accepted inequality `beta>13/110` makes `10beta` largest. The norm head at `X=T^(52/125)` has exponents `1,26/25,29/25`. These arithmetic checks agree with (15)--(17). The fixed Schwartz estimate pays the entire upper tail, and finite norm inequalities pay mixed terms. The actual supremum is used only for the actual full real wave.

## 4. First doubtful or unproved step

No gap was found in the elementary bound or its stated application. The first missing improvement is an estimate that controls the joint signed contribution of shortened fibres or patches strongly enough to overcome the displayed completion loss. Such a bound is not supplied merely by preserving signs in an exact expression.

The report correctly avoids converting the insufficiency of its particular upper bound into an arithmetic lower bound or a universal quadratic-method obstruction. Its inherited full moment remains unchanged.

## 5. Required controls and outcomes

- **Odd composite degeneration: PASS.** With `q=9` and outer divisor `d=3`, the quadratic conductor becomes one. The proof gives the necessary length term rather than a spurious square-root saving. The valuation argument covers every odd prime power and their products.
- **Arbitrary real slope: PASS.** The completion proof uses translated equally spaced frequencies, so integer, rational, irrational, and near-resonant slopes are all included.
- **Sharp endpoints and empty fibres: PASS.** The hyperbola partition uses strict lower and inclusive upper inequalities throughout. The geometric-sum additive constant is absorbed even when the real length is less than one.
- **Primitive physical rationalization: PASS.** Powers of three and the bounded-gap numerator choice guarantee coprimality uniformly; no reduced denominator is assumed comparable after arbitrary rounding.
- **Quadratic means: PASS.** The signed mean is retained exactly, and `G^2` is distinguished from `|G|^2`. The `q=1` degeneracy has mean one and does not force cancellation.
- **Changed singleton scale: PASS.** `H_2~1` occurs at `N~T^(2/5)`, giving the absolute-certificate floor `T^(1/10)`. At `N~T^(2/3)`, the patch length is `T^(2/9)`, not a singleton. The generic head cost at `T^(2/5)` is `T^(15/13+epsilon)`.
- **Moving local resonance: PASS, scoped.** Averaging windows over an interior shell gives an integer center with mass `gg h`. For `2/5<sigma<2/3`, the interval of admissible integers `k` with `R=8km^(3/2)~T` has length tending to infinity. The quadratic Taylor polynomial is integral at integer norms, and its cubic remainder is `O(c2^3)`. Hence the local raw wave is `gg h`, refuting the stated uniform square-root shortcut. This does not estimate the full wave or its moment from below.
- **Complete owners and experimentation: PASS.** No shell, rational main, endpoint, or infinite tail is silently discarded. All checks above are exact algebra or inequalities; no numerical experiment or fresh literature search was used.

## 6. Dependencies, exact artifacts, and isolation

Read the assigned review brief and frozen report. The protocol, active manifest, complete interface, accepted complete-moment kernel, and prior oscillatory-remainder context had already been read in the separately assigned source task; this review uses them only for the normalizations and accepted restoration interface. The independently authored source report was not edited or used to validate the elementary proof. No other sibling report, shared synthesis, or successor plan was read for this review.

Exact reviewed artifacts:

```
strategy/round231_quadratic_signed_admission/briefs/quadratic_bound_review.md
08cfeb18249e92b0b12761185392dc963961ac559c4f7252011015b17471efd9
strategy/round231_quadratic_signed_admission/reports/quadratic_remainder_attack.md
abff6860790aba4cda537ad9e81af504c1f175844a2c252479e685077dd1eb24
state/proof_obligations.yml (frozen graph)
a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b
proofs/kernels/gc_complete_square_root_large_values_moment_bound.md
942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212
```

Only this assigned review file is written. Its final SHA256 is returned separately after freezing, avoiding self-referential hashing.

## 7. Recommended state effect

**Retain** the elementary actual quadratic-twist bound and the new local geometry as reviewed evidence. **Retain** the precisely scoped local resonance counterexample. **Reject** an inference of a better complete bound from the displayed completion estimate alone. **No change** to the authoritative graph, complete moment exponent, pointwise exponent, M1/M2, M9, or quarter target. The review passes without required correction and stops here.
