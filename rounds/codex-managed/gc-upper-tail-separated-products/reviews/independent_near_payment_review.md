# Independent review of the actual close-product payment

Round232; campaign `gc-upper-tail-separated-products`; reviewer `separated_product_attack`, nonauthor of the claimant. Generated2026-10-12 Asia/Shanghai. Claimant: `reports/actual_near_product_payment.md`, verified SHA256 `a4943d33174f49270506dcde6fb81a58412870daeec3dcf2c2686e175985a92a`. Starting graph SHA256 `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`. This is the one assigned bounded review after the reviewer's discovery report was frozen.

## 1. Result and precise verdict

**Pass at the stated component and conditional-reduction scope.** I found no error in the global all-p envelope, the absolute close-band payment, the negative/exterior and mixed-tail accounting, the selected-set stationary-error identity, the cutoff exponent, or the full conditional moment ledger. No claimant repair is required.

Under the reviewed actual representation, the report proves

    C_L(E)<<T^(-4gamma+epsilon) min(L+1,W),
    gamma=16/125, W asymp T^(1-2gamma),

uniformly for real L>=0 and real T>=2. In particular `C_(sqrt(T))(E)<<T^(-3/250+epsilon)`. It correctly leaves the separated signed upper bound open. The claimed equivalence is only between that one-sided bound and the sufficient actual exceptional-set energy estimate at the specified exponent; it is not an equivalence with the complete moment theorem or with target A.

The maximum cutoff power `ell*=4gamma-a*=0.502336480519...` is the maximum delivered by this envelope-and-measure argument. It is not a claimed arithmetic impossibility above that cutoff. The close-band form is not positive semidefinite, and the proof correctly pays it in absolute value.

## 2. Exact statement and hypotheses reviewed

The original band, measure and event are

    F(R)=sum_n [eta(n/T^(64/125))-eta(n/T^(93/125))]
          r2(n)n^(-3/4)Psi(sqrt(n/T))
                         cos(2pi R sqrt(n)-3pi/4),
    dmu=w(R/T)dR, E={R in supp(w(R/T)): |F(R)|>T^gamma}.

The fixed mollifier and cutoffs are those in the frozen actual interface, with R in `[T/2,2T]`. The inherited inputs are `mu(E)<<T^(-2gamma+epsilon)`, `Q_E(F)<<T^epsilon`, the actual ceiling `||F||infinity<<T^(beta+epsilon)`, and the reviewed representation

    F=S+e_T, S=sum_(p!=0)P_p,
    ||e_T||infinity<<T^(-1/2+epsilon),
    P_p=4T^(-1/2)sum_j sum_(h~H_j,h|p,p/h odd)
                    chi4(p/h)K_(j,h,R)((R^2-p)/W_j).

Every rectangle is retained, `D_jM_j asymp N_j`, `X/constant<N_j<constant Y`, `W_j=T/sqrt(N_j)`, and `H_j=TD_j/sqrt(N_j)`. The all-q second-Poisson formula supplies genuine odd Fourier indices. This review does not substitute the historical nearest-q partition. The factor4 appears exactly once; the real cosine branches are already combined. Kernel smoothness and total stationary error are inherited at the explicitly reviewed scope.

Let `a*=10beta-32/25>0` and `L=sqrt(T)`. The open assertion is

    R_L(E)=2sum_(p<p',p'-p>L)int_E P_pP_p' dmu
                                       <<T^(-a*+epsilon).

All bounds below retain the same E selected by the entire F. No regularity of its indicator is used.

## 3. Independent derivation and seam checks

### 3.1 The envelope is global, not restricted to p comparable to T squared

The stated smooth symbol has size `T^(-1/2)D_j^(-1)`, support length `O(D_j)`, and d derivatives at the reciprocal D_j scale. In the sine transform defining K, the substitution `d=D_j t` leaves a compact smooth symbol of bounded size. Since `W_jD_j/h` is bounded above and below, integration by parts gives every fixed Schwartz decay order uniformly in R,h,j.

For p nonzero, the h multiplicity is at most `d(|p|)`. The divisor bound thus gives

    |P_(j,p)|<<T^(-1/2)|p|^eta
                         (1+|s-p|/W_j)^(-B), s=R^2.

The crucial global step is valid: `s<=4T^2`, `W_j<<T^2`, and

    |p|<=s+|p-s|<<T^2(1+|p-s|/W_j).

Therefore `|p|^eta` costs only `T^(2eta)` and eta units of decay. Choosing B larger first, and eta sufficiently small relative to the requested epsilon, proves a common envelope with W a fixed multiple of `T^(1-2gamma)`:

    |P_p|<<T^(-1/2+epsilon)(1+|s-p|/W)^(-A).         (R1)

There is no invalid substitution `d(|p|)<<T^epsilon` at unbounded p. The same argument covers negative p by absolute value. Setting P_0=0 is consistent because h>0 and q odd never give zero product.

The logarithmic number of rectangles changes only epsilon. Taking their sum before squaring leaves every cross-rectangle term in the envelope. Constants depend on fixed Schwartz seminorms and epsilon; the decay order is fixed after the target error power, not allowed to grow with T.

For real s and W>=1, shell counting gives

    sum_p(1+|s-p|/W)^(-A)<<W,
    sum_p(1+|s-p|/W)^(-2A)<<W.

Together with (R1), these prove `sum|P_p|<<T^(-1/2+epsilon)W` and `sum|P_p|^2<<T^(-1+epsilon)W`. For each T the tails are uniformly summable on the compact radius window, so all products may be expanded and integrated on measurable E. No orthogonality or positivity assumption is involved.

### 3.2 Every negative/exterior mode and mixed term is paid

For the claimant's exterior `p<T^2/8` or `p>8T^2`, and `s in[T^2/4,4T^2]`, one has `|s-p|>>T^2`. Summing (R1) over this lattice tail yields

    sum_exterior |P_p|
      <<T^(-1/2+epsilon)W(T^2/W)^(-(A-1)).            (R2)

Substituting W gives the claimed exponent `1/2-2gamma-(A-1)(1+2gamma)+epsilon`. It tends to minus infinity with A. This contains every negative mode and arbitrarily large positive mode. There is no omitted finite strip at a sharp real boundary: an endpoint is either retained or satisfies the same non-strict distance lower bound, and the lattice estimate is uniform in its fractional part.

For any subset of pairs with at least one exterior index, its absolute sum is at most twice the exterior l1 norm times the full l1 norm. The full norm has polynomial size. Even integration over the entire radius window costs only O(T), so increasing A pays exterior-interior and exterior-exterior terms at any prescribed negative power. This also validates the statement for either the near or separated band of pairs.

### 3.3 Exact integer-band counting, real L, and the non-PSD issue

Put a_p=|P_p| and m=floor(L). For each integer shift k,

    sum_p a_pa_(p+k) <= sum_p a_p^2

by Cauchy, with equality of the shifted square sums on the full integer lattice. Summing the `2m+1` permitted shifts proves

    sum_(|p-p'|<=L)a_pa_p'
        <=(2m+1)sum_p a_p^2
        <<T^(-1+epsilon)W(L+1).                     (R3)

This independently recovers the claimant's elementary two-square proof. The competing full l1 square gives `T^(-1+epsilon)W^2`. Multiplying their minimum by `mu(E)<<T^(-2gamma+epsilon)` proves the stated bound for every real L, including L<1 and equality at integer boundaries. Ordered pairs count the diagonal once and both orders of each off-diagonal pair, as required.

At L=0 the exponent is `-4gamma=-64/125`. At L=sqrt(T), it is `1/2-4gamma=-3/250`. The first is the square of the full same-product packet; it includes all divisor and rectangle coincidences, not merely individual h diagonals.

The claimant's finite control is correct: values `(1,-2,1)` at centers `(1,2,3)` have total square0, near form-2 when L=1, and separated form2. Consequently the near form cannot be discarded using positivity. The proof instead bounds its absolute sum, which in this example is14, below the bound18 from (R3). No actual arithmetic realization of that control is asserted or needed to diagnose the matrix error.

### 3.4 Largest cutoff power and meaning of sharpness

For `L=T^ell` with `0<=ell<=1-2gamma`, the method gives exponent `ell-4gamma`. Comparing it with -a* gives

    ell<=4gamma-a*=224/125-10beta=ell*.

Equality is valid in the epsilon convention. The strict margin at ell=1/2 is `ell*-1/2=0.002336480519...`. At and beyond the width exponent the envelope bound saturates at `1-6gamma=29/125`, which supplies no negative-power energy estimate.

The generic shoulder control correctly shows that `W(L+1)` is the order supplied by the envelope class for `1<=L<<W`: there are comparable to W occupied integer centers, each has comparable to L permitted neighbors, and each pair has size comparable to T^(-1). This supports the report's method-level cutoff claim. It does not prove saturation for the actual arithmetic packets or their particular exceptional set, and the report makes that distinction explicitly.

### 3.5 Selected-set error identity and one-sided equivalence

The error norm on the original event satisfies

    q_e=int_E|e_T|^2dmu<<T^(-1-2gamma+epsilon).

Since S=F-e_T, direct expansion and Cauchy give

    |Q_E(S)-Q_E(F)|
       <=2 Q_E(F)^(1/2)q_e^(1/2)+q_e
       <<T^(-1/2-gamma+epsilon).                    (R4)

This uses the accepted zero-power energy only as an already available input; it is not circular with the desired negative-power improvement. The exponent is `-157/250`, safely below both -3/250 and -a*. Paying the error over E rather than over the entire interval is essential here and is done correctly.

Absolute convergence gives `Q_E(S)=D_L(E)+R_L(E)` exactly. Since `|D_L|<=C_L`, (R3)-(R4) prove

    Q_E(F)=R_L(E)+O(T^(-3/250+epsilon)).              (R5)

The error in (R5) is strictly below the target power. Thus either upper bound at -a* implies the other. The lower bound `R_L>=-O(T^(-3/250+epsilon))` follows from `Q_E(F)>=0`, not from positivity of a band. These are sufficient energy-interface statements; neither claims the separated estimate has been proved.

### 3.6 Both tails, complete ownership, and sharp reconstruction

For the strict event E, the layer-cake identity includes the boundary term `V0^2D_F(V0)`. The generic `V^-2` part gives zero-power energy, up to logarithms under the actual polynomial ceiling. The second distribution term gives

    T V0^(2-136/13)=T^(-27/325).

If the open separated estimate is supplied, (R5) and the actual ceiling give the high twelfth moment `T^(10beta-a*+epsilon)=T^(32/25+epsilon)`. The inputs to this ceiling remain the actual full F; no packet, mask, or subevent inherits it.

Below V0, layer cake and the trivial O(T) measure at levels below1 give powers `1`, `10gamma=32/25`, and `1+20gamma/13=389/325`. The threshold boundary is covered by the same budget. The second high-tail owner `1+20beta/13` is below32/25, while the unchanged first high-tail owner is10beta. All exponent losses can be fixed after the desired output epsilon.

The exact decomposition `B=L_head+F+H_high`, with both complementary full twelfth moments at32/25, restores the complete B moment by a finite norm inequality. The infinite frequency tail remains in H_high and the full factor owner U remains inside F. No component is dropped in this conditional implication.

For Z=T^2, the leading sharp-discrepancy amplitude contributes T^6 at the twelfth power and the Jacobian contributes T, so the moment becomes `T^(7+32/25+epsilon)=Z^(207/50+epsilon)`. The accepted smoothing/Bessel error contributes at most `Z^(4+epsilon)`. The stated persistence exponent207/650 is therefore correctly described as weaker than the accepted pointwise benchmark. No pointwise or quarter-theorem promotion follows.

## 4. First doubtful or unproved step

No new gap was found in the close-product component proof under its inherited packet representation. The first missing estimate remains the one-sided signed separated sum on the original actual E at exponent -a*. The global envelope and absolute payment are compatible with unsigned or adversarial packets precisely because they do not claim this remaining full saving.

The report's sharp cutoff statement is scoped to the displayed proof. Promoting it as an arithmetic impossibility for larger cutoffs, treating either matrix band as positive, replacing E by a slow test, or identifying the energy condition as equivalent to the full moment theorem would go beyond the report. None of these substitutions is made in the claimant.

## 5. Required controls and outcomes

- Global all-p envelope: pass; global divisor growth is absorbed into additional Schwartz decay before the T^epsilon notation is used.
- Negative/exterior and mixed modes: pass by (R2) and l1 multiplication; all boundaries are real and all modes are owned.
- Cross rectangles and exact products: pass; rectangles are summed before taking packet products, with their full divisor multiplicity.
- Real T,L,s and band boundaries: pass; floor(L), uniform lattice shell counting, and P_0=0 handle all endpoint cases.
- Non-PSD close band: pass; the exact finite control is correct and the proof uses absolute payment.
- Selected-set error and equivalence: pass; (R4)-(R5) retain the original E and use only accepted baseline inputs.
- Maximal cutoff exponent: pass at method scope, including equality with epsilon and the strict sqrt(T) margin.
- Complete restoration: pass conditionally; both distribution tails, threshold, complementary owners, infinite tail and sharp reconstruction remain visible.
- Isolation and preservation: the initial claimant and reviewer reports remain frozen. No blind report, current-round sibling beyond this expressly assigned claimant, shared state, synthesis, matrix or legacy artifact was accessed or edited in this review. Only the assigned review was written.

The review was analytical/algebraic. No numerical experiment, external theorem import, or additional discovery cycle was used.

## 6. Dependencies and exact artifacts used

The sole newly authorized content read was the frozen claimant identified below. Other mathematical context had been read during the reviewer's initial selected-context assignment. This review independently rederived the relevant estimates and does not depend on the reviewer's own unpromoted large-gcd discovery result.

| Artifact | SHA256 |
|---|---|
| rounds/codex-managed/gc-upper-tail-separated-products/reports/actual_near_product_payment.md | a4943d33174f49270506dcde6fb81a58412870daeec3dcf2c2686e175985a92a |
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| state/proof_obligations.yml | a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b |
| state/active_campaign.yml | 9725379d3b9003f322ce541776a886aa3d493511da4a0b75316e4211d10e80cf |
| rounds/codex-managed/gc-upper-tail-separated-products/briefs/actual_interface.md | c52e963aa8836fc7663c0528e170f4271396a907eafbee1ecc682db5d5885607 |
| rounds/codex-managed/gc-actual-upper-tail-a/synthesis.md | 8f8e7a07d2238728b4f672cc3694ad3431d8c146b7689738c0210452434784a3 |
| rounds/codex-managed/gc-actual-upper-tail-a/reports/signed_upper_tail_attack.md | ccd6592b215eecd1c38909fb088d40de2f0ea0b1916b1e568a58d54ba3c94e20 |
| rounds/codex-managed/gc-actual-upper-tail-a/reports/resonance_hostile_controls.md | 89693f8519e735dbdd9582850e5465c85fef30835aeab50e398b16fe34f837e8 |
| rounds/codex-managed/gc-actual-upper-tail-a/reviews/independent_signed_tail_review.md | dbcb1eb37c35c50e9cf69220ed235708de8252e9fde7737f79809bd6c93e8235 |
| proofs/kernels/gc_complete_square_root_large_values_moment_bound.md | 942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212 |

The reviewer is the author of `reports/separated_product_attack.md`, frozen SHA256 `e8974ef88d0c24e675cbfaf3328655a9cdff292fbff2999e5b9b79019be5fffc`, and is not the author of the present claimant. No self-review promotion is made.

## 7. Recommended state effect

Record this seam review as pass for the actual close-product component bound and its stated conditional reduction. Retain the exact cutoff scope, absolute band handling, and dependence on the reviewed representation. No claimant repair is needed. Leave the separated signed estimate, complete32/25, all M1/M2 parents and the quarter target open. No accepted graph or proof-draft change is requested by this review. Freeze this review and stop; no further cycle or successor is initiated.
