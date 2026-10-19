# Actual close-product payment and the remaining signed energy

Round232; campaign `gc-upper-tail-separated-products`; task `actual_near_product_payment`; role `formalizer`, selected-context claimant. Generated2026-10-11 UTC. Starting graph SHA256 `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`. Candidate evidence only. No current-round sibling report was read.

## 1. Result: the collision payment is valid, with an explicit cutoff limit

The candidate close-product payment is proved for the **all-q second-Poisson packets**, grouped over every smooth divisor rectangle before taking products. Write gamma=16/125, E={|F|>T^gamma}, and W=T^(1-2gamma), allowing a fixed enlargement of W. For every real L>=0,

    C_L(E):=integral_E sum_(|p-p'|<=L) |P_p(R)P_p'(R)| dmu
        <<_epsilon T^(-4gamma+epsilon) min(L+1,W).       (1)

All p,p' are nonzero integers; negative and arbitrarily large positive modes are included. Consequently,

    C_0(E)<<T^(-64/125+epsilon),
    C_(sqrt(T))(E)<<T^(-3/250+epsilon).                 (2)

The latter is smaller than T^(-a*), where a*=10beta-32/25=0.009663519481... . Exterior/negative modes, their cross terms with retained modes, cross-rectangle terms, real endpoints, and the selected-set stationary error are paid below.

The largest power cutoff justified by (1) at the requested budget is

    L<=T^(ell*), ell*=4gamma-a*=224/125-10beta
                      =0.502336480519... .              (3)

Equality is allowed with the usual epsilon loss. Strict power slack requires an exponent below ell*. This is the largest cutoff **furnished by this envelope-and-measure proof**, not a theorem that every larger cutoff fails for the actual arithmetic family.

For the all-product one-sided remainder

    R_L(E)=2 sum_(p<p',p'-p>L) integral_E P_p P_p' dmu,

the exact reduction at L=sqrt(T) is

    Q_E(F)=R_L(E)+O_epsilon(T^(-3/250+epsilon)).         (4)

Thus the requested one-sided bound R_L(E)<<T^(-a*+epsilon) is sufficient for the complete32/25 moment and, at this energy interface, equivalent to Q_E(F)<<T^(-a*+epsilon). That separated bound remains unproved. The near-band form is not positive semidefinite; the proof uses absolute payment, not positivity.

## 2. Exact statement and hypotheses

Use the literal F, fixed rho,Psi,eta,w, and dmu=w(R/T)dR in the frozen actual interface. In particular R lies in [T/2,2T], T is any real number at least2, X=T^(64/125), Y=T^(93/125), and

    F(R)=sum_n [eta(n/X)-eta(n/Y)]r2(n)n^(-3/4)
                   Psi(sqrt(n/T))cos(2pi R sqrt(n)-3pi/4).

The actual exceptional set is E={R in supp(w(R/T)):|F(R)|>T^gamma}. It is never replaced by a packet event, a rectangle event, or a smooth test. The accepted generic distribution and reviewed actual ceiling give

    mu(E)<<T^(-2gamma+epsilon),
    Q_E(F)<<T^epsilon,
    ||F||infinity<<_delta T^(beta+delta),
    beta=(50sqrt(1717)-297)/13762.                     (5)

Only the first two statements are needed to prove (1)-(4). The ceiling is used for the complete moment implication.

Use the reviewed exact second-Poisson representation

    F(R)=S(R)+e_T(R), S(R)=sum_(p!=0)P_p(R),
    P_p=sum_j P_(j,p), ||e_T||infinity<<T^(-1/2+epsilon),
    P_(j,p)=4T^(-1/2)
       sum_(h~H_j,h|p,p/h odd) chi4(p/h)
                    K_(j,h,R)((R^2-p)/W_j),            (6)
    W_j=T/sqrt(N_j), H_j=T D_j/sqrt(N_j).

Here h is a positive integer in a fixed enlarged interval; q=p/h is any odd integer, including negative q. There are O(log^2 T) rectangles, D_jM_j~N_j, and cX<N_j<CY with fixed c,C. Each K is a real odd Schwartz kernel with uniformly bounded fixed seminorms. Its explicit normalization is

    b_(j,h)(d,R)=a_j(d,R^2d/(4h^2))
                       R sqrt(d)/(sqrt(2)h^(3/2)),
    K_(j,h,R)(u)=(sqrt(T)/2) integral
             b_(j,h)(d,R)sin(pi W_j u d/(2h)) dd.

The amplitude a_j does not contain the divisor factor4. This factor appears once in (6). Both cosine branches are already contained in the real representation. No nearest-q relabeling is substituted for this all-q identity. The old hostile report's nearest-q packets are a different grouping; its local envelope is not silently assumed globally here.

For sufficiently large T all W_j>=1, and W_j<=C_0 W where W=T^(1-2gamma). A fixed enlargement can be absorbed in W in every estimate. The bounded remaining T range is covered by enlarging constants. Constants may depend on fixed cutoffs, fixed Schwartz seminorms, and epsilon, never on T,L,R or integer endpoints.

## 3. Proof and derivation

### 3.1 Global packet envelope from the exact all-q formula

The smooth-symbol estimate gives |b_(j,h)|<<T^(-1/2)D_j^(-1), with d support of length O(D_j) and derivatives costing powers D_j^(-1). Changing d=D_j t in K leaves an O(1) smooth compact symbol and a frequency comparable to u because W_jD_j/h~1. Integration by parts proves, for every fixed B,

    |K_(j,h,R)(u)|<<_B (1+|u|)^(-B).

This estimate is valid for every real u, not merely the closest-q cell. The fixed h interval, including h whose stationary point is outside the smooth support, introduces no moving discontinuity.

For p!=0 the number of eligible positive divisors h is at most d(|p|). Hence, for any eta>0 and B,

    |P_(j,p)(R)|<<_(B,eta) T^(-1/2)|p|^eta
                            (1+|R^2-p|/W_j)^(-B).      (7)

This is a global estimate, including negative and unbounded p. Put s=R^2. Since s<=4T^2 and W_j<<T^2,

    |p|<=s+|s-p|<<T^2(1+|s-p|/W_j).

Choose B>A+eta. Equation (7) then gives

    |P_(j,p)(R)|<<_(A,eta) T^(-1/2+2eta)
                             (1+|s-p|/W_j)^(-A).

Sum the O(log^2 T) rectangle envelopes and take eta small relative to the eventual epsilon. With P_0=0 and f_W(t)=(1+|t|/W)^(-A), this proves

    |P_p(R)|<=C_(A,epsilon) T^(-1/2+epsilon)f_W(s-p)
                              for every integer p.     (8)

There is no appeal to d(p)<<T^epsilon outside p~T^2: the extra |p|^eta was explicitly absorbed using additional decay. This is the exterior-mode seam missing from a purely local packet statement.

For A>1 and W>=1, comparison with unit intervals, uniformly in real s, gives

    sum_(p in Z) f_W(s-p)<<_A W,
    sum_(p in Z) f_W(s-p)^2<<_A W.                     (9)

For example partition |s-p| into [0,W] and [kW,(k+1)W]; each shell has O(W) integers and the resulting p-series converges. Thus

    sum_p |P_p|<<T^(-1/2+epsilon)W,
    sum_p |P_p|^2<<T^(-1+epsilon)W.                    (10)

All countable sums and their squared expansions converge absolutely and uniformly over the radius window. Integrating their expansions over the actual measurable E is therefore legitimate. Cross-rectangle contributions are present in |sum_j P_(j,p)|^2; using (8) costs only fixed powers of log T. They are not dropped or counted as orthogonal.

### 3.2 Explicit exterior/negative tail and its mixed terms

Although (8)-(10) let us retain every p, one may remove the fixed exterior

    O_T={p!=0:p<T^2/8 or p>8T^2}.

Every negative p is in O_T. For s in [T^2/4,4T^2], every exterior point is at distance at least cT^2 from s. The lattice tail estimate from (8) yields

    sum_(p in O_T)|P_p(R)|
       <<T^(-1/2+epsilon)W(T^2/W)^(-(A-1))
       <<T^(1/2-2gamma+epsilon-(A-1)(1+2gamma)).         (11)

The exponent tends to minus infinity with A. Thus this exterior l1 tail is O_K(T^(-K)) for every fixed K. The full l1 envelope in (10) has only polynomial size. The sum of absolute products with at least one exterior index is bounded by twice the exterior l1 tail times the full l1 sum. Its integral over E, or even the entire O(T) radius window, is therefore O_K(T^(-K)) after increasing the input decay order. This pays exterior-exterior and exterior-interior terms, whether near or separated. Real boundaries of O_T require no integer rounding convention: use the displayed inequalities and the same lattice estimate.

### 3.3 Close-band absolute payment and every product collision

Fix R and put a_p=|P_p(R)|. Let m=floor(L). The elementary inequality 2a_pa_p'<=a_p^2+a_p'^2 gives

    sum_(|p-p'|<=L)a_pa_p'
          <=(2m+1)sum_p a_p^2
          <<(L+1)T^(-1+epsilon)W.                    (12)

The sum is over ordered pairs, so (12) owns the diagonal once and every off-diagonal twice, exactly as the expansion of S^2 requires. The alternative bound by (sum_p a_p)^2 is O(T^(-1+epsilon)W^2). Combining both,

    sum_(|p-p'|<=L)|P_pP_p'|
          <<T^(-1+epsilon)W min(L+1,W).              (13)

Multiplication by the actual set's measure (5) proves (1), because W/T=T^(-2gamma). This applies to an arbitrary measurable set with the stated measure; no smoothness, reflection symmetry, bounded variation or independence of E is used.

At L=0, (13) pays |P_p|^2, which includes every h,h' coincidence and every cross rectangle at the same integer product p. No oddness cancellation is needed. At L=sqrt(T), the exact exponent is

    -2gamma+1/2+(1-2gamma)-1
        =1/2-4gamma=1/2-64/125=-3/250.

Since 3/250-a*=0.002336480519...>0, this payment lies strictly below the desired energy. For L=T^ell with 0<=ell<=1-2gamma, the paid exponent is ell-4gamma, which gives (3). For larger L the absolute bound saturates at T^(1-6gamma+epsilon)=T^(29/125+epsilon), not at a useful negative power.

The W(L+1) order in (12)-(13), when 1<=L<<W, is sharp for the pointwise envelope class: take cW consecutive integer indices on a shoulder where one nonzero real odd Schwartz K is bounded away from zero, and set a_p=T^(-1/2)|K((s-p)/W)| there. At least c'W(L+1) ordered pairs have both amplitudes comparable to T^(-1/2). The construction can persist on a real s interval of length c''W. This is a generic envelope control, not an actual r2 lower bound and not a counterexample to a larger-cutoff arithmetic theorem.

### 3.4 Stationary errors on E and the exact separated reduction

The reviewed total stationary error obeys ||e_T||infinity<<T^(-1/2+epsilon); second Poisson itself has no error. From (5),

    q_e:=integral_E |e_T|^2dmu<<T^(-1-2gamma+epsilon).

The accepted quadratic tail Q_E(F)<<T^epsilon, Cauchy, and S=F-e_T give

    |integral_E S^2dmu-Q_E(F)|
       <=2 Q_E(F)^(1/2)q_e^(1/2)+q_e
       <<T^(-1/2-gamma+epsilon)
        =T^(-157/250+epsilon).                        (14)

Thus every F-error and leading-term-error cross term is paid on the same actual E. No full-window error charge or transferred exceptional set is used.

Define the signed near form

    D_L(E)=sum_(|p-p'|<=L)integral_E P_pP_p' dmu.

Absolute convergence proves the identity

    integral_E S^2dmu=D_L(E)+R_L(E), |D_L(E)|<=C_L(E).

At L=sqrt(T), (1) and (14) prove (4). In particular

    R_L(E)>=-O(T^(-3/250+epsilon)),
    R_L(E)<=Q_E(F)+O(T^(-3/250+epsilon)).              (15)

The inherited bound supplies only R_L(E)<<T^epsilon. Nothing in the close payment improves that to T^(-a*). The one-sided upper bound is the correct open statement; the harmless lower bound in (15) follows from positivity of the complete energy, not from positivity of either truncated form. If L=T^(ell*) the same reduction holds with O(T^(-a*+epsilon)) error, which is sufficient without strict slack.

### 3.5 Both distribution tails and the complete moment implication

For q=136/13, V0=T^gamma and the strict event E, the exact quadratic identity is

    Q_E(F)=V0^2D_F(V0)+2 integral_(V0)^infinity V D_F(V)dV.

The generic V^(-2) term gives T^epsilon after using the actual polynomial ceiling; its second term contributes

    T V0^(2-q)=T^(-27/325).

These are the inputs behind (5); no threshold boundary is deleted. Assuming the open separated estimate at -a*, (4) gives Q_E(F)<<T^(-a*+epsilon). The actual ceiling then pays

    integral_E |F|^12dmu
      <=||F||infinity^10 Q_E(F)
      <<T^(10beta-a*+epsilon)=T^(32/25+epsilon).        (16)

Below V0, layer cake with the old distribution gives the powers

    T, V0^10, T V0^(12-q),
    max(1,10gamma,1+(20/13)gamma)
          =max(1,32/25,389/325)=32/25.                (17)

This also pays the twelfth threshold boundary. The unchanged second upper tail has exponent 1+20beta/13=1.198409772228...<32/25; the unresolved first tail has exponent10beta=1.289663519481... . Thus the saving required of the restricted energy is exactly a*, not an omitted second-tail or boundary payment.

Use the reviewed exact B=L_head+F+H_high, with both complementary twelfth moments at32/25. The finite L12 norm inequality and (16)-(17) give

    integral w(R/T)|B(R)|^12dR<<T^(32/25+epsilon).

H_high retains the entire infinite frequency tail. No factor-mask remainder U is omitted: the literal full F already contains that owner. Restoring the accepted sharp-discrepancy amplitude and dx=2R dR gives, with Z=T^2,

    integral_(Z/2)^(3Z)|P(x)|^12dx<<Z^(207/50+epsilon).

The accepted smoothing and Bessel error contributes only O(Z^(4+epsilon)) here. This conditional moment improvement would yield persistence exponent207/650, weaker than the accepted theta=(1+2beta)/4. It proves no pointwise improvement and no quarter theorem. All uses of epsilon are made by choosing input losses sufficiently small after fixing the output epsilon.

## 4. First doubtful or unproved step

The all-p packet envelope, exterior payment, close-band bound and error identity above have no remaining internal analytic gap under the explicitly inherited representation (6). Their status is candidate evidence pending the conductor's independent review; the authoritative graph has not changed.

The first unproved estimate needed for a complete gain is exactly

    2 sum_(p<p',p'-p>sqrt(T)) integral_E P_pP_p' dmu
                  <<T^(-a*+epsilon),                 (18)

with E selected by the full original F. Equation (18) has not been shown. The close-payment lemma establishes no character cancellation between separated products. Replacing 1_E by a smooth weight, appealing to odd first averages, or treating the close form as positive would not prove it. The inherited actual distinct-frequency covariance controls remain compatible with this result: their near-product contributions are paid absolutely, while no arithmetic high-tail lower bound is asserted.

The envelope estimate is coefficient-uniform at its stated component scope; it is allowed to pay unsigned/adversarial near bands too. The false generic full saving is avoided because the separated signed estimate (18), where actual arithmetic information would be required, is left open. No characteristic property of chi4 has been pretended to solve this gap.

## 5. Required control tests and outcomes

- **actual_packet_definition: pass.** Equation (6) uses genuine all-q Fourier modes, one divisor factor4, real cosine normalization and all rectangles. The nearest-q construction from the historical hostile report is explicitly distinguished.
- **same_product_and_near_pairs: pass.** Ordered-pair inequality (12) retains the full same-product packet square and every near cross term. Exact payments are -64/125 and -3/250; the sqrt(T) margin over a* is positive.
- **separated_signed_target: open, correctly isolated.** Equations (4),(14),(15) prove the actual reduction. They provide only a zero-power baseline upper bound for the separated remainder. No strict separated saving is claimed.
- **selected_set_not_slow_test: pass.** Only mu(E) and the accepted Q_E(F) are used. The proof applies to the original measurable E with no regularization of its indicator.
- **all_scales_tails_errors: pass.** Global divisor growth is absorbed into Schwartz decay in (7)-(8); (11) pays every negative/exterior mode and its mixed products. Cross rectangles are included before (12). The error cross term is T^(-157/250+epsilon). Real L,T,s and strict/closed pair boundaries are all allowed.
- **non_psd_band_control: pass by exact finite arithmetic.** For three centers1,2,3, L=1 and packet values(1,-2,1), the full square is0, the signed near form is (1+4+1)+2(-2-2)=-2, and the separated form is2. Thus deleting the near form on positivity grounds fails. Its absolute near payment is6+8=14, in agreement with (12)'s upper bound3*6=18. This is an algebraic control, not an actual packet realization or asymptotic counterexample.
- **both_tail_complete_budget: pass conditionally.** The quadratic second-tail exponent is -27/325; below-threshold twelfth exponents are1,32/25,389/325; the second high-tail exponent is1+20beta/13. Full32/25 follows only if (18) is proved, with both norm complements and sharp reconstruction retained.
- **blind_isolation: pass at assigned scope.** This was a selected-context formalization, not a statement-only task. No Round232 sibling report, blind packet statement, or review was read. The conductor received a brief progress message, which supplied no external mathematical premise.
- **graph_and_history_preservation: pass for this task.** Only this report was written. Graph, proof draft, matrices, synthesis and all historical files were untouched. No next round was designed. All mathematical work was analytical/algebraic; no numerical experiment or external source import was used.

## 6. Dependencies and exact artifacts used

The only mathematical inputs beyond elementary lattice/divisor inequalities are the named accepted generic distribution, its actual ceiling and sharp reconstruction, plus the Round231 reviewed representation and complementary-owner ledger. This report independently derives the global all-product envelope and payments from those stated inputs. It does not promote the underlying Round231 candidate representation merely by citing it.

The initial graph display was too large and truncated; the precise `GC-target`, `GC-external-Li-Yang-theta-star`, and `GC-complete-square-root-large-values-moment-bound` nodes were subsequently extracted and read. No neighboring graph theorem was used. Exact context hashes observed during this assignment:

| Artifact | SHA256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| state/proof_obligations.yml | a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b |
| state/active_campaign.yml | 9725379d3b9003f322ce541776a886aa3d493511da4a0b75316e4211d10e80cf |
| rounds/codex-managed/gc-upper-tail-separated-products/briefs/actual_near_product_payment.md | a3642ead79102b9dbc7bd358e84c13dbaab723594231ed864fe8afa69415b1e0 |
| rounds/codex-managed/gc-upper-tail-separated-products/briefs/actual_interface.md | c52e963aa8836fc7663c0528e170f4271396a907eafbee1ecc682db5d5885607 |
| rounds/codex-managed/gc-actual-upper-tail-a/synthesis.md | 8f8e7a07d2238728b4f672cc3694ad3431d8c146b7689738c0210452434784a3 |
| rounds/codex-managed/gc-actual-upper-tail-a/reports/signed_upper_tail_attack.md | ccd6592b215eecd1c38909fb088d40de2f0ea0b1916b1e568a58d54ba3c94e20 |
| rounds/codex-managed/gc-actual-upper-tail-a/reports/resonance_hostile_controls.md | 89693f8519e735dbdd9582850e5465c85fef30835aeab50e398b16fe34f837e8 |
| rounds/codex-managed/gc-actual-upper-tail-a/reviews/independent_signed_tail_review.md | dbcb1eb37c35c50e9cf69220ed235708de8252e9fde7737f79809bd6c93e8235 |
| proofs/kernels/gc_complete_square_root_large_values_moment_bound.md | 942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212 |

No unlisted artifact, source theorem or sibling report was read. The seven-section file is frozen only after writing; its SHA256 is returned separately to avoid a self-referential digest.

## 7. Recommended state effect

Retain this as candidate evidence for the actual near-product component payment and its precise cutoff range, subject to independent statement and seam review. A scoped component promotion, if desired by the conductor, must state its dependence on the reviewed actual representation and cannot be presented as a complete moment gain.

Retain the separated actual upper-tail target, complete32/25, all M1/M2 parents and the quarter target as open. Recommend no change to the accepted complete10beta moment or pointwise benchmark. No blanket decorrelation claim or unsigned full-energy saving is licensed. Freeze this report, return its hash, and stop; no successor is proposed.
