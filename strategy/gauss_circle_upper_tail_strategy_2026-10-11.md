# Upper-tail strategy after the Round231 review

Conductor strategy supplement, 11 October 2026. Input: `strategy/round231_strategy_review_2026-10-11.md`. Read together with checkpoint230 and `gauss_circle_strategy_directive_reconciliation_2026-10-11.md`; this supplement supersedes their generic next-task wording, not their accepted mathematics or source qualifications. Graph SHA256: a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.

## Decision and useful changes

Select the review's actual-coefficient upper-tail estimate A as the first candidate for a bounded exploratory round. Work first with the smooth full norm band F_(16/125), retaining the real reciprocal signs during the radius analysis. This is more specific than asking for an unspecified new moment inequality, and its complete implication can be checked before trying to prove it. Estimate B remains the stronger, separate pointwise-improvement milestone.

The changes are:

- Prefer the smooth full band when its exact r2 divisor identity and smooth amplitude simplify Poisson summation. Use the factor-restricted central component when its arithmetic restrictions help; pay the change of representation in the moment norm.
- Concentrate on the amplitude range above T^(16/125), up to the independently proved actual ceiling T^(beta+epsilon), instead of requiring an improvement at every amplitude or for every individual fibre.
- Track both terms of the large-value estimate. Improving only V^-2 is sufficient for the modest milestone but insufficient for the stronger one under the current calculation.
- Permit a precise conjectured lemma to motivate exploration when it has a mathematical mechanism, a complete conditional implication and genuine falsification tests. Proof of that lemma is required for promotion, not for beginning an attempt.

No estimate A or B is proved by selecting it. This user-requested strategy update launches no analytic campaign; Round231 remains pending design with its objective now narrowed to an explicit exploratory candidate.

## 1. Exact working quantity and representation choice

Keep the fixed real radial mollifier, its real Schwartz transform Psi, and nonnegative window w, large enough for sharp-discrepancy restoration. Define the complete real wave and unnormalized measure by

    B_T(R)=sum_(n>=1) r2(n)n^(-3/4)Psi(sqrt(n/T))
                      cos(2pi R sqrt(n)-3pi/4),
    dmu_T(R)=w(R/T)dR,  M12(F)=integral |F|^12 dmu_T.

Let theta=(3292+25sqrt(1717))/13762 and beta=2theta-1/2. The accepted complete exponent remains10beta=1.289663519481... . For fixed13/125<=gamma<beta, use the exact cutoffs from the reviewed combined-owner packet:

    X_gamma=T^(4gamma), Y_gamma=T^(1-2gamma),
    phi_gamma(n)=eta(n/X_gamma)-eta(n/Y_gamma),
    F_gamma=sum_n phi_gamma(n)r2(n)n^(-3/4)Psi(sqrt(n/T))
                    cos(2pi R sqrt(n)-3pi/4).

Exactly F_gamma=C_gamma+U_gamma and B_T=L_gamma+F_gamma+H_gamma. C_gamma retains d,m>=T^(2gamma-13/42)x(n)^(29/84), the original radius-independent patch starts and literal cutoff equalities. The existing reviewed estimates pay L,H,U at

    m(gamma)=max(1,10gamma,1+20gamma/13).

Thus a moment bound at any exponent b>=m(gamma) for either F_gamma or C_gamma restores the same complete B_T bound; conversely the complete bound implies either component bound at that budget. This is equivalence of upper bounds, not equality of moments or equality of their level sets.

The finite coefficient-uniform Gram argument in the accepted kernel applies because both coefficient vectors are fixed as R varies and divisor bounded on each dyadic block. It gives

    D_F(V):=mu_T{|F|>V} << T^epsilon(V^-2+T V^(-136/13)), V>=1.

The actual ceiling ||F_gamma||infinity,||C_gamma||infinity<<T^(beta+epsilon) follows separately from the exact decompositions, the full actual ceiling and the independently paid complementary ceilings. It is not inherited by arbitrary masks. The combined-owner packet remains reviewed evidence; this supplement does not promote it to the graph.

Do not transfer a literal tail estimate between F and C without checking the correction. From F=C+U one has D_F(V)<=D_C(V-s)+D_U(s) for0<s<V. A moment bound for U does not make its level sets disappear; even ||U||infinity<<T^(gamma+epsilon) is not a fixed fraction of V at V=T^gamma. The strategy only needs the proved moment restoration, so no such tail equivalence is assumed.

## 2. Conditional tail targets and complete budgets

Freeze a representation when launching an attempt. The preferred first choice is the literal F_gamma above. The proposed estimates below must hold for every epsilon>0, uniformly over real T>=2 and V>=T^gamma, with constants allowed to depend on the fixed functions and epsilon.

**Target A, modest complete moment improvement.** For gamma=16/125, seek

    D_F(V)<<T^epsilon[T^(-1/100)V^-2+T V^(-136/13)].

**Target B, pointwise-improvement milestone.** For gamma=13/125, seek

    D_F(V)<<T^epsilon[T^(-13/100)V^-2+T^(24/25)V^(-136/13)].

Both are open sufficient targets, not necessary formulations. In general a proposed upper-tail bound

    D_F(V)<<T^epsilon[T^-a V^-2+T^(1-d)V^(-136/13)]

combined with the old distribution below V0=T^gamma and the actual ceiling gives the sufficient complete exponent

    b=max{m(gamma), 10beta-a, 1-d+20beta/13}.

Proof: layer cake is M12(F)=12 integral_0^infinity V^11 D_F(V)dV. Below1 the measure is O(T); from1 toV0 the old estimate contributes T^(10gamma)+T^(1+20gamma/13). AboveV0 the improved terms integrate to T^(10beta-a)+T^(1-d+20beta/13). Use a ceiling C_delta T^(beta+delta) with delta chosen sufficiently small relative to the requested output epsilon; all constants, logarithms and ceiling losses are then absorbed. Restore the complementary pieces by the finite L12 norm inequality. No ceiling is assumed at the exact exponent without epsilon.

| Target | Low/complement budget | First high-tail exponent | Second high-tail exponent | Complete consequence if proved |
|---|---|---|---|---|
| A |32/25|10beta-1/100=1.279663519481...|1+20beta/13=1.198409772228...|M12(B_T)<<T^(32/25+epsilon)|
| B |29/25|10beta-13/100=1.159663519481...|24/25+20beta/13=1.158409772228...|M12(B_T)<<T^(29/25+epsilon)|

For a target b with m(gamma)<=b, this calculation needs a>=10beta-b and d>=1+20beta/13-b, with negative requirements replaced by zero if only nonnegative savings are considered. A needs a>=0.009663519481... and no saving in the second term. B needs a>=0.129663519481... and d>=0.038409772228... . The displayed choices leave positive margins. In particular, retaining the second term unchanged caps the present B calculation at1.198409772228..., above29/25 and even above the strict pointwise threshold1.176562575326... . This limits that calculation, not the actual moment.

A weaker sufficient objective is

    12 integral_(T^gamma)^infinity V^11 D_F(V)dV
       <<T^(m(gamma)+epsilon).

This equals the integrated excess integral (|F|^12-T^(12gamma))_+ dmu_T. For the actual restricted high moment also include the boundary term T^(12gamma)D_F(T^gamma); the old distribution pays it at m(gamma). A level-dependent saving or a direct signed moment proof that reaches this budget is equally acceptable. Do not demand the stronger uniform A/B formulation after a weaker complete proof succeeds.

A would be a complete moment gain only: its persistence consequence207/650 exceeds the existing theta. B would give102/325, which beats theta. The quarter route still requires an unbounded sequence of fixed even orders with complete b_p=o(p); the accepted distinct-radical reduction remains twelfth-order only.

## 3. First mechanism to investigate

Use smooth factor rectangles DM comparable to N and retain real amplitudes. The corrected Poisson term has

    I_h(d)=b_h(d)e(R^2d/(4h)-1/8)+error,
    h comparable to RD/sqrt(N).

The original real circle shift is e(-3/8), so their product makes the real leading term -Re sum_d chi4(d)b_h(d)e(R^2d/(4h)). For an odd integer q, h>0 and Delta=R^2-hq, exact residue algebra gives

    chi4(d)e(qd/4)=i chi4(q) 1_(d odd),
    -Re sum_d chi4(d)b_h(d)e(R^2d/(4h))
      =chi4(q) sum_(d odd) b_h(d)sin(pi Delta d/(2h)).

This identity is for the real leading stationary term. Keep the conjugate branch and original cosine normalization consistent, and retain higher Bessel terms, stationary errors, nonstationary frequencies and all rectangle weights in the complete expression. At Delta=0 it vanishes; detuning of order h/D need not be small. The relevant near-product width is h/D comparable to T/sqrt(N), corresponding locally to a radial width comparable to N^(-1/2). These windows can be correlated; their width alone is not a large-value estimate.

The mechanism is a hypothesis about cancellation in the aggregate over frequencies and radii, not a claimed symmetry of individual near-products. No independence, reflection pairing or uniform fibrewise square-root bound is available. If q is chosen locally to be near R^2/h, specify a unique partition and its boundaries before summing over q; the identity for an arbitrary odd q does not license summing all q copies of the same fibre. Use a sine Taylor estimate only in its justified small-detuning range.

The first attempt should produce an inequality for the actual exceptional-radius set or its integrated twelfth tail, including all scales and errors. Exact resonance zeros, a product count after absolute values, or applying Poisson back to the original expression are not themselves that inequality. A failure must identify the first unproved correlation or the cost that exhausts the required saving, without asserting a lower bound for the actual complete moment.

## 4. Exploratory admission and stopping rule

The review correctly separates admission to exploration from acceptance of mathematics. Target A has a precise actual quantity, a small positive required saving, an exact conditional complete implication, a candidate real-phase mechanism and existing falsification controls. That is enough to select it for bounded exploratory design. Its truth need not be known beforehand. Any promotion still requires a complete proof, independent seams, controls, dependency closure and a valid State Patch.

When an analytic round is subsequently launched, freeze one objective: improve the actual upper tail sufficiently to reach32/25, or determine precisely why the tested aggregate mechanism fails. Use at most three orthogonal roles for the signed aggregate estimate, hostile controls and full restoration. The controls must include exact resonance, physical detuning, literal real radii, correction thresholds, both distribution terms, repeated/squarefree-class dependence, nonstationary errors and all norm scales. Numerical work can only falsify or diagnose and remains at most20 percent; plan95/5. Reassess after at most two attempts on unchanged premises. A changed representation without a new inequality does not reset that count.

Decoupling remains available for the actual exceptional-radius measure, with cap/tube concentration and restriction from an auxiliary space to the radial trace explicitly paid. Probabilistic or inverse arguments must preserve the fixed lattice's arithmetic and give quantitative control at V growing with T. The existing all-polynomial and coefficient-energy obstructions keep their scoped meanings; they do not prohibit physical-phase or direct-moment arguments. Kloosterman and cusp/spectral routes remain reserves requiring exact matched inputs and complete budgets. No new external dependency is imported here.

The incoming review reports a source-version retrieval discrepancy. It has no role in the elementary tail calculations or the selected mechanism. Do not resolve it by treating either a failed fetch or a secondary index as a theorem audit; recheck the exact primary version if a future attempt uses that source. Existing source qualifications remain unchanged.

## 5. State and evidence

Evidence is archived in `strategy/round231_tail_strategy_review/`: an isolated tail-restoration report, an actual-representation/phase audit, independent strategy review, exact diagnostics and preservation validation. The strategy and next-round workflow change; the graph, proof draft, accepted kernels, closed Round230 manifest, validation matrices, ledger, incoming review and previous strategy packets remain unchanged. No complete estimate, pointwise improvement, State Patch or analytic launch is asserted.
