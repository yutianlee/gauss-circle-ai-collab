# Task Brief: double_poisson_product_defect_attack

- Campaign: `m9-m2-unbalanced-joint-stationary-lattice-gate`
- Research round: `124` (`m9_m2_unbalanced_joint_stationary_lattice_gate`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `2b60eca238542d4f321a19c90f20163c6dd4cd7c60da6f324910b6db10b638c6`
- Generated: `2026-08-23T02:15:32.715428+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 99%.
- Numerical/experimental effort: at most 1%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the complete Round-123 signed nonzero, nonexact near-alias shifted energy be bounded by a genuinely joint stationary-lattice inequality, or does the full character-Poisson stationary map rigorously self-return?

## Reference formula and distinctions

V_(M,H0)=sum_(r,s odd; j!=0,E!=0,|E|<=X^(1+rho)/L) chi_4(r)chi_4(s)Gamma_(M,H0)(r,s), with H0=ceil(X^(1/2)/D), target V_(M,H0)<<X^(1/2+epsilon), and Gamma the exact Round-123 block-square kernel.

- X real at least 2; M integer asymptotic to X with all physical amplitudes frozen at X
- D=X^delta, L=X^ell, R=X/D, K=XL/D^2, 1/4<=delta<1/2, 0<=ell<delta-1/4, and 178ell+1638delta>463
- H0=ceil(X^(1/2)/D), so K is asymptotic to L H0^2 and 1<=H0<<K
- literal W_r and q_(r,k), zero extension, block endpoints, Fejer weight, and exact prefactor (J+H0-1)/H0^2
- the full real ordered-pair sum with positive and negative aliases, defects, shifts, and conjugates retained
- j nearest M(1/r-1/s), E=M(s-r)-jrs; the accepted j=0, nonzero exact-alias, and rapid-tail packages kept distinct
- both chi_4 expansions and all quarter-shift Poisson modes on the r and s legs
- candidate positive odd stationary modes p,q asymptotic to L, their exact stationary points, phases, amplitudes, boundary and nonstationary remainders
- candidate dual product defect N=p(k+h)-qk and the exact relation between the dual k-gradient and the primal reciprocal alias
- dual diagonal p=q,h=0, equal-mode shifted sector p=q,h!=0, and unequal-mode sector p!=q treated separately before any norm
- flat-smooth strict-UNBAL owner only; every hard, sharp, clipped, starred, arithmetic, and transition owner excluded

## Assigned target

Exploit the complete dual product-defect lattice before absolute values, seeking a target bound, a strict equal-mode or unequal-mode gain, or a stronger complete-aggregate inverse theorem.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/conductor_0821_full_proof_strategy.md`
- `rounds/codex-managed/m9-m2-unbalanced-reciprocal-gram-factorization-gate/synthesis.md`
- `rounds/codex-managed/m9-m2-unbalanced-reciprocal-gram-factorization-gate/reports/signed_alias_product_attack.md`
- `rounds/codex-managed/m9-m2-unbalanced-reciprocal-gram-factorization-gate/reviews/conductor_round123_integerization_gram_adjudication.md`
- `rounds/codex-managed/m9-m2-unbalanced-joint-stationary-lattice-gate/derivation_packet.md`

## Required controls

- `literal_Round123_near_alias_survivor`
- `H0_K_normalization`
- `double_character_Poisson_signs`
- `stationary_points_and_Gaussian_units`
- `dual_product_defect`
- `dual_gradient_to_primal_alias`
- `dual_diagonal_one_count`
- `equal_mode_shifted_sector`
- `unequal_mode_sector`
- `mode_shift_alias_multiplicity`
- `character_persistence`
- `stationary_endpoint_and_error_ledger`
- `signed_joint_aggregation`
- `transform_involution_and_norm_scope`
- `owner_and_downstream_scope`

## Required deliverables

- A seven-section analytic report.
- A complete dual stationary formula or a precise statement of the first invalid transform seam.
- A joint inequality, strict safe sector, inverse theorem, or exact self-return with capacity accounting.
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
