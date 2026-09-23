# Task Brief: blind_fejer_short_shift_rederivation

- Campaign: `m9-m2-hard-top-t1-residual-fejer-short-shift-gate`
- Research round: `165` (`m9_m2_hard_top_t1_residual_fejer_short_shift_gate`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `87d58660e7e11a23eb3d8759917e02376479ba38acaf727b0a2dc15d5920f5e0`
- Generated: `2026-08-26T03:15:11.714406+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the exact one-sided aggregate actual residual Fejer short-shift correlation at length R=ceil(L) be bounded by L^2X^epsilon before any shiftwise absolute value, using the signed arithmetic of d'm'-dm=r, chi_4(d')chi_4(d), the literal selectors and profiles, and the square-root phase; or do gcd multiplicity, tangent hyperbola families, near-integral phase increments, parity, hard boundaries, or restored opening scales force a smallest rigorous actual-short-shift no-go?

## Reference formula and distinctions

C_(R,J,L)^rem=sum_(1<=r<R)(1-r/R)sum_N c_(N+r)^rem conjugate(c_N^rem)e(Jr/(sqrt(N+r)+sqrt(N))). Prove Re C_(R,J,L)^rem<=C_epsilon L^2X^epsilon. The literal opening is N=dm, N+r=d'm', d'm'-dm=r, with both supported squarefree residual coefficients, selectors, parity branches, profiles, boundaries, and zero extensions retained.

- J=sqrt(X), y=floor(J), q_X=X/y^2, H=floor(yX^(-1/4)), 1<<L<<H<=J^(1/2), and R=ceil(L).
- The coefficient c_N^rem is exactly the accepted Round-164 residual coefficient and is zero off its supported squarefree row domain.
- The required estimate is one-sided in the complete aggregate real part; no shiftwise, tuplewise, selectorwise, paritywise, or Mobius-opening absolute value is licensed.
- Opening gives the additive product shift d'm'-dm=r, not the separate multiplicative character-Poisson collar.
- The diagonal coefficient energy is L^(2+o(1)); arbitrary phase-aligned arrays can have Fejer energy L^3 and are mandatory false controls.
- A direct full-t1 scalar proof is allowed only with an exact scalar connector; target-safety of the XOR scalar does not imply energy equivalence.
- No t=1 result transfers automatically to other few-point channels, hard TOP, smooth M2 packets, M9-M2, M9, the bridge, or an exponent.

## Assigned target

Starting only from the frozen short-shift statement, independently derive exact additive near-product coordinates, character or phase cancellation mechanisms, and the first missing actual-direction theorem without shiftwise absolute values.

## Permitted context

- `protocol.md`
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/blind_statement.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `state/active_campaign.yml`
- `all strategy files`
- `all Round-165 nonblind artifacts`
- `all Round-165 sibling reports`
- `the Round-165 conductor seed`
- `all Round-164 reports, candidates, reviews, controls, kernels, and synthesis`
- `all earlier hard-TOP short-shift or divisor-transport artifacts`

## Required controls

- `actual_residual_coefficient_domain`
- `aggregate_one_sided_real_part`
- `additive_product_shift_multiplicity`
- `gcd_tangent_and_determinant_coordinates`
- `chi4_progression_or_pairing`
- `square_root_phase_resonance`
- `selected_and_no_pair_rows`
- `odd_divisor_and_even_complement_branch`
- `hard_profile_endpoint_and_zero_extension`
- `phase_aligned_arbitrary_array`
- `missing_L_half_power`
- `remaining_few_point_and_downstream_scope`

## Required deliverables

- A seven-section statement-only analytic report satisfying the repository report contract.
- An independent exact short-shift, multiplicity, resonance, and target-power derivation.
- A proof or the first rigorously isolated missing actual-direction estimate.
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
