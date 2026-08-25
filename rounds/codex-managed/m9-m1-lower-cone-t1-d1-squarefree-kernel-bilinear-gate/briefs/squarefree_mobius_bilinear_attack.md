# Task Brief: squarefree_mobius_bilinear_attack

- Campaign: `m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate`
- Research round: `153` (`m9_m1_lower_cone_t1_d1_squarefree_kernel_bilinear_gate`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `9ffef2e30c99d83d02d28141834b585d02dd77483fa7bfd8e572d45d6985fcc1`
- Generated: `2026-08-25T00:41:22.955757+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

For the exact large-defect, small-square-factor D=d=L=1 survivor P_U^* below M^449 asymp R^780, can squarefree Mobius inversion and a cancellation-preserving bilinear estimate prove |P_U^*|<<X^epsilon or a strict owner-complete range; if not, what is the first exact short-divisor, Type-I/Type-II, spacing, diagonal, endpoint, source, or all-scale obstruction?

## Reference formula and distinctions

Let N=floor(X), R=X^(1/4), 1<<M<=R^2, and M^449<<R^780. Round 152 proves P_U=P_U^*+O(X^epsilon), where P_U^* sums ell=tau s^2 with tau odd squarefree, 1<=s<ceil(M^(1/4)), and |k(ell)^2-Nell|>M^(3/4), retaining chi_4(tau), ell^(-3/4), the literal zero-extended actual profile, and B_(1,U)(1) outside the wave. For fixed s, mu^2(tau)=sum_(a^2|tau)mu(a), tau=a^2b, gives chi_4(b), phase e(as sqrt(Nb)), and A^2 B s^2 asymp M.

- Retain the exact actual profile, zero extension, support components, endpoints, transitions, tails, nearest-integer convention, large-defect mask, and external B_(1,U)(1) seam.
- The s=1 odd-squarefree layer is compulsory unless a conclusion is explicitly a strict s-range theorem.
- Every Mobius-inversion term, including a=1, and its sign must remain until a legal signed bilinear estimate or exact recombination is applied.
- On a~A and b~B, record A^2 B s^2 asymp M, raw count AB, actual M^(-3/4) weight, and common oscillatory scale sqrt(NM).
- Separately price large-a absolute tails, Type-I and Type-II blocks, the a=1 short-divisor seam, and every dyadic summation.
- If Cauchy is used in either variable, retain the surviving arithmetic coefficient and write the exact correlation phase, diagonal, exact collision, near-collision, and pigeonhole multiplicity.
- Exact frequency collisions for s sqrt(N)(sqrt(b_1)-sqrt(b_2)) must be classified before a large-sieve or spacing bound is claimed.
- A bound for each a separately inherits the Round-152 exponent-pair boundary unless cancellation across the complete Mobius sum is proved.
- The D>1 recovery fibre, L>1 rows, growing-M generic t=1 sector, every original t>=2 layer, and the independent Round-138 cross owner remain separate.

## Assigned target

Derive the exact fixed-s Mobius inversion of P_U^*, preserve every a including a=1, and attack the resulting linear-times-square-root bilinear form. Exhaust legal Type-I/Type-II splits, Cauchy placements, exact and near frequency collisions, large-a tails, and dyadic powers. Prove the target, a strict owner-complete range, or the first exact short-divisor, spacing, diagonal, or all-scale no-go.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/round153_d1_squarefree_kernel_bilinear_strategy.md`
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate/barrier_packet.md`
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/candidates/conductor_round152_square_root_wave_reduction.md`
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/reviews/conductor_round152_adjudication.md`
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/controls/conductor_round152_controls.md`
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/candidates/conductor_round148_squarefree_reciprocal_transform_and_dispersion_no_go.md`

## Required controls

- `literal_Pstar_survivor`
- `owned_range_and_owner_exclusion`
- `squarefree_kernel_uniqueness`
- `exact_Mobius_inversion`
- `a1_short_divisor_seam`
- `dyadic_A_B_s_power_ledger`
- `actual_profile_mask_and_B11`
- `Cauchy_coefficient_survival`
- `diagonal_and_pigeonhole_capacity`
- `exact_and_near_frequency_collisions`
- `TypeI_TypeII_signed_bilinear_target`
- `absolute_capacity_vs_signed_sum`
- `N_parity_endpoints_and_transitions`
- `D_L_generic_tge2_cross_and_downstream_scope`

## Required deliverables

- A seven-section analytic report.
- The exact Mobius-expanded identity and complete A-B-s power ledger.
- A target proof, strict owner-complete range, or first rigorous short-divisor, bilinear, spacing, diagonal, endpoint, or power obstruction.
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
