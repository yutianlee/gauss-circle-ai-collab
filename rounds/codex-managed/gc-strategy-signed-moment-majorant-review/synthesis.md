# Round 202 synthesis

Campaign: gc-strategy-signed-moment-majorant-review. Date: 2026-09-23.
Scheduled strategy/current-literature review after Rounds199--201.
Starting graph SHA-256:
682cb189a3ab0ef26f8d19701e2949547446d37505df01f7b7eaf1cfdd0f359c.
Terminal decision: `strategy_review_with_complete_signed_next_target`.
All research was analytical/source-based; zero numerical experiments.

## Accepted result and its strict scope

The actual coefficients a_n(T)=r_2(n)n^(-3/4)Psi(sqrt(n/T)) have a
positive fixed band n~T whose balanced nonzero near-resonance subsum
has real weighted contribution at least cT^(5/2). The full exact mass
has already been removed. Thus a termwise absolute Fourier-kernel
majorant cannot prove the required T^(1+2eta+epsilon) when eta<3/4.
The desired improvement needs eta<0.088281287... .

The State Patch adds only
`GC-physical-twelfth-moment-absolute-majorant-obstruction`.
It does not lower-bound the complete signed moment, reject the actual
twelfth-moment target, or improve any pointwise exponent. All397 prior
nodes and all other graph data remain identical. The exact proof is
`proofs/kernels/gc_physical_twelfth_moment_absolute_majorant_obstruction.md`.

The proof uses a physical band coefficient mass >>T^(1/4), weighted
six-root bins numbering O(T^(3/2)), Cauchy, and deletion of O(1)
exact mass. Multiplication by the radius scale gives T^(5/2).
The statement-only derivation includes real endpoints, multiplicities,
all exact configurations, and the necessary signed/absolute distinction.
A separate exact-hash review checks the formal kernel and its continuum
control, which demonstrates that displaced signed cancellation remains
possible despite a large near-origin peak.

## Cutoffs and current literature

The source audit found no directly applicable new estimate for either
complete source. It retains two precise conditional Kloosterman imports
with full coefficient/mask/modulus/cost ledgers. Neither yet has an exact
transformation from the physical source. Pascadi's favorable example
includes prime squares; the September numerical paper is computational
evidence. The repaired Li--Yang benchmark is unchanged. Versions,
withdrawals, cone-trace limitations and source restrictions are recorded
in `reports/current_primary_methods_audit.md`.

The cutoff audit proves a complete low-head twelfth moment O(T) at
U=T^(1/2047), using an all-sign algebraic separation proof that also
handles dependent squareclasses. The full tail and every mixed stratum
remain. Its audited residual-estimate menu cannot beat eta0=0.148072478...
even when granted the favorable q0=262/27 endpoint. The first genuinely
new required input is therefore a signed tail estimate, not another
interpolation of those same inequalities.

## Strategy adjustment and complete next inequality

The full checkpoint is
`strategy/gauss_circle_strategy_checkpoint_round202_2026-09-23.md`.
Retain the whole-discrepancy route for the next analytical attempt,
preserving all other accepted routes. For fixed real chi supported
away from zero, w=chi^2, and U=T^(1/2047), define the actual signed
tail measure

\[
 \mu_{T,>U}=\tfrac12\sum_{n>U}a_n(T)
 [e(-3/8)\delta_{\sqrt n}+e(3/8)\delta_{-\sqrt n}],
 \quad K_T(\xi)=T\widehat\chi(T\xi).
\]

The complete tail twelfth moment is exactly ||K_T*mu_(T,>U)^{*6}||_2^2.
All signs, cross terms and large indices remain. The next candidate is

\[
 \|K_T*\mu_{T,>U}^{*6}\|_2\ll_\epsilon T^{29/50+\epsilon}.
\]

This is an unproved analytic target. Its exact identity and every
vanishing moment of K_T do not bound the arithmetic remainder.
If proved, it would give eta=2/25 and pointwise exponent102/325 after
the full T^7 reconstruction and persistence step. That milestone is
still weaker than one quarter; the full goal remains unchanged.
The analogous fixed higher-order hierarchy explains the relevance
of this coefficient-preserving direction to the eventual quarter goal.

## Closure and next boundary

Three task reports, a statement-only derivation, two separate seam
reviews, conductor independent analysis and reconciliation supply the
evidence. When worker handles disappeared during continuation, only
unsaved work was resumed; completed reports were preserved. The sole
formatting repair and the resolved radical-separation question are
recorded in the conductor review. The patch is applied only after
exact-hash reviews and green gates; reversal, replay, prior-record
equality and graph/campaign checks are recorded in
`controls/closure_validation.json`.

No full analytic saving has been proved in this round. Round203 is
designed only from this closed state and must attack the complete
filtered-convolution estimate, including an explicitly bounded remainder
for any proposed smooth-density subtraction. Round205 performs the next
scheduled broad strategy/current-literature review.
