# Task brief: one-sided Poisson derivation

Campaign: `m9-top-endpoint-transform`  
Task: `one_sided_poisson_derivation`  
Role: analytic deriver  
Graph SHA-256: `7b5a7c93190fa88305d91bb1f2e64788921fe2f4cbbd02eddb8e60e654d64d58`

Read `protocol.md`, `state/proof_obligations.yml`, `state/active_campaign.yml`,
the Round-7 profile report, and the Round-5 smooth dual transform. Do not edit
shared state. Write only
`rounds/codex-managed/m9-top-endpoint-transform/reports/one_sided_poisson_derivation.md`.

## Objective

Let \(y=\lfloor\sqrt X\rfloor\),
\(w_{\rm end}(d)=W(d/y)\mathbf1_{d\le y}\), with the accepted fixed
profile satisfying \(W(1)=1\), and let
\(1\le h\le H_y=\lfloor yX^{-1/4}\rfloor\) be odd. Derive a rigorous
one-sided Poisson/stationary-phase formula for

\[
S_h=\sum_{d\le y}W(d/y)e(hX/(4d)).
\]

State the endpoint half-weight convention and isolate the full boundary
contribution. Prove or refute a uniform lower bound for
\(\operatorname{dist}(hX/(4y^2),\mathbb Z)\). Determine whether stationary
points are uniformly separated from \(u=1\), and sum every error after
inserting the actual Vaaler factor \(\Phi(h/(H+1))/h\).

If the result is a truncated dual cone, give its exact lattice condition,
leading amplitude, phase, symbol regularity, and boundary term. Decide
whether this closes the full top M2 block or only reduces it.

Required controls: \(X=y^2\), \(X=(y+1)^2-1\), \(h=1\), \(h\asymp H_y\),
both frequency signs, and the distinction between full endpoint weight and
Poisson midpoint weight.

The report must contain result, exact hypotheses, proof, first unproved
step, controls, dependencies, and recommended state effect.
