# Task Brief: blind_cone_automorphy_feasibility

- Campaign: `m9-m1-lower-cone-indefinite-theta-completion-gate`
- Research round: `144` (`m9_m1_lower_cone_indefinite_theta_completion_gate`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `179e40fb38e6a5e26623c2584d469b1c4c8d5ae444a70d791298852f2d511204`
- Generated: `2026-08-23T21:17:02.146012+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Does the exact one-sided divisor-cone generating series for C(m) admit a source-legal signature-(1,1) indefinite-theta, mock, or Appell-Lerch completion whose complete transformation law yields the fixed-centre nonresonant cone target, or a strictly smaller owner-complete signed survivor; if not, what is the first exact lattice-kernel, isotropic-boundary, completion, source-hypothesis, complex-direction, mask, or capacity obstruction?

## Reference formula and distinctions

Let R=X^(1/4), N=floor X, M_*~R^2, k_m=floor(sqrt(Nm)+1/2), C(m)=sum_(hr=m,r odd,r>4h)chi_4(r), and F(tau)=sum_(h>=1,r>4h,r odd)chi_4(r)e(hr tau)=sum_(m>=1)C(m)e(m tau). The exact open scalar is T_N=sum_M sum_(m in [M,2M) intersect [1,M_*], |k_m^2-Nm|>sqrt M) m^(-3/4)V_low(R^2m/N)C(m)e(sqrt(Nm)), with target T_N<<_epsilon X^epsilon uniformly for every real X.

- The proposed automorphic object is F(tau), whose exponent hr is a genuine quadratic form. The nonlinear phase e(sqrt(Nm)) is not itself a theta phase and may not be relabelled as one.
- Round 63 already proved the exact pole-free moving level-four Appell identity and four-term completion. The genuinely new seam is reconciliation with the later Round-141/142 floor-free nonresonant owner, hard mask, rational hierarchy, and Abel return; rediscovery of the Appell identity is not progress.
- The lattice, quadratic and bilinear forms, strict cone, odd-r cosets, chi_4 factor, opposite cones, and both boundaries must be exact before any source theorem is invoked.
- One boundary is isotropic for Q(h,r)=hr. Any limiting, regularization, or Appell-Lerch passage must state its convergence, correction terms, multiplier, and cusp behavior.
- The holomorphic coefficient must remain exactly C(m). A completion that reconstructs r_2/4, a full divisor coefficient, or an opposite-cone combination is not an owner reduction unless the residual is proved target-safe.
- Every nonholomorphic, unary, boundary, residue, continuous, and cusp term is part of the owner ledger.
- A modular transformation must be converted into a lawful coefficient summation formula with a test class accepting the literal smooth weight and hard nonresonant mask. An individual complex direction may not be replaced by a cosine or conjugate pair without an exact bridge.
- The complete R-M-N power ledger must be compared with X^epsilon for the normalized scalar and with the accepted Round-142 owner. Formal automorphy or transform self-return is not a gain.
- This round concerns the Round-141/142 floor-free nonresonant cone scalar only. It cannot by itself promote the collar-tail cross term, complete lower GAR, either direct M1 parent, M9-M1, any M2 owner, endpoint, M9, or the global theorem.

## Assigned target

Independently classify the one-sided divisor-cone series, derive any exact completion and coefficient transformation from scratch, and determine whether its complete correction and boundary ledger can prove the fixed-centre scalar or yield a strict survivor.

## Permitted context

- `protocol.md`
- `rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/blind_statement.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `all strategy files`
- `all Round-108 and Round-138 through Round-144 nonblind artifacts`
- `all Round-144 sibling reports`

## Required controls

- `exact_signature_11_lattice_and_integrality`
- `strict_cone_kernel_opposite_cones_and_boundaries`
- `odd_coset_chi4_level_multiplier`
- `isotropic_boundary_regularization_and_convergence`
- `nonholomorphic_shadow_unary_residue_cusp_ledger`
- `holomorphic_coefficient_equals_C_not_complete_divisor`
- `primary_source_hypothesis_match`
- `coefficient_summation_formula_and_test_class`
- `individual_complex_direction_and_conjugate_control`
- `hard_nonresonant_mask_endpoints_and_owner`
- `round142_rational_spectrum_and_Abel_return_consistency`
- `full_R_M_N_capacity_and_downstream_scope`

## Required deliverables

- A seven-section statement-only analytic report.
- A self-contained lattice, cone, completion, transformation, and capacity analysis.
- A target estimate, strict signed survivor, or first rigorous obstruction.
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
