# Task brief: Fejér-cell owner and capacity audit

- Campaign: `m9-m2-hard-top-t1-residual-k26-near-peak-row-gram-anticoncentration-gate`
- Round: 180
- Role: hostile barrier/no-go auditor
- Access: selected context only
- Starting graph: `e94ef6a364988e47f8a59ca3589f03cb098a04a241ec841afc2efa6e685081b4`

## Objective

Hostilely rederive the proposed reduction from the near-peak off-row theorem
(180.G) to the literal K26 endpoint. Verify or refute the incidence-energy,
row-diagonal, cell-cover, Fejér-weight, far-arc, ordinary-zero, short-
correction, terminal-endpoint, and owner-scope seams. Then audit every
proposed signed contraction against the full false-control suite.

If the reduction is valid, determine the first unavoidable local capacity
or self-return. If it is invalid, stop at the first exact error. Do not
replace a literal lower bound by an adversarial capacity statement.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/round180_m2_hard_top_t1_residual_k26_near_peak_row_gram_strategy.md`
- `proofs/kernels/m9_m2_hard_top_t1_residual_whole_chain_scale_coboundary_positive_capacity_obstruction.md`
- `proofs/kernels/m9_m2_hard_top_t1_residual_maximal_fejer_dyadic_positive_transform_obstruction.md`
- `proofs/kernels/m9_m2_hard_top_t1_residual_tangent_fejer_commutator_self_return_obstruction.md`
- `proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md`
- `proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md`
- `rounds/codex-managed/full-proof-round175-177-strategy-literature-review/reviews/dependency_power_selection_seam_review.md`

## Required controls

- exact \(I_\nu\) partition modulo one and cell kernel;
- exact \(M\asymp L^2\) rather than a rounded surrogate;
- incidence-energy provenance and per-row length;
- diagonal versus off-row and physical versus fixed-dual diagonal;
- \(F_M\) on near cells and far arcs;
- Parseval normalization across both parity branches;
- collective ordinary-zero restoration and once-only short correction;
- dechirped complex, real-cosine, arbitrary-sign, one-row, one-site,
  all-\(1\bmod4\), erased-selector, exact-collision, and hard-boundary
  controls;
- product-collar, fixed-shift, minimal-scale, tangent, and scale-telescope
  no-repeat checks;
- exact local and endpoint power ledger; and
- downstream and exponent quarantine.

## Output contract

Write only
`rounds/codex-managed/m9-m2-hard-top-t1-residual-k26-near-peak-row-gram-anticoncentration-gate/reports/fejer_cell_owner_capacity_audit.md`.
Use the seven-section repository report contract. Give the exact first
failure or the exact verified implication, distinguish capacity from
literal mass, and recommend promote, retain, revise, reject, or no change.
Do not edit shared state or begin Round 181.
