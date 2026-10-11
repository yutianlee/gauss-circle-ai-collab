# Local transfer seam review

## 1. Result

**PASS on mathematical scope and derivation.** Nonauthor review of `reports/oscillatory_remainder_gate.md`, frozen SHA256 `834954f74200d00a508aeb0d360134a444ea1b3b0b2271d4e3b271ecd95febfe`. No substantive repair is required for its exact identities, demodulation argument, actual one-atom certificate obstruction, or stated generic-head limitation. This review does not admit a new complete estimate.

There is one nonblocking presentation defect: equation (3.9), source lines 225-226, contains the broken text `N\ {` followed by `m dyadic}`. Replace that subscript fragment with an ordinary `\text{dyadic}` label in any authorized revision. The following prose fixes the intended dyadic range, so this defect does not affect the mathematical audit. The frozen candidate was not edited.

## 2. Exact statement and hypotheses audited

The review uses the fixed real complete wave, mollifier, physical radius window, and target in the packet. In particular `T>=2`, `R in [T/2,2T]`, `Psi` is the Fourier transform of the stated compactly supported radial mollifier, and the target is the complete real twelfth moment at exponent `29/25`.

The no-go statement concerns exactly the first-order demodulation with interval lengths

    H_N=c_0 min(N,N^(3/4)T^(-1/2)), q_N=max(1,ceil(H_N)),

followed by summing absolute additive partial-sum suprema. Its head is the norm cutoff `n<=X`, paid only by the displayed generic distribution-plus-supremum estimate. The conclusion is a failure of that particular complete certificate, not a lower bound for the signed wave, a universal modular obstruction, or a failure of the target moment.

## 3. Independent checks and derivation

**Stieltjes identity and smooth main.** For `E=A-pi x`, the exact identity is

    sum_n r2(n)F(n)-pi integral F = -integral E F'.

At zero, `E=-pi x`, so `EF=O(x^(1/4))`; the two most singular terms of `EF'` have orders `x^(-3/4)` and `R x^(-1/4)`, both integrable. At infinity, Schwartz decay suffices. The candidate therefore pays both endpoints. Its continuum real projection is also correct: writing `x=y^2`, each marginal frequency is `R-u/sqrt(T)>0` for `|u|<=1`, and its Abel-regularized half-line transform has phase `exp(i pi/4)`. Multiplication by `e(-3/8)` makes it purely imaginary. Removing damping is justified by the Schwartz bound on the original integral and by uniform positivity of the shifted frequencies on the compact marginal support. The physical window satisfies the required strict inequality for every `T>=2`.

**Rational main.** The candidate's coefficient is exactly `kappa(a,q)=G(a,q)^2/q^2`; it is an algebraic square. Finite residue summation gives `E_(a/q)=sum_b e(ab/q)E_(q,b)`. Hence its local formula

    sum_(n in I_j)r2(n)F(n)
      =pi kappa(a_j,q_N) integral_(I_j) g_j
       +integral_(I_j) g_j dE_(a_j/q_N)

is exact, including atoms at right endpoints. Subtracting `E_(a/q)(l_j)` gives the displayed endpoint-inclusive partial summation formula. The rational main cannot be dropped or equated with the globally canceled area transform: its continuously demodulated test depends on the local slope. This remains true for `q=1` and a nonzero integer numerator. The bound `|kappa|<=min(1,2 gcd(a,q)/q)` follows from `|G|^2<=q gcd(2a,q)` and is valid without reducing the fraction.

**Widths and costs.** The raw phase width is `sqrt(N)/R`. After subtracting `a_j x/q_N`, the exact residual derivative has total variation bounded by

    O(H_N/q_N+T H_N^2/N^(3/2))=O(1).

The amplitude derivative has the claimed Schwartz envelope; it does not reintroduce the raw `R sqrt(N)` loss. Thus the rational demodulation is valid even though the raw phase width is subinteger. At `N~T`, `H,q~T^(1/4)`; at `N<=T^(3/2)`, `q=O(T^(5/8)+1)`. All interval counts are retained in the sum defining the certificate. The unmodulated congruence remainder separately costs `(q sqrt(N)+q^2)N^(-3/4)(1+R sqrt(N))`, agreeing with the independently derived local arithmetic report.

**Actual one-atom obstruction.** Choose a full dyadic interior shell with `N~c_1 T^(2/3)` and fixed sufficiently small `c_1`. Then `H_N<1`, each interval has at most one integer, and its partial-sum supremum is precisely `r2(n)` if it contains that integer, regardless of the rational phase. Therefore

    Acal_N=N^(-3/4)[A(2N)-A(N)]
          =pi N^(1/4)+O(N^(-1/4)) >> T^(1/6).

This is uniform in `R`. The shell's envelope `(1+N/T)^(-L)` tends to one. Its position is above `X=T^(52/125)` and below the effective upper cutoff for sufficiently large `T`, so it survives complete restoration. Since `1/6>13/125`, it refutes (3.9). This is an actual coefficient certificate, while cancellation between its interval contributions has expressly been discarded; there is no inference of a signed lower bound.

**Generic norm head and the full moment.** Accepted204 has the distribution uniformly for every real lower cutoff. For `H_X=B_(T,0)-B_(T,X)`, the level-set union bound supplies the same distribution for levels at least 2; levels below 2 cost `O(T)`. The area estimate and partial summation give `||H_X||_infty=O(X^(1/4))`. Layer cake at order 12 therefore yields exactly

    M_12(H_X)<<T^epsilon(T+X^(5/2)+T X^(5/13)).

The exponents at `X=T^(52/125)` are `1,26/25,29/25`. For a hypothetical cutoff-wave supremum `T^gamma`, the same layer cake gives `T+T^(10gamma)+T^(1+20gamma/13)`; at `gamma=13/125`, its maximal exponent is `29/25`. No accepted arbitrary-cutoff pointwise estimate is silently substituted for that hypothesis.

To obtain any exponent `b<10 beta` from the stated head bound with `X=T^sigma`, the necessary condition `(5/2)sigma<=b` gives `sigma<4 beta<2/3`. The one-atom shell then remains outside the head. Swallowing it would leave the unhelpful `X^(5/2)` term of exponent at least `5/3`. These are restrictions of this upper-bound method, not estimates from below for the true head moment. All partial shells, logarithmic recombination losses, real projection, and the absolute Schwartz tail are paid as claimed.

## 4. First unproved step

The exact signed remainder and rational-main identities have no uncovered step in this audit. The first genuine unproved analytic input is a useful bound for the signed oscillatory Stieltjes remainders together with their changing rational mains. Their absolute short-interval replacement is actually too large by the proved one-atom shell.

The review does not exclude larger patches with a nontrivial treatment of the quadratic residual, higher-order phases, cancellation between patches, or a better norm-head theorem. Those are outside the candidate's stated scope and are not methods supplied by this review.

## 5. Controls and outcomes

All checks were analytical; no new computation or external theorem was used.

* Zero endpoint, infinite endpoint, inclusive lattice atoms, and the physical inequality `R>T^(-1/2)`: pass.
* `G^2` versus `|G|^2`, unreduced rational slopes, and the retained changing rational main: pass.
* Raw microscopic width versus bounded-variation demodulated patch width: pass.
* Actual one-atom shell, full dyadic complement, and comparison `1/6>13/125`: pass.
* Distribution quantifiers for arbitrary cutoffs, head layer cake, norm-head versus squarefree-head distinction, and all displayed restored exponents: pass.
* Certificate lower bound versus signed-wave lower bound: the distinction is correctly maintained.

## 6. Dependencies and provenance

Candidate reviewed:

    strategy/round231_local_arithmetic_admission/reports/oscillatory_remainder_gate.md
    SHA256 834954f74200d00a508aeb0d360134a444ea1b3b0b2271d4e3b271ecd95febfe

Other allowed contexts used:

    protocol.md
    f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a

    strategy/round231_local_arithmetic_admission/briefs/complete_target.md
    4cd95ec7203420e99e51a4dbf3e0de5c3732fe1e589ed9e3344bb0b96b1fd8d6

    strategy/round231_local_arithmetic_admission/reports/local_residue_arithmetic.md
    403e2c52c67dd46d033a06ae0d002d308dd695af1018241463f5c91410f67d41

    proofs/kernels/gc_complete_square_root_large_values_moment_bound.md
    942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212

The candidate and own frozen-report hashes were checked during this review. Accepted216 was not needed. No other new file was read, and only this assigned review was written. This is a nonauthor line and implication audit, not a statement-only blind review. The candidate, own arithmetic report, and shared state remain untouched.

## 7. Recommended state effect

Retain the candidate as reviewed prelaunch evidence, with the single nonblocking typesetting note above. No complete analytic admission follows. Reject only the specific absolute certificate at the requested exponent; preserve the actual signed target and all stronger unprovided inputs as open. No graph change, promotion, successor, or campaign launch is recommended. Stop after this review's separately communicated hash.
