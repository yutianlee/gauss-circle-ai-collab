# Task Brief: sqrt_divisor_twist_source_audit

- Campaign: `m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate`
- Research round: `141` (`m9_m1_lower_far_alias_incomplete_fibre_dispersion_gate`)
- Role: `source_auditor`
- Access mode: `selected_context`
- Graph SHA-256: `072e08848e9d368d65b89fbf03c36423a8e3662e7ae61c48052d4c352d1d71b0`
- Generated: `2026-08-23T18:19:00.620003+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the exact Round-140 far height-alias scalar be bounded at R X^epsilon by signed cancellation in its incomplete divisor coefficient across near-radical and nonsquare phase cells; if not, what is the first exact phase-cell, hyperbola, divisor-pairing, additive-twist, source-hypothesis, self-return, circularity, or capacity obstruction?

## Reference formula and distinctions

Let R=X^(1/4), y=floor(sqrt X), N=floor X=y^2+q, 0<=q<=2y, and fix 0<rho<1/8. Put L_h=floor(rho y/sqrt(h)), D_h=y-L_h-1, and let r_h be the least positive odd integer at least 4Nh/D_h^2. The exact grouped far coefficient is A_rho(m)=sum_(h|m, r=m/h odd, r>=r_h+2)chi_4(r). The frozen scalar is T_N=sum_(m>=1)m^(-3/4)V_low(R^2m/N)A_rho(m)e(sqrt(Nm)), effectively m<<N/R^2 asymp y, and the exact target is |T_N|<<_epsilon X^epsilon uniformly for every real X.

- The far mask is height-dependent and integer. Any simplification to r>2sqrt(m), a half-divisor sum, or the complete r_2(m)/4 coefficient must carry an exact target-safe correction.
- The known divisor upper bound and h=1 plateau show matching R^(1/2) excess in the grouped weighted sum before the outer N^(1/4) factor; modulus is not a proof.
- Exact radicals m=Dt^2 for N=Du^2 are target-safe, but near radicals and nonsquare phase cells have no accepted estimate.
- The phase sqrt(Nhr) is rank one and the second canonical transform returns the reciprocal phase. A claimed gain must be noninvertible or use actual signed arithmetic.
- Same-sign supported prime-square fibres and character-correct fourth-power rays rule out automatic fibrewise cancellation, but are not scalar lower bounds.
- The coefficient is a discontinuous divisor-incidence sequence. Any one-dimensional derivative theorem must prove the required coefficient variation or additive partial-sum hypothesis.
- Round 140 supplies unsquared scalar equivalence only. No positive energy, centre average, residual deletion, downstream theorem, or exponent change may substitute for the fixed-centre scalar target.

## Assigned target

Search primary literature for fixed-centre additive twists or Voronoi and exponent-pair estimates applicable to a square-root phase with a truncated chi_4-divisor coefficient. State exact theorems and map every hypothesis and exponent to the Round-141 scalar; certify a usable gain or prove that the located results are inapplicable, circular, averaged, coefficient-complete, or quantitatively insufficient.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/conductor_0823_full_proof_strategy.md`
- `rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/reviews/conductor_round140_height_alias_adjudication.md`
- `rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/synthesis.md`
- `rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/synthesis.md`

## Required controls

- `exact_incomplete_fibre_mask_floors_profiles_and_real_centre`
- `dyadic_m_range_weight_and_small_m_owner`
- `chi4_parity_divisor_pairing_and_complete_fibre_comparison`
- `phase_cell_definition_width_multiplicity_and_endpoints`
- `exact_radical_versus_near_radical_separation`
- `nonresonant_complement_target_return`
- `fourth_power_rays_and_prime_square_fibres`
- `coefficient_variation_or_additive_partial_sum_hypothesis`
- `source_theorem_parameter_and_R_power_audit`
- `canonical_transform_self_return_and_circularity`
- `fixed_centre_signed_directionality`
- `lower_GAR_and_downstream_scope`

## Required deliverables

- A seven-section source-audit report.
- Primary-source citations and exact theorem-hypothesis cards for every candidate result.
- A complete R-power translation certifying a usable theorem or the first rigorous source-level obstruction.
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
