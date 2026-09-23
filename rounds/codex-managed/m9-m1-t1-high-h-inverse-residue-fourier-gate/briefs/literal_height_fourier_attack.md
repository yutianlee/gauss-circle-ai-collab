# Task Brief: literal_height_fourier_attack

- Campaign: `m9-m1-t1-high-h-inverse-residue-fourier-gate`
- Research round: `187` (`m9_m1_t1_high_h_inverse_residue_fourier_gate`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `d1ace6e362a41f1a08fc09c8e44ce628758040fa91ae39c152113c275f76352a`
- Generated: `2026-08-28T02:05:35.763384+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 90%.
- Numerical/experimental effort: at most 10%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the exact one-sided dyadic high-height tangent-gcd aggregate be bounded by L^2 X^epsilon through a genuinely joint inverse-residue Fourier mechanism, can a strict target-safe zero/low-frequency or nonresonant sector be proved with an exact centered complement, or does literal arithmetic deletion force an exact capacity or self-return obstruction?

## Reference formula and distinctions

For every fixed B>0, every real X>=2, every literal middle or lower residual hard-M1 shell L>=2, sigma in {+1,-1}, and every nonempty dyadic Y<h<=2Y with Y>H_B=floor((log(2X))^B), prove the one-sided inequality Re sum_(omega in {+,-}) sum_(f=(kappa,g,h,U,v) satisfying K185.27, Y<h<=2Y) (-1)^(S_(0,omega)) sum_(t in I_(f,omega)) (-1)^t B_(f,omega)^sigma(t) <<_(B,epsilon) L^2 X^epsilon, with all quantities exactly K185.27 and K185.30--K185.35.

- There is one outer real part over both orientations, every primitive row, every affine index, and every literal endpoint field; the theorem is one-sided and no lower bound for a negative dyadic real part is required.
- The invariant domain is kappa,g,h,U,v>0, kappa,g,U odd, (gU,v)=1, (U,h)=1, and 0<2 kappa g h<R_0=ceil(L), with the separate U=1 anchor convention retained.
- For U>1 the exact anchor is E_U(+bar(v)h) in the plus orientation and E_U(-bar(v)h) in the minus orientation, where E_U(a)=(-1)^[a]_U and E_U(a)=U^(-1) sum_(k mod U) hat(E)_U(k)e(ka/U), hat(E)_U(k)=2/(1+e(-k/U)).
- The fresh mechanism must retain the centered nonzero Fourier modes jointly over h, v, t, both orientations, selectors, deletions, endpoints, and phases before any positive norm. Splitting off a target-safe zero mode is not itself a proof of the complement.
- Positive capacity is O(Y L^2 X^epsilon) and the target is O(L^2 X^epsilon), so the full factor Y must be recovered before any positive row, orientation, frequency, gcd, selector, or endpoint recombination.
- A strict sector must carry an exact complementary signed aggregate. Even complete success closes only the exact original-t=1 residual after accepted connectors; every original t>=2 small-G incidence and the large-G near-resonant complement remain open.

## Assigned target

Attack the complete one-sided dyadic high-h target by the exact U-anchor Fourier expansion. Prove the full estimate, prove the widest target-safe zero/low-frequency or genuinely nonresonant signed sector with its exact complement, or isolate the first literal nonzero-mode estimate that remains and quantify its full power deficit.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/round187_m1_t1_high_h_inverse_residue_fourier_strategy.md`
- `proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md`
- `proofs/kernels/m9_m1_hard_top_t1_comparable_factor_exchange_sector_and_residual_fejer_reduction.md`
- `rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/reports/literal_residual_fejer_tangent_gcd_attack.md`
- `rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/reports/tangent_gcd_transfer_capacity_audit.md`
- `rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/synthesis.md`
- `rounds/codex-managed/full-proof-round183-185-strategy-literature-review/reviews/conductor_round186_adjudication.md`

## Required controls

- `exact_one_sided_outer_real_part`
- `literal_K185_27_30_35_carrier`
- `both_orientations_and_sigma`
- `primitive_domain_and_multiplicity_one`
- `U1_anchor_convention`
- `selector_squarefree_coprime_deletions`
- `profile_endpoint_phase_zero_extension`
- `inverse_residue_fourier_normalization`
- `height_zero_mode_power`
- `centered_nonzero_modes_remain_joint`
- `full_factor_Y_before_positive_recombination`
- `no_positive_Poisson_alias_energy_or_conductor_self_return`
- `false_unsigned_and_adversarial_controls`
- `original_t1_only_downstream_scope`
- `exponent_quarantine`

## Required deliverables

- A seven-section analytical report satisfying the repository report contract.
- Exact formulas for the U=1, zero-mode, and centered nonzero-mode pieces, with restored dyadic power ledgers and an exact complement.
- A complete target proof, a strict target-safe sector, or a rigorous scoped no-go with the first unproved literal estimate stated exactly.
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
