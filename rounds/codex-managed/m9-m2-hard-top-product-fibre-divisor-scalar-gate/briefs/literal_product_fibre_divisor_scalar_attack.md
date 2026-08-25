# Task Brief: literal_product_fibre_divisor_scalar_attack

- Campaign: `m9-m2-hard-top-product-fibre-divisor-scalar-gate`
- Research round: `137` (`m9_m2_hard_top_product_fibre_divisor_scalar_gate`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `3c5003b1478d78b8469d4220ad305bb06ee0f869b9c4a741e7211642eeb52cc7`
- Generated: `2026-08-23T15:11:54.340043+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

After the proved hm-square entry sector is removed, can the literal hard-TOP scalar be regrouped by n=hm and bounded at L^(3/2) through the actual truncated chi_4-divisor coefficient, uniformly for every real centre and every polynomial intermediate L; if not, what is the first exact divisor, resonance, completion, self-return, circularity, or capacity obstruction?

## Reference formula and distinctions

T_L^ns=L^(3/2) sum_(n asymp L^2, n not square) n^(-3/4) C_L(n)e(J sqrt(n)), where C_L(n)=sum_(h|n, h odd, sqrt(n)<=h<=2sqrt(n)) chi_4(h) eta_L(h) Phi(h/(H+1)) W(sqrt(q_X h^2/(4n))), J=sqrt(X), y=floor(J), q_X=X/y^2, H=floor(yX^(-1/4)), and the target is |T_L^ns|<<_epsilon L^(3/2)X^epsilon.

- a_end(h,m)=eta_L(h)Phi(h/(H+1))(L^2/(hm))^(3/4)W(sqrt(q_Xh/(4m))) on ceil(h/4)<=m<=h, with h odd
- the exact product-fibre bijection n=hm, h|n, sqrt(n)<=h<=2sqrt(n), m=n/h
- the proved square-entry energy gives |T_L^square|<<L^(5/4)X^epsilon, so only n nonsquare remains
- n asymp L^2, |C_L(n)|<=tau(n), raw scalar capacity L^(2+o(1)), and target L^(3/2+o(1))
- f'(n)=J/(2sqrt(n)) asymp J/L and f''(n)=-J/(4n^(3/2)) asymp -J/L^3
- the near-square divisor truncation, chi_4, Vaaler taper, dyadic height profile, endpoint W, floors, hard edge, zero extension, nonsquare condition, and real q_X are literal
- support-only, parity-only, ambient spectral, product-fibre averaging, entrywise phase alignment, and positive-energy equivalence are parked controls

## Assigned target

Exploit the exact truncated chi_4-divisor coefficient in the n=hm scalar to prove the L^(3/2) target, a strict smaller signed survivor, or the first exact arithmetic/capacity obstruction.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/conductor_0823_full_proof_strategy.md`
- `rounds/codex-managed/m9-top-endpoint-transform/synthesis.md`
- `rounds/codex-managed/m9-m2-top-endpoint-affine-cone/synthesis.md`
- `rounds/codex-managed/m9-m2-hard-top-actual-vector-spectral-gate/blind_statement.md`
- `rounds/codex-managed/m9-m2-hard-top-actual-vector-spectral-gate/synthesis.md`
- `rounds/codex-managed/full-proof-frontier-inequality-selection-gate/synthesis.md`
- `rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/blind_statement.md`

## Required controls

- `literal_hard_cone_and_square_projection`
- `exact_product_fibre_bijection`
- `truncated_chi4_divisor_coefficient`
- `hard_profile_floor_and_real_centre`
- `nonsquare_and_full_divisor_controls`
- `phase_derivatives_and_resonant_dual_modes`
- `one_dimensional_scalar_capacity`
- `completion_bprocess_and_self_return`
- `coefficient_directionality_and_phase_alignment`
- `uniformity_in_L_and_X`
- `boundary_and_owner_scope`
- `full_hard_TOP_and_downstream_scope`

## Required deliverables

- A seven-section analytic report.
- An exact product-fibre coefficient dictionary and complete L-power ledger.
- A target estimate, strict smaller survivor, or first exact product-fibre obstruction.
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
