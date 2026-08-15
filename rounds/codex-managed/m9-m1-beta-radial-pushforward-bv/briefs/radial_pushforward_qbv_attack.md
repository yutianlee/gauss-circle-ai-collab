# Task Brief: radial_pushforward_qbv_attack

- Campaign: `m9-m1-beta-radial-pushforward-bv`
- Research round: `27` (`beta_radial_pushforward_bv`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `8a92f4ad5e1067f9e184baa0d85c6eb71b1e1f2eee76261f66b6b437a5e27cac`
- Generated: `2026-08-12T21:18:58.136919+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

For the hierarchical beta branch Theta_beta=psi(beta), can the double-bounded share and recombined E1+R1 contour displacement be made exact and target-safe, and can the remaining positive-alpha piece be reduced to a radial theta-pushforward with integrable uniform q-BV so that the accepted logarithmic character-kernel lemma proves normalized O_epsilon(X^epsilon), or is there a rigorous obstruction?

## Reference formula and distinctions

Use 1=psi(beta)+(1-psi(beta))psi(alpha)+(1-psi(beta))(1-psi(alpha)). In the beta component apply the accepted Cauchy-Green identity to the complete recombined radial integrand, not isolated R1. In the positive-alpha saddle use alpha_0=pi q sqrt(Xx)/D_j, theta_j(x)=pi sqrt(Xx)/D_j, and the accepted q^0 character kernel. Preserve the actual W_j, phi, H_j+1 floors, top half-star, finite outside sides, and external -(4/pi)X^(1/4) normalization.

- the double-bounded beta share
- the recombined E1+R1 finite connector displacement and full A=0 residue
- the positive-alpha saddle/transition decomposition
- the radial phase pushforward theta_j(x)
- the complete theta-dependent discrete q-BV norm
- hard top Hilbert-pole and smooth interior contributions
- finite sides, endpoints, and signed/unsigned/adversarial controls

## Assigned target

Derive the uniform positive-alpha stationary/transition decomposition, exact radial theta-pushforward, and complete actual-profile q-BV norm for the hierarchical beta branch. Prove the normalized bound using the accepted character-kernel lemma, or isolate the smallest quantitative obstruction. Separate smooth interior scales from the hard top Hilbert pole.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `proofs/kernels/m9_m1_beta_character_dirichlet.md`
- `rounds/codex-managed/m9-m1-diagonal-transition-exhaustion/synthesis.md`
- `rounds/codex-managed/m9-m1-beta-transition-connector/synthesis.md`
- `rounds/codex-managed/m9-m1-beta-transition-connector/reports/beta_physical_kernel_attack.md`
- `rounds/codex-managed/m9-m1-upper-endpoint-character-abel/synthesis.md`
- `rounds/codex-managed/m9-m1-r1-arithmetic-residue/synthesis.md`

## Required controls

- `signed-vs-unsigned`
- `coefficient-adversary`
- `support-and-degeneracy`
- `exact-vs-near-resonance`
- `residue-and-normalization`

## Required deliverables

- Exact stationary/transition and theta-pushforward formula
- Complete-profile q-BV theorem or quantitative obstruction
- Separate hard-top and smooth-interior verdicts
- Seven-section report at the assigned path

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
