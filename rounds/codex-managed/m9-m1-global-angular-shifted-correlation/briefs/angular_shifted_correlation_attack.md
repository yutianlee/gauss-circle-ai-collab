# Task Brief: angular_shifted_correlation_attack

- Campaign: `m9-m1-global-angular-shifted-correlation`
- Research round: `54` (`global_angular_shifted_correlation`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `ee2e84080cef5a9a49fd9a573f3ee0f1e14c3ec5032db3cca8fb5a50bc97ef22`
- Generated: `2026-08-13T17:25:30.674103+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Does one coefficient-preserving Fejer/van-der-Corput step convert the exact global angular radial sum into an averaged signed shifted-divisor correlation with target capacity, or what sharp obstruction remains?

## Reference formula and distinctions

S_X=sum_(n<=16sqrt X)^* A_X(n)n^(-3/4)e(sqrt(Xn)), A_X(n)=sum_(h|n,q=n/h odd)chi_4(q)Omega_X^*(n,h).

- finite Fejer or van der Corput inequality
- shifted phase sqrt(X)(sqrt(n+r)-sqrt n)
- exact coefficient correlation A_X(n+r) conjugate(A_X(n))
- additive incidence h_1q_1-h_2q_2=r
- R and N exponent ledger
- endpoint and angular stars
- spectral or shifted-convolution theorem hypotheses
- transfer back to the projected alpha operator

## Assigned target

Derive and optimize the exact coefficient-preserving shifted-correlation inequality for the global angular radial sum; prove a target range or isolate the first sharp survivor.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-m1-global-angular-shifted-correlation/derivation_packet.md`
- `rounds/codex-managed/m9-m1-alpha-coupled-dyadic-difference/synthesis.md`
- `rounds/codex-managed/m9-m1-dual-r2-recombination/synthesis.md`
- `rounds/codex-managed/m9-m1-ordered-denominator-resonance-cells/synthesis.md`
- `rounds/codex-managed/m9-m1-near-product-character-kernel/synthesis.md`

## Required controls

- `exact_differencing`
- `real_part_scope`
- `shifted_incidence`
- `coefficient_ownership`
- `endpoint_stars`
- `R_N_exponents`
- `absolute_capacity`
- `alpha_transfer_scope`
- `downstream_scope`

## Required deliverables

- seven-section report
- exact shifted kernel
- sufficient averaged theorem or no-go

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
