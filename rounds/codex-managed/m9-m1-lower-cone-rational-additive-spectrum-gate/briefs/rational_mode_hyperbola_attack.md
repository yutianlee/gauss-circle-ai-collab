# Task Brief: rational_mode_hyperbola_attack

- Campaign: `m9-m1-lower-cone-rational-additive-spectrum-gate`
- Research round: `142` (`m9_m1_lower_cone_rational_additive_spectrum_gate`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `de02111a1831d30da33c9f4b2d4a549efa1942dcdc32b5d829e671f6ad5e0e76`
- Generated: `2026-08-23T19:10:21.063256+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the rational additive spectrum of the exact Round-141 cone coefficient be extracted uniformly enough to prove its fixed-centre nonresonant square-root twist, or to reduce it to a strictly smaller owner-complete rational-slope survivor; if not, what is the first exact denominator-uniformity, major-arc accumulation, periodic-branch, endpoint, source-hypothesis, self-return, or capacity obstruction?

## Reference formula and distinctions

Let R=X^(1/4), y=floor(sqrt X), N=floor X=y^2+q_X with 0<=q_X<=2y, and C(m)=sum_(hr=m, r odd, r>4h)chi_4(r). On dyadic I_M=[M,2M) within m<=C_VN/R^2, put k_m=floor(sqrt(Nm)+1/2), j_m=k_m^2-Nm. The exact open scalar is T_nr=sum_M sum_(m in I_M, |j_m|>sqrt M)m^(-3/4)V_low(R^2m/N)C(m)e(sqrt(Nm)), with target |T_nr|<<_epsilon X^epsilon.

- Round 141 proves the exact quarter-frequency asymptotic sum_(m<=M)C(m)e(m/4)=i*pi*M/8+O(M^(1/2)); it does not prove that 1/4 is the only rational main mode.
- For a reduced rational alpha=a/q, unfold S_C(M;alpha)=sum_(4h^2<M)sum_(4h<r<=M/h, r odd)chi_4(r)e(alpha h r). Any row mean, residue class, main constant, and error must be derived with exact endpoints.
- A fixed-q asymptotic is not a q-uniform major-arc theorem. Every use in local slope cells must state the allowed q range, arc width, overlap, endpoint convention, and total weighted q-sum.
- Subtracting a finite periodic projection is useful only if its nonlinear square-root branch is target-safe and the residual has the exact additive partial-sum control required on every complementary slope cell.
- The nonresonant condition |j_m|>sqrt M concerns phase values, not derivative distance. It may not be used as a rational-slope separation without a proved implication.
- Raw rational-mode capacity, a main term in a coefficient Fourier transform, or a real radial cosine estimate is not a lower bound or bound for the signed fixed-centre complex scalar.
- Round 141 supplies an unsquared scalar equivalence only. No lower GAR, direct M1, M9-M1, M2, endpoint, M9, quarter, or exponent promotion follows without its separate owner.

## Assigned target

Derive the exact rational additive spectrum of the cone coefficient. Prove a fixed- and growing-denominator asymptotic for S_C(M;a/q), compute every nonzero main constant, and test whether a denominator-truncated spectral subtraction yields a residual with target-useful uniform additive partial sums and a target-safe reconstruction error.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/conductor_0823_full_proof_strategy.md`
- `rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/candidates/conductor_round141_cone_nonresonant_reduction.md`
- `rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/reviews/conductor_round141_incomplete_fibre_adjudication.md`
- `rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/synthesis.md`

## Required controls

- `exact_cone_hyperbola_endpoints_and_parity`
- `reduced_rational_frequency_and_q_mod_4_cases`
- `row_mean_residue_classes_sign_and_constant`
- `fixed_q_versus_growing_q_error_uniformity`
- `rational_spectrum_convergence_and_reconstruction`
- `local_derivative_arc_width_overlap_and_multiplicity`
- `nonresonant_phase_value_versus_slope_distinction`
- `residual_additive_partial_sum_hypothesis`
- `raw_capacity_versus_fixed_centre_signed_scalar`
- `canonical_transform_self_return_and_downstream_scope`

## Required deliverables

- A seven-section analytic report.
- An exact rational-frequency theorem with all constants and a complete M-, q-, and R-power ledger.
- A target estimate, strict owner-complete rational-spectrum survivor, or first rigorous denominator-accumulation or reconstruction obstruction.
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
