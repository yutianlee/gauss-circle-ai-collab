# Task Brief: whole_moment_analytic_attack

- Campaign: `gc-whole-discrepancy-twelfth-moment`
- Research round: `201` (`whole_discrepancy_twelfth_moment`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `2f4448e999ab90387bca06498ddc60ee97b50f9900a9dfc6ad41fb201833c5f5`
- Generated: `2026-09-23T12:16:23.810602+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the complete whole-discrepancy twelfth moment be bounded by Y^(4+eta+epsilon) with eta<13theta_LY-4, using a fixed-window weighted square-root expansion; if not, what exact signed offdiagonal estimate and power gap remain?

## Reference formula and distinctions

T=sqrt(Y), delta=T^(-1/2), a_n(T)=r_2(n)n^(-3/4)Psi(sqrt(n/T)), H_T(R)=sum a_n(T)cos(2pi R sqrt(n)-3pi/4). Target int w(R/T)|H_T(R)|^12 dR << T^(1+2eta+epsilon). Expand all 2^12 signs with phase e(-3 sum signs/8) and T w-hat(-T sum signs sqrt(n)); retain nonzero differences signed.

- rho is fixed smooth radial nonnegative unit-mass compact disk support; w is fixed nonnegative smooth compactly supported away from zero and equals one on [1/sqrt(2),sqrt(3)].
- The exact-resonance class includes nonpairing relations within one squarefree radical; no probabilistic independence on the finite radius interval is assumed.
- Known low moments are normalization evidence, not a twelfth-moment theorem.
- Moment-to-pointwise theta=(1+p/4+eta)/(p+1); at p=12 it is (4+eta)/13. This route does not discharge M1 or M2 obligations.

## Assigned target

Derive the complete whole-discrepancy Poisson-Bessel expansion with delta=T^(-1/2) fixed across R~T, fixed a_n(T), exact all-sign twelfth-moment Fourier kernel, all errors/tails and real-radius endpoints. Reproduce the known second-moment upper exponent as normalization. Attack the complete twelfth-moment target, retaining signed displaced offdiagonal phase; if open, state its exact inequality and net eta deficit. You may audit primary standard Bessel/Poisson sources as needed and log exact hypotheses. Read only assigned context plus exact standard antecedents you identify. Write only your report.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/round201_whole_discrepancy_twelfth_moment_strategy.md`
- `strategy/gauss_circle_strategy_review_2026-09-23.md`
- `rounds/codex-managed/m9-m2-global-second-moment-exceptional-set/synthesis.md`

## Required controls

- `whole_discrepancy_scope`
- `fixed_window_smoothing`
- `inclusive_jump_error`
- `bessel_and_fourier_normalization`
- `uniform_tail_control`
- `all_sign_patterns`
- `nonpairing_exact_resonances`
- `displaced_offdiagonal_phase`
- `second_moment_normalization`
- `moment_to_pointwise_exponents`
- `primary_source_hypotheses`
- `no_parent_or_exponent_overclaim`

## Required deliverables

- Seven-section report with exact statements, proof/source audit, first open step, controls and state recommendation.
- Write only assigned report; no shared-state edits or next round.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
