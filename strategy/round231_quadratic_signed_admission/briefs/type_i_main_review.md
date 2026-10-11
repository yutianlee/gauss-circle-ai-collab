# Independent review of the complete Type-I main

Conductor-assigned additional seam within this packet, not a new round. Read protocol.md, complete_interface.md, accepted proofs/kernels/gc_complete_square_root_large_values_moment_bound.md and primary https://arxiv.org/html/2204.03754v4 Theorem1.1(iii), AppendixA.3. You may now read conductor_resonant_patch_control.md for a separate narrow seam. Do not read sibling reports until your independent main derivation is written.

For each dyadic shell (N,2N] above X0=T^(52/125) and below T^(3/2), partition it into consecutive real intervals with starts x_j and lengths comparable to H4=N^(9/10)T^(-1/5), choosing starts independently of R. On each patch define r2sharp exactly from AppendixA.3, with R2=x_j^(1/20):

    rsharp(n)=4 sum_(R2<=d<R2²,d|n)chi4(d)(log n-log R2²)/log R2
             +4 sum_(d<R2,d|n)(chi4(d)+chi4(n/d)).

Candidate: after summing whole shells with this piecewise varying approximant, the complex smoothed wave of rsharp over n>X0 (ending at T^(3/2); full remaining tail paid by divisor/Schwartz bounds) has uniform physical supremum

    <= T^(13/84+epsilon) X0^(-103/840) + negligible
     = T^(13/125-13/52500+epsilon).

Prove or refute without inheriting a derivation. Audit the actual exponent-pair source phase class, proper intervals, chi4(n/d), varying patch cutoff/log coefficient variation, endpoint intervals and all tails. The subtlety is avoiding a factor equal to the number of patches. The fixed coefficient vector is divisor-bounded and independent of R, so generic large-value distribution from the accepted finite kernel may be used if justified. Candidate moment for this main is <=T^(29/25-1/2625+epsilon). Do not assume the residual has a paid ceiling or moment; this is only the explicit main.

Also review conductor_resonant_patch_control.md for its narrow actual-r2 lower bound; it makes no complete moment claim. Write strategy/round231_quadratic_signed_admission/reviews/type_i_main_and_resonance_review.md with seven protocol sections, exact proof/refutation and named seam verdicts, final SHA256. This is your sole further assignment and review/repair cycle; stop after report. Do not edit state, source report or conductor file.
