# Task Brief: literal_two_defect_commutator_attack

- Campaign: `m9-m2-balanced-critical-j1-two-defect-commutator-gate`
- Research round: `171` (`m9_m2_balanced_critical_j1_two_defect_commutator_gate`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `4c98bb13558c06159c5ad23128c6f6ff52970db296863858832309a24a4720ac`
- Generated: `2026-08-26T11:35:46.812755+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Does the complete persistent critical j=1 balanced double-far zero-subtracted scalar admit an exact two-direction defect commutator identity that preserves every literal weight and saves one factor L before positive norms, or what is the first exact identity, axial, boundary, restoration, capacity, or ruling no-go?

## Reference formula and distinctions

For a_B^<(h,k)=chi_4(h) eta((h,k)/(sqrt L/2)) A_B(h,k), Delta=h'k'-hk, rho=hk'-h'k, and df={|Delta|>L,|rho|>L}, prove |R_B^osc|<<_epsilon L^3X^epsilon, where R_B^osc=sum_df a_B^<(h,k)conj(a_B^<(h',k'))[e(sqrt X(sqrt(hk)-sqrt(h'k')))-1]. With h'=h+p and k'=k+q, Delta+rho=q(2h+p) and Delta-rho=p(2k+q). These are coordinates, not a proved commutator.

- The target is scoped only to persistent critical j=1 blocks with L asymp X^(1/6).
- Positive capacity is L^4X^epsilon; exactly one factor L must be saved before a positive norm.
- On character support p=2s and chi_4(h)chi_4(h+p)=(-1)^s, constant on fixed-p fibres.
- The p=0 and q=0 axial sectors may satisfy both far gates and cannot be divided away.
- The phase-free term, true diagonal, and two width-L corridors are target-safe, but fixed-Q rulings remain.
- Full BAL separately requires M9-M2-balanced-remaining-label-owner-quantifier-completion.
- No critical-child result implies hard TOP, UNBAL, M1, GAR, endpoint assembly, a bridge, or an exponent theorem.

## Assigned target

Derive the complete literal (h,k,p,q) coordinate domain and attempt an exact two-direction discrete commutator or summation-by-parts identity for R_B^osc. Prove the target, prove an owner-complete strict sector, or stop at the first exact identity, complement, restoration, or capacity no-go.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/round171_m2_balanced_critical_j1_two_defect_commutator_strategy.md`
- `rounds/codex-managed/m9-m2-balanced-critical-j1-two-defect-commutator-gate/barrier_packet.md`
- `rounds/codex-managed/full-proof-round167-169-strategy-literature-review/synthesis.md`
- `rounds/codex-managed/full-proof-round167-169-strategy-literature-review/reports/full_graph_frontier_reconstruction.md`
- `rounds/codex-managed/m9-m2-balanced-literal-energy-connector-fork/synthesis.md`
- `rounds/codex-managed/m9-m2-balanced-literal-energy-connector-fork/reviews/conductor_round114_energy_and_corridors.md`
- `rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/synthesis.md`
- `rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/reviews/conductor_round115_identity_and_zero_mode.md`
- `rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/synthesis.md`
- `rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/reviews/conductor_round136_broad_narrow_adjudication.md`

## Required controls

- `literal_critical_j1_scope`
- `coordinate_bijection_and_multiplicity`
- `Delta_rho_factorizations`
- `two_discrete_difference_identity`
- `fixed_p_character_constancy`
- `p0_q0_axial_sectors`
- `sharp_far_gate_and_support_boundaries`
- `phase_free_subtraction_scope`
- `fixed_Q_rulings`
- `gcd_slanted_symbol_and_alias_restoration`
- `endpoint_and_real_centre_restoration`
- `positive_capacity_factor_L`
- `target_safe_complement`
- `no_positive_norm_before_saving`
- `owner_quantifier_quarantine`
- `no_in_round_pivot`
- `no_status_or_exponent_overpromotion`

## Required deliverables

- A seven-section analytic report satisfying the repository report contract.
- An exact coordinate, identity, boundary, axial, complement, and restored-power ledger.
- A proof, strict-sector lemma, or first exact route-specific no-go with recommended state effect.
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
