# Task Brief: actual_residual_short_shift_attack

- Campaign: `m9-m2-hard-top-t1-residual-fejer-short-shift-gate`
- Research round: `165` (`m9_m2_hard_top_t1_residual_fejer_short_shift_gate`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `87d58660e7e11a23eb3d8759917e02376479ba38acaf727b0a2dc15d5920f5e0`
- Generated: `2026-08-26T03:15:11.714406+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the exact one-sided aggregate actual residual Fejer short-shift correlation at length R=ceil(L) be bounded by L^2X^epsilon before any shiftwise absolute value, using the signed arithmetic of d'm'-dm=r, chi_4(d')chi_4(d), the literal selectors and profiles, and the square-root phase; or do gcd multiplicity, tangent hyperbola families, near-integral phase increments, parity, hard boundaries, or restored opening scales force a smallest rigorous actual-short-shift no-go?

## Reference formula and distinctions

C_(R,J,L)^rem=sum_(1<=r<R)(1-r/R)sum_N c_(N+r)^rem conjugate(c_N^rem)e(Jr/(sqrt(N+r)+sqrt(N))). Prove Re C_(R,J,L)^rem<=C_epsilon L^2X^epsilon. The literal opening is N=dm, N+r=d'm', d'm'-dm=r, with both supported squarefree residual coefficients, selectors, parity branches, profiles, boundaries, and zero extensions retained.

- J=sqrt(X), y=floor(J), q_X=X/y^2, H=floor(yX^(-1/4)), 1<<L<<H<=J^(1/2), and R=ceil(L).
- The coefficient c_N^rem is exactly the accepted Round-164 residual coefficient and is zero off its supported squarefree row domain.
- The required estimate is one-sided in the complete aggregate real part; no shiftwise, tuplewise, selectorwise, paritywise, or Mobius-opening absolute value is licensed.
- Opening gives the additive product shift d'm'-dm=r, not the separate multiplicative character-Poisson collar.
- The diagonal coefficient energy is L^(2+o(1)); arbitrary phase-aligned arrays can have Fejer energy L^3 and are mandatory false controls.
- A direct full-t1 scalar proof is allowed only with an exact scalar connector; target-safety of the XOR scalar does not imply energy equivalence.
- No t=1 result transfers automatically to other few-point channels, hard TOP, smooth M2 packets, M9-M2, M9, the bridge, or an exponent.

## Assigned target

Attack the complete one-sided actual residual short-shift correlation. Test exact additive-divisor, gcd/tangent, character-preserving, phase, delta, or completion mechanisms before every positive norm, and prove the target or isolate the smallest exact sufficient signed subform.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/round165_m2_hard_top_t1_residual_fejer_short_shift_strategy.md`
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/barrier_packet.md`
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/candidates/conductor_round165_short_shift_seed.md`
- `proofs/kernels/m9_m2_hard_top_t1_residual_transport_fejer_energy_reduction.md`
- `proofs/kernels/m9_m2_hard_top_t1_close_opposite_prime_exchange_sector.md`
- `proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md`
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-signed-divisor-transport-gate/synthesis.md`
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-signed-divisor-transport-gate/reports/complete_residual_transport_attack.md`

## Required controls

- `actual_residual_coefficient_domain`
- `aggregate_one_sided_real_part`
- `additive_product_shift_multiplicity`
- `gcd_tangent_and_determinant_coordinates`
- `chi4_progression_or_pairing`
- `square_root_phase_resonance`
- `selected_and_no_pair_rows`
- `odd_divisor_and_even_complement_branch`
- `hard_profile_endpoint_and_zero_extension`
- `phase_aligned_arbitrary_array`
- `scalar_vs_energy_connector`
- `rank_one_collar_geometry_separation`
- `missing_L_half_power`
- `remaining_few_point_and_downstream_scope`

## Required deliverables

- A seven-section analytic report satisfying the repository report contract.
- An exact literal expansion and every multiplicity, phase, profile, parity, and power ledger.
- A proof, owner-complete signed sector, or smallest rigorously scoped actual-short-shift frontier.
- Write only the assigned report and make no graph or shared-state edit.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
