# Task Brief: blind_residual_transport_rederivation

- Campaign: `m9-m2-hard-top-t1-residual-signed-divisor-transport-gate`
- Research round: `164` (`m9_m2_hard_top_t1_residual_signed_divisor_transport_gate`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `81690ebb72b0dedd99bdb6c6127f947df696a901a22af3f65ac8738209125306`
- Generated: `2026-08-26T00:49:39.102222+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the complete literal residual t=1 scalar after subtracting exactly the Round-163 close-opposite-prime XOR incidence sector be bounded by L^(3/2)X^epsilon through an exact cumulative signed-divisor or monotone-transport identity, possibly retaining cross-N square-root phase cancellation; or do unmatched sign mass, transport distance, hard amplitude jumps, diagnostic semiprime capacity, rank-one product geometry, or restored powers repay the full L^(1/2-o(1)) gain?

## Reference formula and distinctions

S_(L,1)^rem=sum_(N asymp L^2)mu^2(N)(L^2/N)^(3/4)e(Jsqrt(N)) sum_(d|N,d odd)chi4(d)rho_N(d)A_N(d), where rho_N is one if no pair was selected and otherwise retains exactly neither/both selected-prime incidences. A_N is the literal zero-extended eta_L Phi W amplitude with every half-open shell, cone, floor, star, endpoint, and parity convention. The target is |S_(L,1)^rem|<<_epsilon L^(3/2)X^epsilon.

- J=sqrt(X), y=floor(J), q_X=X/y^2, H=floor(yX^(-1/4)), and 1<<L<<H<=J^(1/2).
- For each N, the accepted selector depends on N,L,kappa and not on the divisor allocation; it may be absent.
- The residual contains every no-pair product and every neither-selected-prime or both-selected-prime incidence, with the accepted XOR sector subtracted exactly once.
- For ordered residual odd divisors d_i, sigma_i=chi4(d_i), and C_j=sum_(i<=j)sigma_i, exact Abel gives sum_i sigma_i A_i=C_r A_r+sum_(j<r)C_j(A_j-A_(j+1)).
- Equal-mass monotone transport, unequal sign mass, hard jump terms, and zero-extension cemetery terms are distinct.
- The outer phase e(Jsqrt(N)) is constant within one N but must remain available across N if positive transport exceeds target.
- Positive capacity may be L^(2+o(1)); the target requires L^(1/2-o(1)) cancellation after every literal cost.
- No t=1 result transfers automatically to other few-point channels, hard TOP, smooth M2 packets, M9-M2, M9, the bridge, or a global exponent.

## Assigned target

Starting only from the frozen residual statement, independently derive the exact ordered-divisor Abel or Stieltjes identity, unequal-mass correction, hard-jump terms, target power ledger, and the first necessary cross-N theorem if within-product transport does not close.

## Permitted context

- `protocol.md`
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-signed-divisor-transport-gate/blind_statement.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `state/active_campaign.yml`
- `all strategy files`
- `all Round-164 nonblind artifacts`
- `all Round-164 sibling reports`
- `the Round-164 conductor seed`
- `all Round-163 reports, candidates, reviews, controls, kernels, and synthesis`
- `all earlier residual or divisor-transport campaign artifacts`

## Required controls

- `residual_exact_subtraction`
- `ordered_divisor_abel_identity`
- `odd_divisor_and_even_N_branch`
- `sign_mass_and_unmatched_atoms`
- `monotone_transport_normalization`
- `profile_jump_and_zero_extension_variation`
- `outer_N_phase_preservation`
- `arbitrary_real_centre_phase`
- `missing_L_half_power`
- `physical_coefficient_vs_diagnostic`
- `remaining_few_point_and_downstream_scope`

## Required deliverables

- A seven-section statement-only analytic report satisfying the repository report contract.
- An independent exact residual, cumulative-discrepancy, unmatched-mass, hard-jump, and target-power derivation.
- A target theorem or first rigorously isolated missing within-N or cross-N estimate.
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
