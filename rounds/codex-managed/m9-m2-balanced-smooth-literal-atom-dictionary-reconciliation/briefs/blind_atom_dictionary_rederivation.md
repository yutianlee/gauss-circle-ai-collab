# Task Brief: blind_atom_dictionary_rederivation

- Campaign: `m9-m2-balanced-smooth-literal-atom-dictionary-reconciliation`
- Research round: `113` (`m9_m2_balanced_smooth_literal_atom_dictionary_reconciliation`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `9d560539df2db7d69e72dd6e7e6af7247f00237ee795ac13b053b3f34eae8efa`
- Generated: `2026-08-21T01:41:12.870065+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 98%.
- Numerical/experimental effort: at most 2%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the accepted denominator profile, clipped odd-frequency partition, Vaaler coefficient, smooth stationary transform, gcd partition, and prior-owner corrections be instantiated as one finite coefficientwise atom dictionary for every balanced smooth M2 residual block?

## Reference formula and distinctions

For each literal residual block B, define its normalized positive-frequency coefficient a_B(h,k), its exact smooth-gcd partition, the full quarter packet Q_B, and target-safe square, near-square, high-gcd, and transform-error corrections so that the physical block equals 8 Re[-e(1/8)X^(1/4)(LK)^(-3/4)T_B/(2pi)] and the residual T_B is exactly the full quarter packet minus the prior-owner corrections.

- y=floor(sqrt X), D_j=2^(-j)y, and the one hard plus full smooth denominator profiles
- H_D=floor(DX^(-1/4)) and an exact clipped positive-frequency partition including top and bottom pieces
- Phi(u)=pi u(1-u)cot(pi u)+u and the exact positive M2 normalization
- balanced ratio 1<=K/L<=16 with K=XL/D^2
- full slanted stationary symbol and smooth support crossings
- a fixed finite smooth gcd partition with an explicit high-gcd boundary owner
- square, near-square, high-gcd, transform-error, sign, and conjugacy tags
- one-count equality and scale-normalized seminorms uniform in real X

## Assigned target

Independently test the frozen explicit dictionary statement: prove its finite partitions, constants, one-count equation, and first missing datum using only the statement packet.

## Permitted context

- `problems/gauss_circle.md`
- `state/control_models.md`
- `rounds/codex-managed/m9-m2-balanced-smooth-literal-atom-dictionary-reconciliation/blind_statement.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `strategy files`
- `Round-113 derivation packet and candidate`
- `all earlier balanced-packet derivations and all Round-113 sibling reports`

## Required controls

- `denominator_telescoping_and_hard_profile`
- `frequency_telescoping_top_bottom_and_clipping`
- `height_floor_and_empty_block`
- `exact_Phi_and_positive_frequency_constant`
- `positive_negative_frequency_recombination`
- `balanced_ratio_boundary_and_real_X`
- `smooth_gcd_one_count_and_boundary_owner`
- `square_near_square_and_large_gcd_priority`
- `false_arithmetic_mask_and_unsigned_models`
- `capacity_and_downstream_scope`

## Required deliverables

- A seven-section statement-only report.
- A coefficientwise proof or exact counterexample to the dictionary.
- The first doubtful datum and a precise state recommendation.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
