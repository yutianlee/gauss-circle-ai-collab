# 1. Result: PASS for the actual bridge and its explicitly conditional scope

Round235, campaign `gc-signed-sixth-dispersion`; task `actual_bridge_review`; nonauthor seam reviewer of `actual_sixth_bridge.md`. Generated 2026-10-12, Asia/Shanghai. I authored the separate arithmetic discovery report, but not this bridge report. This review independently checks the bridge mathematics and does not certify my own arithmetic grouping or certificate claims.

**PASS** for Sections3A and3B of conductor candidate SHA256 `cee1d243f21577e090acb0f9387c0412f4f70748b918aa3661e64db15586a8f3`, together with the actual-bridge report at SHA256 `e7e1b99ab4b62fb94d66b7f8c1c16b88d6e3bb9f891405da1b4d3c2e697795b6`, as qualified by the candidate's explicit scope clarification. No material mathematical defect was found in the all-class variance, finite absorption, complete two-term Hankel transformation, moving-width linearization, or conditional complete restoration.

The first missing arithmetic estimate is still S6. The full-band distinct-six bound is equivalent to the full-band sixth moment at the stated budget; blockwise S6 is a sufficient hypothesis, not an asserted equivalent condition. The conductor candidate explicitly resolves the frozen report's potentially ambiguous wording on this point. The proposed identity State Patch is consistent with this outcome.

# 2. Exact statement and review hypotheses

I checked the actual coefficients with rho real, nonnegative, radial, smooth, supported in the unit disk and of mass1; Psi its radial Fourier profile; fixed smooth nonnegative radius window w; and the actual low/band/high decomposition with

    X=T^(52/125), Y=T^(99/125),
    phi(n)=eta(n/X)-eta(n/Y),
    F=sum_n phi(n)r2(n)n^(-3/4)Psi(sqrt(n/T))cos(2pi R sqrt(n)-3pi/4).

All R and T are real, R comparable to T. Smooth eta is zero below1 and one above2; both norm transitions are included. For sufficiently large T the two transition strips are disjoint. Bounded T is absorbed into constants. The dyadic blocks N satisfy cX<=N<=CY, with a fixed compact smooth partition. The exact moving width is H_N(x)=2sqrt(x)/sqrt(N).

The reviewed conclusions are:

1. V=sum_(all squarefree d)g_d^2 is O(T^epsilon X^(-1/2)); its integrated cube is O(T^(47/125+epsilon)).
2. Accepted233's finite algebraic relative absorption applies to this finite real family, paying repeats and leaving the signed distinct-six target.
3. F_N(R)=R^(-1/2)S_N(R^2)+E_N(R), with M6(E_N)<<T^(1+epsilon)N^(-6), including all dual modes, transitions and tails.
4. Uniform blockwise S6 implies M6(F)<<T^(193/500+epsilon); it is not proved.
5. The inherited actual complementary bounds and qualified actual supremum imply, conditionally on that band bound, complete M12(B_T)<<T^(29/25+epsilon) and sharp exponent102/325. They do not imply one-quarter.

The accepted distribution and absorption nodes remain `proved_internal`; GC-target remains `open` at the unchanged graph hash. The actual high-norm ledger is inherited reviewed evidence, not newly promoted mathematics in this campaign.

# 3. Independent derivation and seam checks

## All squarefree classes and absorption

For d<=X, the norm lower support forces s>sqrt(X/d). Summing the positive majorant s^(-3/2) gives

    |g_d|<<T^epsilon d^(-3/4)(X/d)^(-1/4)
          =T^epsilon X^(-1/4)d^(-1/2).

For d>X the full convergent harmonic sum gives T^epsilon d^(-3/4). The coefficient bound is valid because the finite band has n<=2Y and hence the divisor loss is absorbed into T^epsilon. Squaring and summing over every positive d, which majorizes the squarefree sum, gives X^(-1/2)log(2X)+O(X^(-1/2)). Cubing and integrating over a radius interval of length O(T) gives exponent1-3(52/125)/2=47/125. This retains high harmonics of small classes and makes no independence or exact-resonance assumption.

The accepted finite real-family inequality is algebraic and therefore applies directly to these g_d; its prior arithmetic bound for another cutoff is not reused. At p6 its constant 719 max(1,(719/delta)^2) agrees with p!-1 and (p-2)/2. Taking delta=1/2 shows the full-band signed target and moment target are upper-bound equivalent once J6 is paid. The difference itself is not asserted to have a smaller absolute error independent of M6.

## Profiles, zero mode, phases and Bessel summability

On the fixed s-annulus, derivatives of eta(Ns^2/X) can be nonzero only when N/X is bounded; otherwise that factor is locally constant. The same observation handles Y. Therefore all transition-block derivative bounds are uniform. Compact support away from0 makes the radial test function smooth at0 and compactly supported, so exact two-dimensional Poisson applies. The radial transform has the angular factor2pi and radial measure u du, giving precisely the report's integrand u^(-1/2)b_N(u)J0(2pi vu).

Two integrations by parts at v=0 cost R^(-2)A^(-3/2), A=sqrt(N). This mode is paid explicitly. At nonzero v, the positive-real fixed-order Bessel specialization gives

    cos(2pi vu-pi/4)/(pi sqrt(vu))
      +sin(2pi vu-pi/4)/(16pi^2(vu)^(3/2))
      +O((vu)^(-5/2)).

Multiplying by the angular factor and the original cosine gives a leading positive difference sine, with coefficient1, and a sum cosine with a minus sign. The second product gives a difference cosine and a negative sum sine with coefficient1/(16pi A) after rescaling. These are independently obtained from the elementary product-to-sum identities; the phases and constants in the report agree.

The remainder integral is O(v^(-5/2)A^(-2)), since the radial amplitude contributes integral u^(-3)|b_N(u)|du=O(A^(-2)). The full sum over the nonzero two-dimensional dual lattice converges because exponent5/2>2. A first-term-only expansion would leave exponent3/2 and would not justify the same summation. The report correctly retains the second term before taking absolute values.

The source card's hypotheses match this use: order0 is fixed and real, z=2pi vu is positive and tends uniformly to infinity on the annulus as T grows, and one term is retained in each even/odd series. The finite range of bounded T causes no transition-of-order issue. This review checks that local source specialization and the permitted earlier derivation; it does not claim a new external theorem or a fresh browser audit.

## Full tails and variable-width linearization

On R/2<=sqrt(m)<=2R,

    |R-sqrt(m)|>=|R^2-m|/(3R).

The shifted-grid sum is O(1+R/A), uniformly at integral and nonintegral centers. On either outside range the complete tail is O(A^(-L)R^(2-q-L+epsilon)) for q=1/2 or3/2; the high range is a convergent infinite series when L is sufficiently large. The sum phase has no exceptional central range and is arbitrarily small after enough integrations by parts. No hard dual cutoff is introduced.

Writing t=A(R-v), u=A(R^2-v^2)/(2R), the exact identity is u=t-t^2/(2AR). In the central v range the ratio u/t=(R+v)/(2R) lies between3/4 and3/2. Hence the segment between t and u preserves sign and comparable size, justifying the stated Schwartz mean-value estimate. The amplitude difference is O(R^(-3/2)A^(-1)|t|). Summing both differences gives

    O(T^epsilon R^(-3/2)A^(-1)(1+R/A)).

The transformed high tail uses u comparable to Am/R, and its sum again has the displayed arbitrarily small bound. Thus the representation preserves H_N(x)=2sqrt(x)/sqrt(N) exactly. Its total error is bounded by

    T^epsilon[N^(-1)+T^(-3/2)N^(-1/2)
                 +T^(-1/2)N^(-1)+T^(-2)N^(-3/4)].

On the required N range the first term dominates. Integrating its sixth power costs T N^(-6), whose largest band exponent is1-6(52/125)=-187/125. This is safely below the target. All statements use real cutoffs; no arithmetic rounding is hidden in the profile estimates.

## Jacobian, complements and exact margin

The Jacobian calculation is decisive: (R^(-1/2))^6 dR=(1/2)x^(-2)dx. Therefore S6 yields T^(-4) times T^(2+1/100)(T/sqrt(N))^3, or T^(1+1/100)N^(-3/2). Summing the finite smooth partition costs only powers of log T. At N comparable to X the exponent is47/125+1/100=193/500.

The low complement has an independently proved coefficient ceiling X^(1/4+epsilon)=T^(13/125+epsilon). The actual high complement has the inherited smooth norm-tail ceiling sqrt(T/Y)T^epsilon=T^(13/125+epsilon), including its infinite tail. The distribution mechanism applies to these fixed divisor-bounded coefficient vectors after those ceilings are established; layer cake gives T+T^(10gamma)+T^(1+20gamma/13), whose maximum at gamma=13/125 is29/25. The exact actual B=L+F+H identity then supplies F's beta ceiling. No actual-B supremum is transferred to arbitrary masks.

Independently, beta<129/1000 is equivalent to 25000sqrt(1717)<1036149. The sides are positive and the squared difference is479750201, so

    6beta+193/500 < 774/1000+386/1000 =29/25.

The report's exact radical expression for the margin is algebraically consistent with this comparison. Internal epsilons can be chosen after the fixed positive margin. Finally, the sharp twelfth moment has squared-radius exponent(7+29/25)/2=102/25; monotonicity persistence divides by13, giving102/325. The smoothing error exponent4 is smaller. This is a conditional fixed-order consequence and does not approach one-quarter by itself.

# 4. First doubtful or unproved step

No unproved step was found in the reviewed bridge relative to its explicitly inherited accepted and reviewed inputs. The first open step in its application is the uniform actual blockwise S6 bound. Equivalently only at the FULL-BAND level, the moment target is equivalent to the signed distinct-six upper bound; no reverse implication from the full-band target to each S6 block is established or needed.

The frozen report's Section4 wording could be misread as asserting that stronger reverse implication. Candidate Section2 explicitly prohibits that reading, and is the controlling synthesis reviewed here. The two broken roman-font escapes in the report are presentation defects; the all-squarefree index is unambiguously defined in the surrounding prose and corrected in the candidate. Neither issue requires rewriting frozen evidence or changes the mathematical verdict.

Detailed proof of candidate Sections3C--3E, including arithmetic grouping and the absolute fraction certificate, is outside this assigned nonauthor seam and is not certified by this review.

# 5. Controls and outcomes

| Seam | Result |
|---|---|
| Actual all-class variance and harmonics | PASS; low classes retain their high harmonics, and the square-sum budget is47/125. |
| Fixed233 application | PASS; finite real-family absorption applies without importing an unrelated cutoff estimate. |
| Hankel normalization and both phases | PASS; leading coefficient1, second coefficient1/(16pi A), correct sine/cosine signs. |
| Two-term remainder and zero mode | PASS; convergent full dual error and explicit zero-mode cost. |
| Both norm transitions and remote tails | PASS; uniform derivative support argument and complete convergent tail estimates. |
| Variable width and real endpoints | PASS; exact quadratic relation and shifted-grid uniformity. |
| Jacobian and error moments | PASS; x^(-2)/2 weight, error exponent-187/125 at the lower band endpoint. |
| Actual complements and supremum | PASS at inherited qualifications; full high tail retained, no arbitrary-mask pointwise claim. |
| Exponent margin and sharp restoration | PASS; exact positive integer479750201 and conditional102/325. |
| Shared exact diagnostics | PASS as recorded diagnostics only; all named checks are true. No finite computation proves S6. |
| Source hypotheses | PASS for fixed order0, positive real argument and the stated two-series truncation. |
| Preservation and isolation | PASS for this review; only the assigned review artifact was written, no discovery extension. |

The manifest discloses the unrelated27/83 expression and its corrected sharp-restoration query, the harmless grouping pre-evaluation warning, and the failed context request. None is used as mathematical evidence for the bridge. No new numerical experiment or sweep was run in this review.

# 6. Dependencies and exact hashes

The candidate hash matches the bound hash in the review brief. Relevant graph nodes were rechecked and the graph bytes are unchanged. Context read earlier in this same task chain was retained rather than redundantly reopened; the current campaign status was read as `review` and its updated hash is recorded below.

| Artifact | SHA256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| state/proof_obligations.yml | dd743db27ed8eaac685d23dd2f92da743dd2d1742c2f150ddecf802dbbca5306 |
| state/active_campaign.yml | 48353e0fea3b38fad5c64829b22280d989c0631aed0fd8304f8b4290b6b8cc54 |
| briefs/actual_bridge_review.md | a7fe5788913a34da9ba43303e9c5e73444df7c1defd54d9d0085ebf0f111a8df |
| candidates/conductor_signed_sixth.md | cee1d243f21577e090acb0f9387c0412f4f70748b918aa3661e64db15586a8f3 |
| reports/actual_sixth_bridge.md | e7e1b99ab4b62fb94d66b7f8c1c16b88d6e3bb9f891405da1b4d3c2e697795b6 |
| controls/control_manifest.md | a2751a7fbca018496711c9002732a9bb76b0474cd588f654915f6b1fe538d385 |
| controls/exact_local_controls.json | 2e6cdf957006c16d4c43455e9151073c36b02732ba7280648c16e2caaf05e7e3 |
| controls/source_check.md | 315c1b7dbd28f1b69836aabc3a90c7899f73ec5ff913dcd98fffcb30767fc3dd |
| proofs/kernels/gc_complete_square_root_large_values_moment_bound.md | 942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212 |
| proofs/kernels/gc_complete_fixed_even_moment_distinct_absorption.md | b1097aa498d0430d5bbe81fb0b8927cc4ffdf278ce838b3ef38f555bc75c31d0 |
| strategy/round231_balanced_cancellation/conductor_combined_owner.md | 9f5d9a31c0624e7ee97a21bcdfa2e638154fa313cc45cbab198856222366d76b |
| strategy/round231_balanced_cancellation/reports/blind_hankel_tail.md | 03b30638eb6da7242343731ac03b425e2f09e16749f73685adc343a357cd01d5 |

Unqualified briefs/candidates/reports/controls paths in this table are relative to `rounds/codex-managed/gc-signed-sixth-dispersion/`. The initial combined display was truncated near the bridge opening; that opening and complete hypotheses were then separately read. No review conclusion relies on unread truncated material. No additional source card, sibling review, or new mathematical context was accessed.

# 7. Recommended state effect

Accept the reviewed actual-bridge seam as **PASS** at the candidate's exact bound hash and stated conditional scope. Retain the proof as reviewed campaign evidence. Apply no new complete-moment or pointwise promotion from this seam; an identity State Patch is appropriate if the other independent seams pass.

Keep S6, the full-band signed target, complete29/25, sharp102/325, and the quarter theorem unproved. Preserve the accepted baseline, source qualifications and frozen artifacts. This review is complete; stop without new discovery or successor work.
