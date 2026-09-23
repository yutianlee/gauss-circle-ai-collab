# Task Brief: blind_lift_gcd_rederivation

- Campaign: `m9-m1-t1-high-h-imprimitive-lift-gcd-gate`
- Research round: `188` (`m9_m1_t1_high_h_imprimitive_lift_gcd_gate`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `be0eca9ca93c3534cca958d70b5541d03d28ff993ebfbcbca6be3cd393fae5ff`
- Generated: `2026-08-29T08:32:17.913983+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 95%.
- Numerical/experimental effort: at most 5%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the exact Round-187 high-conductor complement be bounded by sharpening the fixed-(kappa,u,U) atom count to one dyadic height block, thereby proving every sufficiently imprimitive Fourier lift Q(k,U)>=Y target-safe, and can the remaining primitive or moderately imprimitive packet be controlled by a genuinely signed reciprocity, completion, or determinant mechanism without inventing variation of the literal amplitude?

## Reference formula and distinctions

Fix Q=H_B=floor((log(2X))^B) and Y>Q. Bound Re R_(Y,Q)^sigma by O_(B,epsilon)(L^2X^epsilon), where R is exactly K187.7 restricted to U>4Q, q_U(k)=U/(k,U)>Q, and |k|_U>Q. Put m=(k,U), so U=mq, k=ma, (a,q)=1, c_U(k)=m^(-1)c_q(a). First test the exact sector Qm>=Y and retain the exact complementary joint aggregate Qm<Y under the same single outer real part.

- The carrier, both orientations, all h,v,t,k, selectors, squarefree and coprimality deletions, profiles, endpoints, phase, signs, and zero extensions are exactly K185.27 and K185.30--K185.35 as inherited through K187.1--K187.11.
- The exact high packet has U>4Q, q_U(k)>Q, and |k|_U>Q. The lift variable is m=(k,U)=U/q_U(k), with unique U=mq and k=ma for a unit modulo q.
- On a single dyadic height block, the predicted fixed-(kappa,u,U) live-atom count is O(YL), not the all-height O(UL) count. This and exact-conductor mass O(log(2q)/m) must be proved before any target-safe lift claim.
- The proposed strict lift sector is Qm>=Y. Its exact complement has Qm<Y and must retain one outer real part over all remaining labels until a signed estimate is proved.
- The complete positive capacity is O(YL^2X^epsilon), while the target is O(L^2X^epsilon). Fixed polylogarithmic losses may be rebudgeted, but no positive power of Y may be absorbed.
- Reciprocity, height completion, determinant transposition, or a squarefree-sieve opening is admissible only with every literal weight and hypothesis verified. Raw reflection, arbitrary-weight large sieve, positive transform energy, and assumed periodicity or bounded variation are forbidden shortcuts.
- Even complete success closes only the exact original-t=1 residual through prior connectors. Every original t>=2 small-G incidence and the large-G near-resonant complement remain open.

## Assigned target

Independently derive the exact Fourier-lift decomposition of the stated high packet, the sharpest target-safe lift-gcd sector obtainable from the dyadic atom count, and the first remaining signed relation, using only the self-contained statement packet.

## Permitted context

- `protocol.md`
- `rounds/codex-managed/m9-m1-t1-high-h-imprimitive-lift-gcd-gate/blind_statement.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `state/active_campaign.yml`
- `all strategy files`
- `all source cards and web-search results`
- `all prior round reports, reviews, controls, candidates, kernels, and synthesis`
- `all Round-188 sibling reports, reviews, controls, and conductor analysis`

## Required controls

- `exact_round187_high_packet`
- `literal_K185_27_30_35_carrier`
- `single_outer_real_part_and_both_orientations`
- `unique_U_mq_k_ma_lift_coordinates`
- `exact_cU_m_inverse_cq_normalization`
- `dyadic_fixed_kappa_u_U_atom_count`
- `triple_divisor_convolution_power`
- `Qm_ge_Y_sector_and_exact_complement`
- `full_factor_Y_before_positive_recombination`
- `selector_squarefree_coprime_deletions`
- `profile_endpoint_phase_zero_extension`
- `no_invented_height_or_residue_variation`
- `no_positive_large_sieve_Poisson_alias_energy`
- `false_unsigned_and_adversarial_controls`
- `original_t1_only_downstream_scope`
- `exponent_quarantine`

## Required deliverables

- A seven-section statement-only report satisfying the repository report contract.
- An independent normalization, multiplicity and dyadic-power derivation, exact sector/complement, and first unproved signed relation.
- A proof or rigorous no-go without inferring hidden regularity for the fixed literal amplitude.
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
