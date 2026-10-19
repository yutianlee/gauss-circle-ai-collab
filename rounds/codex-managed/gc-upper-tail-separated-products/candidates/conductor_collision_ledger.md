# Round232 conductor: collision sectors and the complete energy ledger

Campaign `gc-upper-tail-separated-products`; date2026-10-12 Asia/Shanghai. Conductor derivation for nonauthor review. Graph SHA256 `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`. Candidate evidence only.

## 1. Result

The actual selected-set size and packet envelope suffice to pay all integer product pairs at distance at most sqrt(T) by T^(-3/250+epsilon). A separate elementary divisor count pays distinct-product pairs whose underlying reciprocal frequencies have gcd at least T^(1/4) by T^(-9/500+epsilon). Both budgets are below the required T^(-a*+epsilon), a*=10beta-32/25=.009663519481... . This does not bound the remaining separated small-gcd signed sum and therefore does not prove a complete gain.

## 2. Exact hypotheses and ownership

Use `briefs/actual_interface.md` and the full-wave set E={|F|>T^gamma}, gamma=16/125. The accepted generic distribution pays mu(E)<<T^(-2gamma+epsilon). The full second-Poisson leading wave G equals the sum of real terms indexed by rectangle j, positive integer h and odd Fourier index q, with product p=hq. The divisor factor4 is included exactly once in those terms. F=G+e and ||e||infinity<<T^(-1/2+epsilon).

Within p comparable to T^2, each term has envelope C_A T^(-1/2)(1+|R^2-p|/W_j)^(-A), W_j=T/sqrt(N_j)<=C T^(1-2gamma)=:W. Each fixed product has at most T^epsilon divisor/rectangle occurrences. The p<=0 and exterior p tails must first be removed with their full cross terms, as in the assigned actual-payment report; one may choose any desired inverse power by increasing the fixed Schwartz order. The finite product range can be [T^2/8,8T^2] for R in[T/2,2T]. The remaining packet G=sum_p P_p then satisfies |P_p|<<T^(-1/2+epsilon)(1+|R^2-p|/W)^(-A). This report's estimates are conditional on that explicitly audited packet/tail interface, not on an arbitrary mask ceiling.

Use ordered pairs for near products. For high gcd retain the original elementary (j,h,q) labels, not a fictional gcd of grouped packets. The numerical product condition gcd(p,p')>=gcd(h,h') permits an upper enlargement only. It is not an equivalence of sectors.

## 3. Independent derivation

### A. Close products without any positivity assumption

For w_p=(1+|x-p|/W)^(-A), A>1, the integer sum is O_A(W) uniformly in real x and W>=1. By2ab<=a^2+b^2, each p occurs with at most2floor(L)+1 labels in |p-p'|<=L. Therefore

    sum_(|p-p'|<=L) w_p w_p' <=(2floor(L)+1)sum_p w_p^2
                              <<_A (1+L)W.

The unrestricted bound is O(W^2), so the minimum of these bounds is available. Summing actual packet magnitudes, integrating on E and absorbing divisor/rectangle logarithms into epsilon gives

    C_L(E):=int_E sum_(|p-p'|<=L)|P_pP_p'|dmu
            <<T^(-1-2gamma+epsilon)W min(1+L,W)
            <<T^(-4gamma+epsilon)min(1+L,W).

For L=T^(1/2) this is T^(1/2-64/125+epsilon)=T^(-3/250+epsilon). For L=0 the exact-product contribution is T^(-64/125+epsilon). A power cutoff L=T^ell can be paid at target -a* by this estimate whenever ell<=4gamma-a*=224/125-10beta=.502336480519... . This identifies the reach of this envelope certificate, not a lower bound for the actual coefficients.

The close-band matrix is not positive semidefinite in general. For labels0,1,2, L=1 and vector(1,-2,1), its quadratic form equals-2 while the full square is0. Thus the close sector is removed using its absolute bound, not by falsely declaring it nonnegative.

### B. Distinct products with high reciprocal gcd

First truncate the rapid product tails to |R^2-p|<=T^eta W, with arbitrarily small fixed eta>0 chosen within the output epsilon. Let U=2T^eta W be this interval's length. For distinct integer products p,p' in this interval, any common divisor g is at most |p-p'|<=U. The number n_g of multiples of g in an arbitrary real interval of length U satisfies n_g<=floor(U/g)+1, so

    n_g(n_g-1)<=(U/g+1)U/g.

Consequently, for1<=G0<=U, the number of ordered distinct pairs having some common divisor g>=G0 is at most

    sum_(G0<=g<=U)n_g(n_g-1)
       <<U^2/G0+U log(2+U).

If G0>U, there are no such pairs. Counting several divisors of a pair only enlarges this upper bound. The multiplicity of the original elementary labels for each product pair is at most T^epsilon, by divisor bounds and finitely many rectangles. Thus the absolute sum of elementary term products in the distinct-product sector gcd(h,h')>=G0 is bounded pointwise by

    T^(-1+epsilon)[U^2/G0+U log(2+U)].

Integrating on E and choosing eta within epsilon yields, for G0<=W up to harmless powers already absorbed,

    C_high_gcd(E)<<T^(1-6gamma+epsilon)/G0+T^(-4gamma+epsilon).

At G0=T^(1/4), this is T^(-9/500+epsilon), since1-96/125-1/4=-9/500. The logarithmic second term is smaller. The fixed power G0 lies below W throughout the frozen common-width range; no transition loss occurs. The tail truncation is an estimate on actual terms, not a replacement of E. It must include cross terms with the retained wave using polynomial envelope bounds before choosing the Schwartz order.

This sector payment bypasses the Round231 example h=5g,h'=9g with g comparable to T: exact products are already paid in A, and distinct nearby products cannot both be multiples of that large g. It does not assert that such individual correlations are small on the full radius interval.

### C. Remaining signed sector and full restoration

Partition the expanded quadratic energy without overlap:

1. |p-p'|<=sqrt(T), including all exact products and all frequency gcds;
2. |p-p'|>sqrt(T) and gcd(h,h')>=T^(1/4), keeping elementary labels;
3. |p-p'|>sqrt(T) and gcd(h,h')<T^(1/4), with all real signs and all cross-rectangle labels retained.

The first two contributions have absolute budgets T^(-3/250+epsilon) and T^(-9/500+epsilon). The third is real and requires only a one-sided upper bound T^(-a*+epsilon); asserting a bound for its absolute value would be a stronger additional premise. It still uses the original full-F indicator1_E.

The representation error costs less than these budgets. From the accepted Q_E(F)<<T^epsilon and ||e||infinity<<T^(-1/2+epsilon), one has ||e||_(L2(E))<<T^(-1/2-gamma+epsilon). Hence

    |Q_E(F)-Q_E(G)|<=2||F||_(L2(E))||e||_(L2(E))+||e||_(L2(E))^2
                     <<T^(-1/2-gamma+epsilon).

Rapid tails can be made smaller still. If sector3 is bounded as required, then Q_E(F)<<T^(-a*+epsilon). The actual F ceiling T^(beta+epsilon) pays its high twelfth moment at10beta-a*=32/25. Low amplitudes and the threshold boundary have max(1,10gamma,1+20gamma/13)=32/25; exact complementary L,H moments have that budget too. The unchanged second distribution term has quadratic power-27/325 and twelfth-tail power1+20beta/13=1.198409772228..., both paid. No owner is omitted.

The accepted pointwise relation is theta=(1+2beta)/4. Complete32/25 would imply207/650, a weaker pointwise consequence. Without sector3, the restored accepted exponent remains10beta.

## 4. First unproved step

The actual signed sector3 estimate is unproved here. Same-two-adic character signs are constant at each fixed product difference; different reduced parity permits alternation along a solution progression, but no bound for the complete weighted restricted sum follows. Paying collisions is a real component estimate, yet does not by itself pay the much larger collection of separated small-gcd pairs.

## 5. Controls and outcomes

The band matrix control is an exact integer computation with negative quadratic form-2. The divisor count has an exact pointwise proof for any real interval, including endpoints; at G0>U the distinct-pair sector is empty. Both payments use mu(E) only and therefore remain valid when E is selected by F; no independence or smoothness of its boundary is assumed. A generic cloud of like-signed packets can have total energy of order m A^2W^2 and close energy only m A^2WL for L<<W, showing why the small close sector alone is insufficient. Such a cloud is not an arithmetic counterexample.

Bounded local reproduction and rational exponent checks are archived under controls/ and are diagnostic_only. Independent blind and actual-family reviews are required before this candidate is used in synthesis.

## 6. Dependencies and exact artifacts

`protocol.md`, `state/proof_obligations.yml`, `state/active_campaign.yml`, `briefs/actual_interface.md`; closed231 `reports/signed_upper_tail_attack.md`, `reports/resonance_hostile_controls.md` and its completed independent reviews; accepted `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`. No newly imported external theorem. The conductor independently derived the integer band and multiple-count estimates, then communicated the latter to the discovery analyst after that analyst had independently reported the same scale. Sibling initial reports were not shared.

## 7. Recommended state effect

Retain the reviewed close/high-gcd component payments and conditional complete ledger. Do not promote A,32/25, any pointwise gain or parent target unless the actual sector3 estimate is proved and reviewed. This is attempt2 on the same premise; if no complete gain is obtained, conduct the required strategy reassessment at closure and do not auto-launch a third version of the same calculation.
