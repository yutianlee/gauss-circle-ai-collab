# Task Brief: majorant_cross_term_hostile_audit

- Campaign: `m9-m2-unbalanced-one-sided-majorant-gate`
- Research round: `134` (`m9_m2_unbalanced_one_sided_majorant_gate`)
- Role: `seam_reviewer`
- Access mode: `selected_context`
- Graph SHA-256: `40e83c20e83d542e43aa739931f4b89ea76f4541506fb44ef219ce31dca35024`
- Generated: `2026-08-23T12:52:03.900299+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can a one-sided band-limited majorant, applied directly to the endpoint-complete full-character energy E_chi before any sectorwise modulus or positive-row norm, prove E_chi <<_epsilon X^(1/2+epsilon) uniformly on the literal flat-smooth strict-UNBAL packet; if not, what is the first exact order, bandwidth, character, or capacity obstruction?

## Reference formula and distinctions

B_(p,n)=sum_(0<=a<H)b_(p,n+a), E_chi=C_H sum_n |sum_(p>0 odd)chi_4(p)B_(p,n)|^2. With A(k)=sum_p chi_4(p)b_(p,k), D_H(alpha)=sum_(0<=a<H)e(a alpha), and Ahat(alpha)=sum_k A(k)e(k alpha), Parseval gives E_chi=C_H int_0^1 |D_H(alpha)|^2 |Ahat(alpha)|^2 d alpha. Test only lawful one-sided domination of this exact quadratic form or of its literal physical selectors.

- M asymp X, D=X^delta, L=X^ell, K=XL/D^2, H=ceil(X^(1/2)/D), K asymp LH^2
- 1/4<=delta<1/2, 0<=ell<delta-1/4, 178ell+1638delta>463, Q=D^2/(Lsqrt X) tending to infinity
- b_(p,k)=e(-1/8)M^(1/4)k^(-3/4)p^(-3/4)W((X/(2D))sqrt(p/(Mk)))q_L((X/M)p)e(sqrt(Mpk)) for positive odd p, zero-extended before shifts
- C_H=(J+H-1)/H^2 asymp L and D_0=C_H H sum_(p,k)|b_(p,k)|^2 << X^(1/2)
- E_chi is target-equivalent to the complete flat-smooth strict-UNBAL survivor modulo already-safe packages
- the Fejer multiplier F_H=|D_H|^2 is itself a nonnegative trigonometric polynomial of degree H-1 and integral H
- a meaningful bandwidth contraction must reduce degree below H by a fixed power without an L1, diagonal, endpoint, or owner loss
- Gamma_before=min(H,Q) for the best separate positive-row elementary bound, Gamma_claimed=1, and every surviving factor must be displayed
- flat-smooth strict-UNBAL owner only; hard, sharp, clipped, starred, arithmetic-owner, nonflat, and transition packets are excluded

## Assigned target

Hostilely audit every plausible one-sided majorant placement for order validity, complex cross terms, character retention, bandwidth uncertainty, diagonal capacity, Poisson ownership, and endpoint completeness.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/conductor_0823_full_proof_strategy.md`
- `strategy/A1_0823_2.md`
- `rounds/codex-managed/m9-m2-unbalanced-dual-offproduct-sector-gate/synthesis.md`
- `rounds/codex-managed/m9-m2-unbalanced-dual-offproduct-sector-gate/reports/blind_dual_offproduct_sector_rederivation.md`
- `rounds/codex-managed/m9-m2-unbalanced-dual-offproduct-sector-gate/reviews/conductor_round125_dual_sector_adjudication.md`
- `rounds/codex-managed/m9-m2-unbalanced-one-sided-majorant-gate/blind_statement.md`

## Required controls

- `literal_Echi_block_square_and_parseval`
- `majorant_order_relation`
- `Fejer_already_bandlimited`
- `zeroth_coefficient_uncertainty_bound`
- `bandwidth_and_L1_excess_capacity`
- `complex_cross_term_domination`
- `actual_chi4_before_modulus`
- `opposite_character_and_single_row_controls`
- `moving_profiles_zero_extension_and_endpoints`
- `Poisson_only_after_lawful_one_sided_inequality`
- `Gamma_before_claimed_survivor`
- `flat_smooth_owner_and_downstream_scope`

## Required deliverables

- A seven-section hostile report.
- A pass/fail matrix for every possible placement of the majorant.
- The maximal safe theorem or exact fatal correction and surviving power.
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
