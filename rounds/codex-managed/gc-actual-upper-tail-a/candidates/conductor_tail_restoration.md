# Round231 conductor: complete target A restoration and arithmetic controls

Campaign `gc-actual-upper-tail-a`; round231; conductor derivation for nonauthor review; generated2026-10-11 UTC. Graph SHA256 `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`. This is candidate round evidence, not accepted graph mathematics.

## 1. Result

The frozen target A, or its integrated alternative, suffices for the complete twelfth-moment bound32/25. The unchanged second distribution term fits with room to spare; the proposed first saving1/100 has only a small positive margin. Neither an odd real resonance kernel nor the exact character identities below proves this saving. The arithmetic identities distinguish two-adic sectors and identify an actual weighted many-product estimate as the unresolved seam.

## 2. Exact statement and hypotheses

Use precisely `briefs/actual_interface.md`: gamma=16/125, X=T^(64/125), Y=T^(93/125), actual radius-independent smooth band F, unnormalized measure dmu=w(R/T)dR, and B=L+F+H. Let beta=(50sqrt(1717)-297)/13762. The separately reviewed complementary supremum bounds are T^(gamma+epsilon); their complete twelfth moments have exponent m(gamma)=max(1,10gamma,1+20gamma/13). The accepted actual B ceiling and this exact decomposition imply the actual F ceiling T^(beta+epsilon). This inference does not assert a ceiling for arbitrary masks.

The hypothetical pointwise tail is D_F(V)<=C_epsilon T^epsilon[T^(-1/100)V^-2+T V^(-136/13)] for V>=V0=T^gamma. The weaker sufficient hypothesis is12 integral_(V0)^infinity V^11 D_F(V)dV<=C_epsilon T^(32/25+epsilon). Both are OPEN.

For the separate finite arithmetic identities, h,h' are positive integers, q,q' odd integers, g=gcd(h,h'), h=g a, h'=g b, gcd(a,b)=1, and r=aq-bq'. No coefficient or radius assumptions are needed for these identities.

## 3. Proof and complete ledger

### A. All amplitudes and both tails

Layer cake for the nonnegative function |F| gives M12(F)=12 integral_0^infinity V^11D_F(V)dV. Below1 the measure bound O(T) pays O(T). Between1 and V0 the accepted generic distribution pays

    O(T^epsilon[V0^10+T V0^(20/13)]).

Thus the complete low contribution has exponent max(1,10gamma,1+20gamma/13)=32/25. If a truncated event moment is used instead, its extra boundary term V0^12D_F(V0) obeys the same budget; it may not be dropped without this payment.

At large amplitudes truncate at the independently proved actual F ceiling C_delta T^(beta+delta). Integrating the two target-A terms separately yields exponents

    10beta-1/100 =1.279663519481228...,
    1+20beta/13 =1.198409772227881... .

Both are strictly below32/25. Choose the small internal epsilons/delta in terms of the final epsilon (and, if needed, the fixed positive margins); constants in the ceiling are harmless. This proves the integrated alternative conditional on target A. Conversely, the integrated alternative alone and the already paid low range suffice for M12(F)<=T^(32/25+epsilon).

The finite L12 norm inequality applied to B=L+F+H then restores M12(B)<=T^(32/25+epsilon). H contains the full infinite norm tail, and L/H contain the smooth transition regions exactly. If F=C+U is used, pay U at the same exponent before restoring B. Equality of moment targets at this budget does not transfer the literal distribution estimate at V=V0: a correction O(T^(gamma+epsilon)) need not be <=V/2 there.

The first-tail minimum saving is10beta-32/25=0.009663519481228... . The proposed1/100 exceeds it by0.000336480518771... . At the accepted sharp-moment-to-pointwise bridge a complete exponent b produces (7+b)/26; b=32/25 gives207/650, which is larger (weaker) than the accepted theta=(1+beta)/4. This milestone is a moment improvement only. No stronger pointwise claim is admissible.

### B. Same and different two-adic sectors

If a,b are odd, r is even. Multiplying aq-bq'=r by aq modulo4 gives

    1-abqq' =r aq (mod4).

Since r is even and aq odd, r aq=r (mod4). Hence chi4(ab)chi4(q)chi4(q')=(-1)^(r/2), and therefore

    chi4(q)chi4(q')=chi4(ab)(-1)^(r/2).

The arithmetic sign is constant at each fixed r. Exact coincidence r=0 requires q=bk,q'=ak with k odd, and has character sign chi4(ab). This is a character-pair identity, not a positivity assertion about the full weighted analytic covariance. Amplitudes, kernels and restrictions still have to be included.

If a,b have different parity, r is odd for any odd solution. The odd solutions, if present, form a progression (q,q')=(q0+2b j,q0'+2a j). Their character products change by (-1)^(a+b)=-1 at each step. Thus for a finitely supported weighted progression c_j the character sum is bounded by sup|c_j| plus its discrete total variation, by summation by parts and bounded partial sums of (-1)^j. This is potentially useful in that sector, but there is no assertion that every actual restricted progression is long or has small variation. The same-two-adic sector remains.

Finally, if every factorization of a positive integer p is included with unit weight, sum_(h q=p,q odd)chi4(q)=sum_(q|p)chi4(q)=r2(p)/4. This full-product identity cannot replace the actual incomplete smooth weighted product family. Applying it without the weights would return to the original arithmetic coefficients rather than prove the desired saving.

### C. Scope of the controls

The real-phase identity is chi4(d)e(qd/4)=i chi4(q)1_(d odd), q odd. With Delta=R^2-hq the real stationary contribution has the signed sine form in the frozen interface. Exact Delta=0 therefore vanishes, while allowed real detuning can give coherent size T^-1/2 per fibre. Negative cosine frequencies are conjugates, not a second independent source of cancellation. Each frequency needs one q owner or an explicit partition; coincident labels cannot be counted as new terms.

The character identities in B survive actual integer specialization, but no positive high-moment lower bound follows from them. Likewise the independently assigned blind odd-kernel problem concerns general centers and coefficients; it can test an inference from oddness, but cannot establish an actual arithmetic lower bound. These distinctions are essential when judging the attempted target.

## 4. First doubtful or unproved step

Target A and its integrated alternative remain unproved. Neither constant character signs along a fixed product difference nor alternating signs in a different two-adic sector controls the actual weighted union of many product centers on the high-value set. The generic Gram proof's first V^-2 term remains unchanged without such input. A first-moment cancellation against a slow radius test does not bound positive twelfth moments. No failure of the frozen target itself has been proved.

## 5. Required control and outcome

`controls/exact_controls.py`, run with Python using exact integers and rational arithmetic, passes:49,664 same-sector identities;97,792 mixed-sector alternations;680 exact coincidences;512 complete-factor versus literal lattice identities;528 Gaussian-integer real-phase checks. Rational enclosures of beta certify both target-A margins and the32/25 ledger. Outputs are in `controls/exact_controls.json`, explicitly diagnostic_only. These tests supplement the algebra above and do not certify an asymptotic tail estimate.

## 6. Dependencies and exact artifacts used

- `protocol.md`, `state/proof_obligations.yml`, `state/active_campaign.yml` and `briefs/actual_interface.md`.
- `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`: actual complete ceiling, coefficient-uniform distribution, tail treatment and sharp bridge.
- `strategy/round231_balanced_cancellation/conductor_combined_owner.md` and `conductor_seam_repairs.md`: exact smooth complements, cutoff ownership and repaired real phase.
- `strategy/gauss_circle_upper_tail_strategy_2026-10-11.md`: adopted target A and its complete implication.
- `controls/exact_controls.py` and its JSON output. No newly imported external theorem or web claim is used.

## 7. Recommended state effect

Retain the conditional restoration and scoped arithmetic controls as reviewed round evidence, subject to nonauthor review. Unless the discovery report closes the actual quantitative seam, apply an identity State Patch, leave the graph and proof draft unchanged, and close the bounded attempt honestly. This report does not authorize a successor round.
