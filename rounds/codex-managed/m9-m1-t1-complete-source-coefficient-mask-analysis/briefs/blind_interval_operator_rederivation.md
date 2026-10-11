# Task Brief: blind_interval_operator_rederivation

- Campaign: `m9-m1-t1-complete-source-coefficient-mask-analysis`
- Research round: `200` (`complete_source_coefficient_mask_analysis`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `2f4448e999ab90387bca06498ddc60ee97b50f9900a9dfc6ad41fb201833c5f5`
- Generated: `2026-09-23T11:45:02.347606+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the complete original-t=1 residual even-shift source, with P1 and P2 recombined, be bounded at L^2 X^epsilon; otherwise what exact coefficient norm or unmasked analytic estimate is missing after every mask and reconstruction cost?

## Reference formula and distinctions

C_even=sum_(0<r<R0, 2|r)(1-r/R0) sum_N c_(N+r,sigma)^rem conjugate(c_(N,sigma)^rem) e(sigma sqrt(X) r/(sqrt(N+r)+sqrt(N))), R0=ceil(L). Target Re C_even << L^2 X^epsilon; c and total zero-extended lambda are exactly K185.1--3. E_R<=2D+4Re C_even and scalar prefactor O(L).

- Complete source precedes P_cl/P1/P2, both opposing orientations, all gcd/height/packet splits and later T branches.
- A partition identity removes artificial partition boundaries only for a common genuine transport; it provides no analytic saving.
- Geometric interval masks require a proved unmasked all-vector bilinear estimate and a controlled product or projective norm.
- No t>=2, complete M1/M2, bridge, target or exponent conclusion is implied by a t=1 result.

## Assigned target

Independently prove or refute every finite statement in the independent statement packet, including interval-mask, mixed-amplitude norm, commutator and even-parity connector statements. Do not infer any arithmetic saving. Produce a seven-section report and stop.

## Permitted context

- `protocol.md`
- `rounds/codex-managed/m9-m1-t1-complete-source-coefficient-mask-analysis/briefs/independent_statement_packet.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `strategy review and all claimant or historical derivations; read only protocol and the independent statement packet`

## Required controls

- `complete_source_multiplicity`
- `actual_coefficients_only`
- `literal_endpoint_zero_extension`
- `partition_recombination`
- `row_interval_vs_arithmetic_masks`
- `product_and_projective_norms`
- `even_parity_connector`
- `one_outer_real_part`
- `net_power_ledger`
- `no_capacity_lower_bound`
- `no_unverified_theorem_import`
- `protected_parent_and_exponent_scope`

## Required deliverables

- Seven-section protocol report with exact hypotheses, proof, first open step, controls, dependencies and state recommendation.
- No shared-state edits; stop after the assigned report.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
