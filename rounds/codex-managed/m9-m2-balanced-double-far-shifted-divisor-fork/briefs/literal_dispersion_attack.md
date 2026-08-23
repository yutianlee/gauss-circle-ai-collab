# Task Brief: literal_dispersion_attack

- Campaign: `m9-m2-balanced-double-far-shifted-divisor-fork`
- Research round: `115` (`m9_m2_balanced_double_far_shifted_divisor_fork`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `6eb6eb5941e6d4720294c6b0890356113700db3201cf7c19337b96fb5ed47155`
- Generated: `2026-08-21T06:27:39.487204+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 98%.
- Numerical/experimental effort: at most 2%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

For the exact Round-114 double-far survivor, can the literal chi_4-twisted shifted-divisor coefficient be exposed and estimated by a genuinely noninvertible dispersion mechanism with one factor L of saving, or does its actual-symbol main term rigorously retain equal capacity and close this route?

## Reference formula and distinctions

For one persistent j=1 block, a_B^<(h,k)=chi_4(h) eta(gcd(h,k)/(sqrt L/2)) A_B(h,k) and E_(B,df)=sum_(|r|>L)sum_n e(R(sqrt n-sqrt(n+r))) C_B(n,r), where C_B(n,r)=sum_(hk=n,h'k'=n+r, |hk'-h'k|>L) a_B^<(h,k) conjugate(a_B^<(h',k')). The target is |E_(B,df)|<<L^3 X^epsilon at R=sqrt X asymp L^3 and K asymp L. The phase is constant within a fixed (n,r) fibre, so the required saving must act on the literal signed divisor correlation or on its outer shifted-product sum.

- X>=4096 real, R=sqrt X, persistent j=1, L asymp R^(1/3), and 1<=K/L<=16
- one fixed physical block B with the exact Round-113 real slanted symbol A_B and all floors, tapers, profiles, stars, and support crossings
- low-gcd weight eta(gcd(h,k)/(sqrt L/2)); high gcd, squares, near squares, transform error, and isolated exact-square j=2 retain prior owners
- full products n=hk and n+r=h'k'; determinant rho=hk'-h'k; only |r|>L and |rho|>L remain
- chi_4(h)chi_4(h') and the exact parity relation for p=h'-h must remain visible
- linear target L^(3/2), energy target L^3, and coefficient-blind double-far capacity L^4
- no absolute value may enter the inner divisor sum or the outer r,n sum unless the resulting capacity is explicitly paid
- distinct physical blocks and gcd shells may not be combined before their accepted one-count maps

## Assigned target

Starting only from the exact Round-114 survivor, construct and test the smallest noninvertible actual-symbol dispersion, Poisson, Mellin, or shifted-convolution inequality. Compute its main term first and prove a target-safe shift range, strict saving, full target, or exact failed seam.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/conductor_0821_full_proof_strategy.md`
- `rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/derivation_packet.md`
- `rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/candidates/conductor_shifted_divisor_fork.md`
- `rounds/codex-managed/m9-m2-balanced-literal-energy-connector-fork/synthesis.md`
- `rounds/codex-managed/m9-m2-balanced-literal-energy-connector-fork/reviews/conductor_round114_energy_and_corridors.md`
- `rounds/codex-managed/m9-m2-balanced-smooth-quarter-packet-canonicalization/reports/balanced_packet_actual_symbol_formalization.md`

## Required controls

- `literal_full_product_to_divisor_pair_identity`
- `determinant_gate_after_divisor_substitution`
- `increment_chart_and_parity_character`
- `gcd_cutoff_and_slanted_symbol_retention`
- `inner_vs_outer_cancellation`
- `zero_frequency_and_main_term`
- `shift_range_and_conductor_uniformity`
- `linear_vs_energy_capacity`
- `actual_symbol_vs_phase_adapted_control`
- `double_far_owner_and_corridor_scope`
- `fixed_block_and_no_shellwise_l1`
- `critical_j1_and_exact_square_j2_boundary`
- `external_theorem_hypothesis_fit`
- `downstream_scope`

## Required deliverables

- A seven-section discovery report.
- An exact noninvertible transform or inequality with every main term and norm displayed.
- The best proved target-safe range, saving, obstruction, or first failed seam.
- A precise state recommendation.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
