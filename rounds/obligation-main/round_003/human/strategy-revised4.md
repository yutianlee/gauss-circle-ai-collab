# Strategy-Revised4: Architecture And Route Audit

This note reassesses the current proof architecture after reading the obligation graph, proof draft, gap register, lemma bank, current state, and the active round materials. The reconstruction in the earlier answer was directionally right about the framework, but wrong about the ambition: this project is not merely chasing an incremental exponent. It is attempting the full conjectural target, namely theta = 1/4 in the X = R^2 variable, equivalently E(R) = O(R^(1/2+epsilon)), through a specific arithmetic route.

## 1. What The Strategy Is, And Where It Stands

The route is internally visible across the state:

```text
P(X) = N(sqrt(X)) - pi X
  -> symmetric Dirichlet hyperbola identity
  -> floor-compatible sawtooth formula
  -> finite Vaaler approximation of psi
  -> local dyadic chi_4-twisted reciprocal exponential sums.
```

The genuinely proved infrastructure deserves credit. H1 gives the symmetric hyperbola identity, H2 gives the exact partial-sum formula for chi_4, and H3 gives the balanced sawtooth formula with an exact O(1) residual. The structural obstructions H7 and H9 are also valuable: direct Weyl differencing destroys the chi_4 character, and the B-process dual phase has a Hessian degeneracy that blocks off-the-shelf two-dimensional stationary phase or decoupling.

The reduction itself is classical and moves the problem rather than solving it. After H1-H4, the difficulty is concentrated in M9: the fixed-coefficient reciprocal main sums M1 and M2 must be O_epsilon(X^(1/4+epsilon)) uniformly up to D = X^(1/2). That is the endpoint/self-dual scale. The current known-technology gap remains the right warning: the sums sit in the Li--Yang / Bombieri--Iwaniec reciprocal-sum world, but known record-scale technology does not reach theta = 1/4.

The strongest criticism in this note is about R5-Full. The conditional bridge uses H1-H3 + H4 + R5-Full + M9 => target, and `proof_obligations.yml` currently marks R5-Full as `derived_under_assumptions`. Earlier state text, however, identified the Fejer residual as a character-blind or parity-supported DDP-strength obstruction. If that older diagnosis is still correct, R5-Full is over-promoted. If the later product-count proof really resolves the fixed Fejer residual conditional on H4, then the state needs a clearer reconciliation explaining why this does not secretly solve a divisor-problem-strength endpoint. This is the highest-priority audit point.

The newer fourth-moment attack on M9-M2 is directionally right. Opening |S2|^4, clearing denominators to the resonance integer

```text
N = h1 d2 d3 d4 - h2 d1 d3 d4 + h3 d1 d2 d4 - h4 d1 d2 d3
```

and separating exact N = 0 structure from near-collisions is the correct Bombieri--Iwaniec/Bourgain--Watt style instinct. It also reveals the no-slack wall: the diagonal core is already at the conjectural fourth-moment size, so every off-diagonal or near-collision family must be controlled essentially sharply. That is why `M9-near-collision-estimate` remains the active bottleneck.

The process hygiene gap is real. `best_proof_draft.md`, `gap_register.md`, and `lemma_bank.md` are still sparse compared with the state and transcript history. The durable artifact should not be only the judge transcript. The proof draft needs the bridge, H4, R5-Full, M9 definitions, and the current gap list in one place.

## 2. Alternative Strategies Worth Tracking

**A. Retarget to a verified incremental exponent.** Keep the H1-H4 scaffold, reproduce the Li--Yang-style exponent within the repo's notation, and then test whether the second-spacing/additive-energy side can be sharpened. This is the highest-confidence way to produce a checkable mathematical deliverable, but it changes the project goal from the conjectural endpoint to an incremental record-style target.

**B. Mean-square and large-value leverage.** The fourth-moment work is already a small version of the mean-square/large-values philosophy behind modern record exponents. This route should be made theorem-level before it affects state: exact hypotheses, variable conventions, weights, loss factors, and the bridge to M9 are required.

**C. Exact Voronoi--Bessel / Hardy route.** The Vaaler residual difficulty suggests keeping an exact signed transform route alive. A Hardy--Voronoi/Bessel formulation avoids the positive Fejer majorant, but it must include amplitudes, boundary terms, dyadic truncation, character survival, and unsmoothing before it can replace the current route.

**D. Additive energy of sqrt(n).** The near-collision problem should be named directly as an additive-energy or spacing problem for square roots. This is a clean way to organize the M9-M2 fourth-moment taxonomy, even if known bounds are likely still too weak for theta = 1/4.

**E. Omega-side refutation rails.** Hardy--Landau, Heath-Brown distribution results, and Cramer mean-square information should be encoded as guardrails against any spurious sub-1/4 or endpoint-breaking claim. They do not prove the upper bound, but they are useful false-proof detectors.

## Recommendation

Use this note as a risk audit, not as an automatic route pivot.

Immediate state hygiene:

- A1 should consolidate H1-H4, R5-Full, the conditional bridge, M9 definitions, and current blockers into `best_proof_draft.md`.
- A2 should independently referee R5-Full against the older H5r/DDP-trap diagnosis and either confirm the later product-count proof or propose a validator-ready downgrade.
- A3 should keep diagnostics focused on fixed Fejer residuals, M9-M2 fourth moments, exact N = 0 families, and near-collision scaling.

Strategic posture:

- Keep the current `obligation-main` track focused on M9-M2 and exact-resonance/near-collision estimates.
- Do not replace the active route with Li--Yang, Voronoi--Bessel, or spectral machinery until a precise theorem-level bridge is written.
- Consider opening a separate incremental-exponent track only if the project owner explicitly wants a more attainable milestone than the conjectural theta = 1/4 endpoint.
