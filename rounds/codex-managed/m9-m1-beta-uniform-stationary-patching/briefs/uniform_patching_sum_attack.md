# Task Brief: uniform_patching_sum_attack

- Campaign: `m9-m1-beta-uniform-stationary-patching`
- Research round: `28` (`beta_uniform_stationary_patching`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `e2ee85737b2be860789ded13d5526e81239002ff9debb2fb8edcaf5b44644e3e`
- Generated: `2026-08-12T22:26:54.947198+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the separated post-endpoint q^(-2) hard-top gain be extended uniformly through positive-alpha saddle entry and exit, nonstationary zones, and the exact artificial-rho recombination, and can the resulting actual-profile terms be summed over q, h, scales, radial endpoints, and finite sides at normalized O_epsilon(X^epsilon)?

## Reference formula and distinctions

Start from R1=omega G+(1-omega)R1-omega E1, alpha_0=pi q sqrt(Xx)/D_j, and the physical top split (a+i mu)^(-1)=pi delta_0(mu)-i PV(1/mu). The accepted interior bound is (D_j/q) alpha_0 C_PV << D_j/(q alpha_0)=D_j/(q^2 theta_j(x)) only where the saddle is separated from entry, exit, and rho=0. Derive a uniform endpoint-stationary normal form rather than extending this estimate by assertion.

- exact finite alpha integration range and stationary point
- entry and exit transition parameters and half-Fresnel terms
- nonstationary positive- and negative-alpha zones
- signed PV/delta convolution before absolute estimates
- omega-G and omega-E1 artificial-pole seam
- actual smooth interior and one-sided hard-top profiles
- complete q, h, dyadic-scale, and radial sums
- radial endpoints and finite outside u/v sides
- normalized O_epsilon(X^epsilon) beta bound or sharp obstruction

## Assigned target

Prove a uniform beta stationary-transition estimate preserving the accepted q^(-2) interior gain, then execute the complete actual-profile q, h, scale, radial, endpoint, and finite-side sums. If closure fails, isolate the smallest explicit kernel with its exact capacity.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-m1-vector-hankel-kernel/synthesis.md`
- `rounds/codex-managed/m9-m1-diagonal-transition-exhaustion/synthesis.md`
- `rounds/codex-managed/m9-m1-radial-endpoint-renormalization/synthesis.md`
- `rounds/codex-managed/m9-m1-beta-transition-connector/synthesis.md`
- `rounds/codex-managed/m9-m1-beta-radial-pushforward-bv/synthesis.md`
- `rounds/codex-managed/m9-m1-beta-radial-pushforward-bv/reports/pushforward_bv_hostile_audit.md`

## Required controls

- `signed-vs-unsigned`
- `coefficient-adversary`
- `support-and-degeneracy`
- `exact-vs-near-resonance`
- `residue-and-normalization`
- `endpoint-uniformity`

## Required deliverables

- Uniform patching proof and complete sum, or the first exact quantitative survivor
- Separate smooth-interior and hard-top verdicts
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
