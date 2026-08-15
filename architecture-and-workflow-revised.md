# Revised Research Architecture

## Decision

The fixed A1/A2/A3/A4 collaboration is retired. New work uses Codex as the persistent conductor and temporary, function-specific subagents. Reasoning proceeds through numbered rounds designed, monitored, and closed by the conductor. Old rounds remain immutable evidence.

This redesign adopts transferable process ideas from Anthropic's zeta project and the evaluation in `C:/Users/yutia/Downloads/RH-strategy.md`; it does not import the zeta mathematics into the Gauss circle proof.

## Important correction about the precedent

Anthropic did not claim a proof of the Riemann Hypothesis. Its announced result is an unconditional improvement in proportions of zeta zeros known to be on the critical line, with separate distinctness and simplicity statements. Anthropic explicitly says the result has no bearing on RH in either direction and that it does not expect these techniques to prove RH.

The useful precedent is therefore the proof-development process: many isolated attempts, persistent failure memory, counterexample search, independent reproof, human review, and formalization of the stable finite kernel.

Primary references:

- Anthropic, [Learning more about Claude's mathematical capabilities](https://www.anthropic.com/research/riemann-zeta)
- [Research paper](https://www-cdn.anthropic.com/564f962e60643842f5fcb4a17c9dbc8f608f1c37.pdf)
- [Process appendix](https://www-cdn.anthropic.com/d7f3ecf1d01392d887f8bc974ca187e2a121b1ed.pdf)
- [Lean formalization repository](https://github.com/anthropics/zeta-23-lean)

## What is adopted

1. **Mathematical interfaces before delegation.** Freeze a narrow obligation and its exported statement before selecting subagents.
2. **Persistent hub, isolated spokes.** Codex maintains global proof state; temporary workers get minimal, explicit context.
3. **Failure as durable information.** Rejected claims become an anti-memory containing the exact obstruction a replacement must bypass.
4. **Countermodels as proof-unit tests.** Each mechanism is tested against false unsigned, adversarial-sign, boundary-scale, and degenerate analogues.
5. **Route validation around the claimant.** Reviewers inspect different seams, and a blind worker rederives important statements from the statement alone.
6. **Small proof kernel before exposition.** Synthesis waits until the kernel and its interfaces pass the validation matrix.
7. **Computation for destruction, not certification.** Numerical work seeks counterexamples and normalization errors; it never promotes an asymptotic claim.
8. **Early formalization.** Stable finite algebraic or combinatorial kernels are isolated before the analytic shell is polished.
9. **Strong reasoning for discovery and attack.** Expensive subagent work is reserved for creative lemmas, blind reproof, and hostile review, not repeated generic summaries.
10. **Provenance by construction.** Every brief and report records graph hash, context, task, role, dependencies, and status.

## What is not adopted

- No literal transfer of Weil forms, rank--trace inequalities, or zeta-zero arguments.
- No assumption that many subagents create independent statistical validation; correlated model error remains possible.
- No voting ensemble or fixed number of workers.
- No late literature check. Existing source-card discipline stays in force.
- No conductor-memory-only state. The proof-obligation graph and round ledger remain authoritative.
- No claim that formalization validates analytic estimates or external citations beyond the formalized kernel.

## Proof decomposition

| Interface | Current content | Required export |
|---|---|---|
| Reduction shell | H1--H4 and definitions | Exact $\mathcal M_1$, $\mathcal M_2$, coefficient conventions, and error budget |
| Residual shell | R5-Full | Uniform residual estimate with source dependencies explicit |
| M1 kernel | M9-M1 | Pointwise estimate uniform in the active dyadic $D$ range |
| M2 configuration side | $\beta$ algebra, exact $N=0$, near-collision taxonomy and obstructions | Precisely normalized signed and unsigned resonance quantities and multiplicity estimates |
| M2 global side | fourth/local moments, large values, transforms | A global statistic with exact coefficient weights and uniform exponents |
| Pointwise bridge | derivative/coherence and endpoint obligations | A valid implication from global control to $|\mathcal M_2(D;X)|\ll X^{1/4+\varepsilon}$ |
| Assembly | M9 and Conditional-bridge | Final implication only after M1 and M2 close |

The present mathematical diagnosis is that configuration taxonomy is comparatively mature while the pointwise bridge is missing. Ordinary global $L^4$ control is already known to be insufficient. Campaigns should seek the smallest sign-sensitive pointwise bridge or a precise no-go theorem, rather than accumulating undirected fourth-moment classifications.

## Operating cycle

```text
freeze exact obligation
  -> extract barriers and controls
  -> launch up to three orthogonal tasks
  -> select smallest candidate kernel
  -> review normalization / algebra / count / endpoint seams
  -> blind statement-only rederivation
  -> computational falsification and source audit
  -> conductor round-closing synthesis
  -> validate and apply State Patch
  -> update accepted proof draft
```

Only the conductor edits shared state. A subagent may write its assigned report or isolated computation directory but never the graph, validation matrix, synthesis, or accepted proof draft. It stops at the assigned round interface; the conductor alone designs the next round.

## Pilot: weighted-mass adjudication

The first campaign resolves whether a Round 9 conclusion concerns a raw tuple count or the actual $\beta$-weighted mass. It freezes all four quantities: raw count, $1/|h|$-weighted absolute mass, true signed mass, and unsigned mass.

Three tasks run independently:

1. a statement-only derivation of the best valid weighted upper bound;
2. a hostile search for a matching lower-bound family, lift multiplicity, truncation factor, or normalization loss;
3. an exact finite diagnostic across $D=X^{1/4}$, $X^{3/8}$, and $X^{1/2}$.

The conductor adjudicates only after separate reviews of definition/normalization, counting, coefficient summation, and endpoint uniformity. The $X^{3/8}$ split is retained, revised, or removed only through a validated graph patch.

## Repository transition

- Active: `AGENTS.md`, `protocol.md`, `state/active_campaign.yml`, `state/current_round.md`, `state/round_ledger.yml`, `math_collab/campaigns.py`, `state/control_models.md`, `state/validation_matrix.yml`.
- Authoritative: `state/proof_obligations.yml`.
- Derived: `state/next_campaign.md`, `state/failure_ledger.md`, `manifests/reading_packet.md`.
- Candidate kernels: `proofs/kernels/`.
- Active evidence: `rounds/codex-managed/`.
- Legacy evidence: old round trees, fixed-agent owner labels, web/API orchestrator, web configs, and clipboard scripts.

The transition changes research execution and validation, not the status of any mathematical claim.
