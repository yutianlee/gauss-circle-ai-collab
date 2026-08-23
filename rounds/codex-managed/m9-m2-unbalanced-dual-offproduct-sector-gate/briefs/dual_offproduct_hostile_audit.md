# Task Brief: dual_offproduct_hostile_audit

- Campaign: `m9-m2-unbalanced-dual-offproduct-sector-gate`
- Research round: `125` (`m9_m2_unbalanced_dual_offproduct_sector_gate`)
- Role: `seam_reviewer`
- Access mode: `selected_context`
- Graph SHA-256: `27bd4173fbdb16e5689595a02d42d82ffa8bb514b4610ea745ce2da6e2b8b152`
- Generated: `2026-08-23T02:58:29.722041+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 99%.
- Numerical/experimental effort: at most 1%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the complete Round-124 dual off-product aggregate be bounded at the square target by a genuinely signed inequality, or can a violation be localized to a strictly smaller complete sector before this UNBAL lane is parked?

## Reference formula and distinctions

S_off=S_eq^(nonzero)+S_neq, with S_eq^(nonzero)=C_H sum_p sum_(0<|h|<H)(H-|h|)sum_k b_(p,k+h)conj(b_(p,k)) and S_neq=C_H sum_(p!=q)chi_4(p)chi_4(q)sum_(|h|<H)(H-|h|)sum_k b_(p,k+h)conj(b_(q,k)); prove S_off<<X^(1/2+epsilon).

- X real at least 2; M integer asymptotic to X with every physical amplitude frozen at X
- D=X^delta, L=X^ell, K=XL/D^2, H=ceil(X^(1/2)/D), K asymptotic to LH^2
- 1/4<=delta<1/2, 0<=ell<delta-1/4, 178ell+1638delta>463, and Q=D^2/(Lsqrt(X)) tending to infinity
- b_(p,k)=e(-1/8)M^(1/4)k^(-3/4)p^(-3/4)A_(p,k)e(sqrt(Mpk)) for positive odd p, with the literal moving profiles and zero extension
- C_H=(J+H-1)/H^2, exact triangular Fejer weight, all positive and negative shifts, block entries and exits
- D_0=C_H H sum_(p,k)|b_(p,k)|^2 is already O(X^(1/2))
- D_0+S_eq^(nonzero)=C_H sum_p sum_n |sum_(a<H)b_(p,n+a)|^2 is positive but may be a stronger norm than the target
- S_neq retains chi_4(p)chi_4(q), both ordered conjugates, moving p/k and q/k profiles, and no outside sectorwise modulus
- the full scalar S_off is target-equivalent modulo accepted packages to the physical Round-123 survivor
- the equal-mode and unequal-mode pieces may cancel, so separate absolute estimates are only sufficient
- product-defect, gradient, and joint stationary-return identities from Round 124 retained as barriers, not gains
- flat-smooth strict-UNBAL owner only; every hard, sharp, clipped, starred, arithmetic, nonflat, and transition owner excluded

## Assigned target

Hostilely audit sector splitting, positive p-row norms, crossing counts, character cancellation, moving profiles, endpoint ledgers, and every claimed factor in the Round-125 off-product proposal.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/conductor_0821_full_proof_strategy.md`
- `rounds/codex-managed/m9-m2-unbalanced-joint-stationary-lattice-gate/synthesis.md`
- `rounds/codex-managed/m9-m2-unbalanced-joint-stationary-lattice-gate/reports/joint_stationary_lattice_hostile_audit.md`
- `rounds/codex-managed/m9-m2-unbalanced-dual-offproduct-sector-gate/derivation_packet.md`

## Required controls

- `literal_Round124_dual_offproduct_survivor`
- `H_K_Q_normalization`
- `bpk_profile_and_character_placement`
- `Fejer_block_square_identity`
- `equal_mode_offzero_vs_positive_energy`
- `equal_mode_integer_crossings_and_curvature`
- `unequal_mode_product_gradient_defects`
- `unequal_mode_character_persistence`
- `sector_intercancellation`
- `negative_shift_conjugacy`
- `mode_shift_multiplicity`
- `moving_profile_and_zero_extension`
- `stationary_endpoint_and_error_scope`
- `signed_vs_unsigned_and_adversarial_coefficients`
- `capacity_before_and_claimed_gain`
- `owner_and_downstream_scope`

## Required deliverables

- A seven-section hostile report.
- A pass/fail seam table for exact identities, capacities, and endpoint scope.
- The maximal safe theorem or exact fatal correction.
- A precise state recommendation and parked survivor if the route fails.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
