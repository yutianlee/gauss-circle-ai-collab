# Task Brief: reciprocal_energy_attack

- Campaign: `m9-m2-top-endpoint-near-product-energy`
- Research round: `75` (`m9_m2_top_endpoint_near_product_energy`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `b5aa6150a62e1ecc21045c21bcb4af9ede4ab164545b43a93756e53fcc402bd2`
- Generated: `2026-08-14T14:27:31.821516+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 80%.
- Numerical/experimental effort: at most 20%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Does the exact top-M2 cone admit the character-preserving near-product identity and diagonal-scale reciprocal energy in (75.7)-(75.16), and can its actual-symbol off-diagonal be bounded?

## Reference formula and distinctions

sum_(|k|<<L X^epsilon)|sum_(tau,j odd)chi4(j)b_(tau,j,k)e(-kX/j)|^2 << L sqrt(X) X^epsilon.

- J=sqrt(X), 1<=L<=H<=J^(1/2)
- exact B=ceil(sqrt(L)) boundary collars and O(log L) layers
- actual l-dependent radial wavelet
- quarter-shift character transfer and e(1/8) constant
- Parseval diagonal L J and signed reciprocal off-diagonal
- character-leg self-return to the original top M2 block

## Assigned target

Repair the exact interface if needed and prove the actual-symbol reciprocal energy, a strict L-subrange, or a smaller survivor.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-m2-top-endpoint-near-product-energy/derivation_packet.md`
- `rounds/codex-managed/m9-m2-top-endpoint-near-product-energy/briefs/reciprocal_energy_attack.md`
- `rounds/codex-managed/m9-m2-top-endpoint-affine-cone/synthesis.md`
- `rounds/codex-managed/m9-m2-top-endpoint-affine-cone/reports/m2_affine_cone_attack.md`
- `rounds/codex-managed/m9-top-endpoint-transform/synthesis.md`

## Required controls

- `external_normalization`
- `hard_and_flat_boundary_collars`
- `actual_qX_and_layer_ownership`
- `quarter_shift_and_Gaussian_constant`
- `moving_l_symbol`
- `alias_and_layer_errors`
- `Poisson_measure`
- `Parseval_diagonal`
- `signed_offdiagonal`
- `character_self_return`
- `perfect_powers_and_adversarial_weights`
- `downstream_scope`

## Required deliverables

- rounds/codex-managed/m9-m2-top-endpoint-near-product-energy/reports/reciprocal_energy_attack.md

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
