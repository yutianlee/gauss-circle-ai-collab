# Brief: literal K17a cross-gcd alternating-fibre attack

- Campaign: `m9-m2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-gate`
- Round: 176
- Role: discovery
- Access: selected context only
- Starting graph: `9409651dccbbd1c69547546b245ba04c21d2a280173733ae37b693f9894c8b03`
- Output: `reports/literal_cross_gcd_alternating_fibre_attack.md`

## Frozen task

Attack the exact non-polylogarithmic K17a aggregate using the cross gcd and
parity-preserving determinant fibres frozen in the Round-176 strategy.
Derive both opposing orientations and the literal amplitude. Determine
whether the half-frequency \((-1)^t\), kept jointly across determinants
before every modulus, proves the full \(L^2X^\varepsilon\) target, an
owner-complete strict sector, or an exact first no-go.

The main mathematical work is to decide whether squarefree Möbius openings,
the selected/no-pair rule, the original gcd cutoff, and support transitions
preserve exploitable alternating variation. A strict-sector result must have
a complete complement and restored power ledger.

## Exact context

Read only:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/round176_m2_hard_top_t1_residual_k17a_cross_gcd_alternating_fibre_strategy.md`;
- `proofs/kernels/m9_m2_hard_top_t1_residual_transport_fejer_energy_reduction.md`;
- `proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md`;
- `proofs/kernels/m9_m2_hard_top_t1_residual_determinant_endpoint_polylog_shift_reduction.md`; and
- `proofs/kernels/m9_m2_hard_top_t1_close_opposite_prime_exchange_sector.md`.

## Required controls

Check multiplicity, both orientations, parity and two-adic branches,
cross-gcd versus original-gcd distinction, constant-amplitude full fibres,
short fibres, odd-square Möbius progressions, selected/no-pair rows,
canonical-solution jumps, endpoints, zero extension, phase aliases, and the
complete \(L^3\)-to-\(L^2\) ledger. Do not use a shiftwise or fibrewise
triangle as the proof.

## Output contract

Write exactly one seven-section report containing: result; exact statement
and hypotheses; proof or derivation; first doubtful or unproved step;
required control tests and outcomes; dependencies and exact artifacts used;
and recommended state effect. Do not edit shared state, siblings, candidates,
reviews, controls, or synthesis.
