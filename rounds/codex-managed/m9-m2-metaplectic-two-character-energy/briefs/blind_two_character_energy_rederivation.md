# Task Brief: blind_two_character_energy_rederivation

- Campaign: `m9-m2-metaplectic-two-character-energy`
- Research round: `108` (`m9_m2_metaplectic_two_character_energy_core`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `7347081c1a765acafc6a4d1e3a96171d7b971079c2af144f7a0eaa825309bb2a`
- Generated: `2026-08-17T12:52:26.296611+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 90%.
- Numerical/experimental effort: at most 10%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can exact Gaussian linearization of the complete metric chirps and the two-character factorization in the physical square-root variables prove the missing rho^(-1/2) linear gain in the residual hard M2 Gram, or is the resulting metaplectic/theta representation an equal-capacity return?

## Reference formula and distinctions

G_H^act=sum_(a,n)|sum_(0<=j<H)(-1)^j F_a(n+j)|^2 <<_eps X^eps H^2 E_0/rho, with E_0 asymp L J D^2 and rho=A J D^3/L^3; for alpha!=0, e(alpha y^2)=e(sgn(alpha)/8)(2|alpha|)^(-1/2) int_R e(-t^2/(4alpha)+ty)dt, while the metric density alpha=0 is retained separately.

- J=X^(1/2), b=a+2q, h=ga, s=gb, Lambda=X(sqrt(b)-sqrt(a))^2/2
- Ju_ang/(1-u_ang)<k<2Ju_ang/(1+u_ang), G asymp L/A, K asymp JD/A
- positive hard-block capacity L^2 X^eps sqrt(rho); required energy gain rho^(-1)
- the density mode and every nonzero metric mode form one complete coefficient
- the arbitrary-coefficient and unsigned analogues are false controls

## Assigned target

Independently derive the exact Gaussian separation, the weakest sufficient two-character energy inequality, and a capacity/no-go test from the frozen statement only.

## Permitted context

- `problems/gauss_circle.md`
- `state/control_models.md`
- `rounds/codex-managed/m9-m2-metaplectic-two-character-energy/blind_statement.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `strategy files`
- `Round-108 derivation packet and conductor candidate`
- `all Round-108 sibling reports and earlier claimant derivations`

## Required controls

- `gaussian_constant_and_density_limit`
- `metric_density_discrepancy_jointness`
- `actual_symbol_vs_arbitrary_coefficients`
- `transform_inversion_and_capacity`
- `rho_power_and_endpoint_ledger`

## Required deliverables

- A seven-section statement-only report at the assigned path.
- An exact lemma or no-go result, proof, first doubtful step, and control outcomes.
- The weakest sufficient transformed inequality with every normalization visible.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
