# Task Brief: blind_high_h_rederivation

- Campaign: `m9-m1-t1-high-h-inverse-residue-fourier-gate`
- Research round: `187` (`m9_m1_t1_high_h_inverse_residue_fourier_gate`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
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

Independently rederive the exact high-h primitive carrier and seek a one-sided L^2 bound, a strict complete signed sector, or the narrowest unavoidable obstruction, using only the self-contained statement packet.

## Permitted context

- `protocol.md`
- `rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/blind_statement.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `state/active_campaign.yml`
- `all strategy files`
- `all source cards and web-search results`
- `all prior round reports, reviews, controls, candidates, kernels, and synthesis`
- `all Round-187 sibling reports, reviews, controls, and conductor analysis`

## Required controls

- `exact_one_sided_outer_real_part`
- `literal_K185_27_30_35_carrier`
- `both_orientations_and_sigma`
- `primitive_domain_and_multiplicity_one`
- `U1_anchor_convention`
- `selector_squarefree_coprime_deletions`
- `profile_endpoint_phase_zero_extension`
- `affine_parity_and_terminal_dyadic_blocks`
- `inverse_residue_fourier_normalization`
- `height_zero_mode_power`
- `centered_nonzero_modes_remain_joint`
- `full_factor_Y_before_positive_recombination`
- `no_bare_alternation_or_rowwise_Abel`
- `no_positive_Poisson_alias_energy_or_conductor_self_return`
- `false_unsigned_and_adversarial_controls`
- `original_t1_only_downstream_scope`
- `exponent_quarantine`

## Required deliverables

- A seven-section statement-only report satisfying the repository report contract.
- An independent normalization, target/capacity derivation, exact safe pieces and complement, and first unproved relation.
- A proof, strict sector, or rigorous no-go; do not infer hidden regularity for the literal weights.
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
