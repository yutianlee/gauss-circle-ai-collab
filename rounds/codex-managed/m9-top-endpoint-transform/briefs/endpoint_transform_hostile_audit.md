# Task brief: hostile endpoint-transform audit

Campaign: `m9-top-endpoint-transform`  
Task: `endpoint_transform_hostile_audit`  
Role: hostile falsifier  
Graph SHA-256: `7b5a7c93190fa88305d91bb1f2e64788921fe2f4cbbd02eddb8e60e654d64d58`

Read `protocol.md`, `state/proof_obligations.yml`, `state/active_campaign.yml`,
the Round-7 profile and hostile reports, and the Round-5 smooth transform.
Do not edit shared state. Write only
`rounds/codex-managed/m9-top-endpoint-transform/reports/endpoint_transform_hostile_audit.md`.

## Objective

Independently try to falsify the proposed endpoint mechanism before reading
the other Round-8 task reports. In particular:

1. determine the exact minimum of
   \(\operatorname{dist}(hX/(4y^2),\mathbb Z)\) for odd
   \(h\le yX^{-1/4}\), uniformly over \(y^2\le X<(y+1)^2\);
2. test whether a stationary point can approach the endpoint at its natural
   stationary width;
3. derive the correct one-sided Poisson half-weight and identify any
   conditionally convergent boundary series;
4. audit whether the endpoint term is \(O(1)\), \(O(\log H)\), or larger
   after actual beta weights;
5. construct a lowest/highest-frequency or near-square countermodel to any
   unjustified uniform error estimate.

Analytical proof is required. A bounded exact computation may falsify a
constant but cannot validate the asymptotic statement.

The report must contain the first false/doubtful step, exact surviving
lemma or no-go result, controls, dependencies, and recommended state effect.
