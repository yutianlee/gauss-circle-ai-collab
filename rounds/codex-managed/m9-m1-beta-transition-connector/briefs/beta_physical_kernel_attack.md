# Task Brief: beta_physical_kernel_attack

- Campaign: `m9-m1-beta-transition-connector`
- Research round: `26` (`beta_transition_connector`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `dce19447a6adb9e776acc944d2b47f22d31eba1f8c2cfecbacac10565d699fdc`
- Generated: `2026-08-12T20:23:34.369996+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

For one fixed smooth beta-transition mask, can the exact finite character-high trace be shifted across A=0 with the Cauchy-Pompeiu connector and R1 residue reconciled, then returned to a physical mask-convolved chi_4 kernel of normalized size O_epsilon(X^epsilon)?

## Reference formula and distinctions

Set A=s-z/2 and B_+=s+z/2=A+z. The accepted beta-bounded factor is zeta(1-A)X_4(B_+)L(B_+,chi_4). For an even psi in C_c^infinity(R), psi=1 on [-B0,B0] and supported on [-2B0,2B0], derive the finite displacement from Re A=c'-Re z/2 to Re A=-kappa, including dbar psi(Im A), the crossed A=0 pole already represented by R1, all horizontal connectors, actual profiles/floors, and the external -(4/pi)X^(1/4) normalization.

- the shifted vertical beta trace
- the Cauchy-Pompeiu area connector or equivalent strip-edge connector
- the A=0 residue subtraction matched to Round 24
- the physical mask-convolved character kernel with radial integration and symmetric top-Hilbert factor
- signed actual-profile versus unsigned/adversarial controls

## Assigned target

Derive the exact physical mask-convolved chi_4 kernel for the shifted beta line plus connector and prove a target-sized bound, or isolate its smallest rigorous obstruction.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-m1-vector-hankel-kernel/synthesis.md`
- `rounds/codex-managed/m9-m1-diagonal-transition-exhaustion/synthesis.md`
- `rounds/codex-managed/m9-m1-r1-arithmetic-residue/synthesis.md`
- `rounds/codex-managed/m9-m1-partial-functional-equation-transitions/synthesis.md`

## Required controls

- `signed-vs-unsigned`
- `coefficient-adversary`
- `support-and-degeneracy`
- `exact-vs-near-resonance`

## Required deliverables

- Exact post-mask physical or Fourier-convolution kernel
- Normalized bound or quantitative obstruction
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
