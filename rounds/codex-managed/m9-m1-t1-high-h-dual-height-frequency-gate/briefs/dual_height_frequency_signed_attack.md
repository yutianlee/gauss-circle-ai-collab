# Task Brief: dual_height_frequency_signed_attack

- Campaign: `m9-m1-t1-high-h-dual-height-frequency-gate`
- Research round: `189` (`m9_m1_t1_high_h_dual_height_frequency_gate`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `338060b37c19d849053078e5f6a7775c45c626a16b6f9198fafdf9bb4a62265c`
- Generated: `2026-08-29T10:35:22.049689+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 95%.
- Numerical/experimental effort: at most 5%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the exact Round-188 complement be bounded by the dual height frequency j_q(a,v)=|a v^{-1}|_q: first prove the maximal coefficient-insensitive slow-frequency sector j_q(a,v)<=floor(mq/Y)=floor(U/Y) absolutely target-safe by projective residue sparsity and the exact 1/m Fourier-lift weight, then use the complementary dyadic j-ranges and only verified variation of the actual literal endpoint coefficient to gain the full factor Y, or isolate the exact coefficient-discrepancy obstruction?

## Reference formula and distinctions

Fix Q=H_B=floor((log(2X))^B), Y>Q, U=mq, k=ma, (a,q)=1. Bound Re C_(Y,Q)^sigma by O_(B,epsilon)(L^2X^epsilon), where C is exactly the Round-188 complement U=mq>4Q, q>Q, m|a|_q>Q, Qm<Y. Since q divides U divides u=gU and (u,v)=1, define j_q(a,v)=|a v^{-1}|_q. Split before positivity into 1<=j_q(a,v)<=floor(mq/Y)=floor(U/Y) and j_q(a,v)>mq/Y, preserving every h,t,orientation and literal amplitude under one outer real part.

- The carrier, both orientations, every h,v,t,a,m,q,U, selector, squarefree and coprimality deletion, profile, endpoint, phase, sign, conjugation and zero extension are exactly K185.27 and K185.30--K185.35 as inherited through K187 and K188.
- At fixed (kappa,u,U), one has u,v asymptotic to L/kappa, q divides U divides u, Y<h<=2Y, O(kappa) live affine sites per oriented v-row, and coefficient mass sum over a units |c_q(a)|/m=O(log(2q)/m).
- For fixed a,m,q, v maps projectively to a v^{-1} modulo q. The slow set |a v^{-1}|_q<=floor(mq/Y) uses O(mq/Y) unit residue classes; because q divides u and the literal v-interval has length O(u), it should contain O(um/Y) possible v. The resulting factor m is cancelled exactly by c_U(ma)=m^(-1)c_q(a) before divisor summation.
- The slow dual-frequency sector must be summed with the exact kappa,u,m,q divisor ledger and no absorbed positive power of Y. Its exact complement remains a single signed aggregate.
- A geometric height estimate is admissible only after proving the needed discrete variation or discrepancy for the actual zero-extended A_(kappa,g,h,U,v,omega)^sigma. Squarefree, coprimality, residual-selector, profile and endpoint jumps may not be suppressed or replaced by an arbitrary smooth weight.
- The prime-conductor survivor K_p^circ(b)=E_p(b) has height-prefix discrepancy (p-1)/2 at the projective slope b=-2; this is a falsifier of any uniform polylogarithmic height-prefix claim, not a lower bound for the literal aggregate.
- Even complete success closes only the exact original-t=1 residual through prior connectors. Every original t>=2 small-G incidence and the large-G near-resonant complement remain open.

## Assigned target

Derive the exact dual frequency j_q(a,v)=|a v^{-1}|_q on the Round-188 complement. Prove the widest complete target-safe projective-resonance sector, beginning with j_q(a,v)<=floor(mq/Y)=floor(U/Y), using both projective sparsity and the exact 1/m lift weight with exact multiplicity and divisor powers. Then attack the complementary dyadic j-ranges by summation in h or a joint (h,v) transform using only a verified discrepancy norm of the actual literal endpoint aggregate; otherwise isolate the first exact missing relation and its power deficit.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/round189_m1_t1_high_h_dual_height_frequency_strategy.md`
- `proofs/kernels/m9_m1_hard_top_t1_high_h_imprimitive_lift_gcd_reduction.md`
- `proofs/kernels/m9_m1_hard_top_t1_high_h_inverse_residue_conductor_reduction.md`
- `proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md`
- `rounds/codex-managed/m9-m1-t1-high-h-imprimitive-lift-gcd-gate/reports/imprimitive_lift_signed_attack.md`
- `rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/reports/literal_height_fourier_attack.md`

## Required controls

- `exact_round188_Qm_lt_Y_complement`
- `literal_K185_27_30_35_carrier`
- `single_outer_real_part_and_both_orientations`
- `dual_frequency_j_abs_a_v_inverse_mod_q`
- `projective_residue_bijection_and_two_sided_count`
- `q_divides_U_divides_u_v_interval_multiplicity`
- `per_v_O_kappa_affine_sites`
- `exact_cU_m_inverse_cq_normalization`
- `slow_j_le_floor_U_over_Y_sector_and_exact_complement`
- `full_factor_Y_before_positive_recombination`
- `kappa_u_m_q_divisor_power_ledger`
- `centered_exact_conductor_identity`
- `selector_squarefree_coprime_deletions`
- `profile_endpoint_phase_zero_extension`
- `no_invented_height_BV_or_periodicity`
- `original_t1_only_downstream_scope`
- `exponent_quarantine`

## Required deliverables

- A seven-section analytical report satisfying the repository report contract.
- An exact dual-frequency split, projective residue count, restored power ledger, proved strict sector and exact signed complement.
- A complete target proof or the first rigorously isolated actual-coefficient height-discrepancy relation with quantitative deficit.
- Write only the assigned report and any explicitly named diagnostic under this campaign; make no graph or shared-state edit.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
