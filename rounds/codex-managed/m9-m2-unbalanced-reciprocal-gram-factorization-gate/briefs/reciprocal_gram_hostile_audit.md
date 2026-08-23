# Task Brief: reciprocal_gram_hostile_audit

- Campaign: `m9-m2-unbalanced-reciprocal-gram-factorization-gate`
- Research round: `123` (`m9_m2_unbalanced_reciprocal_gram_factorization_gate`)
- Role: `seam_reviewer`
- Access mode: `selected_context`
- Graph SHA-256: `d29ae6c0f398cc2df699b15ee2901b525290263b6cde5eecece49cdeee095bb1`
- Generated: `2026-08-21T19:16:58.382488+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 99%.
- Numerical/experimental effort: at most 1%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the exact flat-smooth UNBAL wave be phase-integerized at target-safe cost and then bounded through a character-preserving joint frequency Gram whose reciprocal aliases factor around N^2, or does the construction rigorously self-return?

## Reference formula and distinctions

R_X=sum_(r odd)chi_4(r)W(X/(rD))sum_k q_L(4Xk/r^2)k^(-1)e(Xk/r), with D=X^delta, L=X^ell, R=X/D, K=XL/D^2, and target R_X<<X^(1/4+epsilon).

- X real at least 2 and N=floor X
- 1/4<=delta<1/2, 0<=ell<delta-1/4, and 178ell+1638delta>463
- literal fixed q_L and W profiles, including support overlap and edges
- phase-only integerized row with amplitudes still frozen at X
- physical product kernels centred at X and N with denominator 4X
- weighted k-Cauchy Gram and its full signed ordered-pair expansion
- diagonal r=s and every off-diagonal reciprocal alias
- j nearest N(1/r-1/s), E=N(s-r)-jrs, and (N-jr)(N+js)-N^2=jE
- N=2^tN_0, exact and near collisions, negative and zero aliases, and mod-four character signs
- flat-smooth owner only; every hard, sharp, starred, clipped, arithmetic, and transition owner excluded

## Assigned target

Hostilely audit the perturbation norm, Gram target equivalence, diagonal cancellation burden, factor and character algebra, alias windows, endpoint scope, circularity, and duplication of prior transforms.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/conductor_0821_full_proof_strategy.md`
- `rounds/codex-managed/m9-m2-smooth-unbalanced-divisor-recombination/reviews/conductor_round107_recombination_and_capacity.md`
- `rounds/codex-managed/m9-m2-balanced-nonzero-alias-defect-gate/synthesis.md`
- `rounds/codex-managed/m9-m2-unbalanced-prescribed-centre-wave-gate/synthesis.md`
- `rounds/codex-managed/m9-m2-unbalanced-reciprocal-gram-factorization-gate/derivation_packet.md`

## Required controls

- `literal_Round118_flat_wave`
- `phase_integerization_physical_kernel`
- `reciprocal_termwise_false_charge`
- `weighted_Gram_normalization`
- `diagonal_capacity`
- `smooth_alias_localization`
- `alias_product_factorization`
- `two_adic_character_sign`
- `exact_versus_near_collision`
- `zero_and_negative_aliases`
- `signed_offdiagonal_aggregation`
- `old_transform_return`
- `owner_and_downstream_scope`

## Required deliverables

- A seven-section hostile report.
- A pass/fail seam table with normalization, parity, capacity, and scope controls.
- The maximal safe theorem or fatal correction and exact smallest survivor.
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
