# Balanced source audit: bilinear competitor and an actual smooth norm tail

Round231 bounded prelaunch continuation; task `balanced_source_audit`; role: independent primary-source auditor and quantitative competitor. Generated 2026-10-11. Starting graph SHA256 `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`. Candidate report, not accepted graph mathematics. No sibling report was read. Two source applications are audited: Kowalski–Robert–Wu Proposition 5 and the real r2 Hankel identity. Preliminary Robert–Sargos screening was superseded by the stronger first application; no third application is asserted.

## 1. Result

The bilinear source is applicable at the square-root exponents, but its fully restored bound does not improve the complete moment. Its decisive weighted shell term is

    T^(1/8) N^(1/16),

not a saving of this size relative to the original normalized wave. In the adaptive central region it gives a full ceiling T^(3/16+epsilon), which is weaker than the inherited actual ceiling T^beta.

The source audit also independently reproduces an inherited paid narrowing. For a fixed smooth eta with eta(t)=0 for t<=1 and eta(t)=1 for t>=2, the actual r2 wave with multiplier eta(n/Q), Q=T^(99/125), satisfies

    sup |B_high| << T^(13/125+epsilon),
    M12(B_high) << T^(29/25+epsilon).

Consequently the same high-norm portion of W_* is paid at 29/25, by subtracting the already controlled high portion of U_*. The missing owner can be replaced exactly by the fixed smooth mask

    W_low(R) = sum_(X0<n<=Z) (1-eta(n/Q)) w_*(n)
               n^(-3/4) Psi(sqrt(n/T)) cos(2pi R sqrt(n)-3pi/4),

supported on X0<n<2T^(99/125). Every omitted part is paid in the physical L12 norm. The 99/125 tail cutoff and odd Hankel kernel were already reviewed in Round205, and the two-sided norm-band principle was used again in Round208. They are not new analytic progress. The only new combination here is with the recent adaptive balanced divisor mask. No improved bound for this middle owner is established, and no complete moment or pointwise exponent is improved.

## 2. Exact statements, source cards, and hypotheses

Use exactly the real coefficients, rho, Psi, w, T, X0=T^(52/125), Z=T^(3/2), adaptive cutoff, and radius-independent patch starts from `briefs/balanced_interface.md`. All estimates hold for every real R in [T/2,2T] and every real T>=2, with bounded T absorbed into constants. Epsilon losses have constants depending on fixed smooth functions and finitely many chosen derivative orders.

**Application A: primary bilinear source.** E. Kowalski, O. Robert, J. Wu, *Small gaps in coefficients of L-functions and B-free numbers in short intervals*, Rev. Mat. Iberoam. 23 (2007), 281–326, DOI 10.4171/RMI/496, [publisher PDF](https://ems.press/content/serial-article-files/38194), printed p.303, Proposition 5 and its preceding definition. The [publisher record](https://ems.press/journals/rmi/articles/4742) gives submission 2005-07-27 and publication 2007-04-30. For X>0, A,B>=1, |phi_a|,|psi_b|<=1, and alpha,beta real outside {0,1}, it bounds

    S = sum_(a~A,b~B) phi_a psi_b
        e(X a^alpha b^beta/(A^alpha B^beta))

by

    (AB)^epsilon [(X A^6 B^6)^(1/8)
                   + A^(1/2) B + A B^(3/4) + X^(-1/2) AB].

There is no exclusion alpha+beta=1 or alpha=beta. Thus alpha=beta=1/2 and the real character coefficients are allowed. The proof treats both X>=B^2 and X<=B^2; no aspect-ratio restriction is silently imported. The fixed phase scale is X=R sqrt(AB).

**Application B: exact real r2 summation.** B. C. Berndt, A. Dixit, S. Kim, A. Zaharescu, *Sums of squares and products of Bessel functions*, [arXiv:1701.07460v1](https://arxiv.org/html/1701.07460), 2017-01-25, Theorem 1.1, equation (1.2), records the Hardy–Landau formula for real bounded-variation tests on a finite positive interval. Endpoint integers receive the stated half weights. Its smooth compact-support specialization is

    sum_(n>=1) r2(n) h(n)
       = pi integral_0^infinity h(y)dy
         + pi sum_(k>=1)r2(k) integral_0^infinity
                                      h(y)J0(2pi sqrt(ky))dy.       (H)

Here h is real C_c^infinity((0,infinity)), so it vanishes at the chosen interval endpoints and there is no half-weight ambiguity. This specialization is independently proved below. The Bessel expansion and real-positive remainder bound are verified in [DLMF 10.17.3 and section 10.17(iii)](https://dlmf.nist.gov/10.17); the angular integral is [DLMF 10.9.1](https://dlmf.nist.gov/10.9).

The quantitative shell lemma proved here is: if A_N is real smooth, supported on [cN,CN], and

    |(y d/dy)^j A_N(y)| <= C_(j,L)(1+N/T)^(-L),

then, uniformly for T^(52/125)<=N<=T^(3/2),

    |sum r2(n)n^(-3/4)A_N(n)cos(2pi R sqrt(n)-3pi/4)|
      <<_(epsilon,L) T^epsilon (1+N/T)^(-L)
          [T^(1/2)N^(-1/2)+T^(-1/2)+N^(-1)].                 (S)

The constants c,C are fixed positive constants. The N^(-1) term explicitly pays a globally summable Bessel remainder. It is harmless throughout the claimed range and is retained rather than hidden.

## 3. Derivation and full restoration

**A. Bilinear coefficients and every boundary.** Write N~dm and orient the divisor pairs using d<=m. Away from d=m, the ordered sum becomes a sum with coefficient chi4(d)+chi4(m), split into two separable terms. The diagonal is included once and has absolute weighted size at most a constant, since sum_d d^(-3/2) converges. For fixed d, d>=D_T(x(dm)) is an upper interval condition on m, since x and D_T are nondecreasing. Because m>=d, this one condition implies both original balanced inequalities. Intersecting with d<=m and norm endpoints still gives one m interval. Cutoff equalities are assigned as in the interface.

A varying interval in each fibre costs only logarithmically here, not one factor for every patch. Indeed, additive Fourier completion on an ambient integer m interval of length O(M) writes its indicator using a kernel bounded by C min(M,||t||^(-1)). Divide the fibre kernel by this common envelope and absorb the resulting bounded d-dependent factor into phi_d. Absorb e(tm) into psi_m. The envelope has integral O(log(2M)), and the source permits arbitrary complex bounded coefficients. This establishes the required proper-interval extension uniformly, with the actual real sum recovered afterwards. Partial summation in the product dm pays amplitude plus total variation O_L(N^(-3/4)(1+N/T)^(-L)); an additional product threshold is again one interval per fibre. Dyadic divisor rectangles and norm shells contribute only fixed powers of log T.

Let D<=sqrt(N) be the smaller factor scale and M~N/D. Substituting A=D, B=M, X=R sqrt(N), and restoring N^(-3/4) gives

    T^epsilon (1+N/T)^(-L)
      [T^(1/8)N^(1/16)+N^(1/4)D^(-1/2)+D^(1/4)+T^(-1/2)]. (K)

Each exponent follows separately: the source first term is X^(1/8)N^(3/4), so the normalization cancels N^(3/4), leaving X^(1/8)=T^(1/8)N^(1/16). Reversing the source orientation does not improve the two aspect-ratio terms when D<=sqrt(N).

Write N=T^nu. The adaptive lower factor exponent is

    delta_min = -533/5250 + 29nu/84,

up to fixed comparability constants. Across the entire central factor range, the three positive exponents in (K) are bounded by

    1/8+nu/16,
    533/10500+13nu/168,
    nu/8.

The first dominates both others for 52/125<=nu<=3/2. Capping by the trivial norm-shell estimate N^(1/4+epsilon), the usable shell exponent below N=T is

    min(nu/4, 1/8+nu/16).

The two branches cross at nu=2/3. For N>T the Schwartz factor in (K), with L chosen sufficiently large, makes the maximum occur at N~T; all n>Z are separately arbitrarily small. Thus the full source ceiling is gamma=3/16. The accepted coefficient-uniform distribution gives the restored moment exponent

    max(1,10gamma,1+20gamma/13)=15/8.

On the subsequently narrowed interval n<2Q, Q=T^(99/125), the analogous source ceiling is 349/2000, still larger than beta. The source neither exploits the specific character enough nor furnishes the required physical twelfth-moment saving.

**B. Independent proof of (H).** For h real C_c^infinity((0,infinity)), the function f(x)=h(|x|^2) on R^2 is smooth and compactly supported, including at the origin. Periodize f and evaluate its absolutely convergent Fourier series at zero. Group lattice points by their squared norm. Angular integration and y=r^2 give

    f-hat(k)=2pi integral_0^infinity h(r^2)J0(2pi|k|r)r dr
            =pi integral_0^infinity h(y)J0(2pi sqrt(|k|^2 y))dy.

The zero spatial term h(0) vanishes; the zero Fourier term is the integral in (H). This proves (H) and absolute convergence for every fixed smooth test without appealing to the convergence of a sharp Hardy series.

**C. Quantitative real shell transformation.** Set

    h(y)=y^(-3/4)A_N(y)cos(2pi R sqrt(y)-3pi/4).

The zero Fourier term is O_J(N^(1/4)(R sqrt(N))^(-J)(1+N/T)^(-L)) by integration by parts after s=sqrt(y). It is negligible.

For k>=1 retain the first two oscillatory terms of J0(2pi sqrt(ky)); the remainder is O((ky)^(-5/4)). Its integrated contribution is bounded absolutely by

    (1+N/T)^(-L) N^(-1) sum_(k>=1)r2(k)k^(-5/4)
       << (1+N/T)^(-L) N^(-1).

This sum converges using the elementary divisor bound with a fixed exponent less than 1/4. The leading transformed term, including the outside pi in (H), is

    k^(-1/4) integral_0^infinity A_N(s^2)s^(-1)
      [sin(2pi(R-sqrt(k))s)-cos(2pi(R+sqrt(k))s)]ds.         (J)

In particular the resonant leading term is a sine: at R=sqrt(k) it vanishes. This correct phase is useful as a sign control, although the bound here does not use the zero. Repeated integration by parts gives for each J

    |(J)| << (1+N/T)^(-L) k^(-1/4)
       [(1+sqrt(N)|R-sqrt(k)|)^(-J)
        +(1+sqrt(N)(R+sqrt(k)))^(-J)].

The second oscillatory Bessel term has the same bounds times O((kN)^(-1/2)). Its amplitude derivatives obey the same scaled estimates, so it is smaller in the near range; in the far ranges its sums are bounded by the same argument.

For k comparable to T^2, k^(-1/4) is O(T^(-1/2)), and

    |R-sqrt(k)| = |R^2-k|/(R+sqrt(k)) ~ |R^2-k|/T.

The divisor bound and the elementary count of integers in intervals yield, uniformly even when R^2 is an integer,

    sum_(k~T^2) r2(k)(1+(sqrt(N)/T)|R^2-k|)^(-J)
       << T^epsilon (1+T/sqrt(N)),

for a fixed sufficiently large J. The two terms are the possible single nearest integer and the full annulus width. Frequencies k much smaller or much larger than T^2 have |R-sqrt(k)| bounded below by a constant multiple of T or sqrt(k), respectively. The displayed integration-by-parts bounds, summed with r2(k)<<k^epsilon, make both tails negligible. This proves (S) with every transformed frequency and both real phases retained.

**D. Smooth high tail and the remaining owner.** Choose eta as stated in Section 1. Smoothly partition the support of eta(n/Q) into dyadic shells. The scaled derivative bounds for Psi(sqrt(n/T)) hold to every fixed order, with arbitrary Schwartz power L; the transition eta contributes fixed constants on the first shells. Sum (S) from N~Q through Z. Its geometric sums give

    sup |B_high| << T^epsilon
      [T^(1/2)Q^(-1/2)+T^(-1/2)+Q^(-1)] + O_K(T^(-K)).

The last term is the untouched actual infinite tail n>Z, paid by the original Schwartz/divisor estimate. In general Q=T^q gives a leading ceiling gamma=(1-q)/2 for q<=1, and the stated Q has gamma=13/125. All coefficients are radius independent and divisor bounded, so the accepted Gram distribution applies to this independently proved ceiling. Its layer cake gives exactly

    M12(B_high) << T^epsilon [T+T^(26/25)+T^(29/25)]
                  << T^(29/25+epsilon).

Multiplying U_* by eta(n/Q) preserves its fixed-fibre proper-interval proof: the new weight has bounded total variation and derivative size at its own scale. Thus sup|U_high|<<T^(13/125+epsilon) and M12(U_high)<<T^(29/25+epsilon). Since Q>X0 for large T,

    W_high = B_high-U_high-eta E_Z,
    W_* = W_low+W_high.

Here eta E_Z denotes precisely the part beyond Z, which is arbitrarily small; for sufficiently large T eta=1 there, but equality is not needed. Hence M12(W_high)<<T^(29/25+epsilon), including all mixed contributions through the finite L12 triangle inequality.

The exact full restoration is therefore

    B_T=H_X0+U_*+W_low+W_high+E_Z,
    M12(B_T) << T^(max(29/25,b)+epsilon)
       whenever M12(W_low)<<T^(b+epsilon).

The converse inequality at the preferred budget also follows by subtraction. The accepted actual ceiling beta transfers to W_low only by this explicit identity and the independently controlled complements. It was not applied freely to a coefficient mask. A prospective exponent b restores the sharp x-variable moment at max(4,(7+b)/2); the preferred b=29/25 would give 102/25, but b is not proved.

For comparison, optimizing only the elementary head N^(1/4) against the proved Hankel tail gives q=2/3 and gamma=1/6. The bilinear bound meets the trivial head there and does not improve that balance. Its generic twelfth-moment certificate is 5/3. This is weaker than the inherited 10beta; the useful output is the paid localization, not a new complete estimate.

## 4. First doubtful or unproved step

The first missing estimate is a signed physical-radius bound for W_low with exponent b<10beta, preferably b<=29/25. The audited bilinear theorem supplies only a weaker ceiling, and the Hankel identity applies to the complete actual r2 coefficients, not directly to the balanced arithmetic mask. The latter distinction is resolved only for the removed high tail, by subtracting U_high.

A sharp hard norm tail is not claimed. The BV source identity assigns half endpoints and need not have absolutely summable transformed terms after an abrupt cutoff. Replacing the smooth eta by a step without paying boundary Fourier tails would be an unproved step. The fixed smooth decomposition avoids needing that assertion and retains the transition band inside W_low.

## 5. Required controls and outcomes

1. **Square-root degeneracy: PASS.** Proposition 5 excludes individual exponents 0 and 1, not alpha+beta=1. Its hypotheses include alpha=beta=1/2. No nonzero Hessian determinant hypothesis is substituted.
2. **Actual real character and cosine: PASS.** chi4 is real and bounded; the bilinear proof may use a stronger complex theorem, but the result is applied to the original real part. Hankel uses a real test, both oscillatory branches, and the phase -3pi/4 exactly.
3. **Sharp/smooth endpoints: PASS in stated scope.** Adaptive divisor boundaries are one interval after orienting d<=m, and Fourier completion costs O(log M). The new top cutoff is smooth and radius independent; transition integers are owned by the exact complementary multiplier. No sharp-tail bound is inferred.
4. **Transformed zero and near resonance: PASS.** h(0)=0; the Fourier zero term is included and negligible. The possible nearest integer to R^2 contributes the explicit T^(-1/2) term. At exact resonance the leading real kernel is sine, confirming the phase algebra without requiring it for the estimate.
5. **Full norm and frequency ranges: PASS.** Original head, adaptive unbalanced owner, smooth transition, all dual k, n>Z, and every L12 mixed term are explicitly paid. The factor (1+N/T)^(-L) is retained above N=T. No upper-tail result is asserted from an abstract or an unknown inverse constant.
6. **Certificate versus arithmetic lower bound: PASS.** Failure of (K) to beat beta is only a failure of this numerical certificate. It is not a lower bound for the actual signed wave. Conversely, the Hankel argument depends on the complete r2 lattice identity and does not imply the same estimate for arbitrary adversarial coefficients.
7. **Bounded local exponent check: PASS; diagnostic_only.** Python standard-library `fractions.Fraction`, in-memory, checked q=99/125, (1-q)/2=13/125, 1/8+q/16=349/2000, the factor cutoff at q equals361/2100, 1+(20/13)(13/125)=29/25, 10(3/16)=15/8, and (7+29/25)/2=102/25. These are independently displayed rational identities, not numerical evidence for an asymptotic theorem. No numerical sampling was used; analytical work exceeded95%.

## 6. Dependencies and exact artifacts used

Only the assigned brief/context, the two named accepted graph nodes, cited primary sources, and the subsequently authorized Round205 section5 and Round208 section1 provenance checks were used. The campaign file remains the closed Round230 status; the present work is a bounded prelaunch continuation as explicitly stated by its interface. The conductor supplied the KRW primary link during source screening; this did not supply a proof. A later conductor message about its own prospective two-sided band was not needed in this report. After the independent Hankel derivation was completed, the conductor identified the older provenance and authorized those exact additional sections; they confirm that neither the tail nor the norm-band principle is new. No sibling report or new source-derived theorem beyond Applications A and B was used.

Local SHA256 provenance:

- `protocol.md`: `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`.
- `state/proof_obligations.yml`: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`; only `GC-complete-square-root-large-values-moment-bound` and `GC-complete-distinct-radical-twelfth-reduction` were inspected as mathematical nodes.
- `state/active_campaign.yml`: `fd65ce5c6b117aa4ca8ed097f85e2c786621c8054ca81791aa6e5e17006a82fa`.
- `strategy/round231_balanced_cancellation/briefs/balanced_source_audit.md`: `4b194e2cf35dfe137f568ababf4e95fa94b952e66ccff2b6869c59fcbf78bd4a`.
- `strategy/round231_balanced_cancellation/briefs/balanced_interface.md`: `cb6f283b2de16774ff946c450acabd61001b39c39ba58c6e2ab719c14050e055`.
- `strategy/round231_residual_saving/conductor_adaptive_factor_cutoff.md`: `02727c91e64931a13d3707ca15df021418d3e96510e35894e0d96a70182506fa`.
- `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`: `942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212`.
- `strategy/gauss_circle_strategy_checkpoint_round205_2026-09-26.md`, section5 only: `03e05b85fcb0fc72fe0e65869f13e33763fea3dc503e9a85d6d1e883eebdcfc4`.
- `strategy/gauss_circle_strategy_checkpoint_round208_2026-09-27.md`, section1 only: `ae22a1a096a380b28b4b409a478dd7f87e5b1d8727068a4231ceb31272e03cbf`.

The complete-moment kernel is used for its coefficient-uniform finite distribution proof and fixed twelfth-moment restoration, not to assert that its actual supremum applies to arbitrary masks. The second graph node supplies only the accepted preferred complete target and its open status. External source details and precise theorem locations appear in Section 2; the claims here do not rely on secondary abstracts.

## 7. Recommended state effect

**Retain** the independent source verification of the inherited smooth actual high-norm-tail lemma and its combination with the recent adaptive W_* mask, pending the assigned nonauthor seam review. Do not count the old tail or norm-band localization as a new mechanism or analytic gain. **Retain** the KRW application as an exact quantitative no-gain comparison. **No change** to accepted complete moments, beta, M9, M1/M2, or the quarter theorem. This report edits only its assigned path, proposes no successor, and stops for conductor adjudication.
