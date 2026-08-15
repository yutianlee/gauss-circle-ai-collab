# Task Brief: regular_symbol_bv_attack

- Campaign: `m9-m1-beta-regular-finite-part-symbol-bv`
- Research round: `31` (`beta_regular_finite_part_symbol_bv`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `fd2cf1bc11f8cba48bce0e3713473d96478500c219cc980b5467312ecc4f992c`
- Generated: `2026-08-12T23:46:02.226983+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Does the complete regular finite part, after removing the explicit delta jumps and q^(-4) face logarithms, satisfy the scale-normalized BV norm needed to retain the local q^(-2) beta gain through every actual profile and residue seam?

## Reference formula and distinctions

For each signed saddle with lambda=pi q sqrt(Xx)/D_j, expand the exact regular finite part from Delta_H(L,mu)=[H(L,L-mu)-H(L,L)]/mu inside the artificial-pole-safe combination omega G+(1-omega)R1-omega E1. Prove ||B||_infinity+||partial_y B||_1 << X^epsilon D_j/(q lambda) times the exact inherited h,D_j,x monomial in the exact Morse variable y, with endpoint traces and summable height tails.

- exact complete regular finite-part amplitude
- divided difference Delta_H and its L derivative
- scale-normalized Morse-variable BV norm
- moving affine endpoint traces
- omega G/R1/E1 derivative cancellation at rho=0
- v=0 axial and b downarrow zero loss
- actual dyadic profiles, floors, stars, and radial factors
- finite U,V,S height tails and q^(-2) normalization

## Assigned target

Expand the complete omega-recombined regular finite part, apply divided-difference and BV product estimates to every actual factor, and prove the scale-normalized symbol norm with endpoint traces and summable tails. If it fails, isolate the smallest explicit derivative term and quantify its exact power loss.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-m1-beta-transition-connector/synthesis.md`
- `rounds/codex-managed/m9-m1-beta-radial-pushforward-bv/synthesis.md`
- `rounds/codex-managed/m9-m1-beta-log-amplitude-two-saddle/synthesis.md`
- `rounds/codex-managed/m9-m1-beta-log-amplitude-two-saddle/reviews/conductor_symbol_derivative_scope.md`

## Required controls

- `product-rule-and-derivative`
- `moving-endpoint-traces`
- `residue-and-normalization`
- `profile-floor-star-uniformity`
- `height-exhaustion`
- `pointwise-versus-BV`

## Required deliverables

- Complete regular-symbol BV proof or smallest explicit offender
- Derivative, endpoint, q-power, tail, and normalization ledger
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
