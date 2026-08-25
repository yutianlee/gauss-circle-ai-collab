# Task Brief: zero_mode_local_factor_attack

- Campaign: `m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate`
- Research round: `156` (`m9_m1_lower_cone_t1_d1_outer_defect_zero_mode_gate`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `f9866ea08923ae28f9631e503d2a5eb6be3cd85a09eb05505deec2903d1658b6`
- Generated: `2026-08-25T04:50:16.174351+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

For the exact v=0 row of the D=d=L=1 signed outer-defect theta completion beyond every fixed polylogarithmic collar, can the zero-frequency theta multiplier be evaluated into primitive or induced real-character local factors and then summed against the literal Bhat_j(0) to prove the X^epsilon target or a strict owner-complete positive-power range; if not, what is the first exact conductor, valuation-support, squareful, profile-variation, endpoint, source, or restored-power obstruction?

## Reference formula and distinctions

Fix A>0, q=4N, J_A=M^(3/4)(log(2X))^A, K=sqrt(NM), and J_A<V<=K. For every odd d|N put c=4N/d. The frozen row is -i(1+i)/(2Nq) sum_(V<|j|<=2V) sum_(d|N,d odd) chi_4(d)d sqrt(c) Bhat_j(0)K(0,-j;c), where K(0,-j;c)=sum_(a mod c)^* epsilon_a(c/a)e_c(-aj), and Bhat_j(0)=sum_(x mod q)B_j(x) retains the literal pre-linearization profile, cell, mask, transitions, and endpoints.

- Retain arbitrary N, every odd d|N, c=4N/d, both signs of j, the strict dyadic mask, actual profile, zero extension, asymmetric cell, transitions, hard endpoints, and external B_(1,U)(1) seam.
- The accepted selected linearization is not licensed on the ambient B_j; use the exact residual phase in the zero row.
- Prove epsilon_a=(1+i)/2+(1-i)chi_4(a)/2 and decompose K(0,-j;4m) exactly, then derive rather than assume the primitive conductors of (m/a) and chi_4(a)(m/a).
- Classify every prime-power Fourier transform, including p=2, induced-modulus multiplicity, principal-character case, squareful degeneration, nonvanishing valuation of j, phase, and magnitude.
- Restore the exterior d sqrt(c)/(2Nq), all d, the number and location of surviving j, and every Bhat_j(0) variation or endpoint cost before assigning a power.
- Direct interchange of j and a, Gauss evaluation, partial summation, Polya--Vinogradov, Burgess, conductor lowering, and divisor switching must be tested with their literal hypotheses.
- Complete v-resummation, termwise DFI, physical-diagonal-only Parseval, bare flat-j localization, and the hypothetical V<=M^(3/2) capacity are frozen as gains.
- Support counts, local magnitudes, character-sum bounds, and theorem right sides are upper capacities, not signed lower bounds.
- A zero-row theorem does not automatically control the nonzero matrix or any D>1, L>1, generic, t>=2, cross, M2, endpoint, M9, bridge, target, or exponent owner.

## Assigned target

Derive the exact primitive and induced-character local factorization of K(0,-j;4N/d), including every odd prime power, the full two-adic factor, squareful and principal degeneracies, nonvanishing valuations of j, exact phases, and the d-sum. Then attack the literal weighted zero row using its actual Bhat_j(0) variation. Prove the target, a strict owner-complete range, or the first exact arithmetic, profile, endpoint, or restored-power obstruction.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/round156_d1_outer_defect_zero_mode_strategy.md`
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/barrier_packet.md`
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/candidates/conductor_round156_zero_mode_seed.md`
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/reviews/conductor_round155_adjudication.md`
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/reports/outer_defect_spectral_dispersion_attack.md`
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/candidates/conductor_round154_root_dispersion_adjudication.md`

## Required controls

- `literal_zero_mode_row`
- `exact_epsilon_two_character_decomposition`
- `primitive_conductor_and_induced_modulus`
- `all_prime_power_two_adic_local_factors`
- `valuation_support_and_squareful_strata`
- `d_sum_and_full_normalization`
- `actual_Bhat0_j_variation`
- `positive_negative_defect_and_endpoints`
- `N_M_V_d_conductor_power_ledger`
- `upper_capacity_vs_signed_sum`
- `nonzero_and_downstream_scope`

## Required deliverables

- A seven-section analytic report.
- Exact local formulas and a completely restored weighted zero-row ledger.
- A target proof, strict owner-complete range, or first rigorous arithmetic or analytical obstruction.
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
