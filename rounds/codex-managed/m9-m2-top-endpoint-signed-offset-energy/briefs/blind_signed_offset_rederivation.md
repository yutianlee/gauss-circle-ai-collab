# Task Brief: blind_signed_offset_rederivation

- Campaign: `m9-m2-top-endpoint-signed-offset-energy`
- Research round: `76` (`m9_m2_top_endpoint_signed_offset_energy`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `baa5fc13ca3682ae561c44cd1b20e94728c117378545f586ff3224c16a8eeb6b`
- Generated: `2026-08-14T15:15:21.757930+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 80%.
- Numerical/experimental effort: at most 20%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the complete alternating even-offset energy in (76.2) be bounded at L^2 X^epsilon, and does Poisson in m followed by the exact gcd-lift phase produce a genuine saving?

## Reference formula and distinctions

sum_m |sum_(h odd,m<=h<=4m) chi4(h)a(h,m)e(sqrt(Xhm))|^2 << L^2 X^epsilon.

- J=sqrt(X), 1<=L<=H<=J^(1/2)
- exact ceiling and both moving m-endpoints
- signed offset chi4(h)chi4(h+2r)=(-1)^r
- negative m-Poisson mode and saddle x*=C_(h,r)^2/(4k^2)
- gcd variables h=ga, h+2r=gb
- linear lift phase alpha_(a,b,k) and actual moving symbol

## Assigned target

Independently validate or refute the complete finite offset identity and candidate Poisson/gcd-lift normal form.

## Permitted context

- `rounds/codex-managed/m9-m2-top-endpoint-signed-offset-energy/derivation_packet.md`
- `rounds/codex-managed/m9-m2-top-endpoint-signed-offset-energy/briefs/blind_signed_offset_rederivation.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `all Round-75 and sibling Round-76 reports`
- `all source cards and literature`

## Required controls

- `exact_ceiling_stars_and_endpoints`
- `diagonal_and_fixed_offsets`
- `alternating_character_sign`
- `Poisson_orientation_and_Gaussian`
- `endpoint_Fresnel_and_error_sum`
- `gcd_parity_and_multiplicity`
- `linear_lift_phase`
- `actual_moving_symbol`
- `rank_one_self_return`
- `perfect_power_and_resonance_capacity`
- `downstream_scope`

## Required deliverables

- rounds/codex-managed/m9-m2-top-endpoint-signed-offset-energy/reports/blind_signed_offset_rederivation.md

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
