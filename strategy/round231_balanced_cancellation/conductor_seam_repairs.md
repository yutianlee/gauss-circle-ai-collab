# Conductor reconciliation of the frozen reports

Round231 central-balanced packet; 2026-10-11. This attachment governs the use of the original reports, which remain byte-for-byte frozen. It records the localized corrections identified by the nonauthor reviews in the packet's single review/repair cycle. None is a new complete estimate or a State Patch.

## 1. Result and exact scope

The reciprocal rectangle bound and the source comparison remain valid. Replace the endpoint logarithm in the reciprocal proof by log(2+D). Interpret its exact quarter-frequency example as a complex-fibre control only. A small physical detuning supplies the corresponding real-fibre control. In the source report, restore the complementary moment budget before converting a residual exponent to the sharp x-variable exponent.

These repairs leave the packet's no-complete-gain conclusion unchanged. They do not assert any lower bound for the whole balanced wave or its twelfth moment.

## 2. Reciprocal logarithm at the allowed endpoint

The hypotheses of reports/balanced_reciprocal_attack.md allow D>=1/2. Its equation(13), and references to that expression, are to be read as

    sum_(h~H) min(D, ||R^2/(4h)+sigma/4||^(-1))
      << T^epsilon [H log(2+D)+D].

For D>=2 the displayed proof by dyadic distance classes is unchanged. For 1/2<=D<=2, each summand is O(1), and the O(H) frequencies are covered because log(2+D) is bounded below by a positive constant. This fixes the vanishing log(2D) at D=1/2. Multiplication by A0 still gives T^epsilon[(T/N)^(1/2)+T^(-1/2)].

## 3. Real phase and a physical detuning

Use the exact convention e(t)=exp(2pi i t), positive real nonnegative amplitude, and the reciprocal stationary term

    I_h(d)=b_h(d)e(alpha_h d-1/8)+error,
    alpha_h=R^2/(4h),
    b_h(d)=a(d,R^2d/(4h^2))R sqrt(d)/(sqrt(2)h^(3/2)).

The circle wave takes Re(e(-3/8) times the complex exponential sum). Thus this real leading contribution equals

    -Re sum_d chi4(d)b_h(d)e(alpha_h d).

At alpha_h=k+1/4, chi4(d)e(d/4)=i for odd d and zero for even d. The sum is purely imaginary, so the real leading term vanishes exactly. The frozen report's modulus counterexample is correct for the complex character fibre; it must not be read as a nonzero real exact-resonance contribution. The second Bessel term, where relevant, is a separate term and is not killed by this leading-order identity.

For a real counterexample to uniform individual-fibre square-root cancellation, fix c=1/32, a positive L congruent1 modulo4, h=L, and choose

    R^2=L^2+4Lc/D.

Then R~L is an admissible real radius, alpha_h=L/4+c/D, and the stationary point is

    v_h=(1/4+c/(LD))d.

Choose smooth nonnegative rectangle weights with d in [D,2D], m comparable to D/4, and b_h comparable to A0 on a fixed interior d interval of length comparable to D. The stationary line stays in that support for large L,D. The real leading term is exactly

    sum_(d odd) b_h(d) sin(2pi c d/D).

On [D,2D], the sine is bounded below by the positive constant sin(pi/16). Hence this contribution is comparable to A0 D as D tends to infinity, contradicting a uniform O(A0 D^(1/2+epsilon)) bound for any fixed epsilon<1/2. The fixed-h stationary error is smaller by O(H^(-1)) in the report's normalization. T can be set to L, and a central norm scale such as N comparable to T^(2/3), D comparable to sqrt(N), places both factors above the adaptive cutoff. Thus no inadmissible complex radius or factor regime is required.

This is an obstruction to bounding every real individual reciprocal fibre by square-root size. The contribution A0 D is only comparable to T^(-1/2). Other h, other rectangles, and the R integral are not controlled from below. In particular, this does not obstruct cancellation across reciprocal frequencies, nor prove a full-wave or moment lower bound.

The statement in conductor_combined_owner.md that quarter-frequency resonances survive the character expansion is to be understood in this precise sense: they are present in the complex expansion; exact resonance has the real leading cancellation just computed, while nearby frequencies can be real-coherent. Taking the absolute value of each complex fibre discards that distinction.

## 4. Complementary owners in sharp-moment restoration

In reports/balanced_source_audit.md section3D, let b_low denote a hypothetical bound M12(W_low)<<T^(b_low+epsilon). The independently paid complementary owners have exponent29/25. The full B exponent therefore is

    b_full=max(29/25,b_low).

Under the inherited sharp discrepancy conversion, the x-variable moment exponent is consequently

    max(4,(7+b_full)/2)=max(102/25,(7+b_low)/2).

The expression max(4,(7+b)/2) is usable only when b already denotes the restored full exponent, or when b>=29/25. At the preferred endpoint b_low=29/25, the exponent102/25 is unchanged. No claim about a smaller residual exponent can silently discard this complementary floor.

## 5. Controls and first unproved step

The endpoint repair is proved by a bounded-D case split. The real-phase control is an exact algebraic identity followed by a positive sine bound, independently rederived by the nonauthor reciprocal reviewer. The source-restoration correction was independently derived by the source reviewer using the full L12 norm inequality and x=R^2. The local finite controls separately verify the Gaussian-integer quarter-frequency identity and exact rational exponents; they are diagnostic, not asymptotic proof.

The first unproved step remains a signed estimate for the actual central balanced owner at a complete exponent below10beta. None of these repairs supplies it.

## 6. Dependencies and state effect

- reports/balanced_reciprocal_attack.md, frozen SHA256 fa63868418be5c8d24d30284394976fa3e0f1df077117dc3a9227441d55cf61f.
- reports/balanced_source_audit.md, frozen SHA256 bd7beaa816e2443be41aaed903e92c8b884b1b827b1ea5b2fb1eb9004b0e9cd7.
- reviews/review_reciprocal_signs.md for the endpoint, real-phase, stationary, and inherited-mask seams.
- reviews/review_source_application.md, SHA256 39a778d3ddcf1acdd25b21be6206bd86559c4abef1067cb781056cdfa64d68a4, for the source and complementary-budget correction.
- conductor_combined_owner.md and reviews/review_hankel_and_owner.md for the exact full owner ledger and its independently paid terms.

Recommended effect: revise the scope of the frozen evidence by this attachment; retain the corrected estimates and scoped controls. No accepted graph mutation, proof-draft revision, complete gain, or analytic campaign launch.
